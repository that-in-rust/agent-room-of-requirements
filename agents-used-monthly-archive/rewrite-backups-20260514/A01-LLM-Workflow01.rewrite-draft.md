# LLM Workflow v01: Work Type Differentiation

Not all work deserves the same process.
The point of this file is to choose the lightest process that still protects quality.

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

```mermaid
flowchart TD
    Work[Incoming Work] --> Classify{What type?}

    Classify -->|Something broke| BUG[Bug]
    Classify -->|Small improvement<br/>to existing| ENHANCE[Enhancement]
    Classify -->|New capability<br/>clear scope| FEATURE[Feature]
    Classify -->|New system<br/>unclear scope| PRODUCT[Product]

    BUG --> BugFlow[Bug Flow<br/>Diagnose -> Fix -> Verify]
    ENHANCE --> EnhanceFlow[Enhancement Flow<br/>Light PRD -> TDD]
    FEATURE --> FeatureFlow[Feature Flow<br/>PRD -> ARCH -> TDD]
    PRODUCT --> ProductFlow[Product Flow<br/>Discovery -> PRD -> ARCH -> Spikes -> TDD]
```

## Flow 1: Bug Flow (Hours)

**Use this when**: something that used to work no longer works.

```mermaid
flowchart TD
    subgraph BUG["Bug Flow"]
        Reproduce[1. Reproduce] --> Diagnose[2. Diagnose]
        Diagnose --> WriteTest[3. Write Failing Test]
        WriteTest --> Fix[4. Fix]
        Fix --> Verify[5. Verify]
        Verify --> UpdateAnti[6. Update Anti-Patterns]
    end

    BugReport[Bug Report<br/>Steps, expected, actual,<br/>environment] -.-> Reproduce

    AntiPatterns[Anti-Pattern Registry<br/>Why it happened,<br/>how to prevent it] -.-> UpdateAnti
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

**Use this when**: the work extends an existing pattern instead of creating a new one.

```mermaid
flowchart TD
    subgraph ENHANCE["Enhancement Flow"]
        Scope[1. Scope Check] --> LightPRD[2. Light PRD]
        LightPRD --> FindExisting[3. Find Existing Patterns]
        FindExisting --> TDD[4. TDD]
        TDD --> Review[5. Quick Review]
    end

    Scope -->|Needs new rails| Escalate[Escalate to Feature Flow]

    ExistingCode[Existing Code<br/>Similar features,<br/>interfaces, tests] -.-> FindExisting

    LightPRDTemplate[Light PRD<br/>What, why, done when,<br/>what is out of scope] -.-> LightPRD
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

If you can describe the work as "do X like we do Y," it is probably an enhancement.
If you cannot find a Y, it is probably a feature.

## Flow 3: Feature Flow (Weeks)

**Use this when**: the capability is new, but the scope is still clear and bounded.

```mermaid
flowchart TD
    subgraph FEATURE["Feature Flow"]
        PRDv1[1. PRDv1<br/>User journey focus] --> PRDv2[2. PRDv2<br/>Architecture-aware]
        PRDv2 --> PRDv3[3. PRDv3<br/>Minimized]
        PRDv3 --> ARCH1[4. ARCHv1<br/>Initial design]
        ARCH1 --> ARCH2[5. ARCHv2<br/>Varied + challenged]
        ARCH2 --> ARCH3[6. ARCHv3<br/>Anti-pattern filtered]
        ARCH3 --> TDD[7. TDD]
        TDD --> Review[8. Review]
        Review --> Ship[9. Ship + Observe]
    end

    ARCH2 -.->|Simpler architecture?| PRDv2

    UserContext[User Journey] -.-> PRDv1
    DepGraph[Dependency Graph] -.-> PRDv2
    PriorArt[Prior Art] -.-> ARCH1
    AntiPatterns[Anti-Patterns] -.-> ARCH3
    Idioms[Idiomatic Patterns] -.-> TDD
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

**Use this when**: the scope is unclear, the domain is new, or you might be solving the wrong problem.

```mermaid
flowchart TD
    subgraph PRODUCT["Product Flow"]
        subgraph DISCOVER["Discovery"]
            Signals[1. Signal Collection] --> Problem[2. Problem Framing]
            Problem --> Size[3. Opportunity Sizing]
            Size --> Hypotheses[4. Key Hypotheses]
        end

        subgraph VALIDATE["Validation"]
            Hypotheses --> Spike1[5. Spike: Feasibility]
            Spike1 --> Spike2[6. Spike: Desirability]
            Spike2 --> Spike3[7. Spike: Viability]
        end

        subgraph BUILD["Build"]
            Spike3 --> MVP_PRD[8. MVP PRD]
            MVP_PRD --> MVP_ARCH[9. MVP Architecture]
            MVP_ARCH --> MVP_TDD[10. MVP TDD]
            MVP_TDD --> Learn[11. Learn]
            Learn --> Iterate{Iterate or pivot?}
            Iterate -->|Iterate| MVP_PRD
            Iterate -->|Pivot| Hypotheses
        end
    end

    UserResearch[User Research<br/>Interviews, observation,<br/>current alternatives] -.-> Signals

    SpikePatterns[Spike Patterns<br/>Fast experiments,<br/>success criteria,<br/>learning extraction] -.-> Spike1
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

