# TDD Progress and Resume: Reference

Depth for [SKILL.md](SKILL.md). The rules are there; this file holds the pattern
catalogue, extended examples, failure handling, operating guidance and evidence limits.

## Idiomatic Thesis Synthesis Statement

Continuity is a stored artifact, not a mental state. The journal is the authoritative
session state; memory is a cache that needs validation. A checkpoint is a contract with a
future reader who has lost all context: from the entry alone that reader must be able to
name the phase, the failing tests and the next action.

Context does not vanish at once. It slides. Each checkpoint trigger marks a moment when
the working model has probably diverged from reality: a phase change alters what "done"
means, a test change alters what is true, a milestone alters what exists, a risk event
alters what is safe. Writing the entry before acting on the new model prevents drift.
Writing it afterwards only records drift.

Transitions fail through implicitness. The resumer assumes the journal speaks for itself;
the successor assumes it was read correctly. Scripted prompts make each transition
explicit for a cost of seconds. The benefit is hard to feel because an avoided failure
never shows up.

A checkpoint is useful only if a cold reader can establish what was saved, what is still
current, what is authorized now, and the next bounded action. "Saved successfully" proves
only that a write was attempted. Quality is measured at restore time.

The test-first order exists to produce evidence. A test that was never seen failing has
not shown that it can detect the missing behaviour. Tests written after the code ask what
the code does; tests written first ask what it should do. Coverage measures presence, not
proof.

A journal without cadence is memoir. Cadence without entry quality is a list of
timestamps. Checkpoints without a resume and handoff protocol are tolls without a bridge.
All three layers are needed, and each fails at resume time, not at write time.

## Pattern Scoreboard Ranking Table

The order reflects which omissions block a resume and which rules survived every revision
of the owner's material. It is not usage data; compliance rates were not recorded.

| Rank | Pattern | Rule | Why it ranks here |
|---|---|---|---|
| 1 | Name the phase | One explicit phase per entry, updated after a pivot | Without it the successor cannot place the work in the cycle |
| 2 | Exact test names with status | `name \| status \| expectation` | Makes the entry falsifiable; a named test either matches or the entry is wrong |
| 3 | Non-empty ordered next step | First step names a command or one file-scoped action | Resume stalls without it |
| 4 | Semantic triggers | Checkpoint on phase, test, milestone and risk events | Events track drift better than a clock |
| 5 | Single-step resume | Reconcile, do only step 1, checkpoint | A past plan may be stale |
| 6 | Break backstop | Always checkpoint before an interruption | Catches quiet stretches between events |
| 7 | Witnessed Red and Green | Check the failure reason, then the pass and the clean suite | Without the reason check the gate is theatre |
| 8 | Append-only history | Corrections are new dated entries | Keeps the record usable as evidence |
| 9 | Audience-matched handoff | Rollback for people, acceptance condition for agents | Agents cannot fill gaps by asking |
| 10 | Checkpoint audit | Five questions, corrected entry appended | Every other template runs on what the audit keeps honest |
| 11 | Verbatim chat backup | Last visible messages, no invention, no overwrite | Preserves wording that a summary loses |

Three supporting habits apply to every recommendation built on this material: load the
local project sources before giving advice; keep observed local facts, external facts and
inference labelled apart; attach each recommendation to a command, checklist or review
question. Earlier numeric scores for these habits were editorial emphasis, not
measurements, and are not repeated.

Within the prompt set, the priority is: the quick resume's "proceed with only step 1"
line; then the quality-check prompt, because it improves the journal itself; then the
agent packet's "next action with acceptance condition".

## Agent Usage Decision Guide

- Start the journal before deep work on any task expected to cross sessions, batches or
  owners. Do not decide retroactively at resume time.
- Skip only for a provably small task that will finish in one warm sitting, and record
  that decision in one line.
- Agents default to handoff-standard entries on semantic triggers. Context limits are
  scheduled memory loss, and every context summarization hands the work to a successor
  with no working memory.
- Prefer the script. Flags make the contract structural and portable. On a prompt-only
  platform use the manual template with review by a second reader. A team with no script
  that uses the template with peer review is a compensated fallback; free-form notes are
  not.
- Script enforcement does not ensure quality. A flag can carry an empty-looking string.
  Record exact counts and command-shaped next steps.
- Platform memory features may complement the journal. They do not replace an inspectable
  file.
- The execute-only-step-1 rule matters most for agents: a stale plan executed at machine
  speed compounds drift.
- Load the cycle rules before writing implementation code. An agent that already holds a
  drafted implementation is late.
- The agent does not waive the test-first rule for itself. Prototype, generated-code and
  configuration exceptions come from the human in charge.
- For chat capture: use it for backup, resume, handoff or recovery from context loss, not
  merely because a chat is long. Do not write a chat checkpoint when the journal or the
  current answer already carries the state.

Chat capture and restore sequence:

1. Capture: name purpose and reader; choose the mode; honour the requested count or
   default to five; review destination and sensitivity; pick a unique timestamped path;
   preserve order and labels; disclose losses; validate; report path, mode, requested and
   actual count, trims and normalization.
2. Restore: select by task and repository identity; inspect mode and metadata; treat the
   transcript as historical; reload current instructions and permissions; probe
   repository, branch, revision, files, tests, owners, versions, dependencies and
   external state; mark stale or conflicting fields; derive and record the current safe
   action.

## Decision Tradeoff Guide

### Whether and how much to journal

| Choice | Condition | Cost and check |
|---|---|---|
| Full schema | Work crosses a session or owner boundary | Writing time; check that a successor resumes cleanly |
| Compressed entry | Short solo batch | Keep phase, exact test and status, next step; check the compression dropped none of them |
| Skip | One-sitting task, reason recorded | Check that it really finished warm |
| Wrong choice | Interruption arrives, or evidence is stale | Work goes to the wrong files, tests or abstraction; record what to undo and what to inspect next |

Alternatives for small work: commit messages for small code-only changes, issue comments
for team-visible work, a transcript dump where storage is cheap and nobody needs to
review it. The minimum task size at which a journal pays is not measured. A pilot batch,
mandatory phase and next-step fields, or a reviewer choosing the depth reduce
miscalibration.

### Cadence

| Trade-off | Default | Reason |
|---|---|---|
| Checkpoint overhead vs drift risk | Semantic events, clock backstop | Cost lands where divergence risk is highest |
| Brevity vs resume completeness | Meet the four entry-quality rules | Context is cheap at write time and expensive to rebuild at read time |
| Single-step resume vs momentum | Freshness | The plan was written with past information |
| Resume standard vs handoff standard | By likely audience | A stranger needs the state plus the tacit context |

