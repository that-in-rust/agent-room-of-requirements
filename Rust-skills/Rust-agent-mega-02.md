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

- **Optional dependencies use `dep:`,** so the feature name is yours and the dependency does not create an implicit feature. Each feature has a line of documentation saying what it adds.

```toml
[features]
default = []
serde = ["dep:serde"]

[dependencies]
serde = { version = "1", optional = true, features = ["derive"] }
```

- **Test the feature combinations you support:** none, default, all, and each alone (`cargo hack --each-feature check`). Code behind a feature CI never enables rots.

### More type details

- **An associated type when the implementer fixes the answer; a generic parameter when the caller chooses.** `Iterator::Item` is associated: one iterator has one item type. `From<T>` is generic: one type converts from many. Choosing wrongly shows up as ambiguity errors or as impls you cannot write.
- **An empty enum models "cannot happen" in a generic position.** Prefer `std::convert::Infallible` to a home-made `Void`. A `Result<T, Infallible>` is unwrapped without a panic path:

```rust
fn into_ok<T>(result: Result<T, Infallible>) -> T {
    match result {
        Ok(value) => value,
        Err(never) => match never {},
    }
}
```

  Never pass an uninhabited type across FFI.
- **`..` in a pattern is a decision about future fields.** Destructuring your own struct *without* `..` makes the compiler stop you when a field is added, which is what you want in `Hash`, `PartialEq`, serialisation and anything else that must consider every field. Use `..` when the code truly does not care about the others, and you must use it for `#[non_exhaustive]` types from other crates.

```rust
impl PartialEq for Account {
    fn eq(&self, other: &Self) -> bool {
        let Self { id, email, cached_score: _ } = self; // a new field fails to compile here
        *id == other.id && *email == other.email
    }
}
```

- **Seal a trait that vouches for a representation.** A trait promising layout, a wire format, zero-copy casting or FFI safety must not be implementable outside the crate, because unsafe code relies on every implementer being correct. If outsiders must implement it, make it an `unsafe trait` with the obligations written down.

```rust
mod private {
    pub trait Sealed {}
}
pub trait NativeType: Copy + Send + Sync + private::Sealed + 'static {}

impl private::Sealed for u32 {}
impl NativeType for u32 {}
```

### Macros and build scripts

**Choosing.** A derive generates impls from a type's structure. An attribute macro wraps or
rewrites an item. A function-like macro is for syntax a function cannot take: variadic
arguments, a small DSL, compile-time checks of a literal. If a function or a generic does the
job, write that.

**`macro_rules!`.**

```rust
#[macro_export]
macro_rules! hashmap {
    ($($key:expr => $value:expr),* $(,)?) => {{
        let mut map = ::std::collections::HashMap::new();
        $( map.insert($key, $value); )*
        map
    }};
}
```

- Absolute paths (`::std::`, `$crate::`) so the expansion does not depend on the caller's imports. Accept a trailing comma.
- Each `$x:expr` is evaluated where it is written: once if used once, twice if used twice. Bind it to a `let` in the expansion if it appears more than once.
- Use the narrowest fragment specifier that works (`ident`, `ty`, `expr`, `path`); `tt` is the escape hatch. Keep matchers simple; a recursive muncher has a recursion limit and awful errors.
- Test the expansion like any API, including a compile-fail case for misuse. `cargo expand` shows what it produces.

**Procedural macros.**

- Parse with `syn`, generate with `quote!`, and put the logic in a function over `proc_macro2::TokenStream` so it can be unit-tested without a compiler. Never build code by string concatenation.
- **A user error is a `syn::Error` at the offending span,** returned as `to_compile_error()`. A panic in a macro gives the user a message with no location. Collect several errors and report them together where possible.
- A procedural macro runs arbitrary code at build time with the developer's privileges, and adds `syn` to everyone's compile. Keep it small and deterministic: no network, no clock, no reading files outside the crate without telling Cargo.
- Generated code that users will see in errors should be as plain as hand-written code.

**Build scripts.**

```rust
// build.rs
use std::{env, fs, path::PathBuf};

fn main() {
    println!("cargo::rerun-if-changed=schema/api.json");
    println!("cargo::rerun-if-env-changed=API_SCHEMA_STRICT");

    let out = PathBuf::from(env::var_os("OUT_DIR").expect("set by Cargo"));
    let code = generate_from(&fs::read_to_string("schema/api.json").expect("read schema"));
    fs::write(out.join("api.rs"), code).expect("write generated code");
}
```

```rust
// lib.rs
include!(concat!(env!("OUT_DIR"), "/api.rs"));
```

- **Write only under `OUT_DIR`.** A build script that edits the source tree breaks read-only checkouts, vendoring and reproducibility.
- **Declare every input.** Without any `rerun-if` line the script re-runs on every change to the package; with one, it runs only when a listed input changes, so a forgotten input means stale output.
- Output is deterministic: sort what you iterate, embed no timestamps.
- `expect` with a message is acceptable here; a panic is how a build script reports failure. Make the message say what to fix.
- The `cargo::` prefix needs Cargo 1.77 or later; older toolchains use `cargo:`. Check the project's minimum supported version.
- A custom `cfg` set by the script is declared with `cargo::rustc-check-cfg=cfg(has_foo)`, or every use warns.
- Linking: `cargo::rustc-link-lib` and `cargo::rustc-link-search`. A crate that links a native library sets `links = "name"` in its manifest so two versions cannot both be linked.
- **Prefer checked-in generated code plus a test that it is current** when the generator is slow, needs tools users may lack, or the output is worth reviewing in diffs.

- A procedural-macro crate sets `proc-macro = true` under `[lib]` and can export nothing else, so the runtime types it refers to live in a sibling crate that re-exports the macro.

### Registries, back ends and generated code

**One declaration line per variant, when the same list drives several sites.** A small macro
turns a list of names into the enum and its dispatch, so the two cannot drift.

```rust
pub trait Phase {
    fn apply(&self, items: &mut Vec<Item>);
}

macro_rules! declare_phase_kind {
    ($($name:ident = $phase:expr),* $(,)?) => {
        #[derive(Clone, Copy, Debug, PartialEq, Eq)]
        pub enum PhaseKind { $($name,)* }

        impl PhaseKind {
            pub const ALL: &'static [PhaseKind] = &[$(PhaseKind::$name,)*];
        }

        impl Phase for PhaseKind {
            fn apply(&self, items: &mut Vec<Item>) {
                match *self { $(Self::$name => $phase.apply(items),)* }
            }
        }
    };
}

declare_phase_kind! {
    Desugar = DesugarPhase,
    Inline = InlinePhase { threshold: 8 },
}
```

- The enum is `Copy` and can be named in configuration and in ordered phase lists. `ALL` lets a test assert that every kind appears in at least one pipeline.
- *Skip the macro* for a list used in one place. A plain enum with an exhaustive `match` already fails to compile when a variant is missing, and anyone can read it.
- A phase with run-time state does not fit a `Copy` variant; that calls for a registry of boxed values.

**When one matrix drives many sites, keep one inventory macro that takes a callback.**

```rust
macro_rules! for_all_sources {
    ($callback:ident) => {
        $callback! {
            { Kafka, KafkaProperties, KafkaSplit },
            { Pulsar, PulsarProperties, PulsarSplit },
        }
    };
}

macro_rules! declare_properties_enum {
    ($({ $name:ident, $props:ty, $split:ty }),* $(,)?) => {
        pub enum SourceProperties { $($name($props),)* }
    };
}
for_all_sources!(declare_properties_enum);
```

- Adding a row updates every generated site at once. That is the whole benefit, and it is real only from about three sites up.
- Callback macros are hard to read and produce poor errors. Keep each callback small, and keep the row shape identical everywhere.

**A back end is a narrow trait: shared flow provided, the difference required.**

```rust
pub trait Backend {
    type Printer: Printer;
    const NAME: &'static str = <Self::Printer as Printer>::NAME;

    fn phases(&self) -> Vec<PhaseKind> {
        Vec::new()
    }

    /// The one thing every target must supply.
    fn module_path(&self, module: &Module) -> PathBuf;

    fn emit(&self, modules: Vec<Module>, printer: Self::Printer) -> Vec<File> {
        /* shared flow, written once */
    }
}
```

- Preparation (phases) stays separate from rendering (the printer); escaping rules for a target live only in its printer.
- A shared phase can carry one target's assumptions into another. Review each back end's phase list on its own.
- *Not for* targets whose pipelines have nothing in common; forcing them under one trait produces a trait of optional methods.

**Capabilities become parser settings before parsing.** Permissions and feature gates are
turned into settings by one function, and the parser consults the settings. Checking the tree
afterwards means every new syntax needs a second, forgettable check.

```rust
pub fn settings_from(capabilities: &Capabilities) -> ParserSettings {
    ParserSettings {
        files_enabled: capabilities.allows(Experimental::Files),
        ..ParserSettings::default()
    }
}
```

- The same text can be valid under one setting and invalid under another, so the diagnostic names the disabled capability, not just "unexpected token".
- The entry point rejects input longer than the offset type can address (a `u32` offset means inputs up to 4 GiB) with a typed error, before parsing.

**A recursive parser spends a depth budget, and every exit restores it.** Unbounded recursion
on untrusted input is a stack overflow, which aborts the process and cannot be caught.

```rust
fn nested<T>(
    &mut self,
    span: Span,
    parse: impl FnOnce(&mut Self) -> Result<T, SyntaxError>,
) -> Result<T, SyntaxError> {
    if self.depth_left == 0 {
        return Err(SyntaxError::too_deep(span));
    }
    self.depth_left -= 1;
    let result = parse(self);
    self.depth_left += 1;
    result
}
```

- Every recursive production goes through the one helper (or one `Drop` guard). Nobody edits the counter by hand, and `?` inside the closure cannot skip the restore.
- Pick the limit from the smallest stack the parser runs on: a spawned thread defaults to 2 MiB, less than the main thread. Test the limit on that stack, in a debug build, where frames are largest.
- Test both the depth error and that a parse succeeds after one failed, which proves the budget came back.
- The same applies to every recursive walk over the tree afterwards: visitors, printers, `Drop` of a deeply nested tree. A parser limit protects them all only if they recurse no deeper than it did.

**Generated bindings come from a typed spec list and are written atomically.** What to
generate is data (an enum of wrapper kinds), so adding an item is one entry plus a generator
test; nobody edits generated files by hand.

```rust
fn save_atomically(content: &str, target: &Path) -> io::Result<()> {
    let dir = target.parent().unwrap_or(Path::new("."));
    let mut file = tempfile::NamedTempFile::new_in(dir)?;
    file.write_all(content.as_bytes())?;
    file.as_file().sync_all()?;
    file.persist(target).map_err(|e| e.error)?;
    Ok(())
}
```

- The temporary file is created in the target's directory. A rename is atomic only within one filesystem; a temp file under `/tmp` may not be.
- On Unix the temporary file is created readable by the owner only, and keeps that mode after `persist`. Set permissions explicitly if others must read it.
- `sync_all` matters when the file must survive a crash; skip it for build outputs that can be regenerated.
- Generation is idempotent: the same spec gives the same bytes, and unchanged output is not rewritten, so timestamps do not trigger rebuilds.
- Validate each spec at generation time. A wrong signature that is only discovered at the foreign call is a run-time crash.

### Procedural macros in practice

**Parse a macro's own syntax into a typed input, apart from code generation.**

```rust
mod kw {
    syn::custom_keyword!(accessors);
}

pub struct MacroInput {
    pub name: Ident,
    pub fields: Punctuated<Field, Token![,]>,
}

impl Parse for MacroInput {
    fn parse(input: ParseStream) -> syn::Result<Self> {
        input.parse::<kw::accessors>()?;
        input.parse::<Token![=]>()?;
        let name: Ident = input.parse()?;
        input.parse::<Token![,]>()?;

        let body;
        braced!(body in input);
        let fields = body.parse_terminated(Field::parse_named, Token![,])?;
        Ok(Self { name, fields })
    }
}
```

- Keywords are `custom_keyword!` types matched with `parse` or `lookahead.peek`, never identifier strings compared by hand. A `Lookahead1` error lists what was expected for free.
- The pipeline is parse, then validate into a model, then generate. Generation never sees raw tokens, and each stage is tested alone.

**The expansion is an ordinary function.** `fn expand(input: TokenStream2) -> syn::Result<TokenStream2>`
holds the logic; the `#[proc_macro]` entry point only converts types and turns an error into
`to_compile_error()`.

- Tests call `expand`, parse the result with `syn::parse2::<syn::File>` and assert on the items. That proves the output is at least syntactically Rust.
- For reading, print it with `prettyplease`, or run `cargo expand`. Text comparisons of pretty-printed output are smoke checks; the meaning is carried by tests that compile and run the generated code, and by compile-fail tests for misuse.

**A derive states what it accepts and rejects the rest.** One that maps a struct onto a
storage schema takes structs with named fields only, emits per-field code in declaration
order (so column order equals source order), and gives every other input a `compile_error!`
at its span. Compile-fail tests cover enums, tuple structs and unions; a round-trip test
asserts the order. Reordering fields is then a schema change, which the docs must say.

### Closed sets and normalised inputs

**A closed set is an enum, decoded at the edge.**

- **Finite command-line choices derive `clap::ValueEnum`; paths are `PathBuf`.** The parser then validates, lists the choices in `--help` and reports a typo with the alternatives.
- **A kind is never a `String` explained in a comment.** Parse it once (file extensions case-insensitively, with `eq_ignore_ascii_case`), returning `None` or a typed error for anything unknown.
- **A `type` discriminator in data is an enum** with `#[serde(tag = "type")]`, not an `Option<String>` beside a bag of optional fields. Model a published format the way its specification writes it, and link the specification from the type's docs.
- **Options are typed per back end:** `enum Backend { Embedded(EmbeddedOptions), Remote(RemoteOptions) }`, decoded once. A `HashMap<String, Value>` read by string key defers every typo to run time.
- **A fixed set of roles is a struct with a field per role,** not a map from name to value. A missing role is then a compile error instead of a silent default.
- **Allowed combinations are one table:** a `match (from, to)` or a `const` slice of pairs. Evaluation consults it first; anything absent is an error. Scattered `if` checks will disagree.
- *An open set stays open.* If users or plugins may add kinds, an enum with `Other(String)` or a validated newtype is the honest model; an enum that must be edited for each new customer is a bottleneck.

**Several input shapes become one type at the edge.**

```rust
#[derive(Deserialize)]
#[serde(untagged)]
enum SpecInput {
    One(String),
    Many(Vec<String>),
    WithMetric(BTreeMap<String, String>),
}

impl SpecInput {
    fn into_specs(self) -> Vec<Spec> {
        match self {
            Self::One(name) => vec![Spec { name, metric: None }],
            Self::Many(names) => names
                .into_iter()
                .map(|name| Spec { name, metric: None })
                .collect(),
            Self::WithMetric(map) => map
                .into_iter()
                .map(|(name, metric)| Spec { name, metric: Some(metric) })
                .collect(),
        }
    }
}
```

- Document the accepted shapes; they are public API, each with a test.
- **`untagged` tries variants in order and takes the first that fits.** Put the most specific first, and check that no input fits two. Its error on failure is "data did not match any variant", which tells the user nothing: for user-edited configuration, a hand-written `Deserialize` or a custom error naming the accepted shapes is worth the code.

**Normalise once, at the boundary.**

- **Empty, null and absent** that mean the same thing decode into one representation (`Option<NonEmptyString>`); code past the boundary never calls `is_empty()` again. *Where they differ* (a partial update: absent keeps, null clears), keep the distinction in a type such as `Patch<T>` and do not collapse it.
- **Whitespace-only is missing** for a required human-entered field: check `trim().is_empty()` and report one variant carrying the field name. *Do not trim* secrets, passwords or anything where whitespace is data.
- **Numbers, times and IDs that arrive as strings are parsed at the boundary** (`serde_with::DisplayFromStr`, a `deserialize_with` function, a newtype), so later code never parses again.
- **Units live in the type or the field name:** a `Duration` with an explicit serde adapter (`humantime_serde`), or `timeout_ms`. A unit that exists only in a comment will be misread.
- **Inferring types from untyped text has a stated, tested order.** If a loader tries "date" before "text", a string that merely looks like a date changes type silently. Document the order, test the ambiguous cases (`"1e5"`, `"NaN"`, `"2024-01-01"`, leading zeros), and let an explicit schema override inference. When several formats are tried, the error names the value and the formats tried.
- **Keep the decoding error as the source,** not flattened into a string, so line and column survive.
- **A parse is a function from input to a finished value.** No parser object whose fields fill in step by step and can be read half-done.
- **Normalise a symmetric operation by ordering its arguments once** (`let (lo, hi) = if a <= b { (a, b) } else { (b, a) };`) instead of writing both branches.
- **A hand-rolled entry point has one usage constant.** Where no argument parser is available (a host function, an FFI command), every arity or type error prints the same `USAGE` text.

**Per-type facts live on a trait; one generic function does the work.**

```rust
pub trait Record: Send + Sync + 'static {
    const TABLE: &'static str;

    fn to_batch(rows: &[Self], embeddings: &[Vec<f32>]) -> Result<Batch, StoreError>
    where
        Self: Sized;
}

fn store<R: Record>(db: &Db, rows: &[R], embeddings: &[Vec<f32>]) -> Result<(), StoreError> {
    if rows.len() != embeddings.len() {
        return Err(StoreError::LengthMismatch {
            rows: rows.len(),
            embeddings: embeddings.len(),
        });
    }
    db.append(R::TABLE, R::to_batch(rows, embeddings)?)
}
```

- **Parallel slices are checked for equal length at entry,** with both lengths in the error. Better still, take one slice of pairs so the mismatch cannot be written.
- Where operations carry a numeric type code (`const TYPE: u16`), a test asserts the codes are unique. Duplicates otherwise dispatch to the wrong handler without any error.

**Smaller rules.**

- **A width-changing cast says whether it sign-extends.** `-1i8 as u64` is `u64::MAX`; `-1i8 as u8 as u64` is `255`. Write the intent in named steps (`u64::from(x as u8)`), use `From` for lossless widening and `try_from` for narrowing, reinterpret same-width bits with `to_ne_bytes` or `to_bits` and never `transmute`. Test with `-1` and the extremes. `clippy::cast_possible_truncation`, `cast_sign_loss` and `cast_possible_wrap` find the rest.
- **"Unsupported" differs from "supported and empty".** A field populated only for some inputs is `Option<Vec<_>>`, with `None` meaning unsupported and the schema saying when. An empty list that might mean either is a wrong answer waiting to be trusted.
- **A handler validates its arguments before any expensive or state-dependent work.** Decode raw input into a typed struct; an unknown enum-like value is an error listing the accepted ones, never a silent default. Otherwise an argument mistake is hidden behind an unrelated later failure.
- **A required per-implementation constant has no default.** `const EXTENSIONS: &'static [&'static str];` without a default makes forgetting it a compile error; an empty default silently supports nothing.
- **`Default` and `new` never fail or panic, and are cheap.** A constructor that looks something up is `try_new() -> Result<Self, _>`. Expensive construction has a verb name (`Index::build(&source)`). When both `new()` and `Default` exist, one calls the other.
- **A derived view borrows its source** (`struct Graph<'a> { parse: &'a ParseResult, .. }`), so it cannot outlive or drift from what it was built from.
- **A child handle may borrow its parent** (`Connection<'db>` holding `&'db Database`), and the compiler then enforces drop order for free. *The cost:* the lifetime makes the handle awkward to store in a struct or move into a spawned task. For handles that travel, share the parent through an `Arc` instead.
- **An algorithm takes its own small parameter struct** of validated values (`NonZeroUsize`, a ratio newtype), built from user configuration in one conversion. The algorithm crate does not depend on the configuration or CLI crate.
- **A command prompts only when attached to a terminal.** If `std::io::stdin().is_terminal()` is false, a missing argument is an error naming the flag. A prompt in CI is a hang.
- **A line-oriented protocol is a tagged enum, and its parse errors carry the line number.** Responses echo the request ID.
- **A tuple that needs a comment to explain its positions is a struct.** `(usize, usize, bool)` becomes named fields and an enum for the flag.

## 7. Ownership, borrowing and data handling

**Defaults.**

- Borrow to read, take ownership to keep, `&mut` to change in place. The signature tells the caller which.
- Clone when the design calls for a second owner, not to make an error go away. A clone of a small value on a cold path is fine and often the clearest code; a clone in a loop over large data is worth a second look.
- `Arc` for shared ownership across threads, `Rc` within one. Neither is a substitute for deciding who owns the data.
- Hold locks and `RefCell` borrows for the shortest scope that is correct, and never across an `.await`.

### Working with the borrow checker

**The error usually describes a real overlap.** Find which borrow is still alive and why,
then shorten it, instead of reaching for `clone` or `Rc<RefCell<_>>`.

```rust
// Rejected: first borrows items while push needs it mutably.
let first = &items[0];
items.push(first.clone());

// End the shared borrow before the mutation.
let first = items[0].clone();
items.push(first);
```

- **A method borrows all of `self`.** Calling `self.helper()` while a field is borrowed fails even if the helper touches other fields. Borrow the fields separately, which the compiler tracks, or make the helper take the fields it needs.

```rust
let Self { index, scratch, .. } = self;
for id in index.keys() {
    scratch.push(*id); // index is borrowed shared, scratch mutably: disjoint fields
}
```

- **Collect, then mutate.** Gather the keys or indices to change in one pass and apply them in a second. Often clearer as well as accepted.
- **Use indices or IDs instead of long-lived references** into a collection that also needs mutation. This is the normal shape for graphs and trees with parent links.
- **Move out through `&mut` with `std::mem::take`, `replace` or `Option::take`,** instead of cloning a field in order to consume it.
- **The `entry` API** does "look up, then insert or update" with one borrow and one hash.

```rust
*counts.entry(word).or_insert(0) += 1;
```

- **Separate the read phase from the write phase in an API.** A method that returns a reference into `self` keeps `self` borrowed for as long as the caller holds it; returning a small owned value or an ID frees the caller.
- `vec.push(vec.len())` compiles through two-phase borrows. Do not design an API that only works because of that rule; write the temporary.
- **Stop and reconsider the design** when a structure wants references to itself, or when lifetimes spread through many signatures. Owned data plus indices, or an arena, is nearly always the answer; `unsafe` is not.

### Interior mutability

| Need | Use | Watch for |
|---|---|---|
| A `Copy` value, one thread | `Cell<T>` | nothing; it cannot fail |
| Any value, one thread | `RefCell<T>` | a second overlapping `borrow_mut` panics at run time |
| Shared across threads | `Mutex<T>` | poisoning, lock order, holding it across `.await` |
| Read-mostly across threads | `RwLock<T>` | writer starvation; often no faster than `Mutex`, so measure |
| A counter or flag | `AtomicUsize`, `AtomicBool` | choosing an ordering; `SeqCst` unless you can argue for less |
| Set once, read often | `OnceLock<T>`, `LazyLock<T>` | initialisation that can fail |

- `RefCell` moves a compile-time rule to run time. Keep each borrow to one statement where possible, and prefer `try_borrow_mut` where re-entrancy is conceivable (callbacks, observers).
- Do not use a `Mutex` in single-threaded code to quiet the borrow checker, and do not make a type `Sync` by wrapping it in one without deciding what the lock protects.
- Interior mutability behind `&self` is part of the API's contract. Say so in the docs when a `&self` method changes observable state.

### Iterators and collections

- **A fallible pipeline short-circuits.** An iterator of `Result<T, E>` collects into `Result<Vec<T>, E>` and stops at the first error. `try_for_each` and `try_fold` do the same without collecting. Never `unwrap` inside a chain.

```rust
let ports: Vec<u16> = fields
    .iter()
    .map(|field| field.parse::<u16>())
    .collect::<Result<_, _>>()?;
```

- **Iterator promises are contracts.** `size_hint` must bracket the true length; implement `ExactSizeIterator` only when the length is exact. Unsafe code must not rely on either for memory safety, since safe code can implement them wrongly.
- Offer `iter()`, `iter_mut()` and `IntoIterator` for `&T`, `&mut T` and `T` on a collection type, so `for x in &collection` works.
- Iterators are lazy. A `map` with side effects that is never consumed does nothing; use `for` when the point is the effect.

| Need | Collection |
|---|---|
| A sequence; the default | `Vec` |
| Push and pop at both ends | `VecDeque` |
| Lookup by key, order irrelevant | `HashMap`, `HashSet` |
| Sorted order, range queries, deterministic iteration | `BTreeMap`, `BTreeSet` |
| Insertion order with lookup | `IndexMap` |
| Repeatedly take the largest | `BinaryHeap` (wrap in `Reverse` for the smallest) |
| A handful of items | a `Vec` and a linear scan, or `SmallVec` if measured |

- **`HashMap` iteration order is arbitrary and differs between runs.** Anything that reaches output, a hash, a snapshot or a test goes through a sort or an ordered map.
- `LinkedList` is almost never right: a `Vec` or `VecDeque` is faster for nearly every workload.
- The default hasher resists collision attacks and is slower for it. A faster hasher (`FxHashMap`, `ahash`) is for keys an attacker does not control, after a profile says hashing matters.
- `Vec::with_capacity` when the size is known; it is free and removes reallocations.

### Sharing and deduplication

**Intern immutable values that repeat heavily.** One canonical `Arc<str>` per distinct value
saves memory and makes clones cheap.

```rust
#[derive(Default)]
pub struct Interner {
    seen: Mutex<HashSet<Arc<str>>>,
}

impl Interner {
    pub fn intern(&self, text: &str) -> Arc<str> {
        let mut seen = self.seen.lock().unwrap_or_else(PoisonError::into_inner);
        if let Some(existing) = seen.get(text) {
            return Arc::clone(existing);
        }
        let value: Arc<str> = Arc::from(text);
        seen.insert(Arc::clone(&value));
        value
    }
}
```

- **Pointer equality (`Arc::ptr_eq`) is valid only if every value of the type comes from the interner.** Enforce that with a newtype whose only constructor is `intern`; otherwise compare contents.
- **An index handle** (`Symbol(u32)` into a table) is `Copy`, four bytes and trivially hashable. It is meaningful only with its table; never compare or serialise symbols from different tables.
- **Never hand out `&'static T` into a `Vec<T>` that can grow.** Growth moves the items. Store `Box` or `Arc` per item, use an arena with stable addresses, or return a clone.
- **The table only grows.** Do not intern unbounded or attacker-controlled input without a cap or scoped lifetime. Evicting by reference count is racy unless done under the table's lock.
- *Skip interning* for values that rarely repeat or are short-lived: it adds a lock and a hash to every construction.

**Deduplicate live resources by canonical identity, holding `Weak`.** A registry of open files
or connections is keyed by the canonical form (absolute path, case-folded where the platform
is case-insensitive) and stores `Weak` references, so it does not keep anything alive. A
failed `upgrade()` removes the entry. A second open with conflicting options is an error, not
a silent share.

**Borrowed or owned, without a `Clone` bound.** `Cow` needs `ToOwned`. For a value that is
sometimes borrowed from a larger structure and sometimes built on demand, and is not
cloneable, a two-variant enum with `Deref` gives one API instead of two.

```rust
pub enum MaybeOwned<'a, T> {
    Owned(T),
    Borrowed(&'a T),
}

impl<T> Deref for MaybeOwned<'_, T> {
    type Target = T;

    fn deref(&self) -> &T {
        match self {
            Self::Owned(value) => value,
            Self::Borrowed(value) => value,
        }
    }
}
```

**Smaller rules.**

- **An RAII guard acquires in its constructor and releases in `Drop`.** Bind it to a name (`let _guard = ...`); `let _ = ...` drops it at once.
- **A handle with several ownership states** (cached, owned, borrowed, transferred) is one type with a state enum and a single release path in `Drop`.
- **A resumable handle checks that it is still valid in every method that advances it,** not only at construction; a stale handle returns a clear error.
- **A point-in-time snapshot is handed out as an iterator or guard that releases on drop,** so callers never manage the underlying commit handle. An empty store yields an empty iterator, not an error.

- **Which wrapper:** `Cow` when the borrowed value may need changing; `MaybeOwned` when the type cannot be cloned; `Arc` when ownership is really shared; a plain owned value when handing it over is the point.

### Iterators in depth

**Accept `impl IntoIterator`, return `impl Iterator`.**

```rust
pub fn total_len<'a>(names: impl IntoIterator<Item = &'a str>) -> usize {
    names.into_iter().map(str::len).sum()
}

pub fn active(users: &[User]) -> impl Iterator<Item = &User> + '_ {
    users.iter().filter(|user| user.active)
}
```

- The caller can pass a `Vec`, a slice, a set or another iterator, and decides whether to collect the result.
- A returned iterator is lazy: nothing happens until it is consumed, and it borrows its source until then. Say so in the docs when the work is expensive or has effects.
- `Box<dyn Iterator>` when the concrete type differs by branch or must be stored. The cost is an allocation and a virtual call per item; it matters only in inner loops.
- **Do not build intermediate `Vec`s** between stages, and do not `collect` only to iterate again.
- Implement `FromIterator` for a custom collection so `collect()` works, and `Extend` so it can be appended to.
- **Do not call `next()` after `None` unless the iterator is fused.** Call `.fuse()` if the code might; make your own iterators fused when that is cheap, and implement `FusedIterator` to say so.
- Implement `DoubleEndedIterator` only where going backwards is natural, and test that `next` and `next_back` meet in the middle without overlap.

**Closure bounds: ask for the least you need.**

| You will call it | Ask for | Callers may pass |
|---|---|---|
| At most once | `FnOnce` | any closure, including one that consumes its captures |
| Several times, one at a time | `FnMut` | closures that mutate their captures |
| Several times, possibly at once or through `&` | `Fn` | closures that only read |

- Asking for `Fn` when you call once rejects closures for no reason.
- A closure sent to a thread or task is `move`, and its captures must be `Send + 'static`. Clone the `Arc` outside the closure and move the clone in.
- Do not require `'static` or `Send` from a callback that is only called before the function returns.

**A lending iterator, when items must borrow from the iterator itself.** A cursor that
decodes into its own buffer cannot be a standard `Iterator`, whose items must outlive the
next call. A generic associated type expresses the loan:

```rust
pub trait LendingIterator {
    type Item<'a>
    where
        Self: 'a;

    fn next(&mut self) -> Option<Self::Item<'_>>;
}
```

- The previous item must be dropped before the next call, which is exactly the constraint the buffer needs. The price: no `for` loop (use `while let`), none of the standard adapters, and no `dyn`.
- *First ask* whether returning owned items is fast enough, or whether a callback (`for_each(|row| ...)`) would do. Both are simpler.
- Never fake it by extending a lifetime with `unsafe` to fit `Iterator`. That is a use-after-free as soon as a caller collects.

**An iterator that owns a resource releases it on every path.** Exhaustion, an error, an
explicit close and an early drop all reach one idempotent clean-up.

```rust
pub struct Rows {
    cursor: Option<Cursor>,
}

impl Rows {
    fn release(&mut self) {
        if let Some(cursor) = self.cursor.take() {
            cursor.close();
        }
    }
}

impl Iterator for Rows {
    type Item = Result<Row, DbError>;

    fn next(&mut self) -> Option<Self::Item> {
        let cursor = self.cursor.as_mut()?;
        match cursor.advance() {
            Ok(Some(row)) => Some(Ok(row)),
            Ok(None) => {
                self.release();
                None
            }
            Err(error) => {
                self.release();
                Some(Err(error))
            }
        }
    }
}

impl Drop for Rows {
    fn drop(&mut self) {
        self.release();
    }
}
```

