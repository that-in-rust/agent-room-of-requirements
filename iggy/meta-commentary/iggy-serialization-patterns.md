# Iggy Serialization Patterns

## Overview

Iggy implements custom binary serialization for high-performance wire protocol, using `Bytes` and `BytesMut` from the `bytes` crate for zero-copy operations.

---

## 1. BytesSerializable Trait

### Core Interface

```rust
pub trait BytesSerializable {
    fn to_bytes(&self) -> Bytes;
    fn from_bytes(bytes: Bytes) -> Result<Self, IggyError>
    where
        Self: Sized;
    
    fn write_to_buffer(&self, _buf: &mut BytesMut) { 
        unimplemented!(); 
    }
    
    fn get_buffer_size(&self) -> usize { 
        unimplemented!(); 
    }
}
```

### Implementation Pattern

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
        let kind = IdKind::from_code(
            *bytes.first().ok_or(IggyError::InvalidIdentifier)?
        )?;
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

## 2. Binary Protocol Frame Format

### Request Frame

```
[4-byte length][4-byte command code][payload]
```

### Response Frame

```
[4-byte status][4-byte length][payload]
```

### Constants

```rust
const REQUEST_INITIAL_BYTES_LENGTH: usize = 4;
const RESPONSE_INITIAL_BYTES_LENGTH: usize = 8;
```

### Send Pattern

```rust
async fn send_raw(&self, code: u32, payload: Bytes) -> Result<Bytes, IggyError> {
    let mut stream_guard = self.stream.lock().await;
    let stream = stream_guard.as_mut().ok_or_else(|| IggyError::NotConnected)?;
    
    let payload_length = payload.len() + REQUEST_INITIAL_BYTES_LENGTH;
    let mut request = BytesMut::with_capacity(4 + REQUEST_INITIAL_BYTES_LENGTH + payload.len());
    request.put_u32_le(payload_length as u32);
    request.put_u32_le(code);
    request.put_slice(&payload);
    
    stream.write(&request).await?;
    stream.flush().await?;
    
    // Read response
    let mut response_header = [0u8; RESPONSE_INITIAL_BYTES_LENGTH];
    stream.read_exact(&mut response_header).await?;
    
    let status = u32::from_le_bytes(response_header[0..4].try_into()?);
    let length = u32::from_le_bytes(response_header[4..8].try_into()?) as usize;
    
    if status != 0 {
        return Err(IggyError::from_code(status).unwrap_or(IggyError::Error));
    }
    
    let mut response_payload = vec![0u8; length];
    stream.read_exact(&mut response_payload).await?;
    
    Ok(Bytes::from(response_payload))
}
```

---

## 3. BytesMut Buffer Management

### Pattern: Pre-sized Buffers

```rust
let mut buf = BytesMut::with_capacity(expected_size);
// Or
let mut buf = BytesMut::zeroed(required_size);
```

### Pattern: Put Methods

```rust
// Fixed-size integers
buf.put_u8(value);
buf.put_u32_le(value);
buf.put_u64_le(value);
buf.put_u128_le(value);

// Variable-size data
buf.put_slice(data);
buf.put_bytes(byte, count);
```

### Pattern: Freeze to Bytes

```rust
let bytes: Bytes = buf.freeze();
```

---

## 4. Command Serialization

### Command Trait

```rust
pub trait Command: Validatable<IggyError> + Send + Sync {
    fn code(&self) -> u32;
    fn to_bytes(&self) -> Result<Bytes, IggyError>;
    fn from_bytes(bytes: Bytes) -> Result<Self, IggyError>
    where
        Self: Sized;
}
```

### Example Command

```rust
#[derive(Debug, Serialize, Deserialize)]
pub struct CreateUser {
    pub username: String,
    pub password: String,
    pub status: UserStatus,
    pub permissions: Permissions,
}

impl Command for CreateUser {
    fn code(&self) -> u32 {
        CommandCode::CreateUser.as_code()
    }
    
    fn to_bytes(&self) -> Result<Bytes, IggyError> {
        let mut buf = BytesMut::new();
        buf.put_u8(self.username.len() as u8);
        buf.put_slice(self.username.as_bytes());
        buf.put_u8(self.password.len() as u8);
        buf.put_slice(self.password.as_bytes());
        buf.put_u8(self.status.as_code());
        // ... permissions
        Ok(buf.freeze())
    }
    
    fn from_bytes(bytes: Bytes) -> Result<Self, IggyError> {
        let mut cursor = 0;
        let username_len = bytes[cursor] as usize;
        cursor += 1;
        let username = String::from_utf8(
            bytes[cursor..cursor + username_len].to_vec()
        )?;
        cursor += username_len;
        // ... rest of parsing
        Ok(Self { username, password, status, permissions })
    }
}
```

