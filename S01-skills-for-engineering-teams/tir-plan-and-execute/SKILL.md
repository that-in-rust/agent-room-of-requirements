---
name: tir-plan-and-execute
description: >-
  Turn an approved design into an ordered, verifiable implementation plan and execute it in checked batches. Use after design approval when ready to write or run a multi-step plan.
---

# TIR Plan and Execute

Focused skill for writing actionable implementation plans and executing them in verified batches. Companion reference: [reference.md](../tir-explore-and-decide/reference.md). Previous step: [tir-explore-and-decide](../tir-explore-and-decide/SKILL.md).

## The Shared Workflow

Every mode is a specialisation of these steps.

1. **Classify the work.** Use the classifier in [A01](../../A01-LLM-Workflow01.md): Bug,
   Enhancement, Feature, Product. Ask in order and stop at the first clear answer: Did
   something break? Am I extending an existing pattern? Can I define done right now? Am I
   still discovering the problem? Pick the lightest process that still protects quality.
   Record the class and its time budget now, not afterwards.
2. **Frame one question.** One decision, one owner, the options, the consequence of being
   wrong, what is reversible, what is prohibited. Unrelated ideas go to a parking lot.
3. **Check the premise.** If the request holds a material ambiguity, a flawed premise or a
   missing constraint, say so plainly and ask one targeted question. If it is workable,
   proceed without ceremony.
4. **Open the option space.** Start with the conventional path. Add real alternatives. No
   straw options, no duplicates with cosmetic differences.
5. **Gather evidence by claim.** For each claim that matters, find the smallest source that
   can settle it. Label each claim: sourced fact, reasoned inference, or speculation.
6. **Challenge.** A skeptical lens, a second agent, or a second timeline attacks the leading
   option. The challenge must be able to change the answer.
7. **Decide, or name the experiment.** Adopt, adapt, avoid, gather more evidence, or
   escalate. An unresolved contradiction that is written down with an owner is a valid
   outcome. A vote is not.
8. **Attach a gate.** Each recommendation gets a command, test, checklist or named review
   that would show it failed, and what happens then.
9. **Get approval where a person must approve.** Designs and plans need an explicit yes.
   Silence, a polished prompt, or "sounds fine" about something else is not approval.
10. **Record and hand off.** Write the decision record, the design, or the plan. Name the
    next bounded action, its owner, the stop condition and the rollback.
## Rules

### Evidence

- No evidence, no proposal entry. Cite `file:line`, log output, runtime results, concrete
  counts, or actual versus expected values inline. "See logs" is not evidence.
- Every proposed fix cites the code it changes and the behaviour that changes.
- Accepting someone else's claim requires your own verification against source or runtime
  evidence. Every acceptance says what was verified. No empty agreement.
- Separate three kinds of statement everywhere: sourced fact, reasoned inference,
  speculation. Label a claim, not a whole section, unless every sentence in the section
  shares source, scope and confidence.
- Information that does not come from the provided sources or from verified research is
  labelled inference or background knowledge, and the user is told they may want to verify
  it independently.
- Prefer primary sources: primary documentation, official publications, papers, direct
  data. Use web research when freshness, citations or precise attribution matter, and include
  links when the user benefits from source access.
- A link that was not fetched is a pointer, not a fact. A search snippet, a landing page or
  a project name is discovery evidence only.
- Copies of the same text are one lineage, not several witnesses. Counting sources is not
  convergence. Being local or being recent gives provenance, not correctness.
- Never average two sources that disagree. Ask whether they make the same claim and which
  authority governs. If that cannot be settled, keep the contradiction, take the reversible
  action, or escalate to the owner.
- Say what would change the conclusion.

### Decision

- Do not give advice by vibe. Compare options on a fixed rubric before recommending.
- One owner decides. Agents and lenses inform. Final judgment stays with a person.
- Choose the smallest bounded next action. High blast radius with weak evidence shrinks the
  action. A tiny reversible action may use more observation and less deliberation.
- Do not pick a middle option because it is the middle. If the compromise weakens
  traceability, dissent or rollback, prefer "avoid" or "gather evidence".
- Record the chosen mode, the rejected options with reasons, the uncertainty and the trigger
  that would reopen the decision. Keep the losing options: they are the monitoring
  instruments later.

### Scope and simplicity

