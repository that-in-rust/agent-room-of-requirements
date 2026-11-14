# Rust Backend Runtime Operations

**Decision supported.** This section helps decide which operational doctrine a Rust backend adopts for configuration, telemetry, and rollout before its first deploy. The seed title names runtime operations but the seed never states the ops file's organizing arc, its eight sections walk a service from boot to rollout, configuration parsed once at startup, secrets redacted, traces correlated, readiness distinguished from liveness, CI gated, images kept small, and schema changes sequenced for zero downtime.

**Recommended default and causal basis.** Parse configuration once at startup into typed settings, fail fast on invalid state, and plan every schema change as an ordered multi-step rollout. Operational failures cluster at transitions, boot, deploy, and migrate, so the file front-loads fail-fast behavior, invalid configuration should kill the process at startup rather than misbehave at runtime, and impossible rollout orderings should be rejected at planning rather than discovered in production.

**Operating conditions and assumptions.** Deployments can be staged and observed, a service deployed by copying a binary to one box exercises little of the sequencing half. This reference covers configuration, secrets, telemetry, CI, containers, and rollout for Rust backend services, service anatomy belongs to the playbook theme and auth or retry semantics to the security sibling.

**Failure boundary and alternatives.** Reading operations as polish applied after delivery inverts the file's stance, its own framing treats tracing, correlation, health checks, and failure classification as design concerns baked in from the start. Bounded alternatives and recoveries: platform-managed operations where the host absorbs config layering and health semantics, thinning some sections while migration sequencing survives untouched.

**Counterexample, gotchas, and operational comparison.** Zero-downtime discipline is conditional, the ops file mandates the four-step schema pattern whenever multiple instances or staggered rollouts are possible, single-instance shops inherit the mandate the day they add a second instance. Good: a service that refuses to boot on a missing database URL and logs a typed settings error. Bad: runtime string lookups of environment variables scattered through handlers. Borderline: config parsed at startup but held as raw strings, half the doctrine, invariants still unenforced.

**Verification, evidence, and uncertainty.** Boot the service with deliberately broken configuration and confirm it dies loudly at startup with a specific complaint. Full read this session of the 89-line runtime-and-ops file and its four sibling bundle files. How the doctrine maps onto serverless or edge runtimes is beyond what the mapped file discusses.

**Second-order consequence.** Six of the eight sections defend a single principle, the process must never run in a state it cannot explain, typed settings, redacted secrets, correlated traces, and honest readiness are all explanations the service carries about itself.

**Revision decision.** Open with the boot-to-rollout arc so readers see one lifecycle, not eight disconnected ops topics.

**Retained seed evidence.** The exact theme title and operations framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source justifies each operational claim class in this theme. The seed one local row carries the whole theme while the ops file leans on its bundle, the reference map routes migration and deployment tasks here, SKILL.md's Operations Mode activates it, and the testing sibling supplies the migration-aware tests its CI section requires.

**Recommended default and causal basis.** Cite the ops file for config, secrets, tracing, health, CI, image, and sequencing claims, named siblings for chained material, externals as candidates only. Operational guidance is chained guidance, a CI expectation references tests defined in the testing sibling and a rollout step references schema shapes owned by persistence doctrine in the playbook, so cross-file claims need by-name citations beyond the single mapped row.

**Operating conditions and assumptions.** The 202604 archive path remains stable for citation resolution. Provenance for this document's statements only, the table does not vouch for the four external URLs, none retrieved during this evolution.

**Failure boundary and alternatives.** Attributing a chained claim to the mapped row alone, for instance quoting harness isolation rules as ops-file content, breaks the provenance the table exists to preserve. Bounded alternatives and recoveries: a future mapping revision adding rows for the named observability crates, aligning the external queue with the file's actual examples.

**Counterexample, gotchas, and operational comparison.** The external rows again omit the crates the file itself names, secrecy, tracing, and tracing-subscriber have no URL row, so the candidate queue misses the theme's most citable ecosystem anchors. Good: citing the ops file's section 8 for the four-step schema pattern. Bad: citing the tokio repository row for tracing guidance it does not anchor. Borderline: citing the reference map for when Operations Mode applies, correct by name, outside the mapped row.

**Verification, evidence, and uncertainty.** Trace disputed claims to the exact ops-file section or named sibling that contains them. Full reads this session of the ops file and all five bundle companions. Whether the omitted crate anchors were deliberate template choices is unrecorded.

**Second-order consequence.** Among the bundle's three risk files this is the only one whose subject, deployment, is inherently unverifiable from source alone, its claims prove out only in rollout behavior, making evidence discipline here more operational than textual.

**Revision decision.** Anchor on the ops file and cite chained bundle files explicitly wherever their content, not just their existence, is used.

**Retained seed evidence.** The single local row and all four external rows with their column values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/rust-backend-runtime-and-ops.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://github.com/rust-lang/api-guidelines | external_research_source_material | external_research_sourced_fact | Rust library-team API design recommendations |
| https://github.com/tokio-rs/tokio | external_research_source_material | external_research_sourced_fact | async runtime implementation and operational model |
| https://github.com/tokio-rs/axum | external_research_source_material | external_research_sourced_fact | Rust web framework implementation and design claims |
| https://docs.rs/axum/latest/axum/ | external_research_source_material | external_research_sourced_fact | published crate documentation for routing and extractors |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which operational discipline a resource-constrained team installs first. The seed scored rows rank corpus hygiene while the ops file's own priority is temporal, boot-time discipline first because it is cheapest and catches the most, telemetry second because it makes everything else diagnosable, and rollout sequencing last only because it applies per schema change rather than per request.

**Recommended default and causal basis.** Adopt typed fail-fast configuration and secret redaction first, structured correlated tracing second, honest health surfaces third, then CI gates, image discipline, and sequencing. Ordering by when a defense pays out matches the file's structure, configuration and secrets guard every process start, tracing guards every request, health checks guard every deploy, and sequencing guards the rare but highest-stakes schema events.

**Operating conditions and assumptions.** The service is early enough to sequence adoption, a live incident reorders everything toward whichever defense the incident lacked. This ranking orders operational doctrines, the anatomy and dispatch rankings live with the playbook and routing themes.

**Failure boundary and alternatives.** Adopting rollout ceremony before boot discipline is the common inversion, teams write elaborate migration plans for services that still crash-loop on malformed environment variables. Bounded alternatives and recoveries: risk-ordered adoption starting from the team's worst recent incident class, emotionally compelling and defensible, it usually converges on the same list reordered.

**Counterexample, gotchas, and operational comparison.** The two migration sections look skippable for teams without current schema work, but the four-step pattern must be habit before the risky change arrives, learning it during the change is how impossible orderings ship. Good: a new service shipping with typed settings and tracing before its first real endpoint. Bad: a migration runbook authored for a service whose logs still print passwords. Borderline: deferring image slimming indefinitely, cheap to defer, the build-cache pain compounds quietly.

**Verification, evidence, and uncertainty.** Compare a team's adoption sequence against the payout-frequency order and ask what justified each inversion. The ops file's eight-section arc and its per-section applicability read in full. No measurement ranks these defenses by realized incident prevention in this repository.

**Second-order consequence.** Frequency-ordered adoption also matches debuggability dependencies, sequencing failures are diagnosed through traces, traces are correlated through identifiers configured at boot, so the adoption order is simultaneously the dependency order.

**Revision decision.** Present the payout-frequency ordering as operative and keep the scored rows as corpus-process emphasis.

**Retained seed evidence.** The three scored seed rows with tier labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `rust_backend_runtime_operations` | 95 | default_adoption_pattern_tier | Source Map First: Load local rust backend material before synthesizing runtime operations recommendations. |
| `rust_backend_runtime_operations` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `rust_backend_runtime_operations` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what operational principle every runtime and rollout choice in this theme must satisfy. The seed generic corpus formulas replace the ops thesis, a Rust backend is operable when its state is explicit at boot, its behavior is explainable per request, and its changes are reversible per rollout step.

