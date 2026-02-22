# TDD Session State: MongoDB E2E Integration Tests

**Date/Time**: 2026-02-22
**Branch**: ab_202602_issue02
**Session Agent**: TDD Context Retention Specialist (tracking only — implementation by rust-coder-01)

---

## Current Phase: GREEN (compilation) -- E2E execution BLOCKED (no Docker)

**Updated**: 2026-02-22 (correction from prior RED state)

All 15 work items were implemented by rust-coder-01. All 9 new files exist on disk.
Both existing-file modifications (fixtures/mod.rs, connectors/mod.rs) were applied.

E2E tests COMPILE cleanly (`cargo test --test mod --no-run` exits 0). They have NOT
been executed against a real MongoDB instance. Docker is not installed on this machine.
testcontainers requires a live Docker daemon to spin up containers.

To advance to TRUE GREEN, install Docker and run:
```
cargo test --test mod -- mongodb
```

**Honest status summary**:
- 52 unit tests: PASSING (verified with `cargo test -p`)
- 8 E2E tests: COMPILE-VERIFIED ONLY (never executed against real MongoDB)

---

## Work Item Registry

All 15 tracked work items follow. Each item has an ID, a status, the exact file path, and precise success criteria so that the implementing agent can self-verify without re-reading the spec.

---

### WI-01: fixtures/mongodb/container.rs

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/fixtures/mongodb/container.rs`

**What must be in this file:**
- `GenericImage::new("mongo", "7")` with `WaitFor::message_on_stdout("Waiting for connections")`
- Random port mapping via `.with_mapped_port(0, MONGODB_PORT.tcp())`
- `MongoDbContainer` struct with private `container: ContainerAsync<GenericImage>` and public `connection_uri: String`
- `MongoDbContainer::start()` async method returning `Result<Self, TestBinaryError>`
- `MongoDbContainer::create_client()` async method returning `Result<mongodb::Client, TestBinaryError>`
- `MongoDbOps` trait with `container(&self) -> &MongoDbContainer` and a delegating `create_client()` default impl
- All 28 env var constants at `pub(super)` visibility (14 sink, 14 source)
- All helper constants at `pub(super)` visibility:
  - `DEFAULT_TEST_STREAM = "test_stream"`
  - `DEFAULT_TEST_TOPIC = "test_topic"`
  - `DEFAULT_SINK_COLLECTION = "iggy_messages"`
  - `DEFAULT_TEST_DATABASE = "iggy_test"`
  - `HEALTH_CHECK_ATTEMPTS = 30`
  - `HEALTH_CHECK_INTERVAL_MS = 500`
  - `DEFAULT_POLL_ATTEMPTS = 100`
  - `DEFAULT_POLL_INTERVAL_MS = 50`
- Connection URI format: `mongodb://localhost:{mapped_port}` (no `?directConnection=true` — standalone only)
- Apache 2.0 license header

**Critical env var correctness (sink uses TOPICS plural, source uses TOPIC singular):**
```
ENV_SINK_STREAMS_0_TOPICS  = "IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_TOPICS"
ENV_SOURCE_STREAMS_0_TOPIC = "IGGY_CONNECTORS_SOURCE_MONGODB_STREAMS_0_TOPIC"
```

**No testcontainers-modules mongo feature needed.** GenericImage uses only the base `testcontainers` transitive dependency.

---

### WI-02: fixtures/mongodb/sink.rs

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/fixtures/mongodb/sink.rs`

**What must be in this file:**

Three fixture structs, each implementing `TestFixture`:

1. `MongoDbSinkFixture` (base — binary payload, no auto_create)
   - Fields: `container: MongoDbContainer`, `payload_format: &'static str`, `auto_create: bool`
   - Implements `MongoDbOps`
   - Methods:
     - `wait_for_documents(client, collection_name, expected) -> Result<Vec<Document>, TestBinaryError>` — polls MongoDB in a `DEFAULT_POLL_ATTEMPTS` loop with `DEFAULT_POLL_INTERVAL_MS` sleep, sorts by `iggy_offset` ascending, returns when `docs.len() >= expected`
     - `count_documents_in_collection(client, collection_name) -> Result<u64, TestBinaryError>`
     - `collection_exists(client, collection_name) -> Result<bool, TestBinaryError>` — calls `db.list_collection_names()`
   - `setup()`: creates container, `payload_format = "binary"`, `auto_create = false`
   - `connectors_runtime_envs()`: inserts 11 env vars (URI, database, collection, payload_format, include_metadata=true, stream, topics (plural `[test_topic]`), schema, consumer_group, path)
   - PATH value: `"../../target/debug/libiggy_connector_mongodb_sink"` (no extension)
   - `ENV_SINK_AUTO_CREATE_COLLECTION` inserted only when `self.auto_create == true`

