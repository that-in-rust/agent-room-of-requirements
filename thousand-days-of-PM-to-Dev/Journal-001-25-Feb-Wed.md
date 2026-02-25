You mean the full #2739 MongoDB sink, not just the last fix. Here is the complete ELI5 model.

**Confidence**
It is working in tested conditions after a full clean rebuild. I ran unit + integration + runtime tests from scratch, including the duplicate-key E2E.

**ELI5 (entire sink)**
Think of Iggy as a conveyor belt of packages, and MongoDB as shelves in a warehouse.

1. The runtime watches an Iggy stream/topic and takes packages in small batches.
2. The Mongo sink turns each package into a Mongo document.
3. It gives each document a unique shelf label `_id` from Iggy message ID.
4. It stores payload + optional metadata (`offset`, `stream`, `topic`, timestamps, checksum).
5. If Mongo says “this `_id` already exists,” that is a hard error (insert-only mode, no upsert).
6. Runtime must report that error clearly, not fake success metrics.

```mermaid
flowchart TB
A["Producer sends messages to Iggy"] --> B["Connectors runtime polls consumer group"]
B --> C["Decode schema + apply transforms"]
C --> D["Mongo sink consume()"]
D --> E["Build Mongo document per message"]
E --> F["Set _id = message.id"]
E --> G["Add metadata fields (optional)"]
E --> H["Encode payload (binary/json/string)"]
F --> I["insert_many into Mongo collection"]
G --> I
H --> I
I --> J{"Insert result"}
J -- "success" --> K["messages_processed increases"]
J -- "failure" --> L["sink returns non-zero/error"]
L --> M["runtime marks last_error + increments errors"]
```

**Where this logic lives**
1. Sink config shape and lifecycle (`open`, `consume`, `close`): [lib.rs](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs) at line 47 and line 110.
2. Core processing + batching: [lib.rs](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs) at line 211.
3. `_id` mapping to `message.id` (critical): [lib.rs](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs) at line 294.
4. Retry + transient error classification (duplicate key treated as non-transient): [lib.rs](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs) at line 362 and line 408.
5. Runtime calling sink and now checking callback result: [sink.rs](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/runtime/src/sink.rs) at line 525.
6. Runtime converting sink failure into connector error state/metrics: [sink.rs](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/runtime/src/sink.rs) at line 223.
7. Runtime sink manager exposing `last_error`: [sink.rs](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/runtime/src/manager/sink.rs) at line 86.
8. Connector config defaults: [config.toml](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/config.toml) at line 18.
9. Integration harness config for sink tests: [sink.toml](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/integration/tests/connectors/mongodb/sink.toml) at line 18.

**Why these rules are needed (Mongo-specific)**
1. Mongo `_id` is unique, so duplicate message IDs naturally collide.
2. At-least-once delivery means duplicates can happen in real systems.
3. Insert-only sink semantics mean collision is failure by design, not “update existing.”
4. If runtime ignores sink failure code, you get silent data loss + fake processed counters.
5. The fix ensures “if Mongo write failed, runtime says failed.”

```mermaid
sequenceDiagram
participant P as Producer
participant R as Runtime
participant S as Mongo Sink
participant M as MongoDB

P->>R: batch [id=1,id=2,id=3]
R->>S: consume(batch)
S->>M: insert_many(ordered)
M-->>S: id=1 inserted
M-->>S: id=2 duplicate key (11000)
M-->>S: stop remaining in that ordered batch
S-->>R: failure (non-zero)
R-->>R: set sink last_error
R-->>R: increment sink errors
R-->>R: do not count full batch as processed
```

**Code x tests (different types)**
1. Unit tests (sink crate): `cargo test -p iggy_connector_mongodb_sink`  
   Covers payload format mapping, retry parsing/classification, no-client error propagation, initial state counters.
2. Integration tests (real Mongo + runtime): `cargo test -p integration --test mod -- mongodb_sink`  
   Covers JSON path, binary path, large batch, auto-create collection, duplicate-key explicit failure test.
3. Runtime tests: `cargo test -p iggy-connectors`  
   Covers runtime metrics/error plumbing and connector manager behavior.

Key new contract test is here: [mongodb_sink.rs](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/integration/tests/connectors/mongodb/mongodb_sink.rs) at line 256.


Great call. Here’s a **line-number mapped sink-only code map** you can use during review.

