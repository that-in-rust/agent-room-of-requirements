# MongoDB Connector Specification for Apache Iggy

**Version**: 2.0
**Date**: February 21, 2026
**Status**: PRD / Design Document (pre-implementation review)
**Supersedes**: mongodb-connector-spec.md (v5)
**Context**: Proposes MongoDB sink and source connectors for the Iggy connectors runtime

---

## 1. Motivation

Apache Iggy's connector ecosystem currently supports PostgreSQL, Elasticsearch, Quickwit, and Iceberg. MongoDB is the most popular document database (per DB-Engines rankings) and a natural fit for both:

- **Sink**: Stream iggy messages into MongoDB collections for queryable storage
- **Source**: Poll MongoDB collections into iggy streams for event-driven pipelines

This spec defines the design, drawing from:
- Existing iggy connector patterns (PostgreSQL as primary reference)
- Industry research across Kafka Connect, Debezium, Flink, and Airbyte MongoDB connectors
- Gap analysis of a prototype implementation against the original spec

---

## 2. Design Decisions

Each decision below was evaluated against industry practice and existing iggy patterns. Rationale is provided for maintainer review.

### 2.1 Connection Field Naming: `connection_uri`

| Platform | Field Name |
|---|---|
| MongoDB Kafka Connector (MongoDB Inc) | `connection.uri` |
| Confluent MongoDB Connector | `connection.uri` |
| Debezium MongoDB | `mongodb.connection.string` |
| Apache Flink MongoDB | `uri` |
| Airbyte MongoDB | `connection_string` |
| iggy PostgreSQL | `connection_string` |
| iggy Elasticsearch | `url` |

**Decision**: Use `connection_uri` for both sink and source.

**Why**: MongoDB's own Kafka Connector (the de facto standard) uses `connection.uri`. In Rust snake_case, this becomes `connection_uri`. While iggy's PostgreSQL connector uses `connection_string`, each database ecosystem has its own terminology. MongoDB documentation consistently refers to the connection parameter as a "URI" (Uniform Resource Identifier), not a "connection string." Using `connection_uri` respects MongoDB's domain language.

**Trade-off acknowledged**: This creates a naming difference from PostgreSQL's `connection_string`. We considered standardizing all connectors to one name, but rejected it because each database SDK uses different terminology and forcing a generic name reduces clarity.

### 2.2 Batch Insert API: `insert_many()` (not `bulk_write()`)

**Decision**: Use `collection.insert_many()` for batch inserts.

**Why**:
- The MongoDB Rust driver's `bulk_write()` requires **MongoDB Server 8.0+**. Requiring the latest server version would limit adoption.
- MongoDB's own documentation states: *"Internally, `insertMany` uses `bulkWrite`, so there's no difference — it's just for convenience."*
- For append-only workloads (which is what a sink connector does — no updates or deletes), `insert_many()` is the idiomatic choice.
- Every major production connector (Kafka Connect, Debezium) uses `bulkWrite()` because they handle **mixed operations** (insert + update + delete from CDC). Our sink is insert-only.

**When to revisit**: If/when CDC support (MongoDB Change Streams) is added to the sink, switch to `bulk_write()` to handle mixed operation types in a single batch.

### 2.3 Collection Validation: Warn and Continue

**Decision**: On source `open()`, warn if the target collection doesn't exist. Do not fail.

**Industry evidence**:

| Platform | Behavior on Missing Collection |
|---|---|
| MongoDB Kafka Source | Does not fail. Opens change stream, waits. |
| Debezium MongoDB | Does not fail. Filters events via regex. |
| Apache Flink MongoDB | Returns zero documents. No error. |
| Flink CDC MongoDB | Opens change streams. Handles gracefully. |

**Why**: MongoDB creates collections lazily (on first insert). In microservices architectures, the source connector may start before the application that creates the collection. Failing hard would require manual restart after collection creation — an operational burden with no safety benefit.

