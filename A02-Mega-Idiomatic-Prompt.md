# A02 Mega Idiomatic Pattern Prompt

## Purpose

This file is a reusable mega-prompt for discovering, scoring, and packaging
idiomatic engineering patterns for any technology, framework, runtime, or
agent surface.

## Product Intent

A02 is not a tutorial generator. It is a product-quality research brief builder
for agents and humans who need to move from "what is idiomatic here?" to
"what defaults should we actually use?" without drowning in scattered advice.

From a Shreyas-style product lens, the prompt should make the user's next
decision easier in the first thirty seconds:

- target surface decision clarity
- evidence quality ranking clarity
- default pattern adoption clarity
- risk avoidance boundary clarity
- output artifact delivery clarity

The core job is to convert broad technology research into a usable operating
system: modes, parameters, evidence, defaults, anti-patterns, verification
gates, and skill packaging.

## User Journey

A reader should be able to skim this file and immediately see dense,
retrieval-friendly handles instead of vague buckets. The previous failure mode
was a visually neat list with weak terms like "sandboxing", "metrics", or
"tracing". This version forces every reusable concept label to carry enough
semantic context to help both a human reviewer and an LLM retrieve the right
pattern later.

The desired journey is:

1. A human picks the target technology and delivery surface.
2. An agent reads source material in bounded chunks and builds an evidence
   ledger.
3. The agent scores idioms by prevention power, ecosystem fit, and verifiable
   reliability.
4. The final artifact becomes either a pattern guide, a review checklist, or a
   reusable agent skill.

## Repo Scan Basis

It was enriched from a repo-wide scan of this repository on 2026-07-06:

- Files scanned outside `.git`: `528`
- Text files read in 100-line chunks: `518`
- 100-line chunks processed: `1809`
- Binary files detected separately: `.DS_Store` files and PNG assets
- Empty files observed: this file before enrichment, two `__init__.py` files, and one empty archived note

The strongest recurring parameters across the repo were:

1. agent context prompt structure
2. identity scope mode triggers
3. executable requirement spec contracts
4. output contract artifact formats
5. idiom type domain modeling
6. testing verification quality gates
7. reliability failure anti patterns
8. research provenance source quality
9. architecture boundary dependency direction
10. operations runtime security resilience

Use the copyable prompt below when asking an internet-capable model to discover
idiomatic patterns for a new technology.

## Required A02 Shape

This document intentionally contains these major surfaces:

1. `purpose_document_usage_scope`: Purpose
2. `product_intent_decision_context`: Product Intent
3. `user_journey_scan_path`: User Journey
4. `repo_scan_evidence_basis`: Repo Scan Basis
5. `copyable_prompt_delivery_artifact`: Copyable Mega Prompt
6. `four_word_parameter_rule`: Four-Word Parameter Rule
7. `primary_objective_parameter_set`: Primary Objective Parameters
8. `parameter_ledger_evidence_record`: Parameter Ledger
9. `research_corpus_source_parameters`: Research Corpus Parameters
10. `work_surface_mode_set`: Work Surface Modes
11. `pattern_taxonomy_mining_dimensions`: Pattern Taxonomy
12. `scoring_rubric_pattern_ranker`: Scoring Rubric
13. `anti_pattern_mining_registry`: Anti-Pattern Mining
14. `output_contract_artifact_order`: Output Contract
15. `agent_skill_skeleton_template`: Agent Skill Skeleton
16. `human_scan_acceptance_test`: Human Scan Acceptance Test

---

## Copyable Mega Prompt

````markdown
# Mega Idiomatic Pattern Mining Prompt

## Role

Act as a rigorous idiomatic-pattern researcher, language/runtime specialist,
production reliability reviewer, and agent-skill designer.

Your job is to discover the most useful idiomatic patterns for the requested
technology and package them into a reusable guide that another agent can use to
plan, implement, review, and verify work in that technology.

Do not produce a generic tutorial. Produce a pattern library and operating
prompt that helps an agent write code, docs, or systems in the style that the
ecosystem itself rewards.