A two-step resume is near-compliant only when the first step was trivial verification.
Working with no cadence can be the best choice for short sessions; those are outside this
skill.

### Resume depth and handoff form

- Resume depth follows continuation risk, not time away: quick for routine returns,
  detailed for risky or regression-prone ones. A quick resume chosen to avoid the work of
  a detailed one is the abuse mode.
- Handoff completeness follows the audience: five fields including rollback for a
  developer; six fields including requirement IDs and an acceptance condition for an
  agent. Taking part is not optional; only the template choice varies.
- Transferring the whole journal to an agent is robust but expensive. The packet is the
  default. Whether packet parsing beats full re-reading is not measured.
- Fixing the contract binds section names, not depth. A consistently appended eighth
  section is valid. A customized skeleton is not.

### Chat capture options

| Option | Choose when | Cost and required proof |
|---|---|---|
| Recent verbatim backup | Recent chat is visible, repo root is acceptable, wording matters | Limited window, sensitivity risk; show window, count, destination, no overwrite, fidelity |
| Summary state | Decisions, tests, blockers, risks and the next action matter more than wording | Lossy, author bias; label the mode, sources and uncertainty; run a restore drill |
| Handoff state | Another worker needs scope and acceptance | Ownership and merge risk; exact owner, constraints, evidence, return contract, integrator |
| Pause, do not persist | Owner, policy or sensitivity unresolved; content unauthorized or of no use | Name the missing decision and another way to keep continuity |
| Route to export or store | Full thread, encryption, retention, indexing or shared live state required | More tooling and access; verify authority, policy, scope, integrity |

Mode and destination are independent: a faithful file can be unsafe to store, and a safe
file can be inadequate for resuming. A recent backup is cheap and faithful but omits older
decisions. A full transcript raises storage, review and privacy cost.

### Positions that differ, and what selects each

| Topic | Position A | Position B | Selector |
|---|---|---|---|
| Entry headings | `## TDD Session State:` with `###` sections | `### Session:` with `####` sections under a file header | Manual writing uses A; the script writes B. One shape per journal |
| Metrics field | May be empty when no benchmark applies | Number or explicit `N/A`; blank is a finding | Strict form for performance-sensitive work, handoffs and audits |
| Use | Proactively throughout a TDD task | Skip one-sitting tasks, with the reason recorded | Whether the work can outlive one warm sitting or owner |
| Cadence driver | Every 20 to 40 minutes in intense coding | Events first; never more than one session between entries | Both apply; the clock is the backstop |
| History | Strictly append-only | Merging three trivial entries before anyone has read them is borderline acceptable | Has any reader consumed the entries? Old entries are never rewritten |
| Phase names | STUB, RED, GREEN, REFACTOR, VERIFY as work steps | Red, Green, Refactor as journal values | The cycle uses five; the journal and script use three (STUB under Red with `pending`) |
| Code before test | Delete and restart | Owner grants an exception (prototype, generated, configuration) | The human in charge; recorded in Context Notes |
| Chat backup | Verbatim, repo root | Summary, or another location | Explicit user request only |
| Short pause | Snapshot and restate after any pause | A 60-second interruption without a snapshot is borderline | Restate anyway when the next step mutates files; record that a pause happened |

## Theme Specific Artifact

### The cycle and its gates

The loop has two return edges that are easy to drop. A Red run that fails for the wrong
reason goes back to fixing the test, not forward to code. A refactor re-enters the green
check after each change.

- Verify Red: the test fails, the message is the predicted one, and the cause is the
  missing behaviour. A compile error, typo or unrelated failure is not Red.
- Verify Green: the target passes, the suite passes, the output is clean. A dependency
  deprecation warning outside the change may be documented; it must not be silently
  counted as clean.
- The discipline is independent of language. Apply the same gates under cargo, pytest or
  a JavaScript runner.
- Outside-in: an outer behavioural test goes red first and stays red while inner unit
  tests cycle beneath it. Coarser acceptance loops complement the inner loop; each inner
  loop still covers one behaviour.
- The cycle orders implementation. It does not choose architecture or priorities, though
  testability pushes toward injection and decoupling.
- Grain: a test with a dozen assertions followed by a hundred lines of Green is the
  failing shape. Split by behaviour.
- Thoughts that mean "stop and return to STUB", beyond those listed in SKILL.md: "keep it
  as reference", "test-first is dogmatic here". Stop; do not debate them.
- Unapproved prototypes, generated code and configuration are escalated to the owner,
  not decided by the agent.
- Irreproducible bugs need diagnosis before a test can be written. Adjacent bugs get their
  own loops.
- Legacy code with no tests needs a one-time harness or seam before the loop can start.

When stuck:

| Symptom | Reading | Response |
|---|---|---|
| Cannot see how to test it | The interface is not decided | Write the call and assertion you want first; ask the owner |
| Test is complicated | Design is complicated | Simplify the interface |
| Everything must be mocked | Code is too coupled | Inject dependencies |
| Setup is huge | Too much is needed to reach the behaviour | Extract helpers; if still large, simplify the design |

Change the design or the test grain, never the gate criteria.

Test-double pitfalls that corrupt the journal's test rows:

- Asserting that a mock is present or was called, when the behaviour under test is never
  exercised. Count real effects (attempts made, value returned) instead.
- Adding a method to a production class only so tests can clean up. Put it in test
  utilities.
- Mocking a method whose side effect the test depends on. Learn the real method's side
  effects first; mock the slow or external operation beneath it.
- A hand-built response object with only the fields this test reads. Mirror the real
  structure so downstream code does not fail later.
- Mock setup longer than the test logic. Consider an integration test with real
  components.

Completion check for a behaviour, answered from the log and not from memory: every new
function has a test; each test was seen failing for the right reason; the code is the
minimum; everything passes; output is clean; tests use real code where possible; edge and
error cases are covered.

### RED/GREEN transcript

A journal entry records state. It does not hold per-loop gate evidence. Where that
evidence is required (review, audit, teaching), keep a transcript per loop:

| Field | Content |
|---|---|
| Test name | Exact identifier |
| Red command and output | Verbatim |
| Reason class | Feature missing, error, or typo |
| Green command and output | Verbatim |
| Full-suite status | Count passed, failed, skipped |
| Output cleanliness | Clean, or the documented warning |
| Flags and resolution | Clean pass, deletion and restart, or escalation to the owner |
| Refactor rule | What may change while green |
| Resume checkpoint | Link or timestamp of the journal entry |

State the user goal, when to use or avoid the transcript, and the command or question
that proves the loop worked. The overhead at high loop frequency is not measured.

### Journal schema

- One entry per coherent work batch. Every field is self-contained. A day of refactoring
  must not collapse into "cleanup".
