# Deep Analysis: MongoDB Connector for Apache Iggy — Issue #2739

**Date**: 2026-02-16
**Issue**: https://github.com/apache/iggy/issues/2739
**Author of Issue**: @amuldotexe
**Status**: OPEN, feature, unassigned
**Analysis Method**: Parseltongue v1.7.2 (15,998 entities, 78,896 edges) + Web Research
**Codebase**: apache/iggy @ branch ab_202602_issue02

---

## PART 1: FIRST PASS ANALYSIS

### 1.1 What is Being Asked?

Issue #2739 requests a MongoDB connector for Apache Iggy — both Sink (Iggy -> MongoDB) and Source (MongoDB -> Iggy). The issue references a Discord conversation about competitor research, suggesting this is motivated by the ecosystem gap analysis (MongoDB is the #2 most-requested missing connector after MQTT).

### 1.2 Why MongoDB Matters for Iggy

From the ecosystem comparison (connector-ecosystem-comparison.md):
- **All 4 competitors** have MongoDB connectors (Kafka, Pulsar, Redpanda, NATS)
- MongoDB is the #1 NoSQL database globally
- IoT use case: sensor data -> Iggy -> MongoDB (document storage) is a natural pipeline
- MongoDB's Change Streams provide built-in CDC — a clean fit for Source connectors

### 1.3 Codebase Architecture (from Parseltongue)

#### The Connector SDK Contract

**File**: `./core/connectors/sdk/src/lib.rs`

```
Sink trait: Send + Sync
  fn open(&mut self) -> Result<(), Error>
  fn consume(&self, topic_metadata, messages_metadata, messages: Vec<ConsumedMessage>) -> Result<(), Error>
  fn close(&mut self) -> Result<(), Error>

Source trait: Send + Sync
  fn open(&mut self) -> Result<(), Error>
  fn poll(&self) -> Result<ProducedMessages, Error>
  fn close(&mut self) -> Result<(), Error>
```

**Key types**:
- `Payload` enum: `Json(simd_json::OwnedValue)`, `Raw(Vec<u8>)`, `Text(String)`, `Proto(String)`, `FlatBuffer(Vec<u8>)`
- `Schema` enum: `Json` (default), `Raw`, `Text`, `Proto`, `FlatBuffer`
- `ConnectorState(pub Vec<u8>)` — opaque bytes for source state persistence
- `ProducedMessages { schema, messages: Vec<ProducedMessage>, state: Option<ConnectorState> }`
- `Error` enum: 17 variants including `Connection(String)`, `Storage(String)`, `CannotStoreData(String)`, `InitError(String)`

#### Existing Connector Complexity Spectrum (from Parseltongue entity counts)

```
StdoutSink     ~8 entities   — No external deps, no state, no connection
QuickwitSink   ~11 entities  — HTTP client (reqwest), JSON only, no state
ElasticsearchSink ~11 entities — elasticsearch crate, JSON + Raw, state tracking
PostgresSink   ~54 entities  — Connection pool (sqlx), batch inserts, retry logic
PostgresSource ~56 entities  — Connection pool, polling + CDC modes, state tracking
ElasticsearchSource ~40 entities — elasticsearch crate, polling, file-based state
IcebergSink    ~47 entities  — Data lake, S3 staging, schema management
```

#### Which Pattern Does MongoDB Follow?

MongoDB is a **Database-tier connector** (like PostgreSQL), NOT an HTTP/Search connector (like Quickwit/Elasticsearch). Here's why:

