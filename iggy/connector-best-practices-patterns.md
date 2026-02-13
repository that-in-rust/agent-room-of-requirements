# Apache Iggy Connectors: Best Practices & Patterns Guide

**Date**: February 8, 2026
**Repository**: apache/iggy
**Analysis Method**: Parseltongue v1.5.6 dependency graph analysis
**Codebase**: 15,637 code entities, 76,133 dependency edges

---

## 1. Architecture Overview

### 1.1 Layered Architecture (from Parseltongue Semantic Clusters)

```
core/connectors/
  sdk/                   (151 entities) - Trait definitions, message types, codecs, transforms
    src/lib.rs           - Core traits: Sink, Source, StreamEncoder, StreamDecoder
    src/sink.rs          - SinkContainer (runtime wrapper)
    src/source.rs        - SourceContainer (runtime wrapper)
    src/encoders/        - JSON, Raw, Text encoders
    src/decoders/        - JSON, Raw, Text decoders
    src/transforms/      - AddFields, DeleteFields, UpdateFields, FilterFields, FlatbufferConvert
    src/log.rs           - Logging utilities (CallbackLayer, tracing integration)

  runtime/               (293 entities) - Plugin loading, lifecycle, config, API
    src/main.rs          - Entry point, plugin loading via C FFI
    src/sink.rs          - Sink lifecycle management (6 functions)
    src/source.rs        - Source lifecycle management (8 functions)
    src/manager/         - SinkManager, SourceManager, ConnectorStatus
    src/configs/         - Config providers (local TOML, HTTP), 136 entities
    src/api/             - REST API (64 entities): CRUD for configs, metrics, stats
    src/state.rs         - StateProvider trait, FileStateProvider
    src/stats.rs         - Runtime statistics
    src/metrics/         - Prometheus metrics (32 entities, cluster #59)
    src/transform.rs     - Transform pipeline orchestration

  sinks/                 - Sink implementations (plugins)
    stdout_sink/         (8 entities)  - Reference implementation
    quickwit_sink/       (11 entities) - Search engine sink
    elasticsearch_sink/  (11 entities) - Search engine sink
    postgres_sink/       (54 entities) - Database sink
    iceberg_sink/        (47 entities) - Data lake sink

  sources/               - Source implementations (plugins)
    random_source/       (11 entities) - Reference implementation
    elasticsearch_source/(40 entities) - Search engine source
    postgres_source/     (56 entities) - Database source
```

### 1.2 Plugin Model

From Parseltongue's `main.rs` entity analysis, the runtime loads connectors as dynamic libraries via C FFI:

```
Runtime Main Structs:
  SinkConnector -> SinkConnectorPlugin -> SinkConnectorWrapper -> SinkWithPlugins
  SourceConnector -> SourceConnectorPlugin -> SourceConnectorWrapper -> SourceWithPlugins
```

Each connector is compiled as a separate shared library (`cdylib`) and loaded at runtime via `resolve_plugin_path`.

---

## 2. Core Traits: The Connector Contract

### 2.1 The `Sink` Trait

**Location**: `core/connectors/sdk/src/lib.rs`
**Blast Radius**: 494 entities at 2 hops (high impact - changes here affect the entire ecosystem)

The Sink trait defines the contract for consuming messages from Iggy and writing to external systems:

**Required Methods** (derived from all 5 implementations):
| Method | Purpose | Called By |
|--------|---------|-----------|
| `new(config)` | Construct from TOML config | Runtime plugin loader |
| `open()` | Initialize connections/resources | Runtime lifecycle |
| `consume(messages)` | Process a batch of messages | Runtime message loop |
| `close()` | Cleanup connections/resources | Runtime shutdown |

**Implementations** (from Parseltongue blast radius analysis):
1. `StdoutSink` - 4 methods (minimum viable)
2. `QuickwitSink` - 7 methods (+ `create_index`, `has_index`, `ingest`)
3. `ElasticsearchSink` - 7 methods (+ `create_client`, `ensure_index_exists`, `bulk_index_documents`)
4. `PostgresSink` - 18 methods (+ connection pooling, batching, retry, format handling)
5. `IcebergSink` - 16 methods (+ routing, catalog mgmt, S3 integration)