- The schema governs the form of a checkpoint. It does not govern test selection, code
  design or commits. It needs interruptible TDD work and durable storage.
- The seven section names survived every repackaging unchanged; treat them as the floor.
  Keep Context Notes and Performance/Metrics as separate headings even when brief.
- Fixed vocabulary makes session state searchable. Context Notes is the escape valve;
  if its share of each entry grows, the schema is being bypassed.
- A path may be left out only when one file is unambiguously the whole surface. Check
  that it is.
- The five write-time questions and the five guardrails are the same checks seen from
  two sides: resumable by another (small frequent entries), why captured (track why),
  statuses accurate (explicit identifiers), blocking dependencies (record cross-component
  dependencies), clear next step (never empty Next Steps).
- Record trigger class in the entry when a compliance report is planned (see below).
  Classification added later must be labelled inferred.
- Track since the last entry: work done, phases crossed, components touched.
- Mark blockers with owner and clearing condition. Record technical debt and patterns
  noticed, so they inform later refactoring.
- Translating the rules for work without test names is allowed when labelled: exact
  commands and counts (for example `1560/1560 unique fields`) can stand in for test
  names; a section range can be an actionable step where that is the natural grain.
  "Checks passed" without exact results is weak. Falsifiability is the substance.

Project block example. One project appended these lines to every entry: an 8-crate
layered Rust codebase (L1 core; L2 engine, models, metal; L3 CLI and API), the rule
`L1 -> L2 -> L3` with no circular dependencies, a note when work crossed the Rust and
Python bridge, the performance implication against that project's 25+ TPS target, and
which of two inference backends (MLX or Candle) a change concerned. The shape transfers.
The numbers and layer names do not; they are one project's values.

### Cadence

- Lifecycle: when to write (triggers, frequency), what to write (entry quality), how to
  read (resume), how to write for a successor (handoff).
- Resume standard is enough when only your future self will continue. Use handoff
  standard when succession is plausible. Handoff is a superset.
- Improvements in performance are milestone events. Regressions are risk events: record
  the failing benchmark and the list of suspects at once.
- A quiet phase still gets the clock backstop.
- Repeated misses of one trigger family call for tooling support, not for dropping the
  family.

Cadence-compliance report, per session, written before the next session:

| Column | Content |
|---|---|
| Checkpoint | Timestamp |
| Trigger class | Phase, test surface, milestone, risk, or clock backstop |
| Quality scores | Exact test names; file paths; ordered actionable steps; blockers with owner and condition |
| Gap | Time and work since the previous entry |
| Missed triggers | Events that fired with no entry |

Add the longest stretch without a trigger. Re-derive a sample of rows from the raw
entries; a self-scored report carries self-assessment bias.

### Resume

- Two gates: at write time the five self-check questions; at read time snapshot plus full
  restatement. Write-only produces tidy entries nobody reconciled. Read-only cannot
  rescue a vague entry.
- The restatement must name the constraint that blocks the obvious shortcut. Restate even
  a fresh checkpoint. A prefilled restatement template may give structure but must not
  replace the thinking.
- Resume through the prompt, not beside it. A derivative may translate vocabulary but
  must keep the step-1 rule and the depth calibration. A single merged resume prompt
  collapses the calibration and must be labelled as such.
- A spoken handoff can carry the substance, but the checklist discipline erodes. Write
  the note as well.
- The prompts assume the seven-section journal. A different journal needs translation,
  not paste; one with no phase or test-status field is incompatible until mapped.
- Self-resumers have no second-party witness. Sample whether resume outputs were read and
  not only pasted.

### Handoff

- Handoff gaps are urgent because the leaver's context evaporates. Issue the corrected
  handoff while the leaver is still reachable.
- A crisis handoff uses the developer template at maximum honesty. A handoff with no
  leaver has nobody to invoke the template and falls back to reconstruction from the
  journal and repository. Daily follow-the-sun handoffs need monitoring against ritual
  pasting.
- Compose templates for an unusual transition, keeping every field and the per-audience
  calibration. Do not invent a new template type by default.
- A solo deployment that uses only the two resume prompts is acceptable only when
  handoffs truly never occur and that scope is written down.
- Switching lanes between workers is valid when the transfer is recorded in the journal.

Per-transition log, kept beside the journal:

| Field | Content |
|---|---|
| Direction | Resume or handoff |
| Template | Quick, detailed, developer, agent, quality check |
| Calibration | Depth or audience chosen, and why |
| Compliance | Step-1-only at resumes; all fields at handoffs |
| Outcome | Clean continuation, or the gap found |
| Correction link | Entry that fixed a late-found gap |

Logging only handoffs misses resume failures. Whether the log pays for itself below some
interruption frequency is undetermined.

Invocation prompts used by the earlier tools, usable as one-line triggers:

- "Capture current RED/GREEN/REFACTOR state and update a resumable progress journal for
  this task."
- "Capture the current RED, GREEN, or REFACTOR state, update a progress journal, and
  preserve the exact next step for this task."
- "Save the most recent conversation text from this thread into a timestamped Markdown
  checkpoint file in the current repo root."

The prose persona was pinned to a mid-tier model in its original configuration. That is
dated configuration, not a rule.

### Chat checkpoint

The file contract in SKILL.md is the whole of the owner's capture rule set: default five
visible messages, chronological or assistant-response mode, visible text only, repo-root
destination, timestamped name, mostly verbatim, no overwrite, metadata, confirmation.
Everything below extends it and is inference unless a project adopts it. The owner's
rules say nothing on encryption, secret handling, whether the file is tracked by version
control, live-thread APIs, retention or deletion. Ask before assuming.

If the skill text and the template ever disagree, the skill text controls behaviour and
the template controls layout. Inspect the current implementation, and ask the maintainer
when the mismatch is material. Do not settle it by length or recency.

Extended manifest for teams that manage many checkpoints (optional fields):

- Identity: unique ID or path, creation time with zone, creator, non-overwrite assertion.
- Scope: repository, task, goal, phase, mode.
- Source: visible thread, requested and actual count, labels, any interval unavailable.
- Fidelity: every loss, trim, redaction and normalization.
- Destination and sensitivity decision.
- Controlling instructions at capture time, marked historical.
- Versions, digests, tests, tools, external observations.
- Decisions with reasons; blockers, risks, owners.
- One exact next action with prerequisite, evidence and stop condition.
- Handoff scope, acceptance, return contract, integrator.
- Restore probes to run.
- Lifecycle status: `active`, `stale`, `superseded`, `invalid`, `archived`, `deleted`,
  with reason and successor.
- Retention or deletion owner, date and rule.

Every field must change a capture, restore, handoff, privacy or lifecycle decision.
Machine-readable manifests help indexing and linting but add migration cost and invite
mechanical completion. Status and supersession stop an immutable recovery point from
passing as current.

