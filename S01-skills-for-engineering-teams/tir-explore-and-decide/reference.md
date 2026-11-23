# Explore and Decide: Reference

Depth for [SKILL.md](SKILL.md): the full pattern catalogue, long tables, extended examples,
failure modes, operating guidance and the limits of the evidence. The rules and templates
needed to do the work are in SKILL.md. This file explains why they hold and what to do when
they strain.

## Idiomatic Thesis Synthesis Statement

Exploring and deciding is a correction architecture. Each stage exists so that it can
invalidate something the previous stage produced: the framing, the option set, the evidence,
or the confidence. Depth comes from correction and comparison. It does not come from length,
from the number of personas, or from the volume of sources. A process in which every named
stage is present but none could have changed the conclusion is simulated correction, and it
is the worst failure this subject has.

One operating sequence runs under all seven modes:

1. **Frame** one question, its owner, the options, the consequence and what is reversible.
2. **Retrieve** by claim: the smallest source that can settle each claim that matters.
3. **Classify** every statement as local fact, external fact, or inference.
4. **Challenge** with contradictory and independent evidence.
5. **Decide**: adopt, adapt, avoid, run an experiment, or escalate. A recorded, unresolved
   contradiction is a valid decision state.
6. **Gate** with a command, test, review, rollback or named authority.
7. **Observe** enough to reconstruct the choice later and to invalidate it.

Three statements follow from this and carry most of the weight.

- **A decision is evidence plus authority.** Evidence supports a design or a choice. It does
  not replace the approval of the person who owns it. A design process is also an
  authorization protocol. A test cannot create authority, and an approval cannot make a
  claim true.
- **Disagreement is data.** Never average two sources that disagree, never settle by count,
  and never treat copies of one text as several witnesses. Decide whether the claims are the
  same and which authority governs. Otherwise keep the contradiction visible and take the
  reversible step.
- **Process is sized to the work.** Classify before loading process and take the lightest
  flow that still protects quality. "Lightest" never means skipping the regression test or
  the approval. Over-processing clear work costs ceremony. Under-processing unclear work
  compounds wrong decisions.

Where it fits best: repository-scoped engineering decisions with inspectable evidence and
one owner; strategic questions with several defensible paths; creative or behavioural work
whose constraints can be inspected and whose owner can review choices. Where it is wrong:
trivial edits, urgent containment, and conflicts of authority that only a person can settle.

Timelines are reasoning scaffolds and not forecasts. A debate protocol improves rigor and
does not replace reading code or running tests. A plan is a contract for execution and not a
record of a conversation. None of the methods here has a measured effect on decision
quality; see Evidence Boundary Notes.

## Pattern Scoreboard Ranking Table

The patterns are ordered by dependency, not by measured effect. The source material attaches
the numbers 95, 91 and 88 to the first three. Those numbers are uncalibrated editorial
metadata: they have no denominator, sample or scoring method, and the distances between them
mean nothing. They are shown once here so nobody mistakes them for results.

| Order | Pattern | What it prevents | Applies to | Inherited score (not measured) |
|---|---|---|---|---|
| 1 | Source map first: load the governing local material before synthesis | Context-free, generic advice | All modes | 95 |
| 2 | Evidence boundary split: local fact, external fact, inference | False authority; laundering | All modes | 91 |
| 3 | Verification gate coupling: each recommendation tied to a command, checklist or review | Instructions nobody can check | All modes | 88 |
| 4 | Classify first | Wrong process weight in either direction | 4, 5, 6, 7 | none |
| 5 | Premise check before optimization | Solving the wrong question well | 1, 2 | none |
| 6 | Three to five lenses with one skeptic | A single fluent framing | 1 | none |
| 7 | Conventional path plus three defensible alternatives | A narrowed option space | 1, 4 | none |
| 8 | Three to five timelines with a three-question filter | Advice by vibe; hidden regret | 2 | none |
| 9 | Living shared document with strikethrough, tags and a dispute log | Chat-transcript debates; empty agreement | 3 | none |
| 10 | Minimum viable fix | Speculative infrastructure | 3, 5 | none |
| 11 | Explicit convergence and explicit approval | False convergence; building on assumed consent | 3, 4 | none |
| 12 | Exact paths, complete code, expected output | Decisions deferred to the executor | 5 | none |
| 13 | Batches of three with a report and a wait | Defects compounding unseen | 6 | none |
| 14 | Stop at blockers | Corrupted deliverables | 6 | none |
| 15 | Proposal as hypothesis; pilot before promotion | Agents built from one interesting prompt | 7 | none |

How to read the order:

- Patterns 1 to 3 are prerequisites. Applied alone, the third gives form without meaning,
  and the first gives knowledge that does not control any action.
- Later sourcing cannot repair a misframed objective or an option space that was narrowed
  too early. That is why 4 and 5 come before 6 to 8.
- Patterns 12 to 14, with classification, cover routing, specification, execution and
  exception handling independently. Three of them done well do not compensate for the
  fourth failing. Misclassification has the widest blast radius.

When to change the order: when one binding policy already settles which source governs,
start at the boundary split. When production risk is high, bring the gate forward. When
sources conflict, pause for the owner or for an experiment before anything else.

When numbers create false precision, use an unscored dependency graph or a risk-weighted
matrix. Rank by the cost of a mistake nobody can trace, by reversibility, and by the
independence of the evidence. Any future score needs published criteria, a sample, named
reviewers and a sensitivity check.

## Agent Usage Decision Guide

### Choosing among the modes

| Signal in the request | Use | Do not use |
|---|---|---|
| "rigorous", "deeper", "test the premise", "what are we missing", several defensible paths | Deep exploration | A seven-section performance for a workable narrow prompt |
| "what happens if", "regret", "over the next quarter", "how will they react", a real fork | Timeline simulation | A pros and cons list; a point-in-time fact answer |
| Two implementation paths in code, architecture or dependency risk, "have the agents argue" | Structured debate | A vote; a chat thread |
| "I want to add", "let's build", "what should this look like" | Brainstorm to design | Scaffolding first and asking preferences after |
| Approved design or spec, several dependent steps | Write a plan | "Implement the feature" as a single step |
| A plan file exists | Execute a plan | Running to the end and reporting once |
| "we need an agent for", "what should we build next" | Roadmap gap analysis | Installing something because the ecosystem supports it |

### Deep exploration

Invoke the full form for rigorous analysis, strategic choice, premise checking, thesis
testing, multi-perspective evaluation or defensible alternatives, when several paths,
premises or stakes justify the evidence work. Wrong tool: a narrow direct request, execution
after a settled decision, or freshness-sensitive research that the permissions make
impossible. Alternatives: compress, ask one clarification, answer directly, hand a verified
thesis to timeline simulation, or defer.

Before starting, check: the reason for invoking it, the calibration, whether the ambiguity
is material, the depth, the lens and alternative set, the evidence need, the route afterwards
and the output shape.

### Timeline simulation

Trigger on the shape of the problem, not on the technology: decision, architecture choice,
strategy, difficult conversation, scenario planning, regret analysis, tradeoff clarity.
"Should we migrate?" needs the six contract sections, not a list. Under-invocation looks
like answering a consequence question as if it were a fact. For a request that is really a
simple opinion, ask before running the full machinery. Follow the order strictly: frame,
paths, comparison, filter.

### Structured debate

Debate only when one consequential, genuinely contested, evidence-bearing decision has at
least two plausible options or one material challenge; the cost of choosing wrongly is
meaningful; the agents can inspect independently; and a stopping, experiment or escalation
condition is defined.

Preconditions: one owner; reversible and prohibited boundaries stated; independent evidence
gathered before any shared-state edit; explicit evidence that would end the debate.

Sequence: smallest authoritative source set; brief and boundaries; independent questions
and exclusive writes; assumptions, contrary evidence and a falsifier for each position;
reconcile and never vote; turn every dissent into a gate, a rollback step or an owner
decision; authorize one bounded action and rerun the evidence.

Bypass for spelling, one-rule compliance, tiny reversible tested changes, ideation without a
pending decision, or emergency containment. Prefer direct implementation, a focused review,
or a disposable experiment. Borderline: a reversible dependency choice gets one dissenting
reviewer unless the evidence truly conflicts and an experiment cannot decide.

Success is a packet that names mode, evidence, dissent, action, owner, gate, and stop or
rollback. More agents, more prose or unanimity are not success.

### Brainstorm to design

Invoke before creating features, components, functionality or behaviour changes, and for
other creative work with the same failure shape. Do not use it for non-creative work that
another process governs, or when a complete approved design has no open decision; in that
case validate the supplied design instead of assuming silence is approval. It is blocked,
not skipped, when references or decisions are missing, approval is ambiguous, containment is
urgent, or writing the design down is prohibited. Then: continue clarification, ask for an
allowed place to record the design, or report the conflict.

The guide moves cheap corrections ahead of expensive commitments. It does not exist to slow
work down.

### Plan writing and execution

Open for unclassified work, for a multi-step spec without a plan, or for a written plan with
no progress. Classify, then write, then execute. Direct execution is right for single-step
work. A requester's label ("urgent bug") often signals urgency and not work type, so
classify even when work arrives labelled. Use the subagent-per-task route when the user
chose that handoff.

### Roadmap gap analysis

Invoke only for repeated unmet outcomes or material risk. Apply when comparable tasks show
the same missing reliable outcome, ownership is clear and a pilot can test value. Do not
apply when demand is anecdotal, an existing skill covers it, the problem is specific to one
project, or the proposal starts with a tool. Bypass for one-off prompts, tiny conventions,
brainstorming or urgent remediation; those get direct instructions, a reference, a skill
update, a reusable job or project automation. Keyword routing over-routes. The right result
is often a smaller change to an existing capability.

## Decision Tradeoff Guide

### The four decision modes

| Mode | Choose when | Cost | Check |
|---|---|---|---|
| Adopt | Authority, task fit, boundaries and a falsifiable gate all line up | Fastest; may carry stale assumptions forward | The selected pattern appears in the governing and current evidence |
| Adapt | The safety invariants survive a mismatch that is understood and bounded | Keeps fit; needs explicit inference labels | No invariant, traceability or rollback was weakened |
| Avoid | Evidence is thin, irrelevant or contradictory, or the task is routine | Prevents false confidence; may delay | A confidence warning or an adjacent route is written down |
| Gather evidence | A cheap reversible experiment or source check can discriminate before irreversible work | Time now for less rework later | The experiment can actually separate the options |

Always weigh the cost of being wrong: the wrong files, tests, abstraction, owner or order of
changes; the rework; the recovery; the coordination; the opportunity lost. The reviewer must
know what to undo and what to inspect next.

Do not choose Adapt as a midpoint if it weakens traceability, dissent or rollback. Record
the mode, the criteria, the rejected modes, the uncertainty and the trigger for changing.
There is no universal numeric threshold: reversibility and policy can outweigh the volume
of evidence.

### Tradeoffs inside each mode

