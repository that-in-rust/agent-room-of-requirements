---
name: rust-review
description: Self-contained checklist for reviewing a Rust change or checking your own work before handoff. Use for code review of a diff or pull request, a pre-merge or pre-release check, hardening, an audit of whether the gates really ran, or as the second pass after a Rust writer skill. Covers the anti-patterns to reject, review questions by area, what each gate proves, severity levels, and extra checklists for services, Tauri apps and unsafe code. It reviews; it does not teach how to write the code.
---

# Reviewing Rust

A review answers three questions: is anything here wrong or unsafe, does the evidence
support what the change claims, and will the next person be able to change it. It is done
by someone who did not write the code, or by the writer in a deliberate second pass with
this list open. The writer remembers what the code was meant to do; the reviewer reads what
it does.

## When to use this skill

- **Use it when** reviewing a diff, a pull request or a design, before handing work over, or before a release.
- **Use it after a writer skill:** write with the skill for the kind of Rust, then review with this one in a fresh pass.
- **Skip it for** learning how to build something. It names what to reject and what to ask, and points at the fix in one line.
- **It is complete on its own.** The gate commands and the definition of done are at the end.

## How to review

**Review in rejection-first order:**

1. Read the diff for the anti-patterns below. This takes minutes.
2. Check that every requirement or claimed behaviour has a test.
3. Run the gates.
4. Check release readiness.

Do not spend a full gate run on a change a short read would reject. It is a pipeline, not a
filter to stop at: a change that passes the first read still goes through every later step.

**Questions for any review, and before any handoff:**

- What is the smallest set of checkable requirements that makes this work testable?
- Which types and invariants belong in the core, and are any leaking into adapters?
- Does the public interface expose concrete containers or dependency types it need not?
- Are error variants actionable, and do they carry context?
- Is any lock or borrow held longer than necessary, or across an await?
- Does any async path block the runtime?
- Which failure modes deserve a doc test, compile-fail test, property test, fuzz target, `loom` or Miri, not unit tests alone?
- Which public names must stay stable, even if a cleaner name exists?
- Do the tests prove every major claim the change makes?

**Design sign-off.** Before finalising a design, check:

- **Requirements:** each is checkable, with an identifier where the project uses them; preconditions, postconditions and error conditions are stated; performance claims have a measurable contract.
- **Testability:** the core can be tested without external systems. Boundaries that touch the network, the clock, the filesystem or a database are behind a seam. A trait is one kind of seam; a function parameter, a generic, or a real dependency in a container are others. Do not add a trait with one implementation only to mock it.
- **Layering:** the core is independent of transport and storage; outer dependencies are justified and few; there is a path from the simple version to the complex one.
- **Resources:** ownership ends every resource. Types that hold raw handles, or need an ordered or fallible shutdown, have an explicit close; `Drop` is the backstop. Most types need no hand-written `Drop`. Shutdown is defined and bounded.
- **Errors:** typed errors where callers branch; context added at boundaries; messages a user or operator can act on.
- **Concurrency:** shared state is identified and its synchronisation stated; ordering and cancellation are specified; tests exercise contention. Tests can find races and deadlocks, not prove their absence; say which guarantees come from types and which from testing.
- **Domain:** the data model handles real cases, not only the tidy example.
- **Verification:** each feature has one command that verifies it.

**Rules by phase:**

| Phase | Do |
|---|---|
| Requirements | Write checkable criteria; replace "better", "faster", "easier" with something measurable |
| Design | Fix the types, errors and boundaries first; decide how each will be tested |
| Implementation | Test first where the behaviour is known; use ownership for clean-up; add error context; exercise concurrency |
| Maintenance | Keep documentation checked against code; keep one command per feature; run the full suite in CI |

**Report findings by severity, most severe first,** each with the file and line, what is
wrong, why it matters and the smallest fix. Separate what you verified by running something
from what you concluded by reading. If you found nothing, say what you checked.

**Rule strength, waivers and severity.**

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

## Anti-patterns

This is the list to scan in review. Each
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

### Mistakes in applying this list

