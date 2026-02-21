# MongoDB Connector Gap Analysis

## Three-Way Comparison: Implementation vs Spec vs Docs

### Implementation vs Spec — Top 3 Differences

**1. Sink uses `connection_uri` instead of `connection_string`**
The spec explicitly says `connection_string`. Our sink uses `connection_uri` (likely because `Client::with_uri_str()` uses the word "URI"). This also means the sink uses a different connection method (`Client::with_uri_str()` vs `ClientOptions::parse()` + `Client::with_options()`), which makes it **impossible to configure `max_pool_size`** in the sink.

**2. Sink missing 3 config fields: `max_pool_size`, `auto_create_collection`, `payload_field_name`**
The spec defines all three. Our sink has none of them. The `auto_create_collection` logic (collection creation in `open()`) is entirely absent.

**3. Source state fields diverge: `tracking_offsets` (HashMap) vs spec's `tracking_offset` (Option\<String\>)**
Our source uses a HashMap keyed by collection name; the spec uses a single scalar. The field is also named `processed_documents` vs spec's `processed_count`. This is a **serialization compatibility break** — old state can't be deserialized by the other format.

### Implementation vs Docs/Thesis — Top 3 Differences

**1. Source has NO retry logic** — `get_max_retries()` exists but is never called. The thesis explicitly flags this as an "unjustified deviation." A single transient network error kills the source permanently.

**2. Source test naming uses `test_*` convention** (all 12 tests) instead of the required `given_*_should_*` format. The sink tests are correct; the source tests were written without checking the convention.

**3. Source `payload_format` config is completely ignored** — `Schema::Json` is hardcoded at line 207. A user setting `payload_format = "bson"` gets silently wrong behavior. The thesis flagged missing payload extraction tests.

### Spec vs Docs — Top 3 Differences

**1. State schema incompatibility** — Spec says single `tracking_offset: Option<String>`, thesis praises the HashMap approach as "functionally equivalent" without noting the migration incompatibility.

**2. `validate_collection()` severity** — Spec says fail hard with `Err()`. Implementation warns and continues. Thesis marked it `PASS` by checking method existence, not behavior.

**3. `PayloadFormat` defaults differ** — Spec source defaults to `Json`, sink defaults to `Binary`. Best-practices doc is silent on what the default should be.

---

## Root Cause Analysis: Why Did We Miss This?

| Root Cause | Examples |
|---|---|
| **Implementation deviated from spec without feedback loop** | `connection_uri` vs `connection_string` — the MongoDB driver API uses "URI" which overrode the spec's naming |
| **Thesis was too generous** — evaluated "does the method exist" not "does it behave correctly" | `validate_collection()` marked PASS despite being a warning not an error |
| **Sink and source were developed independently** without cross-referencing | Different connection methods, different config field names, different test conventions |
| **"Happy path works" trap** | `Schema::Json` hardcode works for most cases so `payload_format` was never wired up |
| **Method stub without integration** | `get_max_retries()` was implemented to satisfy the spec's interface, but the retry loop itself was never written |
| **Best-practices doc and spec were written for different audiences** at different times — no explicit priority when they conflict |

---

## Industry Research: What the Best in Business Do

### Connection Field Naming

| Platform | Field Name |
|---|---|
| **MongoDB Kafka Connector** (MongoDB Inc) | `connection.uri` |
| **Debezium** | `mongodb.connection.string` |
| **Apache Flink** | `uri` |
| **Airbyte** | `connection_string` |
| **Fivetran** | `hosts` (decomposed) |
| **Confluent** | `connection.uri` |

In Rust snake_case, MongoDB's own convention (`connection.uri`) becomes `connection_uri`. PostgreSQL and Airbyte use `connection_string`. The industry is genuinely split.

### Batch Insert: `insertMany` vs `bulkWrite`

**Every major production connector uses `bulkWrite()`** — MongoDB Kafka Connector, Debezium, Confluent all use it.

However, the MongoDB Rust driver's `bulk_write()` requires **Server 8.0+**. For insert-only workloads, `insert_many()` internally calls `bulkWrite()` anyway — identical performance, broader server compatibility.

MongoDB's own docs: "Using `bulkWrite`, you can do many operations in a single connection. Internally, `insertMany` uses `bulkWrite`, so there's no difference — it's just for convenience."

### Collection Validation on Startup

**The industry standard is: do NOT fail hard.** No major connector validates collection existence at startup:

| Platform | Behavior |
|---|---|
| **MongoDB Kafka Source** | Opens change stream and waits. Works on non-existent collections. |
| **Debezium** | Filters change stream events via regex. Non-existent collection = no events. |
| **Flink** | Returns zero documents. No error. |
| **Flink CDC** | Opens change streams. Handles non-existent collections gracefully. |

