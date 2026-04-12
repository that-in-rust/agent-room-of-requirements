# Editorial Monospace Layouts

## Table Of Contents

1. What makes the reference style feel better
2. Pattern: narrated glossary plus card strip
3. Pattern: layered explainer page
4. Pattern: sidecar annotations
5. Composition rules

## What Makes The Reference Style Feel Better

The screenshots are not better because of more lines or more boxes. They are better because they behave like composed pages.

What is happening:

- a strong headline frames the page
- one short paragraph prepares the reader
- aligned definitions create rhythm
- diagrams sit in clearly separated visual zones
- whitespace gives the eye places to rest
- important contrasts are repeated in both prose and visuals

This means the skill should build **monospace explainer pages**, not only isolated diagrams.

## Pattern: Narrated Glossary Plus Card Strip

Use this when the user wants a concept explained through a list of aligned definitions and a visual row of examples.

```text
----
Variation 6: Smart Pointers -- "The book is in a special case"

These are advanced. The book is wrapped in a container that
provides extra abilities.

Box<Self>      = Book in a locked box. One owner.
Rc<Self>       = Book with a sign-out sheet. Many owners.
Arc<Self>      = Same idea, but thread-safe.
Pin<&mut Self> = Book nailed to the table. You can write,
                 but you cannot move it.

+-------------+  +-------------+  +-------------+  +-------------+
| Box<Self>   |  | Rc<Self>    |  | Arc<Self>   |  | Pin<&mut>   |
|             |  |             |  |             |  |             |
|   [book]    |  |   [book]    |  |   [book]    |  |   [book]    |
|             |  |             |  |             |  |             |
| 1 owner     |  | N owners    |  | N owners    |  | can't move  |
| on heap     |  | 1 thread    |  | N threads   |  | it          |
+-------------+  +-------------+  +-------------+  +-------------+
```

Use it when:

- the topic has 3 to 6 concepts to compare
- each concept benefits from both prose and a small visual metaphor

## Pattern: Layered Explainer Page

Use this when the user wants staged understanding, where each section reveals the system one level deeper.

```text
Level 1: The Essence

Every message lives in exactly one tier at any moment.

Producer                          Consumer
   |                                 ^
   v                                 |
TIER 1           TIER 2           TIER 3
+---------+      +---------+      +---------+
| Disk    |      | Frozen  |      | Journal |
+---------+      +---------+      +---------+

read direction:  ======= left to right =======>
write direction: <====== right to left ========

---
Level 2: The Write Path

Producer sends batch
    |
    v
Step 1: append(batch)           <- instant, RAM only
    |
    v
Step 2: threshold check
    |
  +----+-----------------------------+
  |NO  |YES                          |
  v    v                             |
[wait] Step 3: COMMIT                |
             |                       |
             v                       |
        batch.freeze()               |
             |                       |
             v                       |
        Step 4: PERSIST              |
```

Use it when:

- the page has a “first intuition, then mechanism” structure
- one diagram would become too dense without staged sections

## Pattern: Sidecar Annotations

Use short notes to the right or below the main path when the main flow would become unreadable if the notes lived inline.

```text
Step 1: journal.append(batch)        <- RAM only
Step 2: threshold check              <- decides whether to commit
Step 3: persist                      <- disk write happens here
```

Rules:

- keep side notes short
- align them consistently
- do not let side notes become a second paragraph stream

## Composition Rules

- Start with title, then one short setup block.
- Use blank lines between prose and diagrams.
- Keep one idea per visual zone.
- Align repeated structures into rows or columns.
- Use the same indentation level for peer concepts.
- If a page has two major sections, label them explicitly.
- If icons are used, treat them as accents, not structure.
