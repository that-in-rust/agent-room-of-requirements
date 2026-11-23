---
name: tir-root-cause-debugging
description: >-
  Systematic root-cause debugging for test failures, production bugs, flaky behaviour, and unexpected regressions. Use whenever a failure cause is unknown before proposing any fix.
---

# TIR Root-Cause Debugging

Focused skill for isolating, reproducing, and proving root causes before editing code. Companion reference: [reference.md](../tir-code-review/reference.md). Related: [tir-verification-gates](../tir-verification-gates/SKILL.md), [tir-code-review](../tir-code-review/SKILL.md).

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
## E. Debugging to Root Cause

Use for any technical failure: test failures, build failures, production bugs, wrong
results without an error, performance problems, integration issues, flaky CI. Use it
hardest when a quick fix looks obvious, when you are in a hurry, and when a fix has
already failed. A simple bug still has a root cause; its investigation is just short (one
look at the format string for a log typo). Rigor of phase order does not scale down with
severity. Only the size of the notes does.

Keep a debugging ledger from the start (Templates). Fill it as you go, not afterwards,
and never delete a failed hypothesis.

### Phase 1: Investigate the root cause

No fix is proposed until this phase is complete.

1. **Read the error completely.** Whole message, whole stack trace, warnings before it,
   file paths, line numbers, error codes. The answer is often in the text.
2. **Reproduce it.** Exact steps. Every time or sometimes? If it cannot be reproduced,
   gather more data. Do not guess.
3. **Check what changed.** Recent commits, the diff, new dependencies, config,
   environment differences between where it works and where it fails.

   ```bash
   git log --oneline -15
   git diff <last-known-good>..HEAD --stat
   git bisect start && git bisect bad && git bisect good <last-known-good>   # then: git bisect run <failing command>
   ```

4. **Instrument every component boundary** when several components are involved (CI to
   build to signing, API to service to database). At each boundary log what enters, what
   leaves, whether config and environment arrived, and the state. Run once. Read where it
   breaks. Then investigate that component only.

   ```bash
   [ -n "${DEPLOY_TOKEN:-}" ] && echo "== workflow: DEPLOY_TOKEN set" || echo "== workflow: DEPLOY_TOKEN unset"
   # in the build script:
   env | grep -c '^DEPLOY_' ; echo "== build: cwd=$(pwd) node=$(node -v)"
   # in the service:
   curl -s -o /dev/null -w "== service: status=%{http_code} time=%{time_total}\n" "$SERVICE_URL/health"
   # in the database step:
   psql "$DATABASE_URL" -c 'select 1' >/dev/null && echo "== db: reachable" || echo "== db: unreachable"
   ```

   Print whether a secret is set, never its value. Verify the channel before trusting
   silence: suppressed test loggers, sampled traces and buffered stdout can hide the one
   probe that matters. Probes are disposable. Remove them afterwards and keep only what
   is useful as proper logging.
5. **Trace the bad value backward.** Start at the symptom. Ask "what code directly did
   this?", "what called it?", "what value was passed?", "where did that value come
   from?" Repeat until you reach the place where the value first became wrong. That is
   where the fix goes. When you cannot trace by reading, capture a stack just before the
   dangerous operation, on a channel the test runner does not swallow:

   ```js
   console.error('DEBUG before git init', { directory, cwd: process.cwd(), env: process.env.NODE_ENV, stack: new Error().stack });
   ```

   ```python
   import sys, os, traceback
   print("DEBUG before init", {"directory": directory, "cwd": os.getcwd()}, file=sys.stderr); traceback.print_stack(file=sys.stderr)
   ```

   ```bash
   <test command> 2>&1 | grep -A 30 'DEBUG before'
   ```

   Log before the operation, not after it fails. Include directory, working directory,
   environment and a timestamp.
