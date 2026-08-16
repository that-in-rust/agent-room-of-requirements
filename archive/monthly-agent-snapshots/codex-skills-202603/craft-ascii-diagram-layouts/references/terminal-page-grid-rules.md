# Terminal Page Grid Rules

Use this reference when the goal is a long ASCII explainer page that should feel deliberate in a terminal, not just technically valid.

## Table Of Contents

1. Canvas presets
2. Grid rules
3. Section anatomy
4. Repetition discipline
5. Screenful rhythm
6. Alignment rules

## Canvas Presets

Prefer one of these widths:

- `72 cols` for compact terminal output
- `84 cols` for most explainers
- `96 cols` for comparison-heavy pages

Use these prose targets:

- prose width: `52 to 64 cols`
- side note width: `18 to 28 cols`
- gutter between peer panels: `2 to 4 spaces`

When in doubt, narrow the prose and add more vertical sections.

## Grid Rules

- Pick one left margin and keep it.
- Pick one card width per repeated row and reuse it.
- Pick one glossary separator column and align to it.
- Pick one side-note anchor column and align to it.
- Use one blank line between local blocks.
- Use two blank lines between major sections when the page is tall.

## Section Anatomy

Most strong terminal sections follow this order:

1. section heading
2. short setup paragraph
3. local figure or panel row
4. optional short note or legend

Keep the setup paragraph short enough that the figure still dominates the section.

## Repetition Discipline

When several peer concepts appear together:

- keep their boxes the same width
- keep their box heights the same unless there is a good reason not to
- use parallel label phrasing
- keep gutters consistent
- avoid a “special” middle card unless the point is deliberate contrast

## Screenful Rhythm

Treat each 20 to 40 line stretch as one screenful.

Each screenful should do one job:

- define a concept
- compare a small set of options
- trace one mechanism
- summarize one layer

If a screenful tries to do more than one of those jobs, split it.

## Alignment Rules

Glossary lines:

```text
Box<Self>      = one owner on heap
Rc<Self>       = many owners, one thread
Arc<Self>      = many owners, many threads
Pin<&mut Self> = writable, cannot move
```

Side notes:

```text
Step 1: append(batch)             <- RAM only
Step 2: threshold check           <- decides commit
Step 3: persist                   <- disk write
```

Card rows:

```text
+-------------+  +-------------+  +-------------+
| In-Memory   |  | Frozen      |  | Persisted   |
|             |  |             |  |             |
| writable    |  | readable    |  | durable     |
+-------------+  +-------------+  +-------------+
```

If one line breaks the shared grid, fix the wording before changing the layout.
