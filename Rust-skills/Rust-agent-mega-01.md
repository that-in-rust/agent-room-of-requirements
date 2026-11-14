# Rust Agent Mega 01

One file for an AI coding agent that plans, writes, reviews or hardens Rust: libraries, CLIs,
async services, web backends, parsers, FFI wrappers and Tauri desktop apps. Read section 1
first; it routes you to the sections a task needs.

## 1. Operating principles and workflow

Rust work is not only a syntax problem. For every task decide three things before writing code:

1. what must be specified;
2. what must be designed at the type and boundary level;
3. what must be verified before the result can be trusted.

The aim is a decision-complete work packet or implementation that stays correct beyond the happy path.

### Default workflow

1. **Classify the task.** Name the component type first: library, CLI, async service, backend, parser or protocol, FFI wrapper, Tauri app, or review. Decide whether the main risk is ambiguity, design, reliability or review depth, and pick the primary work mode (section 2).
2. **Write executable requirements** (section 3). Reject vague claims such as "faster" or "more reliable" unless they carry a threshold.
3. **Define the architecture before coding** (section 4): layers, and trait seams where substitution or testability matters.
4. **Choose the verification mix deliberately** (section 5). Match tests to the real risk surface; do not default to unit tests only.
5. **Apply the reliability rules** (sections 6 to 10).
6. **Apply local conventions selectively** (section 12).
7. **Run quality gates and anti-pattern checks before handoff** (sections 13 and 16).

### Guardrails

- Keep invalid states unrepresentable where practical.
- Treat async, cancellation and concurrency as correctness problems, not only performance concerns.
- Do not force every repo-local convention onto every Rust task; use the lightest rule set that preserves correctness and compatibility.
- Do not recommend unsafe, lock-free or proc-macro-heavy designs as defaults; use them only when the task truly requires them.
- Stay skeptical about: malformed input, non-UTF-8 boundaries, backpressure, cancellation, semver surface changes, and detached task lifecycles.

- Prefer APIs that make misuse harder than correct use.
- Parse, don't validate: turn raw input into a validated newtype once, at the boundary.
- Keep error surfaces actionable and boundary-aware.
- Fence unsafe code tightly and document the invariants it relies on.
- Ask throughout: what fails here under malformed input, cancellation, backpressure, non-UTF-8 data, concurrency, or API evolution?
- Before handoff, reread the anti-patterns (section 13) and the default reliability stack.

- Require measurable evidence for performance claims.
- Stress-test shared state and cancellation paths in async and concurrent code.
- Keep docs and tests synchronized with behavior changes.
- For MVP work, prefer battle-tested crates over speculative abstractions.

- Prefer patterns that reduce bug classes, misuse and ambiguous failure behavior over patterns that merely look advanced. A pattern earns its place when it prevents a mistake at compile time, narrows API misuse, gives better diagnostics when things still fail, behaves well under async, concurrency and cancellation, and shows up in serious production code.
- The biggest reliability gaps are at failure boundaries, not in syntax: public API evolution without semver traps, typed error design versus app-level aggregation, byte-safe diagnostics when UTF-8 assumptions break, async cancellation with backpressure and structured shutdown, cancel-safe futures inside `select!`, concurrency verification beyond "it passed once", panic-free slicing and offsets on external input, compile-fail tests and fuzzing, tracing and secret handling and supply-chain gates, and types that make incorrect states unrepresentable.
- Tell repo-local conventions (four-word naming, the executable requirements format, one feature per version, Mermaid-only docs) apart from general Rust practice (typed boundaries and newtypes, typed library errors, no blocking in async, cancel-safe `select!`, `loom`, `proptest`, doctests, compile-fail tests, `#[non_exhaustive]`, `Cow`, `OnceLock`, `ExitCode`, `tracing`). The general practice applies everywhere.
- This file covers libraries, CLIs, async services, application backends, moderately low-level systems code and FFI wrappers with contained unsafe. It is not a specialist manual for compiler internals, kernel-grade lock-free systems, deeply embedded no-std firmware or advanced proc-macro internals.

### Decision ladder for any Rust task

Work down this ladder; do not pick patterns at random.

1. Classify the code: library, binary, async service, FFI wrapper, proc-macro or low-level systems component.
2. Choose the ownership surface: borrowing, owned values, shared ownership or type-state.
3. Choose the error surface: typed library error, app-level aggregation or rich binary diagnostics.
4. Choose the concurrency surface: sync, async, channels, cancellation or structured task ownership.
5. Choose the public API stability surface: `#[non_exhaustive]`, additive features, sealed traits, coherence-safe extension points.
6. Choose the verification mix: unit, doctest, compile-fail, property, fuzz, `loom`, coverage gates.
7. If unsafe remains necessary: minimize the block, document the invariant, and verify with Miri or an equivalent.

Reach for the simplest pattern that preserves correctness boundaries, not the most impressive one.

Powerful techniques that are not first bets, because they are niche or easy to misapply:

- allocator overrides as a general default
- `ManuallyDrop` for compile-time or micro-optimization purposes
- proc-macro internals beyond hygiene, spans and diagnostics
- lock-free building blocks without a verification plan
- pinning tricks beyond safe projection and clear containment
- specialization-related designs in public crates

Correctness is won or lost in public API commitments, error boundary design, async cancellation and concurrency semantics, executable verification, and operational behavior after the code ships.

### Priorities by task type

| Task type | Prioritize |
| --- | --- |
| Library or public API | Borrowed inputs and explicit conversions; newtypes and invalid-states-unrepresentable design; typed library errors; semver-safe surface design; doctest and compile-fail coverage for misuse contracts |
| CLI or binary | Explicit requirement contracts for user-visible behavior; actionable diagnostics; `ExitCode` or equivalent boundary behavior; integration tests and release gates |
| Async service or backend | L1/L2/L3 separation; typed boundary parsing and context layering; no blocking and no lock guards across `.await`; bounded concurrency, cancellation and shutdown behavior; stress, property or `loom` coverage when shared state is involved |
| Parser or protocol boundary | Panic-free parsing and slicing; binary-safe diagnostics for non-UTF-8 paths; property tests, fuzzing and round-trip guarantees; explicit ownership and allocation choices |
| FFI or unsafe boundary | Minimal unsafe surface; explicit invariant documentation; layout, nullability and unwind boundary discipline; `Miri` or equivalent verification when possible |
| Review or hardening pass | Misuse resistance; error surface clarity; cancellation and lifecycle ownership; anti-pattern detection; final gate completeness |

### Default reliability stack

If you do not know what to prioritize, work down this list:

1. Model invariants with newtypes, enums and explicit conversions.
2. Keep library errors typed and application errors contextual.
3. Make async code cancel-safe, bounded and non-blocking.
4. Remove panic edges from parsing, slicing and boundary arithmetic.
5. Turn examples, invariants and misuse cases into tests.
6. Keep unsafe small, justified and verified.
7. Make observability and secret discipline part of the design.

### The vital 20 percent

About 20 percent of Rust patterns cover almost all production code:

- **L1:** ownership and borrowing, RAII, `Result`/`Option`, newtypes.
- **L2:** iterator patterns, smart pointers (`Arc`/`Rc`), error propagation with `?`.
- **L3:** async/await, derive macros, established crate patterns.

Compile-first strategy: use idioms that lean on the type system, make invalid states unrepresentable, and let the compiler catch errors before runtime.

### MVP-first rigor

Proven architectures beat theoretical abstractions for MVP delivery.

1. Model the architecture against the real constraints before implementing.
2. Use battle-tested libraries with known performance characteristics, and validate library choices with micro-benchmarks.
3. Back every timing and memory constraint with an automated test, written before the implementation.
4. Keep locking single-responsibility; avoid coordination between multiple locks.
5. Implement concretely for the MVP; add abstractions later.

Apply it when performance constraints are non-negotiable, the system must handle real-world complexity from day one, concurrent access patterns are well defined, memory or CPU is constrained, or behavior must be predictable and measurable. Do not apply it to prototypes, flexible performance requirements, genuinely simple systems or exploration work.

Every performance-critical operation gets a contract test:

```rust
#[test]
fn test_operation_performance_contract() {
    // Setup: Create realistic test conditions
    // Action: Execute the operation under test
    // Assert: Verify timing constraint + correctness
    // Document: Why this constraint matters
}
```

## 2. Work modes and output contract

Choose one or more modes before planning or coding.

| Mode | Use when |
| --- | --- |
| Spec Mode | The request is vague, acceptance criteria are missing, success is not measurable yet, or the work needs `REQ-RUST-*` contracts first. Emphasis: requirement contracts, acceptance criteria, traceability |
| Delivery Mode | The task needs layer boundaries, trait seams, TDD order, decomposition and implementation sequencing |
| Reliability Mode | The main risk is correctness under stress or change: public API design, error surfaces, async and cancellation, concurrency, diagnostics, unsafe, FFI or release gates |
| Review Mode | The task is a code or design review or a hardening pass. Emphasis: anti-patterns, diagnostics, semver, misuse resistance |

Default combinations:

- vague feature request: Spec + Delivery
- library or public API work: Spec + Reliability
- async service, parser or protocol work: Delivery + Reliability
- review or hardening pass: Review + Reliability

### Output contract

Return results in this order:

1. Rust Work Mode
2. Executable Requirements
3. Rust Design (L1/L2/L3 + Traits)
4. Verification Matrix
5. Implementation Plan
6. Quality Gate Results
7. Open Questions

Trace every requirement to a test in a concise table:

| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |

## 3. Executable specifications

- Give every requirement an identifier of the form `REQ-RUST-<NNN>.<REV>`.
- Express behavior as `WHEN ... THEN ... SHALL`.
- A requirement without a measurable threshold or an observable effect is not a requirement yet; send it back.

### Requirement contract template

```markdown

- Give non-functional claims explicit units (`us`, `ms`, `MB`, `ops/s`).

- Split functional from non-functional requirements when they would otherwise blur together.
- Use `REQ-RUST-*` identifiers for Rust work even when the user starts with a generic request.

### Contracts on the function itself

User stories are written for human conversation; an agent cannot ask clarifying questions, so it needs an explicit contract. Put preconditions, postconditions and error conditions on the function, and validate every claim with an automated test.

```rust
// Bad: "As a user, I want to send messages"
// Good: executable specification with contracts

/// Message creation with deduplication contract
///
/// # Preconditions
/// - User authenticated with room access
/// - Content: 1-10000 chars, sanitized HTML
/// - client_message_id: valid UUID
///
/// # Postconditions
/// - Returns Ok(Message<Persisted>) on success
/// - Inserts row into 'messages' table
/// - Updates room.last_message_at timestamp
/// - Broadcasts to room subscribers via WebSocket
/// - Deduplication: returns existing if client_message_id exists
///
/// # Error Conditions
/// - MessageError::Authorization if user lacks room access
/// - MessageError::InvalidContent if content violates constraints
/// - MessageError::Database on persistence failure
pub async fn create_message_with_deduplication(
    &self,
    content: String,
    room_id: RoomId,
    user_id: UserId,
    client_message_id: Uuid,
) -> Result<Message<Persisted>, MessageError>;
```

Specification levels, from widest to narrowest:

- **Constraints:** system-wide invariants and architectural rules.
- **Architecture:** complete data models, error hierarchies and interface contracts.
- **Modules:** method-level contracts, built with STUB, RED, GREEN, REFACTOR.
- **User journeys:** end-to-end behavioral confirmation.

Acceptance criteria name the command, the input and the bound:

```markdown
1. WHEN I run `parseltongue ingest <file>` THEN the system SHALL parse separated dump format with FILE: markers and extract all Rust interface signatures using `syn` crate
2. WHEN processing a 2.1MB Rust code dump THEN the system SHALL complete ISG construction in less than 5 seconds
```

In the design phase, write the test plan next to the interface:

```rust
/// Test Plan for MessageService
///
/// Scenario 1: Successful Message Creation
/// Given: valid user in room and valid content
/// When: create_message_with_deduplication is called
/// Then: returns Ok(Message<Persisted>) and broadcasts via WebSocket
///
/// Scenario 2: Deduplication
/// Given: message with client_message_id X already exists
/// When: new message with same client ID X is created
/// Then: returns Ok(existing Message) - no duplicate created
```

Keep code and documentation tied together: test names carry the requirement id, and doc examples are executable.

```rust
#[test]
fn test_blast_radius_performance_req_mvp_003() { // References REQ-MVP-003.0
    // Test validates <500us execution time requirement
}

/// # Example
/// ```rust
/// let result = storage.calculate_blast_radius(start_hash, 3).await?;
/// assert!(result.len() <= 1000); // Bounded result size
/// ```
```

### Vague-to-executable rewrites

| Vague statement | Executable rewrite |
| --- | --- |
| "Make it faster." | "Reduce p99 latency from 5ms to less than 1ms for 10k entities." |
| "Improve reliability." | "Return typed validation errors for malformed input without panics or detached task leaks." |
| "Handle async correctly." | "Propagate cancellation, avoid blocking in async contexts, and keep lock guards out of `.await`." |
| "Make the API cleaner." | "Accept borrowed inputs, preserve semver-safe public types, and reject invalid states at construction time." |

### Work packet template

Use this shape when a request is not ready for immediate coding:

```markdown
## Rust Work Mode
- Spec Mode
- Delivery Mode

## Executable Requirements
### REQ-RUST-001.0: <title>
**WHEN** ...
**THEN** the system SHALL ...
**AND** SHALL ...
**SHALL** ...

## Rust Design (L1/L2/L3 + Traits)
- L1 core:
- L2 std:
- L3 external:
- Trait seams:

## Verification Matrix
| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |

## Implementation Plan
1. STUB
2. RED
3. GREEN
4. REFACTOR
5. VERIFY

## Quality Gate Results
- fmt:
- clippy:
- tests:
- build:
```
### REQ-RUST-001.0: <short title>

**WHEN** <trigger or input condition>
**THEN** the system SHALL <primary behavior>
**AND** SHALL <secondary measurable behavior>
**SHALL** <edge-case or default behavior>
```

- Keep each `SHALL` independently testable.
- Use explicit units for latency, memory, throughput, retries and concurrency limits.
- Split requirements; do not stack unrelated behavior into one clause.

## 4. Architecture and boundaries

Plan the design before coding.

| Layer | Role | Question to ask |
| --- | --- | --- |
| L1 Core | Domain invariants, types, traits, protocol and state rules. Depends only on `core` or dependency-light standard types | What must stay stable, testable, runtime-agnostic and easy to trust? |
| L2 Std | Collections, ownership orchestration, error composition, iterators, sync primitives. Depends on the Rust standard library | What orchestration belongs in Rust std without framework coupling? |
| L3 External | Async runtime, database, HTTP, serialization, tracing, FFI adapters. Depends on external crates and runtime integration | What touches the outside world and should stay behind traits or adapters? |

- Keep L3 dependencies out of L1.
- Push validated types and invariants as low in the stack as practical.
- Add trait seams around time, randomness, storage, transport and runtime integration when substitution matters.

### Trait-first design

Define the trait before the concrete adapter when IO or adapters should be isolated from domain logic, when the task needs test doubles or integration seams, when public behavior should be settled before storage or transport details, or when infrastructure dependencies would otherwise leak into core logic.

```rust
pub trait EntityStoreBehavior {
    fn load_entity_by_id(
        &self,
        entity_id: EntityId,
    ) -> Result<Option<StoredEntity>, EntityStoreError>;
}

pub struct EntityProcessorService<S: EntityStoreBehavior> {
    store: std::sync::Arc<S>,
}
```

A behavior trait over borrowed input:

```rust
pub trait EntityProcessorBehavior {
    fn process_domain_entities_only(
        &self,
        input: &[DomainEntity],
    ) -> Result<Vec<ProcessedEntity>, ProcessingError>;
}
```

- Keep domain logic testable without network, database or runtime dependencies.

### Layer and dependency examples

```rust
// L1: Core Language Features (no_std compatible)
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct SigHash(pub u128); // Newtype for type safety

// L2: Standard Library Idioms
use std::sync::Arc;
use std::collections::HashMap;

// L3: External Ecosystem
use tokio::sync::RwLock;
use serde::{Serialize, Deserialize};
```

- **L1 Core:** ownership, lifetimes, traits, `Result`/`Option`, RAII, newtypes.
- **L2 Standard:** collections, iterators, smart pointers, thread safety (`Send`/`Sync`).
- **L3 External:** async runtime (Tokio), serialization (Serde), databases (SQLx).

Depend on traits, not concrete types:

```rust
// Bad: hard dependencies
pub struct SystemComponent {
    database: SqliteConnection,
    file_watcher: NotifyWatcher,
}

// Good: trait-based dependencies
pub struct SystemComponent<D, F>
where
    D: DatabaseProvider + Send + Sync,
    F: FileWatchProvider + Send + Sync,
{
    database: Arc<D>,
    file_watcher: Arc<F>,
}

// Production and test implementations
pub type ProductionSystem = SystemComponent<SqliteDatabase, NotifyFileWatcher>;
pub type TestSystem = SystemComponent<MockDatabase, MockFileWatcher>;
```

Manage every resource with RAII, releasing it in `Drop`:

```rust
pub struct ResourceManager {
    connection: Option<Connection>,
    watcher: Option<FileWatcher>,
    _cleanup: CleanupGuard,
}

impl Drop for ResourceManager {
    fn drop(&mut self) {
        if let Some(conn) = self.connection.take() {
            if let Err(e) = conn.close() {
                eprintln!("Failed to close connection: {}", e);
            }
        }
    }
}
```

Model real-world complexity, not a simplified example:

