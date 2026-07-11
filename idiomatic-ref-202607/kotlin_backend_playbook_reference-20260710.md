# Kotlin Backend Playbook Reference

**Decision supported.** This section helps decide how to shape a Kotlin service, route, or worker so transport, application, domain, persistence, integration, and runtime risks remain visible and testable. The seed title does not explain that reliable Kotlin backend delivery starts by preserving the existing framework and making six service boundaries, executable requirements, and operational evidence explicit.

**Recommended default and causal basis.** Preserve the existing Spring or Ktor framework; write a versioned executable requirement; map the six request boundaries; encode domain intent in Kotlin types; model expected errors; name transaction, blocking, timeout, retry, idempotency, migration, observability, and rollback behavior before implementation. Kotlin reduces boilerplate but cannot remove architectural, concurrency, persistence, security, or operational boundaries that determine production behavior.

**Operating conditions and assumptions.** This default works for service features, endpoints, workers, and hardening changes where the codebase already has framework and persistence conventions. Assume feature delivery within an existing Kotlin backend; current repository conventions, user scope, security policy, and verified framework behavior remain controlling.

**Failure boundary and alternatives.** It becomes disproportionate for an intentionally tiny CRUD path and becomes unsafe when framework, transaction, blocking, or migration behavior is guessed rather than inspected. Bounded alternatives and recoveries: Use a compact boundary map for a tiny service, preserve an intentionally blocking stack, narrow to one risky boundary, or defer framework migration to an explicit separate task.

**Counterexample, gotchas, and operational comparison.** Incidental framework migration, one-class-for-everything models, raw primitive identifiers, exceptions as business API, controller transactions, blocking calls on coroutine threads, and unproved SLOs are central risks. Good: add a create-account endpoint with separate request/domain/persistence/response types, duplicate-email outcome, service transaction, migration, and integration test. Bad: serialize a JPA entity and catch all exceptions. Borderline: a CRUD-only internal tool may share shapes if the tradeoff is explicit and tested.

**Verification, evidence, and uncertainty.** Trace the requirement through all six boundaries, compile and test the service, inspect framework and dispatcher behavior, exercise errors and abuse cases, validate migrations and rollback, and collect operational evidence for each non-functional claim. The six boundaries, framework-preserving rule, requirement scheme, type guidance, error taxonomy, transaction defaults, coroutine cautions, client policies, API defaults, and review checklist are direct local facts. Exact framework APIs, test tools, persistence adapters, and acceptable service targets depend on the repository and current dependency versions.

**Second-order consequence.** The playbook is a boundary-preservation method: Kotlin expressiveness should compress implementation noise while making failure semantics and ownership more explicit.

**Revision decision.** Turn the title section into a six-boundary delivery decision with compact, blocked, and explicit-migration branches.

**Retained seed evidence.** The original title remains while the evolved opening supplies the missing service-level contract. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source governs backend shape and when Kotlin, coroutine, Spring, or Ktor documentation is needed for a specific implementation claim. The seed lists one local playbook and four public sources but does not distinguish the local service-level policy from framework- or library-specific freshness evidence, and no public page was retrieved in this pass.

**Recommended default and causal basis.** Use the local playbook for service anatomy and defaults; consult current primary Kotlin or coroutine documentation for language/runtime behavior and the matching Spring or Ktor source only for the framework already present. A service-level rule and a version-specific framework fact have different authority and invalidation conditions.

**Operating conditions and assumptions.** This map works when claims name their boundary, dependency, version, source role, retrieval date, and local applicability. No new browsing occurred, and public pointers cannot override local framework preservation or repository conventions.

**Failure boundary and alternatives.** It fails when all public sources are treated as interchangeable, Spring examples drive Ktor code, or URL presence becomes proof of current behavior. Bounded alternatives and recoveries: Inspect local build files and code, use archived playbook guidance conditionally, retrieve an authorized primary source for a named claim, or preserve uncertainty.

**Counterexample, gotchas, and operational comparison.** Version drift, framework halo, coroutine assumptions, sample-app simplification, and counting one local source as complete policy can create false confidence. Good: use the local playbook to preserve Ktor and current Ktor docs for plugin configuration. Bad: cite a Spring tutorial to justify a Ktor transaction pattern. Borderline: use Kotlin docs for value-class semantics only after checking serializer and persistence support.

**Verification, evidence, and uncertainty.** Check the local source hash and headings, dependency versions, selected external role, retrieval state, exact locator, local behavior test, and conclusion invalidation. The one local playbook was read completely and directly defines cross-framework backend boundaries. The four public sources were not refreshed, and their current examples or compatibility may differ from the archived mapping.

**Second-order consequence.** A narrow local corpus increases the need for repository evidence: build files, existing conventions, tests, and runtime behavior become essential corroboration without becoming duplicate authority.

**Revision decision.** Retain all rows while adding boundary scope, framework match, dependency version, retrieval state, and applicability rules.

**Retained seed evidence.** The seed rows remain for provenance, with the one-source confidence limitation explicit. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/references/kotlin-backend-playbook.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://kotlinlang.org/docs/home.html | external_research_source_material | external_research_sourced_fact | primary language documentation for Kotlin idioms and type system |
| https://github.com/Kotlin/kotlinx.coroutines | external_research_source_material | external_research_sourced_fact | official coroutine library and implementation evidence |
| https://github.com/spring-guides/tut-spring-boot-kotlin | external_research_source_material | external_research_sourced_fact | Spring-maintained Kotlin web application example |
| https://ktor.io/docs/welcome.html | external_research_source_material | external_research_sourced_fact | primary Ktor server and client framework documentation |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide how to order backend delivery controls without treating inherited scores as measured correctness or reliability. The seed assigns 95, 91, and 88 to generic controls without a rubric and omits framework preservation, six-boundary design, executable requirements, or operational proof.

**Recommended default and causal basis.** Treat scores as uncalibrated metadata and order controls causally: inspect the existing stack, specify behavior, map boundaries, model types/errors/transactions, implement the smallest change, then verify functional and operational claims. Source labeling and final verification cannot rescue a feature built on the wrong framework, transaction scope, or blocking assumption.

**Operating conditions and assumptions.** The dependency order works when reviewers need a compact sequence and recognize several gates as jointly mandatory. Do not reinterpret seed numbers as probabilities, SLOs, coverage, or framework preference.

**Failure boundary and alternatives.** It fails when 95 implies success probability, when the top row bypasses executable requirements, or when a generic verifier substitutes for service tests. Bounded alternatives and recoveries: Use an unscored dependency graph or calibrated rubric covering framework fit, boundary integrity, contract behavior, concurrency, persistence, security, operations, and rollback.

**Counterexample, gotchas, and operational comparison.** False precision, score anchoring, independent ranking of dependent controls, and using inherited values to market readiness are principal hazards. Good: preserve score metadata but reject an endpoint lacking transaction tests. Bad: claim 95 percent reliability. Borderline: future scoring is acceptable only with task classes, denominators, reviewers, and sensitivity.

**Verification, evidence, and uncertainty.** Require score derivation, dimensions, sample, calibration, uncertainty, and decision effect; otherwise verify only the ordered backend gates. The row values are seed facts; the playbook directly supports the boundary-first ordering. No benchmark connects score differences to defects, latency, or deployment outcomes.