## Product Intent

This prompt is a decision product, not a content dump. Its job is to help a
user or agent convert scattered ecosystem knowledge into reliable defaults:
which patterns to adopt, which traps to avoid, which source claims to trust,
and which verification gates prove the advice.

Optimize for these product outcomes:

- `surface_diagnosis_before_research`: classify the work surface before naming patterns.
- `evidence_ledger_before_synthesis`: preserve source trail before drawing conclusions.
- `default_decisions_before_options`: recommend usable defaults before listing variations.
- `failure_prevention_before_cleverness`: prefer boring patterns that remove bug classes.
- `agent_packaging_before_finish`: make the output reusable by another coding agent.

## User Journey

The expected user is trying to start work in a technology and wants the
practical idioms an expert would apply automatically. They should not have to
decode one-word buckets, vague advice, or generic "best practices".

Design the answer so the reader can:

1. Recognize the target surface and assumptions immediately.
2. Inspect source strength without hunting through prose.
3. See pattern names that are specific enough to retrieve later.
4. Apply defaults before reading every caveat.
5. Turn the result into a skill, checklist, or implementation prompt.

## Primary Objective Parameters

Find the most idiomatic, reliable, evidence-backed patterns for:

- `target_technology_language_name`: <TECHNOLOGY>
- `ecosystem_platform_scope_context`: <ECOSYSTEM_OR_PLATFORM>
- `runtime_execution_host_environment`: <RUNTIME_OR_HOST>
- `framework_library_stack_names`: <FRAMEWORKS_OR_LIBRARIES>
- `artifact_delivery_surface_type`: choose one or more:
  - `library_api_design_surface`
  - `command_line_interface_surface`
  - `backend_service_delivery_surface`
  - `frontend_interface_delivery_surface`
  - `desktop_mobile_host_surface`
  - `plugin_extension_lifecycle_surface`
  - `agent_skill_packaging_surface`
  - `data_pipeline_processing_surface`
  - `infrastructure_delivery_operations_surface`
  - `documentation_guide_delivery_surface`
- `quality_priority_goal_focus`: choose one or more:
  - `reliability_failure_prevention_focus`
  - `performance_latency_efficiency_focus`
  - `security_threat_control_focus`
  - `maintainability_change_survival_focus`
  - `ergonomics_developer_experience_focus`
  - `production_readiness_operational_focus`
  - `learning_guide_onboarding_focus`
- `audience_consumer_usage_context`: choose one or more:
  - `llm_agent_usage_context`
  - `human_engineer_usage_context`
  - `team_onboarding_usage_context`
  - `reviewer_risk_analysis_context`
  - `architect_decision_design_context`
- `freshness_version_date_window`: <TODAY_OR_TARGET_DATE>

## Four-Word Parameter Rule

Every reusable concept label must use exactly four semantic words.

A reusable concept label is any phrase that names a parameter, field, table
column, taxonomy bullet, source class, work mode, pattern family, scoring
factor, anti-pattern, verification gate, output artifact, checklist item, skill
packaging field, search query label, architecture boundary, risk category, or
context-loading category.

The rule applies whether the label appears in snake_case, prose bullets,
backticks, tables, YAML, skill skeletons, output contracts, or checklist items.

Use this snake_case pattern for machine keys:

```text
scope_constraint_target_qualifier
```

Examples:

- `target_technology_language_name`
- `quality_priority_goal_focus`
- `source_authority_confidence_level`
- `pattern_failure_prevention_power`

Use the same four-word density for prose labels:

```text
sandbox isolation runtime constraints
metrics signal collection strategy
tracing span correlation model
rollback recovery decision path
```

Avoid single-word or two-word labels such as technology, runtime, audience,
source, verification, sandboxing, metrics, tracing, rollback, migrations, tests,
security, or quality gates. The goal is not ritual. The goal is retrieval
density: every reusable label should tell the model what kind of information
belongs there and why it matters.

Example:

```text
target_technology_language_name: Rust
ecosystem_platform_scope_context: async backend services
runtime_execution_host_environment: Tokio on Linux containers
framework_library_stack_names: Axum, SQLx, Tower
artifact_delivery_surface_type: backend_service_delivery_surface
quality_priority_goal_focus: reliability_failure_prevention_focus
audience_consumer_usage_context: llm_agent_usage_context
freshness_version_date_window: 2026-07-06
```

## What The Rule Does Not Mean

The rule does not force ordinary prose, file paths, commands, quoted source
text, technology names, version numbers, or grammatical connector words into a
four-word shape. It applies to reusable labels that structure future reasoning.

Section headings may stay readable, but if a heading names an output artifact,
work mode, taxonomy bucket, source class, risk category, verification gate, or
skill field, give it a four-word handle.

## Taste Rule

Prefer a slightly longer label that reveals intent over an elegant short label
that hides the job. A good label should answer three questions at a glance:
what surface is this about, what boundary or constraint matters, and what kind
of decision will it support?

## Explicit Bad Labels To Remove

Replace vague labels with dense four-word labels:

| rejected_label_example_text | required_four_word_replacement |
| --- | --- |
| `sandboxing` | `sandbox_isolation_runtime_constraints` |
| `metrics` | `metrics_signal_collection_strategy` |
| `tracing` | `tracing_span_correlation_model` |
| `rollback` | `rollback_recovery_decision_path` |
| `migrations` | `migration_rollout_sequencing_plan` |
| `unit tests` | `unit_test_boundary_scope` |
| `security` | `security_threat_control_model` |
| `quality gates` | `quality_gate_verification_commands` |
| `open questions` | `open_question_decision_drivers` |
| `reference maps` | `reference_map_routing_files` |
| `output contracts` | `output_contract_section_order` |
| `mode selection` | `mode_selection_surface_rules` |
| `source briefs` | `source_brief_provenance_summary` |
| `context strategy` | `context_strategy_loading_order` |

## Non-Negotiable Output Thesis

The final result must answer this:

> "What patterns make correct, idiomatic work the easiest path and make common
> mistakes hard to express?"

Prefer patterns that:

- `prevent_bug_class_failures`: remove a repeatable failure category.
- `increase_misuse_resistance_strength`: make incorrect use harder to express.
- `improve_diagnostic_feedback_quality`: make failures easier to understand.
- `match_official_ecosystem_guidance`: align with primary docs or maintainer guidance.
- `appear_in_production_code`: show up in serious maintained systems.
- `survive_operational_failure_conditions`: handle malformed input, version drift,
  concurrency, cancellation, partial failure, and maintenance.
- `support_verification_gate_evidence`: connect to tests, tools, or measurable gates.

Reject patterns that are merely fashionable, clever, aesthetic, or copied from
one unrepresentative codebase.

---

## Parameter Ledger

Maintain a parameter ledger while researching. Update it after every source and
after every 100-line chunk of long sources.

Use this record shape:

```yaml
evidence_source_identifier_key:
source_location_url_path:
source_category_artifact_type: <source_category_artifact_type>
source_authority_confidence_level: <source_authority_confidence_level>
freshness_version_date_window:
technology_version_target_range:
chunk_line_range_pointer:
observed_terms_keyword_signals:
idiom_candidate_pattern_names:
anti_pattern_failure_modes:
reliability_claims_failure_boundaries:
architecture_claims_boundary_design:
testing_claims_verification_gates:
tooling_claims_quality_commands:
security_claims_threat_controls:
operations_claims_runtime_behaviors:
evidence_strength_confidence_score: 1-5
notes_open_questions_context:
```

Use these source category handles:

- `official_docs_reference_source`
- `style_guide_convention_source`
- `reference_repo_example_source`
- `release_notes_migration_source`
- `issue_discussion_context_source`
- `security_advisory_threat_source`
- `benchmark_measurement_evidence_source`
- `tutorial_explanation_context_source`
- `book_reference_learning_source`
- `agent_skill_prompt_source`
- `local_file_repository_source`

Use these authority confidence handles:

- `primary_official_source_level`
- `secondary_interpretive_source_level`
- `community_discussion_source_level`
- `local_inference_source_level`

Do not wait until the end to summarize. Build the ledger incrementally so no
source can quietly disappear from the synthesis.

---

## Research Corpus Parameters

Search broadly, then rank sources. Prefer primary sources first.

### Required Source Classes

For the requested technology, look for:

1. official language reference documentation
2. official style convention guides
3. official framework API documentation
4. release note migration guides
5. maintainer reference implementation examples
6. production repository usage examples
7. security advisory vulnerability guidance
8. testing framework documentation guides
9. packaging build deployment documentation
10. performance profiling optimization documentation
11. concurrency async runtime documentation
12. community idiom discussion signals

### Source Ranking Confidence Table

Score each source:

| source_score_numeric_value | score_meaning_interpretation_text |
| ---: | --- |
| 5 | primary official source or maintainer-authored reference |
| 4 | widely used production repo or official-adjacent guide |
| 3 | high-quality community source with examples and recency |
| 2 | plausible but narrow blog/tutorial |
| 1 | low-authority, stale, or unverified source |

When sources conflict, keep both claims and explain the version, framework, or
context boundary where each is valid.

---

## 100-Line Chunk Protocol

For every long source, local file, repo file, or pasted text:

1. Read the file from start to finish.
2. Split it into chunks of at most 100 lines.
3. After each chunk, append new candidate parameters to the ledger.
4. Preserve the chunk range so claims can be traced.
5. After each file, consolidate duplicates and mark unresolved contradictions.

For each chunk ask:

- What does this chunk say the tool or ecosystem values?
- What names, modes, roles, or surfaces recur?
- What does it say to prefer?
- What does it say to avoid?
- What failure mode is being prevented?
- What boundary is being protected?
- What test or gate would prove the pattern?
- What artifact shape is implied?
- What context should be loaded later and what can stay out of context?

If a source is binary, empty, duplicated, generated, or irrelevant, record that
fact instead of pretending it was read as text.

---

## Work Surface Modes

Classify the target before selecting patterns.

Use one or more work modes:

| work_mode_selection_label | usage_context_trigger_condition |
| --- | --- |
| `Core Language Reliability Mode` | syntax, type system, standard library, package layout, public APIs |
| `Library API Design Mode` | reusable APIs, semver, docs, examples, compile/type contracts |
| `Command Line Interface Mode` | argument parsing, exit codes, config, stdin/stdout/stderr, diagnostics |
| `Backend Service Delivery Mode` | HTTP/RPC, persistence, auth, external clients, config, deployment |
| `Frontend Interface Delivery Mode` | UI state, accessibility, rendering, responsiveness, user workflows |
| `Desktop Mobile Host Mode` | host integration, permissions, packaging, platform conventions |
| `Data Pipeline Processing Mode` | ingestion, schemas, validation, streaming, batch, lineage |
| `Plugin Extension Lifecycle Mode` | manifests, lifecycle hooks, host APIs, compatibility |
| `Agent Skill Packaging Mode` | trigger quality, progressive disclosure, reference maps, tool use |
| `Review Risk Analysis Mode` | risk analysis, anti-pattern scan, test gaps, production readiness |
| `Migration Compatibility Planning Mode` | version drift, compatibility, deprecations, rollout safety |
| `Operations Runtime Readiness Mode` | deployment, observability, secrets, CI, runtime health |
| `Security Threat Control Mode` | auth, permissions, validation, secrets, supply chain |
| `Resilience Failure Recovery Mode` | retries, idempotency, cancellation, backpressure, partial failure |

State the selected modes before presenting patterns.

---

## Pattern Taxonomy

Mine patterns across all dimensions. Do not stop at syntax.

### 1. Language And Type-System Idioms

Look for:

- identifier naming convention patterns
- module package layout conventions
- visibility default access rules
- generic template abstraction patterns
- newtype value class branding
- enum sealed union modeling
- nullability absence state modeling
- ownership borrowing mutation semantics
- type inference boundary rules
- reflection metaprogramming boundary rules
- public API compatibility contracts

