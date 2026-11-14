# Rust Backend Testing Fixtures

**Decision supported.** This section helps decide which testing posture governs a Rust backend service before its first test is written. The seed title pairs testing with fixtures but the seed never states the file's central inversion, for HTTP backends the outside-in integration test is the primary instrument and unit tests are the specialists, reserved for domain constructors, validation, parsing edges, and small pure decisions.

**Recommended default and causal basis.** Start substantial backend work with outside-in tests through the spawned app, and add unit or property tests only at the domain edges the matrix assigns them. The inversion exists because backend defects cluster in wiring, serialization, routing, and state setup, faults that live between units, so tests entering through the public HTTP interface catch what unit tests structurally cannot see.

**Operating conditions and assumptions.** The service exposes a public HTTP interface to test through, non-HTTP Rust work exits to the broader skills before this doctrine applies. This reference covers endpoint verification, harness structure, isolated infrastructure, mocking, helpers, and the test matrix, what to build is the playbook theme and how to deploy is the ops theme.

**Failure boundary and alternatives.** Reading the file as generic test advice misses that its harness, port, database, and mocking sections all serve the one inversion, they are the infrastructure bill the outside-in stance requires teams to pay. Bounded alternatives and recoveries: unit-first pyramids from general testing culture, cheaper per test and blind to exactly the wiring faults the file says dominate backend failure.

**Counterexample, gotchas, and operational comparison.** Integration-first is not integration-only, the file explicitly preserves unit territory, and teams that read it as permission to drop unit tests lose the cheap coverage of constructors and parsing edges it deliberately kept. Good: a new endpoint verified request-in response-out with its database side-effect asserted. Bad: a routing bug shipped under a green suite of handler unit tests. Borderline: unit-testing an extractor's deserialization, useful, the matrix still wants one integration pass over the wire.

**Verification, evidence, and uncertainty.** For a recent defect, ask which test kind the matrix assigns its class and whether such a test existed. Full read this session of the 91-line testing-and-fixtures file and its four sibling bundle files. The file's claim that integration tests catch wiring faults earlier is stated, not measured, in this corpus.

**Second-order consequence.** The file assigns each test kind a jurisdiction rather than a rank, the matrix maps six concerns to preferred test types, so the real doctrine is not integration tests are better but each defect class has one cheapest catcher, choose by concern.

**Revision decision.** Open with the inversion, integration-first with unit tests as domain specialists, and present the remaining sections as its supporting machinery.

**Retained seed evidence.** The exact theme title and testing framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source justifies each testing claim class in this theme. The seed one local row carries the theme while the testing file is the bundle's service hub, the delivery skill's verification-mix step consumes its matrix, the ops file's CI section requires its migration-aware tests, and the reference map routes three different task types through it in order.

**Recommended default and causal basis.** Cite the testing file for technique claims, named siblings for consumption chains, and externals as candidates only. Testing doctrine is consumed doctrine, its authority shows up as other files' requirements, so claims about who uses the matrix or when CI runs these tests chain through named siblings beyond the mapped row.

**Operating conditions and assumptions.** The 202604 archive path remains stable for citation resolution. Provenance for this document's statements only, the four external URLs stayed unretrieved throughout this evolution and confer no current-fact authority.

**Failure boundary and alternatives.** Attributing chained claims to the mapped row alone, for instance quoting the four-gate CI floor as testing-file content, breaks the provenance trail at its first hop. Bounded alternatives and recoveries: a future mapping revision adding the wiremock repository or docs row, aligning the external queue with the file's actual ecosystem claim.

**Counterexample, gotchas, and operational comparison.** The external rows omit wiremock itself, the one crate the file names has no URL row while four framework anchors irrelevant to mocking do, the candidate queue misses this theme's single most citable target. Good: citing section 3 for the random-port isolation rules. Bad: citing the axum docs row for harness structure it does not anchor. Borderline: citing the reference map for which tasks read this file second, correct by name, outside the mapped row.

**Verification, evidence, and uncertainty.** Trace disputed claims to the exact testing-file section or named sibling that contains them. Full reads this session of the testing file and all five bundle companions. Whether the wiremock omission was a deliberate template choice is unrecorded.

**Second-order consequence.** This file contains the bundle's only named test-ecosystem crate, wiremock as the representative mocking example, giving the theme exactly one archive-dated ecosystem claim to guard, a smaller but sharper freshness surface than its siblings carry.

**Revision decision.** Anchor on the testing file for harness, isolation, mocking, helper, property, and matrix claims, and cite the delivery skill, ops file, and reference map by name for consumption claims.

**Retained seed evidence.** The single local row and all four external rows with their column values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/rust-backend-testing-and-fixtures.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://github.com/rust-lang/api-guidelines | external_research_source_material | external_research_sourced_fact | Rust library-team API design recommendations |
| https://github.com/tokio-rs/tokio | external_research_source_material | external_research_sourced_fact | async runtime implementation and operational model |
| https://github.com/tokio-rs/axum | external_research_source_material | external_research_sourced_fact | Rust web framework implementation and design claims |
| https://docs.rs/axum/latest/axum/ | external_research_source_material | external_research_sourced_fact | published crate documentation for routing and extractors |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which testing investment a resource-constrained team makes first. The seed scored rows rank corpus hygiene while the testing file's own priority is infrastructural, the harness comes first because every integration test rides on it, isolation second because unisolated tests poison each other, mocking third because external calls block determinism, and helpers, properties, and the matrix refine what the first three enable.

**Recommended default and causal basis.** Build the spawned-app harness first, wire isolation semantics second, add HTTP mocking third, then let the matrix distribute concerns across the standing infrastructure. The ordering is a dependency chain, no outside-in test exists without a bootable harness, no trustworthy suite exists without port and database isolation, and no external-integration test exists without mocks, so adoption order is forced by what each layer needs beneath it.

**Operating conditions and assumptions.** The service is early enough to sequence adoption, an existing untested service starts the same chain retrofitted, harness first regardless. This ranking orders testing infrastructure, entry-layer and operational rankings live with their own themes.

**Failure boundary and alternatives.** Adopting the matrix before the harness is the common inversion, teams classify their concerns correctly and then cannot write the assigned integration tests because nothing can spawn the app under test configuration. Bounded alternatives and recoveries: risk-ordered adoption starting from the last incident's defect class, emotionally compelling, it usually lands on the same chain because the assigned test still needs the harness.

**Counterexample, gotchas, and operational comparison.** Helper structure looks skippable as mere style, but section 5's warning that a helper hiding too much logic stops helping is load-bearing, an opaque harness converts every test failure into an infrastructure investigation. Good: a service whose first merged test file is the harness booting on a random port. Bad: a property-testing initiative on a service that cannot spawn itself in tests. Borderline: deferring mocks on a service with no external calls yet, fine, the first integration PR changes the answer.

**Verification, evidence, and uncertainty.** Compare a team's testing adoption sequence against the dependency chain and ask what justified each inversion. The testing file's seven-section structure and internal dependencies read in full. No measurement ranks these investments by realized defect prevention in this repository.

**Second-order consequence.** The chain explains why the file spends three of its seven sections on setup rather than assertion, in backend testing the hard engineering is making tests possible and cheap, the assertions themselves are the easy residue once the infrastructure stands.

**Revision decision.** Present the dependency-chain ordering as operative and keep the scored rows as corpus-process emphasis.

**Retained seed evidence.** The three scored seed rows with tier labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `rust_backend_testing_fixtures` | 95 | default_adoption_pattern_tier | Source Map First: Load local rust backend material before synthesizing testing fixtures recommendations. |
| `rust_backend_testing_fixtures` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `rust_backend_testing_fixtures` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what character every test added under this theme must exhibit. The seed generic corpus formulas replace the testing thesis, a Rust backend suite is trustworthy when tests enter from the outside, run on isolated infrastructure, and read like user journeys rather than dependency graphs.

**Recommended default and causal basis.** Evaluate any proposed test or harness change against the three clauses and reject changes that trade one clause for another. Each clause condenses sections of the mapped file, outside entry from the integration-first mindset, isolation from the port and database rules, and journey readability from the harness section's explicit design goal for what tests should read like.