**Recommended default and causal basis.** Evaluate any proposed operational change against the three clauses and reject changes that weaken one to strengthen another. Each clause condenses sections of the mapped file, explicit boot state from hierarchical config and fail-fast startup, explainable behavior from structured correlated tracing and honest health surfaces, reversible change from sequencing rules that require a working rollback after every step.

**Operating conditions and assumptions.** The deployment environment can express the clauses, a platform with no staged rollout support caps the reversibility clause at backup-and-restore. The thesis governs operational posture, what the service computes and how it validates domain input are the playbook theme's concern.

**Failure boundary and alternatives.** Collapsing the thesis to just observability misses the reversibility clause, a perfectly traced deployment that cannot roll back after step three of five is still the disaster the file legislates against. Bounded alternatives and recoveries: an SRE-style error-budget framing, compatible but broader, the mapped file stays at the delivery-team scale where budgets are implicit.

**Counterexample, gotchas, and operational comparison.** Reversibility silently expires, the file's sequencing list asks what rollback still works after each step, past the constraint-tightening step the answer changes, and teams that checked once at planning miss the expiry. Good: rejecting a config flag read lazily at first use, it hides boot-state gaps. Bad: shipping a strict constraint in step one because the data looked clean. Borderline: readiness that ignores an optional cache dependency, defensible, document which dependencies readiness actually reflects.

**Verification, evidence, and uncertainty.** For a recent deploy, ask where each clause was demonstrated and find the artifact that proves it. The ops file's startup, tracing, health, and sequencing sections read in full. Whether three clauses cover multi-region operation is beyond the mapped material.

**Second-order consequence.** The clauses share a direction of proof, each demands the service demonstrate a property before depending on it, config validated before serving, readiness proven before traffic, rollback verified before the next step, operations as preconditions rather than reactions.

**Revision decision.** State the three clauses, explicit at boot, explainable per request, reversible per rollout step, each cited to its sections.

**Retained seed evidence.** The three labeled thesis statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `rust_backend_runtime_operations` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Rust Backend Runtime Operations comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide how to navigate the mapped ops file when an operational question arrives. The seed map row lists heading signals without the file's internal split, sections one through four govern the running process, configuration, secrets, tracing, health, while five through eight govern the delivery machine, CI, images, sequencing, evolution.

**Recommended default and causal basis.** Enter at the process half for runtime questions and at sections seven and eight for anything touching schema or deploy ordering. Process sections and machine sections serve different readers on different days, an on-call engineer needs the process half, a release engineer needs the machine half, and the reference map's task-type rows already route migration work straight to sections seven and eight.

**Operating conditions and assumptions.** Questions arrive classifiable as process or machine concerns, incidents that span both, a bad deploy breaking health checks, read the halves in failure order. This map describes the mapped ops file, the rest of the bundle is described by its sibling themes' corresponding sections.

**Failure boundary and alternatives.** Reading the file whole for a narrow question wastes the internal split, a secrets question needs section two and its secrecy example, not the Docker caching strategy four sections later. Bounded alternatives and recoveries: direct heading search with the bundle's ripgrep commands, effective for experts who already know which section owns their question.

**Counterexample, gotchas, and operational comparison.** Section five's CI expectations quietly bridge the halves, migration-aware tests are a machine concern enforced by process-side tooling, skipping the bridge is how schema drift reaches production with green builds. Good: an on-call reading sections three and four during a readiness incident. Bad: studying image caching while production logs leak a session key. Borderline: reading only section eight for a migration, workable, section seven's ordering questions are the half that prevents impossible plans.

**Verification, evidence, and uncertainty.** Check that recent operational consultations opened the half matching the question class. The ops file's eight-section structure and the reference map's migration row read in full. Whether the halves deserve separate corpus themes eventually is a maintainer call.

**Second-order consequence.** The file's two halves fail differently, process-half violations page someone tonight, machine-half violations corrupt a rollout next quarter, which is why the reference map gives the machine half its own dedicated task-type row.

**Revision decision.** Annotate the row with the process-half versus machine-half split and the map's section-level routing for migration tasks.

**Retained seed evidence.** The single local source row with title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/rust-backend-runtime-and-ops.md | Rust Backend Runtime And Ops | Rust Backend Runtime And Ops; 1. Hierarchical Configuration; 2. Secrets Handling; 3. Structured Tracing And Correlation; 4. Startup, Readiness, Liveness; 5. CI Expectations | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide which external targets deserve retrieval effort when this theme's claims need freshness. The seed four inherited URLs anchor runtime and framework code, yet this theme's ecosystem names live elsewhere, the ops file cites secrecy for redaction, tracing and tracing-subscriber for telemetry, and docker for images, none of which has a row.

**Recommended default and causal basis.** Prioritize dated fetches of the tracing ecosystem when refreshing this theme, and use the existing rows only for their framework-freshness value. The template propagated one URL set across the rust backend cluster, so the rows fit the playbook theme's crates and drift from this theme's, leaving the observability stack, this file's most ecosystem-dependent guidance, without a fetch target.

**Operating conditions and assumptions.** URL structures remain stable, and any docs.rs fetch pins the version it observed. External rows serve future freshness verification, they confer no current-fact authority, all four remained unretrieved throughout this evolution.

**Failure boundary and alternatives.** Treating the rows as this theme's verification queue would spend fetches on axum routing docs while the claims most needing freshness checks, tracing idioms and redaction wrappers, have no queued source at all. Bounded alternatives and recoveries: reading a real service's Cargo.lock and dependency changelogs, which answers is our tracing stack current faster than any general documentation.

**Counterexample, gotchas, and operational comparison.** Tokio's row is the least wrong inherited anchor here, runtime behavior does bear on startup and blocking concerns, but it corroborates the playbook's async claims more than this file's ops claims. Good: a dated fetch of tracing-subscriber docs before asserting current subscriber layering advice. Bad: citing the axum row to freshen a secrets-handling claim. Borderline: using api-guidelines for config-struct naming, tangent to operations, occasionally useful.

**Verification, evidence, and uncertainty.** Confirm externally-flavored claims name a dated retrieval or carry the unretrieved-candidate label. Zero fetches this assignment and the ops file's inline crate examples read in full. How far the 202604 observability idioms have drifted is unknowable without those fetches.

**Second-order consequence.** The mismatch is itself evidence about the corpus template, external maps were cloned per-cluster rather than derived per-file, an audit finding that future template revisions could fix mechanically by scraping each mapped file's named examples.

**Revision decision.** Keep the rows as inherited candidates, flag the missing secrecy, tracing, and docker anchors, and route any real freshness need through dated fetches of those crates' docs.

**Retained seed evidence.** All four external rows with their boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://github.com/rust-lang/api-guidelines | Rust API Guidelines | Rust library-team API design recommendations | external_research_sourced_fact |
| https://github.com/tokio-rs/tokio | Tokio repository | async runtime implementation and operational model | external_research_sourced_fact |
| https://github.com/tokio-rs/axum | Axum repository | Rust web framework implementation and design claims | external_research_sourced_fact |
| https://docs.rs/axum/latest/axum/ | Axum docs.rs | published crate documentation for routing and extractors | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which operational behaviors reviewers must reject on sight in this theme. The seed process rows miss the operational rejections the mapped file names, hard-coded runtime choices, secrets in logs or panics, ad-hoc string logging, boot that limps past invalid config, image-baked configuration, and schema changes requiring impossible orderings.

**Recommended default and causal basis.** Wire the greppable half into CI and assign the reviewable half as named questions in deploy and migration review. Each rejection inverts one ops-file rule, hard-coding inverts layered config, leaked secrets invert redaction wrappers, string logs invert structured correlation, limping boots invert fail-fast, baked config inverts environment-driven injection, and impossible orderings invert the sequencing list.

**Operating conditions and assumptions.** Reviews see the rollout plan, not just the diff, three of the six rejections live in the plan rather than the code. Operational code and rollout-plan failures only, anatomy rejections live with the playbook theme and dispatch rejections with the routing theme.

