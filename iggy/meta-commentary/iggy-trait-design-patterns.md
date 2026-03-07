# Iggy Trait Design Patterns

## Overview

Iggy uses advanced Rust trait patterns including GATs (Generic Associated Types), RPITIT (Return Position Impl Trait In Traits), and sophisticated trait bounds for type-safe abstractions.

---

## 1. RPITIT - Zero-Cost Async Traits

### Pattern: impl Future in Traits

Instead of `#[async_trait]` which boxes futures, use RPITIT:

```rust
pub trait Plane<C>
where
    C: Consensus,
{
    fn on_request(&self, message: RequestMessage<C>) -> impl Future<Output = ()>
    where
        RequestMessage<C>: Project<ReplicateMessage<C>, C, Consensus = C> + Clone;

    fn on_replicate(&self, message: ReplicateMessage<C>) -> impl Future<Output = ()>
    where
        ReplicateMessage<C>: Project<AckMessage<C>, C, Consensus = C> + Clone;

    fn on_ack(&self, message: AckMessage<C>) -> impl Future<Output = ()>;
}
```

### Benefits

- **No heap allocation**: Futures are stack-allocated
- **Compiler optimization**: Full inlining possible
- **Native syntax**: No macro magic

---

## 2. GATs - Generic Associated Types

### Pattern: Lifetime-Bounded Associated Types

```rust
pub trait Journal<S>
where
    S: Storage,
{
    type Header;
    type Entry;
    type HeaderRef<'a>: Deref<Target = Self::Header>
    where
        Self: 'a;

    fn header(&self, idx: usize) -> Option<Self::HeaderRef<'_>>;
    fn previous_header(&self, header: &Self::Header) -> Option<Self::HeaderRef<'_>>;
}
```

### Pattern: Parameterized Message Types

```rust
pub trait Consensus: Sized {
    type Message<H>: ConsensusMessage<H> 
    where 
        H: ConsensusHeader;

    type RequestHeader: ConsensusHeader;
    type ReplicateHeader: ConsensusHeader;
    type AckHeader: ConsensusHeader;
}
```

---

## 3. Type Aliases for Complex Associated Types

### Pattern: Fully-Qualified Syntax

```rust
pub type RequestMessage<C> = <C as Consensus>::Message<<C as Consensus>::RequestHeader>;
pub type ReplicateMessage<C> = <C as Consensus>::Message<<C as Consensus>::ReplicateHeader>;
pub type AckMessage<C> = <C as Consensus>::Message<<C as Consensus>::AckHeader>;
```

### Benefits

- Improves readability
- Self-documenting types
- Reduces repetition

---

## 4. Variadic Trait Implement

### Pattern: iggy_common::variadic! Macro

```rust
impl<C, Head, Tail> Plane<C> for variadic!(Head, ...Tail)
where
    C: Consensus,
    Head: Plane<C> + PlaneIdentity<C>,
    Tail: Plane<C>,
{
    async fn on_request(&self, message: RequestMessage<C>)
    where
        RequestMessage<C>: Project<ReplicateMessage<C>, C, Consensus = C> + Clone,
    {
        if self.0.is_applicable(&message) {
            self.0.on_request(message).await;
        } else {
            self.1.on_request(message).await;
        }
    }
}
```

### Usage

```rust
type MuxPlane = variadic!(MetadataPlane, ConsensusPlane, DataPlane);
```

---

## 5. Where Clause Organization

### Pattern: Hoist Complex Bounds

```rust
// Inlinable bounds in impl header
impl<B: MessageBus, P: Pipeline<Entry = PipelineEntry>> VsrConsensus<B, P> {
    // Methods
}

// Complex multi-trait bounds in where clause
impl<B, P> Consensus for VsrConsensus<B, P>
where
    B: MessageBus,
    P: Pipeline<Message = Message<PrepareHeader>, Entry = PipelineEntry>,
{
    // Trait implementation
}
```

### Method-Level Where Clauses

```rust
fn on_request(&self, message: RequestMessage<C>) -> impl Future<Output = ()>
where
    RequestMessage<C>: Project<ReplicateMessage<C>, C, Consensus = C> + Clone;
```

---

## 6. Sealed Traits

### Pattern: Private Sealed Module

```rust
mod sealed {
    pub trait Sealed {}
}

pub trait PublicTrait: sealed::Sealed {
    // Public methods
}

// Implement Sealed only for allowed types
impl sealed::Sealed for AllowedType {}
```

### Benefits

- Prevents external implementations
- API stability guarantee
- Implementation freedom

---

## 7. Extension Traits

### Pattern: Add Methods to External Types