### 2. Boundary And Parsing Idioms

Look for:

- parse validate boundary patterns
- schema first runtime validation
- unknown input trust handling
- configuration environment parsing rules
- serialization deserialization compatibility rules
- transport normalization adapter boundaries
- filesystem process network boundaries
- interop language runtime boundaries

### 3. Error And Diagnostics Idioms

Look for:

- typed error result values
- exception boundary handling rules
- recoverable unrecoverable failure separation
- context layering diagnostic enrichment
- actionable diagnostic message design
- exit code semantics mapping
- logging tracing convention alignment
- panic crash boundary rules
- user operator message separation

### 4. Async, Concurrency, And Resource Idioms

Look for:

- cancellation propagation boundary rules
- timeout deadline passing rules
- structured concurrency ownership rules
- task ownership lifecycle rules
- async blocking isolation rules
- lock scope ordering discipline
- bounded queue backpressure handling
- retry idempotency coupling rules
- cleanup success error cancellation
- resource lifecycle management boundaries

### 5. Architecture And Boundary Idioms

Look for:

- domain adapter split boundaries
- port interface boundary design
- layer direction dependency rules
- framework light core design
- dependency injection construction seams
- feature module boundary rules
- state ownership lifecycle model
- configuration layering precedence rules
- public facade API design
- migration compatibility seam design

### 6. Testing And Verification Idioms

Look for:

- TDD red green refactor
- executable requirement contract tests
- unit test boundary scope
- integration test wiring coverage
- contract test compatibility coverage
- property test invariant coverage
- fuzz test frontier coverage
- compile fail type tests
- snapshot test output contracts
- concurrency model checking tests
- smoke test runtime readiness
- benchmark gate measurement thresholds
- lint format type gates

### 7. Security, Privacy, And Supply Chain Idioms

Look for:

- authentication session password rules
- secret lifecycle management practices
- input validation output encoding
- permission boundary enforcement model
- sandbox isolation runtime constraints
- dependency audit supply chain
- least privilege access design
- anti enumeration failure behavior
- secure default configuration posture
- privacy PII handling controls

### 8. Operations And Runtime Idioms

Look for:

- deployment model environment assumptions
- health check readiness semantics
- metrics signal collection strategy
- tracing span correlation model
- log correlation request identifiers
- environment configuration precedence rules
- migration rollout sequencing plan
- rollback recovery decision path
- feature flag lifecycle rules
- release gate promotion criteria
- container runtime constraint mapping
- observability contract signal coverage

### 9. Documentation And Agent Idioms

Look for:

- reference map routing structure
- progressive disclosure loading strategy
- frontmatter trigger metadata quality
- output contract section order
- mode selection routing rules
- context strategy loading order
- source brief provenance summary
- quality gate section coverage
- anti pattern registry entries
- example pattern teaching focus
- handoff checkpoint state summary

---

## Scoring Rubric

Score each candidate pattern out of 100.

| scoring_factor_parameter_key | factor_weight_numeric_value | decision_question_prompt_text |
| --- | ---: | --- |
| `pattern_failure_prevention_power` | 25 | Does it prevent a real class of bugs? |
| `pattern_misuse_resistance_strength` | 15 | Does it make the wrong thing harder to express? |
| `diagnostic_feedback_quality_value` | 10 | Does it make failures easier to understand? |
| `ecosystem_guidance_fit_strength` | 15 | Is it supported by official docs or serious code? |
| `applicability_breadth_usage_range` | 10 | Does it apply across common project types? |
| `maintainability_change_survival_score` | 10 | Does it survive change and onboarding? |
| `verification_gate_evidence_strength` | 10 | Can tests or tools prove it? |
| `cost_tradeoff_clarity_level` | 5 | Are the downsides named honestly? |

Keep:

- `default_adoption_pattern_tier`: 93-100, adopt by default
- `strong_context_pattern_tier`: 86-92, strong default with context
- `constraint_match_pattern_tier`: 80-85, useful when constraints match

