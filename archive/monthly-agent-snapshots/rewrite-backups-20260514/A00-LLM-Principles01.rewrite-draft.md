# The 12 Principles of LLM-Native Development

This is a working reference for LLM-assisted engineering.
The goal is simple: make outcomes more predictable.

## Summary: The 12 Principles at a Glance

| # | Principle | Core point | Default move |
| --- | --- | --- | --- |
| 1 | LLMs are retrieval systems | The model responds to cues more than intent | Use precise names, types, and constraints |
| 2 | Iteration is required | First output is usually a draft | Explore, constrain, refine, verify |
| 3 | Context windows forget | Long sessions lose earlier decisions | Write summary checkpoints |
| 4 | Self-critique finds weak spots | Plausible output is not the same as correct output | Ask what is wrong, risky, or assumed |
| 5 | Negative knowledge is leverage | "Do not do this" removes bad paths fast | Keep anti-patterns and failure notes |
| 6 | Tests are the spec | Executable checks beat prose | Write the test before the implementation |
| 7 | Four-word names are a strong default | Names shape retrieval quality | Prefer clear, specific, stable names |
| 8 | Match process to work type | Bugs and products do not need the same process | Use the lightest process that still protects quality |
| 9 | PRD and architecture should co-evolve | Scope and design simplify each other | Let architecture discoveries remove requirements |
| 10 | Serialize state | Progress disappears without checkpoints | Save phase, tests, decisions, next steps |
| 11 | Delegate with rules | Vibes create drift | Use explicit routing rules |
| 12 | Close the loop | Teams improve only if they learn from outcomes | Record failures, fixes, and wins |

## Principle 1: LLMs are Retrieval Systems

```mermaid
flowchart LR
    subgraph MYTH["The Myth"]
        You1[You] -->|Ask question| Brain[LLM Brain]
        Brain -->|Thinks deeply| Answer1[Novel Answer]
    end

    subgraph REALITY["The Reality"]
        You2[You] -->|Keywords| Search[LLM Search]
        Search -->|Retrieves| Patterns[Training Patterns]
        Patterns -->|Assembles| Answer2[Pattern Mashup]
    end
```

LLMs are better understood as retrieval-and-composition systems than as clean reasoners.
That means naming, prompting, and context are part of the implementation.

- Treat prompts like search queries.
- Treat naming like retrieval design.
- When output is off, fix the inputs before blaming the model.

## Principle 2: Iteration Is Required

```mermaid
flowchart TD
    subgraph QUALITY["Output Quality by Iteration"]
        R1[Round 1<br/>Explore] -->|40% correct| R2[Round 2<br/>Constrain]
        R2 -->|70% correct| R3[Round 3<br/>Refine]
        R3 -->|90% correct| R4[Round 4<br/>Validate]
        R4 -->|99% correct| Final[Final]
    end

    subgraph COST["Cost vs Quality"]
        SingleShot[Single Shot<br/>Fast but risky]
        Iterated[4 Iterations<br/>Slower but reliable]
    end
```

The first output is usually a direction, not a result.
Good work comes from deliberate passes, not one lucky prompt.

- Explore: get the rough shape.
- Constrain: add rules, types, interfaces, and limits.
- Refine: simplify and tighten.
- Verify: prove the result against tests or checks.

## Principle 3: Context Windows Forget

```mermaid
flowchart TD
    subgraph MEMORY["Context Retention Over Turns"]
        T1[Turn 1-5<br/>100% retained] --> T2[Turn 6-10<br/>90% retained]
        T2 --> T3[Turn 11-15<br/>70% retained]
        T3 --> T4[Turn 16-20<br/>40% retained]
        T4 --> T5[Turn 21+<br/>~10% retained]
    end

    subgraph SOLUTION["The Checkpoint Solution"]
        Checkpoint[Summary Document] -.->|Re-inject| T5
        T5 -->|Restored to| Recovered[90% context]
    end
```

Long sessions decay.
If a decision matters later, put it in a file.

- Summarize after major decisions.
- Save requirements, architecture choices, and open questions.
- Use files as memory, not just the chat thread.

## Principle 4: Self-Critique Finds Weak Spots

