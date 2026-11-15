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

Before the ladder: choose the work mode, then read the actual code and its callers, and only then pick a pattern. A guide is a checkpoint inside the work, not the implementation plan. The cheapest correct change may be a repaired test or a documentation fix. When a test goes red, confirm it fails for the intended reason and not on a compile error or a setup mistake. A public name kept for compatibility can stay while new private items follow the current convention, and replacing a public error type is a SemVer break.

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

- **Idiomatic means fewest hidden contracts.** Idiomatic Rust is the smallest design that makes ownership, invalid states, failure, task lifetime and dependency direction visible. It is not the most types, the most generics, the fewest clones or the deepest abstraction. Do not apply an idiom list mechanically: keep a concrete type until callers need an abstraction, add a trait only at a real substitution seam, take owned values at real ownership boundaries, stay synchronous when nothing needs async, and keep the repository's existing error convention. `AsRef<str>` earns its place only when it simplifies real callers without ambiguous conversions. A newtype with no validation, `Arc` by habit and a benchmark with no stated constraint copy the shape of an idiom without its purpose.
- **Where contracts hide.** SemVer effects of a public signature, allocations inside ergonomic conversions, lock guards held inside helper functions, cancellation after a partial effect, object safety of a trait, feature combinations, and doctests that compile under a different `cfg`.
- **Framework evidence is local.** An Axum or Tokio example justifies code on that framework at the locked version. It does not justify the design of a CLI or a parser library.

- **Decide per API, not by slogan.** Choose each idiom for one API and one lifecycle. The right choice lowers the total contract complexity for the implementation and its callers together, not inside one function. A good default: borrow the input being parsed and return an owned domain value. Cloning a small value at a task boundary is idiomatic when it makes ownership simpler and the task count is bounded.
- **Costs that spread to callers.** Lifetime parameters in public signatures, blanket conversions that hide which conversion ran, error enums that grow without limit, `Arc` spreading through every type, a borrowed input tied to a returned reference, and a mock that drifts from the production implementation.
- **Existing code and general idioms both have limits.** Existing code is not idiomatic just because it exists, and a repository test can lock in an accidental API. A general idiom still does not override an existing public contract, feature set or MSRV without a migration.

- **Applying a rule from any guide, this one included.** Follow a rule only when the failure it prevents can happen in this task, it fits the task mode and the repository's boundaries, and a fresh check can show it held. An example in a guide can encode an obsolete crate API, and a broad principle can be over-applied: testability does not mean a trait on everything. Do not implement every listed pattern; pick the smallest rule that covers the risk.

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

Keep all seven sections in this order, even when one is short: a reviewer can then check that a section is present before reading its content, and an output with no Quality Gate Results is rejected unread. Open Questions is the easiest section to skip and the most useful signal. An empty list on a vague or under-specified task reads as overconfidence, so list what was assumed. Where a section owes nothing, say so in it: a refactor with no stated performance requirement owes no thresholds.

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
- The IDs are flat. Two work packets in one program both start at `REQ-RUST-001`, and a trace then joins requirements that are unrelated. Prefix IDs by component or service as soon as a second packet shares the program, and do not reuse a retired ID in the same crate.
- Express behavior as `WHEN ... THEN ... SHALL`.
- A requirement without a measurable threshold or an observable effect is not a requirement yet; send it back.

### Requirement contract template

```markdown
### REQ-RUST-001.0: <short title>

**WHEN** <trigger or input condition>
**THEN** the system SHALL <primary behavior>
**AND** SHALL <secondary measurable behavior>
**SHALL** <edge-case or default behavior>
```

- Keep each `SHALL` independently testable.
- Use explicit units for latency, memory, throughput, retries and concurrency limits.
- Retry behavior is a requirement, not a loop added in review: state the retry count, the backoff shape and the concurrency ceiling with units, and link each to a test. A metric showing thirty retries against a stated three is then a violated requirement. State what the requirement assumes about retries in the infrastructure below it. A correct retry requirement can still be implemented on a future that is not cancel-safe, so check the implementation as well.
- A latency regression on a path with no stated threshold violates nothing; add the missing clause. Ask whether a requirement set that is silent on performance is indifferent or avoiding the test.
- Split requirements; do not stack unrelated behavior into one clause.
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

Enter these templates at the first input that is missing. A vague request starts at the rewrite table; a request with testable requirements starts at the work packet; test skeletons come only once requirements and design exist, and a trivial fix can go straight to one. Starting at the skeletons because they look most like code produces tests for requirements nobody stated.

A filled-in template can still be hollow. A `WHEN` clause that says "sometimes" or a metric column that says "fast" satisfies the shape and defeats the rule, so review what is in the blanks against the rewrite table, not only that every section is present.

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

The mode block is example filler: replace it with the modes actually chosen. A packet whose blanks still read like the template is hollow. Fill the gate lines with real command results; a packet with empty gate lines is not complete, and passing tests do not imply the `--all-targets --all-features` build passes, so report the build line separately.

A packet is one document, not six stapled sections. Every requirement ID reappears in the verification matrix, and every matrix row reappears in the plan; a search for the IDs checks it. Matrix rows copied from the example give themselves away by citing IDs the packet never defined. A test row with no requirement behind it means the requirement is written first.

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

**Algorithms over minimum behavioural traits.** When a library has several storage representations, define the smallest composable traits each algorithm needs and implement them per backend, so one algorithm serves all.

```rust
pub trait IntoEdges: IntoEdgeReferences + IntoNeighbors {
    type Edges: Iterator<Item = Self::EdgeRef>;

    fn edges(self, node: Self::NodeId) -> Self::Edges;
}

pub fn dijkstra<G, F, K>(graph: G, start: G::NodeId, goal: Option<G::NodeId>, edge_cost: F) -> HashMap<G::NodeId, K>
where
    G: IntoEdges + Visitable,
    G::NodeId: Eq + Hash,
    F: FnMut(G::EdgeRef) -> K,
    K: Measure + Copy,
```

- Start a new algorithm from the weakest bounds and add a stronger trait only when a concrete operation requires it.
- A new representation proves every small trait contract through shared conformance tests.
- Do not abstract when the algorithm depends on representation-specific mutation, layout or asymptotic guarantees that the traits do not capture.
- Optional plugins are discovered from a small manifest or explicit registry, and one coordinator calls lifecycle hooks in an explicit order. A plugin that fails to load is reported at startup, never silently skipped. Adding a hook updates the trait and the coordinator together, with a fake-plugin test.

**One trait per language, one factory.** Each language owns its grammar, meaningful node kinds, symbol extraction and import resolution behind one trait, and the pipeline is generic over it.

```rust
pub trait Language: Send + Sync {
    fn name(&self) -> &'static str;
    fn get_ts_language(&self) -> tree_sitter::Language;
    fn get_meaningful_kinds(&self) -> Vec<&'static str>;
    fn extract_symbols(&self, node: Node, contents: &str) -> Vec<String>;
    fn extract_imports_exports(&self, node: Node, contents: &str) -> (Vec<String>, Vec<String>) {
        let _ = (node, contents);
        (Vec::new(), Vec::new())
    }
    fn resolve_import(&self, import_path: &str, source_file: &str, all_files: &[String]) -> Option<String>;
}

pub fn get_language(name: &str) -> Option<Box<dyn Language>> {
    match name {
        "rust" => Some(Box::new(Rust {})),
        "python" => Some(Box::new(Python {})),
        _ => None,
    }
}
```

- A default empty implementation silently omits data for a language that has not implemented the richer method. Split the trait into capabilities when defaults become misleading.
- Add a fixture for every non-default method that callers rely on.

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

### Architectural pattern cards

- **Sync core, async shell.** Async handlers, workers and adapters outside; synchronous domain and policy logic inside. Parse and fetch outside, decide and transform inside, then persist or emit outside. Unit-test the core; integration-test the shell. Skip the split for a tiny, purely async library.
- **Transport, domain, persistence separation.** Transport DTOs, then domain commands and values, then persistence rows and queries. Convert at the edge, enforce invariants in domain types, isolate storage specifics in adapters. Costs more conversion code; buys stronger invariants and clearer failure location.
- **Workspace layering by change boundary.** Core domain crates, adapter crates, binary or command crates, optional proc-macro or tooling crates. Split by stable responsibility and dependency direction, not by file count or chronology. Check the workspace graph and dependency direction.
- **Stable external API over composed internals.** Callers depend on a narrow contract while internal modules compose interchangeable engines or strategies chosen by the implementation. Fits parser engines, search and index systems, storage adapters, planners and performance-critical libraries. Buys optimization freedom and lower SemVer pressure.

- **Tauri split.** Frontend UI, then a typed IPC contract, then Rust core and workflows, then the capability and sidecar boundary. Use typed command modules, managed state, explicit permissions and explicit sidecar ownership. Verify with command tests, a permission review, sidecar lifecycle tests and startup and restore checks.

**Platform workarounds and platform errors.**
- A platform workaround lives in one named module as a pair of pure functions (apply and revert) with a round-trip test. Constrain what it rewrites (an exact prefix, not a pattern). A workaround that changes security semantics is not a shim; redesign instead.
- A platform-specific error variant and its `From` conversion sit under the same `cfg` as the code that produces them (`#[cfg(target_os = "windows")] #[error("webview error: {0}")] WebView(..)`). Build and test every target, or gated variants rot. Avoid gated variants when consumers need exhaustive matching as a stable protocol.

**Vendored copies of upstream code.** Copy upstream code only when its API cannot be extended (the needed type is not exposed). The module doc states which crate and version it came from, why it was copied and what was changed; licence and provenance are kept. Allow inherited lints (`#![allow(clippy::manual_strip)]`) instead of reformatting, so the diff against upstream stays small. Keep local changes minimal and track upstream fixes. Not for large or security-sensitive code.

**One state machine over two representations.** When the same logic runs over two encodings (string records and byte records), put the representation-specific access behind a small private trait, write the state machine once over a wrapper, and expose the public API as type aliases:

```rust
trait Record<'r> {
    fn next_field(&mut self) -> Result<&'r str, DeserializeError>;
    fn next_field_bytes(&mut self) -> Result<&'r [u8], DeserializeError>;
}
pub struct RecordWrap<T>(T);
pub type StringRecordDeserializer<'r> = RecordWrap<StringRecord<'r>>;
pub type ByteRecordDeserializer<'r> = RecordWrap<ByteRecord<'r>>;
```

Test each representation for invalid encoding and end-of-row errors. If the variants are simple, plain duplication is clearer.

**Shared engines, decoders and back ends.**
- A shared analysis engine is instantiated from a small per-language input trait (associated types for node, callable, location); the generic logic lives in the shared module. Implement the smallest input first.
- Policy expressed as data rows has a documented priority order and a test for enable, disable and group override.
- When decoding graph-shaped serialised data, resolve references through a cache indexed by id so a repeated reference is decoded once and shared, and return an id-only placeholder when the payload is absent. Test repeated nested references and absent payloads whenever the format changes.
- A pluggable CLI back end is one value holding its short name, description, option parser and runner (a struct with a `clap::Args` type and a run function, or a trait with those four items), so adding one is a single definition.
- A writer for a finite protocol vocabulary takes typed enums (`NodeKind`, `EdgeKind`, `Property`) and owns the conversion to the schema spelling in one `fn spelling(self) -> &'static str`. No schema string literals at call sites; a new fact updates the enum, the spelling, the call site and the schema test together, because a missing spelling silently hides facts from consumers. Provenance (corpus, root, path) travels as a token passed to the writer; emitters never bypass the writer to produce output directly.

**A fast universal source composed with a slower, better one.** When a cheap source (syntax only) and an expensive one (a semantic service) answer the same question, compose them under explicit policy: the accuracy/performance trade-offs are config fields (`prefer_semantic`, `merge_relationships`, `fallback_to_structural`, `timeout_seconds`) with named presets (`accuracy()`, `performance()`), not hidden branches. The slow source has a timeout and a fallback. Merged results need a stable identity or duplicates leak through. A behaviour change updates the tests of both presets.

**Parser work.** Keep syntax in the declarative grammar (or parser generator or combinators) and hand-write lexing only for the context-sensitive tokens (delimiter depth, look-ahead, a preceding newline), each with focused corpus tests for error recovery and delimiter variants. Highlight, locals and injection query files are a public contract shipped beside the grammar: renaming a grammar node updates the queries and the editor tests in the same change.

**Version shims and support levels.**
- To support several versions of a host framework, common code calls one narrow shim trait or module, and each host version has its own implementation selected by a cargo feature or a per-version module. Change only the affected version's shim, and add cross-version tests that assert equal behaviour where compatibility is promised. When versions barely differ, a `cfg` branch is clearer than a shim layer.
- Support is not a boolean. An accelerator, transpiler or adapter with known semantic gaps returns `enum SupportLevel { Compatible(Option<String>), Incompatible(Option<String>), Unsupported(Option<String>) }` next to the conversion function. A conversion that reports unsupported carries the reason, or users see an unexplained fallback. Write the support-level logic and its notes before wiring the conversion into planning; the notes can feed generated documentation.

**Parser recovery by source transform.** Recovery that inserts synthetic tokens and reparses is accepted only if the reparse of the transformed text is clean: no error nodes, the expected root kind, and coverage of the whole input. Every node is then remapped to original byte offsets and synthetic nodes are removed before returning. On any doubt, keep the original tree. Tests assert no errors, original byte spans, and unchanged output for unaffected inputs. Not when the transform cannot be proven byte-faithful or would mask unrelated errors.

**Optional external tooling behind a trait.** An external service that only enriches output (a language server, a symbol index) is a trait whose calls return `Result<Option<T>>` (`Ok(None)` means no data, `Err` a real failure) plus an availability probe:

```rust
#[async_trait]
pub trait SemanticClient: Send + Sync {
    async fn hover(&self, file_path: &Path, line: u32, character: u32) -> Result<Option<HoverResponse>>;
    async fn is_available(&self) -> bool;
}
```

The baseline pipeline continues when the service is absent. Tests inject a mock with exact key-based responses and assert both the enriched and the unavailable path. Surface a warning or metric when degraded, because silent degradation hides a broken setup. Not when missing data would make results wrong instead of less rich.

**Multi-language parser support.**
- Keep one table-backed registry per language: identity, grammar constructor, file extensions and aliases, dialects, query resource paths and the parent language whose queries are inherited. Callers never scatter one-off extension checks. A parser object can be shared as one `Arc<dyn LanguageParser>` registered under every alias; duplicate registrations are detected, and an unknown language is reported, not silently ignored. Adding a language updates the registry, the detection map, the query resources and the fixtures together.
- Language detection is an ordered cascade: file name and extension, then a shebang read from a small prefix buffer, then editor modelines from prefix and suffix buffers, then plain text. Each stage is tested separately, including invalid modelines. Do not read a whole file merely to detect its language.
- Extracting a symbol name across grammars is also an ordered cascade, each step encoding one known grammar shape: the common name field first (stripping a leading path qualifier), then unwrapping nested declarator nodes, then language-specific fallbacks, with a comment naming the shape each step handles. An empty name is never silently accepted: measure extraction coverage on fixtures and test every fallback branch.

**Heavy runtimes and vector indexes.**
- A heavy runtime (an ML runtime, a database engine, an SDK) is hidden behind a private state struct. Construction probes optional accelerators and falls back with a warning (GPU provider unavailable, use CPU), and returns `Result` instead of setting a "valid" flag that callers can forget to check. Tests cover the fallback, a missing model file and a bad tokenizer path.
- A vector index normalises every stored and query vector to unit length so inner product equals cosine, and rejects near-zero vectors (norm squared below about `1e-12`) instead of dividing. Use a fixed inline buffer for common dimensions and the heap above it (`SmallVec`, `ArrayVec` or a reused scratch buffer), never a stack buffer for unbounded sizes. Concurrent searches take a shared read lock and mutations the write lock. Tests: dimension mismatch, zero vectors, duplicate ids, an empty index, and a concurrent search while a write is blocked.
- To search many shard, project or tenant indexes with one query, compute the expensive query representation once above the shard loop and return an explicit error when it cannot be computed; search each shard, merge all hits, sort globally and apply the limit only after the global sort. Scores are comparable only when every shard uses the same model and normalisation. A per-shard metadata lookup failure is handled per hit, not fatal.

**Per-function syntax-tree metrics.** Define the traversal boundary first: the walk for one function stops when it meets a nested function, closure or lambda, so nested scopes are not counted into the parent, while whole-file metrics do not stop. The node kinds that count as a decision are a documented policy list, and fixtures include nested functions.

**Side effects behind a trait that carries the policy context.** Put environment-dependent side effects behind a small trait and pass the policy context alongside each operation.

```rust
#[async_trait]
pub trait ExecutorFileSystem: Send + Sync {
    async fn read_file(
        &self,
        path: &AbsolutePathBuf,
        sandbox: Option<&FileSystemSandboxContext>,
    ) -> FileSystemResult<Vec<u8>>;

    async fn write_file(
        &self,
        path: &AbsolutePathBuf,
        contents: Vec<u8>,
        sandbox: Option<&FileSystemSandboxContext>,
    ) -> FileSystemResult<()>;
}
```

- The adapter, not the caller, picks the safe backend (local, remote, sandboxed).
- Higher-level modules add no direct `std::fs` calls. They extend the trait or its adapters, so sandbox behaviour stays uniform.
- An async trait method must not hide blocking I/O.
- Skip the trait when direct `std::fs` is the whole domain and there is no policy boundary.
- When one operation runs over backends with different execution models, the common trait holds orchestration and cache contracts, and each backend decides batching, filtering and I/O. Document a default no-op for an optional optimisation, so callers do not assume it happened.

**Platform facade over private `cfg` backends.** One public API sits over OS-specific modules selected at compile time.

```rust
#[cfg(target_os = "windows")]
#[path = "windows/mod.rs"]
mod platform;
#[cfg(target_os = "macos")]
#[path = "macos/mod.rs"]
mod platform;

#[cfg(not(any(target_os = "windows", target_os = "macos")))]
compile_error!("The platform you're compiling for is not supported");

pub struct EventLoop<T: 'static> {
    pub(crate) event_loop: platform::EventLoop<T>,
    pub(crate) _marker: PhantomData<*mut ()>, // neither Send nor Sync
}
```

- An unsupported target fails at compile time, not at run time.
- Public wrapper types encode `Send` and `Sync` deliberately. An accidental auto trait is an API promise, and it can be unsound.
- Compile tests assert which public types are `Send` or `Sync`, for example with `fn needs_send<T: Send>() {}`.
- Use run-time selection instead when backends are chosen at run time.

**Indexers, extractors and analysis sessions.**

- An indexer that filters aggressively returns both the included files and the excluded roots, so a caller can explain why a file is absent. Skip lists are per mode (`enum IndexMode { Fast, Full }`), because a hardcoded list can hide real source. Tests cover the selected files and the excluded report for each mode.
- Per-language extraction dispatches with one exhaustive `match` into dedicated functions that all emit one normalised record and reuse shared helpers. An unsupported language is a silent no-op only when callers expect partial extraction.
- An adapter between an interface type and a native type checks for the native-backed wrapper first and returns the inner value without copying; otherwise it copies explicitly. Express the fast path with `fn as_native(&self) -> Option<&Native>` on the trait, not with `Any` downcasts at call sites. The doc comment states that the fast path aliases the original.
- Optional behaviours scoped to one execution are named keys declared together and carried in a context object passed down the execution path, not constructor parameters or global switches.
- An expensive batch analysis is a session object that owns its resources for a bounded lifetime and streams results to a caller-owned sink (`FnMut(Finding) -> Result<(), E>`), so the host decides rendering and failure policy. Return a plain value when results are small.
- Help text, completion candidates and defaults for plugin options are generated from the same registry and descriptors used at run time, so they cannot drift.
- Wrap a generated syntax tree in a thin newtype (`pub struct Term(generated::Program);`) that implements the platform's capability traits by delegation, so generated internals are not the public surface.
- To lower a chained source form such as `a = b = c = expr`, walk to the terminal expression while accumulating obligations (names with spans), fail with a typed error on a shape that cannot be lowered, then fold the obligations back in order. Every generated node keeps its source span.
- A developer tool that needs a persistent project list without a database makes the filesystem layout the durable ledger: one directory per project, a metadata file, known artifact names. Every metadata field is written by the writer and read by the loader. Create a project in a temporary directory and rename it into place.
- One command surface over many toolchain frontends goes through one factory that normalises the language name, checks availability in an explicit fallback order, and normalises the artifact format. Tests pin the fallback precedence.

**Hot-reload boundary.** Convert watcher or compiler output into a runtime descriptor, mark dependent objects dirty, and rebuild them lazily at the next use. Never mutate them in place from the watcher thread.

```rust
pub fn set_shader_code(&mut self, code: Vec<u32>) {
    self.shader_code = code;
    self.should_recreate = true;
}

pub fn get_pipeline(&mut self) -> anyhow::Result<&Pipeline> {
    if self.should_recreate {
        self.rebuild_pipeline()?;
    }
    self.pipeline.as_ref().context("pipeline was never built")
}
```

- A compile error is not fatal: report it and keep the last working module. A failed rebuild falls back to the previous good object.
- Throttle rebuilds. Outside a demo the watcher thread has a stop signal and is joined.

**Query operators, values and planner nodes.**

- A query-plan operator is a trait with the full lifecycle (initialise, consume, reset, clone for another plan) and uniform child traversal. A new operator implements every method before it is registered. Prefer an enum and `match` when the operator set is small and closed.
- A dynamic value that can hold borrowed, shared or owned payloads makes ownership explicit in the representation: `Cow<'a, str>`, `Arc<str>`, or an enum with an `into_owned()` step before the value outlives its source. A new variant adds construction, comparison, hashing, display and clone behaviour together.
- When a pipeline is declared before it runs, separate declaration from compilation and compile exactly once at the first consumption. Lazy construction moves errors to first use, and the API doc says so.
- Planner and AST nodes that are transformed by copying stay immutable after construction: private fields, read-only accessors, and `with_annotation(..) -> Self` building a new node. Cache no reference into the old node across a clone.
- Related grammars or dialects share one core. Each dialect extends it through a helper that rejects a name conflict, and corpus tests run for the base and for every derived grammar.

**Static analysis: matcher algebra and finding identity.** A multi-language analyser compiles language-specific AST shapes into one small algebra of explicit variants.

```rust
pub enum NodeMatcher {
    Attribute { root: String, field: String, description: String },
    Call { canonical: String, description: String },
    MethodNameRegex { regex: CompiledRegex, description: String },
    TypedAssignTarget { type_name: String, description: String },
    LiteralString { description: String, regex: Option<String> },
}

#[derive(Debug, Clone, Default)]
pub struct TaintSpec {
    pub sources: Vec<NodeMatcher>,
    pub sinks: Vec<NodeMatcher>,
    pub sanitizers: Vec<NodeMatcher>,
}
```

- New rule semantics are a new variant, at least one language engine and a parity test, never a raw string.
- A variant that a language engine does not support must not silently do nothing. A coverage test lists `(variant, language)` support and reports unsupported pairs.
- A suppression baseline or report fingerprint is a deterministic hash of normalised domain facts (rule ID, relative path, location, message) with a separator byte between fields, never an object ID or address.
- Too many fields make the fingerprint fragile; too few suppress unrelated findings. Where line numbers churn, anchor on a snippet hash or AST path. Keep a path that still recognises older fingerprints.

**Ambitious algorithm with a conservative fallback.** When a smarter algorithm sits on top of a trusted conservative one, wrap it in cheap preconditions, postconditions and a fallback path.

```rust
if is_binary(base) || is_binary(ours) || is_binary(theirs) {
    let mut stats = MergeStats::default();
    stats.used_fallback = true;
    return git_merge_file(base, ours, theirs, &mut stats);
}
if base.len() > 1_000_000 || ours.len() > 1_000_000 || theirs.len() > 1_000_000 {
    return line_level_fallback(base, ours, theirs, file_path);
}
```

- Preconditions cover binary input, a size cap and supported syntax. Postconditions catch suspicious output such as lost or duplicated content.
- Record that the fallback was used and why, and monitor it. A silent fallback masks quality problems in the smart path.
- Tests include an adversarial input that forces the fallback, and one proving the smart path leaves unchanged lines untouched.
- A conflict renderer may add parsable metadata (entity type and name, confidence, a deterministic hint) and narrow the marked region to the lines that differ. Keep a strict standard mode for downstream tools, and give every marker format a round-trip parse test.

**Version-vector claims for multi-agent coordination.** Separate ownership intent from causal history.

- A claim is an advisory lock. A per-entity version vector, one counter per agent, records causal edit history, so concurrent changes are detected (neither vector dominates) and not overwritten.
- An agent editing an entity updates the claim, heartbeat, content hash and version vector together, and appends to an operation log.
- Safety is never inferred from `claimed_by` alone. Stale-agent cleanup and conflict detection run regularly.
- A database transaction is simpler for single-writer state or hard locks.

**Parsers, lexers and grammars.**

- A large declarative specification (grammar, schema, rule set) is composed from domain-sized modules with one top-level integration point. Composition fails on a duplicate rule name; a later module never silently wins.
- Operators that share one parse shape are a data table, `const BINARY_OPS: &[(Token, Prec, Assoc)]`, driving one precedence-climbing rule. Adding an operator is a table row. A standalone rule is written only when the operator changes the child shape.
- A delimiter whose closing tag must equal its opening tag (heredocs, dollar-quoted strings, raw strings with a variable number of `#`) needs lexer state: store the opening tag when scanned, accept the end only when the same tag recurs, then clear it.
- Dynamic lexical context is a small serialisable lexer state, not grammar recursion. Release replaced state on every path, and test serialise and deserialise for incremental parsing.
- In an indentation-sensitive language, layout is parse state. Keep an indent stack (`Vec<u32>`), emit an indent when a line's indentation exceeds the top and a dedent when it is smaller, emit neither inside brackets, and delay a dedent until comments that belong to the block are consumed.
- Indentation tests cover blank lines, comment-only lines, bracketed continuations, dedents at end of input, and serialisation of the stack.
- When token shapes overlap, try the most specific alternative first and demote broad fallbacks. Add a fallback only after a corpus case proves it is needed, and cover every fallback branch with a corpus example.

**Rule engines, translators and linters.**

- A rule engine with many detectors filters rules by language once and precomputes buckets by entity kind, so each entity sees only rules that can apply.

```rust
struct RuleBuckets {
    function: Vec<FunctionRule>,
    interface: Vec<InterfaceRule>,
    type_alias: Vec<TypeAliasRule>,
}
```

- Route by matching on the entity's enum variant, not on a string-key prefix.
- A new symbol kind updates the signature type, the translator, the rule-target enum, the bucket map and one rule fixture together. With a handful of rules, plain conditionals are clearer.
- A translator from a language-specific tree to the common model is pure and deterministic: no I/O, logging or global state. Queries are compiled once per language, and the caller adds file and repository context one layer up.
- Query capture names and emitted keys are a contract. Each new query gets a fixture proving the emitted entity reaches the expected bucket. Overloads get a disambiguating counter, so same-named entities do not overwrite each other.
- A lint-rule trait has default no-op hooks, so a rule can run on raw source, on selected node kinds, or on state accumulated during traversal.

```rust
pub trait Rule {
    fn get_target_ast_nodes(&self) -> &[&str] { &[] }
    fn check_source(&mut self, _source: &str) -> Vec<LintIssue> { Vec::new() }
    fn check_node(&mut self, _node: &Node, _source: &str) -> Vec<LintIssue> { Vec::new() }
    fn finalize(&mut self, _source: &str) -> Vec<LintIssue> { Vec::new() }
}
```

- The linter walks the tree once and dispatches each node only to the rules registered for its kind, through a kind-to-rule-index map.

**Formatters and structural rewrites.**

- A formatter or codemod lets hand-maintained sections opt out. It replaces each protected region with a reversible placeholder before any opinionated pass and restores it byte-for-byte afterwards, on every path including errors.
- The placeholder is unlikely to collide with real source. Each pass states whether it runs before or after restoration.
- The syntax tree is reparsed whenever the content string changes, so no pass reads a stale tree. A validation stage checks that the output still parses and that formatting is idempotent.
- Pair every structural rewrite with a cheap multiset invariant: count entity signatures before, subtract after, require all zeros, and return the original text on failure.

```rust
let mut diff = HashMap::<TopLevelTokenSignature, i32>::new();
for signature in signatures_of(original_source)? {
    *diff.entry(signature).or_insert(0) += 1;
}
for signature in signatures_of(rewritten_source)? {
    *diff.entry(signature).or_insert(0) -= 1;
}
if diff.values().any(|count| *count != 0) {
    return Ok(original_source.to_owned()); // an entity was lost or duplicated
}
```

- Reordering uses a stable sort, carries leading comments and attributes with their declaration, and leaves unknown nodes in place.
- Do not reorder when declaration order is semantically significant and nothing verifies dependencies.

**Plans carry unsupported work as data.** A planner for migrations, rollouts or refactors returns the complete reviewable plan, with unsupported work as typed steps inside it, not an error at the first incompatible change.

```rust
#[derive(Serialize, Deserialize)]
#[serde(tag = "kind", rename_all = "snake_case")]
pub enum MigrationStep {
    AddType { name: String },
    RenameType { from: String, to: String },
    UnsupportedChange { entity: String, reason: String },
}

pub struct MigrationPlan {
    pub steps: Vec<MigrationStep>,
}

impl MigrationPlan {
    pub fn supported(&self) -> bool {
        !self.steps.iter().any(|s| matches!(s, MigrationStep::UnsupportedChange { .. }))
    }
}
```

- Derive "supported" from the steps; a stored flag can disagree with them.
- A new operation is an enum variant with a serialisation test and a human rendering before its execution is wired.
- Abort at the first unsupported change only when nothing else in the plan would be useful.

**Named layers until execution.** Keep a large computation as named layers with explicit dependencies until execution needs the flat form. A new operation adds one named layer and merges upstream dependencies through one constructor, never by flattening upstream graphs by hand.

**A capability trait in front of storage.** Handlers depend on a storage trait (`begin_upload`, `get_reader`, `finalize_upload`) held as a trait object, not on filesystem paths. Add a method only when several call sites need it. Boxed readers allocate, so skip the indirection in a hot inner loop or when there is one backend and no test double.

