---
name: tir-verification-gates
description: >-
  Evidence-based verification before claiming any task, test, build, or fix is complete. Use before any completion claim, PR merge, or handoff.
---

# TIR Verification Gates

Focused skill for verifying outcomes with fresh command evidence before making completion claims. Companion reference: [reference.md](../tir-code-review/reference.md). Related: [tir-code-review](../tir-code-review/SKILL.md), [tir-root-cause-debugging](../tir-root-cause-debugging/SKILL.md).

## Rules

### Evidence

- Evidence belongs to one claim. Requirement text supports intent. Source, config and
  history support mechanism. A reproduction, test or trace supports behaviour. A support
  policy plus the target supports compatibility. An owner supports a decision. None of
  these stands in for another.
- Fresh means produced after the last consequential change to the candidate. By default,
  run the check in the same turn as the claim. A run from before an edit, rebase,
  dependency bump, config change or regeneration is history.
- Tests prove only what they exercise. A sampled review cannot show that defects are
  absent. "No issue found" always carries its scope.
- Duplicates count once: the same check run locally and in CI, the same comment made
  twice, the same document in two places.
- One red hard gate blocks the state. Passing gates are never averaged against it.
  Report each gate as `pass`, `fail`, `blocked`, `unrun`, `stale`, `conflicting` or
  `not applicable` with a reason. Never as a percentage.
- A `not applicable` needs a reason.
- Do not retry an unchanged patch, response or command hoping for a different result. A
  retry needs a named change in conditions (see Quality Gates).

### Authority and modes

A mode is a permission envelope. Pick one, say which, and do not exceed it.

| Mode | Produces | Writes code? |
|---|---|---|
| Explain | An explanation of a comment, failure or gate | No |
| Prepare request | A review request packet | No behaviour change |
| Review change | Findings and a recommendation | No |
| Intake feedback | Ledger with dispositions | No unapproved fix |
| Authorized remediation | Approved fixes plus checks | Yes, approved scope only |
| Re-review | Fresh check of the current candidate | No |
| Verify resolution | Proof that a finding is closed | Tests and probes only |
| Defer or route | Owner question, tracking, safe current behaviour | No |
| Reject or no change | Counter-evidence and the event that reopens it | No |
| Contain | Narrow, reversible, temporary reduction of active harm | Only what was authorized |
| Improve system | A new linter rule, test helper or checklist item | Yes, with an owner |

- Review-only does not edit. Intake does not decide product questions. A recommendation
  does not merge. An approval covers the exact diff it was given for and nothing after it.
- A reviewer can be right about a defect and wrong about the remedy. An owner can
  authorize a choice without making its premise true. Decide defect, remedy and authority
  separately.
- Technical success is not product, security, merge or release authority. Say "ready with
  these limits" and let the owner decide.
- One writer per file or artifact, one integration owner. Read-only checks can run in
  parallel against a frozen candidate.

### Safety

- Before any write ask: Is remediation authorized? Is the finding valid? Is all coupled
  feedback read? Is the range current and is nobody else writing here? Do I own the
  target? Are scope and compatibility preserved? Are data and commands safe? Is there a
  test that can fail? Is there an integrated check and a way back? Do current approvals
  cover this exact change? A "no" on any of these stops the write. Read-only work may go
  on.
- Keep secrets, credentials, customer payloads, raw prompts and unrelated code out of
  review requests, ledgers and reports. Link to large logs instead of pasting them.
- Edit the authoritative input of generated code, regenerate, then inspect consumers. An
  edit to the output is lost on the next generation. A direct edit of the file is valid
  only when an ownership check shows that generation was retired and the file is now
  maintained source, and only after its metadata (the header naming generator and input)
  is corrected.
- Emergency containment (drain traffic, disable a flag, revert) is allowed when it is
  authorized, narrow, reversible, keeps the evidence, and is temporary. It is not a fix
  and not completion. Investigation continues.

### Wording