**Failure boundary and alternatives.** These defects pass functional review because they are invisible in happy-path behavior, the service works, until rotation day, incident night, or migration hour exposes the missing discipline at maximum cost. Bounded alternatives and recoveries: platform guardrails, secret scanners and deploy policies, catching the mechanical rows organization-wide at the price of per-service nuance.

**Counterexample, gotchas, and operational comparison.** Secret leakage via panic messages and debug dumps is the subtlest row, the file names both explicitly, a Debug derive on a settings struct defeats a redaction wrapper the moment anything logs it. Good: blocking a PR whose new config knob is read from the environment mid-request. Bad: approving a migration plan with no per-step rollback note. Borderline: a Debug impl on settings that elides secret fields manually, acceptable, fragile against the next added field.

**Verification, evidence, and uncertainty.** Check each registry row inverts a citable ops-file rule and carries a working detection signal. The ops file's per-section prohibitions read in full. Relative incidence of the six rejections in real Rust services is unmeasured here.

**Second-order consequence.** Half the registry is greppable and half is only reviewable, hard-coding, string logs, and env-read sprawl yield to static checks, while limping boots, baked config, and impossible orderings need a human asking what happens when this is wrong.

**Revision decision.** Import the six rejections with detection signals, grep for env reads outside the settings module, scan log output for secret classes, and require a rollback answer per rollout step in review.

**Retained seed evidence.** The three seed process rows with their detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which pipeline checks must pass before an operational change may deploy. The seed document verifier stands alone while the ops file defines the delivery gate floor, formatting, linting, tests, and build at minimum, plus dependency hygiene where already enforced, and migration-aware tests in CI whenever database work is involved.

**Recommended default and causal basis.** Run format, lint, test, and build on every change, trigger migration-aware tests on schema diffs, and hold deploy review until the two operational questions have answers. The file scopes gates by change class, every change pays the four-gate floor, schema-touching changes additionally prove the application's expectations match the migrated schema, because green unit tests over a stale schema certify nothing.

**Operating conditions and assumptions.** CI can provision a real database for migration tests, the testing sibling's isolated-database harness is the standing precondition. Delivery-pipeline gates for this theme, runtime verification like health probes belongs to the observability section and endpoint verification to the testing sibling's matrix.

**Failure boundary and alternatives.** A pipeline that skips migration-aware testing passes builds whose first production contact with the new schema is the deploy itself, converting CI's cheapest catch into rollout's most expensive one. Bounded alternatives and recoveries: deploy-time verification through canary analysis, complementary and later, the file's gates exist to catch failures before any instance sees traffic.

**Counterexample, gotchas, and operational comparison.** Dependency hygiene is worded conditionally, if the repo already enforces it, adopting this theme does not mandate introducing audit tooling, but removing existing enforcement to go faster fails the gate's spirit. Good: a schema PR automatically running migration tests against a provisioned database. Bad: a deploy gated only on compilation succeeding. Borderline: skipping the build gate on docs-only changes, fine when the path filter is provably docs-only.

**Verification, evidence, and uncertainty.** Inspect the pipeline configuration for the four gates and the schema-diff trigger, then test the trigger with a trivial migration. The ops file's CI section and sequencing questions read in full. Whether the four-gate floor still matches ecosystem CI norms post-202604 needs external retrieval.

**Second-order consequence.** The conditional structure is the design, unconditional heavyweight gates get disabled under deadline pressure, gating migration tests on migration presence keeps the pipeline cheap enough that nobody is tempted to bypass it.

**Revision decision.** Adopt the four-gate floor with the conditional migration gate, and add the operational review questions, boot-failure behavior demonstrated and per-step rollback named.

**Retained seed evidence.** The seed's document verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide what an agent must produce beyond code when its task touches this theme's territory. The seed four generic bullets stand where the bundle gives agents an operations-specific activation, Operations Mode fires when the main risk is configuration, secrets, tracing, CI, Docker, deployment, migrations, or rollout safety, and it routes here as the primary read.

**Recommended default and causal basis.** Require agents to answer the five sequencing questions verbatim for schema changes and to name boot-failure behavior for config changes. Agents mis-handle operations work in a characteristic way, they optimize the code diff and ignore the rollout plan, so an ops-aware agent must be instructed to produce sequencing artifacts, ordered steps with rollback answers, not just passing code.

**Operating conditions and assumptions.** The agent has access to the live mapped file, embedded stale copies reproduce the staleness failures the routing theme catalogs. Agent behavior over this theme's material, generic bundle dispatch is the routing theme's guide and anatomy decisions the playbook theme's.

**Failure boundary and alternatives.** An agent that treats a migration as a code change emits a correct schema file and a deployment landmine, the file's impossible-ordering prohibition is checkable only in the plan the agent never wrote. Bounded alternatives and recoveries: restricting agents to the code half and reserving rollout planning for humans, safer where schema stakes are high, it forfeits the agent's consistency at template completion.

**Counterexample, gotchas, and operational comparison.** Agents complete templates convincingly, a five-question plan whose backfill step is plausible fiction reads identically to a real one, so human review must check the answers against the actual data shape, not just their presence. Good: an agent PR pairing a migration with five answered sequencing questions. Bad: an agent adding a required column with a one-line migration and no plan. Borderline: an agent flagging that it cannot verify backfill volume, honest uncertainty, exactly what review needs surfaced.

**Verification, evidence, and uncertainty.** Reject agent operational outputs lacking mode declaration, sequencing answers, or boot-behavior notes as their change class requires. SKILL.md's Operations Mode definition and the ops file's five-question list read in full. How reliably agents self-select Operations Mode on mixed tasks lacks measurement.

**Second-order consequence.** The sequencing list doubles as an agent output contract, five ordered questions, what lands first, what code spans both states, when backfill runs, when constraints tighten, what rollback works after each step, an agent answering all five has produced a reviewable plan by construction.

**Revision decision.** Instruct agents to declare Operations Mode when the risk matches, read this file's relevant half, and emit rollout artifacts alongside code for any schema or deploy change.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide which entry into this theme matches the reader's current operational situation. The seed one generic engineer stands in for this theme's three distinct journeys, a service author wiring config and telemetry before first deploy, an on-call responder reading health and traces during an incident, and a release engineer sequencing a risky schema change.

**Recommended default and causal basis.** Identify which journey the current task belongs to and enter the file at that journey's sections rather than the beginning. The three journeys consume the file at different tempos, the author reads it once thoroughly, the responder queries it in minutes under pressure, and the release engineer works through sections seven and eight as a checklist over days.

**Operating conditions and assumptions.** The reader knows their journey, incidents that are secretly migration fallout start in the responder journey and hand off to the release one. Journeys through operational material, the build-something journeys belong to the playbook theme and the which-file journey to the routing theme.

**Failure boundary and alternatives.** Documentation tuned to only the author journey fails the responder, who needs the readiness-versus-liveness distinction findable in seconds, not embedded in prose written for greenfield setup. Bounded alternatives and recoveries: runbooks extracting each journey's slice into standalone documents, faster in the moment, another shadow copy to keep synchronized.

**Counterexample, gotchas, and operational comparison.** The release journey has a hidden prerequisite, its step-two code must read and write both schema shapes, which drags the author journey back in mid-release, teams that staff the two journeys separately drop exactly this handoff. Good: an on-call resolving a stuck deploy by checking whether readiness reflects the real dependency picture. Bad: a release engineer discovering the dual-shape code requirement during the backfill. Borderline: an author skimming sequencing sections they will not need for months, harmless, the habit-forming argument says read them anyway.

**Verification, evidence, and uncertainty.** Ask recent users of this theme which journey they ran and whether the file's structure served that tempo. The ops file's section tempos and the sequencing prerequisites read in full. The actual frequency mix of the three journeys per team is unmeasured.

**Second-order consequence.** The author journey is the cheapest place to serve the other two, correlation identifiers wired on day one are what make the responder's journey short, and reversible habits learned early are what make the release journey routine.

