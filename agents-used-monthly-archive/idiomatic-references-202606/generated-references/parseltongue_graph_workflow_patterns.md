# Parseltongue Graph Workflow Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_bidirectional_workflows.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_endpoints.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_flow_patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | primary automation and CI/CD workflow documentation |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | external_research_source_material | external_research_sourced_fact | primary guidance for reusable workflow composition |
| https://github.com/openai/codex/blob/-/AGENTS.md | external_research_source_material | external_research_sourced_fact | agent project instructions and testing guidance in a real repository |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `parseltongue_graph_workflow_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local parseltongue graph material before synthesizing workflow patterns recommendations. |
| `parseltongue_graph_workflow_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `parseltongue_graph_workflow_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `parseltongue_graph_workflow_patterns` contains 4 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Parseltongue Graph Workflow Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/SKILL.md | run-parseltongue-1-7-2 | Run Parseltongue 1.7.2; Ground Truth; Enforce Version Policy; Code Reading Preference; Flow Modeling Guardrail; Run Workflow | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_bidirectional_workflows.md | Parseltongue 1.7.2 Bidirectional Workflows | Parseltongue 1.7.2 Bidirectional Workflows; Workflow Index; 1) Meet-in-the-Middle Hypothesis Test; Symptom side: who reaches the broken point?; Root-cause side: what does the suspected culprit reach?; Quantify each side | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_endpoints.md | Parseltongue 1.7.2 Endpoints | Parseltongue 1.7.2 Endpoints; Resolve the Base URL First; shellcheck source=/dev/null; Orientation Sequence; Search and Read; Dependency Traversal | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_flow_patterns.md | Parseltongue 1.7.2 Flow Patterns | Parseltongue 1.7.2 Flow Patterns; Modeling Limits; Pattern Index; 1) Ingress-to-Sink Corridor; 2) Gatekeeper Choke Point; 3) Orchestrator Versus Leaf Worker | reference detail file for deeper pattern evidence |

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
| `official_docs_query_phrase` | parseltongue graph workflow patterns official documentation best practices |
| `github_repository_query_phrase` | parseltongue graph workflow patterns GitHub repository examples |
| `release_notes_query_phrase` | parseltongue graph workflow patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