**Operating conditions and assumptions.** The suite can afford real infrastructure, isolation via ephemeral databases assumes provisioning the ops theme's CI preconditions supply. The thesis governs test-suite character, which behaviors to specify is the entry theme's requirements discipline and what the service does is the playbook theme's concern.

**Failure boundary and alternatives.** Collapsing the thesis to just write integration tests misses the readability clause, a suite of outside-in tests that read as dependency wiring is unmaintainable evidence, technically correct and practically unreviewable. Bounded alternatives and recoveries: an assertion-count or coverage-percentage framing of suite quality, easier to measure and blind to all three clauses, coverage can be high on a suite that is inside-out, entangled, and unreadable.

**Counterexample, gotchas, and operational comparison.** Journey readability decays silently as helpers accrete, each extraction individually improves the diff while the accumulated test drifts toward the dependency-graph shape the harness section warns against. Good: a test reading create user, post order, expect 201 and a persisted row. Bad: a test importing six internal modules to assemble state before one assertion. Borderline: a journey test with one internal shortcut for setup speed, acceptable when the shortcut is a labeled helper.

**Verification, evidence, and uncertainty.** Sample recent tests and check each clause, entry point, isolation semantics, and whether a reviewer can narrate the journey aloud. The testing file's mindset, isolation, and harness sections read in full. Whether three clauses cover event-driven services without HTTP surfaces is beyond the mapped material.

**Second-order consequence.** The clauses serve three different readers, outside-in serves the defect finder, isolation serves the suite operator debugging flakes, and journey readability serves the reviewer deciding whether the test proves the requirement, a suite failing one clause fails one audience specifically.

**Revision decision.** State the three clauses, outside-in, isolated, journey-readable, each cited to its sections.

**Retained seed evidence.** The three labeled thesis statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `rust_backend_testing_fixtures` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Rust Backend Testing Fixtures comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide how to navigate the mapped testing file when a suite question arrives. The seed map row lists heading signals without the file's internal split, sections 1 through 5 are universal, every backend service needs mindset, harness, isolation, mocking, and helpers, while 6 and 7 are selective, property tests where domain invariants warrant and the matrix scaled to substantial work.

**Recommended default and causal basis.** Read sections 1 through 5 when standing up any service's suite and enter 6 and 7 when domain invariants or work scale trigger them. The file marks the split itself, property tests are to be used selectively and strongest at the domain edge, and the matrix applies to substantial backend work, so reading depth should follow the universality gradient.

**Operating conditions and assumptions.** Questions arrive classifiable as universal setup versus selective refinement, defect investigations may need the matrix first to identify the missing test class. This map describes the mapped testing file, the rest of the bundle is described by its sibling themes' corresponding sections.

**Failure boundary and alternatives.** Reading the file flat overweights its tail, teams debate property-test strategy for services whose harness still boots on a fixed port, spending attention where the file itself says the stakes are selective. Bounded alternatives and recoveries: direct heading search with the bundle's shipped ripgrep commands, effective for experts who already know which section owns their question.

**Counterexample, gotchas, and operational comparison.** Section 3's closing rule is easy to skim past, shared infrastructure demands a documented isolation boundary and why it is safe, the only sentence in the file that mandates prose documentation rather than code. Good: a new-service suite built from sections 2 and 3 before any assertion is written. Bad: a property-testing debate on a suite with colliding ports. Borderline: reading only the matrix to audit an existing suite, workable, the isolation rules are what the audit will miss.

**Verification, evidence, and uncertainty.** Check that recent consultations entered at the section matching the question's universality class. The testing file's structure and the reference map's routing rows read in full. Whether the universal five deserve separate corpus themes eventually is a maintainer call.

**Second-order consequence.** The file is the bundle's most example-shaped reference, its sections describe reusable objects, a harness, a fixture, a mock, rather than rules, which is why the reference map routes readers here immediately after doctrine files, doctrine tells what, this file tells with-what.

**Revision decision.** Annotate the row with the universal-versus-selective split and the reference map's orderings that route auth work to this file second and endpoint work to it after the playbook.

**Retained seed evidence.** The single local source row with title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/rust-backend-testing-and-fixtures.md | Rust Backend Testing And Fixtures | Rust Backend Testing And Fixtures; 1. Integration-Test-First Mindset; 2. Spawned-App Test Harness; 3. Random Port And Isolated Database Setup; 4. HTTP Mocking And Contract Tests; 5. Maintainable Helper Structure | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide which external targets deserve retrieval effort when this theme's claims need freshness. The seed four inherited URLs anchor framework and runtime code while this theme's single named crate, wiremock, has no row, so the queue can freshen routing docs it barely cites and cannot freshen the one ecosystem claim the file actually makes.

**Recommended default and causal basis.** Prioritize a dated wiremock fetch when refreshing this theme and use the existing rows only for their framework-freshness value one layer down. The template propagated one URL set across the rust backend cluster, fitting the playbook's crates and drifting from this theme's, leaving the mocking ecosystem, this file's only external dependency claim, without a fetch target.

**Operating conditions and assumptions.** URL structures remain stable and any docs fetch pins the version it observed. External rows serve future freshness verification, they confer no current-fact authority, all four remained unretrieved throughout this evolution.

**Failure boundary and alternatives.** Treating the rows as this theme's verification queue would spend retrievals confirming axum extractor docs while the wiremock idiom, the claim most likely to have drifted since 202604, has no queued source. Bounded alternatives and recoveries: reading a real service's dev-dependencies and their changelogs, which answers is our mocking stack current faster than any general documentation.

**Counterexample, gotchas, and operational comparison.** The tokio row has a genuine tangent here, async test runtimes affect harness design, but citing it for harness claims would substitute runtime authority for the testing file's pattern authority. Good: a dated wiremock release-notes check before asserting current mocking idioms. Bad: citing the api-guidelines row to freshen isolation semantics. Borderline: using axum docs for test-client patterns, adjacent and occasionally useful, still not a substitute for the pattern claims.

**Verification, evidence, and uncertainty.** Confirm externally-flavored claims name a dated retrieval or carry the unretrieved-candidate label. Zero fetches this assignment and the file's single named crate read in full. How far mocking-crate idioms have drifted since 202604 is unknowable without the fetch.

**Second-order consequence.** This theme's external surface is deliberately thin by design, the file teaches patterns, spawn, isolate, mock, that are crate-agnostic, naming wiremock only as representative, so most of its content cannot go stale through ecosystem drift at all, only its one example can.

**Revision decision.** Keep the rows as inherited candidates, flag the missing wiremock anchor, and route any real freshness need through a dated fetch of the wiremock repository or docs.

**Retained seed evidence.** All four external rows with their boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://github.com/rust-lang/api-guidelines | Rust API Guidelines | Rust library-team API design recommendations | external_research_sourced_fact |
| https://github.com/tokio-rs/tokio | Tokio repository | async runtime implementation and operational model | external_research_sourced_fact |
| https://github.com/tokio-rs/axum | Axum repository | Rust web framework implementation and design claims | external_research_sourced_fact |
| https://docs.rs/axum/latest/axum/ | Axum docs.rs | published crate documentation for routing and extractors | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which suite behaviors reviewers must reject on sight in this theme. The seed process rows miss the testing rejections the mapped file implies, fixed-port harnesses that collide, tests sharing undocumented infrastructure, suites hitting real external APIs, helpers hiding so much logic they stop helping, property tests substituting for end-to-end coverage, and unit-only suites certifying wiring they never exercised.

**Recommended default and causal basis.** Wire the greppable rejections into CI checks and assign the judgment ones, helper opacity and matrix coverage, as named review questions. Each rejection inverts one file rule, fixed ports invert the random-port rule, undocumented sharing inverts section 3's boundary mandate, live external calls invert the mocking section, opaque helpers invert the helper warning, property substitution inverts the selectivity clause, and unit-only suites invert the mindset itself.

