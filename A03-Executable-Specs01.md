# A03: Executable Specifications for Agents

An executable specification is a small packet that turns an unclear request into
contracts someone can observe, checks that can fail, and one authorized next step.

Read this before you write code for anything that changes behaviour. It distils the
executable-spec material spread across this repo into one working procedure.
[A00](A00-LLM-Principles01.md) explains why tests are the spec.
[A01](A01-LLM-Workflow01.md) picks the process weight. This file is how you do it.

## The Short Version

```text
vague request
  -> outcome + what must not change
  -> atomic REQ contracts (WHEN / THEN / SHALL)
  -> one check per clause that can fail
  -> STUB -> RED -> GREEN -> REFACTOR -> VERIFY
  -> report evidence clause by clause
```

Ten rules carry most of the value:

1. Write the contract before the code. A failing test is a clearer target than prose.
2. One requirement, one decidable behaviour. Split anything joined by "and also".
3. Every requirement gets a stable ID, and every ID gets a check that names it.
4. A check counts only if it would fail when the behaviour is removed or reversed.
5. Specify what must stay the same, not only what is new.
6. Specify failure: empty, invalid, timeout, cancelled, duplicate, partial.
7. No number without a method. No "fast", "robust" or "secure" without a comparison.
8. Do not invent product intent. Mark it as an assumption and ask the owner.
9. A passing run is evidence for the clauses it observed, on the revision it ran on.
10. When a requirement changes, its tests, evidence and approval are stale until redone.

## What a Spec Is Not

- It is not proof the requirement is right. An ID can exist while the intent is wrong.
- It is not approval. Polished formatting does not replace an owner's decision.
- It is not a design. Constrain internals only when something external requires it.
- It is not evidence the code works. That comes from running the checks.

## Step 0: Size the Packet

Scale the spec to consequence, coupling and uncertainty. Over-specifying a typo wastes
time. Under-specifying a migration causes incidents.

**Trivial edit** (typo, rename, comment)
One statement of the intended result, the exact diff, one read-through in context.

**Bug** (something broke)
Reproduce it. Write one requirement for the correct behaviour and one regression test
that fails now. Then fix.

**Enhancement** (extend existing behaviour)
Requirements for the new behaviour plus explicit clauses for the behaviour that must
not change.

**Feature or public contract** (new capability, API, permission, data shape)
The full packet below: requirements, test matrix, TDD plan, quality gates, open
questions.

**Migration or production effect** (data, rollout, external side effects)
The full packet plus coexistence, rollback, idempotency and an owner for recovery.

## Step 1: Take In the Request

Extract five inputs. Treat them as questions to answer, not boxes the request has
already filled.

1. **Outcome.** What observable change is wanted, and who observes it?
2. **Actors and boundaries.** Who calls it, owns it, authorizes it, recovers it?
3. **Failure modes.** Which invalid, partial, duplicate, delayed or unavailable states
   matter?
4. **Performance and reliability.** Which workload, threshold, environment and
   measurement method?
5. **Language and runtime.** Which versions, platforms and dependencies constrain the
   work?

Add security, privacy, accessibility, migration or observability only when they can
change what gets accepted.

Then record two more things before writing any requirement:

- **The unchanged baseline.** What works today that this change must preserve.
- **Unknowns.** Each gap goes in Open Questions with the owner who can decide it.
  Never convert a gap into a precise-looking default.

## Step 2: Write the Contracts

Use this shape:

```markdown
### REQ-<DOMAIN>-<NNN>.<REV>: <Short title>

**WHEN** <trigger or input condition>
**THEN** the system SHALL <primary observable outcome>
**AND** SHALL <secondary measurable behaviour>
**SHALL** <edge-case or default behaviour>
```

A worked example from this repo:

```markdown
### REQ-API-001.0: Filter implementation entities

**WHEN** the caller passes a mixed entity list with implementation and interface entries
**THEN** the system SHALL return only implementation entities
**AND** SHALL preserve original ordering
**SHALL** return an empty list when no implementation entities exist
```

Rules for each requirement:

- **Atomic.** If two parts can pass or fail separately, they are two requirements.
  Keep an explicit link when they share a transaction or an ordering.
- **Observable.** State what a caller, user or operator can see at the boundary. Do
  not state private calls, class names or internal flags.
- **Stable identity.** Never reuse an ID for a different behaviour. Bump `.REV` when
  the meaning changes.
- **Edge cases in the contract.** Empty, invalid and error paths are clauses, not
  afterthoughts.
- **Functional and non-functional kept apart.** "Returns X" and "within 500 µs p99"
  are separate clauses with separate checks.