- **Over-correcting.** Removing every clone, making every `&str` parameter `impl AsRef<str>`, giving every function its own error enum, adding a trait to mock one call. A clone is right when it makes ownership clear and the cost is unmeasured or small. Fix the instance that hurts.
- **Fixing the symptom.** Similar symptoms need opposite fixes: a borrow error may want a clone, a restructured scope, or a different owner. Reproduce the failure in the smallest case, confirm the mechanism, then change the code. Adding a clone, a retry, a lock or a trait before that is guessing.
- **Moving a cost instead of removing it.** A convenience in one function often transfers a panic, an allocation, a queue or a compatibility burden to callers and operators. Ask who pays now.
- **The unnamed shortcut.** A design that deliberately avoids a tempting default (a clone per call, `Arc<Mutex<_>>` around everything, `Box<dyn Error>` in a public API) says so at the boundary. Otherwise the next change puts it back.

## Review questions by area

**Types and invariants.**

- Which invariant is carried only by a comment, not by a type or a test?
- Which primitives stand for distinct domain concepts?
- Where would a newtype, an enum or `TryFrom` remove a whole class of bug?

**Ownership and interface.**

- Where does ownership look accidental: a function that takes ownership because it was convenient, or borrows because the author avoided a move that is semantically right?
- Which clone, allocation or lock is hiding a boundary mistake?
- Which public item leaks internal storage or an adapter's shape, and will be painful to change?
- Which public error or type has committed the crate to a dependency's version?

**Errors and recovery.**

- Which error makes the caller guess how to recover?
- Are typed and dynamic errors each at the right layer?
- Where is the context too thin to diagnose a failure from the log alone?
- Are non-UTF-8 paths and binary data handled, or assumed away?

**Async and concurrency.**

- What happens under cancellation and under timeout, at each await that matters?
- Which queue, channel or fan-out has no bound, or no stated behaviour when full?
- Is any task spawned without an owner, a shutdown path and visible errors?
- Does any clean-up need awaiting or remote coordination, with no explicit shutdown API to do it?
- **Where could a logical race exist although the code is free of data races?** The compiler rules out the second, not the first: check-then-act across an await, two locks taken in different orders, stale reads between transactions.

**Architecture.**

- Are transport, domain and persistence shapes separate, and does any framework type leak inward?
- Are trait seams at real external boundaries, and absent elsewhere?
- Could a new contributor or agent build and test from the workspace root without hidden knowledge?
- Is generated code being edited as if hand-written?

**Honesty of verification.**

- Does each important claim have evidence from the current code?
- Is each bug fix backed by a test that failed before the fix?
- Does the mix of tests match where the risk is, or only where testing was easy?
- Which performance claim lacks a threshold or a profile?

**Scepticism about abstraction.**

- Which abstraction is not yet justified by reuse, an invariant or compatibility pressure?
- Is unsafe code, a procedural macro, a lock-free structure or typestate here because the problem needs it?
- Would a simpler boundary give clearer guarantees?

## Technique reminders by area

A last scan before finishing a design. None of these is a rule to apply everywhere.

