# Progress Journal Schema

Use this schema for every checkpoint entry.

```markdown
## TDD Session State: [Date/Time]

### Current Phase: [Red | Green | Refactor]

### Tests Written:
- [Test name]: [Status] - [Brief description]
- [Optional: file path and line references]

### Implementation Progress:
- [Component/Function]: [Status] - [What changed]
- [Cross-file or cross-crate dependencies]

### Current Focus:
[Current task objective]

### Next Steps:
1. [Immediate next action]
2. [Following action]
3. [Subsequent action]

### Context Notes:
- [Key decisions and rationale]
- [Approaches attempted]
- [Blockers or unresolved questions]
- [Technical debt noted]

### Performance/Metrics:
- [Benchmarks, budgets, limits, or N/A]
```

## Minimal Completion Rules

- Always include one explicit phase.
- Always include at least one next step.
- Always capture failing tests when in `Red`.
- Always capture implementation surface changed when in `Green`.
- Always capture debt or cleanup targets when in `Refactor`.

## Multi-Component Tracking

When work spans modules, crates, or services:
- List each touched component separately.
- State dependency direction (for example: `crate-a -> crate-b`).
- Note which tests validate each component.

## Example Entry

```markdown
## TDD Session State: 2026-02-27 19:10Z

### Current Phase: Green

### Tests Written:
- test_create_message_rejects_empty_body: passing - validates 400 for empty payload
- test_create_message_deduplicates_client_message_id: failing - duplicate path not implemented

### Implementation Progress:
- src/http/messages.rs: partial handler implemented for validation path
- src/domain/message_service.rs: dedupe function stub introduced

### Current Focus:
Implement dedupe branch and make failing integration test pass.

### Next Steps:
1. Implement message lookup by client_message_id.
2. Return existing persisted record when duplicate detected.
3. Re-run integration test and then full suite.

### Context Notes:
- Decided to keep dedupe logic in domain service to avoid HTTP coupling.
- Need fixture helper for duplicate payload setup.

### Performance/Metrics:
- Current p95 for create_message: 1.8ms in local benchmark.
```
