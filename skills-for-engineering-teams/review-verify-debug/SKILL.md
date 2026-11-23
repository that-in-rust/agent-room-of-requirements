---
name: review-verify-debug
description: >-
  Runs the evidence loops around a code change: asking for and giving code review (frozen
  base..head range, findings with file:line and consequence, bounded verdict), handling
  review feedback (every comment gets one of eight dispositions backed by evidence from
  this codebase), verifying before any "done", "fixed", "passes" or "ready" claim (fresh
  full command, complete output read, red-green proof, requirement-by-requirement check),
  and debugging from symptom to root cause in four gated phases (investigate, compare, one
  hypothesis, failing test then one fix; stop after three failed fixes). Use when the user
  says "review this diff", "request a review", "address the PR comments", "the reviewer
  says", "is it done", "verify the fix", "are the tests passing", "ready to merge", "why is
  this failing", "it worked yesterday", "flaky test", "stop guessing"; before a commit,
  push, pull request or handoff; when a test, build or CI job fails; when a subagent
  reports success; when a test waits with sleep or setTimeout. Not for writing the
  requirements or the test matrix (executable-specs), running the TDD cycle or keeping a
  progress journal (tdd-progress-and-resume), commit, branch and pull request mechanics
  (git-delivery-flow), choosing an architecture or product direction, or finding where
  code lives in a large repository (codebase-navigation).
---

# Review, Verify, Debug

A statement about code is a claim: "this is wrong", "this is done", "this is the cause".
This skill is the procedure for testing such claims against the current code before
anyone acts on them, in three settings: code review (asking, giving, receiving),
completion claims, and debugging.

Three rules hold in every setting and have no exceptions for small or urgent work:

1. **No fix without root-cause investigation first.**
2. **No completion claim without fresh verification evidence.**
3. **No review comment acted on, accepted or rejected, before it is checked against this
   codebase.**

Depth and tables are in [reference.md](reference.md). The entry documents are
[A00](../../A00-LLM-Principles01.md) (verify every result and close the loop) and
[A01](../../A01-LLM-Workflow01.md) (the bug flow: reproduce, diagnose, test, fix,
verify).

## When to Use

Use it when:

- You are about to ask a person or a subagent to review a change, or you were asked to
  review one.
- Review comments arrived: pull request threads, inline comments, a pasted list, a
  subagent's review report.
- You are about to write "done", "fixed", "works", "passes", "ready", or anything a reader
  would take as success. Also before `git commit`, `git push`, opening a pull request,
  moving to the next task, or handing off.
- A subagent or another worker reported success and you are about to pass that on.
- A test, build, CI job or production path fails, gives a wrong result silently, is slow
  without explanation, or behaves differently from yesterday.
- A fix did not work and you are about to try another one.
- A test waits with `sleep`, `setTimeout`, `time.sleep()` or `Thread.sleep`.

Requests that should trigger it:

- "Can you review the diff between main and this branch before I merge?"
- "The reviewer left six comments on the PR. Address them."
- "CI is red on the integration job and I changed nothing. Why?"
- "The subagent says the migration is complete. Is it?"
- "This test passes locally and fails one run in five. Fix it."

Requests that should not:

- "Write acceptance criteria for the export feature." That is a specification task
  (`executable-specs`).
- "Squash these commits and open the pull request." That is delivery mechanics
  (`git-delivery-flow`). This skill only supplies the verification before it.
- "Should we use a queue or a cron job here?" That is a design decision. Come back here
  when a concrete change or failure exists.

## Pick the Loop

| You are about to | Loop | First action | It ends with |
|---|---|---|---|
| Ask for a review | A. Request review | Capture base and head, list what was not tested | A request packet |
| Review someone's change | B. Review a change | Confirm range and requirements; stay read-only | Findings and a bounded recommendation |
| Respond to comments | C. Handle feedback | Read every comment before touching code | A ledger with one disposition per comment |
| Claim a state, commit, push, hand off | D. Verify | Name the exact claim and the check that could refute it | A completion report with evidence and limits |
| Fix something that fails | E. Debug | Read the whole error and reproduce it | Root cause, failing test, one fix, verified |