### Rewriting vague requests

| Vague | Executable |
| --- | --- |
| "Make it faster" | WHEN processing 10k items THEN p99 SHALL be under 500 µs, measured by `<bench>` on `<fixture>` |
| "Handle errors better" | WHEN the upstream times out THEN the system SHALL return `Timeout` within 2 s AND SHALL NOT retry a non-idempotent write |
| "Be robust" | WHEN input is empty THEN the system SHALL return an empty result AND SHALL NOT panic |
| "Improve search" | Not executable yet. Ask: which query, which expected result, compared to what baseline? |

If you cannot fill in the right-hand column, the request is still in elicitation.
Do not guess a threshold to make it look finished. Propose a range or a baseline
measurement and mark it provisional.

## Step 3: Map Every Clause to a Check

Build the matrix before writing code. A matrix filled in afterwards only justifies
the tests that already exist.

```markdown
| req_id | test_id | type | assertion |
| --- | --- | --- | --- |
| REQ-API-001.0 | TEST-UNIT-001 | unit | returns only implementation entries |
| REQ-API-001.0 | TEST-UNIT-002 | unit | empty input returns empty list |
| REQ-API-001.0 | TEST-INTEG-003 | integration | order preserved through parser + filter |
```

Name tests after the requirement so a search finds them:

```rust
#[test]
fn test_req_api_001_filter_implementation_entities_only() {
    // Arrange
    let input = create_test_entities_mixed_list();
    // Act
    let output = filter_implementation_entities_only(&input);
    // Assert
    assert!(output.iter().all(Entity::is_implementation));
}
```

### Pick the right kind of evidence

Choose the smallest set that covers the risk, and know what each kind does not show.

- **Unit test.** Local, deterministic behaviour. Does not show the parts work together.
- **Integration test.** Behaviour across a module, process or adapter boundary. Too
  slow to cover every edge case.
- **Doctest.** A public example that is part of the contract.
- **Compile-fail test** (`trybuild`). Misuse must not compile. Says nothing about
  run-time behaviour.
- **Property test** (`proptest`). An invariant or round trip. Does not show you
  stated the right property.
- **Fuzzing.** A parser or decoder that takes untrusted bytes. Finds panics and
  hangs, not semantic errors.
- **`loom`.** A small concurrent state machine. The model must be tiny.
- **Miri.** Unsafe code and aliasing. Covers only paths the tests execute.
- **Benchmark.** Owed only when a number was stated. Needs a representative input.
- **Snapshot test.** Large structured output. A person must read the first snapshot.
- **Review or owner decision.** For intent, policy and risk that no command can check.

Two layers apply. A small floor of commands is owed on every change. Heavier checks
are owed by the boundary the change touches: concurrency, unsafe, an input frontier,
a misuse contract. Classify the change by boundary, or it gets only the floor.

### Make sure the check can fail

A linked test name is not coverage. For each check, ask:

- Would it fail if I deleted or reversed the behaviour?
- Does it observe the outcome at the boundary, or only a proxy such as a log line or
  call count?
- Would a different correct implementation still pass it?
- Has it been seen both failing and passing?

If the honest answer is no, write the row as "not covered". An empty row is better
than an invented test name.

## Step 4: Build Test-First

```text
STUB -> RED -> GREEN -> REFACTOR -> VERIFY
```

- **STUB.** Write the test and the interface it expects. Nothing else.
- **RED.** Run it. Confirm it fails for the reason you expect: missing behaviour, not
  a typo or a broken import.
- **GREEN.** Write the smallest code that satisfies the contract.
- **REFACTOR.** Improve names and structure while the checks stay green.
- **VERIFY.** Run the full gate set and walk the matrix clause by clause.

Work one requirement at a time. After each one goes green, write a short checkpoint
(what is done, what is next, what you learned) to a file. Context windows forget;
a journal lets you or another agent resume without re-deriving the plan.

Do not edit a test to make it pass unless the requirement itself changed. If it did,
bump the revision and say so.

## Step 5: Verify Before Claiming Done

Before any completion claim:

1. Identify the command or review that would prove the claim.
2. Run it fresh and in full, after the last edit.
3. Read the output, not just the exit code. Check how many tests ran and how many
   were skipped or filtered. A filter that matches nothing passes.
4. Report what happened. Then say done or not done.

A result from before the last change proves nothing about the current code. "It
should pass" is not a result.

Quality gates for the packet:

- [ ] Every requirement has a stable `REQ-*` ID.
- [ ] Every `REQ-*` ID has at least one check that names it and can fail.
- [ ] Unchanged behaviour has regression coverage.
- [ ] Empty, invalid, timeout and error paths are covered where they matter.
- [ ] Tests pass. Build passes. Lint and format pass.
- [ ] No new `TODO`, `STUB` or `FIXME`.
- [ ] Every performance claim has a number, a method and a fixture.
- [ ] Open questions are listed with owners, not silently resolved.

For Rust, the command floor is:

```bash
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --all-targets --all-features
cargo build --all-targets --all-features
```

If a tool is unavailable, use a reviewed substitute and record the remaining risk,
or report the gate as blocked. Do not invent evidence.

## Step 6: Report by Clause

Hand off in this order:

1. **Executable Requirements.** The `REQ-*` contracts.
2. **Test Matrix.** Requirement, check, type, assertion, result.
3. **TDD Plan or Log.** What was stubbed, seen red, made green.
4. **Quality Gates.** Each gate with its actual result.
5. **Open Questions.** Unknowns, assumptions, blocked gates, owners.

Keep three labels separate in the report:

- **Verified:** observed on this revision, with the command and result.
- **Inferred:** reasoned from evidence but not directly checked.
- **Unknown:** not observed. Say so.

Bound every claim: "verified for REQ-API-001 on Linux, debug and release" is honest.
"Done" is not.

## Know Which State You Are In

Each state authorizes one kind of next action. Use the strongest state the evidence
supports, and no stronger.

- `intake` — the outcome or owner is unclear. Inspect and ask.
- `draft` — candidate requirements with explicit assumptions. Review and challenge.
- `conflicting` — sources or owners disagree. Keep the alternatives; route the
  decision. Do not pick a silent compromise.
- `experiment_ready` — behaviour is uncertain but a safe, bounded experiment is
  defined. Run it. Do not call the requirements settled.
- `review_ready` — clauses, evidence plan and open questions are complete enough for
  an owner.
- `implementation_ready` — intent is authorized and every clause has a check that
  can fail. Start test-first work inside the declared scope.
- `implemented_unverified` — code exists, evidence is incomplete. Verify or fix.
- `verified_bounded` — the current revision satisfies the declared clauses in the
  observed environment.
- `stale` — the requirement, code, environment or owner changed after evidence was
  taken. Redo the affected parts.
- `superseded` / `retired` — a newer revision replaces it, or it no longer governs.
  Remove the tests that enforced it.

One blocked clause does not block independent clauses. A failure returns you to the
earliest broken premise, not to the start.

## When Requirements Change

- Bump the revision on any change in meaning.
- Mark dependent tests, evidence and approvals stale. Rerun the smallest complete set.
- For changes to existing data or clients, add coexistence, conversion and rollback
  clauses.
- When a requirement is retired, delete or migrate its tests. Leftover tests keep
  enforcing behaviour nobody wants.
- Give every waiver an owner, a scope and a removal condition.

## Anti-Patterns

Each line is a failure, how to spot it, and what to do instead.

**Intent**

- **Invented intent.** No user statement supports a material clause.
  Keep it as an assumption and ask.
- **Approval by polish.** Nobody can say who accepted it.
  Record the owner and scope.
- **Agent-chosen policy.** A consequential default picked because it was convenient.
  Present options with consequences.

**Requirements**

- **Compound clause.** One ID hides several outcomes.
  Split it.
- **Vague quality verb.** "Improve", "optimize", "robust".
  Name the actor, input, baseline and observable result.
- **Guessed number.** No measurement or owner behind a threshold.
  Use a baseline or a provisional range.
- **Happy path only.** Every example assumes valid input.
  Add the failure clauses.
- **Missing baseline.** Only additions are specified.
  Add clauses for what must not change.
- **Mechanism binding.** The contract mandates an internal detail.
  State the outcome; put the design in a decision record.
- **Hidden environment.** Works only under an unstated version, locale or permission.
  Name it or parameterize it.

**Evidence**

- **ID-only traceability.** The test shares the ID but would pass with the behaviour
  removed.
  Break the behaviour once and watch the test fail.
- **Proxy oracle.** The test checks a log or call count while the outcome can still
  fail.
  Observe the boundary.
- **Implementation-coupled test.** A valid refactor breaks it.
  Test public behaviour.
- **Never-red gate.** The check has only ever passed.
  Treat it as advisory until it has failed on a known defect.
- **Flaky verdict.** Timing or randomness decides the result.
  Inject the clock and seed; isolate the dependency.
- **Tests exist, so done.** The handoff omits skipped checks and uncovered clauses.
  Report clause by clause.
