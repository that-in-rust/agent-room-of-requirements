---
name: structured-writing
description: >-
  Structures decision-bearing writing with the Minto pyramid: answer first, an SCQA
  introduction (Situation, Complication, Question, Answer), a Key Line of grouped, ordered
  support, point-driven headings, problem definition (Opening Scene, Disturbing Event, R1,
  R2), yes-or-no issues, logic trees and slide storyboards. Use when the user says "make
  this answer-first", "restructure this draft", "turn these notes into a memo", "apply
  Minto / the pyramid principle / SCQA", "storyboard this deck", "frame the problem
  first", "review the structure", or works on a memo, report, PRD, proposal, RFC, incident
  summary or slide outline (.md, .docx, Marp or reveal Markdown) whose reader must decide
  or act; also to brief another agent top-down. Not for copy editing or tone polish,
  reference or API docs, changelogs, code comments, chat replies, creative prose, slide
  visual design, testable requirements (executable-specs), or choosing between options
  that are still open (explore-and-decide).
---

# Structured Writing

This skill fixes the structure of a document before its prose: it finds the reader's
question, states the answer first, and arranges the support as grouped, ordered ideas that
each answer the question raised by the point above. It covers writing, the problem
definition that precedes analysis, and the storyboard that turns an argument into slides.

Clear writing is clear thinking made visible. When a document is hard to follow, the cause
is usually structure, not sentence style: the writer has not yet made explicit the exact
question, the answer, the grouped ideas that support it, and the order that connects them.

The working implication:

- Structure first, wording second.
- Start from the answer.
- Present from the top down.
- Make every support point earn its place.

What a task gets from it:

- one governing thought instead of topic sprawl
- a clear reader question and answer
- grouped support points with valid logic
- point-driven headings instead of filing labels
- problem-definition framing before deep analysis
- slide or presentation flow derived from the argument

Everything needed to do the job is in this file. Deeper catalogue, extended examples,
failure tables and evidence limits are in [reference.md](reference.md).

## When to Use

Use it when a document has an identifiable reader who must decide or act, and at least one
of these holds:

- Loose notes have to become a memo, report, PRD, proposal, RFC or writeup.
- A flat draft exists but answers no stated question. This is the highest-value trigger,
  because repairing it exercises every rule at once.
- The document opens with background and the answer arrives late or never.
- Headings are filing labels (`Background`, `Findings`, `Recommendations`).
- A list mixes causes, actions, results and evidence.
- Analysis is about to start and nobody has written down the problem.
- A deck has to be built from an argument, or a deck reads like report text on slides.
- Another agent or a subagent needs a brief that will come back top-down.

Requests that should trigger it:

- "Turn this draft into a top-down document with a clear SCQA introduction and Key Line."
- "Here are my notes from the migration spike. Write the recommendation memo for the
  director."
- "This PRD rambles. Restructure it so the decision is on the first screen."
- "We keep collecting data on the outage. Frame the problem first."
- "Storyboard a ten-minute presentation from this report."
- "Review the structure of this proposal. Do not touch the wording yet."

Requests that should not trigger it:

- "Fix the grammar and tighten the sentences in this paragraph." That is copy editing.
  Structure is assumed sound.
- "Write the API reference for this module" or "write the changelog entry." There is no
  reader question to answer. Forcing SCQA onto a changelog is wrong.
- "Make these slides look better." Slide content order belongs here. Slide aesthetics do
  not.

Partial uses are fine and still help: running only the validation checklist on someone
else's finished draft, or using only the SCQA shape for the opening of an email.

Do not open this skill after drafting and jump straight to heading advice. Applying the
method only after the prose exists tends to relabel headings and skip the regrouping. Start
at calibration.

## Pick the Entry Point

| State you are in | Enter at | Hand back |
| --- | --- | --- |
| Subject and answer are at least partly clear | Workflow step 1, top-down build | Worksheet, then document |
| Answer is fuzzy, or only a pile of points exists | Bottom-up build (inside step 1) | Grouped points with one top point, then the workflow |
| A flat draft exists | Step 1 on the draft's implied reader, then rebuild from step 2 | Worksheet, restructured draft, list of points removed |
| Analysis is contested or has not started | Problem definition (Opening Scene, Disturbing Event, R1, R2) | Problem-solving brief, issues, logic tree |
| The deliverable is a deck or talk | Workflow steps 1 to 4, then the storyboard | Storyboard with one stated point per slide |
| Someone else's finished draft, review only | Quality gates | Nine answers, each tied to a passage |
| A one-paragraph note or email | Compressed SCQA only | The note. No worksheet is needed. |
| A brief for another agent | Briefing an agent with a pyramid | Five-line brief |
| A reader exists, but no decision or action is at stake | Do not build a pyramid. Use a narrative format: tell it in the order it happened or the order the reader needs. | The narrative, with a note that the method was not applied and why |
| No reader question exists (reference docs, exploratory notes) | Do not use this skill | Say so and route elsewhere |