6. **Find the polluting test** when a file or state appears during a test run and you do
   not know which test creates it. Run test files one at a time and stop at the first
   one after which the artifact exists:

   ```bash
   ARTIFACT=".git"                                    # path that must not appear
   for f in $(find src -name '*.test.ts' | sort); do
     [ -e "$ARTIFACT" ] && { echo "present before $f: clean up and restart"; break; }
     npm test -- "$f" >/dev/null 2>&1 || true
     [ -e "$ARTIFACT" ] && { echo "polluter: $f"; break; }
   done
   ```

   Adapt the file pattern and the runner (`pytest "$f"`, `cargo test --test`, `go test`)
   and note the adaptation in the ledger.

Exit gate: you can say what is happening and why, with the trace written down.

### Phase 2: Compare with what works

1. Find similar code in the same codebase that works.
2. If you are following a pattern or reference implementation, read it completely. Every
   line. Do not adapt from a skim.
3. List every difference between working and broken, however small. Do not rule one out
   because "that cannot matter".
4. List what the broken code depends on: other components, settings, environment,
   assumptions.

Exit gate: a written list of differences.

### Phase 3: One hypothesis, one test

1. Write one hypothesis: "X is the root cause because Y." Specific, falsifiable.
2. Test it with the smallest possible change. One variable.
3. Confirmed: go to Phase 4. Refuted: revert the change, record it, form a new hypothesis
   from what you learned. Do not add another change on top.
4. If you do not understand something, say "I do not understand X", then research or ask.

Exit gate: one hypothesis confirmed by one minimal test.

### Phase 4: Fix

1. **Write the failing test first.** The simplest reproduction. Automated if a framework
   exists, a one-off script if not. For how to author it well, use
   `tdd-progress-and-resume`.
2. **Make one fix at the root cause.** No "while I am here" improvements. No bundled
   refactoring.
3. **Verify with loop D.** The test passes, nothing else broke, the original symptom is
   gone.
4. **If the fix fails**: stop, revert it, add one to the failed-fix count in the ledger,
   and return to Phase 1 with the new information.
5. **At three failed fixes, stop.** Do not attempt a fourth. Signs that the design is the
   problem: each fix exposes new shared state or coupling somewhere else; a fix would
   need a large refactor; each fix creates a new symptom elsewhere. Take the question
   "is this pattern sound, or are we continuing out of inertia?" to your human partner
   before any further change. This is not a failed hypothesis. It is a wrong
   architecture. The number three is a working rule, not a measured optimum.
6. **Harden after the root fix** when the bug was caused by bad data crossing layers. Add
   a check at each layer the value passes through, then test each layer by bypassing the
   one before it:
   - Entry point: reject invalid input at the API boundary (empty, missing, wrong type).
   - Business logic: check the value makes sense for this operation.
   - Environment guard: refuse dangerous operations in the wrong context (for example,
     in tests, refuse to initialise a repository outside the temp directory).
   - Debug instrumentation: log context and a stack before the risky operation.

   One check can be bypassed by another code path, a refactor or a mock. A fix at the
   source without the layers is correct but incomplete.

### When the source cannot be reached or no cause is found

- The source is in third-party code you cannot change: trace as far as you can, guard the
  boundary, and document what remains. A fix at the symptom site is acceptable only at
  this dead end, never as the first move.
- Investigation shows the issue is environmental, timing-dependent or external: you
  have completed the process. Document what you checked, add fitting handling (retry,
  timeout, error message), and add monitoring for the next occurrence. Reach this
  conclusion only after the full process. Most "no root cause" endings are unfinished
  investigations.

### Flaky tests: wait for the condition, not for time

A test that sleeps for a guessed duration passes on a fast machine and fails under load.
Wait for the thing you care about.

```python
import time

def wait_for(condition, description, timeout_s=5.0, interval_s=0.01):
    deadline = time.monotonic() + timeout_s
    while True:
        value = condition()              # read fresh state on every pass
        if value:
            return value
        if time.monotonic() > deadline:
            raise TimeoutError(f"timed out after {timeout_s}s waiting for {description}")
        time.sleep(interval_s)
```