**Operating conditions and assumptions.** Reviews see test diffs with the same attention as source diffs, suites decay precisely where review attention is absent. Test-suite failures only, application anti-patterns live with the playbook theme and pipeline failures with the ops theme.

**Failure boundary and alternatives.** These defects ship green suites, the collision is intermittent, the live API is usually up, and the unit tests genuinely pass, so each rejection surfaces first as flake investigations or as defects in production that the suite claimed to cover. Bounded alternatives and recoveries: platform-level flake quarantine tooling, which contains the symptom fleet-wide while leaving the registry's root causes unfixed per suite.

**Counterexample, gotchas, and operational comparison.** The live-API rejection has a legitimate-looking cousin, contract tests against a staging instance, the file's mocking doctrine still applies, staging calls belong in a separate deliberately non-deterministic suite, not inside the deterministic one. Good: blocking a test PR that binds port 8080 explicitly. Bad: approving a suite whose auth tests call the real identity provider. Borderline: a shared read-only reference dataset across tests, acceptable exactly when its isolation boundary is documented as section 3 demands.

**Verification, evidence, and uncertainty.** Check each registry row inverts a citable file rule and carries a working detection signal. The testing file's per-section rules and warnings read in full. Relative incidence of the six rejections in real Rust suites is unmeasured here.

**Second-order consequence.** Four of the six rejections are flake factories before they are correctness risks, ports, sharing, live APIs, and opaque helpers first present as intermittent failures, so a team's flake rate is an early integrity signal for this registry, worth reading before any defect escapes.

**Revision decision.** Import the six rejections with detection signals, grep for fixed ports and real external hosts in test code, review for isolation documentation, and audit helper opacity and matrix coverage per concern.

**Retained seed evidence.** The three seed process rows with their detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide what a backend change must demonstrate about its tests before merge. The seed document verifier stands alone while this theme's real gate is the matrix itself, six concern rows each naming its preferred test class, endpoint behavior to integration, domain invariants to unit or property, database work to integration with real migrations, remote APIs to mocks, auth flows to combined coverage, and migration safety to schema and rollout checks.

**Recommended default and causal basis.** Require a concern-to-test mapping note on substantial backend PRs and check it against the matrix's assignments. The matrix converts suite review from taste into table lookup, a change touching a concern row without its assigned test class is a visible gap, so gating on the matrix is gating on a checkable artifact rather than on reviewer intuition.

**Operating conditions and assumptions.** Changes are classifiable by concern, refactors touching no concern row pass with the standing suite as evidence. Suite-composition gates for this theme, pipeline execution gates belong to the ops theme's CI floor and packet gates to the entry theme.

**Failure boundary and alternatives.** Gating only on tests pass admits suites whose green status covers the wrong concerns, the matrix exists because passing is meaningless when endpoint behavior is certified by unit tests that never crossed the wire. Bounded alternatives and recoveries: coverage-percentage gates, cheaper to automate and unable to distinguish which concern a covered line certifies, the exact blindness the matrix was built to remove.

**Counterexample, gotchas, and operational comparison.** The migration-safety row chains outside this file, its schema and rollout checks are specified by the ops sibling, so enforcing that row means holding the change to another file's standards, the one matrix row that cannot be verified from this file alone. Good: an endpoint PR listing endpoint behavior and database writes with both assigned classes present. Bad: a merge justified by overall coverage rising. Borderline: a one-line fix skipping the mapping note, tolerable when the standing suite already covers its concern row.

**Verification, evidence, and uncertainty.** Sample recent substantial PRs for the mapping note and spot-check one concern row's assigned test actually exists. The testing file's matrix table and the delivery skill's verification-mix step read in full. The substantiality threshold at which the mapping note pays for itself is team-calibrated.

**Second-order consequence.** The matrix gate is bidirectional, it catches missing coverage and also over-coverage, a property-test suite on plain data transport fails the selectivity clause the same table encodes, so one artifact polices both under-testing and test theater.

**Revision decision.** Adopt the matrix as the review gate, each substantial change names its touched concerns and shows the assigned test class present, with the delivery skill's verification-mix step as the planning-time twin.

**Retained seed evidence.** The seed's document verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide what an agent must classify and reuse before generating tests under this theme. The seed four generic bullets stand where the bundle gives agents testing-specific instructions, the delivery skill's workflow makes agents choose the verification mix deliberately at step four, and the reference map routes agents here second on new endpoints and auth flows, after doctrine and before implementation.

**Recommended default and causal basis.** Require agents to emit the concern-to-test mapping alongside generated tests and to reuse the standing harness rather than inventing setup. Agents writing backend tests fail in a characteristic direction, they generate unit tests because units are visible in the diff, so an agent following this theme must be instructed to start from the matrix's concern classification, not from the code's module structure.

**Operating conditions and assumptions.** A harness exists for agents to ride, on harness-less services the agent's first assignment is the harness itself, reviewed by a human against section 2. Agent behavior over this theme's material, generic dispatch is the routing theme's guide and requirement writing the entry theme's.

**Failure boundary and alternatives.** An agent asked to add tests without matrix guidance produces mirror tests, one unit test per function touched, high coverage of exactly the wiring-blind kind the integration-first mindset exists to displace. Bounded alternatives and recoveries: restricting agents to test-skeleton generation with humans writing assertions, safer for subtle invariants, it forfeits the volume advantage on journey tests where agents are strongest.

**Counterexample, gotchas, and operational comparison.** Agents replicate whatever setup pattern they first see, one test that binds a fixed port or hits a live API seeds every subsequent generation with the same violation, so the suite's existing hygiene is the agent's effective style guide. Good: an agent PR adding a journey test through the harness with its concern row named. Bad: agent-generated unit tests asserting a handler returns whatever the handler returns. Borderline: an agent flagging that no concern row covers a new webhook path, exactly the escalation the matrix should trigger.

**Verification, evidence, and uncertainty.** Reject agent test PRs lacking the concern mapping or bypassing the standing harness. The delivery skill's step four, the reference map's orderings, and the harness design goal read in full. How reliably agents sustain harness reuse across long sessions lacks measurement.

**Second-order consequence.** The harness is what makes agent-generated integration tests reviewable, tests written through a journey-readable harness read as English user journeys a human can validate at a glance, so harness quality directly bounds how much test generation can be safely delegated.

**Revision decision.** Instruct agents to classify the change's concerns against the matrix, generate the assigned test classes through the spawned-app harness, and state which concerns each generated test certifies.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide which entry into this theme matches the reader's current suite situation. The seed one generic engineer stands in for this theme's three journeys, a suite founder standing up harness and isolation on a new service, a test author adding coverage for one change through the standing infrastructure, and a flake investigator tracing intermittent failures back to isolation debt.

**Recommended default and causal basis.** Identify the journey the current task belongs to and enter the file at that journey's sections rather than the beginning. The three journeys consume different sections at different tempos, the founder works through sections 2 and 3 once and carefully, the author touches the matrix and helpers per change, and the investigator reads section 3's isolation semantics under pressure with a red build behind them.

**Operating conditions and assumptions.** The reader knows their journey, flake investigations that are secretly missing-mock problems start in the investigator journey and resolve in section 4. Journeys through suite work, application-building journeys belong to the playbook theme and rollout journeys to the ops theme.

**Failure boundary and alternatives.** Documentation tuned only to the author journey fails the other two, the founder needs ordering guidance the matrix does not give, and the investigator needs the isolation rules findable fast, not embedded in setup prose. Bounded alternatives and recoveries: extracting per-journey runbooks from the file, faster in the moment, another shadow copy to keep synchronized with the archive original.

**Counterexample, gotchas, and operational comparison.** The author journey quietly accumulates the debt the investigator later pays, each test that bends isolation slightly is individually harmless, so the author journey needs the isolation rules visible per change, not only at founding. Good: a flake resolved in minutes by checking which tests share the schema the boundary note documents. Bad: a founder copying a fixed-port harness from an older service. Borderline: an author skimming property-test guidance for a plain CRUD change, harmless, the selectivity clause says skip it.

