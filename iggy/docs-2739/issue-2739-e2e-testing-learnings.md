# E2E Testing Learnings: MongoDB Connectors for Apache Iggy

**Date**: February 22, 2026
**Status**: Implementation-ready (post rubberduck review)

---

## Rubberduck Review Notes

This section records every gap and contradiction found by talking through the original document against the actual codebase. These are the corrections that make the rest of this document trustworthy.

### Gap 1: "9 new files" was wrong

The original document said "9 new files (4 fixtures + 5 test modules)". After counting the elasticsearch and postgres patterns:

- `fixtures/mongodb/mod.rs` -- 1
- `fixtures/mongodb/container.rs` -- 1
- `fixtures/mongodb/sink.rs` -- 1
- `fixtures/mongodb/source.rs` -- 1
- `mongodb/mod.rs` -- 1
- `mongodb/mongodb_sink.rs` -- 1
- `mongodb/mongodb_source.rs` -- 1
- `mongodb/sink.toml` -- 1
- `mongodb/source.toml` -- 1

That is 9 files. But we also need to touch 2 existing files:

- `fixtures/mod.rs` -- add `mod mongodb;` and re-exports
- `connectors/mod.rs` -- add `mod mongodb;`

So: 9 new files + 2 modifications. The TL;DR line was misleading.

### Gap 2: The document said "use Mongo::repl_set() from testcontainers-modules"

The original document recommended `testcontainers-modules` with `Mongo::repl_set()`. This was pulled from library docs, not from examining how the actual iggy test suite works.

Looking at the actual code:

- Postgres uses `testcontainers-modules`: `postgres::Postgres::default().start().await` -- a first-class module.
- Elasticsearch uses `GenericImage`: `GenericImage::new("elasticsearch", "9.3.0")` -- no testcontainers-modules module exists for it.

The current workspace `Cargo.toml` has:
```toml
testcontainers-modules = { version = "0.14.0", features = ["postgres"] }
```

The `testcontainers-modules` crate does have a `mongo` feature. So we have two options:

**Option A**: Add `"mongo"` feature to `testcontainers-modules` -- gives us `testcontainers_modules::mongo::Mongo` with built-in replica set support.

**Option B**: Use `GenericImage` like Elasticsearch does -- simpler, matches one existing pattern, standalone mode is fine for polling-based connector (no change streams needed).

**Verdict**: Use `GenericImage` for v1. The source connector uses `find()` polling, not Change Streams. Replica set mode is required only for Change Streams (CDC). A standalone MongoDB instance is correct for these tests. If CDC is added in v2, switch to `Mongo::repl_set()`.

The `Cargo.toml` does NOT need a `"mongodb"` feature added to `testcontainers-modules`. The `GenericImage` approach uses only the base `testcontainers` crate which is already a transitive dependency.

### Gap 3: The env var names were guessed, not verified

The original document listed env var names like `IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_CONNECTION_URI` but these were derived by analogy, not confirmed from code.

Confirmed pattern from `fixtures/postgres/container.rs`:
```rust
// Sink env var structure:
"IGGY_CONNECTORS_SINK_{CONNECTOR_NAME}_PLUGIN_CONFIG_{FIELD_NAME}"
"IGGY_CONNECTORS_SINK_{CONNECTOR_NAME}_STREAMS_0_STREAM"
"IGGY_CONNECTORS_SINK_{CONNECTOR_NAME}_STREAMS_0_TOPICS"      // plural
"IGGY_CONNECTORS_SINK_{CONNECTOR_NAME}_STREAMS_0_SCHEMA"
"IGGY_CONNECTORS_SINK_{CONNECTOR_NAME}_STREAMS_0_CONSUMER_GROUP"
"IGGY_CONNECTORS_SINK_{CONNECTOR_NAME}_PATH"

// Source env var structure:
"IGGY_CONNECTORS_SOURCE_{CONNECTOR_NAME}_PLUGIN_CONFIG_{FIELD_NAME}"
"IGGY_CONNECTORS_SOURCE_{CONNECTOR_NAME}_STREAMS_0_STREAM"
"IGGY_CONNECTORS_SOURCE_{CONNECTOR_NAME}_STREAMS_0_TOPIC"     // singular (!)
"IGGY_CONNECTORS_SOURCE_{CONNECTOR_NAME}_STREAMS_0_SCHEMA"
"IGGY_CONNECTORS_SOURCE_{CONNECTOR_NAME}_PATH"
```

Critical difference: sink uses `STREAMS_0_TOPICS` (plural array), source uses `STREAMS_0_TOPIC` (singular). This must be exact.

For MongoDB the connector name in env vars is `MONGODB` (all caps, matching `POSTGRES`, `ELASTICSEARCH`):

```rust
// Sink:
"IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_CONNECTION_URI"
"IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_DATABASE"
"IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_COLLECTION"
"IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_PAYLOAD_FORMAT"
"IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_INCLUDE_METADATA"
"IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_AUTO_CREATE_COLLECTION"
"IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_BATCH_SIZE"
"IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_STREAM"
"IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_TOPICS"
"IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_SCHEMA"
"IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_CONSUMER_GROUP"
"IGGY_CONNECTORS_SINK_MONGODB_PATH"

// Source:
"IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_CONNECTION_URI"
"IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_DATABASE"
"IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_COLLECTION"
"IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_POLL_INTERVAL"
"IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_TRACKING_FIELD"
"IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_DELETE_AFTER_READ"
"IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_PROCESSED_FIELD"
"IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_INCLUDE_METADATA"
"IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_PAYLOAD_FORMAT"
"IGGY_CONNECTORS_SOURCE_MONGODB_STREAMS_0_STREAM"
"IGGY_CONNECTORS_SOURCE_MONGODB_STREAMS_0_TOPIC"
"IGGY_CONNECTORS_SOURCE_MONGODB_STREAMS_0_SCHEMA"
"IGGY_CONNECTORS_SOURCE_MONGODB_PATH"
```

### Gap 4: The connector binary path pattern was missing

Every fixture sets a `PATH` env var pointing to the compiled `.so`/`.dylib`. From postgres:
```rust
envs.insert(
    ENV_SINK_PATH.to_string(),
    "../../target/debug/libiggy_connector_postgres_sink".to_string(),
);
```

For MongoDB:
- Sink PATH: `"../../target/debug/libiggy_connector_mongodb_sink"`
- Source PATH: `"../../target/debug/libiggy_connector_mongodb_source"`

The crate names from `Cargo.toml` are `iggy_connector_mongodb_sink` and `iggy_connector_mongodb_source`, so on Linux the built artifact is `libiggy_connector_mongodb_sink.so` and on macOS it is `libiggy_connector_mongodb_sink.dylib`. The runtime appends the platform extension.

### Gap 5: The polling pattern for iggy messages was described correctly in prose but the code snippet was incomplete

The original document's `wait_for_documents` function described polling MongoDB for documents (sink test), but the source test pattern is different: poll iggy messages using `client.poll_messages()`. Both patterns exist and they are used in different test types. The original conflated them.

From actual postgres source tests, the correct iggy message polling loop is:
```rust
for _ in 0..POLL_ATTEMPTS {
    if let Ok(polled) = client
        .poll_messages(
            &stream_id,
            &topic_id,
            None,
            &Consumer::new(consumer_id.clone()),
            &PollingStrategy::next(),
            10,      // count per poll
            true,    // auto_commit
        )
        .await
    {
        for msg in polled.messages {
            // deserialize and push to received
        }
        if received.len() >= TEST_MESSAGE_COUNT {
            break;
        }
    }
    sleep(Duration::from_millis(POLL_INTERVAL_MS)).await;
}
```

Constants used: `POLL_ATTEMPTS = 100`, `POLL_INTERVAL_MS = 50`. These are defined in `mod.rs` of the test module, not in the fixture.

### Gap 6: "5 sink tests and 6 source tests" included tests that do not match connector behavior

