# E2E Testing Learnings from MongoDB Connectors for Kafka

## What the Industry Does

### MongoDB Kafka Connector (MongoDB Inc)
- Embedded Kafka cluster (in-process) + external MongoDB replica set
- **Round-trip testing is the gold standard**: Source DB → Kafka → Sink DB → compare databases field-by-field
- `ChangeStreamRoundTripTest`: full CRUD (insert/update/replace/delete) replicated and verified
- `FullDocumentRoundTripIntegrationTest`: verifies JSON, BSON, Avro formats survive the round trip
- Exponential backoff for assertions: `1000 + 250 * retry^2` ms, up to 15 retries (~5 min max)
- Tests multi-partition, multi-task, connector restart survival
- Verifies JMX metrics: `records-successful`, `records-failed`, `batch-writes-successful`

### Debezium MongoDB Connector
- Docker container with `mongo` image, **replica set mandatory** (change streams need oplog)
- 39+ test classes covering CDC, snapshots, field filtering, schema, sharded clusters
- `@SkipWhenDatabaseVersion` annotation for version-gated tests
- `Awaitility` for async polling: 5s timeout, 100ms poll interval
- `LogInterceptor` to assert on log output patterns
- Tests: invalid SSL, config validation, server selection timeout, incremental snapshots with 1000 docs

### Apache Flink MongoDB Connector
- Testcontainers with `MongoDBContainer` + Flink's `FlinkContainers`
- Multi-version testing via system property (`-Dmongodb.version=4/5/6/7`)
- Deadline-based polling: `Deadline.fromNow(Duration.ofSeconds(20))` with 1s sleep
- Assertion helpers: `assertThatIdsAreWrittenWithMaxWaitTime`, `assertThatIdsAreWrittenInAnyOrder`
- Tests: upsert sink, append-only sink, network aliases for container-to-container comms

### Rust testcontainers-modules (crate)
- Feature flag: `mongo` — default image `mongo:5.0.6`
- Supports standalone AND **replica set** mode via `Mongo::repl_set()`
- Replica set: runs `rs.initiate()` via mongosh, waits for stepUp log message
- Critical: use `?directConnection=true` for single-node replica set via mapped port

---

## Key Patterns to Steal

1. **Round-trip test** (mongo-kafka): MongoDB A → Iggy → MongoDB B → compare databases
2. **Exponential backoff assertions** (mongo-kafka): every project does some form of retry
3. **Replica set mode always** (Debezium): matches production, enables future CDC
4. **Deadline-based polling** (Flink): `Instant::now() + timeout`, poll every 500ms
5. **Clean up between tests**: drop databases + reset offsets to prevent cross-contamination
6. **Version-gated tests** (Debezium): skip tests for unsupported MongoDB versions

---

## What E2E Tests We Should Build for Iggy

### Infrastructure
- `testcontainers-modules` with `Mongo::repl_set()` (not GenericImage)
- Add `"mongo"` feature to testcontainers-modules in root Cargo.toml
- Follow Elasticsearch `GenericImage` fixture pattern from existing iggy tests
- 9 new files: 4 fixture files + 5 test module files

### Tier 1 — Sink Tests (5)

| Test | Verifies | Inspired By |
|---|---|---|
| `json_messages_sink_to_mongodb` | JSON payloads land as queryable BSON documents, metadata fields correct | mongo-kafka FullDocumentRoundTrip |
| `binary_messages_sink_as_bson_binary` | Raw bytes stored as BSON Binary (subtype Generic) | mongo-kafka FullDocumentRoundTrip |
| `metadata_fields_included` | iggy_offset, iggy_stream, iggy_topic, iggy_timestamp, iggy_checksum all present | Iggy-specific |
| `large_batch_processed_correctly` | 50 msgs with batch_size=10 all arrive, no duplicates, contiguous offsets | mongo-kafka multi-task |
| `auto_create_collection_on_open` | Collection exists before any messages sent when config enabled | mongo-kafka |

### Tier 2 — Source Tests (6)

| Test | Verifies | Inspired By |
|---|---|---|
| `source_polls_documents_to_iggy` | 3 seeded docs appear as messages in iggy stream, correct order | mongo-kafka CopyExisting |
| `offset_tracking_across_polls` | Insert batch 1, poll, insert batch 2 — only batch 2 in second poll | Debezium IncrementalSnapshot |
| `delete_after_read_removes_documents` | MongoDB doc count drops to 0 after polling | Iggy-specific |
| `mark_processed_sets_field` | is_processed flips from false to true, docs not deleted | Iggy-specific |
| `state_persists_across_restart` | Stop connector, insert more docs, restart — no duplicates | mongo-kafka restart survival |
| `source_handles_empty_collection` | No error, no messages produced | Debezium |

### Tier 3 — Round-Trip (stretch goal)

| Test | Verifies | Inspired By |
|---|---|---|
| `round_trip_source_to_sink` | MongoDB A → Iggy → MongoDB B → field-by-field comparison | mongo-kafka ChangeStreamRoundTrip |

### Async Verification Patterns

```rust
// Deadline-based polling (from Flink)
async fn wait_for_documents(collection: &Collection<Document>, expected: usize, timeout: Duration) -> Vec<Document> {
    let deadline = Instant::now() + timeout;
    loop {
        let docs = collection.find(doc!{}).sort(doc!{"iggy_offset": 1}).await...;
        if docs.len() >= expected || Instant::now() > deadline {
            return docs;
        }
        tokio::time::sleep(Duration::from_millis(500)).await;
    }
}

// Exponential backoff (from mongo-kafka)
async fn retry_until<F, Fut>(check: F, max_retries: u32)
where F: Fn() -> Fut, Fut: Future<Output = bool> {
    for attempt in 0..max_retries {
        if check().await { return; }
        tokio::time::sleep(Duration::from_millis(1000 + 250 * (attempt as u64).pow(2))).await;
    }
}
```

---

## File Structure

```
core/integration/tests/connectors/
  fixtures/mongodb/
    container.rs     # MongoDbContainer (GenericImage or testcontainers-modules Mongo)
    sink.rs          # MongoDbSinkFixture, MongoDbSinkJsonFixture, MongoDbSinkBinaryFixture
    source.rs        # MongoDbSourceJsonFixture, MongoDbSourceDeleteFixture, MongoDbSourceMarkFixture
    mod.rs
  mongodb/
    mod.rs
    mongodb_sink.rs  # 5 sink tests
    mongodb_source.rs # 6 source tests
    sink.toml
    source.toml
  fixtures/mod.rs    # add: mod mongodb;
  mod.rs             # add: mod mongodb;
```

---

## Sources
- [mongodb/mongo-kafka](https://github.com/mongodb/mongo-kafka) — MongoDB Inc's official Kafka connector
- [debezium/debezium](https://github.com/debezium/debezium) — Debezium CDC platform
- [apache/flink-connector-mongodb](https://github.com/apache/flink-connector-mongodb) — Flink MongoDB connector
- [testcontainers-rs-modules-community](https://github.com/testcontainers/testcontainers-rs-modules-community) — Rust testcontainers modules