| Aspect | HTTP/Search Pattern (Quickwit) | Database Pattern (Postgres) | MongoDB |
|--------|-------------------------------|---------------------------|---------|
| Connection | HTTP client (reqwest) | Connection pool | **Connection pool** (mongodb crate) |
| State management | Minimal | Rich (tracking offsets, CDC tokens) | **Rich** (resume tokens, cursors) |
| Source CDC | N/A or polling | WAL-based CDC | **Change Streams** (oplog-based) |
| Sink writes | HTTP bulk POST | SQL batch INSERT | **Bulk write** (insertMany/bulkWrite) |
| Auth | Basic/API key | Connection string | **Connection string** (SCRAM, X.509) |
| Error handling | HTTP status codes | Transaction rollback | **Retryable writes** |
| Estimated entities | ~11 per connector | ~50-56 per connector | **~45-55 per connector** |

**Classification: MongoDB is a "Database Layer" connector.** Follow the PostgreSQL pattern, not the Quickwit/Elasticsearch pattern.

However, there's a subtlety: MongoDB's Change Streams API is _cleaner_ than Postgres WAL CDC. Postgres requires logical replication slots, publications, and WAL level configuration. MongoDB change streams are a first-class driver API with built-in resume tokens.

### 1.4 Closest Codebase Analog: PostgreSQL Connector

**PostgresSink struct** (`./core/connectors/sinks/postgres_sink/src/lib.rs`):
```rust
pub struct PostgresSink {
    pub id: u32,
    pool: Option<Pool<Postgres>>,
    config: PostgresSinkConfig,
    state: Mutex<State>,
    verbose: bool,
    retry_delay: Duration,
}
```

**PostgresSinkConfig** (12 fields):
```rust
pub struct PostgresSinkConfig {
    pub connection_string: String,
    pub target_table: String,
    pub batch_size: Option<u32>,
    pub max_connections: Option<u32>,
    pub auto_create_table: Option<bool>,
    pub include_metadata: Option<bool>,
    pub include_checksum: Option<bool>,
    pub include_origin_timestamp: Option<bool>,
    pub payload_format: Option<String>,
    pub verbose_logging: Option<bool>,
    pub max_retries: Option<u32>,
    pub retry_delay: Option<String>,
}
```

**PostgresSource struct** (`./core/connectors/sources/postgres_source/src/lib.rs`):
```rust
pub struct PostgresSource {
    pub id: u32,
    pool: Option<Pool<Postgres>>,
    config: PostgresSourceConfig,
    state: Mutex<State>,
    verbose: bool,
    retry_delay: Duration,
    poll_interval: Duration,
}
```

**PostgresSourceConfig** (24 fields!) — supports both polling and CDC modes:
```rust
pub struct PostgresSourceConfig {
    pub connection_string: String,
    pub mode: String,                    // "polling" or "cdc"
    pub tables: Vec<String>,
    pub poll_interval: Option<String>,
    pub batch_size: Option<u32>,
    pub tracking_column: Option<String>,
    pub initial_offset: Option<String>,
    pub max_connections: Option<u32>,
    pub enable_wal_cdc: Option<bool>,
    pub custom_query: Option<String>,
    pub snake_case_columns: Option<bool>,
    pub include_metadata: Option<bool>,
    pub replication_slot: Option<String>,
    pub publication_name: Option<String>,
    pub capture_operations: Option<Vec<String>>,
    pub cdc_backend: Option<String>,
    pub delete_after_read: Option<bool>,
    pub processed_column: Option<String>,
    pub primary_key_column: Option<String>,
    pub payload_column: Option<String>,
    pub payload_format: Option<String>,
    pub verbose_logging: Option<bool>,
    pub max_retries: Option<u32>,
    pub retry_delay: Option<String>,
}
```

### 1.5 MongoDB-Specific Technical Considerations

#### The `mongodb` Rust Crate (v3.x)
- Official MongoDB driver maintained by MongoDB Inc.
- Fully async (tokio-based), built-in connection pooling
- BSON handling via companion `bson` crate
- Change Streams API: `collection.watch()`, `database.watch()`, `client.watch()`
- Resume tokens for crash recovery
- Bulk writes: `insert_many()`, `bulk_write()` with ordered/unordered modes
- Connection string: `mongodb://user:pass@host:27017/db?replicaSet=rs0`