- Narrow wording that follows the evidence is not hedging. "The formatter is clean" has a
  truth condition. "Probably complete" has none.
- "Should", "probably", "seems to", "looks good" before a check has run are predictions.
  Run the check or call the item a hypothesis or blocked.
- No statement of satisfaction before verification. No praise in place of analysis when
  receiving feedback. Restate the technical point or show the change.
- Prefer verbs that match the support: a policy *requires*, a source *states*, an
  inspection *found*, a run *returned / passed / failed*, an inference *suggests*, a
  search *did not find within <scope>*. Avoid "proves", "guarantees", "always", "never",
  "safe" unless the scope really supports them.
## D. Verifying Before You Claim

**The gate.** Before any status claim or expression of satisfaction:

1. **Identify** the exact claim and the command or inspection that could refute it.
2. **Run** the full check now, on the current candidate. "Full" means the full command
   that applies under the repository's instructions and is safe to run. It never means
   production effects, destructive migrations, live credentials or private data.
3. **Read** all output: exit code, counts, failures, skips, warnings, timeouts.
4. **Compare** the output with each clause of the claim.
5. **Then speak.** If it confirms: state the claim with the evidence. If not: state the
   actual status with the evidence.

Skipping a step is a false report, whatever the words used. The rule covers paraphrases,
synonyms, implications and tone.

**What each claim needs.**

| Claim | Needs | Not enough |
|---|---|---|
| Tests pass | Full applicable test command, zero relevant failures, skips and exclusions named, on this candidate | An earlier run, one focused file, "should pass" |
| Linter clean | Linter output with zero errors on the whole scope | A partial run, extrapolation |
| Build succeeds | The target build command exits 0, with generated inputs; material warnings and omitted targets named | Linter passing, a debug build standing in for release |
| Bug fixed | The original symptom reproduced red on the old code and green on the new, adjacent valid cases and the suite still pass | Code changed, reviewer approved |
| Regression test works | It fails without the fix and passes with it | It passes once on fixed code |
| Requirements met | Every accepted clause mapped to evidence or marked unresolved or routed | A green test suite |
| Artifact usable | Structure checks plus a real render and interaction for the audience: narrow and wide viewports, empty, long, loading and failure states, keyboard use and accessibility | The file exists, the build ran, one desktop render |
| Generated output correct | Authoritative input changed, regenerated, diff inspected, consumers checked | Hand-edited output |
| Migration or compatibility safe | The supported-version matrix, representative data in mixed-version states, the forward path and the rollback path, including the oldest supported version and a downgrade | The migration applied once on an empty database; success on the current version only |
| Agent completed | The actual diff and artifacts inspected, unrelated changes separated, checks rerun by you | The agent's success message |
| Review complete | Every finding has a disposition with current evidence | Threads are closed |
| Ready to merge or release | Every applicable technical, requirement, safety, policy and recovery gate passes for this exact candidate, and the owner has decided | Any stale or unrun premise |

**States.** A claim is `pass`, `fail`, `blocked`, `unrun`, `stale`, `conflicting` or
`not applicable`. Blocked is neither pass nor fail. A plan is not a result. Running a
command is not interpreting it. A bounded pass is not authorization. Keep split states
visible: a test can pass while a requirement is missing; a bug can be fixed while release
is blocked.

**Regression proof (red-green).**

```bash
git diff -- <source paths> > /tmp/fix.patch      # the fix only, not the new test
git apply -R /tmp/fix.patch && <test command>    # must FAIL, for the expected reason
git apply /tmp/fix.patch && <test command>       # must PASS
```

If reverting is unsafe, mutate in a disposable copy or argue from a source trace, and
say that the red step was substituted.

**Requirements.** Reread the plan or requirement list. Make one row per clause, including
what must not change. Check each. Report gaps. Passing tests do not define the
requirements.

**Delegated work.** A worker's report is provisional. Inspect the real files and diff
(`git status --porcelain`, `git diff --stat`), generated outputs, migrations, config, and
effects outside the repository. Separate unrelated changes. Rerun the checks that match
the claim yourself.