Original test `metadata_fields_included` was a separate test. In postgres, metadata verification is folded into the main sink test (it checks `iggy_offset`, `iggy_stream`, `iggy_topic` columns in the same SELECT). We should do the same: metadata verification is part of `json_messages_sink_to_mongodb`, not a separate test.

Original test `offset_tracking_across_polls` requires the connector to run two full poll cycles in a single test run. This is difficult without being able to pause/resume the connector, and the postgres tests do not do this. The "restart" test (`state_persists_across_connector_restart`) covers offset persistence across a stop/start cycle, which tests offset tracking indirectly. Drop `offset_tracking_across_polls` as a standalone test.

Original test `payload_format_json_emits_schema_json` is a unit test concern, not an E2E concern. The schema is set by the connector based on config and is an internal concern. Remove from E2E list.

After pruning: **4 sink tests**, **4 source tests**.

### Gap 7: The document says TestFixture trait with methods "setup()" -- let's confirm the trait signature

From `fixtures/postgres/sink.rs`:
```rust
#[async_trait]
impl TestFixture for PostgresSinkFixture {
    async fn setup() -> Result<Self, TestBinaryError> { ... }
    fn connectors_runtime_envs(&self) -> HashMap<String, String> { ... }
}
```

Two required methods: `setup()` and `connectors_runtime_envs()`. No teardown method -- cleanup is handled by container drop.

### Gap 8: The "state_persists_across_restart" test uses `harness: &mut TestHarness`

In `postgres_source.rs`, the restart test signature is:
```rust
async fn state_persists_across_connector_restart(
    harness: &mut TestHarness,   // mutable reference, not shared reference
    fixture: PostgresSourceJsonFixture,
)
```

And it calls:
```rust
harness.server_mut().stop_dependents().expect("Failed to stop connectors");
harness.server_mut().start_dependents().await.expect("Failed to restart connectors");
sleep(Duration::from_secs(2)).await;
```

The MongoDB restart test must use `&mut TestHarness` and the same `stop_dependents()` / `start_dependents()` API.

### Gap 9: The sink.toml and source.toml content was never specified

Postgres has:
```toml
[connectors]
config_type = "local"
config_dir = "../connectors/sinks/postgres_sink"
```

MongoDB sink.toml and source.toml must follow the same pattern, pointing to the connector's own config directory which contains `config.toml`:
```toml
# sink.toml
[connectors]
config_type = "local"
config_dir = "../connectors/sinks/mongodb_sink"

# source.toml
[connectors]
config_type = "local"
config_dir = "../connectors/sources/mongodb_source"
```

### Gap 10: MongoDB client in test code

The sink tests need to query MongoDB to verify documents were inserted. The Elasticsearch tests use an HTTP client (`reqwest`). For MongoDB, we should use the `mongodb` driver crate directly in the fixture, since it is already a workspace dependency (both connector crates depend on it). This is more natural than going through an HTTP layer.

The fixture's `container.rs` should expose a method to create a `mongodb::Client` for the test to use for verification.

### Gap 11: The "auto_create_collection" sink test description was wrong

The original doc said: "Collection exists before any messages sent when config enabled." But looking at the sink source code, `ensure_collection_exists()` is called during `open()`. The test should verify the collection exists **before any messages are sent** (just after the connector opens). The correct approach: connect to MongoDB directly using the test client, list collection names, assert the collection is present -- without sending any messages. This is a lightweight test.

### Gap 12: Document metadata fields -- sink vs source

The sink's metadata fields (from `insert_batch` in `lib.rs`) are:
- `_id` (message ID as string)
- `iggy_offset` (i64)
- `iggy_timestamp` (BSON DateTime)
- `iggy_stream` (string)
- `iggy_topic` (string)
- `iggy_partition_id` (i32)
- `iggy_checksum` (i64, when `include_checksum=true`)
- `iggy_origin_timestamp` (BSON DateTime, when `include_origin_timestamp=true`)
- `payload` (Binary | Document | String depending on `payload_format`)

The source's metadata fields (from `document_to_message` when `include_metadata=true`):
- `_iggy_source_collection` (string)
- `_iggy_poll_timestamp` (string, RFC3339)

These are very different. The original document conflated them. Sink metadata fields appear in the MongoDB document. Source metadata fields appear in the iggy message payload.

---

## TL;DR (Corrected)

We need **8 E2E tests** across 2 tiers to validate the MongoDB connectors.

**Infrastructure**: 9 new files + 2 existing file modifications. GenericImage approach (no testcontainers-modules mongo feature needed). No Cargo.toml change required.

**Sink tests (4)**:
- JSON payload stored as BSON Document with metadata fields verified
- Binary payload stored as BSON Binary subtype Generic
- Large batch (50 messages) split across multiple inserts, all arrive
- Collection auto-created by `open()` before any messages sent

**Source tests (4)**:
- Seeded documents polled into iggy stream in correct order
- Delete-after-read removes documents from MongoDB post-poll
- Mark-processed sets field to true without deleting documents
- Restart survival: connector picks up from last offset, no duplicates

**Round-trip test**: Stretch goal, not in v1.

---

## References

| What | Where |
|---|---|
| Postgres fixture (canonical pattern) | `core/integration/tests/connectors/fixtures/postgres/` |
| Elasticsearch fixture (GenericImage pattern) | `core/integration/tests/connectors/fixtures/elasticsearch/` |
| Postgres sink tests (how tests use fixtures) | `core/integration/tests/connectors/postgres/postgres_sink.rs` |
| Postgres source tests | `core/integration/tests/connectors/postgres/postgres_source.rs` |
| Elasticsearch sink tests | `core/integration/tests/connectors/elasticsearch/elasticsearch_sink.rs` |
| MongoDB sink connector | `core/connectors/sinks/mongodb_sink/src/lib.rs` |
| MongoDB source connector | `core/connectors/sources/mongodb_source/src/lib.rs` |
| Sink config.toml | `core/connectors/sinks/mongodb_sink/config.toml` |
| Source config.toml | `core/connectors/sources/mongodb_source/config.toml` |
| Workspace Cargo.toml | `Cargo.toml` (line 278: testcontainers-modules features) |

---

## Infrastructure: What to Build

### File Map

```
core/integration/tests/connectors/
  fixtures/
    mod.rs                          -- MODIFY: add `mod mongodb;` and re-exports
    mongodb/
      mod.rs                        -- NEW
      container.rs                  -- NEW
      sink.rs                       -- NEW
      source.rs                     -- NEW
  mongodb/                          -- NEW directory
    mod.rs                          -- NEW
    mongodb_sink.rs                 -- NEW: 4 sink tests
    mongodb_source.rs               -- NEW: 4 source tests
    sink.toml                       -- NEW
    source.toml                     -- NEW
```

`core/integration/tests/connectors/mod.rs` -- MODIFY: add `mod mongodb;`

### Cargo.toml Change

None required. `GenericImage` comes from `testcontainers-modules::testcontainers` which is already a transitive dependency. The `mongodb` driver is already a dependency of the connector crates.

However, the integration test crate needs `mongodb` as a **direct** dev-dependency to query MongoDB for verification in tests. Check whether it is already in `core/integration/Cargo.toml`. If not, add:
```toml
mongodb = { version = "3.0", features = ["rustls-tls"] }
```

### sink.toml

```toml
# core/integration/tests/connectors/mongodb/sink.toml
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

[connectors]
config_type = "local"
config_dir = "../connectors/sinks/mongodb_sink"
```

### source.toml

```toml
# core/integration/tests/connectors/mongodb/source.toml
[connectors]
config_type = "local"
config_dir = "../connectors/sources/mongodb_source"
```

(Same Apache license header as sink.toml.)

---

## Fixture Implementation

### container.rs

Uses `GenericImage` exactly like Elasticsearch. MongoDB 7 is the current LTS. Use `"Waiting for connections"` as the readiness message (standard MongoDB startup log).