**A phased pipeline is data.** A compiler, indexer or ETL pipeline is an ordered table of passes, each with a name and a failure policy.

```rust
struct Pass {
    name: &'static str,
    required: bool,
    run: fn(&mut Context) -> Result<()>,
}

for pass in PASSES {
    let started = Instant::now();
    let result = (pass.run)(&mut ctx);
    tracing::info!(pass = pass.name, elapsed = ?started.elapsed(), ok = result.is_ok());
    match result {
        Err(err) if pass.required => return Err(err.context(pass.name)),
        Err(err) => tracing::warn!(pass = pass.name, error = %err, "best-effort pass failed"),
        Ok(()) => {}
    }
}
```

- Order is semantic. A new pass documents its preconditions and its position, decides whether its errors are fatal, and gets a test for cancellation after that phase.
- Use "best effort" sparingly. It hides regressions.

**Eligibility routing in a rule engine.** A linter, policy engine or API-diff classifier separates rule eligibility (declared language and target kind) from rule logic. Route each input once to its eligible rules, then run small pure checks.

- Each rule declares its eligibility narrowly and has a trigger test and a non-trigger test. Routing keys get a contract test against parser output.
- This does not fit rules that need global ordering or shared mutable state.

### Domain context packs

- **CLI and batch tools.** Path: `clap`, `tracing`, `ExitCode` for process semantics, typed config parsed at startup, `anyhow` at `main` and `thiserror` in the reusable core. Risks: ambiguous exit behavior, config parsing drift, poor diagnostics, blocking or unbounded memory on large input. Verify: command golden tests, config parse failures, exit-code tests, large-input behavior.
- **Backend services.** Path: DTO to domain conversion at the edge, typed state and services, explicit timeout and retry policy, `tracing`, pooled database access (`axum`, `tokio`, `tower`, `sqlx`). Stretch: idempotency keys, durable intent plus background processing, compile-time query checks, overload control. Risks: DTO leakage inward, hidden retries, timeout ambiguity, auth leakage, transactions coupled to remote side effects. Verify: handler integration tests, malformed input, timeout and retry behavior, transaction boundaries.
- **Libraries and SDKs.** Path: curated facade, typed errors, minimal dependency leakage, doctests for caller stories, additive features. Stretch: SemVer-aware layering, feature-matrix verification, optional zero-copy or `no_std` surfaces. Tools: `thiserror`, `proptest`, `criterion`, `cargo-semver-checks`. Risks: public dependency exposure, kitchen-sink errors, re-export sprawl, undocumented feature interactions.
- **Parsers and protocols.** Path: explicit frontier types, corpus tests, malformed-input handling, binary-safe diagnostics, round-trip property tests. Stretch: zero-copy where justified, fuzzing, typestate-assisted protocol handling. Tools: `nom` or a hand-written parser, `proptest`, `arbitrary`, `cargo-fuzz`. Risks: partial parse treated as success, UTF-8 assumptions, panic on bad input, protocol state corruption.
- **Tauri desktop.** Path: owned async commands, explicit managed state, narrow capabilities, exact sidecar scoping, typed IPC contracts. Risks: broad permissions, borrowed async inputs, hidden sidecar lifecycle, large payloads in JSON IPC, overlapping high-privilege windows. Verify: command tests, capability review, startup timeout, sidecar health checks, restore and first-paint behavior, deep-link handoff.
- **FFI and unsafe.** Path: smallest safe wrapper, explicit ownership and nullability, layout discipline, private unsafe core. Tools: `libc`, `bindgen`, `cxx`, Miri. Risks: layout mismatch, aliasing violations, panic crossing FFI, invalid lifetimes. Verify: harness tests, ABI shape review, ownership-transfer tests, Miri or sanitizers.
- **Performance work.** Path: representative benchmark cases, profile first, algorithmic wins and boundary simplification before unsafe or lock-free code. Stretch: worst-case complexity guards, cache-aware layout, allocation budgets. Tools: `criterion`, `iai-callgrind`, `cargo-bloat`, flamegraphs. Risks: optimizing the wrong metric, overfitting microbenchmarks, freezing internals into the public API.
- **When Rust is the wrong tool.** Ultra-short scripts; deadline prototypes that do not need a typed service; one-off binaries with no reusable contract; integration surfaces so dynamic that safe boundary modeling is out of proportion; cases where the dominant latency is outside the process.

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

Choose the rows at the start of the task and record which ones the change triggers; a matrix walked after implementation only justifies the evidence that already exists. The four required commands can all pass over a parser that was never fuzzed or a concurrency change whose interleavings were never explored. The performance row triggers only when a threshold was stated: no threshold means no performance test is owed and no performance claim is allowed. `loom` may be skipped for shared state behind a boundary that is proven single-threaded. In the traceability table an empty row marked as missing is better than an invented test name.

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

The seven rows are an example, not a quota. Keep the metric column to a small shared vocabulary (correctness, integration, usability, misuse, invariant, safety, latency): each word states the kind of evidence the test contributes, so the column read top to bottom is a risk profile. A matrix that is all correctness and has no safety row on code with shared state is a review flag before any code is read.

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

This skeleton shows a threshold as code and nothing more. One `Instant` reading carries scheduler noise, and `cargo test` builds in debug mode, where a latency threshold means little: run threshold tests with `--release`. Keep the single reading only when the margin dwarfs the noise, and say so. Otherwise add warm-up, repetition and percentile reporting, or a statistical benchmark such as `criterion`. State a performance claim in four parts: current value, target value, percentile and population ("from 5 ms to under 1 ms at p99 for 10k entities"). A new system with no current value still states percentile and population.

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

A `join_all` run like this is a smoke check: it sees the schedules the runtime happened to pick, not every interleaving. Where ordering of shared state matters, model it with `loom`. Keep the `loom` model to the smallest interleaving that matters. `loom` does not fit code doing external I/O, so a stress test is the legitimate fallback there: record the substitution and the reason. Keep stress-style tests for load claims, and cite the threshold each one exercises. A retry or concurrency limit stated in a requirement needs a matrix row that exercises it, under the same ID. The rewrite table promises no detached task leaks and no skeleton here tests that, so write that test yourself: assert every spawned task is joined or aborted at shutdown.

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

These skeletons freeze crate-specific shapes: `#[tokio::test]`, `trybuild`, `proptest!`, `loom::model`. Compile a copied skeleton against the project's own crate versions before building on it. If it does not compile, suspect a changed crate API before your own code.

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

- **Parser fixtures.** Keep input and expected tree together as diffable fixtures. For a behaviour change, add the smallest new fixture first, then change the parser until the expected output is intentional; a snapshot can bless a wrong tree if nobody reads it. Keep the parse structure stable and put consumer-specific meaning (highlighting, tags) in separate query files with their own tests.
- **Immutable fixture builders.** Each `with_x` returns a new value, so one case overrides one detail without contaminating the next, and each scenario runs in a fresh context that is closed afterwards.
- **Disposable real infrastructure.** For integration tests against a container, feed its runtime connection details through the same configuration path production uses.
- **Regression test for a UI or runtime bug.** Pair it with the smallest fixture app that reproduces the exact state change, and select elements by stable test ids, not styling.
- **Compile-fail tests for lifetime contracts.** When a wrapper must not outlive its parent, add a `trybuild` case that fails to compile with the expected borrow error.
- **Deterministic checks before model-based checks.** When output is generated or AI-assisted, run one named deterministic check per invariant that needs no model (required keys present, forbidden combinations absent), then the semantic check, and report both. Refresh the deterministic checks when the schema changes.
- **Suppressed failures still fail the run.** A tracker that records individual failures and continues must assert overall success or emit the final report at the end. Do not suppress where the first failure must abort.
- **A verifier beside every benchmarked kernel.** One shared driver runs each kernel with the same trial loop and timing and calls a verifier outside the timed region. A kernel without a verifier is marked unverified explicitly.

**Script DSLs and harness protocols for tests.**
- A fixture or protocol script DSL keeps, on every parsed line, the line number, the raw text and the canonical content (`struct Line { number: usize, raw: String, content: String, kind: LineKind }`), and every error carries the `Line`, so the message points at the exact script line. Directives are a typed enum. Extending the DSL adds the directive, its validation, its canonical rendering and failure tests that assert the line number.
- A harness protocol that shares a stream with log lines wraps each JSON message in explicit begin and end marker lines and a small typed envelope (`{ "name": .., "data": .. }`). Decode into a closed set of message types (a serde enum tagged by name), never by looking a type name up dynamically. Round-trip test every message and keep the frame markers stable.

**Replaying a recorded event stream on another schedule.** Wrap the unchanged iterator in a small adapter that rewrites only the schedule field (offset to a new start time, then compress by a ratio). The adapter initialises its time functions lazily from the first item, so test the empty stream, a first-item anomaly, a future offset, a past offset, no compression, and offset with compression together.

**One conformance suite for many backends.** Separate "run this backend" from "validate this algorithm".

```rust
trait PageRankBackend {
    fn run(&self, graph: &Graph, params: &Params) -> Output;
}

fn conformance_suite<B: PageRankBackend>(backend: &B) {
    for case in fixtures() {
        let got = backend.run(&case.graph, &case.params);
        assert_close(&got, &case.expected, case.tolerance);
    }
}
```

- The shared fixture owns canonical inputs, expected outputs and tolerances. Expected output is captured independently of any implementation.
- Choose the floating-point tolerance per metric: absolute, relative or mixed. Relative deviation misbehaves near an expected zero.
- Define the hook and the sample-resource tests before backend code.
- A fixture loader normalises at the parser boundary: skip blank lines and `#` comments, split with `split_whitespace`, expand undirected input into symmetric edges in one place, and report the line number and token on failure.

**Registration coverage and query templates.**

- Wiring from operation type to handler lives in one registration function. A test iterates the operation enum (`strum::IntoEnumIterator`) and asserts every operation has a handler, because compile success does not prove coverage.
- When large query text lives in template files (`include_str!`), keep three layers apart: the text, extraction of values from the domain operation, and one converter that owns quoting and escaping per placeholder kind.
- Raw substitution is open to injection. Never feed it user-controlled values; use bound parameters.
- A fixture test prepares the final query for each template and fails on any unreplaced placeholder.

**Record at the transport, replay in the production shape.** A recorded HTTP exchange is replayed as the same async shape the code consumes, so streaming (SSE, chunked) clients are tested without the network.

```rust
#[derive(Serialize, Deserialize)]
pub struct RecordedResponse {
    pub status: u16,
    pub headers: Vec<(String, String)>,
    pub body_chunks: Vec<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub body_chunks_base64: Option<Vec<String>>, // binary-safe chunks
}

impl RecordedResponse {
    pub fn into_byte_stream(self) -> BoxStream<'static, io::Result<Vec<u8>>> {
        match self.body_chunks_base64 {
            Some(chunks) => stream::iter(chunks.into_iter().map(|c| STANDARD.decode(c).map_err(io::Error::other))).boxed(),
            None => stream::iter(self.body_chunks.into_iter().map(|c| Ok(c.into_bytes()))).boxed(),
        }
    }
}
```

- Playback is the default. Recording needs an explicit mode.
- Recordings can leak secrets. Redact on record, and assert the redaction before a recording is committed.
- A plain JSON fixture is enough for a small non-streaming response.

**Scoped overrides of global state restore in reverse.** A test override of process-global configuration records the inverse of each change (insert against replace), and a guard applies the inverses in reverse order on drop. This protects the mutation, not concurrent readers; request-scoped state uses explicit dependency injection.

**Conformance scenarios have four parts.** At a specification boundary (a query language, a protocol, cross-runtime compatibility) each executable scenario states the initial state, the input, the expected result or expected error class (compile-time against runtime), and the expected side effects, including "no side effects". A semantics change updates the specification text and the scenarios together.

**Optimised and unoptimised results agree.** Every query or plan optimisation has a test that runs the same input with the optimisation on and off and compares the results.

**Assert the validity invariant, not one golden ordering.** When many outputs are equally valid (topological orders, any-order result sets), the test asserts what defines validity.

```rust
let order = graph.sort_all_nodes_topologically().unwrap();
let position = |node| order.iter().position(|&x| x == node).unwrap();
for (from, to) in edges {
    assert!(position(from) > position(to)); // every dependency precedes its dependant
}
assert!(matches!(cyclic.sort_all_nodes_topologically(), Err(TopoSortError::CycleDetected { .. })));
```

- Generate acyclic and cyclic graph families with `proptest`; fixed fixtures miss edge classes.
- Keep cases for empty, disconnected, cyclic and multiple-valid-ordering inputs, and add the minimal failing input for each regression.

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

- **Commands as data.** For a protocol with many commands, write one descriptor per command (a trait with a `const CODE`, an encoder for the input and a decoder for the response) and one generic executor. A new command is a descriptor plus serializer tests, not new transport code.
- **Variants as typed specs.** When variants differ only in names, extensions and queries, put them in one table of typed specs (a static slice of structs, or an enum with a `spec()` method) and keep the engine generic. Require a test per entry, and move a variant into code only when its control flow really differs.
- **Name the unit of an offset.** Offsets that cross a runtime boundary (Rust UTF-8 bytes against JavaScript UTF-16 code units) get the unit in the type, for example `Utf8Span` and `Utf16Span`, with a separate API per unit and tests on multi-byte text.
- **A validated resource issues its children.** A checked directory, session or connection hands out child handles only while its own state is healthy, through a method that returns `Result`. Callers do not bypass it with raw opens.
- **Keep direct and derived results apart** until the last step that needs them merged.
- **Extension points are explicit.** Register hooks by name and type; never infer one from a method that happens to match a naming pattern. Hook order is part of the API: document and test it. Give a plugin a narrowed registry facade scoped to its own namespace instead of the root mutable service, and fail loudly on a namespace violation.
- **Selection is not traversal.** A selector value (all, none, one, range, neighbours) describes a subset without the data it applies to, and a method such as `fn iter<'g>(&self, graph: &'g Graph) -> impl Iterator<Item = NodeId> + 'g` realises it. Common subsets then need no allocation.
- **Closed enum at a dynamic boundary.** When a runtime value must select typed code, use a closed enum and one central `match`. Keep generic APIs statically dispatched and offer an explicit conversion to `Arc<dyn Trait>` only at FFI, scripting or dynamic-storage boundaries; benchmark boxed iterators and trait objects before putting them in a hot path.

**Fluent builder with a deferred error.** A chaining builder can hold `error: Result<()>`; a conflicting setter records `self.error = self.error.and(Err(Error::DuplicateProtocol(name)))` and returns `self`, and `build()` starts with `self.error?`. Chaining is preserved and the first failure is reported once. The error variant names the offending call. A new setter updates the attribute struct, its `Default`, the setter and the build-time validation together. Not for cases where the caller needs feedback at the failing call.

**Omitted versus explicitly empty.** "Not provided" and "explicitly none" are different inputs: use `Option<Option<T>>` or a three-state enum (`Keep`, `Clear`, `Set(T)`), never a magic value from the domain.

**Extension traits and business actions.** An extension trait separates the required construction hooks from optional optimised methods that have default implementations; implementers satisfy the required ones first. A mutating business action is one unit that validates, then runs under one transaction, and fails with a typed error; transport handlers stay thin. Do not turn every helper into a command type.

**Strategy types that name the trade-off.** Encode an operational choice as named strategy types behind a small trait, not as a hidden boolean:

```rust
pub trait Sharding: Send + Sync + Debug + 'static {
    fn pick_shard(&self, num_shards: usize, messages: &[Message], stream: &Identifier) -> usize;
}
pub struct BalancedSharding { counter: AtomicUsize } // spreads load, does not keep order
pub struct OrderedSharding;                          // keeps per-key order, may skew load
```

Name each strategy after the guarantee it gives and document what it does not preserve. Offer no alternatives where correctness mandates one behaviour.

**Phantom-typed handles for named storage.** A const handle binds a runtime name to compile-time key and value types, and application code passes the handle, never a raw name:

```rust
pub struct TableDefinition<'a, K: Key + 'static, V: Value + 'static> {
    name: &'a str,
    _key_type: PhantomData<K>,
    _value_type: PhantomData<V>,
}
const USERS: TableDefinition<u64, &str> = TableDefinition::new("users");
```

The constructor rejects an empty name. Names created at run time still need validation. Not for user-defined schemas.

**Builders that keep current context.** A fluent builder that remembers a "current" item (current subject, current group) documents which fields each method sets or resets, resets them deliberately at boundaries, returns an error when a method needs context that is not set, and has tests for the missing-context failures. Do not share such a builder across threads.

**Queries as a typed, composable AST.** Callers compose query values with combinators instead of building strings:

```rust
pub enum Query { AllVertex, SpecificEdge(SpecificEdgeQuery), Pipe(PipeQuery), Include(IncludeQuery), Count(CountQuery) }

pub trait QueryExt: Into<Query> {
    fn outbound(self) -> ValidationResult<PipeQuery> {
        PipeQuery::new(Box::new(self.into()), EdgeDirection::Outbound)
    }
    fn include(self) -> IncludeQuery { IncludeQuery::new(Box::new(self.into())) }
}
```

Invalid compositions fail at construction with a validation error. The engine predicts the output shape (how many result sets, of what type) from the AST before running, to validate and pre-allocate. Execution is one interpreter matching exhaustively over the enum. A new variant updates the shape functions, execution, validation tests and its interaction with wrapping variants together. Not when users need an open textual query language with an optimiser.

**Typed constructor arguments instead of tuples and booleans.** When a constructor argument carries a choice that affects correctness, speed or FFI layout (row-major or column-major order, custom strides), make it a small typed builder implemented for the plain forms, so the simple call still works and the choice is visible at the call site:

```rust
pub trait ShapeBuilder {
    type Dim: Dimension;
    type Strides;
    fn into_shape_with_order(self) -> Shape<Self::Dim>;
    fn f(self) -> Shape<Self::Dim>;                       // (3, 4).f() selects column-major
    fn strides(self, strides: Self::Strides) -> StrideShape<Self::Dim>;
}
```

Test each layout separately. Not for ordinary structs where plain fields are clearer.

**Lazy plans carry `#[must_use]` and their metadata.** A value that does nothing until consumed says so (`#[must_use = "zipping producers is lazy and does nothing unless consumed"]`). A lazy traversal plan records the dimension and memory layout of its parts so it can pick the efficient execution order; all parts must have equal dimensions, checked when a part is added and before any unchecked indexed access. Prefer such a lock-step zip to hand-written index loops over several arrays.

**Normalised value objects at a security boundary.** Parse and normalise once into a named type; every policy check, wildcard expansion, loopback test and audit log then uses that type, never the raw string.

```rust
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct Host(String);

impl Host {
    pub fn parse(input: &str) -> Result<Self> {
        let normalized = normalize_host(input);
        ensure!(!normalized.is_empty(), "host is empty");
        Ok(Self(normalized))
    }
}

pub enum NetworkDecision {
    Allow,
    Deny { reason: String, source: NetworkDecisionSource },
}
```

- A deny decision carries its reason and its source.
- Keep the raw input when diagnostics or audit need it.
- Write tests first for odd inputs: bracketed IPv6, trailing dots, ports, wildcard patterns, the empty host.
- A fluent builder accumulates intent, and one `build()` converts it into a validated artifact. Tests call `build()` and never inspect private builder state.

**Joined diagnostic views state provenance.** A view that joins persisted records with live configuration or health carries an explicit marker for each joined part, so absence is not ambiguous. Prefer `enum Joined<T> { Present(T), Missing }` over a `bool` beside an `Option`, since the two can disagree. Tests cover present and missing joins.

**Unit-bearing command-line values.** Sizes such as `10MB`, durations, percentages and rates are parsed once at the command boundary into a domain type (a clap `value_parser` returning `ByteSize(u64)` or `Duration`), so downstream code never repeats unit parsing.

- The suffix policy is explicit and documented: `KB` is 10^3 and `KiB` is 2^10.
- An unknown suffix or extra tokens is an error that quotes the input. Overflow is checked.
- Tests cover a bare number, each suffix, case-insensitivity, fractional values and invalid input.

**Opaque text offsets and ranges.** Parsers, editors, diagnostics and formatters pass a named offset and range type, never a naked `usize`.

```rust
#[derive(Clone, Copy, Default, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct TextSize {
    pub(crate) raw: u32,
}

pub struct TextRange {
    start: TextSize,
    end: TextSize, // private: the constructor asserts start <= end
}
```

- The name says the unit: bytes, not chars or UTF-16 units. Convert at the boundary.
- A `u32` caps a file at 4 GiB, so conversion from `usize` stays fallible through `TryFrom`.

**Capability arguments for dangerous operations.** Process execution, network access, filesystem roots and temporary files require an explicit capability argument in the function signature.

```rust
pub struct ExecCap(()); // private constructor: created only in main or one trusted module

pub fn run_tool(cap: &ExecCap, program: &Path, args: &[OsString]) -> io::Result<Output> {
    let _ = cap;
    std::process::Command::new(program).args(args).output()
}
```

- Back the token with a repository lint that forbids the raw API outside the wrapper module: `disallowed_methods` and `disallowed_types` in `clippy.toml`, for example for `std::process::Command::new` and `std::env::set_var`. Without the lint the token is only social discipline.
- Generated code near process execution goes through the wrapper, never the raw call.

**Parsed names for user-facing filters.** When a filter must address rich entities (impl blocks, generics, lifetimes, wildcards) that plain strings cannot, model the name as a parsed AST such as `enum PatternElem { Ident(String, GenericArgs), Impl(Expr), Wild }`.

- The parse error carries the position and the input.
- A DSL is a long-term promise about syntax and error text. New syntax updates the AST, parser, printer and round-trip tests (`parse(print(x)) == x`) together.
- Prefer existing paths or structured selectors when they suffice.
- A deep deserialisation failure reads as a path from root to leaf: use `serde_path_to_error` or per-field context, and bound the size of any fragment quoted in the message.

**Build-orchestration builder.** An API with many optional flags is a fluent, serialisable builder with one `build()` boundary.

```rust
pub fn capability(mut self, capability: Capability) -> Self {
    self.capabilities.push(capability);
    self
}

// One explicit lowering function turns options into tool flags.
target_features.extend(builder.capabilities.iter().map(|cap| format!("+{cap:?}")));
target_features.extend(builder.extensions.iter().map(|ext| format!("+ext:{ext}")));
```

- Required inputs go in `new()`; options go in consuming setters.
- `build()` rejects incompatible combinations with a clear error, since fluent setters hide them.
- A new option adds the field, the setter, CLI and serde metadata, the lowering, and an incompatibility test.
- Use typestate when options need compile-time sequencing.

**Scalar-or-array argument.** Represent broadcastability as a small trait capability, instead of duplicating every entry point or materialising a repeated constant array.

```rust
pub trait Datum {
    /// Returns the value and whether it is a scalar.
    fn get(&self) -> (&dyn Array, bool);
}

impl<T: Array> Datum for T {
    fn get(&self) -> (&dyn Array, bool) {
        (self, false)
    }
}

#[derive(Debug, Copy, Clone)]
pub struct Scalar<T: Array>(T);

impl<T: Array> Datum for Scalar<T> {
    fn get(&self) -> (&dyn Array, bool) {
        (&self.0, true)
    }
}
```

- The implementor interprets the scalar flag and the scalar's null state correctly.
- Write array-array, array-scalar and scalar-scalar tests, with nulls, before optimising the inner loop.
- Keep separate functions when scalar and vector operations differ in semantics.
- A checked constructor's error quotes both sides of a mismatch, such as the column count and the field count.

**Absent behaviour as an implementation.** Model "no hook installed" as a no-op implementation rather than as `Option<Hook>` branches at every call site.

```rust
pub trait RegistryHooks: Send + Sync {
    fn on_manifest_uploaded(&self, _reference: &ManifestReference) {}
}

impl RegistryHooks for () {}

let hooks: Box<dyn RegistryHooks> = builder.hooks.take().unwrap_or_else(|| Box::new(()));
```

- Document where each hook is invoked and whether its failure is ignored. A silent no-op can hide missing wiring, so the wiring has a test.
- This does not fit a hook that must be confirmed, retried or rolled back inside the core transaction.
- An extension API with many optional lifecycle callbacks is a builder that holds one boxed closure per hook, each with a no-op default, so an author composes only the hooks needed. With one required callback a trait implementation is clearer. Closure fields obscure ordering and error propagation: document the lifecycle order and which hook errors abort. Adding a hook means a no-op default, a builder method and an example.

**Backend families through associated types.** Put platform variation behind associated types that are constrained back to `Self`, so the handles, dispatchers and events of one backend cannot be mixed with another's.

```rust
pub trait Runtime: Sized + 'static {
    type Handle: RuntimeHandle<Runtime = Self>;
    type WindowDispatcher: WindowDispatch<Runtime = Self>;

    fn new(args: RuntimeInitArgs) -> Result<Self>;
    fn handle(&self) -> Self::Handle;
}
```

- Extending the trait updates the trait, the mock backend and every platform backend in the same change.
- An API heavy in associated types needs an example of the common path. A product with one backend does not need the trait.

**Extract and repack.** An API that accepts heterogeneous nested containers, where only some leaves need processing, splits the traversal into an extract phase and a repack phase so the caller gets its own shape back. Offer an opt-out of traversal for huge plain containers, and test structs, tuples and maps as well as lists.

**Behavioural traits need semantic tests.** Independent type families interoperate through one behavioural trait consumed by generic operations. Conformance does not prove the methods agree with each other, so tests check the related methods together (for example shape, keys and identity-hash stability).

**A syntax node travels with its source.** When every node operation needs the original text, wrap the borrowed node with the source slice and pass the wrapper through traversal APIs instead of the raw node.

```rust
#[derive(Clone)]
pub struct NodeWithSource<'a> {
    pub node: Node<'a>,
    pub source: &'a str,
}

impl<'a> NodeWithSource<'a> {
    pub fn child_by_field_id(&self, field_id: u16) -> Option<Self> {
        self.node.child_by_field_id(field_id).map(|child| Self { node: child, source: self.source })
    }

    pub fn text(&self) -> Result<&'a str, Utf8Error> {
        self.node.utf8_text(self.source.as_bytes())
    }
}
```

- Children are derived with the same source reference, so a node and its text cannot drift apart.
- If equality compares the source by pointer, a cloned string is a different source. Test that identity model.
- This is unnecessary when the syntax tree owns its text.

**Coordinates in every unit the boundary needs.** Parsers, editors and wire protocols disagree on byte, character, UTF-16 and line/column coordinates.

```rust
#[derive(Clone, Copy, Default)]
pub struct Offset {
    pub utf8: usize,
    pub utf16: usize,
    pub grapheme: usize,
}
```

- Give each coordinate system its own type, and carry both the human-facing and the byte-facing form across a boundary.
- Every conversion is an explicit function that takes the source text. Rewrite logic never does range arithmetic by hand.
- Advance all units in one pass over the line so they cannot drift, and cache a per-line offset table when conversion is hot.
- Test ASCII, non-ASCII in the basic plane, astral emoji and combining marks.

**Parse fragments under a set of contexts.** A codemod, linter or query engine that accepts code fragments wraps the fragment in each language-defined (prefix, postfix) context, parses, and keeps the trees whose root has no error and no missing node.

- Record the wrapper offsets with each tree, so the fragment's own range can be recovered.
- Report which context parsed. Too many contexts give ambiguous matches.
- A new language defines its fragment contexts and its invalid-root filter before any rewrite rule. Do not wrap where the wrapper would change the meaning.
- Nested lexical modes (interpolation, directive, quoted template, heredoc) are a stack of contexts. Create, serialise, deserialise and destroy change together, with corpus cases for nested interpolation and heredoc boundaries.

**Cross-cutting policy as a decorator.** Throttling, retry, metrics and caching wrap a service by implementing the same trait around the inner trait object. They are applied once in the factory, never as `sleep` or `acquire` calls inside each backend.

```rust
pub struct RateLimitedCompletion {
    completion: Box<dyn CompletionStream>,
    rate_limiter: RateLimiter,
}

#[async_trait]
impl CompletionStream for RateLimitedCompletion {
    async fn generate(&self, prompt: &str, options: CompletionOptions) -> BoxStream<'_, String> {
        self.rate_limiter.acquire(1).await;
        self.completion.generate(prompt, options).await
    }
}
```

- Converting a per-minute limit into per-second refills changes burst behaviour against the vendor's window. One request counter cannot express token-based or per-endpoint quotas.
- Backend selection and capability aliases live in the same factory, which builds the trait object and applies the shared wrappers. Adding a backend updates dispatch, request shaping, capability flags and wrapping in one change.
- A backend kind that comes from user configuration is parsed into an enum at config load and an unknown kind is a typed configuration error, never a `panic!` in the factory.

**Decoding policy wraps the raw stream.** Keep a provider's raw chunk stream separate from product-level decoding (stop conditions, trimming), which sits in a wrapper layer.

```rust
let mut text = String::new();
let mut stop = stop_condition_factory.create(prompt, language); // stateful, one per request
while let Some(chunk) = chunks.next().await {
    let (should_stop, stop_len) = stop.should_stop(&chunk);
    text.push_str(&chunk);
    if should_stop {
        text.truncate(text.len().saturating_sub(stop_len));
        break;
    }
}
```

- A stop sequence can span chunk boundaries, so the condition keeps state across chunks and reports how many trailing bytes to trim.
- The truncation point must be a character boundary.
- Tests split a stop marker across chunks and check that no valid text is cut and no marker leaks.

**Deferred passes and ancestor-scoped state in tree rewriting.** A tree transformation that discovers a whole-file follow-up (reformat, fix imports) registers a deferred pass that runs once after the traversal. It does not revisit the root from inside a node visit.

- Deferred passes are coarse and bounded, and their ordering is tested in combination.
- State that belongs to the ancestor path (the nearest enclosing declaration, pending imports) lives in a scoped context stack with nearest-ancestor lookup, separate from the immutable tree. Its keys are typed, not ad hoc strings.

**Many IDs over one primitive.** When dozens of IDs share one representation, encode the namespace in a const-generic parameter of one transparent wrapper and declare every alias from one registry macro.

