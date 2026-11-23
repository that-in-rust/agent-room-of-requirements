---
name: tir-tdd-progress-and-resume
description: >-
  Keeps a long test-driven task resumable. Runs STUB -> RED -> GREEN -> REFACTOR with a
  witnessed failure and a witnessed pass, writes an append-only progress journal (phase,
  tests, implementation, focus, next steps, notes, metrics) at phase changes, test
  changes, milestones, risk events and before every break, resumes from the latest
  snapshot by checking it against the live repository and doing only the first next step,
  writes developer and agent handoff packets, and saves the last few visible chat messages
  to a timestamped chat-checkpoint-YYYYMMDD-HHMMSS.md file. Use when TDD work spans
  sessions, context resets, several files or crates, or more than one owner; when the user
  says "where were we", "save progress", "checkpoint this", "resume the TDD work", "hand
  this off", "tests are red now", "all green, time to refactor", "back up the last 5
  messages", "dump recent chat to a file"; when a journals/*.md progress journal, a
  chat-checkpoint-*.md file or scripts/journal_orchestrator.py is involved. Not
  for writing requirements or a test matrix (use executable-specs), finding the cause of an
  unknown failure (debug first, then come back with a reproducing test), a one-sitting task
  that finishes warm, full-thread export or encrypted or managed transcript storage,
  project status reports that have no tests behind them, or approving design decisions
  (the journal records decisions, it does not make them).
---

# TDD Progress and Resume

A long test-driven task survives interruptions only if its state is stored in a file, not
in memory. This skill runs the test-first cycle, writes that state as a structured
progress journal, resumes and hands off from the journal, and can back up recent chat text
when a thread is about to lose continuity.

The principles behind it are in [A00](../../A00-LLM-Principles01.md) (context windows
forget; serialize state) and the cycle is step 4 of
[A03](../../A03-Executable-Specs01.md). Depth, long tables and extended examples are in
[reference.md](reference.md); everything needed to do the job is on this page.

## When to use

Use it when any of these is true:

- The task will cross a session, a context reset, a break, or an owner.
- The work touches several files, modules, crates or services and the test state is easy
  to lose.
- Someone asks where the work stands, or asks to save, resume or hand off.
- A chat thread is about to be lost and the recent messages are worth keeping.

Requests that should trigger it:

1. "I've written tests for the new /v1/streaming endpoint. They're all failing as
   expected." (Capture the Red state before implementing.)
2. "I'm back on the MLX integration. Where were we?" (Resume from the journal.)
3. "All tests are green now. The implementation works but it's messy." (Checkpoint the
   Green milestone before refactoring.)
4. "I've updated the engine trait in one crate and added the Metal implementation in
   another." (Track cross-crate progress against the tests.)
5. "Save the last 5 messages to a file before this thread compacts." (Chat checkpoint.)
6. "Write a handoff for the agent that takes over this ticket tomorrow." (Handoff packet.)

Requests that should not trigger it:

1. "Turn 'make import faster' into acceptance criteria." That is requirement writing; use
   [executable-specs](../tir-executable-specs/SKILL.md).
2. "The build fails and I don't know why." Diagnose first. Come back when there is a test
   that reproduces the bug.
3. "Rename this variable." A one-sitting change that finishes warm needs no journal. If
   you skip the journal, say so in one line so the decision is visible.
4. "Export the entire conversation with encryption and retention rules." That needs an
   authorized export or a managed store, not a repo-root Markdown file.

Use it proactively throughout test-driven work; do not wait to be asked for a checkpoint.

Decide at task start. Waiting until context is lost makes reconstruction impossible.
Journaling every trivial errand teaches ceremony and erodes compliance, so the selector is:
will this work plausibly outlive one warm sitting or one owner? If yes, journal.

## Pick the artifact first

Name the purpose and the reader before capturing anything. The three artifacts answer
different questions and do not substitute for each other.

| Artifact | Answers | Reader | Where the rules are |
|---|---|---|---|
| Progress journal checkpoint | Which phase, which tests fail, what is next | Future self after a break | "Journal contract", "Checkpoint cadence" |
| Handoff note or packet | What is done, what is broken, what the successor owns | Another developer or agent | "Handoff" |
| Chat checkpoint file | What was literally said in the last few messages | Anyone recovering a lost thread | "Saving recent chat context" |

A chat checkpoint is not a work-state record: a faithful transcript can lack the failing
test names. A journal is not a transcript: it does not preserve wording. Pair them when
both matter.

## Workflow

