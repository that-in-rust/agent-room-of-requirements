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
- Is it ASCII-only, unless the user explicitly asked for Unicode?

## Layout Checks

- Stay within the chosen width budget.
- Keep the main path visually straight.
- Keep related boxes aligned.
- Minimize connector crossings.
- Prefer whitespace over visual clutter.
- Split the diagram if a single figure is carrying too much meaning.

## Label Checks

- Keep box labels short.
- Put actions on arrows when possible.
- Avoid repeating the same word in every node.
- Add a legend only when abbreviations or symbols would otherwise confuse the reader.

## Failure Modes

These are common bad outcomes:

- a box contains a paragraph
- the diagram needs the author to narrate it line by line
- diagonal connectors create ambiguity
- one label floats between two possible arrows
- a wide diagram wraps in Markdown or terminal output
- decorative ASCII art overwhelms the meaning

## Finish Criteria

A diagram is ready when:

- it is readable in a monospaced block
- the main structure is clear without explanation
- the labels are short and specific
- the layout does not collapse when copied into plain text
- a validator pass finds no ASCII, tab, trailing-space, or width violations