Three bounded alternatives cover the cases where the default top-down build does not fit:

- The answer is fuzzy: use the bottom-up pass, then return to the workflow.
- No decision or action is at stake: use a narrative format instead of a pyramid.
- Speed matters more than tailoring: fill a template skeleton and stop there.

How strictly to apply it:

- **Adopt** the full workflow for decision documents and decks, for example a board or
  director recommendation.
- **Adapt** for short or informal pieces: the SCQA may be implied and the tree may be one
  level deep. Never skip calibration.
- **Avoid** for reference documentation and exploratory notes with no reader question, and
  for documents with no decision or action at stake. An exploratory draft without an answer
  is outside the method, not a failure of it. A document without a decision gets a
  narrative format, not a forced SCQA and Key Line.

## Workflow

Six steps. Work on structure as short lines, not paragraphs, until step 5.

### 1. Calibrate the task

- Identify the reader, the deliverable, and the decision or action wanted.
- State the one question the document must answer.
- State the answer in one sentence, as a complete idea and not a topic label.

Record these three lines before anything else. The one-sentence answer is the decisive
check. If it cannot be written, stop expanding downward and switch to the bottom-up build:

1. List the points you believe matter.
2. Work out how they relate.
3. Group like ideas together.
4. Draw the conclusion each grouping implies.
5. Keep moving upward until one top point emerges.

Bottom-up is slower than top-down. It is better than forcing a fake answer too early. Use
it when the subject is unclear, the reader's question is unclear, or the top point does not
yet feel stable.

### 2. Build the introduction

- **Situation**: the first noncontroversial fact about the subject that the reader will
  accept.
- **Complication**: what changed, failed, appeared, or became urgent. Find it by asking of
  the Situation, "Yes, I know that, so what?" The Complication is a trigger in the story. It
  is not always a problem in the narrow sense, and it is not merely a complaint.
- **Question**: the question the Complication makes the reader ask. Make it explicit.
- **Answer**: the top point. State it early.

Recheck: the Complication should trigger the Question naturally. If it does not, then the
Complication is wrong, or the Question is wrong, or the Answer answers a different
question. Fix that before going on. An introduction that creates the wrong question loses
the reader before any support can matter.

Use this flow even if the final prose will imply part of it. For a reader who already lives
in the context, the Situation may be left implied. Keep the Question explicit.

### 3. Build the Key Line

- Ask what new question the Answer raises: usually "Why?", "How?" or "In what ways?"
- Decide whether the support is deductive (an argument) or inductive (a group of similar
  ideas).
- If inductive, name the plural noun for the group: reasons, steps, changes, problems,
  risks.
- Keep sibling points at the same level of abstraction.
- Order them by deductive, time, structural, or degree logic.

What the Key Line usually contains:

| The Answer says | The reader asks | Key Line is usually |
| --- | --- | --- |
| We should do X | Why? or How? | reasons, or changes |
| We can achieve Y | How? | steps |
| Option A is best | Why A? | criteria, or advantages |

### 4. Expand one level at a time

- Ask what question each point raises.
- Answer that question one level down.
- Keep each child group directly responsive to its parent.
- Remove topic labels that are not real ideas.
- Rewrite vague action statements as visible end products.

Default depth is the Key Line plus one expanded level. Stop when every point's question is
answered. A one-page memo may stop at the Key Line when the argument is truly one level
deep.

### 5. Shape the output

- **Prose**: point-driven headings, parallel wording, clear transitions.
- **Analysis**: define the problem before gathering unlimited data.
- **Decision work**: explicit yes-or-no issues, not fuzzy "key issues".
- **Presentations**: storyboard from the introduction, the Key Line, and one level below.

Polish wording only after the structure is sound.

### 6. Validate before finalizing

Run the nine-item checklist under Quality Gates. Answer each question against a specific
passage. The work ends when the structure and the checklist are verified, not when the
prose sounds finished.