1. **Decide and initialize.** At task start, decide whether to journal. If yes, create one
   journal per feature, ticket or workstream. If a journal for this workstream already
   exists, continue it; never start a fresh one beside it.
   `python3 scripts/journal_orchestrator.py init --path journals/<name>.md --task "<title>"`
2. **Work the cycle one behaviour at a time.** STUB -> RED -> GREEN -> REFACTOR, with the
   two witnessed gates (see "The cycle"). One requirement at a time.
3. **Checkpoint on triggers.** Append an entry at every phase change, test-surface change,
   implementation milestone and risk event, and always before a break. Write the entry
   before acting on the new state, not after.
4. **Run the write-time gate.** Before accepting an entry, answer the five self-check
   questions (see "Journal contract").
5. **Resume from evidence, not memory.** After any pause, read the latest snapshot, check
   it against the live repository, restate the state, then execute only the first next
   step and checkpoint again.
6. **Hand off with the right template.** Developer note for a person, structured packet
   for an agent. Capture a final checkpoint first.
7. **Audit.** At a cadence you choose, run the quality-check prompt on recent entries and
   append corrected entries. "No chosen cadence" means never.
8. **Close.** End the workstream with a final entry: complete (full gate results) or
   abandoned (why, and what state the code is in).

## The cycle

```text
STUB -> RED -> GREEN -> REFACTOR -> (VERIFY, then next behaviour)
```

| Step | Do | Gate | Journal |
|---|---|---|---|
| STUB | Write the test and the interface it expects. Nothing else. | The test compiles or imports and can run. | Phase `Red`, test status `pending`. |
| RED | Run the one test. | It fails, and for the expected reason: the behaviour is missing. The failure message is the one you predicted. An error, typo or broken import proves nothing; fix it and run again. | Phase `Red`, test `failing`, exact failure message in the detail. |
| GREEN | Write the smallest code that satisfies the test. | The target test passes, the rest of the suite still passes, and the output is clean. | Phase `Green`, test `passing`, files and functions changed. |
| REFACTOR | Improve names and structure. Add no behaviour. | Re-run after each change; the suite stays green. | Phase `Refactor`, debt or cleanup targets. |
| VERIFY | Run the full gate set for the requirement. | Fresh run after the last edit; read the output, not only the exit code. | Results in Metrics and Notes; next step names the next behaviour or the close. |

Rules for the cycle:

- No production code before a test has been seen to fail for the intended reason. The
  order produces evidence: a test that never failed has not shown it can catch anything.
- A test that passes on its first run is a warning. Either the behaviour already exists
  (record that) or the test checks the wrong thing (fix the test until it fails for the
  intended reason).
- Do not edit a test to make it pass unless the requirement itself changed. If it did,
  say so in the journal.
- Fix a broken neighbouring test now. Do not defer it to a later cycle.
- One behaviour per test, one test per cycle. A test name that needs "and" is two tests.
  A parameterized test over many inputs is fine when it is still one behaviour.
- Prefer real code over mocks. Assert on what the code under test does, not on the mock.
- For a bug: write the test that reproduces it first, watch it fail, then fix.
- Keep timing assertions out of the cycle ("finishes within 50 ms" makes a flaky Red).
  Benchmark separately and record the number in the journal's metrics.
- Code written before its test: the strict position is to delete it and implement again
  from the test, not keep it "as reference". Throwaway prototypes, generated code and
  configuration files are exceptions only when the human in charge says so. The agent
  does not grant itself the exception. Which position applies is the owner's call; record
  the decision in Context Notes.
- If a thought like "too simple to test", "I'll test after", "this is different because"
  or "deleting this is wasteful" appears, stop and return to STUB. Do not argue with it.
- When stuck: write the call you wish existed and its assertion first. A test that is hard
  to write points at a design that is hard to use; simplify the interface before relaxing
  a gate.
- Work outside-in when a behaviour needs several units: the outer test goes red first and
  stays red while inner tests cycle beneath it.
- The phase decides what the next action may be: in Red, only make the test fail
  correctly; in Green, only make it pass; in Refactor, only restructure.

The journal has three phase values (`Red`, `Green`, `Refactor`) and the bundled script
accepts only those. STUB work is journaled under `Red` with tests marked `pending`. VERIFY
is journaled as the closing entry of the behaviour, under the phase it ran in.

## Journal contract

Every checkpoint carries the same seven sections, with these names:

1. `Current Phase`: exactly one of Red, Green, Refactor.
2. `Tests Written`: each test as name, status, expectation.
3. `Implementation Progress`: each component or function, its status, what changed.
4. `Current Focus`: the task objective right now.
5. `Next Steps`: ordered, actionable. Never empty.
6. `Context Notes`: decisions and why, approaches tried (including the ones that failed),
   blockers and open questions, technical debt.
7. `Performance/Metrics`: benchmarks, budgets, limits, or an explicit `N/A`.

With the date, that is eight fields. An entry with placeholder brackets still in it
proves only that the template was copied.

**Minimal completion rules**

- Always include one explicit phase. Update it after a pivot.
- Always include at least one next step.
- In Red, always capture the failing tests.
- In Green, always capture the implementation surface that changed.
- In Refactor, always capture the debt or cleanup targets.

**Entry quality rules**

- Exact test names, not summaries. "Tests mostly passing" cannot be checked. Where the
  work has no test names, use an equivalent falsifiable command and its count.
- File paths for every changed implementation, with line numbers when useful. Add
  function signatures and exact error messages when available.
- Next steps actionable and ordered. The first one names a command or a single
  file-scoped action. "Investigate the flaky test properly" is not a step.
- Blockers marked clearly, with an owner and the condition that clears them.
- Record why, not only what. The reason behind a test or a design choice is what makes a
  later refactor safe.
- Record which test exercises which component.

**Test row micro-contract.** `name | status | expectation`. Status is `passing`, `failing`
or `pending`. The three parts give identity, state and meaning: enough to re-run the test
and to interpret the result.

**Multi-component tracking.** When work spans modules, crates or services:

- List each touched component separately.
- State the dependency direction, for example `crate-a -> crate-b`.
- Note which tests validate each component.
- Flag any progress in one component that waits on another.

**Project block (optional eighth section).** Section names are fixed; depth is not. A
project may append one extra section if every entry carries it. Useful contents for a
layered codebase: the layer map and its dependency rule (for example `L1 core -> L2 engine
-> L3 CLI/API, no cycles`), work that spans two languages across a bridge, the project's
performance target, and which backend alternative a change belongs to. Those values belong
to the project. Do not copy another project's numbers into the rule set.

**Write-time gate.** Before accepting an entry, answer:

- Could another developer resume this work immediately from this entry alone?
- Is the "why" behind decisions captured, not only the "what"?
- Are all test statuses current and accurate?
- Are dependencies that could block progress noted?
- Is the next step unambiguous?

**Guardrails**

- Never leave Next Steps empty.
- Track why for major decisions, not only what.
- Record cross-component dependencies explicitly.
- Keep updates small and frequent to reduce context drift. Small means scoped, not empty:
  a stream of trivial entries buries the meaningful ones.
- Prefer append-only checkpoints over rewriting history. Fix a wrong entry with a new
  dated correction entry.
- Chat narration is not journaling. If it is not in the file, it is not recorded.
- One owner per journal. Parallel lanes each get their own journal; a master journal may
  track phase transitions across them.

### Two entry shapes

The owner's material has two shapes for the same seven sections. The tool in use selects.
Do not mix them in one journal.

**Manual shape.** Use it on a prompt-only platform or when the script cannot run. Have a
second reader check entries, since nothing enforces the structure.

```markdown
## TDD Session State: [Date/Time]

### Current Phase: [Red | Green | Refactor]

### Tests Written:
- [Test name]: [Status] - [Brief description]
- [Optional: file path and line references]

### Implementation Progress:
- [Component/Function]: [Status] - [What changed]
- [Cross-file or cross-crate dependencies]

### Current Focus:
[Current task objective]

### Next Steps:
1. [Immediate next action]
2. [Following action]
3. [Subsequent action]

### Context Notes:
- [Key decisions and rationale]
- [Approaches attempted]
- [Blockers or unresolved questions]
- [Technical debt noted]

### Performance/Metrics:
- [Benchmarks, budgets, limits, or N/A]
```

**Script shape.** `scripts/journal_orchestrator.py` writes a file header and
appends `### Session: <UTC time>` blocks with `####` section headings. Next steps are
bullets in the order the flags were given; the first `--next-step` is step 1.

```markdown
# TDD Progress Journal

- Task: Feature A end-to-end TDD
- Created: 2026-02-27 19:02:11Z
- Updated: 2026-02-27 19:10:42Z
- Current Phase: Red
- Status: active

## Sessions

### Session: 2026-02-27 19:10:42Z

#### Current Phase: Red

#### Tests Written:
- test_endpoint_rejects_empty_payload: failing - expects 400 on empty payload

#### Implementation Progress:
- api/handlers.rs: added request parser scaffold

#### Current Focus:
Write failing tests for endpoint validation

#### Next Steps:
- Implement minimum handler logic to satisfy validation tests

#### Context Notes:
- Need shared fixture helper for request setup

#### Performance/Metrics:
- (none recorded)
```