- Prefer the minimum viable fix: the smallest change that solves the observed problem.
- Reject speculative infrastructure, premature abstraction, monitoring without evidence of
  need, and edge-case engineering without evidence that the edge case occurs.
- Flag both over-engineering and under-engineering.
- Related but non-blocking ideas go to the parking lot, tagged, not into the proposal.
- Prefer concrete code changes over abstract philosophy.

### Honesty of presentation

- Present conclusions, evidence, assumptions and tradeoffs. Do not present hidden
  chain-of-thought.
- Do not claim certainty where evidence is thin. Lower stated confidence can be the better
  answer.
- Do not use "omniscient" or authority-theatre language in the final response. Name lenses
  by what they examine, not by invented personas.
- Creativity is not rigor. A novel option must still be defensible.
- Results must be free from harmful assumptions and stereotypes.
- A number presented as a result needs a measurement behind it. Scores, thresholds and time
  budgets in this skill are editorial defaults unless a line says they were measured.

### Approval and writes

- No implementation, scaffolding or artifact generation before the design is approved, when
  the request is to build something. A short design is allowed. No design is not.
- One question per message while clarifying. Prefer multiple choice.
- Never start implementation on `main` or `master` without explicit consent.
- Do not commit or push unless the repository's rules and the user allow it. Ask first.
- One writer per file. Parallel work is read-only investigation unless the write sets are
  disjoint and a merge owner is named.
## Mode 5: Write a Plan

Use when there is an approved design or a clear spec for multi-step work, before touching
code. Plan-worthy work is Feature or Product class, or any change with several dependent
steps. Bugs and small enhancements get their lighter flow and a classification note instead.

Write for a skilled engineer who knows nothing about this codebase, its tools or its domain,
and who is not strong at test design. Everything they need is in the plan.

### Rules

1. **Exact file paths, always.** Create, modify (with line range where known), test.
2. **Complete code in the plan.** Not "add validation". The code that adds it.
3. **Exact commands with expected output**, including the expected failure before the fix.
4. **One action per step, two to five minutes each.** Write the failing test. Run it and see
   it fail. Write the minimal code. Run it and see it pass. Commit (if allowed).
5. Do not repeat yourself, do not build what is not needed, test first, commit often.
6. Save to `docs/plans/YYYY-MM-DD-<feature-name>.md`, before the code exists. A plan
   reconstructed after execution proves little.
7. Work in an isolated branch or worktree, not on `main`.

"Implement the endpoint" is an oversized task. Split it.

### Plan template

````markdown
# <Feature Name> Implementation Plan

**Goal:** <one sentence: what this builds>
**Architecture:** <two or three sentences on the approach>
**Tech stack:** <key languages, libraries, tools>
**Work class and budget:** <Feature | Product>, <budget recorded at intake>
**Design:** docs/plans/<date>-<topic>-design.md (approved <version>)
**How to run this plan:** tasks in order, three per batch, report after each batch, stop
and ask at any blocker.

---

### Task 1: <component>

**Files**
- Create: `src/exact/path/new_file.ts`
- Modify: `src/exact/path/existing.ts:120-145`
- Test: `tests/exact/path/new_file.test.ts`

**Step 1. Write the failing test**

```ts
import { parseRetryAfter } from "../../src/exact/path/new_file";

test("parses seconds", () => {
  expect(parseRetryAfter("120")).toBe(120_000);
});
```

**Step 2. Run it and see it fail**

Run: `npx vitest run tests/exact/path/new_file.test.ts`
Expected: FAIL, "parseRetryAfter is not a function" or module not found

**Step 3. Write the minimal implementation**

```ts
export function parseRetryAfter(value: string): number {
  return Number(value) * 1000;
}
```

**Step 4. Run it and see it pass**

Run: `npx vitest run tests/exact/path/new_file.test.ts`
Expected: PASS, 1 test

**Step 5. Commit** (only if the repository rules allow)

```bash
git add tests/exact/path/new_file.test.ts src/exact/path/new_file.ts
git commit -m "Add Retry-After parsing"
```

### Task 2: <component>
...
````

### Handoff

After saving, offer the two ways to run it and let the user choose:

- **Task-by-task with a fresh subagent per task**, in the same conversation, with a review
  after each task. Fast iteration. Dispatch mechanics belong to
  `agent-context-and-orchestration`.
- **A separate executor** that opens the plan and runs it in batches with review checkpoints
  (Mode 6).
