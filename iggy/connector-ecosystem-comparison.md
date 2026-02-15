# Streaming Platform Connector Ecosystem Comparison & Iggy Gap Analysis

**Date**: February 15, 2026
**Methodology**: Official documentation review of Apache Kafka (Confluent), Apache Pulsar, Redpanda, and NATS JetStream connector ecosystems, compared against Apache Iggy's current and planned connector set.

---

## 1. Comparison Matrix

Legend:
- `[x]` = Connector exists (official or verified partner)
- `[~]` = Partial support (e.g., via generic JDBC, community/unmaintained, or third-party bridge)
- `[ ]` = No connector available
- `[P]` = Planned/open issue in Iggy

### 1.1 Databases -- RDBMS

| Target System | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **PostgreSQL** (source+sink) | [x] JDBC + Debezium CDC | [x] JDBC sink, Debezium source | [x] postgres_cdc + SQL | [~] via Wombat/Benthos | [x] native source+sink |
| **MySQL** (source+sink) | [x] JDBC + Debezium CDC | [x] JDBC (MariaDB) sink, Debezium source | [x] mysql_cdc + SQL | [~] via Wombat/Benthos | [P] JDBC #2500 |
| **Microsoft SQL Server** (source+sink) | [x] Debezium CDC + JDBC | [x] Debezium source | [x] mssql_cdc + SQL | [ ] | [ ] |
| **Oracle** (source+sink) | [x] JDBC + Debezium CDC | [x] Debezium source | [x] SQL (oracle driver) | [ ] | [ ] |
| **SQLite** (sink) | [~] JDBC | [x] JDBC SQLite sink | [x] SQL (sqlite driver) | [ ] | [ ] |
| **MariaDB** (sink) | [x] JDBC | [x] JDBC MariaDB sink | [x] SQL (mysql driver) | [ ] | [P] JDBC #2500 |
| **CockroachDB** (source+sink) | [~] via JDBC (PG wire) | [~] via JDBC PostgreSQL | [~] via SQL (postgres) | [ ] | [~] via Postgres connector |
| **Db2** (source+sink) | [x] JDBC + Debezium | [ ] | [~] via SQL | [ ] | [ ] |
| **Generic JDBC** (source+sink) | [x] official | [x] JDBC sink (multiple) | [x] SQL driver abstraction | [ ] | [P] #2500 |

### 1.2 Databases -- NoSQL / Document

| Target System | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **MongoDB** (source+sink) | [x] official + Debezium CDC | [x] source + sink | [x] MongoDB + MongoDB CDC | [x] Synadia connector | [ ] |
| **Cassandra** (sink) | [x] DataStax connector | [x] built-in sink | [x] via SQL (Cassandra) | [ ] | [ ] |
| **DynamoDB** (source+sink) | [x] sink official; source via Debezium | [x] source | [x] output (DynamoDB) | [ ] | [ ] |
| **Couchbase** (source+sink) | [x] official partner | [x] via DataStax 3rd party | [ ] | [ ] | [ ] |
| **HBase** (sink) | [x] Lensesio stream-reactor | [x] built-in sink | [ ] | [ ] | [ ] |
| **Azure Cosmos DB** (source+sink) | [x] official | [ ] | [ ] | [ ] | [ ] |
| **Neo4j** (source+sink) | [x] official partner | [x] via DataStax 3rd party | [x] cypher output | [ ] | [ ] |

### 1.3 Search & Analytics Engines

| Target System | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **Elasticsearch** (source+sink) | [x] official | [x] built-in sink | [x] elasticsearch_v8, v9 | [ ] | [x] native source+sink |
| **OpenSearch** (sink) | [x] community | [~] via ES compat | [x] opensearch output | [ ] | [~] via ES connector |
| **Apache Solr** (sink) | [~] community | [x] via DataStax 3rd party | [ ] | [ ] | [ ] |
| **Quickwit** (sink) | [ ] | [ ] | [ ] | [ ] | [x] native sink |
| **Splunk** (source+sink) | [x] official sink | [x] via DataStax 3rd party | [x] input + output | [ ] | [ ] |
| **Apache Pinot** | [x] native Kafka ingestion | [ ] | [x] via Kafka compat | [ ] | [x] Java connector |

