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

Reach for the simplest pattern that preserves correctness boundaries, not the most impressive one. Test: each pattern you applied should be removable only by weakening a named boundary. A newtype and a typed error that close a boundary in twenty lines beat a typestate protocol wrapped around a two-state flag. Start with the patterns that prevent the most bugs (newtypes for validated values, no blocking across `.await`) before advanced ones (HRTBs, GATs, `PhantomData` variance).

Powerful techniques that are not first bets, because they are niche or easy to misapply:

- allocator overrides as a general default
- `ManuallyDrop` for compile-time or micro-optimization purposes
- proc-macro internals beyond hygiene, spans and diagnostics
- lock-free building blocks without a verification plan
- pinning tricks beyond safe projection and clear containment
- specialization-related designs in public crates

Correctness is won or lost in public API commitments, error boundary design, async cancellation and concurrency semantics, executable verification, and operational behavior after the code ships.

Record the ladder choices on any change that touches a public API, an error surface, concurrency or unsafe: the classification, the four surface choices, the gates matched to each touched boundary, and every unsafe block with its safety argument (state explicitly when there is none). Put it in the PR or the crate docs. Note the condition that would invalidate a choice, for example "`dyn Trait` here because this is a plugin seam; revisit if it becomes a hot loop", so a later reader can tell a decision from an accident. The choices constrain each other in order (the newtype shapes the error variants, the error shape decides what the doctest asserts), so a typed error behind an API that takes `&String` fails the ladder even though each pattern passes on its own.

Size a change by the surfaces it crosses, not by its line or symbol count. A large rename that crosses none is cheap to review; a small diff that changes the API, the error type and the concurrency model at once is three changes. If a change crosses more than two of ownership, error, concurrency and API stability, split it, in that order: introduce the newtype first, then the error redesign it enables; do not convert an API to async and retype its errors in one PR. Any unsafe adds the safety argument and a Miri run regardless of diff size; where Miri cannot run (FFI-heavy code), use an equivalent check. Absence of crashes is not evidence that unsafe code is sound.

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

### Rule strength, waivers and severity

- **Rule strength.** MUST and MUST NOT are mandatory unless a waiver is recorded. SHOULD and SHOULD NOT are defaults that context can override. MAY is optional.
- **Waivers.** An exception to a MUST rule records: reason, narrowed scope, compensating control, verification plan, owner, and a review trigger or expiry.
- **Invalid waiver reasons:** deadline pressure alone; "MVP" with no compensating control; discomfort with tests; unfamiliarity with the Rust feature that would solve the problem; keeping a speculative abstraction alive.
- **Review severity:**
  - P0: correctness or safety failure likely to cause broken behavior, corruption, exploitability or an invalid completion claim.
  - P1: serious design or reliability weakness with high regression or operability risk.
  - P2: notable maintainability, verification or boundary weakness.
  - P3: polish or clarity issue with limited correctness risk.
- **Confidence in a rule:** high when backed by language guarantees, std behavior or broad production precedent; medium for strong but context-sensitive ecosystem precedent; low for a heuristic or local convention.

Waiver rules:

- A waiver names the exact rule waived, with minimal and concrete scope.
- The compensating control addresses the specific risk the rule prevented.
- Verification added by a waiver is stricter than the baseline for that area.
- A waiver expires at the next relevant refactor, release or architecture review.
- Waivers around unsafe, shutdown semantics or public API leakage name the owner and the review trigger.
- A waiver never turns hidden cleanup, hidden background ownership or a hidden dependency commitment into a "temporary" default without a replacement plan.
- Also invalid as reasons: "we know this is safe", "we will test later", "the compiler is annoying", "the framework makes this awkward".

### First principles

1. Make invalid states unrepresentable where practical.
2. Ownership is a design tool. Borrow before cloning.
3. Parse at boundaries; do not let unvalidated shapes travel inward.
4. Make failure modes explicit in types, control flow and tests.
5. Prefer a simple public surface to internal sophistication.
6. Async, cancellation and concurrency are correctness concerns.
7. An advanced pattern earns its place by removing misuse or ambiguity.
8. Safe and unsafe code meet through explicit contracts.
9. Destructor timing and cleanup are part of program semantics.

Enforcement order:

- Check an invariant statically with a type when that is cheap.
- Otherwise validate once at the narrowest trustworthy boundary, not repeatedly downstream.
- An `_unchecked` fast path may exist only beside a checked counterpart that defines the contract, and only where callers can realistically uphold it.
- Debug-only validation is for expensive internal consistency checks; it does not replace boundary validation.

Destructors and temporaries:

- Destructors are infallible, non-blocking and minimal in side effects.
- If teardown must fail, block or await, expose an explicit `shutdown`, `flush` or `close` method.
- Keep temporaries and guards short-lived so drop timing is predictable.
- If correctness depends on teardown happening before later work, show that in control flow and test it.
- If a task can outlive its caller, describe its cancellation and shutdown behavior.

What the compiler does not prove:

- It proves memory and type properties. It does not prove domain correctness, performance, cancellation behavior or SemVer compatibility.
- No borrow-checker error does not mean the clones are justified.
- No data race does not mean no logical race, starvation, dropped work or stale state.
- Unsafe code must stay sound even if the surrounding safe code is logically wrong. Each unsafe block maps to one narrow proof obligation that can be explained locally. Delete an unsafe optimization that does not buy measurable gain.

Working terms:

- **Boundary:** a place where unchecked data, control or side effects enter or leave a component.
- **Soundness:** safe Rust cannot trigger undefined behavior.
- **Minimal exception safety:** code stays memory-safe if unwinding happens at an awkward moment. **Maximal exception safety:** the program also stays semantically correct.
- **Cancel-safe:** safe under interruption, with no silent corruption or lost invariant. **Cancellation point:** a place where a future may be dropped, typically an `.await`.
- **Backpressure:** the explicit policy limiting producer pressure against slower consumers.
- **Opaque error:** an error meant for propagation and display, not detailed matching.
- **Generated surface:** code produced from a schema or tool whose source of truth lives elsewhere.

### Doctrine for core and standard-library code

- **Lifetimes.** Annotations express real relationships between inputs and outputs. If lifetime reasoning gets harder than the logic, rethink the API shape instead of adding annotations. Prefer scoped borrows to long-lived shared mutable access.
- **Parse, don't validate.** Parse once at the edge and pass only validated domain types inward. Re-validation deep in business logic is boundary leakage unless it guards a separate trust boundary.
- **Constructors.** Invariant-preserving constructors are the default way into a domain type; public field mutation is a last resort. If validation must be dynamic, do it immediately and return a typed error, never half-validated state. An `_unchecked` constructor documents its preconditions precisely and sits beside the checked one.
- **Error surface.** Do not leak a dependency's error type through a stable public API unless that SemVer commitment is deliberate. If callers mostly propagate and display an error and rarely inspect it, an opaque error with good context beats a large public enum. State the recovery strategy wherever it changes what the caller should do.
- **Shared state.** `Rc`, `Arc`, `Cell`, `RefCell`, `Mutex`, `RwLock`, atomics and channels are different tools. Narrow shared state to the smallest mutable surface. `Arc<Mutex<T>>` must not become the default architecture for unrelated concerns.
- **Loops.** A manual loop is fine when it is clearer, more controllable or easier to debug than a combinator chain.

### Doctrine for ecosystem and boundary code

- **Conversion names follow cost.** `as_` for a cheap borrowed view, `to_` for a transform that may allocate or copy, `into_` for owned consumption.
- **Generated code** is an implementation artifact. Do not hand-edit it; own the semantic contract in a hand-written wrapper or extension module. A type with deterministic cleanup makes its post-close behavior obvious.
- **Boundary types.** Transport shapes stay transport shapes; domain invariants live in domain types, not raw DTOs. Send binary payloads over a binary-friendly transport, not as large JSON blobs. Inspect opaque or untrusted payloads before converting them to richer internal forms.
- **Persistence and integrations.** Each persistence workflow has one clear transaction owner. When durable state and a remote side effect are combined, state the failure strategy. An external client boundary exposes typed failures, a timeout policy, a retry policy and correlation context. Design idempotency and deduplication wherever callers or infrastructure can replay a request.
- **Measure before optimizing.** Start from a profile or a demonstrated hot path. Compile time, binary size, memory and latency are different targets: name the one being optimized. Benchmarks use representative inputs and stable thresholds. An algorithmic guarantee can outrank a micro-optimization when worst-case behavior matters.
- **Adopting a pattern.** Adopt one only when it reduces a bug class, misuse or ambiguous failure behavior, never because it looks advanced. High-ceremony patterns must pay for themselves in safety, boundary clarity or correctness. Judge a pattern on: zero-cost, type-safe, ergonomic, compositional, resilient.
- **Recovery-aware errors.** Where retryability changes control flow (network clients, storage, subprocesses, queues, external APIs), encode it in the error type as transient or permanent. Classify by recovery strategy, not by cause. Never match on error strings. Test that transient errors retry and permanent errors do not.

### Rule cards

- **Newtypes at trust boundaries (must).** Identifiers, units, tokens, credentials, offsets and validated values get dedicated types once they cross a trust boundary, for example `struct UserId(NonZeroU64);` and `TryFrom<&str> for EmailAddress`. If two values should not be swappable, their types should not be swappable. Not needed for one-shot local glue. Verify with parse and round-trip tests.
- **One conversion path.** Convert between transport, domain and storage forms through `From`, `TryFrom` or a dedicated constructor, for example `TryFrom<CreateUserRequest> for NewUser`. Never hand-validate the same fields in several handlers. Verify with conversion tests and malformed-input cases.
- **Static before dynamic validation (must).** Prefer argument types that rule out invalid input; when that is not enough, validate immediately at the entry point. The best validation is the one callers cannot accidentally forget. Review every unchecked escape hatch.
- **Trait seams at side-effect boundaries.** Put a trait where ownership of side effects changes: outbound HTTP, storage, queues, clock, UUID generation, sidecar processes. The core service depends on a `UserStore` trait and the adapter owns the SQLx pool; handlers never build clients or queries inline. Skip the trait for small leaf logic and stable internal helpers. Verify with unit tests against fakes plus integration tests against the real adapter.

