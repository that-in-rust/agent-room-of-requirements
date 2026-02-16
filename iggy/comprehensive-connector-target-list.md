# Comprehensive Connector Target List for Apache Iggy

**Date**: 2026-02-16
**Methodology**: Cross-referencing Kafka Connect (200+ connectors), Pulsar IO (40+ built-in), Redpanda Connect (200+ via Benthos), NATS (10+ Synadia), Apache Camel (193 Kamelets), Flink, and the broader streaming ecosystem against Iggy's current and planned connectors. Enriched with KP's (Iggy maintainer) stated priorities from Discord.

---

## 1. What Iggy Already Has

```
NATIVE RUST CONNECTORS (cdylib plugin model):
+---------------------+------+--------+-----+
| Connector           | Sink | Source | LOC |
+---------------------+------+--------+-----+
| PostgreSQL          |  x   |   x    | 2398|
| Elasticsearch       |  x   |   x    | 1523|
| Quickwit            |  x   |        |  260|
| Stdout (reference)  |  x   |        |  155|
| Apache Iceberg      |  x   |        |  ???|
+---------------------+------+--------+-----+

JAVA EXTERNAL CONNECTORS:
+-----------------------+------+--------+
| Connector             | Sink | Source |
+-----------------------+------+--------+
| Apache Pinot          |  x   |        |
| (via Kafka compat)    |      |        |
+-----------------------+------+--------+

CODECS:
  [x] JSON  [x] Protobuf  [x] FlatBuffers  [x] Raw/Bytes  [x] Text
```

Total: **5 native sinks, 2 native sources, 2 Java connectors**

---

## 2. What's Already Planned (Open Issues)

| Issue   | Target               | Type        | Status   |
|---------|----------------------|-------------|----------|
| #2739   | MongoDB              | Sink+Source | Open     |
| #2700   | InfluxDB             | Sink+Source | Open     |
| #2539   | ClickHouse           | Sink        | Open     |
| #2540   | Redshift             | Sink        | Open     |
| #2500   | Generic JDBC / MySQL | Sink+Source | Open     |
| #1852   | Delta Lake           | Sink+Source | Open     |
| #1846   | Avro Codec           | Codec       | Open     |
| #1847   | BSON Codec           | Codec       | Open     |

---

## 3. KP's Stated Priorities (Discord)

KP explicitly mentioned interest in connectors for:

```
EXPLICITLY NAMED BY KP:
  - Apache Flink         (stream processing integration)
  - Apache Iceberg       (already implemented)
  - MongoDB              (already tracked as #2739)
  - Redis                (NOT YET TRACKED)
  - Object Storage       (S3 / GCS / Azure Blob -- NOT YET TRACKED)
  - Snowflake            (NOT YET TRACKED)
  - OpenSearch           (NOT YET TRACKED)
  - OTLP Logs            (OpenTelemetry -- NOT YET TRACKED)
  - HTTP                 (NOT YET TRACKED)
  - gRPC                 (NOT YET TRACKED)
  - MQTT                 (NOT YET TRACKED)
  - Apache Camel         (integration framework)

THEMATIC FOCUS:
  - "Modern data stacks"
  - IoT and edge computing
  - Observability pipelines
```

---

## 4. Master Connector Target List

Legend:
- **KP** = Explicitly mentioned by KP in Discord
- **Comp** = How many of {Kafka, Pulsar, Redpanda, NATS} have this connector (0-4)
- **Iggy** = Current Iggy status: HAVE / PLANNED / MISSING
- **Priority** = Recommended priority: P0 (critical) / P1 (high) / P2 (medium) / P3 (low) / P4 (niche)

### 4.1 Relational Databases (RDBMS)

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| PostgreSQL          | Sink+Source |    | 4/4  | HAVE    | --       | Native Rust, CDC via WAL |
| MySQL / MariaDB     | Sink+Source |    | 4/4  | PLANNED | P1       | #2500 JDBC. Most popular RDBMS globally |
| Microsoft SQL Server| Sink+Source |    | 3/4  | MISSING | P2       | Enterprise RDBMS. Debezium CDC in Kafka |
| Oracle              | Sink+Source |    | 3/4  | MISSING | P3       | Complex licensing (GoldenGate CDC) |
| SQLite              | Sink        |    | 2/4  | MISSING | P4       | Niche, embedded use cases |
| CockroachDB         | Sink+Source |    | 2/4  | ~HAVE~  | --       | Works via Postgres wire protocol |
| IBM Db2             | Sink+Source |    | 1/4  | MISSING | P4       | Enterprise/mainframe only |
| Generic JDBC        | Sink+Source |    | 3/4  | PLANNED | P1       | #2500. Covers MySQL, MariaDB, others |

