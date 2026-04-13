# Editorial Monospace Layouts

This reference is for long terminal pages that should feel composed, calm, and teachable in raw ASCII.

## Table Of Contents

1. What terminal references do better
2. Pattern: glossary plus panels
3. Pattern: layered walkthrough
4. Pattern: two-column compare
5. Pattern: mechanism trace
6. Pattern: tall variation gallery
7. Page composition rules

## What Terminal References Do Better

The strong reference pages are not better because they have fancier symbols. They are better because they:

- split the explanation into small teachable sections
- repeat panel sizes and gutters
- keep prose narrow and calm
- use the same alignment anchors again and again
- reveal the system top to bottom instead of forcing horizontal scanning

The goal is not “draw one great diagram.” The goal is “compose one great terminal page.”

## Pattern: Glossary Plus Panels

Use this when the reader needs a quick verbal definition first, then a repeated visual row.

```text
----
Variation 6: Smart Pointers

These wrappers change who owns the value and where it can travel.

Box<Self>      = one owner on the heap
Rc<Self>       = many owners, one thread
Arc<Self>      = many owners, many threads
Pin<&mut Self> = writable, cannot move

+-------------+  +-------------+  +-------------+  +-------------+
| Box<Self>   |  | Rc<Self>    |  | Arc<Self>   |  | Pin<&mut>   |
|             |  |             |  |             |  |             |
| 1 owner     |  | N owners    |  | N owners    |  | fixed in    |
| heap        |  | 1 thread    |  | N threads   |  | place       |
+-------------+  +-------------+  +-------------+  +-------------+
```

Use it when:

- the topic has 3 to 6 concepts
- the reader benefits from both naming and visual repetition

## Pattern: Layered Walkthrough

Use this when the explanation should unfold one layer at a time.

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
Step 1: append(batch)           <- RAM only
    |
    v
Step 2: threshold check
```

Use it when:

- the page has “intuition first, mechanism second”
- one section would otherwise become too dense

## Pattern: Two-Column Compare

Use this when the point is contrast and the two sides should be scanned together.

```text
Option A: Read Optimized            Option B: Write Optimized

+--------------------+             +--------------------+
| old data on disk   |             | new data in memory |
| simpler reads      |             | faster writes      |
| slower ingestion   |             | more coordination  |
+--------------------+             +--------------------+

Tradeoff:
- left side reduces moving parts
- right side reduces write latency
```

Use it when:

- there are exactly two dominant options
- the same categories should appear on both sides

## Pattern: Mechanism Trace

Use this when one path matters most and notes should sit beside it.

```text
Producer sends batch
    |
    v
Step 1: journal.append(batch)    <- instant, RAM only
    |
    v
Step 2: threshold check          <- commit if size is large enough
    |
    v
Step 3: batch.freeze()           <- becomes read-safe
    |
    v
Step 4: persist                  <- data reaches disk
```

Use it when:

- a single sequence carries the explanation
- annotations matter but should stay short

## Pattern: Tall Variation Gallery

Use this when the page should stack many compact variations down a long scroll.

```text
Variation 1: Direct Ownership

+-------------+
| owner = one |
| move = yes  |
+-------------+

Variation 2: Shared Ownership

+-------------+
| owners = N  |
| thread = 1  |
+-------------+

Variation 3: Shared + Thread-Safe

+-------------+
| owners = N  |
| thread = N  |
+-------------+
```

Use it when:

- each variation is small
- the page should read like an atlas or field guide

## Page Composition Rules

- lead with a title, not a diagram
- keep prose outside boxes
- let each section add one new idea
- keep card widths and gutters stable
- keep glossary separators aligned
- use `---` only for real section breaks
- prefer another section over another column when width gets tight
