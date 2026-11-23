# Structured Writing Reference

Depth for [SKILL.md](SKILL.md): the pattern catalogue, worked examples, failure tables,
operating guidance and evidence limits. The rules themselves are in SKILL.md. This file
does not restate them in full; it shows how each one is tested, repaired and scaled.

## Idiomatic Thesis Synthesis Statement

Define the problem, state one answer, and descend by question and answer through named,
ordered, same-kind groups until every point is supported.

Three things follow from that sentence.

- **One mechanism covers writing and problem solving.** The mechanism is the
  question-and-answer dialogue. The introduction creates the first question. Every level
  below answers the question its parent raised. A logic tree is the same dialogue run
  before the evidence is in.
- **Writing failures are thinking failures.** Mixed sibling kinds, arbitrary order, unnamed
  groups and an unanswered reader question are structural defects. Sentence polish cannot
  repair them.
- **Problem definition comes first when the analysis is contested.** The R1-to-R2 framing
  governs the analysis before any writing begins. A thesis that says only "structure the
  document" understates this half.

Two compressions damage the method and should be refused:

- "Answer first, then support." This keeps the top-down rule and drops the same-kind rule,
  which is the rule whose violation is least visible in a finished draft.
- "Group related ideas." Siblings must be the same kind of idea, nameable by one plural
  noun. "Related" is weaker and lets mixed lists through.

A compressed form is acceptable in a short prompt only if the grouping clauses are noted
alongside it.

The method does not apply to free-form narrative. Quoting the thesis as advice for creative
prose is a misuse. The method assumes a reader-directed document with a decision or action
at stake. A document that has a reader but no decision is better served by a narrative
format than by a pyramid.

The pyramid is not just a writing trick. It is a discipline for five things:

- deciding what you are really saying
- forcing the reader's question into the open
- grouping support points into valid logic
- defining problems before analyzing them
- turning analysis into prose, headings and slides without losing the argument

## Pattern Scoreboard Ranking Table

Ranked by repair depth: what it costs to fix the defect once the document exists. The
ranking is a reasoned ordering, not a measurement. How often each rule is violated in real
drafts has not been measured, and no numeric scores are given because none were measured.

The six core rules are diagnostic as a set. A single break signals structural failure, so
check all six on every structured document. The ranking only says where to look first.

| Rank | Pattern | Test | Defect repair depth | Notes |
| --- | --- | --- | --- | --- |
| 1 | Reader's question governs the document | Does the Complication trigger the Question? Does the Answer answer it? | Whole document | A wrong question makes the whole pyramid wrong even if the writing is clean. |
| 2 | One governing thought | Can the document be summarized as one sentence by someone else? | Whole document | Fastest single gate. |
| 3 | SCQA introduction | Is the Situation undisputed? Is the Complication a trigger? | Introduction, sometimes the whole document | Proves the question is the right one. |
| 4 | Same kind of idea in every group | One plural noun names the group | A branch | Most often missed. Mixed lists read fine until the noun test fails. |
| 5 | Parent summarizes children | Do the children, taken together, imply the parent and nothing broader? | A branch | Guards against over-reaching induction. |
| 6 | Children answer the parent's question | State the question the parent raises; check each child answers it | A branch | Removes disconnected facts. |
| 7 | Deductive or inductive, declared | Is it a chain or a class? | A branch | Deduction disguised as induction hides the argument. |
| 8 | Visible order | Why is point two second? | Local | Deductive, time, structural or degree. |
| 9 | Ideas, not topics, in Key Line and headings | Can the heading be a statement? | Local | Mechanical to detect. |
| 10 | End-product actions | What will exist when this is done? | Local | Enables the sufficiency check on steps. |
| 11 | Results above their steps | Is any sibling a substep of another? | Local to a branch | Split the levels. |
| 12 | Yes-or-no issues | Can the issue be answered yes or no? | Local | Otherwise it is a prompt. |
| 13 | Problem defined before data | Are Opening Scene, Disturbing Event, R1 and R2 written? | The analysis, not just the text | Ranks first when the analysis itself is contested. |
| 14 | Storyboard before slides | Does each slide state a point? Do titles alone tell the story? | The deck | Applies only to presentations. |
| 15 | Next Steps holds undisputed actions | Would the reader argue with it? | Local | Disputed steps go back to the body. |

Ways to re-rank later, if records exist: by observed violation frequency, or by measured
repair cost.

## Agent Usage Decision Guide

Open this skill on the act, not on the word "writing": the agent is about to draft,
restructure or review decision-bearing prose or slides.

| Situation | Action |
| --- | --- |
| About to draft a document whose reader must decide or act | Start at calibration, before any prose |
| Loose notes, no clear answer | Bottom-up build, then the workflow |
| Flat draft that answers no stated question | Full rebuild. Highest-value case. |
| Diagnosis, recommendation design, issue analysis, logic trees | Problem definition first |
| Deck or talk | Workflow to the Key Line, then storyboard |
| Finished draft, review only | Nine-item gate, findings by level |
| Email or short note | SCQA shape only |
| Brief for another agent | Five-line pyramid brief |
| A reader exists, but no decision or action is at stake | Do not build a pyramid. Write it in a narrative format and say the method was not applied. |
| Changelog, code comment, chat reply, API reference, exploratory notes, creative prose | Do not use. Say why. |
| Sentence-level polish wanted | Not this skill; a style guide applies |
| Slide mechanics or visual design | Not this skill; presentation tooling applies |

Rules for the agent:

- Calibration is the step most often skipped and the one every later rule assumes. An
  agent that opens the skill after drafting and jumps to heading advice has skipped it.
- Prefer a pattern that comes with a test. Every recommendation the agent makes about a
  draft should name the check that would confirm it: a checklist question, a naming test,
  or a command.
- Keep three kinds of statement apart when reporting: what the owner's notes say, what an
  outside source says, and what the agent inferred.
- Do not key on every mention of writing. That drags the method into changelogs, comments
  and chat, which it does not govern.
- Treat outside sources as a freshness check, not as a replacement for the owner's
  conventions recorded in this skill.

## Decision Tradeoff Guide

### How strictly to apply the method

| Choice | When | Cost | Check |
| --- | --- | --- | --- |
| Adopt the full workflow | A decision is at stake: board or director recommendation, proposal, PRD, decision deck | Time for calibration, worksheet and nine answers | Is the one-sentence answer recorded? Are nine answers tied to passages? |
| Adapt: implied SCQA, shallow tree | Short or informal piece; reader already knows the context | Risk that an implied introduction fails for a cold reader | Name the reader. Is the Question still explicit? |
| Adapt: template skeleton only | Speed matters more than tailoring; routine document | The skeleton caps depth and may not fit the reader position | Does the filled skeleton pass the summarize test? |
| Avoid; use a narrative format | A reader exists, but the document carries no decision or action | The reader gets no answer-first summary, which is correct when there is no answer to give | Is there a decision or action the reader must take? If none, do not force SCQA and a Key Line. |
| Avoid | No reader question: reference docs, exploratory notes, changelogs | None, provided the document is recorded as outside the method | Would any reader ask a single question of this document? |

Never skip calibration, even when compressing everything else.

The default top-down build has three bounded alternatives, each selected by one condition:

| Condition | Alternative |
| --- | --- |
| The answer is fuzzy | Bottom-up pass, then the workflow |
| No decision or action is at stake | Narrative format instead of a pyramid |
| Speed matters more than tailoring | Template skeleton only |

### What being wrong costs

The cost is invisible to the author. A mis-structured memo reads fine to the person who
wrote it and fails only in the reader's unasked question. The price is paid in reader
attention: a document that creates the wrong question loses the reader at the
introduction, before the quality of the support can matter.

### When answer clarity is disputed

A writer who believes the answer is clear may still fail the one-sentence test. Verify
with the test, not with confidence. If the sentence will not come:

