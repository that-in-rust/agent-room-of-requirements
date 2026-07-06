# Plugin Mcp Integration Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/authentication.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/server-types.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/tool-usage.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/mcp-integration/references/authentication.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/references/server-types.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/references/tool-usage.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | external_research_source_material | external_research_sourced_fact | primary MCP resource model for context sharing |
| https://github.com/modelcontextprotocol/servers | external_research_source_material | external_research_sourced_fact | reference and community server implementation index |
| https://github.com/github/github-mcp-server | external_research_source_material | external_research_sourced_fact | GitHub-backed MCP server for repository and issue operations |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | external_research_source_material | external_research_sourced_fact | primary resource-sharing model |
| https://github.com/modelcontextprotocol/servers | external_research_source_material | external_research_sourced_fact | reference server implementation collection |
| https://github.com/github/github-mcp-server | external_research_source_material | external_research_sourced_fact | GitHub platform MCP implementation |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `plugin_mcp_integration_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local plugin mcp material before synthesizing integration patterns recommendations. |
| `plugin_mcp_integration_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `plugin_mcp_integration_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `plugin_mcp_integration_patterns` contains 8 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Plugin Mcp Integration Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/SKILL.md | mcp-integration | MCP Integration for Claude Code Plugins; Overview; MCP Server Configuration Methods; Method 1: Dedicated .mcp.json (Recommended); Method 2: Inline in plugin.json; MCP Server Types | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/authentication.md | MCP Authentication Patterns | MCP Authentication Patterns; Overview; OAuth (Automatic); How It Works; Configuration; Supported Services | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/server-types.md | MCP Server Types: Deep Dive | MCP Server Types: Deep Dive; stdio (Standard Input/Output); Overview; Configuration; Process Lifecycle; Use Cases | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/tool-usage.md | Using MCP Tools in Commands and Agents | Using MCP Tools in Commands and Agents; Overview; Tool Naming Convention; Format; Examples; Discovering Tool Names | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/SKILL.md | mcp-integration | MCP Integration for Claude Code Plugins; Overview; MCP Server Configuration Methods; Method 1: Dedicated .mcp.json (Recommended); Method 2: Inline in plugin.json; MCP Server Types | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/mcp-integration/references/authentication.md | MCP Authentication Patterns | MCP Authentication Patterns; Overview; OAuth (Automatic); How It Works; Configuration; Supported Services | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/references/server-types.md | MCP Server Types: Deep Dive | MCP Server Types: Deep Dive; stdio (Standard Input/Output); Overview; Configuration; Process Lifecycle; Use Cases | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/references/tool-usage.md | Using MCP Tools in Commands and Agents | Using MCP Tools in Commands and Agents; Overview; Tool Naming Convention; Format; Examples; Discovering Tool Names | reference detail file for deeper pattern evidence |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | Model Context Protocol resources | primary MCP resource model for context sharing | external_research_sourced_fact |
| https://github.com/modelcontextprotocol/servers | MCP server implementations | reference and community server implementation index | external_research_sourced_fact |
| https://github.com/github/github-mcp-server | GitHub MCP server | GitHub-backed MCP server for repository and issue operations | external_research_sourced_fact |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | Model Context Protocol resources | primary resource-sharing model | external_research_sourced_fact |
| https://github.com/modelcontextprotocol/servers | MCP server implementations | reference server implementation collection | external_research_sourced_fact |
| https://github.com/github/github-mcp-server | GitHub MCP server | GitHub platform MCP implementation | external_research_sourced_fact |

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
| `official_docs_query_phrase` | plugin mcp integration patterns official documentation best practices |
| `github_repository_query_phrase` | plugin mcp integration patterns GitHub repository examples |
| `release_notes_query_phrase` | plugin mcp integration patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
