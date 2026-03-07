# PR-2815 MongoDB Sink: Executable Specification

Generated on 2026-03-05 for branch `codex/2739-sink-sync`.

## Executable Requirements

### REQ-MDB-001.0: Idempotent Duplicate Handling
WHEN re-delivered messages map to existing documents by `_id`
THEN the sink SHALL treat duplicate-key (11000) as success for those items
AND SHALL return Ok if all non-duplicate inserts succeed
AND SHALL keep document count at exactly one per `_id`.

### REQ-MDB-002.0: Unordered Bulk Progress
WHEN a batch contains a mix of valid items and items that will fail (duplicate or validation)
THEN the sink SHALL use unordered bulk insert for the batch
AND SHALL insert all valid items in the same call
AND SHALL capture per-item failures for classification (duplicate vs non-retryable vs transient).

### REQ-MDB-003.0: Composite Identifier Uniqueness
WHEN constructing MongoDB `_id`
THEN the sink SHALL use a composite format `"{stream}:{topic}:{partition}:{message_id}"`
AND SHALL avoid cross-topic collisions by construction.

### REQ-MDB-004.0: Offset-Progress Safety (No Runtime Change)
WHEN a batch includes only idempotent duplicates as failures
THEN the sink SHALL return Ok so the consumer can advance offsets
AND SHALL NOT require any change to `core/connectors/runtime/src/sink.rs`.

### REQ-MDB-005.0: Numeric Range Safety
WHEN storing offsets and partition IDs
THEN the sink SHALL store `iggy_offset` as i64 when `<= i64::MAX`, else as string `iggy_offset_str`
AND SHALL store `iggy_partition_id` via checked conversion (i32 if in range, else i64).

### REQ-MDB-006.0: Config Normalization and Warnings
WHEN initializing the sink
THEN the sink SHALL normalize `include_*`, `batch_size`, `max_retries`, `retry_delay`, and payload format once
AND SHALL log a `warn` on unrecognized payload format and default to `binary`.

### REQ-MDB-007.0: Dependency Hygiene
WHEN building the crate
THEN the sink crate SHALL not suppress unused dependencies via `cargo-machete` ignore; unused deps SHALL be removed.

### REQ-MDB-008.0: Accurate Counters Without Locks
WHEN updating internal counters
THEN the sink SHALL use `AtomicU64` for `messages_processed` and `insertion_errors`
AND SHALL count only successfully inserted items as processed (duplicates excluded from processed).

### REQ-MDB-009.0: Retry Policy With Backoff
WHEN a transient write error occurs (e.g., `RETRYABLE_WRITE_ERROR`, network, pool, selection timeouts)
THEN the sink SHALL retry with linear backoff `attempt * retry_delay` up to `max_retries`
AND SHALL return Err after exhausting retries with the final error reason preserved.

## Test Matrix
| req_id | test_id | type | assertion | target |
| --- | --- | --- | --- | --- |
| REQ-MDB-001.0 | T-DUP-OK-1 | integration | Re-delivery of already-inserted messages returns Ok; docs remain single per `_id` | core/integration/tests/connectors/mongodb |
| REQ-MDB-002.0 | T-UNORD-1 | integration | Batch with one duplicate and two valid inserts results in 2 inserts, 1 duplicate recorded, Ok returned | core/integration/tests/connectors/mongodb |
| REQ-MDB-003.0 | T-ID-COMP-1 | integration | Two topics produce identical `message_id`; composite `_id` prevents collision; both docs exist | core/integration/tests/connectors/mongodb |
| REQ-MDB-004.0 | T-PROGRESS-1 | integration | Mid-batch duplicate causes no error; subsequent batch offsets advance (simulate by re-sending batch) | core/integration/tests/connectors/mongodb |
| REQ-MDB-005.0 | T-OFFSET-RANGE-1 | unit | Offset > i64::MAX stored under `iggy_offset_str`; smaller offset stored as i64 | mongodb_sink unit tests |
| REQ-MDB-006.0 | T-CONFIG-NORM-1 | unit | Unknown payload format logs warning and defaults to Binary; include flags cached | mongodb_sink unit tests |
| REQ-MDB-007.0 | T-DEPS-1 | build | `cargo machete` (if present) reports no unnecessary ignores; build succeeds without ignored deps | sink crate |
| REQ-MDB-008.0 | T-COUNTS-1 | unit | `messages_processed` increments only by successful inserts; duplicates excluded; atomics used | mongodb_sink unit tests |
| REQ-MDB-009.0 | T-RETRY-1 | integration | Inject transient error once; verify retry then success; total attempts = 2; returns Ok | core/integration/tests/connectors/mongodb |