**Metrics: blank or `N/A`.** Two positions exist. The looser one: Performance/Metrics is
the only section that may be empty when no benchmark applies. The stricter one: every
checkpoint answers the metric question with a number or an explicit `N/A`, and a blank is
a finding. What selects: on performance-sensitive work, or whenever the entry feeds a
handoff or an audit, use the strict form (`--metric "N/A - no benchmark applies"`). The
script's `(none recorded)` is a blank, not an `N/A`.

## Checkpoint cadence

Semantic events drive the cadence. The clock is a backstop.

**Triggers.** Record a checkpoint when any of these happens:

1. Phase transition: Red to Green, Green to Refactor, Refactor to the next Red.
2. Test surface change: new tests added, an existing test's status changed, a failure
   revealed that a requirement is ambiguous.
3. Implementation milestone: a core function implemented, an interface contract changed,
   a cross-file or cross-crate dependency introduced.
4. Risk event: a performance regression, flaky test behaviour, a suspected race or
   concurrency problem. These fire mid-phase; do not wait for a finished feature.

Each family marks a different kind of drift: a phase change alters what "done" means, a
test change alters what is true, a milestone alters what exists, a risk event alters what
is safe. Checkpoint before proceeding on the new model. At Green to Refactor, record what
the passing tests now guarantee.

**Frequency**

- High-intensity coding: every 20 to 40 minutes. This interval is a working heuristic, not
  a measured optimum. Tune it and say that you did.
- Multi-component work: at every meaningful file boundary crossing.
- Before breaks: always one checkpoint. Write as if the interruption starts now.
- Before handoff: a final checkpoint with an explicit next action.
- Before a risky or destructive operation (broad rewrite, commit, push, deletion):
  checkpoint and re-read the current plan or spec.
- Never let more than one session pass between entries.

Time-based cadence suits exploration; event-based cadence suits phase transitions. Use
both. Two events a few minutes apart may share one entry if both are recorded. Do not
thin the cadence when the work gets intense; triggers fire fastest then.

A missed checkpoint gets a catch-up entry now, marked `late`. Never write an entry dated
at the missed time.

## Resume

Continuity is a stored artifact. The journal is the authoritative state; memory is a cache
that must be validated. This applies after any pause, including a short one.

**Protocol**

1. Read the latest snapshot.
   `python3 scripts/journal_orchestrator.py snapshot --path journals/<name>.md`
2. Confirm the current phase and the failing tests against the live repository: re-run
   the named tests.
3. Verify whether recorded dependencies and blockers are now resolved. The world can
   improve during a break.
4. Restate, in your own words, before any edit:
   - the exact failing tests,
   - the files in motion,
   - why the next step is the next step,
   - any constraint that would make a naive continuation dangerous.
5. Execute only the first next step.
6. Update the journal after completing that step.

Any mismatch between the snapshot and the repository is the first work item. Halt, repair
the journal with a new entry, then continue. There is no exemption for a snapshot that is
minutes old. If the recorded plan is obsolete, write a new plan in a new entry; do not
force the first step of a dead plan.

If the journal cannot be resumed from (the phase or the test status cannot be stated),
stop. Rebuild the state once from the repository, the diffs and the test output, and
append one entry marked `reconstructed`. Do not backfill missing entries, and do not
write "tests probably fine". If the evidence is not enough, ask the owner.

**Quick resume prompt.** Use for a routine return.

```text
Load the latest progress journal snapshot and summarize:
1) current TDD phase,
2) currently failing tests,
3) immediate next step.
Then proceed with only step 1.
```

**Detailed resume prompt.** Use when continuing is risky or regression-prone.

```text
Read the latest checkpoint and report:
- test status delta since previous checkpoint,
- implementation files touched,
- unresolved blockers,
- risk areas for regression.
Propose a 3-step continuation plan.
```

Choose depth by the risk of continuing, not by how long you were away. Any wording you
derive from the quick prompt must keep "proceed with only step 1".

## Handoff

Capture a final checkpoint, then write the handoff from it. A handoff carries more than a
resume: the same phase, next steps and blockers, plus open design questions and metrics.
Every context summarization is a handoff to a successor with no working memory, so an
agent should write handoff-standard entries by default.

