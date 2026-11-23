---
name: tir-explore-and-decide
description: >-
  Deep technical exploration, timeline simulation, structured multi-perspective debate, brainstorming into an approved design, and roadmap gap analysis. Use before committing to an architecture or product direction.
---

# TIR Explore and Decide

Focused skill for exploring options, running structured debates, simulating timelines, and converging on an approved design. Companion reference: [reference.md](reference.md). Next step once approved: [tir-plan-and-execute](../tir-plan-and-execute/SKILL.md).

## When to Use

Use it when at least one of these holds:

- There are two or more plausible paths and the wrong one is costly to undo.
- The question may rest on a wrong premise.
- The answer depends on how a choice unfolds over weeks or months.
- Several agents or reviewers should attack one technical question with evidence.
- An idea has to become a design a person approves before anything is built.
- A multi-step change needs a plan that a reader with no context can run.
- Someone proposes a new agent, skill or tool and the need is not yet shown.

Requests that should trigger it:

1. "Explore whether we should move the monolith to services. Test the premise first."
2. "Simulate how rewrite versus refactor plays out over the next two quarters."
3. "Start a debate on whether to use WebSockets or polling." / "Auto debate this auth
   refactor with Codex and Gemini." / "Continue debate 3 and argue for the simpler approach."
4. "Brainstorm an offline mode for the editor, then write the implementation plan."
5. "Execute docs/plans/2026-07-10-offline-mode.md." / "Which agents do we need next?"

Requests that should not trigger it:

1. "What does `--force` do in this script?" Answer directly. A lookup may need a source
   check, not a council.
2. "The login test fails since yesterday." That is a bug: reproduce, diagnose, regression
   test, fix. Use `review-verify-debug`.
3. "Fix the typo in the README." Trivial, reversible, deterministic. Just do it.

Also bypass for one-rule compliance, tiny reversible tested changes, and emergency
containment. In an incident, contain the harm first, record the temporary choice, then run
this skill on the lasting decision.
## Pick the Mode

| The request is shaped like | Mode | Hands back |
|---|---|---|
| Broad, ambiguous, strategic, premise-sensitive question | 1. Deep exploration | Research brief with a chosen thesis |
| A fork whose answer depends on what happens afterwards | 2. Timeline simulation | Scenario map and decision filter |
| A contested technical choice in a codebase, several agents | 3. Structured debate | One shared debate file, converged or parked |
| An idea for a feature, component or behaviour change | 4. Brainstorm to design | Approved design document |
| An approved design or spec for multi-step work | 5. Write a plan | Plan file a zero-context reader can run |
| A written plan with no progress yet | 6. Execute a plan | Batch reports, stop events, finished work |
| "Do we need a new agent or skill for this?" | 7. Roadmap gap analysis | Candidate dossier with Now, Next, Later, Merge or Reject |

The modes chain. The usual orders are:

- Explore (1), then simulate (2) from the evidence, then decide.
- Explore (1), then debate (3) when the remaining disagreement is technical and inspectable.
- Brainstorm (4), then write the plan (5), then execute (6).
- Gap analysis (7) uses 1 for evidence and 2 for the build-or-extend fork.

Route by the shape of the problem, not by keywords. Do not start a timeline before the facts
are gathered. Do not start implementation while the thesis still depends on missing facts.
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
## Mode 1: Deep Exploration

Use for rigorous analysis, deeper context, strategic options, premise checking, thesis
testing, creative but defensible alternatives, or a nuanced answer that must go beyond a
summary and separate sourced facts from inference.

### Workflow

1. **Calibrate the task.** Identify the real objective, the output shape, time sensitivity
   and domain boundaries. If there is a material ambiguity, flawed premise or missing
   constraint, state it plainly and ask a targeted clarification question. If the prompt is
   workable, proceed without ceremony.
2. **Build an expert council.** Choose 3 to 5 lenses that fit the task. Always include one
   skeptical or adversarial lens that attacks assumptions and weak evidence. Keep lenses
   domain-relevant. Avoid theatrical persona naming.
3. **Map the solution space.** Start with the conventional approach. Generate three
   non-obvious alternatives, ideally by blending the problem with a distant but useful
   domain. Evaluate the tradeoffs and choose the best path or a hybrid.
4. **Gather and separate evidence.** Prefer primary sources and current information when
   stakes or freshness matter. Distinguish sourced facts, reasoned inference and speculation.
   Surface what would change the conclusion.