## Rules

### The six core rules

Check these on every structured document. They are invariants to check together, not
options to weigh. If any one breaks, the structure is probably wrong.

1. **One governing thought.** The whole document drives toward a single top point. If you
   cannot state the one thing the document says, it is not ready. Everything below
   explains or defends that point.
2. **Top down.** The reader gets the answer before the detail: top point, then Key Line,
   then supporting detail.
3. **Every parent summarizes its children.** If a parent does not summarize its children,
   the grouping is wrong. If the children do not naturally imply the parent, the reasoning
   is wrong.
4. **Siblings are the same kind of idea.** Reasons with reasons, steps with steps, problems
   with problems, changes with changes, conclusions with conclusions. If you cannot name
   the group with one plural noun, the grouping is probably invalid.
5. **Every group is ordered.** There must be a reason why point two is second and not first
   or third. If the order feels arbitrary, the thinking is unfinished.
6. **Every point answers the question above.** Vertical logic is a question-and-answer
   dialogue. A statement raises a question in the reader's mind and the points below answer
   it directly. Do not answer questions before raising them. Do not raise questions you are
   not ready to answer.

Rule 4 is the one most often missed. A list that mixes causes, actions and evidence reads
fine until the plural-noun test fails. When compressing these rules for a prompt, do not
reduce them to "answer first, then support", and do not weaken "same kind of idea" to
"related ideas". That changes the method.

### The six extending rules

These complete the twelve non-negotiables. Apply them in a full review and whenever the
task involves an introduction, actions, or analysis.

7. **Every document needs a proper introduction.** Situation, Complication, Question,
   Answer. The introduction is not background filler. It is the device that creates the
   exact question the document answers and proves you are answering the right one. The
   Answer then raises the new question that the Key Line answers.
8. **Key Line points are ideas, not topics.** Labels such as background, findings,
   recommendations, operations, marketing and issues are buckets. Good Key Line points are
   actual statements.
9. **Inductive groups need a plural noun.** Name the class: reasons, problems, steps,
   changes, opportunities, risks, conclusions. The noun reveals both the logic and the
   misfits.
10. **Action ideas state end products.** "Improve reporting" is too vague. "Install a
    system that gives early notice of change" is testable. If you cannot visualize the
    result of an action, you cannot judge whether the steps are sufficient.
11. **Define the problem before gathering everything.** Do not collect unlimited data and
    hope the structure appears. Define the problem, generate hypotheses, design the
    analysis, and gather only the data needed to prove or disprove the hypotheses.
12. **The reader's question governs the whole document.** The best structure is the one
    that matches the reader's actual question. If the question is wrong, the whole pyramid
    is wrong even if the writing is clean.

### The three substructures

- **Vertical logic.** You make a statement. The reader asks "Why?", "How?" or "Why do you
  say that?" The next level answers. This is what pulls the reader through the argument.
- **Horizontal logic.** Sibling points form either a deductive chain or an inductive group.
  You must know which one you are using.
- **Introductory flow.** Situation is what the reader already knows or will readily accept.
  Complication is what changed or what tension appeared. Question is what that makes the
  reader ask. Answer is the top point.

### Introductions

- Start the Situation with a fact the reader will accept.
- Treat the Complication as a trigger, not just a complaint.
- Make the Question match the answer you actually intend to give.
- Give the Answer early.
- In longer documents, introduce the Key Line points right after the Answer.

Seven common question shapes. Each one is also a reader position; pick the one that is
true and let it choose the structure.

| Reader position | Question |
| --- | --- |
| We have a problem and do not know how to get from R1 to R2 | What should we do? |
| We think we have a solution but are not sure it is right | Is it the right one? |
| We know the solution but not the implementation path | How do we implement it? |
| We tried a solution and it failed | What now? |
| We have several alternatives | Which is best? |
| We know change is needed but cannot define the target state | What should the objective be? |
| We know the target state but are not sure a problem exists | Do we need to act? |

### Deduction and induction

Most confusion in documents comes from mixing these two.

**Deduction**: use it to prove a conclusion. Pattern: a premise, a comment on the premise,
therefore a conclusion.

- The second point must comment on the first.
- The conclusion must follow from the chain.
- Keep the chain short and readable. If it gets long or heavy, break it up.

**Induction**: use it when several similar ideas imply a higher-order insight. Pattern:
group similar ideas, name them with a plural noun, state the significance of the
similarity.

