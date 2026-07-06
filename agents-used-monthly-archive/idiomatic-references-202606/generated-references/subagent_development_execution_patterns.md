# Subagent Development Execution Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/implementer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/spec-reviewer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/implementer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/spec-reviewer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary guidance for project instruction files and agent context loading |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | community format for predictable agent instructions |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | GitHub implementation and project-level agent guidance |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `subagent_development_execution_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local subagent development material before synthesizing execution patterns recommendations. |
| `subagent_development_execution_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `subagent_development_execution_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `subagent_development_execution_patterns` contains 8 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Subagent Development Execution Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/SKILL.md | subagent-driven-development | Subagent-Driven Development; When to Use; The Process; Prompt Templates; Example Workflow; Advantages | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | Code Quality Reviewer Prompt Template | Code Quality Reviewer Prompt Template | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/implementer-prompt.md | Implementer Subagent Prompt Template | Implementer Subagent Prompt Template; Task Description; Context; Before You Begin; Your Job; Before Reporting Back: Self-Review | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/spec-reviewer-prompt.md | Spec Compliance Reviewer Prompt Template | Spec Compliance Reviewer Prompt Template; What Was Requested; What Implementer Claims They Built; CRITICAL: Do Not Trust the Report; Your Job | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/SKILL.md | subagent-driven-development | Subagent-Driven Development; When to Use; The Process; Prompt Templates; Example Workflow; Advantages | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | Code Quality Reviewer Prompt Template | Code Quality Reviewer Prompt Template | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/implementer-prompt.md | Implementer Subagent Prompt Template | Implementer Subagent Prompt Template; Task Description; Context; Before You Begin; Your Job; Before Reporting Back: Self-Review | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/spec-reviewer-prompt.md | Spec Compliance Reviewer Prompt Template | Spec Compliance Reviewer Prompt Template; What Was Requested; What Implementer Claims They Built; CRITICAL: Do Not Trust the Report; Your Job | local agent-usable source material |

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

## User Journey Scenario

Role based opening scenario: The agent-system designer is starting from a task that needs context selection, tool use, delegation, and verification and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `subagent_development_execution_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what context to load, what to offload, when to delegate, and how to prove completion.
Reference opening trigger: Open this file when the task mentions subagent development execution patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the subagent development execution patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong subagent development execution patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/SKILL.md | canonical primary source | Subagent-Driven Development; When to Use; The Process | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | legacy historical source | Code Quality Reviewer Prompt Template | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/implementer-prompt.md | legacy historical source | Implementer Subagent Prompt Template; Task Description; Context | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/spec-reviewer-prompt.md | legacy historical source | Spec Compliance Reviewer Prompt Template; What Was Requested; What Implementer Claims They Built | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| claude-skills/superpowers/subagent-driven-development/SKILL.md | supporting context source | Subagent-Driven Development; When to Use; The Process | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| claude-skills/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | supporting context source | Code Quality Reviewer Prompt Template | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| claude-skills/superpowers/subagent-driven-development/implementer-prompt.md | supporting context source | Implementer Subagent Prompt Template; Task Description; Context | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| claude-skills/superpowers/subagent-driven-development/spec-reviewer-prompt.md | supporting context source | Spec Compliance Reviewer Prompt Template; What Was Requested; What Implementer Claims They Built | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |

## Theme Specific Artifact

Theme specific artifact: worked subagent development execution patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Subagent Development Execution Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

Good example: Use Subagent Development Execution Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Subagent Development Execution Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Subagent Development Execution Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

Leading indicator: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal: the reference tells agents what to do without defining context budget or escalation rules.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

- The role scenario names the user, starting state, decision, and trigger for Subagent Development Execution Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

Adjacent reference guidance: Use debate, subagent, context, or verification references when the task narrows to a specific agent behavior.
Adjacent reference 1: consider the subagent adjacent reference when the current task pivots away from subagent development execution patterns.
Adjacent reference 2: consider the development adjacent reference when the current task pivots away from subagent development execution patterns.
Adjacent reference 3: consider the execution adjacent reference when the current task pivots away from subagent development execution patterns.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | subagent development execution patterns official documentation best practices |
| `github_repository_query_phrase` | subagent development execution patterns GitHub repository examples |
| `release_notes_query_phrase` | subagent development execution patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