Reject or quarantine patterns below 80 unless the user explicitly asks for
experimental or niche techniques.

---

## Anti-Pattern Mining

For every positive pattern, search for the matching failure pattern.

Capture anti-patterns in this shape:

| anti_pattern_failure_name | failure_mode_effect_summary | detection_signal_review_method | safer_default_replacement_pattern | verification_gate_evidence_method |
| --- | --- | --- | --- | --- |

Always look for:

- vague requirement success claims
- unchecked runtime trust boundaries
- nullable optional abuse patterns
- hidden global mutable state
- broad exception catch blocks
- silent error conversion paths
- async blocking execution hazards
- unbounded concurrency resource growth
- missing cleanup lifecycle paths
- retry idempotency mismatch failures
- framework leakage domain pollution
- transport validation domain confusion
- TODO STUB FIXME drift
- performance claim measurement gaps
- security claim threat gaps
- future work documentation drift

---

## Expert Lenses

Use 3 to 5 lenses. Always include one skeptical lens.

Recommended lenses:

1. ecosystem maintainer compatibility lens
2. production operator reliability lens
3. library API design lens
4. security reliability review lens
5. skeptical engineer challenge lens

Each lens should answer:

- What would this expert call idiomatic?
- What would this expert reject?
- What breaks at scale, under stress, or during maintenance?
- What evidence would change the recommendation?

---

## Output Contract

Return the final artifact in this order.

### 1. Premise Assumption Boundary Check

- State the target technology, version assumptions, and selected modes.
- Name any ambiguity or missing constraint.
- Say what is sourced fact vs inference.

### 2. Source Evidence Mapping Table

Include a compact table:

| source_location_url_path | source_category_artifact_type | source_authority_confidence_level | freshness_version_date_window | source_usage_synthesis_role |
| --- | --- | --- | --- | --- |

### 3. Pattern Scoreboard Ranking Table

Include:

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_name_action_phrase | pattern_failure_prevention_target | source_basis_evidence_summary |
| --- | ---: | --- | --- | --- | --- |

### 4. Idiomatic Thesis Synthesis Statement

Write the core thesis in one paragraph:

> Reliable <TECHNOLOGY> comes from ...

### 5. Mode Specific Pattern Sections

For each active mode, include:

- mode relevance rationale summary
- highest scoring pattern list
- usage context include rules
- usage context exclude rules
- minimal example structure shape
- verification gate evidence method

### 6. Default Reliability Stack Checklist

A compact checklist of defaults to use before writing code.

### 7. Architecture Default Boundary Map

State default boundaries:

- core domain boundary model
- adapter integration boundary layer
- configuration source precedence rules
- IO resource lifecycle boundaries
- persistence migration compatibility seams
- external system failure boundaries
- presentation UI workflow boundaries
- operations runtime readiness gates

### 8. Testing Verification Evidence Matrix

Use:

| requirement_risk_trace_key | verification_gate_test_name | tool_command_runner_name | evidence_output_observed_result |
| --- | --- | --- | --- |

### 9. Anti Pattern Registry Table

Use:

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |

### 10. Agent Skill Packaging Parameters

If the output will become a reusable agent skill, include:

- `skill_name_identifier_handle`
- `trigger_description_search_phrase`
- `usage_context_include_rules`
- `usage_context_exclude_rules`
- `mode_selection_surface_rules`
- `workflow_sequence_execution_steps`
- `context_strategy_loading_order`
- `reference_map_routing_file`
- `guardrail_refusal_avoidance_rules`
- `output_contract_section_order`
- `quality_gate_verification_commands`
- `source_brief_provenance_summary`

### 11. Future Refresh Search Queries

Provide reusable queries:

- `official_docs_query_phrase`
- `style_guide_search_query`
- `release_notes_query_phrase`
- `reference_implementation_search_query`
- `testing_guide_search_query`
- `security_advisory_query_phrase`
- `migration_guide_search_query`
- `production_example_query_phrase`