**Verification, evidence, and uncertainty.** Ask recent users of this theme which journey they ran and whether the file's structure served its tempo. The testing file's section tempos and the isolation documentation rule read in full. The actual frequency mix of the three journeys per team is unmeasured.

**Second-order consequence.** The founder journey is where the other two are won or lost, a harness built journey-readable makes every author's tests cheap, and isolation semantics documented at founding make the investigator's job a lookup instead of an excavation, the file's setup-heavy shape mirrors exactly this leverage.

**Revision decision.** Recast the scenario as three entries, founder through sections 2 and 3 in order, author through matrix and helpers, investigator straight to isolation semantics and the shared-infrastructure boundary rule.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Rust reliability engineer is starting from a requirement that needs a safe API, explicit error model, and testable boundary and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `rust_backend_testing_fixtures` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the idiomatic ownership, async, error, and crate-boundary shape before coding.
Reference opening trigger: Open this file when the task mentions rust backend testing fixtures, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how much realism, isolation, and helper abstraction each suite surface deserves. The seed template rows skip this theme's live tensions, suite speed versus fidelity to real infrastructure, isolation strictness versus setup cost per test, and helper abstraction versus test transparency.

**Recommended default and causal basis.** Test against real schema on isolated infrastructure through transparent helpers, and treat each deviation as a documented exception. The mapped file takes sides with stated reasons, real migrations in test setup because tests must see the real schema, per-test isolation because collisions poison trust, and intent-encoding helpers because a helper hiding too much stops helping.

**Operating conditions and assumptions.** Deviations carry named reasons, a fake substituting for a real dependency should state which behaviors it does not reproduce. Tuning within suite doctrine, application-design tradeoffs belong to the playbook theme and ceremony tradeoffs to the entry theme.

**Failure boundary and alternatives.** Each tension has a seductive wrong default, in-memory fakes that diverge from the real schema, one shared database because provisioning is slow, and mega-helpers that make tests short and meaningless. Bounded alternatives and recoveries: tiered suites, a fast unit tier on every commit and the full integration tier on merge, compatible with all three stances when the tiers' coverage claims stay honest.

**Counterexample, gotchas, and operational comparison.** The speed axis tempts suite-level compromise, making everything slightly less isolated to run faster, but flake cost is superlinear, one intermittent test taxes every build, so isolation should be relaxed per documented boundary or not at all. Good: accepting slower setup to run migrations so tests see production's schema shape. Bad: a shared mutable fixture trimming three seconds and adding weekly flakes. Borderline: an in-memory repository for pure domain tests, fine, those tests certify domain rows, never the database rows.

**Verification, evidence, and uncertainty.** Audit recent deviations from the three stances for their named reasons and revisit any reason that no longer holds. The testing file's explicit rationales in its isolation, migration, and helper sections read in full. The suite duration at which tiering becomes necessary is workload-specific.

**Second-order consequence.** All three stances privilege diagnostic cost over authoring cost, real infrastructure, strict isolation, and transparent helpers each make tests slower to write and dramatically faster to believe when they fail, the file consistently buys trust with authoring effort.

**Revision decision.** Add the three axes with the file's stances and the narrow conditions justifying deviation on each.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the rust backend testing fixtures pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong rust backend testing fixtures guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which document settles a verification question when several plausibly apply. The seed lone canonical row with its confidence warning understates a clean jurisdiction, this file is the bundle's final word on harness, isolation, mocking, helpers, property selection, and the matrix, while it defers what to validate to the playbook's domain doctrine and when tests run to the ops file's CI section.

**Recommended default and causal basis.** Resolve verification-technique disputes here, and read the named sibling whenever a question crosses into domain content or pipeline execution. The bundle partitions by risk surface, so hierarchy questions here are jurisdictional, which file owns the topic, and this file's ownership is everything about how backend behavior gets verified, not what the behavior should be.

**Operating conditions and assumptions.** The bundle stays internally consistent, an upstream revision that moves the matrix would redraw three consumers silently. Precedence within the bundle for verification questions, corpus-wide precedence is the adjacent-routing section's business.

**Failure boundary and alternatives.** The genuine seam invites misjudgment, the matrix's migration-safety row names checks the ops file specifies, so treating this file as sufficient for migration testing gives a row without its rules, half an answer wearing a whole one's confidence. Bounded alternatives and recoveries: treating the corpus's python testing themes as second opinions, useful for pattern shape, subordinate on Rust-specific harness and isolation mechanics.

**Counterexample, gotchas, and operational comparison.** SKILL.md's verification-mix step restates this file's options in compressed form, when the compression and the matrix diverge the matrix wins, the wrapper indexes doctrine, it does not hold it. Good: settling a mocking-strategy dispute from section 4 alone. Bad: deriving migration-check specifics from the matrix row that merely names them. Borderline: taking the playbook's testability arguments as verification doctrine, legitimate as motivation, the technique still lives here.

**Verification, evidence, and uncertainty.** Test hierarchy claims against each file's self-declared use statement and the consumption chain. All five bundle files' charters and this file's three named consumers read in full. No observed upstream revision yet tests how stable the consumption chain is.

**Second-order consequence.** This file is the bundle's most depended-upon reference, the delivery skill's step four, the ops file's CI floor, and three reference-map task orders all consume it, so its jurisdiction is small but its blast radius on revision is the bundle's largest, a hierarchy fact invisible from the file alone.

**Revision decision.** Record the jurisdiction, this file canonical for verification technique, playbook canonical for what domain rules exist, ops canonical for pipeline execution and migration-check specifics, with the migration row flagged as a two-file seam.

**Retained seed evidence.** The single hierarchy row and the confidence warning remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/rust-backend-testing-and-fixtures.md | canonical primary source | Rust Backend Testing And Fixtures; 1. Integration-Test-First Mindset; 2. Spawned-App Test Harness | What guidance, warning, or example should this source contribute to Rust Backend Testing Fixtures? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what standing record makes a suite's infrastructure and coverage reviewable without reading every test. The seed named artifact, a request lifecycle diagram, belongs to the playbook theme, this theme's natural object is a suite manifest, one page recording the harness entry point, the isolation strategy per resource, the documented sharing boundaries, the mock inventory for external systems, and the matrix coverage status per concern row.

**Recommended default and causal basis.** Create the manifest when the harness is founded and review it in every PR that touches test infrastructure. Every file rule presumes suite-specific facts nobody retains accurately, which teardown strategy this suite chose, which tests share what safely, which external APIs have mocks, and the manifest is where those facts live when the founder has moved on.

**Operating conditions and assumptions.** Suites are few enough for per-suite manifests, monorepos with many services generate the manifest's matrix block from test annotations instead. One manifest per service suite, operational wiring has the ops theme's card and dispatch vocabulary the routing theme's.

**Failure boundary and alternatives.** Without the manifest each flake investigation and each new author re-derives the isolation design from test code under pressure, and re-derivation is where undocumented sharing gets mistaken for isolation and trusted. Bounded alternatives and recoveries: encoding the manifest as doc comments on the harness module, closer to the code, invisible to the reviewer auditing coverage from the PR view.

**Counterexample, gotchas, and operational comparison.** The matrix-status block must record gaps honestly, a manifest claiming full concern coverage reproduces the false confidence the matrix gate exists to remove, unknown or missing is a valid and valuable entry. Good: a flake triaged in minutes because the manifest names which tests share the seeded schema. Bad: a new author discovering the teardown strategy by breaking it. Borderline: one manifest for five sibling services' suites, workable when their harnesses are genuinely shared, the first divergence poisons it.

**Verification, evidence, and uncertainty.** Quarterly, pick one manifest block and verify it against the suite's actual behavior. The file's per-section presumption of suite-specific facts and its documentation mandate read in full. Manifest upkeep discipline across team churn is the untested variable.

**Second-order consequence.** The manifest's boundary block operationalizes the file's only documentation mandate, section 3 requires shared infrastructure to have its boundary documented with a safety argument, and the manifest gives that mandate a standing home instead of a scattered comment.

