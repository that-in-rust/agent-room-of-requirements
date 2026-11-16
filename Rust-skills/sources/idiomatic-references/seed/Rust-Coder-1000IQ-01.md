# Rust Coder 1000IQ 01

## 0. Document Status

| Field | Value |
| --- | --- |
| Status | Rigorous working draft |
| Authority | Normative Rust coding doctrine and review spec |
| Scope | Generic Rust delivery across libraries, CLIs, async services, backends, parsers, protocols, contained FFI, and desktop-adjacent work |
| Non-goals | Framework-complete reference manuals, crate-by-crate cataloging, style-only nitpicking, or product-process guidance unrelated to Rust delivery |
| Primary Use | Planning, implementation guidance, design review, hardening, debugging, and verification |
| Decision Standard | Prefer rules that remove bug classes, sharpen boundaries, and make failure behavior explicit |
| Update Rule | Add or revise doctrine only when a rule improves correctness, diagnosability, compatibility, or verification clarity |
| Reading Order | `Fast Router` -> `Mode Selection` -> `Output Contract` -> relevant doctrine sections -> `Pattern Catalog` -> `Quality Gates` |

This document is intended to act as a single-file operator manual plus doctrine atlas.
It MUST remain more rigorous than a style guide and more operational than a narrative essay.

## 1. Fast Router

Use this file when the question is not merely "how do I write Rust syntax?" but one or more of the following:

- how to choose an idiomatic Rust design under real constraints
- how to encode invariants in types, modules, crates, or boundaries
- how to choose tests and quality gates that match the actual risk surface
- how to review Rust for safety, diagnosability, compatibility, and long-term maintainability
- how to reason about async, concurrency, cancellation, persistence, FFI, or desktop-specific hazards

Use this file as the primary doctrine for:

- greenfield Rust features
- major refactors
- public API or crate-surface design
- async service and worker work
- persistence and integration boundaries
- debugging and review passes where the real risk is correctness under change

Do not use this file as the primary authority when:

- the task is purely framework-local and already governed by a narrower doctrine
- the work is so trivial that a language-level doctrine would add more ceremony than clarity
- the repository has an explicit local rule that intentionally overrides a generic Rust default

If a narrower doctrine exists, use this file to validate first principles, verification rigor, and failure-mode handling, not to override the narrower surface by reflex.

## 2. Mode Selection

Choose one or more modes before planning, implementation, or review.

| Mode | Primary Question | Expected Output Emphasis |
| --- | --- | --- |
| `Spec Mode` | What exactly must be true when this work is done? | requirements, measurable contracts, traceability |
| `Delivery Mode` | What is the smallest correct implementation path? | design, sequencing, tests, buildability |
| `Reliability Mode` | How does this fail under pressure? | errors, cancellation, malformed input, recovery |
| `Architecture Mode` | Where should boundaries and ownership live? | crates, modules, traits, adapters, state |
| `Review Mode` | What is risky, non-idiomatic, or brittle here? | findings, anti-patterns, missing tests, regressions |

Default combinations:

- vague feature request: `Spec Mode` + `Delivery Mode`
- public API or reusable crate: `Spec Mode` + `Architecture Mode` + `Reliability Mode`
- async or concurrent system: `Delivery Mode` + `Reliability Mode`
- parser, decoder, or protocol frontier: `Spec Mode` + `Reliability Mode`
- code review: `Review Mode` + one or more of `Architecture Mode` or `Reliability Mode`

Mode precedence:

1. `Spec Mode` decides what must be proven.
2. `Architecture Mode` decides where invariants and dependencies belong.
3. `Reliability Mode` decides what failure behavior must be explicit.
4. `Delivery Mode` decides sequencing.
5. `Review Mode` decides what to challenge hardest.

If two modes appear to disagree, the implementer SHOULD prefer the mode that preserves correctness and compatibility with the smallest surprise to callers.

## 3. Output Contract

Unless the task is very small, return results in this order:

1. `Rust Work Mode`
2. `Executable Requirements`
3. `Rust Design`
4. `Verification Matrix`
5. `Implementation Plan`
6. `Quality Gate Results`
7. `Open Questions`

Use requirement, rule, and test traceability tables like:

| req_id | rule_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- | --- |

Output requirements:

- Every non-trivial behavior claim SHOULD map to a requirement or rule.
- Every non-trivial requirement MUST map to at least one verification path.
- Performance claims MUST include an observable threshold and a verification method.
- Review output MUST lead with findings rather than reassurance.
- Completion claims MUST include fresh verification evidence.

When a section is empty, say why. Do not fake completeness with placeholders disguised as conclusions.

## 4. Normative Conventions

### 4.1 Requirement Language

The following terms are normative:

- `MUST`: mandatory unless a waiver is explicitly recorded
- `MUST NOT`: prohibited unless a waiver is explicitly recorded
- `SHOULD`: default rule unless context justifies deviation
- `SHOULD NOT`: default prohibition unless context justifies deviation
- `MAY`: optional and context-sensitive

### 4.2 Rule Identifier Format

Use stable identifiers:

- `RULE-RUST-L1-OWN-001`
- `RULE-RUST-L2-ERR-003`
- `RULE-RUST-L3-ASYNC-003`
- `ANTI-RUST-L3-CONC-001`
- `ARCH-RUST-API-001`
- `CTX-RUST-BACKEND-001`
- `REQ-RUSTDOC-001.0`
- `TEST-RUST-ASYNC-001`

Identifier classes:

- `RULE-*`: positive normative rule
- `ANTI-*`: anti-pattern or rejected practice
- `ARCH-*`: architectural pattern
- `CTX-*`: domain context pack
- `REQ-*`: executable doctrine requirement
- `TEST-*`: verification reference
- `WAIVER-*`: documented exception

### 4.3 Evidence Grades

| Grade | Meaning |
| --- | --- |
| `High` | supported by core language guarantees, std behavior, or broad production precedent |
| `Medium` | strong ecosystem precedent but still context-sensitive |
| `Low` | useful heuristic or local convention, not a universal rule |

### 4.4 Waiver Discipline

Any explicit exception to a `MUST` or `MUST NOT` rule requires:

- reason
- narrower scope
- compensating control
- verification plan
- owner
- review trigger or expiry condition

Invalid waiver reasons include:

- deadline pressure alone
- "MVP" with no compensating control
- discomfort with tests
- unfamiliarity with the Rust feature that would solve the problem correctly
- desire to keep a speculative abstraction alive without present need

### 4.5 Review Severity

| Severity | Meaning |
| --- | --- |
| `P0` | correctness or safety failure likely to cause broken behavior, corruption, exploitability, or invalid completion claims |
| `P1` | serious design or reliability weakness with high regression or operability risk |
| `P2` | notable maintainability, verification, or boundary weakness |
| `P3` | polish, ergonomics, or clarity issue with limited correctness risk |

### 4.6 Completion Honesty

Fresh verification evidence is required before any claim that work is complete, fixed, passing, or safe to hand off.
Evidence outranks confidence, prior runs, or apparent plausibility.

## 5. Rust First Principles

These principles shape every later rule.

1. Invalid states SHOULD be unrepresentable where practical.
2. Ownership is a design tool, not a compiler obstacle.
3. Borrow before clone.
4. Parse at boundaries; do not leak unvalidated shapes inward.
5. Prefer zero-cost abstractions over manual cleverness.
6. Make failure modes explicit in types, control flow, and tests.
7. Prefer simple public surfaces over sophisticated internal freedom.
8. Async, cancellation, and concurrency are correctness concerns, not only performance concerns.
9. The compiler is a partner for eliminating bug classes, not a nuisance to be appeased.
10. Advanced patterns earn their place by removing misuse or ambiguity, not by sounding smart.
11. Safe and unsafe Rust interact through explicit contracts, not vibes.
12. Destructor timing and cleanup behavior are part of program semantics, not an implementation footnote.

Operational implications:

- If a primitive type can be confused with another domain value, newtype it.
- If a conversion can fail, make it explicit at the boundary.
- If a task can outlive its caller, cancellation and shutdown semantics MUST be described.
- If a rule is justified only by aesthetics, it SHOULD lose to a correctness or compatibility concern.
- If an invariant can be checked statically with a type, prefer that over a runtime check.
- If an invariant cannot be checked statically, validate it once at the narrowest trustworthy edge.
- If a destructor would need to fail, block, or await to do the right thing, the design SHOULD expose an explicit close or shutdown path instead.
- If code is "correct because the compiler accepts it", treat that as an unproven claim until logic, tests, and boundary behavior agree.

### 5.1 Enforcement Hierarchy

- Prefer static enforcement over dynamic enforcement when the type system can rule out bad states cheaply.
- Prefer dynamic boundary validation over repeated downstream checks when static enforcement is not practical.
- `_unchecked` or raw fast paths MAY exist only when their checked counterparts define the contract clearly and the caller can realistically uphold it.
- Debug-only validation SHOULD protect expensive internal consistency checks, not replace boundary discipline.

### 5.2 Safe And Unsafe Contract Thinking

- Safe Rust code MAY rely on the language's soundness guarantees, but MUST still defend against logical bugs, race conditions, and stale assumptions.
- Unsafe Rust MUST assume surrounding safe code can be semantically wrong while still memory-safe.
- Every unsafe block, unsafe trait, and unsafe function SHOULD correspond to a narrow proof obligation that can be explained locally.
- If an unsafe optimization does not buy measurable leverage, delete it rather than widening the proof surface.

### 5.3 Destructor And Temporary Discipline

- Prefer shorter-lived temporaries and guards when that makes drop timing more predictable.
- Destructors SHOULD be infallible, non-blocking, and side-effect-minimal.
- Async or blocking teardown belongs in explicit methods such as `shutdown`, `flush`, or `close`, not in `Drop`.
- If correctness depends on teardown happening before later work, express that in control flow and tests rather than hoping scope boundaries stay obvious.

### 5.4 The Compiler Is Not The Whole Verifier

- The compiler proves memory and type properties, not domain correctness, performance truth, cancellation behavior, or semver cleanliness.
- Lack of borrow-checker errors does not prove clones are justified.
- Lack of data races does not prove absence of logical races, starvation, dropped work, or stale state visibility.
- Use the compiler to shrink the search space, then use tests and review to prove the remaining semantic claims.

## 6. Doctrine by Layer

### 6.1 L1 Core / no_std-Compatible Doctrine

Focus:

- ownership and borrowing
- lifetimes
- traits and generics
- newtypes and invariants
- `Option` and `Result`
- typestate where justified

#### 6.1.1 Ownership and Borrowing

- Public APIs SHOULD accept borrowed inputs such as `&str`, `&[T]`, or `AsRef<_>` when ownership transfer is not semantically required.
- Constructors MAY take owned values when the constructed type must own its state.
- Cloning in hot or boundary-heavy code MUST be justified by simplicity, lifetime isolation, or API ergonomics.
- Methods SHOULD communicate ownership intent clearly: borrowed read access, borrowed mutable access, consuming ownership, or shared ownership.

Tradeoffs:

- Taking ownership simplifies internal storage but can over-constrain callers.
- Aggressive borrowing can create brittle signatures when storage or async needs truly require ownership.

#### 6.1.2 Lifetime Contracts

- Lifetime annotations SHOULD express real relationships, not cargo-cult signatures.
- Returned references MUST never outlive the storage they refer to.
- If lifetime reasoning becomes harder to maintain than the underlying logic, reevaluate the API shape rather than piling on annotations.
- Scoped borrows are preferred over long-lived shared mutable access.

#### 6.1.3 Type-Encoded Invariants

- Newtypes SHOULD guard identifiers, units, offsets, tokens, and validated domain values.
- Enums SHOULD replace booleans or sentinel values when more than one semantic outcome exists.
- Typestate MAY be used when invalid transitions are expensive or dangerous enough to justify extra API structure.
- Phantom types MAY encode invariants with zero runtime cost when the invariant is real and recurring.

#### 6.1.4 Trait and Generic Surface Design

- Trait seams SHOULD exist where substitution, testing, or boundary decoupling materially matters.
- Generic APIs SHOULD not expose more type machinery than callers need.
- Trait objects versus generics MUST be an explicit boundary choice:
  - use generics when static dispatch and compile-time composition matter
  - use trait objects when dynamic boundary shape and reduced type sprawl matter more

#### 6.1.5 Parse-Don't-Validate Boundaries

- Parse once at the edge, then traffic only validated domain types inward.
- Ad hoc re-validation deep in business logic SHOULD be treated as boundary leakage unless it protects against a distinct trust boundary.
- `From` and `TryFrom` SHOULD be preferred over duplicated field-by-field conversion logic.

#### 6.1.6 Argument Validation And Constructor Discipline

