# Rust Backend Playbook Reference

**Decision supported.** This section helps decide which structural doctrine a Rust backend task adopts before any handler code is written. The seed title promises a backend playbook but the seed never states the playbook's organizing claim, the 81-line mapped file structures every service as five layers, transport, handler, domain, persistence, and integration, each narrow enough that failures have an obvious owner.

**Recommended default and causal basis.** Treat every backend request path as the five named layers, keep each narrow, and decide inline-versus-worker before coding long-running paths. The five layers exist to give every failure an owner, parsing failures belong to transport, orchestration and error mapping to handlers, invariants to domain types, transactions to persistence, and remote-system risk to typed clients, so debugging becomes a routing problem instead of a search.

**Operating conditions and assumptions.** The task is an Actix, Axum, or similar Rust web service touching endpoints, app state, persistence, external integrations, or worker flows, per the parent skill's description. This reference governs Rust HTTP backend service shape, the parent skill's guardrails route generic Rust libraries, CLIs, parsers, and FFI work to rust-executable-specs-01 or rust-coder-02 instead.

**Failure boundary and alternatives.** Reading the playbook as framework advice misses its point, actix-web, axum, tokio, sqlx, and reqwest appear only as representative ecosystem examples, the layer boundaries are the doctrine and survive any crate swap. Bounded alternatives and recoveries: the parent SKILL.md's mode-driven workflow for readers who need task classification and executable requirements before anatomy, it wraps this playbook as step two of its context strategy.

**Counterexample, gotchas, and operational comparison.** The playbook covers anatomy only, auth, retries, deployment, and testing depth live in its three sibling references, treating this one file as the whole delivery story leaves security and rollout unplanned. Good: a new endpoint designed as five explicit layers with the worker split decided up front. Bad: business rules buried in extractor glue because the layers were never drawn. Borderline: a tiny internal service collapsing handler and domain layers, defensible at toy scale, the failure-ownership property quietly disappears.

**Verification, evidence, and uncertainty.** Walk a request end to end and name the owning layer for each step, any step with no obvious owner marks a boundary the design still owes. Full read this session of the 81-line playbook plus its four sibling bundle files. Whether the five-layer cut stays ideal for streaming or websocket-heavy services is beyond what the mapped file discusses.

**Second-order consequence.** The playbook is the anatomy volume of a four-reference bundle, testing, runtime-ops, and security-resilience each elaborate one region of the same five-layer body, which is why the reference map routes every task type through the playbook eventually.

**Revision decision.** Open with the five-layer anatomy and its failure-ownership rationale so readers know the playbook is a boundary discipline, not a crate catalog.

**Retained seed evidence.** The exact theme title and playbook framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which file or link may justify each class of claim in this theme. The seed table maps one local row and four external rows, but the single local file is one chapter of a five-file bundle whose SKILL.md, reference map, and three sibling references carry the modes, testing, operations, and security guidance this theme repeatedly needs.

**Recommended default and causal basis.** Cite the playbook for anatomy and boundary claims, the named sibling file for testing, ops, or security claims, and external rows only as candidate pointers. The seed's mapping scoped only the playbook file, so claims about modes, harnesses, migrations, or idempotency must cite the sibling files by name rather than lean on the one mapped row.

**Operating conditions and assumptions.** The archive bundle stays intact at its 202604 path so by-name sibling citations remain resolvable. The table records provenance for this document's claims, it does not certify that the four GitHub and docs.rs URLs resolve or describe current crate behavior.

**Failure boundary and alternatives.** Citing the playbook row for a claim that actually lives in a sibling file, spawned-app harnesses or zero-downtime migrations, misattributes evidence even though the bundle is one lineage. Bounded alternatives and recoveries: expanding the mapped set to the whole bundle in a future revision, which would make sibling citations first-class rows instead of by-name mentions.

**Counterexample, gotchas, and operational comparison.** All four external rows are unretrieved, the api-guidelines, tokio, and axum links are plausible anchors for the playbook's ecosystem examples but none was fetched during this evolution. Good: citing the playbook's section 6 for the worker-split rule. Bad: asserting current axum extractor behavior from the unretrieved docs.rs row. Borderline: citing SKILL.md for a mode default, correct by name, invisible in the seed's mapped table.

**Verification, evidence, and uncertainty.** Check each claim's citation against the file that actually contains it, playbook section numbers for anatomy, sibling titles for everything else. Full reads this session of all five bundle files and the reference map. Whether the corpus intends single-file mapping as a deliberate scope cut or an extraction artifact is not recorded.

**Second-order consequence.** The one-row local map understates the theme by four files, which the seed's own hierarchy confidence warning almost admits, this evolution treats the bundle as context while honoring the single mapped anchor.

**Revision decision.** Keep the playbook as the mapped anchor row and name the four sibling bundle files explicitly wherever their content is used.

**Retained seed evidence.** The single local row and all four external rows with their column values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/rust-web-backend-playbook.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://github.com/rust-lang/api-guidelines | external_research_source_material | external_research_sourced_fact | Rust library-team API design recommendations |
| https://github.com/tokio-rs/tokio | external_research_source_material | external_research_sourced_fact | async runtime implementation and operational model |
| https://github.com/tokio-rs/axum | external_research_source_material | external_research_sourced_fact | Rust web framework implementation and design claims |
| https://docs.rs/axum/latest/axum/ | external_research_source_material | external_research_sourced_fact | published crate documentation for routing and extractors |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which playbook doctrine a constrained Rust backend effort adopts first. The seed scores three document-hygiene rules while the playbook carries unscored but clearly ranked doctrine, layer separation first, edge validation second, transaction ownership third, typed clients fourth, and the worker split as the closing judgment call.

**Recommended default and causal basis.** Adopt layer separation and edge validation before optimizing anything else, they are the two doctrines every later rule presumes. The playbook orders its sections by request flow, transport to integration, and its bundle's reference map orders reading by risk surface, so priority in this theme is positional and mode-driven rather than numerically scored.

**Operating conditions and assumptions.** The service is being designed or refactored, a pure operations incident routes to the runtime-ops sibling before any anatomy work. This ranking orders the playbook's structural doctrines for adoption, the sibling files' testing, ops, and security rules carry their own internal orderings.

**Failure boundary and alternatives.** Treating the seed's 95, 91, and 88 as measured backend data fabricates evidence, they are the corpus template's authorial emphasis and say nothing about Rust service reliability. Bounded alternatives and recoveries: the parent skill's mode table, which prioritizes by declared risk, ambiguity, delivery, operations, security, or resilience, rather than by request flow.

**Counterexample, gotchas, and operational comparison.** The worker split reads like an optional appendix but gates correctness, a slow remote call kept inline holds client connections open and turns retries into duplicate side-effects. Good: a refactor that draws layer boundaries before touching handler bodies. Bad: tuning connection pools while unchecked strings travel through the core. Borderline: adopting typed clients before edge validation on an integration-heavy service, defensible when remote risk dominates.

**Verification, evidence, and uncertainty.** Check adoption order against the playbook's section sequence and the reference map's mode routing before citing priority. The playbook's six-section structure and the reference map's mode table read in full. No measurement validates the flow ordering, it is one bundle's authorial calibration from 202604.

**Second-order consequence.** The playbook's section order doubles as a review order, walking a diff transport-first mirrors how a request meets the code, which is why the reference map sends Review Mode readers back through the playbook last, after risk files.

**Revision decision.** State the flow-ordered doctrine list as the operative priority and keep the seed rows as corpus-process guidance.

**Retained seed evidence.** The three scored seed rows with tier labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `rust_backend_playbook_reference` | 95 | default_adoption_pattern_tier | Source Map First: Load local rust backend material before synthesizing playbook reference recommendations. |
| `rust_backend_playbook_reference` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `rust_backend_playbook_reference` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what organizing principle new Rust backend guidance for this theme must satisfy. The seed recites the generic load-local-first formula while the bundle's real thesis is sharper, reliable Rust backends come from narrow layer boundaries with obvious failure owners, typed values crossing every edge, and deliberate inline-versus-durable work decisions.

