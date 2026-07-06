# Agent Debate Evidence Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/debate-template-and-tag-rules.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/evidence-and-convergence-guardrails.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/repo-workflow-notes.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/debate-template-and-tag-rules.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/evidence-and-convergence-guardrails.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/repo-workflow-notes.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary guidance for project instruction files and agent context loading |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | community format for predictable agent instructions |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | GitHub implementation and project-level agent guidance |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `agent_debate_evidence_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local agent debate material before synthesizing evidence patterns recommendations. |
| `agent_debate_evidence_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `agent_debate_evidence_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `agent_debate_evidence_patterns` contains 8 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Agent Debate Evidence Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/SKILL.md | agent-debate-01 | Agent Debate 01; When To Debate; Workflow; Script Usage; Output Contract; Guardrails | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/debate-template-and-tag-rules.md | Debate Template and Tag Rules | Debate Template and Tag Rules; Required Sections; Debate: {TOPIC}; Context; Evidence; Relevant Files | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/evidence-and-convergence-guardrails.md | Evidence and Convergence Guardrails | Evidence and Convergence Guardrails; Evidence Standard; Simplicity Rules; Behavioral Rules; Convergence Rules | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/repo-workflow-notes.md | Repo Workflow Notes | Repo Workflow Notes; Core Model; Typical Debate Prompts; Upstream CLI Notes; Practical Limitation | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/SKILL.md | agent-debate-01 | Agent Debate 01; When To Debate; Workflow; Script Usage; Output Contract; Guardrails | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/debate-template-and-tag-rules.md | Debate Template and Tag Rules | Debate Template and Tag Rules; Required Sections; Debate: {TOPIC}; Context; Evidence; Relevant Files | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/evidence-and-convergence-guardrails.md | Evidence and Convergence Guardrails | Evidence and Convergence Guardrails; Evidence Standard; Simplicity Rules; Behavioral Rules; Convergence Rules | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/repo-workflow-notes.md | Repo Workflow Notes | Repo Workflow Notes; Core Model; Typical Debate Prompts; Upstream CLI Notes; Practical Limitation | reference detail file for deeper pattern evidence |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary guidance for project instruction files and agent context loading | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | community format for predictable agent instructions | external_research_sourced_fact |
| https://github.com/openai/codex | OpenAI Codex repository | GitHub implementation and project-level agent guidance | external_research_sourced_fact |

## Anti Pattern Registry Table

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | agent debate evidence patterns official documentation best practices |
| `github_repository_query_phrase` | agent debate evidence patterns GitHub repository examples |
| `release_notes_query_phrase` | agent debate evidence patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
