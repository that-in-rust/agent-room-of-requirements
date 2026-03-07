# Iggy Performance Patterns

## Overview

Iggy is designed for maximum performance using thread-per-core architecture, io_uring, lock-free data structures, and careful memory management.

---

## 1. Runtime: compio + io_uring

### Why compio over tokio?

- Native io_uring support on Linux
- Thread-per-core shared-nothing design
- Zero-copy I/O operations

```toml
compio = { version = "0.18.0", features = [
    "runtime", "macros", "io-uring", "time",
    "rustls", "ring", "net", "quic", "tls", "ws", "fs",
] }
```

### Usage

```rust
#[compio::main]
async fn main() {
    // Async runtime with io_uring
}

#[compio::test]
async fn test_async() {
    // Test code
}
```

---

## 2. Memory Allocation

### Pattern: mimalloc Global Allocator

```rust
#[cfg(not(feature = "disable-mimalloc"))]
use mimalloc::MiMalloc;

#[cfg(not(feature = "disable-mimalloc"))]
#[global_allocator]
static GLOBAL: MiMalloc = MiMalloc;
```

### Benefits

- Better memory fragmentation handling
- Lower memory overhead
- Consistent allocation performance

---

## 3. Lock-Free Data Structures

### papaya HashMap

```rust
use papaya::HashMap;

let offsets: Arc<HashMap<PartitionId, AtomicU64>> = Arc::new(HashMap::new());

// Lock-free reads
let offset = offsets.pin().get(&partition_id).map(|v| v.load(Ordering::Relaxed));

// Lock-free writes
offsets.pin().insert(partition_id, AtomicU64::new(0));
```

### DashMap for Sharding Table

```rust
use dashmap::DashMap;

let shards: DashMap<StreamId, PartitionLocation> = DashMap::new();
shards.insert(stream_id, location);
```

### left-right for Metadata

```rust
let (writer, reader) = left_right::new::<InnerMetadata, MetadataOp>();

// Readers never block
let metadata = reader.enter();

// Writer publishes atomically
writer.publish();
```

---

## 4. Single-Threaded Shard Design

### Pattern: RefCell Instead of Mutex

```rust
// Within a shard (single-threaded)
pub(crate) local_partitions: RefCell<LocalPartitions>,
pub(crate) pending_partition_inits: RefCell<AHashSet<IggyNamespace>>,
```

### Why

- No lock overhead
- No possibility of deadlock
- Better cache locality

---

## 5. Zero-Copy Operations

### Pattern: Bytes Instead of Vec<u8>

```rust
use bytes::{Bytes, BytesMut};

// Shared ownership, no copy
let shared: Bytes = original.clone(); // O(1)

// Reference counting handles deallocation
```

### Pattern: Slice References

```rust
fn process_messages(messages: &[IggyMessage]) {
    // Zero-copy access
}
```

---

## 6. Atomic Operations

### Pattern: Cache-Line Aligned Atomics

```rust
use std::sync::atomic::{AtomicU64, Ordering};

#[repr(align(64))]
struct CachePadded(AtomicU64);

pub struct Partition {
    current_offset: CachePadded,
    committed_offset: CachePadded,
}
```

### Ordering Strategy

```rust
// Relaxed for counters (no ordering requirement)
counter.fetch_add(1, Ordering::Relaxed);

// Acquire/Release for synchronization
let value = atomic.load(Ordering::Acquire);
atomic.store(new_value, Ordering::Release);

// SeqCst for flags (visibility across all threads)
shutdown.store(true, Ordering::SeqCst);
```

---

## 7. Batch Processing

### Pattern: Vectored I/O

```rust
async fn write_vectored(&self, buffers: &[IoSlice<'_>]) -> Result<usize, IoError> {
    // Single syscall for multiple buffers
}
```

### Pattern: Batch Message Sending

```rust
pub async fn send_messages(
    &self,
    messages: &mut [IggyMessage],  // Batch, not single
) -> Result<(), IggyError>;
```

