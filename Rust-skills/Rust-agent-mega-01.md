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

1. **Classify the task.** Name the component type first: library, CLI, async service, backend, parser or protocol, FFI wrapper, Tauri app, or review. Pick the primary work mode (section 2).
2. **Write executable requirements** (section 3). Reject vague claims such as "faster" or "more reliable" unless they carry a threshold.
3. **Define the architecture before coding** (section 4): layers, and trait seams where substitution or testability matters.
4. **Choose the verification mix deliberately** (section 5). Match tests to the real risk surface; do not default to unit tests only.
5. **Apply the reliability rules** (sections 6 to 10).
6. **Apply local conventions selectively** (section 12).
7. **Run quality gates and anti-pattern checks before handoff** (sections 13 and 16).

### Guardrails

- Keep invalid states unrepresentable where practical.
- Treat async, cancellation and concurrency as correctness problems, not only performance concerns.
- Do not force every repo-local convention onto every Rust task.
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
| L1 Core | Invariants, types, traits, protocol and state rules | What must stay runtime-agnostic and easy to trust? |
| L2 Std | Collections, ownership orchestration, iterator and sync composition | What belongs in Rust std without framework coupling? |
| L3 External | Runtime, database, HTTP, serialization, tracing, FFI adapters | What touches the outside world and should stay behind traits or adapters? |

- Keep L3 dependencies out of L1.
- Push validated types and invariants as low in the stack as practical.
- Add trait seams around time, randomness, storage, transport and runtime integration when substitution matters.

### Trait-first design

Define the trait before the concrete adapter when the task needs test doubles or integration seams, when public behavior should be settled before storage or transport details, or when infrastructure dependencies would otherwise leak into core logic.

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
- **VERIFY:** run all chosen gates and confirm requirement traceability.

Cover unit, integration, error-path and concurrency cases. Add performance tests only when a metric is specified.

In STUB, write one or more tests per requirement id and define the interface signatures and fixtures.

### Test matrix example

| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |
| REQ-RUST-001.0 | TEST-UNIT-001 | unit | filters only implementation entities | correctness |
| REQ-RUST-001.0 | TEST-INTEG-003 | integration | preserves order across parser and filter | correctness |
| REQ-RUST-001.0 | TEST-PERF-002 | perf | p99 < 500us for 10k entities | latency |
| REQ-RUST-001.0 | TEST-CONC-004 | concurrency | no race under 100 parallel tasks | safety |

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

## 6. Types and API design

- Prefer newtypes, explicit conversions, and designs that make invalid states unrepresentable.

- Accept `&[T]`, `&str` or `AsRef` in public APIs, not `&Vec<T>` or `&String`.
- Use newtypes for domain identifiers and invariants.

## 7. Ownership, borrowing and data handling

- Prefer expression-oriented style and iterators over mutable accumulator code.

## 8. Errors and recovery

- Keep library errors typed and boundary-aware.

- Use `thiserror` for library error enums and `anyhow` at application composition boundaries.
- No `unwrap` or `expect` in production paths.

## 9. Async and concurrency

- Never block inside async code, and never hold a lock guard across `.await`.
- Prefer bounded concurrency and cancellation-aware code.

## 10. Unsafe and FFI

- Keep unsafe surfaces minimal.

## 11. Performance

## 12. Naming, modules and documentation

- Use four-word names for new functions and commands when feasible.
- Preserve public API compatibility when a rename is risky.
- Keep modules cohesive and docs synchronized with behavior.

- Treat Mermaid diagrams as a documentation convention only when the project already expects them.

- Apply the same naming clarity to new crates, folders and top-level commands when creating or renaming them is practical.
- When an existing public API cannot be renamed, keep it and add an adapter.

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

## 14. Rust web backends

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
- Scope permissions by real window labels and concrete actions.
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

## 17. Review checklist

Questions to answer in any review or before handoff:

- Which mode or combination of modes is active?
- What is the smallest set of `REQ-RUST-*` contracts that makes the work testable?
- Which types and invariants belong in L1 instead of leaking into adapters?
- Which risk deserves doctest, compile-fail, property, fuzz, `loom` or `Miri` coverage?
- Which public names must stay stable even if a cleaner new alias exists?
