# Rust Agent Mega 02

One file for an AI coding agent that plans, writes, reviews or hardens Rust: libraries, CLIs,
async services, web back ends, parsers, FFI wrappers and Tauri desktop apps. Section 1 applies
to every task and routes to the sections a task needs.

Every rule here is a default with a reason. Where a rule has limits, they are stated as
**Use when** and **Skip when**. A rule followed outside its conditions is a mistake of the same
size as a rule ignored inside them.

## 1. Operating principles and workflow

Before writing code, decide three things:

1. what must be specified: the behaviour, including what happens on failure;
2. what must be designed in types and at boundaries;
3. what must be verified before the result can be trusted.

### Scale the process to the task

| Task | Process that fits |
|---|---|
| Rename, comment, one-line fix covered by an existing test | Read the code and its callers, change it, run the gates |
| Bug fix | Reproduce it with a failing test, fix, run the gates |
| Feature inside one module | A short list of requirements, tests first, implement |
| New public API, a change that crosses a boundary, concurrency, unsafe | The full workflow below |

Process heavier than the task is a cost, not a virtue: a requirements table around a one-line
fix buries the change the reviewer has to check. Process lighter than the task is how a
"small" change to an error type or a lock ships a regression.

### Default workflow

1. **Classify the task.** Name the component (library, CLI, async service, back end, parser or protocol, FFI wrapper, Tauri app, review) and the main risk: ambiguity, design, reliability or review depth. Pick the work mode (section 2).
2. **Write executable requirements** (section 3). "Faster" and "more reliable" are rejected until they carry a threshold and a way to measure it.
3. **Decide the architecture before coding** (section 4): the layers, and a trait seam only where something is really substituted or faked in tests.
4. **Choose the verification mix on purpose** (section 5). Match tests to the risk; unit tests alone are the default only when the risk is pure logic.
5. **Apply the reliability rules** (sections 6 to 10).
6. **Follow the conventions of the repository you are in** (section 12), not the ones you prefer.
7. **Run the gates and the anti-pattern check before handing over** (sections 13 and 16).

### Guardrails

- **Make invalid states unrepresentable where it is cheap.** Parse raw input into a validated type once, at the boundary, and pass the type inward. *Skip when* the invariant depends on runtime state that changes (a balance, a remote resource): check that at the point of use.
- **Prefer an API where misuse is harder than correct use.** If the caller must remember an order of calls, a cleanup or a unit, move it into a type, a guard or a closure.
- **Async, cancellation and concurrency are correctness topics.** Every `.await` is a point where the future may be dropped and where other tasks run. Decide what state is left behind at each one.
- **Errors tell the caller what to do.** A library error is a type the caller can match on; an application error carries the context a human needs. Never erase which failure happened.
- **Unsafe is fenced and argued.** The smallest block, a `// SAFETY:` comment naming the invariant, a safe wrapper, and a Miri run where Miri can run.
- **Performance claims carry a measurement.** No number, no claim.
- **Advanced is not better.** Unsafe, lock-free structures, proc macros, typestate, GATs and HRTBs are answers to specific problems. Use the simplest construct that closes the boundary; a pattern earns its place by removing a class of bug, not by looking expert.
- **Prefer a well-used crate to a hand-rolled one** for parsing arguments, serialisation, HTTP, time, crypto and async primitives. *Skip when* the need is twenty lines and the crate brings a tree of dependencies.
- **Docs and tests change in the same commit as behaviour.**
- **Stay suspicious at the edges.** Ask of every boundary: what happens with malformed input, non-UTF-8 bytes, an empty or huge input, a slow consumer, a cancelled caller, two callers at once, and a newer or older version on the other side?

General Rust practice (typed boundaries, typed library errors, no blocking in async, cancel-safe
`select!`, property tests, doctests, `#[non_exhaustive]`, `tracing`) applies everywhere.
House conventions (a naming scheme, a requirements format, a diagram format) apply only in
repositories that use them. Do not import one repository's house style into another.

Scope: libraries, CLIs, async services, back ends, moderately low-level systems code and FFI
wrappers with contained unsafe. Compiler internals, kernel-grade lock-free code, deeply embedded
`no_std` firmware and advanced proc-macro internals need specialist material beyond this file.

### Working with the compiler and the ecosystem

These are the mistakes an agent makes most often in Rust, and they are cheap to avoid.

- **Fix the first error first.** Later errors are often cascades. Read the whole message, including the `help:` and `note:` lines; the compiler usually names the fix. Run `cargo check` after each small edit, not after three hundred lines.
- **A borrow-checker error is design information.** Before adding `.clone()`, `Rc<RefCell<_>>`, `Arc<Mutex<_>>` or `'static` to make it compile, say who owns the value and how long the borrow needs to live. A clone is a fine answer when the value is small or the path is cold; it is a bad answer when it silently forks state that was meant to be shared.
- **Never guess an API.** Find the version in `Cargo.lock`, then read the docs for that version or the source under `~/.cargo/registry/src`. Widely used crates change shape between major versions (`clap` 3 to 4, `axum` 0.6 to 0.7, `hyper` 0.14 to 1, `rand` 0.8 to 0.9), and code remembered from one version fails on another.
- **Check the edition and the MSRV** (`edition` and `rust-version` in `Cargo.toml`) before using a newer feature such as `let ... else`, `async fn` in traits or let-chains.
- **Never turn a gate green by weakening it.** No deleted or `#[ignore]`d test, no `#[allow(...)]`, no loosened assertion and no `unwrap_or_default()` over a real error unless you say so in the handover and give the reason.
- **Match the codebase.** Use its error crate, runtime, logging, naming and module layout. A second way of doing the same thing is a cost every later reader pays.
- **Keep the diff to the task.** No drive-by reformatting, renames or dependency upgrades. Report what you noticed; do not fix it uninvited.
- **Add a dependency deliberately.** Check that std or an existing dependency does not already do it, look at maintenance and licence, enable only the features needed, and say in the handover that you added it.

### Working habits on a long task

- **Orient before analysing.** In an unfamiliar codebase: size and layout, then the entry point, then callers and callees. Deep reading of one function comes last.
- **Read before you write.** Read the function you change, its callers and its tests. The cheapest correct change may be a repaired test or a doc fix.
- **Work in rounds.** Explore, apply the constraints, refine, verify. The first draft is a starting point.
- **Debug in a loop with a stop condition.** Reduce to the smallest reproduction, list hypotheses in order of likelihood, run one probe per hypothesis and note what it ruled out. Stop when a probe confirms a cause and a regression test fails for that cause. A plausible story is not a diagnosis.
- **A red test must be red for the right reason.** Confirm it fails on the assertion, not on a compile error or a setup mistake.
- **Checkpoint long work in a file.** After each milestone write the decisions and the state, and read it back before continuing. Context from early in a long task is otherwise lost.
- **Keep a list of past bugs** as wrong and right pairs with the root cause, and reread it at the start of work on that project. Typical entries: `std::thread::sleep` in an async function (use `tokio::time::sleep(..).await`); an `Rc` moved into `tokio::spawn` (use `Arc`).
- **Review your own answer.** List the assumptions that may not hold, the edge cases you did not cover and the likely bottleneck. For a subtle block, be able to say what breaks if each line is removed.
- **Check the repository before touching history.** Before a branch, merge, rebase or push: uncommitted changes, untracked files, the current branch, and the recovery path if it goes wrong.
- **When instructions disagree, name the one that governs.** Do not average two conflicting documents. Say which is authoritative and why, follow it, and flag the other as stale.
- **A recommended pattern states its limits:** when to use it, when to adapt it, when to avoid it, and what it costs if the choice is wrong.
- **Finished means end to end.** It works in the release build, the whole suite passes (not only the new tests), integration is exercised, docs and scripts are updated, and no `todo!()`, stub or "will be implemented" remains.
- **Report plainly.** Give the measured result and where it came from ("p99 fell from 5 ms to 500 µs on the `lookup` benchmark"). Say what you did not check. No superlatives.

### Decision ladder

Work down the ladder; each choice constrains the next.

1. **Kind of code:** library, binary, async service, FFI wrapper, proc macro, low-level component.
2. **Ownership surface:** borrow, own, share (`Rc`/`Arc`) or encode the state in the type.
3. **Error surface:** typed library error, application-level aggregation, or rich diagnostics for a binary.
4. **Concurrency surface:** sync, async, channels, cancellation, who owns each task.
5. **API stability surface:** `#[non_exhaustive]`, additive features, sealed traits. *Skip for* a binary or a private crate with no outside callers.
6. **Verification mix:** unit, doctest, compile-fail, property, fuzz, `loom`, Miri.
7. **Unsafe, if it remains necessary:** smallest block, written invariant, Miri or an equivalent check. The absence of crashes is not evidence of soundness.

The test for a pattern: it can be removed only by weakening a named boundary. A newtype and a
typed error that close a boundary in twenty lines beat a typestate protocol around a two-state
flag. Start with the patterns that stop the most bugs (validated newtypes, no blocking across
`.await`, typed errors) before the advanced ones.

Not first bets, because they are niche or easy to get wrong: a custom global allocator;
`ManuallyDrop` as an optimisation; lock-free structures without a verification plan; pin
projection by hand (use `pin-project-lite`); proc macros where `macro_rules!` or a generic
function would do; anything that depends on specialization.

**Size a change by the surfaces it crosses, not by its line count.** A large mechanical rename
crosses none and is cheap to review. A small diff that changes the API, the error type and the
concurrency model is three changes: split it, in ladder order (the newtype first, then the
error redesign it enables; never convert an API to async and retype its errors in one change).

**Record the choice where it is not obvious.** For a change to a public API, an error surface,
concurrency or unsafe, leave one line saying what was chosen and what would change it: "`dyn
Trait` here because this is a plugin seam; revisit if it shows up in a profile." A later reader
can then tell a decision from an accident. Replacing a public error type is a SemVer break even
when every call site still compiles for you.

### Priorities by task type

| Task | Put first |
|---|---|
| Library or public API | Borrowed inputs and explicit conversions; validated newtypes; typed errors; a surface that can grow without a SemVer break; doctests, and compile-fail tests for misuse the types are meant to stop |
| CLI or binary | Written contracts for user-visible behaviour (output, exit codes, stdin and stdout rules); diagnostics a user can act on; integration tests that run the real binary |
| Async service or back end | Typed parsing at the edge; no blocking and no lock guard across `.await`; bounded queues and concurrency; a timeout on every outbound call; cancellation and shutdown that are designed, not accidental |
| Parser or protocol | No panic on any input; checked slicing and arithmetic; byte-safe diagnostics; property tests, fuzzing, round-trip checks; a limit on input size and nesting depth |
| FFI or unsafe boundary | The smallest unsafe surface; written invariants; layout, nullability, ownership and unwinding rules at the boundary; Miri or sanitizers |
| Review or hardening | Misuse resistance; whether errors stay distinguishable; who owns each task and how it stops; the anti-pattern list; whether the gates really ran |

### Default reliability stack

When nothing else tells you what matters most, work down this list:

1. Model invariants with newtypes, enums and explicit conversions.
2. Keep library errors typed and application errors contextual.
3. Make async code non-blocking, bounded and cancel-safe.
4. Remove panics from parsing, slicing and arithmetic on outside input.
5. Turn examples, invariants and misuse cases into tests.
6. Keep unsafe small, argued and verified.
7. Design logging, metrics and secret handling in; do not bolt them on.

Most production Rust uses a small core: ownership and borrowing, RAII, `Result` and `Option`
with `?`, enums with `match`, newtypes, iterators, `Arc` for sharing, derive macros and a few
established crates. Reach past that core only when a named problem needs it.

### Concrete first, abstract on the second use

- Write the concrete type and function first. Introduce a trait, a generic parameter or a builder when a second real implementation or caller exists, or when a test needs a fake at an I/O boundary.
- Use libraries with known behaviour; benchmark a choice only when the operation is on a path with a stated budget.
- Where a timing or memory limit is a requirement, write its test before the implementation (section 5 shows how to keep such a test honest).
- One lock guards one invariant. A design that needs two locks held together needs a documented lock order, or a redesign that puts both pieces of state under one lock.

*Use this strictly when* limits are hard and known: constrained memory or CPU, a latency budget,
well-defined concurrent access. *Relax it for* a prototype or exploration, where the aim is to
learn the shape of the problem; say so in the handover so nobody mistakes it for production code.

**Anti-patterns.** A trait with one implementation and no test fake. A generic parameter that
is always the same type. A `Config` option nobody asked for. A plugin system for two fixed cases
(use an enum). Each adds a seam that must be kept working and proves nothing yet.

### Rule strength, waivers and severity

- **Strength.** MUST and MUST NOT hold unless a waiver is written down. SHOULD is a default that context can override, with the reason stated. MAY is optional.
- **A waiver records** the exact rule, the reason, the narrowest scope, the compensating control for the risk the rule guarded against, and when it is revisited (the next refactor or release of that code). Checking added under a waiver is stricter than the baseline for that area.
- **Not valid reasons:** deadline alone; "MVP" with no compensating control; "we know it is safe"; "we will test later"; "the compiler is annoying"; "the framework makes it awkward"; not knowing the Rust feature that would solve it.
- **A waiver never makes a hidden thing permanent.** Hidden cleanup, an unowned background task or an unplanned dependency stays temporary only if a replacement plan is written beside it.
- **Review severity.**
  - P0: likely wrong behaviour, data corruption, a security hole, or a claim of completion that is not true.
  - P1: a serious design or reliability weakness with high regression risk.
  - P2: a notable weakness in maintainability, verification or a boundary.
  - P3: polish and clarity.
- **Confidence in a rule.** High when a language guarantee or std behaviour backs it; medium for strong ecosystem precedent that depends on context; low for a heuristic or a house convention. Argue hardest for the high ones and yield first on the low ones.

### First principles not already stated

- **Ownership is a design tool.** Who owns a value answers who may change it, who frees it and how long it lives. Decide that before choosing between `&T`, `T`, `Arc<T>` and a channel.
- **A simple public surface beats internal sophistication.** Complexity belongs behind the API, and only where it pays.
- **Destructor timing is part of the program's meaning.** When a guard, a file, a transaction or a temporary is dropped decides when a lock is released or a write is flushed.

**Where to enforce an invariant, in order of preference:**

1. In a type, when that is cheap: the invalid value cannot be built.
2. Once, at the narrowest boundary that sees the raw input. Do not re-validate downstream; pass the validated type.
3. With `debug_assert!` for expensive internal consistency checks. This never replaces boundary validation, because release builds skip it.
4. An `_unchecked` fast path exists only beside the checked function that defines the contract, is `unsafe` if violating it breaks memory safety, and is added only after a profile shows the check matters.

### Destructors, guards and temporaries

- `Drop` cannot fail, must not block and should have almost no side effects. If teardown can fail, block or needs `.await`, expose `close`, `flush` or `shutdown` returning `Result`, and let `Drop` release only local state as a fallback.
- If correctness needs teardown to happen before later work, show it in control flow (an explicit `drop(guard)` or an inner block) and test it.
- `let _ = mutex.lock();` drops the guard at once; `let _guard = mutex.lock();` holds it to the end of the scope. Choose on purpose.
- A temporary created in a `match` or `if let` scrutinee lives to the end of the whole statement:

```rust
// Bad: the guard lives for the whole match, so the second lock deadlocks.
match cache.lock().unwrap().get(&key).cloned() {
    Some(v) => v,
    None => compute_and_insert(&cache, key), // locks the cache again
}

// Good: the guard is dropped at the end of the let statement.
let hit = cache.lock().unwrap().get(&key).cloned();
match hit {
    Some(v) => v,
    None => compute_and_insert(&cache, key),
}
```

- A task that can outlive its caller documents how it is cancelled and how it shuts down.

### What the compiler does not prove

- It proves memory and type properties. It proves nothing about domain correctness, performance, cancellation behaviour or SemVer compatibility.
- Code that compiles with clones everywhere has not shown the clones are right; it may have forked state that was meant to be shared.
- No data race does not mean no logical race. Check-then-act across two lock acquisitions, starvation, dropped work and stale reads all compile.
- Unsafe code must stay sound even when the safe code around it is logically wrong. One unsafe block, one proof obligation that can be explained on the spot. Delete an unsafe optimisation that has no measured gain.

### Working terms

- **Boundary:** where unchecked data, control or side effects enter or leave a component.
- **Soundness:** no safe caller can cause undefined behaviour.
- **Exception safety:** minimal means memory-safe if a panic unwinds at any point; maximal means the data is also still logically consistent.
- **Cancellation point:** a place where a future can be dropped, in practice every `.await`. **Cancel-safe:** dropping it there loses no data and breaks no invariant.
- **Backpressure:** the stated policy for what a producer does when the consumer is slower (wait, drop, reject).
- **Opaque error:** an error meant to be propagated and displayed, not matched on.
- **Generated surface:** code produced from a schema or tool; its source of truth lives elsewhere.

### What "idiomatic" means

Idiomatic Rust is the smallest design that makes ownership, invalid states, failure, task
lifetime and dependency direction visible. It is not the most types, the most generics, the
fewest clones or the deepest abstraction.

- **Decide per API, not by slogan.** A good default: borrow the input being parsed, return an owned domain value. Stay synchronous when nothing waits on I/O. Keep a concrete type until callers need an abstraction. Cloning a small value into a task is idiomatic when it makes ownership simple.
- **The shape of an idiom without its purpose is noise:** a newtype that validates nothing and wraps a value never confused with another; `Arc` by habit; `impl AsRef<str>` on a function only ever called with `&str`; a benchmark with no stated limit.
- **Costs that spread to callers:** a lifetime parameter in a public type; a returned reference tied to a borrowed input; blanket `From` impls that hide which conversion ran; an error enum that grows a variant per dependency; `Arc` leaking into every signature; a mock that drifts from the real implementation.
- **Where contracts hide:** the SemVer effect of a public signature; an allocation inside an ergonomic conversion; a lock guard held inside a helper; a cancellation after a partial effect; whether a trait is object-safe; feature combinations; doctests that compile under a different `cfg`.
- **Existing code and general idiom both have limits.** Existing code is not right because it exists, and a test can lock in an accidental API. A general idiom still does not override a public contract, a feature set or the MSRV without a migration.
- **Evidence is local.** An `axum` or `tokio` example supports code on that framework at that version. It says nothing about how a CLI or a parser library should look.
- **Apply any rule, from this file included, only when** the failure it prevents can happen in this task and a check can show the rule held. Testability does not mean a trait on everything. Pick the smallest rule that covers the risk.

### Core rules

- **Lifetimes state real relationships** between inputs and outputs. If the lifetime reasoning is harder than the logic, change the shape of the API (return an owned value, take a closure, split the struct); do not add more annotations.
- **Constructors keep invariants.** The checked constructor is the way in; fields stay private. Validation returns a typed error immediately, never a half-valid value. *Skip for* plain data with no invariant: a struct of public fields is honest there, and getters add nothing.
- **Opaque or enumerated errors.** If callers branch on the failure, expose an enum. If they only propagate and print it, an opaque error type with good context is a smaller commitment than a large public enum. Either way, do not leak a dependency's error type through a stable API unless you mean to commit to that dependency.
- **Classify errors by what the caller does next.** Where retrying changes control flow (network, storage, subprocess, queue), the error says transient or permanent through a method or a variant. Never match on error strings. Test that transient failures are retried and permanent ones are not.
- **Shared-state tools differ.** `Rc`/`Arc` share ownership; `Cell`/`RefCell` give single-threaded interior mutability; `Mutex`/`RwLock` serialise access; atomics hold single values; channels move ownership. Narrow the shared part to the smallest mutable piece. `Arc<Mutex<AppState>>` around unrelated concerns is one global lock under another name.
- **A loop is fine.** Use a `for` loop when it is clearer than a combinator chain, especially with early exits, several accumulators or `?` inside.
- **Conversion names follow cost.** `as_` is a free borrowed view, `to_` may allocate or copy, `into_` consumes.
- **Do not edit generated code.** Change the schema or the generator, and put behaviour in a hand-written wrapper next to it.
- **Transport shapes stay at the transport.** Request and row types carry `Option` and strings; domain types carry invariants. Convert once, at the edge, through `TryFrom` or one constructor, so no two handlers validate the same field differently. Shape validation (it parsed as JSON) is not invariant validation (the range is legal).
- **One owner per transaction.** Where a durable write is combined with a remote side effect, state what happens when the second fails (outbox, compensation or accepted inconsistency), and make anything that can be replayed idempotent.
- **An outbound client has four things:** typed failures, a timeout, a retry policy with a limit, and a correlation ID in its logs.
- **Name the target when optimising.** Latency, memory, binary size and compile time are different goals. Start from a profile; an algorithmic bound can matter more than a micro-optimisation when the worst case is what hurts.

### Rule cards

- **Newtypes at trust boundaries (must).** IDs, units, tokens, credentials, offsets and validated values get their own types: `struct UserId(NonZeroU64);`, `impl TryFrom<&str> for EmailAddress`. If two values must not be swapped, their types must not be swappable. *Skip for* local glue inside one function. *Verify* with parse and round-trip tests.
- **Trait seams at side-effect boundaries.** Put a trait where side effects leave the process: storage, outbound HTTP, queues, the clock, random IDs, child processes. The service depends on `UserStore`; the adapter owns the pool. *Skip for* pure helpers and leaf logic, which are tested directly. *Verify* with fakes in unit tests and the real adapter in an integration test, because the fake can drift.
- **Typestate for protocols that must complete (may).** Handshakes, builders with mandatory fields, staged activation: `Connection<Unauthenticated>` becomes `Connection<Authenticated>`. *Skip for* CRUD and soft workflows, for more than about four states, and when states must be stored in one collection or chosen at runtime; an enum fits those. *Verify* with compile-fail tests for the misuse.
- **Typed library errors (must).** A library does not return `anyhow::Error` or `Box<dyn Error>` from its public API. Add context where the operation is known: `read_to_string(path).with_context(|| format!("read config {}", path.display()))?`. A bare `NotFound` with no path is not an error message.
- **Collections by access pattern.** `Vec` for ordered scans and small sets, `HashMap` for keyed lookup, `BTreeMap` for ordered or range iteration and for deterministic output, `VecDeque` for a queue. *Anti-pattern:* `HashMap` everywhere, then sorting on every read, or iterating a `HashMap` into output that tests compare byte for byte.
- **Dependency types in a public API (must) are a commitment.** Either mean it and document it, or wrap the type and convert inside.
- **Owned data across `.await` and into tasks (must).** What is held across an await or moved into `spawn` is owned or `Arc`-shared. Do not hold borrowed request fragments across awaits. *Verify* with a cancellation test for partial progress.
- **No blocking and no lock guard across `.await` (must).** No `std::thread::sleep`, synchronous file or network I/O, or heavy CPU loop on the async runtime; use the async equivalent or `spawn_blocking`. A `std::sync::MutexGuard` is released before any await. One passing run shows nothing about contention; use a stress test with a timeout, and `loom` when the interleaving is the risk.
- **Bounded concurrency (must).** Every worker pool, pipeline, retry loop and queue states its bound, what happens when it is full, and how it is cancelled. If work can pile up, there is already a queue; bound it.
- **Owned tasks and one shutdown path (must).** A `JoinSet` or supervisor owns each spawned task; if nobody owns a task, nobody sees its failure. One trigger fans out to every task (a `CancellationToken` or a watch channel), followed by a join with a deadline. A `main` that returns and hopes tasks vanish loses work. Detached tasks are acceptable only for work whose loss is bounded and harmless. *Verify* shutdown during work and the time teardown takes.
- **Structured observability.** At handlers, jobs, outbound calls and consumers, open a `tracing` span with the request ID, resource ID, attempt number and outcome as fields, not as formatted text. *Skip* tight inner loops when the enclosing span already gives the context.
- **Unsafe islands (must).** Unsafe lives in the smallest private module that can offer a safe interface, with a `// SAFETY:` comment on each block. Never use unsafe to get round the borrow checker.

