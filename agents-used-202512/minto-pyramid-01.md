---
name: minto-pyramid-01
description: minto-pyramid-01
model: sonnet
color: orange
---

# Minto Pyramid Principle: Action Patterns for Writing, Thinking, Problem Solving, and Presentation

Source basis:
- `/Users/amuldotexe/Downloads/Barbara Minto - The Minto Pyramid Principle Logic in Writing Thinking.pdf`
- `/Users/amuldotexe/Downloads/BARBAR MINTO - THE MINTO PYRAMID PRINCIPLE - SELF-STUDY COURSE WORKBOOK (1998, MINTO INTERNATIONAL) - libgen.li (1).pdf`
- `agents-used-202512/rust-coder-01.md` as the precedent for tone and usage

## Premise Check

This file is not a replacement for the original books. It is a practical reference in the same spirit as `rust-coder-01.md`: a working doctrine note we can use while writing memos, proposals, analyses, specifications, presentations, and reviews.

Also, just like `rust-coder-01.md`, this is not meant to be "complete" in the scholarly sense. It is meant to be operational. The goal is to make the durable patterns easy to apply under time pressure.

## The Main Thesis

Clear writing is clear thinking made visible.

The Minto discipline says that if a document is hard to follow, the problem is usually not sentence style but structure. The writer has not yet made explicit:

- the exact question being answered
- the answer to that question
- the grouped ideas that support the answer
- the logical order connecting those ideas

The working implication is simple:

- Structure first
- Wording second
- Start from the answer
- Present from the top down
- Make every support point earn its place

## The Non-Negotiables

### 1. One Governing Thought

Every document should drive toward a single top point.

- If you cannot state the one thing the document is saying, the document is not ready.
- Everything below should explain or defend that one point.

### 2. Present Top Down

The reader should get the answer before the detail.

- Top point first
- Key Line second
- Supporting detail third

### 3. Every Parent Summarizes Its Children

Ideas at any level must summarize the grouped ideas below.

- If a parent does not summarize its children, the grouping is wrong.
- If the children do not naturally imply the parent, the reasoning is wrong.

### 4. Sibling Ideas Must Be the Same Kind of Idea

Each grouping must contain like-with-like.

- reasons with reasons
- steps with steps
- problems with problems
- changes with changes
- conclusions with conclusions

If you cannot name the grouping with one plural noun, the grouping is probably invalid.

### 5. Every Group Must Be Ordered

There must be a reason why point two is second and not first or third.

The common orders are:

- deductive order
- time order
- structural order
- degree or priority order

If the order feels arbitrary, the thinking is unfinished.

### 6. Every Point Must Answer the Question Above

Vertical logic is a question-and-answer dialogue.

- A statement raises a question in the reader's mind.
- The points below must answer that question directly.
- Do not answer questions before raising them.
- Do not raise questions you are not ready to answer.

### 7. Every Document Needs a Proper Introduction

The introduction must create the exact question your document answers.

Use:

- Situation
- Complication
- Question
- Answer

The answer then raises the new question answered by the Key Line.

### 8. Key Line Boxes Must Contain Ideas, Not Topics

Bad Key Line points are labels like:

- background
- findings
- recommendations
- operations
- marketing
- issues

Good Key Line points are actual statements.

### 9. Inductive Groups Need a Plural Noun

If a grouping is inductive, name the class explicitly.

Examples:

- reasons
- problems
- steps
- changes
- opportunities
- risks

That plural noun helps reveal both the logic and the misfits.

### 10. Action Ideas Must State End Products

Avoid vague action language.

- "improve reporting" is too vague
- "install a system that gives early notice of change" is testable

If you cannot visualize the result of an action, you cannot judge whether the steps are sufficient.

### 11. Define the Problem Before Gathering Everything

Do not collect unlimited data and hope the structure appears later.

Instead:

- define the problem
- generate hypotheses
- design the analysis
- gather only the data needed to prove or disprove the hypotheses

### 12. The Reader's Question Governs the Whole Document

The best structure for the writer is the one that best matches the reader's actual question.

If the question is wrong, the whole pyramid will be wrong even if the writing is clean.

## The Core Substructures

The pyramid rests on three substructures:

- vertical question-and-answer logic
- horizontal deductive or inductive logic
- introductory flow

### Vertical Logic

What happens vertically:

- you make a statement
- the reader asks "Why?", "How?", or "Why do you say that?"
- the next level answers that question

This is how the pyramid pulls the reader through the argument.

### Horizontal Logic

What happens horizontally:

- sibling points either form a deductive chain
- or they form an inductive grouping

You must know which one you are using.

### Introductory Flow

The introduction orients the reader before the main argument.

- Situation: what the reader already knows or will readily accept
- Complication: what changed or what tension appeared
- Question: what that change naturally makes the reader ask
- Answer: the top point of the document

## The Top-Down Build Process

When you know roughly what you want to say, build from the top down.

### Step 1. State the Subject

What is the document about?

If the subject is fuzzy, the structure will be fuzzy.

### Step 2. Decide the Reader's Question

What question do you want answered in the reader's mind when they finish reading?

Examples:

- What should we do?
- Is this the right solution?
- How should we implement it?
- Which option is best?

### Step 3. Write the Answer

State the top point as a complete idea, not a topic label.

### Step 4. Identify the Situation

State the first noncontroversial thing the reader will agree is true about the subject.

### Step 5. Develop the Complication

Ask:

- "Yes, I know that, so what?"

The answer to that prompt should expose the complication.

Important:

- the complication is a trigger in the story
- it is not always a "problem" in the narrow sense

### Step 6. Recheck the Question and Answer

The complication should naturally trigger the question.

If it does not:

- the complication is wrong
- or the question is wrong
- or the answer is answering the wrong question

### Step 7. Find the New Question Raised by the Answer

Once you state the answer, the reader asks another question.

Usually:

- Why?
- How?
- In what ways?

This is the Key Line question.

### Step 8. Decide Whether the Support Is Deductive or Inductive

- Deductive if you are making an argument
- Inductive if you are grouping similar support points

If inductive, name the plural noun.

### Step 9. Repeat Down the Pyramid

For each support point:

- ask what question it raises
- answer that question one level down

## The Bottom-Up Build Process

Use bottom-up when:

- the subject is unclear
- the reader's question is unclear
- the top point does not yet feel stable

Bottom-up method:

1. List the points you think matter.
2. Work out their relationships.
3. Group like ideas together.
4. Draw the implied conclusion from each grouping.
5. Continue upward until one top point emerges.

This is slower than top-down, but better than forcing a fake answer too early.

## How to Build Introductions

The introduction is not background filler. It is the device that creates the question.

### The SCQA Shape

```text
Situation: Here is the stable context you know.
Complication: Here is what changed, failed, appeared, or became urgent.
Question: Here is what that should make you ask.
Answer: Here is the top point of this document.
```

### Rules for Strong Introductions

- Start the Situation with a fact the reader will accept.
- Treat the Complication as a trigger, not just a complaint.
- Make the Question match the answer you actually intend to give.
- Give the Answer early.
- In longer documents, introduce the Key Line points after the Answer.

### Common Question Shapes

Use these patterns often:

- We have a problem. What should we do?
- We think we have a solution. Is it the right one?
- We know the solution. How do we implement it?
- We tried a solution. It did not work. What now?
- We have several alternatives. Which is best?
- We know we need change but not the target. What should the objective be?
- We know the target but are not sure there is really a problem. Do we need to act?

### Key Line Guidance

The Key Line should answer the new question raised by the answer.

- If the top point says we should do something, the Key Line may be reasons or changes.
- If the top point says we can achieve something, the Key Line may be steps.
- If the top point says an option is best, the Key Line may be criteria or advantages.

## Deduction vs Induction

Most confusion in documents comes from mixing these two.

### Deductive Logic

Use deduction when you need to prove a conclusion.

Pattern:

- premise
- comment on the premise
- therefore conclusion

Checks:

- the second point must comment on the first
- the conclusion must follow from the chain
- keep deductive chains short

Practical rule:

- if the grouping gets long or heavy, break it up

### Inductive Logic

Use induction when several similar ideas imply a higher-order insight.

Pattern:

- group similar ideas
- name them with a plural noun
- state the significance of that similarity

Checks:

- can every point be described by the same plural noun?
- is any point a misfit?
- does the higher point say something specifically about these points and not a much broader class?

### News Is Not Thinking

A list of facts is not yet reasoning.

Facts belong in the document only if, together, they explain or defend a higher point.

## Logical Ordering Rules

Once the grouping is right, the order must also be right.

### 1. Deductive Order

