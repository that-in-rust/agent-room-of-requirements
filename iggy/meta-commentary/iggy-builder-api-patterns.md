# Iggy Builder & API Design Patterns

## Overview

Iggy uses sophisticated builder patterns and fluent APIs for constructing complex objects, combining `bon` derive builders with traditional fluent builders.

---

## 1. bon Builder - Derive-Based Builders

### Pattern: bon::bon Attribute

```rust
use bon::bon;

#[bon]
impl IggyMessage {
    #[builder]
    pub fn new(
        id: Option<u128>,
        payload: Bytes,
        user_headers: Option<HashMap<HeaderKey, HeaderValue>>,
    ) -> Result<Self, IggyError> {
        if payload.is_empty() {
            return Err(IggyError::InvalidMessagePayloadLength);
        }
        
        let header = MessageHeader {
            id: id.unwrap_or_else(|| uuid::Uuid::now_v7().as_u128()),
            // ... other fields
        };
        
        Ok(Self { header, payload, user_headers })
    }
}
```

### Usage

```rust
let message = IggyMessage::builder()
    .payload("Hello world!".into())
    .user_headers(headers)
    .build()
    .unwrap();
```

### When to Use bon

- Complex constructors with many optional parameters
- Validation logic in build method
- Default value handling

---

## 2. Traditional Fluent Builder

### Pattern: Consuming Builder with Methods

```rust
#[derive(Default)]
pub struct IggyShardBuilder {
    id: Option<u16>,
    shards_table: Option<EternalPtr<DashMap<IggyNamespace, PartitionLocation>>>,
    state: Option<FileState>,
    client_manager: Option<ClientManager>,
}

impl IggyShardBuilder {
    pub fn id(mut self, id: u16) -> Self {
        self.id = Some(id);
        self
    }
    
    pub fn connections(mut self, connections: Vec<ShardConnector<ShardFrame>>) -> Self {
        self.connections = Some(connections);
        self
    }
    
    pub fn build(self) -> IggyShard {
        IggyShard {
            id: self.id.expect("id is required"),
            shards_table: self.shards_table.expect("shards_table is required"),
            // ...
        }
    }
}
```

### When to Use Traditional Builder

- When builder needs to be stored/modified before build
- When construction involves side effects
- When working with external types

---

## 3. Client Configuration Builders

### Pattern: Config Builder with Defaults

```rust
pub struct QuicClientConfigBuilder {
    config: QuicClientConfig,
}

impl QuicClientConfigBuilder {
    pub fn new() -> Self {
        QuicClientConfigBuilder {
            config: QuicClientConfig::default(),
        }
    }
    
    pub fn with_server_address(mut self, server_address: String) -> Self {
        self.config.server_address = server_address;
        self
    }
    
    pub fn with_reconnection_max_retries(mut self, max_retries: Option<u32>) -> Self {
        self.config.reconnection.max_retries = max_retries;
        self
    }
    
    pub fn with_reconnection_interval(mut self, interval: IggyDuration) -> Self {
        self.config.reconnection.interval = interval;
        self
    }
    
    pub fn with_heartbeat_interval(mut self, interval: IggyDuration) -> Self {
        self.config.heartbeat_interval = interval;
        self
    }
    
    pub fn build(self) -> QuicClientConfig {
        self.config
    }
}
```

---

## 4. Factory Methods / Named Constructors

### Pattern: Multiple Constructor Variants

```rust
impl Partitioning {
    pub fn balanced() -> Self {
        Partitioning {
            kind: PartitioningKind::Balanced,
            length: 0,
            value: vec![],
        }
    }

    pub fn partition_id(partition_id: u32) -> Self {
        Partitioning {
            kind: PartitioningKind::PartitionId,
            length: 4,
            value: partition_id.to_le_bytes().to_vec(),
        }
    }

    pub fn messages_key(value: &[u8]) -> Result<Self, IggyError> {
        if value.is_empty() {
            return Err(IggyError::InvalidPartitioning);
        }
        Ok(Partitioning {
            kind: PartitioningKind::MessagesKey,
            length: value.len() as u8,
            value: value.to_vec(),
        })
    }

    pub fn messages_key_str(value: &str) -> Result<Self, IggyError> {
        Self::messages_key(value.as_bytes())
    }

    pub fn messages_key_u32(value: u32) -> Self {
        Self::partition_id(value) // Alias for consistency
    }

    pub fn messages_key_u64(value: u64) -> Self {
        Partitioning {
            kind: PartitioningKind::MessagesKey,
            length: 8,
            value: value.to_le_bytes().to_vec(),
        }
    }
}
```

### Pattern: Identifier Constructors

```rust
impl Identifier {
    pub fn numeric(value: u32) -> Result<Self, IggyError> {
        let identifier = Identifier {
            kind: IdKind::Numeric,
            length: 4,
            value: value.to_le_bytes().to_vec(),
        };
        identifier.validate()?;
        Ok(identifier)
    }
    
    pub fn named(value: &str) -> Result<Self, IggyError> {
        let bytes = value.as_bytes();
        if bytes.len() > 255 {
            return Err(IggyError::InvalidIdentifier);
        }
        let identifier = Identifier {
            kind: IdKind::String,
            length: bytes.len() as u8,
            value: bytes.to_vec(),
        };
        identifier.validate()?;
        Ok(identifier)
    }
}
```

---

## 5. Type-State Pattern

### Pattern: Phantom Types for Compile-Time Safety

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct KeyMarker;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct ValueMarker;

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct HeaderField<T> {
    kind: HeaderKind,
    value: HeaderValue,
    _marker: PhantomData<T>,
}