```mermaid
flowchart TD
    subgraph HIDDEN["Without Self-Critique"]
        Output1[LLM Output] --> Ship1[Ship It]
        Ship1 --> Bug[Bug in Production]
    end

    subgraph SURFACED["With Self-Critique"]
        Output2[LLM Output] --> Q1{What assumptions<br/>am I making?}
        Q1 --> Q2{What could<br/>go wrong?}
        Q2 --> Q3{Can I explain<br/>this simply?}
        Q3 -->|Found flaw| Fix[Fix Before Ship]
        Q3 -->|No flaws| Ship2[Ship Safely]
    end
```

LLMs are fluent by default.
Fluency hides mistakes unless you force a second pass.

- Ask what is wrong with the answer.
- Ask what assumptions it depends on.
- Ask for the simplest explanation of the solution.

If the explanation falls apart, the design probably does too.

## Principle 5: Negative Knowledge Is Leverage

```mermaid
flowchart LR
    subgraph POSITIVE["Positive Example"]
        Good[One Good Way] --> Maybe[LLM might<br/>match it]
    end

    subgraph NEGATIVE["Negative Examples"]
        Bad1[Bad Way 1] --> Block1[Blocked]
        Bad2[Bad Way 2] --> Block2[Blocked]
        Bad3[Bad Way 3] --> Block3[Blocked]
        Block1 & Block2 & Block3 --> Remaining[Only good<br/>ways remain]
    end
```

Positive examples help.
Negative examples prevent repeats.

- Keep a file of bugs, traps, and failure patterns.
- Write anti-patterns in concrete language.
- Reuse them when prompting, reviewing, and refactoring.

One avoided bug is often more valuable than one polished example.

## Principle 6: Tests Are the Spec

```mermaid
flowchart LR
    subgraph VAGUE["Vague Spec"]
        Words[Written Requirements] -->|Interpreted| LLM1[LLM]
        LLM1 -->|Guesses| Output1[Maybe Right?]
    end

    subgraph PRECISE["Test as Spec"]
        Test[Failing Test] -->|Exact target| LLM2[LLM]
        LLM2 -->|Matches| Output2[Definitely Right]
    end
```

If the test is clear, the implementation target is clear.
If the spec is vague, the model fills gaps with guesses.

- Write the failing test first.
- Let the test define names, types, and behavior.
- Treat prose as support for the test, not a substitute for it.

## Principle 7: Four-Word Names Are a Strong Default

```mermaid
flowchart TD
    subgraph SPECTRUM["Semantic Density Spectrum"]
        W1[1 word<br/>filter] -->|Too sparse| Problem1[Matches too much<br/>LLM confused]
        W2[2 words<br/>filter_entities] -->|Still sparse| Problem2[Still ambiguous]
        W4[4 words<br/>filter_implementation<br/>_entities_only] -->|Strong default| Good[Clear intent]
        W6[6 words<br/>filter_only_implementation<br/>_type_entities_from_list] -->|Too dense| Problem3[Attention diluted]
    end
```

The point is not numerology.
The point is semantic density.

- Short names are often vague.
- Long names often dilute the signal.
- Four words is a good default because it tends to force specificity without turning into a paragraph.

Use the pattern when it helps.
Do not preserve a bad public API just to obey a slogan.

## Principle 8: Match Process to Work Type

```mermaid
flowchart TD
    subgraph MATCH["Match Process to Work"]
        Bug[Bug<br/>Something broke] -->|Hours| Light1[Light process<br/>Fix + test]
        Enhance[Enhancement<br/>Small improvement] -->|Days| Light2[Light process<br/>Find pattern + extend]
        Feature[Feature<br/>New capability] -->|Weeks| Medium[Medium process<br/>PRD + ARCH + TDD]
        Product[Product<br/>New system] -->|Months| Heavy[Heavy process<br/>Discovery + Spikes + MVP]
    end

    subgraph WASTE["Mismatch = Waste"]
        BugHeavy[Bug with heavy process] --> Waste1[Waste: over-engineering]
        ProductLight[Product with light process] --> Waste2[Waste: building the wrong thing]
    end
```

Process should match risk and uncertainty.
Too much process is drag.
Too little process is rework.

- Bugs need speed plus regression coverage.
- Enhancements should reuse existing rails.
- Features need bounded design and TDD.
- Products need discovery before build.

See [A01-LLM-Workflow01.md](./A01-LLM-Workflow01.md) for the detailed routing.

## Principle 9: PRD and Architecture Should Co-Evolve