- Releasing on exhaustion alone leaks when the caller stops early (`.take(10)`, `?` in the loop body). `Drop` covers that.
- After an error the iterator yields `None`, so a caller who ignores the error cannot loop forever.
- If closing can fail and the failure matters, offer `close(self) -> Result<()>` as well; `Drop` can only log.

### Collections in depth

- **`IndexMap` removal:** `swap_remove` is O(1) and breaks insertion order; `shift_remove` keeps it and is O(n). Choose deliberately; plain `remove` is deprecated for this reason.
- **Never change a key in place** in a way that alters its hash or order (through interior mutability). The entry becomes unfindable. Remove, change, reinsert.
- **`BinaryHeap::from(vec)` builds in O(n);** pushing n items one at a time is O(n log n). For the k largest of a stream, keep a min-heap of size k rather than sorting everything. For the k largest of a slice, `select_nth_unstable` is linear.
- **A min-heap, or a heap over floats, needs an explicit total order.** `Reverse(x)` flips a key that is already `Ord`. For floats, define the order with `total_cmp` and add a tie-break so equal priorities pop in a deterministic order.

```rust
struct Candidate {
    cost: f64,
    node: NodeId,
}

impl Ord for Candidate {
    fn cmp(&self, other: &Self) -> Ordering {
        other
            .cost
            .total_cmp(&self.cost) // reversed: the smallest cost is popped first
            .then_with(|| self.node.cmp(&other.node))
    }
}
impl PartialOrd for Candidate {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}
impl PartialEq for Candidate {
    fn eq(&self, other: &Self) -> bool {
        self.cmp(other) == Ordering::Equal
    }
}
impl Eq for Candidate {}
```

  All four traits agree because three are defined from `cmp`. A derived `PartialEq` on a float beside a hand-written `Ord` disagrees on NaN and on signed zero, and collections misbehave quietly when they disagree.
- **Packed bits:** `Vec<bool>` spends a byte per flag, which is fine for small sets. For large bitmaps or wire layouts use `bitvec` or a fixed-size bitset, with bit order and storage type written out (`BitVec<u8, Msb0>`).
- **A read-mostly shared map** is best published as an immutable snapshot: `ArcSwap<HashMap<K, V>>` (or `RwLock<Arc<HashMap<K, V>>>`), where a writer builds a new map and swaps it in. Readers never block and always see a consistent whole. For many concurrent writers, a sharded map such as `DashMap`; do not hold one of its references while touching the same map again, which can deadlock on the shard lock.
- **`SmallVec<[T; N]>`** avoids the heap when a small bound usually holds. It makes the value larger and every access branch; adopt it from a profile, not from a hunch.

**Edit-heavy, then read-heavy: two types.** Mutations go into a builder; an explicit
`finish(self) -> Frozen` sorts, deduplicates and computes totals; read-optimised algorithms
take only `Frozen`. A convention that says "call `update()` before reading" will be broken;
the type cannot be. *Not for* data where every mutation must be visible at once.

**Compressed sparse row layout for a static graph.** Neighbours of `u` are a contiguous
slice, which is cache-friendly and trivially partitioned for parallel work.

```rust
pub struct Csr {
    offsets: Vec<usize>, // length: vertices + 1
    targets: Vec<u32>,
}

impl Csr {
    pub fn neighbours(&self, u: usize) -> &[u32] {
        &self.targets[self.offsets[u]..self.offsets[u + 1]]
    }
}
```

- The constructor checks the invariants once: `offsets.len() == vertices + 1`, offsets never decrease, the last equals `targets.len()`, and every target is a valid vertex. Every reader then relies on them.
- Rebuild for large updates; in-place insertion is O(edges). For a graph that changes constantly, use adjacency lists.

**Values and validity in parallel buffers, for columnar data.** A null still advances the
value buffer by one slot, so both buffers always have the same length and position `i` means
the same row in each. For anything small, `Vec<Option<T>>` is simpler and right.

- **NaN in a priority is usually a bug upstream.** `total_cmp` gives it a place in the order, which keeps the heap consistent but can hide a bad cost calculation. Where NaN should not occur, reject it when the value is created.

### Choosing a pointer

| Need | One thread | Across threads |
|---|---|---|
| One owner on the heap (recursive type, large value, trait object) | `Box<T>` | `Box<T>` |
| Several owners, read-only | `Rc<T>` | `Arc<T>` |
| Several owners, mutation | `Rc<RefCell<T>>` | `Arc<Mutex<T>>` or `Arc<RwLock<T>>` |
| A reference back to an owner | `rc::Weak<T>` | `sync::Weak<T>` |

- **Shared and immutable is the cheap case.** Prefer `Arc<T>` of immutable data, replaced whole, over `Arc<Mutex<T>>` mutated in place. `Arc::make_mut` gives copy-on-write when a private change is needed.
- **`Rc<RefCell<T>>` throughout a design is a sign** that ownership was never decided. It suits a few shared nodes (a GUI tree, an observer list), not a whole data model. Indices into an owning `Vec` are usually simpler and faster.
- **Parent-to-child strong, child-to-parent `Weak`,** or the cycle never frees.
- `Arc::clone(&x)` rather than `x.clone()` makes it visible that only the count is bumped.
- Before `Arc<Mutex<T>>` across tasks, ask whether one task could own the state and receive messages on a channel.

## 8. Errors and recovery

**Defaults.**

- A function that can fail returns `Result`; `?` propagates. Panics are for bugs: a broken invariant that no caller could handle.
- **Libraries return typed errors** (an enum or struct, usually via `thiserror`) that callers can match on. **Applications use `anyhow` or `eyre`** at the top, where errors are reported, not matched. Never export `anyhow::Error` from a library: it tells callers nothing and takes away their ability to react.
- No `unwrap` or `expect` on a path that input, I/O or another system can make fail. Where an invariant truly guarantees success, `expect("why this cannot fail")` states it.
- Never swallow an error. Handle it, return it, or log it with a reason for going on.

### Designing an error type

```rust
#[derive(Debug, thiserror::Error)]
pub enum StoreError {
    #[error("record {id} not found")]
    NotFound { id: RecordId },

    #[error("query timed out after {elapsed:?} (limit {limit:?})")]
    Timeout { elapsed: Duration, limit: Duration },

    #[error("reading {}", .path.display())]
    Read {
        path: PathBuf,
        #[source]
        source: io::Error,
    },

    #[error(transparent)]
    Database(#[from] DatabaseError),
}
```

- **One variant per thing a caller might do differently** (retry, report to the user, treat as absent), not one per call site and not one per underlying library.
- **A variant carries the data needed to act or to explain:** the ID, the path, the limit. A variant holding only a `String` is a message, not a type.
- **Keep the cause as `#[source]`, and do not repeat its text in your message.** Reporters print the chain; a message that embeds the source prints it twice. `cause: String` throws the chain away.
- Messages are lower case, without a trailing full stop, and say what was being attempted.
- **`#[from]` only where the conversion needs no context.** A blanket `From<io::Error>` makes every `?` on a file operation produce an error that does not say which file.
- Errors are `Send + Sync + 'static` so they can cross threads and be boxed. Keep them small; box a large payload, since the size of `E` is paid by every `Result<T, E>`.
- **`#[non_exhaustive]` on a public error enum that will grow,** so adding a variant is not a breaking change.

**An opaque error with a kind, when the error space will evolve.** A public enum freezes its
variants and their fields. A struct with a private representation and a public `kind()` keeps
room to change.

```rust
#[derive(Debug)]
pub struct Error {
    kind: ErrorKind,
    source: Option<Box<dyn std::error::Error + Send + Sync>>,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
#[non_exhaustive]
pub enum ErrorKind {
    NotFound,
    Timeout,
    InvalidInput,
}

impl Error {
    pub fn kind(&self) -> ErrorKind {
        self.kind
    }

    pub fn is_retryable(&self) -> bool {
        matches!(self.kind, ErrorKind::Timeout)
    }
}
```

- Callers cannot construct it, so only your crate decides which states exist. Predicates such as `is_retryable()` answer the question callers actually have.
- *Use a plain enum* when the set is small, stable and callers benefit from matching on fields. Most internal crates are in that case.

### Context and reporting

**Add context where the operation is still meaningful.** `?` alone says what failed, not what
was being done.

```rust
pub fn load_config(path: &Path) -> anyhow::Result<Config> {
    let text = fs::read_to_string(path)
        .with_context(|| format!("reading config {}", path.display()))?;
    let config = toml::from_str(&text)
        .with_context(|| format!("parsing config {}", path.display()))?;
    Ok(config)
}
```

- Context belongs at I/O and orchestration boundaries: opening a file, sending a request, decoding a payload, calling another service. Adding it at every helper repeats the same sentence down the chain.
- `with_context` takes a closure, so the message is formatted only on failure.
- In a library, the equivalent is a variant that carries the context plus the `#[source]`, built with `map_err`.

**A diagnostic for a person says where and what to do.** For user-facing input (configuration,
flags, patterns, file formats): the file, line and column or byte offset, what was found, what
was expected, and a hint when there is an obvious repair. An abstract variant name helps
nobody.

- Rich reports with source snippets and labelled spans (`miette`, `ariadne`, `color-eyre`) belong in the binary. Do not put their types in a library's public API; expose spans and messages as plain data and let the binary render them.
- **Diagnostics must survive non-UTF-8 data.** Paths, command output and protocol bytes are not always valid UTF-8. Print paths with `.display()`, bytes with an escaping formatter, and do not convert to `String` early with `unwrap` or lose data with a silent lossy conversion.
- Never put secrets, tokens or whole payloads in an error message. Errors travel to logs and to users.

**The binary owns the exit code.**

```rust
fn main() -> ExitCode {
    match run() {
        Ok(()) => ExitCode::SUCCESS,
        Err(error) if is_broken_pipe(&error) => ExitCode::SUCCESS,
        Err(error) => {
            eprintln!("error: {error:#}");
            ExitCode::from(2)
        }
    }
}
```

- Returning `ExitCode` from `main` lets destructors run; `std::process::exit` does not, so buffered output and temporary files can be lost.
- A closed pipe (`tool | head`) is not a failure. Look for `io::ErrorKind::BrokenPipe` in the chain and exit quietly.
- `{error:#}` prints an `anyhow` error with its causes on one line; `{error:?}` prints the multi-line report with a backtrace if one was captured.
- Distinct exit codes for distinct classes (usage error, runtime failure) are part of a CLI's interface; document them. Errors go to stderr, results to stdout.
- **A library never exits the process,** prints to stdout or stderr, or installs global handlers.

### Panics

- **Audit production paths before a release:** `unwrap`, `expect`, `panic!`, `unreachable!`, `todo!`, slice indexing and arithmetic on external input. Each becomes a `Result` or gets a comment stating the invariant.

```sh
cargo clippy -- -W clippy::unwrap_used -W clippy::expect_used \
  -W clippy::indexing_slicing -W clippy::panic
```

- Compiling and passing unit tests does not show that a panic is unreachable. For each boundary, one test feeds the bad input and asserts the returned error.
- These lints are noisy in tests; allow them there (`#![cfg_attr(test, allow(clippy::unwrap_used))]`) instead of weakening them everywhere.
- **A panic must not cross an FFI boundary.** Catch it with `catch_unwind` at every exported `extern "C"` function and turn it into an error code.

### Retries

**Whether an error may be retried is a property of the error type,** decided where the error
is created, never by matching message text.

```rust
pub trait Retryable {
    /// Permanent unless a variant opts in.
    fn is_retryable(&self) -> bool {
        false
    }
}

pub struct RetryPolicy {
    pub max_attempts: NonZeroU32,
    pub base_delay: Duration,
    pub max_delay: Duration,
    pub max_total: Duration,
}

pub async fn retry<T, E, Fut>(
    policy: &RetryPolicy,
    sleeper: &impl Sleeper,
    mut op: impl FnMut() -> Fut,
) -> Result<T, E>
where
    E: Retryable,
    Fut: Future<Output = Result<T, E>>,
{
    let started = sleeper.now();
    let mut attempt = 1;
    loop {
        match op().await {
            Ok(value) => return Ok(value),
            Err(error) if !error.is_retryable() => return Err(error),
            Err(error) if attempt >= policy.max_attempts.get() => return Err(error),
            Err(error) => {
                let delay = policy.jittered_delay(attempt);
                if sleeper.now() - started + delay > policy.max_total {
                    return Err(error);
                }
                sleeper.sleep(delay).await;
                attempt += 1;
            }
        }
    }
}
```

- **Retry only idempotent operations,** or ones made idempotent with a key the server deduplicates on. Retrying a non-idempotent write duplicates it.
- **Bound attempts and total time, back off exponentially, add jitter.** Without jitter, clients that failed together retry together.
- **Default to permanent.** A wrong "retryable" turns one outage into a retry storm; a wrong "permanent" only surfaces an error.
- **Typical classification for HTTP:** retry timeouts, connection resets, 429, 502, 503 and 504; honour `Retry-After`. Do not retry 400, 401, 403, 404 or 422: the request is wrong and will stay wrong. Treat 500 as retryable only for idempotent calls.
- **Inject the clock and the sleep** (the `Sleeper` above), so tests of the retry loop run instantly and can assert the delays.
- **One layer retries.** Retries at three layers multiply: three by three by three is twenty-seven calls. Put the loop at the operation boundary; inner layers return classified errors.
- **A closure passed to a retrying helper may run more than once.** Say so in the docs. It must not move out of captured state or leave partial effects behind.
- **Retrying a stream restarts it.** Either the caller tolerates repeated partial output, or only committed chunks are passed on and the retry resumes from the last committed position.
- Stop when the caller's deadline or cancellation fires; a retry loop that outlives its request is a leak.
- When retries are exhausted, return the last error together with the attempt count, not a generic "retries exhausted".

### Diagnostics at scale