### 1.4 Cloud Storage & Data Lakes

| Target System | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **Amazon S3** (source+sink) | [x] official | [x] Cloud Storage sink | [x] input + output | [~] Synadia AWS connector | [ ] |
| **Google Cloud Storage** (sink) | [x] official | [x] Cloud Storage sink | [x] gcp_cloud_storage | [ ] | [ ] |
| **Azure Blob Storage** (sink) | [x] official | [~] via community | [x] azure_blob_storage | [~] Synadia Azure connector | [ ] |
| **HDFS 2/3** (source+sink) | [x] official | [x] built-in HDFS2+HDFS3 sink | [x] hdfs input + output | [ ] | [ ] |
| **Apache Iceberg** (sink) | [x] community (Tabular) | [x] StreamNative Lakehouse | [ ] | [ ] | [x] native sink |
| **Delta Lake** (sink) | [x] Databricks connector | [x] StreamNative Lakehouse | [ ] | [ ] | [P] #1852 |
| **Apache Hudi** | [~] community | [ ] | [ ] | [ ] | [ ] |

### 1.5 Data Warehouses

| Target System | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **Snowflake** (sink) | [x] official | [x] via KCA adapter | [x] snowflake_streaming output | [ ] | [ ] |
| **Google BigQuery** (source+sink) | [x] official | [x] StreamNative connector | [x] gcp_bigquery input+output | [ ] | [ ] |
| **Amazon Redshift** (sink) | [x] official | [x] StreamNative | [ ] | [ ] | [P] #2540 |
| **Azure Synapse Analytics** (sink) | [x] official | [ ] | [ ] | [ ] | [ ] |
| **ClickHouse** (sink) | [x] ClickHouse official | [x] JDBC ClickHouse sink | [x] SQL (clickhouse driver) | [ ] | [P] #2539 |
| **Databricks** (sink) | [x] official Delta Lake | [ ] | [x] SQL (databricks driver) | [ ] | [ ] |

### 1.6 Time-Series Databases

| Target System | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **InfluxDB** (source+sink) | [x] official | [x] built-in sink | [ ] | [ ] | [P] #2700 |
| **TimescaleDB** (sink) | [x] via JDBC (PG extension) | [x] via JDBC PostgreSQL | [x] via SQL (postgres) | [ ] | [~] via Postgres sink |
| **Prometheus** (sink) | [x] official Prometheus Metrics | [ ] | [ ] | [ ] | [ ] |
| **QuestDB** (sink) | [~] community | [ ] | [x] questdb output | [ ] | [ ] |

### 1.7 Message Queues & Other Streaming

| Target System | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **RabbitMQ / AMQP** (source+sink) | [x] official | [x] built-in source+sink | [x] amqp_1 input+output | [ ] | [ ] |
| **MQTT** (source+sink) | [x] official | [x] community (MoP) | [x] mqtt input+output | [ ] | [ ] |
| **ActiveMQ / JMS** (source+sink) | [x] official | [~] via JMS 3rd party | [ ] | [ ] | [ ] |
| **Amazon Kinesis** (source+sink) | [x] official source | [x] built-in source+sink | [x] aws_kinesis input+output | [ ] | [ ] |
| **Amazon SQS** (source+sink) | [x] community | [ ] | [x] aws_sqs input+output | [ ] | [ ] |
| **Google Pub/Sub** (source+sink) | [x] official | [ ] | [x] gcp_pubsub input+output | [ ] | [ ] |
| **Apache Pulsar** (source+sink) | [~] community | n/a | [x] pulsar input+output | [ ] | [ ] |
| **NATS / JetStream** (source+sink) | [~] community | [ ] | [x] nats, nats_jetstream | n/a | [ ] |
| **NSQ** (source+sink) | [ ] | [x] built-in source | [x] nsq input+output | [ ] | [ ] |