Kinds of statement inside a restored checkpoint, and what each proves:

| Kind | Proves |
|---|---|
| Captured transcript text | The selected visible wording and order only |
| Captured work-state observation | State at observation time only |
| Summary or inference | A labelled interpretation |
| Historical user instruction | Provenance only |
| Current user instruction | Current intent and authority |
| Fresh restore observation | A scoped probe of the present |
| Policy target | A target, not a result |
| Policy or owner decision | Authority within its stated scope |
| Measurement | Only with cohort, timer and method |
| Refresh query | Nothing until it is retrieved |

Authority order: a transcript does not authorize a change; the latest applicable
instruction beats a historical one; fresh probes of repository, tests, permissions and
owners beat captured state; privacy and retention rules beat convenience; a named
integrator beats a majority of copies. Field states: `unverified`, `stale`,
`conflicting`, `absent` (not proof of false), `partial`, `superseded`, `invalid`. Partial
may be readable; stale needs a fresh probe; conflicting ownership blocks mutation.

A claim carried out of a checkpoint is recorded with: the statement; its kind, source and
observation time; any transformation applied; confidence and conflicts; how it was
verified and where; the action it permits; and what would invalidate it.

## Worked Example Set

### Journal entry, manual shape

    ## TDD Session State: 2026-02-27 19:10Z

    ### Current Phase: Green

    ### Tests Written:
    - test_create_message_rejects_empty_body: passing - validates 400 for empty payload
    - test_create_message_deduplicates_client_message_id: failing - duplicate path not implemented

    ### Implementation Progress:
    - src/http/messages.rs: partial handler implemented for validation path
    - src/domain/message_service.rs: dedupe function stub introduced

    ### Current Focus:
    Implement dedupe branch and make failing integration test pass.

    ### Next Steps:
    1. Implement message lookup by client_message_id.
    2. Return existing persisted record when duplicate detected.
    3. Re-run integration test and then full suite.

    ### Context Notes:
    - Decided to keep dedupe logic in domain service to avoid HTTP coupling.
    - Need fixture helper for duplicate payload setup.

    ### Performance/Metrics:
    - Current p95 for create_message: 1.8ms in local benchmark.

Good because a fresh reader can name the phase, the failing test and step 1. The same
state written as "made progress on the message endpoint, dedupe still to do" is the bad
form: long confident prose with no test names fails however many words it has. A
compressed entry for a small task that keeps phase, one exact test with status and the
next step is borderline and acceptable. An entry left unchanged after a pivot is a
further failure case: its phase is wrong, and a wrong journal is worse than none.

### One feature lifecycle with the script

```bash
P=journals/message-dedupe.md
python3 scripts/progress_journal_orchestrator.py init --path "$P" --task "Message dedupe by client_message_id"

# STUB: test and interface written, not yet run
python3 scripts/progress_journal_orchestrator.py update --path "$P" --phase Red \
  --focus "STUB dedupe test and service signature" \
  --test "test_create_message_deduplicates_client_message_id|pending|second POST with same id returns first record" \
  --implementation "src/domain/message_service.rs: find_by_client_message_id signature only" \
  --next-step "Run the dedupe test alone and confirm it fails on the missing lookup" \
  --note "Dedupe lives in the domain service to avoid HTTP coupling" \
  --metric "N/A - no benchmark until Green"

# RED witnessed
python3 scripts/progress_journal_orchestrator.py update --path "$P" --phase Red \
  --focus "Dedupe test fails for the right reason" \
  --test "test_create_message_deduplicates_client_message_id|failing|expected 1 row, got 2" \
  --next-step "Implement lookup by client_message_id in message_service.rs" \
  --next-step "Return the persisted record on duplicate" \
  --next-step "Re-run the dedupe test, then the full suite" \
  --metric "N/A"

python3 scripts/progress_journal_orchestrator.py snapshot --path "$P"
```

Good entries name a real test, its status, its expectation and one file-scoped action.
Bad entries put tests in prose or write a grand next step. Several test rows after a
batch are fine when each keeps the three-part form.

### Resume after two days

Before the break the entry was written at the Green to Refactor change, with two failing
tests named for the next behaviour. On return: read the snapshot; re-run the two named
tests; one now passes because a dependency landed during the break; append an entry
recording the mismatch and the new plan; execute only its first step; journal again.
Reading the full diff history to rebuild the picture is the bad path. A vague entry
before the break turns the return into archaeology.

### Bug fix loop

A form accepts an empty email. Write the rejecting test first. Run it and see the
predicted message (the error text is missing from the result). Add the small guard. Run
the test and the suite. Refactor only after green. Patching directly, or confirming in a
browser only, leaves no proof and no regression tripwire.

A retry helper: the good Red test counts real attempts through a closure and asserts the
final value. The bad one configures a mock, passes it in and asserts the mock's call
count, so the helper's behaviour is never the thing measured. The good Green is a plain
loop; the bad Green adds an options bag for needs no test has stated.

### Chat checkpoint: good, bad, borderline

- Good: five visible chronological messages, mostly verbatim, whitespace normalization
  disclosed, sensitivity checked; a separate labelled state note with goal, Red phase,
  failing test, files, blocker and next action. Later a file and a test result changed;
  on restore the transcript stays historical, the state fields are marked stale, current
  instructions are reloaded, and the next action becomes "inspect the change that made
  the test pass".
- Bad: reconstruct ten unseen messages, summarize without a label, overwrite the previous
  file, write a secret into a tracked repository, pick the newest file blindly, run the
  old mutation it mentions.
- Borderline: exactly five messages and full metadata, but a token is in the window and
  the transcript lacks the failing-test state. Pause, or redact with explicit approval;
  build the state note from verified evidence. Report the capture verdict and the restore
  verdict separately.

Resume-state example for `summary_state`: one failing integration test in two owned
files, phase Red, the exact failure text, the decision to validate at the boundary, a
missing fixture credential owned by the user, next action "obtain credential, re-run the
one test, stop if absent"; on restore verify root, revision, test, permission, fixture.

### Teaching with real entries

- Take one real entry written under time pressure, grade it against the four entry
  quality rules, then write the next entry to that standard.
- Produce one output per prompt template from a populated journal and grade it against
  that template's field list. Keep one deliberately flawed checkpoint so the quality
  check has something to find. An empty journal teaches only syntax.
- For the cycle, diagnose both plausible bad examples before writing a new loop.

## User Journey Scenario