- **Ownership:** move out of a `&mut` place with `mem::take` or `mem::replace` instead of cloning; move out of collections with `drain`, `pop`, `swap_remove` or `into_iter`; take owned values where the function keeps them and borrow where it only reads.
- **Resources:** fields drop in declaration order and locals in reverse, so order them when it matters; pool what is expensive to create; cap what can grow.
- **Builders:** validate in `build()` and return `Result`; use a typestate builder only when a missing field must be a compile error, since it costs readability.
- **Traits:** extension traits for foreign types; default methods to keep the required set small; sealed traits when outside implementations must be prevented. Auto traits are inferred from fields, so **adding a field can silently remove `Send` or `Sync`**; assert them in a test for public types.
- **Types:** newtypes for meaning, since a type alias gives no safety; const generics for sizes known at compile time; `Debug` on every public type, `Display` only for user-facing text.
- **Dynamic typing:** prefer enums and generics. Use `Any` or type erasure only at a real plugin or registry boundary, and keep the erased type private.
- **`Option` and `Result`:** never `if x.is_some() { x.unwrap() }`; use `if let`, `let else`, `?` or a combinator. In tests, compare whole values and test the `None` and `Err` cases explicitly.
- **Collections:** `get` where an index can be out of range; `sort_unstable` when equal elements need not keep their order; `binary_search` only on data known to be sorted; iterators in place of exposing internals.
- **Serialisation:** derive where possible; version every persisted or wire format; validate during deserialisation so invalid data never becomes a domain value.
- **Compile-time checks:** `const _: () = assert!(size_of::<T>() == N);` for layout facts that code depends on; validation in `const fn` constructors.
- **Macros:** try a function or a generic first; document every exported macro with a compiling example; debug with `cargo expand`.
- **Unsafe and panics:** keep invariants true at every point where a panic can unwind, or restore them with a guard in `Drop`.
- **FFI:** a safe owning wrapper per handle; `CStr` and `CString` at the edge; pointer plus length for arrays; one stated side allocates and frees; no panic crosses the boundary.
- **Async services:** a deadline on every external call; bounded buffers and queues; retries only for idempotent operations, with capped backoff and jitter; a circuit breaker where a failing dependency would otherwise absorb all capacity; every spawned task owned.
- **Networking:** separate connect and request timeouts; pooled connections; `rustls` unless a platform TLS stack is required; a schema for contracts shared between services.
- **Middleware:** cross-cutting concerns as Tower layers. Order is behaviour: with `ServiceBuilder` the first layer added is outermost and sees the request first.
- **I/O:** `BufReader` and `BufWriter` around files and sockets, with an explicit `flush` whose error is checked; in async code, async file APIs or `spawn_blocking`.
- **Streams:** bounded; cancellable by drop; a per-stream decision on whether an item error ends the stream or is skipped.
- **Platform code:** one module per capability with a portable fallback; detect CPU features at run time before using them.
- **Long-lived state:** an explicit state machine with validated transitions; versioned snapshots, migrated on load, with a recovery test from each persisted version.
- **Async tests:** `#[tokio::test(start_paused = true)]` and advancing time, not sleeping; injected faults (timeouts, dropped connections, partial writes); `loom` for hand-written synchronisation.
- **Tests:** table-driven cases; assertion messages that state the expected behaviour; unit tests beside the code, integration tests under `tests/`.
- **Performance:** measure, find the bottleneck, then fix in this order: algorithm, data structure, allocation, memory layout, parallelism. Stop at the stated target. SIMD, prefetching and lock-free structures need a benchmark that proves the gain.
- **Library releases:** semantic versioning checked by `cargo semver-checks`; deprecate before removing; record breaking changes in a changelog.

## What a gate proves

- **Match the gate to the obligation.** `cargo check` proves nothing about behaviour, `cargo test` proves little about concurrency, and Clippy is not design review. For an interface claim, compile a caller. For an error claim, test each variant. For a bounded channel, fill it. For cancellation, cancel.
- **Each gate proves only its own contract.** Completion is all of them together.
- **A zero exit code can hide tests that did not run.** Read the count: how many ran, how many were ignored or filtered out. A filter that matches nothing passes.
- **Run from the workspace root you mean.** A command run in one member checks that member only. With several workspaces, run the gates in each; one record must not sign for a workspace its commands never touched.
- **Where feasible, see a gate fail on the defect it guards** before trusting its pass. A test that cannot fail is not evidence.
- **Release-mode tests complement the debug run; they do not replace it.** Release removes debug assertions and overflow checks and changes optimisation-dependent behaviour. The two catch different failures.
- **If a tool is unavailable** (Miri on an unsupported target), use a reviewed substitute and record the remaining risk, or report the gate as blocked. Do not invent evidence.
- **Keep rarely run gates working.** A gate that runs only for high-risk changes breaks when it is needed most. A command copied from a guide, this one included, has been read and not run until it runs in your repository with your tool versions.

**False proxies.** Zero Clippy warnings do not prove the design. Fewer clones do not imply
speed. More traits do not imply testability. High coverage does not imply the assertions
check anything. The useful signal is fewer surprises at boundaries: callers, errors, tasks
and features behave as the design said they would.

**Two layers of gate.** The required commands are owed on every change. The heavier gates
are owed by the boundary a change touches: `loom` for hand-written synchronisation, Miri
for unsafe, fuzzing for an input frontier, compile-fail tests for a misuse contract. A
change that is never classified by boundary gets only the floor, which under-verifies
exactly the concurrent, unsafe and FFI work that needs more.

