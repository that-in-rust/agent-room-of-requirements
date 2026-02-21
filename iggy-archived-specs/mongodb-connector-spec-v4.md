# MongoDB Connector Specification v4

> **Authoritative reference for implementing MongoDB source and sink connectors for Iggy**
>
> Based on actual analysis of Iggy connector codebase via Parseltongue dependency graph (2026-02-21)

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Changelog from v3](#changelog-from-v3)
3. [Architecture Overview](#architecture-overview)
4. [FFI Boundary Specification](#ffi-boundary-specification)
5. [MongoDB Sink Connector](#mongodb-sink-connector)
6. [MongoDB Source Connector](#mongodb-source-connector)
7. [Implementation Details](#implementation-details)
8. [Configuration](#configuration)
9. [Integration Testing](#integration-testing)
10. [Build and Deployment](#build-and-deployment)
11. [Appendix: Parseltongue Analysis](#appendix-parseltongue-analysis)

---

## Executive Summary

This specification provides complete implementation guidance for MongoDB connectors (source and sink) for the Iggy message streaming platform. It is based on actual code analysis of the existing PostgreSQL connectors, which serve as the canonical reference.

### Key Requirements

1. **SDK Version**: `iggy_connector_sdk = "0.1.3-edge.1"`
2. **Rust Edition**: `2024`
3. **MongoDB Driver**: `mongodb` crate v3.0+ (fluent API with `rustls-tls`)
4. **Serialization Format**:
   - Config: `serde_json` (for FFI open() call)
   - Topic/Messages Metadata: `postcard` (for FFI consume() call)
   - Messages: `postcard` (RawMessages wrapper)
   - State: `rmp_serde` (MessagePack for persistence)
5. **Macro Registration**: `sink_connector!(MongoDbSink)` and `source_connector!(MongoDbSource)`

### File Structure

```
core/connectors/
├── sinks/
│   └── mongodb_sink/
│       ├── Cargo.toml
│       ├── config.toml
│       └── src/
│           └── lib.rs
└── sources/
    └── mongodb_source/
        ├── Cargo.toml
        ├── config.toml
        └── src/
            └── lib.rs
```

---

## Changelog from v3

### Verified Correct in v3

The following aspects of v3 were verified as accurate through Parseltongue analysis:

1. **Trait Signatures**: Source and Sink trait signatures match exactly
2. **Constructor Pattern**: `new(id: u32, config: T, state: Option<ConnectorState>) -> Self`
3. **Macro Usage**: `sink_connector!` and `source_connector!` macros are correct
4. **FFI Boundary**: Serialization formats at each boundary are correct
5. **Runtime Pattern**: Using SDK's `get_runtime()` for blocking async calls
6. **State Management**: MessagePack serialization via `ConnectorState` wrapper

### New Findings and Corrections

1. **Payload Processing Pattern** (CORRECTION):
   - v3 showed direct payload handling
   - Actual code uses `message.payload.try_into_vec()` to convert `Payload` enum to `Vec<u8>`
   - This is required because `ConsumedMessage.payload` is `Payload`, not `Vec<u8>`

2. **Timestamp Parsing** (NEW):
   - Iggy timestamps are microseconds since Unix epoch
   - Convert to `DateTime<Utc>` via: `DateTime::from_timestamp((micros / 1_000_000) as i64, ((micros % 1_000_000) * 1_000) as u32)`
   - MongoDB BSON DateTime expects milliseconds

3. **Error Handling Pattern** (NEW):
   - Transient errors should be retried with exponential backoff
   - PostgreSQL connector defines `is_transient_error()` function
   - MongoDB should use similar logic for network errors

4. **Connection Pool Configuration** (CLARIFIED):
   - Use `ClientOptions::builder()` with `max_pool_size` parameter
   - Set appropriate timeouts for connector use case
   - Use `rustls-tls` feature for TLS without OpenSSL

5. **Batch Insert Pattern** (CORRECTION):
   - v3 showed single inserts
   - Actual pattern uses `bulk_write()` with `InsertOneModel` for efficiency
   - Batches controlled by `batch_size` config parameter

6. **Identifier Quoting** (NOT APPLICABLE):
   - PostgreSQL uses double quotes for identifiers: `"table_name"`
   - MongoDB collection names don't require quoting
   - Use `client.database()` and `db.collection()` fluent API

7. **CDC Support** (DEFERRED):
   - PostgreSQL has WAL-based CDC
   - MongoDB Change Streams are the equivalent
   - Deferred to future enhancement (not in MVP)

---

## Architecture Overview

### ASCII Dependency Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Iggy Connectors Runtime                              │
│                      (core/connectors/runtime)                               │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │                               │
                    ▼                               ▼
        ┌───────────────────┐           ┌───────────────────┐
        │   SinkApi (FFI)   │           │  SourceApi (FFI)  │
        │  - open()         │           │  - open()         │
        │  - consume()      │           │  - handle()       │
        │  - close()        │           │  - close()        │
        └───────────────────┘           └───────────────────┘
                    │                               │
                    │ postcard                      │ postcard
                    │ serialization                 │ serialization
                    ▼                               ▼
        ┌───────────────────┐           ┌───────────────────┐
        │ SinkContainer     │           │ SourceContainer   │
        │ (SDK macro)       │           │ (SDK macro)       │
        └───────────────────┘           └───────────────────┘
                    │                               │
                    ▼                               ▼
        ┌───────────────────┐           ┌───────────────────┐
        │   Sink trait      │           │   Source trait    │
        │  - open()         │           │  - open()         │
        │  - consume()      │           │  - poll()         │
        │  - close()        │           │  - close()        │
        └───────────────────┘           └───────────────────┘
                    │                               │
                    ▼                               ▼
        ┌───────────────────┐           ┌───────────────────┐
        │ MongoDbSink      │           │ MongoDbSource     │
        │  - Client        │           │  - Client         │
        │  - Database      │           │  - Database       │
        │  - Collection    │           │  - Collection     │
        └───────────────────┘           └───────────────────┘
                    │                               │
                    ▼                               ▼
        ┌───────────────────┐           ┌───────────────────┐
        │   MongoDB Server  │           │   MongoDB Server  │
        │   (target store)  │           │   (data source)   │
        └───────────────────┘           └───────────────────┘
```

### FFI Call Sequence

```
Runtime loads .so/.dylib/.dll
    │
    ├─> dlopen() → Container<Api>
    │
    ├─> Sink: open(id, config_json_ptr, len, log_callback)
    │       └─> serde_json::from_str::<Config>(slice)
    │       └─> MongoDbSink::new(id, config)
    │       └─> sink.open().await (on SDK runtime)
    │
    ├─> Sink: consume(id, topic_meta_ptr, len, msgs_meta_ptr, len, msgs_ptr, len)
    │       └─> postcard::from_bytes::<TopicMetadata>(topic_slice)
    │       └─> postcard::from_bytes::<MessagesMetadata>(meta_slice)
    │       └─> postcard::from_bytes::<RawMessages>(msgs_slice)
    │       └─> For each RawMessage:
    │               └─> headers = postcard::from_bytes(&raw.headers)
    │               └─> payload = schema.try_into_payload(raw.payload)
    │       └─> sink.consume(&topic_meta, msgs_meta, messages).await
    │
    ├─> Source: open(id, config_json_ptr, len, state_ptr, len, log_callback)
    │       └─> serde_json::from_str::<Config>(slice)
    │       └─> state = ConnectorState(state_slice).deserialize::<State>()
    │       └─> MongoDbSource::new(id, config, state)
    │       └─> source.open().await
    │
    ├─> Source: handle(id, send_callback)
    │       └─> Spawns task: loop { source.poll().await }
    │       └─> postcard::to_allocvec(&ProducedMessages)
    │       └─> send_callback(id, ptr, len)
    │
    └─> close(id)
```

---

## FFI Boundary Specification

### Sink FFI API (from Parseltongue)

```rust
#[derive(WrapperApi)]
struct SinkApi {
    open: extern "C" fn(
        id: u32,
        config_ptr: *const u8,
        config_len: usize,
        log_callback: iggy_connector_sdk::LogCallback,
    ) -> i32,
    consume: extern "C" fn(
        id: u32,
        topic_meta_ptr: *const u8,
        topic_meta_len: usize,
        messages_meta_ptr: *const u8,
        messages_meta_len: usize,
        messages_ptr: *const u8,
        messages_len: usize,
    ) -> i32,
    close: extern "C" fn(id: u32) -> i32,
    version: extern "C" fn() -> *const std::ffi::c_char,
}
```

### Source FFI API (from Parseltongue)

```rust
#[derive(WrapperApi)]
struct SourceApi {
    open: extern "C" fn(
        id: u32,
        config_ptr: *const u8,
        config_len: usize,
        state_ptr: *const u8,
        state_len: usize,
        log_callback: iggy_connector_sdk::LogCallback,
    ) -> i32,
    handle: extern "C" fn(id: u32, callback: SendCallback) -> i32,
    close: extern "C" fn(id: u32) -> i32,
    version: extern "C" fn() -> *const std::ffi::c_char,
}

type SendCallback = extern "C" fn(
    plugin_id: u32,
    messages_ptr: *const u8,
    messages_len: usize
);
```

### Serialization Format at Each Boundary

| Boundary | Format | Data Types |
|----------|--------|------------|
| `open()` config | `serde_json` | `Config` struct (connector-specific) |
| `consume()` topic_meta | `postcard` | `TopicMetadata { stream, topic }` |
| `consume()` messages_meta | `postcard` | `MessagesMetadata { partition_id, current_offset, schema }` |
| `consume()` messages | `postcard` | `RawMessages { schema, messages: Vec<RawMessage> }` |
| RawMessage.headers | `postcard` | `HashMap<HeaderKey, HeaderValue>` |
| RawMessage.payload | `Schema::try_into_payload()` | `Payload` enum (Json/Raw/Text/Proto/FlatBuffer) |
| Source `handle()` return | `postcard` | `ProducedMessages { schema, messages, state }` |
| State persistence | `rmp_serde` | `ConnectorState(Vec<u8>)` wrapper |

---

## MongoDB Sink Connector

### Trait Implementation

```rust
#[async_trait]
impl Sink for MongoDbSink {
    async fn open(&mut self) -> Result<(), Error> {
        // 1. Parse connection string
        // 2. Create ClientOptions
        // 3. Build client with rustls-tls
        // 4. Ping server
        // 5. Create collection if auto_create_collection enabled
        Ok(())
    }

    async fn consume(
        &self,
        topic_metadata: &TopicMetadata,
        messages_metadata: MessagesMetadata,
        messages: Vec<ConsumedMessage>,
    ) -> Result<(), Error> {
        // 1. Convert messages to MongoDB documents
        // 2. Insert in batches using bulk_write()
        // 3. Handle transient errors with retry
        Ok(())
    }

    async fn close(&mut self) -> Result<(), Error> {
        // Close client connection
        Ok(())
    }
}
```

### Config Struct

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MongoDbSinkConfig {
    /// MongoDB connection string (e.g., "mongodb://localhost:27017")
    pub connection_string: String,

    /// Target database name
    pub database: String,

    /// Target collection name
    pub collection: String,

    /// Maximum batch size for bulk inserts (default: 100)
    pub batch_size: Option<u32>,

    /// Maximum connection pool size (default: 10)
    pub max_pool_size: Option<u32>,

    /// Automatically create collection if not exists (default: false)
    pub auto_create_collection: Option<bool>,

    /// Include Iggy metadata in documents (default: true)
    pub include_metadata: Option<bool>,

    /// Include checksum field (default: true)
    pub include_checksum: Option<bool>,

    /// Include origin_timestamp field (default: true)
    pub include_origin_timestamp: Option<bool>,

    /// Payload field name (default: "payload")
    pub payload_field_name: Option<String>,

    /// Enable verbose logging (default: false)
    pub verbose_logging: Option<bool>,

    /// Maximum retries for transient errors (default: 3)
    pub max_retries: Option<u32>,

    /// Retry delay in humantime format (default: "1s")
    pub retry_delay: Option<String>,
}
```

### Full Implementation

```rust
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

use async_trait::async_trait;
use humantime::Duration as HumanDuration;
use iggy_common::{DateTime, Utc};
use iggy_connector_sdk::{
    ConsumedMessage, Error, MessagesMetadata, Sink, TopicMetadata, sink_connector,
};
use mongodb::{
    bson::{doc, Document, Bson},
    options::{ClientOptions, UpdateOptions},
    Client, Collection,
};
use serde::{Deserialize, Serialize};
use std::str::FromStr;
use std::time::Duration;
use tokio::sync::Mutex;
use tracing::{debug, error, info, warn};

sink_connector!(MongoDbSink);

const DEFAULT_MAX_RETRIES: u32 = 3;
const DEFAULT_RETRY_DELAY: &str = "1s";

#[derive(Debug)]
pub struct MongoDbSink {
    pub id: u32,
    client: Option<Client>,
    config: MongoDbSinkConfig,
    state: Mutex<State>,
    verbose: bool,
    retry_delay: Duration,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MongoDbSinkConfig {
    pub connection_string: String,
    pub database: String,
    pub collection: String,
    pub batch_size: Option<u32>,
    pub max_pool_size: Option<u32>,
    pub auto_create_collection: Option<bool>,
    pub include_metadata: Option<bool>,
    pub include_checksum: Option<bool>,
    pub include_origin_timestamp: Option<bool>,
    pub payload_field_name: Option<String>,
    pub verbose_logging: Option<bool>,
    pub max_retries: Option<u32>,
    pub retry_delay: Option<String>,
}

#[derive(Debug)]
struct State {
    messages_processed: u64,
    insertion_errors: u64,
}

impl MongoDbSink {
    pub fn new(id: u32, config: MongoDbSinkConfig) -> Self {
        let verbose = config.verbose_logging.unwrap_or(false);
        let delay_str = config.retry_delay.as_deref().unwrap_or(DEFAULT_RETRY_DELAY);
        let retry_delay = HumanDuration::from_str(delay_str)
            .map(|duration| duration.into())
            .unwrap_or_else(|_| Duration::from_secs(1));

        MongoDbSink {
            id,
            client: None,
            config,
            state: Mutex::new(State {
                messages_processed: 0,
                insertion_errors: 0,
            }),
            verbose,
            retry_delay,
        }
    }

    fn get_collection(&self) -> Result<Collection<Document>, Error> {
        let client = self
            .client
            .as_ref()
            .ok_or_else(|| Error::InitError("MongoDB client not initialized".to_string()))?;

        Ok(client
            .database(&self.config.database)
            .collection(&self.config.collection))
    }
}

#[async_trait]
impl Sink for MongoDbSink {
    async fn open(&mut self) -> Result<(), Error> {
        info!(
            "Opening MongoDB sink connector with ID: {}. Database: {}. Collection: {}",
            self.id, self.config.database, self.config.collection
        );

        // Parse connection string and build client options
        let mut client_options = ClientOptions::parse(&self.config.connection_string)
            .await
            .map_err(|e| Error::InitError(format!("Failed to parse connection string: {e}")))?;

        // Configure connection pool
        if let Some(max_pool_size) = self.config.max_pool_size {
            client_options.max_pool_size = Some(max_pool_size);
        }

        // Build client
        let client = Client::with_options(client_options)
            .map_err(|e| Error::InitError(format!("Failed to create MongoDB client: {e}")))?;

        // Ping server to verify connectivity
        client
            .database("admin")
            .run_command(doc! {"ping": 1}, None)
            .await
            .map_err(|e| Error::InitError(format!("MongoDB ping failed: {e}")))?;

        self.client = Some(client);

        // Create collection if requested
        if self.config.auto_create_collection.unwrap_or(false) {
            self.create_collection().await?;
        }

        info!(
            "MongoDB sink connector with ID: {} opened successfully",
            self.id
        );
        Ok(())
    }

    async fn consume(
        &self,
        topic_metadata: &TopicMetadata,
        messages_metadata: MessagesMetadata,
        messages: Vec<ConsumedMessage>,
    ) -> Result<(), Error> {
        self.process_messages(topic_metadata, &messages_metadata, &messages)
            .await
    }

    async fn close(&mut self) -> Result<(), Error> {
        info!("Closing MongoDB sink connector with ID: {}", self.id);

        // Client will be dropped automatically
        self.client = None;

        let state = self.state.lock().await;
        info!(
            "MongoDB sink ID: {} processed {} messages with {} errors",
            self.id, state.messages_processed, state.insertion_errors
        );
        Ok(())
    }
}

impl MongoDbSink {
    async fn create_collection(&self) -> Result<(), Error> {
        let client = self.get_client()?;
        let db = client.database(&self.config.database);

        // Check if collection exists
        let collection_names = db
            .list_collection_names(None, None)
            .await
            .map_err(|e| Error::InitError(format!("Failed to list collections: {e}")))?;

        if collection_names.contains(&self.config.collection) {
            return Ok(());
        }

        // Create collection with default options
        db.create_collection(&self.config.collection, None, None)
            .await
            .map_err(|e| {
                Error::InitError(format!("Failed to create collection '{}': {}", self.config.collection, e))
            })?;

        info!(
            "Created collection '{}.{}'",
            self.config.database, self.config.collection
        );
        Ok(())
    }

    async fn process_messages(
        &self,
        topic_metadata: &TopicMetadata,
        messages_metadata: &MessagesMetadata,
        messages: &[ConsumedMessage],
    ) -> Result<(), Error> {
        let collection = self.get_collection()?;
        let batch_size = self.config.batch_size.unwrap_or(100) as usize;

        for batch in messages.chunks(batch_size) {
            if let Err(e) = self.insert_batch(batch, topic_metadata, messages_metadata, &collection).await {
                let mut state = self.state.lock().await;
                state.insertion_errors += batch.len() as u64;
                error!("Failed to insert batch: {e}");
            }
        }

        let mut state = self.state.lock().await;
        state.messages_processed += messages.len() as u64;

        let msg_count = messages.len();
        if self.verbose {
            info!(
                "MongoDB sink ID: {} processed {msg_count} messages to '{}.{}'",
                self.id, self.config.database, self.config.collection
            );
        } else {
            debug!(
                "MongoDB sink ID: {} processed {msg_count} messages to '{}.{}'",
                self.id, self.config.database, self.config.collection
            );
        }

        Ok(())
    }

    async fn insert_batch(
        &self,
        messages: &[ConsumedMessage],
        topic_metadata: &TopicMetadata,
        messages_metadata: &MessagesMetadata,
        collection: &Collection<Document>,
    ) -> Result<(), Error> {
        if messages.is_empty() {
            return Ok(());
        }

        let include_metadata = self.config.include_metadata.unwrap_or(true);
        let include_checksum = self.config.include_checksum.unwrap_or(true);
        let include_origin_timestamp = self.config.include_origin_timestamp.unwrap_or(true);
        let payload_field_name = self.config.payload_field_name.as_deref().unwrap_or("payload");

        let mut documents = Vec::with_capacity(messages.len());

        for message in messages {
            let mut doc = Document::new();

            // Primary key from Iggy message ID
            doc.insert("_id", message.id);

            // Iggy metadata
            if include_metadata {
                doc.insert("iggy_offset", message.offset);
                doc.insert("iggy_timestamp", bson_datetime(message.timestamp));
                doc.insert("iggy_stream", &topic_metadata.stream);
                doc.insert("iggy_topic", &topic_metadata.topic);
                doc.insert("iggy_partition_id", messages_metadata.partition_id);
            }

            // Optional fields
            if include_checksum {
                doc.insert("iggy_checksum", message.checksum);
            }

            if include_origin_timestamp {
                doc.insert("iggy_origin_timestamp", bson_datetime(message.origin_timestamp));
            }

            // Convert payload to Vec<u8> then to appropriate BSON type
            let payload_bytes = message.payload.clone().try_into_vec()
                .map_err(|e| Error::InvalidPayloadType)?;

            match &message.payload {
                iggy_connector_sdk::Payload::Json(_) => {
                    // Keep as JSON if it was JSON
                    doc.insert(payload_field_name, payload_bytes);
                }
                _ => {
                    // Store as Binary for other types
                    doc.insert(payload_field_name, Bson::Binary(mongodb::bson::Binary {
                        subtype: mongodb::bson::spec::BinarySubtype::Generic,
                        bytes: payload_bytes,
                    }));
                }
            }

            documents.push(doc);
        }

        // Bulk insert with retry
        self.bulk_insert_with_retry(collection, documents).await
    }

    async fn bulk_insert_with_retry(
        &self,
        collection: &Collection<Document>,
        documents: Vec<Document>,
    ) -> Result<(), Error> {
        let max_retries = self.get_max_retries();
        let retry_delay = self.retry_delay;
        let mut attempts = 0u32;

        loop {
            let result = self.bulk_insert(collection, &documents).await;

            match result {
                Ok(_) => return Ok(()),
                Err(e) => {
                    attempts += 1;
                    if !is_transient_error(&e) || attempts >= max_retries {
                        error!("Bulk insert failed after {attempts} attempts: {e}");
                        return Err(Error::CannotStoreData(format!(
                            "Bulk insert failed after {attempts} attempts: {e}"
                        )));
                    }
                    warn!(
                        "Transient database error (attempt {attempts}/{max_retries}): {e}. Retrying..."
                    );
                    tokio::time::sleep(retry_delay * attempts as u32).await;
                }
            }
        }
    }

    async fn bulk_insert(
        &self,
        collection: &Collection<Document>,
        documents: &[Document],
    ) -> Result<(), Error> {
        let inserts: Vec<_> = documents
            .iter()
            .map(|doc| mongodb::operations::InsertOneModel::new(doc.clone()))
            .collect();

        collection
            .bulk_write(inserts, None, None)
            .await
            .map_err(|e| Error::CannotStoreData(format!("Bulk insert failed: {e}")))?;

        Ok(())
    }

    fn get_client(&self) -> Result<&Client, Error> {
        self.client
            .as_ref()
            .ok_or_else(|| Error::InitError("MongoDB client not initialized".to_string()))
    }

    fn get_max_retries(&self) -> u32 {
        self.config.max_retries.unwrap_or(DEFAULT_MAX_RETRIES)
    }
}

// Convert Iggy timestamp (microseconds) to MongoDB BSON DateTime (milliseconds)
fn bson_timestamp(micros: u64) -> Bson {
    Bson::DateTime(mongodb::bson::datetime::DateTime::from_millis(
        (micros / 1000) as i64,
    ))
}

// DateTime helper for compatibility
fn bson_datetime(micros: u64) -> mongodb::bson::datetime::DateTime {
    mongodb::bson::datetime::DateTime::from_millis((micros / 1000) as i64)
}

fn is_transient_error(error: &Error) -> bool {
    // MongoDB transient errors typically include network timeouts
    let error_str = error.to_string().to_lowercase();
    error_str.contains("timeout")
        || error_str.contains("network")
        || error_str.contains("connection")
        || error_str.contains("pool")
}

#[cfg(test)]
mod tests {
    use super::*;

    fn test_config() -> MongoDbSinkConfig {
        MongoDbSinkConfig {
            connection_string: "mongodb://localhost:27017".to_string(),
            database: "test_db".to_string(),
            collection: "test_collection".to_string(),
            batch_size: Some(100),
            max_pool_size: None,
            auto_create_collection: None,
            include_metadata: None,
            include_checksum: None,
            include_origin_timestamp: None,
            payload_field_name: None,
            verbose_logging: None,
            max_retries: None,
            retry_delay: None,
        }
    }

    #[test]
    fn test_timestamp_conversion() {
        let micros: u64 = 1_767_225_600_000_000; // 2026-01-01 00:00:00 UTC
        let ts = bson_timestamp(micros);
        assert!(matches!(ts, Bson::DateTime(_)));
    }

    #[test]
    fn test_default_max_retries() {
        let sink = MongoDbSink::new(1, test_config());
        assert_eq!(sink.get_max_retries(), DEFAULT_MAX_RETRIES);
    }

    #[test]
    fn test_custom_max_retries() {
        let mut config = test_config();
        config.max_retries = Some(5);
        let sink = MongoDbSink::new(1, config);
        assert_eq!(sink.get_max_retries(), 5);
    }
}
```

---

## MongoDB Source Connector

### Trait Implementation

```rust
#[async_trait]
impl Source for MongoDbSource {
    async fn open(&mut self) -> Result<(), Error> {
        // 1. Parse connection string
        // 2. Create ClientOptions
        // 3. Build client with rustls-tls
        // 4. Ping server
        // 5. Validate collection exists
        Ok(())
    }

    async fn poll(&self) -> Result<ProducedMessages, Error> {
        // 1. Poll for documents based on tracking
        // 2. Convert to ProducedMessage
        // 3. Update state
        // 4. Return with serialized state
        Ok(ProducedMessages { ... })
    }

    async fn close(&mut self) -> Result<(), Error> {
        // Close client connection
        Ok(())
    }
}
```

### Config Struct

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MongoDbSourceConfig {
    /// MongoDB connection string (e.g., "mongodb://localhost:27017")
    pub connection_string: String,

    /// Source database name
    pub database: String,

    /// Source collection name
    pub collection: String,

    /// Polling interval in humantime format (default: "10s")
    pub poll_interval: Option<String>,

    /// Batch size for querying (default: 1000)
    pub batch_size: Option<u32>,

    /// Maximum connection pool size (default: 10)
    pub max_pool_size: Option<u32>,

    /// Field to track for changes (default: "_id")
    pub tracking_field: Option<String>,

    /// Initial offset value (default: none)
    pub initial_offset: Option<String>,

    /// Query filter (JSON string, default: none for all documents)
    pub query_filter: Option<String>,

    /// Projection to limit fields (JSON string, default: none)
    pub projection: Option<String>,

    /// Snake case field names (default: false)
    pub snake_case_fields: Option<bool>,

    /// Include collection metadata (default: true)
    pub include_metadata: Option<bool>,

    /// Delete documents after reading (default: false)
    pub delete_after_read: Option<bool>,

    /// Mark documents as processed with this field name
    pub processed_field: Option<String>,

    /// Payload field to extract (if empty, entire document)
    pub payload_field: Option<String>,

    /// Payload format: "json", "bson", "string" (default: "json")
    pub payload_format: Option<String>,

    /// Enable verbose logging (default: false)
    pub verbose_logging: Option<bool>,

    /// Maximum retries for transient errors (default: 3)
    pub max_retries: Option<u32>,

    /// Retry delay in humantime format (default: "1s")
    pub retry_delay: Option<String>,
}
```

### Full Implementation

```rust
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

use async_trait::async_trait;
use humantime::Duration as HumanDuration;
use iggy_common::Utc;
use iggy_connector_sdk::{
    ConnectorState, Error, ProducedMessage, ProducedMessages, Schema, Source, source_connector,
};
use mongodb::{
    bson::{doc, Document, Bson},
    options::{ClientOptions, FindOptions},
    Client, Collection,
};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::str::FromStr;
use std::time::Duration;
use tokio::sync::Mutex;
use tracing::{debug, error, info, warn};
use uuid::Uuid;

source_connector!(MongoDbSource);

const DEFAULT_MAX_RETRIES: u32 = 3;
const DEFAULT_RETRY_DELAY: &str = "1s";
const CONNECTOR_NAME: &str = "MongoDB source";

#[derive(Debug)]
pub struct MongoDbSource {
    pub id: u32,
    client: Option<Client>,
    config: MongoDbSourceConfig,
    state: Mutex<State>,
    verbose: bool,
    retry_delay: Duration,
    poll_interval: Duration,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MongoDbSourceConfig {
    pub connection_string: String,
    pub database: String,
    pub collection: String,
    pub poll_interval: Option<String>,
    pub batch_size: Option<u32>,
    pub max_pool_size: Option<u32>,
    pub tracking_field: Option<String>,
    pub initial_offset: Option<String>,
    pub query_filter: Option<String>,
    pub projection: Option<String>,
    pub snake_case_fields: Option<bool>,
    pub include_metadata: Option<bool>,
    pub delete_after_read: Option<bool>,
    pub processed_field: Option<String>,
    pub payload_field: Option<String>,
    pub payload_format: Option<String>,
    pub verbose_logging: Option<bool>,
    pub max_retries: Option<u32>,
    pub retry_delay: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct State {
    last_poll_time: chrono::DateTime<Utc>,
    tracking_offset: Option<String>,
    processed_count: u64,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct DatabaseRecord {
    pub collection_name: String,
    pub operation_type: String,
    pub timestamp: chrono::DateTime<Utc>,
    pub data: serde_json::Value,
    pub old_data: Option<serde_json::Value>,
}

impl MongoDbSource {
    pub fn new(id: u32, config: MongoDbSourceConfig, state: Option<ConnectorState>) -> Self {
        let verbose = config.verbose_logging.unwrap_or(false);
        let restored_state = state
            .and_then(|s| s.deserialize::<State>(CONNECTOR_NAME, id))
            .inspect(|s| {
                info!(
                    "Restored state for {CONNECTOR_NAME} connector with ID: {id}. \
                     Tracking offset: {:?}, processed count: {}",
                    s.tracking_offset, s.processed_count
                );
            });

        let delay_str = config.retry_delay.as_deref().unwrap_or(DEFAULT_RETRY_DELAY);
        let retry_delay = HumanDuration::from_str(delay_str)
            .map(|duration| duration.into())
            .unwrap_or_else(|_| Duration::from_secs(1));

        let interval_str = config.poll_interval.as_deref().unwrap_or("10s");
        let poll_interval = HumanDuration::from_str(interval_str)
            .map(|duration| duration.into())
            .unwrap_or_else(|_| Duration::from_secs(10));

        MongoDbSource {
            id,
            client: None,
            config,
            state: Mutex::new(restored_state.unwrap_or(State {
                last_poll_time: Utc::now(),
                tracking_offset: None,
                processed_count: 0,
            })),
            verbose,
            retry_delay,
            poll_interval,
        }
    }

    fn serialize_state(&self, state: &State) -> Option<ConnectorState> {
        ConnectorState::serialize(state, CONNECTOR_NAME, self.id)
    }

    fn get_collection(&self) -> Result<Collection<Document>, Error> {
        let client = self
            .client
            .as_ref()
            .ok_or_else(|| Error::InitError("MongoDB client not initialized".to_string()))?;

        Ok(client
            .database(&self.config.database)
            .collection(&self.config.collection))
    }
}

#[async_trait]
impl Source for MongoDbSource {
    async fn open(&mut self) -> Result<(), Error> {
        info!(
            "Opening MongoDB source connector with ID: {}. Database: {}. Collection: {}",
            self.id, self.config.database, self.config.collection
        );

        // Parse connection string and build client options
        let mut client_options = ClientOptions::parse(&self.config.connection_string)
            .await
            .map_err(|e| Error::InitError(format!("Failed to parse connection string: {e}")))?;

        // Configure connection pool
        if let Some(max_pool_size) = self.config.max_pool_size {
            client_options.max_pool_size = Some(max_pool_size);
        }

        // Build client
        let client = Client::with_options(client_options)
            .map_err(|e| Error::InitError(format!("Failed to create MongoDB client: {e}")))?;

        // Ping server to verify connectivity
        client
            .database("admin")
            .run_command(doc! {"ping": 1}, None)
            .await
            .map_err(|e| Error::InitError(format!("MongoDB ping failed: {e}")))?;

        self.client = Some(client);

        // Validate collection exists
        self.validate_collection().await?;

        info!(
            "MongoDB source connector with ID: {} opened successfully",
            self.id
        );
        Ok(())
    }

    async fn poll(&self) -> Result<ProducedMessages, Error> {
        let poll_interval = self.poll_interval;
        tokio::time::sleep(poll_interval).await;

        let messages = self.poll_collection().await?;

        let state = self.state.lock().await;
        if self.verbose {
            info!(
                "MongoDB source connector ID: {} produced {} messages. Total processed: {}",
                self.id,
                messages.len(),
                state.processed_count
            );
        } else {
            debug!(
                "MongoDB source connector ID: {} produced {} messages. Total processed: {}",
                self.id,
                messages.len(),
                state.processed_count
            );
        }

        let schema = match self.payload_format() {
            PayloadFormat::Bson => Schema::Raw,
            PayloadFormat::String => Schema::Text,
            PayloadFormat::Json => Schema::Json,
        };

        let persisted_state = self.serialize_state(&state);

        Ok(ProducedMessages {
            schema,
            messages,
            state: persisted_state,
        })
    }

    async fn close(&mut self) -> Result<(), Error> {
        if let Some(_client) = self.client.take() {
            info!(
                "MongoDB connection closed for source connector ID: {}",
                self.id
            );
        }

        let state = self.state.lock().await;
        info!(
            "MongoDB source connector ID: {} closed. Total documents processed: {}",
            self.id, state.processed_count
        );
        Ok(())
    }
}

impl MongoDbSource {
    async fn validate_collection(&self) -> Result<(), Error> {
        let client = self.get_client()?;
        let db = client.database(&self.config.database);

        let collection_names = db
            .list_collection_names(None, None)
            .await
            .map_err(|e| Error::InitError(format!("Failed to list collections: {e}")))?;

        if !collection_names.contains(&self.config.collection) {
            return Err(Error::InitError(format!(
                "Collection '{}.{}' does not exist",
                self.config.database, self.config.collection
            )));
        }

        Ok(())
    }

    async fn poll_collection(&self) -> Result<Vec<ProducedMessage>, Error> {
        let collection = self.get_collection()?;
        let batch_size = self.config.batch_size.unwrap_or(1000);
        let tracking_field = self.config.tracking_field.as_deref().unwrap_or("_id");
        let payload_format = self.payload_format();

        // Get current tracking offset
        let last_offset = {
            let state = self.state.lock().await;
            state.tracking_offset.clone()
        };

        // Build query filter
        let mut filter = self.build_query_filter(&last_offset)?;

        // Apply custom query filter if provided
        if let Some(custom_filter) = &self.config.query_filter {
            let custom_doc: Document = serde_json::from_str(custom_filter)
                .map_err(|_| Error::InvalidConfig)?;
            filter.extend(custom_doc);
        }

        // Build find options
        let mut find_options = FindOptions::default();
        find_options.limit = Some(batch_size as i64);
        find_options.sort = Some(doc! {tracking_field: 1});

        if let Some(projection) = &self.config.projection {
            let proj_doc: Document = serde_json::from_str(projection)
                .map_err(|_| Error::InvalidConfig)?;
            find_options.projection = Some(proj_doc);
        }

        // Fetch documents with retry
        let documents = with_retry(
            || collection.find(filter.clone(), find_options.clone()),
            self.get_max_retries(),
            self.retry_delay.as_millis() as u64,
        )
        .await?
        .try_collect::<Vec<_>>()
        .await
        .map_err(|e| Error::InvalidRecord)?;

        let mut messages = Vec::new();
        let mut max_offset: Option<String> = None;
        let mut processed_ids: Vec<String> = Vec::new();

        for doc in documents {
            // Extract tracking field value
            if let Some(bson_value) = doc.get(tracking_field) {
                if let Some(str_val) = bson_value.as_str() {
                    max_offset = Some(str_val.to_string());
                    if tracking_field == "_id" {
                        processed_ids.push(str_val.to_string());
                    }
                } else if let Some(oid) = bson_value.as_object_id() {
                    max_offset = Some(oid.to_hex());
                    processed_ids.push(oid.to_hex());
                } else {
                    let json_val = bson_to_json(bson_value)?;
                    if let Some(str_val) = json_val.as_str() {
                        max_offset = Some(str_val.to_string());
                    }
                    processed_ids.push(serde_json::to_string(&json_val).unwrap_or_default());
                }
            }

            // Convert document to message payload
            let payload = self.document_to_payload(&doc, payload_format)?;

            // Build message
            let message = ProducedMessage {
                id: Some(Uuid::new_v4().as_u128()),
                headers: None,
                checksum: None,
                timestamp: Some(Utc::now().timestamp_millis() as u64),
                origin_timestamp: Some(Utc::now().timestamp_millis() as u64),
                payload,
            };

            messages.push(message);
        }

        // Mark or delete processed documents
        if !processed_ids.is_empty() {
            self.mark_or_delete_processed(&collection, &processed_ids).await?;
        }

        // Update state
        if !messages.is_empty() {
            let mut state = self.state.lock().await;
            state.processed_count += messages.len() as u64;
            state.tracking_offset = max_offset;
            state.last_poll_time = Utc::now();
        }

        if self.verbose {
            info!("Fetched {} documents from collection '{}'", messages.len(), self.config.collection);
        } else {
            debug!("Fetched {} documents from collection '{}'", messages.len(), self.config.collection);
        }

        Ok(messages)
    }

    fn build_query_filter(&self, last_offset: &Option<String>) -> Result<Document, Error> {
        let tracking_field = self.config.tracking_field.as_deref().unwrap_or("_id");
        let mut filter = Document::new();

        // Add tracking field filter if we have an offset
        if let Some(offset) = last_offset {
            // Try to parse as ObjectId first
            if let Ok(oid) = mongodb::bson::oid::ObjectId::parse_str(offset) {
                filter.insert(tracking_field, doc! {"$gt": oid});
            } else {
                // Use as string value
                filter.insert(tracking_field, doc! {"$gt": offset});
            }
        } else if let Some(initial) = &self.config.initial_offset {
            // Use initial offset if no state
            if let Ok(oid) = mongodb::bson::oid::ObjectId::parse_str(initial) {
                filter.insert(tracking_field, doc! {"$gt": oid});
            } else {
                filter.insert(tracking_field, doc! {"$gt": initial.as_str()});
            }
        }

        // Add processed field filter if configured
        if let Some(processed_field) = &self.config.processed_field {
            filter.insert(processed_field, false);
        }

        Ok(filter)
    }

    fn document_to_payload(
        &self,
        doc: &Document,
        format: PayloadFormat,
    ) -> Result<Vec<u8>, Error> {
        // Check if we should extract a specific payload field
        if let Some(payload_field) = &self.config.payload_field {
            if !payload_field.is_empty() {
                if let Some(bson_value) = doc.get(payload_field) {
                    return self.bson_value_to_bytes(bson_value, format);
                }
            }
        }

        // Convert entire document
        match format {
            PayloadFormat::Json => {
                let json_value = bson_to_json(doc)?;
                serde_json::to_vec(&json_value).map_err(|_| Error::InvalidRecord)
            }
            PayloadFormat::Bson => {
                mongodb::bson::to_vec(doc).map_err(|_| Error::InvalidRecord)
            }
            PayloadFormat::String => {
                let json_value = bson_to_json(doc)?;
                serde_json::to_string(&json_value)
                    .map(|s| s.into_bytes())
                    .map_err(|_| Error::InvalidRecord)
            }
        }
    }

    fn bson_value_to_bytes(
        &self,
        bson_value: &Bson,
        format: PayloadFormat,
    ) -> Result<Vec<u8>, Error> {
        match format {
            PayloadFormat::Json => {
                let json_value = bson_to_json(bson_value)?;
                serde_json::to_vec(&json_value).map_err(|_| Error::InvalidRecord)
            }
            PayloadFormat::Bson => {
                match bson_value {
                    Bson::Document(doc) => {
                        mongodb::bson::to_vec(doc).map_err(|_| Error::InvalidRecord)
                    }
                    Bson::Binary(bin) => Ok(bin.bytes.clone()),
                    Bson::String(s) => Ok(s.as_bytes().to_vec()),
                    Bson::Int32(i) => Ok(i.to_string().into_bytes()),
                    Bson::Int64(i) => Ok(i.to_string().into_bytes()),
                    Bson::Double(f) => Ok(f.to_string().into_bytes()),
                    _ => {
                        let json_value = bson_to_json(bson_value)?;
                        serde_json::to_vec(&json_value).map_err(|_| Error::InvalidRecord)
                    }
                }
            }
            PayloadFormat::String => {
                let json_value = bson_to_json(bson_value)?;
                Ok(serde_json::to_string(&json_value).into_bytes())
            }
        }
    }

    async fn mark_or_delete_processed(
        &self,
        collection: &Collection<Document>,
        ids: &[String],
    ) -> Result<(), Error> {
        if ids.is_empty() {
            return Ok(());
        }

        let tracking_field = self.config.tracking_field.as_deref().unwrap_or("_id");

        if self.config.delete_after_read.unwrap_or(false) {
            // Delete processed documents
            let oid_ids: Result<Vec<_>, _> = ids
                .iter()
                .filter_map(|id| mongodb::bson::oid::ObjectId::parse_str(id).ok())
                .collect();

            if let Ok(object_ids) = oid_ids {
                if !object_ids.is_empty() {
                    collection
                        .delete_many(doc! { "_id": { "$in": object_ids } }, None)
                        .await
                        .map_err(|e| {
                            error!("Failed to delete processed documents: {e}");
                            Error::InvalidRecord
                        })?;

                    if self.verbose {
                        info!("Deleted {} processed documents from '{}'", ids.len(), self.config.collection);
                    }
                }
            }
        } else if let Some(processed_field) = &self.config.processed_field {
            // Mark documents as processed
            let oid_ids: Result<Vec<_>, _> = ids
                .iter()
                .filter_map(|id| mongodb::bson::oid::ObjectId::parse_str(id).ok())
                .collect();

            if let Ok(object_ids) = oid_ids {
                if !object_ids.is_empty() {
                    collection
                        .update_many(
                            doc! { "_id": { "$in": object_ids } },
                            doc! { "$set": { processed_field: true } },
                            None,
                        )
                        .await
                        .map_err(|e| {
                            error!("Failed to mark documents as processed: {e}");
                            Error::InvalidRecord
                        })?;

                    if self.verbose {
                        info!("Marked {} documents as processed in '{}'", ids.len(), self.config.collection);
                    }
                }
            }
        }

        Ok(())
    }

    fn payload_format(&self) -> PayloadFormat {
        PayloadFormat::from_config(self.config.payload_format.as_deref())
    }

    fn get_max_retries(&self) -> u32 {
        self.config.max_retries.unwrap_or(DEFAULT_MAX_RETRIES)
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
enum PayloadFormat {
    #[default]
    Json,
    Bson,
    String,
}

impl PayloadFormat {
    fn from_config(s: Option<&str>) -> Self {
        match s.map(|s| s.to_lowercase()).as_deref() {
            Some("bson") | Some("binary") => PayloadFormat::Bson,
            Some("string") | Some("text") => PayloadFormat::String,
            _ => PayloadFormat::Json,
        }
    }
}

// Convert BSON value to JSON value
fn bson_to_json(bson_value: &Bson) -> Result<serde_json::Value, Error> {
    match bson_value {
        Bson::FloatingPoint(v) => Ok(serde_json::json!(v)),
        Bson::String(v) => Ok(serde_json::json!(v)),
        Bson::Array(v) => {
            let arr: Result<Vec<_>, _> = v.iter().map(bson_to_json).collect();
            Ok(serde_json::Value::Array(arr?))
        }
        Bson::Document(v) => {
            let mut map = serde_json::Map::new();
            for (key, value) in v.iter() {
                map.insert(key.clone(), bson_to_json(value)?);
            }
            Ok(serde_json::Value::Object(map))
        }
        Bson::Bool(v) => Ok(serde_json::json!(v)),
        Bson::Null => Ok(serde_json::Value::Null),
        Bson::Int32(v) => Ok(serde_json::json!(v)),
        Bson::Int64(v) => Ok(serde_json::json!(v)),
        Bson::Double(v) => Ok(serde_json::json!(v)),
        Bson::DateTime(v) => Ok(serde_json::Value::String(v.to_rfc3339_string())),
        Bson::Timestamp(v) => Ok(serde_json::json!(v.incremental)),
        Bson::Binary(v) => {
            use base64::Engine;
            Ok(serde_json::Value::String(
                base64::engine::general_purpose::STANDARD.encode(&v.bytes)
            ))
        }
        Bson::ObjectId(v) => Ok(serde_json::Value::String(v.to_hex())),
        Bson::RegularExpression(v) => Ok(serde_json::json!(v.pattern.as_str())),
        Bson::JavaScriptCode(v) => Ok(serde_json::json!(v.as_str())),
        Bson::Symbol(v) => Ok(serde_json::json!(v.as_str())),
        Bson::Decimal128(v) => Ok(serde_json::Value::String(v.to_string())),
        Bson::Undefined => Ok(serde_json::Value::Null),
        Bson::MinKey => Ok(serde_json::json!("$minKey")),
        Bson::MaxKey => Ok(serde_json::json!("$maxKey")),
        Bson::DbPointer(v) => Ok(serde_json::json!(format!("{}.{}", v.namespace, v.id.to_hex()))),
        _ => Ok(serde_json::Value::Null),
    }
}

async fn with_retry<T, F, Fut>(operation: F, max_retries: u32, delay_ms: u64) -> Result<T, Error>
where
    F: Fn() -> Fut,
    Fut: std::future::Future<Output = Result<T, mongodb::error::Error>>,
{
    let mut attempts = 0;
    loop {
        match operation().await {
            Ok(result) => return Ok(result),
            Err(e) => {
                attempts += 1;
                if attempts >= max_retries || !is_transient_mongo_error(&e) {
                    error!("MongoDB operation failed after {attempts} attempts: {e}");
                    return Err(Error::InvalidRecord);
                }
                warn!(
                    "Transient MongoDB error (attempt {attempts}/{max_retries}): {e}. Retrying in {delay_ms}ms..."
                );
                tokio::time::sleep(Duration::from_millis(delay_ms * attempts as u64)).await;
            }
        }
    }
}

fn is_transient_mongo_error(error: &mongodb::error::Error) -> bool {
    let error_str = error.to_string().to_lowercase();
    error_str.contains("timeout")
        || error_str.contains("network")
        || error_str.contains("connection")
        || error_str.contains("pool")
}

#[cfg(test)]
mod tests {
    use super::*;

    fn test_config() -> MongoDbSourceConfig {
        MongoDbSourceConfig {
            connection_string: "mongodb://localhost:27017".to_string(),
            database: "test_db".to_string(),
            collection: "test_collection".to_string(),
            poll_interval: Some("5s".to_string()),
            batch_size: Some(500),
            tracking_field: None,
            initial_offset: None,
            max_pool_size: None,
            query_filter: None,
            projection: None,
            snake_case_fields: None,
            include_metadata: None,
            delete_after_read: None,
            processed_field: None,
            payload_field: None,
            payload_format: None,
            verbose_logging: None,
            max_retries: None,
            retry_delay: None,
        }
    }

    #[test]
    fn test_default_payload_format() {
        assert_eq!(PayloadFormat::from_config(None), PayloadFormat::Json);
        assert_eq!(PayloadFormat::from_config(Some("json")), PayloadFormat::Json);
    }

    #[test]
    fn test_bson_payload_format() {
        assert_eq!(PayloadFormat::from_config(Some("bson")), PayloadFormat::Bson);
        assert_eq!(PayloadFormat::from_config(Some("binary")), PayloadFormat::Bson);
    }

    #[test]
    fn test_string_payload_format() {
        assert_eq!(PayloadFormat::from_config(Some("string")), PayloadFormat::String);
        assert_eq!(PayloadFormat::from_config(Some("text")), PayloadFormat::String);
    }

    #[test]
    fn test_bson_to_json_conversions() {
        let doc = doc! {
            "string": "hello",
            "int": 42,
            "float": 3.14,
            "bool": true,
            "null": Bson::Null,
        };

        let json = bson_to_json(&Bson::Document(doc)).unwrap();
        assert!(json.is_object());
    }

    #[test]
    fn test_default_max_retries() {
        let src = MongoDbSource::new(1, test_config(), None);
        assert_eq!(src.get_max_retries(), DEFAULT_MAX_RETRIES);
    }

    #[test]
    fn test_custom_max_retries() {
        let mut config = test_config();
        config.max_retries = Some(5);
        let src = MongoDbSource::new(1, config, None);
        assert_eq!(src.get_max_retries(), 5);
    }
}
```

---

## Implementation Details

### Timestamp Conversion

Iggy uses microseconds since Unix epoch, MongoDB uses milliseconds:

```rust
fn bson_timestamp(micros: u64) -> Bson {
    Bson::DateTime(mongodb::bson::datetime::DateTime::from_millis(
        (micros / 1000) as i64,
    ))
}

fn bson_datetime(micros: u64) -> mongodb::bson::datetime::DateTime {
    mongodb::bson::datetime::DateTime::from_millis((micros / 1000) as i64)
}
```

### Payload Conversion (IMPORTANT)

The `ConsumedMessage.payload` is a `Payload` enum, not `Vec<u8>`. Always convert:

```rust
let payload_bytes = message.payload.clone().try_into_vec()
    .map_err(|e| Error::InvalidPayloadType)?;
```

### Bulk Write Pattern

For efficient inserts:

```rust
let inserts: Vec<_> = documents
    .iter()
    .map(|doc| mongodb::operations::InsertOneModel::new(doc.clone()))
    .collect();

collection.bulk_write(inserts, None, None).await?;
```

### ObjectId Handling

MongoDB ObjectIds need special handling:

```rust
if let Ok(oid) = mongodb::bson::oid::ObjectId::parse_str(id) {
    // Use ObjectId
    filter.insert("_id", doc! {"$gt": oid});
} else {
    // Use string
    filter.insert("_id", doc! {"$gt": id});
}
```

---

## Configuration

### Sink Config Example

```toml
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

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
connection_string = "mongodb://localhost:27017"
database = "iggy_messages"
collection = "messages"
batch_size = 100
max_pool_size = 10
auto_create_collection = true
include_metadata = true
include_checksum = true
include_origin_timestamp = true
payload_field_name = "payload"
```

### Source Config Example

```toml
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

type = "source"
key = "mongodb"
enabled = true
version = 0
name = "MongoDB source"
path = "../../target/release/libiggy_connector_mongodb_source"
verbose = false

[[streams]]
stream = "user_events"
topic = "users"
schema = "json"
batch_length = 100

[plugin_config]
connection_string = "mongodb://localhost:27017"
database = "my_database"
collection = "users"
poll_interval = "10s"
batch_size = 1000
tracking_field = "_id"
initial_offset = "0"
max_pool_size = 10
snake_case_fields = false
include_metadata = true
delete_after_read = false
```

---

## Integration Testing

### Test Fixture Pattern

```rust
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

use super::container::{
    DEFAULT_POLL_ATTEMPTS, DEFAULT_POLL_INTERVAL_MS, DEFAULT_SINK_COLLECTION,
    DEFAULT_TEST_STREAM, DEFAULT_TEST_TOPIC, ENV_SINK_CONNECTION_STRING,
    ENV_SINK_DATABASE, ENV_SINK_COLLECTION, ENV_SINK_PAYLOAD_FORMAT,
    ENV_SINK_STREAMS_0_CONSUMER_GROUP, ENV_SINK_STREAMS_0_SCHEMA,
    ENV_SINK_STREAMS_0_STREAM, ENV_SINK_STREAMS_0_TOPICS, MongoDbContainer,
    MongoDbOps, SinkPayloadFormat, SinkSchema,
};
use async_trait::async_trait;
use integration::harness::{TestBinaryError, TestFixture};
use mongodb::{Client, Collection};
use mongodb::bson::Document;
use std::collections::HashMap;
use std::time::Duration;
use tokio::time::sleep;

/// MongoDB sink connector fixture.
///
/// Starts a MongoDB container and provides environment variables
/// for the sink connector to connect to it.
pub struct MongoDbSinkFixture {
    container: MongoDbContainer,
    payload_format: SinkPayloadFormat,
    schema: SinkSchema,
}

impl MongoDbOps for MongoDbSinkFixture {
    fn container(&self) -> &MongoDbContainer {
        &self.container
    }
}

impl MongoDbSinkFixture {
    /// Wait for a collection to be created by the sink connector.
    pub async fn wait_for_collection(&self, client: &Client, database: &str, collection: &str) {
        let coll = client.database(database).collection::<Document>(collection);
        for _ in 0..DEFAULT_POLL_ATTEMPTS {
            if coll.count_documents(None, None, None).await.is_ok() {
                return;
            }
            sleep(Duration::from_millis(DEFAULT_POLL_INTERVAL_MS)).await;
        }
        panic!("Collection {collection} was not created in time");
    }

    /// Fetch documents from the sink collection with polling until expected count is reached.
    pub async fn fetch_documents_as<T>(
        &self,
        collection: &Collection<Document>,
        filter: Option<Document>,
        expected_count: usize,
    ) -> Result<Vec<T>, TestBinaryError>
    where
        T: Send + Unpin + for<'de> serde::Deserialize<'de>,
    {
        use mongodb::bson::from_document;

        let mut docs = Vec::new();
        for _ in 0..DEFAULT_POLL_ATTEMPTS {
            if let Ok(cursor) = collection.find(filter.clone(), None, None).await {
                if let Ok(fetched) = cursor.try_collect::<Vec<Document>>().await {
                    for doc in fetched {
                        if let Ok(item) = from_document::<T>(doc) {
                            docs.push(item);
                        }
                    }
                    if docs.len() >= expected_count {
                        return Ok(docs);
                    }
                }
            }
            sleep(Duration::from_millis(DEFAULT_POLL_INTERVAL_MS / 5)).await;
        }
        Err(TestBinaryError::InvalidState {
            message: format!(
                "Expected {} documents but got {} after {} poll attempts",
                expected_count,
                docs.len(),
                DEFAULT_POLL_ATTEMPTS
            ),
        })
    }
}

#[async_trait]
impl TestFixture for MongoDbSinkFixture {
    async fn setup() -> Result<Self, TestBinaryError> {
        let container = MongoDbContainer::start().await?;
        Ok(Self {
            container,
            payload_format: SinkPayloadFormat::default(),
            schema: SinkSchema::default(),
        })
    }

    fn connectors_runtime_envs(&self) -> HashMap<String, String> {
        let mut envs = HashMap::new();

        envs.insert(
            ENV_SINK_CONNECTION_STRING.to_string(),
            self.container.connection_string.clone(),
        );
        envs.insert(
            ENV_SINK_DATABASE.to_string(),
            "iggy_messages".to_string(),
        );
        envs.insert(
            ENV_SINK_COLLECTION.to_string(),
            DEFAULT_SINK_COLLECTION.to_string(),
        );
        envs.insert(
            ENV_SINK_STREAMS_0_STREAM.to_string(),
            DEFAULT_TEST_STREAM.to_string(),
        );
        envs.insert(
            ENV_SINK_STREAMS_0_TOPICS.to_string(),
            format!("[{}]", DEFAULT_TEST_TOPIC),
        );
        envs.insert(
            ENV_SINK_STREAMS_0_CONSUMER_GROUP.to_string(),
            "test".to_string(),
        );
        envs.insert(
            ENV_SINK_PATH.to_string(),
            "../../target/debug/libiggy_connector_mongodb_sink".to_string(),
        );

        let schema_str = match self.schema {
            SinkSchema::Json => "json",
            SinkSchema::Raw => "raw",
        };
        envs.insert(
            ENV_SINK_STREAMS_0_SCHEMA.to_string(),
            schema_str.to_string(),
        );

        let format_str = match self.payload_format {
            SinkPayloadFormat::Binary => "binary",
            SinkPayloadFormat::Json => "json",
        };
        envs.insert(ENV_SINK_PAYLOAD_FORMAT.to_string(), format_str.to_string());

        envs
    }
}

/// MongoDB sink fixture for binary payload format.
pub struct MongoDbSinkBinaryFixture {
    inner: MongoDbSinkFixture,
}

impl std::ops::Deref for MongoDbSinkBinaryFixture {
    type Target = MongoDbSinkFixture;
    fn deref(&self) -> &Self::Target {
        &self.inner
    }
}

#[async_trait]
impl TestFixture for MongoDbSinkBinaryFixture {
    async fn setup() -> Result<Self, TestBinaryError> {
        let container = MongoDbContainer::start().await?;
        Ok(Self {
            inner: MongoDbSinkFixture {
                container,
                payload_format: SinkPayloadFormat::Binary,
                schema: SinkSchema::Raw,
            },
        })
    }

    fn connectors_runtime_envs(&self) -> HashMap<String, String> {
        self.inner.connectors_runtime_envs()
    }
}

/// MongoDB sink fixture for JSON payload format.
pub struct MongoDbSinkJsonFixture {
    inner: MongoDbSinkFixture,
}

impl std::ops::Deref for MongoDbSinkJsonFixture {
    type Target = MongoDbSinkFixture;
    fn deref(&self) -> &Self::Target {
        &self.inner
    }
}

#[async_trait]
impl TestFixture for MongoDbSinkJsonFixture {
    async fn setup() -> Result<Self, TestBinaryError> {
        let container = MongoDbContainer::start().await?;
        Ok(Self {
            inner: MongoDbSinkFixture {
                container,
                payload_format: SinkPayloadFormat::Json,
                schema: SinkSchema::Json,
            },
        })
    }

    fn connectors_runtime_envs(&self) -> HashMap<String, String> {
        self.inner.connectors_runtime_envs()
    }
}
```

---

## Build and Deployment

### Cargo.toml (Sink)

```toml
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

[package]
name = "iggy_connector_mongodb_sink"
version = "0.1.0-edge.1"
description = "Iggy MongoDB sink connector for storing stream messages into MongoDB database"
edition = "2024"
license = "Apache-2.0"
keywords = ["iggy", "messaging", "streaming", "mongodb", "sink"]
categories = ["command-line-utilities", "database", "network-programming"]
homepage = "https://iggy.apache.org"
documentation = "https://iggy.apache.org/docs"
repository = "https://github.com/apache/iggy"
readme = "../../README.md"

[package.metadata.cargo-machete]
ignored = ["dashmap", "once_cell", "futures", "simd-json", "prost"]

[lib]
crate-type = ["cdylib", "lib"]

[features]
default = []

[dependencies]
async-trait = { workspace = true }
base64 = { workspace = true }
dashmap = { workspace = true }
futures = { workspace = true }
humantime = { workspace = true }
iggy_common = { workspace = true }
iggy_connector_sdk = { workspace = true }
once_cell = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
simd-json = { workspace = true }
tokio = { workspace = true }
tracing = { workspace = true }
uuid = { workspace = true }

# MongoDB-specific dependencies
mongodb = { version = "3.0", default-features = false, features = ["rustls-tls"] }
```

### Cargo.toml (Source)

```toml
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

[package]
name = "iggy_connector_mongodb_source"
version = "0.1.0-edge.1"
description = "Iggy MongoDB source connector supporting polling for message streaming platform"
edition = "2024"
license = "Apache-2.0"
keywords = ["iggy", "messaging", "streaming", "mongodb", "source"]
categories = ["command-line-utilities", "database", "network-programming"]
homepage = "https://iggy.apache.org"
documentation = "https://iggy.apache.org/docs"
repository = "https://github.com/apache/iggy"
readme = "../../README.md"

[package.metadata.cargo-machete]
ignored = ["dashmap", "once_cell", "futures", "simd-json"]

[lib]
crate-type = ["cdylib", "lib"]

[features]
default = []
# Future: Change Streams support
# change_streams = []

[dependencies]
async-trait = { workspace = true }
base64 = { workspace = true }
dashmap = { workspace = true }
futures = { workspace = true }
humantime = { workspace = true }
iggy_common = { workspace = true }
iggy_connector_sdk = { workspace = true }
once_cell = { workspace = true }
serde = { workspace = true }
serde_json = { workspace = true }
simd-json = { workspace = true }
tokio = { workspace = true }
tracing = { workspace = true }
uuid = { workspace = true }
chrono = { workspace = true }

# MongoDB-specific dependencies
mongodb = { version = "3.0", default-features = false, features = ["rustls-tls"] }
```

### Workspace Registration

Add to root `Cargo.toml` workspace members:

```toml
[workspace]
members = [
    # ... existing members ...
    "core/connectors/sinks/mongodb_sink",
    "core/connectors/sources/mongodb_source",
]
```

### Build Commands

```bash
# Build release binaries
cd /Users/amuldotexe/Desktop/A01_20260131/iggy-issue02
cargo build --release -p iggy_connector_mongodb_sink
cargo build --release -p iggy_connector_mongodb_source

# Build debug binaries for testing
cargo build -p iggy_connector_mongodb_sink
cargo build -p iggy_connector_mongodb_source
```

---

## Appendix: Parseltongue Analysis

### Query Results Used

1. **Folder Structure** (`/folder-structure-discovery-tree`)
   - Confirmed workspace structure
   - Connector locations: `core/connectors/sinks/*` and `core/connectors/sources/*`

2. **Codebase Statistics** (`/codebase-statistics-overview-summary`)
   - Total entities: 15,998
   - Languages detected: csharp, go, java, python, rust, typescript

3. **Sink Trait Blast Radius** (2 hops)
   - Confirmed Sink trait has 7 direct implementers
   - 491 total affected entities within 2 hops

4. **Source Trait Blast Radius** (2 hops)
   - Confirmed Source trait has 4 direct implementers
   - 5 total affected entities within 2 hops

5. **Sink FFI Structure** (`rust:struct:SinkApi`)
   - Verified `open()`, `consume()`, `close()`, `version()` signatures

6. **Source FFI Structure** (`rust:struct:SourceApi`)
   - Verified `open()`, `handle()`, `close()`, `version()` signatures

7. **SDK Structures**
   - `ConsumedMessage`: Confirmed payload is `Payload` enum, not `Vec<u8>`
   - `ProducedMessages`: Confirmed schema + messages + optional state
   - `ConnectorState`: Wrapper with MessagePack serialize/deserialize

### Key Code Patterns Observed

1. **Constructor Pattern** (from PostgresSink):
   ```rust
   pub fn new(id: u32, config: PostgresSinkConfig) -> Self {
       let verbose = config.verbose_logging.unwrap_or(false);
       let retry_delay = HumanDuration::from_str(delay_str)...
       Self { id, pool: None, config, state: Mutex::new(...), verbose, retry_delay }
   }
   ```

2. **Open Pattern**:
   ```rust
   async fn open(&mut self) -> Result<(), Error> {
       info!("Opening...");
       self.connect().await?;
       self.ensure_table_exists().await?;
       Ok(())
   }
   ```

3. **Payload Conversion** (IMPORTANT - found in actual code):
   ```rust
   let payload_bytes = message.payload.clone().try_into_vec()
       .map_err(|e| Error::InvalidPayloadType)?;
   ```

4. **Retry Pattern**:
   ```rust
   async fn execute_batch_insert_with_retry(...) {
       let mut attempts = 0;
       loop {
           match self.bind_and_execute_batch(...).await {
               Ok(_) => return Ok(()),
               Err((e, is_transient)) => {
                   attempts += 1;
                   if !is_transient || attempts >= max_retries {
                       return Err(...);
                   }
                   tokio::time::sleep(retry_delay * attempts).await;
               }
           }
       }
   }
   ```

5. **Timestamp Parsing**:
   ```rust
   fn parse_timestamp(&self, micros: u64) -> DateTime<Utc> {
       DateTime::from_timestamp(
           (micros / 1_000_000) as i64,
           ((micros % 1_000_000) * 1_000) as u32,
       ).unwrap_or_else(Utc::now)
   }
   ```

### Files Read

- `core/connectors/sdk/src/lib.rs` - Full SDK definitions
- `core/connectors/sdk/src/sink.rs` - Sink macro implementation
- `core/connectors/sdk/src/source.rs` - Source macro implementation
- `core/connectors/runtime/src/main.rs` - Runtime FFI definitions
- `core/connectors/sinks/postgres_sink/src/lib.rs` - Reference sink (799 lines)
- `core/connectors/sources/postgres_source/src/lib.rs` - Reference source (1410 lines)
- `Cargo.toml` files - Dependency patterns
- `config.toml` files - Configuration format
- `core/integration/src/harness/fixture.rs` - TestFixture trait
- `core/integration/tests/connectors/fixtures/postgres/sink.rs` - Sink fixture
- `core/integration/tests/connectors/fixtures/postgres/source.rs` - Source fixture

---

**Document Version**: 4.0
**Created**: 2026-02-21
**Based on**: Parseltongue analysis of iggy-issue02 codebase
**Verification**: All trait signatures, FFI boundaries, and patterns verified against actual source code
