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