## Mode 6: Execute a Plan

Use when a written plan exists and has not been run. The default is a separate executor with
a reachable reviewer. Self-review or continuous execution is a deviation and is recorded as
one.

### Workflow

1. **Load and review the plan critically.** Raise questions and concerns with the human
   partner before starting. This step is not optional. If there are none, make a task list
   and proceed.
2. **Execute a batch.** Default: the next three tasks. For each task: mark it in progress,
   follow each step exactly, run the verification the plan specifies, compare with the
   expected output, mark it complete.
3. **Report.** What was implemented, the verification output verbatim, then
   "Ready for feedback." Then wait.
4. **Continue.** Apply the feedback, run the next batch, repeat.
5. **Finish.** When all tasks are complete and verified, run the full checks, present the
   options for the branch (merge, pull request, keep, discard) and carry out the one chosen.

### Stop and ask

Stop at once when:

- A blocker appears mid-batch: a missing dependency, a failing test, an unclear instruction.
- The plan has a gap that prevents starting.
- You do not understand an instruction.
- A verification fails repeatedly. Rerun it once. If it still fails, stop and report the
  output. A repeated failure is a stop trigger, not a retry loop.

Ask instead of guessing, even when the fix looks obvious. Do not patch a small plan gap
silently. Return to step 1 when the plan is updated or the approach needs rethinking. Two
failed plan revisions on the same task go to the user.

The wording of a stop tells the reviewer where the defect is: "instruction unclear" points
at the plan; "test fails" points at execution or at a wrong assumption in the plan.

### Batch size

Three is the default. Change it only with the reviewer's consent. Twelve tasks across four
reports is healthy. Forty steps without a report is not. Five homogeneous configuration
tasks in one batch are acceptable with consent. Do not let "three" drift into "a few".

### Batch report template

```markdown
## Batch <n>: tasks <a> to <b>

**Implemented**
- Task <a>: <what changed, files>

**Verification output**
<verbatim command and output for each task>

**Deviations from the plan**
- none | <what, why, who agreed>

**Stops**
- none | <trigger: missing dependency / test fails / instruction unclear>, <output>, <question>

Ready for feedback.
```
## Where the Sources Disagree

Keep both positions. The right-hand column says what selects each.

| Topic | Position A | Position B | What selects |
|---|---|---|---|
| Expert council presentation | Lenses named by function; no theatre; proceed without ceremony; compress small tasks | Older staged protocol: announce a council of 3 to 5 "world-class" personas, narrate each phase at length, state "Premise is sound. Proceeding with optimized protocol." when nothing is wrong | A is the default. Use B only when the user explicitly asks to see the staged protocol. Even then, no "omniscient" or authority language in the final response and no hidden chain-of-thought |
| How verification questions are answered | From available evidence, with research when freshness or attribution matters | From internal knowledge only | A whenever sources or browsing are available. B only when neither is; then label every answer as unverified background knowledge |
| Design before any work | Always present a design and get approval, even for work that looks simple | Proceed without ceremony when the prompt is workable; validate an existing complete design instead of redoing it | Building or changing behaviour: A (a compact design is enough). Analysis-only answer, or a complete approved design with no open decision: B |
| Number of timelines | Three to five | Two for a binary fork | Three to five by default. Two only for a low-stakes binary fork, labelled as a deviation |
| Timeline comparison columns | Workflow lists variance | Template table has no variance column | Workflow governs: include variance. Six columns only on request |
| Debate participants | Two agents | Three agents | Two for speed. Three when the tradeoff is genuinely unclear |
| Ending a debate | Converge only when every dispute is `CLOSED` or `PARKED` | An unresolved contradiction is a valid result | Both hold: an unresolved contradiction is recorded as `PARKED` with an owner and next experiment, or the proposal stays `OPEN` and goes to the owner. It is never papered over |
| Execution batch size | Three tasks | Other sizes | Three by default. Another size only with the reviewer's consent |
| Committing the design or plan step | Commit the design document and each task | Never commit or push without permission in repositories that say so | The repository's rule and the user decide. Ask when unsure |
| Process weight | Full plan-and-batch discipline | Lightest safe flow | Feature and Product work: full. Enhancement: light. Bug: reproduce, test, fix. Unsure: the lighter flow, with the intake budget as a tripwire |
## Output Contract

Hand back the artifact for the mode, plus a short decision summary.

