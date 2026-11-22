# Review, Verify, Debug: Reference

Depth for [SKILL.md](SKILL.md). The rules are there. This file holds the reasoning behind
them, the ranked patterns, extended examples, the record formats for consequential work,
failure handling, operating guidance at scale, and the limits of the evidence.

## Idiomatic Thesis Synthesis Statement

Code review, completion reporting and debugging look like three activities. They are one:
each tests a claim about code against evidence before anyone acts on it. They differ only
in who made the claim and when.

| Setting | The claim | Who makes it | The tempting shortcut | The control |
|---|---|---|---|---|
| Review | "This is wrong" or "this is fine" | A reviewer, about a bounded change | Agree, comply and close the thread, or defend and dismiss | A disposition per atomic claim, backed by evidence from this codebase |
| Completion | "This is done" | You, or a worker reporting to you | Infer success from effort, an old run or a proxy | A fresh, claim-specific check that could have failed |
| Debugging | "This is the cause" | You, under pressure | Patch where the error shows | Trace to the origin, one hypothesis, a failing test, one fix |

**Review is an evidence-bearing change-control loop.** It is not agreement, not comment
volume and not a transfer of authority. A comment is a falsifiable technical claim about a
bounded change. Four questions inside it are independent and are answered separately: is
there a real defect; what is the intended behaviour and who has authority over it; which
remedy fits; what evidence supports the state now being claimed. A reviewer can be right
about the defect and wrong about the remedy. An owner can authorize a choice without making
its factual premise true. The right stance is skeptical cooperation: investigate every
comment, without implementing it because of its label and without defending the code
because changing it is inconvenient.

**A completion claim is a compound statement.** "Done" asserts at once that the intent was
understood, that the thing checked is the thing being reported, that the check fits the
claim, that the result was actually observed, that the check would have failed if the
claim were false, that the scope is what is stated, that the check was safe to run, that
someone with authority accepts what remains, that there is a way back, and that the
outcome has the value sought. Each of the ten needs its own support. A test can pass while
a requirement is missing. A bug can be fixed while release is blocked. Narrow wording that
follows the evidence is precision, not hedging: "the formatter is clean" can be checked,
"probably complete" cannot.

**Debugging is an evidence order.** The four phases are not ceremony. Each one produces
the input the next one needs: the investigation produces a trace, the comparison produces
a list of differences, the hypothesis test produces a confirmed mechanism, and only then
is there something to fix. Skipping ahead means fixing something that has not been
identified. A simple bug is not exempt; its investigation is merely short. The rigor of
the order does not scale with severity. The amount written does.

**Why the rules are worded absolutely.** "No fix without investigation" and "no claim
without fresh evidence" are stated without exceptions on purpose. Under pressure, a rule
with a feasibility clause ("investigate when practical") is read as permission. Three
structural defences back up the wording: a phase that must complete before the next
begins; an explicit branch for what to do when a fix fails; and a list of the exact
thoughts that precede a shortcut, so that the thought itself becomes the signal to stop.
The rules apply to paraphrases and implications as well as to the literal words.

**What the three share.**

- Evidence belongs to one claim. Intent, mechanism, behaviour, compatibility, authority
  and outcome each need their own kind.
- The object must be frozen. Evidence about a candidate that has since changed is
  history.
- A check that cannot fail for the concern proves nothing.
- Gates are conjunctive. One red gate is not offset by any number of green ones.
- Authority is separate from correctness. A technical pass is not a merge decision, and a
  merge decision does not make a premise true.
- The end state is a bounded statement: what was observed, on what, with which limits, and
  what would make it stale.

## Pattern Scoreboard Ranking Table

The order reflects consequence: which omission most often turns into a false statement or
an unsafe change, according to the method lineage and the owner's pattern references. It
is not usage data. No compliance or defect rates were measured, and the numeric scores
attached to patterns in earlier material were uncalibrated and are not repeated here.

| Rank | Pattern | What it blocks | Loop | Minimum evidence that it was followed |
|---|---|---|---|---|
| 1 | Root cause before any fix | Symptom patches, masked bugs, new bugs from guesses | E | A written trace from symptom to original trigger, dated before the fix |
| 2 | Fresh claim-specific evidence before a status claim | False "done", stale passes, proxy gates | D | Command, candidate, exit code and counts from after the last change |
| 3 | Check the comment against the codebase before acting | Blind implementation, defensive rejection | C | Evidence line in the ledger for each claim |
| 4 | Freeze the object (requirement, base, head, worktree) | Moving-target review, wrong-candidate verification | A to E | Recorded SHAs and a check that they did not move |
| 5 | Split into atomic claims | Claim bundling, partial fixes hidden in "addressed" | C, D | One row per claim |
| 6 | Read everything, clarify coupled ambiguity before any edit | Partial implementation built on a wrong reading | C | The clarification question and the paused set |
| 7 | Phase gates as evidence order | Fixing an unidentified cause | E | Exit artifact per phase |
| 8 | Backward tracing to the original trigger | Fixing at the symptom site | E | The chain with each caller and passed value |
| 9 | One hypothesis, one minimal test | Shotgun fixes, unattributable results | E | Hypothesis sentence and single-variable change |
| 10 | Failing test first; red-green proof | Tests that cannot fail, unproven regressions | D, E | Observed red on old behaviour, green on new |
| 11 | Stop after three failed fixes | Thrashing against a wrong architecture | E | Failed-fix count and the escalation note |
| 12 | One disposition per comment, with owner and reopening event | Thread-only closure, unowned deferral | C | Ledger completeness |
| 13 | Defect, remedy and authority decided separately | Remedy conflation, authority substitution | B, C | Separate rows or fields |
| 14 | Requirement-by-requirement map | Requirements-by-tests | D | Clause table with evidence or unresolved |
| 15 | Independent validation of delegated work | Agent-report trust | D | Inspected diff and rerun output |
| 16 | Hard gates are conjunctive, reported by state | Averaging a red away, percentage theatre | A to E | State per gate with reason |
| 17 | Mode as a permission envelope | Review-only work that edits, intake that decides product | A to E | Mode named in the output |
| 18 | Safety preflight; never production to finish a check | Destructive or credentialed verification | A to E | Preflight answers; blocked state when unsafe |
| 19 | Boundary instrumentation in multi-component systems | Investigating the wrong layer | E | Probe output per boundary |
| 20 | Wait on the condition, not on time | Flaky tests, guessed sleeps | E | Poll with timeout; no bare sleep |
| 21 | Defense in depth after a data bug | Recurrence through another path | E | A check at each layer plus a bypass test |
| 22 | Evidence-bearing review request | Context-free review, review theatre | A | Filled packet |
| 23 | Severity from consequence | Severity laundering, nit-blocking | B, C | Reach, effect, likelihood, detection, recovery stated |
| 24 | Bounded wording and bounded recommendation | Readiness inflation | A to E | Limits and unrun gates in the report |
| 25 | Promote repeated findings into automation | The same comment every review | B, C | New linter rule, schema or test with an owner |

How to use the ranking: when time is short, the top of the table is what may not be cut.
Nothing below rank 3 justifies skipping something above it. The lower rows are where
record depth can shrink for small local changes.

A scoreboard for review or verification quality must not reward comment count, severity
inflation, number of approvals, number of green checks, speed of thread closure or volume
of output. Those can all rise while quality falls.

### Evidence profile after the hard gates

Judging a finding or a completion claim has two stages. Stage one is the hard gates. They
are conjunctive: one red blocks the state, and passes are not averaged against it. Stage
two starts only when every hard gate passes. Rate each dimension that applies as `strong`,
`mixed`, `weak` or `not applicable`, and give a short evidence reason for the label. Do
not convert the labels into a total score.

The profile is for locating disagreement, not for automating the verdict. One reviewer
may dispute the reproduction. Another may accept the defect and prefer a different
architecture. One may doubt that the test is sensitive. Another may accept the test and
dispute the scope of the requirement. A single number would hide which repair is needed.

Review dimensions:

| Dimension | Strong | Mixed | Weak | The label decides |
|---|---|---|---|---|
| Reviewability | Coherent bounded diff, explicit requirements, known environment, reproducible commands | Some cross-cutting or generated effects need extra reconstruction | Moving target, broad unrelated changes, or no stated expected behaviour | Proceed, stage the review, or return the change for preparation |
| Finding validity | Mechanism reproduced or traced directly, and a relevant counter-example checked | Plausible from source, but behaviour or compatibility only partly tested | Rests on style preference, analogy or incomplete context | Accept, investigate, reject or route |
| Consequence | Affected users, data, behaviour, reach and recovery established | Impact plausible, frequency or blast radius uncertain | Severity taken from tone or category with no failure evidence | Order of containment and resolution effort |
| Requirement alignment | The remedy satisfies accepted intent without widening scope | Intent incomplete, or several valid designs remain | Adds an unrequested capability or conflicts with an owner decision | Select the remedy, clarify, or defer |
| Regression coverage | Positive, negative, boundary and integrated evidence tell old from new behaviour | The direct test passes; platform, migration or cross-module tails remain | Code changed with no test able to fail for the original defect | Close, canary, narrow, or keep unresolved |
| Evidence boundary | Facts, reviewer hypotheses, external support, compatibility and owner decisions are kept apart | Some inference is visible, source or scope is coarse | Citations or labels imply authority they do not carry | How much confidence to state; what must not be passed on as fact |
| Remediation fit | A small coherent change addresses the cause and keeps architecture and supported behaviour | The fix works; lifecycle or an alternative design is still disputed | The literal comment is satisfied while the root cause or another path remains | Implement, redesign, supersede or reject |
| Lifecycle and recovery | Owner, fallback, invalidation, rollback and tracking of unresolved items are active | Recovery exists; long-term maintenance or ownership uncertain | Orphaned exception, temporary workaround with no expiry, no way back | Retain, defer, route, or do not adopt |

Completion dimensions:

| Dimension | Strong | Mixed | Weak | The label decides |
|---|---|---|---|---|
| Claim alignment | The gate observes the exact proposition and requirement | It covers most clauses; one reading or owner question remains | A convenient check only loosely related to the statement | Whether the result can support the wording |
| Failure sensitivity | A known defective or safely mutated condition turns red for the expected reason | Source reasoning supports sensitivity; direct mutation is unavailable | The gate has never been shown to reject the target failure | Regression evidence or ceremony |
| Freshness | Candidate and all material inputs fingerprinted after the final change | One low-impact environment or generated input is inferred stable | The result predates edits, or the candidate identity is unknown | Retain, narrow or invalidate the evidence |
| Requirement coverage | Every declared clause has direct evidence or an explicit owner resolution | Some clauses rest on review judgement or on bounded unrun conditions | A general green suite stands in for traceability | Claim "requirements met" or expose the gaps |
| Result completeness | Full output, exit code, failures, skips, warnings, timeout and cleanup reconciled | The tool hides some internals; the relevant result can be checked independently | Only the summary line or a favourable excerpt is kept | Trust the execution evidence or rerun |
| Reproducibility | A fresh reviewer can run or inspect the evidence from saved context | The environment is specialized; an owner can reproduce it | The result depends on private memory or state that is gone | Whether a handoff and later invalidation are possible |
| Non-interference | Representative unrelated paths stay valid; no hidden artifact changes | The direct behaviour passes; the wider tail is explicitly unobserved | The fix proves one case and leaves an unknown regression surface | The bound on a "bug fixed" or readiness claim |
| Safety and privacy | Least-risk evaluator, minimized data, approved effects, cleanup verified | A safe substitute narrows what was observed directly | The evidence exposes data or causes uncontrolled effects | Permit use, or invoke containment |
| Recovery | Independent fallback and residual-state checks pass | Rollback exists; part of the operational tail needs owner assurance | Recovery is prose only, or shares the failed dependency | Whether consequential readiness can be supported |
| Lifecycle cost | The gate has an owner, maintenance, false-blocking review, fallback and a retirement path | Value is clear; the long-term burden is uncertain | A shared gate with no owner or removal condition | Adopt, narrow, improve or retire the control |

Profiles in use:

- Good acceptance: a boundary input causes a reproducible panic, the requirement says a
  typed error is returned, and the patch adds a narrow guard plus a regression test that
  fails on the old revision. Scope, owner and integrated tests pass. Accepted with no
  score.
- Bad readiness (review): the report covers quality, architecture, testing and production
  categories, but it reviewed a range from before a rebase and never inspected generated
  output. Review identity is red. Category coverage cannot support merge readiness.
- Borderline compatibility: a newer API would simplify the code, and the supported
  platform matrix includes an older release. Finding validity is strong. Remedy
  compatibility is red. Keep the branch or route a support-policy decision.
- Bad readiness (completion): formatter, linter and compiler pass, but the requirement is
  about runtime retry behaviour and its integration test never ran. Claim alignment is
  red. Three green commands do not support readiness.
- Stale evidence: the full suite passed, then a generated input and the implementation
  changed. Freshness is red even when the same suite is expected to pass. Rerun.
- Good blocked state: a rollback check needs an approved disposable database that is not
  available. Keep the other passes, report the recovery gate as blocked, and do not claim
  release readiness.

Checking the profile itself: freeze the claim, candidates, requirements and evaluators;
present cases that are known valid, known invalid, stale, partial, unsafe, delegated and
missing a requirement; confirm that a hard red always prevents the broad statement. Ask
independent reviewers to record the state they would allow. A disagreement should trace
to claim, candidate, requirement, sensitivity, scope, safety or authority. Agreement is
not correctness when every reviewer relies on the same proxy. Retire a profile dimension
or a manual check once a stable deterministic control has made it ordinary
infrastructure.

## Agent Usage Decision Guide

### Which loop

```text
Is something failing, wrong or slow, and the cause is not established?
  yes -> E (debug). Do not propose a fix yet.
  no  -> Did someone make statements about a change that you must respond to?
           yes -> C (handle feedback).
           no  -> Are you about to state a status, commit, push, hand off or accept a worker's report?
                    yes -> D (verify).
                    no  -> Are you asked to judge a change?
                             yes -> B (review, read-only).
                             no  -> Do you want a judgement on your change?
                                      yes -> D for your own claims, then A (request).
                                      no  -> this skill does not apply.
```

### Which mode

| Request wording | Mode | Stop condition |
|---|---|---|
| "What does this comment mean?", "why is this gate red?" | Explain | The explanation is given; no state changed |
| "Get this ready for review" | Prepare request | Packet complete; no behaviour change |
| "Review this" | Review change | Findings and recommendation returned; no edits |
| "Here are the comments" with no instruction to fix | Intake feedback | Every claim has a disposition; nothing implemented |
| "Address the comments", "fix what the review found" | Authorized remediation | Only accepted items inside the approved scope are changed |
| "Check again after my changes" | Re-review | Fresh check of the current candidate; old approval not reused |
| "Is finding 3 really closed?" | Verify resolution | Proof for that finding; only tests and probes written |
| "This needs the security team" | Defer or route | Owner question sent; safe current behaviour stated |
| "I do not think that comment is right" | Reject or no change | Counter-evidence and reopening event recorded |
| "It is hurting users now" | Contain | Authorized, narrow, reversible action; investigation continues |
| "We keep getting this comment" | Improve system | New control with scope, owner, evaluator and retirement condition |

When wording is ambiguous between intake and remediation, take intake. It is read-only
and loses nothing.

