# Iggy Core Architecture Patterns

## Overview

Iggy is a persistent message streaming platform built from the ground up using a **thread-per-core shared-nothing architecture** with `io_uring` via `compio` runtime. This document captures the idiomatic Rust patterns used throughout the codebase.

---

## 1. Shard-Based Architecture

### Core Concept

Each shard runs on a single-threaded `compio` runtime, eliminating the need for locks within a shard:

```rust
//! Per-shard partition data.
//!
//! Each shard runs on a single-threaded compio runtime, so per-shard data
//! needs NO synchronization.
```

### Pattern: Single-Threaded Interior Mutability

Within shards, use `RefCell` for interior mutability (no need for `Mutex`):

```rust
pub(crate) local_partitions: RefCell<LocalPartitions>,
pub(crate) pending_partition_inits: RefCell<AHashSet<IggyNamespace>>,
```

### Pattern: Cross-Shard Communication via Channels

Shards communicate through message passing, not shared memory:

```rust
pub struct IggyShardBuilder {
    // ...
    connections: Option<Vec<ShardConnector<ShardFrame>>>,
}
```

---

## 2. Left-Right Concurrency Pattern

### Core Concept

The metadata system uses the **Left-Right pattern** for lock-free reads across all shards while maintaining a single writer on shard 0:

```rust
pub fn create_metadata_handles() -> (MetadataWriter, MetadataReadHandle) {
    let (write_handle, read_handle) = left_right::new::<InnerMetadata, MetadataOp>();
    let mut writer = MetadataWriter::new(write_handle);
    writer.publish();
    (writer, read_handle)
}
```

### When to Use

- Multiple readers need consistent snapshots
- Single writer updates state atomically
- Read-heavy workloads where lock contention would be problematic

### Pattern Benefits

1. **Zero-contention reads**: All shards can read metadata simultaneously
2. **Atomic updates**: Writer publishes complete state changes
3. **Memory safe**: No unsafe code required

---

## 3. Lock-Free Data Structures

### DashMap for Shards Table

```rust
shards_table: Option<EternalPtr<DashMap<IggyNamespace, PartitionLocation>>>
```

### Papaya HashMap for Hot Paths

```rust
last_polled_offsets: Arc::new(papaya::HashMap::new()),
```

### Atomic Counters

```rust
// Atomic offsets for lock-free increment
pub struct AtomicOffset {
    value: AtomicU64,
}
```

---

## 4. Task Lifecycle Management

### TaskRegistry Pattern

```rust
enum Kind {
    Continuous,  // Long-running servers (TCP, HTTP, WebSocket)
    Periodic,    // Timed tasks (message saver, cleaner)
    OneShot,     // Single execution tasks
}
```

### Graceful Shutdown with Timeouts

```rust
pub async fn graceful_shutdown(&self, timeout: Duration) -> bool {
    // First shutdown long-running tasks (continuous and periodic)
    // Calculate remaining time for oneshots
    // Then shutdown oneshot tasks with remaining time
}
```

### Critical Task Detection

Mark tasks that should trigger system-wide shutdown on failure:

```rust
registry.spawn_critical("message_saver", task);
```

---

## 5. Segmented Log Architecture

### Pattern: Hybrid Message Storage

```rust
pub struct SegmentedLog<J>
where
    J: Journal + Debug,
{
    journal: J,                              // In-memory recent writes
    _access_map: AllocRingBuffer<usize>,     // Ring buffer for cleanup
    segments: Vec<Segment>,                  // Disk-backed segments
    indexes: Vec<Option<IggyIndexesMut>>,    // Index files
    storage: Vec<Storage>,                   // Storage abstraction
    in_flight: IggyMessagesBatchSetInFlight, // Messages being persisted
}
```

### Poll Strategy: Memory-Disk Hybrid

```rust
pub async fn poll_messages(...) -> Result<(IggyPollMetadata, IggyMessagesBatchSet), IggyError> {
    // Case 0: Journal is empty - check in_flight buffer or disk
    // Case 1: All messages are in journal
    // Case 2: All messages on disk
    // Case 3: Messages span disk and journal boundary
}
```