```rust
// Bad: oversimplified
pub struct Function {
    pub name: String,
    pub signature: String,
}

// Good: handles real complexity
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct RustFunction {
    pub name: InternedString,
    pub signature: RustSignature,
    pub generics: Option<GenericParams>,
    pub where_clause: Option<WhereClause>,
    pub visibility: Visibility,
    pub async_kind: AsyncKind,
}

// Test with real-world complexity
#[test]
fn test_complex_generic_parsing() {
    let code = r#"
        impl<H, S> ErasedIntoRoute<S, Infallible> for MakeErasedHandler<H, S>
        where
            H: Clone + Send + Sync + 'static,
            S: 'static,
        {
            fn into_route(self) -> Route { todo!() }
        }
    "#;

    let parsed = parse_rust_code(code).unwrap();
    let impl_node = parsed.find_impl_node().unwrap();

    assert!(impl_node.generics.is_some());
    assert!(impl_node.where_clause.is_some());
    assert_eq!(impl_node.generics.unwrap().params.len(), 2); // H, S
}
```

### Embedded template (Embassy, no_std)

```rust
#![no_std]
#![no_main]

use embassy_executor::Spawner;
use embassy_time::{Duration, Timer};
use {defmt_rtt as _, panic_probe as _};

#[embassy_executor::main]
async fn main(spawner: Spawner) {
    let p = embassy_stm32::init(Default::default());
    
    // Spawn concurrent tasks
    spawner.spawn(blink_task(p.PA5)).unwrap();
    spawner.spawn(sensor_task(p.PA0)).unwrap();
    
    // Main loop
    loop {
        Timer::after(Duration::from_secs(1)).await;
    }
}

#[embassy_executor::task]
async fn blink_task(pin: embassy_stm32::gpio::AnyPin) {
    let mut led = Output::new(pin, Level::Low, Speed::Low);
    loop {
        led.set_high();
        Timer::after_millis(500).await;
        led.set_low();
        Timer::after_millis(500).await;
    }
}
```

In `no_std` binaries define one `#[panic_handler]`: minimal, non-allocating, no unwinding.

```rust
#![no_std]
use core::panic::PanicInfo;
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    // signal fault, then halt
    loop {}
}
```

For serde in `no_std`, use `postcard` with fixed buffers; validate sizes, do not trust unverified input, and do not allocate in interrupt paths.

```rust
#![no_std]
use postcard::{to_slice, from_bytes};
let mut buf = [0u8; 64];
let written: &mut [u8] = to_slice(&my_struct, &mut buf)?;
let round: My = from_bytes(written)?;
```

## 5. Verification and test-first delivery

### Verification selection matrix

| Verification type | Choose it when |
| --- | --- |
| unit | Behavior is local and deterministic |
| integration | Behavior crosses module or adapter boundaries |
| doctest | Public examples are part of the contract |
| compile-fail | Misuse contracts should fail at compile time |
| property | Invariants or round trips matter more than examples |
| fuzz | A parser, decoder, protocol or input frontier is risky |
| `loom` | Small concurrent state models need interleaving exploration |
| `Miri` | Unsafe, aliasing or UB-risking logic needs extra scrutiny |
| performance | Latency or memory thresholds were explicitly stated |
| coverage | Higher-risk changes need stronger release confidence |

### TDD loop

```text
STUB -> RED -> GREEN -> REFACTOR -> VERIFY
```

- **STUB:** write the tests and the expected interface first.
- **RED:** confirm the failure matches the missing behavior.
- **GREEN:** implement the minimum code that satisfies the test.
- **REFACTOR:** improve decomposition, ownership and naming while staying green.
- **VERIFY:** run formatting, lints, tests and build, plus any higher-risk gate chosen (doctest, compile-fail, property, fuzz, `loom`, coverage), and confirm requirement traceability.

Cover unit, integration, error-path and concurrency cases. Add performance tests only when a metric is specified.

In STUB, write one or more tests per requirement id and define the interface signatures and fixtures.

For each requirement cover the happy path, the error path and the edge path. Add property-based tests for invariant-heavy logic and integration tests for cross-module workflows.

### Test matrix example

| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |
| REQ-RUST-001.0 | TEST-UNIT-001 | unit | filters only implementation entities | correctness |
| REQ-RUST-001.0 | TEST-INTEG-003 | integration | preserves order across parser and filter | correctness |
| REQ-RUST-001.0 | TEST-PERF-002 | perf | p99 < 500us for 10k entities | latency |
| REQ-RUST-001.0 | TEST-CONC-004 | concurrency | no race under 100 parallel tasks | safety |

A matrix that uses the wider verification mix. Choose the smallest useful set, not the biggest possible set.

| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |
| REQ-RUST-001.0 | TEST-UNIT-001 | unit | validates parsed entity ids | correctness |
| REQ-RUST-001.0 | TEST-INTEG-002 | integration | persists and reloads valid entities | integration |
| REQ-RUST-002.0 | TEST-DOC-003 | doctest | public example compiles and behaves as documented | usability |
| REQ-RUST-003.0 | TEST-CF-004 | compile-fail | rejects invalid generic usage | misuse |
| REQ-RUST-004.0 | TEST-PROP-005 | property | round-trip preserves invariant | invariant |
| REQ-RUST-005.0 | TEST-LOOM-006 | concurrency | shared state remains race-safe | safety |
| REQ-RUST-006.0 | TEST-PERF-007 | performance | p99 < 500us for 10k entities | latency |

### Test skeletons

Name each test after the requirement it proves.

Unit:

```rust
#[test]
fn test_req_rust_001_filter_implementation_entities_only() {
    let input = create_test_entities_mixed_set();
    let output = filter_implementation_entities_only(&input);
    assert!(output.iter().all(DomainEntity::is_implementation));
}
```

Async integration:

```rust
#[tokio::test]
async fn test_req_rust_001_pipeline_integration() -> anyhow::Result<()> {
    let fixture = create_pipeline_fixture_valid_case().await?;
    let output = run_processing_pipeline_async(&fixture).await?;
    assert_eq!(output.status, ProcessingStatus::Completed);
    Ok(())
}
```

Performance contract:

```rust
#[test]
fn test_req_rust_001_performance_contract() {
    use std::time::{Duration, Instant};
    let input = create_test_entities_large_set(10_000);
    let start = Instant::now();
    let _ = filter_implementation_entities_only(&input);
    assert!(start.elapsed() < Duration::from_micros(500));
}
```

Concurrency contract:

```rust
#[tokio::test]
async fn test_req_rust_001_concurrency_contract() -> anyhow::Result<()> {
    use futures::future::join_all;
    let shared = std::sync::Arc::new(create_shared_processor_state());
    let tasks = (0..100).map(|_| {
        let shared = std::sync::Arc::clone(&shared);
        tokio::spawn(async move { shared.process_safely_async().await })
    });
    let results = join_all(tasks).await;
    assert!(results.into_iter().all(|r| r.is_ok()));
    Ok(())
}
```

Doctest:

```rust
/// ```
/// let user_id = UserId::try_from("user_123")?;
/// assert_eq!(user_id.as_str(), "user_123");
/// # Ok::<(), UserIdError>(())
/// ```
```

Compile-fail (with `trybuild`):

```rust
#[test]
fn test_req_rust_003_invalid_usage_compile_fails() {
    let t = trybuild::TestCases::new();
    t.compile_fail("tests/ui/invalid_usage.rs");
}
```

Property (with `proptest`):

```rust
proptest! {
    #[test]
    fn test_req_rust_004_round_trip_invariant(input in valid_entity_strategy()) {
        let encoded = encode_entity_for_wire(&input)?;
        let decoded = decode_entity_from_wire(&encoded)?;
        prop_assert_eq!(decoded, input);
    }
}
```

Concurrency model (with `loom`):

```rust
#[cfg(loom)]
#[test]
fn test_req_rust_005_shared_state_loom_model() {
    loom::model(|| {
        // model the smallest interesting concurrent interaction here
    });
}
```

Performance and memory-layout claims as tests:

```rust
#[tokio::test]
async fn test_query_performance_contract() {
    let system = create_test_system().await;

    for i in 0..10_000 {
        system.add_node(create_test_node(i)).await.unwrap();
    }

    let start = Instant::now();
    let result = system.execute_query(test_query()).await.unwrap();
    let elapsed = start.elapsed();

    assert!(elapsed < Duration::from_micros(500),
            "Query took {:?}, expected <500us", elapsed);
}

#[test]
fn test_memory_layout_validation() {
    assert_eq!(mem::size_of::<NodeData>(), 72);
    assert_eq!(mem::align_of::<NodeData>(), 8);

    // Same pointer means the string was interned
    let str1 = InternedString::new("common_name");
    let str2 = InternedString::new("common_name");
    assert_eq!(str1.as_ptr(), str2.as_ptr());
}
```

Concurrency stress test with a final consistency check:

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
                let node = create_test_node(i * 100 + j);
                storage_clone.add_node(node).await.unwrap();
            }
        });
    }

    // Spawn multiple readers
    for _ in 0..20 {
        let storage_clone = Arc::clone(&storage);
        join_set.spawn(async move {
            for _ in 0..50 {
                let _ = storage_clone.get_random_node().await;
            }
        });
    }

    // Wait for all tasks; panic if any task failed
    while let Some(result) = join_set.join_next().await {
        result.unwrap();
    }

    // Verify data consistency: 10 writers * 100 nodes each
    let final_count = storage.node_count().await.unwrap();
    assert_eq!(final_count, 1000);
}
```

Property tests for round trips and validation:

```rust
use proptest::prelude::*;

proptest! {
    #[test]
    fn user_id_roundtrip(id in any::<u64>()) {
        let user_id = UserId(id);
        let serialized = serde_json::to_string(&user_id)?;
        let deserialized: UserId = serde_json::from_str(&serialized)?;
        prop_assert_eq!(user_id, deserialized);
    }
    
    #[test]
    fn message_content_validation(
        content in ".*",
        max_len in 1usize..10000
    ) {
        let result = validate_message_content(&content, max_len);
        if content.len() <= max_len && !content.trim().is_empty() {
            prop_assert!(result.is_ok());
        } else {
            prop_assert!(result.is_err());
        }
    }
}
```

A complete `loom` model:

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

Mutation testing with `cargo-mutants` checks test quality by introducing bugs; write tests that cover each boundary so every mutation is caught:

```rust
#[cfg(test)]
mod mutation_tests {
    use super::*;
    
    #[test]
    fn test_user_validation_comprehensive() {
        // Test should catch all possible mutations
        assert!(validate_user("").is_err());           // Empty name
        assert!(validate_user("a").is_err());          // Too short  
        assert!(validate_user("a".repeat(101)).is_err()); // Too long
        assert!(validate_user("valid_user").is_ok());  // Valid case
    }
}
```

### Testing and contract verification patterns

- **Doctests as executable contracts.** Examples rot when they are not executed; a doctest turns API explanation into a regression boundary. Use when the example communicates expected behavior, not just syntax. Move very large examples to integration tests.
- **Compile-fail UI tests for misuse contracts.** If misuse should fail with a specific type error, that is part of the public contract, especially for macros, builders and type-level APIs. Do not assert unstable compiler wording too precisely.
- **Property tests for invariants and round trips.** Example tests prove one chosen case; property tests probe the input space and shrink failures to something readable. Use for serializers, parsers, formatters, normalizers and algebraic invariants. Skip when the state space is tiny and examples cover it.
- **Fuzzing for parser, decoder and protocol frontiers.** Fuzzing explores malformed input no human would write. Use for bytes, external protocols, compressed data and attacker-influenced input. Pair it with sanitizers, corpus hygiene and timeouts.
- **Snapshot tests (`expect-test`) where textual output is the contract.** Good for parsers, formatters, diagnostics and macro expansions whose whole output shape matters. Do not let snapshots become golden files reviewers stop reading.
- **Test infrastructure that optimizes failure readability and isolation.** A suite is only as fast as its failure-diagnosis loop. Use dedicated temp dirs, diff-friendly assertions, explicit command wrappers and retries for flaky OS operations in integration tests that touch real filesystems, commands or multi-line output.

Doctest as contract (keep examples small, and make them assert something):