**Second-order consequence.** Backend reliability is bottlenecked by the earliest unnamed boundary, so late polish cannot compensate for a wrong transport, transaction, or coroutine model.

**Revision decision.** Preserve and qualify the rows while linking them to the concrete Kotlin delivery sequence.

**Retained seed evidence.** The original scoreboard stays visible with its unsupported precision bounded. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `kotlin_backend_playbook_reference` | 95 | default_adoption_pattern_tier | Source Map First: Load local kotlin backend material before synthesizing playbook reference recommendations. |
| `kotlin_backend_playbook_reference` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `kotlin_backend_playbook_reference` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what compact governing thesis should guide a Kotlin backend feature from requirement to deployable behavior. The seed offers generic local-first synthesis but omits the playbook's actual thesis: Kotlin backend quality comes from visible boundaries, framework sympathy, explicit contracts, typed intent, and verified operations.

**Recommended default and causal basis.** Preserve the current framework, define executable behavior, keep six service boundaries visible, use Kotlin types for domain intent, separate DTO/domain/persistence shapes when invariants differ, model expected failures, place transactions around use cases, name blocking and retry behavior, and prove every non-functional claim. Reliable delivery requires boundary clarity and evidence rather than Kotlin syntax, framework novelty, or architecture ceremony.

**Operating conditions and assumptions.** This thesis works when one service feature can be traced from edge validation through runtime and rollback. Present framework-neutral service policy separately from versioned Spring, Ktor, database, and coroutine facts.

**Failure boundary and alternatives.** It fails when applied as rigid layering to an intentionally tiny app or when current framework behavior is assumed without repository inspection. Bounded alternatives and recoveries: Compress layers for simple CRUD with named tradeoffs, keep a blocking architecture deliberately, or isolate a migration as its own executable requirement.

**Counterexample, gotchas, and operational comparison.** Clean-looking data classes can hide JPA identity problems, suspend functions can hide blocking work, and generic exceptions can hide unstable public contracts. Good: a payment transition uses a sealed outcome, service transaction, typed ID, timeout-bound client, and stable error envelope. Bad: annotate one mutable entity for request, domain, persistence, and response. Borderline: manual mapping is sufficient until complexity justifies explicit mappers.

**Verification, evidence, and uncertainty.** Map every final recommendation to a boundary, requirement, code path, test, migration, operational signal, and rollback condition. Every element of the thesis is direct local playbook guidance. The smallest appropriate architecture and exact adapter choices remain repository-specific.

**Second-order consequence.** Idiomatic Kotlin backend design is not maximal abstraction; it places type precision and explicit effects exactly where failures cross boundaries.

**Revision decision.** Replace generic evidence order with a framework-preserving six-boundary delivery thesis.

**Retained seed evidence.** The three evidence labels remain beneath a concrete backend thesis. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `kotlin_backend_playbook_reference` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Kotlin Backend Playbook Reference comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which playbook sections govern each backend decision and when repository or external evidence must supplement them. The seed correctly maps one local playbook but does not expose its section-level authority or the limits of drawing broad policy from a single archived source.

**Recommended default and causal basis.** Use Service Anatomy and Framework Choice first, then load the relevant sections for requirements, modeling, errors, persistence, transactions, coroutines, clients/workers, API contracts, and review. Section-targeted reading reduces generic advice and keeps each recommendation tied to the risk boundary it addresses.

**Operating conditions and assumptions.** This map works when a task names the endpoint, worker, persistence change, or operational concern before guidance is selected. Archived playbook guidance cannot override current code, current dependencies, or higher-priority requirements.

**Failure boundary and alternatives.** It fails when the entire playbook is treated as an exhaustive framework manual or a single source is promoted to immutable organizational policy. Bounded alternatives and recoveries: Read only the relevant section, inspect local code and build configuration, consult current primary framework docs, or add a confidence boundary.

**Counterexample, gotchas, and operational comparison.** One-source authority inflation, truncated heading signals, archived dependency assumptions, and framework-neutral rules misapplied as APIs can mislead implementation. Good: use Transaction Boundaries plus local service tests for a write use case. Bad: infer a Spring annotation from a framework-neutral sentence. Borderline: use the checklist as orientation before deeper source inspection.

**Verification, evidence, and uncertainty.** Record source hash, relevant headings, extracted rule, local code evidence, version-sensitive gaps, and whether supplemental evidence changed the decision. The complete 143-line playbook and its sections were directly inspected. No companion local files establish framework-version detail or organizational precedence.

**Second-order consequence.** A single local source is strongest as a decision index and weakest as independent corroboration; repository behavior supplies the missing specificity.

**Revision decision.** Turn the one-row map into a section-indexed decision guide with explicit single-source limits.

**Retained seed evidence.** The canonical row remains while its authority is narrowed to the service-level playbook. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/references/kotlin-backend-playbook.md | Kotlin Backend Playbook | Kotlin Backend Playbook; Service Anatomy; Framework Choice; Executable Requirements; REQ-KOTLIN-BACKEND-001.0: Create Account Endpoint; Kotlin Domain Modeling | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide which current primary source should verify a language, coroutine, or framework-specific claim. The seed maps Kotlin, coroutines, Spring, and Ktor sources but does not define when each is relevant or prevent cross-framework and stale-version inference.

**Recommended default and causal basis.** Use Kotlin docs for language/type behavior, kotlinx.coroutines for concurrency semantics, Spring-maintained material for existing Spring services, and Ktor docs for existing Ktor services; always match repository versions. Framework and library semantics change independently, and a generally correct Kotlin rule may fail at serialization, persistence, proxying, or plugin boundaries.

**Operating conditions and assumptions.** This approach works when browsing is authorized and the exact dependency and behavior under dispute are known. No browsing occurred in this pass, and external rows remain pointers rather than current facts.

**Failure boundary and alternatives.** It fails under no-browse constraints, version mismatch, cross-framework copying, or reliance on example applications as production proof. Bounded alternatives and recoveries: Inspect dependency source/help, run focused compile and integration tests, use local conventions, narrow the claim, or preserve uncertainty.

**Counterexample, gotchas, and operational comparison.** Sample-app shortcuts, prerelease APIs, servlet/reactive confusion, coroutine bridge differences, and undocumented transitive versions can invalidate guidance. Good: check current coroutine cancellation semantics for the installed version. Bad: use a Ktor example to justify Spring WebFlux/JPA mixing. Borderline: a Spring guide provides orientation but local tests establish behavior.

**Verification, evidence, and uncertainty.** Capture URL, version, date, exact locator, supported claim, local dependency, reproduction, contradiction, and resulting code or guidance change. The mapped source categories are appropriate primary surfaces for their named domains. No public content was retrieved now, so current details remain unverified.

**Second-order consequence.** External research should begin from a failing boundary or disputed API, not from a generic Kotlin backend search.

**Revision decision.** Preserve the rows with dependency-version, framework-match, retrieval, and local-test requirements.

**Retained seed evidence.** The four public rows remain discovery surfaces with claim scope explicit. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://kotlinlang.org/docs/home.html | Kotlin documentation | primary language documentation for Kotlin idioms and type system | external_research_sourced_fact |
| https://github.com/Kotlin/kotlinx.coroutines | Kotlin coroutines repository | official coroutine library and implementation evidence | external_research_sourced_fact |
| https://github.com/spring-guides/tut-spring-boot-kotlin | Spring Boot Kotlin guide | Spring-maintained Kotlin web application example | external_research_sourced_fact |
| https://ktor.io/docs/welcome.html | Ktor documentation | primary Ktor server and client framework documentation | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which backend mistakes should stop implementation or trigger redesign before rollout. The seed lists only generic source and verification failures, omitting the playbook's Kotlin-specific architecture, modeling, persistence, transaction, coroutine, and API hazards.

