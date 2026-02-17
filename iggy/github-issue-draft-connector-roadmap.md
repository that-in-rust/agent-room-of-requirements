# Connector Ecosystem Roadmap: tracking 120+ connector targets across databases, cloud, IoT, and observability

## Overview

Apache Iggy's connector ecosystem is growing. This issue tracks the full landscape of connectors -- what's done, what's in progress, what's planned, and what's proposed next -- to help contributors find high-impact work and avoid duplication.

**Current state**: 5 native Rust connectors (sinks + sources) + 2 Java connectors + 2 codecs in progress.

**Competitive context**: Kafka Connect has 200+ connectors, Redpanda Connect has 200+ (via Benthos), Pulsar IO has 40+ built-in. Iggy's Rust plugin model (cdylib + C FFI) offers performance and resource advantages but needs breadth to compete.

---

## Status: Done

| Connector | Type | Issue | Notes |
|-----------|------|-------|-------|
| [PostgreSQL](https://www.postgresql.org/) | Sink + Source (CDC) | #1849 | Native Rust. WAL-based CDC for source. ~2,400 LOC |
| [Elasticsearch](https://www.elastic.co/elasticsearch) | Sink + Source | #1851 | Native Rust. Bulk API sink, scroll/search source. ~1,500 LOC |
| [Apache Iceberg](https://iceberg.apache.org/) | Sink | #1850 | Native Rust. 7k GitHub stars, used by Airbnb, Apple, LinkedIn |
| [Quickwit](https://quickwit.io/) | Sink | -- | Native Rust. Cloud-native search engine. ~260 LOC |
| Stdout | Sink | -- | Reference implementation for connector developers. ~155 LOC |
| [Apache Pinot](https://pinot.apache.org/) | Sink | -- | Java connector via Kafka compatibility layer |

**Connector runtime infrastructure** (shipped):
- HTTP-based configuration provider (#2388)
- Separated connector/runtime config (#2318)
- E2E tests: Iceberg sink (#2595), Elasticsearch sink (#2592), Quickwit sink (#2594)

---

## Status: In Progress (Open Issues)

| Connector | Type | Issue | Assignee | Notes |
|-----------|------|-------|----------|-------|
| [InfluxDB](https://www.influxdata.com/) | Sink + Source | #2700 | @ryerraguntla | 31k GitHub stars. #1 time-series DB. IoT standard |
| [ClickHouse](https://clickhouse.com/) | Sink | #2539 | @hemantkrsh | 45k GitHub stars. Real-time OLAP |
| [Redshift](https://aws.amazon.com/redshift/) | Sink | #2540 | @GaneshPatil7517 | AWS cloud data warehouse |
| [JDBC / MySQL](https://dev.mysql.com/) | Sink + Source | #2500 | @shbhmrzd | Generic JDBC covers MySQL, MariaDB, others |
| [Delta Lake](https://delta.io/) | Sink + Source | #1852 | @Aditya-PS-05 | 8.6k GitHub stars. Lakehouse format |
| [MongoDB](https://www.mongodb.com/) | Sink + Source | #2739 | *(unassigned)* | 28k GitHub stars. Most popular NoSQL. Change Streams CDC |
| Avro codec | Codec | #1846 | *(unassigned)* | Kafka ecosystem standard serialization |
| BSON codec | Codec | #1847 | @sobczal2 | MongoDB native binary format |
| Flink transport | Enhancement | #2484 | @GaneshPatil7517 | Switch Flink connector transport HTTP to TCP |

**E2E tests in progress**: Pinot (#2598), Elasticsearch source (#2593)
**Runtime bug**: Connector loading loop on Linux (#2712, @hubcio)

---

## Status: Proposed -- Comprehensive Connector Target List

Organized by category. For each target:
- **Priority**: P0 (critical) / P1 (high) / P2 (medium) / P3 (low) / P4 (niche)
- **Comp**: How many of {Kafka, Pulsar, Redpanda, NATS} have this connector
- **Rust Crate**: The crate a contributor would use to build this connector

---

### 1. Relational Databases

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [MySQL / MariaDB](https://dev.mysql.com/) | Sink+Source | P1 | 4/4 | Most popular RDBMS globally. Covered by planned JDBC connector #2500. Every web application's default database. | [`sqlx`](https://crates.io/crates/sqlx) (54.9M downloads) or [`mysql_async`](https://crates.io/crates/mysql_async) |
| [Microsoft SQL Server](https://www.microsoft.com/sql-server) | Sink+Source | P2 | 3/4 | Enterprise RDBMS. Required for Fortune 500 adoption. Debezium CDC in Kafka ecosystem. | [`tiberius`](https://crates.io/crates/tiberius) (native TDS protocol) |
| [Oracle](https://www.oracle.com/database/) | Sink+Source | P3 | 3/4 | Complex licensing (GoldenGate CDC). Enterprise-heavy. Required for legacy enterprise migration but licensing costs limit adoption. | No mature Rust crate; JDBC bridge or C OCI FFI |
| [SQLite](https://www.sqlite.org/) | Sink | P4 | 2/4 | Embedded database. Niche use case for local/edge analytics sinks. | [`rusqlite`](https://crates.io/crates/rusqlite) |
| [CockroachDB](https://www.cockroachlabs.com/) | Sink+Source | -- | 2/4 | PostgreSQL wire protocol compatible. Works via existing Postgres connector automatically. | Existing PG connector |
| [IBM Db2](https://www.ibm.com/db2) | Sink+Source | P4 | 1/4 | Enterprise/mainframe only. Very niche. | JDBC bridge |
| Generic JDBC | Sink+Source | P1 | 3/4 | Planned as #2500. Covers MySQL, MariaDB, and dozens of other databases through a single connector. | [`sqlx`](https://crates.io/crates/sqlx) |

### 2. NoSQL / Document Databases

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [MongoDB](https://www.mongodb.com/) | Sink+Source | P0 | 4/4 | Planned #2739. 28k GitHub stars, 50k customers. Most popular NoSQL DB. Change Streams enable real-time CDC without WAL complexity. Essential for IoT device metadata and telemetry storage. | [`mongodb`](https://crates.io/crates/mongodb) (official, 9.5M downloads) |
| [Cassandra](https://cassandra.apache.org/) | Sink | P2 | 3/4 | 9.6k stars. Wide-column store optimized for high-write workloads. Bloomberg serves 20B+ requests/day on 1,700+ nodes. Used by Netflix, Apple. Essential for time-series and IoT at massive scale. | [`scylla`](https://crates.io/crates/scylla) (Cassandra-compatible, pure Rust) |
| [DynamoDB](https://aws.amazon.com/dynamodb/) | Sink+Source | P2 | 3/4 | AWS-native NoSQL. Handles 10T+ requests/day. DynamoDB Streams for CDC source. Required for AWS-centric architectures. Used by Lyft, Airbnb, Samsung. | [`aws-sdk-dynamodb`](https://crates.io/crates/aws-sdk-dynamodb) (official AWS SDK) |
| [Couchbase](https://www.couchbase.com/) | Sink+Source | P3 | 2/4 | Multi-model NoSQL (document + KV + search). Used in mobile/edge sync. Less common than MongoDB. | No mature Rust crate; REST API via `reqwest` |
| [HBase](https://hbase.apache.org/) | Sink | P3 | 2/4 | Hadoop ecosystem wide-column store. Declining as Cassandra and cloud-native alternatives grow. | No Rust crate; Thrift/REST API |
| [Azure Cosmos DB](https://azure.microsoft.com/cosmosdb) | Sink+Source | P3 | 1/4 | Azure-native multi-model database. MongoDB API compatible, so MongoDB connector partially covers it. | [`azure_data_cosmos`](https://crates.io/crates/azure_data_cosmos) |
| [ScyllaDB](https://www.scylladb.com/) | Sink | P3 | 1/4 | Cassandra-compatible but written in C++ for 10x performance. Growing adoption for low-latency workloads. Covered by Cassandra connector. | [`scylla`](https://crates.io/crates/scylla) (official Rust driver) |
| [Apache CouchDB](https://couchdb.apache.org/) | Sink+Source | P4 | 1/4 | Document DB with built-in replication. Niche. | [`reqwest`](https://crates.io/crates/reqwest) (CouchDB REST API) |

### 3. Search & Analytics Engines

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [OpenSearch](https://opensearch.org/) | Sink | P1 | 2/4 | 12.4k GitHub stars. Elasticsearch fork, AWS-aligned. Linux Foundation project. May work as thin adapter over existing ES connector with compatibility layer. | [`opensearch`](https://crates.io/crates/opensearch) (official Rust client) |
| [Apache Solr](https://solr.apache.org/) | Sink | P3 | 2/4 | Legacy search engine. Declining as Elasticsearch/OpenSearch dominate. Only for existing Solr shops. | [`reqwest`](https://crates.io/crates/reqwest) (Solr REST API) |
| [Splunk](https://www.splunk.com/) | Sink | P2 | 3/4 | 15k customers. 89 of Fortune 100. Acquired by Cisco for $28B. HTTP Event Collector (HEC) API makes integration straightforward. Enterprise observability standard. | [`reqwest`](https://crates.io/crates/reqwest) (HEC is HTTP POST) |
| [Meilisearch](https://www.meilisearch.com/) | Sink | P4 | 0/4 | 48k GitHub stars. Lightweight search engine with great DX. Growing alternative to Elasticsearch for smaller deployments. | [`meilisearch-sdk`](https://crates.io/crates/meilisearch-sdk) |
| [Typesense](https://typesense.org/) | Sink | P4 | 0/4 | 22k GitHub stars. Another lightweight search alternative. REST API. | [`reqwest`](https://crates.io/crates/reqwest) (Typesense REST API) |

### 4. Cloud Object Storage

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [Amazon S3](https://aws.amazon.com/s3/) | Sink+Source | P0 | 4/4 | Universal data lake landing zone. 350T+ objects stored, 100M+ req/sec. 90%+ Fortune 100 via AWS. Enables Snowflake/Redshift S3 staging. Build with abstract storage interface so GCS/Azure/MinIO become thin adapters. | [`aws-sdk-s3`](https://crates.io/crates/aws-sdk-s3) (official AWS SDK, v1.123) |
| [Google Cloud Storage](https://cloud.google.com/storage) | Sink+Source | P1 | 3/4 | GCP object storage. Thin adapter over S3 connector architecture. GCP holds ~13% cloud market. | [`cloud-storage`](https://crates.io/crates/cloud-storage) or [`google-cloud-storage`](https://crates.io/crates/google-cloud-storage) |
| [Azure Blob Storage](https://azure.microsoft.com/products/storage/blobs) | Sink+Source | P1 | 3/4 | Azure object storage. Thin adapter over S3 connector architecture. Azure holds ~20% cloud market. | [`azure_storage_blobs`](https://crates.io/crates/azure_storage_blobs) |
| [MinIO](https://min.io/) | Sink+Source | P1 | 1/4 | S3-compatible, self-hosted. 50k+ GitHub stars. Works via S3 connector automatically since it implements S3 API. | `aws-sdk-s3` (S3-compatible) |
| [DigitalOcean Spaces](https://www.digitalocean.com/products/spaces) | Sink | P4 | 0/4 | S3-compatible. Covered by S3 connector. | `aws-sdk-s3` (S3-compatible) |
| [Backblaze B2](https://www.backblaze.com/cloud-storage) | Sink | P4 | 0/4 | S3-compatible. Covered by S3 connector. | `aws-sdk-s3` (S3-compatible) |

### 5. Data Lakehouse Formats

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [Delta Lake](https://delta.io/) | Sink+Source | P2 | 2/4 | Planned #1852. 8.6k GitHub stars. Databricks/Linux Foundation. ACID transactions on data lakes. Growing fast with Databricks adoption. | [`deltalake`](https://crates.io/crates/deltalake) (Rust-native, delta-rs project) |
| [Apache Hudi](https://hudi.apache.org/) | Sink | P3 | 1/4 | Uber's lakehouse format. 5.5k stars. Strong in incremental processing and CDC use cases. Less popular than Iceberg/Delta. | [`hudi`](https://crates.io/crates/hudi) (Rust-native, apache/hudi-rs) |
| [Apache Paimon](https://paimon.apache.org/) | Sink | P4 | 0/4 | Flink-native lakehouse format. Emerging. Formerly Flink Table Store. Optimized for streaming writes. | No Rust crate; Java only |

### 6. Data Warehouses

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [Snowflake](https://www.snowflake.com/) | Sink | P1 | 3/4 | Leading cloud DW. 12k+ customers, $1.09B product revenue (Q2 FY26). Snowpipe Streaming API for real-time ingestion. 3/4 competitors have it. | [`reqwest`](https://crates.io/crates/reqwest) (Snowpipe REST API); or S3 staging |
| [ClickHouse](https://clickhouse.com/) | Sink | P1 | 2/4 | Planned #2539. 45k GitHub stars. Real-time OLAP. $400M Series D (Jan 2026). Native HTTP interface. Popular in Rust community. | [`clickhouse`](https://crates.io/crates/clickhouse); [`klickhouse`](https://crates.io/crates/klickhouse) (native protocol) |
| [Amazon Redshift](https://aws.amazon.com/redshift/) | Sink | P2 | 2/4 | Planned #2540. AWS cloud DW. S3 staging + COPY pattern for efficient bulk loading. | `aws-sdk-s3` + [`sqlx`](https://crates.io/crates/sqlx) (PG wire protocol) |
| [Google BigQuery](https://cloud.google.com/bigquery) | Sink | P2 | 3/4 | GCP flagship analytics warehouse. 13.6% DW market share. 13k+ companies. Storage Write API for streaming. | [`gcp-bigquery-client`](https://crates.io/crates/gcp-bigquery-client) |
| [Databricks](https://www.databricks.com/) | Sink | P2 | 2/4 | Via Delta Lake connector or SQL API. Databricks SQL Connector available. Spark ecosystem integration. | `deltalake` crate or REST API |
| [Azure Synapse](https://azure.microsoft.com/products/synapse-analytics) | Sink | P3 | 1/4 | Microsoft cloud DW. Competes with Snowflake on Azure. | [`tiberius`](https://crates.io/crates/tiberius) (TDS/SQL Server protocol) |
| [StarRocks](https://www.starrocks.io/) | Sink | P3 | 1/4 | Real-time OLAP. Fast-growing fork of Apache Doris. Strong benchmark performance for complex JOINs. | [`reqwest`](https://crates.io/crates/reqwest) (Stream Load HTTP API) |
| [Apache Doris](https://doris.apache.org/) | Sink | P3 | 1/4 | StarRocks parent project. 13k+ GitHub stars. Strong in China/Asia-Pacific. | [`reqwest`](https://crates.io/crates/reqwest) (Stream Load HTTP API) |
| [Firebolt](https://www.firebolt.io/) | Sink | P4 | 0/4 | Niche cloud DW for extreme query speed. Startup. | REST API via `reqwest` |
| [DuckDB](https://duckdb.org/) | Sink | P3 | 0/4 | 28k+ GitHub stars. Embedded OLAP. Huge Rust/data community adoption. "SQLite for analytics." | [`duckdb`](https://crates.io/crates/duckdb) (official Rust bindings) |

### 7. Time-Series Databases

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [InfluxDB](https://www.influxdata.com/) | Sink+Source | P0 | 2/4 | Planned #2700. 31k GitHub stars. #1 time-series DB by community. IoT standard. Line protocol write API is universal. InfluxDB 3 is built in Rust. | [`reqwest`](https://crates.io/crates/reqwest) (HTTP API; no mature Rust client) |
| [TimescaleDB](https://www.timescale.com/) | Sink+Source | -- | 2/4 | PostgreSQL extension. Works via existing Postgres connector automatically. No additional work needed. | Existing PG connector |
| [Prometheus](https://prometheus.io/) | Sink | P2 | 1/4 | 63k GitHub stars. CNCF graduated. Industry-standard monitoring. `remote_write` API (protobuf/snappy over HTTP) for pushing metrics from Iggy. | [`prost`](https://crates.io/crates/prost) + [`reqwest`](https://crates.io/crates/reqwest) |
| [QuestDB](https://questdb.io/) | Sink | P3 | 1/4 | 15k GitHub stars. Fast time-series DB. InfluxDB Line Protocol compatible, so InfluxDB connector could cover it. | InfluxDB Line Protocol or PG wire protocol |
| [TDengine](https://tdengine.com/) | Sink | P3 | 0/4 | IoT-focused TSDB. Popular in Asia-Pacific. REST API available. | [`reqwest`](https://crates.io/crates/reqwest) (REST API) |
| [VictoriaMetrics](https://victoriametrics.com/) | Sink | P3 | 0/4 | 13k+ GitHub stars. Prometheus-compatible. Covered by Prometheus remote_write connector. | Same as Prometheus (`remote_write`) |
| [CrateDB](https://cratedb.com/) | Sink | P4 | 0/4 | SQL time-series DB. PostgreSQL wire protocol compatible. Works via PG connector. | Existing PG connector or `sqlx` |

### 8. Graph Databases

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [Neo4j](https://neo4j.com/) | Sink | P3 | 3/4 | $200M+ ARR. 84% Fortune 100. 44% graph DB market. Stream events into graph for relationship analysis, fraud detection, recommendation engines. | [`neo4rs`](https://crates.io/crates/neo4rs) (async Bolt protocol client) |
| [ArangoDB](https://www.arangodb.com/) | Sink | P4 | 0/4 | Multi-model (graph + document + KV). 14k GitHub stars. Niche but versatile. | [`arangors`](https://crates.io/crates/arangors) |
| [Amazon Neptune](https://aws.amazon.com/neptune/) | Sink | P4 | 0/4 | AWS-managed graph DB. Gremlin and SPARQL APIs. | `reqwest` (Neptune REST API) |
| [JanusGraph](https://janusgraph.org/) | Sink | P4 | 0/4 | Open-source, Hadoop-backed graph DB. Declining adoption. | Gremlin protocol via `reqwest` |

### 9. Message Queues & Streaming Bridges

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [MQTT](https://mqtt.org/) | Source+Sink | P0 | 3/4 | THE IoT protocol. De facto standard with 50%+ enterprise IoT adoption. Billions of connected devices. Iggy's "runs on Raspberry Pi" story is incomplete without MQTT. The single most important missing connector. | [`rumqttc`](https://crates.io/crates/rumqttc) (237K downloads/month, async, MQTT v5) |
| [RabbitMQ / AMQP](https://www.rabbitmq.com/) | Source+Sink | P1 | 3/4 | 13k GitHub stars. Most popular traditional message broker. Migration path from legacy MQ to Iggy. AMQP 0.9.1 protocol. | [`lapin`](https://crates.io/crates/lapin) (async AMQP 0.9.1) |
| [Apache Kafka](https://kafka.apache.org/) | Source+Sink | P2 | n/a | 32k GitHub stars. 80%+ Fortune 100. Bridge connector for gradual Kafka-to-Iggy migration. Enables hybrid architectures during migration. | [`rdkafka`](https://crates.io/crates/rdkafka) (18.6M sys downloads) |
| [Amazon Kinesis](https://aws.amazon.com/kinesis/) | Source+Sink | P2 | 3/4 | AWS streaming service. Cross-cloud bridge for AWS-centric organizations moving to Iggy. | [`aws-sdk-kinesis`](https://crates.io/crates/aws-sdk-kinesis) (official AWS SDK) |
| [Amazon SQS](https://aws.amazon.com/sqs/) | Source+Sink | P3 | 2/4 | AWS queue service. Simple point-to-point messaging. Bridge for SQS-to-Iggy migration. | [`aws-sdk-sqs`](https://crates.io/crates/aws-sdk-sqs) |
| [Google Pub/Sub](https://cloud.google.com/pubsub) | Source+Sink | P2 | 2/4 | GCP streaming/messaging service. Cross-cloud bridge for GCP organizations. | [`google-cloud-pubsub`](https://crates.io/crates/google-cloud-pubsub) |
| [Apache Pulsar](https://pulsar.apache.org/) | Source+Sink | P3 | 1/4 | Alternative streaming platform. Bridge connector for Pulsar-to-Iggy migration. | [`pulsar`](https://crates.io/crates/pulsar) (async Rust client) |
| [NATS / JetStream](https://nats.io/) | Source+Sink | P3 | 1/4 | Lightweight messaging. Growing in cloud-native/K8s. Bridge for NATS-to-Iggy migration. | [`async-nats`](https://crates.io/crates/async-nats) (official async client) |
| [NSQ](https://nsq.io/) | Source+Sink | P4 | 2/4 | Simple distributed queue by Bitly. Declining. | No mature Rust crate |
| [IBM MQ](https://www.ibm.com/products/mq) | Source+Sink | P4 | 1/4 | Enterprise mainframe messaging. Only for large financial institutions with IBM infrastructure. | No native Rust crate; JMS bridge |
| [Azure Service Bus](https://azure.microsoft.com/products/service-bus) | Source+Sink | P3 | 1/4 | Azure messaging service. AMQP 1.0 protocol. | [`azure_messaging_servicebus`](https://crates.io/crates/azure_messaging_servicebus); or [`fe2o3-amqp`](https://crates.io/crates/fe2o3-amqp) |
| [Azure Event Hubs](https://azure.microsoft.com/products/event-hubs) | Source | P3 | 1/4 | Azure Kafka-compatible event streaming. Since it supports Kafka wire protocol, the Kafka bridge connector covers it. | `rdkafka` (Kafka-compatible protocol) |

### 10. Caches & Key-Value Stores

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [Redis](https://redis.io/) | Sink+Source | P0 | 3/4 | 67k+ GitHub stars. Most popular KV store. Cache warming from streams, real-time state management, pub/sub bridge. 4B+ Docker pulls. 10k enterprise customers. | [`redis`](https://crates.io/crates/redis) (official); [`fred`](https://crates.io/crates/fred) (high-level async) |
| [DragonflyDB](https://www.dragonflydb.io/) | Sink+Source | P3 | 0/4 | 29.4k GitHub stars. Redis-compatible with 25x throughput. Covered by Redis connector automatically. | `redis` crate (Redis-compatible API) |
| [Memcached](https://memcached.org/) | Sink | P4 | 1/4 | Legacy cache. Declining in favor of Redis. Still used by Facebook, Wikipedia. | [`memcache`](https://crates.io/crates/memcache) |
| [Aerospike](https://aerospike.com/) | Sink | P4 | 2/4 | High-performance KV for adtech, fraud detection. $1B+ valuation. Niche. | [`aerospike`](https://crates.io/crates/aerospike) |
| [Hazelcast](https://hazelcast.com/) | Source | P4 | 2/4 | In-memory data grid. Java-centric. Low priority. | REST API via `reqwest` |
| [etcd](https://etcd.io/) | Sink+Source | P4 | 0/4 | 48k+ GitHub stars. CNCF graduated. Kubernetes config store. Streaming config changes for K8s auditing. | [`etcd-client`](https://crates.io/crates/etcd-client) (async gRPC) |

### 11. File Systems & Formats

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| Local Filesystem | Sink+Source | P3 | 2/4 | File tail source (like Filebeat) and file write sink. Basic but essential for log ingestion and data export. | [`tokio::fs`](https://docs.rs/tokio); [`notify`](https://crates.io/crates/notify) (file watcher) |
| FTP / SFTP | Sink+Source | P3 | 3/4 | Legacy file transfer. Still required in regulated industries (healthcare, banking). | [`suppaftp`](https://crates.io/crates/suppaftp); [`russh-sftp`](https://crates.io/crates/russh-sftp) |
| [HDFS](https://hadoop.apache.org/) | Sink | P3 | 3/4 | Declining but still in legacy Hadoop shops. Being replaced by S3/GCS. | [`hdfs-native`](https://crates.io/crates/hdfs-native) |
| [Parquet](https://parquet.apache.org/) (format) | Output fmt | P1 | 3/4 | De facto columnar storage format. Essential for S3/GCS/HDFS sinks. Without Parquet, streaming data to object storage is inefficient. | [`parquet`](https://crates.io/crates/parquet) (Apache Arrow, very mature) |
| [Avro](https://avro.apache.org/) (codec) | Codec | P0 | 4/4 | Planned #1846. Kafka ecosystem standard. Without Avro, interop with Kafka-migrating users is blocked. Enables schema evolution. | [`apache-avro`](https://crates.io/crates/apache-avro) (official) |
| [BSON](https://bsonspec.org/) (codec) | Codec | P2 | 0/4 | Planned #1847. MongoDB native format. Enables zero-transformation pipelines between Iggy and MongoDB. | [`bson`](https://crates.io/crates/bson) (official, 14.2M downloads) |
| [ORC](https://orc.apache.org/) (format) | Output fmt | P4 | 1/4 | Hadoop-specific columnar format. Declining as Parquet dominates. | No mature Rust crate |
| CSV (format) | Input/Output | P3 | 2/4 | Universal data exchange. Human-readable. Batch imports/exports. | [`csv`](https://crates.io/crates/csv) (BurntSushi's, very popular) |
| [MessagePack](https://msgpack.org/) (codec) | Codec | P4 | 1/4 | Compact binary. More efficient than JSON. Useful for bandwidth-constrained IoT. | [`rmp-serde`](https://crates.io/crates/rmp-serde) |

### 12. HTTP & API Protocols

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| HTTP / Webhook | Source+Sink | P0 | 4/4 | Universal integration. HTTP source receives webhooks from any service; HTTP sink pushes to any API. The "connect to anything" fallback. Every web service speaks HTTP. | [`reqwest`](https://crates.io/crates/reqwest) (client); [`axum`](https://crates.io/crates/axum) (server) |
| [gRPC](https://grpc.io/) | Source+Sink | P1 | 1/4 | 44k GitHub stars. High-performance RPC for microservices. Pairs with OTLP (which uses gRPC). Essential for microservice architectures. | [`tonic`](https://crates.io/crates/tonic) (gRPC); [`prost`](https://crates.io/crates/prost) (protobuf) |
| [GraphQL](https://graphql.org/) | Sink | P4 | 0/4 | Niche for streaming. GraphQL subscriptions could make Iggy a data source for GraphQL APIs. Specialized use case. | [`graphql_client`](https://crates.io/crates/graphql_client) |
| WebSocket | Source+Sink | P3 | 1/4 | Real-time bidirectional. Ingest trading data, chat, live updates. Push events to browser dashboards. | [`tokio-tungstenite`](https://crates.io/crates/tokio-tungstenite) |

### 13. Observability & Monitoring

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [OpenTelemetry (OTLP)](https://opentelemetry.io/) | Source+Sink | P0 | 1/4 | 2nd largest CNCF project. 10k contributors. 1,200 companies. OTLP becoming universal observability standard. Makes Iggy an observability pipeline backbone for logs, traces, and metrics. | [`opentelemetry`](https://crates.io/crates/opentelemetry); [`opentelemetry-otlp`](https://crates.io/crates/opentelemetry-otlp) |
| [Splunk (HEC)](https://www.splunk.com/) | Sink | P2 | 3/4 | 46.8% SIEM market. 18k+ companies. Cisco-owned ($28B acquisition). HTTP Event Collector is simple HTTP POST. | [`reqwest`](https://crates.io/crates/reqwest) |
| [Datadog](https://www.datadoghq.com/) | Sink | P3 | 2/4 | $827M Q2 2025 revenue. 47k+ customers. SaaS observability leader. HTTP API for metrics, logs, traces. | [`reqwest`](https://crates.io/crates/reqwest) |
| [Prometheus](https://prometheus.io/) remote_write | Sink | P2 | 1/4 | 63k GitHub stars. De facto monitoring standard. One connector covers the entire Prometheus ecosystem (VictoriaMetrics, Cortex, Thanos, Mimir). | [`prost`](https://crates.io/crates/prost) + `reqwest` (protobuf/snappy over HTTP) |
| [Grafana Loki](https://grafana.com/oss/loki/) | Sink | P2 | 1/4 | 28k GitHub stars. 100k+ active clusters. 1B+ Docker pulls. Log aggregation that pairs with Grafana. HTTP push API. | [`reqwest`](https://crates.io/crates/reqwest) |
| [Jaeger](https://www.jaegertracing.io/) | Sink | P3 | 0/4 | 22k+ GitHub stars. CNCF graduated. Being replaced by OTLP as ingestion standard, so OTLP connector covers it. | `opentelemetry-otlp` (Jaeger now prefers OTLP) |
| [New Relic](https://newrelic.com/) | Sink | P4 | 1/4 | 552k+ companies. Supports OTLP, so the OTLP connector covers it. | `reqwest` or OTLP connector |

### 14. AI/ML & Vector Databases

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [Qdrant](https://qdrant.tech/) | Sink | P3 | 0/4 | 27k+ GitHub stars. Rust-native vector DB. Natural ecosystem fit for Iggy. Stream embeddings for real-time semantic search, RAG, recommendations. | [`qdrant-client`](https://crates.io/crates/qdrant-client) (official gRPC client) |
| [Weaviate](https://weaviate.io/) | Sink | P3 | 0/4 | 11k GitHub stars. 1M+ pulls/month. Best-in-class hybrid search. REST API. | `reqwest` (REST API) |
| [Pinecone](https://www.pinecone.io/) | Sink | P3 | 0/4 | Leading SaaS vector DB. Simplest integration (REST API). Used by Gong, Vanguard. | [`pinecone-sdk`](https://crates.io/crates/pinecone-sdk) or `reqwest` |
| [Milvus](https://milvus.io/) | Sink | P3 | 0/4 | 40k+ GitHub stars. Most popular OSS vector DB. Used by NVIDIA, Salesforce, eBay. 72% memory reduction in v2.6. | [`milvus-sdk`](https://crates.io/crates/milvus-sdk); or gRPC via `tonic` |
| [MLflow](https://mlflow.org/) | Sink | P4 | 0/4 | 23k GitHub stars. 30M+ monthly downloads. Most popular MLOps platform. Stream training metrics. | `reqwest` (REST API) |
| [Feast](https://feast.dev/) | Source | P4 | 0/4 | 5k+ GitHub stars. Feature store. Linux Foundation. ML feature serving from Iggy. | `reqwest` (REST API) |

### 15. SaaS & Enterprise

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [Salesforce](https://www.salesforce.com/) | Source+Sink | P4 | 1/4 | #1 CRM. $34.9B revenue. 150k+ customers. Stream CRM events. Enterprise-heavy. | `reqwest` (REST/Bulk API) |
| [ServiceNow](https://www.servicenow.com/) | Source+Sink | P4 | 1/4 | Leading ITSM. $10B+ revenue. 85% Fortune 500. Stream incident events. | `reqwest` (REST API) |
| [Slack](https://slack.com/) | Sink | P4 | 0/4 | 65M+ daily active users. Alert notifications from Iggy streams to channels. Simple webhook. | `reqwest` (Webhook HTTP POST) |
| Email (SMTP) | Sink | P4 | 1/4 | Universal alert notifications. Stream events matching conditions as email alerts. | [`lettre`](https://crates.io/crates/lettre) |
| [Stripe](https://stripe.com/) | Source | P4 | 0/4 | Leading payment processor. $1T+ processed. Ingest payment events for real-time financial analytics. | `reqwest` (webhooks) |
| [Twilio](https://www.twilio.com/) | Sink | P4 | 0/4 | Leading CPaaS. 300k+ accounts. SMS alerts for IoT scenarios (equipment failure notifications). | `reqwest` (REST API) |

### 16. Stream Processing Integration

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [Apache Flink](https://flink.apache.org/) | Source+Sink | P1 | 2/4 | 26k GitHub stars. Leading stream processor. Used by Alibaba, Apple, Netflix, Uber. Needs Flink connector JAR. Enables complex event processing, windowing, joins. Already has #2484 for transport. | Java connector JAR; Iggy Kafka compat could help |
| [Apache Spark Streaming](https://spark.apache.org/) | Source | P3 | 2/4 | 41k GitHub stars. Most popular data processing framework. Structured Streaming for batch+stream. | Java/Scala connector; or Kafka compat layer |
| [Apache Beam](https://beam.apache.org/) | Source+Sink | P3 | 1/4 | 8k+ GitHub stars. Google-backed. Unified batch+stream. Runs on Flink, Spark, Dataflow. | Java SDK connector |
| [Materialize](https://materialize.com/) | Source | P4 | 0/4 | Streaming SQL DB. PostgreSQL-compatible. Incremental materialized views. | PG wire protocol or Kafka compat |
| [RisingWave](https://risingwave.com/) | Source | P4 | 0/4 | 8.6k GitHub stars. Rust-based streaming DB. Natural ecosystem partner. PG-compatible. | Native Rust integration or PG/Kafka compat |
| [Apache Camel](https://camel.apache.org/) | Framework | P2 | n/a | 6.1k GitHub stars. 193+ connectors (Kamelets). An Iggy Camel component would give access to hundreds of systems. Requires JVM. | Java component (Camel is JVM-based) |

### 17. Workflow & Orchestration

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [Apache Airflow](https://airflow.apache.org/) | Trigger | P4 | 1/4 | 44k GitHub stars. Industry standard workflow orchestration. Iggy sensor/trigger for event-driven DAGs. | `reqwest` (REST API) |
| [Temporal](https://temporal.io/) | Source+Sink | P4 | 0/4 | 12k+ GitHub stars. Durable execution platform. Bridge between streams and fault-tolerant workflows. | [`temporal-sdk-core`](https://crates.io/crates/temporal-sdk-core) (official Rust SDK) |
| [Prefect](https://www.prefect.io/) | Trigger | P4 | 0/4 | 20k GitHub stars. 25k+ community. Modern Airflow alternative. Event-driven workflow triggering. | `reqwest` (REST API / webhooks) |
| [Dagster](https://dagster.io/) | Source | P4 | 0/4 | 14k GitHub stars. Asset-based data orchestration. Growing adoption. | `reqwest` (REST API) |

### 18. IoT Protocols

| Target | Type | Priority | Comp | Why It Matters | Rust Crate |
|--------|------|:--------:|:----:|----------------|------------|
| [MQTT](https://mqtt.org/) | Source+Sink | P0 | 3/4 | (See #9.) De facto IoT standard. 50%+ enterprise adoption. $17.6B IoT protocol market. Billions of devices. The single most important missing connector. | [`rumqttc`](https://crates.io/crates/rumqttc) |
| [CoAP](https://coap.technology/) | Source+Sink | P3 | 0/4 | IETF RFC 7252. UDP-based, 4-byte header. For ultra-constrained sensors where MQTT is too heavy. Healthcare, robotics, smart cities. | [`coap`](https://crates.io/crates/coap); [`coap-lite`](https://crates.io/crates/coap-lite) |
| [OPC-UA](https://opcfoundation.org/about/opc-technologies/opc-ua/) | Source | P2 | 1/4 | IEC 62541 standard. 40%+ market share in industrial data acquisition. 1,000+ manufacturers. Industry 4.0 standard. Bridges factory floor into streaming. | [`opcua`](https://crates.io/crates/opcua) (pure Rust client/server) |
| [Modbus](https://www.modbus.org/) | Source | P3 | 1/4 | 40%+ market share in industrial data. Hundreds of millions of devices. 45+ years old. Legacy factory equipment integration. | [`tokio-modbus`](https://crates.io/crates/tokio-modbus) (async RTU/TCP) |
| [LwM2M](https://www.openmobilealliance.org/specifications/lwm2m/) | Source | P4 | 0/4 | IoT device management protocol on CoAP. 400+ ready-to-use objects. Smart metering, smart cities. Specialized. | `coap` crate (LwM2M builds on CoAP) |

---

## Codec / Serialization Format Status

| Format | Status | Issue | Notes |
|--------|--------|-------|-------|
| JSON | Done | -- | Built-in to connector runtime |
| Protobuf | Done | -- | Built-in to connector runtime |
| FlatBuffers | Done | -- | Unique to Iggy -- zero-copy for IoT |
| Raw / Bytes | Done | -- | Built-in |
| Text / String | Done | -- | Built-in |
| Avro | In progress | #1846 | Critical for Kafka ecosystem interop. [`apache-avro`](https://crates.io/crates/apache-avro) crate |
| BSON | In progress | #1847 | MongoDB native format. [`bson`](https://crates.io/crates/bson) crate (14.2M downloads) |
| Parquet | Proposed | -- | Output format for S3/GCS/HDFS sinks. [`parquet`](https://crates.io/crates/parquet) crate |
| CSV | Proposed | -- | Human-readable batch import/export. [`csv`](https://crates.io/crates/csv) crate |
| MessagePack | Proposed | -- | Compact binary for IoT. [`rmp-serde`](https://crates.io/crates/rmp-serde) crate |

---

## Summary Counts

| Category | Total | Done | In Progress | Proposed |
|----------|:-----:|:----:|:-----------:|:--------:|
| Relational Databases | 7 | 1 (PG) | 1 (JDBC) | 5 |
| NoSQL / Document | 8 | 0 | 1 (MongoDB) | 7 |
| Search & Analytics | 5 | 3 (ES, Quickwit, Pinot) | 0 | 2 |
| Cloud Object Storage | 6 | 0 | 0 | 6 |
| Data Lakehouse | 3 | 1 (Iceberg) | 1 (Delta) | 1 |
| Data Warehouses | 10 | 0 | 2 (CH, Redshift) | 8 |
| Time-Series DBs | 7 | 0 | 1 (InfluxDB) | 6 |
| Graph DBs | 4 | 0 | 0 | 4 |
| Message Queues | 12 | 0 | 0 | 12 |
| Caches & KV | 6 | 0 | 0 | 6 |
| File Systems & Formats | 9 | 0 | 2 (Avro, BSON) | 7 |
| HTTP & API | 4 | 0 | 0 | 4 |
| Observability | 7 | 0 | 0 | 7 |
| AI/ML & Vector DBs | 6 | 0 | 0 | 6 |
| SaaS & Enterprise | 6 | 0 | 0 | 6 |
| Stream Processing | 6 | 0 | 1 (Flink) | 5 |
| Workflow | 4 | 0 | 0 | 4 |
| IoT Protocols | 5 | 0 | 0 | 5 |
| **TOTAL** | **115** | **5** | **9** | **101** |

---

## How to Contribute

1. Check this issue and the linked open issues above to avoid duplicating work
2. Comment here to claim a proposed connector
3. Reference the existing connectors (PostgreSQL, Elasticsearch) as implementation templates
4. See the connector SDK traits (`Sink`, `Source`, `Transform`) in the SDK crate
5. Each connector is a separate Rust cdylib crate under `core/connectors/`
6. For every P0-P2 target, a mature Rust crate exists on crates.io (linked above)