1. Use the seven reader positions to select the question shape.
2. If that does not settle it, go to full problem definition.
3. If the analysis itself is contested, pair with a second person.

The level of stakes below which the method can safely be skipped has not been measured.

### When the evidence for a rule is in question

| Evidence state | Choice | Cost | Check |
| --- | --- | --- | --- |
| The owner's notes and current outside sources agree | Adopt | Fastest path, but can copy a stale assumption from both | Does the rule appear in both? |
| The owner's notes are strong but outside guidance has moved | Adapt, with an explicit note that the adaptation is an inference | Keeps fit with the owner's practice; needs the note | Are the note's fact, the outside fact and the inference labelled separately? |
| Evidence is thin, conflicting or unrelated to the task | Avoid; add a confidence warning or route elsewhere | Prevents false confidence; may need more research | Is there a warning or a route? |

Cost of error: when wrong guidance is followed anyway, the result is a wasted loop and
weaker verification. A reviewer should be able to tell what to undo and what to inspect
next.

### Top-down or bottom-up

| | Top-down | Bottom-up |
| --- | --- | --- |
| Use when | Subject at least partly clear; answer can be stated | Subject, question or top point unclear |
| Speed | Faster | Slower; convergence is not guaranteed |
| Risk | Forcing a fake answer too early | Regrouping the same notes without progress |
| Exit | Every point's question is answered | One top point emerges; then switch to top-down |

### Deductive or inductive

| | Deductive | Inductive |
| --- | --- | --- |
| Use when | A conclusion must be proved | Several similar ideas imply a higher insight |
| Shape | Premise, comment on the premise, therefore | Class of same-kind points under one summary |
| Reader load | Must hold the chain in mind; keep it short | Can take each point on its own |
| Typical failure | Chain too long or heavy; second point does not comment on the first | Misfit in the class; summary broader than the points |
| Repair | Break the chain up | Remove the misfit; narrow the summary |

### How exhaustive a breakdown must be

Two positions exist. One says causes and options should be broken down mutually exclusive
and collectively exhaustive. The other says collectively exhaustive enough for the
decision. Aim for full coverage while exploring causes, because a missing branch can hide
the real cause. Accept "enough for the decision" when the remaining branches could not
change the choice, and name the branches left out.

## Theme Specific Artifact

### The pyramid shape

```text
                     Answer (governing thought)
                               |
          reader asks: Why? / How? / In what ways?
                               |
        +----------------------+----------------------+
   Key Line 1             Key Line 2             Key Line 3      <- same kind, ordered
        |                      |                      |
   reader asks            reader asks            reader asks
        |                      |                      |
   +----+----+            +----+----+            +----+----+
  1.1       1.2          2.1       2.2          3.1       3.2    <- each group: same kind, ordered
```

Above the pyramid sits the introduction: Situation, Complication, Question. It exists to
make the reader ask the question that the top box answers.

Read vertically, the pyramid is a dialogue. Read horizontally, each row under one parent
is either a deductive chain or an inductive class.

### Pattern: the question-and-answer dialogue

- **What it is.** Each statement raises one question. The level below answers it and
  nothing else.
- **Test.** Write the question next to the parent. Read each child as an answer to it. A
  child that answers a different question is in the wrong place.
- **Two prohibitions.** Do not answer a question before raising it: the detail has no
  home yet. Do not raise a question you are not ready to answer: the reader will wait for
  it.
- **Stop condition.** Expansion stops when the reader would ask nothing further.

### Pattern: the SCQA introduction

The introduction is the device that creates the question. It proves that the right
question is being answered. It is not generic background.

| Element | Content | Test | Common defect |
| --- | --- | --- | --- |
| Situation | The first noncontroversial fact about the subject | Would the reader nod? | Opens with something disputed, or with history the reader does not need |
| Complication | What changed, failed, appeared or became urgent | Does it answer "Yes, I know that, so what?" | A complaint with no trigger; or a "problem" forced where the trigger is an opportunity |
| Question | What the Complication makes the reader ask | Does it follow from the Complication without help? | Matches the writer's interest, not the reader's |
| Answer | The top point, as a statement | Does it answer exactly that Question? | A topic label; or the answer to a neighbouring question |

When the Complication does not trigger the Question, one of three things is wrong: the
Complication, the Question, or the Answer (it answers a different question).

The Situation may be left implied for a reader who lives in the context. The Question may
not. An implied introduction works for a known reader and fails for a cold one, so any
verdict on an introduction has to name the reader.

In a longer document, the Key Line points are introduced right after the Answer, so the
reader holds the plan of the document before the first section begins.

### Pattern: reader position selects the structure

The seven positions, the question each produces, and the Key Line that usually fits. The
positions and questions come from the owner's notes. The Key Line column extends the three
stated Key Line rules (reasons or changes; steps; criteria or advantages) to the other
positions and is an inference.

| # | Reader position | Question | Key Line usually (inference beyond rows 1, 3, 5) |
| --- | --- | --- | --- |
| 1 | Does not know how to get from R1 to R2 | What should we do? | Changes, or reasons for the recommended action |
| 2 | Thinks they have a solution, unsure it is right | Is it the right one? | Reasons it is or is not; criteria it meets |
| 3 | Knows the solution, not the path | How do we implement it? | Steps, in time order |
| 4 | Tried a solution and it failed | What now? | Causes of the failure, then changes |
| 5 | Has several alternatives | Which is best? | Criteria, or advantages of the chosen option |
| 6 | Knows something is wrong, cannot define the target | What should the objective be? | Conditions the target must satisfy |
| 7 | Knows the target, unsure a problem exists | Do we need to act? | Reasons to act or not; evidence of the gap between R1 and R2 |

### Pattern: Key Line of ideas

- **What it is.** The row directly under the Answer. It answers the new question the
  Answer raises.
- **Test.** Each Key Line point is a sentence. Replace it with its one-word label and see
  whether meaning is lost. If nothing is lost, it was a bucket.
- **Bucket words.** background, findings, recommendations, operations, marketing, issues.
- **Repair.** Open the bucket and state the point it contains. `Findings` becomes the
  finding.

### Pattern: deductive chain

```text
Premise:      Every service that writes to the ledger must pass the idempotency check.
Comment:      The new payout service writes to the ledger.
Therefore:    The payout service must pass the idempotency check before launch.
```

Checks: the second line comments on the first; the conclusion follows; the chain is short.
When a chain grows long or heavy, break it up: summarize the chain as one point and move
its links one level down.

### Pattern: inductive group

```text
Summary:      Three changes will make CI results trustworthy again.
Plural noun:  changes
  1. Tag every test as fast or full.
  2. Quarantine tests that fail without a code change, each with an owner.
  3. Run the full tier nightly and ticket each failure.
```

Checks: one plural noun fits every point; no misfit; the summary speaks about these points
and not about a broader class. Useful nouns: reasons, problems, steps, changes,
opportunities, risks, conclusions.

A list of facts with no summary above it is news. Facts enter the document only when,
together, they explain or defend a higher point.

### Pattern: deduction disguised as induction

Three bullets that look like a class but are a chain:

```text
- Our deploys fail when migrations run long.
- Migrations run long because they lock the largest table.
- So we should move to online schema changes.
```

No plural noun fits: one is a problem, one is a cause, one is an action. Written honestly
it is a deduction: premise, comment, therefore. Either present it as that, or keep the
conclusion as the parent and put the two supporting statements below it as reasons.

### Pattern: order

| Order | Fits | Example group | Why point two is second |
| --- | --- | --- | --- |
| Deductive | An argument | Premise, comment, conclusion | It comments on the first |
| Time | Sequence, process, cause and effect, implementation steps | Tag tests, quarantine, run nightly | It needs the output of the first |
| Structural | Parts of a structure, system, geography, organization, layout | Client, gateway, service, database | It is the next part along the path |
| Degree | Importance, size, severity, priority, magnitude | Highest-risk change first | It matters less than the first and more than the third |