- **Coverage as proof.** High coverage with weak assertions.
  Use coverage to find untested code, not to certify tested code.

**Lifecycle**

- **State collapse.** Draft, ready and verified share one label.
  Use the states above.
- **Revision without invalidation.** The requirement changed; the evidence still
  reads as valid.
  Mark it stale and rerun.
- **Unrecorded run.** A command ran but nobody can say on what revision.
  Capture command, revision, result and skips when you run it.
- **Placeholder shipped.** `TODO` or a stub in a change called complete.
  Finish it or narrow the claim.
- **Mixed scope.** Several features in one change, each half done.
  Finish one requirement end to end first.

## Language and Platform Notes

**Rust.** Keep invariants in the lowest layer and adapters at the edge:

```text
L1 Core:     invariants, types, traits, state rules
L2 Std:      collections, ownership, iterator and sync composition
L3 External: runtime, database, HTTP, serialization, FFI
```

Keep L3 out of L1. Put trait seams around time, randomness, storage and transport so
tests can substitute them. Prefer making a bad state unrepresentable over testing for
it. Detail: [Rust core](methodology/executable-specifications/rust/core.md) and
[Rust reference](methodology/executable-specifications/rust/reference.md).

**Tauri.** Specify the IPC boundary: typed command inputs and outputs, serializable
errors, the narrowest capability and filesystem scope, and lifecycle behaviour for
sidecars, updater and windows. Test the Rust core and the boundary separately. Detail:
[Tauri core](methodology/executable-specifications/tauri/core.md) and
[Tauri reference](methodology/executable-specifications/tauri/reference.md).

**Naming.** Where the repo uses four-word names (`verb_constraint_target_qualifier`,
for example `filter_implementation_entities_only`), new functions and tests follow it.
Do not impose it on a stable public name or a codebase that does not use it.

## Copyable Agent Prompt

```text
Turn this request into an executable specification before writing code.

Request: <paste>
Repo and runtime: <language, versions, platform>

Do this in order:
1. State the outcome, who observes it, and what existing behaviour must not change.
2. List unknowns and who can decide each. Do not fill gaps with invented defaults.
3. Write atomic requirements as REQ-<DOMAIN>-<NNN>.<REV> with WHEN / THEN / SHALL,
   including empty, invalid, timeout and error behaviour.
4. Keep performance and reliability clauses separate, each with a number and a
   measurement method, or mark them provisional.
5. Build a test matrix: req_id, test_id, type, assertion. Every clause gets a check
   that would fail if the behaviour were removed.
6. Plan STUB -> RED -> GREEN -> REFACTOR -> VERIFY, one requirement at a time.
7. After implementing, run the gates fresh, read the full output, and report per
   clause as verified, inferred or unknown.

Output sections: Executable Requirements, Test Matrix, TDD Plan, Quality Gates,
Open Questions.
Stop and ask if a material clause has no owner-backed intent.
```

## Self-Check

A spec passes if a second agent, given only the packet, can answer yes to all of
these:

- Can I tell what to build and what to leave alone?
- Can I accept or reject each clause on its own?
- Do I know which check proves each clause, and would it fail on a violation?
- Do I know what happens on bad input and on failure?
- Is every number backed by a method?
- Can I see what is assumed, unknown or blocked, and who decides?
- Do I know which next action this packet authorizes?

## Where to Read More

Load these only when the task needs the detail.

- [Core workflow](methodology/executable-specifications/core.md) — the compact skill
  this file expands.
- [Templates](methodology/executable-specifications/templates.md) — requirement,
  matrix, TDD and test skeletons for Rust, TypeScript and Go.
- [Meta-patterns](methodology/executable-specifications/meta-patterns.md) — naming,
  context budgets, agent patterns.
- [Specification skill patterns](library/idiomatic/202607/executable_specification_skill_patterns-20260710.md)
  — states, full anti-pattern registry, worked examples.
- [Traceability template patterns](library/idiomatic/202607/executable_traceability_template_patterns-20260710.md)
  — traceability as an evidence graph with invalidation.
- [Completion verification gates](library/idiomatic/202607/completion_verification_gate_patterns-20260710.md)
  — what a completion claim needs.
- [TDD cycle patterns](library/idiomatic/202607/tdd_cycle_skill_patterns-20260710.md)
  and [progress journal schema](library/idiomatic/202607/tdd_progress_journal_schema-20260710.md)
  — checkpoints and resumable handoffs.
- [Rust review skill](Rust-skills/skills/rust-review/SKILL.md) — what each gate
  proves and what it does not.