```ts
export async function waitFor<T>(read: () => T | null | undefined | false, what: string, timeoutMs = 5000): Promise<T> {
  const deadline = Date.now() + timeoutMs;
  for (;;) {
    const value = read();                // read fresh state on every pass
    if (value) return value;
    if (Date.now() > deadline) throw new Error(`timed out after ${timeoutMs}ms waiting for ${what}`);
    await new Promise((r) => setTimeout(r, 10));
  }
}
// await waitFor(() => events.find((e) => e.type === 'DONE'), 'DONE event');
// await waitFor(() => machine.state === 'ready', 'machine ready');
// await waitFor(() => items.length >= 5, 'five items');
// await waitFor(() => events.find((e) => e.type === 'TOOL_RESULT' && e.data.id === 'call_123'), 'TOOL_RESULT call_123');
// await waitFor(() => fs.existsSync(path), `file ${path}`);
// await waitFor(() => ready && value > 10, 'ready and value above 10');
```

Typical conversion: a test that sends a message, sleeps 300 ms hoping the tools have
started, aborts, sleeps 50 ms hoping results arrived, and then asserts on a count. Replace
the first sleep with a wait for the two "tool started" events and the second with a wait
for the two results.

- Poll about every 10 ms. Polling every 1 ms wastes CPU.
- Always have a timeout with a message that names what was awaited.
- Read state inside the loop. A value cached before the loop never changes.
- A fixed delay is correct only when the test is about timing itself (debounce, throttle,
  tick intervals). Then all three must hold: wait for the triggering condition first;
  base the delay on known timing; write a comment saying why. Example: wait for the
  "started" event, then 200 ms because the tool ticks every 100 ms and two ticks are
  needed. A commented sleep with no condition before it meets only the third rule.
- Running a flaky suite in parallel can make the races worse. Fix the waits first.

### Signals to stop and return to Phase 1

Your own thoughts: "quick fix for now, investigate later"; "just try changing X"; "make
several changes and run the tests"; "skip the test, I will check by hand"; "it is
probably X"; "I do not fully understand it but this might work"; "the pattern says X but
I will adapt it"; listing fixes before tracing the data; "one more fix" after two have
failed; every fix revealing a new problem somewhere else.

Your partner's words: "is that not happening?" (you assumed without checking); "will it
show us?" (you should have added evidence gathering); "stop guessing"; "think harder
about this" (question fundamentals); "we're stuck?" (the approach is not working).

Structural signs: fixing where the error appears; bundling changes; skipping the failing
test; stacking a fix on a failed fix.

### Under pressure

Three situations make the shortcut look reasonable. In each, the "compromise" (a
five-minute look, then the shortcut) is still the shortcut.

- **Outage and money.** A remembered retry looks like a two-minute fix. Do not ship it.
  Instrument the boundaries, say out loud what evidence you have and which layer fails,
  and use reversible containment (drain traffic, roll back the last deploy) if it is
  authorized. Containment is not the fix.
- **Sunk cost and fatigue.** Hours of longer and longer sleeps. Delete them and return to
  Phase 1. A longer sleep with a TODO is a symptom patch.
- **Authority.** A senior engineer is sure of the fix and the room wants to move on. Ask
  the Phase 1 question aloud ("why is the middleware invalidating the token?") and ask
  for the time to answer it. Experience is a source of hypotheses, not of evidence.
## Templates

### Review request packet

```text
REVIEW REQUEST
what_was_implemented:      <one paragraph: what and why>
requirement_or_plan:       <link or text of the accepted requirement, plan item, invariant>
base_sha:                  <sha>
head_sha:                  <sha>
uncommitted_or_generated:  <files outside the range that matter, or "none">
checks_run_and_results:    <command -> result, with counts and skips>
environments_in_scope:     <platforms, versions, data, compatibility targets>
not_tested_and_assumed:    <gaps, assumptions, external or generated dependencies, exclusions>
fallback_or_rollback:      <how to undo>
verdict_requested:         <exploratory | blocking | specialist: which>
sensitive_data:            none included
```

### Reviewer brief (for a subagent or a person)