The loops chain. Debugging ends in D. A fix for a review comment ends in D. A review
comment that says "this is a bug" and cannot be confirmed by reading goes through E to
get a reproduction. A failed verification in D opens E. When the question is "why did it
break", use E. When the question is "is it done", use D.

## The Shared Workflow

Every loop is a special case of these steps.

1. **State the outcome and pick the mode.** Say what decision the work feeds. Choose the
   mode with the least authority that can deliver it (table under Rules). Read-only is
   the default.
2. **Freeze the object.** Record the requirement or plan, base and head revisions, dirty
   worktree state, generated files, dependencies, environment, and who else is writing.
   If any of these moves, earlier evidence about it is historical.
3. **Split into atomic claims.** One claim is one thing that can be true or false. "Done"
   splits into "tests pass", "requirement 3 is met", "the build succeeds". A review
   comment splits into "there is a defect", "this is the intended behaviour", "this is
   the right remedy".
4. **Choose evidence that could prove the claim wrong.** A check that cannot fail for the
   concern proves nothing. Decide in advance what pass, relevant fail, blocked and stop
   look like.
5. **Preflight safety.** Know what the command reads, writes, costs and contacts. Never
   run production, destructive, credentialed, migration or external-effect commands just
   to finish a review or a verification. Use a static, dry-run, mock or disposable
   substitute, or report the gate as blocked.
6. **Collect the evidence now and read all of it.** Exit code, failure count, skips,
   warnings, timeouts, cache hits. A timeout means the effect is unknown, not absent.
7. **Decide.** A disposition for a comment, a state for a claim, a verdict for a
   hypothesis. Record the strongest counter-example you looked for.
8. **Act on one coherent unit, only if the mode allows writes.** One finding or one
   shared-cause group, one hypothesis, one fix.
9. **Prove it twice.** First the check specific to the claim (old behaviour fails, new
   passes). Then the integrated checks (suite, build, static checks, generated files,
   final diff).
10. **Report in bounded words.** State what was observed, on which candidate, what was
    not checked, who must decide what remains, and which change would make the report
    stale.

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

## A. Requesting Review

**When.** After each task in subagent-driven work. After a major feature. Before merging
to the main branch. Also useful when stuck, before a refactor (to get a baseline), and
after a complex bug fix. Do not skip review because the change looks simple. Review
cadence also has to respect reviewer capacity: when reviews queue faster than they can be
read, make the diffs smaller or batch by coherent unit rather than dropping the review.

**Steps.**

1. Finish loop D for the claims you make in the request. Do not send unverified "tests
   pass".
2. Capture the range.

   ```bash
   BASE_SHA=$(git merge-base origin/main HEAD)   # or the commit before the task began
   HEAD_SHA=$(git rev-parse HEAD)
   git status --porcelain                        # empty, or list the uncommitted files in the request
   git diff --stat "$BASE_SHA".."$HEAD_SHA"
   ```

3. Fill the request packet (Templates). It must state: what was implemented and why; the
   accepted requirement, plan or invariant; exact base and head; tests, fixtures and
   commands with results; platforms, versions, data and compatibility in scope; gaps,
   assumptions, generated or external dependencies and exclusions; the verdict you want
   (exploratory, blocking, specialist).
4. Keep the diff small and coherent. Split a broad diff into staged reviews or along
   ownership boundaries. File count is not the measure: a one-line credential change can
   need a specialist, and a large mechanical rename can be checked by a script.
5. Send it to the reviewer. For a subagent reviewer, pass the packet and the reviewer
   brief (Templates) and require the report format. Check that every placeholder in the
   brief is filled before dispatch; an unfilled or misnamed placeholder is a broken
   request.
6. When the report returns, run loop C on it. Severity labels set the default handling:
   Critical is fixed before anything else, Important before proceeding to the next task,
   Minor is recorded for later. A label is still a claim: confirm the consequence first,
   and push back with code or tests when the reviewer is wrong.

