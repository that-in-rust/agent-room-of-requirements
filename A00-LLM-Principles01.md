# The 12 Principles of LLM-Native Development

This is a working reference for LLM-assisted engineering.
The point is not to sound clever.
The point is to make outcomes more predictable.

## Summary: The 12 Principles at a Glance

| # | Principle | Core point | Default move |
| --- | --- | --- | --- |
| 1 | LLMs are retrieval systems | The model retrieves against the context you give it | Use precise names, types, constraints, and input context |
| 2 | Iteration is required | First output is usually a draft | Explore, constrain, refine, verify |
| 3 | Context windows forget | Long sessions lose earlier decisions | Write summary checkpoints |
| 4 | Rubber duck debugging finds weak spots | Explanation pressure exposes weak reasoning | Ask it to explain, challenge, and restate the work |
| 5 | Negative knowledge is leverage | "Do not do this" removes bad paths fast | Keep anti-patterns and failure notes |
| 6 | Tests are the spec | Executable checks beat prose | Write the test before the implementation |
| 7 | Four-word names are a strong default | Names shape retrieval quality | Prefer clear, specific, stable names |
| 8 | Match process to work type | Bugs and products do not need the same process | Use the lightest process that still protects quality |
| 9 | PRD and architecture should co-evolve | Scope and design simplify each other | Let architecture discoveries remove requirements |
| 10 | Serialize state | Progress disappears without checkpoints | Save phase, tests, decisions, next steps |
| 11 | Delegate with rules | Vibes create drift | Use explicit routing rules |
| 12 | Close the loop | Teams improve only if they learn from outcomes | Record failures, fixes, and wins |

## Principle 1: LLMs Are Retrieval Systems

```text
Compare the two mental models.

Myth: [You] -> [LLM Brain] -> [Answer]

Reality: [You] -> [Search] -> [Patterns] -> [Answer]

The second model gives you something to tune.
```

LLMs are better understood as retrieval-and-composition systems
than as clean reasoners.
The quality of the output depends heavily on the quality of the
input context.

- Treat prompts like search queries.
- Use precise names, types, and constraints.
- Give the model the right input context so it can retrieve the
  relevant patterns, methods, and examples.
- When output is off, fix the inputs before blaming the model.

## Principle 2: Iteration Is Required

```text
Read this as a sequence of passes.

+-----------+
| Round 1   |
| Explore   |
+-----------+
      |
      v
+-----------+
| Round 2   |
| Constrain |
+-----------+
      |
      v
+-----------+
| Round 3   |
| Refine    |
+-----------+
      |
      v
+-----------+
| Round 4   |
| Verify    |
+-----------+

Single shot  = faster start, weaker finish
Four passes  = slower start, better odds
```

The first output is usually a direction, not a result.
Good work comes from deliberate passes, not one lucky prompt.

- Explore: get the rough shape.
- Constrain: add rules, types, interfaces, and limits.
- Refine: simplify and tighten.
- Verify: prove the result against tests or checks.

## Principle 3: Context Windows Forget

```text
Context over time

Turn 1-5    --> strong
Turn 6-10   --> still good
Turn 11-15  --> fading
Turn 16-20  --> weak
Turn 21+    --> easy to lose earlier decisions

Checkpoint path

Turn 15 --> [summary note] --> Turn 21 starts with context again
```

Long sessions decay.
If a decision matters later, put it in a file.

- Summarize after major decisions.
- Save requirements, architecture choices, and open questions.
- Use files as memory, not just the chat thread.

## Principle 4: Rubber Duck Debugging Finds Weak Spots

```text
Compare the direct path with the reviewed path.

Without critique: [Output] -> [Ship it] -> [Bug]

With critique:
[Output] -> [What assumptions?]
         -> [What could fail?]
         -> [Can I explain it?]
                         |
                         v
                      [Revise]

Critique is cheaper than repair.
```

This is rubber duck debugging in LLM form.
You ask the model to slow down, explain itself, and surface the weak
parts of its own reasoning.

LLMs are fluent by default.
Fluency hides mistakes unless you force explanation and review.

- Ask it to explain the solution in plain steps.
- Ask what assumptions the solution depends on.
- Ask what could fail at runtime, at the edges, or in maintenance.
- Ask it to restate the design more simply.

The philosophy is simple: if the model cannot explain the move
clearly, it probably does not understand the move clearly.
If the explanation falls apart, the design probably does too.

## Principle 5: Negative Knowledge Is Leverage

```text
Positive example

[one good path] --> maybe reused

Negative knowledge

[bad path 1] --> blocked
[bad path 2] --> blocked
[bad path 3] --> blocked

What remains: fewer wrong moves
```

Positive examples help.
Negative examples prevent repeats.