**Handoff summary.** Always include:

1. Current phase.
2. Top three next steps.
3. Blocker list.
4. Open design questions and unresolved decisions.
5. Latest metrics, if the work is performance-sensitive.

**Developer handoff prompt.** For a person.

```text
Create a handoff note from the latest journal entry with:
- current phase,
- what is done,
- what is broken,
- exact next three steps,
- rollback strategy if next step fails.
```

**Agent-to-agent handoff prompt.** For a machine successor. Use it as written; an agent
cannot reliably recover a missing field by asking.

```text
Prepare a structured handoff packet:
- Current phase
- Requirement IDs impacted
- Tests: passing/failing/pending
- Implementation progress by file
- Dependencies and blockers
- Next action with acceptance condition
```

Rules:

- A person gets a rollback strategy. An agent gets an acceptance condition. Do not send
  the developer note to an agent.
- The "what is broken" list is honest even when it is longer than the "done" list.
- If no requirement IDs exist, map to the nearest stable identifier (ticket, queue row,
  test file). Never leave the field blank.
- `N/A` means considered and not applicable. A blank means nothing was recorded. If
  rollback is irrelevant, say why.
- One handoff per successor, each with a distinct scope. No broadcast handoff.
- If the successor finds a gap, answer quickly in whatever channel is fastest and also
  append the corrected note to the journal. A side-channel answer alone leaves the single
  source of truth wrong.
- A successor inherits the existing journal and continues it.

## Auditing checkpoints

Run this on recent entries at the cadence you chose.

```text
Audit the latest checkpoint for missing context:
- Is next step specific and test-linked?
- Are failing tests named exactly?
- Are changed files listed?
- Is decision rationale captured?
- Is there at least one measurable metric or explicit N/A?
If anything is missing, propose a corrected checkpoint.
```

The five questions test presence, not truth. Also re-run one named test and compare one
claim against the diff. Append the corrected checkpoint as a new entry; do not edit the
old one. A finding that is never written back is a failed audit.

## Saving recent chat context

Use this to back up the last few visible messages of the active thread into a file that
can be reopened if the thread loses continuity. It is the lightest of the three artifacts.

**Defaults**

- Capture the last `5` visible messages unless the user gives a count.
- `messages` or `turns` means chronological message blocks, regardless of speaker.
- `responses` means assistant messages only. Include the immediately preceding user prompt
  when the response is unclear without it.
- Write a timestamped Markdown file to the current repo root.
- Use local time from the current environment.
- Prefer direct copy of the chat text over summarization.

**Steps**

1. Determine the capture window. A stated count (`3`, `5`, `10`) wins. No count means
   `5`. "Responses" means assistant responses. Otherwise capture both sides in order.
2. Determine the destination. Repo root, or the working directory if that is the repo
   root. Filename `chat-checkpoint-YYYYMMDD-HHMMSS.md`. Never overwrite an existing
   checkpoint unless the user explicitly asks; on a name collision pick a new name.
3. Capture only what is actually visible in the active thread. The current conversation is
   the source of truth. Do not invent or reconstruct earlier text. Preserve ordering and
   speaker labels.
4. Write the file with the template below. Keep the transcript mostly verbatim. Light
   whitespace cleanup is fine. Do not rewrite substance unless the user explicitly asks
   for a summary checkpoint.
5. Confirm. Report the saved path, the capture mode and count, and anything trimmed or
   normalized.

**File contract.** Every checkpoint contains `created_at_local`, `repo_root`,
`capture_mode`, `capture_count`, `source`, and a `Transcript` section.

```md
# Chat Checkpoint

- created_at_local: 2026-04-22 16:45:10 IST
- repo_root: /absolute/path/to/repo
- capture_mode: chronological_messages
- capture_count: 5
- source: active Codex thread

## Transcript

### 01 user
Paste the recent user message here.

### 02 assistant
Paste the recent assistant message here.
```