#### Change Streams (Source Connector)
- Requires replica set or sharded cluster (NOT standalone)
- Captures: insert, update, replace, delete, drop, rename, invalidate
- `fullDocument: "updateLookup"` — includes full doc on updates (not just delta)
- `fullDocumentBeforeChange: "whenAvailable"` — pre-image (MongoDB 6.0+)
- Resume tokens persist cursor position across restarts
- Pipeline filtering: `[{"$match": {"operationType": {"$in": ["insert", "update"]}}}]`

#### BSON → JSON Conversion
- Two Extended JSON modes: Relaxed (human-readable) and Canonical (round-trip safe)
- Edge cases: ObjectId → `{"$oid": "hex"}`, DateTime → `{"$date": "ISO-8601"}`, Decimal128
- `bson` crate provides `into_relaxed_extjson()` and `into_canonical_extjson()`
- For high throughput: `serde_transcode` (BSON→JSON without intermediate Rust types)

#### Kafka Connect MongoDB Connector (by MongoDB Inc) — Reference Architecture
- Source: opens change stream, stores resume token in Kafka offset topic
- `startup.mode`: `latest` (only new changes) or `copy_existing` (snapshot + CDC)
- Sink: supports CDC handlers, staleness checks, configurable write models
- Batched ordered bulk writes

### 1.6 Proposed Architecture

#### MongoDBSink

```
MongoDBSink {
    id: u32,
    client: Option<mongodb::Client>,
    config: MongoDBSinkConfig,
    state: Mutex<State>,
    verbose: bool,
    retry_delay: Duration,
}

MongoDBSinkConfig {
    connection_string: String,
    database: String,
    collection: String,
    write_mode: Option<String>,        // "insert" | "upsert" | "replace"
    id_field: Option<String>,          // field to use as _id for upsert/replace
    ordered: Option<bool>,             // ordered vs unordered bulk writes
    batch_size: Option<u32>,
    max_pool_size: Option<u32>,
    include_metadata: Option<bool>,
    json_mode: Option<String>,         // "relaxed" | "canonical" | "simple"
    verbose_logging: Option<bool>,
    max_retries: Option<u32>,
    retry_delay: Option<String>,
}
```

**Flow**: `consume()` → convert `Payload` to BSON `Document` → batch → `insert_many()` or `bulk_write()`

#### MongoDBSource

```
MongoDBSource {
    id: u32,
    client: Option<mongodb::Client>,
    config: MongoDBSourceConfig,
    state: Mutex<State>,
    verbose: bool,
    poll_interval: Duration,
}

MongoDBSourceConfig {
    connection_string: String,
    database: String,
    collection: Option<String>,        // None = watch entire database
    mode: String,                      // "change_stream" | "polling"
    pipeline: Option<Vec<Document>>,   // aggregation filter for change stream
    full_document: Option<String>,     // "updateLookup" | "whenAvailable"
    full_document_before_change: Option<String>,
    startup_mode: Option<String>,      // "latest" | "copy_existing"
    poll_interval: Option<String>,
    batch_size: Option<u32>,
    tracking_field: Option<String>,    // for polling mode: field to track offset
    initial_offset: Option<String>,
    max_pool_size: Option<u32>,
    json_mode: Option<String>,
    include_metadata: Option<bool>,
    verbose_logging: Option<bool>,
    max_retries: Option<u32>,
    retry_delay: Option<String>,
}

State {
    resume_token: Option<bson::Document>,   // for change stream resume
    total_events: u64,
    copy_existing_complete: bool,
    last_offset: Option<String>,            // for polling mode
    last_poll_time: DateTime<Utc>,
    error_count: u64,
    last_error: Option<String>,
}
```

**Flow (change_stream mode)**: `poll()` → `tokio::time::sleep(poll_interval)` → open change stream with resume token → `next_if_any()` up to batch_size → convert BSON to JSON → persist resume token in ConnectorState