- **Typestate for must-complete protocols (may).** Use for handshakes, builders with mandatory fields, resource lifecycles and staged activation, for example `Connection<Unauthenticated>` to `Connection<Authenticated>`. Do not use for ordinary CRUD or soft workflows where the state-machine cost exceeds the risk. Verify with compile-fail misuse tests plus transition tests.
- **Typed library errors (must).** The error type is part of the API. Never export `anyhow::Error` as a library's default contract. Add context where the operation or repair action becomes clear: file I/O, database calls, subprocesses, HTTP requests, task joins, for example `read_to_string(path).with_context(|| format!("read config: {path}"))?`. Never propagate a bare `NotFound` or `Io`.
- **Collection by access pattern.** `BTreeMap` for stable ordered iteration, `HashMap` for fast keyed lookup, `Vec` for compact ordered scans. Using `HashMap` everywhere and then re-sorting or cloning into the shape the caller needed is the anti-pattern.

- **Dependency types in public APIs (must).** Each exposed dependency type is a deliberate compatibility commitment. Otherwise wrap it in a local `Error`, `Request` or `Config` type and convert internally. Verify with a SemVer-oriented API review before release.
- **Explicit close (must).** A type whose teardown can fail, block or needs ordering exposes `close`, `flush` or `shutdown` returning `Result`; `Drop` only releases local state. No I/O, task waiting or panics in a destructor. Test the close path, double-close behavior and shutdown ordering.
- **Owned async boundaries (must).** Anything retained across `.await` or handed to a spawned task is owned. Move the request or domain state into the workflow; do not hold borrowed request fragments across awaits. Test cancellation and partial progress.
- **No blocking, no locks across await (must).** No `std::thread::sleep`, sync file I/O or `MutexGuard` held into a `select!` or network await. One passing run proves nothing about fairness or contention: use stress, timeout or latency tests, and `loom` when race behavior matters.
- **Bounded concurrency and explicit cancellation (must).** Worker pools, pipelines, retries and supervisors state their concurrency bound, backpressure and cancellation behavior. Throughput without defined overload and shutdown behavior is not reliability.

- **Shutdown fan-out (must).** A multi-task system has a single shutdown trigger, explicit fan-out to every owned task (a cancellation token or shutdown channel cloned into workers), and a bounded join phase with timeout or escalation. A main task that exits and hopes spawned tasks disappear is the anti-pattern. Test shutdown, signal handling, cancel-during-work and teardown time.
- **Structured task ownership.** A `JoinSet` or supervisor owns spawned tasks, so lifecycle and failure propagation are visible in control flow. If no one owns a task, no one owns its failure. If work can accumulate, the system already has a queue, so bound it. Detached work is acceptable only for telemetry-like tasks with bounded, acceptable loss.
- **Structured observability.** At request handlers, jobs, external calls, supervisors and queue consumers, emit `tracing` spans with request IDs, resource IDs, attempt counts and outcome fields. No free-form string logs with unstable wording. Skip tight inner loops when a higher boundary already gives the context.
- **Transport to domain at the edge (must).** Request DTO, then `TryFrom`, then domain command, then workflow, then persistence. Shape validation is not invariant validation. Handlers, services and database calls must not share raw strings and optional fields.

- **Unsafe islands (must).** Isolate unsafe code in the smallest private module or helper that can uphold a stable safe interface, with a `SAFETY` comment on each block. Never use unsafe for convenience around the borrow checker. Verify with invariant-focused tests, Miri or sanitizers, and a module-level safety review.
- **Measure first.** Profile, isolate the hotspot, benchmark representative workloads, optimize, re-measure. Do not add unsafe, caches, clone avoidance or lock-free structures because they "should be faster". An optimization that cannot name its metric is not justified.

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

### Mode precedence and defaults

Default mode combinations:

- vague feature request: Spec + Delivery
- public API or reusable crate: Spec + Architecture + Reliability
- async or concurrent system: Delivery + Reliability
- parser, decoder or protocol: Spec + Reliability
- code review: Review + Architecture or Reliability

When modes disagree, apply them in this order:

1. Spec decides what must be proven.
2. Architecture decides where invariants and dependencies belong.
3. Reliability decides which failure behavior must be explicit.
4. Delivery decides sequencing.
5. Review decides what to challenge hardest.

Prefer the choice that preserves correctness and compatibility with the least surprise to callers.

Output rules:

- Every non-trivial behavior claim maps to a requirement or rule, and every non-trivial requirement to at least one verification path.
- Review output leads with findings, not reassurance.
- Completion claims include fresh verification evidence. Evidence outranks confidence, earlier runs and plausibility.
- When a section is empty, say why. Do not fill it with placeholders.

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

### Embedded workflow

- **Target and linking.** Add the target (`rustup target add thumbv7em-none-eabihf` for Cortex-M4F/M7F), set it in `.cargo/config.toml`, and provide a `memory.x` defining FLASH, RAM, stack and vector table. Do not hardcode addresses in code; use `#[link_section]` sparingly.

```toml

### Architectural pattern cards

- **Sync core, async shell.** Async handlers, workers and adapters outside; synchronous domain and policy logic inside. Parse and fetch outside, decide and transform inside, then persist or emit outside. Unit-test the core; integration-test the shell. Skip the split for a tiny, purely async library.
- **Transport, domain, persistence separation.** Transport DTOs, then domain commands and values, then persistence rows and queries. Convert at the edge, enforce invariants in domain types, isolate storage specifics in adapters. Costs more conversion code; buys stronger invariants and clearer failure location.
- **Workspace layering by change boundary.** Core domain crates, adapter crates, binary or command crates, optional proc-macro or tooling crates. Split by stable responsibility and dependency direction, not by file count or chronology. Check the workspace graph and dependency direction.
- **Stable external API over composed internals.** Callers depend on a narrow contract while internal modules compose interchangeable engines or strategies chosen by the implementation. Fits parser engines, search and index systems, storage adapters, planners and performance-critical libraries. Buys optimization freedom and lower SemVer pressure.

- **Tauri split.** Frontend UI, then a typed IPC contract, then Rust core and workflows, then the capability and sidecar boundary. Use typed command modules, managed state, explicit permissions and explicit sidecar ownership. Verify with command tests, a permission review, sidecar lifecycle tests and startup and restore checks.

### Domain context packs

- **CLI and batch tools.** Path: `clap`, `tracing`, `ExitCode` for process semantics, typed config parsed at startup, `anyhow` at `main` and `thiserror` in the reusable core. Risks: ambiguous exit behavior, config parsing drift, poor diagnostics, blocking or unbounded memory on large input. Verify: command golden tests, config parse failures, exit-code tests, large-input behavior.
- **Backend services.** Path: DTO to domain conversion at the edge, typed state and services, explicit timeout and retry policy, `tracing`, pooled database access (`axum`, `tokio`, `tower`, `sqlx`). Stretch: idempotency keys, durable intent plus background processing, compile-time query checks, overload control. Risks: DTO leakage inward, hidden retries, timeout ambiguity, auth leakage, transactions coupled to remote side effects. Verify: handler integration tests, malformed input, timeout and retry behavior, transaction boundaries.
- **Libraries and SDKs.** Path: curated facade, typed errors, minimal dependency leakage, doctests for caller stories, additive features. Stretch: SemVer-aware layering, feature-matrix verification, optional zero-copy or `no_std` surfaces. Tools: `thiserror`, `proptest`, `criterion`, `cargo-semver-checks`. Risks: public dependency exposure, kitchen-sink errors, re-export sprawl, undocumented feature interactions.
- **Parsers and protocols.** Path: explicit frontier types, corpus tests, malformed-input handling, binary-safe diagnostics, round-trip property tests. Stretch: zero-copy where justified, fuzzing, typestate-assisted protocol handling. Tools: `nom` or a hand-written parser, `proptest`, `arbitrary`, `cargo-fuzz`. Risks: partial parse treated as success, UTF-8 assumptions, panic on bad input, protocol state corruption.
- **Tauri desktop.** Path: owned async commands, explicit managed state, narrow capabilities, exact sidecar scoping, typed IPC contracts. Risks: broad permissions, borrowed async inputs, hidden sidecar lifecycle, large payloads in JSON IPC, overlapping high-privilege windows. Verify: command tests, capability review, startup timeout, sidecar health checks, restore and first-paint behavior, deep-link handoff.
- **FFI and unsafe.** Path: smallest safe wrapper, explicit ownership and nullability, layout discipline, private unsafe core. Tools: `libc`, `bindgen`, `cxx`, Miri. Risks: layout mismatch, aliasing violations, panic crossing FFI, invalid lifetimes. Verify: harness tests, ABI shape review, ownership-transfer tests, Miri or sanitizers.
- **Performance work.** Path: representative benchmark cases, profile first, algorithmic wins and boundary simplification before unsafe or lock-free code. Stretch: worst-case complexity guards, cache-aware layout, allocation budgets. Tools: `criterion`, `iai-callgrind`, `cargo-bloat`, flamegraphs. Risks: optimizing the wrong metric, overfitting microbenchmarks, freezing internals into the public API.
- **When Rust is the wrong tool.** Ultra-short scripts; deadline prototypes that do not need a typed service; one-off binaries with no reusable contract; integration surfaces so dynamic that safe boundary modeling is out of proportion; cases where the dominant latency is outside the process.
# .cargo/config.toml
[build]
target = "thumbv7em-none-eabihf"
```

```ld
/* memory.x */
MEMORY { FLASH : ORIGIN = 0x08000000, LENGTH = 512K; RAM : ORIGIN = 0x20000000, LENGTH = 128K }
PROVIDE(_stack_start = ORIGIN(RAM) + LENGTH(RAM));
```

- **Structure.** Use `embedded-hal` traits and a platform HAL so code is not tied to one MCU; structure with RTIC or Embassy. Never block inside an async task; use the Embassy time driver, not busy-wait delays. A global allocator is needed only when using `alloc`.
- **Logging.** `defmt` over RTT with `panic-probe`. No semihosting in production, no blocking prints in interrupts, no verbose logs on time-critical paths.