### 12. Open Question Decision Drivers

List only questions that materially change the pattern set.

---

## Agent Skill Skeleton

When asked to turn the research into a skill, use this shape.

```markdown
---
name: <technology>-coder-01
description: Reliability-first <TECHNOLOGY> skill for <surfaces>. Use when work needs <specific trigger terms>, <failure boundaries>, <tooling>, or <verification>.
---

# <Technology> Reliability

## Skill Purpose Overview Summary

Use this skill when the task is primarily about ...

## Usage Trigger Inclusion Rules

- ...

## Work Mode Selection Rules

- `Core Language Reliability Mode`: ...
- `Boundary Parsing Validation Mode`: ...
- `Async Runtime Resource Mode`: ...
- `Testing Verification Evidence Mode`: ...
- `Review Risk Analysis Mode`: ...

## Execution Workflow Sequence Steps

1. `surface_classification_initial_step`: Classify the delivery surface.
2. `executable_requirement_authoring_step`: Write requirements when behavior is unclear.
3. `progressive_reference_loading_step`: Load references progressively.
4. `boundary_design_preimplementation_step`: Design boundaries before implementation.
5. `reliability_rule_application_step`: Apply reliability rules.
6. `native_gate_verification_step`: Verify with repo-native gates.

## Output Artifact Expectation List

1. `<Technology> Work Planning Mode`
2. `Executable Requirement Contract Set`
3. `Boundary Type Design Summary`
4. `Runtime Interop Constraint Map`
5. `Verification Evidence Matrix Table`
6. `Implementation Sequence Planning Steps`
7. `Quality Gate Verification Commands`
8. `Open Question Decision Drivers`

## Guardrail Constraint Behavior Rules

- ...

## Reference File Routing Map

- [Reference Map Routing File](./references/reference-map.md)
- [Reliability Pattern Reference Guide](./references/<technology>-reliability-reference.md)
- [Quality Anti Pattern Guide](./references/<technology>-quality-gates-and-anti-patterns.md)
- [Source Research Brief Summary](./references/sources-and-research-brief.md)
```

---

## Human Scan Acceptance Test

Before answering, visually scan the artifact the way a skeptical product lead
would scan it. Look especially at objective parameters, ledger fields, source
classes, work modes, taxonomy bullets, scoring factors, anti-pattern rows,
output artifact names, skill skeleton labels, search query labels, and final
checklist items.

The artifact passes only if:

1. `four_word_label_compliance`: Reusable labels are exactly four semantic words.
2. `retrieval_density_label_quality`: Labels are specific enough to retrieve later.
3. `decision_support_label_clarity`: Labels imply the user decision they support.
4. `short_bucket_avoidance_check`: Labels avoid one-word buckets unless explicitly shown as rejected examples.
5. `pattern_boundary_proof_gate`: Every pattern explains adoption boundary, failure prevented, and proof gate.
6. `source_claim_uncertainty_split`: Every source claim separates fact, inference, and unresolved uncertainty.
7. `artifact_reuse_readiness_check`: The final output can become a review checklist or agent skill without
   another structural rewrite.

## Quality Bar

Specific, concrete, useful density beats elegant brevity. Do not add decorative
theory. Do not pad labels with empty words. Do not leave one-word taxonomy
bullets, skill fields, output artifacts, source classes, mode labels, or search
query parameters for the user to fix later.

## Final Verification Before Answering

Before finalizing, verify:

1. `active_parameter_completion_check`: Every active parameter was either filled or explicitly marked unknown.
2. `default_pattern_source_check`: Every default adoption pattern has at least one strong source.
3. `nonfunctional_claim_gate_check`: Every non-functional claim has a measurement or gate.
4. `anti_pattern_replacement_check`: Every anti-pattern has a safer replacement.
5. `recommendation_boundary_context_check`: Every recommendation says when it does not apply.
6. `version_specific_guidance_check`: Version-specific guidance is labeled by version.
7. `fact_inference_separation_check`: The output separates sourced facts from inference.
8. `human_scan_acceptance_check`: Every reusable concept label survives the human scan acceptance test.
9. `human_agent_utility_check`: The result is useful for both humans and LLM agents.

