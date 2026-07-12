# Idiomatic Reference Evolution Handoff - July 2026

## Purpose

This document captures the current state of the idiomatic reference evolution work and gives the next developer or agent enough evidence to continue without guessing.

The active workstream is the two-pass evolution of the `idiomatic-ref-202607/` corpus:

1. First pass: evolve all 99 idiomatic reference files section by section.
2. Second pass: create larger combined references under `mega-idiomatic-references-202607/` so users do not need to choose among 99 small files.

The work is intentionally tracked with granular queue rows, per-lane progress journals, per-file question packets, and a master progress journal.

## Latest Saved Checkpoint

- Branch: `main`
- Remote: `origin`
- Latest pushed commit: `2832255b0fcfe96c2fc1708e2a8d693cb5dd0029`
- Commit summary: `Checkpoint idiomatic reference evolution`
- Commit time: `2026-07-12 09:02:07 +0530`
- Working tree at handoff time: clean

## Current Phase

- Phase: `Red`
- Reason: the full corpus suite is still expected to fail until the remaining first-pass files are completed.
- Accepted first-pass references: `47 / 99`
- Remaining first-pass references: `52 / 99`
- Queue rows complete: `5,703 / 11,961`
- Queue rows pending: `6,258 / 11,961`
- Packet files on disk: `48`
- Accepted packet files: `47`
- Partial packet draft: `1`

The partial packet is Alpha assignment 21:

- Reference: `idiomatic-ref-202607/subagent_development_execution_patterns-20260710.md`
- Packet: `idiomatic-reference-evolution-work/alpha/packets/subagent_development_execution_patterns-20260710-question-packets.md`
- Durable progress: Sections `001-009` complete
- Next exact section: Section `010`
- Do not regenerate Sections `001-009`

## Core Artifacts

- Spec: `idiomatic-reference-evolution-spec-202607.md`
- Queue: `idiomatic-reference-evolution-tasks-202607.csv`
- Master journal: `idiomatic-reference-evolution-progress-202607.md`
- Source/evolved corpus: `idiomatic-ref-202607/`
- Tests: `tests/test_idiomatic_reference_evolution.py`
- Focused verifier: `tests/verify_idiomatic_reference_file.py`
- Queue updater: `tools/update_idiomatic_evolution_queue.py`
- Work lanes:
  - `idiomatic-reference-evolution-work/alpha/`
  - `idiomatic-reference-evolution-work/beta/`
  - `idiomatic-reference-evolution-work/gamma/`
  - `idiomatic-reference-evolution-work/delta/`

## Quality Contract

Each completed first-pass reference must satisfy these conditions:

- Preserve the exact original 26 section headings and order.
- Evolve every section to be strictly longer than its seed section.
- Create exactly 26 matching packet sections.
- Create exactly 260 question entries per packet.
- Populate exactly 1,560 mandatory packet fields.
- Keep all 1,560 exact field values unique.
- Keep all 1,560 normalized field values unique after stripping synthetic section/question prefixes.
- Avoid unsupported current-world claims unless explicitly marked as unverified or candidate-only.
- Avoid introducing forbidden placeholder markers.
- Keep tables, fences, ASCII, whitespace, and final newline checks clean.
- Complete a full packet/reference reread in checkpoints of no more than five sections.
- Run focused verification before accepting a file into the queue.

## Verification Status

Last verified before the checkpoint commit:

```bash
git diff --check
```

Result: passed.

```bash
/usr/bin/python3 -m unittest tests.test_idiomatic_reference_evolution.IdiomaticReferenceEvolutionTests.test_packet_content_uniqueness
```

Result: passed.

```bash
/usr/bin/python3 -m unittest tests.test_idiomatic_reference_evolution
```

Result: failed as expected because the workstream is incomplete.

Expected failures at checkpoint:

- `test_question_packets_complete`: 51 future packets are missing.
- `test_reference_files_evolved`: 51 future references are unchanged.
- `test_queue_rows_complete`: 6,258 queue rows remain pending.

These failures do not indicate corruption in the accepted 47 files. They indicate the remaining first-pass corpus work has not been completed.

## Lane State

### Alpha

Owner: `evolve_reference_sections_alpha`