Rationale: MongoDB collections are created lazily. The source connector may start before the app that creates the collection.

---

## Design Decisions (Resolved)

| Decision | Choice | Rationale |
|---|---|---|
| Connection field name | **`connection_uri`** for both sink and source | MongoDB's own Kafka Connector uses `connection.uri`. Rename source's `connection_string` to `connection_uri`. |
| Batch insert API | **Keep `insert_many()`** | `bulk_write()` requires Server 8.0+. We're append-only (no CDC). `insert_many` internally calls `bulkWrite`. Identical perf, broader compat. |
| Collection validation | **Warn and continue** (current behavior) | Industry standard — Kafka Connect, Debezium, Flink all do this. Fix the misleading log message ("will be created on first write" is wrong for a source). |
| E2E tests | **Full E2E** for both sink and source | Use existing testcontainers + `#[iggy_harness]` pattern from Postgres. |

---

## Full Issue List

### Must fix (blocking)

| # | Issue | File | Impact |
|---|---|---|---|
| F1 | Source has no retry logic despite config fields for it | `sources/mongodb_source/src/lib.rs` | High — permanent failure on transient errors |
| F2 | 4 unused config fields in source (`initial_offset`, `snake_case_fields`, `payload_format`, `include_metadata`) | `sources/mongodb_source/src/lib.rs` | High — dead code, silent misconfiguration |
| F3 | Source timestamps always `Utc::now()` — discards original document temporal data | `sources/mongodb_source/src/lib.rs:392-393` | Medium — data loss |
| F4 | Source misuses `Error::InitError` for runtime query errors | `sources/mongodb_source/src/lib.rs` | Medium — wrong error semantics |

### Should fix (quality)

| # | Issue | File | Impact |
|---|---|---|---|
| S1 | Source `connection_string` should be `connection_uri` to match sink and MongoDB convention | `sources/mongodb_source/src/lib.rs:60`, `config.toml` | Medium — naming inconsistency |
| S2 | Sink missing `max_pool_size`, `auto_create_collection` config fields | `sinks/mongodb_sink/src/lib.rs:46-59` | Medium — feature gap |
| S3 | Sink `connect()` uses `Client::with_uri_str()` instead of `ClientOptions::parse()` — can't configure pool | `sinks/mongodb_sink/src/lib.rs:144-162` | Medium — architectural limitation |
| S4 | Sink `process_messages()` swallows errors — returns `Ok(())` even on batch failures | `sinks/mongodb_sink/src/lib.rs:164-204` | Medium — silent data loss |
| S5 | No `is_transient_error()` for selective retry | Both connectors | Low-Medium |
| S6 | `docs.to_vec()` clones documents on every retry attempt | `sinks/mongodb_sink/src/lib.rs:302` | Low — perf inefficiency |
| S7 | Source `validate_collection()` log message is misleading ("will be created on first write" — sources don't write) | `sources/mongodb_source/src/lib.rs:249` | Low |

### Test quality

| # | Issue | File | Impact |
|---|---|---|---|
| T1 | All 12 source tests use `test_*` naming instead of `given_*_should_*` | `sources/mongodb_source/src/lib.rs:484-582` | Low — convention |
| T2 | Missing integration tests with Docker MongoDB | N/A (new files needed) | Medium |

---

## SDK Error Types Available

For reference, here are the error variants available in `iggy_connector_sdk`:

- `Error::InitError(String)` — for initialization/setup failures only
- `Error::Connection(String)` — for connection failures during runtime
- `Error::Storage(String)` — for storage/query runtime errors
- `Error::CannotStoreData(String)` — for data write failures
- `Error::InvalidRecord` — for document conversion failures
- `Error::InvalidConfig` — for malformed config
- `Error::InvalidPayloadType` — for payload type mismatches
- `Error::InvalidJsonPayload` / `Error::InvalidTextPayload` — for payload parsing
- `Error::Serialization(String)` — for serialization errors

The source should use `Error::Connection` and `Error::Storage` for runtime errors, not `Error::InitError`.

---

## E2E Test Infrastructure (Already Available)

The repo has full testcontainers + `#[iggy_harness]` infrastructure. Key patterns:
- `TestFixture` trait with `setup()` and `connectors_runtime_envs()`
- PostgreSQL and Elasticsearch fixtures as templates
- `testcontainers-modules` v0.14.0 in workspace (needs `"mongodb"` feature added)
- GenericImage pattern available for custom containers

New files needed for E2E:
```
core/integration/tests/connectors/fixtures/mongodb/
  container.rs, sink.rs, source.rs, mod.rs
core/integration/tests/connectors/mongodb/
  mod.rs, mongodb_sink.rs, mongodb_source.rs, sink.toml, source.toml
```
