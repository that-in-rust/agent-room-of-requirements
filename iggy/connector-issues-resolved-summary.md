# Apache Iggy Connectors: Resolved Issues & Code Changes Summary

**Date**: February 8, 2026
**Repository**: apache/iggy (fork: amuldotexe/iggy)
**Analysis Method**: Parseltongue v1.5.6 dependency graph + GitHub CLI
**Codebase Scale**: 15,637 code entities, 76,133 dependency edges, 6 languages

---

## 1. Overview

The Apache Iggy connectors framework has undergone significant development since its initial introduction in June 2025. This document catalogs all resolved connector-related issues and their corresponding code changes, organized chronologically.

**Total Resolved Issues**: 12
**Total Merged PRs**: 17+
**Total Code Changes**: ~13,400+ lines added across 170+ files

---

## 2. Resolved Issues (Chronological)

### 2.1 Foundation Phase (Jun 2025)

#### Issue #1826 - Connectors Runtime (PR #1826)
- **Merged**: June 1, 2025
- **Scope**: +3,960 / -14 across 39 files
- **Description**: The foundational PR that introduced the entire connector runtime. Established the plugin-based architecture using C FFI for maximum performance. Created the `Sink` and `Source` traits, the runtime lifecycle (`new` -> `open` -> `consume/poll` -> `close`), and data transformation pipeline.
- **Code Impact (Parseltongue)**:
  - Created `core/connectors/runtime/` (293 entities across 11 modules: api, configs, manager, context, error, log, sink, source, state, stats, transform)
  - Created `core/connectors/sdk/` (151 entities including 4 core traits: `Sink`, `Source`, `StreamEncoder`, `StreamDecoder`)
  - Blast radius of `Sink` trait: 494 entities at 2 hops
  - Blast radius of `Source` trait: 5 entities at 2 hops

#### Issue #1848 - Extend JSON Field Transformations (PR ~Jun 2025)
- **Closed**: June 16, 2025
- **Description**: Extended the data transformation pipeline beyond the initial `add_fields` and `delete_fields` transforms. Added `update_fields` and `filter_fields` with support for key/value/regex-based filtering.
- **Code Impact (Parseltongue)**:
  - Transform modules in `sdk/src/transforms/`: `add_fields.rs`, `delete_fields.rs`, `update_fields.rs`, `filter_fields.rs`
  - `Transform` trait (1 trait, multiple impl blocks)
  - Each transform has: struct definition, config struct, `Transform` impl, `new`/`transform` methods

#### Issue #1845 - Protobuf Payload Support
- **Closed**: June 29, 2025
- **Description**: Implemented `StreamDecoder` and `StreamEncoder` for Protocol Buffers, with schema support via custom configuration and JSON conversion.
- **Code Impact (Parseltongue)**:
  - Added to `sdk/src/encoders/` and `sdk/src/decoders/`
  - Encoder/decoder pairs: JSON, Raw, Text (+ Protobuf)
  - Each pair follows identical pattern: struct + 2 method impls (`encode`/`decode`, `new`)

#### Issue #1844 - FlatBuffers Payload Support
- **Closed**: July 2, 2025
- **Description**: Implemented `StreamDecoder` and `StreamEncoder` for FlatBuffers with schema configuration.
- **Code Impact (Parseltongue)**:
  - `flatbuffer_convert.rs` in transforms: 3 impl blocks, 5 methods
  - Extended the `Schema` enum in `sdk/src/lib.rs` (alongside `Payload` and `Error` enums)

---

### 2.2 Connector Implementation Phase (Sep-Nov 2025)

#### Issue #1849 - PostgreSQL Connectors (PR #2579 extended)
- **Closed**: October 16, 2025
- **Description**: Full bidirectional PostgreSQL connector with CDC (Change Data Capture), table-based data fetching, and stream message storage.
- **Code Impact (Parseltongue)**:
  - `sinks/postgres_sink/`: 54 entities (struct `PostgresSink`, `PostgresSinkConfig`, `PayloadFormat` enum, plus 39+ test functions)
  - `sources/postgres_source/`: 56 entities (struct `PostgresSource`, `PostgresSourceConfig`, `PayloadFormat` enum, offset/polling logic, 41+ test functions)
  - Key methods: `new`, `open`, `consume` (sink), `poll` (source), `close`
  - Extended in PR #2579 (Jan 2026): +3,726 / -1,474 across 34 files adding JSON/raw format support, multiple processing modes (mark/delete), bytea column handling, comprehensive integration tests