5. **Run structured challenge.** The skeptical lens challenges the leading approach. The
   other lenses respond with counter-evidence or constraints. Synthesize into a single
   working thesis.
6. **Verify before finalizing.** Write fact-checkable verification questions for the main
   claims. Answer them from available evidence. Revise if verification exposes gaps or
   overstatement.

### Lens menu

Pick 3 to 5: domain specialist; historian or precedent analyst; operator or implementer;
economist or incentive analyst; user or stakeholder advocate; policy, ethics or governance;
skeptical engineer or devil's advocate (always present). Each lens must contribute something
the others do not. Replace a lens when the controlling issue changes, for example economist
to regulator when compliance becomes decisive. Do not rerun the same five.

### Skeptical lens questions

- Which premise is weakest?
- What evidence would falsify the leading claim?
- What has been ignored because it is inconvenient?
- What breaks at scale, under stress, or in edge cases?
- What would a critic say is naive, overstated, or underspecified?

### Conceptual blending prompts

Blend the problem with: ecology or evolution; logistics or supply chains; game design or
behavioural incentives; safety engineering or reliability design; urban planning,
architecture or networks. Explain each blend. The blend should improve the solution, not
decorate it.

### Verification pass

1. What are the 3 to 7 most important factual claims?
2. What evidence supports each?
3. Which claims are inference rather than direct evidence?
4. What counterexample would most damage the conclusion?
5. What minimal revision would make the answer more accurate?

The 3 to 7 checks apply to factual claims. A value judgment or a claim about the future
cannot be settled by checking a fact: validate it with scenarios (does the conclusion hold
under each plausible case?) or with the stakeholders whose values it rests on, and say
which was used. When checking, do not cite a source that only repeats the claim under test
(circular citation), and do not pick the counterexample that is easiest to dismiss. Use the
one that would do the most damage.

Keep a claim ledger while doing this:

```markdown
| id | claim | class (fact / inference / speculation) | source and date | strongest contrary evidence | check result | revision made | what would invalidate it |
|---|---|---|---|---|---|---|---|
```

### Sizing

| Situation | Form |
|---|---|
| Consequential multi-path decision | Full council, all seven output sections |
| Small but non-trivial question | Same logic compressed into fewer sections |
| One loaded assumption | Premise check only, then answer |
| Central claim is freshness-sensitive | Research first (if permitted), then the rest |
| Central fact cannot be obtained | Conditional thesis: "if X holds, then A; otherwise B" |
| Narrow, workable prompt | Direct answer |
| Research not permitted and claim cannot be narrowed | Defer and say what is needed |

If browsing is not allowed or not available: use the provided evidence, narrow or condition
the claim, label background knowledge as unverified, ask for authorization, or defer.

### Output order

`Premise Check`, `Expert Lenses`, `Candidate Approaches`, `Chosen Thesis`,
`Evidence and Verification`, `Final Synthesis`, `Open Questions`. Compress for smaller tasks.

### Templates

Research brief:

```markdown
## Premise Check
- Assumptions that appear sound
- Assumptions that need correction or clarification

## Expert Lenses
- Domain expert
- Operator or implementer
- Skeptical reviewer

## Candidate Approaches
1. Conventional path
2. Alternative path
3. Blended path

## Chosen Thesis
- Recommended direction
- Why it wins

## Evidence and Verification
- Key facts with source links
- Key inferences marked clearly
- Verification questions and answers

## Final Synthesis
- Short, decisive conclusion

## Open Questions
- Question, and which decision it would change
```

Strategy comparison (use when the user needs a choice, a recommendation or a roadmap):

```markdown
| option | upside | downside | risk | evidence strength |
| --- | --- | --- | --- | --- |
```

Creative-but-defensible exploration (use when the user explicitly wants novelty, fresh
thinking or differentiated strategy):

```markdown
## Conventional Approach
- What most teams would do

## Non-Obvious Alternatives
- Alternative A: blend with distant domain
- Alternative B: blend with distant domain
- Alternative C: blend with distant domain

## Best Hybrid
- Selected elements
- Why this combination is superior
```

Verification checklist:

- Are the main claims tied to evidence?
- Are uncertainties explicit?
- Are alternatives compared fairly?
- Did the skeptical lens materially change the answer?
- Is the final recommendation actionable?

