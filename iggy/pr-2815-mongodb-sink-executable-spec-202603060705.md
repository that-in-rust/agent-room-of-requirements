# PR-2815 MongoDB Sink: Executable Specification (Updated)

Generated on 2026-03-06 07:05 (Asia/Kolkata) for branch `codex/2739-sink-sync`.  
Supersedes: `/Users/amuldotexe/Desktop/agent-room-of-requirements/iggy/pr-2815-mongodb-sink-executable-spec-202603051856.md`

## Executable Requirements

### REQ-MDB-001.1: Idempotent Duplicate Handling
**WHEN** re-delivered messages map to existing MongoDB documents by `_id`  
**THEN** the sink SHALL treat duplicate-key write errors (code `11000`) as idempotent success for those specific items  
**AND** SHALL return `Ok` when all non-duplicate writes in the same batch succeed  
**SHALL** keep document count at exactly one per `_id`.

### REQ-MDB-002.1: Unordered Bulk Progress
**WHEN** a batch contains a mix of valid items and duplicate/failing items  
**THEN** the sink SHALL execute `insert_many` with `ordered(false)`  
**AND** SHALL persist valid items from the same call without stopping at first duplicate  
**SHALL** classify duplicate-only outcomes separately from hard/transient failures.

### REQ-MDB-003.1: Composite Identifier Uniqueness
**WHEN** constructing MongoDB `_id`  
**THEN** the sink SHALL use the format `"{stream}:{topic}:{partition}:{message_id}"`  
**AND** SHALL prevent cross-topic collisions for identical `message_id` and partition values  
**SHALL** preserve one-document-per-message identity under this composite key.

### REQ-MDB-004.1: Offset Progress Safety Without Runtime Changes
**WHEN** a batch has only idempotent duplicate failures  
**THEN** the sink SHALL return `Ok` so consumer offsets can advance  
**AND** SHALL keep runtime behavior compatible without modifying `core/connectors/runtime/src/sink.rs`  
**SHALL** keep sink status non-error for duplicate-only outcomes.

### REQ-MDB-005.1: Numeric Range Safety for Metadata
**WHEN** storing offset and partition metadata  
**THEN** the sink SHALL store `iggy_offset` as `i64` when `offset <= i64::MAX`  
**AND** SHALL store oversized offsets under `iggy_offset_str` as decimal string  
**SHALL** store `iggy_partition_id` as `i32` when in range, otherwise as `i64`.

### REQ-MDB-006.1: Config Normalization and Warning Contract
**WHEN** initializing the sink from config  
**THEN** the sink SHALL normalize `batch_size`, `include_*` flags, `max_retries`, `retry_delay`, and payload format exactly once in `new()`  
**AND** SHALL default unknown payload formats to `binary`  
**SHALL** emit a `warn` log for unknown payload format.

### REQ-MDB-007.1: Dependency Hygiene Enforcement
**WHEN** validating crate dependencies  
**THEN** the sink crate SHALL have no `cargo-machete` ignore overrides for unused dependencies  
**AND** SHALL remove actually unused dependencies from `Cargo.toml` and `Cargo.lock`  
**SHALL** pass `cargo machete --with-metadata` without findings for `iggy_connector_mongodb_sink`.

### REQ-MDB-008.1: Accurate Counters Without Locks
**WHEN** tracking sink processing metrics  
**THEN** the sink SHALL use `AtomicU64` counters for `messages_processed` and `insertion_errors`  
**AND** SHALL increment processed count only for successful inserts (excluding duplicate skips)  
**SHALL** avoid `Mutex<State>` locking for these counters.

### REQ-MDB-009.1: Retry Policy With Linear Backoff
**WHEN** transient write failures occur (network, pool, server selection, retryable write conflict classes)  
**THEN** the sink SHALL retry with linear backoff `attempt * retry_delay` up to `max_retries`  
**AND** SHALL stop retrying and return final error after retry budget is exhausted  
**SHALL** preserve non-transient failures as errors without false success.

## Test Matrix

