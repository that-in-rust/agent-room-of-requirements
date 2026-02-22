# Learn Rust by Reading the MongoDB Connector

## TL;DR (Bottom Line Up Front)

22 files. 3,801 lines. Two plugins + their tests. Here's the mental model:

```
  ┌─────────────────────────────────────────────────────────────┐
  │  You wrote TWO shared libraries (.dylib/.so) that the      │
  │  Iggy runtime hot-loads at startup via dlopen.              │
  │                                                             │
  │  SINK:   Iggy messages ──▶ MongoDB documents                │
  │  SOURCE: MongoDB documents ──▶ Iggy messages                │
  │                                                             │
  │  Each is ONE Rust file implementing ONE trait (interface).   │
  │  The macro generates all the FFI glue.                      │
  │  The tests spin up REAL MongoDB containers via Docker.      │
  └─────────────────────────────────────────────────────────────┘
```

Everything below teaches the Rust you need to read and modify this code.

---

## The 22 Files at a Glance

```
  THE DIFF (3,801 lines)
  ══════════════════════

  PLUMBING (3 files, ~350 lines)
  ├── Cargo.toml (root)  ─── 2 lines: register new crates in workspace
  ├── Cargo.lock          ─── auto-generated dependency lockfile
  └── integration/Cargo.toml ─ 1 line: add mongodb driver for tests

  SINK CONNECTOR (4 files, ~790 lines)
  ├── mongodb_sink/Cargo.toml  ─── dependency list
  ├── mongodb_sink/config.toml ─── default user config
  ├── mongodb_sink/README.md   ─── usage docs
  └── mongodb_sink/src/lib.rs  ─── ★ ALL sink code + 19 unit tests

  SOURCE CONNECTOR (4 files, ~1,245 lines)
  ├── mongodb_source/Cargo.toml
  ├── mongodb_source/config.toml
  ├── mongodb_source/README.md
  └── mongodb_source/src/lib.rs ─── ★ ALL source code + 33 unit tests

  E2E TESTS (11 files, ~1,416 lines)
  ├── fixtures/mongodb/
  │   ├── container.rs  ─── Docker container + env var constants
  │   ├── sink.rs       ─── 4 fixture structs (Json, Binary, Batch, AutoCreate)
  │   ├── source.rs     ─── 3 fixture structs (Default, Delete, Mark)
  │   └── mod.rs
  ├── mongodb/
  │   ├── mongodb_sink.rs   ─── 4 E2E sink tests
  │   ├── mongodb_source.rs ─── 4 E2E source tests
  │   ├── sink.toml         ─── connector config for test runtime
  │   ├── source.toml
  │   └── mod.rs
  └── (2 mod.rs files wiring modules together)
```

---

## Part 1: Root Cargo.toml — 2 Lines That Matter

```toml
[workspace]
members = [
    # ... 30+ existing crates ...
    "core/connectors/sinks/mongodb_sink",        # ← NEW
    "core/connectors/sources/mongodb_source",    # ← NEW
]
```

```
  Cargo.toml = Rust's package.json
  workspace  = mono-repo: one root file lists all sub-projects ("crates")

  Without these 2 lines, Cargo doesn't know our code exists.
  That's the entire change to the root file.
```

---

## Part 2: Crate Cargo.toml — The Shopping List

```toml
# mongodb_sink/Cargo.toml

[package]
name = "iggy_connector_mongodb_sink"
version = "0.3.0"
edition = "2024"

[lib]
crate-type = ["cdylib", "lib"]     # ← THE KEY LINE

[dependencies]
iggy_connector_sdk = { workspace = true }
mongodb = { version = "3.0", features = ["rustls-tls"] }
serde = { workspace = true }
tokio = { workspace = true }
# ... etc
```

```
  ┌─────────────────────────────────────────────────┐
  │  crate-type = ["cdylib", "lib"]                 │
  │                                                 │
  │  "cdylib" = compile to .so/.dylib (shared lib)  │
  │             The Iggy runtime loads this via      │
  │             dlopen at startup. It's a PLUGIN.    │
  │                                                 │
  │  "lib"    = normal Rust library                  │
  │             Used by unit tests and other crates  │
  │                                                 │
  │  { workspace = true } = "use the version the    │
  │   root Cargo.toml declared." No copy-paste drift.│
  └─────────────────────────────────────────────────┘
```