```rust
use integration::harness::TestBinaryError;
use mongodb::{options::ClientOptions, Client};
use testcontainers_modules::testcontainers::core::{IntoContainerPort, WaitFor};
use testcontainers_modules::testcontainers::runners::AsyncRunner;
use testcontainers_modules::testcontainers::{ContainerAsync, GenericImage, ImageExt};
use tracing::info;

const MONGODB_IMAGE: &str = "mongo";
const MONGODB_TAG: &str = "7";
const MONGODB_PORT: u16 = 27017;
const MONGODB_READY_MSG: &str = "Waiting for connections";

pub(super) const DEFAULT_TEST_STREAM: &str = "test_stream";
pub(super) const DEFAULT_TEST_TOPIC: &str = "test_topic";
pub(super) const DEFAULT_SINK_COLLECTION: &str = "iggy_messages";
pub(super) const DEFAULT_TEST_DATABASE: &str = "iggy_test";

pub(super) const HEALTH_CHECK_ATTEMPTS: usize = 30;
pub(super) const HEALTH_CHECK_INTERVAL_MS: u64 = 500;
pub(super) const DEFAULT_POLL_ATTEMPTS: usize = 100;
pub(super) const DEFAULT_POLL_INTERVAL_MS: u64 = 50;

// Sink env vars
pub(super) const ENV_SINK_CONNECTION_URI: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_CONNECTION_URI";
pub(super) const ENV_SINK_DATABASE: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_DATABASE";
pub(super) const ENV_SINK_COLLECTION: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_COLLECTION";
pub(super) const ENV_SINK_PAYLOAD_FORMAT: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_PAYLOAD_FORMAT";
pub(super) const ENV_SINK_INCLUDE_METADATA: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_INCLUDE_METADATA";
pub(super) const ENV_SINK_AUTO_CREATE_COLLECTION: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_AUTO_CREATE_COLLECTION";
pub(super) const ENV_SINK_BATCH_SIZE: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_PLUGIN_CONFIG_BATCH_SIZE";
pub(super) const ENV_SINK_STREAMS_0_STREAM: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_STREAM";
pub(super) const ENV_SINK_STREAMS_0_TOPICS: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_TOPICS";
pub(super) const ENV_SINK_STREAMS_0_SCHEMA: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_SCHEMA";
pub(super) const ENV_SINK_STREAMS_0_CONSUMER_GROUP: &str =
    "IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_CONSUMER_GROUP";
pub(super) const ENV_SINK_PATH: &str = "IGGY_CONNECTORS_SINK_MONGODB_PATH";

// Source env vars
pub(super) const ENV_SOURCE_CONNECTION_URI: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_CONNECTION_URI";
pub(super) const ENV_SOURCE_DATABASE: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_DATABASE";
pub(super) const ENV_SOURCE_COLLECTION: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_COLLECTION";
pub(super) const ENV_SOURCE_POLL_INTERVAL: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_POLL_INTERVAL";
pub(super) const ENV_SOURCE_TRACKING_FIELD: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_TRACKING_FIELD";
pub(super) const ENV_SOURCE_DELETE_AFTER_READ: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_DELETE_AFTER_READ";
pub(super) const ENV_SOURCE_PROCESSED_FIELD: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_PROCESSED_FIELD";
pub(super) const ENV_SOURCE_INCLUDE_METADATA: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_INCLUDE_METADATA";
pub(super) const ENV_SOURCE_PAYLOAD_FORMAT: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_PLUGIN_CONFIG_PAYLOAD_FORMAT";
pub(super) const ENV_SOURCE_STREAMS_0_STREAM: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_STREAMS_0_STREAM";
pub(super) const ENV_SOURCE_STREAMS_0_TOPIC: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_STREAMS_0_TOPIC";
pub(super) const ENV_SOURCE_STREAMS_0_SCHEMA: &str =
    "IGGY_CONNECTORS_SOURCE_MONGODB_STREAMS_0_SCHEMA";
pub(super) const ENV_SOURCE_PATH: &str = "IGGY_CONNECTORS_SOURCE_MONGODB_PATH";

pub struct MongoDbContainer {
    #[allow(dead_code)]
    container: ContainerAsync<GenericImage>,
    pub(super) connection_uri: String,
}

impl MongoDbContainer {
    pub(super) async fn start() -> Result<Self, TestBinaryError> {
        let container = GenericImage::new(MONGODB_IMAGE, MONGODB_TAG)
            .with_exposed_port(MONGODB_PORT.tcp())
            .with_wait_for(WaitFor::message_on_stdout(MONGODB_READY_MSG))
            .with_mapped_port(0, MONGODB_PORT.tcp())
            .start()
            .await
            .map_err(|e| TestBinaryError::FixtureSetup {
                fixture_type: "MongoDbContainer".to_string(),
                message: format!("Failed to start container: {e}"),
            })?;

        info!("Started MongoDB container");

        let mapped_port = container
            .ports()
            .await
            .map_err(|e| TestBinaryError::FixtureSetup {
                fixture_type: "MongoDbContainer".to_string(),
                message: format!("Failed to get ports: {e}"),
            })?
            .map_to_host_port_ipv4(MONGODB_PORT)
            .ok_or_else(|| TestBinaryError::FixtureSetup {
                fixture_type: "MongoDbContainer".to_string(),
                message: "No mapping for MongoDB port".to_string(),
            })?;

        // Standalone mode: plain URI. No ?directConnection=true needed
        // (directConnection is only required for single-node replica sets).
        let connection_uri = format!("mongodb://localhost:{mapped_port}");

        info!("MongoDB container available at {connection_uri}");

        Ok(Self {
            container,
            connection_uri,
        })
    }

    pub async fn create_client(&self) -> Result<Client, TestBinaryError> {
        let options = ClientOptions::parse(&self.connection_uri)
            .await
            .map_err(|e| TestBinaryError::FixtureSetup {
                fixture_type: "MongoDbContainer".to_string(),
                message: format!("Failed to parse URI: {e}"),
            })?;

        Client::with_options(options).map_err(|e| TestBinaryError::FixtureSetup {
            fixture_type: "MongoDbContainer".to_string(),
            message: format!("Failed to create client: {e}"),
        })
    }
}

/// Common MongoDB operations for fixtures.
pub trait MongoDbOps: Sync {
    fn container(&self) -> &MongoDbContainer;

    fn create_client(
        &self,
    ) -> impl std::future::Future<Output = Result<Client, TestBinaryError>> + Send {
        self.container().create_client()
    }
}
```

### sink.rs

Three fixtures: base `MongoDbSinkFixture`, `MongoDbSinkJsonFixture` (payload_format=json), and `MongoDbSinkAutoCreateFixture` (auto_create_collection=true). The base fixture stores documents as Binary (default).

The fixture exposes a `wait_for_documents()` polling helper that queries MongoDB directly using the `mongodb` crate.