**Revision decision.** Define the artifact as the suite manifest with five blocks, harness, isolation, boundaries, mocks, matrix status, updated in the same change as any infrastructure it describes.

**Retained seed evidence.** The artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: fixture plan with unit, integration, negative, and flaky-test handling.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Rust Backend Testing Fixtures | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which exercise most efficiently builds trustworthy suite-construction habits. The seed abstract usage lines replace the teaching walkthrough this theme wants, one new endpoint verified end to end through the full stack, spawn the app on a random port against an isolated migrated database, post the request, assert the response and the persisted row, then mock the downstream API and assert the outbound request shape.

**Recommended default and causal basis.** Run new backend contributors through the walkthrough and the drill on a practice service before they own suite changes. The walkthrough exercises five of the seven sections in one artifact, harness, isolation, journey readability, mocking, and the matrix's endpoint and database rows, so a single worked example carries most of the file's doctrine into muscle memory.

**Operating conditions and assumptions.** A practice service with real migrations exists, the walkthrough against a schemaless store teaches the motions but not the migration-fidelity judgment. Teaching suite construction, endpoint design walkthroughs belong to the playbook theme and migration drills to the ops theme.

**Failure boundary and alternatives.** Engineers who have only read the sections assemble them wrong under deadline, a spawned app against a shared database, or a mock asserting nothing about the outbound shape, integration theater that the walkthrough's assertions would have caught. Bounded alternatives and recoveries: studying an existing exemplary suite, cheaper and effective for shape, it cannot deliver the manufactured flake's lesson about what isolation debt feels like.

**Counterexample, gotchas, and operational comparison.** The mock half of the walkthrough is where learners over-trust defaults, a mock that matches any request passes everything, so the walkthrough must include the outbound-shape assertion failing once before being written correctly. Good: a trainee's walkthrough diary noting the flake vanishing when the second schema was provisioned. Bad: certifying suite competence from a single happy-path unit test. Borderline: practicing with an in-memory database, gentler, migration fidelity is exactly the lesson lost.

**Verification, evidence, and uncertainty.** Have the trainee stand up a fresh endpoint test unsupervised and audit it against the five exercised sections. The testing file's harness, isolation, and mocking assertions read in full. How long the habits persist without periodic suite founding is unmeasured.

**Second-order consequence.** The failure drill teaches what green suites cannot, flakes from isolation debt reproduce only under interleaving, so experiencing one manufactured flake converts the isolation rules from setup pedantry into remembered pain, the cheapest vaccination the suite can buy.

**Revision decision.** Anchor the section on the endpoint walkthrough plus one failure drill, deliberately break isolation by pointing two tests at one schema and watch the intermittent failure appear and disappear.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Rust Backend Testing Fixtures after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Rust Backend Testing Fixtures as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Rust Backend Testing Fixtures only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which measurements prove this theme's suite discipline pays for itself. The seed compile-centric indicator ignores suite feedback, nothing counts defects caught by integration tests versus escaped to production, flake rate as the isolation-debt signal, or matrix coverage per concern row across the suite.

**Recommended default and causal basis.** Label the three event streams as they occur and review the ratios quarterly beside the escaped-defect count. Each ratio measures one doctrine claim in operation, catch-versus-escape tests the integration-first bet, flake rate tests the isolation rules, and matrix coverage tests whether the concern-to-class assignments are actually being honored.

**Operating conditions and assumptions.** Retrospectives honestly classify which test class could have caught each escape, hindsight classification drifts optimistic without a named rubric, the matrix is that rubric. Measuring this theme's suite disciplines, pipeline health belongs to the ops theme's loop and dispatch discipline to the entry theme's.

**Failure boundary and alternatives.** Without the ratios the integration-first stance stays a creed, and creeds lose to deadlines the first quarter someone proposes skipping the harness work because unit tests are faster to write. Bounded alternatives and recoveries: coverage-percentage tracking, cheaper and already tooled, unable to say which concern any covered line certifies, the blindness that motivated the matrix.

**Counterexample, gotchas, and operational comparison.** A falling flake rate can mean improving isolation or growing quarantine lists, pair the ratio with the quarantined-test count before celebrating. Good: a quarter showing wiring defects dying in CI while the escape count holds at zero. Bad: defending harness investment with no data when its cost is questioned. Borderline: counting a quarantined flake as resolved, the quarantine is triage, the ratio should still carry it.

**Verification, evidence, and uncertainty.** Confirm the three ratios exist, cite real event streams, and were consumed at the last quarterly review. The alignment between the file's doctrine claims and their measurable suite signatures. Healthy baseline values for the ratios await the first measured quarters.

**Second-order consequence.** Flake rate is the leading indicator of the three, isolation debt produces flakes months before it produces escaped defects, so a rising flake trend is the cheapest early warning this theme offers, actionable while the fix is still a boundary note rather than a rewrite.

**Revision decision.** Add the three ratios with their collection points, defect retrospectives for catch-versus-escape, CI retry records for flake rate, and the suite manifest's matrix block for coverage.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: compile attempts and review comments decrease because the API shape is explicit before implementation.
Failure signal: the reference hides ownership or error tradeoffs behind generic guidance.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what must be confirmed before this testing reference is declared faithful. The seed shape items never audit fidelity to the mapped file's countable content, seven sections, four unit-test territories, four harness properties, four isolation rules, three mock assertion classes, four helper roles, four property-test targets, and six matrix rows.

**Recommended default and causal basis.** Run the count-and-pairing audit at every reread cycle and after any archive change touching the bundle. This theme's claims transcribe an enumerable source, so completeness reduces to counting the enumerables against the file and diffing the matrix table, whose concern-to-class pairings are the payload most damaged by paraphrase drift.

**Operating conditions and assumptions.** The 202604 file remains at its path for line-level comparison. Auditing this reference document against its source, auditing live suite practice belongs to the metrics loop and the matrix gate.

**Failure boundary and alternatives.** Count-passing paraphrase is the residual risk, a matrix row reworded to endpoint behavior, any tests keeps the row count at six while deleting the assignment that made the table a gate. Bounded alternatives and recoveries: checksumming the mapped file and re-auditing on change only, efficient, blind to drift introduced by this document's own future edits.

**Counterexample, gotchas, and operational comparison.** Auditing this document against memory of the testing file rather than the file itself is the failure mode all corpus audits share, the check costs minutes only when the source is actually opened. Good: an audit catching a matrix cell that swapped mock tests for integration tests. Bad: declaring fidelity because all 26 headings and both tables exist. Borderline: accepting paraphrased helper-role wording, tolerable, the four roles and their count must survive exactly.

**Verification, evidence, and uncertainty.** Count the enumerables and diff the matrix cell by cell against the live mapped file. The fully enumerable structure of the 91-line testing file read in full. Whether cell-level auditing needs corpus tooling remains open.

**Second-order consequence.** The matrix deserves cell-level treatment because it is the file's only table and its consumers' contract, three sibling files route through it, so a drifted cell here propagates as wrong doctrine into every consumer, the highest-leverage sixty cells in the theme.

**Revision decision.** Add the count items and an exact-pairing check on the matrix table, concern and preferred class compared cell by cell, each audit cycle.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Rust Backend Testing Fixtures.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send a test-flavored question this theme does not own. The seed token-split rows point nowhere while this theme's real neighbors are exact, the playbook theme for what domain rules the tests should verify, the ops theme for CI execution and migration-check specifics, the security sibling's theme for auth-flow content behind the matrix's auth row, and the routing theme for which file a task reads first.

**Recommended default and causal basis.** Test each arriving question for technique versus content, answer technique here, and forward content with its destination named. Verification touches every concern, so this theme accumulates questions that merely sound like testing, a what-should-this-validate question is domain doctrine, and a when-do-tests-run question is pipeline doctrine, each wearing test vocabulary.

**Operating conditions and assumptions.** Destination themes exist under their expected corpus names, the routing theme's pointer probes keep this checkable. Sending away what this theme cannot own, summaries of the destinations' content are deliberately absent.