**Recommended default and causal basis.** Detect incidental framework migration, collapsed DTO/domain/entity shapes, primitive identifier drift, data-class JPA entities without lifecycle analysis, exception-only business outcomes, controller transactions, external calls inside transactions, GlobalScope, unbounded calls, blocking work on event loops, blind retries, entity serialization, and unproved NFRs. Each failure obscures ownership or lets a local convenience cross a boundary with production consequences.

**Operating conditions and assumptions.** The registry works when every anti-pattern has an observable code or test signal, containment action, owner, and rerun gate. Evaluate actual code, tests, and runtime behavior rather than style preferences alone.

**Failure boundary and alternatives.** It fails when labels are enforced without repository context or when every small CRUD class is forced into maximal layering. Bounded alternatives and recoveries: Use architecture tests, compile fixtures, integration tests, transaction probes, coroutine tests, migration tests, abuse cases, and load tests tied to explicit requirements.

**Counterexample, gotchas, and operational comparison.** Suspend syntax can look non-blocking, sealed outcomes can be bypassed by thrown infrastructure errors, and a green unit test can miss proxy or transaction behavior. Good: isolate blocking JDBC on a bounded pool in an intentionally blocking service. Bad: call JPA from an event-loop path without naming pool impact. Borderline: one model for a tiny CRUD app is acceptable only with intentional constraints.

**Verification, evidence, and uncertainty.** Seed failures for duplicate business outcomes, malformed input, missing auth, proxy equality, lazy loading, timeout, cancellation, duplicate delivery, migration compatibility, and accidental entity exposure. Every anti-pattern is derived directly from the local playbook. Severity and detection tooling depend on framework and persistence choices.

**Second-order consequence.** The most dangerous Kotlin anti-pattern is syntactic safety theater: concise or suspend code can hide mutable identity, blocking I/O, and uncontrolled effects.

**Revision decision.** Expand the registry into framework, type, mapping, error, transaction, coroutine, integration, API, and evidence failures.

**Retained seed evidence.** The generic seed rows remain as umbrella categories beneath Kotlin-specific diagnostics. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide what evidence proves both this reference and a Kotlin backend change are reliable. The seed supplies only the generated-reference verifier, which cannot prove compilation, framework wiring, request contracts, transactions, coroutine behavior, migrations, security, or operations.

**Recommended default and causal basis.** Layer focused reference validation with repository build and tests, requirement trace, endpoint integration tests, domain outcome tests, transaction and persistence tests, coroutine/cancellation tests, migration checks, abuse cases, and SLO-specific measurements. Markdown validity, functional behavior, and operational safety are separate claims requiring different evidence.

**Operating conditions and assumptions.** The gate stack works when the repository exposes its actual build, framework test harness, database strategy, and deployment checks. The retained archive command proves only generated-reference structure.

**Failure boundary and alternatives.** It fails when one green suite substitutes for production boundaries, when mocks hide transaction or serialization behavior, or when fixed latency numbers are copied without an SLO. Bounded alternatives and recoveries: Use test fixtures, Testcontainers or repository equivalents, contract tests, architecture checks, migration dry runs, targeted benchmarks, and manual operational review.

**Counterexample, gotchas, and operational comparison.** Wrong Gradle task, stale generated code, test profiles unlike production, virtual-time misuse, transaction rollback in tests, and missing migration ordering can create false confidence. Good: compile, run endpoint and database integration tests, inject timeout/cancellation, validate migration rollback, and measure against the service SLO. Bad: run only the reference verifier. Borderline: unit tests suffice for a pure domain value object, not its adapters.

**Verification, evidence, and uncertainty.** Record commands, versions, exits, requirement IDs, selected boundaries, fixtures, database state, timing method, failures injected, migration result, security result, and residual risk. The playbook directly requires executable requirements, evidence for NFRs, and tests proving breakable boundaries. Exact commands and tools depend on Gradle/Maven, framework, persistence, and CI configuration.

**Second-order consequence.** Verification should cross the same six boundaries as the request; otherwise a green layer can conceal a broken neighboring contract.

**Revision decision.** Keep the seed command as one layer and add build, contract, domain, persistence, coroutine, migration, security, and operational gates.

**Retained seed evidence.** The original verifier remains with a precise proof boundary. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when to use the playbook, when to narrow to one boundary, and when to route to a framework, testing, security, or runtime reference. The seed triggers generically on theme or path and does not distinguish service design, framework-specific implementation, test-fixture work, operational hardening, or explicit migration.

**Recommended default and causal basis.** Use for Kotlin service features, routes, workers, persistence changes, and operational review; inspect the existing framework first, write the requirement, then select only the boundary guidance needed. The playbook is cross-framework service policy, not a substitute for current framework APIs or specialized testing and operations guidance.

**Operating conditions and assumptions.** Full use works when a feature crosses several boundaries or changes storage, integration, or runtime behavior. Do not use this guide to override repository architecture, user scope, or current framework evidence.

**Failure boundary and alternatives.** It is the wrong sole reference for fixture mechanics, framework migration, deep security design, or day-two operations beyond the playbook's scope. Bounded alternatives and recoveries: Use a compact boundary review, route fixture work to the Kotlin testing reference, consult current Spring/Ktor docs, invoke security/runtime guidance, or split explicit migration.

**Counterexample, gotchas, and operational comparison.** Over-triggering, migrating frameworks incidentally, loading external docs before reading local conventions, and implementing before an executable requirement are common errors. Good: use full playbook for create-account; use only domain modeling for a validated ID. Bad: use it to invent a Ktor API in Spring. Borderline: pair it with fixture guidance when integration setup dominates.

**Verification, evidence, and uncertainty.** Check trigger, existing framework, requirement ID, affected boundaries, selected supporting evidence, route decision, and whether the output changes the next implementation or review action. The local playbook explicitly frames itself as service-level shape before framework detail. The point at which specialized references should take over depends on repository complexity.

**Second-order consequence.** Correct narrowing prevents a comprehensive playbook from becoming generic context that obscures the one boundary actually at risk.

**Revision decision.** Replace generic bullets with full-playbook, boundary-only, framework-detail, fixture, security/runtime, and migration routes.

**Retained seed evidence.** The original trigger remains while boundary and destination selection govern use. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide how a builder moves from a requested backend behavior to a verified and rollback-aware Kotlin change. The seed names a Kotlin builder and production safety but skips the actual journey from requirement and framework inspection through boundaries, implementation, verification, and rollout.

**Recommended default and causal basis.** Identify the user outcome, inspect framework and persistence conventions, write a versioned requirement, map six boundaries, choose domain/error/transaction/coroutine/client models, implement the smallest change, test breakable boundaries, validate migration and operations, then plan rollout and rollback. Visible stages expose incompatible assumptions before they become coupled implementation and deployment defects.

**Operating conditions and assumptions.** The journey works when the feature scope, service owner, repository, and deployment environment are known. Keep the change within the authorized feature and preserve existing framework and operational contracts.