```rust
use super::container::{
    DEFAULT_POLL_ATTEMPTS, DEFAULT_POLL_INTERVAL_MS, DEFAULT_SINK_COLLECTION,
    DEFAULT_TEST_DATABASE, DEFAULT_TEST_STREAM, DEFAULT_TEST_TOPIC,
    ENV_SINK_AUTO_CREATE_COLLECTION, ENV_SINK_BATCH_SIZE, ENV_SINK_COLLECTION,
    ENV_SINK_CONNECTION_URI, ENV_SINK_DATABASE, ENV_SINK_INCLUDE_METADATA, ENV_SINK_PATH,
    ENV_SINK_PAYLOAD_FORMAT, ENV_SINK_STREAMS_0_CONSUMER_GROUP, ENV_SINK_STREAMS_0_SCHEMA,
    ENV_SINK_STREAMS_0_STREAM, ENV_SINK_STREAMS_0_TOPICS, MongoDbContainer, MongoDbOps,
};
use async_trait::async_trait;
use integration::harness::{TestBinaryError, TestFixture};
use mongodb::{Client, bson::Document};
use std::collections::HashMap;
use std::time::Duration;
use tokio::time::sleep;
use tracing::info;

pub struct MongoDbSinkFixture {
    container: MongoDbContainer,
    payload_format: &'static str,
    auto_create: bool,
}

impl MongoDbOps for MongoDbSinkFixture {
    fn container(&self) -> &MongoDbContainer {
        &self.container
    }
}

impl MongoDbSinkFixture {
    pub async fn wait_for_documents(
        &self,
        client: &Client,
        collection_name: &str,
        expected: usize,
    ) -> Result<Vec<Document>, TestBinaryError> {
        let db = client.database(DEFAULT_TEST_DATABASE);
        let collection = db.collection::<Document>(collection_name);

        for _ in 0..DEFAULT_POLL_ATTEMPTS {
            let cursor = collection
                .find(mongodb::bson::doc! {})
                .sort(mongodb::bson::doc! { "iggy_offset": 1 })
                .await;

            if let Ok(mut c) = cursor {
                use futures::TryStreamExt;
                if let Ok(docs) = c.try_collect::<Vec<_>>().await {
                    if docs.len() >= expected {
                        info!("Found {} documents in MongoDB collection '{collection_name}'", docs.len());
                        return Ok(docs);
                    }
                }
            }
            sleep(Duration::from_millis(DEFAULT_POLL_INTERVAL_MS)).await;
        }

        Err(TestBinaryError::InvalidState {
            message: format!(
                "Expected at least {expected} documents in '{collection_name}' after {} attempts",
                DEFAULT_POLL_ATTEMPTS
            ),
        })
    }

    pub async fn count_documents_in_collection(
        &self,
        client: &Client,
        collection_name: &str,
    ) -> Result<u64, TestBinaryError> {
        let db = client.database(DEFAULT_TEST_DATABASE);
        let collection = db.collection::<Document>(collection_name);
        collection.count_documents(mongodb::bson::doc! {}).await.map_err(|e| {
            TestBinaryError::InvalidState {
                message: format!("Failed to count documents: {e}"),
            }
        })
    }

    pub async fn collection_exists(
        &self,
        client: &Client,
        collection_name: &str,
    ) -> Result<bool, TestBinaryError> {
        let db = client.database(DEFAULT_TEST_DATABASE);
        let names = db.list_collection_names().await.map_err(|e| TestBinaryError::InvalidState {
            message: format!("Failed to list collections: {e}"),
        })?;
        Ok(names.contains(&collection_name.to_string()))
    }
}

#[async_trait]
impl TestFixture for MongoDbSinkFixture {
    async fn setup() -> Result<Self, TestBinaryError> {
        let container = MongoDbContainer::start().await?;
        Ok(Self {
            container,
            payload_format: "binary",
            auto_create: false,
        })
    }

    fn connectors_runtime_envs(&self) -> HashMap<String, String> {
        let mut envs = HashMap::new();
        envs.insert(
            ENV_SINK_CONNECTION_URI.to_string(),
            self.container.connection_uri.clone(),
        );
        envs.insert(ENV_SINK_DATABASE.to_string(), DEFAULT_TEST_DATABASE.to_string());
        envs.insert(ENV_SINK_COLLECTION.to_string(), DEFAULT_SINK_COLLECTION.to_string());
        envs.insert(ENV_SINK_PAYLOAD_FORMAT.to_string(), self.payload_format.to_string());
        envs.insert(ENV_SINK_INCLUDE_METADATA.to_string(), "true".to_string());
        envs.insert(
            ENV_SINK_STREAMS_0_STREAM.to_string(),
            DEFAULT_TEST_STREAM.to_string(),
        );
        envs.insert(
            ENV_SINK_STREAMS_0_TOPICS.to_string(),
            format!("[{}]", DEFAULT_TEST_TOPIC),
        );
        envs.insert(ENV_SINK_STREAMS_0_SCHEMA.to_string(), "json".to_string());
        envs.insert(
            ENV_SINK_STREAMS_0_CONSUMER_GROUP.to_string(),
            "mongodb_sink_cg".to_string(),
        );
        envs.insert(
            ENV_SINK_PATH.to_string(),
            "../../target/debug/libiggy_connector_mongodb_sink".to_string(),
        );
        if self.auto_create {
            envs.insert(ENV_SINK_AUTO_CREATE_COLLECTION.to_string(), "true".to_string());
        }
        envs
    }
}

/// Sink fixture with JSON payload format.
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
                payload_format: "json",
                auto_create: false,
            },
        })
    }

    fn connectors_runtime_envs(&self) -> HashMap<String, String> {
        let mut envs = self.inner.connectors_runtime_envs();
        // Schema must be "json" for the runtime to route messages correctly.
        // Already set in base, but override STREAMS_0_SCHEMA just to be explicit.
        envs.insert(ENV_SINK_STREAMS_0_SCHEMA.to_string(), "json".to_string());
        envs
    }
}

/// Sink fixture with auto_create_collection enabled.
pub struct MongoDbSinkAutoCreateFixture {
    inner: MongoDbSinkFixture,
}

impl std::ops::Deref for MongoDbSinkAutoCreateFixture {
    type Target = MongoDbSinkFixture;
    fn deref(&self) -> &Self::Target {
        &self.inner
    }
}

#[async_trait]
impl TestFixture for MongoDbSinkAutoCreateFixture {
    async fn setup() -> Result<Self, TestBinaryError> {
        let container = MongoDbContainer::start().await?;
        Ok(Self {
            inner: MongoDbSinkFixture {
                container,
                payload_format: "binary",
                auto_create: true,
            },
        })
    }

    fn connectors_runtime_envs(&self) -> HashMap<String, String> {
        // auto_create flag is set in the base connectors_runtime_envs()
        self.inner.connectors_runtime_envs()
    }
}
```

### source.rs

Three fixtures: `MongoDbSourceFixture` (base, json format), `MongoDbSourceDeleteFixture` (delete_after_read=true), `MongoDbSourceMarkFixture` (processed_field=is_processed).

The fixture exposes `seed_documents()` for inserting test documents directly into MongoDB, and `count_documents()` for post-poll verification.