The final answer should be deeper than a summary, more honest than a sales pitch, more
structured than a brainstorm, and more useful than a literature dump.
## Mode 2: Timeline Simulation

Use when the right answer depends on how different choices unfold over time: a decision, an
architecture choice, a strategy question, a career move, a difficult conversation; scenario
planning, risk comparison, regret analysis. Build 3 to 5 plausible timelines and compare
them. Timelines are reasoning scaffolds, not forecasts. Judge the comparison, not the
prediction.

### Workflow

1. **Frame the decision.** Identify the actual fork in the road. Capture goals, values, hard
   constraints, and what would count as a win and as a failure. The frame matters most: if
   the real fork is "now versus after the deadline", three fine rewrite-versus-refactor paths
   answer the wrong question.
2. **Choose the horizon.** First week, first month, first quarter, first year, or whatever
   fits. The week, month and quarter rows in the template are defaults. Rewrite them for a
   decade-scale decision.
3. **Build the timelines.** Give each path a clear label. Start from a concrete action that
   could be taken tomorrow. Explain the causal chain step by step: month one must follow from
   week one. Include likely reactions from other people, teams or systems. Give each
   likelihood a reason, not an adjective.
4. **Add the lived-experience layer.** Stress, relief, attention cost and daily reality, not
   only the abstract outcome. This is the step most often skipped under deadline.
5. **Compare across timelines.** Upside, downside, reversibility, regret risk and variance.
   Surface the inflection points where small changes create different branches.
6. **End with a decision filter.** Recommend the most robust path, or the next experiment
   that would collapse the uncertainty.

### Count and proportion

- Three to five timelines. Fewer than three invites confirmation. More than five dilutes
  attention. Add `Timeline D` and `Timeline E` only when the problem needs them, and say why.
  Never pad.
- A genuinely binary, low-stakes fork may get a labelled two-path sketch. That is a stated
  deviation, not the default. One confident answer with no alternative is a failure.
- A real fork is required. If the paths converge, report a false fork: there is no material
  decision.
- Routine fork: workflow only. High stakes (the wrong branch costs days or more) or a need
  for stable structure: fill the template field by field, not as prose under headings.

### Guardrails

- Do not confuse unlikely stories with useful scenarios. A catastrophe path is allowed only
  to cover an unbounded-regret tail, and is labelled as such. Vivid is not likely.
- Do not hide assumptions. State them. One hidden premise shared by every path produces
  agreement around an error.
- Do not skip the emotional or operational cost of a path.
- If source-backed research is needed first, run Mode 1 and simulate from the evidence.
- Simulate one fork at a time. Record downstream forks as inflection points and come back.
- Draft before the decision. A timeline written afterwards is documentation.

### Decision filter

Answer all three and keep them separate:

1. Which path is strongest if everything goes normally?
2. Which path is safest if things go badly?
3. What experiment or conversation would reduce uncertainty fastest?

When 1 and 2 name different paths, say so: "A wins normally, B wins badly." That tension is
often the finding. The owner, or an explicit risk policy, weighs it. If the filter cannot
separate the paths, the answer is the experiment in 3.

### Output order

`Decision Frame`, `Timeline A`, `Timeline B`, `Timeline C`, `Cross-Timeline Analysis`,
`Decision Filter`.

### Template

```markdown
## Decision Frame

- Fork in the road:
- Desired outcome:
- Hard constraints:
- Time horizon:
- What would count as failure:
- Assumptions shared by every path:

## Timeline A: [Short Name]

- Opening move:
- Week 1:
- Month 1:
- Quarter 1:
- Long-term shape:
- Likelihood:
- Stress points:
- Inflection points:

## Timeline B: [Short Name]

- Opening move:
- Week 1:
- Month 1:
- Quarter 1:
- Long-term shape:
- Likelihood:
- Stress points:
- Inflection points:

## Timeline C: [Short Name]

- Opening move:
- Week 1:
- Month 1:
- Quarter 1:
- Long-term shape:
- Likelihood:
- Stress points:
- Inflection points:

## Cross-Timeline Analysis

| path | upside | downside | reversibility | regret risk | variance | who/what has to cooperate |
| --- | --- | --- | --- | --- | --- | --- |

## Decision Filter

- Which path is strongest if everything goes normally?
- Which path is safest if things go badly?
- What experiment or conversation would reduce uncertainty fastest?

## Decision Record (append when the choice is made)

- Chosen path:
- Filter answers at the time:
- Assumptions relied on:
- Signals to watch (leading indicators, reversal triggers):
- Override, if the chosen path is not the one the filter favoured, and why:
```