### 2.2 The `Source` Trait

**Location**: `core/connectors/sdk/src/lib.rs`
**Blast Radius**: 5 entities at 2 hops (smaller footprint than Sink)

**Required Methods**:
| Method | Purpose | Called By |
|--------|---------|-----------|
| `new(config)` | Construct from TOML config | Runtime plugin loader |
| `open()` | Initialize connections/resources | Runtime lifecycle |
| `poll()` | Fetch new messages from external system | Runtime polling loop |
| `close()` | Cleanup connections/resources | Runtime shutdown |

**Implementations**:
1. `RandomSource` - 6 methods (minimum + `generate_messages`, `generate_random_text`)
2. `ElasticsearchSource` - 24 methods (+ state management, auto-save, search)
3. `PostgresSource` - 25 methods (+ CDC, polling, replication parsing)

### 2.3 Supporting Traits

| Trait | Location | Purpose |
|-------|----------|---------|
| `StreamEncoder` | `sdk/src/lib.rs` | Serialize messages for sinks (JSON, Raw, Text) |
| `StreamDecoder` | `sdk/src/lib.rs` | Deserialize messages from sources |
| `Transform` | `sdk/src/transforms/mod.rs` | Per-field message transformations |
| `ConnectorsConfigProvider` | `runtime/src/configs/connectors.rs` | Load connector configurations |
| `StateProvider` | `runtime/src/state.rs` | Persist connector state across restarts |
| `Router` | `sinks/iceberg_sink/src/router/mod.rs` | Route messages to different destinations |
| `StateStorage` | `sources/elasticsearch_source/src/state_manager.rs` | Source-specific state persistence |

---

## 3. Patterns Derived from Codebase Analysis

### 3.1 Pattern: Minimal Sink (StdoutSink - 8 entities)

The simplest possible sink. Use as your starting template:

**Entity Structure**:
```
Structs:
  StdoutSink         - Main connector struct
  StdoutSinkConfig   - Deserialized TOML configuration
  State              - Internal mutable state

Methods:
  new(config)        - Parse config, initialize state
  open()             - No-op or connection setup
  consume(messages)  - Core processing logic
  close()            - Cleanup
```

**Key Insight**: Every sink needs exactly 3 structs (Connector, Config, State) and 4 methods.

### 3.2 Pattern: Minimal Source (RandomSource - 11 entities)

**Entity Structure**:
```
Structs:
  RandomSource       - Main connector struct
  RandomSourceConfig - Deserialized TOML configuration
  Record             - Domain-specific data model
  State              - Internal mutable state

Methods:
  new(config)             - Parse config, initialize state
  open()                  - Setup
  poll()                  - Core data fetching logic
  close()                 - Cleanup
  generate_messages()     - Helper for message creation
  generate_random_text()  - Helper for data generation
```

**Key Insight**: Sources follow the same 3+1 struct pattern (Connector, Config, State + optional domain model) with `poll()` instead of `consume()`.

### 3.3 Pattern: Search Engine Connector (Elasticsearch, Quickwit)

Both search engine sinks follow an identical method signature pattern:

```
ElasticsearchSink methods: new, open, consume, close, create_client, ensure_index_exists, bulk_index_documents
QuickwitSink methods:      new, open, consume, close, (implicit client), create_index, has_index, ingest
```

**Shared Pattern**:
1. `new()` - Parse config
2. `open()` - Create HTTP client, ensure index/collection exists
3. `consume()` - Bulk-index documents via HTTP API
4. `close()` - Flush and disconnect

**Best Practice**: When writing a search engine sink:
- Create client connection in `open()`, not `new()`
- Use bulk/batch APIs for ingestion (not per-document)
- Handle index creation idempotently (check if exists first)
- Keep entity count low (11 entities = manageable complexity)

### 3.4 Pattern: Database Connector (PostgreSQL - 54+56 entities)