```rust
/// Adds two numbers.
/// ```
/// assert_eq!(my_crate::add(2, 2), 4);
/// ```
pub fn add(a: i32, b: i32) -> i32 { a + b }
```

Compile-fail UI tests with `trybuild`, cases under `tests/ui/*.rs`:

```rust
#[test]
fn ui() {
    let t = trybuild::TestCases::new();
    t.compile_fail("tests/ui/*.rs");
}
```

Fuzz target for `cargo-fuzz`. Keep the harness minimal, run it in nightly CI, keep and minimize the corpus:

```rust
#![no_main]
use libfuzzer_sys::fuzz_target;
fuzz_target!(|data: &[u8]| { let _ = my_crate::parse(data); });
```

For property tests, record failing seeds for reproducibility and let the framework shrink to a minimal counterexample.

Inline snapshot with `expect-test`, for parsers, formatters and analyzers:

```rust
use expect_test::expect;

fn render(x: &[u8]) -> String { format!("{:?}", x) }

#[test]
fn snapshot() {
    let got = render(&[1,2,3]);
    expect![["[1, 2, 3]"]].assert_eq(&got);
    // Run with `EXPECT=overwrite` to update.
}
```

Document `# Errors`, `# Panics` and `# Safety` on public items; an undocumented panic or unsafe precondition is a defect:

```rust
/// Parses input.
/// # Errors
/// Returns Err if input is invalid.
pub fn parse(_s: &str) -> Result<(), Error> { Ok(()) }
```

## 6. Types and API design

- Prefer newtypes, explicit conversions, and designs that make invalid states unrepresentable.

- Accept `&[T]`, `&str` or `AsRef` in public APIs, not `&Vec<T>` or `&String`.
- Use newtypes for domain identifiers and invariants.

- Use `AsRef<T>` where ergonomic conversions improve call sites.
- Use `From` for infallible conversions and `TryFrom` for fallible ones.
- Model domain states with enums and domain types so invalid states cannot be built.

### API and type design patterns

Each pattern: why it matters, when to use it, when to avoid it.

- **Accept borrowed inputs in public APIs.** `&[T]`, `&str`, `AsRef<T>` and `Borrow<T>` reduce caller friction and needless allocation; the API commits to semantics, not to a backing container, and hot paths get cheaper by default. Use when the function reads its input and callers may hold slices, arrays, `Vec`, `String`, `&str` or borrowed views. Avoid when the function must take ownership for long-term storage or mutation.
- **Newtypes and parse-don't-validate.** Turning raw data plus repeated checks into a validated type removes whole classes of downstream bugs, and newtypes stop accidental mixing of offsets, IDs, units and domain concepts that are all primitives underneath. It converts runtime discipline into compile-time discipline, which makes it one of the highest-leverage Rust patterns. Use for IDs, offsets, handles, units, validated strings and FFI wrapper types. Avoid when the wrapper adds no semantic distinction and only makes the API noisier.
- **`From` and `TryFrom`, not ad hoc constructors.** Conversions become composable and discoverable, and infallible and fallible conversions are cleanly separated. Use when the operation is fundamentally a conversion between two domain types. Avoid when the operation does real work beyond conversion and deserves a named constructor.
- **Option and Result combinators over nested matching.** `map`, `and_then`, `transpose`, `ok_or_else` and `try_fold` keep linear flows linear; deep nested matching hides the control flow. Use for straightforward transformation or chaining. Avoid when a full `match` shows the branching more clearly than stacked combinators.
- **Trait objects versus generics as an explicit decision.** Both dispatch kinds are valid; problems come when the choice is accidental. Hot paths often want generics. Plugin points, heterogeneous collections and boundary seams often want `dyn Trait`. Use `dyn` when flexibility and type erasure are worth the dispatch cost or save code size. Avoid it in a tight loop or heavily inlined path.
- **Return `impl Iterator` when laziness matters.** It preserves laziness, hides messy adapter types and avoids `Box<dyn Iterator>` overhead. Use when the pipeline should stay lazy and the concrete type is an implementation detail. Avoid when you need heterogeneity, object safety or long-lived trait objects.
- **Named outcome enums over booleans and sentinels.** A boolean says something happened; an enum says which action the caller must take next. Strong in control-flow helpers, search engines, state machines and CLI parsing. Use when the return value controls caller behavior. Avoid when there are truly two obvious, universally understood states.
- **Blanket impls for `&T`, `&mut T` and `Box<T>`.** Traits are easier to use when references and boxed forms work naturally; this cuts wrapper boilerplate. Use when a trait is read-only, object-safe or naturally delegating. Avoid when object-safety or ownership semantics would make the impls misleading.
- **Flat public API facades with `pub use`.** Internal file layout and public API shape should not be welded together; re-exports let a crate reorganize internals without breaking callers. Use when a crate has several internal modules and wants one stable import surface. Avoid when it only hides useful structure.
- **`PhantomData<fn() -> T>` invariance for typed handles.** Handle types, arena indices and lifetime-sensitive tokens can be unsound if variance is too permissive. Use when the type parameter carries lifetime or aliasing implications that must not be coerced. Avoid when ordinary covariance is correct.
- **Type-state plus a drop bomb for must-complete protocols.** Some APIs are wrong if partially used. Type-state makes legal transitions explicit, and a debug-time bomb in `Drop` catches "forgot to complete or abandon" immediately. Use for parser markers, staged builders, transactions and protocol objects that must be finalized. Avoid when the state machine is trivial and the extra types would outweigh the gain.

### Core idioms with code

- **Expression-oriented code.** When a function computes a value, return the last expression. Use `if/else` and `match` as expressions and `let` bindings for clarity. Avoid `mut` accumulators where `map`/`fold` suffice, and stray semicolons that turn an expression into `()`.
- **Slices and traits in public APIs.** Over-generic bounds hurt inference; keep them simple.

```rust
fn process<S: AsRef<str>>(s: S) {
    let s: &str = s.as_ref();
    // ...
}
```

- **`Cow<'_, str>` / `Cow<'_, [u8]>`.** Use when data is usually borrowed and sometimes modified: config, cache keys, deserialized data. Do not use it when data is always owned or always borrowed, and watch for hidden `.to_string()` in tight loops.
- **Conversions.** Do not return `Result` for an infallible conversion. To implement a conversion for a foreign type, wrap it in a newtype (orphan rule).
- **Newtypes.** A `type` alias does not create a distinct type. Add `#[repr(transparent)]` when the newtype crosses FFI.

```rust
#[repr(transparent)]
struct UserId(String);
impl UserId { fn parse(s: &str) -> Option<Self> { (!s.is_empty()).then(|| Self(s.to_owned())) } }
```

- **Trait objects versus generics.** Use `Box<dyn Trait>` for heterogeneous collections and at API boundaries, where flexibility and smaller code size matter. Use generics on hot paths. Avoid trait objects in tight loops and over-generic public APIs that cause monomorphization bloat.

- **Function pointers.** When a callable never captures, take `fn(T) -> U`; it avoids an extra monomorphization.

```rust
fn apply<T,U>(x: T, f: fn(T) -> U) -> U { f(x) }
fn double(n: i32) -> i32 { n*2 }
let y = apply(21, double);
```

- **Monomorphization bloat.** If generics inflate compile time or binary size, use `dyn Trait` at API boundaries and on rarely used paths, and measure the effect.
- **Do not clone to satisfy the borrow checker.** Borrow where possible; use `Rc`/`Arc` when several owners are really required, and design ownership instead of applying `Arc` everywhere.
- **Visibility.** Scope items with `pub(crate)`, `pub(super)` and `pub(in path)`; do not default to `pub`. Use `#![no_implicit_prelude]` in modules that need explicit paths, such as macro internals.

```rust
pub mod outer { 
    pub(in crate::outer) fn only_outer() {}
}
```

- **Explicit collection construction.** `FromIterator::from_iter` names the target type without a turbofish:

```rust
use std::iter::FromIterator;
let it = [1,2,3].into_iter().map(|x| x * 2);
let v = Vec::<i32>::from_iter(it);
```

- **`#[non_exhaustive]` in use.** Outside the defining crate, matches need a wildcard arm and the type cannot be constructed directly:

```rust
#[non_exhaustive]
pub enum Error { Io(std::io::Error), Parse }

fn handle(e: Error) {
    match e { Error::Io(_)| Error::Parse | _ => {} }
}
```

### Trait, async and macro boundary discipline

- **Pin, pin projection and async trait boundaries.** Pinned values carry movement invariants; violating them is not an ordinary logic bug. Use safe projection helpers when implementing custom futures, self-referential state machines or pinned wrappers. Do not hand-project pinned fields or call `Pin::new_unchecked` without a proof. Understand the object-safety and allocation tradeoffs before choosing `async-trait` or async fn in traits.
- **HRTBs, GATs and object safety.** Use them when ordinary trait methods cannot express borrowed output or a callback valid for any lifetime (lending-style iteration, for example). Do not add them where simple ownership is clearer, and do not publish a trait that looks dyn-friendly but is not object-safe.
- **Additive features, sealed traits and coherence.** API stability also depends on whether features compose and whether downstream crates can safely implement your traits. Keep features additive, never mutually exclusive. Seal a trait when you still need freedom to evolve it.
- **Macro and proc-macro hygiene.** A macro bug repeats at every expansion site. Use absolute paths in expansions, disciplined spans and compile-time diagnostics. Do not panic inside a proc macro on user error, and do not rely on the caller's imports.
- **`NonZero` niches, ZSTs and uninhabited types.** Use `NonZero*` and `Option<NonZero*>` when the niche is real and semantically clean, zero-sized marker types with `PhantomData` for compile-time state that costs nothing at runtime, and uninhabited types for impossible states in place of sentinel values. Use them because the model is clearer, not because the layout looks clever.

### Trait and language details

- **Coherence and the orphan rule.** Either the trait or the self type must be local (E0117, E0210). Provide extension traits for foreign types. Avoid blanket impls that could conflict with downstream impls.
- **Specialization.** Do not use `specialization` or `min_specialization` in general libraries; prefer explicit trait design.
- **Trait-object upcasting.** Upcast `dyn SubTrait` to `dyn SuperTrait` directly where the toolchain supports it, in place of hand-written `as_super` shims.
- **HRTBs for callbacks.** Use `for<'a> Fn(&'a T) -> U` when a callback borrows data of any lifetime. Do not require `'static` unnecessarily or encode the lifetime as a type parameter.
- **GATs for lending.** Use them when an associated type depends on a lifetime (lending iterators, parser cursors), so outputs can borrow instead of allocating.
- **Object safety.** For dyn-compatible traits, avoid `Self` in return position and generic methods, and use object-safe receivers (`&self`, `&mut self`, `Box<Self>`).
- **Never type.** Use `!` for functions that never return. Document any library function that diverges by panicking.
- **`where` clauses.** Move long bounds off the signature into `where`.
- **Raw identifiers.** Use `r#ident` when a name collides with a keyword across editions; do not rename a public symbol that must stay stable.
- **Pattern matching in the 2024 edition.** Be explicit about `ref`/`mut` bindings instead of relying on older match ergonomics; migrate with `cargo fix --edition`.
- **Custom futures and executors.** Respect the `Poll::Pending` contract: return `Pending` only after arranging a wake, and wake only when progress is possible. No busy-loop polling.

- **Dispatchable and non-dispatchable methods.** Object-safe receivers are `&self`, `&mut self`, `Box<Self>`, `Rc<Self>`, `Arc<Self>` and `Pin<P>`. Mark helpers `where Self: Sized` to keep them off the trait object while keeping a rich API on concrete types.

```rust
trait DynOk {
  fn do_it(&self);
  // not on dyn objects; callable only on concrete types
  fn into_inner(self) where Self: Sized; 
}
```

- **Pin projection.** Use `pin-project-lite` or `pin-project` to project pinned fields safely.

```rust
use pin_project_lite::pin_project;
pin_project! {
  struct Task { #[pin] fut: impl Future<Output = ()> }
}
```

- **Lifetime elision.** Rely on elision for simple cases. Add explicit lifetimes when there are several reference inputs or the output cannot be inferred; `fn frob(s: &str, t: &str) -> &str` is ambiguous.
- **Trait-object lifetimes.** Know the default object lifetime bound; write `&'a dyn Trait` where needed, and avoid an accidental `'static`.
- **Preludes.** Do not shadow std prelude items or re-import them. Offer a crate `prelude` for frequently used traits and types, keeping internal modules private:

```rust
pub mod prelude { pub use crate::{MyTrait, KeyType}; }
```

- **API guidelines.** Follow the standard casing conventions. Name features without `no-`, `use-` or `with-` prefixes. Changing a public trait can break SemVer; seal traits to control external impls.
- **Additive features in Cargo.** Use `dep:` to decouple feature names from dependency names, guard code with `#[cfg(feature = "foo")]`, and document each feature's effect:

```toml
[features]
serde = ["dep:serde"]
fast = []
```

- **Explicit patterns under the 2024 edition:**

```rust
// Before (implicit, may lint under 2024)
match &opt { Some(x) => {/*...*/}, _ => {} }
// After (explicit)
match opt.as_ref() { Some(x) => {/*...*/}, None => {} }
```

- **Associated types.** Prefer `type Output;` to an extra generic parameter when the output is fixed by the implementor.

### Macros and build scripts

- **Choose the flavor.** Derive to generate impls from type structure; attribute macros to transform or wrap items; function-like macros for DSLs. Do not write a proc macro where `macro_rules!` suffices, or heavy proc-macro logic that could run in `build.rs`.
- **Hygiene.** Refer to items with `$crate::path` or `::std::...`, and use unique internal names.

```rust
#[macro_export]
macro_rules! myvec {
    ($($x:expr),* $(,)?) => {{
        let mut v = ::std::vec::Vec::new();
        $(v.push($x);)*
        v
    }};
}
```

- **`macro_rules!` matchers.** Use `$( ... )*` or `+` with separators and the correct fragment specifier (`expr`, `ty`, `path`, `ident`, `tt`). Keep matchers simple and layered; avoid greedy or ambiguous patterns.
- **Proc-macro pipeline.** Parse with `syn`, generate with `quote!`, and target `proc-macro2` so the logic is testable outside a proc-macro crate. Never build code by string concatenation.
- **Errors.** Emit `compile_error!` with a span on the exact offending tokens. Do not `panic!`, and do not swallow an error and generate broken code.
- **Cost and security.** Proc macros run at compile time with filesystem access. Keep the surface small, document the cost, avoid quadratic token growth, and do not read arbitrary files without rerun guards.
- **Formatting.** Keep macro bodies readable and tested; do not disable formatting wholesale or depend on formatting-sensitive macro bodies.
- **Build-script codegen.** Write generated files only under `OUT_DIR`, declare inputs with `cargo::rerun-if-changed`, keep generation deterministic, and `include!` the result:

```rust
// build.rs
use std::{env, fs, path::PathBuf};
fn main() {
    let out: PathBuf = env::var_os("OUT_DIR").unwrap().into();
    fs::write(out.join("generated.rs"), "pub const V: &str = \"1.0\";").unwrap();
    println!("cargo::rerun-if-changed=build.rs");
}
```

```rust
// lib.rs
include!(concat!(env!("OUT_DIR"), "/generated.rs"));
```

- **Build-script directives.** Narrow rebuilds with `cargo::rerun-if-changed` and `cargo::rerun-if-env-changed`, link with `cargo::rustc-link-lib` and `cargo::rustc-link-search`, and declare custom cfgs with `cargo::rustc-check-cfg`.

```rust
// build.rs
println!("cargo::rerun-if-changed=wrapper.h");
println!("cargo::rustc-link-lib=static=foo");
println!("cargo::rustc-check-cfg=cfg(has_foo)");
```

- **Proc-macro crates** set `proc-macro = true` under `[lib]`.

## 7. Ownership, borrowing and data handling

- Prefer expression-oriented style and iterators over mutable accumulator code.

- Prefer borrowing over cloning in hot paths.
- Use iterator pipelines for data transforms when they improve clarity.
- Keep lock scope small and explicit.
- Use `Arc` for shared ownership across threads and `Rc` for single-threaded sharing.

### Ownership, borrowing and iterator sharp edges

- **Interior mutability versus synchronization.** `Cell` and `RefCell` solve single-thread logical mutability; `Mutex` and `RwLock` solve cross-thread synchronization. Do not use a mutex in single-threaded code to quiet the borrow checker, and do not carry `RefCell` borrows or lock guards across async suspension points.
- **Borrow-checker-friendly API design.** Many awkward APIs are awkward because their shape prolongs borrows. Smaller scopes, temporaries and methods that separate read and write phases remove E0502-class friction without cloning everything. Do not rely on subtle two-phase-borrow behavior where clear structure would do.
- **Iterator contracts and fallible pipelines.** Support owned and borrowed iteration correctly and keep error short-circuiting. `size_hint`, `ExactSizeIterator`, `try_fold`, `try_for_each` and `FromIterator` define what consumers may assume. Do not claim exact iterator properties you cannot uphold, and do not `unwrap` inside a chain that should short-circuit with `Result`.
- **Collection choice.** `Vec`, `VecDeque`, `HashMap`, `BTreeMap`, `IndexMap` and `BinaryHeap` make different operational promises: dense append-heavy storage, queue, hashed lookup, ordered map, stable iteration order, priority scheduling. The wrong default causes performance or determinism bugs. Do not use `LinkedList` as a default, and never treat `HashMap` iteration order as meaningful.

- **Two-phase borrows.** In a nested call the mutable borrow is reserved first and activated later; shared borrows must end before activation. Do not publish an API that is only sound under a specific compiler lowering.

```rust
let mut v = vec![1];
// OK: len() borrow ends before push activates the &mut
v.push(v.len());
```

- **Fixing E0502.** Shorten borrows with inner scopes, bind temporaries so the shared borrow ends before the `&mut` use, and split struct borrows by field.
- **Fallible pipelines.** An iterator of `Result<T, E>` collects into `Result<Vec<T>, E>`; use `try_fold`/`try_for_each` to stop at the first error.

```rust
let items: Vec<Result<u32, &'static str>> = vec![Ok(1), Ok(2)];
let ok: Result<Vec<_>, _> = items.into_iter().collect();
```

- **RAII guards.** Acquire in the constructor, release in `Drop`, keep guards short-lived, and do not share a guard beyond the scope that needs it.

### Iterators and closures

- **`IntoIterator`, `iter`, `iter_mut`.** Accept `impl IntoIterator<Item = X>` for flexibility. Use `iter()`/`iter_mut()` when a borrow suffices; `into_iter()` on an owned container moves it. Arrays implement `IntoIterator` by value on modern editions; do not rely on edition-specific behavior.
- **Implement `IntoIterator` for owned and borrowed forms** of a custom collection, so `for x in &collection` works:

```rust
#[derive(Debug)]
struct MyCollection(Vec<i32>);
impl IntoIterator for MyCollection {
  type Item = i32;
  type IntoIter = std::vec::IntoIter<i32>;
  fn into_iter(self) -> Self::IntoIter { self.0.into_iter() }
}
impl<'a> IntoIterator for &'a MyCollection {
  type Item = &'a i32;
  type IntoIter = std::slice::Iter<'a, i32>;
  fn into_iter(self) -> Self::IntoIter { self.0.iter() }
}
```

- **Adapters versus consumers.** Compose with adapters (`map`, `filter`, `take`) and drive with consumers (`collect`, `sum`, `for_each`). Do not build intermediate `Vec`s, put side effects in adapters, or collect when a lazy pipeline suffices.
- **Return `impl Iterator`**, not a concrete adaptor type, and document when evaluation happens. Do not box iterators on hot paths.
- **`FromIterator`.** Implement it for custom containers. Keep turbofish use readable.
- **Fusion and reversal.** Call `.fuse()` if `next()` may be called after exhaustion; do not assume fused behavior. Implement `DoubleEndedIterator` only where reverse traversal is natural, and keep forward and backward state consistent in `next_back`.
- **`size_hint` and `ExactSizeIterator`.** Give a meaningful `size_hint`; implement `ExactSizeIterator` only when the length is truly exact. Unsafe code must never rely on `size_hint` being correct.
- **Closure bounds.** Pick the narrowest that fits: `Fn` for repeated read-only calls, `FnMut` when the closure mutates, `FnOnce` when it may consume its captures. Function pointers implement all three.
- **Closures across threads and tasks.** Use `move`; captured values must be `Send + 'static` where required. Prefer a channel to `Arc<Mutex<_>>` when one suffices.

### Collections

- **Sequences.** Default to `Vec`. Use `VecDeque` for queue or deque semantics. Use `LinkedList` only when O(1) splicing dominates and the cache cost is acceptable.
- **Maps.** `HashMap` for average O(1) lookup; `BTreeMap` for ordering, range queries and predictable iteration. Do not use `BTreeMap` for hot random access with no ordering need. `IndexMap` gives stable insertion order for caches, diffs and tests; after a removal, order is kept only with `shift_remove`.
- **Hashers.** The std map is a SwissTable. Swap in a faster hasher (aHash, fxhash) only for non-adversarial input, because of hash-flooding DoS. Never mutate a key in place.
- **Priority queues.** `BinaryHeap` builds from a `Vec` in O(n), with O(log n) push and pop. Use it for top-k and scheduling; do not fully sort or emulate a heap with `BTreeMap`.
- **Capacity.** Use `with_capacity` when the number of pushes is known.
- **Small collections.** `SmallVec<[T; N]>` cuts heap traffic when a small bound holds on a hot path. Profile first and watch the cost when it spills to the heap.
- **Bits.** Use `bitvec` for packed booleans and protocol layouts, with an explicit bit order and store type, not `Vec<bool>` or ad-hoc bit-twiddling:

```rust
use bitvec::prelude::*;
let mut bits: BitVec<u8, Msb0> = bitvec![0; 16];
bits.set(3, true);
assert!(bits[3]);
```

- **Read-mostly concurrent maps.** When reads dominate and eventual consistency is acceptable, use a read-optimized map such as `evmap` in place of `Mutex<HashMap>`. Readers see snapshots; writers publish with `refresh()`. It is not linearizable.

```rust
let (read, mut write) = evmap::new();
write.insert("k", 1);
write.refresh();
assert_eq!(read.get_and("k", |v| v.iter().copied().collect::<Vec<_>>()), Some(vec![1]));
```

```rust
let mut v = Vec::with_capacity(1024);
use indexmap::IndexMap; let mut im = IndexMap::new();
use std::collections::BinaryHeap; let h = BinaryHeap::from(vec![3,1,4]);
```

Repeatedly pushing ascending values into a `BinaryHeap` is its slow path; build it from a `Vec`.

### Smart pointer decision matrix

| Scenario | Single-Threaded | Multi-Threaded | Use Case |
|----------|------------------|----------------|----------|
| **Unique Ownership** | `Box<T>` | `Box<T>` | Heap allocation, trait objects |
| **Shared Ownership** | `Rc<T>` | `Arc<T>` | Multiple owners, reference counting |
| **Interior Mutability** | `RefCell<T>` | `Mutex<T>` / `RwLock<T>` | Modify through shared reference |
| **Combined** | `Rc<RefCell<T>>` | `Arc<Mutex<T>>` | Shared mutable state |

## 8. Errors and recovery

- Keep library errors typed and boundary-aware.

- Use `thiserror` for library error enums and `anyhow` at application composition boundaries.
- No `unwrap` or `expect` in production paths unless an invariant is documented and justified.

- Propagate errors with `?` and attach context at I/O and boundary operations.

### Error design patterns