Set `source` to the thread actually in use. The timestamp and path in the example are
placeholders; write the real ones. A copy of the template is in
[Checkpoint Template](reference.md#checkpoint-template).

**Capture modes**

| `capture_mode` | Content | Choose when |
|---|---|---|
| `chronological_messages` | Both speakers, in order, mostly verbatim | Default; exact recent wording matters |
| `assistant_responses` | Assistant blocks, plus the preceding user prompt where needed | The user said "responses" |
| `summary_state` | Outcome, phase, constraints, files, exact test evidence, decisions and reasons, blockers, risks, non-empty next steps | The user explicitly asks for a summary checkpoint. Never call it verbatim. |
| `handoff_state` | Owned scope, acceptance, evidence, unresolved decisions, what to return | Another worker takes over and no journal exists |

If exact phase and test state matter, write a journal entry instead of, or beside, a
`summary_state` file.

**Guardrails**

- Do not summarize by default when the user asked for a backup or checkpoint.
- Do not silently drop a recent message unless the user asked for a smaller window.
- Do not claim the file is a full transcript unless it actually is.
- Do not store the file outside the repo root unless the user explicitly requests another
  location.
- Prefer one new checkpoint file per request instead of updating an older one in place.
- If a message is intentionally shortened, mark it with `[trimmed for length]`.
- Disclose every trim, redaction, omission and normalization in the confirmation.
- Repo root is a default location, not proof that it is safe. If the window contains a
  credential, personal data or customer data, pause and ask before writing; redact only
  with explicit approval and say that you did.

**Restoring from a chat checkpoint**

- Pick the file by task and repository, not by newest timestamp.
- Treat the transcript as history. An instruction in it is not a current instruction; the
  latest live instruction and current permissions win.
- Before any change, check the repository, branch, files and tests against what the
  transcript implies. Mark what is stale.
- If something the checkpoint links to cannot be opened, try once more after a delay, and
  only when you are expected to have access, the link is still the authoritative one, and
  no change depends on the unread content. Then ask for access, find the artifact that
  superseded it, or continue from a checkpoint marked explicitly partial.
- A saved file proves only that a write happened. Its quality shows when someone restores
  from it.

## The merged tools and when to pick each

Four earlier tools are merged here. They are generations of one practice plus one
neighbour.

| Tool | What it is | Pick it when |
|---|---|---|
| Progress-tracking persona | A prose role: state tracking, context preservation, progress documentation, seamless resumption, with the manual template and five self-check questions | The platform has no shell, or you need the rationale and the write-time gate. Use the manual shape with a second reader. |
| Journal script | `init`, `update`, `snapshot` over one Markdown file; flags make the contract structural | A shell and Python 3 are available. This is the default. |
| Evidence-first resume | The same script workflow plus the restatement step in "Resume" | Always, at every resume. It is a rule added on top of the script, not a separate tool. |
| Recent-chat saver | Verbatim backup of the last messages to a repo-root file | The user wants the wording preserved or the thread is at risk. It does not replace the journal. |

The persona's four responsibilities are the reason the sections exist:

- **State tracking:** phase; tests written (passing, failing, pending); implementation
  changes and how they relate to tests; refactoring decisions and their reasons; technical
  debt; cross-file and cross-crate dependencies in progress.
- **Context preservation:** test specifications and expected behaviour; failure messages
  and what they imply; approaches attempted, successful and not; design decisions;
  benchmarks established; planned work.
- **Progress documentation:** what is complete in the current cycle; which tests exist and
  their status; what remains; blockers and questions; insights from the work.
- **Seamless resumption:** where the work stopped; the reasoning behind earlier decisions;
  the exact next step; all of it without searching.

Assume the developer is interrupted often. Write every summary so that re-entry takes the
least possible thought.

## Using the bundled script

`scripts/journal_orchestrator.py` needs Python 3 and no packages. The path is
relative to this skill's directory; call it by its installed path from a project.

```bash
python3 scripts/journal_orchestrator.py init \
  --path journals/feature-a.md \
  --task "Feature A end-to-end TDD"

python3 scripts/journal_orchestrator.py update \
  --path journals/feature-a.md \
  --phase Red \
  --focus "Write failing tests for endpoint validation" \
  --test "test_endpoint_rejects_empty_payload|failing|expects 400 on empty payload" \
  --implementation "api/handlers.rs: added request parser scaffold" \
  --next-step "Implement minimum handler logic to satisfy validation tests" \
  --note "Need shared fixture helper for request setup"

python3 scripts/journal_orchestrator.py snapshot \
  --path journals/feature-a.md
```

| Command | Flags | Behaviour |
|---|---|---|
| `init` | `--path` (required), `--task` (required), `--phase` (default `Red`), `--status` (default `active`), `--force` | Creates parent directories and the header. Refuses to overwrite an existing journal unless `--force` is given. `--force` destroys history; do not use it on a live workstream. |
| `update` | `--path`, `--phase` (required; `Red`, `Green`, `Refactor`, any case), `--focus`, and repeatable `--test "name\|status\|detail"`, `--implementation`, `--next-step`, `--note`, `--metric` | Appends one `### Session:` block stamped in UTC and rewrites the header's `Updated` and `Current Phase`. Fails if the journal does not exist. |
| `snapshot` | `--path` | Prints the header fields and the latest session block, or `No sessions recorded yet.` |

What the script does not do, so you must:

- It does not reject an empty entry. A missing `--next-step` renders `(none recorded)`, a
  missing `--focus` renders `(not set)`, a `--test` without a status renders `unknown`,
  and a nameless one renders `(unnamed test)`. Each of those is a failed entry.
- It has no `Stub` phase. Use `Red` with `pending` tests.
- It never changes `Status` after `init`. At close, append the final entry and edit the
  `Status` line by hand (`complete` or `abandoned`). The header is a pointer to current
  state, not history.
- It does not check that the tests named exist or have the recorded status. The resume
  protocol does that.
- It stamps UTC. Chat checkpoints use local time. Keep each as its tool writes it.

If the script fails, fall back to the manual shape with a second reader, and say so in the
entry.

## What to load when

This page is enough for every operation. Open [reference.md](reference.md) only for:

- the reasoning behind a rule, or a trade-off the rules here leave open
  ("Idiomatic Thesis Synthesis Statement", "Decision Tradeoff Guide");
- the per-loop RED/GREEN transcript, the cadence-compliance report, the transition log,
  or the extended chat-checkpoint manifest ("Theme Specific Artifact");
- worked examples to teach from ("Worked Example Set", "User Journey Scenario");
- failure handling beyond the cases here ("Failure Mode Table",
  "Retry Backpressure Guidance");
- planning limits, targets and metrics, all labelled as unmeasured
  ("Workload Model" through "Outcome Metrics and Feedback Loops").

The prompts in "Resume", "Handoff" and "Auditing checkpoints" are needed only at those
transitions.

## Output contract

What to hand back, by operation:

- **After a checkpoint:** the journal path; the phase; failing tests by exact name; the
  first next step; anything you could not record and why.
- **After a resume:** the restatement (phase, exact failing tests with their live status,
  files in motion, why the next step is next, the dangerous-continuation constraint); any
  mismatch found between snapshot and repository; then the result of step 1 and the new
  entry.
- **After a handoff:** the note or packet in the template's field order, and the journal
  path it was built from.
- **After a chat save:** the saved path; capture mode and count; what was trimmed or
  normalized. Do not call it a full transcript unless it is.
- **At close:** the final entry, the full gate commands with their observed results, and
  the open questions with owners.

Keep observed results separate from inference. "Re-ran `test_x`: fails with `expected
400, got 200`" is an observation. "Should pass now" is not a result.

## Quality gates

Journal entry gate. Run after each `update`; fix every FAIL by appending a corrected entry.

```bash
J=journals/feature-a.md
SNAP="$(python3 scripts/journal_orchestrator.py snapshot --path "$J")"
echo "$SNAP" | grep -qE '^#### Current Phase: (Red|Green|Refactor)$' || echo "FAIL: no phase"
echo "$SNAP" | awk '/^#### Next Steps:/{f=1;next} /^#### /{f=0} f&&/^- /' \
  | grep -v '(none recorded)' | grep -q . || echo "FAIL: Next Steps empty"
echo "$SNAP" | grep -qE '\(unnamed test\)|: unknown( |$)' && echo "FAIL: test row lacks name or status"
echo "$SNAP" | grep -A1 '^#### Current Focus:' | grep -q '(not set)' && echo "FAIL: focus not set"
echo "$SNAP" | awk '/^#### Performance\/Metrics:/{f=1;next} /^#### /{f=0} f&&/^- /' \
  | grep -q '(none recorded)' && echo "WARN: metrics blank; write a number or N/A"
grep -c '^### Session:' "$J"   # entry count; compare with the number of triggers that fired
```

No output apart from the count means the mechanical scan passed. Then read the entry once
for actionability; a scan cannot judge that.

Cycle gates. Run the one test at RED and GREEN, then the suite. Substitute your runner.

```bash
# RED and GREEN: the single test, with its output
cargo test -p <crate> <module>::<test_name> -- --exact --nocapture
pytest path/to/test_file.py::test_name -x
npx jest path/to/file.test.ts -t "test name"

# GREEN and REFACTOR: the whole suite, clean output
cargo test --all-targets --all-features
pytest
npx jest
```

Resume gate. The tests named `failing` in the snapshot must still fail, for the recorded
reason, before you continue. If one passes or fails differently, journal the mismatch
first.

```bash
python3 scripts/journal_orchestrator.py snapshot --path "$J"
git status --short            # files in motion match the entry?
git log --oneline -5          # anything landed since the entry's timestamp?
```

Chat checkpoint gate.

```bash
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
F="$ROOT/chat-checkpoint-$(date +%Y%m%d-%H%M%S).md"
test -e "$F" && echo "FAIL: exists, choose a new name"
date '+%Y-%m-%d %H:%M:%S %Z'   # value for created_at_local

# after writing
for k in created_at_local repo_root capture_mode capture_count source; do
  grep -q "^- $k: " "$F" || echo "FAIL: missing $k"
done
grep -q '^## Transcript$' "$F" || echo "FAIL: missing Transcript"
grep -c '^### [0-9][0-9]* ' "$F"   # blocks written; reconcile with capture_count
test -z "$(tail -c1 "$F")" || echo "FAIL: no final newline"
```

In `assistant_responses` mode the block count can exceed `capture_count` by the user
prompts kept for clarity. Say so in the confirmation.

Cold-reader gate, at least once per review cycle: give the latest entry to a reader who
has not seen the session and ask for the phase, the failing tests and the next action. If
they need to ask a question, the entry failed.

## Anti-patterns

| Anti-pattern | Why it fails | Do instead |
|---|---|---|
| "Made progress on tests", "tests mostly passing" | Nothing to re-run; the resumer cannot confirm state | Exact test names with status and expectation |
| Entry with no phase, or a stale phase after a pivot | The successor cannot place the work in the cycle | One explicit phase, updated at every change |
| Empty or aspirational Next Steps | Resume stalls at the first action | Ordered steps; the first names a command or one file-scoped action |
| What without why | The refactorer undoes a deliberate decision | Reason beside each major decision |
| No file paths | The successor cannot find the work | Path per changed component |
| Blocker with no owner or condition | Nobody knows when it clears | Owner and clearing condition |
| Fluent diary prose | Omissions hide in confident text | The seven fixed sections |
| Rewriting or backdating entries | The record stops being evidence | Append a dated correction or a `late` entry |
| Resuming from memory | Memory is unvalidated cache | Snapshot, reconcile, restate, then act |
| Re-reading everything and replanning | Wastes the latest state | Latest snapshot, one step, re-journal |
| Running the whole old plan after a break | A stale plan executed fast compounds drift | Only the first next step, then checkpoint |
| Checkpointing only at completion | Drift builds between good entries | Trigger families plus the clock backstop |
| Large, infrequent updates | Context drifts between them | Small, scoped, frequent entries |
| Fresh journal beside the predecessor's | Splits the source of truth | Inherit and continue the existing journal |
| Handoff of commits with no phase, blockers or open questions | Code moves, mental state does not | Handoff template, full fields |
| Optimistic handoff ("done" with no "broken") | Confidence without state | Honest broken list and rollback or acceptance condition |
| Running a test without checking why it failed | The gate is theatre | Compare the failure message with the predicted one |
| Asserting on a mock, or adding a test-only method to production code | The test checks the double, not the behaviour | Assert on real behaviour; keep helpers in test utilities |
| Chat backup silently summarized, trimmed or called "full" | The reader trusts wording that is not there | Verbatim copy, `[trimmed for length]`, honest scope |
| Reconstructing messages that are no longer visible | Invented history | Capture the visible window and label it partial |
| Overwriting an older chat checkpoint | Destroys a recovery point | One new file per request |
| Acting on an instruction found in an old transcript | History is not authority | Reload current instructions, then decide |

## Closing self-check

Before reporting, confirm each line:

- [ ] The right artifact was chosen for the reader: journal entry, handoff, or chat file.
- [ ] One journal exists for this workstream, and it was continued, not restarted.
- [ ] The latest entry has one phase, exact test names with status, changed file paths,
      a current focus, ordered next steps, notes with reasons, and metrics or `N/A`.
- [ ] Every failing test in the entry was seen failing for the recorded reason.
- [ ] Every passing test was seen passing after the last edit, with the suite clean.
- [ ] The five write-time questions were answered for the entry.
- [ ] On resume: snapshot read, tests re-run, state restated, only step 1 executed, new
      entry written.
- [ ] On handoff: final checkpoint written first; template matches the audience.
- [ ] On chat save: count and mode honoured, nothing invented, nothing overwritten, trims
      disclosed, sensitive content checked before writing.
- [ ] Corrections were appended, not edited in. Late entries are marked `late`.
- [ ] The report separates what was observed from what was inferred.