### 1.8 Caches & Key-Value Stores

| Target System | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **Redis** (source+sink) | [x] official (sink + source) | [x] built-in sink | [x] redis_list/pubsub/streams/hash | [ ] | [ ] |
| **Memcached** (sink) | [~] community (unmaintained) | [ ] | [ ] | [ ] | [ ] |
| **Aerospike** (sink) | [~] community | [x] built-in sink | [ ] | [ ] | [ ] |
| **Hazelcast** | [x] official source | [x] via DataStax 3rd party | [ ] | [ ] | [ ] |

### 1.9 SaaS & API Integrations

| Target System | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **Salesforce** (source+sink) | [x] official (8 connectors) | [ ] | [ ] | [ ] | [ ] |
| **ServiceNow** (source+sink) | [x] official | [ ] | [ ] | [ ] | [ ] |
| **Datadog** (sink) | [x] official metrics + logs | [x] via DataStax 3rd party | [ ] | [ ] | [ ] |
| **HTTP/Webhook** (source+sink) | [x] community | [x] built-in HTTP sink | [x] http_client + http_server | [x] HTTP Gateway | [ ] |
| **AWS Lambda** (sink) | [x] community | [x] StreamNative | [ ] | [ ] | [ ] |

### 1.10 Monitoring & Observability

| Target System | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **Splunk** (sink) | [x] official | [x] via 3rd party | [x] splunk output | [ ] | [ ] |
| **Datadog** (metrics sink) | [x] official | [x] via 3rd party | [ ] | [ ] | [ ] |
| **Prometheus** (metrics sink) | [x] official | [ ] | [ ] | [ ] | [ ] |
| **OpenTelemetry** (source+sink) | [~] community | [ ] | [x] opentelemetry input+output | [ ] | [ ] |
| **New Relic** (sink) | [~] community | [x] via DataStax 3rd party | [ ] | [ ] | [ ] |

---

## 2. Gap Analysis for Iggy

### 2.1 Critical Gaps (3/4 or 4/4 competitors have it, high use-case relevance)

