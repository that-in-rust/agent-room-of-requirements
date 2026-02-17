# MongoDB Connector Specification for Apache Iggy

**Document version**: 2.0
**Date**: 2026-02-17
**Based on**: v1.0 (2026-02-17)
**Target Iggy version**: 0.2.2-edge.1 (current workspace version)
**MongoDB Rust driver**: v3.x (fluent builder API, released 2024-06-25; latest v3.5.1 as of 2026-02-03)
**Source code basis**: All trait signatures, macro patterns, config patterns, and struct designs were read directly from the live Iggy codebase at `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/` via the Parseltongue code analysis server at `http://localhost:7777` (15,998 entities, 78,896 edges indexed).

---

## Changelog from v1

This section lists every fix applied to v1. Each fix is tagged with a `<!-- v2-fix: BUG-N -->` comment at the point of change in the spec.

| ID | Severity | Description |
|----|----------|-------------|
| BUG-2 | Critical | MongoDB Rust driver v3 uses a fluent builder API, not `with_options()`. All `collection.insert_many(...).with_options(opts)`, `collection.find(...).with_options(opts)`, and `db.watch()...with_options(opts)` patterns replaced with fluent chaining (e.g., `.ordered(false)`, `.sort(...)`, `.batch_size(n)`, `.full_document(...)`). `InsertManyOptions::builder()` and `FindOptions::builder()` removed. |
| BUG-3 | Critical | `ChangeStreamOptions` struct with `.resume_after` field assignment removed; replaced with fluent `.resume_after(token_doc)` chained on the `watch()` call. |
| BUG-11 | Medium | `process_messages` now returns `Err` when a batch insert fails after all retry attempts, instead of swallowing the error and returning `Ok(())`. |
| BUG-12 | Medium | `messages_processed` counter now only increments for successfully inserted batches, not unconditionally for all messages. |
| BUG-13 | Medium | `execute_insert_many_with_retry` now passes `&docs` (a slice) to `insert_many()` instead of cloning the entire `Vec<Document>` on every retry attempt. The mongodb v3 API accepts `impl IntoIterator<Item = impl Borrow<Document>>`, so `&docs` works without allocation. |
| BUG-14 | Medium | The change stream cursor is now opened once in `open()` and stored as `Option<ChangeStream<Document>>` on `MongoDBSource`. `poll_change_stream()` drains the existing cursor instead of reopening it on every poll. The cursor is re-opened on error. |
| ISSUE-7 | Minor | `with_retry_async` signature changed from `delay: Duration` to `delay_ms: u64` to match the real PostgresSource pattern. Backoff uses `Duration::from_millis(delay_ms * attempts as u64)`. |
| ISSUE-16 | Minor | `prost` added to `cargo-machete` ignored list in both Cargo.toml files, matching the real PostgresSink pattern. |
| ISSUE-17 | Minor | Apache 2.0 license header added to the full `lib.rs` code blocks. |
| ISSUE-22 | Minor | `include_metadata` flag in `poll_collections` now actually controls output structure: when false, `collection_name`, `operation_type`, and `timestamp` are omitted from the `MongoChangeRecord` (those fields become `Option<String>` / `Option<DateTime<Utc>>`). |
| ISSUE-23 | Minor | `offset_string_to_bson` now attempts to parse ISO 8601 datetime strings before falling back to plain string, enabling correct `$gt` comparisons on BSON DateTime fields. |

---

## Table of Contents

1. Background and Motivation
2. Architecture Overview
3. Exact Trait Signatures (from real source code)
4. The Plugin System (cdylib + FFI macros)
5. MongoDBSink — Full Specification
6. MongoDBSource — Full Specification
7. Config Structs and TOML Examples
8. Cargo.toml Dependencies
9. Error Handling Strategy
10. State Management and Offset Tracking
11. Retry Logic
12. Testing Strategy
13. File and Directory Layout
14. Implementation Checklist

---

## 1. Background and Motivation

Apache Iggy is a persistent message streaming platform. Its connector system lets external systems
read from Iggy (via Source connectors) and write to external systems (via Sink connectors). Each
connector is a Rust dynamic library (`.so` / `.dylib` / `.dll`) loaded at runtime by the connector
daemon.

MongoDB is the most widely deployed document database. A MongoDB connector would enable:

- **Sink**: persisting every Iggy message as a MongoDB document, with optional metadata fields,
  configurable collection naming, BSON or raw payload storage, and batched inserts via
  `insert_many`.
- **Source**: streaming MongoDB data into Iggy — either by polling collections on an interval
  (analogous to PostgresSource polling mode) or by tailing MongoDB Change Streams (the MongoDB
  equivalent of PostgreSQL WAL CDC).

This spec is modeled precisely on the two most relevant existing connectors:

| Reference connector | File | LOC |
|---------------------|------|-----|
| PostgresSink | `core/connectors/sinks/postgres_sink/src/lib.rs` | 799 |
| PostgresSource | `core/connectors/sources/postgres_source/src/lib.rs` | 1,410 |

**MongoDB Rust Driver v3 Note**: The mongodb crate v3 (released 2024-06-25) changed the API from
`with_options(SomeOptions::builder().field(val).build())` to a fluent builder pattern where options
are chained directly on the operation call. This spec uses the v3 fluent API exclusively.

---

## 2. Architecture Overview

```
                +----------------------------------------+
                |        connector runtime daemon         |
                |  core/connectors/runtime/src/main.rs   |
                |                                        |
                |  dlopen2 loads .so/.dylib at runtime   |
                |  calls open() / consume() / close()    |
                |  calls open() / handle() / close()     |
                +--------------------+-------------------+
                                     |  FFI
              +----------------------+----------------------+
              |                      |                      |
   +----------v----------+  +--------v-----------+
   |  iggy_connector_    |  |  iggy_connector_    |
   |  mongodb_sink       |  |  mongodb_source     |
   |  (cdylib + lib)     |  |  (cdylib + lib)     |
   |                     |  |                     |
   |  MongoDBSink        |  |  MongoDBSource      |
   |  implements Sink    |  |  implements Source  |
   +----------+----------+  +----------+----------+
              |                        |
              v                        v
      MongoDB via mongodb crate  MongoDB via mongodb crate
      (insert_many batches)      (find polling / change streams)
```

The runtime loads each connector as a shared library. The `sink_connector!(MongoDBSink)` and
`source_connector!(MongoDBSource)` macros (defined in the SDK) generate the `extern "C"` FFI
boundary functions (`open`, `consume`/`handle`, `close`, `version`).

---

## 3. Exact Trait Signatures (from real source code)

These are copied verbatim from `core/connectors/sdk/src/lib.rs`.

### Sink trait

```rust
/// The Sink trait defines the interface for a sink connector, responsible for consuming
/// the messages from the configured topics.
/// Once the messages are consumed (and optionally transformed before), they should be
/// sent further to the specified destination.
#[async_trait]
pub trait Sink: Send + Sync {
    /// Invoked when the sink is initialized, allowing it to perform any necessary setup.
    async fn open(&mut self) -> Result<(), Error>;

    /// Invoked every time a batch of messages is received from the configured stream(s) and topic(s).
    async fn consume(
        &self,
        topic_metadata: &TopicMetadata,
        messages_metadata: MessagesMetadata,
        messages: Vec<ConsumedMessage>,
    ) -> Result<(), Error>;

    /// Invoked when the sink is closed, allowing it to perform any necessary cleanup.
    async fn close(&mut self) -> Result<(), Error>;
}
```

### Source trait

```rust
/// The Source trait defines the interface for a source connector, responsible for producing
/// the messages to the configured stream and topic.
/// Once the messages are produced (e.g. fetched from an external API), they will be sent
/// further to the specified destination.
#[async_trait]
pub trait Source: Send + Sync {
    /// Invoked when the source is initialized, allowing it to perform any necessary setup.
    async fn open(&mut self) -> Result<(), Error>;

    /// Invoked every time a batch of messages is produced to the configured stream and topic.
    async fn poll(&self) -> Result<ProducedMessages, Error>;

    /// Invoked when the source is closed, allowing it to perform any necessary cleanup.
    async fn close(&mut self) -> Result<(), Error>;
}
```

### Key SDK types used by implementations

```rust
// From core/connectors/sdk/src/lib.rs

#[repr(C)]
#[derive(Debug, Serialize, Deserialize)]
pub struct TopicMetadata {
    pub stream: String,
    pub topic: String,
}

#[repr(C)]
#[derive(Debug, Serialize, Deserialize)]
pub struct MessagesMetadata {
    pub partition_id: u32,
    pub current_offset: u64,
    pub schema: Schema,
}

#[repr(C)]
#[derive(Debug, Serialize, Deserialize)]
pub struct ConsumedMessage {
    pub id: u128,
    pub offset: u64,
    pub checksum: u64,
    pub timestamp: u64,
    pub origin_timestamp: u64,
    pub headers: Option<HashMap<HeaderKey, HeaderValue>>,
    pub payload: Payload,
}

#[repr(C)]
#[derive(Debug, Serialize, Deserialize)]
pub struct ProducedMessages {
    pub schema: Schema,
    pub messages: Vec<ProducedMessage>,
    pub state: Option<ConnectorState>,
}

#[repr(C)]
#[derive(Debug, Serialize, Deserialize)]
pub struct ProducedMessage {
    pub id: Option<u128>,
    pub checksum: Option<u64>,
    pub timestamp: Option<u64>,
    pub origin_timestamp: Option<u64>,
    pub headers: Option<HashMap<HeaderKey, HeaderValue>>,
    pub payload: Vec<u8>,
}

/// ConnectorState wraps serialized state bytes using MessagePack (rmp_serde).
#[derive(Debug, Serialize, Deserialize)]
pub struct ConnectorState(pub Vec<u8>);

impl ConnectorState {
    pub fn deserialize<T: serde::de::DeserializeOwned>(
        self, connector_name: &str, connector_id: u32,
    ) -> Option<T> { /* rmp_serde::from_slice */ }

    pub fn serialize<T: serde::Serialize>(
        state: &T, connector_name: &str, connector_id: u32,
    ) -> Option<Self> { /* rmp_serde::to_vec */ }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash, Error)]
pub enum Error {
    #[error("Invalid config")]                     InvalidConfig,
    #[error("Invalid record")]                     InvalidRecord,
    #[error("Init error: {0}")]                    InitError(String),
    #[error("HTTP request failed: {0}")]           HttpRequestFailed(String),
    #[error("Storage error: {0}")]                 Storage(String),
    #[error("Connection error: {0}")]              Connection(String),
    #[error("Cannot store data: {0}")]             CannotStoreData(String),
    #[error("Serialization error: {0}")]           Serialization(String),
    #[error("Invalid JSON payload.")]              InvalidJsonPayload,
    #[error("Invalid text payload.")]              InvalidTextPayload,
    #[error("Invalid payload type")]               InvalidPayloadType,
    // ... and more
}

// Payload DOES derive Clone (confirmed from real source).
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum Payload {
    Json(simd_json::OwnedValue),
    Raw(Vec<u8>),
    Text(String),
    Proto(String),
    FlatBuffer(Vec<u8>),
}

impl Payload {
    pub fn try_into_vec(self) -> Result<Vec<u8>, Error> { /* ... */ }
}
```

---

## 4. The Plugin System (cdylib + FFI macros)

### How plugins are loaded

The runtime (`core/connectors/runtime/src/main.rs`) uses `dlopen2` to load `.so`/`.dylib`/`.dll`
files. It calls these `extern "C"` symbols:

**For a Sink plugin**:
```
open(id, config_ptr, config_len, log_callback) -> i32
consume(id, topic_meta_ptr, topic_meta_len, messages_meta_ptr, messages_meta_len,
        messages_ptr, messages_len) -> i32
close(id) -> i32
version() -> *const c_char
```

**For a Source plugin**:
```
open(id, config_ptr, config_len, state_ptr, state_len, log_callback) -> i32
handle(id, callback: SendCallback) -> i32
close(id) -> i32
version() -> *const c_char
```

### The macros generate all FFI boilerplate

In `lib.rs`, a single macro invocation does everything:

```rust
// For a sink:
sink_connector!(MongoDBSink);

// For a source:
source_connector!(MongoDBSource);
```

