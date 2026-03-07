# Iggy Testing Patterns

## Overview

Iggy employs comprehensive testing strategies including unit tests, integration tests, BDD tests, and benchmarks.

---

## 1. Unit Test Organization

### Pattern: Inline Tests with cfg(test)

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_identifier_validation() {
        let id = Identifier::numeric(1).unwrap();
        assert!(id.validate().is_ok());
    }

    #[test]
    fn test_invalid_identifier() {
        let result = Identifier::named("");
        assert!(result.is_err());
    }
}
```

### Pattern: Async Tests with compio

```rust
#[cfg(test)]
mod tests {
    #[compio::test]
    async fn test_oneshot_completion_detection() {
        // Async test code
    }
    
    #[compio::test]
    async fn test_timeout_error() {
        // Test timeout handling
    }
}
```

---

## 2. Integration Tests

### Pattern: Scenario-Based Testing

```rust
// core/integration/tests/server/scenarios/authentication_scenario.rs

pub async fn run(harness: &TestHarness) {
    let client = create_client(harness).await;
    
    // Phase 1: Verify ping works without auth
    client.ping().await.expect("ping should work without auth");
    
    // Phase 2: Verify all protected commands fail without auth
    test_all_commands_require_auth(&client).await;
    
    // Phase 3: Login and verify commands work
    let identity = login_root(&client).await.expect("login failed");
    setup_test_resources(&client).await;
    verify_auth_works(&client).await;
}
```

### Pattern: Test Harness

```rust
pub struct TestHarness {
    pub server: IggyServer,
    pub client: IggyClient,
    pub temp_dir: TempDir,
}

impl TestHarness {
    pub async fn new() -> Self {
        let temp_dir = tempfile::tempdir().unwrap();
        let server = IggyServer::start(&temp_dir).await;
        let client = IggyClient::connect(server.address()).await;
        Self { server, client, temp_dir }
    }
}
```

---

## 3. BDD Testing with Cucumber

### Pattern: Feature Files

```gherkin
# bdd/features/messages/send_messages.feature

Feature: Send messages to topic
  As a producer
  I want to send messages to a topic
  So that consumers can read them

  Scenario: Send single message successfully
    Given I am connected to the server
    And I am authenticated as "producer"
    And stream "test_stream" exists
    And topic "test_topic" exists in stream "test_stream"
    When I send message "hello world" to topic "test_topic"
    Then the message should be stored
    And I should receive confirmation
```

### Pattern: Step Definitions

```rust
// bdd/rust/src/steps/message_steps.rs

use cucumber::{given, when, then};

#[given(regex = r"^topic \"(.*)\" exists in stream \"(.*)\"$")]
async fn topic_exists(world: &mut TestWorld, topic: String, stream: String) {
    world.ensure_topic_exists(&stream, &topic).await;
}

#[when(regex = r"^I send message \"(.*)\" to topic \"(.*)\"$")]
async fn send_message(world: &mut TestWorld, payload: String, topic: String) {
    world.send_message(&payload, &topic).await;
}

#[then(regex = r"^the message should be stored$")]
async fn message_stored(world: &mut TestWorld) {
    assert!(world.last_message_stored);
}
```

---

## 4. Mock Patterns

### Pattern: Mock Trait Implementations

```rust
use mockall::automock;

#[automock]
#[async_trait]
pub trait MessageClient: Send + Sync {
    async fn send_messages(&self, ...) -> Result<(), IggyError>;
    async fn poll_messages(&self, ...) -> Result<PolledMessages, IggyError>;
}

// Usage in tests
let mut mock_client = MockMessageClient::new();
mock_client
    .expect_send_messages()
    .returning(|_| Ok(()));
```

---

## 5. Task Registry Testing

### Pattern: Comprehensive Task Testing

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[compio::test]
    async fn test_oneshot_completion_detection() {
        let registry = TaskRegistry::new();
        let completed = Arc::new(AtomicBool::new(false));
        
        registry.spawn_oneshot("test", {
            let completed = completed.clone();
            async move {
                completed.store(true, Ordering::Relaxed);
            }
        });
        
        // Wait for completion
        sleep(Duration::from_millis(100)).await;
        assert!(completed.load(Ordering::Relaxed));
    }
    
    #[compio::test]
    async fn test_timeout_error() {
        let registry = TaskRegistry::new();
        
        registry.spawn_periodic("slow_task", Duration::from_secs(10), || async {
            sleep(Duration::from_secs(100)).await;
        });
        
        let result = registry.graceful_shutdown(Duration::from_millis(50)).await;
        assert!(!result); // Timeout occurred
    }
}
```

---

## 6. Concurrency Testing

### Pattern: Stress Testing with JoinSet