| Connector | Kafka | Pulsar | Redpanda | NATS | Iggy Status | Use-Case Relevance |
|---|---|---|---|---|---|---|
| **MongoDB** (source+sink) | [x] | [x] | [x] | [x] | MISSING | Very High -- dominant NoSQL DB, IoT/analytics |
| **Redis** (sink+source) | [x] | [x] | [x] | [ ] | MISSING | Very High -- cache, real-time state |
| **Amazon S3** (sink+source) | [x] | [x] | [x] | [~] | MISSING | Very High -- data lake landing zone |
| **MQTT** (source+sink) | [x] | [x] | [x] | [ ] | MISSING | Very High -- IoT protocol, Iggy's core market |
| **RabbitMQ / AMQP** (source+sink) | [x] | [x] | [x] | [ ] | MISSING | High -- migration path from legacy MQ |
| **MySQL** (source+sink) | [x] | [x] | [x] | [~] | PLANNED (JDBC #2500) | High -- most popular RDBMS globally |
| **HTTP/Webhook** (source+sink) | [x] | [x] | [x] | [x] | MISSING | High -- universal integration endpoint |
| **Amazon Kinesis** (source) | [x] | [x] | [x] | [ ] | MISSING | Medium -- cross-cloud streaming bridge |

### 2.2 Important Gaps (3/4 competitors)

| Connector | Kafka | Pulsar | Redpanda | NATS | Iggy Status |
|---|---|---|---|---|---|
| **Snowflake** (sink) | [x] | [x] | [x] | [ ] | MISSING |
| **Google BigQuery** (sink) | [x] | [x] | [x] | [ ] | MISSING |
| **GCS** (sink) | [x] | [x] | [x] | [ ] | MISSING |
| **Azure Blob** (sink) | [x] | [x] | [x] | [ ] | MISSING |
| **Cassandra** (sink) | [x] | [x] | [x] | [ ] | MISSING |
| **Splunk** (sink) | [x] | [x] | [x] | [ ] | MISSING |
| **MS SQL Server** | [x] | [x] | [x] | [ ] | MISSING |
| **DynamoDB** | [x] | [x] | [x] | [ ] | MISSING |

### 2.3 Nice-to-Have (2/4 competitors)

| Connector | Present In | Iggy Relevance |
|---|---|---|
| **OpenTelemetry** | Kafka(~), Redpanda | High -- emerging observability standard |
| **OpenSearch** | Kafka, Redpanda | Medium -- ES fork, AWS-aligned |
| **Datadog** | Kafka, Pulsar | Medium -- observability |
| **Neo4j** | Kafka, Pulsar, Redpanda | Low -- niche graph DB |
| **AWS SQS** | Kafka, Redpanda | Medium |
| **AWS Lambda** | Kafka, Pulsar | Medium -- serverless trigger |

---

## 3. Top 10 Recommended Connectors for Iggy (Beyond Already Planned)

### Rank 1: MQTT Source + Sink
- **Why**: THE IoT protocol. Iggy targets IoT. 3/4 competitors have it. Single highest-impact connector for Iggy's positioning.
- **Complexity**: Medium. Rust crates: `rumqttc`, `paho-mqtt`. Handle QoS, wildcards, sessions.
- **Similar to**: Elasticsearch Source (subscription) + Stdout Sink (simple write)

### Rank 2: MongoDB Source + Sink
- **Why**: Most popular NoSQL. ALL 4 competitors have it. IoT metadata, analytics.
- **Complexity**: Medium-High. `mongodb` Rust driver. CDC via change streams.
- **Similar to**: PostgreSQL Source + Sink (connection pool, batch, CDC)

### Rank 3: Amazon S3 Sink (+ Source)
- **Why**: Universal data lake landing zone. 3/4 have it. Enables Snowflake/Redshift staging.
- **Complexity**: Medium. `aws-sdk-s3` crate. Partitioning, format (JSON/Parquet), batching.
- **Similar to**: Iceberg Sink (already uses S3 under the hood)

### Rank 4: Redis Sink (+ Source)
- **Why**: Most popular cache. Cache warming, real-time state, leaderboards. 3/4 have it.
- **Complexity**: Low-Medium. `redis` Rust crate. Write to streams/hashes/lists.
- **Similar to**: Elasticsearch Sink (~11 entities, schema-less)

### Rank 5: HTTP / Webhook Source + Sink
- **Why**: Universal integration. ALL 4 competitors have it. "Connect Iggy to anything."
- **Complexity**: Low-Medium. `reqwest` (sink) + `axum` (source) already in codebase.
- **Similar to**: Quickwit Sink (HTTP POST pattern, generalized)

### Rank 6: Snowflake Sink
- **Why**: Leading cloud data warehouse. 3/4 have it. Enterprise pipeline destination.
- **Complexity**: High. Snowpipe Streaming or S3 staging. Complex auth.
- **Similar to**: Redshift Sink (#2540, same S3 staging pattern)

### Rank 7: Google BigQuery Sink
- **Why**: #2 cloud DW. 3/4 have it. Completes multi-cloud warehouse story.
- **Complexity**: High. Storage Write API (gRPC), schema management.
- **Similar to**: Iceberg Sink (schema mgmt, batch writes)

### Rank 8: RabbitMQ / AMQP Source + Sink
- **Why**: Most deployed traditional broker. Migration path. 3/4 have it.
- **Complexity**: Medium. `lapin` Rust crate. Consumer acks, prefetch.
- **Similar to**: ES Source + Quickwit Sink (subscribe/push pattern)

### Rank 9: OpenTelemetry Sink (+ Source)
- **Why**: Emerging observability standard. Iggy as telemetry pipeline backbone.
- **Complexity**: Medium-High. OTLP via gRPC (`tonic`) or HTTP/protobuf.
- **Similar to**: Protobuf codec + HTTP sink pattern

### Rank 10: Google Cloud Storage Sink
- **Why**: GCP object storage. 3/4 have it. Thin adapter over S3 sink architecture.
- **Complexity**: Low-Medium. Same as S3 with different storage backend.
- **Similar to**: S3 Sink (once built)

---

## 4. Codec / Format Gaps

| Format | Kafka | Pulsar | Redpanda | NATS | Iggy |
|---|---|---|---|---|---|
| **JSON** | [x] | [x] | [x] | [x] | [x] |
| **Avro** | [x] + Schema Registry | [x] | [x] | [x] | [P] #1846 |
| **Protobuf** | [x] + Schema Registry | [x] | [x] | [x] | [x] |
| **FlatBuffers** | [~] | [ ] | [ ] | [ ] | [x] **unique** |
| **JSON Schema** | [x] + Schema Registry | [x] | [x] | [ ] | [ ] |
| **Raw / Bytes** | [x] | [x] | [x] | [x] | [x] |
| **Text / String** | [x] | [x] | [x] | [x] | [x] |
| **BSON** | [ ] | [ ] | [ ] | [ ] | [P] #1847 |
| **Parquet** (output) | [x] | [x] | [x] | [ ] | [ ] |
| **CSV** | [x] | [ ] | [x] | [ ] | [ ] |

**Critical**: Avro (#1846) -- default Kafka format, interop requirement
**High**: Parquet -- output format for S3/GCS sinks
**Unique advantage**: FlatBuffers -- Iggy is the ONLY platform with native support

---

## 5. Recommended Build Order (all connectors)

**Phase 1 -- IoT + Universal Integration:**
1. MQTT Source + Sink (NEW)
2. HTTP / Webhook Source + Sink (NEW)
3. InfluxDB Sink + Source (PLANNED #2700)
4. Avro Codec (PLANNED #1846)

**Phase 2 -- Data Platform Essentials:**
5. MongoDB Source + Sink (NEW)
6. Amazon S3 Sink (NEW)
7. Redis Sink + Source (NEW)
8. JDBC / MySQL (PLANNED #2500)
9. ClickHouse Sink (PLANNED #2539)

**Phase 3 -- Cloud Data Warehouse:**
10. Snowflake Sink (NEW)
11. Redshift Sink (PLANNED #2540)
12. BigQuery Sink (NEW)
13. Delta Lake (PLANNED #1852)
14. GCS Sink (NEW)

**Phase 4 -- Ecosystem & Observability:**
15. RabbitMQ / AMQP (NEW)
16. OpenTelemetry (NEW)
17. BSON Codec (PLANNED #1847)
18. Parquet output format (NEW)
19. Splunk Sink (NEW)

---

## 6. The IoT Differentiator

Iggy's killer combination that NO competitor matches:

```
MQTT (IoT protocol)
  + InfluxDB (IoT time-series DB)
  + FlatBuffers (zero-copy, unique to Iggy)
  + Protobuf (compact binary)
  + Rust runtime (low memory, edge-deployable)
  = Best-in-class IoT streaming pipeline
```

This should be the primary narrative for Iggy's connector roadmap.

---

## Sources

- [Confluent Cloud Managed Connectors](https://docs.confluent.io/cloud/current/connectors/overview.html)
- [Confluent Hub / Marketplace](https://www.confluent.io/hub/)
- [Apache Pulsar Built-in Connectors](https://pulsar.apache.org/docs/next/io-connectors/)
- [StreamNative Connector Hub](https://docs.streamnative.io/hub)
- [Redpanda Connect Components](https://docs.redpanda.com/redpanda-connect/components/about/)
- [Synadia Platform Connectors](https://www.synadia.com/platform)
- [NATS JetStream Documentation](https://docs.nats.io/nats-concepts/jetstream)