2. `MongoDbSinkJsonFixture`
   - Contains `inner: MongoDbSinkFixture` and uses `Deref<Target = MongoDbSinkFixture>`
   - `setup()`: creates container, `payload_format = "json"`, `auto_create = false`
   - `connectors_runtime_envs()`: delegates to `inner.connectors_runtime_envs()` then overrides `ENV_SINK_STREAMS_0_SCHEMA` to `"json"`

3. `MongoDbSinkAutoCreateFixture`
   - Contains `inner: MongoDbSinkFixture` and uses `Deref<Target = MongoDbSinkFixture>`
   - `setup()`: creates container, `payload_format = "binary"`, `auto_create = true`
   - `connectors_runtime_envs()`: delegates to `inner.connectors_runtime_envs()` (auto_create flag already handled by base)

**Imports needed**: `futures::TryStreamExt` for `c.try_collect::<Vec<_>>()` in `wait_for_documents`

---

### WI-03: fixtures/mongodb/source.rs

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/fixtures/mongodb/source.rs`

**What must be in this file:**

Three fixture structs, each implementing `TestFixture`:

1. `MongoDbSourceFixture` (base — json payload, no delete, no mark)
   - Fields: `container: MongoDbContainer`
   - Module-private constant: `SOURCE_COLLECTION = "test_events"`
   - Implements `MongoDbOps`
   - Methods:
     - `collection_name() -> &str` — returns `SOURCE_COLLECTION`
     - `seed_documents(client, docs: Vec<Document>) -> Result<(), TestBinaryError>` — `collection.insert_many(docs).await`
     - `count_documents(client) -> Result<u64, TestBinaryError>` — `count_documents(doc! {}).await`
     - `count_processed_documents(client) -> Result<u64, TestBinaryError>` — `count_documents(doc! { "is_processed": true }).await`
   - `setup()`: creates container
   - `connectors_runtime_envs()`: inserts 10 env vars (URI, database, collection=test_events, poll_interval="10ms", tracking_field="seq", payload_format="json", stream, topic (singular), schema, path)
   - PATH value: `"../../target/debug/libiggy_connector_mongodb_source"` (no extension)

2. `MongoDbSourceDeleteFixture`
   - Contains `inner: MongoDbSourceFixture`, uses `Deref<Target = MongoDbSourceFixture>`
   - `connectors_runtime_envs()`: delegates to inner then adds `ENV_SOURCE_DELETE_AFTER_READ = "true"`

3. `MongoDbSourceMarkFixture`
   - Contains `inner: MongoDbSourceFixture`, uses `Deref<Target = MongoDbSourceFixture>`
   - `connectors_runtime_envs()`: delegates to inner then adds `ENV_SOURCE_PROCESSED_FIELD = "is_processed"`

**Tracking field note**: All source fixtures use `seq` (integer) as the tracking field. Seeded documents MUST have `seq` field with values `1, 2, 3, ...`.

---

### WI-04: fixtures/mongodb/mod.rs

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/fixtures/mongodb/mod.rs`

**Exact content required:**
```rust
mod container;
mod sink;
mod source;

pub use container::MongoDbOps;
pub use sink::{MongoDbSinkAutoCreateFixture, MongoDbSinkFixture, MongoDbSinkJsonFixture};
pub use source::{MongoDbSourceDeleteFixture, MongoDbSourceFixture, MongoDbSourceMarkFixture};
```

Apache license header must be present.

---

### WI-05: fixtures/mod.rs (MODIFY existing file)

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/fixtures/mod.rs`

**Current content** (lines 20-34 relevant section):
```rust
mod elasticsearch;
mod iceberg;
mod postgres;
mod quickwit;
mod wiremock;

pub use elasticsearch::{ElasticsearchSinkFixture, ElasticsearchSourcePreCreatedFixture};
pub use iceberg::{DEFAULT_NAMESPACE, DEFAULT_TABLE, IcebergOps, IcebergPreCreatedFixture};
pub use postgres::{...};
pub use quickwit::{...};
pub use wiremock::{...};
```

**What to add** (insert after existing mod declarations, before existing pub use lines or alongside them):
```rust
mod mongodb;