**Flow (polling mode)**: `poll()` → `tokio::time::sleep(poll_interval)` → `find()` with sort by tracking_field > last_offset → convert → update offset in state

### 1.7 File Structure

```
core/connectors/
  sinks/
    mongodb_sink/
      Cargo.toml
      src/
        lib.rs        # MongoDBSink struct, config, Sink impl, new()
  sources/
    mongodb_source/
      Cargo.toml
      src/
        lib.rs        # MongoDBSource struct, config, Source impl, new()
        state.rs      # State serialization, resume token handling (optional split)
```

### 1.8 Cargo.toml Dependencies

```toml
[dependencies]
iggy_connector_sdk = { workspace = true }
iggy_common = { workspace = true }
async-trait = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
simd-json = { workspace = true }
tokio = { workspace = true }
tracing = { workspace = true }
uuid = { workspace = true }
humantime = { workspace = true }
chrono = { workspace = true }
# MongoDB-specific
mongodb = "3"
bson = { version = "2", features = ["serde_json-1"] }
futures = { workspace = true }
```

### 1.9 TOML Config Examples

**Sink** (`mongodb_sink.toml`):
```toml
[sink]
enabled = true
name = "mongodb_sink"
path = "./connectors/mongodb_sink"

[[sink.streams]]
stream = "sensor-data"
topics = ["temperature"]

[sink.plugin_config]
connection_string = "mongodb://localhost:27017"
database = "iot_data"
collection = "sensor_readings"
write_mode = "insert"
batch_size = 500
ordered = false
```

**Source** (`mongodb_source.toml`):
```toml
[source]
enabled = true
name = "mongodb_source"
path = "./connectors/mongodb_source"

[[source.streams]]
stream = "mongo-events"
topic = "changes"

[source.plugin_config]
connection_string = "mongodb://localhost:27017/?replicaSet=rs0"
database = "mydb"
collection = "orders"
mode = "change_stream"
full_document = "updateLookup"
startup_mode = "latest"
batch_size = 100
poll_interval = "1s"
```

---

## PART 2: RUBBER DUCK DEBUGGING — CRITICIZING THE ANALYSIS

Let me step back and systematically poke holes in my own analysis.

### Critique 1: "Follow the PostgreSQL pattern" Is Too Simplistic

**The problem**: I said MongoDB is a "Database Layer" connector like PostgreSQL. But MongoDB's data model is fundamentally different:

- PostgreSQL uses typed rows in tables with schemas. Iggy's `insert_batch()` builds parameterized SQL with column-level type mapping.
- MongoDB stores schemaless BSON documents. There is no table DDL, no column types, no `auto_create_table`.
- PostgreSQL's CDC uses WAL logical replication (low-level, requires DBA setup). MongoDB's Change Streams are a high-level API (no oplog access needed).

**What I got wrong**: The MongoDB Sink is actually _simpler_ than PostgresSink (no schema management, no DDL, no parameterized queries). The MongoDB Source is also _simpler_ than PostgresSource (no WAL configuration, no replication slots, no publication management). The entity count estimate of ~45-55 is probably high. **It might be closer to ~25-35 per connector.**

**The actual pattern**: MongoDB Sink is structurally between QuickwitSink (HTTP, JSON-only, ~11 entities) and PostgresSink (~54 entities). MongoDB Source is structurally between ElasticsearchSource (~40 entities) and PostgresSource (~56 entities).

### Critique 2: Change Stream Lifecycle in `poll()` Is Wrong

**The problem**: My proposed architecture opens a new change stream on every `poll()` call. This is terrible:

- Opening a change stream involves a server-side cursor allocation
- The `resume_after` token requires the server to find the oplog position
- Each `poll()` call would create a new TCP round-trip for cursor creation
- If poll_interval is 1 second, that's 1 change stream open/close per second

