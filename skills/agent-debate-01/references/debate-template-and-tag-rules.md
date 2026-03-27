# Debate Template and Tag Rules

Source basis: `gumbel-ai/agent-debate`

Use this structure for every debate file.

## Required Sections

```markdown
# Debate: {TOPIC}

**Created:** {DATE}
**Agent 1:** {AGENT_1}
**Agent 2:** {AGENT_2}
**Agent 3:** {AGENT_3}
**Max Rounds:** {MAX_ROUNDS}
**Status:** OPEN

## Context
### Evidence
### Relevant Files
### Constraints

## Proposal
STATUS: OPEN

## Parking Lot

## Dispute Log
```

## Tag Rules

- Use `[A1-R1]`, `[A2-R1]`, `[A3-R2]` style tags.
- `A` means agent number.
- `R` means round number.

## Editing Rules

- Disagree by striking through the specific claim: `~~text~~`
- Write the counterpoint directly below the struck text.
- Add or update a dispute log row whenever a disagreement opens, closes, or gets parked.

## Status Rules

- Proposal status is `OPEN` or `CONVERGED`.
- Dispute status is `OPEN`, `CLOSED`, or `PARKED`.
- Do not converge while any dispute remains `OPEN`.