The `sink_connector!` macro (from `core/connectors/sdk/src/sink.rs`) generates:
- A `static INSTANCES: Lazy<DashMap<u32, SinkContainer<MongoDBSink>>>` for multi-instance support
- `extern "C" fn open(...)` — deserializes config JSON, calls `MongoDBSink::new(id, config)`
- `extern "C" fn consume(...)` — dispatches to the stored instance
- `extern "C" fn close(...)` — removes from map, calls `sink.close()`
- `extern "C" fn version()` — returns `CARGO_PKG_VERSION`

The `source_connector!` macro generates the equivalent with `handle` instead of `consume`, plus
state restoration (the runtime passes back persisted `ConnectorState` bytes on restart).

### Constructor signatures required by the macros

The macro calls `<$type>::new` as a factory function. This means:

```rust
// Sink constructor — called by sink_connector! macro via SinkContainer::open
impl MongoDBSink {
    pub fn new(id: u32, config: MongoDBSinkConfig) -> Self { ... }
}

// Source constructor — called by source_connector! macro via SourceContainer::open
impl MongoDBSource {
    pub fn new(id: u32, config: MongoDBSourceConfig, state: Option<ConnectorState>) -> Self { ... }
}
```

The sink does NOT receive state (sinks are stateless from the runtime's perspective). The source
DOES receive `Option<ConnectorState>` for offset resume.

---

## 5. MongoDBSink — Full Specification

### 5.1 Struct Definition

```rust
// Licensed under the Apache License, Version 2.0
// core/connectors/sinks/mongodb_sink/src/lib.rs
// <!-- v2-fix: ISSUE-17 — Apache license header added -->

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

use async_trait::async_trait;
use humantime::Duration as HumanDuration;
use iggy_common::{DateTime, Utc};
use iggy_connector_sdk::{
    ConsumedMessage, Error, MessagesMetadata, Sink, TopicMetadata, sink_connector,
};
use mongodb::{Client, Collection, Database};
use mongodb::bson::{doc, Document, Bson, DateTime as BsonDateTime};
use mongodb::options::ClientOptions;
// <!-- v2-fix: BUG-2 — InsertManyOptions removed; v3 uses fluent API, not with_options() -->
use serde::{Deserialize, Serialize};
use std::str::FromStr;
use std::time::Duration;
use tokio::sync::Mutex;
use tracing::{debug, error, info, warn};

sink_connector!(MongoDBSink);

const DEFAULT_MAX_RETRIES: u32 = 3;
const DEFAULT_RETRY_DELAY_MS: u64 = 1000;
const DEFAULT_RETRY_DELAY: &str = "1s";

#[derive(Debug)]
pub struct MongoDBSink {
    pub id: u32,
    client: Option<Client>,
    config: MongoDBSinkConfig,
    state: Mutex<SinkState>,
    verbose: bool,
    retry_delay_ms: u64,
    // <!-- v2-fix: ISSUE-7 — retry delay stored as u64 millis to match PostgresSource pattern -->
}
```

### 5.2 Config Struct

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MongoDBSinkConfig {
    /// MongoDB connection URI, e.g. "mongodb://user:pass@localhost:27017"
    pub connection_uri: String,

    /// Target database name
    pub database: String,

    /// Target collection name. Supports template variables: {stream}, {topic}
    /// If None, defaults to "{topic}"
    pub collection: Option<String>,

    /// Maximum number of documents per insert_many call (default: 100)
    pub batch_size: Option<u32>,

    /// Maximum number of connections in the driver pool (default: 10)
    pub max_pool_size: Option<u32>,

    /// Whether to include Iggy metadata fields as top-level BSON fields
    /// (iggy_offset, iggy_timestamp, iggy_stream, iggy_topic, iggy_partition_id)
    /// Default: true
    pub include_metadata: Option<bool>,

    /// Whether to include iggy_checksum field. Default: true
    pub include_checksum: Option<bool>,

    /// Whether to include iggy_origin_timestamp field. Default: true
    pub include_origin_timestamp: Option<bool>,

    /// How to store the message payload:
    ///   "document"  — parse JSON payload and embed as a BSON sub-document (default)
    ///   "binary"    — store raw bytes as BSON Binary
    ///   "string"    — store UTF-8 text as BSON String
    pub payload_format: Option<String>,

    /// Whether to use ordered inserts (stops on first error) or unordered
    /// (continues on error, maximizing throughput). Default: false (unordered)
    pub ordered_inserts: Option<bool>,

    /// Enable verbose INFO-level logging (default: false, uses DEBUG)
    pub verbose_logging: Option<bool>,

    /// Maximum retry attempts for transient errors. Default: 3
    pub max_retries: Option<u32>,

    /// Humantime duration string for base retry delay, e.g. "1s", "500ms". Default: "1s"
    pub retry_delay: Option<String>,
}
```

### 5.3 Internal State Struct

```rust
#[derive(Debug)]
struct SinkState {
    messages_processed: u64,
    insertion_errors: u64,
}
```

### 5.4 PayloadFormat Enum

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub enum PayloadFormat {
    #[default]
    Document,  // Parse JSON into BSON Document (best for JSON payloads)
    Binary,    // Store raw bytes as BSON Binary
    Text,      // Store UTF-8 string as BSON String
}

impl PayloadFormat {
    fn from_config(s: Option<&str>) -> Self {
        match s.map(|s| s.to_lowercase()).as_deref() {
            Some("binary") | Some("raw") | Some("bytes") => PayloadFormat::Binary,
            Some("string") | Some("text") | Some("utf8") => PayloadFormat::Text,
            _ => PayloadFormat::Document,
        }
    }
}
```

### 5.5 Constructor

```rust
impl MongoDBSink {
    pub fn new(id: u32, config: MongoDBSinkConfig) -> Self {
        let verbose = config.verbose_logging.unwrap_or(false);
        // <!-- v2-fix: ISSUE-7 — store as u64 millis to match PostgresSource with_retry pattern -->
        let delay_str = config.retry_delay.as_deref().unwrap_or(DEFAULT_RETRY_DELAY);
        let retry_delay_ms = HumanDuration::from_str(delay_str)
            .map(|d| {
                let dur: Duration = d.into();
                dur.as_millis() as u64
            })
            .unwrap_or(DEFAULT_RETRY_DELAY_MS);
        MongoDBSink {
            id,
            client: None,
            config,
            state: Mutex::new(SinkState {
                messages_processed: 0,
                insertion_errors: 0,
            }),
            verbose,
            retry_delay_ms,
        }
    }
}
```

### 5.6 Sink Trait Implementation

```rust
#[async_trait]
impl Sink for MongoDBSink {
    async fn open(&mut self) -> Result<(), Error> {
        info!(
            "Opening MongoDB sink connector with ID: {}. Database: {}, Collection template: {}",
            self.id,
            self.config.database,
            self.config.collection.as_deref().unwrap_or("{topic}"),
        );
        self.connect().await?;
        Ok(())
    }

    async fn consume(
        &self,
        topic_metadata: &TopicMetadata,
        messages_metadata: MessagesMetadata,
        messages: Vec<ConsumedMessage>,
    ) -> Result<(), Error> {
        self.process_messages(topic_metadata, &messages_metadata, &messages).await
    }

    async fn close(&mut self) -> Result<(), Error> {
        info!("Closing MongoDB sink connector with ID: {}", self.id);

        // The mongodb driver manages its own connection pool; dropping the client closes it.
        self.client = None;
        info!("MongoDB client released for sink connector ID: {}", self.id);

        let state = self.state.lock().await;
        info!(
            "MongoDB sink ID: {} processed {} messages with {} errors",
            self.id, state.messages_processed, state.insertion_errors
        );
        Ok(())
    }
}
```

### 5.7 Private Implementation Methods

```rust
impl MongoDBSink {
    async fn connect(&mut self) -> Result<(), Error> {
        let uri = &self.config.connection_uri;
        let redacted = redact_connection_uri(uri);
        let max_pool_size = self.config.max_pool_size.unwrap_or(10);

        info!("Connecting to MongoDB (pool size: {max_pool_size}): {redacted}");

        let mut options = ClientOptions::parse(uri)
            .await
            .map_err(|e| Error::InitError(format!("Failed to parse MongoDB URI: {e}")))?;

        options.max_pool_size = Some(max_pool_size);

        let client = Client::with_options(options)
            .map_err(|e| Error::InitError(format!("Failed to create MongoDB client: {e}")))?;

        // Verify connectivity with a ping
        client
            .database("admin")
            .run_command(doc! { "ping": 1 })
            .await
            .map_err(|e| Error::InitError(format!("MongoDB connectivity test failed: {e}")))?;

        self.client = Some(client);
        info!("Connected to MongoDB with pool size {max_pool_size}");
        Ok(())
    }

    fn resolve_collection_name(
        &self,
        topic_metadata: &TopicMetadata,
    ) -> String {
        let template = self.config.collection.as_deref().unwrap_or("{topic}");
        template
            .replace("{stream}", &topic_metadata.stream)
            .replace("{topic}", &topic_metadata.topic)
    }

    fn get_collection(&self, collection_name: &str) -> Result<Collection<Document>, Error> {
        let client = self.client.as_ref()
            .ok_or_else(|| Error::InitError("MongoDB client not connected".to_string()))?;
        let db: Database = client.database(&self.config.database);
        Ok(db.collection(collection_name))
    }

    async fn process_messages(
        &self,
        topic_metadata: &TopicMetadata,
        messages_metadata: &MessagesMetadata,
        messages: &[ConsumedMessage],
    ) -> Result<(), Error> {
        // <!-- v2-fix: BUG-11 — propagate errors instead of swallowing them -->
        // <!-- v2-fix: BUG-12 — only count successfully processed messages -->
        let batch_size = self.config.batch_size.unwrap_or(100) as usize;
        let collection_name = self.resolve_collection_name(topic_metadata);
        let mut successfully_processed: usize = 0;

        for batch in messages.chunks(batch_size) {
            match self
                .insert_batch(batch, topic_metadata, messages_metadata, &collection_name)
                .await
            {
                Ok(()) => {
                    // <!-- v2-fix: BUG-12 — count only after successful insert -->
                    successfully_processed += batch.len();
                }
                Err(e) => {
                    let mut state = self.state.lock().await;
                    state.insertion_errors += batch.len() as u64;
                    error!("Failed to insert batch into MongoDB collection '{collection_name}': {e}");
                    // <!-- v2-fix: BUG-11 — return Err so the runtime knows this batch failed -->
                    return Err(e);
                }
            }
        }

        {
            let mut state = self.state.lock().await;
            // <!-- v2-fix: BUG-12 — only increment by the number actually inserted -->
            state.messages_processed += successfully_processed as u64;
        }

        if self.verbose {
            info!(
                "MongoDB sink ID: {} processed {} messages to collection '{collection_name}'",
                self.id, successfully_processed
            );
        } else {
            debug!(
                "MongoDB sink ID: {} processed {} messages to collection '{collection_name}'",
                self.id, successfully_processed
            );
        }

        Ok(())
    }

    async fn insert_batch(
        &self,
        messages: &[ConsumedMessage],
        topic_metadata: &TopicMetadata,
        messages_metadata: &MessagesMetadata,
        collection_name: &str,
    ) -> Result<(), Error> {
        if messages.is_empty() {
            return Ok(());
        }

        let include_metadata = self.config.include_metadata.unwrap_or(true);
        let include_checksum = self.config.include_checksum.unwrap_or(true);
        let include_origin_timestamp = self.config.include_origin_timestamp.unwrap_or(true);
        let payload_format = PayloadFormat::from_config(self.config.payload_format.as_deref());

        let mut docs: Vec<Document> = Vec::with_capacity(messages.len());

        for message in messages {
            let doc = self.build_document(
                message,
                topic_metadata,
                messages_metadata,
                include_metadata,
                include_checksum,
                include_origin_timestamp,
                payload_format,
            )?;
            docs.push(doc);
        }

        self.execute_insert_many_with_retry(collection_name, docs).await
    }

    fn build_document(
        &self,
        message: &ConsumedMessage,
        topic_metadata: &TopicMetadata,
        messages_metadata: &MessagesMetadata,
        include_metadata: bool,
        include_checksum: bool,
        include_origin_timestamp: bool,
        payload_format: PayloadFormat,
    ) -> Result<Document, Error> {
        let mut doc = Document::new();

        // Use Iggy message ID as MongoDB _id (stored as string since u128 exceeds i64)
        doc.insert("_id", message.id.to_string());

        if include_metadata {
            doc.insert("iggy_offset", message.offset as i64);
            let ts = micros_to_bson_datetime(message.timestamp);
            doc.insert("iggy_timestamp", ts);
            doc.insert("iggy_stream", topic_metadata.stream.clone());
            doc.insert("iggy_topic", topic_metadata.topic.clone());
            doc.insert("iggy_partition_id", messages_metadata.partition_id as i32);
        }

        if include_checksum {
            doc.insert("iggy_checksum", message.checksum as i64);
        }

        if include_origin_timestamp {
            let ots = micros_to_bson_datetime(message.origin_timestamp);
            doc.insert("iggy_origin_timestamp", ots);
        }

        let payload_bytes = message.payload.clone().try_into_vec()
            .map_err(|e| Error::CannotStoreData(format!("Failed to convert payload: {e}")))?;

        match payload_format {
            PayloadFormat::Document => {
                // Parse JSON bytes into a BSON document
                let json_value: serde_json::Value = serde_json::from_slice(&payload_bytes)
                    .map_err(|_| Error::InvalidJsonPayload)?;
                let bson_value = mongodb::bson::to_bson(&json_value)
                    .map_err(|e| Error::CannotStoreData(format!("Failed to convert JSON to BSON: {e}")))?;
                doc.insert("payload", bson_value);
            }
            PayloadFormat::Binary => {
                doc.insert("payload", Bson::Binary(mongodb::bson::Binary {
                    subtype: mongodb::bson::spec::BinarySubtype::Generic,
                    bytes: payload_bytes,
                }));
            }
            PayloadFormat::Text => {
                let text = String::from_utf8(payload_bytes)
                    .map_err(|_| Error::InvalidTextPayload)?;
                doc.insert("payload", text);
            }
        }

        doc.insert("created_at", BsonDateTime::now());

        Ok(doc)
    }

    async fn execute_insert_many_with_retry(
        &self,
        collection_name: &str,
        docs: Vec<Document>,
    ) -> Result<(), Error> {
        // <!-- v2-fix: BUG-2 — use fluent API instead of InsertManyOptions::builder() + with_options() -->
        // <!-- v2-fix: BUG-13 — pass &docs (slice) to insert_many to avoid cloning on every retry -->
        let max_retries = self.config.max_retries.unwrap_or(DEFAULT_MAX_RETRIES);
        let retry_delay_ms = self.retry_delay_ms;
        let ordered = self.config.ordered_inserts.unwrap_or(false);
        let collection = self.get_collection(collection_name)?;

        let mut attempts = 0u32;
        loop {
            // The mongodb v3 API accepts impl IntoIterator<Item = impl Borrow<Document>>.
            // Passing &docs (a shared slice reference) avoids allocating a clone on every attempt.
            match collection
                .insert_many(&docs)
                .ordered(ordered)          // <!-- v2-fix: BUG-2 — fluent .ordered() instead of InsertManyOptions -->
                .await
            {
                Ok(result) => {
                    if self.verbose {
                        info!(
                            "Inserted {} documents into '{collection_name}'",
                            result.inserted_ids.len()
                        );
                    }
                    return Ok(());
                }
                Err(e) => {
                    attempts += 1;
                    let is_transient = is_transient_mongodb_error(&e);
                    if !is_transient || attempts >= max_retries {
                        error!("MongoDB insert_many failed after {attempts} attempts: {e}");
                        return Err(Error::CannotStoreData(format!(
                            "insert_many failed after {attempts} attempts: {e}"
                        )));
                    }
                    warn!(
                        "Transient MongoDB error (attempt {attempts}/{max_retries}): {e}. Retrying..."
                    );
                    // <!-- v2-fix: ISSUE-7 — use delay_ms * attempts to match PostgresSource pattern -->
                    tokio::time::sleep(Duration::from_millis(retry_delay_ms * attempts as u64)).await;
                }
            }
        }
    }
}
```

### 5.8 Transient Error Detection for MongoDB

```rust
fn is_transient_mongodb_error(e: &mongodb::error::Error) -> bool {
    use mongodb::error::ErrorKind;
    match e.kind.as_ref() {
        // Network-level errors are always transient
        ErrorKind::Io(_) => true,
        // Connection pool exhausted — transient
        ErrorKind::ConnectionPoolCleared { .. } => true,
        // Server selection timeout — might recover
        ErrorKind::ServerSelection { .. } => true,
        // Write errors: duplicate key (_id conflict) is NOT transient;
        // other write errors may be transient
        ErrorKind::Write(write_failure) => {
            use mongodb::error::WriteFailure;
            match write_failure {
                WriteFailure::WriteConcernError(_) => true,
                WriteFailure::WriteError(we) => {
                    // 11000 = duplicate key error — not transient
                    we.code != 11000
                }
            }
        }
        // BulkWrite: check if any error is non-transient
        ErrorKind::BulkWrite(bw) => {
            // If all failures are duplicate key, not transient
            bw.write_errors.as_ref().map(|errs| {
                errs.iter().all(|e| e.code != 11000)
            }).unwrap_or(true)
        }
        _ => false,
    }
}

fn redact_connection_uri(uri: &str) -> String {
    // Same pattern as PostgresSink: show scheme + first 3 chars, redact rest
    if let Some(scheme_end) = uri.find("://") {
        let scheme = &uri[..scheme_end + 3];
        let rest = &uri[scheme_end + 3..];
        let preview: String = rest.chars().take(3).collect();
        return format!("{scheme}{preview}***");
    }
    let preview: String = uri.chars().take(3).collect();
    format!("{preview}***")
}

fn micros_to_bson_datetime(micros: u64) -> BsonDateTime {
    // BsonDateTime uses milliseconds since Unix epoch
    let millis = (micros / 1000) as i64;
    BsonDateTime::from_millis(millis)
}
```

---

## 6. MongoDBSource — Full Specification

### 6.1 Struct Definition

```rust
// Licensed under the Apache License, Version 2.0
// core/connectors/sources/mongodb_source/src/lib.rs
// <!-- v2-fix: ISSUE-17 — Apache license header added -->

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

use async_trait::async_trait;
use humantime::Duration as HumanDuration;
use iggy_common::{DateTime, Utc};
use iggy_connector_sdk::{
    ConnectorState, Error, ProducedMessage, ProducedMessages, Schema, Source, source_connector,
};
use mongodb::{Client, Database};
use mongodb::bson::{doc, Document, Bson, DateTime as BsonDateTime};
use mongodb::change_stream::event::{ChangeStreamEvent, OperationType};
// <!-- v2-fix: BUG-2 — ChangeStreamOptions, FindOptions removed; v3 uses fluent API -->
// <!-- v2-fix: BUG-3 — ChangeStreamOptions struct no longer needed for resume_after -->
use mongodb::options::{ClientOptions, FullDocumentType};
use mongodb::change_stream::ChangeStream;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::str::FromStr;
use std::time::Duration;
use tokio::sync::Mutex;
use tracing::{debug, error, info, warn};
use uuid::Uuid;

source_connector!(MongoDBSource);

const DEFAULT_MAX_RETRIES: u32 = 3;
const DEFAULT_RETRY_DELAY_MS: u64 = 1000;
const DEFAULT_RETRY_DELAY: &str = "1s";
const CONNECTOR_NAME: &str = "MongoDB source";

#[derive(Debug)]
pub struct MongoDBSource {
    pub id: u32,
    client: Option<Client>,
    config: MongoDBSourceConfig,
    state: Mutex<SourceState>,
    verbose: bool,
    retry_delay_ms: u64,
    // <!-- v2-fix: ISSUE-7 — u64 millis to match PostgresSource pattern -->
    poll_interval: Duration,
    // <!-- v2-fix: BUG-14 — change stream cursor stored as a field, opened once in open() -->
    change_stream: Mutex<Option<ChangeStream<Document>>>,
}
```

### 6.2 Config Struct

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MongoDBSourceConfig {
    /// MongoDB connection URI
    pub connection_uri: String,

    /// Database to read from
    pub database: String,

    /// Operating mode: "polling" or "change_stream"
    /// - "polling": repeatedly queries collections using find() with offset tracking
    /// - "change_stream": uses MongoDB Change Streams (requires replica set or Atlas)
    pub mode: String,

    /// Collections to poll (used in polling mode). Ignored for change_stream mode
    /// where all collections in the database are watched unless filter_collections is set.
    pub collections: Vec<String>,

    /// In change_stream mode: limit change stream to these collections.
    /// If empty, watches the entire database.
    pub filter_collections: Option<Vec<String>>,

    /// Polling interval (humantime string). Default: "10s". Used in polling mode.
    pub poll_interval: Option<String>,

    /// Maximum documents per poll cycle per collection. Default: 1000
    pub batch_size: Option<u32>,

    /// Field used for offset tracking in polling mode. Default: "_id"
    /// For timestamp-based tracking, use a field like "updated_at"
    pub tracking_field: Option<String>,

    /// Initial offset value for tracking_field. Default: None (read all)
    pub initial_offset: Option<String>,

    /// Maximum pool connections. Default: 10
    pub max_pool_size: Option<u32>,

    /// In change_stream mode: resume token (hex string of BSON) to restart from.
    /// Populated automatically in persisted state; can be set manually for initial positioning.
    pub resume_token: Option<String>,

    /// Operations to capture in change_stream mode.
    /// Valid values: "insert", "update", "replace", "delete"
    /// Default: ["insert", "update", "replace", "delete"]
    pub capture_operations: Option<Vec<String>>,

    /// Include full document in change stream events for update operations.
    /// Requires MongoDB 6.0+ or Atlas. Default: true
    pub full_document_on_update: Option<bool>,

    /// Whether to include source metadata (collection name, operation type, timestamp)
    /// as top-level fields in the produced JSON. Default: true
    /// When false, the produced JSON contains only the document data.
    pub include_metadata: Option<bool>,

    /// Whether to delete documents after reading in polling mode. Default: false
    pub delete_after_read: Option<bool>,

    /// Field to set to true after reading in polling mode (alternative to delete_after_read).
    /// If set, documents where this field is false/absent are selected.
    pub processed_field: Option<String>,

    /// Enable verbose INFO-level logging. Default: false
    pub verbose_logging: Option<bool>,

    /// Maximum retry attempts for transient errors. Default: 3
    pub max_retries: Option<u32>,

    /// Humantime duration string for base retry delay. Default: "1s"
    pub retry_delay: Option<String>,
}
```

### 6.3 State Struct (persisted via ConnectorState / MessagePack)

```rust
#[derive(Debug, Serialize, Deserialize)]
struct SourceState {
    /// Last poll timestamp (for logging / diagnostics)
    last_poll_time: DateTime<Utc>,

    /// Per-collection offset tracking (polling mode).
    /// Key: collection name, Value: last seen tracking_field value as string
    tracking_offsets: HashMap<String, String>,

    /// Total documents processed across all sessions
    processed_documents: u64,

    /// Change stream resume token (change_stream mode).
    /// This is serialized as a JSON string of the BSON resume token document.
    resume_token_json: Option<String>,
}
```

### 6.4 Constructor (with state restoration)

```rust
impl MongoDBSource {
    pub fn new(id: u32, config: MongoDBSourceConfig, state: Option<ConnectorState>) -> Self {
        let verbose = config.verbose_logging.unwrap_or(false);

        // Restore persisted state if available (mirrors PostgresSource pattern exactly)
        let restored_state = state
            .and_then(|s| s.deserialize::<SourceState>(CONNECTOR_NAME, id))
            .inspect(|s| {
                info!(
                    "Restored state for {CONNECTOR_NAME} connector with ID: {id}. \
                     Tracking offsets: {:?}, processed documents: {}, \
                     has resume token: {}",
                    s.tracking_offsets,
                    s.processed_documents,
                    s.resume_token_json.is_some(),
                );
            });

        // <!-- v2-fix: ISSUE-7 — store as u64 millis -->
        let delay_str = config.retry_delay.as_deref().unwrap_or(DEFAULT_RETRY_DELAY);
        let retry_delay_ms = HumanDuration::from_str(delay_str)
            .map(|d| {
                let dur: Duration = d.into();
                dur.as_millis() as u64
            })
            .unwrap_or(DEFAULT_RETRY_DELAY_MS);

        let interval_str = config.poll_interval.as_deref().unwrap_or("10s");
        let poll_interval = HumanDuration::from_str(interval_str)
            .map(|d| d.into())
            .unwrap_or_else(|_| Duration::from_secs(10));

        MongoDBSource {
            id,
            client: None,
            config,
            state: Mutex::new(restored_state.unwrap_or(SourceState {
                last_poll_time: Utc::now(),
                tracking_offsets: HashMap::new(),
                processed_documents: 0,
                resume_token_json: None,
            })),
            verbose,
            retry_delay_ms,
            poll_interval,
            // <!-- v2-fix: BUG-14 — initialize change_stream field -->
            change_stream: Mutex::new(None),
        }
    }

    fn serialize_state(&self, state: &SourceState) -> Option<ConnectorState> {
        ConnectorState::serialize(state, CONNECTOR_NAME, self.id)
    }
}
```

### 6.5 Source Trait Implementation

```rust
#[async_trait]
impl Source for MongoDBSource {
    async fn open(&mut self) -> Result<(), Error> {
        info!(
            "Opening MongoDB source connector with ID: {}. Mode: {}, Database: {}",
            self.id, self.config.mode, self.config.database
        );

        self.connect().await?;

        match self.config.mode.as_str() {
            "change_stream" => {
                // Verify change stream is supported (requires replica set)
                self.verify_change_stream_support().await?;
                // <!-- v2-fix: BUG-14 — open the change stream ONCE in open(), not in every poll() -->
                self.open_change_stream().await?;
                info!(
                    "MongoDB change stream mode enabled for connector ID: {}",
                    self.id
                );
            }
            "polling" => {
                info!(
                    "MongoDB polling mode enabled for connector ID: {}. \
                     Poll interval: {:?}",
                    self.id, self.poll_interval
                );
            }
            _ => {
                return Err(Error::InitError(format!(
                    "Invalid mode '{}'. Supported modes: 'polling', 'change_stream'",
                    self.config.mode
                )));
            }
        }

        info!(
            "MongoDB source connector with ID: {} opened successfully",
            self.id
        );
        Ok(())
    }

    async fn poll(&self) -> Result<ProducedMessages, Error> {
        // Mirror PostgresSource: sleep first, then poll
        tokio::time::sleep(self.poll_interval).await;

        let messages = match self.config.mode.as_str() {
            "polling" => self.poll_collections().await?,
            "change_stream" => self.poll_change_stream().await?,
            _ => {
                error!("Invalid mode: {}", self.config.mode);
                return Err(Error::InvalidConfig);
            }
        };

        let state = self.state.lock().await;
        if self.verbose {
            info!(
                "MongoDB source connector ID: {} produced {} messages. Total: {}",
                self.id, messages.len(), state.processed_documents
            );
        } else {
            debug!(
                "MongoDB source connector ID: {} produced {} messages. Total: {}",
                self.id, messages.len(), state.processed_documents
            );
        }

        let persisted_state = self.serialize_state(&state);

        Ok(ProducedMessages {
            schema: Schema::Json,
            messages,
            state: persisted_state,
        })
    }

    async fn close(&mut self) -> Result<(), Error> {
        // <!-- v2-fix: BUG-14 — drop the stored change stream cursor on close -->
        {
            let mut cs = self.change_stream.lock().await;
            *cs = None;
        }
        self.client = None;
        info!("MongoDB client released for source connector ID: {}", self.id);

        let state = self.state.lock().await;
        info!(
            "MongoDB source connector ID: {} closed. Total documents processed: {}",
            self.id, state.processed_documents
        );
        Ok(())
    }
}
```

### 6.6 Polling Mode Implementation

```rust
impl MongoDBSource {
    async fn connect(&mut self) -> Result<(), Error> {
        let uri = &self.config.connection_uri;
        let redacted = redact_connection_uri(uri);
        let max_pool_size = self.config.max_pool_size.unwrap_or(10);

        info!("Connecting to MongoDB (pool size: {max_pool_size}): {redacted}");

        let mut options = ClientOptions::parse(uri)
            .await
            .map_err(|e| Error::InitError(format!("Failed to parse MongoDB URI: {e}")))?;

        options.max_pool_size = Some(max_pool_size);

        let client = Client::with_options(options)
            .map_err(|e| Error::InitError(format!("Failed to create MongoDB client: {e}")))?;

        client
            .database("admin")
            .run_command(doc! { "ping": 1 })
            .await
            .map_err(|e| Error::InitError(format!("MongoDB connectivity test failed: {e}")))?;

        self.client = Some(client);
        info!("Connected to MongoDB with pool size {max_pool_size}");
        Ok(())
    }

    fn get_database(&self) -> Result<Database, Error> {
        let client = self.client.as_ref()
            .ok_or_else(|| Error::InitError("MongoDB client not connected".to_string()))?;
        Ok(client.database(&self.config.database))
    }

    async fn verify_change_stream_support(&self) -> Result<(), Error> {
        let db = self.get_database()?;
        // The hello command returns "setName" if part of a replica set,
        // "isWritablePrimary" on Atlas, or "msg": "isdbgrid" on sharded clusters.
        // All three support change streams.
        let result = db.run_command(doc! { "hello": 1 })
            .await
            .map_err(|e| Error::InitError(format!("Failed to run hello command: {e}")))?;

        let is_replica_set = result.get("setName").is_some();
        let is_mongos = result.get("msg")
            .and_then(|v| v.as_str())
            .map(|s| s == "isdbgrid")
            .unwrap_or(false);
        let is_writable_primary = result.get("isWritablePrimary")
            .and_then(|v| v.as_bool())
            .unwrap_or(false);

        if !is_replica_set && !is_mongos && !is_writable_primary {
            return Err(Error::InitError(
                "MongoDB change streams require a replica set, Atlas, or sharded cluster. \
                 Standalone MongoDB does not support change streams. \
                 Use mode = 'polling' for standalone, or use a replica set.".to_string()
            ));
        }

        info!("MongoDB change stream support verified for connector ID: {}", self.id);
        Ok(())
    }

    async fn poll_collections(&self) -> Result<Vec<ProducedMessage>, Error> {
        let db = self.get_database()?;
        let batch_size = self.config.batch_size.unwrap_or(1000);
        let tracking_field = self.config.tracking_field.as_deref().unwrap_or("_id");
        let include_metadata = self.config.include_metadata.unwrap_or(true);

        let mut messages: Vec<ProducedMessage> = Vec::new();
        let mut state_updates: Vec<(String, String)> = Vec::new();
        let mut total_processed: u64 = 0;
        let mut processed_ids_by_collection: Vec<(String, Vec<String>)> = Vec::new();

        for collection_name in &self.config.collections {
            // Get last offset with minimal lock time
            let last_offset = {
                let state = self.state.lock().await;
                state.tracking_offsets.get(collection_name).cloned()
            };

            let filter = self.build_polling_filter(tracking_field, &last_offset)?;

            let collection = db.collection::<Document>(collection_name);
            // <!-- v2-fix: BUG-2 — use fluent API instead of FindOptions::builder() + with_options() -->
            let mut cursor = with_retry_async(
                || collection
                    .find(filter.clone())
                    .sort(doc! { tracking_field: 1 })   // fluent .sort() instead of FindOptions
                    .limit(batch_size as i64),           // fluent .limit() instead of FindOptions
                self.config.max_retries.unwrap_or(DEFAULT_MAX_RETRIES),
                self.retry_delay_ms,
            )
            .await?;

            let mut max_offset: Option<String> = None;
            let mut processed_ids: Vec<String> = Vec::new();

            use futures::StreamExt;
            while let Some(result) = cursor.next().await {
                let doc = result.map_err(|e| {
                    error!("Error reading document from '{collection_name}': {e}");
                    Error::InvalidRecord
                })?;

                // Track offset from tracking_field
                if let Some(bson_val) = doc.get(tracking_field) {
                    if let Some(s) = bson_to_offset_string(bson_val) {
                        max_offset = Some(s);
                    }
                }

                // Track _id for delete/mark-processed operations
                if let Some(id_val) = doc.get("_id") {
                    if let Some(id_str) = bson_to_offset_string(id_val) {
                        processed_ids.push(id_str);
                    }
                }

                // <!-- v2-fix: ISSUE-22 — include_metadata actually controls output structure -->
                // Build the ChangeRecord JSON — when metadata is false, emit only the raw data
                let record = if include_metadata {
                    MongoChangeRecord {
                        collection_name: Some(collection_name.clone()),
                        operation_type: Some("find".to_string()),
                        timestamp: Some(Utc::now()),
                        data: bson_document_to_json(&doc),
                        old_data: None,
                    }
                } else {
                    // When include_metadata is false, omit envelope fields; emit data only
                    MongoChangeRecord {
                        collection_name: None,
                        operation_type: None,
                        timestamp: None,
                        data: bson_document_to_json(&doc),
                        old_data: None,
                    }
                };

                let payload = simd_json::to_vec(&record)
                    .map_err(|_| Error::InvalidRecord)?;

                messages.push(ProducedMessage {
                    id: Some(Uuid::new_v4().as_u128()),
                    headers: None,
                    checksum: None,
                    timestamp: Some(Utc::now().timestamp_millis() as u64),
                    origin_timestamp: Some(Utc::now().timestamp_millis() as u64),
                    payload,
                });
                total_processed += 1;
            }

            // Mark/delete after read (outside cursor, lock-free DB I/O)
            if !processed_ids.is_empty() {
                processed_ids_by_collection.push((collection_name.clone(), processed_ids));
            }

            if let Some(offset) = max_offset {
                state_updates.push((collection_name.clone(), offset));
            }
        }

        // Handle delete_after_read / mark processed
        for (coll_name, ids) in &processed_ids_by_collection {
            self.mark_or_delete_processed_documents(
                &db, coll_name, ids,
            ).await?;
        }

        // Apply state updates with single lock acquisition
        {
            let mut state = self.state.lock().await;
            state.processed_documents += total_processed;
            for (coll, offset) in state_updates {
                state.tracking_offsets.insert(coll, offset);
            }
            state.last_poll_time = Utc::now();
        }

        Ok(messages)
    }

    fn build_polling_filter(
        &self,
        tracking_field: &str,
        last_offset: &Option<String>,
    ) -> Result<Document, Error> {
        let mut filter = Document::new();

        // Apply offset filter if we have a last seen value
        if let Some(offset) = last_offset {
            filter.insert(
                tracking_field,
                doc! { "$gt": offset_string_to_bson(offset) },
            );
        } else if let Some(initial) = &self.config.initial_offset {
            filter.insert(
                tracking_field,
                doc! { "$gt": offset_string_to_bson(initial) },
            );
        }

        // Add processed_field filter if configured
        if let Some(processed_field) = &self.config.processed_field {
            // Select documents where processed_field is false or missing
            filter.insert(
                processed_field,
                doc! { "$ne": true },
            );
        }

        Ok(filter)
    }

    async fn mark_or_delete_processed_documents(
        &self,
        db: &Database,
        collection_name: &str,
        ids: &[String],
    ) -> Result<(), Error> {
        if ids.is_empty() {
            return Ok(());
        }

        let id_bsons: Vec<Bson> = ids.iter()
            .map(|id| offset_string_to_bson(id))
            .collect();

        let collection = db.collection::<Document>(collection_name);
        let filter = doc! { "_id": { "$in": id_bsons } };

        if self.config.delete_after_read.unwrap_or(false) {
            collection.delete_many(filter)
                .await
                .map_err(|e| {
                    error!("Failed to delete processed documents from '{collection_name}': {e}");
                    Error::InvalidRecord
                })?;
        } else if let Some(processed_field) = &self.config.processed_field {
            let update = doc! { "$set": { processed_field: true } };
            collection.update_many(filter, update)
                .await
                .map_err(|e| {
                    error!("Failed to mark documents as processed in '{collection_name}': {e}");
                    Error::InvalidRecord
                })?;
        }

        Ok(())
    }
}
```

### 6.7 Change Stream Implementation

```rust
impl MongoDBSource {
    /// Open the change stream cursor and store it in `self.change_stream`.
    /// Called once from `open()`. On error during `poll_change_stream()`, the cursor
    /// is replaced by calling this method again.
    // <!-- v2-fix: BUG-14 — persistent cursor, opened in open() not on every poll() -->
    // <!-- v2-fix: BUG-2 — fluent API for watch() -->
    // <!-- v2-fix: BUG-3 — resume_after chained on watch() builder, not set on ChangeStreamOptions -->
    async fn open_change_stream(&self) -> Result<(), Error> {
        let db = self.get_database()?;
        let full_doc = self.config.full_document_on_update.unwrap_or(true);
        let batch_size = self.config.batch_size.unwrap_or(1000) as u32;

        let capture_ops: Vec<String> = self.config.capture_operations
            .as_ref()
            .map(|ops| ops.iter().map(|s| s.to_lowercase()).collect())
            .unwrap_or_else(|| vec![
                "insert".to_string(),
                "update".to_string(),
                "replace".to_string(),
                "delete".to_string(),
            ]);

        // Retrieve resume token from state (minimal lock time)
        let resume_token_json = {
            let state = self.state.lock().await;
            state.resume_token_json.clone()
        };

        // Build pipeline to filter by operation type and optionally by collection
        let pipeline = self.build_change_stream_pipeline(&capture_ops);

        // <!-- v2-fix: BUG-2 — fluent builder API. No ChangeStreamOptions struct. -->
        // Chain options directly on db.watch():
        let mut watch_builder = db
            .watch()
            .pipeline(pipeline)
            .batch_size(batch_size);                    // fluent .batch_size()

        if full_doc {
            // <!-- v2-fix: BUG-4 — FullDocumentType::UpdateLookup is the correct variant -->
            watch_builder = watch_builder.full_document(FullDocumentType::UpdateLookup);
        }

        // <!-- v2-fix: BUG-3 — chain .resume_after() directly on the builder, not on options struct -->
        if let Some(token_json) = &resume_token_json {
            match serde_json::from_str::<serde_json::Value>(token_json) {
                Ok(json_val) => {
                    match mongodb::bson::to_document(&json_val) {
                        Ok(token_doc) => {
                            watch_builder = watch_builder.resume_after(token_doc);
                            info!(
                                "MongoDB change stream resuming from saved token for connector ID: {}",
                                self.id
                            );
                        }
                        Err(e) => {
                            warn!(
                                "Failed to parse saved resume token, starting fresh: {e}"
                            );
                        }
                    }
                }
                Err(e) => {
                    warn!("Failed to deserialize resume token JSON, starting fresh: {e}");
                }
            }
        }

        let change_stream = watch_builder
            .await
            .map_err(|e| Error::InitError(format!("Failed to open change stream: {e}")))?;

        let mut cs = self.change_stream.lock().await;
        *cs = Some(change_stream);
        Ok(())
    }

    async fn poll_change_stream(&self) -> Result<Vec<ProducedMessage>, Error> {
        // <!-- v2-fix: BUG-14 — drain the existing cursor; re-open on error -->
        let include_metadata = self.config.include_metadata.unwrap_or(true);
        let batch_size = self.config.batch_size.unwrap_or(1000) as usize;

        let mut messages: Vec<ProducedMessage> = Vec::new();
        let mut last_resume_token: Option<String> = None;

        // Drain available events up to batch_size without blocking on empty stream
        use futures::StreamExt;

        let mut cs_guard = self.change_stream.lock().await;
        let change_stream = match cs_guard.as_mut() {
            Some(cs) => cs,
            None => {
                // Should not happen if open() succeeded, but handle gracefully
                error!("Change stream not initialized for connector ID: {}", self.id);
                return Err(Error::InitError("Change stream not initialized".to_string()));
            }
        };

        while messages.len() < batch_size {
            // Use timeout to avoid blocking indefinitely when the stream has no new events
            match tokio::time::timeout(
                Duration::from_millis(100),
                change_stream.next(),
            ).await {
                Ok(Some(Ok(event))) => {
                    // Save resume token
                    if let Some(token) = &event.id {
                        match serde_json::to_string(
                            &mongodb::bson::from_document::<serde_json::Value>(token.clone())
                                .unwrap_or(serde_json::Value::Null)
                        ) {
                            Ok(token_str) => last_resume_token = Some(token_str),
                            Err(_) => {}
                        }
                    }

                    if let Some(msg) = self.change_event_to_message(
                        &event, include_metadata,
                    )? {
                        messages.push(msg);
                    }
                }
                Ok(Some(Err(e))) => {
                    error!("Change stream error for connector ID {}: {e}", self.id);
                    // Drop the broken cursor so open_change_stream() will create a new one
                    *cs_guard = None;
                    drop(cs_guard);
                    if is_transient_mongodb_error(&e) {
                        // Re-open the cursor and return what we have; runtime will call poll() again
                        warn!("Transient change stream error; re-opening cursor");
                        self.open_change_stream().await?;
                        break;
                    }
                    return Err(Error::InvalidRecord);
                }
                Ok(None) => break, // Stream exhausted (should not happen with watch)
                Err(_) => break,   // Timeout — no more events available right now
            }
        }

        // Update resume token in state
        if let Some(token) = last_resume_token {
            let mut state = self.state.lock().await;
            state.resume_token_json = Some(token);
            state.processed_documents += messages.len() as u64;
            state.last_poll_time = Utc::now();
        } else if !messages.is_empty() {
            let mut state = self.state.lock().await;
            state.processed_documents += messages.len() as u64;
            state.last_poll_time = Utc::now();
        }

        Ok(messages)
    }

    fn build_change_stream_pipeline(&self, capture_ops: &[String]) -> Vec<Document> {
        let mut pipeline = Vec::new();

        // Filter by operation type
        let op_types: Vec<Bson> = capture_ops.iter()
            .map(|op| Bson::String(op.clone()))
            .collect();
        pipeline.push(doc! {
            "$match": {
                "operationType": { "$in": op_types }
            }
        });

        // If filter_collections is set, add a filter on ns.coll
        if let Some(ref collections) = self.config.filter_collections {
            if !collections.is_empty() {
                let coll_bsons: Vec<Bson> = collections.iter()
                    .map(|c| Bson::String(c.clone()))
                    .collect();
                pipeline.push(doc! {
                    "$match": {
                        "ns.coll": { "$in": coll_bsons }
                    }
                });
            }
        }

        pipeline
    }

    fn change_event_to_message(
        &self,
        event: &ChangeStreamEvent<Document>,
        include_metadata: bool,
    ) -> Result<Option<ProducedMessage>, Error> {
        let operation_type = match &event.operation_type {
            OperationType::Insert => "insert",
            OperationType::Update => "update",
            OperationType::Replace => "replace",
            OperationType::Delete => "delete",
            OperationType::Invalidate => return Ok(None), // stream invalidated
            OperationType::Drop => return Ok(None),
            OperationType::DropDatabase => return Ok(None),
            OperationType::Rename => return Ok(None),
            _ => return Ok(None),
        };

        let collection_name = event.ns.as_ref()
            .and_then(|ns| ns.coll.as_deref())
            .unwrap_or("unknown")
            .to_string();

        let data = if let Some(full_doc) = &event.full_document {
            bson_document_to_json(full_doc)
        } else if let Some(doc_key) = &event.document_key {
            // For deletes: only the _id is available
            bson_document_to_json(doc_key)
        } else {
            serde_json::Value::Null
        };

        let old_data = event.full_document_before_change.as_ref()
            .map(|d| bson_document_to_json(d));

        // <!-- v2-fix: ISSUE-22 — include_metadata controls the output structure -->
        let record = if include_metadata {
            MongoChangeRecord {
                collection_name: Some(collection_name.clone()),
                operation_type: Some(operation_type.to_string()),
                timestamp: Some(event.wall_time
                    .map(|t| DateTime::from_timestamp_millis(t.timestamp_millis()))
                    .flatten()
                    .unwrap_or_else(Utc::now)),
                data,
                old_data,
            }
        } else {
            // When metadata is disabled, emit only the document data
            MongoChangeRecord {
                collection_name: None,
                operation_type: None,
                timestamp: None,
                data,
                old_data: None,
            }
        };

        let payload = simd_json::to_vec(&record)
            .map_err(|_| Error::InvalidRecord)?;

        Ok(Some(ProducedMessage {
            id: Some(Uuid::new_v4().as_u128()),
            headers: None,
            checksum: None,
            timestamp: Some(Utc::now().timestamp_millis() as u64),
            origin_timestamp: Some(Utc::now().timestamp_millis() as u64),
            payload,
        }))
    }
}
```

### 6.8 MongoChangeRecord (output schema)

```rust
/// The JSON schema for every message produced by MongoDBSource.
/// Mirrors PostgresSource's DatabaseRecord struct.
///
/// Fields are Option<T> because include_metadata = false omits the envelope fields,
/// leaving only `data` (and optionally `old_data`).
// <!-- v2-fix: ISSUE-22 — fields are Option<T> so include_metadata can actually omit them -->
#[derive(Debug, Serialize, Deserialize)]
pub struct MongoChangeRecord {
    /// Collection the document came from. None when include_metadata = false.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub collection_name: Option<String>,
    /// "insert", "update", "replace", "delete", "find" (polling mode).
    /// None when include_metadata = false.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub operation_type: Option<String>,
    /// Timestamp of the event. None when include_metadata = false.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub timestamp: Option<DateTime<Utc>>,
    /// Full document (or document key for deletes)
    pub data: serde_json::Value,
    /// Previous version of the document (change stream update events only)
    #[serde(skip_serializing_if = "Option::is_none")]
    pub old_data: Option<serde_json::Value>,
}
```

### 6.9 BSON helper functions

```rust
/// Convert a BSON value to a string suitable for offset tracking
fn bson_to_offset_string(bson: &Bson) -> Option<String> {
    match bson {
        Bson::Int32(n) => Some(n.to_string()),
        Bson::Int64(n) => Some(n.to_string()),
        Bson::Double(f) => Some(f.to_string()),
        Bson::String(s) => Some(s.clone()),
        Bson::ObjectId(oid) => Some(oid.to_hex()),
        Bson::DateTime(dt) => Some(dt.timestamp_millis().to_string()),
        _ => None,
    }
}

/// Convert an offset string back to BSON for use in a query filter.
///
/// Tries in order: integer, ObjectId (24-char hex), ISO 8601 datetime, plain string.
// <!-- v2-fix: ISSUE-23 — try parsing as datetime before falling back to string -->
fn offset_string_to_bson(s: &str) -> Bson {
    // Try integer first
    if let Ok(n) = s.parse::<i64>() {
        return Bson::Int64(n);
    }
    // Try ObjectId (24-char hex)
    if s.len() == 24 {
        if let Ok(oid) = mongodb::bson::oid::ObjectId::parse_str(s) {
            return Bson::ObjectId(oid);
        }
    }
    // Try ISO 8601 datetime — needed for tracking_field = "created_at" / "updated_at"
    if let Ok(dt) = chrono::DateTime::parse_from_rfc3339(s) {
        return Bson::DateTime(BsonDateTime::from_millis(dt.timestamp_millis()));
    }
    // Fall back to string
    Bson::String(s.to_string())
}

/// Convert a BSON Document to a serde_json::Value
fn bson_document_to_json(doc: &Document) -> serde_json::Value {
    // mongodb::bson provides Serialize impls, route through serde_json
    match serde_json::to_value(doc) {
        Ok(val) => val,
        Err(_) => serde_json::Value::Null,
    }
}
```

### 6.10 Retry helper for async MongoDB operations

```rust
/// Retry an async MongoDB operation with exponential linear backoff.
///
/// Signature matches the real PostgresSource `with_retry` pattern:
/// `delay_ms: u64` and `Duration::from_millis(delay_ms * attempts)`.
// <!-- v2-fix: ISSUE-7 — changed delay: Duration to delay_ms: u64 to match PostgresSource -->
async fn with_retry_async<T, F, Fut>(
    operation: F,
    max_retries: u32,
    delay_ms: u64,
) -> Result<T, Error>
where
    F: Fn() -> Fut,
    Fut: std::future::Future<Output = Result<T, mongodb::error::Error>>,
{
    let mut attempts = 0u32;
    loop {
        match operation().await {
            Ok(result) => return Ok(result),
            Err(e) => {
                attempts += 1;
                if attempts >= max_retries || !is_transient_mongodb_error(&e) {
                    error!("MongoDB operation failed after {attempts} attempts: {e}");
                    return Err(Error::InvalidRecord);
                }
                warn!(
                    "Transient MongoDB error (attempt {attempts}/{max_retries}): {e}. Retrying..."
                );
                tokio::time::sleep(Duration::from_millis(delay_ms * attempts as u64)).await;
            }
        }
    }
}
```

---

## 7. Config Structs and TOML Examples

### 7.1 MongoDBSink config.toml

```toml
# core/connectors/sinks/mongodb_sink/config.toml

type = "sink"
key = "mongodb"
enabled = true
version = 0
name = "MongoDB sink"
path = "../../target/release/libiggy_connector_mongodb_sink"
verbose = false

[[streams]]
stream = "user_events"
topics = ["users", "orders"]
schema = "json"
batch_length = 100
poll_interval = "5ms"
consumer_group = "mongodb_sink"

[plugin_config]
connection_uri = "mongodb://user:pass@localhost:27017"
database = "iggy_data"
collection = "{topic}"           # Template: uses the Iggy topic name as collection name
batch_size = 100
max_pool_size = 10
include_metadata = true
include_checksum = true
include_origin_timestamp = true
payload_format = "document"      # "document" | "binary" | "string"
ordered_inserts = false          # unordered = higher throughput, tolerates dup key errors
verbose_logging = false
max_retries = 3
retry_delay = "1s"
```

**Minimal config (simplest possible)**:

```toml
type = "sink"
key = "mongodb"
enabled = true
version = 0
name = "MongoDB sink"
path = "../../target/release/libiggy_connector_mongodb_sink"

[[streams]]
stream = "events"
topics = ["raw"]
schema = "raw"
batch_length = 50

[plugin_config]
connection_uri = "mongodb://localhost:27017"
database = "iggy"
```

**Config with fixed collection name and binary payload**:

```toml
type = "sink"
key = "mongodb"
enabled = true
version = 0
name = "MongoDB sink binary"
path = "../../target/release/libiggy_connector_mongodb_sink"

[[streams]]
stream = "binary_data"
topics = ["frames"]
schema = "raw"
batch_length = 200
poll_interval = "1ms"

[plugin_config]
connection_uri = "mongodb://localhost:27017"
database = "sensors"
collection = "raw_frames"
batch_size = 200
payload_format = "binary"
include_metadata = true
include_checksum = false
include_origin_timestamp = false
```

### 7.2 MongoDBSource config.toml — Polling mode

```toml
# core/connectors/sources/mongodb_source/config.toml

type = "source"
key = "mongodb"
enabled = true
version = 0
name = "MongoDB source"
path = "../../target/release/libiggy_connector_mongodb_source"
verbose = false

[[streams]]
stream = "mongodb_events"
topic = "documents"
schema = "json"
batch_length = 100

[plugin_config]
connection_uri = "mongodb://user:pass@localhost:27017"
database = "app_db"
mode = "polling"
collections = ["users", "orders", "products"]
poll_interval = "5s"
batch_size = 1000
tracking_field = "_id"
initial_offset = ""              # Empty = read all documents on first run
max_pool_size = 10
include_metadata = true
verbose_logging = false
max_retries = 3
retry_delay = "1s"
```

**Polling mode with timestamp tracking and delete-after-read**:

```toml
[plugin_config]
connection_uri = "mongodb://localhost:27017"
database = "queue_db"
mode = "polling"
collections = ["jobs"]
poll_interval = "500ms"
batch_size = 50
tracking_field = "created_at"    # ISO date field
initial_offset = "2024-01-01T00:00:00Z"
delete_after_read = true         # Remove documents after they are read
include_metadata = true
```

**Polling mode with processed_field (soft delete)**:

```toml
[plugin_config]
connection_uri = "mongodb://localhost:27017"
database = "app_db"
mode = "polling"
collections = ["events"]
poll_interval = "10s"
batch_size = 500
tracking_field = "updated_at"
processed_field = "iggy_processed"  # Set to true after reading
include_metadata = false
```

### 7.3 MongoDBSource config.toml — Change Stream mode

```toml
type = "source"
key = "mongodb"
enabled = true
version = 0
name = "MongoDB CDC source"
path = "../../target/release/libiggy_connector_mongodb_source"
verbose = false

[[streams]]
stream = "mongo_cdc"
topic = "changes"
schema = "json"
batch_length = 500

[plugin_config]
connection_uri = "mongodb://user:pass@replica-set-host:27017/?replicaSet=rs0"
database = "app_db"
mode = "change_stream"
# filter_collections = ["users", "orders"]  # Optional: watch specific collections
capture_operations = ["insert", "update", "replace", "delete"]
batch_size = 500
full_document_on_update = true   # Requires MongoDB 6.0+ for pre-image; post-image always available
include_metadata = true
max_pool_size = 5
verbose_logging = false
max_retries = 3
retry_delay = "2s"
```

**Change stream watching only inserts, with collection filtering**:

```toml
[plugin_config]
connection_uri = "mongodb+srv://user:pass@cluster.mongodb.net/?appName=iggy"
database = "ecommerce"
mode = "change_stream"
filter_collections = ["orders"]
capture_operations = ["insert"]
batch_size = 200
full_document_on_update = false
include_metadata = true
```

---

## 8. Cargo.toml Dependencies

### 8.1 MongoDBSink Cargo.toml

```toml
# core/connectors/sinks/mongodb_sink/Cargo.toml

[package]
name = "iggy_connector_mongodb_sink"
version = "0.2.2-edge.1"
description = "Iggy MongoDB sink connector for storing stream messages into MongoDB collections"
edition = "2024"
license = "Apache-2.0"
keywords = ["iggy", "messaging", "streaming", "mongodb", "sink"]
categories = ["command-line-utilities", "database", "network-programming"]
homepage = "https://iggy.apache.org"
documentation = "https://iggy.apache.org/docs"
repository = "https://github.com/apache/iggy"
readme = "../../README.md"

# <!-- v2-fix: ISSUE-16 — prost added to match PostgresSink's cargo-machete ignored list -->
[package.metadata.cargo-machete]
ignored = ["dashmap", "once_cell", "futures", "simd-json", "prost"]

[lib]
crate-type = ["cdylib", "lib"]

[dependencies]
async-trait     = { workspace = true }
dashmap         = { workspace = true }
futures         = { workspace = true }
humantime       = { workspace = true }
iggy_common     = { workspace = true }
iggy_connector_sdk = { workspace = true }
once_cell       = { workspace = true }
serde           = { workspace = true }
serde_json      = { workspace = true }
simd-json       = { workspace = true }
tokio           = { workspace = true }
tracing         = { workspace = true }
mongodb         = { version = "3", features = ["tokio-runtime"] }
```

**Note on the `mongodb` crate version**: The mongodb crate v3.x (released 2024-06-25) is the
current stable API. It uses a fluent builder pattern instead of the `with_options()` approach from
v2.x. The `tokio-runtime` feature enables the async client. The latest version as of 2026-02-03 is
v3.5.1.

For workspace.toml, add:
```toml
[workspace.dependencies]
mongodb = { version = "3", features = ["tokio-runtime"] }
```

### 8.2 MongoDBSource Cargo.toml

```toml
# core/connectors/sources/mongodb_source/Cargo.toml

[package]
name = "iggy_connector_mongodb_source"
version = "0.2.2-edge.1"
description = "Iggy MongoDB source connector supporting polling and Change Stream CDC"
edition = "2024"
license = "Apache-2.0"
keywords = ["iggy", "messaging", "streaming", "mongodb", "cdc"]
categories = ["command-line-utilities", "database", "network-programming"]
homepage = "https://iggy.apache.org"
documentation = "https://iggy.apache.org/docs"
repository = "https://github.com/apache/iggy"
readme = "../../README.md"

# <!-- v2-fix: ISSUE-16 — prost added to match PostgresSink's cargo-machete ignored list -->
[package.metadata.cargo-machete]
ignored = ["dashmap", "once_cell", "futures", "simd-json", "prost"]

[lib]
crate-type = ["cdylib", "lib"]

[dependencies]
async-trait     = { workspace = true }
dashmap         = { workspace = true }
futures         = { workspace = true }
humantime       = { workspace = true }
iggy_common     = { workspace = true }
iggy_connector_sdk = { workspace = true }
once_cell       = { workspace = true }
serde           = { workspace = true }
serde_json      = { workspace = true }
simd-json       = { workspace = true }
tokio           = { workspace = true }
tracing         = { workspace = true }
uuid            = { workspace = true }
mongodb         = { version = "3", features = ["tokio-runtime"] }
```

---

## 9. Error Handling Strategy

The approach mirrors PostgresSink / PostgresSource exactly. All errors are mapped to variants of
`iggy_connector_sdk::Error`.

### Error mapping table

| MongoDB error category | Maps to `Error` variant | Retry? |
|------------------------|------------------------|--------|
| URI parse failure | `Error::InitError(...)` | No |
| Connection refused / timeout | `Error::InitError(...)` on open; `Error::Connection(...)` on operation | Yes |
| Ping failure | `Error::InitError(...)` | No |
| Duplicate key (11000) | `Error::CannotStoreData(...)` | No |
| WriteConcernError | `Error::CannotStoreData(...)` | Yes |
| IO / network error | `Error::CannotStoreData(...)` on sink; `Error::InvalidRecord` on source | Yes |
| Pool cleared / selection timeout | `Error::CannotStoreData(...)` | Yes |
| JSON parse failure in payload | `Error::InvalidJsonPayload` | No |
| UTF-8 decode failure in payload | `Error::InvalidTextPayload` | No |
| BSON serialization failure | `Error::Serialization(...)` | No |
| Change stream invalidated | Logged as warning, return empty batch | No |
| Client not initialized | `Error::InitError("MongoDB client not connected")` | No |

### Transient error detection

The `is_transient_mongodb_error()` function (defined in section 5.8) covers:
- Network / IO errors
- Connection pool cleared
- Server selection timeout
- Write concern errors
- Non-duplicate-key write errors

Duplicate key errors (code 11000) are NOT transient: the message has already been inserted,
or there is a genuine ID conflict. The sink should skip these (log as warning) rather than retry.

### Handling duplicate _id on retry

When a batch insert is retried (e.g., after a WriteConcernError), some documents may have already
been written. With `ordered_inserts = false` (the default), MongoDB will insert all documents that
don't conflict and report errors for duplicates. The connector should:

1. Log duplicate key errors as warnings, not errors.
2. Count them in `insertion_errors` state.
3. Not propagate them as fatal errors.

Implementation detail: inspect the `BulkWriteError` returned by `insert_many` for code 11000
entries and filter them out before deciding whether to surface an error to the runtime.

### Error propagation from process_messages (v2 fix)

In v2, `process_messages` returns `Err` when any batch fails after all retry attempts. This
matches the behavior of the real PostgresSink. In v1, errors were swallowed and `Ok(())` was
returned unconditionally — this caused the runtime to believe a batch had succeeded when it had
actually failed to insert. The fix ensures the runtime can detect failures and apply backpressure
or alerting.

---

## 10. State Management and Offset Tracking

### Sink state

The sink tracks two counters: `messages_processed` and `insertion_errors`. These are held in
`Mutex<SinkState>` and are **not persisted** (sinks don't receive state from the runtime). They
are only used for logging at close time. This matches PostgresSink behavior exactly.

### Source state

The source persists `SourceState` via `ConnectorState` (MessagePack bytes). This is returned in
`ProducedMessages.state` from every `poll()` call. The runtime stores this state and passes it
back as the `state_ptr` / `state_len` arguments to `open()` on restart.

**Polling mode offset tracking:**

- `tracking_offsets: HashMap<String, String>` — one entry per collection.
- Key = collection name, Value = last seen `tracking_field` value as a string.
- On each poll cycle, the maximum value seen for `tracking_field` across all documents in a batch
  replaces the stored offset.
- On restart, the query filter adds `{ tracking_field: { $gt: last_offset } }`.
- ObjectIds are handled specially: `ObjectId::from_hex()` for parsing, `.to_hex()` for storage.
  This ensures correct ordering since MongoDB ObjectIds embed a timestamp.
- DateTime fields (e.g., `created_at`, `updated_at`) are stored as millis strings via
  `bson_to_offset_string` and parsed back to `BsonDateTime` via `offset_string_to_bson`'s
  RFC 3339 fallback path (v2 fix for ISSUE-23).

**Change stream offset tracking:**

- `resume_token_json: Option<String>` — serialized form of the change stream resume token.
- The resume token is a BSON document (`_id` field of each change event).
- It is serialized to JSON (via `serde_json::to_string`) for storage in `SourceState`.
- On restart, it is deserialized back to a BSON Document and passed via `.resume_after()` on
  the `watch()` fluent builder (v2 fix for BUG-3 — was previously set as a field on the
  `ChangeStreamOptions` struct).
- Resume tokens are opaque and durable: they work even after the change stream event has
  been purged from the oplog, as long as the token is within the oplog retention window.

**Change stream cursor lifetime (v2 fix for BUG-14):**

The change stream cursor is opened **once** in `open()` via `open_change_stream()` and stored in
`self.change_stream: Mutex<Option<ChangeStream<Document>>>`. Each `poll_change_stream()` call
drains the existing cursor up to `batch_size` events. If the cursor returns an error, it is
replaced by calling `open_change_stream()` again. This avoids the expensive reconnect-per-poll
pattern in v1 and is consistent with how PostgresSource reuses its replication connection.

**Critical design principle (from PostgresSource):**

Database I/O must happen **outside** the `Mutex<SourceState>` lock. The lock is acquired only
for reading the last offset (at the start) and for writing the new offset (at the end). This
matches the explicit comment in PostgresSource:

```rust
// Get last offset with minimal lock time
let last_offset = {
    let state = self.state.lock().await;
    state.tracking_offsets.get(collection_name).cloned()
};
// ... Database I/O without holding the lock ...
// Apply all state updates with a single lock acquisition
{
    let mut state = self.state.lock().await;
    state.tracking_offsets.insert(collection, offset);
}
```

---

## 11. Retry Logic

The retry pattern is identical to PostgresSink's `execute_batch_insert_with_retry`:

```rust
let mut attempts = 0u32;
loop {
    match operation().await {
        Ok(_) => return Ok(()),
        Err(e) => {
            attempts += 1;
            let is_transient = is_transient_mongodb_error(&e);
            if !is_transient || attempts >= max_retries {
                error!("Failed after {attempts} attempts: {e}");
                return Err(Error::CannotStoreData(...));
            }
            warn!(
                "Transient error (attempt {attempts}/{max_retries}): {e}. Retrying..."
            );
            // Linear multiplicative backoff: delay_ms * attempt number (1x, 2x, 3x)
            // Matches PostgresSource: Duration::from_millis(delay_ms * attempts as u64)
            tokio::time::sleep(Duration::from_millis(retry_delay_ms * attempts as u64)).await;
        }
    }
}
```

Key points:
- `retry_delay_ms` is parsed from a humantime string (e.g., `"1s"`, `"500ms"`) in the constructor
  and stored as `u64` milliseconds, matching the real PostgresSource `with_retry` signature.
- Backoff is linear multiplicative (`delay_ms * attempts`), exactly as PostgresSource uses it.
- Non-transient errors fail immediately without retry.
- The `max_retries` default is `3` (same as both Postgres connectors).
- The `retry_delay` default is `"1s"` (same as both Postgres connectors).

---

## 12. Testing Strategy

### Unit tests (no running MongoDB required)

Follow the PostgresSink test patterns exactly. All unit tests go in a `#[cfg(test)]` module at
the bottom of `lib.rs`.

```rust
#[cfg(test)]
mod tests {
    use super::*;

    fn test_sink_config() -> MongoDBSinkConfig {
        MongoDBSinkConfig {
            connection_uri: "mongodb://localhost:27017".to_string(),
            database: "test_db".to_string(),
            collection: None,
            batch_size: Some(100),
            max_pool_size: None,
            include_metadata: None,
            include_checksum: None,
            include_origin_timestamp: None,
            payload_format: None,
            ordered_inserts: None,
            verbose_logging: None,
            max_retries: None,
            retry_delay: None,
        }
    }

    fn test_source_config() -> MongoDBSourceConfig {
        MongoDBSourceConfig {
            connection_uri: "mongodb://localhost:27017".to_string(),
            database: "test_db".to_string(),
            mode: "polling".to_string(),
            collections: vec!["users".to_string()],
            filter_collections: None,
            poll_interval: Some("5s".to_string()),
            batch_size: Some(100),
            tracking_field: Some("_id".to_string()),
            initial_offset: None,
            max_pool_size: None,
            resume_token: None,
            capture_operations: None,
            full_document_on_update: None,
            include_metadata: None,
            delete_after_read: None,
            processed_field: None,
            verbose_logging: None,
            max_retries: None,
            retry_delay: None,
        }
    }
```

**Required unit tests for MongoDBSink:**

```rust
    #[test]
    fn given_document_format_should_return_document() {
        assert_eq!(PayloadFormat::from_config(Some("document")), PayloadFormat::Document);
        assert_eq!(PayloadFormat::from_config(None), PayloadFormat::Document);
    }

    #[test]
    fn given_binary_format_should_return_binary() {
        assert_eq!(PayloadFormat::from_config(Some("binary")), PayloadFormat::Binary);
        assert_eq!(PayloadFormat::from_config(Some("raw")), PayloadFormat::Binary);
    }

    #[test]
    fn given_text_format_should_return_text() {
        assert_eq!(PayloadFormat::from_config(Some("string")), PayloadFormat::Text);
        assert_eq!(PayloadFormat::from_config(Some("text")), PayloadFormat::Text);
    }

    #[test]
    fn given_default_config_should_use_default_retries() {
        let sink = MongoDBSink::new(1, test_sink_config());
        assert_eq!(sink.config.max_retries.unwrap_or(DEFAULT_MAX_RETRIES), DEFAULT_MAX_RETRIES);
    }

    #[test]
    fn given_custom_retry_delay_should_parse_humantime() {
        let mut config = test_sink_config();
        config.retry_delay = Some("500ms".to_string());
        let sink = MongoDBSink::new(1, config);
        assert_eq!(sink.retry_delay_ms, 500u64);
    }

    #[test]
    fn given_verbose_logging_enabled_should_set_verbose_flag() {
        let mut config = test_sink_config();
        config.verbose_logging = Some(true);
        let sink = MongoDBSink::new(1, config);
        assert!(sink.verbose);
    }

    #[test]
    fn given_collection_template_with_topic_should_resolve_correctly() {
        let mut config = test_sink_config();
        config.collection = Some("{topic}".to_string());
        let sink = MongoDBSink::new(1, config);
        let metadata = TopicMetadata {
            stream: "my_stream".to_string(),
            topic: "my_topic".to_string(),
        };
        assert_eq!(sink.resolve_collection_name(&metadata), "my_topic");
    }

    #[test]
    fn given_collection_template_with_stream_should_resolve_correctly() {
        let mut config = test_sink_config();
        config.collection = Some("{stream}_{topic}".to_string());
        let sink = MongoDBSink::new(1, config);
        let metadata = TopicMetadata {
            stream: "events".to_string(),
            topic: "users".to_string(),
        };
        assert_eq!(sink.resolve_collection_name(&metadata), "events_users");
    }

    #[test]
    fn given_no_collection_config_should_default_to_topic_name() {
        let sink = MongoDBSink::new(1, test_sink_config());
        let metadata = TopicMetadata {
            stream: "s".to_string(),
            topic: "orders".to_string(),
        };
        assert_eq!(sink.resolve_collection_name(&metadata), "orders");
    }

    #[test]
    fn given_connection_uri_with_credentials_should_redact() {
        let uri = "mongodb://user:password@localhost:27017/db";
        let redacted = redact_connection_uri(uri);
        assert_eq!(redacted, "mongodb://use***");
    }
```

**Required unit tests for MongoDBSource:**

```rust
    #[test]
    fn given_no_offset_and_no_initial_should_return_empty_filter() {
        let src = MongoDBSource::new(1, test_source_config(), None);
        let filter = src.build_polling_filter("_id", &None).unwrap();
        assert!(filter.is_empty());
    }

    #[test]
    fn given_last_offset_should_add_gt_filter() {
        let src = MongoDBSource::new(1, test_source_config(), None);
        let filter = src.build_polling_filter("_id", &Some("100".to_string())).unwrap();
        assert!(filter.contains_key("_id"));
    }

    #[test]
    fn given_processed_field_config_should_add_filter() {
        let mut config = test_source_config();
        config.processed_field = Some("is_processed".to_string());
        let src = MongoDBSource::new(1, config, None);
        let filter = src.build_polling_filter("_id", &None).unwrap();
        assert!(filter.contains_key("is_processed"));
    }

    #[test]
    fn given_no_state_should_start_fresh() {
        let src = MongoDBSource::new(1, test_source_config(), None);
        let rt = tokio::runtime::Runtime::new().unwrap();
        rt.block_on(async {
            let state = src.state.lock().await;
            assert!(state.tracking_offsets.is_empty());
            assert_eq!(state.processed_documents, 0);
            assert!(state.resume_token_json.is_none());
        });
    }

    #[test]
    fn given_persisted_state_should_restore_tracking_offsets() {
        let original_state = SourceState {
            last_poll_time: Utc::now(),
            tracking_offsets: HashMap::from([
                ("users".to_string(), "507f1f77bcf86cd799439011".to_string()),
            ]),
            processed_documents: 1500,
            resume_token_json: None,
        };
        let connector_state = ConnectorState::serialize(
            &original_state, CONNECTOR_NAME, 1
        ).expect("serialize should succeed");

        let src = MongoDBSource::new(1, test_source_config(), Some(connector_state));
        let rt = tokio::runtime::Runtime::new().unwrap();
        rt.block_on(async {
            let state = src.state.lock().await;
            assert_eq!(
                state.tracking_offsets.get("users"),
                Some(&"507f1f77bcf86cd799439011".to_string())
            );
            assert_eq!(state.processed_documents, 1500);
        });
    }

    #[test]
    fn given_numeric_string_should_parse_to_int64_bson() {
        let bson = offset_string_to_bson("42");
        assert_eq!(bson, Bson::Int64(42));
    }

    #[test]
    fn given_objectid_hex_should_parse_to_objectid_bson() {
        let hex = "507f1f77bcf86cd799439011";
        let bson = offset_string_to_bson(hex);
        assert!(matches!(bson, Bson::ObjectId(_)));
    }

    #[test]
    // <!-- v2-fix: ISSUE-23 — new test for datetime offset parsing -->
    fn given_iso8601_datetime_string_should_parse_to_bson_datetime() {
        let dt_str = "2024-01-01T00:00:00Z";
        let bson = offset_string_to_bson(dt_str);
        assert!(matches!(bson, Bson::DateTime(_)),
            "Expected BsonDateTime, got: {bson:?}");
    }

    #[test]
    fn given_arbitrary_string_should_stay_as_string_bson() {
        // A string that is not a number, not a 24-char hex, not an ISO date
        let bson = offset_string_to_bson("some-non-date-string");
        assert!(matches!(bson, Bson::String(_)));
    }

    #[test]
    // <!-- v2-fix: ISSUE-22 — test that include_metadata = false omits envelope fields -->
    fn given_include_metadata_false_should_omit_envelope_fields() {
        let record = MongoChangeRecord {
            collection_name: None,
            operation_type: None,
            timestamp: None,
            data: serde_json::json!({"_id": "123"}),
            old_data: None,
        };
        let json = serde_json::to_string(&record).unwrap();
        // Envelope fields should be absent (skip_serializing_if = None)
        assert!(!json.contains("collection_name"));
        assert!(!json.contains("operation_type"));
        assert!(!json.contains("timestamp"));
        assert!(json.contains("data"));
    }
```

### Integration tests

Integration tests require a running MongoDB instance. Place them in
`core/connectors/sinks/mongodb_sink/tests/integration.rs` and
`core/connectors/sources/mongodb_source/tests/integration.rs`.

```toml
# Cargo.toml additions for integration tests:
[[test]]
name = "integration"
path = "tests/integration.rs"
required-features = ["integration-tests"]

[features]
integration-tests = []
```

Run with:
```bash
MONGODB_TEST_URI="mongodb://localhost:27017" \
  cargo test --features integration-tests -- --test-threads=1
```

**Integration test checklist:**

For the sink:
- `test_sink_open_and_close_should_connect_and_disconnect`
- `test_sink_consume_json_should_insert_documents`
- `test_sink_consume_binary_should_insert_binary_documents`
- `test_sink_consume_batch_should_insert_all_documents`
- `test_sink_duplicate_id_should_not_fail_with_unordered_inserts`
- `test_sink_metadata_fields_should_be_present_in_document`
- `test_sink_collection_template_should_resolve_dynamically`
- `test_sink_process_messages_should_return_err_on_failed_batch` (v2: BUG-11 regression test)

For the source (polling mode):
- `test_source_polling_should_read_existing_documents`
- `test_source_polling_should_track_offset_and_not_re_read`
- `test_source_polling_delete_after_read_should_remove_documents`
- `test_source_polling_processed_field_should_be_set`
- `test_source_polling_state_persistence_and_restore`
- `test_source_polling_datetime_tracking_field_should_use_bson_datetime_comparison` (v2: ISSUE-23)

For the source (change stream mode — requires replica set):
- `test_source_change_stream_should_receive_insert_events`
- `test_source_change_stream_should_receive_update_events`
- `test_source_change_stream_should_receive_delete_events`
- `test_source_change_stream_should_resume_from_token`
- `test_source_change_stream_invalid_mode_should_fail_on_standalone`
- `test_source_change_stream_cursor_persists_across_poll_calls` (v2: BUG-14 regression test)

---

## 13. File and Directory Layout

```
core/connectors/sinks/mongodb_sink/
├── Cargo.toml
├── config.toml                      # Example configuration
├── README.md                        # Connector-specific documentation
├── src/
│   └── lib.rs                       # All code (single file, matching postgres_sink pattern)
└── tests/
    └── integration.rs               # Integration tests (feature-gated)

core/connectors/sources/mongodb_source/
├── Cargo.toml
├── config.toml                      # Example configuration
├── README.md
├── src/
│   └── lib.rs                       # All code
└── tests/
    └── integration.rs
```

The Cargo workspace at `core/connectors/Cargo.toml` (or root workspace) must add both crates:

```toml
[workspace]
members = [
    # ... existing members ...
    "sinks/mongodb_sink",
    "sources/mongodb_source",
]
```

---

## 14. Implementation Checklist

### Phase 1: MongoDBSink

- [ ] Create `core/connectors/sinks/mongodb_sink/` directory
- [ ] Write `Cargo.toml` (section 8.1) — include `prost` in cargo-machete ignored list
- [ ] Write `src/lib.rs` with Apache 2.0 license header:
  - [ ] `sink_connector!(MongoDBSink)` macro invocation
  - [ ] `MongoDBSinkConfig` struct (section 5.2)
  - [ ] `PayloadFormat` enum and `from_config()` (section 5.4)
  - [ ] `SinkState` struct (section 5.3)
  - [ ] `MongoDBSink::new()` with `retry_delay_ms: u64` field (section 5.5)
  - [ ] `impl Sink for MongoDBSink` — `open()`, `consume()`, `close()` (section 5.6)
  - [ ] `connect()` — parse URI, build ClientOptions, ping (section 5.7)
  - [ ] `resolve_collection_name()` — template substitution (section 5.7)
  - [ ] `process_messages()` — returns Err on failure; only counts successful batches (section 5.7)
  - [ ] `insert_batch()` — build documents, call insert_many (section 5.7)
  - [ ] `build_document()` — metadata fields, payload format handling (section 5.7)
  - [ ] `execute_insert_many_with_retry()` — fluent API, pass `&docs` not `docs.clone()` (section 5.7)
  - [ ] `is_transient_mongodb_error()` — error classification (section 5.8)
  - [ ] `redact_connection_uri()` — credentials redaction (section 5.8)
  - [ ] `micros_to_bson_datetime()` — timestamp conversion (section 5.8)
  - [ ] `#[cfg(test)] mod tests` — all unit tests (section 12)
- [ ] Write `config.toml` (section 7.1)
- [ ] Add to workspace Cargo.toml

### Phase 2: MongoDBSource

- [ ] Create `core/connectors/sources/mongodb_source/` directory
- [ ] Write `Cargo.toml` (section 8.2) — include `prost` in cargo-machete ignored list
- [ ] Write `src/lib.rs` with Apache 2.0 license header:
  - [ ] `source_connector!(MongoDBSource)` macro invocation
  - [ ] `MongoDBSourceConfig` struct (section 6.2)
  - [ ] `SourceState` struct with `Serialize` + `Deserialize` (section 6.3)
  - [ ] `MongoChangeRecord` struct with `Option<T>` envelope fields (section 6.8)
  - [ ] `MongoDBSource` struct with `change_stream: Mutex<Option<ChangeStream<Document>>>` (section 6.1)
  - [ ] `MongoDBSource::new()` with `retry_delay_ms: u64` and `change_stream` field (section 6.4)
  - [ ] `serialize_state()` helper (section 6.4)
  - [ ] `impl Source for MongoDBSource` — `open()` calls `open_change_stream()`; `close()` drops cursor (section 6.5)
  - [ ] `connect()` (section 6.6)
  - [ ] `get_database()` helper (section 6.6)
  - [ ] `verify_change_stream_support()` — check setName, isWritablePrimary, isdbgrid (section 6.6)
  - [ ] `poll_collections()` — fluent find() API, include_metadata controls output structure (section 6.6)
  - [ ] `build_polling_filter()` — filter construction (section 6.6)
  - [ ] `mark_or_delete_processed_documents()` (section 6.6)
  - [ ] `open_change_stream()` — fluent watch() API with .resume_after() chained (section 6.7)
  - [ ] `poll_change_stream()` — drains existing cursor; re-opens on error (section 6.7)
  - [ ] `build_change_stream_pipeline()` — operationType and ns.coll filters (section 6.7)
  - [ ] `change_event_to_message()` — include_metadata controls envelope fields (section 6.7)
  - [ ] `bson_to_offset_string()` (section 6.9)
  - [ ] `offset_string_to_bson()` — try datetime parse before string fallback (section 6.9)
  - [ ] `bson_document_to_json()` (section 6.9)
  - [ ] `with_retry_async()` — takes `delay_ms: u64`, not `Duration` (section 6.10)
  - [ ] `is_transient_mongodb_error()` (reuse from sink or shared module)
  - [ ] `redact_connection_uri()` (reuse)
  - [ ] `#[cfg(test)] mod tests` — all unit tests including v2 additions (section 12)
- [ ] Write `config.toml` (section 7.2, 7.3)
- [ ] Add to workspace Cargo.toml

### Phase 3: Workspace integration

- [ ] Add `mongodb = { version = "3", features = ["tokio-runtime"] }` to workspace dependencies
- [ ] Add both crates to workspace `[members]`
- [ ] Run `cargo build --package iggy_connector_mongodb_sink`
- [ ] Run `cargo build --package iggy_connector_mongodb_source`
- [ ] Run `cargo test --package iggy_connector_mongodb_sink`
- [ ] Run `cargo test --package iggy_connector_mongodb_source`
- [ ] Run `cargo clippy --package iggy_connector_mongodb_sink -- -D warnings`
- [ ] Run `cargo clippy --package iggy_connector_mongodb_source -- -D warnings`
- [ ] Verify both connectors load correctly in the runtime with a `config.toml`

---

## Appendix A: Why Change Streams vs WAL CDC

MongoDB Change Streams (the MongoDB equivalent of PostgreSQL WAL CDC) are fundamentally different
in implementation but serve the same purpose:

| Aspect | PostgreSQL WAL CDC | MongoDB Change Streams |
|--------|-------------------|----------------------|
| Mechanism | Logical replication via `pg_logical_slot_get_changes()` | Oplog tailing via `$changeStream` aggregation |
| Requirement | `wal_level = logical` in `postgresql.conf` | Replica set or Atlas (standalone not supported) |
| Resume | WAL LSN + replication slot | Opaque resume token (BSON document) |
| Pre-image | Requires `REPLICA IDENTITY FULL` | `fullDocumentBeforeChange` (MongoDB 6.0+) |
| Granularity | Table-level via publication | Collection-level via `ns.coll` filter in pipeline |
| Setup | `CREATE PUBLICATION` + `pg_create_logical_replication_slot` | No setup needed; open watch cursor |

The PostgresSource's `setup_cdc()` method creates publications and replication slots in the
database as a prerequisite. For MongoDBSource, there is no equivalent setup step: Change Streams
are opened directly with `db.watch()` using the fluent builder API. The only prerequisite check
is the `verify_change_stream_support()` call in `open()`.

**v3 API note**: In mongodb crate v3, the watch cursor is opened with:
```rust
db.watch()
    .pipeline(pipeline)
    .batch_size(batch_size)
    .full_document(FullDocumentType::UpdateLookup)
    .resume_after(token_doc)
    .await?
```
Not the v2 pattern of `ChangeStreamOptions::builder().field(val).build()` passed to
`.with_options()`.

---

## Appendix B: MongoDB _id and the u128 Message ID

Iggy message IDs are `u128` values. MongoDB's default `_id` type is `ObjectId` (12 bytes / 96
bits). Since u128 is 128 bits, it exceeds ObjectId capacity.