- **Explain the known cause, keep the original.** At startup and configuration boundaries, match the typed causes you recognise and print what it means plus one concrete action ("port 8080 is in use; pass `--port` or stop the other process"), with the original error attached. Do not guess at causes you have not matched: a confident wrong hint is worse than the raw error.
- **Presentation is owned by helpers, facts by the error.** Quote and escape every interpolated identifier, path and value through shared helpers, so messages are consistent and hostile input cannot inject control characters or fake log lines.
- **Rate-limit a log line on a hot failure path, and count it.** Keep the state per call site (a `static` atomic counter and timestamp), and pair it with a metric, since suppressed lines hide how often it happens. Never rate-limit security or audit events.
- **One `ensure!`/`bail!` pair per crate** that builds the crate's typed error, if invariant checks are numerous. Use the project's existing macros; a new error macro hides control flow and must earn its place through repetition.
- **A debug switch for backtraces, not a second code path.** Capture a `Backtrace` in the error when `RUST_BACKTRACE` (or a project variable read once) asks for it. Keep the default path cheap.
- Install a report handler (`color_eyre::install()`, `miette`'s hook) once, at the top of `main`, in the binary only.
- `snafu` is an alternative to `thiserror` when most call sites need to attach context to the same underlying error: its context selectors make "this I/O error, while reading this path" one short expression. Use one of the two per crate.

**An error that crosses a process or language boundary is versioned data.** Its numeric code
and stable name are a wire contract.

```rust
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
#[repr(u32)]
pub enum WireCode {
    Unknown = 1,
    InvalidConfiguration = 2,
    ResourceNotFound = 20,
}

impl WireCode {
    pub fn from_u32(raw: u32) -> Self {
        match raw {
            2 => Self::InvalidConfiguration,
            20 => Self::ResourceNotFound,
            _ => Self::Unknown,
        }
    }
}
```

- Every variant has an explicit number. Never renumber or reuse one; retire it and leave a comment.
- **Decoding an unknown code yields `Unknown`, not a failure,** so an old client survives a new server.
- Send the code, a stable machine name and a human message as separate fields. Clients branch on the code, never on the message, which is then free to improve.
- Use the stable name in metrics and logs. *Not for* internal errors, which should stay free to change.

### Resilience patterns

**Retry as a decorator.** A wrapper that implements the same trait as the backend it holds
(`struct Retrying<B> { policy: RetryPolicy, inner: B }`) keeps retry out of every call site
and every backend. Wrap reads and writes separately: reads are usually safe to repeat, writes
only when the backend deduplicates them. One policy object serves the blocking, async and
streaming entry points, so their rules cannot drift.

**A circuit breaker records exactly one outcome per admitted call.**

| State | Behaviour |
|---|---|
| Closed | Calls pass; failures are counted |
| Open | Calls are rejected at once until the cooldown ends |
| Half-open | Exactly one probe is admitted; others are rejected with a retry-after |

```rust
pub enum Outcome {
    Success,
    Failure,
    /// Says nothing about the dependency's health.
    Neutral,
}

pub struct Permit<'a> {
    breaker: &'a Breaker,
    recorded: bool,
}

impl Permit<'_> {
    pub fn record(mut self, outcome: Outcome) {
        self.recorded = true;
        self.breaker.record(outcome);
    }
}

impl Drop for Permit<'_> {
    fn drop(&mut self) {
        if !self.recorded {
            self.breaker.record(Outcome::Neutral);
        }
    }
}
```

- **Caller cancellation, a caller-side timeout and a client error (a 4xx) are neutral.** They release the probe without changing health. Counting them as failures opens the breaker because of bad requests; never recording them wedges it half-open for ever.
- The permit's `Drop` guarantees a record on every path, including a cancelled future. Call sites never touch breaker state.
- Release the breaker's lock before awaiting the wrapped call.
- "Rejected because open" is its own error variant, distinct from the upstream failure, so callers and dashboards can tell them apart.
- Inject the clock. *Use for* remote dependencies that fail for a while; not for cheap local operations, where it only adds a failure mode.

**Partial failure across two systems is reported item by item.** An operation that changes
two durable systems (object storage and a metadata table) returns which items succeeded, which
failed on each side, and each side's error. One opaque error hides which system needs repair.

```rust
#[derive(Debug, thiserror::Error)]
#[error("deleted {} items; {} failed in storage, {} in metadata",
    .deleted.len(), .storage_failed.len(), .metadata_failed.len())]
pub struct DeleteError {
    pub deleted: Vec<ItemId>,
    pub storage_failed: Vec<(ItemId, StorageError)>,
    pub metadata_failed: Vec<(ItemId, MetadataError)>,
}
```

- Change the second system only for the items that succeeded in the first.
- Choose the order so that the leftover state after a crash is the harmless one: an orphaned blob can be garbage-collected, a metadata row pointing at nothing is a user-visible error.
- The same shape suits any batch API: return per-item results, not the first error.

### Error surfaces for callers

**Answer the caller's question with a method.** Callers want to know "was it not found?",
"should I retry?", "can I fall back?". Give them `is_*` methods, so they never match on
message text or on a dependency's error type.

```rust
impl Error {
    pub fn is_not_found(&self) -> bool {
        match self {
            Error::Pull { source: Some(source), .. } => source
                .downcast_ref::<RegistryError>()
                .is_some_and(RegistryError::is_not_found),
            _ => false,
        }
    }
}
```

- The dependency's error stays a boxed `#[source]`, out of your public API, so upgrading the dependency is not a breaking change for your callers.
- A probe built on `downcast_ref` breaks silently if the dependency changes its error type. Keep each probe small and cover it with a test that produces the real error.

**An API client's error carries what recovery needs as fields:** the HTTP status, the parsed
`Retry-After` delay, and the rate-limit limit, remaining count and reset time. Callers never
scrape strings. An empty or non-JSON error body still produces a sensible message that
includes the status. Rate-limit state is kept per credential, not in one global.

**Absent, unsupported and failed are three outcomes.** An optional converter, accelerator or
plugin lookup says which happened, and the fallback is a visible decision.

```rust
pub enum Conversion<T> {
    Converted(T),
    NoConverter,
    Unsupported(Reason),
    Failed(Error),
}
```

- Collapsing the last three into `None` hides real failures behind a silent fallback. If a fallback is taken, log or count the reason.
- A mandatory transformation's failure is an error, never a fallback.

**A plugin-facing error is a small stable type.** An extension trait returns a public error
with the few variants an extension can act on (a timeout with its duration, invalid input) and
an opaque `Other` for the rest. One `From<InternalError>` does the mapping, so internal errors
can change freely. *Not when* callers need the full internal error as a contract.

**Diagnostics that accumulate context.** In compilers, linters and language servers, an error
gains a file path, span, category and severity as it travels up. Build that into the error
type (`error.with_file_path(path).with_span(span)`), each call wrapping and keeping the
source, and decide at each `?` whether this layer knows something worth adding. The rendered
result still has one clear primary message. A plain internal error enum does not need this.

**Scoped panic context, for debugging only.** A thread-local stack of "what I am doing"
frames, printed by a panic hook installed once, turns a bare panic into one with a story.

```rust
let _ctx = panic_context::enter(format!("request: {method}"));
```

- The guard pops its frame on drop; `let _ = ...` would drop it at once.
- It is thread-local, so it does not follow an async task that moves between threads. There, use `tracing` spans.
- It explains crashes. It is not error handling and must not replace a `Result`.

### Errors on the wire

**One metadata trait and one envelope, when a machine acts on the error.** Errors that cross
an API, CLI or agent boundary need a stable code, a retry hint and a decision about what is
safe to show. Every domain error implements one trait; one envelope carries the fields.

```rust
pub trait ErrorData {
    fn code(&self) -> &'static str;
    fn retryable(&self) -> bool;
    /// Internal errors are not shown to external callers.
    fn internal(&self) -> bool;
    fn http_status(&self) -> u16 {
        500
    }
    /// What the caller can do about it.
    fn hint(&self) -> Option<String> {
        None
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ErrorEnvelope {
    pub code: String,
    pub message: String,
    pub retryable: bool,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub hint: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub context: Option<serde_json::Value>,
}
```

- **`code`, `retryable` and `internal` have no defaults,** so a new variant cannot be added without deciding them. Prefer a `match` with no wildcard arm, or a derive that generates one.
- **Two projections of one error.** The external one replaces an internal error's message with a generic text and a correlation ID; the detailed one goes to logs. The web framework's response conversion uses only the external one. An internal message reaching a client (a SQL fragment, a file path, a host name) is an information leak.
- **A table test covers every visible variant:** status, code, serialised shape and retry class. A snapshot of the envelope catches a renamed field.
- **A public code is a compatibility promise.** Put a new error in the narrowest existing class (client error, transient, server error); clients decide to retry from the class, never from the message.
- *Not for* a small private module, where `thiserror` and context are enough.

**Translate a generated client's errors once, at the SDK boundary.** An extension trait on the
generated `Result` maps into the house error type. A documented API error keeps its status,
code and source; a transport error becomes a communication error that is retryable for
connect and timeout failures. Do not flatten everything into one variant while a caller still
needs the status or the retry decision.

**Classify from the whole chain.** When errors are wrapped with context, the type that decides
retryability is the innermost one.

```rust
fn is_transient(error: &anyhow::Error) -> bool {
    error
        .chain()
        .find_map(|cause| cause.downcast_ref::<BackendError>())
        .is_some_and(BackendError::is_transient)
}
```

- Retry only what is explicitly temporary. A typed permanent error passes through unchanged; an unknown error is treated as permanent.
- In a stack of backends or plugins, one wrapper adds the operation, service and path as structured fields, and retry policy reads a typed field, never a substring.

### Recovery by error class

| Class | Where it arises | Recovery | Represent as |
|---|---|---|---|
| Validation | parsing, input edge | reject with the reason | typed parse or validation error |
| Business rule | domain workflow | reject with a precise outcome | named domain error or outcome enum |
| Transient external | network, storage, subprocess | retry with bounds, degrade, reschedule | retryable variant or flag |
| Permanent external | auth, contract or schema mismatch | fail fast, name the repair | typed permanent error |
| Timeout | async orchestration | fail, retry or cancel, explicitly | timeout error carrying the limit |
| Cancellation | task or workflow boundary | stop cooperatively, clean up | its own path, not a failure |
| Overload | queue, pool, stream | reject, shed or wait with a bound | explicit "saturated" result |
| Invariant breach | core logic | make impossible by construction, else fail fast | a narrow panic or an internal error |
| Clean-up failure | close, shutdown | explicit `close`, best-effort `Drop` | close error or shutdown report |
| FFI boundary | ABI, foreign ownership | convert, isolate or abort | the safe wrapper's error |

- **A message answers three questions:** what failed, where, and what the reader should do next.
- **If callers branch on it, give them structure; if they only pass it up, give them context.** Most errors are the second kind.
- Cancellation and overload are not failures of the operation and should not be logged or counted as such.
- A dependency's error type in your public signature makes its version part of your API. Wrap it or re-export it deliberately.

**Smaller rules.**

- **An undo log for in-memory mutations that need rollback.** Record each mutation's inverse as data (`enum UndoOp { CreateNode(NodeId), UpdateAttr { id, old } }`) and replay it backwards on failure. A new mutation kind adds its undo record in the same change; an exhaustive `match` enforces it. Use real transactions when the storage engine has them.
- **`no_std` errors:** implement `core::fmt::Display` by hand and `core::error::Error` directly (stable since Rust 1.81), or put `std::error::Error` behind a `std` feature on older toolchains.
- **Tests assert the variant or code, not message text,** so wording can improve. Retry tests assert behaviour (a permanent error is attempted once; the deadline stops the loop), not exact jittered delays.

### Errors at external edges

**Only "not found" selects the defaults.** A loader for an optional file opens it and matches
on the error kind. Do not test `exists()` first: the file can change between the check and
the read, and a permission error would be treated as absence.

```rust
fn load_rules(path: &Path) -> Result<Rules, LoadError> {
    match fs::read_to_string(path) {
        Ok(text) => Rules::parse(&text).map_err(LoadError::Parse),
        Err(error) if error.kind() == io::ErrorKind::NotFound => Ok(Rules::default()),
        Err(error) => Err(LoadError::Read(error)),
    }
}
```

- **A corrupt store is not an empty store.** A reader that returns "empty" for both a missing file and one that fails to parse lets the next write destroy the data. Absent means empty; unparsable is an error, or the file is moved aside before anything is written.
- **A reloaded configuration that fails to parse leaves the last good one in force.** Parse and validate fully, then swap; on failure, log and keep serving.
- Reading and parsing are two functions, so the parser is tested without a file system.

**Smaller rules.**

- **HTTP client: status first, then a typed decode, then a bounded snippet.** Check the status before treating the body as data. If decoding fails, the error carries the status and a length-capped piece of the body, never the whole payload and never an untyped value.
- **Read the OS error immediately.** After a failing libc or FFI call, `io::Error::last_os_error()` goes on the very next line, before any other call can overwrite `errno`.
- **A status variable assigned along the way starts as failure,** so an early return cannot report success.
- **A missing optional capability is a typed state.** Do not catch a load failure at start-up, print a warning and leave a `None` that every later use must check. Gate it with a Cargo feature, or return an explicit "unsupported" error when it is used.
- **A failure says how far it got** when that helps the caller: `CycleDetected { processed }`, `Truncated { read, expected }`.
- **A message takes its limit from the constant.** Format `MAX_SIZE` into the text; a literal "4 GB" beside the constant goes stale.
- **A structured variant, not a static string.** `InvalidInput { field, reason }` can name the offending value; `Invalid(&'static str)` cannot. A catch-all `Other(String)` belongs at an application edge, not in a library's public enum.
- **An error sent to a user interface has a short message and a separate detail,** so the UI can show a title and an expandable cause.
- **Distinct misses get distinct codes.** In a routed or distributed service, "no such resource", "not the leader" and "lease expired" lead a client to different actions (fail, re-route, retry), so they are different codes.
- **A drop-in replacement keeps the original's error contract:** the codes, the structured fields and any wording that callers are known to match on.
- **Three-valued logic is `Option` and `?`.** Write the inner computation to return `Option<T>` so a null operand short-circuits, and convert to the public error type in an outer function.

## 9. Async and concurrency

**Defaults.**

- **Never block the executor.** No blocking I/O, `std::thread::sleep`, long CPU work or blocking lock inside an async function. Blocking work goes to `spawn_blocking`; CPU-heavy work to a thread pool such as `rayon`.
- **Never hold a lock guard across `.await`.**
- **Everything is bounded:** channels, concurrency, retries, timeouts, buffers.
- **Every task has an owner** that can cancel it and learns how it ended.
- **Every long-running operation can be cancelled** and has a deadline.
- First ask whether you need async at all. A CLI, a build tool or a CPU-bound pipeline is usually simpler and as fast with threads. Async earns its place with many concurrent I/O waits.

### Blocking and locks

**How long is too long without an `.await`?** As a rule of thumb, more than about 100
microseconds of work between yield points starts to hurt other tasks' latency.

| Work | Where it runs |
|---|---|
| Short CPU work, non-blocking calls | inline in the task |
| Blocking I/O, a synchronous client, file-system calls | `tokio::task::spawn_blocking` |
| Heavy CPU work, parallel across cores | `rayon`, with the result sent back over a `oneshot` |
| A long-lived blocking loop | a dedicated `std::thread` |

- `spawn_blocking` tasks cannot be cancelled once started, and the pool is large but finite. Do not park an endless loop there.
- `tokio::fs` uses the blocking pool underneath. For many small file operations, one `spawn_blocking` around the whole batch is faster.

**Locks.**

```rust
// Wrong: the guard lives across the await.
let mut state = shared.lock().unwrap();
state.total += fetch_amount().await?;

// Right: await first, then lock briefly.
let amount = fetch_amount().await?;
shared.lock().unwrap().total += amount;
```

- **Use `std::sync::Mutex` (or `parking_lot`) for short critical sections, even in async code.** It is faster than an async mutex, and its guard is not `Send`, so the compiler rejects holding it across an `.await` in a spawned task.
- **Use `tokio::sync::Mutex` only when the guard must be held across an `.await`,** such as serialising access to a connection. Then ask whether a single owning task with a channel would be clearer.
- A guard in a temporary lives to the end of the statement, and in `if let` or `match` on editions before 2024 to the end of the block. When in doubt, bind the value you need and `drop(guard)` explicitly.
- The same rule holds for a `RefCell` borrow and for anything else that must be released: a pooled connection, a permit, a transaction.
- **Lock order:** when two locks are ever held together, one documented order, everywhere. Better, restructure so that no code holds two.

### Cancellation

**In async Rust, any `.await` is a point where the future may be dropped and never resumed.**
That happens on `select!`, on a timeout, when a `JoinHandle` is aborted, and when a client
disconnects.

- **A future is cancel-safe if dropping it between polls loses nothing.** `recv()` on a Tokio channel is. Reading "exactly n bytes" into a local buffer is not: the bytes already read vanish with the future.
- **In `select!`, keep state outside the branch futures.** A half-filled buffer or a half-advanced parser lives in a variable that survives the loop iteration; the branch only awaits the next piece.

```rust
let mut buffer = BytesMut::new(); // outlives each select! iteration
loop {
    tokio::select! {
        _ = shutdown.cancelled() => break,
        read = socket.read_buf(&mut buffer) => {
            if read? == 0 { break; }
            while let Some(frame) = try_parse(&mut buffer)? {
                handle(frame).await?;
            }
        }
    }
}
```

- **A multi-step change that must not be half-done** is either made atomic (one transaction, one message to an owning task) or run in a spawned task the caller waits on, so that dropping the caller does not stop it midway.
- **Clean-up after cancellation runs in `Drop`, which cannot `.await`.** Hand async clean-up to an owner task, or offer an explicit async `shutdown()` and treat `Drop` as the fallback.
- **Use a `CancellationToken` for cooperative shutdown.** Pass it down, check it in loops and `select!`, and give children `child_token()` so a subtree can be cancelled alone.
- Document, for every public async function, whether it is cancel-safe.

### Tasks and their owners

**A spawned task belongs to something that waits for it.** A detached `tokio::spawn` whose
handle is dropped keeps running, its panic goes unnoticed, and shutdown cannot wait for it.

```rust
let mut tasks = JoinSet::new();
for job in jobs {
    tasks.spawn(process(job));
}
while let Some(joined) = tasks.join_next().await {
    match joined {
        Ok(Ok(report)) => reports.push(report),
        Ok(Err(error)) => return Err(error), // dropping the set aborts the rest
        Err(join_error) => return Err(Error::TaskPanicked(join_error)),
    }
}
```

- `JoinSet` aborts its remaining tasks when dropped, so an early return does not leak work. A `JoinError` is a panic or an abort; handle it, do not `unwrap` it.
- **Bound the fan-out.** A `Semaphore` permit per task, or `futures::stream::iter(jobs).map(f).buffer_unordered(limit)` when the futures need not be spawned.
- **`join!` and `try_join!` for a fixed, small set** of futures on the current task: no spawn, no `'static` bound, borrowing allowed. `tokio::spawn` when the work should run in parallel on other threads or outlive the caller.
- **A background task for the life of the service** is held by the component that starts it: store the `JoinHandle` and the cancellation token, and have `shutdown()` cancel and then await it with a time limit.
- **Carry trace context across the spawn.** Do it in the project's one spawn helper, so tasks inherit the caller's span by default.

```rust
tokio::spawn(work().instrument(tracing::Span::current()));

let span = tracing::Span::current();
tokio::task::spawn_blocking(move || span.in_scope(blocking_work));
```

- **Threads:** name them (`thread::Builder::new().name(...)`), join them, and prefer `std::thread::scope` when they only need to borrow local data for a bounded time.

**A supervisor fails in-flight jobs before it restarts the worker.** A worker that can crash
(a thread, a child process, a WASM instance) has a supervisor holding a registry of pending
replies.

```rust
struct Supervisor {
    in_flight: HashMap<JobId, oneshot::Sender<Result<Output, WorkerError>>>,
    consecutive_restarts: u32,
}

impl Supervisor {
    fn on_worker_exit(&mut self) -> Result<(), WorkerError> {
        for (_, reply) in self.in_flight.drain() {
            let _ = reply.send(Err(WorkerError::Crashed)); // the caller may have gone away
        }
        self.consecutive_restarts += 1;
        if self.consecutive_restarts > MAX_RESTARTS {
            return Err(WorkerError::GaveUp);
        }
        self.spawn_worker()
    }

    fn on_worker_ready(&mut self) {
        self.consecutive_restarts = 0; // only a successful start resets the count
    }
}
```

- **A clean error beats a future that never completes.** Jobs are failed, not replayed: only the caller knows whether a retry is safe.
- Restart with backoff and a cap. A worker that dies at start-up must not be restarted in a tight loop.
- Per-job resources are freed by an owning guard's `Drop`, so the crash path releases them too.

**A timeout does not mean the work stopped.** Dropping a timed-out future stops async work at
its next `.await`, but a `spawn_blocking` closure, a thread or a child process carries on.

```rust
match self.running.get(&job) {
    Some(handle) if !handle.is_finished() => return Tick::StillRunning, // skip this tick
    Some(_) => {
        self.running.remove(&job);
    }
    None => {}
}
let handle = tokio::task::spawn_blocking({
    let job = job.clone();
    move || run(job)
});
self.running.insert(job, handle);
```

- For a periodic job, skip the tick while the previous run is alive, or runs pile up on the same data.
- For work that must stop, give it a flag or token it checks, or run it in a child process that can be killed.
- Report "timed out, still running" differently from "failed".

### Shared state and primitives

| Need | Use |
|---|---|
| One producer of work, many async consumers of results | `tokio::sync::mpsc` (bounded) |
| One reply to one request | `tokio::sync::oneshot` |
| The latest value; readers may skip intermediate ones | `tokio::sync::watch` |
| Every subscriber sees every message | `tokio::sync::broadcast` (slow receivers get `Lagged`) |
| Limit concurrency | `tokio::sync::Semaphore` |
| Wake a waiter without data | `tokio::sync::Notify` |
| Threads, not tasks; multi-consumer; `select` | `crossbeam-channel` or `flume` |
| Initialise once | `OnceLock`, `LazyLock`, `tokio::sync::OnceCell` for async |

- **Bounded channels by default.** An unbounded queue turns overload into memory growth that shows up far from its cause. A full bounded channel makes the producer wait or fail, which is the signal you want. Decide which: `send().await` waits, `try_send` sheds.
- **Do not call a blocking channel operation in async code,** and use `blocking_send` to feed a Tokio channel from a thread.
- **Prefer one owning task and messages to a shared lock** when state has a lifecycle or multi-step updates. Callers hold a cheap handle with a sender; each request carries a `oneshot` for the reply. A plain `Mutex` is still right for a small map with short updates.
- **Atomics: choose the ordering by argument.** `Relaxed` for a counter nobody synchronises on. `Acquire`/`Release` when a store publishes data another thread then reads. `SeqCst` when several atomics must be seen in one global order, or when you cannot yet make the argument. A wrong `Relaxed` passes every test on x86 and fails on ARM.
- **Two atomics are not one atomic state.** If two values must change together, use one atomic holding both, or a lock.
- **Globals:** `LazyLock` for an immutable table or compiled regex is fine. Global mutable state leaks between tests and hides dependencies; pass it in.

**Model-check small lock-free pieces with `loom`.** One passing run of a concurrent test
proves little. `loom` runs a small model under every interleaving and weak-memory behaviour.

```rust
#[test]
#[cfg(loom)]
fn two_increments_are_both_counted() {
    loom::model(|| {
        let counter = Arc::new(Counter::new());
        let other = Arc::clone(&counter);
        let handle = loom::thread::spawn(move || other.increment());
        counter.increment();
        handle.join().unwrap();
        assert_eq!(counter.get(), 2);
    });
}
```

- Keep the model tiny: two or three threads, a few operations. The state space grows explosively.
- The code under test must use `loom`'s atomics and locks when built with `--cfg loom`, usually through one small `sync` module of re-exports.
- For ordinary lock-based code, a stress test under ThreadSanitizer and a look at lock order are better value.

### Concurrency patterns

**Fan out, tag, merge in order.** Workers compute from an immutable input and never touch the
shared structure. Each result carries its identity; one merge step applies them in a
deterministic order.

```rust
let mut tasks = JoinSet::new();
for (index, item) in items.into_iter().enumerate() {
    let limit = Arc::clone(&limit);
    tasks.spawn(async move {
        let _permit = limit.acquire_owned().await.expect("semaphore is never closed");
        (index, analyse(item).await)
    });
}

let mut results = Vec::new();
while let Some(joined) = tasks.join_next().await {
    results.push(joined?); // a JoinError is a panic, kept apart from a domain error
}
results.sort_by_key(|(index, _)| *index);
```

- **Take the permit inside the task,** so every task is spawned and the semaphore alone decides how many run. Size it from the scarce resource (memory, connections, CPU), not from a worker count.
- Completion order is not input order. Sort by the tag when order matters; output that depends on scheduling is a flaky test and an irreproducible build.
- **For CPU-bound passes over a shared structure,** each `rayon` worker builds its own diff (`fold`), diffs are merged (`reduce`), and one apply step mutates at the end. The merge must be associative and order-independent, or the merged diff is sorted before applying. *Not when* later items must see earlier mutations.
- **A sequential and a parallel form of the same kernel** (a plain update and a `compare_exchange` update) must be semantically identical. Test them against each other on the same input.
- **Build the index first.** Linking records by repeated linear search is quadratic; one pass builds the key-to-parent map.

**Do slow work outside the lock, then recheck.** Construction, I/O and repair never happen
under a broad lock.

```rust
if let Some(found) = self.pool.read().get(&key) {
    return Ok(Arc::clone(found));
}
let fresh = Arc::new(Connection::open(&key).await?); // no lock held
let mut pool = self.pool.write();
Ok(Arc::clone(pool.entry(key).or_insert(fresh))) // another caller may have won
```

- The loser of the race discards its duplicate. That is acceptable when construction is cheap enough to waste occasionally.
- **When it is not, use single-flight:** cache the in-flight initialisation, so concurrent callers share one load. A map from key to `Arc<tokio::sync::OnceCell<T>>` with `get_or_try_init` does this.
- **Decide what a failed initialisation does.** `get_or_try_init` leaves the cell empty, so the next caller retries, which under a persistent failure is a retry per request; add backoff or cache the failure briefly.
- **After re-acquiring, revalidate.** The entry may have been removed, replaced or shut down while the lock was released.
- **Lazy construction moves failures from start-up to first use.** Good for optional or numerous backends; for a required dependency, connect at start-up so a bad configuration fails the deploy, not the first request.

**Backpressure and loss are decisions, written down.**

- **Bound by the unit that costs.** When messages vary widely in size, a count-bounded channel bounds nothing. Reserve capacity in bytes, rows or tokens before sending (a `Semaphore` with `acquire_many` does it), and define what happens to one item larger than the whole limit.
- **With `Notify`, create the `notified()` future, recheck the condition, then await,** so a wake-up between the check and the wait is not lost.
- **A lossy queue says so.** Best-effort work (cache warming, compaction hints, telemetry) may `try_send` and drop when full. Comment that it is lossy, count the drops in a metric, and add a periodic full pass if freshness matters. Never for anything durable, billed or user-visible.
- **Supersedable events coalesce; semantic events do not.** For progress updates and text deltas, keep only the latest pending one per class when the output is full. Before sending a semantic event (start, end, error), flush the pending ones so order holds.
- **Latest-state streams are `watch`:** a subscriber gets the current value at once, then changes, and may skip intermediate values. Right for a dashboard, wrong for an audit trail.
- **Debounce file events into stable batches.** Track each path's last event time, flush only paths quiet for the delay, keep deletions and modifications consistent (a delete cancels a pending modify and the reverse), and flush what remains on shutdown.
- **One writer task behind a bounded channel** owns the file or log, batches, and flushes the remainder when the channel closes. Do the expensive encoding before queueing, not in the writer.

**Lifecycle as explicit states.** A long-running job whose phases have different event loops
is clearer as one type per state, each returning the next, than as one loop with a status
flag.

```rust
pub enum Transition {
    Stop,
    Advance(Box<dyn State>),
}

#[async_trait]
pub trait State: Send {
    async fn next(self: Box<Self>, ctx: &mut JobContext) -> Result<Transition, StateError>;
}
```

- Each state owns its `select!` loop; allowed transitions are visible in the return values. For a short handler, a plain enum and a `match` is enough.

**Shutdown and restart.**

- **Shutdown has a deadline.** Stop accepting work, cancel, wait for tasks to drain or checkpoint under a timeout, then exit and log what was abandoned. A shutdown that waits for ever is a hang; one that does not wait loses work.
- **Race a CLI command against Ctrl-C** in `select!`; cancellation is a typed outcome with its own exit code.
- **Classify persisted recovery state before reloading it.** Durable policy and operator-visible history are kept. Per-process control state (failure counts, an exhausted retry budget, an open breaker) is reset, or a restarted process inherits a failure it has not experienced. Pair the reset with crash backoff so a crash loop does not hammer dependencies.
- **A "set if absent, with expiry" marker** returns whether this caller won. It suits idempotent "only one starts" jobs. It is not a lock: strict mutual exclusion needs a fencing token checked by the resource.
- **A concurrency limit from configuration** is `Option<Arc<Semaphore>>`; the unit of work holds an `OwnedSemaphorePermit`, so release happens on every path, including cancellation.

**Smaller rules.**

- **A timeout on every external call,** and one overall deadline passed down, so nested timeouts do not add up past what the caller will wait.
- **Stdio servers:** blocking threads own stdin and stdout; bounded channels connect them to the async loop.
- **Streaming HTTP clients** (server-sent events): check the status first, buffer across chunks, split only on complete lines. A line or a UTF-8 character can span two chunks.
- **Validate a stream's contract before returning it** (schema, arity), then adapt every item the same way; fail once at the start, not on each item.
- **Never read mutable UI or editor state across an `.await`.** Take an immutable snapshot, work on it off the main thread, and apply the result in one update after checking it is not stale.
- **A library accepts a runtime handle** instead of creating its own runtime.

### An owning task (the actor pattern)

One task owns the state; everyone else holds a cheap handle and sends typed messages. There is
no lock, the state's lifecycle is the task's, and every operation is one message, so multi-step
updates cannot interleave.

```rust
enum Command {
    Get {
        key: Key,
        reply: oneshot::Sender<Option<Value>>,
    },
    Put {
        key: Key,
        value: Value,
        reply: oneshot::Sender<Result<(), StoreError>>,
    },
}

#[derive(Clone)]
pub struct StoreHandle {
    commands: mpsc::Sender<Command>,
}

impl StoreHandle {
    pub fn spawn(capacity: usize) -> (Self, JoinHandle<()>) {
        let (commands, inbox) = mpsc::channel(capacity);
        let task = tokio::spawn(run(Store::default(), inbox));
        (Self { commands }, task)
    }

    pub async fn get(&self, key: Key) -> Result<Option<Value>, StoreError> {
        let (reply, response) = oneshot::channel();
        self.commands
            .send(Command::Get { key, reply })
            .await
            .map_err(|_| StoreError::Stopped)?;
        response.await.map_err(|_| StoreError::Stopped)
    }
}

async fn run(mut store: Store, mut inbox: mpsc::Receiver<Command>) {
    while let Some(command) = inbox.recv().await {
        match command {
            Command::Get { key, reply } => {
                let _ = reply.send(store.get(&key)); // the caller may have given up
            }
            Command::Put { key, value, reply } => {
                let _ = reply.send(store.put(key, value));
            }
        }
    }
    // Every handle is gone: flush and release here.
}
```

- **Messages are a typed enum, one variant per operation.** A generic "run this closure on the state" message gives back the unstructured access the pattern was meant to remove.
- **The mailbox is bounded,** so a slow actor slows its callers instead of growing memory.
- **The loop ends when every handle is dropped;** that is the shutdown path, and the place for final clean-up. Keep the `JoinHandle` so something can wait for it.
- **Both the send and the reply can fail** (the actor stopped or panicked). The handle maps both to an error; it never `unwrap`s.
- **Do not do slow work in the loop.** While the actor awaits an HTTP call, every other message waits. Spawn the slow part and have it send its result back as a message.
- **Two actors that await each other's replies can deadlock** exactly like two locks. Keep the call graph between actors acyclic, or use one-way messages.
- *Use a `Mutex` instead* for a small piece of state with short, independent updates. An actor is worth its ceremony when the state has a lifecycle, owns I/O, or needs operations to be serialised.

**`select!` details.**

- Branches are polled in random order by default, which is fair. `biased;` polls them top to bottom: put shutdown first so it is noticed promptly, and be aware that a branch that is always ready then starves those below it.
- A branch whose future is created inside the loop is created afresh each iteration. A timer that should span iterations (`sleep`, `interval`) is created outside and pinned.
- Use a `CancellationToken`, not a shared boolean: a flag cannot wake a task that is waiting on something else.

### Threads

**Scoped threads borrow; no `Arc` and no `'static` needed.** Every thread spawned in the
scope is joined before it returns, so borrowing local data is sound.

```rust
let (left, right) = data.split_at_mut(data.len() / 2);
let (sum_left, sum_right) = thread::scope(|scope| {
    let a = scope.spawn(|| process(left));
    let b = scope.spawn(|| process(right));
    (a.join(), b.join())
});
```

- Split mutable data into disjoint parts first (`split_at_mut`, `chunks_mut`); each thread then owns its part exclusively. Do not wrap data in `Arc<Mutex<_>>` only to satisfy a `'static` bound.
- **`join()` returns `Err` if the thread panicked.** Decide what that means: propagate it, or record it. An unjoined, unnamed thread that panics is a silent loss of work.
- For "apply this to every item in parallel", `rayon`'s `par_iter` is less code and balances load. Keep I/O out of the `rayon` pool; a blocked worker stalls unrelated parallel work.
- **Async has no equivalent of a borrowing scope.** A spawned Tokio task must be `'static`. To run borrowing futures concurrently, keep them on the current task with `join!` or `FuturesUnordered`.

**Thread-side channels and locks.**

- `std::sync::mpsc` is enough for many producers and one consumer. For several consumers, `select` over channels, or timers and deadlines, use `crossbeam-channel` or `flume`. Pick one family per project.
- **Every receive loop handles disconnection.** A `recv` error means all senders are gone and is the normal way a worker learns to stop. Dropping the last sender is the shutdown signal; a clone kept alive by accident is a worker that never exits.
- **A zero-capacity (rendezvous) channel** makes the producer wait until the consumer takes the item; a small capacity throttles. `send_timeout` gives a producer a bounded wait and a point at which to shed load. Never busy-wait in place of a blocking receive.
- **`parking_lot` locks** are smaller, do not poison, and can be faster under contention; `std`'s are good since 1.62 and need no dependency. Choose from a measurement, and use one kind per project so guards and conventions are not mixed.
- **Poisoning:** a `std` mutex is poisoned when a holder panicked, since the data may be half-updated. `lock().unwrap()` spreads the panic, which is right when the invariant may be broken. Recover with `into_inner` only where every critical section leaves the data valid at each step.

**Runtime choice.** Tokio is the default and has the ecosystem. Other runtimes
(single-threaded, or thread-per-core over `io_uring`) are specialist choices that follow from
a measured need. Do not mix runtimes in one process without a clear boundary: a future built
on one runtime's I/O types generally fails on another. A library should depend on `futures`
traits and take the runtime's pieces from its caller where it can.

### Atomics and lock-free code

**A read followed by a write is not atomic, whatever the orderings.**

```rust
// Lost update: two threads can both read 5 and both store 6.
let current = counter.load(Ordering::Acquire);
counter.store(current + 1, Ordering::Release);

// One atomic operation.
counter.fetch_add(1, Ordering::Relaxed);

// A conditional update: retry until no one else changed it in between.
let mut current = high_water.load(Ordering::Relaxed);
while candidate > current {
    match high_water.compare_exchange_weak(
        current,
        candidate,
        Ordering::Relaxed,
        Ordering::Relaxed,
    ) {
        Ok(_) => break,
        Err(actual) => current = actual,
    }
}
```

- Use the single-operation forms: `fetch_add`, `fetch_max`, `fetch_update`, `swap`, `compare_exchange`. Orderings govern what other memory becomes visible; they do not join two operations into one.
- `compare_exchange_weak` may fail spuriously and belongs in a loop; the strong form is for a single attempt.
- **A fence or an atomic store does not make plain data shareable.** Non-atomic mutable state reached from two threads needs a lock or an atomic of its own, or it is a data race and undefined behaviour.
- **Do not hand-roll a spin lock, a lock-free queue or memory reclamation.** Use `Mutex`, `crossbeam`'s queues and deques, `crossbeam-epoch` for deferred reclamation, and `AtomicCell` for a small `Copy` slot. Freeing a node another thread may still be reading is the classic lock-free bug, and it passes most tests.
- **Lock-free is not automatically faster.** An uncontended mutex costs a few nanoseconds. Go lock-free only when a profile shows contention on that lock, and after trying to shrink the critical section, shard the data, or give each thread its own copy.
- A `loom` test joins its threads and asserts the invariant; without the assertion it checks nothing. No timers, randomness or I/O inside the model.
- `std::sync::OnceLock` and `LazyLock` replace `lazy_static!` and most of `once_cell`; reach for the crates only to support an older toolchain.

### Locks and scheduling at scale

- **Several keyed locks are taken in one global order.** Sort the keys, lock in that order, keep the guards together and release them together. No call site picks its own order. Striped locks cap the number of locks at the price of unrelated keys sharing a stripe.
- **`rayon` for CPU-bound loops over large collections.** Items must be independent, with no locks and no I/O inside. Do not parallelise tiny tasks: below roughly a microsecond of work per item, the scheduling overhead wins. Measure the speed-up; memory-bound loops often do not scale.
- **A hand-built work-stealing pool** (a global injector plus a deque per worker, from `crossbeam-deque`) is for building a scheduler. Application code should use `rayon` or the async runtime, which already are one.
- **Double-buffered work sets.** An iterative scheduler keeps a current and a next set and swaps them at the start of each round (`mem::swap(&mut current, &mut next); next.clear();`), so work scheduled during a round cannot change the set being consumed, and both allocations are reused.
- **The scheduler owns the cross-cutting concerns:** dependency order, timeouts, error propagation and removal of failed work. A task exposes `run` and its dependencies; it does not start its dependents itself.
- **An engine with user callbacks** owns loading, scheduling and iteration; user code implements a trait with one required method and a few defaulted hooks. Add a hook only when an algorithm needs it: an empty default can hide a step that an implementer should have handled.

### Shared resources that are slow to create

**One key, two states: connecting and connected.** When a miss starts slow async set-up, the
map holds both states under the key, and the decision is taken under the lock as a plain
value. All awaiting happens after the guard is gone.

```rust
enum Slot {
    Connecting(watch::Receiver<()>),
    Connected(Arc<Tunnel>),
}

enum Action {
    Use(Arc<Tunnel>),
    Wait(watch::Receiver<()>),
    Connect(watch::Sender<()>),
}

let action = match self.slots.lock().expect("slot map poisoned").entry(key.clone()) {
    Entry::Occupied(slot) => match slot.get() {
        Slot::Connected(tunnel) => Action::Use(Arc::clone(tunnel)),
        Slot::Connecting(ready) => Action::Wait(ready.clone()),
    },
    Entry::Vacant(slot) => {
        let (done, ready) = watch::channel(());
        slot.insert(Slot::Connecting(ready));
        Action::Connect(done)
    }
};
// The guard ended with the statement above.
```

- **If the connecting caller fails or is cancelled, a drop guard removes the `Connecting` entry.** Without it, every waiter waits for ever. This is the part most often missed.
- **Waiters look the key up again after being woken;** the attempt may have failed and the entry gone.
- The entry is removed when its last user releases it, or by an idle timeout.
- *Do not share* when callers need separate credentials, quotas or independent cancellation.

**A `Mutex<()>` can serialise an external side effect.** For "download once, then everyone
reads", probe without the lock, take the lock, probe again, then do the work. The second probe
is what makes concurrent first use perform one download. In a service, bound the wait with a
timeout, since the lock hides a long operation.

**Never run a callback while holding your own lock.** A timer or delayed-task scheduler keeps
a heap of due times (`BinaryHeap<Reverse<(Instant, TaskId)>>`) under a mutex that guards only
the heap. It pops the due task, drops the guard, runs the callback, and locks again. A
callback that schedules or cancels would otherwise deadlock, and a slow one would block every
insertion. Say what cancelling a task that is already running does: wait for it, or report
that it was too late.

**Active and pending copies.** Readers use a stable active structure while a replacement is
prepared on the side. A change clones the active copy into pending if there is none and
edits only pending; promotion swaps it in atomically (`ArcSwap`, or a short write lock) and
fixes everything that referred to the old copy in the same step. Readers never see a half
built structure. The cost is two copies in memory during preparation.

**Multi-key batches take their locks in key order, before anything else.** Keep the batch in
a `BTreeMap` so it iterates in lock order; acquire every lock; only then start the change.
Keep the phases apart (lock, mutate, publish, mark dirty), and bound the batch size, since a
large batch holds many locks. Where persistence progress has several stages, model them as an
enum keyed by epoch and object, and assert that a final state is never overwritten. This is
storage-engine machinery; a simple cache needs none of it.

**A scoped thread-local restores the previous value.** A guard that sets ambient context at a
callback or FFI boundary puts back what was there before, so nested scopes unwind correctly.

```rust
thread_local! {
    static CURRENT: Cell<Option<Tracker>> = const { Cell::new(None) };
}

pub struct TrackerGuard {
    previous: Option<Tracker>,
}

impl TrackerGuard {
    pub fn enter(tracker: Tracker) -> Self {
        Self { previous: CURRENT.with(|cell| cell.replace(Some(tracker))) }
    }
}

impl Drop for TrackerGuard {
    fn drop(&mut self) {
        CURRENT.with(|cell| cell.set(self.previous.take()));
    }
}
```

- Clearing instead of restoring breaks the outer scope as soon as two are nested.
- Thread-local context does not follow an async task across threads; use `tokio::task_local!` or pass the value explicitly.
- Ambient context is a hidden parameter. Prefer an explicit argument, and keep thread-locals for boundaries where the signature is not yours to change.

### Checking lock order, and CPU-parallel loops

**Lock ranks, checked in debug builds.** When a component has more than a handful of locks,
"one documented order" stops being checkable by reading. Give each lock a rank and assert on
every acquisition that it is higher than every rank the thread already holds.

```rust
#[cfg(debug_assertions)]
thread_local! {
    static HELD: RefCell<Vec<LockRank>> = const { RefCell::new(Vec::new()) };
}

pub struct RankedMutex<T> {
    rank: LockRank,
    inner: Mutex<T>,
}

pub struct RankedGuard<'a, T> {
    guard: MutexGuard<'a, T>,
    rank: LockRank,
}

impl<T> RankedMutex<T> {
    pub fn lock(&self) -> RankedGuard<'_, T> {
        // Checked before blocking, so a violation panics instead of deadlocking.
        #[cfg(debug_assertions)]
        HELD.with(|held| {
            let mut held = held.borrow_mut();
            assert!(
                held.iter().all(|other| *other < self.rank),
                "lock order violation: {:?} taken while holding {:?}",
                self.rank,
                held
            );
            held.push(self.rank);
        });
        RankedGuard {
            guard: self.inner.lock().unwrap_or_else(PoisonError::into_inner),
            rank: self.rank,
        }
    }
}

impl<T> Drop for RankedGuard<'_, T> {
    fn drop(&mut self) {
        #[cfg(debug_assertions)]
        HELD.with(|held| {
            let mut held = held.borrow_mut();
            if let Some(position) = held.iter().rposition(|other| *other == self.rank) {
                held.remove(position);
            }
        });
    }
}
```

- The check fires on the first run that takes locks in a bad order, even when no deadlock happens that time. That is its whole value: a deadlock needs an unlucky interleaving, a rank violation does not.
- Every lock gets a rank when it is added. One unranked lock makes the check meaningless.
- It is per-thread, so it does not see a guard held across `.await` on another thread; that case is already forbidden.
- For two or three locks, a comment stating the order is enough.

**Per-thread accumulators, one merge.** A counter, map or histogram updated inside a parallel
loop becomes one accumulator per worker, merged at the end, instead of a lock or atomic
touched on every iteration.

```rust
let histogram = items
    .par_iter()
    .fold(Histogram::default, |mut local, item| {
        local.record(item);
        local
    })
    .reduce(Histogram::default, Histogram::merge);
```

- The identity must be a true identity and the merge associative. `rayon` splits the work differently on each run, so a merge that depends on grouping gives different answers on different runs. Floating-point sums are the usual trap: they are not associative, so parallel totals differ in the last bits.
- *Not when* updates need one global order.

**Index-stealing workers** are the dependency-free form of the same thing: a shared atomic
"next index" hands each item out exactly once and balances uneven items without pre-split
ranges.

```rust
let next = AtomicUsize::new(0);
let per_worker: Vec<Vec<(usize, Output)>> = thread::scope(|scope| {
    let handles: Vec<_> = (0..workers)
        .map(|_| {
            scope.spawn(|| {
                let mut local = Vec::new();
                loop {
                    let index = next.fetch_add(1, Ordering::Relaxed);
                    let Some(item) = items.get(index) else { break };
                    local.push((index, process(item)));
                }
                local
            })
        })
        .collect();
    handles
        .into_iter()
        .map(|handle| handle.join().expect("worker panicked"))
        .collect()
});
```

- Results carry their index and are sorted after the merge when order matters. `Relaxed` is correct here: `fetch_add` is atomic, and nothing else is published through the counter.
- Run serially when there are few items or one worker. Not for dependent jobs or ordered execution.

**Smaller rules.**

- **Write the algorithm against an execution policy** with a sequential and a parallel adapter over the same body. Tests run the sequential one, which separates "the algorithm is wrong" from "the scheduling is wrong". Abstract the execution, never the data model.
- **Chunked CPU work** sizes chunks as `ceil(items / threads)` clamped to a minimum and maximum, and gives each worker a stable index for its scratch buffers. **Cancellation stops pulling new chunks;** discarding results while the work continues is not cancellation.
- **Parallel workers, one writer.** Workers send whole results to a single thread that owns the `BufWriter`, so output lines never interleave.
- **A metric or timer guard records in `Drop`,** so early returns and `?` are covered. Held across an `.await`, it also times the suspension, which may or may not be what you want to measure.
- **An `accept` error does not end the server.** Log it and continue, with a short pause on resource exhaustion (`EMFILE`) so the loop does not spin. Only a bind failure is fatal. Each connection is handed off under a concurrency bound, so one slow client cannot block the next accept.
- **A lock held in a database row** for long background work records the owner, what is locked and a heartbeat the holder refreshes, so a stale lock can be detected and explained. A constraint enforces the single row. It is a single-host convenience, not a distributed lock.
- **State for a callback whose signature cannot carry it** may go in a `thread_local!` `RefCell`, set before the call and read inside. Keep borrows short and never hold `borrow_mut` across a call that may re-enter. Valid only while the whole call runs on one thread.

### Cancellation, saturation and shutdown as contracts

**Say what each long-running operation does when it is cancelled:** cancel-safe (nothing is
lost), restartable (safe to run again from the start), resumable (continues from a persisted
point) or lossy. If partial progress matters, persist the intent before acting, so an
interruption leaves something to resume from and not a silent half-change.

**Name the saturation policy.** When producers can outpace consumers, the choices are: make
the producer wait, reject, shed the oldest or newest, batch, or spill to durable storage.
"The queue should stay small" is not a policy. One unbounded producer anywhere defeats every
bounded channel downstream of it.

**The shutdown contract** states who starts it, how the signal reaches every task, how
completion is awaited, and that calling it twice is harmless.

- **Rust has no async destructors.** Clean-up that must be awaited (flush, close a protocol properly, deregister) is an explicit `async fn shutdown(self)`. It belongs in the API documentation and in a test; `Drop` is the best-effort fallback.
- **At shutdown, every accepted job has a known fate:** it ran, or it was closed without running and its submitter was told. Nothing is left silently in a queue.
- `tokio_util` supplies the pieces: `CancellationToken` (with `drop_guard()`, so that dropping an owner cancels its group) and `TaskTracker` (wait until every tracked task has finished). Prefer them to a hand-built guard with a reference count and a channel; a `JoinSet` is enough when one owner spawns and joins.
- **Test shutdown under load.** Inject cancellation while messages are in flight and assert that none is lost or handled twice. It is where bounded channels, tokens and cancel-safe branches either work together or fail together.

**Retries interact with cancellation.** A retry loop around a future that is not cancel-safe
re-enters half-consumed state on each attempt. The hazards: a timeout after the remote effect
already happened, a library retry nested inside an application retry, cancellation between
an effect and its acknowledgement, and a backoff that outlasts the caller's deadline. Keep
the first error as well as the last; the first usually names the cause.

**Do not hold a span guard across `.await`.**

```rust
// Wrong: the span stays "entered" on this thread while the task is suspended,
// so unrelated tasks polled here are recorded inside it.
let _entered = span.enter();
fetch().await;

// Right.
fetch().instrument(span).await;
```

- Useful telemetry follows the design: each task's parent and how it ended, queue depth beside its capacity, and cancellation recorded as its own outcome and not as an error. Metric labels never come from user input, since each distinct value is a new time series.

### More queue and event patterns

**The capacity permit travels with the queued item.**

```rust
pub struct Queued {
    pub message: Message,
    // Held only for its Drop: returns the capacity when the item is dropped.
    _capacity: OwnedSemaphorePermit,
}
```

- Capacity is returned wherever the item ends up: processed, discarded or cancelled. The field looks unused and is load-bearing, so the comment stays.
- **Count what is sent but not yet acknowledged.** A send queue limited by bytes must include batches awaiting acknowledgement, or memory is unbounded while the peer is slow.
- **Admit before enqueueing.** Ask the admission policy first, make room second, and increase the running count immediately before the spawn. Then a task that never runs cannot have displaced accepted work or leaked a count. Anything held while waiting is released by a guard, so cancellation of the wait releases it.

**`try_send` from a thread that must not block.** A blocking send from an event-loop or
reactor thread onto a full inbox parks the thread that drives everything else.

```rust
match inbox.try_send(message) {
    Ok(()) => {}
    Err(TrySendError::Full(_)) => {
        dropped.increment(1);
        warn!(shard, "inbox full, message dropped");
    }
    Err(TrySendError::Closed(_)) => return Err(Error::ShardStopped { shard }),
}
```

- A dropped message needs a written recovery path (retransmission, a log to replay). Without one, this is data loss with a log line.

**Discard results from superseded requests.** For typeahead, search or preview, cancelling
the previous request is not enough: its result may already be on the way.

```rust
let generation = self.latest.fetch_add(1, Ordering::Relaxed) + 1;
let results = search(&query).await;
if generation == self.latest.load(Ordering::Relaxed) {
    self.show(results); // otherwise a newer request has started; drop this one
}
```

- Use an ordered queue instead when every request must complete.
- **Coalesce level-triggered state, never edge-triggered events.** "Needs a rerun" can be merged into one flag. One-shot triggers and queued items must each be kept, or they are lost.
- **A guard can signal completion on every exit path** by sending in `Drop`. It cannot tell success from failure from cancellation, so use it only where "finished, somehow" is the whole message.

**One event enum drives a terminal UI or long-running client.** Ticks, input and loaded data
become one stream consumed by one state machine.

```rust
pub enum Event {
    Key(KeyEvent),
    Tick,
    Loaded(Result<Data, LoadError>),
}

loop {
    let event = tokio::select! {
        _ = ticker.tick() => Event::Tick,
        Some(key) = keys.recv() => Event::Key(key),
        Some(loaded) = results.recv() => Event::Loaded(loaded),
    };
    if app.update(event) == Flow::Quit {
        break;
    }
    terminal.draw(|frame| app.render(frame))?;
}
```

- A new action is a new variant handled in `update`. Rendering reads state and performs no I/O; loading happens in tasks that report back as events.
- Bound the channel or coalesce ticks, or a slow render builds an unseen backlog.
- *Not when* the UI framework already owns the event loop.

**Smaller rules.**

- **An in-process event broker** keys subscriptions by event type, returns a `#[must_use]` handle that unsubscribes on drop, keeps payloads cheap to clone, and bounds what a slow subscriber can hold up. Not for cross-process or durable delivery.
- **A resource that is expensive or not thread-safe belongs to one worker;** only job payloads cross the queue, and failures come back through the job's result. Cancellation covers queued and in-flight jobs alike.
- **Blocking reads behind an async API** run in `spawn_blocking` under a configurable semaphore. Too many permits overload the storage; too few slow every reader.
- **Round-robin by `fetch_add(1, Relaxed) % len`** is fine for spreading load over candidates that are already filtered. A least-loaded picker rotates its ties, or the first candidate always wins.
- **Bridging to a foreign event loop** (a UI loop, another language's runtime): the Rust future holds a guard that cancels the foreign task if dropped early, and all calls into the foreign loop go through its thread-safe entry point. Prefer a maintained adapter crate to a hand-written bridge.

### Streams, hedging and tight loops

**Hedged requests, for idempotent reads only.** Start the primary; start a backup on another
replica only if the primary has not answered after a grace period. The first success wins.

```rust
let primary = fetch(replica_a, &key);
tokio::pin!(primary);

tokio::select! {
    result = &mut primary => match result {
        Ok(value) => return Ok(value),
        Err(_) => return fetch(replica_b, &key).await, // failed early: fall back now
    },
    _ = tokio::time::sleep(grace) => {}
}

tokio::select! {
    Ok(value) = &mut primary => Ok(value),
    Ok(value) = fetch(replica_b, &key) => Ok(value),
    else => Err(Error::BothReplicasFailed),
}
```

- Set the grace period near the 95th-percentile latency, so only the slow tail is duplicated: a few per cent more load for a much shorter tail.
- Dropping the loser cancels it locally; the remote server may still do the work.
- **Never hedge a write or anything with a side effect.** Never hedge into an overloaded cluster: the duplicates make the overload worse. Cap hedges as a fraction of traffic.

**A stream ends when its channel closes.** Turning a blocking producer (a database cursor, a
directory walk) into an async stream: a thread or `spawn_blocking` task sends items on a
bounded channel and the receiver is the stream.

- The end is the last sender being dropped, which also happens on early return and on panic. Never an in-band magic value that a real item could equal. If "finished cleanly" must be distinguished from "producer died", send `Result` items and a final explicit `Done`.
- The producer stops when the send fails, which means the consumer went away. That is the cancellation path, so check every send.
- Fan-out width comes from an explicit limit, never from the size of the input.
- A small result-set type over a stream offers `one`, `all` and the raw stream, with an idempotent `close` and a terminal error that can still be read after the drain.

**Check for cancellation every N iterations of a tight loop.** Synchronous CPU work cannot be
dropped like a future; it has to look.

```rust
const CHECK_EVERY: usize = 10_000;

for (index, item) in items.iter().enumerate() {
    if index % CHECK_EVERY == 0 && cancelled.load(Ordering::Relaxed) {
        return Err(Error::Cancelled);
    }
    process(item);
}
```

- N trades cancellation latency against overhead; choose it from the cost of one iteration so the check runs every few milliseconds. The flag is passed in, not global.
- In an async task, a long loop also needs `tokio::task::yield_now().await` at intervals, or it starves its neighbours and cannot be cancelled either.

## 10. Unsafe and FFI

**Defaults.**

- **Most code needs no `unsafe`.** Before writing it, look for a safe form: slices and iterators in place of pointer arithmetic, `bytemuck` or `zerocopy` in place of transmutes, `std` atomics and locks, a maintained `-sys` crate with a safe wrapper.
- **`unsafe` does not switch off the rules; it makes you the one who checks them.** Each block rests on an invariant the compiler cannot see. Write it down.
- **Keep it small, private and behind a safe API** whose every use is sound. If safe callers can cause undefined behaviour through your safe function, the function is unsound, however unlikely the call.
- **Unsafe as an optimisation needs a measurement.** `get_unchecked` to skip a bounds check is rarely worth it; restructuring into iterators usually removes the check safely.
- Application crates can set `#![forbid(unsafe_code)]`. Crates that need unsafe set `#![deny(unsafe_op_in_unsafe_fn)]` and `clippy::undocumented_unsafe_blocks`.

### Writing an unsafe block

```rust
/// Returns the element at `index` without a bounds check.
///
/// # Safety
///
/// `index` must be less than `self.len()`.
pub unsafe fn get_unchecked(&self, index: usize) -> &T {
    // SAFETY: the caller guarantees `index < self.len`, and `self.ptr` points to
    // `self.len` initialised elements for as long as `self` is borrowed.
    unsafe { &*self.ptr.as_ptr().add(index) }
}
```

- **An `unsafe fn` has a `# Safety` section** stating what the caller must guarantee. **Every `unsafe` block has a `// SAFETY:` comment** stating why those guarantees hold here. "This is safe" is not a reason; name the invariant and where it is established.
- **One unsafe operation per block where practical,** so each comment covers one claim.
- **The invariant lives in a type.** Fields that the unsafe code relies on are private, and every safe method preserves the invariant. The whole module is the trust boundary: any code that can touch those fields can break the unsafe block, even though it contains no `unsafe` itself.
- **An `unsafe trait`** is for a property that unsafe code elsewhere relies on (`Send`, `Sync`, "this layout is plain bytes"). The `unsafe impl` carries its own `SAFETY` comment.
- **Hand-written `unsafe impl Send` or `Sync` is a strong claim.** State why access from several threads is sound: the type owns its pointee exclusively, or every access is synchronised.

### What must always hold

| Rule | The usual violation |
|---|---|
| `&mut T` is unique; `&T` is not mutated (outside `UnsafeCell`) | two `&mut` made from one raw pointer; writing through a pointer while a `&` is live |
| A reference is non-null, aligned and points to a valid, initialised `T` | `&*ptr` on a null or dangling pointer; a reference to a `repr(packed)` field |
| Every value is valid for its type | a `bool` other than 0 or 1, an enum with an unknown discriminant, a `char` that is a surrogate, uninitialised integers |
| Pointer arithmetic stays within one allocation | `ptr.add(n)` past the end plus one |
| Memory is freed once, by the allocator that made it, with the same layout | `Box::from_raw` on a pointer from C's `malloc`; a `Vec` rebuilt with the wrong capacity |
| No data races | a `static mut` touched from two threads |

- **Breaking these is undefined behaviour even when the program appears to work.** The optimiser assumes they hold, so the failure can appear later, elsewhere, or only at another optimisation level.
- **Creating an invalid reference is already undefined behaviour,** used or not. Stay with raw pointers (`&raw const`, `&raw mut`, `ptr::read`, `ptr::write`) until a valid reference can be made.
- **`MaybeUninit<T>` for memory not yet initialised.** Write through `as_mut_ptr()` or `write()`, and call `assume_init` only after every part is written. Never make a `&mut T` or `&T` to it earlier. `mem::uninitialized` and `mem::zeroed` on a type with invalid zero bytes are always wrong.

```rust
let mut buffer = [const { MaybeUninit::<u8>::uninit() }; 4];
for (index, slot) in buffer.iter_mut().enumerate() {
    slot.write(index as u8);
}
// SAFETY: the loop above initialised all four elements.
let bytes: [u8; 4] = unsafe { mem::transmute(buffer) };
```

- **Panic safety.** If code between two unsafe steps can panic (a user closure, `clone`, an allocation), the unwind runs destructors over the half-finished state. Keep the structure valid at every panic point, or use a guard whose `Drop` repairs it. Setting a length before the elements are written is the classic mistake.
- **`static mut` is almost never right.** Use an atomic, a `Mutex`, `OnceLock`, or an `UnsafeCell` wrapper with a documented `Sync` argument.
- **`transmute` is the last resort.** Prefer `to_ne_bytes`/`from_ne_bytes`, pointer `cast`, `bytemuck`, or a `union`. Never transmute between types whose layout is unspecified, and never to extend a lifetime.

### The FFI boundary

**Only C-shaped types cross.** `&str`, `&[T]`, `String`, `Vec`, `&dyn Trait`, tuples and
default-layout structs have no stable ABI. Pass a pointer and a length; pass structs marked
`repr(C)`.

```rust
#[repr(C)]
pub struct ByteSlice {
    pub ptr: *const u8,
    pub len: usize,
}

/// # Safety
///
/// `input.ptr` must point to `input.len` readable bytes that are not modified during
/// the call. `out` must be valid for one write.
#[unsafe(no_mangle)] // `#[no_mangle]` before edition 2024
pub unsafe extern "C" fn lib_checksum(input: ByteSlice, out: *mut u64) -> i32 {
    let outcome = std::panic::catch_unwind(|| {
        if input.ptr.is_null() || out.is_null() {
            return Err(Status::NullPointer);
        }
        // SAFETY: non-null was checked; the caller guarantees the length and validity.
        let bytes = unsafe { std::slice::from_raw_parts(input.ptr, input.len) };
        let value = checksum(bytes).map_err(Status::from)?;
        // SAFETY: `out` is non-null and valid for one write by the caller's contract.
        unsafe { out.write(value) };
        Ok(())
    });
    match outcome {
        Ok(Ok(())) => 0,
        Ok(Err(status)) => status as i32,
        Err(_panic) => Status::Panic as i32,
    }
}
```

- **A panic never unwinds into foreign code.** Catch it at every exported function and every callback handed to C, and turn it into an error code. Since Rust 1.81 an uncaught panic leaving `extern "C"` aborts the process; before that it was undefined behaviour. `extern "C-unwind"` is only for a boundary where both sides have agreed to unwinding. With `panic = "abort"`, `catch_unwind` catches nothing, so know which profile ships.
- **Check every incoming pointer for null,** and treat every length, index and enum value from the other side as untrusted input.
- **Results go out through out-parameters and a status code.** Error detail comes from a "last error" function or an error out-parameter, never from a Rust type.
- **Nullable things are `Option<NonNull<T>>`, `Option<&T>` or `Option<extern "C" fn(...)>`.** These have the same representation as a nullable C pointer, and the type forces the check. No magic sentinel integers.
- **An integer from C is not yet a Rust enum.** An unknown discriminant is undefined behaviour the moment the enum value exists. Receive the integer and convert it with `TryFrom`. Give C-facing enums an explicit `#[repr(u8)]` or `#[repr(C)]` and explicit values.

**Layout.**

| Attribute | Use |
|---|---|
| `#[repr(C)]` | any struct, union or enum the other side reads or writes |
| `#[repr(transparent)]` | a newtype that must be passed exactly like its one field (`struct Fd(i32)`) |
| `#[repr(u8)]`, `#[repr(i32)]` | a field-less enum with a fixed integer size |
| `#[repr(align(N))]` | raise alignment, for example to a cache line to stop false sharing |
| `#[repr(packed)]` | match a packed C or wire layout; only when you must |

- The default layout is unspecified and may change between compiler versions; that freedom is why it packs best. Never rely on field order or size without a `repr`.
- **A reference to a packed field is undefined behaviour** because it may be unaligned. Copy the field out by value, or use `&raw const` and `read_unaligned`.
- Check layout assumptions at compile time: `const _: () = assert!(size_of::<Header>() == 16);`.
- For reading wire formats, parsing bytes into fields is usually simpler and safer than a packed struct overlay; `zerocopy` does the overlay safely when the speed matters.

**Ownership across the boundary.**

- **Memory is freed by the side that allocated it,** with that side's function. A string from the C library is copied and then released with the library's free; a Rust allocation handed to C comes back to Rust to be dropped.
- **An opaque handle** is `Box::into_raw(Box::new(value))` going out and `Box::from_raw` exactly once coming back, in an exported `destroy` function that accepts null.
- **Strings:** `CStr::from_ptr` borrows a NUL-terminated string from C; it is not necessarily UTF-8, so convert with `to_str()` and handle the error, or use `to_string_lossy()` knowingly. `CString::new` fails on an interior NUL. A `CString` given away with `into_raw` is reclaimed with `CString::from_raw`, never with C's `free`.
- **Never take `.as_ptr()` from a temporary.** `CString::new(name)?.as_ptr()` dangles at the end of the statement. Bind the owner to a variable that outlives the call. The same holds for a `Cow` or any buffer normalised for the call.
- **Callbacks** are an `extern "C" fn` plus a `*mut c_void` for user data. State who owns the user data, how long the callback may be called, and from which thread; that decides whether the data must be `Send`.

**A child handle borrows its parent.** The wrapper owns the raw pointer, keeps alive anything
the C side still points into, and carries the parent's lifetime in `PhantomData`.

```rust
pub struct RawIterator<'db> {
    inner: NonNull<ffi::iterator_t>,
    _options: ReadOptions,              // the C iterator points into this
    _database: PhantomData<&'db Database>, // cannot outlive the database
}

impl Drop for RawIterator<'_> {
    fn drop(&mut self) {
        // SAFETY: `inner` came from `iterator_create` and is destroyed only here.
        unsafe { ffi::iterator_destroy(self.inner.as_ptr()) }
    }
}
```

- A raw pointer field makes the type `!Send` and `!Sync`, which is the safe default. Add `unsafe impl Send` only after reading what the C library promises about threads.

**One helper for a C error out-parameter.** Copy the message, free it with the library's own
function, and convert to `Err`, in one place.

```rust
/// # Safety
///
/// `message` must be a NUL-terminated string allocated by the library.
pub(crate) unsafe fn take_error(message: *mut c_char) -> Error {
    // SAFETY: guaranteed by the caller.
    let text = unsafe { CStr::from_ptr(message) }.to_string_lossy().into_owned();
    // SAFETY: allocated by the library, so released by the library. Never Rust's allocator.
    unsafe { ffi::lib_free(message.cast()) };
    Error::new(text)
}

macro_rules! ffi_try {
    ($function:path, $($argument:expr),* $(,)?) => {{
        let mut error: *mut ::std::ffi::c_char = ::std::ptr::null_mut();
        let result = $function($($argument,)* &mut error);
        if !error.is_null() {
            return Err(unsafe { $crate::take_error(error) });
        }
        result
    }};
}
```

**Crate layout.** Raw bindings live in a `foo-sys` crate with `links = "foo"` in its manifest
and a build script that finds or builds the library; it contains declarations and nothing
else. A separate `foo` crate depends on it and exposes the safe API. Generate bindings with
`bindgen` (and headers for a Rust library with `cbindgen`) so that declarations cannot drift
from the header; a hand-written signature that disagrees with the C one is undefined
behaviour that no tool reports.

- **Keep the public API's constraints in safe types and the unchecked path private.** The implementation takes a fast path (`get_unchecked`, a flat loop over contiguous storage) only after it has established the shape that makes it valid, and falls back to the checked path otherwise.

### Containing unsafe in larger designs

**Checked constructor first; an unchecked twin only after profiling.**

```rust
impl SortedIds {
    pub fn try_new(ids: Vec<u32>) -> Result<Self, NotSorted> {
        if ids.is_sorted() { Ok(Self { ids }) } else { Err(NotSorted) }
    }

    /// # Safety
    ///
    /// `ids` must be sorted ascending: exactly what `try_new` checks.
    pub unsafe fn new_unchecked(ids: Vec<u32>) -> Self {
        debug_assert!(ids.is_sorted());
        Self { ids }
    }
}
```

- Add the unchecked form only when a profile shows validation repeated on data already proven valid. Its preconditions are exactly the checks of the safe one, and each call site says why they hold.
- A `debug_assert!` of the precondition inside the unchecked function catches wrong callers in tests at no release cost.
- **It needs `unsafe` only if breaking the invariant can cause undefined behaviour** (other code skips bounds checks on the strength of it). If a broken invariant merely gives wrong answers, name it `new_unchecked` without `unsafe`, or better, drop it.
- Never call the unchecked form to make an error go away.

**Smaller rules.**

- **A trait whose answers unsafe code trusts is an `unsafe trait`.** If a fast path believes `is_contiguous()` or `len()` and skips checks, a wrong implementation is undefined behaviour, so implementing it must be an explicit promise.
- **One narrow type owns raw allocation.** If raw buffers are needed at all, one small struct holds the pointer, length and `Layout`, and is the only code that calls the allocator and frees in `Drop`. Prefer `Vec`, `Box<[T]>` or an established buffer crate; zero-size and overflowing layouts are easy to get wrong.
- **At an exported entry point, in order:** set out-parameters to null or zero, convert opaque pointers to references once, validate every size and relation between the arguments, then work. A failed call then leaves nothing uninitialised for the caller to read.
- **Low-level copy and bit-packing routines** keep their separate fast paths (tiny, byte-aligned, unaligned). Do not simplify one without benchmarks and tests for zero, tiny, aligned, unaligned and boundary-spanning ranges.
- **Owned or borrowed, for every function of a C API.** Write the owning wrapper, whose `Drop` calls the matching release function, before any logic. An owning wrapper around a borrowed handle is a double free. RAII settles lifetime, not thread safety.
- **Unsafe wrapping in one place.** When a typed wrapper is only valid for raw values produced by a particular object (a match from *this* query, an index into *this* arena), one `unsafe fn wrap` does the pairing and the public iterator always supplies the right pair, so callers stay safe.

**Bindings for another language over a Rust core.**

- **The binding layer is thin:** convert inputs, call the core, wrap the result. It has no behaviour of its own, so the core is tested without the host language.
- **Errors cross through one pair of conversions,** core error to host exception and back, not an ad hoc `map_err` per function. A host exception that passes through Rust comes out as the original exception. Interrupts and cancellation keep their identity; they are not wrapped as generic failures.
- **Host control signals become a typed value at the boundary;** every other exception propagates unchanged.

```rust
match callback_result {
    Ok(_) => Ok(Control::Continue),
    Err(error) if error.is_instance_of::<PruneSearch>(py) => Ok(Control::Prune),
    Err(error) if error.is_instance_of::<StopSearch>(py) => Ok(Control::Stop),
    Err(error) => Err(error), // never swallow an unknown exception as control flow
}
```

- **Cross the boundary once, before going parallel.** Call every host callback and validate every value (NaN, negative weights) up front on the calling thread, into a plain table. The parallel section touches only native data and never calls back into the host runtime, which avoids its global lock and its exceptions inside worker threads. *Not when* the callback depends on traversal state or must be lazy.
- **Model the host's scope protocol as states.** For a context manager or similar: `Pending`, `Entered`, `Finalized`. Re-entry and use after finalisation return an error; they never touch released state.
- **Field order is drop order.** When a wrapper holds a resource and the owner it depends on, the dependent field comes first, with a comment saying the order is load-bearing.

```rust
struct ActiveWrite {
    transaction: WriteTransaction, // must drop before `database`: declared first on purpose
    database: Py<Database>,
}
```

**Dynamic-library plugins.** Rust has no stable ABI. A plugin exposing Rust types is valid
only when built by the same compiler version, for the same target, against the same API
version.

```rust
fn check_compatible(plugin: &BuildInfo, host: &BuildInfo) -> Result<(), PluginError> {
    if plugin.api_version != host.api_version {
        return Err(PluginError::ApiMismatch);
    }
    if plugin.rustc != host.rustc {
        return Err(PluginError::CompilerMismatch);
    }
    if plugin.target != host.target {
        return Err(PluginError::TargetMismatch);
    }
    Ok(())
}
```

- **The build-info query is itself a C-ABI function returning plain data,** and it is the first thing called. Nothing else in the library runs until it passes.
- Both sides must allocate and free with the same allocator; the host passes its own, or ownership never crosses.
- **Unloading is not safe in general:** any vtable, `'static` string or thread from the plugin dangles afterwards. Leak the library deliberately and accept that "reload" keeps the old code mapped.
- **Prefer alternatives.** A C-ABI interface (`abi_stable` or hand-written), WebAssembly, or a separate process over IPC all give versioning and isolation that a Rust-ABI `dylib` cannot. Untrusted plugins always run sandboxed or out of process; a loaded library has the host's full privileges.
- **A binding mirrors the C library's supported ABI version range** and checks a loaded artefact against it before use.

### Fixed layouts, exported ABIs and handlers

**A fixed binary header is checked at compile time and validated after the cast.** For a
fixed-width network, disk or shared-memory record read by reinterpreting bytes:

```rust
pub const HEADER_SIZE: usize = 256;

#[repr(C)]
#[derive(Debug, Clone, Copy, CheckedBitPattern, NoUninit)]
pub struct Header {
    pub magic: [u8; 4],
    pub version: u32,
    pub kind: RecordKind, // #[repr(u8)], also CheckedBitPattern
    _reserved: [u8; 247],
}

const _: () = {
    assert!(size_of::<Header>() == HEADER_SIZE);
    assert!(offset_of!(Header, kind) == 8);
};

let header: &Header = bytemuck::checked::try_from_bytes(&buffer[..HEADER_SIZE])?;
header.validate()?; // magic, version range, lengths within the file
```

- `NoUninit` refuses a struct with padding, so no uninitialised byte is ever written out. `CheckedBitPattern` rejects bytes that are not a valid `bool` or enum value, where a plain cast would be undefined behaviour.
- **The cast proves only that the bytes are a valid `Header`.** A `validate()` step checks meaning before any field is used: magic, version, and every length and offset against the real buffer size.
- **Decide endianness.** A byte cast reads native-endian integers. Store explicitly little-endian fields (`zerocopy`'s byte-order types, or `from_le_bytes` on read) if the data crosses machines. The cast also needs the buffer aligned for the struct; `try_from_bytes` fails otherwise, and `pod_read_unaligned` copies instead.
- Changing the header changes the assertions and the invalid-byte tests in the same commit.
- *Not for* formats that must grow. Those want a length-prefixed or tagged encoding, parsed field by field.

**A C ABI exported from Rust** publishes opaque handles and status codes, never a Rust struct
layout.

- Every handle has a `create` and a `destroy`. Every function returns a status enum with fixed values: zero for success, negative for errors, stable across releases.
- Callers never see inside a handle; the header declares `typedef struct lib_session lib_session;` and nothing more. In the other direction, never reach into a C library's private struct.
- For overload-like convenience, generate one real typed symbol per type with a macro, and put any generic facade on the Rust side.
- The header is generated (`cbindgen`) and checked in CI for freshness.

**Generated bindings and files.**

- A generated file begins with a header naming its generator and the command that regenerates it. Nobody edits it by hand. CI regenerates and fails on a difference.
- Review the generator and one representative output, not thousands of generated lines; generated code hides a bad abstraction well.
- **One core, many languages:** a single interface definition generates every language's package around the same opaque core type (`uniffi`, or per-language tools such as `pyo3` and `napi-rs` driven from one definition). A new method goes into the definition and into each language's end-to-end tests, never by hand into one package.
- **A blocking host method that drives an async Rust future** releases the interpreter lock while it waits, checks for interrupts so Ctrl-C works, and says in its documentation that it blocks.
- **Bulk data crosses in a columnar or batch format** (Arrow's C data interface, a byte buffer), not as one host object per record. Per-record crossings dominate the run time.

**Untrusted extension code runs in a sandbox behind a byte protocol.** With WebAssembly, the
host owns a small protocol: serialised input in, bytes out, explicit registration of what
may be called.

- Every call is fallible I/O: it can trap, time out or return nonsense. Give it fuel or a deadline and a memory limit, and validate the output like any external input.
- Each host function or WASI capability you grant widens the sandbox. Do not call it a security boundary without reviewing what is exposed.
- Trusted first-party extensions are plain Rust; the sandbox is a cost paid only for code you do not control.

**A crash signal handler reports once and re-raises.**

```rust
extern "C" fn on_fatal_signal(signal: i32) {
    static ENTERED: AtomicBool = AtomicBool::new(false);
    if !ENTERED.swap(true, Ordering::SeqCst) {
        // One minimal write(2) to stderr. Nothing else.
    }
    restore_default_and_reraise(signal); // sigaction(SIG_DFL), then raise
}
```

- Re-raising with the default disposition lets the shell and core-dump tooling see the real termination. The atomic guard stops recursion if the handler itself faults.
- **Almost nothing is safe inside a signal handler:** no allocation, no locks, no logging framework, no `println!`. A backtrace allocates; printing one is a knowing compromise. No recovery logic belongs there.
- **For ordinary shutdown signals, do not write a handler.** Use `tokio::signal` or `signal-hook`, which only set a flag or wake a task; the real work runs in normal code.

**Typed arena handles with a niche.**

```rust
pub struct Handle<T> {
    index: NonZeroU32,
    _marker: PhantomData<fn() -> T>,
}

impl<T> Clone for Handle<T> {
    fn clone(&self) -> Self {
        *self
    }
}
impl<T> Copy for Handle<T> {}
```

- `NonZeroU32` makes `Option<Handle<T>>` four bytes. Store `index + 1`, or reserve slot zero, so that zero never names an element.
- The type parameter stops a `Handle<Expr>` being used where a `Handle<Type>` is expected. It does not stop a handle from one arena being used with another arena of the same type; that needs a generation or arena id, checked in debug builds.
- **Implement `Clone`, `Copy`, `PartialEq`, `Eq` and `Hash` by hand.** A derive would add `T: Clone` and the rest, which the handle does not need.
- `PhantomData<fn() -> T>` keeps the handle `Send` and `Sync` whatever `T` is, and tells the compiler the handle does not own a `T`.
- This is entirely safe code. Indices plus an arena are the usual way to avoid unsafe pointer graphs.

### Wrappers around native handles

**Early close is idempotent.** Normally the owning wrapper frees its native peer once, in
`Drop`. Where a handle must also be closable early, as in bindings for a garbage-collected
language, hold it as an `Option` and let exactly one function free it.

```rust
pub struct Parser {
    raw: Option<NonNull<ffi::Parser>>,
}

impl Parser {
    pub fn close(&mut self) {
        if let Some(raw) = self.raw.take() {
            // SAFETY: `raw` came from `ffi::parser_new`, and `take()` means it is freed once.
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

- Every public method goes through `handle()` and returns a "closed" error; none touches a freed peer.
- A wrapper that may hold either an owned or a borrowed handle records which, and never frees a borrowed one.
- An atomic pointer makes reading the pointer atomic. It does not make the native object thread-safe.
- In plain Rust code, prefer consuming `self` in `close(self)`: use after close then fails to compile and no closed state exists.

**One gateway for foreign status codes.** Every call into a C library that returns an integer
status passes through one function that turns the code into a typed status and then a domain
error. The library's detailed message is fetched lazily, on failure only.

```rust
fn check(code: ffi::Status, detail: impl FnOnce() -> String) -> Result<(), NativeError> {
    match Status::try_from(code) {
        Ok(Status::Success) => Ok(()),
        Ok(status) => Err(NativeError::new(status, detail())),
        Err(_) => Err(NativeError::unknown_code(code)),
    }
}
```

- Call sites never compare raw integers, and a code the binding does not know is an error of its own, not a success and not a panic.

**One closed enum owns a set of native bindings.** When a fixed set of native components is
linked in (grammars, codecs, drivers), one enum is the only code that calls their `extern`
constructors, and it also drives listing, parsing of names and display.

```rust
impl Language {
    pub fn grammar(self) -> tree_sitter::Language {
        // SAFETY: each function returns a pointer to a static grammar linked into this binary.
        unsafe {
            match self {
                Language::Go => tree_sitter_go(),
                Language::Rust => tree_sitter_rust(),
                Language::TypeScript => tree_sitter_typescript(),
            }
        }
    }
}
```

- No wildcard arm, so a new variant does not compile until it is wired. Components loaded at run time need a registry instead.

**Smaller rules.**

- **One native artefact, thin loaders.** A native library used from several runtimes is one core product with a minimal loader per runtime. Each loader has the same smallest test, "the library loads here", written before any behaviour test. It catches packaging and link failures and says nothing about correctness, which is tested once, in the core.
- **A native binding must pay for itself.** It is justified when the hot operation's cost outweighs the build, packaging and safety burden of the binding.
- **Raw-pointer containers** (intrusive lists, linked nodes) sit behind a narrow set of typed operations written once, as a generic or a macro. The raw form never leaks out of its module. Try an arena with indices first.
- **Arena handles do not survive a rebuild of the arena.** Either the arena never moves or reuses slots, or handles carry a generation that is checked.

### More handle and callback rules

**A typed wrapper keeps its library context alive.** The wrapper holds the raw handle, an
`Arc` of the context the handle belongs to, and the element type as `PhantomData<T>`. `Drop`
frees the handle; the `Arc` guarantees the context is still there when it does.

```rust
pub struct SparseMatrix<T: ValueType> {
    context: Arc<Context>,
    raw: ffi::Matrix,
    _element: PhantomData<T>,
}

impl<T: ValueType> SparseMatrix<T> {
    /// Gives up ownership. The caller must free the handle while the context lives.
    pub fn into_raw(self) -> (ffi::Matrix, Arc<Context>) {
        let this = ManuallyDrop::new(self);
        // SAFETY: `this` is never dropped, so the `Arc` is moved out exactly once.
        (this.raw, unsafe { ptr::read(&this.context) })
    }
}
```

- Handing ownership out is safe, like `Box::into_raw`; taking a raw handle back in (`from_raw`) is the `unsafe` direction, because the caller vouches for where it came from.
- A handle borrowed from another owner gets a separate borrowed wrapper with a lifetime, and no `Drop`.
- Review drop, clone, extraction and the context's lifetime together, and re-justify each `unsafe impl Send` or `Sync` when any of them changes.

**One opaque Rust type per kind of foreign object,** so two handle types cannot be passed for
each other.

```rust
#[repr(C)]
pub struct Store {
    _data: [u8; 0],
    _marker: PhantomData<(*mut u8, PhantomPinned)>,
}

pub type StoreRef = *const Store;
```

- The marker makes the type `!Send`, `!Sync` and `!Unpin`, and it can never be constructed or read in Rust. Take integer and boolean widths from the `-sys` crate's typedefs (`c_int`, `c_long`), never from a guess: `long` is 32 bits on Windows.

**A closure handed to a C library** that takes a function pointer and a user-data pointer:

- Box a context struct holding the closure and anything it must keep alive. Pass `Box::into_raw` as the user data, and register an `extern "C"` trampoline that casts the pointer back and calls the closure inside `catch_unwind`.
- **Reclaim the box with `Box::from_raw` in exactly one place,** reached both when the callback is replaced and when the owner is dropped. Clear the registration in the C library first, so it never holds a dangling pointer.
- If the library may call from another thread, the closure must be `Send`; say so in the bound.
- **State for a single-threaded host** (an editor's scripting engine, a UI thread) can be `Rc<RefCell<T>>`. The wrapper is then `!Send`, which is the correct statement of the host's rule. Do not reach for `Arc<Mutex<T>>` to quiet the compiler.
- Positions crossing such a boundary are newtypes converted at the edge; the two sides often count in different units (bytes, UTF-16 units, characters).

**A synchronous foreign surface shares one runtime.** When the host cannot await a Rust
future, the FFI library holds one process-wide runtime and each exported method calls
`block_on` on it. No exported method builds its own.

```rust
static RUNTIME: LazyLock<tokio::runtime::Runtime> = LazyLock::new(|| {
    tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .build()
        .expect("tokio runtime for the FFI layer")
});

impl Client {
    pub fn connect(&self) -> Result<(), ClientError> {
        RUNTIME.block_on(self.inner.connect())
    }
}
```

- This belongs at the FFI edge only. Calling `block_on` from inside async code panics or deadlocks; a callback that re-enters an exported method from a runtime thread hits exactly that.

**Smaller rules.**

- **Resources in a managed runtime** (a JVM object behind a global reference) are owned by a Rust wrapper. Scope-bound local references never leave it. `Drop` closes the resource and logs a failure; it never panics.
- **`Drop` does not run on abort, `SIGKILL` or power loss.** A type that creates a temporary system resource (a mount, a keychain, a lock file) also offers explicit clean-up, and start-up removes leftovers from a previous crashed run.
- **Generated C is not held to your warning policy.** When a build script compiles generated code with `cc`, turn warnings off for that unit.
- **A binding crate tests every public member on every target it claims.** A binding that passes on the host can fail under another ABI. Tests that share one native object do not depend on order.
- **A binding generator evaluates C constants in a wide type** (`i128`) and narrows at the end, with a fixture per expression form. A macro it cannot evaluate is skipped with a diagnostic, never emitted as a wrong constant.
- **The core `run` function takes its arguments as parameters,** not from `std::env::args()`, so a binding and the command-line binary share one implementation.

**Verification for unsafe code.**

| Tool | Finds |
|---|---|
| `cargo +nightly miri test` | aliasing violations, use of uninitialised memory, out-of-bounds and use-after-free, in what the tests execute. Cannot run foreign code. |
| AddressSanitizer, ThreadSanitizer | memory errors and data races across the FFI boundary |
| `cargo fuzz` | inputs that reach a bad state in parsers and decoders |
| `loom` | interleavings of small concurrent models |
| `cargo geiger`, `cargo-careful` | where unsafe is; extra standard-library checks |

- Miri and sanitizers only judge the paths the tests take, so the tests must cover empty, one-element, boundary and error cases. A clean run is evidence, not proof.

## 11. Performance

**Defaults.**

- **Correct first, then measured, then faster.** Do not optimise without a profile showing where time or memory goes, and do not keep an optimisation without a benchmark showing it helped.
- **The largest wins are algorithmic and structural:** a better complexity class, less work, fewer allocations, fewer passes, data laid out for the cache. Micro-tuning comes last and matters least.
- **Build in release mode to measure.** A debug build can be ten to a hundred times slower and has a different profile.
- Clear, idiomatic Rust (iterators, slices, borrowed arguments) is usually already fast. Optimisation that costs clarity must pay for it in numbers.

### Speed that keeps the checks

- **A performance change is verified on two axes:** the benchmark delta, and that no checked operation became unchecked and no cached value can outlive its input. Do not replace `.get()` with indexing because a benchmark improved.
- **Prefer speed-ups that add named structure to ones that remove checks.** A precomputed view as its own type is safer than a skipped validation.
- **"Already proved above" stops being true when code moves.** If a check is removed, the invariant is stated where the check was, and ideally carried by a type.
- **On external input, use `checked_*` arithmetic and `.get()`** for offsets, lengths and cursor movement. Use `saturating_*` only where saturation is the documented meaning, never to hide an overflow.
- **Prepare once, query many.** Compile, normalise or index once into a named value (a compiled pattern set, a routing table), then reuse it. *Not when* the preparation costs more than the reuse saves, or the prepared value can go stale unnoticed.
- **Accumulate, then build.** Structures that can only be optimised when the whole batch is known (pattern sets, registries) collect their inputs, and per-item errors, then build once. Do not rebuild on every addition.
- **A builder is mutable; the configuration it produces is frozen** and cheap to share during execution.

### Benchmarks you can trust

- **State the conditions:** input sizes and distribution, toolchain, target, profile and features, machine. A number without them cannot be reproduced.
- **Check both versions return the same result** before comparing their speed.
- **Stop the optimiser deleting the work:** pass inputs and results through `std::hint::black_box`. A benchmark that reports a fraction of a nanosecond measured nothing.
- **Report spread, not one number.** Use `criterion` or `divan` for statistics, and look at the tail (p99) for latency, since an average hides it. Reproduce a result on a second run before acting.
- **Noise sources:** frequency scaling, other processes, cache warmth, allocator state, hash seeds, runtime start-up. For CI, instruction counts (`iai-callgrind`) are steadier than wall time.
- **A microbenchmark supports a claim about that operation on that machine.** Confirm with an end-to-end measurement before claiming the program is faster.
- **Let the measurement reject work.** The most useful result is often that the optimisation is unnecessary; keep the simpler code when the requirement is already met.

### Structural speed-ups

**Per-stage timings at the orchestration boundary.** A multi-stage pipeline takes one borrowed
options struct and returns how long each stage took, so a regression can be attributed.

```rust
pub struct SearchOptions<'a> {
    pub path: &'a Path,
    pub queries: &'a [String],
    pub language: Option<Language>,
    pub max_results: Option<usize>,
    pub timeout: Duration,
}

#[derive(Default)]
pub struct SearchTimings {
    pub query_preprocessing: Option<Duration>,
    pub file_searching: Option<Duration>,
    pub result_processing: Option<Duration>,
    pub total: Option<Duration>,
}
```

- `None` means the stage did not run, which is different from running in zero time.
- Options are typed: a `Duration`, not a bare `u64`; an enum, not a string. The struct holds what the pipeline needs and does not become a dumping ground for every flag in the program.
- Measure with `Instant`, never the wall clock. For anything finer than stages, use spans and a profiler instead of more fields.

**Parse once, plan once, evaluate many.** When one query is evaluated against many inputs,
build a plan up front: resolved term indices, required and excluded sets, and shortcut flags
such as "matches everything". The scan never walks the syntax tree again. *Not for*
single-shot evaluation, where the plan is pure overhead.

**Per-thread caches for worker state.** State that is expensive to build, mutable or not
`Send` (parsers, compiled queries, scratch buffers) is cached per worker thread, not behind
one shared `Mutex` that every worker queues on.

```rust
thread_local! {
    static PARSERS: RefCell<HashMap<Language, Parser>> = RefCell::new(HashMap::new());
}

fn with_parser<R>(
    language: Language,
    work: impl FnOnce(&mut Parser) -> R,
) -> Result<R, ParseSetupError> {
    PARSERS.with(|parsers| {
        let mut parsers = parsers.borrow_mut();
        let parser = match parsers.entry(language) {
            Entry::Occupied(slot) => slot.into_mut(),
            Entry::Vacant(slot) => {
                let mut parser = Parser::new();
                parser.set_language(&language.grammar())?;
                slot.insert(parser)
            }
        };
        Ok(work(parser))
    })
}
```

- Initialise lazily and return the construction error. `work` must not call `with_parser` again: the `RefCell` is borrowed, and the second borrow panics.
- The cache lives as long as the thread, and a pool has many threads, so memory is cache size times thread count. Bound it.
- **In async code a thread-local is not per task:** a task moves between worker threads at each `.await`. Use it only within one synchronous stretch, or in `rayon` and `spawn_blocking` work.
- A shared cache that must be shared is sharded (`dashmap`, or an array of locks indexed by hash), not one `Mutex<LruCache>`.
- *Not for* small single-threaded tools; it only complicates lifecycle and tests.

**The runtime chooses the representation.** When a step can run over a sparse or a dense form
(a frontier as a list or a bitmap), the shared runtime picks from a cheap estimate against a
threshold, not each algorithm. A bad threshold costs speed, never correctness. A flag forces
either mode, and a test runs both and compares results.

**Cache a stable yes-or-no at the call site.** When a hot path asks "is this enabled?" and
the answer changes only with configuration, cache it in an atomic so the path costs one
load. Every reconfiguration must run the rebuild, or sites stay wrongly on or off; test
reconfiguration after the sites exist. Logging and tracing crates already do this for level
checks. *Not when* the answer depends on per-record state.

**Slow side effects leave the hot path through a bounded channel.** Log and telemetry I/O
goes to a worker thread, and the constructor returns a guard whose `Drop` flushes.

```rust
let (writer, _guard) = tracing_appender::non_blocking(file);
// `_guard` lives to the end of scope. `let _ = ...` would drop it now and lose the logs.
```

- Choose the pressure policy and write it down: lossy (drops counted and exposed as a metric) or blocking (producers feel backpressure).
- Never for audit or transactional records, which must be durable before the program continues.

**Data larger than memory.**

- The decision sits beside the storage metadata: if the budget is smaller than the data, stream partitions; otherwise read it in.
- The algorithm is a callback over partitions the storage layer has already filtered, so "what to compute" stays apart from "how to stream". State what the callback may mutate: atomics, or partition-local state merged afterwards.
- **Memory mapping is not free.** It gives no crash-consistent writes, an I/O error arrives as a signal instead of a `Result`, and another process truncating the file is undefined behaviour, which is why creating a map is `unsafe`. It suits large read-only files you control. Not small files, and not files others may modify.

**Manual prefetching and similar micro-techniques** (staging a ring of independent lookups so
cache misses overlap) help only memory-bound pointer-chasing over large data. Keep the simple
path, and adopt the staged one only with benchmark evidence on the target CPUs; it can make
other machines slower.

### Allocating less

**Borrow when nothing changes; allocate only when something does.**

```rust
pub fn normalize_newlines(content: &str) -> Cow<'_, str> {
    if content.contains('\r') {
        Cow::Owned(content.replace("\r\n", "\n"))
    } else {
        Cow::Borrowed(content)
    }
}

pub fn mentions(content: &str) -> impl Iterator<Item = &str> {
    content
        .split_whitespace()
        .filter_map(|word| word.strip_prefix('@'))
}
```

- `Cow` pays off when the unchanged case is common. If nearly every input is rewritten, return `String` and keep the signature simple.
- Returning an iterator of borrowed slices lets the caller decide whether to collect at all.

**In order of how often they pay off:**

1. **Do not allocate in the loop.** Hoist the buffer out and `clear()` it each iteration; `clear` keeps the capacity.
2. **Reserve when the size is known:** `Vec::with_capacity`, `String::with_capacity`, `extend` from an exact-size iterator.
3. **Borrow instead of cloning:** take `&str` and `&[T]`, return slices or iterators, share with `Arc` when ownership really is shared.
4. **Avoid intermediate collections:** chain iterators instead of `collect` and then iterate again; `write!` into an existing `String` instead of `format!` and then `push_str`.
5. **Then, with a profile:** small-size-optimised containers, arenas, pools, a different global allocator.

```rust
let mut line = String::new();
while reader.read_line(&mut line)? != 0 {
    handle(line.trim_end());
    line.clear(); // keeps the allocation for the next line
}
```

- **A `match` on string literals is already compiled to efficient comparisons.** It needs no macro. For a large static lookup table, `phf` builds a perfect hash at compile time.

**A buffer pool, when reuse in place is not possible** (buffers handed between tasks). The
guard returns the buffer on drop.

```rust
pub struct PooledBuffer {
    buffer: Option<Vec<u8>>, // an Option so that Drop can take it
    pool: Weak<Pool>,        // a buffer that outlives the pool is simply freed
}

impl Drop for PooledBuffer {
    fn drop(&mut self) {
        if let (Some(mut buffer), Some(pool)) = (self.buffer.take(), self.pool.upgrade()) {
            buffer.clear();
            if buffer.capacity() <= MAX_RETAINED_CAPACITY {
                pool.put_back(buffer);
            }
        }
    }
}
```

- **A pool holds on to peak memory.** Cap both the number of buffers kept and the capacity of each, or one huge request pins that memory for the life of the process.
- Clear on return, so data from one request can never be read by the next.
- The allocator is already a good pool for small short-lived objects. Add a pool only when a profile shows allocation of large buffers is the cost.

**Inline small case, heap for the rest.** `SmallVec`, a small-string type, or an enum such
as `Inline(InlineData) | Heap(Arc<HeapData>)` keeps the common small case free of
allocation.

- Adopt after profiling shows allocation or cache misses dominate. An inline container is larger to move, and every access branches on which form it is; with the wrong inline size it is slower than `Vec`.
- Pin the size where it matters: `const _: () = assert!(size_of::<Node>() == 16);`.
- A layout change touches every copy, free and tag path. It is never a local edit.

**Permissive builder, compact final form.** Accept entries in any order (edges, sparse
triplets), then convert once to a compressed form: count per row, prefix-sum to offsets,
fill one contiguous array, merging duplicates in that pass. Lookups then read one cache-
friendly array instead of chasing a `Vec<Vec<T>>`. The converting constructor is fallible
for untrusted input; it does not `assert!`.

**Dense internal ids.** Map external keys (strings, sparse numbers) to `0..n` at the input
boundary, run the kernel on plain arrays indexed by id, and map back at the output. The
mapping never leaks into the kernel. "No result" is `Option`, or one named sentinel
constant where the array's size matters.

**Scoped memory accounting.** A child tracker forwards each `allocate(bytes)` to its parent
and remembers the total; on drop it releases the total in one call. A query or a collection
is then accounted for without tracking each element.

```rust
pub struct ScopedTracker<'parent> {
    parent: &'parent Tracker,
    tracked: usize,
}

impl ScopedTracker<'_> {
    pub fn allocate(&mut self, bytes: usize) -> Result<(), OutOfBudget> {
        self.parent.allocate(bytes)?;
        self.tracked += bytes;
        Ok(())
    }
}