pub use mongodb::{
    MongoDbOps, MongoDbSinkAutoCreateFixture, MongoDbSinkFixture, MongoDbSinkJsonFixture,
    MongoDbSourceDeleteFixture, MongoDbSourceFixture, MongoDbSourceMarkFixture,
};
```

**Constraint**: Do NOT remove or alter any existing content. Only add the new `mod mongodb;` and `pub use` block.

---

### WI-06: mongodb/mod.rs (test module)

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/mongodb/mod.rs`

**Exact content required:**
```rust
mod mongodb_sink;
mod mongodb_source;

const TEST_MESSAGE_COUNT: usize = 3;
const POLL_ATTEMPTS: usize = 100;
const POLL_INTERVAL_MS: u64 = 50;
```

These constants match the postgres and elasticsearch patterns exactly (`TEST_MESSAGE_COUNT=3`, `POLL_ATTEMPTS=100`, `POLL_INTERVAL_MS=50`). Apache license header must be present.

---

### WI-07: mongodb/mongodb_sink.rs

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/mongodb/mongodb_sink.rs`

**4 tests required:**

**Test 1: `json_messages_sink_to_mongodb`**
- Fixture: `MongoDbSinkJsonFixture`
- Harness: `&TestHarness` (immutable)
- Config path: `"tests/connectors/mongodb/sink.toml"`
- Actions: Send 3 JSON messages via `client.send_messages()`, call `fixture.wait_for_documents()`, assert count == 3
- Assertions:
  - `docs[0]` contains all 5 metadata keys: `iggy_offset`, `iggy_stream`, `iggy_topic`, `iggy_partition_id`, `iggy_timestamp`
  - Offsets are contiguous 0, 1, 2 (sorted by `iggy_offset` ascending — `wait_for_documents` sorts this)
  - `docs[0].get("payload")` is `Bson::Document(_)` (not Binary — json format stores as BSON Document)

**Test 2: `binary_messages_sink_as_bson_binary`**
- Fixture: `MongoDbSinkFixture` (base — binary format)
- Harness: `&TestHarness` (immutable)
- Config path: `"tests/connectors/mongodb/sink.toml"`
- Actions: Send 3 raw byte payloads, call `fixture.wait_for_documents()`
- Assertions:
  - Each doc's `payload` field is `Bson::Binary(bin)` with `bin.subtype == BinarySubtype::Generic`
  - `bin.bytes == raw_payloads[i]` (byte-for-byte match)

**Test 3: `large_batch_processed_correctly`**
- Fixture: `MongoDbSinkFixture` (base) OR a new `MongoDbSinkBatchFixture` that adds `ENV_SINK_BATCH_SIZE = "10"`
- Harness: `&TestHarness` (immutable)
- Config path: `"tests/connectors/mongodb/sink.toml"`
- Actions: Send 50 messages (JSON `{"idx": i}`), call `fixture.wait_for_documents(..., 50)`
- Assertions:
  - `docs.len() >= 50`
  - All 50 offsets 0..49 are contiguous (no gaps)
- **Implementation decision needed**: The spec mentions either creating a `MongoDbSinkBatchFixture` or overriding via harness env injection. The simpler approach per the spec is a dedicated fixture variant that sets `ENV_SINK_BATCH_SIZE = "10"`. The rust-coder-01 agent must choose and document which approach was used.

**Test 4: `auto_create_collection_on_open`**
- Fixture: `MongoDbSinkAutoCreateFixture`
- Harness: `&TestHarness` (immutable, add `let _ = harness;` to suppress unused warning)
- Config path: `"tests/connectors/mongodb/sink.toml"`
- Actions: No messages sent. Poll `fixture.collection_exists()` in a `DEFAULT_POLL_ATTEMPTS` loop
- Assertions:
  - Collection `DEFAULT_SINK_COLLECTION` exists before any messages sent
  - `count_documents_in_collection()` returns 0 (empty collection)

**Imports for all sink tests:**
```rust
use super::{POLL_ATTEMPTS, POLL_INTERVAL_MS, TEST_MESSAGE_COUNT};
use crate::connectors::fixtures::{MongoDbSinkAutoCreateFixture, MongoDbSinkFixture, MongoDbSinkJsonFixture};
use crate::connectors::fixtures::container::{DEFAULT_POLL_ATTEMPTS, DEFAULT_POLL_INTERVAL_MS, DEFAULT_SINK_COLLECTION};
use bytes::Bytes;
use iggy::clients::client::IggyClient;
use iggy::identifier::Identifier;
use iggy::messages::send_messages::Partitioning;
use iggy::models::messages::IggyMessage;
use integration::harness::{seeds, TestHarness};
use std::time::Duration;
use tokio::time::sleep;
```

---

### WI-08: mongodb/mongodb_source.rs

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/mongodb/mongodb_source.rs`

