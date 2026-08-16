# TDD Checkpoint Cadence Playbook

Use this cadence to prevent context drift in long sessions.

## Checkpoint Triggers

Record a checkpoint when any of these happen:

1. Phase transition:
- Red to Green
- Green to Refactor
- Refactor to next Red cycle

2. Test surface change:
- New tests added
- Existing test status changed
- Test failures reveal new requirement ambiguity

3. Implementation milestone:
- Core function implemented
- Interface contract changed
- Cross-file or cross-crate dependency introduced

4. Risk event:
- Performance regression
- Flaky test behavior
- Concurrency or race condition suspicion

## Recommended Frequency

- High intensity coding: every 20 to 40 minutes.
- Multi-component work: every meaningful file boundary crossing.
- Before breaks: always capture one checkpoint.
- Before handoff: capture a final checkpoint with explicit next action.

## Entry Quality Rules

- Prefer exact test names over generic summaries.
- Include file paths for changed implementations.
- Keep next steps actionable and ordered.
- Mark blockers clearly with owner and condition where possible.

## Resume Protocol

When returning to work:

1. Read latest snapshot.
2. Confirm current phase and failing tests.
3. Verify whether dependencies are now resolved.
4. Execute only the first next step.
5. Update journal after completing that step.

## Handoff Protocol

When handing off to another developer or agent:

1. Include current phase.
2. Include top three next steps.
3. Include blocker list.
4. Include open design questions.
5. Include latest metrics if performance-sensitive.