The most feature-rich pattern. Key additions over minimal:

**Sink extras** (18 methods):
- `connect()`, `get_pool()` - Connection pooling
- `build_batch_insert_query()`, `bind_and_execute_batch()` - SQL batching
- `execute_batch_insert_with_retry()`, `get_max_retries()`, `get_retry_delay()` - Retry logic
- `payload_format()`, `process_messages()` - Format handling (JSON, Raw, Bytea)
- `ensure_table_exists()` - Schema management
- `from_config()` - Builder pattern
- `parse_timestamp()`, `sql_type()` - Type mapping
- 29 test functions - Comprehensive unit tests

**Source extras** (25 methods):
- `poll_tables()`, `poll_cdc()`, `poll_cdc_builtin()` - Multiple polling strategies
- `setup_cdc()` - CDC initialization
- `parse_insert_message()`, `parse_update_message()`, `parse_delete_message()` - Replication parsing
- `mark_or_delete_processed_rows()` - Processing mode (mark vs delete)
- `substitute_query_params()`, `validate_custom_query()` - Custom query support
- `extract_column_value()`, `extract_payload_column()` - Data extraction
- `build_polling_query()`, `format_offset_value()` - Query building
- 23 test functions

**Best Practice**: When writing a database connector:
- Always implement connection pooling
- Support multiple payload formats via `PayloadFormat` enum
- Implement retry with configurable max_retries and retry_delay
- Use batch operations (multi-row INSERT, bulk UPDATE)
- Add `from_config()` builder for clean initialization
- Include comprehensive unit tests (test-to-method ratio ~1.5:1)

### 3.5 Pattern: Data Lake Connector (Iceberg - 47 entities)

The most architecturally complex pattern, introducing the `Router` trait:

**Unique Architecture**:
```
Router trait (in iceberg_sink/src/router/mod.rs)
  StaticRouter  - Fixed table mapping from config
  DynamicRouter - Route based on message field values (extract_route_field)

DynamicWriter  - Per-table writer management (load_table_if_exists, push_to_existing)
JsonArrowReader - Convert JSON to Arrow format (fill_buf, read, load_next)
```

**Catalog & Storage Functions** (10 standalone functions):
- `init_catalog()`, `get_rest_catalog()` - Catalog initialization
- `init_props()`, `get_props_s3()` - Storage configuration
- `write_data()` - Core write operation
- `table_exists()`, `is_valid_namespaced_table()`, `slice_user_table()` - Table management
- `get_partition_type_value()`, `primitive_type_to_literal()` - Type conversion

**Best Practice**: When writing a data lake connector:
- Consider implementing the `Router` trait for multi-table fan-out
- Separate catalog/storage initialization from connector lifecycle
- Use standalone functions for complex initialization logic
- Support both static (config-driven) and dynamic (field-driven) routing

---

## 4. Configuration Patterns

### 4.1 Per-Connector TOML Configuration

After Issue #2318, each connector has its own TOML config file. Structure:

```
configs/
  sinks/
    postgres.toml        - PostgresSinkConfig
    elasticsearch.toml   - ElasticsearchSinkConfig
    iceberg.toml         - IcebergSinkConfig
  sources/
    postgres.toml        - PostgresSourceConfig
    elasticsearch.toml   - ElasticsearchSourceConfig
```