impl Drop for ScopedTracker<'_> {
    fn drop(&mut self) {
        self.parent.release(self.tracked);
    }
}
```

- The budget check happens before the allocation it accounts for, and running out is an error the query can report, not an abort.

### Without a heap

**Capacity is a const generic, and running out is an error.** In `no_std`, embedded or
deterministic code, storage is on the stack or static, and every write that could exceed it
returns a structured error.

```rust
pub struct FixedBuffer<const N: usize> {
    buffer: [u8; N],
    length: usize, // invariant: length <= N
}

impl<const N: usize> FixedBuffer<N> {
    pub fn write_bytes(&mut self, bytes: &[u8]) -> Result<(), CapacityExceeded> {
        let remaining = N - self.length;
        if bytes.len() > remaining {
            return Err(CapacityExceeded {
                needed: bytes.len(),
                available: remaining,
            });
        }
        self.buffer[self.length..self.length + bytes.len()].copy_from_slice(bytes);
        self.length += bytes.len();
        Ok(())
    }
}
```

- **A failed write leaves the buffer unchanged.** Check first, then mutate.
- The error says how much was needed and how much was available.
- If `as_str()` relies on the contents being UTF-8, every write path preserves that and never splits a multi-byte character; a `write_str` that takes `&str` and writes all or nothing does.
- Implement `core::fmt::Write` so `write!` works.
- Prefer `heapless` (`Vec`, `String`, queues, maps) or `arrayvec` to writing these by hand.
- **A large `[T; N]` lives wherever its owner does.** On the stack, a big `N` overflows it, and moves copy all `N` elements; put large fixed storage in a `static` or behind a reference.
- When allocation is acceptable, use `Vec` and `String`. Fixed capacity is a constraint to satisfy, not an optimisation to reach for.

### Arenas, drops and the allocator

**An arena's lifetime matches one phase of work.** Many small allocations that die together
(one file's syntax tree, one request's scratch data) go into a bump arena such as
`bumpalo::Bump`, which is reset at the phase boundary and reused.

- Name the owning phase. Nothing arena-backed escapes it; the `&'bump` borrow enforces that.
- **A bump arena does not run destructors** for what it holds unless you use its owning `Box`. Keep plain data in it, not types that own files, locks or heap memory.
- **A long-lived arena is a leak in disguise.** It grows to the largest workload it has seen and frees nothing until reset.
- *Not for* objects with independent lifetimes, or data that must outlive the phase.