If no row explains the order, the thinking is unfinished. Fix the grouping before the
order: a group that cannot be ordered often contains two kinds of idea.

### Pattern: end-product wording

The weak and better forms in the first three rows are the owner's standing examples. The
remaining rows are illustrations in a software setting.

| Weak | Better | End product you can see |
| --- | --- | --- |
| Improve reporting | Install a reporting system that flags change early | A system that gives early notice of change |
| Strengthen coordination | Assign planning responsibility to the regions | A named owner for planning in each region |
| Enhance efficiency | Establish a follow-up system for overdue accounts | A follow-up system for overdue accounts |
| Improve profits | Improve profits by 10 percent by January 15 | A stated amount and date to test against |
| Improve test coverage | Add characterization tests to every module the agent may edit | A test file per module in scope |
| Strengthen code review | Require a named owner's approval on changes to the payments module | An ownership rule that blocks merge |
| Optimize onboarding | Publish a conventions file that an agent and a new engineer both read first | One file at a known path |

Three questions turn a weak action into a better one:

1. What will exist when this step is complete?
2. What will someone literally have in hand?
3. How will we know the action is done?

Specific wording is what makes the sufficiency test possible. With "improve profits" there
is no way to ask whether the steps below are enough. With an amount and a date there is.

### Pattern: levels of action

A result and the substeps that produce it are different levels.

```text
Mixed (wrong):                      Split (right):
- Cut build time                    Cut build time
- Cache dependencies                  - Cache dependencies
- Run tests in parallel               - Run tests in parallel
```

If siblings include both a result and one of its substeps, move the substeps under the
result.

### Pattern: direct summaries and the inductive leap

A summary states the message the group implies. It is not a placeholder such as "there are
three issues with the pipeline". When moving from grouped ideas to the higher point: stay
close to the evidence, do not infer more than the group warrants, and remove what does not
fit.

Over-reach looks like this: three slow endpoints in one service, summarized as "the
platform does not scale". The points warrant "this service has three slow endpoints with a
shared cause", if they do share one.

### Pattern: the page shows the pyramid

| Rule | Test |
| --- | --- |
| Title reflects the main point | Could the title stand as the answer? |
| Headings state ideas | Read the headings alone. Do they tell the argument? |
| Parallel points in parallel form | Same grammatical shape across siblings |
| Headings are short | Essence of the thought only |
| Groups are introduced | A sentence before the first heading of a group names what is coming |
| Prose survives without headings | Delete the headings mentally. Does it still read? |
| Never one of anything | No lone subheading, no lone bullet |
| Hierarchy markers reveal, not decorate | Headings, decimal numbers, indentation, dot-dash outlines, used only to show levels |

A dot-dash outline shows two levels below a heading:

```text
Tag every test as fast or full
  . Fast tests finish inside a review cycle
      - unit tests
      - contract tests
  . Full tests run nightly
      - end-to-end tests
      - migration tests
```

### Pattern: transitions, summaries, endings

- Each Key Line section opens with a short introduction: a brief story that leads to the
  point, or a backward reference to the main idea of the previous section.
- A long or dense section gets a summary before the next one begins.
- A conclusion is written only when needed. It adds perspective, reinforces significance,
  or creates readiness to act and sets up the next action. It never merely restates.
- `Next Steps` holds actions the reader will not argue with, which are obvious once the
  recommendation is accepted. Anything that still needs proof, argument or defense returns
  to the body.

### Problem solving: definition before analysis

```text
Opening Scene      the stable structure or process in which the problem lives
      |
Disturbing Event   what changed, or what became visible
      |             (external change | internal change | newly recognized evidence)
      v
R1  Undesired Result  ------ gap ------>  R2  Desired Result (specific, quantified if possible)
      |
Reader position (one of seven)  ->  Question  ->  Answer  ->  Key Line
```

Keep the Opening Scene simple enough to visualize. Make R2 specific. A vague R2 makes
every proposed action unfalsifiable, for the same reason vague action wording does.

The data-first habit looks like diligence: gather everything, file it under generic
headings, wait for conclusions. The preferred sequence is define the problem, generate
likely explanations, build a diagnostic framework or logic tree, gather only the evidence
that confirms or rejects a branch. The claim that this is more efficient and easier to
write up is a design claim and has not been measured.

### Problem solving: logic trees

A logic tree serves four purposes: identify possible causes, generate alternative actions,
test completeness, and reveal flaws in grouped ideas. Each branch must be a real
analytical choice.

```text
Why do checkout requests time out during the nightly batch window?
  |- The database refuses or delays the request
  |    |- Batch holds locks that checkout needs          evidence: lock wait log in the window
  |    '- Connection pool is exhausted by batch workers  evidence: pool usage in the window
  |- The application cannot serve the request
  |    |- Worker threads are starved                     evidence: thread dump in the window
  |    '- Retries multiply the load                      evidence: retry count per request
  '- The request never reaches the application
       '- Gateway or network limits are hit              evidence: gateway rejects in the window
```

Each leaf names the evidence that would confirm or reject it. That list is the whole data
request. A random list, by contrast, has branches that overlap or leave a gap: "database",
"slow queries", "Tuesday's deploy".

### Problem solving: issue analysis

An issue is a question whose answer decides something. It is usually yes-or-no.

| Good | Weak | Why the weak one fails |
| --- | --- | --- |
| Is the present inventory level too high? | What are the key issues? | A prompt. No answer decides anything. |
| Is the centralized ordering system placing orders properly? | How should we reorganize? | Assumes the decision and asks for a design. |
| Should we reorganize functionally? | | |

A section headed "Issues" usually stands in for something else. Decide which and name it:

| What the section really contains | Name it |
| --- | --- |
| The gap between what is and what is wanted | Problem definition |
| A breakdown of possible causes | Diagnostic framework |
| A breakdown of possible actions | Solution logic tree |
| A choice and its reasons | Decision recommendation |
| A sequence of steps | The process, by its name |

### Presentations: from pyramid to storyboard

The pyramid decides what goes on screen and what stays in speech. The slides carry the
introduction points, the Key Line points and one level below. The rest is spoken.

Storyboard table to fill at step 2 of the storyboarding workflow:

```text
| # | Slide title (the point, as a sentence) | Level        | Type            | Visual sketch | Spoken bridge |
|---|----------------------------------------|--------------|-----------------|---------------|---------------|
| 1 |                                        | Introduction | text            |               |               |
| 2 |                                        | Answer       | text            |               |               |
| 3 |                                        | Key Line 1   | text or exhibit |               |               |
| 4 |                                        | 1.1          | exhibit         |               |               |
```

- A text slide clarifies structure: the answer, the plan of the talk, a summary.
- An exhibit slide proves one point visually: a chart, a diagram, a table.
- Every slide has a sentence or phrase that states its point. Read in order, the titles
  are the story.
- The script is written around the slides, after the storyboard, and rehearsed until the
  flow is natural.

The boundary of this skill is the seam between argument and rendering. It decides what
each slide must say. It does not decide how the slide looks.

### Templates and working artifacts

SKILL.md carries the structure worksheet and the four skeletons (SCQA, decision memo,
problem-solving brief, presentation). The artifacts below add to them.

Which artifact for which job:

| Job | Artifact |
| --- | --- |
| Memo, report, PRD, proposal | Structure worksheet, then decision memo skeleton |
| Diagnosis or recommendation design | Problem-solving brief, logic tree, yes-or-no issues |
| Deck or talk | Presentation skeleton, then storyboard table |
| One-paragraph note or email | SCQA skeleton only, or nothing |
| Review of someone else's draft | Review record (below) |
| A commitment to a reader about a rewrite | Reader promise (below) |

Review record:

```text
Document:
Reader assumed:
Top point as I would summarize it:

| # | Checklist question                                   | Yes/No | Passage or line | Finding |
|---|------------------------------------------------------|--------|-----------------|---------|
| 1 | One governing thought?                               |        |                 |         |
| 2 | Introduction creates the exact question?             |        |                 |         |
| 3 | Each child group answers the question above?         |        |                 |         |
| 4 | Siblings the same kind of idea?                      |        |                 |         |
| 5 | Order visible and non-arbitrary?                     |        |                 |         |
| 6 | Each inductive group named by a plural noun?         |        |                 |         |
| 7 | Actions written as end products?                     |        |                 |         |
| 8 | Headings tell the same story as the body?            |        |                 |         |
| 9 | Deck: slide titles tell the same story as the talk?  |        |                 |         |

Deepest defect level (question | grouping | order | wording):
Repair proposed:
```

Reader promise, for a restructuring job where the result must be accepted by someone:

```text
Reader promise: After reading the first screen, [reader] can [decide or do what].
Before: [the opening of the current draft, quoted]
After:  [the opening of the restructured draft]
Acceptance test, in plain language: [a person who has not seen the draft reads the first
  screen and states the decision asked of them and the main reasons]
```

Fill the worksheet before or alongside drafting. Filled afterwards, it rationalizes the
draft instead of testing it. A good worksheet shows, for example, three reasons named as
reasons in degree order. A worksheet with no checklist answers is borderline and
acceptable only for a low-stakes memo. Whether worksheet discipline improves outcomes has
not been tested.

### Briefing an agent

This sub-topic is an inference from the method, not part of Minto's material.

The five things a pyramid makes explicit are the five things a model otherwise has to
guess: reader, question, answer, grouped support, logical order. Stating them up front is
expected to reduce drift, vague prose and context sprawl. That effect has not been
measured.

| Brief line | Pyramid element | If omitted |
| --- | --- | --- |
| Here is the reader | Calibration | Output pitched at nobody |
| Here is the question they need answered | Question | Output covers the topic instead of answering |
| Here is the answer we currently believe | Answer | Model invents a thesis or avoids one |
| Here are the support points to prove or refine | Key Line | Model pads with whatever it retrieves |
| Return the output top-down | Presentation order | Background first, answer last |

When the answer is not known, say so and ask for a bottom-up build: grouped points, the
conclusion each group implies, one top point. Do not ask for a recommendation and a
literature survey in the same brief; the survey will win.

When an agent returns work to a person, the same shape applies: outcome first, then the
support, then open items.

## Worked Example Set

All examples are illustrative. Names and situations are invented. No figure in them is a
measurement.

### Example 1: a flat draft rebuilt

Before. The heading story is four filing labels:

```text
# Search Cluster Update

## Background
The search cluster was set up three years ago ... (four paragraphs of history)

## Findings
- Version in use reaches end of support this year
- Reindex takes most of a weekend
- Two teams depend on a plugin that the new version drops
- Rebuild would need a second cluster for a time

## Issues
- What are the key issues with the upgrade?
- How should we handle the plugin?

## Recommendations
- Improve the upgrade process
- Upgrade in place
```

Diagnosis, top-down:

- Question level: no reader, no question, answer buried as the last bullet.
- Grouping level: `Findings` mixes a deadline, a cost, a dependency and a requirement.
- Wording level: "Improve the upgrade process" has no end product. The two "issues" are
  prompts.

Calibration: the reader is the platform lead. The decision is which upgrade path to fund.
The reader has two alternatives, so the position is "which is best?".

After:

```text
# Upgrade the search cluster in place this quarter

Situation:    The search cluster serves every product search and runs a version that
              reaches end of support this year.
Complication: Two upgrade paths exist, in-place and rebuild, and the teams disagree.
Question:     Which path should we fund?
Answer:       Upgrade in place this quarter.

Key Line question: Why in place?
Logic: inductive.  Plural noun: reasons.  Order: degree (strongest first).

## In-place upgrade keeps the plugin two teams depend on until they migrate
## In-place upgrade needs no second cluster
## In-place upgrade can be rehearsed on a copy before the support deadline

Next Steps (undisputed once accepted):
- Book the rehearsal window.
- Name the owner of the plugin migration.
```

What moved: the history shrank to one Situation sentence. Each finding became evidence
under the reason it supports. The "issues" became one question, already answered. "Improve
the upgrade process" was removed because nothing in the notes said what would exist
afterwards.

### Example 2: bottom-up from loose notes

Notes from a pilot of an AI coding agent in a large codebase:

```text
a. Agent changes pass review quickly in modules that have tests.
b. The agent gets lost in the legacy billing module.
c. Reviewers spend most of their time on agent changes to untested code.
d. The team has no written conventions file.
e. Two engineers each keep a private prompt file.
f. Agent changes in the payments module were reverted twice.
g. Many directories have no named owner.
h. The vendor shipped a new model last week.
```

Group like with like, and name each group:

```text
Group 1, observations about where the agent succeeds or fails:  a, b, c, f
  -> The agent is reliable only where tests exist.
Group 2, observations about where the needed knowledge lives:   d, e, g
  -> What the agent needs to know is not written down.
Misfit: h. It is news. It supports neither point. Removed.
```

Draw the higher point from the two group summaries:

```text
Top point: Before widening the pilot, add tests and a conventions file to the modules in
           scope.
```

Now the reader's question can be stated ("Should we widen the pilot?"), and the build
switches to top-down. The two group summaries become the Key Line, as reasons.

### Example 3: the same support, two logics

Inductive, as reasons:

```text
Answer: Add tests and a conventions file before widening the pilot.
  1. The agent is reliable only where tests exist.
  2. What the agent needs to know is not written down.
```

Deductive, as a chain:

```text
Premise:   The agent produces reliable changes only where tests and written conventions
           exist.
Comment:   The modules next in scope have neither.
Therefore: Add tests and a conventions file before widening the pilot.
```

Both are valid. Choose the chain when the reader doubts the conclusion and must be walked
to it. Choose the group when the reader accepts the direction and wants the grounds, each
of which can then be expanded on its own.

### Example 4: a problem-solving brief

```text
Opening Scene:    Checkout calls the order database directly. A nightly batch job
                  rebuilds reporting tables in the same database.
Disturbing Event: Internal change. The batch job was extended to cover a new region and
                  now overlaps with morning traffic from that region.
R1:               Checkout requests time out during the batch window.
R2:               No checkout request waits on the batch job; the error rate in the
                  window equals the rate outside it.
Reader position:  1. Does not know how to get from R1 to R2.
Question:         What should we do to stop checkout timeouts in the batch window?

Issues (yes or no):
- Does the batch job hold locks that checkout needs?
- Is the connection pool exhausted by batch workers in the window?
- Do client retries multiply the load in the window?

Evidence to gather: only what the three issues need. See the logic tree in the pattern
section.

Answer: [written after the issues are answered]
Support:
- diagnosis
- options
- recommendation
- immediate next steps
```

The Answer line stays empty until the issues are decided. Writing a confident answer
before that would be the fake answer that the bottom-up build exists to prevent.

### Example 5: a storyboard from Example 1

```text
| # | Slide title                                                   | Level        | Type    | Visual sketch                         |
|---|---------------------------------------------------------------|--------------|---------|---------------------------------------|
| 1 | Search runs on a version that loses support this year         | Introduction | text    | Timeline with the support end date    |
| 2 | Upgrade in place this quarter                                 | Answer       | text    | The answer and the three reasons      |
| 3 | In place keeps the plugin two teams depend on                 | Key Line 1   | exhibit | Dependency diagram: teams to plugin   |
| 4 | In place needs no second cluster                              | Key Line 2   | exhibit | Side-by-side of the two paths         |
| 5 | In place can be rehearsed before the deadline                 | Key Line 3   | exhibit | Calendar: rehearsal, upgrade, deadline|
| 6 | Two actions start now                                         | Next steps   | text    | Owner and date for each               |
```