### How much record

| Situation | Record depth |
|---|---|
| One-line fix, one reviewer, local effect, reversible | The disposition and the check in the reply; a three-line debug note |
| Several comments, one repository, tests exist | Feedback ledger; completion report |
| Cross-team, generated artifacts, public contract, migration | Resolution record or completion warrant (see Theme Specific Artifact) |
| Security, data loss, money, production | Full record, specialist route, owner decision before any write |

The gate order is the same in every row. Only the amount written changes.

### Reading a request for authority

- "Fix" grants edits inside the reported failure. It does not grant refactors,
  dependency changes, schema changes or a change of public behaviour.
- "Review" grants reading and reporting only.
- "Make CI green" grants fixing the cause. It never grants disabling, skipping or
  weakening the check. If the check itself is wrong, that is a finding to route.
- "Ship it" from someone without release authority is an opinion.
- Silence is not approval. An approval covers the diff it was given for.

### Good, bad and borderline agent behaviour

Completion claims:

- Good, direct: "`npm test` exited 0 on `a1b2c3d` with 212 passed, 0 failed, 3 skipped
  (the three Windows-only path tests). The build was not run."
- Bad: "All done! Everything should be working now."
- Borderline: "The focused tests for the parser pass." True, but it omits that the
  integration suite was not run when the change touched the database layer. Add the
  unrun scope and it becomes good.
- Delegated: "The worker reported success. I inspected the diff: four files, one
  unrelated fixture reformatted, which I separated. I reran the unit selection: 41
  passed, 1 skipped. The schema file was not regenerated, so the output requirement is
  unresolved."
- No claim possible: "I could not run the migration check; it needs the staging
  database, which I am not authorized to use. Static review of the SQL found no
  destructive statement. Status: blocked, owner: database lead."
- Stale: "The suite passed before the rebase. I have not rerun it since. Status: stale."
- Concurrent edit: "Another writer changed `config/limits.yaml` after my run. The limit
  tests are stale; the others stand."

Debugging:

- Good: reads the whole trace, reproduces, traces the empty directory value back through
  five callers to a getter read before setup, writes a failing test, fixes the getter,
  adds guards at each layer.
- Bad: adds a retry because a similar service needed one last week.
- Borderline: adds a documented fixed delay in a test. Acceptable only if it waits for
  the triggering condition first, the delay is derived from known timing, and the reason
  is in a comment.

Review feedback:

- Good: "Checked the build target: it is 10.15 and this API needs 13. The legacy path is
  still required. Do you want the path fixed, or the old target dropped?"
- Bad: "Great catch, implementing now."
- Borderline: silently fixing a correct comment. Fine for the code; the thread still
  needs a statement of what changed and where.

## Decision Tradeoff Guide

### Review: three independent judgements

| Judgement | Question | Evidence | A wrong call costs |
|---|---|---|---|
| Validity | Is the alleged defect real here? | Source, reproduction, tests, history | Accepting a false finding: churn, regressions, lost behaviour. Rejecting a true one: the defect ships |
| Remedy | Does the proposed change fit scope, contract and constraints? | Alternatives compared against the requirement | Adopting an unfit remedy: new failure modes. Refusing every remedy: the defect stays |
| Authority | Who may decide this? | Ownership, policy, the request | Deciding for an owner: unwanted product change. Routing everything: stalled work |

Further costs to weigh:

- Wrong deferral: a valid finding with no owner disappears. Deferral has a cost; so does
  "no change". Both are actions and are recorded as such.
- Wrong severity: inflation blocks work on nits; deflation lets harm through.
- Wrong readiness: "ready" on a stale premise transfers the risk to whoever merges.

Remedy options to compare before accepting the reviewer's proposal: the smallest local
correction; a correction at the root that supersedes several findings; a guard or
validation at a boundary; removal of the unused surface; a test or fixture only (when the
code is right and the proof was missing); a documentation or contract clarification; no
change with recorded evidence; containment now and a designed fix later; a bounded
canary. The canary fits when the fit of the remedy is uncertain, the hard gates pass and
the scope can be reversed on its own. It gives local outcome evidence. A small sample and
novelty limit how far that evidence generalizes. It needs guardrails, a cohort, a stop
rule, a rollback and an expansion rule, all declared before it starts.

Default disposition by evidence result:

| Evidence result | Default disposition | Record |
|---|---|---|
| Any hard gate red | Pause, contain, reject or route | The exact gate, the active risk, current safe behaviour, owner, resume condition |
| Valid defect, fitting remedy, strong regression evidence | Accept and implement the coherent correction | Mechanism, consequence, diff, finding-specific proof, integrated checks, what invalidates it |
| Valid defect, disputed remedy | Keep the defect accepted and the architecture open | Alternatives, owners, tradeoffs, fallback, the evidence that would discriminate |
| Plausible claim, incomplete behaviour evidence | Investigate, or canary, inside a safe bounded scope | Hypothesis, the missing case, the stop rule, the state if not adopted |
| False or incompatible claim | Reject with technical evidence | Counter-example, supported behaviour, residual uncertainty, the evidence that would reopen it |
| Valid, outside the accepted change | Defer or route explicitly | Consequence, owner, tracking state, dependency, why the current work stays safe |
| Duplicate symptom with a shared cause | Supersede under the root finding | Dependency map and proof that every original path is resolved |
| Existing behaviour already meets the requirement | Keep it and close as no change | Requirement trace, relevant verification, why the edit adds nothing |

No change is a decision backed by evidence, not a score of zero. Deferral has a lifecycle
cost and must not be used to hide a blocking harm.

When two reviewers conflict: freeze the dependent work, restate both positions as claims
with their scope, find which premise differs (requirement, candidate, environment,
contract), collect evidence on that premise, and route the remaining choice to the owner
of the surface. Do not split the difference in code.

A reviewer who becomes an implementer, or an author who reviews their own change, has
changed role. Say so, and get a second reader for anything consequential.

### Verification: responses to a gate

| Situation | Response | What you may then say |
|---|---|---|
| A safe, relevant, sensitive check exists | Verify directly | The claim, with evidence |
| The check cannot fail for the concern | Redesign the gate (mutation, known-red baseline, a better fixture) | Nothing until the gate is redesigned |
| The check is unsafe or unavailable | Substitute: static proof, simulation, disposable environment, specialist, owner-run | A narrower claim that names the substitution |
| Only part of the scope can be checked | Narrow the claim | The checked clause, plus the unrun clauses |
| None of the above | Block | Blocked, with owner route and fallback |
| The claim no longer matters | Retire the gate and remove the completion dependencies on it | Nothing about the claim; record the replacement or the no-need evidence, the owner and a residual audit |

Gates to consider for a material claim: the repository's canonical full command; a
focused test plus the full relevant suite; a static or source proof where execution is
unsafe; red-green or a safe mutation for regression sensitivity; a clause-by-clause
checklist with owner resolution; a rebuild of generated artifacts and a diff read in
context; visual, accessibility or interaction inspection; a compatibility and migration
matrix; a fault, cancellation, fallback or rollback exercise; an independent reviewer or
specialist; a narrower completion statement; an honest blocked, failed, stale or unrun
state. A command is not required just because it exists, and a repository can have many
green commands and no evaluator for the actual user outcome. Making no completion claim
is not a failure. It can be the correct state until the evidence matures. A judgement
claim may have no useful command and still support a bounded owner decision when the
evidence is laid out.

Evidence strength depends on the question. A source read is strong for "what does the
code do on this path" and weak for "does it behave under load". A green CI run is strong
for "the configured jobs passed on this commit" and silent on anything the jobs do not
select. A stale negative result is still useful as a pointer to where to look. It is not
a current state.

Cost of the gate against cost of the claim being false: a typo fix does not need a
warrant, and a migration does. The gate that is never waived is the one between
observation and statement.

### Debugging

| Tension | Position | Selector |
|---|---|---|
| Speed against investigation | Investigate first; guessing produces rework | No selector. A short investigation is still an investigation |
| Rigor against severity | Phase order is fixed for every bug | Only note depth scales |
| Fix at source against fix at symptom | Source | Symptom-site guard only when the source is unreachable (third-party code), with the residue documented |
| One validation against several layers | Several, after a data bug | Skip a layer only when it cannot be reached by any other path, and say why |
| Fixed delay against condition wait | Condition | Fixed delay only for behaviour that is itself about timing, with the three conditions |
| Persist against stop | Stop at three failed fixes | The number is a working rule; a team with recorded data may tune it. The direction does not change |
| Fix against containment | Both, separately | Containment needs authorization and reversibility and never closes the investigation |
| Parallel against serial | Collect evidence in parallel; test hypotheses serially | One ledger, one owner |

Precedence when debugging guidance conflicts: the rules (the law and the phase gates)
outrank the techniques (tracing, waiting, layering); the techniques outrank the history of
how the method came about; and the scenarios used to test the method are never doctrine.

### Trust

| Source of a statement | Trust in intent | Trust in implementation detail |
|---|---|---|
| The person you work for | High, within their authority | Verify |
| A team reviewer | Evaluate | Verify |
| An external reviewer or reviewing agent | Evaluate; check they had context | Verify; stop if it conflicts with the owner's earlier decision |
| A worker's success report | None until inspected | Inspect and rerun |
| Your own memory of an earlier run | None after a change | Rerun |

## Theme Specific Artifact

Three records for consequential work. For small work, the ledger and report in SKILL.md
are enough. Keep exactly one authoritative copy of each record; a thread, a chat and a
ticket that each hold part of the state will disagree.

### Code review resolution record

```text
CODE REVIEW RESOLUTION RECORD
record_id / owner / last_updated:
state:                 prepared | in_review | triaged | remediation_approved | applied |
                       resolution_verified | re_reviewed | ready_with_limits
                       (alternates: blocked | routed | deferred | rejected | superseded | contained | stale)
change:                requirement or plan; base..head; generated and external artifacts; environments
request:               what was asked of the reviewer; verdict type requested
findings[]:
  id / source / location:
  claim:               restated, atomic
  evidence_checked:    source, tests, history, environments; role of each
  consequence:         reach, effect, likelihood, detection, recovery
  validity:            confirmed | refuted | unverified (what is missing)
  remedy:              chosen; alternatives considered; why
  authority:           who decided, on what
  disposition:         accept | clarify | reject | defer | route | contain | supersede | no change
  finding_proof:       evaluator, expected red, observed red, observed green
  integrated_proof:    suite, build, static checks, generated artifacts, final diff
  reopens_when:
unresolved_and_deferred: each with owner, tracking, safe current behaviour
limits:                scope not inspected; residual risk; who accepted it
invalidated_by:        force-push or rebase; generated, dependency or requirement change;
                       reviewer correction; stale approval; removal of a test or route
```

Validation before closing the record: every finding has exactly one disposition; no
`accept` lacks finding-specific proof; no `defer` or `route` lacks an owner; the head SHA
in the record equals the current head; approvals listed were given for that head.

### Completion evidence warrant

```text
COMPLETION EVIDENCE WARRANT
claim:                 one atomic statement and the next action it would authorize
state:                 proposed | defined | planned | ready_to_run | executed | interpreted | passed_bounded
                       (alternates: failed | blocked | unrun | stale | conflicting | not_applicable | retired)
candidate:             repository, branch, head, dirty files, generated inputs, environment
requirement:           the clause this claim answers, and what must not change
evaluator:             command or inspection; why it can fail for this claim; known red or mutation used
safety_preflight:      reads, writes, cost, network, credentials, data; authorization
execution:             when, where, full command, exit code, duration
observed:              counts, failures, skips, warnings, timeouts, retries, cache status, partial effects
interpretation:        which clauses are supported; which are not
scope_and_non_interference: what else changed; unrelated diffs separated
authority:             who accepts residual risk; who decides merge or release
recovery:              rollback path and whether it was exercised
limits:                what this does not prove
invalidated_by:        the events that make it stale
```

The ten things a warrant keeps apart: intent, exact candidate, evaluator fit, observed
result, failure sensitivity, scope, safety, authority, recovery, outcome value. A warrant
with nine of them and "n/a" on the tenth needs a reason for the tenth.

### Debugging session ledger

Five parts, written as the work proceeds:

1. **Symptom and reproduction**: exact error, where, frequency, steps.
2. **Evidence**: recent changes, boundary probe output, the backward trace.
3. **Comparison**: the working example and every difference.
4. **Hypotheses**: each with its minimal test and result, including the refuted ones, and
   the failed-fix count.
5. **Resolution**: failing test, single fix, verification, disposition, hardening layers,
   residual monitoring.

The full field list is in SKILL.md under Templates. Two rules for the ledger: it is not
written afterwards, and failures are never erased. A ledger that shows only the
successful hypothesis hides the information that would stop the next person repeating the
failed ones.

### Where each kind of finding should end up

| Finding | Durable form |
|---|---|
| Behavioural defect | Code change plus a regression test |
| Implicit requirement surfaced in review | Executable acceptance case |
| Deterministic, mechanical finding | Linter rule, schema, validator |
| Missing negative-case coverage that keeps recurring | Shared test helper or fixture |
| Ownership dispute | A written boundary |
| Comments that went stale under a moving diff | Smaller diffs |
| A convention nobody can justify | Removal of the convention |

Promote a finding into a control only when it recurs or is severe, and give the control a
scope, an owner, an evaluator and a retirement condition.

## Worked Example Set

Every example here is a decision fixture, not a record of a real incident. What carries
over to another codebase is the premise that changes the disposition or the state, not
the verdict.

### Reusing an example

Before applying an example, replace each of these with the target's own and verify it:

- the accepted behaviour or requirement, what must not change, and the exact reviewed
  range or final candidate (including generated inputs and outputs, environment and
  concurrent writers);
- the actual source, callers, generated artifacts, configuration, tests and history;
- intended and not-intended users, platforms, versions and environments;
- the claim (the reviewer's, or the completion statement and the action it would
  authorize), its strongest counter-example, the consequence and the severity;
- the evaluator and why it can reject the relevant defect; the expected pass, the
  relevant fail, skips, warnings, timeout, cleanup and fallback;
- sensitivity of data, credentials, network and external effects, and the safe way to
  check;
- defect validity separately from remedy fit, and the alternatives: code, test,
  requirement, configuration, upstream, automation, deferral, removal, no change;
- the owners and their decisions, the direct and integrated gates, fallback, rollback,
  and the first event that makes the result expire.

Do not copy a hypothetical command. Do not keep a verdict or a state when its decisive
premise differs in the target.

Testing an example that is kept for training or for evaluator tests:

1. Name the decision boundary it teaches and the expected disposition or state.
2. Identify the one or two premises that decide it.
3. Change one premise in a disposable copy. The expected disposition or state should
   change.
4. Ask independent reviewers to explain the result and give the strongest
   counter-argument.
5. Confirm it teaches a mechanism no other kept example teaches.
6. Compare the reasoning with real outcomes before calling the set calibrated.
7. Refresh it after a change of source, platform, policy, requirement or team practice.
8. Retire it when it no longer teaches a distinct boundary.

If the verdict never changes when the evidence is mutated, the example teaches a fixed
preference, not evidence. When reviewers disagree about a review example, find which
dimension is missing: requirement, fact, compatibility, severity, remedy, authority or
acceptable risk. For a completion example the candidates are claim, candidate,
requirement, evaluator, result, scope, safety, authority and recovery. Keep some held-out
and messy real cases next to the set, so that training does not overfit to tidy examples.