- **`thiserror` in libraries, `anyhow` or `eyre` in binaries.** Libraries need structured errors callers can inspect; binaries need ergonomic propagation, context and display. Mixing the two produces mushy error boundaries. Never export `anyhow::Error` from a library because it feels easier.
- **Opaque public errors with a private kind.** A public error struct that wraps a private or controlled kind keeps semver room while still allowing inspection, and it stops downstream code constructing states only your crate should own. Use when the library's error space is public and likely to evolve. Avoid when the error really is a small fixed enum.
- **`#[non_exhaustive]` on public enums and structs that will grow.** Future-proofing a public type is an API reliability pattern, not a cosmetic one; omitting the attribute silently promises the type will never grow. Use when the type is public and the domain has room to evolve. Avoid when the type is intentionally sealed and extra variants would change its meaning.
- **Actionable diagnostics with exact location and a repair hint.** Telling a user the byte offset and a valid workaround is worth more than another abstract variant name. Use when parsing user-facing input, formats, flags, sizes, patterns and configuration. Avoid when the detail is internal and would confuse the caller.
- **Binary-safe diagnostics for non-UTF-8 data.** Paths and byte-oriented data are often not valid UTF-8; converting to `String` too early loses data or panics in the wrong place. Use for file paths, regex patterns, command stderr, protocol bytes and search output. Avoid only when the domain guarantees UTF-8 and the proof is local and strong.
- **Context at I/O and orchestration boundaries.** `?` preserves propagation but not local meaning; add context where the operation is still understandable: opening files, issuing requests, decoding payloads, crossing service boundaries. Avoid adding it at every small helper layer, which repeats the same message.
- **`ExitCode` and error-chain inspection at CLI boundaries.** CLIs need semantically correct exit behavior, not "print error and die". Broken pipes and other wrapped I/O failures often need special handling, and returning `ExitCode` keeps destructors running. A library must never own process exit semantics.
- **FFI unwind boundaries with `catch_unwind` and explicit contracts.** A panic crossing an FFI boundary can be undefined behavior. Handle it explicitly whenever exporting or importing C-facing APIs; never assume the other side handles it.

- **Source-annotated diagnostics with `miette` or `color-eyre`.** Some failures are best explained with a context snippet and labeled spans. Use in binaries and CLIs for end-user parse or config errors. Do not leak rich diagnostic types into library APIs that callers need lightweight and stable.

Library error enum and application context, side by side:

```rust
// Library errors: structured with thiserror
#[derive(Error, Debug)]
pub enum SystemError {
    #[error("Database error: {0}")]
    Database(#[from] DatabaseError),

    #[error("Query failed: {query} - {cause}")]
    QueryFailed { query: String, cause: String },

    #[error("Timeout after {elapsed:?} (limit: {limit:?})")]
    Timeout { elapsed: Duration, limit: Duration },
}

// Application errors: anyhow for context
pub async fn process_request(req: Request) -> anyhow::Result<Response> {
    let data = fetch_data(&req.id)
        .await
        .with_context(|| format!("Failed to fetch data for request {}", req.id))?;

    let result = process_data(data)
        .with_context(|| "Data processing failed")?;

    Ok(Response::new(result))
}
```

Adding context while propagating:

```rust
use anyhow::Context;
fn load(path: &str) -> anyhow::Result<String> {
    std::fs::read_to_string(path).with_context(|| format!("reading {}", path))
}
```

In libraries, use `thiserror` with `#[from]` and `map_err`; never swallow the source error.

Rich reports in binaries only: install a global reporter at startup.

```rust
fn main() -> color_eyre::Result<()> {
    color_eyre::install()?;
    // ...
    Ok(())
}
```

Typed library error with a transparent source. Use `snafu` when call sites need context-rich enums:

```rust
#[derive(thiserror::Error, Debug)]
pub enum ParseError {
  #[error("invalid header: {0}")]
  InvalidHeader(String),
  #[error(transparent)]
  Io(#[from] std::io::Error),
}
```

- **CLI termination.** Return `Result<(), E>` from `main` or use `std::process::ExitCode`. Do not panic on expected user errors, and keep nonzero codes consistent.

Span-labeled diagnostics with `miette`, in binaries only:

```rust
use miette::{Diagnostic, Result, SourceSpan};
use thiserror::Error;

#[derive(Debug, Error, Diagnostic)]
#[error("parse error")]
struct ParseErr {
  #[source_code]
  src: String,
  #[label("here")] span: SourceSpan,
}

fn parse(_s: &str) -> Result<()> { Err(ParseErr { src: "x+y".into(), span: (2..3).into() }.into()) }
```

## 9. Async and concurrency

- Never block inside async code, and never hold a lock guard across `.await`.
- Prefer bounded concurrency and cancellation-aware code.

- Move CPU-bound or blocking work off the executor with `spawn_blocking`.
- Do not hold `Mutex` or `RwLock` guards across `.await`.
- Use bounded channels for backpressure.
- Give long-running async operations a cancellation path.
- Validate shared-state behavior with concurrent stress tests.

### Async and concurrency reliability patterns

- **No blocking and no locks across `.await`.** Violations cause latency spikes, deadlocks, starvation and performance cliffs. Applies on any async runtime. Do not assume a short synchronous call is harmless without proving it is non-blocking.
- **Bounded channels, backpressure and cancellation tokens.** Unbounded queues hide problems until memory pressure is the symptom; backpressure makes throughput limits visible; cancellation tokens make shutdown explicit and cooperative. Use in pipelines, workers, fan-out systems and long-running services.
- **Cancel-safe `tokio::select!`.** A future dropped by `select!` loses its internal state at once. If partially consumed state lives inside the future, cancellation becomes data loss or protocol corruption. Keep half-read buffers and half-advanced parsers outside the branch futures when multiplexing reads, writes, shutdown signals, timers and work streams.
- **Structured concurrency with `JoinSet` and task scopes.** Detached tasks are easy to start and hard to reason about; structured concurrency keeps ownership, shutdown and error propagation visible. Use when a parent operation owns a family of subtasks and must know when they finish or fail.
- **Model checking with `loom`.** One passing run proves almost nothing about concurrency. `loom` explores interleavings of a small model and finds races ordinary tests miss. Use for lock-free pieces, ordering-sensitive state machines and subtle synchronization. Carve out a focused model; do not put the whole production system into `loom`.
- **Atomic ordering by reasoning, not superstition.** Do not use `SeqCst` everywhere or `Relaxed` everywhere. Justify each ordering by the memory relation needed, then test it where possible.
- **Thread naming, join discipline and `move` closures.** Name threads so their purpose is visible, join them so their lifecycle is explicit, and use `move` closures so ownership across the boundary is clear. Do not leak threads or rely on implicit shutdown.
- **`OnceLock` and `LazyLock` for one-time initialization.** Use for expensive shared configuration, lookup tables, regexes and lazily initialized global state; they replace hand-rolled synchronization. Do not reach for global mutable state where plain ownership is simpler.

- **Channel and synchronization choice.** `std::sync::mpsc`, `crossbeam-channel`, `flume`, Tokio channels, `Mutex`, `RwLock` and `parking_lot` are not interchangeable defaults; concurrency bugs often start at primitive selection. Do not mix channel ecosystems casually, and do not use the std channel where MPMC, select, deadlines or rendezvous semantics are needed.

### Async runtime discipline, in code

```rust
// Offload blocking work
pub async fn process_heavy_computation(data: Vec<u8>) -> Result<ProcessedData> {
    tokio::task::spawn_blocking(move || {
        // CPU-intensive work that would block the runtime
        expensive_computation(data)
    }).await?
}

// Use timeouts for all external calls
pub async fn fetch_external_data(url: &str) -> Result<Data> {
    tokio::time::timeout(
        Duration::from_secs(30),
        reqwest::get(url)
    ).await??
}

// Structured concurrency with JoinSet
pub async fn process_batch(items: Vec<Item>) -> Vec<Result<ProcessedItem>> {
    let mut tasks = JoinSet::new();
    
    for item in items {
        tasks.spawn(async move { process_item(item).await });
    }
    
    let mut results = Vec::new();
    while let Some(result) = tasks.join_next().await {
        results.push(result.unwrap_or_else(|e| Err(ProcessError::TaskPanic(e.to_string()))));
    }
    results
}
```

### Actor pattern for state

Message-passing concurrency: one task owns the state and other tasks send it messages.

```rust
use tokio::sync::{mpsc, oneshot};

pub struct StateActor<T> {
    state: T,
    receiver: mpsc::Receiver<StateMessage<T>>,
}

pub enum StateMessage<T> {
    Get { 
        respond_to: oneshot::Sender<T> 
    },
    Update { 
        updater: Box<dyn FnOnce(&mut T) + Send>,
        respond_to: oneshot::Sender<Result<(), StateError>>
    },
}

impl<T> StateActor<T> 
where 
    T: Clone + Send + 'static 
{
    pub async fn run(mut self) {
        while let Some(msg) = self.receiver.recv().await {
            match msg {
                StateMessage::Get { respond_to } => {
                    let _ = respond_to.send(self.state.clone());
                }
                StateMessage::Update { updater, respond_to } => {
                    updater(&mut self.state);
                    let _ = respond_to.send(Ok(()));
                }
            }
        }
    }
}
```

### Short async examples

Release the lock before awaiting:

```rust
let data = Arc::new(Mutex::new(vec![]));
// Anti-pattern:
// let mut guard = data.lock().unwrap();
// async_call().await; // lock held across await
// Correct:
{
    let mut guard = data.lock().unwrap();
    guard.push(1);
}
async_call().await;
```

Bounded channel with a timeout. Use `tokio_util::sync::CancellationToken` for cooperative cancellation, not ad-hoc boolean flags:

```rust
use tokio::{sync::mpsc, time::{timeout, Duration}};
let (tx, mut rx) = mpsc::channel(1024);
let send = async move { tx.send(item).await.ok(); };
let recv = async move { while let Some(v) = rx.recv().await { /* ... */ } };
let _ = timeout(Duration::from_secs(1), recv).await; // apply backpressure/timeouts
```

Cancellation-safe `select!`: the stream owns its buffered state outside the branch futures, and no branch does blocking I/O:

```rust
use tokio::select;
async fn run(mut stream: BufferedStream) {
    loop {
        select! {
            biased;
            maybe = stream.next() => { if maybe.is_none() { break; } },
            _ = shutdown_token.cancelled() => { break; }
        }
    }
}
```

Backpressure with a bounded or rendezvous channel (`crossbeam_channel::bounded`, `flume::bounded`), sending with a timeout or deadline:

```rust
let (tx, rx) = flume::bounded::<u32>(1024);
// send with timeout
if tx.send_timeout(42, std::time::Duration::from_millis(50)).is_err() {
    // apply backpressure strategy
}
```

Task scope: children finish before the scope exits, so no task outlives its owner and no manual join bookkeeping is needed:

```rust
use tokio::task;
async fn parent() {
    task::scope(|s| async move {
        let h1 = s.spawn(async { /* child */ });
        let h2 = s.spawn(async { /* child */ });
        let _ = (h1.await, h2.await);
    }).await;
}
```

`JoinSet` owns its children; dropping it cancels the outstanding ones. Drain it with `join_next()`:

```rust
use tokio::task::JoinSet;
let mut set = JoinSet::new();
for i in 0..10 { set.spawn(async move { i }); }
while let Some(res) = set.join_next().await { let _ = res?; }
```

- **Runtime choice.** Tokio for general-purpose work and ecosystem; smol for lightweight single-threaded use; glommio for io_uring with sharded executors. Do not mix runtimes in one process without clear isolation.
- **Async in traits.** Use `async fn` in traits for static dispatch. For dynamic dispatch, return a boxed future or use `async-trait` and accept the boxing cost. State `Send` bounds explicitly. Async trait methods are not dyn-compatible by default.

```rust
use core::future::Future;
trait Fetch {
  async fn get(&self, k: &str) -> Vec<u8>; // static dispatch
}
// dynamic dispatch alternative
trait FetchDyn {
  fn get(&self, k: &str) -> Pin<Box<dyn Future<Output = Vec<u8>> + Send + '_>>;
}
```

### Threads, locks, atomics and channels

- **`parking_lot`.** Smaller and faster locks than std on contended paths, with optional deadlock detection. Poisoning and fairness differ from std. Do not mix `std::sync` and `parking_lot` guards.

```rust
use parking_lot::{Mutex, RwLock};
static DATA: Mutex<Vec<u8>> = Mutex::new(Vec::new());
let mut g = DATA.lock();
g.push(1);
```

- **Scoped threads.** `std::thread::scope` lets threads borrow from the parent without `'static`; all are joined when the scope exits. Do not wrap data in `Arc<Mutex<_>>` only to satisfy `'static`.

```rust
use std::thread;
let mut v = vec![1, 2, 3];
thread::scope(|s| {
    s.spawn(|| { /* read-only borrow is fine */ });
    s.spawn(|| { /* can borrow &mut v in disjoint regions via interior logic */ });
    s.spawn(|| println!("len = {}", v.len()));
}); // all threads joined here; v is still valid
```

- **Thread naming and joining.** Name threads with `thread::Builder`, keep the `JoinHandle` and join it. Do not rely on process exit to clean up work.

```rust
use std::thread;
let h = thread::Builder::new().name("worker-1".into()).spawn(|| { /* work */ })?;
let res = h.join();
```

- **MPMC channels.** `crossbeam-channel` gives multi-producer multi-consumer channels and `select!` over receivers and timers. Handle disconnection. Do not use `std::sync::mpsc` for complex topologies.

```rust
use crossbeam_channel::{bounded, select, tick};
let (tx, rx) = bounded::<u32>(1024);
let ticker = tick(std::time::Duration::from_millis(10));
loop {
    select! {
        recv(rx) -> msg => if let Ok(x) = msg { /* handle */ } else { break },
        recv(ticker) -> _ => { /* periodic work */ },
        default(Duration::from_millis(1)) => { /* do other work */ }
    }
}
```

- **Rendezvous.** `std::sync::mpsc::sync_channel(0)` blocks the producer until the consumer receives; a small capacity throttles producers. Do not busy-wait where blocking is wanted.

```rust
use std::sync::mpsc;
let (tx, rx) = mpsc::sync_channel::<String>(0); // rendezvous
std::thread::spawn(move || { tx.send("hello".into()).ok(); });
let msg = rx.recv().unwrap();
```

- **One-time initialization.** Prefer `std::sync::OnceLock`/`LazyLock`; use `once_cell` only for an older MSRV. Do not use `lazy_static!` where these suffice.

```rust
use std::sync::OnceLock;
static CONFIG: OnceLock<String> = OnceLock::new();
fn config() -> &'static str { CONFIG.get_or_init(|| "default".to_string()) }
```

- **Atomic orderings.** Default to `Acquire`/`Release` for hand-off patterns; use `Relaxed` only with a proven invariant; use fences sparingly. Model with `loom`, which treats `SeqCst` operations as `AcqRel`. Keep `loom` tests deterministic.

```rust
use loom::{sync::{Arc, atomic::{AtomicUsize, Ordering::*}}, thread};
loom::model(|| {
  let n = Arc::new(AtomicUsize::new(0));
  let a = n.clone(); thread::spawn(move || { let cur = a.load(Acquire); a.store(cur+1, Release); });
  let b = n.clone(); thread::spawn(move || { let cur = b.load(Acquire); b.store(cur+1, Release); });
});
```

- **Fences order only atomic operations.** A fence does not make plain memory accesses visible across threads; never share non-atomic mutable state on the strength of one.

```rust
use std::sync::atomic::{AtomicBool, Ordering, fence};
static LOCK: AtomicBool = AtomicBool::new(false);
fn lock() { while LOCK.swap(true, Ordering::Acquire) {} }
fn unlock() { fence(Ordering::Release); LOCK.store(false, Ordering::Release); }
```

- **Lock-free building blocks.** Use `crossbeam-epoch` for deferred reclamation and `AtomicCell<T: Copy>` for simple shared slots. No hand-rolled hazard pointers or ad-hoc reclamation.
- **CPU data parallelism.** Replace hot sequential loops over large collections with Rayon's `into_par_iter()`. Keep work items independent, hold no locks inside, do not parallelize tiny tasks, and measure the speedup.

```rust
use rayon::prelude::*;
let sum: i64 = (0..1_000_000i64).into_par_iter().sum();
```

- **io_uring runtimes.** `monoio` (thread-per-core, non-`Send` tasks) and `tokio-uring` suit high-throughput I/O-bound Linux servers on kernel 5.11 or later. Benchmark on the real workload, gate behind a feature, and do not use them where epoll/kqueue suffices.

## 10. Unsafe and FFI

- Keep unsafe surfaces minimal.

### Unsafe and FFI containment patterns

- **Encapsulate unsafe behind a minimal surface, with SAFETY docs and Miri.** Unsafe is not wrong by default; undocumented unsafe is. Keep it small and private where possible, justify each block with a `SAFETY` comment and test it with Miri. Use it only where raw pointers, FFI, aliasing-sensitive optimization or manual memory invariants are truly required. Do not spread it across a wide public surface without one owned invariant boundary.
- **`MaybeUninit`, aliasing invariants and RAII guards.** Memory-safety mistakes cluster around manual initialization and raw-pointer writes. Separate "allocated but uninitialized", "safely initialized" and "resource must be released" into explicit phases and guards. Never create a reference to uninitialized memory. `&mut` implies uniqueness.
- **FFI layout, wide pointers and explicit nullability.** `&str`, `&[u8]` and `&dyn Trait` are not FFI-safe. Use explicit `repr` choices, `(ptr, len)` structs and `Option<NonNull<T>>` for nullability. Never export Rust fat pointers over FFI or assume default Rust layout is stable for external consumers.

Never let a panic cross FFI. Catch it and convert to an error code; consider `extern "C-unwind"` only with an explicit contract:

```rust
#[no_mangle]
pub extern "C" fn api_do(ptr: *const u8, len: usize) -> i32 {
  let res = std::panic::catch_unwind(|| unsafe { do_work(std::slice::from_raw_parts(ptr, len)) });
  match res { Ok(Ok(())) => 0, Ok(Err(_e)) => -2, Err(_panic) => -1 }
}
```

- **Nullable pointers:** model them as `Option<NonNull<T>>` or `Option<extern "C" fn()>`, which have a guaranteed representation. No magic sentinel integers.
- **Layout:** choose `repr(C)` or `repr(transparent)` whenever ABI stability is required.
- **Trait objects:** never construct vtables by hand in unsafe code or leak raw trait-object pointers.

- **Aliasing model.** `&mut` implies uniqueness and `&` implies immutability outside `UnsafeCell`. A read or write through an unrelated pointer can invalidate a reference. Set up raw pointers before writing, never write through a raw pointer while a shared reference is live, and validate with Miri (`cargo +nightly miri test` in CI).
- **`MaybeUninit`.** Write with `ptr::write`, and call `assume_init` only after every byte is initialized. Do not call `assume_init_mut` and read before initialization.