```rust
// Cargo.toml (bins)
// defmt = "*", rtt-target = "*", panic-probe = { version = "*", features = ["print-defmt"] }
#[defmt::panic_handler]
fn panic() -> ! { panic_probe::hard_fault() }
#[defmt::timestamp]
fn ts() -> u64 { 0 }
```

- **Flash and run** with `probe-rs`, selecting the chip explicitly:

```sh
cargo flash --chip STM32F401RETx --release --example blinky
probe-rs run --chip STM32F401RETx target/thumbv7em-none-eabihf/release/app
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

### Verification rules by risk

- **Bug-fix rule.** Reproduce the bug, write or strengthen a regression test, see it fail on the broken state, apply the fix, then see the regression test and the broader suite pass. Do not claim a regression test exists if it was never observed failing.
- **Checkpoints for long sessions.** Record the current red, green or refactor state, the exact failing tests or pending gates, the files touched, and open design or verification questions. A checkpoint guards against context drift; it does not replace tests.
- **Differential and adversarial tests.** Use malformed corpora and adversarial inputs at parser, codec and protocol edges, not only golden happy paths. Use differential tests when an old and a new implementation can check each other cheaply. Test generated-code wrappers at the wrapper seam.
- **Benchmarks need thresholds.** Track a named metric: latency, throughput, memory, binary size or compile time. Use realistic input sizes and worst-case pressure. A benchmark without an acceptance threshold does not show that a performance contract is met.
- **Tests by risk surface:**

| Risk surface | Preferred tests |
| --- | --- |
| pure logic | unit + property |
| public API contract | unit + doctest + misuse cases |
| persistence or I/O | integration |
| async orchestration | integration + timeout + cancellation |
| concurrency | stress, and `loom` where justified |
| parsing or protocol | corpus + malformed input + property + fuzz |
| compile-time misuse | compile-fail UI tests |
| performance claim | benchmark with threshold |
| unsafe or FFI boundary | harness + Miri or sanitizer |

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

- **Refutable and irrefutable patterns.** `match` for exhaustive handling, `if let` for one case, `while let` for loops that run until the pattern fails, irrefutable patterns in `let`. Do not use `if let` where several cases need handling.

```rust
// if let: handle one case
if let Some(x) = maybe { use_x(x); }

// while let: drain until pattern fails
while let Some(item) = iter.next() { process(item); }

