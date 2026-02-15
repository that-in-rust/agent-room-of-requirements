# Thesis: InfluxDB Connector for Apache Iggy (Issue #2700)

**Date**: February 15, 2026
**Issue**: [apache/iggy#2700](https://github.com/apache/iggy/issues/2700)
**Status**: Assigned to @ryerraguntla (Feb 15, 2026)
**Analysis Method**: Parseltongue v1.7.2 (15,998 entities, 78,896 edges) + External Research
**Author**: Research for contribution planning

---

## Governing Thesis

**The InfluxDB connector is a "Search Engine Layer" connector (like Quickwit/Elasticsearch), not a "Database Layer" connector (like Postgres).** It communicates via HTTP, uses bulk writes, has no connection pooling beyond reqwest, and needs no CDC/replication logic. The implementation should produce ~11-15 entities for the sink and ~20-30 for the source, staying firmly in the manageable middle of the complexity spectrum.

---

## 1. Issue Requirements

From issue #2700 (by @kparisa, Feb 7, 2026):
- **Sink**: Stream data from Iggy into InfluxDB (primary deliverable)
- **Source**: Ingest data from InfluxDB into Iggy (secondary, "design that can later support")
- **Use cases**: Metrics, observability, IoT, financial ticks, real-time analytics
- **Testing requirement** (from @hubcio, contributor): "finished task should contain extensive tests using testcontainers"

### Critical Context
- Issue is **already assigned** to @ryerraguntla as of Feb 15, 2026
- Any contribution should coordinate, not duplicate

---

## 2. Where This Fits in the Codebase (Parseltongue)

### 2.1 Entity Map — Existing Sinks (from Parseltongue fuzzy search)

| Connector | Entities | File Path | Pattern |
|-----------|----------|-----------|---------|
| `StdoutSink` | 3 (struct + impl + config) | `sinks/stdout_sink/src/lib.rs` | Minimal |
| `QuickwitSink` | 3 (struct + impl + config) | `sinks/quickwit_sink/src/lib.rs` | HTTP/Search |
| `ElasticsearchSink` | 4 (struct + impl + 2 configs) | `sinks/elasticsearch_sink/src/lib.rs` | HTTP/Search |
| `PostgresSink` | 3 + PayloadFormat enum | `sinks/postgres_sink/src/lib.rs` | Database |
| `IcebergSink` | 6 (struct + 2 impls + config + 2 enums) | `sinks/iceberg_sink/src/lib.rs` + `src/sink.rs` | Data Lake |

**InfluxDB Sink should follow the QuickwitSink/ElasticsearchSink pattern** — HTTP-based, bulk writes, single `lib.rs` file.

### 2.2 Entity Map — Existing Sources (from Parseltongue)

| Connector | Entities | File Path | Pattern |
|-----------|----------|-----------|---------|
| `RandomSource` | struct + impl + config | `sources/random_source/src/lib.rs` | Minimal |
| `ElasticsearchSource` | struct + impl + config + StateManager | `sources/elasticsearch_source/src/lib.rs` + `state_manager.rs` | HTTP/Stateful |
| `PostgresSource` | struct + impl + config | `sources/postgres_source/src/lib.rs` | Database/CDC |

**InfluxDB Source should follow ElasticsearchSource** — HTTP polling with state management for watermark tracking.

### 2.3 SDK Trait Contract (from Parseltongue)

The Sink trait lives at `core/connectors/sdk/src/lib.rs` (entity: `rust:trait:StreamEncoder:____core_connectors_sdk_src_lib:T1848364895`).

**SinkContainer** wraps all sinks: `rust:struct:SinkContainer:____core_connectors_sdk_src_sink:T1672295994`

Every sink implements exactly:

| Method | Where Called |
|--------|-------------|
| `new(config: Value)` | Runtime plugin loader |
| `open()` | Runtime lifecycle start |
| `consume(messages: &[ConsumedMessage], metadata: &MessagesMetadata)` | Runtime message loop (`runtime/src/sink.rs` → `consume()` → `consume_messages()`) |
| `close()` | Runtime shutdown |

The `consume()` function in `runtime/src/sink.rs` and `consume_messages()` are the runtime-side entry points that call the plugin's `consume()` method.

### 2.4 Runtime Infrastructure (from Parseltongue)

| Entity | File | Role |
|--------|------|------|
| `SinkManager` | `runtime/src/manager/sink.rs` | Lifecycle management |
| `SinkConfig` | `runtime/src/configs/connectors.rs` | Config deserialization |
| `SinkConfigFile` | `runtime/src/configs/connectors/local_provider.rs` | TOML file loading |
| `ConnectorStatus` | `sdk/src/api.rs` | Status enum |
| `resolve_plugin_path` | `runtime/src/main.rs` | Dynamic library loading |
| `RetryConfig` | `runtime/src/configs/runtime.rs` | Retry configuration |

### 2.5 Dependencies Already Available (from Parseltongue)

| Crate | Used By | Relevance to InfluxDB |
|-------|---------|----------------------|
| `reqwest` (Client, StatusCode) | Existing connectors | HTTP client for InfluxDB API |
| `reqwest_retry` (ExponentialBackoff, RetryTransientMiddleware) | Existing connectors | Retry for 5xx/429 |
| `testcontainers_modules` (AsyncRunner, HealthWaitStrategy) | Integration tests | InfluxDB testcontainer |
| `serde_json` | All connectors | JSON message parsing |
| `iggy_connector_sdk` (ConnectorError, Schema, Transform) | All connectors | SDK traits and types |

### 2.6 Test Infrastructure (from Parseltongue)

| Entity | File | Purpose |
|--------|------|---------|
| `iggy_harness` proc macro | `core/harness_derive/src/lib.rs` | Test setup automation |
| `ElasticsearchSinkFixture` | `external-dependency-sink` | Reference test fixture pattern |
| Test harness handle | `core/integration/src/harness/handle/` (18 entities) | Connector lifecycle test handles |
| Test harness config | `core/integration/src/harness/config/` (3 entities) | Test configuration |

---

## 3. InfluxDB Technical Profile (External Research)

### 3.1 Data Model

```
measurement,tag1=val1,tag2=val2 field1=value1,field2=value2 timestamp
└── table    └── indexed tags    └── non-indexed fields       └── nanosecond
```

- **Measurement** = table name (string)
- **Tags** = indexed string key-value pairs (for filtering/grouping)
- **Fields** = non-indexed data values (float64, int64, uint64, string, bool)
- **Timestamp** = nanosecond-capable epoch
- **Point uniqueness** = measurement + tag set + timestamp

### 3.2 Write Path

```
POST /api/v2/write?org={org}&bucket={bucket}&precision={precision}
Authorization: Token {token}
Content-Type: text/plain; charset=utf-8
Content-Encoding: gzip  (optional but recommended)

measurement,tag1=val1 field1=1.0,field2="hello" 1630525358000000000
measurement,tag1=val2 field1=2.5,field2="world" 1630525359000000000
```

- **Batch size**: 5,000-10,000 points per request (official recommendation)
- **Gzip**: Up to 5x write speed improvement
- **Tag sorting**: Lexicographic order improves write performance
- **Universal**: `/api/v2/write` works across InfluxDB 2.x, 3.x, and Cloud

### 3.3 Query Path (for Source)

- **No streaming/subscription API exists** in 2.x or 3.x
- Must poll with time-range queries + persistent high-water mark
- Query languages: SQL (v3 primary), Flux (v2, maintenance mode), InfluxQL (all versions)

### 3.4 Error Categories

| HTTP Code | Meaning | Retriable | Strategy |
|-----------|---------|-----------|----------|
| 204/200 | Success | — | — |
| 400 | Malformed line protocol | No | Log + DLQ |
| 401 | Auth failure | No | Halt |
| 413 | Payload too large | No | Split batch |
| 422 | Schema conflict | No | Log + DLQ |
| 429 | Rate limited | Yes | Backoff per Retry-After |
| 5xx | Server error | Yes | Exponential backoff + jitter |

### 3.5 Rust Client Landscape

**No official Rust client exists.** Community crates are alpha-quality. The recommendation is to use `reqwest` directly — the API is a single POST endpoint for writes and queries.

### 3.6 Version Targeting

**Target `/api/v2/write` for maximum compatibility** — works on InfluxDB 2.x, 3.x Core, 3.x Enterprise, and all Cloud variants. Query support should be version-aware (SQL for 3.x, Flux/InfluxQL for 2.x).

---

## 4. Implementation Blueprint

### 4.1 File Structure

```
core/connectors/
  sinks/
    influxdb_sink/
      Cargo.toml                    # cdylib, depends on reqwest, serde, iggy_connector_sdk
      src/
        lib.rs                      # InfluxdbSink, InfluxdbSinkConfig, State, line protocol builder
  sources/
    influxdb_source/
      Cargo.toml
      src/
        lib.rs                      # InfluxdbSource, InfluxdbSourceConfig, State
        state_manager.rs            # High-water mark persistence (follow ES source pattern)
  configs/
    sinks/
      influxdb.toml                 # Sink config template
    sources/
      influxdb.toml                 # Source config template
```

### 4.2 Sink Struct Design (following QuickwitSink pattern from Parseltongue)

```
InfluxdbSink (struct)              — Main connector
InfluxdbSinkConfig (struct)        — TOML config deserialization
State (struct)                     — Internal mutable state (client, stats)
MeasurementSource (enum)           — Field | Topic | Static
Precision (enum)                   — Nanosecond | Microsecond | Millisecond | Second

Methods:
  new(config)                      — Parse TOML, validate
  open()                           — Create reqwest::Client, health check InfluxDB
  consume(messages, metadata)      — Convert JSON → line protocol, batch write
  close()                          — Flush pending, drop client
  build_line_protocol(msg)         — JSON message → line protocol string (private)
  write_batch(lines)               — POST to /api/v2/write with retry (private)
  health_check()                   — GET /health (private)
```

**Estimated entity count: ~11-15** (matching QuickwitSink/ElasticsearchSink scale)

### 4.3 Source Struct Design (following ElasticsearchSource pattern)

```
InfluxdbSource (struct)            — Main connector
InfluxdbSourceConfig (struct)      — TOML config deserialization
State (struct)                     — Internal state (client, watermark)
StateManager (struct)              — Watermark persistence (in state_manager.rs)
QueryLanguage (enum)               — Sql | Flux | InfluxQL

Methods:
  new(config)                      — Parse TOML, validate
  open()                           — Create client, detect InfluxDB version, init state
  poll()                           — Time-range query from watermark, convert results to messages
  close()                          — Persist watermark, drop client
  execute_query(query)             — Run query against InfluxDB (private)
  detect_version()                 — Auto-detect v2 vs v3 (private)
  row_to_message(row)              — Query result row → Iggy ProducedMessage (private)
```

**Estimated entity count: ~20-25** (matching ElasticsearchSource scale)

### 4.4 TOML Configuration (Sink)

```toml
[sink]
type = "influxdb"

[sink.influxdb]
# Connection
url = "http://localhost:8086"
token = "${INFLUX_TOKEN}"
org = "my-org"
bucket = "my-bucket"
precision = "ms"                    # ns, us, ms, s

# Message → Line Protocol Mapping
measurement_from = "field"          # "field", "topic", "static"
measurement_field = "measurement"   # when measurement_from = "field"
measurement_name = ""               # when measurement_from = "static"
tag_fields = ["host", "region"]     # JSON fields extracted as tags
timestamp_field = "timestamp"       # JSON field for timestamp (optional)
timestamp_format = "epoch_ms"       # epoch_ns, epoch_us, epoch_ms, epoch_s, rfc3339

# Performance
batch_size = 5000
gzip = true

# Retry
max_retries = 3
retry_backoff_ms = 1000
```

### 4.5 TOML Configuration (Source)

```toml
[source]
type = "influxdb"

[source.influxdb]
url = "http://localhost:8086"
token = "${INFLUX_TOKEN}"
org = "my-org"
bucket = "my-bucket"

# Query
measurement = "temperature"
query_language = "sql"              # sql (v3), flux (v2), influxql (all)
custom_query = ""                   # optional override
poll_interval_ms = 5000
buffer_duration_s = 10              # lag behind "now"
page_size = 1000

# Output
output_format = "json"
```

### 4.6 Cargo.toml (Sink)

```toml
[package]
name = "influxdb_sink"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["cdylib"]

[dependencies]
iggy_connector_sdk = { path = "../../sdk" }
reqwest = { version = "0.12", features = ["json", "gzip"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
tokio = { version = "1", features = ["full"] }
toml = "0.8"
tracing = "0.1"
flate2 = "1"                       # gzip compression for line protocol
urlencoding = "2"
async-trait = "0.1"
```

---

## 5. Key Design Decisions

### 5.1 Why reqwest, not an InfluxDB client crate?

From Parseltongue, `reqwest` is already an external dependency used across the connector ecosystem (`external-dependency-reqwest`). No InfluxDB Rust client is mature enough. The API is two endpoints: POST for write, POST for query. Adding a dependency would add risk with no benefit.

### 5.2 Why follow QuickwitSink, not PostgresSink?

| Dimension | QuickwitSink | PostgresSink | InfluxDB Need |
|-----------|-------------|-------------|---------------|
| Protocol | HTTP | TCP (libpq) | HTTP |
| Connection | reqwest client | Connection pool | reqwest client |
| Write method | Bulk POST | Batch INSERT | Bulk POST |
| Retry | HTTP-level | Transaction-level | HTTP-level |
| Entity count | 11 | 54 | ~11-15 (target) |
| State management | None | Complex | Watermark only |

InfluxDB's write path is closer to a search engine (HTTP bulk API) than a database (connection pool + SQL).

### 5.3 Line Protocol Generation: Custom vs. Crate

Build it custom. The line protocol format is simple (one function), the escaping rules are documented, and the `influxdb-line-protocol` crate from InfluxData is a parser (read), not a writer. Building a `build_line_protocol()` method keeps dependencies minimal and the code auditable.

### 5.4 Source Polling Strategy

InfluxDB has no subscription/streaming API. Must poll. Follow the ElasticsearchSource pattern from Parseltongue:
- `StateManager` in a separate `state_manager.rs` (entity: `rust:impl:StateManager:____core_connectors_sources_elasticsearch_source_src_state_manager:T1729629500`)
- Persist high-water mark (last processed timestamp) to survive restarts
- Buffer duration: don't query too close to "now" to avoid reading in-flight data

### 5.5 Version Compatibility

Target `/api/v2/write` — it's universal. Auto-detect InfluxDB version via `/health` for query path:
- v3 detected → use SQL via `/api/v3/query_sql`
- v2 detected → use Flux via `/api/v2/query`
- InfluxQL available as fallback for both

---

## 6. Testing Plan

### 6.1 Unit Tests (in `lib.rs`)

Follow the PostgresSink naming convention from Parseltongue:
```
given_{precondition}_should_{expected_behavior}
```

**Sink unit tests:**
- `given_json_message_with_all_fields_should_build_correct_line_protocol`
- `given_message_with_special_chars_should_escape_tags_and_fields`
- `given_measurement_from_topic_should_use_topic_name`
- `given_measurement_from_field_should_extract_field_value`
- `given_static_measurement_should_use_config_name`
- `given_timestamp_as_epoch_ms_should_convert_to_precision`
- `given_timestamp_as_rfc3339_should_parse_correctly`
- `given_missing_fields_should_return_error`
- `given_empty_batch_should_skip_write`
- `given_gzip_enabled_should_compress_payload`
- `given_tag_fields_config_should_extract_only_configured_tags`
- `given_multiple_messages_should_batch_into_single_request`

**Source unit tests:**
- `given_json_response_should_parse_into_messages`
- `given_empty_response_should_return_empty_vec`
- `given_watermark_should_query_from_last_position`
- `given_v3_detected_should_use_sql_query`
- `given_v2_detected_should_use_flux_query`

**Target: ~15-20 unit tests** (~1:1 method-to-test ratio)

### 6.2 Integration Tests (using testcontainers)

From Parseltongue, the test infrastructure uses:
- `iggy_harness` proc macro (`core/harness_derive/src/lib.rs`)
- `testcontainers_modules` with `AsyncRunner` and `HealthWaitStrategy`
- Fixtures in `core/integration/src/harness/`

**Integration test plan:**
- Spin up InfluxDB 2.x container via testcontainers
- Test: write single point → verify in InfluxDB
- Test: batch write → verify all points
- Test: write with all tag/field types
- Test: write with gzip
- Test: retry on simulated 5xx
- Test: source poll → verify messages match written data
- Test: source watermark persistence across restarts

Follow PR #2579 (Postgres e2e) and #2594 (Quickwit e2e) patterns.

---

## 7. Complexity Assessment

### 7.1 Predicted Entity Counts

| Component | Predicted | Reference |
|-----------|-----------|-----------|
| `InfluxdbSink` (struct + impl + config) | ~12 | QuickwitSink: 11, EsSink: 11 |
| `InfluxdbSource` (struct + impl + config + state) | ~22 | EsSource: 40 (we're simpler) |
| Unit tests | ~20 | PostgresSink: 29 |
| Integration tests | ~8-10 | Quickwit e2e: ~5 |
| **Total** | **~62-64** | — |

### 7.2 Risk Assessment

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Line protocol escaping bugs | Medium | Extensive unit tests with special characters |
| InfluxDB version detection failure | Low | Default to v2 API (universal) |
| Timestamp precision mismatch | Medium | Validate precision in config, convert at ingestion |
| Testcontainer InfluxDB image issues | Low | Pin specific Docker image version |
| Scope creep into full v3 API | Medium | v1 targets v2 write API only, v3 native as follow-up |

---

## 8. Implementation Order

### Phase 1: Sink (MVP)
1. Create `core/connectors/sinks/influxdb_sink/` crate with Cargo.toml
2. Implement `InfluxdbSink` struct with `new()`, `open()`, `consume()`, `close()`
3. Implement `build_line_protocol()` for JSON → line protocol conversion
4. Implement `write_batch()` with reqwest + gzip + retry
5. Add TOML config file
6. Write unit tests (~12 tests)
7. Write integration tests with testcontainers (~5 tests)

### Phase 2: Source
8. Create `core/connectors/sources/influxdb_source/` crate
9. Implement `InfluxdbSource` with time-range polling
10. Implement `StateManager` for watermark persistence
11. Add version detection (v2 vs v3 query path)
12. Write unit tests (~8 tests)
13. Write integration tests (~3-5 tests)

### Phase 3: Polish
14. Add to Cargo workspace
15. Register in runtime plugin resolution
16. Add version FFI export via SDK macros
17. Documentation and config examples

---

## 9. Relationship to Other Open Issues

| Issue | Relationship |
|-------|-------------|
| #1846 (Avro payload) | InfluxDB connector could benefit from Avro support for schema evolution, but is not blocked by it |
| #2683 (simd_json bug) | If ElasticsearchSink uses simd_json, InfluxDB should use standard serde_json to avoid the same bug |
| #2712 (Linux metadata) | Runtime bug — affects all connectors equally, not specific to InfluxDB |
| #2539 (ClickHouse) | Similar complexity level, could share HTTP connector patterns |
| #2540 (Redshift) | Different pattern (S3 staging), not directly related |

---

## 10. Minto Pyramid Summary

**Governing Thought**: InfluxDB is an HTTP-based time-series database. The Iggy connector should follow the QuickwitSink/ElasticsearchSink pattern (HTTP bulk API, ~11 entities for sink), not the PostgresSink pattern (connection pool, CDC, 54 entities). The key technical challenge is the JSON-to-line-protocol transformation, which is a single well-defined function.

**Supporting Arguments**:
1. InfluxDB's write API is a single POST endpoint with line protocol in the body — identical in structure to Quickwit's bulk ingest API
2. No official Rust client exists; `reqwest` (already a dependency per Parseltongue) is the right tool
3. The source connector requires time-range polling with watermark (no streaming API in InfluxDB) — follow ElasticsearchSource pattern from `state_manager.rs`
4. Tests must use testcontainers (per @hubcio's comment) — infrastructure already exists in `core/integration/`

**Bottom Line**: ~62 entities total, 2-phase delivery (sink first, source second), grounded entirely in existing codebase patterns.

---

*Parseltongue v1.7.2: 15,998 entities, 78,896 edges | Workspace: parseltongue20260215210700*
*External research: InfluxDB 2.x/3.x API docs, Confluent Kafka connector, Telegraf, Rust crate ecosystem*
*Cross-repo knowledge base: 4 prior documents (patterns, resolved issues, minto pyramid, complete tracker)*