**What the PostgresSource does**: It keeps the connection pool alive across `poll()` calls (stored in `self.pool`). The `poll()` method just executes queries against the existing pool.

**What the ElasticsearchSource does**: It keeps the `Elasticsearch` client alive and uses `search_documents()` against it — no reconnection per poll.

**The fix**: The change stream cursor must be kept alive across `poll()` calls. It should be opened once in `open()` (or lazily on first `poll()`) and stored in the struct. The `poll()` method should call `next_if_any()` on the existing cursor.

BUT: The `Source` trait requires `poll(&self)` (immutable borrow). To mutate the change stream cursor, we'd need it behind a `Mutex`. This is exactly what ElasticsearchSource and PostgresSource do with their state — store it in `Mutex<State>`.

**Revised approach**: Store `change_stream: Option<Mutex<ChangeStream<...>>>` in the struct, opened in `open()`, iterated in `poll()`.

### Critique 3: BSON → simd_json::OwnedValue Conversion Gap

**The problem**: The Iggy Payload enum uses `simd_json::OwnedValue`, not `serde_json::Value`. All existing connectors that produce JSON use simd_json. But:

- MongoDB's `bson` crate produces `bson::Bson` / `bson::Document`
- The `into_relaxed_extjson()` method produces `serde_json::Value`
- There is no direct `bson::Document` → `simd_json::OwnedValue` conversion

**The conversion chain**: `bson::Document` → `serde_json::Value` (via `into_relaxed_extjson()`) → `String` (via `serde_json::to_string()`) → `simd_json::OwnedValue` (via `simd_json::from_slice()`)

This double serialization is wasteful for high-throughput scenarios. The PostgresSink handles this by using `simd_json::to_vec()` and `simd_json::from_slice()` directly. The ElasticsearchSink uses `simd_json::json!()` macros.

**The fix**: For the **sink** (Iggy→MongoDB), messages arrive as `Payload::Json(simd_json::OwnedValue)`. Convert: `simd_json::OwnedValue` → `serde_json::Value` → `bson::Document`. The codebase already has `owned_value_to_serde_json()` in the ES sink.

For the **source** (MongoDB→Iggy), the payload is `Vec<u8>`. We can use `serde_json::to_vec()` on the BSON document's relaxed Extended JSON, and the runtime will handle decoding.

### Critique 4: "copy_existing" Startup Mode Is Underspecified

**The problem**: I mentioned `startup_mode: "copy_existing"` but didn't think through the implications:

- How do you know when the snapshot is complete? What if the collection has 10M documents?
- While snapshotting, new writes are happening. How do you not miss changes between the end of the snapshot and the start of the change stream?
- The Kafka MongoDB connector solves this by opening the change stream FIRST (getting a resume token), THEN doing the snapshot, THEN resuming the change stream from the saved token.

**This is a significant architectural decision** that affects correctness, not just performance.

### Critique 5: The `write_mode: "upsert"` Path Is Non-Trivial

**The problem**: For upsert/replace modes, MongoDB needs an `_id` or filter to identify which document to update. The proposed `id_field` config is too naive:

- What if the incoming JSON has a nested field as the ID?
- What if the `_id` should be computed (e.g., hash of multiple fields)?
- The Kafka MongoDB Sink connector supports a full `document.id.strategy` with multiple strategies: `BsonOidStrategy`, `KafkaMetaDataStrategy`, `FullKeyStrategy`, `PartialKeyStrategy`, etc.

