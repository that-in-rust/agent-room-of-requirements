# Rust-skills

The files in this repository that are about Rust (and Tauri, which is a Rust framework),
gathered in one place: 120 files. Each is a byte-identical copy of an original; the
originals are unchanged and remain the source.

| Folder | Files | What it holds |
|---|---|---|
| `idiomatic-references/` | 76 | Rust and Tauri idiomatic references: current (202607), seed, and the 202604 and 202606 archives |
| `skills/` | 29 | Archived Codex and Claude skills for Rust and Tauri, by month |
| `methodology/` | 2 | Rust and Tauri executable-specification method |
| `research/` | 4 | Strategy notes about Rust |
| `other-rust-content/` | 9 | Files not named after Rust that hold a large amount of Rust code or Rust guidance |

How the set was built:

1. Every file on all three branches was searched by content for `rust` at the start of a word,
   whatever the file's name. 271 distinct files matched.
2. Files with identical content are kept once, so some month folders under `skills/` are incomplete.
3. Where several versions of one document existed, only the newest is kept. In every case the
   newest already held everything in the older ones.
4. Files where Rust is not the subject were left out: files that mention it once or twice,
   files that mention it in under 5% of their lines, project bookkeeping that only lists Rust
   file names (task queues, assignment sheets, document indexes, coverage ledgers, progress logs),
   and the review question packets.

Links inside the copied files still point to their original relative locations and may not resolve from here.

## Every file and where it came from

"Rust lines" is the share of non-empty lines that mention Rust or a common Rust tool or crate, or sit inside a Rust code block.