### 4.2 NoSQL / Document Databases

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| MongoDB             | Sink+Source | KP | 4/4  | PLANNED | P0       | #2739. Most popular NoSQL. Change Streams CDC |
| Cassandra           | Sink        |    | 3/4  | MISSING | P2       | Wide-column store. DataStax connector in Kafka |
| DynamoDB            | Sink+Source |    | 3/4  | MISSING | P2       | AWS-native NoSQL. Streams API for source |
| Couchbase           | Sink+Source |    | 2/4  | MISSING | P3       | Less common than Mongo |
| HBase               | Sink        |    | 2/4  | MISSING | P3       | Hadoop ecosystem, declining |
| Azure Cosmos DB     | Sink+Source |    | 1/4  | MISSING | P3       | Azure-native, multi-model |
| ScyllaDB            | Sink        |    | 1/4  | MISSING | P3       | Cassandra-compatible, Rust-friendly |
| Apache CouchDB      | Sink+Source |    | 1/4  | MISSING | P4       | Niche |

### 4.3 Search & Analytics Engines

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Elasticsearch       | Sink+Source |    | 4/4  | HAVE    | --       | Native Rust |
| OpenSearch          | Sink        | KP | 2/4  | MISSING | P1       | ES fork, AWS-aligned. May work via ES connector with compat layer |
| Quickwit            | Sink        |    | 0/4  | HAVE    | --       | Native Rust. Unique to Iggy |
| Apache Solr         | Sink        |    | 2/4  | MISSING | P3       | Declining, replaced by ES/OpenSearch |
| Splunk              | Sink        |    | 3/4  | MISSING | P2       | Enterprise observability. HEC API |
| Apache Pinot        | Sink        |    | 2/4  | HAVE    | --       | Java connector (via Kafka compat) |
| Meilisearch         | Sink        |    | 0/4  | MISSING | P4       | Lightweight search, growing |
| Typesense           | Sink        |    | 0/4  | MISSING | P4       | Alternative to Meilisearch |

### 4.4 Cloud Object Storage

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Amazon S3           | Sink+Source | KP | 4/4  | MISSING | P0       | Universal data lake landing zone |
| Google Cloud Storage| Sink+Source | KP | 3/4  | MISSING | P1       | GCP object storage |
| Azure Blob Storage  | Sink+Source | KP | 3/4  | MISSING | P1       | Azure object storage |
| MinIO               | Sink+Source |    | 1/4  | MISSING | P1       | S3-compatible, self-hosted. Works via S3 connector |
| DigitalOcean Spaces | Sink        |    | 0/4  | MISSING | P4       | S3-compatible |
| Backblaze B2        | Sink        |    | 0/4  | MISSING | P4       | S3-compatible |

**Architecture note**: Build S3 connector first with abstract storage interface. GCS, Azure Blob, MinIO become thin adapters over the same partitioning/batching/format logic.

### 4.5 Data Lakehouse Formats

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Apache Iceberg      | Sink        | KP | 2/4  | HAVE    | --       | Native Rust |
| Delta Lake          | Sink+Source |    | 2/4  | PLANNED | P2       | #1852. Databricks ecosystem |
| Apache Hudi         | Sink        |    | 1/4  | MISSING | P3       | Uber's lakehouse format |
| Apache Paimon       | Sink        |    | 0/4  | MISSING | P4       | Flink-native, emerging |