---

## Part 3: config.toml — How Config Becomes Your Struct

```toml
# mongodb_sink/config.toml

type = "sink"
key = "mongodb"
path = "../../target/release/libiggy_connector_mongodb_sink"

[[streams]]                              # ← double brackets = array of tables
stream = "user_events"
topics = ["users", "orders"]
schema = "json"

[plugin_config]                          # ← THIS SECTION becomes YOUR struct
connection_uri = "mongodb://localhost:27017"
database = "iggy_messages"
collection = "messages"
batch_size = 100
```

```
  config.toml                         Your Rust struct
  ┌──────────────────┐                ┌──────────────────────┐
  │ [plugin_config]  │   TOML parse   │ MongoDbSinkConfig {  │
  │ connection_uri = │──────────────▶ │   connection_uri:    │
  │   "mongodb://..."│   → JSON       │     String,          │
  │ database = "iggy"│   → FFI        │   database: String,  │
  │ batch_size = 100 │   → serde      │   batch_size:        │
  └──────────────────┘                │     Option<u32>,     │
                                      └──────────────────────┘

  The runtime reads TOML, converts [plugin_config] to JSON,
  passes it through FFI, and serde auto-deserializes it.
  You never parse TOML yourself.
```

---

## Part 4: Sink lib.rs — The Heart of Everything

### 4A. The Macro — One Line, ~100 Lines Generated

```rust
sink_connector!(MongoDbSink);
```

```
  This generates:
  • extern "C" fn open()    → creates MongoDbSink, calls .open()
  • extern "C" fn consume() → finds instance, calls .consume()
  • extern "C" fn close()   → calls .close(), drops instance
  • A static HashMap to store instances by ID

  The ! means MACRO — it writes code for you at compile time.
  Think of it as a code template. You never see the output.
```

### 4B. The Struct — Your Data Container

```rust
#[derive(Debug)]
pub struct MongoDbSink {
    pub id: u32,                          // public field
    client: Option<Client>,               // private, nullable
    config: MongoDbSinkConfig,            // private, owned
    state: Mutex<State>,                  // private, locked
    verbose: bool,
    retry_delay: Duration,
}
```

Every new Rust concept in one struct:

```
  #[derive(Debug)]       Attribute (decorator). Auto-generates
  │                      println!("{:?}", sink) support.
  │
  pub                    Public (like export). Without it = private.
  │
  Option<Client>         Rust's "nullable". Either Some(client) or None.
  │                      Rust FORCES you to handle the None case.
  │                      .unwrap_or(default) = "use value or default"
  │
  Mutex<State>           Lock for shared mutable state. Only ONE
                         piece of code can access State at a time.
                         WHY? Because consume() takes &self (shared
                         ref) so multiple calls can happen at once.

  ┌──────────────────────────────────────────┐
  │  RUST TYPE QUICK REFERENCE               │
  │                                          │
  │  u32       unsigned 32-bit integer       │
  │  i64       signed 64-bit integer         │
  │  f64       floating point (like JS num)  │
  │  bool      true / false                  │
  │  String    owned text (heap-allocated)   │
  │  &str      borrowed text (read-only ref) │
  │  Vec<T>    growable array                │
  │  Option<T> Some(value) or None           │
  │  Result<T,E> Ok(value) or Err(error)     │
  └──────────────────────────────────────────┘
```

### 4C. The Config Struct — Why Everything Is Option

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MongoDbSinkConfig {
    pub connection_uri: String,           // REQUIRED — no Option
    pub database: String,                 // REQUIRED
    pub collection: String,               // REQUIRED
    pub batch_size: Option<u32>,          // optional — has default
    pub max_pool_size: Option<u32>,
    pub include_metadata: Option<bool>,
    pub payload_format: Option<String>,
    pub max_retries: Option<u32>,
    pub retry_delay: Option<String>,
    // ...
}
```

```
  WHY Option<...> on most fields?

  Because the user's config might not include every field:

    [plugin_config]
    connection_uri = "mongodb://localhost"
    database = "mydb"
    # batch_size not specified!

  serde sets batch_size = None.
  Your code: config.batch_size.unwrap_or(100)
  → "use 100 if not specified"

  Required fields (String, not Option<String>) will
  cause a parse error if missing → connector won't start.