Reading the titles alone gives the argument. The four paragraphs of history from the
original draft appear nowhere on screen; one sentence of it is spoken over slide 1.

### Example 6: a brief for a subagent

```text
Reader: The tech lead of the billing team, who must decide whether the agent may edit
  the invoicing module unsupervised.
Question: Is the invoicing module safe for unsupervised agent edits?
Answer we currently believe: Not yet.
Support points to prove or refine:
- Which public functions have no test that would fail on a behaviour change.
- Which conventions are followed in the code but written nowhere.
- Which files have no named owner.
Return the output top-down: a yes or no first, then the three points in degree order,
each with file paths as evidence. No background section.
```

### Example 7: verdicts

Grade structure, not tone.

| Verdict | Case | Why |
| --- | --- | --- |
| Good | A memo rebuilt from one governing thought downward | Every rule exercised |
| Good | A Key Line that states reasons in a visible order | Named class, stated order |
| Good | An action that reads "establish a follow-up system for overdue accounts" | End product visible |
| Good | A `Findings` heading replaced by the finding itself | Idea, not label |
| Good | A review that records nine answers with line references | Gate actually run |
| Good | A failing memo triaged at its introduction before its support | Deepest level first |
| Bad | Sentences polished in a document with no stated reader question | Wrong level repaired |
| Bad | Background first, then `Findings` and `Recommendations` headings | Answer late, labels for thought |
| Bad | An action that says only "improve reporting" | Blank assertion |
| Bad | An issues section listing "what are the key issues" prompts | No decision point |
| Bad | Sign-off that the structure "looks Minto-ish" | Not a gate |
| Bad | SCQA forced onto a changelog, or the method used to format API reference docs | Outside scope |
| Bad | Bullets reordered under a wrong governing thought | Order fixed, question still wrong |
| Bad | Three prose rewrites of a document whose groups are mixed | Retry without change |
| Borderline | Situation omitted for an executive who lives in the context, Question explicit | Fine for this reader; fails for a cold one |
| Borderline | Only the checklist applied to someone else's finished draft | Partial use, tolerated |
| Borderline | Only the SCQA shape used for an email opening | Fragment use, still helps |
| Borderline | A `Background` heading in a fixed corporate template, answer stated first | Template constraint |
| Borderline | Top-down presentation waived for an exploratory draft | Record it as outside the method |
| Borderline | A deck gated on the eight prose questions only | Misses the deck question |
| Borderline | A memo that stops at the Key Line | Defensible when depth is truly one level |
| Borderline | A valid tree with one misfit point | Repair by removal |

The weak cases are all professionally normal. Background sections, key-issues lists and
improve-efficiency actions are standard office prose. That is why explicit tests are
needed and taste is not enough.

## User Journey Scenario

### Main journey: loose notes to a recommendation memo

- **User.** A consultant, or an agent acting for one, starting cold.
- **Starting state.** Interview notes, no draft, and uncertainty about which structure
  should drive the memo.
- **Decision.** Which reading path, example or rewrite makes the director's action
  obvious.
- **Trigger.** A one-page recommendation is due and the reader must decide.

1. **Calibrate.** Names the reader (the director), the decision (fund or not), the
   question, and tries the answer in one sentence. The sentence comes. If it had not, the
   journey would turn here into the bottom-up build and return once a top point emerged.
   This is the decisive beat of the whole journey.
2. **Introduction.** Drafts Situation, Complication, Question, Answer as four lines.
3. **Recheck.** Confirms the Complication triggers the Question. Journeys that skip this
   produce introductions that answer a question the reader never asked.
4. **Key Line.** The Answer says "we should do X". The reader asks "why?". Writes three
   reasons, names the plural noun, orders them by degree.
5. **Expand.** Takes each reason one level down. Stops when no further question is raised.
6. **Headings.** Rewrites each as a statement in parallel form. The title becomes the
   answer.
7. **Shape.** Writes the prose. Adds a `Next Steps` section with two undisputed actions.
8. **Validate.** Records nine answers, each against a passage. Fixes what fails, at the
   level it fails.

The journey ends when the structure and the checklist are verified, not when the prose
sounds finished.

### Variant journeys

- **Diagnosis.** Enters through Opening Scene, Disturbing Event, R1 and R2. Writes
  yes-or-no issues and a logic tree. Gathers only the evidence the tree needs. Joins the
  main journey at step 1 once the issues are answered.
- **Deck.** Follows the main journey to step 5, then the storyboarding workflow. The
  introduction is written in full first and kept fixed while slides are sketched.
- **Review only.** Reads the introduction first, as cheap triage. Then runs the nine
  questions and reports findings by level.
- **Flat draft.** Infers the reader and question from the draft, then rebuilds from step
  2. Reports which points were removed.

How often work starts from loose notes versus a flat draft has not been recorded.

## Anti Pattern Registry Table

Most detectors are naming tests. An invalid structure resists being named: a mixed group
has no plural noun, and a topic heading has no statement form. That makes review
mechanical.

| Anti-pattern | Why it happens | Detector | Replacement |
| --- | --- | --- | --- |
| Background before answer | Politeness; wish to seem thorough | Is the answer on the first screen? | State the answer first when it is known |
| Topic headings (`Background`, `Findings`, `Issues`, `Recommendations`) | Template habit | Can the heading be a statement? | The point itself as the heading |
| Categories in the Key Line | Sorting mistaken for reasoning | Replace each point by its label; is anything lost? | Statements that answer the Key Line question |
| Mixed abstraction levels: results, substeps, causes, actions, evidence as siblings | Points listed in the order they were thought of | One plural noun for the group? | Regroup; split results from steps |
| Vague action language: improve, strengthen, enhance, optimize | The end state was never pictured | What will exist when done? | End-product wording |
| Data first, structure later | Gathering feels rigorous | Is there a written problem definition and hypothesis tree? | Define, hypothesize, then gather |
| Fake issue lists | "Key issues" used as a bucket | Is each issue yes-or-no? | Decision questions, or the section's real name |
| Deduction disguised as induction | Bullets flatten a chain | Does point two comment on point one? | Present the chain, or conclusion over reasons |
| Induction without a plural noun | Points share a topic, not a kind | Name the class | Remove misfits or regroup |
| Presentations as visual recitation | Deck built by pasting the report | Do titles alone tell the story? Is there a script? | Storyboard, point-stating titles, rehearsal |
| Disconnected facts | Reluctance to cut work done | Which parent's question does this answer? | Attach or delete |
| Lone element in a group | A level was added for one point | Count siblings | Merge up, or find the missing sibling |
| Over-reaching summary | Wish for a big conclusion | Does the summary speak only about these points? | Narrow the summary |
| Limp conclusion | Feeling that a document must end with one | Does it add perspective, significance or readiness to act? | Cut it, or make it do one of those |
| Disputed Next Steps | Recommendation smuggled into the ending | Would the reader argue? | Move to the body and defend it |
| Method applied after drafting | Skill opened late | Was a one-sentence answer recorded before the prose? | Return to calibration |
| All-yes checklist sweep | Checklist fatigue | Is each answer tied to a passage? | Answer per question, with the passage |
| Compressed doctrine: "answer first, then support" | Prompt brevity | Is the same-kind rule still stated? | Keep the grouping clauses |
| Generic advice with no reading of the material | The agent skips the draft and notes and writes general writing tips | Does each finding cite a passage of this draft? | Read the material first; findings tied to passages |
| Rule quoted as authority with no stated origin | Guidance sounds authoritative | Is each claim labelled as from the owner's notes, an outside source, or inferred? | Keep the three kinds apart |
| Recommendation with no check attached | Advice cannot be confirmed by a command or a review question | Does each recommendation name its test? | Attach the checklist question, naming test or command |