### 4.6 Data Warehouses

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Snowflake           | Sink        | KP | 3/4  | MISSING | P1       | Leading cloud DW. Snowpipe Streaming API |
| ClickHouse          | Sink        |    | 2/4  | PLANNED | P1       | #2539. Real-time OLAP, popular in Rust community |
| Amazon Redshift     | Sink        |    | 2/4  | PLANNED | P2       | #2540. AWS cloud DW |
| Google BigQuery     | Sink        |    | 3/4  | MISSING | P2       | GCP analytics DW. Storage Write API |
| Databricks          | Sink        |    | 2/4  | MISSING | P2       | Via Delta Lake connector or SQL |
| Azure Synapse       | Sink        |    | 1/4  | MISSING | P3       | Microsoft cloud DW |
| StarRocks           | Sink        |    | 1/4  | MISSING | P3       | Real-time OLAP, growing |
| Apache Doris        | Sink        |    | 1/4  | MISSING | P3       | StarRocks parent project |
| Firebolt            | Sink        |    | 0/4  | MISSING | P4       | Niche cloud DW |
| DuckDB              | Sink        |    | 0/4  | MISSING | P3       | Embedded OLAP, huge Rust/data community |

### 4.7 Time-Series Databases

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| InfluxDB            | Sink+Source |    | 2/4  | PLANNED | P0       | #2700. IoT standard TSDB |
| TimescaleDB         | Sink+Source |    | 2/4  | ~HAVE~  | --       | PG extension, works via Postgres connector |
| Prometheus          | Sink (remote_write) |    | 1/4 | MISSING | P2  | Monitoring standard. remote_write API |
| QuestDB             | Sink        |    | 1/4  | MISSING | P3       | InfluxDB Line Protocol compatible |
| TDengine            | Sink        |    | 0/4  | MISSING | P3       | IoT-focused TSDB, popular in Asia |
| VictoriaMetrics     | Sink        |    | 0/4  | MISSING | P3       | Prometheus-compatible, growing |
| CrateDB             | Sink        |    | 0/4  | MISSING | P4       | SQL TSDB |

### 4.8 Graph Databases

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Neo4j               | Sink        |    | 3/4  | MISSING | P3       | Leading graph DB |
| ArangoDB            | Sink        |    | 0/4  | MISSING | P4       | Multi-model (graph+doc+KV) |
| Amazon Neptune      | Sink        |    | 0/4  | MISSING | P4       | AWS graph DB |
| JanusGraph          | Sink        |    | 0/4  | MISSING | P4       | Open-source, Hadoop-backed |

### 4.9 Message Queues & Streaming Bridges

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| MQTT                | Source+Sink | KP | 3/4  | MISSING | P0       | THE IoT protocol. rumqttc Rust crate |
| RabbitMQ / AMQP     | Source+Sink |    | 3/4  | MISSING | P1       | Most popular traditional MQ. `lapin` crate |
| Apache Kafka        | Source+Sink |    | n/a  | MISSING | P2       | Bridge for Kafka migration. `rdkafka` crate |
| Amazon Kinesis      | Source+Sink |    | 3/4  | MISSING | P2       | AWS streaming. Cross-cloud bridge |
| Amazon SQS          | Source+Sink |    | 2/4  | MISSING | P3       | AWS queue service |
| Google Pub/Sub      | Source+Sink |    | 2/4  | MISSING | P2       | GCP streaming |
| Apache Pulsar       | Source+Sink |    | 1/4  | MISSING | P3       | Alt streaming platform bridge |
| NATS / JetStream    | Source+Sink |    | 1/4  | MISSING | P3       | Lightweight messaging bridge |
| NSQ                 | Source+Sink |    | 2/4  | MISSING | P4       | Simple queue |
| IBM MQ              | Source+Sink |    | 1/4  | MISSING | P4       | Enterprise/mainframe |
| Azure Service Bus   | Source+Sink |    | 1/4  | MISSING | P3       | Azure messaging |
| Azure Event Hubs    | Source      |    | 1/4  | MISSING | P3       | Azure Kafka-compatible |

### 4.10 Caches & Key-Value Stores

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Redis               | Sink+Source | KP | 3/4  | MISSING | P0       | Cache warming, real-time state. `redis` crate |
| DragonflyDB         | Sink+Source |    | 0/4  | MISSING | P3       | Redis-compatible, works via Redis connector |
| Memcached           | Sink        |    | 1/4  | MISSING | P4       | Legacy cache |
| Aerospike           | Sink        |    | 2/4  | MISSING | P4       | High-performance KV |
| Hazelcast           | Source      |    | 2/4  | MISSING | P4       | In-memory data grid |
| etcd                | Sink+Source |    | 0/4  | MISSING | P4       | K8s config store |

