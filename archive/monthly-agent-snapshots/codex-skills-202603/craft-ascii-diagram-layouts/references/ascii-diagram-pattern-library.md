# ASCII Diagram Pattern Library

## Table Of Contents

1. System map
2. Flow diagram
3. Sequence diagram
4. Tree diagram
5. Comparison grid
6. Card strip
7. Two-column compare
8. Mechanism trace
9. Pattern selection rules

## System Map

Use this when the reader needs to understand components and major relationships.

```text
+---------+      +-----------+      +----------+
| Client  | ---> | API Layer | ---> | Database |
+---------+      +-----------+      +----------+
     |                  |
     |                  v
     |            +-----------+
     +----------> | Cache     |
                  +-----------+
```

Good for:

- service boundaries
- data stores
- major integration points

Avoid when:

- time order matters more than topology

## Flow Diagram

Use this when the reader should follow a process from start to finish.

```text
+--------+
| Input  |
+--------+
    |
    v
+-----------+
| Validate  |
+-----------+
    |
    v
+-----------+
| Transform |
+-----------+
    |
    v
+--------+
| Output |
+--------+
```

Good for:

- ETL flows
- request lifecycles
- job pipelines

## Sequence Diagram

Use this when multiple actors exchange messages over time.

```text
Client        API         Worker       Database
  |            |            |             |
  |-- request->|            |             |
  |            |-- enqueue->|             |
  |            |            |-- write --->|
  |            |<-- ack ----|             |
  |<- 202 -----|            |             |
```

Good for:

- request/response flows
- async handoffs
- retry sequences

Rules:

- keep actors on one line
- move downward in time
- keep message labels short

## Tree Diagram

Use this for hierarchies, file trees, or branching decisions.

```text
project/
+-- src/
|   +-- main.rs
|   +-- lib.rs
+-- tests/
|   +-- smoke.rs
+-- Cargo.toml
```

Good for:

- directory layouts
- menu structures
- taxonomy views

## Comparison Grid

Use this when the point is contrast rather than flow.

```text
+------------+------------+------------+
| Option     | Strength   | Risk       |
+------------+------------+------------+
| ASCII      | Portable   | Less rich  |
| Mermaid    | Structured | Renderer   |
| HTML       | Flexible   | Heavier    |
+------------+------------+------------+
```

Good for:

- tool tradeoffs
- before/after snapshots
- feature matrices

## Card Strip

Use this when several concepts should feel like a coordinated gallery instead of a generic table.

```text
+-------------+  +-------------+  +-------------+
| In-Memory   |  | Frozen      |  | Persisted   |
|             |  |             |  |             |
|   [data]    |  |   [data]    |  |   [data]    |
|             |  |             |  |             |
| writable    |  | readable    |  | durable     |
| hot path    |  | shared      |  | on disk     |
+-------------+  +-------------+  +-------------+
```

Good for:

- visual metaphors
- ownership or tier comparisons
- compact concept galleries

## Two-Column Compare

Use this when the main point is contrast between exactly two alternatives.

```text
Option A                         Option B

+------------------+            +------------------+
| simpler reads    |            | faster writes    |
| more disk-first  |            | more RAM-first   |
+------------------+            +------------------+
```

Good for:

- before vs after
- approach A vs approach B
- read path vs write path

## Mechanism Trace

Use this when one path should dominate and side notes stay short.

```text
Step 1: append(batch)           <- RAM only
    |
    v
Step 2: threshold check         <- commit gate
    |
    v
Step 3: persist                 <- disk write
```

Good for:

- write paths
- lifecycle explanations
- commit or state transitions

## Pattern Selection Rules

- If topology matters, use `System Map`.
- If order matters, use `Flow Diagram`.
- If multiple actors exchange messages, use `Sequence Diagram`.
- If hierarchy matters, use `Tree Diagram`.
- If tradeoffs matter, use `Comparison Grid`.
- If repeated concepts should read like a gallery, use `Card Strip`.
- If two alternatives should be scanned together, use `Two-Column Compare`.
- If one sequence plus short notes should dominate, use `Mechanism Trace`.

When one diagram tries to do two of these jobs at once, split it.