### Evidence hygiene

- **Check that source is really source.** Before concluding anything from a repository, list its manifests and source files. An empty `src`, an empty manifest or Git LFS pointer stubs (files starting `version https://git-lfs.github.com/spec/v1`) are not code. A file name or a keyword hit is a lead, not a finding.
- **A stale or broken index is not evidence.** Use a code index for navigation and confirm each claim in the source files.

## 2. Work modes and output contract

Pick the mode before planning. A task usually needs two.

| Mode | Use when | Produces |
|---|---|---|
| Spec | The request is vague, acceptance criteria are missing, or success is not yet measurable | Requirement contracts, acceptance criteria, a requirement-to-test table |
| Delivery | The work needs structure: layers, seams, an order of steps | The design, the test-first sequence, the slices |
| Reliability | The risk is correctness under stress or change: public API, errors, async and cancellation, concurrency, unsafe, FFI, release | Failure behaviour made explicit, and the checks that prove it |
| Review | The task is a code or design review or a hardening pass | Findings by severity, each with evidence and a fix |

Default pairs:

- vague feature request: Spec + Delivery
- public API or reusable crate: Spec + Reliability
- async or concurrent system: Delivery + Reliability
- parser, decoder or protocol: Spec + Reliability
- review or hardening: Review + Reliability

When modes pull in different directions, Spec decides what must be proven, the design decides
where invariants and dependencies live, Reliability decides which failures must be explicit,
Delivery decides the order, and Review decides what to challenge hardest. Between two valid
options, take the one that surprises callers least.

### Output contract

For a work packet (a feature, a design, a hardening pass), report in this order:

1. Work mode
2. Executable requirements
3. Design (layers and trait seams)
4. Verification matrix
5. Implementation plan
6. Quality gate results
7. Open questions

with every requirement traced to a test:

| req_id | test_id | test_type | assertion | metric |
|---|---|---|---|---|

- **Keep the order, and say so when a section owes nothing** ("no performance requirement was stated, so no thresholds"). A fixed order lets a reviewer see what is missing before reading what is there.
- **Gate results are what you ran, with the outcome.** "Should pass" is not a result. A gate you could not run is listed as not run, with the reason.
- **Open questions is the section most often skipped and the most useful.** An empty list on an under-specified task reads as overconfidence. List what you assumed.
- **Review output leads with findings,** most severe first, not with reassurance.
- **Every completion claim rests on a check run after the last change.** Evidence outranks confidence, an earlier run and plausibility.

*Skip the seven sections for a small change.* A bug fix or a contained edit reports three
things: what changed and why, what was run and its result, and what is uncertain or left open.
Wrapping a three-line fix in seven headings hides the fix.

## 3. Executable specifications

A requirement is executable when a test can fail for it. The form:

- An identifier, `REQ-<AREA>-<NNN>.<REV>`, for example `REQ-RUST-014.1`. If the repository already has a scheme, use that one. Prefix by component once two work packets share a program, bump the revision when the meaning changes, and never reuse a retired number.
- Behaviour written as `WHEN ... THEN ... SHALL`.
- A threshold with a unit, or an effect a test can observe. Without one it is a wish; send it back.

```markdown
### REQ-RUST-001.0: <short title>

**WHEN** <trigger or input condition>
**THEN** the system SHALL <primary behaviour>
**AND** SHALL <second measurable behaviour>
**SHALL** <edge-case or default behaviour>
```

| Wish | Requirement |
|---|---|
| "Handle bad input gracefully." | WHEN the body is not valid UTF-8 THEN the parser SHALL return `ParseError::InvalidUtf8 { offset }` AND SHALL NOT panic. |
| "Make lookups fast." | WHEN the index holds 10,000 entries THEN `lookup` SHALL complete in under 1 ms at p99 on the reference benchmark. |
| "Retry on failure." | WHEN the upstream returns 503 THEN the client SHALL retry at most 3 times with exponential backoff from 100 ms, AND SHALL return `UpstreamUnavailable` after the third failure. |
| "Be thread-safe." | WHEN 64 tasks increment the counter 1,000 times each THEN the final value SHALL be 64,000. |

Rules:

- **One `SHALL`, one test.** Split a clause that stacks two behaviours. Keep functional and non-functional requirements apart when they blur.
- **Units everywhere:** `us`, `ms`, `MB`, `ops/s`, a retry count, a concurrency limit.
- **Failure behaviour is specified, not left to the implementation.** For each input boundary write the rejected case too: what is returned, and what state is left behind.
- **Retry is a requirement,** not a loop added in review: the count, the backoff shape and the concurrency ceiling, each linked to a test. State what it assumes about retries in the layers below, since three retries on top of a client that retries three times is nine calls.
- **Silence on performance is a choice.** A regression on a path with no threshold violates nothing. Ask whether the path really has no budget or whether nobody wrote it down, and add the clause if it has one.
- **Requirements describe behaviour, not implementation.** "SHALL use a `HashMap`" is a design decision; "SHALL return the entry in constant expected time" is a requirement.

*Use when* behaviour is new or changing and someone other than you must agree it is right.
*Skip for* a pure refactor (the existing tests are the specification; state that behaviour is
unchanged and show the suite passing before and after) and for exploratory spikes.

**Anti-patterns.** A requirement that restates the code ("SHALL call `validate()`"). An
unmeasurable adjective ("robust", "scalable", "user-friendly"). One requirement with five
`AND` clauses and one test. A requirements list written after the code to match what it does.
A threshold copied from another project with no benchmark behind it.

### The contract on the function

An agent cannot ask the author what a function is supposed to do, so the contract sits on the
function: what it needs, what it guarantees, what it changes and how it fails. Use the rustdoc
headings tools already understand (`# Errors`, `# Panics`, `# Safety`), and move every
precondition you can into a parameter type.

```rust
/// Stores a message, or returns the stored one if `client_message_id` was seen before.
///
/// On success: inserts one row, updates the room's `last_message_at` and broadcasts to
/// the room's subscribers. A repeated `client_message_id` causes none of these.
///
/// # Errors
/// - [`MessageError::Forbidden`] if the user has no access to the room.
/// - [`MessageError::Database`] if the write fails; nothing is broadcast.
pub async fn create_message(
    &self,
    content: MessageContent, // 1..=10_000 chars, checked when the value was built
    room: RoomId,
    user: UserId,
    client_message_id: Uuid,
) -> Result<Message, MessageError>;
```

- **A precondition a type can carry is not written in prose.** "Content must be 1 to 10,000 characters" became `MessageContent`, and the `InvalidContent` error left this function for the constructor.
- **Document side effects and their order on failure.** "Nothing is broadcast if the write fails" is the line a caller needs and the signature cannot say.
- **Every documented error and effect has a test.** A contract line with no test drifts.
- **Do not restate the signature.** "Takes a room ID and returns a message" adds nothing.
- `# Panics` lists every way the function can panic; the best version of that section is absent because there is none. `# Safety` is mandatory on every `unsafe fn`.

*Use when* the function is public, has side effects, or has failure behaviour a caller must
plan for. *Skip for* private helpers whose name and types say everything.

### Levels of specification

| Level | Holds |
|---|---|
| Constraints | System-wide invariants and rules that every part obeys |
| Architecture | Data models, the error hierarchy, interface contracts |
| Module | Function-level contracts, built test-first |
| User journey | End-to-end checks of what a user or caller sees |

A requirement belongs at the widest level where it is true. "No handler blocks the runtime" is
a constraint, not a note on one function.

**Acceptance criteria name the command, the input and the bound:**

```markdown
1. WHEN I run `tool ingest <file>` on a dump with `FILE:` markers THEN the system SHALL
   extract every public function signature from each marked file.
2. WHEN the input is the 2.1 MB reference dump THEN ingestion SHALL finish in under 5 s.
```

**Write the scenarios beside the interface while designing,** as given, when, then. Each one
becomes a test name, so the list is the test plan:

```text
Scenario: duplicate client id
  Given a stored message with client_message_id X
  When  create_message is called again with X
  Then  it returns the stored message and inserts nothing
```

**Tie tests and docs to requirements.** A test name or a comment carries the requirement ID, so
a failing test names the broken requirement and a search for the ID finds its proof. Doc
examples are doctests that run, not illustrations:

```rust
#[test]
fn blast_radius_stays_under_budget_req_perf_003() { /* asserts REQ-PERF-003.0 */ }

/// ```
/// # use mycrate::{Graph, NodeId};
/// # fn main() -> Result<(), mycrate::Error> {
/// let graph = Graph::from_edges(&[(1, 2), (2, 3)])?;
/// assert_eq!(graph.blast_radius(NodeId(1), 3)?.len(), 2);
/// # Ok(())
/// # }
/// ```
pub fn blast_radius(&self, start: NodeId, depth: u32) -> Result<Vec<NodeId>, Error> { /* ... */ }
```

Lines starting with `#` inside a doctest compile but are hidden in the rendered docs; they are
how an example uses `?` without showing boilerplate. An example that cannot run (it needs a
network or a database) is marked `no_run` so it still compiles; `ignore` is a last resort
because an ignored example rots.

### Vague to executable

| Vague | Executable |
|---|---|
| "Make it faster." | "Reduce p99 latency from 5 ms to under 1 ms for 10,000 entities on the reference benchmark." |
| "Improve reliability." | "Return a typed validation error for malformed input; no panic and no task left running." |
| "Handle async correctly." | "Cancellation propagates to every spawned task within 1 s; no blocking call and no lock guard is held across `.await`." |
| "Make the API cleaner." | "Take borrowed inputs, expose no dependency types, and reject invalid values at construction." |

- **Start at the first thing that is missing.** A vague request starts with the rewrite. A request with testable requirements starts at the design. Test skeletons come after requirements and design exist; a trivial fix goes straight to its test. Starting at the skeletons because they look most like code yields tests for requirements nobody stated.
- **A filled-in template can be hollow.** A `WHEN` that says "sometimes" or a metric that says "fast" has the shape and defeats the purpose. Review what is in the blanks, not that the headings are present.
- **If the rewrite needs a number you do not have, ask or measure.** Do not invent a threshold; record the current measured value as the baseline and state that the target is still to be agreed.

### Work packet template

Use this when a request is not ready for coding:

```markdown
## Work mode
<the modes chosen, and why>

## Executable requirements
### REQ-RUST-001.0: <title>
**WHEN** ... **THEN** the system SHALL ... **AND** SHALL ...

## Design
- L1 core:
- L2 orchestration:
- L3 adapters:
- Trait seams:

## Verification matrix
| req_id | test_id | test_type | assertion | metric |
|---|---|---|---|---|

## Implementation plan
1. STUB  2. RED  3. GREEN  4. REFACTOR  5. VERIFY

## Quality gate results
- fmt:      <command, result>
- clippy:   <command, result>
- tests:    <command, result>
- build:    <command, result>

## Open questions
```

- **A packet is one document.** Every requirement ID appears again in the matrix and every matrix row in the plan; searching for the IDs checks it. A test row with no requirement behind it means the requirement gets written first.
- **Gate lines hold real results.** Passing tests do not imply that `cargo build --all-targets --all-features` passes, so the build line is reported on its own.
- **Template text left in place marks a hollow packet:** example modes, example IDs, a matrix row that cites a requirement the packet never defined.

## 4. Architecture and boundaries

Decide the layers before writing code. Dependencies point inward only.

| Layer | Holds | May depend on |
|---|---|---|
| L1 Core | Domain types, invariants, state rules, pure functions, the traits the core needs from outside | `core`/`std` data types and small pure crates |
| L2 Orchestration | Use cases: sequencing, error composition, collections, concurrency policy | L1, the standard library |
| L3 Adapters | Runtime, database, HTTP, serialisation formats, tracing setup, FFI | L1 and L2, external crates |

- **L1 never imports L3.** No `tokio`, `sqlx`, `reqwest` or web-framework type in a domain signature. The core defines the trait; the adapter implements it.
- **Push validated types down.** If the core receives a `UserId`, nothing below the edge handles a raw string.
- **Wiring happens once,** in `main` or one composition module: build the adapters, hand them to the services, start the runtime.
- **Layers are modules first.** Split into crates when compile time, reuse or an enforced dependency rule justifies it. Three crates for five hundred lines is ceremony.

*Use when* the program has I/O and logic worth testing apart from it. *Skip for* a small script
or a thin CLI: one module with a pure `run(input) -> Result<Output>` function and a `main`
that does the I/O gives the same testability.

**Pragmatic exception.** `#[derive(Serialize, Deserialize)]` on a domain type is acceptable
when the wire shape and the domain shape are the same thing and no outside party depends on
the format. Once they differ, or the format is a public contract, use a separate transport
type and convert at the edge.

**Anti-patterns.** A handler that builds SQL. A domain function that takes a connection pool.
A `utils` or `common` module everything depends on and nothing owns. A core that reads
environment variables or the clock directly. Layers that exist as folders while every file
imports every other.

### Trait seams

Define the trait before the adapter when I/O should be kept out of domain logic, when tests
need a fake, or when behaviour should be settled before storage or transport is chosen.

```rust
pub trait EntityStore {
    fn load(&self, id: EntityId) -> Result<Option<StoredEntity>, StoreError>;
}

pub struct EntityService<S> {
    store: S,
}

impl<S: EntityStore> EntityService<S> {
    pub fn describe(&self, id: EntityId) -> Result<String, ServiceError> {
        let entity = self.store.load(id)?.ok_or(ServiceError::NotFound(id))?;
        Ok(entity.summary())
    }
}
```

- **The trait is owned by its consumer and sized to it.** It lists the few operations the service needs, in domain terms (`load`, `save_order`), not the adapter's whole API (`execute_sql`).
- **The error type belongs to the trait,** not to the adapter. `StoreError` does not expose `sqlx::Error`.
- **Generic or `dyn`.** A generic parameter (`S: EntityStore`) costs nothing at run time and suits one implementation per binary. `Arc<dyn EntityStore>` suits a choice made at run time, heterogeneous collections, and stopping a type parameter spreading through every signature. Default to generics inside a library and `dyn` at the application's wiring layer.
- **Async methods.** `async fn` in a trait works with generics but makes the trait unusable as `dyn`, and promises nothing about `Send`. For `dyn` use, return a boxed future or use the `async-trait` crate; for a public trait, write the return type as `impl Future<Output = T> + Send` so spawned callers compile.
- **A fake is a real implementation,** usually an in-memory map, kept in the test support code and run through the same contract tests as the real adapter. A fake that only ever returns `Ok` tests nothing about failure.

*Skip the trait when* there is one implementation, no test needs a fake, and the dependency is
pure (a parser, a formatter, a calculation). Call the function.

**Algorithms over the smallest capability traits.** When a library has several representations
of one concept (graph storage, matrix layouts, byte sources), write each algorithm against the
smallest set of capability traits it needs, and implement those per representation:

```rust
pub fn dijkstra<G, F, K>(graph: G, start: G::NodeId, edge_cost: F) -> HashMap<G::NodeId, K>
where
    G: IntoEdges + Visitable,
    G::NodeId: Eq + Hash,
    F: FnMut(G::EdgeRef) -> K,
    K: Measure + Copy,
```

- Start from the weakest bounds; add a stronger trait only when an operation needs it.
- Each representation passes one shared conformance suite for every capability it claims.
- *Skip when* there is one representation, or the algorithm relies on layout, mutation or complexity guarantees the traits cannot express. The bounds above are hard to read and hard to debug; they must buy real reuse.

**A closed set of variants: one trait, one factory.** When each member of a family (languages,
file formats, back ends) supplies the same handful of operations, give the family one trait
with defaults for optional parts, and build members in one place:

```rust
pub trait Format: Send + Sync {
    fn name(&self) -> &'static str;
    fn extensions(&self) -> &'static [&'static str];
    fn parse(&self, text: &str) -> Result<Document, ParseError>;
    fn imports(&self, _doc: &Document) -> Vec<String> {
        Vec::new() // optional capability: the default says "none"
    }
}

pub fn format_named(name: &str) -> Result<Box<dyn Format>, UnknownFormat> {
    match name {
        "json" => Ok(Box::new(Json)),
        "toml" => Ok(Box::new(Toml)),
        other => Err(UnknownFormat { name: other.to_owned(), supported: &["json", "toml"] }),
    }
}
```

- The pipeline is written once against `dyn Format`; adding a member touches its own file and the factory.
- An unknown name is an error that lists what is supported, not a silent `None`.
- If the members share no behaviour and differ only in data, a table of structs is simpler. If the set is fixed and small and the logic is a `match`, an enum keeps exhaustiveness checking, which a trait object gives up.
- **Plugins loaded at run time** come from an explicit registry or manifest, one coordinator calls their hooks in a stated order, and a plugin that fails to load is reported at startup, never skipped silently.

- **A default method can lie.** An empty default silently drops data for every member that has not implemented the richer method, and nothing fails. When "not supported" and "supported, found nothing" must be told apart, return `Option` from the default or split the capability into its own trait. Every non-default method callers rely on gets a fixture per member.

### Dependencies, resources and real inputs

**Depend on the trait, not the concrete adapter.**

```rust
// Bad: the component can only ever be built with a real database and a real watcher.
pub struct Indexer {
    database: SqliteConnection,
    watcher: NotifyWatcher,
}

// Good: the dependencies are parameters.
pub struct Indexer<D, W> {
    database: D,
    watcher: W,
}

impl<D: Database, W: FileWatcher> Indexer<D, W> {
    pub fn new(database: D, watcher: W) -> Self {
        Self { database, watcher }
    }
}

pub type ProductionIndexer = Indexer<SqliteDatabase, NotifyFileWatcher>;
```

- **Bounds go on the `impl`, not on the struct definition.** A bound on the struct must be repeated on every `impl` and every function that mentions the type. Put it on the struct only when a field's type or the `Drop` impl needs it.
- **Ask for `Send + Sync` where it is needed** (the function that spawns), not on every type by reflex.
- **Wrap in `Arc` only what is shared.** A component with a single owner holds its dependencies by value.
- **Two or three type parameters is the practical ceiling.** Beyond that, signatures and error messages become unreadable; switch to `Arc<dyn Trait>` fields, or group the dependencies behind one context trait.

**Resources are released by RAII, with an explicit path for teardown that can fail.**

```rust
pub struct Session {
    connection: Option<Connection>,
}

impl Session {
    /// Flushes and closes. Call this on the normal path; it reports failure.
    pub fn close(mut self) -> Result<(), CloseError> {
        match self.connection.take() {
            Some(connection) => connection.close(),
            None => Ok(()),
        }
    }
}

impl Drop for Session {
    fn drop(&mut self) {
        // Fallback for early returns and panics: best effort, never panics.
        if let Some(connection) = self.connection.take() {
            if let Err(error) = connection.close() {
                tracing::warn!(%error, "session dropped without close(); close failed");
            }
        }
    }
}
```

- `Option::take` lets `close(self)` and `Drop` share the resource without closing it twice.
- **Drop order is part of the design.** Struct fields drop in declaration order; local variables drop in reverse order of declaration. If the pool must outlive the workers that use it, declare the workers first, or shut down explicitly.
- A guard whose only job is cleanup is bound to a name (`let _guard = ...`), never to `_`.
- *Anti-patterns:* a `Drop` that blocks on a network call or joins a thread with no timeout; a `Drop` that panics (a panic during unwinding aborts the process); async cleanup attempted in `Drop` by spawning a task nobody waits for; `mem::forget` used to skip cleanup.

**Model the input you will really receive.** A type sketched from the simplest example breaks
on the first real file.

```rust
// Sketch: fine until a generic, async or pub(crate) function shows up.
pub struct Function {
    pub name: String,
    pub signature: String,
}

// Model: every part a requirement reads has a field with a type.
pub struct Function {
    pub name: Ident,
    pub visibility: Visibility,
    pub generics: Option<GenericParams>,
    pub where_clause: Option<WhereClause>,
    pub is_async: bool,
    pub signature: Signature,
}
```

- **Test against samples taken from real code,** including the awkward ones: nested generics, `where` clauses, attributes, macros, unusual whitespace, non-ASCII identifiers.
- **Model what a requirement uses, and be explicit about the rest.** Either keep the unparsed remainder (a span or the raw text) or return an "unsupported" error. Never drop it silently, because a quietly incomplete result is worse than a failure.
- *Skip the full model when* the tool needs one fact (a name, a count). Extract that fact, and still test it against the awkward samples.

### Embedded and `no_std` essentials

This file is not an embedded manual. These are the rules an agent needs so as not to break a
firmware project it is asked to touch. HAL and executor APIs (Embassy, RTIC, the chip HALs)
change between releases: read the versions in `Cargo.lock` and the project's own examples
before writing any of it from memory.

```rust
#![no_std]
#![no_main]

use embassy_executor::Spawner;
use embassy_time::Timer;
use {defmt_rtt as _, panic_probe as _};

#[embassy_executor::main]
async fn main(spawner: Spawner) {
    let p = embassy_stm32::init(Default::default());
    spawner.spawn(blink(p.PA5.into())).unwrap(); // spawn fails only if the task pool is full
    loop {
        Timer::after_secs(1).await;
    }
}
```

- **No heap by default.** Use fixed-size buffers, `heapless` collections and `&'static` data. Add a global allocator only if the project already uses `alloc`, and never allocate in an interrupt handler.
- **Never block in an async task.** Use the executor's timer (`Timer::after_millis`), not a busy-wait delay, which stalls every other task on that executor.
- **Exactly one panic handler,** minimal and non-allocating: signal the fault, then halt or reset. In a debug build `panic-probe` reports over the probe; decide separately what production does (usually reset).

```rust
#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! {
    // put outputs in a safe state, then halt or reset
    loop {}
}
```

- **Write against `embedded-hal` traits** so a driver is not tied to one chip, and so it can be tested on the host with a fake pin or bus. Keep logic in a `no_std` library crate that also builds for the host; keep the chip-specific binary thin.
- **Serialisation:** `postcard` into a fixed buffer. Check lengths and treat every received frame as untrusted.

```rust
let mut buf = [0u8; 64];
let written: &mut [u8] = postcard::to_slice(&reading, &mut buf)?; // Err if it does not fit
let back: Reading = postcard::from_bytes(written)?;
```