| Mode | Tension | How to hold it |
|---|---|---|
| Exploration | Depth versus ceremony | Full council for consequential multi-path decisions; compressed logic for small questions; a premise check alone for one loaded assumption. The mode never relaxes evidence honesty |
| Exploration | Novelty versus defensibility | Keep a blended alternative only if it changes the solution |
| Timeline | Count versus attention | Three to five; justify more than three |
| Timeline | Structure versus flexibility | Workflow only for routine forks; full template when the wrong branch costs days or more. Mandatory fields can suffocate a casual choice and protect a high-stakes one |
| Timeline | Narrative richness versus comparability | Fixed fields inside prose; identical fields make stories mechanically comparable |
| Timeline | Robustness versus optimality | State both filter answers; the owner or an explicit risk policy weighs them |
| Debate | Speed versus coverage | Two agents by default; three when unclear |
| Debate | Convergence versus honesty | Park with an owner instead of forcing agreement |
| Brainstorm | Thoroughness versus fatigue | One question at a time; stop asking when no decision is open |
| Brainstorm | Early visuals versus anchoring | Exploratory artifacts only with explicit approval |
| Plan | Completeness versus plan length | Complete code wins; split long plans at batch boundaries |
| Execution | Flow versus review | Three per batch; other sizes with consent |
| Gap analysis | New versus extend | Extend or merge before new; pilot before promotion; Later when evidence is incomplete; Reject when the gap is weak |

### Process weight

| Class | Process | Budget stated in A01 (asserted, not measured) |
|---|---|---|
| Bug | Reproduce, diagnose, regression test, fix, verify. No plan file | 2 to 4 hours |
| Enhancement | Scope check, light PRD, find the pattern, test-first, review | 1 to 2 days |
| Feature | PRD and architecture tighten each other, then a written plan and batch execution | 1 to 2 weeks |
| Product | Discovery, hypotheses, spikes, smallest useful version, learn | 4 or more weeks |

If unsure between two flows, take the lighter one, record the budget at intake and treat it
as a tripwire. A blown budget suggests misclassification. A budget written down afterwards
is not valid evidence. An enhancement that keeps discovering new rails becomes a Feature.
A scoping spike is the alternative when classification is truly ambiguous. A one-line
enhancement whose rails are certain may defensibly skip the light PRD. The fit of these
budgets to documentation-heavy work is not measured.

For Feature work, an earlier draft of the workflow staged the loop more finely: three PRD
versions and three architecture versions tightening each other, with an anti-pattern filter
before test-first work. The current root document shows two of each. Treat the three-stage
version as optional extra iterations, used when the second architecture pass still removes
scope.

## Theme Specific Artifact

### Deep exploration: the research brief

Full field list for a substantial task: objective; output shape; time and domain bounds;
premise check; rationale for each of the 3 to 5 lenses, including the skeptic; conventional
path; three non-obvious alternatives; tradeoff matrix; evidence ledger; chosen thesis;
structured challenge; 3 to 7 claim checks; revisions made; synthesis; open questions, each
with the decision it would affect.

Exclude hidden chain-of-thought, secrets, irrelevant transcript and unsupported claims.
Every field traces to a user need or a source. The skeptic must materially validate or
change the thesis. Narrow tasks may use a decision memo, the strategy table, the
creative-but-defensible layout, or the verification checklist alone.

The thesis is lossy compression of a challenged solution space. Keep the decisive evidence,
the rejected alternatives and the conditions that would invalidate it.

**What the claim checks can settle.** The 3 to 7 claim checks settle factual claims only.
Value judgments and claims about the future need something else: scenario validation or
stakeholder validation. Test the conclusion under each plausible case, or put it to the
people whose values it depends on. Record which form of validation was used next to the
claim. In the check itself, avoid circular citations (a source that repeats the claim
rather than supporting it) and cherry-picked counterexamples (the weakest objection chosen
because it is easy to answer).

**Trace for a substantial task.** Each recommendation should be traceable through
objective, premise, lenses, options, evidence class, skeptical objection, verification and
revision. For small tasks compress the same logic.

**Modes.**

| Mode | When |
|---|---|
| Full council | Consequential decision with several paths |
| Compressed exploration | Small but non-trivial question |
| Premise check | A loaded assumption is the whole problem |
| Evidence refresh | The central claim is freshness-sensitive and research is authorized |
| Conditional thesis | A needed fact cannot be obtained; state the thesis under each condition |
| Timeline route | The thesis is verified and the remaining question is how it unfolds |
| Direct answer | Narrow workable prompt |
| Defer | Research is not permitted and the claim cannot be narrowed |

Record the selected and rejected modes, the objective, the stakes, the open premise, the
evidence need, the time budget, the change trigger and whether the depth was justified.

**Research without browsing.** Use the provided evidence, narrow or condition the claim,
label background knowledge as unverified, ask for authorization, or defer. Hazards when
researching: the halo of an official source outside its topic, link drift, snippets,
secondary summaries, spillover from an adjacent topic, and gathering citations after the
thesis is fixed. Search outward from the claim ledger, never inward from a convenient link.

### Deep exploration: the older staged protocol

An earlier prompt for the same job ran as four announced phases. It is kept here because
its phase content is sound and because some users ask for it by name. Its presentation
rules conflict with the current ones; SKILL.md, Where the Sources Disagree, says what
selects each.

| Phase | Content |
|---|---|
| 0. Deconstruct and clarify | Identify the core objective, implicit assumptions, domain, complexity and desired output format. State any flawed premise, logical fallacy or significant ambiguity and request clarification before proceeding. If there is none, the older prompt requires the exact sentence "Premise is sound. Proceeding with optimized protocol." Then outline an execution plan naming the reasoning modules to use: simple chain-of-thought, tree-of-thoughts, multi-perspective debate |
| 1. Staging | Allocate 3 to 5 expert personas suited to the task; one must be a "Skeptical Engineer" or "Devil's Advocate" who challenges assumptions and identifies risks; announce the council. Then scaffold the knowledge: outline the domains, concepts and frameworks the answer needs |
| 2. Exploration and synthesis | Divergent brainstorming: outline the most conventional approach; generate three novel alternatives, each by conceptual blending with an unexpected distant domain (the example given is business strategy blended with mycology); explain each blend; evaluate all; select the most promising or a hybrid and justify it. Structured debate: each expert gives a concise opening statement on how to proceed with the selected path; the skeptic challenges the primary assertions; the others respond; a synthesizer role integrates the result into one cohesive, nuanced core thesis |
| 3. Drafting and verification | Write an initial draft from the thesis. Chain of verification: list specific fact-checkable questions covering the key claims, data points and assertions; answer each one by one; identify inconsistencies, errors and weaknesses; produce the final revised response. Factuality and bias: claims are verifiable; results are free from harmful assumptions and stereotypes; anything from outside the given sources is flagged as such, with a note that the user may want to verify it independently |

What carries into the current workflow unchanged: phase 0's deconstruction list; the plan
naming which reasoning module fits; knowledge scaffolding as part of calibration; opening
statements per lens before the challenge; draft first, then verify, then revise; the
factuality and bias rule.

What does not carry by default: the "omniscient superintelligence with an IQ of 1000" role
framing; "world-class" persona announcements; the instruction to articulate the workflow
verbosely; answering verification questions from internal knowledge only. The first is
never used in a final response. The second and third are used only on explicit request. The
fourth is used only when neither sources nor browsing exist, with every answer labelled
unverified.

### Timeline simulation: the scenario map

The template has four parts: a decision frame of five fields, three field-identical
timeline blocks of eight fields each, a comparison table, and three filter blanks. Fill
fields, not prose under headings.

| Part | Fields | Notes |
|---|---|---|
| Decision frame | Fork in the road; desired outcome; hard constraints; time horizon; what would count as failure | Add the assumptions shared by every path |
| Timeline block | Opening move; week 1; month 1; quarter 1; long-term shape; likelihood; stress points; inflection points | Horizon rows are defaults, not doctrine |
| Comparison | Path; upside; downside; reversibility; regret risk; who or what has to cooperate | The workflow also requires variance; add the column |
| Decision filter | Strongest if normal; safest if bad; fastest uncertainty-reducing experiment or conversation | Never merge the first two |

The cooperation column is what makes the template work for difficult conversations: the
other person's likely reaction is part of the causal chain.

The artifact is a scenario map with assumptions, leading indicators and reversal triggers.
At choice time append a decision record: chosen path, filter answers, assumptions, signals,
and any override. Revisit it when a watched signal fires. The record prevents hindsight
rewriting. Choosing a path the filter did not favour is valid; hiding that corrupts later
calibration. Keep the losing paths, because they tell you what to watch.

Vocabulary may change in derived work ("scenarios" for timelines, "decision matrix" for the
comparison) as long as the functions, the stated assumptions and the two-sided filter
remain.

**What timelines do not do.** One fork at a time. No composed decision trees: simulate the
nearest fork fully, record downstream forks as inflection points, and run again later. No
modelling of an adversary who optimizes against your move beyond likely reactions; that
needs game theory. No aggregation of simultaneous portfolios. No prose where a quantitative
expected-value model is needed; say that the quantitative analysis is missing. A tightly
coupled pair of choices may be treated as one composite fork with four paths. A three-level
prose tree may not.

### Structured debate: the decision record around the file

The debate file is the working surface. Around it, the owner needs a record with these
fields.

| Field | Must contain |
|---|---|
| Goal, question, owner | Concrete outcome; one choice that evidence can change; who can stop the debate |
| Scope and write boundary | Systems, exclusive files, prohibited actions, reversibility |
| Options and assumptions | Plausible non-straw alternatives and their failure modes |
| Claim ledger | Boundary (local, external, inference), locator, freshness, confidence |
| Counterargument and dissent | The strongest objection; resolved, gated, deferred with an owner, or escalated |
| Convergence | The evidence that permits or prevents a decision; abstaining is allowed |
| Selected action | Only the next bounded implementation or review action |
| Verification gate | Command, test, experiment or reviewer criterion; expected evidence; response to failure |
| Recovery and refresh | Rollback state, escalation owner, evidence that reopens the question |

Every recommendation traces to the ledger or is marked as judgment. Every material dissent
affects the choice, the gate, the rollback or the owner. The stopping rule is written down,
not held in someone's head. A record may be shortened only while it keeps decision,
evidence, challenge, gate and rollback.

**Source roles when agents cite documents.**

| Role | Governs |
|---|---|
| Canonical entry point | Invocation and top-level workflow |
| Supporting detail | Its own narrow mechanic only |
| Legacy | Rationale and history; shows what changed; does not replace by default |
| Duplicate | Nothing extra: identical content is one lineage |
| Conflicting | Kept visible until authority, experiment or the owner resolves it |

Later is not automatically normative. When two copies or versions of a governing document
differ, write a conflict note that names three things: the claim that changed, the role
that governs it (canonical, supporting or legacy), and the rationale for that choice. If
the reason an older rule should win cannot be recovered, keep both readings, avoid
irreversible action and ask the owner. A local file can govern a workflow and still hold a
stale example.

**External material in a debate.** Retrieve public material only when the unresolved issue
is current tool behaviour, instruction format or implementation. Record the address or
query, retrieval date, revision or locator, the claim it supports, any conflict with local
material and the effect on the decision. A capability conflict (the tool cannot do what the
local rule assumes) may need adaptation. A policy conflict needs the owner. External
evidence should falsify a material assumption, not add rows that look authoritative.

### Brainstorm: the design brief

