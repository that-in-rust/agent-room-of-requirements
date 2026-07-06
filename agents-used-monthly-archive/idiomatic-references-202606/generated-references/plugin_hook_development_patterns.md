# Plugin Hook Development Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/hookify/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/advanced.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/migration.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/hookify/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/hook-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/hook-development/references/advanced.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/hook-development/references/migration.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/hook-development/references/patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | external_research_source_material | external_research_sourced_fact | primary MCP resource model for context sharing |
| https://github.com/modelcontextprotocol/servers | external_research_source_material | external_research_sourced_fact | reference and community server implementation index |
| https://github.com/github/github-mcp-server | external_research_source_material | external_research_sourced_fact | GitHub-backed MCP server for repository and issue operations |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `plugin_hook_development_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local plugin hook material before synthesizing development patterns recommendations. |
| `plugin_hook_development_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `plugin_hook_development_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `plugin_hook_development_patterns` contains 10 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Plugin Hook Development Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/hookify/SKILL.md | writing-hookify-rules | Writing Hookify Rules; Overview; Rule File Format; Basic Structure; Frontmatter Fields; Advanced Format (Multiple Conditions) | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/SKILL.md | hook-development | Hook Development for Claude Code Plugins; Overview; Hook Types; Prompt-Based Hooks (Recommended); Command Hooks; Hook Configuration Formats | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/advanced.md | Advanced Hook Use Cases | Advanced Hook Use Cases; Multi-Stage Validation; !/bin/bash; Immediate approval for safe commands; Let prompt hook handle complex cases; Conditional Hook Execution | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/migration.md | Migrating from Basic to Advanced Hooks | Migrating from Basic to Advanced Hooks; Why Migrate?; Migration Example: Bash Command Validation; Before (Basic Command Hook); !/bin/bash; Hard-coded validation logic | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/patterns.md | Common Hook Patterns | Common Hook Patterns; Pattern 1: Security Validation; Pattern 2: Test Enforcement; Pattern 3: Context Loading; !/bin/bash; Detect project type | reference detail file for deeper pattern evidence |
| claude-skills/plugins/hookify/SKILL.md | writing-hookify-rules | Writing Hookify Rules; Overview; Rule File Format; Basic Structure; Frontmatter Fields; Advanced Format (Multiple Conditions) | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/hook-development/SKILL.md | hook-development | Hook Development for Claude Code Plugins; Overview; Hook Types; Prompt-Based Hooks (Recommended); Command Hooks; Hook Configuration Formats | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/hook-development/references/advanced.md | Advanced Hook Use Cases | Advanced Hook Use Cases; Multi-Stage Validation; !/bin/bash; Immediate approval for safe commands; Let prompt hook handle complex cases; Conditional Hook Execution | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/hook-development/references/migration.md | Migrating from Basic to Advanced Hooks | Migrating from Basic to Advanced Hooks; Why Migrate?; Migration Example: Bash Command Validation; Before (Basic Command Hook); !/bin/bash; Hard-coded validation logic | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/hook-development/references/patterns.md | Common Hook Patterns | Common Hook Patterns; Pattern 1: Security Validation; Pattern 2: Test Enforcement; Pattern 3: Context Loading; !/bin/bash; Detect project type | reference detail file for deeper pattern evidence |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | Model Context Protocol resources | primary MCP resource model for context sharing | external_research_sourced_fact |
| https://github.com/modelcontextprotocol/servers | MCP server implementations | reference and community server implementation index | external_research_sourced_fact |
| https://github.com/github/github-mcp-server | GitHub MCP server | GitHub-backed MCP server for repository and issue operations | external_research_sourced_fact |

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
| `official_docs_query_phrase` | plugin hook development patterns official documentation best practices |
| `github_repository_query_phrase` | plugin hook development patterns GitHub repository examples |
| `release_notes_query_phrase` | plugin hook development patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