- **Target and memory layout live in configuration, not in code.** The target goes in `.cargo/config.toml`; flash, RAM and stack go in `memory.x`. Take the numbers from the chip's datasheet, never from another project.

```toml
# .cargo/config.toml
[build]
target = "thumbv7em-none-eabihf" # Cortex-M4F / M7F
```

```text
/* memory.x */
MEMORY {
  FLASH : ORIGIN = 0x08000000, LENGTH = 512K
  RAM   : ORIGIN = 0x20000000, LENGTH = 128K
}
```

- **Logging:** `defmt` over RTT. No semihosting in production, no formatting or blocking prints in interrupt handlers, no verbose logs on time-critical paths.
- **Shared state between an interrupt and the main code** goes through a critical-section mutex, an atomic or a channel made for it. `static mut` is the anti-pattern.
- **Pin dependency versions.** `"*"` as a version requirement makes a firmware build unreproducible.
- **Verification an agent can do without hardware:** `cargo build --release --target <target>`, `cargo clippy --target <target>`, host-side unit tests of the logic crate, and a check of the binary size against flash (`cargo size`). Say plainly that the code was not run on a device.

- **Flashing names the chip explicitly** (`probe-rs run --chip <CHIP> <elf>`); never rely on auto-detection in a script.
- `#![cfg_attr(not(test), no_std)]` keeps `std` for host tests only. A `no_std` error enum that is `Copy + PartialEq + Eq` and implements `core::error::Error` can be compared directly in tests.
- **Fixed-capacity structures are property-tested for their laws** (idempotence, symmetry, transitivity, no-op operations), and recursion is replaced by a loop where stack depth is constrained.

### Architectural pattern cards

- **Sync core, async shell.** Fetch and parse outside, decide and transform in synchronous pure code, persist and emit outside. The core gets fast unit tests with no runtime; the shell gets integration tests. *Skip for* a small library whose whole job is async I/O.
- **Transport, domain, persistence are three shapes.** Request types, domain values and commands, rows and queries; convert at each edge. It costs conversion code and buys invariants and a clear place for each failure. *Skip when* the service is a thin pass-through with no rules of its own.
- **Split a workspace by change boundary and dependency direction:** core crates, adapter crates, binaries, proc-macro or tooling crates. Not by file count or by when the code was written. Check with `cargo tree` that no core crate pulls in an adapter.
- **A narrow stable API over interchangeable internals.** Callers see one contract; engines and strategies behind it can be swapped. Fits parsers, search and index code, storage and planners, where it buys freedom to optimise without SemVer pressure.
- **A platform workaround lives in one named module** as a pair of pure functions (apply, revert) with a round-trip test, and rewrites an exact value, not a pattern. A workaround that changes security behaviour is a redesign, not a shim.
- **A platform-specific error variant sits under the same `cfg` as the code that produces it,** and every target is built in CI or the gated code rots. *Avoid* gated variants when consumers match exhaustively.
- **Vendored upstream code** is a last resort for when the needed item is not exposed. The module doc records the crate, version, reason and local changes; the licence is kept; inherited lints are allowed, not reformatted, so the diff against upstream stays small. Never for large or security-sensitive code.
- **One state machine over two representations** (string records and byte records, two encodings): put the representation-specific access behind a small private trait, write the logic once over a wrapper, and expose type aliases. If the variants are short, plain duplication is clearer.

```rust
trait Record<'r> {
    fn next_field(&mut self) -> Result<&'r str, DeserializeError>;
    fn next_field_bytes(&mut self) -> Result<&'r [u8], DeserializeError>;
}
pub struct RecordWrap<T>(T);
pub type StringRecordDeserializer<'r> = RecordWrap<StringRecord<'r>>;
pub type ByteRecordDeserializer<'r> = RecordWrap<ByteRecord<'r>>;
```

- **A finite vocabulary is an enum with one spelling function.** Kinds, properties and protocol keywords are typed enums with a single `fn spelling(self) -> &'static str`; no string literals at call sites. A new member updates the enum, the spelling and the schema test together.
- **A registry per family, not scattered checks.** One table holds each member's identity, constructor, file extensions, aliases and resources. Duplicate registrations are detected and an unknown member is reported. Callers never write their own extension check.
- **Detection is an ordered cascade,** cheapest first (file name, extension, a small prefix read, then the fallback), each stage tested on its own. Do not read a whole file to classify it. The same shape fits any "try the common case, then known special cases" extraction: one step per known shape, a comment naming the shape, and an empty result never accepted silently.
- **A fast source composed with a slower, better one.** The trade-off is configuration with named presets (`accuracy()`, `performance()`), not hidden branches. The slow source has a timeout and a fallback, merged results need a stable identity or duplicates leak, and both presets are tested.
- **Optional enrichment sits behind a trait that returns `Result<Option<T>>`:** `Ok(None)` means no data, `Err` a real failure, plus an availability probe. The baseline works without it, tests cover the enriched and the unavailable path, and degraded mode emits a warning or a metric. *Not when* missing data makes the result wrong instead of less rich.
- **Support is not a boolean.** An adapter with known gaps returns `enum SupportLevel { Compatible, Incompatible(Reason), Unsupported(Reason) }` beside the conversion, so a fallback is always explained.
- **Supporting several versions of a host:** common code calls one narrow shim, with one implementation per version chosen by a cargo feature, and cross-version tests where equal behaviour is promised. When versions barely differ, a `cfg` branch is clearer than a shim layer.
- **A heavy runtime (ML runtime, database engine, SDK) hides behind a private state struct.** Construction probes optional accelerators, falls back with a warning, and returns `Result`; there is no "valid" flag for callers to forget. Tests cover the fallback and each missing resource.
- **Parsers:** keep syntax in the grammar or combinators and hand-write only context-sensitive lexing. Recovery that rewrites the input is accepted only when the reparse is clean and every node maps back to original byte offsets; on any doubt keep the original result.
- **Searching many shards with one query:** compute the expensive query representation once, search each shard, merge, sort globally, then apply the limit. Scores compare only when every shard uses the same model and normalisation. Normalise vectors once, and reject near-zero vectors instead of dividing by their length.

### Boundary patterns

**Side effects behind a trait that carries the policy.** When a side effect is subject to a
policy (a sandbox, a tenant, a permission set), the policy travels with each call, and the
adapter, not the caller, picks the safe back end.

```rust
#[async_trait]
pub trait FileSystem: Send + Sync {
    async fn read_file(&self, path: &AbsolutePath, policy: &AccessPolicy) -> FsResult<Vec<u8>>;
    async fn write_file(&self, path: &AbsolutePath, contents: Vec<u8>, policy: &AccessPolicy) -> FsResult<()>;
}
```

- Once the trait exists, nothing above it calls `std::fs` directly. One direct call is one hole in the policy; a clippy `disallowed-methods` entry enforces it.
- Prefer a required policy parameter to `Option<&Policy>`. With an optional one, the easiest call to write is the unchecked one. If "no policy" is legitimate, make it a named value (`AccessPolicy::unrestricted()`) that shows up in review.
- An async method must not hide blocking I/O; the adapter uses async I/O or `spawn_blocking`.
- Where back ends differ in execution model, the trait fixes the contract and each back end decides batching and I/O. An optional optimisation with a no-op default is documented as such, so callers do not assume it ran.
- *Skip when* file access is the whole program and there is no policy boundary.

**Platform facade over private `cfg` back ends.** One public API, with OS-specific modules
chosen at compile time.

```rust
#[cfg(target_os = "windows")]
#[path = "windows/mod.rs"]
mod platform;
#[cfg(target_os = "macos")]
#[path = "macos/mod.rs"]
mod platform;

#[cfg(not(any(target_os = "windows", target_os = "macos")))]
compile_error!("unsupported target: only Windows and macOS are implemented");

pub struct EventLoop<T: 'static> {
    inner: platform::EventLoop<T>,
    _not_send_sync: PhantomData<*mut ()>,
}
```

- An unsupported target fails at compile time with a message, not at run time.
- **`Send` and `Sync` on a public wrapper are decided, not inherited.** Auto traits are an API promise, and for a handle tied to one thread they are unsound. Pin the decision with a compile test:

```rust
fn assert_send<T: Send>() {}
#[test]
fn proxy_is_send() { assert_send::<EventLoopProxy<()>>(); }
// and a compile-fail test (trybuild) that assert_send::<EventLoop<()>>() does not compile
```

- Every platform module exposes the same items with the same signatures, and CI builds each target (`cargo check --target ...`). A `cfg` branch that is never compiled is broken.
- *Use run-time selection* (a trait object) when the back end is chosen by configuration or by what is installed, not by the target.

**Hot reload: mark dirty, rebuild lazily.** The watcher only records that something changed.
The owner rebuilds at the next use, on its own thread.

```rust
pub fn set_shader_code(&mut self, code: Vec<u32>) {
    self.shader_code = code;
    self.dirty = true;
}

pub fn pipeline(&mut self) -> anyhow::Result<&Pipeline> {
    if self.dirty {
        match self.build_pipeline() {
            Ok(built) => self.pipeline = Some(built),
            Err(error) => tracing::warn!(%error, "rebuild failed; keeping the previous pipeline"),
        }
        self.dirty = false;
    }
    self.pipeline.as_ref().context("pipeline was never built")
}
```

- A failed rebuild reports the error and keeps the last working object. A syntax error in a file being edited must not take the program down.
- Debounce events (editors write a file several times per save), and give the watcher thread a stop signal and a join.
- The same shape fits configuration reload: parse and validate the new configuration completely, then swap it in atomically (`ArcSwap` or a `watch` channel). Never apply half a configuration.

**Smaller patterns worth knowing.**

- **Report what was left out.** Anything that filters aggressively (an indexer, a walker, a deduplicator) returns the excluded set and the reason alongside the result, so "why is my file missing" has an answer. Skip lists belong to a named mode (`enum IndexMode { Fast, Full }`), not to a constant buried in the code.
- **Dispatch over a closed set with one exhaustive `match`** into dedicated functions that all produce the same normalised record. No `_ =>` arm, so a new variant fails to compile until it is handled.
- **A fast path is a trait method, not a downcast:** `fn as_native(&self) -> Option<&Native>` in place of `Any` at call sites. Document that the fast path aliases the original.
- **Options scoped to one run travel in a context value** passed down the call path. They are not constructor parameters and not globals.
- **An expensive batch job streams to a caller-owned sink** (`FnMut(Finding) -> Result<(), E>`), so the caller decides rendering, limits and when to stop. Return a `Vec` when results are small.
- **Help text, completions and defaults are generated from the registry used at run time,** so they cannot drift from behaviour.
- **Wrap generated types in a thin newtype** (`pub struct Term(generated::Program);`) and implement the public traits on the wrapper, so regenerating does not change the public API.
- **The file system as the ledger.** A tool that needs a durable list without a database uses one directory per item with a metadata file. Write into a temporary directory and `rename` into place, so a crash never leaves a half-written item visible. Every field the writer writes, the loader reads, and a round-trip test proves it.
- **Declared-then-run pipelines compile once,** at first use, and the documentation says errors surface then. Offer an explicit `build()` or `validate()` for callers who want them early.
- **Tree and plan nodes that are transformed by copying are immutable:** private fields, accessors, and `with_x(self, ..) -> Self`. No reference into the old node survives a transformation.
- **A value that may be borrowed, shared or owned says which:** `Cow<'a, str>`, `Arc<str>`, or an enum with `into_owned()` called before the value outlives its source.
- **An operator set that is small and closed is an enum with `match`.** Use a trait with the full lifecycle (initialise, consume, reset) when third parties add operators, and implement every method before registering one.
- **Rules as data use a small algebra of typed variants,** never raw strings: `enum Matcher { Call { name }, Attribute { root, field }, Regex(CompiledRegex) }`. A variant that one back end cannot evaluate must not silently match nothing; a coverage test lists each (variant, back end) pair.
- **A fingerprint for deduplication or suppression** is a deterministic hash of normalised domain facts (rule ID, relative path, location or snippet hash, message) with a separator between fields. Never hash an address, an absolute path or an iteration order. Too many fields and it breaks on every edit; too few and it suppresses unrelated findings. Keep reading the old format when the scheme changes.

### Transformations that must not lose data

These apply to anything that rewrites, merges, formats or migrates someone else's content.

**A smart algorithm over a trusted conservative one.** Guard the smart path with cheap
preconditions, check its output, and fall back.

```rust
if is_binary(base) || is_binary(ours) || is_binary(theirs) {
    return fallback(base, ours, theirs, FallbackReason::Binary);
}
if [base, ours, theirs].iter().any(|text| text.len() > MAX_SMART_BYTES) {
    return fallback(base, ours, theirs, FallbackReason::TooLarge);
}
let merged = smart_merge(base, ours, theirs)?;
if !postconditions_hold(&merged, ours, theirs) {
    return fallback(base, ours, theirs, FallbackReason::SuspiciousOutput);
}
```

- Preconditions cover what the smart path cannot handle (binary, size, unsupported syntax). Postconditions look for lost or duplicated content.
- **Every fallback is recorded with its reason and counted.** A silent fallback hides that the smart path stopped working; a fallback rate that climbs is a bug report.
- Tests include an adversarial input that forces each fallback, and one that proves the smart path leaves untouched content byte-identical.
- *Skip when* there is no trusted simpler implementation to fall back to. Then the failure is an error, not a guess.

**Pair every structural rewrite with a cheap conservation check.** Count what must be conserved
before and after, and return the original on any difference.

```rust
let mut balance = HashMap::<ItemSignature, i32>::new();
for signature in signatures_of(original)? {
    *balance.entry(signature).or_insert(0) += 1;
}
for signature in signatures_of(&rewritten)? {
    *balance.entry(signature).or_insert(0) -= 1;
}
if balance.values().any(|count| *count != 0) {
    return Ok(original.to_owned()); // something was lost or duplicated
}
```

- **Formatters and codemods are idempotent and output still parses.** Both are tests: `format(format(x)) == format(x)`, and the result parses to an equivalent tree.
- **Re-parse after every change to the text.** No pass reads a tree built from an earlier version of the string.
- **Protected regions round-trip byte for byte.** Replace each opt-out region with a placeholder that cannot collide with real content, run the passes, restore, on every path including errors.
- **Reordering uses a stable sort,** carries comments and attributes with their item, and leaves unknown nodes in place. Do not reorder where order has meaning (macro definitions, `mod` declarations with `#[macro_use]`, trait-impl overlap, SQL migrations).

**A plan carries unsupported work as data.** A planner for migrations, rollouts or refactors
returns the whole plan, with the parts it cannot do as typed steps, so a reviewer sees
everything at once. It does not stop at the first incompatible change.

```rust
#[derive(Serialize, Deserialize)]
#[serde(tag = "kind", rename_all = "snake_case")]
pub enum MigrationStep {
    AddType { name: String },
    RenameType { from: String, to: String },
    Unsupported { entity: String, reason: String },
}

pub struct MigrationPlan {
    pub steps: Vec<MigrationStep>,
}

impl MigrationPlan {
    pub fn is_executable(&self) -> bool {
        !self.steps.iter().any(|step| matches!(step, MigrationStep::Unsupported { .. }))
    }
}
```

- Planning is pure and separate from execution: plan, show, confirm, apply. The executor refuses a plan that contains an unsupported step; it never skips one.
- The plan is serialisable, so it can be reviewed, stored and replayed.

**Coordinating several writers.** A claim ("agent A is editing this") is an advisory lock; it is
not proof that nothing else changed. Detect concurrent edits with a version (a counter, a
content hash, or a version vector with one counter per writer) checked at write time, and
expire stale claims with a heartbeat. *For one writer, or where a hard lock is acceptable, a
database transaction is simpler and stronger.*

### Parsers, rule engines and linters

Rules for the cases where a task builds or extends one.

- **Operators that share a parse shape are a table,** `const BINARY_OPS: &[(Token, Prec, Assoc)]`, driving one precedence-climbing function. A new operator is a row.
- **Try the most specific alternative first.** Add a broad fallback only after a real input proves the need, and give every fallback branch a corpus case.
- **Context-sensitive lexing is explicit lexer state:** a closing delimiter that must match its opener (heredocs, raw strings with a variable number of `#`) stores the opener and clears it on close. Indentation-sensitive layout is an indent stack, with no indent or dedent tokens inside brackets. If the parser is incremental, that state serialises and the round trip is tested.
- **A large grammar, schema or rule set is composed from modules,** and composition fails on a duplicate name. A later module never silently wins.
- **A translator from a specific tree to a common model is pure:** no I/O, no logging, no global state. Queries are compiled once, not per file. The caller adds file and repository context one layer up.
- **Names emitted by a parser stage are a contract** with the stage that consumes them. Each new one gets a fixture that follows it to its destination. Same-named items (overloads) get a disambiguator so one does not overwrite another.
- **A rule engine filters once and buckets by kind,** so each item meets only the rules that can apply; route on the enum variant, not on a string prefix. The walker visits the tree once and dispatches by node kind. With a handful of rules, plain `if` statements are clearer.
- **A rule trait with default no-op hooks** lets a rule opt into raw source, selected nodes, or a final pass:

```rust
pub trait Rule {
    fn node_kinds(&self) -> &[&str] { &[] }
    fn check_source(&mut self, _source: &str) -> Vec<Issue> { Vec::new() }
    fn check_node(&mut self, _node: &Node, _source: &str) -> Vec<Issue> { Vec::new() }
    fn finish(&mut self, _source: &str) -> Vec<Issue> { Vec::new() }
}
```

- **Parser inputs are hostile.** Bound recursion depth, input size and time; return an error with a byte offset; never panic on malformed input. A fuzz target or a property test (`parse` never panics; `print(parse(x))` re-parses to the same tree) finds what examples miss.

### Pipelines, registries and handler chains

**A phased pipeline is data.** A compiler, indexer or ETL job is an ordered table of passes,
each with a name and a failure policy.

```rust
struct Pass {
    name: &'static str,
    required: bool,
    run: fn(&mut Context) -> anyhow::Result<()>,
}

for pass in PASSES {
    let started = Instant::now();
    let result = (pass.run)(&mut ctx);
    tracing::info!(pass = pass.name, elapsed = ?started.elapsed(), ok = result.is_ok());
    match result {
        Err(error) if pass.required => return Err(error.context(pass.name)),
        Err(error) => {
            tracing::warn!(pass = pass.name, %error, "optional pass failed");
            ctx.degraded.push(pass.name);
        }
        Ok(()) => {}
    }
}
```

- **Order is behaviour.** A new pass states what it needs from earlier passes and where it sits, and gets a test for cancellation after it.
- **"Optional" is rare and visible.** An optional pass that fails is recorded in the result (`degraded` above), not only logged, so the caller and the tests can see it. Default to required; a pass nobody would miss should not exist.
- *Skip the table for* two or three steps. Three function calls in a row are clearer than a pass framework.

**A handler chain where a handler can say "not mine".** In a chain of plugins, codecs,
authentication schemes or planners, each handler returns `Result<Option<T>>`: `Ok(None)` means
"not mine", `Err` means "mine, and it failed".

```rust
let mut plan = None;
for planner in &self.planners {
    plan = planner.plan(node, inputs).await?;
    if plan.is_some() {
        break;
    }
}
let plan = plan.ok_or_else(|| PlanError::NoPlannerFor { node: format!("{node:?}") })?;
self.ensure_schema_matches(node.schema(), &plan)?;
```

- The first `Some` wins, so registration order is behaviour: document it and test two handlers that both accept an input.
- "Nothing accepted this" is its own error and names the input.
- Validate what a handler returns before trusting it; a plugin is not your code.
- *Anti-pattern:* a handler that returns `Ok(None)` on its own failure. The chain then moves on and the real error is lost.
- If every handler must handle every input, use plain `Result`.

**Check every rewrite rule where it runs.** A rewrite pipeline (optimiser, tree or graph
transform) wraps each rule in a postcondition that names the rule, so a bad rewrite is caught
next to its cause and not three passes later.

```rust
let before = plan.schema();
let plan = rule.rewrite(plan, config)?;
if !is_allowed_schema_change(&before, &plan.schema()) {
    return Err(OptimizerError::SchemaChanged { rule: rule.name().to_owned() });
}
#[cfg(debug_assertions)]
check_invariants(&plan)?;
```

- Cheap checks always run. Whole-structure walks run under `cfg(debug_assertions)` or a flag, and CI runs the test suite with them on.
- Each rule ships with a negative test built on a deliberately invalid rewrite, which proves the check can fire.
- Say what the check does not cover. A partial invariant read as a full one gives false confidence.

**Registries.**

- **An open set is a trait plus registration; a closed set is a `match`.** Use a registry when the set is meant to grow without edits to the orchestration (languages, providers, formats). For one or two cases a `match` is simpler and exhaustive.
- **An unknown key is a typed error that lists the supported values.** Never a panic on a missing map entry, never a silent default.
- **Decide the duplicate policy** (reject, or last wins) and test it. Reject is the safer default.
- **Capabilities are read from the registry.** Do not keep a second hand-written support matrix; it will drift. Capability tests and help output query the registry.
- **A new member is added to every per-member table in one change,** with one smoke fixture that exercises the whole path.
- **The fallback arm of a dispatcher returns a domain error naming the operation and the back end** ("no translation for `X` in back end `Y`"), raised at the dispatch point. Not `unreachable!()`, and not a missing-function error from deep inside.

**Extension traits: each default states what it means.** Required methods form the core
contract. For every default method decide whether it means *unsupported* (an error naming the
operation), *no-op* or *delegate*. A default encoder that returns `Ok(())` loses data silently;
prefer the explicit unsupported error unless a round-trip test proves the no-op is lossless.
Decode failures are always explicit.

**Inject content access.** An analyser or parser takes a narrow reader, for example
`impl Fn(&Path) -> io::Result<Vec<u8>>`, and does not call `std::fs::read` itself. The same
logic then runs over the working tree, a Git revision or an in-memory fixture. Document whether
paths are absolute or relative to a root. *Skip when* the code needs metadata, streaming or
directory walking; pass a small file-system trait then.

**A storage capability in front of handlers.** Handlers depend on a few domain operations
(`begin_upload`, `reader`, `finalize_upload`), not on file paths or bucket names. Add a method
when a second call site needs it. *Skip when* there is one back end, no test double, or the
call sits in a hot loop where a boxed reader per item costs too much.

**Derived state is computed, not stored.** `plan.is_executable()` is derived from the steps; a
stored `supported: bool` can disagree with them. Store a derived value only as a measured
cache, with one function that updates both.

### Middleware, capabilities and shared vocabulary

**Layered middleware: static when the stack is fixed, dynamic when it is configured.** When the
concerns around one back-end trait (retry, logging, metrics, timeout) are known at build time,
compose them as types. A layer wraps an inner implementation, and a forwarding trait with a
blanket impl supplies every operation, so a layer overrides only what it changes.

```rust
pub trait Layer<A: Access> {
    type Layered: Access;
    fn layer(&self, inner: A) -> Self::Layered;
}

pub trait LayeredAccess: Send + Sync + 'static {
    type Inner: Access;
    fn inner(&self) -> &Self::Inner;
    // every operation has a default body that forwards to self.inner()
}

impl<L: LayeredAccess> Access for L { /* forwards every operation */ }
```