- Constructors and parsing APIs SHOULD choose argument types that rule out invalid input whenever practical.
- If dynamic validation is necessary, it SHOULD happen immediately and return a typed failure rather than leaking half-validated state inward.
- `_unchecked` constructors MUST document preconditions precisely and SHOULD live beside their checked equivalents.
- Invariant-preserving constructors SHOULD be the default path into domain types; field-by-field public mutation is a last resort.

### 6.2 L2 Standard Library Doctrine

Focus:

- collections
- iterators
- `std::sync`
- `std::thread`
- module and crate organization
- error interoperability

#### 6.2.1 Collection and Iterator Discipline

- Collection choice SHOULD match access pattern, ordering needs, and mutation profile rather than habit.
- Iterator pipelines SHOULD be preferred when they preserve clarity and avoid needless intermediate allocation.
- `impl Iterator` MAY be used in return position when laziness is valuable and concrete iterator types would leak implementation noise.
- Manual loops remain acceptable when they are clearer, more controllable, or easier to debug than combinator chains.

#### 6.2.2 Error and Recovery Surfaces

- Library crates SHOULD expose typed errors.
- Application binaries MAY use dynamic error aggregation at top-level orchestration boundaries.
- Error chains SHOULD preserve root cause and boundary context.
- Recovery strategy SHOULD be explicit where caller behavior changes materially.
- Non-UTF-8 boundaries SHOULD be diagnosed safely without assuming text.
- Public dependency error types SHOULD NOT leak through stable APIs unless the semver commitment is deliberate.
- If an error is mostly propagated and displayed rather than inspected programmatically, opaque wrapping with good context is often superior to a giant public enum.

#### 6.2.3 Shared State and Synchronization

- `Rc`, `Arc`, `Cell`, `RefCell`, `Mutex`, `RwLock`, atomics, and channels are different tools, not interchangeable defaults.
- Shared state SHOULD be narrowed to the smallest mutable surface possible.
- `Arc<Mutex<T>>` MUST NOT become the default architecture for unrelated concerns.
- One-time initialization SHOULD prefer `OnceLock` or `LazyLock` rather than bespoke global patterns.

#### 6.2.4 API Ergonomics and Cohesion

- Public modules SHOULD present a flat, intentional façade where it improves discoverability.
- `pub use` MAY simplify public entrypoints, but MUST NOT obscure ownership, error, or feature boundaries.
- Names SHOULD reflect domain intent, not implementation accident.
- Keep modules cohesive; split when a module has multiple unrelated change reasons.
- Conversion names SHOULD follow real cost and ownership semantics: `as_` for cheap borrowed views, `to_` for potentially allocating or copying transforms, and `into_` for owned consumption.

#### 6.2.5 Workspace and Module Structure

- Workspaces SHOULD centralize shared dependency versions, shared lockfile discipline, and common quality gates.
- Feature flags SHOULD be additive by default.
- Workspace conventions MUST be visible in code or manifest structure, not left as tribal knowledge.
- Cross-crate domain types SHOULD live where ownership and compatibility pressure are easiest to manage, not wherever they were first needed.

#### 6.2.6 Teardown And Generated Surfaces

- `Drop` implementations SHOULD not become the primary API for operations that can fail, block, or require ordering guarantees.
- Types needing deterministic cleanup SHOULD expose explicit close or shutdown methods and make post-close behavior obvious.
- Generated Rust SHOULD be treated as an implementation artifact, not as the primary hand-edited doctrine surface.
- Hand-maintained wrappers or extension modules SHOULD own the semantic contract around generated code rather than patching generated files directly.

### 6.3 L3 Ecosystem Doctrine

Focus:

- async runtimes
- serialization
- HTTP or service frameworks
- observability
- persistence
- fuzz, property, and concurrency tooling

#### 6.3.1 Async Runtime and Cancellation Discipline

- Async boundaries SHOULD own data they may hold across suspension points.
- Blocking calls MUST NOT live in async hot paths.
- Lock guards MUST NOT be held across `.await`.
- Cancellation semantics MUST be described for long-running or partial-progress operations.
- Background tasks MUST have lifecycle ownership, structured shutdown, and failure visibility.

#### 6.3.2 Serialization and Boundary Types

- Transport shapes SHOULD remain transport shapes.
- Domain invariants SHOULD live in domain types, not raw DTOs.
- Binary payloads MUST use binary-friendly transports rather than giant JSON blobs where size or performance matters.
- Opaque or untrusted payloads SHOULD be inspected carefully before conversion to richer internal forms.

#### 6.3.3 Persistence and External Integration Boundaries

- Persistence workflows SHOULD have one clear transaction owner.
- Durable state and remote side effects MUST have an explicit failure strategy when combined.
- External client boundaries SHOULD expose typed failures, timeout policy, retry policy, and correlation context.
- Idempotency and deduplication MUST be designed where callers or infra can replay requests.

#### 6.3.4 Observability and Diagnostics

- Orchestration boundaries SHOULD emit structured tracing with stable fields.
- User-facing errors SHOULD contain actionable repair hints where possible.
- Debuggability SHOULD be treated as a design constraint, not a postscript.
- Secret-bearing data MUST be redacted or represented safely.

#### 6.3.5 Framework-Specific Containment

- Framework-specific types SHOULD be contained near integration boundaries.
- Core logic SHOULD remain testable without runtime, database, or framework bootstrapping where feasible.
- Desktop capabilities, sidecars, and plugin permissions MUST be scoped minimally and supervised explicitly.
- Unsafe and FFI surfaces MUST remain small, documented, and independently verified.

#### 6.3.6 Measurement Before Optimization

- Performance work SHOULD begin with profiling or a demonstrated hot path, not intuition.
- Algorithmic guarantees MAY outrank local micro-optimizations when worst-case behavior matters.
- Benchmark-driven claims MUST use representative inputs and stable thresholds.
- Compile time, binary size, memory use, and latency are different optimization dimensions; name the one being optimized.

## 7. Pattern Catalog

### 7.1 Pattern Selection Rubric

Elevate only patterns that score well on at least several of these dimensions:

| Criterion | Description |
| --- | --- |
| `Zero-cost` | abstraction does not impose avoidable runtime overhead |
| `Type-safe` | the type system prevents misuse or narrows misuse strongly |
| `Ergonomic` | common use stays simple while hard cases remain possible |
| `Compositional` | pattern combines well with other patterns |
| `Resilient` | failure modes and edge cases are handled cleanly |
| `Meta-level` | reveals a deeper design principle, not just syntax |

Promotion policy:

- A pattern SHOULD be promoted only when it reduces bug classes, misuse, or ambiguous failure behavior.
- A pattern MUST NOT be promoted merely because it looks advanced.
- Patterns that demand high ceremony MUST justify the cost with clear safety, boundary, or correctness leverage.

### 7.2 Pattern Card Template

```md
### RULE-RUST-<LAYER>-<TOPIC>-<NNN>

- `Layer`:
- `Status`: MUST / SHOULD / MAY
- `Pattern Name`:
- `Problem`:
- `Rule`:
- `Rationale`:
- `When to Use`:
- `When Not to Use`:
- `Example Shape`:
- `Counterexample Shape`:
- `Verification`:
- `Evidence Grade`:
- `Meta Insight`:
- `Related`:
```

### 7.3 Seed Rule Card

### RULE-RUST-L2-ERR-003

- `Layer`: L2
- `Status`: SHOULD
- `Pattern Name`: Recovery-Aware Error Classification
- `Problem`: callers cannot choose retry, degrade, or fail-fast safely when recoverability is implicit
- `Rule`: Error types SHOULD encode recovery strategy when retryability materially changes control flow
- `Rationale`: failure cause and recovery policy are different dimensions
- `When to Use`: network clients, storage boundaries, subprocesses, queues, external APIs
- `When Not to Use`: tiny leaf functions with no policy branching and no meaningful caller choice
- `Example Shape`: typed transient/permanent or retryable/non-retryable error metadata
- `Counterexample Shape`: matching on error strings in multiple call sites
- `Verification`: tests prove transient errors retry and permanent errors do not
- `Evidence Grade`: High
- `Meta Insight`: classify by recovery strategy, not by cause
- `Related`: `ANTI-RUST-L2-ERR-002`

### RULE-RUST-L1-OWN-001

- `Layer`: L1
- `Status`: SHOULD
- `Pattern Name`: Borrowed Public Inputs
- `Problem`: callers are forced to allocate or give up ownership when a read-only view would suffice
- `Rule`: Public APIs SHOULD accept borrowed views such as `&str`, `&[T]`, or `AsRef<_>` unless ownership is semantically required
- `Rationale`: borrowed boundaries preserve flexibility and reduce incidental allocation or cloning
- `When to Use`: parsers, lookups, pure transforms, queries, and validation functions
- `When Not to Use`: constructors or async workflows that must own data beyond the call boundary
- `Example Shape`: `fn parse_name(input: &str) -> Result<Name, ParseNameError>`
- `Counterexample Shape`: `fn parse_name(input: &String) -> Result<Name, _>`
- `Verification`: API review plus allocation-sensitive tests in hot paths
- `Evidence Grade`: High
- `Meta Insight`: ownership should communicate semantics, not caller inconvenience
- `Related`: `RULE-RUST-L1-CONV-001`, `ANTI-RUST-L1-OWN-001`

### RULE-RUST-L1-TYPE-001

- `Layer`: L1
- `Status`: MUST
- `Pattern Name`: Newtypes And Parse-At-The-Edge
- `Problem`: primitive obsession allows invalid or swapped values to travel deep into the system
- `Rule`: Domain identifiers, units, tokens, and validated values MUST use dedicated types once they cross a trust boundary
- `Rationale`: type distinctions remove whole classes of misuse and make invariants explicit
- `When to Use`: IDs, offsets, credentials, validated strings, protocol fields, units, and resource handles
- `When Not to Use`: local one-shot glue code with no reuse or ambiguity and no boundary crossing
- `Example Shape`: `struct UserId(NonZeroU64);` plus `TryFrom<&str> for EmailAddress`
- `Counterexample Shape`: raw `String`, `u64`, or `bool` values standing in for multiple domain meanings
- `Verification`: compile-time misuse resistance plus parse and round-trip tests
- `Evidence Grade`: High
- `Meta Insight`: if two values should not be swappable, their types should not be swappable
- `Related`: `RULE-RUST-L1-CONV-001`, `ANTI-RUST-L1-TYPE-001`

### RULE-RUST-L1-CONV-001

- `Layer`: L1
- `Status`: SHOULD
- `Pattern Name`: Explicit Domain Conversions
- `Problem`: repeated ad hoc conversion logic leaks validation inconsistently
- `Rule`: Conversions between transport, domain, and storage representations SHOULD use `From`, `TryFrom`, or dedicated constructors with explicit failure semantics
- `Rationale`: one conversion path is easier to test and reason about than many near-duplicates
- `When to Use`: DTO-to-domain, string-to-newtype, storage-row-to-domain, config parsing
- `When Not to Use`: trivial internal reshaping with no invariants and no error path
- `Example Shape`: `TryFrom<CreateUserRequest> for NewUser`
- `Counterexample Shape`: hand-validating the same fields in multiple handlers
- `Verification`: conversion tests, malformed input cases, and compile-time API review
- `Evidence Grade`: High
- `Meta Insight`: conversion is part of the contract, not a private convenience
- `Related`: `RULE-RUST-L1-TYPE-001`, `ARCH-RUST-BOUNDARY-002`

### RULE-RUST-L1-VALIDATE-001

- `Layer`: L1
- `Status`: MUST
- `Pattern Name`: Static Before Dynamic Validation
- `Problem`: invalid values reach the core because validation is postponed or expressed only by comments
- `Rule`: APIs MUST prefer argument types that rule out invalid inputs, and MUST perform dynamic validation immediately when static enforcement is insufficient
- `Rationale`: catching bad states earlier reduces downstream branching and produces clearer failure surfaces
- `When to Use`: constructors, parsers, protocol boundaries, config loading, public API entrypoints
- `When Not to Use`: none when unchecked input crosses a trust boundary; local glue may use narrower helpers if the checked boundary already exists
- `Example Shape`: `TryFrom<&str>` for validated domain values, or a checked constructor plus a documented `_unchecked` fast path
- `Counterexample Shape`: accepting raw primitives everywhere and re-checking them opportunistically in later business logic
- `Verification`: malformed-input tests, compile-time misuse resistance where types are involved, and API review of unchecked escape hatches
- `Evidence Grade`: High
- `Meta Insight`: the best validation is the one callers cannot accidentally forget
- `Related`: `RULE-RUST-L1-TYPE-001`, `RULE-RUST-L1-CONV-001`, `ANTI-RUST-L1-TYPE-001`

### RULE-RUST-L1-TRAIT-001