**Revision decision.** Recast the scenario as three entries, author reads whole, responder jumps to sections three and four, release engineer checklists sections seven and eight.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Rust reliability engineer is starting from a requirement that needs a safe API, explicit error model, and testable boundary and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `rust_backend_runtime_operations` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the idiomatic ownership, async, error, and crate-boundary shape before coding.
Reference opening trigger: Open this file when the task mentions rust backend runtime operations, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how much strictness, telemetry, and ceremony each operational surface deserves. The seed template rows skip this theme's live tensions, boot strictness versus startup resilience, telemetry richness versus overhead and noise, and rollout ceremony versus delivery speed.

**Recommended default and causal basis.** Fail fast at boot, record curated correlated fields, and pay full sequencing ceremony on any change touching schema or rollout order. The mapped file takes sides with stated reasons, fail fast because surprising runtime misconfiguration costs more than a loud boot failure, record high-value fields once because re-derivation costs more than propagation, sequence rollouts because impossible orderings cannot be fixed after the fact.

**Operating conditions and assumptions.** Deviations carry named reasons, a service that must boot degraded, for instance, should enumerate exactly which dependencies readiness will not reflect. Tuning within operational doctrine, the inline-versus-worker and type-ceremony tensions belong to the playbook theme's guide.

**Failure boundary and alternatives.** Each tension has a seductive wrong default, tolerant boots that limp into undefined behavior, log-everything telemetry that drowns the correlating identifier, and ceremony-free deploys that work until the one change that needed step discipline. Bounded alternatives and recoveries: environment-differentiated stances, strict in production and tolerant in development, the file's layered configuration is precisely the mechanism that makes such differentiation explicit rather than accidental.

**Counterexample, gotchas, and operational comparison.** The ceremony axis tempts proportional thinking, small migration small ceremony, but the file's trigger is kind not size, any schema change altering runtime assumptions gets the full five questions, tiny additive columns included when constraints follow later. Good: a boot that fails on unknown config keys, catching typos at deploy rather than at 3 a.m. Bad: tracing every function entry until the request identifier drowns. Borderline: a degraded-boot mode for a cache-optional service, defensible with the readiness caveat documented.

**Verification, evidence, and uncertainty.** Audit recent deviations from the three stances for their named reasons and revisit any reason that no longer holds. The ops file's explicit rationales in its startup, tracing, and sequencing sections read in full. The telemetry overhead level at which curation stops mattering is workload-specific.

**Second-order consequence.** All three stances privilege failure-time cost over success-time cost, strict boots, curated fields, and stepped rollouts each tax every normal day slightly to make the abnormal day survivable, one discount rate applied three ways.

**Revision decision.** Add the three axes with the file's stances and the narrow conditions justifying deviation.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the rust backend runtime operations pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong rust backend runtime operations guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which document settles an operational question when several plausibly apply. The seed lone canonical row with its confidence warning understates a clean jurisdiction, this file is the bundle's final word on config, secrets, telemetry, health, CI, images, and rollout, while it defers anatomy to the playbook, verification depth to the testing sibling, and auth or retry semantics to the security file.

**Recommended default and causal basis.** Resolve topic ownership by the jurisdiction map first, and read both owners whenever a question names two surfaces at once. The bundle partitions by risk surface with almost no overlap, so hierarchy disputes here are rare and jurisdictional rather than doctrinal, the question is which file owns the topic, not which contradicts which.

**Operating conditions and assumptions.** The bundle stays internally consistent, an upstream revision that moves a topic between files redraws this map silently. Precedence within the bundle for operational questions, corpus-wide precedence is the adjacent-routing section's business.

**Failure boundary and alternatives.** The one genuine seam invites misjudgment, background-worker readiness, section four raises whether readiness requires healthy workers while worker design lives in the security sibling, answering from either file alone gives half the picture. Bounded alternatives and recoveries: treating the corpus's other rust ops-adjacent themes as second opinions, useful for gaps, subordinate on this file's owned topics.

**Counterexample, gotchas, and operational comparison.** SKILL.md restates several ops rules in compressed guardrail form, secrets redacted and configuration layered, when compression and detail diverge the detailed file wins, the wrapper is an index, not a second authority. Good: settling a readiness dispute from section four and the worker rules together. Bad: quoting SKILL.md's one-line secrets guardrail over the ops file's four-bullet detail. Borderline: taking testing-sibling harness advice for CI database provisioning, legitimate, that seam is genuinely shared.

**Verification, evidence, and uncertainty.** Test hierarchy claims against each file's self-declared use statement and the bundle's context strategy. All five bundle files' charters and the worker-readiness seam read in full. No observed upstream revision yet tests how stable the jurisdiction map is.

**Second-order consequence.** The seed's thin-evidence warning inverts here, one mapped source is not weakness when that source has clean jurisdiction, the risk is not missing corroboration but missing the seams where jurisdiction genuinely shares.

**Revision decision.** Record the jurisdiction map, this file canonical for its eight topics, siblings canonical for theirs, and the worker-readiness seam flagged as a two-file question.

**Retained seed evidence.** The single hierarchy row and the confidence warning remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/rust-backend-runtime-and-ops.md | canonical primary source | Rust Backend Runtime And Ops; 1. Hierarchical Configuration; 2. Secrets Handling | What guidance, warning, or example should this source contribute to Rust Backend Runtime Operations? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what standing record makes a service's operational wiring reviewable without reading its source. The seed named artifact lacks operational form, this theme's natural object is a per-service operations card, one page recording config layers and their sources, secret classes and rotation owners, trace identifier and propagation path, readiness semantics, and the standing rollout pattern.

**Recommended default and causal basis.** Create the card at service birth alongside the typed settings module and review it in every deploy-affecting PR. Every ops-file rule presumes service-specific facts nobody memorizes accurately, which env layer wins, which key rotates quarterly, what readiness actually checks, the card is where those facts live when the person who wired them is on holiday.

**Operating conditions and assumptions.** Services are few enough for per-service cards, fleets need the card generated from configuration rather than written by hand. One card per service capturing operational wiring, request-lifecycle structure belongs to the playbook theme's diagram and routing vocabulary to the routing theme's card.

**Failure boundary and alternatives.** Without the card each incident and rollout re-derives the facts from code under time pressure, and re-derivation under pressure is where the wrong config layer gets edited and the wrong key gets rotated. Bounded alternatives and recoveries: encoding the card's facts as structured comments in the settings module, closer to the code, invisible to the on-call reading dashboards at 3 a.m..

**Counterexample, gotchas, and operational comparison.** The card must never contain secret values, only classes, locations, and owners, a card that quotes even one token converts documentation into the leak surface section two guards against. Good: an incident shortened because the card named which layer sets the pool size in staging. Bad: rotation day spent grepping for every place the old key might live. Borderline: one shared card for five sibling services, workable when their wiring is genuinely identical, the first divergence poisons it.

**Verification, evidence, and uncertainty.** Quarterly, pick one card block and verify it against the running service's actual behavior. The ops file's per-section presumption of service-specific facts read in full. Card upkeep discipline across team churn is the untested variable.

**Second-order consequence.** The card's secrets block enforces a rule the file states but code cannot express, separate secret classes have separate rotation concerns, listing each class beside its rotation owner turns an abstract separation into named accountability.

**Revision decision.** Define the artifact as the operations card with five blocks, config, secrets, telemetry, health, rollout, updated in the same change as any wiring it describes.

**Retained seed evidence.** The artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: operations runbook for deploy, rollback, SLO breach, logging, and incident review.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Rust Backend Runtime Operations | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which exercise most efficiently builds safe schema-change habits. The seed abstract usage lines replace the teaching walkthrough this theme wants, one risky mandatory-field migration executed through the full four-step evolution, expand compatibly, deploy dual-shape code, backfill, then tighten constraints, with the rollback answer rechecked at each step.

