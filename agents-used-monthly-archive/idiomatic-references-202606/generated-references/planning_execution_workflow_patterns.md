# Planning Execution Workflow Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| A01-LLM-Workflow01.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/executing-plans/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-plans/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/rewrite-backups-20260514/A01-LLM-Workflow01.rewrite-draft.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/superpowers/executing-plans/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/writing-plans/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | primary automation and CI/CD workflow documentation |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | external_research_source_material | external_research_sourced_fact | primary guidance for reusable workflow composition |
| https://github.com/openai/codex/blob/-/AGENTS.md | external_research_source_material | external_research_sourced_fact | agent project instructions and testing guidance in a real repository |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `planning_execution_workflow_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local planning execution material before synthesizing workflow patterns recommendations. |
| `planning_execution_workflow_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `planning_execution_workflow_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `planning_execution_workflow_patterns` contains 6 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Planning Execution Workflow Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| A01-LLM-Workflow01.md | LLM Workflow v01: Work Type Differentiation | LLM Workflow v01: Work Type Differentiation; Quick Classifier; Work Type Framework; Flow 1: Bug Flow (Hours); Flow 2: Enhancement Flow (Days); Flow 3: Feature Flow (Weeks) | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/executing-plans/SKILL.md | executing-plans | Executing Plans; Overview; The Process; Step 1: Load and Review Plan; Step 2: Execute Batch; Step 3: Report | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-plans/SKILL.md | writing-plans | Writing Plans; Overview; Bite-Sized Task Granularity; Plan Document Header; [Feature Name] Implementation Plan; Task Structure | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/rewrite-backups-20260514/A01-LLM-Workflow01.rewrite-draft.md | LLM Workflow v01: Work Type Differentiation | LLM Workflow v01: Work Type Differentiation; Quick Classifier; Work Type Framework; Flow 1: Bug Flow (Hours); Flow 2: Enhancement Flow (Days); Flow 3: Feature Flow (Weeks) | local agent-usable source material |
| claude-skills/superpowers/executing-plans/SKILL.md | executing-plans | Executing Plans; Overview; The Process; Step 1: Load and Review Plan; Step 2: Execute Batch; Step 3: Report | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/writing-plans/SKILL.md | writing-plans | Writing Plans; Overview; Bite-Sized Task Granularity; Plan Document Header; [Feature Name] Implementation Plan; Task Structure | skill entrypoint or reusable agent prompt |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://docs.github.com/actions | GitHub Actions documentation | primary automation and CI/CD workflow documentation | external_research_sourced_fact |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | Reusable workflow docs | primary guidance for reusable workflow composition | external_research_sourced_fact |
| https://github.com/openai/codex/blob/-/AGENTS.md | OpenAI Codex repository AGENTS | agent project instructions and testing guidance in a real repository | external_research_sourced_fact |

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
| `official_docs_query_phrase` | planning execution workflow patterns official documentation best practices |
| `github_repository_query_phrase` | planning execution workflow patterns GitHub repository examples |
| `release_notes_query_phrase` | planning execution workflow patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
