# Iggy Naming Conventions

## Overview

Iggy follows strict naming conventions to ensure code clarity, consistency, and LLM-friendliness.

---

## 1. Crate Naming

### Pattern: hyphenated-lowercase

```
iggy-common
iggy-binary-protocol
iggy-connector-sdk
iggy-bench-runner
```

### Workspace Path Names

```
core/common/
core/binary_protocol/
core/connectors/sdk/
core/bench/runner/
```

---

## 2. Type Naming

### Structs: PascalCase

```rust
pub struct IggyMessage {
    pub header: MessageHeader,
    pub payload: Bytes,
    pub user_headers: Option<HashMap<HeaderKey, HeaderValue>>,
}

pub struct ConsumerGroup {
    pub id: ConsumerGroupId,
    pub name: String,
    pub partitions: Vec<PartitionId>,
}
```

### Enums: PascalCase Variants

```rust
pub enum IggyError {
    InvalidConfiguration,
    ConsumerGroupIdAlreadyExists(u32, u32),
    CannotDeserializePayload(u32, usize, usize),
}

pub enum ClientState {
    Disconnected,
    Connecting,
    Connected,
    Authenticating,
    Authenticated,
}
```

### Type Aliases: PascalCase

```rust
pub type StreamId = usize;
pub type TopicId = usize;
pub type PartitionId = usize;
pub type UserId = u32;
pub type ConsumerGroupId = usize;

pub type MetadataReadHandle = left_right::ReadHandle<InnerMetadata>;
```

---

## 3. Function Naming

### Pattern: snake_case

```rust
pub fn create_stream(&self, name: &str) -> Result<Stream, IggyError>;
pub fn poll_messages(&self, stream: &Identifier) -> Result<Messages, IggyError>;
pub fn send_messages(&self, messages: Vec<IggyMessage>) -> Result<(), IggyError>;
```

### Verb Prefixes

| Prefix | Usage |
|--------|-------|
| `create_` | Creates new resource |
| `get_` | Retrieves resource |
| `update_` | Modifies existing resource |
| `delete_` | Removes resource |
| `send_` | Transmits data |
| `poll_` | Receives data (non-blocking) |
| `receive_` | Receives data (may block) |
| `validate_` | Checks validity |
| `serialize_` | Converts to bytes |
| `deserialize_` | Converts from bytes |
| `compute_` | Calculates value |
| `process_` | Handles data flow |
| `init_` | Initializes state |
| `shutdown_` | Graceful termination |

### Query Functions: is_/has_/can_

```rust
pub fn is_connected(&self) -> bool;
pub fn is_authenticated(&self) -> bool;
pub fn has_permission(&self, permission: Permission) -> bool;
pub fn can_read(&self) -> bool;
```

### Conversion Functions

```rust
pub fn from_bytes(bytes: Bytes) -> Result<Self, IggyError>;
pub fn to_bytes(&self) -> Bytes;
pub fn from_str(s: &str) -> Result<Self, IggyError>;
pub fn as_code(&self) -> u32;
```

---

## 4. Variable Naming

### Pattern: snake_case

```rust
let stream_id = stream.id();
let topic_name = topic.name();
let consumer_group = ConsumerGroup::new(name);
```

### Iterator Variables: Descriptive

```rust
// Preferred
for partition in partitions {
    process_partition(partition);
}

// When index needed
for (index, message) in messages.iter().enumerate() {
    println!("Message {}: {}", index, message);
}
```

### Boolean Variables: is_/has_/should_ prefix

```rust
let is_connected = client.state() == ClientState::Connected;
let has_messages = !messages.is_empty();
let should_retry = retries < max_retries;
```

---

## 5. Constant Naming

### Pattern: SCREAMING_SNAKE_CASE

```rust
pub const DEFAULT_PORT: u16 = 8090;
pub const MAX_MESSAGE_SIZE: usize = 10 * 1024 * 1024;
pub const SHUTDOWN_TIMEOUT: Duration = Duration::from_secs(30);
pub const REQUEST_INITIAL_BYTES_LENGTH: usize = 4;
```