#### Issue #1851 - Elasticsearch Connectors (PR #1872)
- **Closed (PR merged)**: November 18, 2025
- **Scope**: +2,079 / -36 across 17 files
- **Description**: Bidirectional Elasticsearch connector with batch processing, index management, and state tracking.
- **Code Impact (Parseltongue)**:
  - `sinks/elasticsearch_sink/`: 11 entities (struct `ElasticsearchSink`, `ElasticsearchSinkConfig`, `State`, methods: `new`, `open`, `consume`, `close`, `create_client`, `ensure_index_exists`, `bulk_index_documents`)
  - `sources/elasticsearch_source/`: 40 entities (struct `ElasticsearchSource`, `ElasticsearchSourceConfig`, state management via `StateManager`, `FileStateStorage`, `StateStorage` trait, auto-save, cleanup)
  - Note: Issue #1851 remains OPEN (full feature scope not yet complete)

#### Issue #1850 - Apache Iceberg Connectors (PR #2191)
- **Closed**: November 19, 2025
- **Scope**: +1,906 / -11 across 14 files
- **Description**: Iceberg sink connector with S3-compatible storage, REST catalogs, single-table and multi-table fan-out routing (static and dynamic).
- **Code Impact (Parseltongue)**:
  - `sinks/iceberg_sink/`: 47 entities (the most complex sink)
  - Key entities: `IcebergSink`, `DynamicRouter`, `DynamicWriter`, `StaticRouter`, `Router` trait
  - Enums: `IcebergSinkStoreClass`, `IcebergSinkTypes`
  - 12 functions including `init_catalog`, `get_props_s3`, `get_rest_catalog`, `write_data`, `table_exists`, `slice_user_table`
  - Router pattern: `Router` trait with `DynamicRouter` and `StaticRouter` implementations

---

### 2.3 Infrastructure & Configuration Phase (Nov-Dec 2025)

#### Issue #2318 - Split Connector Configs (PR #2317)
- **Closed**: November 10, 2025
- **Scope**: +409 / -149 across 16 files
- **Description**: Separated per-connector TOML configurations from the monolithic runtime config file. Each connector now has its own config file in organized directories.
- **Code Impact (Parseltongue)**:
  - `runtime/configs/`: 136 entities (the largest runtime module)
  - `ConnectorsConfigProvider` trait in `configs/connectors.rs`
  - `ProviderState` trait in `configs/connectors/local_provider.rs`
  - Local provider complexity: 105 total coupling (outbound)

#### Issue #2319 - TCP TLS Config for Connectors and MCP
- **Closed**: November 11, 2025
- **Description**: Added optional TLS configuration for TCP connections to the Iggy server, shared between Connectors Runtime and MCP server.
- **Code Impact**: TLS config struct additions to runtime configuration

