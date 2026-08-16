# Repo Workflow Notes

Source: <https://github.com/gumbel-ai/agent-debate>

Use these notes when the user wants parity with the upstream repo workflow.

## Core Model

- Multiple agents edit one shared markdown file in place.
- The repo supports manual and auto debate modes.
- The shared document is the source of truth.

## Typical Debate Prompts

- "Start a debate on whether to use WebSockets or polling."
- "Continue debate 3 and argue for the simpler approach."
- "Auto debate this auth refactor with Codex and Gemini."

## Upstream CLI Notes

- Debate files are created from a markdown template.
- Guardrails are injected into agent prompts.
- Supported aliases in the repo are centered on Claude, Codex, and Gemini.
- Auto mode is orchestrator-driven; manual mode is terminal-by-terminal participation.

## Practical Limitation

- Final judgment is still human.
- Local provider auth and CLI reliability affect the upstream orchestrator.
- The debate protocol improves rigor, but it does not replace code reading or testing.