**4 tests required:**

**Test 1: `source_polls_documents_to_iggy`**
- Fixture: `MongoDbSourceFixture`
- Harness: `&TestHarness` (immutable)
- Config path: `"tests/connectors/mongodb/source.toml"`
- Actions:
  1. Seed 3 documents with `seq: 1, 2, 3` and `name: "event_1", "event_2", "event_3"`
  2. Shut down the seeding `mongo_client` with `.shutdown().await`
  3. Poll iggy for `TEST_MESSAGE_COUNT` messages (100 attempts, 50ms sleep)
- Assertions:
  - `received.len() >= TEST_MESSAGE_COUNT`
  - Documents arrive in seq order: `received[i]["seq"].as_i64() == (i+1) as i64`

**Test 2: `delete_after_read_removes_documents`**
- Fixture: `MongoDbSourceDeleteFixture`
- Harness: `&TestHarness` (immutable)
- Actions:
  1. Seed 3 documents
  2. Verify `initial_count == 3`
  3. Poll iggy until `received_count >= TEST_MESSAGE_COUNT`
  4. Poll `fixture.count_documents()` until it returns 0 (separate POLL_ATTEMPTS loop)
- Assertions:
  - Messages received from iggy: `received_count >= TEST_MESSAGE_COUNT`
  - MongoDB document count after poll: `final_count == 0`

**Test 3: `mark_processed_sets_field`**
- Fixture: `MongoDbSourceMarkFixture`
- Harness: `&TestHarness` (immutable)
- Actions:
  1. Seed 3 documents with `is_processed: false`
  2. Poll iggy until `received_count >= TEST_MESSAGE_COUNT`
  3. Poll `fixture.count_processed_documents()` until it returns `TEST_MESSAGE_COUNT as u64`
- Assertions:
  - `processed == TEST_MESSAGE_COUNT as u64` (all docs marked)
  - `total == TEST_MESSAGE_COUNT as u64` (no docs deleted)

**Test 4: `state_persists_across_connector_restart`**
- Fixture: `MongoDbSourceFixture`
- Harness: **`&mut TestHarness` (MUTABLE)** — this is a critical difference from the other 7 tests
- Actions:
  1. Seed first batch: `seq 1, 2, 3` (names: `batch1_1`, `batch1_2`, `batch1_3`)
  2. Poll iggy with consumer `"restart_test_consumer"` until `received_before == TEST_MESSAGE_COUNT`
  3. Call `harness.server_mut().stop_dependents()` — stops connector runtime
  4. Seed second batch: `seq 4, 5, 6` (names: `batch2_4`, `batch2_5`, `batch2_6`)
  5. Call `harness.server_mut().start_dependents().await` — restarts connector runtime
  6. `sleep(Duration::from_secs(2)).await` — allow startup + first poll
  7. Poll iggy with same consumer `"restart_test_consumer"` (PollingStrategy::next() picks up from last offset)
- Assertions:
  - First batch: `received_before == TEST_MESSAGE_COUNT` (exactly 3)
  - Second batch: `received_after.len() == TEST_MESSAGE_COUNT` (exactly 3)
  - No duplicates: all messages in `received_after` have `seq > TEST_MESSAGE_COUNT as i64`

**Imports for all source tests:**
```rust
use super::{POLL_ATTEMPTS, POLL_INTERVAL_MS, TEST_MESSAGE_COUNT};
use crate::connectors::fixtures::{MongoDbSourceDeleteFixture, MongoDbSourceFixture, MongoDbSourceMarkFixture};
use iggy::clients::client::IggyClient;
use iggy::consumer::Consumer;
use iggy::identifier::Identifier;
use iggy::messages::poll_messages::PollingStrategy;
use integration::harness::{seeds, TestHarness};
use std::time::Duration;
use tokio::time::sleep;
```

---

### WI-09: mongodb/sink.toml

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/mongodb/sink.toml`

**Exact content:**
```toml
# Apache License 2.0 header (same as postgres/sink.toml)