**Move an expensive drop off the latency-critical thread.** When freeing a large structure
(a deep tree, a big index) stalls a UI or request thread, send the value to a long-lived
background thread that only receives and drops.

```rust
// Fails only if the background thread is gone; then the value drops here, as before.
let _ = self.drop_queue.send(std::mem::take(&mut self.tree));
```

- *Not for* a resource that must be released before the next step (a lock, a file another process waits on). Confirm with a profile that the drop was the stall.
- A deep recursive structure can also overflow the stack while dropping. Write an iterative `Drop`, or hold the nodes in a `Vec` or arena.

**The global allocator** is changed only when allocation is a measured bottleneck, typically
a multi-threaded server with many small allocations.

```rust
#[global_allocator]
static GLOBAL: mimalloc::MiMalloc = mimalloc::MiMalloc;
```

- Measure throughput, tail latency and resident memory before and after; an allocator can win on speed and lose on memory. Only a binary sets it, never a library.

**Build settings.**

```toml
[profile.release]
lto = "thin"        # "fat" for a little more speed and much longer builds
codegen-units = 1   # better optimisation, slower builds
panic = "abort"     # smaller and slightly faster; only if nothing relies on unwinding
```

- These trade build time for run time. Measure the gain; on I/O-bound programs it is often nil. Keep them out of the dev profile.
- **`panic = "abort"` changes behaviour:** no `catch_unwind`, no destructors on panic, and one panicking task ends the whole server.
- **`target-cpu=native` makes a binary that may crash on other machines.** Use it only when you build on, or for, the machine that runs it. Otherwise detect features at run time (`is_x86_feature_detected!`).
- **`#[inline]` matters for small functions called across crates,** which cannot otherwise be inlined without LTO. Generic functions already can be. `#[inline(always)]` is for measured cases only; applied widely it bloats code and slows it down. `#[cold]` on error paths is the cheaper hint.
- Profile-guided optimisation (`cargo-pgo`) is worth setting up for a long-lived hot binary with a representative workload, and not before.

### Caches

**A cache is a correctness risk bought for speed.** Before adding one, state the key, what
invalidates an entry, the size bound and what a stale read costs.

- **Bound it:** a maximum size, usually a time to live as well. An unbounded map used as a cache is a memory leak. `moka` for a concurrent cache with eviction; a `HashMap` or `lru` behind the owner's lock for a small one.
- **The key contains every input that changes the answer.** Tenant, authorisation scope, locale, version, options. A key that omits the user serves one user's data to another.
- **Never cache what is not a pure function of the key** unless staleness is accepted and bounded.
- **Policy is part of a cache's identity.** Settings that change validity (time to live, capacity, persistence, scope) belong in the type or key that decides whether an existing cache may be reused.
- **Negative results are cached separately,** with a shorter life: "not found" goes stale as soon as the thing is created.
- **Many concurrent misses for one key should compute once.** Use the cache's get-or-insert-with, or single-flight, not a check followed by an insert.
- **Measure the hit rate.** A cache that rarely hits costs memory, locking and complexity for nothing.
- A process-wide cache needs an invalidation path, and tests need a way to start with it empty.

**Build-style cache keys come from every semantic input.**

```rust
let mut entries: Vec<_> = fs::read_dir(dir)?.collect::<Result<_, _>>()?;
entries.sort_by_key(|entry| entry.file_name()); // traversal order must not change the key
for entry in entries {
    hasher.update(b"file\0");
    hasher.update(entry.file_name().as_encoded_bytes());
    hasher.update(b"\0");
    hasher.update(&fs::read(entry.path())?);
}
```

- Hash the tool version, the input contents, the options and each environment setting that affects output. Separate fields with a tag and a delimiter, so `("ab", "c")` and `("a", "bc")` differ.
- **Size and modification time may shortcut re-reading an unchanged file; they are never the identity.**
- Use a stable hash (BLAKE3, SHA-256) for anything persisted. `DefaultHasher` is not stable across Rust versions.
- Namespace cached output by the producer's version, write with a temporary file and an atomic rename, treat an unreadable entry as a miss, and keep a `--force` or `--no-cache` escape hatch.
- **Invalidate by interface when that is what dependants use.** Hash the sorted public facts (names, signatures, imports) and classify a change as none, cosmetic or structural. The hash ignores bodies by design; add behaviour inputs explicitly if they matter.
- **Cache a compiled intermediate form** (a lowered plan, a compiled template) with `OnceLock` or a keyed cache, and know what invalidates it before the source is allowed to change.

### Bulk data

- **Per-thread worker state in `rayon`:** `for_each_init` or `map_init` builds the non-thread-safe state per worker split; shared immutable data goes in an `Arc`.

```rust
let outcomes: Vec<(usize, Result<(), ProcessError>)> = files
    .par_iter()
    .enumerate()
    .map_init(
        || Highlighter::with_store(Arc::clone(&store)), // per worker, not per item
        |highlighter, (index, path)| (index, process(highlighter, path)),
    )
    .collect();
```

- Return per-item results and report them from one place. Printing from inside workers interleaves output and loses the count of failures.
- **Parallel export with one sink per chunk** works only where independent output chunks are acceptable. Where order or one transaction is required, keep a single ordered writer.
- **Batch writes by statement shape,** not only by count, so each batch is one prepared statement. Parallel batches each need their own connection and a first-error policy.
- **An append-only chunk writer** reuses one buffer, writes a placeholder header, streams records through the compressor and checksum, backfills length and checksum, and issues one `write_all`. Shrink the buffer after an unusually large batch. A round-trip reader test accompanies every format change.
- **Columnar engines** (Polars, Arrow with DataFusion): use the lazy or SQL API so the engine can plan, push filters down and stream. Do not convert columns to row structs early; that discards the vectorisation you adopted the engine for. Fix the query plan before tuning thread or memory settings.

### Derived data, hashing and streaming input

**Derived data cached on its owner has one invalidation function.** Derived facts (a
transpose, degree counts, a sorted flag) are computed lazily and reused.

```rust
pub struct Graph {
    edges: Vec<Edge>,              // private: mutated only through methods below
    degrees: OnceCell<Vec<u32>>,
    is_symmetric: Option<bool>,    // None means "not yet known"
}

impl Graph {
    pub fn add_edge(&mut self, edge: Edge) {
        self.edges.push(edge);
        self.invalidate_derived();
    }

    fn invalidate_derived(&mut self) {
        self.degrees = OnceCell::new();
        self.is_symmetric = None;
    }
}
```

- The base field is private and every mutating method calls the one invalidation function. A stale derived fact gives wrong answers silently, so this is not left to each caller.
- "Not computed" and "unknown" are explicit (`Option`, a three-state enum), never a default that looks like an answer.
- *Not when* the base changes on nearly every operation: recompute, or maintain the fact incrementally.

**Canonical hashing of structured values.** Raw bytes hash directly. A structured value is
hashed in a canonical form: object keys sorted, only identity-bearing fields included,
arrays left in order when order has meaning.

- Write down which fields define identity before adding the hash.
- Test both directions: the same content in another key order gives the same hash, and different content of the same shape gives a different one. Over-normalising merges distinct inputs; under-normalising causes needless misses.
- **Canonicalise floats used as keys:** `-0.0` and `0.0` compare equal but have different bits, and NaN has many bit patterns and equals nothing. Normalise both before hashing, or do not key on floats.

**On-disk caches of regenerable results.**

- The cache version combines a hand-bumped schema number with the package version; a mismatch means start empty. Any change to what is stored bumps the schema number in the same commit.
- A missing, truncated or unreadable entry is a miss, never an error. The cache can always be deleted.
- **A key is validated so that it cannot be a path:** no separators, no `..`. Better, name files by the hex hash of the key.
- A small index stays in memory; payloads load on demand.

**Stream a large top-level JSON array** one element at a time instead of deserialising the
whole document. With `serde`, a `Visitor` whose `visit_seq` handles each element as it
arrives does this without hand-parsing brackets and commas:

```rust
struct ForEach<F>(F);

impl<'de, F: FnMut(Record)> Visitor<'de> for ForEach<F> {
    type Value = usize;

    fn expecting(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str("an array of records")
    }

    fn visit_seq<A: SeqAccess<'de>>(mut self, mut seq: A) -> Result<usize, A::Error> {
        let mut count = 0;
        while let Some(record) = seq.next_element::<Record>()? {
            (self.0)(record);
            count += 1;
        }
        Ok(count)
    }
}

let mut deserializer = serde_json::Deserializer::from_reader(BufReader::new(file));
let count = deserializer.deserialize_seq(ForEach(|record| sink.push(record)))?;
```

- `serde_json`'s `StreamDeserializer` (`into_iter`) handles concatenated or newline-separated values, not a comma-separated array. If you control the format, newline-delimited JSON is simpler to stream, append to and resume.
- Wrap the reader in a `BufReader`, and make errors name the element index.
- *Not when* validation needs the whole document before any element may be acted on.

**A prefilter may give false positives and never false negatives.** A cheap test in front of
an expensive match can say "maybe" wrongly; it can never say "no" wrongly.

- Decide what "cannot translate this condition" means before writing the combinators. In an `And`, an untranslatable term is dropped: fewer conditions still admit every real match. In an `Or`, one untranslatable branch makes the whole `Or` unknown, because dropping the branch would drop real matches.
- An evaluation error in the prefilter counts as "maybe".
- Test it as a property: everything the full matcher accepts, the prefilter also accepts.

**Greedy selection under a budget.**

```rust
scored.sort_by(|a, b| b.score.total_cmp(&a.score).then_with(|| a.id.cmp(&b.id)));

let mut used = 0;
let mut selected = Vec::new();
for candidate in scored {
    if used + candidate.cost <= budget {
        used += candidate.cost;
        selected.push(candidate);
    }
}
```

- `f64::total_cmp` gives a total order that tolerates NaN; `partial_cmp().unwrap()` panics on it. The tie-break makes the selection deterministic.
- An item that does not fit is skipped and a smaller later one may still fit. This is a heuristic, not optimal packing; say so, and return the amount used.

**Caches that own live resources.**

- **A manager owns expensive open handles** (files, sessions): a bounded LRU, its lock, and close-on-evict. The key includes every argument that distinguishes handles (path, mode, options). Callers never close what the manager gave them.
- **Eviction of an async resource only signals stop,** because eviction is synchronous and clean-up is not. Each session runs in a task that holds its resources and waits for the signal. Shutdown makes an explicit pass that awaits every such task; fire-and-forget eviction is not a shutdown guarantee.
- **A cache addressed by two keys** keeps the forward and reverse maps in one struct and updates both in every add, move, remove and clear.
- **A shortened hash used as an identifier can collide.** Detect it; do not assume it away.
- **A fixed table of `OnceLock` indexed by a small parameter space** is a cache bounded by construction.

**Smaller rules.**

- **Hidden reordering stays hidden.** A batching optimisation that reorders its inputs (sorting by length to reduce padding) restores the original order before returning.
- **A per-call override is a parameter.** Pass `top_k` with the request or apply it to a per-request copy. Never mutate a shared component and restore it afterwards: concurrent requests race, and an early return leaves it changed.
- **Variants are chosen by exact identifier,** not by substring match with a silent default.
- **A long batch run checkpoints each finished unit** under a deterministic key, written with a temporary file and a rename, and skips saved keys on resume. Replacing a unit that failed for infrastructure reasons is a separate, explicit operation.
- **Randomness is injected** (`&mut impl Rng`, or a seed that is logged), so a run can be reproduced.
- **At the boundary of a typed kernel,** match on the type tag once and downcast inside the arm that proved the type, not repeatedly in the inner loop.
- **In an incremental framework** (`salsa`), every changing fact is a typed input, and each new query is checked for what invalidates it: one query that reads global data makes everything recompute. A tool that runs once and exits needs no such framework.
- **When several ranking signals are fused,** keep each signal's contribution on the result so the ranking can be explained and tuned. Demote with a negative signal instead of excluding.
- **A vector index compares like with like.** Inner product equals cosine similarity only for normalised vectors, so never mix normalised and unnormalised embeddings. Never hold the index lock across the call that computes an embedding.

### Incremental and amortised work

**Append cheaply, consolidate lazily.** For frequent signed updates where many increments
and decrements cancel (reference counts, change logs, multiset deltas), push each update and
consolidate only when a clean view is needed or the unsorted tail outgrows the clean prefix.

```rust
pub struct ChangeBatch<T> {
    updates: Vec<(T, i64)>,
    clean: usize, // updates[..clean] is sorted, merged and free of zeros
}

impl<T: Ord> ChangeBatch<T> {
    pub fn update(&mut self, item: T, delta: i64) {
        self.updates.push((item, delta));
        if self.updates.len() > 2 * self.clean.max(MIN_BATCH) {
            self.compact();
        }
    }

    /// Compacts first, so it takes `&mut self`.
    pub fn is_empty(&mut self) -> bool {
        self.compact();
        self.updates.is_empty()
    }

    fn compact(&mut self) {
        self.updates.sort_by(|a, b| a.0.cmp(&b.0));
        self.updates.dedup_by(|later, earlier| {
            if later.0 == earlier.0 {
                earlier.1 += later.1;
                true
            } else {
                false
            }
        });
        self.updates.retain(|(_, delta)| *delta != 0);
        self.clean = self.updates.len();
    }
}
```

- Compacting when the tail doubles the clean part keeps the amortised cost per update logarithmic, the same argument as `Vec` growth.
- **An observer that compacts takes `&mut self` and says so.** Hiding the mutation behind a `RefCell` to keep `&self` trades a compile-time rule for a run-time panic.
- The same shape serves any "write-optimised log plus periodic merge": tombstones in an index, pending edits to a sorted array.

**Incremental indexing by content hash.** Keep the set of content hashes per source file.
After a change, new minus old is inserted and old minus new is deleted; nothing else is
touched.