Code files:
- [mongodb_sink implementation](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs)
- [mongodb_sink integration tests](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/integration/tests/connectors/mongodb/mongodb_sink.rs)

**L0 Map (city view)**
```mermaid
flowchart TB
  A["Runtime entry: Sink trait impl (L108-149)"] --> B["open(): connect + optional create (L110-123)"]
  A --> C["consume(): delegate to process_messages (L125-133)"]
  A --> D["close(): drop client + report counters (L135-148)"]

  C --> E["process_messages(): batch loop + accounting (L211-270)"]
  E --> F["insert_batch(): build Mongo docs (L272-360)"]
  F --> G["insert_batch_with_retry(): retry loop (L362-391)"]
  G --> H["is_transient_error(): retry classifier (L408-438)"]
```

**L1 Map (data path view)**
```mermaid
flowchart TB
  A["ConsumedMessage[]"] --> B["Chunk by batch_size (L220, L226)"]
  B --> C["Build document per message (L290+)"]
  C --> D["_id from message.id (L294)"]
  C --> E["Metadata fields (L296-315)"]
  C --> F["Payload transform json/binary/string (L322-353)"]
  D --> G["docs Vec (L288, L355)"]
  E --> G
  F --> G
  G --> H["insert_many with retry (L372)"]
  H --> I["successful_inserts updated (L231-233)"]
  I --> J["messages_processed += successful_inserts (L247)"]
```

**L2 Map (failure/safety view)**
```mermaid
flowchart TB
  A["insert_many error"] --> B{"Transient? (L378, L408-438)"}
  B -->|"Yes"| C["Retry with backoff (L384-387)"]
  B -->|"No"| D["Return CannotStoreData error (L379-382)"]
  C --> E{"Max retries reached?"}
  E -->|"No"| A
  E -->|"Yes"| D

  D --> F["process_messages increments insertion_errors (L235-237)"]
  F --> G["process_messages returns Err if any batch failed (L263-269)"]
```

**L3 Map (test coverage view)**
```mermaid
flowchart TB
  A["Payload contract"] --> A1["json_messages_sink_to_mongodb (L46)"]
  A --> A2["binary_messages_sink_as_bson_binary (L134)"]

  B["Batch + ordering"] --> B1["large_batch_processed_correctly (L202)"]

  C["Duplicate/failure semantics"] --> C1["duplicate_key_is_explicit_failure_and_not_silent_success (L256)"]
  C --> C2["ordered_duplicate_partial_insert_has_exact_accounting (L433)"]

  D["More failure paths"] --> D1["schema_validation_mid_batch_surfaces_hard_error_and_partial_prefix (L606)"]
  D --> D2["write_concern_timeout_does_not_report_full_success (L793)"]
  D --> D3["retryable_write_failover_keeps_single_doc_per_id (L919)"]
  D --> D4["no_writes_performed_label_path_preserves_state_accuracy (L1066)"]

  E["Startup behavior"] --> E1["auto_create_collection_on_open (L1214)"]

  F["Unit guardrails"] --> F1["given_no_client_should_return_error_not_silent_ok (lib.rs L616)"]
  F --> F2["transient classifier tests (lib.rs L567-604)"]
```

### Line-by-line reading order (ELI5 + why)

- [Config and state types](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:36): defines knobs and counters so behavior is explicit and measurable.
- [Constructor `new()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:88): applies safe defaults and initializes counters.
- [`open()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:110): ensures DB connectivity before work starts.
- [`connect()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:153): parses URI, sets pool, pings DB; prevents fake “healthy” state.
- [`ensure_collection_exists()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:182): supports auto-create startup path.
- [`consume()` -> `process_messages()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:125): runtime entry into core sink logic.
- [`process_messages()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:211): batch loop, partial-success accounting, and explicit error return.
- [`insert_batch()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:272): shapes docs; this is payload and metadata contract.
- [`insert_batch_with_retry()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:362): bounded retries for transient failures only.
- [`is_transient_error()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:408): key safety classifier for retry-vs-fail.
- [`redact_connection_uri()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:440): avoids leaking secrets in logs.
- [`close()`](/Users/amuldotexe/Desktop/A01_20260131/iggy-issue02/iggy_2739_sink/core/connectors/sinks/mongodb_sink/src/lib.rs:135): lifecycle close and final telemetry snapshot.

If you want, I can also generate the same map as a checked-in markdown file in sink repo (`docs/sink-code-map.md`) so you can link it in PR comments.