### Review feedback

**1. Boundary validation.** Comment: "`parseLimit` accepts negative values." Check:
read the function and its callers; add a test with `-1`, `0`, the maximum, an empty
string and a malformed value. The `-1` case fails. Disposition: accept. Fix at the
parser, not at the three callers. Proof: the new cases go red on the old code and green
on the new; the suite passes.

- False finding: the comment says an empty or null input can be dereferenced. The type
  boundary and a property test show that such input cannot reach the function under
  supported construction. Reject with that evidence. A generic null check added before
  inspecting the boundary is the bad outcome: the new branch hides a caller defect. Add a
  boundary assertion only if it makes the contract clearer for later readers.
- Borderline: the source suggests the input can be empty only through a deserializer
  whose current configuration is unclear. Investigate the deserialization contract. The
  finding stays unresolved; do not invent the behaviour.
- Flip: a new public constructor permits the empty input. The earlier rejection expires
  and the boundary has to be requalified.

**2. Compatibility cleanup.** Comment: "Remove the legacy code path." Check: the
project's lowest supported target against the minimum version of the newer API. The
lowest target is older. Disposition: reject the removal with that fact, and route the
real question (fix the path or drop the target) to the owner.

- Good removal: the support policy excludes the old platform, the migration is complete,
  usage and compatibility tests show no dependent path, and the owners approve.
- Bad removal: the branch is ugly, and the reviewer tested only the newest environment.
- Borderline: the platform vendor's documentation deprecates the API, but the
  repository's support window is undecided. Record the external fact, route the policy
  question, leave the code unchanged.
- Counter-argument to keep in view: a compatibility branch has a running cost. Keep it
  only while the support contract and the tests justify that cost.

**3. Concurrency.** Comment: "Two deliveries can both pass the guard." Check: a
deterministic fixture that releases both calls at the guard. Two external calls are
observed. Disposition: accept the defect. The remedy is a separate decision (see User
Journey Scenario).

- Bad: the severity label leads to immediate adoption of the proposed global cache, with
  no test of multi-instance failure, eviction or recovery.
- Borderline: the race is plausible from source but cannot be reproduced safely against
  the real service. Use a simulation and a specialist review, and keep the readiness
  statement bounded.
- Flip: if the cache already gives owner-approved durable idempotency with tested failure
  semantics, it becomes a viable remedy for that exact system.

**4. Security.** Comment: "User input reaches the query unescaped." Check: trace the data
flow by reading; build a safe fixture with a marker string against a disposable
database. Never test against shared or production data. Disposition: accept and route to
the security owner for the remedy review. The record omits payloads that would work as an
exploit.

- Good, for a path-traversal variant: the source data flow and a specialist-approved
  fixture show access outside the allowed root. Contain if it is active, normalize or
  redesign at the trust boundary, add negative cases, involve the security owner.
- Bad: the reviewer supplies an offensive command and the receiver runs it against shared
  or production data to prove the point.
- Borderline: static analysis reports a path, an upstream schema appears to constrain the
  input, and the enforcement of that schema is generated. Inspect the generated boundary.
  Neither dismiss the finding nor try to exploit it on a guess.
- Hard rule: a general code review can identify the problem and contain it. It cannot
  authorize sensitive testing or accept the residual risk.

**5. Unused feature.** Comment: "Implement the metrics endpoint properly: persistence,
date filters, CSV export." Check: search for callers, generated clients, dynamic lookups,
external consumers and roadmap entries. Nothing calls it. Disposition: propose removal.
If an accepted public contract or a real consumer turns up, the answer flips to
implementing it, and it then needs explicit requirements and verification like any other
feature.

- Bad: build the full subsystem because completeness looks professional.
- Borderline: a feature flag and an accepted near-term plan mention the endpoint, but its
  scope is unsettled. Route the product question. Do not build speculative architecture.

**6. Tests.** Comment: "This test does not test anything." Check: mutate the behaviour
under test and run it. The test stays green. Disposition: accept. Rewrite the test so the
mutation turns it red, then restore the code.

- Good challenge of the opposite claim ("the test proves retry recovery"): removing the
  retry transition makes the test fail for the expected reason, and the timeout,
  cancellation, exhaustion and fallback cases also tell the behaviours apart.
- Bad: the mock returns the final success directly, so the test stays green with the
  retry logic deleted. It is a proxy. Repair the fixture.
- Borderline: integration coverage exists but is flaky because of an external service.
  Keep the failure evidence, build a deterministic local test of the mechanism, and state
  what remains unobserved about the wider behaviour.

**7. Generated code.** Comment: "Fix the typo in `client.gen.ts`." Check: the file header
names its generator and input. Disposition: accept the defect, supersede the remedy. Edit
the schema under its owning process, regenerate, inspect the diff and the consumers, run
the compatibility checks, and confirm the rollback.

- Bad: edit the generated output because that is where the reviewer saw the problem. The
  next regeneration silently restores the defect.
- Borderline: the generator is temporarily unavailable while the output causes active
  harm. Contain under explicit owner authority, with a plan to regenerate and reconcile.
- Flip: an ownership investigation proves that generation was retired and the file is now
  maintained source. A direct correction becomes valid, but only after the metadata (the
  header naming generator and input) is corrected.

**8. Performance.** Comment: "This loop is quadratic." Check: confirm by reading; state
the workload (how many items in practice); measure a baseline with a reproducible input.
If the realistic size is twenty items, disposition: no change, with the measurement and
the size at which it would matter as the reopening event. If it is large, accept and show
before and after on the same input with identical results.

- Good, when the proposed remedy is a cache: a user-visible or operational requirement
  defines the workload; a reproducible baseline shows the bottleneck with correctness
  unchanged; alternatives are compared; cache invalidation and recovery are tested.
- Bad: an intuition about complexity, or one microbenchmark, drives a new shared cache
  with no end-to-end measurement.
- Borderline: the local benchmark improves, but production workload, memory pressure and
  invalidation cost are unknown. Keep the claim bounded, or run a limited canary under the
  owners with a stop rule.
- No change: the path is cold and the accepted performance requirement already passes.
  Avoid the complexity, whatever the theoretical speed-up.

**9. API ambiguity.** Comment: "Should this return 404 or an empty list?" This is a
question about intended behaviour. Disposition: clarify, routed to the API owner. Pause
any work that depends on the answer. Do not pick one and call it resolved.

- Good clarification: callers, the API contract and the product owner establish which
  state is meant; tests and a migration encode it before the implementation changes.
- Bad: take the reviewer's preference because it shortens caller code, and so change the
  error semantics silently.
- Borderline: internal callers expect an empty result while the public documentation
  specifies an error. Keep the conflict visible, stop the behaviour change, route the
  contract question to its owner.
- Split outcome: the reviewer can be right that the behaviour is inconsistent and still
  not be the one who decides which behaviour wins.

**10. Naming.** Comment: "Rename `handler` to `ingestHandler`." Check: is the name public,
does it violate a written convention, does it mislead? No to all. Disposition: no change,
with the reopening event (the name becomes public, or a convention is adopted). A rename
here would churn history and generated references for no observed benefit.

- Good change: a repository policy, repeated evidence that readers cannot find the
  symbol, or public API consistency shows real value, and the migration is bounded.
- Bad: label a naming preference "Important" and block a behaviour fix on it.
- Borderline: the name is confusing, but a larger refactor will remove the symbol soon.
  Defer under that dependency. Do not create two migrations.

### Completion claims

**1. Test suite.** Claim: "tests pass." Run the full applicable command, capture the exit
code, read the counts. Result: 0 failed, 3 skipped. Statement: the counts, the skipped
names and why, the commit.

- Bad: one focused file passes and the whole repository is called green. Report the
  selected scope and run the wider gates that the claim needs.
- Borderline: the full local suite passes, and a group that needs an approved external
  service is unavailable. State "local suite passes; integration blocked".
- Flip: if repository policy explicitly marks that external group as non-blocking for
  this class of change, the broader state may advance under that recorded rule.

**2. Build.** The linter is clean. The claim "the build succeeds" still needs the build
command for the target configuration, with generated assets, features and material
warnings reconciled. A debug build does not support a claim about the release artifact.

- Borderline: the debug build succeeds and release packaging for another platform is
  unrun. Report the exact target only.
- Flip: if the requested deliverable is only the verified debug target, the narrower
  statement is complete. Do not keep the broader wording.

**3. Bug fix.** The handler was changed. Reproduce the original symptom on the old code
(red), run it on the new code (green), run adjacent valid cases, run the suite. "I updated
the handler" is activity. "The request that returned 500 now returns 200 with the expected
body" is a result.

- Bad: the guard exists and a reviewer says it looks right, but the original symptom was
  never run.
- Borderline: a source proof shows the branch changed, but the parser that only exists in
  production cannot be invoked safely. State "repair supported by source; runtime effect
  unverified".
- Flip: an approved disposable fixture of that parser allows a direct observation, which
  can promote the runtime clause.

**4. Regression test.** A new test passes. Revert the fix and run it. It must fail, for
the expected reason. Restore and rerun. A test that was never red has not shown it can
detect the bug.

- Borderline: a direct mutation would be destructive. A minimal disposable model plus a
  source trace supports a bounded sensitivity statement only.
- Flip: if the test stays green with the target defect present, demote it to a proxy,
  even when every current run passes.

