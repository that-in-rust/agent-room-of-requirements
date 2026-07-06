# Python Reference Routing Sources

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/reference-map.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/sources-and-research-brief.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://docs.python.org/3/library/typing.html | external_research_source_material | external_research_sourced_fact | primary typing module documentation |
| https://docs.pytest.org/en/stable/ | external_research_source_material | external_research_sourced_fact | primary Python testing framework documentation |
| https://mypy.readthedocs.io/ | external_research_source_material | external_research_sourced_fact | static type checking documentation and constraints |
| https://docs.astral.sh/ruff/ | external_research_source_material | external_research_sourced_fact | linting and formatting tool documentation |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `python_reference_routing_sources` | 95 | default_adoption_pattern_tier | Source Map First: Load local python reference material before synthesizing routing sources recommendations. |
| `python_reference_routing_sources` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `python_reference_routing_sources` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `python_reference_routing_sources` contains 2 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Python Reference Routing Sources comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/reference-map.md | Reference Map | Reference Map; Jump Points; Section Search; Use Order | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/sources-and-research-brief.md | Sources And Research Brief | Sources And Research Brief; Primary Sources; Repo-Local Sources; Synthesis Notes | skill entrypoint or reusable agent prompt |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://docs.python.org/3/library/typing.html | Python typing docs | primary typing module documentation | external_research_sourced_fact |
| https://docs.pytest.org/en/stable/ | pytest documentation | primary Python testing framework documentation | external_research_sourced_fact |
| https://mypy.readthedocs.io/ | mypy documentation | static type checking documentation and constraints | external_research_sourced_fact |
| https://docs.astral.sh/ruff/ | Ruff documentation | linting and formatting tool documentation | external_research_sourced_fact |

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

Role based opening scenario: The Python maintainer is starting from scripts or services that need typing, fixtures, packaging, and lint discipline and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `python_reference_routing_sources` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing how strict to make typing, tests, validation, and dependency hygiene for the current risk level.
Reference opening trigger: Open this file when the task mentions python reference routing sources, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the python reference routing sources pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong python reference routing sources guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/reference-map.md | canonical primary source | Reference Map; Jump Points; Section Search | What guidance, warning, or example should this source contribute to Python Reference Routing Sources? |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/sources-and-research-brief.md | supporting detail source | Sources And Research Brief; Primary Sources; Repo-Local Sources | What guidance, warning, or example should this source contribute to Python Reference Routing Sources? |

## Theme Specific Artifact

Theme specific artifact: canonical source routing rules for stale, duplicate, and conflicting sources.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Python Reference Routing Sources | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

Good example: Use Python Reference Routing Sources after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Python Reference Routing Sources as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Python Reference Routing Sources only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

Leading indicator: the next agent can modify the package without weakening type, lint, or fixture coverage.
Failure signal: the reference says quality matters but gives no migration path from loose scripts to strict package code.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

- The role scenario names the user, starting state, decision, and trigger for Python Reference Routing Sources.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

Adjacent reference guidance: Use reliability, routing, or quality references when the problem is governance rather than syntax.
Adjacent reference 1: consider the python adjacent reference when the current task pivots away from python reference routing sources.
Adjacent reference 2: consider the reference adjacent reference when the current task pivots away from python reference routing sources.
Adjacent reference 3: consider the routing adjacent reference when the current task pivots away from python reference routing sources.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | python reference routing sources official documentation best practices |
| `github_repository_query_phrase` | python reference routing sources GitHub repository examples |
| `release_notes_query_phrase` | python reference routing sources changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
