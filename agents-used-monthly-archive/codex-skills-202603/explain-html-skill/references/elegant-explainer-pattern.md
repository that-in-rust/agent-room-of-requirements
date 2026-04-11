# Elegant Explainer Pattern

Use this reference when turning technical source material into a standalone HTML explainer.

## Design Goal

Produce a page that feels like a guided tour, not a dump of implementation notes.

- Start with intuition.
- Earn the right to go deeper.
- Use visuals to simplify, not decorate.
- Keep every section grounded in source artifacts.

This pattern is adapted from the Samantha-style explainers in your local workflow and takes strong pacing cues from Paras Chopra's "How LLMs Actually Work": a visual journey, a mystery-first opening, short conceptual steps, and steady movement from intuition to machinery.

## Inputs To Gather

Collect the minimum source set that lets you explain the system honestly:

- Core implementation files
- Supporting interfaces, traits, or protocols
- Specs, notes, or PRD material
- Existing diagrams, tests, or issue threads
- Any earlier explainer page that establishes local tone

Write down:

- The one-sentence thesis
- The main loop or lifecycle
- The primary actors
- The persisted state
- The failure classes
- The extension points or plugin boundaries
- The top 3 details that are surprising or easy to misunderstand

## Narrative Spine

Use this as the default story arc. Delete steps that do not apply.

### 1. Open With The Mystery

State the real problem in human terms. Why does this system exist, and why is it hard?

Good patterns:

- "Data lives here, but it needs to move there."
- "The system looks simple, but the tricky part is not losing state."
- "Two components speak the same protocol but very different native dialects."

### 2. Show The Core Loop

Give the reader the heartbeat early. If the system is cyclical, show the cycle as a numbered flow.

Preferred sequence:

- open or initialize
- read or poll
- transform
- deliver or apply
- commit or checkpoint

If the code uses different verbs, mirror the code's verbs.

### 3. Compare Modes Or Implementations

When multiple paths exist, use side-by-side cards.

Good comparison targets:

- polling vs event-driven
- source vs sink
- implementation A vs implementation B
- happy path vs recovery path
- sync vs async mode

Keep the comparison asymmetric if reality is asymmetric. Do not force false symmetry.

### 4. Explain State And Safety

Readers usually get lost here. Slow down.

Focus on:

- what gets remembered
- when it gets persisted
- what happens on crash or retry
- what counts as committed vs tentative
- whether behavior is at-most-once, at-least-once, or effectively once

Use a small diagram or branch view when commit/discard behavior matters.

### 5. Surface Architecture Boundaries

Show what is pluggable, what is fixed, and where the runtime takes over.

Typical questions:

- What does the author implement directly?
- What does the framework, container, or runtime provide?
- Where are the seams for adding new adapters or connectors?

### 6. Cover Failure Modes And Tradeoffs

Split failures into buckets when possible.

Useful buckets:

- transient vs fatal
- recoverable vs unrecoverable
- user error vs infrastructure error
- correctness tradeoff vs performance tradeoff

Keep this section concrete. Name a few real examples from the code or notes.

### 7. Close With Compression

End with a simple summary that compresses the system into one sentence or short rhythm.

Examples of the pattern:

- "Poll. Transform. Deliver. Checkpoint. Repeat."
- "Read state, decide, apply, persist, recover."

## Component Palette

Use the template's components intentionally.

### Hero

Use for:

- the plain-language title
- a subtitle that says why the page exists
- one framing line that promises a guided tour

### Metaphor Card

Use for one idea that benefits from analogy.

Rules:

- Keep it short.
- Follow it with the exact mechanical explanation.
- Delete it if the metaphor does more harm than good.

### Flow Steps

Use for any repeatable lifecycle. Favor 4 to 6 steps.

### Code Block

Use only one or two code snippets that reveal something important. Do not paste large files.

Good candidates:

- a representative query
- a trait or interface shape
- a retry condition
- a config fragment

### Diagram Block

Use for small ASCII-style sketches, pipeline views, or branch logic.

The diagram should still make sense if copied into plain text.

### Comparison Cards

Use when two paths need contrast. Label them clearly and keep each card tight.

### Option Cards

Use for finite lists:

- payload formats
- offset types
- cleanup strategies
- config modes

### Summary Table

Use near the end for a compact cross-system sweep. Keep the columns simple enough to read on a laptop.

## Writing Rules

- Prefer short paragraphs.
- Define jargon once, then reuse it consistently.
- Use the exact nouns from the source where precision matters.
- Explain the why, not just the what.
- Keep the tone calm and factual.
- Do not oversell. Let the mechanics be interesting.

## Visual Rules

- Keep the page as one HTML file.
- Keep CSS and JavaScript inline unless the user asks otherwise.
- Keep motion subtle.
- Keep the palette coherent.
- Keep the page readable on mobile.
- Prefer text-first diagrams over image dependencies.

## Source Grounding Checklist

Before finalizing, confirm:

- Every major claim maps back to a source artifact.
- The main loop is visible by the second act.
- The page names what state is persisted and when.
- The explanation distinguishes mechanism from metaphor.
- The footer lists the files or notes used.
- Placeholder text is gone.