- `Layer`: L1
- `Status`: SHOULD
- `Pattern Name`: Trait Seams Before Concrete Adapters
- `Problem`: domain logic becomes hard to test or evolve when concrete infrastructure types bleed inward
- `Rule`: Trait seams SHOULD exist at external dependency boundaries when substitution, isolation, or compile-time decoupling materially helps
- `Rationale`: the seam belongs where ownership of side effects changes, not everywhere by default
- `When to Use`: outbound HTTP, storage, queue, clock, UUID generation, sidecar process orchestration
- `When Not to Use`: tiny leaf logic or stable internal helpers where a trait adds indirection without benefit
- `Example Shape`: core service depends on a `UserStore` trait, adapter owns the SQLx pool
- `Counterexample Shape`: handlers constructing clients or queries inline
- `Verification`: unit tests against fakes plus integration tests against the real adapter
- `Evidence Grade`: Medium
- `Meta Insight`: abstract only where the boundary, not the syntax, truly changes
- `Related`: `ARCH-RUST-BOUNDARY-001`, `ANTI-RUST-L2-API-001`

### RULE-RUST-L1-STATE-001

- `Layer`: L1
- `Status`: MAY
- `Pattern Name`: Typestate For Must-Complete Protocols
- `Problem`: runtime state machines allow illegal transitions and forgotten mandatory steps
- `Rule`: Typestate MAY be used when state transitions are critical enough that compile-time invalid-state elimination outweighs the additional API structure
- `Rationale`: protocol correctness sometimes deserves stronger guarantees than runtime checks provide
- `When to Use`: handshakes, builders with mandatory fields, resource lifecycle protocols, staged compilation or activation flows
- `When Not to Use`: ordinary CRUD paths, soft workflows, or APIs where the state machine cost dwarfs the risk
- `Example Shape`: `Connection<Unauthenticated>` -> `Connection<Authenticated>`
- `Counterexample Shape`: enum state plus scattered runtime checks at every call site
- `Verification`: compile-fail misuse tests plus state transition tests
- `Evidence Grade`: Medium
- `Meta Insight`: use the type system to forbid illegal moves when the protocol matters more than API brevity
- `Related`: `TEST-RUST-COMPILE-001`, `ANTI-RUST-L1-STATE-001`

### RULE-RUST-L2-ERR-001

- `Layer`: L2
- `Status`: MUST
- `Pattern Name`: Typed Library Errors And Dynamic App Boundaries
- `Problem`: callers either lose actionable structure or are forced to depend on internal details
- `Rule`: Libraries MUST expose typed error surfaces; binaries MAY aggregate lower-level errors dynamically at the top orchestration boundary
- `Rationale`: callers of reusable code need structured handling, while top-level apps need concise propagation and context layering
- `When to Use`: all crates with a public API or reusable domain/service layer
- `When Not to Use`: private, throwaway, single-binary helpers with no reusable boundary
- `Example Shape`: `thiserror` enum in library code, `anyhow` or `eyre` at CLI `main`
- `Counterexample Shape`: exporting `anyhow::Error` from a library API as the default contract
- `Verification`: error exhaustiveness review, display tests where useful, and integration tests for boundary reporting
- `Evidence Grade`: High
- `Meta Insight`: the error type is part of the API surface, not a logging afterthought
- `Related`: `RULE-RUST-L2-ERR-003`, `ANTI-RUST-L2-ERR-001`

### RULE-RUST-L2-ERR-002

- `Layer`: L2
- `Status`: SHOULD
- `Pattern Name`: Context-Rich Error Layering
- `Problem`: failures become opaque once they cross I/O or orchestration boundaries
- `Rule`: Errors SHOULD gain context at boundaries where location, operation, or caller repair action becomes clearer
- `Rationale`: debugging quality depends on preserving both cause and boundary semantics
- `When to Use`: file I/O, database calls, subprocesses, HTTP client requests, background task joins
- `When Not to Use`: ultra-local helpers where the added context duplicates the only possible operation
- `Example Shape`: `read_to_string(path).with_context(|| format!(\"read config: {path}\"))?`
- `Counterexample Shape`: propagating generic `NotFound` or `Io` with no operation context
- `Verification`: error snapshot or string-shape tests when presentation matters, plus boundary review
- `Evidence Grade`: High
- `Meta Insight`: errors are data; context gives the data an actionable location
- `Related`: `RULE-RUST-L2-ERR-001`, `ANTI-RUST-L2-ERR-002`

### RULE-RUST-L2-COLL-001

- `Layer`: L2
- `Status`: SHOULD
- `Pattern Name`: Collection Choice By Access Pattern
- `Problem`: defaulting to a favorite collection hides performance, ordering, and ownership tradeoffs
- `Rule`: Collection selection SHOULD follow lookup, iteration, ordering, mutation, and memory behavior rather than habit
- `Rationale`: collection choice is a boundary decision about semantics and costs
- `When to Use`: caches, registries, queues, ordered output, deduplication, incremental builders
- `When Not to Use`: tiny local scopes where the structure cannot materially affect clarity or behavior
- `Example Shape`: `BTreeMap` for stable ordered iteration, `HashMap` for fast keyed lookup, `Vec` for compact ordered scans
- `Counterexample Shape`: using `HashMap` everywhere, then re-sorting or cloning into a shape the caller actually needed
- `Verification`: benchmark or profiling evidence for hot paths, plus review of ordering and mutation expectations
- `Evidence Grade`: Medium
- `Meta Insight`: collection choice is part of the contract when access pattern matters
- `Related`: `RULE-RUST-L2-ITER-001`, `ANTI-RUST-L2-ITER-001`

### RULE-RUST-L2-ITER-001

- `Layer`: L2
- `Status`: SHOULD
- `Pattern Name`: Iterator Contracts Over Manual Plumbing
- `Problem`: imperative data plumbing obscures transformation intent and increases intermediate-state noise
- `Rule`: Iterator pipelines SHOULD be preferred when they improve clarity, preserve laziness, or avoid unnecessary allocation
- `Rationale`: iterator contracts compose and make transformation boundaries easier to inspect
- `When to Use`: filtering, mapping, aggregation, owned/borrowed traversal, fallible pipelines
- `When Not to Use`: control-heavy loops where explicit state machines are clearer
- `Example Shape`: iterator adapters with `collect::<Result<Vec<_>, _>>()`
- `Counterexample Shape`: nested mutable accumulators with repeated push logic and implicit branch state
- `Verification`: property tests or golden-output tests for transformation correctness
- `Evidence Grade`: Medium
- `Meta Insight`: iterators encode data-flow intent more directly than ad hoc mutation does
- `Related`: `RULE-RUST-L2-COLL-001`, `ANTI-RUST-L2-ITER-001`

### RULE-RUST-L2-BUILD-001

- `Layer`: L2
- `Status`: SHOULD
- `Pattern Name`: Builder Plus Frozen Config
- `Problem`: complex construction requires many optional knobs but runtime code should consume a stable final configuration
- `Rule`: Use builders for staged configuration and freeze into a validated final struct before execution
- `Rationale`: construction-time flexibility should not leak as runtime mutability or half-configured state
- `When to Use`: clients, services, compilers, pipelines, request options, sidecar startup config
- `When Not to Use`: tiny structs with two obvious required fields
- `Example Shape`: builder validates and returns an immutable `Config`
- `Counterexample Shape`: mutable config object passed through the whole system and patched on demand
- `Verification`: builder validation tests and config serialization/round-trip tests where relevant
- `Evidence Grade`: Medium
- `Meta Insight`: let variability live at the edge of construction, not in the core of execution
- `Related`: `RULE-RUST-L1-STATE-001`, `ANTI-RUST-L2-BUILD-001`

### RULE-RUST-L2-API-001

- `Layer`: L2
- `Status`: SHOULD
- `Pattern Name`: Flat Public Facades With Intentional Re-Exports
- `Problem`: deep module trees leak internal organization into the user-facing API
- `Rule`: Public APIs SHOULD present intentional, flat façades when that improves discoverability without hiding boundary truth
- `Rationale`: callers should navigate concepts, not internal folder history
- `When to Use`: libraries, SDK crates, shared utility surfaces, domain crates with stable public entrypoints
- `When Not to Use`: when re-exporting would conceal meaningful ownership or feature boundaries
- `Example Shape`: `pub use` selected types and functions from narrow modules
- `Counterexample Shape`: forcing callers to descend through incidental module layers for common entrypoints
- `Verification`: API review, doctest examples, and semver impact review
- `Evidence Grade`: Medium
- `Meta Insight`: good public shape is curated, not accidental
- `Related`: `ARCH-RUST-API-001`, `ANTI-RUST-L2-API-001`

### RULE-RUST-L2-API-002

- `Layer`: L2
- `Status`: MUST
- `Pattern Name`: Public Dependency Exposure Is A Deliberate Commitment
- `Problem`: stable APIs accidentally inherit semver fragility from upstream crate types
- `Rule`: Public APIs MUST treat exposed dependency types as deliberate commitments; otherwise translate them into local façade or domain types
- `Rationale`: a leaked upstream type silently widens the compatibility surface of your crate
- `When to Use`: reusable libraries, SDKs, shared internal platform crates, public error types, public iterators and config surfaces
- `When Not to Use`: private binaries or internal-only modules with no consumer stability expectation
- `Example Shape`: local `Error`, `Request`, or `Config` wrapper that owns the public contract while storing or converting dependency details internally
- `Counterexample Shape`: public signatures or enum variants directly exposing volatile third-party types by convenience
- `Verification`: semver-oriented API review, downstream example inspection, and release checklist review
- `Evidence Grade`: High
- `Meta Insight`: a dependency type in your public API is no longer just their decision
- `Related`: `RULE-RUST-L2-ERR-001`, `ARCH-RUST-API-001`, `ANTI-RUST-L2-ERR-004`

### RULE-RUST-L2-WS-001

- `Layer`: L2
- `Status`: SHOULD
- `Pattern Name`: Workspace And Feature Discipline
- `Problem`: large Rust repos decay into build drift, hidden coupling, and feature-flag chaos
- `Rule`: Workspaces SHOULD centralize dependency versions, unify top-level gates, and keep features additive by default
- `Rationale`: build discipline is architecture, not housekeeping
- `When to Use`: any multi-crate repo or crate with optional integrations
- `When Not to Use`: single tiny crate with no optional behavior and no meaningful shared infra
- `Example Shape`: workspace root owns shared versions, member crates avoid copy-pasted version drift
- `Counterexample Shape`: implicit feature assumptions and duplicate dependency declarations with divergent versions
- `Verification`: workspace build from root, feature matrix checks, and release review
- `Evidence Grade`: High
- `Meta Insight`: correctness at scale includes build topology, not just code shape
- `Related`: `ARCH-RUST-WS-001`, `ANTI-RUST-L2-WS-001`

### RULE-RUST-L2-DTOR-001

- `Layer`: L2
- `Status`: MUST
- `Pattern Name`: Explicit Close For Fallible Or Blocking Teardown
- `Problem`: cleanup that can fail, block, or require ordering is hidden in `Drop`, where callers cannot reason about it well
- `Rule`: Types with fallible, blocking, or protocol-sensitive teardown MUST expose an explicit `close`, `flush`, or `shutdown` path and keep `Drop` best-effort, infallible, and non-blocking
- `Rationale`: deterministic cleanup is a behavioral contract, not a destructor side effect
- `When to Use`: file-like resources, network clients, sidecars, task supervisors, buffered writers, transactional or session-like resources
- `When Not to Use`: trivial resources with pure in-memory cleanup and no meaningful teardown failure mode
- `Example Shape`: explicit async or sync shutdown method that returns `Result`, with `Drop` only releasing local state
- `Counterexample Shape`: destructor performing I/O, waiting on tasks, or panicking when cleanup fails
- `Verification`: close-path tests, double-close behavior tests, shutdown ordering tests, and review of `Drop` side effects
- `Evidence Grade`: High
- `Meta Insight`: the cleanup path you need to reason about should be callable, not magical
- `Related`: `RULE-RUST-L3-ASYNC-004`, `ANTI-RUST-L2-DTOR-001`

### RULE-RUST-L3-ASYNC-001

- `Layer`: L3
- `Status`: MUST
- `Pattern Name`: Owned Async Boundaries
- `Problem`: borrowed data crossing suspension points creates brittle lifetimes or hidden data-loss hazards
- `Rule`: Async boundaries MUST own any data they may retain across `.await` or task handoff
- `Rationale`: async state machines extend lifetimes in ways that should remain explicit and stable
- `When to Use`: `tokio::spawn`, long-running async functions, command handlers, background jobs, multi-step orchestration
- `When Not to Use`: synchronous helpers or strictly local borrows that do not cross `.await`
- `Example Shape`: move owned request or domain state into async workflow
- `Counterexample Shape`: borrowed request fragments held through spawned or multi-await task lifetimes
- `Verification`: compile-time ownership proof plus cancellation and partial-progress tests where relevant
- `Evidence Grade`: High
- `Meta Insight`: async ownership should be obvious before the scheduler makes it non-obvious
- `Related`: `ANTI-RUST-L3-ASYNC-001`, `RULE-RUST-L3-ASYNC-003`