- Can every point be described by the same plural noun?
- Is any point a misfit? Remove it.
- Does the higher point say something specifically about these points, and not about a
  much broader class? Do not infer more than the evidence warrants.

**News is not thinking.** A list of facts is not yet reasoning. Facts belong in the
document only if, together, they explain or defend a higher point.

### Ordering

Once the grouping is right, the order must also be right. Use one visible logic per group.

| Order | Use when |
| --- | --- |
| Deductive | Making an argument |
| Time | Describing sequence, process, cause and effect, or implementation steps |
| Structural | Commenting on parts of a structure, system, geography, organization, or layout |
| Degree | Ranking by importance, size, severity, priority, or magnitude |

### Grouping, summarizing and wording

- **Avoid intellectually blank assertions.** "Improve efficiency", "strengthen
  performance" and "enhance coordination" are too blank to test. Better: "assign planning
  responsibility to the regions", "establish a system for following up overdue accounts",
  "install a reporting system that flags change early".
- **State the effect of actions.** Ask: What will exist when this step is complete? What
  will someone literally have in hand? How will we know the action is done?
- **Make the wording specific.** Specific wording lets you test whether the support points
  are collectively sufficient. "Improve profits" becomes "improve profits by 10 percent by
  January 15".
- **Distinguish levels of action.** Do not mix a result with a substep required to create
  it. Keep the result above the steps that generate it. If siblings include both, split the
  levels.
- **Summarize directly.** A summary states the real message the grouping implies, not a
  placeholder category.
- **Make the inductive leap carefully.** Stay close to the evidence, do not infer more than
  the grouping warrants, and remove ideas that do not fit.

### On the page

Use headings to reveal the structure, not to replace it.

- Reflect the main point in the title.
- Use headings that state ideas, not filing labels.
- Keep points at the same level in parallel grammatical form.
- Keep headings short. Limit wording to the essence of the thought.
- Introduce each group of headings before the headings appear.
- The prose should read smoothly even if the headings were removed. Headings are visual
  signs, not the full carrier of meaning.
- Never use only one of any element in a group: no single subheading, no single bullet.
- Hierarchical headings, decimal numbering, indented display and dot-dash outlines are all
  allowed. Use them only to reveal hierarchy, not to decorate the page.

A `Background` heading that a fixed corporate template requires is tolerable, provided the
answer is stated first.

### Transitions, summaries, conclusions, Next Steps

- Begin each Key Line section with a brief introduction that orients the reader: either a
  short story that leads to the point, or a reference back to the previous section's main
  idea.
- When a section is long or dense, summarize before moving on.
- Write a full conclusion only when needed. It should put the message in perspective,
  reinforce its significance, or create readiness to act and set up the next action. Do
  not end with a limp restatement of what the reader already knows.
- Use a `Next Steps` section only for actions that are obvious once the recommendation is
  accepted, the ones the reader will not argue with. If a step still needs proof, argument
  or defense, it belongs in the body.

## Problem Solving

Pick this part when the task is diagnosis, recommendation design, issue analysis or logic
trees, or when the analysis behind a document is contested. Problem definition comes before
writing.

### Define the problem

Define four elements, then identify the reader's question.

- **Opening Scene** (or Starting Point): the stable structure or process in which the
  problem lives. Keep it simple enough to visualize.
- **Disturbing Event**: what changed, or what became visible, that disturbed the prior
  state. Common kinds: an external change, an internal change, newly recognized evidence of
  a problem or opportunity.
- **R1, Undesired Result**: the result you have and do not want.
- **R2, Desired Result**: the result you want instead. Make it as specific as possible.
  Quantify it when the task allows.

Then place the reader in one of the seven positions in the table above. The document
structure changes to fit the position that is true.

### Diagnose before gathering data

Avoid this habit: gather all available data, label it under generic headings, hope
conclusions emerge later. It looks like diligence. It is the pattern to avoid.

Prefer this habit:

1. Define the problem.
2. Generate likely explanations.
3. Create diagnostic frameworks or logic trees.
4. Gather only the evidence needed to confirm or reject them.

This is more efficient and easier to write up later. (Stated as a design claim. It has not
been measured.)

When breaking down causes or options, make the branches mutually exclusive and
collectively exhaustive. How exhaustive is a judgement: exhaustive enough for the decision
at hand. Do not confuse a random list with a proper analysis tree.

### Logic trees

