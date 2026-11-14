# Rust-skills

Every file in this repository that says a meaningful amount about Rust, gathered in one
place: 188 files. Each is a byte-identical copy of an original; the originals are
unchanged and remain the source.

How the set was built:

1. Every file on all three branches (`main`, `devin/1783832548-idiomatic-evolution-alpha-a21`,
   `codex/kotlin-backend-delivery-skill`) was searched by content, whatever its name. A file
   counts if it contains `rust` in any letter case at the start of a word (`Rust`, `rustc`,
   `rust-lang`; not `trust`). 271 distinct files matched.
2. Files with identical content are kept once.
3. Files that mention Rust only once or twice were dropped (52 files).
4. Where several versions of one document existed (same file name and at least 80% of lines in
   common), only the newest is kept (34 documents, 34 older versions dropped). In every
   case the newest version already held everything in the older ones: the older versions
   differed only in lines that the newest rewords, almost all of them renamed folder paths.
   Files that share a generic name (`SKILL.md`, `progress.md`, `assignments.csv`) but are
   different documents are all kept.

Four Tauri and scan-summary files that do not contain the word are kept because they belong
to a Rust or Tauri skill.

| Folder | Files | What it holds |
|---|---|---|
| `idiomatic-references/` | 76 | Rust and Tauri idiomatic references: current (202607), seed, and the 202604 and 202606 archives |
| `skills/` | 29 | Archived Codex and Claude skills for Rust and Tauri, by month |
| `methodology/` | 2 | Rust and Tauri executable-specification method |
| `research/` | 4 | Strategy notes about Rust |
| `mentions-rust/main/` | 68 | Other files on `main` that mention Rust three or more times, under their original paths |
| `mentions-rust/branch-idiomatic-evolution-alpha-a21/` | 9 | Files that exist only on that branch |

Things to know:

- Because identical files are kept once, some month folders under `skills/` are incomplete.
- Links inside the copied files still point to their original relative locations and may not resolve from here.

## Every file and where it came from

"Mentions" is the number of times `rust` appears. "Older versions dropped" is the number of earlier versions of the same document that this file replaces.