```rust
use super::container::{
    DEFAULT_TEST_DATABASE, DEFAULT_TEST_STREAM, DEFAULT_TEST_TOPIC,
    ENV_SOURCE_COLLECTION, ENV_SOURCE_CONNECTION_URI, ENV_SOURCE_DATABASE,
    ENV_SOURCE_DELETE_AFTER_READ, ENV_SOURCE_PATH, ENV_SOURCE_PAYLOAD_FORMAT,
    ENV_SOURCE_POLL_INTERVAL, ENV_SOURCE_PROCESSED_FIELD,
    ENV_SOURCE_STREAMS_0_SCHEMA, ENV_SOURCE_STREAMS_0_STREAM, ENV_SOURCE_STREAMS_0_TOPIC,
    ENV_SOURCE_TRACKING_FIELD, MongoDbContainer, MongoDbOps,
};
use async_trait::async_trait;
use integration::harness::{TestBinaryError, TestFixture};
use mongodb::{Client, bson::Document};
use std::collections::HashMap;

const SOURCE_COLLECTION: &str = "test_events";

pub struct MongoDbSourceFixture {
    container: MongoDbContainer,
}

impl MongoDbOps for MongoDbSourceFixture {
    fn container(&self) -> &MongoDbContainer {
        &self.container
    }
}

impl MongoDbSourceFixture {
    pub fn collection_name(&self) -> &str {
        SOURCE_COLLECTION
    }

    /// Insert documents with integer `seq` field used as tracking field.
    pub async fn seed_documents(
        &self,
        client: &Client,
        docs: Vec<Document>,
    ) -> Result<(), TestBinaryError> {
        let db = client.database(DEFAULT_TEST_DATABASE);
        let collection = db.collection::<Document>(SOURCE_COLLECTION);
        collection.insert_many(docs).await.map_err(|e| TestBinaryError::FixtureSetup {
            fixture_type: "MongoDbSourceFixture".to_string(),
            message: format!("Failed to insert documents: {e}"),
        })?;
        Ok(())
    }

    pub async fn count_documents(&self, client: &Client) -> Result<u64, TestBinaryError> {
        let db = client.database(DEFAULT_TEST_DATABASE);
        let collection = db.collection::<Document>(SOURCE_COLLECTION);
        collection.count_documents(mongodb::bson::doc! {}).await.map_err(|e| {
            TestBinaryError::InvalidState {
                message: format!("Failed to count documents: {e}"),
            }
        })
    }

    pub async fn count_processed_documents(&self, client: &Client) -> Result<u64, TestBinaryError> {
        let db = client.database(DEFAULT_TEST_DATABASE);
        let collection = db.collection::<Document>(SOURCE_COLLECTION);
        collection
            .count_documents(mongodb::bson::doc! { "is_processed": true })
            .await
            .map_err(|e| TestBinaryError::InvalidState {
                message: format!("Failed to count processed documents: {e}"),
            })
    }
}

#[async_trait]
impl TestFixture for MongoDbSourceFixture {
    async fn setup() -> Result<Self, TestBinaryError> {
        let container = MongoDbContainer::start().await?;
        Ok(Self { container })
    }

    fn connectors_runtime_envs(&self) -> HashMap<String, String> {
        let mut envs = HashMap::new();
        envs.insert(
            ENV_SOURCE_CONNECTION_URI.to_string(),
            self.container.connection_uri.clone(),
        );
        envs.insert(ENV_SOURCE_DATABASE.to_string(), DEFAULT_TEST_DATABASE.to_string());
        envs.insert(ENV_SOURCE_COLLECTION.to_string(), SOURCE_COLLECTION.to_string());
        envs.insert(ENV_SOURCE_POLL_INTERVAL.to_string(), "10ms".to_string());
        envs.insert(ENV_SOURCE_TRACKING_FIELD.to_string(), "seq".to_string());
        envs.insert(ENV_SOURCE_PAYLOAD_FORMAT.to_string(), "json".to_string());
        envs.insert(
            ENV_SOURCE_STREAMS_0_STREAM.to_string(),
            DEFAULT_TEST_STREAM.to_string(),
        );
        envs.insert(
            ENV_SOURCE_STREAMS_0_TOPIC.to_string(),
            DEFAULT_TEST_TOPIC.to_string(),
        );
        envs.insert(ENV_SOURCE_STREAMS_0_SCHEMA.to_string(), "json".to_string());
        envs.insert(
            ENV_SOURCE_PATH.to_string(),
            "../../target/debug/libiggy_connector_mongodb_source".to_string(),
        );
        envs
    }
}

/// Source fixture with delete_after_read enabled.
pub struct MongoDbSourceDeleteFixture {
    inner: MongoDbSourceFixture,
}

impl std::ops::Deref for MongoDbSourceDeleteFixture {
    type Target = MongoDbSourceFixture;
    fn deref(&self) -> &Self::Target {
        &self.inner
    }
}

#[async_trait]
impl TestFixture for MongoDbSourceDeleteFixture {
    async fn setup() -> Result<Self, TestBinaryError> {
        let container = MongoDbContainer::start().await?;
        Ok(Self {
            inner: MongoDbSourceFixture { container },
        })
    }

    fn connectors_runtime_envs(&self) -> HashMap<String, String> {
        let mut envs = self.inner.connectors_runtime_envs();
        envs.insert(ENV_SOURCE_DELETE_AFTER_READ.to_string(), "true".to_string());
        envs
    }
}

/// Source fixture with is_processed field marking.
pub struct MongoDbSourceMarkFixture {
    inner: MongoDbSourceFixture,
}

impl std::ops::Deref for MongoDbSourceMarkFixture {
    type Target = MongoDbSourceFixture;
    fn deref(&self) -> &Self::Target {
        &self.inner
    }
}

#[async_trait]
impl TestFixture for MongoDbSourceMarkFixture {
    async fn setup() -> Result<Self, TestBinaryError> {
        let container = MongoDbContainer::start().await?;
        Ok(Self {
            inner: MongoDbSourceFixture { container },
        })
    }

    fn connectors_runtime_envs(&self) -> HashMap<String, String> {
        let mut envs = self.inner.connectors_runtime_envs();
        envs.insert(ENV_SOURCE_PROCESSED_FIELD.to_string(), "is_processed".to_string());
        envs
    }
}
```

### fixtures/mongodb/mod.rs

```rust
mod container;
mod sink;
mod source;

pub use container::MongoDbOps;
pub use sink::{MongoDbSinkAutoCreateFixture, MongoDbSinkFixture, MongoDbSinkJsonFixture};
pub use source::{MongoDbSourceDeleteFixture, MongoDbSourceFixture, MongoDbSourceMarkFixture};
```

---

## Test Module: mongodb/mod.rs

```rust
mod mongodb_sink;
mod mongodb_source;

const TEST_MESSAGE_COUNT: usize = 3;
const POLL_ATTEMPTS: usize = 100;
const POLL_INTERVAL_MS: u64 = 50;
```

---

## The 4 Sink Tests

### File: mongodb/mongodb_sink.rs

**Test 1: json_messages_sink_to_mongodb**

Purpose: Send 3 JSON messages via iggy, verify they appear in MongoDB as BSON Documents with correct metadata fields.

```rust
#[iggy_harness(
    server(connectors_runtime(config_path = "tests/connectors/mongodb/sink.toml")),
    seed = seeds::connector_stream
)]
async fn json_messages_sink_to_mongodb(harness: &TestHarness, fixture: MongoDbSinkJsonFixture) {
    let client = harness.root_client().await.unwrap();
    let mongo_client = fixture.create_client().await.expect("Failed to create MongoDB client");

    let stream_id: Identifier = seeds::names::STREAM.try_into().unwrap();
    let topic_id: Identifier = seeds::names::TOPIC.try_into().unwrap();

    let json_payloads: Vec<serde_json::Value> = vec![
        serde_json::json!({"name": "Alice", "age": 30}),
        serde_json::json!({"name": "Bob", "score": 99}),
        serde_json::json!({"name": "Carol", "active": true}),
    ];

    let mut messages: Vec<IggyMessage> = json_payloads
        .iter()
        .enumerate()
        .map(|(i, payload)| {
            let bytes = serde_json::to_vec(payload).expect("Failed to serialize");
            IggyMessage::builder()
                .id((i + 1) as u128)
                .payload(Bytes::from(bytes))
                .build()
                .expect("Failed to build message")
        })
        .collect();

    client
        .send_messages(&stream_id, &topic_id, &Partitioning::partition_id(0), &mut messages)
        .await
        .expect("Failed to send messages");

    // Wait for connector to consume and insert into MongoDB.
    let docs = fixture
        .wait_for_documents(&mongo_client, DEFAULT_SINK_COLLECTION, TEST_MESSAGE_COUNT)
        .await
        .expect("Documents did not appear in MongoDB");

    assert_eq!(docs.len(), TEST_MESSAGE_COUNT);

    // Verify metadata fields are present on first document.
    let first = &docs[0];
    assert!(
        first.contains_key("iggy_offset"),
        "Expected iggy_offset field"
    );
    assert!(
        first.contains_key("iggy_stream"),
        "Expected iggy_stream field"
    );
    assert!(
        first.contains_key("iggy_topic"),
        "Expected iggy_topic field"
    );
    assert!(
        first.contains_key("iggy_partition_id"),
        "Expected iggy_partition_id field"
    );
    assert!(
        first.contains_key("iggy_timestamp"),
        "Expected iggy_timestamp field"
    );
    // Verify offset sequence is contiguous.
    for (i, doc) in docs.iter().enumerate() {
        let offset = doc.get_i64("iggy_offset").expect("iggy_offset missing");
        assert_eq!(offset, i as i64, "Offset mismatch at document {i}");
    }
    // Verify payload is stored as a BSON Document (queryable) not Binary.
    let payload = first.get("payload").expect("payload field missing");
    assert!(
        matches!(payload, mongodb::bson::Bson::Document(_)),
        "Expected payload to be BSON Document for json format, got: {payload:?}"
    );
}
```