### 4.11 File Systems & Formats

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Local Filesystem    | Sink+Source |    | 2/4  | MISSING | P3       | File tail source, file write sink |
| FTP / SFTP          | Sink+Source |    | 3/4  | MISSING | P3       | Legacy file transfer |
| HDFS                | Sink        |    | 3/4  | MISSING | P3       | Declining but still in Hadoop shops |
| **Parquet** (format)| Output fmt  |    | 3/4  | MISSING | P1       | Essential for S3/GCS/HDFS sinks |
| **Avro** (codec)    | Codec       |    | 4/4  | PLANNED | P0       | #1846. Kafka ecosystem standard |
| **BSON** (codec)    | Codec       |    | 0/4  | PLANNED | P2       | #1847. MongoDB native format |
| ORC (format)        | Output fmt  |    | 1/4  | MISSING | P4       | Hadoop-specific |
| CSV (format)        | Input/Output|    | 2/4  | MISSING | P3       | Human-readable, batch imports |
| MessagePack (codec) | Codec       |    | 1/4  | MISSING | P4       | Compact binary, niche |

### 4.12 HTTP & API Protocols

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| HTTP / Webhook      | Source+Sink | KP | 4/4  | MISSING | P0       | Universal integration. `reqwest`/`axum` |
| gRPC                | Source+Sink | KP | 1/4  | MISSING | P1       | High-perf RPC. `tonic` crate |
| GraphQL             | Sink        |    | 0/4  | MISSING | P4       | Niche subscription source |
| WebSocket           | Source+Sink |    | 1/4  | MISSING | P3       | Real-time bidirectional |

### 4.13 Observability & Monitoring

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| OpenTelemetry (OTLP)| Source+Sink | KP | 1/4  | MISSING | P0       | Emerging standard. gRPC + HTTP/proto |
| Splunk (HEC)        | Sink        |    | 3/4  | MISSING | P2       | Enterprise. HTTP Event Collector API |
| Datadog             | Sink        |    | 2/4  | MISSING | P3       | SaaS observability |
| Prometheus remote_write | Sink    |    | 1/4  | MISSING | P2       | Push metrics to Prometheus |
| Grafana Loki        | Sink        |    | 1/4  | MISSING | P2       | Log aggregation. HTTP push API |
| Jaeger              | Sink        |    | 0/4  | MISSING | P3       | Tracing backend (OTLP preferred) |
| New Relic           | Sink        |    | 1/4  | MISSING | P4       | SaaS observability |

### 4.14 AI/ML & Vector Databases

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Qdrant              | Sink        |    | 0/4  | MISSING | P3       | Rust-native vector DB |
| Weaviate            | Sink        |    | 0/4  | MISSING | P3       | Popular vector DB |
| Pinecone            | Sink        |    | 0/4  | MISSING | P3       | SaaS vector DB |
| Milvus              | Sink        |    | 0/4  | MISSING | P3       | Open-source vector DB |
| MLflow              | Sink        |    | 0/4  | MISSING | P4       | ML experiment tracking |
| Feature Store (Feast)| Source     |    | 0/4  | MISSING | P4       | ML feature serving |

### 4.15 SaaS & Enterprise

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Salesforce          | Source+Sink |    | 1/4  | MISSING | P4       | CRM. Kafka has 8 connectors |
| ServiceNow          | Source+Sink |    | 1/4  | MISSING | P4       | ITSM |
| Slack               | Sink        |    | 0/4  | MISSING | P4       | Alerts/notifications |
| Email (SMTP)        | Sink        |    | 1/4  | MISSING | P4       | Alert notifications |
| Stripe              | Source      |    | 0/4  | MISSING | P4       | Payment events |
| Twilio              | Sink        |    | 0/4  | MISSING | P4       | SMS/notifications |

### 4.16 Stream Processing Integration

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Apache Flink        | Source+Sink | KP | 2/4  | MISSING | P1       | Leading stream processor. Needs Flink connector JAR |
| Apache Spark Streaming | Source   |    | 2/4  | MISSING | P3       | Batch+streaming. Spark connector |
| Apache Beam         | Source+Sink |    | 1/4  | MISSING | P3       | Unified batch+stream model |
| Materialize         | Source      |    | 0/4  | MISSING | P4       | Streaming SQL database |
| RisingWave          | Source      |    | 0/4  | MISSING | P4       | Streaming database, Rust-based |
| Apache Camel        | Framework   | KP | n/a  | MISSING | P2       | Integration framework, 193+ connectors |