- It buys a hot path with no dynamic dispatch. It costs long type names, slow compiles and hard error messages.
- **Order is behaviour.** A retry layer outside a timeout layer retries timeouts; inside it, all the retries share one timeout. Metrics outside retry count one call; inside, they count every attempt. Write the intended order down and test it.
- *Use trait objects* when layers are chosen at run time, or when the call is I/O-bound and one virtual call is noise. For HTTP services use the ecosystem's `tower` layers; do not invent a parallel system.

**One capability gate for optional arguments.** A unified API over providers that differ keeps
a capability record per back end and checks optional arguments in one layer, before the request
reaches the back end.

```rust
async fn write(&self, path: &str, args: OpWrite) -> Result<Writer> {
    let capability = self.info.capability();
    if args.content_type().is_some() && !capability.write_with_content_type {
        return Err(unsupported(&self.info, Operation::Write, "content_type"));
    }
    self.inner.write(path, args).await
}
```

- The error names the operation, the argument and the back end. Callers never scatter capability checks, and a back end never silently ignores an argument it cannot honour.
- A new optional argument adds the capability bit, the check and a test against a back end that lacks it.

**Middleware states which form of the body it sees.** Interceptors that read or change the
request's meaning run before serialisation; signing and authentication that need the final
bytes run after it. Model it with `enum Body { Message(Request), Bytes(Bytes) }` or two typed
stages, and test the common chain: mutate, serialise, sign. Mutating after signing is the bug
this prevents.

**A shared vocabulary lives in one crate.** Names that several crates read and write in one
persisted schema (table names, relationship kinds, event types) are closed enums with `ALL`,
`as_str` and `FromStr`:

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum EdgeKind { Calls, Imports, Implements }

impl EdgeKind {
    pub const ALL: &[EdgeKind] = &[EdgeKind::Calls, EdgeKind::Imports, EdgeKind::Implements];
    pub const fn as_str(self) -> &'static str {
        match self {
            EdgeKind::Calls => "calls",
            EdgeKind::Imports => "imports",
            EdgeKind::Implements => "implements",
        }
    }
}
```

- A new kind then fails to compile in every exhaustive `match` downstream, which is the point. A test round-trips every member of `ALL` through `as_str` and `FromStr`.
- The spelling is a persisted format. Renaming a variant is free; changing its string is a data migration. An alias kept for old data is recorded as compatibility debt.

**Smaller rules.**

- **One gate owns transaction mode.** Where explicit and implicit (per-statement) transactions coexist, one context object holds the lifecycle and every statement path goes through it. Starting a transaction while one is active is an error, as is a write inside a read-only one. Nesting needs savepoints.
- **Loading a stateful extension is idempotent by a unique name:** already loaded means return. Initialise before recording it as loaded, persist the fact, and replay loads at startup. Never load a dynamic library and lose track of it.
- **Selecting among discovered implementations is a policy function:** highest explicit priority, a stable tie-breaker (the name), and a loud failure when there is none. Test that the intended one wins.
- **One source of truth per builder field.** If a field accepts a typed value or a pre-serialised escape hatch, `enum Bindings { Typed(Map), Raw(String) }` makes mixing them unrepresentable. Otherwise `build()` returns an error; a library does not panic for this. Irreversible conversion waits until `build()`.
- **Registry keys are structs, not joined strings.** Canonicalise first (trim, case-fold, fill defaults), then use a struct deriving `Hash` and `Eq`. A delimiter-joined string breaks the day a part contains the delimiter.
- **Compile user-authored rules once.** Validate, resolve cross-references and build lookup tables at load time; resolution at run time is then cheap. Conflict order is an explicit field with a documented direction, two rules with the same key and order are a load error naming both, and nothing depends on map iteration order.
- **Reload by build, swap, bump.** Build the new plugin or rule set off to the side, swap it in atomically (`ArcSwap`), and bump a version so caches holding decisions from the old set invalidate them. An allow-listed host API is not a sandbox and does not make untrusted plugin code safe.
- **Data-access ladder.** Use the narrowest layer that expresses the query: the built-in typed operation, then a typed query, then a hand-written query, then raw SQL. Raw SQL always uses bound parameters, never string formatting.
- **Tree nodes share one identity contract:** structural equality, a hash consistent with it, deep clone, a debug dump and conversion back to source. An enum deriving `PartialEq`, `Eq`, `Hash` and `Clone` gives this with no variant able to forget a field. With trait-object nodes, test `clone(x) == x`, equal hashes and the source round trip.
- **A local rewrite does five things in order:** check its own switch, prove the node's shape (arity, types), prove the result type and nullability are preserved, rewrite, then re-resolve the new node through the normal resolution path instead of filling in its type by hand. A rewrite that needs whole-plan reasoning is not a local visitor.
- **Limits that differ by value kind** share one entry point that checks compatibility, and each kind owns only its own rule: `enum Limit { Bool(bool), Int(i64), Float(f64) }` with one `is_violated(&Value) -> Result<bool, TypeMismatch>`.

### Trees, lowering and decision gates

**Recursion control is a value.** A tree walk's hooks return what to do next, and a node type
implements only `apply_children` to get the walk for free.

```rust
pub enum Recursion {
    Continue, // keep walking
    Jump,     // skip this subtree
    Stop,     // end the whole walk
}

pub trait TreeNode: Sized {
    fn apply_children<F>(&self, f: F) -> Result<Recursion>
    where
        F: FnMut(&Self) -> Result<Recursion>;

    fn visit<V: Visitor<Node = Self>>(&self, visitor: &mut V) -> Result<Recursion> {
        match visitor.pre_visit(self)? {
            Recursion::Stop => return Ok(Recursion::Stop),
            Recursion::Jump => return visitor.post_visit(self),
            Recursion::Continue => {}
        }
        if let Recursion::Stop = self.apply_children(|child| child.visit(visitor))? {
            return Ok(Recursion::Stop);
        }
        visitor.post_visit(self)
    }
}
```

- Visitors do not smuggle control flow through side-effect flags. Each early exit has a comment, and the continue, jump and stop cases each have a test.
- **Recursion depth follows input depth.** For trees built from untrusted or generated input, cap the depth and return an error, or walk with an explicit stack. A stack overflow is an abort, not a `Result`.
- *Skip for* shallow data of fixed shape: a `match` is simpler.

**Lower the parse tree to a small typed tree first.** Do not run domain logic on generic parser
nodes with string kinds. Convert into the smallest typed tree that holds what the algorithm
needs, keeping a span on every node for diagnostics.

```rust
pub enum Statement {
    Simple { text: String, span: Range<usize> },
    Return { text: String, span: Range<usize> },
    If { cond: String, then: Box<Statement>, otherwise: Option<Box<Statement>>, span: Range<usize> },
    While { cond: String, body: Box<Statement>, span: Range<usize> },
    Block(Vec<Statement>),
}
```

- The lowering is where "unsupported construct" is reported, once, with a span. After it, the algorithm matches exhaustively and has no string comparisons.
- A tree with single ownership is `Box` and `Vec`. `Rc<RefCell<_>>` is for real sharing; a graph is usually better as an arena, a `Vec` of nodes addressed by index.
- Test the conversion before building anything on it.
- *Skip when* the work needs full fidelity: comments, whitespace, exact tokens (formatters, refactoring tools).

**Scoped context is passed by value.** A recursive pass that needs "where does `break` go from
here" carries the answer in a small `Copy` struct, not in mutable state it must remember to
restore.

```rust
#[derive(Clone, Copy)]
struct Scope {
    break_target: Option<NodeIndex>,
    continue_target: Option<NodeIndex>,
}

let body_scope = Scope { break_target: Some(loop_exit), continue_target: Some(loop_update) };
build(body, graph, body_scope)?;
// the caller's scope is untouched here
```

- With a mutable context the save and restore must bracket every recursive call, including the early-return paths; a missed restore leaks one branch's state into the next. If mutation is unavoidable, restore through a guard whose `Drop` does it.
- Every new control construct gets a test with nesting.

**Placeholders never leave the builder.** Internal scaffolding (dummy nodes, sentinel entries)
is acceptable while building, provided a normalisation pass removes it and the boundary rejects
any survivor with a hard error before the value is returned, serialised or rendered.

```rust
while remove_unreachable_nodes(&mut graph) {}
while remove_placeholder_nodes(&mut graph)? {}
ensure_no_placeholders(&graph)?;
```

- A cleanup loop runs to a fixed point: the function returns whether it changed anything, and each iteration must make progress, or the loop does not terminate.
- Stronger still is two types, a builder node with a `Placeholder` variant and a final node without one, so the conversion is the check.

**Ordered pure rules with evidence.** A decision gate (access, quota, deployment, safety)
evaluates pure rules in priority order, with the rule name as tie-breaker. Each returns a
decision, structured evidence and a readable reason.

- Rules do no I/O. Facts are gathered first and passed in, which makes every rule a table test and makes the decision reproducible from the recorded inputs.
- Record the decision, the deciding rule and the evidence. "Denied" with no rule name cannot be debugged.
- State the combination policy (first match, or deny overrides allow) and what happens when no rule matches. For anything security-relevant, no match means deny.
- Each rule is tested alone and in interaction with the rules above it.

**Render back ends behind one trait.** Parse, then build the model, then render. The model
knows nothing about output formats, and each format is one small implementation over it.

```rust
pub trait Render {
    fn render(&self, graph: &Graph) -> Result<String>;
}

pub enum Backend { Dot, Tikz, D2 }

impl Render for Backend {
    fn render(&self, graph: &Graph) -> Result<String> {
        match self {
            Backend::Dot => dot::render(graph),
            Backend::Tikz => tikz::render(graph),
            Backend::D2 => d2::render(graph),
        }
    }
}
```

- For a closed set of back ends an enum with a `match` needs no macro and no boxing. The `enum_dispatch` crate generates the same thing when the trait has many methods.
- Escaping belongs to the back end. Every back end is tested with labels containing its own special characters (quotes, braces, backslashes, newlines).
- Output is deterministic: iterate in a defined order, so the rendered text can be compared in a snapshot test.

**Fetch context in rungs.** When gathering context is expensive (for an agent or a tool), order
the sources from cheapest to dearest (summary, outline, the relevant path, raw source). Start at
the cheapest and go up a rung only when the current one did not answer the question, under a
hard cap.

### Storage, artifacts and edits

**One core crate, several thin adapters.** When one engine serves a desktop UI, a CLI, a server
and tests, the core owns the request and response types and the orchestration. Each adapter
converts input, calls the core and maps the error, and nothing else. Review check: an adapter
file containing an `if` about domain rules has logic in the wrong place.

**A storage factory with an in-memory back end.** The back end is chosen by configuration (a
URI scheme: file, object store, memory). The in-memory one implements the same trait and passes
the same contract suite, which gives tests a fast, deterministic store.

```rust
// One suite, run against every back end.
pub fn contract_suite(store: &dyn Storage) {
    put_then_get_returns_same_bytes(store);
    get_missing_key_is_not_found(store);
    overwrite_replaces_value(store);
    list_is_sorted_and_complete(store);
}

#[test]
fn memory_store_meets_contract() { contract_suite(&MemoryStore::default()); }
#[test]
fn file_store_meets_contract() { contract_suite(&FileStore::new(tempfile::tempdir().unwrap().path())); }
```

- The contract suite is what keeps a fake honest. Without it, tests pass against behaviour the real back end does not have (ordering, case sensitivity, atomicity).
- *Skip the trait when* every call site needs back-end-specific features; a lowest common denominator that leaks is worse than a concrete type.
- **An enum for which, a trait for how.** A persisted enum of provider kinds maps each variant to an implementation that can detect, install and run it, and every variant passes the same contract tests. Renaming a persisted variant is a data migration.

**Artifacts on disk.**

- **Any artifact of more than one file has a manifest** naming each file, its layout and the format version. The reader opens files through the manifest, never by file-name convention. Tests round-trip the manifest and open an artifact written by the previous version.
- **A format carries a version from its first release,** and the reader rejects a version it does not know with an error that states both versions.
- **A manifest does not store its own path.** A type that saves itself keeps the path in a `#[serde(skip)]` field set by the reader. A missing file is `Ok(None)`, not an error, when absence is normal.
- **Memory-mapped data sits behind typed cursors.** Validate the ID at the edge and return a typed view over `offsets[n]..offsets[n + 1]`; higher layers never index the raw mapping. A mapped file is untrusted input: check every offset and length before slicing, and remember that another process truncating the file makes the mapping fault.
- **Write atomically:** write to a temporary file in the same directory, flush, then rename over the target.

**A validated edit set, applied back to front.** A tool that modifies text computes every edit
as a byte range against the original, rejects out-of-range and overlapping edits, and applies
from the end backward so earlier offsets stay valid.

```rust
pub struct TextEdit {
    pub start: usize,
    pub end: usize,
    pub replacement: String,
}

pub struct EditSet {
    edits: Vec<TextEdit>,
}

impl EditSet {
    pub fn new(mut edits: Vec<TextEdit>, source: &str) -> Result<Self, EditConflict> {
        edits.sort_by_key(|e| (e.start, e.end));
        for e in &edits {
            let in_bounds = e.start <= e.end
                && e.end <= source.len()
                && source.is_char_boundary(e.start)
                && source.is_char_boundary(e.end);
            if !in_bounds {
                return Err(EditConflict::OutOfBounds { start: e.start, end: e.end });
            }
        }
        for pair in edits.windows(2) {
            if pair[1].start < pair[0].end {
                return Err(EditConflict::Overlap { at: pair[1].start });
            }
        }
        Ok(Self { edits })
    }

    /// `source` must be the string the set was validated against.
    pub fn apply(&self, source: &str) -> String {
        let mut out = source.to_owned();
        for e in self.edits.iter().rev() {
            out.replace_range(e.start..e.end, &e.replacement);
        }
        out
    }
}
```

- The `is_char_boundary` check is what stops `replace_range` panicking on multi-byte text.
- **Positions are converted once, in one tested function.** Editors count lines and UTF-16 code units, parsers count bytes, humans count from one. Tests include a multi-byte character and an emoji before the edited position.
- Two inserts at the same offset need a stated order (a priority field, or input order with a stable sort).
- Tests: one edit, several disjoint edits, same-position inserts, overlap rejected, out-of-bounds rejected, non-ASCII text.

**Editor back ends.** Translate each change into the parser's native edit, apply it to the old
tree and re-parse incrementally; recompute highlights and diagnostics on a debounce. Keep a
bounded map from buffer version to tree, and cancel a stale parse when a newer edit arrives.
Test insert, delete and multi-line edits, not only the first parse. *For small files or
parse-once input, a full re-parse is simpler and none of this is needed.*

**A stdio tool server is a loop over a registry.** Read one JSON-RPC request per line, dispatch
by method, write exactly one JSON line per response.

- **Stdout carries the protocol and nothing else.** Logs go to stderr. One stray `println!`, from your code or a dependency, corrupts the stream.
- Invalid JSON gets a parse-error response and the loop continues. An unknown method gets a method-not-found response. A handler that panics must not take the server down: isolate it and answer with an internal error.
- Flush after every response, and exit cleanly when stdin reaches end of file.
- Integration tests send initialise, list, an unknown method, invalid JSON and one real call, and assert that every response is one line of valid JSON.

**Invariants over a whole collection.**

- **A collection invariant lives in a wrapper.** When no single element can enforce it (every batch has the declared schema, every part belongs to one tenant), a wrapper owns the collection and `try_new` rejects the first violation, naming the expected and the actual value. `TryFrom` impls reuse that constructor; `into_inner` gives the parts back. Do not hand out `&mut` to the inner collection, or the invariant is gone.
- **A duplicate registration is a typed error.** Whatever owns scarce names (routes, URL schemes, sockets, commands) refuses a second registration with an error carrying the name, and leaves its state unchanged. Nothing is overwritten silently.
- **Typed attributes for composed views.** When several views share one graph or document model, the view-specific meaning is a typed attribute (`enum EdgeKind { Ast, ControlFlow, DataFlow }`), not a free-form string that degrades silently when misspelled.
- **Emulating a missing platform feature** with a narrower one is a small pure module of three functions (match, apply, revert) with a round-trip test and a test that names sharing a prefix do not match. Not where security depends on the original semantics, such as a page's origin.

### Module depth and seams

- **Judge a module by its depth.** A module's interface is everything a caller must know: signatures, invariants, ordering rules, errors, configuration and performance. A deep module hides a lot of behaviour behind a small interface. *Deletion test:* if deleting the module would push the same complexity into every caller, it earns its place; if the complexity simply disappears, it was a pass-through.
- **A seam needs two adapters.** Put a trait where behaviour really varies: several back ends, or a production and a test implementation. A trait with one implementation and no test double is not a seam yet; it is an indirection.
- **Semantics belong to the interface.** If correctness depends on conflict rules, scan order, write ordering or atomicity, the trait's documentation states them and each adapter either implements them or returns an explicit unsupported error. A contract suite checks it.
- **One required method, many provided.** When many wrapper types share operations, the trait requires one accessor to the core and supplies the rest as default methods.
- **Plugin seams are object-safe.** A trait called through `dyn` has no generic methods and no `Self` by value; generic conveniences live in an extension trait or a builder. Publish one implementation-independent test suite that every adapter runs.
- **Back ends advertise what they support.** Default bodies return an explicit unsupported error, capability flags say which are real, and a conformance test checks the flags against the behaviour.

### Protocols, messages and state

**Parse bytes without doing I/O.** A codec takes a byte slice and returns a frame plus the
number of bytes consumed. The transport owns reads, timeouts, encryption and backpressure.

```rust
pub enum Decoded<'a> {
    Frame { frame: Frame<'a>, consumed: usize },
    NeedMore { at_least: usize },
}

pub fn decode(buf: &[u8]) -> Result<Decoded<'_>, FrameError> {
    let Some(header) = buf.get(..HEADER_LEN) else {
        return Ok(Decoded::NeedMore { at_least: HEADER_LEN - buf.len() });
    };
    let len = u32::from_be_bytes([header[0], header[1], header[2], header[3]]) as usize;
    if len > MAX_FRAME_LEN {
        return Err(FrameError::TooLarge { len });
    }
    let total = HEADER_LEN + len;
    match buf.get(HEADER_LEN..total) {
        Some(payload) => Ok(Decoded::Frame { frame: Frame { payload }, consumed: total }),
        None => Ok(Decoded::NeedMore { at_least: total - buf.len() }),
    }
}
```

- "Not enough bytes yet" is not an error; it is distinct from "malformed". Conflating them either drops slow connections or accepts garbage.
- **Check the declared length against a maximum before allocating or waiting for it.** A length field from the network is an allocation request from a stranger. Use `get(..)` and checked arithmetic, never indexing.
- The same codec then works over TCP, a file, a test vector and a fuzzer. Tests: a short header, a length beyond the buffer, a length over the maximum, several frames back to back, a round trip. A fuzz target asserts that decoding never panics.
- **A stream that ends at a record boundary is `Ok(None)`; one that ends inside a record is an error.**
- A format that leaves the process family gets a version header and compatibility tests.

**An envelope for every message on a shared bus.**

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BusEvent<T> {
    pub id: Uuid,
    pub subject: String,
    pub timestamp: DateTime<Utc>,
    pub source: String,
    pub payload: T,
}
```

- Subjects are constants shared by publisher and subscriber. The subject and source stay in the body, not only in broker headers, so an event can be stored, replayed and inspected on its own.
- **Delivery is at least once, so consumers are idempotent,** keyed on `id`. Order across subjects is not guaranteed unless the broker says so.
- Adding an optional payload field is compatible; renaming or removing one is not. Version the subject or the payload when it must break.
- Tests round-trip real payloads and cover acknowledge, reject and redelivery against a real broker, not a mock.

**Wire types and internal types are different types.**

- **Internal events are translated, not serialised.** One function maps each internal event to an optional protocol message; internal enums never go on the wire, or every refactor becomes a protocol change. Snapshot-test each mapping.
- **Nothing unwraps a wire field.** Required fields go through a helper that returns an error naming the missing field. Each variant has a golden fixture, plus a negative one with a required field removed.
- **A name resolved on demand needs an allow-list.** A lookup that falls back to treating an unknown name as a URL or a path accepts only explicit schemes and rejects the rest clearly. This is how a convenient fallback becomes a file-read or request-forgery hole.

**Actors behind a typed mailbox.** Callers hold a handle with methods; the channel is private.

```rust
#[derive(Clone)]
pub struct CounterHandle {
    tx: mpsc::Sender<Command>,
}

enum Command {
    Add { amount: u64, reply: oneshot::Sender<u64> },
}