**Failure boundary and alternatives.** It fails when framework choice is guessed, requirements stay narrative, or operational evidence is deferred until after rollout. Bounded alternatives and recoveries: Pause for one missing constraint, narrow to a pure domain change, preserve a blocking architecture, or split migration and feature delivery.

**Counterexample, gotchas, and operational comparison.** Premature abstraction, hidden auth assumptions, data-model leakage, long transactions, uncancelled clients, and unreviewed schema changes can derail delivery. Good: define duplicate email as a sealed outcome and HTTP 409, then test transaction and migration. Bad: code a controller first. Borderline: a read-only endpoint may omit a write transaction but still needs validation and deterministic pagination.

**Verification, evidence, and uncertainty.** A reviewer should reconstruct requirement, framework evidence, each boundary, model choices, tests, migration, metrics, rollout, rollback, and unresolved risk. The journey is a direct synthesis of the playbook's ordered concerns. Repository workflow determines the exact implementation and deployment sequence.

**Second-order consequence.** The journey is reliable when every boundary has an owner, observable failure, and rollback or recovery path.

**Revision decision.** Expand the scenario into requirement, inspection, boundary design, implementation, verification, and rollout states.

**Retained seed evidence.** The original builder role remains while the journey becomes executable. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Kotlin backend builder is starting from a service, route, or worker that must become production-safe and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `kotlin_backend_playbook_reference` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the smallest reliable backend pattern that preserves coroutine, framework, and operational discipline.
Reference opening trigger: Open this file when the task mentions kotlin backend playbook reference, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide which backend implementation strategy fits the existing stack, invariants, operational needs, and cost of being wrong. The seed's generic Adopt, Adapt, Avoid rows omit the consequential Kotlin choices among Spring/Ktor preservation, blocking/reactive stacks, persistence styles, mapping depth, transaction scope, and durable workflows.

**Recommended default and causal basis.** Preserve Spring or Ktor; choose blocking or non-blocking end to end; select JPA, JDBC, Exposed, jOOQ, or R2DBC deliberately; separate shapes when invariants differ; and choose single transaction, outbox, saga, or no transaction explicitly. Each choice trades convenience, control, framework compatibility, and operational complexity, so local stack consistency is safer than novelty.

**Operating conditions and assumptions.** The guide works when existing dependencies, team conventions, data model, traffic behavior, and failure requirements are visible. A feature task cannot silently become a framework or persistence migration.

**Failure boundary and alternatives.** It fails when R2DBC is selected for fashion, JPA is mixed into event-loop paths, or every DTO/entity split becomes ceremony. Bounded alternatives and recoveries: Spring-preserving, Ktor-preserving, intentionally blocking, end-to-end reactive, manual mapping, explicit mapper, JPA, JDBC, Exposed, jOOQ, outbox, saga, or defer.

**Counterexample, gotchas, and operational comparison.** Hybrid stacks can combine both complexity sets, and sunk framework effort can bias a feature toward migration. Good: retain Spring MVC/JPA for conventional CRUD and isolate one timeout-bound client. Bad: introduce Ktor and R2DBC in the same feature. Borderline: use one shape for intentional CRUD-only scope with a documented exit trigger.

**Verification, evidence, and uncertainty.** Record chosen and rejected options, framework evidence, invariants, blocking model, persistence tradeoff, transaction scope, migration impact, operational cost, and change trigger. All listed tradeoffs are direct playbook guidance. No universal framework or persistence choice wins across services.

**Second-order consequence.** The cost of being wrong is usually boundary mismatch, not syntax: thread pools, proxy semantics, transaction duration, and public contracts determine blast radius.

**Revision decision.** Replace generic modes with framework, execution, persistence, mapping, transaction, and workflow decisions.

**Retained seed evidence.** The seed decision vocabulary remains as context beneath concrete Kotlin choices. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the kotlin backend playbook reference pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong kotlin backend playbook reference guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide how to use one archived service-level source without overstating authority or losing practical guidance. The seed marks the sole playbook canonical but also warns that one local source is insufficient for broad policy; it does not explain how repository and current primary evidence supplement rather than vote against it.

**Recommended default and causal basis.** Treat the playbook as canonical for this reference's cross-framework service shape, local repository code and tests as implementation evidence, and current primary docs as version-specific verification. A single source can organize decisions but cannot independently prove current framework APIs or universal organizational policy.

**Operating conditions and assumptions.** The hierarchy works when claims are separated into service policy, repository convention, and dependency behavior. Do not promote this generated reference to organization-wide policy without approved corroboration.

**Failure boundary and alternatives.** It fails when the playbook overrides current code, when local convention is copied despite a known defect, or when external samples become policy. Bounded alternatives and recoveries: Preserve the playbook default, document a local deviation, verify a current API, seek another approved internal source, or retain a confidence warning.

**Counterexample, gotchas, and operational comparison.** Canonical can be confused with exhaustive, recency with correctness, and repeated repository patterns with intentional architecture. Good: use the playbook for service transaction placement and local tests for the actual annotation. Bad: infer current Ktor APIs. Borderline: deviate from a local pattern when tests and an approved migration justify it.

**Verification, evidence, and uncertainty.** Record claim class, source, version, local evidence, conflict, owner decision, and invalidation trigger. The playbook's service-level content is direct and internally coherent. No companion local source or governance policy establishes broader precedence.

**Second-order consequence.** The hierarchy is triangular: stable service principles, current repository reality, and current dependency semantics constrain one another.

**Revision decision.** Add claim-class authority, repository evidence, external verification, conflict handling, and promotion limits.

**Retained seed evidence.** The single-source warning remains central rather than being hidden by the canonical label. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/references/kotlin-backend-playbook.md | canonical primary source | Kotlin Backend Playbook; Service Anatomy; Framework Choice | What guidance, warning, or example should this source contribute to Kotlin Backend Playbook Reference? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete design artifact makes a Kotlin backend request path reviewable before coding. The seed requests a lifecycle diagram with persistence, observability, and failures but does not specify the six boundaries, contracts, transaction scope, coroutine behavior, rollout, or evidence needed to review it.

**Recommended default and causal basis.** Produce a request lifecycle dossier with a six-boundary ASCII flow, request and response contracts, domain types and outcomes, transaction scope, persistence and migration, external timeout/retry/idempotency, dispatcher or blocking model, logs/metrics/health, tests, rollout, rollback, and failure table. The artifact reveals cross-boundary assumptions and gives implementation and review a shared contract.

**Operating conditions and assumptions.** It works for endpoints and workers with meaningful persistence, integration, or runtime behavior. The artifact must reflect the actual framework and deployment path rather than an aspirational architecture.

**Failure boundary and alternatives.** It fails when the diagram is decorative, omits error paths, or records abstractions without mapping them to existing code. Bounded alternatives and recoveries: Use a compact boundary checklist for a small endpoint, a state transition table for domain-only work, or a sequence diagram for distributed workflows.

**Counterexample, gotchas, and operational comparison.** Happy-path-only arrows, unspecified transaction edges, retries inside transactions, missing cancellation, and metrics without owners can create false readiness. Good: show parse/auth, command, sealed outcome, service transaction, outbox, timeout, response mapping, metric, and rollback. Bad: controller-to-database arrow. Borderline: a read-only route can use a shorter dossier while retaining validation, ordering, and timeout behavior.

