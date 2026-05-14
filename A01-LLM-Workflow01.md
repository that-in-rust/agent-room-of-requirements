# LLM Workflow v01: Work Type Differentiation

Not all work deserves the same process.
The point of this file is to choose the lightest process that still
protects quality.

## Quick Classifier

| Work Type | Use it for | PRD | Architecture | TDD | Time |
| --- | --- | --- | --- | --- | --- |
| Bug | Something broke | None | None | Fix + regression test | Hours |
| Enhancement | Small change on existing rails | Light | Light | Yes | Days |
| Feature | New bounded capability | Yes | Yes | Full | Weeks |
| Product | New system or unclear scope | Deep | Extensive | Full + spikes | Months |

Over-process wastes time.
Under-process builds the wrong thing.

## Work Type Framework

```text
Classify before you load process.

Incoming work
     |
     v
What type?
     |
     +--> something broke            --> Bug flow
     +--> small improvement          --> Enhancement flow
     +--> new capability, clear      --> Feature flow
     +--> new system, unclear        --> Product flow

Pick the lightest safe route.
```

## Flow 1: Bug Flow (Hours)

Use this when something that used to work no longer works.

```text
Follow the shortest safe repair loop.

[Reproduce] -> [Diagnose] -> [Write test]
                               |
                               v
                             [Fix]
                               |
                               v
                            [Verify]
                               |
                               v
                    [Update anti-patterns]

End with a regression and a note.
```

**Default steps**

1. Reproduce the bug.
2. Find the root cause.
3. Write the regression test first.
4. Make the smallest fix that passes.
5. Run the relevant checks.
6. Record why it slipped through.

**Load these files**

- `S07-anti-patterns-registry.md`
- `C03-test-inventory.md`

**Do not load by default**

- PRD files
- architecture exploration
- spikes

## Flow 2: Enhancement Flow (Days)

Use this when the work extends an existing pattern instead of creating
a new one.

```text
Use this when the rails already exist.

[Scope check] -> [Light PRD] -> [Find pattern]
                                   |
                                   v
                                 [TDD]
                                   |
                                   v
                                [Review]

If new rails are needed, move to Feature Flow.
```

**Default steps**

1. Confirm the change fits existing rails.
2. Write a short PRD.
3. Find the closest prior example in the codebase.
4. Use TDD.
5. Review quickly and ship.

**Load these files**

- `C01-dependency-graph.md`
- `C02-existing-interfaces.md`
- `S08-idiomatic-patterns.md`

**Do not load by default**

- deep discovery
- long PRD cycles
- broad architecture exploration

**Rule of thumb**

If you can describe the work as "do X like we do Y," it is probably
an enhancement.
If you cannot find a Y, it is probably a feature.

## Flow 3: Feature Flow (Weeks)

Use this when the capability is new, but the scope is still clear and
bounded.

```text
PRD and architecture should tighten each other.

[PRD v1]  -> [ARCH v1]
    ^            |
    |            v
[PRD v2] <- simpler path found
    |
    v
[ARCH v2] -> [TDD] -> [Ship]

If the design simplifies scope, update the PRD.
```

**Default steps**

1. Write the first PRD from the user journey.
2. Tighten the PRD with implementation reality.
3. Minimize the scope.
4. Iterate architecture in parallel with the PRD.
5. Run TDD against the final shape.
6. Review and observe after shipping.

**Load these files**

- `S06`, `S07`, `S08`
- `C01-C04`
- domain-specific files when relevant

**Key rule**

Let architecture remove scope.
Do not treat the first PRD as sacred.

## Flow 4: Product Flow (Months)

Use this when the scope is unclear, the domain is new, or you might
be solving the wrong problem.

```text
Discovery

[Signals] --> [Problem] --> [Sizing] --> [Hypotheses]

Validation

[Hypotheses] --> [Feasibility] --> [Desirability] --> [Viability]

Build

[MVP PRD] --> [MVP ARCH] --> [MVP TDD] --> [Learn]
                                          |
                                          v
                                   iterate or pivot
```

**Default steps**

1. Define the problem before the feature list.
2. Write the key hypotheses.
3. Run spikes to test the risky assumptions.
4. Build the smallest useful MVP.
5. Learn from reality and loop.

**Load these files**

- `S01-problem-discovery-patterns.md`
- `S02-technical-spike-patterns.md`
- Tier 1 files for the build phase
- new domain files if the space is new

**Key rule**

Product work is about learning before scale.
Do not confuse activity with validation.

## The Classification Decision Tree

```text
Move through the questions in order.

New work item
     |
     v
Is something broken?
     | yes
     +--------------------------> Bug Flow
     |
     no
     |
     v
Does similar code exist?
     | yes
     +--------------------------> Enhancement Flow
     |
     no
     |
     v
Is scope clear?
     | yes
     +--------------------------> Feature Flow
     |
     no
     |
     v
Product Flow

Stop as soon as one answer is clear.
```

**Ask in this order**

1. Did something break?
2. Am I extending an existing pattern?
3. Can I define done right now?
4. If not, am I still discovering the problem?

## Reference Files by Work Type

```text
Use the tiers as a loading guide.

Tier 1: Always         -> S06, S07, S08
Tier 2: Phase-specific -> S01-S05
Tier 3: Domain         -> D01-D04
Tier 4: Codebase       -> C01-C04

Bug         -> Tier 1 + Tier 4
Enhancement -> Tier 1 + Tier 4
Feature     -> Tier 1 + Tier 2 + Tier 4
Product     -> Tier 1 + Tier 2 + Tier 3 + Tier 4

Load upward only when the work justifies it.
```

| Work Type | Load first | Usually skip |
| --- | --- | --- |
| Bug | S07, C03 | discovery, spikes |
| Enhancement | S08, C01-C02 | deep PRD, broad architecture |
| Feature | S06-S08, C01-C04 | discovery-heavy product work |
| Product | everything relevant | nothing by default |

## Time Budget by Work Type

| Work Type | PRD | ARCH | Spike | TDD | Review | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Bug | 0 | 0 | 0 | 2h | 30m | 2-4 hours |
| Enhancement | 30m | 0 | 0 | 4h | 1h | 1-2 days |
| Feature | 4h | 4h | 0-4h | 16h | 4h | 1-2 weeks |
| Product | 8h+ | 8h+ | 16h+ | 40h+ | 8h+ | 4+ weeks |

Time budget is a signal.
If the real work keeps blowing past the expected budget, the
classification is probably wrong.

## Updated Master Workflow

```text
This is the whole routing model at a glance.

Classify
  |
  +--> Bug         --> Reproduce -> Diagnose -> Test -> Fix -> Verify
  |
  +--> Enhancement --> Scope -> Light PRD -> Pattern -> TDD -> Review
  |
  +--> Feature     --> PRD <-> ARCH -> TDD -> Review -> Ship
  |
  +--> Product     --> Discovery -> Hypotheses -> Spikes -> MVP -> Learn
                                                           |
                                                           v
                                                       iterate/pivot

Choose one lane and stay disciplined inside it.
```

## The Common-Sense Test

Before starting, ask:

1. What kind of work is this?
2. What is the lightest process that still protects quality?
3. What is the time budget?
4. Which files actually matter for this kind of work?

The goal is not maximum process.
The goal is minimum viable process with maximum confidence.