**When the evidence is partial or unavailable.**

- Focused pass, broader scope unrun: report the focused clause, the unrun clauses, the
  consequence and the next check. The broad claim stays blocked. Example: "The focused
  unit selection passes on the current worktree. Database integration, cancellation and
  generated artifacts were not exercised."
- No safe evaluator: report blocked, the safety boundary, what evidence exists, the owner
  route and the fallback. A substitute (static proof, simulation, disposable
  environment, specialist, owner-run) supports a narrower claim only.
- Failure: report the actual red, keep the output, and separate a real failure from an
  environment, fixture, command or requirement error.
- Conflict between two results: freeze the dependent statement, keep both scopes, and
  reconcile candidate, requirement, environment or owner.
- Earlier run now stale: demote it to history, record what invalidated it, rerun.

**Migrations and compatibility.** Passing on the current version only can break
supported users or their data. Check the forward path, the backward path and the
mixed-version state (old code on new data, new code on old data) with representative
data. If the forward migration passes but a downgrade loses data the old version needs,
readiness is `fail`, even when every normal test is green. A redesigned compatibility
path plus a verified cleanup of what the failed attempt left behind can requalify the
candidate. What the support window is remains the owner's decision.

**What invalidates a pass.** Any material edit, force-push or rebase, dependency, config,
environment or requirement change, regenerated input, or another writer touching the
surface. Owner approval does not transfer to a materially different candidate.
## Output Contract

Hand back, depending on the loop:

- **A. Request review**: the filled request packet with real SHAs and real check
  results.
- **B. Review a change**: evidence-bearing strengths (or none), findings ordered by
  consequence with `file:line`, mechanism, consequence, evidence and fix direction, the
  scope not inspected, and a bounded recommendation. No edits.
- **C. Handle feedback**: the ledger with one disposition per atomic claim, reported
  before editing; then per accepted item the change, the finding-specific proof and the
  integrated proof; the list of deferred, routed and unresolved items with owners; the
  replies posted.
- **D. Verify**: a completion report per claim, with states for every gate, limits, and
  the one allowed next action.
- **E. Debug**: the ledger, the root cause in one sentence with its trace chain, the
  failing test, the single fix, the verification result, the failed-fix count, and
  residual monitoring.

In every case also state: the mode you worked in, the exact candidate, what you did not
check, and the event that would make the result stale. If you stopped, return the stop
block instead of a partial success statement.
## Quality Gates

Run these before handing back. Replace `<...>` with the repository's own commands.

```bash
# 1. Candidate identity: the thing verified is the thing reported.
git rev-parse --abbrev-ref HEAD && git rev-parse HEAD && git status --porcelain

# 2. Full check, complete output, real exit code.
set -o pipefail
<test or build command> 2>&1 | tee /tmp/verify.log; echo "exit=$?"

# 3. Skips, warnings and partial selection are visible.
grep -n -i -E "skip|ignored|pending|xfail|deselected|todo|warning|timed out" /tmp/verify.log

# 4. Regression test can fail (red-green). See loop D.
git diff -- <source paths> > /tmp/fix.patch
git apply -R /tmp/fix.patch && <test command>; echo "expect non-zero: $?"
git apply /tmp/fix.patch && <test command>; echo "expect zero: $?"

# 5. Scoped diff: only intended files changed, no probes or debug output left behind.
git diff --stat "$BASE_SHA"..HEAD
git diff "$BASE_SHA"..HEAD | grep -n -E "^\+.*(DEBUG|console\.error\('DEBUG|print\(\"DEBUG)" || echo "no probes left"

# 6. Range has not moved since the review or the last verification.
git diff --quiet "$REVIEWED_HEAD" HEAD && echo "same candidate" || echo "stale: rerun affected gates"

# 7. No guessed waits remain in tests touched by a flakiness fix.
git grep -n -E "sleep\(|setTimeout\(|Thread\.sleep" -- '*test*' '*spec*'
```