Fields: user goal; audience; problem; constraints; non-goals; taste rubric or examples;
options; recommendation; architecture or composition; flows; error states; accessibility;
tests; approval events; transition to planning.

It is a contract for planning, not conversation memory. Scale the sections to the
complexity and trace each choice to something the user said or approved. Lighter forms: a
concise design note for small work, a storyboard for a visual flow, a decision record for
one settled tradeoff.

Reject: marketing prose; a one-option document; omitted failure states; documentation
written after implementation; aesthetic labels without support ("clean", "modern");
partial or ambiguous approval.

Keep a design ledger linking context facts, user answers, options, tradeoffs, approval,
artifact location and version, and the planning handoff. The user decides the prompt, the
controls, the taste rubric, what triggers regeneration and the final acceptance bar.
External conventions may constrain delivery. They never silently approve aesthetics, scope
or interaction choices.

Routing after approval: image generation, algorithmic art, visual explanation, timeline
analysis, document design, or plan writing. Specialist tools realize a chosen direction;
they must not anchor taste before alternatives are understood. If the next step is not
specific, stay in clarification or use a text storyboard.

### Plan writing: the plan as contract

The operational artifact is a plan file that predates the code, plus the batch reports and
stop events that match it. Required content: header; user goal; architecture; tech stack;
exact paths; complete code; steps of two to five minutes; commands; expected outputs.

Why each rule exists:

| Rule | What happens without it |
|---|---|
| Exact paths | The executor searches, guesses, and edits the wrong file |
| Complete code | A design decision is deferred to someone with less context |
| Expected output, including the expected failure | A test that passes for the wrong reason is accepted |
| Two-to-five-minute steps | A step hides several decisions and a failure cannot be localized |
| Plan saved before code | The plan describes what was done, which proves little |
| Zero-context reader | Knowledge that lives only in the author's head is lost at handoff |

Do not create this artifact for Bug or Enhancement work. Keep a classification record, or
the log of the subagent run, instead.

### Plan execution: reports and stop events

A batch report transfers control to the reviewer. It holds what was implemented, verbatim
verification output and "Ready for feedback." A stop event holds the trigger (missing
dependency, failing test, unclear instruction, repeated verification failure), the output
and the question.

Stop events show the discipline working. A long run with no stops is suspicious, not
successful, if blockers were guessed through. Three stops for missing dependencies mean the
plan template should require a dependency check. Discoveries made while executing are
written back into the plan, or they are lost when the work resumes.

### Roadmap gap analysis: dossier and portfolio board

Dossier fields: gap; cohort; recurrence and task evidence; alternatives; overlap;
opportunity; urgency; feasibility; owner; pilot; state; dependencies; metrics; kill
criteria. Each field needs evidence and each state needs entry and exit criteria. Use a
one-page brief for low-cost candidates and an architecture decision record for a single
implementation choice.

Lifecycle: intake, gap framing, evidence sampling, overlap audit, opportunity sizing,
prioritization, pilot, promotion, review or retirement. Every state yields an inspectable
artifact and can exit to reject, merge, defer or escalate.

| State | Entry requires | Exit |
|---|---|---|
| Discovery | A framed gap and an expiry date | Evidence found, or expiry reached and closed |
| Now | Demand evidence, overlap audit, owner, pilot passed | Promotion, or kill criterion met |
| Next | Evidence and owner present; capacity not yet | Moves to Now, or is re-evaluated |
| Later | Incomplete evidence; owner and review date | Review date: promote, merge or reject |
| Merge | Overlap audit shows an existing capability covers most of it | Existing skill extended |
| Reject | Weak gap, anecdotal demand, or failed pilot | Reason recorded and kept |

The smallest durable intervention wins. Other actions besides a new agent: Extend, Merge,
Reference, Job, Project Instruction, Manual. A reference is right when reusable reasoning
does not need autonomy. A pilot of about two weeks may precede Merge or New; the duration
is a judgment, not a measured optimum. Sunk cost and urgency bias promotion.

**When demand cannot be observed.** Pause the analysis in any of three cases: demand cannot
be observed; public analogues are being treated as demand; the overlap or ownership checks
are incomplete. Then do one of: interview the users, mine the task history, or validate one
narrow manual workflow. The candidate stays in Discovery with its expiry date while this
happens. A trustworthy evidence pipeline may be the first deliverable, not a new agent.

A roadmap file that exists but is empty proves only that the roadmap is unresolved. Do not
infer demand or ranking from a file name. The absence of roadmap content is itself a
governance gap. The pause rule above applies: build the way of collecting demand evidence
first.

### Evidence labels and the claim record

Three labels are used across the source material. They are foundations, not proof.

| Label | Meaning | Requires |
|---|---|---|
| `local_corpus_sourced_fact` | A statement taken directly from local material | Exact file and version, preferably heading or line. Gives provenance and possible authority, not infallibility or currency |
| `external_research_sourced_fact` | A statement taken from a retrieved public source | Address, retrieval date, revision, locator. A mapped but unfetched address is not a current fact |
| `combined_evidence_inference_note` | A recommendation synthesized from the two | Premises, the facts used, conflicts, assumptions, confidence and what would falsify it |

Finer classes when the work needs them: user-provided fact or premise; user-stated
preference; approval event; render observation; observed demand; pilot evidence; background
knowledge; reasoned inference; speculation; contradiction. An unlabelled claim is treated
as inference.

Claim record: claim; boundary; locator; relevance; confidence with a reason; conflict, or
"none within scope"; verification (command, test, experiment, review or authority); the
evidence that would invalidate it.

Labels make revision local: when a source or a preference changes, the claims that depended
on it can be found and redone without discarding the rest. Labels cannot make irrelevant or
unrepresentative evidence stronger, make taste objective, or prove causation. Labels are
stripped when text is reused in a prompt or a packet, so a qualifier such as "asserted, not
measured" must travel next to the number it qualifies.

## Worked Example Set

Each set uses one scenario three ways, so the difference between the cases is one condition
and not a label. A useful exercise for any of them: hand the three traces to a reviewer and
ask for the decisive evidence, the missing control, the unresolved risk and the condition
that would move the borderline case. If the classification depends only on the words
"good" and "bad", the examples are not doing their job.

### Exploration: a platform migration

**Good.** The request is "plan our all-at-once migration to the new platform". The premise
check corrects it: nothing requires all-at-once. Four paths are compared (all-at-once,
phased by service, strangler in front of the old system, stay and harden) through operator,
user, economic, domain and skeptical lenses. The skeptic asks what outage data says about
the old platform; the check shows most incidents come from two services. The thesis narrows
to migrating those two first. The brief records the rejected all-at-once path and the claim
check that removed it.

**Bad.** Five personas with impressive titles are invented, each speaks a paragraph, and
the answer is "microservices". No premise was tested, no claim was checked, and nothing a
lens said could have changed the result.

**Borderline.** Current cost data cannot be researched. The brief gives a conditional
comparison: "if run cost per service is below X, phased wins; otherwise stay and harden",
and names the cost figure as the open question. This is acceptable because the condition
is explicit and the decision owner knows what to obtain. Proceeding conditionally with one
non-critical constraint missing is also acceptable; proceeding with the central fact
missing and no condition stated is not.

The journey question that usually decides the shape early: does cost or reversibility
dominate for this owner?

### Timeline: rewrite versus refactor

**Good.** The frame is checked first and the real fork turns out to be "start now versus
after the release deadline". Three paths: refactor in place now; rewrite on a branch after
the deadline; strangler module starting now. Each opens with something doable tomorrow.
Each states its assumptions (two engineers stay on the team; the release date holds). The
lived layer says the rewrite path means six weeks of double maintenance. The filter says:
strangler is strongest if things go normally; refactor in place is safest if the deadline
slips; a two-day spike on the hardest module would settle which of the two applies. The
plain plausibility of the paths is a feature.

**Bad, variant one (vibe retrofit).** The author already prefers the rewrite. All template
fields are filled fluently, every path shares the unstated premise that the team keeps its
size, and the assumptions line reads "none significant". The structure certifies what it
was built to prevent. Thin or generic assumptions are the tell.

**Bad, variant two (catastrophe theatre).** One path ends in a data-loss disaster described
in vivid detail, and it crowds out the likely outcome, which is mediocre delay.

**Borderline.** Simulating a fictional fork to learn the mechanics. There are no stakes, so
it is acceptable for a first pass only.