**Test 2: binary_messages_sink_as_bson_binary**

Purpose: Send raw bytes, verify stored as `BSON Binary (subtype: Generic)`.

```rust
#[iggy_harness(
    server(connectors_runtime(config_path = "tests/connectors/mongodb/sink.toml")),
    seed = seeds::connector_stream
)]
async fn binary_messages_sink_as_bson_binary(harness: &TestHarness, fixture: MongoDbSinkFixture) {
    let client = harness.root_client().await.unwrap();
    let mongo_client = fixture.create_client().await.expect("Failed to create MongoDB client");

    let stream_id: Identifier = seeds::names::STREAM.try_into().unwrap();
    let topic_id: Identifier = seeds::names::TOPIC.try_into().unwrap();

    let raw_payloads: Vec<Vec<u8>> = vec![
        b"plain text message".to_vec(),
        vec![0x00, 0x01, 0x02, 0xFF, 0xFE, 0xFD],
        vec![0xDE, 0xAD, 0xBE, 0xEF],
    ];

    let mut messages: Vec<IggyMessage> = raw_payloads
        .iter()
        .enumerate()
        .map(|(i, payload)| {
            IggyMessage::builder()
                .id((i + 1) as u128)
                .payload(Bytes::from(payload.clone()))
                .build()
                .expect("Failed to build message")
        })
        .collect();

    client
        .send_messages(&stream_id, &topic_id, &Partitioning::partition_id(0), &mut messages)
        .await
        .expect("Failed to send messages");

    let docs = fixture
        .wait_for_documents(&mongo_client, DEFAULT_SINK_COLLECTION, raw_payloads.len())
        .await
        .expect("Documents did not appear");

    assert_eq!(docs.len(), raw_payloads.len());

    for (i, doc) in docs.iter().enumerate() {
        let payload = doc.get("payload").expect("payload field missing");
        match payload {
            mongodb::bson::Bson::Binary(bin) => {
                assert_eq!(
                    bin.subtype,
                    mongodb::bson::spec::BinarySubtype::Generic,
                    "Expected Generic subtype at doc {i}"
                );
                assert_eq!(
                    bin.bytes, raw_payloads[i],
                    "Payload bytes mismatch at doc {i}"
                );
            }
            other => panic!("Expected Binary, got {other:?} at doc {i}"),
        }
    }
}
```

**Test 3: large_batch_processed_correctly**

Purpose: Send 50 messages with `batch_size=10`, verify all 50 arrive, no gaps in offsets.

```rust
#[iggy_harness(
    server(connectors_runtime(config_path = "tests/connectors/mongodb/sink.toml")),
    seed = seeds::connector_stream
)]
async fn large_batch_processed_correctly(harness: &TestHarness, fixture: MongoDbSinkFixture) {
    let client = harness.root_client().await.unwrap();
    let mongo_client = fixture.create_client().await.expect("Failed to create MongoDB client");

    let bulk_count = 50usize;

    let stream_id: Identifier = seeds::names::STREAM.try_into().unwrap();
    let topic_id: Identifier = seeds::names::TOPIC.try_into().unwrap();

    let mut messages: Vec<IggyMessage> = (0..bulk_count)
        .map(|i| {
            let payload = serde_json::to_vec(&serde_json::json!({"idx": i}))
                .expect("Failed to serialize");
            IggyMessage::builder()
                .id((i + 1) as u128)
                .payload(Bytes::from(payload))
                .build()
                .expect("Failed to build message")
        })
        .collect();

    client
        .send_messages(&stream_id, &topic_id, &Partitioning::partition_id(0), &mut messages)
        .await
        .expect("Failed to send messages");

    let docs = fixture
        .wait_for_documents(&mongo_client, DEFAULT_SINK_COLLECTION, bulk_count)
        .await
        .expect("Not all documents appeared");

    assert!(
        docs.len() >= bulk_count,
        "Expected at least {bulk_count} documents, got {}",
        docs.len()
    );

    // Verify offsets are contiguous (0..N).
    for (i, doc) in docs.iter().enumerate() {
        let offset = doc.get_i64("iggy_offset").expect("iggy_offset missing");
        assert_eq!(offset, i as i64, "Offset gap detected at position {i}");
    }
}
```

Note: `batch_size=10` must be set in the fixture `connectors_runtime_envs()` for this test via `ENV_SINK_BATCH_SIZE`. Options: create a dedicated fixture `MongoDbSinkBatchFixture`, or override in the test via an env injection mechanism (if the harness supports it). The simplest approach is to create a variant fixture that overrides `ENV_SINK_BATCH_SIZE` to `"10"`.

**Test 4: auto_create_collection_on_open**

Purpose: Verify the collection is created by `open()` without sending any messages.

```rust
#[iggy_harness(
    server(connectors_runtime(config_path = "tests/connectors/mongodb/sink.toml")),
    seed = seeds::connector_stream
)]
async fn auto_create_collection_on_open(
    harness: &TestHarness,
    fixture: MongoDbSinkAutoCreateFixture,
) {
    let mongo_client = fixture.create_client().await.expect("Failed to create MongoDB client");

    // The connector's open() creates the collection. We poll until it appears.
    // No messages sent.
    let mut found = false;
    for _ in 0..DEFAULT_POLL_ATTEMPTS {
        if fixture
            .collection_exists(&mongo_client, DEFAULT_SINK_COLLECTION)
            .await
            .unwrap_or(false)
        {
            found = true;
            break;
        }
        sleep(Duration::from_millis(DEFAULT_POLL_INTERVAL_MS)).await;
    }

    assert!(
        found,
        "Collection '{DEFAULT_SINK_COLLECTION}' was not created by open() within timeout"
    );

    // No messages sent -- collection should be empty.
    let count = fixture
        .count_documents_in_collection(&mongo_client, DEFAULT_SINK_COLLECTION)
        .await
        .expect("Failed to count");
    assert_eq!(count, 0, "Collection should be empty after open() with no messages");

    // Suppress unused harness warning.
    let _ = harness;
}
```

---

## The 4 Source Tests

### File: mongodb/mongodb_source.rs

**Tracking field consideration**: The source connector tracks offsets via a `tracking_field`. Using MongoDB's `_id` (ObjectId) as tracking field is the default, but comparing ObjectIds as strings in `$gt` queries requires care. For tests, use an integer `seq` field as the tracking field. This matches how the postgres source uses `id` as tracking column. Fixtures set `ENV_SOURCE_TRACKING_FIELD = "seq"`.

Documents to seed must have a `seq` field with integer values: `1, 2, 3, ...`.

**Test 1: source_polls_documents_to_iggy**