Gate rules:

- Gate order for a review finding: request identity, complete intake, finding validity,
  remedy fit, safety and privacy, authority, finding-specific proof, integrated
  regression, audit of unresolved and deferred items, recovery.
- Gate order for a completion claim: atomic claim and next action, candidate bound,
  evaluator can fail, safety preflight, baseline or known red, focused check, integrated
  checks, requirement map, artifact inspection, delegated work reconciled, recovery,
  authority.
- Gate order for debugging: investigation notes and root cause, then one hypothesis and a
  failing test, then the pass or fail verdict and the suite, then acceptance.
- Retry is allowed only for a plausible transient on a safe, repeatable (read-only or
  idempotent) operation, with the first attempt kept in the record. A deterministic
  failure, an unknown write state after a timeout, an unsafe or unauthorized command, and
  a user stop are never retried blindly. A changed patch, test, config or environment is
  a new candidate, not a retry. Three reds followed by an unexplained green keep the
  claim blocked.
- Pick evaluators by defect class: boundary bug: the exact failing input plus empty,
  maximum, malformed, duplicate and adjacent-valid cases; error handling: a traced cause
  plus safe fault injection for timeout, partial result, cancel, retry and fallback;
  concurrency: a deterministic schedule, model or bounded stress covering reorder,
  duplicate, cancel, shutdown and contention; performance: a stated workload, a
  reproducible baseline and correctness parity; security or privacy: a stated threat
  boundary, a safe data-flow proof, a specialist-approved safe test and a policy review,
  with negative cases for an unauthorized caller, untrusted input, redaction, privilege
  and fail-closed behaviour; never offensive commands against shared or production data.
  A generic verifier cannot authorize offensive testing or accept residual risk; both go
  to the security owner.
- After every hard gate passes, and only then, rate each relevant evidence dimension
  `strong`, `mixed`, `weak` or `not applicable` with a short reason. Do not add the
  labels into a total. For review the dimensions are reviewability, finding validity,
  consequence, requirement alignment, regression coverage, evidence boundary, remediation
  fit, and lifecycle and recovery. For completion they are claim alignment, failure
  sensitivity, freshness, requirement coverage, result completeness, reproducibility,
  non-interference, safety and privacy, recovery, and lifecycle cost. The profile shows
  where two reviewers disagree (one disputes the reproduction, the other accepts the
  defect and prefers another design). It does not produce the verdict.
## Anti-Patterns