impl CounterHandle {
    pub async fn add(&self, amount: u64) -> Result<u64, ActorGone> {
        let (reply, rx) = oneshot::channel();
        self.tx.send(Command::Add { amount, reply }).await.map_err(|_| ActorGone)?;
        rx.await.map_err(|_| ActorGone)
    }
}
```

- The mailbox is bounded, and what happens when it is full is decided (wait, or `try_send` and reject).
- The actor ends when every handle is dropped (`recv` returns `None`) or on a shutdown signal, and its exit is observable through its `JoinHandle`.
- Tests work at the handle: send after exit, a full queue, a dropped reply, a panic inside the actor.
- *Use when* state has one logical owner and several async callers. *Skip when* a mutex held briefly with no `.await` inside does the job; it is simpler and faster.

**Smaller rules.**

- **Lifecycle metadata lives apart from payloads.** For jobs with large bodies, one store holds the record (ID, state, attempts, deadlines, last error) and another holds the bodies. Leases, retries and polling then change without touching payload storage.
- **A journal sits on narrow storage.** The storage trait offers positioned read and write; the journal above it owns append, lookup and recovery. The same tests run against a temporary file and memory, including reopen, a torn final record and a corrupted entry.
- **Lazy loading state is an enum in the registry:** not loaded, loading with its waiters, loaded, failed with the cached error. Concurrent requests join the one load (`tokio::sync::OnceCell` covers the simple case). Decide whether a failure is cached or retried.
- **Detection is pure; verification is a later step.** Classify arguments with slice patterns in a function with no side effects; file-system checks and execution come after, explicitly.
- **A rewrite reports whether it changed anything,** and an unchanged node must say so, or a fixed-point loop never ends. The driver also has a pass limit and checks an invariant after every rule.
- **Variants of one algorithm share one output type,** and a compare mode runs the simple and the optimised variant and fails when they differ. It is the cheapest oracle available for an optimisation.
- **An operator that returns a stream does no work until polled** and never blocks inside `poll`. Tests poll it, check the schema and drop it early.
- **A guard fixes the order of unlock and side effect.** When an effect must follow a lock release, a guard's `Drop` releases and then runs the effect, so no path can do them in the wrong order.
- **Versions are explicit in storage.** A read states the version it reads as of, and a held read blocks compaction below that version. Operations that combine versions or timestamps return `None` on overflow.
- **A schema states capabilities per field** (queryable, stored, sortable); ingestion and query parsing both read it, and a query on an unsupported field is an error, not an empty result.
- **Constrained choices are `Copy` enums with `ALL` and `const fn` relations** (valid partners, command names, defaults), so prompts, validation and docs read one source.

**Small languages and analysis hosts.**

- **A public parse entry point consumes the whole input:** skip surrounding whitespace, then require end of input, so trailing garbage fails. Inner rules never require end of input, because they must compose.
- **Two entry points:** one returning the domain error for programs, one returning a rendered diagnostic with a source span for people. The parsing library's types stay inside the module; the API returns owned nodes.
- **Grammar first, meaning second.** The grammar accepts the shape. Rules that need context (duplicates, unknown names) live in a later check with domain messages, and negative tests assert the message.
- **Owned output keeps byte ranges.** When results outlive the source text, convert to owned values paired with their source ranges. Never drop the ranges; diagnostics and navigation map back through them.
- **A hand-written mini-language stays tiny.** Acceptable for a controlled internal format with a handful of constructs. Once it needs expressions, escaping, includes or untrusted input, use a maintained parser crate.
- **A virtual file system sits between I/O and analysis.** Analyses never read the disk; a loader does, and the VFS assigns file identities and merges changes. Tests use an in-memory loader.
- **Extraction is pure; storage is incremental.** Functions turn input into facts; a store keeps them. A test changes one file and checks that only its dependents are recomputed. An incremental result is compared with a from-scratch run on the final input: that golden test catches most incremental bugs.
- **One context owns the caches,** with a memoised "derive this" method; individual checks consume the context. A test runs two checks over one item and asserts a single derivation.
- **Anything touching unstable compiler internals sits in one thin adapter,** and the toolchain version is pinned and treated as part of the interface.
- **External tools are candidates behind a trait** (detect, installed, install, version) that receives a command runner; tests pass a fake runner.

### More boundary rules

- **Options are a named type.** Two or more booleans passed together become a small options struct with named constructors (`SortOptions::desc().nulls_last()`). `sort(true, false)` is unreadable at the call site and easy to swap.
- **A walker borrows per step.** A traversal object that borrows the graph only inside `next(&mut self, graph: &Graph)` lets the caller mutate the graph between steps; an iterator that holds `&Graph` for its whole life does not.
- **A list assembled from features is built in one place.** One function takes configuration and discovered context and returns the complete, validated list (tools, routes, commands) with its handlers; features do not append to it from elsewhere. Reject duplicate names and missing handlers, and snapshot the result per representative configuration.
- **Subprocess placement is an adapter.** A launcher takes a command and returns a transport that owns the process handle and its cleanup. Tests start a fixture process, exchange one message, close, and assert that no child remains; on Unix, test process-group termination as well.
- **A cloneable handle is `Arc<Inner>`,** and teardown order lives in `Inner`'s `Drop`. When deleting, remove the manifest before the data, so an interrupted cleanup cannot resurrect deleted data. A fatal persist failure poisons the handle so later calls fail fast.
- **Snapshots and write transactions share a read-only trait.** Query helpers take `impl Readable`, which has no write methods, so one helper serves both and cannot break a repeatable read.
- **Read and write traits are split.** Algorithms depend on the read trait and the mutable trait extends it, so an algorithm can be tested against a read-only fake and cannot write by accident.
- **Collection is split from merge.** A collector yields a partial result per segment and merges them at the end, so the engine can run segments in parallel. The merge must not depend on order; a test shuffles the partial results.
- **A node that runs also reports facts.** A plan operator exposes its output schema, ordering and input requirements beside `execute`, so optimiser passes reason through the trait and a generic invariant check can reject an invalid custom operator.
- **Scans accept pushdown and say what they did with it.** A scan takes projection, filters and a limit, and reports per filter whether it was applied exactly, inexactly or not at all. Then the caller knows what it still has to re-check.
- **Local and remote implementations share one trait and one contract suite,** and a slow remote produces the same error shape as a local timeout.
- **An escape hatch states its invariant.** When a wrapper exposes its inner value for advanced use, the documentation says what the caller must keep true, and a property test compares the high-level operation with the raw manipulation.
- **Optional hooks get a builder.** An extension point with many optional lifecycle hooks keeps one trait with inert defaults and offers a builder that stores only the closures supplied. Hooks run in a documented order.
- **Generated build artifacts are named by content.** A build script hashes the generated bytes and writes under `OUT_DIR` only when they changed, so an unchanged input triggers no rebuild.
- **Validate plugin configuration once, at initialisation,** and fail there with a clear message, before any work starts.
- **Internal objects do not cross a process boundary.** Define serialisable domain types beside the adapter, and snapshot their structure, not `Debug` strings. `Debug` output is not a stable format.
- **A degraded mode does strictly less, never a guess.** When the precise path is unavailable, the fallback performs only what is safe without it, and reports that it ran. It never produces output that looks like the precise result.
- **Unsupported is not empty.** A file in an unsupported language, or an input that could not be decoded, returns a skipped status or an error. It never returns the same empty result as a supported input with no findings.
- **One bad item does not abort a batch.** Record the failure against the item and carry on; report the count at the end and fail the run if policy says so. For text that is not valid UTF-8, decode lossily and record that you did, or skip it explicitly.
- **A field filled by a later pass says so.** It is an `Option` initialised to `None`, documented with the pass that fills it, and read through an accessor that returns an error, not a default, when still empty. When many fields share the pattern, give the later stage its own type.
- **An intermediate representation documents its producer and consumer, and has a small interpreter.** The interpreter lets lowering be tested by running programs before the back end exists, and remains the reference when the back end is optimised.
- **Versioned formats dispatch on the version first.** The parser reads the header and dispatches; a caller that already knows the version passes it explicitly.
- **Parse complex input into one typed request, and return warnings as data:** `fn parse(input: &str) -> Result<(Request, Vec<Warning>), ParseError>`. A library never prints.
- **Split statements with the tokenizer,** never with `split(';')`, which breaks on a separator inside a string or a comment. Incomplete input asks for more; empty input is handled explicitly.
- **A heavy optional back end is a Cargo feature at a module boundary.** `#[cfg(feature = "...")]` goes on the `mod` line, not on statements scattered inside functions. Every back end implements one trait.
- **Supported output formats are one allow-list,** with the deliberately unsupported ones written down.
- **Syntax queries:** captures name roles shared by every language (`@function.name`, `@definition.function`), not node kinds. Query error and missing nodes too, so a region that failed to parse is visible and not indexed as valid. Embed query text with `include_str!`, and deduplicate matches by kind and byte range, since overlapping patterns match a node twice. A dialect with its own grammar gets its own entry; "close enough" yields silently wrong facts. A file that mixes languages is split into regions before parsing.
- **Chunk source by syntax, not by character window:** a chunk is a whole function, type or impl block, with its identity, its relationships and its text kept as separate metadata.

### Domain packs

The defaults, risks and checks for each kind of work. Details are in the later sections.

| Domain | Default path | Main risks | Verify with |
|---|---|---|---|
| CLI and batch tools | `clap`; typed configuration parsed at startup; `anyhow` in `main`, `thiserror` in the reusable core; `ExitCode`; diagnostics on stderr, data on stdout | Ambiguous exit codes; unbounded memory on large input; output that scripts cannot parse | Golden tests of commands, bad-configuration tests, exit-code tests, a large-input run |
| Back-end services | Transport-to-domain conversion at the edge; typed state; explicit timeouts and retries; `tracing`; a pooled database | Transport types leaking inward; hidden retries; a transaction spanning a remote call; secrets in logs | Handler integration tests, malformed input, timeout and retry tests, transaction-boundary tests |
| Libraries and SDKs | A small curated API; typed errors; no dependency types leaked; doctests; additive features | Public dependency exposure; one giant error enum; re-export sprawl; feature interactions | Doctests, `cargo-semver-checks`, a feature-matrix build, an MSRV build |
| Parsers and protocols | Explicit input and output types; corpus tests; errors with offsets; round-trip properties | A partial parse reported as success; UTF-8 assumptions; panics on bad input; unbounded recursion or allocation | A malformed-input corpus, property tests, a fuzz target |
| Tauri desktop | Owned async commands; explicit managed state; narrow capabilities; typed IPC | Broad permissions; large payloads through JSON IPC; an unowned sidecar process | Command tests, a capability review, sidecar lifecycle tests |
| FFI and unsafe | The smallest safe wrapper over a private unsafe core; explicit ownership and nullability; `#[repr(C)]` | Layout mismatch; aliasing; a panic crossing the boundary; lifetimes the other side does not honour | Ownership-transfer tests, Miri, sanitizers |
| Performance work | A representative benchmark; a profile first; algorithm and allocation before unsafe or lock-free | Optimising the wrong metric; overfitting a microbenchmark; freezing internals into the API | `criterion` before and after, an allocation count, a worst-case input |

**When Rust is the wrong tool.** Say so when it is true: a throwaway script; a prototype whose
only goal is to learn whether an idea works; glue so dynamic that typing the boundary costs
more than the logic; a task where the time is spent outside the process (a slow query, a
remote API), so a faster language changes nothing. If the repository is Rust and the task is
small, write Rust anyway; a second language in a repository has its own cost.

### Tooling and pipeline rules

- **Read back what an external tool actually did.** After starting a tool or service, read the port, path and URL it recorded and check health before using it; do not assume the values you asked for took effect. Give each run its own directory and pin the tool's version.
- **Bound the time of work you do not control.** Parsing an arbitrary file, calling a plugin or running a subprocess gets a deadline, and a timeout is a per-item result, not a crash. A deadline may scale with input size under a named ceiling. On timeout take the unoptimised but correct path; never use a partial result.
- **Bootstrap is idempotent.** Schema and index creation can run on every start, and writes that may repeat are explicit upserts.
- **A downloader streams.** Decompress as bytes arrive, keep URLs and references as typed values, report progress through a channel, verify the checksum, and set the executable bit only after the file is complete.
- **A generator fails or omits the record when an input is unreadable.** The error is a diagnostic; its text is never written into the artefact where content belongs. Every generated file starts with a `@generated` marker, and indexers, formatters and reviewers skip marked, vendored and minified files.
- **A code generator returns its fragments and its shared definitions separately,** and the caller emits each shared definition once.
- **Extra context gets a named entry point over one private worker.** `parse_file(source, lang)` and `parse_path(source, lang, path)` both call a private function taking `Option<&Path>`. Callers never write `None`.
- **A table with two enum keys is one exhaustive `match` on the pair,** with no wildcard arm. Nested string-keyed maps hide a missing combination; the `match` refuses to compile.

```rust
fn query_for(language: Language, kind: QueryKind) -> Option<&'static str> {
    match (language, kind) {
        (Language::Rust, QueryKind::Definitions) => Some(include_str!("queries/rust/definitions.scm")),
        (Language::Tsx, QueryKind::Definitions) => query_for(Language::TypeScript, kind),
        (Language::Rust, QueryKind::Folds) => None,
        // every remaining pair is listed
    }
}
```

- **A partial implementation rejects what it does not support before it starts.** A preflight pass returns a typed error naming the construct, so unsupported input is never half-understood.
- **Resolve an artefact in a fixed order and report which source was used.** A silent fallback location turns "works on my machine" into a mystery.
- **A process-wide cache has a reset,** for tests and for long-running hosts.
- **A finding carries the whole range and a context line.** A start position alone cannot be underlined or deduplicated.
- **A parse result keeps the tree with the bytes it came from** (`struct ParsedFile { tree, source: Arc<[u8]>, .. }`), so a byte range is never applied to a different buffer. Derived facts live in side tables keyed by node ID, so they can be dropped without re-parsing.
- **Extract one direction, derive the other.** Record outgoing references; build the incoming index from them. Two independently extracted directions will disagree.
- **Listings are computed from the registry.** Supported languages and extensions are derived from what is registered, and an ambiguous key (`.h` is C or C++) has a documented default and an override.
- **Say what is not produced.** If a language's support covers definitions but not call edges, the tool reports that per language. "Not supported" must never read as "no callers".
- **A dump is bounded.** Serialising a tree takes options (depth, include text) with no unbounded default.
- **Redact secrets before code leaves the machine,** record what was redacted, and send a chunk again only when its content hash changed.
- **Check proposed identifiers against the index.** Before accepting generated code that names a function or type, look the name up; an unknown name is reported, not assumed.
- **A relaxed format is normalised by a tested pure helper before a strict parse** (strip comments and trailing commas outside strings, then parse JSON).
- **Conversion failures inside a parser are parse errors at their position** (`map_res` in combinator libraries), never panics.
- **A byte classifier is a 256-entry table** built by a `const fn` and indexed by `u8`, so no index can be out of range.
- **One enum variant per kind of parsed thing,** not a tag plus unrelated optional fields. Unknown input is handled by an explicit arm.
- **A streaming decoder is resumable.** It keeps partial state between reads, and a test checks that any chunking of the input gives the same output as one call.
- **Reserved names have a prefix users cannot use** (`__name`), declared as a `pub const` and rejected in user input.
- **Documentation examples are files a test runs,** so a cookbook cannot rot.
- **Do not split a long file into numbered parts joined by `use super::*`.** Split by responsibility into named modules with explicit imports.
- **Two implementations of one thing share a trait, a documented default and a differential test** that compares them over a corpus, with the reference implementation as the oracle.
- **Parallel work items declare the files they modify,** and run concurrently only when those sets are disjoint.
- **An orchestrator's module doc lists its responsibilities,** and gives the reason when work is deliberately sequential, so nobody parallelises it without measuring.
- **Reduce a misparse to the smallest input and read the parser's trace** before changing the grammar. Every declared grammar conflict has a comment and a test input that needs it.

### Last rules for tools that process source

- **Build a line-start index once per file** and binary-search it. Calling `source.lines().collect()` or counting newlines for every symbol is quadratic in the file size.
- **An incremental command says how it detects change and what that can miss.** Modification time plus size is cheap and misses a same-size edit within the timestamp's granularity, so offer a content-hash mode. Do the CPU work in parallel and write from one thread in one transaction. The summary counts what was skipped and why.
- **Limits are a named struct, and every limit is enforced.** `ChunkLimits { max_lines, max_chars, overlap_lines }` replaces three positional numbers of the same type. Construction rejects nonsense (an overlap not smaller than the maximum). A limit that is accepted and never checked is a bug.
- **Unknown input falls back to a named strategy,** such as one whole-file chunk, so nothing is dropped silently. User configuration overrides the built-in table entry by entry.
- **Invented positions use one named constant** (`Span::DUMMY`), never a zero range written inline, so diagnostics can tell real positions from synthesised ones.
- **Wrappers are peeled in one loop into a flat result.** For modifiers, parentheses or reference markers around an inner node, walk inward with an exhaustive `match`, set a flag per wrapper and stop at the innermost name. A new wrapper kind is then a compile error in one place.
- **Copy out of a lending iterator inside the loop.** A streaming cursor's item borrows from the cursor, so use `while let Some(m) = matches.next()` and take what you need before the next step; it cannot be collected.
- **Do not glob re-export enum variants** (`pub use self::Kind::*`); it pollutes the namespace and a later variant can shadow a type. A type with an argument-free `new` also implements `Default`.

## 5. Verification and test-first delivery

### Choose the evidence before writing the code

| Evidence | Choose it when | It does not show |
|---|---|---|
| Unit test | Behaviour is local and deterministic | That the parts work together |
| Integration test | Behaviour crosses a module, process or adapter boundary | Every edge case; too slow for that |
| Doctest | A public example is part of the contract | Anything about error paths, unless written |
| Compile-fail test (`trybuild`) | Misuse must not compile: typestate, `Send` bounds, lifetimes | Run-time behaviour |
| Property test (`proptest`) | An invariant or a round trip matters more than examples | That the stated property is the right one |
| Fuzzing (`cargo-fuzz`) | A parser, decoder or other frontier takes untrusted bytes | Semantic correctness; it finds panics, hangs and whatever you assert |
| `loom` | A small concurrent state machine built on atomics or locks | Anything about async I/O or large systems; the model must be tiny |
| Miri | Unsafe code, aliasing, uninitialised memory | Paths the tests do not execute; no FFI |
| Benchmark | A latency or memory threshold was stated | Production behaviour, unless the input is representative |
| Snapshot test (`insta`) | Output is large and structured: rendered text, plans, diagnostics | Correctness of the first snapshot; a person must read it |

- **Pick the rows at the start and record which ones the change triggers.** A matrix filled in after the code only justifies the evidence that already exists. Formatting, lints, tests and a build can all pass over a parser that was never fuzzed and a lock whose interleavings were never explored.
- **No threshold, no performance claim.** The benchmark row is owed only when a number was stated; without one, do not write "fast" in the report either.
- **Choose the smallest set that covers the risk,** not the largest that can be listed.
- **A missing test is written as missing.** An empty row marked "not covered" is honest; an invented test name is not.
- Coverage is a tool for finding untested code. It is not evidence that the tested code is right, and it is a poor target.

### The test-first loop

```text
STUB -> RED -> GREEN -> REFACTOR -> VERIFY
```

- **STUB.** Write the signature with a `todo!()` body, and the tests against it. At least one test per requirement.
- **RED.** Run it and *read the failure*. The first failure should be the missing behaviour. An unrelated compile error or a panic in the set-up means the test is not yet testing the thing. A test that has never failed has not been shown to test anything.
- **GREEN.** The least code that passes. Resist generalising here.
- **REFACTOR.** Improve names, decomposition and ownership with the tests green. No behaviour change in this step.
- **VERIFY.** Formatting, lints, the full test suite and a build, plus whichever rows from the table the change triggered.

For each requirement, cover three paths: the normal one, the error one, and an edge (empty,
one, maximum, boundary). State the empty case in the requirement itself: no matches is an empty
`Vec`, not an error and not `None`.

**When to apply it strictly, and when not.**

- *Strictly* for a bug fix (the failing test is the reproduction and stays as the regression test), for logic with a clear input-to-output contract, and for anything behind a public API.
- *Loosely* for exploratory work where the interface is not known yet: spike without tests, learn the shape, then throw the spike away or write the tests before it is merged. Do not let a spike become the implementation untested.
- *Not test-first* for pure wiring, generated code and thin adapters; an integration test afterwards covers them better than unit tests written in advance.
- Anti-pattern: writing the implementation, then writing tests that assert whatever it does. Those tests pin the bugs.
- Anti-pattern: changing the assertion to make a failing test pass, without first deciding whether the code or the test was wrong.

**Cheap checks before commit.** Search the added lines of the diff for `TODO`, `FIXME`,
`todo!`, `unimplemented!` and `dbg!`, and the added non-test lines for `.unwrap()` and
`.expect(`. Each hit is either removed or justified.

### The requirement-to-test table

| Requirement | Test | Type | Asserts | Evidence kind |
|---|---|---|---|---|
| REQ-RUST-001.0 | `req_001_rejects_empty_id` | unit | An empty ID returns `IdError::Empty` | correctness |
| REQ-RUST-001.0 | `req_001_persists_and_reloads` | integration | A stored entity reloads equal | integration |
| REQ-RUST-003.0 | `ui/unsealed_state.rs` | compile-fail | Sending before connecting does not compile | misuse |
| REQ-RUST-004.0 | `req_004_round_trip` | property | `decode(encode(x)) == x` | invariant |
| REQ-RUST-005.0 | `req_005_counter_under_contention` | loom | No lost update with two writers | safety |
| REQ-RUST-006.0 | `bench_filter_10k` | benchmark | p99 under 500 µs for 10,000 entities | latency |

- The rows are an example, not a quota. A small change may have two.
- Read the last column top to bottom as a risk profile. All "correctness" and no "safety" on code with shared state is a finding before any code is read.
- *Use the table when* the work has stated requirements or is being reviewed by someone else. *Skip it for* a small fix, where the test name and the commit message carry the same information.

### Test names and shape

Name a test for the behaviour it proves, and include the requirement ID when there is one. The
name should read as a sentence when the test fails.

```rust
#[test]
fn req_001_filter_keeps_only_implementation_entities() {
    let input = mixed_entities();

    let output = filter_implementation_entities(&input);

    assert!(!output.is_empty(), "fixture must contain implementation entities");
    assert!(output.iter().all(Entity::is_implementation));
}
```

- **Guard against the vacuous pass.** `all()` on an empty collection is true. Assert the count or non-emptiness first.
- Arrange, act, assert, with one behaviour per test. Several assertions about one behaviour are fine.
- `test_1`, `it_works` and `test_filter` say nothing when they fail. `filter_returns_empty_for_empty_input` does.

### Skeletons by evidence type

**Async integration.** Return `Result` so set-up can use `?`, and assert on an observable
outcome, not on "it did not error".

```rust
#[tokio::test]
async fn req_001_pipeline_completes_valid_input() -> anyhow::Result<()> {
    let fixture = valid_pipeline_fixture().await?;

    let output = run_pipeline(&fixture).await?;

    assert_eq!(output.status, Status::Completed);
    assert_eq!(output.records.len(), fixture.expected_records);
    Ok(())
}
```

- A test that can hang gets a timeout (`tokio::time::timeout`), so a deadlock fails the run instead of stalling it.
- Tests that depend on time use `#[tokio::test(start_paused = true)]` and advance the clock. Real sleeps make a suite slow and flaky.

**Doctest.** The hidden last line lets the example use `?`.

```rust
/// ```
/// # use my_crate::{UserId, UserIdError};
/// let user_id = UserId::try_from("user_123")?;
/// assert_eq!(user_id.as_str(), "user_123");
/// # Ok::<(), UserIdError>(())
/// ```
```

**Compile-fail.** Each file under `tests/ui/` is one misuse, with its expected error beside it.

```rust
#[test]
fn req_003_misuse_does_not_compile() {
    let cases = trybuild::TestCases::new();
    cases.compile_fail("tests/ui/*.rs");
}
```

- The `.stderr` files change with the compiler version. Pin the toolchain for this test or expect to refresh them on upgrade. For a single small case, a `compile_fail` doctest is lighter.
- Review the expected error once: a file can fail to compile for the wrong reason (a typo, a missing import) and the test still passes.

**Property.** State the property, then let the generator find the counter-example.

```rust
proptest! {
    #[test]
    fn req_004_wire_round_trip(input in valid_entity()) {
        let encoded = encode(&input)?;
        let decoded = decode(&encoded)?;
        prop_assert_eq!(decoded, input);
    }
}
```

- Properties that pay for themselves: a round trip; agreement with a simple reference implementation; idempotence (`f(f(x)) == f(x)`); an invariant kept by every operation; "never panics" on arbitrary bytes.
- Commit the regression file `proptest` writes, and turn each counter-example it finds into a named unit test as well.
- A generator that produces only tidy values proves little. Include empty, maximal, non-ASCII and boundary values.
- Anti-pattern: a property that re-implements the function under test and compares the two copies.

**Concurrency: a stress run is a smoke check, a model is a proof.**

```rust
#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn req_005_no_lost_updates_under_load() -> anyhow::Result<()> {
    let counter = Arc::new(Counter::default());

    let tasks: Vec<_> = (0..100)
        .map(|_| {
            let counter = Arc::clone(&counter);
            tokio::spawn(async move { counter.increment().await })
        })
        .collect();
    for task in tasks {
        task.await??;
    }

    assert_eq!(counter.get().await, 100);
    Ok(())
}
```

- Assert the final state, not only that every task returned `Ok`. One hundred successful tasks and a lost update is exactly the bug.
- The default `#[tokio::test]` runtime is single-threaded; real parallelism needs `flavor = "multi_thread"`.
- This sees only the schedules the runtime happened to choose. Where the order of operations on shared state matters, model it:

```rust
#[cfg(loom)]
#[test]
fn req_005_two_writers_never_lose_an_update() {
    loom::model(|| {
        let counter = loom::sync::Arc::new(Counter::default());
        let other = counter.clone();
        let handle = loom::thread::spawn(move || other.increment());
        counter.increment();
        handle.join().unwrap();
        assert_eq!(counter.get(), 2);
    });
}
```

- `loom` explores every interleaving, so the model must be tiny: two or three threads and a few operations. The code under test must use `loom`'s `sync` and `atomic` types behind a `cfg`, and it runs with `RUSTFLAGS="--cfg loom"`.
- `loom` does not fit code that does real I/O or uses an async runtime. A stress test is the legitimate fallback there; write down that it is a substitute and why.
- A limit stated in a requirement (retries, concurrency, queue depth) has a test that reaches it.
- **Test that nothing is left running.** After shutdown, every spawned task has been joined or aborted. No detached task survives its owner.

**Performance: a threshold in a test is a tripwire, not a measurement.**

```rust
#[test]
#[ignore = "timing; run with: cargo test --release -- --ignored"]
fn req_006_filter_10k_stays_under_budget() {
    let input = entities(10_000);
    let mut samples: Vec<Duration> = (0..200)
        .map(|_| {
            let start = Instant::now();
            std::hint::black_box(filter_implementation_entities(std::hint::black_box(&input)));
            start.elapsed()
        })
        .collect();
    samples.sort();
    let p99 = samples[samples.len() * 99 / 100];
    assert!(p99 < Duration::from_micros(500), "p99 was {p99:?}");
}
```

- `cargo test` builds without optimisation, where a latency number means little. Timing tests run with `--release`, and are `#[ignore]`d from the default run so a loaded CI machine does not fail unrelated work.
- One `Instant` reading is noise. Repeat, discard nothing silently, and assert on a percentile. `black_box` stops the optimiser deleting the work.
- For a real measurement or a comparison of two versions use `criterion`; for CI gating that must not flake, count instructions (`iai-callgrind`) or allocations instead of wall-clock time.
- **A performance claim has four parts:** the current value, the target, the percentile and the population ("from 5 ms to under 1 ms at p99 for 10,000 entities"). A new system with no current value still states percentile and population.

**Layout claims as tests.** When a size or an identity is part of the design (a cache-line
budget, an interning guarantee, a niche-optimised `Option`), pin it.

```rust
#[test]
fn node_layout_stays_within_budget() {
    assert!(std::mem::size_of::<Node>() <= 64, "Node must fit one cache line");
    assert_eq!(std::mem::size_of::<Option<NodeId>>(), std::mem::size_of::<NodeId>());
}

#[test]
fn interning_returns_the_same_allocation() {
    let a = Interned::new("common_name");
    let b = Interned::new("common_name");
    assert!(std::ptr::eq(a.as_str(), b.as_str()));
}
```

- Prefer an upper bound (`<=`) to an exact size unless the exact size is the contract (FFI, an on-disk format). Exact sizes differ between 32-bit and 64-bit targets and may change with the compiler for `repr(Rust)` types.
- For a hard guarantee, check at compile time: `const _: () = assert!(std::mem::size_of::<Node>() <= 64);`.
- *Skip* for types whose size nobody depends on; the test then only blocks harmless refactors.

**Mixed readers and writers, with a final consistency check.** `JoinSet` owns the tasks, so a
panic in any of them surfaces and none outlives the test.

```rust
#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn concurrent_reads_and_writes_keep_the_store_consistent() {
    let store = Arc::new(Store::new().await);
    let mut tasks = JoinSet::new();

    for writer in 0..10 {
        let store = Arc::clone(&store);
        tasks.spawn(async move {
            for n in 0..100 {
                store.add(node(writer * 100 + n)).await.unwrap();
            }
        });
    }
    for _ in 0..20 {
        let store = Arc::clone(&store);
        tasks.spawn(async move {
            for _ in 0..50 {
                let _ = store.get_any().await;
            }
        });
    }

    while let Some(joined) = tasks.join_next().await {
        joined.unwrap(); // a panicked task fails the test
    }
    assert_eq!(store.count().await.unwrap(), 1_000);
}
```

- The final count is the assertion that matters. Stronger still: assert the exact set of IDs, which also catches a duplicate hiding a loss.
- Give readers something to check too (every value they see is complete and valid), or they only add load.

**A validation property states the rule independently.**

```rust
proptest! {
    #[test]
    fn content_validation_matches_the_rule(content in ".*", max_len in 1usize..10_000) {
        let accepted = validate_content(&content, max_len).is_ok();
        let expected = !content.trim().is_empty() && content.len() <= max_len;
        prop_assert_eq!(accepted, expected);
    }
}
```

- This is useful when the rule is simpler to state than the implementation is to write. When the "expected" line is a copy of the implementation, the test proves nothing; write example tests at the boundaries instead (empty, whitespace only, exactly `max_len`, one over).
- Decide and state what a length means: bytes (`len()`), `char`s, or grapheme clusters. They differ for non-ASCII text, and the generator `".*"` will find the difference.

**Skeletons freeze library shapes.** `#[tokio::test]`, `trybuild`, `proptest!` and
`loom::model` are written against particular crate versions. Compile a copied skeleton against
the project's own versions before building on it, and if it fails, suspect a changed crate API
before your own code.

### More kinds of evidence

**Fuzzing, for anything that takes bytes from outside.**

```rust
#![no_main]
use libfuzzer_sys::fuzz_target;

fuzz_target!(|data: &[u8]| {
    if let Ok(value) = my_crate::parse(data) {
        // Not only "does not panic": what parsed must survive a round trip.
        let again = my_crate::parse(&value.to_bytes()).expect("re-parse of own output");
        assert_eq!(value, again);
    }
});
```

- A target that only ignores the result finds panics, overflows (in debug) and hangs. Add an assertion and it finds logic errors: a round trip, agreement with a reference implementation, an invariant on the output.
- Seed the corpus with real inputs, and keep it. Every crash becomes a checked-in regression test with the minimised input.
- For structured input derive `arbitrary::Arbitrary` instead of hand-decoding bytes.
- Run it with a time limit on a schedule, not on every push. Set a per-input timeout and a memory limit so a hang or an allocation bomb is reported as a finding.
- *Use for* parsers, decoders, decompressors, protocol state machines, and unsafe code reachable from input. *Skip for* code whose input is already a validated domain type.

**Snapshots, where the whole text is the contract.**

```rust
use expect_test::expect;

#[test]
fn renders_a_two_node_graph() {
    let got = render(&two_node_graph());
    expect![[r#"
        digraph {
          a -> b
        }
    "#]]
    .assert_eq(&got);
}
```

- Good for parsers, formatters, diagnostics, plans and macro expansion. `expect-test` keeps the text inline and updates with `UPDATE_EXPECT=1`; `insta` keeps files and has a review command.
- **A snapshot nobody reads is not a test.** Keep each one small enough to review in a diff, and read the diff on every update. An update accepted blindly records the bug as the expected output.
- Remove what varies before comparing: timestamps, temporary paths, addresses, map order, durations.
- Anti-pattern: one huge snapshot of a whole response where three fields matter. Assert the three fields.

**Mutation testing asks whether the tests would notice a bug.** `cargo-mutants` changes the
code (flips a comparison, replaces a return value) and reports each change no test caught.

- A survivor is usually a missing boundary case. For a length check from 2 to 100, the tests need 1, 2, 100 and 101, not only "empty" and "valid".
- Run it on a module that matters (validation, money, authorisation, parsing), not on the whole workspace on every push; it is slow.
- Not every survivor is worth killing. Equivalent mutants and changes to log text are noise.

**Test infrastructure serves the failure, not the pass.** A suite is as fast as its slowest
diagnosis.

- Each test gets its own temporary directory (`tempfile::tempdir()`), its own port (bind to port 0 and read it back) and its own data. Tests run in parallel and in any order; shared state between them is where flakiness comes from.
- A failing assertion shows both values and enough context to act on: `assert_eq!(got, want, "for input {input:?}")`. Use a diffing assertion (`pretty_assertions`, `similar-asserts`) for multi-line values.
- No test depends on the working directory, the wall clock, the locale, the network or an environment variable set elsewhere. Inject them. A test that needs an external service is `#[ignore]`d or feature-gated, with the command to run it written beside it.
- **A flaky test is a bug with a cause.** Find it (a race, a real sleep, shared state, an unordered map) before reaching for a retry. Retry only an operation known to be flaky in the operating system, and say which.
- Table-driven tests keep many cases cheap; make each case name itself in the failure message.

### Documentation that is checked

Every public item that can fail, panic or be misused says so. An undocumented panic or unsafe
precondition is a defect.

```rust
/// Parses a port from text.
///
/// # Errors
/// Returns [`PortError::NotANumber`] if `text` is not a decimal integer, and
/// [`PortError::OutOfRange`] if it is zero or above 65535.
///
/// # Examples
/// ```
/// # use my_crate::parse_port;
/// assert_eq!(parse_port("8080")?.get(), 8080);
/// assert!(parse_port("0").is_err());
/// # Ok::<(), my_crate::PortError>(())
/// ```
pub fn parse_port(text: &str) -> Result<Port, PortError> { /* ... */ }
```

- `# Errors` names the variants and their conditions; "returns an error if something goes wrong" documents nothing. `# Panics` lists every condition, or the function does not panic. `# Safety` on an `unsafe fn` lists what the caller must guarantee.
- A doctest asserts something. An example that only calls the function checks that it compiles and nothing else.
- Show the error case in the example when the error is part of what a caller must handle.
- Keep doctests small; each is compiled as its own crate, so hundreds of them slow the suite. Long scenarios belong in `tests/`.
- Use `no_run` for examples that need a network or a device (still compiled), and avoid `ignore`, which checks nothing.
- In compile-fail tests, do not depend on exact compiler wording more than the tool forces you to; the message changes between releases.

### Test design patterns

**One conformance suite for many implementations.** Separate "run this back end" from "check
this behaviour". The suite is generic; each implementation is one line.

```rust
pub trait RankBackend {
    fn run(&self, graph: &Graph, params: &Params) -> Output;
}

pub fn conformance_suite<B: RankBackend>(backend: &B) {
    for case in fixtures() {
        let got = backend.run(&case.graph, &case.params);
        assert_close(&got, &case.expected, case.tolerance, &case.name);
    }
}
```

- The expected output is captured independently of every implementation (by hand, or from a trusted reference), or the suite only checks that the code agrees with itself.
- Floating-point comparison needs a stated tolerance: absolute near zero, relative elsewhere. A purely relative tolerance fails against an expected zero.
- Write the suite and its fixtures before the second implementation.
- A fixture loader reports the line number and the offending token on bad input.

**Assert what makes an answer valid, not one valid answer.** When several outputs are correct
(a topological order, a set returned in any order), a golden value makes the test fail on a
harmless change.

```rust
let order = graph.topological_order().unwrap();
let position = |node| order.iter().position(|&n| n == node).unwrap();
for (dependency, dependant) in graph.edges() {
    assert!(position(dependency) < position(dependant));
}
assert_eq!(order.len(), graph.node_count());
assert!(matches!(cyclic.topological_order(), Err(SortError::Cycle { .. })));
```

- Keep cases for empty, single, disconnected, cyclic and several-valid-answers inputs. Generate graph families with `proptest`; fixed fixtures miss classes of input.
- If the output must be deterministic (it is shown to users, or diffed), say so and test the exact order. That is a different requirement.

**Optimised and unoptimised paths agree.** Every optimisation, cache or fast path has a test
that runs the same input with it on and off and compares results. This is the cheapest oracle
there is, and it needs the switch to exist.

**Record at the transport, replay in the production shape.** A recorded exchange is replayed
as the same async type the code consumes, so streaming clients are tested without a network.

```rust
#[derive(Serialize, Deserialize)]
pub struct RecordedResponse {
    pub status: u16,
    pub headers: Vec<(String, String)>,
    pub body_chunks: Vec<String>,
}

impl RecordedResponse {
    pub fn into_byte_stream(self) -> BoxStream<'static, io::Result<Bytes>> {
        stream::iter(self.body_chunks.into_iter().map(|c| Ok(Bytes::from(c)))).boxed()
    }
}
```

- Keep the chunk boundaries. A parser that works on whole bodies and fails when an event is split across two chunks is the bug this finds; add a case that splits at an awkward place on purpose.
- Playback is the default; recording needs an explicit mode.
- **Recordings leak secrets.** Redact tokens and cookies when recording, and check the redaction before the file is committed.
- A recording goes stale when the remote API changes. Note when it was taken, and re-record on a schedule or when the client changes.
- For a small non-streaming response, a plain JSON fixture is enough.

**One default test configuration, small overrides.** Build one production-like default, and
let each test change only what it is about.

```rust
let config = TestConfig { replicas: 3, ..TestConfig::default() };
let table = test_table(|config| config.replicas = 3);
```

- The override is the documentation: a reader sees which setting the test depends on. Copying the whole builder chain into each test hides that.
- Fixture builders return new values (`with_x(self) -> Self`), so one case cannot contaminate the next.

**Registration is tested, because compiling does not prove coverage.** When handlers are wired
to an enum of operations at run time, a test iterates the enum (`strum::IntoEnumIterator`, or
an `ALL` constant) and asserts that each has a handler. Prefer an exhaustive `match` where it
is possible; then the compiler does this.

**Smaller rules.**

- **Fixtures keep input and expected output together,** as files a person can diff. For a behaviour change, add the smallest new fixture first, then change the code until the new output is what you intend.
- **Real infrastructure in tests is disposable and configured the production way.** A container's connection details go through the same configuration path the application uses, so the test exercises that path too.
- **A suppressed failure still fails the run.** A harness that records failures and continues must assert overall success at the end. Do not continue where the first failure invalidates the rest.
- **A benchmarked kernel has a verifier,** called outside the timed region. A fast wrong answer is the usual result of optimising without one.
- **Deterministic checks come before model-based ones.** For generated or AI-assisted output, check what needs no judgement first (required keys, forbidden combinations, it parses, it compiles), then the semantic check, and report both.
- **A scoped override of global state restores in reverse order,** through a guard. It protects the mutation, not concurrent readers, so tests that touch process-global state (environment variables, the current directory) must not run in parallel with each other. Better: inject the value and have no global.
- **A conformance scenario has four parts:** initial state, input, expected result or error class, and expected side effects, including "none". A change in semantics updates the specification and the scenarios together.
- **A test DSL keeps the line number** on every parsed line, and every error points at it.
- **Query text in template files** is three layers: the text, extraction of values, and one converter that owns quoting. User-controlled values always go through bound parameters, never substitution. A test prepares every template and fails on an unreplaced placeholder.
- **A lifetime contract gets a compile-fail test:** if a wrapper must not outlive its parent, a case that tries must fail to compile.
- **A regression test for a UI bug** uses the smallest fixture that reproduces the state change, and selects elements by stable test IDs, not by styling.

### Harnesses, fakes and failure injection

**A snapshot matrix generated from fixtures.** For compilers, formatters, renderers and
migrations, generate one test per fixture file and back end with a custom harness
(`harness = false` in `Cargo.toml`, `libtest-mimic` for the trials).

```rust
fn build_trials() -> Vec<Trial> {
    let mut trials = Vec::new();
    for case in collect_cases("tests/fixtures") {
        for backend in Backend::ALL {
            let case = case.clone();
            let name = format!("{}::{}", backend.name(), case.name);
            let trial = Trial::test(name, move || run_case(&case, *backend));
            trials.push(trial.with_ignored_flag(case.skip_reason.is_some()));
        }
    }
    trials
}
```

- Each trial has a specific name, so one failure can be run alone with a filter. A skipped case is marked ignored with its reason; it does not silently vanish.
- Adding support for a construct is then adding one named fixture.
- For security-sensitive or numeric behaviour, assert the property directly as well. A snapshot is too easy to accept.

**One recording fake tests every layer.** A fake inner implementation records calls and injects
errors on demand. Each wrapper (retry, timeout, metrics, cache) is tested against it for five
things: untouched operations are forwarded, the retry count is exact, a timeout cancels the
inner call, the metric is emitted once, and the inner error survives intact.

**Reference implementations and injected failures, for storage and anything stateful.**

- **A verification adapter** runs a simple, slow, obviously correct implementation (a `BTreeMap`) beside the real one and compares every result. Under a property test or a fuzzer generating operation sequences, it finds what example tests do not.
- **Failures are injected at named points:** an I/O error on the nth write, a crash before and after each flush. After each, reopen and check that the state is one of the allowed ones (the old value or the new one, never a mixture).
- **A write-restart-read test** exists for anything that claims durability.
- **A panic in a caller-supplied closure must not leave half a mutation.** Either the transaction is rolled back or the handle is poisoned and the next commit fails. Test it by panicking inside the closure and reading the earlier data back.
- **Adapters agree on failures.** A conformance test checks that every provider adapter maps authentication, not-found, conflict and retryable errors to the same domain errors.

**A real-socket harness, only when one is needed.**

- If calling the router as a service in-process is enough (`tower::ServiceExt::oneshot`), do that; it is faster and has no ports to manage.
- When a real listener is needed, a harness behind a `test-support` feature owns the temporary storage, binds port 0, starts the server, and reports the bound address. Its `Drop` signals shutdown and joins the thread, so no server outlives its test.
- **Functions that probe the outside world take the probe as a parameter** (an `exists` closure, an environment lookup), so their logic is tested without a real file system or environment.
- **A loader for plugins is tested with built fixtures:** small crates generated in a temporary directory, a sanitised environment so nothing leaks from the developer's shell, the real binary run, and its output asserted. Cases: a duplicate name, missing metadata, an explicit override.

**Honest results.**

- **An unimplemented check must not look like a clean result.** A detector or rule whose body is a stub returns "not implemented" or is left out of the registry. A stub returning an empty list is indistinguishable from "no findings": a missing feature becomes a false all-clear. Test that every registered check fires on a fixture built to trigger it.
- **A reported crash becomes a fixture.** The smallest input from the bug report is committed with the issue reference, so that recovery on that malformed input stays tested.
- **One fixture per feature,** named after what it exercises. Coverage is then counted in features handled, not files processed.
- **A quality benchmark names its ground truth:** one primary measure, an independent source of truth, and a dataset version reported with every result. Every tool compared runs through the same adapter.
- **Scenario tests keep state in a typed struct** with named fields, not a string-keyed bag. *Skip the scenario layer* when plain unit tests say the same thing.

### What to test, by risk

| Risk surface | Evidence |
|---|---|
| Pure logic | Unit tests, plus a property where there is an invariant |
| Public API contract | Unit tests, doctests, misuse cases |
| Persistence or I/O | Integration tests against the real thing, write-restart-read |
| Async orchestration | Integration tests with timeout, cancellation and shutdown cases |
| Shared mutable state | A stress test, and `loom` where the ordering is subtle |
| Parsing or protocol | A corpus, malformed input, a property test, a fuzz target |
| Compile-time misuse | Compile-fail tests |
| A performance claim | A benchmark with a threshold |
| Unsafe or FFI | A harness, Miri, sanitizers |

- **A bug fix has a test that was seen to fail.** Reproduce the bug, write the test, watch it fail on the broken code, fix, watch it and the wider suite pass. Do not report a regression test that was never observed failing.
- **Differential tests** are the cheapest strong evidence when an old and a new implementation, or a simple and a fast one, can check each other.
- **Adversarial inputs at every edge:** malformed, truncated, huge, deeply nested, non-UTF-8. Not only the well-formed cases.
- **In a long session, checkpoint the state:** which step of the loop you are in, the tests failing right now, the files touched, the open questions. A checkpoint guards against drift; it does not replace running the tests again.

### Fixtures and helpers

- **Fixture paths start from `env!("CARGO_MANIFEST_DIR")`,** so the test does not depend on the working directory.
- **Helpers that can fail are `#[track_caller]` and name the path,** so the panic points at the test, and a missing fixture cannot look like a parse failure.

```rust
#[track_caller]
fn read_fixture(rel: &str) -> String {
    let path = Path::new(env!("CARGO_MANIFEST_DIR")).join("tests/fixtures").join(rel);
    fs::read_to_string(&path).unwrap_or_else(|e| panic!("fixture {}: {e}", path.display()))
}
```

- **Path tests use awkward paths:** spaces, non-ASCII characters, a trailing separator, a relative path, a symlink. Plain alphanumeric names hide quoting and normalisation bugs.
- **Tests for an optional feature are gated** with `#[cfg(feature = "...")]` so the default run stays green, and CI runs the feature matrix. A gated test that CI never enables is not a test.
- **Start an out-parameter at the wrong value.** If a function writes through `&mut`, initialise the target to something other than the expected result, so a function that writes nothing cannot pass.
- **A streaming parser is tested for chunking equivalence:** the whole input in one call and one byte at a time must give the same events. A property test checks it at random split points.
- **Check the representation before the value** when a type has several (borrowed or owned, sparse or dense, inline or heap). Otherwise a test passes because the value silently fell back to the slow form.
- **Prove the fast path was taken.** A test that an asset is embedded, a cache is hit or an index is used asserts that directly (a fetch counter of zero, an offline run, a query plan), not only that the answer is right.
- **Every member of a closed set is exercised.** A test iterates `Language::ALL` (or the equivalent) and loads each one.
- **When one datum appears in two places in a response, read each event kind from exactly one,** and test that the other place produces nothing. Reading both emits duplicates.
- **An embeddable component has a test constructor** (`build_for_testing()`) that owns its temporary storage, so tests do not repeat the set-up.
- **Expose internals to a fuzz crate through one dedicated module,** not by making them public.

- **A contract test pins what you rely on in a dependency.** If the code depends on names, shapes or behaviour another component may change (node kinds of a grammar, fields of an API response), one test asserts exactly those, so an upgrade fails there instead of silently changing output.
- **A bucketing function is tested by conservation:** the bucket counts sum to the number of in-range inputs, for one bucket and for many, with a value on each edge and one outside. The doc states whether the upper edge is inclusive.
- **Generated tests are reviewed and cut like hand-written ones.** One behaviour per test, named in the test name. Delete tests that only mirror the implementation's steps; they fail on every refactor and catch nothing.

## 6. Types and API design

The aim: a caller who has not read the implementation uses the API correctly, and the wrong
use does not compile or returns an error that says what to do.

### Core patterns

Each with when it pays and when it does not.