```rust
use std::{mem::MaybeUninit, ptr};
let mut buf: MaybeUninit<[u8; 4]> = MaybeUninit::uninit();
let p = buf.as_mut_ptr() as *mut u8;
unsafe { ptr::write(p, 1); ptr::write(p.add(1), 2); ptr::write(p.add(2), 3); ptr::write(p.add(3), 4); }
let arr = unsafe { buf.assume_init() };
```

- **Drop check.** When implementing `Drop` for a generic type, generic parameters must outlive `self`; do not hold references into shorter-lived data in a struct with `Drop`.
- **Fat pointers.** Never construct an invalid fat pointer or transmute between unrelated `dyn` types.
- **Public surface.** Keep unsafe internals private and do not expose raw pointers in public APIs. An `unsafe fn` contract must be sound and documented.

- **Representation choices.** `repr(C)` for FFI structs and enums; `repr(transparent)` for newtypes crossing FFI; primitive enum reprs such as `repr(u8)` only when required. Default `repr(Rust)` optimizes best. Do not read discriminants of enums without a `repr`, and avoid `repr(packed)`, which creates unaligned references.

```rust
#[repr(C)]
struct CTimeSpec { tv_sec: i64, tv_nsec: i64 }
#[repr(transparent)]
struct Fd(i32);
#[repr(u8)]
enum Kind { A, B(u32) }
```

- **dyn upcasting (Rust 1.86+).** `&dyn Sub` coerces to `&dyn Super`, also through `Box`, `Arc` and raw pointers. Remove `as_super()` helpers; never upcast by transmute.

```rust
trait Super {}
trait Sub: Super {}
fn take_super(x: &dyn Sub) -> &dyn Super { x }
```

- **Nullability at the boundary.** A `&T` or `&mut T` is never null. Keep `unsafe` at the boundary and wrap it in safe APIs.

```rust
use core::ptr::NonNull;
#[no_mangle]
pub extern "C" fn api(cb: Option<extern "C" fn(i32)>) -> i32 { if let Some(f) = cb { f(1); } 0 }
// Nullable pointer field
type MaybeBuf = Option<NonNull<u8>>;
```

- **Alignment and packing.** `#[repr(align(N))]` raises alignment, for cache lines for example. `#[repr(packed(n))]` creates unaligned fields: access them through raw pointers only, never take a reference to one, and do not combine `align` with `packed`.

```rust
#[repr(align(64))]
struct CacheLine([u8; 64]);
```

- **Enum discriminants.** Use `#[repr(u8)]` for C-like enums in FFI or wire formats, and inspect discriminants with `mem::discriminant`.
- **The `-sys` crate pattern.** Put raw bindings in `foo-sys` with `package.links = "foo"` and link metadata from its build script; a separate crate depends on it and exposes the safe API. Do not mix raw FFI and the safe wrapper in one crate.

```toml
# Cargo.toml
[package]
links = "foo"

[build-dependencies]
cc = "*"
```

## 11. Performance

### Performance without sacrificing correctness

- **Panic-free arithmetic and slicing.** External input plus unchecked indexing is a classic source of boundary bugs. Use `checked_*`, `saturating_*` and `.get()` for ranges, offsets, terminators, suffix stripping and parser cursor movement. Do not rely on "we already proved this above" in code that will change.
- **Builder plus frozen config struct.** Configuration is mutable during construction and immutable during execution; a builder that produces a cheap frozen config makes the split explicit. Use when a component has many orthogonal knobs and a stable execution phase. Keep runtime state and expensive artifacts out of the builder.
- **Accumulate, then build, collecting errors as you go.** Some structures (pattern sets, registries, ignore lists, aggregated configuration) can only be optimized once the whole batch is known. Collect non-fatal build-time errors separately from final construction. Do not force eager construction on every incremental addition.
- **Prepare once, query many.** Precompute a normalized or derived view once as a named value type, then reuse it across many checks: matching, routing, filtering, repeated comparison against one input. Avoid when precomputation costs more than the reuse saves or hides a freshness requirement.

### Memory-efficiency examples

```rust
use std::borrow::Cow;

// Conditional ownership with Cow
pub fn normalize_content(content: &str) -> Cow<str> {
    if content.contains('\r') {
        Cow::Owned(content.replace('\r', ""))
    } else {
        Cow::Borrowed(content)
    }
}

// Zero-allocation string processing
pub fn extract_mentions(content: &str) -> impl Iterator<Item = &str> {
    content
        .split_whitespace()
        .filter_map(|word| word.strip_prefix('@'))
}
```

Compile-time string matching with a macro:

```rust
// Compile-time string matching
macro_rules! command_matcher {
    ($($pattern:literal => $handler:expr),* $(,)?) => {
        pub fn handle_command(input: &str) -> Option<CommandResult> {
            match input {
                $($pattern => Some($handler),)*
                _ => None,
            }
        }
    };
}

command_matcher! {
    "/help" => CommandResult::Help,
    "/quit" => CommandResult::Quit,
    "/status" => CommandResult::Status,
}
```

### Allocator and build-time optimization

- **Global allocator.** Switch to jemalloc or mimalloc only when allocator behavior is a measured bottleneck; measure throughput, latency and RSS.

```rust
#[global_allocator]
static GLOBAL: mimalloc::MiMalloc = mimalloc::MiMalloc;
```

- **LTO, PGO and inlining.** Enable ThinLTO or fat LTO in release after measuring compile time and size; use `cargo-pgo` for profile-guided optimization; put `#[inline]` on tiny hot wrappers only, never blanket `inline(always)`.

```toml
[profile.release]
lto = "thin"
codegen-units = 1
```

### Caching and data processing

- **Caches.** `moka::Cache` for concurrent TTL/LRU caching; `cached` macros for function memoization. Bound the size and TTL; never cache non-deterministic results.

```rust
use moka::sync::Cache;
let cache = Cache::builder().max_capacity(10_000).build();
cache.insert("k", 1);
if let Some(v) = cache.get("k") { /* ... */ }
```

```rust
#[cached::cached(size=128)]
fn fib(n: u64) -> u64 { /* ... */ n }
```

- **Columnar analytics.** With Polars, prefer the lazy API for query planning and parallel execution, and streaming when memory-bound. Fix the query plan before tuning environment knobs.

```rust
use polars::prelude::*;
let df = df!("a" => &[1,2,3], "b" => &[4,5,6])?;
let out = df.lazy()
    .groupby([col("a")])
    .agg([col("b").sum()])
    .collect()?;
```

- **In-memory analytics.** Arrow with DataFusion gives columnar, vectorized SQL; do not convert Arrow data to row structs early.

### Benchmark harness (criterion)

```rust
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn benchmark_message_processing(c: &mut Criterion) {
    let messages = generate_test_messages(1000);
    
    c.bench_function("process_messages", |b| {
        b.iter(|| {
            for message in &messages {
                black_box(process_message(black_box(message)));
            }
        })
    });
}

criterion_group!(benches, benchmark_message_processing);
criterion_main!(benches);
```

### Panic strategy

Use `panic = "abort"` in release binaries (CLIs, embedded) where unwinding is undesirable, to fail fast and reduce binary size. Keep unwinding in debug builds for backtraces. Never set it in a library, and never abort in tests.

```toml
[profile.release]
panic = "abort"
```

## 12. Naming, modules and documentation

- Use four-word names for new functions and commands when feasible.
- Preserve public API compatibility when a rename is risky.
- Keep modules cohesive and docs synchronized with behavior.

- Treat Mermaid diagrams as a documentation convention only when the project already expects them.

- Apply the same naming clarity to new crates, folders and top-level commands when creating or renaming them is practical.
- When an existing public API cannot be renamed, keep it and add an adapter.

- Keep rustdoc examples executable and aligned with current behavior.
- Use structured tracing at system boundaries in async services.
- Never log secrets or sensitive payloads.

### Rules not to universalize

Do not treat these as default Rust quality rules:

- "Run `cargo clean` constantly."
- Doctrine copied verbatim into every skill or plan.
- Four-word naming when it would break a stable API or make a name materially worse.
- Mermaid-only documentation as a universal requirement.
- "MVP" used as cover for skipping tests, contracts or verification.

### Four-word naming pattern (local convention)

Where a repository adopts four-word names, the shape is `verb_constraint_target_qualifier()`: functions use underscores, crates, folders and commands use hyphens.

- Verb: `filter`, `render`, `detect`, `save`, `create`, `process`
- Constraint: `implementation`, `box_with_title`, `visualization_output`
- Target: `entities`, `unicode`, `file`, `database`
- Qualifier: `only`, `to`, `in`, `from`, `with`

```text
good: filter_implementation_entities_only()
good: render_box_with_title_unicode()
good: create_database_connection_pool_async()
bad:  filter_entities()                    (2 words)
bad:  detect_cycles_in_dependency_graph()  (5 words)
```

## 13. Anti-patterns

Reject these by default:

- vague requirements with no measurable assertions
- public APIs that accept `&Vec<T>` or `&String`
- library APIs that return `anyhow::Error`
- `unwrap()` or `expect()` in production paths without an invariant story
- blocking work directly on async executors
- holding locks or mutable borrows across `.await`
- unbounded channels in high-throughput or long-lived paths
- byte-processing code that assumes all input is UTF-8
- detached tasks with no lifecycle ownership
- concurrency code that has never been stress-tested or modeled
- L3 dependencies leaking into L1 core

Fatal anti-patterns; do not ship code with these:

1. Ambiguous requirements with no measurable assertions.
2. Monolithic "god object" structs with mixed responsibilities.
3. Performance claims without benchmark or contract tests.
4. Hard concrete dependencies that block unit testing.
5. Resource lifecycle leaks or missing cleanup guarantees.
6. Oversimplified domain models that ignore real constraints.
7. Layer violations: L3 dependencies leaking into L1 core.
8. Async or concurrency logic with no stress or race validation.

- public enums likely to grow but missing `#[non_exhaustive]`
- textual diagnostics that discard the exact failure location
- tests that cover examples but not invariants

### The eight fatal anti-patterns, in code

```rust
// Bad: "As a user, I want better performance"
// Good: Performance Contract with measurable test
#[test]
fn test_query_performance_contract() {
    // Query execution must complete within 500us
}

// Bad: Monolithic component with 20+ fields
pub struct SystemManager { /* everything */ }

// Bad: "This operation takes 5us" - no test to verify

// Bad: Cannot be tested in isolation
pub struct Component {
    db: SqliteConnection, // Hard dependency
}

// Bad: No cleanup strategy
pub struct FileProcessor {
    files: Vec<File>, // Never closed
}

// Bad: Won't handle real code
pub struct Function {
    name: String, // What about generics? Visibility? Async?
}

// Bad: L3 async code in L1 core
pub struct CoreProcessor {
    runtime: tokio::Runtime, // Mixing layers
}

// Bad: Shared mutable state without stress tests
```

Premature abstraction is a ninth: "make it generic so we can swap implementations later" is wrong; make it work correctly and fast first, then abstract if needed.

## 14. Rust web backends

This section applies to Rust HTTP backends and APIs (Actix, Axum or similar). For generic libraries, CLIs, parsers, protocol crates and FFI boundaries use sections 1 to 13 instead.

### Backend work modes

| Mode | Use for |
| --- | --- |
| Spec Mode | Vague backend requests, missing acceptance criteria, or greenfield service work that needs `REQ-WEB-*` contracts first |
| Delivery Mode | Endpoints, app state, persistence, external integrations and implementation sequencing |
| Operations Mode | Configuration, secrets, tracing, CI, Docker, deployment, migrations and rollout safety |
| Security Mode | Validation, credentials, password handling, session and cookie flows, reset flows and anti-enumeration behavior |
| Resilience Mode | Retries, idempotency, timeout handling, transactions, external API failures and background workers |
| Review Mode | Backend reviews where the question is production readiness, not generic Rust style |

Default combinations:

- new endpoint or feature: Spec + Delivery
- auth or session work: Spec + Security
- migration or deployment work: Delivery + Operations
- external integration or idempotent workflow: Delivery + Resilience
- backend review: Review + one or more of Security, Operations, Resilience

### Backend workflow

1. **Classify the task and choose modes.** Name the service slice first: endpoint, auth flow, external API client, migration, deployment, worker flow, or review. Decide whether the main risk is ambiguity, delivery sequencing, operational safety, security or resilience.
2. **Write executable requirements** as `REQ-WEB-<NNN>.<REV>` in `WHEN ... THEN ... SHALL` form. Reject "faster", "safer" or "more reliable" without a threshold or an observable outcome.
3. **Design the service boundaries before coding.** Separate the request handler, application state, domain types, persistence boundary and external integration boundary. Prefer typed inputs and typed domain objects over raw strings or loosely shaped payloads crossing several layers. Decide early which work stays inline in the request and which is handed to durable background processing.
4. **Choose the verification mix:** unit, integration, spawned-app tests, database-backed tests, HTTP mock tests, property tests, migration tests and rollout checks. Prefer integration-first coverage for endpoint behavior, wiring and persistence side effects.
5. **Apply the backend delivery rules** (below).
6. **Run delivery and operational gates before handoff:** format, lint, tests and build pass; every requirement is covered; non-functional claims have measurable evidence; migration and rollout safety is reviewed whenever schema or deployment behavior changes.

Output order: Backend Work Mode, Executable Requirements, Service Design, Verification Matrix, Implementation Plan, Quality Gates, Open Questions. Traceability table columns: `req_id | test_id | test_type | assertion | target`.

### Backend delivery rules

- Keep domain validation out of transport-only types. Transport validation is not the whole validation story; keep domain invariants explicit.
- Keep secrets redacted and configuration layered by environment.
- Treat tracing, request correlation, health checks and failure classification as design concerns, not polish.
- Treat idempotency, retries and transaction scope as correctness problems whenever external systems are involved.
- Do not handle work synchronously in the request when it needs durable retries, deduplication or long-running external calls, unless the tradeoff is stated.
- Do not design password or session flows without addressing storage, failure behavior and async-safe verification boundaries.
- Do not treat deployment and migrations as postscript tasks when schema or background workflow behavior changes.

### Backend security hardening checklist

DoS mitigation:

- [ ] `TimeoutLayer` prevents slow-client attacks
- [ ] `tower_governor` provides rate limiting
- [ ] `DefaultBodyLimit` prevents memory exhaustion
- [ ] Bounded channels prevent unbounded queues

Data protection:

- [ ] Input validation with `serde` + `validator`
- [ ] TLS enforcement with `rustls`
- [ ] Memory wiping with `zeroize` for sensitive data
- [ ] Constant-time comparison with `subtle` for crypto

### Database pool and compile-time checked queries

```rust
// Shared pool with proper error handling
#[derive(Clone)]
pub struct Database {
    pool: sqlx::PgPool,
}

impl Database {
    pub async fn new(database_url: &str) -> Result<Self, sqlx::Error> {
        let pool = sqlx::PgPool::connect(database_url).await?;
        sqlx::migrate!("./migrations").run(&pool).await?;
        Ok(Self { pool })
    }
    
    // Compile-time query validation
    pub async fn get_user(&self, id: UserId) -> Result<Option<User>, sqlx::Error> {
        sqlx::query_as!(
            User,
            "SELECT id, name, email FROM users WHERE id = $1",
            id.0
        )
        .fetch_optional(&self.pool)
        .await
    }
}
```

### Axum service template

```rust
use axum::{
    extract::{State, Path, Json},
    response::Json as ResponseJson,
    routing::{get, post},
    Router,
};
use tower::{ServiceBuilder, timeout::TimeoutLayer};
use tower_http::{trace::TraceLayer, cors::CorsLayer};

#[derive(Clone)]
pub struct AppState {
    db: Database,
    config: AppConfig,
}

pub fn create_app(state: AppState) -> Router {
    Router::new()
        .route("/api/health", get(health_check))
        .route("/api/users", post(create_user))
        .route("/api/users/:id", get(get_user))
        .layer(
            ServiceBuilder::new()
                .layer(TimeoutLayer::new(Duration::from_secs(30)))
                .layer(TraceLayer::new_for_http())
                .layer(CorsLayer::permissive())
        )
        .with_state(state)
}

async fn health_check() -> &'static str {
    "OK"
}

async fn create_user(
    State(state): State<AppState>,
    Json(payload): Json<CreateUserRequest>,
) -> Result<ResponseJson<User>, AppError> {
    payload.validate()?;
    let user = state.db.create_user(payload).await?;
    Ok(ResponseJson(user))
}
```

### Configuration, storage and messaging choices

- **Layered configuration.** Defaults, then files, then environment, deserialized into one typed struct through a central builder (`config`, `dotenvy` in development, `envy`). Document precedence; do not hand-parse env or scatter config reads.

```rust
#[derive(serde::Deserialize)]
struct Settings { db_url: String, workers: usize }
let mut cfg = config::Config::builder()
    .set_default("workers", 4)?
    .add_source(config::File::with_name("Config").required(false))
    .add_source(config::Environment::default())
    .build()?;
let s: Settings = cfg.try_deserialize()?;
```

- **Diesel.** Compile-time checked queries with `diesel_cli` migrations; keep the generated `schema.rs` in sync and do not fall back to string queries.
- **Embedded key-value stores.** RocksDB: LSM, high write throughput, needs tuning. Sled: pure Rust, single process, may use more space. LMDB: memory-mapped, strong read throughput, multi-process, one writer at a time. Measure space and write amplification before choosing.
- **Messaging.** NATS for simple pub/sub, with JetStream for at-least-once; Kafka (`rdkafka`) for partitions and consumer groups; Pulsar for topic partitioning with an async API. Bound consumers, make handlers idempotent with dedupe keys, and do not assume exactly-once.
- **JetStream.** Durable consumers with explicit acks, sized ack waits and bounded pull batches.

