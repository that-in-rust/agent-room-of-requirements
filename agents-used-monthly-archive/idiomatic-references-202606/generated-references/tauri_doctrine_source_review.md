# Tauri Doctrine Source Review

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/tauri-executable-specs-01/references/tauri-doctrine.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://v2.tauri.app/ | external_research_source_material | external_research_sourced_fact | primary Tauri 2 application and security documentation |
| https://github.com/tauri-apps/tauri | external_research_source_material | external_research_sourced_fact | desktop runtime implementation and release surface |
| https://github.com/rust-lang/api-guidelines | external_research_source_material | external_research_sourced_fact | Rust-facing API and error design reference |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | primary automation and CI/CD workflow documentation |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | external_research_source_material | external_research_sourced_fact | primary guidance for reusable workflow composition |
| https://github.com/openai/codex/blob/-/AGENTS.md | external_research_source_material | external_research_sourced_fact | agent project instructions and testing guidance in a real repository |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `tauri_doctrine_source_review` | 95 | default_adoption_pattern_tier | Source Map First: Load local tauri doctrine material before synthesizing source review recommendations. |
| `tauri_doctrine_source_review` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `tauri_doctrine_source_review` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `tauri_doctrine_source_review` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Tauri Doctrine Source Review comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/tauri-executable-specs-01/references/tauri-doctrine.md | Tauri Doctrine | Tauri Doctrine; Premise Check; Source Base; Selection Rubric; Coverage Verdict; Chosen Patterns | reference detail file for deeper pattern evidence |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://v2.tauri.app/ | Tauri documentation | primary Tauri 2 application and security documentation | external_research_sourced_fact |
| https://github.com/tauri-apps/tauri | Tauri repository | desktop runtime implementation and release surface | external_research_sourced_fact |
| https://github.com/rust-lang/api-guidelines | Rust API Guidelines | Rust-facing API and error design reference | external_research_sourced_fact |
| https://docs.github.com/actions | GitHub Actions documentation | primary automation and CI/CD workflow documentation | external_research_sourced_fact |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | Reusable workflow docs | primary guidance for reusable workflow composition | external_research_sourced_fact |
| https://github.com/openai/codex/blob/-/AGENTS.md | OpenAI Codex repository AGENTS | agent project instructions and testing guidance in a real repository | external_research_sourced_fact |

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

Role based opening scenario: The Tauri desktop app team is starting from a frontend action that must cross into Rust commands and platform permissions and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `tauri_doctrine_source_review` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the safest command, permission, IPC, packaging, and verification boundary.
Reference opening trigger: Open this file when the task mentions tauri doctrine source review, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the tauri doctrine source review pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong tauri doctrine source review guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/tauri-executable-specs-01/references/tauri-doctrine.md | canonical primary source | Tauri Doctrine; Premise Check; Source Base | What guidance, warning, or example should this source contribute to Tauri Doctrine Source Review? |

## Theme Specific Artifact

Theme specific artifact: worked tauri doctrine source review example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Tauri Doctrine Source Review | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

Good example: Use Tauri Doctrine Source Review after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Tauri Doctrine Source Review as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Tauri Doctrine Source Review only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

Leading indicator: the feature can be tested across frontend, Rust command, and packaged desktop behavior.
Failure signal: the reference ignores permissions, IPC risk, or platform-specific verification.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

- The role scenario names the user, starting state, decision, and trigger for Tauri Doctrine Source Review.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

Adjacent reference guidance: Use executable, doctrine, or legacy Tauri references when the task is about specs, policy, or migration.
Adjacent reference 1: consider the tauri adjacent reference when the current task pivots away from tauri doctrine source review.
Adjacent reference 2: consider the doctrine adjacent reference when the current task pivots away from tauri doctrine source review.
Adjacent reference 3: consider the source adjacent reference when the current task pivots away from tauri doctrine source review.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | tauri doctrine source review official documentation best practices |
| `github_repository_query_phrase` | tauri doctrine source review GitHub repository examples |
| `release_notes_query_phrase` | tauri doctrine source review changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