```rust
#[derive(Clone, Copy, Default, Hash, PartialOrd, PartialEq, Eq, Ord)]
#[repr(transparent)]
pub struct TypedId<const N: usize, P>(pub(crate) P);

pub trait UniqueTypedIdDeclaration {}

macro_rules! declare_id_type {
    ($name:ident, $primitive:ty, $type_id:expr) => {
        pub type $name = TypedId<{ $type_id }, $primitive>;
        impl UniqueTypedIdDeclaration for $name {}
    };
}

declare_id_type!(TableId, u32, 1);
declare_id_type!(JobId, u32, 2);
```

- Trait implementations (serde, database conversion, `Display`) are written once for the generic wrapper, and the IDs still cannot be mixed.
- The marker trait makes a reused type number a compile error, because the two implementations conflict.
- A few IDs with invariants of their own stay hand-written newtypes.

**Withhold a lossy conversion.** When a `From` implementation would let `?` silently drop required context, do not implement it. Provide named constructors that attach the context.

```rust
#[derive(thiserror::Error, Debug)]
pub enum RpcError {
    #[error(transparent)]
    GrpcStatus(Box<StatusWithService>), // boxed: keeps the enum small
    #[error(transparent)]
    Internal(#[from] anyhow::Error),
}

// No `impl From<tonic::Status> for RpcError`: the status must say which service produced it.
impl RpcError {
    pub fn from_meta_status(status: tonic::Status) -> Self {
        RpcError::GrpcStatus(Box::new(StatusWithService::new(status, "meta")))
    }
}
```

- On stable Rust, omit the implementation and say why in a comment. Negative implementations are nightly-only.
- Mark builders, guards and status-like return types of your own `#[must_use]`. Never write `let _ =` on a `Result` without a comment that says why.

**One exhaustive serialiser for an export format.** Writing typed runtime values back into a replayable text format (a dump or export) puts every escape rule behind one exhaustive `match`: identifier quoting, string escaping, numeric precision, temporal constructors.

- No formatting is scattered across export paths, and the match has no wildcard arm, so a new value type fails to compile until its arm exists.
- A new stored value type adds its arm and an export-then-import round-trip test in the same change.

**Shared scaffolding in a provided method.** Cross-cutting execution scaffolding (progress tracker, task naming, job ID, concurrency wiring) is built once in a provided trait method, which then calls a minimal required method with the ready tracker. Implementers write only the required method. A change to the default affects every implementation, so keep it conservative. Result accounting (timings, counts, configuration echo) wraps the side effect in one shared consumer in the same way, and the write is skipped for empty input.

**Commands declare their response shape and their consistency check.**

- When one endpoint can return several projections, the command value carries its response shape as an enum beside the statement and parameters, so serialisation, execution and decoding share one contract. Each command kind has a fixture that asserts both body and shape.
- An optional consistency check, such as optimistic locking by expected version or row count, is an explicit value on the request (`Option<OptimisticLock>`), not a hidden executor side channel. The checker errors when asked to check a request without one. On a mismatch the stale tracked entity is evicted before the conflict error is returned. Test "absent" and "mismatch evicts".

**Plan nodes expose scan and lookup.** A query-plan node offers both execution modes, producing candidates and answering "contains?", each with a cost estimate. An intersection picks the cheapest producer and orders the remaining membership checks by cost. Plan shape stays separate from execution mode.

**Dynamic namespaces only at the edge.** A large, versioned remote API whose endpoints are not all known when the client ships may use a dynamic namespace builder (`client.namespace("a").namespace("b").call(params)`), with ordered parameters (`IndexMap` or a vector of pairs) and execution behind one small query-runner trait. Misspellings then fail only at execution, so return suggestions from the server's listing. Prefer typed methods wherever a typo must fail at compile time.

**Reusable algorithm objects: state, driver and lifecycle.**

- An iterative algorithm splits its state (parameters, result buffers, working data, with `init()` and `reset()`) from its driver (prepare, loop, convergence check). Stale state is reset before each run, and a test runs the same instance twice.
- Reusable data-parallel skeletons (advance, filter) live in operators. Algorithm-specific per-item logic is passed as small closures bounded `Fn + Send + Sync` with explicit captures. Test with each optional stage on and off, because a filter silently changes the working set.
- Make premature access to results unrepresentable: `run(self) -> Finished` or a `run()` that returns the result. Where a `has_run` flag is unavoidable, as in bindings, set it false at the start and true only after complete results exist, never on the error path, and have every getter check it and return an error.

**Dynamic named side data with typed handles.** Per-node or per-edge attributes chosen at run time are a name registry of type-erased storages with typed handles at the read and write boundary.

- Attaching rejects a duplicate name. `get::<T>` checks the stored `TypeId` and returns a typed error on mismatch.
- Handles are invalidated on detach and check element validity on access. Test detach, type mismatch and missing element.
- A fixed attribute set is plain fields.

**Normalise messy input forms once.** User-facing index, slice or mask syntax is resolved once into a small typed value that carries both the display meaning and the low-level call arguments. The accepted forms and the guiding error messages are public API, with a test per accepted input type.

**Operator overloading builds a lazy, checked expression.** `std::ops` implementations for a DSL build a thin lazy expression value and reject ambiguity at construction: operand type checks, and no mixing of operators whose Rust precedence would mislead. Prefer explicit methods where an overloaded operator would surprise.

**Typed registration, dense dispatch.** Keep registration ergonomic (typed, by operation type) and build the optimised dispatch form once at start-up: a dense `Vec` or array indexed by a compact, stable type code.

- Before the hot loop starts, check that every advertised operation code has a handler and that every code is in range.
- Sparse, untrusted or runtime-changing codes use a map.

**Algorithms against the minimal traversal contract.** Write an algorithm once against the smallest trait it needs (node count, node iterator, degree, neighbours), and have each container implement that trait, instead of hard-coding one representation. Identify the required methods first, and run the algorithm against at least two implementing types in tests.

**One gate owns timing policy.** A workload driver's timing sits behind one gate that answers "may execute": wait for dependency checks, then for the scheduled start, using an injectable time source and a sleep interval that explicitly trades CPU for timing accuracy.

- Callers never duplicate schedule checks.
- Tests keep an "ignore schedule" and a "respect schedule" mode and use a fake time source for check failure, scheduled delay and zero sleep.
- This does not fit a low-latency loop. Add cancellation where a wait must be interruptible.

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

- **Native and WASM bounds behind local aliases.** For a library that runs on both, hide target-specific bounds behind a few named traits defined once per target (`Spawnable`, `Stream`, `SpawnableOutput`, `TransportStream`: with `Send` on native, without it on wasm). Code uses the aliases, never a direct `Send` bound, and both targets are built before a bound changes.
- **One wrapper around the HTTP request builder.** Wrap the client's builder once so hooks, guards (for example a keep-awake guard held for the duration of the call) and target-specific execution apply to every request. Call sites never reach the underlying builder.
- **External tools with the same lifecycle.** One trait (minimum version, can auto-install, install, update, instructions) with an implementation per tool and a shared command runner that logs each step. Run a version check after an automatic update, and remember that logged transcripts can carry values from the environment.

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

**Seal traits that prove a representation.** A trait that promises layout, serialization format, zero-copy casting, FFI or protocol safety must not be implementable downstream:

```rust
mod private { pub trait Sealed {} }
pub trait NativeType: Copy + Send + Sync + Default + private::Sealed + 'static { /* .. */ }
impl private::Sealed for u32 {}
impl NativeType for u32 {}
```

Say in the docs that the trait is sealed. Do not seal a trait that is a real extension point for other crates.

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

**Macro-declared pass registry.** One registry line per pass yields a `Copy`, serialisable enum (usable in configuration and pass lists) and the dispatch match:

```rust
pub trait Phase {
    fn apply(&self, items: &mut Vec<Item>);
}

macro_rules! declare_phase_kind {
    {$($name:ident = $phase:expr),*$(,)?} => {
        #[derive(Clone, Debug, Copy, serde::Serialize, serde::Deserialize)]
        pub enum PhaseKind { $($name,)* }

        impl Phase for PhaseKind {
            fn apply(&self, items: &mut Vec<Item>) {
                match *self { $(Self::$name => $phase.apply(items),)* }
            }
        }
    }
}
```

Adding a pass means implementing the trait, adding it to the macro and checking that it appears in the relevant pass list. Stateful passes that cannot be a `Copy` variant need a different registry shape.

**A back end is preparation passes plus a printer under one narrow trait.**

```rust
pub trait Backend {
    type Printer: Printer;
    const NAME: &'static str = Self::Printer::NAME;
    fn phases(&self) -> Vec<PhaseKind> { vec![] }
    fn modules_to_files(&self, modules: Vec<Module>, printer: Self::Printer) -> Vec<File> { /* shared flow */ }
    fn module_path(&self, module: &Module) -> Utf8PathBuf; // the one thing every target must supply
}
```

Use an associated type, an associated const defaulted from it, default methods for the shared flow and one required method for what differs. Target preparation stays separate from target rendering, and printer-specific escaping stays in the printer. Shared passes can leak one target's assumptions, so review each back end's pass list independently. Not when targets have unrelated pipelines.

**Parser settings derived from capabilities, and a guarded recursion budget.** Permissions and feature gates become parser settings (syntax flags and recursion limits) before parsing, through one derive function, not checks after the tree is built:

```rust
pub fn settings_from_capabilities(cap: &Capabilities) -> ParserSettings {
    ParserSettings {
        files_enabled: cap.allows_experimental(&ExperimentalTarget::Files),
        ..Default::default()
    }
}
```

The entry point rejects input larger than the offset type can address (`ensure!(input.len() <= u32::MAX as usize, Error::QueryTooLarge)`) and renders errors against the input. The same text can be valid in one context and invalid in another, so the diagnostic names the disabled capability.

A recursive parser spends a depth budget through a guard so every exit path, including `?`, restores it:

```rust
if self.settings.object_recursion_limit == 0 {
    return Err(SyntaxError::new("Exceeded query recursion depth limit").with_span(span));
}
self.settings.object_recursion_limit -= 1;
struct Dropper<'a, 'b>(&'a mut Parser<'b>);
impl Drop for Dropper<'_, '_> {
    fn drop(&mut self) { self.0.settings.object_recursion_limit += 1; }
}
```

Wrap each recursive branch in the one guard; never hand-edit the counter. Test the depth-limit error and that the budget is restored after an error.

**Generated bindings driven by typed specs, written atomically.** Describe what to generate as a typed spec list, with small macros so the list reads declaratively, and never edit generated files by hand:

```rust
pub enum ItemWrapperSpec {
    Constructor { signature: Option<String>, suffix: Option<String> },
    Method { name: String, signature: Option<String>, suffix: Option<String> },
    FieldGetterSetter { field_name: String },
}

fn save_file_atomic(content: &str, temp_dir: &Path, file_path: &Path) -> Result<()> {
    let mut file = tempfile::NamedTempFile::new_in(temp_dir)?;
    file.write_all(content.as_bytes())?;
    file.into_temp_path().persist(file_path)?;
    Ok(())
}
```

Create the temporary file in a directory on the same filesystem as the target so `persist` is an atomic rename. Generation is idempotent. A new wrapped item is a spec-list entry plus generator tests. Validate signatures at generation time, or the error surfaces at run time in the foreign call.

**One inventory macro for a variant matrix.** When the same matrix (variant, property type, split type) drives several generated sites, keep one inventory macro that takes a callback macro, and expand every site from it.

```rust
macro_rules! for_all_classified_sources {
    ($macro:path $(, $extra_args:tt)*) => {
        $macro! {
            { { Mysql }, { Postgres } },
            {
                { Kafka, $crate::source::kafka::KafkaProperties, $crate::source::kafka::KafkaSplit },
                { Pulsar, $crate::source::pulsar::PulsarProperties, $crate::source::pulsar::PulsarSplit }
            }
            $(, $extra_args)*
        }
    };
}
```

- Adding a variant edits only the inventory, and the compiler then checks the enum, string matching, dispatch and registration sites.
- Write no one-off match arm elsewhere.
- Macros obscure generated code and error messages. Use plain enums and matches when the set is small.

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

- **Interning for immutable, highly repeated values.** A canonical `Arc` per distinct value turns equality into a pointer comparison:

```rust
pub struct Interned<T: Internable + ?Sized> { arc: Arc<T> }

// lookup by precomputed hash in a sharded map; Occupied clones the Arc, Vacant inserts it
impl<T: Internable + ?Sized> PartialEq for Interned<T> {
    fn eq(&self, other: &Self) -> bool { Arc::ptr_eq(&self.arc, &other.arc) }
}

impl<T: Internable + ?Sized> Drop for Interned<T> {
    fn drop(&mut self) {
        if Arc::strong_count(&self.arc) == 2 { self.drop_slow(); }   // only the map and this handle remain
    }
}
```

  Pointer equality is correct only because every constructor goes through the interner. Use it for compiler types, paths and terms, not for mutable or low-cardinality values. For plain strings, a map from `Arc<str>` with a read lock on the hit path is enough; re-check under the write lock on a miss when one canonical `Arc` is required.
- **Deduplicating live resources.** Key by canonical identity (absolute path, case-folded on case-insensitive platforms) and hold `Weak` references so the registry does not keep the resource alive; remove the entry when `upgrade()` fails, and reject a second open whose options conflict with the first.
- **Move-only handle with ownership states.** When an entry may be cached, owned, borrowed or transferred, use one handle with an enum of states and a single release path in `Drop`. Adding a state means updating every transition.
- **Stateful result handles.** A pending or resumable handle checks "still executable" in every public method that advances it, not only at construction, and a stale handle returns a clear error.
- **Bootstrap builders.** Provide "copy an existing dependency set" separately from "override one", so tests and embedders do not restate everything. Adding a dependency touches the copy path, the setter and the accessor together.
- **Snapshots as iterators.** Turn an engine's point-in-time file set into a closeable iterator at the boundary, so callers never manage commit handles; an empty store yields an empty iterator, not an error.

**Index-handle interning.** A variant of interning hands out a `u32` index into a global table instead of a pointer: equality and hashing are O(1) on the integer, and the handle is `Copy`, small and easy to serialise. Caveats for index-handle interning: never hand out `&'static T` into a `Vec<T>` that can grow, because growth moves the items; box or leak each item, use an append-only arena with stable addresses, or return a clone or an `Arc`. Any `unsafe` lifetime extension states its invariant (entries are never removed or moved) at the block. The table never shrinks, so do not intern unbounded or attacker-controlled values.

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

**Parallel validity channel for columnar data.** When positions must stay aligned (columnar or vectorised data), keep values and validity in two parallel buffers: `append_value` pushes the value and a "present" bit, `append_null` pushes an "absent" bit and still advances the value buffer by one slot, so both always have the same length. Test append-value, append-null, append-slice, the finished length and the null count. For small collections `Vec<Option<T>>` is simpler.

**Edit-heavy, then read-heavy structures.** Mutations append to a pending buffer, and an explicit, named consolidation step (`update()` or `finish()`) sorts, deduplicates, applies removals and recomputes totals before read-optimised algorithms run. Reads before consolidation may see stale counts, so make that a type-state (`Builder` into `Frozen`) or a checked error, not a convention. Not when every mutation must be visible immediately.

**Compressed sparse row (CSR) layout.** For a static or mostly static graph, store `offsets: Vec<usize>` of length `vertices + 1` and packed `edge_targets` and `edge_values` arrays; the neighbours of `u` are `edge_targets[offsets[u]..offsets[u + 1]]`. Contiguous arrays give cache-friendly scans and easy parallel partitioning. At construction assert `offsets.len() == vertices + 1`, that offsets are non-decreasing, and that the last offset equals `edge_targets.len()`. Rebuild for major updates instead of inserting in place.

**Total-order priority wrapper for `BinaryHeap`.** Wrap the priority key in a type with an explicit `Ord` to turn the standard max-heap into a min-heap and to give partially ordered keys a deterministic order.

```rust
pub struct MinScored<K, T>(pub K, pub T);

impl<K: PartialOrd, T> Ord for MinScored<K, T> {
    fn cmp(&self, other: &Self) -> Ordering {
        let a = &self.0;
        let b = &other.0;
        if a < b {
            Ordering::Greater
        } else if a > b {
            Ordering::Less
        } else if a.ne(a) {
            Ordering::Less // NaN: a policy choice
        } else {
            Ordering::Equal
        }
    }
}
```

- `PartialOrd`, `PartialEq` and `Eq` are implemented consistently with it.
- Where NaN sorts is a policy choice that can mask a bad cost calculation. Reject NaN at the boundary when it should be an error, or use `f64::total_cmp`.
- Tests cover equal scores, reversed ordering and NaN.
- `std::cmp::Reverse` is enough when the key is already `Ord`.

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

- **Retryability lives on the error type.** Classify with a trait, not by matching message strings, and inject the sleep so tests never wait on a real clock:

```rust
pub trait Retryable {
    fn is_retryable(&self) -> bool { false }   // permanent unless a variant opts in
}

pub enum Retry<E> { Permanent(E), Transient(E) }

#[async_trait::async_trait]
pub trait MockableSleep {
    async fn sleep(&self, duration: Duration);
}

pub async fn retry_with_mockable_sleep<T, E, Fut>(
    params: &RetryParams,
    op: impl Fn() -> Fut,
    sleep: impl MockableSleep,
) -> Result<T, E>
where
    E: Retryable + std::fmt::Debug + 'static,
    Fut: Future<Output = Result<T, E>>,
{ /* loop: run op, return on Ok or a non-retryable error, else back off through sleep */ }
```

  A wrong `is_retryable` creates a retry storm, so every new error enum gets explicit transient and permanent tests plus a no-sleep test path. Never wrap a non-idempotent operation.
- **One retry state at the operation boundary.** For a managed transaction or work closure, keep max total retry time, injected sleep, backoff and the dead-connection limit in one state object that loops while it may continue and produces the final error itself. Call sites do not retry. Say in the API docs that the closure may run more than once, honour cancellation and deadlines inside the loop, and test cancellation, the time limit, error classification and commit failure.
- **Retries for streams.** Use the same classification for value-returning and streaming calls: retry 429, 500, 502, 503 and 504, never 400, 401, 403, 404 or 422; bound attempts and total time; add jitter; honour `Retry-After`. Retrying a stream restarts it from the beginning, so the caller must tolerate repeated partial output or pass on only committed chunks.
- **Actionable startup and configuration diagnostics.** Match the known typed cause, then print a description plus one concrete action in the user's terms, with the original error still attached. Analyse only failure types you know, so the real cause is not replaced by a guess.
- **User-facing diagnostics are a boundary format.** Route every interpolated value, identifier and type name through shared quoting and escaping helpers, so error constructors carry facts and the helpers own the presentation. Changing a helper changes many snapshot tests at once; review that diff.
- **Rate-limited logging.** For a log line on a hot failure path, keep the state per call site (a `static AtomicU64` count and last-reset time inside the macro), check it, then call `tracing`; no allocation and no shared map. Pair it with a counter metric, because suppressed lines hide how often the failure happens. Never rate-limit security or audit events.

**One ensure/bail pair, with a debug switch.** A library with many invariant checks uses one pair of macros that build the typed error:

```rust
macro_rules! ensure {
    ($cond:expr, $($tt:tt)+) => { if !$cond { bail!($($tt)+); } };
}
```

A process-wide strategy read once (`static STRATEGY: LazyLock<ErrorStrategy>`, from an environment variable) can turn errors into panics or attach backtraces while debugging, with normal typed errors as the default. Use the project's existing macros; add a new error helper only when repeated call sites justify it, because macros hide control flow.

**Errors that cross a process or language boundary are versioned data.**

```rust
#[derive(Clone, Debug, Error, EnumDiscriminants, IntoStaticStr, FromRepr)]
#[repr(u32)]
#[strum(serialize_all = "snake_case")]
pub enum WireError {
    #[error("Error")] Error = 1,
    #[error("Invalid configuration")] InvalidConfiguration = 2,
    #[error("Resource with key: {0} was not found.")] ResourceNotFound(String) = 20,
}
```

Give every variant an explicit discriminant, never renumber or reuse one, decode with `from_repr`, and use the stable snake_case name in telemetry. Not for internal errors that change often.

**Scoped panic context.** A thread-local stack of frames, printed by a panic hook installed once, tells you what the thread was doing when it panicked:

```rust
pub fn enter(frame: String) -> PanicContext {
    SET_HOOK.call_once(set_hook);
    with_ctx(|ctx| ctx.push(frame));
    PanicContext { _priv: () }
}
impl Drop for PanicContext {
    fn drop(&mut self) { with_ctx(|ctx| assert!(ctx.pop().is_some())); }
}
let _ctx = panic_context::enter(format!("request: {method}")); // `let _ =` would drop it at once
```

It is diagnostic only, not error handling, and because it is thread-local it does not follow an async task across threads.

**Retry as a decorator over a trait implementation.** Wrap a whole backend in a type that implements the same trait (`struct RetryWrites<B>(RetryPolicy, B)`), with reads and writes wrapped separately and pass-through methods documented. Retry writes only when submission and polling tolerate duplicates.

**One retry policy for every entry point.** A single policy (retry predicate, initial delay, multiplier, jitter factor, maximum total retry time) is shared by every API style the client exposes (blocking, async, stream), so the rules cannot drift. Bound retries by total elapsed time, not only by attempt count. The delay with jitter is uniform in `[delay - delay * jitter, delay + delay * jitter]`, then `delay *= multiplier`. The final error carries the earlier attempts' errors so logs keep them. A change to the rules updates all entry points and tests the deadline, the jitter bounds and the preserved earlier errors.

**Circuit breaker with three outcomes.** States are closed, open and half-open. While open, calls are rejected until the cooldown has passed; then exactly one probe is admitted and a second caller is rejected with a retry-after. Every admitted call is followed by exactly one of success, failure or neutral. Caller cancellation, caller timeouts and terminal client errors are neutral: they release the probe permit without changing health. An admission without a matching record wedges the breaker, so do the classification in one wrapper (ideally a guard whose `Drop` records neutral) and never let call sites touch breaker state. Release the state lock before awaiting the wrapped call, distinguish "rejected while open" from the upstream error in the returned error type, and inject the clock for tests. Use it for flaky remote dependencies, not cheap local operations.

**Extension-facing error shim.** A plugin-facing trait returns a small public error type. A newtype shim with `impl From<InternalError>` maps the cases an extension can act on (a timeout with its duration) to typed variants and everything else to an opaque `Other(message, Box<dyn Any>)` holding the original internal value, so privileged host code can downcast it back while extensions see a stable surface. Both the immediate call error and the error from an awaited callback go through the same shim. Document the downcast escape hatch. Not when callers need the full internal error type as a public contract.

**Diagnostic context combinators.** In CLI, compiler, linter and language-server code, context attachment is built into the error type, so a call site enriches a failure instead of replacing it.

```rust
pub trait DiagnosticExt: internal::Sealed + Sized {
    fn context<M>(self, message: M) -> Error
    where
        Self: 'static,
        M: fmt::Display + 'static,
        Error: From<internal::ContextDiagnostic<M, Self>>;

    fn with_category(self, category: &'static Category) -> Error;
    fn with_file_path(self, path: impl AsResource) -> Error;
    fn with_file_span(self, span: impl AsSpan) -> Error;
    fn with_severity(self, severity: Severity) -> Error;
}
```

- Each combinator wraps the original diagnostic in a typed layer and keeps the source.
- At each `?` in diagnostic-heavy code, decide whether this boundary should add a path, span, category or severity.
- Chained contexts get noisy. The rendered diagnostic keeps one clear primary message.
- A simple internal error enum whose context is never shown does not need this.

**Absent, unsupported and failed are different outcomes.** An optional-acceleration or conversion registry returns which of them happened, and the fallback is explicit.

```rust
pub enum Conversion<T> {
    Converted(T),
    NoConverter,
    Unsupported(Reason),
    Failed(Error),
}
```

- Collapsing the last three into `None` hides bugs. Logs and metrics keep the reason.
- Each converter has tests for the happy path, the unsupported input, duplicate registration and the failure fallback.
- Never swallow the failure of a mandatory transformation.

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

**Public status codes are one taxonomy.** Each public code carries a classification (client error, transient, server error) and a description that tells the client what to do (fix the request, retry later). Retry decisions are read from the classification, not from the message: `enum Status` with `fn class(&self) -> Class` and `fn description(&self) -> &'static str`. A new error goes in the narrowest category. Once public, a name is a compatibility commitment.

**Retry bounds and retry tests.** Retry at least twice before the elapsed-time bound applies: `retry_count < 2 || elapsed < max_retry_time`. Tests assert semantics and not exact jittered delays: a non-retryable error is attempted exactly once, a timeout stops retries, and each retry is logged.

**Undo log for mutations without transactions.** An in-memory mutation system that needs rollback logs each mutation's inverse as data and replays the log backward on failure.

```rust
enum UndoOp {
    CreateNode(NodeId),
    DeleteEdge(Edge),
    UpdateAttr { id: NodeId, old: Value },
}
```

- Each new mutation kind adds its undo record and its rollback path in the same change. An exhaustive `match` enforces it, because one missing kind is a silent consistency gap.
- Use real transactions when the storage engine provides them.