// match: exhaustive handling
match res {
    Ok(v) => use_v(v),
    Err(e) => handle(e),
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

- **Zero-sized markers.** Field-less marker types with `PhantomData` encode modes and states at no runtime cost. Do not depend on the layout of structs containing ZSTs beyond what is guaranteed.

```rust
use core::marker::PhantomData;
struct ReadOnly;
struct Buffer<T, Mode> { data: Vec<T>, _mode: PhantomData<Mode> }
let _buf: Buffer<u8, ReadOnly> = Buffer { data: vec![], _mode: PhantomData };
```

- **Uninhabited types.** `!` is the canonical one; an empty enum models an impossible case in a generic, such as `Result<T, Void>`. Never expose an uninhabited type over FFI.

```rust
enum Void {}
fn into_ok<T>(r: Result<T, Void>) -> T { match r { Ok(v) => v, Err(e) => match e {} } }
```

- **`_` and `..` in patterns.** `_` ignores one field and `..` the rest. Use `..` when destructuring types that may gain fields, and always with `#[non_exhaustive]` types.

```rust
struct S { a: u32, b: u32, c: u32 }
let s = S { a: 1, b: 2, c: 3 };
let S { a, .. } = s; // ignore b, c
let S { b: _, c, .. } = s; // ignore b explicitly, bind c
```

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

### Error and recovery taxonomy

| Error class | Typical boundary | Recovery | Representation | Required tests |
| --- | --- | --- | --- | --- |
| validation | parse or input edge | reject with explicit reason | typed parse or domain validation error | malformed input cases |
| business rule | domain workflow | reject with precise outcome | named domain error or outcome enum | behavior tests |
| transient external | network, storage, subprocess, queue | retry, degrade or reschedule | retryable metadata or dedicated variant | retry behavior |
| permanent external | auth, contract or schema mismatch | fail fast, escalate or surface a repair action | typed permanent error | non-retry behavior |
| internal invariant breach | core domain | impossible by construction, or fail fast | impossible state or tightly scoped panic | invariant tests |
| timeout | async orchestration | fail, retry or cancel explicitly | timeout-aware typed error | timeout tests |
| cancellation | task or workflow boundary | cooperative stop with clear ownership | explicit cancel-aware path | cancel tests |
| backpressure or overload | queue, worker pool, stream | reject, shed, buffer or bounded wait | explicit saturation result | overload tests |
| FFI or unsafe boundary | ABI or memory ownership boundary | convert, abort or isolate | safe wrapper error contract | harness and invariant tests |
| cleanup or teardown | close or shutdown boundary | explicit close, best-effort drop, or escalate | typed close error or shutdown result | close-path and teardown tests |
| dependency leakage | public library surface | wrap, translate or deliberately re-export | local facade type | SemVer and downstream compile review |

- An error message answers what failed, where, and what the caller or operator should do next.
- If the caller must branch on an error, expose stable structured information. If the caller mostly propagates it, prefer an opaque error with context.
- Binary or non-UTF-8 input boundaries stay diagnosable without assuming text.
- Box or layer large cold-path error payloads so they do not bloat hot-path `Result` values.

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

- **Channel choice for threads.** `std::sync::mpsc` is the simple MPSC baseline; `crossbeam-channel` adds MPMC, `select!` and speed; `flume` adds async support, deadlines, rendezvous and a `Selector`. Do not block on sends without a timeout or mix channel ecosystems without need.

```rust
// flume rendezvous + select-like API
let (tx1, rx1) = flume::bounded::<u32>(0); // rendezvous
let (tx2, rx2) = flume::bounded::<u32>(1024);
flume::Selector::new()
    .recv(&rx1, |v| println!("r1: {}", v))
    .recv(&rx2, |v| println!("r2: {}", v))
    .wait();
```

- **Work stealing.** With `crossbeam-deque`, use a global `Injector` plus a LIFO `Worker` per thread; idle threads steal in batches. Avoid a single global queue and heavy locking around queues.

```rust
use crossbeam_deque::{Injector, Worker, Stealer, Steal};
let injector = Injector::new();
let workers: Vec<_> = (0..num_cpus::get()).map(|_| Worker::new_lifo()).collect();
let stealers: Vec<Stealer<_>> = workers.iter().map(|w| w.stealer()).collect();
// spawn workers: pop local, else steal batch from injector or others
```

- **Epoch reclamation.** Pin the epoch before touching shared pointers and retire removed nodes with deferred destruction. Never free without retiring, access a pointer outside a pin, or mix collector domains.

```rust
use crossbeam_epoch as epoch;
let guard = epoch::pin();
let shared: epoch::Atomic<usize> = epoch::Atomic::null();
let ptr = shared.load(epoch::Acquire, &guard);
// ... remove node ...
unsafe { guard.defer_destroy(ptr) };
```

- **A complete `loom` test.** Join the threads and assert the invariant. No randomness, timers or I/O inside the model, and cap the state space.

```rust
loom::model(|| {
    use loom::{sync::{Arc, atomic::{AtomicUsize, Ordering::*}}, thread};
    let n = Arc::new(AtomicUsize::new(0));
    let a = n.clone(); let b = n.clone();
    let t1 = thread::spawn(move || { let cur = a.load(Acquire); a.store(cur+1, Release); });
    let t2 = thread::spawn(move || { let cur = b.load(Acquire); b.store(cur+1, Release); });
    t1.join().unwrap(); t2.join().unwrap();
    assert_eq!(n.load(Relaxed), 2);
});
```

### Cancellation, backpressure and primitive choice

Primitive choice:

| Concern | Primitive | Use when | Avoid when |
| --- | --- | --- | --- |
| producer to workers | bounded `mpsc` | buffering must be explicit and backpressure matters | consumers need replay or state snapshots |
| latest state | `watch` | only the latest value matters | every event or history matters |
| every subscriber gets events | `broadcast` | bounded fan-out is needed | slow consumers or message loss cannot be tolerated |
| shared mutable state | `Mutex` or `RwLock` | shared mutation is simpler than message passing | ownership can be localized |
| one-time global state | `OnceLock` or `LazyLock` | initialization is one-shot | reset or a mutable lifecycle is required |
| task orchestration | `JoinSet` or a task scope | the parent owns task lifecycle | never use it to excuse detached long-lived work |
| concurrency limit | `Semaphore` | parallel work count must be bounded | work is sequential or bounded elsewhere |

Cancellation:

- Cancellation normally happens by dropping a future. Assume any `.await` may be the cut line.
- State for each long-running operation whether it is cancel-safe, restartable, resumable or lossy under cancellation.
- A branch that loses a `select!` race is dropped. Design branch-local state and cleanup for drop-as-cancellation, and watch for partially consumed state.
- If partial progress matters, persist intent or structure the workflow so an interruption cannot corrupt state silently.
- Prefer cancellation tokens or shutdown channels to boolean flags once several tasks or ownership domains are involved.

Backpressure:

- If producers can outpace consumers, define the saturation policy: reject, wait, shed, batch or durable offload. "The queue should stay small" is not a policy.
- No concurrency claim without reasoning, stress evidence or model checking in proportion to the risk.
- Prefer message passing when it settles correctness questions better than shared mutation.

Shutdown and cleanup:

- **No async destructors.** Rust has none, so a design that needs awaited cleanup exposes an explicit async cleanup method. Do not rely on cancellation alone for soundness or business invariants. Cleanup required for protocol correctness belongs in the API contract and the test plan.
- **Shutdown contract.** Define who initiates shutdown, how the signal fans out and how completion is awaited. Make shutdown idempotent or document repeated-call behavior. If teardown can block on I/O or task completion, that path is explicit in control flow and tested.
- **Snapshots over contention.** Prefer immutable snapshots or owned work packets when lock contention would otherwise dominate the reasoning.
- **Concurrency evidence.** A single green CI run proves almost nothing about concurrency. High-risk interleavings get `loom` or equivalent model checking; lower-risk code still gets stress, timeout, teardown and cancellation tests.

- **Retry only where state ownership is clean.** A retry loop around a future that is not cancel-safe re-enters half-consumed state on every attempt. Give retries a budget. Shutdown is where bounded channels, cancellation tokens and cancel-safe `select!` branches either compose or fail together, so test it: inject cancellation under load and assert no message is lost or processed twice. A bounded channel's fullness is a measurable saturation signal; an unbounded channel grows silently until memory pressure is the symptom. An unbounded channel on a provably low-volume control path is tolerable if the reason is written down.

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

- **Wide pointers.** `&[T]`, `&str` and `&dyn Trait` are pointer plus length or vtable. Never pass them across FFI (`extern "C" fn foo(s: &str)` is wrong); pass `(ptr, len)` in a `repr(C)` struct.

```rust
#[repr(C)]
pub struct SliceU8 { ptr: *const u8, len: usize }
#[no_mangle]
pub extern "C" fn take_bytes(s: SliceU8) { /* safe FFI shape for &[u8] */ }
```

- **Manual `Send`/`Sync`.** Write `unsafe impl` only when the thread-safety invariant is proven: no non-thread-safe interior mutability, raw pointers guarded by atomics or locks, no leaked lifetimes. Prefer composing `Send`/`Sync` fields. State the justification in docs.

```rust
unsafe impl<T: Send> Send for MyType<T> {}
unsafe impl<T: Sync> Sync for MyType<T> {}
// Justify invariants in docs: why concurrent access is safe.
```
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

- **Verify a performance change on two axes.** The benchmark delta, and a check that no checked operation became unchecked and no precomputed value outlives the freshness of its input. Do not replace `.get()` with indexing in a loop because the benchmark improved. "We already proved this above" stops being true when the code moves, so when a check is removed, state the invariant at the place the check was. Prefer speedups that add named structure (a precomputed view as its own type) over speedups that remove checks. Use saturating arithmetic only where saturation is the documented meaning, not to hide an overflow.

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

### Anti-pattern cards

Each card gives the smell and the preferred alternative.

- **Borrowing by habit.** Complex lifetimes or hidden clones added only to avoid taking ownership where the workflow clearly retains the data. Take owned inputs where storage or async lifetimes require it.
- **Stringly recovery logic.** Retry, fallback or escalation branches keyed on substrings of an error message. Message drift and wrapper layers break them silently. Use typed variants or retryability metadata.
- **Kitchen-sink public error enum.** One giant enum with a variant per crate, subsystem and transport failure plus catch-all strings. Callers cannot tell what is actionable and every internal refactor becomes an API change. Use typed local errors at meaningful boundaries and translate dependency failures into local concepts.

- **Accidental public dependency leakage.** Public functions, structs or error variants that name third-party types by convenience, so a dependency upgrade becomes a breaking change. Use local facade types and conversion layers. Exception: a crate whose purpose is to re-export the upstream contract.
- **Trait and module sprawl.** Many tiny traits, wrappers or modules that exist only to look abstract. Add seams only at real external or semantic boundaries.
- **Imperative accumulator soup.** Nested loops with repeated `push`, temporary flags and branch-specific accumulation. Use an iterator pipeline or small named helpers, unless the loop is control-heavy and a chain would be less clear.
- **Mutable config blob at runtime.** Partially filled config structs patched by many call sites before use, so validity depends on timing. Validate once in a builder and hand out a frozen config.
- **Implicit workspace and feature coupling.** The repo builds only because developers remember undocumented features, toolchains or root-only commands. Make workspace config explicit, pin conventions, keep features additive and run gates from the root. Verify with a root workspace build and a feature-matrix check.
- **Fire-and-forget task architecture.** Spawned tasks with no join path, shutdown path or failure observation, which leads to leaks, partial shutdown, hidden panics and stale state. Use a `JoinSet` or supervisor, bounded channels and cancellation tokens.
- **Transport types leaking inward.** Handlers, services and persistence share the same DTO struct, so every layer re-decides what is valid. Convert DTOs to domain commands at the edge.
- **Broad desktop privilege and unchecked sidecars.** Wide filesystem grants, generic shell authority, or sidecars with no health check or owner. Use granular capabilities, exact sidecar scoping, startup bounds and a supervised lifecycle. No exception for software running on a user's machine.

- **Speculative unsafe or lock-free code.** Unsafe blocks or lock-free structures added for an anticipated speed-up, with no measurement. Build the safe baseline first, then narrow unsafe only after measurement and a proof plan.
- **Compiler acceptance as proof.** "The borrow checker would have complained" used to justify logical behavior. Pair compile-time guarantees with behavior tests, boundary review and claim-specific evidence such as benchmarks or shutdown tests.
- **Hand-edited generated source.** Direct edits in `generated/`, `prost` or other codegen output. Regeneration discards them. Edit the schema, the generator configuration or a thin wrapper module, and check that regeneration is reproducible.

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

Handoff notes: the migration and rollout review is triggered by a change in schema or rollout behavior, not by whether a migration file was touched; a code-only change that alters rollout behavior still needs it. Passing format, lint, tests and build does not evidence a "faster" or "safer" claim; each such claim needs its measurement. Keep the Open Questions section even when it is empty. For a two-line fix the traceability table may be skipped if the requirement-to-test link is kept in the commit message.

When a gate fails, return to the workflow step that gate checks instead of redoing everything: an unmeasured claim sends you back to the requirements, a coverage hole to the verification mix. After a second failure at the same step, ask a human. Do not recover throughput by relaxing gates. Follow a sampled traceability row to its test now and then; a test id that names no real test is a hollow row.

### Backend delivery rules

- Keep domain validation out of transport-only types. Transport validation is not the whole validation story; keep domain invariants explicit.
- Keep secrets redacted and configuration layered by environment.
- Treat tracing, request correlation, health checks and failure classification as design concerns, not polish.
- Treat idempotency, retries and transaction scope as correctness problems whenever external systems are involved.
- Do not handle work synchronously in the request when it needs durable retries, deduplication or long-running external calls, unless the tradeoff is stated.
- Do not design password or session flows without addressing storage, failure behavior and async-safe verification boundaries.
- Do not treat deployment and migrations as postscript tasks when schema or background workflow behavior changes.

- **Layers give every failure an owner.** Parsing failures belong to transport, orchestration and error mapping to handlers, invariants to domain types, transactions to persistence, remote-system risk to typed clients. Walk a request end to end and name the owning layer for each step; a step with no owner is a boundary the design still owes. The layer boundaries are the rule; the crates are replaceable.
- **Decide inline or worker before coding a long-running path.** A slow remote call kept inline holds client connections open and turns client retries into duplicate side effects. Keep a slow call inline only with a stated tradeoff. Do not add a queue without a durability reason.
- **Adoption order when refactoring:** layer separation, edge validation, transaction ownership, typed clients, then the worker split. Draw layer boundaries before touching handler bodies; do not tune connection pools while unchecked strings still travel through the core. Review a diff in the same order, transport first.

- **Reject on sight in a backend review:** business rules in extractor glue; clients constructed inside handlers or per request; unchecked strings crossing the core; a multi-write workflow with no named transaction owner; inline work that needed durable retries; secrets in logs. Detection: grep handlers for client construction and SQL, check logs for secret material, check mutations for idempotency keys. Prioritize edge validation and transaction ownership, whose failures corrupt data.
- **Durable intent and remote side effects.** Saving intent and calling a remote system in one sequential block looks correct and fails only when the remote call succeeds and the commit does not, or the reverse. Name the transaction owner and define the recovery for each half-completed state.
- **Backend gate stack.** Format, lint, tests and build on every change. Add by concern: spawned-app integration tests for endpoints (app on a random port, isolated database state, migrations applied automatically); `wiremock` contract tests for outbound clients; property tests for domain constructors and round-trips; migration tests when the schema moves. Unit tests alone cover the layer backends break least; integration tests catch wiring, serialization, routing and state-setup errors.
- **Seven backend review questions.** Are credentials typed? Are logs redacted? Are failures shaped for the client? Are transactions explicit? Is idempotency defined for each mutation? What state is left if the process crashes mid-workflow? Should this work be asynchronous?
- **Default backend mode combinations.** New endpoint: Spec plus Delivery. Auth flow: Spec plus Security. Migration: Delivery plus Operations. Skip Spec mode only when acceptance criteria already exist. Never generate handler code before a requirement and a boundary decision exist.
- **Version-specific crate questions.** Read the target repository's `Cargo.lock` and the crate changelog; do not answer from memory of a crate's API. A `docs.rs/.../latest` link floats, so pin the version when citing behavior.

- **Worker split definitions.** Keep work inline until retries must be durable, the call fans out to unreliable systems, or a connection would hang. When you split, define four things: what the endpoint commits, what the worker consumes, what "already processed" means, and what operators can observe. A payment retry loop inline in a handler is wrong; so is a queue hiding a simple request flow.
- **Backend defaults.** Inline handling, domain types converted at the edge, and pools and clients held in app state and wired in one place. Deviate only with a named reason. Reusing transport types as domain types is cheap until a second writer appears.
- **Request lifecycle record per service.** Trace transport, handler, domain, persistence and integration, and mark the transaction owner, the correlation identifier hook, the inline-or-worker fork, and each layer's failure classes. Update it in the same change as any boundary or split decision; a stale record misleads incident responders. For a worker, trace from queue message to side effect.
- **Review order differs from build order.** Build shape first, then risk. Review risk first (credential handling, rollback safety, session handling), then shape.
- **Reference endpoint exercise.** Parse at transport, convert to a newtype at the edge, own one transaction, call a typed remote client, and prove it with a spawned-app test plus a `wiremock` contract test. The transaction must not span the remote call. Test the duplicate-submission case for idempotent replay and the remote-timeout case. Practice on write endpoints, not only reads.

- **Invalid inputs are named contracts.** Each empty, malformed and duplicate input case gets a requirement and a named test.
- **Scope each change to one service slice:** one endpoint or worker with its requirements, layer design and assigned tests. Do not put an endpoint, its schema change and a new worker loop in one change; split them. A risky schema change is several ordered deliveries, not one. Batching trivial read endpoints that share every boundary is acceptable.
- **Delivery speed is not the measure.** An inline remote call demos faster than a worker split until the first duplicated payment. When a layer keeps collecting incidents, its boundary is drawn in the wrong place.
- **Routing.** Libraries, CLIs, parsers, protocol crates and FFI follow the general Rust rules, not the backend rules. The costly misroute is the reverse: a web service reviewed as a generic library, so sessions, migrations and idempotency go unexamined. Worker and queue questions are backend questions.

- **Backend reliability targets, audited per release:** zero unowned transactions; zero repeatable writes without an idempotency definition; zero unclassified remote failure paths; a working rollback after every rollout step. All four are reviewable before deployment. High unit coverage does not show any of them. A waiver for an additive-only schema change is recorded against the sequencing rule.
- **Ambiguity is not caught by deterministic tests.** A timeout or crash that leaves a workflow in an undefined state passes every test and fails only under production timing. Kill a worker mid-workflow on staging and check the observable state transitions.
- **Three ways backend discipline decays.** Boundary erosion: business rules drift back into handlers; catch it with a lint for SQL in handlers and review. Split debt: an inline call that was correct at ten requests a day duplicates side effects at ten thousand though the diff never changed; re-check the worker-split criteria as traffic grows. Sequencing violations: schema and code shipped in an order that works on one instance and fails in a rolling deploy; require a sequencing plan with every migration. A slow call kept inline needs its tradeoff note, or it is indistinguishable from debt.
- **Before rollout, plan for a request surge:** rate limits, queue bounds, cancellation and a rollback procedure for when traffic exceeds handler or pool limits.

- **Retry ladder.** Classify every remote failure first: client error, server error, timeout, transport failure, malformed response. Then assign each class a policy: fail fast, retry, record for replay, surface to an operator, or move to async recovery. Retry only under an idempotency definition (key boundary, replay state, what counts as the same request, concurrent behavior). A retried client error burns quota; a retried timeout without a key may run the side effect twice. No blanket retry count. Move retries that must outlive the request behind a worker. Unbounded worker retries need alerting.
- **Never hold a database transaction open across a retrying remote call.** It turns remote slowness into pool exhaustion. Test each failure class with simulated faults and assert no double side effect.
- **Minimal service record.** One correlation identifier propagated through every layer and into worker handoffs; worker state transitions visible to operators; readiness separate from liveness; a secret-redaction check in review; error, timeout, retry and saturation counts. Trace sampling is acceptable on high-volume reads; keep mutations unsampled.
- **Performance: audit four mechanisms before reading latency numbers.** Pool and client reuse, transaction scope, inline-or-worker placement, and fan-out. Per-request client construction adds connection setup to every call; a transaction spanning a remote call serializes the pool; inline fan-out holds connections open. Then measure p95 and p99 on representative handlers against the SLO.

- **Fix the mechanism, not the symptom.** Do not add a cache over an endpoint whose pool is exhausted by held transactions; move the remote call after the commit. Averages hide the tail: one blocking credential hash on the async executor stalls every request sharing that worker thread.
- **Latency gate.** Require a service-specific SLO before deployment. Without one, hold representative handlers to p95 under 200 ms and p99 under 500 ms locally, or document why latency does not apply.
- **Scale seams are design events.** Traffic growth re-triggers the worker-split question. A second instance or a rolling deploy makes multi-step schema evolution mandatory: never ship a strict-constraint migration in one step. Moving work behind a worker adds queue tables whose schema changes then need sequencing. Several independent services are beyond single-service rules.

- **Name the task's dominant risk before designing.** The risk classes are ambiguity, delivery sequencing, operational safety, security, resilience and review readiness. The dominant risk is often not the stated topic: a migration's topic is schema and its risk is rollout ordering; a retry question is a resilience question, not a client-boundary one. Classify by risk, not by a keyword shared with the ticket.

- **Re-classify mid-task.** When a delivery task uncovers an auth or durability question, treat it as a new risk and apply that risk's rules before continuing. Risk rules consulted after the code is written arrive too late. Checking too much wastes minutes; checking too little ships unexamined risk, so when unsure check more.

- **A task that resists quick classification is compound.** Split it into slices that each classify cleanly (for example a migration-plus-worker ticket becomes two). When the guidance you applied did not answer the task, re-classify with the new information before re-reading the same material.

- **Configuration.** Parse configuration once at startup into typed settings and fail fast: an invalid or missing value kills the process at boot with a specific error. No environment-variable string lookups scattered through handlers. Settings parsed at startup but held as raw strings leave invariants unenforced. Test it: boot with deliberately broken configuration and confirm a loud, specific failure.
- **Operational adoption order.** Typed fail-fast configuration and secret redaction first, structured correlated tracing second, honest health surfaces third, then CI gates, image size, and migration sequencing. Do not write migration runbooks for a service that still crash-loops on malformed environment variables or prints passwords in logs. Tracing, correlation, health checks and failure classification are design concerns from the start, not polish.

- **Operability test for any runtime or rollout change.** State is explicit at boot, behavior is explainable per request, and change is reversible per rollout step. Do not weaken one to strengthen another. Prove each property before depending on it: configuration validated before serving, readiness proven before traffic, rollback verified before the next step. Reject a configuration flag read lazily at first use. Rollback options change after a constraint-tightening step, so re-check what rollback still works after each step. Document which dependencies readiness reflects.

- **Operational rejections.** Reject on sight: hard-coded runtime choices, secrets in logs or panic messages, ad-hoc string logging, a boot that limps past invalid configuration, configuration baked into the image, and schema changes that need an impossible deploy ordering. Enforce the greppable half in CI: grep for environment reads outside the settings module and scan log output for secret classes. Enforce the rest in review: require a rollback answer for every rollout step. A `Debug` derive on a settings struct defeats a redaction wrapper as soon as anything logs it; a hand-written `Debug` that elides secrets breaks when the next field is added, so wrap each secret field in a redacting type.
- **Migration-aware tests.** Any change that touches the schema runs tests against a real database with migrations applied, in CI, triggered by the schema diff. Green unit tests over a stale schema prove nothing, and without this gate the first contact with the new schema is the deploy. Never gate a deploy on compilation alone. Skip the build gate only for a path filter that is provably docs-only. Do not remove existing dependency-audit enforcement to go faster.

- **Schema or deploy-order change: deliver a rollout plan with the code.** Answer the five sequencing questions in writing: what lands first, what code works against both the old and new schema, when the backfill runs, when constraints tighten, and what rollback still works after each step. A migration file with no plan is incomplete; a required column added by a one-line migration is a defect. The intermediate release must read and write both schema shapes, so plan that code before the backfill starts. If backfill volume or data shape cannot be verified, say so in the plan. For a configuration change, state the boot-failure behavior.
- **Operational strictness defaults.** Fail fast at boot, record a curated set of correlated fields once and propagate them, and apply full sequencing to any change touching schema or rollout order. A service that must boot degraded lists exactly which dependencies readiness does not reflect. Wire correlation identifiers before the first deploy; incident response depends on them. Keep heavyweight gates conditional on the change class so nobody is tempted to disable them.

- **Strictness details.** Fail the boot on unknown configuration keys so a typo is caught at deploy. Express strict-in-production and tolerant-in-development through the configuration layers, not through code branches. The trigger for full migration sequencing is the kind of change, not its size: any schema change that alters runtime assumptions qualifies, including a small additive column whose constraint follows later. Do not trace every function entry; the request identifier must stay easy to find.
- **Per-service operations card.** Keep one page per service, created with the typed settings module and reviewed in every deploy-affecting change: configuration layers and which one wins, secret classes and who rotates them, the trace identifier and how it propagates, what readiness checks, and the standing rollout pattern. Whether readiness requires healthy background workers is a decision to record there.

- **Four-step schema evolution.** (1) Expand: add the new shape compatibly, with no strict constraint. (2) Deploy code that reads and writes both shapes; this is application work and is routinely underestimated because the schema diff already looks finished. (3) Backfill. (4) Tighten constraints. Never merge expand and tighten into one migration because the data looks clean. Re-answer the rollback question after every step: reversibility expires step by step, and after the backfill some data movements need a forward fix instead of a rollback. Rehearse on production-shaped data, including a deliberate rollback after step three; an empty database or a table without foreign keys hides the hard parts.
- **Operational outcome measures.** Track three ratios from records that already exist: configuration defects caught at boot versus found at runtime (deploy logs), incidents diagnosed from traces versus from log archaeology (incident retrospectives), and rollouts that completed every step versus aborted mid-sequence (release records). Read the boot-catch ratio alongside the absolute count of misconfiguration incidents. A rollout aborted through a working rollback counts as a success. The operations card lists secret classes, locations and owners, never secret values.

- **Operational invariants.** Zero secrets in logs or panics, ever; zero deploys of unvalidated configuration; every request traceable by one identifier end to end; every rollout step with a rollback that has been executed in staging, not only written down. The first two are binary per event: one leaked key is a full rotation incident. A tracing crate in `Cargo.toml` proves nothing about propagation; sample real traces. A batch job with no requests still correlates by job identifier.
- **Operational decay happens through additions.** New knobs bypass the typed settings module, new code paths skip the correlation field, health checks stop reflecting real dependencies, and each successful migration is used to justify less sequencing on the next. Probe each: count environment reads outside the settings module, check trace-field coverage for every new endpoint, compare readiness checks against the real dependency list, and require the sequencing answers on every schema change regardless of recent success. Removing a dependency check from readiness because it slowed the probe is how a green endpoint ends up over a failing service.
- **Estimate a sequenced migration as several deliveries.** Each step is its own release; short SQL does not make it one ticket. Do not batch two unrelated migrations into one sequence, because their rollback answers then depend on each other.

- **Deploy-time retries: two regimes.** A failed boot, health check or image build changed nothing durable, so retry it automatically under a crash-loop ceiling. A failure inside a migration step is never simply rerun: stop, page a human, and start from that step's planned rollback answer. Mark migration steps non-retryable in a pipeline that retries uniformly. Do not rerun a timed-out backfill blindly, do not auto-reverse a partial backfill, and do not stack a second release behind a paused migration; the dual-shape code lets the paused state serve traffic while it is assessed. Verify on staging by injecting a failure of each kind.
- **Telemetry floor, wired at setup and checked for each new endpoint.** Structured traces, not string logs; one request or operation identifier propagated end to end, including into workers and background jobs; high-value fields recorded once and propagated, never re-derived per layer, because a field that disagrees with itself across spans is worse than a missing one; health surfaces that reflect real dependencies; a log shape usable for both local debugging and operator triage. Sampling high-volume reads is acceptable; mutations stay unsampled. Test: walk one recent production request by identifier alone.
- **Operational performance.** Record per release: boot-to-ready duration, pipeline wall time, image build time with a cold and a warm cache, and traced-versus-untraced request overhead. Alarm on the trend, not a fixed ceiling, because these degrade one dependency, gate or field at a time. Rust image builds are the likeliest offender: order image layers so dependency compilation is cached separately from application source, and re-check after dependency-graph changes.

- **Operational scale triggers.** Enabling autoscaling or a rolling deploy crosses the multi-instance line on the day it is configured, not on the first scale-out: make migration sequencing mandatory in the same change. The safe default is to use the four-step pattern from day one. Many services need templated setup; hand-wired configuration across a fleet drifts. When deploy authority and schema authority belong to different owners, write the handoff down. Generic container layer advice can worsen Rust build times; verify cache behavior against Rust's dependency compilation.

- **Backend test suite shape.** For an HTTP service the outside-in integration test is the primary instrument, because backend defects cluster in wiring, serialization, routing and state setup, which lie between units. Unit tests keep domain constructors, validation, parsing edges and small pure decisions. Integration-first is not integration-only. Each defect class has one cheapest catcher; choose the test kind by concern, not by rank.
- **Build order for the suite.** First a harness that boots the app under test configuration; second isolation (random port, per-test database state); third HTTP mocking for external calls; then helpers, property tests and the concern-by-test matrix. Property tests are selective and strongest at the domain edge. Do not start a property-testing effort on a service that cannot spawn itself in tests.
- **Tests read as user journeys.** A test should read "create user, post order, expect 201 and a persisted row", not as six internal imports assembling state before one assertion. A helper that hides too much logic stops helping: every failure becomes a harness investigation. An internal setup shortcut is acceptable as a labeled helper. Unit-testing an extractor's deserialization is useful, but still run one pass over the wire. If tests share infrastructure, write down the isolation boundary and why it is safe.

- **Test-suite rejections.** A harness on a fixed port; tests sharing undocumented infrastructure; a deterministic suite that calls a real external API (calls to a staging instance belong in a separate, deliberately non-deterministic suite); helpers that hide the logic under test; property tests standing in for end-to-end coverage; a unit-only suite certifying wiring it never exercised. Grep test code for fixed ports and real external hosts. These defects ship green and show up first as flakes, so a rising flake rate is an early warning.
- **Concern-to-test matrix as the merge gate.** Endpoint behavior: integration. Domain invariants: unit or property. Database work: integration with real migrations. Remote APIs: HTTP mocks. Auth flows: combined coverage. Migration safety: schema and rollout checks. A substantial backend change lists the concerns it touches and shows the assigned test kind for each. Rising overall coverage is not evidence, since it cannot say which concern a covered line certifies. The matrix also catches over-testing, such as property tests on plain data transport.

- **When generating backend tests.** Start from the concerns the change touches, not from the module structure of the diff. Reuse the existing harness instead of inventing setup; if the service has no harness, building one is the first task. State which concern each new test certifies. Do not write mirror tests (one unit test per touched function, asserting that a handler returns what it returns). Existing tests are copied as the style guide, so fix a fixed-port or live-API test before adding more beside it. If no concern in the matrix covers a new path such as a webhook, raise it. An intermittent failure is usually isolation debt or a missing mock: check which tests share state first.

- **Realism, isolation and helper trade-offs in tests.** Default: run the real migrations in test setup so tests see the production schema shape, isolate state per test, and use helpers that state intent without hiding logic. Each deviation is a documented exception. A fake states which behaviors of the real dependency it does not reproduce. An in-memory repository is fine for pure domain tests, which then certify domain rules and never database behavior. Do not make the whole suite slightly less isolated to run faster: one intermittent test taxes every build, so relax isolation per documented boundary or not at all. A fast unit tier on every commit with the full integration tier on merge is acceptable if each tier's coverage claim stays accurate.

- **Suite manifest.** Keep one page per service suite, updated in the same change as the infrastructure it describes: harness entry point, isolation strategy per resource, documented sharing boundaries, the mocks that exist for each external system, and coverage status per concern. "Unknown" and "missing" are valid entries; a manifest that claims full coverage it does not have is worse than none.
- **Reference endpoint test.** Spawn the app on a random port against an isolated, migrated database; send the request; assert the response and the persisted row; mock the downstream API and assert the shape of the outbound request. A mock that matches any request passes everything, so see the outbound-shape assertion fail once before trusting it. A spawned app against a shared database, or a mock that asserts nothing, only looks like integration testing.
- **Flake accounting.** A quarantined flaky test is triage, not a fix; keep counting it. A falling flake rate may only mean a growing quarantine list.

- **Suite invariants to enforce.** No fixed port in test code (a hard-coded 8080 or 5432 fails CI); every shared resource has a documented isolation boundary; every external integration is mocked in the deterministic suite; every substantial change is mapped to its concerns. The first, third and fourth can be checked by machine. One live external call in the deterministic suite is a source of nondeterminism in every build, not a tolerable percentage. Absence of recent flakes does not prove isolation.
- **How a suite decays.** New tests quietly share state the original harness kept separate; authors hand-roll setup around the harness (for example importing the database pool directly); mocks drift from the real API's current shape; new kinds of concern appear with no assigned test kind. All four happen in new tests while old ones stay correct, so review a new test's infrastructure choices and not only its assertions. Stop the first harness bypass, because the next author copies it; a justified bypass (one unusual websocket test) is recorded with its reason. Periodically shuffle test order and re-record external contracts.
- **Suite cost.** The first integration test carries the cost of the harness; do not reject integration testing because that first estimate is large. A schema migration can break fixtures silently, so repair fixtures in the same change as the migration. A throwaway prototype may skip the harness if it says so.

- **Failing test versus flaky test.** A deterministic failure is fixed forward; rerunning it changes nothing. No automatic retries in the deterministic suite, and never merge on the third rerun's green. One deliberate rerun to tell deterministic from intermittent is legitimate when the result sends the test to quarantine, with an owner and a deadline, and not to merge. Cap the quarantine list; if it grows month over month, stop adding integration tests and repay the isolation debt first. A deliberately non-deterministic suite against staging may retry within stated bounds.
- **Mocks drift on the provider's schedule.** Compare each mock with the real API's contract on a calendar, not only when tests change. Keep an inventory of what each mock simulates per external system, generated from the mock definitions where the framework allows, so "what do we assume about the payment API" has an answer without reading every test. A test name that states the journey and the concern makes the suite self-describing.
- **Suite speed.** Track suite wall time, per-test setup cost and time to the first test on a new service. When wall time rises, review which speedups leave the isolation boundaries intact before optimizing, because sharing state is the easiest speedup and the wrong one. A suite developers stop running locally has lost its value.

- **Where the single-app harness stops.** The harness assumes one service, one database the test owns, and a suite one team runs whole. A second service in one journey calls for contract tests: split the journey into one harness test per service plus a contract pair, not one test that spawns three services by hand. A shared datastore calls for schema-level isolation with the boundary documented. A suite too slow to run locally calls for tiered execution, valid only while every merge still answers to the full matrix somewhere. A test that is awkward to write is a sign one of these assumptions no longer holds. If most of the runtime is setup and not assertions, parallel runs or template databases cut it without touching a test.

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

Auth and recovery flows:

- **Secrets.** Wrap credentials and tokens in typed, redacting values, keep their exposure minimal, hash passwords, and store reset tokens hashed and scoped. A secret wrapper formatted into a log line is still a leak.
- **One public shape for auth failures.** Login and reset return the same response, status code, redirect and timing whether or not the account exists. Operator diagnostics go to logs and traces, not to the client. Keep login and reset as separate flows.
- **Commit, then effect.** Persist the intent, commit, then perform the remote effect from a deduplicated worker with visible status. Never send mail or call a remote system inside the transaction, and never return success before the intent is durable. Synchronous remote work is acceptable only when it is bounded, idempotent and safely recoverable.
- **Idempotency keys** are bound to the request content and the caller; a replay must not return a response the caller is no longer authorized to see. Keys and tokens expire.
- **Workers** acknowledge a job only after durable completion and tolerate duplicate delivery.
- **Every externally visible result corresponds to a durable, authorized state** that can be explained after a crash. Model each flow as an explicit state machine.
- **Tests for these flows.** Compare public failure responses and timing for known and unknown accounts; race identical writes; replay and reuse reset tokens concurrently; crash before and after commit; inject each remote failure class and a timeout after remote success; replay jobs; check that an operator can see and reconcile stuck state.
- **Scope.** This list is not a threat model. Authorization, CSRF, SSRF, TLS, key management, dependency risk and data retention need their own review. If no durable store for idempotency and recovery exists, narrow the operation, fail closed, or require manual reconciliation. Choose hashing crates and parameters from current documentation for the locked version.

- **Release blockers in auth and recovery code.** Raw credentials past the adapter; secrets in logs; public failures that depend on identity; reusable or overbroad reset tokens; idempotency keys not bound to actor and normalized request; a lock or transaction held across a remote effect; retry of a permanent failure; a remote call with no timeout; a job that is not durable; an acknowledgment before durable completion; a status transition written after the acknowledgment. Reset tokens are not sessions: single use, scoped, hashed. An unmodeled intermediate state is the most dangerous defect, because it can leak information and duplicate effects at once.
- **Check framework behavior against the locked version.** Read `Cargo.lock`, enabled features and the matching docs for extractor rejection shape, middleware order, timeout semantics and graceful shutdown; latest docs may not match. A correct runtime and framework can still compose into an unsafe flow, so test the composed flow. A type wrapper is not access control.

- **Design order for a security-sensitive flow.** Assets and actors; public observations; durable states and effects; typed boundaries and error classes; idempotency and transaction scope; inline or worker; abuse and crash tests; staged rollout with a rehearsed rollback. Decide the state and observation contract before coding.
- **Test fixtures for these flows.** `cargo test` alone is not enough. Use a database-backed fixture with isolated state, controlled clock and randomness, and a fake remote that can fail both before and after its effect. Run concurrent requests, not only sequential ones. Make sure background tasks do not outlive the test. Run password hashing on the blocking pool, not on the async executor. A read-only route may omit write-replay tests if the scope is stated.

- **Per-flow trade-offs.** Decide auth, retry and recovery per flow and deployment, not through one global policy. Deny by default. Sessions need a revocation path. Idempotency storage must not retain sensitive payloads longer than data policy allows. A queue moves a failure; it does not remove it, so add background work only with a durable owner and operator recovery. Retries can amplify an outage. A deploy rollback does not roll back data. Do not assume client retries arrive sequentially. Prefer the option with the fewest ambiguous states over the one with the lowest latency or least code, and never drop durable state for performance without recording it.

- **Flow threat-and-recovery record, required for sensitive or mutating flows.** Goal, assets, actors, trust and authorization boundaries, secrets, public observations, state machine, transactions, idempotency, remote effects, failure classes, timeouts, workers, logs, abuse cases, controls, tests, rollback, residual risk. Every ambiguous outcome is assignable to one durable state, one owner and one next action. Typed identifiers do not imply authorization. Check that secrets and payloads do not end up in logs or idempotency records, and that remote effects carry a correlation identifier. A read-only route may use a reduced record if it exposes no sensitive topology.
- **Product-required disclosure is an isolated exception.** If a flow must reveal account state (for example an invitation flow), confine the exception to that flow and test its abuse boundary. Tests that encode enumerable behavior are defects, not specifications. An incident workaround does not become policy.

- **Security-flow outcome measures.** Count secret-exposure findings, observable differences between auth responses, token misuse cases, duplicate-effect incidents, unresolved idempotency races, ambiguous timeout states, retry amplification, worker job age and terminal states, and rollback failures. The most useful single number is unexplained state after a failure. Zero incidents is not proof, fewer compile attempts or review comments say nothing about security, and the metrics themselves must not expose identities. Completeness means no unexplained observation or state inside the declared flow; it is not a claim about the whole system.

- **Review scope for security flows.** One review covers one asset and one durable workflow. Split by authorization domain, transaction boundary, remote effect, worker lifecycle, deployment unit or operator; endpoint and request counts do not predict review effort. Review password reset separately from session refresh, then reconcile the token and logging controls they share. Keep one owner for the end-to-end visible and durable contract. Distinguish authentication from authorization, a runtime timeout from a business deadline, a framework rejection from a product error, and a dependency advisory from exploitability.

- **Retry preconditions.** Retry only a classified transient failure, and only after confirming: the caller is still authorized, the request identity is unchanged, the replay state is durable, the transaction outcome is known, deadline remains, the attempt count is bounded, deduplication is in place, and no remote effect is unresolved. A timeout after the remote may have acted is ambiguous: freeze replay, reconcile the provider's record with durable state, then resume. Never retry an ambiguous charge-like effect. Client errors do not enter worker queues, and a cancellation is not a failure to replay. Operator replay requires reconciliation first and is itself a recorded transition. When state is unclear, slow or stop intake; further requests obscure which effects already happened.
- **Failure containment.** Locate the failing phase: credential edge, token state, public response, authorization, idempotency lookup, transaction, post-commit effect, remote failure class, timeout, enqueue, worker attempt, terminal status, rollback. Containment keeps enough evidence to tell apart no effect, durable intent, remote success and completed workflow. Do not map every fault to a 500, delete duplicate effects without a root cause, or restart in a way that erases evidence. Options: fail closed, revoke or expire tokens, stop intake, disable workers, reconcile, narrow the rollout.

- **Secret-safe observability.** Link events with an opaque flow identifier, never an email, token or key. Record the durable transition, transaction result, remote failure class, timeout, worker attempt, terminal status and rollback trigger with redacted data. Do not label metrics or logs by whether a user exists, do not put payload data in idempotency keys, and avoid high-cardinality identity labels and timing dashboards that expose cohorts. Log failures and cancellations as well as successes. Detailed operator records need access control and bounded retention. The test: reconstruct one flow's state from its events, and confirm the events reveal nothing an attacker could use.
- **Benchmark with the controls on.** Measure success, denial, duplicate, timeout and saturation paths with hashing, durable writes and failure shaping enabled; removing them makes an unsafe path look fast. Check that auth variants are not distinguishable by timing. Throughput gained through unbounded queues does not count. Measure password verification separately. Fixed latency numbers are placeholders until the service has its own SLO.
- **Across services.** A local transaction and typed states do not span independent services, and exactly-once delivery cannot be assumed. Carry idempotency and correlation identifiers explicitly, define authorization and replay semantics at each interface, give each queue one owner, and define rollback order. One endpoint review does not certify a distributed workflow.

- **Levels of security evidence.** Documented is not locked, locked is not reachable, tested is not deployed, deployed is not observable, and observed once is not attacker-resistant. State which level each security claim rests on. Compile success proves no authorization property and one abuse test proves no general one. After a framework, runtime or advisory change, re-check the exact locked versions, reproduce the public response behavior, and update the abuse tests. Do not copy a security middleware example without checking it against the locked version and the flow.

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

```rust
use opensearch::{OpenSearch, http::transport::Transport};
use serde_json::json;
let transport = Transport::single_node("http://localhost:9200")?;
let client = OpenSearch::new(transport);
let resp = client.index(opensearch::IndexParts::IndexId("logs", "1"))
  .body(json!({"msg":"hello","ts":123}))
  .send().await?;
```

- **MessagePack.** Use `rmp-serde` for compact binary serialization. Cap message sizes, validate input, add a schema or version field, do not assume map key order, and do not deserialize untrusted data into unbounded nested structures.

```rust
use rmp_serde::{encode::to_vec_named, decode::from_slice};
#[derive(serde::Serialize, serde::Deserialize)]
struct Event { id: u64, msg: String }
let bytes = to_vec_named(&Event { id: 1, msg: "hi".into() })?;
let evt: Event = from_slice(&bytes)?;
```

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

Run these in the order listed: it is also cheapest-first, so the fastest check fails first. Keep `--all-targets --all-features` on every one; dropping the flags quietly shrinks the gate, and feature-gated code that never builds in CI is the usual way a defect gets through. `clippy` without `-D warnings` does not count as the gate. A waiver with a stated reason may apply to a local convention (four-word naming on a stable public API, Mermaid diagrams where the project has no such standard), never to these commands. When you skip the higher-risk gates (release-mode tests, coverage floor) on a low-risk change, record that risk call.

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

Workspace hygiene:

- Declare dependency versions once at the workspace root and inherit them in member crates; use path dependencies between local crates.
- Share common types through one workspace crate.
- Keep optional dependencies behind features, grouped by feature set.
- Re-export the public API from `lib.rs`.
- Run `cargo clean` after a major dependency or workspace-configuration change, or when build errors make no sense, before trusting a critical test run.

### Gate discipline

- **Before any completion claim:** identify which command proves the claim, run it fresh and in full, inspect the output and exit status, report the actual result, and only then claim success or incompleteness.
- **No completion claim survives if:** requirement coverage is missing; failure paths that matter are untested; a performance claim lacks evidence; concurrency assumptions are hand-waved; cancellation or shutdown is unspecified for a long-running task; or a public API changed without a compatibility review.
- **API, unsafe and generated-code gates:** review public API changes for leaked dependency types, error surfaces and re-exports; unsafe changes carry `SAFETY` reasoning and targeted invariant tests; regenerate or diff-check generated sources from their true inputs; treat each Clippy suppression as a design decision with a stated reason.

Rule to test to gate:

| Rule | Test type | Gate |
| --- | --- | --- |
| newtypes at boundaries | unit + conversion, valid and invalid parsing | `cargo test` |
| typestate | compile-fail on illegal state transition misuse | compile-fail suite |
| recovery-aware errors | unit: retryable versus permanent branch | `cargo test` |
| iterator pipelines | property: transformation correctness and order | `cargo test` |
| workspace and features | integration: root build and feature matrix | `cargo build --workspace` |
| no blocking, no lock across await | stress | `cargo test` |
| bounded concurrency and cancellation | integration + timeout + cancellation | `cargo test` |
| task ownership | teardown + failure propagation | `cargo test`, optional `loom` |
| transport to domain at the edge | integration: conversion and error shaping | `cargo test --all-targets` |
| unsafe containment | harness, wrapper invariants | `cargo test`, optional `cargo miri test` |
| explicit close | integration + teardown | `cargo test` |
| shutdown fan-out | integration + signal + timeout | `cargo test` with shutdown scenarios |
| dependency exposure | downstream compile + doctest | API review, optional SemVer tooling |
| measure first | benchmark + profile | benchmark gate |
| all rules | format and lint | `cargo fmt --all -- --check`, `cargo clippy --all-targets --all-features -- -D warnings` |

### Completion contract for an agent

- "It compiles" is not done. Done is: the four required commands green with their output shown, the release checklist affirmed item by item, and none of the review rejections present. If you cannot run commands, list them as follow-up for a human; do not claim them.
- Before handoff, grep your own output for placeholder markers (`TODO`, `FIXME`, `todo!()`, `unimplemented!()`).
- A requirement id in the traceability table must point at a real requirement; never invent ids to satisfy the gate. If a checklist item does not apply (documentation on a change that touches no documented behavior), say why.
- The commands catch what a machine can see: format, lints, failing tests, build breaks. They cannot see an unmeasurable requirement, a layer leak that compiles, a design that cannot be tested in isolation, or concurrency that passed one run. Check those by reading, and ask of every design: what here cannot be tested?
- A pinned `clippy -- -D warnings` gate can start failing after a toolchain update with no code change, because new lints arrive; that is intended. If features are mutually exclusive, `--all-features` cannot build: document the feature sets the gate runs instead.
- Read the review rejections at planning time as well; they are cheapest to act on before the architecture is fixed.

- **Gate record at handoff.** With a release or handoff claim, attach: the four command results and the toolchain version they ran under; the risk classification and whether the advanced gates ran; each checklist item with a pointer to the test, doc or threshold that makes it true (a clean grep output is a valid pointer for the placeholder item); and the verdict of the review-rejection pass. A later defect can then be traced to a gate that failed or a gate that was skipped, which need opposite fixes. A green badge alone is not a record.
- **Naming conventions versus stable APIs.** Do not rename a published API to comply with a naming convention. Keep the stable surface, give new surfaces the clear names, and bridge with an adapter that states when it will be removed.

- **How the gate decays.** Flags trimmed from the commands to save CI time (review such a change as a change to the gate, not as minutes saved); the review-rejection pass quietly dropped while the badges stay green; universal rules reclassified one by one as waivable local conventions; checklist boxes ticked from a template with pointers that no longer resolve. Each keeps the visible artifacts and verifies less, so compare the CI configuration with the command list and follow a sampled pointer to its evidence. Require the four commands in branch protection so they cannot be skipped. A hotfix that bypasses the review pass under incident pressure says so in the record and runs the pass afterwards.
- **A failed required command is fixed, not rerun.** `fmt`, `clippy` and `build` are deterministic for the same source and toolchain; a test command that flakes is reporting test-isolation or environment debt. Take toolchain updates as scheduled changes so new lints arrive as planned work.
- **Gate cost is fixed per handoff.** Automate the commands and the record, and prefer small frequent handoffs. Batching work into one large change to pay the gate less often makes the review pass shallow and defects harder to attribute.

- **Lint drift is not a flake.** A `clippy` failure right after a toolchain update is a new lint generation, not nondeterminism; the toolchain version in the record tells the two apart. When the gate fails repeatedly, stop starting new work and repay what it reports: toolchain drift, flaky tests or a broken feature combination.
- **Secret-logging check.** Check per handoff that no secret or sensitive payload is logged; no compiler error hints at this one. Look at debug, error and crash paths first, because a handler that prints the whole request is invisible on the happy path. Richer logging and tracing widen the leak surface, so adopt typed secret wrappers together with them.
- **Performance wording.** Every performance statement in requirements, docs, release notes or a changelog carries a threshold and a method ("p95 under 10 ms on the named benchmark"), or is marked unverified. "Significantly faster" fails. "Faster than the previous release" passes only with the comparison method and the margin. A threshold with no runnable method fails as surely as no number.
- **More than one workspace.** One gate record must not sign for a workspace its commands never ran against. Run the commands per workspace and combine the results into one record.
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

### Technique checklist by area

Before finishing a design, check whether one of these applies:

- **Ownership:** move a value out of a `&mut` place with `mem::replace` or `mem::take` instead of cloning; move out of collections with `drain`, `pop`, `swap_remove` or `into_iter`; take owned values in constructors and borrow in method arguments; derive `Clone` only on types that should be cheaply copyable.
- **Resources:** release in reverse order of acquisition (fields drop in declaration order, locals in reverse); pool expensive resources such as connections and buffers; cap resource use with explicit limits.
- **Builders:** validate in `build()` and return `Result`; implement `Default` for the common case; choose consuming (`self`) builders for one-shot construction and `&mut self` builders for reuse; use type-state or phantom-typed builders when required fields must be enforced at compile time; nest builders for nested configuration.
- **Traits:** extension traits to add methods to foreign types; marker traits for compile-time capabilities; conditional impls (`impl<T: Bound> Trait for Wrapper<T>`); default method implementations to keep required methods minimal; auto traits (`Send`, `Sync`, `Unpin`) are inferred from fields, so check them after adding a field.
- **Types:** const generics for sizes and capacities known at compile time; type aliases only to shorten names, never for type safety.
- **API shape:** implement `Display` for user-facing text and `Debug` for every public type; `AsRef`/`AsMut` for cheap view conversions; visitor for traversing heterogeneous trees; command, strategy and factory as enums or trait objects; adapter to fit a foreign type to a local trait.
- **Macros:** internal rules (`@name` arms) to hide helper cases; recursive macros only with a clear base case and bounded depth.
- **Tests:** parameterized tests (table of cases, or `rstest`); shared fixtures and test utilities in one module; assertion messages that state the expected behavior; unit tests beside the code, integration tests under `tests/`.
- **Safety:** safe wrapper types that own an invariant; panic guards that restore state in `Drop`; capability or permission types that must be held to call an operation; validation chains that return the first or all errors.
- **Performance:** batch work to amortize per-call overhead; compute at compile time with `const fn` and const evaluation; use SIMD and prefetching only with a benchmark that proves the gain; lazy initialization for expensive, rarely used state.
- **Async services:** stream processing with bounded buffering; timeouts on every external call; rate limiting at ingress; circuit breakers around failing dependencies; async initialization done once and awaited before serving; errors propagated with context across task boundaries.
- **Collections:** custom iterators in place of exposing internals; `sort_unstable` when stability is not needed and `binary_search` on sorted data; views and cursors in place of copies; checked indexing (`get`) where an index can be out of range.
- **Serialization:** derive serde where possible and write custom impls only for a real format need; version every persisted or wire format and plan schema evolution (`#[serde(default)]`, optional fields, explicit version tag); validate during deserialization (`try_from`, `deny_unknown_fields`) so invalid data never becomes a domain value; choose binary formats for size and speed and text formats for human editing.

- **Networking:** pool connections; retry only idempotent operations, with capped exponential backoff and jitter; put a deadline on every request; define wire contracts with Protocol Buffers (`prost`, `tonic`) or another schema when several services share them.
- **FFI:** wrap each C API in a safe type that owns the handle and frees it in `Drop`; convert strings with `CStr`/`CString` and never assume UTF-8 or a trailing NUL; pass arrays as pointer plus length; state which side allocates and which side frees; pass callbacks as `extern "C" fn` with a `void*` user-data pointer and catch panics inside them; map errors to integer codes plus an out-parameter or last-error call.
- **Optimization order:** measure, find the bottleneck, then fix in this order: algorithm, data structure, allocation, cache layout, parallelism. Stop when the stated target is met.
- **Middleware:** express cross-cutting concerns (auth, tracing, timeouts, limits, compression) as Tower `Layer`/`Service` values composed with `ServiceBuilder`; keep middleware state in a cloned handle; order layers deliberately, because the outermost layer sees the request first.
- **Runtime typing:** prefer enums and generics. Use `Any`/`TypeId` downcasting or type erasure only at real plugin or registry boundaries, and keep the erased type private.
- **I/O:** wrap files and sockets in `BufReader`/`BufWriter`; use vectored (scatter-gather) writes for multi-part frames; reuse buffers (`bytes::BytesMut`); use async file APIs or `spawn_blocking` for file I/O in async code.
- **Streams:** bound buffers; split, merge and window with `StreamExt` combinators; decide per stream whether an item error ends the stream or is skipped; make every stream cancellable by drop.
- **Platform abstraction:** wrap OS APIs and syscalls behind one trait or module per capability; detect CPU features at run time (`is_x86_feature_detected!`) before using them; keep a portable fallback.
- **Macro debugging:** inspect output with `cargo expand`; document every exported macro with a compiling example.

- **`Option` misuse:** never write `if x.is_some() { x.unwrap() }` or nest `match` on options; use `if let`, `let else` or combinators. In tests, compare whole values (`assert_eq!(Some(expected), result)`) and test the `None` case explicitly.
- **Unsafe and panics:** keep invariants true at every point where a panic can unwind (exception safety); if they cannot be, restore them with a guard in `Drop`.
- **Async networking:** set connect, read and write timeouts separately; configure keep-alive; reconnect with backoff; terminate TLS with `rustls` unless a platform stack is required.
- **Compile-time validation:** assert layout and size facts at compile time (`const _: () = assert!(size_of::<T>() == N);`); validate constants in `const fn` constructors; let type-level constraints and const generics reject invalid combinations; treat dead-code warnings as errors.
- **Long-lived state:** model it as an explicit state machine with validated transitions; persist snapshots with a version tag, migrate old versions on load, and test recovery from each persisted version.
- **Async tests:** use `#[tokio::test]`; control time with `tokio::time::pause` or `start_paused = true` instead of sleeping; mock services behind traits; inject faults (timeouts, dropped connections, partial writes); test races with `loom` or repeated stress runs.
- **Library releases:** follow SemVer, check each release with `cargo semver-checks`, deprecate before removing, and record breaking changes in a changelog.

### Review questions

- **Types and invariants.** Which invariant is carried only by comments, not types or tests? Which primitives stand for distinct domain concepts? Where would a newtype, enum or `TryFrom` remove a whole bug class?
- **Ownership and API surface.** Where does ownership look accidental? Which function takes ownership only because that was convenient? Which borrows only because the author avoided moving, though ownership is semantically correct? Which public API leaks internal storage or adapter shape and will be painful to evolve?
- **Errors and recovery.** Which error path makes callers guess the recovery strategy? Are typed and dynamic errors at the right layer? Where is error context too vague to diagnose quickly? Are non-UTF-8 or binary boundaries handled safely? Which public error or type has committed the crate to a dependency's SemVer?

- **Async and concurrency.** Where is behavior unspecified under cancellation or timeout? Which queue, channel or task fan-out lacks a bound or saturation policy? Which clone, allocation or lock hides a boundary mistake? Is any task spawned without ownership, shutdown and error visibility? Does any cleanup path need awaiting, blocking or remote coordination without an explicit shutdown API? Where could a logical race exist although the code is data-race-free?
- **Architecture and boundaries.** Are transport, domain and persistence shapes separated? Does a framework type leak inward? Are trait seams at real external boundaries and absent elsewhere? Could a fresh contributor or agent build and test from the workspace root without hidden knowledge? Is any generated surface being edited as if hand-written?
- **Verification honesty.** Does each important claim have fresh evidence? Is each bug fix backed by a failing-then-passing regression test? Does the test mix match the risk surface, or only the easiest unit cases? Which performance claim lacks a threshold or profile?
- **Abstraction skepticism.** Which abstraction is not yet justified by reuse, invariants or compatibility pressure? Where is unsafe, proc-macro, lock-free or typestate complexity used for show? Would a simpler boundary give clearer guarantees?