Use a logic tree to identify possible causes, generate alternative actions or solutions,
test completeness, and reveal flaws in grouped ideas. Build it so each branch reflects a
real analytical choice, not a random topic list.

### Issue analysis

Use issue analysis when you need decision-driving questions. A real issue is usually
phrased as a yes-or-no question.

| Good | Weak |
| --- | --- |
| Is the present inventory level too high? | What are the key issues? |
| Is the centralized ordering system placing orders properly? | How should we reorganize? |
| Should we reorganize functionally? | |

The weak ones may be useful prompts. They do not define a clean decision point.

A section called "Issues" often signals fuzzy thinking. What is usually needed is one of: a
problem definition, a diagnostic framework, a solution logic tree, or a decision
recommendation. If an "issues" section is really a process, a recommendation or an analysis
tree, name it accordingly.

## Presentations

Pick this part when the deliverable is a deck or a talk. A presentation is not a report on
slides. Slides are visual aids inside a live story. Use the pyramid to decide what belongs
on screen and what stays in speech.

Storyboarding workflow:

1. Write the introduction in full.
2. Put the introduction points, the Key Line points, and one level below onto a blank
   storyboard.
3. Sketch how each point should be shown visually.
4. Script the spoken words around the slides.
5. Finish the slide design.
6. Rehearse repeatedly, until the flow is natural.

Slide rules:

- Each slide has a sentence or phrase that states its point.
- Text slides clarify structure.
- Exhibit slides prove a point visually.
- The deck reflects the story flow and stays aligned with the spoken story. It is not a
  data inventory.

Storyboarding multiplies the work per point: each Key Line point becomes slides, script and
rehearsal. Budget for it.

## Briefing an Agent with a Pyramid

This part is an inference from the method, not Minto's own material. The method helps in
AI-assisted work because it forces five things to be explicit: reader, question, answer,
grouped support, logical order. Giving an AI system those five up front reduces drift,
vague prose and context sprawl. (A design claim. Not measured.)

A strong prompt mirrors a pyramid introduction:

```text
Reader: [who will read the output and what they must decide or do]
Question: [the one question they need answered]
Answer we currently believe: [one sentence, or "unknown: build bottom-up from the notes"]
Support points to prove or refine:
- [point 1]
- [point 2]
- [point 3]
Return the output top-down: answer first, then the support points in [time | degree | structural | deductive] order.
```

## Which Procedure to Run

Three procedures describe the same build at different grain. They do not conflict.

| Procedure | Pick it when |
| --- | --- |
| Six-step workflow (above) | Default for any task. It includes shaping for the medium and validation. |
| Nine-step top-down build | You are constructing the pyramid itself and the subject is at least partly clear. |
| Twelve-step operating procedure | A serious document where each decision should be recorded: memo, report, spec, presentation. |

Nine-step top-down build:

1. State the subject. If the subject is fuzzy, the structure will be fuzzy.
2. Decide the reader's question: what should be answered in the reader's mind when they
   finish? Typical: What should we do? Is this the right solution? How should we implement
   it? Which option is best?
3. Write the answer as a complete idea, not a topic label.
4. Identify the Situation: the first noncontroversial thing the reader will agree is true.
5. Develop the Complication by asking "Yes, I know that, so what?"
6. Recheck the Question and Answer against the Complication.
7. Find the new question the Answer raises. This is the Key Line question.
8. Decide whether the support is deductive or inductive. If inductive, name the plural
   noun.
9. Repeat down the pyramid: for each support point, ask what question it raises and answer
   it one level down.

Twelve-step operating procedure:

1. State the subject.
2. Name the reader.
3. Identify the exact question in the reader's mind.
4. Write the answer as one clear top point.
5. Build the Situation and Complication to prove that the question is the right one.
6. Identify the Key Line question raised by the answer.
7. Choose deductive or inductive support.
8. If inductive, name the plural noun.
9. Order the support points logically.
10. Check every parent-child relationship as question and answer.
11. Convert the pyramid into headings, paragraphs, or slides.
12. Polish wording only after the structure is sound.

## Where the Sources Disagree

The owner's notes exist in a longer and a shorter form. Both positions are kept.