The original comparison table has six columns and no `variance` column, while the workflow
requires variance. The workflow governs, so the column is added here. Drop it only when the
user asks for the original six-column layout. `Assumptions shared by every path` and the
decision record are additions that serve the "state assumptions" guardrail.
## Mode 3: Structured Debate

Use when multiple agents (for example Codex, Claude, Gemini) should inspect the same
codebase question and converge on the strongest evidence-backed answer: comparing
architecture options, challenging a refactor, adversarial code review, a non-trivial
implementation tradeoff.

### When to debate

- There are at least two plausible implementation paths.
- The decision affects architecture, dependencies or operational risk.
- A normal single-pass review is likely to miss tradeoffs.
- The user explicitly wants multiple agents or adversarial review.

Do not debate trivial edits, simple lookups or fully deterministic tasks. For a reversible
dependency choice, one dissenting reviewer or a disposable experiment is usually enough;
escalate to a full debate only when the evidence conflicts and an experiment cannot decide.

Before starting, confirm: one owner; what may be written and what is prohibited; that each
agent can inspect the evidence independently; and what evidence would end the debate.

### Workflow

1. **Frame the debate narrowly.** Convert the request into one concrete debate question.
   State the scope, non-negotiable constraints and relevant files. Push unrelated ideas to
   the parking lot.
2. **Initialize the shared Markdown file** with `scripts/init_debate_document.py`. Prefer 2
   agents for speed and 3 only when the tradeoff is genuinely unclear.
3. **Generate the next-turn prompt** with `scripts/render_debate_turn_prompt.py`, so each
   participant gets the same guardrails and round context. In manual mode, run it before each
   turn for the current agent.
4. **Ground every claim in evidence.** Cite `file:line`, log output, runtime results or
   concrete counts inline. Unsupported claims do not enter the proposal. Park them.
5. **Edit a living document, not a chat transcript.** Disagree by striking through the exact
   claim and writing the counter directly below it. Tag every substantive edit with a round
   marker such as `[A2-R1]`. Update the dispute log whenever a substantive disagreement
   opens, closes or is parked.
6. **Optimize for the minimum viable fix.** Favor the smallest change that solves the
   observed problem. Reject speculative infrastructure, premature abstraction and monitoring
   without evidence of need.
7. **Converge explicitly.** Do not mark `STATUS: CONVERGED` while any dispute is `OPEN`.
   Close only when all disputes are `CLOSED` or `PARKED` and the proposal is coherent. Any
   agent may revert the proposal to `STATUS: OPEN` and must say why.

### File format

```markdown
# Debate: {TOPIC}

**Created:** {DATE}
**Agent 1:** {AGENT_1}
**Agent 2:** {AGENT_2}
**Agent 3:** {AGENT_3}
**Max Rounds:** {MAX_ROUNDS}
**Status:** OPEN

## Context

{Describe the problem and what is being decided.}

### Evidence

### Relevant Files

### Constraints

---

## Proposal

STATUS: OPEN

---

## Parking Lot

- [A1-R2] issue description

---

## Dispute Log

| Round | Agent | Section | What Changed | Why | Status |
|-------|-------|---------|--------------|-----|--------|
```

- Tags: `[A1-R1]`, `[A2-R1]`, `[A3-R2]`. `A` is the agent number, `R` is the round number.
- Disagreement: `~~struck claim~~`, with the counterpoint on the line directly below.
- Proposal status: `OPEN` or `CONVERGED`. Dispute status: `OPEN` (unresolved), `CLOSED`
  (resolved), `PARKED` (deferred and not blocking convergence).
- Agent 1 writes the first proposal in Round 1. Everyone else reads the current proposal and
  edits in place. Every fix cites exact `file:line`, what the code does now and what it
  should do instead.
- An unused third slot holds `-`.
- When the proposal converges, set the header `**Status:**` line to match.

A worked edit:

```markdown
~~[A1-R1] Polling every 2 s is enough; `src/server/realtime.ts:41` already batches updates.~~
[A2-R1] Counter: `realtime.ts:41-58` batches per connection, not per client. With 3 tabs
open the log shows 3 requests per interval (`logs/dev.log`, 14:02:10 to 14:02:16, 9 requests
in 6 s). Verified by running `npm run dev` and opening three tabs.
```