| req_id | test_id | type | assertion | target |
| --- | --- | --- | --- | --- |
| REQ-MDB-001.1 | T-DUP-OK-1 | integration | Pre-seeded duplicate in batch is treated idempotently; no extra doc for same `_id`; sink remains non-error | `core/integration/tests/connectors/mongodb/mongodb_sink.rs` |
| REQ-MDB-002.1 | T-UNORD-1 | integration | With duplicate in middle, suffix valid message still persists (`ordered(false)` behavior) | `core/integration/tests/connectors/mongodb/mongodb_sink.rs` |
| REQ-MDB-003.1 | T-ID-CROSS-1 | unit (new) | Same `message_id` + partition with different topic names yields different composite `_id` strings | `core/connectors/sinks/mongodb_sink/src/lib.rs` tests |
| REQ-MDB-004.1 | T-PROGRESS-1 | integration | Duplicate-only batch does not force sink status error; runtime file remains unchanged in diff | `core/integration/tests/connectors/mongodb/mongodb_sink.rs` + git diff gate |
| REQ-MDB-005.1 | T-OFFSET-RANGE-1 | unit (new) | `offset > i64::MAX` stored as `iggy_offset_str`; smaller offset stored as `iggy_offset` i64 | `core/connectors/sinks/mongodb_sink/src/lib.rs` tests |
| REQ-MDB-005.1 | T-PARTITION-RANGE-1 | unit (new) | Partition id converts to `Bson::Int32` in range and `Bson::Int64` otherwise | `core/connectors/sinks/mongodb_sink/src/lib.rs` tests |
| REQ-MDB-006.1 | T-CONFIG-NORM-1 | unit (expand) | Cached config fields in sink struct match normalized defaults/overrides | `core/connectors/sinks/mongodb_sink/src/lib.rs` tests |
| REQ-MDB-006.1 | T-CONFIG-WARN-1 | unit (new) | Unknown payload format emits `warn` and resolves to `PayloadFormat::Binary` | `core/connectors/sinks/mongodb_sink/src/lib.rs` tests |
| REQ-MDB-007.1 | T-DEPS-1 | build | `cargo machete --with-metadata` reports no unused sink dependencies | sink crate |
| REQ-MDB-008.1 | T-COUNTS-1 | unit | `messages_processed` tracks only successful inserts; `insertion_errors` updates on failed batches | `core/connectors/sinks/mongodb_sink/src/lib.rs` tests |
| REQ-MDB-009.1 | T-RETRY-1 | integration | Retryable error path recovers and stores one doc per id | `core/integration/tests/connectors/mongodb/mongodb_sink.rs` |

## TDD Plan

1. STUB
- Add failing tests: `T-ID-CROSS-1`, `T-OFFSET-RANGE-1`, `T-PARTITION-RANGE-1`, `T-CONFIG-WARN-1`.
- Add build-check task for `T-DEPS-1`.
- Use four-word helper naming for new test helpers (example: `build_cross_topic_documents_expected`).

2. RED
- Run `cargo test -p iggy_connector_mongodb_sink`.
- Run `cargo test -p integration --test mod connectors::mongodb::mongodb_sink::`.
- Run `cargo machete --with-metadata` and capture failing dependency list.

3. GREEN
- Remove unused sink dependencies reported by machete.
- Implement/adjust minimal logic for missing cross-topic and range/warn contracts.
- Keep runtime file unchanged for REQ-MDB-004.1.

4. REFACTOR
- Keep helper names 4WNC-compliant where new symbols are added.
- Consolidate duplicate assertion helpers in Mongo sink integration tests.
- Keep logs concise and avoid behavior changes outside sink scope.

5. VERIFY
- `cargo fmt --all -- --check`
- `cargo clippy -p iggy_connector_mongodb_sink --all-targets --all-features -- -D warnings`
- `cargo test -p iggy_connector_mongodb_sink`
- `cargo test -p integration --test mod connectors::mongodb::mongodb_sink::`
- `cargo machete --with-metadata`
- `cargo sort --check --workspace`
- `cargo test --locked --doc`
- `cargo doc --no-deps --all-features --quiet`

## Quality Gates

- Every `REQ-MDB-*.1` maps to at least one test in the matrix.
- No runtime edits outside sink crate for this PR (`core/connectors/runtime/src/sink.rs` unchanged).
- No `TODO`, `STUB`, `FIXME` in new sink PR code.
- `cargo machete --with-metadata` is clean for sink crate.
- Mongo sink integration slice passes on real Docker-backed MongoDB.
- Repo-level checks pass in a clean workspace:
  - `./scripts/ci/trailing-whitespace.sh --check --ci`
  - `./scripts/ci/trailing-newline.sh --check --ci`
  - `./scripts/ci/taplo.sh --check --ci`
  - `./scripts/ci/markdownlint.sh --check`
  - `./scripts/ci/sync-rust-version.sh --check`
  - `./scripts/ci/python-version-sync.sh --check`
  - `./scripts/ci/licenses-list.sh --check`
  - `./scripts/ci/license-headers.sh --check` (run after excluding generated `test_logs/**` artifacts)

## Open Questions

- Should duplicate skips be exposed as a dedicated metric (for observability) instead of only implied via processed/error counters?
- Should `_id` component escaping be formalized if stream/topic can contain separator `:`?
- Do we want a strict non-transient classification contract test table by Mongo error code in unit tests?
- For PR CI, should generated `test_logs/**` be excluded from license-header check or cleaned as pre-step?
