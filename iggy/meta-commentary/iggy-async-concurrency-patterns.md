# Iggy Async & Concurrency Patterns

## Overview

Iggy uses `compio` runtime with `io_uring` for async I/O, implementing sophisticated concurrency patterns for high-throughput message streaming.

---

## 1. Async Runtime: compio over tokio

### Why compio?

- Native `io_uring` support on Linux
- Thread-per-core architecture
- Zero-copy I/O operations

```rust
// Cargo.toml
compio = { version = "0.18.0", features = [
    "runtime", "macros", "io-uring", "time",
    "rustls", "ring", "net", "quic", "tls", "ws", "fs",
] }
```

### Async Test Attribute

```rust
#[compio::test]
async fn test_oneshot_completion_detection() {
    // Test code
}
```

---

## 2. RPITIT - Return Position Impl Trait In Traits

### Pattern: Zero-Cost Async Traits

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

- No heap allocation
- Compiler can inline and optimize
- Native async/await syntax

---

## 3. Channel Patterns

### flume for MPMC Channels

```rust
let (tx, rx) = flume::bounded::<u32>(1024);
```

### crossfire for High-Performance Channels

```rust
// Preferred for production hot paths
use crossfire::{mpsc, mpmc};
```

### async-broadcast for Event Distribution

```rust
pub struct TcpClient {
    events: (Sender<DiagnosticEvent>, Receiver<DiagnosticEvent>),
}

async fn subscribe_events(&self) -> Receiver<DiagnosticEvent> {
    self.events.1.clone()
}
```

### Pattern: Bounded Channels for Backpressure

```rust
// Always use bounded channels in production
let (tx, rx) = mpsc::channel(1024); // Not unbounded!

// Apply timeout on send
match tx.send_timeout(msg, Duration::from_millis(50)) {
    Ok(_) => { /* sent */ },
    Err(_) => { /* apply backpressure strategy */ },
}
```

---

## 4. Cancellation Safety

### Pattern: Spawn for Lock Acquisition

```rust
async fn send_raw(&self, code: u32, payload: Bytes) -> Result<Bytes, IggyError> {
    // SAFETY: we run code holding the `stream` lock in a task
    // so we can't be cancelled while holding the lock.
    tokio::spawn(async move {
        let mut stream = stream.lock().await;
        // ... send/receive logic
    })
    .await
    .map_err(|e| IggyError::TcpError)?
}
```

### Pattern: CancellationToken via AtomicBool

```rust
pub struct IggyConsumer {
    shutdown: Arc<AtomicBool>,
}

impl IggyConsumer {
    pub async fn shutdown(&mut self) -> Result<(), IggyError> {
        if self.shutdown.swap(true, Ordering::Relaxed) {
            return Ok(()); // Already shutting down
        }
        // Cleanup...
    }
}
```

### Pattern: Loop with Shutdown Check

```rust
fn store_offsets_in_background(&self, interval: IggyDuration) {
    let shutdown = self.shutdown.clone();
    tokio::spawn(async move {
        loop {
            sleep(interval.get_duration()).await;
            // ... work ...
            if shutdown.load(Ordering::Relaxed) {
                break;
            }
        }
    });
}
```

---

## 5. Stream Implementation

### Pattern: Implementing futures::Stream

```rust
impl Stream for IggyConsumer {
    type Item = Result<ReceivedMessage, IggyError>;

    fn poll_next(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {
        // Return buffered message if available
        if let Some(message) = self.buffered_messages.pop_front() {
            return Poll::Ready(Some(Ok(ReceivedMessage::new(message))));
        }

        // Create poll future if needed
        if self.poll_future.is_none() {
            let future = self.create_poll_messages_future();
            self.poll_future = Some(Box::pin(future));
        }

        // Poll the future
        while let Some(future) = self.poll_future.as_mut() {
            match future.poll_unpin(cx) {
                Poll::Ready(Ok(polled_messages)) => {
                    // Handle messages
                }
                Poll::Ready(Err(err)) => return Poll::Ready(Some(Err(err))),
                Poll::Pending => return Poll::Pending,
            }
        }
        Poll::Pending
    }
}
```

---

## 6. Lock-Free Atomics

### Pattern: Atomic State Machine

```rust
pub enum ClientState {
    Disconnected = 0,
    Connecting = 1,
    Connected = 2,
    Authenticating = 3,
    Authenticated = 4,
}

// Usage
self.state.store(ClientState::Connected as u8, Ordering::SeqCst);
```

### Pattern: AtomicBool for Flags

```rust
pub struct IggyConsumer {
    shutdown: Arc<AtomicBool>,
    joined_consumer_group: Arc<AtomicBool>,
}

// Atomic swap returns previous value
if self.shutdown.swap(true, Ordering::Relaxed) {
    return Ok(()); // Was already true
}
```