**Failure boundary and alternatives.** Keeping every test-flavored question here dilutes the file's clean jurisdiction, technique, into a general quality helpdesk answering domain and pipeline questions shallowly. Bounded alternatives and recoveries: for test-framework specifics no local theme covers, crate documentation externally labeled unretrieved.

**Counterexample, gotchas, and operational comparison.** Mocking questions never leave this theme even when they name external services, the service's API shape is content, but how to simulate and assert against it is technique, the split runs through the middle of most mocking questions. Good: forwarding a what-makes-a-password-valid question to domain doctrine while keeping its property-test structure here. Bad: answering a CI-scheduling question because it mentions the test suite. Borderline: a fixture-data realism question, mostly technique, the data's business meaning still belongs next door.

**Verification, evidence, and uncertainty.** Sample recent forwarded and kept questions against the technique-versus-content test. The jurisdiction partition read across all five bundle files. Misroute frequency into this theme lacks measurement.

**Second-order consequence.** The matrix is this section's built-in router, each of its six rows names a concern whose content lives elsewhere while its verification class lives here, so the table doubles as an adjacency map, read the row for the class, follow the concern to its owning theme.

**Revision decision.** Route by jurisdiction, keep harness, isolation, mocking, helpers, property selection, and matrix questions here, and forward domain content, pipeline execution, auth semantics, and dispatch to their owners.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use backend, executable, or quality-gate Rust references when the question shifts to HTTP delivery, specs, or review gates.
Adjacent reference 1: consider the rust adjacent reference when the current task pivots away from rust backend testing fixtures.
Adjacent reference 2: consider the backend adjacent reference when the current task pivots away from rust backend testing fixtures.
Adjacent reference 3: consider the testing adjacent reference when the current task pivots away from rust backend testing fixtures.

## Workload Model

**Decision supported.** This section helps decide how to budget suite effort so founding, authoring, and maintenance are each priced correctly. The seed endpoint-count budgets fit request work, not suite work, whose real units are founding cost per service paid once for harness and isolation, marginal cost per test riding the standing infrastructure, and maintenance cost per infrastructure change when migrations or dependencies shift under the suite.

**Recommended default and causal basis.** Budget the founding as a project, drive marginal cost down through harness quality, and slot maintenance into every schema or dependency change rather than deferring it. The three units scale on different axes, founding scales with service count, marginal cost scales with test count and dominates authoring economics, and maintenance scales with schema and dependency churn, so a single number cannot budget them together.

**Operating conditions and assumptions.** The service will accumulate enough tests to amortize founding, throwaway prototypes may rationally skip the harness and say so. Budgeting suite effort for services adopting this theme, application-slice budgets belong to the playbook theme and rollout budgets to the ops theme.

**Failure boundary and alternatives.** Budgeting suites at marginal cost alone is the classic error, the first integration test costs days because it carries the harness, and plans that price it like the fiftieth test conclude falsely that integration testing is too expensive to start. Bounded alternatives and recoveries: shared platform harnesses across services, cutting founding cost fleet-wide at the price of per-service isolation semantics becoming somebody else's abstraction.

**Counterexample, gotchas, and operational comparison.** Maintenance is the forgotten unit, a migration that changes the schema breaks fixtures silently, and suites without budgeted maintenance decay into the quarantine lists the metrics loop warns about. Good: a plan pricing the first endpoint test at harness cost and the next twenty at hours each. Bad: rejecting integration testing because the first test's estimate looked absurd. Borderline: batching fixture repairs into quarterly cleanups, workable, each broken window meanwhile teaches authors to bypass the fixtures.

**Verification, evidence, and uncertainty.** Compare recent suite estimates against actuals split by the three units. The testing file's infrastructure-heavy structure and its amortization logic read in full. Typical founding cost for a well-templated Rust service is unestimated here.

**Second-order consequence.** The file's economics run on one ratio, founding cost divided across all future tests, every harness improvement is a price cut on every subsequent test, which is why the dependency-chain ordering front-loads exactly the work that compounds.

**Revision decision.** Restate the model in three units, founding cost per service, marginal cost per test with the harness as its divisor, and maintenance cost per infrastructure shift.

**Retained seed evidence.** The workload dimension rows with boundary values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Rust Backend Testing Fixtures as a backend service operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | service implementation, route review, worker execution, and operational hardening work where a single wrong recommendation can affect live request handling | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one service boundary, up to 25 endpoints or workers, 1000 representative requests, and one deploy rollback path per review batch | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Rust Backend Testing And Fixtures; 1. Integration-Test-First Mindset; 2. Spawned-App Test Harness; 3. Random Port And Isolated Database Setup; 4. HTTP | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is fixture plan with unit, integration, negative, and flaky-test handling | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which suite invariants must demonstrably hold for this theme's guidance to count as adopted. The seed document-property thresholds stand where suite invariants should, zero fixed ports in test code, every shared resource carrying a documented isolation boundary, every external integration mocked in the deterministic suite, and every substantial change mapped to its matrix rows.

**Recommended default and causal basis.** Wire the three mechanical targets into CI and hold the boundary target in infrastructure review. Each target is a file rule stated as an invariant, the port rule from section 3, the boundary mandate from its closing sentence, the mock target from section 4's doctrine, and the mapping target from the matrix's role as the verification-mix contract.

**Operating conditions and assumptions.** Test code is distinguishable from source for the greps, unconventional layouts need the manifest to name the test roots. Suite invariants for services under this theme, service-behavior targets belong to the playbook theme and pipeline targets to the ops theme.

**Failure boundary and alternatives.** Targets averaged over time hide the binary ones, one live external call in the deterministic suite is one nondeterminism source taxing every build, not a tolerable percentage. Bounded alternatives and recoveries: quarantine-based containment, tolerating violations and isolating their blast radius, honest as triage and corrosive as policy.

**Counterexample, gotchas, and operational comparison.** The mock target needs its staging exception stated, deliberately non-deterministic contract suites against staging are legitimate, the invariant binds the deterministic suite only, and the manifest should name which suite is which. Good: CI failing a PR that hard-codes port 5432 in a test. Bad: declaring isolation from the absence of recent flakes. Borderline: waiving the mapping target for a refactor PR, reasonable, the standing suite is the evidence and the waiver should say so.

**Verification, evidence, and uncertainty.** Review the four target audits together at each release checkpoint with their evidence artifacts attached. The testing file's port, boundary, mocking, and matrix rules read in full. Grep precision for live-host detection across HTTP client styles is implementation-dependent.

**Second-order consequence.** Three of the four targets are enforceable by machine, ports, hosts, and mapping notes are greppable or template-checkable, leaving only the boundary-documentation target to human review, so the target set is cheap to hold once wired, its cost is the wiring, not the vigilance.

**Revision decision.** Publish the four targets with their evidence methods, grep for ports and hosts, manifest review for boundaries, mock-inventory diff for coverage, and PR audit for matrix mapping.

**Retained seed evidence.** All four seed reliability rows with thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which decay modes need standing probes and what each probe inspects at the growth edge. The seed generic drift and surge rows miss how suite discipline decays, isolation debt where new tests quietly share what founding kept separate, harness bypass where authors hand-roll setup because the helper confused them once, mock rot where simulated behaviors drift from the real API's current shape, and matrix drift where new concern classes appear with no assigned test kind.

**Recommended default and causal basis.** Run the PR-cycle probes in review and the calendar probe quarterly, attributing each finding to its decay mode. All four decay through accretion at the suite's growth edge, existing tests stay correct while new tests route around the discipline, so diff review that checks the new test's assertions and not its infrastructure choices misses every one.

**Operating conditions and assumptions.** Probes are owned, an unowned probe list is the erosion mode applied to the failure table itself. Decay of suite discipline, application-boundary erosion belongs to the playbook theme and pipeline decay to the ops theme.

**Failure boundary and alternatives.** Each mode presents as its own absence, shared state passes until interleaving changes, bypassed harnesses still spawn apps, stale mocks still match, and unmapped concerns still ship tested-looking code, the decay surfaces as flakes and escapes long after the causal PR merged. Bounded alternatives and recoveries: periodic suite game-days that shuffle test order and re-record external contracts, expensive, they test the accumulated truth no per-PR probe can.