### 4.17 Workflow & Orchestration

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| Apache Airflow      | Trigger     |    | 1/4  | MISSING | P4       | Workflow orchestration |
| Temporal            | Source+Sink |    | 0/4  | MISSING | P4       | Durable workflows |
| Prefect             | Trigger     |    | 0/4  | MISSING | P4       | Modern Airflow alternative |
| Dagster             | Source      |    | 0/4  | MISSING | P4       | Data orchestration |

### 4.18 IoT Protocols (Beyond MQTT)

| Target              | Direction   | KP | Comp | Iggy    | Priority | Notes |
|---------------------|-------------|:--:|:----:|---------|:--------:|-------|
| MQTT                | Source+Sink | KP | 3/4  | MISSING | P0       | See 4.9 |
| CoAP                | Source+Sink |    | 0/4  | MISSING | P3       | Constrained Application Protocol |
| OPC-UA              | Source      |    | 1/4  | MISSING | P2       | Industrial IoT standard |
| Modbus              | Source      |    | 1/4  | MISSING | P3       | Industrial protocol |
| LwM2M               | Source      |    | 0/4  | MISSING | P4       | IoT device management |

---

## 5. Competitive Coverage Matrix (Summary)

```
                        Kafka  Pulsar  Redpanda  NATS  Iggy
Total Connectors:       200+    40+     200+     10+   7+2
RDBMS:                    8       5       6       1     1 (PG) + JDBC planned
NoSQL:                    7       5       3       1     0 + MongoDB planned
Search:                   5       3       3       0     3 (ES, Quickwit, Pinot)
Cloud Storage:            4       2       4       1     0
Lakehouse:                3       2       0       0     1 (Iceberg) + Delta planned
Data Warehouse:           6       3       3       0     0 + ClickHouse/Redshift planned
Time-Series:              3       1       1       0     0 + InfluxDB planned
Message Queues:           8       4       8       0     0
Caches/KV:                3       2       4       0     0
HTTP/API:                 2       1       2       1     0
Observability:            4       2       2       0     0
```

---

## 6. Prioritized Roadmap

### Phase 1: Foundation (IoT + Universal Integration)

These establish Iggy as a credible IoT/edge streaming platform and enable basic integration with any system.

| # | Connector/Codec      | Type        | KP | Comp | Est. LOC | Rationale |
|---|----------------------|-------------|:--:|:----:|:--------:|-----------|
| 1 | **MQTT**             | Source+Sink | KP | 3/4  | 600-800  | THE IoT protocol. Iggy's core market |
| 2 | **HTTP / Webhook**   | Source+Sink | KP | 4/4  | 500-700  | Connect Iggy to anything. Universal fallback |
| 3 | **gRPC**             | Source+Sink | KP | 1/4  | 700-900  | High-perf API. tonic crate. Pairs with OTLP |
| 4 | **InfluxDB**         | Sink+Source |    | 2/4  | 800-1000 | #2700. IoT TSDB standard |
| 5 | **Avro Codec**       | Codec       |    | 4/4  | 300-400  | #1846. Interop with Kafka ecosystem |
| 6 | **OpenTelemetry**    | Source+Sink | KP | 1/4  | 800-1000 | OTLP logs/traces/metrics. Observability pipe |

**After Phase 1**: Iggy can ingest from IoT devices (MQTT), web APIs (HTTP), microservices (gRPC), and telemetry (OTLP), and store time-series data (InfluxDB). Avro enables Kafka interop.

### Phase 2: Data Platform Essentials

These make Iggy a viable data platform for production workloads.