| Mode | Artifact | Must contain |
|---|---|---|
| 1 | Research brief | The seven sections in order (or a stated compression); claim classes; what would change the conclusion |
| 2 | Scenario map | Six sections in order; 3 to 5 timelines (or labelled deviation); assumptions; all three filter answers, each naming a timeline or an experiment |
| 3 | Debate file | Header with topic, agents, rounds, status; context, evidence, relevant files, constraints; proposal with `STATUS: OPEN` or `STATUS: CONVERGED`; parking lot; dispute log with `OPEN`, `CLOSED`, `PARKED`; per-turn prompts rendered from the live file |
| 4 | Design document | Options with tradeoffs; recommendation; design sections; approval events; handoff |
| 5 | Plan file | Header; tasks with exact paths, complete code, commands, expected output |
| 6 | Batch reports | Implemented items; verbatim verification output; stops; "Ready for feedback." |
| 7 | Candidate dossier | Evidence of demand; overlap audit; owner; pilot; kill criteria; state |

Decision summary, for every mode:

```markdown
- Decision or recommendation:
- Mode used and why:
- Options rejected, with reasons:
- Evidence it rests on (facts with locators; inferences marked):
- Remaining dissent or open questions, and who owns them:
- Next bounded action and owner:
- Gate (command, test, checklist or review) and what a failure triggers:
- Stop condition and rollback:
```

An uninvolved reviewer should be able to reconstruct the decision from the artifact alone,
without the conversation.
## Quality Gates

Run the ones that match the artifact. A passing structural check shows the shape is
complete. It does not show the reasoning is right; read the artifact once more after it
passes.

Exploration brief, section order:

```bash
F=brief.md
prev=0
for h in "Premise Check" "Expert Lenses" "Candidate Approaches" "Chosen Thesis" \
         "Evidence and Verification" "Final Synthesis" "Open Questions"; do
  n=$(grep -n -m1 -E "^#+ +$h" "$F" | cut -d: -f1)
  if [ -z "$n" ]; then echo "MISSING: $h"; elif [ "$n" -lt "$prev" ]; then echo "OUT OF ORDER: $h"; fi
  prev=${n:-$prev}
done
grep -n -i -E "omniscient|IQ of|world-class expert" "$F" && echo "FAIL: authority language"
```

Timeline output, sections, count and filter:

```bash
F=timelines.md
for h in "Decision Frame" "Cross-Timeline Analysis" "Decision Filter"; do
  grep -q -E "^#+ +$h" "$F" || echo "MISSING: $h"
done
n=$(grep -c -E "^#+ +Timeline [A-E]" "$F")
[ "$n" -ge 3 ] && [ "$n" -le 5 ] || echo "CHECK: $n timelines (3 to 5 expected, or a labelled deviation)"
[ "$(grep -c -E '^- Opening move: *\S' "$F")" -eq "$n" ] || echo "FAIL: a timeline has no opening move"
grep -c -i -E "strongest if|safest if|reduce uncertainty" "$F"   # expect 3 or more
```

Debate file, convergence and tags:

```bash
F=debates/topic.md
grep -n '^STATUS:' "$F"                                   # exactly one line
open=$(grep -c -E '\| *OPEN *\| *$' "$F")
if grep -q '^STATUS: CONVERGED' "$F" && [ "$open" -gt 0 ]; then
  echo "FAIL: CONVERGED with $open OPEN disputes"
fi
grep -c -E '\[A[1-3]-R[0-9]+\]' "$F"                      # tagged lines; the unreplaced parking-lot placeholder counts as 1
grep -n -E '^\{' "$F"                                     # leftover placeholders
grep -n -i -E 'see (the )?logs|as discussed|I agree\.?$|looks good' "$F"   # weak evidence, empty agreement
python3 scripts/render_debate_turn_prompt.py --debate-file "$F" --agent-number 1 --round 1 >/dev/null \
  && echo "header parses"
```

Plan file, completeness:

```bash
F=docs/plans/2026-07-10-feature.md
for k in '\*\*Goal:\*\*' '\*\*Architecture:\*\*' '\*\*Tech stack:\*\*'; do
  grep -q -i -E "$k" "$F" || echo "MISSING header field: $k"
done
t=$(grep -c -E '^### Task [0-9]+' "$F"); r=$(grep -c -E '^Run: ' "$F"); e=$(grep -c -E '^Expected: ' "$F")
echo "tasks=$t run=$r expected=$e"                        # run and expected must be equal, and at least 2 per task
grep -n -i -E 'add validation|handle (the )?edge cases|as appropriate|TBD|TODO|similar to above|etc\.' "$F" \
  && echo "FAIL: vague step"
git branch --show-current                                 # not main or master before executing
```