| File | Rust lines | Rust code lines | Original path on `main` |
|---|---|---|---|
| `idiomatic-references/archive-202604/rust-executable-specs-01/rust-executable-specs-reference.md` | 17% | 9 | `archive/monthly-agent-snapshots/idiomatic-references-202604/rust-executable-specs-01/rust-executable-specs-reference.md` |
| `idiomatic-references/archive-202604/tauri-executable-specs-01/tauri-executable-specs-reference.md` | 19% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202604/tauri-executable-specs-01/tauri-executable-specs-reference.md` |
| `idiomatic-references/archive-202606/generated-references/rust_backend_playbook_reference.md` | 25% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_playbook_reference.md` |
| `idiomatic-references/archive-202606/generated-references/rust_backend_reference_routing.md` | 24% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_reference_routing.md` |
| `idiomatic-references/archive-202606/generated-references/rust_backend_runtime_operations.md` | 25% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_runtime_operations.md` |
| `idiomatic-references/archive-202606/generated-references/rust_backend_security_resilience.md` | 25% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_security_resilience.md` |
| `idiomatic-references/archive-202606/generated-references/rust_backend_skill_entrypoint.md` | 27% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_skill_entrypoint.md` |
| `idiomatic-references/archive-202606/generated-references/rust_backend_testing_fixtures.md` | 25% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_backend_testing_fixtures.md` |
| `idiomatic-references/archive-202606/generated-references/rust_coder_reliability_patterns.md` | 29% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_coder_reliability_patterns.md` |
| `idiomatic-references/archive-202606/generated-references/rust_conventions_quality_gates.md` | 25% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_conventions_quality_gates.md` |
| `idiomatic-references/archive-202606/generated-references/rust_executable_reference_maps.md` | 28% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_executable_reference_maps.md` |
| `idiomatic-references/archive-202606/generated-references/rust_executable_reliability_reference.md` | 25% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_executable_reliability_reference.md` |
| `idiomatic-references/archive-202606/generated-references/rust_executable_skill_patterns.md` | 28% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_executable_skill_patterns.md` |
| `idiomatic-references/archive-202606/generated-references/rust_executable_template_patterns.md` | 29% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_executable_template_patterns.md` |
| `idiomatic-references/archive-202606/generated-references/rust_idiomatic_skill_patterns.md` | 27% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_idiomatic_skill_patterns.md` |
| `idiomatic-references/archive-202606/generated-references/rust_idioms_checklist_patterns.md` | 28% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_idioms_checklist_patterns.md` |
| `idiomatic-references/archive-202606/generated-references/rust_legacy_coder_prompts.md` | 29% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_legacy_coder_prompts.md` |
| `idiomatic-references/archive-202606/generated-references/rust_quality_gate_patterns.md` | 27% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/rust_quality_gate_patterns.md` |
| `idiomatic-references/archive-202606/generated-references/tauri_conventions_quality_gates.md` | 25% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_conventions_quality_gates.md` |
| `idiomatic-references/archive-202606/generated-references/tauri_doctrine_source_review.md` | 26% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_doctrine_source_review.md` |
| `idiomatic-references/archive-202606/generated-references/tauri_executable_playbook_templates.md` | 27% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_executable_playbook_templates.md` |
| `idiomatic-references/archive-202606/generated-references/tauri_executable_reference_maps.md` | 28% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_executable_reference_maps.md` |
| `idiomatic-references/archive-202606/generated-references/tauri_executable_skill_patterns.md` | 28% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_executable_skill_patterns.md` |
| `idiomatic-references/archive-202606/generated-references/tauri_legacy_coder_patterns.md` | 31% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/generated-references/tauri_legacy_coder_patterns.md` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-coverage-ledger.json` | 34% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-coverage-ledger.json` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-evidence-index.json` | 10% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-evidence-index.json` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part1-repos.txt` | 69% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-1-repos.txt` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part1.md` | 38% | 274 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-Part1.md` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part2-repos.txt` | 70% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-2-repos.txt` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part2.md` | 44% | 486 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-Part2.md` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part3-repos.txt` | 69% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-3-repos.txt` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part3.md` | 40% | 328 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-Part3.md` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part4-repos.txt` | 69% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-4-repos.txt` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part4.md` | 43% | 596 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-Part4.md` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part5-repos.txt` | 69% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-5-repos.txt` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-Part5.md` | 39% | 430 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-Part5.md` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-progress.md` | 37% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-progress.md` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-repo-inventory.json` | 27% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-repo-inventory.json` |
| `idiomatic-references/archive-202606/meta-rust-ref-202606-scan-summary.json` | 0% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/meta-rust-ref-202606-scan-summary.json` |
| `idiomatic-references/archive-202606/rust-patterns-1-repos.txt` | 13% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-1-repos.txt` |
| `idiomatic-references/archive-202606/rust-patterns-1.md` | 77% | 572 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-1.md` |
| `idiomatic-references/archive-202606/rust-patterns-2-repos.txt` | 13% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-2-repos.txt` |
| `idiomatic-references/archive-202606/rust-patterns-2.md` | 78% | 767 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-2.md` |
| `idiomatic-references/archive-202606/rust-patterns-3-repos.txt` | 19% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-3-repos.txt` |
| `idiomatic-references/archive-202606/rust-patterns-3.md` | 80% | 622 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-3.md` |
| `idiomatic-references/archive-202606/rust-patterns-4.md` | 79% | 978 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-4.md` |
| `idiomatic-references/archive-202606/rust-patterns-5.md` | 79% | 858 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-5.md` |
| `idiomatic-references/archive-202606/rust-patterns-codegraphcontext-evidence.json` | 9% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-codegraphcontext-evidence.json` |
| `idiomatic-references/archive-202606/rust-patterns-progress.md` | 44% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-progress.md` |
| `idiomatic-references/archive-202606/rust-patterns-repo-inventory.json` | 14% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-repo-inventory.json` |
| `idiomatic-references/archive-202606/rust-patterns-scan-summary.json` | 38% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/rust-patterns-scan-summary.json` |
| `idiomatic-references/archive-202606/tools/verify_meta_rust_ref.py` | 8% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/tools/verify_meta_rust_ref.py` |
| `idiomatic-references/archive-202606/tools/verify_rust_patterns_reference.py` | 7% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/tools/verify_rust_patterns_reference.py` |
| `idiomatic-references/current-202607/rust/rust_backend_playbook_reference-20260710.md` | 18% | 0 | `library/idiomatic/202607/rust_backend_playbook_reference-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_backend_reference_routing-20260710.md` | 14% | 0 | `library/idiomatic/202607/rust_backend_reference_routing-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_backend_runtime_operations-20260710.md` | 14% | 0 | `library/idiomatic/202607/rust_backend_runtime_operations-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_backend_security_resilience-20260710.md` | 15% | 0 | `library/idiomatic/202607/rust_backend_security_resilience-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_backend_skill_entrypoint-20260710.md` | 14% | 0 | `library/idiomatic/202607/rust_backend_skill_entrypoint-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_backend_testing_fixtures-20260710.md` | 13% | 0 | `library/idiomatic/202607/rust_backend_testing_fixtures-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_coder_reliability_patterns-20260710.md` | 25% | 0 | `library/idiomatic/202607/rust_coder_reliability_patterns-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_conventions_quality_gates-20260710.md` | 20% | 0 | `library/idiomatic/202607/rust_conventions_quality_gates-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_executable_reference_maps-20260710.md` | 14% | 0 | `library/idiomatic/202607/rust_executable_reference_maps-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_executable_reliability_reference-20260710.md` | 15% | 0 | `library/idiomatic/202607/rust_executable_reliability_reference-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_executable_skill_patterns-20260710.md` | 17% | 0 | `library/idiomatic/202607/rust_executable_skill_patterns-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_executable_template_patterns-20260710.md` | 16% | 0 | `library/idiomatic/202607/rust_executable_template_patterns-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_idiomatic_skill_patterns-20260710.md` | 16% | 0 | `library/idiomatic/202607/rust_idiomatic_skill_patterns-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_idioms_checklist_patterns-20260710.md` | 31% | 0 | `library/idiomatic/202607/rust_idioms_checklist_patterns-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_legacy_coder_prompts-20260710.md` | 29% | 0 | `library/idiomatic/202607/rust_legacy_coder_prompts-20260710.md` |
| `idiomatic-references/current-202607/rust/rust_quality_gate_patterns-20260710.md` | 12% | 0 | `library/idiomatic/202607/rust_quality_gate_patterns-20260710.md` |
| `idiomatic-references/current-202607/tauri/tauri_conventions_quality_gates-20260710.md` | 27% | 0 | `library/idiomatic/202607/tauri_conventions_quality_gates-20260710.md` |
| `idiomatic-references/current-202607/tauri/tauri_doctrine_source_review-20260710.md` | 23% | 0 | `library/idiomatic/202607/tauri_doctrine_source_review-20260710.md` |
| `idiomatic-references/current-202607/tauri/tauri_executable_playbook_templates-20260710.md` | 30% | 0 | `library/idiomatic/202607/tauri_executable_playbook_templates-20260710.md` |
| `idiomatic-references/current-202607/tauri/tauri_executable_reference_maps-20260710.md` | 23% | 0 | `library/idiomatic/202607/tauri_executable_reference_maps-20260710.md` |
| `idiomatic-references/current-202607/tauri/tauri_executable_skill_patterns-20260710.md` | 19% | 0 | `library/idiomatic/202607/tauri_executable_skill_patterns-20260710.md` |
| `idiomatic-references/current-202607/tauri/tauri_legacy_coder_patterns-20260710.md` | 22% | 0 | `library/idiomatic/202607/tauri_legacy_coder_patterns-20260710.md` |
| `idiomatic-references/seed/Rust-Coder-1000IQ-01.md` | 17% | 0 | `library/idiomatic/seed/Rust-Coder-1000IQ-01.md` |
| `methodology/executable-specifications/rust/core.md` | 19% | 0 | `methodology/executable-specifications/rust/core.md` |
| `methodology/executable-specifications/tauri/core.md` | 27% | 0 | `methodology/executable-specifications/tauri/core.md` |
| `other-rust-content/broad-idiomatic-patterns.md` | 13% | 2 | `archive/monthly-agent-snapshots/idiomatic-references-202602/broad-idiomatic-patterns.md` |
| `other-rust-content/critique-JD-01.md` | 6% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/critique-JD-01.md` |
| `other-rust-content/critique-SD-01.md` | 9% | 0 | `archive/monthly-agent-snapshots/idiomatic-references-202606/critique-SD-01.md` |
| `other-rust-content/idiomatic-code-patterns-1.md` | 18% | 539 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-1.md` |
| `other-rust-content/idiomatic-code-patterns-2.md` | 27% | 942 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-2.md` |
| `other-rust-content/idiomatic-code-patterns-3.md` | 27% | 741 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-3.md` |
| `other-rust-content/idiomatic-code-patterns-4.md` | 26% | 800 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-4.md` |
| `other-rust-content/idiomatic-code-patterns-5.md` | 21% | 765 | `archive/monthly-agent-snapshots/idiomatic-references-202606/idiomatic-code-patterns-5.md` |
| `other-rust-content/notes01-agent.md` | 16% | 163 | `archive/monthly-agent-snapshots/claude-skills-202602/notes01-agent.md` |
| `research/20-more-rust-hackathon-ideas-after-the-first-shortlist.md` | 25% | 0 | `research/strategic/20-more-rust-hackathon-ideas-after-the-first-shortlist.md` |
| `research/how-to-rank-rust-opportunities-when-codex-is-helping.md` | 26% | 0 | `research/strategic/how-to-rank-rust-opportunities-when-codex-is-helping.md` |
| `research/how-to-win-a-rust-hackathon-in-6-hours.md` | 28% | 0 | `research/strategic/how-to-win-a-rust-hackathon-in-6-hours.md` |
| `research/why-rust-backends-need-a-separate-playbook.md` | 20% | 0 | `research/strategic/why-rust-backends-need-a-separate-playbook.md` |
| `skills/claude/202602/rust-coder-01.md` | 42% | 957 | `archive/monthly-agent-snapshots/claude-skills-202602/rust-coder-01.md` |
| `skills/claude/202602/rust-coder-02.md` | 6% | 0 | `archive/monthly-agent-snapshots/claude-skills-202602/rust-coder-02.md` |
| `skills/claude/202602/Tauri-coder-01.md` | 45% | 397 | `archive/monthly-agent-snapshots/claude-skills-202602/Tauri-coder-01.md` |
| `skills/claude/202604/personal/rust-web-backend-skill-explainer/SKILL.md` | 21% | 0 | `archive/monthly-agent-snapshots/claude-skills-202604/personal/rust-web-backend-skill-explainer/SKILL.md` |
| `skills/claude/202604/rust-executable-specs-01.md` | 19% | 0 | `archive/monthly-agent-snapshots/claude-skills-202604/rust-executable-specs-01.md` |
| `skills/claude/202604/tauri-executable-specs-01.md` | 27% | 0 | `archive/monthly-agent-snapshots/claude-skills-202604/tauri-executable-specs-01.md` |
| `skills/codex/202602/idiomatic-rust-coder-01/agents/openai.yaml` | 75% | 0 | `archive/monthly-agent-snapshots/codex-skills-202602/idiomatic-rust-coder-01/agents/openai.yaml` |
| `skills/codex/202602/idiomatic-rust-coder-01/references/rust-executable-specs-templates.md` | 61% | 42 | `archive/monthly-agent-snapshots/codex-skills-202602/idiomatic-rust-coder-01/references/rust-executable-specs-templates.md` |
| `skills/codex/202602/idiomatic-rust-coder-01/references/rust-idioms-checklist.md` | 19% | 0 | `archive/monthly-agent-snapshots/codex-skills-202602/idiomatic-rust-coder-01/references/rust-idioms-checklist.md` |
| `skills/codex/202602/idiomatic-rust-coder-01/references/rust-quality-gates-anti-patterns.md` | 23% | 0 | `archive/monthly-agent-snapshots/codex-skills-202602/idiomatic-rust-coder-01/references/rust-quality-gates-anti-patterns.md` |
| `skills/codex/202603/idiomatic-rust-coder-01/SKILL.md` | 28% | 0 | `archive/monthly-agent-snapshots/codex-skills-202603/idiomatic-rust-coder-01/SKILL.md` |
| `skills/codex/202603/rust-coder-02/agents/openai.yaml` | 75% | 0 | `archive/monthly-agent-snapshots/codex-skills-202603/rust-coder-02/agents/openai.yaml` |
| `skills/codex/202603/rust-coder-02/references/reference-map.md` | 21% | 0 | `archive/monthly-agent-snapshots/codex-skills-202603/rust-coder-02/references/reference-map.md` |
| `skills/codex/202603/rust-coder-02/SKILL.md` | 40% | 0 | `archive/monthly-agent-snapshots/codex-skills-202603/rust-coder-02/SKILL.md` |
| `skills/codex/202603/tauri-coder-01/agents/openai.yaml` | 75% | 0 | `archive/monthly-agent-snapshots/codex-skills-202603/tauri-coder-01/agents/openai.yaml` |
| `skills/codex/202603/tauri-coder-01/references/reference-map.md` | 21% | 0 | `archive/monthly-agent-snapshots/codex-skills-202603/tauri-coder-01/references/reference-map.md` |
| `skills/codex/202604/rust-executable-specs-01/agents/openai.yaml` | 75% | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-executable-specs-01/agents/openai.yaml` |
| `skills/codex/202604/rust-executable-specs-01/references/reference-map.md` | 42% | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-executable-specs-01/references/reference-map.md` |
| `skills/codex/202604/rust-executable-specs-01/references/rust-conventions-and-gates.md` | 31% | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-executable-specs-01/references/rust-conventions-and-gates.md` |
| `skills/codex/202604/rust-executable-specs-01/references/rust-executable-specs-playbook.md` | 48% | 61 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-executable-specs-01/references/rust-executable-specs-playbook.md` |
| `skills/codex/202604/rust-executable-specs-01/SKILL.md` | 26% | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-executable-specs-01/SKILL.md` |
| `skills/codex/202604/rust-web-backend-delivery-01/agents/openai.yaml` | 75% | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-web-backend-delivery-01/agents/openai.yaml` |
| `skills/codex/202604/rust-web-backend-delivery-01/references/reference-map.md` | 51% | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-web-backend-delivery-01/references/reference-map.md` |
| `skills/codex/202604/rust-web-backend-delivery-01/SKILL.md` | 23% | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/rust-web-backend-delivery-01/SKILL.md` |
| `skills/codex/202604/tauri-executable-specs-01/agents/openai.yaml` | 75% | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/tauri-executable-specs-01/agents/openai.yaml` |
| `skills/codex/202604/tauri-executable-specs-01/references/tauri-conventions-and-gates.md` | 31% | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/tauri-executable-specs-01/references/tauri-conventions-and-gates.md` |
| `skills/codex/202604/tauri-executable-specs-01/references/tauri-doctrine.md` | 13% | 12 | `archive/monthly-agent-snapshots/codex-skills-202604/tauri-executable-specs-01/references/tauri-doctrine.md` |
| `skills/codex/202604/tauri-executable-specs-01/references/tauri-executable-specs-playbook.md` | 36% | 19 | `archive/monthly-agent-snapshots/codex-skills-202604/tauri-executable-specs-01/references/tauri-executable-specs-playbook.md` |
| `skills/codex/202604/tauri-executable-specs-01/SKILL.md` | 34% | 0 | `archive/monthly-agent-snapshots/codex-skills-202604/tauri-executable-specs-01/SKILL.md` |
