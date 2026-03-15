# MCU-Style Walkthrough: Iggy Connectors Down to `postgres_source/src/lib.rs`

```text
Date: 2026-03-15
Repo for notes only: agent-room-of-requirements
Source repo intentionally left untouched: iggy

========================================================================
0. WHAT THIS NOTE IS
========================================================================

This is an outside-in, "MCU camera zoom" explanation of:

1. What Apache Iggy is
2. Where connectors fit
3. Which connector crates exist
4. Which outside systems they talk to
5. How the runtime, SDK, and plugin crates snap together
6. How one concrete source connector works
7. A line-by-line, line-band walkthrough of:

   iggy/core/connectors/sources/postgres_source/src/lib.rs

This is a code-reading note, not a code change note.


========================================================================
1. EXTREME OUTSIDE: WHAT IGGY DOES
========================================================================

Think of Iggy as a very fast post office + event log.

Apps put messages in.
Other apps read messages out.
Messages stay stored in order.
Consumers can replay old messages later.

ASCII mental model:

  +---------+      +-------------------+      +-------------+
  | App A   | ---> |                   | ---> | Database    |
  | App B   | ---> |       IGGY        | ---> | Analytics   |
  | App C   | ---> |                   | ---> | Search      |
  | Sensors | ---> |  stream/topic log | ---> | ML systems  |
  +---------+      +-------------------+      +-------------+

Key point:
Iggy itself is the streaming system.
It is not "Postgres with extra features".
It is not "Kafka on top of SQL".
It is its own Rust server with its own storage and transport layers.


========================================================================
2. WHERE IT LIVES IN THE REPO
========================================================================

The codebase is a Rust workspace.

High level:

  iggy/
  |
  +-- core/server/              <- the Iggy server itself
  +-- core/sdk/                 <- client SDK crate
  +-- core/connectors/          <- connector subsystem
  |   |
  |   +-- runtime/              <- control tower / loader / orchestrator
  |   +-- sdk/                  <- traits, schemas, macros, helpers
  |   +-- sources/              <- source plugin crates
  |   +-- sinks/                <- sink plugin crates
  |
  +-- core/integration/tests/   <- end-to-end tests
  +-- foreign/                  <- non-Rust SDKs and integrations
  +-- web/                      <- web UI

The important idea is:

  core/server      != connectors runtime

The connectors runtime is a separate program that talks to Iggy.
It is not the same process as the main message server logic.


========================================================================
3. WHAT CONNECTORS ARE
========================================================================

A connector is a bridge between Iggy and some outside system.

Two directions:

  Source:
    outside world -> Iggy

  Sink:
    Iggy -> outside world

ASCII:

  source connector
  +-----------+      +------------------+
  | Postgres  | ---> | Iggy stream/topic|
  +-----------+      +------------------+

  sink connector
  +------------------+      +-----------+
  | Iggy stream/topic| ---> | Postgres  |
  +------------------+      +-----------+


========================================================================
4. WHICH OUTSIDE SYSTEMS THIS CONNECTOR SUBSYSTEM TALKS TO
========================================================================

In the Rust connector area shown in this repo:

Sources:
  - PostgreSQL
  - Elasticsearch
  - Random generator (testing/dev)

Sinks:
  - PostgreSQL
  - Elasticsearch
  - MongoDB
  - Apache Iceberg
  - Quickwit
  - Stdout

So if you ask "which databases does this subsystem deal with?",
the concrete answer in this workspace is:

  Postgres
  Elasticsearch
  MongoDB
  Iceberg catalogs / object storage world
  Quickwit


========================================================================
5. THE THREE MAIN CONNECTOR LAYERS
========================================================================

There are three concentric rings:

  +-------------------------------------------------------------+
  | Layer 1: runtime                                            |
  | core/connectors/runtime                                     |
  |                                                             |
  | "Which plugins exist? Load them. Start them. Wire them."    |
  +-------------------------------------------------------------+
                           |
                           v
  +-------------------------------------------------------------+
  | Layer 2: sdk                                                |
  | core/connectors/sdk                                         |
  |                                                             |
  | "What shape must a plugin have? What is a Source?           |
  |  What is ProducedMessages? How do FFI entrypoints look?"    |
  +-------------------------------------------------------------+
                           |
                           v
  +-------------------------------------------------------------+
  | Layer 3: plugin crate                                       |
  | core/connectors/sources/postgres_source                     |
  |                                                             |
  | "How do I actually read rows from Postgres?"                |
  +-------------------------------------------------------------+

This note zooms through those layers in that order.


========================================================================
6. HOW CONFIG FLOWS IN
========================================================================

There are two config levels:

  A. runtime config
     "how does the runtime talk to Iggy?"
     "where do connector config files live?"
     "where should state be stored?"

  B. connector config
     "which shared library should be loaded?"
     "which stream/topic should receive messages?"
     "what is the Postgres connection string?"
     "which tables should be polled?"

ASCII:

  runtime config
  +-------------------------------------------+
  | [iggy]                                    |
  | [state]                                   |
  | [connectors] config_dir = ...             |
  +-------------------------------------------+
                        |
                        v
  connector config file
  +-------------------------------------------+
  | type = "source"                           |
  | key = "postgres"                          |
  | path = "../../target/...postgres_source"  |
  | [[streams]] stream=... topic=...          |
  | [plugin_config] connection_string=...     |
  +-------------------------------------------+
                        |
                        v
  PostgresSourceConfig Rust struct


========================================================================
7. HOW THE RUNTIME STARTS
========================================================================

The runtime binary is:

  core/connectors/runtime/src/main.rs

What it does:

  1. Load env / config
  2. Create Iggy producer and consumer clients
  3. Ask a config provider for active source/sink configs
  4. Dynamically load shared libraries
  5. Call source/sink open hooks
  6. Spawn background tasks
  7. Expose HTTP stats / health / config API

ASCII call picture:

  runtime main()
     |
     +--> load runtime config
     +--> create Iggy clients
     +--> fetch connector configs
     +--> source::init(...)
     +--> sink::init(...)
     +--> source::handle(...)
     +--> sink::consume(...)
     +--> api::init(...)


========================================================================
8. HOW PLUGINS ARE LOADED
========================================================================

The runtime does not statically link every connector into one giant binary.
Instead it loads connector libraries dynamically.

That means the connector crate compiles to:

  .so     on Linux
  .dylib  on macOS
  .dll    on Windows

ASCII:

  config says:
    path = "../../target/release/libiggy_connector_postgres_source"

  runtime:
    resolve path
       ->
    dlopen library
       ->
    look for exported symbols:
       iggy_source_open
       iggy_source_handle
       iggy_source_close
       iggy_source_version

The runtime knows the names of those functions because the SDK macro
generates them.


========================================================================
9. WHAT THE SDK DEFINES
========================================================================

The SDK is the rulebook.

The core trait for a source is:

  Source
    open(&mut self)
    poll(&self)
    close(&mut self)

The important shared data structures are:

  ConnectorState
  ProducedMessage
  ProducedMessages
  Schema

Meaning:

  ConnectorState
    optional bytes the source can persist across restarts

  ProducedMessages
    one batch returned by poll()

  Schema
    tells the runtime how to interpret payload bytes
    (json, raw, text, proto, flatbuffer)


========================================================================
10. WHAT THE `source_connector!` MACRO DOES
========================================================================

This is one of the most important pieces.

When a source crate says:

  source_connector!(PostgresSource);

the macro generates the FFI bridge.

It effectively creates:

  iggy_source_open(...)
  iggy_source_handle(...)
  iggy_source_close(...)
  iggy_source_version()

and also stores connector instances in a static map keyed by plugin id.

ASCII:

  runtime (C-like FFI call)
      |
      v
  generated macro entrypoint
      |
      v
  SourceContainer<PostgresSource>
      |
      v
  PostgresSource::new(...)
  PostgresSource::open()
  PostgresSource::poll()
  PostgresSource::close()


========================================================================
11. HOW A SOURCE BATCH MOVES THROUGH THE SYSTEM
========================================================================

This is the full source path from Postgres DB to Iggy topic:

  +----------------------+
  | PostgreSQL database  |
  +----------------------+
             |
             v
  PostgresSource::poll_tables() or poll_cdc()
             |
             v
  Vec<ProducedMessage>
             |
             v
  ProducedMessages { schema, messages, state }
             |
             v
  SDK handle_messages() serializes batch with postcard
             |
             v
  runtime callback receives bytes
             |
             v
  runtime source_forwarding_loop()
             |
             +--> decode payload according to schema
             +--> apply transforms
             +--> encode for target stream schema
             +--> producer.send(...) to Iggy
             +--> save returned ConnectorState to state file
             |
             v
  Iggy stream/topic now contains the messages


========================================================================
12. THE CONCRETE POSTGRES SOURCE CRATE
========================================================================

File of interest:

  iggy/core/connectors/sources/postgres_source/src/lib.rs

Its job:

  "Read rows or change events from Postgres and turn them into Iggy
   messages."

It supports two broad modes:

  polling
    repeatedly query tables

  cdc
    read logical replication changes

It also supports multiple delivery styles:

  - JSON wrapper payloads (DatabaseRecord)
  - direct BYTEA passthrough
  - direct TEXT passthrough
  - direct JSONB passthrough
  - delete-after-read
  - mark-as-processed
  - stateful offset tracking


========================================================================
13. THE POSTGRES-SPECIFIC CONFIG MENTAL MODEL
========================================================================

The connector config has two halves:

  runtime-facing:
    type, key, path, streams, schema

  plugin-facing:
    connection_string, mode, tables, tracking_column, etc.

ASCII:

  config.toml

  +---------------------------------------------------------------+
  | type = "source"                                               |
  | key = "postgres"                                              |
  | path = "...libiggy_connector_postgres_source"                 |
  |                                                               |
  | [[streams]]                                                   |
  | stream = "user_events"                                        |
  | topic  = "users"                                              |
  | schema = "json"                                               |
  |                                                               |
  | [plugin_config]                                               |
  | connection_string = "postgresql://..."                        |
  | mode = "polling"                                              |
  | tables = ["users", "orders"]                                  |
  | tracking_column = "id"                                        |
  | poll_interval = "1s"                                          |
  +---------------------------------------------------------------+

Think of it as:

  top half    = "how runtime should wire this plugin"
  bottom half = "how plugin should talk to Postgres"


========================================================================
14. CODE ZOOM: TOP-LEVEL SHAPE OF `postgres_source/src/lib.rs`
========================================================================

At a glance, the file is shaped like this:

  imports
  source_connector!(PostgresSource)

  struct PostgresSource
  struct PostgresSourceConfig
  enum PayloadFormat
  struct State
  struct DatabaseRecord

  impl PostgresSource {
    new()
    serialize_state()
  }

  impl Source for PostgresSource {
    open()
    poll()
    close()
  }

  impl PostgresSource {
    connect()
    setup_cdc()
    poll_cdc()
    poll_cdc_builtin()
    poll_tables()
    mark_or_delete_processed_rows()
    get_pool()
    payload_format()
    get_max_retries()
    build_polling_query()
    validate_custom_query()
    substitute_query_params()
    parse_*_message()
    extract_payload_column()
    extract_column_value()
  }

  helper functions
  tests


========================================================================
15. LINE-BY-LINE / LINE-BAND WALKTHROUGH OF `postgres_source/src/lib.rs`
========================================================================

Note:
This is "line-by-line" in the code-reading sense:
small line bands, each with its local purpose.
It is more useful than pasting the whole 1409-line file.

----------------------------------------------------------------------
15.1  Lines 20-35
----------------------------------------------------------------------

Imports.

What they tell you immediately:

  async_trait        -> the Source trait methods are async
  humantime          -> config strings like "1s" become Duration
  iggy_connector_sdk -> shared connector types and the Source trait
  sqlx               -> database access
  tokio::Mutex       -> async-safe mutable state
  tracing            -> logs
  uuid               -> generate message ids

This import list already tells the story:

  "async Rust connector that talks to Postgres and emits Iggy messages"

----------------------------------------------------------------------
15.2  Line 36
----------------------------------------------------------------------

  source_connector!(PostgresSource);

This is the FFI bridge line.

Without this, the runtime cannot dynamically load and call the connector.
This one line exports the plugin shape the runtime expects.

----------------------------------------------------------------------
15.3  Lines 38-39
----------------------------------------------------------------------

Default retry policy constants:

  DEFAULT_MAX_RETRIES = 3
  DEFAULT_RETRY_DELAY = "1s"

These are runtime behavior defaults for transient DB errors.

----------------------------------------------------------------------
15.4  Lines 41-50
----------------------------------------------------------------------

Definition of the main connector struct:

  PostgresSource {
    id,
    pool,
    config,
    state,
    verbose,
    retry_delay,
    poll_interval,
  }

Mental model:

  id            = runtime-assigned instance id
  pool          = live Postgres connection pool
  config        = parsed plugin config
  state         = persisted offset/progress information
  verbose       = info vs debug logging choice
  retry_delay   = retry backoff base
  poll_interval = how often poll() waits before reading

----------------------------------------------------------------------
15.5  Lines 52-78
----------------------------------------------------------------------

Definition of PostgresSourceConfig.

This is the plugin-specific config contract.

The presence of these fields tells you the capabilities:

  mode                    -> polling or cdc
  tables                  -> multiple tables supported
  tracking_column         -> incremental polling
  initial_offset          -> start position
  custom_query            -> override query generation
  delete_after_read       -> destructive queue style
  processed_column        -> non-destructive ack style
  payload_column          -> direct payload extraction
  payload_format          -> raw / text / json-direct
  publication_name        -> logical replication
  replication_slot        -> logical replication state
  capture_operations      -> which CDC ops to keep

----------------------------------------------------------------------
15.6  Lines 80-97
----------------------------------------------------------------------

PayloadFormat enum plus parser from config string.

Meaning:

  Json       -> default wrapped JSON record
  Bytea      -> raw bytes
  Text       -> plain UTF-8 text
  JsonDirect -> use JSONB directly as payload

This is important because it decides what Schema the connector reports
back to the runtime later.

----------------------------------------------------------------------
15.7  Lines 100-105
----------------------------------------------------------------------

State struct.

This is what gets serialized into ConnectorState and written to disk:

  last_poll_time
  tracking_offsets per table
  processed_rows count

Very important:
state is connector-owned, not runtime-owned.
The runtime only stores opaque bytes.

----------------------------------------------------------------------
15.8  Lines 107-114
----------------------------------------------------------------------

DatabaseRecord struct.

This is the default JSON wrapper payload shape when the connector is not
extracting a direct payload column.

It carries:

  table_name
  operation_type
  timestamp
  data
  old_data

So the default source output is not "just row JSON";
it is row JSON plus metadata.

----------------------------------------------------------------------
15.9  Line 116
----------------------------------------------------------------------

  CONNECTOR_NAME = "PostgreSQL source"

Used mainly for logs and state serialization messages.

----------------------------------------------------------------------
15.10  Lines 118-156
----------------------------------------------------------------------

Constructor and state serializer.

`new()` does several things:

  - read verbose flag from config
  - try to deserialize old ConnectorState
  - log restored offsets if state exists
  - parse retry_delay
  - parse poll_interval
  - create fresh default state if no old state exists

Key insight:

  new() builds the object
  open() does the side effects

So construction is cheap and deterministic.
The real DB connection is delayed until open().

----------------------------------------------------------------------
15.11  Lines 159-198
----------------------------------------------------------------------

`impl Source for PostgresSource` starts here.

`open()`:

  1. log mode and tables
  2. call connect()
  3. if mode == cdc:
       setup CDC infrastructure
  4. if mode == polling:
       just log poll interval
  5. reject unknown mode

This is the "plugin startup handshake" the runtime triggers during
iggy_source_open.

----------------------------------------------------------------------
15.12  Lines 200-243
----------------------------------------------------------------------

`poll()`

This is the core heartbeat.

Sequence:

  1. sleep for poll_interval
  2. branch by mode
  3. get a Vec<ProducedMessage>
  4. inspect current state for logging
  5. choose Schema based on payload format
  6. serialize state to ConnectorState
  7. return ProducedMessages

Critical architectural point:

  poll() does not send to Iggy itself.

It only returns ProducedMessages.
The runtime does the actual send.

----------------------------------------------------------------------
15.13  Lines 245-259
----------------------------------------------------------------------

`close()`

Shutdown path:

  - close the SQLx pool if it exists
  - log final processed row count

Very standard resource cleanup.

----------------------------------------------------------------------
15.14  Lines 263-284
----------------------------------------------------------------------

`connect()`

This is the real DB connection setup:

  - decide max connection count
  - redact connection string for logs
  - build SQLx PgPool
  - run "SELECT 1" as connectivity test
  - store pool in self.pool

This means open() will fail early and loudly if DB config is wrong.

----------------------------------------------------------------------
15.15  Lines 286-339
----------------------------------------------------------------------

`setup_cdc()`

Only relevant when CDC mode is requested.

It:

  - checks wal_level
  - requires logical replication capability
  - creates publication if needed
  - creates logical replication slot if needed

This function is the "prepare Postgres so CDC can work" phase.

----------------------------------------------------------------------
15.16  Lines 341-363
----------------------------------------------------------------------

`poll_cdc()`

This is a tiny dispatcher.

It reads `cdc_backend` and chooses:

  builtin
  pg_replicate (feature-gated / not implemented here)
  error for anything else

Important design note:
the connector already anticipates multiple CDC engine backends.

----------------------------------------------------------------------
15.17  Lines 365-432
----------------------------------------------------------------------

`poll_cdc_builtin()`

This is the built-in CDC reader.

High-level flow:

  - call pg_logical_slot_get_changes(...)
  - loop over returned replication rows
  - parse textual change message
  - map accepted change into DatabaseRecord
  - serialize to JSON bytes
  - wrap as ProducedMessage
  - bump processed_rows state

This is "logical replication messages -> Iggy payloads".

----------------------------------------------------------------------
15.18  Lines 435-458
----------------------------------------------------------------------

Start of `poll_tables()`

It gathers:

  pool
  batch_size
  tracking column
  primary key column
  payload format
  payload column

Then it prepares temporary accumulators:

  state_updates
  total_processed

That is a clue the function is carefully minimizing lock hold time on
shared state.

----------------------------------------------------------------------
15.19  Lines 460-473
----------------------------------------------------------------------

For each table:

  - read last offset from state
  - choose custom query or generated query
  - execute query with retry logic

This is the top-level polling loop.

----------------------------------------------------------------------
15.20  Lines 475-518
----------------------------------------------------------------------

Row decoding loop.

For each SQL row:

  - track max offset seen
  - track processed primary keys
  - optionally extract payload column specially
  - otherwise build a JSON map of column name -> JSON value

This is where SQL rows are translated into connector-friendly data.

----------------------------------------------------------------------
15.21  Lines 520-555
----------------------------------------------------------------------

Payload construction.

Two possibilities:

  direct payload extraction path:
    use extracted bytes from payload column

  default wrapper path:
    build DatabaseRecord
    serialize to JSON bytes

Then each payload becomes a ProducedMessage with:

  uuid id
  timestamps
  payload bytes

This is the exact place where "row becomes outgoing message".

----------------------------------------------------------------------
15.22  Lines 558-587
----------------------------------------------------------------------

Post-row finalization for each table:

  - delete or mark processed rows if configured
  - queue offset update
  - log fetch count

After all tables:

  - take one lock on state
  - update processed_rows
  - update tracking_offsets
  - update last_poll_time

This is efficient because the function avoids holding the mutex while
doing database I/O.

----------------------------------------------------------------------
15.23  Lines 589-654
----------------------------------------------------------------------

`mark_or_delete_processed_rows()`

This is the "what should happen after successful processing?" policy.

Options:

  delete_after_read = true
    DELETE FROM table WHERE pk IN (...)

  processed_column is set
    UPDATE table SET processed_col = TRUE WHERE pk IN (...)

Important conceptual point:

  source connector can behave like:
    - a queue (delete rows)
    - an ack table (mark processed)
    - a pure reader (do neither)

----------------------------------------------------------------------
15.24  Lines 656-673
----------------------------------------------------------------------

Three small helpers:

  get_pool()
    fail if DB was not connected

  payload_format()
    decide effective output format

  get_max_retries()
    config or default

These are little policy accessors that keep bigger functions cleaner.

----------------------------------------------------------------------
15.25  Lines 675-718
----------------------------------------------------------------------

`build_polling_query()`

This is the default SQL query generator.

It builds:

  SELECT * FROM "table"
  WHERE "tracking_column" > offset
    AND "processed_column" = FALSE   (optional)
  ORDER BY "tracking_column" ASC
  LIMIT batch_size

This is the heart of incremental polling mode.

----------------------------------------------------------------------
15.26  Lines 720-751
----------------------------------------------------------------------

Custom query helpers:

  validate_custom_query()
    basic sanity checks

  substitute_query_params()
    replace:
      $table
      $offset
      $limit
      $now
      $now_unix

This allows the connector to be generic while still letting users write
domain-specific polling SQL.

----------------------------------------------------------------------
15.27  Lines 753-775
----------------------------------------------------------------------

`parse_logical_replication_message()`

This is the CDC dispatcher.

It ignores BEGIN/COMMIT and routes:

  INSERT: -> parse_insert_message()
  UPDATE: -> parse_update_message()
  DELETE: -> parse_delete_message()

Only operations present in `capture_operations` are kept.

----------------------------------------------------------------------
15.28  Lines 777-850
----------------------------------------------------------------------

`parse_insert_message()`, `parse_update_message()`,
`parse_delete_message()`

All three functions do roughly the same thing:

  - find table name inside textual replication message
  - parse key/value data part
  - build DatabaseRecord with op type

This is a light parser for Postgres logical replication text output.

----------------------------------------------------------------------
15.29  Lines 852-885
----------------------------------------------------------------------

`extract_payload_column()`

This powers the direct payload modes:

  Bytea      -> raw bytes
  Text       -> UTF-8 bytes
  JsonDirect -> serialize JSON value directly
  Json       -> fallback byte handling

This function is why the connector can act like:

  "copy this BYTEA blob straight into Iggy"

instead of always forcing wrapper JSON.

----------------------------------------------------------------------
15.30  Lines 887-960
----------------------------------------------------------------------

First half of `extract_column_value()`

Maps Postgres types to JSON values:

  BOOL
  INT2
  INT4
  INT8
  FLOAT4
  FLOAT8
  NUMERIC
  VARCHAR / TEXT / CHAR

This is the typed row-to-JSON translation layer for default wrapper mode.

----------------------------------------------------------------------
15.31  Lines 961-1005
----------------------------------------------------------------------

Second half of `extract_column_value()`

Handles:

  TIMESTAMP / TIMESTAMPTZ -> RFC3339 string
  UUID                    -> string
  JSON / JSONB            -> JSON object/value
  BYTEA                   -> base64 string
  everything else         -> string fallback

This is what makes the generic wrapper output practical across common
Postgres column types.

----------------------------------------------------------------------
15.32  Lines 1008-1049
----------------------------------------------------------------------

Helper functions:

  quote_identifier()
    safely quote table/column names

  format_offset_value()
    numbers stay unquoted, strings become SQL literals

  to_snake_case()
    optional output key normalization

These are small but important safety / ergonomics helpers.

----------------------------------------------------------------------
15.33  Lines 1051-1087
----------------------------------------------------------------------

`parse_record_data()`

This parses the textual key/value portion of logical replication change
messages and guesses primitive JSON types:

  integer
  float
  bool
  string

So this is the tiny parser that turns CDC text into structured JSON.

----------------------------------------------------------------------
15.34  Lines 1089-1127
----------------------------------------------------------------------

Retry helpers:

  with_retry(...)
  is_transient_error(...)

Behavior:

  - retry only transient SQLx/Postgres failures
  - stop on non-transient errors
  - backoff grows with attempt number

This keeps the polling source resilient to temporary DB glitches.

----------------------------------------------------------------------
15.35  Lines 1129-1138
----------------------------------------------------------------------

`redact_connection_string()`

Very small helper, but useful:
logs only a safe preview of the DB connection string.

Good example of "small operational polish" in connector code.

----------------------------------------------------------------------
15.36  Lines 1140-1171
----------------------------------------------------------------------

Start of tests module and `test_config()`.

This gives a reusable config fixture for unit tests.

Why that matters:
the unit tests are validating helper logic without needing a live DB.

----------------------------------------------------------------------
15.37  Lines 1173-1409
----------------------------------------------------------------------

Unit tests.

They validate:

  - polling query generation
  - processed-column filter insertion
  - numeric offset quoting rules
  - identifier escaping
  - CDC insert/update/delete parsing
  - custom query substitution
  - connection string redaction
  - state restore / fresh start / invalid state fallback
  - state serialization round-trip

This test section tells you what the author considered contractually
important:

  query correctness
  safe identifier handling
  CDC message parsing
  persistence correctness


========================================================================
16. HOW THE RUNTIME TOUCHES THIS FILE SPECIFICALLY
========================================================================

Concrete startup chain for this exact connector:

  runtime main()
    -> source::init()
      -> load connector library
      -> call iggy_source_open(...)
        -> macro-generated entrypoint
          -> SourceContainer::open(...)
            -> PostgresSource::new(...)
            -> PostgresSource::open(...)

Concrete poll chain:

  runtime source::handle()
    -> call iggy_source_handle(...)
      -> macro-generated entrypoint
        -> SourceContainer::handle(...)
          -> SDK handle_messages() loop
            -> PostgresSource::poll()
              -> poll_tables() or poll_cdc()
            -> callback(plugin_id, serialized ProducedMessages)
              -> runtime source_forwarding_loop()
                -> decode payloads
                -> apply transforms
                -> send to Iggy producer
                -> persist state file


========================================================================
17. WHAT THE INTEGRATION TESTS PROVE
========================================================================

The integration test file for the source connector checks six very
practical behaviors:

  1. JSON row mode works
  2. BYTEA payload passthrough works
  3. JSONB direct payload mode works
  4. delete_after_read removes source rows
  5. processed_column marks rows instead of deleting
  6. state survives connector restart

ASCII summary:

  +----------------------------+-------------------------------+
  | test                       | what it proves                |
  +----------------------------+-------------------------------+
  | json_rows_source...        | generic wrapper JSON path     |
  | bytea_rows_source...       | raw bytes path                |
  | jsonb_rows_source...       | direct JSON path              |
  | delete_after_read...       | destructive queue semantics   |
  | processed_column...        | ack column semantics          |
  | state_persists...          | resume after restart          |
  +----------------------------+-------------------------------+


========================================================================
18. THE SIMPLEST POSSIBLE KID-SAFE SUMMARY
========================================================================

If you had to explain this to a smart 10-year-old:

  - Iggy is a super-fast message warehouse.
  - A source connector is a robot that brings stuff into the warehouse.
  - The Postgres source robot reads rows from a Postgres database.
  - Sometimes it reads by polling tables.
  - Sometimes it reads change events from Postgres replication.
  - It packs what it found into message boxes.
  - It hands the boxes to the runtime.
  - The runtime puts the boxes onto the right Iggy shelf
    (stream/topic).
  - The robot also keeps a notebook of "where I stopped last time"
    so it can continue after a restart.


========================================================================
19. BEST READING ORDER IF YOU WANT TO GO DEEPER
========================================================================

Read in this order:

  1. iggy/README.md
  2. iggy/core/connectors/README.md
  3. iggy/core/connectors/runtime/src/main.rs
  4. iggy/core/connectors/sdk/src/lib.rs
  5. iggy/core/connectors/sdk/src/source.rs
  6. iggy/core/connectors/runtime/src/source.rs
  7. iggy/core/connectors/sources/postgres_source/config.toml
  8. iggy/core/connectors/sources/postgres_source/src/lib.rs
  9. iggy/core/integration/tests/connectors/postgres/postgres_source.rs


========================================================================
20. ONE-SCREEN CHEAT SHEET
========================================================================

  OUTSIDE WORLD
     |
     v
  Postgres tables / WAL
     |
     v
  PostgresSource::poll_*()
     |
     v
  ProducedMessages { schema, messages, state }
     |
     v
  SDK FFI callback bridge
     |
     v
  runtime source_forwarding_loop()
     |
     +--> decode
     +--> transform
     +--> encode
     +--> send to Iggy
     +--> save state
     |
     v
  Iggy stream/topic

One sentence:

  `postgres_source/src/lib.rs` is the Postgres-reading brain;
  the SDK macro is the plugin socket;
  the runtime is the traffic controller that gets those records into
  Iggy safely and repeatedly.
```