**5. Requirements.** Four accepted clauses. Three have tests. The fourth ("existing
output files are not overwritten") has none. Statement: three met with evidence, one
unresolved. A green suite does not make it four.

- Borderline: the technical clauses pass, and the product wording has two plausible
  readings. The requirement claim is `conflicting`. Route it to the owner.
- Flip: a versioned owner decision resolves the ambiguity. The affected tests and code are
  then evaluated again against that decision.

**6. Artifact.** A report page builds. Open it. Check the narrow and wide viewport, the
empty state, a long value, the loading state, the failure state, keyboard use and
accessibility. "The file exists" is not "the page is usable".

- Borderline: the desktop render and interaction pass, and no mobile viewport is
  available. Report the structural and desktop results. Cross-viewport readiness is
  `unrun`.
- Flip: approved mobile render and interaction evidence can promote the broader claim.

**7. Delegation.** A worker says "implementation complete, unit tests pass". Inspect the
diff. Rerun. See User Journey Scenario for a full run.

- Borderline: the files are correct, but another writer changed a dependency after the
  worker's run. The delegated evidence is `stale`. Verify the current composition again.
- Flip: one integration owner reconciles the dependency and fresh gates pass.

**8. Generated output.** The schema changed. Regenerate, inspect the output diff, check
the consumers compile and their tests pass. A hand edit to the output is not a fix.

**9. Migration and recovery.** Claim: "the migration is safe to release."

- Good: in an approved environment, the forward and backward paths pass on representative
  data; mixed versions are exercised (old code on the new schema, new code on old data);
  an interrupted run is tried; rollback, the state left behind, monitoring and the
  owner's process are all checked. A minimal mechanical form is up, then down, then up
  again on a disposable database, comparing schema and data each time.
- Bad: the migration applies once on an empty database and release readiness is claimed.
- Borderline: the forward migration passes, but a downgrade loses data that the old
  version requires. Readiness is `fail`, even when every normal test passes.
- Blocked: no approved disposable database is available. The recovery claim is blocked,
  and the readiness claim with it. Keep the other passes.
- Flip: a redesigned compatibility path, plus a verified cleanup of the residual state,
  can requalify the candidate.

**10. Performance requirement.** Claim: "the latency requirement is met."

- Good: the current candidate, with correctness equal to the baseline, is benchmarked
  against the declared workload, environment and baseline, in warm and cold states and
  inside the resource limits, with the threshold set before looking at results.
- Bad: one microbenchmark or a complexity argument is presented as evidence about the
  production tail.
- Borderline: a representative local workload passes; production contention and tails are
  unobserved. State the local benchmark result only.
- Flip: a bounded canary under the owner's guardrails can support a broader operational
  statement. It still does not show that the result is permanent.

**11. Completion without a favourable claim.** Claim: "verification is complete."

- Good failure: the full gate runs and finds a reproducible defect. The verification task
  is complete with state `fail`. The implementation is not complete.
- Good blocked result: direct proof in production is prohibited and no safe substitute is
  enough. The analysis is complete, and it reports the first unmet gate, the fallback and
  the owner route.
- Bad: add "probably" to a success statement because the evidence is missing.
- Retirement: a manual checklist is replaced by a reliable compiler rule with a known
  pass, a known fail, a fallback and little false blocking. After an audit of what still
  depends on it, remove the duplicate manual check.

### Debugging

**1. Empty directory.** Symptom: a `.git` directory appears in the source tree during
tests.

```text
symptom:    git init ran in the package directory
<- cause:   the worktree helper was called with an empty directory string
<- caller:  the session initializer passed its projectDir through
<- caller:  the test read projectDir from the setup context at module load
<- trigger: the context getter returned '' because it was read before beforeEach ran
```

Fix at the trigger: make the getter throw when read before setup. Then add layers: the
entry point rejects an empty or missing directory; the workspace code rejects a
non-existent one; under the test environment the git helper refuses to initialise outside
the temp directory; a stack is logged before `git init`. Test each layer by bypassing the
one before it. Bad version of the same work: add `if (!dir) return` next to `git init`.
Borderline: fix the getter and stop. Correct, but another path can still pass an empty
value.

**2. Flaky test.** A test passes alone and fails one run in five under load. It sleeps
300 ms and then asserts on an event list. Replace the sleep with a wait for the event,
with a five-second timeout and a message naming the event. Do not raise the sleep.

**3. Polluter.** A stray file appears after the full suite, never after a single test you
tried. Run test files one at a time and check for the file after each. The first file
after which it exists is the polluter. Then trace inside that file.

**4. Multi-component failure.** Signing fails in CI and works locally. Add one probe per
boundary: is the secret present in the workflow, is it present in the build script's
environment, is the keychain unlocked and the identity listed, what does the signing call
print. One run shows the secret present in the workflow and absent in the build script.
Investigate that hand-off only.

**5. Third failed fix.** Fix 1 removes a race and a second appears in the cache. Fix 2
locks the cache and a deadlock appears in shutdown. Fix 3 reorders shutdown and a test in
another module fails on shared state. Stop. Each fix revealed coupling somewhere else.
Take the design question to the human partner with the ledger.

**6. No root cause found.** After the full process, a timeout correlates only with an
upstream provider's incidents. Record what was checked and ruled out, add a bounded retry
with a clear error message, add a metric and an alert on the timeout. This is a completed
investigation, not a skipped one.

## User Journey Scenario

Three illustrative journeys. The systems are hypothetical. The remedies chosen in them are
examples, not prescriptions.

### Journey 1: three comments on a payment handler

**Contract.** Duplicate delivery of an operation identifier must create at most one
external charge.

**People.** The contributor supplies intent and tests. The reviewer tests hypotheses. The
payment owner decides what "duplicate" means. The storage owner decides persistence and
recovery. The integration owner reconciles and merges. A fresh reviewer checks the final
candidate. Nobody decides outside their own domain.

**Request.** The packet gives base and head, the files and generated artifacts, the
reasoning behind the local guard, the tests and results, the statement that concurrent
delivery was not tested, the supported environments, the rollback, and the verdict wanted
(correctness and readiness). It contains no payment payloads or credentials.

**Comments received.**

1. Critical: two concurrent deliveries can both pass the local guard.
2. Important: use a global cache to deduplicate.
3. Minor: rename `handler` to something more specific.

**Intake.** All three are read before any edit. They split into: a defect claim (the
race), a remedy proposal (the cache), and a preference (the name).

**Verification of the race.** A disposable fixture with a fake charge client releases two
calls at the guard. The old candidate makes two calls. A serial duplicate makes one. The
defect is confirmed. How often this happens in production, and how it would be detected,
were not measured, and the record says so. If the reproduction had been unsafe, source
reasoning and a specialist would have been used, and readiness would have stayed blocked.

**Remedy comparison.**

| Option | What it costs or leaves open |
|---|---|
| Leave the guard | The race remains |
| In-process lock | Fails across instances if more than one is supported |
| Atomic durable operation record | Schema, failure handling, migration, recovery |
| Global cache | Eviction, durability, split-brain, retention, availability, ownership |
| Deduplicate at an upstream gateway | Paths that bypass it, availability, ownership |
| Drop the guarantee | A product decision, not an engineering one |

The defect is accepted. The cache remedy is rejected on evidence (eviction and durability
do not meet the contract) and the alternatives go to the storage owner, who approves the
durable record with exact semantics.

**The rename.** The name is internal, consistent and clear, and a rename would touch
unrelated files. Disposition: no change. It would become valid under an enforced
convention, a repeated navigation problem, or exposure in a public contract.

**Dispositions are reported before editing.** Then only the approved storage, handler,
migration and tests change. The final diff is checked for accidental paths, a second copy
of non-atomic logic, unsafe logging, migration and rollback, behaviour when storage is
unavailable, and stale documentation.

**Proof.** Old and new candidates under the concurrent fixture; distinct identifiers;
failure, cancellation, retry and recovery; serial and integrated behaviour; migration
forward and back; the exact diff; a fresh re-review of the current head. The integration
owner makes the merge decision, with the limits stated.

**What is kept.** A deterministic concurrency fixture and an executable idempotency
contract. Not a rule that says "always use a durable record" or "never use a cache".

**Checkpoint if interrupted.** Outcome, mode, exact revisions, stable finding ids, safe
current behaviour, first unmet gate, owners, changed paths, failed and unrun cases, next
action. On resume, revalidate intent, range, writers, approvals and safety. A cache
shortcut, an owner disagreement, a fixture found to be wrong, a moved range, or a rollback
that loses data each send the work back to paused.

### Journey 2: "Implementation complete. Unit tests pass."

**Requirements for a batch importer.** (1) Valid rows persist exactly once. (2) Malformed
rows produce a typed report and leave no partial committed state. (3) Cancellation leaves
a resumable checkpoint, and a retry writes no duplicates. (4) Generated help and schema
match the input contract.

**People.** The request owner defines the outcome. The worker implements and returns
paths, evidence and gaps, and cannot verify its own report. The verification owner
reconciles. The data owner accepts persistence, recovery and retention. A reviewer
challenges. The integration owner decides merge or handoff.

**The report.** A worker returns "Implementation complete. Unit tests pass." with no
mention of the diff, integration, generated files, cancellation or rollback.

**Decomposition.** The sentence contains seven claims: the source changed as intended;
focused tests pass; the regression tests are sensitive; each requirement is met;
persistence, rollback, cancellation and retry work when integrated; the generated help is
current; the work is ready.

**Candidate.** Revision, worktree, changed and untracked files, generator inputs and
outputs, dependencies, config and other writers are recorded. The diff shows the schema
and help were not regenerated, and that an unrelated formatter fixture was changed. The
changes are preserved, the unrelated file is separated, the generated-artifact claim is
marked false, and one writer is named.

**Trace against requirements.** The valid-row test is serial and has no
duplicate-after-interruption case. The parser-error test has no assertion on transaction
state. Cancellation is untested. The old snapshots were neither regenerated nor checked
against consumers. A green unit run is not completion.

**Focused run.** Units pass. Database integration is skipped because the variable naming
the disposable database is absent. There is no generated-snapshot check. The cancellation
tests were not collected. The truthful statement is: "The current focused unit selection
passes; database integration, cancellation and generated artifacts were not exercised."

**Sensitivity.** The malformed-row test stays green when a partial commit is injected,
because it checks only the error value. It is a proxy. A transaction-aware test must go
red on a committed row and green on a typed report with no partial state, and must also
cover valid-once and idempotent retry. Where mutation is unsafe, use a disposable
database, a source proof or the data owner's evidence.

**Repair of the demonstrated causes.** Make persistence and checkpointing coherent and
recoverable; add cancellation and retry cases; change the authoritative schema input and
regenerate; separate the fixture; require generated artifacts in the worker's return
manifest.

**Final packet.** Defect red and current green; valid-once; idempotent retry; resumable
checkpoint; the partial-state model; full applicable suites with skips named; build and
static checks; clean regeneration and diff; rendered help matching the schema; scoped
diff; rollback and residue check; a fresh reviewer's reproduction. It does not prove
behaviour at every production volume, failure schedule or platform, and it does not
authorize data policy, merge or release.

**Lessons.** Enumerate generated artifacts. Expose skips. Make regression tests sensitive
to the mechanism. Map return fields to requirements. Make rollback executable. Adopt each
as a standing control only if it recurs or is severe enough to justify the maintenance
and the false blocks.

### Journey 3: five minutes into an outage

**Situation.** A full outage. A manager wants a patch now. You remember that a similar
service once needed a retry, and it would take two minutes to add.

**Do not ship the retry.** It is a guess from a different failure.

**Instead.**

1. Read the error that is actually being produced.
2. Add one probe at each boundary (for a release pipeline: workflow, build, signing,
   execution; for a request path: gateway, service, dependency, database). One run shows
   which layer breaks.
3. Narrate while you work: what evidence you have, which layer fails, what you are
   checking next. The pressure comes largely from silence.
4. If the harm must be reduced before the cause is known, propose reversible containment
   (drain traffic from the failing instance, roll back the last deploy, disable the
   flag), get it authorized, and state that it is containment. The investigation
   continues.
5. Trace back from the failing layer, form one hypothesis, test it minimally, write the
   failing test, fix.

**The other branch.** The retry is applied. It masks the failure or does nothing. A
second fix is stacked on it, then a third. Hours later the cause turns out to be
architectural, and the room no longer believes status updates.

The cost figures used to stage such a scenario in training are illustrative. The point of
the exercise is to choose and act under pressure, not to discuss what one would do.

## Anti Pattern Registry Table

The compact table is in SKILL.md. This registry groups the patterns by the link in the
chain that fails, which is what tells you what to repair.

### Review

| Anti-pattern | Mechanism | Consequence | Repair |
|---|---|---|---|
| Context-free or moving-target request | No requirement or range; lines drift after the review starts | Findings about code that no longer exists; real defects unseen | Freeze the range, state the contract, re-evaluate on the current head |
| Review theatre | Generic comments, an oversized diff, an approval that could not have been withheld | False assurance | Start from outcome and risk; stage the diff; atomic findings |
| Performative agreement | Social response before technical check | Wrong changes implemented politely | Restate, inspect, test, classify, then act |
| Blind implementation | An external suggestion applied because it sounds right | Regressions, scope growth, broken compatibility | Five checks; usage search |
| Defensive preservation | Authorship or inconvenience in place of evidence | Real defects ship | A falsifiable counter-claim; accept when overturned |
| Authority substitution | A senior voice treated as proof, or a technical result treated as permission | Wrong fact accepted, or unauthorized change made | Separate fact from authority |
| Severity laundering, lineage inflation | Tone, reputation, category, or the same comment repeated standing in for consequence | Attention spent on the wrong finding | Reclassify by reach, effect, likelihood, detection, recovery; count duplicates once |
| Literal-comment fix | Wording satisfied, mechanism untouched | The failure remains on another path | Trace the root and its dependents |
| Symptom-only fix | The reported line changes, the cause does not | Recurrence | Loop E |
| Partial fix | Some coupled findings implemented, others pending | Inconsistent state built on a guess | Pause the coupled set |
| Remedy conflation | Accepting the defect read as accepting the design | An unfit design adopted | Keep the remedy open |
| Unowned deferral | "Later" without owner or trigger | The finding disappears | Owner, tracking, condition, safe state |
| Thread-only closure | Thread state taken as technical state | Unverified "resolved" | One authoritative ledger; proof first |
| Stale approval replay | Approval reused after the diff changed | Unreviewed code merged | Requalify the current candidate |
| Proxy verification | A check that cannot fail for the finding | False confidence | Mutation or known red |
| Private-data dump | Payloads, credentials or whole logs pasted into the request | Exposure | Minimise; link to protected evidence |
| Unsafe verification | A destructive or production command run to settle a comment | Harm caused by the review | Static, disposable or specialist evaluator |
| Shared-write fan-out | Several workers editing the same surface to "address comments" | Conflicts, lost changes | One writer per artifact, one integrator |

### Completion

| Class | Named patterns | Repair |
|---|---|---|
| Claim formation | Speculative claim; claim bundling; scope creep by wording ("done" growing from "tests pass" to "ready"); satisfaction before evidence; activity reported as outcome | Split into atomic claims; one state each |
| Candidate and source | Stale evidence; wrong candidate (another branch, a clean checkout while the worktree is dirty); uninspected generated output; trusting a worker's report; ignoring a concurrent writer | Bind the exact identity; rerun |
| Evaluator selection | Proxy gate; test that cannot fail; lint or compile as behaviour; debug build as release; one platform as all | Redesign or narrow |
| Execution | Partial suite reported as full; hidden skip; cache-shaped green; timeout treated as pass or as no effect; unsafe proof | Read selection and status; reconcile unknown state |
| Interpretation and reporting | Summary-line trust; warning blindness; retry until green; averaging a red away; percentage readiness; "not applicable" without reason; a different word for the same unverified claim | Read everything; report by state |
| Lifecycle | Evidence not invalidated after a change; approval carried to a new candidate; a blocked item silently dropped; an obsolete gate never retired | Record what invalidates; requalify; retire with an audit of consumers |

### Debugging

| Channel | Signals | Response |
|---|---|---|
| Your own thoughts | "Quick fix for now", "just change X", "one more fix", "I see the problem, let me fix it", "it is probably X", "I will write the test after" | Stop. Seeing a symptom is not understanding a cause. Phase 1 |
| Your partner's words | "Is that not happening?", "will it show us?", "we're stuck?", "stop guessing", "think harder about this" | Treat the question as a reading that your own monitoring failed. Phase 1 |
| Structure of the work | Fix at the symptom site; bundled changes; no failing test; a fix stacked on a failed fix; a fourth attempt | Stop, isolate one hypothesis, investigate again |

Excuses and what is true:

| Excuse | Reality |
|---|---|
| "It is simple, no process needed" | Simple bugs have root causes. The process is short for them |
| "It is an emergency" | Guessing is slower than a directed investigation. Contain if needed |
| "Try this first, then investigate" | The first fix sets the pattern. Start correctly |
| "I will write the test once it works" | An untested fix does not stay fixed |
| "Several fixes at once saves time" | You cannot tell which one worked, and you may add bugs |
| "The reference is long, I will adapt the pattern" | Partial understanding produces bugs. Read it fully |
| "I see the problem" | You see the symptom |
| "One more attempt" after two failures | Three failures point at the design |
| "Should work now", "I am confident" | Confidence is not evidence. Run the check |
| "The linter passed" | The linter is not the compiler, and neither is the test suite |
| "The agent said it succeeded" | Verify independently |
| "A partial check is enough" | A partial check supports a partial claim |
| "I used different words, so the rule does not apply" | The rule covers the meaning |
| "I am tired", "just this once" | Neither changes what was observed |

Three ways the method itself degrades: anecdote inflation (numbers from one occasion
quoted as benchmarks); scenario leakage (a deliberately bad suggestion from a training
scenario quoted as guidance); and mandate softening (the absolute order rewritten as
"investigate when feasible"). When reusing this material, check the wording of every
`always`, `never` and `must` against the original rule.

## Verification Gate Command Set

SKILL.md has the seven core gates. These are the supporting commands and the selection
rules.

### Establish and guard the candidate

```bash
git rev-parse HEAD                                  # the candidate
git status --porcelain                              # dirty and untracked files are part of it
git merge-base origin/main HEAD                     # base for the review range
git diff --stat "$BASE_SHA".."$HEAD_SHA"            # the surface
git log --oneline "$BASE_SHA".."$HEAD_SHA"          # the history inside the range
git diff --quiet "$REVIEWED_HEAD" HEAD; echo "moved=$?"   # 0 = same candidate, 1 = moved
git ls-files -m -o --exclude-standard               # modified and untracked, for delegated work
```

### Find the authoritative command

Do not invent the test or build command. Look for it, in this order: the repository's
agent or contributor instructions, the CI workflow, the task runner, the package
manifest.

```bash
ls AGENTS.md CLAUDE.md CONTRIBUTING.md Makefile justfile package.json pyproject.toml Cargo.toml 2>/dev/null
grep -n -E "run:|script:" .github/workflows/*.yml 2>/dev/null | head -40
grep -n -A 20 '"scripts"' package.json 2>/dev/null
```

If the local command and the CI command differ, say which one you ran. The same check run
locally and in CI is one piece of evidence, not two.

### Run and read

```bash
set -o pipefail
<command> 2>&1 | tee /tmp/verify.log; echo "exit=$?"
tail -n 40 /tmp/verify.log
grep -n -i -E "skip|ignored|pending|xfail|deselected|todo" /tmp/verify.log
grep -n -i -E "warn|deprecat|timed out|retry|flaky|cached|FROM CACHE" /tmp/verify.log
```

Read for: exit status; totals (passed, failed, skipped, errored); what was selected and
what was not; warnings; timeouts; retries; whether results came from a cache; partial
effects left behind.

### Prove sensitivity

```bash
# Revert only the fix, keep the new test.
git diff -- <source paths> > /tmp/fix.patch
git apply -R /tmp/fix.patch
<test command>; echo "red exit=$?"       # must be non-zero, failing for the expected reason
git apply /tmp/fix.patch
<test command>; echo "green exit=$?"     # must be zero
```

Use a disposable worktree when the main one must not be disturbed:

```bash
git worktree add /tmp/verify-wt HEAD && cd /tmp/verify-wt
# ... mutate and run here ...
cd - && git worktree remove --force /tmp/verify-wt
```

When no revert is possible, mutate the behaviour by hand in the disposable copy (flip the
condition, remove the retry, inject the partial commit) and confirm the test goes red.

### Evaluator by claim

| Claim | Evaluator | It must be able to show | Negative or contrast cases | Limit |
|---|---|---|---|---|
| Tests pass | The full applicable test command on the current candidate | A failure, were there one; skips and exclusions | The focused subset against the full selection; skipped groups; a group that needs an unavailable service | Tests prove only what they exercise |
| Build succeeds | The full declared target build with generated inputs, features, packaging and material warnings | A compile or link error in the target configuration | Clean build, release mode, an alternate target, a missing generated artifact | One target does not prove every platform |
| Input or validation bug fixed | Reproduction of the original symptom on the exact contract, plus adjacent valid cases | Red on old, green on new | Empty, maximum, malformed, duplicate and neighbouring valid input | The fixture can encode the wrong requirement or miss integration |
| Error handling works | A traced cause plus safe failure injection and the fallback | The failure path taken and recovered from | Timeout, partial result, cancellation, exhaustion, recovery | Production failures may not be safely reproducible |
| Concurrency invariant holds | A deterministic schedule, a model or property check, a read of the synchronization in source, bounded stress | The violation under the bad schedule | Reordering, duplicate delivery, cancellation, shutdown, contention | Finite stress cannot prove all schedules |
| Security or privacy gate passes | The threat boundary, direct flow analysis, a specialist-approved safe test, a policy review | The unsafe flow, were it present | Unauthorized caller, untrusted input, redaction, privilege, fail-closed behaviour | A generic verifier cannot authorize offensive testing or accept residual risk |
| Performance requirement met or improved | A reproducible benchmark with declared workload, environment and baseline, and identical results | No change, or a correctness difference | Cold and warm states, the worst relevant input, contention, the failure path, the resource limit | A microbenchmark does not establish production tails or user value |
| Compatibility preserved | The supported-version contract, a version matrix, the migration, the mixed-version state, the owner's decision | A supported version or data shape that breaks | The oldest supported case, a downgrade, data compatibility, a removed feature | What the platform currently supports does not decide the local support policy |
| Migration safe | Forward, backward and forward again on a disposable database with representative data; mixed versions; an interrupted run | Schema drift, data loss, residual state | An empty database against representative data; old code on the new schema; a downgrade | Needs an approved environment; without one the claim is blocked |
| Regression guarded | Mutation or revert of the fix | Red without the fix | The target defect reintroduced by hand | A substituted red (model or source trace) supports bounded sensitivity only |
| Requirements complete | The current clause inventory mapped to tests, review assertions, artifacts and owner decisions | A clause with no evidence | Omitted, contradictory, not-intended and changed requirements | A trace can be complete while the requirements are wrong |
| User-facing artifact usable | Schema and build checks plus a representative render, viewports, accessibility and interaction | Broken states | Empty data, long text, failure state, mobile, keyboard, loading, recovery | A sample inspection cannot cover every device and user |
| Generated output current | Change of the authoritative input, regeneration, exact diff, consumer checks | A non-empty diff when stale | Regenerate twice, a clean baseline, stale output, rollback | The generator can itself be wrong or sensitive to its environment |
| Delegated work complete | Inspection of the returned artifacts, the approved scope, a local rerun, an independent requirement trace | Unrelated or missing changes | Missing files, unrelated edits, a stale baseline, a hidden external effect | An independent check can still share faulty requirements |
| Finding resolved | The finding-specific check plus integrated checks | The failure on any covered path | The other paths that share the mechanism | Thread state and a changed line show nothing |
| Feedback rejection correct | Current behaviour, the requirement, a counter-example, the consequence of the suggested change | The reviewer's case, if it were real | The reviewer's strongest plausible case | A weak counter-example creates false confidence |
| Feature removal complete | Caller and contract audit, behaviour before and after, migration, residual references, fallback | A remaining caller | Dynamic, external, generated, rare and compatibility consumers | Absence from a search does not prove absence of use |

### Durable evidence by claim family

| Claim family | Evidence to keep | Why |
|---|---|---|
| Deterministic behaviour | A focused failing case plus the broader relevant suite | Shows the mechanism and checks for regression |
| Build and type contract | The full target-specific build or compiler result | Observes how the declared artifact is built and its static constraints |
| Structural invariant | Linter, schema, formatter, static analyser or exact parser check | Enforces a deterministic shape cheaply, within its scope |
| Requirement completion | A requirement-to-evidence matrix with unresolved clauses visible | Stops a general suite from hiding missing intent |
| User-facing artifact | Structure checks plus rendered, visual, accessibility and interaction inspection | Existence and valid syntax do not establish usability |
| Generated output | Change to the authoritative input, the regeneration result, a diff read in context, consumer checks | A direct edit of the output disappears or diverges |
| Compatibility or migration | A version matrix, representative mixed states, the forward path and the rollback path | Success on the current version only can break supported users or data |
| Recovery | A safe fault, a rollback, a residual-state check and requalification | A written fallback may not be executable or independent |
| Architecture or specialist judgement | Alternatives, scenarios, direct constraints, the specialist's and the owner's decision | Several designs can be correct, and sensitive tests can still be insufficient |
| Delegated completion | Inspection of the actual diff, a current local rerun, a requirement trace, reconciliation of shared state | A worker's report is not independent proof |
| Explicit inability to verify | A blocked-state record: evidence completed so far, the safety boundary, the owner route, the safe fallback | An honest non-claim is safer than an unsafe or proxy execution |

The pieces have to hand off to each other. A test without a readable failure, a
requirement without an evaluator, a screenshot not tied to a candidate, or an owner
decision without technical evidence moves the uncertainty somewhere else. It does not
resolve it.

### Evaluator by defect class

| Class | Minimum cases |
|---|---|
| Boundary | The exact failing input; empty; maximum; malformed; duplicate; an adjacent valid value |
| Error handling | A traced cause; safe fault injection for timeout, partial result, cancellation, retry, fallback |
| Concurrency | A deterministic schedule, a model, or bounded stress; reorder, duplicate, cancel, shutdown, contention |
| Performance | A stated workload; a reproducible baseline; correctness parity before and after |
| Security or privacy | A stated threat boundary; a safe data-flow proof; a specialist-approved safe fixture; a policy review. Negative cases: unauthorized caller, untrusted input, redaction, privilege, fail-closed behaviour. Never offensive commands against shared or production data. Limit: a generic verifier cannot authorize offensive testing or accept residual risk |
| Flaky external integration | A deterministic local mechanism for the logic, plus an explicit statement of what the external system was not observed to do |

A mutation that removes the retry must make the retry test fail. A test that mocks the
final success directly is a proxy.

### Debugging phase gates

| Before | You must hold |
|---|---|
| Proposing any fix | Completed investigation notes and a trace to the trigger |
| Implementing | One confirmed hypothesis and a failing test |
| Accepting the fix | That test green, no other test broken, the original symptom gone |
| A fourth attempt | Not available. The architecture discussion comes first |

### Safety preflight

Answer before running anything that is not obviously read-only: what does it read; what
does it write, and where; what does it cost; what does it contact; which credentials does
it use; is the data private; can it be cancelled, and what does a cancel leave behind; is
there a dry-run; who authorized it. Any unknown that matters: do not run it. Use a
substitute and narrow the claim, or report blocked.

### Reporting

Each gate gets one state: `pass`, `fail`, `blocked`, `unrun`, `stale`, `conflicting`,
`not applicable`. Give a reason for everything except `pass`. Never report a percentage.
A timeout is an unknown effect, to be reconciled against the authoritative state before
anything is repeated.

## Failure Mode Table

| Failure | Signal | Containment and recovery |
|---|---|---|
| Range, context or source drift | Comments on lines that no longer exist; evidence and authority disagree | Freeze; rebuild the range; re-review; invalidate dependent states |
| Stale or wrong candidate | The verified SHA is not the reported one; dirty files not included | Invalidate; bind the exact identity; rerun the affected gates |
| Invalid or missed consequential finding | A counter-example, or an incident, shows the finding was false or a defect was missed | Stop the remediation or contain the effect; correct context and coverage; requalify |
| Generic advice or severity error | No local mechanism named; a style point blocks while a harm waits | Demote or exclude; reorder by consequence |
| Remedy or requirement failure | The root path remains; a regression; tests contradict the contract | Roll back or disable; separate defect from remedy; clarify the requirement; compare remedies |
| Omitted requirement, slice or generated artifact | A clause, module or output with no evidence row | Reconcile the inventory; the claim stays blocked |
| Proxy or insensitive gate | The test stays green under a seeded defect | Seed a relevant red; redesign or narrow the claim |
| Hidden skip, cache or partial output | Counts do not add up; "0 tests ran"; cached results | Parse the selection and result; keep the unverified scope visible |
| Timeout or unknown mutation state | A write command ended without a terminal state | Query the authoritative state before any repeat |
| Retry fishing, flaky shared dependency | Several reds, then an unexplained green | Keep all attempts; diagnose; throttle; never report only the favourable run |
| False-green or false-red verifier | Misconfigured, flaky or over-broad gate | Narrow the claim; test the gate with known pass, fail, skip and cancel cases; repair or retire it |
| Unsafe or unauthorized proof | A secret, destructive or external effect; stale or narrow approval | Stop and contain; safe evaluator, specialist, current owner approval |
| Generated or mirrored overwrite | A hand edit erased by regeneration or sync | Fix the authoritative input; regenerate; inspect residue and compatibility |
| Thread and record divergence | The thread says resolved; the ledger, range or the user's intent says otherwise | Reopen; link to the one authoritative record; reread it before writing |
| Unreconciled delegation, shared writers | Two workers changed the same surface; a report without a diff | One owner, one integrator; inspect and rerun |
| Missing authority or recovery | A technical pass with nobody to accept the risk, or no rollback | The result stays bounded; the transition is blocked |
| Fan-out, dependency or recovery failure | Queues grow; a platform or owner is unavailable; rollback fails | Backpressure; one integrator; an independent fallback; widen containment; requalify |
| False block, retirement residue | A gate blocks valid work, or an old check or comment remains after its reason is gone | Measure what it interferes with; narrow, replace or retire; audit consumers |
| Symptom fix recurs | The same failure through another path | Reopen as a debugging incident; trace to the trigger; add layers |
| Fix stacking | Several unreverted attempts in the diff | Revert to the last verified state; Phase 1 |
| Probe hides the evidence | Silence from a suppressed logger, a sampled trace or a buffered stream | Verify the channel with a known message first |
| Anecdote inflation | One occasion's numbers quoted as a benchmark | Label as not measured; remove the benchmark wording |
| Scenario leakage | A training scenario's bad option quoted as guidance | Keep scenarios evaluative only |
| Mandate softening | "No fix before investigation" rewritten as "investigate when practical" | Restore the absolute wording |

**Severity routing.** Local and low consequence: the code and review owner. Operational:
repository or module owners, with a coordinated rollback. High consequence (security,
private data, credentials, production, destructive, broad, correlated, unrecoverable):
contain, and hand to the controlling specialist process. Unknown reach defaults to the
stricter route. General guidance like this file never waives a policy.

**Incident loop** when one of these has already caused harm: record minimally; stop or
narrow; freeze outcome, range, artifacts and owners; keep the findings and corrections;
compare hypotheses; trace dependents; repair the controlling source; verify fallback,
residue and ownership; rerun every gate; add proportionate prevention; watch what the new
control costs; close with the confidence in the cause, the remaining uncertainty, the
owner and the recurrence check. A changed reply plus a clean lint run is not closure.

**Recovery from a false statement already made.** Withdraw or narrow it where it was
made. Restore the last verified state. Find which link broke: claim, candidate, evaluator,
execution, interpretation, authority or lifecycle. Repair that link. Reverify with a
check that would have caught the error. A fallback must not depend on the component that
failed.

## Workload Model

The load is decision and control capacity, not comment volume or command throughput.
Review work includes discovery, reconstructing the range, source reading, negative cases,
owner decisions, remediation, re-review, reconciliation, rollback and retirement.
Verification work includes defining the claim, binding the candidate, designing the gate,
running it, interpreting it, reconciling delegated work and exercising recovery.

**Dimensions of pressure.** Number of outcomes and claims; size of the change surface; how
coupled the findings are; breadth of source; consequence; ownership; uncertainty;
verification cost; reviewer context; coordination; lifecycle.

**Classes.** Classify by the highest consequence and coupling present. One line that
changes a permission can be specialist work. A hundred independent mechanical files can be
compact.

| Class | Shape | Operating model |
|---|---|---|
| Compact local | One claim or a few findings, one owner, a direct safe gate, simple revert | One verifier; ledger and report |
| Coupled repository | Several clauses or modules, shared state, generated code, migration, more than one owner | One integrator; staged gates; a manifest of artifacts; rollback |
| Distributed portfolio | Many candidates, a shared gate, cohorts | Federated owners; a common record; a versioned contract; staged rollout; selective disablement |
| Specialist-controlled | Security, data, credentials, production, external or severe effect | Contain and route the exact clauses; specialist approval; safe evaluator; recorded residual risk |

Move up a class when a consequence is discovered. Move down only when a boundary has
actually been removed.

**Default capacity.** One outcome and baseline. One writer per artifact. The smallest
coherent diff, finding set and evidence. Reserve capacity for clarification, the negative
case, the integrated run, re-review and recovery. Earlier material suggested fixed sizes
(one packet, at most twenty requirements, one matrix). Those figures were not measured.
Keep the idea of bounded focus and calibrate the numbers locally.

**Budgets.** Request context; evidence; review attention; gate design; execution;
interpretation; reconciliation; owner attention; recovery. When one runs out: return,
split or narrow the work; automate what is deterministic; stop starting new remediation;
serialize decisions; hold readiness. Do not spend the verification or recovery reserve on
more comments, more polish or more green commands.

**Parallel work.**

- Good boundaries: disjoint modules or domains; read-only questions; the defect question
  separate from the remedy question; independent tests; platform matrices with one
  interpreter; specialist clauses with a defined return.
- Bad boundaries: arbitrary counts; shared writers; workers on different untracked
  states; execution split from interpretation; a readiness statement before the
  specialist returns; fan-out that all waits on one owner.
- Every delegated unit needs: the claim, the requirements, the candidate, inputs,
  permissions, the evaluator, the expected failure, the return format, a stop condition
  and the integrator.

**Debugging cost.** The cost is front-loaded: minutes of investigation and bookkeeping
before any fix. It is repaid by rework avoided. The ratio was not measured; record your
own (see Outcome Metrics). Keep the gates even when the ledger shrinks to three lines.

**Resume record** for work that outlives one sitting:

```text
accepted_outcome:
workload_class_and_reason:
requirements_base_head_and_paths:
artifact_review_and_integration_owners:
completed_findings_or_claims_and_their_states:
active_units_and_write_boundaries:
failed_unrun_skipped_and_negative_evidence:
verification_interpretation_and_re_review_debt:
conflicts_rejected_remedies_and_deferrals:
debug_hypotheses_and_failed_fix_count:
current_safe_behavior:
changed_paths_and_artifacts:
first_unmet_gate:
next_action:
expiry_or_revalidation_event:
```

On resume, revalidate before acting: intent, requirements, candidate, writers, the source
of the command, approvals. For how to keep such a record across context loss, use
`tdd-progress-and-resume`.

## Reliability Target

Reliability here means that the recorded state agrees with the best current evidence. It
does not mean the feature, service or organisation is free of defects.

**Hard invariants.** A known violation blocks the claim. These are response rules, not
probabilities, and they are not averaged.

- No material claim without current, matched evidence.
- No statement about a candidate other than the one checked.
- No finding marked resolved without finding-specific proof.
- No proxy presented as regression proof.
- No fix before a recorded root-cause trace.
- No fourth fix attempt without the architecture discussion.
- No omitted requirement, generated artifact, platform or material skip.
- No secret, private data or unauthorized effect.
- No approval reused for a different candidate.
- No omitted failure, correction, rollback or unrun gate in the report.
- No consequential gate without a fallback, a rollback and an owner.
- The phase order of debugging is never softened in wording.

"Zero known violations" is not "zero latent defects".

**Calibrated indicators.** Local, segmented, and set before observing: false-block rate
of a gate, agreement on routing, recovery time, first-attempt stability of a check,
failed fixes per incident. Earlier material carried targets such as "100 percent",
"18 of 20", "zero" and "p95 under ten minutes for a reviewer to find the next action".
Those are prompts for a local target. They have no denominator, sample, owner or window,
and no achieved result stands behind them.

**A local contract** defines: the control and its owner; the accepted outcome; what
counts as an eligible opportunity, by stratum (intended, not intended, ambiguous, stale,
false, missed, failure, fallback, removal); the hard invariants; local objectives; the
warning and stop thresholds; method, denominator, exclusions and confounders; privacy;
fallback and recovery; the decision each result leads to; and an expiry.

**Rates** are reported only with stable definitions, and with numerator, denominator,
strata, window and exclusions. For sparse or severe cases use representative positive,
negative, stale and not-intended cases, tabletop or disposable recovery exercises,
independent owner review, incidents and long-run drift. "No misses observed" is not
proof.

**Fault schedule** to test the practice itself: a stale candidate; a proxy gate; a hidden
skip; two conflicting results; a timeout on a write; an unsafe command offered as the
only check; an owner who becomes unavailable; a rollback that fails. For each, the
correct outcome is a non-pass state with the reason.

**Never improve the numbers** by labelling anomalies as transient, overwriting failed
attempts with the passing one, or closing an item with no owner or recovery. Make a
control permanent only after repeated evidence or one severe event, and give it a test,
an owner, a rollback and a review date.

**Recovery sequence.** Detect (drift, invalid or missed finding, unsafe action, false
block, exposure, owner or dependency failure). Contain the harmful code, comment or
readiness statement and keep the manual path available. Diagnose which input failed:
requirement, source, reviewer, fixture, remedy, platform, authority. Restore, revert,
disable or reroute. Say what the safe next action is. Repair the controlling source.
Requalify. Record what was learned.

## Retry Backpressure Guidance

### Three different things are called "retry"

| Thing | Rule |
|---|---|
| Repeating a failed **fix** | Never. Revert it, count it, return to Phase 1 with the new information, form one new hypothesis, run one minimal test. At three, stop |
| Repeating a **check** unchanged | Only for a plausible transient on a safe, repeatable operation, within a budget, with every attempt kept |
| Running a check after a **change** | Not a retry. A new candidate, with fresh gates and a fresh budget |

No universal attempt count, delay, timeout or jitter exists. One retry is a conservative
example, not a standard. Choose the smallest local budget after the eligibility questions.

### States

| State | Condition | Action |
|---|---|---|
| `proceed` | Valid candidate, gate, capacity and authority | Run |
| `bounded_retry` | Known terminal result; repetition is safe; a transient mechanism is plausible; cumulative limits hold | Repeat within budget; keep both attempts |
| `throttle` | A pressure threshold is reached | Reduce concurrency and intake; protect the recovery reserve |
| `block` | Deterministic defect; unmet requirement; stale or irrelevant gate; policy or budget | Do not repeat. Fix, or report |
| `reconcile` | Timeout, cancel, unknown mutation state, or conflicting results | Query the authoritative state first |
| `escalate` | Unresolved safety, authority, ownership, source or recovery | Hand to the owner |

### Before any retry

1. What exactly failed, and what was its terminal state?
2. What class of error is it, on what evidence? "It might pass" is not a mechanism.
3. What has changed that could change the result?
4. Is the operation read-only or idempotent at every boundary it touches (file, process,
   platform, service, comment thread, external system)? Are there hidden effects: billing,
   caches, locks, audit entries, notifications?
5. Could the first attempt have left partial state? After a timed-out write, reconcile.
6. Are intent, range, approval and owner still current?
7. What does another attempt cost in data, quota and duplicate effects?
8. How is it cancelled and cleaned up?
9. What is the fallback?
10. What are the cumulative limits on attempts, time, cost and concurrency?
11. Will the result tell you something new?
12. What stops it: success, failure, budget, cancel, pressure, escalation?

Any unresolved answer that matters means no retry.

### Never retried blindly

A deterministic failure on an unchanged candidate. An uncovered requirement or an
irrelevant gate. A stale or unknown candidate. A write whose commit state is unknown. An
unsafe, credentialed, costly or unauthorized command. A policy stop or a user stop. An
exhausted budget or an open circuit. Corrupt output. A failure that needs a person to
interpret it. A missing owner or policy. An unresolved conflict. A failed fallback.
Another writer on the surface.

### Classifying a failed signal while debugging

Transient; stale evidence; missing context; true contradiction. Allow one bounded
refresh for stale evidence. After that, escalate. A true contradiction ends the current
hypothesis.

### Backpressure

Stop dependent work and do not merely warn when any of these holds:

| State | Meaning |
|---|---|
| Range red | The reviewed or verified range is not the current one |
| Evidence red | A material claim has no current support |
| Scope red | The change exceeds the approved scope or breaks compatibility |
| Safety red | The next step has an unassessed or unsafe effect |
| Authority red | The needed decision or approval is missing or stale |
| Verification debt | Changes are landing faster than they are verified |
| Reconciliation debt | Returns from workers or reviewers are arriving faster than they are integrated |
| Context drift | Intent, requirement or terms have shifted during long work |
| Dependency circuit open | A shared dependency keeps failing |
| User pause | The user said stop |
| Strike limit | Three failed fixes on one incident |

Release needs current controlling evidence for the state that was red. More reviewers or
more runners cannot supply authority or interpretation. If results arrive faster than
they can be interpreted or recovered from, continuing lowers reliability.

**Pressure controls.** Bounded delay with jitter; respect the server's rate-limit window;
caps per gate and per owner; queues ordered fairly by consequence and age; a circuit
breaker; quarantine of a contaminated candidate; a pause on new implementation while a
hard gate is red. A substitute check is acceptable only if it independently governs the
same requirement and was declared before the result was known. Revalidate candidates that
aged in a queue.

**Alternatives to repeating.** A delayed bounded repeat; a manual fallback; a reread or
re-review; a new candidate; reauthorization; rollback or compensation; routing or
escalation; abandoning or retiring the check.

**Attempt record.** Id and parent; candidate, gate, environment, tool and selection;
start, terminal state, cancel and effects; error class and eligibility; budget consumed
and remaining; delay and queue; bounded output or a pointer to protected output; actor,
owner, interpretation, next state. Group attempts under the original opportunity. Never
reset the budget or discard failed attempts on restart.

**Examples.** Good: a rate-limited read fails; the first attempt and the server's delay
are recorded; one bounded second attempt passes; both are kept and the check's
first-attempt stability is marked down. Bad: a deterministic test fails three times and
then passes with no explanation; the claim stays blocked. A deployment that timed out
needs a query of the authoritative operation state, not a second dispatch.

Persistent pressure can justify narrower gates, immutable fixtures and manifests,
idempotent operations, clearer ownership, or retiring low-value checks. Each of those
changes needs its own verification, rollback and review date.

## Observability Checklist

### While debugging

- [ ] Log entry and exit at every component boundary.
- [ ] Log what data enters and leaves, whether config and environment arrived, and state.
- [ ] Capture a stack before the dangerous operation, not after it fails.
- [ ] Write to a channel the runner does not suppress (standard error in tests).
- [ ] Include directory, working directory, environment and timestamp.
- [ ] Verify the channel with a known message before trusting silence.
- [ ] Print whether a secret is set, never its value.
- [ ] Run once, read where it breaks, then narrow.
- [ ] If the path cannot be reproduced, add data collection. Do not guess.
- [ ] Remove the probes afterwards. Keep only what earns a place as real logging.

Step debugging helps locally and fails across CI and multi-process boundaries. The shell
and JavaScript probe recipes need translating for other runtimes.

### For a material completion claim

Record enough to connect: bounded claim, exact candidate, required gates, outcomes,
interpretation, state transition, authority.

- [ ] Claim and candidate identity.
- [ ] Gate identity (the command, its source, the selection).
- [ ] Attempt outcome, including fail, skip, cache, cancel, timeout and partial.
- [ ] Interpretation and any conflict.
- [ ] Final state and who authorized the transition.
- [ ] Recovery, exception and next action.
- [ ] What the evidence does not cover.
- [ ] Where protected output is kept, and for how long.

Useful event names for teams that log this: `verification_opportunity`, `claim_defined`,
`candidate_bound`, `gate_selected`, `execution_attempted`, `evidence_interpreted`,
`claim_transitioned`, `correction_recorded`, `fallback_activated`, `drift_detected`,
`control_retired`. Use stable ids and parent links so that unfavourable attempts and
corrections survive. Use an explicit `unknown` instead of a guess.

### For review

Observe only what changes a named decision. The questions worth answering: was this an
eligible opportunity for review; were the requirement, range and method right; what was
the finding and its disposition; was there independent evidence; was there a
clarification, correction, fallback, rollback or owner action; what invalidated it; what
happens to the control next (retain, adapt, narrow, route, automate, roll back, retire).

Keep these distinct when counting: an opportunity, a request, a finding, a disposition, a
remediation, a verification, a correction, a fallback, a retry, an owner action, drift.
Do not count comments as defects, thread state as technical state, attempts as
opportunities, or a finally corrected state as a first-time success.

**Channel by need.** Structured logs for repeated transitions. Aggregate counters for
volume only. Privacy-safe traces for sequences. The resolution record or warrant for
low-volume consequential work. Periodic source and owner audits for drift. Incident
reviews for rare severe events. Interviews for usability. Nothing at all for low-value
controls.

**Alerts go to the owner who can act.** Stale approval: invalidate and stop. Invalid
consequential finding: stop the remediation and reroute. Missed severe defect: contain
and reopen. Sensitive command attempted: policy owner. False blocking: narrow or retire
the gate. Repeated correction cycles: separate defect from design. Verification debt:
backpressure. Owner unavailable: hold or find a delegate. The need has gone: retire.

**Do not record** raw prompts, full comment threads, private source, secrets, customer
data, hidden reasoning or complete shared logs. Use opaque identifiers and links to
protected evidence.

**Time measures** need comparable strata and defined clocks, must include failures,
retries, fallback and cleanup, and must not be reported as p50, p95 or p99 without enough
observations. A schema change breaks trend comparison unless the old data is migrated or
kept separate.

**Audit** a claim by replaying candidate, gate, result and transition, and by checking
that adverse attempts and expiry were kept. A green summary alone, or a command string
alone, is not auditable.

## Performance Verification Method

### Performance claims about code

A performance statement is a claim about a named workload, method, environment and
baseline, with correctness unchanged. It is not a statement about speed in general.

1. Before measuring, write down: the decision the number feeds; the target; the fixture
   and its size; cold or warm state; resource limits; whether the tail matters; the
   acceptance threshold.
2. Measure baseline and candidate the same way, on the same input, more than once.
3. Check that the results are identical. A faster wrong answer is a defect.
4. Keep the setup: versions, hardware, dependencies, raw results, variability, and the
   conditions that were not observed.
5. State the claim with its envelope: "On the 10,000-row fixture, cold cache, median of
   ten runs went from A to B on this machine; results identical; concurrency not
   measured."

One microbenchmark, or the assertion that a loop is quadratic, does not establish a user
or operational effect. For a review comment about performance, also compare cache
invalidation and recovery behaviour of the proposed change.

### Speed of debugging

Speed means less rework, not a faster first action. Two concrete levers:

- Replace guessed sleeps with condition polls. Poll at about 10 ms with an explicit
  timeout. Shorter intervals burn CPU; longer ones add latency.
- A fixed delay is legitimate only when it waits for the triggering condition first, is
  derived from known timing, and carries a comment saying why. Example: 200 ms because
  two ticks of 100 ms are needed. A commented sleep alone satisfies only the third
  condition.

One reported conversion of fifteen sleeps to polls raised a suite's pass rate and
shortened it. The direction is well argued. The magnitude comes from a single occasion and
was not measured here. Running a flaky suite in parallel can amplify its races.

### Performance of the practice

Comparing two ways of reviewing or verifying (a new gate, a new checklist, an automated
reviewer) is itself a measurement and follows the same rules.

- **Parity first.** Same requirements, same class of candidate, same ability to detect a
  known defect, same visibility of skipped scope, same meaning of the verdict, same safety
  and recovery. A fast syntax check does not replace a behavioural suite if a seeded
  behavioural regression stays green under it.
- **Method: paired replay by stratum.** Freeze revision, range, requirements, sources,
  fixtures, tools and rubric. Choose strata by consequence, size, novelty, language,
  ownership and mode, and include the hard boundary cases. Calibrate with known valid,
  invalid and hard-red cases. Run baseline and candidate identically, in varied order.
  Adjudicate independently. Check hard-gate parity before anything else. Include the cost
  of correction, re-review, fallback and owner time. Watch delayed outcomes.
- **Measures.** Opportunity coverage; completed reviews; precision of findings (valid
  over raised); recall of material findings, against known issues only; quality of
  accepted dispositions; correction cycles; escaped issues; decision time; total
  lifecycle cost. Publish unit, workload, inclusion, missing data and window.
- **Cost split.** Execution; interpretation and review; correction and retry; queueing;
  owner time; recovery; maintenance; storage; privacy. A better median can hide queue
  ageing, retries or stale candidates in the tail.
- **Integrity.** Keep failures, timeouts, fallbacks and inconclusive runs. Keep
  denominators separate. Prevent duplicate attempts from counting twice. Look for
  learning and order effects, tool drift and dependence on one adjudicator. Keep negative
  results.
- **Decision.** Adopt when parity holds and the benefit is material across the intended
  workload with no unacceptable transferred cost. Adapt or run a limited trial when
  evidence is sparse or environment-specific. Avoid when the candidate omits scope, hides
  failures, runs unsafely, or its verdicts disagree with the baseline without
  explanation. Keep the baseline until the rollback condition expires. Revalidate when
  requirements, fixtures, tools, hardware, reviewers, dependencies, concurrency or
  workload mix change.

A handful of structured expert reviews can be promising and is too sparse for percentile
or productivity claims. No comparative study, universal latency target or achieved
improvement stands behind this skill. Comment speed, finding count and tool-call count
are intermediate quantities only.

## Scale Boundary Statement

Scale begins where one person or agent can no longer keep the sources, authority,
effects, verification, integration and recovery of a piece of work coherent. It does not
begin at a line count, a file count or a context size. A one-line credential or schema
change can be specialist work. A very large generated diff can stay local.

**Assess independently:** consequence, coupling, ownership, writable state, breadth of
source, verification, recovery, concurrency, duration. A strength in one does not offset a
weakness in another: good source visibility does not make up for unknown recovery.
Escalate by the strongest boundary that applies.

**Zones.**

| Zone | Signs | How to work |
|---|---|---|
| Local | One candidate, one authority, executable gates, contained recovery | One person or agent, the ledgers in SKILL.md |
| Coordinated | Independent slices that share integration or resources | One writer per slice; read-only checks in parallel; a versioned manifest; a merge order; checkpoints; backpressure; one integrator |
| Specialist-controlled | Security, privacy, legal, data, production, irreversible effect, or domain judgement | Named approval; least privilege; an approved environment; rollback or containment; a recorded residual-risk decision |
| Redesign | Slices cannot fail, recover or retire independently; the property is emergent; coupling, ownership or verification cannot be bounded | Stop and redesign before any completion claim |

Moving up a zone acknowledges a boundary. Moving down requires that contracts, isolation
or authority have actually improved.

**The smallest useful slice** is one that can be independently assigned, frozen and
reviewed, verified by its own gate, approved, observed, disabled or rolled back,
recovered or replayed without duplicate effects, and retired. Its contract names: the
claim; the revision, artifacts, config, data and environment; its dependencies (code,
data, config, runtime, source, authority, lifecycle); the gate, with skip, cache and
partial visibility; one writer and one verification owner; its states; its effects; how
its failure is isolated; correction, rollback and escalation; who consumes it at
integration; and how it retires. Migrations that cannot be separated stay atomic and get
more coordination, not less.

**Edges that imports do not show:** generated files, indexes and build caches;
migrations, snapshots, retention and consistency; settings, secrets, regions, tenants and
service versions; queues, rate limits, locks and external traffic; reused evidence and
its consumers; who may write, approve, deploy, accept risk, roll back and retire; shared
cleanup. Dependency graphs help narrow the search and miss runtime, organisational and
policy edges.

**Partitioning.** By component or service, by requirement, by risk band, by workflow
stage, by immutable shard, by ownership of file or theme, or with central integration.
Choose one primary partition and expose the overlaps. Run a shared gate once under one
identity, and invalidate every consumer of it when the method or candidate changes.

**Rules for distributed review and verification.** Freeze and version the shared
assumptions. One writer per artifact. One verifier per slice and one integrator for the
whole. Parallelise only immutable read-only checks. Require structured returns with
failures, retries, skips, cache status and uncertainty. Reject stale returns. Group
retries. Limit active slices to what integration, specialists and recovery can absorb.
Stop when queues, conflicts or verification waits grow. Run contract and end-to-end gates.
Close only under integrated authority. A system-wide property needs a system model and a
fault schedule; labelling components does not make them independent.

**Failures at scale and their response.**

| Failure | Response |
|---|---|
| Omitted slice | Reconcile the inventory; block |
| Overlapping authority | One owner |
| Candidate skew between slices | Rebind and rerun |
| Contract drift | Version it; test compatibility |
| Cyclic invalidation | Merge the slices or redesign |
| Correlated dependency failure | Circuit and recovery |
| Integration bottleneck | Throttle, add capacity or shrink the packets |
| Orphaned recovery | Specialist or redesign |
| Green locally, red globally | A system-level gate |
| Lifecycle residue | Coordinated cleanup |

**Readiness audit before working at scale.** List claims, dependencies, gates, effects,
owners, recovery and lifecycle. Show that each slice can be approved, observed, disabled,
corrected, recovered and retired on its own, or name who integrates it. Freeze and read in
parallel. Inject a slice failure. Change a shared contract and confirm the dependants go
stale. Interrupt and resume. Fail a dependency and confirm there is no retry storm.
Exercise every rollback. Retire something and clean up its consumers. Record the risks
that remain with owners.

**Debugging at scale.** Hypotheses are tested serially within one incident. Evidence can
be gathered in parallel, through one ledger and one verification owner. Three failed
fixes escalate. Repeated fixes that each reveal new coupling are an architecture signal,
not bad luck, and redesign starts where this method ends. The method is not enough alone
for several independent systems, several ownership boundaries, unbounded source discovery,
or production traffic with no stated service objective. In a large codebase, narrow the
dependency and source graph first (see `codebase-navigation`). In long work, context
drift is a reliability failure: checkpoint, summarise the risks, and reread the
requirement.

The aim is bounded failure domains whose evidence composes, not the largest number of
workers. When integration, invalidation and recovery cost more than the parallelism
gains, improve the contracts, the seams, the ownership or the architecture.

## Outcome Metrics and Feedback Loops

Measure accepted decisions and safe changes at acceptable total cost. Do not measure
comment count, speed, approvals, severity distribution, report length, command count or
coverage percentage: each can improve while the intent is missed. Agreement and closure
are not correctness.

**The question a measurement answers.** Does this control (a checklist item, a gate, a
review step) improve this outcome (accepted finding, right remedy, correct readiness
state) for these classes of work, against this baseline, while the guardrails on fact,
scope, compatibility, safety, privacy, authority and recovery hold, at an acceptable cost
to authors, reviewers, tools, correction, queues and upkeep?

**Outcome families.**

| Loop | What to observe |
|---|---|
| Review | Finding validity (confirmed, false, duplicate, stale, unsupported, missed); correctness of disposition and remedy; alignment with requirements; coverage of meaning, not lines; regression and recovery; clarifications; corrections and rework; latency and effort; non-interference; whether the control is sustainable |
| Completion | Accuracy of the recorded state; candidate freshness; claim and evidence alignment; requirement coverage; failure sensitivity of gates; completeness of result reading; reproducibility; non-interference; safety and privacy; accuracy of authority; recovery; latency and effort |
| Debugging, per incident, in the ledger | First-time fix (yes or no); time to fix against time spent thrashing; new bugs introduced by the fix; failed fixes; recovery of the test pass rate; change in suite time |

A rising average of failed fixes per incident is the earliest alarm. It can mean
investigation is eroding or the architecture is ageing, and it shows before the fix rate
falls. Without recording, the visible cost of investigating first hides the rework it
avoided. A useful leading sign: explicit probes are reducing the blast radius or the
uncertainty. A failure sign: jumping to a known pattern before the shape of the problem is
established.

Figures quoted with the debugging method (a high first-time fix rate against a low one;
a quarter to half an hour against two to three hours) are an author's account and were
not measured. They are not your baseline. Start your own series without them, and review
it as incidents accumulate.

"Every shipped claim has a requirement id and fresh evidence" is a usable leading
indicator only once "claim", "requirement id" and "fresh" are defined locally. Red-green
proof applies to behavioural regressions, not to every architecture or artifact decision.

**Hard guardrails.** These stop expansion of a control whatever the soft numbers say:
stale or wrong range or candidate; unsupported finding or claim; broken compatibility or
scope; sensitive exposure; unauthorized effect; stale or narrow approval; omitted misses,
corrections, rollbacks, bypasses or unreviewed cases; no fallback or owner. Known
violations block. They are not percentage deductions.

**Cost.** Preparation, candidate capture, gate design, inspection, execution (setup,
services, cache, artifacts, cleanup, retries), interpretation, triage, remediation,
verification, correction, queues and reconciliation, owner attention, recovery, upkeep
and retirement. Report wall-clock time separately from total human, machine and owner
effort.

**Methods**, least intrusive first: controlled replay; independent paired review or
interpretation; a limited trial on real work; an audit sample; a privacy-safe trace of
states; incident review; long-run review. Use the least intrusive one that can change the
decision. Higher consequence needs stronger and more independent evidence.

**Protocol.** Set baseline, strata, outcome, guardrails and thresholds before observing,
from consequence, reversibility, frequency, capacity and baseline. Freeze the relevant
conditions. Include intended, not-intended, negative, stale, ambiguous, duplicate,
partial, skipped, blocked, unsafe, delegated, failure, fallback and no-change cases.
Define denominators and what counts as false success, false block, correction and
bypass. Capture failures, timeouts, cancels, unrun and reverted work. Minimise data.
Review the guardrails first. Analyse mix, difficulty, learning, co-changes and owner
availability. Keep the observation replayable. Apply the action that was declared in
advance, with an expiry. With sparse samples use raw cases and qualitative review. Make
no causal, percentile, productivity or escape-rate claim without stable denominators and
follow-up.

**What each signal should change.**

| Signal | Action |
|---|---|
| The same deterministic finding recurs | Make it an executable gate |
| Many invalid findings | Fix the context given to reviewers, or the routing |
| Remedies keep changing after acceptance | Separate defect from design earlier |
| A class of defect is missed | Add a specialist route or a scenario |
| A gate blocks valid work | Narrow, demote or retire it |
| Fewer clarifications but more silent wrong assumptions | Roll back the change that reduced clarifications |
| Stale success, drifted ranges | Better manifest and invalidation; smaller units; identity check |
| Requirement gaps found late | Add the clause trace |
| Delegated returns keep missing artifacts | Strengthen the return format |
| Hidden skips or cache hits | Parse them in the gate |
| A recurring proxy gate | Redesign it |
| Proof is unsafe to obtain | A safe substitute or an owner route |
| Queues cost more than the control gives | Backpressure, federate or prune |
| The class of problem has disappeared | Retire the control, after a safety check |
| A stable automated check duplicates a manual one | Retire the manual one |

Keep or expand a control only when the correct state improves and the guardrails and cost
hold.

## Completeness Checklist

Completeness depends on the mode. An explanation is complete without a diff. A review is
complete at findings. A plan is complete without execution. A failed or blocked
verification can be complete. Applied is not verified. A focused pass is not an
integrated pass. A technical pass is not release authority. Claim the narrowest state the
fresh evidence supports and name the first unmet gate above it.

**Universal blocks.** Any one prevents the state being claimed, and none is averaged
against polish, speed or the number of boxes ticked:

- ambiguous claim;
- stale or unknown requirement, range, candidate, generated state, environment or owner;
- unsupported finding;
- a change that is out of scope, incompatible, or fails equivalently on another path;
- sensitive or unauthorized effect;
- approval that does not cover the exact diff and domains;
- a direct test that cannot discriminate, or an integration run left unrun without a
  bounded reason;
- partial, timed-out, cancelled, conflicting or cache-ambiguous output;
- intended or not-intended scope that is claimed and untested;
- unreconciled delegation;
- authority inflation;
- no owner, fallback, rollback or safe behaviour;
- a concurrent writer;
- omitted unfavourable findings;
- `not applicable` without a reason.

**States and what each requires.**

| State | Requires |
|---|---|
| Explanation complete | The question answered at the depth asked; fact, hypothesis, external statement, owner decision and synthesis kept apart; no implication of review, pass or readiness; the next route named |
| Request prepared | Outcome and requirements; base, head, worktree, paths, generated files, migrations, dependencies; an accurate summary; observed test results; environments, risks, exclusions, fallback; the verdict and expertise wanted; no sensitive data |
| Review complete | A stable range; inspection of source, tests, config, generated output and history in proportion; atomic findings ordered by consequence with evidence, uncertainty and action; evidence-bearing strengths; scope skipped; a bounded recommendation and the owner gates; no writes |
| Feedback triaged | Everything read; ambiguity paused or clarified; every comment has a disposition; defect kept apart from remedy and severity; duplicates merged; scope, compatibility, consequence, owner and safe state recorded; alternatives noted |
| Remediation approved | Named owners approve the exact range, paths, behaviour, data, commands, compatibility and rollout; conditions and exclusions stated; no material change since approval |
| Applied | Only approved files; authoritative inputs for generated code; no accidental, sensitive or rejected change; direct tests and structural checks run. Not yet "resolved" |
| Claim defined | Atomic wording; outcome; requirements and what must not change; candidate; consequence of a wrong pass and a wrong fail. This permits gate design only |
| Verification planned | A claim-sensitive evaluator; expected pass, fail, skip, warning, timeout, cancel and stop; effects, data, network, credentials, cleanup, fallback, owner. A plan has no result |
| Ready to run | Frozen candidate and inputs; the authoritative command; a healthy environment; no concurrent writer; preflight done |
| Execution complete | A known terminal state; full exit, counts, skips, warnings, cache, timeout, retries and cleanup; candidate unchanged; effects reconciled. Invocation alone is not this |
| Bounded pass | The exact claim supported; a known red where behavioural; scope and unrun conditions explicit; no authority inflation; expiry recorded |
| Failure complete | A reproducible, scoped contradiction; environment, fixture, command and requirement errors separated from real failure; effects contained; the next step (repair, reject, roll back, route) identified |
| Bug or regression verified | Current requirement and mechanism; baseline or mutation red; candidate green; adjacent negative, boundary and valid cases; integrated build, static checks, generated files and diff; recovery and owner clauses |
| Requirements complete | A versioned inventory accepted by the owner; each clause mapped; contradictions, not-intended behaviour and compatibility resolved; no inventory inferred from the tests |
| Artifact complete | Authoritative generation and structure; representative states (empty, long, loading, failure, keyboard use); viewport, accessibility, interaction, packaging and consumer checks; no stale output; audience limits stated |
| Delegated work verified | The return treated as provisional; files, effects, unrelated changes, scope, requirements, generated output, migration, config and dependencies reconciled; independently rerun; gaps reported |
| Resolution verified | The original claim, or a strong rejection; old or mutated code fails and the candidate passes; positive, negative, boundary, failure, compatibility, migration and cancel cases; integrated checks; other supported paths; safety, authority, recovery; unrun limits explicit |
| Re-review complete | A fresh reviewer has checked the current candidate, prior and new findings, direct and integrated evidence, and the ledger. New findings return to triage |
| Root cause established | Error read in full; reproduction; recent changes checked; boundary evidence; a trace to the original trigger; differences from a working example listed |
| Fix verified | One confirmed hypothesis; a failing test seen red; one change; the test green; the suite run; the symptom gone; failed-fix count recorded; hardening considered; probes removed |
| Blocked handoff | The exact unavailable premise; completed evidence; the broad state marked inactive; safe behaviour and the prohibited operation; owner question, fallback, resume action; minimal sensitive context. Blocked is neither pass nor fail |
| Ready with limits | Every applicable gate passes; blockers resolved or controlled; deferrals and routes demonstrably non-blocking, with owners and triggers; limits, risk and recovery visible. The recommendation is `ready`, `ready with named fixes or limits`, or `not ready`. The owner decides |
| Rolled back | Trigger and decision; the prior safe code, artifact, config, data and workflow restored; residue in generated, persistent, cached and external state checked; the failed candidate kept as negative evidence; re-adoption needs a changed cause and full requalification |
| Gate improvement adopted | Recurring or severe value shown; pass, fail, false-trigger, skip, timeout, disable, fallback and rollback cases tested; owners accept the upkeep; staged rollout, monitoring, rollback and a retirement date |

Deferred, routed, contained and rolled-back states need safe current behaviour, an owner,
a trigger, evidence, a fallback and a requalification step. They are not technical
closure.

**Statements that are never valid:** "reviewed" from having read the headings; "fixed"
from a changed line; "verified" from a lint run; "approved" from a severity label;
"current" after a rebase; "safe" from one environment; "deferred" with no owner; "closed"
from thread state.

**Recall check** for someone learning the debugging loop. They should be able to answer
without looking: what the four phases are, in order; what must happen before any fix is
attempted; what to do when a hypothesis is refuted; why several fixes at once are not
allowed; what to do when something is not understood; whether a simple bug is exempt.

## Adjacent Reference Routing

Keep preparation, intake, disposition, remediation, re-review, verification and
root-cause investigation here. Route only an atomic premise that needs another method,
source, expertise or authority.

| Question | Where it goes |
|---|---|
| Why did it break? How do I find the cause? | Stays here (loop E) |
| Is it done? Can I say it passes? | Stays here (loop D) |
| How do I write the failing test well? How do I keep red-green-refactor state across a long task? | [tdd-progress-and-resume](../tdd-progress-and-resume/SKILL.md) |
| What are the requirements? What should the acceptance cases be? | [executable-specs](../executable-specs/SKILL.md) |
| Where is this code? Who calls it? What is the dependency graph? | [codebase-navigation](../codebase-navigation/SKILL.md) |
| How do I commit, branch, open the pull request, finish the branch? | `git-delivery-flow` |
| How do I brief, bound and reconcile subagents? | `agent-context-and-orchestration` |
| Which design or approach should we choose? How should the system fail? | `explore-and-decide`, then back here when a concrete change exists |
| How do I write or restructure a skill like this one? | [authoring-skills-and-references](../authoring-skills-and-references/SKILL.md) |
| Why close the loop at all? | [A00](../../../A00-LLM-Principles01.md), [A01](../../../A01-LLM-Workflow01.md), [A03](../../../A03-Executable-Specs01.md) |

Notes on the boundaries:

- A flaky test starts here (diagnosis). The style of a new test belongs to the TDD skill.
  If the cause is architectural, it ends in a design discussion.
- Diagnosis comes before prescription. A retry can be the tempting wrong fix in a
  debugging incident and a legitimate architecture choice in a design discussion.
- In TDD, "the simplest code that passes" is about the next increment. In debugging,
  "the root cause" is about where a wrong value originated. Do not use one to answer the
  other.
- "Did the test run?" is settled by the command, its configuration, the selection and the
  output, before any general research.

**Handoff packet** when routing a premise to a person, a specialist or another agent:

```text
route_id:
original_outcome:
atomic_question_or_premise:
why_it_changes_the_disposition_or_claim:
why_local_work_is_insufficient:
requirement_range_candidate_environment:
finding_or_claim_and_its_current_state:
expected_pass_and_relevant_fail:
completed_evidence:
negative_conflicting_skipped_and_unrun_evidence:
current_safe_behavior:
safety_privacy_and_authority_boundary:
allowed_tools_and_write_scope:
requested_return_fields:
stop_timeout_or_cycle_condition:
integration_owner:
resume_action:
```

**A return must state:** the answer as `confirmed`, `narrowed`, `contradicted`,
`incompatible`, `unresolved`, `routed` or `not applicable`; the exact evidence, version,
candidate and owner; the boundaries; alternatives considered and anything not run; the
authority behind it; its effect on the local work; and the first unmet gate. Accept
"unknown" and negative returns as results. Then reconcile atomically and rerun the local
gates. A return is not completion.

**Route states:** `local`, `route`, `wait`, `return`, `conflict`, `closed`.

**Invalid routes.** Routing on a keyword. Treating a file's name or date as authority.
Sending the whole repository or conversation. Several agents writing to the same
candidate or record. Letting a prompt decide policy, product, security, merge or release.
Letting the destination widen tools, data access or write scope. Dropping the rejected
alternatives or the negative evidence. Treating the return as completion. Cycles with no
new evidence and no stop. Fan-out beyond what the owner, the environment or the
integrator can reconcile.

## Source Evidence Mapping Table

What each body of source material supports, and what it does not.

| Source | Kind | Supports | Does not support |
|---|---|---|---|
| Owner's pattern reference on code review feedback (July 2026) | Owner's synthesis | The review loop; the eight dispositions; request contents; the mode table; the write preflight; gate order; the resolution record; workload classes; backpressure states; evidence roles and verbs | Any measured rate; current behaviour of hosting platforms; that a given remedy is right for a given codebase |
| Owner's pattern reference on completion verification gates (July 2026) | Owner's synthesis | The ten-part completion claim; the claim table; the seven states; the warrant; evaluator selection; retry states; event names; the scale zones and slice contract | Target correctness; current command names in any repository; hosted CI behaviour; measured improvement |
| Owner's pattern reference on systematic debugging (July 2026) | Owner's synthesis | The precedence of rules over techniques over history over scenarios; the session ledger; the per-incident measures; the reading of three as doctrine; the anecdote labels | Efficacy of the method; any of the figures quoted with it |
| Superpowers skill collection, receiving code review | Third-party method | The read, understand, verify, evaluate, respond, implement sequence; no performative agreement; the coupled-ambiguity stop; skepticism toward external feedback; the usage check; pushback conditions; thread replies | Team-specific phrases and house style as general rules; the current shape of the hosting API |
| Superpowers skill collection, requesting code review and reviewer brief | Third-party method | When to request; base and head capture; the reviewer's checklist families; the findings format; severity handling | The mandatory "strengths" section and the yes/no merge verdict as stated (see SKILL.md, Where the Sources Disagree) |
| Superpowers skill collection, systematic debugging with its companions on root-cause tracing, defense in depth and condition-based waiting | Third-party method | The law; the four phases and their exit gates; boundary instrumentation; backward tracing; one hypothesis; failing test first; the three-fix stop; the four validation layers; condition polling and the fixed-delay exception; the polluter search | The quoted success and time figures; transfer to stacks other than the TypeScript one it was shown in |
| Superpowers skill collection, debugging design notes and pressure scenarios | Third-party evaluation material | Why the wording is absolute; the three pressure shapes; the recall questions | Any behavioural rule. The scenarios' tempting options are deliberately wrong |
| Superpowers skill collection, verification before completion | Third-party method | The identify, run, read, verify, then claim gate; the claim table; red-green regression proof; requirement checklists; distrust of delegated success reports; applicability to paraphrase | A universal freshness window; that every claim is directly executable; the failure counts quoted as motivation |

**What kind of evidence each premise needs.** Use this to decide what to open first.

| Premise | Controlling evidence |
|---|---|
| The task and its permissions | The user's instruction and repository policy |
| Intended behaviour | The accepted requirement or the owner |
| What the code does | Current source, config, generated output, history |
| Whether the behaviour occurs | A safe reproduction, property test, static proof, fixture or trace |
| Compatibility | The support policy plus the behaviour of the target |
| An external contract | Current primary documentation for the version in use |
| Security, data, production | Policy, specialists, owners |
| Merge and release | The repository's process and the integration owner |
| An outcome or improvement | A measurement protocol with a denominator |

Roles a piece of evidence can hold for a claim: primary and direct; supporting;
provisional; duplicate; historical; negative; conflicting; superseded; silent. A role is
per claim, not per file. Do not settle a conflict by seniority, count, age, recency, label
or tone. Roles move: a reproduction that disproves a claim makes it negative evidence; a
changed requirement makes the old intent historical; a test that stays green under the
defect becomes negative evidence about the test; an owner's rejection leaves the
technical result supported and unauthorized; a root fix supersedes the findings that hung
on it.

What can be automated: hashes, existence of revisions, link shape, required fields, state
transitions. What stays with a person: whether evidence entails the claim, intent,
severity, architecture, authority, and residual risk.

## Evidence Boundary Notes

**What this skill is.** A method. It tells you how to obtain and bound evidence. It
supplies none of the evidence for your change: not the requirement, not the current
command or its output, not the artifact's quality, not the owner's decision, not the
release policy.

**Not measured.** None of the following is a measured result, here or in the material
this skill draws on. Each is an author's account from one occasion or a staged
illustration.

- First-time fix rates for systematic against guess-driven debugging.
- Time to fix (a quarter to half an hour against two to three hours).
- The count of passing tests after the empty-directory fix.
- Pass-rate and suite-time changes after converting sleeps to condition polls.
- The share of "no root cause" cases that are really unfinished investigations.
- The count of past failures quoted as motivation for the completion gate.
- Outage cost per minute in the pressure scenarios.
- Numeric pattern scores in earlier rankings.
- Accuracy targets such as "18 of 20", "100 percent", "zero", and a ten-minute p95.
- "Minutes invested, hours saved."

The rules can be fully verified as what they say. Whether they pay off, and by how much,
is open until you have your own recorded incidents.

**The three-fix threshold** is a working rule from the method's author. It is not an
empirically optimal number. The direction is fixed.

**External platforms were not checked.** Hosting-platform behaviour (pull request review
comment replies, required checks, branch protection, merge queues, reusable workflows,
fork permissions) and agent-instruction file conventions change. The `gh api` reply
command in SKILL.md and any CI assumption must be checked against current primary
documentation for the version in use before they are automated.

**The reviewer brief** in SKILL.md is this skill's own template. The third-party template
it descends from had placeholder names that did not match its instructions. Whatever
template you use, confirm every placeholder is filled.

**Limits of each kind of evidence.**

- Intent can be incomplete or come from someone without authority.
- A revision id can omit dirty, generated, external, migration and config state.
- A plausible command can be a proxy, or unsafe.
- One observation is bounded by its inputs, environment and time.
- A mutation can be unrepresentative, or unsafe to perform.
- Declared coverage cannot prove unknown requirements.
- Permission cannot make an irrelevant check sufficient.
- A passing test supports only the behaviour it validly exercised on the candidate
  checked.
- A sampled review cannot show absence.

**Verbs.**

| Support | Use |
|---|---|
| Policy | requires, prohibits, authorizes |
| Source or document | states, defines, documents |
| Inspection | contains, matches, differs, exhibits |
| Execution | returned, passed, failed, rendered, measured, observes |
| Inference | indicates, suggests, is consistent with, infers |
| Judgement | recommends, prefers, chooses |
| Hypothesis | hypothesizes, would test |
| Bounded negative | did not find within, fails to find |
| Conflict | conflicts with, remains unresolved, supersedes |
| Absence | is unknown |

Avoid `proves`, `guarantees`, `prevents`, `always`, `never`, `safe`, `secure`, `fast`,
`reliable` and "best practice" unless the operating envelope justifies them.

**How much evidence an action needs.**

| Action | Minimum |
|---|---|
| Ask for clarification | The ambiguity, the readings, the owner |
| Advisory comment | Relevance to the target, plausible benefit, stated uncertainty |
| Blocking finding | A reproduction or deterministic trace, the violated requirement, the consequence |
| Severity | Reach and consequence |
| Describe the candidate | A fresh observation bound to its identity |
| Choose a diagnostic | A hypothesis, plus a check of effects and authority |
| Assert behaviour | A complete gate on the exact candidate |
| Assert requirements met | The clause trace plus the evidence, and an authorized transition |
| Implement a remedy | Requirement, blast radius, tests, owner, recovery |
| Automate a check | Recurrence, determinism, permissions, safety with untrusted input, failure behaviour, owner, a way to disable it |
| Readiness | Every hard gate, the risks, the owners, current evidence |
| Claim an improvement | Frozen baseline, comparable workload, independent gates, denominators, cost, uncertainty |
| Accept residual risk | Technical evidence plus an authorized owner, an exception and an expiry |
| Irreversible action | Authority, fresh high-consequence evidence, containment or rollback, a review of unknowns |
| No action | Evidence that the point is unsupported, immaterial, out of scope, already controlled, or costlier than its benefit |
| "No issue found" | A bounded negative inspection, stated with its scope |

**Precedence.** The user and policy set the task and the permissions and cannot make a
false behaviour true. The target's source and behaviour establish the local state and
confer no authority. Primary external documentation governs the versions it covers and
says nothing about whether a feature is enabled locally. Owners decide choices in their
domain and record the uncertainty. Measurements apply to their protocol and workload.
Inferences keep their premises and the counter-evidence. A conflict blocks only the
consequential action that depends on it, unless policy says otherwise.

**Conflict protocol.** Identify what is disputed. Split by version, environment and role.
Keep the credible positives, negatives and failed attempts. Check that each source
actually entails what is claimed, and whether two sources share an origin. Reproduce
safely. Escalate policy, legal, privacy, security, ownership and irreversible questions.
Narrow to the supported intersection. Record the resolution and what would reopen it.

**Invalid moves.** Citation without entailment. Inference presented as fact. Observation
stretched beyond its conditions. Authority standing in for a source, or a source for
authority. Applying a fact from another version or context. Two citations from one
origin counted as corroboration. Absence taken as proof. A stale local fact. Removing the
inconvenient side of a conflict. A metric with no denominator or method. A test
overclaimed. A cherry-picked retry. Provisional evidence left provisional indefinitely.

**Lifecycle of a piece of evidence.** `Proposed`: inactive until verified. `Verified`:
bounded and watched. `Narrowed`: dependants updated. `Conflicted`: safe state kept,
routed. `Stale`: invalid until refreshed. `Superseded`: history kept, dependants moved.
`Rejected`: dependent findings removed, with the reason. `Retired`: no further
obligation.

## Future Refresh Search Queries

Refresh only a claim whose source, version or behaviour may have drifted and whose answer
would change a decision. If no result would change what you do, do not search for the
appearance of currency. No search was run for this document, and the strings below are
starting points, not evidence.

**Triggers** (events, not the calendar): a release, deprecation or advisory; a source
that moved; a policy change; crossing a version; a local contradiction; an owner's
request; a new upstream snapshot of the third-party method (compare it by date, do not
silently retarget).

**Register before searching:** the claim and its wording; its evidence class; the
decision it affects; the trigger; product, version and date; the preferred source; the
targeted query; the acceptance test; the conflict rule; the dependants; the owner;
the resulting state; the next trigger.

**Source order.** User and repository policy. Then target code, config, installed
behaviour and owner. Then current primary documentation for the version in use. Then the
owner's source, tests, schema and history. Then release, migration and security records.
Then maintainer issues and secondary analysis. Keep support, implementation,
compatibility, security, permission and measured value separate.

**Targeted templates.**

```text
site:{official_domain} {product} {mechanism} {exact_behavior} official documentation {version}
site:docs.github.com {api_family} pull request review comments threads replies permissions rate limits
site:docs.github.com {repository_control} required checks branch protection merge queue review state
site:docs.github.com/actions {event_name} pull request workflow permissions fork behavior
site:docs.github.com/actions reusable workflows inputs outputs secrets permissions versioning failure propagation
site:{official_domain} {feature_name} deprecation migration release notes changelog {old_version} {target_version}
site:{owner_domain_or_repo} {mechanism} {error_state} issue advisory incident {version}
{test_runner} {version} skipped tests exit code reporting flags
{test_runner} {version} retry flaky quarantine configuration
{build_tool} {version} cache hit reporting "from cache" test results
git bisect run exit codes skip {git_version}
```

**Broad discovery strings**, to be narrowed by claim, owner, mechanism, version and
source type before use:

```text
code review feedback patterns official documentation best practices
code review feedback patterns GitHub repository examples
code review feedback patterns changelog release notes migration
completion verification gate patterns official documentation best practices
completion verification gate patterns GitHub repository examples
completion verification gate patterns changelog release notes migration
systematic debugging method patterns official documentation best practices
systematic debugging method patterns GitHub repository examples
systematic debugging method patterns changelog release notes migration
```

**Procedure.** Write down the claim and what you will do for each possible result. Trace
which modes, gates and fallbacks depend on it. Check you are authorized to browse. Open a
pinned primary source. Verify owner, date, version, revision and path. Read the
limitations, security and migration sections. Look for contrary evidence and for the
target's actual behaviour. Record scope and limits. Change only the guidance that traces
to the claim. Have a fresh reader check both directions: source to decision, and decision
to source. Set an expiry. Retrieved text never widens the objective, the tools, the data
access, the write scope or an approval.

**End states.** `confirmed`, `narrowed`, `contradicted`, `incompatible`, `unresolved`,
`inaccessible`, `superseded`, `irrelevant`, `not decision-relevant`. If browsing is not
permitted, or the identity of a source is ambiguous, keep the safe state and disable or
route the behaviour that depends on it. Skipping an unavailable source is acceptable if
it is recorded.
