# Claude Code Setup Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/hooks-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/mcp-servers.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/plugins-reference.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/skills-reference.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/subagent-templates.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/claude-code-setup/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/claude-code-setup/references/hooks-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/claude-code-setup/references/mcp-servers.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/claude-code-setup/references/plugins-reference.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/claude-code-setup/references/skills-reference.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/claude-code-setup/references/subagent-templates.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://github.com/davepoon/buildwithclaude | external_research_source_material | external_research_sourced_fact | GitHub collection of Claude skills, agents, commands, hooks, and plugins |
| https://github.com/Cranot/claude-code-guide | external_research_source_material | external_research_sourced_fact | community-maintained guide for Claude Code skills, hooks, plugins, and MCP |
| https://www.claudedirectory.org/blog/claude-code-skills-vs-subagents-vs-mcp | external_research_source_material | external_research_sourced_fact | current public taxonomy for Claude Code extension surfaces |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `claude_code_setup_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local claude code material before synthesizing setup patterns recommendations. |
| `claude_code_setup_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `claude_code_setup_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `claude_code_setup_patterns` contains 12 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Claude Code Setup Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/SKILL.md | claude-automation-recommender | Claude Automation Recommender; Output Guidelines; Automation Types Overview; Workflow; Phase 1: Codebase Analysis; Detect project type and tools | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/hooks-patterns.md | Hooks Recommendations | Hooks Recommendations; Auto-Formatting Hooks; Prettier (JavaScript/TypeScript); ESLint (JavaScript/TypeScript); Black/isort (Python); Ruff (Python - Modern) | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/mcp-servers.md | MCP Server Recommendations | MCP Server Recommendations; Setup & Team Sharing; Documentation & Knowledge; context7; Browser & Frontend; Playwright MCP | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/plugins-reference.md | Plugin Recommendations | Plugin Recommendations; Official Plugins; Development & Code Quality; Git & Workflow; Frontend; Learning & Guidance | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/skills-reference.md | Skills Recommendations | Skills Recommendations; Available from Official Plugins; Plugin Development (plugin-dev); Git Workflows (commit-commands); Frontend (frontend-design); Automation Rules (hookify) | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/subagent-templates.md | Subagent Recommendations | Subagent Recommendations; Code Review Agents; code-reviewer; security-reviewer; test-writer; Specialized Agents | reference detail file for deeper pattern evidence |
| claude-skills/plugins/claude-code-setup/SKILL.md | claude-automation-recommender | Claude Automation Recommender; Output Guidelines; Automation Types Overview; Workflow; Phase 1: Codebase Analysis; Detect project type and tools | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/claude-code-setup/references/hooks-patterns.md | Hooks Recommendations | Hooks Recommendations; Auto-Formatting Hooks; Prettier (JavaScript/TypeScript); ESLint (JavaScript/TypeScript); Black/isort (Python); Ruff (Python - Modern) | reference detail file for deeper pattern evidence |
| claude-skills/plugins/claude-code-setup/references/mcp-servers.md | MCP Server Recommendations | MCP Server Recommendations; Setup & Team Sharing; Documentation & Knowledge; context7; Browser & Frontend; Playwright MCP | reference detail file for deeper pattern evidence |
| claude-skills/plugins/claude-code-setup/references/plugins-reference.md | Plugin Recommendations | Plugin Recommendations; Official Plugins; Development & Code Quality; Git & Workflow; Frontend; Learning & Guidance | reference detail file for deeper pattern evidence |
| claude-skills/plugins/claude-code-setup/references/skills-reference.md | Skills Recommendations | Skills Recommendations; Available from Official Plugins; Plugin Development (plugin-dev); Git Workflows (commit-commands); Frontend (frontend-design); Automation Rules (hookify) | reference detail file for deeper pattern evidence |
| claude-skills/plugins/claude-code-setup/references/subagent-templates.md | Subagent Recommendations | Subagent Recommendations; Code Review Agents; code-reviewer; security-reviewer; test-writer; Specialized Agents | reference detail file for deeper pattern evidence |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://github.com/davepoon/buildwithclaude | Build with Claude collection | GitHub collection of Claude skills, agents, commands, hooks, and plugins | external_research_sourced_fact |
| https://github.com/Cranot/claude-code-guide | Claude Code guide collection | community-maintained guide for Claude Code skills, hooks, plugins, and MCP | external_research_sourced_fact |
| https://www.claudedirectory.org/blog/claude-code-skills-vs-subagents-vs-mcp | Claude concept comparison | current public taxonomy for Claude Code extension surfaces | external_research_sourced_fact |

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
| `official_docs_query_phrase` | claude code setup patterns official documentation best practices |
| `github_repository_query_phrase` | claude code setup patterns GitHub repository examples |
| `release_notes_query_phrase` | claude code setup patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