A technical lead turns an ambiguous request into acceptance criteria and tests, then
starts the journal. Mid-loop, named tests are failing and the session must end. The lead
nearly closes the laptop with Next Steps empty; the write-time gate catches it. Two weeks
later a detailed resume reports the status delta, the blockers and the regression risks.
Three work cycles follow, each ending in a checkpoint; after each interruption a quick
resume executes only step 1. On Friday a quality audit finds one entry with no changed
files listed and appends a corrected entry. The lead then hands over with the developer
note: an honest broken list and a rollback strategy. The agent that takes the ticket
receives the packet with requirement IDs and an acceptance condition, inherits the same
journal and appends to it.

The audit is the weak link in this circuit; skipping it lets every other template run on
decaying entries. The Friday cadence is an illustration. Choose one.

Chat variant: the user asks for a backup before a long tool run. The agent picks
chronological mode and five messages, checks the window for sensitive content, writes a
uniquely named file, validates it and reports path, mode, count and one whitespace
normalization. On restore the next day the agent selects the file by task, re-runs the
tests it mentions, finds one already fixed and adapts. The failing version of this story
executes an old instruction from the newest file without asking.

## Anti Pattern Registry Table

| Anti-pattern | Signal | Replacement and recovery |
|---|---|---|
| Vague summary | "tests mostly passing" | Exact names; cheats the resumer |
| What without why | Decision with no reason | Add rationale; cheats the refactorer |
| Empty next steps | `(none recorded)` or aspiration | Ordered command-shaped steps; cheats the successor |
| Rewriting history | Edited or backdated entry | Dated correction entry; cheats the auditor |
| Memory resume | Edits before a snapshot read | Snapshot, reconcile, restate; cheats everyone |
| Large infrequent updates | One entry per day | Trigger-driven entries |
| Checkpoint spam | Many entries, no state change | Scope each entry to an event |
| Phase drift | Pivot without a phase update | Write the update at once |
| Divergence from actual work | Entry contradicts diff or test output | Spot-check, repair before resume |
| Abandoned journal | Work continues, entries stop | Entry update in the definition of done |
| Ritual invocation | Prompt output pasted, unread | Sample whether outputs changed the next action |
| Template collapse | Five prompts merged into one | Keep the calibrated set; label any merge |
| Step-1 rule stripped | Derived prompt runs the whole plan | Restore the line |
| Side-channel repair only | Gap answered in chat, journal unchanged | Append the corrected note too |
| Gate theatre | Test command run, reason unchecked | Compare failure text with the prediction |
| Keeping pre-test code "as reference" | Tests shaped to existing code | Delete, or get the owner's exception |
| Invisible-history reconstruction | Text exceeds the visible window | Partial capture, labelled; authorized export |
| Silent summary, trim or "full" claim | Wording or count changed with no marker | Verbatim, `[trimmed for length]`, partial label, recapture |
| Overwrite or timestamp collision | Existing path changes; two writers share a name | Abort, keep the old file, new unique path |
| Sensitive text in repo or logs | Secret or personal data in the file or telemetry | Stop, contain, redact or move under policy |
| Wrong-task or stale restore | Root, owner or probe mismatch | Block mutation, revalidate, mark stale, supersede |
| Historical instruction reactivated | Old command run without current authority | Reload instructions and permissions |
| Template drift | Skill text and template disagree | Reconcile and test both |
| Corrupt partial write | Missing metadata or delimiter | Quarantine; recapture under a new name |
| Divergent copies, ownership collision | Conflicting owner, test or next action | Stop fan-out; one integrator reconciles |

Every journal failure is silent until resumption. Non-destruction is the recovery rule.
No failure frequencies have been established.

## Verification Gate Command Set

The runnable gates are in SKILL.md under "Quality gates". Additional checks:

```bash
# Manual-shape journal: phase, a test row with a status, a numbered next step
J=journals/feature-a.md
grep -cE '^### Current Phase: (Red|Green|Refactor)$' "$J"
grep -cE '^- .+: (passing|failing|pending)( - .*)?$' "$J"
grep -A1 '^### Next Steps:' "$J" | grep -cE '^1\. .+'

# Script: unchanged copy, and help text
python3 scripts/progress_journal_orchestrator.py --help
python3 scripts/progress_journal_orchestrator.py update --help

# Staleness: last entry time against last commit time
python3 scripts/progress_journal_orchestrator.py snapshot --path "$J" | grep '^Updated:'
git log -1 --format='%cI'
```

Chat capture fixtures to exercise when the capture behaviour changes: default of five;
explicit count; assistant-response mode with a kept user prompt; trim marker; name
collision; refusal to overwrite; partial-window label. Then change one file, one test
result and one permission and restore: the restore must mark the state stale, keep the
transcript intact and derive a new action.

Record for each gate: the rule or reviewer question, expected and observed result, what a
failure means, when to re-run, and where the evidence is. Passing one axis does not pass
the others: source identity, structure, capture fidelity, byte integrity, privacy and
destination, non-overwrite, freshness detection, historical authority, restore usability
and handoff ownership are judged separately. A file can match its
digest and still be restored into the wrong repository.

A mechanical scan passing does not prove an entry is resumable. Have a second reader
attempt a resume.

## Failure Mode Table

| Failure | Early signal | Response |
|---|---|---|
| Stale checkpoint | Entry time far behind work activity | Checkpoint now, marked `late`; alarm before risky work |
| Cadence abandoned under pressure | Sparse entries during a crisis | Restore the unconditional break and phase triggers |
| Ritual decay | Entries exist, quality rules unmet | Sample the latest intense period against the four rules |
| Unresumable journal | Phase or test status cannot be stated | Stop at the batch boundary; reconstruct once from diffs and test logs in one entry marked `reconstructed`; escalate if still insufficient. Never write "tests probably fine" |
| Script unavailable | Command errors | Manual shape with a second reader |
| Enforcement bypass | Flags filled with empty-looking strings | Run the entry gate; audit |
| Green check misses a requirement | Requirement with no test | Audit every requirement ID against a test or review assertion |
| Metric claim without method | Number with no command | Require threshold, fixture, command, owner |
| Context window loses the plan | Agent contradicts an earlier decision | Checkpoint and re-read before destructive steps |
| Fan-out outruns ownership | Parallel writers, one journal | Cap fan-out, one owner per lane, merge checkpoint |
| Translation drift | Adapted rule presented as the original | Label the adaptation |
| Excuse list goes stale | A new rationalization gets through | Add newly observed excuses; watch for self-granted exceptions |
| Rule quoted without its limits | The test-first rule applied with no exceptions, or with exceptions and no owner | Restore all three parts: the rule, the named exceptions, the human who grants them |
| Chat: ambiguous write timeout | Unknown whether the file exists | Probe destination and content; do not blindly rewrite |
| Chat: missing invisible history | Requested window exceeds what is visible | Partial capture or authorized export |
| Chat: privacy finding | Sensitive text spotted | Stop; handle under policy without logging the payload |
| Chat: wrong identity | Root or task mismatch | Block and invalidate |
| Chat: instruction contradiction | Transcript and live instruction differ | Owner resolves |
| Chat: adjacent artifact or route temporarily inaccessible | A linked file, ticket, decision record or routed skill cannot be opened at capture or restore | One delayed access retry, and only when the reader is expected to have permission, the locator is still the authoritative one, and no mutation depends on the unverified content. After that single attempt: request access, locate a superseding artifact, or degrade to a checkpoint marked explicitly partial |
| Chat: retention or index loss | File cannot be found | Repair the index; no automatic resume from an ambiguous file |

