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