## B. Reviewing a Change

You are read-only. You produce findings and a recommendation, not edits.

1. Confirm the range and the requirement you are reviewing against. If either is
   missing, ask or state the assumption at the top of the report.
2. Read the diff, then the surrounding source, tests, config, generated outputs and
   history in proportion to consequence. Do not comment on code you did not read.
3. Check five families:
   - **Requirements**: every plan item met, behaviour matches the spec, no scope creep,
     breaking changes documented.
   - **Correctness and quality**: error handling, edge cases, type safety, separation of
     concerns, duplication.
   - **Architecture**: design soundness, performance and scalability implications,
     security.
   - **Tests**: they exercise real logic and not only mocks, cover edge and negative
     cases, include integration where needed, and currently pass.
   - **Readiness**: migration strategy for schema changes, backward compatibility,
     documentation, rollback.
4. Write each finding as an atomic claim: location (`file:line`), what is wrong (the
   mechanism), why it matters (the consequence and under which conditions), evidence, and
   a fix direction when it is not obvious. When the cause cuts across files, name the
   root cause once and list the locations.
5. Set severity from consequence: reach, effect, likelihood or exploitability, how it
   would be detected, how it would be recovered. Critical: bugs, security problems, data
   loss, broken functionality. Important: architecture problems, missing required
   behaviour, poor error handling, test gaps. Minor: style, small optimizations,
   documentation polish. Not everything is Critical. A style nit never blocks while a
   harm waits.
