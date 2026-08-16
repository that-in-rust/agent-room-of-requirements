# Evidence and Convergence Guardrails

Source basis: `gumbel-ai/agent-debate`

## Evidence Standard

- Every problem statement must include evidence.
- Every proposed fix must cite the code it changes.
- Accepting another agent's claim requires independent verification.
- Inline the evidence in the document; do not rely on "see logs" references.
- If evidence is missing, move the idea to the parking lot.

## Simplicity Rules

- Prefer the minimum viable fix first.
- Reject speculative infrastructure for unobserved problems.
- Reject edge-case engineering without evidence the edge case occurs.
- Keep debate scope tight; related but non-blocking ideas go to the parking lot.

## Behavioral Rules

- Do your own analysis instead of trusting the other agent's claim.
- Disagree plainly when the evidence points elsewhere.
- Concede explicitly when another agent's evidence is stronger.
- Do not write empty agreement language.

## Convergence Rules

- Mark `STATUS: CONVERGED` only after the proposal is stable.
- Any agent may revert the proposal to `STATUS: OPEN`.
- All dispute log entries must be `CLOSED` or `PARKED` before convergence.