```rust
#[tokio::test]
async fn test_concurrent_read_write_safety() {
    let storage = Arc::new(create_concurrent_storage().await);
    let mut join_set = JoinSet::new();
    
    // Spawn multiple writers
    for i in 0..10 {
        let storage_clone = Arc::clone(&storage);
        join_set.spawn(async move {
            for j in 0..100 {
                let message = create_test_message(i * 100 + j);
                storage_clone.append(message).await.unwrap();
            }
        });
    }
    
    // Spawn multiple readers
    for _ in 0..20 {
        let storage_clone = Arc::clone(&storage);
        join_set.spawn(async move {
            for _ in 0..50 {
                let _ = storage_clone.poll_messages(...).await;
            }
        });
    }
    
    // Wait for all tasks
    while let Some(result) = join_set.join_next().await {
        result.unwrap();
    }
    
    // Verify data consistency
    let final_count = storage.message_count().await.unwrap();
    assert_eq!(final_count, 1000);
}
```

### Pattern: Loom for Model Checking

```rust
#[cfg(loom)]
mod loom_tests {
    use loom::sync::{Arc, Mutex};
    use loom::thread;
    
    #[test]
    fn concurrent_counter() {
        loom::model(|| {
            let counter = Arc::new(Mutex::new(0));
            
            let handles: Vec<_> = (0..2).map(|_| {
                let counter = counter.clone();
                thread::spawn(move || {
                    let mut guard = counter.lock().unwrap();
                    *guard += 1;
                })
            }).collect();
            
            for handle in handles {
                handle.join().unwrap();
            }
            
            assert_eq!(*counter.lock().unwrap(), 2);
        });
    }
}
```

---

## 7. Property-Based Testing

### Pattern: proptest for Invariants

```rust
use proptest::prelude::*;

proptest! {
    #[test]
    fn identifier_roundtrip(value in any::<u32>()) {
        let id = Identifier::numeric(value).unwrap();
        let bytes = id.to_bytes();
        let recovered = Identifier::from_bytes(bytes).unwrap();
        prop_assert_eq!(id, recovered);
    }
    
    #[test]
    fn message_payload_validation(
        payload in ".*",
        max_len in 1usize..10000
    ) {
        let result = validate_payload(&payload, max_len);
        if payload.len() <= max_len && !payload.is_empty() {
            prop_assert!(result.is_ok());
        } else {
            prop_assert!(result.is_err());
        }
    }
}
```

---

## 8. Benchmarking

### Pattern: Criterion Benchmarks

```rust
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn benchmark_message_serialization(c: &mut Criterion) {
    let messages = generate_test_messages(1000);
    
    c.bench_function("serialize_messages", |b| {
        b.iter(|| {
            for message in &messages {
                black_box(message.to_bytes());
            }
        })
    });
}

fn benchmark_partition_polling(c: &mut Criterion) {
    let rt = tokio::runtime::Runtime::new().unwrap();
    let partition = rt.block_on(create_test_partition());
    
    c.bench_function("poll_messages", |b| {
        b.to_async(&rt).iter(|| {
            partition.poll_messages(PollingStrategy::next(), 100)
        })
    });
}

criterion_group!(benches, benchmark_message_serialization, benchmark_partition_polling);
criterion_main!(benches);
```

---

## 9. Test Coverage

### Pattern: cargo-llvm-cov Integration

```toml
# CI configuration
- name: Run coverage
  run: |
    cargo llvm-cov --workspace --branch --fail-under-lines 75
```

### Coverage Requirements

| Component | Minimum Coverage |
|-----------|------------------|
| Error handling | 90% |
| Message serialization | 85% |
| Consumer groups | 80% |
| Core protocol | 85% |

---

## 10. Test Utilities

### Pattern: Test Fixtures

```rust
pub fn create_test_message(payload: &str) -> IggyMessage {
    IggyMessage::builder()
        .payload(payload.as_bytes().to_vec().into())
        .build()
        .unwrap()
}

pub fn create_test_stream(name: &str) -> Stream {
    Stream::new(
        Identifier::named(name).unwrap(),
        1,
    )
}

pub async fn setup_test_environment() -> TestEnvironment {
    let temp_dir = tempfile::tempdir().unwrap();
    let server = IggyServer::start(&temp_dir).await;
    TestEnvironment { server, temp_dir }
}
```

### Pattern: Test Assertions

```rust
pub fn assert_error_code(result: Result<(), IggyError>, expected: u32) {
    match result {
        Err(e) => assert_eq!(e.as_code(), expected),
        Ok(_) => panic!("Expected error with code {}", expected),
    }
}
```

---

## 11. CI Quality Gates

### Pattern: Multi-Stage Testing

```yaml
# .github/workflows/test.yml
jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: cargo test --workspace --lib
      
  integration-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: cargo test --workspace --test '*'
      
  bdd-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: cargo test --package iggy-bdd
      
  coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: cargo llvm-cov --workspace --codecov --output-path codecov.json
```

---

## Summary: Testing Checklist

- [ ] Write inline unit tests with `#[cfg(test)]`
- [ ] Use `#[compio::test]` for async tests
- [ ] Create scenario-based integration tests
- [ ] Use Cucumber for BDD-style tests
- [ ] Mock external dependencies with `mockall`
- [ ] Write stress tests for concurrent code
- [ ] Use `loom` for lock-free data structure verification
- [ ] Add property-based tests with `proptest`
- [ ] Create criterion benchmarks for hot paths
- [ ] Maintain 75%+ branch coverage
- [ ] Run full test suite in CI