**Classify retries from the whole error chain.** Walk the source chain (`std::error::Error::source`, or `anyhow`'s `chain().find_map(|e| e.downcast_ref())`) for the innermost typed backend error.

- Retry only when it is explicitly temporary. Pass a typed permanent error through unchanged. Wrap an unknown error as permanent, naming the operation.
- Never add a broad catch-all retry. A test proves a permanent error passes through after exactly one attempt.

**Routed-resource lookups in a distributed service.** The lookup returns `Result<Arc<Part>, ErrorCode>` with a distinct machine-readable code per miss, such as `SpaceNotFound` and `PartNotFound`, and holds the read lock only for the lookup.

- Every operation starts with the lookup and applies leadership and permission checks immediately after it, before touching the engine.
- "Leader changed" and "leader lease failed" are distinct codes, so a client can re-route or retry.
- A local invariant violation still panics; it does not become a status value.

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

**Parallel kernels with a sequential and an atomic form.** A parallel graph framework owns traversal, filtering and frontier creation; each algorithm supplies a tiny kernel:

```rust
trait EdgeKernel {
    fn cond(&self, dst: VertexId) -> bool;
    fn update(&self, src: VertexId, dst: VertexId) -> bool;
    fn update_atomic(&self, src: VertexId, dst: VertexId) -> bool; // compare_exchange on an atomic
}
```

`update` and `update_atomic` must be semantically equivalent, or the sequential and parallel modes diverge. Implement all three hooks together and test under real parallel races. Not when the update needs broad mutable state that cannot be made atomic or partitioned.

**Parallel passes that produce diffs, applied once.** For parallel passes over a shared structure, workers read the unchanged initial structure, each accumulates its own diff plus side results (a rayon `fold` with a per-worker `(DiffBuilder, Accumulator)`, then `reduce` to merge), and one deterministic apply step mutates the structure at the end, so writes never interleave with reads. Merging must be associative and order-independent, or the merged diff is sorted before applying. Peak memory holds all parts and all diffs until the apply. Generate-parts, run-on-part, merge and final apply are separate functions with lifecycle tests. Not when later parts must see earlier mutations.

**Lifecycle as an explicit async state machine.** Each lifecycle state owns its event loop and returns an explicit transition value instead of mutating a global status.

```rust
pub enum Transition {
    Stop,
    Advance(StateHolder),
}

#[async_trait]
impl State for Running {
    async fn next(mut self: Box<Self>, ctx: &mut JobContext) -> Result<Transition, StateError> {
        tokio::select! {
            msg = ctx.rx.recv() => { /* handle a control message, maybe Advance */ }
            _ = tokio::time::sleep(HEARTBEAT) => { /* check liveness */ }
            _ = log_interval.tick() => { /* periodic report */ }
        }
    }
}
```

- Allowed transitions are declared in one place. Adding a state updates the state module and the transition declarations together.
- No new lifecycle path goes through an ad hoc status flag.
- For a short request handler, a plain enum and `match` is enough.

**Lazy backends in a keyed registry.** Key a dynamic integration by its stable connection identity (scheme and authority), cache the trait-object adapter, and defer the heavy client construction to first use.

```rust
pub struct LazyStore<S> {
    cell: tokio::sync::OnceCell<S>,
    initializer: Box<dyn Fn() -> BoxFuture<'static, Result<S>> + Send + Sync>,
}

impl<S> LazyStore<S> {
    async fn get(&self) -> Result<&S> {
        self.cell.get_or_try_init(|| (self.initializer)()).await
    }
}
```

- Lazy construction moves failures from start-up to the first I/O call. The error names the backend, and creation is logged.
- A new scheme extends the one central dispatch and keeps the cache and lazy wrappers. No call site constructs a client inline.
- A failed load retries on every request. Add backoff or a cached diagnostic when failures repeat.
- In a local tool, validate configuration and probe reachability before constructing the client, and return an error that carries the cause and concrete suggestions. A process-global client leaks between tests (give it a reset or isolate the process) and is wrong for a multi-tenant server with per-request credentials.
- Static wiring is simpler when backends are few and cheap.

**Validate a stream's contract once, adapt every item the same way.** A metadata-only adapter over a lazy stream checks the stream-level contract before returning (an arity mismatch is an error naming both counts), then maps every item through the same derived metadata.

```rust
let schema = rename_schema(&stream.schema(), names)?; // fails here, before any item
let stream = stream.map(move |item| item.and_then(|batch| with_schema(batch, &schema)));
```

- The advertised schema and the per-item schema change together, never one alone.
- A change of types, semantics or ordering is an explicit projection step, not a rename adapter.

**Trace context at the spawn boundary.** Instrument where work is spawned, so spawned tasks inherit trace context by default instead of entering spans ad hoc inside task bodies.

```rust
use tracing::Instrument;

tokio::spawn(work().instrument(tracing::Span::current()));

let span = tracing::Span::current();
tokio::task::spawn_blocking(move || span.in_scope(|| blocking_work()));
```

- Put this in the project's one spawn helper or `JoinSet` wrapper. Wrapper span names are coarse; domain attributes and business-level spans stay at the call site.

**Whole-unit FIFO assignment.** When a queued unit must be assigned as a whole, a unit that does not fit goes back to the front and assignment stops.

```rust
while let Some(region) = self.task_queue.pop_front() {
    match assigner.try_assign_task_region(region) {
        Ok(assigned) => assignments.extend(assigned),
        Err(region) => {
            // Accepted downside: head-of-line blocking. Keeps FIFO order, no partial assignment.
            self.task_queue.push_front(region);
            break;
        }
    }
}
```

- State the accepted downside in the code. Trying later items instead needs a redesign of starvation, ordering and atomicity, not a local tweak.
- Monitor queue depth and free slots. Use a priority or fair-share queue when small later jobs should overtake.
- Model work capacity separately from data ownership. A worker with no tasks that still owns intermediate data a consumer needs is not idle, so idleness, scale-down and shutdown check both. Logical slots are not resource isolation; memory and CPU need their own accounting.

**A supervisor fails in-flight jobs before it restarts the worker.** A supervisor that owns a crash-prone worker (thread, child process, WASM instance) keeps a registry of in-flight jobs keyed by a stable job ID.

```rust
struct Supervisor {
    in_flight: HashMap<JobId, oneshot::Sender<Result<Output, WorkerError>>>,
    consecutive_restarts: u32,
}

impl Supervisor {
    fn on_worker_exit(&mut self) -> Result<(), WorkerError> {
        for (_, reply) in self.in_flight.drain() {
            let _ = reply.send(Err(WorkerError::Crashed)); // caller may have gone away
        }
        self.consecutive_restarts += 1;
        if self.consecutive_restarts > MAX_RESTARTS {
            return Err(WorkerError::CircuitOpen);
        }
        self.spawn_worker()
    }

    fn on_worker_ready(&mut self) {
        self.consecutive_restarts = 0; // reset only after a successful ready signal
    }
}
```

- A clean error beats a hung future. Jobs are rejected, not replayed: the caller decides whether a retry is safe.
- Test worker termination during a request, and assert that the caller gets a useful error.
- Per-request native allocations are released on every path by an owning guard whose `Drop` frees, never by a manual free after the happy path. A test injects a failure mid-dispatch and asserts the release.

**A timeout does not mean the worker stopped.** For a periodic job whose work cannot be force-cancelled, a timed-out worker keeps its per-key lock until it is observed finished.

```rust
match self.running.get(&job) {
    Some(handle) if !handle.is_finished() => return TickOutcome::StillRunning, // skip this tick
    Some(_) => { self.running.remove(&job); } // the worker really ended; its lock guard is gone
    None => {}
}
self.running.insert(job.clone(), tokio::task::spawn_blocking(move || run_holding_lock(job)));
```

- The worker holds the lock guard itself, so the release happens at its real end. Releasing on timeout alone starts a second run over the same state.
- Track live workers separately from scheduling state, and record the `timeout` and `still_running` transitions.
- The work is idempotent. A long-lived timeout needs observability and a manual recovery path.

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

- **Several keyed locks.** Take them in one global order (sort by a stable key), keep the guards in a `Vec` so they are released together, and never let a call site choose its own order. Striped locks bound the number of locks, but unrelated keys can share a stripe. No long I/O inside. Test the two-key collision case.
- **Double-buffered work sets.** An iterative scheduler keeps a current and a next set, and at the start of each round does `std::mem::swap(&mut cur, &mut next); next.clear();`, so work scheduled during a round cannot change the set being consumed. Test the first round, the swap, "also this round" and the early stop when nothing new was scheduled.
- **Dependency-aware scheduling.** Dependency traversal, timeout interruption, error propagation and removal of the failed task belong to the scheduler; a task exposes `run`, its children and its termination state. Dependent work never bypasses the scheduler.
- **Engine and callbacks.** The engine owns loading, scheduling, storage and iteration; user code implements a trait with one required method and default no-op lifecycle hooks. Add a hook only when the algorithm needs that state, since an empty default can hide a missed lifecycle need.

**Probe without the lock, then lock around the side effect.** The fast path reads a registry without the mutex; the slow path takes it, re-checks, and only then runs the side effect.

```rust
static REGISTRY: LazyLock<LanguageRegistry> = LazyLock::new(LanguageRegistry::new);
static DOWNLOAD_CACHE_LOCK: Mutex<()> = Mutex::new(());

pub fn get_language(name: &str) -> Result<Language, Error> {
    if let Ok(lang) = REGISTRY.get_language(name) {
        return Ok(lang);
    }
    let _cache_guard = DOWNLOAD_CACHE_LOCK
        .lock()
        .map_err(|e| Error::LockPoisoned(e.to_string()))?;
    if let Ok(lang) = REGISTRY.get_language(name) {
        return Ok(lang); // another thread loaded it while this one waited
    }
    ensure_cache_registered(name)?;
    REGISTRY.get_language(name)
}
```

- A poisoned lock becomes a typed error, not a panic.
- A global lock can hide a long download. In a service, add a timeout or cancellation and log the wait.
- Test concurrent first access: N threads, exactly one download.
- Do not use this when every lookup mutates, or when a stale negative lookup is dangerous.

**Delayed-task scheduler that never runs callbacks under its lock.** Keep a min-heap ordered by due time, `BinaryHeap<Reverse<(Instant, TaskId)>>`, under a mutex that protects only heap bookkeeping.

- Pop the due task under the lock, drop the guard, run the callback, then lock again. Insertion and abort are never blocked by long work.
- Callbacks tolerate concurrent scheduler operations. An abort that races with a running task waits or is reported, never ignored.
- This is not for persistent or distributed jobs.

**Active and pending copies.** When readers need a stable structure while background work prepares a replacement, keep an active copy and an optional pending one.

- A modification clones the active copy into pending if none exists and populates pending independently.
- Promotion swaps pending into the active slot atomically (`ArcSwap`, or `active = pending.take()` under a short write lock) and repairs every dependent object that referred to the old copy in the same step.

**Keyed resource with `Connecting` and `Connected` states.** For an expensive keyed resource whose miss starts async setup, store both states under the same key and decide a local action under the lock.

```rust
enum Action {
    Return(ManagedHandle),
    AwaitConnection(watch::Receiver<()>),
    StartConnection(watch::Sender<()>),
}

let action = match self.tunnels.lock().expect("lock poisoned").entry(key.clone()) {
    Entry::Occupied(mut o) => match o.get_mut() {
        State::Connected(handle) => Action::Return(ManagedHandle::new(handle, self, &key)),
        State::Connecting(rx) => Action::AwaitConnection(rx.clone()),
    },
    Entry::Vacant(v) => {
        let (tx, rx) = watch::channel(());
        v.insert(State::Connecting(rx));
        Action::StartConnection(tx)
    }
};
// The guard ended with the statement above. Every .await happens after it.
```

- Waiters re-check the map after the watch fires, because the starter may have failed and removed the entry.
- If the starter future is dropped or fails, a drop guard removes the `Connecting` entry. Without it every waiter hangs forever.
- The managed handle removes the map entry when its last user drops it.
- Do not share when callers need isolated credentials, independent cancellation or separate quotas.

**Ordered multi-key batches and flush epochs.**

- Keep the batch in a `BTreeMap`, so its keys iterate in the same order as the lock key space. Acquire every lock in that order first, and only then enter the flush epoch. No item is then marked dirty in a later epoch than its batch.
- Keep the phases separate: lock acquisition, mutation, visibility, dirty marking.
- Large batches hold many locks. Bound the batch size, and add concurrency tests before changing lock scope.
- Model persistence progress as explicit states keyed by `(flush_epoch, object_id)`.

```rust
pub enum Dirty {
    NotYetSerialized { low_key: InlineArray, node: Object, collection_id: CollectionId },
    CooperativelySerialized { object_id: ObjectId, data: Arc<Vec<u8>>, mutation_count: u64 },
    MergedAndDeleted { object_id: ObjectId, collection_id: CollectionId },
}
```

- A final state is never overwritten within an epoch, and an assertion checks it.
- Adding a state updates the final-state check, the install path, flush matching, the event verifier and crash-recovery tests together.
- Run fault-injection and concurrency tests. This is overkill for a simple cache with no epoch ordering.

**Scoped thread-local context restores the previous value.** A guard that sets ambient thread-local context at a callback or FFI boundary puts the previous value back on drop instead of clearing it, so nested registrations unwind correctly.

```rust
thread_local! {
    static CURRENT: Cell<Option<Tracker>> = const { Cell::new(None) };
}

pub struct TrackerGuard {
    previous: Option<Tracker>,
}

impl TrackerGuard {
    pub fn enter(tracker: Tracker) -> Self {
        Self { previous: CURRENT.with(|c| c.replace(Some(tracker))) }
    }
}

impl Drop for TrackerGuard {
    fn drop(&mut self) {
        CURRENT.with(|c| c.set(self.previous.take()));
    }
}
```

- Registration is explicit at every entry point.
- Never use it for an async task that can hop threads. Use a task-local or an explicit argument.

**Scoped metric guards.** A timer or gauge guard records in `Drop`, so early returns and `?` are covered. `mem::forget` or a leaked guard skips the record, and a guard held across `.await` times the suspension too.

**Debug-only lock-rank checking.** Give every lock a rank, with a leaf rank for locks under which nothing else is taken, and assert in debug builds that a thread acquires only a lock of higher rank than those it holds.

```rust
#[cfg(debug_assertions)]
thread_local! {
    static HELD: RefCell<Vec<LockRank>> = const { RefCell::new(Vec::new()) };
}

#[cfg(debug_assertions)]
fn check_order(rank: LockRank) {
    HELD.with(|held| {
        let held = held.borrow();
        assert!(held.last().is_none_or(|top| *top < rank), "lock order violation: {rank:?} under {held:?}");
    });
}
```

- A rank is assigned before the lock's first use. A new lock without a rank makes the check drift.
- Tests cover nested acquisition in the allowed and the forbidden order.

**Index-stealing workers for uneven independent work.** A shared "next index" hands each item out exactly once and balances itself without pre-split ranges or a queue. Rayon's `par_iter` is the first choice; this is the dependency-free form.

```rust
let next = AtomicUsize::new(0);
let results: Vec<Vec<Output>> = std::thread::scope(|scope| {
    let handles: Vec<_> = (0..workers)
        .map(|_| {
            scope.spawn(|| {
                let mut local = Vec::new();
                loop {
                    let index = next.fetch_add(1, Ordering::Relaxed);
                    let Some(item) = items.get(index) else { break };
                    local.push(process(item));
                }
                local
            })
        })
        .collect();
    handles.into_iter().map(|h| h.join().expect("worker panicked")).collect()
});
```

- Per-item writes are isolated. Results are merged after the parallel section and sorted when order matters.
- A trivial workload runs serially, and the single-worker path is tested.
- Do not use it for dependent jobs, ordered execution or cancellation inside an item.
- A lock-protected facade that delegates every method is generated by a macro when signatures change often, with an explicit opt-out for intentionally lock-free methods. Generated locking still hides contention and deadlocks, and it is wrong where per-method invariants or cross-object ordering matter.

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

- **Classify a failure before retrying it.** Never retry a compiler error, a panic, an invariant violation, a deterministic assertion, an authorization failure or a schema incompatibility. Retry hazards: a timeout after the remote effect already succeeded, a library retry nested inside an application retry, cancellation between an effect and its acknowledgment, jitter that outlasts the parent deadline, and a retry that discards the first error chain. Keep both the first and the terminal error. A bounded channel does not bound the system if another producer is unbounded.
- **Backpressure is part of correctness.** It lets the system reject and explain work before resource exhaustion destroys the evidence needed to diagnose it.
- **Telemetry that maps to the design.** Record the parent of each task and its shutdown result, queue depth with its capacity, the typed terminal result and the cancellation reason. Keep cancellation distinct from other terminal states. Do not build metric labels from user input, do not let a span guard cross an `.await` by accident, and check that panic paths and sampling do not drop the rare terminal failures. A library should not impose telemetry policy: typed errors and executable examples are its diagnostics.

- **`try_send` on a reactor thread.** A blocking send on a full inbox parks the thread that drives every other task. Use `try_send` and decide each outcome:

```rust
match inbox.try_send(msg) {
    Ok(()) => {}
    Err(TrySendError::Full(_)) => warn!(shard_id, "inbox full, dropping message"),
    Err(TrySendError::Disconnected(_)) => warn!(shard_id, "inbox closed"),
}
```

  Choose drop or backpressure explicitly and write down the recovery path (write-ahead log, retransmission). Without one, a dropped message is data loss.
- **Drop guard for completion.** When "finished" must be signalled on every exit path, return a guard whose `Drop` sends the notification (for example the generation number on a `watch` channel, unless a newer generation was already processed). `Drop` cannot await and a failed send is silent, so do not use it when success, failure and cancellation must be told apart. Name the guard after its side effect and test overlapping generations.
- **Stale results from cancelled work.** For typeahead or search, cancel the previous request's `Arc<AtomicBool>`, install a fresh one, and also give each request a monotonically increasing id; the consumer rejects any result whose id is not the latest. Use an ordered queue instead when every request must complete.
- **Share in-flight loads.** For an expensive lazy load, cache finished results and the work in progress, so concurrent callers await one load (`tokio::sync::OnceCell` per key, or a map of shared futures). Remove the in-flight entry when it ends and decide whether a failure is cached; otherwise a failing load is retried by every caller forever. Not when each caller needs its own instance or its own cancellation.
- **Coalescing requests.** Merging pending requests under a lock is fine for level-triggered state ("needs a rerun"); keep edge-triggered events (one-shot triggers, queued items) explicitly or they are lost. Test the timing cases.
- **Round-robin with `Relaxed`.** `counter.fetch_add(1, Ordering::Relaxed) % candidates.len()` is acceptable for spreading load across candidates that were already filtered and partitioned (local first, then remote). It is not acceptable where the order is part of correctness.
- **In-process event broker.** Key subscriptions by event type (`trait Event: Debug + Clone + Send + Sync + 'static`), make `subscribe` `#[must_use]` and return a handle that unsubscribes on drop, keep payloads cheap to clone, and give slow subscribers a timeout or a bounded queue. Not for cross-process or durable delivery.
- **Worker-owned resources.** Bind a client or connection that is expensive or not thread-safe to one worker and send only job payloads through the queue. When worker errors are not returned to the submitter, report them through the job's result or a callback. A pool is a small scheduler: a queue, a registry of workers with a state, a maximum size, and a completion hook that starts the next job. Cancellation must cover queued and in-flight work; test both and test saturation.
- **Bounded blocking reads behind an async API.** Keep the public API async, run the blocking storage read in `spawn_blocking`, and gate it with a configurable `tokio::sync::Semaphore`. Too many permits overload storage; too few slow every reader.
- **Shutdown owns its queue.** A temporary owner of concurrent cleanup work verifies at shutdown that nothing is still queued: every accepted job either ran and closed, or was closed without running.

**Bridging two async runtimes.** A future that wraps a task on a foreign runtime (a Python event loop, a UI loop) owns a guard whose `Drop` cancels the foreign task if the Rust future is dropped before completion, and does nothing once the task has finished. Cancellation, result forwarding and event-loop thread affinity are design points of every such bridge: schedule the cancel on the foreign loop through its thread-safe entry point and never call the other runtime's loop methods from an arbitrary thread. Prefer a maintained adapter crate over a hand-rolled bridge.

**The capacity permit travels with the queued item.**

```rust
pub struct MessageWithPermit {
    pub inner: Message,
    _bytes_permit: Option<OwnedSemaphorePermit>, // lifetime guard: released when the message is dropped
}
```

Byte or slot capacity is released when the item is dropped, wherever that happens (processed, discarded, cancelled). The unused-looking field is load-bearing: keep it and say so in a comment. Not when the permit must be released before the item itself is dropped.

**Bounded send queue that counts unacknowledged work.** A send queue limited by bytes and by count must track both unsent batches and batches sent but not yet acknowledged, or memory is unbounded while the peer is slow. A limit checked before the increment can overshoot by one batch; decide whether that is acceptable. Adding a batch type updates size accounting, enqueue, wait callbacks and failure flushing together.

**Admission before enqueue.** Order the steps of accepting work: ask the admission policy first (reject, delay or allow), check capacity or evict second, and increment the running gauge immediately before spawning. A task that never runs can then never evict or displace accepted work or leak a count. A delay slot held while sleeping is released on every path, including cancellation of the sleeping future, so release it in a guard's `Drop`. Not needed when admission and queue capacity are the same decision.

**One event enum for a terminal UI or long-running client.** Periodic ticks, key input and asynchronously loaded data become one stream consumed by one state machine:

```rust
pub enum Event { Key(KeyEvent), Tick, DataLoaded { data: UiData } }

tokio::select! {
    _ = interval.tick() => { tx.send(Event::Tick).ok(); }
    Some(Ok(evt)) = reader.next().fuse() => {
        if let crossterm::event::Event::Key(key) = evt { tx.send(Event::Key(key)).ok(); }
    }
}
```

A new UI action is a new variant handled in the app state; widgets never make network calls. An unbounded channel hides backpressure when producers outpace rendering, so use a bounded channel or coalesce ticks. Not when the UI framework already owns a full event loop.

**Shutdown guard with cascading cancellation.** Task ownership equals guard lifetime.

```rust
impl Drop for ShutdownGuard {
    fn drop(&mut self) {
        if !self.temporary {
            self.token.cancel();
        }
        let count = self.ref_count.fetch_sub(1, Ordering::SeqCst);
        if count == 1 {
            let _ = self.tx.send(());
        }
    }
}
```

- Dropping a non-temporary guard cancels the shared token, so a failed or finished task brings its group down. The last guard dropped signals that all children are done.
- Children get guards through provided methods (`child_guard`, a named `spawn_task`), never by hand-cloning tokens and channels.
- Make the cloning rule obvious: a temporary guard does not cancel.
- For one-shot ownership a `JoinSet` is enough.
- A cached, transport-bound client is looked up through one helper with one key shape; inconsistent keys create duplicate clients. Its shutdown is explicit: stop the event loop, drain background tasks, then report drain completion (count, success, error).

**Hedged requests for idempotent reads.** Start the primary request, and start a backup on another replica only if the primary has not answered after a grace period.

```rust
let primary = fetch(replica_a, &key);
tokio::pin!(primary);

tokio::select! {
    result = &mut primary => match result {
        Ok(value) => return Ok(value),
        Err(_) => return fetch(replica_b, &key).await, // failure before the timer: fall back now
    },
    _ = tokio::time::sleep(grace) => {}
}

tokio::select! {
    Ok(value) = &mut primary => Ok(value),
    Ok(value) = fetch(replica_b, &key) => Ok(value),
    else => Err(Error::BothReplicasFailed),
}
```

- The first success wins, and dropping the loser's future cancels it locally. The remote work may continue.
- Never hedge a write or any call with side effects. Do not hedge on a saturated cluster, because the duplicate work amplifies load.
- Test the latency and failure cases before applying this to a new RPC.

**Stream completion is the channel closing.** Turning a blocking producer (a database cursor) into a cancellable stream uses a bounded channel, sends with a timeout, and guaranteed termination on success, failure and timeout.

- Completion is the last sender being dropped, which also happens on early return and panic, or an explicit `enum Item<T> { Row(T), Done }`. Never use an in-band magic value that a real row could equal.
- Validate and normalise a user-supplied plan once into typed work items before constructing workers. A worker never reinterprets raw input, and fan-out width is bounded by an explicit semaphore, not by input size.

**Optimistic in-memory event append.** Append by compare-and-swap with a version check, retry contention with a capped retry count, and publish to subscribers only after the append is accepted. Test append ordering, version rejection and publication. This is not a durable high-volume log.

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

- **Child handle tied to its parent.** The wrapper owns the raw pointer, keeps alive the option state the C side still points into, and borrows the parent through `PhantomData`:

```rust
pub struct RawIterator<'a, D: DbAccess> {
    inner: std::ptr::NonNull<ffi::iterator_t>,
    _readopts: ReadOptions,          // C side keeps pointers into this
    db: PhantomData<&'a D>,          // iterator cannot outlive the database
}
```

  Prove it with a compile-fail test whose expected output is the borrow error. Not needed when the C library hands out independent owned handles.
- **One macro for a C error out-parameter.** Copy the message, free it with the library's own free function, and return early:

```rust
pub(crate) unsafe fn from_cstr_and_free(ptr: *const c_char) -> String {
    let s = String::from_utf8_lossy(unsafe { CStr::from_ptr(ptr) }.to_bytes()).into_owned();
    unsafe { ffi::lib_free(ptr as *mut c_void) };      // never Rust's allocator
    s
}

macro_rules! ffi_try {
    ( $($function:ident)::*( $($arg:expr,)* ) ) => {{
        let mut err: *mut ::libc::c_char = ::std::ptr::null_mut();
        let result = $($function)::*($($arg,)* &mut err);
        if !err.is_null() {
            return Err(Error::new(unsafe { from_cstr_and_free(err) }));
        }
        result
    }};
}
```

  The early return fits only functions with a compatible `Result`. Test the success and the error path of each wrapper.
- **`Cow` where a view must be normalised for C.** Return `Cow::Borrowed` when the storage already has the required form and `Cow::Owned` when a sliced view must be rebased. A pointer taken from the `Cow` is valid only while it lives: bind `let proper = indptr.to_proper();` in a scope that outlives the call and never call `.as_ptr()` on a temporary.
- **Safe shape bounds, private unsafe fast path.** Public APIs carry the shape constraints in types; the implementation takes the unchecked path only after it has established them:

```rust
if self.data.is_contiguous() && rhs.data.is_contiguous() && out.data.is_contiguous() {
    // shapes already equal: one flat loop over as_slice_unchecked()
} else {
    // nested column and row loop through checked accessors
}
```

  A storage trait whose `is_contiguous` or `strides` the fast path trusts is an `unsafe trait`, because a wrong implementation is undefined behaviour.
- **`extern "C"` entry points.** Set the out-parameters to null or zero first, convert opaque pointers once at the top, and validate every size and type relation between the inputs before any work.
- **Packed bitmaps and other low-level copies.** Write the common fast paths explicitly (tiny copies bit by bit, byte-aligned bulk copy, unaligned shifting) and return a useful summary such as "any null seen". Do not simplify without benchmarks and tests for zero, tiny, aligned, unaligned, inverted and boundary-spanning ranges.

**One narrow type owns raw allocation.** If raw buffers are needed, a single small struct (`data: NonNull<u8>, len: usize, layout: Layout`) owns alignment, capacity rounding (for example up to a multiple of 64 bytes), allocation and `Drop`; nothing else calls the allocator. Prefer an existing buffer type from an established crate. Test zero capacity, large capacity, conversions to and from safe types, and drop.

**Language bindings over a Rust core.**
- The binding layer is thin: normalise inputs, call the core, wrap the returned core handle in a new immutable wrapper. It has no behaviour of its own. When changing a wrapper method, check both the facade and the native method, and test overloads and deprecation adapters, because the two drift.
- Errors cross the boundary through one pair of conversion traits, never ad hoc `map_err` per call:

```rust
trait FromHostResult<T> { fn from_host_result(self) -> CoreResult<T>; }
impl<T> FromHostResult<T> for PyResult<T> {
    fn from_host_result(self) -> CoreResult<T> {
        self.map_err(|err| CoreError::host(HostedErr(err)))
    }
}
trait IntoHostResult<T> { fn into_host_result(self) -> PyResult<T>; }
```

- A host exception enters Rust as a wrapped "hosted" error and leaves as the original exception. Cancellation and interrupt signals keep their identity; they are not wrapped as generic runtime failures.

**Checked constructor first, unchecked twin only after profiling.** Write the safe constructor (`try_new(..) -> Result<Self, Error>`) first, with tests for every invalid shape. Add `unsafe fn new_unchecked(..)` only when profiling shows the validation is being repeated on data already proven valid. Its documented preconditions are exactly the checks `try_new` performs, and each call site carries a nearby argument for why `try_new` would pass. Never call the unchecked form to silence an error.

**Binding-layer lifetimes as a state machine.** When a wrapper holds a resource and the owner it depends on, fields drop in declaration order, so order them deliberately and say so:

```rust
struct ActiveWrite {
    txn: WriteTransaction, // field order is load-bearing: txn must be dropped before db
    db: Py<Database>,
}
enum State { Pending(ActiveWrite), InWith(ActiveWrite), Finalized }
```

Rely on field drop order only with a comment and a test. Model the host language's scope protocol (enter, exit) as explicit states; re-entry and use after finalisation return errors instead of panicking or touching freed state.

**Plans owned by a native engine.** A planner that emits a plan into a native engine keeps traversal in a builder layer and funnels every native append call through one checked wrapper that turns the return code into a typed error. Dispatch is an exhaustive match over the node enum, so a new node kind fails to compile until it is handled.

**Dynamic-library plugins need a compatibility gate.** Rust has no stable ABI, so a Rust-ABI plugin is valid only when built by the same compiler, for the same target, against the same API version. Check all three before calling anything else in the library:

```rust
fn err_on_mismatch(plugin: &BuildInfo, host: &BuildInfo) -> Result<(), PluginLoadingError> {
    if plugin.api_version != host.api_version { return Err(PluginLoadingError::ApiMismatch); }
    if plugin.rustc != host.rustc { return Err(PluginLoadingError::CompilerMismatch); }
    if plugin.target != host.target { return Err(PluginLoadingError::TargetMismatch); }
    Ok(())
}

pub unsafe fn load(path: &Path) -> Result<LoadedPlugin, PluginLoadingError> {
    let lib = Library::new(path)?;
    let get_build_info: Symbol<GetBuildInfo> = lib.get(GET_BUILD_INFO_SYMBOL)?;
    let ctor: Symbol<Constructor> = lib.get(CONSTRUCTOR_SYMBOL)?;
    err_on_mismatch(&get_build_info(), &BuildInfo::get())?;
    let plugin = Box::from_raw(ctor(host_allocator()));
    std::mem::forget(lib); // plugin code must stay mapped while any plugin object lives
    Ok(LoadedPlugin { plugin })
}
```

The host passes its allocator so both sides allocate and free with the same one. The library is deliberately leaked, so plugins are never truly unloaded and a "reload" leaves the old code mapped. Test with a mismatched build-info fixture. Untrusted plugins run out of process in a sandbox instead.

**Foreign callbacks that steer or feed native work.**
- Translate the host language's control signals into a typed control value at the boundary and propagate every other exception unchanged; never swallow an unknown exception as control flow:

```rust
match result {
    Err(e) if e.is_instance_of::<PruneSearch>(py) => Ok(Control::Prune),
    Err(e) if e.is_instance_of::<StopSearch>(py) => Ok(Control::Break(())),
    Err(e) => Err(e),
    Ok(_) => Ok(Control::Continue),
}
```

- Cross the dynamic-language boundary once, before going parallel. Run every host callback and all validation (NaN, negative weights) up front on the calling thread, into a plain table indexed by stable ids (`Vec<Option<f64>>`, keeping `None` for holes left by removed items); the parallel section then touches only native values and never calls back into the host runtime. An optional callback is an enum with a default-value variant (`enum CostFn { Default(f64), Callback(Py<PyAny>) }`). Test inputs with removed items. The table costs memory proportional to the index bound. Not when the callback depends on mutable traversal state or must be lazy.

**Typed wrappers over raw parser matches.** Replace stringly typed captures with generated per-query types whose generic associated types are tied to the query and tree lifetimes:

```rust
pub trait Query {
    type Match<'query, 'tree: 'query>: QueryMatch<'query, 'tree>;
    type Capture<'query, 'tree: 'query>: QueryCapture<'query, 'tree>;
    fn raw(&self) -> &'static raw::Query;
    /// # Safety
    /// `m` must have been produced by this same query instance.
    unsafe fn wrap_match<'query, 'tree>(&self, m: raw::QueryMatch<'query, 'tree>) -> Self::Match<'query, 'tree>;
}
```

The unsafe step happens in exactly one place, and the public iterator API is safe because it always pairs the raw matches with the query that produced them. Keep `raw`, `wrap_match`, `wrap_capture` and the cursor adapters in step, and test invalid capture indexes. Not for ad hoc exploratory queries.

**Owned versus borrowed handles from a C API.** When binding a C API, write the owning wrapper (its `Drop` calls the matching delete function) before any business logic, and document for every API whether it returns an owned or a borrowed pointer. Never put an owning wrapper around a borrowed handle; that is a double free. RAII fixes lifetime, not thread safety: a shared handle still needs synchronisation or one instance per thread.

**Mirror the C library's ABI version range.** A binding re-exports the library's version constants and checks a loaded grammar or plugin against the supported range before use.

```rust
pub const LANGUAGE_VERSION: usize = ffi::LIB_LANGUAGE_VERSION as usize;
pub const MIN_COMPATIBLE_LANGUAGE_VERSION: usize = ffi::LIB_MIN_COMPATIBLE_LANGUAGE_VERSION as usize;

pub fn check_version(found: usize) -> Result<(), LanguageError> {
    if (MIN_COMPATIBLE_LANGUAGE_VERSION..=LANGUAGE_VERSION).contains(&found) {
        Ok(())
    } else {
        Err(LanguageError::IncompatibleVersion { found })
    }
}
```

- The failure is a typed error. Handles stay opaque: never reach into a private C struct.
- A generated file starts with a header naming its generator and its regeneration command. Reviewers inspect the generator and a representative output, because generated code can hide a bad abstraction.
- When one native core is exposed to many languages, one binding specification generates every package around the same opaque core type. CI runs a freshness check that fails when generated files are stale, and per-language end-to-end tests check the same behaviours. A new method goes into the specification and those tests, never by hand into one package.

**Fixed header layout checked at compile time.** A fixed-width network, disk or shared-memory record that is decoded by a byte cast is `#[repr(C)]`, derives the checked `bytemuck` traits, and has compile-time size and offset assertions.

```rust
pub const HEADER_SIZE: usize = 256;

#[repr(C)]
#[derive(Debug, Clone, Copy, CheckedBitPattern, NoUninit)]
pub struct GenericHeader {
    // fixed-width fields, then:
    reserved_command: [u8; 128],
}

const _: () = {
    assert!(size_of::<GenericHeader>() == HEADER_SIZE);
    assert!(offset_of!(GenericHeader, reserved_command) + size_of::<[u8; 128]>() == HEADER_SIZE);
};
```

- `CheckedBitPattern` rejects invalid enum and bool bytes. `NoUninit` forbids padding.
- After the cast, a `validate()` method checks semantic fields before use.
- Pin integer widths, alignment, endianness and enum representation.
- Editing the header updates the offset assertions and the invalid-byte tests in the same change.
- This is not for extensible formats.

**Bindings over a native async engine.**

- Implement the Rust binding first. The host-language wrapper is a typed one-line facade with documentation.
- Plan creation, execution, metrics caching and format conversion live in the native core.
- A synchronous host method that drives an async Rust future blocks the caller's thread. It releases the interpreter lock while waiting, checks for interrupts, and its doc says it blocks.
- Extension hooks such as user-defined functions cross the boundary in the engine's native batch format (Arrow arrays through the C data interface), never as per-record adapter objects.
- A host callable's exception becomes an execution error.
- Tests cover type conversion, null handling, host exceptions and reconstruction across processes.
- Examples of one feature in several languages keep the query text and parameter names identical, and each closes its session on failure paths too.

**Sandboxed extension code behind a byte protocol.** User-supplied extension code runs in a WASM sandbox behind a small host-owned binary protocol: serialised inputs in, bytes out, with explicit registration.

```rust
pub fn call(&mut self, input_bindings: &[&str]) -> Result<Vec<u8>> {
    let serialized = serde_json::to_vec(input_bindings)?;
    let data: &[u8] = self.plugin.call(&self.name, serialized)?;
    Ok(data.to_vec())
}
```

- Every call is fallible plugin I/O.
- Enabling WASI or host functions widens the sandbox. Do not call it a security boundary without a threat-model review.
- Test serialisation and repeated invocation before adding a capability. Trusted first-party functions are plain Rust.

**Crash handlers report once and re-raise.** A signal handler emits minimal diagnostics once, restores the default disposition and re-raises, so the shell and core-dump tooling see the real abnormal termination.

```rust
extern "C" fn handler(sig: i32) {
    static BEEN_HERE_BEFORE: AtomicBool = AtomicBool::new(false);
    if !BEEN_HERE_BEFORE.swap(true, Ordering::SeqCst) {
        // minimal write to stderr
    }
    restore_default_and_reraise(sig); // sigaction(SIG_DFL), then raise
}
```

- The atomic guard stops recursion when the handler itself faults.
- No logging framework, lock or heap-heavy formatting runs in a signal handler. Printing a backtrace allocates and is not strictly async-signal-safe; accept that knowingly and keep the `unsafe` small.
- No recovery logic belongs there.

**Status codes and typed symbols in an exported C ABI.** A C ABI exported from Rust publishes opaque handle pointers and an explicit status enum with fixed numeric values (0 for success, positive for informational, negative for errors), never an internal struct layout.

- Every handle has explicit create and free functions, and every entry point returns the status.
- For overload-like ergonomics, generate the real typed functions with a macro for ABI clarity and layer a generic facade (a trait implemented per type) on top. Add the typed symbol first, then the facade entry, in the same change.

**Niche-optimised arena handles.** An arena handle carries its target type and stores a non-zero index, so `Option<Handle<T>>` is four bytes and a handle for one arena cannot index another.

```rust
pub struct Handle<T> {
    index: NonZeroU32,
    _phantom: PhantomData<T>,
}

impl<T> Clone for Handle<T> {
    fn clone(&self) -> Self { *self }
}
impl<T> Copy for Handle<T> {}
```

- Slot 0 of the arena is reserved and never initialised, so zero never means "some".
- Implement `Clone`, `Copy`, `Eq` and `Hash` by hand. A derive would wrongly require `T: Clone` and so on.
- Build the index with `NonZeroU32::new(..).expect(..)` outside proven hot paths; `new_unchecked` rests on the reserved-slot invariant. Test the `Option` round trip before changing the representation.
- Handles do not survive an arena rebuild.

**Raw container machinery behind typed operations.** Intrusive lists and raw-pointer linkage are wrapped in narrow typed operations generated once, by a macro or a generic. The raw form stays a private implementation detail, and the linkage field is declared next to the element type.

**One closed enum owns a set of grammar bindings.** A supported-parser set is one enum that drives CLI parsing, listing, display names and query compilation, and it is the only place that touches the unsafe grammar FFI.

```rust
#[derive(Display, FromRepr, EnumIter, VariantNames, PartialEq, Eq, Hash, Debug)]
#[strum(serialize_all = "lowercase")]
pub enum Language {
    Go,
    Rust,
    TypeScript,
}

impl Language {
    pub fn language(&self) -> tree_sitter::Language {
        // SAFETY: each function returns a pointer to a static grammar linked into this binary.
        unsafe {
            match self {
                Language::Go => tree_sitter_go(),
                Language::Rust => tree_sitter_rust(),
                Language::TypeScript => tree_sitter_typescript(),
            }
        }
    }

    pub fn parse_query(&self, raw: &str) -> anyhow::Result<tree_sitter::Query> {
        tree_sitter::Query::new(&self.language(), raw).map_err(|err| anyhow!("{err}"))
    }
}
```

- The match has no wildcard and no `todo!()` arm, so a new variant fails to compile until every arm exists.
- CLI tests cover listing, an invalid-language error and one real query per language.
- Grammars loaded at run time need a plugin registry instead.

**Early close of a foreign handle is idempotent.** Normally the owning wrapper frees the native peer once in `Drop`. Where a handle must be closable early, as in bindings to a garbage-collected language, treat it as a nullable capability.

```rust
pub struct Parser {
    raw: Option<NonNull<ffi::Parser>>,
}

impl Parser {
    pub fn close(&mut self) {
        if let Some(raw) = self.raw.take() {
            // SAFETY: `raw` came from `ffi::parser_new` and `take()` guarantees it is freed once.
            unsafe { ffi::parser_free(raw.as_ptr()) }
        }
    }

    fn handle(&self) -> Result<NonNull<ffi::Parser>, Error> {
        self.raw.ok_or(Error::Closed)
    }
}

impl Drop for Parser {
    fn drop(&mut self) {
        self.close();
    }
}
```

- Exactly one function frees the peer, and every method checks the capability and returns an error after close.
- An atomic pointer makes the pointer read atomic. It does not make the native object thread-safe.

## 11. Performance

### Performance without sacrificing correctness

- **Panic-free arithmetic and slicing.** External input plus unchecked indexing is a classic source of boundary bugs. Use `checked_*`, `saturating_*` and `.get()` for ranges, offsets, terminators, suffix stripping and parser cursor movement. Do not rely on "we already proved this above" in code that will change.
- **Builder plus frozen config struct.** Configuration is mutable during construction and immutable during execution; a builder that produces a cheap frozen config makes the split explicit. Use when a component has many orthogonal knobs and a stable execution phase. Keep runtime state and expensive artifacts out of the builder.
- **Accumulate, then build, collecting errors as you go.** Some structures (pattern sets, registries, ignore lists, aggregated configuration) can only be optimized once the whole batch is known. Collect non-fatal build-time errors separately from final construction. Do not force eager construction on every incremental addition.
- **Prepare once, query many.** Precompute a normalized or derived view once as a named value type, then reuse it across many checks: matching, routing, filtering, repeated comparison against one input. Avoid when precomputation costs more than the reuse saves or hides a freshness requirement.

- **Verify a performance change on two axes.** The benchmark delta, and a check that no checked operation became unchecked and no precomputed value outlives the freshness of its input. Do not replace `.get()` with indexing in a loop because the benchmark improved. "We already proved this above" stops being true when the code moves, so when a check is removed, state the invariant at the place the check was. Prefer speedups that add named structure (a precomputed view as its own type) over speedups that remove checks. Use saturating arithmetic only where saturation is the documented meaning, not to hide an overflow.

- **Benchmark pitfalls.** A debug build cannot support a production claim, an average hides the tail, one run gives no precision, and dead-code elimination can remove the work being measured. Clones do not tell you allocations: measure them. Declare the input distribution, toolchain, target, build profile and features; assert that both versions return identical results; report variance. Noise sources include CPU frequency scaling, allocator caching, cache warmth, hash order and async runtime startup. A microbenchmark supports only the measured operation on that machine. Do not ban `clone` because one microbenchmark was faster, and keep the simpler version when the requirement is already met.

- **Let the measurement reject work.** Performance evidence is strongest when it can show an optimization is unnecessary or damages a contract. Run correctness tests before measuring, and reproduce a result on a second run before acting on it.

**One options struct and one timings struct at the orchestration boundary.** A multi-stage pipeline takes a single borrowed options struct and returns per-stage timings:

```rust
pub struct SearchOptions<'a> {
    pub path: &'a Path,
    pub queries: &'a [String],
    pub language: Option<&'a str>,
    pub max_results: Option<usize>,
    pub timeout: u64,
}
pub struct SearchTimings {
    pub query_preprocessing: Option<Duration>,
    pub file_searching: Option<Duration>,
    pub result_processing: Option<Duration>,
    pub total_search_time: Option<Duration>,
}
```

Per-stage `Option<Duration>` fields attribute a regression to a stage. A new flag is threaded through the options struct, the pipeline and the timing output in one change, with tests for default propagation and flag interactions. Do not let the options struct become a dumping ground.

**Parse once, precompute, evaluate many.** When one parsed query is evaluated against many inputs, move interpretation into a plan built once (term indices, required and excluded sets, shortcut flags such as "matches everything" or "only exclusions") so the scan never re-walks the syntax tree. A single `Mutex<LruCache>` shared by many evaluating threads becomes contention; use a per-thread or sharded cache. New syntax updates parsing, term collection, the precomputed flags and the tests together. Not for single-shot evaluation.

**Dense dispatch tables.** For a closed set of numbered operations, register handlers by type during start-up (a map) and compile the registrations once into a dense table indexed by the stable operation code (`Vec<Option<Handler>>` or an array), so dispatch is O(1). Validate the code (`table.get(code)`, with an error for an unknown or unregistered code) instead of indexing unchecked. Adding an operation updates the code mapping, the registration and a missing-handler test. Not for sparse, untrusted or late-loaded operation types.

**Runtime-chosen representation.** When a shared runtime can run a step over a sparse or a dense representation, the runtime, not each algorithm, picks one from a cheap workload estimate (active items plus their outgoing edge count against a threshold). A bad threshold costs speed but never correctness. Callers can force one mode with a flag, and tests exercise both branches and assert identical results.

**Thread-local caches for worker threads.** State that is expensive to build, mutable or not `Send` (parsers, compiled queries, scratch buffers) is cached per worker thread instead of behind a shared `Mutex` on the hot path:

```rust
thread_local! {
    static THREAD_PARSERS: RefCell<HashMap<Language, Parser>> = RefCell::new(HashMap::new());
}

fn ensure_thread_parser(language: Language) -> Result<(), ParseSetupError> {
    THREAD_PARSERS.with(|parsers| {
        let mut parsers = parsers.borrow_mut();
        if parsers.contains_key(&language) { return Ok(()); }
        let mut parser = Parser::new();
        parser.set_language(&language.grammar())?;
        parsers.insert(language, parser);
        Ok(())
    })
}
```

Initialise lazily and return the construction error instead of panicking. Never hold the `RefCell` borrow across a call that can re-enter the same thread-local. The cache lives as long as the worker thread, so bound it. Not for small single-threaded tools, where it only complicates lifecycle and tests.

**Out-of-core processing under a memory budget.**

- Put the memory-budget decision beside the storage metadata. If the budget is smaller than the data, use direct I/O and stream partitions; otherwise use buffered reads.
- Expose the algorithm as a callback over already-filtered partitions, for example `fn stream_edges(&self, active: Option<&Bitmap>, f: impl Fn(&Edge) + Sync)`. The algorithm says "process matching edges", and the storage layer decides how to stream them.
- State the callback's mutation rules: atomic updates or partition-local ownership. A callback can hide random writes into shared state.
- One array-like type can support both full-file memory mapping and an explicit hot window loaded with positioned reads when the state exceeds the budget.
- Memory mapping gives no crash-consistent writes, is unsafe when another process truncates the file, and is not worth it for small vectors.

**Cache a stable eligibility decision at the call site.** When a hot path asks "is this enabled?" and the answer changes only with configuration, cache it in an atomic per static call site (never, sometimes, always), so the hot path is one atomic load.

- Rebuild the cache deliberately whenever configuration changes. Any runtime reconfiguration (a new subscriber, a changed level or filter) calls the rebuild path, or sites stay wrongly enabled or disabled.
- Test reconfiguration after call sites already exist.
- This does not fit eligibility that depends on volatile per-record state.

**Slow side effects leave the hot path through a bounded channel and a guard.** Log or telemetry I/O goes through a bounded channel to a worker thread, and the constructor returns a `#[must_use]` guard whose `Drop` signals shutdown and flushes.

```rust
let (writer, _guard) = tracing_appender::non_blocking(file);
// `let _guard` keeps the worker alive until the end of scope; `let _ =` drops it at once and loses logs.
```

- Choose and document the pressure policy: lossy (`try_send`, with drops counted and exposed as a metric) or blocking (`send`, so producers feel backpressure). Test both.
- Never use it for audit or transactional records that must be durable before the program continues.

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

- **Buffer pool with a returning guard.** The guard holds `Option<Vec<u8>>` so `Drop` can take it, and a `Weak` to the pool so a buffer that outlives the pool is simply freed:

```rust
impl Drop for PooledBuffer {
    fn drop(&mut self) {
        if let (Some(buf), Some(pool)) = (self.buf.take(), self.pool.upgrade()) {
            pool.lock().put_back(buf);        // clear, and cap the capacity kept
        }
    }
}
```

  A pool retains peak memory, so cap the capacity it keeps and stress-test before changing that. Not worth it in a small command-line tool.
- **Permissive builder, compact final form.** Collect sparse entries as triplets (row, column, value) in any order, convert once to the compressed form, and sum duplicates in that conversion. Build compressed adjacency by counting degrees, prefix-summing to offsets, then filling one contiguous array. Constructors that `assert!` on lengths and bounds panic on bad input; give untrusted data a fallible constructor. Test directed, symmetrised, self-loop, duplicate and weighted inputs.
- **Compile-time and run-time sizes under one trait.** In numeric libraries, a `Const<const N: usize>` and a `Dyn(usize)` can implement one dimension trait, with arithmetic as traits that have an associated `Output`. Implement each operation for both, and compile static-static, static-dynamic and dynamic-dynamic examples. Not for business objects.
- **Dense internal ids.** Compact ids on input and expand results on output at the I/O boundary, never inside the kernel. Decide the mapping, one sentinel for "no result", and the output format before calling the kernel.
- **Two representations with a switch.** When a cost model switches between two representations of the same data at a threshold, the thresholds depend on the workload: test at the switch boundary and keep a result verifier.

**Scoped memory accounting.** A child tracker forwards each `allocate(bytes)` to its parent and sums what it forwarded; on close or `Drop` it releases the whole sum to the parent in one call, so a query or a collection is accounted for without tracking each element. Allocating after close is an error.

```rust
struct ScopedTracker<'a> { parent: &'a Tracker, tracked: usize }
impl Drop for ScopedTracker<'_> {
    fn drop(&mut self) { self.parent.release(self.tracked); }
}
```

**Fixed-capacity stack buffer for `no_std`.** Where the heap is forbidden, a const-generic buffer states its invariants in the type and enforces them at every write boundary.

```rust
#![deny(unsafe_code)]

pub struct FixedBuffer<const N: usize> {
    buffer: [u8; N],
    length: usize,
}

impl<const N: usize> FixedBuffer<N> {
    pub fn write_bytes(&mut self, bytes: &[u8]) -> Result<(), FixedBufferError> {
        let remaining = N - self.length;
        if bytes.len() > remaining {
            return Err(FixedBufferError::CapacityExceeded {
                bytes_needed: bytes.len(),
                bytes_available: remaining,
            });
        }
        self.buffer[self.length..self.length + bytes.len()].copy_from_slice(bytes);
        self.length += bytes.len();
        Ok(())
    }
}
```

- The capacity error carries the bytes needed and the bytes available.
- A failed write leaves the buffer unchanged. A property test asserts this, and it is written before any new mutation method.
- If `as_str()` relies on the contents being UTF-8, every byte-writing path must preserve that and never split a multi-byte character.
- Implement `core::fmt::Write` so `write!` works. Use `String` when allocation is acceptable.

**Inline small case, heap for the rest.** A compact representation keeps the common small case inline and falls back to the heap for large or complex cases: `SmallVec`, a small-string type, or `enum Node { Inline(InlineData), Heap(Arc<HeapData>) }`.

- Adopt it only after profiling shows allocation or cache locality is the bottleneck.
- Document layout invariants beside the type and pin the size: `const _: () = assert!(std::mem::size_of::<Node>() == 16);`.
- A layout change touches every copy, free and tag path. It is never a local edit.

**Fixed capacity as a type-level constant.** In `no_std`, embedded or deterministic code the capacity is a const generic, storage is stack or static, and every push site returns a structured capacity error instead of panicking.

```rust
#![no_std]

pub struct TopoSort<const N: usize> {
    adjacency: [heapless::Vec<usize, N>; N],
    in_degree: [usize; N],
    num_nodes: usize,
}

impl<const N: usize> TopoSort<N> {
    pub fn add_edge(&mut self, from: usize, to: usize) -> Result<(), TopoSortError> {
        if from >= N || to >= N {
            return Err(TopoSortError::IndexOutOfBounds { index: from.max(to), capacity: N });
        }
        let current = self.adjacency[from].len();
        self.adjacency[from]
            .push(to)
            .map_err(|_| TopoSortError::CapacityExceeded { current, max: N })?;
        self.in_degree[to] += 1;
        Ok(())
    }
}
```

- Check bounds before indexing, and write one capacity-exceeded test per push site.
- Storage of N by N rules this out for large or unbounded inputs.

**Arena lifetime matches workload lifetime.** Many small allocations that die together (one file's parse, one temporary registry) go in a bump arena such as `bumpalo::Bump`, which is reset at the phase boundary and reused.

- Name the owning phase. Nothing arena-backed escapes it; the `&'bump` borrow enforces that.
- A long-lived arena is a leak in disguise: it grows to the largest workload it has ever seen.

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

- **Cache identity includes policy.** Settings that change validity (time to live, maximum entries, persistence, authorization scope) are part of the cache's key or identity type, not only a closure argument. Reuse a cache only when they match and close the old storage before replacing it. When adding an option, update the equality check, the storage context and the replacement tests together.
- **Negative results.** Cache a failed optional lookup separately from successes, and accept that it can go stale. A global cache needs an invalidation path and a test with changed credentials or options.
- **Cache keys from every semantic input.** Hash the tool version, the source file, dependency directories (excluding outputs), and each environment knob; separate fields with a tag and a zero byte; sort directory entries before hashing so traversal order cannot change the key; never use timestamps as identity.

```rust
let mut entries: Vec<_> = fs::read_dir(dir)?.collect::<Result<_, _>>()?;
entries.sort_by_key(|e| e.file_name());
for entry in entries {
    hasher.update(b"file\0");
    hasher.update(entry.file_name().as_encoded_bytes());
    hasher.update(b"\0");
    hasher.update(&fs::read(entry.path())?);
}
```

  Size and modification time may serve as a shortcut to skip re-reading an unchanged file, never as the identity. Namespace cached output by the extractor version, write the index with a temporary file and an atomic rename, and keep a `--force` escape hatch.
- **Invalidate by contract when that is the unit.** When downstream work depends only on the public structure, hash the sorted structural facts (name, signature, parameters, return type, imports) and classify a change as none, cosmetic or structural. The hash ignores bodies by design; add behaviour inputs explicitly if they matter.
- **Per-thread worker state in rayon.** Share immutable data in an `Arc`, build the mutable, non-thread-safe state once per worker thread, and count with atomics:

```rust
files.par_iter().for_each_init(
    || Highlighter::with_store(store.clone()),          // once per worker thread
    |highlighter, path| match process(highlighter, path) {
        Ok(()) => { done.fetch_add(1, Ordering::Relaxed); }
        Err(e) => { failed.fetch_add(1, Ordering::Relaxed); eprintln!("{}: {e}", path.display()); }
    },
);
```

  Per-thread processing does not give a stable output order; collect results with an index and sort when order matters.
- **Parallel export with one sink per chunk.** Share the schema, give each chunk its own sink and decoder through a factory, and let one generic driver own the orchestration (`(0..size).into_par_iter().step_by(chunk_size)` with `try_for_each`, each chunk calling `sink.finish()?`). Use it only where independent output chunks are acceptable; keep a single ordered writer where order or one transaction is required.
- **Batch writes by shape.** Group bulk writes by statement shape (same table, label or statement), not only by count. Parallel batches each need their own connection and a first-error policy. Not when ordering across shapes matters.
- **Append-only chunk writer.** Reuse one buffer (clear it, and shrink it to a soft maximum after an unusually large batch), write a placeholder length header, stream the records through a compressing encoder wrapped in a checksum hasher, backfill checksum and length in a fixed order, and issue one `write_all`. Add a round-trip reader test whenever the chunk format changes. Not for random updates or per-record `fsync`.

**Cache the compiled intermediate form.** When a stable description (a query plan, a schema, a template) is repeatedly lowered to an intermediate representation, store the lowered form behind a lock (`Mutex<Option<Cached>>`): the first call converts and stores, later calls reuse. Know what invalidates it before allowing the description to change. Watch lock contention and memory growth from cloned arenas.

**Normalise to the physical representation once.** At the boundary of a computation kernel, convert logical values to their physical representation, match on the type tag, and downcast immediately inside the arm that proved the type (the one place an `unwrap` on a downcast is acceptable). Canonicalise floats (`-0.0`, NaN payloads) before hashing or comparing them as keys.

**Changing facts as incremental inputs.** In an incremental computation framework, each changing fact is a typed input (`#[salsa::input] struct FileText { text: Arc<str>, file_id: FileId }`) set with a durability level: rarely changing inputs (library sources) are marked durable so revalidation can skip everything that depends only on them. One over-broad query that reads global data destroys incrementality, so ask what each new query will be invalidated by. Batch tools that run once should use plain immutable context instead.

**Semantic scope before text scan.** For usage search and rename, build the search scope from the semantic graph first (reverse dependencies of the defining crate, module children, visibility) as a map from file to optional text range, then scan text only inside it. Reuse the existing scope builder for every usage-style query instead of collecting files ad hoc.

**Large on-disk caches of regenerable results.** The cache version combines a hand-bumped schema number with the package version; a mismatch means start empty. A small index (version and key list) stays in memory while payload shards are loaded on demand. A missing or unreadable shard is a cache miss, never an error. Keys are validated so a key cannot be a path (no separators, no `..`). A change to any field that affects cached output bumps the schema number in the same change, with a warm-cache regression test.

**Small in-memory embedding index.** Items and their vectors are two aligned arrays mutated only together under the write lock, and the query cache is cleared in the same locked section whenever vectors change. A query caches its embedding by prompt text in a bounded cache, takes a read lock only for the scan, scores every stored vector with cosine similarity, drops scores below a minimum, sorts descending and takes the top k. Never hold the lock across the embedding call. Inner-product ranking equals cosine only when vectors are normalised, so never mix normalised and unnormalised embeddings. Fine for medium in-process catalogs, not for million-scale or distributed indexes.

**Hidden reordering.** A batching optimisation that reorders inputs (sorting by length to reduce padding) restores the original order before returning, so callers never see it. A per-model strategy is an explicit adapter chosen by an exact model identifier, not by substring matching with a silent default.

**Derived data cached on its owner.** Derived facts (a transpose, degree vectors, a symmetry flag) are computed lazily and reused, with "not computed" and "unknown" explicit (`Option<T>`, `enum Tri { True, False, Unknown }`). One invalidation function resets every derived field, and every mutation of the base data calls it: make the base field private and mutate only through methods that invalidate. A stale derived fact silently gives wrong answers. Not when the base changes so often that invalidation cannot be proven.

**First error wins.** Once an error is recorded for an operation, later failures during cleanup or unwinding must not overwrite it.

**Streaming a large top-level JSON array.** Consume bulky inputs one element at a time through an iterator instead of deserialising the whole document, and make every error name the element index:

```rust
pub(crate) fn iter_json_array<T: DeserializeOwned, R: Read>(
    mut reader: R,
) -> impl Iterator<Item = Result<T, io::Error>> {
    let mut started = false;
    (0..).map_while(move |i| {
        yield_next_obj(&mut reader, &mut started)
            .map_err(|e| io::Error::new(e.kind(), format!("element #{i}: {e}")))
            .transpose()
    })
}
```

The step function reads `[` first, then before each element expects `,` or `]`. Handle `[` followed directly by `]` explicitly, or an empty array is fed to the element deserialiser. Tests: an empty array, a malformed separator and premature end of input. `serde_json::Deserializer::from_reader(..).into_iter()` covers whitespace-separated values but not a comma-separated array. Not when validation needs cross-element context before any output.

**Canonical hashing of structured values.** Raw bytes hash directly (`Sha256` over the content, hex-encoded). A structured value is hashed in a canonical form: object keys sorted, only a whitelist of identity-bearing fields included, arrays left in order when order is meaningful (traces, patches, rankings). Write down which fields define identity before adding a hash. Test the same content in a different key order (same hash) and different content in the same shape (different hash). Over-normalising collapses distinct inputs; under-normalising causes needless cache misses.

**Rank fusion keeps every signal separate.** Compute a per-signal reciprocal rank (`1.0 / (k + rank + 1)`) for lexical, semantic and evidence channels; use a negative signal that demotes test and fixture files instead of excluding them (make the demotion conditional for test-writing work); apply a graph boost only to items already in the result set, never to add new ones. Keep the per-signal breakdown on each result so ranking can be debugged and tuned.

**Handle manager for expensive open resources.** When many logical objects are backed by fewer open resources such as file handles, a small manager owns the bounded LRU cache, the lock and the close-on-evict behaviour.

- Logical lifetime is decoupled from physical lifetime.
- The cache key includes every opener argument that distinguishes handles (path, mode, options), which prevents aliasing.
- Callers never close a handle acquired from the manager.
- Plugin discovery is lazy and cached once in a `OnceLock`. The plugin contract is validated at load time, with a typed options struct and not a free-form map.

**Greedy selection under a budget.** Score candidates by relevance, sort descending, and take each one that still fits.

```rust
scored.sort_by(|a, b| b.relevance_score.total_cmp(&a.relevance_score));

let mut used_tokens = 0;
let mut selected = Vec::new();
for entity in scored {
    if used_tokens + entity.estimated_tokens <= budget {
        used_tokens += entity.estimated_tokens;
        selected.push(entity);
    }
}
```

- An item that does not fit is skipped; a smaller later one may still fit. This is a heuristic, not optimal packing.
- Return the amount used. Use `f64::total_cmp` for a total order that tolerates NaN.
- When weights or depth limits change, add an example that pins the selected items and the amount used for a known input.

**Conservative prefilter in front of expensive matching.** A prefilter may produce false positives and never false negatives.

```rust
enum Formula<P> {
    And(Vec<Formula<P>>),
    Or(Vec<Formula<P>>),
    Pred(P),
}

enum Predicate {
    Literal(String),
    Regex(Regex),
}
```

- Decide what "cannot translate" means before writing the combinators. An `And` drops an untranslatable term with `filter_map`, since fewer conditions are still sound. An `Or` with any unknown branch becomes unknown as a whole, with `collect::<Option<Vec<_>>>()`, because dropping a branch would drop real matches.
- Keep a fast literal path beside the regex path, cache compiled regexes, and treat a regex evaluation error as a match.

**Caches that own side-effectful resources.**

- A cache addressed by two keys, such as directory and generated project ID, keeps the forward and reverse maps in one owner struct and updates them together in add, move, remove and clear.
- A generated ID is the directory name, with a short hash of the full path appended only on collision. A collision of the shortened hash is detected, not assumed impossible.
- Eviction stops a file watcher or subprocess before it removes the entry.
- A bounded LRU of long-lived external-tool sessions has one owner for connection lifetime, eviction and cleanup. Each session runs in a task that holds its resources and waits on a stop signal.
- The eviction callback only signals stop, because eviction is synchronous and cleanup is async. Shutdown runs an explicit pass that awaits every session task, since fire-and-forget eviction cleanup is no shutdown guarantee.
- Test eviction and explicit cleanup separately.

**Registry-composed pipelines and resumable batches.**

- A retrieval pipeline is assembled from named stages resolved through a registry, with per-stage timings.
- A per-call override such as `top_k` is a request parameter or is applied to a per-request clone. Never mutate a shared component and restore it afterwards: that races across concurrent requests and leaks on an early return.
- Single-query and batch paths are implemented and tested together.
- A long batch run checkpoints each finished unit under a deterministic key such as `(trial, task_id, seed)`. Under one lock it skips a saved key, writes to a temporary file in the same directory, renames it into place, and flushes the index.
- Replacing a unit whose earlier result was an infrastructure error is a separate, explicit operation. Tests cover resume, duplicate save, replacement and a crash during the write.
- Randomness inside a domain object is injected or seeded (`&mut impl Rng`), so tests are deterministic.

**Bounded cache of expensive machinery.** Cache expensive machinery in a fixed table of `OnceCell` or `OnceLock` indexed by the small supported parameter space, so the cache is bounded by construction.

```rust
static AUTOMATON_BUILDER: [[OnceCell<LevenshteinAutomatonBuilder>; 2]; 3] = [
    [OnceCell::new(), OnceCell::new()],
    [OnceCell::new(), OnceCell::new()],
    [OnceCell::new(), OnceCell::new()],
];

let builder = AUTOMATON_BUILDER
    .get(self.distance as usize)
    .ok_or_else(|| InvalidArgument(format!("Levenshtein distance of {} is not allowed", self.distance)))?
    [self.transposition_cost_one as usize]
    .get_or_init(|| LevenshteinAutomatonBuilder::new(self.distance, self.transposition_cost_one));
```

- An input outside the supported range is a typed invalid-argument error raised before execution, never an unbounded build.
- The bound is a product decision. Raising it increases memory and expansion cost sharply.
- Tests cover the bounds, each mode and invalid operand types.

**Lazy consolidation of signed updates.** For frequent signed updates where many increments and decrements cancel, append cheaply and consolidate only when a clean view is needed or the dirty tail outgrows the clean prefix.

```rust
pub struct ChangeBatch<T, const X: usize = 2> {
    updates: SmallVec<[(T, i64); X]>,
    clean: usize,
}

impl<T: Ord, const X: usize> ChangeBatch<T, X> {
    pub fn update(&mut self, item: T, value: i64) {
        self.updates.push((item, value));
        self.maintain_bounds();
    }
}
```

- Consolidation sorts, sums equal keys and drops zeros.
- Methods that may compact take `&mut self`, including observers such as `is_empty`. Observing can change the representation, and the doc says so.
- A `SmallVec` with inline capacity avoids allocation for the common tiny batch.
- Tests cover cancellation to empty, draining, and that no zero entry is retained.

**Frontier-gated notifications.** In a streaming operator that buffers by logical time, delayed work is released only when observed input progress proves that no earlier data can arrive, never by a wall-clock timer.

- Holding a capability retains a progress obligation. Drop it as soon as its work is emitted, or everything downstream stalls.
- Every stash keyed by timestamp has a test that advances the frontiers and proves release order.

**Retrieval and incremental indexing.**

- Linter traversal and ignore-directive filtering are centralised in the linter, not in each rule. A stateful rule clears its accumulated data in its finalisation hook or is constructed per file, or findings leak across files. Every rule has an ignore-directive test.
- Index a code chunk together with cheap structural context, and store the same enriched text for embeddings and for the keyword column, so dense retrieval, keyword search and reranking all see it.

```rust
pub fn build_structural_context(block: &CodeBlock) -> String {
    let mut parts = Vec::with_capacity(4);
    parts.push(format!("# File: {}", block.path));
    parts.push(format!("# Language: {}", block.language));
    if !block.symbols.is_empty() {
        parts.push(format!("# Defines: {}", block.symbols.join(", ")));
    }
    parts.join("\n")
}
```

- A paired function strips the preamble before display, or snippets and line numbers shown to people are polluted.
- When scores from two retrieval systems are not comparable, fuse ranks through stable row IDs: each source adds `weight / (rank + k)` to the ID's score.

```rust
for (i, id) in vector_ids.iter().enumerate() {
    let score = self.vector_weight / (i as f32 + self.k);
    rrf_scores.entry(*id).and_modify(|e| *e += score).or_insert(score);
}
// The same loop over keyword_ids with self.keyword_weight.
```

- Weights and `k` are configuration tuned by evaluation sweeps. Tests cover vector-only hits, keyword-only hits and overlap. With calibrated comparable scores, use the scores.
- Incremental indexing keeps per-file old and new content-hash sets: new minus old is inserted, old minus new is deleted, and no full rebuild is needed.

```rust
let exists = !force_reindex && ctx.store.content_exists(&content_hash, "code_blocks").await?;
if !exists {
    code_blocks_batch.push(code_block.clone());
}

let hashes_to_remove: Vec<String> = existing_hashes
    .into_iter()
    .filter(|hash| !new_hashes.contains(hash))
    .collect();
```

- The hash inputs define cache identity. Including line ranges improves uniqueness but re-embeds after pure movement, so choose the inputs from the invalidation behaviour wanted.
- Changing chunking updates hash construction and stale-removal tests together.

**Canonicalise, then hash.** An identity hash of structured data is computed from a canonical form: sort and deduplicate every unordered semantic collection, serialise, then hash, and carry a format version in the hashed data.

```rust
fn canonical_strings(values: &[String]) -> Vec<String> {
    let mut values = values.to_vec();
    values.sort();
    values.dedup();
    values
}

pub fn schema_ir_hash(ir: &SchemaIr) -> Result<String> {
    let json = canonical_json(ir)?; // collections already sorted, ir.version included
    let mut hasher = Sha256::new();
    hasher.update(json.as_bytes());
    Ok(format!("sha256:{:x}", hasher.finalize()))
}
```

- Equivalent input in any declaration order gives one hash. Skip the sorting where declaration order is meaningful.
- For each new field decide whether it is semantic or presentation-only, and change the canonicalisation and the hash-stability tests in the same commit.
- Normalise by type through a trait implemented per domain type. Do not hash `Debug` or default serialisation output and hope it is stable. A value that cannot be hashed deterministically is an explicit error or a documented fallback.
- Short IDs derived from a hash can collide, so check for collisions explicitly. An identity hash is not a security proof.

**Bitset prefilter and reused scoring buffers.** A fuzzy matcher rejects most impossible candidates with one bit test before any scoring.

```rust
#[derive(Clone, Copy, Default)]
pub struct CharBag(u64); // one bit per lowercased a-z and 0-9

impl CharBag {
    pub fn is_superset(self, other: CharBag) -> bool {
        self.0 & other.0 == other.0
    }
}
```

- The prefilter is monotonic: it rejects only impossible candidates and is never the only correctness check.
- Scoring matrices are fields reused across candidates (`clear()` then `resize(len, None)`), stored as one flat `Vec` indexed `[query_idx * path_len + path_idx]`, not as nested vectors.
- Keep candidate eligibility, score calculation and match-position reconstruction separate.
- Matrix size grows with query length times candidate length, so a large search keeps its cancellation checks. A change to scoring constants keeps the multi-byte boundary tests and the reconstruction invariants.

**Rolling hashes nominate, comparison decides.** Duplicate detection over fixed-size windows uses a rolling hash, so all overlapping windows cost one pass.

```rust
hash = hash.wrapping_mul(BASE).wrapping_add(incoming);
hash = hash.wrapping_sub(POWER.wrapping_mul(outgoing)); // POWER = BASE^window
```

- Collapse a long run of identical items to its first and last before windowing, and test repeated-item input separately.
- A hash match only nominates a candidate. Verify by comparing the blocks.
- The result is lexical duplication, not semantic equivalence.

**A shared log segment is deleted only when every dependant has persisted past it.** A durability artifact that serves several partitions, such as a write-ahead-log segment holding writes for many keyspaces, records one sequence number per partition.

- Eviction walks from oldest to newest and stops at the first segment that some live partition has not yet persisted past. A deleted partition no longer holds a segment back.
- Crash-recovery tests cover mixed partitions, deleted partitions and eviction of the oldest segment.

**A snapshot is a leased read instant.** Opening a snapshot increments a reference count for its sequence number and returns a guard whose `Drop` decrements it.

```rust
pub fn open(&self) -> SnapshotGuard {
    let _gc = self.gc_lock.read(); // garbage collection cannot run mid-open
    let seqno = self.seqno.load(Ordering::Acquire);
    *self.open.entry(seqno).or_insert(0) += 1;
    SnapshotGuard::new(seqno, self.clone())
}

pub fn publish(&self, batch_seqno: u64) {
    self.seqno.fetch_max(batch_seqno + 1, Ordering::AcqRel); // never moves backwards
}
```

- Garbage collection frees only versions below the lowest sequence number still referenced.
- A leaked snapshot blocks collection forever. Test the drop path, export a metric for the oldest open snapshot, and detect leaks.
- Tests assert that an old snapshot still reads old values after later writes, a buffer rotation and an explicit collection.

**Durable formats: permanent field identity, optional first, absent is not zero.**

- Every serialised field of a file format or wire schema has a permanent tag that is never reused or renumbered (in `prost`, reserve retired tags).
- New information arrives as optional before it may ever become required. A reader distinguishes absent from zero or false with `Option<T>`, not a defaulted scalar, and tolerates unknown fields. Use `#[serde(default)]` only where the default really means "absent".
- Test the absent, present and unknown-field cases.
- Separate physical representation from logical interpretation: a small stable set of storage types, plus a tagged extensible enum of logical annotations that carry their parameters (`Decimal { scale, precision }`, `Timestamp { unit, utc }`). A new logical type updates the compatibility mapping, reader validation and round-trip tests, not only the enum.

**A semantic hash normalises first.** A change-detection hash over a syntax tree walks the tree, skips noise kinds (comments, whitespace), emits kind and text for value-sensitive kinds (literals, operators, identifiers) and kind only for structural kinds, then hashes that stream.

- The three kind sets define what "semantic" means. A missing value-sensitive kind reports "unchanged" for a real change.
- Changing the vocabulary is a hash-version bump and needs paired fixtures: ignored noise, and a preserved semantic edit.
- Do not use it where exact text or comments are part of the record.

**Fuse rankings by rank, not by raw score.** Heterogeneous retrieval signals (vector similarity, BM25, graph neighbours) sit on incomparable scales. Combine them with weighted reciprocal rank fusion: each list contributes `weight / (k + rank)` to an item's score.

- Graph-neighbour expansion is opt-in and down-weighted, so it cannot overpower direct matches.
- Log per-phase timings, and inspect each list separately before changing weights.

**Non-overlapping code chunks by line ownership.** Sort symbol spans by length, longest first, and assign each span's lines to it in that order, so a nested span overwrites its parent. Emit runs of one owner as chunks, and window only the unowned gaps.

- Spans are 1-based, inclusive and clamped to the file.
- A syntax error or an unsupported language falls back to plain windows without failing the index.
- Test nested ownership and the fallback. Skip this when retrieval benefits from overlapping context.

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

- **Over-correcting an anti-pattern.** Removing every clone, replacing every `String` parameter with generic `AsRef<str>`, giving every error its own enum, or adding a trait to mock one function. A clone is fine when ownership clarity outweighs a measured cost. Make no zero-cost claim without a measurement.
- **Hazards a signature does not show.** Lock guards kept alive inside iterators, `Arc` reference cycles, and a new trait changing object safety or SemVer.

- **Fixing the symptom.** Similar symptoms can need opposite fixes, so find the cause before adding a trait, clone, retry or lock. Reproduce the failure in the smallest fixture, confirm the mechanism, then change the code. The costly failures are hidden contract transfers: convenience in one function moves a panic, an ownership rule, a queue or a compatibility cost onto callers and operators. Also watch for panic hooks that hide abort behavior and locks nested through helper calls.

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

- **One outbound client wrapper.** Correlation ids, trace propagation, token refresh and retry logging live in one wrapper so every operation gets them. It does not retry non-idempotent writes.
- **Protocol error translation in one place.** Map internal errors to responses at the boundary, narrow cases first and the catch-all last, keep the source error as context, and log server-side failures.
- **Required and enhancing dependencies.** Classify each dependency of a request. A required one fails the request; an enhancing one degrades with a warning and a result tagged with the path that produced it:

```rust
let dense = dense_res.map_err(|e| anyhow!("dense search failed: {e}"))?;
let sparse = match sparse_res {
    Some(Ok(hits)) => Some(hits),
    Some(Err(e)) => {
        warn!("sparse channel failed, falling back to dense-only: {e}");
        return Ok(dense_only(dense, limit));      // every candidate tagged CandidateSource::DenseOnly
    }
    None => None,
};
```

  Count each path in metrics, or the fallback hides an outage. No silent degradation where audit or exact-match guarantees need every back end.
- **Per-tenant services.** Share the expensive resources and cache one service facade per tenant in a registry with single creation under concurrency. Handlers obtain the service from the registry, tenant identity travels in request-scoped state, tenant existence is validated before creation, and services of removed tenants are dropped. Not when tenants need process isolation or their own credentials.
- **Pipelined protocols.** Every send enqueues the handler for its expected reply in the same order and every received message pops one. A reply with no handler waiting is a protocol error. Add "append message" and "enqueue handler" together. When replies can arrive out of order, use correlation ids instead.

- **Size results for the consumer.** Derive output limits from the consumer's capacity with a safety margin, and never clip silently:

```rust
const MAX_OUTPUT_TOKENS: usize = 52_000;
const SAFETY_MARGIN: f32 = 0.85;
const SAFE_OUTPUT_TOKENS: usize = ((MAX_OUTPUT_TOKENS as f32) * SAFETY_MARGIN) as usize;

// when the serialized result is too large, keep a prefix of the array and say so
obj.insert("_truncated".into(), json!({
    "original_items": item_count,
    "kept_items": keep_items,
    "reason": "result exceeded the output limit",
}));
```

  Every array-returning operation goes through the same function and returns enough metadata for a follow-up page. When filling a budget by priority, add items while they fit, cut the first one that does not in a stated order (lowest-value parts first, main content last), then stop. Approximate limits do not fit records that must be exact and auditable.
- **Tool schemas are executable contracts.** List every tool in one registry (name, description, parameter schema), look the tool up and validate the parameters on the server before dispatch even though a model read the schema, and dispatch in one place. Test that every listed tool has an implementation and that the schemas serialize.
- **Pluggable storage behind one `open`.** Route by capability (the first back end that can handle the path, else the default), wrap the handle (for example with decompression) only when the access mode allows it, and reject unsupported combinations before the caller gets a handle. Registration order is part of the API.
- **Canonical ids.** One small module owns id normalisation (Unicode NFKC, separators, case folding) and every producer calls it; a test proves each producer gives the same output on non-ASCII input. Normalisation can collide, so pair the id with source path and kind when uniqueness matters.
- **Reverse impact walks.** Seed a breadth-first walk with the queried node and its direct members, then follow only dependency relations backwards to a depth limit. Ownership edges stay out of the dependency set.
- **External programs with shared arguments.** One function builds the invariant `Command` (common parameters, stream handling, expected exit code) and takes the variable part from one narrow hook. Argument order is part of the contract, and a logged command line can expose paths or credentials.

**The error family implements the response contract.** One implementation per error family at the service boundary maps each variant to a status and a serialised body; handlers never hand-build JSON errors:

```rust
impl ResponseError for CompilerError {
    fn status_code(&self) -> StatusCode { /* per variant */ }
    fn error_response(&self) -> HttpResponse {
        HttpResponseBuilder::new(self.status_code()).json(ErrorResponse::from_error(self))
    }
}
```

A new variant gets its `Display` text, its code/detail mapping and its status mapping in the same change. Low-level core crates do not implement HTTP traits.

**Module-level transaction contract.** For a module of database operations, state the contract in the module doc: every operation is a building block that runs inside the caller's transaction; on success the database is consistent; a failure that depends on current state returns an error; an operation that would be invalid in every possible state is a programmer bug and may panic. Classify the failure modes before writing a new operation, and never panic on a path reachable from user input.

**One wrapper around generated transport clients.** Generated clients (for example tonic) are called through one wrapper that maps the status to a domain error, keeps the original error as the source, and takes operation context from the call site: service, method and the most specific resource identifier (a binding name, a key, a path, a secret's name and never its value). A status with a domain meaning in that context (`NotFound` plus a key becomes `KeyNotFound { binding, key }`) becomes that variant; everything else becomes a generic `CallError { service, method, code, details }`. Every new client method goes through the wrapper.

**Post-response background work.** Before exposing a background-work helper, define how tasks are registered, observed, drained and reported on failure. Register each task in a central tracker (id, description, registered-at, completed flag, error), and at shutdown await everything still pending with a deadline (`tokio::task::JoinSet` or `TaskTracker`). One task's failure is recorded on its entry and never blocks or fails the drain. This is not a substitute for a durable job queue when work must survive process death.

**Typed internal HTTP client with one shared parse boundary.** Endpoint methods are domain-specific and return domain types; status handling, decoding, timeouts and URL building live in one helper layer:

```rust
pub async fn get_jobs(&self) -> ClientResult<Vec<Job>> {
    self.json::<Vec<Job>>(&self.url("jobs")).await
}

async fn json<R: DeserializeOwned>(&self, url: &str) -> ClientResult<R> {
    let response = self.get(url).await?.error_for_status().map_err(ClientError::from)?;
    response.json::<R>().await.map_err(ClientError::from)
}

fn url_encode(&self, id: &str) -> String {
    percent_encode(id.as_bytes(), NON_ALPHANUMERIC).to_string()
}
```

Every path segment taken from data is percent-encoded. Endpoint methods add no presentation behaviour such as sorting. Each endpoint has tests for URL encoding, error-status mapping and parse failure. Not when a generated client already gives correct typed boundaries.

**Endpoint-per-file router.** Centralise route registration and error conversion, and localise endpoint implementation.

- One builder registers every route. Each endpoint lives in its own handler module. One error enum implements `IntoResponse` and maps each variant to a status code.
- Adding an endpoint touches the handler module, `mod.rs`, the route builder and the shared error type.
- Split the route file by group once it stops being scannable.
- Degraded behaviour for a downstream client is decided per method and written beside the client contract: fail fast, fallback value, retry, or enqueue on failure. Never default to a no-op fallback. A logging-only fallback loses the work for good unless a retry queue or reconciliation backs it.

**Two-step authentication extractors.** Split request authentication into a parsing extractor and a verifying extractor, and make the verified type the only way into a protected handler.

```rust
pub struct ValidCredentials(pub UserId);

impl FromRequestParts<Arc<App>> for ValidCredentials {
    type Rejection = StatusCode;

    async fn from_request_parts(parts: &mut Parts, state: &Arc<App>) -> Result<Self, StatusCode> {
        // Unverified only parses the header: malformed is 400, absent is "no credentials".
        let unverified = Unverified::from_request_parts(parts, state).await?;
        state
            .auth_provider
            .check_credentials(&unverified)
            .await
            .map(ValidCredentials)
            .ok_or(StatusCode::UNAUTHORIZED)
    }
}
```

- A protected handler takes `creds: ValidCredentials` in its signature and does its permission checks in its first lines.
- The rejection is a bare status code, so no authentication detail leaks to the client.
- Multi-step redirect or session flows need middleware; an extractor does not fit them.

**Convert domain errors to transport errors at the edge.** The failure point returns the precise domain error with its source. One `IntoResponse` implementation maps each variant to a status and a fixed, safe client message.

```rust
impl IntoResponse for RegistryError {
    fn into_response(self) -> Response {
        match self {
            RegistryError::NotFound => StatusCode::NOT_FOUND.into_response(),
            RegistryError::IncomingReadFailed(_source) => {
                (StatusCode::INTERNAL_SERVER_ERROR, "could not read input stream").into_response()
            }
        }
    }
}
```

- Log the original error chain before it is discarded; a fixed client message with no server-side detail slows incident response.
- A new variant gets its source error and its explicit response arm before it is wired into a route. Unmapped cases fall through to a generic sanitised failure, never to an internal message.
- A handler that offers buffered and streaming responses runs one parse, validate and authorise path that produces one options value, and branches on output mode last. An error after the first chunk cannot become a status code, so errors after headers are sent get their own tests, and every new option is tested in both modes. Split the handlers when the modes differ in authorisation, consistency or limits.
- Data-version negotiation is an explicit parameter in the route-to-domain call (requested version in, actual version out and echoed in a response header), never ambient global state. When an option can arrive by query string or by JSON body, document and test the precedence.

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

- **Server-side fetch of a user-supplied URL.** One `validate_url(url) -> Result<Url, _>` runs before every such fetch: allow only `http` and `https`; reject private, loopback, link-local and cloud metadata addresses and internal hostnames. Checking the hostname is not enough: resolve it, check the address, and connect to the address you checked, so a second DNS answer cannot differ (DNS rebinding). Validate every redirect the same way and cap the response size. Test IPv4, IPv6, IPv4-mapped IPv6 and metadata hosts. Make intranet exceptions explicit instead of weakening the default.
- **Local paths from input.** Canonicalize, then require the result to be inside the allowed base directory (`canonical.strip_prefix(&base)`), and return `Result`. A wrapper that remaps paths sends every path parameter through the same fallible encoder; that alone is not a security boundary.
- **Deserialization across a trust boundary.** Prefer a structured format with a closed schema: `#[serde(deny_unknown_fields)]` and closed enums. Never accept an open, self-describing set of types from untrusted input; if a polymorphic format is unavoidable, restrict the accepted types before construction and test that an unrelated type is rejected.
- **Running commands.** Prefer `std::process::Command` with a program and separate arguments, no shell. If shell text must be accepted from a user or an agent, split it into pipeline segments, parse each, check the program against an allowlist, block redirects and subshells, and test the dangerous shapes. This lowers risk; it does not make arbitrary shell text safe. When a remote shell is unavoidable, model the shell dialect in a type that owns quoting, build the command in one function, and reject multi-line arguments with a real error, not only `debug_assert!`.
- **Wrapping a command-line tool as a service.** Keep command construction and output parsing in one adapter. Do not pass credentials as arguments (they show in process listings), do not infer success from output text where an exit code or structured output exists, and do not ignore a failed write to the child's stdin. Internal administration only.
- **Secrets redact by default.** Hold secrets in a type whose `Debug` and serialization print a placeholder, such as `secrecy::SecretString`, and require a narrow explicit call (`expose_secret()`) at the one place that needs the value. Replace a secret instead of mutating it. Validation messages must not reveal a secret or its exact shape.
- **Text handed to a model or an agent.** Put a policy step between retrieval and presentation: deny by path pattern (`.env`, `*.pem`, `*.key`, `id_rsa`, `*.tfvars`), replace secret-shaped text with a fixed marker, and report how many items were excluded or redacted. Every new context field goes through the same step. Pattern scans miss unusual secrets, so pair them with a dedicated scanner, and keep secret and prompt-injection fixtures in the tests.

**Authorization pre-indexed around the questions asked at run time.** For read-heavy hot-path checks, keep maps and sets shaped like the questions (`HashMap<UserId, GlobalPermissions>`, `HashMap<(UserId, StreamId), StreamPermissions>`, a set of "users that may read all streams"), so a check is a couple of lookups returning `Result<(), Error>`. Every update and delete path must maintain every derived set: a new permission dimension touches initialisation, mutation, deletion and the rule check together, with a test that a revoked permission is denied.

**No-follow path helpers for recursive walkers.** `Path::exists` and `fs::metadata` follow links; a recursive walker that uses them can loop forever or overflow the stack. Keep one small module of no-follow helpers and use only those while walking:

```rust
pub fn exists_no_follow(path: &Path) -> bool {
    fs::symlink_metadata(path).is_ok()
}
pub fn is_symlink_or_junction(path: &Path) -> bool {
    let Ok(meta) = fs::symlink_metadata(path) else { return false };
    if meta.file_type().is_symlink() { return true; }
    #[cfg(target_os = "windows")]
    {
        use std::os::windows::fs::MetadataExt;
        const FILE_ATTRIBUTE_REPARSE_POINT: u32 = 0x400;
        if meta.file_attributes() & FILE_ATTRIBUTE_REPARSE_POINT != 0 { return true; }
    }
    false
}
```

Windows junctions are reparse points, not symlinks, so check both. If linked workspaces must be followed, make it an opt-in mode with cycle detection.

**Zeroise short-lived secret carriers.** A struct that carries key material, passwords, tokens or serialised credentials implements `Zeroize` and `Drop` together, or derives `ZeroizeOnDrop`.

```rust
pub struct Pkcs12Archive {
    pub der: Vec<u8>,
    pub pass: String,
}

impl Zeroize for Pkcs12Archive {
    fn zeroize(&mut self) {
        self.der.zeroize();
        self.pass.zeroize();
    }
}

impl Drop for Pkcs12Archive {
    fn drop(&mut self) {
        self.zeroize();
    }
}
```

- Tests assert `std::mem::needs_drop::<T>()` and that `zeroize()` clears each field.
- An `into_parts()` that moves the fields out hands the duty to the caller, and its doc says so.
- Do not claim secrecy for data that was copied elsewhere, interned, logged, or passed to a library that keeps its own buffer.

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

**Format-like query macro with bound parameters.** A query macro can read like `format!` while every value becomes a bound parameter. The wrapper's `Display` writes the placeholder and moves the value into the parameter map.

```rust
impl<T: Into<BoltType>> std::fmt::Display for QueryParameter<'_, T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let Some(v) = self.value.replace(None) else {
            return Err(std::fmt::Error);
        };
        self.params.borrow_mut().put(self.name.into(), v.into());
        write!(f, "${}", self.name)
    }
}
```

- Reject ambiguous unnamed forms at compile time with `compile_error!`.
- Tests assert both the rendered query text and the contents of the parameter map.
- Document and test any form that still falls back to plain interpolation.
- Identifiers, dynamic clauses and schema names need their own escaping rules. They do not go through value parameters.

**A detached result stream owns its connection.** Bundle a lazy stream with the resource it depends on, so a caller cannot consume data after its transport is gone.

```rust
pub struct DetachedRowStream {
    stream: RowStream,
    connection: ManagedConnection,
}

impl DetachedRowStream {
    pub async fn next(&mut self) -> Result<Option<Row>> {
        self.stream.next(&mut self.connection).await
    }

    pub async fn finish(mut self) -> Result<RunResult> {
        self.stream.finish(&mut self.connection).await
    }
}
```

- An open stream holds a pooled connection, so a slow consumer can starve the pool. Document it, bound it with a timeout, or buffer fully when results are small.
- Tests cover partial consumption followed by drop, and `finish()`.
- Keep the connection in an explicit transaction scope when a transaction must manage it.

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

- **Typed option definitions.** One validated settings struct per group, checked at startup. Each option carries its parser, default and a reusable predicate such as a range check, so text becomes a typed value once, at the boundary. Test parsing, a wrong type and an out-of-range value.
- **Versioned payloads.** Persisted or queued payloads carry a format version; the version number and the old-version decode branches sit next to the serializer, not at call sites. Add a round-trip test and at least one old-version fixture. A change to serialized state is a wire-format change: update size constants, encoder, decoder and edge-case tests together.
- **No raw struct bytes on disk or wire.** Write fields one by one (`to_le_bytes`), or use a derive that guarantees a padding-free layout, so padding never leaks into the format.
- **Snapshot emission apart from mutation.** An atomic "write queued" flag can collapse redundant snapshot writes, and the state lock and the file-write lock stay separate. A crash between mutation and persistence loses the latest progress, so this does not fit audit-critical state.
- **Checkpoint before side effects.** Before starting asynchronous work that edits user files, write the rollback data and register the pending state, and define what happens when the checkpoint itself fails.
- **Scoped key-value storage.** A shared key-value store exposes a scoped handle so the owner of a namespace is explicit. Plain strings leave serialization and versioning to the caller; typed domain records get their own schema and migrations.
- **SQLite as a local coordination store.** Use WAL journal mode with a `busy_timeout`, reconcile liveness periodically and delete rows of dead processes. A process id alone does not prove identity because ids are reused: store the start time or working directory with it and verify before sending work. Not for several hosts, or for messaging that needs authentication.
- **Edited text as input.** Human- or agent-edited text that updates a database is an input format, not trusted data: parse into typed records, validate, apply in one transaction, verify against the stored state, and only then remove or advance the input. Keep a test per accepted shape.
- **Idempotent reload of providers and plugins.** Purge the entries owned by a stable source id before registering the replacement set, debounce file-watch events, and keep the old entries when a reload fails on a partially written file.
- **Synchronization tokens are a set.** For bookmarks and continuation tokens, an update removes the old ones and adds the new ones under one lock. A persistence hook that runs inside the update can fail the caller and lengthens the lock, so keep it short.

**Transaction guarantees visible where handles are created.** Document on the constructor what a handle guarantees: a read transaction is a snapshot that may coexist with writes; a write transaction is the single writer. Keep read transactions short, because a long-lived reader pins old state and blocks space reclamation. Do not wrap a whole application workflow in one transaction by default.

**Strict configuration with path-aware diagnostics.** For user-edited configuration, collect unknown keys with their full path and report them, and make a type error name the path to the field:

```rust
let mut ignored_paths = Vec::new();
let mut on_ignored = |p: serde_ignored::Path<'_>| ignored_paths.push(p.to_string());
let de = serde_ignored::Deserializer::new(value, &mut on_ignored);
let result: Result<T, _> = serde_path_to_error::deserialize(de);
```

Typos fail loudly instead of being ignored. A new config field arrives with its schema, a strict-validation test and an unknown-field diagnostic test. Not when forward compatibility requires keeping unknown fields, since a file written for a newer version would be rejected.

**Typed setting keys.** A library setting is a typed key that carries its name, description, default and parser, read through one typed getter:

```rust
pub struct Setting<T> {
    pub key: &'static str,
    pub description: &'static str,
    pub default: fn() -> T,
    pub parse: fn(&str) -> Result<T, SettingError>,
}
```

`get(&Setting<T>)` checks the explicit value, then the environment override, then the default, in that one place. A failed conversion of an override is an error that names the key and the offending value, never a silent fall back to the default.

**Storage API split into snapshot, sink and phases.** A store with concurrent writers separates an immutable snapshot view, a mutable write sink, and explicit prepare (conflict check) and flush (make visible) phases. Implement snapshot and sink together and test conflicting concurrent writers. For a simple store, one transaction object is enough.

**Transaction-scope helper.** `fn transaction(&self, attempts, join_current, f)`:
- clamps attempts to at least one;
- begins a transaction only if it did not join an outer one, commits only the transaction it created, and returns whether it created it;
- retries only on errors classified retryable (conflict, concurrent modification), rolling back before the next attempt;
- requires a closure that is safe to run more than once; external side effects stay outside the retried block or are guarded by idempotency keys.

Not when callers need savepoints or streaming across transaction boundaries.

**Ambient state.** Avoid thread-local transaction or context state in async code, where work moves between threads; pass the handle or use `tokio::task_local!`. If ambient state is unavoidable, every initialisation has a matching removal on all exit paths through a `Drop` guard. A temporary override captures the previous value, sets the new one and restores the exact previous value (not a default) in `Drop`, so nested overrides unwind correctly; express it as one helper (`fn with_mode<R>(mode, f: impl FnOnce() -> R) -> R`) and test nested calls.

**Configuration precedence lives in the config layer.** Precedence (explicit override, environment, file, default) and parsing are implemented once, not at call sites. A parse failure names the key and the offending value. Values parsed lazily at first access surface bad configuration late, so validate critical keys at startup, and give each new key a bad-input test.

**Environment knobs on hot paths.** A process-level knob read on a hot path is parsed once (`static` `OnceLock` or `LazyLock`) with a default, trimming, and rejection of invalid or negative values (keep the default). A `OnceLock` cannot be reset, so put the parsing in a pure function that tests call directly, and pass the resolved value into the component:

```rust
fn parse_budget(raw: Option<&str>) -> usize {
    raw.map(str::trim)
        .and_then(|s| s.parse::<usize>().ok())
        .filter(|n| *n > 0)
        .unwrap_or(DEFAULT_BUDGET)
}
```

Tests must not mutate the process environment: `std::env::set_var` is `unsafe` in edition 2024 and races with other test threads. Not for configuration that must change while the process runs.

**Several databases.** Each pool is a distinct named field or newtype (`struct Pools { primary: PgPool, reporting: PgPool }`), each repository takes exactly the pool it owns, and a transaction never spans pools. Adding a database adds its pool, its repositories and an integration test together.

**Transactional outbox.** When a change must reach a second system, write the source record and an outbox row in one local transaction, and let a relay replay unprocessed rows later:

```rust
pub struct OutboxEntry {
    pub id: Uuid,
    pub aggregate_id: Uuid,
    pub aggregate_type: String,
    pub operation: OutboxOperation,
    pub payload: serde_json::Value,
    pub created_at: DateTime<Utc>,
    pub processed_at: Option<DateTime<Utc>>,
    pub attempt_count: u32,
}
```

The relay stamps `processed_at` on success and increments `attempt_count` on failure. Delivery is at least once, so the target deduplicates by outbox id or natural key, and the payload carries every identifier needed for idempotent replay. A new side effect is a new operation variant and payload. Not when the second effect must be synchronous and exactly once.

**External schemas with several versions.** For specification dialects, event formats and provider payloads, detect the version once (`fn detect_version(&Value) -> Result<SpecVersion, Error>`; an unknown version is an error that lists the keys seen), convert each version into one internal normalised form at the boundary, and keep the raw input for audit. Generate missing stable ids deterministically and check them for collisions. Everything downstream is version-agnostic, and a new dialect is a new converter only.

**Hash-gated writes to a shared index.** A mutable index shared by several processes stores a hash of its contents. A writer reads the local and the remote hash before mutating, and after the mutation writes the new remote hash only if the two were equal beforehand. If they differed, it warns and leaves the remote hash alone, so drift stays visible instead of being silently blessed, and a follow-up sync must reconcile. Keep the order: local hash, remote hash, mutation, conditional hash write.

**Storage primitives versus domain operations.** The backend trait holds only the primitives a storage engine must supply (fetch, mutate, iterate), with a generic associated type for its borrowed transaction; shared query, mutation and validation logic lives once on a generic wrapper that composes them:

```rust
pub type DynIter<'a, T> = Box<dyn Iterator<Item = Result<T>> + 'a>;

pub trait Transaction<'a> {
    fn all_vertices(&'a self) -> Result<DynIter<'a, Vertex>>;
    fn sync(&self) -> Result<()> { Err(Error::Unsupported) } // optional capability
}
pub trait Datastore {
    type Transaction<'a>: Transaction<'a> where Self: 'a;
    fn transaction(&self) -> Self::Transaction<'_>;
}
pub struct Database<D: Datastore> { pub datastore: D }
```

Optional capabilities are default methods that return an "unsupported" error. A new operation goes on the wrapper when it can be composed, and on the backend trait only when a backend can do it much more efficiently. Boxed iterators cost an allocation and a virtual call per item, acceptable at this boundary but measure hot paths. Not worth it for a single hard-coded engine.

**Loading several on-disk formats.** Probe the format at the edge (magic bytes at the start of the file), convert legacy formats once into the current internal representation, and keep everything downstream format-agnostic. A missing file is a distinct error from an unsupported or malformed one. If conversion writes a converted sibling file, that side effect is explicit in the API (a `persist_to` argument), never a surprise for a caller expecting read-only loading. Each format has probe and conversion tests. Magic-byte probing is not enough when formats share a prefix or need version negotiation.

**Type-erased variable registry with typed parsing.** Erase the type only at the registry boundary, and keep parsing and constraints attached to the concrete type through function pointers captured at definition.

```rust
pub struct VarDefinition {
    pub name: &'static UncasedStr,
    pub value: VarDefaultValue,
    pub constraint: Option<ValueConstraint>,
    parse: fn(VarInput) -> Result<Box<dyn Value>, VarParseError>,
    type_name: fn() -> Cow<'static, str>,
}

pub trait DomainConstraint: Debug + Send + Sync + 'static {
    type Value;
    fn check(&self, var: &dyn Var, v: &Self::Value) -> Result<(), VarError>;
}
```

- Choose the concrete value type first and attach constraints at definition, rather than validating elsewhere after parsing.
- Downcasts rely on correct registry construction, so test each definition.
- A plain typed struct is better when there is no dynamic lookup by name.
- A config field that may hold a secret placeholder is its own type: validated on assignment, resolved through a provider at use, redacted in `Debug` and serialisation. A field accepting both templated and concrete values is an enum of the two.

**Typed option conversion for a DSL.** Each target type owns accepting, rejecting, naming and rendering its option value.

```rust
pub trait TryFromValue<T>: Sized {
    fn try_from_value(v: T) -> Result<Self, PlanError>;
    fn try_into_value(self, catalog: &dyn SessionCatalog) -> Option<T>;
    fn name() -> String;
}
```

- The reverse conversion serves display and catalog serialisation.
- Error quality depends on `name()` and the failure path. Test valid syntax and wrong-kind syntax, such as a string where a secret is required.

**Length-prefixed messages over a byte stream.** A `Content-Length` style protocol is an explicit reader state machine looping over a pending buffer. One read is never assumed to be one message.

```rust
enum ReaderState {
    Header,
    Body { content_length: usize },
}
```

- In `Header`, wait for a full header line. In `Body`, wait until `content_length` bytes are buffered, then emit the message and return to `Header`.
- Bound the pending buffer and the declared content length, and reject malformed headers. Otherwise a peer can grow memory or stall the connection.
- Tests cover a split header, a split body, several messages in one chunk and an invalid content length.
- Prefer a maintained framing codec such as `tokio_util::codec` when one fits.
- One map at the transport boundary owns the request lifecycle: an ID from a monotonically increasing counter maps to a `oneshot` sender. Success, error response, timeout and connection close each remove the entry, and connection close fails every waiter. Tests cover all four paths and out-of-order replies.

**Config discovery ladder.** The search order lives in one function that returns an ordered list, project-local before the user directory.

```rust
pub fn discover() -> Result<Option<Self>, Error> {
    for path in config_search_paths() {
        if path.exists() {
            let config = Self::load(&path).map_err(|e| {
                Error::Config(format!("Failed to parse config at {}: {e}", path.display()))
            })?;
            return Ok(Some(config));
        }
    }
    Ok(None)
}
```

- The first existing file wins. A parse failure in it is an error naming the path; it never falls through to the next file or to defaults.
- `Ok(None)` means no config. Using defaults is the caller's deliberate decision.
- A parent-directory search has a depth limit and handles symlinks with care.
- Discovery is explicit, with no ladder, where security or reproducibility requires it.
- A database-backed store owns its connection, schema setup, statement cache and close behind one handle. Use the driver's statement cache (`rusqlite`'s `prepare_cached`, `sqlx`'s per-connection cache) and do not share one connection across threads without a pool or documented synchronisation.

**Buffer-first wire codec.** Allocation is the caller's choice: the primitive writes into a caller-supplied buffer, and the convenient form is layered on top.

```rust
pub trait WireEncode {
    fn encode(&self, buf: &mut BytesMut);
    fn encoded_size(&self) -> usize;

    #[must_use]
    fn to_bytes(&self) -> Bytes {
        let mut buf = BytesMut::with_capacity(self.encoded_size());
        self.encode(&mut buf);
        buf.freeze()
    }
}
```

- `encoded_size()` and `encode()` stay in lockstep. Every wire type has a round-trip test and `assert_eq!(x.encoded_size(), x.to_bytes().len())`.
- This does not suit a streaming format whose size is unknown without doing the work twice.

**Options declare their mutability scope.** An option declaration carries its scope beside its namespace, value type, default and validation predicate.

```rust
enum Mutability {
    Fixed,         // never after first initialisation
    GlobalOffline, // cluster-wide, only while offline
    Global,
    Maskable,      // a local override is allowed
    Local,
}
```

- A change outside the allowed scope is a typed error at set time, not a downstream failure.
- Read-after-write consistency tokens shared across sessions are a mergeable set behind one small manager per workload: an update removes the consumed tokens and adds the new ones. A failure in its persistence hook is logged and monitored, never swallowed.

**Named pipeline registry.** Schema and config files refer to a processing pipeline by a stable name, while each pipeline stays a composable builder.

```rust
pub struct TokenizerManager {
    tokenizers: Arc<RwLock<HashMap<String, TextAnalyzer>>>,
}
```

- Separate named lookup from pipeline construction. `get(name)` clones the pipeline out, so no lock is held during analysis.
- Registering under an existing name replaces the pipeline and silently breaks data built by the old one. Reject or version a re-registration when persisted data depends on the name.
- Freeze the registry after startup when analysis must be immutable. Test a successful lookup and a missing name.

**Config paths resolve against the config file.** A relative path in a config file is relative to that file's directory, not to the process working directory.

```rust
#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct AppConfig {
    #[serde(default)]
    pub auth: AuthConfig,
    #[serde(skip)]
    base_dir: PathBuf, // set by the single load function, right after parsing
}

impl AppConfig {
    pub fn resolve_auth_env_file(&self) -> Option<PathBuf> {
        let path = Path::new(self.auth.env_file.as_deref()?);
        Some(if path.is_absolute() { path.to_path_buf() } else { self.base_dir.join(path) })
    }
}
```

- An empty `base_dir` resolves silently to the wrong place, so only the load function constructs the config.
- Every path field has a resolver method, tested with an absolute and a relative value.

**Additive schema reconciliation for embedded SQLite.** An embedded app may repair additive schema drift at startup: compare the desired columns with `PRAGMA table_info` and add the missing ones with `ALTER TABLE ... ADD COLUMN`.

- Use it only for nullable or defaulted additive columns. Identifiers come from the code's own schema, never from user input.
- Destructive changes, type changes, backfills and index rebuilds stay explicit ordered migrations.
- Test against snapshots of old database files.

**Read-only query gate.** When users or agents may submit queries but only reads are allowed, one shared validator serves every entry point (CLI, tool server, UI).

- Reject empty input. Strip string literals and comments before scanning. Reject statement separators. Then reject any mutating keyword on word boundaries, case-insensitively.
- A keyword scan is defence in depth, not a sandbox. The database role or connection must also be read-only.
- Before loosening the validator, add tests with forbidden keywords in comments, in strings, in procedure calls and in mixed case.

**Result limits resolved in one place.** Per-tool or per-endpoint result limits come from one helper with a fixed precedence: configuration, then the caller's default, then a built-in default, then unlimited.

- Clamp a configured value to at least 1. Warn on unknown keys, which are usually typos.
- For an agent-facing tool, malformed configuration falls back to defaults and is logged. An operational service fails startup instead.

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

Size the planning work by the trust boundaries the change crosses. Write the full set (requirements, layered design, verification matrix) when the change crosses IPC or touches capabilities, for example adding filesystem access to a window. For a small bounded change, trim it and write down which sections were dropped; the sections that feel tedious are usually the boundary ones, and the verification matrix is the last thing to drop. Skip it for a throwaway spike or for frontend styling that never crosses IPC, and write the requirements before a spike is promoted, since "it already works" is how spike code ships without them. During an incident, go straight to the failure checks and write the plan up afterward. A plan that never names a window, a permission or an IPC shape has not yet dealt with Tauri. A wrong permission or an untyped invoke payload ships inside a packaged binary on users' machines, so these come before general tidiness. A command handler that temporarily holds business logic is acceptable only with a named extraction task and a date.

Record the result of every gate in the plan: fmt, clippy, Rust tests, Rust build, frontend checks and Tauri checks. An empty results block is not done, a failing gate has an owner and a date, and a platform-specific gate that could not run locally is recorded as skipped. A gate command copied into a repo with a different layout can run nothing and still exit zero, so confirm it did real work. Before editing a capability file, check its schema against the docs for the project's Tauri major version, because permission guidance goes stale at major versions. General Rust API guidance on error types applies to command errors only within Tauri's serialization requirements.

Split Tauri work by boundaries crossed, not by lines or symbols changed. One slice holds a handful of requirements whose design decisions and matrix rows a single reviewer can keep in mind. Split when requirements multiply or the change spans several windows and capability files, for example a feature that touches both filesystem capabilities and tray lifecycle. A small diff that rewrites every window's permissions is a large change. Frontend code that calls `window.__TAURI__` globals with no typed invoke contract has skipped the plan. A one-file fix may ship with its requirements and a deferred matrix when the deferral is logged. A requirement-to-test traceability percentage can be raised by writing vaguer requirements, so read the requirements along with the number. Permission-denied defects tend to appear only in packaged builds; when one does, reopen the capability decisions.

A permission failure often surfaces in the webview as a generic runtime error, and two boundary failures can hide each other. Catch a capability gap in a mocked-IPC test before packaging; a user crash report is the wrong place to learn of it. The other Tauri failure classes to check for are payload drift between the frontend and a command, a sidecar that fails with nothing supervising it, and a broken single-instance handoff. While any gate is red, stop new implementation, and resume when the blocking evidence is recorded green; elapsed time does not release the stop. Classify a failure before any retry. Allow one rerun only for a transient cause or stale evidence. Three silent reruns of a failing clippy gate is the bad case. A desktop-boundary test that looks flaky may be retried once with a note that flakiness is still a guess. A contradiction between requirements is escalated, not retried. Write each record at the stage that produced it (sources at load, layer decisions at design, matrix and gate results at verification) and end with a short note of skipped gates and open risks; a record rebuilt at the end of a session forgets what was skipped. Signs that one plan has outgrown itself are a growing number of window labels and capability files, more sidecars, behavior that differs by platform, and store-distribution requirements. At that point split the work by window or capability domain and add a dedicated security review.

Choose the work mode before writing requirements; requirements written first with a mode fitted afterwards usually mismatch the design split. A requirement can wear the WHEN-THEN-SHALL shape and still say nothing checkable ("SHALL be more reliable"); the metric column exposes it. When a requirement is rejected as vague, renegotiate it with the requester. Do not quietly reword it yourself, for example "safer" into "robust". A threshold you had to guess is marked as estimated until the requester confirms it. Ask the performance question while writing requirements and record either a threshold or a deliberate waiver, because with no stated threshold no test guards speed. Async commands and payload routing still apply without one.

Match each test to the boundary where the risk lives. Passing frontend tests do not certify the IPC contract, which is why the typed invoke contract check is its own row in the mix, and a permission-scoping requirement proved only by unit tests is tested at the wrong boundary. Every test id in the matrix resolves to a real test. Keep a command a thin adapter over a tested core when it holds real logic, so the core can be tested without a desktop runtime; a trivial command gains nothing from the extra layer.

Write one plan per request; coupled changes may share one when the coupling is named. A plan rejected at review goes back to the step that failed (a vague requirement to the requirements step, an incoherent design to the design step) and is not patched at the surface. Record each gate's own result, not "all green". Many open questions are honest when they truly block and a warning when they were decidable; no open questions on every plan is a warning too. A question answered after handoff goes into a dated revision of the plan, not a verbal amendment.

When a request would weaken permissions or lifecycle safety, do not simply comply: pause, say what it weakens, and propose the least-privilege version. Keep a repo's established permission model or plugin stack unless it is broader than needed. That exception allows tightening only; never widen an existing scheme to match an example. A half-adopted permission scheme is not an established model to keep, and replacing ad hoc plugin bridging with official plugins is argued for, not assumed.

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

**Managed state is keyed by type.** Tauri's state manager looks state up by `TypeId`, so only one value of each concrete type can be managed.

```rust
struct PrimaryDb(Pool);
struct AuditDb(Pool);

app.manage(PrimaryDb(primary));
app.manage(AuditDb(audit));

#[tauri::command]
fn audit_count(db: tauri::State<'_, AuditDb>) -> Result<u64, String> { /* ... */ }
```

- Wrap two values of the same type in distinct newtypes.
- A command that asks for unmanaged state fails at call time, so register all state before any command can run, and test the missing-state path.
- Shared mutable state is wrapped explicitly in a `Mutex`, `RwLock` or atomic. Do not hand-roll a type map with `unsafe` downcasts.
- A plugin composes its optional lifecycle hooks (`setup`, `on_navigation`, `on_page_load`, `on_event`) through `tauri::plugin::Builder`. The `setup` hook returns a `Result`, and its error aborts start-up.

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
- Mocks left in place after a test let later tests pass against stale handlers; that is what the `clearMocks()` call prevents.
- The mock handler checks the command name and returns data in the shape the real command serializes, so the test pins the invoke contract. Returning an object where the command returns a JSON string changes the contract under test without anyone noticing.
- Test both ends of a changed boundary. Green frontend mocks can sit over a broken backend, and green Rust tests can sit under a drifted invoke contract. A backend-only refactor with an unchanged contract may skip the mocked layer when that is recorded.
- When a contract change lands on both ends but not in the mocks, the app works and the mocked suite fails; update the stale mocks, the code has not regressed. Mocks kept only for the riskiest commands are acceptable when the partial coverage is stated.
- Treat the mocking imports and the platform support list as version-dependent: check them against the docs for the project's Tauri version before relying on them.

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

These checks apply at design time. A new command lands with its typed boundary test in the same change, with no plan to backfill, so test coverage grows with the IPC surface. The mock preference has a limit: lifecycle behavior (tray, updater, single-instance, deep links) often cannot be mocked faithfully, so when a deep-link handoff is tested only in mocks, record that trade. Read the relevant Tauri patterns before committing to structure (async boundary, IPC transport, process supervision) and note which pattern forced which choice; a feature that meets these rules for the first time at review turns each violation into a rewrite. The trade-offs are decided by an observable condition: mutex flavor by whether the guard crosses `.await`, events or channels by stream volume and duration, store or files by payload size, mock or integration by runtime weight. Start on the cheap side and move only when the condition is observed and recorded; do not shrink a volume estimate to keep the cheap tool. A non-negotiable is fixed, not excepted: an unrecorded team habit such as "owned inputs are optional for internal commands" is a shadow rule nobody reviewed. A temporary exception during a migration is acceptable when it is dated, recorded and expires. In example code, a `sleep` inside an async command stands in for real I/O and is not a pattern to copy.

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

These checks are unconditional and come before tool output. A Tauri app is a web frontend holding OS-level power through IPC, so its typical failures are at that boundary: permissions granted too widely, a blocked runtime, a command that panics. Clippy and `cargo test` do not see them. Green cargo gates are required and not sufficient: fail a review for a broad shell or filesystem grant even when every command passes. Rules phrased "verify no ..." are gates; rules phrased "use when feasible" (naming, diagram style) are local conventions and never block delivery. Apply this gate list at the end of the work, after the design is settled; do not start a design from it.

Alongside the Rust command gates, run the repo's frontend and Tauri checks for the changed boundary. Use the repo's actual package manager and scripts; for example:

```bash
pnpm test
pnpm build
pnpm tauri build
```

Run both command families in CI and spend review time on the inspection checks. The bundle build is the slowest command and the first one skipped: a nightly run is an acceptable compromise when it is written down, but trimming flags to fit a CI budget changes the gate. Copy commands with their flags intact, since a command without `--all-features` or `-D warnings` looks the same in a skim and checks less. `--all-features` can interact with feature-gated Tauri plugins, so use the project's feature matrix where features conflict.

A failed gate is information. Rerun only after something changed, and record what changed (a dependency cache clear counts). Do not answer a red lint with an `#[allow]` or a failed bundle by dropping the command. Fix a flaky frontend test instead of rerunning it, because rerun-until-green teaches the team to distrust the gate. The same check failing across several changes points to a gap earlier in the work (design guidance, onboarding), not to a check that should be loosened.

Desktop logs live on the user's machine and cannot be recalled, so check logging by absence: read the output of the release configuration (debug builds log more than what ships) for tokens, payloads and paths. Log-everything-and-filter-later is a server habit and does not fit here. Performance is gated by structure before any benchmark: no blocking work in an async command, channels or binary responses for high volume, the store only for small structured state, bounded sidecar waits. Each one limits how much work can load one shared resource (the runtime, the IPC channel, the store, the startup path), and for a new case ask which shared resource the change loads without a bound. A benchmark at test volume passes an event-per-row progress stream that collapses at user volume. `spawn_blocking` keeps the runtime responsive and does not make the work fast. Where events are used for a small stream, record the bound assumed. In a multi-window app, review capabilities per window label. Keep project-specific lessons in the project's own review record; a gate list that collects them grows until people route around it.

No operator watches a user's machine, so a desktop app supervises its own children: sidecars, setup tasks and update flows. Logs are capped at the source because nobody rotates them on a user's disk. A bounded startup wait is a timeout on a polled readiness condition; a fixed sleep is not a bound. An async command protects the runtime and not the wall clock: one that runs for a minute still needs channel progress, since responsiveness and completion time are separate budgets. Choose the lane for each payload at design time by size: small structured data through the store and events, sustained streams through channels, large binaries through binary responses or files. An export, for example, keeps metadata in the store, sends progress on a channel and hands the archive over as a file path. A million-row result serialized through a JSON invoke "because it worked in testing" is the typical failure. Measure after the lanes are right. For plugin-author internals and mobile-only APIs this guidance has nothing to say; say so, and do not stretch the desktop capability patterns to them by analogy.

### Tauri release readiness checklist

- [ ] Requirements are executable and measurable.
- [ ] Each `REQ-TAURI-*` has at least one linked test.
- [ ] Command, IPC and UI-state behavior are covered at the right boundary.
- [ ] Capability, filesystem, plugin, sidecar and lifecycle choices are explicit.
- [ ] Rust quality gates pass.
- [ ] Repo-normal frontend or desktop checks pass for the changed surface.

The gate reads only the artifact: code, capability files, configuration and docs. Intentions are not inputs, so the walk works across a handoff where the closing reviewer lacks the author's context. Tick an item only against something checkable (a linked test, a command log, a capability file) and leave that evidence per section, with a reason for each waived convention; a ticked list with no linked tests is not a pass. If the commands could not be run, say the review was inspection-only. Scale the walk to the changed boundary: a docs-only change can skip the bundle build with the reason recorded. A sidecar change is the longest walk: check supervision, bounded startup, permission scope and the packaging declaration separately. Gate rules name Tauri 2 mechanisms (capability syntax, channels, the store plugin, the updater), so keep the intent and check the mechanism against the project's Tauri version.

For a case no rule lists, ask how costly the choice is to undo. Freely reversible choices (naming, diagram style) are conventions: follow them when feasible and waive them with a reason, for example keeping an old command identifier while renaming internals. Exposure that outlives the change (a granted permission, a panic in a shipped command, a blocked runtime) is a gate and is never waived: a waived no-`unwrap` check is a failure. Events versus channels is decided by payload volume, and the store plugin versus real storage by data size. Use the narrowest mutex that fits the access pattern; an async mutex is the right choice only where a guard has to live across `.await`. Signs that the gate is eroding: a waiver on a verification row, or a clippy run with `--all-targets --all-features` or `-D warnings` trimmed for speed. Repeated waivers of one convention mean it does not fit the project, so amend it locally.

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
# deny.toml
[licenses]
allow = ["MIT", "Apache-2.0"]

[advisories]
db-path = "~/.cargo/advisory-db"
```

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

Workspace hygiene:

- Declare dependency versions once at the workspace root and inherit them in member crates; use path dependencies between local crates.
- Share common types through one workspace crate.
- Keep optional dependencies behind features, grouped by feature set.
- Re-export the public API from `lib.rs`.
- Run `cargo clean` after a major dependency or workspace-configuration change, or when build errors make no sense, before trusting a critical test run.

- **Protocol on stdout, logs on stderr.** A binary that speaks a protocol over stdout (JSON lines, LSP, MCP stdio) sends `tracing` output to stderr and never calls `println!` for diagnostics. A helper daemon started detached gets a health check before spawning and cleanup of stale instances.
- **Fallback ladders.** When there are several ways to obtain a dependency (installed, then vendored build), use a fixed order, log each fallback, and surface an unavailable option. Building at load time is slow and surprising in production; an automatic download needs a single retry limit and a pinned checksum, and is off in offline or reproducible builds.
- **Cargo-integrated analysis tools.** Run ordinary `cargo check` with the tool re-entered as `RUSTC_WRAPPER`, pass the tool's own arguments serialized in one environment variable with a versioned format, detect an existing wrapper such as `sccache`, and apply a timeout to the child process.
- **Accumulating validation.** For intake, registries and admin tools where a complete fix list helps, collect issues with field, message and severity and report them together; the input is invalid only when an error-severity issue exists. Keep hot paths fail-fast.
- **One source for schema, type and validation.** Derive the runtime validation, the Rust type and the advertised schema from one definition (for example `serde` plus `schemars`), so they cannot drift.
- **Diagnostic log for a desktop or local app.** Append-only JSON lines with typed entries (RFC 3339 timestamp, level enum, event, command, message, error code). Redact on write and again on export, and add a test for every credential shape; redaction is a second line of defence, not permission to log secrets.

- **Command registries.** When the argument parser does not already give you the tree, one command trait carries name, description, usage, aliases and `execute`; the registry is a case-insensitive map that rejects a duplicate name or alias at registration, and no other code dispatches on strings. In a first-match table the order is the priority and a catch-all last entry sends unknown input into the normal error flow; an earlier broad matcher shadows later ones, so test each new matcher with varied whitespace and case.
- **REPL input buffering.** Track only the lexical state needed to know when a statement ends (comments, quotes, escapes, the awaited closing delimiter), recognise meta-commands only before a statement has started, and leave validation to the real parser. Test terminators inside comments and quotes, escaped quotes and unterminated text.
- **Caching external responses in a test harness.** Normalise volatile fields (ids, timestamps) at the adapter before caching so keys and values are deterministic, and keep a bypass for live runs.
- **Multi-stage ranking or routing.** Keep each stage's score and timing as separate fields in the result, and compute an explanation with the same function production uses, not a copy. Test stage scores, final order and the timing fields, not only the top result.

**Feature flags and plugin registration.**
- Read feature flags through one helper with a declared default per flag; a missing key must never silently read as `false`. Business logic does not look flags up in raw configuration. Each flag has an owner and a removal plan.
- Self-registering plugin lists (`inventory`, `linkme`, `ctor`) depend on link order and can register twice. Prefer an explicit registration list, and test that every plugin sets its selector.

**Feature-gate composition in one pure function.** When several flags combine into one behaviour, a single pure function maps the flag set to a mode enum (`fn exec_mode(features: &Features) -> ExecMode { Disabled | Fork | Direct }`); a dependent flag is never silently enabled by another. Call sites match on the mode and never call `features.enabled(..)` themselves. A new gate extends the function and its tests, which cover the flag combinations.

**Policy routed through a typed caller identity.** Behaviour that depends on who is calling matches exhaustively on a source enum, with no wildcard arm, so a new source forces a deliberate decision about which behaviour it inherits:

```rust
fn hint_for_source<'a>(cfg: &'a Config, source: &SessionSource) -> Option<&'a str> {
    match source {
        SessionSource::SubAgent(SubAgentSource::ThreadSpawn { .. }) => cfg.subagent_hint.as_deref(),
        SessionSource::Cli | SessionSource::VSCode | SessionSource::Exec => cfg.root_hint.as_deref(),
        SessionSource::Internal(_) | SessionSource::SubAgent(_) => None,
    }
}
```

**Searchable tool metadata apart from the loadable definition.** When many tools exist but few should enter a model's context, index a light search record per tool (name, description, parameter descriptions) and load the full definition only on demand; drop output schemas from the search payload and exclude tool kinds that must not be searchable. The names and descriptions must contain the words a caller would search for, or the tool is undiscoverable. Not for a small fixed tool set.

**Framed binary protocols.** One `write_message(code, len, |w| payload)` and `read_message(expected_codes, |kind, len| payload)` pair owns the type byte, the length, validation of the expected type, logging, flushing and error handling; each message supplies only its payload. The payload code must consume exactly the declared length or the stream loses alignment, so check the remaining count after the callback. A new message goes through the helpers and never writes to the channel directly. Not when a generated codec owns framing.

**Request types and executors.** In a command protocol with many request types, each request owns its encoding, decoding, command code and response type (`trait Request { type Response; const COMMAND: u8; fn write(..); fn read(..); }`), and semantic handling is a separate executor trait with one method per request, or an exhaustive match over a request enum. Client and server can then have different executors, and there are no downcast chains. Adding a command touches request, response and executor in one change.

**Telemetry providers and spawned-resource registries.**
- Telemetry providers are a `Vec<Box<dyn Provider>>` built from a config enum (one variant per provider plus a no-op). A provider that fails to construct is logged and skipped, an empty list gets the no-op provider, and each call is isolated so one failing provider never breaks the product or the other providers. A new telemetry feature is added to the trait once, with a default no-op body.
- Spawned child processes and background tasks are registered in one process-wide registry so shutdown can terminate all of them. Each handle unregisters itself through an idempotent helper (a registered flag, or `Drop`), so repeated exit paths cannot double-clean. Every launch path registers and every exit path (success, error, cancellation, timeout) unregisters, with tests for the cancellation and error exits.
- Instrumentation separates the observation payload (a context struct with the operation's data) from the naming convention (a trait returning the metric name, low-cardinality tags and high-cardinality tags). High-cardinality values such as query text and parameters are opt-in.

**Transparent proxy around a subprocess protocol.** A proxy between a caller and a tool can add a transcript log, per-command timing, stderr forwarding and optional policy checks without changing either side: read one command, log it, write it to the child's stdin and flush, read the response, log the elapsed time, write the response through unchanged, then run the check. A cheap frame delimiter (newline, balanced parentheses) is enough only for simple text protocols, and breaks when the delimiter can appear inside string literals; binary or streaming protocols need a real framing parser. The proxy's own diagnostics go to the log or stderr, never into the protocol stream.

**Prerequisite-gated tool servers.** When tools need a prerequisite (a built index, a login, a migration), gate every tool by default and exempt only an explicit allowlist of tools proven not to need it (init, reindex, doctor, catalog). A missing prerequisite returns at once a structured error envelope (`{ command, is_error: true, status: "index_not_built", next_command, retry_after_seconds }`) that tells the caller exactly what to run next, instead of hanging, timing out or returning empty output. A new tool is assumed to need the prerequisite, and the allowlist has a preflight test. Not when the prerequisite is cheap and safe to create automatically.

**Static drift audits of registered surfaces.** Audits of commands, routes, tools and migrations read the source statically (`syn`, or the registry constant) instead of starting the server, and keep the raw list long enough to fail on duplicates before deduplicating; collecting straight into a `HashSet` hides a duplicate registration. Traversal helpers are separate from reporting. Static readers miss plugins registered at run time, which need a separate dynamic audit.

**Maintenance scripts.** Discover the valid set of targets from the filesystem (directories that actually exist) plus a small explicit alias table, not a hand-kept list that drifts. Validate the user-supplied name against the discovered set before touching git or files, which also rejects path traversal and typos. Test direct names, aliases, missing paired directories and invalid names against a fake directory tree.

**Agent loops and query rewriting.**
- An agent search loop has explicit budgets (maximum depth per chain, maximum model calls, total tokens), explicit terminal and give-up states as a typed enum, and keeps failed trajectories for analysis. A regression fixture checks call count, tokens, terminal nodes, give-up nodes and depth pruning.
- A loop ends through an explicit finish tool whose argument is a typed outcome (`enum ReturnType { GiveAnswer, GiveUpAndRestart }` plus an optional final answer), not by parsing free text. An invalid finish call is an input error, never a silent success, and every outcome path is tested.
- When a model rewrites or splits a query into phrases, always keep the search on the original prompt as the baseline. Per item keep the best phrase score, multiply phrase-only hits by a discount, then merge; drop very short phrases. Tests cover phrase-only hits, duplicates and the discount.
- A retrieval benchmark keeps four separate steps (candidate generation, result serialisation as `results[query_id][doc_id] = score`, relevance-judgement construction, metric evaluation) so a retriever can be swapped without changing the contract.

**Plan runners, routing and auxiliary ranking channels.**
- A runner for a precomputed linear plan takes the side-effecting tool call as an injected trait or closure and emits a typed event for every transition through an iterator, stream or channel, independent of transport:

```rust
enum PlanEvent {
    PlanStarted { plan_id: PlanId, goal: String, step_count: usize },
    StepCompleted { step_id: StepId, tool: String, output_preview: String },
    StepFailed { step_id: StepId, tool: String, error: String },
    PlanAborted { plan_id: PlanId, failed_step: StepId, error: String },
    PlanCompleted,
}
```

- Argument-binding errors are a distinct kind from tool errors, and output previews are length-capped. Extend semantics by adding event variants, never by changing existing ones. Not for plans that need replanning, fan-out or conditionals.
- Intent routing is four separate stages: vector search, score aggregation per route, threshold gating (a per-route threshold overrides the global one), then argument extraction for routes that carry a function schema. A threshold is `Option<f32>`, so `0.0` and "no threshold" are different values.
- When ranking has an auxiliary channel (graph neighbours), fuse the primary channels by weight first, then inject auxiliary-only candidates below the weakest primary result instead of fusing them as an equal channel. The auxiliary channel then adds recall without displacing primary evidence. Keep a per-channel score breakdown and test exact-match queries separately from relationship-heavy ones.
- A tool's schema declaration and its handler are separate: the schema list stays close to product language and the handler sits behind a small trait with `execute(arguments)`. An unknown tool name is an explicit error.
- A row or size cap is applied before stringification. The truncation provenance (the original row count) travels with the data value itself, not through a side channel, later transformations preserve it, and the human-readable warning is produced from it at the end. Tests cover under the limit, over the limit and an invalid limit setting.

**Binary handshakes and chunked framing.**
- A fixed-size opening frame (magic bytes, then a fixed number of version proposals, answered with the one chosen version or all zeros for none) keeps old clients working. One reserved proposal value is an escape into an extensible manifest exchange that can advertise version ranges and capabilities; treat that marker as a protocol value, never as an ordinary version number. Test all-zero rejection, selection of the highest mutually supported version and manifest acceptance. Not needed where a standard negotiator (TLS ALPN, HTTP content negotiation) is available.
- In chunked framing, each chunk is a two-byte big-endian length followed by that many bytes, and a message ends with a zero-length chunk. Transport framing is separate from payload parsing, so the receiver recovers exact message boundaries, can skip or quarantine an unknown message, and the sender need not know the total size up front. An empty chunk has protocol meaning, so keep-alive handling must not be confused with end-of-message. Decoder tests: a single chunk, several chunks, two messages back to back, the zero-length marker, and input split at every byte boundary.

**Context compaction and repair inputs for agent tooling.**
- To compact history, summarise the older head and keep the recent tail verbatim (a tail budget of about half the limit), recursing only if summary plus tail still exceeds the limit, with a depth guard. The summary preserves file paths, decisions, commands and unresolved constraints. Not when exact earlier wording must stay verbatim.
- A tool failure handed to an automated repair step is a small typed result (`struct LintResult { text: String, lines: Vec<usize> }`), and one common wrapper attaches a bounded source window around the reported lines and owns the wording. Each new linter only returns the typed result. Too much context dilutes the target; too little makes syntax errors ambiguous.

**Keep a syntax-tree probe beside parser-backed features.** A tiny CLI that prints the syntax tree of a file (`println!("{}", tree.root_node().to_sexp())`, with the language chosen by a `clap::ValueEnum`) lets every query capture and tree walker be grounded in node shapes observed on representative snippets, never guessed. The printed tree is a diagnostic surface, not a stable API. `unwrap` and `expect` are tolerable in such a probe but not in a user-facing batch tool.

**Context and report packers.** Fill a token or byte budget in priority bands: cap the summary band and reserve a minimum for primary evidence, so summaries cannot starve code evidence. At emission time re-hash each snippet's source range and skip any whose hash no longer matches the stored anchor; stale evidence is worse than none. Record which sections were omitted so the consumer knows what it did not see. The ratios are policy knobs, not constants, and token estimates are approximate, so leave headroom. Hand-tuned ranking weights overfit one repository shape, so return the rank-signal breakdown as debug metadata.

**Agent-facing tool guardrails.** Size limits are named constants with a soft cap (truncate and say so) and a hard cap (refuse), and list-returning tools have a default limit:

```rust
pub(crate) const READ_FILE_SOFT_CAP_LINES: usize = 5_000;
pub(crate) const READ_FILE_SOFT_CAP_BYTES: usize = 500 * 1024;
pub(crate) const READ_FILE_HARD_CAP_BYTES: usize = 2 * 1024 * 1024;
pub(crate) const CALL_GRAPH_DEFAULT_LIMIT: usize = 200;
```

Every tool starts with a readiness check that returns a status payload when its index is missing, stale or still building. An empty result is a first-class response carrying a hint about what to try next (another tool, a broader query), tested as carefully as a success. Failures are shaped as guidance: readiness, truncation, totals and a suggested next tool. Caps are configurable for administrative use, and hints must not be so prescriptive that they steer callers away from valid paths.

**Local environment launcher.** Split "what service is this" from "how services are started, logged, checked and stopped".

```rust
pub trait Task: 'static + Send {
    fn execute(&mut self, ctx: &mut ExecuteContext<impl std::io::Write>) -> anyhow::Result<()>;
    fn id(&self) -> String {
        "<task>".into()
    }
}