The best training fork is a past decision from the learner's own history whose outcome is
known: the simulated timelines can then be graded against what happened. Grading on field
completeness alone teaches nothing, because the failures look identical to the good case at
the structural level. A convergence finding ("every path ends in the same place, so the
choice does not matter") delivered with its evidence is a good result. Three near-identical
timelines pushed to a confident verdict is not.

### Debate: schema change before or with application code

**Good.** The owner frames two options and blocks production changes. One investigator
reads the local migration and deployment rules; another inspects schema dependencies and
backward-compatibility tests; a third challenges the rollback assumptions. Each claim has a
locator. Evidence shows that old application instances coexist during rollout, so deploying
together can break readers. A dissent notes that the compatibility phase adds temporary
complexity; the group turns that dissent into a cleanup checkpoint instead of deleting it.
The owner chooses schema-first compatibility, requires a rehearsal and a rollback test, and
authorizes only that bounded step. A failed rehearsal reopens the decision. Independent
evidence changed the option, disagreement shaped the gates, convergence was not a vote, and
recovery is explicit.

**Bad.** Four agents get the prompt "debate the best migration". All summarize generic
zero-downtime practice, cite the same secondary text and vote for schema-first. Nobody
reads the repository's migration code, the deployment topology or the rollback tooling. The
majority is called convergence and production work begins before a rehearsal. The question
is vague, the perspectives are duplicates, the sources say nothing about local behaviour,
and the gate cannot falsify the choice.

**Borderline.** The migration affects an isolated, disposable environment that can be
recreated in minutes. A full rehearsal of both sequences will show the compatibility
behaviour faster than a debate. The owner writes a short brief, runs both, keeps the
results and has one reviewer challenge the interpretation. A full debate becomes warranted
only if the results conflict, the production topology differs materially, or rollback
cannot be demonstrated. A cheap reversible experiment carries more information than more
discussion.

### Brainstorm: a new editor workflow

**Good.** The agent reads the editor's existing commands, then asks who the feature is
for before asking anything else. Three layouts are offered that differ in information
density, not in colour. The dense layout is recommended for the stated expert audience.
The design is presented in sections; the keyboard and screen-reader states get their own
section and their own approval. The approved version is written down and handed to plan
writing.

**Bad.** The agent scaffolds a panel and then asks what the user would like changed. Or it
clones a public example and calls the result the design. In both, the first coherent
interpretation was treated as user intent, and the cost of changing direction is already
rising.

**Borderline.** The user supplies a complete design. The agent validates it, finds that
only the error states are undecided, asks about those, and records approval. Accepting a
requirements document as the design is right only after confirming no decision is open.
Showing three mood references is right only after the user approves exploratory visuals.

### Plan and execution: one feature

**Good.** The work is classified as a Feature with its budget noted. The plan has the
header, exact paths, complete code, and for each step the command with its expected output,
including the expected FAIL before the implementation. A fresh executor reviews it, raises
one question, runs three tasks, reports verbatim output and waits. Twelve tasks arrive in
four reports. One stop reads "instruction unclear: task 7 names a file that does not
exist"; the plan is corrected and work resumes.

**Bad.** The task is not classified. The plan is improvised and one step reads "implement
the feature". A missing dependency is guessed around. The work is done on `main`.

**Borderline.** A complete plan is executed as one long batch with a single report at the
end. Code is produced, and the loss shows only when late review finds an early mistake
repeated through every later task. Also borderline: an executor silently correcting an
obviously mistyped path. It is low risk and contained, and it still breaks the stop rule;
report it. And: skipping the light requirements note for a bounded one-line enhancement
whose rails are certain is defensible.

The bad cases all move work forward in time: a vague plan defers decisions to the executor,
and a skipped report defers review to the end, where a fix costs most.

### Gap analysis: a proposed new agent

**Good.** Three incident reviews in a row show the same evidence-triage gap. The overlap
audit finds an existing reviewer skill covers half of it. A narrow pilot extends that skill
and is tried on held-out incidents; rework drops in the pilot sample; the extension is
promoted with a review date. Likewise: recurring dependency-upgrade failures lead to
extending an existing maintainer agent after overlap analysis, and repeated release-note
errors go through overlap audit to a limited pilot.

**Bad.** An agent is created from one interesting prompt, approved because its name is new,
and installed. Or a roadmap is produced by searching for "agents needed next".

**Borderline.** Value is plausible and evidence is thin: the candidate stays in Discovery
with an expiry date, or a narrow detector is piloted. When the missing behaviour is one
capability, it is merged into the existing owner. When the reusable part is reasoning that
needs no autonomy, a reference is added instead. A broad pilot may be waived for a tiny
reversible reference update.

## User Journey Scenario

The user is an engineering owner, a consultant or a workshop participant with a concrete
decision pending, some local material, and uncertainty about which path to take. The
journey starts in ambiguity and ends in a bounded action or an explicit reason not to act.

| State | The user's question | Required artifact | Exit condition |
|---|---|---|---|
| Entry | What decision is pending, and who owns it? | One-sentence decision, owner, deadline, consequence | Specific enough that evidence could change an action |
| Boundary | What is reversible, forbidden, or governed by policy? | Scope, write boundary, rollback boundary, authorities | Irreversible work is blocked until its gate exists |
| Options | Which choices or critiques deserve independent treatment? | Option set with assumptions and expected failure modes | Options differ in substance, not wording |
| Evidence | Which claims are relevant and current? | Ranked source list and claim ledger | Each material claim has provenance or is labelled judgment |
| Challenge | What survives adversarial testing? | Positions, counterarguments, disputes, dissent | Disagreement resolved, turned into a gate, or escalated |
| Convergence | What action is justified now? | Decision, rejected options, confidence, owner, stop rule | Owner accepts a bounded action or an explicit abstention |
| Execution | Did reality support the decision? | Fresh command, test, experiment or review result | Gate passes, or execution stops and rolls back |
| Recovery | What changes after failure or new evidence? | Failure class, restored state, changed condition, next route | System is safe and the record is updated |

A journey that ends after collecting links is incomplete. One that reaches implementation
without an owner is unsafe. One that stops at an unresolved contradiction can be correct,
provided state is preserved and the next authority or experiment is named.

Variations by mode:

- **Exploration.** Intake; objective and output calibration; time and domain bounds; one
  targeted clarification if material; premise check; lens selection; conventional and
  non-obvious paths; evidence separation; structured challenge; chosen thesis; verification;
  revision; synthesis; open questions. It fails when the agent asks unnecessary questions,
  hides disagreement, floods the user with lens transcripts, or returns options without
  choosing.
- **Timeline.** Frame; horizon; paths; lived layer; comparison; filter; decision record;
  revisit when a watched signal fires. If the frame changes mid-build, stop and restart from
  the corrected fork. Salvage a built path only if its opening move survives and its chain
  is re-derived.
- **Brainstorm.** Intake; context; one-question clarification; constraints; alternatives;
  recommendation; sectional presentation; revision; approval; design record; planning
  handoff. Return to clarification whenever needed. Risks: fatigue, repeated questions, too
  many options, visual anchoring, vague acceptance.
- **Plan and execute.** Classify; save the plan; fresh executor; mandatory plan review;
  batches of three; stop and ask; report and wait; finish through the branch-completion
  step.
- **Gap analysis.** Intake; gap framing; evidence sampling; overlap audit; sizing;
  prioritization; pilot; promotion; review or retirement. Users ask for solutions instead
  of outcomes, pilots drift to easy tasks, and promotion can lose the original gap metric.
  Retirement and consolidation are proper outcomes, not signs the analysis failed.

Incident response is a boundary case: contain first when delay is unsafe, record the
temporary decision, then run the evidence workflow before the permanent fix. Compliance
work may also need implementation before a full portfolio cycle.

Reconstruction test: an uninvolved reviewer follows each transition, can say why the next
action was allowed, can name the remaining dissent, and can run the recovery path, without
reading a transcript.

## Anti Pattern Registry Table

Detection has to test meaning. The presence of a label, a path or a command proves nothing.
Apply each control at the earliest cheap point: source selection for irrelevant evidence,
claim formation for boundary errors, convergence review for duplicated perspectives,
implementation gating for unsafe writes.

| Anti-pattern | Why it harms | Replacement | How to detect |
|---|---|---|---|
| Context-free summary | Skips local material; generic advice | Load the governing source first | Sample actionable claims; each needs a relevant locator or a reason none governs |
| Unsourced recommendation | Sounds authoritative with no boundary | Label fact, external fact, inference | Check claim-level labels, premises and confidence |
| Unverifiable instruction | Cannot be checked | Couple each recommendation to a gate | The gate can falsify it, and a failure changes something stated |
| Irrelevant-source laundering | A real source cited outside its scope | Review source-to-claim relevance | A reviewer explains the entailment without leaning on title or authority |
| Duplicate-perspective consensus | Agents repeat one source or one argument | Independent evidence and failure models | Compare evidence origins; repeated wording is not support |
| False convergence pressure | Disagreement removed to finish | Dissent disposition gate | Dissent is preserved and visibly changed a test, rollback, escalation or decision |
| Gate without meaning | A command passes but tests something else | Align gate with claim | State the exact claim a failure would invalidate |
| Premature shared-state change | Work starts before evidence and convergence | Evidence before writes | Inspect order of events; stop writes until the owner authorizes one bounded action |
| Uncalibrated objective | The wrong question is answered well | Calibrate objective, output, bounds | Replay the decision path, not the labels |
| Premise laundering | A flawed premise is optimized | Premise test | The brief names a corrected or confirmed premise |
| Irrelevant or theatrical lenses | Appearance of breadth | Lens rationale review | Each lens has a contribution the others lack |
| Straw or duplicate alternatives | No real comparison | Option-distance check | Options differ in mechanism |
| Decorative domain blend | Novelty without use | Keep only blends that change the solution | Remove the blend; if nothing changes, it was decoration |
| Mixed evidence classes | Inference read as fact | Claim ledger | Sample claims and find their class |
| Ceremonial skepticism | Challenge that cannot change anything | Damaging-counterexample review | Thesis diff before and after the challenge |
| Claim checks without revision | Verification theatre | Record the revision | A check that found a gap produced an edit |
| Unsupported certainty | Overstated confidence | State uncertainty and falsifier | Confidence has a reason |
| Hidden reasoning shown, or a summary or literature dump as output | No thesis, or private reasoning leaked | One thesis with rejected alternatives | The final synthesis is a decision |
| Unlikely stories as scenarios | Drama over plausibility | Plausible paths; labelled tail only | Each likelihood has a reason |
| Hidden assumptions in timelines | Agreement around an error | Shared-assumption field | Assumptions are specific, not "none" |
| Skipped lived cost | Abstract-only comparison | Lived-experience layer | Stress points are filled and concrete |
| Single-path advice | Advice by vibe | Three to five paths | Count the paths |
| Path without an executable opening move | Cannot be started | Concrete action for tomorrow | Opening move is an action |
| Comparison that restates the paths | No cross-path insight | Fixed rubric table | Table cells compare; they do not narrate |
| Structure laundering | Format gives authority to a gut answer | Assumptions and causal links | Thin or generic assumptions |
| Catastrophe theatre | Vivid path crowds out the likely one | Label tail risk | Catastrophe path is labelled as tail coverage |
| Empty agreement | Acceptance without checking | Say what was verified | Search the file for bare agreement phrases |
| Scope creep in the proposal | Debate loses its question | Parking lot | Proposal entries all serve the framed question |
| Speculative infrastructure | Cost without observed need | Minimum viable fix | Each element cites an observed problem |
| Skipped context | Questions the repository could answer | Inspect first | First questions are about intent, not facts on disk |
| Bundled questions | Shallow answers; fatigue | One question per message | Count question marks per message |
| Missing alternatives or straw options | One-option document | Two or three real approaches | Options differ in substance |
| Inferred or silent approval | Building on assumed consent | Recorded approval event | Approval names version, person, date |
| Premature implementation | Direction not validated | Design gate | No code or scaffold predates approval |
| Missing design documentation | Decisions live in chat | Design file | The file exists and matches what was approved |
| Random variants | Iteration without criteria | Rubric-driven iteration | Each variant names the criterion it tests |
| Uninspected output | Render defects ship | Look at the rendered artifact | A render check is recorded |
| Process mismatch | Feature ceremony on a bug, or no plan for a feature | Classify first | Classification record exists and fits |
| Vague plan step | Decision deferred to executor | Exact path, code, command, output | Search for "add validation"-style phrases |
| Guessed-through blocker | Corrupted deliverable | Stop and ask | Stops are recorded with triggers |
| Skipped batch report | Defects compound unseen | Report after each batch | Reports per batch |
| Implementation on main | Unreviewed changes on the shared branch | Branch or worktree; consent | Branch name before execution |
| Solution-first proposal | A tool looking for a problem | Frame the gap as an outcome | Dossier starts with a missing outcome and a cohort |
| Duplicate capability or trigger collision | Two skills fight for one request | Overlap audit; held-out triggers | Held-out phrases route to one skill |
| Orphan maintenance | Nobody owns the new thing | Named owner | Owner field is a person or role with capacity |
| Metric-free promotion | Pilot "worked" by assertion | Metrics and kill criteria written first | Baseline and threshold predate the pilot |

Negative tests. Introduce on purpose: an irrelevant citation; an inference with no
premises; two agents using one source; unanimous text with an unresolved risk; a command
unrelated to its claim. For a roadmap candidate: irrelevant demand; duplicate capability;
vague trigger; absent owner; failed pilot; no kill criterion. Each case must fail for its
intended reason. If one passes, fix the detector before trusting the registry.

Low-risk work may use lighter evidence. It may not label judgment as fact. The weight of a
control scales with consequence; honesty about provenance does not.

Roadmap anti-patterns are often interactions across the portfolio, not defects inside one
candidate. Votes favour novelty, and one loud request can pass for recurring demand.

## Verification Gate Command Set

The runnable structural checks for each artifact are in SKILL.md under Quality Gates. This
section covers what a gate must record, what it proves, and the checks for the skill
itself.

**Gate record.** For every gate: the exact command, the working directory, the exit code,
the counts it produced, unresolved failures, and what a failure triggers. A gate that never
changes the action is not operating as a gate.

**What each layer proves.**

| Layer | Proves | Does not prove |
|---|---|---|
| Structural check (sections, counts, status lines) | The artifact has its required shape | That the reasoning is right |
| Trace audit (follow locators by hand) | Claims are tied to the sources named | That the sources are current |
| Behavioural check (run the command the plan names; rehearse the migration) | The specific claim under test | Claims it does not exercise |
| Editorial reread | The artifact reads as one argument | Anything mechanical |
| Value check (held-out tasks, pilot against baseline) | The intervention helps on tasks it was not designed on | Long-term maintenance value |

No layer stands in for another. In particular, no command proves taste, demand or
approval. For visual or interactive work the rendered output must be looked at.

**Checks for this skill's own files.** Run from the skill directory.

```bash
# front matter parses and names the skill
python3 - <<'EOF'
import re, sys
t = open("SKILL.md", encoding="utf-8").read()
m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
assert m, "no front matter"
fm = m.group(1)
assert re.search(r"^name: explore-and-decide$", fm, re.M), "name"
assert re.search(r"^description:", fm, re.M), "description"
assert "Use when" in fm and "Not for" in fm, "triggers"
print("front matter ok")
EOF

# bundled scripts run
python3 scripts/init_debate_document.py --help >/dev/null && echo "init ok"
python3 scripts/render_debate_turn_prompt.py --help >/dev/null && echo "render ok"

# round trip in a scratch directory
d=$(mktemp -d)
python3 scripts/init_debate_document.py --path "$d/debate.md" --topic "T" --agent A --agent B
python3 scripts/render_debate_turn_prompt.py --debate-file "$d/debate.md" --agent-number 2 --round 1 | head -5
python3 scripts/render_debate_turn_prompt.py --debate-file "$d/debate.md" --agent-number 3 --round 1 \
  || echo "expected failure: slot 3 is empty"
python3 scripts/init_debate_document.py --path "$d/debate.md" --topic "T" --agent A --agent B \
  || echo "expected failure: refuses to overwrite"

# relative links resolve
python3 - <<'EOF'
import os, re
for f in ("SKILL.md", "reference.md"):
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", open(f, encoding="utf-8").read()):
        if "://" in target or target.startswith("mailto:"):
            continue
        if not os.path.exists(target):
            print("BROKEN", f, target)
print("links checked")
EOF
```

From the repository root, the navigation and Rust sync check is
`python3 S03-how-to-use-skills/check.py`.

**Gate order for a candidate or a decision.** Follow the cost of finding a problem late:
gap, overlap, value, ownership, pilot, promotion, recovery. For a plan: classification
recorded; each step's verification run and compared with its expected output; each batch
closed with verbatim output and "Ready for feedback."

Common ways a gate lies: the wrong working directory; an ignored exit code; a check aimed
at different files; a metric with no baseline; a pass on a shared corpus reported as a
pass for one item.

## Failure Mode Table

Classify a failure before retrying. Several modes cascade, so stop downstream writes as
soon as an upstream evidence or convergence gate fails. Repair the earliest stage that can
explain the defect: later polish does not fix a wrong objective, and more evidence does not
widen an option space narrowed by duplicate lenses.

| Failure mode | Trigger | Observable signal | Mitigation |
|---|---|---|---|
| Source drift | Guidance changed after the artifact was written | Locator missing; a version diff changes a governing claim; behaviour contradicts the record | Pause the affected action; refresh if authorized; mark affected claims stale |
| Generic advice escapes | Plausible practice copied without local evidence | Recommendations survive when the sources are removed | Block until each material claim has provenance or is bounded judgment |
| Irrelevant-source laundering | An authoritative source on a different topic | Reviewer cannot explain how the source entails the claim | Remove the claim, find a relevant source, or state the uncertainty |
| Duplicate-perspective consensus | Agents share a source or a failure model | Different prose, same premises and citations | Seek independent evidence, or reduce to one analysis plus a targeted challenge |
| False convergence | Completion pressure erases disagreement | Dissent vanishes with no changed evidence, gate or owner decision | Restore dissent; reopen; no writes until disposition is explicit |
| Lost context | A long run forgets scope or intent | Write boundary, owner or stop condition changes without a decision | Checkpoint; reread the current spec and constraints; resume only the next bounded action |
| Fan-out outruns budget | Parallel calls conflict or duplicate | Overlapping writes; repeated retrieval; growing merge work | Stop new fan-out; keep results; one owner per surface; reconcile before retry |
| Ownership ambiguity | Several actors can authorize or edit one artifact | Conflicting decisions with no resolver | Restore exclusive ownership; name one integrator |
| Gate without meaning | Verification passes but tests something else | Nobody can name the claim a failure would falsify | Replace or supplement the gate |
| Premature execution | Work begins before evidence and convergence | A diff predates authorization or open dissent | Stop; restore safe state; audit side effects; rerun the decision gate |
| Evidence access blocked | Source, tool or authority unavailable | A critical claim stays unsupported after bounded retrieval | Narrow to a reversible action, escalate, or abstain |
| Policy conflict treated as technical | Agents try to settle an authority question with implementation evidence | Both options pass technical tests and violate different owners' constraints | Ask the policy owner; tests cannot create authority |
| Decision path left implicit | The reader cannot tell when to adopt, adapt or avoid | Reviewers pick different routes for the same case | Add the decision table, the cost of being wrong, and a route elsewhere |
| Corpus becomes a list | Many sources indexed, none ranked | No statement of which source governs | Classify canonical, supporting, legacy, duplicate, conflicting |
| Calibration failure (exploration) | Objective or output shape misread | Answer is thorough and off-target | One clarification; restate the objective |
| Lens failure | Lenses overlap or are irrelevant | Lenses agree without adding anything | Replace one lens |
| Option failure | Alternatives share one mechanism | Options differ only cosmetically | Generate a mechanism-distinct option |
| Simulated correction | Every stage present, none can alter the conclusion | Thesis identical before and after challenge and verification | Rerun the skeptic with a damaging counterexample; narrow confidence |
| Doctrine dilution (timeline) | Retelling softens "3 to 5, compare, filter" into "consider several options" | The count bound, the comparison and the filter questions are gone | Check for the specifics, not for topical resemblance; send readers to the full rule |
| Structure laundering | A gut answer wears the template | Assumptions thin or "none significant" | Reject; redo from the frame |
| Filter reduction | Derived prompt asks only "which path is best" | One verdict question | Restore both questions and the experiment |
| Forced verdict | Inconclusive comparison pushed into a recommendation because the section must be filled | Confident pick with near-identical paths | Report the false fork, or answer with the experiment |
| Calibration abandonment | Decision records never kept | No way to compare likelihoods with what happened | Start the record at the next decision |
| Missing intent (brainstorm) | Purpose or audience never established | Variants multiply without converging | Return to one question. More variants cannot fix missing intent |
| Absent approval | Agreement assumed | No approval event for the built version | Stop; present; obtain approval. A better render cannot fix absent approval |
| Render defect | Output clipped, unreadable or inaccessible | Seen on inspection | Re-render without reopening approved scope; reopen one decision only if a missing constraint is exposed |
| Tool failure read as design failure | A generation tool fails | Design gets redone needlessly | Separate the two; retry the tool, keep the design |
| Misclassification | Work routed to the wrong flow | Budget blown after real work is sunk; new rails appear mid-task | Reclassify; an enhancement needing new rails is a Feature |
| Plan-gap stranding | The plan omits something the executor needs | Stop worded "instruction unclear" | Revise the plan; never rerun a stranded plan unchanged |
| Blocker guessing | Executor improvises | Deviation found in review | Revert to the last reviewed batch; re-run with the plan fixed |
| Review starvation | Reports skipped or reviewer saturated | An early mistake repeated across batches; approvals with no comments | Smaller batches; fewer concurrent plans |
| False demand | Popularity or an easy sample mistaken for need | One request; no traces | Collect traces. More research cannot fix absent ownership |
| Duplicate scope | A new capability overlaps an old one | Held-out triggers collide | Merge. More agents cannot fix duplicate scope |
| Owner loss; zombie "Later" | Candidate parked with nobody responsible | No owner; review date passed | Assign or reject |
| Pilot bias | Pilot ran on easy or design-time tasks | Result does not hold on new tasks | Rerun on held-out tasks |

To triage a failed plan execution, walk backward: review cadence, then stop handling, then
plan quality, then the original classification. The failures chain: a misclassified
Feature gets no plan, having no plan leaves the executor guessing, and guessing without
review compounds. The earliest guard is worth the most.

After mitigation, reproduce the original signal and rerun only the gate that concerns it.
A cleared symptom is not enough if the cause remains. In a cascade, contain side effects
first, then settle source and ownership questions, then rerun the reasoning.

How often each mode occurs, and how severe it is, has not been measured.

## Workload Model

These are planning heuristics. None is a measured capacity.

| Dimension | Boundary | Pressure point |
|---|---|---|
| Decision scope | One primary task; one governing question | Split when decisions have independent owners or side effects |
| Sources | Up to about 10 files, ranked | Narrow when evidence cannot be ranked. Ten weak sources can be worse than two decisive traces; eleven small sources may be easier than four conflicting systems |
| Delegation | Up to about 3 delegated subtasks, each with its own evidence surface or disjoint writes | Two agents editing one file are riskier than several inspecting disjoint read-only surfaces |
| Integration | One integrator; one owner per artifact, file or theme | Stop when one owner cannot reconcile every result |
| Audit | A written completion audit for every run | Missing audit means the run is not finished |
| Side effects | Shared-state and irreversible actions blocked until convergence and verification | Record order of changes, rollback state, authorization |

Per mode:

- **Exploration.** One governing decision; 3 to 5 lenses including the skeptic; the
  conventional path and three alternatives; 3 to 7 claims verified; sources loaded
  progressively. One owner for premise and synthesis.
- **Timeline.** Template mode takes on the order of an hour of focused work according to
  its source description; that figure is not measured. A two-path sketch for a low-stakes
  fork takes minutes. The lived-experience reflection is the first thing cut under a
  deadline; protect it.
- **Debate.** Two agents by default, three when unclear; a default of three rounds. One
  owner who can stop it.
- **Brainstorm.** One artifact family; about three representative variants; one
  accessibility or readability pass; one way of checking the rendered result. One approval
  owner and one writer of the design document. Three distinct options are usually enough;
  many cosmetic variants add anchoring and fatigue without information.
- **Plan and execute.** One plan, one flow, one work item, one executor, one reviewer.
  Steps of two to five minutes; three tasks per batch.
- **Gap analysis.** One candidate or one tightly related cluster; two investigators may
  audit demand and overlap while one owner writes the dossier. Three agents independently
  reprioritizing one board is the failure case. Use one integrator and disjoint
  investigations and writes. When the portfolios are independent, one flat analysis is the
  wrong shape: use sequential discovery, map-reduce evidence collection, per-candidate
  dossiers, or hierarchical review.

Raw counts predict less than coupling, review burden, ownership collisions and rollback
complexity. Record source rank, dependency edges, active writers, tool-call and time
budgets, the merge owner, unresolved conflicts and checkpoint state. The scarce resource is
coherent attention for reconciliation and judgment, not generation capacity.

Do not split work that shares one safety invariant, a tightly coupled migration order, or
outputs that cannot be reconciled without rebuilding the whole problem.

## Reliability Target

Three classes of target are kept apart so that an uncalibrated number never acquires the
force of policy.

**Hard invariants** (checkable every time):

| Invariant | How to check |
|---|---|
| Every actionable recommendation keeps its evidence boundary visible | Sample each one; trace label and locator. Check relevance, not only presence |
| No unsupported production, security, latency or reliability claim in final guidance | Reject any such claim without a source, stated premises, or an aligned gate |
| Every "avoid" or failure case names rollback, escalation or the next route | Read failure, retry and routing material together |
| Every material dissent is resolved, gated, deferred with an owner, or escalated | Audit the artifact against the selected action |
| Exploration: one skeptical lens; claim-level verification; revision when a gap is exposed; uncertainty disclosed | Thesis diff; claim ledger |
| Timeline: 3 to 5 compared paths (or labelled deviation); the six ordered sections; the four guardrails; all three filter questions kept together | Section and filter checks in SKILL.md |
| Debate: no `CONVERGED` with an `OPEN` dispute | Convergence check in SKILL.md |
| Brainstorm: no implementation before approval; approval names a version; a recovery path to the last approved design | Order of events; approval record |
| Plan: saved before the code; steps carry commands and expected output | Timestamps or history; plan check |
| Execution: plan reviewed first; verbatim output in every report; stop at blockers | Batch reports |
| Gap analysis: owner and kill criteria present before promotion | Dossier |

**Provisional pilot target** (not measured): at least 18 of 20 sampled uses route to the
correct decision mode or the correct neighbouring skill. Twenty observations suit a pilot
review. They do not support a claim about accuracy in general, and "18 of 20" must not be
restated as "90 percent accurate". Keep the raw verdicts so the threshold can be revised.

**Diagnostics** (no pass mark): cases where reviewers disagree about the right route;
agreement between reviewers on a design rubric.

For any empirical target define the sample frame, task class, adjudicator, denominator,
review window and corrective action first.

"One hundred percent" language invites superficial labelling. "Zero unsupported claims" is
a rule about what may ship; it does not assert that review never misses one, and it needs a
definition of what counts as material.

Recovery clarity is a reliability property in its own right. Even when the first choice is
no more accurate, a precise rollback and escalation path shortens and cheapens a wrong
decision. The costliest breach in timeline work is filter reduction, because it hides the
risk preference the paired questions exist to expose.

## Retry Backpressure Guidance

Retry only when the next attempt can produce new information. Classify the failure, change
one relevant condition, bound the attempt, and preserve any side-effect state.

| Failure class | Default retry | Condition that must change | Stop or escalate when |
|---|---|---|---|
| Transient tool failure | One, after confirming the operation is idempotent or read-only | Tool availability, timeout or invocation | Second failure, or uncertain side effects |
| Missing context | One, after loading the exact governing source | The specific missing locator or dependency | Source unavailable, or authorities conflict |
| Stale external evidence | At most one authorized refresh | Retrieval date, revision or source authority | Browsing prohibited; still conflicting; freshness cannot be shown |
| True contradiction | Do not repeat the debate | A discriminating experiment, a higher authority, or a narrower reversible action | No safe discriminator and no owner |
| Ownership or write collision | No parallel retry | Exclusive owner and a clean merge point | Overlapping writes cannot be reconciled safely |
| Failed verification gate | Retry implementation only after diagnosis | Code, assumption or gate alignment | Repeated failure; incomplete rollback; new risk |
| Duplicated perspectives | Do not add copies of the same prompt | An independent source, role or failure model | Independence cannot be had |
| Irreversible or security-sensitive effect | Zero automatic retries | Explicit human authorization and a restored safe state | Authorization absent or restoration unverified |
| Failed plan-step verification | Rerun once | Nothing, for the single rerun | Still failing: stop and report the output |
| Persistent plan gap | None by the executor | The plan is revised by its author | Two failed revisions on the same task: to the user |
| Repeated budget overrun | None | Reclassification | Do not add ceremony to avoid reclassifying |
| Weak exploration result | One bounded pass | One lens replaced, or one claim narrowed | Same failure with no new information |
| Frame error in a timeline | Restart from the corrected fork | The frame | n/a |
| Paths converge | None | n/a: report the false fork | n/a |
| Filter cannot separate paths | None | n/a: the experiment is the answer | n/a |
| Rejected design variant | One targeted question, a narrower scope, or a changed rubric | The criterion | Repeated taste conflict without criteria: owner decision |
| Biased pilot | Rerun on held-out tasks | The task sample | Absent owner, policy contradiction, repeated trigger collision, irreversible damage |

A retry record holds: failure class, hypothesis, changed condition, attempt budget, side
effects, new evidence, gate outcome, and the next stop decision.

Checkpoint after each batch. Reread the current user constraints before a broad rewrite, a
commit, a push or any destructive operation. Stop new generation or implementation while
source coverage, challenge coverage or a verification gate is red.

Good retry: repair one missing locator, rerun once, compare the changed claim ledger; add
held-out tasks after finding selection bias; rerun a failing step once and then raise it
with its output. Bad retry: run the same prompts again and treat repeated agreement as
support; a fifth silent rerun of one verification; regenerate creative variants at random
(identical creative retries erase the rationale). Borderline: retry a timeout only before
any change has been made and only when the operation is known to be safe.

Backpressure protects the quality of reasoning as well as compute. Repetition can look like
convergence while lowering the chance that a contradicting signal gets attention. In plan
execution the relief valve is social: every hard failure goes to the human partner, by
design and not as a last resort. Sunk prototype cost keeps weak candidates alive; a retry
is not the remedy for that.

## Observability Checklist

Record enough structured evidence to reconstruct and challenge the decision without
keeping a raw transcript or anything sensitive.

| Event or field | Minimum record | Why |
|---|---|---|
| Decision identity | Stable name, owner, task class, start and stop | Separates comparable runs; keeps accountability |
| Scope state | Systems in scope, exclusive files, prohibited actions, reversibility | Shows boundary drift |
| Source load | Local path and heading; external date and revision; intentional skips | Provenance and freshness |
| Claim event | Atomic claim with a stable id, label, locator, confidence, conflict status | Traceability from source to decision |
| Position event | Option, assumptions, strongest counterargument, falsifier | Separates independent reasoning from paraphrase |
| Dissent event | Unresolved risk, owner, disposition, gate, expiry | Prevents silent consensus |
| Tool event | Command or tool, purpose, result summary, side effects | Shows fan-out, retries, unsafe changes |
| Verification event | Exact gate, expected result, actual result, interpretation | Connects evidence to action |
| Retry event | Failure class, changed condition, attempt number, outcome | Detects low-information repetition |
| Action event | Authorized bounded action, writer, changed paths, rollback state | Collision and recovery audits |
| Completion event | Selected mode, unresolved risks, next action, stop condition | Handoff without rereading the run |

Per mode, add:

- **Exploration.** Thesis versions; lens rationale; option set and where each came from;
  the strongest challenge; the 3 to 7 verification questions and answers; revisions. Keep
  the rejected option and the claim check that removed it.
- **Timeline.** The decision record; watched signals; any override. When reviewing a past
  simulation, examine disagreements at the level of one comparison cell or one causal link,
  and date them against what was knowable at the time. Without the appended decision
  record, the actual choice and its rationale are the observability hole. A review that
  looks only at the outcome loses the quality of the reasoning.
- **Debate.** The file itself is the log: tags, strikethroughs and the dispute table.
- **Brainstorm.** Questions and answers, options, rubric, revisions, approvals with
  version, render checks. A log with only the final approval, or with failed options
  deleted, cannot be reconstructed.
- **Plan and execute.** Classification and budget; plan path; verbatim batch reports; stop
  events with trigger and resolution.
- **Gap analysis.** Candidate state history; rejected candidates with their overlap
  evidence and kill reason. Leaving out the rejected ones is survivorship bias. A record
  that says only "roadmap reviewed" is not a record. Logs that reward tool volume are
  invalid. Timing may be omitted for one-off work as long as state evidence is kept.

Optional performance fields: input size, ranked source count, tool-call count, reviewer
time, latency of a repeated workflow. Use p50, p95 or p99 only with enough comparable
samples and stable event definitions. A percentile on one run means nothing.

Prefer summaries of command output, changed-file lists, locators and unresolved-risk notes
to raw transcripts. Exclude secrets, private reasoning and unrelated conversation. Follow
the repository's retention and privacy rules.

Reconstruction test: an uninvolved reviewer can say why the decision was made, what
dissent remains, which action was authorized, how to reproduce the gate, and what state to
restore on failure. If not, observability is incomplete however many metrics exist.

## Performance Verification Method

Performance here is the value of a decision workflow at acceptable cost. It is not service
latency, unless the decision being made is about such a system.

**One-run audit.**

- Record start and stop, input size, ranked source count, tool calls, delegated
  investigations, retries, reviewer time and side-effect checkpoints.
- Record quality outcomes: unsupported claims caught, material dissent, reversals before
  action, gate failures, unresolved risk.
- State the baseline, or say why there is none.
- Judge whether the run gave a clearer next action, a stronger stop condition, or cheaper
  recovery than a simpler method would have.

**Repeated-workflow evaluation.**

1. Define comparable task classes and stable start and stop events.
2. Pick a baseline: direct implementation, a targeted review, or experiment-first work.
3. Collect enough cases before reporting percentiles; keep the sample count and the
   distribution.
4. Pair lead time and reviewer effort with gate failures, downstream rework and recovery
   cost.
5. Investigate the adverse cases instead of optimizing one aggregate.
6. Change one workflow control and watch later comparable runs.

**Pass.** A reviewer can identify the right next bounded action, the gate, the owner and
the stop condition without unrelated files, and the quality guards did not weaken to gain
speed.

**Fail.** Implementation starts before workload, reliability and failure boundaries are
explicit; speed comes from suppressing dissent or skipping approval or overlap review;
measured activity cannot be tied to a decision.

Tool-call and time budgets are controls, not targets. A slower debate, a longer design
phase or a slower gap analysis performs better when it causes a cheap reversal before
expensive work, or avoids an unnecessary agent. Avoiding a new agent can be the best
outcome a gap analysis has. A fast literature dump can be useless.

Mode-specific points:

- **Exploration.** Compare the thesis diff and the information gained per pass. An
  inherited reviewer target of "p95 under 10 minutes" exists in the source material. It
  has no data behind it and is not a service objective.
- **Timeline.** Optimize decision quality per unit of deliberation. A fifth path rarely
  changes the filter. A two-day experiment can beat a month of analysis. Screen with three
  paths, then deepen the two finalists.
- **Gap analysis.** Compare Extend against New on held-out tasks and on maintenance. Keep a
  resumable journal for work longer than one focused period. A timebox is acceptable while
  a baseline is being built.

For one-off work use wall time and reviewer decision time directly. No universal threshold
is asserted here. The structure of the measurement is dependable; the values are unknown
until a local baseline exists.

## Scale Boundary Statement

One flat workflow stops being enough when the task spans independent systems, several
authority owners, unbounded discovery, production change with no explicit objective, or
more evidence than one integrator can review.

**Default decomposition.** Split by independent decision and ownership boundary. One
writer per artifact. One integration owner for shared invariants. Parallel evidence
gathering is safe only with disjoint write surfaces and a defined merge order.

**Do not split** a tightly coupled migration order, one security invariant, or a policy
decision whose alternatives share side effects. Delegated pieces can each be coherent and
together violate the global constraint. Centralize the synthesis and parallelize read-only
collection.

**Artifacts required at scale.**

- A decision dependency graph showing shared assumptions and ordering.
- An ownership matrix for evidence, artifacts, authorization and integration.
- A ranked source budget and a stop rule for discovery.
- The list of shared invariants every split must keep.
- The merge order and who resolves conflicts.
- Integration tests or review gates across boundaries.
- Checkpoint and recovery state for long work.

Per mode:

| Mode | Scales by | Does not scale by |
|---|---|---|
| Exploration | Read-only evidence split by independent domain or lens; a shared claim ledger | Several synthesis owners; incompatible evidence standards in one brief |
| Timeline | Running the nearest fork, then the next | Decision trees, adversarial strategy, portfolios (see Theme Specific Artifact) |
| Debate | Separate debates per independent decision | More agents on one question; several writers of the decision record |
| Brainstorm | Splitting illustration and copy after one approved concept; centralizing navigation and splitting page details | Each agent defining the brand; artifacts that share an interaction model, brand rule or accessibility invariant |
| Plan and execute | More plans only up to what the reviewer can read | Reviewer saturation, which turns checkpoints into rubber stamps |
| Gap analysis | Splitting by independent user gap and owner; one portfolio integrator; shared triggers, security rules and lifecycle standards centralized. Independent portfolios: sequential discovery, map-reduce evidence collection, per-candidate dossiers, or hierarchical review | Candidates that share triggers, a safety invariant, migration order or policy ownership; each owner creating overlapping general-purpose agents |

Example: API compatibility and storage compatibility can be investigated independently,
while one migration integrator owns deployment order and rollback. Two investigators
rewriting the same decision record breaks the boundary even when their technical work is
sound. Likewise: split frontend and deployment gaps, and integrate shared authentication
and trigger rules.

In a large codebase, narrow the context with a dependency or source graph before debating.
A long unranked source list is not context. In long work, forgotten ownership, drifted
scope and lost dissent are reliability failures: resume from a checkpoint. Discoveries
made during a resumed plan are written back into the plan.

No file count or agent count marks the boundary. The limit is reached when reconciliation
attention, merge contention and discoverability cost grow faster than the value of
independent evidence.

## Outcome Metrics and Feedback Loops

Metrics answer whether the practice improves decisions at acceptable cost. Do not reward
document length, agent count, lens count, citation volume, variant count, apparent
unanimity, speed gained through pressure, or fewer questions without checking whether
ambiguity was missed. No effect size has been established for anything in this skill.

| Signal | Definition | Reading | Limit |
|---|---|---|---|
| Framing corrections | Material changes to decision, scope, owner or options before the main work | Early correction prevents wasted evidence gathering | Many corrections can mean poor intake |
| Unsupported claims caught | Actionable claims rejected or relabelled before implementation | Evidence controls are working | Few can mean shallow analysis |
| Reversals before action | Decisions changed by challenge, source conflict or experiment before any shared change | Information arrived while change was cheap | A high rate can mean weak framing or indecision |
| Gate failure rate | Bounded actions stopped by their declared gate | Gates can falsify | Too many means poor decisions |
| Downstream rework | Time spent undoing choices | Should fall within comparable task classes | Task mix and project maturity confound it |
| Decision lead time | Framed question to bounded owner decision | Workflow cost | Speed is harmful if dissent is suppressed |
| Unresolved-risk age | Time a material dissent has no gate, owner or escalation | Shows forgotten risk | Separate urgent from low-risk items |
| Clarification quality | Clarifications that changed scope, evidence or action | Fewer and more decisive is good | Raw question count is ambiguous |

Per mode:

- **Exploration.** Material premise corrections; diversity of relevant options;
  claim-to-evidence coverage; inference labelling; skeptical objections that changed or
  strengthened the thesis; verification-driven revisions; confidence calibration; decision
  usefulness; later reversals. Not every change is an improvement, and reviewer agreement
  is not truth.
- **Timeline.** Calibration (coarse buckets such as likely and unlikely against realized
  branches, over dozens of records; percentage precision from prose labels is false rigor);
  inflection-signal hit rate (did watched signals fire before the divergence); how often
  the filter's experiment was run; override honesty (chosen versus recommended, recorded
  plainly). The experiment-execution rate is the most diagnostic: a team that never runs
  the recommended experiment is reading simulations as entertainment. Review quarterly.
  Counting simulations with no revisits is template theatre. One vivid success story is
  motivating and uncalibrated; keep counting.