| Anti-pattern | What it looks like | Do instead |
|---|---|---|
| Context-free or moving-target request | No requirement, no range, lines drift under the reviewer | Freeze base and head, state the contract, re-evaluate on the current head |
| Review theater | Generic checklist comments, approval that cannot change the outcome | Start from outcome and risk; stage the diff; make findings atomic |
| Performative agreement | Praise or "implementing now" before the claim is checked | Restate the concern, inspect, test, classify, then act |
| Blind implementation | Applying an external suggestion because it sounds professional | Five checks for external feedback; search for usage |
| Defensive preservation | "It is intentional" or authorship in place of counter-evidence | A falsifiable counter-claim with direct evidence; accept if overturned |
| Partial implementation of unclear feedback | Doing items 1, 2, 3, 6 while 4, 5 are unclear | Pause the coupled set, ask |
| Severity laundering | Tone, reputation or a label standing in for consequence | Reclassify by reach, effect, likelihood, detection, recovery |
| Literal-comment fix | Wording satisfied, root path still fails | Trace the root and its dependents |
| Remedy conflation | Accepting the defect means adopting the reviewer's design | Accept the defect, keep the remedy open, compare alternatives |
| Unowned deferral | "Later" with no owner, trigger or safe state | Owner, tracking item, reconsideration condition |
| Thread-only closure | Thread resolved, failure remains | One authoritative ledger; proof before `resolved` |
| Stale approval replay | Old approval reused after the diff changed | Requalify the current candidate |
| Speculative claim | "Should work now", "looks correct", "done!" | Run the check or report hypothesis or blocked |
| Claim bundling | "Done" covering tests, build, requirements and readiness | Split into atomic claims, one state each |
| Activity as outcome | "I updated the handler" presented as "the bug is fixed" | Report the observed result of the original symptom |
| Proxy gate | Lint or compile presented as behaviour; a test that cannot fail for the defect | Red-green or mutation; behaviour check |
| Partial-suite inflation | One focused file reported as "all tests pass" | Report the exact subset; broad claim stays blocked |
| Hidden skip, cache-shaped green | Skipped or cached tests counted as passed | Read selection, skips, cache status |
| Summary-line trust | Reading only the last line | Read exit code, counts and warnings |
| Retry until green | Rerunning until it passes, keeping only the pass | Keep all attempts; diagnose the flake |
| Agent-report trust | Passing on a worker's "success" | Inspect the diff and artifacts, rerun |
| Requirements by tests | Green suite taken as "requirements met" | Clause-by-clause map |
| Readiness inflation | Technical pass reported as "ready to release" | Bounded recommendation; owner decides |
| Unsafe verification | Running a production migration to "prove" it | Disposable substitute or blocked |
| Fix before investigation | Patch proposed from the error message alone | Phase 1 first |
| Symptom-site patch | Null check where the error surfaces | Trace back to the original trigger |
| Shotgun fix | Several changes at once | One hypothesis, one minimal change |
| Stacked fixes | New fix on top of a failed one | Revert, return to Phase 1 |
| Fourth attempt | Trying again after three failures | Stop; architecture discussion |
| Test after the fix | "I will add the test once it works" | Failing test first |
| Guessed sleep | `sleep(500)` raised to `sleep(5000)` | Wait for the condition with a timeout |
| Borrowed fix | Adding a retry because another service needed one last week | Evidence from this failure |
| Single validation point | One check at the entry after a data bug | A check at every layer the value crosses |
| Retroactive ledger | Notes written afterwards, failures erased | Write as you go; keep refuted hypotheses |

When you catch one: withdraw or narrow the statement, restore the last verified state,
find which link broke (claim, candidate, evaluator, execution, interpretation, authority,
lifecycle), repair that link, and reverify with a check that would have caught it.
Fixing only the wording after a state has moved is not a repair.
## Self-Check Before You Finish

- [ ] I said which loop and which mode I was in, and stayed inside the mode.
- [ ] The requirement, base, head and worktree state are written down, and I checked they
      did not move.
- [ ] Every claim I make is atomic and has a state with a reason.
- [ ] Every check I cite ran after the last consequential change, and I read its exit
      code, counts, skips and warnings.
- [ ] For a bug fix: I saw the failing test red before the fix and green after it, and the
      wider suite ran.
- [ ] For review feedback: every comment has one disposition; nothing is `resolved`
      without proof; unclear coupled items were clarified before any edit.
- [ ] For a review I wrote: every finding has a location, a mechanism, a consequence and
      evidence; I listed what I did not inspect; my recommendation is bounded.
- [ ] For debugging: the trace reaches the original trigger; one hypothesis at a time;
      failed fixes are counted; I stopped at three.
- [ ] For delegated work: I inspected the real diff and reran the checks myself.
- [ ] For a migration or compatibility claim: the forward path, the backward path and the
      mixed-version state were checked on representative data, or the claim is `blocked`.
- [ ] For a comment that was plausible but unproven: it has a bounded investigation or a
      canary with a stop rule, not a `resolved` label.
- [ ] No probe, debug print or guessed sleep is left in the diff.
- [ ] No secret, credential or customer data is in any packet, ledger or reply.
- [ ] I did not run anything destructive, credentialed or production-facing to get
      evidence.
- [ ] My wording matches the evidence: no "should", "probably" or satisfaction ahead of a
      result; what the evidence does not prove is stated.
- [ ] Decisions that belong to an owner (product, security, merge, release) are routed,
      not taken.
- [ ] I named the event that makes this result stale.