**Recommended default and causal basis.** Run new backend engineers through the walkthrough on a staging copy before they own any schema change. The four-step pattern is the file's most algorithmic content and its most catastrophic to improvise, a walkthrough that runs all four steps on a realistic table teaches the ordering logic that a rule statement cannot.

**Operating conditions and assumptions.** A staging environment with production-shaped data exists, the walkthrough on an empty database teaches the steps but not the backfill judgment. Teaching operational sequencing, endpoint-construction walkthroughs belong to the playbook theme and dispatch drills to the routing theme.

**Failure boundary and alternatives.** Engineers who have only read the pattern reliably compress it under pressure, merging expand and tighten into one migration because the data looks clean, the exact impossible ordering the walkthrough exists to make visceral. Bounded alternatives and recoveries: reviewing a past incident retrospective of a mis-sequenced migration, cheaper and vivid, secondhand caution fades faster than firsthand rollback experience.

**Counterexample, gotchas, and operational comparison.** Step two is the walkthrough's hidden difficulty, code that reads and writes both shapes is application work, not migration work, and learners consistently underestimate it because the schema diff looks finished before any of it is written. Good: a trainee's walkthrough diary noting the rollback answer changing after each step. Bad: certifying schema competence from a single additive-column migration. Borderline: practicing on a table without foreign keys, gentler, the constraint interactions are half the lesson.

**Verification, evidence, and uncertainty.** Have the trainee execute a fresh four-step change unsupervised and audit their per-step rollback answers. The ops file's four-step default and five sequencing questions read in full. How long the habit persists without periodic real migrations is unmeasured.

**Second-order consequence.** The rollback drill teaches the pattern's deepest lesson, reversibility is a property that expires step by step, learners who roll back after backfill discover which data movements survive reversal and which need forward-fix instead, knowledge no green migration ever surfaces.

**Revision decision.** Anchor the section on the four-step migration walkthrough plus one failure drill, a rollback exercised deliberately after step three.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Rust Backend Runtime Operations after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Rust Backend Runtime Operations as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Rust Backend Runtime Operations only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which measurements prove this theme's operational ceremony pays for itself. The seed compile-centric indicator ignores operational feedback, nothing counts boot failures caught at deploy versus runtime misconfiguration discovered by incident, incidents diagnosed within the trace versus escalated to log archaeology, or rollouts completing all steps versus aborting mid-sequence.

**Recommended default and causal basis.** Label the three event streams as they occur and review the ratios quarterly beside the incident count. Each ratio measures one thesis clause in production, boot-catch ratio proves explicit-at-boot is working, trace-resolution ratio proves explainable-per-request, and rollout-completion ratio proves reversible-per-step, closing the loop between doctrine and outcomes.

**Operating conditions and assumptions.** Retrospectives honestly record whether traces sufficed, a culture that backfills tidy diagnostic narratives poisons the middle ratio. Measuring this theme's operational disciplines, code-boundary adoption metrics belong to the playbook theme's loop and dispatch metrics to the routing theme's.

**Failure boundary and alternatives.** Without the ratios the doctrine's value stays anecdotal, and anecdote loses to deadline pressure the first quarter someone proposes skipping ceremony to ship faster. Bounded alternatives and recoveries: adopting platform-level DORA-style metrics instead, broader and comparable across teams, they cannot attribute outcomes to specific ops-file rules the way the three ratios can.

**Counterexample, gotchas, and operational comparison.** A rising boot-catch ratio can mean improving discipline or deteriorating config hygiene generating more catches, pair it with the absolute misconfiguration-incident count before celebrating. Good: a quarter showing most config defects dying at deploy while runtime misconfiguration incidents hit zero. Bad: defending fail-fast boots with no data when a team proposes tolerant startup. Borderline: counting aborted rollouts as failures, an abort executed via a working rollback is the discipline succeeding.

**Verification, evidence, and uncertainty.** Confirm the three ratios exist, cite real event streams, and were consumed at the last quarterly review. The alignment between the file's three doctrinal clauses and their measurable production signatures. Healthy baseline values for the ratios await the first measured quarters.

**Second-order consequence.** The ratios are cheap because their raw events are already recorded somewhere, deploys log their failures, retrospectives name their diagnostic path, and releases track their steps, the loop is mostly labeling existing records rather than new instrumentation.

**Revision decision.** Add the three ratios with their collection points, deploy logs for boot catches, incident retrospectives for trace resolution, and release records for rollout completion.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: compile attempts and review comments decrease because the API shape is explicit before implementation.
Failure signal: the reference hides ownership or error tradeoffs behind generic guidance.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what must be confirmed before this operations reference is declared faithful. The seed shape items never audit fidelity to the mapped file's countable content, eight sections, three config layers, four secret classes named, two health distinctions, five CI minimums, five sequencing questions, and four evolution steps.

**Recommended default and causal basis.** Run the count-and-quote audit at every reread cycle and after any archive change touching the bundle. This theme's claims transcribe an enumerable source, so completeness reduces to counting the enumerables here against the file and diffing the quoted sequencing and evolution lists, which are the payload most damaged by paraphrase drift.

**Operating conditions and assumptions.** The 202604 file remains at its path for line-level comparison. Auditing this reference document against its source, auditing live operational practice belongs to the metrics loop and pipeline gates.

**Failure boundary and alternatives.** Count-passing paraphrase is the residual risk, a reworded sequencing question that drops the after-each-step qualifier keeps the count at five while gutting the rule that rollback expires progressively. Bounded alternatives and recoveries: checksumming the mapped file and re-auditing on change only, efficient, blind to drift introduced by this document's own future edits.

**Counterexample, gotchas, and operational comparison.** Auditing this document against memory of the ops file rather than the file itself is the failure mode all these corpus audits share, the check costs minutes only when the source is actually opened. Good: an audit catching that a quoted evolution list swapped backfill and tighten. Bad: declaring fidelity because all 26 headings and both tables exist. Borderline: accepting paraphrased CI gate names, tolerable, the gate count and the migration conditional must survive exactly.

**Verification, evidence, and uncertainty.** Count the enumerables and diff both ordered lists verbatim against the live mapped file. The fully enumerable structure of the 89-line ops file read in full. Whether order-sensitive quoting needs its own tooling across the corpus is open.

**Second-order consequence.** The two ordered lists deserve verbatim treatment precisely because their power is positional, reordering the evolution steps is not a paraphrase but a different and dangerous algorithm, so the audit must compare order, not just membership.

**Revision decision.** Add the count items and an exact-quote check on the two ordered lists, sequencing questions and evolution steps, each audit cycle.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Rust Backend Runtime Operations.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send an operations-flavored question this theme does not own. The seed token-split rows point nowhere while this theme's real neighbors are exact, the playbook theme for anatomy and persistence seams, the routing theme for bundle dispatch, the security sibling's theme for auth and idempotency, and the corpus's CI and quality-gate themes for pipeline depth beyond the four-gate floor.

**Recommended default and causal basis.** Test each arriving question against the eight owned topics and forward anything failing the test with its destination named. Operations touches everything, so this theme accumulates questions that merely sound operational, a retry policy question mentions deployment but belongs to resilience doctrine, and a test-flakiness question mentions CI but belongs to verification practice.

**Operating conditions and assumptions.** Destination themes exist under their expected corpus names, the routing theme's pointer probes keep this checkable. Sending away what this theme cannot own, summaries of the destinations' content are deliberately absent.

**Failure boundary and alternatives.** Keeping every ops-flavored question here dilutes the file's clean jurisdiction, the eight owned topics, into a general operations helpdesk that answers everything shallowly. Bounded alternatives and recoveries: for platform specifics no local theme covers, kubernetes semantics or cloud IAM, external documentation explicitly labeled unretrieved.

**Counterexample, gotchas, and operational comparison.** Migration questions never leave this theme, they are the jurisdiction's crown, but data-modeling questions wearing migration vocabulary, should this be one table or two, belong to persistence doctrine at the playbook theme. Good: forwarding an idempotency-key question to the security sibling's territory despite its deployment framing. Bad: answering a table-design question here because a migration would implement it. Borderline: a Docker orchestration question, image shape stays here, cluster scheduling exits to external sources.