- Keep a file of bugs, traps, and failure patterns.
- Write anti-patterns in concrete language.
- Reuse them when prompting, reviewing, and refactoring.

One avoided bug is often more valuable than one polished example.

## Principle 6: Tests Are the Spec

```text
Vague prose

[written requirement] --> interpret --> guess --> maybe right

Executable spec

[failing test] --> target is clear --> implement --> pass or fail
```

If the test is clear, the implementation target is clear.
If the spec is vague, the model fills gaps with guesses.

- Write the failing test first.
- Let the test define names, types, and behavior.
- Treat prose as support for the test, not a substitute for it.

## Principle 7: Four-Word Names Are a Strong Default

```text
Read the gradient from vague to useful.

filter
  |
  +--> too broad

filter_entities
  |
  +--> still broad

filter_implementation_entities_only
  |
  +--> clear enough to guide the model

filter_only_the_implementation_entity_variants
  |
  +--> signal starts to blur again

The goal is specificity, not ritual.
```

The point is not numerology.
The point is semantic density.

- Short names are often vague.
- Long names often dilute the signal.
- Four words is a good default because it often forces specificity
  without turning into a paragraph.

Use the pattern when it helps.
Do not preserve a bad public API just to obey a slogan.

## Principle 8: Match Process to Work Type

```text
Route work by uncertainty and risk.

Bug         --> light process --> fix + regression test
Enhancement --> light process --> extend an existing pattern
Feature     --> medium process --> PRD + design + TDD
Product     --> heavy process --> discovery + spikes + MVP

Mismatch costs:
- heavy process on a bug    --> waste
- light process on a product --> wrong build

Use the lightest process that still protects quality.
```

Process should match risk and uncertainty.
Too much process is drag.
Too little process is rework.

- Bugs need speed plus regression coverage.
- Enhancements should reuse existing rails.
- Features need bounded design and TDD.
- Products need discovery before build.

See [A01-LLM-Workflow01.md](./A01-LLM-Workflow01.md) for the
detailed routing.

## Principle 9: PRD and Architecture Should Co-Evolve

```text
Linear

[PRD final] --> [Architecture] --> [Build]

Co-evolution

[PRD v1] --> [ARCH v1]
    ^           |
    |           v
[PRD v2] <-- [simpler path found]
    |
    v
[ARCH v2] --> [Build less, but better]
```

Requirements and architecture should push on each other.
The design should reveal what can be removed, not just what can be
built.

- Start with the user value, not a maximal scope list.
- Let architecture discoveries simplify the PRD.
- Stop when the scope is clear, useful, and hard to simplify further.

## Principle 10: Serialize State

```text
Without checkpoints

[Session 1] --> [Break] --> [Session 2 starts cold]

With checkpoints

[Session 1] --> [phase + tests + decisions + next steps]
                   |
                   v
                [Break]
                   |
                   v
             [Session 2 resumes cleanly]
```

If progress matters, write it down.
A checkpoint should let someone else resume without guesswork.

- Capture the current phase.
- Record test status.
- Record key decisions and rejected options.
- Write the next steps plainly.

If the note cannot restart the work, it is not a checkpoint yet.

## Principle 11: Delegate With Rules

```text
Implicit

[Task] --> [gut feel] --> maybe proceed / maybe ask

Explicit

[Task] --> Can I write a failing test now?
             | yes
             v
          [Proceed]

             | no, need facts
             v
          [Research]

             | no, unclear requirement
             v
          [Escalate]
```

Delegation needs a rule, not a mood.
The cleanest rule is usually: can I define correctness right now?

- If yes, proceed.
- If not because you lack facts, research.
- If not because the requirement is unclear, escalate.

This keeps autonomy useful without letting it drift.

## Principle 12: Close the Loop

```text
Open loop

[Build] --> [Ship] --> [Next feature]

Closed loop

[Build] --> [Ship] --> [Observe]
                         |
                         v
                  [Failure or success]
                         |
             +-----------+-----------+
             |                       |
             v                       v
      [update anti-patterns]   [update patterns]
                         \       /
                          v     v
                       [next feature]
```

Teams improve only if results change future behavior.
Shipping without learning is just repetition.

- Record failures and their causes.
- Record wins worth repeating.
- Feed both back into prompts, tests, and review habits.

## How They Connect

```text
Read left to right, then back through learning.

[Foundation] -> [Quality] -> [Process]
      ^                           |
      |                           |
      +-------- learning ---------+

Foundation = model behavior
Quality    = output quality
Process    = safe delivery
```

These principles fit together:

- Foundation explains how the model behaves.
- Quality improves what you get from it.
- Process decides how work moves safely.

The through-line is simple:

> Fill the context with the right information at the right time.