Use when making an argument.

### 2. Time Order

Use when describing sequence, process, cause and effect, or implementation steps.

### 3. Structural Order

Use when commenting on parts of a structure, system, geography, organization, or layout.

### 4. Degree Order

Use when ranking by importance, size, severity, priority, or magnitude.

## Grouping and Summarizing Discipline

This is where vague writers usually fail.

### Avoid Intellectually Blank Assertions

Weak:

- improve efficiency
- strengthen performance
- enhance coordination

These are too blank to test.

Better:

- assign planning responsibility to the regions
- establish a system for following up overdue accounts
- install a reporting system that flags change early

### State the Effect of Actions

Action ideas should be worded so you can see the end product.

Ask:

- What will exist when this step is complete?
- What will someone literally have in hand?
- How will we know the action is done?

### Make the Wording Specific

Specific wording helps you test whether the support points are collectively sufficient.

Bad:

- improve profits

Better:

- improve profits by 10 percent by January 15

### Distinguish Levels of Action

Do not mix:

- a result
- a substep required to create the result

Put results and their producing actions at different levels in the pyramid.

### Summarize Directly

Do not hide behind generic labels.

Summaries should state the real message implied by the grouping, not a placeholder category.

### Make the Inductive Leap Carefully

When moving from grouped ideas to a higher conclusion:

- stay close enough to the evidence
- do not infer more than the grouping warrants
- remove ideas that do not fit

## Problem Solving with Minto

The book extends the pyramid beyond writing into problem solving.

### The Problem-Definition Framework

Define four elements:

- Starting Point or Opening Scene
- Disturbing Event
- R1: Undesired Result
- R2: Desired Result

Then determine the reader's question.

### Opening Scene

What is the stable structure or process we are dealing with?

Keep it simple and visual.

### Disturbing Event

What changed, or what became visible, that disturbed the previous state?

Common kinds:

- external change
- internal change
- newly recognized evidence of a problem or opportunity

### R1: Undesired Result

What result do we have that we do not want?

### R2: Desired Result

What result do we want instead?

State R2 as specifically as possible. If possible, quantify it.

### The Seven Common Reader Positions

The reader is usually in one of these positions:

1. They do not know how to get from R1 to R2.
2. They think they know how, but are not sure they are right.
3. They know the solution, but not the implementation path.
4. They tried a solution and it failed.
5. They have alternatives and need to choose.
6. They know something is wrong but cannot define the target state.
7. They know the target state but are not sure they really have a problem.

The document structure should change to fit which of these is true.

## Diagnostic Frameworks Before Data

Bad habit:

- gather all available data
- label it with generic headings
- hope conclusions emerge later

Better habit:

- define the problem first
- generate possible explanations
- create diagnostic frameworks and logic trees
- gather only the evidence needed to test them

This is both more efficient and easier to write up later.

### Use MECE Thinking Carefully

When breaking down causes or options:

- make them mutually exclusive
- make them collectively exhaustive enough for the decision

Do not confuse a random list with a proper analysis tree.

## Logic Trees and Issue Analysis

### Logic Trees

Use logic trees to:

- identify possible causes
- generate possible solutions
- test completeness
- reveal flaws in grouped ideas

### Issue Analysis

Use issue analysis when you need decision-driving questions.

A real issue is usually a yes-or-no question.

Good:

- Is the present inventory level too high?
- Is the centralized system placing orders properly?
- Should we reorganize functionally?

Weak:

- What are the key issues?
- How should we reorganize?

Those may be important prompts, but they are not crisp issues.

### Do Not Hide Behind "Issues"

A section called "Issues" often signals fuzzy thinking.

Usually what you really need is one of these:

- a problem definition
- a diagnostic framework
- a solution logic tree
- a decision recommendation

## How to Reflect the Pyramid on the Page

Once the structure is right, the page should make the structure obvious.

### Titles and Headings

- Reflect the main point in the title.
- Use headings that state ideas, not filing labels.
- Use parallel grammar for points at the same level.
- Keep headings short.
- Introduce each group of headings before the headings appear.
- The prose should still read smoothly even if the headings were removed.

### Numbering and Indentation

You can use:

- hierarchical headings
- decimal numbering
- indented display
- dot-dash outlines

Use them only to reveal hierarchy, not to decorate the page.

### Important Page-Level Rules