pub trait DockerServiceConfig: Send + 'static {
    fn id(&self) -> String;
    fn is_user_managed(&self) -> bool;
    fn image(&self) -> String;
    fn ports(&self) -> Vec<(String, String)> {
        vec![]
    }
}
```

- A new service implements the small config trait and composes the existing readiness-check tasks before any bespoke orchestration.
- Shared task mechanics own logs, progress, container lifecycle and the TCP readiness check.
- Command construction and environment variables are heavy with side effects, so keep a seam around command execution for tests.

**Dependency boundaries as lint rules.** Encode a boundary as a lint with an actionable replacement message.

```toml
# clippy.toml
disallowed-methods = [
    { path = "std::process::Command::new", reason = "use crate::exec::run_command (sandboxed, logged)" },
]
```

- Deny `clippy::disallowed_methods` at the crate root. The wrapper module carries the only `#[allow]`.
- Add the rule and its recommended alternative before refactoring callers, and add no rule until the replacement API is mature.
- Keep exceptions few and justified.

**Agent tool routing.**

- With a large tool catalog grouped by server, retrieve in two stages: rank servers, then rank tools only inside the matched servers. Combine the two scores with one explicit formula.
- The handoff from model output to the router is a parsed contract. Malformed output is a typed "no parse" result, distinct from "no match".
- Routing heuristics are pure functions such as `fn detect_signals(task: &str) -> TaskSignals`. Keywords match on word boundaries (`\b` with `regex::escape`, compiled once in a `LazyLock`), so `class` does not match `classification`. Every keyword has one positive test and one near-miss negative test.
- Historical memory is a bounded hint, never a dependency of a latency-sensitive handler. The lookup runs under `tokio::time::timeout`, and a miss or timeout yields `None`.
- Advice from memory is used only above a sample floor (`const MIN_SAMPLES: usize = 3`) and a success threshold. Both are named constants covered by tests.
- Derive a tool's schema from its typed argument struct (`schemars::JsonSchema`, doc comments as parameter descriptions) and prebind runtime-only dependencies, so the model sees only user-relevant parameters. A test inspects the generated schema.
- A flat nearest-neighbour search is fine for a tiny catalog, and deterministic policy rules win over similarity.