```rust
pub trait IdentifierExt {
    fn as_stream_id(&self) -> Result<StreamId, IggyError>;
    fn as_topic_id(&self) -> Result<TopicId, IggyError>;
}

impl IdentifierExt for Identifier {
    fn as_stream_id(&self) -> Result<StreamId, IggyError> {
        match self.kind {
            IdKind::Numeric => Ok(u32::from_le_bytes(self.value.as_slice().try_into()?) as usize),
            IdKind::String => Err(IggyError::InvalidIdentifier),
        }
    }
}
```

---

## 8. Marker Traits

### Pattern: Zero-Sized Type Markers

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct KeyMarker;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct ValueMarker;

pub type HeaderKey = HeaderField<KeyMarker>;
pub type HeaderValue = HeaderField<ValueMarker>;
```

### Benefits

- Compile-time type distinction
- Zero runtime overhead
- Clear API contracts

---

## 9. Trait Objects with Dyn

### Pattern: Dynamic Dispatch at Boundaries

```rust
pub trait Source: Send + Sync {
    fn name(&self) -> &str;
    fn start(&mut self) -> impl Future<Output = Result<(), IggyError>>;
    fn stop(&mut self) -> impl Future<Output = Result<(), IggyError>>;
}

// Dynamic collection
let sources: Vec<Box<dyn Source>> = vec![/* ... */];
```

### When to Use Dyn

- Plugin systems
- Heterogeneous collections
- API boundaries where flexibility needed

---

## 10. Associated Constants

### Pattern: Trait-Level Configuration

```rust
pub trait Storage {
    const MAX_SEGMENT_SIZE: usize;
    const INDEX_GRANULARITY: u32;
    
    fn read(&self, offset: u64, length: usize) -> impl Future<Output = Result<Bytes, IggyError>>;
    fn write(&self, data: &[u8]) -> impl Future<Output = Result<u64, IggyError>>;
}
```

---

## 11. Supertraits

### Pattern: Trait Composition

```rust
pub trait ConsensusMessage<H>: 
    Debug + Clone + Send + Sync + 'static
where
    H: ConsensusHeader,
{
    fn header(&self) -> &H;
    fn payload(&self) -> &[u8];
}

pub trait ConsensusHeader: 
    Debug + Clone + Copy + Send + Sync + 'static
{
    fn op(&self) -> u64;
    fn checksum(&self) -> u128;
}
```

---

## 12. Default Trait Methods

### Pattern: Overridable Defaults

```rust
pub trait Client {
    fn connect(&self) -> impl Future<Output = Result<(), IggyError>>;
    
    fn connect_with_retry(&self, max_retries: u32) -> impl Future<Output = Result<(), IggyError>> {
        async move {
            let mut retries = 0;
            loop {
                match self.connect().await {
                    Ok(_) => return Ok(()),
                    Err(e) => {
                        retries += 1;
                        if retries > max_retries {
                            return Err(e);
                        }
                        sleep(Duration::from_millis(100)).await;
                    }
                }
            }
        }
    }
}
```

---

## 13. Command Pattern with Traits

### Pattern: BinaryTransport Trait

```rust
#[async_trait]
pub trait BinaryTransport: Send + Sync {
    async fn get_state(&self) -> ClientState;
    async fn set_state(&self, state: ClientState);
    async fn connect(&self) -> Result<(), IggyError>;
    async fn disconnect(&self) -> Result<(), IggyError>;
}
```

### MessageClient Trait

```rust
#[async_trait]
pub trait MessageClient: Send + Sync {
    async fn poll_messages(
        &self,
        stream_id: &Identifier,
        topic_id: &Identifier,
        partition_id: Option<u32>,
        consumer: &Consumer,
        strategy: &PollingStrategy,
        count: u32,
        auto_commit: bool,
    ) -> Result<PolledMessages, IggyError>;

    async fn send_messages(
        &self,
        stream_id: &Identifier,
        topic_id: &Identifier,
        partitioning: &Partitioning,
        messages: &mut [IggyMessage],
    ) -> Result<(), IggyError>;
}
```

---

## Summary: Trait Design Checklist

- [ ] Use RPITIT (`impl Future`) instead of `#[async_trait]` when possible
- [ ] Use GATs for lifetime-dependent associated types
- [ ] Create type aliases for complex associated types
- [ ] Hoist complex bounds to `where` clauses
- [ ] Seal traits to prevent external implementations
- [ ] Use marker types for compile-time safety
- [ ] Prefer static dispatch over dynamic dispatch
- [ ] Use associated constants for trait-level configuration
- [ ] Provide default methods for common patterns