---

## 7. Backpressure Handling

### Pattern: Semaphore-Based Permits

```rust
pub enum BackpressureMode {
    FailImmediately,
    Block,
    BlockWithTimeout(IggyDuration),
}

async fn dispatch(&self, messages: Vec<IggyMessage>) -> Result<(), IggyError> {
    let permit_bytes = match self.bytes_permit.clone().try_acquire_many_owned(...) {
        Ok(perm) => perm,
        Err(_) => match self.config.failure_mode {
            BackpressureMode::FailImmediately => {
                return Err(IggyError::BackgroundSendBufferOverflow);
            }
            BackpressureMode::Block => {
                self.bytes_permit.acquire_many_owned(...).await?
            }
            BackpressureMode::BlockWithTimeout(timeout) => {
                tokio::time::timeout(timeout.get_duration(), 
                    self.bytes_permit.acquire_many_owned(...)
                ).await??
            }
        },
    };
    // ... dispatch with permit
}
```

---

## 8. Graceful Shutdown Pattern

### Phased Shutdown

```rust
pub async fn graceful_shutdown(&self, timeout: Duration) -> bool {
    let start = Instant::now();
    
    // Phase 1: Shutdown continuous and periodic tasks
    for task in &self.continuous_tasks {
        task.shutdown();
    }
    
    // Calculate remaining time
    let elapsed = start.elapsed();
    let remaining = timeout.saturating_sub(elapsed);
    
    // Phase 2: Shutdown oneshot tasks with remaining time
    for task in &self.oneshot_tasks {
        if !task.shutdown_timeout(remaining).await {
            warn!("Oneshot task did not complete in time");
        }
    }
    
    true
}
```

### Consumer Shutdown with Offset Flush

```rust
pub async fn shutdown(&mut self) -> Result<(), IggyError> {
    if self.shutdown.swap(true, Ordering::Relaxed) {
        return Ok(());
    }
    
    // Flush final offsets
    for entry in self.last_consumed_offsets.iter() {
        if consumed_offset > stored_offset {
            let _ = Self::store_consumer_offset(...).await;
        }
    }
    
    // Leave consumer group if applicable
    if self.is_consumer_group && self.joined_consumer_group.load(Ordering::Relaxed) {
        client.leave_consumer_group(...).await?;
    }
    Ok(())
}
```

---

## 9. Leader Redirection Pattern

### Pattern: Cluster-Aware Client

```rust
pub async fn check_and_redirect_to_leader<C: ClusterClient>(
    client: &C,
    current_address: &str,
    transport: TransportProtocol,
) -> Result<Option<String>, IggyError> {
    match client.get_cluster_metadata().await {
        Ok(metadata) => {
            // Process metadata to find leader
            process_cluster_metadata(&metadata, current_address, transport)
        }
        Err(e) => {
            warn!("Failed to get cluster metadata: {}", e);
            Ok(None) // Continue on current node
        }
    }
}
```

---

## 10. Sharding Pattern for Producers

### Pattern: Background Producer with Sharding

```rust
pub enum Sharding {
    Ordered,
    Balanced,
}

async fn dispatch(&self, messages: Vec<IggyMessage>) -> Result<(), IggyError> {
    // Select shard based on sharding strategy
    let shard_ix = self.config.sharding.pick_shard(&messages);
    let shard = &self.shards[shard_ix];
    
    shard.send(ShardMessageWithPermit::new(shard_message, permit_bytes)).await
}
```

---

## 11. Timeout Patterns

### Pattern: Timeout Wrapper for All External Calls

```rust
pub async fn fetch_external_data(url: &str) -> Result<Data> {
    tokio::time::timeout(
        Duration::from_secs(30),
        reqwest::get(url)
    ).await?
}
```

### Pattern: Select with Timeout

```rust
use tokio::select;

loop {
    select! {
        biased;
        maybe = stream.next() => {
            if maybe.is_none() { break; }
        }
        _ = shutdown_token.cancelled() => {
            break;
        }
    }
}
```

---

## Summary: Async Concurrency Checklist

- [ ] Use `compio` for Linux io_uring performance
- [ ] Prefer RPITIT over `#[async_trait]` for internal traits
- [ ] Always use bounded channels with backpressure
- [ ] Spawn tasks for lock acquisition to prevent cancellation issues
- [ ] Use `AtomicBool` for shutdown signals
- [ ] Implement `Stream` for async iteration patterns
- [ ] Implement phased graceful shutdown
- [ ] Apply timeouts to all external I/O
- [ ] Use `select!` with `biased` for deterministic polling