### RULE-RUST-L3-ASYNC-002

- `Layer`: L3
- `Status`: MUST
- `Pattern Name`: No Blocking And No Locks Across Await
- `Problem`: executor starvation and deadlock-prone interleavings hide behind superficially correct code
- `Rule`: Async hot paths MUST avoid blocking calls and MUST NOT hold lock guards across `.await`
- `Rationale`: one passed run proves nothing about async fairness or contention behavior
- `When to Use`: any runtime-backed async service, worker, desktop command, or client orchestration
- `When Not to Use`: tightly bounded startup or one-shot tooling where no executor fairness contract exists and blocking is explicit
- `Example Shape`: async I/O plus scoped lock usage before suspension
- `Counterexample Shape`: `std::thread::sleep`, sync file I/O, or `MutexGuard` held into a `select!` or network await
- `Verification`: stress, timeout, or latency tests; code review of blocking call sites; `loom` or model checks when race behavior matters
- `Evidence Grade`: High
- `Meta Insight`: async correctness fails through starvation and interleaving long before it fails through syntax
- `Related`: `ANTI-RUST-L3-ASYNC-001`, `ANTI-RUST-L3-CONC-001`

### RULE-RUST-L3-ASYNC-003

- `Layer`: L3
- `Status`: MUST
- `Pattern Name`: Bounded Concurrency And Explicit Cancellation
- `Problem`: unbounded task fan-out, queue growth, or forgotten cancellation semantics produce invisible instability
- `Rule`: Long-running async systems MUST make concurrency bounds, backpressure, and cancellation behavior explicit
- `Rationale`: throughput without shutdown or overload behavior is not reliability
- `When to Use`: worker pools, streaming pipelines, service orchestration, retries, sidecar supervision, background processing
- `When Not to Use`: strictly local single-step async functions with no queueing or task fan-out
- `Example Shape`: semaphore or bounded channel plus cancellation token and shutdown path
- `Counterexample Shape`: fire-and-forget spawning with implicit infinite buffering
- `Verification`: overload tests, cancellation tests, and shutdown tests
- `Evidence Grade`: High
- `Meta Insight`: if work can accumulate, the system already has a queue whether you model it or not
- `Related`: `RULE-RUST-L3-CONC-001`, `ANTI-RUST-L3-CONC-002`

### RULE-RUST-L3-ASYNC-004

- `Layer`: L3
- `Status`: MUST
- `Pattern Name`: Explicit Shutdown And Cancellation Fan-Out
- `Problem`: systems cannot stop predictably because cancellation intent is implicit, fragmented, or not propagated to all owned tasks
- `Rule`: Multi-task async systems MUST define a single shutdown trigger, explicit fan-out to owned tasks, and a bounded wait path for completion or escalation
- `Rationale`: graceful shutdown is part of steady-state correctness, not a last-minute operator concern
- `When to Use`: services, daemons, workers, desktop sidecars, background processors, long-lived command loops
- `When Not to Use`: single-future one-shot flows with no owned background work
- `Example Shape`: a cancellation token or shutdown channel cloned into worker tasks plus a join phase with timeout or escalation
- `Counterexample Shape`: main task exits and hopes spawned tasks disappear cleanly without coordination
- `Verification`: shutdown tests, ctrl-c or signal integration tests where relevant, cancel-during-work tests, and bounded-teardown timing checks
- `Evidence Grade`: High
- `Meta Insight`: if shutdown is implicit, ownership is probably implicit too
- `Related`: `RULE-RUST-L3-ASYNC-003`, `RULE-RUST-L3-CONC-001`, `RULE-RUST-L2-DTOR-001`

### RULE-RUST-L3-CONC-001

- `Layer`: L3
- `Status`: SHOULD
- `Pattern Name`: Structured Concurrency With Visible Ownership
- `Problem`: detached background work outlives its parent without clear error, lifecycle, or cleanup semantics
- `Rule`: Task orchestration SHOULD use structured ownership such as task sets, join discipline, or explicit supervisor ownership
- `Rationale`: lifecycle and failure propagation should be visible in the control flow
- `When to Use`: services, orchestrators, workers, sidecars, multiphase pipelines, desktop subsystems
- `When Not to Use`: intentionally detached telemetry or fire-and-forget work with bounded and acceptable loss characteristics
- `Example Shape`: `JoinSet` or equivalent supervisor that owns spawned tasks
- `Counterexample Shape`: background tasks launched and forgotten with no shutdown or error collection path
- `Verification`: teardown tests, error-propagation tests, and leak-resistant shutdown checks
- `Evidence Grade`: High
- `Meta Insight`: if no one owns a task, no one owns its failure
- `Related`: `ANTI-RUST-L3-CONC-002`, `RULE-RUST-L3-ASYNC-003`

### RULE-RUST-L3-OBS-001

- `Layer`: L3
- `Status`: SHOULD
- `Pattern Name`: Structured Observability At Orchestration Boundaries
- `Problem`: failures are hard to localize when work spans IO, tasks, retries, or components without stable context
- `Rule`: Orchestration boundaries SHOULD emit structured tracing with stable fields, error context, and correlation data
- `Rationale`: debug time is often dominated by missing context, not missing features
- `When to Use`: request handlers, background jobs, external client calls, sidecar supervision, queue consumers, CLI top-level flows
- `When Not to Use`: tight inner loops where instrumentation cost outweighs value and a higher boundary already provides sufficient context
- `Example Shape`: `tracing` spans with request IDs, resource IDs, attempt counts, and outcome fields
- `Counterexample Shape`: free-form string logs with unstable wording and missing identity fields
- `Verification`: log-shape review, integration tests around error reporting where needed, and operational dry runs
- `Evidence Grade`: Medium
- `Meta Insight`: systems fail at boundaries, so that is where observability should get richer
- `Related`: `RULE-RUST-L2-ERR-002`, `ANTI-RUST-L3-OBS-001`

### RULE-RUST-L3-BACKEND-001

- `Layer`: L3
- `Status`: MUST
- `Pattern Name`: Transport To Domain Conversion At The Edge
- `Problem`: unchecked request payload shapes leak into business logic and persistence code
- `Rule`: Service edges MUST convert transport types into validated domain types before domain workflows and persistence logic proceed
- `Rationale`: shape validation is not equivalent to invariant validation
- `When to Use`: HTTP handlers, queue consumers, CLI input adapters, RPC or IPC boundaries
- `When Not to Use`: none when untrusted or loosely shaped input crosses into the core
- `Example Shape`: request DTO -> `TryFrom` -> domain command -> workflow -> persistence
- `Counterexample Shape`: handlers, services, and DB calls all sharing raw strings and optional fields
- `Verification`: handler integration tests, malformed input cases, domain conversion tests
- `Evidence Grade`: High
- `Meta Insight`: transport is where data arrives; domain is where truth begins
- `Related`: `ARCH-RUST-BOUNDARY-002`, `ANTI-RUST-L3-BOUNDARY-001`

### RULE-RUST-L3-TAURI-001

- `Layer`: L3
- `Status`: MUST
- `Pattern Name`: Minimal Capabilities And Explicit Sidecar Ownership
- `Problem`: desktop apps quietly broaden privilege, spawn unmanaged processes, or move giant payloads through the wrong transport
- `Rule`: Tauri capabilities, filesystem scopes, sidecar process rules, and IPC payload shapes MUST be explicit, minimal, and lifecycle-owned
- `Rationale`: desktop boundaries are security and operability boundaries, not just convenience glue
- `When to Use`: Tauri commands, plugin integrations, sidecars, window-specific privileges, updater or deep-link wiring
- `When Not to Use`: non-desktop Rust systems with no capability or sidecar boundary
- `Example Shape`: owned async commands, granular capabilities, supervised sidecar with health checks and bounded startup
- `Counterexample Shape`: borrowed async command inputs, broad filesystem permissions, shell-like sidecar escape hatches
- `Verification`: command tests, capability review, startup timeout checks, and IPC payload-shape review
- `Evidence Grade`: High
- `Meta Insight`: least privilege is part of correctness when the runtime is the user machine
- `Related`: `ANTI-RUST-L3-TAURI-001`, `CTX-RUST-TAURI-001`

### RULE-RUST-L3-UNSAFE-001

- `Layer`: L3
- `Status`: MUST
- `Pattern Name`: Unsafe Containment With Safety Proofs
- `Problem`: one broad unsafe surface can invalidate the guarantees the rest of the system depends on
- `Rule`: Unsafe code MUST be minimized, locally documented with `SAFETY` reasoning, and independently verified where practical
- `Rationale`: unsafe is a boundary contract, not merely a syntax marker
- `When to Use`: FFI, pinning internals, initialization tricks, performance-critical primitives with proven need
- `When Not to Use`: ordinary application logic, avoidable micro-optimization, or convenience around the borrow checker
- `Example Shape`: small private unsafe block inside a safe wrapper with invariants documented
- `Counterexample Shape`: large mixed safe/unsafe function bodies with implicit assumptions
- `Verification`: targeted tests, Miri where supported, sanitizer or FFI harnesses where relevant, review of invariants
- `Evidence Grade`: High
- `Meta Insight`: the safest unsafe code is code whose proof obligations are painfully obvious
- `Related`: `ANTI-RUST-L3-UNSAFE-001`, `CTX-RUST-FFI-001`

### RULE-RUST-L3-UNSAFE-002

- `Layer`: L3
- `Status`: MUST
- `Pattern Name`: Unsafe Islands Behind Safe Facades
- `Problem`: mixed safe and unsafe code spreads proof obligations across too much surface area
- `Rule`: Unsafe implementation details MUST be isolated in the smallest module or helper that can uphold a stable safe interface
- `Rationale`: localizing proof obligations keeps review, refactoring, and testing tractable
- `When to Use`: pointer tricks, FFI shims, custom collections, pinning internals, layout-sensitive code
- `When Not to Use`: code that can remain fully safe without unacceptable performance or compatibility cost
- `Example Shape`: private module with documented unsafe helpers wrapped by safe public methods
- `Counterexample Shape`: large public modules with interleaved safe logic and repeated ad hoc unsafe blocks
- `Verification`: module-level safety review, invariant-focused tests, Miri or sanitizer use where supported
- `Evidence Grade`: High
- `Meta Insight`: unsafe should form an island with a customs checkpoint, not a coastline
- `Related`: `RULE-RUST-L3-UNSAFE-001`, `ARCH-RUST-UNSAFE-001`, `ANTI-RUST-L3-UNSAFE-001`

### RULE-RUST-L3-PERF-001

- `Layer`: L3
- `Status`: SHOULD
- `Pattern Name`: Measure First, Optimize Second
- `Problem`: teams pay complexity costs for optimizations that do not move the real constraint
- `Rule`: Performance-motivated design changes SHOULD start from profiling, representative benchmarks, or a documented asymptotic requirement
- `Rationale`: unmeasured optimization often widens APIs or proof burdens while missing the actual bottleneck
- `When to Use`: hot loops, parser engines, storage paths, allocation reduction work, async throughput changes, binary-size work
- `When Not to Use`: obvious algorithmic fixes with overwhelming evidence and negligible API or correctness risk
- `Example Shape`: profile -> isolate hotspot -> benchmark representative workloads -> optimize and re-measure
- `Counterexample Shape`: introducing unsafe, caching, clone avoidance, or lock-free structures because they "should be faster"
- `Verification`: benchmarks with thresholds, profile deltas, memory or binary-size metrics, and regression checks on worst-case behavior
- `Evidence Grade`: High
- `Meta Insight`: optimization that cannot name its metric is design theater
- `Related`: `RULE-RUST-L2-COLL-001`, `ANTI-RUST-L3-UNSAFE-001`

## 8. Anti-Pattern Catalog

### 8.1 Anti-Pattern Card Template

```md
### ANTI-RUST-<LAYER>-<TOPIC>-<NNN>

- `Layer`:
- `Anti-Pattern Name`:
- `Problem`:
- `Typical Smell`:
- `Why It Fails`:
- `Preferred Alternative`:
- `Exception Case`:
- `Verification`:
- `Related`:
```

### 8.2 Seed Anti-Pattern Card

### ANTI-RUST-L3-ASYNC-001

- `Layer`: L3
- `Anti-Pattern Name`: Blocking Work in Async Paths
- `Problem`: executor starvation and hidden latency spikes
- `Typical Smell`: sync I/O, `std::thread::sleep`, or long CPU work inside async request paths
- `Why It Fails`: unrelated tasks stall and latency becomes nondeterministic
- `Preferred Alternative`: async I/O, bounded worker offload, explicit concurrency limits
- `Exception Case`: tightly bounded startup or one-shot tooling where executor fairness is irrelevant
- `Verification`: stress or latency tests plus review of blocking call sites
- `Related`: `RULE-RUST-L3-ASYNC-002`, `RULE-RUST-L3-ASYNC-003`

