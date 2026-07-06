# Rust Executable Specs Reference

Use this file as the standalone reference behind `rust-executable-specs-01`.

It merges the strongest parts of:

- executable specs and TDD-first planning
- idiomatic Rust architecture with L1/L2/L3 boundaries
- reliability-first Rust delivery and review
- selective repo-local conventions such as four-word naming where feasible

## 1) Work Modes

| mode | use when | emphasis |
| --- | --- | --- |
| `Spec Mode` | Request is vague or not yet measurable | `REQ-RUST-*`, acceptance criteria, traceability |
| `Delivery Mode` | Work needs implementation structure | L1/L2/L3, traits, TDD order, decomposition |
| `Reliability Mode` | Main risk is correctness under stress or change | errors, async, concurrency, unsafe, FFI, release gates |
| `Review Mode` | Main task is critique or hardening | anti-patterns, diagnostics, semver, misuse resistance |

Default combinations:

- vague feature request -> `Spec Mode` + `Delivery Mode`
- library or API change -> `Spec Mode` + `Reliability Mode`
- async service or parser/protocol -> `Delivery Mode` + `Reliability Mode`
- code review or hardening pass -> `Review Mode` + `Reliability Mode`

## 2) Choose by Task Type

### Library or Public API

Prioritize:

- borrowed inputs and explicit conversions
- newtypes and invalid-states-unrepresentable design
- typed library errors
- semver-safe surface design
- doctest and compile-fail coverage for misuse contracts

### CLI or Binary

Prioritize:

- explicit requirement contracts for user-visible behavior
- actionable diagnostics
- `ExitCode` or equivalent boundary behavior
- integration tests and release gates

### Async Service or Backend

Prioritize:

- L1/L2/L3 separation
- typed boundary parsing and context layering
- no blocking and no lock guards across `.await`
- bounded concurrency, cancellation, and shutdown behavior
- stress, property, or `loom` coverage when shared state is involved

### Parser or Protocol Boundary

Prioritize:

- panic-free parsing and slicing
- binary-safe diagnostics for non-UTF-8 paths
- property tests, fuzzing, and round-trip guarantees
- explicit ownership and allocation choices

### FFI or Unsafe Boundary

Prioritize:

- minimal unsafe surface
- explicit invariant documentation
- layout, nullability, and unwind boundary discipline
- `Miri` or equivalent verification when possible

### Review or Hardening Pass

Prioritize:

- misuse resistance
- error surface clarity
- cancellation and lifecycle ownership
- anti-pattern detection
- final gate completeness

## 3) Requirement Contract Template

```markdown
### REQ-RUST-001.0: <short title>

**WHEN** <trigger or input condition>
**THEN** the system SHALL <primary behavior>
**AND** SHALL <secondary measurable behavior>
**SHALL** <edge-case or default behavior>
```

Rules:

- Keep each `SHALL` independently testable.
- Use explicit units for latency, memory, throughput, retries, or concurrency limits.
- Split requirements rather than stacking unrelated behavior into one clause.

## 4) Rust Design Scaffold

Plan the design before coding:

| layer | role | question |
| --- | --- | --- |
| `L1 Core` | invariants, types, traits, protocol/state rules | what must stay runtime-agnostic and easy to trust? |
| `L2 Std` | collections, ownership orchestration, iterator and sync composition | what belongs in Rust std without framework coupling? |
| `L3 External` | runtime, database, HTTP, serialization, tracing, FFI adapters | what touches the outside world and should stay behind traits/adapters? |

Planning rules:

- Keep L3 out of L1.
- Push validated types and invariants as low in the stack as practical.
- Add trait seams around time, randomness, storage, transport, and runtime integration when substitution matters.

## 5) Trait-First Template

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

Use trait-first design when:

- the task needs test doubles or integration seams
- the public behavior should be settled before storage or transport details
- infrastructure dependencies would otherwise leak into core logic

## 6) Verification Selection Matrix

| verification type | choose it when |
| --- | --- |
| unit | behavior is local and deterministic |
| integration | behavior crosses module or adapter boundaries |
| doctest | public examples are part of the contract |
| compile-fail | misuse contracts should fail at compile time |
| property | invariants or round trips matter more than examples |
| fuzz | parser, decoder, protocol, or input frontier is risky |
| `loom` | small concurrent state models need interleaving exploration |
| `Miri` | unsafe, aliasing, or UB-risking logic needs extra scrutiny |
| performance | latency or memory thresholds were explicitly stated |
| coverage | higher-risk changes need stronger release confidence |

## 7) TDD Loop

```text
STUB -> RED -> GREEN -> REFACTOR -> VERIFY
```

Execution policy:

- `STUB`: Write tests and expected interface first.
- `RED`: Confirm the failure matches the missing behavior.
- `GREEN`: Implement the minimum code that satisfies the test.
- `REFACTOR`: Improve decomposition, ownership, and naming while staying green.
- `VERIFY`: Run all chosen gates and confirm requirement traceability.

## 8) Default Reliability Stack

If you do not know what to prioritize, start here:

1. model invariants with newtypes, enums, and explicit conversions
2. keep library errors typed and application errors contextual
3. make async code cancel-safe, bounded, and non-blocking
4. remove panic edges from parsing, slicing, and boundary arithmetic
5. turn examples, invariants, and misuse cases into tests
6. keep unsafe small, justified, and verified
7. make observability and secret discipline part of the design

## 9) Conventions and Gates

Selective local conventions:

- use four-word naming when feasible for new functions and commands
- preserve stable public APIs when renaming is risky
- keep modules cohesive and purpose-specific
- treat Mermaid as a documentation convention only when the project already expects it

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

## 10) High-Value Anti-Patterns

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

## 11) Output Contract

When producing a substantial Rust response, return results in this order:

1. `Rust Work Mode`
2. `Executable Requirements`
3. `Rust Design (L1/L2/L3 + Traits)`
4. `Verification Matrix`
5. `Implementation Plan`
6. `Quality Gate Results`
7. `Open Questions`

Use traceability tables like:

| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |

## 12) Review Questions

- Which mode or combination of modes is active?
- What is the smallest set of `REQ-RUST-*` contracts that makes the work testable?
- Which types and invariants belong in L1 instead of leaking into adapters?
- Which risk deserves doctest, compile-fail, property, fuzz, `loom`, or `Miri` coverage?
- Which public names must stay stable even if a cleaner new alias exists?
