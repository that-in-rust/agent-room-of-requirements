---
name: explain-html-skill
description: Create polished, single-file technical explainer HTML pages in the elegant narrative style used for pages like .prd/ELI5/index.html. Use when Codex needs to turn source code, architecture notes, PRDs, connectors, workflows, or mixed technical artifacts into a scrollable ELI5 or executive explainer, especially for requests such as "how this actually works", "make an elegant HTML explainer", "build a visual journey", or "convert this understanding page into a reusable format".
---

# Explain HTML Skill

## Overview

Build a self-contained explainer page that a teammate can open locally in a browser and understand without a build step. Reuse the bundled template, bootstrap script, and pattern guide so the result stays visually consistent, source-grounded, and easy to reproduce across projects.

## Quick Start

1. Read the source artifacts first: code, notes, specs, diagrams, issue threads, and existing explainers.
2. Read [references/elegant-explainer-pattern.md](references/elegant-explainer-pattern.md) before writing the page.
3. Bootstrap a new page with the script:

```bash
python3 scripts/create_elegant_explainer_html.py \
  --output .prd/ELI5/index.html \
  --hero-label "Connector Explainer" \
  --hero-title "How the Source Connector Actually Works" \
  --hero-subtitle "A visual journey through the polling loop, state, and failure handling." \
  --source core/connectors/sources/mongodb_source/src/lib.rs \
  --source core/connectors/sdk/src/lib.rs
```

4. Replace scaffold text with source-grounded explanations. Delete sections that do not serve the story.
5. Keep the output as one HTML file with inline CSS and inline JavaScript.

## Read The Source

Extract the explanation from evidence, not vibes.

- Identify the main loop, handshake, or lifecycle first.
- List the nouns that matter: actors, state objects, checkpoints, queues, topics, tables, slots, offsets, retries.
- Identify the system boundaries: what enters, what transforms, what persists, what fails, what gets retried.
- Capture the exact terms used by the codebase and define them once in plain language.
- Keep a short source list for the footer so readers can trace the page back to code and notes.

If the request points at an existing explainer such as `.prd/ELI5/index.html`, inspect it and preserve its section density, pacing, and tone unless the user asks for a redesign.

## Shape The Story

Use the Paras Chopra-style "visual journey" pacing as the baseline inspiration, then adapt it to the repo's subject matter and house tone. In practice that means:

- Open with a strong problem statement or mystery.
- Move from intuition to mechanism in stages.
- Use short sections that each answer one question.
- Introduce metaphors to lower the cognitive barrier, then immediately tie them back to exact mechanics.
- Put dense comparisons into side-by-side cards or small tables instead of long prose.
- End with a high-signal takeaway that compresses the whole system into one repeatable sentence.

Prefer 5 to 8 acts. A strong default outline is:

1. The problem or mystery
2. The core loop or data path
3. Key modes, variants, or implementations
4. State, safety, and checkpointing
5. Architecture and extension points
6. Failure modes and tradeoffs
7. Big picture and takeaway

## Build The Page

Start from the bundled template at [assets/elegant-explainer-template.html](assets/elegant-explainer-template.html). It already includes the layout primitives that make this pattern repeatable:

- Hero section with a clear title and subtitle
- Dot navigation for major acts
- Reveal-on-scroll staging
- Metaphor cards for intuition
- Flow steps for loops or lifecycles
- Code blocks for one or two telling examples
- Diagram blocks for simplified ASCII-style mechanics
- Comparison cards for competing modes or systems
- Option cards for configuration choices or data formats
- Summary table plus final takeaway

Keep the visuals intentional:

- Use one dominant visual direction, not a grab bag of widgets.
- Keep paragraphs short enough to scan on a laptop screen.
- Make every diagram legible in plain text before styling.
- Use animation sparingly; motion should support orientation, not spectacle.
- Preserve mobile readability.

## Guardrails

- Do not invent behavior that is not supported by source artifacts.
- Do not let metaphors replace the actual mechanism.
- Do not overload the page with every implementation detail. Pick the details that unlock understanding.
- Do not bury the main loop. Readers should understand the heartbeat of the system by the second act.
- Do include the source list in the footer.
- Do call out uncertainty directly if the source material is incomplete or conflicting.

## Finish Strong

Before finishing, verify:

- The title answers "what is this page explaining?"
- The page can be opened directly from disk in a browser.
- The story moves from overview to mechanism to caveats to takeaway.
- Each major claim can be traced back to code or notes.
- Unused scaffold sections and placeholder copy are removed.
- The footer lists the key source files or documents.

## Resources

- Use [references/elegant-explainer-pattern.md](references/elegant-explainer-pattern.md) for the narrative beats, UI component rules, and final checklist.
- Use [scripts/create_elegant_explainer_html.py](scripts/create_elegant_explainer_html.py) to bootstrap new explainers quickly.
- Use [assets/elegant-explainer-template.html](assets/elegant-explainer-template.html) as the single-file shell that keeps the look and behavior consistent.