## Verification Gate Command Set

### The three checklists and how they nest

| Question | Seven-question list | Nine-item list | Twelve-item list |
| --- | --- | --- | --- |
| One top point | yes | yes | yes |
| Introduction creates the exact question | yes | yes | yes |
| Child groups answer the question above | | yes | yes |
| Same kind of idea | yes | yes | yes |
| Visible order | yes | yes | yes |
| Plural noun for inductive groups | yes | yes | yes |
| Actions as end products | yes | yes | yes |
| Headings tell the same story as the body | yes | yes | yes (with slide titles) |
| Deck: slide titles match the spoken flow | | yes | folded into the row above |
| Any points only topics | | | yes |
| Problem definition has all four elements | | | yes |
| Issues are real decision questions | | | yes |
| Ending leaves the reader knowing what to think or do | | | yes |

The nine-item list is the release gate. The seven-question list is a subset: running only
it silently skips the vertical check and the deck check. The twelve-item list adds four
situational checks. Use nine always, plus whichever of the four apply.

### Intensity

| Stakes | Gate |
| --- | --- |
| Trivial note | None. Record nothing. |
| Low | Spot-check three of the nine |
| Normal | All nine, each against a passage |
| High | All nine by two reviewers independently, then compare |
| Any, as a first look | Summarize-the-top-point test; then the introduction alone |

Checklist gates are judgements, not commands. Agreement between reviewers on the judgement
questions has not been measured.

### Commands

SKILL.md lists nine candidate finders for a Markdown draft. The commands below add a
one-shot count and two checks for Markdown slide decks.

Count candidates per finder, as a quick profile of a draft:

```bash
f=draft.md
printf 'label headings: %s\n' "$(grep -c -i -E '^#+ +([0-9.]+ +)?(background|context|overview|introduction|findings|results|analysis|discussion|(key )?issues|recommendations?|operations|marketing|observations|considerations|miscellaneous|other)[[:space:]:]*$' "$f")"
printf 'short headings: %s\n' "$(awk '/^(```|~~~)/{c=!c} !c && /^#+ /{ if (NF-1 <= 2) k++ } END{print k+0}' "$f")"
printf 'vague verbs:    %s\n' "$(grep -c -i -w -E 'improve|strengthen|enhance|optimi[sz]e' "$f")"
printf 'open prompts:   %s\n' "$(grep -c -i -E '^[[:space:]]*([-*+]|[0-9]+[.)])[[:space:]]+(what|how|which|why|where|who)[[:space:]].*\?' "$f")"
```

Slide titles of a Marp or reveal Markdown deck, one per slide, to read as a story:

```bash
d=deck.md
awk 'NR==1 && /^---[[:space:]]*$/{fm=1; next} fm{ if(/^---[[:space:]]*$/) fm=0; next }
     /^(```|~~~)/{c=!c} c{next}
     /^---[[:space:]]*$/{s++; seen=0; next}
     /^#+ / && !seen {print "slide " s+1 ": " $0; seen=1}' "$d"
```

Slides that have content but no title:

```bash
d=deck.md
awk 'NR==1 && /^---[[:space:]]*$/{fm=1; next} fm{ if(/^---[[:space:]]*$/) fm=0; next }
     /^(```|~~~)/{c=!c} c{next}
     /^---[[:space:]]*$/{ if(body && !seen) print "slide " s+1 ": no title"; s++; seen=0; body=0; next }
     /^#+ /{seen=1} NF{body=1}
     END{ if(body && !seen) print "slide " s+1 ": no title" }' "$d"