```rust
// sync nats crate example (JetStream)
let nc = nats::connect("nats://127.0.0.1:4222")?;
let js = nats::jetstream::new(nc);
js.add_stream(nats::jetstream::StreamConfig {
    name: "events".into(), subjects: vec!["events.*".into()], ..Default::default()
})?;
let mut sub = js.subscribe("events.foo")?; // durable can be configured via consumer APIs
js.publish("events.foo", "hello")?;
if let Some(msg) = sub.next() { msg.ack()?; }
```

- **Kafka.** Use `StreamConsumer` with async and `FutureProducer` for backpressure-aware sends; choose manual or auto commit explicitly; handle rebalances; no synchronous commits on the hot path.

```rust
use rdkafka::{ClientConfig, consumer::{CommitMode, StreamConsumer}, message::BorrowedMessage};
use futures::StreamExt;
let consumer: StreamConsumer = ClientConfig::new()
  .set("group.id", "g1").set("bootstrap.servers", "localhost:9092")
  .create()?;
consumer.subscribe(&["input"])?;
let mut stream = consumer.stream();
while let Some(Ok(m)) = stream.next().await {
    handle(&m.payload().unwrap_or(&[]));
    consumer.commit_message(&m, CommitMode::Async)?;
}
```

- **Redis.** Pool connections with `deadpool-redis`; take short-lived connections, set timeouts and a maximum size, and do not hold one across long await chains.

```rust
use deadpool_redis::{Config, Runtime};
use redis::AsyncCommands;
let cfg = Config::from_url("redis://127.0.0.1/");
let pool = cfg.create_pool(Some(Runtime::Tokio1))?;
let mut conn = pool.get().await?;
conn.set::<_, _, ()>("k", "v").await?;
let v: String = conn.get("k").await?;
```

- **Search.** Use the official OpenSearch or Elasticsearch client with typed bodies or `serde_json::json!`; handle 429 with backoff, set timeouts, and chunk bulk requests.

## 15. Tauri desktop apps

Tauri work is neither only frontend work nor only Rust work. Decide what must be specified, what must be designed across the frontend, command, Rust core and desktop boundaries, and what must be verified. Where Tauri-specific security or lifecycle guidance conflicts with a generic Rust default, the Tauri guidance wins.

### Tauri work modes

| Mode | Use when |
| --- | --- |
| Spec Mode | The request is vague, acceptance criteria are missing, or the work needs `REQ-TAURI-*` contracts first. Emphasis: contracts, acceptance criteria, traceability |
| App Architecture Mode | The task needs command boundaries, managed state, IPC shape, frontend/backend contracts, module structure or build seam decisions. Emphasis: invoke contracts, managed state, module shape, build seams |
| Desktop Security Mode | The main risk is permissions or trust boundaries: capabilities, filesystem or plugin scope, CSP, sidecars, updater trust |
| Lifecycle Mode | The main risk is desktop runtime behavior: tray, single-instance, deep links, window state, startup/setup, external binary packaging, platform config drift |
| Review Mode | The question is whether the app will stay safe, reliable and operable under change. Emphasis: anti-patterns, safety, operability, compatibility, final gates |

Default combinations:

- vague feature request: Spec + App Architecture
- command, state or frontend IPC work: Spec + App Architecture
- filesystem, plugin, capability or sidecar work: App Architecture + Desktop Security
- updater, tray, deep-link, single-instance or window-state work: Desktop Security + Lifecycle
- review or hardening pass: Review + one or more of the above

### Tauri workflow

1. **Classify the task and choose modes.** Name the component type first: feature request, command or IPC surface, permission boundary, sidecar or external binary, lifecycle path, or review.
2. **Write executable requirements** as `REQ-TAURI-<NNN>.<REV>` in `WHEN ... THEN ... SHALL` form. Reject "safer" or "more reliable" without a threshold or an explicit boundary effect.
3. **Define the design before coding.** Split it across the frontend contract, the command layer, the Rust core, and the desktop capability and lifecycle boundaries. Keep the frontend invoke contract explicit. Keep command functions thin so the deeper Rust logic stays testable.
4. **Choose the verification mix:** Rust unit, Rust integration, frontend tests, typed invoke contract checks, mocked Tauri boundary tests, desktop boundary tests; performance tests only when a metric is stated. Do not default to one layer only.
5. **Apply the Tauri reliability rules** (below).
6. **Apply local conventions selectively:** four-word names for new functions and commands when feasible; preserve API, window, command and event compatibility when a rename is risky; keep modules cohesive and the registration structure explicit.
7. **Run quality gates and anti-pattern checks before handoff.**

Output order: Tauri Work Mode, Executable Requirements, Tauri Design (Frontend/IPC/Rust Core + Permissions/Lifecycle), Verification Matrix, Implementation Plan, Quality Gate Results, Open Questions. Use the same traceability table as section 2.

### Tauri priorities by task type

| Task type | Prioritize |
| --- | --- |
| Commands and frontend IPC | Typed invoke contracts; serializable command errors; async command ownership rules; a clear split between the command layer and the deeper Rust core; Rust integration tests plus frontend contract tests |
| Shared state and Rust core | Managed state discipline; explicit state ownership and synchronization choice; centralized command registration and module structure; Rust unit and integration tests around the core boundary |
| Capabilities, permissions, filesystem or plugin access | Capability scoping by window label; least-privilege filesystem and plugin access; CSP hardening where relevant; permission review before feature convenience |
| Sidecars and external binaries | Exact sidecar permissions and arguments; startup bounds, health checks, restart policy and log caps; explicit external binary packaging; lifecycle ownership and failure visibility |
| Lifecycle and platform integration | Setup/startup boundaries; tray event flow; single-instance handoff; deep-link routing; window-state restore; platform config drift management |
| Review or hardening pass | Panic and serialization risks in command paths; permission creep; lifecycle ownership gaps; event spam and binary payload misuse |

### Tauri requirements

Use the template of section 3 with `REQ-TAURI-001.0` identifiers. Use explicit units for latency, payload size, retries, startup bounds and resource limits. Split security, lifecycle and operability requirements; do not hide them in one broad clause.

Use `REQ-TAURI-*` identifiers even when the request begins as a generic desktop feature.

| Vague statement | Executable rewrite |
| --- | --- |
| "Add a Tauri sync feature." | "Expose a typed frontend invoke contract and a Rust command that validates input, reports progress, and returns a serializable result for the sync operation." |
| "Make permissions safer." | "Restrict filesystem and plugin capabilities to the minimum paths and commands needed by the named windows and sidecars." |
| "Handle app startup better." | "Initialize required state during setup without blocking the UI thread and restore the app to a ready state within the stated startup bound." |
| "Support tray and deep links." | "Route tray actions and deep-link events to the primary instance without spawning duplicate background workers or losing window focus semantics." |
| "Improve reliability." | "Return typed frontend-visible errors, avoid panics in command and lifecycle paths, and bound sidecar startup/retry behavior." |

Work packet shape for a request that is not ready for coding:

```markdown
## Tauri Work Mode
- Spec Mode
- App Architecture Mode

## Executable Requirements
### REQ-TAURI-001.0: <title>
**WHEN** ...
**THEN** the system SHALL ...
**AND** SHALL ...
**SHALL** ...

## Tauri Design (Frontend/IPC/Rust Core + Permissions/Lifecycle)
- Frontend contract:
- Command layer:
- Rust core:
- Managed state:
- Capabilities and permissions:
- Sidecars and external binaries:
- Lifecycle and platform behavior:

## Verification Matrix
| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |

## Implementation Plan
1. STUB
2. RED
3. GREEN
4. REFACTOR
5. VERIFY

## Quality Gate Results
- fmt:
- clippy:
- rust tests:
- rust build:
- frontend checks:
- tauri checks:
```

### Tauri design scaffold

| Area | Role | Question to ask |
| --- | --- | --- |
| Frontend contract | Typed invoke payloads, responses, events or channels | What exact UI-facing boundary should stay stable? |
| Command layer | Tauri commands and request validation | What belongs in the command boundary versus deeper Rust services? |
| Rust core | Domain logic, adapters, state types, sidecar supervision | What should stay testable and framework-light? |
| Managed state | Tauri-managed shared state and synchronization | What state is shared, and what mutex model fits it? |
| Capabilities and permissions | Capability files, labels, filesystem and plugin scope | What is the least-privilege set for the actual windows and actions? |
| Lifecycle and packaging | Setup, tray, updater, single-instance, deep links, external binaries | What lifecycle ownership and packaging guarantees are required? |

- Make the frontend invoke contract explicit before implementation.
- Choose the narrowest typed request/response or stream contract the UI should rely on.
- Scope permissions by real window labels and concrete actions, not UI titles or future hopes.
- Decide the mutex or async-mutex discipline for each piece of shared mutable state.
- Treat sidecars, updater, tray and single-instance behavior as design decisions, not afterthoughts.
- Treat lifecycle and packaging as part of design, not deployment cleanup.

### Tauri verification matrix

| Verification type | Choose it when |
| --- | --- |
| Rust unit | Behavior is local and deterministic inside the Rust core |
| Rust integration | Behavior crosses command, adapter or serialization boundaries |
| frontend test | UI logic depends on typed command or event results |
| typed invoke contract check | Stringly-typed IPC drift is a material risk |
| mocked Tauri boundary test | Desktop runtime behavior must be validated without a full live shell |
| desktop boundary test | Tray, deep links, single-instance, updater or window-state behavior is central |
| performance | Latency or payload thresholds were explicitly stated |

Follow the TDD loop of section 5, with one test or test skeleton per `REQ-TAURI-*`. Run the command gates of section 16 plus the repo's normal frontend and Tauri checks for the changed boundary.

In STUB, define the command payloads, expected responses, window and capability assumptions, and fixtures.

Example matrix:

| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |
| REQ-TAURI-001.0 | TEST-RUST-UNIT-001 | rust-unit | command service validates normalized request shape | correctness |
| REQ-TAURI-001.0 | TEST-RUST-INTEG-002 | rust-integration | command returns serializable `AppError` on invalid input | boundary |
| REQ-TAURI-002.0 | TEST-FRONTEND-003 | frontend | typed invoke caller handles success and failure shapes | contract |
| REQ-TAURI-003.0 | TEST-MOCK-004 | mocked-tauri | UI reacts correctly to mocked IPC and window behavior | desktop-boundary |
| REQ-TAURI-004.0 | TEST-LIFECYCLE-005 | desktop-boundary | second launch triggers single-instance handoff | lifecycle |
| REQ-TAURI-005.0 | TEST-PERF-006 | performance | p99 command latency < 100ms for stated fixture | latency |

### Tauri test skeletons

Rust unit:

```rust
#[test]
fn test_req_tauri_001_command_validates_payload() {
    let input = create_valid_request_payload();
    let output = normalize_command_request(input).unwrap();
    assert_eq!(output.command_name, "sync-workspace");
}
```

Rust integration:

```rust
#[tokio::test]
async fn test_req_tauri_002_command_returns_serializable_error() {
    let result = run_sync_workspace_command(invalid_request()).await;
    assert!(matches!(result, Err(AppError::InvalidRequest(_))));
}
```

Frontend typed invoke:

```ts
it("TEST-FRONTEND-001 handles typed invoke contract", async () => {
  const result = await invokeSyncWorkspaceSafely(validPayload);
  expect(result.status).toBe("completed");
});
```

Mocked Tauri boundary:

```ts
it("TEST-MOCK-002 recovers from desktop command failure", async () => {
  mockIPC((cmd) => {
    if (cmd === "sync_workspace") {
      throw new Error("permission denied");
    }
  });
  render(<SyncWorkspaceScreen />);
  expect(await screen.findByText(/permission denied/i)).toBeVisible();
});
```

Lifecycle boundary test:

- Launch the primary instance.
- Trigger a second launch or a deep-link open.
- Assert the handoff reaches the primary window.
- Assert no duplicate long-running background service remains active.

Performance contract:

```rust
#[test]
fn test_req_tauri_003_command_performance_contract() {
    use std::time::{Duration, Instant};
    let fixture = create_large_fixture();
    let start = Instant::now();
    let _ = evaluate_preview_command(fixture).unwrap();
    assert!(start.elapsed() < Duration::from_millis(100));
}
```

### Tauri review questions

- Which mode or combination of modes is active, and which one is primary?
- What is the smallest set of `REQ-TAURI-*` contracts that makes the work testable?
- What belongs in the frontend contract, the command layer and the Rust core respectively?
- Which boundaries require capability, sidecar-policy or lifecycle-ownership decisions?
- Which risks deserve Rust tests, frontend tests, mocked desktop tests or desktop boundary checks instead of unit tests alone?
- Which names, command IDs or window labels must stay stable even if a cleaner new name exists?

### Tauri default reliability and security stack

If you do not know what to prioritize, work down this list:

1. Make frontend-to-command contracts explicit and typed.
2. Keep command failures serializable and user-reachable paths panic-free.
3. Keep shared mutable state in disciplined Tauri-managed boundaries.
4. Make permissions least-privilege by window label and action.
5. Use channels or binary responses for large or long-running IPC.
6. Supervise sidecars and external binaries explicitly.
7. Treat updater, tray, deep links, single-instance and window state as correctness concerns.

### Tauri reliability and security rules

- Command errors are serializable and visible to the frontend. Never panic in a command.
- Keep managed state disciplined.
- Capabilities are least-privilege by default. Scope filesystem, plugin, sidecar and updater permissions.
- Bound the sidecar lifecycle; keep binary packaging and lifecycle ownership explicit.
- Async command inputs are owned values.
- Treat tray, deep links, single-instance and startup/setup behavior as correctness concerns, not polish.
- Stay skeptical about: malformed input, permission creep, event spam, detached sidecars, updater trust, and lifecycle drift across platforms.

- When a rename is risky, keep command IDs, event names and window labels stable. Keep command registration centralized.

- Make I/O-heavy commands async.
- Return `Result<T, AppError>` or an equivalent serializable shape from every fallible command.
- Package sidecars deterministically.
- This guidance targets Tauri 2.

- Keep shared mutable state in Tauri-managed state with the narrowest mutex that fits the access pattern.
- Scope filesystem, plugin and sidecar permissions exactly, not broadly.
- Use the plugin store for small structured state, not large blobs.
- Use channels or binary responses for long-running or high-volume payloads; do not spam events.
- Supervise sidecars with startup checks, bounded waits, explicit restart rules and explicit binary packaging declarations.
- Keep docs, examples, tests and capability and config files synchronized with behavior changes.

### Tauri non-negotiables

- All fallible commands return `Result<T, AppError>`.
- Async commands use owned inputs.
- Shared mutable state lives in Tauri-managed mutexes, not ad hoc globals.
- Capabilities are window-scoped and least-privilege.
- `plugin-store` is for small structured state, not binary payloads.
- Large or streaming IPC uses channels or binary responses, not event spam.
- Sidecars get health checks, bounded startup waits, explicit restart rules and log caps.
- No `unwrap()` or `expect()` in command paths that users can hit.

### Tauri pattern catalog

Scope: Tauri 2 app-layer work. It does not cover plugin-author internals, mobile-only APIs or non-Tauri desktop shells.

**Commands and state**

- **Async command handlers.** Use an async command for anything that touches disk, network, process spawning or can otherwise stall the UI. Use owned inputs (`String`, not `&str`). Never call `std::thread::sleep` inside one. Keep `generate_handler!` registration in one place.

  ```rust
  use serde::Serialize;

  #[derive(Serialize)]
  struct GreetResponse {
      message: String,
  }

  #[tauri::command]
  async fn greet_user(name: String) -> Result<GreetResponse, AppError> {
      tokio::time::sleep(std::time::Duration::from_millis(50)).await;
      Ok(GreetResponse {
          message: format!("Hello, {name}!"),
      })
  }
  ```

- **Managed state.** Let Tauri manage global state and add interior mutability only where needed. Use `std::sync::Mutex` for short synchronous access. Use `tauri::async_runtime::Mutex` only when the lock must live across `.await`. Do not wrap state in `Arc` before `.manage(...)`; Tauri already shares it. Use dedicated state types and aliases so command signatures stay consistent.
- **Serializable errors.** Make every frontend-visible failure explicit and serializable (a `thiserror` enum that implements `Serialize`). Preserve a readable structured error; do not panic and do not collapse to an opaque string late.
- **Command module structure.** Keep command modules and registration explicit so naming and handler wiring are easy to audit. Avoid hidden command sprawl.
- **Typed frontend invoke.** Wrap `invoke` in centralized typed functions; do not scatter stringly-typed calls. Normalize error and result shapes at that boundary.

**Security**

- **Minimal capabilities.** Capabilities are the primary Tauri 2 security boundary. Scope them by window label, platform and permission set. Grant the minimum command and plugin access each window needs. Treat broad filesystem or shell permissions as security decisions.
- **Window labels.** Labels, not titles, are the security boundary. Scope capability differences between windows intentionally.
- **Path scopes.** Resolve paths through scope-aware APIs. Keep path decisions close to capability definitions. Reject over-broad path assumptions and unchecked traversal.
- **Official plugins.** Prefer official plugins over custom OS bridging, and match each with explicit permission scope; the permission scope is the safety story, not the plugin choice.
- **CSP.** Keep the content security policy explicit, and do not widen it to unblock convenience code.
- **Updater.** Treat signatures, channels and artifact provenance as part of correctness.
- **Raw requests.** Drop to raw request handling only when JSON helpers are not enough. Validate early and keep the parsing logic narrow and auditable.

**IPC shape**

- **Channels** for sustained streams and long-running or high-volume progress; keep payloads bounded and explicit.
- **Events** for sparse notifications and coarse progress only.
- **Binary responses** for binary payloads; do not degrade them into giant JSON blobs.

**Persistence**

- **Bound store payload sizes.** Keep large data out of store-backed persistence.
- **Blobs out of band.** Keep metadata in structured state and large binary or document payloads in files with explicit path and lifecycle handling.

**Sidecars**