**Verification, evidence, and uncertainty.** Sample recent forwarded and kept questions against the eight-topic ownership test. The jurisdiction partition read across all five bundle files. Misroute frequency into this theme lacks measurement.

**Second-order consequence.** The worker-readiness seam identified in the hierarchy section is this section's standing exception, questions on that seam are legitimately dual-routed, answered here for the readiness half and at the security theme for the worker half, a designed double-route rather than a misroute.

**Revision decision.** Route by the jurisdiction map, keep config, secrets, telemetry, health, CI floor, images, and rollout here, and forward anatomy, dispatch, resilience semantics, and deep verification to their owners.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use backend, executable, or quality-gate Rust references when the question shifts to HTTP delivery, specs, or review gates.
Adjacent reference 1: consider the rust adjacent reference when the current task pivots away from rust backend runtime operations.
Adjacent reference 2: consider the backend adjacent reference when the current task pivots away from rust backend runtime operations.
Adjacent reference 3: consider the runtime adjacent reference when the current task pivots away from rust backend runtime operations.

## Workload Model

**Decision supported.** This section helps decide how to budget operational effort so its spikes are planned rather than absorbed. The seed endpoint-count budgets fit request work, not operational work, whose real units are per-service setup performed once, per-deploy checks performed constantly, and per-migration sequencing performed rarely at high stakes.

**Recommended default and causal basis.** Invest setup fully at service birth, keep per-deploy checks automated below human attention cost, and schedule migrations as the multi-delivery projects they are. The three units scale on different axes, setup scales with service count, deploy checks scale with release frequency, and sequencing scales with schema churn, so a single capacity number cannot budget them together.

**Operating conditions and assumptions.** Service birth rate is low enough for full setup, teams spinning many services need the setup templated or the investment collapses. Budgeting operational effort for services adopting this theme, implementation-slice budgeting belongs to the playbook theme's model.

**Failure boundary and alternatives.** Budgeting operations as a flat tax breaks at migration time, a five-step sequenced change is a multi-day workload spike that flat models schedule as an afternoon, producing exactly the compressed impossible orderings the file forbids. Bounded alternatives and recoveries: platform teams absorbing the setup unit fleet-wide, effective at scale, it moves the knowledge away from the service team that will answer the 3 a.m. page.

**Counterexample, gotchas, and operational comparison.** The rare-but-spiky migration unit is the one teams forget to staff, a quarter with three sequenced changes is a different quarter, and calendar planning that ignores schema churn discovers this during the overlap. Good: a roadmap slotting a mandatory-field migration as five ordered deliveries across two sprints. Bad: estimating that migration as one ticket because the SQL is short. Borderline: batching two unrelated migrations into one sequence, tempting, their rollback answers now entangle.

**Verification, evidence, and uncertainty.** Compare recent migration calendar estimates against their actual multi-delivery spans. The ops file's per-section applicability tempos and the five-step expansion read in full. Typical setup cost for a well-templated Rust service is unestimated here.

**Second-order consequence.** The units trade against each other deliberately, richer setup, typed config, wired tracing, honest readiness, is precisely what drives the marginal deploy cost toward zero, the file's front-loading is a workload-shaping strategy, not just a safety one.

**Revision decision.** Restate the model in three units, setup cost per new service, marginal check cost per deploy, and spike cost per sequenced migration with its five-delivery expansion made explicit.

**Retained seed evidence.** The workload dimension rows with boundary values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Rust Backend Runtime Operations as a backend service operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | service implementation, route review, worker execution, and operational hardening work where a single wrong recommendation can affect live request handling | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one service boundary, up to 25 endpoints or workers, 1000 representative requests, and one deploy rollback path per review batch | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Rust Backend Runtime And Ops; 1. Hierarchical Configuration; 2. Secrets Handling; 3. Structured Tracing And Correlation; 4. Startup, Readiness, Livene | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is operations runbook for deploy, rollback, SLO breach, logging, and incident review | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which operational invariants a service must demonstrably hold for this theme's guidance to count as adopted. The seed document-property thresholds stand where operational targets should, zero secrets in logs or panics ever, zero deploys of unvalidated configuration, every request traceable by one identifier end to end, and every rollout step leaving a demonstrated rollback.

**Recommended default and causal basis.** Gate deploys on the two pre-deploy targets and sample production weekly for the two runtime ones. Each target is an ops-file rule stated as an invariant, redaction rules imply the zero-leak target, fail-fast boot implies the validated-config target, correlation rules imply the traceability target, and the sequencing questions imply the per-step rollback target.

**Operating conditions and assumptions.** Log scanning can recognize the service's secret classes, which the operations card's secrets block enumerates, the artifacts interlock. Operational invariants for services under this theme, service-level latency targets belong to the performance section and correctness targets to the playbook theme.

**Failure boundary and alternatives.** Targets averaged over time hide the absolutes that matter, a 99 percent secret-redaction rate is not near-success, one leaked key is a full rotation incident, so the first two targets are binary per event, not percentages. Bounded alternatives and recoveries: chaos-style verification, deliberately injecting bad config and watching the boot die, heavier than record audits and the only direct test of fail-fast behavior under realistic conditions.

**Counterexample, gotchas, and operational comparison.** The rollback target is demonstrated, not asserted, a rollback that exists in the plan but has never been executed against staging is a hypothesis, and migration hour is the wrong time to test hypotheses. Good: a release blocked because step two's rollback was never exercised in staging. Bad: declaring traceability from the tracing dependency being present in Cargo.toml. Borderline: waiving the trace target for a batch job with no requests, reasonable, its operations still deserve correlation by job identifier.

**Verification, evidence, and uncertainty.** Review the four target audits together at each release checkpoint with their evidence artifacts attached. The ops file's redaction, boot, correlation, and sequencing rules read in full. Sampling frequency sufficient to catch propagation regressions is workload-dependent.

**Second-order consequence.** Two targets are verifiable before production and two only in it, config validation and rollback demonstration are pre-deploy checkable, while leak absence and trace propagation need production sampling, so the target set spans both sides of the deploy boundary by construction.

**Revision decision.** Publish the four targets with their evidence methods, log scanning for leaks, deploy-gate records for config validation, trace sampling for identifier propagation, and release records for rollback demonstrations.

**Retained seed evidence.** All four seed reliability rows with thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which decay modes need standing probes and what each probe must inspect. The seed generic drift and surge rows miss how this theme's discipline decays, config sprawl where new knobs bypass the typed settings module, telemetry rot where new code paths skip the correlation field, readiness lies where health surfaces stop reflecting real dependencies, and ceremony erosion where each successful migration justifies less sequencing on the next.

**Recommended default and causal basis.** Run the addition-focused probes in CI where greppable and in deploy review where not, attributing each finding to its mode. All four decay through addition, not modification, existing wiring stays correct while new features route around it, so the decay is invisible in any diff review that looks only at what changed rather than what the change bypassed.

**Operating conditions and assumptions.** Probes are owned, an unowned probe list is itself the erosion mode applied to the failure table. Decay of operational discipline, code-boundary erosion belongs to the playbook theme's table and routing decay to the routing theme's.

**Failure boundary and alternatives.** Each mode presents as its own absence, sprawled config still boots, uncorrelated paths still log, lying readiness still passes probes, and unceremonised migrations still usually work, the discipline's value only reappears at the incident it would have prevented. Bounded alternatives and recoveries: periodic game-day exercises that fail dependencies deliberately and watch whether readiness notices, expensive, they test the accumulated truth no per-change probe can.

**Counterexample, gotchas, and operational comparison.** Readiness lies grow from optimization, a dependency check removed because it slowed probes, the removal is individually reasonable and the accumulated result is a green endpoint over a failing service, exactly the distinction section four exists to preserve. Good: CI failing a PR that reads an environment variable outside the settings module. Bad: trusting readiness because the probe endpoint returns ok. Borderline: a documented fast-boot mode skipping one dependency check, acceptable with the readiness caveat recorded on the operations card.

