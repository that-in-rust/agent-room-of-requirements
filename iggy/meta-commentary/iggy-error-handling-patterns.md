# Iggy Error Handling Patterns

## Overview

Iggy uses a sophisticated error handling system combining `thiserror`, `error_set`, and explicit error codes for wire protocol stability.

---

## 1. IggyError - The Core Error Type

### Pattern: Discriminant-Based Error Enum

```rust
#[derive(Clone, Debug, Error, EnumDiscriminants, IntoStaticStr, FromRepr, Default)]
#[repr(u32)]
#[strum(serialize_all = "snake_case")]
#[strum_discriminants(
    vis(pub),
    derive(FromRepr, IntoStaticStr),
    strum(serialize_all = "snake_case")
)]
pub enum IggyError {
    #[default]
    #[error("Error")]
    Error = 1,
    
    #[error("Invalid configuration")]
    InvalidConfiguration = 2,
    
    #[error("Invalid identifier")]
    InvalidIdentifier = 3,
    
    // ... 100+ error variants organized by category
}
```

### Key Design Decisions

1. **Clone + Debug**: Enables efficient error propagation through async boundaries
2. **#[repr(u32)]**: Explicit wire format for protocol stability
3. **EnumDiscriminants**: Pattern matching without full equality
4. **IntoStaticStr**: Static string conversion for serialization

### Error Code Categories

| Range | Category |
|-------|----------|
| 1-99 | General/Client errors |
| 100-199 | Connection errors |
| 1000-1999 | Stream errors |
| 2000-2999 | Topic errors |
| 3000-3999 | Partition errors |
| 4000-4999 | Message/Segment errors |
| 5000-5999 | Consumer Group errors |

---

## 2. Rich Error Context

### Pattern: Parameterized Error Variants

```rust
#[error("Consumer group with ID {0} already exists in topic with ID {1}")]
ConsumerGroupIdAlreadyExists(u32, u32),

#[error("Invalid state entry checksum: expected {0}, got {1}, at position {2}")]
InvalidStateEntryChecksum(u64, u64, u64),

#[error("Failed to deserialize payload for command {0}, expected length: {1}, actual: {2}")]
CannotDeserializePayload(u32, usize, usize),
```

### When to Use

- When error context aids debugging
- When error messages need to be reconstructible
- When error comparison should ignore context

---

## 3. Error Conversion Patterns

### From Implementations

```rust
impl From<std::io::Error> for IggyError {
    fn from(error: std::io::Error) -> Self {
        match error.kind() {
            ErrorKind::NotFound => IggyError::FileNotFound,
            ErrorKind::PermissionDenied => IggyError::PermissionDenied,
            _ => IggyError::IoError(error.to_string()),
        }
    }
}
```

### Error Mapping with Context

```rust
let id = self
    .writer()
    .create_consumer_group(...)
    .map_err(|e| {
        if let IggyError::ConsumerGroupNameAlreadyExists(_, _) = &e {
            IggyError::ConsumerGroupNameAlreadyExists(name.clone(), topic_id)
        } else {
            e
        }
    })?;
```

---

## 4. ServerError - Composable Error Domains

### Pattern: error_set! Macro

```rust
error_set!(
    ServerError := NumaError || ConfigurationError || ArchiverError || 
                   ConnectionError || LogError || CompatError || QuicError || ShardError

    IoError := { std::io::Error }
    NumaError := { /* ... */ }
    ConfigurationError := { /* ... */ }
);
```

### Benefits

- Clear error domain boundaries
- Automatic `From` implementations
- Composition over inheritance

---

## 5. Validation Pattern

### Validatable Trait

```rust
pub trait Validatable<E> {
    fn validate(&self) -> Result<(), E>;
}
```

### Implementation Example

```rust
impl Validatable<IggyError> for Identifier {
    fn validate(&self) -> Result<(), IggyError> {
        if self.length == 0 {
            return Err(IggyError::InvalidIdentifier);
        }
        if self.value.is_empty() {
            return Err(IggyError::InvalidIdentifier);
        }
        if self.length != self.value.len() as u8 {
            return Err(IggyError::InvalidIdentifier);
        }
        if self.kind == IdKind::Numeric && self.length != 4 {
            return Err(IggyError::InvalidIdentifier);
        }
        Ok(())
    }
}
```

### Usage Pattern

```rust
let identifier = Identifier::from_bytes(bytes)?;
identifier.validate()?; // Early validation before use
```

---

## 6. Error Recovery Patterns

### Automatic Reconnection

```rust
async fn send_raw_with_response(&self, code: u32, payload: Bytes) -> Result<Bytes, IggyError> {
    let result = self.send_raw(code, payload.clone()).await;
    
    if result.is_ok() {
        return result;
    }

    let error = result.unwrap_err();
    if !matches!(
        error,
        IggyError::Disconnected | IggyError::EmptyResponse | IggyError::Unauthenticated
    ) {
        return Err(error);
    }

    if !self.config.reconnection.enabled {
        return Err(IggyError::Disconnected);
    }

    // Attempt reconnection
    self.disconnect().await?;
    self.connect().await?;
    self.send_raw(code, payload).await
}
```

### Retry with Exponential Backoff

```rust
async fn send_with_retries(&self, max_retries: u32) -> Result<(), IggyError> {
    let mut retries = 0;
    loop {
        match client.send_messages(...).await {
            Ok(_) => return Ok(()),
            Err(error) => {
                retries += 1;
                if retries > max_retries {
                    return Err(error);
                }
                sleep(retry_interval).await;
            }
        }
    }
}
```

---

## 7. Producer Error Context

### Pattern: Wrapping Errors with Context

```rust
fn make_failed_error(&self, cause: IggyError, failed: Vec<IggyMessage>) -> IggyError {
    IggyError::ProducerSendFailed {
        cause: Box::new(cause),
        failed: Arc::new(failed),
        stream_name: self.stream_name.clone(),
        topic_name: self.topic_name.clone(),
    }
}
```

---

## 8. Error Code Serialization

### Pattern: Wire-Compatible Error Codes

```rust
impl IggyError {
    pub fn as_code(&self) -> u32 {
        self.discriminant() as u32
    }
    
    pub fn from_code(code: u32) -> Option<Self> {
        Self::from_repr(code)
    }
}
```

### Binary Protocol Response

```
[4-byte status code][4-byte length][payload]
```

---

## 9. Anti-Patterns to Avoid

### Don't: Unwrap in Production Code

```rust
// BAD
let value = result.unwrap();

// GOOD
let value = result.map_err(|e| IggyError::InvalidConfiguration)?;
```

### Don't: Generic Error Messages

```rust
// BAD
#[error("Invalid input")]
InvalidInput,

// GOOD
#[error("Invalid message payload length: expected <= {0}, got {1}")]
InvalidMessagePayloadLength(usize, usize),
```

### Don't: Swallow Errors

```rust
// BAD
if let Err(_) = operation() { /* ignore */ }

// GOOD
if let Err(e) = operation() {
    warn!("Non-critical operation failed: {}", e);
}
```

---

## Summary: Error Handling Checklist

- [ ] Use discriminant-based enum for wire protocol errors
- [ ] Include rich context in error variants
- [ ] Implement `Validatable` for input types
- [ ] Use `error_set!` for composable server errors
- [ ] Map external errors to domain errors
- [ ] Implement reconnection logic for transient failures
- [ ] Never unwrap in production code paths
- [ ] Document error conditions in API docs
