# Apache Iggy Connector Issues — Snapshot 2026-02-15 21:45 UTC

**Validated via**: `gh issue list --repo apache/iggy` with 12 separate search queries
**Search terms used**: `connector`, `sink`, `source`, `integration`, `plugin`, `ingest`, `database`, `runtime`, `MCP`, `transform`, `S3`, `clickhouse`, `redshift`, `delta lake`, `JDBC`, `elasticsearch`, `quickwit`, `iceberg`, `postgres`, `flink`, `kafka`, `redis`, `mongo`, `payload`, `codec`, `avro`, `bson`, `protobuf`, `flatbuffers`, `A2A`, `agent protocol`

---

## OPEN Issues — Connector-Related (16 total, newest first)

| # | Title | Opened | Labels | Category | Assigned? |
|---|-------|--------|--------|----------|-----------|
| **2712** | [Bug] Connector Runtime: IoError(Unsupported) on Linux Metadata and Recursive Plugin Loading Loop | 2026-02-10 | bug | Bug | — |
| **2700** | InfluxDB Connector (Sink, Source) for Apache Iggy | 2026-02-07 | connectors | New Connector | @ryerraguntla |
| **2598** | Add e2e tests for Apache Pinot connector | 2026-01-21 | good first issue, connectors, java | Testing | — |
| **2595** | Add e2e tests for Iceberg sink connector | 2026-01-20 | good first issue, test, connectors | Testing | — |
| **2593** | Add e2e tests for Elasticsearch source connector | 2026-01-20 | good first issue, test, connectors | Testing | — |
| **2592** | Add e2e tests for Elasticsearch sink connector | 2026-01-20 | good first issue, test, connectors | Testing | — |
| **2540** | Implement Redshift Sink Connector with S3 staging | 2026-01-05 | — | New Connector | — |
| **2539** | Implement ClickHouse Sink Connector | 2026-01-05 | — | New Connector | — |
| **2500** | JDBC Source and Sink Connectors for Iggy | 2025-12-18 | connectors | New Connector | — |
| **2484** | Flink connector - transport - HTTP to TCP | 2025-12-12 | enhancement, java | Enhancement | — |
| **2417** | Restart connector with new config without restarting runtime | 2025-11-28 | good first issue, connectors | Runtime | — |
| **1852** | Implement Delta Lake connectors | 2025-06-07 | rust, connectors | New Connector | — |
| **1851** | Implement Elasticsearch connectors (full scope) | 2025-06-07 | rust, connectors | New Connector | — |
| **1847** | Add support for BSON payload to connectors runtime | 2025-06-07 | rust, connectors | Codec | — |
| **1846** | Add support for Avro payload to connectors runtime | 2025-06-07 | rust, connectors | Codec | — |
| **1762** | Integration with Google Agent2Agent Protocol | 2025-05-10 | — | Integration | — |

---

## CLOSED Issues — Connector-Related (13 total, newest first)