```rust
let to_insert: Vec<&Chunk> = new_chunks
    .iter()
    .filter(|chunk| !old_hashes.contains(&chunk.hash))
    .collect();
let to_remove: Vec<&Hash> = old_hashes
    .iter()
    .filter(|hash| !new_hashes.contains(*hash))
    .collect();
```

- **The hash inputs decide what counts as a change.** Including line numbers makes a pure move look like a change and redoes the expensive work; leaving them out means stored positions must be updated separately. Choose from the invalidation behaviour you want.
- Insert the new before deleting the old, or do both in one transaction, so a crash between them never leaves a file with no entries.
- Changing how content is chunked changes every hash: bump the index version and rebuild.
- Keep a full-rebuild command. It is the recovery path and the oracle for testing the incremental one: both must produce the same index.

**Smaller rules.**

- **Text enriched for retrieval is stripped before display.** If a chunk is indexed with a context preamble (file, language, defined symbols), one paired function removes it, so snippets and line numbers shown to people are those of the source.
- **Scores from two retrieval systems are not comparable; ranks are.** Fuse through stable ids, each source adding `weight / (rank + k)`. The weights and `k` are configuration tuned by evaluation, not constants in code. With calibrated, comparable scores, use the scores.
- **Cross-cutting behaviour lives in the framework, not in each plugin.** A linter owns traversal and suppression comments; rules only report. A rule that accumulates state is constructed per file or cleared in a finalisation hook, or findings leak from one file into the next.
- **In a streaming operator ordered by logical time,** buffered work is released when input progress proves that nothing earlier can arrive, never by a wall-clock timer. A held capability or watermark blocks everything downstream; drop it as soon as its output is emitted.
- **A parameter outside the supported range is a typed error before any work,** never an unbounded build. The bound is a product decision, since cost often grows steeply with it.

### Hashes, prefilters and storage invariants

**More on identity hashes.**

- **Put a format version in the hashed data,** so a change to the canonical form cannot be mistaken for unchanged content.
- **Normalise per domain type through a trait.** Never hash `Debug` output or default serialisation and hope it is stable: field order, float formatting and map order are not promises.
- For each new field, decide whether it is semantic or presentation-only, and change the canonical form and the hash-stability tests in the same commit.
- A value that cannot be hashed deterministically is an explicit error.
- **An identity hash is not a security proof.** For anything an attacker can influence, use a keyed MAC or a signature.
- **A semantic hash over a syntax tree** skips noise nodes (comments, whitespace), emits kind and text for value-bearing nodes and kind only for structural ones. Those three sets define "semantic": a value-bearing kind left out reports "unchanged" for a real change. Changing them is a version bump. *Not where* exact text or comments are part of the record.

**A cheap bit test in front of expensive scoring.**

```rust
#[derive(Clone, Copy, Default)]
pub struct CharBag(u64); // one bit per lowercased a-z and 0-9

impl CharBag {
    pub fn is_superset(self, other: CharBag) -> bool {
        self.0 & other.0 == other.0
    }
}
```

- A candidate whose bag lacks any query character cannot match, so most are rejected with one AND. The filter rejects only the impossible and is never the only check.
- **Scratch matrices are fields reused across candidates** (`clear()` then `resize`), stored as one flat `Vec` indexed `row * width + column`. A `Vec<Vec<T>>` allocates per row and scatters rows across the heap.
- Cost grows with query length times candidate length, so a long search keeps its cancellation checks.

**A rolling hash nominates; comparison decides.** Finding repeated fixed-size windows with a
rolling hash costs one pass over the input.

```rust
hash = hash.wrapping_mul(BASE).wrapping_add(incoming);
hash = hash.wrapping_sub(POWER.wrapping_mul(outgoing)); // POWER = BASE^window
```

- Equal hashes mean "probably equal". Confirm by comparing the blocks. This holds for any hash used as a shortcut for equality.
- Use explicit `wrapping_*` arithmetic; plain `*` and `+` panic on overflow in debug builds.
- Long runs of identical items produce a quadratic number of matches; collapse them first.

**A snapshot is a leased read instant.** Opening one registers its sequence number and
returns a guard whose `Drop` deregisters it. Garbage collection frees only versions below
the lowest number still registered.

```rust
pub fn open(&self) -> SnapshotGuard {
    let _gc = self.gc_lock.read(); // collection cannot run between the load and the insert
    let sequence = self.sequence.load(Ordering::Acquire);
    *self.open.entry(sequence).or_insert(0) += 1;
    SnapshotGuard::new(sequence, self.clone())
}

pub fn publish(&self, batch_sequence: u64) {
    self.sequence.fetch_max(batch_sequence + 1, Ordering::AcqRel); // never moves backwards
}
```

- **A leaked or long-held snapshot blocks collection for ever.** Export the age of the oldest open snapshot as a metric.
- Test that an old snapshot still reads old values after later writes and an explicit collection.

**Shared durable artefacts are deleted only when every dependant is past them.** A
write-ahead-log segment serving several partitions records one sequence number per
partition. Deletion walks from the oldest segment and stops at the first one that some live
partition has not yet persisted beyond. A deleted partition stops holding segments back.
Test crash recovery with mixed and deleted partitions.

**Durable formats.**

- **Every serialised field has a permanent tag or name,** never reused and never renumbered. Retired tags are reserved.
- **New fields arrive as optional.** A reader distinguishes absent from zero or false with `Option<T>`, not a defaulted scalar, and tolerates unknown fields. Use `#[serde(default)]` only where the default truly means "absent".
- Test three cases: field absent (old writer), field present, unknown field present (newer writer).
- **Separate physical storage from logical meaning:** a small stable set of storage types, plus tagged logical annotations carrying their parameters (`Decimal { precision, scale }`, `Timestamp { unit, utc }`). A new logical type also updates reader validation and round-trip tests.
- `#[serde(deny_unknown_fields)]` suits configuration files, where a typo should fail. It is wrong for a wire format that newer writers will extend.

**Smaller rules.**

- **A cache miss is a value.** Absence in a cache or content-addressed store is `Ok(None)`; `Err` is for real failures. Removing an entry that is already gone is success.
- **Non-overlapping chunks by line ownership.** Sort symbol spans longest first and assign each span's lines to it in that order, so a nested span overrides its parent; emit runs of one owner as chunks and window the unowned gaps. A file that fails to parse falls back to plain windows instead of failing the index. *Not when* retrieval benefits from overlapping context.
- **Expansion signals are opt-in and down-weighted** (graph neighbours of a hit), so they cannot outrank direct matches. Inspect each ranked list separately before changing weights.

### Pipelines, sync and derived indexes

**Decorate, compute, undecorate.** When an algorithm compares heavy values many times (diff,
longest common subsequence, deduplication over long strings), map each distinct value to a
small integer once, run the algorithm on integers, and map back at the end.

```rust
fn intern<'a, T: Eq + Hash>(
    values: &'a [T],
    ids: &mut HashMap<&'a T, u32>,
    by_id: &mut Vec<&'a T>,
) -> Vec<u32> {
    values
        .iter()
        .map(|value| {
            *ids.entry(value).or_insert_with(|| {
                by_id.push(value);
                (by_id.len() - 1) as u32
            })
        })
        .collect()
}
```

- The reverse table is a `Vec` indexed by id: no second map, no `unwrap`.
- Interned ids make equality exact, unlike a hash, which can collide. The same idea gives subtrees an identity: intern each node's shape plus its children's ids.
- *Not worth it* when values are small or compared only a few times.

**Batch each stage to its own bottleneck.** In an offline job, slow external calls
(inference, remote APIs) run in fixed-size chunks with bounded concurrency; results land in
a pre-sized `Vec` by index, so order is preserved; one bulk write follows when everything
exists. Report progress per chunk. *Not for* streaming ingestion, where partial results
must be usable at once.

**Synchronise an inventory by diff, not rebuild.** Build maps of the existing and the
discovered items on a stable key, compare a fingerprint of the meaningful fields, and return
what happened.

```rust
pub struct SyncReport {
    pub added: Vec<Key>,
    pub updated: Vec<Key>,
    pub removed: Vec<Key>,
    pub unchanged: usize,
    pub errors: Vec<(Key, SyncError)>,
}
```

- One bad item is recorded in `errors`; it does not fail the whole run.
- The key must be unique within its scope, or a rename looks like a removal plus an addition.
- **An empty or failed discovery is not "delete everything".** Distinguish "source returned nothing" from "source could not be read" before removing.

**An incremental plan keeps four outcomes apart.** The timestamp decides when to hash; the
hash decides what changed.

| Observation | Step |
|---|---|
| Modified time newer, hash differs | index the new version, retire the old |
| Modified time newer, hash equal | record the new time only |
| Path gone | remove |
| Modified time not newer | nothing |

- **Metadata is a shortcut, not proof.** Timestamp precision varies by filesystem, and clocks and checkouts can move times backwards. Where a missed change is costly, compare with "different", not "newer", or hash regardless.
- A two-stage key does the same for caches: a cheap metadata key first, the content key as the authority. Write down what the cheap key assumes.

**Derived structures change together.**

- **After a registry change, everything derived from it is rebuilt and swapped as one unit:** one `ArcSwap` or one lock over a struct holding all of them. Readers never see a new index beside an old lookup table.
- **A derived index is keyed by everything that produced it:** source identity (repository and commit), tool version, schema version and relevant settings. Commit alone goes stale on a tool upgrade, and is wrong when uncommitted or generated files feed the index.
- **A content-addressed store shared by several tags** (branches, workspaces) tracks which tags use each artefact. Adding a tag recomputes nothing; removing the last tag deletes the artefact. Tag changes are transactional when writers run concurrently. *Skip it* when artefacts are cheap to rebuild.

**Graph results cross a boundary ready to use.** Return analysed structures, not raw
traversal order.

```rust
let has_self_edge = component.len() == 1
    && graph
        .get(&component[0])
        .is_some_and(|children| children.contains(&component[0]));
components.push(Component {
    is_cycle: component.len() > 1 || has_self_edge,
    nodes: component,
});
```

- A single-node component is a cycle only when it has an edge to itself.
- Sort roots and children before traversal, so output is deterministic.
- **Recursive graph algorithms overflow the stack on deep input.** Use an explicit stack for anything whose depth the input controls.

**Smaller rules.**

- **A ranking is sorted by score, then by a stable key.** `HashMap` iteration order must never decide the order of equal scores.
- **A fused score is relative evidence,** not a probability. Validate that the number of weights equals the number of lists.
- **One connection boundary for a subsystem with several services.** `connect` is idempotent, checks every dependency before any work, and fails with a message that says how to fix it. Keep health per dependency visible when they can degrade independently.
- **Export files follow the importer's boundaries** (one file per table or relation). Write a header only when creating the file, put the path in every I/O error, and remove partial files after a failed write.
- **Oversized inputs are skipped before expensive work,** by a stated size cap, and the skip is reported.

### Streams, formats and protocols

**Streamed text becomes lines first.** Before any diff, patch or parse logic, turn chunks
into complete lines: append each chunk to a buffer, emit every complete line, keep the
trailing partial line, and flush the remainder when the stream ends.

```rust
pub struct LineBuffer {
    pending: Vec<u8>,
}

impl LineBuffer {
    pub fn push(&mut self, chunk: &[u8]) -> Vec<String> {
        self.pending.extend_from_slice(chunk);
        let mut lines = Vec::new();
        while let Some(end) = self.pending.iter().position(|byte| *byte == b'\n') {
            let line: Vec<u8> = self.pending.drain(..=end).collect();
            lines.push(String::from_utf8_lossy(&line).into_owned());
        }
        lines
    }

    pub fn finish(self) -> Option<String> {
        (!self.pending.is_empty())
            .then(|| String::from_utf8_lossy(&self.pending).into_owned())
    }
}
```

- **Buffer bytes, not `String`s.** A chunk boundary can fall inside a multi-byte character; decoding each chunk separately corrupts it. A complete line is safe to decode because `\n` never occurs inside a UTF-8 sequence.
- Tests feed chunks that split mid-line, mid-character, and a stream with no final newline.
- Bound the pending buffer if the peer is untrusted: a stream with no newline grows it without limit.
- Fuzzy matching of edit anchors (accepting lines equal after trimming) suits prose and code edits. It is wrong for data formats where one character matters, and it never matches on blank lines.

**A line-oriented format with a few exclusive regions is a state enum and one `match` per
line.** Write the enum first.

```rust
#[derive(Debug, Clone, Copy)]
enum Region { Outside, Left, Base, Right }

let mut state = Region::Outside;
let mut opened_at = None;
for (index, line) in input.split_inclusive('\n').enumerate() {
    if line.starts_with(LEFT_MARKER) {
        state = Region::Left;
        opened_at = Some(index);
        continue;
    }
    // The base, right and end markers change `state` the same way.
    match state {
        Region::Outside => { left.push_str(line); right.push_str(line); }
        Region::Left => left.push_str(line),
        Region::Right => right.push_str(line),
        Region::Base => {}
    }
}
if let (Region::Left | Region::Base | Region::Right, Some(line)) = (state, opened_at) {
    return Err(ParseError::Unterminated { opened_at: line });
}
```

- `split_inclusive('\n')` keeps line endings, so content is rebuilt byte for byte, including `\r\n`. `lines()` discards them.
- **Record where the open region began,** so an unterminated region at the end of input is an error with a location, not silently accepted.
- A marker in the wrong state (an end with no start) is an error too. Nested or escaped markers need a stack or a real parser.

**Cross-language contracts.**

- **Integers beyond 2^53 − 1 do not survive JavaScript.** A Rust service exposing `u64` or `i64` identifiers to a JavaScript client sends them as strings.

```rust
#[derive(Serialize, Deserialize)]
pub struct Event {
    #[serde(with = "u64_as_string")]
    pub id: u64,
}
```

- **Parity tests compare canonical structure,** ignoring object key order. Compare bytes only when the exact bytes are the contract (signatures, hashes).
- Shared fixtures include large integers, dates and time zones, binary data, empty and nested arrays, `null` versus absent, and non-ASCII text.
- **Variants are a tagged enum** (`#[serde(tag = "type")]`) whose variants carry only the fields valid for that kind. A flat struct of optional fields lets illegal mixtures through.
- Add the discriminant and its validation before adding consumers.

**Incremental update protocols define their conflicts.** A patch stream (live graph, index
deltas, UI state) says what happens when one patch both removes and upserts the same id,
and reconciles before publishing.

- With upsert-wins, the removal is netted away, so a client applying removals and upserts in either order reaches the same state.
- Replication and audit logs want delete-wins with tombstones instead. Choose deliberately.
- Test removing and recreating one id in a single patch.
- Patches carry a sequence number, so a client can detect a gap and ask for a full snapshot.

**Smaller rules.**

- **An optional enhancement sits behind a capability check with the plain path as fallback.** Initialise it once and remember failure (`OnceLock<Option<T>>`), so it is not retried per item. **A silent fallback makes deployments behave differently:** log the capability state at start-up and record it with any output that depends on it.
- **Resources that survive reconnects get identifiers from a stable property** (a fixed name, a hash of the canonical path), never a process-local counter. A short hash prefix is fine as a local key and wrong as a global identity. Do not leak a sensitive path through a public id.
- **A list that is capped says so.** Return a `truncated` flag or the total beside it, and sort before capping by a documented, deterministic order.
- **Dangling references found while projecting data are skipped and counted,** as a signal of index integrity, not ignored.
- **A fixed-point loop converges on a canonical form.** If equal states can be represented differently (unsorted, with cancelling entries), the loop never sees "no change". Normalise each round, and cap the iterations with an error that says the cap was hit.
- **An append-only segment writer** uses positioned writes at its tracked offset, takes `fsync` as an explicit policy so the caller sees the cost, and publishes the new size only after the write succeeds. Concurrent writers reserve their range first or are serialised. After recovery, the counter equals the file length.
- **A null-aware column builder appends a value for every row,** a default for null rows, and tracks validity separately, so the values buffer and logical length always agree. The validity bitmap is created at the first null and back-filled.

### Lazy side structures, memos and multi-file output

**Create an optional side structure on first need.** When the all-default case dominates
(no nulls, nothing dirty, no overrides), keep only a count until the first exception, then
build the structure and back-fill it.

```rust
pub struct ValidityBuilder {
    bitmap: Option<BitmapBuilder>,
    valid_before_bitmap: usize,
}

impl ValidityBuilder {
    pub fn append_valid(&mut self, count: usize) {
        match self.bitmap.as_mut() {
            Some(bitmap) => bitmap.append_n(count, true),
            None => self.valid_before_bitmap += count,
        }
    }

    pub fn append_null(&mut self) {
        let seen = self.valid_before_bitmap;
        self.bitmap
            .get_or_insert_with(|| {
                let mut bitmap = BitmapBuilder::new();
                bitmap.append_n(seen, true);
                bitmap
            })
            .append(false);
    }

    pub fn finish(self) -> Option<Bitmap> {
        self.bitmap.map(BitmapBuilder::finish)
    }
}
```

- The common case pays one integer add and no allocation; consumers get `None` and skip the check entirely.
- Property-test that the side structure's length equals the main length after any sequence of appends.
- *Not when* a placeholder stored for an absent row is costly, or could be read by a consumer that skips the validity check.

**An async memo entry has a pending state.** Keyed by a fingerprint of the inputs, each
entry is `Pending` or `Ready(Option<T>)`: a second caller waits for the first, and a
finished empty result is not mistaken for unfinished work.

- *Only for* deterministic work, or with every side-effect dimension in the fingerprint.
- **A producer that fails or is cancelled must clear or fail its pending entry,** or every waiter hangs. A guard that removes the entry on drop covers cancellation.
- Decide whether errors are cached. Usually they are not, or a transient failure becomes permanent.
- Race test: two concurrent requests for one fingerprint, and assert that one producer ran.

**Schema inference is deterministic.** To infer one schema from heterogeneous JSON or CSV,
infer a type per value and merge with fixed, written rules: nothing seen gives null, one
type stays, structs union their fields, lists merge element types, integer with float gives
float, null with a type gives that type made nullable.

- **Incompatible types are a typed conflict error or an explicit, documented fallback.** A silent fall back to string loses data and hides the bad rows.
- Field order follows first appearance (an insertion-ordered map), so the same input gives the same schema. Table-test each merge rule.
- Inference from a sample is a guess. Say how many rows were sampled, and validate the remaining rows against the result.

**Files written in parts.**

- **Clean up on failure.** A step that creates several outputs records each path as it is created and removes them all if a later step fails. A guard whose `Drop` removes them unless committed also covers panics and early returns.

```rust
pub struct OutputSet {
    paths: Vec<PathBuf>,
    committed: bool,
}

impl OutputSet {
    pub fn commit(mut self) {
        self.committed = true;
    }
}

impl Drop for OutputSet {
    fn drop(&mut self) {
        if !self.committed {
            for path in &self.paths {
                let _ = std::fs::remove_file(path); // best effort; the original error is what matters
            }
        }
    }
}
```

- A kill or power loss skips `Drop`. Write under temporary names and rename on commit, so leftovers are recognisable and a start-up sweep can remove them.
- **Validate a split by hashing:** the original through one hasher, the ordered parts through another, and compare. Where part order is not authoritative, keep a manifest with each part's index, size and hash. Tests delete a part, reorder two and flip one byte.
- **Archives need explicit parent directories.** A tar writer emits an entry for every ancestor, top-down, once each.
- **Retention deletes by reference, never by age alone.** Cleaning up old checkpoints removes a file only when no retained checkpoint refers to it: a compacted file from an old epoch may still be live. Delete data before the metadata that names it, advance the "oldest kept" marker last, and test the still-referenced case.
- Zero-pad sequence numbers in paths (`checkpoint-{epoch:07}`), so lexical order is numeric order.

**Smaller rules.**

- **Optional enrichment stays optional.** A network lookup that only improves data runs when its credential is present and its skip flag is unset, and only on entries already valid without it. The offline path and the tests work without the credential.
- **A vector with a read cursor is a queue** in allocation-free code: push to the back and advance an index. Otherwise use `VecDeque`; `Vec::remove(0)` in a loop is quadratic.
- **A failed push to a fixed-capacity container is handled,** not discarded, unless an invariant proves the capacity.
- **A size-bounded cache keeps a running total,** updated on insert and evict. Re-summing entries on every insert makes each insert linear.

**More on benchmarks.**

- **A fast path and the general path are two benchmarks over the same input,** named for the path (`dot_generic`, `dot_dense`). A specialisation with no paired benchmark has no evidence behind it.
- **A harness comparing several back ends has one outcome type,** normalised at the harness and not in each adapter. Format for display last; never mix numbers and words such as "timeout" in one column.

```rust
pub enum Outcome {
    Elapsed(Duration),
    Timeout,
    Failed(String),
}
```

- Each operation gets the same wall-clock budget, enforced per operation (`tokio::time::timeout`, or a child process killed at the deadline).
- **Name the phases** (load, start, readiness, measured loop, clean-up) and attach every metric to one. Set-up shortcuts stay out of the measured phase, and the measured path is the one users actually run.
- A run that reuses loaded data needs an explicit reset switch, and the report says whether the run was warm or cold.

### Numbers you state

- **State the gate before measuring, and report a miss plainly.** Write the threshold down first. If the run misses it, the headline says so. A feature that fails its gate ships off by default, or not at all.
- **A projected number is labelled a projection,** with the measurement that would confirm it. An estimate written like a result will be quoted as one.
- **A performance figure names its conditions:** build profile, machine, input, warm or cold, tool version. A debug-build number says nothing about release.
- **A size or cost reduction is reported with the quality it kept.** A smaller context or a faster search with unmeasured recall is not a result.
- **One or two inputs do not support a general claim.** Say how many were used and which.
- **A later result that contradicts an earlier one supersedes it visibly.** Mark the earlier document superseded; do not delete it.
- **A backtest uses only what was known at the time.** Evaluate each historical case at its own commit, and exclude signals that leak the answer.
- **A memory benchmark says which lifetime it measures.** Constructing the object fresh per iteration shows the peak a batch job would cause; reusing it shows steady state. Report allocations and peak memory, not only time.
- **Inputs that once caused a failure stay as benchmark inputs:** the huge literal, the deep nesting, the very long function.
- **A benchmark file says how to run it:** the command and features in its header, fixtures built outside the timed closure, one named case per input shape, and `Throughput::Bytes` when sizes differ so results compare as bytes per second.
- **Benchmark settings are documented environment variables, parsed once.** A malformed value is an error naming the variable, not a panic in a lazy static. Generator parameters are named constants shared with the benchmark.
- **A count names its unit and method.** A token count names its tokenizer; a line count says whether blanks and comments are included.
- **A report opens with tool version, input and totals,** so two runs can be compared.

Two last structural notes for this section:

- **Order conditions cheap and selective first.** Test the inexpensive predicate that rejects most inputs before a regex or a parse.
- **A sparse set** gives constant-time insert, membership and clear over a bounded integer universe: a dense vector of members plus a vector mapping value to dense index. It beats a bitmap that must be cleared between many small sets. Adopt it on a measurement from the real workload.

## 12. Naming, modules and documentation

### Names

**A name says what the thing is or does at the call site,** in the vocabulary of the domain.
Length follows scope: a loop index may be `i`; a public function may not be `process`.

- **Follow the Rust API naming conventions:** `as_`, `to_`, `into_` by cost; `iter`, `iter_mut`, `into_iter`; `new` and `with_` constructors; `try_` for the fallible twin; `is_` and `has_` for predicates; getters without a `get_` prefix; `_mut` and `_unchecked` suffixes.
- **Casing:** `UpperCamelCase` types and traits, `snake_case` functions and modules, `SCREAMING_SNAKE_CASE` constants. Acronyms are words: `HttpClient`, `parse_url`. Crate names avoid `-rs` and `rust-`.
- **A name carries its unit when the type does not:** `timeout_ms`, `size_bytes`. Better, let the type carry it (`Duration`, a newtype).
- **Do not repeat the module in the item:** `cache::Config`, not `cache::CacheConfig`, unless items are usually imported bare.
- **One concept, one word.** If the code says `fetch`, `load` and `get` for the same operation, the reader assumes three operations.
- **Avoid names that say nothing:** `data`, `info`, `manager`, `helper`, `util`, `handle_it`, `do_work`.
- **Booleans read as assertions,** positively: `is_enabled`, not `not_disabled` or `flag`.
- **Follow the repository's own scheme where it has one.** Some codebases adopt a fixed pattern such as four-word `verb_constraint_target_qualifier` names (`filter_implementation_entities_only`). That is a local convention: apply it there, and nowhere else by default. Never count words where the result is a worse name.
- **A risky rename of a public item is done in two steps:** add the new name, deprecate the old with `#[deprecated(note = "use `new_name`")]`, and remove it in the next major version.

### Modules and crate roots

- **A module has one reason to exist** and a name that states it. `utils`, `common` and `misc` are where unrelated code goes to be forgotten.
- **Name what the crate root exports.** Write named re-exports (`pub use counter::{LineStats, count_file};`), so the public API is readable in one place and an internal addition cannot leak. A glob re-export is acceptable only for a deliberate prelude.
- **Default to private.** `pub(crate)` for what the crate shares internally; `pub` is a promise.
- **Binary orchestration is not library API.** Argument handling and the main flow live in the binary or in private modules. `main.rs` parses, calls the library and maps the result to an exit code.
- **One module per subcommand** in a CLI, under `commands/`, with the parent module only declaring them.
- Split a file when it holds two things that change for different reasons, not at a line count.

### Documentation

- **Document the contract, not the implementation:** what it does, what it returns, when it errors (`# Errors`), when it panics (`# Panics`), what the caller must uphold (`# Safety`).
- **Comments say why.** The code already says what. A comment that restates the next line will drift from it.
- **Documentation is checked like code.** Examples are doctests, and `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps` fails on a broken intra-doc link. Libraries set `#![warn(missing_docs)]`.
- **Crate docs open with one complete example** of the main use. Mark it `no_run` when it needs a real service, and hide a `fn main() -> Result<..>` wrapper so `?` works.
- **A shipped example is a complete program:** `fn main() -> Result<(), Error>`, inputs from arguments, usage printed when one is missing.
- **A hand-written parser carries its grammar in the module doc,** and states what the module does not check.
- **Field comments give meaning, unit and format.** An analogy is not a definition.
- **Docs do not describe code that is not there.** A doc naming a crate the module no longer uses is drift; fix it in the same change as the code.
- **A workaround cites its issue.** A bound, attribute or pin that exists because of an upstream limitation carries the reference, so it can be removed later.
- **Each stable error code has a page:** what happened, usual causes, the fix. The message prints the code.
- **A shared data file opens with a legend and provenance:** every field defined, and the date and source it was synced from.
- **Diagrams follow the project's convention.** Where Mermaid is used: one statement per line, direction in the header. Do not add a diagram format the repository does not already use.
- **Never log or document secrets or sensitive payloads,** including in examples.

**Decision records** are for choices that are expensive to reverse: a foundational
dependency, a storage format, a public protocol.

- State the problem, the options considered, the choice, what was rejected and why, and **what the choice costs**.
- Give it a status: draft, accepted, superseded.
- **Say how it could be reversed:** the assumptions, the signal that would show one is wrong, and the migration in bounded steps.
- *Not for* decisions that a later commit can undo cheaply. A record for every choice is noise.

### Rules not to turn into universal law

- "Run `cargo clean` constantly": it discards the incremental cache and fixes nothing in a healthy build. Use it for a suspected stale-artefact problem.
- A fixed word count for names.
- One diagram format for all documentation.
- Doctrine copied verbatim into every plan or prompt.
- "MVP" as cover for skipping tests, contracts or verification. A smaller scope is fine; an unverified one is not.

## 13. Anti-patterns

Most of these are covered in their own sections. This is the list to scan in review. Each
has an exception, because the opposite mistake exists too.

### Reject by default

| Smell | Do instead | Legitimate exception |
|---|---|---|
| A requirement with nothing measurable ("make it faster") | A testable statement: input, expected result, threshold | Exploratory spikes, labelled as such and thrown away |
| A performance claim with no measurement | A benchmark, or a contract test that enforces the number | None; say "not measured" |
| `&Vec<T>`, `&String`, `&Box<T>` parameters | `&[T]`, `&str`, `&T` | You need `capacity()` or another method of the container itself |
| `anyhow::Error` or `Box<dyn Error>` in a library's public API | A typed error enum | Applications and binaries, where nobody matches on the error |
| `unwrap()` or `expect()` on a path input can reach | `?` and a typed error | A proven invariant, stated in the `expect` message; tests |
| Blocking work on an async executor | `spawn_blocking`, a dedicated thread, or an async API | Work bounded well under a millisecond |
| A lock guard or `RefCell` borrow held across `.await` | Copy out and drop the guard; or an async mutex where the await is the point | An async mutex guarding an I/O resource that must be used serially |
| An unbounded channel or queue | A bound, plus a stated policy when full | A provably bounded producer, with the proof in a comment |
| A spawned task with no owner | `JoinSet` or a supervisor; a cancellation path; observed failures | None in a long-running service |
| Concurrency never exercised under contention | Stress tests, `loom` for small lock-free cores, TSan | Code that is trivially confined to one thread |
| Text handling that assumes UTF-8, or one byte per character | `&[u8]`, `OsStr`, `Path`; `char_indices` for boundaries | Input already validated as `str` |
| I/O, runtime or framework types in the core domain | Pure core; adapters at the edge | Small programs where the split would be the bulk of the code |
| A struct holding the concrete database or HTTP client it uses | Depend on a narrow trait or pass a function; construct at the edge | The adapter itself |
| A "manager" struct with twenty fields | Split by responsibility and by what changes together | A plain configuration record |
| A domain model that ignores real cases | Model the cases the input actually has, or reject them explicitly | A stated, enforced subset |
| A public enum that will grow, without `#[non_exhaustive]` | Add it before the first release | Enums that are closed by definition |
| A diagnostic that drops the location | Carry file, line, column or byte span through to the message | None |
| Tests that only replay examples | Add the invariant: a property test, a round trip, a boundary table | Glue code with no invariant to state |
| Generic "so we can swap it later" | One concrete implementation; abstract at the second real use | A boundary you must fake in tests today |

A note on resource leaks: Rust closes files, sockets and locks when their owner is dropped,
so "forgot to close" is rare. The leaks that do happen are tasks and threads nobody joins,
child processes nobody waits for, temporary files, `Rc` or `Arc` cycles, entries never
removed from a long-lived map, and anything whose clean-up is async and so cannot run in
`Drop`.

### Subtler ones

- **Borrowing by habit.** Lifetimes threaded through a design, or clones hidden inside, only to avoid taking ownership of data the callee keeps anyway. If it is stored, moved to a task or outlives the call, take it owned.
- **Recovery logic keyed on message text.** Retry or fallback chosen by a substring of an error message breaks silently when the wording or a wrapper changes. Match typed variants or a retryability method.
- **The kitchen-sink error enum.** One public enum with a variant per dependency and a catch-all string. Callers cannot tell what is actionable, and every internal change is an API change. Use errors local to each boundary, expressed in that boundary's terms.
- **Dependency types in a public API.** A dependency upgrade becomes your breaking change. Wrap them. *Exception:* crates whose purpose is to extend that dependency, and vocabulary crates such as `bytes`, `http` or `serde`.
- **Trait and module sprawl.** Tiny traits and wrappers that exist to look abstract. A seam belongs at a real external or semantic boundary.
- **Accumulator soup.** Nested loops with pushes, flags and branch-specific state. Use an iterator chain or small named helpers. Keep the loop when control flow is heavy (early exits, `?`, several outputs) and the chain would be harder to read.
- **A mutable configuration blob,** patched by many call sites before use, so validity depends on timing. Validate once and hand out a frozen value.
- **A build that works only by folklore:** undocumented features, a remembered toolchain, commands that work only from one directory. Pin the toolchain, keep features additive, and run the gates from the workspace root.
- **Transport types used as domain types.** When handlers, services and storage share one DTO, every layer re-decides what is valid. Convert at the edge.
- **Speculative `unsafe` or lock-free code.** Build the safe version, measure, and only then narrow `unsafe` to the proven hot spot, with a proof plan.
- **"It compiles" offered as proof of behaviour.** The compiler proves memory and thread safety, not logic, liveness, ordering or performance. Each of those needs its own evidence.
- **Hand-edited generated code.** Regeneration discards the edit. Change the schema, the generator configuration or a wrapper module.
- **Broad desktop privilege:** wide filesystem grants, generic shell access, sidecar processes with no owner or health check. Running on the user's own machine is not an exception.
- **Hazards a signature does not show:** a guard kept alive by an iterator or a temporary in a `match` scrutinee; an `Arc` cycle; a new trait method that breaks object safety; a new auto-trait-breaking field (`Rc`, a raw pointer) that silently removes `Send` from a public type.