- **Scale strictness to the code.** Public, concurrent and invariant-heavy code needs stronger explicit contracts than private glue.
- **Keep the mandatory floor small** and trigger the extras by risk. Over-gating produces complaints; under-gating is silent until an incident. Check occasionally that the extra tier does run on high-risk changes.

**Scope a change by the contracts it crosses, not by its size.** Count public items,
downstream callers, error variants, spawned tasks, locks and channels, external effects,
feature sets and supported toolchains.

- A three-line patch that changes a public enum, cancellation behaviour or feature resolution needs the full treatment.
- A thousand-line mechanical rename can be reviewed as one unit once behaviour and contracts are shown unchanged.
- **A change is too large when one person cannot list the affected contracts and verify them.** Split along a public interface, a runtime lifecycle, a persistence effect or a rollback unit, and keep one owner for the integration.
- Couplings that defeat a split: shared types between nominally separate crates, feature unification, migrations that outlive binaries, and a rollback order that differs from the deployment order.

**Where a review misses callers and code:** macro expansions, build scripts, examples and
doc tests, non-default features, target-specific code, callers outside the repository, and
tests that run on a different runtime flavour from production.

**Looking up current behaviour.** Go to the owning source for the locked version: the
crate's documentation at that version, its changelog, its source. A search snippet or a
remembered API is not evidence. The usual traps are stable against nightly, major-version
differences in Tokio, Axum and Tauri, examples written against an unreleased branch, and
lints that were renamed or removed.

**How gates decay.** Each of these keeps the visible artefacts and verifies less:

- Flags trimmed from commands to save CI time. Review that as a change to the gate, not as minutes saved.
- The reading pass dropped while the badges stay green.
- Universal rules reclassified one by one as waivable conventions.
- Checklist boxes ticked from a template, with pointers that no longer resolve.

Compare the CI configuration with the stated commands now and then, and follow a sampled
pointer to its evidence. Require the commands in branch protection. A hotfix that bypasses
review under incident pressure says so and gets the review afterwards.

- **A failed required command is fixed, not rerun.** Format, lint and build are deterministic for the same source and toolchain. A test that flakes is reporting an isolation or environment defect.
- **Lint drift is not a flake.** Clippy failing right after a toolchain update is a new lint generation. Pin the toolchain and take updates as planned work, so new lints arrive on your schedule.
- **Gate cost is paid per handoff.** Automate the commands and prefer small, frequent changes. Batching work to pay the gate less often makes review shallow and defects hard to attribute.

### Gates that commands cannot run

**Traceability.** Every stated requirement has a stable identifier and at least one test
that names it. A requirement with no verification fails review. For a small change with no
formal requirements, the equivalent is: every behaviour the change claims has a test that
would fail without it.

**Structure.**

- Modules are single-purpose, and a reader can say what each is for.
- Public interfaces that others depend on are preserved, or the break is deliberate, versioned and stated.
- Names follow the repository's convention. Where it uses four-word names, new symbols do too; do not impose that on a codebase that does not, or on a stable public name.

**Runtime and safety.**

- No blocking I/O or CPU-bound work runs directly on an async executor.
- No lock guard or `RefCell` borrow is held across `.await`, unless an async mutex was chosen for that purpose.
- Cancellation, timeout and shutdown are handled wherever async work can outlive its caller.
- Every new `unsafe` block has a safety comment stating the invariant and who upholds it.
- No secret is logged, and no secret appears in an error message or a `Debug` output.

**Release readiness.**

- [ ] Requirements are checkable, and each is linked to a test.
- [ ] Tests cover the success path, the error paths and the edges, not only the example given.
- [ ] Every performance claim has a threshold, a fixture and a method.
- [ ] Concurrency claims were exercised under contention, not only single-threaded.
- [ ] Documentation and examples match current behaviour.
- [ ] No placeholder stands in for required behaviour: no `todo!()`, `unimplemented!()` or stub on a reachable path.

A `TODO` comment for work that is out of scope is acceptable when it says what and links
to where it is tracked. A `TODO` marking something this change was supposed to do is not.

### Gate discipline

**Before any claim of completion:**

1. Identify the command that would prove the claim.
2. Run it fresh and in full, after the last edit.
3. Read the output and the exit status.
4. Report what happened, and only then say done or not done.

