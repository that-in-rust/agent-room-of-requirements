# AI-Native Meta-Patterns Digest

Source reference: `/Users/amuldotexe/Downloads/notes01-agent (1).md`

Use this digest to justify choices while producing executable specs.

## 1) Measured Outcomes to Preserve

| Metric | Before patterns | After patterns | Observed improvement |
| --- | --- | --- | --- |
| Compile attempts (avg) | 4.9 | 1.6 | 67% fewer attempts |
| Production bugs | 1 per 100 LOC | 1 per 1000 LOC | 90% reduction |
| Context accuracy | ~60% | ~95% | 58% improvement |
| Onboarding time | 2-3 weeks | 3-5 days | 70% faster |

Treat these as directional targets, not guaranteed outcomes.

## 2) Seven Core Principles (Operational Form)

1. LLMs behave like search + assimilation systems.
- Bias with specific keywords and semantic names.

2. Iteration is required.
- Use explicit rounds: explore, constrain, refine, verify.

3. Context windows forget.
- Write short summary checkpoints after milestones.

4. Explicit reasoning improves quality.
- Ask for assumption checks and flaw detection.

5. Anti-patterns prevent repeat failures.
- Keep concrete "do not repeat" lists.

6. TDD-first reduces ambiguity.
- Write tests first to define executable contracts.

7. Learning is cumulative.
- Keep reusable prompt and workflow patterns.

## 3) Four-Word Naming Convention (4WNC)

Pattern:

```text
verb_constraint_target_qualifier
```

Examples:
- `filter_implementation_entities_only`
- `render_box_with_title_unicode`
- `save_visualization_output_to_file`
- `create_database_connection_pool_async`

Rules:
- Use four words for new function names where feasible.
- Preserve external API compatibility when required.
- Prefer high semantic density over short names.

## 4) TDD-First Loop

```text
STUB -> RED -> GREEN -> REFACTOR -> VERIFY
```

Execution policy:
- STUB: Write test and expected interface first.
- RED: Confirm failure reason.
- GREEN: Implement minimum behavior.
- REFACTOR: Improve structure safely.
- VERIFY: Run full checks and traceability pass.

## 5) Executable Requirement Pattern

Prefer this structure:

```markdown
**WHEN** <condition>
**THEN** the system SHALL <behavior>
**AND** SHALL <measurable constraint>
**SHALL** <edge-case behavior>
```

Do not accept:
- "Make it better"
- "Optimize"
- "Improve performance"

Require measurable constraints:
- Throughput, latency, memory, reliability, or error-rate bounds.

## 6) Context Budget Guidance

| Task | Suggested budget | Selection strategy |
| --- | --- | --- |
| Quick explanation | 2k tokens | Direct callers/callees only |
| Code review | 4k tokens | Include transitive depth 1-2 |
| Bug investigation | 6k tokens | Include error paths |
| Refactoring | 8k tokens | Include blast radius |

Apply discovery before deep analysis:
1. Discovery
2. Search
3. Traversal
4. Analysis

## 7) 2026 Agent Patterns to Reuse

1. Give agents a computer.
- Use filesystem and shell as primary primitives.

2. Keep action space small.
- Prefer few atomic tools; compose with shell.

3. Use progressive disclosure.
- Load details only when needed.

4. Offload context to files.
- Save plans and summaries for long tasks.

5. Optimize cacheability.
- Keep static instructions stable.

6. Isolate context with sub-agents.
- Parallelize independent checks when possible.

7. Evolve context from trajectories.
- Reflect and update prompts/skills based on outcomes.

## 8) Anti-Patterns Checklist

- Expecting perfect first-pass output.
- Shipping requirements without explicit tests.
- Mixing multiple features into one version with partial completion.
- Keeping TODO/STUB placeholders in production changes.
- Claiming performance gains without benchmark evidence.
