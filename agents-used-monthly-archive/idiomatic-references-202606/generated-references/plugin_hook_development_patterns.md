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

## User Journey Scenario

Role based opening scenario: The agent-tool platform builder is starting from a capability request that could become a command, hook, plugin, MCP server, or setting and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `plugin_hook_development_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the right extension surface and proving install, invocation, permissions, and recovery behavior.
Reference opening trigger: Open this file when the task mentions plugin hook development patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the plugin hook development patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong plugin hook development patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/hookify/SKILL.md | canonical primary source | Writing Hookify Rules; Overview; Rule File Format | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/SKILL.md | legacy historical source | Hook Development for Claude Code Plugins; Overview; Hook Types | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/advanced.md | supporting detail source | Advanced Hook Use Cases; Multi-Stage Validation; !/bin/bash | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/migration.md | supporting detail source | Migrating from Basic to Advanced Hooks; Why Migrate?; Migration Example: Bash Command Validation | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/patterns.md | supporting detail source | Common Hook Patterns; Pattern 1: Security Validation; Pattern 2: Test Enforcement | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| claude-skills/plugins/hookify/SKILL.md | supporting context source | Writing Hookify Rules; Overview; Rule File Format | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| claude-skills/plugins/plugin-dev/hook-development/SKILL.md | supporting context source | Hook Development for Claude Code Plugins; Overview; Hook Types | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| claude-skills/plugins/plugin-dev/hook-development/references/advanced.md | supporting detail source | Advanced Hook Use Cases; Multi-Stage Validation; !/bin/bash | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| claude-skills/plugins/plugin-dev/hook-development/references/migration.md | supporting detail source | Migrating from Basic to Advanced Hooks; Why Migrate?; Migration Example: Bash Command Validation | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| claude-skills/plugins/plugin-dev/hook-development/references/patterns.md | supporting detail source | Common Hook Patterns; Pattern 1: Security Validation; Pattern 2: Test Enforcement | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |

## Theme Specific Artifact

Theme specific artifact: hook lifecycle map with bypass policy, safety constraints, and debug workflow.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Plugin Hook Development Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

Good example: Use Plugin Hook Development Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Plugin Hook Development Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Plugin Hook Development Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

Leading indicator: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal: the reference confuses adjacent extension types or omits failure recovery.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

- The role scenario names the user, starting state, decision, and trigger for Plugin Hook Development Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

Adjacent reference guidance: Use command, hook, MCP, settings, or manifest references when one extension surface is already selected.
Adjacent reference 1: consider the plugin adjacent reference when the current task pivots away from plugin hook development patterns.
Adjacent reference 2: consider the hook adjacent reference when the current task pivots away from plugin hook development patterns.
Adjacent reference 3: consider the development adjacent reference when the current task pivots away from plugin hook development patterns.

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
