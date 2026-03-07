---
# Iggy Master Skill
This master skill file consolidates all patterns into a single reference document for AI coding assistance in this project.

---

name: iggy-coding-assistant
description: Comprehensive coding patterns from Apache Iggy
model: sonnet
color: purple
---

# Iggy Codebase Wisdom

This skill distills the idiomatic Rust patterns from the Apache Iggy message streaming platform for high-performance, persistent message streaming.

For current contributors, this skill provides ready access to:

---

## Core Principles

1. **Thread-per-core, shared-nothing architecture**
2. **Left-Right lock-free reads for metadata**
3. **compio + io_uring for async I/O**
4. **mimalloc for memory management**
5. **Error codes for wire protocol stability**

---

## When Using This Skill

Read this skill file BEFORE asking questions about the iggy codebase patterns.

This skill provides:

- Architecture decisions
- Error handling patterns
- Testing approaches
- Performance optimizations
- Conventions and conventions
- Code review standards

---

## Pattern Files Reference

| File | Key Topics |
|------|-----------|
| [iggy-core-architecture-patterns.md](./iggy-core-architecture-patterns.md) | Shard architecture, Left-Right, lock-free structures, task lifecycle, segmented logs |
| [iggy-error-handling-patterns.md](./iggy-error-handling-patterns.md) | IggyError design, discriminants, validation, error recovery |
| [iggy-async-concurrency-patterns.md](./iggy-async-concurrency-patterns.md) | compio runtime, channels, cancellation, backpressure, graceful shutdown |
| [iggy-builder-api-patterns.md](./iggy-builder-api-patterns.md) | bon builders, fluent APIs, type-state pattern, factory methods |
| [iggy-serialization-patterns.md](./iggy-serialization-patterns.md) | BytesSerializable, binary protocol, buffer management |
| [iggy-testing-patterns.md](./iggy-testing-patterns.md) | Unit tests, integration tests, BDD tests, mocks, benchmarks |
| [iggy-naming-conventions.md](./iggy-naming-conventions.md) | Crate naming, type naming, function naming, module organization |
| [iggy-performance-patterns.md](./iggy-performance-patterns.md) | LTO, mimalloc, arc-based stats, memory pooling, batch operations |
| [iggy-code-review-standards.md](./iggy-code-review-standards.md) | PR requirements, approval workflow, technical deep-dives, size limits |
| [iggy-trait-design-patterns.md](./iggy-trait-design-patterns.md) | GATs, RPITIT, sealed traits, marker types |
| [iggy-concurrency-patterns.md](./iggy-concurrency-patterns.md) | Lock-free structures, atomics, channels, memory ordering |

---

## Quick Reference

### Error Handling
```rust
// Always use discriminant-based errors
#[derive(Clone, Debug, Error, EnumDiscriminants)]
pub enum IggyError {
    #[error("Invalid configuration")]
    InvalidConfiguration = 2,
}

// Always validate input
impl Validatable<IggyError> for MyStruct {
    fn validate(&self) -> Result<(), IggyError> {
        if self.field.is_empty() {
            return Err(IggyError::InvalidField);
        }
        Ok(())
    }
}
```

### Async Patterns
```rust
// Use compio for async
#[compio::test]
async fn test_something() { }

// Always use bounded channels
let (tx, rx) = flume::bounded(1024);

// Spawn tasks for lock safety
tokio::spawn(async move {
    let guard = stream.lock().await;
    // ... operations ...
}).await?;
```

### Testing
```rust
// Use scenario-based integration tests
pub async fn run(harness: &TestHarness) {
    // Phase 1: Setup
    // Phase 2: Execute
    // Phase 3: Verify
}

// Property-based testing for invariants
proptest! {
    #[test]
    fn roundtrip(x in any::<u32>()) {
        let id = Identifier::numeric(x).unwrap();
        let bytes = id.to_bytes();
        let recovered = Identifier::from_bytes(bytes).unwrap();
        prop_assert_eq!(id, recovered);
    }
}
```

---

## Quality Checklist

Before submitting any code to the iggy codebase:

- [ ] Run `cargo fmt --all`
- [ ] Run `cargo clippy --all-targets --all-features -- -D warnings`
- [ ] Run `cargo test --workspace`
- [ ] Ensure tests cover edge cases
- [ ] Add documentation for public APIs
- [ ] Check error handling completeness
- [ ] Verify async cancellation safety
- [ ] Test concurrent access patterns