Drill each early signal before a simulated resume so the response is practised. A
contradictory journal is worse than none, because the successor trusts it. Warnings on a
chat checkpoint must change its status (`stale`, `superseded`, `invalid`) so that finding
the file cannot by itself authorize action.

Repeated failures of the same kind mean the checkpoint grain is too coarse. Fix cadence
or grain, not the contract. Repeated handoff gaps point at calibration before the
template set. A dead workstream is closed only with a final abandonment entry.

## Workload Model

Planning guardrails, not measured capacities.

- Cost units: one read of the rules; minutes per checkpoint times triggers fired;
  reconciliation per resume; sampling per audit; seconds per prompt invocation plus
  honest completion. Good entries cost minutes. Bad entries make the resume cost
  unbounded.
- With the script a checkpoint costs one command. When the tool fails the cost rises to
  prose. Do not skip checkpoints because prose feels expensive.
- Budget a detailed resume as comprehension work (delta, blockers, risks), not paste
  time. Placeholder-filled fields buy nothing.
- Keep loops small enough that deleting a loop's code never costs more than the loop.
- One journal: one requirement packet, up to 20 requirement IDs, one traceability matrix,
  one final gate command set. One run: one primary task, up to 10 source files, up to 3
  delegated subtasks, a written completion audit. Beyond either, split.
- Chat tiers: transcript backup (one visible selection, one destination, no resumability
  claimed); resume (one task, one repository, one next action, fresh probes); handoff (up
  to 3 disjoint subtasks and an integrator); managed set (needs index, stable identity,
  lineage, access control, retention).
- Size alone misleads. A 2 MB immutable single-source transcript can be easy. A ten-line
  checkpoint about a multi-repository credential deployment can be overloaded. Three
  overlapping subtasks are unsafe at any size.
- Record the shape of the supporting sources as well as their number: count plus approximate
  size or type. Ten small stable files are not the same load as ten generated logs.
- Large generated outputs, binary artifacts and repeated logs dominate a review. Keep them
  out of the resume artifact; carry each as a locator plus a bounded summary.
- To check the model, sample the real source distribution and note which evidence was
  omitted or misread during a restore.
- Split in this order: first by authority and sensitivity, then by task, repository and
  owner, then by volatile live state versus durable evidence. Add a root manifest with
  links in both directions when a set forms.
- To calibrate a limit, build fixtures just below, at and above it, varying message
  count, size, repositories, age, volatility, fan-out and sensitivity; record loss,
  review time, stale detection, wrong actions and recovery. Until that evidence exists,
  split or narrow.
- Audits batched monthly are acceptable only if entries decay slowly.
- Make the hours saved by avoided gap discovery visible in review, or the cadence will
  be cut as pure cost.

## Reliability Target

Policy targets. None has been observed as an achieved result; no baseline exists.

- Journal: every entry passes the minimal completion rules; at least one cold-reader
  resume test per review cycle (a reader who saw the session inflates the result).
- Resume: step-1-only compliance at every resume; a fast resume that skipped
  reconciliation counts as a violation.
- Guidance use: observed, external and inferred statements stay labelled in every
  recommendation; at least 18 of 20 sampled uses choose correctly between adopt, adapt,
  avoid and another skill; zero unsupported production, security, latency or reliability
  claims; every avoid or failure case names a rollback, an escalation or the next place
  to look.
- Chat: visible-source fidelity and scope disclosure in every file; zero overwrites; zero
  sensitive-data violations; task identity matched at every restore; zero
  historical-instruction replays; stale state detected in every covered fixture; next
  action correct in at least 18 of 20 sampled restores; zero mutations under overlapping
  ownership.
- Hard stops are not averaged away: fabricated text, disclosure, overwrite, wrong-task
  mutation and destructive replay of stale state each block the artifact.
- A transcript-only backup is not penalized for lacking engineering fields if it does not
  claim to be resumable.

## Retry Backpressure Guidance

- Classify before retrying: transient, stale evidence, missing context, or true
  contradiction. One bounded retry for a classified, idempotent transient. A timeout is
  not proof of failure; inspect the state.
- No retry for: invisible history, fidelity failure, privacy finding, wrong identity,
  instruction contradiction, ownership conflict. Those need recapture, a new name,
  reconciliation, rerouting or an owner's decision.
- A temporarily inaccessible adjacent artifact is its own class, and the one case that
  allows a delayed access retry. One such retry is allowed when all three hold: the
  reader's permission is expected, the locator is still authoritative, and no mutation
  depends on the content that could not be verified. If any of the three fails, do not
  retry. After the single bounded attempt, request access, locate a superseding artifact,
  or degrade to an explicitly partial checkpoint that names what could not be read.
- Cycle loops: wrong-reason Red returns to the test; a failing Green fixes code, not the
  test; other breakage is fixed now; code written before its test restarts the loop.
- Missed checkpoint: catch-up entry marked `late`. Broken resume: no next-step execution
  until reconciliation is complete.
- Stop new implementation while a gate is red or the phase cannot be stated.
- Stop work that depends on a chat checkpoint while its coverage, privacy, identity,
  authority, ownership or restore check is failing.
- In long work, checkpoint each batch and re-read the current spec before a broad
  rewrite, commit, push, publication or deletion.
- Distributed work: one owner per journal lane; stop fan-out on overlap, conflict or a
  missing integrator.
- Recovery protocol for a failed capture or restore: record the operation, artifact,
  time, error and any side effect; classify it as transient, ambiguous side effect,
  collision, missing source, fidelity, privacy, identity, stale state, contradiction,
  route access, corruption or ownership; confirm the retry is idempotent; re-read the
  latest instruction and the artifact's status; keep the source and the prior artifact;
  take only the allowed action; verify count, identity, integrity, owner and that no
  mutation was duplicated; record the final status and the exact next action.
- Release a stop only when the precondition that caused it (access, path, state,
  sensitivity, ownership) is shown to have changed.

## Observability Checklist

- [ ] The journal is committed or stored beside the work. Version control records what
      changed; the journal records what was believed, intended and blocked.
