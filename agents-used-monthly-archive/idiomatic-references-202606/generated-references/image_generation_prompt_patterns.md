# Image Generation Prompt Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/cli.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/codex-network.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/image-api.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/prompting.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/sample-prompts.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://platform.openai.com/docs/guides/images | external_research_source_material | external_research_sourced_fact | primary image generation API documentation |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | agent runtime and CLI reference point |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `image_generation_prompt_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local image generation material before synthesizing prompt patterns recommendations. |
| `image_generation_prompt_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `image_generation_prompt_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `image_generation_prompt_patterns` contains 6 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Image Generation Prompt Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/SKILL.md | "imagegen" | Image Generation Skill; Top-level modes and rules; When to use; When not to use; Decision tree; Workflow | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/cli.md | CLI reference ('scripts/image_gen.py') | CLI reference ('scripts/image_gen.py'); What this CLI does; Quick start (works from any repo); Quick start; Guardrails; Defaults | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/codex-network.md | Codex network approvals / sandbox notes | Codex network approvals / sandbox notes; Why am I asked to approve image generation calls?; Important note about approvals vs network; How do I reduce repeated approval prompts?; Safety note | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/image-api.md | Image API quick reference | Image API quick reference; Scope; Endpoints; Core parameters for GPT Image models; Edit-specific parameters; Output | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/prompting.md | Prompting best practices | Prompting best practices; Contents; Structure; Specificity policy; Allowed and disallowed augmentation; Composition and layout | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/sample-prompts.md | Sample prompts (copy/paste) | Sample prompts (copy/paste); Generate; photorealistic-natural; product-mockup; ui-mockup; infographic-diagram | reference detail file for deeper pattern evidence |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://platform.openai.com/docs/guides/images | OpenAI image generation guide | primary image generation API documentation | external_research_sourced_fact |
| https://github.com/openai/codex | OpenAI Codex repository | agent runtime and CLI reference point | external_research_sourced_fact |

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

Role based opening scenario: The creative tool builder or artifact creator is starting from vague creative intent that needs constraints, iteration, and quality review and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `image_generation_prompt_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the prompt, controls, taste rubric, regeneration trigger, and final acceptance bar.
Reference opening trigger: Open this file when the task mentions image generation prompt patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the image generation prompt patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong image generation prompt patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/SKILL.md | canonical primary source | Image Generation Skill; Top-level modes and rules; When to use | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/cli.md | supporting detail source | CLI reference ('scripts/image_gen.py'); What this CLI does; Quick start (works from any repo) | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/codex-network.md | supporting detail source | Codex network approvals / sandbox notes; Why am I asked to approve image generation calls?; Important note about approvals vs network | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/image-api.md | supporting detail source | Image API quick reference; Scope; Endpoints | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/prompting.md | supporting detail source | Prompting best practices; Contents; Structure | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/sample-prompts.md | supporting detail source | Sample prompts (copy/paste); Generate; photorealistic-natural | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |

## Theme Specific Artifact

Theme specific artifact: prompt contract with bad-prompt rewrite and evaluation criteria.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Image Generation Prompt Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

Good example: Use Image Generation Prompt Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Image Generation Prompt Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Image Generation Prompt Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

Leading indicator: iteration improves the artifact against named taste criteria rather than random novelty.
Failure signal: the reference celebrates creativity without defining what good output looks like.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

- The role scenario names the user, starting state, decision, and trigger for Image Generation Prompt Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

Adjacent reference guidance: Use image, art, playground, or timeline references when the artifact type is specific.
Adjacent reference 1: consider the image adjacent reference when the current task pivots away from image generation prompt patterns.
Adjacent reference 2: consider the generation adjacent reference when the current task pivots away from image generation prompt patterns.
Adjacent reference 3: consider the prompt adjacent reference when the current task pivots away from image generation prompt patterns.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | image generation prompt patterns official documentation best practices |
| `github_repository_query_phrase` | image generation prompt patterns GitHub repository examples |
| `release_notes_query_phrase` | image generation prompt patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