pub type HeaderKey = HeaderField<KeyMarker>;
pub type HeaderValue = HeaderField<ValueMarker>;
```

### Benefits

- Keys and values cannot be confused at compile time
- Zero runtime overhead
- Clear API contracts

---

## 6. Producer Builder Pattern

### Pattern: Nested Builder with Strategies

```rust
let mut producer = client
    .producer("dev01", "events")?
    .direct(  // or .background()
        DirectConfig::builder()
            .batch_length(1000)
            .linger_time(IggyDuration::from_str("1ms")?)
            .build(),
    )
    .partitioning(Partitioning::balanced())
    .build();

producer.init().await?;
```

### Background Producer Configuration

```rust
let mut producer = client
    .producer("stream", "topic")?
    .background(
        BackgroundConfig::builder()
            .buffer_size_bytes(ByteSize::mb(64))
            .failure_mode(BackpressureMode::Block)
            .sharding(Sharding::Balanced)
            .build(),
    )
    .partitioning(Partitioning::partition_id(1))
    .build();
```

---

## 7. Consumer Builder Pattern

### Pattern: Fluent Chain with Multiple Options

```rust
let mut consumer = client
    .consumer_group("my_app", "dev01", "events")?
    .auto_commit(AutoCommit::IntervalOrWhen(
        IggyDuration::from_str("1s")?,
        AutoCommitWhen::ConsumingAllMessages,
    ))
    .create_consumer_group_if_not_exists()
    .auto_join_consumer_group()
    .polling_strategy(PollingStrategy::next())
    .poll_interval(IggyDuration::from_str("1ms")?)
    .batch_length(1000)
    .build();

consumer.init().await?;
```

---

## 8. BytesSerializable Trait

### Pattern: Custom Serialization Interface

```rust
pub trait BytesSerializable {
    fn to_bytes(&self) -> Bytes;
    fn from_bytes(bytes: Bytes) -> Result<Self, IggyError>
    where
        Self: Sized;
    
    fn write_to_buffer(&self, _buf: &mut BytesMut) { unimplemented!(); }
    fn get_buffer_size(&self) -> usize { unimplemented!(); }
}
```

### Implementation Example

```rust
impl BytesSerializable for Identifier {
    fn to_bytes(&self) -> Bytes {
        let mut bytes = BytesMut::with_capacity(2 + self.length as usize);
        bytes.put_u8(self.kind.as_code());
        bytes.put_u8(self.length);
        bytes.put_slice(&self.value);
        bytes.freeze()
    }

    fn from_bytes(bytes: Bytes) -> Result<Self, IggyError> {
        let kind = IdKind::from_code(*bytes.first().ok_or(IggyError::InvalidIdentifier)?)?;
        let length = *bytes.get(1).ok_or(IggyError::InvalidIdentifier)?;
        let value = bytes.get(2..2 + length as usize)
            .ok_or(IggyError::InvalidIdentifier)?
            .to_vec();
        let identifier = Identifier { kind, length, value };
        identifier.validate()?;
        Ok(identifier)
    }
}
```

---

## 9. Protocol Abstraction

### Pattern: ClientWrapper Enum

```rust
pub enum ClientWrapper {
    Iggy(IggyClient),
    Http(HttpClient),
    Tcp(TcpClient),
    Quic(QuicClient),
    WebSocket(WebSocketClient),
}

impl MessageClient for ClientWrapper {
    async fn poll_messages(&self, ...) -> Result<PolledMessages, IggyError> {
        match self {
            ClientWrapper::Iggy(c) => c.poll_messages(...).await,
            ClientWrapper::Tcp(c) => c.poll_messages(...).await,
            ClientWrapper::Quic(c) => c.poll_messages(...).await,
            // ...
        }
    }
}
```

### BinaryTransport Trait

```rust
#[async_trait]
pub trait BinaryTransport: Send + Sync {
    async fn get_state(&self) -> ClientState;
    async fn set_state(&self, state: ClientState);
    async fn connect(&self) -> Result<(), IggyError>;
    async fn disconnect(&self) -> Result<(), IggyError>;
}
```

---

## 10. Connection String Parsing

### Pattern: URI-Style Connection Strings

```rust
let client = IggyClient::from_connection_string(
    "iggy://user:secret@localhost:8090?transport=tcp&tls=true"
)?;
```

### Supported Formats

```
iggy://localhost:8090
iggy://user:pass@localhost:8090
iggy://localhost:8090?transport=quic
iggy://localhost:8090?transport=websocket&tls=true
http://localhost:3000
```

---

## 11. Display Implementations

### Pattern: Human-Readable Formatting

```rust
impl std::fmt::Display for IggyMessage {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match String::from_utf8(self.payload.to_vec()) {
            Ok(payload) => {
                write!(
                    f,
                    "[{offset}] ID:{id} '{preview}'",
                    offset = self.header.offset,
                    id = self.header.id,
                    preview = if payload.len() > 50 {
                        format!("{}... ({}B)", &payload[..47], self.payload.len())
                    } else {
                        payload
                    }
                )
            }
            Err(_) => {
                write!(
                    f,
                    "[{offset}] ID:{id} <binary {payload_len}B>",
                    offset = self.header.offset,
                    id = self.header.id,
                    payload_len = self.payload.len()
                )
            }
        }
    }
}
```

---

## Summary: API Design Checklist

- [ ] Use `bon` for derive-based builders
- [ ] Use traditional builders for side-effect construction
- [ ] Provide named constructors for common cases
- [ ] Use type-state pattern for compile-time safety
- [ ] Implement `BytesSerializable` for wire types
- [ ] Implement `Display` for human-readable output
- [ ] Use protocol abstraction for multi-transport support
- [ ] Support connection string parsing for ergonomics