### ANTI-RUST-L1-OWN-001

- `Layer`: L1
- `Anti-Pattern Name`: Borrowing By Habit Against Semantic Ownership
- `Problem`: APIs pretend not to own data even when the workflow clearly retains it
- `Typical Smell`: complex lifetimes or hidden clones added only to avoid taking ownership where ownership is natural
- `Why It Fails`: caller and callee semantics drift apart and the implementation becomes brittle
- `Preferred Alternative`: take owned inputs where retained storage or async lifetimes require it
- `Exception Case`: truly local pure transforms with no retention
- `Verification`: API review and ownership-through-lifecycle inspection
- `Related`: `RULE-RUST-L1-OWN-001`

### ANTI-RUST-L1-TYPE-001

- `Layer`: L1
- `Anti-Pattern Name`: Primitive Domain Collapse
- `Problem`: distinct domain meanings are flattened into interchangeable primitives
- `Typical Smell`: `String`, `u64`, or `bool` values reused for multiple semantic roles
- `Why It Fails`: swapped arguments, unchecked values, and unreadable signatures survive code review too easily
- `Preferred Alternative`: newtypes, enums, `TryFrom`, and explicit conversion paths
- `Exception Case`: local glue code with no reuse, no ambiguity, and no trust boundary
- `Verification`: misuse-oriented unit tests and public API review
- `Related`: `RULE-RUST-L1-TYPE-001`, `RULE-RUST-L1-CONV-001`

### ANTI-RUST-L1-STATE-001

- `Layer`: L1
- `Anti-Pattern Name`: Ceremony-Heavy Typestate For Soft Workflows
- `Problem`: typestate is used where ordinary runtime checks would be clearer and cheaper
- `Typical Smell`: marker types and phantom generics around CRUD or loosely coupled business steps
- `Why It Fails`: API complexity rises without proportional correctness gain
- `Preferred Alternative`: runtime validation, explicit enums, or simpler builder validation
- `Exception Case`: protocol sequencing or must-complete lifecycle invariants that truly justify compile-time enforcement
- `Verification`: complexity review and misuse-surface assessment
- `Related`: `RULE-RUST-L1-STATE-001`

### ANTI-RUST-L2-ERR-001

- `Layer`: L2
- `Anti-Pattern Name`: Dynamic Errors As Default Library API
- `Problem`: library callers lose typed handling and compatibility expectations
- `Typical Smell`: public reusable crates returning `anyhow::Error` everywhere
- `Why It Fails`: callers can no longer rely on typed matchable failure contracts
- `Preferred Alternative`: typed library errors, dynamic aggregation only at binary orchestration boundaries
- `Exception Case`: internal-only private crates with no stable public consumers
- `Verification`: public API review and compile-time downstream usage examples
- `Related`: `RULE-RUST-L2-ERR-001`

### ANTI-RUST-L2-ERR-002

- `Layer`: L2
- `Anti-Pattern Name`: Stringly Recovery Logic
- `Problem`: recovery policy depends on error-message wording instead of explicit semantics
- `Typical Smell`: retry, fallback, or escalation branches keyed off substring checks
- `Why It Fails`: message drift, locale changes, and wrapper layers break behavior silently
- `Preferred Alternative`: typed recovery classification, explicit variants, or metadata carrying retryability
- `Exception Case`: extremely local glue over a hostile external API with no typed access and a single choke point
- `Verification`: focused tests for recovery branching
- `Related`: `RULE-RUST-L2-ERR-003`

### ANTI-RUST-L2-ERR-003

- `Layer`: L2
- `Anti-Pattern Name`: Kitchen-Sink Public Error Enum
- `Problem`: one public error type freezes unrelated implementation details and grows without a stable handling story
- `Typical Smell`: a giant enum with variants for every crate, subsystem, and transport failure, including catch-all strings
- `Why It Fails`: callers cannot tell what is meaningfully actionable, semver pressure rises, and internal refactors become API events
- `Preferred Alternative`: use typed local errors at meaningful boundaries, wrap opaque propagation errors where inspection is not the main use case, and translate dependency failures into local concepts
- `Exception Case`: tightly scoped domain APIs where all variants represent stable caller-facing distinctions
- `Verification`: public API review, error-size inspection where relevant, and downstream handling walkthroughs
- `Related`: `RULE-RUST-L2-ERR-001`, `RULE-RUST-L2-API-002`

### ANTI-RUST-L2-ERR-004

- `Layer`: L2
- `Anti-Pattern Name`: Accidental Public Dependency Leakage
- `Problem`: dependency upgrades become breaking API events because third-party types escaped into the public contract by convenience
- `Typical Smell`: public functions, structs, or error variants directly naming dependency types that were never meant to be part of the product identity
- `Why It Fails`: the crate inherits semver and ergonomics decisions from upstream without a deliberate contract review
- `Preferred Alternative`: local façade types, conversion layers, and stable wrappers around upstream details
- `Exception Case`: deliberate re-export or wrapper crate whose purpose is to surface the upstream contract
- `Verification`: semver review, downstream compile examples, and dependency-upgrade impact review
- `Related`: `RULE-RUST-L2-API-002`, `RULE-RUST-L2-ERR-001`

### ANTI-RUST-L2-API-001

- `Layer`: L2
- `Anti-Pattern Name`: Trait And Module Sprawl Without Boundary Justification
- `Problem`: indirection expands faster than the real design pressure
- `Typical Smell`: many tiny traits, wrappers, or modules that exist only to look abstract
- `Why It Fails`: navigation, testing, and change reasoning all get harder without reducing any bug class
- `Preferred Alternative`: add seams only at real external or semantic boundaries
- `Exception Case`: library APIs intentionally preparing for multiple concrete backends with stable semantic contracts
- `Verification`: architecture review and change-surface inspection
- `Related`: `RULE-RUST-L1-TRAIT-001`, `RULE-RUST-L2-API-001`

### ANTI-RUST-L2-ITER-001

- `Layer`: L2
- `Anti-Pattern Name`: Imperative Accumulator Soup
- `Problem`: data-flow intent disappears into mutable plumbing and incidental state
- `Typical Smell`: nested loops with repeated push, temporary flags, and branch-specific accumulation where a clear iterator pipeline or helper would suffice
- `Why It Fails`: transformation boundaries blur and correctness is harder to verify or refactor
- `Preferred Alternative`: iterator pipelines or small named helpers that preserve explicit transformation stages
- `Exception Case`: control-heavy loops where iterator chains would genuinely reduce clarity
- `Verification`: transformation tests and readability review against the simpler alternative
- `Related`: `RULE-RUST-L2-COLL-001`, `RULE-RUST-L2-ITER-001`

### ANTI-RUST-L2-BUILD-001

- `Layer`: L2
- `Anti-Pattern Name`: Mutable Config Blob At Runtime
- `Problem`: construction-time flexibility leaks into steady-state behavior as hidden mutability
- `Typical Smell`: partially filled config structs patched by many call sites before each use
- `Why It Fails`: invariants become timing-dependent and it becomes unclear when configuration is actually valid
- `Preferred Alternative`: builder validates once, then yields a frozen runtime config
- `Exception Case`: truly interactive editors or admin tools where mutation is the product behavior
- `Verification`: builder validation tests and runtime immutability review
- `Related`: `RULE-RUST-L2-BUILD-001`, `ANTI-RUST-L1-STATE-001`

### ANTI-RUST-L2-DTOR-001

- `Layer`: L2
- `Anti-Pattern Name`: Fallible Or Blocking Destructor Cleanup
- `Problem`: resource teardown semantics disappear into `Drop`, where failure and latency cannot be controlled sanely
- `Typical Smell`: destructors performing I/O, waiting on tasks, acquiring contended locks, or panicking when cleanup fails
- `Why It Fails`: drop timing becomes part of correctness without an explicit call site, and panics during teardown are especially hazardous
- `Preferred Alternative`: explicit close or shutdown APIs with tests, leaving `Drop` to best-effort local release
- `Exception Case`: simple in-memory cleanup that cannot fail and does not block
- `Verification`: explicit close-path tests, teardown timing review, and panic-path inspection
- `Related`: `RULE-RUST-L2-DTOR-001`, `RULE-RUST-L3-ASYNC-004`

### ANTI-RUST-L2-WS-001

- `Layer`: L2
- `Anti-Pattern Name`: Implicit Workspace And Feature Coupling
- `Problem`: the repo builds only because developers remember undocumented feature or toolchain assumptions
- `Typical Smell`: duplicated dependency versions, surprising default features, or root-only tribal commands
- `Why It Fails`: CI drift, local build breakage, and accidental compatibility regressions follow
- `Preferred Alternative`: explicit workspace config, pinned conventions, additive features, root-level gates
- `Exception Case`: single-crate experiments not intended for team or long-term reuse
- `Verification`: root workspace build, feature matrix checks, and release review
- `Related`: `RULE-RUST-L2-WS-001`

### ANTI-RUST-L3-CONC-001

- `Layer`: L3
- `Anti-Pattern Name`: Lock Guards Across Await
- `Problem`: interleavings become brittle and deadlock risk rises sharply
- `Typical Smell`: guard acquisition followed by network, file, timer, or channel await
- `Why It Fails`: lock ownership outlives the reasoning window and fairness disappears
- `Preferred Alternative`: copy or extract needed data before suspension, then reacquire if necessary
- `Exception Case`: none by default; exceptional designs require unusually strong proof
- `Verification`: code review, stress tests, and concurrency modeling when warranted
- `Related`: `RULE-RUST-L3-ASYNC-002`

### ANTI-RUST-L3-CONC-002

- `Layer`: L3
- `Anti-Pattern Name`: Fire-And-Forget Task Architecture
- `Problem`: lifecycle, cancellation, and failure paths are unowned
- `Typical Smell`: spawned tasks with no join path, no shutdown path, and no failure observation
- `Why It Fails`: leaks, partial shutdown, hidden panics, and stale state follow
- `Preferred Alternative`: structured concurrency, supervisors, `JoinSet`, bounded channels, explicit cancellation tokens
- `Exception Case`: intentionally lossy telemetry or metrics emission with bounded impact
- `Verification`: teardown, shutdown, and error-propagation tests
- `Related`: `RULE-RUST-L3-CONC-001`, `RULE-RUST-L3-ASYNC-003`

### ANTI-RUST-L3-OBS-001

- `Layer`: L3
- `Anti-Pattern Name`: Unstructured Boundary Logging
- `Problem`: failures span tasks or IO boundaries without stable diagnostic context
- `Typical Smell`: free-form strings, missing IDs, and inconsistent field naming at orchestration boundaries
- `Why It Fails`: operators and reviewers cannot reconstruct what happened without reading code
- `Preferred Alternative`: structured tracing with stable fields, error context, and correlation identifiers
- `Exception Case`: tiny local tools where one synchronous path is obvious and transient
- `Verification`: log-shape review and failure-path dry runs
- `Related`: `RULE-RUST-L3-OBS-001`

### ANTI-RUST-L3-BOUNDARY-001

- `Layer`: L3
- `Anti-Pattern Name`: Transport Types Leaking Inward
- `Problem`: domain logic silently depends on request shape and optional raw data
- `Typical Smell`: handlers, services, and persistence all share the same DTO struct
- `Why It Fails`: invariants stay partial and every deeper layer must re-decide what is valid
- `Preferred Alternative`: convert DTOs to domain commands or values at the edge
- `Exception Case`: none when the input boundary is untrusted or loosely shaped
- `Verification`: boundary conversion tests and service-core type review
- `Related`: `RULE-RUST-L3-BACKEND-001`

### ANTI-RUST-L3-TAURI-001

- `Layer`: L3
- `Anti-Pattern Name`: Broad Desktop Privilege And Unchecked Sidecars
- `Problem`: desktop integrations silently become security and operability liabilities
- `Typical Smell`: wide filesystem grants, generic shell authority, or sidecars with no health checks or ownership
- `Why It Fails`: least-privilege and lifecycle guarantees disappear
- `Preferred Alternative`: granular capabilities, exact sidecar scoping, startup bounds, supervised lifecycle
- `Exception Case`: none by default in user-machine desktop software
- `Verification`: capability review, command-path tests, startup timeout checks
- `Related`: `RULE-RUST-L3-TAURI-001`

### ANTI-RUST-L3-UNSAFE-001

- `Layer`: L3
- `Anti-Pattern Name`: Speculative Unsafe Or Lock-Free Cleverness
- `Problem`: complexity and proof burden rise before the problem truly requires it
- `Typical Smell`: unsafe blocks or lock-free structures added for anticipated performance wins without measurement or verification
- `Why It Fails`: the system inherits proof obligations it does not actually need
- `Preferred Alternative`: safe baseline first, then narrow unsafe only after measurement and proof planning
- `Exception Case`: proven bottlenecks or unavoidable FFI/ABI requirements
- `Verification`: benchmark evidence plus invariant review and dedicated tooling where possible
- `Related`: `RULE-RUST-L3-UNSAFE-001`