- **Supervise the lifecycle.** Health checks, bounded and observable startup, explicit restart rules, log caps, and a named owner for the child process.
- **Scope permissions exactly.** Whitelist the executable and its expected arguments. Avoid generic shell escape hatches.
- **Declare external binaries explicitly.** Packaging must be exact about names, target triples and ownership.

**Lifecycle and build**

- **Setup.** Keep setup logic bounded: initialize just enough state, and hand long-running work to owned, supervised paths.
- **Tray.** Keep tray behavior lifecycle-aware with deterministic state transitions; avoid duplicate or conflicting event wiring.
- **Single instance.** Route a second launch deterministically to the primary instance.
- **Deep links.** Handle them together with single-instance handoff; they mix OS integration, IPC and a trust boundary.
- **CLI contracts.** Model desktop launch semantics explicitly.
- **Window state.** Restore window state without a visible flash.
- **Build hooks.** Treat the frontend/backend build seam as part of the design.
- **Platform configs.** Put platform differences in explicit config, not scattered runtime branches.

### Tauri code examples

**Managed state with a dedicated type alias**

```rust
use std::sync::Mutex;
use tauri::State;

#[derive(Default)]
struct AppState {
    counter: i32,
    user_name: Option<String>,
}

type ManagedAppState = Mutex<AppState>;

#[tauri::command]
fn increment_counter(state: State<'_, ManagedAppState>) -> Result<i32, AppError> {
    let mut state = state.lock().map_err(|_| AppError::StatePoisoned)?;
    state.counter += 1;
    Ok(state.counter)
}

pub fn run() {
    tauri::Builder::default()
        .manage(Mutex::new(AppState::default()))
        .invoke_handler(tauri::generate_handler![increment_counter])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

**Serializable command error**

```rust
use serde::Serialize;
use thiserror::Error;

#[derive(Debug, Error)]
enum AppError {
    #[error("state lock poisoned")]
    StatePoisoned,
    #[error("io error: {0}")]
    Io(String),
    #[error("file not found: {0}")]
    FileNotFound(String),
    #[error("permission denied: {0}")]
    PermissionDenied(String),
    #[error("invalid request: {0}")]
    InvalidRequest(&'static str),
    #[error("sidecar failed: {0}")]
    Sidecar(String),
}

impl Serialize for AppError {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        serializer.serialize_str(self.to_string().as_str())
    }
}
```

Contract: when a command fails it rejects with a typed error, the error serializes cleanly for the frontend, and the command does not panic. Avoid `unwrap()` in commands, raw `String` errors everywhere, and leaking opaque backend-only error types to JS.

**Capability file** (`src-tauri/capabilities/`)

```json
{
  "identifier": "default",
  "description": "Main window capability",
  "windows": ["main"],
  "permissions": [
    "core:default",
    "dialog:allow-open",
    "fs:allow-read-text-file",
    {
      "identifier": "fs:scope",
      "allow": ["$APPDATA/*", "$DOCUMENT/MyApp/**"]
    }
  ]
}
```

- Grant permissions per window, not per app.
- Prefer granular permissions such as `fs:allow-read-text-file` over `fs:default`.
- Scope filesystem access to exact directories and patterns.
- Sidecars need explicit shell permissions for execute or spawn.
- Never grant `"permissions": ["fs:default", "shell:default"]` as a convenience.

The safest bug is the one the window cannot perform.

**Scope-anchored file access** (frontend)

```typescript
import {
  BaseDirectory,
  exists,
  mkdir,
  readTextFile,
  writeTextFile,
} from '@tauri-apps/plugin-fs';

export async function loadSettings(): Promise<Settings> {
  const name = 'settings.json';

  if (!(await exists(name, { baseDir: BaseDirectory.AppData }))) {
    return defaultSettings;
  }

  const text = await readTextFile(name, {
    baseDir: BaseDirectory.AppData,
  });

  return JSON.parse(text) as Settings;
}

export async function saveSettings(settings: Settings): Promise<void> {
  await mkdir('.', { baseDir: BaseDirectory.AppData, recursive: true });
  await writeTextFile('settings.json', JSON.stringify(settings, null, 2), {
    baseDir: BaseDirectory.AppData,
  });
}
```

- Treat paths as capability-bound resources, not free-form strings.
- Prefer `BaseDirectory`-anchored access over hand-built absolute paths.
- Keep user data in app-specific directories when possible.
- Every accessed path must match `fs:scope`.
- Constrain paths early; path bugs become cross-platform bugs.

**Plugin registration**

```rust
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_store::Builder::default().build())
        .plugin(tauri_plugin_fs::init())
        .plugin(tauri_plugin_shell::init())
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

- Register every plugin explicitly via `.plugin(...)` and add the matching capability permissions.
- Keep the plugin count intentional; every plugin expands the authority surface.

**Typed invoke wrapper** (frontend)

```typescript
import { invoke } from '@tauri-apps/api/core';

interface GreetResponse {
  message: string;
}

export async function greetUser(name: string): Promise<GreetResponse> {
  return invoke<GreetResponse>('greet_user', { name });
}
```

- Never scatter raw command strings across the UI.
- Prefer generated bindings when using `specta` or similar tooling.

**Channel progress plus binary response**

```rust
use serde::Serialize;
use tauri::ipc::{Channel, Response};

#[derive(Clone, Serialize)]
struct DownloadProgress {
    bytes_downloaded: u64,
    total_bytes: u64,
}

#[tauri::command]
async fn download_file(
    url: String,
    on_progress: Channel<DownloadProgress>,
) -> Result<Response, AppError> {
    let bytes = reqwest::get(url)
        .await
        .map_err(|e| AppError::Sidecar(e.to_string()))?
        .bytes()
        .await
        .map_err(|e| AppError::Sidecar(e.to_string()))?;

    on_progress
        .send(DownloadProgress {
            bytes_downloaded: bytes.len() as u64,
            total_bytes: bytes.len() as u64,
        })
        .map_err(|e| AppError::Sidecar(e.to_string()))?;

    Ok(Response::new(bytes.to_vec()))
}
```

- Channels are for high-frequency, ordered progress; large binary payloads use `tauri::ipc::Response`.
- Do not fake streaming with hundreds of tiny `invoke` calls.

**Window-targeted event**

```rust
use tauri::{AppHandle, Emitter, Manager};

fn notify_window(app: &AppHandle, label: &str, message: &str) {
    if let Some(window) = app.get_webview_window(label) {
        let _ = window.emit("notification", message);
    }
}
```

- Use events for user-visible state changes, background completion and window-targeted notifications.
- Always clean up listeners on unmount. Keep payloads small and serializable.

**CSP** (`tauri.conf.json`)

```json
{
  "app": {
    "security": {
      "csp": {
        "default-src": "'self'",
        "script-src": "'self'",
        "style-src": "'self' 'unsafe-inline'",
        "img-src": "'self' data: https:",
        "connect-src": "'self' https://api.example.com",
        "frame-src": "'none'"
      },
      "dangerousDisableAssetCspModification": false
    }
  }
}
```

- Keep `default-src` and `script-src` tight; avoid remote script execution.
- Allow only the outbound connections you need.
- Leave `dangerousDisableAssetCspModification` set to `false`.

**Supervised sidecar**

```rust
use std::collections::VecDeque;
use std::sync::Mutex;
use std::time::{Duration, Instant};
use tauri::{AppHandle, Manager, State};
use tauri_plugin_shell::{
    process::{CommandChild, CommandEvent},
    ShellExt,
};

#[derive(Default)]
struct SidecarState {
    child: Mutex<Option<CommandChild>>,
    logs: Mutex<VecDeque<String>>,
}

#[tauri::command]
async fn ensure_sidecar_ready(
    app: AppHandle,
    state: State<'_, SidecarState>,
) -> Result<String, AppError> {
    let url = "http://127.0.0.1:7780".to_string();
    if check_local_health(&url).await {
        return Ok(url);
    }

    if let Some(mut child) = state
        .child
        .lock()
        .map_err(|_| AppError::StatePoisoned)?
        .take()
    {
        let _ = child.kill();
    }

    let (mut rx, child) = app
        .shell()
        .sidecar("my-sidecar")
        .map_err(|e| AppError::Sidecar(e.to_string()))?
        .args(["serve"])
        .spawn()
        .map_err(|e| AppError::Sidecar(e.to_string()))?;

    *state
        .child
        .lock()
        .map_err(|_| AppError::StatePoisoned)? = Some(child);

    tauri::async_runtime::spawn(async move {
        while let Some(event) = rx.recv().await {
            match event {
                CommandEvent::Stdout(bytes) | CommandEvent::Stderr(bytes) => {
                    let _line = String::from_utf8_lossy(&bytes);
                }
                _ => {}
            }
        }
    });

    wait_until_healthy(&url, Duration::from_secs(30)).await?;
    Ok(url)
}

async fn check_local_health(url: &str) -> bool {
    let Ok(parsed) = reqwest::Url::parse(url) else {
        return false;
    };

    let Ok(client) = reqwest::Client::builder()
        .timeout(Duration::from_secs(3))
        .no_proxy()
        .build()
    else {
        return false;
    };

    let Ok(health_url) = parsed.join("/health") else {
        return false;
    };

    client
        .get(health_url)
        .send()
        .await
        .map(|r| r.status().is_success())
        .unwrap_or(false)
}

async fn wait_until_healthy(url: &str, timeout: Duration) -> Result<(), AppError> {
    let started = Instant::now();
    while started.elapsed() < timeout {
        if check_local_health(url).await {
            return Ok(());
        }
        tokio::time::sleep(Duration::from_millis(100)).await;
    }
    Err(AppError::Sidecar("startup timed out".into()))
}
```

Sidecar rules: treat it as a subsystem, not a shell command.

- Keep the child handle in managed state.
- Kill the old child before spawning a replacement.
- Poll health with a bounded timeout.
- Disable proxy use for loopback health checks.
- Cap sidecar logs with a ring buffer.
- Whitelist the executable name and allowed args in capabilities.

**Store payload policy** (frontend)

```typescript
type PersistPolicy = {
  warnBytes: number;
  maxBytes: number;
  onOversize: 'drop' | 'truncate' | 'blobRef';
};

const policies: Record<string, PersistPolicy> = {
  promptHistory: { warnBytes: 128 * 1024, maxBytes: 256 * 1024, onOversize: 'blobRef' },
  promptDraft: { warnBytes: 64 * 1024, maxBytes: 128 * 1024, onOversize: 'blobRef' },
  terminal: { warnBytes: 64 * 1024, maxBytes: 128 * 1024, onOversize: 'truncate' },
};

function estimatePersistedBytes(value: unknown): number {
  return new TextEncoder().encode(JSON.stringify(value)).length;
}
```

- Put hard byte caps on hot keys; truncate or externalize oversize payloads.
- If a rollout period is needed, log oversize writes before enforcing the cap.

**Blobs out of band**

```text
Small JSON state -> plugin-store
Large binary payloads -> app data files
Persisted state -> blob reference only
Hydration -> lazy, only when needed
```

- Image and file metadata lives in the store; blob bytes live under app data.
- State stores a `blob_id`, never base64.
- Cleanup is TTL-based or reference-scan based.
- This matters most for apps that accumulate screenshots, chat attachments or terminal snapshots.

**Updater** (`tauri.conf.json`)

```json
{
  "plugins": {
    "updater": {
      "pubkey": "YOUR_PUBLIC_KEY",
      "endpoints": [
        "https://releases.example.com/{{target}}/{{arch}}/{{current_version}}"
      ]
    }
  }
}
```

- Sign updates. Embed only the public key. Never commit the private signing key.
- Surface download progress through a channel or an explicit progress callback.
- On Windows, account for quit-and-install behavior.

**Command modules**

```rust
// src-tauri/src/commands/files.rs
#[tauri::command]
pub async fn read_settings_file() -> Result<String, AppError> {
    std::fs::read_to_string("settings.json").map_err(|e| AppError::Io(e.to_string()))
}

// src-tauri/src/commands/windows.rs
#[tauri::command]
pub fn show_main_window(window: tauri::WebviewWindow) -> Result<(), AppError> {
    window.show().map_err(|e| AppError::Io(e.to_string()))?;
    Ok(())
}

// src-tauri/src/commands/mod.rs
pub mod files;
pub mod windows;

// src-tauri/src/lib.rs
mod commands;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            commands::files::read_settings_file,
            commands::windows::show_main_window,
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

- Commands defined in `lib.rs` must not be `pub`.
- Commands in separate modules should be `pub`.
- Command names are global, not module-scoped, so they must be unique across modules.
- Call `invoke_handler(...)` once, with a single `generate_handler![...]` list.

**Setup lifecycle**

```rust
use tauri::{AppHandle, Manager};

async fn warm_start_services(app: AppHandle) {
    if let Some(window) = app.get_webview_window("main") {
        let _ = window.emit("app-warm-started", ());
    }
}

#[tauri::command]
async fn reveal_main_window(app: AppHandle) -> Result<(), AppError> {
    if let Some(window) = app.get_webview_window("main") {
        window.show().map_err(|e| AppError::Io(e.to_string()))?;
        window.set_focus().map_err(|e| AppError::Io(e.to_string()))?;
    }
    Ok(())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let handle = app.handle().clone();
            tauri::async_runtime::spawn(async move {
                warm_start_services(handle).await;
            });
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![reveal_main_window])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

- Put app-wide initialization in `.setup(...)`, not scattered across commands.
- Avoid heavy blocking work directly inside `.setup(...)`.
- Use `AppHandle` for path resolution, restart and update access, and cross-window orchestration.
- Key runtime window logic by stable labels, not titles.

**Binary response**

```rust
use tauri::ipc::Response;

#[tauri::command]
fn read_image_file(path: std::path::PathBuf) -> Result<Response, AppError> {
    let data = std::fs::read(path).map_err(|e| AppError::Io(e.to_string()))?;
    Ok(Response::new(data))
}
```

- Use `tauri::ipc::Response` for file bytes, image bytes and download payloads.
- Keep JSON responses for structured metadata and small payloads.

**Raw request validation**

```rust
use tauri::ipc::{InvokeBody, Request};

#[tauri::command]
fn upload_binary(request: Request) -> Result<(), AppError> {
    let InvokeBody::Raw(bytes) = request.body() else {
        return Err(AppError::InvalidRequest("raw body required"));
    };

    let Some(_authorization) = request.headers().get("Authorization") else {
        return Err(AppError::InvalidRequest("missing Authorization header"));
    };

    if bytes.is_empty() {
        return Err(AppError::InvalidRequest("empty upload body"));
    }

    Ok(())
}
```

- Validate headers and body shape explicitly.
- Treat raw IPC handlers as privileged ingress points.

**Sidecar permission scope**

```json
{
  "$schema": "../gen/schemas/desktop-schema.json",
  "identifier": "default",
  "windows": ["main"],
  "permissions": [
    "core:default",
    {
      "identifier": "shell:allow-spawn",
      "allow": [
        {
          "name": "binaries/my-sidecar",
          "sidecar": true,
          "args": ["serve", { "validator": "\\d+" }]
        }
      ]
    }
  ]
}
```

```rust
let (_rx, _child) = app
    .shell()
    .sidecar("my-sidecar")
    .map_err(|e| AppError::Sidecar(e.to_string()))?
    .args(["serve", "7780"])
    .spawn()
    .map_err(|e| AppError::Sidecar(e.to_string()))?;
```

- Use `shell:allow-execute` for `execute()` and `shell:allow-spawn` for `spawn()`.
- Match the sidecar name exactly with the configured binary reference.
- Whitelist exact arguments or validators.
- Never grant broad shell authority because the app needs one safe sidecar.

**Window labels and capabilities**

```rust
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let webview_url = tauri::WebviewUrl::App("index.html".into());

            tauri::WebviewWindowBuilder::new(app, "first", webview_url.clone())
                .title("First")
                .build()?;

            tauri::WebviewWindowBuilder::new(app, "second", webview_url)
                .title("Second")
                .build()?;

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```json
{
  "identifier": "dialog",
  "windows": ["first", "second"],
  "permissions": ["dialog:allow-ask"]
}
```

- Labels must be unique and stable. Capabilities attach to labels, not window titles.
- Overlapping capabilities merge, so keep high-privilege windows isolated.
- Use the `platforms` field when a capability should exist only on certain operating systems.
- Expose window-creation ability only to windows you trust with privilege.

**Tray menu**

```rust
use tauri::{
    menu::{Menu, MenuItem},
    tray::TrayIconBuilder,
};

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let quit_item = MenuItem::with_id(app, "quit", "Quit", true, None::<&str>)?;
            let menu = Menu::with_items(app, &[&quit_item])?;

            let _tray = TrayIconBuilder::new()
                .menu(&menu)
                .menu_on_left_click(true)
                .build(app)?;

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

- Enable the `tray-icon` feature explicitly.
- Keep menu item IDs stable and machine-readable.
- Handle tray and menu events in one obvious place.

**Mocked frontend IPC test**

```typescript
import { afterEach, expect, test } from 'vitest';
import { clearMocks, mockIPC, mockWindows } from '@tauri-apps/api/mocks';
import { invoke } from '@tauri-apps/api/core';

afterEach(() => {
  clearMocks();
});

test('loads settings through IPC', async () => {
  mockWindows('main', 'settings');
  mockIPC((cmd) => {
    if (cmd === 'read_settings_file') {
      return '{"theme":"dark"}';
    }
  });

  const result = await invoke<string>('read_settings_file');
  expect(result).toContain('"theme":"dark"');
});
```

- Reliable Tauri code needs two test layers: mocked frontend IPC tests and runtime-backed Rust tests. End-to-end WebDriver tests help but are not the whole story.
- Call `clearMocks()` after each test.
- Use `mockIPC(...)` to validate command usage and simulate backend responses.
- Use `shouldMockEvents: true` when testing event-driven flows.
- Use `mockWindows(...)` for label-oriented frontend logic.
- Tauri's WebDriver-based desktop end-to-end support excludes macOS desktop clients.

**Build hooks** (`tauri.conf.json`)