**Verification, evidence, and uncertainty.** Trace each arrow and failure row to a requirement, code owner, test, signal, and rollback; ensure the ASCII diagram remains aligned and legible. The six-boundary model and seed artifact directly support this dossier. Distributed systems may need additional sequence, deployment, or data-flow artifacts.

**Second-order consequence.** A lifecycle diagram is valuable when it shows where ownership and failure semantics change, not merely call order.

**Revision decision.** Expand the three-field seed artifact into a six-boundary lifecycle dossier with an operational ASCII flow.

**Retained seed evidence.** The original lifecycle-diagram intent remains and gains concrete review fields. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

**Operational ASCII diagram.**

~~~text
HTTP request
  -> Transport: parse, authenticate, map response
  -> Application: use case, idempotency, transaction choreography
  -> Domain: typed invariants, state transition, expected outcome
  -> Persistence: query, migration compatibility, transaction scope
  -> Integration: timeout, retry class, deduplication or outbox
  -> Runtime: logs, metrics, health, rollout, rollback
HTTP response or durable worker outcome
~~~

Theme specific artifact: request lifecycle diagram with persistence boundary, observability hook, and failure table.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Kotlin Backend Playbook Reference | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide what good, bad, and borderline backend delivery look like for the same create-account endpoint. The seed examples are circular source-loading statements and do not demonstrate a real Kotlin request lifecycle, error contract, transaction, coroutine boundary, migration, or operational gate.

**Recommended default and causal basis.** Use one create-account scenario across all cases so framework fit, shape separation, domain outcomes, transaction scope, persistence, timeout behavior, tests, migration, and rollout can be compared directly. A controlled scenario reveals which boundary decision changes reliability rather than defining quality by reference compliance.

**Operating conditions and assumptions.** The examples work when each starts from the same executable requirement and existing framework. Examples illustrate design mechanics and are not current code or performance evidence.

**Failure boundary and alternatives.** They fail when good simply follows the playbook, bad merely ignores it, or borderline lacks a precise condition that changes acceptability. Bounded alternatives and recoveries: Use a payment transition, paginated read, queue worker, or external-client workflow when it better exposes the boundary under review.

**Counterexample, gotchas, and operational comparison.** Examples can invent framework behavior, overfit one ORM, hide security decisions, or use unrealistic in-memory tests as proof. Good: parse and authenticate, map to a command, return a sealed duplicate outcome, commit once, migrate safely, and test HTTP 409. Bad: bind JSON directly to a JPA data class and catch Exception. Borderline: one CRUD model is acceptable for a tiny internal app until invariants diverge.

**Verification, evidence, and uncertainty.** Ask reviewers to identify requirement, six boundaries, domain outcome, transaction, blocking model, migration, tests, operational signal, rollback, and the borderline flip condition. The good and bad properties are direct playbook guidance. One endpoint cannot establish universal architecture or framework APIs.

**Second-order consequence.** A borderline example is useful when it names the future invariant or scale trigger that would require stronger separation.

**Revision decision.** Replace circular examples with one create-account trace, failed shortcut, and bounded CRUD case.

**Retained seed evidence.** The good, bad, and borderline labels remain while their backend consequences become comparable. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Kotlin Backend Playbook Reference after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Kotlin Backend Playbook Reference as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Kotlin Backend Playbook Reference only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide how to tell whether the playbook improves delivery reliability without rewarding speed or architecture volume. The seed measures completion within one focused session and guessed framework behavior, but it omits requirement traceability, escaped boundary defects, migration safety, timeout/cancellation behavior, rollback, and operational outcomes.

**Recommended default and causal basis.** Track requirement-to-test coverage, boundary defects found before rollout, escaped contract errors, migration rehearsal, timeout and cancellation outcomes, duplicate-write prevention, rollback readiness, saturation signals, review effort, and lead time by comparable feature class. These measures connect explicit design to safer behavior rather than treating one-session completion or more layers as success.

**Operating conditions and assumptions.** The feedback loop works with stable task classes, baselines, service ownership, review windows, and corrective actions. Metrics cannot replace service-specific SLOs or justify unnecessary abstractions.

**Failure boundary and alternatives.** It fails when faster means skipped integration tests, more types means quality, or no incident means an untested path is safe. Bounded alternatives and recoveries: Use qualitative delivery retrospectives, paired reviews, defect taxonomies, requirement trace audits, or later operational outcome review.

**Counterexample, gotchas, and operational comparison.** Small samples, survivor bias, test-environment mismatch, reviewer familiarity, and changes in traffic can distort conclusions. Good: record that cancellation testing caught a pool-saturation bug before rollout. Bad: celebrate same-day delivery. Borderline: track traceability and rollback while a service-level outcome baseline develops.

**Verification, evidence, and uncertainty.** Define metric, denominator, task class, sample, reviewer, environment, exclusions, uncertainty, threshold, action, and later invalidations. Executable requirements and boundary tests are direct playbook quality mechanisms. No corpus evidence supplies universal targets or causal effect sizes.

**Second-order consequence.** A playbook can increase design time while reducing total lead time by preventing cross-boundary rework and rollback.

**Revision decision.** Replace generic speed language with requirement, boundary, migration, resilience, rollback, and downstream outcome feedback.

**Retained seed evidence.** The seed leading and failure signals remain as broad diagnostics within a fuller measurement chain. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: lead time from requirement to verified endpoint stays under one focused implementation session.
Failure signal: framework choice or coroutine behavior is guessed instead of verified with tests and docs.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide whether a Kotlin backend design is complete enough to implement or deploy for its declared scope. The seed checks generic reference artifacts but omits the playbook's executable requirement, six boundaries, framework, types, errors, transactions, coroutines, clients, migrations, API, tests, and rollout evidence.

**Recommended default and causal basis.** Require existing-framework evidence, versioned requirement, six-boundary map, request and response contracts, domain invariants, expected errors, transaction scope, persistence and migration, blocking model, deadlines, retry/idempotency, validation, observability, tests, rollout, rollback, and NFR evidence. A fluent design can hide the exact cross-boundary omission that fails under production load or adverse input.

**Operating conditions and assumptions.** The checklist works when critical omissions block transition and waivers state authority, reason, and compensating evidence. Complete-for-scope is not proof of production readiness without environment-specific validation.

**Failure boundary and alternatives.** It fails as a memory list, when all items are mandatory for pure domain work, or when boxes lack tests and code locations. Bounded alternatives and recoveries: Use a compact checklist for one boundary, schema validation for the dossier, architecture tests, or risk-weighted review.

**Counterexample, gotchas, and operational comparison.** Checklist theater, stale framework assumptions, happy-path-only tests, hidden external calls, and unowned metrics create false completeness. Good: mark no transaction for an external-only read and justify it. Bad: mark coroutines safe because the handler is suspend. Borderline: waive explicit mappers for CRUD-only scope with an exit trigger.

**Verification, evidence, and uncertainty.** Remove one critical artifact or test and confirm the implementation/deployment gate identifies the affected requirement and failure. Every checklist item maps to direct playbook guidance. Criticality and waiver policy depend on feature scope and service risk.

**Second-order consequence.** Checklist order should follow the request path so early contract errors are found before adapter and runtime polish.

**Revision decision.** Add all six boundaries, executable behavior, operational evidence, and waiver semantics to the retained checklist.