```

### 4D. The Trait Implementation — The Contract

```rust
#[async_trait]
impl Sink for MongoDbSink {
    async fn open(&mut self) -> Result<(), Error> {
        self.connect().await?;
        if self.config.auto_create_collection.unwrap_or(false) {
            self.ensure_collection_exists().await?;
        }
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
        self.client.take();    // drop the client
        Ok(())
    }
}
```

The five things to understand here:

```
  ┌─────────────────────────────────────────────────────┐
  │  1. impl Sink for MongoDbSink                       │
  │     "MongoDbSink satisfies the Sink interface"      │
  │     Like `class MongoDbSink implements Sink` in Java│
  │                                                     │
  │  2. &mut self vs &self                              │
  │     open()    → &mut self → can modify fields       │
  │     consume() → &self     → read-only access        │
  │     close()   → &mut self → can modify fields       │
  │                                                     │
  │     consume() gets &self because the runtime may    │
  │     call it from multiple tasks simultaneously.     │
  │     That's why you need Mutex for mutable state.    │
  │                                                     │
  │  3. Result<(), Error>                               │
  │     Either Ok(()) = success (nothing to return)     │
  │     Or     Err(e) = failure (with error value)      │
  │     No exceptions. No try/catch.                    │
  │                                                     │
  │  4. The ? operator                                  │
  │     self.connect().await?                           │
  │                        ^                            │
  │     "If this fails, return the error immediately."  │
  │     Shorthand for:                                  │
  │       match self.connect().await {                  │
  │           Ok(v)  => v,                              │
  │           Err(e) => return Err(e),                  │
  │       }                                             │
  │     You'll see ? EVERYWHERE. It replaces try/catch. │
  │                                                     │
  │  5. Ok(()) = return success with no value           │
  │     () is the "unit type" — like void.              │
  │     No semicolon = this is the return value.        │
  └─────────────────────────────────────────────────────┘