**Verification, evidence, and uncertainty.** Confirm each failure row names its probe, owner, and cadence, and sample one probe's recent findings. The addition-shaped bypass structure read against each ops-file rule. Decay onset speed relative to team churn is unmeasured.

**Second-order consequence.** Ceremony erosion has a signature arithmetic, every skipped step that survives raises confidence while leaving the base rate of catastrophe unchanged, teams read their luck as skill until the sample size catches up, which is why the probe checks presence of ceremony, never recent outcomes.

**Revision decision.** Add the four rows with addition-focused probes, grep counts of env reads outside settings, trace-field coverage per new endpoint, readiness-versus-dependency diffs, and sequencing-question presence per schema change.

**Retained seed evidence.** All four seed failure rows with mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| request surge overloads path | traffic spikes exceed handler, pool, or coroutine limits | apply rate limits, queue bounds, cancellation, and rollback playbook before rollout |
| security boundary silently fails | auth, permission, or input validation assumptions are untested | run abuse-case tests and require explicit deny-by-default behavior |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide which operational failures may retry automatically and which must stop for assessment. The seed corpus-process bullets stand where deploy-time retry doctrine should, failed deploys and failed migrations are retried events too, and their retry rules differ, a failed boot may redeploy freely, a failed migration step must never simply rerun.

**Recommended default and causal basis.** Automate retries for boot-class failures with a crash-loop ceiling, and page a human with the step's planned rollback answer for migration-class failures. Boot failures are idempotent by the fail-fast design, nothing happened, so retry is safe, while migration steps mutate durable state, so a mid-step failure leaves partial work whose rerun semantics depend on exactly which step and what it touched.

**Operating conditions and assumptions.** The deploy system distinguishes the two classes, a pipeline that retries all failures uniformly must have migration steps marked non-retryable explicitly. Retry semantics for operational events, request-level retry and idempotency doctrine belongs to the security sibling's territory and is routed there.

**Failure boundary and alternatives.** Treating migration retry like deploy retry reruns a partially applied backfill or reapplies a constraint against half-moved data, converting a recoverable pause into the ambiguous state the sequencing questions exist to prevent. Bounded alternatives and recoveries: fully automated migration rollback on failure, attractive and dangerous, automated reversal of a partial backfill can destroy the evidence needed to fix forward, human assessment earns its latency here.

**Counterexample, gotchas, and operational comparison.** Backpressure applies to deploy queues too, stacking a second release behind a paused migration multiplies the ambiguous state, the file's dual-shape step exists so the paused state serves traffic indefinitely, use that grace to unstack rather than push. Good: a crash-looping config typo caught by the loop ceiling and fixed in minutes. Bad: a backfill job rerun blindly after a timeout, double-writing half the table. Borderline: auto-retrying a failed image build, safe, it mutates nothing durable, though a ceiling still bounds the waste.

**Verification, evidence, and uncertainty.** Inject a failure into each class on staging and confirm the pipeline retries one and pages with rollback context on the other. The fail-fast idempotence of boot and the durable mutation of migration steps read from the ops file's sections. The right crash-loop ceiling before paging is deployment-cadence-specific.

**Second-order consequence.** The sequencing list pre-answers the assessment, because each step was planned with a what-rollback-still-works answer, a mid-step failure consults a decision already made calmly at planning time rather than improvising one at incident tempo, the ceremony's payoff is precisely this pre-computation.

**Revision decision.** Add the two-regime rule, free retry for pre-traffic failures like boot and health, and stop-and-assess for any failure inside a sequenced migration, with the current step's rollback answer as the assessment's first input.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence emission a service must demonstrate before this theme considers it observable. The seed generic counters replace the specific record set the mapped file mandates, structured traces over string logs, one propagated request or operation identifier, high-value fields recorded once, health surfaces reflecting real dependencies, and log shapes serving both local debugging and operator triage.

**Recommended default and causal basis.** Wire the emission floor at service setup and hold new endpoints to it in review rather than retrofitting after incidents. Each mandate targets a distinct consumer, correlation serves the incident responder walking one request, single-recording serves cost and consistency, dependency-honest health serves the deploy system's traffic decisions, and dual-audience log shape serves the developer and the operator from the same stream.

**Operating conditions and assumptions.** The tracing stack supports field propagation, the file's named ecosystem examples cover this, subject to the freshness caveats the external map records. What operational evidence services must emit, dispatch records belong to the routing theme and boundary-adoption evidence to the playbook theme.

**Failure boundary and alternatives.** Observability built for only one consumer fails the others quietly, developer-oriented debug logs that operators cannot triage, or operator dashboards whose aggregates hide the single request a responder needs to walk. Bounded alternatives and recoveries: log aggregation with retroactive parsing where structured tracing cannot be adopted, recovering partial correlation at much higher query cost, the file's ordering of preference is explicit.

**Counterexample, gotchas, and operational comparison.** Worker and background operations need the same floor under an operation identifier instead of a request one, section four's worker-readiness question implies this extension even though the tracing section speaks in request vocabulary. Good: an incident walked end to end on one identifier across handler, database, and worker spans. Bad: grepping three log formats to reconstruct one request's path. Borderline: sampling traces on high-volume reads, acceptable for cost, mutations stay unsampled.

**Verification, evidence, and uncertainty.** Pick a recent production request and walk it by identifier alone, any gap marks a checklist violation. The ops file's tracing and health mandates read in full. The cost crossover where trace volume needs sampling is workload-specific.

**Second-order consequence.** The once-recorded rule is the checklist's quiet load-bearer, fields re-derived at each layer drift into contradiction, and a trace whose user identifier disagrees with itself across spans is worse than one missing it, consistency of evidence outranking quantity.

**Revision decision.** Define the emission floor from the file's mandates, structured correlated traces, once-recorded high-value fields, dependency-honest readiness, and dual-audience log shape, checked per new endpoint in review.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture error count, timeout count, retry count, saturation signal, and rollback trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove the operational machinery itself stays fast enough not to tax delivery. The seed request-latency ceilings measure the wrong layer for this theme, whose performance surfaces are boot time to readiness, deploy pipeline duration, image build time under Rust's compilation economics, and telemetry overhead per request.

**Recommended default and causal basis.** Record the four measurements per release and investigate any surface whose trend breaks its historical band. The file touches each surface with a stated concern, fail-fast boots should die quickly and readiness should reflect truth promptly, CI gates bound pipeline time, the Docker section names build caching for Rust dependency compilation explicitly, and curated fields bound trace cost.

**Operating conditions and assumptions.** Releases are frequent enough for trends to exist, low-cadence teams substitute explicit re-measurement at each release. Verifying operational performance, request-path latency methods belong to the playbook theme and its SLO precondition.

**Failure boundary and alternatives.** Ignoring the operational surfaces lets them decay into delivery friction, a forty-minute uncached image build taxes every deploy, and slow readiness delays every rollout's traffic shift, costs that never appear in request percentiles. Bounded alternatives and recoveries: accepting fixed budgets per surface instead of trends, simpler to enforce, they age poorly as services legitimately grow.

**Counterexample, gotchas, and operational comparison.** Rust's compile times make the image surface the likeliest offender, the file's caching-strategy mandate is a performance rule wearing packaging clothes, and cache invalidation by careless layer ordering silently multiplies every build. Good: a trend alarm catching image builds doubling after a dependency graph change. Bad: request p99 dashboards standing in for deploy-pipeline health. Borderline: tolerating slow boots on a rarely deployed service, defensible, the readiness-truth half still deserves verification.

**Verification, evidence, and uncertainty.** Inspect the four trend series and confirm each release appended its measurements. The ops file's caching mandate, fail-fast framing, and curated-field rule read in full. Reasonable trend bands for Rust image builds vary widely with dependency choices.