**Retained seed evidence.** The seven generic seed checks remain beneath the Kotlin delivery gate. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Kotlin Backend Playbook Reference.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when the service-level playbook should hand off to testing fixtures, framework APIs, security analysis, runtime operations, database migration, or distributed-workflow guidance. The seed points vaguely to runtime, security, testing, Kotlin, backend, and playbook references without naming pivots, handoff evidence, or return conditions.

**Recommended default and causal basis.** Keep cross-boundary service design here; route when one specialized uncertainty dominates, carrying requirement IDs, affected boundaries, code paths, tests, dependency versions, risks, and rollback conditions. Evidence-bearing handoffs prevent specialized guidance from losing the service contract or reopening settled framework choices.

**Operating conditions and assumptions.** Routing works when the destination has a distinct job and explicit stop or return condition. A handoff cannot authorize framework migration or relax user scope.

**Failure boundary and alternatives.** It fails when keywords choose the route, fixture mechanics replace behavior design, or day-two operations begin without a verified contract. Bounded alternatives and recoveries: Route to Kotlin testing fixtures, current Spring/Ktor docs, security abuse-case guidance, runtime observability, persistence migration, or distributed transaction design.

**Counterexample, gotchas, and operational comparison.** Context loss, duplicated design, incompatible framework assumptions, broadened permissions, and conditional findings becoming unconditional code can fragment delivery. Good: hand the create-account requirement and repository ports to fixture guidance. Bad: ask a testing reference to choose transaction scope. Borderline: return from a framework API lookup to reconcile the service dossier.

**Verification, evidence, and uncertainty.** Record pivot, destination, evidence packet, dependency versions, unresolved question, owner, expected output, stop condition, return path, and changed decision. The playbook defines service-level shape before framework detail, supporting specialization after boundaries are known. Available adjacent references and packet formats vary by workspace.

**Second-order consequence.** Routing is correct when it closes one boundary uncertainty while preserving end-to-end behavior and rollback.

**Revision decision.** Replace placeholder adjacency with boundary-triggered, evidence-preserving routes.

**Retained seed evidence.** The broad adjacent categories remain as destinations with concrete pivots. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use runtime, security, or testing Kotlin references when the question is about day-two operation, abuse cases, or fixtures.
Adjacent reference 1: consider the kotlin adjacent reference when the current task pivots away from kotlin backend playbook reference.
Adjacent reference 2: consider the backend adjacent reference when the current task pivots away from kotlin backend playbook reference.
Adjacent reference 3: consider the playbook adjacent reference when the current task pivots away from kotlin backend playbook reference.

## Workload Model

**Decision supported.** This section helps decide how much Kotlin backend change one playbook review can coordinate coherently. The seed fixes one service, twenty-five endpoints, one thousand requests, and one rollback path without calibration, ignoring boundary coupling, migration risk, external effects, and ownership.

**Recommended default and causal basis.** Center one service boundary and one release objective; batch endpoints or workers only when they share contracts, persistence, execution model, owner, and rollback; split when migrations, external workflows, or ownership create independent failure domains. Endpoint count and synthetic request count do not measure architecture coupling or operational review capacity.

**Operating conditions and assumptions.** The model works for one coherent service change with explicit owners and a testable rollback. Parallel work needs exclusive ownership and cannot redefine shared contracts independently.

**Failure boundary and alternatives.** It fails across independent services, multiple schema timelines, mixed blocking/reactive stacks, or several teams racing shared contracts. Bounded alternatives and recoveries: Narrow to one vertical slice, split by boundary or release, use hierarchical review, or create separate migration and runtime plans.

**Counterexample, gotchas, and operational comparison.** A small endpoint count can hide one dangerous migration, while many uniform reads can be reviewed together safely. Good: review five routes sharing one command and transaction. Bad: batch twenty-five unrelated workers. Borderline: group endpoints only when one rollout and rollback covers them.

**Verification, evidence, and uncertainty.** Record shared requirements, boundary graph, schema impact, external dependencies, execution model, owners, rollout, rollback, test load, and split rationale. One service boundary and explicit rollback are sound concepts; the seed's numeric caps are not evidenced. No universal endpoint, request, or reviewer count defines capacity.

**Second-order consequence.** Review capacity is bounded by coupled failure modes and rollback coherence, not by source or endpoint totals.

**Revision decision.** Replace fixed counts with service coupling, migration, execution, ownership, and rollback boundaries.

**Retained seed evidence.** The workload rows remain as inherited heuristics with unsupported quantities qualified. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Kotlin Backend Playbook Reference as a backend service operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | service implementation, route review, worker execution, and operational hardening work where a single wrong recommendation can affect live request handling | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one service boundary, up to 25 endpoints or workers, 1000 representative requests, and one deploy rollback path per review batch | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Kotlin Backend Playbook; Service Anatomy; Framework Choice; Executable Requirements; REQ-KOTLIN-BACKEND-001.0: Create Account Endpoint; Kotlin Domain  | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is request lifecycle diagram with persistence boundary, observability hook, and failure table | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which backend properties are hard invariants and which outcomes need service-specific calibration. The seed mixes evidence labels, an uncalibrated eighteen-of-twenty routing sample, zero unsupported claims, and recovery coverage without Kotlin contract, transaction, coroutine, migration, or rollback controls.

**Recommended default and causal basis.** Make requirement traceability, stable error mapping, explicit transaction scope, named blocking behavior, bounded external calls, retry classification, idempotent writes, migration compatibility, deny-by-default security, observability, and rollback hard controls; calibrate latency and availability per service. Contract and safety invariants can be audited, while operational targets depend on traffic, infrastructure, and business criticality.

**Operating conditions and assumptions.** This model works when the service, environment, denominator, reviewer, and corrective action are explicit. Do not turn inherited samples or local test latency into production guarantees.

**Failure boundary and alternatives.** It fails when one hundred percent means superficial labels, eighteen of twenty implies universal accuracy, or fixed p95/p99 values replace an SLO. Bounded alternatives and recoveries: Use severity-weighted audits, integration fixtures, load profiles, confidence calibration, chaos or failure tests, and later incident review.

**Counterexample, gotchas, and operational comparison.** Green tests can share production's wrong assumptions, latency can hide saturation, and retry success can mask duplicate side effects. Good: hard-fail an unbounded client and separately measure service latency. Bad: claim ninety-percent reliability. Borderline: exhaustive traceability only for action-controlling requirements.

**Verification, evidence, and uncertainty.** Retain raw results, requirement IDs, boundary coverage, environment, load, errors, transaction evidence, migration state, reviewer, uncertainty, and later corrections. The hard controls are direct playbook requirements; seed quantitative targets lack methodology. No local evidence establishes universal reliability rates or SLOs.

**Second-order consequence.** A reliable backend makes failure explicit and recoverable before optimizing steady-state success.

**Revision decision.** Classify seed targets and add Kotlin contract, coroutine, persistence, security, observability, and rollback reliability.

**Retained seed evidence.** The original target rows remain with evidence classes and calibration limits. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide how to diagnose a Kotlin backend failure at the earliest causal boundary and choose a bounded recovery. The seed includes source drift, generic advice, request surge, and security assumptions but omits stage-specific failures across the six service boundaries.

