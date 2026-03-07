# Iggy Concurrency Patterns

## Overview

Iggy implements sophisticated concurrency patterns for high-throughput message streaming, balancing performance with safety.

---

## 1. Lock-Free Data Structures

### papaya HashMap

```rust
use papaya::HashMap;

// Lock-free concurrent map
let map: HashMap<K, V> = HashMap::new();
map.pin().insert(key, value);
```

### DashMap for Shards Table

```rust
use dashmap::DashMap;

// Sharded concurrent map
let shards = DashMap::<IggyNamespace, PartitionLocation>::new();
shards.insert(namespace, location);
```

### When to Choose

| Structure | Use Case | Contention |
|-----------|---------|------------|
| papaya | High reads, rare writes | Low |
| DashMap | Balanced reads/writes | Medium |
| std::HashMap + Single-threaded | None |

---

## 2. Left-Right Pattern

### Implementation
```rust
use left_right;

pub fn create_metadata_handles() -> (MetadataWriter, MetadataReadHandle) {
    let (write_handle, read_handle) = left_right::new::<InnerMetadata, MetadataOp>();
    let mut writer = MetadataWriter::new(write_handle);
    writer.publish();
    (writer, read_handle)
}
```

### Benefits
- Zero-contention reads
- Atomic snapshot updates
- Memory safe without unsafe

### When to Use
- Read-heavy workloads
- Single writer (shard 0)
- Need for consistent snapshots

---

## 3. Atomic State Management

### Client State Machine
```rust
pub enum ClientState {
    Disconnected = 0,
    Connecting = 2,
    Connected = 3,
    Authenticating = 4,
    Authenticated = 5,
}

// Thread-safe state
self.state.store(ClientState::Connected as u8, Ordering::SeqCst);
```

### Shutdown Signal
```rust
use std::sync::atomic::{AtomicBool, Ordering};

pub struct ShutdownSignal {
    is_shutdown: AtomicBool,
}

impl ShutdownSignal {
    pub fn new() -> Self {
        Self {
            is_shutdown: AtomicBool::new(false),
        }
    }
    
    pub fn trigger(&self) {
        self.is_shutdown.store(true, Ordering::SeqCst);
    }
    
    pub fn is_shutdown(&self) -> bool {
        self.is_shutdown.load(Ordering::SeqCst)
    }
}
```

---

## 4. Channel Patterns

### Bounded Channels for Backpressure
```rust
use flume::{bounded, Sender, Receiver};

let (tx, rx) = bounded::<Message>(1024);

// Send with timeout
match tx.send_timeout(msg, Duration::from_millis(50)) {
    Ok(_) => { /* sent */ },
    Err(_) => { /* backpressure */ },
}
```

### Async Broadcast for Events
```rust
use async_broadcast::{broadcast, Receiver};

let (tx, rx) = broadcast::<DiagnosticEvent>(16);

// Multiple subscribers
let rx1 = tx.new_receiver();
let rx2 = tx.new_receiver();
```

### Crossbeam for High-Performance
```rust
use crossbeam_channel::{bounded, unbounded};

// Choose based on workload
let (tx, rx) = if needs_backpressure {
    bounded(1024)
} else {
    unbounded()
};
```

---

## 5. Single-Threaded Shard Pattern

### Interior Mutability Without Locks
```rust
use std::cell::RefCell;

pub struct LocalPartition {
    // Safe because each shard is single-threaded
    messages: RefCell<Vec<Message>>,
}

impl LocalPartition {
    pub fn add_message(&self, msg: Message) {
        self.messages.borrow_mut().push(msg);
    }
}
```

### Why It Works
- Each shard runs on dedicated thread
- No cross-shard data access
- compio runtime is single-threaded per shard

---

## 6. Arc-Based Sharing

### Stats Propagation
```rust
use std::sync::Arc;

let stream_stats = Arc::new(StreamStats::default());
let topic_stats = Arc::new(TopicStats::new(stream_stats.clone()));
let partition_stats = Arc::new(PartitionStats::new(topic_stats.clone()));
```

### Shared Configuration
```rust
pub struct SharedConfig {
    inner: Arc<ConfigInner>,
}

impl Clone for SharedConfig {
    fn clone(&self) -> Self {
        Self {
            inner: Arc::clone(&self.inner),
        }
    }
}
```

---

## 7. Task Coordination

### JoinSet for Concurrent Tasks
```rust
use tokio::task::JoinSet;

let mut tasks = JoinSet::new();

for i in 0..10 {
    tasks.spawn(async move {
        process_shard(i).await
    });
}

// Wait for all
while let Some(result) = tasks.join_next().await {
    match result {
        Ok(Ok(_)) => { /* success */ },
        Ok(Err(e)) => { /* task error */ },
        Err(e) => { /* join error */ },
    }
}
```

### Barrier for Synchronization
```rust
use std::sync::Barrier;

let barrier = Arc::new(Barrier::new(num_shards));

for shard in shards {
    let b = barrier.clone();
    thread::spawn(move || {
        // Work...
        b.wait(); // All shards synchronized
    });
}
```

---

## 8. Memory Ordering

### Consistent Ordering
```rust
use std::sync::atomic::Ordering;

// Release semantics for writes
self.value.store(new_value, Ordering::Release);

// Acquire semantics for reads
let value = self.value.load(Ordering::Acquire);

// Sequential consistency for critical sections
self.flag.store(true, Ordering::SeqCst);
```

### When to Use Each
| Ordering | Use Case |
|----------|---------|
| Relaxed | Statistics, counters |
| Release/Acquire | Flag publishing, flag reading |
| SeqCst | Critical synchronization |
| AcqRel | Lock-free algorithms |

---

## 9. Concurrency Testing

### Loom Model Checking
```rust
#[cfg(loom)]
mod loom_tests {
    use loom::sync::{Arc, Mutex};
    
    #[test]
    fn test_mutex_safety() {
        loom::model(|| {
            let m = Arc::new(Mutex::new(0));
            // Test all interleavings
        });
    }
}
```

### Stress Testing
```rust
#[tokio::test(flavor = "multi_thread")]
async fn stress_test() {
    let storage = Arc::new(Storage::new());
    
    let mut tasks = JoinSet::new();
    for _ in 0..100 {
        let s = storage.clone();
        tasks.spawn(async move {
            for _ in 0..1000 {
                s.write(generate_data()).await.unwrap();
            }
        });
    }
    
    while tasks.join_next().await.is_some() {}
}
```

---

## Summary: Concurrency Checklist

- [ ] Use lock-free structures for read-heavy paths
- [ ] Apply Left-Right for metadata
- [ ] Use atomic types for shared state
- [ ] Prefer bounded channels with backpressure
- [ ] Leverage single-threaded shards for lock-free access
- [ ] Share immutable data via Arc
- [ ] Use JoinSet for concurrent task management
- [ ] Apply correct memory ordering
- [ ] Test with loom for correctness
- [ ] Stress test under concurrent load