```rust
#[iggy_harness(
    server(connectors_runtime(config_path = "tests/connectors/mongodb/source.toml")),
    seed = seeds::connector_stream
)]
async fn source_polls_documents_to_iggy(harness: &TestHarness, fixture: MongoDbSourceFixture) {
    let client = harness.root_client().await.unwrap();
    let mongo_client = fixture.create_client().await.expect("Failed to create MongoDB client");

    // Seed documents before the connector starts polling.
    let docs: Vec<_> = (1..=TEST_MESSAGE_COUNT)
        .map(|i| {
            mongodb::bson::doc! {
                "seq": i as i64,
                "name": format!("event_{i}"),
                "value": (i * 10) as i64,
            }
        })
        .collect();
    fixture
        .seed_documents(&mongo_client, docs)
        .await
        .expect("Failed to seed documents");
    mongo_client.shutdown().await;

    let stream_id: Identifier = seeds::names::STREAM.try_into().unwrap();
    let topic_id: Identifier = seeds::names::TOPIC.try_into().unwrap();
    let consumer_id: Identifier = "test_consumer".try_into().unwrap();

    let mut received: Vec<serde_json::Value> = Vec::new();
    for _ in 0..POLL_ATTEMPTS {
        if let Ok(polled) = client
            .poll_messages(
                &stream_id,
                &topic_id,
                None,
                &Consumer::new(consumer_id.clone()),
                &PollingStrategy::next(),
                10,
                true,
            )
            .await
        {
            for msg in polled.messages {
                if let Ok(json) = serde_json::from_slice(&msg.payload) {
                    received.push(json);
                }
            }
            if received.len() >= TEST_MESSAGE_COUNT {
                break;
            }
        }
        sleep(Duration::from_millis(POLL_INTERVAL_MS)).await;
    }

    assert!(
        received.len() >= TEST_MESSAGE_COUNT,
        "Expected at least {TEST_MESSAGE_COUNT} messages from source, got {}",
        received.len()
    );

    // Verify documents arrive in seq order.
    for (i, doc) in received.iter().enumerate() {
        let seq = doc["seq"].as_i64().expect("seq field missing");
        assert_eq!(seq, (i + 1) as i64, "Seq mismatch at position {i}");
    }
}
```

**Test 2: delete_after_read_removes_documents**

```rust
#[iggy_harness(
    server(connectors_runtime(config_path = "tests/connectors/mongodb/source.toml")),
    seed = seeds::connector_stream
)]
async fn delete_after_read_removes_documents(
    harness: &TestHarness,
    fixture: MongoDbSourceDeleteFixture,
) {
    let client = harness.root_client().await.unwrap();
    let mongo_client = fixture.create_client().await.expect("Failed to create MongoDB client");

    let docs: Vec<_> = (1..=TEST_MESSAGE_COUNT)
        .map(|i| mongodb::bson::doc! { "seq": i as i64, "name": format!("event_{i}") })
        .collect();
    fixture.seed_documents(&mongo_client, docs).await.expect("Failed to seed");

    let initial_count = fixture.count_documents(&mongo_client).await.expect("count failed");
    assert_eq!(initial_count, TEST_MESSAGE_COUNT as u64);

    let stream_id: Identifier = seeds::names::STREAM.try_into().unwrap();
    let topic_id: Identifier = seeds::names::TOPIC.try_into().unwrap();
    let consumer_id: Identifier = "test_consumer".try_into().unwrap();

    // Wait for messages to appear in iggy stream.
    let mut received_count = 0usize;
    for _ in 0..POLL_ATTEMPTS {
        if let Ok(polled) = client
            .poll_messages(
                &stream_id,
                &topic_id,
                None,
                &Consumer::new(consumer_id.clone()),
                &PollingStrategy::next(),
                10,
                true,
            )
            .await
        {
            received_count += polled.messages.len();
            if received_count >= TEST_MESSAGE_COUNT {
                break;
            }
        }
        sleep(Duration::from_millis(POLL_INTERVAL_MS)).await;
    }

    assert!(received_count >= TEST_MESSAGE_COUNT, "Messages not received from source");

    // Wait for delete_after_read to complete.
    let mut final_count = initial_count;
    for _ in 0..POLL_ATTEMPTS {
        final_count = fixture.count_documents(&mongo_client).await.unwrap_or(initial_count);
        if final_count == 0 {
            break;
        }
        sleep(Duration::from_millis(POLL_INTERVAL_MS)).await;
    }

    assert_eq!(
        final_count, 0,
        "Expected 0 documents after delete_after_read, got {final_count}"
    );

    mongo_client.shutdown().await;
}
```

**Test 3: mark_processed_sets_field**

```rust
#[iggy_harness(
    server(connectors_runtime(config_path = "tests/connectors/mongodb/source.toml")),
    seed = seeds::connector_stream
)]
async fn mark_processed_sets_field(harness: &TestHarness, fixture: MongoDbSourceMarkFixture) {
    let client = harness.root_client().await.unwrap();
    let mongo_client = fixture.create_client().await.expect("Failed to create MongoDB client");

    let docs: Vec<_> = (1..=TEST_MESSAGE_COUNT)
        .map(|i| mongodb::bson::doc! {
            "seq": i as i64,
            "name": format!("event_{i}"),
            "is_processed": false,
        })
        .collect();
    fixture.seed_documents(&mongo_client, docs).await.expect("Failed to seed");

    let stream_id: Identifier = seeds::names::STREAM.try_into().unwrap();
    let topic_id: Identifier = seeds::names::TOPIC.try_into().unwrap();
    let consumer_id: Identifier = "test_consumer".try_into().unwrap();

    let mut received_count = 0usize;
    for _ in 0..POLL_ATTEMPTS {
        if let Ok(polled) = client
            .poll_messages(
                &stream_id,
                &topic_id,
                None,
                &Consumer::new(consumer_id.clone()),
                &PollingStrategy::next(),
                10,
                true,
            )
            .await
        {
            received_count += polled.messages.len();
            if received_count >= TEST_MESSAGE_COUNT {
                break;
            }
        }
        sleep(Duration::from_millis(POLL_INTERVAL_MS)).await;
    }

    assert!(received_count >= TEST_MESSAGE_COUNT);

    // Wait for is_processed to flip on all documents.
    let mut processed = 0u64;
    for _ in 0..POLL_ATTEMPTS {
        processed = fixture
            .count_processed_documents(&mongo_client)
            .await
            .unwrap_or(0);
        if processed >= TEST_MESSAGE_COUNT as u64 {
            break;
        }
        sleep(Duration::from_millis(POLL_INTERVAL_MS)).await;
    }

    assert_eq!(
        processed, TEST_MESSAGE_COUNT as u64,
        "Expected {TEST_MESSAGE_COUNT} processed documents, got {processed}"
    );

    // Total document count unchanged -- no deletes.
    let total = fixture.count_documents(&mongo_client).await.expect("count failed");
    assert_eq!(
        total, TEST_MESSAGE_COUNT as u64,
        "Documents should not be deleted when using mark-processed"
    );

    mongo_client.shutdown().await;
}
```

**Test 4: state_persists_across_connector_restart**

Note: harness parameter is `&mut TestHarness` (mutable), not `&TestHarness`. This is the same as postgres.