**Counterexample, gotchas, and operational comparison.** Harness bypass is self-reinforcing, each hand-rolled setup makes the next author likelier to copy it than to learn the harness, so the probe should catch the first bypass, the second is already a faction. Good: review catching a new test importing the database pool directly around the harness. Bad: trusting mocks last verified against the API two majors ago. Borderline: a documented harness bypass for one exotic websocket test, acceptable, the manifest should record why.

**Verification, evidence, and uncertainty.** Confirm each failure row names its probe, owner, and cadence, and sample one probe's recent findings. The accretion-shaped bypass structure read against each testing-file rule. Decay onset speed relative to suite growth rate is unmeasured.

**Second-order consequence.** Mock rot is the only row with an external clock, the real API drifts on the provider's schedule regardless of local discipline, so its probe must be calendar-driven while the other three ride the PR cycle, one table, two cadences.

**Revision decision.** Add the four rows with growth-edge probes, isolation review on every new fixture, harness-usage grep across new tests, periodic mock-versus-contract comparison, and a matrix review whenever a new external system or concern class lands.

**Retained seed evidence.** All four seed failure rows with mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| request surge overloads path | traffic spikes exceed handler, pool, or coroutine limits | apply rate limits, queue bounds, cancellation, and rollback playbook before rollout |
| security boundary silently fails | auth, permission, or input validation assumptions are untested | run abuse-case tests and require explicit deny-by-default behavior |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide which suite failures may rerun and what any rerun's result is allowed to mean. The seed corpus-process bullets stand where suite retry doctrine should, a failing test and a flaking test demand opposite responses, deterministic failures are signal to fix forward, while retry-until-green on a flake is evidence destruction, each retry teaches the team the suite lies.

**Recommended default and causal basis.** Fail the build on any deterministic-suite failure, route detected flakes to quarantine with an owner and a deadline, and cap the quarantine list as a standing gate. The file's isolation rules exist precisely so failures are deterministic, when they are, rerunning changes nothing and fixing is the only move, and when they are not, the flake is an isolation-debt report whose correct handling is diagnosis, not dice-rolling.

**Operating conditions and assumptions.** The pipeline distinguishes suites, a deliberately non-deterministic staging-contract suite may retry within stated bounds, the deterministic one may not. Retry semantics for suite failures, application-level retry doctrine belongs to the security sibling's territory one layer down.

**Failure boundary and alternatives.** Auto-retry policies that rerun failed tests until they pass convert the suite's honesty into noise, masked flakes accumulate as isolation debt while green builds certify less each week, the suite equivalent of rerunning a failed migration blindly. Bounded alternatives and recoveries: statistical flake detection that reruns everything and reports pass rates, informative at platform scale, it institutionalizes the retry-as-acceptance habit the regime exists to forbid.

**Counterexample, gotchas, and operational comparison.** Backpressure applies to suite growth, a team whose quarantine list grows monthly should stop adding integration tests and repay isolation debt first, more tests on a flaking foundation multiply the noise, not the coverage. Good: a red build fixed forward because the failure reproduced identically twice. Bad: a merge on the third rerun's green. Borderline: rerunning once to classify a suspected flake, legitimate exactly when the result routes to quarantine rather than to merge.

**Verification, evidence, and uncertainty.** Inject a deterministic failure and a manufactured flake on a practice branch and confirm each takes its regime's path. The determinism the isolation rules purchase and its retry implications read from the testing file. The quarantine-list cap that balances honesty against delivery pressure is team-calibrated.

**Second-order consequence.** One deliberate rerun is legitimate as an instrument, running a suspected flake twice distinguishes deterministic from intermittent, the regime forbids retry as acceptance while keeping it as diagnosis, the same action with opposite meanings depending on what consumes the result.

**Revision decision.** Add the two-regime rule, no automatic retries in the deterministic suite, and a diagnose-then-quarantine path for detected flakes with the quarantine list burning down visibly.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence suite work must emit for its discipline to be auditable. The seed generic counters replace the record set suite work needs, which tests ride the harness versus bypass it, which resources each test isolates versus shares, which external behaviors each mock simulates, and which matrix rows each substantial change claims to cover.

**Recommended default and causal basis.** Wire the four records into naming conventions, the manifest, and PR templates rather than into separate tooling. Each record serves a distinct consumer, harness records serve the bypass probe, isolation records serve the flake investigator, mock inventories serve the rot probe, and mapping records serve the matrix gate, the four probes of the failure table each need their record stream.

**Operating conditions and assumptions.** Conventions are actually enforced, self-reporting decays into misreporting the first quarter names stop being reviewed. What suite work must record, service runtime telemetry belongs to the ops theme's checklist.

**Failure boundary and alternatives.** Unrecorded mock behavior is the quiet loss, a mock's simulated responses live only in test code, so when the real API drifts nobody can list what the suite believes about it without reading every mock, the inventory is what makes rot detectable. Bounded alternatives and recoveries: coverage tooling as the record system, rich on line detail and empty on the semantic fields, concern rows and isolation semantics, that make these records useful.

**Counterexample, gotchas, and operational comparison.** Mock inventories can rot like the mocks themselves, an inventory maintained by hand drifts from the code, so the inventory should be generated from the mock definitions where the framework allows, recorded truth beats transcribed truth. Good: a flake investigation starting from the manifest's sharing table instead of a code excavation. Bad: answering what do we mock about the payment API by grepping. Borderline: recording matrix mappings only for new endpoints and not refactors, defensible, the waiver convention should say so.

**Verification, evidence, and uncertainty.** Pick a recent test and locate all four records from its artifacts alone. The artifact-embedded nature of the harness, isolation, and mocking rules read in full. The suite size at which hand-maintained inventories must become generated is team-specific.

**Second-order consequence.** Test names are the cheapest record surface, a convention encoding the journey and the concern row into the name makes the suite self-reporting, coverage questions answered by listing test names instead of reading test bodies.

**Revision decision.** Define the emission floor, harness usage visible per test, isolation semantics in the manifest, mock inventory per external system, and matrix mapping per substantial PR, kept in the artifacts the discipline already produces.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture error count, timeout count, retry count, saturation signal, and rollback trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove the suite's trust infrastructure stays fast enough to keep running. The seed request-latency ceilings measure the service, this theme's performance surfaces are suite wall time as the delivery tax every merge pays, per-test setup cost as the isolation price, and time-to-first-test on a new service as the founding friction.

**Recommended default and causal basis.** Record the three measurements per release and investigate any surface whose trend breaks its historical band. The file's choices all spend suite performance to buy trust, real migrations, per-test provisioning, and spawned apps each cost seconds, so the doctrine's sustainability depends on those seconds staying bounded, an unmeasured suite quietly becomes the bottleneck its critics predicted.

**Operating conditions and assumptions.** Suite runs are instrumented for timing, most test frameworks emit this for free once asked. Verifying suite performance, service latency belongs to the playbook theme's SLO clause and pipeline duration to the ops theme.

**Failure boundary and alternatives.** Ignoring suite performance lets it decay until developers stop running tests locally, at which point defects surface in CI or later, the trust the infrastructure bought is refunded as latency. Bounded alternatives and recoveries: fixed suite-duration budgets, simpler to enforce, they age poorly as legitimate coverage grows and invite exactly the isolation compromises the review would catch.

**Counterexample, gotchas, and operational comparison.** Wall-time optimization tempts isolation compromise first because sharing is the easiest speedup, the trend alarm should therefore trigger an optimization review, not an optimization, the review's first question is which speedups leave the boundaries intact. Good: a trend review catching setup time doubling after a migration added seed data. Bad: developers skipping local runs because the suite crossed ten minutes unremarked. Borderline: tolerating a slow founding on an exotic stack, defensible, the marginal cost per test is what must stay flat.

**Verification, evidence, and uncertainty.** Inspect the three trend series and confirm each release appended its measurements. The per-test infrastructure costs implied by the file's isolation and migration rules read in full. Reasonable trend bands for suite wall time vary widely with database choice.

