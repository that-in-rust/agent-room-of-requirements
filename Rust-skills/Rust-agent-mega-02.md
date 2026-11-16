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

