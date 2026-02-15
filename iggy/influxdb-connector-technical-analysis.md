# InfluxDB Connector for Apache Iggy: Technical Analysis

## Table of Contents

1. [InfluxDB Data Model](#1-influxdb-data-model)
2. [InfluxDB Client Libraries (Rust)](#2-influxdb-client-libraries-rust)
3. [InfluxDB Write Path](#3-influxdb-write-path)
4. [InfluxDB Read/Query Path (Source Connector)](#4-influxdb-readquery-path-source-connector)
5. [How Other Streaming Platforms Connect to InfluxDB](#5-how-other-streaming-platforms-connect-to-influxdb)
6. [Key Design Decisions for an Iggy InfluxDB Connector](#6-key-design-decisions-for-an-iggy-influxdb-connector)
7. [InfluxDB Versions and Compatibility](#7-influxdb-versions-and-compatibility)

---

## 1. InfluxDB Data Model

### 1.1 Core Concepts: Measurements, Tags, Fields, Timestamps

InfluxDB uses a time-series data model with four core components:

| Component | Required | Indexed | Description |
|-----------|----------|---------|-------------|
| **Measurement** | Yes | Yes | A namespace/table name for related data (analogous to a SQL table name). Case-sensitive. Cannot begin with `_`. |
| **Tags** | No | Yes | Key-value string pairs that act as indexed metadata. Used for fast filtering/grouping. Think of them as indexed columns. |
| **Fields** | Yes (at least one) | No | Key-value pairs containing the actual data. Values can be float, integer, unsigned integer, string, or boolean. Not indexed. |
| **Timestamp** | No (auto-assigned) | Yes | Unix timestamp associated with the data point. Supports nanosecond to second precision. |

**Key design principles:**
- Tags are **indexed**; fields are **not**. Querying by tag is fast; querying by field requires a full scan.
- A **series** is the unique combination of measurement + tag set. This is the fundamental unit of identity.
- A **point** is uniquely identified by measurement + tag set + timestamp. Writing a point with the same identity merges field sets (last-write-wins for conflicts).
- **Cardinality** = number of unique series. High cardinality (e.g., using UUIDs as tag values) degrades performance. Use fields for high-cardinality identifiers.

### 1.2 Line Protocol Format

The wire protocol for writing data to InfluxDB is the **line protocol**, a text-based format:

```
<measurement>[,<tag_key>=<tag_value>[,...]] <field_key>=<field_value>[,...] [<timestamp>]
```

**Examples:**

```
# Single point
cpu,host=server01,region=us-west usage_idle=98.3,usage_user=1.2 1630525358000000000

# Multiple points (newline-separated)
temperature,location=office,sensor=dht22 value=23.5 1630525358000000000
temperature,location=warehouse,sensor=bme280 value=18.2,humidity=45.3 1630525358000000000

# String field values (double-quoted)
events,source=app message="User logged in",level="info" 1630525358000000000

# Integer fields (trailing i), unsigned (trailing u), boolean
metrics,host=db01 connections=142i,healthy=true,bytes_sent=98234u 1630525358000000000
```

**Field value data types:**

| Type | Syntax | Example |
|------|--------|---------|
| Float (64-bit IEEE-754) | Plain number or with decimal | `value=1.0` or `value=1` |
| Integer (64-bit signed) | Trailing `i` | `value=1i` |
| Unsigned Integer (64-bit) | Trailing `u` | `value=1u` |
| String | Double-quoted | `value="hello"` |
| Boolean | `t`/`T`/`true`/`True`/`TRUE` (or `f`/`F`/`false`/`False`/`FALSE`) | `value=true` |

**Whitespace rules:**
- First unescaped space separates measurement+tags from field set.
- Second unescaped space separates field set from timestamp.
- Commas separate tags within the tag set and fields within the field set.
- No spaces around `=` signs.
- Tag keys, tag values, and field keys: escape spaces, commas, and equals signs with `\`.
- Newline `\n` is not supported in tag or field values.
- Lines beginning with `#` are comments.

### 1.3 Buckets and Organizations (InfluxDB 2.x/3.x)

**InfluxDB 2.x** replaced the 1.x concepts of "databases" and "retention policies" with a simplified hierarchy:

```
Organization
  └── Bucket (= database + retention policy)
        └── Measurement
              └── Series (measurement + unique tag set)
                    └── Points (field values at timestamps)
```

- **Organization**: Top-level grouping entity. All resources belong to an organization.
- **Bucket**: Named location where time-series data is stored. Each bucket has:
  - A unique name (within an organization)
  - A retention period
  - An associated organization

**InfluxDB 3.x** further simplifies:
- Uses **databases** (similar to buckets) and **tables** (similar to measurements).
- The v2-compatible API still accepts bucket/org parameters.
- The v3-native API uses database/table terminology.

### 1.4 Retention Policies

**InfluxDB 2.x:**
- Retention is configured per-bucket at creation time.
- Can be infinite (data never expires) or as short as 1 hour.
- InfluxDB deletes data in **shard groups**, not individual points. A shard group is deleted only when its entire time range exceeds the retention period.
- Retention enforcement runs every 30 minutes by default (configurable via `storage-retention-check-interval`).
- DBRP (Database and Retention Policy) mappings exist for backward compatibility with InfluxDB 1.x.

**InfluxDB 3.x:**
- Retention periods are configurable per-database.
- Data is stored as Parquet files on object storage with configurable lifecycle management.

---

## 2. InfluxDB Client Libraries (Rust)

### 2.1 Available Rust Crates

| Crate | Version | Target | Maintainer | Status |
|-------|---------|--------|------------|--------|
| [`influxdb`](https://crates.io/crates/influxdb) | 0.7.2 | InfluxDB 1.x (2.x compat mode) | Community (influxdb-rs) | Active, most mature |
| [`influxdb2`](https://crates.io/crates/influxdb2) | ~0.4 | InfluxDB 2.x native API | aprimadi (fork of IOx client) | Alpha |
| [`influxdb3`](https://crates.io/crates/influxdb3) | 0.1.0 | InfluxDB 3.x | Romain S. (community) | Very new (Dec 2025) |
| [`influxdb_rs`](https://crates.io/crates/influxdb_rs) | varies | InfluxDB 2.x API | Community | Available |
| [`influx-client`](https://crates.io/crates/influx-client) | early | InfluxDB general | Community | Early stage |
| [`influxdb-line-protocol`](https://crates.io/crates/influxdb-line-protocol) | varies | Line protocol parser only | InfluxData (from IOx) | Part of InfluxDB codebase |
| `influxdb3_client` | internal | InfluxDB 3.x | InfluxData | Internal crate in influxdata/influxdb repo |

### 2.2 Detailed Assessment

#### `influxdb` (v0.7.2) -- Most Mature Community Crate

**Repository:** [github.com/influxdb-rs/influxdb-rust](https://github.com/influxdb-rs/influxdb-rust)

**Features:**
- Read and write to InfluxDB
- Optional Serde support for deserialization
- Multiple queries in one request
- Single or multiple measurements in one write
- `#[derive(InfluxDbWriteable)]` derive macro
- GROUP BY support
- Async/await with Tokio and async-std
- Swappable HTTP backends (reqwest default, or surf for async-std)
- TLS via `rustls` (default), native-tls, or vendored native-tls

**Limitation:** Can only interact with InfluxDB 2.0 in "compatibility mode" -- does not natively support the v2 token/org/bucket API.

**Usage example:**
```rust
use influxdb::{Client, Query, Timestamp, ReadQuery};

let client = Client::new("http://localhost:8086", "my_database")
    .with_auth("username", "password");

// Write
let write_query = Query::write_query(Timestamp::Seconds(1630525358), "cpu")
    .add_field("usage_idle", 98.3)
    .add_tag("host", "server01");
client.query(write_query).await?;

// Read
let read_query = ReadQuery::new("SELECT * FROM cpu WHERE host = 'server01'");
let result = client.query(read_query).await?;
```

#### `influxdb2` -- InfluxDB 2.x Native Client

**Repository:** [github.com/aprimadi/influxdb2](https://github.com/aprimadi/influxdb2)

**Features:**
- Native InfluxDB 2.0 API (token auth, org/bucket)
- Fork from the official `influxdb_iox/influxdb2_client`
- Uses reqwest under the hood
- Choose between native-tls and rustls

**Note:** Alpha status. Originally forked because the query functionality in the official IOx client was not working.

#### `influxdb3` (v0.1.0) -- InfluxDB 3 Client

**crates.io:** [crates.io/crates/influxdb3](https://crates.io/crates/influxdb3)
**docs.rs:** [docs.rs/influxdb3](https://docs.rs/influxdb3/latest/influxdb3/)

Very new (published December 2025). Expected API surface (based on the InfluxDB 3 client library pattern across languages):
- Write via line protocol (HTTP `/api/v2/write` or v3 `/api/v3/write_lp`)
- Query via SQL (Apache Arrow Flight or HTTP `/api/v3/query_sql`)
- Query via InfluxQL
- Uses `reqwest` for HTTP and `arrow-flight` for Flight queries

#### `influxdb3_client` -- Internal InfluxDB Crate

Located in the [influxdata/influxdb](https://github.com/influxdata/influxdb) repository under `influxdb3_client/`. This is the client used internally by the `influxdb3` CLI binary. It provides:
- `write_line_protocol()` -- write data in line protocol format
- `api_v3_query_sql()` -- query with SQL via the v3 API
- `api_v3_query_influxql()` -- query with InfluxQL
- Health check endpoints

#### `influxdb-line-protocol` -- Parser Crate

A pure Rust line protocol parser from the InfluxDB IOx project. Useful if building a connector that needs to parse or generate line protocol without the full client overhead.

### 2.3 Does InfluxDB Have an Official Rust Client?

**No official standalone Rust client library exists.** InfluxData maintains official v3 client libraries for Python, Go, Java, JavaScript/TypeScript, and C#, but Rust is not among them. The closest official Rust code is:
- `influxdb3_client` -- internal crate in the main InfluxDB repo (not published separately on crates.io)
- `influxdb-line-protocol` -- parser crate from the IOx project

### 2.4 Recommendation for the Iggy Connector

**For InfluxDB 2.x support:** Use `reqwest` directly against the HTTP API. The community crates are either alpha-quality or target InfluxDB 1.x. The v2 HTTP API is simple enough that a thin wrapper is more reliable than depending on an under-maintained community crate.

**For InfluxDB 3.x support:** Monitor the `influxdb3` crate. If it matures, adopt it. Otherwise, use `reqwest` for writes (line protocol over HTTP) and `arrow-flight` for queries (SQL over Flight).

**For line protocol generation:** Consider using the `influxdb-line-protocol` crate for parsing, or implement a simple line protocol serializer (it is a straightforward text format).

---

## 3. InfluxDB Write Path

### 3.1 HTTP API Endpoint

**InfluxDB 2.x endpoint:**
```
POST /api/v2/write?org={org}&bucket={bucket}&precision={precision}
```

**InfluxDB 3.x v2-compatible endpoint (same as above):**
```
POST /api/v2/write?org={org}&bucket={bucket}&precision={precision}
```

**InfluxDB 3.x native v3 endpoint:**
```
POST /api/v3/write_lp?db={database}&precision={precision}
```

### 3.2 Request Format

**Required headers:**
```http
POST /api/v2/write?org=my-org&bucket=my-bucket&precision=ns HTTP/1.1
Host: localhost:8086
Authorization: Token <INFLUX_API_TOKEN>
Content-Type: text/plain; charset=utf-8
Accept: application/json
```

**Optional compression header:**
```http
Content-Encoding: gzip
```

**Query parameters:**

| Parameter | Required | Default | Values |
|-----------|----------|---------|--------|
| `org` | Yes (v2) | -- | Organization name or ID |
| `bucket` | Yes (v2) | -- | Bucket name |
| `db` | Yes (v3) | -- | Database name (v3 endpoint) |
| `precision` | No | `ns` | `ns` (nanosecond), `us` (microsecond), `ms` (millisecond), `s` (second) |

**Request body:** Line protocol, one point per line, newline (`\n`) separated.

**Complete curl example:**
```bash
curl --request POST \
  "http://localhost:8086/api/v2/write?org=my-org&bucket=my-bucket&precision=s" \
  --header "Authorization: Token ${INFLUX_TOKEN}" \
  --header "Content-Type: text/plain; charset=utf-8" \
  --header "Accept: application/json" \
  --data-binary '
cpu,host=server01,region=us-west usage_idle=98.3,usage_user=1.2 1630525358
cpu,host=server02,region=us-east usage_idle=72.1,usage_user=15.4 1630525358
memory,host=server01 used_percent=64.2,available=8192i 1630525358
'
```

### 3.3 Batch Write Best Practices

| Deployment | Recommended Batch Size | Max Payload |
|------------|----------------------|-------------|
| InfluxDB OSS 2.x | **5,000 lines** per request | No strict limit (practical: ~5-10 MB) |
| InfluxDB Cloud (TSM) | **5,000 lines** per request | 50 MB (usage-based), 5 MB (free plan) |
| InfluxDB 3 Cloud Dedicated | **10,000 lines** or 10 MB (whichever first) | Varies |
| InfluxDB 3 Enterprise | **10,000 lines** or 10 MB (whichever first) | Varies |

**Additional optimization techniques:**

1. **Sort tags by key lexicographically** before writing. InfluxDB can process pre-sorted tags more efficiently.
   ```
   # Good (sorted)
   cpu,host=server01,region=us-west usage=98.3
   # Bad (unsorted)
   cpu,region=us-west,host=server01 usage=98.3
   ```

2. **Use the coarsest timestamp precision possible.** If millisecond precision is sufficient, use `precision=ms` rather than `precision=ns`. This improves compression.

3. **Enable gzip compression.** Set `Content-Encoding: gzip` for up to 5x speed improvement on write payloads.

4. **Write sequentially (order matters).** Wait for the response before sending the next batch if ordering guarantees are needed.

5. **InfluxDB 3 column ordering.** The first write to a table determines the physical column order in storage. Place most-queried tags first.

### 3.4 Error Handling

**HTTP Response Codes:**

| Code | Meaning | Retriable? | Action |
|------|---------|------------|--------|
| `204 No Content` | Success (v2) | -- | Data written |
| `200 OK` | Success (v3) | -- | Data written |
| `400 Bad Request` | Malformed line protocol | **No** | Fix the data. Response body contains the first malformed line. Entire batch rejected. |
| `401 Unauthorized` | Invalid/missing token | **No** | Check authentication |
| `404 Not Found` | Bucket/org not found | **No** | Check configuration |
| `413 Request Entity Too Large` | Payload too large | **No** | Reduce batch size |
| `422 Unprocessable Entity` | Schema conflict (e.g., field type mismatch) | **No** | Fix the data schema. Some points may have been rejected. |
| `429 Too Many Requests` | Rate limited (Cloud) | **Yes** | Back off and retry. Check `Retry-After` header. |
| `500 Internal Server Error` | Server error | **Yes** | Retry with exponential backoff |
| `503 Service Unavailable` | Server overloaded | **Yes** | Retry after `Retry-After` header duration |

**Error response format (JSON):**
```json
{
  "code": "invalid",
  "message": "failed to parse line protocol: errors encountered on line(s): ..."
}
```

**Critical considerations for the connector:**
- **400/422 errors are non-retriable.** The data itself is malformed or conflicts with the schema. Log these, send to a dead-letter queue, and continue.
- **5xx and 429 errors are retriable.** Use exponential backoff with jitter.
- **Partial writes:** In InfluxDB 2.x, a `400` rejects the entire batch. There is no partial write on `400`. However, `422` can indicate partial rejection (some points accepted, others rejected due to schema conflicts). In InfluxDB Cloud (TSM), data might not yet be queryable when you receive `204` -- it is async.
- **Idempotency:** Writing the same point (same measurement + tags + timestamp) with the same field values is idempotent. InfluxDB merges duplicate points, with the last write winning for conflicting fields.

### 3.5 Precision Options

| Value | Precision | Timestamp Example | Use Case |
|-------|-----------|-------------------|----------|
| `ns` | Nanosecond | `1630525358000000000` | Default. High-precision telemetry. |
| `us` | Microsecond | `1630525358000000` | Network/application metrics. |
| `ms` | Millisecond | `1630525358000` | Most common for IoT, web metrics. |
| `s` | Second | `1630525358` | Low-frequency data, daily aggregates. |

**Recommendation:** Use `ms` (millisecond) as the default for the Iggy connector unless the user needs higher precision. It offers good compression and is sufficient for most streaming use cases.

---

## 4. InfluxDB Read/Query Path (Source Connector)

### 4.1 Query Language Support by Version

| Language | InfluxDB 1.x | InfluxDB 2.x | InfluxDB 3.x |
|----------|-------------|-------------|-------------|
| **InfluxQL** | Primary | Supported (via DBRP mapping) | Supported |
| **Flux** | Not available | Primary | **Deprecated / Removed** |
| **SQL** | Not available | Not available | **Primary** (DataFusion) |

### 4.2 Flux Query Language (InfluxDB 2.x)

Flux is a functional data scripting language with pipe-forward (`|>`) syntax:

```flux
from(bucket: "my-bucket")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> filter(fn: (r) => r._field == "usage_idle")
  |> filter(fn: (r) => r.host == "server01")
  |> aggregateWindow(every: 5m, fn: mean)
  |> yield(name: "mean")
```

**API endpoint:**
```
POST /api/v2/query?org={org}
Content-Type: application/vnd.flux
Authorization: Token <token>

from(bucket: "my-bucket") |> range(start: -1h) |> ...
```

**Response format:** Annotated CSV (default) or JSON.

**Relevance to the connector:** Flux is in **maintenance mode** as of 2023 and has been **removed from InfluxDB 3.x**. If targeting 2.x, Flux is the primary query language. If targeting 3.x, use SQL.

### 4.3 InfluxQL (SQL-like)

InfluxQL is a SQL-like language designed for time-series data:

```sql
SELECT mean("usage_idle") FROM "cpu"
WHERE "host" = 'server01' AND time > now() - 1h
GROUP BY time(5m), "host"
```

**Key limitations:**
- No JOIN support
- No DatePart-like queries
- Strong at schema exploration (`SHOW MEASUREMENTS`, `SHOW TAG KEYS`, `SHOW FIELD KEYS`)

**Supported in both InfluxDB 2.x (via DBRP mapping) and 3.x.**

### 4.4 SQL in InfluxDB 3.x (DataFusion)

InfluxDB 3.x uses Apache DataFusion for SQL support:

```sql
SELECT
  time,
  host,
  usage_idle,
  usage_user
FROM cpu
WHERE host = 'server01'
  AND time >= now() - INTERVAL '1 hour'
ORDER BY time DESC
LIMIT 100
```

**API endpoint (v3):**
```
POST /api/v3/query_sql
Content-Type: application/json
Authorization: Token <token>

{
  "db": "my-database",
  "q": "SELECT * FROM cpu WHERE time > now() - INTERVAL '1 hour'",
  "format": "json"
}
```

**Query via Apache Arrow Flight (preferred for performance):**
```rust
// Pseudocode for Arrow Flight query
let flight_client = FlightClient::connect("http://localhost:8086").await?;
let ticket = Ticket::new(json!({
    "database": "my-database",
    "sql_query": "SELECT * FROM cpu WHERE time > now() - INTERVAL '1 hour'"
}).to_string());
let stream = flight_client.do_get(ticket).await?;
// Process RecordBatch stream
```

**Output formats:** JSON, CSV, Parquet, Arrow IPC (via Flight).

### 4.5 Streaming/Subscription APIs

**InfluxDB does NOT have a native push/subscription API for streaming new data in real-time.**

| Feature | InfluxDB 1.x | InfluxDB 2.x | InfluxDB 3.x |
|---------|-------------|-------------|-------------|
| Subscriptions (push to endpoint) | Yes | **Removed** | No |
| Continuous Queries | Yes | Tasks (scheduled Flux) | Processing Engine (Python) |
| Change Data Capture | No | No | No |
| WebSocket streaming | No | No | No |
| HTTP long-polling | No | No | No |

**This is a critical design constraint for a Source connector.** There is no way to "subscribe" to new data in InfluxDB 2.x or 3.x. The connector must use a **polling strategy**.

### 4.6 Polling Strategies for Source Connector

Since InfluxDB lacks a streaming API, the source connector must poll for new data. Recommended approach:

**Strategy: Time-Range Polling with High-Water Mark**

```
┌─────────────────────────────────────────────────────────┐
│  Source Connector Polling Loop                          │
│                                                         │
│  1. Load last_timestamp (high-water mark) from state    │
│  2. Query: SELECT * FROM measurement                    │
│     WHERE time > last_timestamp                         │
│     AND time <= now() - buffer_duration                  │
│     ORDER BY time ASC                                   │
│     LIMIT page_size                                     │
│  3. For each row: serialize to Iggy message, send       │
│  4. Update last_timestamp to max(row.time)              │
│  5. Persist last_timestamp to durable state             │
│  6. Sleep for poll_interval                             │
│  7. Repeat from step 1                                  │
└─────────────────────────────────────────────────────────┘
```

**Key considerations:**
- **Buffer duration (step 2):** Subtract a small buffer (e.g., 5-10 seconds) from `now()` to avoid reading data that might still be in-flight or not yet flushed to queryable storage. InfluxDB Cloud (TSM) writes are async -- data may not be queryable immediately after `204`.
- **Pagination:** Use `LIMIT` and `OFFSET` or cursor-based pagination via the time column to handle large result sets.
- **Deduplication:** Since points are identified by measurement + tags + timestamp, polling the same time range again should return the same results (unless fields were updated). The connector should track the exact high-water mark to avoid reprocessing.
- **Multiple measurements:** The connector should support configuring which measurements to poll, potentially running parallel queries.

---

## 5. How Other Streaming Platforms Connect to InfluxDB

### 5.1 Kafka InfluxDB Sink Connector (Confluent)

The [Confluent InfluxDB Sink Connector](https://docs.confluent.io/kafka-connectors/influxdb/current/influx-db-sink-connector/overview.html) is a mature, production-grade connector built on Kafka Connect.

**Architecture:**
- Built on the Kafka Connect framework (Java).
- Available as self-managed (Confluent Platform) and fully-managed (Confluent Cloud).
- Supports InfluxDB 1.x, 2.x, and 3.x (separate connector versions for 2 and 3).

**Data mapping model:**

```
Kafka Record
├── measurement (String field, required unless measurement.name.format is set)
├── tags (Map<String, String> field, optional)
├── <field1> (Float/Integer/String/Boolean) -- at least one required
├── <field2> ...
└── timestamp (from record header, or event.time.fieldname)
```

**Key configuration properties:**

| Property | Description |
|----------|-------------|
| `influxdb.url` | InfluxDB host URL |
| `influxdb.db` | Target database/bucket name |
| `measurement.name.format` | Format string for measurement name (supports `${topic}` placeholder) |
| `event.time.fieldname` | Field name containing event timestamp (default: Kafka record timestamp) |
| `influxdb.gzip.enable` | Enable gzip compression |
| `max.retries` | Maximum retry attempts on error |
| `retry.backoff.ms` | Backoff duration between retries |

**Batching behavior:**
- Records with the same measurement, time, and tags within a batch are **merged** (combined into a single point).
- At-least-once delivery guarantee.
- Dead Letter Queue (DLQ) support for failed records.

**Schema support:** AVRO, PROTOBUF, JSON_SR (JSON Schema), and schemaless JSON.

**Lessons for the Iggy connector:**
1. Support both "measurement from record field" and "measurement from topic name" approaches.
2. Tags should be extractable from a nested map/object in the message.
3. Timestamp should default to the message timestamp but be overridable from a field.
4. Implement DLQ/dead-letter topic for records that fail to write.
5. Merge duplicate points within a batch before writing.

### 5.2 Telegraf -- InfluxData's Agent

[Telegraf](https://github.com/influxdata/telegraf) is InfluxData's official plugin-driven agent (written in Go) for collecting, processing, and writing metrics.

**Plugin architecture:**

```
Input Plugins  -->  Processor Plugins  -->  Aggregator Plugins  -->  Output Plugins
  (collect)          (transform)             (aggregate)              (write)
```

**Four plugin types:**
1. **Input Plugins** (~300+): Collect metrics from systems, services, APIs. Two subtypes:
   - **Regular**: Executed at each collection interval (poll-based).
   - **Service**: Run as a background service (event-based, e.g., listening on a socket).
2. **Processor Plugins**: Transform, enrich, and filter metrics (e.g., rename, regex, dedup).
3. **Aggregator Plugins**: Create aggregate metrics (mean, min, max, quantiles, histograms).
4. **Output Plugins**: Write metrics to destinations (InfluxDB, Kafka, Prometheus, etc.).

**Internal data model:** Telegraf uses InfluxDB's data model internally (measurement, tags, fields, timestamp). Input plugins use an `Accumulator` interface to add measurements.

**InfluxDB v2 output plugin configuration:**
```toml
[[outputs.influxdb_v2]]
  urls = ["http://localhost:8086"]
  token = "$INFLUX_TOKEN"
  organization = "my-org"
  bucket = "my-bucket"
  # Gzip compression is enabled by default
  content_encoding = "gzip"
```

**Relevance to the Iggy connector:**
- Telegraf's plugin model (Input -> Process -> Aggregate -> Output) is similar to a connector pipeline.
- Telegraf's Kafka consumer input + InfluxDB output is a common alternative to a direct Kafka-InfluxDB connector.
- The Telegraf `tail` input plugin demonstrates a "file tailing" pattern that is analogous to a streaming source.
- **Iggy could be added as a Telegraf input/output plugin** in Go, separate from the native Rust connector.

### 5.3 Existing Rust-Based InfluxDB Connectors

**There are no existing open-source Rust-based streaming-platform-to-InfluxDB connectors.** The Rust ecosystem for InfluxDB is limited to client libraries. The Iggy connector would be the first known Rust-based streaming connector for InfluxDB.

Relevant related projects:
- [questdb/c-questdb-client](https://github.com/questdb/c-questdb-client) -- Rust/C/C++ client for QuestDB using InfluxDB Line Protocol (demonstrates line protocol generation in Rust for a compatible TSDB).
- [influxdata/rskafka](https://github.com/influxdata/rskafka) -- InfluxData's minimal Rust Kafka client (demonstrates InfluxData's investment in Rust for streaming).

---

## 6. Key Design Decisions for an Iggy InfluxDB Connector

### 6.1 Sink Connector: Mapping Iggy Messages to InfluxDB Line Protocol

**Message format assumption:** Iggy messages are likely JSON (or can be deserialized to a structured format). The sink connector needs a configurable mapping.

**Proposed mapping configuration:**

```toml
[sink.influxdb]
# Connection
url = "http://localhost:8086"
token = "${INFLUX_TOKEN}"
org = "my-org"
bucket = "my-bucket"
precision = "ms"

# Mapping
measurement_from = "field"        # "field" or "topic" or "static"
measurement_field = "measurement" # JSON field name (when measurement_from = "field")
measurement_name = "my_metric"    # Static name (when measurement_from = "static")

# Tag extraction
tag_fields = ["host", "region", "sensor_id"]  # JSON fields to extract as tags
# OR
tag_map_field = "tags"            # JSON field containing a map of tags

# Field extraction
field_strategy = "remaining"       # "remaining" (all non-tag/non-measurement fields)
                                   # or "explicit" (only listed fields)
field_names = ["value", "count"]   # When field_strategy = "explicit"

# Timestamp
timestamp_from = "field"           # "field" or "iggy_timestamp"
timestamp_field = "timestamp"      # JSON field name
timestamp_format = "epoch_ms"      # "epoch_ns", "epoch_us", "epoch_ms", "epoch_s", "rfc3339"

# Batching
batch_size = 5000
flush_interval_ms = 1000
max_batch_bytes = 5_000_000        # 5 MB

# Error handling
max_retries = 3
retry_backoff_ms = 1000
retry_backoff_multiplier = 2.0
dead_letter_topic = "influxdb-dlq"

# Compression
gzip = true
```

**Example transformation:**

```json
// Iggy message (JSON payload)
{
  "measurement": "temperature",
  "host": "sensor-01",
  "location": "warehouse-A",
  "value": 23.5,
  "humidity": 67.2,
  "timestamp": 1630525358000
}
```

Transforms to line protocol:
```
temperature,host=sensor-01,location=warehouse-A value=23.5,humidity=67.2 1630525358000
```

**Implementation sketch (Rust):**

```rust
use serde_json::Value;
use std::fmt::Write;

pub struct LineProtocolBuilder {
    measurement_from: MeasurementSource,
    tag_fields: Vec<String>,
    timestamp_field: Option<String>,
    precision: Precision,
}

impl LineProtocolBuilder {
    pub fn build_line(&self, json: &Value) -> Result<String, ConversionError> {
        let mut line = String::with_capacity(256);

        // 1. Measurement name
        let measurement = self.extract_measurement(json)?;
        write_escaped_measurement(&mut line, &measurement);

        // 2. Tags (sorted lexicographically by key)
        let mut tags: Vec<(&str, &str)> = Vec::new();
        for tag_key in &self.tag_fields {
            if let Some(val) = json.get(tag_key).and_then(|v| v.as_str()) {
                tags.push((tag_key.as_str(), val));
            }
        }
        tags.sort_by_key(|(k, _)| *k);
        for (key, value) in &tags {
            write!(line, ",{}={}", escape_tag_key(key), escape_tag_value(value))?;
        }

        line.push(' ');

        // 3. Fields (all remaining non-tag, non-measurement, non-timestamp fields)
        let mut first_field = true;
        if let Some(obj) = json.as_object() {
            for (key, value) in obj {
                if self.is_reserved_field(key) { continue; }
                if !first_field { line.push(','); }
                write_field(&mut line, key, value)?;
                first_field = false;
            }
        }
        if first_field {
            return Err(ConversionError::NoFields);
        }

        // 4. Timestamp
        if let Some(ts) = self.extract_timestamp(json)? {
            write!(line, " {}", ts)?;
        }

        Ok(line)
    }
}
```

### 6.2 Source Connector: Polling Strategy

**Recommended approach: Time-Range Polling with Persistent High-Water Mark**

```rust
pub struct InfluxDbSource {
    client: reqwest::Client,
    config: SourceConfig,
    /// Last timestamp successfully processed (persisted to Iggy consumer state)
    high_water_mark: i64,
}

impl InfluxDbSource {
    pub async fn poll(&mut self) -> Result<Vec<IggyMessage>, SourceError> {
        // Buffer: don't query too close to "now" to avoid reading in-flight data
        let upper_bound = now_epoch_ns() - self.config.buffer_duration_ns;

        let query = format!(
            "SELECT * FROM \"{}\" WHERE time > {} AND time <= {} ORDER BY time ASC LIMIT {}",
            self.config.measurement,
            self.high_water_mark,
            upper_bound,
            self.config.page_size
        );

        let results = self.execute_query(&query).await?;
        let mut messages = Vec::with_capacity(results.len());

        for row in &results {
            let message = self.row_to_iggy_message(row)?;
            messages.push(message);
        }

        if let Some(last_row) = results.last() {
            self.high_water_mark = last_row.timestamp;
            self.persist_watermark(self.high_water_mark).await?;
        }

        Ok(messages)
    }
}
```

**Configuration for source connector:**

```toml
[source.influxdb]
url = "http://localhost:8086"
token = "${INFLUX_TOKEN}"
org = "my-org"
bucket = "my-bucket"

# Query configuration
measurement = "temperature"
query_language = "sql"           # "sql" (v3), "influxql" (v2/v3), "flux" (v2 only)
custom_query = ""                # Override with custom query (optional)
poll_interval_ms = 5000          # How often to poll
buffer_duration_s = 10           # Lag behind "now" to avoid reading in-flight data
page_size = 1000                 # Max rows per poll

# Output format
output_format = "json"           # "json" or "line_protocol"

# State management
watermark_persist_interval_ms = 10000
```

### 6.3 HTTP API Directly vs. Client Library

**Recommendation: Use `reqwest` directly for the HTTP API.**

Rationale:
1. **No mature, official Rust client library exists.** The community crates are alpha-quality or target outdated versions.
2. **The InfluxDB HTTP API is simple.** Writing is a POST with line protocol in the body. Querying is a POST with a query string. This does not justify a heavy dependency.
3. **Full control over connection pooling, retries, and error handling.** A connector needs precise control over these concerns.
4. **Reduced dependency risk.** Community crates may become unmaintained.

**Suggested architecture:**

```rust
pub struct InfluxDbClient {
    http_client: reqwest::Client,  // Connection pool managed by reqwest/hyper
    base_url: String,
    token: String,
    org: String,
    bucket: String,
    precision: Precision,
    gzip: bool,
}

impl InfluxDbClient {
    /// Write line protocol data to InfluxDB
    pub async fn write(&self, line_protocol: &str) -> Result<(), WriteError> {
        let url = format!(
            "{}/api/v2/write?org={}&bucket={}&precision={}",
            self.base_url,
            urlencoding::encode(&self.org),
            urlencoding::encode(&self.bucket),
            self.precision.as_str()
        );

        let body = if self.gzip {
            compress_gzip(line_protocol.as_bytes())?
        } else {
            line_protocol.as_bytes().to_vec()
        };

        let mut request = self.http_client
            .post(&url)
            .header("Authorization", format!("Token {}", self.token))
            .header("Content-Type", "text/plain; charset=utf-8")
            .header("Accept", "application/json");

        if self.gzip {
            request = request.header("Content-Encoding", "gzip");
        }

        let response = request.body(body).send().await?;

        match response.status().as_u16() {
            204 | 200 => Ok(()),
            429 => {
                let retry_after = response.headers()
                    .get("Retry-After")
                    .and_then(|v| v.to_str().ok())
                    .and_then(|v| v.parse::<u64>().ok());
                Err(WriteError::RateLimited { retry_after_secs: retry_after })
            },
            400 => {
                let body = response.text().await?;
                Err(WriteError::BadRequest(body))
            },
            401 => Err(WriteError::Unauthorized),
            422 => {
                let body = response.text().await?;
                Err(WriteError::UnprocessableEntity(body))
            },
            status if status >= 500 => {
                Err(WriteError::ServerError(status))
            },
            status => {
                Err(WriteError::Unexpected(status))
            },
        }
    }

    /// Health check
    pub async fn health(&self) -> Result<bool, reqwest::Error> {
        let url = format!("{}/health", self.base_url);
        let response = self.http_client.get(&url).send().await?;
        Ok(response.status().is_success())
    }

    /// Query with SQL (InfluxDB 3.x)
    pub async fn query_sql(&self, sql: &str, database: &str) -> Result<String, QueryError> {
        let url = format!("{}/api/v3/query_sql", self.base_url);
        let response = self.http_client
            .post(&url)
            .header("Authorization", format!("Token {}", self.token))
            .json(&serde_json::json!({
                "db": database,
                "q": sql,
                "format": "json"
            }))
            .send()
            .await?;
        // ... handle response
        todo!()
    }
}
```

### 6.4 Connection Management

**reqwest provides built-in connection pooling via hyper.** Default configuration is reasonable:
- Idle connections are pooled per host.
- Default pool idle timeout: 90 seconds.
- TLS connections are reused.

**Recommended `reqwest::Client` configuration for the connector:**

```rust
let client = reqwest::Client::builder()
    .pool_max_idle_per_host(10)         // Connection pool size
    .pool_idle_timeout(Duration::from_secs(90))
    .timeout(Duration::from_secs(30))    // Per-request timeout
    .connect_timeout(Duration::from_secs(10))
    .tcp_keepalive(Duration::from_secs(60))
    .gzip(false)                         // We handle gzip manually for writes
    .build()?;
```

### 6.5 Error Categories

| Category | HTTP Codes | Retriable | Strategy |
|----------|-----------|-----------|----------|
| **Malformed data** | 400 | No | Log error, send to DLQ, skip batch |
| **Authentication failure** | 401 | No | Log, halt connector, alert operator |
| **Resource not found** | 404 | No | Log, halt connector (bucket/org misconfigured) |
| **Schema conflict** | 422 | No | Log, send to DLQ. May be partial. |
| **Payload too large** | 413 | No | Reduce batch size, retry with smaller batches |
| **Rate limited** | 429 | Yes | Backoff per `Retry-After` header |
| **Server error** | 500 | Yes | Exponential backoff with jitter |
| **Service unavailable** | 503 | Yes | Backoff per `Retry-After` header |
| **Network error** | (connection refused, timeout) | Yes | Exponential backoff with jitter |

**Retry implementation:**

```rust
pub async fn write_with_retry(
    client: &InfluxDbClient,
    line_protocol: &str,
    config: &RetryConfig,
) -> Result<(), WriteError> {
    let mut attempt = 0;
    let mut backoff = config.initial_backoff;

    loop {
        match client.write(line_protocol).await {
            Ok(()) => return Ok(()),
            Err(WriteError::RateLimited { retry_after_secs }) => {
                if attempt >= config.max_retries {
                    return Err(WriteError::MaxRetriesExceeded);
                }
                let delay = retry_after_secs
                    .map(Duration::from_secs)
                    .unwrap_or(backoff);
                tokio::time::sleep(delay).await;
                attempt += 1;
            },
            Err(WriteError::ServerError(_)) | Err(WriteError::NetworkError(_)) => {
                if attempt >= config.max_retries {
                    return Err(WriteError::MaxRetriesExceeded);
                }
                let jitter = rand::thread_rng().gen_range(0..backoff.as_millis() / 4);
                tokio::time::sleep(backoff + Duration::from_millis(jitter as u64)).await;
                backoff = std::cmp::min(backoff * 2, config.max_backoff);
                attempt += 1;
            },
            Err(e) => return Err(e), // Non-retriable
        }
    }
}
```

---

## 7. InfluxDB Versions and Compatibility

### 7.1 Version Landscape

| Version | Status | Engine | Query Languages | License | Write API |
|---------|--------|--------|-----------------|---------|-----------|
| **InfluxDB OSS 2.x** | Stable, widely deployed | TSM (Go) | Flux (primary), InfluxQL (compat) | MIT (2.x) | `/api/v2/write` |
| **InfluxDB Cloud (TSM)** | Managed service | TSM (Go) | Flux, InfluxQL | Proprietary | `/api/v2/write` |
| **InfluxDB 3 Core** | GA (Apr 2025) | IOx (Rust, FDAP stack) | SQL (primary), InfluxQL | MIT / Apache 2.0 | `/api/v2/write` (compat), `/api/v3/write_lp` (native) |
| **InfluxDB 3 Enterprise** | GA (Apr 2025) | IOx (Rust, FDAP stack) | SQL (primary), InfluxQL | Commercial | `/api/v2/write` (compat), `/api/v3/write_lp` (native) |
| **InfluxDB Cloud Serverless** | Managed service | IOx (Rust) | SQL, InfluxQL | Proprietary | `/api/v2/write` |
| **InfluxDB Cloud Dedicated** | Managed service | IOx (Rust) | SQL, InfluxQL | Proprietary | `/api/v2/write` |

### 7.2 InfluxDB 3 Core vs. Enterprise

| Feature | Core (OSS) | Enterprise |
|---------|-----------|------------|
| License | MIT / Apache 2.0 | Commercial (free tier available) |
| Deployment | Single-node only | Multi-node (up to 3 initially) |
| Query time range | ~72 hours (configurable but resource-intensive) | Unlimited historical |
| Compaction | No | Yes (critical for long-term performance) |
| High Availability | No | Yes (read replicas, automatic failover) |
| Processing Engine | Yes (embedded Python) | Yes (embedded Python) |
| Object Storage | Parquet on local/object storage | Parquet on object storage |
| Apache Iceberg | Planned | Planned |

### 7.3 What Version Should We Target?

**Recommended: Target the `/api/v2/write` endpoint as the primary write path.**

Rationale:
1. **Maximum compatibility.** The `/api/v2/write` endpoint works across InfluxDB 2.x, 3.x Core, 3.x Enterprise, Cloud (TSM), Cloud Serverless, and Cloud Dedicated. It is the universal write interface.
2. **The line protocol format is identical across all versions.** The data format does not change.
3. **Query support should be version-aware:**
   - Default to SQL for InfluxDB 3.x (via `/api/v3/query_sql` or Arrow Flight)
   - Support Flux for InfluxDB 2.x (via `/api/v2/query`)
   - Support InfluxQL for all versions

**Proposed version compatibility matrix:**

```toml
[connector.influxdb]
# Auto-detected or manually configured
version = "auto"  # "auto", "v2", "v3"

# Write endpoint (always v2-compatible)
write_endpoint = "v2"  # "v2" (default, universal) or "v3" (InfluxDB 3 native)

# Query endpoint (for source connector)
query_language = "sql"  # "sql" (v3), "flux" (v2), "influxql" (v2/v3)
```

**Version detection strategy:**

```rust
pub async fn detect_version(client: &reqwest::Client, base_url: &str) -> InfluxDbVersion {
    // Try v3 health endpoint first
    if let Ok(resp) = client.get(format!("{}/health", base_url)).send().await {
        if let Ok(body) = resp.json::<serde_json::Value>().await {
            if body.get("version").and_then(|v| v.as_str())
                .map(|v| v.starts_with("3."))
                .unwrap_or(false)
            {
                return InfluxDbVersion::V3;
            }
        }
    }
    // Fall back to v2
    InfluxDbVersion::V2
}
```

---

## Summary of Recommendations

| Decision | Recommendation | Rationale |
|----------|---------------|-----------|
| **HTTP client** | `reqwest` directly (no InfluxDB client crate) | No mature official Rust client; API is simple enough |
| **Write endpoint** | `/api/v2/write` (default) | Universal across all InfluxDB versions |
| **Batch size** | 5,000 lines default, configurable | InfluxDB official recommendation |
| **Compression** | gzip enabled by default | Up to 5x write speed improvement |
| **Timestamp precision** | `ms` default, configurable | Good balance of precision and compression |
| **Error handling** | Retry 5xx/429; DLQ for 4xx | Standard categories from InfluxDB docs |
| **Source polling** | Time-range with high-water mark | No streaming/subscription API available |
| **Query language** | SQL for v3, Flux for v2 (configurable) | Matches primary language per version |
| **Line protocol generation** | Custom implementation | Simple format; avoids dependency on unmaintained crates |
| **Tag sorting** | Sort lexicographically before write | InfluxDB best practice for write performance |
| **Target version** | All (v2 write API is universal) | Maximum user flexibility |

---

## References

- [InfluxDB v2 Line Protocol Reference](https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/)
- [InfluxDB v2 Write API Documentation](https://docs.influxdata.com/influxdb/v2/write-data/developer-tools/api/)
- [Optimize Writes to InfluxDB](https://docs.influxdata.com/influxdb/v2/write-data/best-practices/optimize-writes/)
- [Troubleshoot Issues Writing Data](https://docs.influxdata.com/influxdb/v2/write-data/troubleshoot/)
- [InfluxDB Data Retention](https://docs.influxdata.com/influxdb/v2/reference/internals/data-retention/)
- [InfluxDB 3 Core Documentation](https://docs.influxdata.com/influxdb3/core/)
- [InfluxDB 3 Enterprise Documentation](https://docs.influxdata.com/influxdb3/enterprise/)
- [influxdb crate (Rust)](https://crates.io/crates/influxdb) | [GitHub](https://github.com/influxdb-rs/influxdb-rust)
- [influxdb2 crate (Rust)](https://crates.io/crates/influxdb2) | [GitHub](https://github.com/aprimadi/influxdb2)
- [influxdb3 crate (Rust)](https://crates.io/crates/influxdb3) | [docs.rs](https://docs.rs/influxdb3/latest/influxdb3/)
- [influxdb-line-protocol crate](https://crates.io/crates/influxdb-line-protocol)
- [Confluent InfluxDB Sink Connector](https://docs.confluent.io/kafka-connectors/influxdb/current/influx-db-sink-connector/overview.html)
- [Confluent InfluxDB 2 Sink Connector (Cloud)](https://docs.confluent.io/cloud/current/connectors/cc-influxdb2-sink.html)
- [Confluent InfluxDB 3 Sink Connector (Cloud)](https://docs.confluent.io/cloud/current/connectors/cc-influx-db3-sink.html)
- [Telegraf Plugin Directory](https://docs.influxdata.com/telegraf/v1/plugins/)
- [Telegraf InfluxDB v2 Output Plugin](https://github.com/influxdata/telegraf/blob/master/plugins/outputs/influxdb_v2/README.md)
- [Telegraf GitHub Repository](https://github.com/influxdata/telegraf)
- [InfluxDB IOx Announcement](https://www.influxdata.com/blog/announcing-influxdb-iox/)
- [InfluxDB 3 Core and Enterprise GA Announcement](https://www.influxdata.com/blog/influxdb-3-oss-ga/)
- [InfluxQL vs SQL for InfluxDB](https://www.influxdata.com/blog/influxql-vs-sql-influxdb/)
- [Flux vs InfluxQL Comparison](https://docs.influxdata.com/influxdb/v2/reference/syntax/flux/flux-vs-influxql/)
- [InfluxDB v3: Why Rust Beat Go](https://thenewstack.io/influxdb-v3-why-rust-beat-go-for-time-series-database/)
- [InfluxDB 3 Open Source GA (InfoQ)](https://www.infoq.com/news/2025/04/influxdb3-open-source/)