### Static Values

```rust
pub static VERSION: &str = "0.1.0";
pub static DEFAULT_SERVER_ADDRESS: &str = "127.0.0.1:8090";
```

---

## 6. Module Naming

### Pattern: snake_case

```
src/
  streaming/
    partitions/
    segments/
  client/
    tcp/
    quic/
    http/
```

### Re-exports Pattern

```rust
// lib.rs
pub mod streaming;
pub mod client;

pub use streaming::partition::Partition;
pub use client::{TcpClient, QuicClient};
```

---

## 7. Trait Naming

### Pattern: PascalCase with Verb or Noun

```rust
// Verb traits (behavior)
pub trait Serializable { }
pub trait Validatable { }
pub trait Send { }
pub trait Clone { }

// Noun traits (capability)
pub trait Stream { }
pub trait Iterator { }
pub trait Consensus { }
pub trait Storage { }
```

### Trait Suffixes

| Suffix | Meaning |
|--------|---------|
| `able` | Can be done to type (`Validatable`) |
| `er` | Agent that performs (`Consumer`, `Producer`) |
| `or` | Agent that performs (`Visitor`, `Executor`) |

---

## 8. File Naming

### Pattern: snake_case.rs

```
message_client.rs
consumer_group.rs
partition_config.rs
```

### Module Organization

```
partition/
  mod.rs          # Re-exports
  config.rs       # PartitionConfig
  segment.rs      # Segment
  log.rs          # SegmentedLog
  ops.rs          # Operations
```

---

## 9. Commit Message Format

### Pattern: type(scope): subject

```
feat(server): add consumer group rebalancing
fix(protocol): handle connection timeout correctly
refactor(client): extract common retry logic
perf(storage): optimize message polling
docs(readme): update installation instructions
ci(actions): add coverage reporting
```

### Types

| Type | Usage |
|------|-------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Code restructuring |
| `perf` | Performance improvement |
| `docs` | Documentation |
| `test` | Test changes |
| `ci` | CI/CD changes |
| `chore` | Maintenance |

---

## 10. Field Naming

### Pattern: snake_case

```rust
pub struct TopicConfig {
    pub max_partitions: u32,
    pub message_expiry: Option<IggyDuration>,
    pub replication_factor: u8,
}
```

### Optional Fields

```rust
pub struct ConsumerConfig {
    pub auto_commit: Option<AutoCommitConfig>,
    pub consumer_group: Option<String>,
}
```

---

## 11. Error Variant Naming

### Pattern: PascalCase with Context

```rust
pub enum IggyError {
    // Resource not found
    StreamNotFound(u32),
    TopicNotFound(u32, u32),  // stream_id, topic_id
    
    // Already exists
    StreamAlreadyExists(String),
    ConsumerGroupNameAlreadyExists(String, u32),
    
    // Invalid state
    InvalidStateEntryChecksum(u64, u64, u64),
    CannotDeserializePayload(u32, usize, usize),
}
```

---

## 12. Avoid These Anti-Patterns

### Don't: Abbreviations

```rust
// Bad
let msg = message;
let conn = connection;
let cfg = config;

// Good
let message = message;
let connection = connection;
let config = config;
```

### Don't: Single-letter Variables (except common)

```rust
// Bad
let x = get_value();
let t = transform(x);

// Acceptable (common conventions)
for i in 0..count { }
let (k, v) = entry;
```

### Don't: Inconsistent Naming

```rust
// Bad
fn getStream() -> Stream { }
fn fetch_topic() -> Topic { }

// Good
fn get_stream() -> Stream { }
fn get_topic() -> Topic { }
```

---

## Summary: Naming Checklist

- [ ] Crate names: hyphenated-lowercase
- [ ] Types: PascalCase
- [ ] Functions: snake_case with verb prefix
- [ ] Variables: snake_case, descriptive
- [ ] Constants: SCREAMING_SNAKE_CASE
- [ ] Modules: snake_case
- [ ] Traits: PascalCase (verb or noun)
- [ ] Files: snake_case.rs
- [ ] Commit messages: `type(scope): subject`