```

Limits of all these commands: they read Markdown only, they see form and not meaning, and
a clean result does not show that siblings are the same kind or that the question is the
right one. Those remain reviewer questions.

## Failure Mode Table

Triage from the top: question, then grouping, then order, then wording. Repair depth
matches defect depth. How often each failure occurs has not been measured.

| Failure | Signal | Impact | Repair | Level |
| --- | --- | --- | --- | --- |
| Wrong question | Complication does not trigger the Question; reader asks something else | Reader lost at the introduction | Recalibrate; rebuild the introduction; rebuild the document | Question |
| No governing thought | No one can summarize the document in a sentence | Topic sprawl | Bottom-up build until one top point emerges | Question |
| Fake answer forced early | Top point changes each time support is added | Unstable tree | Stop top-down; go bottom-up | Question |
| Mixed group | No plural noun names the siblings | Reader cannot see the logic | Regroup; remove misfits; split levels | Grouping |
| Parent does not summarize children | Summary is a label, or broader than the points | Unsupported claim | Rewrite the summary from the children, or regroup | Grouping |
| Children do not answer the parent | A child answers a different question | Disconnected facts | Move or delete the child | Grouping |
| Chain shown as class | Points depend on each other but are bulleted as equals | Argument hidden | Present as deduction, or conclusion over reasons | Grouping |
| Deductive chain too long | Reader must hold many premises | Lost thread | Break the chain; push links down a level | Grouping |
| Arbitrary order | No answer to "why is this second?" | Unfinished thinking shows | Reorder by time, degree, structure or deduction | Order |
| Topic Key Line | Key Line boxes are buckets | Headings carry no message | State the point in each bucket | Wording |
| Blank action | No visible end product | Steps cannot be tested for sufficiency | Apply the three end-product questions | Wording |
| Headings diverge from body | Heading story differs from the text | Skimmers get a different argument | Rewrite headings from the pyramid | Wording |
| Data-first analysis | Data gathered before a problem definition exists | Unbounded effort; conclusions do not emerge | Return to Opening Scene, Disturbing Event, R1, R2 | Analysis |
| Vague R2 | Desired result not specific | Any action can be claimed sufficient | Specify; quantify when the task allows | Analysis |
| Non-MECE tree | Branches overlap or leave a gap | Missed cause; double counting | Rebuild branches as real analytical choices | Analysis |
| Disputed Next Steps | Reader argues with a "next step" | Recommendation undefended | Move it into the body | Ending |
| Deck recites report | Slides are paragraphs; titles are labels | Audience reads instead of listening | Storyboard from introduction and Key Line | Medium |
| Child document drift | A chapter answers a question the parent never asked | Large document loses its thread | Restate the parent's question at the top of each child | Scale |
| Misdiagnosed level | Rework changes nothing | Wasted rounds | Re-triage from the question down; pair review if contested | Process |

Structural failures surface late, usually as the reader's confusion, and no signal inside
the document fully predicts them. Checklist gates, introduction-only reviews and logic
trees for contested branches are the ways to catch them earlier.

## Workload Model

- **Unit of work.** One document, for one audience and one decision, per focused sitting.
  Restructuring five documents shallowly in one sweep is the bad case.
- **Default depth.** Key Line plus one expanded level. Stop when every point's question
  is answered.
- **What effort scales with.** Tree depth and width, not page count.
- **Best single predictor.** Whether the answer is clear at calibration. A fuzzy answer
  means a bottom-up build, which is open-ended grouping work with no guaranteed
  convergence. Budget it separately. Its duration has not been measured.
- **Contested analysis.** A shallow document over contested analysis can cost more than a
  deep routine one. Split calibration and structuring into separate sittings, or pair.
- **Decks.** Storyboarding multiplies work per point: slides, script, rehearsal. A deck
  storyboarded over two sittings is acceptable when the introduction is frozen between
  them.
- **Routine documents.** A template skeleton caps depth and cost.
- **Provisional bounds.** One audience, one decision, one checklist, and at most about
  twelve source documents per use. Beyond that, split or narrow. The figure is a working
  bound, not a measured limit.
- **Deliverable of a restructuring job.** A reader promise, a before-and-after rewrite of
  the opening, and a plain-language acceptance test.

## Reliability Target

Two binary targets per structured document:

1. A one-sentence answer is recorded.
2. Every inductive group has a named class.

Notes:

- No baseline exists. The first period in which documents are scanned sets what is
  achievable.
- A recorded answer does not prove the document argues it. The summarize test is the
  independent second gate.
- An exploratory document without an answer is recorded as outside the method. It is not
  counted as a failure.
- The answer-sentence target audits calibration, the step most often skipped. Its absence
  predicts the downstream defects the checklist would otherwise catch later and at higher
  cost.
- Every "avoid" or failure verdict names what to do next: return to an earlier step,
  escalate to a person, or route to another skill.
- A sampling target of 18 correct routing decisions out of 20 has been proposed for
  auditing when this skill is opened or avoided. It has never been sampled. Treat it as a
  proposal, not as achieved performance.
- No claim about speed or quality gain from the method may be reported as achieved without
  a record behind it.
- Every recommendation that is reused keeps its evidence label. The count of unsupported
  claims about production behaviour, security, latency or reliability in a structured
  document should be zero.

## Retry Backpressure Guidance

For a writing skill, a retry is a rework round. The rules:

- **Classify before reworking.** Decide which level failed: question, grouping, order or
  wording. Rework that level. Also decide what kind of failure it is: a passing slip, stale
  evidence, missing context, or a true contradiction in the material.
- **Stale outside evidence.** One bounded retry, then escalate to a person or to a narrower
  source.
- **Stop conditions.** Stop drafting when the sources have not been covered, when review
  findings are unanswered, or when a gate is failing.
- **Polish is not a retry.** Rewriting sentences while the structure is unchanged
  reproduces the defect. Three prose rewrites of a document with mixed groups is the
  typical waste.
- **Level-to-repair map.** Wrong question: recalibrate. Mixed siblings: regroup. Arbitrary
  sequence: reorder.
- **Stop regrouping the same notes.** A repeated bottom-up build over unchanged notes
  signals a gap in the problem definition. Escalate to R1 and R2. A second build is
  legitimate when new points have surfaced.
- **When diagnosis is contested.** A misread defect sends the rework to the wrong layer.
  Get a second reviewer.
- **When structure keeps failing.** Fall back to a template skeleton.
- **Before a broad rewrite.** Re-read the calibration lines and the worksheet. In a long
  job, checkpoint after each batch, and re-read the brief before a broad rewrite, a commit,
  a push or anything destructive. For work spread across several agents, one owner per
  document or branch, and a check of exact path, headings, evidence labels and the Key
  Line at merge time.

## Observability Checklist

What to keep after a structuring or review job:

- [ ] The filled worksheet, storyboard or problem-solving brief.
- [ ] The nine answers, per question, each with its passage. A single pass or fail loses
      the evidence the feedback loop needs.
- [ ] The diagnosed level and the findings.
- [ ] Which inputs were read and which were intentionally skipped.
- [ ] The exact check used: the command, the reviewer question, or the rendered artifact
      that was looked at.
- [ ] The reviewer's decision and any stated uncertainty.
- [ ] The leading indicator and the failure signal that apply to this document.
- [ ] What would trigger a re-check.

Keep records small: the worksheet, the answers, a summary of commands run, the list of
files changed and the unresolved risks. Not transcripts. The worksheet costs
nothing extra to keep, because the workflow already produced it, and unlike prose it shows
its grouping and ordering logic directly.

Scale the record to the document:

| Document | Record |
| --- | --- |
| Three-line note | None, or a one-line "nothing to record" entry |
| Routine memo | Worksheet only |
| Review of someone else's draft | Findings only |
| High volume of similar documents | A sample |
| Decision document | Everything in the checklist above |

Time measurements (elapsed time, reviewer time, and p50, p95 and p99 latency where a tool
is being timed) are worth recording only when the speed of the workflow is itself in
question.

## Performance Verification Method

The claim that structure-first work is more efficient has not been measured. To test it:

1. Compare first-pass yield on the nine-item gate, and the number of rework rounds, for
   documents that were calibrated before drafting against documents that were not.
2. Compare within the same author where possible. This removes the confound of author
   skill that cross-author comparisons carry.
3. Re-baseline when the genre changes.
4. Review the record quarterly, once enough documents exist.

A reader-side test: a reviewer who has not seen the draft can find the correct next action
within about ten minutes, and can name the action, the check that verifies it, and the
stop condition without opening unrelated files. The ten-minute figure is a target, not a
measurement. The test fails when drafting or implementation begins before the unit of
work, the reliability targets and the failure table are explicit.

What to capture when timing a run: input size, number of sources, number of tool calls,
wall-clock time, and the reviewer's decision time.

Limits:

- Rework rounds undercount silent failures. A document that shipped unpolished and
  confused its reader shows zero rework.
- Small document counts make trends noisy. The effect size and the sample needed are
  unknown.
- Adopting the claim unverified for a quarter while the record accumulates is acceptable
  if it is noted as assumed. Quoting the benefit as measured when nothing was tracked is
  not.

## Scale Boundary Statement

The owner's notes treat one document at a time. Everything in this section extends them
and is an inference. The size at which a single pyramid stops working has not been
measured and depends on the genre.

A single pyramid is no longer enough when the work spans several independent systems, more
than one ownership boundary, or an open-ended set of sources. It also does not stand in
for an operational commitment: a memo about a system that serves production traffic does
not replace an explicit service-level objective.

- **Recurse.** A Key Line point that outgrows its level becomes its own pyramid with its
  own SCQA. The question-and-answer mechanism supports this without new rules.
- **Restate the parent's question in each child.** Child documents drift away from the
  parent's question unless the Key Line they hang from is repeated at their top.
- **Freeze the Key Line as the interface.** With several authors, agree the Key Line
  first, assign one editor per branch, and review the tree on a schedule to catch drift.
- **Large programs.** Use a master summary with satellite documents.
- **Large codebases.** Narrow the sources first: decide which modules and files bear on
  the reader's question before reading. See
  [codebase-navigation](../tir-codebase-navigation/SKILL.md).
- **Parallel agents.** Split by theme and keep one owner of verification. One owner per
  document or branch. Never let two agents rewrite the same document without a merge
  checkpoint.
- **Long-running jobs.** Checkpoint state, summarize open risks, and re-check the brief
  before continuing.

| Verdict | Case |
| --- | --- |
| Good | A hundred-page report split into a summary pyramid and chapter pyramids |
| Bad | One governing thought stretched over a program nobody can summarize |
| Borderline | Two authors sharing one memo with the Key Line frozen between them |

## Outcome Metrics and Feedback Loops

Record per document: whether calibration happened, which checklist items failed, and the
rule behind each failure.

| Signal | What it tells you | Caution |
| --- | --- | --- |
| Fraction of documents with a recorded one-sentence answer | Whether calibration happens | Cheapest signal; can be checked without reading the draft |
| First-pass yield on the nine-item gate | Whether structure is right before review | A rising rate can mean laxer checking |
| Findings per review, keyed to the six core rules | Which rule fails most | Weight them: nine heading nits can outnumber one wrong-question introduction that sinks the document |
| Reader can act without hidden author context | Leading indicator of success | Needs a reader who was not involved |
| A literature dump replaces a guided explanation | Failure signal | |

Feedback loop:

- When the same rule fails repeatedly, tighten the guidance for that rule. Example:
  repeated plural-noun failures lead to stricter grouping guidance.
- Run an occasional deep audit as an independent check on the pass rate. Celebrating pass
  rates while audits find mixed siblings is the failure case.
- Use reader responses where they are available.
- At first, tracking only the recorded-answer fraction is enough.
- Re-run the term check in the Completeness Checklist after any edit to the skill files.
  Refresh outside sources when the public material they describe changes.
- In a period with no structured documents, record that and skip the metrics.

Baselines and thresholds for all of these are provisional. None has been measured.

## Completeness Checklist

For a document produced with this skill:

- [ ] One-sentence answer recorded.
- [ ] SCQA present, or its implied parts noted with the reader named.
- [ ] Key Line with declared logic, plural noun where inductive, stated order.
- [ ] One level below the Key Line, or a note that depth is one level.
- [ ] Headings as statements; no lone elements.
- [ ] Actions as end products.
- [ ] If diagnostic: Opening Scene, Disturbing Event, R1, R2; yes-or-no issues.
- [ ] If a deck: storyboard, point-stating titles, script.
- [ ] Nine answers recorded against passages.

For any copy, summary or prompt that carries this method, check that the doctrine has
survived intact. Presence is not enough; phrasing can drift while the rule name stays.

- [ ] All six core rules, with the warning that a single break means the structure is
      probably wrong. Six rules listed without that warning lose the claim that makes
      them non-negotiable.
- [ ] "Same kind of idea", not "related ideas".
- [ ] SCQA, with the Complication as trigger.
- [ ] The four problem-definition elements.
- [ ] The plural-noun test and the end-product test.
- [ ] The guardrails against background dumps, label headings, mixed groups, disconnected
      facts, data before problem, and decks that recite text.
- [ ] The nine-item gate, including the deck question.

Term check, run from this directory:

```bash
for t in "governing thought" "Key Line" "Situation" "Complication" "Opening Scene" \
         "Disturbing Event" "Undesired Result" "Desired Result" "plural noun" \
         "end product" "same kind of idea" "If any one breaks"; do
  grep -q -i -F "$t" SKILL.md || echo "MISSING: $t"