- **Brainstorm.** Open-decision closure; distinctness of options; approval revisions;
  requirements caught before implementation; rubric improvement; render defects;
  accessibility defects; rework; reviewer effort. Unanchored taste scores and approval
  counts that reward churn are invalid.
- **Plan and execute.** Classification; budgeted against actual time; stop events by
  trigger type; plan gaps found; batches per report. Stop events show the discipline
  working. Zero stops in a long run is suspicious.
- **Gap analysis.** Gap-resolution rate; reuse on held-out tasks; overlap incidents;
  trigger confusion; pilot-to-promotion quality; maintenance burden; retirements;
  downstream rework. High usage can be over-triggering. Low clarification can be missed
  ambiguity. Zero retirements can be weak governance. A successful roadmap may shrink the
  portfolio while closing more gaps. Counting agents created is the vanity metric.

Before collecting any metric define the task class, numerator, denominator, cohort,
baseline, owner, review window and the action taken on adverse movement. For one-off
decisions hold a qualitative after-action review instead of inventing percentages.

Loop: capture the record; review false positives and missed risks; change one control;
sample later comparable decisions. Three stops for missing dependencies mean the plan
template needs a dependency check. Lower stated confidence can go with better decisions.

## Completeness Checklist

Each checked item points at evidence. "It was considered" does not count. Critical
omissions in authority, claim traceability, dissent, action gate, approval or recovery
block completion. Low-risk work may use a shorter artifact. It may not pretend absent
evidence exists.