**Recommended default and causal basis.** Classify transport validation/auth, application choreography/idempotency, domain invariant/error, persistence/transaction/migration, integration timeout/retry, and runtime config/saturation/rollback failures separately. Adding retries cannot fix a domain invariant, and controller changes cannot repair a transaction or migration defect.

**Operating conditions and assumptions.** The taxonomy works when each mode has a reproducible signal, containment, prior valid state, owner, and recheck. Stop rollout when the failed boundary affects contract, data integrity, security, or recoverability.

**Failure boundary and alternatives.** It fails when every problem is called framework behavior, when expected domain outcomes and infrastructure exceptions are conflated, or when all layers are rewritten. Bounded alternatives and recoveries: Reject at the edge, revise command validation, restore an invariant, narrow transaction scope, roll migration, isolate blocking work, disable retry, or rollback release.

**Counterexample, gotchas, and operational comparison.** Failures cascade: malformed input reaches domain code, an exception escapes transport mapping, retries repeat a non-idempotent write, and saturation obscures the original cause. Good: detect pool saturation from blocking calls and isolate the dispatcher. Bad: increase timeouts. Borderline: reopen architecture only when failure exposes a boundary mismatch.

**Verification, evidence, and uncertainty.** Reproduce, identify earliest boundary, change one cause, compare behavior and telemetry, rerun downstream tests, and record residual risk. Every class maps directly to the six-boundary model and playbook cautions. Failure frequency and severity require service data.

**Second-order consequence.** Boundary-aware diagnosis preserves valid code and avoids treating concise Kotlin syntax as the unit of failure.

**Revision decision.** Expand the table into a six-boundary causal taxonomy with containment and recheck.

**Retained seed evidence.** The seed failures remain as cross-cutting symptoms inside a precise backend model. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| request surge overloads path | traffic spikes exceed handler, pool, or coroutine limits | apply rate limits, queue bounds, cancellation, and rollback playbook before rollout |
| security boundary silently fails | auth, permission, or input validation assumptions are untested | run abuse-case tests and require explicit deny-by-default behavior |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a Kotlin backend operation may retry and what backpressure prevents duplicate effects or saturation. The seed offers one stale-evidence retry and generic checkpoints but does not distinguish external-call retries from request, transaction, worker, or migration recovery.

**Recommended default and causal basis.** Retry only classified transient external or broker failures with bounded attempts, deadlines, jitter where appropriate, cancellation, idempotency or deduplication, and observable exhaustion; never blindly retry domain failures or whole transactions. A retry repeats effects and consumes pools, so correctness depends on failure class, idempotency, and capacity rather than optimism.

**Operating conditions and assumptions.** It works for timeouts or transient provider failures where the write is idempotent and the budget fits the parent deadline. Retries cannot bypass business rules, security, parent cancellation, or service SLO budgets.

**Failure boundary and alternatives.** It is wrong for validation, authorization, invalid state, duplicate business outcomes, unknown commit status without idempotency, or overloaded dependencies. Bounded alternatives and recoveries: Fail fast, return a stable error, enqueue durable work, use outbox/deduplication, apply rate limits, shed load, pause a consumer, or require operator recovery.

**Counterexample, gotchas, and operational comparison.** Retries inside database transactions, multiplicative layers, uncancelled children, fixed delays, and hidden queue growth can amplify incidents. Good: retry a timeout-bound idempotent provider call twice within the request deadline. Bad: retry create-account after an unknown commit. Borderline: worker redelivery is safe only with deduplication and poison-message handling.

**Verification, evidence, and uncertainty.** Record failure class, attempt budget, deadline, idempotency key, transaction boundary, queue depth, saturation signal, cancellation result, exhaustion behavior, and rollback. Timeouts, retry classification, idempotency, durable queues, and outbox guidance are direct playbook facts. Exact attempts, delays, and thresholds are service-specific.

**Second-order consequence.** Backpressure is part of correctness because uncontrolled concurrency can turn transient failure into data corruption or systemic saturation.

**Revision decision.** Replace generic retry text with failure-class, idempotency, deadline, capacity, and durable-work controls.

**Retained seed evidence.** The seed's bounded-retry intent remains under backend-specific semantics. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what telemetry lets operators and reviewers connect runtime behavior back to the executable requirement and failing boundary. The seed records sources, proofs, percentiles, errors, retries, saturation, and rollback but omits requirement IDs, six-boundary ownership, transaction and dispatcher context, dependency budgets, migration version, and stable error outcomes.

**Recommended default and causal basis.** Record requirement and operation IDs, route/worker, outcome code, latency, error class, transaction result, dispatcher or pool, dependency timeout/retry, queue depth, saturation, migration version, health, rollout cohort, and rollback trigger with controlled cardinality. Boundary-aware signals distinguish domain rejection from infrastructure failure and local slowness from dependency or pool saturation.

**Operating conditions and assumptions.** It works when names, units, labels, sampling, and ownership are stable and sensitive data is excluded. Never expose secrets or personal data and do not claim observability coverage without exercised signals.

**Failure boundary and alternatives.** It fails when logs are unstructured, metrics have unbounded labels, traces omit asynchronous hops, or alerts lack an action and rollback. Bounded alternatives and recoveries: Use a minimal structured log set, RED/USE metrics, trace sampling, audit events, or risk-tiered telemetry.

**Counterexample, gotchas, and operational comparison.** PII leakage, correlation-ID loss, coroutine context loss, misleading percentiles, duplicate retry errors, and health checks that ignore dependencies can mislead operations. Good: correlate HTTP 409 to a domain outcome without logging email. Bad: log exception text and payload. Borderline: omit tracing for a tiny service but retain structured outcomes and pool saturation.

**Verification, evidence, and uncertainty.** Replay representative success, expected failure, timeout, cancellation, retry exhaustion, migration issue, and rollback; confirm signal, cardinality, redaction, owner, and action. Runtime config, logging, metrics, health, rollback, and seed signals are direct concerns. Tooling, retention, and alert thresholds vary by environment.

**Second-order consequence.** Observability completes the domain model by showing whether expected outcomes and infrastructure failures remain distinguishable in production.

**Revision decision.** Convert the generic checklist into a requirement- and boundary-linked telemetry contract.

**Retained seed evidence.** The seed's compact evidence signals remain and gain Kotlin request-path context. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture error count, timeout count, retry count, saturation signal, and rollback trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to verify Kotlin backend performance without turning arbitrary local latency into a production promise. The seed prescribes local p95 under 200 ms and p99 under 500 ms absent an SLO, which is unsupported and ignores workload, environment, blocking pools, dependencies, and correctness guards.

**Recommended default and causal basis.** Start from a service-specific SLO and representative workload; measure end-to-end and boundary latency, throughput, errors, allocations where relevant, dispatcher and connection-pool saturation, dependency budgets, cancellation, and correctness under load. Latency percentiles are meaningful only with a workload, sample, environment, warmup, and quality constraints.

**Operating conditions and assumptions.** The method works when traffic mix, data size, concurrency, environment, SLO, and rollback threshold are explicit. Never publish local measurements as production SLO compliance without representative evidence.

**Failure boundary and alternatives.** It fails on one-run percentiles, mocked dependencies, tiny data, no warmup, hidden retries, or latency improvement that breaks correctness. Bounded alternatives and recoveries: Use direct timing for one run, microbenchmarks for pure code, integration load tests, capacity tests, profiling, or document that latency is not decision-relevant.