- never use only one of any element in a group
- keep parallel points in parallel form
- limit wording to the essence of the thought
- treat headings as visual signs, not the full carrier of meaning

## Transitions, Summaries, and Conclusions

### Introduce Each New Group

Each Key Line section should begin with a brief introduction that orients the reader.

You can do this by:

- telling a short story that leads to the point
- referencing backward to the previous section's main idea

### Summarize Long Sections

When a section is long or dense, pause and summarize before moving on.

### Make Full Conclusions Only When Needed

Do not end with a limp restatement.

If you need a conclusion, it should:

- put the message in perspective
- reinforce significance
- create desire or readiness to act

### Use "Next Steps" Only for Obvious Immediate Actions

If you include a Next Steps section:

- include only actions the reader will not argue with
- if an action still needs proof, it belongs in the body of the reasoning

## Presentations and Storyboarding

Presentation logic should also follow the pyramid.

### A Presentation Is Not a Report on Slides

Slides are visual aids inside a live story, not page text pasted on a screen.

### Storyboarding Workflow

1. Write the introduction in full.
2. Put the intro points, Key Line points, and one level below onto a blank storyboard.
3. Sketch how each point should be shown visually.
4. Script the spoken words around the slides.
5. Finish slide design.
6. Rehearse repeatedly.

### Slide Rules

- each slide should have a sentence or phrase stating the point
- text slides clarify structure
- exhibit slides prove a point visually
- the slide deck should reflect the story flow, not just the data inventory

## The Minto Operating Procedure

When writing any serious document, run this sequence:

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

## Final Quality Gates

Before finalizing a memo, report, spec, or presentation, verify:

- [ ] Can I state the governing thought in one sentence?
- [ ] Does the introduction create the exact question the document answers?
- [ ] Do the points below each statement answer the question it raises?
- [ ] Are sibling points the same kind of idea?
- [ ] Is every grouping in a clear order?
- [ ] If a grouping is inductive, can I name the plural noun?
- [ ] Are any points only topics instead of ideas?
- [ ] Are action points worded as end products?
- [ ] Does the problem definition clearly identify Opening Scene, Disturbing Event, R1, and R2?
- [ ] Are "issues" phrased as real decision questions where needed?
- [ ] Do headings and slide titles tell the same story as the argument?
- [ ] Does the conclusion or Next Steps section leave the reader knowing what to think or do?

## Anti-Patterns to Avoid

### 1. Background Before Answer

Starting with a dump of context before stating the answer.

### 2. Topic Headings Instead of Ideas

Using labels like `Background`, `Findings`, `Issues`, `Recommendations` as if they were thinking.

### 3. Categories in the Key Line

Putting buckets where statements should be.

### 4. Mixed Abstraction Levels

Combining results, substeps, causes, and evidence in one sibling group.

### 5. Vague Action Language

Using words like improve, strengthen, enhance, optimize without a concrete end state.

### 6. Data First, Structure Later

Collecting facts without a problem definition or hypothesis tree.

### 7. Fake Issue Lists

Calling a bag of topics "key issues" instead of framing actual yes-or-no questions.

### 8. Deduction Disguised as Induction

Listing points that are actually a chain of reasoning but presenting them like a class of similar ideas.

### 9. Induction Without a Plural Noun

Grouping points that do not belong to the same class.

### 10. Presentations as Visual Recitation

Putting report text on slides with no story flow, no point-driven headlines, and no rehearsal-driven script.

## Reference Templates

### Decision Memo Template

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

### Problem-Solving Template

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

### Presentation Template

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

## Modern Extension for AI-Assisted Work

This section is inference, not direct source material from Minto.

The Minto method is especially useful in AI-assisted workflows because it forces explicit structure:

- reader
- question
- answer
- grouped support
- logical order

If we give an AI system those five things up front, we reduce drift, vague prose, and context sprawl.

A strong prompt often mirrors a Minto introduction:

- Here is the reader.
- Here is the question they need answered.
- Here is the answer we currently believe.
- Here are the support points we need proved or refined.
- Return the output top-down.

## Bottom Line

The Minto Pyramid Principle is not just a writing trick. It is a discipline for:

- deciding what you are really saying
- forcing the reader's question into the open
- grouping support points into valid logic
- defining problems before analyzing them
- turning analysis into prose, headings, and slides without losing the argument

If the structure is right, the writing usually becomes easy.
If the structure is wrong, better prose only hides the problem.
