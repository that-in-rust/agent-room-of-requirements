Here I am 

Doubting my own abilities in iggy



Now let me tell you the story:                                                                                                                                                             
``` text                                        
  ---                                                                                                                                                                                        
  The Story of Your MongoDB Connector                                                                                                                                                      
                                                                                                                                                                                             
  Act 1: The World You're Entering                                                                                                                                                           
                                                                                                                                                                                             
  What is Iggy?

  Imagine a river of messages flowing through a system:

  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │   Producer   │────►│    IGGY      │────►│   Consumer   │
  │  (sends msg) │     │  (the river) │     │ (gets msg)   │
  └──────────────┘     └──────────────┘     └──────────────┘

  Iggy is a message streaming system (like Kafka, but simpler). It:
  - Receives messages from producers
  - Stores them in streams → topics → partitions
  - Delivers them to consumers

  Stream: "user_events"
      │
      ├── Topic: "logins"
      │       ├── Partition 0: [msg1, msg2, msg3, ...]
      │       └── Partition 1: [msg4, msg5, msg6, ...]
      │
      └── Topic: "purchases"
              └── Partition 0: [msg7, msg8, ...]

  What is MongoDB?

  MongoDB is a document database. Instead of tables with rows, it has collections with documents:

  Collection: "messages"
      │
      ├── Document: { "_id": 1, "payload": "hello", "timestamp": "2024-01-01" }
      ├── Document: { "_id": 2, "payload": "world", "timestamp": "2024-01-02" }
      └── Document: { "_id": 3, "payload": { "name": "Alice" }, "tags": ["a", "b"] }

  What is BSON?

  BSON = Binary JSON. It's MongoDB's internal format.

  JSON (what humans read):        BSON (what MongoDB stores):
  {                               [binary data]
    "name": "Alice",              - More types (Date, Binary, ObjectId)
    "age": 30                     - Faster to parse
  }                               - Includes field lengths

  Why care? When you send data to MongoDB, you're building BSON documents, not JSON strings.

  ---
  Act 2: The Job (What You Built)

  Your connector is a bridge between Iggy and MongoDB:

                           YOUR CODE
                      ┌─────────────────┐
                      │                 │
     Iggy Stream  ───►│  MongoDB Sink   │───► MongoDB Collection
                      │                 │
     Iggy Stream  ◄───│ MongoDB Source  │◄─── MongoDB Collection
                      │                 │
                      └─────────────────┘

  Two Directions, One Pattern

  ┌────────────────────────────────┬───────────────────────────────┐
  │              Sink              │            Source             │
  ├────────────────────────────────┼───────────────────────────────┤
  │ Iggy → MongoDB                 │ MongoDB → Iggy                │
  ├────────────────────────────────┼───────────────────────────────┤
  │ Reads messages FROM Iggy       │ Reads documents FROM MongoDB  │
  ├────────────────────────────────┼───────────────────────────────┤
  │ Writes documents TO MongoDB    │ Writes messages TO Iggy       │
  ├────────────────────────────────┼───────────────────────────────┤
  │ "I consume what Iggy gives me" │ "I poll MongoDB for new data" │
  └────────────────────────────────┴───────────────────────────────┘

  ---
  Act 3: The Code - Sink Edition

  Let's walk through mongodb_sink/src/lib.rs line by line.

  Scene 1: The Imports (Lines 19-29)

  use async_trait::async_trait;
  use humantime::Duration as HumanDuration;
  use iggy_connector_sdk::{
      ConsumedMessage, Error, MessagesMetadata, Sink, TopicMetadata, sink_connector,
  };
  use mongodb::{Client, Collection, bson, options::ClientOptions};
  use serde::{Deserialize, Serialize};
  use std::str::FromStr;
  use std::time::Duration;
  use tokio::sync::Mutex;
  use tracing::{debug, error, info, warn};

  Translation:
  - async_trait - Lets you use async in traits (Rust doesn't natively support this yet)
  - humantime - Parses human-readable durations like "1s" or "5m"
  - iggy_connector_sdk - The SDK (your contract with Iggy)
    - Sink - The trait you MUST implement
    - ConsumedMessage - A message from Iggy
    - sink_connector! - A macro that registers your connector
  - mongodb - The official MongoDB driver
    - Client - Your connection to MongoDB
    - bson - Types for building MongoDB documents
  - serde - Serialization (JSON ↔ Rust structs)
  - tokio::sync::Mutex - Thread-safe mutable state
  - tracing - Logging (info!, warn!, error!, debug!)

  Scene 2: The Macro (Line 31)

  sink_connector!(MongoDbSink);

  What it does: This macro generates boilerplate code that:
  1. Exports your connector as a C-compatible library
  2. Registers it with Iggy's plugin system
  3. Creates the create_connector() function that Iggy calls

  Think of it as: "Hello Iggy, I exist! My name is MongoDbSink."

  Scene 3: Constants (Lines 33-34)

  const DEFAULT_MAX_RETRIES: u32 = 3;
  const DEFAULT_RETRY_DELAY: &str = "1s";

  Rust syntax:
  - const - Compile-time constant (baked into the binary)
  - u32 - Unsigned 32-bit integer (0 to 4 billion)
  - &str - A string slice (reference to text, doesn't own the data)

  Scene 4: The Main Struct (Lines 36-44)

  #[derive(Debug)]
  pub struct MongoDbSink {
      pub id: u32,
      client: Option<Client>,
      config: MongoDbSinkConfig,
      state: Mutex<State>,
      verbose: bool,
      retry_delay: Duration,
  }

  Rust syntax explained:

  ┌────────────────────────┬───────────────────────────────────────────────────────────────────────┐
  │         Piece          │                                Meaning                                │
  ├────────────────────────┼───────────────────────────────────────────────────────────────────────┤
  │ #[derive(Debug)]       │ Auto-generates Debug trait (lets you print the struct with {:?})      │
  ├────────────────────────┼───────────────────────────────────────────────────────────────────────┤
  │ pub struct             │ Public struct (visible outside this file)                             │
  ├────────────────────────┼───────────────────────────────────────────────────────────────────────┤
  │ pub id: u32            │ Public field named id of type unsigned 32-bit int                     │
  ├────────────────────────┼───────────────────────────────────────────────────────────────────────┤
  │ client: Option<Client> │ Either Some(Client) or None (nullable)                                │
  ├────────────────────────┼───────────────────────────────────────────────────────────────────────┤
  │ Mutex<State>           │ Thread-safe wrapper around State (only one task can access at a time) │
  └────────────────────────┴───────────────────────────────────────────────────────────────────────┘

  Why Option<Client>?

  Before open() is called:    client = None     (not connected yet)
  After open() succeeds:      client = Some(Client)  (connected!)

  Why Mutex<State>?

  Multiple async tasks might try to update state simultaneously. Mutex ensures only one accesses it at a time:

  Task 1: lock state ────► update counter ────► unlock
  Task 2:                    (waits)          ────► lock ────► update

  Scene 5: The Config Struct (Lines 46-61)

  #[derive(Debug, Clone, Serialize, Deserialize)]
  pub struct MongoDbSinkConfig {
      pub connection_uri: String,
      pub database: String,
      pub collection: String,
      pub max_pool_size: Option<u32>,
      pub auto_create_collection: Option<bool>,
      pub batch_size: Option<u32>,
      pub include_metadata: Option<bool>,
      pub include_checksum: Option<bool>,
      pub include_origin_timestamp: Option<bool>,
      pub payload_format: Option<String>,
      pub verbose_logging: Option<bool>,
      pub max_retries: Option<u32>,
      pub retry_delay: Option<String>,
  }

  Rust syntax:

  ┌─────────────┬─────────────────────────────────────────────┐
  │    Piece    │                   Meaning                   │
  ├─────────────┼─────────────────────────────────────────────┤
  │ Clone       │ Lets you make copies with .clone()          │
  ├─────────────┼─────────────────────────────────────────────┤
  │ Serialize   │ Lets you convert TO JSON/TOML               │
  ├─────────────┼─────────────────────────────────────────────┤
  │ Deserialize │ Lets you convert FROM JSON/TOML             │
  ├─────────────┼─────────────────────────────────────────────┤
  │ Option<T>   │ Optional field - can be Some(value) or None │
  └─────────────┴─────────────────────────────────────────────┘

  Why so many Option?

  These come from a TOML config file:

  [plugin_config]
  connection_uri = "mongodb://localhost:27017"  # Required (String, not Option)
  database = "mydb"                              # Required
  collection = "messages"                        # Required
  batch_size = 100                               # Optional - if not set, use default
  verbose_logging = true                         # Optional

  If user doesn't set batch_size, it's None → code uses default 100.

  Scene 6: The Enum (Lines 63-69)

  #[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
  pub enum PayloadFormat {
      #[default]
      Binary,
      Json,
      String,
  }

  Rust syntax:

  ┌────────────┬──────────────────────────────────────────────────┐
  │   Piece    │                     Meaning                      │
  ├────────────┼──────────────────────────────────────────────────┤
  │ enum       │ Enumeration - a type with fixed variants         │
  ├────────────┼──────────────────────────────────────────────────┤
  │ Copy       │ Type is copied by value (not moved)              │
  ├────────────┼──────────────────────────────────────────────────┤
  │ PartialEq  │ Can compare with ==                              │
  ├────────────┼──────────────────────────────────────────────────┤
  │ Eq         │ Full equality (reflexive, symmetric, transitive) │
  ├────────────┼──────────────────────────────────────────────────┤
  │ #[default] │ Default value is Binary                          │
  └────────────┴──────────────────────────────────────────────────┘

  What it represents:

  How should we store the message payload in MongoDB?

  Binary: Store as BSON Binary (raw bytes)
          { "payload": <Binary 0x8a7f3b...> }

  Json:   Parse as JSON, store as BSON object
          { "payload": { "name": "Alice", "age": 30 } }

  String: Store as UTF-8 text
          { "payload": "Hello, world!" }

  Scene 7: The Trait Implementation (Lines 108-149)

  This is the HEART of your connector:

  #[async_trait]
  impl Sink for MongoDbSink {
      async fn open(&mut self) -> Result<(), Error> {
          // Connect to MongoDB
          // Create collection if needed
      }

      async fn consume(
          &self,
          topic_metadata: &TopicMetadata,
          messages_metadata: MessagesMetadata,
          messages: Vec<ConsumedMessage>,
      ) -> Result<(), Error> {
          // Process messages from Iggy
          // Store them in MongoDB
      }

      async fn close(&mut self) -> Result<(), Error> {
          // Cleanup
          // Log final stats
      }
  }

  Rust syntax breakdown:

  ┌───────────────────────────┬────────────────────────────────────────────────────┐
  │           Piece           │                      Meaning                       │
  ├───────────────────────────┼────────────────────────────────────────────────────┤
  │ #[async_trait]            │ Magic attribute that makes async fn work in traits │
  ├───────────────────────────┼────────────────────────────────────────────────────┤
  │ impl Sink for MongoDbSink │ "I'm implementing the Sink trait for my struct"    │
  ├───────────────────────────┼────────────────────────────────────────────────────┤
  │ &mut self                 │ Mutable borrow of self (can modify)                │
  ├───────────────────────────┼────────────────────────────────────────────────────┤
  │ &self                     │ Immutable borrow of self (read-only)               │
  ├───────────────────────────┼────────────────────────────────────────────────────┤
  │ Result<(), Error>         │ Returns either Ok(()) or Err(Error)                │
  ├───────────────────────────┼────────────────────────────────────────────────────┤
  │ &TopicMetadata            │ Reference to TopicMetadata (no copy)               │
  └───────────────────────────┴────────────────────────────────────────────────────┘

  The lifecycle:

  1. Iggy calls open()
     └── Connect to MongoDB
     └── Create collection if needed

  2. Iggy calls consume() repeatedly
     └── Each call brings new messages
     └── You store them in MongoDB

  3. Iggy calls close()
     └── Cleanup
     └── Log stats

  Scene 8: The connect() Method (Lines 153-179)

  async fn connect(&mut self) -> Result<(), Error> {
      let redacted = redact_connection_uri(&self.config.connection_uri);
      info!("Connecting to MongoDB: {redacted}");

      let mut options = ClientOptions::parse(&self.config.connection_uri)
          .await
          .map_err(|e| Error::InitError(format!("Failed to parse connection URI: {e}")))?;

      if let Some(pool_size) = self.config.max_pool_size {
          options.max_pool_size = Some(pool_size);
      }

      let client = Client::with_options(options)
          .map_err(|e| Error::InitError(format!("Failed to create client: {e}")))?;

      client
          .database(&self.config.database)
          .run_command(mongodb::bson::doc! {"ping": 1})
          .await
          .map_err(|e| Error::InitError(format!("Database connectivity test failed: {e}")))?;

      self.client = Some(client);
      info!("Connected to MongoDB database: {}", self.config.database);
      Ok(())
  }

  Line-by-line:

  let redacted = redact_connection_uri(&self.config.connection_uri);
  - Call function to hide password in logs
  - mongodb://user:SECRET@localhost:27017 → mongodb://loc***

  let mut options = ClientOptions::parse(&self.config.connection_uri)
      .await
      .map_err(|e| Error::InitError(...))?;
  - Parse connection string into options struct
  - .await = wait for async operation to complete
  - .map_err(...) = convert MongoDB error to Iggy error
  - ? = if error, return early. If ok, continue.

  if let Some(pool_size) = self.config.max_pool_size {
      options.max_pool_size = Some(pool_size);
  }
  - if let Some(x) = option = "if option is Some, extract x"
  - Only set pool_size if user configured it

  client.database(&self.config.database)
      .run_command(mongodb::bson::doc! {"ping": 1})
      .await
  - Send { "ping": 1 } command to MongoDB
  - This tests if connection actually works

  Scene 9: The insert_batch_with_retry() Method (Lines 343-372)

  async fn insert_batch_with_retry(
      &self,
      collection: &Collection<mongodb::bson::Document>,
      docs: &[mongodb::bson::Document],
  ) -> Result<(), Error> {
      let max_retries = self.get_max_retries();
      let retry_delay = self.retry_delay;
      let mut attempts = 0u32;

      loop {
          let result = collection.insert_many(docs.to_vec()).await;

          match result {
              Ok(_) => return Ok(()),
              Err(e) => {
                  attempts += 1;
                  if !is_transient_error(&e) || attempts >= max_retries {
                      error!("Batch insert failed after {attempts} attempts: {e}");
                      return Err(Error::CannotStoreData(...));
                  }
                  warn!("Transient database error (attempt {attempts}/{max_retries}): {e}");
                  tokio::time::sleep(retry_delay * attempts).await;
              }
          }
      }
  }

  The retry logic:

  Attempt 1: insert_many() → Error!
             Is it transient (network timeout)?
               YES: Wait 1s, retry
               NO:  Fail immediately

  Attempt 2: insert_many() → Error!
             Is it transient?
               YES: Wait 2s, retry
               NO:  Fail immediately

  Attempt 3: insert_many() → Success!
             Return Ok(())

  Rust syntax:

  loop { ... }              // Infinite loop (break with return or break)
  match result {            // Pattern matching
      Ok(_) => ...,         // Success (ignore the value with _)
      Err(e) => ...,        // Error, bind to variable e
  }

  Scene 10: The is_transient_error() Function (Lines 389-419)

  fn is_transient_error(e: &mongodb::error::Error) -> bool {
      use mongodb::error::ErrorKind;

      if e.contains_label(mongodb::error::RETRYABLE_WRITE_ERROR) {
          return true;
      }

      match e.kind.as_ref() {
          ErrorKind::Io(_) => true,
          ErrorKind::ConnectionPoolCleared { .. } => true,
          ErrorKind::ServerSelection { .. } => true,
          ErrorKind::Authentication { .. } => false,
          ErrorKind::InsertMany(insert_many_error) => {
              let has_non_retryable_write_error = insert_many_error
                  .write_errors
                  .as_ref()
                  .is_some_and(|wes| wes.iter().any(|we| matches!(we.code, 11000 | 13 | 121)));
              !has_non_retryable_write_error
          }
          _ => {
              let msg = e.to_string().to_lowercase();
              msg.contains("timeout") || msg.contains("network")
          }
      }
  }

  What it does: Classifies errors as "retry-able" or "permanent".

  ┌────────────────────────────┬────────────┬─────────────────────────────────────┐
  │           Error            │ Transient? │                 Why                 │
  ├────────────────────────────┼────────────┼─────────────────────────────────────┤
  │ Network timeout            │ YES        │ Network might recover               │
  ├────────────────────────────┼────────────┼─────────────────────────────────────┤
  │ Connection pool exhausted  │ YES        │ Wait for connection to free up      │
  ├────────────────────────────┼────────────┼─────────────────────────────────────┤
  │ Authentication failed      │ NO         │ Wrong password, retrying won't help │
  ├────────────────────────────┼────────────┼─────────────────────────────────────┤
  │ Duplicate key (code 11000) │ NO         │ Data conflict, retrying won't help  │
  ├────────────────────────────┼────────────┼─────────────────────────────────────┤
  │ Unauthorized (code 13)     │ NO         │ Permission denied                   │
  └────────────────────────────┴────────────┴─────────────────────────────────────┘

  Rust syntax:

  match e.kind.as_ref() {           // Match on the error kind
      ErrorKind::Io(_) => true,     // Any IO error → transient
      _ => { ... }                  // Catch-all (underscore = wildcard)
  }

  matches!(we.code, 11000 | 13 | 121)   // Is code one of these values?

  ---
  Act 4: The Code - Source Edition

  The source is similar but does the reverse. Key differences:

  1. It Polls Instead of Being Pushed

  async fn poll(&self) -> Result<Option<Vec<ProducedMessage>>, Error> {
      // Query MongoDB for new documents
      // Convert them to Iggy messages
      // Return Some(messages) or None if no new data
  }

  The flow:

  Every 10 seconds (poll_interval):

  1. Query MongoDB:
     db.collection.find({ "_id": { "$gt": last_seen_id } })

  2. Convert documents to Iggy messages

  3. Remember last seen _id (for next poll)

  4. Return messages to Iggy

  2. It Tracks Position

  struct State {
      tracking_offsets: HashMap<String, String>,  // collection → last seen _id
  }

  Why: If the connector restarts, it needs to know where it left off:

  Collection "events":
    Document _id: "abc123"  ← processed
    Document _id: "def456"  ← processed
    Document _id: "ghi789"  ← NOT processed yet!

  State: { "events": "def456" }

  Next query: find({ "_id": { "$gt": "def456" } })

  ---
  Act 5: Key Rust Concepts You Used

  1. Ownership & Borrowing

  fn process(&self, messages: &[ConsumedMessage])
  //              ^                  ^
  //              |                  |
  //        immutable borrow    slice (reference to array)

  - &self = borrow self (don't take ownership)
  - &[T] = slice = reference to a sequence

  2. Option vs Result

  Option<T>                          Result<T, E>
  ├── Some(value)                    ├── Ok(value)
  └── None                           └── Err(error)

  Used for: "might not have a value"    Used for: "might fail"

  3. The ? Operator

  let client = Client::with_options(options)
      .map_err(|e| Error::InitError(...))?;

  What it does:
  - If Ok(client), unwrap and continue
  - If Err(e), return the error immediately

  Without ?:
  let client = match Client::with_options(options) {
      Ok(c) => c,
      Err(e) => return Err(Error::InitError(...)),
  };

  4. Async/Await

  async fn open(&mut self) -> Result<(), Error> {
      let client = Client::with_options(options).await?;
      //                                   ^^^^^^
      //                                   Wait for this to complete
  }

  Mental model: .await pauses this function, lets other code run, resumes when the operation completes.

  5. Pattern Matching

  match result {
      Ok(_) => return Ok(()),       // Success, ignore value
      Err(e) => {                   // Error, bind to e
          // handle error
      }
  }

  ---
  Summary: What You Built

  ┌─────────────────────────────────────────────────────────────────────┐
  │                         MONGODB SINK                                │
  │                                                                     │
  │  1. Iggy sends you messages                                        │
  │  2. You convert them to BSON documents                             │
  │  3. You insert them into MongoDB (with retry on transient errors)  │
  │                                                                     │
  │  Lines of real code: ~250                                          │
  │  Key functions: open(), consume(), insert_batch_with_retry()       │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │                        MONGODB SOURCE                               │
  │                                                                     │
  │  1. You poll MongoDB for new documents                             │
  │  2. You convert them to Iggy messages                              │
  │  3. You track position (last seen _id)                             │
  │  4. Iggy receives the messages                                     │
  │                                                                     │
  │  Lines of real code: ~350                                          │
  │  Key functions: open(), poll(), fetch_documents()                  │
  └─────────────────────────────────────────────────────────────────────┘

  You now understand every line of production code in this PR!

```