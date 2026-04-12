---
name: craft-ascii-diagram-layouts
description: Create high-quality monospaced ASCII diagrams and ASCII-like explanatory layouts for architecture, flows, sequences, trees, state transitions, comparisons, and terminal-friendly documentation. Use when Codex needs to explain systems in plain text, Markdown, README files, commit messages, code comments, design notes, or terminals where images and Mermaid are unavailable, undesirable, or too heavy, and when the user wants diagrams that feel editorial, spacious, and visually composed rather than merely functional.
---

# Craft ASCII Diagram Layouts

## Goal

Turn structure into plain-text diagrams that are readable in a monospaced font, survive copy-paste, and still make sense in raw Markdown or a terminal.

## Target Aesthetic

Aim for composed monospace pages, not bare diagrams.

- Give the diagram a clear title.
- Add one short setup sentence before dense visuals.
- Use generous vertical spacing.
- Align related text into invisible columns.
- Treat the page like a poster or notebook spread, not a terminal dump.

When the user shows a reference with restrained icons or other non-ASCII accents, match the style carefully:

- Keep the structure in plain ASCII.
- Use Unicode or emoji only as accent, never as the structural backbone.
- Validate with `--allow-unicode --editorial` when checking that richer style.

## Pick The Right Diagram Type

1. Use `System Map` for components and relationships.
2. Use `Flow Diagram` for step-by-step processing or request lifecycles.
3. Use `Sequence Diagram` for actors exchanging messages over time.
4. Use `Tree Diagram` for directory layouts, hierarchies, and decision branches.
5. Use `Comparison Grid` for before/after, option tradeoffs, or capability tables.

For screenshot-level quality, also pick a page archetype before drawing:

- Use `Narrated Glossary Plus Card Strip` when the explanation needs aligned concept definitions followed by a visual row.
- Use `Layered Explainer Page` when the explanation should unfold in sections such as “essence first, mechanism second.”
- Use `Diagram With Sidecar Notes` when short annotations would clutter the main path if left inline.

If the diagram needs curved lines, dense graphs, heavy crossing edges, or visual polish beyond monospaced text, stop and recommend Mermaid, HTML, or an image instead.

## Workflow

1. Extract the shape before drawing.
- List the nodes.
- List the edges or transitions.
- Decide the reading order.
- Drop any label that does not help the reader navigate.

2. Choose a width budget before drafting.
- Default to 80 columns.
- Stretch to 100 only when the user clearly benefits.
- If the diagram still feels cramped, split it into two diagrams instead of squeezing labels.

3. Draft the layout in coarse blocks first.
- Place the main actors or stages.
- Keep the most important path visually straight.
- Prefer top-down over left-right when space is tight.
- If the page needs explanation plus visuals, reserve clear zones for both instead of mixing prose into the diagram body.

4. Route connectors with discipline.
- Prefer straight vertical and horizontal lines.
- Avoid decorative diagonals.
- Avoid crossed connectors whenever possible.
- Keep arrow labels short and attach them close to the arrow they describe.

5. Clean the text surface.
- Use spaces, never tabs.
- Keep ASCII only by default.
- Use consistent box and arrow characters.
- Put the diagram in a fenced `text` block when returning Markdown.
- Use visual rhythm: headline, short prose, diagram, then notes.

6. Review and tighten.
- Remove decorative noise.
- Shorten labels inside boxes.
- Add a legend only if a reader would otherwise guess.
- Run [check_ascii_diagram_quality.py](scripts/check_ascii_diagram_quality.py) when working from a file.

## Default Style Rules

- Use ASCII characters only unless the user explicitly asks for Unicode box-drawing.
- If the user supplies a reference that uses emoji or sparse Unicode accents, keep the layout ASCII-first and use those accents sparingly.
- Use one visual vocabulary per diagram:
  - boxes: `+`, `-`, `|`
  - arrows: `-->`, `<--`, `|`, `v`, `^`
  - branches: `|`, `+`, `\`
- Keep nouns inside boxes and actions on arrows.
- Prefer 3 to 7 primary nodes per diagram.
- Split the diagram when one figure tries to show both architecture and sequence at full detail.
- Prefer page composition over density. White space is part of the diagram.

## Use The Bundled Resources

- Use [Editorial monospace layouts](references/editorial-monospace-layouts.md) when the goal is “ASCII like the screenshots” rather than a minimal wire diagram.
- Use [ASCII diagram pattern library](references/ascii-diagram-pattern-library.md) to choose a layout and copy a fitting skeleton.
- Use [ASCII diagram review checklist](references/ascii-diagram-review-checklist.md) to catch readability problems before finishing.
- Use [check_ascii_diagram_quality.py](scripts/check_ascii_diagram_quality.py) to validate ASCII-only output, tabs, trailing whitespace, width, and composed-page heuristics with `--editorial`.

## Output Contract

Return results in this order when the user asks for a substantial diagram:

1. `Title`
2. `Setup` as one short paragraph or 1 to 3 aligned glossary lines
3. `Diagram Section` or `Diagram Sections`
4. `Legend` if needed
5. `Reading Notes`

If the user wants screenshot-level quality, prefer a composed page:

1. `Headline`
2. `Short setup paragraph`
3. `Visual zone 1`
4. `Visual zone 2` when helpful
5. `Short reading notes`

The diagram itself should usually be wrapped like this:

```text
+---------+
| Client  |
+---------+
     |
     v
+---------+
| Server  |
+---------+
```

## Guardrails

- Do not fake polish with noisy ASCII art.
- Do not mix ASCII and Unicode box-drawing unless the user explicitly asks for Unicode.
- Do not let labels become paragraphs.
- Do not exceed the width budget when a split diagram would be clearer.
- Do not use a single diagram to show every detail of a system.
- Do not force ASCII when the task really needs Mermaid, HTML, or an image.
- Do not confuse density with sophistication. The reference quality in the screenshots comes from composition, hierarchy, and spacing.

## Context Strategy

Load progressively:

1. Load this `SKILL.md`.
2. Load [Editorial monospace layouts](references/editorial-monospace-layouts.md) when the user wants “ASCII like this” or shares a rich reference image.
3. Load [ASCII diagram pattern library](references/ascii-diagram-pattern-library.md) to choose a shape and copy a fitting pattern.
4. Load [ASCII diagram review checklist](references/ascii-diagram-review-checklist.md) before finalizing or reviewing a diagram.
5. Run [check_ascii_diagram_quality.py](scripts/check_ascii_diagram_quality.py) when validating a file-backed diagram. Add `--editorial` for composed explainer pages.

## References

- [Editorial monospace layouts](references/editorial-monospace-layouts.md)
- [ASCII diagram pattern library](references/ascii-diagram-pattern-library.md)
- [ASCII diagram review checklist](references/ascii-diagram-review-checklist.md)
