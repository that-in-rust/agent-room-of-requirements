# Apache Iggy Connectors: Remaining Work
> Tracking proposed connectors and infrastructure work with no active PRs

---

## Master Tracking Resources

| Resource | Link | Purpose |
|----------|------|---------|
| **Roadmap Issue** | [#2753](https://github.com/apache/iggy/issues/2753) | Full 120+ connector target list |
| **Ecosystem Discussion** | [#2756](https://github.com/apache/iggy/discussions/2756) | Community prioritization discussion |
| **Original Plugin Proposal** | [#1670](https://github.com/apache/iggy/discussions/1670) | Architecture discussion |

---

## Status Summary

| Category | Done | In Progress (PR Open) | Proposed (No PR) |
|----------|:----:|:---------------------:|:----------------:|
| Native Rust Connectors | 5 | 4 | 101+ |
| Java Connectors | 2 | 0 | ~6 |
| Codecs | 5 | 2 (Avro, BSON) | 3 |

---

## In Progress (Has Active PR)

| Connector | Type | PR | Issue | Status |
|-----------|------|----|----|--------|
| ClickHouse | Sink | [#2886](https://github.com/apache/iggy/pull/2886) | [#2539](https://github.com/apache/iggy/issues/2539) | Review required |
| MongoDB | Sink | [#2815](https://github.com/apache/iggy/pull/2815) | [#2739](https://github.com/apache/iggy/issues/2739) | Review required |
| InfluxDB | Sink+Source | [#2801](https://github.com/apache/iggy/pull/2801) | [#2700](https://github.com/apache/iggy/issues/2700) | Changes requested |
| Delta Lake | Sink | [#2783](https://github.com/apache/iggy/pull/2783) | [#1852](https://github.com/apache/iggy/issues/1852) | Changes requested |
| Connector Restart | Infra | [#2781](https://github.com/apache/iggy/pull/2781) | [#2417](https://github.com/apache/iggy/issues/2417) | Changes requested |

---

## High Priority (P0/P1) - No Active PR

### Data Warehouses

| Target | Type | Issue | Why Critical | Rust Crate |
|--------|------|-------|--------------|------------|
| **Snowflake** | Sink | None | #1 cloud data warehouse. $70B+ revenue. | `reqwest` (REST API) |
| **BigQuery** | Sink | None | Google's serverless warehouse. Petabyte scale. | `gcp-bigquery-client` |
| **Redshift** | Sink+Source | [#2540](https://github.com/apache/iggy/issues/2540) | AWS's data warehouse. | `aws-sdk-redshift` |

### Relational Databases

| Target | Type | Issue | Why Critical | Rust Crate |
|--------|------|-------|--------------|------------|
| **MySQL/MariaDB** | Sink+Source | None | Most popular RDBMS globally. | `sqlx` or `mysql_async` |
| **Oracle** | Sink+Source | None | Enterprise standard. Fortune 500. | `oracle` crate |
| **SQL Server** | Sink+Source | None | Microsoft's RDBMS. Enterprise heavy. | `tiberius` |

### NoSQL Databases

| Target | Type | Issue | Why Critical | Rust Crate |
|--------|------|-------|--------------|------------|
| **Redis** | Sink+Source | None | Most popular cache. In-memory speed. | `redis` crate |
| **Cassandra/ScyllaDB** | Sink+Source | None | Linear scalability. Netflix/Apple use. | `scylla` crate |
| **DynamoDB** | Sink | None | AWS native. Serverless workloads. | `aws-sdk-dynamodb` |

### Cloud Object Storage

| Target | Type | Issue | Why Critical | Rust Crate |
|--------|------|-------|--------------|------------|
| **AWS S3** | Sink+Source | None | Object storage standard. Data lake foundation. | `aws-sdk-s3` |
| **Google Cloud Storage** | Sink | None | GCP native storage. | `google-cloud-storage` |
| **Azure Blob Storage** | Sink | None | Azure native storage. | `azure_storage_blobs` |

### Stream Processing

| Target | Type | Issue | Why Critical | Rust Crate |
|--------|------|-------|--------------|------------|
| **Apache Flink** | Source+Sink | [#2484](https://github.com/apache/iggy/issues/2484) (transport only) | Leading stream processor. | Java connector JAR |
| **Apache Spark** | Source | None | Most popular data processing framework. | Java/Scala connector |

---

## Medium Priority (P2) - No Active PR

### Time-Series Databases

| Target | Type | Issue | Why It Matters | Rust Crate |
|--------|------|-------|----------------|------------|
| **TimescaleDB** | Sink+Source | None | PostgreSQL-based time-series. | `sqlx` |
| **Prometheus** | Sink | None | De facto monitoring standard. | `prometheus` crate |
| **VictoriaMetrics** | Sink | None | Prometheus-compatible. High perf. | `reqwest` |

### Message Queues

| Target | Type | Issue | Why It Matters | Rust Crate |
|--------|------|-------|----------------|------------|
| **Apache Kafka** | Source+Sink | None | Industry standard. Migration path. | `rdkafka` |
| **RabbitMQ** | Source+Sink | None | Popular message broker. | `lapin` |
| **NATS JetStream** | Source+Sink | None | Cloud-native messaging. | `nats` |

### Graph Databases

| Target | Type | Issue | Why It Matters | Rust Crate |
|--------|------|-------|----------------|------------|
| **Neo4j** | Sink | None | Most popular graph DB. | `neo4rs` |
| **Amazon Neptune** | Sink | None | AWS managed graph DB. | `aws-sdk-neptune` |

---

## Lower Priority (P3/P4) - Not Started

### AI/ML & Vector DBs
- **Pinecone** (P3) - Vector DB for AI apps
- **Weaviate** (P3) - Vector search engine  
- **Milvus** (P3) - Open-source vector DB
- **Chroma** (P4) - AI-native embedding DB
- **Qdrant** (P4) - Vector similarity search

### Observability
- **OpenTelemetry** (P2) - Observability standard
- **Grafana/Loki** (P3) - Log aggregation
- **Jaeger** (P3) - Distributed tracing
- **Datadog** (P3) - Cloud monitoring

### IoT Protocols
- **MQTT** (P2) - IoT standard protocol
- **CoAP** (P3) - Constrained application protocol
- **OPC-UA** (P3) - Industrial automation

### SaaS & Enterprise
- **Salesforce** (P4) - CRM events
- **Stripe** (P4) - Payment events
- **Slack** (P4) - Alert notifications
- **Twilio** (P4) - SMS alerts

---

## Codecs/Formats Remaining

| Format | Priority | Issue | Rust Crate |
|--------|----------|-------|------------|
| **Avro** | High | [#1846](https://github.com/apache/iggy/issues/1846) | `apache-avro` (in progress) |
| **BSON** | Medium | [#1847](https://github.com/apache/iggy/issues/1847) | `bson` (in progress) |
| **Parquet** | High | None | `parquet` crate |
| **CSV** | Low | None | `csv` crate |
| **MessagePack** | Low | None | `rmp-serde` crate |

---

## Infrastructure Issues (No PR)

| Issue | Description | Priority |
|-------|-------------|----------|
| [#2500](https://github.com/apache/iggy/issues/2500) | JDBC Source and Sink Connectors | High |
| [#2598](https://github.com/apache/iggy/issues/2598) | E2E tests for Pinot connector | Medium |

---

## How to Claim a Connector

1. Comment on [Roadmap Issue #2753](https://github.com/apache/iggy/issues/2753)
2. Reference existing connectors as templates:
   - PostgreSQL: `core/connectors/sinks/postgres_sink/`
   - Elasticsearch: `core/connectors/sinks/elasticsearch_sink/`
3. Review connector SDK traits (`Sink`, `Source`, `Transform`) in SDK crate
4. Each connector is a separate Rust cdylib crate under `core/connectors/`

---

## Quick Links

| Category | Link |
|----------|------|
| All Open Connector Issues | [GitHub Search](https://github.com/apache/iggy/issues?q=is%3Aissue+is%3Aopen+connector) |
| All Open Connector PRs | [GitHub Search](https://github.com/apache/iggy/pulls?q=is%3Apr+is%3Aopen+connector) |
| Connector SDK | `sdk/src/connectors/` in repo |
| Example Connectors | `core/connectors/sinks/` in repo |

---

*Last updated: 2026-03-07*
*Based on Roadmap Issue #2753 and Discussion #2756*