All modes:

- [ ] User, concrete goal, pending decision, accountable owner and urgency are named.
- [ ] Scope, exclusive write ownership, prohibited actions and the reversible boundary are
      explicit.
- [ ] At least two plausible options exist, or one recommendation faces a material
      challenge. Routine work was routed elsewhere.
- [ ] The smallest relevant source set was loaded, with locators.
- [ ] Copies were deduplicated or compared; conflicts were not merged silently.
- [ ] External content was freshly retrieved with date and revision, or is marked
      unverified.
- [ ] Every actionable claim is labelled; inference shows premises, confidence and what
      would change it.
- [ ] Alternatives include direct execution, targeted review, experiment, deferral and
      escalation where relevant.
- [ ] Counterarguments and failure modes are represented without straw treatment.
- [ ] Every dissent is resolved, gated, deferred with an owner, or escalated.
- [ ] The convergence rule allows abstention and does not rest on a count.
- [ ] The selected action is bounded and names owner, command or test, expected evidence
      and stop condition.
- [ ] Rollback, state restoration and the route to a neighbouring skill are actionable.
- [ ] Mechanical checks pass, followed by a full editorial reread.
- [ ] Any waiver names the item, the rationale, the risk owner, the expiry and the
      compensating control.

Exploration: calibrated objective, output, time and domain; material ambiguity handled;
premise check; 3 to 5 justified lenses with a skeptic; conventional plus three non-obvious
paths; explicit tradeoffs; evidence classes; structured challenge; 3 to 7 claim checks;
resulting revisions; synthesis; open questions; proportional format. Block when a central
claim lacks current evidence, or when the skeptic and the verification could not have
affected the thesis.