**Second-order consequence.** Trend alarms fit operational surfaces better than ceilings because the surfaces degrade by accretion, one added dependency, one more gate, one extra recorded field, each individually reasonable, the alarm catches the slope that no single change trips.

**Revision decision.** Measure the four surfaces, boot-to-ready duration, pipeline wall time, image build time with and without warm cache, and traced-versus-untraced request overhead, each with a trend alarm rather than a fixed ceiling.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require a service-specific SLO before deployment; absent that, keep local verification to p95 under 200 ms and p99 under 500 ms for representative handlers or document why latency does not apply.
Leading indicator to measure: compile attempts and review comments decrease because the API shape is explicit before implementation.
Failure signal to watch: the reference hides ownership or error tradeoffs behind generic guidance.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what instance count, service count, or team structure this theme's guidance must be re-derived rather than stretched. The seed document-scale bounds stand where operational scale seams should, the file's guidance assumes one service, few instances, and one team, and each assumption has a named breaking point, instance growth mandating the four-step pattern, service growth demanding templated setup, and organizational growth splitting deploy authority from schema authority.

**Recommended default and causal basis.** Operate the doctrine as written within the assumptions, and treat each named trigger as a design event for the operational layer, not a parameter tweak. The file itself flags the first seam, the four-step evolution is the default whenever multiple instances or staggered rollouts are possible, the other two follow from its economics, per-service hand setup and single-owner sequencing stop scaling with count and headcount respectively.

**Operating conditions and assumptions.** Growth events are noticed, autoscaling that quietly adds the second instance crosses the sharpest seam without any human decision. Bounding this theme's operational doctrine, request-scale and architecture seams belong to the playbook theme's statement.

**Failure boundary and alternatives.** Crossing seams unnoticed produces era-mismatched operations, single-instance migration habits under rolling deploys ship the impossible orderings, and hand-wired config across thirty services guarantees the sprawl the settings module prevents in one. Bounded alternatives and recoveries: adopting the multi-instance posture from day one regardless of count, the file endorses this direction by making the four-step pattern the safe default, paying ceremony early to never track the seam.

**Counterexample, gotchas, and operational comparison.** The autoscaling case deserves emphasis, a service configured to scale horizontally has already crossed the multi-instance seam on the day of configuration, not the day of first scale-out, sequencing discipline starts then. Good: enabling autoscaling and mandatory sequencing in the same change. Bad: a fleet of twenty hand-configured services with drifting env conventions. Borderline: two teams sharing deploy authority informally, workable at two, the written handoff pays for itself at three.

**Verification, evidence, and uncertainty.** At each growth event, re-test the three assumptions and record which seams the event crossed. The ops file's own multi-instance conditional and its per-service economics read in full. The service count at which templating becomes mandatory varies with team tooling.

**Second-order consequence.** The seams order themselves by irreversibility, instance growth changes what is safe immediately and retroactively, while templating and authority splits are gradual debts, so the second-instance seam is the one deserving an explicit tripwire in deploy configuration.

**Revision decision.** Name the three seams with their triggers, second instance activates mandatory sequencing, service count activates setup templating, and split authority activates a written handoff between deploy and schema owners.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Rust Backend Runtime Operations stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which probes reveal that this theme's operational examples or principles have gone stale. The seed theme-name queries would surface generic DevOps content while this theme's staleness lives in named places, the observability crates the file cites, secrecy, tracing, tracing-subscriber, container build practice for Rust's compilation model, and the upstream bundle's own revision state.

**Recommended default and causal basis.** Run crate-release probes on the faster cadence, dating each finding against the 202604 anchor, and check the archive at every corpus refresh. Operational idioms churn faster than boundary doctrine, subscriber APIs reshape, image-building tools and cache strategies evolve, and CI norms shift, so this theme's examples date faster than its principles and the probes should target the examples.

**Operating conditions and assumptions.** Probe findings are triaged into example-breaking versus principle-breaking before any rewrite, most churn will be the former. Refreshing this document's ecosystem and lineage claims, principle-level refresh rides on upstream bundle revisions watched by the routing theme's probes.

**Failure boundary and alternatives.** Name-based searching returns tutorials that neither confirm nor deny whether the file's 202604 crate idioms still match current releases, the only question a refresh actually needs answered. Bounded alternatives and recoveries: pinning this document explicitly to the 202604 idiom set and marking all ecosystem examples as archive-dated, zero probe cost, honest, increasingly less useful.

**Counterexample, gotchas, and operational comparison.** Docker probe results skew toward general-purpose advice, Rust's dependency compilation makes its caching strategy unusual, and generic layer wisdom applied naively can worsen the exact build times the file's mandate protects. Good: a probe noting a tracing-subscriber API change and dating the affected example. Bad: logging that rust backend runtime operations tutorials say nothing new. Borderline: probing new observability standards adoption, adjacent and unbounded, cap it to the crates the file names.

**Verification, evidence, and uncertainty.** Record each probe with its date and the specific example or principle it confirmed or flagged. The ops file's named crate examples and the 202604 bundle date read from the mapped files. Actual churn rates of the named crates since 202604 are unknowable without the fetches.

**Second-order consequence.** The probes split by what can invalidate what, crate releases can invalidate examples but not the once-recorded principle, while a bundle revision can invalidate principles too, so the archive watch is lower frequency but higher consequence, an ordering the probe budget should respect.

**Revision decision.** Replace the name queries with targeted probes, release notes for the three named observability crates since 202604, current Rust container build guidance, and the archive watch for a revised bundle.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | rust backend runtime operations official documentation best practices |
| `github_repository_query_phrase` | rust backend runtime operations GitHub repository examples |
| `release_notes_query_phrase` | rust backend runtime operations changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide under what label and with what attached conditions each claim here may be reused. The seed label definitions stand without this assignment's ledger, one mapped ops file read fully, five bundle companions read fully and cited by name, zero external URLs fetched, and every operational practice construct above marked as inference.

**Recommended default and causal basis.** Before reusing a claim, identify its stratum, cite section for facts, carry the condition for conditional doctrine, and attach reasoning for inference. The fact stratum is the file's transcribable content, eight sections, three config layers, the redaction rules, the correlation mandates, the health distinction, the five CI gates, the five sequencing questions, and the four evolution steps, while the cards, ratios, probes, regimes, and seams are this evolution's constructed machinery.

**Operating conditions and assumptions.** The archive path stays stable so fact-class claims remain mechanically checkable. Reuse rules for this document's claims, transcribed doctrine travels with file-and-section citations, constructed machinery travels only with its reasoning.

**Failure boundary and alternatives.** The costliest mislabel would present the crate names or the four-step pattern's universality as verified current facts, the crates are archive-dated illustrations and the pattern's default status is conditional on the multi-instance premise the file itself states. Bounded alternatives and recoveries: per-paragraph inline labels if the stratum-level split ever proves too coarse for a dispute.

**Counterexample, gotchas, and operational comparison.** The five sequencing questions travel especially well and dangerously, they read as universal wisdom, but their after-each-step rollback framing presumes the stepped rollout model, quoted into a big-bang deployment context they promise a safety they cannot deliver. Good: reusing the redaction rules with their section citation. Bad: citing the operations card as bundle doctrine. Borderline: reusing the fail-fast principle for a CLI tool, the logic carries, the file's service-lifecycle context does not fully.

**Verification, evidence, and uncertainty.** Sample claims from earlier sections and confirm each declares its stratum cleanly. This assignment's read ledger, six bundle files read in full, zero retrievals. Readers can check the citations but not the reading behind them.

**Second-order consequence.** This theme adds a third stratum the cluster's other themes lack, conditionally stated doctrine, rules the file itself scopes with wheres and whens, reusing the four-step default without its multi-instance condition is not paraphrase drift but evidence-boundary violation, the condition is part of the fact.

**Revision decision.** Publish the strata, countable ops-file content as local corpus fact, sibling-cited chains as by-name local fact, and all practice machinery as combined-evidence inference.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