Checks with no command:

- Brainstorm: there is a recorded approval event for the version being planned; the options
  differ in substance; questions were asked one at a time. For visual or interactive work,
  open the rendered output; text checks do not substitute for looking.
- Execution: every batch report holds verbatim verification output; every stop has a
  trigger and a resolution.
- Gap analysis: remove the owner or the kill criterion from the dossier; if nothing blocks,
  the gate is not working.
## Anti-Patterns

| Anti-pattern | What to do instead |
|---|---|
| Advice by vibe: one confident answer, no alternatives | Compare options on a fixed rubric; give the filter answers |
| Premise laundering: optimizing a question that should have been corrected | Check the premise first; ask one targeted question |
| Theatrical experts; "omniscient" framing | Functional lenses, each with a distinct contribution |
| Straw or duplicate options; decorative domain blends | Options that differ in substance; blends that change the solution |
| Ceremonial skepticism; verification that changes nothing | The challenge must be able to move the thesis; show the revision |
| Mixed evidence classes; unsupported certainty | Label fact, inference, speculation per claim |
| Literature dump or summary instead of a thesis | One working thesis with rejected alternatives |
| Catastrophe theatre in timelines | Plausible paths; tail risk only when labelled |
| Structure laundering: a gut answer poured into template fields | Opening moves, causal links and specific assumptions; thin generic assumptions are the tell |
| Collapsing "strongest if normal" and "safest if bad" | Answer both; state the tension |
| Empty agreement in a debate ("I agree", "looks good") | Each acceptance says what was verified |
| Majority vote or source counting as convergence | Reconcile on evidence; park with an owner |
| `STATUS: CONVERGED` with open disputes | Revert to `OPEN` and explain |
| Scope creep in the proposal | Parking lot |
| Speculative infrastructure for unobserved problems | Minimum viable fix |
| Building before approval; inferring approval from silence | Present, ask, record the approval event |
| Several questions in one message | One question per message |
| "Too simple to need a design" | A design of a few sentences, approved |
| Vague plan step ("add validation") | Exact path, complete code, command, expected output |
| Guessing through a blocker | Stop, report the output, ask |
| Skipping batch reports; reporting only at the end | Report after every batch and wait |
| Heavy process on a bug; no plan for a multi-step feature | Classify first; lightest safe flow |
| New agent from one interesting prompt; tool-first proposal | Demand evidence, overlap audit, pilot, kill criteria |
| Gate with no meaning: a command unrelated to the claim | A gate whose failure invalidates a named claim |
| Acting before the evidence is in (premature mutation) | No writes until the owner authorizes one bounded action |
## Closing Self-Check

Before handing anything back:

- [ ] The work was classified, and the process matches the class.
- [ ] One question, one owner, stated constraints.
- [ ] The premise was checked, and corrected or confirmed in a line.
- [ ] At least the conventional option and real alternatives were compared; the rejected
      ones are recorded with reasons.
- [ ] Every claim that carries weight has a locator, or is marked inference or speculation.
- [ ] Something challenged the leading option and the result of that challenge is visible.
- [ ] The recommendation names the next bounded action, its owner, its gate, its stop
      condition and its rollback.
- [ ] Dissent is resolved, gated, parked with an owner, or escalated. None was dropped.
- [ ] No certainty beyond the evidence; no authority language; no hidden reasoning shown.
- [ ] For a debate: no `CONVERGED` with `OPEN` disputes; every edit tagged.
- [ ] For a timeline: 3 to 5 paths with opening moves, lived cost, variance, three filter
      answers.
- [ ] For a design: explicit approval recorded before anything was built.
- [ ] For a plan: exact paths, complete code, commands, expected output, saved before the
      code.
- [ ] For execution: reviewed first, batches of three, verbatim output, stopped at blockers.
- [ ] For a gap analysis: demand evidence, overlap audit, owner, pilot, kill criteria; or
      the work paused because demand could not be observed, and the next step is an
      interview, a task-history review or one narrow manual trial.
- [ ] The quality-gate commands for the artifact were run and their output read.