done
```

For a reference file on this subject, also confirm it contains: a role scenario (user,
starting state, decision, trigger); an adopt, adapt, avoid and cost-of-error guide; a
confidence warning where sources are secondhand; a reviewable artifact; good, bad and
borderline examples; one leading indicator and one failure signal; and routing to adjacent
skills.

Spot-read two items against the text in each review cycle; how many depends on how much
was edited. Carrying forward the previous cycle's phrasing check is acceptable only with a
note that it is stale. Ticks made from a glance at the headings do not count; a term check
cannot see an inverted rule. A final probe: the document that carries the method should itself be able
to answer the nine questions. If it cannot, its transmission of them is suspect.

## Adjacent Reference Routing

The dividing question: is the request about what the document argues, or about how it is
rendered? Argument structure, SCQA, grouping, ordering and storyboard logic belong here.
Rendering does not.

| Need | Route |
| --- | --- |
| Options still open; premise untested; a decision to be reached | [explore-and-decide](../tir-explore-and-decide/SKILL.md), then return here to write it up |
| Requirements that must map to tests | [executable-specs](../tir-executable-specs/SKILL.md) and [A03](../../A03-Executable-Specs01.md) |
| Writing or merging skills and reference files | [authoring-skills-and-references](../tir-authoring-skills-and-references/SKILL.md) |
| Briefing, context packing and coordination of subagents | [agent-context-and-orchestration](../tir-agent-context-and-prompts/SKILL.md) |
| Finding the evidence in a large codebase before writing | [codebase-navigation](../tir-codebase-navigation/SKILL.md) |
| Reviewing code or verifying a claim, not a document's structure | [review-verify-debug](../tir-code-review/SKILL.md) |
| Why process is sized to the work type | [A00](../../A00-LLM-Principles01.md), [A01](../../A01-LLM-Workflow01.md) |
| Mining patterns from a corpus into a reference | [A02](../../A02-Mega-Idiomatic-Prompt.md) |
| Sentence-level polish, house style | A style guide. Not covered here. |
| Slide mechanics, visual and media production | Presentation or media tooling. Not covered here. |
| Reference and API documentation | Documentation templates. Not covered here. |

A deck request often arrives as one request with two parts. Keep the content order and
slide points here; send image and layout production elsewhere.

Verify that a destination exists before routing to it. A route that is only a keyword
strands the reader. When no destination exists, record the need as a gap and say so.

## Source Evidence Mapping Table

External sources and upstream works only.

| Source | Supports | Status |
| --- | --- | --- |
| Barbara Minto, *The Minto Pyramid Principle: Logic in Writing, Thinking, and Problem Solving* | The whole doctrine: governing thought, top-down presentation, SCQA, Key Line, deduction and induction, ordering, problem definition, logic trees, issue analysis, page display, storyboarding | Named basis of the owner's working notes. Not consulted directly for this reference. No claim here has been checked against the book. |
| Barbara Minto, *The Minto Pyramid Principle Self-Study Course Workbook* (1998, Minto International) | Same doctrine in exercise form | Same status |
| https://developers.openai.com/codex/guides/agents-md | Agent instruction file format | Not evidence for any writing rule. Do not cite it for SCQA, grouping or pyramid rules. |
| https://agents.md/ | Agent instruction file format | Same |
| https://docs.github.com/actions | CI automation | Same. Authoritative on its own subject, which is not writing. |

No third-party project contributed text or structure to this skill.

Provenance examples: citing the owner's notes for the six core rules is sound. Attributing
the SCQA shape to Minto is correct in substance but verified only against the notes.
Citing CI documentation for an introduction rule is fabrication.

## Evidence Boundary Notes

- **Secondhand to Minto.** The rules here are the owner's working doctrine, distilled from
  the two books named above. They are operational notes, not a replacement for the books
  and not complete in a scholarly sense. Do not quote any rule as Minto's own verified
  words.
- **What cannot be detected.** Conflicts between the long and short forms of the owner's
  notes can be resolved, and SKILL.md records them. Conflicts between the notes and the
  books cannot even be detected without reading the books.
- **Label by claim, not by section.** When reusing a rule in a brief or a report, keep
  three kinds apart: taken from the owner's notes (`local_corpus_sourced_fact`); taken from
  an outside source (`external_research_sourced_fact`); inferred from both
  (`combined_evidence_inference_note`). A label on a section lets one labelled sentence cover for its unlabelled neighbours.
  Reuse in prompts strips labels, so a load-bearing sentence should carry its qualifier
  inside itself.
- **Inferences in this skill.** The agent-briefing section; the Key Line column of the
  reader-position table beyond the three stated cases; the repair-depth ranking; all
  scale guidance (recursion, frozen Key Line, child documents); the mechanical commands;
  the software examples.
- **Not measured.** Efficiency of structure-first work. Benefit of the worksheet.
  Frequency of each anti-pattern and failure. Agreement between reviewers. Convergence
  time of the bottom-up build. The stakes threshold for skipping the method. The size
  limit of a single pyramid. The ten-minute and 18-of-20 figures are proposed targets.
- **Transfer.** The tests transfer from consulting memos to engineering documents, but
  examples tied to one genre may need replacing. How far the method transfers to
  conversational or exploratory writing is not established.
- **Illustrative figures.** "Improve profits by 10 percent by January 15" is an example of
  specific wording, not a result.

## Future Refresh Search Queries

Search the vocabulary of the field, not the name of this skill.

- `Minto pyramid principle` book editions and chapter summaries
- `SCQA framework` introduction examples
- `Minto problem definition R1 R2 opening scene disturbing event`
- `MECE` grouping and logic tree commentary
- `issue tree` versus `hypothesis tree` consulting problem solving
- structured business writing, answer-first memo
- `storyboard` presentation `action titles`

Weak probes, kept for completeness: searching a coined title such as "minto pyramid
writing patterns" together with "official documentation best practices", "GitHub
repository examples", or "changelog release notes migration". The method has no official
documentation, repository or release notes, so these return little.

Guidance for a refresh:

- The best target is concrete: the two books themselves.
- Refresh slowly. The rules come from books that are decades old. New commentary and new
  applications matter more than changed rules.
- Results skew toward consulting marketing that names the pyramid without carrying its
  rules. Grade a result for doctrinal substance before using it, and label anything
  adopted from such a source as an inference until corroborated.
- An empty result is not confirmation that nothing changed.