A result from before the last change proves nothing about the code as it now is. "It
should pass" is not a result.

**A completion claim does not stand if:**

- a requirement has no test;
- a failure path that matters is untested;
- a performance claim has no measurement;
- concurrency safety is asserted, not exercised;
- a long-running task has no stated cancellation or shutdown behaviour;
- a public interface changed without a compatibility review.

**Changes that need their own look:**

- **Public interface:** leaked dependency types, the error surface, re-exports, auto traits.
- **Unsafe:** a `SAFETY` comment for the new invariant, and a targeted test, under Miri where possible.
- **Generated code:** regenerated from its true inputs and diffed, not hand-edited.
- **Lint suppressions:** each is a design decision with a stated reason.

**From rule to test to gate:**

| Rule | Evidence | Gate |
|---|---|---|
| Newtypes at boundaries | Unit tests for valid and invalid parsing | `cargo test` |
| Typestate | Compile-fail test for an illegal transition | `trybuild` suite or `compile_fail` doc test |
| Recovery-aware errors | Unit tests for the retryable and the permanent branch | `cargo test` |
| Iterator and transformation logic | Property tests for correctness and order | `cargo test` |
| Workspace and features | Build across the supported feature combinations | `cargo hack` or a CI matrix |
| No blocking, no lock across await | Clippy's `await_holding_lock` lints, review, a latency test under load | Clippy, `cargo test` |
| Bounded concurrency and cancellation | Integration tests with a deadline and a cancelled caller | `cargo test` |
| Task ownership | Teardown and failure-propagation tests | `cargo test`, `loom` for hand-written synchronisation |
| Transport to domain at the edge | Integration tests of conversion and error shaping | `cargo test` |
| Unsafe containment | Tests of the safe wrapper's invariants | `cargo miri test` |
| Explicit close and shutdown fan-out | Integration tests with a signal and a timeout | `cargo test` |
| Dependency exposure | A downstream compile, doc tests | Review, `cargo semver-checks` |
| Measure first | Benchmark with a baseline and a profile | Benchmark job |
| Everything | Format and lint | `cargo fmt --check`, Clippy with warnings denied |

A stress test passing does not prove the absence of a race or a blocked executor; it only
fails to find one. Where a rule can be checked statically (a lint, a type), prefer that to
a test that depends on timing.

### Numbers and claims

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

## Production readiness

For a service, worker or tool boundary, ask for four artefacts. Adjectives such as
"robust" and "scalable" do not stand in for them.

| Artefact | Contents |
|---|---|
| Interface contract | Input, output, error taxonomy, idempotency key, timeout, retry rule, resource bounds, owner |
| Capacity targets | p50, p95 and p99 latency, throughput, memory budget, the saturation signal, the degraded behaviour, what changes at ten times the load |
| Observability map | Which logs, metrics and traces exist, and the alert threshold for each |
| Failure drill | One dependency failure, one slow path, one malformed input and one stale input, each with the expected recovery written down |

Scale this to the thing being built. A command-line tool needs the interface contract and
the failure cases; a multi-tenant service needs all four. Inventing percentile targets for
a script is ceremony.

**Further checks:**

- **Debugging locality.** When an outcome is bad, the telemetry shows which stage produced it.
- **Rust failure modes to model:** executor starvation, unbounded task spawning, lock contention, oversized clones, error erasure and hidden blocking calls.
- **Service failure modes to model:** a dependency timeout, a partial database failure, a slow downstream service, a replayed request or token.
- **A hook or callback cannot stall its host.** It has a timeout, its failure is isolated from the caller, and each run is logged with its duration and outcome.
- **A missing configuration key never enables risky behaviour.** Defaults are the safe choice. A validation error names the field, and a rejected configuration leaves the previous one in force.
- **An extension has a compatibility contract:** version negotiation with the host, and install, update, removal and rollback that each work.
- **Generated output is reproducible.** Record the seed, the inputs and the generator version, and test that the same seed gives the same bytes.
- **Terminal output has a width contract,** with a snapshot at that width. Output that is piped, not shown on a terminal, carries no colour codes and no progress bars.
- **A deployable has an operations model:** objectives, capacity limits, deployment checks, rollback triggers and a runbook.
- **A threat model names actions, not adjectives:** what an attacker does, what each failure exposes, where the permission boundaries are, and how a new dependency is reviewed.
- **Crate health is tracked over time:** build time, test duration, dependency count, binary size. A change that grows one of them says so. Keep one cheap test tier that runs on every change.
- **Test-loop health:** flake rate and suite duration are watched. A test that never failed and a stale green check are both defects.
- **A verification record can be rerun.** Each claim carries the exact command that proves it, and evidence is stale once the code under it changes.
- **Evidence is small enough to review:** the command, pass or fail, the failing lines, the changed files and the unresolved risks. A raw transcript hides the one line that matters.
- **Shortcuts taken to make a test pass are written down,** and the list is emptied in the refactoring step, not carried into the handoff.