---

## 6. Consumer Group Rebalancing

### Pattern: Cooperative Rebalancing

Avoid full rebalances by incrementally adjusting assignments:

```rust
pub fn rebalance_cooperative(&mut self) {
    // Step 1: Assign unassigned partitions to idle members
    // Step 2: Mark excess partitions as pending revocation
    // Only revoke when consumer has committed past last poll
}
```

### Pending Revocation Tracking

```rust
pub struct PendingRevocation {
    pub partition_id: PartitionId,
    pub target_slab_id: usize,
    pub target_member_id: usize,
    pub created_at_micros: IggyTimestamp,
}
```

---

## 7. Memory Management Patterns

### Custom Global Allocator

```rust
#[cfg(not(feature = "disable-mimalloc"))]
use mimalloc::MiMalloc;

#[cfg(not(feature = "disable-mimalloc"))]
#[global_allocator]
static GLOBAL: MiMalloc = MiMalloc;
```

### Arc-Based Stats Sharing

```rust
let stream_stats = Arc::new(StreamStats::default());
let topic_stats = Arc::new(TopicStats::new(stream_stats.clone()));
let partition_stats = Arc::new(PartitionStats::new(topic_stats.clone()));
```

### Memory Pooling for Zero-Copy

```rust
pub struct MemoryPool {
    buffers: Mutex<Vec<BytesMut>>,
    buffer_size: usize,
}
```

---

## 8. Security Patterns

### Root User Credential Generation

```rust
pub fn create_root_user() -> User {
    let mut username = env::var(IGGY_ROOT_USERNAME_ENV);
    let mut password = env::var(IGGY_ROOT_PASSWORD_ENV);
    // Validates lengths, generates secure password if not provided
    User::root(&username, &password)
}
```

### Message Encryption Support

```rust
async fn decrypt_messages(
    &self,
    batches: IggyMessagesBatchSet,
    encryptor: &EncryptorKind,
) -> Result<IggyMessagesBatchSet, IggyError> {
    // Decrypts payload, updates headers
}
```

---

## 9. Observability Patterns

### Structured Logging with Tracing

```rust
pub async fn run(self: &Rc<Self>) -> Result<(), IggyError> {
    let now: Instant = Instant::now();
    info!("Starting...");
    // ...
    let elapsed = now.elapsed();
    info!("Initialized in {} ms.", elapsed.as_millis());
}
```

### Instrumented Shutdown

```rust
#[instrument(skip_all, name = "trace_shutdown")]
pub async fn trigger_shutdown(&self) -> bool {
    self.is_shutting_down.store(true, Ordering::SeqCst);
    debug!("Shard {} shutdown state set", self.id);
    self.task_registry.graceful_shutdown(SHUTDOWN_TIMEOUT).await
}
```

---

## 10. Module Organization Principles

### Clear Type Aliases for Domain Clarity

```rust
pub type MetadataReadHandle = left_right::ReadHandle<InnerMetadata>;
pub type StreamId = usize;
pub type TopicId = usize;
pub type PartitionId = usize;
pub type UserId = u32;
pub type ConsumerGroupId = usize;
```

### Re-exports in lib.rs

```rust
pub mod streaming;
pub mod shard;
pub mod metadata;

pub use shard::IggyShard;
pub use metadata::{MetadataWriter, MetadataReadHandle};
```

---

## Summary: Architecture Decision Record

| Decision | Rationale |
|----------|-----------|
| Single-threaded shards | Eliminates lock contention, simpler reasoning |
| Left-Right metadata | Lock-free reads, atomic writes |
| compio + io_uring | Maximum I/O performance on Linux |
| Segmented log | Kafka-proven persistence pattern |
| Cooperative rebalancing | Avoid consumer group pause on topology changes |
| mimalloc | Better memory fragmentation handling |
| Arc-based stats | Zero-contention statistics sharing |