[connectors]
config_type = "local"
config_dir = "../connectors/sinks/mongodb_sink"
```

**Verification**: The path `../connectors/sinks/mongodb_sink` must resolve to `core/connectors/sinks/mongodb_sink` relative to the integration test working directory. The mongodb_sink `config.toml` exists at `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/connectors/sinks/mongodb_sink/config.toml`.

---

### WI-10: mongodb/source.toml

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/mongodb/source.toml`

**Exact content:**
```toml
# Apache License 2.0 header

[connectors]
config_type = "local"
config_dir = "../connectors/sources/mongodb_source"
```

**Verification**: The path resolves to `core/connectors/sources/mongodb_source` which contains the source connector's `config.toml` at `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/connectors/sources/mongodb_source/config.toml`.

---

### WI-11: connectors/mod.rs (MODIFY existing file)

**Status**: NOT STARTED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/mod.rs`

**Current mod declarations (lines 20-28):**
```rust
mod api;
mod elasticsearch;
mod fixtures;
mod http_config_provider;
mod iceberg;
mod postgres;
mod quickwit;
mod random;
mod stdout;
```

**What to add**: Insert `mod mongodb;` into the sorted list (alphabetically between `mod iceberg;` and `mod postgres;`):
```rust
mod mongodb;
```

**Constraint**: Do NOT remove or alter any existing content. Only add the single new line.

---

### WI-12: Cargo.toml dependency check — mongodb

**Status**: NEEDS ACTION

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/Cargo.toml`

**Current state**: `mongodb` is NOT present in this file (confirmed by grep returning "NOT FOUND").

**Action required**: Add to the `[dependencies]` section (the file has no `[dev-dependencies]` section, only `[dependencies]`):
```toml
mongodb = { version = "3.0", features = ["rustls-tls"] }
```