**Recommended default and causal basis.** Test any proposed backend guidance against the three clauses before adopting it into this theme. Each thesis clause anchors one playbook section, narrow boundaries in section 1, typed edges in section 3, and the durability decision in section 6, while the parent skill's guardrails restate the same clauses as prohibitions.

**Operating conditions and assumptions.** The service has genuine persistence and remote integrations, a stateless proxy exercises the boundary clauses but leaves the durability clause mostly idle. The thesis governs service anatomy and boundary discipline, spec-writing, verification mix, and rollout sequencing are the parent skill's workflow concerns layered on top.

**Failure boundary and alternatives.** A thesis reduced to use typed values misses the ownership half, types without narrow layers still let one handler own parsing, business rules, and SQL at once, and failures again have no obvious owner. Bounded alternatives and recoveries: a spec-first framing that leads with REQ-WEB contracts and treats anatomy as derived, the parent skill supports it through Spec Mode for vague requests.

**Counterexample, gotchas, and operational comparison.** The thesis presumes async Rust norms, shared clients and pools in app state, blocking work kept off the request executor, violating those norms breaks the clauses in ways the playbook only implies. Good: rejecting a helper that parses raw strings deep in the core, it violates the typed-edge clause. Bad: adopting a queue because queues are modern with no durability reasoning. Borderline: accepting an inline slow call with an explicit tradeoff note, the guardrails permit it only when the tradeoff is stated.

**Verification, evidence, and uncertainty.** Trace each clause to its playbook section and confirm proposed guidance names which clause it serves. The playbook's sections 1, 3, and 6 and the parent skill's guardrails read in full. Whether the three clauses stay complete for event-sourced or streaming architectures is beyond the mapped material.

**Second-order consequence.** The parent skill compresses the same thesis operationally, decision-complete work packets that are spec-first, service-aware, and production-biased, its three adjectives map onto requirements, anatomy, and rollout in that order.

**Revision decision.** Restate the thesis as three clauses, narrow owned layers, typed edges, deliberate durability, each traceable to its playbook section.

**Retained seed evidence.** The three labeled thesis statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `rust_backend_playbook_reference` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Rust Backend Playbook Reference comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which bundle file a given Rust backend question should open first. The seed map lists the playbook alone with its heading signals, hiding that the playbook is the anatomy chapter of a five-file bundle routed by a dedicated reference map with mode-specific read orders.

**Recommended default and causal basis.** Classify the incoming question as shape, verification, operations, or security-resilience, then open the playbook only for shape and route the rest by the bundle's map. The bundle partitions by risk surface, the playbook answers shape questions, testing-and-fixtures answers verification questions, runtime-and-ops answers deployment and config questions, and security-and-resilience answers auth and retry questions, with reference-map.md as the router.

**Operating conditions and assumptions.** Questions arrive separable by risk surface, mixed tasks follow the map's task-type read orders instead. This map routes into the local bundle, external ecosystem documentation is the external map's subject.

**Failure boundary and alternatives.** A reader who treats the one mapped path as the whole corpus will answer security and migration questions from an anatomy file that deliberately excludes them. Bounded alternatives and recoveries: reading all five files sequentially for large unfamiliar tasks, the map's own default read order sanctions this at higher context cost.

**Counterexample, gotchas, and operational comparison.** Heading search lines in SKILL.md use references-relative paths that only resolve from the skill root, running them elsewhere returns empty and suggests missing sections. Good: routing a password-reset question straight to security-and-resilience per the map. Bad: hunting migration sequencing in the playbook, it lives in runtime-and-ops sections 7 and 8. Borderline: opening the playbook for a testing question, its REQ-WEB note gestures at specs, the harness detail is in the testing sibling.

**Verification, evidence, and uncertainty.** Spot-check the mapped heading signals against the live playbook and confirm sibling routing against reference-map.md's tables. Section-by-section reads of all five bundle files and the router this session. Whether future corpus revisions promote the siblings to mapped rows is a maintainer choice this map cannot settle.

**Second-order consequence.** The bundle's own context strategy is progressive, read the map first, the playbook second, then only the risk-relevant sibling, this theme inherits a reading discipline, not just content.

**Revision decision.** Annotate the playbook row as the anatomy chapter and name the router plus three sibling chapters with their question classes.

**Retained seed evidence.** The single local source row with title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/rust-web-backend-playbook.md | Rust Web Backend Playbook | Rust Web Backend Playbook; 1. Service Anatomy; 2. Request Handlers And App State; 3. Domain Types And Validation Boundaries; 4. Persistence Boundaries; 5. External API Client Boundary | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide what confidence external links may contribute to this theme's claims and which to fetch first. The seed map carries four plausible ecosystem anchors, api-guidelines, tokio, axum, and axum docs, yet none was retrieved during this evolution and the playbook itself cites crates only as representative examples, never through these URLs.

**Recommended default and causal basis.** Treat the axum docs row as the priority fetch for handler and extractor freshness questions and quote all rows only as candidate pointers. The playbook names actix-web, axum, tokio, sqlx, reqwest, and wiremock inline as ecosystem illustrations, so the external rows are the corpus template's best-guess anchors for those names rather than sources the bundle actually used.

**Operating conditions and assumptions.** The GitHub and docs.rs URL structures stay stable, docs.rs latest links float by design and must be version-pinned when cited. This map queues external verification targets, it grants no live-fact authority and cannot date any crate's current API.

**Failure boundary and alternatives.** Quoting the rows as live facts about current tokio or axum behavior fabricates freshness, every row is an unretrieved candidate until a dated fetch exists. Bounded alternatives and recoveries: reading a target repository's Cargo.lock and crate changelogs directly, which answers version-specific questions faster than general documentation.

**Counterexample, gotchas, and operational comparison.** The docs.rs latest URL is self-updating, a claim checked against it today may silently describe a different axum version at the next audit. Good: labeling a tokio runtime claim as candidate-anchored pending retrieval. Bad: asserting current axum extractor signatures from the unretrieved docs row. Borderline: citing api-guidelines for naming conventions, on-topic for Rust, tangential to this theme's service anatomy.

**Verification, evidence, and uncertainty.** Confirm externally-flavored claims carry unretrieved-candidate labels and no undated crate-behavior assertions. Zero external fetches recorded in this assignment's working notes. How far the 202604 crate landscape has moved is unknowable without the fetches these rows queue.

**Second-order consequence.** The notable absences are sqlx, reqwest, and wiremock links, three of the playbook's most operational crate examples have no external row at all, so the candidate queue is thinner than the theme's surface area.

**Revision decision.** Mark all four rows as unretrieved candidates and note the playbook's inline crate names as the local facts they would corroborate.

**Retained seed evidence.** All four external rows with their boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://github.com/rust-lang/api-guidelines | Rust API Guidelines | Rust library-team API design recommendations | external_research_sourced_fact |
| https://github.com/tokio-rs/tokio | Tokio repository | async runtime implementation and operational model | external_research_sourced_fact |
| https://github.com/tokio-rs/axum | Axum repository | Rust web framework implementation and design claims | external_research_sourced_fact |
| https://docs.rs/axum/latest/axum/ | Axum docs.rs | published crate documentation for routing and extractors | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which backend code behaviors this theme must reject on sight in review. The seed lists three generic documentation failures while the bundle names concrete backend rejections, business rules in extractor glue, clients constructed inside handlers, unchecked strings crossing the core, mixed transaction owners, per-request HTTP clients, and inline work that needed durable retries.

**Recommended default and causal basis.** Review backend diffs against the combined rejection set, prioritizing edge validation and transaction ownership, the two whose failures corrupt data rather than merely slow it. Each rejection inverts a playbook rule, extractor-glue logic inverts thin handlers, in-handler client construction inverts single wiring, raw strings invert edge conversion, and inline slow work inverts the worker split, so the registry is the playbook read in negative.