---

## 8. Memory Pooling

### Pattern: Reusable Buffers

```rust
pub struct MemoryPool {
    buffers: Mutex<Vec<BytesMut>>,
    buffer_size: usize,
}

impl MemoryPool {
    pub fn acquire(&self) -> BytesMut {
        let mut guard = self.buffers.lock();
        guard.pop().unwrap_or_else(|| BytesMut::with_capacity(self.buffer_size))
    }
    
    pub fn release(&self, mut buffer: BytesMut) {
        buffer.clear();
        self.buffers.lock().push(buffer);
    }
}
```

---

## 9. Checksum: blake3

### Pattern: Fast Cryptographic Hash

```rust
use blake3::Hash;

pub fn compute_checksum(data: &[u8]) -> u128 {
    let hash = blake3::hash(data);
    u128::from_be_bytes(hash.as_bytes()[..16].try_into().unwrap())
}
```

### Why blake3

- SIMD-optimized
- Faster than SHA-256
- Parallel implementation

---

## 10. Compile-Time Optimization

### Profile Configuration

```toml
[profile.release]
lto = true              # Link-time optimization
codegen-units = 1       # Single codegen unit for better optimization

[profile.dev.package.argon2]
opt-level = 3           # Optimize crypto even in dev

[profile.dev.package.twox-hash]
opt-level = 3           # Optimize hashing in dev
```

### Selective Optimization

```rust
// Optimize hot paths even in dev
#[inline(always)]
fn fast_hash(data: &[u8]) -> u64 {
    // ...
}
```

---

## 11. Lazy Initialization

### Pattern: OnceLock / LazyLock

```rust
use std::sync::OnceLock;

static CONFIG: OnceLock<ServerConfig> = OnceLock::new();

fn config() -> &'static ServerConfig {
    CONFIG.get_or_init(|| ServerConfig::load().unwrap())
}
```

---

## 12. Avoid Allocations

### Pattern: Reuse Collections

```rust
pub struct MessageBuffer {
    buffer: Vec<IggyMessage>,
}

impl MessageBuffer {
    pub fn clear_and_reuse(&mut self) {
        self.buffer.clear();  // Keep capacity
    }
}
```

### Pattern: Cow for Conditional Ownership

```rust
use std::borrow::Cow;

fn normalize(s: &str) -> Cow<str> {
    if s.contains('\r') {
        Cow::Owned(s.replace('\r', ""))  // Allocate only if needed
    } else {
        Cow::Borrowed(s)                  // Zero-copy
    }
}
```

---

## 13. Ring Buffer for Log

### Pattern: AllocRingBuffer

```rust
use ringbuffer::AllocRingBuffer;

let access_map: AllocRingBuffer<usize> = AllocRingBuffer::with_capacity(1024);
```

---

## 14. Benchmarks

### Pattern: Criterion for Performance Testing

```rust
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn benchmark_message_polling(c: &mut Criterion) {
    let partition = create_test_partition();
    
    c.bench_function("poll_1000_messages", |b| {
        b.to_async(&runtime).iter(|| {
            partition.poll_messages(PollingStrategy::next(), 1000)
        })
    });
}

criterion_group!(benches, benchmark_message_polling);
criterion_main!(benches);
```

### Performance Targets

| Operation | Target |
|-----------|--------|
| Message send | < 1µs p99 |
| Message poll | < 1µs p99 |
| Throughput | > 5M msg/sec |

---

## Summary: Performance Checklist

- [ ] Use compio with io_uring on Linux
- [ ] Set mimalloc as global allocator
- [ ] Use lock-free structures (papaya, DashMap, left-right)
- [ ] Single-threaded shards with RefCell
- [ ] Zero-copy with `Bytes`
- [ ] Cache-line align atomics
- [ ] Batch operations
- [ ] Pool memory for hot paths
- [ ] Use blake3 for checksums
- [ ] Enable LTO in release
- [ ] Benchmark with criterion