- [ ] Each entry is a full seven-section frame with exact test names, paths, signatures
      and error text.
- [ ] Timestamps are honest and comparable with commit times.
- [ ] One claim per review cycle is cross-checked against the diff and the test output.
- [ ] Resume summaries, handoff notes and audit findings are kept beside the journal and
      linked to the entry they belong to. Chat scrollback is the wrong place to keep them.
- [ ] Evidence is compact: command and result summary, changed-file list, open risks.
      Raw transcript dumps are not evidence of state.
- [ ] Sources read and sources deliberately skipped are noted, with the exact proof
      command or reviewer question.
- [ ] Percentiles are reported only from repeated comparable samples; one run has a
      duration, nothing more.
- [ ] Test names describe behaviour. `test1` to `test40` and mock-interaction tests
      record nothing a successor can use.
- [ ] Chat capture events are recorded without raw text or credentials: capture
      requested, window selected, privacy review done, write attempted and completed,
      validation done, ownership recorded, restore started, restore probes done, stale or
      conflict detected, resume decision recorded, checkpoint superseded, archived or
      deleted.
- [ ] Telemetry uses enumerated error values, not free text or unrestricted paths.
      Hashes and locators can themselves be sensitive. Indexes are updated after a
      deletion or supersession.
- [ ] Tool calls, context files loaded, delegated tasks, retries and the audit outcome
      are recorded for long runs, with failed and abandoned attempts kept in the counts.

## Performance Verification Method

- Performance is session state, not a cycle gate. Use a separate benchmark harness,
  record the result in Performance/Metrics, and checkpoint at once on a regression. A
  benchmark that was not recorded must be re-run.
- Deterministic properties such as a call count are legitimate test assertions. Wall-clock
  assertions are not. Use generous timeouts in the cycle.
- Performance-relevant work should not leave metrics empty entry after entry. Sample
  `N/A` entries for plausibility; even a refactor can regress performance.
- To measure the practice itself: time from opening the journal to the first productive
  action on sampled resumes, and writing time per checkpoint; compare with unjournaled
  tasks; publish the ratio with the sample size. One sample is low confidence because
  task difficulty confounds it. Counting clarifying questions is an alternative.
- For chat checkpoints measure capture and restore separately, and the full loop. A speed
  or size gain that comes with fabrication, loss, overwrite, disclosure or stale replay
  is rejected.
- Capture intervals: source selection, privacy review, construction, write, validation.
  Restore intervals: discovery, review, identity and freshness probes, decision
  (continue, adapt, stop, reroute or clarify), recovery.
- Experiment shape: a baseline (no checkpoint, or the prior form); small and boundary
  fixtures; a cold reader; the expected action, gate and stop condition declared in
  advance; enough repetitions in randomized order; failed and abandoned runs included;
  repeat after material changes. Set tool-call and timeout budgets for the run.
- Measurement packet: input size, source count, tool-call count, wall-clock time,
  percentiles where runtime applies, reviewer decision time.
- Pass: a reviewer can find the next action, the gate and the stop condition without
  opening unrelated files. No measured baseline or percentile exists for any of this.

## Scale Boundary Statement

- One journal per feature, ticket or lane. Scale by adding journals, not by growing one.
  Three concurrent writers make a single shared phase undefined; split.
- Two tiers work: a master journal tracks phase transitions across lanes while lane
  journals hold batch detail. Four lanes with one master has been run. More than two
  tiers is untested.
- Keep entries link-sized. The latest entry must carry everything needed forward; history
  is for audit. A rollup summary (about every dozen entries, a heuristic) helps skimming
  and never replaces entry quality. Archive completed journals where they can be found.
- The journal records decisions. It does not approve or govern them.
- Each prompt covers one transition of one workstream.
- A chat checkpoint is enough while one cold reader can find the file, understand its
  mode, verify the state, identify one owner and choose one action.
- Long journals can use a rolling summary at the head, a milestone index, or linked
  continuation journals. Each keeps the latest entry self-sufficient.
- The practice is not enough for several independent systems, more than one ownership
  boundary, unbounded discovery, or production traffic with no explicit objective. There,
  add a parent manifest, exclusive scopes, an integrator, and the operations controls of
  the domain.
- Chat checkpoints progress through stages as volume grows: standalone file; manifested
  set with a root owner; managed store with lineage, access, integrity and retention;
  the domain's records system for incidents and legal evidence. When moving between
  stages preserve bytes, provenance, time, mode, owner and status, keep links in both
  directions, switch the active pointer atomically, apply deletions to payload and index
  alike, and never widen permissions. No universal size threshold exists.

Signals that the simple chat checkpoint is no longer enough, and the control each calls
for before continuing:

| Signal | Why a timestamped file falls short | Minimum control | Route or split |
|---|---|---|---|
| Several repositories or independent systems | State changes under separate versions, owners and release cycles | Parent manifest, probes per system, one integrator | Split by repository or authority; link returned evidence to one parent decision |
| Several owners | Several actors can issue incompatible next actions or change overlapping scope | Accepted ownership, exclusive scopes, conflict detection, a convergence owner | Handoff or orchestration protocol; freeze overlapping writes until reconciled |
| Unbounded discovery | The reader cannot tell whether the evidence set is complete or canonical | Ranked sources, a stopping rule, a source budget | Narrow by task, dependency graph, time horizon or claim |
| Many versions | File names no longer show which checkpoint is current | Stable ID, active pointer, status, lineage, a consistent index | Root manifest or managed index; test cold discovery |
| Incompatible privacy, access or retention classes | One repository destination cannot lawfully or safely serve every artifact and every reader | Classification, approved stores, least-privilege access, retention, deletion and audit controls | Split by policy domain and link only safe bridge metadata |
| Concurrent creators or restorers | Unique file names prevent overwrite but not divergent authority or duplicate mutation | Concurrency control, an idempotent identity, owner arbitration, status-transition rules | A managed store or an orchestrator with one integration owner |
| Drift over time | Captured files, tests, instructions, permissions and owners become history | Periodic checkpoints, observation times, stale probes, supersession | Split by milestone; check against the current spec before continuing |
| A broad codebase | Review budget goes to unrelated files and the canonical evidence is hidden | Narrow the dependency graph first, rank evidence, bound fan-in | Narrower task checkpoints, not one codebase-wide resume file |
| Production traffic or production mutations | A wrong restore can affect availability, data, customers or rollback authority | An explicit service objective, authorization, durable auditable state, idempotency, rollback, monitoring, incident integration | Production operations and deployment controls; the checkpoint is supporting context only |
| Regulated, audit-grade or legal recordkeeping | Editable local files may not meet immutability, custody, access, residency or deletion duties | An approved records system with integrity and custody evidence, policy-driven retention, authorized export | Repo-root Markdown is not the system of record |
| Index or managed-store outage | Central discovery becomes an availability bottleneck | Read-only fallback marked with its age, no mutation, reconciliation after recovery | Conditional access only; never infer current authority from a cached copy |