```mermaid
flowchart TD
    Start[New Work Item] --> Q1{Is something<br/>broken?}
    Q1 -->|Yes| BUG[Bug Flow]
    Q1 -->|No| Q2{Does similar<br/>code exist?}
    Q2 -->|Yes, extend it| ENHANCE[Enhancement Flow]
    Q2 -->|No| Q3{Is scope<br/>clear?}
    Q3 -->|Yes, bounded| FEATURE[Feature Flow]
    Q3 -->|No, uncertain| PRODUCT[Product Flow]
```

**Ask in this order**

1. Did something break?
2. Am I extending an existing pattern?
3. Can I define done right now?
4. If not, am I still discovering the problem?

## Reference Files by Work Type

```mermaid
flowchart TD
    subgraph FILES["Reference File Tiers"]
        T1[Tier 1: Always<br/>S06, S07, S08]
        T2[Tier 2: Phase-Specific<br/>S01-S05]
        T3[Tier 3: Domain<br/>D01-D04]
        T4[Tier 4: Codebase<br/>C01-C04]
    end

    BUG[Bug] --> T1
    BUG --> T4

    ENHANCE[Enhancement] --> T1
    ENHANCE --> T4

    FEATURE[Feature] --> T1
    FEATURE --> T2
    FEATURE --> T4

    PRODUCT[Product] --> T1
    PRODUCT --> T2
    PRODUCT --> T3
    PRODUCT --> T4
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
If the real work keeps blowing past the expected budget, the classification is probably wrong.

## Updated Master Workflow

```mermaid
flowchart TD
    subgraph CLASSIFY["Step 0: Classify Work"]
        Input[Work Item] --> Type{What type?}
        Type -->|Broken| BUG
        Type -->|Extend existing| ENHANCE
        Type -->|New, clear scope| FEATURE
        Type -->|New, unclear scope| PRODUCT
    end

    subgraph BUG["Bug Flow"]
        B1[Reproduce] --> B2[Diagnose] --> B3[Test] --> B4[Fix] --> B5[Update Anti-Patterns]
    end

    subgraph ENHANCE["Enhancement Flow"]
        E1[Scope Check] --> E2[Light PRD] --> E3[Find Patterns] --> E4[TDD] --> E5[Review]
    end

    subgraph FEATURE["Feature Flow"]
        F1[PRD] --> F2[ARCH] --> F3[TDD] --> F4[Review] --> F5[Ship]
        F2 -.-> F1
    end

    subgraph PRODUCT["Product Flow"]
        P1[Discovery] --> P2[Hypotheses] --> P3[Spikes] --> P4[MVP] --> P5[Learn]
        P5 -.-> P2
    end

    BUG --> Done[Done]
    ENHANCE --> Done
    FEATURE --> Done
    PRODUCT --> Done

    Done --> Input
```

## The Common-Sense Test

Before starting, ask:

1. What kind of work is this?
2. What is the lightest process that still protects quality?
3. What is the time budget?
4. Which files actually matter for this kind of work?

The goal is not maximum process.
The goal is minimum viable process with maximum confidence.