## Extra checks by kind of Rust

Apply the block that matches what the change touches.

### A web service or worker

**Reject on sight in a back-end review:**

- business rules inside extractor or middleware glue;
- SQL or client construction inside handlers;
- unchecked strings travelling through the core;
- a multi-write workflow with no named transaction owner;
- a transaction held open across a remote call;
- a mutation with no idempotency definition that clients will retry;
- secrets in logs, errors or panic messages;
- environment variables read outside the settings module.

**Seven questions for any back-end review:** Are credentials typed? Are logs redacted? Are
failures shaped for the client? Are transactions explicit? Is idempotency defined for each
mutation? What state is left if the process dies mid-workflow? Should this work be
asynchronous?

**Per release, four things should be zero:** unowned transactions; retried writes with no
idempotency definition; unclassified remote failure paths; rollout steps with no rehearsed
rollback.

**Release blockers:**

- raw credentials past the adapter, or secrets in logs;
- public failures that depend on whether an identity exists;
- reusable, long-lived or over-broad reset tokens;
- idempotency keys not bound to actor and request;
- a lock or transaction held across a remote effect;
- a remote call with no timeout, or a retry of a permanent failure;
- an acknowledgement before durable completion.
- **Schema change:** shipped as expand, deploy code that handles both shapes, backfill, tighten; a rollback answer exists for each step.
- **New route:** protected by default; authentication by a verified type in the signature, authorisation checked in the handler.

### A Tauri desktop application

**Before shipping a Tauri feature, verify:**

- **Commands:** structured success and structured failure; no blocking call in an async command; no `unwrap()` or `expect()` on a reachable path; names unique across modules; bytes returned as a binary response.
- **State:** the right lock for each piece; no guard across an await unless an async mutex was chosen for that reason.
- **Permissions:** each new permission is the narrowest that works; a high-privilege window inherits nothing through merged capabilities; sidecar scope names the binary and its arguments; the CSP was not widened.
- **Persistence:** stored payloads stay under their caps; files are written atomically.
- **Sidecars:** start-up has a deadline and a health check; the child is stopped on exit.
- **Lifecycle:** single-instance is registered first; deep links are validated beyond the scheme; the window does not flash on restore; tray and quit paths were run on each platform.
- **Front end:** listeners are removed on unmount; mocks are cleared between tests.
- **Build:** hooks and output paths match the front-end tooling; platform overrides are intentional and small; updater keys are not in the repository; no secret or sensitive payload is logged.

Reject by default:

- **`"permissions": ["fs:default", "shell:default"]`,** or any broad grant used as a convenience. *Fix:* exact commands with scoped paths, per window.
- **A command that takes a path, URL or shell fragment from the webview and uses it directly.** *Fix:* accept an identifier, or validate against an allow-list in Rust.
- **Events used as a data stream,** or large payloads sent as JSON. *Fix:* a channel, a binary response, or a file path.
- **The store as a blob sink.** A theme preference is fine; base64 screenshot history and multi-megabyte scrollback are not. *Fix:* files with a reference.
- **A sidecar spawned and then assumed ready, well-behaved and quiet.** *Fix:* a supervisor with a health check, a deadline, an argument scope and capped logs.
- **Opaque or unserialisable command errors,** or a front end that parses error message text.
- **String-named `invoke` calls scattered across components.**
- **Updater, tray, single-instance or deep-link behaviour verified only in `tauri dev`.**
- **Generic Rust habits overriding Tauri's rules** where they conflict: for example, renaming a command or window label for style when the name is a compatibility surface.
- **Requirements with nothing measurable** ("more reliable", "safer").