```json
{
  "build": {
    "beforeDevCommand": "pnpm dev",
    "beforeBuildCommand": "pnpm build",
    "devUrl": "http://localhost:1420",
    "frontendDist": "../dist"
  }
}
```

- Wire `beforeDevCommand` and `beforeBuildCommand` to the real frontend scripts.
- Keep `devUrl` and `frontendDist` aligned with the actual frontend toolchain.
- Treat the config, not README prose, as the source of truth for the build seam.
- Commit lockfiles so frontend and Rust builds stay reproducible together.

**Platform config files**

```json
// src-tauri/tauri.conf.json
{
  "productName": "MyApp",
  "bundle": {
    "resources": ["./resources"]
  },
  "plugins": {
    "deep-link": {}
  }
}
```

```json
// src-tauri/tauri.windows.conf.json
{
  "productName": "MyApp Windows",
  "plugins": {
    "cli": {
      "description": "Windows CLI entrypoint"
    }
  }
}
```

- Use `tauri.windows.conf.json`, `tauri.macos.conf.json`, `tauri.linux.conf.json` and the mobile variants when platform behavior diverges.
- Tauri merges a platform config into the base config with JSON Merge Patch semantics.
- Prefer config-layer overrides for platform packaging, identifiers or plugin shape before adding runtime `cfg` branches.
- Use `--config` for flavors such as beta builds; do not clone entire config trees.

**External binaries**

```json
{
  "bundle": {
    "externalBin": [
      "binaries/my-sidecar"
    ]
  }
}
```

```rust
use tauri_plugin_shell::ShellExt;

let sidecar = app
    .shell()
    .sidecar("my-sidecar")
    .map_err(|e| AppError::Sidecar(e.to_string()))?;
```

- Relative `bundle.externalBin` entries resolve relative to `src-tauri/tauri.conf.json`.
- Each bundled binary needs the correct `-$TARGET_TRIPLE` suffix for the target architecture.
- `shell().sidecar(...)` expects the filename alias, not the full path from `externalBin`.
- Keep sidecar naming stable across config, capability files and runtime calls.

**Single-instance handoff**

```rust
use tauri::Manager;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    let mut builder = tauri::Builder::default();

    #[cfg(desktop)]
    {
        builder = builder.plugin(tauri_plugin_single_instance::init(|app, _args, _cwd| {
            if let Some(window) = app.get_webview_window("main") {
                let _ = window.unminimize();
                let _ = window.show();
                let _ = window.set_focus();
            }
        }));
    }

    builder
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

- Register the single-instance plugin first so other plugins cannot interfere.
- A second launch should focus or route to the existing main window.
- The plugin has no JavaScript API; drive it from Rust lifecycle code.

**Deep links with single instance**

```rust
use tauri_plugin_deep_link::DeepLinkExt;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    let mut builder = tauri::Builder::default();

    #[cfg(desktop)]
    {
        builder = builder.plugin(tauri_plugin_single_instance::init(|_app, argv, _cwd| {
            println!("new instance argv: {argv:?}");
        }));
    }

    builder
        .plugin(tauri_plugin_deep_link::init())
        .setup(|app| {
            #[cfg(any(windows, target_os = "linux"))]
            {
                app.deep_link().register_all()?;
            }

            if let Some(urls) = app.deep_link().get_current()? {
                println!("startup deep links: {urls:?}");
            }

            app.deep_link().on_open_url(|event| {
                println!("deep link URLs: {:?}", event.urls());
            });

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```json
{
  "plugins": {
    "deep-link": {
      "desktop": {
        "schemes": ["my-tauri-app"]
      }
    }
  }
}
```

- When combining with deep links, register single-instance first.
- On Linux and Windows, `register_all()` is useful in development and for AppImage-style environments.
- Validate the deep-link format even after scheme matching; users can pass fake-looking arguments manually.
- Runtime-registered schemes require manual argument inspection for safety.
- If the frontend listens for deep-link events, capabilities usually need `core:event:default` plus `deep-link:default`.

**CLI contract**

```json
{
  "plugins": {
    "cli": {
      "description": "My app CLI",
      "args": [
        {
          "short": "v",
          "name": "verbose",
          "description": "Verbosity level"
        }
      ],
      "subcommands": {
        "run": {
          "description": "Run the application",
          "args": [
            { "name": "debug", "description": "Run in debug mode" },
            { "name": "release", "description": "Run in release mode" }
          ]
        }
      }
    }
  }
}
```

```rust
use tauri_plugin_cli::CliExt;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_cli::init())
        .setup(|app| {
            if let Ok(matches) = app.cli().matches() {
                println!("{matches:?}");
            }
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

- Define root args and subcommands under `plugins.cli` and read them through the plugin API; do not invent ad hoc argument parsing.
- Use `app.cli().matches()` in Rust or `getMatches()` in JavaScript.
- Add the `cli:default` capability if the frontend needs the CLI matches.
- On Windows, production apps cannot reliably write text back to the calling console by default, so do not design critical flows around stdout output.

**Window-state restore**

```rust
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            #[cfg(desktop)]
            app.handle().plugin(tauri_plugin_window_state::Builder::default().build());

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```typescript
import { saveWindowState, StateFlags } from '@tauri-apps/plugin-window-state';

await saveWindowState(StateFlags.ALL);
```

- Initialize the window-state plugin on desktop targets.
- Add the `window-state:default` capability when using its guest APIs.
- To avoid a visual flash during restore, create the window with `visible: false` and let restoration show it.
- Use explicit save and restore when window persistence is part of workflow correctness, not just convenience.

**The five boundaries**

Tauri reliability mostly comes from getting these boundaries right: the Rust command boundary, the window capability boundary, the filesystem scope boundary, the sidecar process boundary and the persistence size boundary. Make each explicit, typed and least-privilege.

### Tauri TDD-first checks

- Write or update typed boundary tests before widening the command surface.
- Validate serializable error shapes before UI handling depends on them.
- Test lifecycle-sensitive behavior wherever tray, updater, single-instance or deep links are involved.
- Prefer mocked desktop-boundary tests when full runtime integration is heavier than necessary.

Before shipping any meaningful Tauri feature, verify:

- the capability file proves least privilege for every new permission
- the command returns structured success and structured failure
- the async command has no blocking call sites
- managed state has the right mutex type
- persisted payload size stays below explicit caps
- sidecar startup has a timeout and a health endpoint
- updater keys are not in git
- listeners are cleaned up on unmount
- command names are unique across modules
- sidecar permissions whitelist the binary and its args
- high-privilege windows do not accidentally inherit merged capabilities
- binary responses do not go through JSON when raw bytes are intended
- mocked frontend tests clear state between runs
- build hooks and frontend dist paths match the real toolchain
- platform-specific config overrides are intentional and minimal
- single-instance is registered first if the app uses it
- deep links are validated beyond scheme matching
- CLI access has the right plugin config and capability
- window-state restore avoids first-paint flash

### Tauri runtime and safety gates

- No blocking work runs directly in an async command context.
- No lock guard or mutable access pattern crosses `.await` unless the chosen async mutex model explicitly requires it.
- No `unwrap()` or `expect()` remains in user-reachable command or lifecycle paths.
- No secret or sensitive payload is logged.
- Updater, sidecar, filesystem and plugin boundaries stay least-privilege.
- Lifecycle ownership is verified for tray, deep links, single-instance handoff, sidecars and startup/setup work.

Alongside the Rust command gates, run the repo's frontend and Tauri checks for the changed boundary. Use the repo's actual package manager and scripts; for example:

```bash
pnpm test
pnpm build
pnpm tauri build
```

### Tauri release readiness checklist

- [ ] Requirements are executable and measurable.
- [ ] Each `REQ-TAURI-*` has at least one linked test.
- [ ] Command, IPC and UI-state behavior are covered at the right boundary.
- [ ] Capability, filesystem, plugin, sidecar and lifecycle choices are explicit.
- [ ] Rust quality gates pass.
- [ ] Repo-normal frontend or desktop checks pass for the changed surface.

### Tauri anti-patterns

Reject these by default:

- vague desktop requirements with no measurable assertions
- generic Rust rules overriding Tauri-specific capability or lifecycle safety guidance
- borrowed inputs on async command boundaries
- `unwrap()` or `expect()` in user-reachable command or lifecycle paths
- broad filesystem, plugin or sidecar permissions used as convenience defaults
- event spam for large payloads or streaming progress
- the plugin store used as a blob sink
- unchecked sidecar spawning with no lifecycle ownership
- updater, tray or deep-link behavior treated as post-hoc polish

- broad shell permissions used as a convenience default
- sidecar spawning without bounded startup, permission scoping or packaging declarations
- command surfaces that panic or return opaque, unserializable failures
- four-word naming applied where it would break stable command, API or window compatibility

- blocking inside an async command handler
- an unnecessary `Arc` around state Tauri already manages
- filesystem access wider than the actual paths and windows involved

Anti-patterns with their fixes:

```rust
// Blocking an async command. Fix: use async APIs or spawn_blocking.
async fn bad_command() -> String {
    std::thread::sleep(std::time::Duration::from_secs(5));
    "done".into()
}

// Borrowed async input. Fix: take String.
async fn bad_command(name: &str) -> String {
    format!("hello {name}")
}

// Panicking command path. Fix: return Result<T, AppError>.
fn read_file_now() -> String {
    std::fs::read_to_string("file.txt").unwrap()
}

// Double-wrapped managed state. Fix: manage(Mutex::new(...)).
use std::sync::{Arc, Mutex};
let state = Arc::new(Mutex::new(AppState::default()));
tauri::Builder::default().manage(state);
```

- `{ "permissions": ["fs:default"] }`. Fix: exact commands plus scoped directories.
- Plugin store as a blob sink: `settings.json` and a theme preference are fine; base64 screenshot history and multi-megabyte terminal scrollback are not. Fix: externalize large payloads.
- Unchecked sidecar spawning: spawn the process, then assume it is ready, its args are safe and its logs stay small. Fix: capabilities, health check, timeout and bounded logs.

## 16. Quality gates and commands

Required command gates:

```bash
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --all-targets --all-features
cargo build --all-targets --all-features
```

Optional advanced gates:

```bash
cargo test --release
cargo llvm-cov --workspace --branch --fail-under-lines 75
```

Run the optional advanced gates for high-risk changes.

### Traceability gate

- Every requirement has a stable id (`REQ-RUST-<NNN>.<REV>`) and is linked to one or more tests.
- Fail the review if any requirement lacks verification.

### Naming and structure gate

- New symbols use four-word names when feasible.
- Modules are single-purpose and understandable.
- Existing public API contracts are preserved when compatibility matters.

### Runtime and safety gate

- No blocking I/O or CPU-bound work runs directly on an async executor.
- No mutex guard, rwlock guard or mutable borrow is held across `.await`.
- Cancellation, timeout and shutdown paths are handled wherever async work can outlive its caller.
- No secret value is logged.

### Release readiness checklist

- [ ] Requirements are executable and measurable.
- [ ] Each `REQ-RUST-*` has at least one linked test.
- [ ] Tests validate functional, error and edge behavior.
- [ ] Performance claims include explicit thresholds and a test method.
- [ ] Documentation and examples reflect current behavior.
- [ ] No TODO, STUB or FIXME placeholders remain in finalized code.

Reject work that lacks requirement coverage, measurable performance evidence, or concurrency validation where it matters.

### Tooling, release and operations patterns

- **`cargo clippy -D warnings` as a correctness gate.** A meaningful subset of lints catches correctness bugs, needless allocation and API footguns. Optional warnings become background noise. Do not suppress large lint classes without understanding why they fire.
- **`rustfmt` as non-negotiable.** Consistent formatting removes review churn and keeps diffs and blame readable. Do not hand-tune style against the formatter.
- **MSRV policy and toolchain pinning.** Depending on "whatever latest stable has" makes compatibility accidental. State the MSRV, pin the toolchain, and document any MSRV change.
- **Supply-chain policy with `cargo audit`, `cargo deny` or `cargo vet`.** Advisories, license constraints and yanked crates affect whether code is safe to ship. `Cargo.lock` alone is not risk management.
- **Structured observability with `tracing`.** Spans, fields and correlation IDs make async and concurrent failures reconstructable. Never log secrets or dump whole payloads unfiltered.
- **Secret handling with `secrecy`.** Wrap API keys, tokens and passwords in types that resist accidental display. Do not pass secrets as plain `String` because the code is internal.
- **SQLx compile-time query checking and pool discipline.** Compile-time verified queries stop SQL strings and schemas drifting apart. Do not hold pooled connections across unnecessary `.await`s. Dynamic SQL generation loses the benefit.

- **Coverage as a gate with `cargo-llvm-cov`.** A coverage floor on critical modules guards against silent test regressions; branch coverage helps where line coverage gives false confidence. Do not chase 100 percent in place of meaningful test depth.
- **Workspace, toolchain and additive-feature discipline.** In multi-crate repos, keep workspace layering clear, the toolchain pinned and features additive, so a change does not introduce build drift. Workspace configuration must not be tribal knowledge.

MSRV in `Cargo.toml`; test on that toolchain, and do not depend on nightly-only features in libraries:

```toml
[package]
rust-version = "1.76"
```

License and advisory policy in `deny.toml`; run the advisory check as a scheduled job:

```toml

Commit `rustfmt.toml` so style is project-wide and diffs stay stable:

```toml
edition = "2024"
max_width = 100
group_imports = "StdExternalCrate"
```

CI gates: `cargo fmt --check`, `cargo clippy -D warnings`, doctests, `nextest`, coverage (`llvm-cov` or `grcov`), `cargo-deny` and a SemVer check.

SQLx migrations and offline mode: manage schema with the CLI, and prepare offline query data so hermetic CI builds need no database.

```sh
sqlx migrate add init
sqlx migrate run --database-url=${DATABASE_URL}
```

Pin the toolchain per project:

```toml
# rust-toolchain.toml
[toolchain]
channel = "1.80.1"
components = ["rustfmt", "clippy"]
```

Workspaces share one `Cargo.lock` and `target`; keep profiles at the root, and put aliases and offline mode in `.cargo/config.toml`:

```toml
# .cargo/config.toml
[alias]
c = "check --workspace"
[net]
offline = true
```

Coverage in CI: emit lcov or JSON, and exclude generated and build directories with `--ignore-filename-regex`.

```sh
cargo llvm-cov --all-features --workspace --branch --fail-under-lines 75
```

Fuzzing setup; seed RNGs for determinism in CI and minimize failing inputs:

```sh
cargo fuzz init && cargo fuzz add parse && cargo fuzz run parse
```
# deny.toml
[licenses]
allow = ["MIT", "Apache-2.0"]

[advisories]
db-path = "~/.cargo/advisory-db"
```

Instrument service boundaries and propagate span fields such as `trace_id` and `user_id`. No `println!`-style logging in libraries:

```rust
#[tracing::instrument(skip(req))]
pub async fn handle(req: Request) -> Result<Response, Error> {
    tracing::info!(method = %req.method(), path = %req.uri().path());
    // ...
    Ok(resp)
}
```

Keep secrets in `SecretString`/`SecretVec`, which have no `Display`/`Debug` output, and do not clone them widely:

```rust
use secrecy::{ExposeSecret, SecretString};
let api_key = SecretString::new(load_key());
// tracing::info!(key = %api_key); // anti-pattern
tracing::info!(has_key = api_key.expose_secret().len() > 0);
```

SQLx: use `query!`/`query_as!` with offline mode, and set timeouts and a connection maximum on the pool:

```rust
#[derive(sqlx::FromRow)]
struct User { id: i64, name: String }
let row = sqlx::query_as!(User, "SELECT id, name FROM users WHERE id = $1", id)
    .fetch_one(&pool).await?;
```

Run Clippy and coverage across all targets and features, not a subset. Exclude generated code from coverage.

## 17. Review checklist

Questions to answer in any review or before handoff:

- Which mode or combination of modes is active?
- What is the smallest set of `REQ-RUST-*` contracts that makes the work testable?
- Which types and invariants belong in L1 instead of leaking into adapters?
- Which failure modes deserve doctest, compile-fail, property, fuzz, `loom` or `Miri` coverage instead of unit tests alone?
- Which public names must stay stable even if a cleaner new alias exists?

- Does this API expose concrete containers unnecessarily?
- Are error variants actionable and contextualized?
- Are any locks or borrows held too long?
- Does async code block the runtime?
- Do tests prove every major claim in the implementation?

### Architecture sign-off checklist

Before finalizing a design, verify:

- **Executable specifications:** requirements are in WHEN/THEN/SHALL form; every acceptance criterion has an automated test; the design states preconditions, postconditions and error conditions; performance claims have measurable contracts.
- **Testability:** components are trait-based with mock implementations; dependency injection allows isolated testing; no hard dependency on external systems; interfaces between components are clear.
- **Layering:** L1 is isolated (no_std compatible where applicable); L2 follows std idioms; L3 dependencies are justified and minimal; there is a clear path from the simple version to the complex one.
- **Resources:** every resource-holding type implements `Drop`; no possible leaks; graceful shutdown under all conditions.
- **Performance:** claims and memory layout are validated by tests; critical paths have benchmarks; regression detection is in place.
- **Errors:** a structured hierarchy with `thiserror`; application context with `anyhow`; clear error boundaries; actionable messages.
- **Domain complexity:** data models handle real-world cases, not simplified examples.
- **Concurrency:** thread safety is validated by tests; stress tests run under concurrent load; no possible deadlocks or races.
- **Workflow:** requirements reference acceptance-criteria ids; each interface has a test plan; tasks follow STUB, RED, GREEN, REFACTOR; each feature has a one-command verification.

### Rules by phase

- **Requirements:** write executable acceptance criteria; assign ids for requirement-to-test mapping; replace "better", "faster", "easier" with measurable criteria.
- **Design:** start with traits; include test contracts; respect L1, L2, L3; design for real complexity.
- **Implementation:** write tests first; give every performance assertion a test; use RAII consistently; structure errors with context; stress-test concurrency.
- **Maintenance:** keep docs synchronized with code by automation; provide one command that validates a whole feature; run the full suite in CI.