**Note**: Both connector crates (`iggy_connector_mongodb_sink`, `iggy_connector_mongodb_source`) already use `mongodb = { version = "3.0", features = ["rustls-tls"] }`. The workspace `Cargo.toml` does NOT have a workspace-level `mongodb` entry (it is declared inline in each connector's `Cargo.toml`). Therefore the integration crate must also declare it inline the same way.

**Risk**: If the version pin differs from what the connector crates use, Cargo will deduplicate but it must be compatible. Both connectors use `"3.0"` — use the same version.

---

### WI-13: Cargo.toml dependency check — futures

**Status**: ALREADY PRESENT — NO ACTION NEEDED

**File**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/Cargo.toml`

`futures = { workspace = true }` is already at line 40. The `TryStreamExt` trait used in `wait_for_documents` is covered.

---

### WI-14: Build verification — connector crates

**Status**: NOT STARTED (blocker for all tests)

**Command:**
```bash
cargo build -p iggy_connector_mongodb_sink -p iggy_connector_mongodb_source
```

**Run from**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02`

**Success criterion**: Exit code 0, artifacts exist at:
- `target/debug/libiggy_connector_mongodb_sink.so` (Linux) or `.dylib` (macOS)
- `target/debug/libiggy_connector_mongodb_source.so` (Linux) or `.dylib` (macOS)

**Must be done before running tests**, because the fixture env var `PATH` points to these compiled artifacts.

---

### WI-15: Integration test compilation check

**Status**: NOT STARTED (blocker for test execution)

**Command:**
```bash
cargo test --test connectors --no-run
```

**Run from**: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02`

**Success criterion**: Exit code 0. The `--no-run` flag compiles without executing, which will catch:
- Missing imports
- Type mismatches in fixture implementations
- Missing `mod mongodb;` declarations
- Incorrect `mongodb` dependency (if WI-12 was not applied)

**This is the key "compilation green" gate** before attempting actual test runs.

---

## Tests Written

All 8 tests implemented and COMPILE CLEAN. Execution status: BLOCKED (no Docker).

| Test Name | File | Status | Fixture Used |
|---|---|---|---|
| `json_messages_sink_to_mongodb` | `mongodb/mongodb_sink.rs` | COMPILE-VERIFIED | `MongoDbSinkJsonFixture` |
| `binary_messages_sink_as_bson_binary` | `mongodb/mongodb_sink.rs` | COMPILE-VERIFIED | `MongoDbSinkFixture` |
| `large_batch_processed_correctly` | `mongodb/mongodb_sink.rs` | COMPILE-VERIFIED | `MongoDbSinkFixture` or batch variant |
| `auto_create_collection_on_open` | `mongodb/mongodb_sink.rs` | COMPILE-VERIFIED | `MongoDbSinkAutoCreateFixture` |
| `source_polls_documents_to_iggy` | `mongodb/mongodb_source.rs` | COMPILE-VERIFIED | `MongoDbSourceFixture` |
| `delete_after_read_removes_documents` | `mongodb/mongodb_source.rs` | COMPILE-VERIFIED | `MongoDbSourceDeleteFixture` |
| `mark_processed_sets_field` | `mongodb/mongodb_source.rs` | COMPILE-VERIFIED | `MongoDbSourceMarkFixture` |
| `state_persists_across_connector_restart` | `mongodb/mongodb_source.rs` | COMPILE-VERIFIED | `MongoDbSourceFixture` |

**To advance all 8 from COMPILE-VERIFIED to PASSING**: install Docker and run
`cargo test --test mod -- mongodb`.

---

## Implementation Progress

**Updated 2026-02-22**: All work items completed by rust-coder-01. Files verified to exist on disk.

| Work Item | Status | Notes |
|---|---|---|
| WI-01 container.rs | COMPLETE | File exists, GenericImage("mongo", "7") pattern |
| WI-02 sink.rs | COMPLETE | File exists, 3 fixture structs |
| WI-03 source.rs | COMPLETE | File exists, 3 fixture structs |
| WI-04 fixtures/mongodb/mod.rs | COMPLETE | File exists with re-exports |
| WI-05 fixtures/mod.rs (modify) | COMPLETE | mod mongodb; and pub use added |
| WI-06 mongodb/mod.rs | COMPLETE | File exists |
| WI-07 mongodb_sink.rs | COMPLETE | File exists, 4 tests |
| WI-08 mongodb_source.rs | COMPLETE | File exists, 4 tests |
| WI-09 sink.toml | COMPLETE | File exists |
| WI-10 source.toml | COMPLETE | File exists |
| WI-11 connectors/mod.rs (modify) | COMPLETE | mod mongodb; added |
| WI-12 Cargo.toml mongodb dep | COMPLETE | mongodb dep added to integration Cargo.toml |
| WI-13 Cargo.toml futures dep | COMPLETE | Already present at line 40 |
| WI-14 Build verification | COMPILE-VERIFIED | cargo test --test mod --no-run exits 0 |
| WI-15 Compilation check | COMPILE-VERIFIED | cargo test --test mod --no-run exits 0; execution requires Docker |

---

## Current Focus

**Updated 2026-02-22**: All implementation work is complete. All 15 work items are COMPLETE
or COMPILE-VERIFIED. The single remaining blocker is Docker installation for E2E execution.

Implementation order is no longer relevant. Focus is now on E2E execution unblocking.

---

## Next Steps

**Updated 2026-02-22**: Implementation complete. Steps to advance to TRUE GREEN:

1. Install Docker Desktop for macOS (https://www.docker.com/products/docker-desktop/)
2. Build connector artifacts: `cargo build -p iggy_connector_mongodb_sink -p iggy_connector_mongodb_source`
3. Execute E2E tests: `cargo test --test mod -- mongodb --nocapture`
4. Fix any failures and re-run
5. Only after all 8 tests pass: update PR description to remove "compile-verified" qualifier

---

## Context Notes

### Key Decisions (from spec post-rubberduck review)

**Decision 1: GenericImage over testcontainers-modules mongo feature**
- Rationale: MongoDB source uses `find()` polling, not Change Streams. Standalone mode is correct. Replica set is only required for Change Streams / CDC which is out of scope for v1.
- Impact: No `"mongo"` feature needed in `testcontainers-modules`. No workspace Cargo.toml change needed.

**Decision 2: `seq` integer field as tracking field**
- Rationale: Avoids ObjectId string comparison complexity in `$gt` queries. Mirrors how postgres source tests use integer `id` as tracking column.
- Impact: All seeded documents MUST have `seq: 1, 2, 3, ...` in order. Fixture sets `ENV_SOURCE_TRACKING_FIELD = "seq"`.

**Decision 3: 4 sink tests, 4 source tests (not 5+6)**
- Tests dropped: `offset_tracking_across_polls`, `payload_format_json_emits_schema_json`, `metadata_fields_included` (merged into json test), `source_handles_empty_collection`, `round_trip_source_to_sink`
- Rationale documented in spec Gap 6 section.

**Decision 4: poll_interval = "10ms" in source fixtures**
- Rationale: Source connector sleeps BEFORE its first poll. Using 10ms keeps test duration acceptable.
- The 5-second total polling window (100 attempts x 50ms) gives 500x margin over the 10ms poll interval.

**Decision 5: `state_persists_across_connector_restart` uses `&mut TestHarness`**
- This is the ONLY test among all 8 that uses a mutable harness reference.
- Required because `harness.server_mut().stop_dependents()` and `start_dependents()` need mutability.

**Decision 6: MongoDB metadata fields differ between sink and source**
- Sink metadata (in MongoDB document): `_id`, `iggy_offset`, `iggy_timestamp`, `iggy_stream`, `iggy_topic`, `iggy_partition_id`
- Source metadata (in iggy message payload): `_iggy_source_collection`, `_iggy_poll_timestamp`
- The json_messages_sink_to_mongodb test checks sink metadata fields. Source tests do not check source metadata fields (they check the `seq` field to verify ordering).

### Critical Correctness Traps

**Trap 1: TOPICS vs TOPIC (plural vs singular)**
```
Sink:   ENV_SINK_STREAMS_0_TOPICS   = "IGGY_CONNECTORS_SINK_MONGODB_STREAMS_0_TOPICS"    (array)
Source: ENV_SOURCE_STREAMS_0_TOPIC  = "IGGY_CONNECTORS_SOURCE_MONGODB_STREAMS_0_TOPIC"   (singular)
```
Getting this wrong causes messages to not route. The sink topics value format is `"[test_topic]"` (bracket syntax for array).

**Trap 2: Connector binary path has no file extension**
```
Sink:   "../../target/debug/libiggy_connector_mongodb_sink"
Source: "../../target/debug/libiggy_connector_mongodb_source"
```
The runtime appends `.so` or `.dylib` based on platform. Do not hardcode the extension.

**Trap 3: `wait_for_documents` sorts by `iggy_offset` ascending**
The offset contiguity assertions in tests 1 and 3 (sink) depend on documents being returned in offset order. The `wait_for_documents` helper must include `.sort(doc! { "iggy_offset": 1 })` in its find query.

**Trap 4: `state_persists_across_connector_restart` second-batch seq values**
Second batch seeded at `seq = TEST_MESSAGE_COUNT + 1` to `TEST_MESSAGE_COUNT * 2`. With `TEST_MESSAGE_COUNT = 3`, second batch is `seq 4, 5, 6`. The assertion `seq > TEST_MESSAGE_COUNT as i64` checks `seq > 3`, which correctly validates no first-batch documents appear after restart.

**Trap 5: The `large_batch_processed_correctly` test needs `batch_size=10` configured**
The base `MongoDbSinkFixture` does not set `ENV_SINK_BATCH_SIZE`. For this test to exercise multi-batch behavior, the batch_size must be set to a value smaller than the message count (10 < 50). Either:
- (Option A) Create a `MongoDbSinkBatchFixture` that wraps base and adds `ENV_SINK_BATCH_SIZE = "10"` — cleaner, follows existing pattern
- (Option B) Set `batch_size=10` in the base fixture's `connectors_runtime_envs()` — simpler but affects all tests using base
- The rust-coder agent must pick one and record which was chosen here when updating this document.

### Codebase Architecture Facts

- The integration test crate is at `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/`
- Connector test binaries are at `../../target/debug/` relative to the integration test working directory
- The `TestFixture` trait requires exactly two methods: `async fn setup() -> Result<Self, TestBinaryError>` and `fn connectors_runtime_envs(&self) -> HashMap<String, String>`
- `#[iggy_harness(...)]` macro handles fixture setup/teardown automatically
- Container drop handles teardown — no explicit teardown needed in fixture
- The `seeds::connector_stream` seed creates the stream and topic referenced by `seeds::names::STREAM` and `seeds::names::TOPIC`

### Existing File Locations (for reference during implementation)

Pattern files to study:
- Elasticsearch container (GenericImage pattern): `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/fixtures/elasticsearch/container.rs`
- Postgres sink fixture (TestFixture trait pattern): `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/fixtures/postgres/sink.rs`
- Postgres source fixture: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/fixtures/postgres/source.rs`
- Postgres sink tests: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/postgres/postgres_sink.rs`
- Postgres source tests (restart test pattern): `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/integration/tests/connectors/postgres/postgres_source.rs`

MongoDB connector implementations:
- Sink: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/connectors/sinks/mongodb_sink/src/lib.rs`
- Source: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/connectors/sources/mongodb_source/src/lib.rs`

Connector config files (referenced by sink.toml/source.toml):
- Sink config: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/connectors/sinks/mongodb_sink/config.toml`
- Source config: `/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/core/connectors/sources/mongodb_source/config.toml`

---

## Blockers and Questions

**Blocker B1**: `mongodb` dev-dependency missing from `core/integration/Cargo.toml` (WI-12). Without this, compilation fails immediately. This must be the FIRST action.

**Open Question Q1**: `large_batch_processed_correctly` — which fixture variant for batch_size? (Option A: new `MongoDbSinkBatchFixture`, Option B: set in base). The rust-coder agent should resolve this and update this document with the decision when implementing WI-07.

**Open Question Q2**: Does the `#[iggy_harness]` macro import `DEFAULT_POLL_ATTEMPTS` and `DEFAULT_POLL_INTERVAL_MS` from the fixture automatically, or do these need to be explicitly imported in the test file from the container module? The spec snippet shows `DEFAULT_POLL_ATTEMPTS` used directly in `auto_create_collection_on_open` without a `super::` prefix. Verify by looking at how other tests import constants from container modules.

---

## Technical Debt Identified

**TD-01**: The `large_batch_processed_correctly` test does not parametrize batch_size — it will need a companion fixture variant or configuration override. If batch_size is not set to less than 50, the connector may process all 50 in one batch and the test would still pass, but the "split across multiple inserts" behavior would not be exercised.

**TD-02**: No round-trip test in v1. The spec explicitly deferred this as a stretch goal. It would require both sink and source connectors running simultaneously against the same MongoDB instance.

**TD-03**: Source `state_persists_across_connector_restart` test uses `sleep(Duration::from_secs(2))` after restart — a fixed sleep, not a polling assertion. This could be flaky on slow CI. Could be improved with a polling wait for the connector to acknowledge readiness, but the postgres test uses the same pattern.

---

## Performance / Metrics

No performance benchmarks apply to these E2E integration tests. The tests are correctness-only. The overall test budget is approximately:
- Container startup: ~5 seconds per test (MongoDB 7 image starts fast)
- Test execution (message flow): ~5 seconds per test (100 attempts x 50ms)
- Restart test: +2 seconds for the post-restart sleep
- Total estimated duration: ~50 seconds for all 8 tests running sequentially

---

## State Update Protocol

When the rust-coder-01 agent completes a work item, update this document as follows:

1. Change the work item status from `NOT STARTED` to `IN PROGRESS` when starting, then `COMPLETE` when done
2. Update the `Implementation Progress` table
3. Record any implementation decisions that deviated from the spec (especially for Q1 and Q2 above)
4. Add any new blockers discovered during implementation
5. Update the `Current Phase` at the top when:
   - All 15 WIs complete and WI-15 succeeds: phase = GREEN (compilation)
   - All 8 tests pass: phase = GREEN (tests)
   - Refactoring begins: phase = REFACTOR

---

## Session Correction Log

### 2026-02-22: E2E Execution Gap Corrected

**Prior state of this document**: Showed `Current Phase: RED`, all WIs as NOT STARTED.

**Actual state discovered**: All 15 WIs were completed by rust-coder-01. Files verified
to exist via `ls` commands. E2E tests compile but have never been executed.

**Root cause of stale state**: The TDD state file was not updated by rust-coder-01 after
completing the implementation. The prior TDD Context Retention Specialist session that
wrote this document predated the implementation session.

**Additional gap discovered**: The PR prep doc contained false claims that "all E2E tests
are passing." This was incorrect -- `cargo test --test mod --no-run` (compile gate only)
was confused with actual test execution. Docker is not installed; no test has been run
against a live MongoDB instance.

**Files corrected**:
- This TDD state file: phase updated, WI statuses updated, tests table updated
- `issue-2739-pr-preparation.md`: all 7 false claims about E2E execution corrected,
  Phase 5 journal entry added documenting the gap

**Verified facts as of 2026-02-22**:
- `which docker` returns nothing (Docker not installed)
- `cargo test --test mod --no-run` exits 0 (compilation verified)
- `cargo test -p iggy_connector_mongodb_sink -p iggy_connector_mongodb_source` exits 0 (52 tests pass)