### Mistakes in applying this section

- **Over-correcting.** Removing every clone, making every `&str` parameter `impl AsRef<str>`, giving every function its own error enum, adding a trait to mock one call. A clone is right when it makes ownership clear and the cost is unmeasured or small. Fix the instance that hurts.
- **Fixing the symptom.** Similar symptoms need opposite fixes: a borrow error may want a clone, a restructured scope, or a different owner. Reproduce the failure in the smallest case, confirm the mechanism, then change the code. Adding a clone, a retry, a lock or a trait before that is guessing.
- **Moving a cost instead of removing it.** A convenience in one function often transfers a panic, an allocation, a queue or a compatibility burden to callers and operators. Ask who pays now.
- **The unnamed shortcut.** A design that deliberately avoids a tempting default (a clone per call, `Arc<Mutex<_>>` around everything, `Box<dyn Error>` in a public API) says so at the boundary. Otherwise the next change puts it back.

## 14. Rust web back ends

This section applies to HTTP services (Axum, Actix or similar) and their workers and queues.
Libraries, CLIs, parsers and FFI follow sections 1 to 13. The costly misrouting is a web
service reviewed as a generic library: sessions, migrations and idempotency go unexamined.

### Start from the risk

**Name the task's dominant risk before designing.** It is often not the ticket's topic.

| Risk | Typical task | What must exist before code |
|---|---|---|
| Ambiguity | New endpoint, vague request | Testable requirements, including each invalid-input case |
| Sequencing | Schema change, deploy-order change | A rollout plan with a rollback answer per step |
| Security | Auth, sessions, credentials, reset flows | Storage, failure behaviour, what an attacker learns from each response |
| Resilience | External calls, retries, workers | Failure classes, idempotency definition, the state left by a crash |
| Operations | Configuration, tracing, health, CI | Boot behaviour, what is observable, what is reversible |

- A migration's topic is schema; its risk is rollout order. A retry question is about idempotency, not about the HTTP client.
- **Re-classify mid-task.** When delivery work uncovers an auth or durability question, stop and apply that risk's rules. Consulted after the code is written, they arrive too late.
- **A task that will not classify is two tasks.** Split a migration-plus-worker ticket.
- **One service slice per change:** an endpoint or a worker, with its requirements and tests. An endpoint, its schema change and a new worker loop are three changes. Trivial read endpoints that share every boundary may be batched.
- **Version-specific crate questions are answered from `Cargo.lock` and the changelog,** not from memory. Web framework APIs change between versions.

### Layers give every failure an owner

| Layer | Owns |
|---|---|
| Transport (extractors, DTOs) | Parsing, shape and size limits, authentication of the request |
| Handler | Orchestration, mapping domain errors to responses |
| Domain types | Invariants; values that cannot be invalid |
| Persistence | Queries, transactions |
| Typed clients | Remote calls: timeouts, retries, failure classification |

- Walk a request end to end and name the owner of each step. A step with no owner is a boundary the design still owes.
- **Transport validation is not domain validation.** A DTO that deserialised is well-formed, not valid. Convert it to domain types at the edge, and pass only those inward.
- **Pools and clients are built once,** held in application state and wired in one place. A client constructed per request pays connection set-up on every call and defeats pooling.
- The layers are the rule. The crates are replaceable.

**Reject on sight in a back-end review:**

- business rules inside extractor or middleware glue;
- SQL or client construction inside handlers;
- unchecked strings travelling through the core;
- a multi-write workflow with no named transaction owner;
- a transaction held open across a remote call;
- a mutation with no idempotency definition that clients will retry;
- secrets in logs, errors or panic messages;
- environment variables read outside the settings module.

**When refactoring an existing service, fix in this order:** layer separation, edge
validation, transaction ownership, typed clients, then the worker split. Do not tune
connection pools while unchecked strings still travel through the core. Validation and
transaction ownership come first because their failures corrupt data.

### Inline or worker

**Keep work inline in the request until one of these holds:** retries must outlive the
request; the call fans out to unreliable systems; the client would wait longer than it
reasonably keeps a connection open.

- A slow remote call kept inline holds connections open and turns client retries into duplicate side effects. Keeping it inline needs a stated reason.
- **A queue needs a durability reason.** A worker hiding a simple request flow adds a second failure domain for nothing.
- When you split, define four things: what the endpoint commits, what the worker consumes, what "already processed" means, and what an operator can observe.
- Re-ask as traffic grows. An inline call that was fine at ten requests a day duplicates side effects at ten thousand, though the code never changed.

### Transactions, remote calls and retries

**Saving intent and calling a remote system in one block is correct until one half fails.**
The remote call succeeds and the commit does not, or the reverse.

- **Never hold a database transaction open across a remote call.** Remote slowness becomes pool exhaustion.
- **Use an outbox:** in one transaction, commit the state change and a row describing the side effect. A worker performs the side effect with an idempotency key and marks the row done. A crash at any point leaves a state the worker can resume.

```rust
let mut tx = pool.begin().await?;
orders::mark_paid(&mut tx, order_id).await?;
outbox::enqueue(&mut tx, OutboxMessage::SendReceipt { order_id }).await?;
tx.commit().await?;
// The worker delivers SendReceipt at least once; the receiver deduplicates on order_id.
```

- For every multi-step workflow, write down the state left by a crash after each step, and what resumes or compensates it.

**Classify remote failures before choosing a retry policy.**

| Failure | Default policy |
|---|---|
| Client error (4xx other than 408, 429) | Fail fast. A retry burns quota and cannot succeed |
| 429, 503 with `Retry-After` | Retry after the stated delay, within a budget |
| Server error, transport failure | Retry with backoff and jitter, if idempotent |
| Timeout | Outcome unknown: retry only with an idempotency key |
| Malformed response | Fail and surface to an operator; do not retry blindly |

- **A retry is safe only under an idempotency definition:** the key, what counts as the same request, what is replayed to a duplicate, and what happens when two arrive at once. A reused key with a different body is an error, not a replay.
- No blanket retry count. Retries that must outlive the request go behind a worker, and unbounded worker retries need a dead-letter state and an alert.
- Test each failure class with simulated faults, and assert that no side effect ran twice.

### Configuration and secrets

- **Parse configuration once at start-up into typed settings and fail fast.** A missing or invalid value stops the process at boot with a specific error. No `std::env::var` scattered through handlers, and no flag read lazily at first use.
- Settings hold types, not raw strings: `Url`, `Duration`, `SocketAddr`, validated newtypes.
- **Unknown keys fail the boot,** so a typo is caught at deploy. Strict-in-production and tolerant-in-development are configuration layers, not code branches.
- Configuration is supplied to the image, never baked into it.
- **Each secret field is wrapped in a redacting type** (`secrecy::SecretString` or equivalent). A derived `Debug` on the settings struct otherwise prints every secret the first time anything logs it, and a hand-written `Debug` breaks when the next field is added.
- Test it: boot with deliberately broken configuration and expect a loud, specific failure.

### Schema changes are rollouts

**A schema change that alters what running code assumes ships as ordered steps,** each its
own release:

1. **Expand:** add the new shape compatibly, with no strict constraint.
2. **Deploy code that reads and writes both shapes.** This is application work, and it is routinely underestimated because the schema diff already looks finished.
3. **Backfill.**
4. **Tighten:** add the constraint; later, remove the old shape.

- **Never merge expand and tighten because the data looks clean.** During a rolling deploy, old code is still writing the old shape. A required column added in one migration is a defect.
- **Answer five questions in writing with the code:** what lands first; which code works against both shapes; when the backfill runs; when constraints tighten; what rollback still works after each step.
- **Reversibility expires step by step.** After a backfill, some changes need a forward fix. Re-answer the rollback question after every step.
- The trigger is the kind of change, not its size, and not whether a migration file was touched: a code-only change that alters rollout behaviour needs the same plan.
- Rehearse on production-shaped data. An empty database hides lock times, foreign keys and bad rows.
- **A failed migration step is never simply rerun.** Stop, assess, and start from that step's rollback answer. A failed boot or health check changed nothing durable and may be retried automatically, under a crash-loop limit.
- Do not batch two unrelated migrations into one sequence: their rollback answers become entangled.
- Any change touching the schema runs tests against a real database with migrations applied. Green unit tests over a stale schema prove nothing.

### Operability

Three properties, each proven before it is relied on: **state is explicit at boot,
behaviour is explainable per request, and change is reversible per step.**

- **One correlation identifier per request,** propagated through every layer, into outbound calls and into worker hand-offs. A batch job correlates by job id. Test: follow one real request by identifier alone.
- **Structured traces, not formatted strings.** Record high-value fields once on the span and let them propagate. Do not trace every function entry.
- **Readiness is separate from liveness,** and reflects the dependencies the service cannot work without. Document which. Removing a slow dependency check from readiness is how a green endpoint ends up in front of a failing service.
- **Count errors, timeouts, retries and saturation** (pool waits, queue depth). Sampling high-volume reads is fine; mutations stay unsampled.
- **Before rollout, plan for a surge:** rate limits, bounded queues, request timeouts, load shedding, and the rollback procedure.
- Adopt in order: typed fail-fast configuration and redaction, then correlated tracing, then honest health checks, then CI gates and migration sequencing. Runbooks are premature for a service that prints passwords or crash-loops on a malformed variable.

**Decay happens through additions.** A new setting bypasses the settings module; a new code
path skips the correlation field; a health check stops matching the real dependency list;
each successful migration justifies less care on the next. Probe for each periodically.

### Performance of a service

**Audit four mechanisms before reading latency numbers:** pool and client reuse,
transaction scope, inline-or-worker placement, and fan-out.

- **Fix the mechanism, not the symptom.** Do not put a cache over an endpoint whose pool is exhausted by held transactions; move the remote call after the commit.
- **Averages hide the tail.** One password hash run on the async executor stalls every request on that worker thread. Measure p95 and p99.
- Require a service-specific latency objective before deployment. Absent one, a local default such as p95 under 200 ms and p99 under 500 ms for representative handlers is a starting point, not a fact about your users.
- Image builds: order layers so dependency compilation is cached separately from application source (`cargo-chef` or equivalent).

### What tests cannot show

- **Unit tests cover the layer back ends break least.** Wiring, routing, serialisation and state set-up fail in integration. Default stack: spawned-app tests on a random port with an isolated database and migrations applied; mock-server contract tests for each outbound client; property tests for domain constructors; migration tests when the schema moves.
- **Each empty, malformed and duplicate input is a named test.**
- **Ambiguity under failure passes every deterministic test.** Kill a worker mid-workflow in staging and check the state it leaves.
- Passing format, lint, tests and build is no evidence for "faster" or "safer". Each such claim needs its own measurement.

**Seven questions for any back-end review:** Are credentials typed? Are logs redacted? Are
failures shaped for the client? Are transactions explicit? Is idempotency defined for each
mutation? What state is left if the process dies mid-workflow? Should this work be
asynchronous?

**Per release, four things should be zero:** unowned transactions; retried writes with no
idempotency definition; unclassified remote failure paths; rollout steps with no rehearsed
rollback.

### The service test suite

**Choose the test kind by concern, not by rank.**

| Concern | Cheapest test that catches it |
|---|---|
| Endpoint behaviour, routing, serialisation, wiring | Spawned-app integration test over the wire |
| Domain invariants | Unit or property test |
| Queries and transactions | Integration test against a real, migrated database |
| Outbound calls | Mock-server contract test |
| Auth flows | Both: unit tests for rules, an integration pass for the wire |
| Migration safety | Schema tests plus the rollout plan |

- **Build the suite in order:** a harness that boots the app under test configuration; isolation (random port, database state per test); mocks for external calls; then helpers and property tests. If a service has no harness, building one is the first task.
- **A test reads as a user journey:** "create user, post order, expect 201 and a stored row". A helper states intent; a helper that hides the logic under test turns every failure into a harness investigation.
- **Start from the concerns a change touches,** not from the modules in the diff. No mirror tests that assert a handler returns what it returns.
- **Existing tests are copied as the style guide.** Fix a fixed-port or live-API test before adding more beside it, and stop the first bypass of the harness.
- **A mock that matches any request passes everything.** Assert the shape of the outbound request, and see that assertion fail once before trusting it.
- **Mocks drift on the provider's schedule.** Re-check each against the real contract periodically, not only when tests change.
- **A fake states what it does not reproduce.** An in-memory repository certifies domain rules, never database behaviour.
- Repair fixtures in the same change as the migration that breaks them.
- A second service in one journey calls for a contract pair, one harness test per service, not one test that spawns three services by hand.

**Reject in a service suite:** a fixed port; shared state with no documented boundary; a
live external call in the deterministic suite; automatic retries of failing tests.

**Flaky tests.**

- A deterministic failure is fixed; rerunning it changes nothing. Never merge on the third rerun's green.
- An intermittent failure is usually shared state or a missing mock. Check what the test shares first, and run the suite in shuffled order now and then.
- **Quarantine is triage, not a fix.** A quarantined test has an owner and a date, and the list is capped. A falling flake rate may only mean a growing quarantine.
- **Sharing state is the easiest speed-up and the wrong one.** Parallel runs and template databases cut set-up cost without touching isolation. A suite developers stop running locally has lost its value.

### Service building blocks

**One error family implements the response contract.** At the service boundary, one
implementation maps each variant to a status and a serialised body. Handlers never
hand-build JSON errors.

```rust
impl IntoResponse for ApiError {
    fn into_response(self) -> Response {
        let (status, code) = match &self {
            ApiError::NotFound { .. } => (StatusCode::NOT_FOUND, "not_found"),
            ApiError::Invalid { .. } => (StatusCode::UNPROCESSABLE_ENTITY, "invalid"),
            ApiError::Conflict { .. } => (StatusCode::CONFLICT, "conflict"),
            ApiError::Internal(source) => {
                tracing::error!(error = ?source, "internal error");
                (StatusCode::INTERNAL_SERVER_ERROR, "internal")
            }
        };
        (status, Json(ErrorBody { code, message: self.public_message() })).into_response()
    }
}
```

- **Internal detail is logged, not returned.** The client gets a stable code and a safe message; the cause, the SQL and the stack stay on the server, joined by the correlation id.
- A new variant gets its message, code and status in the same change. Narrow cases first, catch-all last.
- Core crates do not implement HTTP traits. The mapping lives in the service crate.

**A failure table for each route.** For every dependency a handler calls, one row: the
failure (timeout, refused, malformed reply), the status and body the client receives, what
is logged or counted, and whether the call is retried. A dependency with no row has
undecided behaviour. Each row has a test that injects the failure.

**Required and enhancing dependencies.** A required dependency fails the request. An
enhancing one degrades, with a warning and a result tagged by the path that produced it.

```rust
let primary = primary_result.map_err(SearchError::Primary)?;
let enriched = match secondary_result {
    Ok(extra) => merge(primary, extra, Source::Both),
    Err(error) => {
        tracing::warn!(%error, "secondary search failed; serving primary only");
        metrics::counter!("search_degraded_total").increment(1);
        tag(primary, Source::PrimaryOnly)
    }
};
```

- **Count each path.** A silent fallback hides an outage for as long as the primary holds.
- *No degradation* where audit or exactness requires every back end.

**One wrapper around outbound clients.** Correlation ids, trace propagation, timeouts, token
refresh and retry logging live in one wrapper, so every operation gets them.

