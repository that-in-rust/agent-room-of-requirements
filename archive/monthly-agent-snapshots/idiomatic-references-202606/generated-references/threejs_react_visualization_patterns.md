# Threejs React Visualization Patterns

## Source Evidence Mapping Table

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202602/react-threejs-coder-01.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202604/react-threejs-coder-01/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202604/react-threejs-coder-01/references/force-graph-scene-checklist.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202604/react-threejs-coder-01/references/react-threejs-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom-ThreeJS-Visualization-Patterns.md | local_corpus_source_material | local_corpus_sourced_fact | historical idiomatic pattern corpus |
| https://react.dev/learn | external_research_source_material | external_research_sourced_fact | primary React learning and component model documentation |
| https://www.typescriptlang.org/docs/handbook/intro.html | external_research_source_material | external_research_sourced_fact | TypeScript language model for React applications |
| https://threejs.org/docs/ | external_research_source_material | external_research_sourced_fact | primary Three.js API documentation |
| https://react.dev/learn | external_research_source_material | external_research_sourced_fact | component-driven frontend behavior reference |
| https://threejs.org/docs/ | external_research_source_material | external_research_sourced_fact | visual scene API documentation |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | delivery verification and automation reference |

## Pattern Scoreboard Ranking Table

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `threejs_react_visualization_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local threejs react material before synthesizing visualization patterns recommendations. |
| `threejs_react_visualization_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `threejs_react_visualization_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `threejs_react_visualization_patterns` contains 5 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Threejs React Visualization Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202602/react-threejs-coder-01.md | React + Three.js + TypeScript Coder Agent | React + Three.js + TypeScript Coder Agent; Tech Stack; Project Structure; 4-Word Naming Convention (TypeScript Adaptation); Functions (camelCase, 4 words); Components (PascalCase, 3-4 words) | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202604/react-threejs-coder-01/SKILL.md | react-threejs-coder-01 | React Threejs Coder 01; Overview; Workflow; Default Rules; Reference Use; Output Contract | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202604/react-threejs-coder-01/references/force-graph-scene-checklist.md | Force Graph And Scene Checklist | Force Graph And Scene Checklist; Interaction; Data Volume; Rendering; Reliability | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202604/react-threejs-coder-01/references/react-threejs-patterns.md | React Three.js Patterns | React Three.js Patterns; Core Separation; Recommended Shape; Good Defaults; Anti-Patterns | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom-ThreeJS-Visualization-Patterns.md | Idiom-ThreeJS-Visualization-Patterns.md | Idiom-ThreeJS-Visualization-Patterns.md; Three.js Idiomatic Patterns Reference (LLM Context Anchor); Section 1: The Four-Word Naming Convention (Three.js Adaptation); 1.1 Scene Objects (PascalCase, 4 units); 1.2 Functions (camelCase, 4 words); 1.3 Animation/Update Functions | historical idiomatic pattern corpus |

## External Research Source Map

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://react.dev/learn | React documentation | primary React learning and component model documentation | external_research_sourced_fact |
| https://www.typescriptlang.org/docs/handbook/intro.html | TypeScript handbook | TypeScript language model for React applications | external_research_sourced_fact |
| https://threejs.org/docs/ | Three.js documentation | primary Three.js API documentation | external_research_sourced_fact |
| https://react.dev/learn | React documentation | component-driven frontend behavior reference | external_research_sourced_fact |
| https://threejs.org/docs/ | Three.js documentation | visual scene API documentation | external_research_sourced_fact |
| https://docs.github.com/actions | GitHub Actions documentation | delivery verification and automation reference | external_research_sourced_fact |

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

Role based opening scenario: The frontend product engineer is starting from a user workflow that must become a typed, accessible, resilient interface and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `threejs_react_visualization_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing component boundaries, state ownership, loading/error/empty states, and visual verification.
Reference opening trigger: Open this file when the task mentions threejs react visualization patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the threejs react visualization patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong threejs react visualization patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202602/react-threejs-coder-01.md | canonical primary source | React + Three.js + TypeScript Coder Agent; Tech Stack; Project Structure | What guidance, warning, or example should this source contribute to Threejs React Visualization Patterns? |
| agents-used-monthly-archive/codex-skills-202604/react-threejs-coder-01/SKILL.md | legacy historical source | React Threejs Coder 01; Overview; Workflow | What guidance, warning, or example should this source contribute to Threejs React Visualization Patterns? |
| agents-used-monthly-archive/codex-skills-202604/react-threejs-coder-01/references/force-graph-scene-checklist.md | supporting detail source | Force Graph And Scene Checklist; Interaction; Data Volume | What guidance, warning, or example should this source contribute to Threejs React Visualization Patterns? |
| agents-used-monthly-archive/codex-skills-202604/react-threejs-coder-01/references/react-threejs-patterns.md | supporting detail source | React Three.js Patterns; Core Separation; Recommended Shape | What guidance, warning, or example should this source contribute to Threejs React Visualization Patterns? |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom-ThreeJS-Visualization-Patterns.md | legacy historical source | Idiom-ThreeJS-Visualization-Patterns.md; Three.js Idiomatic Patterns Reference (LLM Context Anchor); Section 1: The Four-Word Naming Convention (Three.js Adaptation) | What guidance, warning, or example should this source contribute to Threejs React Visualization Patterns? |