**Timed child process without pipe deadlock.** A parent that waits for exit before draining full stdout and stderr pipes deadlocks. Drain both pipes concurrently while waiting.

```rust
let stdout_pipe = child.stdout.take();
let stdout_thread = std::thread::spawn(move || {
    let mut buf = Vec::new();
    if let Some(mut pipe) = stdout_pipe {
        let _ = pipe.read_to_end(&mut buf);
    }
    buf
});
// The same for stderr.

match child.wait_timeout(timeout)? {
    Some(status) => Ok(TimedOutput::Finished(Output { status, stdout, stderr })),
    None => {
        let _ = child.kill();
        let _ = child.wait();
        Ok(TimedOutput::TimedOut { stdout, stderr })
    }
}
```

- One shared wrapper owns the child's lifecycle and pipes. Every external CLI call goes through it.
- The timeout outcome is data, with partial output kept. On timeout, kill and then wait, so the child is reaped.
- The drain threads buffer everything, so cap captured output for noisy or hostile tools.
- Tests cover timeout, non-zero exit and large stdout and stderr.
- This is not for interactive or long-lived children.

**Agent edit tools.**

- An edit-context tool returns the target symbol's code, signatures of called dependencies, relevant imports and types, ordered by edit utility and serialised compactly. It enforces a hard token budget before returning (`enforce_budget(&mut out, max_tokens)?`), trimming the lowest-priority fields first.
- Before editing, check that the types the edit needs are present in the returned context.
- After a patch, a structural diff lists the changed symbols, confirms the intended symbol changed, and reports every unexpected one. It is paired with tests or a build, because structure does not prove behaviour.
- A codebase scanner layers ignore policy in a documented order: built-in defaults, the tool-local ignore file, then the project ignore file (`ignore::WalkBuilder`). It reports the active ignore sources before scanning and offers an explicit include override for audits.
- Dense per-character metadata over a large text is stored as run-length ranges in a rope or balanced tree, never one object per character. An update replaces the affected runs, coalesces equal neighbours and invalidates derived caches.
- An editor with injected language layers applies queued edits to an isolated copy of parser state per layer, removes a layer whose ranges become empty, returns only the union of invalidated byte ranges, and supports cancellation and a parser timeout.
- A repair pass at an ingestion boundary (canonical IDs, normalised values, rewritten edges, dropped dangling references) returns counts and reasons. It does not hide a violation that should fail hard.
- Parse-tree consumers read named fields (`node.child_by_field_name("tag_name")`), not child positions. Keyword case is normalised once at the lexer boundary.

