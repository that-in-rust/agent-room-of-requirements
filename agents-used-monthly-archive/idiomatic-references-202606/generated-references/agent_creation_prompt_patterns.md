# Agent Creation Prompt Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/examples/agent-creation-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | example or template demonstrating expected artifact shape |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/examples/complete-agent-examples.md | local_corpus_source_material | local_corpus_sourced_fact | example or template demonstrating expected artifact shape |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/agent-creation-system-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/system-prompt-design.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/triggering-examples.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/agent-development/examples/agent-creation-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | example or template demonstrating expected artifact shape |
| claude-skills/plugins/plugin-dev/agent-development/examples/complete-agent-examples.md | local_corpus_source_material | local_corpus_sourced_fact | example or template demonstrating expected artifact shape |
| claude-skills/plugins/plugin-dev/agent-development/references/agent-creation-system-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/references/system-prompt-design.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/references/triggering-examples.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary guidance for project instruction files and agent context loading |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | community format for predictable agent instructions |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | GitHub implementation and project-level agent guidance |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `agent_creation_prompt_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local agent creation material before synthesizing prompt patterns recommendations. |
| `agent_creation_prompt_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `agent_creation_prompt_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `agent_creation_prompt_patterns` contains 12 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Agent Creation Prompt Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/SKILL.md | agent-development | Agent Development for Claude Code Plugins; Overview; Agent File Structure; Complete Format; Frontmatter Fields; name (required) | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/examples/agent-creation-prompt.md | AI-Assisted Agent Generation Template | AI-Assisted Agent Generation Template; Usage Pattern; Step 1: Describe Your Agent Need; Step 2: Use the Generation Prompt; Step 3: Claude Returns JSON; Step 4: Convert to Agent File | example or template demonstrating expected artifact shape |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/examples/complete-agent-examples.md | Complete Agent Examples | Complete Agent Examples; Example 1: Code Review Agent; Code Review Summary; Critical Issues (Must Fix); Major Issues (Should Fix); Minor Issues (Consider Fixing) | example or template demonstrating expected artifact shape |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/agent-creation-system-prompt.md | Agent Creation System Prompt | Agent Creation System Prompt; The Prompt; Usage Pattern; Converting to Agent File; Customization Tips; Adapt the System Prompt | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/system-prompt-design.md | System Prompt Design Patterns | System Prompt Design Patterns; Core Structure; Pattern 1: Analysis Agents; Summary; Critical Issues; Major Issues | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/triggering-examples.md | Agent Triggering Examples: Best Practices | Agent Triggering Examples: Best Practices; Example Block Format; Anatomy of a Good Example; Context; User Message; Assistant Response (Before Triggering) | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/SKILL.md | agent-development | Agent Development for Claude Code Plugins; Overview; Agent File Structure; Complete Format; Frontmatter Fields; name (required) | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/agent-development/examples/agent-creation-prompt.md | AI-Assisted Agent Generation Template | AI-Assisted Agent Generation Template; Usage Pattern; Step 1: Describe Your Agent Need; Step 2: Use the Generation Prompt; Step 3: Claude Returns JSON; Step 4: Convert to Agent File | example or template demonstrating expected artifact shape |
| claude-skills/plugins/plugin-dev/agent-development/examples/complete-agent-examples.md | Complete Agent Examples | Complete Agent Examples; Example 1: Code Review Agent; Code Review Summary; Critical Issues (Must Fix); Major Issues (Should Fix); Minor Issues (Consider Fixing) | example or template demonstrating expected artifact shape |
| claude-skills/plugins/plugin-dev/agent-development/references/agent-creation-system-prompt.md | Agent Creation System Prompt | Agent Creation System Prompt; The Prompt; Usage Pattern; Converting to Agent File; Customization Tips; Adapt the System Prompt | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/references/system-prompt-design.md | System Prompt Design Patterns | System Prompt Design Patterns; Core Structure; Pattern 1: Analysis Agents; Summary; Critical Issues; Major Issues | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/references/triggering-examples.md | Agent Triggering Examples: Best Practices | Agent Triggering Examples: Best Practices; Example Block Format; Anatomy of a Good Example; Context; User Message; Assistant Response (Before Triggering) | reference detail file for deeper pattern evidence |

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
| `official_docs_query_phrase` | agent creation prompt patterns official documentation best practices |
| `github_repository_query_phrase` | agent creation prompt patterns GitHub repository examples |
| `release_notes_query_phrase` | agent creation prompt patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