**Operating conditions and assumptions.** Reviews see handler, domain, and persistence context together, several rows are invisible in a single-file diff. This registry names Rust backend code failures, corpus-document process failures stay in the seed rows, and generic Rust style belongs to the sibling skills the guardrails name.

**Failure boundary and alternatives.** A registry without the backend rows cannot catch the failures this bundle exists to prevent, generic process checks pass a service whose secrets appear in logs and whose retries duplicate side-effects. Bounded alternatives and recoveries: lint and clippy automation for the mechanical rows, leaving transaction scope and failure shaping to human review, no lint sees a missing idempotency key.

**Counterexample, gotchas, and operational comparison.** Mixing durable-intent saves with remote side-effect calls is the subtlest row, it looks like straightforward sequential code and only fails when the remote call succeeds and the commit does not, or the reverse. Good: bouncing a handler that builds a reqwest client per request. Bad: approving a two-write workflow with no named transaction owner. Borderline: allowing a raw string user id in an internal admin tool, technically contained, the edge-conversion rule exists precisely because containment erodes.

**Verification, evidence, and uncertainty.** Cross-check each registry row against the playbook or sibling rule it inverts and confirm its detection signal works in an ordinary diff. The playbook's boundary rules and the security sibling's review checklist read in full. Relative base rates of these failures in real Rust services are unmeasured here, the ordering is authorial judgment.

**Second-order consequence.** The security sibling's review checklist is the registry in interrogative form, its seven questions, typed credentials, redacted logs, shaped failures, explicit transactions, defined idempotency, crash ambiguity, async candidacy, each detect one rejection class.

**Revision decision.** Import the bundle's rejections with detection signals, grep handlers for client construction and SQL, check logs for secret material, and check mutations for idempotency keys.

**Retained seed evidence.** The three seed process rows with their detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which commands and test layers constitute the verification gate for backend claims. The seed supplies only the corpus document verifier while the bundle defines a real gate stack, format, lint, tests, and build as the CI minimum, integration-first coverage through a spawned-app harness, HTTP mock tests with wiremock, and migration-aware tests when schema changes.

**Recommended default and causal basis.** Run the CI minimum on every change and add the matrix-assigned test types for each concern the diff touches. The testing sibling argues integration tests catch wiring, serialization, routing, and state-setup errors that unit tests structurally miss, so the gate mix is ordered by what each layer can see, not by execution speed.

**Operating conditions and assumptions.** The harness boots the app on a random port with isolated database state and auto-applied migrations, without that isolation the integration gates flake and lose authority. These gates verify Rust backend behavior and delivery quality, corpus document verification stays with the seed command, and generic Rust lint policy belongs to the repo.

**Failure boundary and alternatives.** Gates that stop at cargo test with unit coverage certify the layer backends break least, the expensive failures live at wiring, persistence, and remote boundaries that only harness and mock tests exercise. Bounded alternatives and recoveries: property-based tests for domain edges, the sibling endorses them selectively for constructors and round-trips, never as a substitute for end-to-end request tests.

**Counterexample, gotchas, and operational comparison.** Sharing test infrastructure without documenting the isolation boundary is the sibling's named trap, green suites over shared mutable state certify nothing about concurrent safety. Good: a new endpoint gated by a spawned-app test plus a wiremock contract test on its outbound call. Bad: certifying a migration by unit tests that never touch the schema. Borderline: skipping property tests on a trivial newtype, defensible, the constructor edge is where they pay most.

**Verification, evidence, and uncertainty.** Map each changed concern to its matrix row and confirm the assigned test type exists and runs in CI. The testing sibling's matrix and harness sections and SKILL.md's quality gates read in full. Whether the named tooling still reflects ecosystem defaults after 202604 is unverifiable without retrieval.

**Second-order consequence.** The testing sibling's matrix is a gate assignment table, each concern row, endpoint, domain invariant, database, remote API, auth flow, migration, names its preferred test type, so gate selection is a lookup rather than a debate.

**Revision decision.** Import the gate stack, CI four-gate minimum, spawned-app integration tests on endpoints, wiremock contract tests on clients, property tests on domain constructors, and migration tests when schema moves.

**Retained seed evidence.** The seed's document verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide what procedure an agent follows when a task requires the Rust backend bundle. The seed gives four generic bullets while the parent skill scripts a six-step workflow, classify the task and pick modes, write REQ-WEB requirements, design boundaries before coding, choose the verification mix, apply delivery rules, and run quality gates before handoff.

**Recommended default and causal basis.** Have agents execute the six steps literally, logging the chosen mode set and emitting the output contract in order. The ordering is load-bearing, mode selection scopes which references load, requirements precede design so acceptance is testable, and boundaries precede code so the verification mix has seams to target.

**Operating conditions and assumptions.** The task names a service slice, endpoint, auth flow, client, migration, worker, or review, so step one has something to classify. This guide scripts agent behavior over the backend bundle, in-pattern implementation detail belongs to the destination references.

**Failure boundary and alternatives.** An agent that skips step one loads the wrong references or all of them, and one that skips step two ships code whose success criteria were never stated, the workflow degrades worst from the top. Bounded alternatives and recoveries: embedding routed reference spans in recurring prompts for repetitive endpoint work, faster per task, frozen against bundle revisions.

**Counterexample, gotchas, and operational comparison.** The guardrails are part of the contract, an agent that completes all steps but recommends this skill for a parser or CLI has misrouted at the threshold, the description's not-for list is explicit. Good: an agent log showing Delivery plus Resilience modes, three REQ-WEB rows, and a traceability table. Bad: an agent generating handler code before any requirement or boundary decision exists. Borderline: skipping Spec Mode on a precisely specified endpoint, sanctioned when acceptance criteria already exist.

**Verification, evidence, and uncertainty.** Reject agent outputs missing the mode declaration, REQ-WEB identifiers, or the ordered output contract. SKILL.md's mode selection, workflow, output contract, and guardrails read in full. Whether six steps stay sufficient as the bundle grows more references is untested.

**Second-order consequence.** The output contract is the workflow made auditable, its seven ordered artifacts ending in open questions, plus the req-to-test traceability table, let a reviewer verify the steps ran without replaying the session.

**Revision decision.** Restate the guide as the six-step workflow with the mode table's default combinations, new endpoint takes Spec plus Delivery, auth takes Spec plus Security, migration takes Delivery plus Operations.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide whether the reader's current task matches a mode this reference serves and which entry it takes. The seed describes one generic reliability engineer while the bundle serves distinct mode-shaped journeys, a builder specifying a new endpoint, a security implementer on auth flows, an operator sequencing a migration, and a reviewer judging production readiness.

**Recommended default and causal basis.** Declare the mode first, then enter by the map's read order for that mode, and exit with a design or a verdict. The reference map assigns each journey its own read order, builders start at the playbook, security work starts at security-and-resilience, migrations start at runtime-and-ops, and reviews read risk files first and the playbook last.

**Operating conditions and assumptions.** The task is classifiable into the six modes, exploratory prototyping without acceptance criteria belongs in Spec Mode by definition. The journey covered runs from task-in-hand to read-order-chosen and design-decided, the coding between belongs to the destination references.

**Failure boundary and alternatives.** Forcing every journey through the same door misfires, a reviewer sent playbook-first reads anatomy while the diff's real questions, credential handling and rollback safety, wait in the files the map would have opened first. Bounded alternatives and recoveries: the map's default read order for large unfamiliar tasks, all files in sequence, when mode classification itself is uncertain.

**Counterexample, gotchas, and operational comparison.** Mixed journeys are the norm, the map's default combinations exist because auth work is rarely security-only, skipping the second mode's reading leaves half the risk surface unread. Good: a migration task entering at runtime-and-ops sections 7 and 8 and exiting with a sequenced rollout. Bad: a reviewer reading the playbook top to bottom while the diff's session-cookie handling goes unexamined. Borderline: a quick bugfix skipping mode selection, tolerable once, the habit erodes the routing discipline.