Timeline: real fork; horizon; 3 to 5 paths or labelled deviation; opening moves; causal
links; reactions; lived layer; assumptions; five comparison dimensions; inflection points;
three filter answers kept separate; drafted before the decision.

Debate: one question; file initialized; prompts rendered per turn; all edits tagged;
dispute log current; every acceptance says what was verified; no `CONVERGED` with `OPEN`.

Brainstorm (block plan writing unless all are present): context; goal and audience;
constraints and non-goals; answers obtained one question at a time; two or three distinct
options; tradeoffs; recommendation; design sections; error and accessibility states;
explicit approval; document version; handoff. Link every design section to its approval
event, and block when a critical item is removed. Instead of checklist theatre, use
schema validation, severity-weighted review, storyboard checks, or artifact-specific
rubrics.

Plan and execute: classification and budget; header; exact paths; complete code; commands
and expected outputs; plan predates code; plan reviewed; batches of three (watch for
wording drift from "three" to "a few"); verbatim reports; stops recorded.

Gap analysis: gap; cohort; recurrence; cost; alternatives; overlap; intervention; owner;
pilot; metrics; dependencies; kill criteria; review state. Marking demand complete because
one user asked once is the standard false tick. Complete means ready for one transition,
not permanently right.

A checklist is reliable only if a deliberately removed critical item makes the reviewer
stop the next action. Try it.

## Adjacent Reference Routing

Route to the narrowest place that answers the dominant open question, then come back to
integrate. Do not load every neighbour in advance. Record the question before routing. If
the destination does not settle it, stop after one hop and narrow or escalate. When two
topics are tightly coupled, name one integrator and state which takes precedence.

| Open question | Go to | Bring back |
|---|---|---|
| How do I brief, dispatch and reconcile subagents, or keep context small? | [agent-context-and-orchestration](../tir-agent-context-and-prompts/SKILL.md) | One dispatch plan and merge owner |
| How do I find the relevant code before debating it? | [codebase-navigation](../tir-codebase-navigation/SKILL.md) | Ranked files and locators for the claim ledger |
| How do I write the requirement, the acceptance criteria or the spec the plan implements? | [executable-specs](../tir-executable-specs/SKILL.md) | A testable requirement |
| How do I run the red-green-refactor loop inside a task, track progress, or resume? | [tdd-progress-and-resume](../tir-tdd-progress-and-resume/SKILL.md) | A passing test and a resumable journal |
| Something broke; or I need a code review; or I need to verify before claiming done | [review-verify-debug](../tir-code-review/SKILL.md) | Root cause, review findings, or fresh verification output |
| How should a new skill or reference that passed gap analysis be written? | [authoring-skills-and-references](../tir-authoring-skills-and-references/SKILL.md) | The skill, with trigger tests |
| Worktree setup, branch finishing, commits and pull requests | The `git-delivery-flow` skill in this library | A finished branch |
| The approved design calls for images, generative art, a visual explanation or a formatted document | The `generative-art-and-images`, `visual-explainers` or `structured-writing` skill in this library | The realized artifact for render inspection |
| Why is process sized to the work? | [A00](../../A00-LLM-Principles01.md), [A01](../../A01-LLM-Workflow01.md) | The classification and its flow |
| What does a testable contract look like? | [A03](../../A03-Executable-Specs01.md) | The contract format |