```text
You are reviewing a code change. You are read-only: produce findings, do not edit.

What was implemented:   {WHAT_WAS_IMPLEMENTED}
Requirement or plan:    {REQUIREMENT_OR_PLAN}
Range:                  {BASE_SHA}..{HEAD_SHA}
    git diff --stat {BASE_SHA}..{HEAD_SHA}
    git diff {BASE_SHA}..{HEAD_SHA}
Not tested / assumed:   {GAPS}
Verdict wanted:         {VERDICT_REQUESTED}

Check: requirements met and no scope creep; correctness, error handling, edge cases;
design, performance, security; tests exercise real logic and cover negative cases;
migration, compatibility, documentation, rollback.

Return exactly:
  Strengths      - specific, each with file:line evidence; omit if none
  Findings       - grouped Critical / Important / Minor; for each:
                   file:line | what is wrong | why it matters and when | evidence | fix direction
  Not inspected  - files, environments or cases you did not cover
  Recommendation - ready | ready with named fixes or limits | not ready, with 1-2 sentences of reasoning
Rules: severity follows consequence; no comment on code you did not read; no vague
findings; say so when you could not verify something.
```

Check that all six placeholders are filled before sending.

### Feedback ledger (one row per atomic claim)

```text
id | source and location | claim restated | evidence checked | consequence if true | disposition | owner | action or non-action | finding-specific proof | integrated proof | reopens when
F1 | reviewer A, api/charge.ts:88 | two concurrent deliveries can both pass the guard | reproduced with synchronized fake-charge fixture: 2 calls | duplicate external charge | accept (defect) | payments owner | remedy open: see F2 | old: 2 calls, new: 1 call | suite + migration up/down | storage contract changes
F2 | reviewer A, same thread | use a global cache as the remedy | eviction and durability do not meet the contract | n/a | reject remedy, route alternative | storage owner | atomic durable operation record proposed | - | - | owner approves cache with durable semantics
F3 | reviewer B, handler.ts:12 | rename handler | internal, consistent, no convention violated | none | no change | - | none | - | - | name becomes public or a convention is enforced
```

### Completion report

```text
claim:                            <exact, checkable statement>
candidate_and_scope:              <branch, head sha, dirty files, environment>
fresh_evidence:                   <command or inspection, run when>
observed_result:                  <exit code, counts, key output lines>
failures_skips_and_unrun_gates:   <each with reason>
what_the_evidence_does_not_prove: <platforms, cases, requirements not exercised>
owner_or_policy_boundary:         <who decides merge, release, risk>
allowed_next_action:              <the one step this evidence authorizes>
```

### Debugging ledger

```text
DEBUG LEDGER  <symptom in one line>  opened <time>
symptom:            <exact error text, where, how often>
reproduction:       <steps or command; reliable? yes/no>
recent_changes:     <commits, deps, config, environment differences>
boundary_evidence:  <probe output per boundary; which layer breaks>
trace_chain:        symptom <- immediate cause <- caller <- ... <- original trigger
working_vs_broken:  <differences found>
hypotheses:
  H1: <X is the root cause because Y> | minimal test: <...> | result: confirmed / refuted
  H2: ...
failed_fix_count:   <0-3; at 3 stop and take the architecture question to the human partner>
failing_test:       <path or script; seen red: yes/no>
fix:                <one change, where>
verification:       <test green, suite result, symptom gone>
disposition:        root cause fixed | symptom guarded at boundary (source unreachable) | environmental (handled and monitored)
hardening_layers:   entry / business / environment / instrumentation: <added or why not>
residual_monitoring:<what to watch>
```

Scale the form down for a one-line typo, but keep the order of the gates.

### Stop and handoff block

Use it when intent, range, authority, safety or a rollback path is unresolved.

```text
outcome_sought:
current_mode_and_range_or_candidate:
finding_claim_or_hypothesis:
completed_evidence:
first_unmet_gate:
current_safe_behavior:
owner_question:
changed_paths_or_artifacts:
unresolved_risk:
fallback_and_recovery:
resume_action:
```
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