**Verification, evidence, and uncertainty.** Ask which mode the task declares and whether the files opened match the map's read order for it. The reference map's mode and task-type tables read in full. Median time from task receipt to correct mode selection has never been measured for this bundle.

**Second-order consequence.** The map's review order inverts the build order, builders go shape then risk, reviewers go risk then shape, encoding that review attention should land where production failures start, not where the code listing does.

**Revision decision.** Recast the scenario as mode-shaped entries with the map's read orders, keeping the seed's engineer as the Delivery Mode default.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Rust reliability engineer is starting from a requirement that needs a safe API, explicit error model, and testable boundary and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `rust_backend_playbook_reference` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the idiomatic ownership, async, error, and crate-boundary shape before coding.
Reference opening trigger: Open this file when the task mentions rust backend playbook reference, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how much durability machinery, type ceremony, and resource sharing each backend surface deserves. The seed offers generic adopt-adapt-avoid rows without this theme's live tensions, inline handling versus durable background work, transport-type convenience versus domain-type invariants, and shared long-lived resources versus per-request construction.

**Recommended default and causal basis.** Prefer inline handling, edge-converted domain types, and app-state-owned shared resources, deviating only where a section 6 criterion names the flip. The playbook resolves each tension with a stated default and flip conditions, keep work inline until retries must be durable or connections would hang, convert to domain types at the edge always, and hold pools and clients in app state wired in one place.

**Operating conditions and assumptions.** The team can articulate which criterion forces a queue or which invariant forces a newtype, if no reason can be named the default stands. This guide tunes choices within the playbook's anatomy, choosing whether this bundle applies at all is the guardrails' threshold question.

**Failure boundary and alternatives.** Resolving the tensions by habit produces the signature failures, everything-async architectures whose queues hide simple request flows, and everything-inline services whose retries duplicate payments. Bounded alternatives and recoveries: uniform regimes, queue everything or forbid queues, simpler to audit and defensible where per-case judgment cannot be trusted, at the cost of misfitting half the endpoints.

**Counterexample, gotchas, and operational comparison.** The split has its own price the playbook makes explicit, splitters must define what the endpoint commits, what the worker consumes, what already-processed means, and what operators can observe, skipping those four definitions trades one failure mode for four. Good: an email workflow moved behind a worker with all four split definitions written. Bad: a payment retry loop inline in the handler because the queue felt heavy. Borderline: transport types reused as domain types in a three-field internal service, cheap now, the invariant gap surfaces at the first added writer.

**Verification, evidence, and uncertainty.** Sample recent endpoints per axis and check deviations from the defaults carry a named criterion. The playbook's sections 2, 3, and 6 with their explicit defaults read in full. The traffic level at which inline defaults stop being safe is service-specific and unmeasured here.

**Second-order consequence.** The worker-split criteria are all failure-shaped, fan-out to unreliable systems, durable retries, idempotency, held connections, the playbook decides architecture by how things break rather than by how they perform, a colder and more checkable test.

**Revision decision.** Add the three tension axes with the playbook's defaults and the section 6 flip conditions for the durability axis.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the rust backend playbook reference pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong rust backend playbook reference guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which file's word governs when bundle guidance appears to disagree or fall silent. The seed crowns the playbook canonical with a confidence warning about single-source mapping, but the real structure is a five-file bundle where SKILL.md governs workflow, the map governs routing, and three siblings each own a risk surface the playbook defers to.

**Recommended default and causal basis.** Resolve anatomy disputes in the playbook, activation and guardrail disputes in SKILL.md, and risk-surface disputes in the owning sibling. The bundle's own context strategy defines the precedence, map first, playbook second, siblings by risk, so canonicality is per-question-class, anatomy to the playbook, verification to testing-and-fixtures, rollout to runtime-and-ops, auth and retries to security-and-resilience.

**Operating conditions and assumptions.** The 202604 bundle stays intact so per-file canonicality remains checkable against the context strategy. This hierarchy settles precedence within the bundle, precedence against the corpus's other Rust themes belongs to adjacent routing.

**Failure boundary and alternatives.** Treating the playbook as canonical for everything makes its silence authoritative, it says nothing about sessions or migrations, and a reader who stops there ships both unplanned. Bounded alternatives and recoveries: treating this corpus's other rust themes as a second-opinion layer when the bundle is silent, the adjacent routing section names them.

**Counterexample, gotchas, and operational comparison.** The siblings never contradict the playbook but do exceed it, the security file's transaction questions are stricter than the playbook's one-owner rule, reading the stricter rule as optional detail understates the bundle's demands. Good: settling a retry-scope question in security-and-resilience rather than stretching the playbook's persistence rules. Bad: declaring migrations out of scope because the canonical playbook barely mentions them. Borderline: taking SKILL.md's guardrails over a sibling's permissive example, wrapper precedence is defensible for activation questions.

**Verification, evidence, and uncertainty.** Check role claims against the bundle's context strategy order and each file's self-declared use line. The context strategy, the map's read orders, and all five files' opening use statements read in full. Whether the corpus will remap this theme to the full bundle is a maintainer choice this hierarchy cannot force.

**Second-order consequence.** The seed's confidence warning is self-correcting evidence, it invites adjacent-source discovery, and the discovery target is the playbook's own bundle, four files sitting beside the mapped one at the same archive path.

**Revision decision.** Keep the playbook canonical for anatomy, name SKILL.md canonical for workflow and guardrails, the map for routing, and each sibling for its risk surface.

**Retained seed evidence.** The single hierarchy row and the confidence warning remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/rust-web-backend-playbook.md | canonical primary source | Rust Web Backend Playbook; 1. Service Anatomy; 2. Request Handlers And App State | What guidance, warning, or example should this source contribute to Rust Backend Playbook Reference? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete object a team maintains to make backend request behavior reviewable per service. The seed names a request lifecycle diagram with persistence boundary, observability hook, and failure table but gives only generic completion rules, while the playbook supplies the concrete anatomy the diagram must trace.

**Recommended default and causal basis.** Draw the diagram per service at design time and update it in the same change as any boundary or split decision. The diagram's spine is the five-layer path, transport, handler, domain, persistence, integration, its persistence boundary marks the transaction owner, its observability hook carries the correlation identifier the ops sibling requires, and its failure table classifies each layer's failure classes per the security sibling.

**Operating conditions and assumptions.** The service has nameable request paths, event-driven workers need the same diagram drawn from queue message to side-effect instead. The artifact standardizes per-service request records, it does not replace the parent skill's traceability table, which maps requirements to tests.

**Failure boundary and alternatives.** A lifecycle diagram without the worker split marked misleads exactly where the architecture decision matters, the inline-versus-durable fork is the diagram's highest-value edge. Bounded alternatives and recoveries: encoding the same facts as a table per endpoint, cheaper to diff in review than a drawing, weaker at showing the fork structure.

**Counterexample, gotchas, and operational comparison.** A stale diagram misleads more than none, a marked transaction owner that a later refactor split silently sends responders to the wrong layer during an incident. Good: a checkout diagram marking the order-save transaction owner and the email fan-out behind a worker fork. Bad: a boxes-and-arrows sketch with no owner, hook, or fork marked. Borderline: one diagram covering five near-identical CRUD endpoints, defensible compression, the exceptional endpoint still deserves its own.

**Verification, evidence, and uncertainty.** Sample two diagrams per quarter and check the marked owners, hooks, and forks still match the code. The artifact's element derivation from the playbook's five layers and section 6 split definitions read in full. The maintenance cost at which teams abandon lifecycle diagrams is unmeasured here.

**Second-order consequence.** The diagram doubles as the failure-ownership map the playbook promises, when an incident arrives, the layer whose annotation matches the symptom is the owner, converting triage from archaeology into lookup.

**Revision decision.** Define the artifact as the five-layer path with the transaction owner, correlation hook, worker fork, and per-layer failure classes annotated.