End with a concise summary of what changed after verification.
````

---

## Parameter Reference

Use this section to adapt the prompt quickly without rewriting it.

### Core Input Parameters

| four_word_parameter_name | example_values_or_context |
| --- | --- |
| `target_technology_language_name` | Rust, Kotlin, Python, TypeScript, Go, Java, Swift |
| `ecosystem_platform_scope_context` | web backend, frontend, desktop, mobile, embedded, data, infra |
| `runtime_execution_host_environment` | Tokio, Node.js, JVM, CPython, browser, WASM, Linux container |
| `framework_library_stack_names` | Axum, React, Ktor, Spring Boot, FastAPI, Tauri |
| `artifact_delivery_surface_type` | library, CLI, API, worker, plugin, skill, guide |
| `quality_priority_goal_focus` | reliability, security, performance, maintainability |
| `audience_consumer_usage_context` | LLM coding agent, human implementer, reviewer, architect |
| `freshness_version_date_window` | current date or target version window |

### Research Parameters

| four_word_parameter_name | question_to_answer_clearly |
| --- | --- |
| `source_authority_confidence_level` | Is this official, maintainer-authored, production code, or community? |
| `source_freshness_version_window` | Is the source current for the requested version? |
| `source_conflict_resolution_basis` | Which sources disagree, and why? |
| `reference_implementation_evidence_source` | What serious codebase demonstrates the pattern? |
| `migration_pressure_change_driver` | What changed recently that invalidates old idioms? |

### Pattern Parameters

| four_word_parameter_name | question_to_answer_clearly |
| --- | --- |
| `pattern_failure_prevention_power` | What failure does this pattern remove? |
| `pattern_misuse_resistance_strength` | How does the pattern make incorrect use harder? |
| `diagnostic_feedback_quality_value` | How does it make failures easier to debug? |
| `ergonomic_cost_tradeoff_profile` | What does the pattern make more verbose or harder? |
| `applicability_boundary_usage_limit` | When should the pattern not be used? |
| `verification_gate_evidence_method` | What test, lint, build, or check proves it? |

### Agent Packaging Parameters

| four_word_parameter_name | question_to_answer_clearly |
| --- | --- |
| `trigger_description_search_phrase` | What user phrasing should load this skill? |
| `mode_selection_surface_rules` | What surfaces require different behavior? |
| `context_strategy_loading_order` | What is loaded first, later, or never? |
| `reference_map_routing_file` | Which file routes the agent to detailed references? |
| `output_contract_section_order` | What sections must the agent return? |
| `guardrail_refusal_avoidance_rules` | What must the agent refuse or avoid? |

---

## Repo Pattern Sources Folded Into This Prompt

The prompt above incorporates recurring structures from the repo:

- `llm_native_engineering_principles`: retrieval biasing, iteration, checkpointing, negative knowledge, tests as specs, four-word naming, and workflow routing.
- `executable_specification_contract_patterns`: `WHEN...THEN...SHALL`, stable requirement IDs, TDD plans, and traceability matrices.
- `reliability_language_skill_patterns`: scored pattern boards, type/value boundaries, strict compiler/type gates, parse-at-boundary defaults, explicit cancellation, and anti-pattern registries.
- `backend_delivery_skill_patterns`: mode selection, service boundaries, persistence/migration safety, security, resilience, operations, and production quality gates.
- `skill_development_documentation_patterns`: trigger descriptions, progressive disclosure, reference maps, lean `SKILL.md` bodies, and validation of bundled references.
- `context_engineering_agent_patterns`: small action surfaces, filesystem offload, subagent isolation, source maps, and verification before completion.
- `frontend_design_review_patterns`: audience fit, artifact-first output, domain-specific visual/design expectations, and review checklists.

The point is not to make every future prompt longer. The point is to make the
search space explicit so each future technology run can choose the relevant
parameters deliberately.