**Counterexample, gotchas, and operational comparison.** JIT warmup, GC, coroutine scheduling, pool queues, cold caches, coordinated omission, and test-profile differences can distort results. Good: test representative create-account traffic with database contention and duplicate outcomes. Bad: time a mocked controller. Borderline: provisional local timing is acceptable only as non-SLO diagnostic evidence.

**Verification, evidence, and uncertainty.** Record SLO, workload, dataset, concurrency, environment, versions, warmup, sample, percentiles, errors, saturation, retries, exclusions, and regression action. The playbook requires evidence for NFRs and names blocking/pool effects; the seed's fixed thresholds lack evidence. No universal Kotlin backend latency target exists.

**Second-order consequence.** Performance validation is boundary diagnosis under load, not a stopwatch around handler code.

**Revision decision.** Remove the fixed fallback thresholds and define SLO-led, boundary-aware measurement.

**Retained seed evidence.** The inherited measurement packet remains while unsupported latency precision is rejected. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require a service-specific SLO before deployment; absent that, keep local verification to p95 under 200 ms and p99 under 500 ms for representative handlers or document why latency does not apply.
Leading indicator to measure: lead time from requirement to verified endpoint stays under one focused implementation session.
Failure signal to watch: framework choice or coroutine behavior is guessed instead of verified with tests and docs.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when one playbook instance must split and how distributed work preserves service contracts and rollout safety. The seed names multiple systems, ownership boundaries, unbounded discovery, production traffic, and context drift but does not define Kotlin service, schema, workflow, or execution-model decomposition.

**Recommended default and causal basis.** Split by independent service, schema migration, external workflow, or runtime failure domain after shared requirements, contracts, compatibility rules, owners, rollout order, and rollback are explicit; keep one integrator for cross-boundary behavior. Parallel implementation scales disjoint adapters but can fragment transactions, error contracts, migrations, and operational ownership.

**Operating conditions and assumptions.** It works when writes are disjoint, interfaces versioned, dependencies ordered, and integration gates exist. Distributed work cannot silently change shared public contracts or framework strategy.

**Failure boundary and alternatives.** It fails with shared entities, one transaction, coupled schema changes, mixed blocking/reactive decisions, or multiple owners editing the same contract. Bounded alternatives and recoveries: Narrow to one vertical slice, use sequential migration, hierarchical review, centralize coupled work, or parallelize read-only investigation.

**Counterexample, gotchas, and operational comparison.** Contract drift, migration races, incompatible error envelopes, duplicate idempotency logic, and rollout ordering can create distributed defects. Good: split client adapter and observability after the service contract is fixed. Bad: let teams redefine domain outcomes. Borderline: separate services but preserve a shared compatibility matrix.

**Verification, evidence, and uncertainty.** Produce dependency graph, requirement ownership, contract versions, exclusive paths, migration order, integration tests, rollout cohorts, rollback map, and final reviewer. Boundary visibility, migration compatibility, and explicit ownership support these controls. No universal service, endpoint, or worker count marks scale.

**Second-order consequence.** Scale is reached when coordination and rollback coupling grow faster than useful parallelism.

**Revision decision.** Add service, schema, workflow, execution, ownership, merge, rollout, and rollback boundaries.

**Retained seed evidence.** The generic scale cautions remain and become a Kotlin service delivery architecture. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Kotlin Backend Playbook Reference stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide how future authorized research should refresh the exact dependency behavior controlling a backend decision. The seed uses broad best-practice, repository-example, and release-note searches that cannot verify a named Kotlin, coroutine, Spring, Ktor, persistence, or migration claim.

**Recommended default and causal basis.** Form claim-first queries against current primary Kotlin, kotlinx.coroutines, Spring, Ktor, database, and persistence documentation, including dependency version, execution model, and disputed API. Version-specific research is falsifiable and prevents popular examples from defining framework or runtime semantics.

**Operating conditions and assumptions.** It works when browsing is authorized, repository versions are known, and a local reproduction follows source review. Future browsing requires authorization and cannot justify incidental migration.

**Failure boundary and alternatives.** It fails with generic theme searches, snippets, unversioned examples, cross-framework results, or release notes unrelated to installed dependencies. Bounded alternatives and recoveries: Use build dependency reports, source code, generated API docs, local compile tests, framework help, or state a freshness gap.

**Counterexample, gotchas, and operational comparison.** Preview APIs, bridge libraries, BOM versioning, deprecations, Enterprise constraints, and copied samples can hide mismatch. Good: query current cancellation behavior for the installed coroutine version. Bad: search 'Kotlin backend best practices.' Borderline: use a repository example to form a test, not as sole proof.

**Verification, evidence, and uncertainty.** Record claim, query, authorization, date, dependency version, source class, locator, selected and rejected results, reproduction, contradiction, and guidance change. The seed source categories identify appropriate primary families. No query was run now and future behavior may change.

**Second-order consequence.** Refresh should target the boundary most capable of invalidating the design, not collect general ecosystem advice.

**Revision decision.** Retain query labels but replace their text with versioned, framework-matched, claim-oriented templates.

**Retained seed evidence.** The generic query rows remain as weak seeds under stricter research guidance. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | kotlin backend playbook reference official documentation best practices |
| `github_repository_query_phrase` | kotlin backend playbook reference GitHub repository examples |
| `release_notes_query_phrase` | kotlin backend playbook reference changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how every action-controlling backend claim exposes provenance, environment, confidence, and invalidation. The seed distinguishes local, external, and inference labels but omits repository convention, executable requirement, framework-version fact, test observation, benchmark, production signal, user constraint, and unresolved assumption.

**Recommended default and causal basis.** Label local playbook rule, repository convention, user requirement, current framework fact, code observation, test result, migration result, benchmark, production signal, reasoned inference, unresolved assumption, confidence, and invalidation trigger at claim level. A plausible recommendation can launder archived guidance, sample code, or local timing into a production guarantee unless evidence classes remain distinct.

**Operating conditions and assumptions.** It works when claims are atomic, versions and environments recorded, and labels propagate into plans and reviews. Expose explicit evidence without leaking secrets, sensitive payloads, or unsupported certainty.

**Failure boundary and alternatives.** It fails when one section label covers mixed claims, tests are generalized beyond environment, or repository convention is called idiomatic truth. Bounded alternatives and recoveries: Use inline citations, provenance columns, requirement trace matrices, evidence ledgers, or a separate appendix.

**Counterexample, gotchas, and operational comparison.** Duplicate sources, stale dependency versions, test-profile mismatch, benchmark halo, silent deviations, and downstream label loss are principal risks. Good: label transaction placement a playbook rule, annotation behavior a tested Spring fact, and latency a local benchmark. Bad: call 200 ms a service SLO. Borderline: section-level labels only when source, version, and environment are uniform.

**Verification, evidence, and uncertainty.** Sample final claims and reconstruct requirement, source, version, code path, environment, test, contrary evidence, confidence, and invalidation condition. The playbook directly requires evidence for NFRs and separates service concerns. Correct labels do not prove a source, test, or inference is sufficient.

**Second-order consequence.** Fine-grained boundaries make upgrades and incidents local: changed framework behavior invalidates identifiable claims rather than the whole design.

**Revision decision.** Extend the three seed labels into a claim-level Kotlin backend evidence grammar.

**Retained seed evidence.** The original evidence labels remain as a compatible subset of richer delivery evidence. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