with the dispute log row
`| 1 | A2 | Proposal | Struck polling-is-enough claim | Batching is per connection | OPEN |`.

### Behaviour in a turn

- Do your own analysis instead of trusting another agent's claim.
- Disagree plainly when the evidence points elsewhere.
- Concede explicitly when another agent's evidence is stronger, and say what you checked.
- Reconcile; never vote. Every material dissent ends as a changed proposal, a gate, a
  rollback step, or a `PARKED` row with an owner.

### Modes and limits

- Manual mode: one terminal per agent, a person passes the turn. Auto mode: an orchestrator
  drives the turns. The upstream project this protocol follows (gumbel-ai/agent-debate)
  ships both, creates debate files from a Markdown template, injects guardrails into agent
  prompts and centres its aliases on Claude, Codex and Gemini. Follow that project's own
  commands only when the user wants parity with it.
- The shared document is the source of truth.
- Final judgment is still human. Local provider authentication and CLI reliability affect an
  orchestrator. The protocol improves rigor; it does not replace reading the code or running
  the tests.
## Mode 4: Brainstorm into an Approved Design

Use before building a feature, a component, new functionality or a behaviour change, when the
intent is still vague. The output is a design a person has approved. The design process is
also the authorization: permission to implement comes from explicit agreement, not from
momentum.

### Workflow

1. **Inspect the context.** Files, documents, recent history. Do not ask what the repository
   can tell you.
2. **Clarify, one question per message.** Purpose, audience, constraints, success criteria,
   non-goals. Prefer multiple choice. Ask the audience question before the layout question.
3. **Offer 2 or 3 credible approaches** with tradeoffs. Lead with the one you recommend and
   say why. Options must differ in substance.
4. **Present the design in sections**, each sized to its difficulty: a few sentences when it
   is straightforward, a few paragraphs when it is not. Cover architecture or composition,
   components, data flow, error states, accessibility where it applies, and testing. Ask
   after each section whether it is right so far. Go back when something does not hold.
5. **Record approval.** Which version, who, when. Cut features that are not needed.
6. **Write the design document** to `docs/plans/YYYY-MM-DD-<topic>-design.md`. Commit it
   only if the repository's rules and the user allow.
7. **Hand off to plan writing (Mode 5).** Not to an implementation tool.

### Sizing

| Situation | Form |
|---|---|
| Novel or high-impact work, much uncertainty | Full design, section by section |
| Small but genuinely creative change | Compact design: a few sentences, still approved |
| A complete design or spec already exists | Validate it: confirm no decision is open, then approve |
| Important context or decisions missing | Continue discovery |
| Approval or a permitted place to write is unavailable | Defer or block, and say so |

Select by novelty, reversibility, blast radius, user availability and open decisions.
Only waive the "2 or 3 approaches" step when the constraints leave one workable design and
the user confirms that.

### Design brief template

```markdown
# <Topic> Design

- Status: draft | approved (version, approver, date)
- User goal:
- Audience:
- Problem:
- Constraints:
- Non-goals:
- Taste rubric or reference examples (for visual or interactive work):

## Options considered
| option | what it is | upside | downside | why chosen or rejected |
|---|---|---|---|---|

## Recommendation

## Design
### Architecture or composition
### Components and data flow
### Flows
### Error states
### Accessibility
### Testing

## Approval events
| section | version | approved by | date |
|---|---|---|---|

## Handoff
- Plan file to be written:
- Open items carried into the plan (none, or list):
```

Low-fidelity exploration artifacts (mood references, rough sketches) are allowed only when
the user has explicitly approved exploratory output. An implementation preview shown early
anchors taste and pushes agreement.
## Mode 7: Roadmap Gap Analysis

Use when someone proposes a new agent, skill, tool or automation, or asks "what should we
build next". Treat each proposal as a hypothesis to be supported by evidence. A gap is a
missing reliable outcome, not an empty slot in a taxonomy. A one-off prompt is not a durable
abstraction. Every new agent adds discovery, maintenance, trigger-overlap and verification
cost.

### Workflow

1. **Frame the gap** as an outcome that is repeatedly not achieved, for a named group of
   users. Not as a tool.