## Theme Specific Artifact

Theme specific artifact: component ownership map with state, data boundary, render budget, and tests.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Threejs React Visualization Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

Good example: Use Threejs React Visualization Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Threejs React Visualization Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Threejs React Visualization Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

Leading indicator: primary workflow completion improves without introducing layout, accessibility, or state regressions.
Failure signal: the reference lists tools without describing the user workflow and failure states.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

- The role scenario names the user, starting state, decision, and trigger for Threejs React Visualization Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

Adjacent reference guidance: Use React, Three.js, or design references when the task is component logic, canvas behavior, or UI quality.
Adjacent reference 1: consider the threejs adjacent reference when the current task pivots away from threejs react visualization patterns.
Adjacent reference 2: consider the react adjacent reference when the current task pivots away from threejs react visualization patterns.
Adjacent reference 3: consider the visualization adjacent reference when the current task pivots away from threejs react visualization patterns.

## Workload Model

`combined_evidence_inference_note`: Treat Threejs React Visualization Patterns as a frontend experience operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | interface implementation, visual verification, accessibility review, and browser/runtime behavior checks where perceived reliability is user-visible | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one user flow, three viewport classes, one loading state, one error state, and one keyboard-only path | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include React + Three.js + TypeScript Coder Agent; Tech Stack; Project Structure; 4-Word Naming Convention (TypeScript Adaptation); Functions (camelCase, 4 wo | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is component ownership map with state, data boundary, render budget, and tests | require the artifact before claiming the reference is operationally usable |

## Reliability Target

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| viewport state breaks flow | layout, loading, or error state was not rendered across target viewports | capture screenshots and check text overlap, focus order, and interaction latency |
| client error lacks recovery | network, auth, or hydration failure leaves user stuck | add retry affordance, empty state, and instrumentation event |

## Retry Backpressure Guidance

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture viewport, browser, console error count, interaction latency, and screenshot evidence.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

Performance method: require interaction latency p95 under 100 ms for local UI actions and no layout overlap across mobile, tablet, and desktop screenshots.
Leading indicator to measure: primary workflow completion improves without introducing layout, accessibility, or state regressions.
Failure signal to watch: the reference lists tools without describing the user workflow and failure states.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

Threejs React Visualization Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | threejs react visualization patterns official documentation best practices |
| `github_repository_query_phrase` | threejs react visualization patterns GitHub repository examples |
| `release_notes_query_phrase` | threejs react visualization patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