Previous worker id in the original Codex thread:

```text
019f5134-d8c6-74c3-8e1e-7c38eda1ea85
```

Current state:

- Accepted through assignment 20.
- Assignment 21 is partially complete.
- Assignment 21 file: `idiomatic-ref-202607/subagent_development_execution_patterns-20260710.md`
- Completed sections: `001-009`
- Next section: `010`
- Packet fields completed in draft: `540 / 1,560`
- Queue rows are not accepted for assignment 21 yet.

Alpha remaining files:

```text
idiomatic-ref-202607/subagent_development_execution_patterns-20260710.md
idiomatic-ref-202607/tauri_executable_playbook_templates-20260710.md
idiomatic-ref-202607/tauri_executable_reference_maps-20260710.md
idiomatic-ref-202607/tdd_progress_journal_schema-20260710.md
idiomatic-ref-202607/writing_skills_validation_patterns-20260710.md
```

Immediate Alpha continuation:

1. Open the Alpha progress journal and confirm the latest entry.
2. Resume `subagent_development_execution_patterns-20260710.md` at Section `010`.
3. Append packet Section `010`, then evolve reference Section `010`.
4. Continue in small groups, preserving existing Sections `001-009`.
5. Run focused verification only after all 26 sections are complete and reread.

### Beta

Owner: `evolve_reference_sections_beta`

Previous worker id in the original Codex thread:

```text
019f5134-d946-7e52-a8e1-dc0070b4dfb1
```

Current state:

- Accepted through assignment 9.
- Stopped before assignment 10.
- No active partial Beta file.

Beta remaining files:

```text
idiomatic-ref-202607/parallel_agent_dispatch_patterns-20260710.md
idiomatic-ref-202607/planning_execution_workflow_patterns-20260710.md
idiomatic-ref-202607/plugin_mcp_integration_patterns-20260710.md
idiomatic-ref-202607/polyglot_idiomatic_reference_patterns-20260710.md
idiomatic-ref-202607/python_reference_routing_sources-20260710.md
idiomatic-ref-202607/rust_backend_playbook_reference-20260710.md
idiomatic-ref-202607/rust_backend_testing_fixtures-20260710.md
idiomatic-ref-202607/rust_coder_reliability_patterns-20260710.md
idiomatic-ref-202607/rust_executable_template_patterns-20260710.md
idiomatic-ref-202607/rust_quality_gate_patterns-20260710.md
idiomatic-ref-202607/skill_installer_distribution_patterns-20260710.md
idiomatic-ref-202607/systematic_debugging_method_patterns-20260710.md
idiomatic-ref-202607/tdd_resume_handoff_prompts-20260710.md
idiomatic-ref-202607/threejs_react_visualization_patterns-20260710.md
idiomatic-ref-202607/typescript_language_reliability_patterns-20260710.md
idiomatic-ref-202607/visual_explainer_skill_patterns-20260710.md
```

### Gamma

Owner: `evolve_reference_sections_gamma`

Previous worker id in the original Codex thread:

```text
019f5134-d9c9-7c93-993f-fac3da13cd5b
```

Current state:

- Accepted through assignment 9.
- Stopped before assignment 10.
- No active partial Gamma file.

Gamma remaining files:

```text
idiomatic-ref-202607/image_generation_prompt_patterns-20260710.md
idiomatic-ref-202607/kotlin_backend_skill_entrypoint-20260710.md
idiomatic-ref-202607/kotlin_reliability_reference_patterns-20260710.md
idiomatic-ref-202607/local_vision_media_patterns-20260710.md
idiomatic-ref-202607/openai_api_documentation_patterns-20260710.md
idiomatic-ref-202607/plugin_hook_development_patterns-20260710.md
idiomatic-ref-202607/python_quality_antipattern_gates-20260710.md
idiomatic-ref-202607/rust_backend_runtime_operations-20260710.md
idiomatic-ref-202607/rust_executable_reliability_reference-20260710.md
idiomatic-ref-202607/rust_executable_skill_patterns-20260710.md
idiomatic-ref-202607/rust_idiomatic_skill_patterns-20260710.md
idiomatic-ref-202607/tauri_conventions_quality_gates-20260710.md
idiomatic-ref-202607/tauri_legacy_coder_patterns-20260710.md
idiomatic-ref-202607/tdd_context_retainer_skills-20260710.md
idiomatic-ref-202607/tdd_cycle_skill_patterns-20260710.md
idiomatic-ref-202607/typescript_backend_reliability_patterns-20260710.md
```