- **Accept borrowed inputs.** `&str`, `&[T]` and `&Path`, not `&String`, `&Vec<T>` and `&PathBuf`. The API then commits to meaning, not to a container. *When the function stores the value,* take it owned (`String`, or `impl Into<String>`) so the caller who already owns one does not pay for a clone. `impl AsRef<Path>` is right for path arguments; `impl AsRef<str>` everywhere is noise and bloats code through monomorphisation.
- **Newtypes, and parse instead of validating.** Turn raw data plus repeated checks into a type that can only hold a valid value. IDs, units, offsets, validated strings and handles stop being interchangeable primitives. *Skip when* the wrapper carries no invariant and no distinction anyone could confuse; a newtype around every `String` is ceremony.

```rust
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct Email(String);

impl Email {
    pub fn parse(raw: &str) -> Result<Self, EmailError> {
        let trimmed = raw.trim();
        if trimmed.is_empty() {
            return Err(EmailError::Empty);
        }
        if !trimmed.contains('@') {
            return Err(EmailError::MissingAt);
        }
        Ok(Self(trimmed.to_owned()))
    }
    pub fn as_str(&self) -> &str { &self.0 }
}
```

  Keep the field private and offer no constructor that skips the check, or the guarantee is gone. That includes `Deserialize`: derive it through `#[serde(try_from = "String")]`, not on the raw field. Do not implement `DerefMut` or hand out `&mut` to the inner value.
- **`From` for conversions that cannot fail, `TryFrom` for those that can.** *Use a named constructor instead* when the operation does real work, loses information or has more than one sensible meaning. `From` must be cheap and unsurprising, because `?` and `.into()` call it invisibly.
- **Combinators for straight-line flows, `match` for branching.** `map`, `and_then`, `ok_or_else` and `transpose` keep a linear transformation linear. When there are several arms with different work, or a chain of four closures, a `match` or `let ... else` reads better.
- **Generics or `dyn`, chosen on purpose.** Generics for hot paths and when the caller knows the type. `dyn Trait` for heterogeneous collections, plugin points, and to keep compile time and code size down. For a call that does I/O, the virtual call is immeasurable; do not make a service generic over five type parameters to avoid it.
- **Return `impl Iterator` to stay lazy** and hide adapter types. Use `Box<dyn Iterator>` when branches return different iterator types or the type must be stored in a struct field without a generic parameter. Return a `Vec` when the caller always needs all of it and the size is bounded.
- **A named enum over a boolean or a sentinel.** A `bool` says something happened; an enum says what the caller must do next. `enum Inserted { New, Replaced(Old) }` beats `true`; `Option<usize>` beats `-1`. *A `bool` is fine* for a real yes-or-no question (`is_empty`).
- **A flat public facade with `pub use`.** Internal file layout and public paths are separate decisions; re-exports let internals move without breaking callers. Re-export deliberately, item by item. Do not re-export a dependency's types unless they are part of your contract, because then its version is too.
- **Blanket impls for `&T`, `&mut T` and `Box<T>`** make a trait usable through references and boxes without wrappers. Add them when the trait is naturally delegating and its methods take `&self`.
- **Omitted is not the same as explicitly empty.** For a partial update, "not provided" and "set to nothing" are different inputs:

```rust
pub enum Patch<T> {
    Keep,
    Clear,
    Set(T),
}
```

  `Option<Option<T>>` works with serde but is hard to read; the enum is clearer in domain code. Never use a magic value from the domain (an empty string, zero) to mean either.
- **Name the unit of an offset.** Bytes, `char`s and UTF-16 code units are different numbers for the same position. Put the unit in the type (`ByteOffset`, `Utf16Offset`) wherever offsets cross a boundary, and test on multi-byte text.
- **Strategies are named for the guarantee they give.** An operational choice is a named type behind a small trait, not a hidden boolean, and its documentation says what it does *not* preserve:

```rust
pub trait Sharding: Send + Sync {
    fn pick_shard(&self, shard_count: usize, key: &Key) -> usize;
}
pub struct Balanced { next: AtomicUsize } // spreads load; does not keep per-key order
pub struct Ordered;                       // keeps per-key order; load may skew
```

  Offer no alternatives where correctness needs one behaviour.

### Type-level techniques

Stronger tools. Each costs readability and compile-error quality, so each needs a reason.

**Typestate, for a protocol that is wrong when used out of order.**

```rust
pub struct Request<State> {
    parts: Parts,
    _state: PhantomData<State>,
}
pub struct NoBody;
pub struct HasBody;

impl Request<NoBody> {
    pub fn body(self, bytes: Vec<u8>) -> Request<HasBody> { /* ... */ }
}
impl Request<HasBody> {
    pub fn send(self) -> Result<Response, SendError> { /* ... */ }
}
```

- `send` does not exist on `Request<NoBody>`, so the mistake is a compile error, and consuming `self` stops the old state being reused.
- *Use for* builders with required steps, connections (connected, authenticated), transactions, and resources that must be finalised.
- *Skip when* the state is chosen at run time (then it is an enum and a `match`), when there are more than a handful of states (the types multiply), or when the object must be stored in a collection with others in different states.
- **A must-complete object can carry a drop bomb:** `Drop` does `debug_assert!` that it was finished or explicitly abandoned. Keep it to debug builds, and never panic in `Drop` while already unwinding (check `std::thread::panicking()`), or the process aborts.

**Phantom-typed handles bind a name to its types.**

```rust
pub struct Table<K, V> {
    name: &'static str,
    _types: PhantomData<fn() -> (K, V)>,
}

impl<K, V> Table<K, V> {
    pub const fn new(name: &'static str) -> Self {
        assert!(!name.is_empty());
        Self { name, _types: PhantomData }
    }
}

pub const USERS: Table<u64, String> = Table::new("users");
```

- Code passes `USERS`, never the string `"users"`, so the key and value types cannot be mismatched at a call site.
- `PhantomData<fn() -> T>` says "produces `T`, owns none": the handle stays `Send`, `Sync` and `Copy` regardless of `T`, and drop-check is not affected. `PhantomData<T>` claims ownership of a `T`, which is rarely what a handle means. For a handle whose parameter must not be coerced at all (invariance), use `PhantomData<fn(T) -> T>`.
- *Not for* schemas defined by users at run time; those need validation, not types.

**Queries as a typed tree, not a string.**

```rust
pub enum Query {
    AllVertices,
    Edges(EdgeQuery),
    Pipe(Box<Query>, Direction),
    Count(Box<Query>),
}
```

- Callers compose values; an invalid composition fails at construction; execution is one interpreter with an exhaustive `match`. There is no injection, because there is no string.
- *Not when* users need an open textual language. Then parse the text into this tree and keep the rest.

### Boundary types

**Normalise once at a security boundary.** Parse and normalise into a named type; every policy
check, comparison and audit line then uses that type, never the raw string. Two code paths
that normalise differently are how allow-lists get bypassed.

```rust
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct Host(String);

impl Host {
    pub fn parse(input: &str) -> Result<Self, HostError> {
        let normalised = normalise_host(input)?; // lower-case, strip trailing dot, unbracket IPv6
        if normalised.is_empty() {
            return Err(HostError::Empty);
        }
        Ok(Self(normalised))
    }
}

pub enum NetworkDecision {
    Allow,
    Deny { reason: DenyReason, source: PolicySource },
}
```

- A denial carries its reason and which rule produced it. "Denied" alone cannot be debugged or audited.
- Keep the raw input beside the parsed value only when diagnostics need it, and never compare on it.
- Write the tests for odd inputs first: bracketed IPv6, a trailing dot, an embedded port, mixed case, an internationalised name, a wildcard, the empty string.
- The same rule applies to paths (canonicalise, then check the root), URLs and identifiers used in access checks.

**Capability arguments for dangerous operations.** Running a process, opening the network,
writing outside a root: require a token in the signature that only trusted code can create.

```rust
pub struct ExecCap(()); // private field: constructed only in one trusted module

pub fn run_tool(_cap: &ExecCap, program: &Path, args: &[OsString]) -> io::Result<Output> {
    std::process::Command::new(program).args(args).output()
}
```

- The signature now shows which functions can spawn processes, and a reviewer can follow the token.
- **Back it with a lint, or it is only a convention.** In `clippy.toml`: `disallowed-methods = ["std::process::Command::new", "std::env::set_var"]`, with `#[allow]` in the wrapper module alone.
- This is a tool for auditability inside one code base. It is not a sandbox: it does not constrain dependencies or unsafe code.
- *Skip when* the program is small enough that the dangerous calls are all visible in one file.

**Opaque text offsets and ranges.** Parsers, editors and diagnostics pass a named offset and
range, never a bare `usize`.

```rust
#[derive(Clone, Copy, Default, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct TextSize(u32); // a byte offset

#[derive(Clone, Copy, PartialEq, Eq, Hash)]
pub struct TextRange {
    start: TextSize,
    end: TextSize, // private: the constructor checks start <= end
}
```

- `u32` halves the size of every span and caps a file at 4 GiB, so conversion from `usize` is `TryFrom`, not `as`.
- Offsets into `str` must fall on character boundaries; slicing at any other offset panics. Check with `is_char_boundary` wherever an offset arrives from outside.

**Unit-bearing values are parsed once, at the edge.** Sizes such as `10MB`, durations, rates
and percentages become a domain type in the argument parser (a `clap` `value_parser` returning
`ByteSize` or `Duration`); nothing downstream parses units again.

- State the suffix policy: `KB` is 10^3 and `KiB` is 2^10, or say which you chose.
- An unknown suffix is an error that quotes the input. Multiplication is checked for overflow.
- Test a bare number, each suffix, upper and lower case, a fractional value, a negative value and rubbish.

**A join states what was missing.** A view that joins stored records with live state marks
each joined part: `enum Joined<T> { Present(T), Missing }`, or simply `Option<T>` with a
documented meaning. Never a `bool` beside an `Option`; the two can disagree.

### Builders

Use a builder when construction has many optional settings, or when validity depends on
several fields together. For two or three required fields, a `new` function is clearer.

```rust
pub struct ServerBuilder {
    addr: SocketAddr,
    workers: Option<usize>,
    tls: Option<TlsConfig>,
}

impl ServerBuilder {
    pub fn new(addr: SocketAddr) -> Self {
        Self { addr, workers: None, tls: None }
    }
    #[must_use]
    pub fn workers(mut self, workers: usize) -> Self {
        self.workers = Some(workers);
        self
    }
    pub fn build(self) -> Result<Server, BuildError> {
        let workers = self.workers.unwrap_or_else(default_workers);
        if workers == 0 {
            return Err(BuildError::ZeroWorkers);
        }
        Ok(Server { addr: self.addr, workers, tls: self.tls })
    }
}
```

- **Required inputs go in `new`; options go in setters.** A builder whose `build()` fails because a required field was never set has moved a compile error to run time.
- **`build()` is the one validation boundary.** It rejects incompatible combinations with an error naming both options. Tests call `build()`; they do not inspect the builder's fields.
- **Defaults are applied in one place** (`build` or `Default`), and documented.
- Consuming setters (`self -> Self`) chain cleanly; `&mut self -> &mut Self` suits builders configured in loops or conditionals. Pick one per builder.
- **A deferred error keeps the chain intact.** A setter that can fail may record the first error in the builder and return `self`; `build()` starts by returning it. *Not when* the caller needs to react at the failing call.
- **A builder that tracks a "current" item** (the current group, the current subject) documents which methods set and reset it, and returns an error when a method needs context that is absent.
- A new option touches the field, the setter, the default, the validation and a test, together.
- Use typestate only when a step is required *and* must come in order; otherwise it is weight without benefit.
- **Make a choice visible at the call site.** When an argument affects correctness or layout (row-major or column-major, inclusive or exclusive), take a small named type, not a tuple or `true`.

### Smaller API rules

- **Lazy values are `#[must_use]`** with a message saying they do nothing until consumed. So are builders and guards. `Result` already is.
- **Commands as data.** For a protocol with many commands, write one descriptor per command (its code, how to encode the request, how to decode the response) and one generic executor. A new command is a descriptor and a round-trip test, not new transport code.
- **Variants as a table of typed specs.** When variants differ only in data (names, extensions, flags), keep one table and a generic engine. Move a variant into code only when its control flow really differs.
- **A validated resource issues its children.** A checked directory, session or connection hands out child handles through its own methods; callers do not open things beside it.
- **Extension points are explicit.** A hook is registered by name and type, never inferred from a naming pattern. Hook order is part of the contract: document and test it. A plugin gets a registry narrowed to its own namespace.
- **Selection is not traversal.** A selector value (all, one, a range, neighbours) describes a subset without the data; a method applies it to a collection and returns an iterator. Common selections then allocate nothing.
- **An extension trait separates required from optional.** A few required methods; the rest have default implementations in terms of them, which an implementer may override for speed. Test that an override agrees with the default.
- **A mutating business action is one unit:** validate, run in one transaction, fail with a typed error. Transport handlers stay thin. Do not turn every helper into a command object.
- **A deep deserialisation error reads as a path** from root to leaf (`serde_path_to_error`). Bound the size of any input fragment quoted in a message.
- **A small language is a long-term promise** about syntax and error text. Prefer existing structured selectors; if a DSL is needed, the parser, the printer and a `parse(print(x)) == x` test change together.

### Traits as seams

**Absent behaviour is an implementation, not an `Option`.** "No hook installed" is a no-op
implementation, so call sites do not branch.

```rust
pub trait RegistryHooks: Send + Sync {
    fn on_manifest_uploaded(&self, _reference: &ManifestRef) {}
    fn on_blob_deleted(&self, _digest: &Digest) {}
}

impl RegistryHooks for () {}

let hooks: Box<dyn RegistryHooks> = builder.hooks.take().unwrap_or_else(|| Box::new(()));
```

- Default method bodies mean a new hook does not break existing implementers.
- Document where each hook is called, in what order, and whether its failure is ignored or aborts the operation.
- **A silent no-op hides missing wiring,** so the wiring itself has a test: install a recording hook and assert it was called.
- *Not for* a step that must be confirmed, retried or rolled back with the core operation. That is part of the operation, not a hook.
- With many optional callbacks and one author composing a few, a builder holding one boxed closure per hook is lighter than a trait. With one required callback, a trait is clearer.

**A family of related types goes through associated types tied back to `Self`,** so the
handles and events of one back end cannot be mixed with another's.

```rust
pub trait Runtime: Sized + 'static {
    type Handle: RuntimeHandle<Runtime = Self>;
    type Window: WindowDispatch<Runtime = Self>;

    fn new(args: InitArgs) -> Result<Self, RuntimeError>;
    fn handle(&self) -> Self::Handle;
}
```

- Extending the trait changes the trait, the mock back end and every real back end in the same commit.
- An API heavy in associated types needs a worked example of the common path; the signatures alone are hard to read.
- **One back end does not need the trait.** Add it with the second implementation, or with the mock if tests need one.

**A behavioural trait needs semantic tests.** Implementing the methods does not prove they
agree with each other. Test the laws that relate them: `a == b` implies equal hashes; `len`
equals the number of items iterated; `Ord` is consistent with `Eq`; `decode(encode(x)) == x`.
Write these once as a generic function and run it for every implementer.

**Smaller rules.**

- **A checked constructor's error quotes both sides of the mismatch:** "expected 4 columns, row has 3", not "column count mismatch".
- **A scalar-or-collection argument** is a small trait that reports which it is, not a second copy of every entry point. Keep separate functions when the two differ in meaning, and test collection-collection, collection-scalar and scalar-scalar.
- **Extract and repack.** An API that processes some leaves of a nested container returns the caller's own shape, by splitting the walk into an extract phase and a repack phase.

### Text, positions and source

**A node travels with its source.** When every operation on a syntax node needs the original
text, pass a wrapper holding both; children are derived with the same source, so a node and
its text cannot drift apart.

```rust
#[derive(Clone, Copy)]
pub struct NodeWithSource<'a> {
    pub node: Node<'a>,
    pub source: &'a str,
}

impl<'a> NodeWithSource<'a> {
    pub fn child(&self, field: u16) -> Option<Self> {
        self.node.child_by_field_id(field).map(|node| Self { node, source: self.source })
    }
    pub fn text(&self) -> Result<&'a str, Utf8Error> {
        self.node.utf8_text(self.source.as_bytes())
    }
}
```

- The general rule: when two values are only meaningful together (an index and its collection, an offset and its text, a handle and its arena), give them one type.
- *Unnecessary when* the tree owns its text.

**Coordinates exist in several units; convert in one place.** Parsers count bytes, editors and
LSP count UTF-16 code units by default, people count lines and columns, and a "character" on
screen may be several `char`s.

- One type per coordinate system. A conversion is an explicit function that takes the text; nobody does range arithmetic across units by hand.
- Compute all units in one pass over a line so they cannot drift, and keep a table of line-start offsets when conversion is frequent.
- Test with ASCII, a two-byte character, an emoji outside the basic plane (two UTF-16 units, four UTF-8 bytes), a combining mark, a tab, and CRLF line endings.
- A column shown to a person is one-based and, for alignment, depends on display width (`unicode-width`), which is a fourth number.

- **A fragment parser tries a small set of wrapping contexts** (as an expression, as a statement, as an item), records the wrapper offsets so the fragment's own range can be recovered, and reports which context parsed. Many contexts mean ambiguous matches.
- **A whole-file follow-up found during a tree walk** (reformat, fix imports) is registered as a deferred pass that runs once afterwards. A node visit does not restart from the root.

### Decorators and policy layers

**Cross-cutting policy wraps the service; it is not sprinkled inside it.** Rate limiting,
retry, metrics and caching implement the same trait around an inner implementation, and are
applied once, in the factory.

```rust
pub struct RateLimited<S> {
    inner: S,
    limiter: RateLimiter,
}

impl<S: Completion> Completion for RateLimited<S> {
    async fn generate(&self, prompt: &str, options: &Options) -> Result<TextStream, CompletionError> {
        self.limiter.acquire(1).await;
        self.inner.generate(prompt, options).await
    }
}
```

- **Order of layers is behaviour.** Retry outside a rate limiter makes every attempt wait for a permit; retry inside it does not. A timeout outside retry bounds the whole operation; inside, each attempt. A cache outside metrics hides hits from them. Write the order down and test it.
- A limiter that counts requests cannot express a quota in tokens, bytes or per-endpoint budgets. Turning "per minute" into per-second refills changes the burst behaviour relative to the provider's window.
- Selection of the back end and application of the wrappers live in one factory. Adding a back end touches dispatch, request shaping, capability flags and wrapping in one change.
- **A back-end kind from configuration is parsed into an enum when the configuration loads.** An unknown kind is a typed configuration error at start-up, never a `panic!` in the factory at first use.
- In a service already built on `tower`, use its `Layer` and `Service` instead of a parallel mechanism.

**Decoding policy wraps the raw stream.** A provider's chunk stream stays raw; product rules
(stop sequences, trimming, limits) sit in a layer over it.

```rust
let mut text = String::new();
let mut stop = StopMatcher::new(&stop_sequences); // stateful: one per request
while let Some(chunk) = chunks.next().await {
    text.push_str(&chunk?);
    if let Some(cut) = stop.find_in(&text) {
        text.truncate(cut); // a byte index on a char boundary
        break;
    }
}
```

- **A marker can be split across chunks.** Match against the accumulated text (or keep a tail as long as the longest marker), never against one chunk alone.
- `String::truncate` panics off a character boundary; an index from `str::find` is always on one.
- When forwarding incrementally, hold back the last `longest_marker - 1` bytes until the next chunk shows they are not the start of a marker.
- Test a marker split at every position, a marker at the very start and the very end, and text that only resembles one.

### Identifiers and conversions

**Many IDs over one primitive: one generic wrapper, one marker per kind.** Shared trait
implementations are written once, and the IDs still cannot be mixed.

```rust
pub struct Id<T> {
    raw: u32,
    _kind: PhantomData<fn() -> T>,
}

impl<T> Clone for Id<T> {
    fn clone(&self) -> Self { *self }
}
impl<T> Copy for Id<T> {}
impl<T> PartialEq for Id<T> {
    fn eq(&self, other: &Self) -> bool { self.raw == other.raw }
}
impl<T> Eq for Id<T> {}

pub struct TableKind;
pub struct JobKind;
pub type TableId = Id<TableKind>;
pub type JobId = Id<JobKind>;
```

- **Write the trait impls by hand, or use `derive-where`.** `#[derive(Clone)]` on `Id<T>` adds `T: Clone`, which the marker types do not satisfy.
- `Debug` should print the kind (`TableId(7)`), or logs are full of bare numbers.
- A handful of IDs is simpler as hand-written or macro-generated newtypes. An ID with its own invariant (a checksum, a format) is always its own type.
- IDs from different instances of the same store are still mixable. If that matters, the handle carries the store's identity too, checked in debug builds.

**Withhold a `From` that would lose context.** If `?` would silently turn a low-level error
into yours while dropping what the caller needs to know, do not implement the conversion.
Provide named constructors that demand the context.

```rust
#[derive(Debug, thiserror::Error)]
pub enum RpcError {
    #[error("{service}: {status}")]
    Status { service: &'static str, status: Box<tonic::Status> },
    #[error(transparent)]
    Internal(#[from] anyhow::Error),
}

// Deliberately no From<tonic::Status>: a status must say which service produced it.
impl RpcError {
    pub fn from_status(service: &'static str, status: tonic::Status) -> Self {
        Self::Status { service, status: Box::new(status) }
    }
}
```

- The call site becomes `.map_err(|s| RpcError::from_status("meta", s))?`: one visible line instead of an invisible lossy one.
- Leave a comment where the impl would be, so nobody "helpfully" adds it.
- Boxing a large payload keeps the error enum, and every `Result` that carries it, small.
- **`let _ = fallible();` needs a comment saying why the error does not matter.** Without one it reads as an oversight, and usually is.

**One exhaustive serialiser per export format.** Writing typed values back into a replayable
text format puts every escaping rule (identifier quoting, string escapes, float precision,
date syntax) behind one `match` with no wildcard arm. A new value type then fails to compile
until its arm exists, and arrives with an export-then-import round-trip test. Formatting
scattered across call sites is how one path forgets to escape.

### Handles, options and dependencies

**A cloneable handle, with a builder per call.** An SDK or client entry point is a small
handle around `Arc`-shared internals: `Clone + Send + Sync`, cheap to clone, every method on
`&self`. Options for one call come from an operation builder that implements `IntoFuture`, so
the plain call stays short.

```rust
let bytes = op.read("hello.txt").await?;

let bytes = op
    .read_with("hello.txt")
    .range(0..8 * 1024 * 1024)
    .concurrent(4)
    .await?;
```

- Callers clone the handle into tasks; they never wrap it in their own `Arc<Mutex<_>>`. If they have to, the handle is wrong.
- Per-call options do not mutate the handle. Settings on the handle are defaults fixed at construction.
- *Skip the per-call builder* when an operation has one or two options; a plain argument or an options struct is enough.

**Dependencies are injected, never read from a hidden global.** A shared cache, credential
source, clock or policy is passed through the constructor or builder, with a default so simple
callers need not supply one.

