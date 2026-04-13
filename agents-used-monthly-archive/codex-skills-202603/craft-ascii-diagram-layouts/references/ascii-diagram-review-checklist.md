# ASCII Diagram Review Checklist

## Table Of Contents

1. First-pass checks
2. Layout checks
3. Label checks
4. Failure modes
5. Finish criteria

## First-Pass Checks

- Can the reader tell what type of diagram this is in under five seconds?
- Is the reading direction obvious?
- Does the diagram still make sense in raw plain text?
- Is it strict ASCII-only?
- Does the page feel composed, not dumped?
- Is there enough whitespace for the eye to rest?
- Does each major section have one obvious job?

## Layout Checks

- Stay within the chosen width budget.
- Keep prose lines within the chosen prose width.
- Keep the main path visually straight.
- Keep related boxes aligned.
- Minimize connector crossings.
- Prefer whitespace over visual clutter.
- Split the diagram if a single figure is carrying too much meaning.
- If there is prose plus a diagram, give each its own visual zone.
- If there are repeated concepts, align them as a row or column instead of staggering them.
- If there are repeated cards, keep their widths and heights consistent.
- If the page is tall, make each screenful feel like one coherent chunk.

## Label Checks

- Keep box labels short.
- Put actions on arrows when possible.
- Avoid repeating the same word in every node.
- Add a legend only when abbreviations or symbols would otherwise confuse the reader.
- If a side note exists, keep it shorter than the line it annotates.
- If glossary-style lines exist, keep the separator column aligned.

## Failure Modes

These are common bad outcomes:

- a box contains a paragraph
- the diagram needs the author to narrate it line by line
- diagonal connectors create ambiguity
- one label floats between two possible arrows
- a wide diagram wraps in Markdown or terminal output
- decorative ASCII art overwhelms the meaning
- the whole page is one dense blob with no hierarchy
- the diagram explains nothing without surrounding prose, or the prose duplicates the diagram completely
- panel widths drift for no reason
- the page forces horizontal scanning when vertical stacking would be clearer

## Finish Criteria

A diagram is ready when:

- it is readable in a monospaced block
- the main structure is clear without explanation
- the labels are short and specific
- the layout does not collapse when copied into plain text
- a validator pass finds no ASCII, tab, trailing-space, or width violations
- a validator pass finds no prose-width or alignment violations in editorial mode
- the composition still feels deliberate when viewed as a full page