### Delta

Owner: `evolve_reference_sections_delta`

Previous worker id in the original Codex thread:

```text
019f5134-da52-7370-8b11-b54414a22d15
```

Current state:

- Accepted through assignment 9.
- Stopped before assignment 10.
- No active partial Delta file.

Delta remaining files:

```text
idiomatic-ref-202607/minto_pyramid_writing_patterns-20260710.md
idiomatic-ref-202607/plugin_settings_configuration_patterns-20260710.md
idiomatic-ref-202607/python_language_skill_entrypoint-20260710.md
idiomatic-ref-202607/react_typescript_reliability_patterns-20260710.md
idiomatic-ref-202607/rust_backend_reference_routing-20260710.md
idiomatic-ref-202607/rust_backend_skill_entrypoint-20260710.md
idiomatic-ref-202607/rust_conventions_quality_gates-20260710.md
idiomatic-ref-202607/rust_executable_reference_maps-20260710.md
idiomatic-ref-202607/skill_creator_evaluation_patterns-20260710.md
idiomatic-ref-202607/skill_development_reference_patterns-20260710.md
idiomatic-ref-202607/system_design_architecture_patterns-20260710.md
idiomatic-ref-202607/tauri_doctrine_source_review-20260710.md
idiomatic-ref-202607/tauri_executable_skill_patterns-20260710.md
idiomatic-ref-202607/tdd_checkpoint_cadence_playbook-20260710.md
idiomatic-ref-202607/timeline_decision_simulation_patterns-20260710.md
```

## How To Resume

Start from evidence, not memory.

```bash
git pull origin main
/usr/bin/python3 /Users/amuldotexe/.codex/skills/tdd-task-progress-context-retainer/scripts/progress_journal_orchestrator.py snapshot --path idiomatic-reference-evolution-progress-202607.md
```

Check current queue status:

```bash
/usr/bin/python3 - <<'PY'
import csv
from collections import Counter, defaultdict

rows = list(csv.DictReader(open("idiomatic-reference-evolution-tasks-202607.csv", newline="")))
status = Counter(row["task_status"] for row in rows)
per_file = defaultdict(Counter)

for row in rows:
    per_file[row["reference_file_path"]][row["task_status"]] += 1

accepted = [
    path for path, counts in per_file.items()
    if counts.get("complete", 0) == sum(counts.values())
]

print("rows_total", len(rows))
print("complete_rows", status.get("complete", 0))
print("pending_rows", status.get("pending", 0))
print("files_total", len(per_file))
print("accepted_files", len(accepted))
print("pending_files", len(per_file) - len(accepted))
PY
```

Then continue in this order:

1. Resume Alpha assignment 21 from Section `010`.
2. After Alpha assignment 21 is fully complete, run the focused verifier.
3. Use the queue updater to accept Alpha assignment 21.
4. Update the master journal.
5. Continue Alpha assignments 22-25.
6. Continue Beta, Gamma, and Delta from assignment 10 onward with the same owner mapping.
7. After all 99 first-pass files are accepted, start pass two under `mega-idiomatic-references-202607/`.

## Per-File Completion Procedure

For each reference file:

1. Read the seed reference and the relevant local source artifacts listed in the queue rows.
2. Preserve the 26 original headings exactly.
3. For each section, pose the ten required questions.
4. Write the packet section first.
5. Evolve the matching reference section second.
6. Save frequently, ideally every section or every three sections.
7. Run local sanity checks after each small group.
8. After Section `026`, reread every packet/reference pair in groups of no more than five sections.
9. Run focused verification.
10. Only then update the shared queue.

Focused verifier:

```bash
/usr/bin/python3 tests/verify_idiomatic_reference_file.py --path idiomatic-ref-202607/<file-name>.md
```

Queue updater:

```bash
/usr/bin/python3 tools/update_idiomatic_evolution_queue.py --path idiomatic-ref-202607/<file-name>.md
```