**Corrected log message**: The prototype had "will be created on first write" which is misleading for a source (sources read, they don't write). Corrected to: "polling will return empty results until the collection is created."

### 2.4 State Schema: `HashMap<String, String>` for Offset Tracking

**Decision**: Use `tracking_offsets: HashMap<String, String>` in the source State struct.

**Why**:
- iggy's PostgreSQL source already uses `tracking_offsets: HashMap<String, String>` — this is the established pattern for polling-based source connectors that may track multiple entities.
- Polling with `find()` requires per-collection cursors. A single `Option<String>` would only work if multi-collection support is never added.
- `HashMap` provides forward compatibility — adding multi-collection support later requires no state migration.
- Kafka Connect and Debezium both use maps for offset storage, even when conceptually tracking a single cursor.

**Note**: The original spec (v5) used `tracking_offset: Option<String>`. This was incorrect and has been superseded.

### 2.5 Error Handling in Sink `process_messages()`: Log and Continue

**Decision**: When a batch fails after retries, log the error, increment error counter, continue to next batch.

**Why**: This is the established iggy pattern. PostgreSQL sink and Elasticsearch sink both do the same. The connectors runtime handles higher-level retry and error reporting. Propagating batch errors would cause the runtime to stop consuming from the stream, which is a worse failure mode than logging and continuing (partial data loss vs total data loss).

### 2.6 Unused Config Fields: Wire All

**Decision**: Every field declared in the config struct must be wired to actual functionality. No dead config.

**Why**: Users configure connectors via TOML files. A field that appears in config but silently does nothing is a **silent misconfiguration bug**. The prototype had 4 unused fields in the source (`initial_offset`, `snake_case_fields`, `payload_format`, `include_metadata`). All must be implemented or removed.

---

## 3. Sink Connector Design

### 3.1 Overview

The MongoDB sink consumes messages from iggy streams and inserts them as documents into a MongoDB collection.

**Crate**: `core/connectors/sinks/mongodb_sink/`
**Crate type**: `cdylib` + `lib`
**Plugin registration**: `sink_connector!(MongoDbSink)`
**Entity count**: 4 structs/enums (MongoDbSink, MongoDbSinkConfig, PayloadFormat, State)

### 3.2 Config

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MongoDbSinkConfig {
    // Required
    pub connection_uri: String,
    pub database: String,
    pub collection: String,

    // Connection
    pub max_pool_size: Option<u32>,              // Default: driver default
    pub auto_create_collection: Option<bool>,    // Default: false

    // Batching
    pub batch_size: Option<u32>,                 // Default: 100

    // Document fields
    pub include_metadata: Option<bool>,          // Default: true (iggy_offset, iggy_timestamp, etc.)
    pub include_checksum: Option<bool>,          // Default: true
    pub include_origin_timestamp: Option<bool>,  // Default: true
    pub payload_format: Option<String>,          // Default: "binary". Values: "binary", "json", "string"/"text"

    // Retry
    pub max_retries: Option<u32>,                // Default: 3
    pub retry_delay: Option<String>,             // Default: "1s" (humantime format)

    // Observability
    pub verbose_logging: Option<bool>,           // Default: false
}
```

### 3.3 Connection Pattern

Use `ClientOptions::parse()` + `Client::with_options()`:

```rust
async fn connect(&mut self) -> Result<(), Error> {
    let mut options = ClientOptions::parse(&self.config.connection_uri).await
        .map_err(|e| Error::InitError(format!("Failed to parse connection URI: {e}")))?;

    if let Some(pool_size) = self.config.max_pool_size {
        options.max_pool_size = Some(pool_size);
    }

    let client = Client::with_options(options)
        .map_err(|e| Error::InitError(format!("Failed to create client: {e}")))?;

    client.database(&self.config.database)
        .run_command(doc! {"ping": 1}).await
        .map_err(|e| Error::InitError(format!("Ping failed: {e}")))?;

    self.client = Some(client);
    Ok(())
}
```

**Why not `Client::with_uri_str()`**: That API does not accept `ClientOptions`, so `max_pool_size` cannot be configured. The `ClientOptions::parse()` pattern is what the source already uses and matches iggy's PostgreSQL builder pattern.

### 3.4 Document Structure

Each iggy message becomes one MongoDB document:

```json
{
    "_id": "340282366920938463463374607431768211456",  // message.id (u128 as string)
    "iggy_offset": 42,                                 // when include_metadata = true
    "iggy_timestamp": ISODate("2026-02-21T..."),       // microseconds / 1000 → BSON DateTime
    "iggy_stream": "my-stream",
    "iggy_topic": "my-topic",
    "iggy_partition_id": 0,
    "iggy_checksum": 12345678,                         // when include_checksum = true
    "iggy_origin_timestamp": ISODate("2026-02-21T..."),// when include_origin_timestamp = true
    "payload": <Binary|Document|String>                // per payload_format
}
```

### 3.5 PayloadFormat Enum

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub enum PayloadFormat {
    #[default]
    Binary,   // BSON Binary (subtype Generic). Raw bytes preserved.
    Json,     // Parse payload as JSON, store as BSON Document. Queryable.
    String,   // Store as BSON String. Aliases: "text".
}
```

**Default is Binary** for sinks because it preserves the original payload without transformation. This matches PostgreSQL sink's default of `Bytea`.

### 3.6 Retry with Transient Error Detection

```rust
fn is_transient_error(error: &mongodb::error::Error) -> bool {
    let msg = error.to_string().to_lowercase();
    msg.contains("timeout") || msg.contains("network")
        || msg.contains("connection") || msg.contains("pool")
        || msg.contains("server selection")
}
```

Only retry on transient errors. Do not retry on:
- Authentication failures
- Duplicate key errors
- Invalid BSON errors

### 3.7 Lifecycle

| Method | Responsibility |
|---|---|
| `new(id, config)` | Parse config, set defaults, initialize empty state |
| `open()` | Connect, ping, optionally create collection |
| `consume(topic_metadata, messages_metadata, messages)` | Delegate to `process_messages()` |
| `close()` | Drop client, log statistics |

---

## 4. Source Connector Design

### 4.1 Overview

The MongoDB source polls a collection for new/unprocessed documents and produces them as iggy messages.

**Crate**: `core/connectors/sources/mongodb_source/`
**Crate type**: `cdylib` + `lib`
**Plugin registration**: `source_connector!(MongoDbSource)`
**Entity count**: 4 structs/enums (MongoDbSource, MongoDbSourceConfig, PayloadFormat, State)

### 4.2 Config

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MongoDbSourceConfig {
    // Required
    pub connection_uri: String,          // Renamed from connection_string
    pub database: String,
    pub collection: String,

    // Polling
    pub poll_interval: Option<String>,   // Default: "10s" (humantime)
    pub batch_size: Option<u32>,         // Default: 1000

    // Connection
    pub max_pool_size: Option<u32>,      // Default: driver default

    // Offset tracking
    pub tracking_field: Option<String>,  // Default: "_id"
    pub initial_offset: Option<String>,  // MUST BE WIRED: seed tracking_offsets on first run

    // Filtering
    pub query_filter: Option<String>,    // JSON string merged into find() filter
    pub projection: Option<String>,      // JSON string for field selection

    // Document processing
    pub snake_case_fields: Option<bool>, // MUST BE WIRED: convert field names to snake_case
    pub include_metadata: Option<bool>,  // MUST BE WIRED: add iggy_* fields to payload
    pub payload_field: Option<String>,   // Extract specific field as payload (else entire doc)
    pub payload_format: Option<String>,  // MUST BE WIRED: "json" (default), "bson"/"binary", "string"/"text"

    // Post-processing
    pub delete_after_read: Option<bool>, // Default: false
    pub processed_field: Option<String>, // Field to mark as processed (alternative to delete)

    // Retry
    pub max_retries: Option<u32>,        // Default: 3. MUST BE WIRED to poll_collection().
    pub retry_delay: Option<String>,     // Default: "1s". MUST BE WIRED to poll_collection().

    // Observability
    pub verbose_logging: Option<bool>,   // Default: false
}
```

### 4.3 PayloadFormat Enum (Source)

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub enum PayloadFormat {
    #[default]
    Json,     // Serialize document to JSON bytes. Schema::Json.
    Bson,     // Serialize document to BSON bytes. Schema::Raw. Aliases: "binary".
    String,   // Serialize document to string. Schema::Text. Aliases: "text".
}
```

**Default is Json** for sources because downstream consumers most commonly expect JSON. This matches PostgreSQL source's default of `Json`.

Maps to SDK Schema:
- `Json` -> `Schema::Json`
- `Bson` -> `Schema::Raw`
- `String` -> `Schema::Text`

### 4.4 State Struct

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
struct State {
    last_poll_time: DateTime<Utc>,
    tracking_offsets: HashMap<String, String>,  // key: collection name, value: last offset
    processed_documents: u64,
}
```

Serialized via `ConnectorState` (MessagePack / `rmp_serde`). Persisted by the runtime between polls and across restarts.

**`initial_offset` wiring**: When no persisted state exists AND `initial_offset` is configured, seed the HashMap:

```rust
let initial_state = restored_state.unwrap_or_else(|| {
    let mut offsets = HashMap::new();
    if let Some(offset) = &config.initial_offset {
        offsets.insert(config.collection.clone(), offset.clone());
    }
    State { last_poll_time: Utc::now(), tracking_offsets: offsets, processed_documents: 0 }
});
```

### 4.5 Polling with Retry

The source MUST wrap `find()` + cursor operations in a retry loop:

```rust
async fn poll_collection(&self) -> Result<Vec<ProducedMessage>, Error> {
    let max_retries = self.get_max_retries();
    let mut attempts = 0;
    loop {
        match self.execute_poll().await {
            Ok(msgs) => return Ok(msgs),
            Err(e) if is_transient_error_str(&e.to_string()) && attempts < max_retries => {
                attempts += 1;
                warn!("Poll failed (attempt {attempts}/{max_retries}): {e}");
                tokio::time::sleep(self.retry_delay * attempts).await;
            }
            Err(e) => return Err(e),
        }
    }
}
```

**Why this matters**: Without retry, a single transient network error (VPC timeout, rolling restart, pool exhaustion) kills the source permanently. The PostgreSQL source has retry. The Elasticsearch source does not — and that's a gap in Elasticsearch too.

### 4.6 Timestamp Handling

`document_to_message()` must extract timestamps from the document, not default to `Utc::now()`:

1. If tracking field is `_id` and value is `ObjectId` -> use `oid.timestamp()` (ObjectId embeds creation time)
2. If document has a recognized timestamp field -> use it
3. Fallback to `Utc::now()` only when no document timestamp is available

### 4.7 Error Types

| Context | Correct Error Type |
|---|---|
| Connection setup in `open()` | `Error::InitError(String)` |
| Config JSON parse failure | `Error::InvalidConfig` |
| Query failure during `poll()` | `Error::Storage(String)` |
| Connection drop during `poll()` | `Error::Connection(String)` |
| Document serialization failure | `Error::InvalidRecord` |
| Delete/mark failure | `Error::Storage(String)` |

The original prototype used `Error::InitError` for everything, which misrepresents runtime errors as initialization errors.

### 4.8 Lifecycle

| Method | Responsibility |
|---|---|
| `new(id, config, state)` | Parse config, restore state, set defaults |
| `open()` | Connect, ping, validate collection (warn if missing) |
| `poll()` | Sleep for `poll_interval`, call `poll_collection()` with retry, update state, return messages |
| `close()` | Drop client, log statistics |

---

## 5. Wiring the Previously Unused Config Fields

These 4 fields existed in the prototype source config but were never wired. Each must be implemented:

### 5.1 `initial_offset`

**Purpose**: Start polling from a specific offset instead of the beginning.
**Wiring**: Seed `tracking_offsets` HashMap in constructor when no persisted state exists (see 4.4).

### 5.2 `snake_case_fields`

**Purpose**: Convert MongoDB camelCase field names (e.g., `firstName`) to snake_case (e.g., `first_name`) in the produced payload.
**Wiring**: In `document_to_message()`, before serializing the document, iterate keys and convert to snake_case. Use a simple char-by-char conversion (insert `_` before uppercase, lowercase all).

### 5.3 `payload_format`

**Purpose**: Control how documents are serialized into message payloads.
**Wiring**: Parse config into `PayloadFormat` enum. Use it in `poll()` to set `Schema` on `ProducedMessages`, and in `document_to_message()` to choose serialization method (JSON, BSON, or String).

### 5.4 `include_metadata`

**Purpose**: When true, add iggy-related metadata fields to the produced payload (source collection name, poll timestamp, document offset).
**Wiring**: In `document_to_message()`, when enabled, inject metadata fields into the document before serialization:
```rust
if self.config.include_metadata.unwrap_or(false) {
    doc.insert("_iggy_source_collection", &self.config.collection);
    doc.insert("_iggy_poll_timestamp", Utc::now().to_rfc3339());
}
```

---

## 6. E2E Integration Test Design

### 6.1 Infrastructure

Uses existing iggy testcontainers + `#[iggy_harness]` infrastructure. No external scripts (Go/Python) needed.

**Root Cargo.toml change**:
```toml
testcontainers-modules = { version = "0.14.0", features = ["postgres", "mongodb"] }
```

### 6.2 File Structure

```
core/integration/tests/connectors/
  fixtures/mongodb/
    container.rs     # MongoDbContainer using GenericImage or testcontainers-modules
    sink.rs          # MongoDbSinkFixture, MongoDbSinkBinaryFixture, MongoDbSinkJsonFixture
    source.rs        # MongoDbSourceFixture with seed() for inserting test documents
    mod.rs           # Re-exports
  mongodb/
    mod.rs           # Module + constants (TEST_MESSAGE_COUNT, etc.)
    mongodb_sink.rs  # Sink integration tests
    mongodb_source.rs # Source integration tests
    sink.toml        # Connector runtime config for sink
    source.toml      # Connector runtime config for source
```

### 6.3 Container Pattern

Follow the Elasticsearch GenericImage pattern (not the PostgreSQL testcontainers-modules pattern), unless `testcontainers-modules` v0.14.0 has a MongoDB module:

```rust
pub struct MongoDbContainer {
    container: ContainerAsync<GenericImage>,
    pub(super) connection_uri: String,
}

impl MongoDbContainer {
    pub(super) async fn start() -> Result<Self, TestBinaryError> {
        let image = GenericImage::new("mongo", "7")
            .with_exposed_port(27017.tcp())
            .with_wait_for(WaitFor::message_on_stdout("Waiting for connections"));
        let container = image.start().await?;
        let port = container.get_host_port_ipv4(27017).await?;
        let connection_uri = format!("mongodb://localhost:{port}");
        Ok(Self { container, connection_uri })
    }
}
```

### 6.4 Sink Test Cases

| Test | What It Verifies |
|---|---|
| `json_messages_sink_to_mongodb` | 3 JSON messages land in MongoDB with correct field values |
| `binary_messages_sink_as_bson_binary` | Binary payload stored as BSON Binary type |
| `metadata_fields_included` | `iggy_offset`, `iggy_stream`, etc. present when `include_metadata = true` |
| `large_batch_processed_correctly` | Message count > `batch_size` splits into multiple batches correctly |
| `auto_create_collection_on_open` | Collection created when `auto_create_collection = true` |

### 6.5 Source Test Cases

| Test | What It Verifies |
|---|---|
| `source_polls_documents_to_iggy` | Seed 3 docs in MongoDB, verify they appear in iggy stream |
| `offset_tracking_across_polls` | Insert docs, poll once, insert more, poll again — second poll returns only new docs |
| `delete_after_read_removes_documents` | After polling, documents are deleted from MongoDB |
| `mark_processed_sets_field` | After polling, `processed` field is set to `true` |
| `payload_format_json_emits_schema_json` | Schema on produced messages is `Schema::Json` |

### 6.6 Environment Variables

Fixtures inject config via environment variables (established iggy pattern):

**Sink**:
```
IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_CONNECTION_URI
IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_DATABASE
IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_COLLECTION
IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_STREAM
IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_TOPICS
IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_CONSUMER_GROUP
IGGY_CONNECTORS_SINK_MONGODB_PATH
```

**Source**:
```
IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_CONNECTION_URI
IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_DATABASE
IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_COLLECTION
IGGY_CONNECTORS_SOURCE_MONGODB_STREAMS_0_STREAM
IGGY_CONNECTORS_SOURCE_MONGODB_STREAMS_0_TOPIC
IGGY_CONNECTORS_SOURCE_MONGODB_PATH
```

---

## 7. Unit Test Convention

All unit tests must follow `given_{precondition}_should_{expected_behavior}`:

```rust
fn given_no_initial_offset_should_start_from_beginning()
fn given_bson_payload_format_should_return_schema_raw()
fn given_transient_timeout_error_should_retry()
fn given_auth_failure_should_not_retry()
fn given_snake_case_fields_enabled_should_convert_keys()
fn given_connection_uri_with_credentials_should_redact()
```

Target: 1:1+ test-to-method ratio. Integration tests use descriptive names without the `given_should` pattern.

---

## 8. Dependencies

### Sink Cargo.toml

```toml
[dependencies]
async-trait = { workspace = true }
dashmap = { workspace = true }
futures = { workspace = true }
humantime = { workspace = true }
iggy_common = { workspace = true }
iggy_connector_sdk = { workspace = true }
mongodb = { version = "3.0", default-features = false, features = ["rustls-tls"] }
once_cell = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
simd-json = { workspace = true }
tokio = { workspace = true }
tracing = { workspace = true }

[package.metadata.cargo-machete]
ignored = ["dashmap", "once_cell", "futures", "simd-json"]  # Required by SDK macros
```

### Source Cargo.toml

Same as sink, plus:
```toml
uuid = { workspace = true }        # For message ID generation
chrono = { workspace = true }       # If needed for timestamp handling
```

---

## 9. Future Work (Out of Scope for v1)

| Feature | Why Deferred | When to Add |
|---|---|---|
| MongoDB Change Streams (CDC) | Fundamentally different architecture (cursor-based, not slot-based like PostgreSQL). Requires `bulk_write()` for mixed ops. | v2, after polling mode is stable |
| Aggregation pipeline support | Complex feature, low initial demand | When users request it |
| Connection pool metrics | Nice-to-have observability | When runtime metrics are expanded |
| Multi-collection source | HashMap state is forward-compatible. Config change needed (`collections: Vec<String>`). | When users need it |

---

## 10. Open Questions for Maintainers

These are areas where we'd appreciate maintainer input before implementation:

1. **Field naming convention**: We chose `connection_uri` following MongoDB's own naming. Would you prefer consistency with PostgreSQL's `connection_string` across all database connectors?

2. **Error swallowing in sinks**: The current pattern (PostgreSQL, Elasticsearch) logs batch errors but returns `Ok(())`. Should we consider propagating errors for MongoDB, or is this the intentional design?

3. **`insert_many` vs `bulk_write`**: We chose `insert_many` for broader server compatibility. If apache/iggy targets MongoDB 8.0+ as minimum, we'd switch to `bulk_write`.

4. **Test infrastructure**: We plan to use testcontainers with the `GenericImage` pattern (like Elasticsearch). Any preference for a specific MongoDB version in tests?

5. **Connector runtime registration**: The `local_provider.rs` and `main.rs` need to know about the new connector. Is there a preferred process for registering new connectors?

---

*This document was produced through systematic gap analysis comparing a prototype implementation against the original spec, existing iggy connector patterns, and industry research across Kafka Connect, Debezium, Flink, and Airbyte MongoDB connectors.*
