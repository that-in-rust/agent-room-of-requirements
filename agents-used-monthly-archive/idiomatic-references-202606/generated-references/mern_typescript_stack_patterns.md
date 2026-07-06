# Mern Typescript Stack Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202602/MERN-coder-01.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/mern-coder-01/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/mern-coder-01/references/doctrine.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/idiomatic-references-202602/MERN-TypeScript-IdiomaticPatterns_20251206.md | local_corpus_source_material | local_corpus_sourced_fact | historical idiomatic pattern corpus |
| https://www.typescriptlang.org/docs/handbook/intro.html | external_research_source_material | external_research_sourced_fact | primary TypeScript language documentation |
| https://expressjs.com/en/ | external_research_source_material | external_research_sourced_fact | Node.js web framework documentation |
| https://www.mongodb.com/resources/products/compatibilities/using-typescript-with-mongodb-tutorial | external_research_source_material | external_research_sourced_fact | MongoDB TypeScript integration guidance |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `mern_typescript_stack_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local mern typescript material before synthesizing stack patterns recommendations. |
| `mern_typescript_stack_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `mern_typescript_stack_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `mern_typescript_stack_patterns` contains 4 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Mern Typescript Stack Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202602/MERN-coder-01.md | MERN-coder-01 | MERN Coder 01; Premise Check; Coverage Verdict; Selection Method; The Cut: Patterns Above 80; Section 1: Contract Boundaries | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/mern-coder-01/SKILL.md | mern-coder-01 | MERN Coder 01; Overview; Workflow; Default Rules; Reference Map; Boundary Notes | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/mern-coder-01/references/doctrine.md | MERN-coder-01 | MERN Coder 01; Premise Check; Coverage Verdict; Selection Method; The Cut: Patterns Above 80; Section 1: Contract Boundaries | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/idiomatic-references-202602/MERN-TypeScript-IdiomaticPatterns_20251206.md | MERN + TypeScript Idiomatic Pattern Library | MERN + TypeScript Idiomatic Pattern Library; Table of Contents; Getting Started; Prerequisites Pattern; Environment Configuration Pattern; Project Structure Patterns | historical idiomatic pattern corpus |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://www.typescriptlang.org/docs/handbook/intro.html | TypeScript handbook | primary TypeScript language documentation | external_research_sourced_fact |
| https://expressjs.com/en/ | Express documentation | Node.js web framework documentation | external_research_sourced_fact |
| https://www.mongodb.com/resources/products/compatibilities/using-typescript-with-mongodb-tutorial | MongoDB TypeScript guide | MongoDB TypeScript integration guidance | external_research_sourced_fact |

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
| `official_docs_query_phrase` | mern typescript stack patterns official documentation best practices |
| `github_repository_query_phrase` | mern typescript stack patterns GitHub repository examples |
| `release_notes_query_phrase` | mern typescript stack patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