### Unsafe code and FFI

- Does every `unsafe` block have a `SAFETY` comment that names an invariant, and does the surrounding code uphold it on every path, including panics and early returns?
- Can any safe caller reach undefined behaviour through a safe function?
- Is every pointer, length and discriminant from the foreign side checked before use?
- Does every exported function catch unwinding? Is it written down which side allocates and frees each value?
- Which tool runs cover the change (Miri, sanitizers, `loom`, fuzzing), and which were skipped and why?
- If the unsafe code is an optimisation, where is the measurement?

### A parser, index, cache or other infrastructure

- No panic on any input: checked slicing and arithmetic, limits on input size and nesting depth, a fuzz target or property test.
- Offsets say what they count (bytes, characters, UTF-16 units) and are converted at one place.
- Output that reaches a file, a hash or a user is deterministic: no dependence on `HashMap` order, thread timing or traversal order.
- Every cache states its key, its bound and what invalidates an entry; the key contains every input that changes the answer.
- A performance claim has a benchmark, a baseline and stated conditions.
- A persisted format has a version, and an unreadable or truncated file is an error or a miss, never silently empty data.

### A published library

- Does the public interface expose a dependency's types, a concrete container or an error it will regret?
- Do growing enums and structs carry `#[non_exhaustive]`? Are auto traits (`Send`, `Sync`) asserted in a test for public types?
- Is the minimum Rust version declared and built in CI? Did `cargo semver-checks` run on an interface change?
- Do the documented examples compile as doc tests, and does every public item say when it errors and when it panics?

### A command-line tool

- Output on stdout, diagnostics on stderr; exit codes are deliberate and documented.
- A closed pipe ends the program quietly; non-UTF-8 paths and arguments are handled, not assumed away.
- Piped output carries no colour codes or progress bars.
- Configuration is resolved once at start-up, and a broken configuration file is an error that names the file.

## Patterns seen in production repositories

Each entry names the project it was observed in. Treat them as shapes to adapt, not as APIs to copy.

- **Coverage per crate.** A workspace total can hide one poorly tested crate. On a multi-crate release, give a readiness verdict for each crate. A line-coverage floor (75% with `cargo-llvm-cov` in the source checklist) is a gate to add when risk calls for it, not one of the default gates.
- **Failure drill.** Before calling a service ready, inject one dependency failure, one slow path, one malformed input and one stale-data case, and write down how the system recovered from each.

## Out of scope

- **Writing the code.** Use the writer skill for the kind of Rust in question.
- **A full threat model or a performance investigation.** A review flags the need for one.

<!-- core:begin -->
## Working rules shared by every Rust skill

This block is the same in every Rust skill. It covers how to work, the gates, and what
"done" means. Where the repository you are in has its own convention or gate, that wins.

**If nothing else is in reach:**

1. **Say what "correct" means before writing code,** in terms something can check.
2. **Put invariants in types** where that is cheap, and in tests where it is not.
3. **Make ownership, errors, cancellation and shutdown deliberate.** Each should be a decision someone can point to.
4. **Bound everything that can grow:** queues, buffers, retries, recursion, waits, output.
5. **Treat everything from outside the process as untrusted** until it has been parsed into a type that cannot hold the invalid form.
6. **Measure before optimising, and state the method with the number.**
7. **Follow the repository you are in** over any general convention, this skill included.
8. **Report what you ran and what you saw.** Unverified is a legitimate status; passing it off as verified is not.

### Size the process to the task

| Task | Process that fits |
|---|---|
| Rename, comment, one-line fix covered by an existing test | Read the code and its callers, change it, run the gates |
| Bug fix | Reproduce it with a failing test, fix, run the gates |
| Feature inside one module | A short list of checkable requirements, tests first, implement |
| New public API, a change that crosses a boundary, concurrency, unsafe | Requirements, design of types and boundaries, a chosen test mix, then code |

Process heavier than the task buries the change the reviewer has to check. Process lighter
than the task is how a "small" change to an error type or a lock ships a regression.

### Working with the compiler and the ecosystem