```rust
#[iggy_harness(
    server(connectors_runtime(config_path = "tests/connectors/mongodb/source.toml")),
    seed = seeds::connector_stream
)]
async fn state_persists_across_connector_restart(
    harness: &mut TestHarness,
    fixture: MongoDbSourceFixture,
) {
    let mongo_client = fixture.create_client().await.expect("Failed to create MongoDB client");

    // Seed first batch.
    let first_batch: Vec<_> = (1..=TEST_MESSAGE_COUNT)
        .map(|i| mongodb::bson::doc! { "seq": i as i64, "name": format!("batch1_{i}") })
        .collect();
    fixture.seed_documents(&mongo_client, first_batch).await.expect("Failed to seed");

    let stream_id: Identifier = seeds::names::STREAM.try_into().unwrap();
    let topic_id: Identifier = seeds::names::TOPIC.try_into().unwrap();
    let consumer_id: Identifier = "restart_test_consumer".try_into().unwrap();

    let client = harness.root_client().await.unwrap();

    // Consume first batch.
    let mut received_before = 0usize;
    for _ in 0..POLL_ATTEMPTS {
        if let Ok(polled) = client
            .poll_messages(
                &stream_id,
                &topic_id,
                None,
                &Consumer::new(consumer_id.clone()),
                &PollingStrategy::next(),
                10,
                true,
            )
            .await
        {
            received_before += polled.messages.len();
            if received_before >= TEST_MESSAGE_COUNT {
                break;
            }
        }
        sleep(Duration::from_millis(POLL_INTERVAL_MS)).await;
    }
    assert_eq!(received_before, TEST_MESSAGE_COUNT, "First batch not fully consumed");

    // Stop connectors runtime.
    harness
        .server_mut()
        .stop_dependents()
        .expect("Failed to stop connectors");

    // Seed second batch while stopped.
    let second_batch_start = TEST_MESSAGE_COUNT + 1;
    let second_batch: Vec<_> = (second_batch_start..=(second_batch_start + TEST_MESSAGE_COUNT - 1))
        .map(|i| mongodb::bson::doc! { "seq": i as i64, "name": format!("batch2_{i}") })
        .collect();
    fixture.seed_documents(&mongo_client, second_batch).await.expect("Failed to seed batch 2");

    // Restart connectors.
    harness
        .server_mut()
        .start_dependents()
        .await
        .expect("Failed to restart connectors");
    sleep(Duration::from_secs(2)).await;

    // Consume after restart. Expect only second batch (no duplicates).
    let mut received_after: Vec<serde_json::Value> = Vec::new();
    for _ in 0..POLL_ATTEMPTS {
        if let Ok(polled) = client
            .poll_messages(
                &stream_id,
                &topic_id,
                None,
                &Consumer::new(consumer_id.clone()),
                &PollingStrategy::next(),
                10,
                true,
            )
            .await
        {
            for msg in polled.messages {
                if let Ok(json) = serde_json::from_slice(&msg.payload) {
                    received_after.push(json);
                }
            }
            if received_after.len() >= TEST_MESSAGE_COUNT {
                break;
            }
        }
        sleep(Duration::from_millis(POLL_INTERVAL_MS)).await;
    }

    assert_eq!(
        received_after.len(),
        TEST_MESSAGE_COUNT,
        "Second batch count mismatch"
    );

    // All messages from second poll must have seq > TEST_MESSAGE_COUNT.
    for msg in &received_after {
        let seq = msg["seq"].as_i64().expect("seq field missing");
        assert!(
            seq > TEST_MESSAGE_COUNT as i64,
            "Got seq={seq} from first batch after restart -- duplicate detected"
        );
    }

    mongo_client.shutdown().await;
}
```

---

## Modifications to Existing Files

### fixtures/mod.rs -- add MongoDB

```rust
// Add to existing file:
mod mongodb;

pub use mongodb::{
    MongoDbOps, MongoDbSinkAutoCreateFixture, MongoDbSinkFixture, MongoDbSinkJsonFixture,
    MongoDbSourceDeleteFixture, MongoDbSourceFixture, MongoDbSourceMarkFixture,
};
```

### connectors/mod.rs -- add MongoDB test module

```rust
// Add to existing file (after existing mod lines):
mod mongodb;
```

---

## Integration Test Dependencies

The integration test crate (`core/integration/Cargo.toml`) needs `mongodb` as a dev-dependency if not already present, because the fixture queries MongoDB directly. Check with:
```bash
grep -n "mongodb" core/integration/Cargo.toml
```

If missing, add:
```toml
[dev-dependencies]
mongodb = { version = "3.0", features = ["rustls-tls"] }
futures = { workspace = true }
```

The `futures` crate is needed for `TryStreamExt` in the `wait_for_documents` helper.

---

## Polling Behavior: The poll_interval Problem

The source connector's `poll()` method sleeps for `poll_interval` **before** doing any work:

```rust
async fn poll(&self) -> Result<ProducedMessages, Error> {
    let poll_interval = self.poll_interval;
    tokio::time::sleep(poll_interval).await;   // sleeps FIRST
    let messages = self.poll_collection().await?;
    ...
}
```

This means documents seeded before the connector starts will be read on the first poll, but only after the poll_interval delay. For tests, set `poll_interval = "10ms"` (via `ENV_SOURCE_POLL_INTERVAL`) to minimize wait time. The test polls iggy 100 times with 50ms sleep between attempts, giving 5 seconds total -- more than enough for a 10ms poll interval.

For the restart test, `sleep(Duration::from_secs(2))` after `start_dependents()` accounts for the poll_interval plus connector startup time.

---

## What Was Dropped from the Original Document

| Original item | Why dropped |
|---|---|
| Round-trip test `round_trip_source_to_sink` | Stretch goal. Not needed for v1. |
| `offset_tracking_across_polls` | Requires two poll cycles without ability to pause connector. Implicit in restart test. |
| `payload_format_json_emits_schema_json` | Unit test concern. Already covered by unit tests in `lib.rs`. |
| `metadata_fields_included` as separate test | Merged into `json_messages_sink_to_mongodb`. |
| `source_handles_empty_collection` | The connector warns but does not error. There is no observable behavior to assert on (no messages appear, which is indistinguishable from "connector hasn't polled yet"). |
| `Mongo::repl_set()` recommendation | Replica set only needed for CDC/Change Streams. Out of scope for v1. |
| "Add `mongo` feature to testcontainers-modules" | Not needed -- using GenericImage. |

---

## Async Patterns Verified Against Actual Code

The original document had speculative async helpers. Correct patterns from actual iggy test code:

**For sink tests (wait for MongoDB document)**: Poll MongoDB directly using the mongodb crate in a `for _ in 0..POLL_ATTEMPTS` loop with `sleep(Duration::from_millis(POLL_INTERVAL_MS)).await` between attempts.

**For source tests (wait for iggy messages)**: `client.poll_messages(..., &PollingStrategy::next(), 10, true)` in a loop, accumulating messages until `received.len() >= expected`.

**No deadline/Instant-based polling**: The actual iggy test code uses simple count-based loops, not deadline-based loops. The original document's `Instant::now() + timeout` suggestion was correct in spirit but not matching the actual code style.

**No exponential backoff**: The actual iggy test code uses fixed 50ms intervals. The exponential backoff pattern from mongo-kafka was industry research, not the iggy convention.

---

## Summary Checklist for Implementer

Before calling the implementation done:

- [ ] `fixtures/mongodb/container.rs` -- MongoDbContainer using GenericImage, all env var constants defined
- [ ] `fixtures/mongodb/sink.rs` -- MongoDbSinkFixture, MongoDbSinkJsonFixture, MongoDbSinkAutoCreateFixture
- [ ] `fixtures/mongodb/source.rs` -- MongoDbSourceFixture, MongoDbSourceDeleteFixture, MongoDbSourceMarkFixture
- [ ] `fixtures/mongodb/mod.rs` -- re-exports
- [ ] `fixtures/mod.rs` -- add `mod mongodb` and re-exports
- [ ] `mongodb/mod.rs` -- TEST_MESSAGE_COUNT=3, POLL_ATTEMPTS=100, POLL_INTERVAL_MS=50
- [ ] `mongodb/sink.toml` and `mongodb/source.toml` with correct config_dir paths
- [ ] `mongodb/mongodb_sink.rs` -- 4 sink tests
- [ ] `mongodb/mongodb_source.rs` -- 4 source tests
- [ ] `connectors/mod.rs` -- add `mod mongodb`
- [ ] Check `core/integration/Cargo.toml` for `mongodb` dev-dependency
- [ ] Verify connector binary path: `libiggy_connector_mongodb_sink` and `libiggy_connector_mongodb_source` (no extension; runtime appends `.so` or `.dylib`)
- [ ] Both MongoDB crates must be built before running tests: `cargo build -p iggy_connector_mongodb_sink -p iggy_connector_mongodb_source`
- [ ] `ENV_SINK_STREAMS_0_TOPICS` is plural (array syntax `[topic_name]`); `ENV_SOURCE_STREAMS_0_TOPIC` is singular -- get this right or messages will not route