```mermaid
flowchart LR
    subgraph WRONG["Linear"]
        PRD1[PRD Final] --> ARCH1[Architecture]
        ARCH1 --> Build1[Build]
    end

    subgraph RIGHT["Co-Evolution"]
        PRD2[PRD v1] --> ARCH2[ARCH v1]
        ARCH2 -->|Simpler path?| PRD3[PRD v2 Simplified]
        PRD3 --> ARCH3[ARCH v2]
        ARCH3 -->|Even simpler?| PRD4[PRD v3 Minimal]
        PRD4 --> Build2[Build Minimal]
    end
```

Requirements and architecture should push on each other.
The design should reveal what can be removed, not just what can be built.

- Start with the user value, not a maximal scope list.
- Let architecture discoveries simplify the PRD.
- Stop when the scope is clear, useful, and hard to simplify further.

## Principle 10: Serialize State

```mermaid
flowchart TD
    subgraph WITHOUT["Without State Tracking"]
        Session1[Session 1<br/>Progress made] --> Break1[Break]
        Break1 --> Session2[Session 2<br/>Start over]
    end

    subgraph WITH["With State Tracking"]
        Session3[Session 1<br/>Progress made] --> Save[Save State<br/>Phase + Tests + Decisions]
        Save --> Break2[Break]
        Break2 --> Load[Load State]
        Load --> Session4[Session 2<br/>Continue exactly]
    end
```

If progress matters, write it down.
A checkpoint should let someone else resume without guesswork.

- Capture the current phase.
- Record test status.
- Record key decisions and rejected options.
- Write the next steps plainly.

If the note cannot restart the work, it is not a checkpoint yet.

## Principle 11: Delegate With Rules

```mermaid
flowchart TD
    subgraph IMPLICIT["Implicit"]
        Task1[Task] --> Vibes{Gut feeling}
        Vibes --> Maybe[Maybe proceed?<br/>Maybe ask?]
    end

    subgraph EXPLICIT["Explicit"]
        Task2[Task] --> Test{Can I write<br/>a failing test<br/>right now?}
        Test -->|Yes| Proceed[Proceed]
        Test -->|No, need info| Research[Delegate: Research]
        Test -->|No, unclear req| Escalate[Escalate: Human]
    end
```

Delegation needs a rule, not a mood.
The cleanest rule is usually: can I define correctness right now?

- If yes, proceed.
- If not because you lack facts, research.
- If not because the requirement is unclear, escalate.

This keeps autonomy useful without letting it drift.

## Principle 12: Close the Loop

```mermaid
flowchart TD
    subgraph OPEN["Open Loop"]
        Build1[Build] --> Ship1[Ship]
        Ship1 --> Next1[Next Feature]
        Next1 --> Build1
    end

    subgraph CLOSED["Closed Loop"]
        Build2[Build] --> Ship2[Ship]
        Ship2 --> Observe[Observe Production]
        Observe --> Learn{Did it work?}
        Learn -->|No| Diagnose[Diagnose Why]
        Learn -->|Yes| Extract[Extract Pattern]
        Diagnose --> UpdateAnti[Update Anti-Patterns]
        Extract --> UpdatePatterns[Update Patterns]
        UpdateAnti --> Next2[Next Feature]
        UpdatePatterns --> Next2
    end
```

Teams improve only if results change future behavior.
Shipping without learning is just repetition.

- Record failures and their causes.
- Record wins worth repeating.
- Feed both back into prompts, tests, and review habits.

## How They Connect

```mermaid
flowchart TD
    subgraph FOUNDATION["Foundation"]
        P1[1. Retrieval]
        P3[3. Context]
        P7[7. Naming]
    end

    subgraph QUALITY["Quality"]
        P2[2. Iteration]
        P4[4. Self-Critique]
        P5[5. Negative Knowledge]
        P6[6. Tests]
    end

    subgraph PROCESS["Process"]
        P8[8. Work Type]
        P9[9. PRD + ARCH]
        P10[10. State]
        P11[11. Delegation]
        P12[12. Feedback]
    end

    FOUNDATION --> QUALITY
    QUALITY --> PROCESS
    PROCESS -->|Learning| FOUNDATION
```

These principles fit together:

- Foundation explains how the model behaves.
- Quality improves what you get from it.
- Process decides how work moves safely.

The through-line is simple:

> Fill the context with the right information at the right time.