Packet uniqueness test:

```bash
/usr/bin/python3 -m unittest tests.test_idiomatic_reference_evolution.IdiomaticReferenceEvolutionTests.test_packet_content_uniqueness
```

Full suite:

```bash
/usr/bin/python3 -m unittest tests.test_idiomatic_reference_evolution
```

The full suite should remain red until all 99 files are accepted.

## Journal Update Procedure

After accepting any completed file, update the master journal:

```bash
/usr/bin/python3 /Users/amuldotexe/.codex/skills/tdd-task-progress-context-retainer/scripts/progress_journal_orchestrator.py update \
  --path idiomatic-reference-evolution-progress-202607.md \
  --phase Red \
  --focus "Accept <file-name> and continue first-pass corpus evolution" \
  --test "<focused-verifier>|passing|26 sections, 260 questions, 1560 fields, normalized uniqueness 1560" \
  --test "test_queue_rows_complete|failing|<complete_rows> of 11961 rows complete; remaining failures are unfinished corpus work" \
  --implementation "Accepted <file-name> into shared queue" \
  --next-step "Continue the next assigned file for the same lane" \
  --note "Full suite remains red only because the corpus is incomplete" \
  --metric "accepted_files=<n>; completed_rows=<n>; pending_rows=<n>; active_lanes=4"
```

Also append detailed lane evidence to the relevant lane journal:

```text
idiomatic-reference-evolution-work/<lane>/progress.md
```

## Important Constraints

- Keep the same file with the same lane owner.
- Do not let two workers edit the same reference, packet, lane journal, or shared queue simultaneously.
- The coordinator should be the only process that edits `idiomatic-reference-evolution-tasks-202607.csv`.
- Do not mark a file complete in the queue until focused verification passes.
- Do not treat packet existence as acceptance. Acceptance requires queue update.
- Do not browse the web unless the specific file requires current external facts and the claim will be labeled with evidence status.
- Do not promote candidate external sources into facts without direct verification.
- Do not rewrite accepted files unless a verifier exposes a real issue.
- Do not use `path` as a `zsh` loop variable. In `zsh`, `path` is tied to `PATH` and can break command lookup. Use `ref` or `file_path` instead.

## Pass Two Plan

Pass two has not started.

Start it only after the first pass reaches:

- `99 / 99` accepted references
- `11,961 / 11,961` complete queue rows
- Full evolution suite passing

Expected output folder:

```text
mega-idiomatic-references-202607/
```

The mega references should combine related themes so a user can choose a small number of larger reference documents instead of choosing among 99 individual references.

Likely grouping dimensions:

- Agent design and orchestration
- TDD, executable specs, and progress tracking
- Language-specific backend reliability
- Rust and Tauri delivery
- Kotlin backend delivery
- TypeScript, React, and frontend reliability
- Plugin, skill, and MCP development
- Documentation, explanation, and visual communication
- Debugging, review, and verification
- Planning, decision-making, and system design

## Rollback Strategy

If the next continuation attempt damages a file:

1. Stop editing immediately.
2. Identify whether the damage is in a reference, packet, lane journal, or shared queue.
3. Use `git diff <path>` to inspect only that file.
4. If the damaged file was accepted before commit `2832255`, restore from git only with explicit user approval.
5. If the damaged file is the active partial Alpha assignment, preserve Sections `001-009` unless they are the proven source of the issue.
6. Re-run the focused verifier for the affected reference before continuing.

## Best Next Prompt

Use this prompt to continue:

```text
Continue the idiomatic reference evolution work from IDIOMATIC_REFERENCE_EVOLUTION_HANDOFF_202607.md.

Use tdd-task-progress-context-retainer.
Start by reading the latest master journal snapshot and the Alpha lane progress journal.
Resume Alpha assignment 21 at Section 010 of idiomatic-ref-202607/subagent_development_execution_patterns-20260710.md.
Do not regenerate Sections 001-009.
Keep packet and reference writes frequent.
After completing all 26 sections and bounded rereads, run focused verification, update the queue with tools/update_idiomatic_evolution_queue.py, update the master journal, and report exact counts.
Do not start pass two until all 99 first-pass references are accepted.
```