### ANTI-RUST-L1-OWN-002

- `Layer`: L1
- `Anti-Pattern Name`: Clone To Satisfy The Borrow Checker
- `Problem`: ownership pressure is masked by cloning instead of being designed explicitly
- `Typical Smell`: clones sprinkled through core paths with no semantic explanation other than "it compiles this way"
- `Why It Fails`: hidden allocation, stale ownership boundaries, and harder-to-evolve APIs accumulate
- `Preferred Alternative`: redesign ownership, shorten borrows, restructure control flow, or move data once where ownership is actually needed
- `Exception Case`: cheap `Copy`-like semantics or explicitly measured clones at cold boundaries
- `Verification`: allocation review, hot-path benchmarks where relevant, and ownership-through-lifecycle inspection
- `Related`: `RULE-RUST-L1-OWN-001`, `RULE-RUST-L3-PERF-001`

### ANTI-RUST-L2-VERIFY-001

- `Layer`: L2
- `Anti-Pattern Name`: Compiler Acceptance As Proof Of Correctness
- `Problem`: semantic, compatibility, and concurrency risks are ignored because the code compiles cleanly
- `Typical Smell`: "the borrow checker would have complained" used as the main justification for logical behavior
- `Why It Fails`: the compiler does not prove domain invariants, shutdown semantics, public API stability, or performance claims
- `Preferred Alternative`: pair compile-time guarantees with behavior tests, boundary review, and explicit operational verification
- `Exception Case`: none when the claim extends beyond pure type or memory safety
- `Verification`: regression tests, integration tests, and claim-specific evidence such as benchmarks or shutdown tests
- `Related`: `RULE-RUST-L1-VALIDATE-001`, `RULE-RUST-L3-ASYNC-004`, `RULE-RUST-L3-PERF-001`

### ANTI-RUST-L3-TOOL-001

- `Layer`: L3
- `Anti-Pattern Name`: Hand-Edited Generated Source As Ground Truth
- `Problem`: generated code becomes a maintenance trap because human fixes live in files that should be reproducible artifacts
- `Typical Smell`: direct edits inside `generated/`, `prost`, `pb`, or codegen output that are not reflected in the generator or wrapper layer
- `Why It Fails`: regeneration discards fixes, review context becomes misleading, and the semantic boundary between source and artifact collapses
- `Preferred Alternative`: edit the schema, generator configuration, or thin wrapper modules that own the real contract
- `Exception Case`: none by default; even temporary patches should be isolated and replaced quickly
- `Verification`: regeneration checks, wrapper tests, and codegen reproducibility review
- `Related`: `RULE-RUST-L2-DTOR-001`, `RULE-RUST-L3-UNSAFE-002`

## 9. Architectural Patterns

This section captures patterns that are larger than a single function but smaller than full domain playbooks.

Architectural pattern card:

```md
### ARCH-RUST-XXX-???

- `Pattern Name`:
- `Problem`:
- `Boundary Split`:
- `Preferred Shape`:
- `Tradeoffs`:
- `When to Use`:
- `When Not to Use`:
- `Verification`:
- `Related Rules`:
```

### ARCH-RUST-BOUNDARY-001

- `Pattern Name`: Sync Core With Async Shell
- `Problem`: async runtime concerns and I/O details infect pure domain logic
- `Boundary Split`: async handlers, workers, and adapters on the outside; sync domain and policy logic in the core where possible
- `Preferred Shape`: parse and fetch outside, decide and transform inside, then persist or emit outside
- `Tradeoffs`: some duplication at the shell boundary; improved testability and clearer ownership in return
- `When to Use`: services, CLIs with I/O phases, background pipelines, desktop commands
- `When Not to Use`: tiny purely async libraries where the abstraction split would be artificial
- `Verification`: unit tests for core logic, integration tests for shell orchestration
- `Related Rules`: `RULE-RUST-L1-TRAIT-001`, `RULE-RUST-L3-ASYNC-003`

### ARCH-RUST-BOUNDARY-002

- `Pattern Name`: Transport, Domain, Persistence Separation
- `Problem`: request or storage shapes dictate business logic and weaken invariants
- `Boundary Split`: transport DTOs -> domain commands and values -> persistence rows and queries
- `Preferred Shape`: convert at the edge, enforce invariants in domain types, isolate storage specifics in adapters
- `Tradeoffs`: more conversion code; better invariants, reuse, and clearer failure localization
- `When to Use`: HTTP or RPC services, queue consumers, protocol decoders, IPC boundaries
- `When Not to Use`: simple purely internal data plumbing with no trust boundary
- `Verification`: conversion tests, integration tests across the boundary, review of domain type purity
- `Related Rules`: `RULE-RUST-L1-TYPE-001`, `RULE-RUST-L1-CONV-001`, `RULE-RUST-L3-BACKEND-001`

### ARCH-RUST-API-001

- `Pattern Name`: Curated Public Facade With Internal Depth
- `Problem`: callers inherit internal file or module history as API surface
- `Boundary Split`: narrow public entrypoints and richer private/internal organization
- `Preferred Shape`: expose curated types and functions through stable modules or re-exports, keep implementation churn behind them
- `Tradeoffs`: requires deliberate API curation and semver thinking
- `When to Use`: libraries, shared internal platform crates, SDK-style packages
- `When Not to Use`: throwaway binaries with no meaningful consumer API
- `Verification`: doctest examples, semver review, external-usage walkthrough
- `Related Rules`: `RULE-RUST-L2-API-001`, `RULE-RUST-L2-ERR-001`

### ARCH-RUST-WS-001

- `Pattern Name`: Workspace Layering Around Change Boundaries
- `Problem`: crates accrete based on chronology instead of ownership, testability, and release pressure
- `Boundary Split`: core domain crates, adapter crates, binary or command crates, optional proc-macro or tooling crates
- `Preferred Shape`: split by stable responsibility and dependency direction, not by arbitrary file count
- `Tradeoffs`: more manifests and explicit wiring; better build clarity and ownership boundaries
- `When to Use`: multi-binary repos, shared libraries, platform plus adapters, desktop apps with sidecars or shared core
- `When Not to Use`: tiny single-crate apps where extra crate boundaries add no decision value
- `Verification`: workspace graph review, root builds, dependency direction inspection
- `Related Rules`: `RULE-RUST-L2-WS-001`, `RULE-RUST-L1-TRAIT-001`

### ARCH-RUST-ADAPTER-001

- `Pattern Name`: Trait-Seamed External Adapter
- `Problem`: core logic is entangled with concrete IO, DB, HTTP, or process details
- `Boundary Split`: domain depends on behavior contracts; adapters own concrete clients and side effects
- `Preferred Shape`: small behavior trait plus concrete adapter module and integration tests
- `Tradeoffs`: additional abstraction and test doubles; lower coupling and clearer failure ownership
- `When to Use`: DB stores, third-party APIs, subprocesses, queues, file systems, time providers
- `When Not to Use`: pure transforms or local helpers with no meaningful side-effect boundary
- `Verification`: fake-based unit tests plus real-adapter integration tests
- `Related Rules`: `RULE-RUST-L1-TRAIT-001`, `RULE-RUST-L2-ERR-002`

### ARCH-RUST-UNSAFE-001

- `Pattern Name`: Unsafe Island With Safe Customs Gate
- `Problem`: unsafe proof obligations leak through modules and APIs that should otherwise be ordinary safe Rust
- `Boundary Split`: tiny private unsafe implementation core surrounded by a documented safe facade and tests
- `Preferred Shape`: wrapper module owns invariants, public methods stay safe, internal helpers carry local `SAFETY` reasoning
- `Tradeoffs`: extra wrapper code and review ceremony; dramatically clearer proof boundaries
- `When to Use`: FFI shims, custom buffers, intrusive data structures, pinning internals, uninitialized-memory patterns
- `When Not to Use`: when safe Rust can solve the problem at acceptable cost
- `Verification`: invariant-focused tests, Miri where supported, code review of every safety assumption
- `Related Rules`: `RULE-RUST-L3-UNSAFE-001`, `RULE-RUST-L3-UNSAFE-002`

### ARCH-RUST-COMP-001

- `Pattern Name`: Internal Composition Behind Stable External API
- `Problem`: high-performance or evolving internals force breaking changes because the external contract mirrors the implementation too closely
- `Boundary Split`: stable, minimal public API outside; composable interchangeable engines or strategies inside
- `Preferred Shape`: external callers depend on a narrow contract while internal modules compose specialized strategies chosen by the implementation
- `Tradeoffs`: more internal indirection and documentation effort; better optimization freedom and lower semver pressure
- `When to Use`: parser engines, search/index systems, storage adapters, execution planners, performance-critical libraries
- `When Not to Use`: tiny single-strategy libraries where internal composition would be speculative
- `Verification`: benchmark comparisons across strategies, stable API review, and tests that assert behavior rather than internal engine choice
- `Related Rules`: `RULE-RUST-L2-API-002`, `RULE-RUST-L3-PERF-001`

### ARCH-RUST-TAURI-001

- `Pattern Name`: Frontend, IPC, Rust Core, And Capability Split
- `Problem`: desktop code mixes frontend transport, command handlers, side effects, and privilege decisions into one surface
- `Boundary Split`: frontend UI -> typed IPC contract -> Rust core/workflows -> capability and sidecar boundary
- `Preferred Shape`: typed command modules, managed state, explicit permissions, explicit sidecar ownership
- `Tradeoffs`: more setup files and capability discipline; stronger desktop correctness and security
- `When to Use`: Tauri applications with filesystem, plugin, tray, updater, deep-link, or sidecar behavior
- `When Not to Use`: non-desktop Rust systems
- `Verification`: command tests, permission review, sidecar lifecycle tests, startup and restore behavior checks
- `Related Rules`: `RULE-RUST-L3-TAURI-001`, `ANTI-RUST-L3-TAURI-001`

## 10. Error and Recovery Taxonomy

Map failures by cause, boundary, caller action, and proof burden.

| Error Class | Typical Boundary | Recovery Strategy | Representation | Required Tests |
| --- | --- | --- | --- | --- |
| validation | parse or input edge | reject with explicit reason | typed parse or domain validation error | malformed input cases |
| business rule | domain workflow | reject with precise business outcome | named domain error or outcome enum | behavior tests |
| transient external | network, storage, subprocess, queue | retry, degrade, or reschedule | retryable metadata or dedicated variant | retry behavior |
| permanent external | auth, contract mismatch, schema mismatch | fail fast, escalate, or surface repair action | typed permanent error | non-retry behavior |
| internal invariant breach | core domain | impossible by construction or fail fast | impossible state or tightly scoped panic | invariant tests |
| timeout | async orchestration | fail, retry, or cancel explicitly | timeout-aware typed error | timeout tests |
| cancellation | task or workflow boundary | cooperative stop with clear ownership | explicit cancel-aware path | cancel tests |
| backpressure or overload | queue, worker pool, stream | reject, shed, buffer, or apply bounded wait | explicit saturation result | overload tests |
| FFI or unsafe boundary | ABI or memory ownership boundary | convert, abort, or isolate failure clearly | safe wrapper error contract | harness and invariant tests |
| cleanup or teardown | close or shutdown boundary | explicit close, best-effort drop, or escalate | typed close error or shutdown result | close-path and teardown tests |
| public dependency leakage | public library surface | wrap, translate, or deliberately re-export | local facade type or explicit re-export contract | semver and downstream compile review |

Error taxonomy rules:

- Library errors MUST be typed.
- Dynamic aggregation belongs at top-level orchestration or binary surfaces, not as the default reusable contract.
- Error messages SHOULD answer what failed, where it failed, and what the caller or operator should do next.
- Recovery policy MUST NOT depend on string matching unless trapped behind a single well-tested choke point.
- Binary or non-UTF-8 input boundaries MUST preserve diagnostic usefulness without assuming text.
- If the caller must branch programmatically, expose stable structured information.
- If the caller mostly propagates the error upward, prefer contextual opacity over freezing every implementation detail into the public ABI.
- Public dependency types in errors SHOULD be wrapped or translated unless re-export is a conscious compatibility promise.
- Large cold-path error payloads SHOULD be boxed or layered carefully when they would bloat hot-path results or public ABI shape.

## 11. Async and Concurrency Doctrine

### 11.1 Non-Negotiables

- No blocking work in async hot paths.
- No lock guards across `.await`.
- No hidden unbounded queues in long-lived systems.
- No detached background task architecture without explicit lifecycle ownership.
- No concurrency claim without either reasoning, stress evidence, or model checking appropriate to the risk.

### 11.2 Primitive Choice Matrix

