# Github Context Capture Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/discussions-graphql-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/ghcli-surface-map.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/github-repo-context-thesis.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/output-contract.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | primary workflow and automation documentation |
| https://github.com/github/github-mcp-server | external_research_source_material | external_research_sourced_fact | GitHub repository automation through MCP |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | external_research_source_material | external_research_sourced_fact | workflow reuse and governance guidance |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `github_context_capture_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local github context material before synthesizing capture patterns recommendations. |
| `github_context_capture_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `github_context_capture_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `github_context_capture_patterns` contains 5 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Github Context Capture Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/SKILL.md | capture-github-repo-context | Capture GitHub Repo Context; Goal; Choose The Right Mode; Workflow; Command Selection Guide; Use The Bundled Scripts | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/discussions-graphql-patterns.md | Discussions GraphQL Patterns | Discussions GraphQL Patterns; Table Of Contents; Why Discussions Need GraphQL; Repo-Wide Discussion Index; Focused Discussion Thread; Limits And Caveats | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/ghcli-surface-map.md | GHCLI Surface Map | GHCLI Surface Map; Table Of Contents; Command Choice Rules; Surface Matrix; Common Traps; Trap 1: Treating issue comments as all PR discussion | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/github-repo-context-thesis.md | GitHub Repo Context Thesis | GitHub Repo Context Thesis; Table Of Contents; Core Thesis; Why This Skill Matters; What Counts As Repository Context; Content surfaces | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/output-contract.md | Output Contract | Output Contract; Table Of Contents; Digest Goals; Required Sections; Coverage Notes; Raw Artifact Expectations | reference detail file for deeper pattern evidence |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://docs.github.com/actions | GitHub Actions documentation | primary workflow and automation documentation | external_research_sourced_fact |
| https://github.com/github/github-mcp-server | GitHub MCP server | GitHub repository automation through MCP | external_research_sourced_fact |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | Reusable workflow docs | workflow reuse and governance guidance | external_research_sourced_fact |

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
| `official_docs_query_phrase` | github context capture patterns official documentation best practices |
| `github_repository_query_phrase` | github context capture patterns GitHub repository examples |
| `release_notes_query_phrase` | github context capture patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