**Best Practice**:
- Config struct must be `Deserialize`-able from TOML
- Name config files with `.toml` extension only (Issue #2507)
- Support environment variable overrides for array and string fields (PR #2579)

### 4.2 Config Providers (136 entities in runtime/configs)

Two provider implementations:
1. **Local Provider** (`local_provider.rs`, 105 coupling) - Reads TOML files from directories
2. **HTTP Provider** - Fetches from remote APIs (Issue #2388), with retry mechanism (Issue #2416)

Both implement the `ConnectorsConfigProvider` trait with `ProviderState` for lifecycle management.

### 4.3 TLS Configuration

After Issue #2319, all connectors support optional TLS for the Iggy TCP connection:

```toml
[iggy]
address = "localhost:8090"
[iggy.tls]
enabled = true
ca_file = "/path/to/ca.pem"
```

---

## 5. Message Flow Patterns

### 5.1 SDK Message Types

From Parseltongue entity analysis of `sdk/src/lib.rs`:

```
Message Flow (Sink):
  ReceivedMessage -> StreamDecoder -> DecodedMessage -> Transform -> Sink.consume()

Message Flow (Source):
  Source.poll() -> ProducedMessage -> StreamEncoder -> RawMessage -> Iggy

Supporting Types:
  ConsumedMessage    - Message consumed from Iggy stream
  MessagesMetadata   - Batch metadata (topic, partition info)
  TopicMetadata      - Topic-level metadata
  RawMessages        - Raw bytes batch
  ProducedMessages   - Batch of produced messages
  Payload            - Enum: JSON | Raw | Text | Protobuf | FlatBuffers
  Schema             - Enum for serialization schemas
  ConnectorState     - Persistent connector state
```

### 5.2 Encoder/Decoder Implementations

| Format | Encoder | Decoder | Location |
|--------|---------|---------|----------|
| JSON | `JsonStreamEncoder` | `JsonStreamDecoder` | `sdk/src/encoders/json.rs`, `sdk/src/decoders/json.rs` |
| Raw | `RawStreamEncoder` | `RawStreamDecoder` | `sdk/src/encoders/raw.rs`, `sdk/src/decoders/raw.rs` |
| Text | `TextStreamEncoder` | `TextStreamDecoder` | `sdk/src/encoders/text.rs`, `sdk/src/decoders/text.rs` |

Each encoder/decoder follows the same pattern: struct definition + 2 methods (`new`, `encode`/`decode`).

**Best Practice**: When adding a new codec (e.g., Avro, BSON):
1. Create `sdk/src/encoders/{format}.rs` and `sdk/src/decoders/{format}.rs`
2. Implement `StreamEncoder` / `StreamDecoder` traits
3. Add variant to `Payload` enum in `sdk/src/lib.rs`
4. Register in `sdk/src/encoders/mod.rs` and `sdk/src/decoders/mod.rs`

### 5.3 Transform Pipeline

Transforms modify messages between decoding and consumption. Available transforms:

| Transform | File | Methods |
|-----------|------|---------|
| `AddFields` | `add_fields.rs` | `new`, `transform`, `fmt` |
| `DeleteFields` | `delete_fields.rs` | `new`, `transform`, `fmt`, `delete` |
| `UpdateFields` | `update_fields.rs` | `new`, `transform`, `fmt` |
| `FilterFields` | `filter_fields.rs` | `new`, `transform`, `fmt`, `matches` + enums for operators |
| `FlatbufferConvert` | `flatbuffer_convert.rs` | `new`, `transform`, `fmt` + 3 impl blocks |

**Best Practice**: When adding a new transform:
1. Create `sdk/src/transforms/{name}.rs`
2. Implement `Transform` trait
3. Add config struct for TOML deserialization
4. Register in `sdk/src/transforms/mod.rs`

---

## 6. Testing Patterns

### 6.1 Unit Tests Within Connector

From Parseltongue analysis, the database connectors embed unit tests directly:
- `postgres_sink`: 29 test functions (prefix: `given_*_should_*`)
- `postgres_source`: 23 test functions (same naming pattern)

**Naming Convention**: `given_{precondition}_should_{expected_behavior}`

Examples:
```
given_all_options_enabled_should_build_full_insert_query
given_batch_of_3_rows_should_build_multi_row_insert_query
given_connection_string_with_credentials_should_redact
given_empty_identifier_should_fail
given_json_format_should_return_json
```

### 6.2 Integration Tests

From Parseltongue analysis, integration tests live in `core/integration/`:

```
core/integration/
  src/harness/
    handle/     (18 entities) - Test connector lifecycle handles
    config/     (3 entities)  - Test configuration
```

**Best Practice** (from PR #2667):
- Use `iggy_harness` proc macro for integration test setup
- Follow the pattern established in PR #2579 (Postgres e2e tests)
- Use Docker containers for external dependencies (Quickwit, Elasticsearch, PostgreSQL)
- Test: basic operation, batch behavior, error handling for invalid payloads

### 6.3 Test-to-Code Ratios (from Parseltongue)

| Connector | Code Entities | Test Functions | Ratio |
|-----------|---------------|----------------|-------|
| stdout_sink | 8 | 0 | 0:1 (reference only) |
| quickwit_sink | 11 | 0 | 0:1 |
| elasticsearch_sink | 11 | 0 | 0:1 |
| postgres_sink | 25 (methods) | 29 | 1.16:1 |
| iceberg_sink | 47 | 0 | 0:1 |
| random_source | 11 | 0 | 0:1 |
| elasticsearch_source | 40 | 0 | 0:1 |
| postgres_source | 33 (methods) | 23 | 0.70:1 |

**Target**: Aim for ~1:1 test-to-method ratio for production connectors. The PostgreSQL connectors set the standard.

---

## 7. Observability Patterns (PR #2633, #2660)

### 7.1 Metrics

The runtime exposes Prometheus metrics at `/metrics`:
- **Runtime Gauges**: sources/sinks total count, running count
- **Per-Connector Counters**: messages produced/sent (source), consumed/processed (sink), errors
- **System Metrics**: CPU/memory usage, uptime

### 7.2 Stats

JSON stats endpoint at `/stats` includes:
- Per-connector version info (from `version()` FFI export)
- Connector status (from `ConnectorStatus` enum in manager)

### 7.3 Runtime API Endpoints

From Parseltongue (64 entities in `runtime/api/`):

| Category | Endpoints |
|----------|-----------|
| Sinks | `get_sinks`, `get_sink`, `get_sink_config`, `get_sink_configs`, `get_sink_active_config`, `update_sink_active_config`, `get_sink_plugin_config`, `get_sink_transforms`, `create_sink_config`, `delete_sink_config` |
| Sources | `get_sources`, `get_source`, `get_source_config`, `get_source_configs`, `get_source_active_config`, `update_source_active_config`, `get_source_plugin_config`, `get_source_transforms`, `create_source_config`, `delete_source_config` |
| System | `get_metrics`, `get_stats`, `init`, `configure_cors`, `resolve_api_key` |

---

## 8. Complexity Analysis & Antipatterns

### 8.1 Complexity Hotspots (Parseltongue)

| Rank | Entity | Coupling | Risk Level |
|------|--------|----------|------------|
| #52 | `sources/postgres_source/src/lib.rs` | 147 | High - Consider splitting |
| #83 | `runtime/src/source.rs` | 110 | Medium - Runtime internal |
| #87 | `runtime/src/sink.rs` | 109 | Medium - Runtime internal |
| #91 | `runtime/configs/local_provider.rs` | 105 | Medium - Config complexity |

### 8.2 Healthy Signals

- **Zero circular dependencies** across the entire codebase
- Clean trait hierarchy (no diamond inheritance patterns)
- SDK traits have small surface area (4 methods each)
- Encoder/decoder pairs are symmetric and isolated

### 8.3 Antipatterns to Avoid

1. **God connector**: Postgres source has 25 methods and 147 coupling. If your connector grows beyond ~15 methods, consider extracting helpers into separate modules.
2. **Missing state management**: Simple sinks (Quickwit, Stdout) don't persist state. For connectors that need exactly-once or at-least-once semantics, implement `StateProvider`.
3. **Monolithic config**: Issue #2318 taught that a single config file doesn't scale. Always use per-connector config files.
4. **No retry logic**: Issue #2416 showed that HTTP-based operations need exponential backoff. Always add retry for network operations.

---

## 9. Checklist: Implementing a New Connector

### 9.1 Sink Connector

- [ ] Create `core/connectors/sinks/{name}_sink/` crate
- [ ] Define `{Name}Sink` struct, `{Name}SinkConfig` struct, `State` struct
- [ ] Implement `Sink` trait: `new()`, `open()`, `consume()`, `close()`
- [ ] Add TOML config file to `configs/sinks/{name}.toml`
- [ ] Register in `runtime/src/configs/connectors/local_provider.rs`
- [ ] Add to `runtime/src/main.rs` plugin resolution
- [ ] Add Cargo.toml with `crate-type = ["cdylib"]`
- [ ] Add unit tests (target: 1:1 method-to-test ratio)
- [ ] Add integration tests in `core/integration/`
- [ ] Add version FFI export via SDK macros

### 9.2 Source Connector

- [ ] Create `core/connectors/sources/{name}_source/` crate
- [ ] Define `{Name}Source` struct, `{Name}SourceConfig` struct, `State` struct
- [ ] Implement `Source` trait: `new()`, `open()`, `poll()`, `close()`
- [ ] Implement state management if needed (`StateProvider` or custom)
- [ ] Add TOML config file to `configs/sources/{name}.toml`
- [ ] Register in `runtime/src/configs/connectors/local_provider.rs`
- [ ] Add to `runtime/src/main.rs` plugin resolution
- [ ] Add Cargo.toml with `crate-type = ["cdylib"]`
- [ ] Add unit tests
- [ ] Add integration tests

### 9.3 New Codec (Encoder/Decoder)

- [ ] Create `sdk/src/encoders/{format}.rs` and `sdk/src/decoders/{format}.rs`
- [ ] Implement `StreamEncoder` and `StreamDecoder` traits
- [ ] Add variant to `Payload` enum in `sdk/src/lib.rs`
- [ ] Add variant to `Schema` enum if schema-based
- [ ] Register modules in `sdk/src/encoders/mod.rs` and `sdk/src/decoders/mod.rs`
- [ ] Add unit tests for encode/decode roundtrip

---

## 10. Java Connector Patterns (Flink, Pinot)

### 10.1 Flink Connector (336 entities)

From Parseltongue analysis, the Java Flink connector follows Flink's standard Source/Sink API:

**Sink side**:
- `IggySink` -> `IggySinkBuilder` -> `IggySinkWriter` -> `IggyCommittable`
- Builder pattern for configuration
- Two-phase commit via `IggyCommittable`

**Source side**:
- `IggySource` -> `IggySourceBuilder` -> `IggySourceReader`
- Split-based: `IggySourceSplit` -> `IggySourceSplitEnumerator`
- State serialization: `IggySourceEnumeratorState` + `IggySourceEnumeratorStateSerializer`

**Serialization**:
- `SerializationSchema` / `DeserializationSchema` (traits/interfaces)
- `JsonSerializationSchema`, `JsonDeserializationSchema`, `StringDeserializationSchema`

### 10.2 Pinot Connector (72 entities)

- `IggyJsonMessageDecoder` - Custom Pinot decoder for Iggy messages
- Simpler architecture than Flink (Pinot has built-in ingestion framework)

**Best Practice**: External Java connectors use the framework's native APIs (Flink Source/Sink API, Pinot decoder API) rather than reimplementing the Rust SDK patterns.

---

## 11. Summary: Golden Rules

1. **Start with StdoutSink/RandomSource**: Copy the reference implementation and extend
2. **4 methods minimum**: `new()`, `open()`, `consume()`/`poll()`, `close()`
3. **3 structs minimum**: Connector, Config, State
4. **Per-connector TOML config**: One file per connector in the configs directory
5. **Batch operations**: Always use bulk/batch APIs for external systems
6. **Retry with backoff**: For any network operation
7. **Connection pooling**: For database connectors
8. **Unit test naming**: `given_{precondition}_should_{expected_behavior}`
9. **Zero circular dependencies**: Keep the trait hierarchy flat
10. **Keep entity count low**: Simple sinks ~11 entities, complex ~50 max

---

*Generated using Parseltongue v1.5.6 dependency graph analysis*
*Codebase: 15,637 entities, 76,133 edges, 0 circular dependencies*
*Workspace: parseltongue20260208133459*
