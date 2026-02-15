# Apache Iggy Connectors: Complete Issue Tracker

**Last Updated**: February 14, 2026
**Source**: `gh issue list --repo apache/iggy`

---

## OPEN Issues (20)

### New Connectors

| # | Title | Labels | Created |
|---|-------|--------|---------|
| **2700** | InfluxDB Connector (Sink, Source) for Apache Iggy | connectors | Feb 7, 2026 |
| **2540** | Implement Redshift Sink Connector with S3 staging | — | — |
| **2539** | Implement ClickHouse Sink Connector | — | — |
| **2500** | JDBC Source and Sink Connectors for Iggy | connectors | Dec 18, 2025 |
| **1852** | Implement Delta Lake connectors | rust, connectors | Jun 7, 2025 |
| **1851** | Implement Elasticsearch connectors (full scope) | rust, connectors | Jun 7, 2025 |

### Codec / Payload Support

| # | Title | Labels | Created |
|---|-------|--------|---------|
| **1847** | Add support for BSON payload to connectors runtime | rust, connectors | Jun 7, 2025 |
| **1846** | Add support for Avro payload to connectors runtime | rust, connectors | Jun 7, 2025 |

### Bugs

| # | Title | Labels | Created |
|---|-------|--------|---------|
| **2712** | [Bug] Connector Runtime: IoError(Unsupported) on Linux Metadata and Recursive Plugin Loading Loop | bug | Feb 2026 |
| **2683** | fix(connectors): simd_json OwnedValue serialization bug in Elasticsearch sink | — | Feb 5, 2026 |

### Testing (E2E)

| # | Title | Labels | Created |
|---|-------|--------|---------|
| **2598** | Add e2e tests for Apache Pinot connector | good first issue, connectors, java | Jan 21, 2026 |
| **2595** | Add e2e tests for Iceberg sink connector | good first issue, test, connectors | Jan 20, 2026 |
| **2593** | Add e2e tests for Elasticsearch source connector | good first issue, test, connectors | Jan 20, 2026 |
| **2592** | Add e2e tests for Elasticsearch sink connector | good first issue, test, connectors | Jan 20, 2026 |

### Runtime Improvements

| # | Title | Labels | Created |
|---|-------|--------|---------|
| **2417** | Restart connector with new config without restarting runtime | good first issue, connectors | Nov 28, 2025 |

### Java / External Connectors

| # | Title | Labels | Created |
|---|-------|--------|---------|
| **2484** | Flink connector - transport - HTTP to TCP | enhancement, java | — |

### Integration / Protocol

| # | Title | Labels | Created |
|---|-------|--------|---------|
| **1762** | Integration with Google Agent2Agent Protocol | — | — |

---

## CLOSED Issues (12)

| # | Title | Closed | What Was Done |
|---|-------|--------|---------------|
| **2594** | Add e2e tests for Quickwit sink connector | Jan 30, 2026 | E2E tests using Docker |
| **2507** | Take only TOML files when reading connectors configs | Dec 19, 2025 | Filter in local_provider.rs |
| **2416** | Add Retry Mechanism to Connectors HTTP Config Provider | Dec 3, 2025 | Exponential backoff (PR #2437, +84/-5) |
| **2388** | HTTP-based Connectors Configuration Provider | Nov 28, 2025 | RESTful config fetching |
| **2319** | Add TCP TLS config to Connectors and MCP | Nov 11, 2025 | TLS config struct additions |
| **2318** | Split connectors configs from runtime config | Nov 10, 2025 | Per-connector TOML files (PR #2317, +409/-149) |
| **2276** | Implement Processor Infra/Libraries (Flink) | Dec 6, 2025 | Flink processor framework |
| **1850** | Implement Apache Iceberg connectors | Nov 19, 2025 | IcebergSink with S3, REST catalog, routing (PR #2191, +1906/-11) |
| **1849** | Implement PostgreSQL connectors | Oct 16, 2025 | PostgresSink + PostgresSource (PR #2579, +3726/-1474) |
| **1848** | Extend JSON field transformations | Jun 16, 2025 | update_fields, filter_fields transforms |
| **1845** | Protobuf payload support | Jun 29, 2025 | StreamEncoder + StreamDecoder for protobuf |
| **1844** | FlatBuffers payload support | Jul 2, 2025 | StreamEncoder + StreamDecoder for flatbuffers |

---

## Key Merged PRs (implementation references)

| # | Title | Merged | Scope |
|---|-------|--------|-------|
| **1826** | Add connectors runtime | Jun 1, 2025 | +3,960/-14, 39 files — foundational PR |
| **1872** | Elasticsearch sink and source connectors | Nov 18, 2025 | +2,079/-36, 17 files |
| **2191** | Iceberg sink connector | Nov 19, 2025 | +1,906/-11, 14 files |
| **2317** | Split connectors configs from runtime config | Nov 8, 2025 | +409/-149, 16 files |
| **2374** | Switch ES connector to rustls | Nov 19, 2025 | — |
| **2378** | Change connector state to binary representation | Nov 19, 2025 | — |
| **2437** | Add retry mechanism to HTTP config provider | Dec 3, 2025 | +84/-5, 6 files |
| **2472** | Add ARM64 builds and connector plugins to edge release | Dec 12, 2025 | CI/CD |
| **2499** | Add iggy-pinot external connector | Jan 21, 2026 | Java/Pinot |
| **2502** | Add --version flag to connector runtime | Dec 18, 2025 | — |
| **2579** | Extend Postgres sink & source, add integration tests | Jan 19, 2026 | +3,726/-1,474, 34 files |
| **2605** | Update iceberg to 0.8.0 | Jan 27, 2026 | Deps |
| **2632** | Add core test harness library | Jan 29, 2026 | Testing infra |
| **2633** | Add Prometheus metrics and stats endpoints | Jan 28, 2026 | +1,082/-22, 23 files |
| **2660** | Add connector version to stats endpoint | Feb 3, 2026 | +148/-33, 25 files |
| **2667** | Migrate connectors tests to iggy_harness proc macro | Feb 3, 2026 | Testing refactor |

---

## Contribution Opportunity Analysis

### Good First Issues (labeled)
- **#2592** — E2E tests for ES sink
- **#2593** — E2E tests for ES source
- **#2595** — E2E tests for Iceberg sink
- **#2598** — E2E tests for Pinot connector
- **#2417** — Restart connector without restarting runtime

### Medium Complexity
- **#2683** — Fix simd_json serialization bug (clear bug report with line numbers)
- **#2712** — Fix Linux metadata IoError (deployment blocker)
- **#1846** — Avro payload support (follow Protobuf/FlatBuffers pattern)
- **#1847** — BSON payload support (follow same pattern)
- **#2484** — Flink HTTP to TCP transport

### High Complexity (new connectors)
- **#2700** — InfluxDB Sink + Source
- **#2539** — ClickHouse Sink
- **#2540** — Redshift Sink with S3 staging
- **#2500** — JDBC Source + Sink
- **#1852** — Delta Lake connectors

---

*Pulled via `gh issue list --repo apache/iggy` on February 14, 2026*