- Callers can then share one instance across several builds, and tests can substitute it.
- Show the shared-instance path in the example; it is the one callers get wrong.
- `build` may return the product together with its diagnostics (`(Image, BuildReport)`), so callers need no second call to learn what happened.

**A callback in an options struct: decide what `Clone` and `Debug` do.**

```rust
#[derive(Clone)]
pub struct PushOptions {
    pub retries: u32,
    pub on_progress: Option<Arc<dyn Fn(Progress) + Send + Sync>>,
}

impl fmt::Debug for PushOptions {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("PushOptions")
            .field("retries", &self.retries)
            .field("on_progress", &self.on_progress.is_some())
            .finish()
    }
}
```

- `Arc<dyn Fn>` makes the clone carry the callback, which is what a reader of `.clone()` expects. A hand-written `Clone` that silently drops a field is a trap; if a callback must not be shared, do not implement `Clone`.
- `Debug` says whether a callback is present and prints nothing of it.
- Say on which thread or task the callback runs, and that it must not block.

**Raw and resolved paths are different types.** Untrusted path input is one type; a
canonical path known to be inside an allowed root is another. One resolver, built from an
explicit base directory, converts the first into the second.

```rust
pub struct ResolvedPath(PathBuf);

impl Resolver {
    pub fn resolve(&self, raw: &RawPath) -> Result<ResolvedPath, PathError> {
        let joined = self.base.join(raw.as_path());
        let canonical = joined.canonicalize().map_err(PathError::Io)?;
        if !canonical.starts_with(&self.base) {
            return Err(PathError::OutsideBase);
        }
        Ok(ResolvedPath(canonical))
    }
}
```

- Never join a user-supplied path onto a root and open it. `..`, an absolute path (which replaces the base in `join`) and a symlink all escape.
- `canonicalize` needs the path to exist and follows symlinks; the base must itself be canonical. For a file about to be created, canonicalise the parent and validate the final component separately.
- A check followed by an open is a race if someone else can modify the directory. Where that matters, open relative to a directory handle (`cap-std`, `openat`) instead of checking a string.
- Case sensitivity, symlinks and prefixes differ by platform; test each supported one.

### Algorithms, dispatch and dynamic data

**An algorithm is written against the smallest contract it needs.** Not against one concrete
container: a trait with the few operations used (node count, neighbours, degree), which each
representation implements. Run it against at least two implementers in tests. *Skip the trait*
while there is one representation and no second in sight.

**Results cannot be read before the run.** `fn run(self) -> Finished`, or a `run` that returns
the result, makes "read before running" and "read after a failed run" impossible to write.

- Where a flag is unavoidable (bindings to another language), set it false at the start, true only after complete results exist, never on the error path, and every getter checks it.
- A reusable algorithm object separates its state (with `reset`) from its driver. Test by running the same instance twice; stale state from the first run is the usual bug.

**Shared scaffolding lives in a provided method.** The trait's provided method sets up what
every implementation needs (progress, naming, accounting) and calls one small required
method. Implementers write only that. A change to the provided method changes every
implementation at once, so keep it conservative, and do not let implementers override it.

**Register by type, dispatch by dense index.** Registration stays ergonomic and typed; at
start-up it is compiled once into a `Vec` indexed by a compact, stable code.

- Before the hot loop, check that every advertised code has a handler and is in range.
- Codes that are sparse, untrusted or change at run time use a map, and an unknown code is an error, not an index panic.

**Dynamic side data has typed handles.** Attributes chosen at run time live in a registry of
type-erased storages; reads and writes go through a typed handle. Attaching rejects a duplicate
name; a typed read checks the stored type and returns an error on mismatch; a handle is
invalid after detach. *A fixed set of attributes is plain struct fields.*

**Smaller rules.**

- **An optional consistency check is an explicit value on the request** (`Option<ExpectedVersion>`), not a side channel in the executor. Test "absent" and "mismatch".
- **A command that can return several shapes carries the expected shape** beside the statement, so encoding, execution and decoding share one contract.
- **Dynamic, stringly-typed access is for the edge only:** a remote API whose endpoints are not known when the client ships. Wherever a typo must fail at compile time, write typed methods.
- **Operator overloading must not surprise.** Use `std::ops` where the algebra is the ordinary one (vectors, durations, money in one currency). For a DSL, where precedence or laziness would mislead, prefer named methods.
- **Messy input forms are normalised once** into a small typed value; the accepted forms and their error messages are public API with a test each.
- **One gate owns timing policy.** A scheduler or load driver asks one place "may this run now", backed by an injectable clock. Tests use a fake clock; callers never repeat schedule checks.

### State, transitions and atomic change

**A multi-step change that must not be half-done is a typestate transaction.** For a
multi-file edit, a migration or a generated patch, where a wrong call order corrupts user
data, each irreversible phase is a type and each transition consumes `self`.

```rust
pub struct Pending;
pub struct Staged;
pub struct Applied;

pub struct Transaction<State = Pending> {
    root: PathBuf,
    edits: Vec<ValidatedEdit>,
    backups: Option<BackupSet>,
    _state: PhantomData<State>,
}

impl Transaction<Pending> {
    pub fn stage(self) -> Result<Transaction<Staged>, BatchError> { /* ... */ }
}
impl Transaction<Staged> {
    pub fn apply(self) -> Result<Transaction<Applied>, BatchError> { /* ... */ }
}
impl Transaction<Applied> {
    pub fn commit(self) -> Result<Report, BatchError> { /* ... */ }
    pub fn rollback(self) -> Result<(), BatchError> { /* ... */ }
}
```

- Committing before applying does not compile. Inputs are already validated types.
- Decide what happens when an `Applied` transaction is dropped without commit or rollback: roll back in `Drop` on a best-effort basis and log, since `Drop` cannot return the error.
- For a single file, write a temporary file in the same directory and rename it over the target. That is atomic and needs no machinery.

**Apply a group of options atomically.** An update of several settings never leaves the
object half-changed. Build the next value and swap:

```rust
let mut next = self.clone();
next.apply(&options)?;
*self = next;
```

- If cloning is too expensive, validate everything first and mutate only after nothing can fail.
- Options with irreversible side effects (opening a port, deleting a file) are validated with the rest and performed last.

**Every status write goes through one setter that consults the transition table.**

```rust
impl Job {
    pub fn transition(&mut self, next: Status) -> Result<(), IllegalTransition> {
        if !self.status.can_become(next) {
            return Err(IllegalTransition { from: self.status, to: next });
        }
        self.status = next;
        Ok(())
    }
}
```

- The field is private; nothing assigns it directly. The table is one `match` on `(from, to)`.
- Adding a status changes the table first, then every handler that enters or leaves it.
- Do not add a second stored status when the state can be derived from data already held; two sources will disagree.

**Publish an immutable result from a mutable builder.** Analysis that needs mutable working
state keeps it inside the builder and publishes through `finish(self) -> Catalog`. Consuming
the builder means nothing can change after publication, and the result can be shared in an
`Arc` without locks. Callers that need live updates get an explicit session type instead.

**Protocol state that is not concurrent says so in its type.** A cursor, session, transaction
or result stream with hidden protocol state has `&mut self` methods and is neither `Clone` nor
`Sync`, so interleaved use does not compile. Where sharing is forced on you (a foreign handle),
a guard fails loudly on a second concurrent entry (`try_lock`, then an error) instead of
interleaving silently.

**Read and write entry points can be separate types.** A marker parameter such as
`Batch<Read>` and `Batch<Write>` makes a write inside a read batch a compile error. Worth it
when the distinction has consequences (a read replica, a read-only transaction); otherwise a
run-time check is simpler.

**Preflight checks cannot be skipped when the context is only reachable through them.** When
one operation is shared by several entry points with different checks, the shared helper does
not take the raw context. It takes a provider that hands the context out only after running
that entry point's checks.

```rust
pub trait CheckedAccess {
    async fn checked(&self, request: &Request, auth: &Auth) -> Result<&Store, AccessError>;
}
```

- The provider is chosen at the API boundary, never inside the helper.
- The bypass implementation has an alarming name (`UncheckedAccess`) and does not appear in a public handler. A search for the name is then an audit.
- If the check changes what the operation means, it is two operations.

**Smaller rules.**

- **A heuristic score explains itself:** the number, its named factor contributions and the inputs that were missing. A missing signal is reported as missing, never replaced with a default that looks like data. Weights are a struct with `Default`. Do not let such a score trigger an irreversible action unattended.
- **A writer finalised in `Drop` flushes when the temporary dies,** which is the end of the statement unless it is bound to a name. Errors in `Drop` are lost, so offer an explicit `finish()` for callers who need them.
- **A replayable view is a list of immutable snapshots and an index.** One pure function computes the steps; previous, next and reset only move the index. For long runs, keep a window or compute lazily.
- **Configuration round-trips.** A type rebuilt from its configuration stores the declared values verbatim and derives the rest in a build step. A test rebuilds, reads the configuration back and compares.

### Callbacks and sinks

**Push events to a caller-defined sink when the traversal is complex.** The traversal strategy
(search, scan, parse) stays internal; the caller supplies what to do with each event.

```rust
pub trait Sink {
    type Error;

    /// Return `Ok(false)` to stop early.
    fn matched(&mut self, mat: &Match<'_>) -> Result<bool, Self::Error>;

    fn context(&mut self, _line: &Context<'_>) -> Result<bool, Self::Error> {
        Ok(true)
    }

    fn finish(&mut self, _summary: &Summary) -> Result<(), Self::Error> {
        Ok(())
    }
}
```

- One required method; the rest default, so a simple sink is a few lines.
- The sink borrows event data for the call (`Match<'_>`), so the traversal can reuse its buffers and nothing is allocated per event. A sink that needs to keep data copies it.
- State the contract: `finish` is called exactly once, including after an early stop, and not after an error.
- *Prefer an iterator* when the traversal is simple enough to be one. Iterators compose and the caller keeps control. A sink is for when borrowing rules or internal buffering make an iterator awkward or slow.
- An enum for the return (`ControlFlow<()>`) reads better than a `bool` whose meaning has to be remembered.

### Strategies, formats and bounds

**One operation, several strategies, chosen in one place.** A public operation may have
several implementations (memory map, whole buffer, incremental reader) selected from
configuration, input shape and platform. The selection is one function.

- Impossible configurations are rejected up front with a typed error, before any work starts.
- **A fast path never removes the slow path,** and the two are tested against each other. The rarely taken path gets its own tests; configuration bugs live there.
- Let a test force each strategy. If only the heuristic can choose, the fallback is never exercised.
- *Not for* callers who need one exact algorithm; give them the named function.

**Permissive on the way in, canonical inside.** A forgiving input form (unsorted, duplicates
allowed) accepts messy data. The compute form has a documented invariant (sorted, unique)
established once, at conversion.

- The canonical type's constructor is the only way to make one, so every holder may rely on the invariant. Operations that receive raw parts check and return a typed error; they do not compute a wrong answer.
- Canonicalising can change the element count (duplicates merge). Do not carry counts across the conversion.
- Do not canonicalise silently on a hot path where a sort would surprise, or where duplicates mean something.

**Bundle repeated bounds into one named trait.**

```rust
pub trait Scalar:
    Copy + PartialEq + Add<Output = Self> + Sub<Output = Self> + Mul<Output = Self> + Default
{
}

impl<T> Scalar for T where
    T: Copy + PartialEq + Add<Output = T> + Sub<Output = T> + Mul<Output = T> + Default
{
}
```

- The blanket impl makes it an alias: every qualifying type gets it for free. Leave the blanket impl out only when implementers must opt in or supply methods.
- Create it after the same bound list has appeared three times, not before. Its supertraits are exactly what the algorithms call; a bound nobody uses still shuts types out.
- Long supertrait lists make compiler errors long. Split the trait if implementers must supply much more than each algorithm uses.

**A scoped helper makes the safe lifetime the default.** If the caller must remember cleanup,
offer `with_x(|resource| ...)` beside the raw constructor.

```rust
pub fn with_temp_dir<T>(f: impl FnOnce(&Path) -> io::Result<T>) -> io::Result<T> {
    let dir = tempfile::tempdir()?;
    let result = f(dir.path());
    dir.close()?; // explicit, so a clean-up failure is reported
    result
}
```

- The borrow checker stops the resource escaping the closure, and clean-up runs on the error path too.
- An RAII guard is the more flexible form and composes with `?` and early return. Use the closure when the resource must not outlive a scope under any circumstances, or when clean-up can fail and the caller should hear about it.
- An async closure borrowing the resource is awkward to type; there a guard, or an owned handle with an explicit `close().await`, is usually simpler.
- Where native handles are exposed to JavaScript (Tauri, WebAssembly), provide the scoped form on that side too, and test both the throwing and the resolving callback.

**One `apply_update` for a streamed record.** A record built up progressively (a job status,
a trace) changes only through `apply(&mut self, update: Update) -> Result<(), UpdateError>`
over a typed update enum.

- An impossible or out-of-order update is a typed error, never a panic, since updates may come from outside.
- The full internal record and the form sent to clients are different types, and the conversion is where redaction and trimming happen. It runs before anything leaves the process.

**A conversion that only reads its source takes a reference.** `impl From<&Dense> for Sparse`
lets the caller keep the original; add `From<Dense>` only when consuming the source saves a
copy. Have the impl delegate to a named function, which can be tested and benchmarked alone.

### Core idioms

- **Expressions over statements.** `if`, `match` and blocks are expressions; bind their value instead of declaring a `mut` and assigning in each branch. Use an iterator chain where it reads as a description of the result; use a loop where there are side effects, early exits or several accumulators.

```rust
let label = match status {
    Status::Active => "active",
    Status::Suspended { .. } => "suspended",
    Status::Closed => "closed",
};
```

- **`Cow<'_, str>` when the value is usually borrowed and sometimes changed:** normalisation, escaping, lossy decoding.

```rust
pub fn normalise(input: &str) -> Cow<'_, str> {
    if input.contains('\t') {
        Cow::Owned(input.replace('\t', "    "))
    } else {
        Cow::Borrowed(input)
    }
}
```

  *Skip it* when the value is always owned or always borrowed, and in struct fields unless profiling asks for it: the lifetime spreads to every holder. Calling `.into_owned()` on every result means it should have returned `String`.
- **A `type` alias is not a new type.** `type UserId = u64;` documents and checks nothing. Use a newtype for distinction; use an alias to shorten a long generic type.
- **`#[repr(transparent)]` on a newtype** is needed only when its layout is relied on: across FFI, or for a reference cast between the wrapper and its field. Elsewhere it is harmless and unnecessary.
- **The orphan rule:** to implement a foreign trait for a foreign type, wrap the type in a local newtype.
- **Do not return `Result` from something that cannot fail,** and do not return `Option` where an error would explain why.
- **`impl Fn` for callbacks, `fn` pointers for tables.** `impl Fn(T) -> U` accepts closures and inlines. A plain `fn(T) -> U` pointer rejects capturing closures; use it in static dispatch tables, in `const` contexts and across FFI, where a nameable, `Copy` type is the point. `&dyn Fn` or `Box<dyn Fn>` when the callback is stored or code size matters more than the call.
- **Keep generic bounds as simple as the use.** `fn f(s: &str)` beats `fn f<S: AsRef<str>>(s: S)` unless callers really pass several types; over-generic signatures hurt inference and error messages. When a generic wrapper is wanted, make it thin and delegate at once to a non-generic inner function, so the body is compiled once.

```rust
pub fn read_config(path: impl AsRef<Path>) -> Result<Config, ConfigError> {
    fn inner(path: &Path) -> Result<Config, ConfigError> { /* the real body */ }
    inner(path.as_ref())
}
```

- **Visibility is the narrowest that works.** Start private; widen to `pub(crate)`, then `pub` when something outside needs it. Every `pub` item in a library is a promise.
- **Do not clone to quiet the borrow checker.** The error is usually pointing at an ownership question: who should own this, and for how long. Answer that. `Rc` or `Arc` is for when several owners really exist.
- **Monomorphisation has a cost.** If generics inflate compile time or binary size, use `dyn Trait` at boundaries and on cold paths, and measure the effect (`cargo llvm-lines`, `cargo bloat`).
- **Name the collection type where it reads best:** `let v: Vec<_> = iter.collect();` or `iter.collect::<Vec<_>>()`. Collect into `Result<Vec<_>, _>` to stop at the first error.
- **Pick the pattern form by the number of cases.** `match` when every case matters; `if let` for one case where the rest is nothing; `let ... else` to unwrap or leave early and keep the happy path unindented; `while let` to drain; `matches!` for a boolean test.

```rust
let Some(user) = users.get(&id) else {
    return Err(Error::UnknownUser(id));
};
```

- **`#[non_exhaustive]` keeps room to grow.** On a public enum, other crates must write a wildcard arm, so adding a variant is not a breaking change; on a struct, they cannot construct it literally, so adding a field is not either. *Use on* public error enums and option structs expected to grow. *Do not use on* an enum callers are meant to match exhaustively (a closed set of states), because it takes the compiler's check away from them. It has no effect inside the defining crate.
- **Avoid a wildcard arm on your own enums.** `_ =>` silences the compiler exactly when a new variant arrives. List the variants, or group them explicitly.

### Traits: the details that bite

- **Object safety (dyn compatibility) is a design decision made early.** A trait is usable as `dyn Trait` only if its methods take `&self`, `&mut self`, `Box<Self>`, `Rc<Self>`, `Arc<Self>` or `Pin<..>`, have no generic type parameters, and do not return `Self`. Keep a method off the trait object, and the trait usable, with `where Self: Sized`:

```rust
pub trait Shape {
    fn area(&self) -> f64;

    fn scaled(self, factor: f64) -> Self
    where
        Self: Sized;
}
```

  Add a test that names `dyn Shape` (`fn _assert(_: &dyn Shape) {}`), so a later method cannot silently break it.
- **Async methods in traits.** `async fn` in a trait works with generics and static dispatch, but the trait is then not usable as `dyn`, and the returned future's `Send`-ness cannot be named by callers. For a `dyn` trait, return `Pin<Box<dyn Future<Output = T> + Send + '_>>` by hand or through `async-trait`; the cost is one allocation per call, which is negligible beside I/O. In a public trait whose futures must be `Send`, write `fn f(&self) -> impl Future<Output = T> + Send`.
- **Seal a trait you are not ready to let others implement.** Then adding a method is not a breaking change.

```rust
mod private {
    pub trait Sealed {}
}
pub trait Format: private::Sealed {
    fn name(&self) -> &'static str;
}
```

  Document that it is sealed. *Do not seal* a trait that exists to be an extension point.
- **Coherence.** Either the trait or the type must be local. Extend a foreign type with an extension trait; implement a foreign trait for a foreign type through a newtype. A blanket `impl<T: Other> Mine for T` prevents you and everyone else from writing any other overlapping impl later: add one only when it is the whole story.
- **Higher-ranked bounds for callbacks that borrow.** `F: for<'a> Fn(&'a Row) -> &'a str` says the callback works for any lifetime. Elision usually writes this for you in `Fn(&Row) -> &str`. Do not demand `'static` from a callback that is only called before the function returns.
- **Generic associated types for lending.** When an associated type must borrow from `self` (a lending iterator, a cursor over a buffer), a GAT (`type Item<'a> where Self: 'a;`) expresses it without allocation. It also makes the trait harder to use and not `dyn`-compatible. Reach for it when returning owned items is measurably too slow, not before.
- **Trait-object lifetimes default to `'static` in a `Box`.** `Box<dyn Trait>` means `Box<dyn Trait + 'static>`. To box something that borrows, write `Box<dyn Trait + 'a>`. The error "borrowed value does not live long enough" on a boxed closure is often this.
- **Lifetime elision** covers one input reference, or `&self`. With two input references and a returned reference, write the lifetimes; that is the place to decide which input the output borrows from.
- **Upcasting** from `&dyn Sub` to `&dyn Super` works directly on recent toolchains (1.86 and later). Older code needs an `as_super(&self) -> &dyn Super` method; check the project's minimum supported version before removing one.
- **No specialisation in library code.** It is unstable and its soundness questions are open. Design the trait explicitly, or dispatch on an enum.
- **`where` clauses** take bounds that do not fit on the signature line.
- **A crate `prelude` is for traits users must import to call methods,** plus a few ubiquitous types. Keep it small; a glob import that brings in fifty names causes collisions.
- **`NonZero`, zero-sized and uninhabited types** when they are the honest model: `Option<NonZeroU32>` for an ID where zero means absent (and it is the size of a `u32`); a zero-sized marker for compile-time state; `Infallible` for an error that cannot occur. Use them because the model is clearer, not because the layout is clever.
- **Edition 2024** changes how `ref` and `mut` interact with default binding modes in patterns, among other things. Migrate with `cargo fix --edition` and read the diff; do not hand-edit patterns in bulk.

### Pin and hand-written futures

Most code never needs this. `async fn`, `tokio::pin!` and `Box::pin` cover nearly everything.

- **Project pinned fields with `pin-project-lite`,** never by hand and never with `Pin::new_unchecked` without a written proof.

```rust
pin_project_lite::pin_project! {
    pub struct Timed<F> {
        #[pin]
        inner: F,
        started: Instant,
    }
}

impl<F: Future> Future for Timed<F> {
    type Output = (F::Output, Duration);

    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        let this = self.project();
        let output = std::task::ready!(this.inner.poll(cx));
        Poll::Ready((output, this.started.elapsed()))
    }
}
```

- **The `Pending` contract:** return `Poll::Pending` only after something has been arranged to wake the task (usually by polling an inner future that registered the waker). Returning `Pending` without that hangs forever; calling `wake` immediately and returning `Pending` is a busy loop.
- Do not poll a future again after it returned `Ready` unless it is documented as fused.
- *Prefer* an `async` block or a combinator. Write a manual `Future` only for a leaf primitive or when the state machine must be named and stored.

### Features, macros and targets

- **Features are additive.** Enabling a feature never removes or changes existing API, and no two features are mutually exclusive, because Cargo unifies features across the whole dependency graph and some crate will enable both. For a real either-or (two TLS back ends), pick a documented precedence or fail with `compile_error!` that names both.
- Name features for what they add (`serde`, `tokio`), without `use-`, `with-` or `no-` prefixes. `default` features are a compatibility surface: removing one is a breaking change.
- **Macro hygiene.** A macro bug repeats at every expansion. In `macro_rules!`, use `$crate::` paths. In a procedural macro, emit absolute paths (`::core::option::Option`), never rely on the caller's imports, and report user errors with `syn::Error` at the offending span, not with a panic.
- **Prefer a function, then a generic, then `macro_rules!`, then a procedural macro.** Each step costs compile time, tooling support and readability of errors.
- **Native and WebAssembly bounds behind local aliases.** A library for both targets defines a few traits once per target (`MaybeSend`: `Send` on native, nothing on wasm) and uses those, never a bare `Send`. Build both targets in CI before any bound changes.
- **One wrapper around the HTTP request builder,** so hooks, authentication, timeouts and target-specific execution apply to every request. Call sites never reach the underlying client.
- **External tools share one lifecycle trait** (minimum version, install, update, instructions) and one logging command runner. Check the version again after an automatic update, and remember that command transcripts can contain environment values.