| Topic | Position A | Position B | What selects |
| --- | --- | --- | --- |
| Number of non-negotiables | Six core rules | Twelve non-negotiables | Six for a quick structural check on any document. All twelve for a full review, or when introduction, actions or analysis are in play. |
| Procedure | Six-step workflow | Twelve-step operating procedure, with a nine-step build | See the table above. |
| Final checklist | Seven questions | Nine items; a twelve-item list also covers topics versus ideas, problem definition, issues and the ending | Nine is the release gate. Seven is a subset: it skips the child-answers-parent check and silently skips decks. Add the four extra items when the document defines a problem, lists issues, or has a conclusion or Next Steps. |
| Exhaustiveness of a breakdown | Mutually exclusive and collectively exhaustive | Collectively exhaustive enough for the decision | Aim for full coverage when exploring causes. Accept "enough for the decision" when the decision does not turn on the remaining branches, and say which branches were left out. |
| What a conclusion adds | Perspective, significance, desire or readiness to act | Significance, perspective, or set up the next action | Same intent. Use whichever wording fits; never a bare restatement. |
| What qualifies as a Next Step | Actions the reader will not argue with | Actions obvious once the recommendation is accepted | Apply both tests. Failing either sends the step back to the body. |

## Templates

Fill the worksheet before or alongside drafting. A worksheet filled after writing only
rationalizes the draft. A reviewer should be able to validate the argument from the
worksheet alone.

### Structure worksheet

```text
Reader:
Deliverable:
Decision or action wanted:
Subject:
Question:
Answer (one sentence):

Situation:
Complication:

Key Line question (Why? / How? / In what ways?):
Logic (deductive | inductive):
Plural noun (if inductive):
Order (deductive | time | structural | degree):

Key Line:
1.
2.
3.

One level below (question each point raises -> answers):
1. Q:
   -
   -
2. Q:
   -
   -
3. Q:
   -
   -

Points removed as misfits or unsupported:
-
```

### SCQA skeleton

```text
Situation:
Complication:
Question:
Answer:
```

With the meaning of each line:

```text
Situation: Here is the stable context you know.
Complication: Here is what changed, failed, appeared, or became urgent.
Question: Here is what that should make you ask.
Answer: Here is the top point of this document.
```

### Decision memo skeleton

```text
Title: [State the answer]

Situation:
Complication:
Question:
Answer:

Key Line:
- reason/change/step 1
- reason/change/step 2
- reason/change/step 3
```

### Problem-solving brief skeleton

```text
Opening Scene:
Disturbing Event:
R1:
R2:
Question:

Answer:

Support:
- diagnosis
- options
- recommendation
- immediate next steps
```

### Presentation skeleton

```text
Opening story:
Audience question:
Answer:

Slide 1: state the answer
Slide 2: show support point 1
Slide 3: show support point 2
Slide 4: show support point 3
Slide 5: show implication or next steps
```

### A filled worksheet (illustrative)

```text
Reader: Engineering director
Deliverable: One-page recommendation memo
Decision or action wanted: Approve the test-suite split
Subject: Continuous integration for the main repository
Question: How do we make CI results trustworthy again without dropping coverage?
Answer (one sentence): Split the suite into a required fast tier and a nightly full tier,
  and quarantine flaky tests under a named owner.

Situation: Every pull request runs the full test suite before merge.
Complication: The suite now outlasts a review cycle and fails for reasons unrelated to
  the change, so engineers re-run it until it is green.

Key Line question: How?
Logic: inductive
Plural noun: changes
Order: time (each change depends on the one before)

Key Line:
1. Tag every test as fast or full, so the required tier finishes inside a review cycle.
2. Move tests that fail without a code change to a quarantine list that names an owner
   and an expiry date.
3. Run the full tier nightly and open a ticket for the owner on each failure.
```

The memo title becomes the answer: "Split the test suite into two tiers and quarantine
flaky tests". The three changes become the headings, in that order, in parallel form.

## Output Contract

Hand back, in this order:

1. **The calibration lines**: reader, decision or action wanted, question, one-sentence
   answer.
2. **The structure**: the filled worksheet, or for a deck the storyboard, or for diagnosis
   the problem-solving brief with yes-or-no issues. For each group state the logic
   (deductive or inductive), the plural noun if inductive, and the order used.
3. **The deliverable** in its medium: document with point-driven headings, slide outline
   with a stated point per slide, or the review findings.
4. **The gate record**: the nine checklist answers, each with the passage or line it was
   checked against. Per question, not one overall pass or fail.
5. **Open items**: points removed as misfits, claims that still lack support, Next Steps
   moved back into the body, anything the reader's position left undecided.