#### Issue #2388 - HTTP-based Config Provider (PR ~Nov 2025)
- **Closed**: November 28, 2025
- **Description**: HTTP-based configuration provider allowing connectors to fetch configs from remote APIs, supporting RESTful, query-based, and wrapped response formats.
- **Code Impact (Parseltongue)**:
  - `HttpConnectorsConfigProvider` impl (2 entities in cluster #610)
  - Extends `ConnectorsConfigProvider` trait

#### Issue #2416 - Retry Mechanism for HTTP Config (PR #2437)
- **Closed**: December 3, 2025
- **Scope**: +84 / -5 across 6 files
- **Description**: Exponential backoff retry logic for HTTP config provider requests, handling transient network issues and rate limiting.
- **Code Impact**: Added to HTTP config provider implementation

#### Issue #2507 - TOML-Only Config Reading
- **Closed**: December 19, 2025
- **Description**: Local config provider now only reads `.toml` files from the config directory instead of attempting to parse all files.
- **Code Impact**: Filter change in `local_provider.rs`

---

### 2.4 Testing & Observability Phase (Jan-Feb 2026)

#### Issue #2594 - E2E Tests for Quickwit Sink (PR ~Jan 2026)
- **Closed**: January 30, 2026
- **Description**: End-to-end integration tests for the Quickwit sink connector following the Postgres pattern from PR #2579.
- **Code Impact (Parseltongue)**:
  - `sinks/quickwit_sink/`: 11 entities (struct `QuickwitSink`, `QuickwitSinkConfig`, `IndexConfig`, methods: `new`, `open`, `consume`, `close`, `create_index`, `has_index`, `ingest`)
  - Integration test harness: 18 entities in `core/integration/src/harness/handle/`, 3 in `harness/config`

#### PR #2633 - Prometheus Metrics and Stats Endpoints
- **Merged**: January 28, 2026
- **Scope**: +1,082 / -22 across 23 files
- **Description**: Added `/metrics` (Prometheus) and `/stats` (JSON) endpoints. Tracks runtime gauges (sources/sinks total/running), per-connector counters (messages produced/sent/consumed/processed/errors), CPU/memory usage, uptime.
- **Code Impact (Parseltongue)**:
  - `runtime/stats.rs`: 3 entities (2 structs, 1 function)
  - `runtime/api/`: 64 entities (expanded with metrics/stats handlers)
  - `runtime/metrics/`: 32 entities (cluster #59 - metrics module)

#### PR #2660 - Connector Version to Stats
- **Merged**: February 3, 2026
- **Scope**: +148 / -33 across 25 files
- **Description**: Added `version()` FFI export to SDK connector macros, exposing per-connector version info in stats response.

---

## 3. Supporting Infrastructure (Existing Connectors)

### 3.1 StdoutSink (Reference Implementation)
- **Entity Count**: 8 (simplest sink)
- **Entities**: `StdoutSink` struct, `StdoutSinkConfig`, `State`, methods: `new`, `open`, `consume`, `close`
- **Purpose**: Minimal reference implementation for learning the Sink pattern

### 3.2 RandomSource (Reference Implementation)
- **Entity Count**: 11 (simplest source)
- **Entities**: `RandomSource` struct, `RandomSourceConfig`, `Record`, `State`, methods: `new`, `open`, `poll`, `close`, `generate_messages`, `generate_random_text`
- **Purpose**: Minimal reference implementation for learning the Source pattern

---

## 4. Codebase Architecture Summary (Parseltongue)

### 4.1 Entity Distribution
| Component | Entities | Role |
|-----------|----------|------|
| `core/connectors/sdk/` | 151 | Trait definitions, encoders/decoders, transforms |
| `core/connectors/runtime/` | 293 | Plugin loading, lifecycle, config, API, metrics |
| `core/connectors/sinks/postgres_sink/` | 54 | PostgreSQL sink + tests |
| `core/connectors/sources/postgres_source/` | 56 | PostgreSQL source + tests |
| `core/connectors/sinks/iceberg_sink/` | 47 | Iceberg sink (most complex) |
| `core/connectors/sources/elasticsearch_source/` | 40 | ES source with state mgmt |
| `core/connectors/sinks/elasticsearch_sink/` | 11 | Elasticsearch sink |
| `core/connectors/sinks/quickwit_sink/` | 11 | Quickwit sink |
| `core/connectors/sources/random_source/` | 11 | Random source (reference) |
| `core/connectors/sinks/stdout_sink/` | 8 | Stdout sink (reference) |
| `foreign/java/.../iggy-connector-flink/` | 336 | Flink connector (Java) |
| `foreign/java/.../iggy-connector-pinot/` | 72 | Pinot connector (Java) |

### 4.2 Dependency Graph Health
- **Circular Dependencies**: 0 (clean architecture)
- **Complexity Hotspots** (connector-related):
  - `sources/postgres_source/src/lib.rs`: 147 total coupling (highest)
  - `runtime/src/source.rs`: 110 total coupling
  - `runtime/src/sink.rs`: 109 total coupling
  - `runtime/src/configs/.../local_provider.rs`: 105 total coupling

### 4.3 Core Traits (in `sdk/src/lib.rs`)
| Trait | Purpose | Implementations |
|-------|---------|----------------|
| `Sink` | Consume messages from Iggy to external system | ElasticsearchSink, IcebergSink, PostgresSink, QuickwitSink, StdoutSink |
| `Source` | Produce messages from external system to Iggy | ElasticsearchSource, PostgresSource, RandomSource |
| `StreamEncoder` | Encode messages for sinks | JSON, Raw, Text encoders |
| `StreamDecoder` | Decode messages from sources | JSON, Raw, Text decoders |
| `Transform` | Transform message fields | AddFields, DeleteFields, UpdateFields, FilterFields, FlatbufferConvert |

---

## 5. Open Issues Remaining

| # | Title | Labels | Priority Signal |
|---|-------|--------|----------------|
| **2700** | InfluxDB Connector (Sink, Source) | connectors | New connector |
| **2683** | simd_json serialization bug in ES sink | — | Bug fix |
| **2598** | E2E tests for Apache Pinot connector | good first issue | Testing |
| **2595** | E2E tests for Iceberg sink connector | good first issue | Testing |
| **2593** | E2E tests for ES source connector | good first issue | Testing |
| **2592** | E2E tests for ES sink connector | good first issue | Testing |
| **2540** | Redshift Sink Connector with S3 staging | — | New connector |
| **2539** | ClickHouse Sink Connector | — | New connector |
| **2500** | JDBC Source and Sink Connectors | connectors | New connector |
| **2484** | Flink connector - HTTP to TCP | improvement, java | Enhancement |
| **2417** | Runtime - restart with new config | good first issue | Runtime |
| **1852** | Delta Lake connectors | rust, connectors | New connector |
| **1851** | Elasticsearch connectors (full scope) | rust, connectors | Enhancement |
| **1847** | BSON payload support | rust, connectors | Codec |
| **1846** | Avro payload support | rust, connectors | Codec |

---

*Generated using Parseltongue v1.5.6 (15,637 entities, 76,133 edges) and GitHub CLI*
*Workspace: parseltongue20260208133459*