| File | Mentions | Original path | Branch | Older versions dropped |
|---|---|---|---|---|
| `idiomatic-references/archive-202604/rust-executable-specs-01/rust-executable-specs-reference.md` | 13 | `archive/monthly-agent-snapshots/idiomatic-references-202604/rust-executable-specs-01/rust-executable-specs-reference.md` | main | 0 |
| `idiomatic-references/archive-202604/tauri-executable-specs-01/tauri-executable-specs-reference.md` | 13 | `archive/monthly-agent-snapshots/idiomatic-references-202604/tauri-executable-specs-01/tauri-executable-specs-reference.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_backend_playbook_reference.md` | 45 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_playbook_reference.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_backend_reference_routing.md` | 38 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_reference_routing.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_backend_runtime_operations.md` | 45 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_runtime_operations.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_backend_security_resilience.md` | 45 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_security_resilience.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_backend_skill_entrypoint.md` | 50 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_skill_entrypoint.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_backend_testing_fixtures.md` | 45 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_testing_fixtures.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_coder_reliability_patterns.md` | 63 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_coder_reliability_patterns.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_conventions_quality_gates.md` | 46 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_conventions_quality_gates.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_executable_reference_maps.md` | 57 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_executable_reference_maps.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_executable_reliability_reference.md` | 51 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_executable_reliability_reference.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_executable_skill_patterns.md` | 58 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_executable_skill_patterns.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_executable_template_patterns.md` | 75 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_executable_template_patterns.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_idiomatic_skill_patterns.md` | 51 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_idiomatic_skill_patterns.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_idioms_checklist_patterns.md` | 58 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_idioms_checklist_patterns.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_legacy_coder_prompts.md` | 59 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_legacy_coder_prompts.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/rust_quality_gate_patterns.md` | 56 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_quality_gate_patterns.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/tauri_conventions_quality_gates.md` | 9 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_conventions_quality_gates.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/tauri_doctrine_source_review.md` | 9 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_doctrine_source_review.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/tauri_executable_playbook_templates.md` | 9 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_executable_playbook_templates.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/tauri_executable_reference_maps.md` | 13 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_executable_reference_maps.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/tauri_executable_skill_patterns.md` | 9 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_executable_skill_patterns.md` | main | 0 |
| `idiomatic-references/archive-202606/generated-references/tauri_legacy_coder_patterns.md` | 9 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_legacy_coder_patterns.md` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part1-repos.txt` | 128 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-1-repos.txt` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part1.md` | 1427 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-Part1.md` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part2-repos.txt` | 128 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-2-repos.txt` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part2.md` | 1451 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-Part2.md` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part3-repos.txt` | 126 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-3-repos.txt` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part3.md` | 1370 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-Part3.md` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part4-repos.txt` | 126 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-4-repos.txt` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part4.md` | 1396 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-Part4.md` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part5-repos.txt` | 125 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-5-repos.txt` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part5.md` | 1392 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-Part5.md` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-coverage-ledger.json` | 2455 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-coverage-ledger.json` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-evidence-index.json` | 3155 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-evidence-index.json` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-progress.md` | 34 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-progress.md` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-repo-inventory.json` | 2201 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-repo-inventory.json` | main | 0 |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-scan-summary.json` | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-scan-summary.json` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-1-repos.txt` | 3 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-1-repos.txt` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-1.md` | 218 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-1.md` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-2-repos.txt` | 3 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-2-repos.txt` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-2.md` | 205 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-2.md` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-3-repos.txt` | 5 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-3-repos.txt` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-3.md` | 188 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-3.md` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-4.md` | 173 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-4.md` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-5.md` | 245 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-5.md` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-codegraphcontext-evidence.json` | 9 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-codegraphcontext-evidence.json` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-progress.md` | 55 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-progress.md` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-repo-inventory.json` | 19 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-repo-inventory.json` | main | 0 |
| `idiomatic-references/archive-202606/rust-patterns-scan-summary.json` | 773 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-scan-summary.json` | main | 0 |
| `idiomatic-references/archive-202606/tools/verify_meta_rust_ref.py` | 12 | `archive/monthly-agent-snapshots/idiomatic-references-202606/tools/verify_meta_rust_ref.py` | main | 0 |
| `idiomatic-references/archive-202606/tools/verify_rust_patterns_reference.py` | 7 | `archive/monthly-agent-snapshots/idiomatic-references-202606/tools/verify_rust_patterns_reference.py` | main | 0 |
| `idiomatic-references/current-202607/rust/rust_backend_playbook_reference-20260710.md` | 84 | `library/idiomatic/202607/rust_backend_playbook_reference-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_backend_reference_routing-20260710.md` | 57 | `library/idiomatic/202607/rust_backend_reference_routing-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_backend_runtime_operations-20260710.md` | 60 | `library/idiomatic/202607/rust_backend_runtime_operations-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_backend_security_resilience-20260710.md` | 62 | `library/idiomatic/202607/rust_backend_security_resilience-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_backend_skill_entrypoint-20260710.md` | 67 | `library/idiomatic/202607/rust_backend_skill_entrypoint-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_backend_testing_fixtures-20260710.md` | 54 | `library/idiomatic/202607/rust_backend_testing_fixtures-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_coder_reliability_patterns-20260710.md` | 109 | `library/idiomatic/202607/rust_coder_reliability_patterns-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_conventions_quality_gates-20260710.md` | 69 | `library/idiomatic/202607/rust_conventions_quality_gates-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_executable_reference_maps-20260710.md` | 64 | `library/idiomatic/202607/rust_executable_reference_maps-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_executable_reliability_reference-20260710.md` | 68 | `library/idiomatic/202607/rust_executable_reliability_reference-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_executable_skill_patterns-20260710.md` | 78 | `library/idiomatic/202607/rust_executable_skill_patterns-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_executable_template_patterns-20260710.md` | 86 | `library/idiomatic/202607/rust_executable_template_patterns-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_idiomatic_skill_patterns-20260710.md` | 70 | `library/idiomatic/202607/rust_idiomatic_skill_patterns-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_idioms_checklist_patterns-20260710.md` | 122 | `library/idiomatic/202607/rust_idioms_checklist_patterns-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_legacy_coder_prompts-20260710.md` | 154 | `library/idiomatic/202607/rust_legacy_coder_prompts-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/rust/rust_quality_gate_patterns-20260710.md` | 57 | `library/idiomatic/202607/rust_quality_gate_patterns-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/tauri/tauri_conventions_quality_gates-20260710.md` | 23 | `library/idiomatic/202607/tauri_conventions_quality_gates-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/tauri/tauri_doctrine_source_review-20260710.md` | 24 | `library/idiomatic/202607/tauri_doctrine_source_review-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/tauri/tauri_executable_playbook_templates-20260710.md` | 34 | `library/idiomatic/202607/tauri_executable_playbook_templates-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/tauri/tauri_executable_reference_maps-20260710.md` | 18 | `library/idiomatic/202607/tauri_executable_reference_maps-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/tauri/tauri_executable_skill_patterns-20260710.md` | 23 | `library/idiomatic/202607/tauri_executable_skill_patterns-20260710.md` | main | 1 |
| `idiomatic-references/current-202607/tauri/tauri_legacy_coder_patterns-20260710.md` | 18 | `library/idiomatic/202607/tauri_legacy_coder_patterns-20260710.md` | main | 1 |
| `idiomatic-references/seed/Rust-Coder-1000IQ-01.md` | 294 | `library/idiomatic/seed/Rust-Coder-1000IQ-01.md` | main | 0 |
| `mentions-rust/branch-idiomatic-evolution-alpha-a21/IDIOMATIC_REFERENCE_EVOLUTION_HANDOFF_202607.md` | 14 | `IDIOMATIC_REFERENCE_EVOLUTION_HANDOFF_202607.md` | devin/1783832548-idiomatic-evolution-alpha-a21 | 0 |
| `mentions-rust/branch-idiomatic-evolution-alpha-a21/idiomatic-reference-evolution-progress-202607.md` | 26 | `idiomatic-reference-evolution-progress-202607.md` | devin/1783832548-idiomatic-evolution-alpha-a21 | 0 |
| `mentions-rust/branch-idiomatic-evolution-alpha-a21/idiomatic-reference-evolution-tasks-202607.csv` | 4475 | `idiomatic-reference-evolution-tasks-202607.csv` | devin/1783832548-idiomatic-evolution-alpha-a21 | 0 |
| `mentions-rust/branch-idiomatic-evolution-alpha-a21/idiomatic-reference-evolution-work/alpha/assignments.csv` | 3 | `idiomatic-reference-evolution-work/alpha/assignments.csv` | devin/1783832548-idiomatic-evolution-alpha-a21 | 0 |
| `mentions-rust/branch-idiomatic-evolution-alpha-a21/idiomatic-reference-evolution-work/beta/assignments.csv` | 5 | `idiomatic-reference-evolution-work/beta/assignments.csv` | devin/1783832548-idiomatic-evolution-alpha-a21 | 0 |
| `mentions-rust/branch-idiomatic-evolution-alpha-a21/idiomatic-reference-evolution-work/delta/assignments.csv` | 4 | `idiomatic-reference-evolution-work/delta/assignments.csv` | devin/1783832548-idiomatic-evolution-alpha-a21 | 0 |
| `mentions-rust/branch-idiomatic-evolution-alpha-a21/idiomatic-reference-evolution-work/gamma/assignments.csv` | 4 | `idiomatic-reference-evolution-work/gamma/assignments.csv` | devin/1783832548-idiomatic-evolution-alpha-a21 | 0 |
| `mentions-rust/branch-idiomatic-evolution-alpha-a21/unclassified-yet/DOCUMENT_INDEX.md` | 79 | `unclassified-yet/DOCUMENT_INDEX.md` | devin/1783832548-idiomatic-evolution-alpha-a21 | 1 |
| `mentions-rust/branch-idiomatic-evolution-alpha-a21/unclassified-yet/Prompts202606.md` | 5 | `unclassified-yet/Prompts202606.md` | devin/1783832548-idiomatic-evolution-alpha-a21 | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/claude-skills-202602/commit-push-dev-flow.md` | 7 | `archive/monthly-agent-snapshots/claude-skills-202602/commit-push-dev-flow.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/claude-skills-202602/minto-pyramid-01.md` | 3 | `archive/monthly-agent-snapshots/claude-skills-202602/minto-pyramid-01.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/claude-skills-202602/notes01-agent.md` | 26 | `archive/monthly-agent-snapshots/claude-skills-202602/notes01-agent.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/claude-skills-202602/react-threejs-coder-01.md` | 3 | `archive/monthly-agent-snapshots/claude-skills-202602/react-threejs-coder-01.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/claude-skills-202603/plugins/claude-code-setup/references/hooks-patterns.md` | 8 | `archive/monthly-agent-snapshots/claude-skills-202603/plugins/claude-code-setup/references/hooks-patterns.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/codex-skills-202603/run-parseltongue-1-7-2/central-logs/parseltongue-query-log.txt` | 42 | `archive/monthly-agent-snapshots/codex-skills-202603/run-parseltongue-1-7-2/central-logs/parseltongue-query-log.txt` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202602/broad-idiomatic-patterns.md` | 28 | `archive/monthly-agent-snapshots/idiomatic-references-202602/broad-idiomatic-patterns.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/critique-JD-01.md` | 173 | `archive/monthly-agent-snapshots/idiomatic-references-202606/critique-JD-01.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/critique-SD-01.md` | 185 | `archive/monthly-agent-snapshots/idiomatic-references-202606/critique-SD-01.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-1.md` | 190 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-1.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-2.md` | 294 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-2.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-3.md` | 271 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-3.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-4.md` | 224 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-4.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-5.md` | 242 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-5.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-codegraphcontext-evidence.md` | 11 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-codegraphcontext-evidence.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-codegraphcontext-smoke.json` | 18 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-codegraphcontext-smoke.json` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-coverage-ledger.json` | 1266 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-coverage-ledger.json` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-coverage-ledger.md` | 102 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-coverage-ledger.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-evidence-index.json` | 2573 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-evidence-index.json` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-progress.md` | 6 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-progress.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-repo-inventory.json` | 1291 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-repo-inventory.json` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/prd-idiomatic-202606.md` | 61 | `archive/monthly-agent-snapshots/idiomatic-references-202606/prd-idiomatic-202606.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/reference-generation-coverage.md` | 32 | `archive/monthly-agent-snapshots/idiomatic-references-202606/reference-generation-coverage.md` | main | 0 |
| `mentions-rust/main/archive/monthly-agent-snapshots/idiomatic-references-202606/tools/generate_reference_files.py` | 18 | `archive/monthly-agent-snapshots/idiomatic-references-202606/tools/generate_reference_files.py` | main | 0 |
| `mentions-rust/main/library/idiomatic/202607/executable_specification_skill_patterns-20260710.md` | 3 | `library/idiomatic/202607/executable_specification_skill_patterns-20260710.md` | main | 1 |
| `mentions-rust/main/library/idiomatic/202607/executable_traceability_template_patterns-20260710.md` | 12 | `library/idiomatic/202607/executable_traceability_template_patterns-20260710.md` | main | 1 |
| `mentions-rust/main/library/idiomatic/202607/polyglot_idiomatic_reference_patterns-20260710.md` | 7 | `library/idiomatic/202607/polyglot_idiomatic_reference_patterns-20260710.md` | main | 1 |
| `mentions-rust/main/library/idiomatic/202607/python_language_skill_entrypoint-20260710.md` | 3 | `library/idiomatic/202607/python_language_skill_entrypoint-20260710.md` | main | 1 |
| `mentions-rust/main/library/idiomatic/202607/skill_creator_evaluation_patterns-20260710.md` | 6 | `library/idiomatic/202607/skill_creator_evaluation_patterns-20260710.md` | main | 1 |
| `mentions-rust/main/methodology/prompts/202606-prompt-library.md` | 5 | `methodology/prompts/202606-prompt-library.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/handoff.md` | 14 | `projects/idiomatic-reference-evolution/202607/handoff.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/progress.md` | 26 | `projects/idiomatic-reference-evolution/202607/progress.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/assignments.csv` | 3 | `projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/assignments.csv` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/packets/rust_backend_security_resilience-20260710-question-packets.md` | 104 | `projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/packets/rust_backend_security_resilience-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/packets/rust_idioms_checklist_patterns-20260710-question-packets.md` | 299 | `projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/packets/rust_idioms_checklist_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/packets/rust_legacy_coder_prompts-20260710-question-packets.md` | 249 | `projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/packets/rust_legacy_coder_prompts-20260710-question-packets.md` | main | 1 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/packets/tauri_executable_playbook_templates-20260710-question-packets.md` | 74 | `projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/packets/tauri_executable_playbook_templates-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/packets/tauri_executable_reference_maps-20260710-question-packets.md` | 7 | `projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/packets/tauri_executable_reference_maps-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/progress.md` | 30 | `projects/idiomatic-reference-evolution/202607/section-review-packets/alpha/progress.md` | main | 1 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/beta/assignments.csv` | 5 | `projects/idiomatic-reference-evolution/202607/section-review-packets/beta/assignments.csv` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/polyglot_idiomatic_reference_patterns-20260710-question-packets.md` | 23 | `projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/polyglot_idiomatic_reference_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/rust_backend_playbook_reference-20260710-question-packets.md` | 242 | `projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/rust_backend_playbook_reference-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/rust_backend_testing_fixtures-20260710-question-packets.md` | 93 | `projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/rust_backend_testing_fixtures-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/rust_coder_reliability_patterns-20260710-question-packets.md` | 289 | `projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/rust_coder_reliability_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/rust_executable_template_patterns-20260710-question-packets.md` | 125 | `projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/rust_executable_template_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/rust_quality_gate_patterns-20260710-question-packets.md` | 62 | `projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/rust_quality_gate_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/threejs_react_visualization_patterns-20260710-question-packets.md` | 4 | `projects/idiomatic-reference-evolution/202607/section-review-packets/beta/packets/threejs_react_visualization_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/beta/progress.md` | 10 | `projects/idiomatic-reference-evolution/202607/section-review-packets/beta/progress.md` | main | 1 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/delta/assignments.csv` | 4 | `projects/idiomatic-reference-evolution/202607/section-review-packets/delta/assignments.csv` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/python_language_skill_entrypoint-20260710-question-packets.md` | 11 | `projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/python_language_skill_entrypoint-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/rust_backend_reference_routing-20260710-question-packets.md` | 151 | `projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/rust_backend_reference_routing-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/rust_backend_skill_entrypoint-20260710-question-packets.md` | 114 | `projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/rust_backend_skill_entrypoint-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/rust_conventions_quality_gates-20260710-question-packets.md` | 152 | `projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/rust_conventions_quality_gates-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/rust_executable_reference_maps-20260710-question-packets.md` | 90 | `projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/rust_executable_reference_maps-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/skill_creator_evaluation_patterns-20260710-question-packets.md` | 18 | `projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/skill_creator_evaluation_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/tauri_doctrine_source_review-20260710-question-packets.md` | 49 | `projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/tauri_doctrine_source_review-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/tauri_executable_skill_patterns-20260710-question-packets.md` | 31 | `projects/idiomatic-reference-evolution/202607/section-review-packets/delta/packets/tauri_executable_skill_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/delta/progress.md` | 9 | `projects/idiomatic-reference-evolution/202607/section-review-packets/delta/progress.md` | main | 1 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/assignments.csv` | 4 | `projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/assignments.csv` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/rust_backend_runtime_operations-20260710-question-packets.md` | 114 | `projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/rust_backend_runtime_operations-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/rust_executable_reliability_reference-20260710-question-packets.md` | 124 | `projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/rust_executable_reliability_reference-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/rust_executable_skill_patterns-20260710-question-packets.md` | 180 | `projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/rust_executable_skill_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/rust_idiomatic_skill_patterns-20260710-question-packets.md` | 154 | `projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/rust_idiomatic_skill_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/tauri_conventions_quality_gates-20260710-question-packets.md` | 46 | `projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/tauri_conventions_quality_gates-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/tauri_legacy_coder_patterns-20260710-question-packets.md` | 25 | `projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/packets/tauri_legacy_coder_patterns-20260710-question-packets.md` | main | 0 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/progress.md` | 8 | `projects/idiomatic-reference-evolution/202607/section-review-packets/gamma/progress.md` | main | 1 |
| `mentions-rust/main/projects/idiomatic-reference-evolution/202607/task-queue.csv` | 4475 | `projects/idiomatic-reference-evolution/202607/task-queue.csv` | main | 0 |
| `mentions-rust/main/unclassified-yet/DOCUMENT_INDEX.md` | 233 | `unclassified-yet/DOCUMENT_INDEX.md` | main | 0 |
| `methodology/executable-specifications/rust/core.md` | 21 | `methodology/executable-specifications/rust/core.md` | main | 0 |
| `methodology/executable-specifications/tauri/core.md` | 12 | `methodology/executable-specifications/tauri/core.md` | main | 0 |
| `research/20-more-rust-hackathon-ideas-after-the-first-shortlist.md` | 29 | `research/strategic/20-more-rust-hackathon-ideas-after-the-first-shortlist.md` | main | 0 |
| `research/how-to-rank-rust-opportunities-when-codex-is-helping.md` | 50 | `research/strategic/how-to-rank-rust-opportunities-when-codex-is-helping.md` | main | 0 |
| `research/how-to-win-a-rust-hackathon-in-6-hours.md` | 59 | `research/strategic/how-to-win-a-rust-hackathon-in-6-hours.md` | main | 0 |
| `research/why-rust-backends-need-a-separate-playbook.md` | 24 | `research/strategic/why-rust-backends-need-a-separate-playbook.md` | main | 0 |
| `skills/claude/202602/Tauri-coder-01.md` | 33 | `archive/monthly-agent-snapshots/claude-skills-202602/Tauri-coder-01.md` | main | 0 |
| `skills/claude/202602/rust-coder-01.md` | 169 | `archive/monthly-agent-snapshots/claude-skills-202602/rust-coder-01.md` | main | 0 |
| `skills/claude/202602/rust-coder-02.md` | 41 | `archive/monthly-agent-snapshots/claude-skills-202602/rust-coder-02.md` | main | 0 |
| `skills/claude/202604/personal/rust-web-backend-skill-explainer/SKILL.md` | 17 | `archive/monthly-agent-snapshots/claude-skills-202604/personal/rust-web-backend-skill-explainer/SKILL.md` | main | 0 |
| `skills/claude/202604/rust-executable-specs-01.md` | 21 | `archive/monthly-agent-snapshots/claude-skills-202604/rust-executable-specs-01.md` | main | 0 |
| `skills/claude/202604/tauri-executable-specs-01.md` | 12 | `archive/monthly-agent-snapshots/claude-skills-202604/tauri-executable-specs-01.md` | main | 0 |
| `skills/codex/202602/idiomatic-rust-coder-01/agents/openai.yaml` | 4 | `archive/monthly-agent-snapshots/codex-skills-202602/idiomatic-rust-coder-01/agents/openai.yaml` | main | 0 |
| `skills/codex/202602/idiomatic-rust-coder-01/references/rust-executable-specs-templates.md` | 20 | `archive/monthly-agent-snapshots/codex-skills-202602/idiomatic-rust-coder-01/references/rust-executable-specs-templates.md` | main | 0 |
| `skills/codex/202602/idiomatic-rust-coder-01/references/rust-idioms-checklist.md` | 4 | `archive/monthly-agent-snapshots/codex-skills-202602/idiomatic-rust-coder-01/references/rust-idioms-checklist.md` | main | 0 |
| `skills/codex/202602/idiomatic-rust-coder-01/references/rust-quality-gates-anti-patterns.md` | 4 | `archive/monthly-agent-snapshots/codex-skills-202602/idiomatic-rust-coder-01/references/rust-quality-gates-anti-patterns.md` | main | 0 |
| `skills/codex/202603/idiomatic-rust-coder-01/SKILL.md` | 20 | `archive/monthly-agent-snapshots/codex-skills-202603/idiomatic-rust-coder-01/SKILL.md` | main | 1 |
| `skills/codex/202603/rust-coder-02/SKILL.md` | 14 | `archive/monthly-agent-snapshots/codex-skills-202603/rust-coder-02/SKILL.md` | main | 0 |
| `skills/codex/202603/rust-coder-02/agents/openai.yaml` | 4 | `archive/monthly-agent-snapshots/codex-skills-202603/rust-coder-02/agents/openai.yaml` | main | 0 |
| `skills/codex/202603/rust-coder-02/references/reference-map.md` | 3 | `archive/monthly-agent-snapshots/codex-skills-202603/rust-coder-02/references/reference-map.md` | main | 0 |
| `skills/codex/202603/tauri-coder-01/agents/openai.yaml` | 0 | `archive/monthly-agent-snapshots/codex-skills-202603/tauri-coder-01/agents/openai.yaml` | main | 0 |
| `skills/codex/202603/tauri-coder-01/references/reference-map.md` | 0 | `archive/monthly-agent-snapshots/codex-skills-202603/tauri-coder-01/references/reference-map.md` | main | 0 |
| `skills/codex/202604/rust-executable-specs-01/SKILL.md` | 28 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-executable-specs-01/SKILL.md` | main | 0 |
| `skills/codex/202604/rust-executable-specs-01/agents/openai.yaml` | 5 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-executable-specs-01/agents/openai.yaml` | main | 0 |
| `skills/codex/202604/rust-executable-specs-01/references/reference-map.md` | 33 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-executable-specs-01/references/reference-map.md` | main | 0 |
| `skills/codex/202604/rust-executable-specs-01/references/rust-conventions-and-gates.md` | 7 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-executable-specs-01/references/rust-conventions-and-gates.md` | main | 0 |
| `skills/codex/202604/rust-executable-specs-01/references/rust-executable-specs-playbook.md` | 37 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-executable-specs-01/references/rust-executable-specs-playbook.md` | main | 0 |
| `skills/codex/202604/rust-web-backend-delivery-01/SKILL.md` | 30 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-web-backend-delivery-01/SKILL.md` | main | 0 |
| `skills/codex/202604/rust-web-backend-delivery-01/agents/openai.yaml` | 4 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-web-backend-delivery-01/agents/openai.yaml` | main | 0 |
| `skills/codex/202604/rust-web-backend-delivery-01/references/reference-map.md` | 38 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-web-backend-delivery-01/references/reference-map.md` | main | 0 |
| `skills/codex/202604/tauri-executable-specs-01/SKILL.md` | 6 | `archive/monthly-agent-snapshots/codex-skills-202604/tauri-executable-specs-01/SKILL.md` | main | 0 |
| `skills/codex/202604/tauri-executable-specs-01/agents/openai.yaml` | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/tauri-executable-specs-01/agents/openai.yaml` | main | 0 |
| `skills/codex/202604/tauri-executable-specs-01/references/tauri-conventions-and-gates.md` | 3 | `archive/monthly-agent-snapshots/codex-skills-202604/tauri-executable-specs-01/references/tauri-conventions-and-gates.md` | main | 0 |
| `skills/codex/202604/tauri-executable-specs-01/references/tauri-doctrine.md` | 5 | `archive/monthly-agent-snapshots/codex-skills-202604/tauri-executable-specs-01/references/tauri-doctrine.md` | main | 0 |
| `skills/codex/202604/tauri-executable-specs-01/references/tauri-executable-specs-playbook.md` | 24 | `archive/monthly-agent-snapshots/codex-skills-202604/tauri-executable-specs-01/references/tauri-executable-specs-playbook.md` | main | 0 |