**Classify a failure before retrying it.** CI retry automation decides first whether a failure is transient, and "deterministic" is the default.

```rust
const MAX_CLASSIFY_INPUT_SIZE: usize = 1024 * 1024;

pub fn classify_failure(output: &str) -> FlakeClassification {
    let mut end = output.len().min(MAX_CLASSIFY_INPUT_SIZE);
    while !output.is_char_boundary(end) {
        end -= 1; // slicing at an arbitrary byte can panic inside a multi-byte character
    }
    for line in output[..end].lines() {
        let line = line.trim().to_lowercase();
        if line.contains("eaddrinuse") || line.contains("address already in use") {
            return FlakeClassification::Transient {
                category: FlakeCategory::PortConflict,
                matched_line: line,
            };
        }
    }
    FlakeClassification::Deterministic
}
```

- Only a named transient category retries, under a capped policy, and each retry logs an event with the matched line.
- Each category has a positive and a negative fixture.
- Do not add a classifier while the flake taxonomy is immature. It masks regressions.

**Integration metadata in one table.** IDs, aliases, credential environment keys, routing defaults and required tests for each integration live in one `const` table, not in conditionals spread through the code.

```rust
pub struct ProviderMetadata {
    pub canonical_id: &'static str,
    pub aliases: &'static [&'static str],
    pub auth_env_keys: &'static [&'static str],
    pub routing_defaults: Option<ProviderRoutingDefaults>,
    pub test_obligations: ProviderTestObligations,
}

pub const PROVIDER_METADATA: &[ProviderMetadata] = &[/* one entry per provider */];
```