- It maps transport status to domain errors with context from the call site: service, method and the most specific resource name (a key, a path, a secret's name and never its value). `NotFound` for a known key becomes `KeyNotFound { key }`; the rest become a generic call error carrying the code.
- Endpoint methods are domain-specific and return domain types. Status handling, decoding and URL building sit in one helper beneath them.
- It does not retry non-idempotent writes. Generated clients (gRPC, OpenAPI) are always called through it.

**Background work after the response.** Before offering a "run this later" helper, define
how tasks are registered, observed, drained and reported.

- Track them (`JoinSet`, `TaskTracker`) and await what is pending at shutdown, with a deadline. One task's failure is recorded and never blocks the drain.
- **This is not a durable queue.** Work that must survive process death goes through the outbox or a job table.

**Smaller rules.**

- **Start a new service with one thin slice** through every layer: typed input, one domain function, persistence, error mapping, a spawned-app test of success and of one failure. It settles the boundaries and the harness while they are cheap to change.
- **A module of database operations states its transaction contract:** each operation runs inside the caller's transaction; a failure that depends on current state is an error; never panic on a path user input can reach.
- **Per-tenant services** share expensive resources and cache one facade per tenant in a registry with single creation under concurrency. Tenant identity travels in request-scoped state and is validated before anything is created. *Not when* tenants need separate processes or credentials.
- **Size results for the consumer and never clip silently.** One function caps every list-returning operation and returns what was cut and how to get the next page.
- **Tool and RPC schemas are checked on the server** before dispatch, whatever the client claims to have read. One registry lists every operation; a test proves each has an implementation.
- **Pipelined protocols** enqueue a handler for each expected reply as the request is sent, and pop one per reply. A reply with no handler waiting is a protocol error. Out-of-order replies need correlation ids instead.
- **Canonical ids come from one module** (Unicode normalisation, case, separators) that every producer calls. Normalisation can collide, so pair the id with its source when uniqueness matters.
- **One function builds the invariant part of an external command,** with the variable part passed in. A logged command line can expose credentials.
- **Turning on autoscaling or rolling deploys makes the service multi-instance that day,** not at the first scale-out. Stepwise migrations become mandatory in the same change.

### Routes, authentication and readiness

**The verified type is the only way into a protected handler.** Split authentication into
an extractor that parses and one that verifies.

```rust
pub struct ValidCredentials(pub UserId);

impl FromRequestParts<Arc<App>> for ValidCredentials {
    type Rejection = StatusCode;

    async fn from_request_parts(parts: &mut Parts, state: &Arc<App>) -> Result<Self, StatusCode> {
        // `Unverified` only parses the header: malformed is 400.
        let unverified = Unverified::from_request_parts(parts, state).await?;
        state
            .auth
            .check_credentials(&unverified)
            .await
            .map(ValidCredentials)
            .ok_or(StatusCode::UNAUTHORIZED)
    }
}
```

- A protected handler takes `ValidCredentials` in its signature, so forgetting the check is a compile error, not a missing middleware line.
- **Authentication is not authorisation.** The extractor proves who; the handler, in its first lines, checks whether this user may touch this resource. 401 for no valid identity, 403 for a valid one without permission, and 404 where even existence must not leak.
- The rejection is a bare status: no detail about why verification failed.
- Multi-step flows (redirects, sessions) need middleware; an extractor does not fit them.

**Route layout.**

- One builder registers every route; each endpoint lives in its own handler module; one error type maps to responses. Split the route file by group once it stops being scannable.
- **Every path segment and query value built from data is percent-encoded.** Use the URL type's segment API, not `format!`.
- **Degraded behaviour for each downstream call is decided per method** and written beside the client: fail fast, fallback value, retry, or enqueue. Never a no-op by default: a fallback that only logs loses the work for good unless something reconciles it.
- **A handler offering buffered and streamed responses** runs one parse, validate and authorise path and branches on output mode last. An error after the first chunk cannot become a status code, so errors after headers are sent get their own tests.
- **Version negotiation is an explicit parameter** from route to domain (requested in, actual out and echoed in a header), never ambient state. When an option can arrive by query string or body, document and test the precedence.

**Readiness that depends on an expensive condition is a flag that flips once.** The probe's
fast path is one atomic load; the expensive check runs in a background task that the probe
wakes.

```rust
pub async fn check_ready(&self) -> bool {
    if self.ready.load(Ordering::Acquire) {
        return true;
    }
    self.wake_checker.notify_one();
    tokio::time::timeout(PROBE_TIMEOUT, self.wait_ready()).await.is_ok()
}

fn set_ready(&self) {
    self.ready.store(true, Ordering::Release);
    self.ready_signal.notify_waiters();
}
```

- The waiter registers its `Notified` future before re-checking the flag, or a `notify_waiters` between the check and the wait is lost.
- Once ready it stays ready. Later regressions belong to a separate health check; decide for each new criterion which of the two it is.
- Tell operators what "ready" means.

**Wire payloads become small internal types at the boundary.** JSON-RPC, server-sent events
and webhooks are framed and parsed by a real parser, then converted to a minimal internal
type with explicit defaults.

- **A malformed payload is an error, never an empty list.** "No results" and "could not parse" are different outcomes.

**One wrapper retries a transactional callback.** It owns begin, commit and rollback, the
backoff (initial delay, multiplier, jitter), an overall deadline, cancellation, and which
errors are retryable (serialisation failure, deadlock). Non-retryable errors propagate at
once.

- **The callback may run more than once,** and its documentation says so. It contains database work only: no emails, no remote calls, no mutation of outside state.

**Smaller rules.**

- **A logical write spanning several tables** is turned by one function into an ordered list of statements, parent first. A separate executor applies the list in one transaction. Parameters are bound, never formatted into SQL.
- **Recursive SQL suits graph traversal** when the graph is relational and the result joins back to relational data. Review the base case, the recursive case, the termination or depth cap, and the path reconstruction separately. A reusable path service with complex policy belongs in application code that can be unit-tested.
- **Graph and path results are parsed by the grammar,** then hydrated through an identity cache keyed by entity id, so a vertex repeated in a path is one object. Never split such values by hand.

### Process, state and storage edges

**Shutdown is a process concern.** One future, passed to the framework's graceful-shutdown
hook, waits for SIGTERM or SIGINT on Unix and Ctrl-C on Windows, and logs which arrived.
Signal handling stays out of application state and handlers.

```rust
async fn shutdown_signal() {
    let ctrl_c = async { tokio::signal::ctrl_c().await.ok(); };
    #[cfg(unix)]
    let terminate = async {
        let mut signal = signal(SignalKind::terminate()).expect("install SIGTERM handler");
        signal.recv().await;
    };
    #[cfg(not(unix))]
    let terminate = std::future::pending::<()>();
    tokio::select! { _ = ctrl_c => {}, _ = terminate => {} }
}

axum::serve(listener, app).with_graceful_shutdown(shutdown_signal()).await?;
```

- Graceful shutdown has a deadline shorter than the orchestrator's kill timeout. After the server stops accepting, drain tracked background tasks, then flush telemetry.
- A container's default stop signal is SIGTERM. A service that handles only Ctrl-C is killed mid-request on every deploy.

**A library that ships routes is generic over a state capability.** It does not fix the
host's state type. It defines a small trait for what its handlers need.

```rust
pub trait HasCommandServer {
    fn command_server(&self) -> &Arc<CommandServer>;
}

pub fn create_router<S>() -> Router<S>
where
    S: HasCommandServer + Clone + Send + Sync + 'static,
{
    Router::new()
        .route("/commands", post(create_command::<S>))
        .route("/commands/{command_id}", get(get_command_status::<S>))
}
```

- The host implements the trait on its own state, and a test uses the service itself as the state. No global singleton.
- In Axum, `FromRef` gives the same result for extracting a sub-state. Inside one application, use that and skip the trait.

**Bind to port 0 and read the port back.** A worker, agent or test server binds
`127.0.0.1:0`, takes the assigned port from `local_addr`, registers it, and only then
starts accepting. Fixed ports collide across instances and parallel tests.

**Reading a request body consumes it.** A router that picks an upstream from a body field
parses the body once into a typed enum of the payloads it supports, derives the key, and
rebuilds the upstream request from that value. Forwarding the original request after
inspecting it sends an empty body. Unsupported payloads are rejected, not passed through.

**Uploads stream into storage.** Write each chunk to the storage writer, count bytes
against a limit as they arrive, and flush explicitly.

- Body-read errors and storage-write errors are separate variants: one is the client's fault.
- A failed or oversized upload removes its partial object.
- When the whole body must be validated before any write, use a size-limited extractor with a documented limit.
- Test with a body larger than one chunk, and assert the stored length and digest.

**Archives are inspected behind a size gate,** counting uncompressed size and entry count,
not the size on the wire. Before supporting extraction, add fixtures for an entry that
escapes the target directory (`../`, an absolute path, a symlink).

**Database layer.**

- **Identifiers formatted into SQL go through one validating helper;** values are always bound parameters. There is no third case.
- **One module per aggregate,** with methods named after the domain operation (`join_channel`, not `insert_row`), taking id newtypes.
- **The database layer never sends notifications.** An operation that others must hear about returns a result naming them; the caller notifies after the commit. A notification sent inside the transaction announces something that may roll back.
- **An instant is stored in a time-zone-aware column** and mapped to `DateTime<Utc>`. When migrating a zone-less column, the migration states which zone the old values were in.
- A batch write runs in one transaction; an empty batch returns early.
- Database tests use unique table or schema names, so they can run in parallel.
- **A single-process tool may keep one SQLite connection behind a mutex.** A server uses a pool. With async code, the mutex guard must not be held across an await: run the query in `spawn_blocking`, or use an async driver.

**Clients of external APIs.**

- **The base URL is a parameter,** so tests point the client at a mock server.
- Every client sets a timeout and a user agent, and clamps paging to the provider's limits.
- Each status maps to a domain error: authentication, rate limit (after its retries), and invalid request with the provider's message parsed out.
- Tests inject the delay or use a paused clock. No real sleeps.

**Optional exporters sit behind a cargo feature;** core metrics are always compiled, and
tests run with and without the feature. An in-memory metric store has a retention bound.

### Security of a service

This is a floor, not a threat model. Authorisation design, CSRF, SSRF, key management,
dependency risk and data retention each need their own review.

**Limits on every public listener.**

| Control | Guards against | Typical tool |
|---|---|---|
| Request timeout | Slow clients holding connections | `tower_http::timeout::TimeoutLayer` |
| Body size limit | Memory exhaustion | `DefaultBodyLimit`, per-route where uploads differ |
| Rate limit | Brute force, abuse | `tower_governor`, or the gateway |
| Concurrency limit, bounded queues | Overload collapse | `ConcurrencyLimitLayer`, bounded channels |
| TLS | Interception | `rustls`, or termination at a trusted proxy |

- **Middleware order is behaviour.** A body limit placed after a layer that buffers the body protects nothing. Check order against the framework version in `Cargo.lock`.
- A rate limit keyed on client address is only as good as the address: behind a proxy, take it from the header your proxy sets, not from one the client can send.

**Secrets and credentials.**

- Credentials and tokens are typed, redacting values (`secrecy`), exposed at the one place they are used. Sensitive buffers are wiped (`zeroize`).
- **Passwords are hashed with a memory-hard function** (Argon2id) using parameters from current guidance, and verified on the blocking pool: a hash takes tens of milliseconds of CPU.
- **Secret comparison is constant-time** (`subtle`, or the verify function of the MAC or hash crate). `==` on tokens leaks through timing.
- **Reset tokens are not sessions:** random, single use, short-lived, scoped to one action, stored hashed.
- **Sessions have a revocation path.** A stateless token that cannot be revoked needs a short lifetime.
- A type wrapper is not access control. A typed `UserId` says the id is well-formed, not that the caller may use it.

**One public shape for authentication failures.** Login and reset return the same body,
status, redirect and timing whether or not the account exists. Diagnostics go to logs.

- "Same timing" means doing the same work: verify against a dummy hash when the user is unknown.
- **A product-required disclosure is an isolated exception.** If an invitation flow must reveal account state, confine it to that flow, rate-limit it and test its abuse boundary.
- A test that asserts a distinguishable response for unknown accounts encodes a defect.

**Idempotency and replay.**

- **An idempotency key is bound to the caller and the request content.** A replay never returns a response the caller is no longer authorised to see. Keys expire, and their records do not hold sensitive payloads longer than policy allows.
- **Workers acknowledge a job only after durable completion,** and tolerate duplicate delivery. Exactly-once delivery cannot be assumed, least of all across services.
- **A timeout after the remote may have acted is ambiguous, not failed.** Do not retry a charge-like effect blindly: query the provider with the idempotency key or reconcile first. A cancellation is not a failure to replay.
- **Webhook handlers verify the signature over the raw body** before parsing, store each provider event id and ignore repeats, apply status changes through explicit transitions (events arrive out of order), and are backed by periodic reconciliation with the provider.
- **Every externally visible result corresponds to a durable, authorised state.** Model each sensitive flow as an explicit state machine. An unmodelled intermediate state is the most dangerous defect: it can leak information and duplicate an effect at once.

**Observability without leaks.**

- Link events by an opaque flow id, never an email, token or key.
- No metric label or log field that reveals whether a user exists. No payload data inside idempotency keys.
- Log failures and cancellations as well as successes. Operator records have access control and bounded retention.

**Tests these flows need.**

- Compare public responses and timing for known and unknown accounts.
- Race identical writes; send concurrent requests, not only sequential ones.
- Reuse and replay reset tokens, including concurrently.
- Crash before and after the commit. Inject each remote failure class, and a timeout after the remote succeeded.
- Fixtures: an isolated database, a controlled clock and randomness, and a fake remote that can fail both before and after its effect.
- **Benchmark with the controls on.** Removing hashing, durable writes or failure shaping makes an unsafe path look fast.

**Design order for a sensitive flow:** assets and actors; what each party can observe;
durable states and effects; typed boundaries and error classes; idempotency and transaction
scope; inline or worker; abuse and crash tests; staged rollout with a rehearsed rollback.

**Release blockers:**

- raw credentials past the adapter, or secrets in logs;
- public failures that depend on whether an identity exists;
- reusable, long-lived or over-broad reset tokens;
- idempotency keys not bound to actor and request;
- a lock or transaction held across a remote effect;
- a remote call with no timeout, or a retry of a permanent failure;
- an acknowledgement before durable completion.

**Judgement calls.**

- **Deny by default.** A new route is protected until someone decides otherwise.
- **A queue moves a failure; it does not remove it.** Add background work only with a durable owner and a way for an operator to see and recover stuck jobs.
- **Retries can amplify an outage.** Bound them, add jitter, and stop when the dependency is clearly down.
- **A deploy rollback does not roll back data.**
- Prefer the design with the fewest ambiguous states over the one with the lowest latency or least code.
- When state is unclear during an incident, slow or stop intake. More requests obscure which effects already happened. Keep the evidence: do not restart in a way that erases it.

### Untrusted input at the edges

These apply to any Rust program that takes input from outside, not only to web services.

**Server-side fetch of a user-supplied URL.** One `validate_url` runs before every such
fetch.

- Allow only `http` and `https`. Reject loopback, private, link-local and cloud-metadata addresses, and internal hostnames.
- **Checking the hostname is not enough.** Resolve it, check the address, and connect to the address you checked, so a second DNS answer cannot differ.
- Validate every redirect the same way, or disable redirects. Cap the response size and set a timeout.
- Test IPv4, IPv6, IPv4-mapped IPv6 (`::ffff:127.0.0.1`), and decimal or octal spellings of an address.
- An intranet exception is an explicit allow-list, not a weaker default.

**Paths from input.** Canonicalise, then require the result to lie inside the allowed base.

```rust
fn resolve_inside(base: &Path, requested: &Path) -> Result<PathBuf, PathError> {
    let base = base.canonicalize()?;
    let candidate = base.join(requested).canonicalize()?;
    if candidate.starts_with(&base) {
        Ok(candidate)
    } else {
        Err(PathError::OutsideBase)
    }
}
```

- `canonicalize` requires the path to exist. For a file about to be created, canonicalise the parent and validate the file name separately.
- Compare with `Path::starts_with`, which works on whole components. A string prefix test accepts `/data-evil` for base `/data`.
- A check followed by a later open can be raced by a symlink swap. Where that matters, open relative to a directory handle (`cap-std`, `openat`) and do not re-resolve.

**Recursive walkers use no-follow calls.** `Path::exists` and `fs::metadata` follow links,
so a walker using them can loop forever or leave the tree. Use `fs::symlink_metadata`.

```rust
pub fn is_symlink_or_junction(path: &Path) -> bool {
    let Ok(meta) = fs::symlink_metadata(path) else { return false };
    if meta.file_type().is_symlink() {
        return true;
    }
    #[cfg(windows)]
    {
        use std::os::windows::fs::MetadataExt;
        const FILE_ATTRIBUTE_REPARSE_POINT: u32 = 0x400;
        if meta.file_attributes() & FILE_ATTRIBUTE_REPARSE_POINT != 0 {
            return true;
        }
    }
    false
}
```

- Windows junctions are reparse points, not symlinks, so check both.
- Following links is an opt-in mode with cycle detection.

**Deserialising across a trust boundary.** Use a closed schema: named fields, closed enums,
`#[serde(deny_unknown_fields)]` where an unknown field signals a mistake, and limits on
size and nesting depth. Never let untrusted input choose which type gets constructed.

**Running commands.**

- **Use `Command` with a program and separate arguments. No shell.** Arguments passed this way are not re-parsed, which removes injection at its source.
- An argument beginning with `-` can still be read as an option. Put `--` before data-derived positional arguments where the program supports it.
- **Do not pass credentials as arguments;** they appear in process listings. Use the environment, standard input or a file with restricted permissions.
- Success is the exit status or structured output, not a phrase in the text. A failed write to the child's standard input is an error.
- If shell text must be accepted, parsing it against an allow-list of programs and rejecting redirects and subshells lowers the risk. It does not make arbitrary shell text safe; say so.

**User-supplied expressions** (formulas, filters) are parsed into a syntax tree, validated
recursively against an allow-list of node kinds, operators, functions and variable names,
then evaluated in a constrained scope, with limits on depth and cost. Never hand one to a
general evaluator. An unknown name gets an error with a close-match suggestion.

**Embedding one query language in another.** Where a position cannot take a bound
parameter:

- Validate identifiers against a strict pattern such as `^[A-Za-z_][A-Za-z0-9_]*$` and reject everything else.
- Quote a free-form body with a delimiter proven absent from it. Never assume a delimiter cannot occur.
- Prefer real bind parameters wherever the driver allows them.

**Authorisation before the body.** On an upload or import route, the authorisation check
runs before anything buffers the body or spools it to disk.

- In Actix, extractors run in parameter order: put the authorising extractor first and leave a comment saying why.
- In Axum, the body extractor must be last anyway; authorise in an earlier extractor or in middleware.
- Test that an unauthorised upload creates no temporary file.

**Untrusted commands and repository configuration.** A bot, webhook handler or agent bridge
dispatches through a static table (an enum and a `match`), never by loading something named
by the input.

- **Configuration found in a repository is untrusted.** It cannot set host-only keys: secrets, filesystem paths, endpoints, the commands to run.
- Security-relevant settings are refused on the command line with a pointer to the host configuration.

**Text handed to a model or agent** passes a policy step between retrieval and
presentation: exclude by path (`.env`, `*.pem`, `*.key`, `id_rsa`), replace secret-shaped
text with a marker, and report how many items were excluded. Pattern scans miss unusual
secrets, so treat this as reduction, not a guarantee.

**Secret carriers are wiped on drop.** A struct holding key material derives
`ZeroizeOnDrop`.

```rust
#[derive(Zeroize, ZeroizeOnDrop)]
pub struct Pkcs12Archive {
    der: Vec<u8>,
    passphrase: String,
}
```

- An `into_parts()` that moves the fields out hands the duty to the caller, and says so.
- **Wiping is best effort.** It does not reach copies made by a reallocating `Vec`, a clone, a log line, or a library that kept its own buffer. Do not claim more.

**Authorisation data is indexed by the questions asked.** For hot-path checks, keep maps
shaped like the questions (`HashMap<(UserId, StreamId), Permissions>`), so a check is a
lookup or two. Every update and delete path maintains every derived set. Test that a
revoked permission is denied: a stale allow is the dangerous failure.

**State the level of evidence behind a security claim.** Documented is not configured;
configured is not reachable; tested is not deployed; observed once is not attacker-proof.
Compilation proves no authorisation property. After a framework upgrade or an advisory,
re-check behaviour against the locked version and rerun the abuse tests.

### Database access

```rust
#[derive(Clone)]
pub struct Database {
    pool: PgPool,
}

impl Database {
    pub async fn connect(settings: &DatabaseSettings) -> Result<Self, sqlx::Error> {
        let pool = PgPoolOptions::new()
            .max_connections(settings.max_connections)
            .acquire_timeout(settings.acquire_timeout)
            .connect_with(settings.connect_options())
            .await?;
        Ok(Self { pool })
    }

    pub async fn find_user(&self, id: UserId) -> Result<Option<User>, sqlx::Error> {
        sqlx::query_as!(User, "SELECT id, name, email FROM users WHERE id = $1", id.0)
            .fetch_optional(&self.pool)
            .await
    }
}
```

- **Size the pool deliberately.** Instances times `max_connections` must fit under the database's connection limit, with room for migrations and operators. Set an acquire timeout, so pool exhaustion surfaces as an error, not as requests that hang.
- **A pooled connection held is a connection denied to others.** Do not hold one across a remote call, a long computation or a slow client.
- **Compile-time checked queries** (`query!`, `query_as!`) verify SQL and types against a real schema. They need a database at build time, or prepared metadata (`cargo sqlx prepare`) committed and checked for staleness in CI. *Use the unchecked functions* for SQL assembled at run time, with bound values.
- **Where migrations run is a deployment decision.** Running them at start-up is fine for one instance. With several replicas or stepwise rollouts, run them as a separate step: replicas otherwise race, and a tightening migration applies before old code is gone.
- `fetch_optional` for zero-or-one, `fetch_one` only when absence is a bug, and a `LIMIT` on anything a user can make large.
- Map database errors to domain errors in this layer: a unique-constraint violation becomes `Conflict`, not a 500.

**A lazy result stream owns its connection.** Bundle the stream with the resource it reads
from, so a caller cannot consume rows after the transport is gone.

```rust
pub struct DetachedRowStream {
    stream: RowStream,
    connection: ManagedConnection,
}

impl DetachedRowStream {
    pub async fn next(&mut self) -> Result<Option<Row>> {
        self.stream.next(&mut self.connection).await
    }

    pub async fn finish(mut self) -> Result<RunSummary> {
        self.stream.finish(&mut self.connection).await
    }
}
```

- An open stream holds a pooled connection, so a slow consumer can starve the pool. Bound it with a timeout, or buffer fully when results are small.
- Test partial consumption followed by drop, and `finish()`.

**A query macro may read like `format!` only if every value becomes a bound parameter.**
Test both the rendered text and the parameter map. Identifiers and dynamic clauses never go
through value parameters; they have their own validation.

### A service skeleton

```rust
#[derive(Clone)]
pub struct AppState {
    db: Database,
    settings: Arc<Settings>,
}

pub fn build_router(state: AppState) -> Router {
    Router::new()
        .route("/health/live", get(|| async { StatusCode::OK }))
        .route("/health/ready", get(readiness))
        .route("/api/users", post(create_user))
        .route("/api/users/{id}", get(get_user))
        .layer(
            ServiceBuilder::new()
                .layer(TraceLayer::new_for_http())
                .layer(TimeoutLayer::new(state.settings.request_timeout))
                .layer(DefaultBodyLimit::max(state.settings.max_body_bytes))
                .layer(cors_layer(&state.settings)),
        )
        .with_state(state)
}

async fn create_user(
    State(state): State<AppState>,
    Json(request): Json<CreateUserRequest>,
) -> Result<(StatusCode, Json<UserResponse>), ApiError> {
    let new_user = NewUser::try_from(request)?; // DTO to domain type; validation lives here
    let user = state.db.insert_user(&new_user).await?;
    Ok((StatusCode::CREATED, Json(UserResponse::from(user))))
}

async fn get_user(
    State(state): State<AppState>,
    Path(id): Path<UserId>,
) -> Result<Json<UserResponse>, ApiError> {
    let user = state.db.find_user(id).await?.ok_or(ApiError::NotFound)?;
    Ok(Json(UserResponse::from(user)))
}
```

- **CORS is an allow-list from settings.** `CorsLayer::permissive()` is for local development only; combined with credentials it lets any site act as the user.
- **The router is built by a function that takes state,** so a test can build the same router against a test database.
- **Request and response types are separate from the domain type.** `User` may hold a password hash; `UserResponse` cannot.
- A create returns 201; an absent resource returns 404 through the error type, not through an `Option` serialised as `null`.
- Timeouts, body limits and state are set from typed settings, not literals in the router.
- Path syntax, layer order and extractor rules differ between framework versions. Write against the version in `Cargo.lock`.

### Configuration, storage and messaging choices

**Layered configuration:** defaults, then a file, then the environment, deserialised into
one typed struct in one place.

```rust
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
struct Settings {
    database_url: SecretString,
    workers: usize,
}

let settings: Settings = config::Config::builder()
    .set_default("workers", 4)?
    .add_source(config::File::with_name("config").required(false))
    .add_source(config::Environment::with_prefix("APP").separator("__"))
    .build()?
    .try_deserialize()?;
```

- Document the precedence. A prefix keeps unrelated environment variables out.
- Each option has one parser, one default and one range check, applied at this boundary. Test a wrong type and an out-of-range value.
- A `.env` file is a development convenience. It is not loaded in production and never committed with real secrets.

**Choosing components.** Pick on the property you need, and measure the rest.

| Need | Options | Watch for |
|---|---|---|
| Relational queries | `sqlx` (checked SQL), Diesel (typed query builder, generated `schema.rs` kept in sync), SeaORM | Async or sync; build-time database access |
| Embedded key-value | RocksDB (write-heavy, needs tuning, C++ build), LMDB (memory-mapped, fast reads, one writer), `redb` (pure Rust) | Space and write amplification; maintenance status of the crate |
| Local coordination | SQLite in WAL mode with a `busy_timeout` | One host only |
| Cache, ephemeral state | Redis through a pool | Timeouts; connections held across awaits |
| Simple pub/sub | NATS; JetStream for at-least-once | Ack waits, redelivery |
| Partitioned log | Kafka (`rdkafka`) | Rebalances, commit policy, C library build |
| Search | The official OpenSearch or Elasticsearch client | 429 with backoff; bulk requests chunked |
| Compact binary payloads | MessagePack (`rmp-serde`), Protobuf (`prost`) | Size caps; a version field |

- Check a crate's maintenance and the client library's current API before adopting it. Examples in old guides often use deprecated clients.

**Message consumers.**

- **Assume at-least-once.** Handlers are idempotent, with a dedupe key. Exactly-once is not available end to end.
- **Acknowledge or commit after processing,** not before. Committing first turns a crash into a lost message.
- **A consume loop handles its errors.** `while let Some(Ok(message)) = stream.next().await` exits silently on the first error and the consumer stops. Match on the error: log, back off and continue, or fail loudly.
- **A message that always fails goes to a dead-letter destination** after a bounded number of attempts. Otherwise it blocks its partition forever.
- Bound in-flight work, and size ack deadlines above the worst handler time.
- Choose manual or automatic offset commit explicitly, and handle rebalances: work in flight for a revoked partition may be redone elsewhere.

```rust
loop {
    match consumer.recv().await {
        Ok(message) => {
            if let Err(error) = handle(&message).await {
                dead_letter_or_retry(&message, error).await?;
            }
            consumer.commit_message(&message, CommitMode::Async)?;
        }
        Err(error) => {
            tracing::warn!(%error, "consumer error");
            tokio::time::sleep(backoff.next_delay()).await;
        }
    }
}
```

**Pooled connections** (Redis, databases) are taken for a short operation and returned. Set
a maximum size and timeouts, and do not hold one across a long chain of awaits.

**Persisted and queued payloads.**

- **Every payload carries a format version.** The version and the old-version decode branches sit beside the serialiser, not at call sites. Keep at least one old-version fixture.
- **No raw struct bytes on disk or wire.** Write fields explicitly (`to_le_bytes`) or use a derive that guarantees a padding-free layout. Padding leaks memory and breaks across compilers.
- **Untrusted binary input is size-capped** before decoding, including nested lengths. Do not rely on map key order.
- A change to serialised state updates the encoder, decoder, size constants and tests together.

**Local state and coordination.**

- **A process id does not prove identity;** ids are reused. Store the start time with it and verify before acting on a liveness record. Reconcile and delete rows of dead processes.
- **Checkpoint before side effects.** Before asynchronous work that edits user files, write the rollback data and register the pending state. Define what happens when the checkpoint itself fails.
- **Coalesced snapshot writes** (an atomic "write queued" flag, separate locks for state and file) lose the newest progress on a crash. Fine for convenience state; wrong for audit-critical state.
- **Human- or agent-edited text that updates a store is an input format:** parse into typed records, validate, apply in one transaction, verify, and only then remove or advance the input.
- **Reload is idempotent.** Remove the entries owned by a source before registering its replacement, debounce file-watch events, and keep the old entries when a reload fails on a half-written file.
- **A shared key-value store hands out scoped handles,** so the owner of each namespace is explicit.
- **Continuation tokens and bookmarks are replaced as a set** under one lock: remove the old, add the new.

**Transaction guarantees are documented where handles are created:** a read transaction is
a snapshot that may coexist with writes; a write transaction is the single writer. Keep
read transactions short, because a long-lived reader pins old state and blocks space
reclamation. Do not wrap a whole workflow in one transaction by default.

### Settings, transactions and stores: further patterns

**User-edited configuration reports typos with their path.** Collect unknown keys with the
full path, and make a type error name the field.

```rust
let mut unknown = Vec::new();
let deserializer = serde_ignored::Deserializer::new(value, |path| unknown.push(path.to_string()));
let settings: Settings = serde_path_to_error::deserialize(deserializer)?; // error names the path
if !unknown.is_empty() {
    return Err(ConfigError::UnknownKeys(unknown));
}
```

- *Not when* a file written for a newer version must still load. Then warn about unknown keys and keep going.

**A setting is a typed key** carrying its name, description, default and parser, read
through one getter that applies precedence: explicit value, environment, default.

```rust
pub struct Setting<T> {
    pub key: &'static str,
    pub description: &'static str,
    pub default: fn() -> T,
    pub parse: fn(&str) -> Result<T, SettingError>,
}
```

- **A value that fails to parse is an error naming the key and the value.** Falling back to the default silently means the operator's setting is ignored and nobody knows.
- The one tolerable exception is a pure tuning knob, and even that logs a warning.

**A knob read on a hot path is parsed once** into a `OnceLock` or `LazyLock`. Put the
parsing in a pure function that tests call directly, since the cell cannot be reset.

```rust
fn parse_budget(raw: Option<&str>) -> usize {
    raw.map(str::trim)
        .and_then(|text| text.parse::<usize>().ok())
        .filter(|budget| *budget > 0)
        .unwrap_or(DEFAULT_BUDGET)
}
```

- **Tests do not mutate the process environment.** `std::env::set_var` is `unsafe` from edition 2024 and races with other test threads. Pass the value in.
- Not for configuration that must change while the process runs.

**Ambient state.**

- **Avoid thread-local context in async code;** a task moves between threads. Pass the handle, or use `tokio::task_local!`.
- **A temporary override restores the exact previous value in `Drop`,** not a default, so nested overrides unwind correctly. Offer it as one function taking a closure, and test nesting.

**A transaction helper commits only what it began.** If it joined the caller's transaction,
it neither commits nor rolls back; the outer owner does. It retries only errors classified
as retryable, rolling back first, and its closure must be safe to run more than once.

**Several databases.** Each pool is a named field or newtype
(`struct Pools { primary: PgPool, reporting: PgPool }`), each repository takes the pool it
owns, and no transaction spans pools. Two writes to two databases are a workflow with
intermediate states, not a transaction: use the outbox.

**The outbox record.**

```rust
pub struct OutboxEntry {
    pub id: Uuid,
    pub aggregate_id: Uuid,
    pub operation: OutboxOperation,
    pub payload: serde_json::Value,
    pub created_at: DateTime<Utc>,
    pub processed_at: Option<DateTime<Utc>>,
    pub attempt_count: u32,
}
```

- The relay stamps `processed_at` on success and increments `attempt_count` on failure. After a bound, the row is parked for an operator.
- Delivery is at least once: the target deduplicates on the outbox id, and the payload carries every identifier a replay needs.
- With several relay instances, claim rows with `FOR UPDATE SKIP LOCKED` or a lease. Ordering across aggregates is not guaranteed; if order per aggregate matters, process each aggregate's rows in sequence.
- Processed rows are pruned, or the table grows without bound.
- *Not when* the second effect must be synchronous.

**External formats with several versions.** Detect the version once (an unknown version is
an error listing what was seen), convert each version to one internal form at the boundary,
and keep the raw input for audit. Everything downstream is version-agnostic; a new dialect
is a new converter.

- The same applies to files: probe at the edge (magic bytes), convert legacy formats once. A missing file, an unsupported format and a malformed one are three different errors.
- **A loader that writes a converted copy says so in its signature.** A caller expecting a read-only load must not find new files.

**Storage engines behind a trait.** The back-end trait holds only the primitives an engine
must supply (fetch, mutate, iterate). Shared query and validation logic lives once on a
generic wrapper.

```rust
pub trait Datastore {
    type Transaction<'a>: Transaction<'a> where Self: 'a;
    fn transaction(&self) -> Self::Transaction<'_>;
}

pub struct Database<D: Datastore> {
    datastore: D,
}
```

- A new operation goes on the wrapper when it can be composed from primitives, and on the trait only when an engine can do it much more efficiently.
- An optional capability is a default method returning "unsupported", and callers must handle that.
- Not worth it for a single engine.

**Hash-gated writes to a shared index.** A writer reads the local and remote content hash
before mutating, and afterwards advances the remote hash only if the two were equal. If
they differed, it warns and leaves the hash alone, so drift stays visible and a sync must
reconcile.

### Protocols and configuration discovery

**Length-prefixed messages over a byte stream.** One read is never one message. The reader
is a state machine looping over a pending buffer.

```rust
enum ReaderState {
    Header,
    Body { content_length: usize },
}

fn next_message(state: &mut ReaderState, pending: &mut BytesMut) -> Result<Option<Bytes>, FrameError> {
    loop {
        match *state {
            ReaderState::Header => {
                let Some(end) = find_header_end(pending) else {
                    if pending.len() > MAX_HEADER_BYTES {
                        return Err(FrameError::HeaderTooLong);
                    }
                    return Ok(None); // need more bytes
                };
                let content_length = parse_content_length(&pending[..end])?;
                if content_length > MAX_BODY_BYTES {
                    return Err(FrameError::BodyTooLarge { content_length });
                }
                pending.advance(end);
                *state = ReaderState::Body { content_length };
            }
            ReaderState::Body { content_length } => {
                if pending.len() < content_length {
                    return Ok(None);
                }
                *state = ReaderState::Header;
                return Ok(Some(pending.split_to(content_length).freeze()));
            }
        }
    }
}
```

- **Bound the header and the declared length before buffering.** Otherwise a peer grows your memory with one number.
- Tests: a split header, a split body, several messages in one chunk, an invalid length.
- **Prefer a maintained codec** (`tokio_util::codec::LengthDelimitedCodec`, `Framed`) when the format fits one.

**One map owns in-flight requests.** At the transport boundary, an id from a monotonic
counter maps to a `oneshot` sender.

- Success, error response, timeout and connection close each remove the entry.
- Connection close fails every waiter. A waiter left pending forever is the usual bug.
- Test all four paths, and replies arriving out of order.

**A wire encoder writes into the caller's buffer;** the allocating form is layered on top.

```rust
pub trait WireEncode {
    fn encode(&self, buf: &mut BytesMut);
    fn encoded_size(&self) -> usize;

    fn to_bytes(&self) -> Bytes {
        let mut buf = BytesMut::with_capacity(self.encoded_size());
        self.encode(&mut buf);
        buf.freeze()
    }
}
```

- `encoded_size()` and `encode()` must agree. Every wire type gets a round-trip test and `assert_eq!(x.encoded_size(), x.to_bytes().len())`.
- Not for a streaming format whose size is unknown without doing the work twice.

**Configuration discovery is one function returning an ordered list,** project-local before
the user directory.

```rust
pub fn discover() -> Result<Option<Self>, ConfigError> {
    for path in config_search_paths() {
        match fs::read_to_string(&path) {
            Ok(text) => {
                return Self::parse(&text)
                    .map(Some)
                    .map_err(|source| ConfigError::Parse { path, source });
            }
            Err(error) if error.kind() == io::ErrorKind::NotFound => continue,
            Err(source) => return Err(ConfigError::Read { path, source }),
        }
    }
    Ok(None)
}
```

- **The first file found wins, and a broken one is an error naming its path.** It never falls through to the next file or to defaults: the user would run with settings they did not write.
- Read and match on `NotFound`, as above. An `exists()` check followed by a read is a race, and it treats "permission denied" as "absent".
- `Ok(None)` means no configuration. Using defaults is then the caller's deliberate choice.
- A search up parent directories has a depth limit.
- *Skip discovery entirely* where security or reproducibility matters: take an explicit path.

**Option declarations.**

- **An option declares when it may change:** fixed after initialisation, changeable only offline, changeable live, overridable locally. A change outside its scope is a typed error at set time, not a failure later.
- **A field that may hold a secret reference is its own type:** validated on assignment, resolved through a provider at use, redacted in `Debug` and serialisation. A field accepting either a template or a concrete value is an enum of the two.
- **A registry of settings looked up by name erases types only at the registry boundary.** Each definition keeps its parser and constraint as function pointers captured where the concrete type is known. Test every definition, since a wrong downcast is a run-time failure. With no lookup by name, a plain typed struct is better.

**A database-backed store owns its connection, schema setup and statement cache behind one
handle.** Use the driver's statement cache (`prepare_cached` in `rusqlite`), and do not
share one connection across threads without a pool or a documented lock.

### Last service patterns

**A relative path in a configuration file is relative to that file,** not to the working
directory. The single load function records the file's directory, and every path field is
read through a resolver.

```rust
impl AppConfig {
    pub fn load(path: &Path) -> Result<Self, ConfigError> {
        let mut config: AppConfig = parse(&fs::read_to_string(path)?)?;
        config.base_dir = path.parent().unwrap_or(Path::new(".")).to_path_buf();
        Ok(config)
    }

    pub fn auth_env_file(&self) -> Option<PathBuf> {
        let path = Path::new(self.auth.env_file.as_deref()?);
        Some(if path.is_absolute() { path.to_path_buf() } else { self.base_dir.join(path) })
    }
}
```

- `base_dir` is private and skipped by serde. Do not derive `Default` on such a type: an empty base directory resolves silently against the working directory.

**A read-only query gate.** When users or agents may submit queries but only reads are
allowed:

- **The database enforces it:** a read-only role or connection (`SQLITE_OPEN_READ_ONLY`, a role with only `SELECT`), plus a statement timeout and a row limit.
- A validator in front is defence in depth: one shared function for every entry point, which strips literals and comments, rejects statement separators, and rejects mutating keywords on word boundaries.
- **A keyword scan alone is not a sandbox.** Functions with side effects, pragmas and writable common table expressions get past it.
- Test forbidden keywords in comments, in strings and in mixed case.

**A service address taken from the request is checked against an allow-list.** A handler
that forwards to a `url` parameter is a request-forgery hole. The default is a named
constant, overrides come from configuration, and traversal parameters such as `depth` are
bounded in the typed query struct.

**Additive schema repair for an embedded database.** An embedded SQLite application may add
missing nullable or defaulted columns at start-up by comparing `PRAGMA table_info` with the
schema in the code.

- Identifiers come from the code, never from input.
- Type changes, backfills, index rebuilds and anything destructive stay ordered migrations, tracked by a version (`PRAGMA user_version` or a migrations table).
- Test against saved copies of old database files.

**A registry of named pipelines** (tokenisers, analysers) hands out a clone, so no lock is
held while the pipeline runs. Re-registering an existing name silently invalidates data
built with the old pipeline: reject it or version the name. Freeze the registry after
start-up when persisted data depends on it.

**Result limits resolve in one helper:** configuration, then the caller's default, then a
built-in default. Clamp to at least 1. An interactive tool may log a malformed limit and
use the default; a service fails start-up.

## 15. Tauri desktop apps

A Tauri application is two programs with a trust boundary between them: a webview running
front-end code, and a Rust process with the user's privileges. Most Tauri-specific defects
live at that boundary or in the desktop lifecycle, not in either half alone.

Where Tauri's security or lifecycle rules conflict with a general Rust habit, the Tauri
rule wins. Check everything here against the project's Tauri major version: capability and
permission formats changed between 1 and 2.

### Classify the work

| The change touches | Decide first | Verify with |
|---|---|---|
| A command or event (IPC) | The typed contract: arguments, result, error shape | Rust tests of the core, a contract check both sides share, mocked-IPC front-end tests |
| Managed state | Who owns it, which lock, what crosses an await | Rust unit and concurrency tests |
| Filesystem, shell, plugin or capability scope | The narrowest permission, per window | A test that the out-of-scope call is denied |
| Sidecar or external binary | Who supervises it, how it is packaged per platform | A packaged-build check; a kill-and-restart test |
| Updater | Signing key custody, endpoint, rollback | A staged update on each platform |
| Tray, single instance, deep link, window state | The lifecycle path: cold start, already running, shutdown | Manual or automated runs on each platform |
| Front-end only, never crossing IPC | Nothing Tauri-specific | Front-end tests |

### How to work

1. **Name the boundary crossed** before anything else: which window, which command, which permission. A plan that never names a window, a permission or an IPC shape has not yet dealt with Tauri.
2. **Write requirements with a checkable outcome** (section 3). "Safer" and "more reliable" are not requirements. Do not quietly reword a vague request into a different vague one; ask.
3. **Design across four layers:** the front-end contract, the command layer, the Rust core, and the desktop permissions and lifecycle.
4. **Keep commands thin** over a core that tests without a desktop runtime. A trivial command needs no extra layer.
5. **Match each test to the boundary where the risk lives.** Passing front-end tests say nothing about the IPC contract. A permission requirement proved only by a unit test is tested in the wrong place.
6. **Run the gates and record each result:** format, lints, Rust tests, Rust build, front-end checks, Tauri build. A gate that could not run on this platform is recorded as skipped, not passed.

**Size the effort by the trust boundaries crossed, not by the diff.** A small diff that
rewrites every window's permissions is a large change. Styling that never crosses IPC needs
none of this.

**Tauri-specific failure classes to look for:**

- **A permission gap that appears only in the packaged build.** It often surfaces in the webview as a generic error. Catch it with a mocked-IPC or denied-call test before packaging.
- **Payload drift** between the front end and a command: a renamed field, a changed casing, an optional that became required.
- **An unsupervised sidecar** that dies and nothing notices.
- **A broken single-instance handoff:** the second launch's arguments or deep link never reach the first instance.
- **Behaviour that differs by platform:** paths, tray, window decorations, webview engine.

- A wrong permission or an untyped payload ships inside a binary on users' machines and cannot be hot-fixed like a server. These come before general tidiness.
- Front-end code calling `window.__TAURI__` globals with no typed wrapper has skipped the contract.
- A gate command copied from another repository can run nothing and still exit zero. Confirm it did real work.
- Classify a failing gate before rerunning it. One rerun for a transient cause; repeated silent reruns hide a real failure.
- Split the work by window or capability domain when window labels, capability files, sidecars or platform differences multiply, and add a dedicated security review.

### Requirements and design for a Tauri change

**When a request would widen permissions or weaken lifecycle safety, do not simply
comply.** Say what it weakens and propose the least-privilege version.

- Keep a repository's established permission model. Tighten it where it is broader than needed; never widen it to match an example from documentation.
- Replacing hand-written plugin bridging with an official plugin is a change to argue for, not to assume.

**Requirements name the window, the action and the bound.** Use explicit units for latency,
payload size, retries and start-up time. Keep security, lifecycle and operability as
separate requirements, not clauses of one.

| Vague | Checkable |
|---|---|
| "Add a sync feature." | A typed command validates its input, reports progress on a channel, and returns a serialisable result or a typed error. |
| "Make permissions safer." | Filesystem and plugin permissions for the `main` window are limited to the named paths and commands; a call outside them is denied. |
| "Handle start-up better." | Required state is initialised in setup without blocking the main thread; the window is interactive within the stated bound. |
| "Support tray and deep links." | Tray actions and deep links reach the primary instance, start no second set of background workers, and focus the existing window. |
| "Improve reliability." | No panic in a command or lifecycle path; errors reach the front end typed; sidecar start-up and retries are bounded. |

**Design questions, one per layer.**

| Layer | Holds | Ask |
|---|---|---|
| Front-end contract | Typed invoke arguments, results, events, channels | What exact shape may the UI rely on? |
| Command layer | `#[tauri::command]` functions, input validation, error mapping | What belongs here, and what belongs deeper? |
| Rust core | Domain logic, adapters, sidecar supervision | What must test without a desktop runtime? |
| Managed state | Shared state and its lock | What is shared, and is the lock ever held across an await? |
| Capabilities | Capability files, window labels, filesystem and plugin scope | What is the least set for these windows and these actions? |
| Lifecycle and packaging | Setup, tray, updater, single instance, deep links, bundled binaries | Who owns each background thing, and what is guaranteed per platform? |

- **Fix the invoke contract before implementing either side.** Choose the narrowest request, response or stream the UI needs.
- **Scope permissions by real window labels and concrete actions,** not by UI titles or by what a future feature might want.
- **Sidecars, updater, tray and single-instance behaviour are design decisions.** Left to the end, they become packaging surprises.

**What each kind of test can show.**

| Test | Shows | Cannot show |
|---|---|---|
| Rust unit | Core logic is correct | Anything about IPC or permissions |
| Rust integration | Commands, adapters and serialisation agree | Front-end expectations |
| Front-end test with mocked IPC | The UI handles each result and error | That the real command returns that shape |
| Shared contract check (generated bindings, or one fixture both sides parse) | The two sides agree on the payload | Behaviour |
| Mocked runtime test (`tauri::test`) | A command runs with state and a mock app handle | Real windows, permissions as packaged |
| Packaged-build run on each platform | Capabilities, sidecars, tray, deep links, updater | Nothing quickly: keep these few |
| Performance | A stated latency or payload bound | Anything, if no bound was stated |

- **Generated bindings remove payload drift at its source.** Tools such as `tauri-specta` or `ts-rs` derive the TypeScript types from the Rust ones. Without them, keep one fixture that both a Rust test and a front-end test parse.