**Retained seed evidence.** The artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: request lifecycle diagram with persistence boundary, observability hook, and failure table.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Rust Backend Playbook Reference | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which exercises most efficiently teach this theme's boundary discipline. The seed describes usage abstractly while the bundle implies one composed walkthrough, a new endpoint that parses at transport, converts to a newtype at the edge, owns one transaction, calls a typed remote client, and proves itself through a spawned-app test with a wiremock contract.

**Recommended default and causal basis.** Train newcomers on the composed endpoint first, then hand them the timeout failure case before certifying them on the bundle. The walkthrough chains five playbook rules and two sibling disciplines into one artifact, so a learner who completes it has exercised the theme's whole boundary doctrine rather than isolated fragments.

**Operating conditions and assumptions.** Training tasks include a real persistence and mock-remote boundary, examples without both teach the type half and silently skip the durability half. Worked examples here teach service anatomy and boundary discipline, deep auth, migration, and worker examples belong to the sibling files' own material.

**Failure boundary and alternatives.** Rules taught in isolation lose the composition, a learner who can write a newtype and a handler separately still lets the transaction span the remote call when assembling a real workflow. Bounded alternatives and recoveries: paired implementation with a veteran observing, slower than solo walkthroughs but surfaces boundary misconceptions live.

**Counterexample, gotchas, and operational comparison.** The walkthrough's subtlest step is what happens after commit, the security sibling forbids mixing durable-intent saves with remote side-effects absent a deliberate failure strategy, and the example must show that strategy explicitly. Good: a trainee's endpoint whose duplicate-submission case replays idempotently under test. Bad: memorizing the five layer names without composing any two boundaries. Borderline: practicing only on read endpoints, fluent in parsing and shape, untested on transactions and side-effects.

**Verification, evidence, and uncertainty.** Have the trainee build the endpoint solo and check the named invalid-input tests and the post-commit failure strategy exist. The playbook's REQ-WEB note and the security sibling's transaction rules read in full. How many composed exercises produce durable habit is unmeasured.

**Second-order consequence.** The playbook's REQ-WEB note makes examples self-verifying, invalid input paths become named contracts with named tests, so a trainee's walkthrough is graded by whether its empty, malformed, and duplicate cases each carry a test.

**Revision decision.** Anchor the section on the composed endpoint walkthrough plus one deliberate failure case, the remote call timing out after the durable intent is saved.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Rust Backend Playbook Reference after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Rust Backend Playbook Reference as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Rust Backend Playbook Reference only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which measurements justify this doctrine's continued emphasis and drive its revision. The seed names a compile-and-review leading indicator but no loop connects shipped services back to the doctrine, nothing counts which boundary rules recur as review rejections, which incidents trace to unowned layers, or which retries duplicated side-effects.

**Recommended default and causal basis.** Classify every backend rejection and incident against the layer and rule set and read the quarterly distribution before adjusting review emphasis. Review rejections and incidents are each classifiable against the playbook's layer rules and the siblings' risk rules, so tallying them per rule shows which boundaries the team has absorbed and which it re-learns per outage.

**Operating conditions and assumptions.** Reviews and retrospectives record enough detail to classify, one-word rejections and blameless-but-causeless postmortems starve the tally. This loop tunes doctrine adoption and review emphasis, service-level SLO tracking belongs to operations, not this reference.

**Failure boundary and alternatives.** Measuring only delivery speed rewards the deferred-cost failures this theme targets, an inline remote call demos faster than a worker split right up to the first duplicated payment. Bounded alternatives and recoveries: CI telemetry on the mechanical gates, complete capture for format and lint failures, blind to the semantic rules the loop most needs.

**Counterexample, gotchas, and operational comparison.** Falling rejection counts are ambiguous between absorbed discipline and eroding attention, corroborate quiet quarters with an occasional seeded boundary-violation diff. Good: a quarter showing transaction-scope rejections falling while layer attributions stay flat. Bad: declaring the doctrine absorbed because deploy frequency rose. Borderline: publishing per-person rejection stats, motivating for some teams, surveillance for others, aggregate by rule instead.

**Verification, evidence, and uncertainty.** Confirm recent review and incident records carry rule and layer classifications and the last quarterly review consumed them. The classifiable structure of the playbook's rules and the seed's own leading indicator read in full. Expected rejection base rates for a trained team have no baseline yet in this repository.

**Second-order consequence.** Layer attribution is the loop's sharpest instrument, the five-layer anatomy makes every incident classifiable to one owner, and a layer that accumulates attributions is a boundary drawn in the wrong place, feedback the anatomy itself generates.

**Revision decision.** Add the tally loop, per-rule rejection counts from review, per-layer incident attributions from retrospectives, and idempotency-violation counts from operator reports, reviewed quarterly.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: compile attempts and review comments decrease because the API shape is explicit before implementation.
Failure signal: the reference hides ownership or error tradeoffs behind generic guidance.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what must be confirmed before declaring this reference complete and faithful to its mapped bundle. The seed confirms this document's sections exist but never audits its content against the mapped bundle, no item catches a dropped layer, a paraphrased mode, or a misstated split criterion.

**Recommended default and causal basis.** Run the count audit and the sibling spot-check at every reread and refresh cycle before accepting this document as complete. This theme's correctness is largely transcription correctness, five layers, six playbook sections, six modes, six workflow steps, seven output-contract artifacts, five guardrails, and four split definitions, all countable against short files in minutes.

**Operating conditions and assumptions.** The 202604 bundle remains at its archived path for line-level comparison. This checklist audits this reference document's fidelity to its sources, auditing the bundle's internal consistency is the hierarchy section's job.

**Failure boundary and alternatives.** Count checks miss silence drift, if a future bundle revision adds a sixth layer or seventh mode, this document's counts fail loudly, but if a sibling file quietly rewrites its rules, the counts still pass while the by-name citations go stale. Bounded alternatives and recoveries: checksumming the five bundle files and re-auditing only on checksum change, near-zero steady-state cost, blind to drift in this document's own text.

**Counterexample, gotchas, and operational comparison.** Auditing against memory of the files rather than the files themselves recreates the pedigree-free-synthesis failure inside the audit itself. Good: an audit catching that a transcribed mode list dropped Review Mode. Bad: passing the audit because all 26 headings exist. Borderline: accepting paraphrased workflow steps, tolerable if the classify-first ordering survives verbatim.

**Verification, evidence, and uncertainty.** Count layers, sections, modes, steps, artifacts, guardrails, and split definitions in this document against the bundle files. The fully countable structure of all five bundle files read in full. Whether count-plus-spot-check auditing catches all meaningful drift in prose guidance is unproven.

**Second-order consequence.** The count audit doubles as a staleness detector for the bundle itself, any upstream revision that changes the countable structure fails this document immediately, flagging the refresh before drift misleads anyone.

**Revision decision.** Add fidelity items with the exact counts plus a sibling-freshness item, spot-check three by-name sibling citations against their live files each audit.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Rust Backend Playbook Reference.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send a question that arrived at this theme but is not a Rust backend service question. The seed splits the theme name into rust, backend, and playbook tokens, producing self-referential rows, while the real neighbors are named by the bundle itself, rust-executable-specs-01 and rust-coder-02 for non-service Rust work, plus this corpus's other rust themes for delivery, quality gates, and specs.

**Recommended default and causal basis.** Classify arriving questions as service-shaped or not, keep the service-shaped ones, and send the rest to the guardrail-named destinations. The parent skill's guardrails route explicitly, generic libraries, CLIs, parsers, protocol crates, and FFI go to the two named sibling skills, so the commonest misroute into this theme already has a documented exit.

**Operating conditions and assumptions.** The named destination skills and themes exist in the archive and corpus and cover their assigned classes. Routing sends away questions this theme cannot close, it does not summarize what the destination themes contain.

**Failure boundary and alternatives.** The costliest misroute is the reverse one, a web service treated as a generic library, its reviewer applies style guidance while sessions, migrations, and idempotency go unexamined by any skill. Bounded alternatives and recoveries: for framework-version specifics no local theme answers, external documentation explicitly labeled unretrieved, never presented as verified.

