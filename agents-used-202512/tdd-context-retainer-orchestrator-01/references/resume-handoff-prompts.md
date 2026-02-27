# Resume and Handoff Prompts

Use these prompts to make context transitions explicit and reliable.

## Resume Prompts

### Quick Resume

```text
Load the latest progress journal snapshot and summarize:
1) current TDD phase,
2) currently failing tests,
3) immediate next step.
Then proceed with only step 1.
```

### Detailed Resume

```text
Read the latest checkpoint and report:
- test status delta since previous checkpoint,
- implementation files touched,
- unresolved blockers,
- risk areas for regression.
Propose a 3-step continuation plan.
```

## Handoff Prompts

### Developer Handoff

```text
Create a handoff note from the latest journal entry with:
- current phase,
- what is done,
- what is broken,
- exact next three steps,
- rollback strategy if next step fails.
```

### Agent-to-Agent Handoff

```text
Prepare a structured handoff packet:
- Current phase
- Requirement IDs impacted
- Tests: passing/failing/pending
- Implementation progress by file
- Dependencies and blockers
- Next action with acceptance condition
```

## Quality Check Prompt

```text
Audit the latest checkpoint for missing context:
- Is next step specific and test-linked?
- Are failing tests named exactly?
- Are changed files listed?
- Is decision rationale captured?
- Is there at least one measurable metric or explicit N/A?
If anything is missing, propose a corrected checkpoint.
```