Inside this skill:

- Evidence is missing: exploration first, then simulate or debate.
- The question is how a verified thesis unfolds: timeline.
- The remaining dispute is technical and inspectable: debate.
- A difficult conversation is being rehearsed: timeline. It stays here.
- A quantitative expected-value model is needed: nothing here substitutes. Say so.
- The design is approved: plan writing, never straight to an implementation tool.

Good route: send convergence mechanics to the debate rules and bring the stopping rule back
into the decision record; route trigger design to skill authoring after the candidate
passes overlap review. Bad route: send the word "agent" to another overview; generate
images to avoid asking who the audience is. Borderline: combine context and verification
guidance only when the pending decision depends on both.

Routing is a context-budget control. Hand over the chosen thesis, assumptions, evidence
boundary and open questions with the work, so the specialist does not reopen settled
premises or invent context.

## Source Evidence Mapping Table

What each body of source material contributes. Locations are described, not linked: the
original files are being retired, and this skill is their replacement.

| Source | Kind | Contributes | Where it lands |
|---|---|---|---|
| Agent-debate skill for Codex (owner, February 2026 snapshot): skill file | Owner; canonical for debate | Triggers, seven-step workflow, output contract, guardrails | SKILL.md, Mode 3 |
| Same skill: debate template and tag rules | Owner; supporting | File skeleton, tags, strikethrough, statuses | SKILL.md, Mode 3 file format |
| Same skill: evidence and convergence guardrails | Owner; supporting | Evidence standard, simplicity, behaviour, convergence, reopening | SKILL.md, Rules and Mode 3 |
| Same skill: upstream workflow notes | Owner; supporting | Manual and auto modes, typical prompts, limits | SKILL.md, Mode 3 modes and limits |
| Same skill: `init_debate_document.py`, `render_debate_turn_prompt.py` | Owner; executable | The debate file and per-turn prompt | `scripts/`, byte-identical |
| Deep-exploration skill for Codex (owner, March 2026 snapshot): skill file | Owner; canonical for exploration | Six-step workflow, output order, guardrails, research standard | SKILL.md, Mode 1 |
| Same skill: expert-lens and verification playbook | Owner; supporting | Lens menu, skeptic questions, blending prompts, verification pass, final standard | SKILL.md, Mode 1 |
| Same skill: output patterns | Owner; supporting | Research brief, strategy table, creative layout, checklist | SKILL.md, Mode 1 templates |
| Timeline-traverser skill for Codex (owner, April 2026 snapshot): skill file | Owner; canonical for timelines | Six-step workflow, output order, guardrails | SKILL.md, Mode 2 |
| Same skill: comparison template | Owner; supporting | Frame, timeline blocks, table, filter | SKILL.md, Mode 2 template |
| Older "1000 IQ" analysis prompt (owner, February 2026) | Owner; legacy | Four-phase staged protocol; factuality and bias rule | This file, Theme Specific Artifact; SKILL.md, Where the Sources Disagree |
| Debate evidence digest (owner, July 2026) | Owner digest | Operating sequence, source roles, decision modes, decision record, failure and retry tables, metrics | Throughout this file |
| Roadmap gap-analysis digest (owner, July 2026) | Owner digest | Proposal as hypothesis, lifecycle, dossier, states, portfolio failures | SKILL.md, Mode 7; this file |
| Creative planning and ideation digest (owner, July 2026) | Owner digest | Design as authorization, modes, design brief, ledger | SKILL.md, Mode 4; this file |
| Deep-exploration lens digest (owner, July 2026) | Owner digest | Correction architecture, modes, claim ledger, research hazards | SKILL.md, Mode 1; this file |
| Planning and execution digest (owner, July 2026) | Owner digest | Classify first, four rules, plan as contract, triage order | SKILL.md, Modes 5 and 6; this file |
| Timeline simulation digest (owner, July 2026) | Owner digest | Scaffold not forecast, count bound, filter integrity, decision record, limits | SKILL.md, Mode 2; this file |
| [A01](../../A01-LLM-Workflow01.md) (owner, root document) | Owner; canonical for classification | Four work classes, classifier questions, budgets | SKILL.md, Shared Workflow; this file, Decision Tradeoff Guide |
| Brainstorming skill from the superpowers skill collection for Claude | Third party; ideas only, paraphrased | Design gate before building, one question at a time, sectioned presentation, dated design file | SKILL.md, Mode 4 |
| Writing-plans skill, same collection | Third party; ideas only, paraphrased | Zero-context reader, step granularity, plan header, handoff choice | SKILL.md, Mode 5 |
| Executing-plans skill, same collection | Third party; ideas only, paraphrased | Critical review first, batch of three, report and wait, stop conditions | SKILL.md, Mode 6 |
| gumbel-ai/agent-debate (public project) | Third party; named as the upstream of the debate protocol | Shared-file model, manual and auto modes | SKILL.md, Mode 3 |

The plan and design templates in SKILL.md are this library's own wording and examples. The
ideas behind them (test first, exact paths, expected output, small steps) come from the
superpowers collection and are credited above.

## Evidence Boundary Notes

**What rests on what.**

- The debate protocol, the exploration workflow and the timeline workflow are the owner's
  own skills. They are local facts about how the owner works. They are not evidence that
  the methods improve outcomes.
- The behaviour of the two scripts was observed by running them: two or three agents
  required; default of three rounds; refusal to overwrite without `--force`; empty third
  slot rejected by the renderer; round bounded by the file's maximum; agent name matched
  without regard to case. These are measured in the plain sense that the commands were run
  and the output read.
- The digests are editorial synthesis over the same skills. Agreement between a digest and
  its skill is one lineage, not corroboration. Monthly copies of a skill are also one
  lineage.
- The brainstorming, plan-writing and plan-execution practices come from a third-party
  collection. Their claims about what happens when the gate is skipped are that author's
  experience, not measured here.
- No public source was fetched for this skill. Addresses that appear in the source material
  (the Codex guide on AGENTS.md at developers.openai.com, agents.md, the openai/codex
  repository, GitHub Actions documentation) are pointers only. None of them is evidence
  about debate efficacy, creative authority or roadmap priority, and an instruction-file
  convention cannot establish a convergence threshold.

**Numbers and their status.**

| Number | Status |
|---|---|
| Pattern scores 95, 91, 88 | Editorial metadata. No sample, no method. Not measured |
| "At least 18 of 20" routing | Provisional pilot target. Not measured. Not a population accuracy |
| "p95 under 10 minutes" reviewer target | Inherited figure. Not measured. Not a service objective |
| Work-class budgets (2 to 4 hours, 1 to 2 days, 1 to 2 weeks, 4 or more weeks) | Asserted in A01. Not measured here; fit to documentation-heavy work unknown |
| "Hour-scale" for a full timeline template | Source description. Not measured |
| About two weeks for a pilot | Judgment. Not measured |
| 3 to 5 lenses, three alternatives, 3 to 7 claims, 3 to 5 timelines, 2 or 3 agents, 3 rounds, batch of 3, steps of 2 to 5 minutes, 2 or 3 design options | Design choices stated by the sources. Normative, not empirical |
| One task, 10 sources, 3 subtasks | Planning heuristics. Not validated |

**Not established anywhere in the material.** The effect of any of these methods on
decision quality; the frequency or severity of any failure mode; how often plan revision
succeeds on a second attempt; how often timelines converge; which negligent execution
pattern dominates in practice; transfer from graded exercises to real decisions; baseline
decision quality without the practice.

**Known gaps.** The source roadmap inventory for gap analysis was an empty file. The gap
analysis mode is therefore method only: it carries no list of agents to build, and none
should be inferred. The older staged protocol's Phase 0 execution plan names
tree-of-thoughts and multi-perspective debate as modules without defining them beyond what
Phases 2 and 3 show.

**Using labels well.** Good: a convergence rule is cited to the debate rules; applying it
to a migration is labelled inference and gated by a rehearsal. Bad: a paragraph drawn from
several sources labelled as one local fact; a priority labelled as fact. Borderline: a
section-level label when every sentence shares source, scope and confidence. A
recommendation is not "approved" until consent is recorded. Approval does not imply
objective quality, one render does not imply general usability, and a pilot result does not
imply universal demand.

Carry the labels in a form that fits the density of claims: inline citations, footnotes,
provenance columns, claim or decision ledgers, confidence tables, approval receipts, or a
separate evidence appendix. A section label must not cover mixed claims, inference wording
must not hide speculation, and an unfetched address must not become an external fact.
Correct labels do not prove that a source is accurate, that the premises are complete or
that a causal claim is valid. They make revisions local and traceable.

The main ways boundaries fail: label laundering; missing locators; copies counted as
corroboration; conflicts resolved silently; labels lost when text is reused downstream.
Audit by sampling actionable recommendations and asking an uninvolved reviewer to find
source, freshness, premises, conflict status, confidence, verification and invalidation.

## Future Refresh Search Queries

None of these has been run. Browsing needs authorization. Capture every result with
retrieval date, authority, exact locator or revision, the claim it supports, conflicting
evidence and its effect on a decision. Start from the most consequential disputed
inference or the weakest claim in the ledger, never from the theme name. Add date,
jurisdiction, version, population and system boundary to a query where they matter.
Changing a query after a favoured result appears biases the inquiry.

| Purpose | Query | Claim it should test |
|---|---|---|
| Upstream debate protocol | `gumbel-ai agent-debate README manual auto mode` | Whether the shared-file protocol, tags and statuses described here still match the upstream project |
| Debate counter-evidence | `multi-agent debate false convergence evidence software engineering` | Whether debate degrades decisions under some conditions. Treat non-primary results as hypotheses |
| Instruction precedence | `site:developers.openai.com Codex AGENTS.md instruction precedence` | A current instruction-loading assumption an orchestrated debate depends on |
| Implementation behaviour | `repo:openai/codex AGENTS.md discovery precedence` | One behaviour, tied to a revision |
| Third-party workflow drift | `superpowers skills brainstorming writing-plans executing-plans changelog` | Whether the design gate, batch size or handoff options changed upstream |
| Scenario method evidence | `scenario planning decision quality empirical evaluation premortem` | Whether structured scenario comparison has measured effects, and under what conditions |
| Calibration practice | `forecast calibration coarse buckets decision journal evidence` | Whether coarse-bucket calibration over dozens of records is a sound gauge |
| Plan granularity | `implementation plan task granularity LLM coding agent evaluation` | Whether small explicit steps with expected output improve agent execution |
| Capability portfolio | `agent skill trigger overlap evaluation held-out prompts` | Methods for testing trigger collisions between skills |
| Reusable workflow constraints | `GitHub Actions reusing workflow configurations` | Only when a gap analysis ends in a reusable job |

Without the network: compare the copies of a skill across months to see whether they
duplicate, extend or conflict; diff local agent manifests; read repository history; run a
prototype; ask the maintainer. These remain valid when no authoritative public guidance
exists. If none exists, say so, and do not turn the existence of a neighbouring document
into direct evidence.

A good refresh tests one claim. A bad one copies a search summary, counts results, or
searches for "agents needed next". Examples found on GitHub are hypotheses until code,
tests, revision and local applicability have been inspected.