- **Fix the first error first.** Later errors are often cascades. Read the whole message, including the `help:` and `note:` lines. Run `cargo check` after each small edit, not after three hundred lines.
- **A borrow-checker error is design information.** Before adding `.clone()`, `Rc<RefCell<_>>`, `Arc<Mutex<_>>` or `'static` to make it compile, say who owns the value and how long the borrow must live. A clone is fine when the value is small or the path is cold; it is wrong when it silently forks state that was meant to be shared.
- **Never guess an API.** Find the version in `Cargo.lock`, then read the documentation for that version or the source under `~/.cargo/registry/src`. Widely used crates change shape between major versions, and code remembered from one version fails on another.
- **Check the edition and the minimum Rust version** (`edition` and `rust-version` in `Cargo.toml`) before using a newer language feature.
- **Match the codebase.** Use its error crate, runtime, logging, naming and module layout. A second way of doing the same thing is a cost every later reader pays.
- **Keep the diff to the task.** No drive-by reformatting, renames or dependency upgrades. Report what you noticed; do not fix it uninvited.
- **Add a dependency deliberately.** Check that std or an existing dependency does not already do it, look at maintenance and licence, enable only the features needed, and say in the handover that you added it.
- **Read before you write.** Read the function you change, its callers and its tests.
- **A red test must be red for the right reason:** it fails on the assertion, not on a compile error or a set-up mistake.
- **Debug in a loop with a stop condition.** Reduce to the smallest reproduction, test one hypothesis per probe, and stop when a regression test fails for the confirmed cause. A plausible story is not a diagnosis.

### What the compiler does not prove

- It proves memory and type properties. It proves nothing about domain correctness, performance, cancellation behaviour or compatibility.
- Code that compiles with clones everywhere has not shown the clones are right.
- No data race does not mean no logical race: check-then-act across two lock acquisitions, dropped work and stale reads all compile.

### The required gates

Cheapest first, so the fastest check fails first:

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-targets --all-features
cargo test --workspace --doc --all-features
```

- **Use the repository's own gate if it has one** (a `just` or `make` target, a CI script). These commands are the default when there is none.
- **`--all-targets` does not run doc tests.** They need the separate `--doc` run.
- **Clippy without `-D warnings` is not the gate.** It prints and passes.
- **`--all-features` is wrong for crates with mutually exclusive features.** Test the supported combinations explicitly.
- Run from the workspace root you mean. A command run in one member checks that member only.
- **A zero exit code can hide tests that did not run.** Read the count: how many ran, how many were ignored or filtered out.

Run a heavier gate when the change touches its risk, and say so when you skip one:

| Gate | Run it when |
|---|---|
| `cargo test --release` | Behaviour could differ with optimisation: overflow checks, `debug_assert`, timing, unsafe code |
| `cargo +nightly miri test` | Unsafe code changed |
| `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps` | Public items or documentation changed |
| `cargo deny check` or `cargo audit` | Dependencies changed |
| `cargo semver-checks` | A published library's public interface changed |
| Benchmarks against a baseline | A performance claim is made, or a hot path changed |

### Before claiming done

1. Identify the command that would prove the claim.
2. Run it fresh and in full, after the last edit.
3. Read the output and the exit status.
4. Report what happened, and only then say done or not done.

- **"It compiles" is not done.** Done is: the required gates green on the final code, and the claimed behaviour covered by tests.
- **If you could not run a command, say so and list it for a human.** Never report an unrun command as passed, and never describe output you did not see. "Skipped" is not "passed".
- **Do not weaken a check to make it pass:** no deleted or `#[ignore]`d test, no loosened assertion, no blanket `#[allow]`, no special case for the test's input. If a test is wrong, say so and fix the test as its own visible change.
- **Before handoff, search your own diff** for `todo!()`, `unimplemented!()`, `dbg!`, stray `println!`, commented-out code and placeholder `TODO` markers.
- **Never invent an identifier, a number or a citation** to satisfy a checklist. If an item does not apply, say why.
- **No secret reaches a log, an error message or a `Debug` output.** No compiler checks this; look at debug, error and crash paths.

**The record at handoff:** the commands run, their results and the toolchain version;
which heavier gates ran or were skipped, with the reason; what was verified by test, what
by reading, and what not at all; known limitations and anything left for a human.
<!-- core:end -->