**The fix**: Start with `insert` mode only (like PostgresSink's initial approach). Add upsert/replace as a follow-up enhancement.

### Critique 6: Missing Error Classification

**The problem**: MongoDB errors have specific types that should map to Iggy's `Error` enum differently:

| MongoDB Error | Iggy Error Mapping | Retry? |
|--------------|-------------------|--------|
| `ServerSelectionError` | `Error::Connection(...)` | Yes |
| `WriteError` (duplicate key) | `Error::CannotStoreData(...)` | No (idempotent) |
| `WriteError` (write concern) | `Error::CannotStoreData(...)` | Yes |
| `BulkWriteError` (partial) | `Error::CannotStoreData(...)` | Partial |
| `AuthenticationError` | `Error::InitError(...)` | No |
| `CursorNotFound` | `Error::Connection(...)` | Yes (reopen stream) |

The analysis didn't address partial bulk write failures — where some documents succeed and others fail. This needs careful handling (log failures, continue with successful ones, report error count in state).

### Critique 7: Replica Set Requirement Is a Deployment Blocker

**The problem**: MongoDB Change Streams require a replica set. Many development setups use standalone MongoDB. The source connector will fail with a cryptic error if someone tries to use it against a standalone instance.

**The fix**: In `open()`, check the deployment topology. If standalone, return a clear `Error::InitError("MongoDB change streams require a replica set. Please configure MongoDB as a replica set or use 'polling' mode instead.")`.

---

## PART 3: THREE SOLUTION OPTIONS

### OPTION A: "Minimal Viable Connector" — Sink Only, Insert Mode

**Scope**: Only the MongoDBSink connector. Insert mode only. No CDC, no source.

**What gets built**:
- `mongodb_sink/src/lib.rs` (~150-200 lines)
- `MongoDBSink` struct with `mongodb::Client`
- `MongoDBSinkConfig`: connection_string, database, collection, batch_size, ordered, max_pool_size
- `consume()`: convert `Payload::Json` → `serde_json::Value` → `bson::Document` → `insert_many()`
- Metadata injection: `_iggy_offset`, `_iggy_stream`, `_iggy_topic`, `_iggy_timestamp`
- TOML config
- Basic e2e test with Docker testcontainer

**What does NOT get built**:
- No source connector
- No upsert/replace modes
- No CDC / change streams
- No polling mode
- No BSON-native payload support

**Estimated complexity**: ~15-20 code entities. Similar to QuickwitSink (~11) but with connection pooling.

**Pros**:
- Fastest to implement and merge
- Lowest review burden
- Covers the most common use case (stream data INTO MongoDB)
- Clean foundation to build on
- Easy to test (just need a MongoDB container)

**Cons**:
- No source connector (half the value)
- Can't compete with Kafka/Debezium MongoDB connectors which have full CDC
- Users who need MongoDB→Iggy have no solution

#### Rubber Duck Critique of Option A

**"Is insert-only actually useful?"** — Yes. The majority of message streaming use cases with databases are sinking (stream → DB for analytics, archival, or materialized views). This is confirmed by the fact that Iggy's PostgresSink was merged months before PostgresSource.

**"Will this be throwaway work?"** — No. The Sink will remain unchanged when Source is added later. The struct, config, connection handling, BSON conversion, and Cargo.toml are all reusable.

**"What about the BSON conversion overhead?"** — For a minimal connector, the double-serialization (simd_json → serde_json → bson) is acceptable. The overhead is measurable but not significant at typical batch sizes (100-1000 docs). Optimize later if profiling shows it matters.

---

### OPTION B: "Full Database Connector" — Sink + Source, Following Postgres Pattern

**Scope**: Both MongoDBSink and MongoDBSource. Two modes: change_stream + polling.

**What gets built**:

MongoDBSink (~200-250 lines):
- Everything in Option A
- Plus: upsert mode with configurable `id_field`
- Plus: replace mode
- Plus: `json_mode` config (relaxed/canonical Extended JSON)

MongoDBSource (~350-450 lines):
- `MongoDBSource` struct with `mongodb::Client` + `Mutex<ChangeStream>`
- Two modes: `change_stream` and `polling`
- Change stream mode: resume token persistence via `ConnectorState`
- Polling mode: tracking field offset, like PostgresSource `poll_tables()`
- State management: save/load state for crash recovery
- `startup_mode: "copy_existing"` with proper ordering (open stream first, snapshot, resume)
- Pipeline filtering
- Full document / pre-image config

Supporting infrastructure:
- State serialization module
- BSON → JSON conversion utilities
- TOML config examples for both
- e2e tests for both sink and source

**Estimated complexity**: ~40-50 entities per connector, ~80-100 total. Similar to PostgresSink + PostgresSource.

**Pros**:
- Complete solution — matches Kafka MongoDB connector feature parity
- Both sink and source in one PR (or split into two)
- CDC via change streams is the killer feature
- Resume tokens provide exactly-once-ish semantics
- Positions Iggy as a serious MongoDB integration option

**Cons**:
- Larger implementation scope
- Change stream lifecycle management is tricky (keeping cursor alive across `poll()` calls)
- `copy_existing` mode is an ordering problem (snapshot + CDC overlap)
- Upsert mode requires design decisions about ID strategies
- Longer review cycle
- More test infrastructure needed (replica set Docker container)

#### Rubber Duck Critique of Option B

**"Is the change stream lifecycle actually hard?"** — Yes, somewhat. The `Source::poll(&self)` signature takes `&self` (immutable). To advance the change stream cursor, you need interior mutability. The PostgresSource solves this with `Mutex<State>` — and its state doesn't include a cursor. For MongoDB, you'd need `Mutex<Option<ChangeStream<...>>>`. The `ChangeStream` type is generic over the document type AND involves async iteration. Wrapping this in a Mutex and sharing it across the `open()` and `poll()` boundary requires careful lifetime management.

**Alternative**: Don't keep the change stream open across polls. Open it fresh each time with `resume_after()`. The overhead is a server round-trip per poll cycle (cursor creation), but Change Streams are designed to be resumed efficiently. This is the approach the Kafka MongoDB connector takes (it doesn't keep cursors across poll cycles either — it stores the resume token and reopens).