| Concern | Preferred Primitive | Use When | Avoid When |
| --- | --- | --- | --- |
| one producer to one or many workers | bounded `mpsc` | buffering must be explicit and backpressure matters | if consumers need replay or state snapshots |
| latest state broadcast | `watch` | only latest value matters | history or every event matters |
| every subscriber receives events | `broadcast` | bounded event fan-out is needed | slow consumers cannot be tolerated or message loss is unacceptable |
| shared mutable state | `Mutex` or `RwLock` | true shared mutation is simpler than message passing | if ownership can be localized instead |
| global one-time state | `OnceLock` / `LazyLock` | initialization is one-shot | mutable lifecycle or reset is required |
| task orchestration | `JoinSet` or explicit task scope | parent owns task lifecycle | detached long-lived background work is being hand-waved |
| concurrency limiting | `Semaphore` | parallel work count must be bounded | work is strictly sequential or already bounded elsewhere |

### 11.3 Cancellation Doctrine

- Long-running operations MUST state whether they are cancel-safe, restartable, resumable, or lossy under cancellation.
- `tokio::select!` and similar branching MUST be written with awareness of partially consumed state.
- If partial progress matters, persist intent or structure the workflow so interruption cannot corrupt state silently.
- In async Rust, cancellation normally happens by dropping a future; code SHOULD assume any `.await` point may be the cut line.
- Branches that lose a `select!` race are dropped, so branch-local state and cleanup obligations MUST be designed with drop-as-cancellation in mind.
- Cancellation tokens or explicit shutdown channels SHOULD be preferred over ad hoc boolean flags once multiple tasks or ownership domains are involved.

### 11.4 Backpressure Doctrine

- If producers can outpace consumers, the system MUST define a saturation policy.
- Saturation policy may be reject, wait, shed, batch, or durable offload, but it must be explicit.
- "The queue should probably stay small" is not a policy.

### 11.5 Shared State Doctrine

- Shared mutable state SHOULD be narrow, typed, and owned deliberately.
- `Arc<Mutex<T>>` is a tool, not a design.
- Prefer message passing when it collapses correctness questions better than shared mutation does.
- Prefer immutable snapshots or owned work packets when lock contention would otherwise dominate reasoning.

### 11.6 Concurrency Verification Expectations

- High-risk interleavings SHOULD receive `loom` or equivalent model checking where practical.
- Lower-risk concurrent code SHOULD still receive stress, timeout, teardown, and cancellation tests.
- A single green CI run proves almost nothing about concurrency.

### 11.7 Shutdown And Teardown Semantics

- Systems with owned background tasks MUST define who initiates shutdown, how the signal fans out, and how completion is awaited.
- Explicit `shutdown` or `close` paths SHOULD perform coordinated cleanup; `Drop` should only perform bounded, synchronous best effort.
- If teardown can block on I/O or task completion, the blocking path MUST be explicit in control flow and tests.
- Shutdown code SHOULD remain idempotent or clearly document repeated-call behavior.

### 11.8 Async Cleanup Caveat

- Rust does not provide async destructors; designs requiring awaited cleanup MUST expose explicit async cleanup APIs.
- Do not rely on cancellation alone for soundness or business invariants.
- If cleanup is required for protocol correctness, that requirement belongs in the API contract and verification plan.

## 12. TDD and Verification Matrix

Map risk surface to test type deliberately.

| Risk Surface | Preferred Tests | Notes |
| --- | --- | --- |
| pure logic | unit + property | keep deterministic and exhaustive over invariants where possible |
| public API contract | unit + doctest + misuse cases | enforce caller story and documentation truth |
| persistence or I/O | integration | verify side effects and boundary shaping |
| async orchestration | integration + timeout + cancellation | prove lifecycle and partial-progress behavior |
| concurrency | stress + `loom` where justified | avoid false confidence from one run |
| parsing or protocol | corpus + malformed input + property + fuzz | boundary discipline matters most here |
| compile-time misuse | compile-fail UI tests | use when types are the intended guardrail |
| performance claim | benchmark with threshold | no vague speed claims |
| unsafe or FFI boundary | harness + Miri/sanitizer where feasible | prove wrapper invariants, not only happy paths |

### 12.1 Test Progression

- `STUB`: write failing test skeletons or executable contract stubs first
- `RED`: prove the intended failure actually fails for the right reason
- `GREEN`: implement the smallest change that satisfies the current slice
- `REFACTOR`: improve structure without relaxing coverage
- `VERIFY`: run the full relevant gate set before claiming completion

### 12.2 Bug-Fix Rule

For bug fixes:

1. reproduce the bug
2. write or strengthen a regression test
3. see the test fail on the broken state
4. apply the fix
5. see the regression test and broader suite pass

Do not claim a regression test exists if it was never observed failing against the broken behavior.

### 12.3 Checkpoint Discipline

For long or interrupted TDD sessions, capture:

- current red, green, or refactor state
- exact failing tests or pending gates
- files or modules touched
- unresolved design or verification questions

Checkpointing is not a substitute for tests.
It is a guard against context drift between valid red-green iterations.

### 12.4 Verification Mix Rules

- Unit tests SHOULD cover local pure logic and invariant-preserving helpers.
- Integration tests MUST cover cross-boundary behavior and side effects.
- Doctests SHOULD be used for public library usage contracts.
- Compile-fail tests SHOULD back patterns whose main value is misuse prevention.
- Property tests SHOULD back parsing, round-trip, normalization, and algebraic invariants.
- Fuzzing SHOULD back parser, decoder, and protocol frontiers where malformed input risk is real.
- Benchmarks MUST back performance claims.

### 12.5 Performance And Profiling Verification

- Profile before optimization when the bottleneck is not already obvious and localized.
- Benchmark inputs SHOULD reflect realistic sizes and worst-case pressure where algorithmic guarantees matter.
- Performance regressions SHOULD be tracked against a named metric: latency, throughput, memory, binary size, or compile time.
- Benchmarks without acceptance thresholds are evidence of curiosity, not evidence of a satisfied performance contract.

### 12.6 Differential And Adversarial Testing

- Parser, codec, and protocol edges SHOULD use malformed corpora and adversarial inputs, not only golden happy paths.
- Differential tests SHOULD be used when two implementations or old/new engines can validate one another cheaply.
- Generated-code wrappers SHOULD be tested at the wrapper seam, not merely by trusting regeneration.

## 13. Quality Gates

### 13.1 Default Gates

- `cargo fmt --all -- --check`
- `cargo clippy --all-targets --all-features -- -D warnings`
- `cargo test --all-targets --all-features`
- `cargo build --all-targets --all-features`

### 13.2 Conditional Gates

Use when the boundary or claim requires them:

- `cargo test --doc`
- `cargo doc --no-deps`
- compile-fail UI tests
- property tests
- fuzz targets
- `loom`
- `cargo llvm-cov --workspace --branch --fail-under-lines 75`
- `cargo miri test`
- supply-chain or policy checks such as `cargo deny` or equivalent
- targeted benchmarks with thresholds

### 13.3 Gate Function

Before any completion claim:

1. identify which command proves the claim
2. run the full relevant command fresh
3. inspect output and exit status
4. report the actual result
5. only then claim success or incompleteness

### 13.4 Gate Fail Conditions

No completion claim should survive if:

- requirement coverage is missing
- failure paths are untested where they matter
- performance claims lack evidence
- concurrency assumptions are hand-waved
- cancellation or shutdown semantics are unspecified for long-running tasks
- public API changes were made without compatibility thought

### 13.5 API, Unsafe, And Generated-Code Gates

- Public API changes SHOULD receive a semver review focused on leaked dependency types, error surfaces, and curated re-exports.
- Unsafe code changes MUST include local `SAFETY` reasoning and targeted invariant verification.
- Generated sources SHOULD be regenerated or diff-checked from their true inputs rather than manually patched in place.
- Clippy suppressions SHOULD be reviewed as design decisions, not left as unexplained noise.

### 13.6 Release Readiness Checklist

- build is green from the right root
- lint and format gates pass
- tests match the risk surface touched
- error behavior is explicit and reviewable
- tracing, logs, or diagnostics are sufficient for operations
- secret handling is safe
- docs and doctests are synchronized where public behavior changed

## 14. Domain Context Packs

Each context pack stays short and operational.

Context pack template:

```md
### CTX-RUST-<DOMAIN>-???

- `Use For`:
- `Practical Path`:
- `Stretch Path`:
- `Recommended Crates by Concern`:
- `Main Risks`:
- `Verification Focus`:
- `When Rust Is the Wrong Tool`:
```

### CTX-RUST-CLI-001

- `Use For`: command-line apps, batch processors, and one-shot automation
- `Practical Path`: `clap` for CLI, `tracing` for diagnostics, `ExitCode` for process semantics, typed config parsing at startup
- `Stretch Path`: richer progress output, structured diagnostics, plugin or workspace-style subcommand architectures
- `Recommended Crates by Concern`: `clap`, `tracing`, `anyhow` at `main`, `thiserror` for reusable core, `serde`, `toml` or `serde_json`
- `Main Risks`: ambiguous exit behavior, config parsing drift, poor diagnostics, accidental blocking or unbounded memory on large input
- `Verification Focus`: command golden tests, config parse failures, exit-code tests, large-input behavior
- `When Rust Is the Wrong Tool`: ultra-short scripts where startup speed of implementation matters more than long-term reliability

### CTX-RUST-BACKEND-001

- `Use For`: HTTP services, workers, auth flows, persistence-backed orchestration
- `Practical Path`: transport DTO -> domain conversion at the edge, typed state and services, explicit timeout and retry policy, `tracing`, pooled DB access
- `Stretch Path`: idempotency keys, durable intent plus background processing, compile-time query checks, richer observability and overload control
- `Recommended Crates by Concern`: `axum` or equivalent, `tokio`, `tracing`, `sqlx`, `serde`, `thiserror`, `tower`, testcontainers or equivalent if needed
- `Main Risks`: DTO leakage inward, hidden retry semantics, timeout ambiguity, auth leakage, transaction and remote side-effect coupling
- `Verification Focus`: handler integration tests, malformed input, timeout and retry behavior, transaction boundaries, failure shaping
- `When Rust Is the Wrong Tool`: deadline-driven prototypes where compile-debug tax overwhelms delivery value and a typed service is not actually required

### CTX-RUST-LIB-001

- `Use For`: reusable crates, SDKs, shared internal platform libraries, public domain packages
- `Practical Path`: curated public facade, typed errors, minimal dependency leakage, doctests for caller stories, additive features
- `Stretch Path`: semver-aware layering, internal engine composition, feature-matrix verification, optional zero-copy or no-std-friendly surfaces where justified
- `Recommended Crates by Concern`: `thiserror`, `proptest`, `criterion`, `cargo-semver-checks` or equivalent if available, `tracing` only where library-level diagnostics are part of the contract
- `Main Risks`: accidental public dependency exposure, kitchen-sink errors, unstable re-export sprawl, undocumented feature interactions
- `Verification Focus`: doctests, downstream-usage examples, semver review, feature matrix tests, benchmark evidence for performance claims
- `When Rust Is the Wrong Tool`: when the real need is a tiny one-off binary or script and no reusable contract will survive the first week

### CTX-RUST-PARSER-001

- `Use For`: parsers, decoders, protocol frontiers, binary or text ingest
- `Practical Path`: explicit frontier types, corpus tests, malformed input handling, binary-safe diagnostics, property tests for round trips
- `Stretch Path`: zero-copy boundaries where justified, fuzzing, state-machine or typestate-assisted protocol handling
- `Recommended Crates by Concern`: `nom` or hand-written parser, `proptest`, `arbitrary`, `cargo-fuzz`, `thiserror`
- `Main Risks`: partial parses treated as success, UTF-8 assumptions, panic-on-bad-input, ambiguous recovery, protocol state corruption
- `Verification Focus`: malformed corpus, property tests, fuzzing, round-trip invariants, non-UTF-8 cases
- `When Rust Is the Wrong Tool`: none by default if parser correctness is central; the only weak fit is throwaway quick-and-dirty parsing with minimal lifetime value

### CTX-RUST-TAURI-001

- `Use For`: Tauri desktop apps with commands, managed state, sidecars, tray, updater, deep links, or window-specific privileges
- `Practical Path`: owned async commands, explicit managed state, narrow capabilities, exact sidecar scoping, typed IPC contracts
- `Stretch Path`: generated command bindings, supervised sidecar protocols, platform-merge discipline, deep-link and single-instance choreography
- `Recommended Crates by Concern`: Tauri core and official plugins, `thiserror`, `serde`, `tokio`, optionally `specta` or similar when bindings justify it
- `Main Risks`: broad permissions, borrowed async inputs, hidden sidecar lifecycle, large payloads in JSON IPC, overlapping high-privilege windows
- `Verification Focus`: command tests, capability review, startup timeout, sidecar health checks, restore and first-paint behavior, deep-link handoff
- `When Rust Is the Wrong Tool`: when the real problem is frontend-only behavior and desktop-native boundaries are not materially involved

### CTX-RUST-FFI-001