**Counterexample, gotchas, and operational comparison.** Worker and queue questions look infrastructure-shaped but belong here, the playbook's section 6 and the security sibling's background-processing rules own them, routing them away strands the asker. Good: sending a parser-crate API design question to rust-coder-02 per the guardrails. Bad: routing to the playbook adjacent reference, a token synonym for this same file. Borderline: keeping a Docker build question, the ops sibling covers image shape, deep container orchestration still exits the bundle.

**Verification, evidence, and uncertainty.** Confirm each named destination exists and matches its assigned question class. The guardrails' not-for list and the seed's own adjacent guidance line read in full. Actual misroute frequency into this theme is estimated, not measured.

**Second-order consequence.** This theme's routing is bidirectionally documented, the guardrails name the exits and the description's not-for list names the non-entries, few corpus themes state both sides, making misroutes here a reader failure rather than a documentation gap.

**Revision decision.** Route non-service Rust work to the guardrail-named skills, spec-writing depth to executable-specs themes, review-gate depth to quality-gate themes, and keep service anatomy, boundaries, and worker splits here.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use backend, executable, or quality-gate Rust references when the question shifts to HTTP delivery, specs, or review gates.
Adjacent reference 1: consider the rust adjacent reference when the current task pivots away from rust backend playbook reference.
Adjacent reference 2: consider the backend adjacent reference when the current task pivots away from rust backend playbook reference.
Adjacent reference 3: consider the playbook adjacent reference when the current task pivots away from rust backend playbook reference.

## Workload Model

**Decision supported.** This section helps decide how much backend delivery work one team can sustain per review batch without the discipline decaying. The seed budgets one service boundary, 25 endpoints, and 1000 representative requests per review batch, but never connects the budget to the bundle's own unit of work, the mode-classified service slice with its layer boundaries and verification matrix.

**Recommended default and causal basis.** Scope each unit of work to one service slice and budget integration-first testing as first-class effort, not overhead. The bundle's costs are per-slice, requirements and boundary design are one-time costs per endpoint, the harness amortizes across every integration test, migration sequencing is per-schema-change, and the verification matrix is the recurring cost that scales with concern count.

**Operating conditions and assumptions.** Work decomposes into nameable slices, cross-cutting refactors and bundle-wide upgrades need their own splitting discipline. This model budgets implementation and review effort for bundle consumers, authoring effort for this corpus document is a separate, rarer workload.

**Failure boundary and alternatives.** The model breaks when one change spans several slices, an endpoint plus its migration plus a worker in one review degrades attention until the per-slice checks, transaction scope, rollout order, idempotency keys, silently drop. Bounded alternatives and recoveries: concern-based estimation from the verification matrix, costing each matrix row the change touches, finer-grained but demands the matrix be filled first.

**Counterexample, gotchas, and operational comparison.** Migration work hides its true size, the ops sibling's five-step sequencing means one risky schema change is really five ordered deliveries, estimating it as one ships the impossible orderings the sibling forbids. Good: a slice scoped as one endpoint, three REQ-WEB rows, and four matrix tests before estimation. Bad: one PR carrying an endpoint, its schema change, and a new worker loop. Borderline: batching five trivial read endpoints into one review, defensible when they share every boundary, log it as one slice decision.

**Verification, evidence, and uncertainty.** Track review units per slice in the journal and watch for multi-slice PR signatures. The seed capacity row and the bundle's per-slice cost structure read across the five files. The slice count at which review attention measurably decays is judgment, not measured.

**Second-order consequence.** The seed's 25-endpoint ceiling is generous precisely because slices amortize, a service whose endpoints share one harness, one wiring point, and one persistence module reviews far cheaper per endpoint than the first endpoint did.

**Revision decision.** Restate capacity in slice terms, one mode-classified slice with its REQ-WEB rows, layer design, and matrix-assigned tests per review unit, splitting anything larger.

**Retained seed evidence.** The workload dimension rows with boundary values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Rust Backend Playbook Reference as a backend service operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | service implementation, route review, worker execution, and operational hardening work where a single wrong recommendation can affect live request handling | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one service boundary, up to 25 endpoints or workers, 1000 representative requests, and one deploy rollback path per review batch | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Rust Web Backend Playbook; 1. Service Anatomy; 2. Request Handlers And App State; 3. Domain Types And Validation Boundaries; 4. Persistence Boundaries | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is request lifecycle diagram with persistence boundary, observability hook, and failure table | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what reliability the shipped backend must demonstrate for this theme's guidance to count as working. The seed measures document properties like label preservation while the shipped service's own reliability questions go unstated, does every workflow have one transaction owner, every repeatable write an idempotency definition, every remote call a timeout policy, and every schema change a rollback that still works.

**Recommended default and causal basis.** Audit the four rule-derived targets per release and triage any violation to its owning bundle rule before the next release. The bundle's rules define measurable targets directly, the one-owner rule implies zero ambiguous multi-write workflows, the idempotency rules imply zero undefined replay states, the client contract implies zero unclassified remote failures, and the sequencing rules imply zero irreversible rollout steps.

**Operating conditions and assumptions.** Reviews can see workflow-level context, single-file diffs hide three of the four targets. Targets here cover service correctness and delivery safety, latency SLOs are the performance section's subject and product uptime belongs to operations.

**Failure boundary and alternatives.** Targets measured only in tests miss the ambiguity failures the security sibling's checklist names, a timeout or crash that leaves a workflow in an undefined state passes every deterministic test and fails only in production timing. Bounded alternatives and recoveries: operator-facing chaos drills, kill a worker mid-workflow on staging and check the observable state transitions, heavier than static audit and the only test of the ambiguity target.

**Counterexample, gotchas, and operational comparison.** Zero recorded violations over a long window more often means the audit stopped running than that the service is perfect, corroborate quiet windows with a seeded ambiguous-workflow drill. Good: a release audit finding one repeatable write without a replay definition and blocking on it. Bad: declaring the service reliable because unit coverage is high. Borderline: waiving the rollback target for an additive-only schema change, defensible, record the waiver against the sequencing rule.

**Verification, evidence, and uncertainty.** Review the four target audits together at each release checkpoint. The security sibling's checklist questions and the ops sibling's sequencing rules read in full. This repository's baseline violation rates are unknown until the audits begin.

**Second-order consequence.** All four targets are greppable or reviewable before deployment, transaction owners, idempotency keys, failure-class matches, and rollback notes are static artifacts, the discipline converts reliability from observation into reviewable structure.

**Revision decision.** Add the operational targets, zero unowned transactions, zero undefined idempotency boundaries on repeatable writes, zero unclassified remote failure paths, and a working rollback after every rollout step.

**Retained seed evidence.** All four seed reliability rows with thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which ways this theme's discipline silently fails and how each failure is caught. The seed covers drift, process, surge, and security rows but not the decay modes specific to this theme's discipline, boundary erosion where business rules migrate back into handlers, split debt where inline shortcuts accumulate past their criteria, and sequencing violations where schema and code ship in impossible orders.

**Recommended default and causal basis.** Attach each failure row to its own detection cadence, review tallies quarterly, split re-evaluation at traffic milestones, sequencing plans per schema change. Each mode follows from the doctrine's construction, the layers demand ongoing discipline nothing enforces, the worker-split criteria demand re-evaluation as traffic grows, and the five-step rollout order demands coordination nothing in the code itself checks.

**Operating conditions and assumptions.** Someone owns the probes, a failure table without assigned owners is itself the erosion mode it describes. This table catalogs failures of the theme's discipline, individual code anti-patterns are the registry's subject one level down.

**Failure boundary and alternatives.** All three modes produce working services at first, fat handlers pass their tests, inline slow calls succeed under low traffic, and mis-sequenced deployments work on single instances, each fails only under the load, retry, or rollout condition it was never designed for. Bounded alternatives and recoveries: automating the mechanical probes into CI, a lint for handler-embedded SQL and a deploy gate requiring a sequencing note when migrations are present.