```

### 4E. The connect() Method — Ownership and References

```rust
async fn connect(&mut self) -> Result<(), Error> {
    let mut options = ClientOptions::parse(&self.config.connection_uri)
        .await
        .map_err(|e| Error::InitError(format!("Failed to parse URI: {e}")))?;

    if let Some(pool_size) = self.config.max_pool_size {
        options.max_pool_size = Some(pool_size);
    }

    let client = Client::with_options(options)
        .map_err(|e| Error::InitError(format!("Failed to create client: {e}")))?;

    self.client = Some(client);
    Ok(())
}
```

```
  &self.config.connection_uri
  ^
  BORROW — parse() just reads the string, doesn't take ownership.

  if let Some(pool_size) = self.config.max_pool_size {
  ^^^^^^^^^^^^^^^^^^^^
  PATTERN MATCH in an if. "If this Option is Some, bind the
  inner value to pool_size and run the block."

  .map_err(|e| Error::InitError(format!("...")))
           ^^^
  CLOSURE (anonymous function). |e| = parameter.
  Like JavaScript: (e) => new InitError(`...${e}`)

  format!("Failed: {e}")
  Like JS template literals: `Failed: ${e}`
  But it's a macro (!) not a function.

  self.client = Some(client);
  The client value MOVES into self.client.
  After this line, the local `client` variable is gone.
  This is OWNERSHIP — Rust's #1 unique feature.
```

### 4F. The Retry Loop — Practical Error Handling

```rust
async fn insert_batch_with_retry(&self, ...) -> Result<(), Error> {
    let max_retries = self.get_max_retries();
    let mut attempts = 0u32;             // mut = mutable. 0u32 = typed literal.

    loop {                               // infinite loop, exit with return/break
        match collection.insert_many(docs.to_vec()).await {
            Ok(_) => return Ok(()),      // success → exit function
            Err(e) => {
                attempts += 1;
                if attempts >= max_retries {
                    return Err(Error::CannotStoreData(format!("...")));
                }
                tokio::time::sleep(retry_delay * attempts).await;
            }
        }
    }
}
```

```
  match = switch on steroids
  • Compiler checks you handle ALL cases
  • No fallthrough (no break needed)
  • Can destructure values: Ok(_), Err(e)

  loop { } = infinite loop. Exit with return or break.

  let mut attempts = 0u32;
      ^^^            ^^^
      mutable        "the number 0, typed as u32"
      (without mut,  Rust needs exact integer types.
       attempts += 1
       would fail!)
```

### 4G. The Payload Match — Enum (Tagged Union)

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub enum PayloadFormat {
    #[default]
    Binary,
    Json,
    String,
}
```

```
  enum in Rust ≠ enum in Java/C.
  It's a TAGGED UNION: a value that is ONE OF several variants.

  In TypeScript: type PayloadFormat = "binary" | "json" | "string"

  The match on it:

  match payload_format {
      PayloadFormat::Binary => {
          doc.insert("payload", bson::Binary { ... });
      }
      PayloadFormat::Json => {
          let json: serde_json::Value = serde_json::from_slice(&bytes)?;
          let bson = bson::to_bson(&json)?;
          doc.insert("payload", bson);
      }
      PayloadFormat::String => {
          let text = String::from_utf8(bytes)?;
          doc.insert("payload", text);
      }
  }

  match MUST be exhaustive — miss a variant → compiler error.
```

---

## Part 5: Source lib.rs — What's Different

Same architecture, three key differences:

### 5A. Constructor Takes Persisted State

```rust
pub fn new(id: u32, config: MongoDbSourceConfig, state: Option<ConnectorState>) -> Self {
    let initial_state = state
        .and_then(|s| s.deserialize(CONNECTOR_NAME, id))  // restore from disk
        .unwrap_or_else(|| State { ... });                 // or start fresh
```

```
  .and_then() on Option:
    None.and_then(f)    → None          (skip entirely)
    Some(x).and_then(f) → f(x)         (which returns another Option)

  This is how the source resumes after restart:
  ┌─────────────────────────────────────────────────┐
  │  poll() runs → returns state bytes → saved to   │
  │  disk → connector restarts → new() receives     │
  │  state bytes → deserialize → "I was at doc #47, │
  │  continue from #48"                             │
  └─────────────────────────────────────────────────┘
```

### 5B. poll() Returns Data (Instead of Consuming It)

```rust
async fn poll(&self) -> Result<ProducedMessages, Error> {
    tokio::time::sleep(self.poll_interval).await;
    let messages = self.poll_collection().await?;

    Ok(ProducedMessages {
        schema: payload_format.to_schema(),
        messages,                          // Vec<ProducedMessage>
        state: self.serialize_state(&state), // save offsets for restart
    })
}
```

```
  SINK:   receives ConsumedMessage (rich enum, pre-decoded)
          → .clone().try_into_vec() → Vec<u8> → insert into MongoDB

  SOURCE: builds ProducedMessage (raw bytes, you serialize)
          → serde_json::to_vec(&doc) → Vec<u8> → send to Iggy

  ┌────────────────┐          ┌────────────────┐
  │  SINK unpacks   │          │  SOURCE packs   │
  │  a gift box    │          │  a cardboard box│
  └────────────────┘          └────────────────┘
```

### 5C. The BSON Type Mismatch Bug (Real Bug We Found)

```rust
// delete_processed_documents() and mark_documents_processed()
// BEFORE (broken):
let delete_filter = doc! {tracking_field: {"$lte": &offset}};
// offset is String "3" but MongoDB field is Int64(3)
// MongoDB does NOT coerce types → 0 documents match!

// AFTER (fixed):
if let Ok(n) = offset.parse::<i64>() {
    doc! {tracking_field: {"$lte": n}}      // compare as number
} else {
    doc! {tracking_field: {"$lte": &offset}} // compare as string
}
```

```
  This was caught by the E2E tests, not unit tests.
  Unit tests mock the data. E2E tests hit real MongoDB.
  Real MongoDB has real type rules.
```

---

## Part 6: E2E Tests — The Trust Signal (Cursory)

### How the test harness works:

```
  #[iggy_harness(
      server(connectors_runtime(config_path = "tests/connectors/mongodb/sink.toml")),
      seed = seeds::connector_stream
  )]
  async fn my_test(harness: &TestHarness, fixture: MongoDbSinkJsonFixture) {

  What this macro does:
  ┌──────────────────────────────────────────────────────┐
  │  1. Start iggy-server binary                         │
  │  2. Start iggy-connectors binary with sink.toml      │
  │  3. Create stream + topic (the "seed")               │
  │  4. Call MongoDbSinkJsonFixture::setup()              │
  │     → spins up Docker MongoDB container              │
  │     → returns fixture with connection_uri             │
  │  5. Override connector env vars with fixture's        │
  │     connection_uri (so connector talks to test DB)   │
  │  6. Call your test function                           │
  │  7. Tear everything down                             │
  └──────────────────────────────────────────────────────┘
```

### The fixture pattern:

```rust
pub struct MongoDbSinkJsonFixture {
    inner: MongoDbSinkFixture,     // composition, not inheritance
}

impl std::ops::Deref for MongoDbSinkJsonFixture {
    type Target = MongoDbSinkFixture;
    fn deref(&self) -> &Self::Target { &self.inner }
}
// Deref lets you call inner's methods directly:
// fixture.wait_for_documents(...)  ← calls inner.wait_for_documents()
```

```
  Deref = Rust's answer to inheritance for method delegation.
  "When someone calls a method on me that I don't have,
   delegate to my inner field."
```

### The 8 tests in ASCII:

```
  SINK (4 tests)
  ══════════════

  json_messages_sink_to_mongodb
  ┌──────────┐    ┌──────┐    ┌─────────┐
  │ 3 JSON   │───▶│ Iggy │───▶│ MongoDB │  assert: payload is BSON Document
  │ messages │    │ Sink │    │ .find() │  assert: offsets 0,1,2 contiguous
  └──────────┘    └──────┘    └─────────┘  assert: metadata fields present

  binary_messages_sink_as_bson_binary
  ┌──────────┐    ┌──────┐    ┌─────────┐
  │ raw bytes│───▶│ Iggy │───▶│ MongoDB │  assert: payload is Bson::Binary
  │ 0xDEADBEEF    │ Sink │    │ .find() │  assert: subtype = Generic
  └──────────┘    └──────┘    └─────────┘  assert: bytes match exactly

  large_batch_processed_correctly
  ┌──────────┐    ┌──────┐    ┌─────────┐
  │ 50 msgs  │───▶│batch │───▶│ MongoDB │  assert: 50 docs (no loss)
  │ size=10  │    │=10   │    │ .find() │  assert: offsets 0..49 contiguous
  └──────────┘    └──────┘    └─────────┘

  auto_create_collection_on_open
  ┌──────────┐    ┌──────┐    ┌─────────┐
  │ no msgs  │    │ Iggy │    │ MongoDB │  assert: collection EXISTS
  │ sent     │    │ open │    │ .list() │  assert: 0 documents
  └──────────┘    └──────┘    └─────────┘


  SOURCE (4 tests)
  ════════════════

  source_polls_documents_to_iggy
  ┌─────────┐    ┌──────┐    ┌──────────┐
  │ MongoDB │───▶│ Iggy │───▶│ Iggy     │  assert: 3 messages received
  │ 3 docs  │    │Source│    │ stream   │  assert: seq order preserved
  └─────────┘    └──────┘    └──────────┘

  delete_after_read_removes_documents
  ┌─────────┐    ┌──────┐    ┌──────────┐
  │ MongoDB │───▶│ Iggy │───▶│ MongoDB  │  assert: messages in Iggy
  │ 3 docs  │    │Source│    │ count: 0 │  assert: 0 docs remain
  └─────────┘    └──────┘    └──────────┘

  mark_processed_sets_field
  ┌─────────┐    ┌──────┐    ┌──────────┐
  │ MongoDB │───▶│ Iggy │───▶│ MongoDB  │  assert: messages in Iggy
  │ 3 docs  │    │Source│    │processed │  assert: is_processed = true
  │ is_p=F  │    │      │    │ = true   │  assert: doc count unchanged
  └─────────┘    └──────┘    └──────────┘

  state_persists_across_connector_restart
  ┌─────────┐    ┌──────┐    ┌──────────┐
  │ batch 1 │───▶│STOP  │    │          │
  │ batch 2 │    │RESTART───▶│ Iggy     │  assert: only batch 2 received
  │ (while  │    │      │    │ stream   │  assert: all seq > batch_1_max
  │  down)  │    └──────┘    └──────────┘  (no duplicates from batch 1)
  └─────────┘
```

### The polling pattern (used in every test):

```rust
for _ in 0..POLL_ATTEMPTS {           // 100 attempts
    // check if expected state is reached
    if done { break; }
    sleep(Duration::from_millis(50)).await;  // 50ms between polls
}
assert!(done, "timeout message");

// This is "deadline-based polling" — the standard async
// verification pattern across Kafka, Debezium, and Flink.
```

---

## Syntax Cheat Sheet

```
  ┌──────────────────┬────────────────────────────────────┐
  │  RUST             │  WHAT IT MEANS                    │
  ├──────────────────┼────────────────────────────────────┤
  │  let x = 5;      │  immutable variable                │
  │  let mut x = 5;  │  mutable variable                  │
  │  fn foo() -> T   │  function returning T              │
  │  &self           │  read-only method (shared access)  │
  │  &mut self       │  read-write method (exclusive)     │
  │  &x              │  borrow (read-only reference)      │
  │  *x              │  dereference (reach inside ref)    │
  │  x.clone()       │  deep copy                         │
  │  pub             │  public (like export)              │
  │  struct { }      │  data type                         │
  │  enum { A, B }   │  tagged union                      │
  │  impl Foo { }    │  add methods to Foo                │
  │  impl T for Foo  │  implement interface T             │
  │  use x::y;       │  import                            │
  │  x as y          │  type cast or rename               │
  │  ::              │  path separator (like . in JS)     │
  │  macro!()        │  invoke a macro                    │
  │  #[derive(...)]  │  auto-implement traits             │
  │  Result<T, E>    │  Ok(T) or Err(E)                   │
  │  Option<T>       │  Some(T) or None                   │
  │  ?               │  unwrap-or-return-error            │
  │  .unwrap_or(v)   │  use value or default              │
  │  .map(|x| ...)   │  transform inner value             │
  │  .map_err(|e|..) │  transform error                   │
  │  .await          │  wait for async result             │
  │  match x { }     │  pattern match (switch on steroids)│
  │  if let Some(x)  │  conditional pattern match         │
  │  loop { }        │  infinite loop                     │
  │  for x in iter   │  for-each loop                     │
  │  format!("{x}")  │  string interpolation              │
  │  doc! { }        │  BSON document literal (macro)     │
  │  no semicolon    │  = return this expression          │
  │  semicolon       │  = statement, don't return         │
  └──────────────────┴────────────────────────────────────┘
```

---

## The Full Data Flow

```
  ┌───────────┐                                    ┌───────────┐
  │  SOURCE   │                                    │   SINK    │
  │           │                                    │           │
  │ new()     │← config + persisted state          │ new()     │← config
  │   │       │                                    │   │       │
  │ open()    │← connect to MongoDB                │ open()    │← connect, auto-create
  │   │       │                                    │   │       │
  │ poll()    │← called in loop by runtime         │consume()  │← called when msgs arrive
  │  │        │                                    │  │        │
  │  ├─ sleep(poll_interval)                       │  ├─ for batch in messages.chunks()
  │  ├─ build filter (tracking_field > offset)     │  ├─ for msg in batch:
  │  ├─ collection.find(filter).await              │  │    ├─ build BSON Document
  │  ├─ for doc in cursor:                         │  │    ├─ add metadata fields
  │  │    ├─ extract timestamp from ObjectId       │  │    └─ match payload_format
  │  │    ├─ inject _iggy metadata if enabled      │  ├─ insert_many with retry
  │  │    └─ serialize to ProducedMessage           │  └─ update state counters
  │  ├─ update tracking offset                     │           │
  │  ├─ delete or mark-processed if configured     │ close()   │← drop client
  │  └─ return ProducedMessages { state }          └───────────┘
  │   │       │
  │   ▼       │
  │  ═══ IGGY STREAM ════════════════════════▶
  │           │
  │ close()   │← drop client, log stats
  └───────────┘
```