The chosen approach (storing `message.id.to_string()` as a BSON String `_id`) is simple and
correct. Alternative approaches considered:

1. **BSON Binary**: Store as 16 bytes (`Binary { subtype: Generic, bytes: id.to_be_bytes().to_vec() }`)
   — more compact but less readable.
2. **Decimal128**: BSON Decimal128 can represent u128 values but the mongodb crate's Decimal128
   support is limited.
3. **String (chosen)**: Simple, human-readable, unique, sortable for small values.

For production use at high message volumes, approach 1 (BSON Binary) may be preferable for index
efficiency. The spec defaults to String for simplicity; this can be made configurable via a
`message_id_format: Option<String>` config field in a follow-up.

---

## Appendix C: MongoDB Driver v3 Fluent API — Quick Reference

This appendix summarizes the key API changes from the mongodb crate v2.x to v3.x that affect this
spec. All code in this document uses the v3 fluent API.

### insert_many

```rust
// v2 (wrong — do not use):
let options = InsertManyOptions::builder().ordered(false).build();
collection.insert_many(docs.clone()).with_options(options).await?;

// v3 (correct — fluent API, pass &docs to avoid clone):
collection.insert_many(&docs).ordered(false).await?;
```

### find

```rust
// v2 (wrong — do not use):
let options = FindOptions::builder()
    .sort(doc! { field: 1 })
    .limit(n as i64)
    .build();
collection.find(filter).with_options(options).await?;

// v3 (correct — fluent API):
collection.find(filter).sort(doc! { field: 1 }).limit(n as i64).await?;
```

### watch (change stream)

```rust
// v2 (wrong — do not use):
let mut options = ChangeStreamOptions::builder()
    .batch_size(n)
    .full_document(Some(FullDocumentType::UpdateLookup))
    .build();
options.resume_after = Some(token_doc);
db.watch().pipeline(pipeline).with_options(options).await?;

// v3 (correct — fluent API, chain all options):
db.watch()
    .pipeline(pipeline)
    .batch_size(n)
    .full_document(FullDocumentType::UpdateLookup)
    .resume_after(token_doc)
    .await?;
```

---

*Specification written by the Iggy connector design process.*
*Version 2.0 incorporates rubber-duck debugging findings from post-v1 analysis.*
*Based on code read directly from the live codebase via Parseltongue at http://localhost:7777.*
*All trait signatures, macro patterns, constructor signatures, config structures, and error types*
*are sourced from the actual implementation files, not inferred.*