**Second-order consequence.** The setup-versus-assertion split is the diagnostic ratio, a suite whose runtime is mostly setup is paying isolation costs that parallelization or template databases can cut without touching a single assertion, the split says where optimization is safe.

**Revision decision.** Measure the three surfaces with trend alarms, total wall time per suite run, setup-versus-assertion time split per test, and calendar time from service founding to first green integration test.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require a service-specific SLO before deployment; absent that, keep local verification to p95 under 200 ms and p99 under 500 ms for representative handlers or document why latency does not apply.
Leading indicator to measure: compile attempts and review comments decrease because the API shape is explicit before implementation.
Failure signal to watch: the reference hides ownership or error tradeoffs behind generic guidance.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what service count, datastore topology, or suite duration this theme's guidance must be re-derived rather than stretched. The seed document-scale bounds stand where suite scale seams should, the file's guidance assumes one service, one database, and a suite one team runs whole, and each assumption has a breaking point, multi-service integration exceeding the spawned-app harness, shared datastores breaking per-test provisioning, and suite duration forcing selective execution.

**Recommended default and causal basis.** Operate the doctrine as written within the assumptions, and treat each trigger as a design event for the suite, not a workaround opportunity. The harness spawns one application, so tests spanning services need contract tests or environment-level orchestration the file does not cover, and per-test database provisioning assumes a database the test owns, both assumptions named in the file's own mechanics.

**Operating conditions and assumptions.** Growth events are noticed, a second service added to a journey crosses the sharpest seam the day its call ships, not the day its test flakes. Bounding this theme's suite doctrine, service architecture seams belong to the playbook theme and rollout seams to the ops theme.

**Failure boundary and alternatives.** Stretching the harness across seams produces the worst of both worlds, multi-service tests through one service's harness assert against half a system, and shared-store provisioning that pretends to isolate reproduces the undocumented-sharing anti-pattern at architecture scale. Bounded alternatives and recoveries: adopting contract-test infrastructure from day one regardless of service count, paying orchestration cost early to never track the multi-service seam.

**Counterexample, gotchas, and operational comparison.** Tiered execution's honesty clause matters most, a fast tier advertised as the suite quietly demotes the integration tier to nightly noise, tiers are legitimate only while every merge still answers to the full matrix somewhere. Good: a cross-service journey split into two harness tests plus one contract pair. Bad: one mega-test spawning three services through hand-rolled orchestration. Borderline: schema-per-test on a shared warehouse, workable when the schema boundary is documented as section 3 demands.

**Verification, evidence, and uncertainty.** At each growth event, re-test the three assumptions and record which seams the event crossed. The single-app harness mechanics and per-test provisioning assumptions read in full. The suite duration at which tiering becomes necessary varies with team tooling.

**Second-order consequence.** The seams share a signature, each appears first as a test that is awkward to write, the awkwardness is the doctrine reporting that its assumptions no longer hold, so hard-to-write tests deserve architectural attention before authorial persistence.

**Revision decision.** Name the three seams with their triggers, a second service in one journey triggers contract-test strategy, a shared datastore triggers schema-level isolation design, and suite duration past local patience triggers tiered execution with honest tier labels.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Rust Backend Testing Fixtures stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which probes reveal that this theme's testing examples or patterns have gone stale. The seed theme-name queries would surface generic testing content while this theme's staleness lives in named places, the wiremock crate the file cites as its representative example, the property-testing ecosystem behind section 6, and the upstream bundle's own revision state.

**Recommended default and causal basis.** Run the crate probes on the faster cadence, dating each finding against the 202604 anchor, and check the archive at every corpus refresh. Testing-tool idioms churn faster than testing doctrine, mocking APIs reshape, property-test frameworks evolve, and harness conveniences appear, so this theme's one named crate and its tool-shaped advice date faster than its pattern advice.

**Operating conditions and assumptions.** Probe findings are triaged into example-breaking versus pattern-breaking before any rewrite, most churn will be the former. Refreshing this document's ecosystem and lineage claims, principle-level refresh rides on upstream bundle revisions watched by the routing theme's probes.

**Failure boundary and alternatives.** Name-based searching returns tutorials that neither confirm nor deny whether the 202604 wiremock idiom still matches current releases, the only ecosystem question a refresh of this theme needs answered. Bounded alternatives and recoveries: pinning this document explicitly to the 202604 idiom set and marking the ecosystem example archive-dated, zero probe cost, honest, increasingly less useful.

**Counterexample, gotchas, and operational comparison.** Property-testing probes skew toward advocacy content, the file's selectivity clause, strongest at the domain edge and no substitute for end-to-end tests, is the local doctrine any enthusiastic finding must be read against. Good: a probe noting a wiremock major release and dating the affected mocking example. Bad: logging that rust testing tutorials say nothing new. Borderline: probing new harness-generation tools, adjacent and promising, findings extend the doctrine rather than refresh it.

**Verification, evidence, and uncertainty.** Record each probe with its date and the specific example or pattern it confirmed or flagged. The file's named crate, its property-testing section, and the 202604 bundle date read from the mapped files. Actual churn rates of the testing crates since 202604 are unknowable without the fetches.

**Second-order consequence.** The probes split by what can invalidate what, crate releases can invalidate the example and the tool-shaped tips but not the spawn-isolate-mock pattern, while a bundle revision can invalidate the pattern too, so the archive watch is lower frequency but higher consequence.

**Revision decision.** Replace the name queries with targeted probes, wiremock release notes since 202604, current Rust property-testing framework state, and the archive watch for a revised bundle.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | rust backend testing fixtures official documentation best practices |
| `github_repository_query_phrase` | rust backend testing fixtures GitHub repository examples |
| `release_notes_query_phrase` | rust backend testing fixtures changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide under what label and with what attached caveats each claim here may be reused. The seed label definitions stand without this assignment's ledger, one mapped testing file read fully, five bundle companions read fully and cited by name, zero external URLs fetched, and every suite-practice construct above marked as inference.

**Recommended default and causal basis.** Before reusing a claim, identify its stratum, cite section for facts, date the ecosystem example, and attach reasoning to inference. The fact stratum is the file's transcribable content, seven sections, the unit-test territories, the harness properties, the isolation rules, the mock assertion classes, the helper roles, the property targets, and the six matrix pairings, while the manifests, ratios, probes, regimes, and seams are this evolution's constructed machinery.

**Operating conditions and assumptions.** The archive path stays stable so fact-class claims remain mechanically checkable. Reuse rules for this document's claims, transcribed doctrine travels with file-and-section citations, constructed machinery travels only with its reasoning.

**Failure boundary and alternatives.** The costliest mislabel would present wiremock as the currently recommended mocking crate, the file offers it as a representative ecosystem example from 202604, and the difference between representative-then and recommended-now is exactly what the label protects. Bounded alternatives and recoveries: per-paragraph inline labels if the stratum-level split ever proves too coarse for a dispute.

**Counterexample, gotchas, and operational comparison.** The journey-readability phrase travels especially well, a test should read like a user journey, not a dependency graph is quotable doctrine, and its source is the harness section specifically, quoting it as general test philosophy without the citation unmoors it from the harness design it constrains. Good: reusing the isolation rules with their section citation. Bad: citing the suite manifest as bundle doctrine. Borderline: reusing the integration-first mindset for a GraphQL service, the logic carries, the HTTP framing should travel with it.

**Verification, evidence, and uncertainty.** Sample claims from earlier sections and confirm each declares its stratum cleanly. This assignment's read ledger, six bundle files read in full, zero retrievals. Readers can check the citations but not the reading behind them.

**Second-order consequence.** The matrix needs its own reuse rule, its pairings are quotable fact but their force is contractual, three sibling files consume them, so quoting a pairing without noting its consumers understates what a change to it would break, the fact travels with a blast radius.

**Revision decision.** Publish the strata, countable testing-file content as local corpus fact, sibling-cited chains as by-name local fact, and all practice machinery as combined-evidence inference.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
