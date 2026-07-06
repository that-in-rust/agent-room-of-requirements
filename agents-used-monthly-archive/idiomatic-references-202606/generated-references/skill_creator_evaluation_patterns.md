# Skill Creator Evaluation Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/skill-creator/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/skill-creator/agents/analyzer.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/plugins/skill-creator/agents/comparator.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/plugins/skill-creator/agents/grader.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/plugins/skill-creator/references/schemas.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/skill-creator/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/skill-creator/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/skill-creator/agents/analyzer.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/plugins/skill-creator/agents/comparator.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/plugins/skill-creator/agents/grader.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/plugins/skill-creator/references/schemas.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary agent instruction context model |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | verification and automation model |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | general agent instruction format |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `skill_creator_evaluation_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local skill creator material before synthesizing evaluation patterns recommendations. |
| `skill_creator_evaluation_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `skill_creator_evaluation_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `skill_creator_evaluation_patterns` contains 11 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Skill Creator Evaluation Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/skill-creator/SKILL.md | skill-creator | Skill Creator; Communicating with the user; Creating a skill; Capture Intent; Interview and Research; Write the SKILL.md | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/skill-creator/agents/analyzer.md | Post-hoc Analyzer Agent | Post-hoc Analyzer Agent; Role; Inputs; Process; Step 1: Read Comparison Result; Step 2: Read Both Skills | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/plugins/skill-creator/agents/comparator.md | Blind Comparator Agent | Blind Comparator Agent; Role; Inputs; Process; Step 1: Read Both Outputs; Step 2: Understand the Task | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/plugins/skill-creator/agents/grader.md | Grader Agent | Grader Agent; Role; Inputs; Process; Step 1: Read the Transcript; Step 2: Examine Output Files | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/plugins/skill-creator/references/schemas.md | JSON Schemas | JSON Schemas; evals.json; history.json; grading.json; metrics.json; timing.json | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/skill-creator/SKILL.md | skill-creator | Skill Creator; About Skills; What Skills Provide; Core Principles; Concise is Key; Set Appropriate Degrees of Freedom | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/skill-creator/SKILL.md | skill-creator | Skill Creator; Communicating with the user; Creating a skill; Capture Intent; Interview and Research; Write the SKILL.md | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/skill-creator/agents/analyzer.md | Post-hoc Analyzer Agent | Post-hoc Analyzer Agent; Role; Inputs; Process; Step 1: Read Comparison Result; Step 2: Read Both Skills | local agent-usable source material |
| claude-skills/plugins/skill-creator/agents/comparator.md | Blind Comparator Agent | Blind Comparator Agent; Role; Inputs; Process; Step 1: Read Both Outputs; Step 2: Understand the Task | local agent-usable source material |
| claude-skills/plugins/skill-creator/agents/grader.md | Grader Agent | Grader Agent; Role; Inputs; Process; Step 1: Read the Transcript; Step 2: Examine Output Files | local agent-usable source material |
| claude-skills/plugins/skill-creator/references/schemas.md | JSON Schemas | JSON Schemas; evals.json; history.json; grading.json; metrics.json; timing.json | reference detail file for deeper pattern evidence |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | external_research_sourced_fact |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | external_research_sourced_fact |

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
| `official_docs_query_phrase` | skill creator evaluation patterns official documentation best practices |
| `github_repository_query_phrase` | skill creator evaluation patterns GitHub repository examples |
| `release_notes_query_phrase` | skill creator evaluation patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
