# Image Generation Prompt Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/cli.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/codex-network.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/image-api.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/prompting.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/sample-prompts.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://platform.openai.com/docs/guides/images | external_research_source_material | external_research_sourced_fact | primary image generation API documentation |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | agent runtime and CLI reference point |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `image_generation_prompt_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local image generation material before synthesizing prompt patterns recommendations. |
| `image_generation_prompt_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `image_generation_prompt_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `image_generation_prompt_patterns` contains 6 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Image Generation Prompt Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/SKILL.md | "imagegen" | Image Generation Skill; Top-level modes and rules; When to use; When not to use; Decision tree; Workflow | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/cli.md | CLI reference ('scripts/image_gen.py') | CLI reference ('scripts/image_gen.py'); What this CLI does; Quick start (works from any repo); Quick start; Guardrails; Defaults | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/codex-network.md | Codex network approvals / sandbox notes | Codex network approvals / sandbox notes; Why am I asked to approve image generation calls?; Important note about approvals vs network; How do I reduce repeated approval prompts?; Safety note | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/image-api.md | Image API quick reference | Image API quick reference; Scope; Endpoints; Core parameters for GPT Image models; Edit-specific parameters; Output | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/prompting.md | Prompting best practices | Prompting best practices; Contents; Structure; Specificity policy; Allowed and disallowed augmentation; Composition and layout | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/sample-prompts.md | Sample prompts (copy/paste) | Sample prompts (copy/paste); Generate; photorealistic-natural; product-mockup; ui-mockup; infographic-diagram | reference detail file for deeper pattern evidence |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://platform.openai.com/docs/guides/images | OpenAI image generation guide | primary image generation API documentation | external_research_sourced_fact |
| https://github.com/openai/codex | OpenAI Codex repository | agent runtime and CLI reference point | external_research_sourced_fact |

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
| `official_docs_query_phrase` | image generation prompt patterns official documentation best practices |
| `github_repository_query_phrase` | image generation prompt patterns GitHub repository examples |
| `release_notes_query_phrase` | image generation prompt patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