**"Is copy_existing really needed for v1?"** — No. The Kafka MongoDB connector added it as an enhancement. Start with `startup_mode: "latest"` only and add `copy_existing` later.

**"What about sharded clusters?"** — Change streams work on sharded clusters via `mongos`. No special handling needed. But testing against a sharded cluster is hard. Skip for v1.

---

### OPTION C: "Source-First with Change Streams" — Source Only, CDC Focus

**Scope**: Only the MongoDBSource connector with change stream mode. No sink. No polling.

**What gets built**:

MongoDBSource (~250-300 lines):
- `MongoDBSource` struct with `mongodb::Client`
- Change stream mode only (no polling)
- Resume token persistence via `ConnectorState`
- `startup_mode: "latest"` only (no copy_existing)
- Pipeline filtering
- Full document config
- Relaxed Extended JSON output
- State management: serialize/deserialize resume token
- e2e test with Docker replica set

**What does NOT get built**:
- No sink connector
- No polling mode
- No copy_existing
- No pre-image support

**Estimated complexity**: ~25-30 entities. Structurally between ElasticsearchSource (~40) and QuickwitSink (~11).

**Pros**:
- MongoDB→Iggy is the more _unique_ use case (Iggy→MongoDB can be done with any JSON-to-MongoDB tool)
- Change streams are MongoDB's unique strength vs other databases
- Demonstrates Iggy's CDC capabilities alongside PostgresSource
- Simpler than Option B (no sink, no polling, no copy_existing)
- Resume tokens provide clean crash recovery
- Good demo material ("stream your MongoDB changes into Iggy in real-time")

**Cons**:
- No sink (the more commonly needed connector type)
- Users who want to archive Iggy streams to MongoDB have no solution
- Only works with replica sets (not standalone)
- Change stream mode only — no fallback for non-replica-set deployments

#### Rubber Duck Critique of Option C