6. List strengths only when they are specific and carry evidence ("migration is
   reversible, `db/0042_down.sql` tested in `test_migrations.py:88`"). Generic praise is
   filler.
7. Order findings by consequence, but put a shared cause or a dependency before the
   findings that hang on it.
8. Give a clear recommendation: `ready`, `ready with named fixes or limits`, or
   `not ready`, with one or two sentences of technical reasoning, the scope you did not
   inspect, and the owner decisions that remain. The merge decision belongs to the owner.

Reviewer rules: do not write "looks good" without checking. Do not be vague ("improve
error handling"). Do not withhold a verdict. Mark exploratory design questions as
non-blocking. A deterministic finding that will recur belongs in a linter, schema or
test, not in the next reviewer's memory.

## C. Handling Review Feedback

Stance: skeptical cooperation. Investigate every comment. Do not implement because the
label is severe, the reviewer is senior or the suggestion sounds professional. Do not
defend existing code because changing it is inconvenient or because you wrote it.

The question for each comment: what behaviour, requirement, invariant or risk is alleged;
does it hold in this codebase and its supported environments; which owner decides the
remedy; what evidence would show the disposition is right without a regression.

**Steps.**

1. **Read all of it** before reacting or editing. Confirm the range has not moved since
   the review:

   ```bash
   git diff --quiet "$REVIEWED_HEAD" HEAD && echo "same candidate" || echo "range moved: re-evaluate comments"
   ```

2. **Split** each comment into atomic claims and restate each in your own words.
3. **Clarify coupled ambiguity first.** If any item is unclear, and it could change how
   another item is done, implement none of the coupled set. Say which items you
   understand and which need an answer. Example: asked to fix items 1 to 6, you understand
   1, 2, 3 and 6. Reply "I understand 1, 2, 3 and 6. I need clarification on 4 and 5
   before I start", and wait.
4. **Verify each claim** against source, tests, history and supported environments. For
   feedback from outside the team ask five things: is it technically correct here; does
   it break existing behaviour; is there a reason for the current implementation; does it
   work on every supported platform and version; does the reviewer have the full context.
   If you cannot verify, say so: "I cannot verify this without X. Should I investigate,
   ask, or proceed?"
5. **Check for use before building more.** When a comment asks to implement something
   "properly", search for callers first (direct, generated, dynamic, external, roadmap).

   ```bash
   git grep -n "exportMetrics" -- ':!*.md'      # or: rg -n "exportMetrics"
   ```

   If nothing uses it, propose removal instead of adding persistence, filters and
   exports. An accepted public contract or a real consumer flips the answer.
6. **Give every comment one disposition** (table below) and report the dispositions
   before editing.
7. **Implement** accepted items one coherent unit at a time. Default order after
   clarification: blocking items (breakage, security), then simple fixes (typos,
   imports), then complex ones (logic, refactors). A shared root cause or a dependency
   goes before the items it covers, whatever their labels.
8. **Test each fix** on its own (old behaviour fails, new passes), then run the
   integrated checks, then reread the final diff and the list of unresolved items.
9. **Reply** where the comment was made, with what changed and where, or with the
   counter-evidence.

**Dispositions.**

| Disposition | Use when | Record and do |
|---|---|---|
| Accept | Real defect or unmet requirement, and the direction fits scope | Finding, evidence, affected behaviour, fix, verifier. Smallest coherent correction plus a test |
| Clarify | Behaviour, case, scope or term is ambiguous | The exact question, the readings, why they change the implementation. Pause coupled work |
| Reject with evidence | False, already handled, incompatible, wrong scope, or would regress | Current evidence, a counter-example, residual risk, and the case that would reopen it |
| Defer explicitly | Valid but non-blocking, out of scope, needs separate design, or a planned larger change will remove the code soon (a confusing name on a symbol about to be refactored away: defer under that dependency, do not create two migrations) | Owner, consequence, tracking item, dependency, condition for reconsidering. Keep it out of this diff |
| Route | Product, security, data, architecture, compatibility, production or policy authority is elsewhere | One atomic owner question, safe current behaviour, evidence so far, the action that is blocked |
| Contain | An active severe effect needs reducing now | Trigger, scope, fallback, owner, time limit. Stop propagation, keep evidence |
| Supersede or duplicate | A root fix covers the same mechanism | The dependency and a check that every path closes |
| No change | Current behaviour meets the contract, or churn costs more than it gives | Requirement trace, representative verification, counter-example, reopening event |

Never mark a comment `resolved` on thread closure, a changed line or literal compliance
with the wording. The failure can remain on another path.

**Plausible but unproven.** When a claim is plausible and the behaviour evidence is
incomplete, neither accept nor reject yet. Investigate inside a safe, bounded scope. If
the hard gates pass and the change can be reversed on its own, a limited canary under the
owners is the other option. Either way record the hypothesis, the missing case, the stop
rule and the state that holds if the change is not adopted. A canary declares its cohort,
guardrails, stop rule, rollback and expansion rule before it starts. Example: a cache
improves a local benchmark, but production workload, memory pressure and invalidation
cost are unknown. Keep the claim bounded, or canary it; do not call it resolved.

**A rejection has an expiry.** "Reject with evidence" rests on a premise. Example: a
comment asks for a null check, and the type boundary plus a property test show the empty
input cannot reach the function under supported construction. Reject with that evidence
instead of adding a generic check that would hide a caller defect. If a deserializer
makes the boundary unclear, investigate first. If a new public constructor later permits
the empty input, the rejection has expired and the boundary must be checked again.

**Who the feedback is from.**

- From the person you work for: their intent is trusted within their authority. Act after
  you understand it, ask when scope is unclear, and still verify the implementation.
- From an external reviewer or a reviewing agent: a suggestion to evaluate. If it
  conflicts with a decision your human partner already made, stop and discuss with them
  first.
- Both you and the reviewer answer to the owner. If the owner does not need the feature,
  do not add it.

**Push back when** the suggestion breaks existing behaviour, the reviewer lacks context,
the feature is unused, it is technically wrong for this stack, legacy or compatibility
reasons exist, or it conflicts with the owner's architectural decisions. Use technical
reasoning, specific questions and references to working code or tests. Involve the owner
when it is architectural. If open pushback is socially hard, agree a neutral signal
phrase with your human partner in advance and use it.

Example: the comment says "remove the legacy code path". Check the build target against
the API's minimum version first. If the oldest supported target still needs the path,
reply with that fact and ask whether to fix the path or drop the old target.

**Reply wording.**

- Correct feedback: "Fixed: <what changed> in <location>." Or just show the fix.
- Your pushback was wrong: "Checked <X>; it does <Y>. My reading was wrong because
  <reason>. Fixing." One or two sentences. No long apology, no defence.
- No performative agreement ("you're absolutely right", "great point") and no
  "implementing now" before verification. The upstream method this draws on also bans
  thanks of any kind; see Where the Sources Disagree.
- For inline GitHub comments, reply in the comment thread, not as a top-level comment:

  ```bash
  gh api -X POST "repos/$OWNER/$REPO/pulls/$PR/comments/$COMMENT_ID/replies" -f body="Fixed in $SHA: <what changed>"
  ```

  Check the endpoint against the current GitHub REST documentation before automating it.

**Stop mutating and hand off** when the range changes under you, a decisive generated or
external artifact has not been inspected, a severity label has no stated consequence,
another worker owns the surface, no owner can reverse the effect, or no meaningful check
exists. Use the stop block in Templates.

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

## Where the Sources Disagree

Both positions are kept. The selector says which applies.

| Topic | Position 1 | Position 2 | What selects |
|---|---|---|---|
| Order of fixing review findings | Blocking first, then simple, then complex | Dependency and shared cause first | Use severity order unless one finding's fix changes or removes another; then the cause goes first |
| Acting on severity labels | Fix Critical immediately, Important before proceeding | A label without a stated consequence is not actionable | Confirm the consequence, then apply the label's urgency. No consequence: ask or reclassify |
| Feedback from your human partner | Trusted; implement once understood | Intent is trusted within their authority; the implementation is still verified | Trust the *what*; verify the *how* and anything outside their domain |
| Freshness of evidence | The check must run in the same turn as the claim | No universal time limit; evidence expires on a consequential change | Default to same turn. Reuse an earlier run only when you can show nothing consequential changed since |
| "Run the full command" | Always the full command | The full command that is applicable and safe | Safe and permitted: full. Otherwise a substitute with a narrower claim, or blocked |
| Proof of delegated work | Check the version-control diff | The diff is one example; also artifacts, generated outputs, non-file effects, rerun | Diff suffices only when all effects are in tracked files |
| Rigor versus size | Debugging rigor never scales with severity | Record detail scales with consequence in review and verification | Phase order and gates never scale. The amount written does |
| Emergencies | No fix before investigation | Containment is allowed | Containment only if authorized, narrow, reversible, evidence-preserving and temporary; it is not a fix |
| Fix at the symptom site | Never | Acceptable at a traced dead end | Source reachable: fix there. Unreachable: guard the boundary and document |
| Fixed sleeps in tests | Forbidden | Allowed for timing behaviour | All three conditions: condition first, known timing, comment |
| Three failed fixes | Hard stop | The number is doctrine, not a measured optimum | Keep three unless the team has recorded data for another number; the direction (stop and question the design) is fixed |
| Retrying | Never repeat a failed fix | A bounded retry of a check is allowed | Fixes: never. Checks: only for a plausible transient on a safe, repeatable operation |
| Review cadence | Early and often: after every task, every batch of about three plan tasks, before merge | Cadence must respect reviewer capacity | Keep the checkpoints; when queues grow, shrink the diffs or batch coherent units |
| Thanks in replies | No gratitude of any kind | The rule's purpose is that a reply carries content | Follow the team's norm; whatever the norm, never let thanks replace the technical statement |
| "Strengths" in a review | Always acknowledge strengths | Strengths must be specific and evidenced | Include them when you have evidence; omit the section rather than fill it |
| Reviewer verdict | "Ready to merge: yes / no / with fixes" | A recommendation is not merge authority | The reviewer recommends; the merge or release owner decides |

## Bundled Scripts

None. The skill has no scripts or assets. The commands above are complete as written and
use only `git`, `grep`, `gh` and the repository's own test and build commands. The
polluter loop and the wait helpers in loop E are meant to be copied into the project and
adapted.

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
