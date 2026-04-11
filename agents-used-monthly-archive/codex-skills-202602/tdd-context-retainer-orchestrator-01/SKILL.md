---
name: tdd-context-retainer-orchestrator-01
description: Retain and orchestrate context for long-running TDD work by tracking red, green, and refactor state, test status, implementation progress, and resumable next steps in a structured progress journal. Use when sessions span interruptions, multiple files or crates, or frequent context switches and Codex must produce reliable handoffs and resume points.
---

# Tdd Context Retainer Orchestrator 01

Use this skill to preserve continuity in long TDD efforts and provide deterministic resume context across interruptions.

## Workflow

1. Initialize a journal once per workstream.
- Run `scripts/progress_journal_orchestrator.py init`.
- Store one journal per feature or ticket.

2. Capture checkpoint updates continuously.
- Run `scripts/progress_journal_orchestrator.py update` after each meaningful change:
- Test batch created or changed.
- Phase transition (`Red`, `Green`, `Refactor`).
- Multi-file or multi-crate edits.
- Performance or error regression discovery.

3. Resume work from the last saved state.
- Run `scripts/progress_journal_orchestrator.py snapshot`.
- Use the latest checkpoint to restore current phase, failing tests, implementation status, and next action.

4. Emit handoff summaries.
- Produce a short human-readable status with:
- current phase
- top three next steps
- blockers
- unresolved design decisions

## Journal Contract

Capture these sections in every checkpoint:

- `Current Phase`
- `Tests Written`
- `Implementation Progress`
- `Current Focus`
- `Next Steps`
- `Context Notes`
- `Performance/Metrics`

Use explicit identifiers when available:
- test names
- file paths
- function signatures
- error messages

## Script Usage

```bash
python3 scripts/progress_journal_orchestrator.py init \
  --path journals/feature-a.md \
  --task "Feature A end-to-end TDD"

python3 scripts/progress_journal_orchestrator.py update \
  --path journals/feature-a.md \
  --phase Red \
  --focus "Write failing tests for endpoint validation" \
  --test "test_endpoint_rejects_empty_payload|failing|expects 400 on empty payload" \
  --implementation "api/handlers.rs: added request parser scaffold" \
  --next-step "Implement minimum handler logic to satisfy validation tests" \
  --note "Need shared fixture helper for request setup"

python3 scripts/progress_journal_orchestrator.py snapshot \
  --path journals/feature-a.md
```

## Guardrails

- Never leave `Next Steps` empty.
- Track `why` for major decisions, not only `what`.
- Record cross-component dependencies explicitly.
- Keep updates small and frequent to reduce context drift.
- Prefer append-only checkpoints over rewriting history.

## Context Strategy

Load progressively:

1. Load this `SKILL.md`.
2. Load [Journal schema and examples](./references/progress-journal-schema.md).
3. Load [Checkpoint cadence playbook](./references/tdd-checkpoint-cadence-playbook.md) for long-running sessions.
4. Load [Resume and handoff prompts](./references/resume-handoff-prompts.md) when resuming or transferring work.

## References

- [Journal schema and examples](./references/progress-journal-schema.md)
- [Checkpoint cadence playbook](./references/tdd-checkpoint-cadence-playbook.md)
- [Resume and handoff prompts](./references/resume-handoff-prompts.md)