For a review-only task hand back items 1, 4 and 5, and name the level of each defect:
question, grouping, order, or wording.

For a one-paragraph note, hand back the note. Record nothing else.

Do not report a structure as verified because it "looks Minto-ish". That is not a gate.

## Quality Gates

### Gate 1: the nine-item release checklist

Answer each against a specific passage.

- [ ] Can I state one governing thought, in one sentence?
- [ ] Does the introduction create the exact question being answered?
- [ ] Does each child group answer the question raised above it?
- [ ] Are sibling points the same kind of idea?
- [ ] Is the ordering visible and non-arbitrary?
- [ ] Can each inductive grouping be named by a plural noun?
- [ ] Are action points written as end products?
- [ ] Do the headings tell the same story as the body?
- [ ] If this is a deck, do the slide titles tell the same story as the spoken flow?

Add these when they apply:

- [ ] Are any points only topics instead of ideas?
- [ ] Does the problem definition clearly identify Opening Scene, Disturbing Event, R1 and
      R2?
- [ ] Are "issues" phrased as real decision questions?
- [ ] Does the conclusion or Next Steps section leave the reader knowing what to think or
      do?

How hard to run it:

- Low stakes: spot-check three questions.
- High stakes: a second reviewer answers the nine independently.
- Fastest single gate: can someone else summarize the document as one top point?

These are judgement calls. Two reviewers can disagree on whether headings tell the same
story as the body. Answering all nine "yes" in one sweep, without passages, is checklist
fatigue and does not count.

### Gate 2: mechanical candidate finders

These commands find candidates in a Markdown draft. They do not decide. An empty result
from one of them is not proof that the structure is sound. Set `f` to the draft.

```bash
f=draft.md

# 1. The heading story: read these lines alone. Do they state the argument?
awk '/^(```|~~~)/{c=!c} !c && /^#+ /{print NR": "$0}' "$f"

# 2. Filing-label headings (extend the list for your house style).
grep -n -i -E '^#+ +([0-9.]+ +)?(background|context|overview|introduction|findings|results|analysis|discussion|(key )?issues|recommendations?|operations|marketing|observations|considerations|miscellaneous|other)[[:space:]:]*$' "$f"

# 3. Headings of one or two words: likely topics, not ideas.
awk '/^(```|~~~)/{c=!c} !c && /^#+ /{ if (NF-1 <= 2) print NR": "$0 }' "$f"

# 4. Vague action verbs: each hit needs a visible end product.
grep -n -i -w -E 'improve|strengthen|enhance|optimi[sz]e' "$f"

# 5. List items that are open prompts instead of yes-or-no issues.
grep -n -i -E '^[[:space:]]*([-*+]|[0-9]+[.)])[[:space:]]+(what|how|which|why|where|who)[[:space:]].*\?' "$f"

# 6. A heading with exactly one subheading (never use only one of any element).
awk '
function shut(l,   k){ for(k=6;k>=l;k--){ if(t[k]!="" && n[k]==1) print ln[k]": only one subheading under: "t[k]; t[k]=""; n[k]=0 } }
/^(```|~~~)/{c=!c}
!c && /^#+ /{ match($0,/^#+/); l=RLENGTH; shut(l); for(p=l-1;p>=1;p--) if(t[p]!=""){ n[p]++; break } t[l]=$0; ln[l]=NR; n[l]=0 }
END{ shut(1) }' "$f"

# 7. A list with exactly one item.
awk '
/^(```|~~~)/{c=!c; next} c{next}
{ b = ($0 ~ /^[[:space:]]*([-*+]|[0-9]+[.)])[[:space:]]/) }
b { n++; if(n==1) first=NR": "$0; next }
NF && $0 !~ /^[[:space:]]/ { if(n==1) print first; n=0 }
END{ if(n==1) print first }' "$f"

# 8. The opening: is the answer on the first screen?
sed -n '1,25p' "$f"