**"Source-only is backwards. Most users want sink first."** — This is a valid criticism. Looking at Iggy's own history: PostgresSink (PR #2579) landed in October 2025, PostgresSource in the same PR. IcebergSink landed in November 2025 — no source yet. ElasticsearchSink was first. The pattern is clear: **Sink connectors land first** because the primary use case is "stream data into a database for storage/analytics."

**"But Change Streams are the cool feature."** — Cool features don't matter if users can't use them. A source-only connector targets a niche audience (people who already have data in MongoDB and want to stream changes somewhere). A sink connector targets anyone with a message stream who needs to store documents.

**"Could this create a foundation for the sink later?"** — Sort of. The Cargo.toml, mongodb crate integration, BSON conversion utilities, and TOML config patterns transfer. But the Source and Sink don't share any code beyond dependencies — they're separate cdylib crates.

---

## PART 4: RECOMMENDATION MATRIX

| Criterion | Option A (Sink Only) | Option B (Full) | Option C (Source Only) |
|-----------|---------------------|-----------------|----------------------|
| **Implementation scope** | Small | Large | Medium |
| **Review burden** | Low | High | Medium |
| **User impact (breadth)** | High (sink is more common) | Highest | Low |
| **Competitive parity** | Partial | Full | Partial |
| **Technical risk** | Low | Medium (change stream lifecycle) | Medium (change stream lifecycle) |
| **Foundation for future** | Yes (sink done, add source later) | Complete | Weak (need sink separately) |
| **Testability** | Easy (standalone MongoDB) | Hard (replica set) | Hard (replica set) |
| **Merge probability** | Highest | Medium | Medium |

### My Recommendation: **Option A first, then upgrade to Option B**

Ship the Sink connector (Option A) as PR #1. It's small, focused, high-impact, and easy to review. Then follow up with the Source connector as PR #2, building on the established crate structure. This is the same pattern PostgreSQL followed (sink + source in one PR, but the sink was the primary deliverable).

If you want to be ambitious, do **Option B** but split it into two PRs:
1. PR #1: MongoDBSink (insert + upsert modes)
2. PR #2: MongoDBSource (change stream mode with resume tokens)

---

## APPENDIX: Key Parseltongue Queries Used

```
/code-entities-search-fuzzy?q=PostgresSink         → 3 entities (struct, impl, config)
/code-entities-search-fuzzy?q=PostgresSource        → 4 entities (struct, impl, config, unresolved)
/code-entities-search-fuzzy?q=ElasticsearchSink     → 4 entities
/code-entities-search-fuzzy?q=ElasticsearchSource   → 5 entities
/code-entities-search-fuzzy?q=QuickwitSink          → 3 entities
/code-entities-search-fuzzy?q=StdoutSink            → 3 entities
/code-entities-list-all?entity_type=trait            → 137 traits, filtered to 12 connector-related
/code-entity-detail-view → 20+ entity detail queries for:
  - Sink trait, Source trait, Transform trait
  - PostgresSink struct/impl/config, PostgresSource struct/impl/config
  - ElasticsearchSink struct/impl/config, ElasticsearchSource struct/impl/config
  - QuickwitSink struct/impl, StdoutSink struct/impl
  - ConnectorConfig enum, SinkConfig struct, SourceConfig struct
  - Error enum, Payload enum, Schema enum, ConnectorState struct
  - ProducedMessages struct, ConsumedMessage struct
  - SinkConnectorPlugin, SinkConnectorWrapper, SourceConnectorPlugin
  - StateStorage enum, FileStateStorage impl
  - PostgresSource methods: poll_cdc, setup_cdc, poll_tables, process_messages, insert_batch
  - ElasticsearchSink: bulk_index_documents
```

---

*Generated: 2026-02-16T08:45:00Z*
*Analysis grounded in: Parseltongue v1.7.2 (15,998 entities, 78,896 edges) + mongodb crate docs + Kafka/Debezium MongoDB connector research*