- Adding an integration starts with the table entry; authentication, defaults, aliases and tests are routed through it.
- A test checks that IDs and aliases are unique and that every entry's test obligations are met.
- A static table lags fast-changing providers and does not fit runtime plugin registration.

**Telemetry names are an API.** Cross-cutting attribute keys, propagation environment names, span kinds and status codes are constants in one vocabulary module shared by traces, metrics and logs across crates.

```rust
pub struct SpanAttribute;

impl SpanAttribute {
    pub const RETRY_ATTEMPT: &'static str = "retry.attempt";
    pub const EXECUTION_JOB_ID: &'static str = "execution.job.id";
    pub const SESSION_ID: &'static str = "session.id";
}
```

- Before adding a key, search that module, and extend it there when the key is cross-cutting or shown on a dashboard. One-off debug labels stay local.
- Give the module naming rules and an owner, or it becomes a dumping ground.

**Stdout is data, stderr is diagnostics.** When a child process's stdio is an RPC transport, stdout carries framed protocol messages only and stderr carries structured log records, with a plain-text fallback for lines that do not parse.

- One stray print to stdout corrupts the protocol. Configure the child's logger for stderr and deny `clippy::print_stdout` in that crate.
- Each direction (stdin writer, stdout reader, stderr reader) is its own task.
- Use a socket or a pipe when stdout must stay user-facing.

**Resolve resource locations before entering a sandbox.** Resolve and cache filesystem locations before dropping privileges, then derive the sandbox access list from the same function.

- Discovery is centralised. A new resource location updates the access list in the same change.
- Development-only fallbacks, such as scanning the working directory, stay behind a non-production guard.

**Structure-aware context excerpts.** Context for a model or an edit is expanded with the enclosing signature and closing lines from the file outline, not with arbitrary line padding. Clip to whole lines, merge overlapping ranges, and order them deterministically.

- The directly requested range is always kept, even when outline data is missing or wrong.
- Do not use excerpts for an exact refactor, where an omitted body hides a dependency.

**Build-time registries and a committed public surface.**

- When the source tree already holds the truth, registry bookkeeping moves to build time (the `inventory` or `linkme` crates, a build script or a derive). Sort generated registry output so diffs stay reviewable. Runtime plugin loading keeps a runtime registry.
- Commit the public API as a golden file. CI regenerates it (`cargo public-api`), normalises line endings, fails with a diff, and an explicit command overwrites it. The regenerated diff is reviewed, never edited by hand.

**Symlink-safe recursive traversal.** A recursive workspace walk tracks the canonical identity (`fs::canonicalize`) of each directory on the current ancestor path in a `HashSet`.

- A broken link is skipped with a warning. A directory already on the path is a symlink cycle and is skipped.
- Remove the entry when the directory is finished, so a sibling branch can still reach a shared target.
- Pair the walk with include and exclude tests, and with cancellation and progress for long walks. `walkdir` with `follow_links(true)` detects loops itself.

**Ordered recognisers for a small markup pipeline.** Token precedence in a small markup or lexer pipeline can be an ordered list of recognisers ending in a catch-all, with input escaped before recognition and output behind an append-only sink. The order is behaviour: a new recogniser goes next to its most specific competitor, with regression tests that nothing earlier or later is shadowed. This does not fit a grammar that needs global context or backtracking.

**Build artifacts ship their metadata.** A build step that produces named artifacts emits serialised metadata (names, source file and line, attributes), so later driver phases filter, run and report without reparsing source or scraping command output.

- A new artifact kind extends the metadata first, then selection and reporting.
- Substring selection surprises when names overlap. Keep an exact mode, and make it the only mode for security-sensitive dispatch.

**Typed fail-fast in a parallel batch.** An early stop carries a typed payload (which unit failed and its full result) as a private error type.

```rust
let results = pool.install(|| {
    sorted_units
        .par_iter()
        .enumerate()
        .map(|(index, unit)| {
            let result = check(unit)?;
            if fail_fast && result.failed() {
                Err(anyhow::Error::new(FailFastInfo { index, result }))
            } else {
                Ok(UnitResult { unit, result })
            }
        })
        .collect::<anyhow::Result<Vec<_>>>() // short-circuits
});
```

- The orchestrator downcasts the payload and returns an ordinary result structure, so the fail-fast type never crosses the public API.
- Rayon cancellation is cooperative: units already running finish. Sort the inputs first so output order is deterministic.
- Do not use it when every failure must be reported or units have side effects that cannot be interrupted.

**Stackless walk of a large syntax tree.** Walk with an explicit cursor state machine (first child, else next sibling, else parent) instead of recursion, so deep input cannot overflow the stack.

```rust
let mut cursor = root.walk();
let (mut depth, mut child_done) = (0usize, false);
loop {
    if !child_done && cursor.goto_first_child() {
        depth += 1;
        visit(cursor.node());
    } else if cursor.goto_next_sibling() {
        child_done = false;
        visit(cursor.node());
    } else if depth > 0 {
        cursor.goto_parent();
        child_done = true;
        depth -= 1;
    } else {
        break;
    }
}
```

- Node offsets are bytes: take text with `&source[node.byte_range()]`, never with `chars().skip(node.start_byte())`.

**Budget gate, parallel-safety policy and command approval for agent loops.**

- A loop with several independent ceilings (tokens, turns, wall clock) checks all of them through one gate at the top of each iteration, before the next expensive call, and records usage at the single point where authoritative usage exists. Stop reasons are distinct enum variants (aborted, budget exhausted, error), so the caller knows whether to retry, resume or ask.
- Run a batch of actions concurrently only when a policy function proves every action is read-only. Otherwise run them serially in order. A tool declares its parallel safety when it is registered, and an unknown tool is treated as a write.
- Command auto-approval with allow and deny prefix lists first rejects syntax that can change a command's meaning (command substitution, backticks, process substitution), then resolves by specificity: the longest matching prefix wins, deny wins when no allow matches, and a wildcard allow loses to any deny match. Test each of those cases. Prefix policy is not adversarial shell parsing.
- Responses from a worker, subprocess or WASM boundary are untrusted frames. Wrap each request with a fresh random per-call token, set the token after copying the payload fields so the payload cannot overwrite it, and reject a response whose token is missing or different before reading anything else. The token proves correlation, not correctness: still validate fields and enforce a timeout.

**Locked commit of a small shared state file.** A JSON, config or state file shared by processes is replaced transactionally: take a file lock with a stale timeout and bounded retries, write the new content to a uniquely named temp file in the same directory, rename the old file to a backup, rename the temp file into place, clean up, release the lock. Never write the target in place. A rename across filesystems is not atomic, which is why the temp file sits in the same directory.

**Context assembly, artifacts and result caches for agent tooling.**

- Prompt or context assembly is a staged pipeline: candidates, dependency closure, sensitivity filter, firewall, score, deduplicate, then select and pack under the budget. Each stage returns its survivors and its drops. Stage order is semantic, and an accounting test asserts `included + dropped == total_candidates`.
- Long or sensitive tool output is stored out of band as a content-addressed artifact, and only a small scrubbed summary with the reference enters the prompt. The firewall is idempotent: an item that is already enveloped or already carries a content hash passes through unchanged. Deterministic mode fails closed when a summariser is model-backed.
- A cache of tool or API results stores only normalised, successful, policy-allowed calls. The key hashes the server, the tool and the canonically serialised parameters with sorted keys. Never cache errors, empty results, rate-limit pages, non-idempotent calls or personalised responses, and classify freshness per tool first. For multi-process use, SQLite runs in WAL mode with a busy timeout and one connection per thread or process.
- Retrieval over a large grouped catalog is two-stage: prune at the group level, then rank inside the surviving groups, with a combined score. Measure recall as well as precision, and keep fixtures for malformed input, missing or zero vectors and near ties.
- A deterministic evaluation sandbox versions state by the index of the event that produced it. State at a turn is the latest snapshot at or before that index (`BTreeMap::range(..=index).next_back()`), with an initial empty snapshot at index 0.
- Benchmark scenarios are a reusable base plus data-bearing extensions: messages, allowed and denied tools, milestones that must happen and actions that must not. Every rollout persists the final context, a readable transcript and the evaluation result, without sensitive data.
- The sessions of many external tool servers belong to one owning scope: connect and discover on entry, close all on exit even after a failure, through an explicit async `close()` on every path with `Drop` only as a backstop. A cleanup error is logged and never masks the task's own failure; a long-running host surfaces cleanup errors, because swallowed ones hide leaks.

**Helper captures are filtered at one extractor boundary.** A query language can mark scaffolding captures by a naming convention, such as a leading underscore.

- Compute the ignored capture indices once per query, not per match, and skip them where matches are extracted.
- Warn or fail when every capture is ignored. Empty output otherwise reads as "no matches".
- Tests prove that visible captures still carry text and positions.

**Ignore-aware parallel file discovery.** File discovery uses the `ignore` crate's `WalkBuilder`, so a tool sees the user's Git-visible files by default, with the ignore policy a first-class option.

```rust
let (root_sender, receiver) = crossbeam_channel::unbounded();
builder.git_ignore(opts.git_ignore).build_parallel().run(|| {
    let sender = root_sender.clone();
    Box::new(move |entry| match entry {
        Ok(entry) => match sender.send(Ok(entry)) {
            Ok(()) => ignore::WalkState::Continue,
            Err(_) => ignore::WalkState::Quit,
        },
        Err(err) => {
            let _ = sender.send(Err(err)); // report the walk error; receiver gone means we are stopping anyway
            ignore::WalkState::Quit
        }
    })
});
drop(root_sender); // or the drain below never ends
let mut entries: Vec<_> = receiver.iter().collect::<Result<_, _>>()?;
entries.sort_by(|a, b| a.path().cmp(b.path())); // parallel walk order is not deterministic
```

- The parallel walk only discovers and sends entries. Parsing happens afterwards.
- A security or audit scanner must be able to include ignored files.
- CLI transcript tests cover default ignore, no-gitignore and several roots.

**Binary-search the prefix that fits a token budget.** When a list is sorted by relevance and its rendered size grows with prefix length, binary-search the largest prefix whose rendered output fits.

- Count with the tokenizer production uses, never a character estimate.
- A ranked prefix can exclude a small crucial item, so explicit must-include anchors (files the user named) are placed first.
- Fixtures put the budget cut in the middle of a structured outline.

**A small combinator vocabulary before a large grammar.** Before writing a large parser (`nom`, `winnow`, `chumsky`, a tree-sitter grammar), define named combinators for the recurring shapes (separated list, delimited form, optional argument list, field-wrapped capture), so domain rules stay readable.

- Keep the helpers shallow. They can hide precedence, conflict and recovery behaviour, so forms with unique recovery or precedence stay hand-written.
- Each helper has a corpus fixture that exercises nesting and ambiguity.

**Deterministic arbitration of overlapping matches.** Overlapping rule matches on source (diagnostics, lenses, highlights) each claim a byte interval.

- Sort candidates by specificity descending, then claim width descending, then start ascending, which is a total order. Accept a candidate only if its interval overlaps no accepted claim and it renders successfully.
- A new rule states what it claims (a header or the whole subtree) and has an overlap test against a broader neighbour.
- Greedy selection can hide a more helpful match of lower specificity.

**Message keys in analysis, prose in catalogs.** Analysis returns a locale-independent message key with typed parameters, and a per-locale catalog layer renders the prose. A missing key is a hard error, a test asserts that every key exists in every required catalog, and rule code contains no hard-coded sentences.

**Partial context bundles say so.** A context bundle built from many optional sources (code, memory, documents, graph neighbours) hydrates each source independently. A failing source appends a labelled error and the rest still return.

- A source is recorded as used only after its data is present. The bundle renders its errors and provenance, so a partial bundle never looks complete.
- Do not return partial output where it is unsafe and every source must be present.
- Trimming a bundle to a token budget follows an explicit ladder ordered by regeneration cost and decision value, not by section order or size. Drop what can be fetched again first (call neighbours, then raw code), and keep facts that are expensive to recover (decisions, observations) longest. Recount tokens after each rung and stop as soon as it fits. A new section declares its rung and has a budget test for when it survives and when it drops.

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

- **Match the gate to the obligation.** `cargo check` alone proves nothing about behavior, `cargo test` alone proves nothing about concurrency, and Clippy is not design review. Compile a public-call fixture for an API claim, test each error variant, saturate the bounded channel, cancel the work. Where features are mutually exclusive, `--all-features` is invalid by design: run the intended feature matrix and record it. Also check workspace default members, feature unification, target-specific code and the MSRV toolchain.
- **Scale strictness to the code.** Public, concurrent and invariant-heavy code needs stronger explicit contracts than simple private glue. State what must be representable, borrowable, fallible, cancellable and testable before leaning on the compiler; otherwise compiler-driven churn becomes the architecture.

- **False proxies.** Zero Clippy warnings do not prove the design, fewer clones do not imply speed, and more traits do not imply testability. The useful signal is fewer surprises at boundaries: callers, errors, tasks and features behave as the design said they would.
- **Scope a change by contract crossings, not by size.** Count public items, downstream callers, error variants, spawned tasks, locks and channels, external effects, feature sets and MSRV targets. A small patch that changes a public enum, cancellation semantics or feature resolution needs the full gate; a broad rename can be reviewed as one unit once behavior and contracts are shown unchanged. Split a change by public API, runtime lifecycle, persistence effect, dependency layer or feature matrix.
- **Where a review misses callers and code.** Proc-macro expansion, build scripts, examples compiled as downstream crates, doctest features, hidden default features, transitive runtime dependencies, target-specific dependencies, callers outside the repository, and tests that run on a different runtime flavor.

- **When a change is too large for one review.** The measure is evidence closure: one owner can list the affected contracts and verify their callers, errors, task lifetimes, features and rollback. Line count is not the trigger. Split when that closure fails, along a service, runtime, public contract, migration phase, feature family or rollback unit, and keep one compatibility matrix and one integration owner across the slices. Couplings that defeat a split: shared types between nominally separate crates, build scripts crossing layers, feature unification, database migrations that outlive binaries, and a rollback order that differs from the deployment order.
- **Looking up current behavior.** Search by the exact obligation and the owning source ("lock guard across await" in the Tokio docs for the locked version), not by a general phrase. Open the source; a search snippet is not evidence. Version traps: stable versus nightly, Tokio major versions, Axum examples on unreleased branches, Cargo feature-resolver changes, deprecated Clippy lints, and an MSRV policy that is stricter than what the compiler accepts.

- **What a passing gate proves.** Each gate proves only its own contract, and completion is all of them together. A zero exit code can hide skipped or ignored tests, so read how many ran. Run the command from the workspace root you mean, and do not reuse an earlier result after the code changed. Where feasible, see a gate fail on the defect it guards before trusting its pass. If a tool such as Miri is unavailable, use a reviewed substitute and record the remaining risk, or report the gate as blocked; do not invent evidence.

- **Release-mode tests complement the debug run.** `cargo test --release` is not a superset of `cargo test`. Release mode removes debug assertions and overflow checks and changes optimization-dependent behavior, so the two runs catch different failures. Run both for a high-risk change; never replace the debug run with the release run.
- **Apply each gate in its phase.** The no-placeholder rule audits finished code, not the stub step of the test-first loop. Do not shape a design around tool gates before the requirements exist; the requirement-shaped rejections (ambiguous wording, claims with no threshold) apply from the first draft.

- **Sizing the gate set.** Keep the mandatory floor small and trigger the extras (release tests, coverage, `loom`, Miri) by risk. A coverage threshold is a team policy: justify the number locally and do not inherit one from a guide. Over-gating shows up as complaints, while under-gating is silent until an incident, so check now and then that the extra tier does run on high-risk changes. Moving an extra into the floor for a release-critical crate is fine when the reason is recorded with the change.

- **Design against the avoid-rules, review against the verify-checks.** The async rules run twice: as constraints while designing and as checks at review (no blocking work on the executor, no lock across `.await`, cancellation and timeouts handled, no secrets in logs). Run both phases. The timeout check asks whether a decision was made, so a documented unbounded wait passes; it does not mandate a value. Secret logging is a correctness gate, reviewed before shipping. When a check does not apply (secret logging in a pure computation crate), record that scoping call.
- **Performance claims at review.** Reject a claim with no test on the first read, and check again at release readiness that every claim has a threshold test. A benchmark and a contract test are different kinds of evidence, so record which one was accepted. A claim whose threshold sits near the noise needs release-mode evidence.
- **Gates across a workspace.** Run the command floor once at the workspace root and give a readiness verdict per crate. A workspace coverage number can hide one untested crate behind well-tested siblings, so read coverage per crate.

- **Keep rarely run gate commands working.** A gate that runs only on high-risk changes breaks when it is needed most. Test the exact flag combination (for example `cargo llvm-cov --workspace --branch --fail-under-lines N`) against the installed tool version; checking that the tool exists misses a flag that was renamed. A command copied from a guide has been read, not run, until it runs here.

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

- **Two gate layers.** The four commands are owed on every change. The heavier gates are owed by the boundary a change touches: `loom` for shared-state interleavings, Miri for unsafe, fuzzing for an input frontier, compile-fail for a misuse contract. They add up; neither replaces the other. A change that is never classified by boundary gets the four commands only, and that under-verifies exactly the concurrent, unsafe and FFI work that needs more.

## 17. Review checklist

Review in rejection-first order: read the diff for the fatal anti-patterns of section 13, then check that every requirement has a test, then run the tool gates, then check release readiness. The fatal read takes minutes and the gates cost tool runs, so do not spend a full gate run on a change a short read would reject. It is a pipeline, not a filter to stop at: a change that passes the first read still goes through every later step. Half of the fatal list is about requirements (ambiguous wording, unverified performance claims), so it applies to a one-line fix too.

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