**Counterexample, gotchas, and operational comparison.** Split debt is the stealthiest mode because its criteria are external to the code, the same inline email call is correct at ten requests a day and a duplication engine at ten thousand, nothing in the diff ever changed. Good: a traffic review catching an inline fan-out that newly meets two split criteria. Bad: praising a quiet quarter no one actually probed. Borderline: a documented decision to keep a slow call inline with a stated tradeoff, sanctioned by the guardrails, indistinguishable from debt when the note is missing.

**Verification, evidence, and uncertainty.** Confirm each failure row names its probe, owner, and cadence, and that the journal shows the probes ran. The layer discipline, split criteria, and sequencing rules read across the bundle files. Actual onset times for boundary erosion among real teams are unmeasured.

**Second-order consequence.** The three modes decay on different clocks, erosion tracks team churn, split debt tracks traffic growth, and sequencing violations track deploy cadence, so one annual review cannot cover them and each needs its own trigger.

**Revision decision.** Add rows for boundary erosion caught by layer-attributed review tallies, split debt caught by re-checking section 6 criteria at traffic reviews, and sequencing violations caught by requiring the five-step plan on every schema change.

**Retained seed evidence.** All four seed failure rows with mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| request surge overloads path | traffic spikes exceed handler, pool, or coroutine limits | apply rate limits, queue bounds, cancellation, and rollback playbook before rollout |
| security boundary silently fails | auth, permission, or input validation assumptions are untested | run abuse-case tests and require explicit deny-by-default behavior |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide how many retry attempts each failure class gets and through which mechanism. The seed covers document-verification retries but not the runtime retry surfaces this theme owns, failure-class-specific policies at remote boundaries, durable retries behind workers, and idempotency keys that make retries safe to receive.

**Recommended default and causal basis.** Classify every remote failure, retry only under an idempotency definition, and promote retries to durable workers when they must outlive the request. The security sibling composes these into a ladder, classify the failure first, client error, server error, timeout, transport failure, malformed response, then assign each class its policy, fail fast, retry, record for replay, surface to operator, or move to async recovery.

**Operating conditions and assumptions.** Remote boundaries flow through typed clients whose contracts include timeout and status handling, ad hoc calls scattered in handlers have no surface for the ladder to attach to. This section governs service-level retry and backpressure behavior, corpus-process retries stay in the seed bullets, and client-side UI retry belongs to frontend themes.

**Failure boundary and alternatives.** Retrying without classification is the ladder's collapse, a client error retried burns quota on a request that can never succeed, and a timeout retried without an idempotency key may execute the side-effect twice. Bounded alternatives and recoveries: circuit-breaker layers on hot remote paths, beyond what the mapped bundle prescribes, compatible with its failure-class framing where fan-out risk is severe.

**Counterexample, gotchas, and operational comparison.** Backpressure inside the transaction is the subtle trap, holding a database transaction open across a retrying remote call converts remote slowness into pool exhaustion, the two boundaries must not nest. Good: a payment call whose timeout retries once under an idempotency key then records for replay. Bad: a blanket three-retries policy applied to malformed responses. Borderline: infinite worker retries on an operator-visible queue, defensible with alerting, unbounded without it.

**Verification, evidence, and uncertainty.** Test each failure class under wiremock-simulated faults and confirm the assigned policy fires with no double side-effects. The security sibling's failure-class and idempotency sections and the playbook's split criteria read in full. The right retry caps per class are product-tolerance choices this bundle deliberately leaves local.

**Second-order consequence.** Idempotency is backpressure's receiving end, the sibling's four definitions, key boundary, replay state, sameness, and concurrency behavior, are what let a service absorb the retry storms its own timeouts provoke, senders and receivers of retries are designed as one system.

**Revision decision.** Add the runtime ladder, classify by failure class, retry only the retryable classes, key every repeatable write, and move durable retries behind the worker boundary section 6 defines.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence each shipped backend must produce for the reliability loops to function. The seed logs document-usage evidence and generic counters but not the backend-specific signals the bundle makes observable, correlation identifiers on every request, worker state transitions operators can see, readiness distinct from liveness, and secrets provably absent from logs.

**Recommended default and causal basis.** Emit the service record for every request path and review it beside the release-time target audit. The ops sibling demands structured tracing with propagated identifiers and health surfaces that reflect real dependencies, and the playbook's split definitions require operator-visible state transitions, so the checklist items are transcriptions of stated bundle requirements.

**Operating conditions and assumptions.** Record emission stays cheap, high-value fields recorded once and propagated rather than re-derived per layer, per the ops sibling. This checklist specifies observability of backend service behavior, business analytics and frontend telemetry belong to their own systems.

**Failure boundary and alternatives.** Observability that stops at error counts cannot answer the checklist's own triage questions, without correlation identifiers a multi-layer failure cannot be walked back to its owning layer, and the five-layer anatomy loses its diagnostic value. Bounded alternatives and recoveries: log aggregation with retroactive parsing for teams that cannot adopt structured tracing, recovering some correlation at much higher query cost.

**Counterexample, gotchas, and operational comparison.** Worker observability is the commonly skipped half, a queue consumer with no visible state transitions makes already-processed disputes unresolvable, exactly the ambiguity the split definitions exist to prevent. Good: a trace showing one request identifier crossing handler, domain, and persistence into a worker handoff. Bad: a quarter summarized as no backend incidents with no correlated telemetry behind it. Borderline: sampling traces on high-volume read paths, defensible for cost, mutations should stay unsampled.

**Verification, evidence, and uncertainty.** Sample recent traces and check identifier propagation, worker transitions, and redaction hold end to end. The ops sibling's tracing and health sections and the playbook's operator-visibility definitions read in full. The sampling rate at which trace volume stays affordable is workload-dependent.

**Second-order consequence.** The checklist's cheapest item carries the most weight, propagating one request identifier through all five layers turns the anatomy into a queryable index, every incident becomes a filtered trace instead of a log excavation.

**Revision decision.** Define the minimal service record, correlated structured traces per request, worker state transitions per workflow, readiness and liveness split per the ops sibling, and a secret-redaction check in review.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture error count, timeout count, retry count, saturation signal, and rollback trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove backend performance without rewarding wrong-but-fast fixes. The seed sets p95 and p99 ceilings while the bundle defines the mechanism-level method, verify boundary behavior first, pool and client reuse, transaction scope, inline-versus-worker placement, because those mechanisms are where backend latency regressions originate.

**Recommended default and causal basis.** Audit the four mechanisms on the changed path, then measure p95 and p99 on representative handlers against the SLO or the seed's fallback ceilings. The playbook's rules are performance rules in disguise, per-request client construction adds connection setup to every call, transactions spanning remote calls serialize the pool, and inline fan-out holds connections open, so mechanism audit explains what latency numbers only report.

**Operating conditions and assumptions.** Representative load exists, the seed's 1000-request batch from the workload model gives the measurement its sample. This method verifies service-level request performance, database query tuning and infrastructure sizing belong to their own methods.

**Failure boundary and alternatives.** Verifying only the ceiling invites the wrong fix, a slow endpoint gets caching sprinkled over it when the actual defect is a transaction held across a remote call that no cache can shorten. Bounded alternatives and recoveries: continuous latency telemetry from the observability record instead of point-in-time drills, catching regressions between releases at the cost of noisier attribution.

**Counterexample, gotchas, and operational comparison.** Averages hide the tail here as everywhere, one blocking credential hash on the async executor disappears into a mean while stalling every request sharing the worker thread. Good: a regression traced to a transaction newly spanning a remote call, fixed by moving the call post-commit. Bad: adding a cache over an endpoint whose pool was exhausted by held transactions. Borderline: accepting a p99 breach on an admin-only endpoint, defensible by traffic, document it against the SLO precondition.

**Verification, evidence, and uncertainty.** Inspect mechanism audit results beside the latency numbers before drawing any conclusion. The playbook's resource and transaction rules and the seed's SLO precondition read in full. The seed's 200 and 500 millisecond fallback ceilings are corpus defaults, not measurements from any service in this repository.