# 9. Worksheet fields left blank (run on the worksheet file).
grep -n -E '^[A-Za-z0-9 ./()|?-]+:[[:space:]]*$' worksheet.md
```

Reading the results:

- Command 2 or 3 prints a heading: rewrite it as a statement, unless a fixed template
  forces the label and the answer is already stated first. `Next Steps` is allowed as a
  label when it holds only undisputed actions.
- Command 4 prints a line: apply the three end-product questions.
- Command 5 prints a line: rephrase as a yes-or-no question, or rename the section for
  what it really is.
- Command 6 or 7 prints a line: either the group has a missing sibling or the lone child
  should merge into its parent.
- Command 9 prints a field name: that field is empty, so calibration or the Key Line is
  not finished. `Key Line:` and `Points removed ...:` head a list and always print; ignore
  those two.

### Gate 3: triage order when something fails

Check the question first, then the grouping, then the order. The failures sort by repair
depth: an ordering fix is local, a grouping fix rebuilds a branch, and a wrong question
rebuilds the document. Reviewing only the introduction is a cheap first triage. Do not
reorder bullets under a wrong governing thought.

## Anti-Patterns

| Anti-pattern | What it looks like | Test and repair |
| --- | --- | --- |
| Background before answer | A dump of context before the answer. It hides in politeness: the writer delays the answer to seem thorough. | If the answer is known, state it first. |
| Topic headings instead of ideas | `Background`, `Findings`, `Issues`, `Recommendations` used as if they were thinking | Can the heading be a statement? Write the finding itself. |
| Categories in the Key Line | Buckets where statements should be | Replace each bucket with the point it holds. |
| Mixed abstraction levels | Results, substeps, causes, actions and evidence in one sibling group | Name the plural noun. If none fits, regroup and split levels. |
| Vague action language | improve, strengthen, enhance, optimize with no concrete end state | Name what will exist when the step is done. |
| Data first, structure later | Facts collected with no problem definition or hypothesis tree | Go back to Opening Scene, Disturbing Event, R1, R2. |
| Fake issue lists | A bag of topics called "key issues" | Phrase each as a yes-or-no question, or rename the section. |
| Deduction disguised as induction | Points that are a chain of reasoning, presented as a class of similar ideas | Decide which logic it is and write it as that. |
| Induction without a plural noun | Grouped points that do not belong to one class | Find the noun or remove the misfit. |
| Presentations as visual recitation | Report text on slides: no story flow, no point-driven headlines, no rehearsed script | Storyboard from the introduction and Key Line. |
| Disconnected facts | Facts that do not explain or defend a higher point | Make each child answer its parent's question, or cut it. |
| Polish as repair | Rewriting sentences in a document with mixed groups or no stated question | Repair the diagnosed level first. Prose polish without a structural change is a retry that changes nothing. |
| Worksheet after the fact | Skeleton filled in to match finished prose | Fill it before or alongside drafting. |
| Repeated regrouping of the same notes | A second or third bottom-up build with no new points | The gap is in the problem definition. Go to R1 and R2. A second build is valid only when new points surfaced. |

The weak forms in this table are all normal office prose. That is why the tests are
explicit and why review is a matter of naming, not taste: an invalid structure resists
being named.

## Bundled Scripts

None. The commands under Gate 2 are complete as written and need only `awk`, `grep` and
`sed`.

## Adjacent Skills

- Still choosing between options, or testing whether the premise holds:
  [explore-and-decide](../explore-and-decide/SKILL.md). Come back here to write up the
  decision.
- Writing requirements that map to tests:
  [executable-specs](../executable-specs/SKILL.md). The pyramid can shape a PRD's argument;
  it does not make a clause testable.
- Writing or merging skill and reference files:
  [authoring-skills-and-references](../authoring-skills-and-references/SKILL.md).
- Briefing and coordinating subagents beyond the five-line brief:
  [agent-context-and-orchestration](../agent-context-and-orchestration/SKILL.md).

## Closing Self-Check

Before handing back, confirm each line.

- [ ] The reader, the question and the one-sentence answer are written down.
- [ ] The Complication triggers the Question, and the Answer answers that Question.
- [ ] The answer appears before the background.
- [ ] The Key Line answers the question the Answer raises, and its logic (deductive or
      inductive) is named.
- [ ] Every inductive group has a plural noun, and no sibling is a misfit.
- [ ] Every group has a stated order, and I can say why point two is second.
- [ ] Every heading is a statement, in parallel form with its siblings, and no group has a
      single member.
- [ ] Every action names its end product.
- [ ] Any issues are yes-or-no questions; any problem definition has all four elements.
- [ ] Next Steps holds only undisputed actions; the ending is not a restatement.
- [ ] For a deck: every slide states its point, and the titles alone tell the story.
- [ ] The nine checklist answers are recorded against passages.
- [ ] Wording was polished last.

If the structure is right, the writing usually becomes easy. If the structure is wrong,
better prose only hides the problem.
