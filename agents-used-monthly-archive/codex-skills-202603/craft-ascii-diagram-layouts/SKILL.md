---
name: craft-ascii-diagram-layouts
description: Create high-quality terminal-native ASCII explainer pages and diagrams for architecture, flows, sequences, trees, state transitions, comparisons, and codebase walkthroughs. Use when Codex needs to explain systems in plain text, .txt-style output, raw Markdown code blocks, commit messages, design notes, or terminals where the result must survive copy-paste without Unicode box-drawing, images, or Mermaid.
---

# Craft ASCII Diagram Layouts

## Goal

Turn structure into plain-text layouts that read well in a monospaced terminal, survive copy-paste, and still make sense as raw `.txt`.

## Target Aesthetic

Aim for terminal page systems, not isolated figures.

- Build for vertical scrolling. Height is cheap; width is expensive.
- Use a clear heading and one short setup paragraph per major section.
- Keep repeated panels on a visible grid with matching widths and gutters.
- Treat whitespace as structure, not leftover space.
- Make each 20 to 40 line stretch feel like one coherent screenful.
- Prefer calm alignment over decorative cleverness.

ASCII is the first-class mode:

- Use plain ASCII only.
- Do not rely on Unicode, emoji, or box-drawing.
- Make the page readable in a bare terminal with no styling.

## Pick The Right Page System

Choose the page system before the local diagram type.

1. Use `Tall Variation Gallery` for many compact panels stacked down a long page.
2. Use `Glossary Plus Panels` for aligned definitions followed by repeated cards.
3. Use `Layered Walkthrough` when the explanation should unfold one level deeper per section.
4. Use `Two-Column Compare` when the main point is contrast between two approaches.
5. Use `Mechanism Trace` when the reader should follow one path with short side notes.

Within a section, choose the local figure that best fits:

- `System Map` for components and relationships.
- `Flow Diagram` for ordered processing.
- `Sequence Diagram` for actors over time.
- `Tree Diagram` for hierarchies and branches.
- `Comparison Grid` for explicit tradeoffs.

If the page needs curved lines, dense graph topology, or visual polish beyond raw monospaced text, stop and recommend a non-ASCII format.

## Workflow

1. Outline the page before drawing any boxes.
- Write the page title.
- List the sections from top to bottom.
- Decide what each section teaches in one sentence.
- Keep one dominant visual move per section.

2. Choose the canvas and anchors.
- Default to 72, 84, or 96 columns.
- Keep prose wraps around 52 to 64 characters.
- Pick anchor columns for panels, glossary lines, and side notes.
- If the page feels wide, stack more sections instead of widening the canvas.

3. Draft the page in modules.
- Block out headings, prose, panels, and notes as separate zones.
- Give repeated cards the same width and usually the same height.
- Use consistent gutters between peer panels.
- Prefer stacked sections over giant all-in-one spreads.

4. Draw the local figures with discipline.
- Keep the main path visually straight.
- Prefer top-down flow when space is tight.
- Use short arrow labels and short box labels.
- Put paragraphs outside boxes, not inside them.

5. Tighten the writing.
- Use parallel phrasing for repeated concepts.
- Keep glossary separators aligned.
- Keep side notes shorter than the line they annotate.
- Let prose set up the diagram instead of narrating every line after it.

6. Use a layered teaching cadence when explaining a concept.
- Start with the essence in one sentence and one small figure.
- Then expand into key parts with one focused panel each.
- Only then add the mechanism trace or deeper walkthrough.
- Keep each deeper section visually related to the earlier one instead of redrawing from scratch in a totally different grammar.

7. Review the full scroll.
- Check that each screenful has a coherent purpose.
- Remove any section that repeats the previous one without adding a new angle.
- Run [check_ascii_diagram_quality.py](scripts/check_ascii_diagram_quality.py) with `--editorial` when working from a file.

## Default Style Rules

- Use ASCII characters only.
- Use one visual vocabulary per diagram:
  - boxes: `+`, `-`, `|`
  - arrows: `-->`, `<--`, `|`, `v`, `^`
  - branches: `|`, `+`, `\`
- Use `---` for section breaks when the page needs explicit separation.
- Keep nouns inside boxes and actions on arrows.
- Prefer 3 to 7 primary nodes per local figure.
- Keep repeated cards and comparison columns on the same width grid.
- Keep setup prose outside the diagram body.
- Prefer page composition over density. White space is part of the layout.
- Split vertically before you split the reader's attention horizontally.

## Use The Bundled Resources

- Use [Editorial monospace layouts](references/editorial-monospace-layouts.md) when the goal is a long terminal explainer page rather than one minimal figure.
- Use [Terminal page grid rules](references/terminal-page-grid-rules.md) when the layout needs stable widths, gutters, anchors, or section rhythm.
- Use [ASCII diagram pattern library](references/ascii-diagram-pattern-library.md) to choose a layout and copy a fitting skeleton.
- Use [ASCII diagram review checklist](references/ascii-diagram-review-checklist.md) to catch readability problems before finishing.
- Use [check_ascii_diagram_quality.py](scripts/check_ascii_diagram_quality.py) to validate ASCII-only output, tabs, trailing whitespace, width, prose width, and composed-page heuristics with `--editorial`.
- If the user also wants plain-English simplification, pair this skill with `explain_ai_native_eli5` and let this skill handle the terminal layout layer.

## Output Contract

Return results in this order when the user asks for a substantial diagram:

1. `Title`
2. `Setup` as one short paragraph
3. `Section` or `Sections`
4. `Legend` if needed
5. `Reading Notes`

If the user wants terminal screenshot-level quality, prefer a long ASCII page:

1. `Headline`
2. `Short setup paragraph`
3. `Section 1`
4. `Section 2`
5. `Section 3` when helpful
6. `Short reading notes`

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

- Do not fake richness with noisy ASCII art.
- Do not use Unicode box-drawing, emoji, or decorative symbols.
- Do not let labels become paragraphs.
- Do not exceed the width budget when a taller page would be clearer.
- Do not use one giant figure to show topology, sequence, glossary, and tradeoffs at the same time.
- Do not center content randomly; align it to a chosen column system.
- Do not make the reader pan horizontally to understand the page.
- Do not confuse density with sophistication. Terminal quality comes from composition, rhythm, and repetition.

## Context Strategy

Load progressively:

1. Load this `SKILL.md`.
2. Load [Editorial monospace layouts](references/editorial-monospace-layouts.md) when the user wants “ASCII like this” or needs a long scrollable explainer page.
3. Load [Terminal page grid rules](references/terminal-page-grid-rules.md) when the layout needs fixed widths, gutters, anchor columns, or section pacing.
4. Load [ASCII diagram pattern library](references/ascii-diagram-pattern-library.md) to choose a local figure and copy a fitting pattern.
5. Load [ASCII diagram review checklist](references/ascii-diagram-review-checklist.md) before finalizing or reviewing a page.
6. Run [check_ascii_diagram_quality.py](scripts/check_ascii_diagram_quality.py) when validating a file-backed page. Add `--editorial` for composed explainer pages.

## References

- [Editorial monospace layouts](references/editorial-monospace-layouts.md)
- [Terminal page grid rules](references/terminal-page-grid-rules.md)
- [ASCII diagram pattern library](references/ascii-diagram-pattern-library.md)
- [ASCII diagram review checklist](references/ascii-diagram-review-checklist.md)