2. **Collect demand evidence**: task logs, support requests, failure records, capability
   audits, repository history, trigger evaluations. Ten representative task traces beat
   borrowed authority. That the ecosystem supports something is not local demand.
   **Pause** if demand cannot be observed, if public analogues are being treated as demand,
   or if the overlap or ownership checks are incomplete. Then do one of: interview the
   users, mine the task history, or validate one narrow manual workflow. A trustworthy
   evidence pipeline may be the first deliverable, not a new agent.
3. **Audit overlap.** Does an existing skill already cover it? Test held-out trigger phrases
   against existing agents.
4. **Size the value**: frequency, cost of failure, urgency, feasibility, owner capacity.
5. **Choose the smallest durable intervention**, in this order of preference: extend or
   merge into an existing skill; add a reference; write a reusable job; change project
   instructions; leave it manual; only then a new agent.
6. **Pilot narrowly and reversibly**, on tasks not used to design it, with a kill criterion
   written first.
7. **Place it**: Now, Next, Later, Merge or Reject. Candidates still being investigated sit
   in Discovery with an expiry date. Later needs an owner and a review date.
8. **Review or retire** on the review date.

Gates follow the cost of discovering a problem late: gap, overlap, value, ownership, pilot,
promotion, recovery. A missing critical item blocks the move to the next state.

### Candidate dossier template

```markdown
# Candidate: <name>

- Gap (missing reliable outcome):
- User cohort:
- Recurrence evidence (traces, dates, counts; say if not measured):
- Cost when the outcome is missed:
- Existing capabilities checked, and overlap found:
- Alternatives considered: extend | merge | reference | job | project instruction | manual
- Chosen intervention and why the smaller ones are not enough:
- Owner:
- Dependencies:
- Pilot: scope, held-out tasks, baseline, duration
- Metrics: numerator, denominator, baseline, threshold
- Kill criteria:
- State: Discovery (expires <date>) | Now | Next | Later (review <date>) | Merge | Reject
- Change-of-mind trigger:
```

Now, Next, Later without evidence is a preference list. Keep rejected candidates and the
reason they were rejected.
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
## Bundled Scripts

Both are plain Python 3 with no dependencies. Run them from the skill directory or give the
full path.

`scripts/init_debate_document.py` creates the shared debate file.

```bash
python3 scripts/init_debate_document.py \
  --path debates/websocket-vs-polling.md \
  --topic "Should this service use WebSockets or polling?" \
  --agent "Codex" \
  --agent "Claude" \
  --max-rounds 3 \
  --context "Real-time updates are required for dashboard clients." \
  --relevant-file "src/server/realtime.ts" \
  --constraint "Do not add a new managed service in v1."
```

| Flag | Meaning |
|---|---|
| `--path` (required) | Output Markdown path. Parent directories are created |
| `--topic` (required) | The debate question |
| `--agent` (required, 2 or 3 times) | Agent display names, in slot order. Otherwise: "Provide 2 or 3 --agent values." |
| `--max-rounds` | Default 3. Must be at least 1 |
| `--context` | Problem statement |
| `--evidence` (repeatable) | Evidence bullets |
| `--relevant-file` (repeatable) | File or `file:line` references |
| `--constraint` (repeatable) | Non-negotiables |
| `--force` | Overwrite. Without it: "Refusing to overwrite existing file: <path>" |

It prints `Created debate file: <path>`. Sections left without input hold a placeholder in
braces; replace every one before Round 1 ends.

`scripts/render_debate_turn_prompt.py` renders the prompt for one agent's turn from the live
file.

```bash
python3 scripts/render_debate_turn_prompt.py \
  --debate-file debates/websocket-vs-polling.md \
  --agent-name "Codex" \
  --round 1
```

| Flag | Meaning |
|---|---|
| `--debate-file` (required) | The debate file. It must exist and hold the five header fields (topic, three agent lines, max rounds) |
| `--agent-name` or `--agent-number` (exactly one) | Name is matched case-insensitively against the header; number is 1, 2 or 3. An empty slot (`-`) is an error |
| `--round` (required) | From 1 to the file's max rounds |
| `--output` | Save the prompt to a file instead of printing; prints `Wrote prompt: <path>` |

The prompt tells the agent to edit the file directly, gives the first-proposal rule to Agent
1 in Round 1 and the edit-in-place rule to everyone else, sets the tag for the turn, and
repeats the evidence, quality and convergence rules. Render it again before every turn so the
round number and the tag are right.
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