---

## 5. Message Serialization

### Message Header Format

```rust
pub struct MessageHeader {
    pub offset: u64,           // 8 bytes
    pub id: u128,              // 16 bytes
    pub timestamp: u64,        // 8 bytes
    pub checksum: u128,        // 16 bytes
    pub origin_timestamp: u64, // 8 bytes
    pub headers_length: u16,   // 2 bytes
    pub payload_length: u32,   // 4 bytes
}
```

### IggyMessage Serialization

```rust
impl BytesSerializable for IggyMessage {
    fn to_bytes(&self) -> Bytes {
        let headers_bytes = self.serialize_headers();
        let total_size = HEADER_SIZE + headers_bytes.len() + self.payload.len();
        
        let mut buf = BytesMut::with_capacity(total_size);
        
        // Header fields
        buf.put_u64_le(self.header.offset);
        buf.put_u128_le(self.header.id);
        buf.put_u64_le(self.header.timestamp);
        buf.put_u128_le(self.header.checksum);
        buf.put_u64_le(self.header.origin_timestamp);
        buf.put_u16_le(headers_bytes.len() as u16);
        buf.put_u32_le(self.payload.len() as u32);
        
        // Headers (optional)
        if !headers_bytes.is_empty() {
            buf.put_slice(&headers_bytes);
        }
        
        // Payload
        buf.put_slice(&self.payload);
        
        buf.freeze()
    }
}
```

---

## 6. Serde for Configuration

### Pattern: serde with SerdeJsonValue

```rust
#[derive(Debug, Serialize, Deserialize)]
pub struct StreamConfig {
    #[serde(with = "SerdeJsonValue")]
    pub max_topics: u32,
    #[serde(with = "IggyDuration")]
    pub retention: IggyDuration,
}
```

### Custom Deserializers

```rust
pub mod IggyDuration {
    use serde::{Deserialize, Deserializer, Serializer};
    
    pub fn serialize<S>(value: &IggyDuration, serializer: S) -> Result<S::Ok, S::Error>
    where S: Serializer {
        serializer.serialize_str(&value.to_string())
    }
    
    pub fn deserialize<'de, D>(deserializer: D) -> Result<IggyDuration, D::Error>
    where D: Deserializer<'de> {
        let s = String::deserialize(deserializer)?;
        IggyDuration::from_str(&s).map_err(serde::de::Error::custom)
    }
}
```

---

## 7. Batch Serialization

### Pattern: IggyMessagesBatch

```rust
pub struct IggyMessagesBatch {
    pub base_offset: u64,
    pub messages: Vec<IggyMessage>,
}

impl BytesSerializable for IggyMessagesBatch {
    fn to_bytes(&self) -> Bytes {
        let messages_size: usize = self.messages.iter()
            .map(|m| m.get_buffer_size())
            .sum();
        
        let mut buf = BytesMut::with_capacity(8 + 4 + messages_size);
        buf.put_u64_le(self.base_offset);
        buf.put_u32_le(self.messages.len() as u32);
        
        for message in &self.messages {
            message.write_to_buffer(&mut buf);
        }
        
        buf.freeze()
    }
}
```

---

## 8. Flatbuffers Integration

### Pattern: Generated Code

```rust
// Generated from .fbs schema
pub mod generated {
    include!(concat!(env!("OUT_DIR"), "/flatbuffers/messages_generated.rs"));
}

// Usage
let builder = flatbuffers::FlatBufferBuilder::new();
let message = generated::Message::create(&mut builder, &args);
```

---

## 9. Checksum Computation

### Pattern: blake3 for Integrity

```rust
use blake3::Hash;

pub fn compute_checksum(data: &[u8]) -> u128 {
    let hash = blake3::hash(data);
    u128::from_be_bytes(hash.as_bytes()[..16].try_into().unwrap())
}
```

---

## 10. Zero-Copy Patterns

### Pattern: Slice References

```rust
pub struct IggyMessagesBatchSet {
    pub batches: Vec<IggyMessagesBatch>,
}

impl IggyMessagesBatchSet {
    pub fn as_slice(&self) -> &[u8] {
        // Zero-copy access to underlying bytes
    }
}
```

---

## Summary: Serialization Checklist

- [ ] Implement `BytesSerializable` for wire types
- [ ] Use `BytesMut` for building, `Bytes` for sharing
- [ ] Pre-size buffers with `with_capacity`
- [ ] Use little-endian for wire format
- [ ] Include length prefixes for variable-size fields
- [ ] Validate all parsed data
- [ ] Use blake3 for checksums
- [ ] Consider flatbuffers for schema evolution
