---
name: agent-debate-01
description: Run evidence-based multi-agent technical debates using a shared markdown file that agents edit in place with strikethrough disagreements, dispute logs, and convergence rules. Use when the user asks to compare architecture options, challenge a refactor, stage adversarial code review, or resolve non-trivial implementation tradeoffs across agents such as Codex, Claude, or Gemini.
---

# Agent Debate 01

Use this skill to set up and run structured technical debates where multiple agents inspect the same codebase question and converge on the strongest evidence-backed answer.

## When To Debate

Use debate mode when:
- there are at least two plausible implementation paths
- the decision affects architecture, dependencies, or operational risk
- a normal single-pass review is likely to miss tradeoffs
- the user explicitly wants multiple agents or adversarial review

Do not use debate mode for trivial edits, simple lookups, or fully deterministic tasks.

## Workflow

1. Frame the debate narrowly.
- Convert the user's request into one concrete debate question.
- State the scope, non-negotiable constraints, and relevant files.
- Push unrelated ideas to the parking lot.

2. Initialize the shared markdown file.
- Use `scripts/init_debate_document.py` to scaffold the debate document.
- Prefer 2 agents for speed and 3 agents only when the tradeoff is genuinely unclear.

3. Generate the next-turn prompt.
- Use `scripts/render_debate_turn_prompt.py` so each participant gets the same guardrails and round context.
- In manual mode, run it before each turn for the current agent.

4. Ground every claim in evidence.
- Cite `file:line`, log output, runtime results, or concrete counts inline.
- Do not allow unsupported claims into the proposal; park them instead.

5. Edit a living document, not a chat transcript.
- Disagree by striking through the exact claim and writing the counter directly below it.
- Tag all edits with round markers such as `[A2-R1]`.
- Update the dispute log whenever a substantive disagreement opens, closes, or is parked.

6. Optimize for minimum viable fix.
- Favor the smallest change that solves the observed problem.
- Reject speculative infrastructure, premature abstraction, or monitoring without evidence of need.

7. Converge explicitly.
- Do not mark `STATUS: CONVERGED` while any dispute remains `OPEN`.
- Close only when all disputes are `CLOSED` or `PARKED` and the current proposal is coherent.

## Script Usage

```bash
python3 scripts/init_debate_document.py \
  --path debates/websocket-vs-polling.md \
  --topic "Should this service use WebSockets or polling?" \
  --agent "Codex" \
  --agent "Claude" \
  --max-rounds 3 \
  --context "Real-time updates are required for dashboard clients." \
  --relevant-file "src/server/realtime.ts" \
  --constraint "Do not add a new managed service in v1."
```

```bash
python3 scripts/render_debate_turn_prompt.py \
  --debate-file debates/websocket-vs-polling.md \
  --agent-name "Codex" \
  --round 1
```

## Output Contract

The debate file should always contain:

1. debate header with topic, agents, rounds, and status
2. context, evidence, relevant files, and constraints
3. proposal section with `STATUS: OPEN` or `STATUS: CONVERGED`
4. parking lot for out-of-scope ideas
5. dispute log with `OPEN`, `CLOSED`, or `PARKED`
6. per-turn prompts rendered from the live file so all agents share the same rules

## Guardrails

- No evidence, no proposal entry.
- No empty agreement; every acceptance must say what was verified.
- No scope creep in the main proposal.
- No convergence while unresolved disputes remain.
- Prefer concrete code changes over abstract philosophy.

## Context Strategy

Load progressively:

1. Load this `SKILL.md`.
2. Load [Debate template and tag rules](./references/debate-template-and-tag-rules.md).
3. Load [Evidence and convergence guardrails](./references/evidence-and-convergence-guardrails.md).
4. Load [Repo workflow notes](./references/repo-workflow-notes.md) only if the user wants parity with the upstream `gumbel-ai/agent-debate` workflow.

## References

- [Debate template and tag rules](./references/debate-template-and-tag-rules.md)
- [Evidence and convergence guardrails](./references/evidence-and-convergence-guardrails.md)
- [Repo workflow notes](./references/repo-workflow-notes.md)