| # | Title | Closed | Labels | What Was Done |
|---|-------|--------|--------|---------------|
| **2683** | fix(connectors): simd_json OwnedValue serialization bug in ES sink | 2026-02-15 | — | Bug fix in ES sink serialization |
| **2604** | Update iceberg-rs and migrate deprecated code | 2026-01-27 | — | Dependency update for Iceberg crate |
| **2594** | Add e2e tests for Quickwit sink connector | 2026-01-30 | good first issue, test, connectors | E2E tests using Docker |
| **2507** | Take only TOML files when reading connectors configs | 2025-12-19 | good first issue, enhancement, connectors | Filter in local_provider.rs |
| **2416** | Add Retry Mechanism to Connectors HTTP Config Provider | 2025-12-03 | good first issue, enhancement, connectors | Exponential backoff (PR #2437) |
| **2388** | HTTP-based Connectors Configuration Provider | 2025-11-28 | connectors | RESTful config fetching |
| **2319** | Add TCP TLS config to Connectors and MCP | 2025-11-11 | config, connectors, mcp | TLS config struct additions |
| **2318** | Split connectors configs from runtime config | 2025-11-10 | config, connectors | Per-connector TOML files (PR #2317) |
| **2276** | Implement Processor Infra/Libraries (Flink) | 2025-12-06 | java | Flink processor framework |
| **1850** | Implement Apache Iceberg connectors | 2025-11-19 | rust, connectors | IcebergSink (PR #2191) |
| **1849** | Implement PostgreSQL connectors | 2025-10-16 | rust, connectors | PostgresSink + PostgresSource (PR #2579) |
| **1848** | Extend JSON field transformations | 2025-06-16 | rust, connectors | update_fields, filter_fields |
| **1845** | Protobuf payload support | 2025-06-29 | rust, connectors | StreamEncoder + StreamDecoder |
| **1844** | FlatBuffers payload support | 2025-07-02 | rust, connectors | StreamEncoder + StreamDecoder |

---

## Summary by Category

### New Connectors (OPEN: 6)

| # | System | Type | Pattern | Complexity |
|---|--------|------|---------|------------|
| **2700** | InfluxDB | Sink + Source | HTTP/Search (like Quickwit) | Medium |
| **2539** | ClickHouse | Sink | HTTP/Search (like Quickwit) | Medium |
| **2540** | Redshift | Sink | S3-staging (like Iceberg) | High |
| **2500** | JDBC | Sink + Source | Database (like Postgres) | High |
| **1852** | Delta Lake | Sink + Source | Data Lake (like Iceberg) | High |
| **1851** | Elasticsearch | Full scope | HTTP/Search (extend existing) | Medium |

### New Connectors (CLOSED: 3)

| # | System | Delivered |
|---|--------|-----------|
| **1850** | Apache Iceberg | Sink (Nov 2025) |
| **1849** | PostgreSQL | Sink + Source (Oct 2025) |
| **2276** | Flink Processor | Java infra (Dec 2025) |

### Codec/Payload (OPEN: 2, CLOSED: 2)

| # | Format | Status |
|---|--------|--------|
| **1846** | Avro | OPEN |
| **1847** | BSON | OPEN |
| **1845** | Protobuf | CLOSED (Jun 2025) |
| **1844** | FlatBuffers | CLOSED (Jul 2025) |

### Testing E2E (OPEN: 4, CLOSED: 1)

| # | Target | Status |
|---|--------|--------|
| **2598** | Pinot | OPEN |
| **2595** | Iceberg sink | OPEN |
| **2593** | ES source | OPEN |
| **2592** | ES sink | OPEN |
| **2594** | Quickwit sink | CLOSED (Jan 2026) |

### Runtime/Infra (OPEN: 2, CLOSED: 5)

| # | Topic | Status |
|---|-------|--------|
| **2712** | Linux IoError bug | OPEN (bug) |
| **2417** | Hot config reload | OPEN |
| **2683** | simd_json serialization bug | CLOSED (Feb 15, 2026 — today!) |
| **2604** | Iceberg dependency update | CLOSED |
| **2507** | TOML-only config reading | CLOSED |
| **2416** | HTTP config retry | CLOSED |
| **2388** | HTTP config provider | CLOSED |

### Other (OPEN: 2, CLOSED: 1)

| # | Topic | Status |
|---|-------|--------|
| **2484** | Flink HTTP→TCP transport | OPEN |
| **1762** | Google A2A Protocol | OPEN |
| **2318** | Config splitting | CLOSED |
| **2319** | TLS config | CLOSED |

---

## Delta from Previous Tracker (connector-issues-complete-tracker.md, Feb 14)

| Change | Detail |
|--------|--------|
| **#2683 now CLOSED** | Was listed as open. Closed today (Feb 15, 2026) |
| **#2604 added** | Closed Iceberg dependency update — was missing entirely |
| **Dates validated** | All 30 issues verified with exact ISO timestamps via gh CLI |
| **Search coverage** | 12 search queries vs. 2 in previous tracker |
| **No new open issues found** | Broader search did not uncover additional connector issues |

---

## Contribution Priority (unassigned, newest first)

### Immediate (unassigned, recent, clear scope)
1. **#2712** — Linux IoError bug (deployment blocker, Feb 10)
2. **#2592** — ES sink e2e tests (good first issue, Jan 20)
3. **#2593** — ES source e2e tests (good first issue, Jan 20)
4. **#2595** — Iceberg e2e tests (good first issue, Jan 20)
5. **#2598** — Pinot e2e tests (good first issue, Jan 21)

### Medium-term (unassigned, clear pattern to follow)
6. **#2539** — ClickHouse Sink (HTTP pattern, like Quickwit)
7. **#1846** — Avro payload (follow Protobuf/FlatBuffers pattern)
8. **#1847** — BSON payload (follow same pattern)
9. **#2417** — Hot config reload (runtime change)
10. **#2484** — Flink HTTP→TCP (Java, enhancement)

### Long-term (unassigned, high complexity)
11. **#2540** — Redshift Sink (S3 staging, like Iceberg)
12. **#2500** — JDBC Sink + Source (like Postgres but generic)
13. **#1852** — Delta Lake (like Iceberg, data lake pattern)
14. **#1851** — Elasticsearch full scope (extend existing)

### Already assigned
- **#2700** — InfluxDB (assigned to @ryerraguntla)

### Unclear/Stale
- **#1762** — Google A2A Protocol (May 2025, no activity, unclear connector relevance)

---

*Generated: 2026-02-15T21:45:00Z*
*Queries: 12 gh CLI searches across sink/source/connector/integration/plugin/ingest/database/runtime/MCP/transform/S3 + specific system names*
*Validated: 30 issues total (16 open, 14 closed)*