| # | Connector/Codec      | Type        | KP | Comp | Est. LOC | Rationale |
|---|----------------------|-------------|:--:|:----:|:--------:|-----------|
| 7 | **MongoDB**          | Sink+Source | KP | 4/4  | 1200-1300| #2739. Most popular NoSQL |
| 8 | **Amazon S3**        | Sink+Source | KP | 4/4  | 800-1000 | Data lake landing zone. Enables Snowflake |
| 9 | **Redis**            | Sink+Source | KP | 3/4  | 600-800  | Cache warming, real-time state |
| 10| **Generic JDBC/MySQL** | Sink+Source |  | 4/4  | 900-1100 | #2500. Broadest RDBMS coverage |
| 11| **ClickHouse**       | Sink        |    | 2/4  | 600-800  | #2539. Real-time OLAP |
| 12| **OpenSearch**       | Sink        | KP | 2/4  | 200-400  | ES fork. May be thin adapter over ES connector |
| 13| **Parquet Format**   | Output fmt  |    | 3/4  | 400-600  | Essential for S3/GCS sinks |

**After Phase 2**: Iggy can land data in MongoDB, S3, Redis, MySQL, ClickHouse, and write Parquet files. Covers 80% of production use cases.

### Phase 3: Cloud & Analytics

These complete the cloud DW story and add multi-cloud storage.

| # | Connector/Codec      | Type        | KP | Comp | Est. LOC | Rationale |
|---|----------------------|-------------|:--:|:----:|:--------:|-----------|
| 14| **Snowflake**        | Sink        | KP | 3/4  | 1000-1200| Leading cloud DW. Snowpipe Streaming |
| 15| **GCS**              | Sink+Source | KP | 3/4  | 300-500  | Thin adapter over S3 architecture |
| 16| **Azure Blob**       | Sink+Source | KP | 3/4  | 300-500  | Thin adapter over S3 architecture |
| 17| **Redshift**         | Sink        |    | 2/4  | 800-1000 | #2540. AWS cloud DW |
| 18| **BigQuery**         | Sink        |    | 3/4  | 1000-1200| GCP analytics DW |
| 19| **Delta Lake**       | Sink+Source |    | 2/4  | 800-1000 | #1852. Databricks ecosystem |
| 20| **Apache Flink**     | Source+Sink | KP | 2/4  | 800-1000 | Java connector JAR for Flink |

**After Phase 3**: Iggy can feed all major cloud DWs and object stores. Flink integration enables complex stream processing.

### Phase 4: Ecosystem & Bridges

These expand the ecosystem with bridges and specialized connectors.

| # | Connector/Codec      | Type        | KP | Comp | Est. LOC | Rationale |
|---|----------------------|-------------|:--:|:----:|:--------:|-----------|
| 21| **RabbitMQ / AMQP**  | Source+Sink |    | 3/4  | 600-800  | Migration path from legacy MQ |
| 22| **Apache Kafka**     | Source+Sink |    | n/a  | 600-800  | Bridge for Kafka migration |
| 23| **Amazon Kinesis**   | Source+Sink |    | 3/4  | 600-800  | Cross-cloud streaming bridge |
| 24| **Splunk**           | Sink        |    | 3/4  | 400-600  | Enterprise observability |
| 25| **Prometheus**       | Sink        |    | 1/4  | 400-500  | remote_write for monitoring |
| 26| **Grafana Loki**     | Sink        |    | 1/4  | 400-500  | Log aggregation |
| 27| **BSON Codec**       | Codec       |    | 0/4  | 200-300  | #1847. MongoDB native |
| 28| **OPC-UA**           | Source      |    | 1/4  | 600-800  | Industrial IoT |
| 29| **Cassandra**        | Sink        |    | 3/4  | 600-800  | Wide-column store |
| 30| **DynamoDB**         | Sink+Source |    | 3/4  | 600-800  | AWS NoSQL |

---

## 7. The IoT Differentiator Story

Iggy's strongest strategic positioning vs Kafka/Pulsar/Redpanda:

```
         IoT Device Layer                Iggy Layer                  Analytics Layer
  +--------------------------+     +------------------+     +------------------------+
  | Sensors (MQTT)      -----|---->|                  |---->| InfluxDB (time-series) |
  | PLCs (OPC-UA)       -----|---->|     IGGY         |---->| ClickHouse (OLAP)      |
  | Gateways (HTTP)     -----|---->|                  |---->| S3 + Parquet (lake)    |
  | Cameras (gRPC)      -----|---->|  Single binary   |---->| Elasticsearch (search) |
  | Telemetry (OTLP)    -----|---->|  ~15MB           |---->| MongoDB (documents)    |
  | Edge devices        -----|---->|  No JVM          |---->| Redis (real-time)      |
  |   (FlatBuffers)     -----|---->|  Runs on RPi     |---->| Snowflake (DW)         |
  |   (Protobuf)        -----|---->|                  |---->| Grafana (dashboards)   |
  +--------------------------+     +------------------+     +------------------------+

  UNIQUE ADVANTAGES:
  - FlatBuffers codec (zero-copy, ONLY Iggy has this)
  - Single ~15MB binary (vs Kafka's JVM + ZooKeeper)
  - Runs on Raspberry Pi (edge computing)
  - Rust performance + memory safety
  - MQTT + InfluxDB + FlatBuffers = unmatched IoT pipeline
```

---

## 8. Apache Camel Integration Note

KP mentioned Apache Camel specifically. Rather than building individual connectors for every possible target, an Apache Camel integration strategy could provide access to 193+ systems through a single bridge:

**Option A**: Build an Iggy component for Apache Camel (Java)
- Iggy becomes a Camel endpoint: `from("iggy:stream/topic").to("slack:channel")`
- Immediately inherits 193+ Camel connectors
- Requires JVM (conflicts with Iggy's "no JVM" positioning)

**Option B**: Build a Camel-Kafka-Connector compatibility layer
- Iggy already has Kafka wire protocol compatibility (for Pinot)
- If expanded, any Camel Kafka Connector works with Iggy out of the box

**Option C**: Selective native connectors + HTTP/gRPC for the rest
- Build native Rust connectors for top 20-30 targets
- HTTP/Webhook + gRPC connectors serve as universal fallback
- No JVM dependency, maintains Iggy's lightweight positioning

**Recommended**: Option C as primary strategy, Option A as secondary for enterprise users who already have JVM infrastructure.

---

## 9. Total Count Summary

| Category                  | Total Targets | Iggy Has | Planned | Missing |
|---------------------------|:------------:|:--------:|:-------:|:-------:|
| RDBMS                     | 8            | 1        | 1       | 6       |
| NoSQL / Document          | 8            | 0        | 1       | 7       |
| Search & Analytics        | 8            | 3        | 0       | 5       |
| Cloud Object Storage      | 6            | 0        | 0       | 6       |
| Data Lakehouse Formats    | 4            | 1        | 1       | 2       |
| Data Warehouses           | 10           | 0        | 2       | 8       |
| Time-Series DBs           | 7            | 0        | 1       | 6       |
| Graph DBs                 | 4            | 0        | 0       | 4       |
| Message Queues & Streaming| 12           | 0        | 0       | 12      |
| Caches & KV Stores        | 6            | 0        | 0       | 6       |
| File Systems & Formats    | 9            | 0        | 2       | 7       |
| HTTP & API Protocols      | 4            | 0        | 0       | 4       |
| Observability             | 7            | 0        | 0       | 7       |
| AI/ML & Vector DBs        | 6            | 0        | 0       | 6       |
| SaaS & Enterprise         | 6            | 0        | 0       | 6       |
| Stream Processing         | 6            | 0        | 0       | 6       |
| Workflow & Orchestration   | 4            | 0        | 0       | 4       |
| IoT Protocols             | 5            | 0        | 0       | 5       |
| **TOTAL**                 | **120**      | **5**    | **8**   | **107** |

KP-mentioned targets: 12 (of which 2 are HAVE, 1 is PLANNED, 9 are MISSING)

---

## 10. Sources

- Confluent Kafka Connectors: https://docs.confluent.io/platform/current/connect/kafka_connectors.html
- Confluent Hub: https://www.confluent.io/hub/
- Apache Pulsar IO: https://pulsar.apache.org/docs/next/io-connectors/
- StreamNative Hub: https://docs.streamnative.io/hub
- Redpanda Connect: https://docs.redpanda.com/redpanda-connect/components/about/
- Synadia NATS Connectors: https://www.synadia.com/platform
- Apache Camel Kafka Connector: https://camel.apache.org/camel-kafka-connector/4.10.x/reference/index.html
- Awesome Kafka Connect: https://github.com/conduktor/awesome-kafka-connect
- Apache Iggy Connectors: https://github.com/apache/iggy/tree/master/core/connectors