- `Use For`: C ABI boundaries, unsafe wrappers, external library integration, performance primitives with justified unsafe
- `Practical Path`: smallest possible safe wrapper, explicit ownership and nullability, layout discipline, private unsafe core
- `Stretch Path`: richer bindgen or handwritten wrapper separation, panic containment, niche optimization only after proof and measurement
- `Recommended Crates by Concern`: `thiserror`, `libc` or binding crates, `bindgen` if appropriate, `cxx` or equivalent when the model fits, Miri where supported
- `Main Risks`: layout mismatch, aliasing violations, panic crossing FFI, invalid lifetimes, unverifiable "trust me" unsafe
- `Verification Focus`: harness tests, invariant review, Miri or sanitizer support where feasible, ABI shape review, ownership transfer tests
- `When Rust Is the Wrong Tool`: when the integration surface is so dynamic or reflection-heavy that safe, maintainable boundary modeling is disproportionate to the problem

### CTX-RUST-PERF-001

- `Use For`: parser engines, data pipelines, hot loops, memory-sensitive services, binary-size or compile-time optimization work
- `Practical Path`: establish representative benchmark cases, profile first, prefer algorithmic wins and boundary simplification before unsafe or lock-free tricks
- `Stretch Path`: worst-case complexity guards, cache-aware data layout, allocation budgets, engine composition that preserves stable APIs while enabling strategy variation
- `Recommended Crates by Concern`: `criterion`, `iai-callgrind` or equivalent, `proptest`, `cargo-bloat`, flamegraph tools, profiling support appropriate to the platform
- `Main Risks`: optimizing the wrong metric, overfitting microbenchmarks, freezing internals into public APIs, unsafe complexity without proof
- `Verification Focus`: profile deltas, thresholded benchmarks, memory and binary-size checks, regression tests for worst-case behavior
- `When Rust Is the Wrong Tool`: when the dominant latency is outside the process and the team is using Rust complexity to avoid measuring the real system

## 15. Exception and Waiver Rules

Use a waiver only when a rule is materially wrong for the specific context.

Waiver template:

```md
### WAIVER-RUST-???

- `Rule ID`:
- `Scope`:
- `Reason`:
- `Compensating Control`:
- `Verification Added`:
- `Expiry or Review Trigger`:
```

Waiver rules:

- A waiver MUST reference the exact rule being waived.
- Scope MUST be minimal and concrete.
- The compensating control MUST address the specific risk the rule was preventing.
- Verification added by the waiver MUST be stricter than the baseline for that area.
- Waivers SHOULD expire on the next relevant refactor, release boundary, or architectural review.
- Waivers around unsafe, shutdown semantics, or public API leakage MUST name the specific owner and review trigger explicitly.
- Waivers MUST NOT convert hidden cleanup, hidden background ownership, or hidden dependency commitments into "temporary" defaults without a replacement plan.

Common invalid waivers:

- "too much work right now"
- "we know this is safe"
- "we will test later"
- "the compiler is annoying"
- "the framework makes this awkward"

## 16. Review Interrogation Checklist

Use these questions in `Review Mode`.

### 16.1 Types and Invariants

- What invariant is currently carried only by comments, not types or tests?
- Which primitives represent domain concepts that should be distinct?
- Where would a newtype, enum, or `TryFrom` remove a whole bug class?

### 16.2 Ownership and API Surface

- Where does ownership look accidental rather than intentional?
- Which function is taking ownership only because the implementation is convenient?
- Which function is borrowing only because the author feared moving, even though ownership is semantically correct?
- Which public API would be painful to evolve because it leaks internal storage or adapter shape?

### 16.3 Error and Recovery

- Which error path forces callers to guess recovery strategy?
- Are typed and dynamic errors used at the right layer?
- Where does error context become too vague to diagnose quickly?
- Are non-UTF-8 or binary boundaries handled safely?
- Which public error or type has accidentally committed the crate to a dependency's semver?

### 16.4 Async and Concurrency

- Where is async behavior underspecified under cancellation or timeout?
- Which queue, channel, or task fan-out lacks an explicit bound or saturation policy?
- Which clone, allocation, or lock is hiding a boundary mistake?
- Is any task spawned without clear ownership, shutdown, and error visibility?
- Does any cleanup path require awaiting, blocking, or remote coordination without an explicit shutdown API?
- Where could logical races still exist even though the code is data-race-free?

### 16.5 Architecture and Boundaries

- Are transport, domain, and persistence shapes properly separated?
- Does any framework type leak too far inward?
- Are trait seams present at real external boundaries and absent where they would only add ceremony?
- Is workspace or feature discipline explicit enough for a fresh contributor or agent to succeed?
- Which generated or codegen-owned surface is being treated as if it were hand-authored doctrine?

### 16.6 Verification and Completion Honesty

- Does each important claim have fresh evidence?
- Are bug fixes backed by a real failing-then-passing regression proof?
- Does the test mix match the actual risk surface, or only the easiest local unit cases?
- Where is the document or PR overclaiming confidence?
- Which performance claim lacks a benchmark threshold or profile-backed justification?

### 16.7 Abstraction Skepticism

- Which abstraction is clever but not yet justified by reuse, invariants, or compatibility pressure?
- Where is unsafe, proc-macro, lock-free, or typestate complexity being used as sophistication theater?
- Would a simpler boundary yield clearer guarantees?

## 17. Glossary

| Term | Working Meaning |
| --- | --- |
| invalid state | a state the program should make impossible or detect immediately |
| boundary | a place where unchecked data, control, or side effects enter or leave a component |
| typed invariant | a correctness property encoded in the type system |
| recovery strategy | what the caller should do after failure |
| transport type | a shape used for request, response, payload, or wire-level parsing |
| domain type | a value whose invariants are intended to hold throughout the business core |
| structured concurrency | task ownership where lifecycle, shutdown, and failure propagation are explicit |
| cancel-safe | safe under interruption without silent corruption or lost invariants |
| backpressure | the explicit policy that limits or shapes producer pressure against slower consumers |
| context pack | a scoped appendix for a particular Rust domain |
| soundness | the guarantee that safe Rust cannot trigger Undefined Behavior |
| minimal exception safety | unsafe or low-level code remains memory-safe even if unwinding happens at awkward moments |
| maximal exception safety | the program remains semantically correct, not merely memory-safe, when panics or early exits occur |
| semver leakage | accidental exposure of a dependency or internal detail as part of the stable public contract |
| opaque error | an error surface meant mainly for propagation and display, not detailed caller matching |
| kitchen-sink error | a broad error enum that mixes unrelated failure categories and freezes implementation detail |
| cancellation point | a place where async execution may stop because the future is dropped, typically at an `.await` boundary |
| generated surface | code produced from schemas or tools whose source of truth lives elsewhere |

## 18. Traceability Appendix

### 18.1 Requirements to Rules

| req_id | rule_id | rationale |
| --- | --- | --- |
| `REQ-RUSTDOC-001.0` | `RULE-RUST-L1-TYPE-001` | domain values must not collapse into ambiguous primitives |
| `REQ-RUSTDOC-002.0` | `RULE-RUST-L1-OWN-001` | public boundaries should preserve caller flexibility unless ownership is semantically required |
| `REQ-RUSTDOC-003.0` | `RULE-RUST-L2-ERR-001` | reusable Rust code must expose typed failure contracts |
| `REQ-RUSTDOC-004.0` | `RULE-RUST-L2-ERR-003` | caller recovery must not depend on message parsing |
| `REQ-RUSTDOC-005.0` | `RULE-RUST-L3-ASYNC-002` | async correctness requires no blocking and no locks across await |
| `REQ-RUSTDOC-006.0` | `RULE-RUST-L3-ASYNC-003` | long-lived async systems must define bounds, backpressure, and cancellation |
| `REQ-RUSTDOC-007.0` | `RULE-RUST-L3-CONC-001` | task ownership and shutdown semantics must be visible |
| `REQ-RUSTDOC-008.0` | `RULE-RUST-L3-BACKEND-001` | transport data must not become the domain model by accident |
| `REQ-RUSTDOC-009.0` | `RULE-RUST-L3-TAURI-001` | desktop privilege and sidecar boundaries must be explicit and minimal |
| `REQ-RUSTDOC-010.0` | `RULE-RUST-L3-UNSAFE-001` | unsafe surfaces must remain small, justified, and independently verifiable |
| `REQ-RUSTDOC-011.0` | `RULE-RUST-L2-DTOR-001` | fallible or blocking teardown must be explicit rather than hidden in `Drop` |
| `REQ-RUSTDOC-012.0` | `RULE-RUST-L3-ASYNC-004` | shutdown intent and cancellation fan-out must be first-class |
| `REQ-RUSTDOC-013.0` | `RULE-RUST-L2-API-002` | public dependency exposure must be deliberate |
| `REQ-RUSTDOC-014.0` | `RULE-RUST-L3-PERF-001` | performance claims require measurement and named metrics |

### 18.2 Rules to Tests

| rule_id | test_id | test_type | target |
| --- | --- | --- | --- |
| `RULE-RUST-L1-TYPE-001` | `TEST-RUST-TYPE-001` | unit + conversion | invalid and valid domain parsing |
| `RULE-RUST-L1-STATE-001` | `TEST-RUST-COMPILE-001` | compile-fail | illegal state transition misuse |
| `RULE-RUST-L2-ERR-003` | `TEST-RUST-ERR-001` | unit | retryable vs permanent branch behavior |
| `RULE-RUST-L2-ITER-001` | `TEST-RUST-ITER-001` | property | transformation correctness and order |
| `RULE-RUST-L2-WS-001` | `TEST-RUST-WS-001` | integration | workspace-root build and feature matrix |
| `RULE-RUST-L3-ASYNC-002` | `TEST-RUST-ASYNC-001` | stress | no blocking or lock-across-await symptoms |
| `RULE-RUST-L3-ASYNC-003` | `TEST-RUST-ASYNC-002` | integration + timeout + cancellation | bounded queue and shutdown behavior |
| `RULE-RUST-L3-CONC-001` | `TEST-RUST-CONC-001` | teardown + failure propagation | task lifecycle ownership |
| `RULE-RUST-L3-BACKEND-001` | `TEST-RUST-BACKEND-001` | integration | DTO-to-domain conversion and error shaping |
| `RULE-RUST-L3-TAURI-001` | `TEST-RUST-TAURI-001` | command + startup | capability scope and sidecar ownership |
| `RULE-RUST-L3-UNSAFE-001` | `TEST-RUST-UNSAFE-001` | harness + Miri where supported | unsafe wrapper invariants |
| `RULE-RUST-L2-DTOR-001` | `TEST-RUST-DTOR-001` | integration + teardown | explicit close and best-effort drop behavior |
| `RULE-RUST-L3-ASYNC-004` | `TEST-RUST-ASYNC-003` | integration + signal + timeout | graceful shutdown and cancellation fan-out |
| `RULE-RUST-L2-API-002` | `TEST-RUST-API-001` | downstream compile + doctest | public facade and semver leakage control |
| `RULE-RUST-L3-PERF-001` | `TEST-RUST-PERF-001` | benchmark + profile | named performance metric regression guard |

### 18.3 Rules to Gates

| rule_id | gate | pass_condition |
| --- | --- | --- |
| `RULE-RUST-L1-TYPE-001` | `cargo test` | conversion and invariant tests pass |
| `RULE-RUST-L2-ERR-001` | `cargo test` | typed error behavior and top-level aggregation paths pass |
| `RULE-RUST-L2-WS-001` | `cargo build --workspace` | workspace builds from root with intended feature set |
| `RULE-RUST-L3-ASYNC-002` | `cargo test` | async orchestration and timeout tests pass |
| `RULE-RUST-L3-CONC-001` | `cargo test` plus optional `loom` | lifecycle and interleaving checks pass for the chosen risk level |
| `RULE-RUST-L3-BACKEND-001` | `cargo test --all-targets` | integration tests prove boundary conversion and persistence behavior |
| `RULE-RUST-L3-TAURI-001` | framework-specific test and build gate | command, capability, and packaging assumptions hold |
| `RULE-RUST-L3-UNSAFE-001` | `cargo test` plus optional `cargo miri test` | invariants remain valid under supported tooling |
| `RULE-RUST-L2-DTOR-001` | `cargo test` | explicit close and teardown semantics remain correct |
| `RULE-RUST-L2-API-002` | API review plus optional semver tooling | accidental dependency leakage is caught before release |
| `RULE-RUST-L3-ASYNC-004` | `cargo test` plus signal/shutdown scenarios | graceful shutdown remains bounded and owned |
| `RULE-RUST-L3-PERF-001` | benchmark gate | performance claims stay evidence-backed |
| `ALL MAJOR RULES` | `cargo fmt --all -- --check` | formatting is clean |
| `ALL MAJOR RULES` | `cargo clippy --all-targets --all-features -- -D warnings` | lint clean as correctness gate |