**Second-order consequence.** The seed's own precondition is the method's sharpest rule, require a service-specific SLO before deployment and document when latency does not apply, making absent SLOs a named gap rather than an implicit pass.

**Revision decision.** Measure mechanism first, client reuse, transaction span, executor blocking, and work placement, then confirm the seed's ceilings as the user-facing consequence.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require a service-specific SLO before deployment; absent that, keep local verification to p95 under 200 ms and p99 under 500 ms for representative handlers or document why latency does not apply.
Leading indicator to measure: compile attempts and review comments decrease because the API shape is explicit before implementation.
Failure signal to watch: the reference hides ownership or error tradeoffs behind generic guidance.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what traffic, instance count, or service count this theme's guidance must change shape rather than merely stretch. The seed bounds document scale but not the discipline's scaling seams, the traffic level where inline work must move behind workers, the instance count where zero-downtime sequencing becomes mandatory, and the service count where this single-service anatomy stops describing the system.

**Recommended default and causal basis.** Apply the playbook as written within one service and treat any seam crossing as a design event requiring re-evaluation, not parameter tuning. The bundle states two seams directly, section 6 flips inline to durable when retries, fan-out, or held connections appear, and the ops sibling makes the four-step schema evolution the default whenever multiple instances or staggered rollouts are possible, the third seam, multi-service architecture, is the seed's own stated stop line.

**Operating conditions and assumptions.** Growth is observable, someone notices the traffic milestone, the second instance, or the second service and re-asks the seam questions. This statement marks where this theme's single-service guidance stops, cross-service contracts, distributed sagas, and platform architecture are out of scope.

**Failure boundary and alternatives.** Scaling by stretching the existing shapes defeats them, an inline handler absorbing tenfold traffic becomes a connection-holding retry amplifier, and a single-instance migration habit under rolling deploys ships the impossible orderings the sibling forbids. Bounded alternatives and recoveries: designing for the seams from day one, always-durable work and always-sequenced migrations, safer for teams expecting fast growth, pure overhead for services that never grow.

**Counterexample, gotchas, and operational comparison.** The seams interact, moving work behind a worker at the traffic seam adds queue tables whose schema changes then hit the sequencing seam, crossing one seam often schedules the next. Good: a traffic review moving email fan-out behind a worker as retries became durable requirements. Bad: a rolling deploy shipping a strict-constraint migration in one step. Borderline: keeping single-instance migration habits on a two-instance service with maintenance windows, defensible, the window is now the load-bearing assumption.

**Verification, evidence, and uncertainty.** Check the seam questions at each growth event against section 6 criteria and the four-step evolution pattern. The playbook's split criteria and the ops sibling's multi-instance default read in full. The exact traffic level at which each criterion trips is service-specific and unmeasured here.

**Second-order consequence.** All three seams share one shape, assumptions that were invisible at small scale, short requests, single instances, one service, become load-bearing exactly when growth invalidates them, so the seams are best checked at growth events, not on a calendar.

**Revision decision.** Add the seams, traffic growth re-triggers the section 6 criteria, instance growth mandates the four-step evolution pattern, and service multiplication exits this theme entirely.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Rust Backend Playbook Reference stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which searches and probes reveal that this theme's doctrine or examples have gone stale. The seed recycles the theme name while this theme's staleness lives in three specific places, the crate ecosystem the playbook names as representative examples, the bundle's own 202604 lineage, and the async runtime norms the anatomy presumes.

**Recommended default and causal basis.** Run crate-release probes on a faster cadence than the lineage watch, dating every finding against the 202604 anchor. The theme's claims are boundary doctrine tied to a frozen authoring moment, doctrine ages slowly but its ecosystem illustrations age fast, so refresh probes are release-note reads for axum, tokio, sqlx, and reqwest, plus a watch for a post-202604 revision of rust-web-backend-delivery.

**Operating conditions and assumptions.** Refresh effort stays bounded, probes are ordered by expected impact so the budget goes to the crates the playbook actually names. These probes refresh this file's ecosystem and lineage claims, refreshing general Rust language guidance belongs to the other rust themes' own queries.

**Failure boundary and alternatives.** Theme-name searches return this corpus's own files and generic Rust tutorials, neither can reveal that an axum release changed extractor signatures or that a newer bundle revision restructured the reference set. Bounded alternatives and recoveries: watching the upstream skill archive for a rust-web-backend-delivery-02, if the authors ship a revision, diffing it beats re-deriving changes from release notes.

**Counterexample, gotchas, and operational comparison.** Boundary doctrine rarely breaks on releases, a new axum version changes example syntax, not the thin-handler rule, so probe findings need triage into doctrine-breaking versus example-breaking before any rewrite. Good: a probe finding sqlx changed its migration API, and the persistence examples gain a dated caveat. Bad: logging that the theme-name query returned nothing new. Borderline: probing new Rust web frameworks for adoption, adjacent to the ecosystem list, unbounded if not capped.

**Verification, evidence, and uncertainty.** Record each probe with its date and the specific rule or example it confirmed or invalidated. The 202604 bundle date and the playbook's named crate examples read from the mapped files. How fast the Rust web ecosystem invalidates 202604 illustrations is unknowable without the fetches these queries queue.

**Second-order consequence.** The bundle's own structure orders the probe budget, doctrine files like the playbook need lineage watching, while the crate examples need release watching, two different cadences the seed's single query set cannot express.

**Revision decision.** Replace the name-based trio with targeted probes, crate release notes for the four named crates since 202604, an archive watch for newer bundle revisions, and a periodic check that the five-layer anatomy still matches framework idioms.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | rust backend playbook reference official documentation best practices |
| `github_repository_query_phrase` | rust backend playbook reference GitHub repository examples |
| `release_notes_query_phrase` | rust backend playbook reference changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide which of this document's statements may travel elsewhere and under what label. The seed defines the three labels but omits this evolution's concrete ledger, one mapped file plus four sibling bundle files read fully, zero external URLs retrieved, and every operational policy above marked as inference.

**Recommended default and causal basis.** When reusing a claim from this file, ask whether the count audit could verify it, citing the file and section if yes and carrying the reasoning along if no. The five layers, section rules, modes, workflow steps, guardrails, split criteria, failure classes, and sequencing steps are transcribable local facts with named files and sections, while the tally loop, audit targets, seam framings, and probe cadences are this evolution's constructed machinery built on those facts.

**Operating conditions and assumptions.** The 202604 bundle stays at its archived path so fact-class claims remain mechanically re-checkable. These notes govern reuse of this document's claims, transcribed doctrine travels freely with citations, constructed machinery travels only with its reasoning attached.

**Failure boundary and alternatives.** The highest-risk mislabel here is presenting the crate names or the seed's latency ceilings as verified current facts, the crates are archive-dated illustrations and the ceilings are corpus defaults no service has measured. Bounded alternatives and recoveries: inline per-claim labels throughout the document if the section-level split proves too coarse for downstream disputes.

**Counterexample, gotchas, and operational comparison.** Sibling-sourced facts carry a subtler label risk than playbook facts, only the playbook is in the mapped table, so sibling citations must stay by-name and explicit or they masquerade as claims from the mapped row. Good: reusing the five-layer anatomy with its playbook section cited. Bad: citing the quarterly tally cadence as a rust-web-backend-delivery rule. Borderline: reusing the worker-split criteria against a non-Rust backend, the logic transfers, the Rust-specific executor caveats do not.

**Verification, evidence, and uncertainty.** Sample claims from earlier sections and confirm each falls cleanly on one side of the published split. This assignment's read ledger, five bundle files read in full, zero retrievals. Readers cannot re-verify the reading itself, only the citations it produced.

**Second-order consequence.** The fact-inference split follows the countability line again, everything the completeness audit can count against the bundle is fact, everything it cannot count is this evolution's machinery, one boundary serving both the audit and the label.

**Revision decision.** Publish the split explicitly, layers, rules, modes, criteria, and classes are local corpus facts, loops, targets, seams, and cadences are combined-evidence inference.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
