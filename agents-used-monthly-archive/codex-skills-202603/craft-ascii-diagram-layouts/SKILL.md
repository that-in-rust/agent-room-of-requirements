---
name: craft-ascii-diagram-layouts
description: Create high-quality monospaced ASCII diagrams for architecture, flows, sequences, trees, state transitions, comparisons, and terminal-friendly documentation. Use when Codex needs to explain systems in plain text, Markdown, README files, commit messages, code comments, design notes, or terminals where images, Mermaid, or Unicode box-drawing are unavailable, undesirable, or too heavy.
---

# Craft ASCII Diagram Layouts

## Goal

Turn structure into plain-text diagrams that are readable in a monospaced font, survive copy-paste, and still make sense in raw Markdown or a terminal.

## Pick The Right Diagram Type

1. Use `System Map` for components and relationships.
2. Use `Flow Diagram` for step-by-step processing or request lifecycles.
3. Use `Sequence Diagram` for actors exchanging messages over time.
4. Use `Tree Diagram` for directory layouts, hierarchies, and decision branches.
5. Use `Comparison Grid` for before/after, option tradeoffs, or capability tables.

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

6. Review and tighten.
- Remove decorative noise.
- Shorten labels inside boxes.
- Add a legend only if a reader would otherwise guess.
- Run [check_ascii_diagram_quality.py](scripts/check_ascii_diagram_quality.py) when working from a file.

## Default Style Rules

- Use ASCII characters only unless the user explicitly asks for Unicode box-drawing.
- Use one visual vocabulary per diagram:
  - boxes: `+`, `-`, `|`
  - arrows: `-->`, `<--`, `|`, `v`, `^`
  - branches: `|`, `+`, `\`
- Keep nouns inside boxes and actions on arrows.
- Prefer 3 to 7 primary nodes per diagram.
- Split the diagram when one figure tries to show both architecture and sequence at full detail.

## Use The Bundled Resources

- Use [ASCII diagram pattern library](references/ascii-diagram-pattern-library.md) to choose a layout and copy a fitting skeleton.
- Use [ASCII diagram review checklist](references/ascii-diagram-review-checklist.md) to catch readability problems before finishing.
- Use [check_ascii_diagram_quality.py](scripts/check_ascii_diagram_quality.py) to validate ASCII-only output, tabs, trailing whitespace, and width.

## Output Contract

Return results in this order when the user asks for a substantial diagram:

1. `Title`
2. `Legend` if needed
3. `Diagram`
4. `Reading Notes`

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

## Context Strategy

Load progressively:

1. Load this `SKILL.md`.
2. Load [ASCII diagram pattern library](references/ascii-diagram-pattern-library.md) to choose a shape and copy a fitting pattern.
3. Load [ASCII diagram review checklist](references/ascii-diagram-review-checklist.md) before finalizing or reviewing a diagram.
4. Run [check_ascii_diagram_quality.py](scripts/check_ascii_diagram_quality.py) when validating a file-backed diagram.

## References

- [ASCII diagram pattern library](references/ascii-diagram-pattern-library.md)
- [ASCII diagram review checklist](references/ascii-diagram-review-checklist.md)
