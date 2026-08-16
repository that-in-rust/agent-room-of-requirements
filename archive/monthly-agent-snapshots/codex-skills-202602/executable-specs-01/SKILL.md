---
name: executable-specs-01
description: Convert software requests into executable specifications with measurable WHEN...THEN...SHALL contracts, traceable requirement IDs, and TDD-first plans. Use when Codex needs to turn ambiguous feature ideas into testable acceptance criteria, generate unit/integration/performance test plans, enforce four-word naming conventions, or produce pre-commit quality gates for implementation work.
---

# Executable Specs 01

Use this skill to generate implementation-ready specs and test packets from product or engineering requests.

## Workflow

1. Parse the request into five inputs.
- Feature outcome
- Actors and boundaries
- Failure modes
- Performance and reliability limits
- Language/runtime constraints

2. Write requirement contracts with stable IDs.
- Format IDs as `REQ-<DOMAIN>-<NNN>.<REV>`.
- Use this structure for each contract:

```markdown
### REQ-API-001.0: Filter implementation entities

**WHEN** the caller passes a mixed entity list with implementation and interface entries
**THEN** the system SHALL return only implementation entities
**AND** SHALL preserve original ordering
**SHALL** return an empty list when no implementation entities exist
```

3. Convert each contract into executable verification.
- Map each `REQ-*` to at least one test.
- Prefer unit plus integration coverage.
- Add performance tests only when a metric is stated.
- Reject claims without measurable thresholds.

4. Plan TDD execution.
- `STUB`: Write failing test skeletons first.
- `RED`: Run tests and capture expected failure reason.
- `GREEN`: Implement minimal code to pass.
- `REFACTOR`: Simplify while keeping tests green.
- `VERIFY`: Run full suite and contract checks.

5. Apply four-word naming for generated symbols.
- Use `verb_constraint_target_qualifier`.
- Keep new function names at four words.
- Preserve existing public API names when compatibility is required; add wrappers for new compliant names when useful.

6. Emit a pre-commit quality gate.
- Verify tests and build pass.
- Verify no `TODO`, `STUB`, or `FIXME` in new code.
- Verify no unmeasured performance claims.
- Verify each requirement ID has at least one test reference.

## Output Contract

Return results in this order:

1. `Executable Requirements`
2. `Test Matrix`
3. `TDD Plan`
4. `Quality Gates`
5. `Open Questions`

Use concise traceability tables:

| req_id | test_id | type | assertion | target |
| --- | --- | --- | --- | --- |

## Guardrails

- Replace vague language like "make it faster" with explicit thresholds.
- Avoid narrative-only requirements; always include verification steps.
- Avoid performance claims without a measurement method.
- Separate functional and non-functional requirements.
- Cover empty input, invalid input, and timeout/error paths.

## Context Strategy

Use progressive loading:

1. Load this `SKILL.md`.
2. Load [Executable specs templates](./references/executable-specs-templates.md) for scaffolds.
3. Load [AI-native meta-patterns digest](./references/meta-patterns-reference.md) when rationale or process evidence is needed.
4. Write short checkpoint summaries after major iterations to avoid context drift.

## References

- [Executable specs templates](./references/executable-specs-templates.md)
- [AI-native meta-patterns digest](./references/meta-patterns-reference.md)