## TDD Plan
1. STUB: Add failing integration tests (T-DUP-OK-1, T-UNORD-1, T-ID-COMP-1, T-PROGRESS-1) and unit tests (T-OFFSET-RANGE-1, T-CONFIG-NORM-1, T-COUNTS-1, T-RETRY-1).
2. RED: Run tests; confirm failures.
3. GREEN:
   - Implement composite id builder: `build_composite_document_id()`.
   - Use unordered `insert_many` and classify per-item errors; treat duplicate-key as success.
   - Add checked conversions for offset/partition; add `*_str` fallback.
   - Normalize config at `new()`; warn on unknown payload format.
   - Replace `Mutex<State>` with `AtomicU64` counters.
   - Keep runtime callback behavior unchanged.
4. REFACTOR: Extract helpers (e.g., `classify_insert_error_outcome()`), simplify logs, minimize allocations.
5. VERIFY: Full suite + Codecov patch, no dependency ignores, Parseltongue entity search shows new helpers.

## Quality Gates
- All tests and build pass; integration tests runnable with MongoDB fixture.
- No `TODO`/`STUB`/`FIXME` in new code.
- No runtime changes outside sink crate.
- Each `REQ-MDB-*` referenced by at least one test.
- New helpers follow four-word naming.
- No `cargo-machete` ignores for sink crate.

## Open Questions
- Should composite `_id` be configurable or fixed initially?
- For validation failures (121), return Err (default) or make configurable?
- Expose optional `ordered=true` mode as opt-in?
- Add separate `duplicate_skips` counter for observability?
- Any `_id` length/encoding constraints in deployment?

## Implementation Notes (non-binding)
- Suggested helpers (4WNC): `build_composite_document_id`, `classify_insert_error_outcome`, `apply_unordered_insert_strategy`.
- Keep `_id` ASCII-safe; escape `:` if necessary.

## Parseltongue Queries Run
(Logged in run folder: `queries/queried-endpoints.log`)
- GET /server-health-check-status
- GET /codebase-statistics-overview-summary
- GET /folder-structure-discovery-tree
- GET /api-reference-documentation-help
- GET /code-entities-list-all
- GET /code-entities-list-all?entity_type=fn
- GET /code-entities-search-fuzzy?q=main
- GET /code-entities-search-fuzzy?q=mongodb
- GET /code-entities-search-fuzzy?q=process_messages
- GET /code-entities-search-fuzzy?q=insert_batch_with_retry
- GET /code-entities-search-fuzzy?q=MongoDbSink
- GET /reverse-callers-query-graph?entity=rust:method:process_messages:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_sinks_mongodb_sink_src_lib:T1836509056
- GET /forward-callees-query-graph?entity=rust:method:process_messages:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_sinks_mongodb_sink_src_lib:T1836509056
- GET /smart-context-token-budget?focus=rust:method:process_messages:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_sinks_mongodb_sink_src_lib:T1836509056&tokens=4000
- GET /ingestion-diagnostics-coverage-report?section=summary
- GET /ingestion-diagnostics-coverage-report?section=test_entities
- GET /ingestion-coverage-folder-report?depth=3
- GET /code-entity-detail-view?key=rust:method:process_messages:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_sinks_mongodb_sink_src_lib:T1836509056
- GET /code-entity-detail-view?key=rust:method:insert_batch_with_retry:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_sinks_mongodb_sink_src_lib:T1777147853
- GET /code-entity-detail-view?key=rust:method:insert_batch:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_sinks_mongodb_sink_src_lib:T1890535942
- GET /code-entity-detail-view?key=rust:fn:is_transient_error:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_sinks_mongodb_sink_src_lib:T1700865724
- GET /code-entity-detail-view?key=rust:method:new:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_sinks_mongodb_sink_src_lib:T1767653871
- GET /code-entity-detail-view?key=rust:method:from_config:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_sinks_mongodb_sink_src_lib:T1795465424
- GET /code-entity-detail-view?key=rust:struct:MongoDbSink:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_sinks_mongodb_sink_src_lib:T1607229599
- GET /code-entity-detail-view?key=rust:fn:process_messages:___Users_amuldotexe_Desktop_iggy202603_iggy_codex_2739_sink_sync_core_connectors_runtime_src_sink:T1657268432