## Outcome Metrics and Feedback Loops

No baseline or healthy range has been measured for any metric here.

| Metric | Meaning | Caution |
|---|---|---|
| Resume latency | Start to first productive action | A fast resume that skipped reconciliation is a violation |
| Reconstruction incidents | Context had to be re-derived beyond the snapshot | Count against real context breaks; zero may mean no interruptions |
| Trigger coverage | Triggers fired vs entries written | From the compliance report |
| Checkpoint staleness | Time between last entry and current work | Leading indicator; every resume failure starts stale |
| Completion-rule violations per entry | From the entry gate | Self-grading inflates |
| Restatement fidelity | State restated in own operational terms | Verbatim copying does not count |
| Succession depth | Summary or owner boundaries crossed with no reconstruction | Integrated score; one clean boundary is underpowered |
| Handoff success | Successor proceeds without clarification | Late gaps must link to their transition |
| Audit yield, corrections per audit | Findings per audit | Falling yield is success and not a reason to stop auditing; zero may mean a toothless audit |
| Mediated vs improvised transitions | Share run through a template | Invocation alone rewards ritual pasting |
| Witnessed-failure rate, first-run passes, restarts, owner exceptions, regression catches | Cycle discipline | Zero restarts is ambiguous |
| Chat: fidelity, undisclosed loss, overwrites, sensitive violations, identity errors, stale detection, next-action accuracy, review time, handoff conflicts, recovery completeness, storage used | Capture and restore quality | State each denominator; file count is not continuity |

Journal volume measures writing, not continuity. A metric that never changes a rule or a
cadence should stop being collected. A resume that needed transcript archaeology is the
signal to tighten cadence or entry rules.

## Completeness Checklist

Run before accepting an artifact and again before resuming or handing off.

- [ ] Purpose, reader and artifact type named.
- [ ] All seven sections present, plus a real date; no placeholder brackets.
- [ ] Minimal completion rule for the current phase met.
- [ ] Each touched component listed with dependency direction and its validating tests.
- [ ] Trigger that caused the entry is identifiable.
- [ ] Entry checked against the live repository at least once since it was written.
- [ ] Handoff: template matches audience; rollback or acceptance condition present;
      requirement IDs or nearest stable identifiers filled.
- [ ] Chat file: mode, count, labels, order, trim markers, unique name, metadata, final
      newline; sensitive content reviewed; partial scope stated.
- [ ] Restore drill done: historical vs current facts separated, what must be revalidated
      named, next safe action derived.
- [ ] Capture verdict and restore verdict recorded separately.

## Adjacent Reference Routing

| Question | Where |
|---|---|
| Requirement wording, test matrix, quality gates per requirement | [executable-specs](../executable-specs/SKILL.md) and [A03](../../../A03-Executable-Specs01.md) |
| Why state must be serialized | [A00](../../../A00-LLM-Principles01.md), principles 3 and 10 |
| Process weight for a task | [A01](../../../A01-LLM-Workflow01.md) |
| Cause of an unknown failure | A debugging method; return with a reproducing test |
| Splitting work across subagents | A delegation or subagent-execution skill; this skill supplies the packet |
| Complete thread export, encryption, retention | An authorized export or records system |
| Live branch, diff and file state | Repository tooling; the journal only points at it |
| Contested architecture | A decision record; the journal links to it |
| Sensitive content in a capture window | The security or privacy owner, before anything is written |
| Shared ownership of files or lanes | Handoff coordination with a named integrator |
| Mock and test-double design in depth | A testing anti-patterns guide; the short list is under "The cycle and its gates" |
| Checking that a skill file itself is well formed | A skill-writing or skill-validation skill |

When routing, send the smallest payload, name the owner and the observation time, and say
what evidence should come back (a test, a permission, an acceptance, a locator). Check
the route again on restore. Do not fill an unavailable, stale or superseded route from
memory. Reject a route that is circular, has no named owner, cannot return its result to
the reader, weakens permissions, duplicates without explanation, or would not change the
decision.

## Source Evidence Mapping Table

| Source | Used for | Status |
|---|---|---|
| "superpowers" skill collection: test-driven-development skill and its testing anti-patterns companion | Ideas, restated: explicit verify steps with return edges, restart on code-before-test with owner exceptions, when-stuck readings, test-double pitfalls | Read locally; upstream location and authorship not recorded |
| https://developers.openai.com/codex/guides/agents-md | Context on agent instruction scope | Listed; not retrieved |
| https://docs.github.com/actions | Context on automation, artifacts, retention | Listed; not retrieved |
| https://agents.md/ | Context on the agent instruction file format | Listed; not retrieved |

The three URLs are analogues. None is evidence that phase-based journaling or the seven
sections are a standard.

## Evidence Boundary Notes

- The journal contract, cadence rules, prompts, chat capture rules and the script are the
  owner's practice, distilled from use. They are internally consistent and have run
  across many assignments and context summaries with agent successors. That is documented
  usage with the evaluator, operator and subject overlapping. It is not a controlled
  comparison.
- Not measured: journaled versus unjournaled work; scripted versus improvised
  transitions; the 20 to 40 minute interval; the dozen-entry rollup; audit frequency; the
  minimum task size worth journaling; packet versus full-journal handoff; transcript
  overhead at high loop frequency; any reliability target above.
- Claims that test-first is faster than debugging afterwards are the upstream author's
  assertions, not findings.
- The owner's chat capture rules cover capture mechanics only. Restore reconciliation,
  manifests, lifecycle states, privacy review and telemetry in this file are extensions
  by inference.
- The project block example (layers, 25+ TPS target, backends) is one project's
  configuration.
- The script behaviours listed in SKILL.md can be confirmed by running the bundled script.
- The rules name events and behaviours, not tools, so they age slowly. A stable rule can
  still be unvalidated. A controlled cadenced-versus-uncadenced run and
  an independent deployment would be the natural upgrades.

## Future Refresh Search Queries

- agent session persistence checkpoint resume workflow
- agent memory management session handoff
- TDD workflow journaling practices progress journal
- chat transcript checkpoint export restore agent thread
- AGENTS.md conventions changelog
- superpowers test-driven-development skill upstream repository release notes

Search by ecosystem vocabulary; the internal titles return noise. Date each retrieval,
record which claim it confirmed or changed, and do not read a failed query as absence.
Refresh when the host agent's thread, memory or export features change, since those can
supersede the repo-root chat file.
