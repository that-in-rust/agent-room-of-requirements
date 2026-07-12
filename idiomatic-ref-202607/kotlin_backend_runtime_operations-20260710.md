# Kotlin Backend Runtime Operations

Use this reference when a Kotlin backend change alters how a service or worker is built, configured, started, observed, migrated, packaged, deployed, admitted to traffic, stopped, diagnosed, or recovered. It converts an accepted runtime behavior into target-owned operational evidence. It is not a mandate to add tools to every Kotlin change and does not establish one platform, service objective, alert threshold, or deployment model.

**Runtime boundary test**

Activate this reference when at least one accepted behavior changes across an environment or production lifecycle boundary:

| Boundary | Activation signal | First negative question | Required owner or evidence |
|---|---|---|---|
| build and dependency | wrapper, Kotlin/JVM line, framework plugin, dependency resolution, package, or image input changes | can the target build and package reproducibly with the intended versions? | repository wrapper, effective dependency result, build owner |
| static gate | formatter, lint, analysis, warning, or policy behavior changes | can the configured gate detect the targeted defect without blocking valid exceptions? | actual task and configuration, failing and passing fixture, policy owner |
| configuration | key, type, default, validation, precedence, refresh, or environment source changes | does missing or malformed production-like config fail safely before traffic? | typed binding, startup fixture, configuration owner |
| secrets | credential source, scope, rotation, redaction, or access changes | can a failure expose a real or test secret in output or persisted state? | secret platform, access policy, redaction checks, security owner |
| observability | outcome vocabulary, correlation, logs, metrics, traces, audits, dashboard, or alert changes | can a reviewer distinguish the failure and identify an authorized action? | bounded signal schema, query or alert test, operator owner |
| health and traffic | liveness, readiness, startup, dependency, degraded mode, or traffic stage changes | can automation send traffic too early or restart a recoverable service repeatedly? | platform semantics, degraded scenario, traffic owner |
| data migration | schema, data remediation, compatibility, migration tool, or rollout order changes | can old and new application states coexist, and what happens after partial failure? | production dialect, data owner, rehearsal, recovery plan |
| container and platform | runtime image, user, port, filesystem, resource, network, or orchestrator contract changes | does the artifact start with least necessary privilege and accepted resources? | package or image inspection, platform policy, startup and smoke evidence |
| CI and release | gate placement, artifact promotion, environment, approval, canary, or rollback changes | can an unverified or incompatible artifact advance to the next stage? | pipeline definition, immutable artifact identity, release owner |
| shutdown and recovery | drain, cancellation, in-flight request, lease, worker, queue, or restart behavior changes | can accepted work be lost, duplicated, or left unrecoverable during termination? | isolated shutdown/restart scenario, work identity, operations owner |

Do not activate a new runtime mechanism merely because the task mentions production, robust, scalable, or best practice. Convert the word into observable behavior and an owner decision first.

**Default operating sequence**

1. **Name the runtime outcome.** State what users or operators observe during normal operation, failure, degradation, shutdown, and recovery.
2. **Inspect the target.** Read project instructions, wrappers, effective versions, config binding, secret integration, migration tool, telemetry stack, health endpoints, package, pipeline, deployment, and runbooks that actually exist.
3. **Preserve the stance.** Keep Gradle versus Maven, Kotlin and Java targets, Spring versus Ktor, compiler plugins, migration tool, telemetry platform, image base, and deployment model unless their change is explicitly accepted.
4. **Map the lifecycle.** Trace source to package, config to startup, migration to mixed versions, release to traffic, signal to operator action, and termination to durable recovery.
5. **Select changed boundaries.** Load only build, config, observability, migration, container, CI, deploy, shutdown, or incident guidance that changes a decision or gate.
6. **Write operational requirements.** Define startup failure, compatibility, signal semantics, traffic admission, stop trigger, recovery, and data or work integrity in observable terms.
7. **Choose the smallest credible evidence.** Use configured local gates for deterministic behavior and production-like environments when platform, dialect, network, identity, or lifecycle semantics matter.
8. **Stage safely.** Preserve artifact identity, compatibility states, owner authority, monitoring, stop conditions, and rollback or forward recovery.
9. **Observe normal and failed paths.** Confirm signals are bounded, non-sensitive, fresh, and actionable; keep telemetry failure visible.
10. **Exercise termination and recovery.** Verify in-flight requests, workers, migrations, leases, queues, and external effects according to the accepted contract.
11. **Reassess from evidence.** Narrow claims that exceed the environment, add a missing boundary exposed by failure, and split independently recoverable outcomes.
12. **Freeze the handoff.** Persist target revision, decisions, exact actions, results, limitations, owners, recovery state, and invalidation events.

**Preservation defaults**

- Use the repository's wrapper and configured tasks; do not report a remembered command as executed evidence.
- Preserve Kotlin, Java, Spring, Ktor, compiler-plugin, dependency-management, migration-tool, telemetry, and platform versions unless upgrade is the accepted outcome.
- Prefer typed startup configuration at the application boundary and keep business logic independent of environment-name branches.
- Use the target's secret store and access policy; fake test values must be unmistakably non-production and absent from committed runtime credentials.
- Reuse existing logs, metrics, traces, health, and alert semantics when they already answer the changed question.
- Treat migration files and compatibility behavior as deployable code, including supported prior states and partial failure.
- Preserve the target package and image pipeline; a smaller or newer image is not automatically safer when compatibility and provenance are unverified.
- Keep fast and long-running gates in their project-owned stages while ensuring a consequential changed boundary has a blocking gate somewhere.
- Make graceful shutdown and restart evidence match request-scoped versus deliberately durable work.

These are defaults, not universal mechanisms. Explicit project policy, target behavior, current direct authority, and accountable owner decisions can adapt or reject them within their scope.

**Direct fit**

Use this reference for:

- changing Gradle or Maven tasks, compiler plugins, dependency versions, package or image creation;
- adding or changing typed settings, profile behavior, environment variables, secret injection, or startup validation;
- defining logs, metrics, traces, audits, health, dashboards, alerts, or incident queries;
- creating schema or data migrations and planning mixed-version rollout;
- changing container user, port, filesystem, resource, network, readiness, liveness, or shutdown behavior;
- changing CI gate placement, artifact promotion, deployment, canary, rollback, or forward recovery;
- hardening a service or worker for production and diagnosing an escaped runtime assumption.

Keep this reference as a companion rather than the primary guide when the central decision is domain modeling, framework wiring, authentication policy, query design, test fixture construction, or language syntax. Route product semantics, legal constraints, threat acceptance, data cleanup policy, service objectives, and live incident command to the accountable owners. This reference can carry their accepted constraints into runtime evidence; it cannot invent them.

**Stay, compose, split, or stop**

| Decision | Condition | Runtime result |
|---|---|---|
| stay with existing operations | code behavior changes but build, config, data, signals, platform, release, and recovery contracts remain stable | run inherited required gates and record why no runtime expansion is needed |
| adapt one boundary | one target-owned operational contract changes under the existing platform | update its requirement, artifact, negative scenario, and recovery evidence |
| compose specialists | runtime work depends on security, persistence, testing, performance, provider, or framework decisions | exchange bounded owner artifacts and reconcile them in one release route |
| split outcomes | schema, application, platform, traffic, or recovery work can be accepted or reversed independently | create separate requirements, owners, gates, compatibility, and handoff records |
| stop or escalate | destructive action, unowned service objective, missing platform authority, unknown data recovery, or unsafe production access blocks evidence | preserve a safe interim state and request the exact owner decision or environment |

**Good route**

A service introduces one required timeout setting. The route confirms the existing configuration binder and secret platform, adds typed validation, exercises valid, missing, and malformed production-like startup, preserves deployment tooling, and changes telemetry only if operators need a new failure distinction. It does not redesign the whole config system.

**Bad route**

A pure parser change triggers a new linter, metrics stack, container base, readiness endpoint, and arbitrary latency objective. None protects the parser contract, and each creates permanent compatibility and ownership work.

**Conditional route**

A schema migration is locally valid, but rolling-deploy policy and production data shape are unavailable. The route can specify production-dialect rehearsal, old/new compatibility, data profiling, and recovery questions. It remains planning-level and must not call rollback safe or rollout ready.

**Runtime evidence record**

```text
Accepted runtime outcome, failure, degradation, shutdown, and recovery
Target revision, framework, wrappers, versions, package, and platform
Changed lifecycle boundaries and deliberately unchanged boundaries
Project policy and accountable product, data, security, release, and operations owners
Selected mechanism, simpler baseline, assumptions, and reversal signal
Config, secret, schema, telemetry, health, pipeline, deploy, and runbook artifacts
First negative scenario and production-like evidence boundary
Exact commands or actions, environment, results, and limitations
Traffic stop, rollback or forward recovery, and post-recovery observation
Consumers, invalidation events, next review, fallback, and retirement
```

The frozen source provides historical operational questions and defaults. It does not establish a target's current tasks, platform, service objective, alert policy, migration safety, production capacity, or successful recovery. A detailed runbook remains a plan until its target-specific gates and owner-authorized recovery paths are observed.

## Source Evidence Mapping Table

The mapped runtime file is the first historical doctrine source for this theme, not the complete authority chain. Runtime decisions also depend on target policy, effective build and platform state, accepted product and data behavior, and observed transitions through startup, traffic, failure, shutdown, and recovery.

The complete required runtime-source read, companion heading inspection, and recorded hashes establish frozen source identity at their stated depth. They do not prove current public APIs, target adoption, service objectives, operational ownership, or successful production behavior.

**Frozen local evidence**

| Source and SHA-256 | Direct contribution to runtime routing | Non-authority boundary | First target reconciliation |
|---|---|---|---|
| `references/kotlin-backend-runtime-and-ops.md`, `d0a218f3c5d7b07c561cd4aba94b7c943aa7575cd439d371fdbaf4e5415b1069` | Historical defaults and questions for wrappers, versions, static gates, typed config, environments, observability, migrations, containers, CI, shutdown, and review | Does not establish a target task, platform, service objective, secret policy, traffic rule, or recovery result | Inspect the exact changed lifecycle boundary and execute its target-owned negative and recovery scenario |
| `references/reference-map.md`, `7451085f357ed6af8fdd41f592e83f5f4b5c7aa858be8a5456390b377f00f180` | Historical mode routing and common read orders that activate runtime guidance | Navigation cannot define runtime mechanism or prove deployability | Show which accepted outcome activates Operations and which companion mode owns each dependency |
| `SKILL.md`, `e3413837049aa6f31d325fa368bb8b9dcce7f298c770b42cd5f13c1217c3a410` | Historical entrypoint, delivery workflow, guardrails, output contract, and progressive context strategy | Top-level coordination cannot substitute for target artifacts or platform authority | Compare workflow assumptions with project instructions, owners, wrappers, and release path |
| `references/kotlin-backend-playbook.md`, `8654c3a4c68cda2514c546035e7a7908a99ad0f884088b7bf329abf807c31994` | Service, data, transaction, integration, coroutine, worker, compatibility, and delivery questions that shape runtime effects | Shared design advice does not select config, telemetry, migration, container, or deploy tooling | Trace runtime behavior back to the application, data, provider, and durable-work contract it protects |
| `references/kotlin-spring-ktor-idioms.md`, `02c20786240e893fc258f4e067557bc65dcdafcac11a6efbdd049710b827ac5d` | Historical Spring and Ktor configuration, lifecycle, health, framework test, and execution-model candidates | Separate framework examples do not authorize migration or match every effective version | Preserve the target framework and inspect actual plugins, properties, lifecycle hooks, and packaging |
| `references/kotlin-backend-testing-and-fixtures.md`, `92f45a34cc8ac472b930eba33e4ffb6a442719baa53dd8caabd43006dfa99e26` | Boundary-first test selection, production-dialect fixtures, migration evidence, framework hosts, providers, brokers, and quality gates | A named fixture or command is not evidence that the target configures or executed it | Discover repository-native gates and prove the runtime mechanism in a representative environment |
| `references/kotlin-backend-security-and-resilience.md`, `8a07eb77e27a3b508224db76c60e20508b8b3d13b81fce86e87ea052be7d14a5` | Secret, abuse, cancellation, timeout, retry, idempotency, external dependency, worker, and recovery questions | Does not define target threat policy, provider effect, total deadline, or accepted degraded behavior | Exercise secret redaction, failure classification, duplicate effects, cancellation, and owner-authorized recovery |
| `references/sources-and-research-brief.md`, `2f73340890073548e7c9a723ba051528e0097581444889cc7a8fa400026a1ee1` | Dated 2026-06-23 research lineage, premise checks, external mappings, and expert review lenses | Public summaries are not refreshed current authority and do not establish platform-specific operations | Use as provenance; retrieve direct current authority only for a material versioned mechanism when authorized |

The companion files add questions and boundary context. Repetition across them is not independent proof. For example, several files recommend explicit cancellation or migration testing; target call paths and executed environments determine whether those recommendations apply and whether they work.

**Inherited public mappings**

No browsing occurred. These locations are historical discovery leads inherited from the seed and dated research brief:

| Inherited location | Possible future question | What it cannot establish here | Required target gate after authorized refresh |
|---|---|---|---|
| `https://kotlinlang.org/docs/home.html` | Current Kotlin, JVM target, compiler, plugin, and interoperability behavior for a selected build or package change | Target wrapper, plugin alignment, framework support, image, CI, or deployment policy | Compile and package with effective target versions and run affected runtime compatibility checks |
| `https://github.com/Kotlin/kotlinx.coroutines` | Current coroutine cancellation, dispatcher, test, or lifecycle semantics for shutdown and worker behavior | Target pool, blocking dependency, framework integration, provider cancellation, or durable recovery | Exercise cancellation, timeout, shutdown, blocking isolation, and resource release in the target stack |
| `https://github.com/spring-guides/tut-spring-boot-kotlin` | A current Spring-maintained Kotlin example for narrowly comparable config or packaging | Target architecture, versions, migration tool, security, health policy, pipeline, or production objective | Match effective Spring and Kotlin lines and reproduce only the relevant configured behavior |
| `https://ktor.io/docs/welcome.html` | Current Ktor documentation root for selected config, plugin, health, logging, client, or shutdown behavior | Target plugin installation, deployment platform, alerting, provider contract, or traffic policy | Inspect pinned Ktor and run target module, plugin, startup, shutdown, and smoke fixtures |

Recognizable publishers do not make these rows current evidence. A direct future source must name mechanism, version, retrieval date, scope, and route impact. Public language or framework documentation cannot choose product degradation, data remediation, secret access, service objective, or production action authority.

**Target applicability evidence**

| Evidence class | Runtime question answered | Required identity | Frequent overreach |
|---|---|---|---|
| project instructions and ownership | Which operational conventions, approvals, environments, and recovery authorities govern the change? | instruction path, owner role, scope, target revision, and decision artifact | treating generic skill prose as policy |
| wrapper and effective build | Which Gradle or Maven tasks, Kotlin/JVM lines, plugins, dependencies, and package outputs exist? | wrapper, manifests or catalog, resolved versions, task, artifact, and result | assuming a remembered task or plugin is configured |
| configuration and secret system | Which keys, types, sources, precedence, validation, rotation, and redaction behavior apply? | binding code, environment contract, secret integration, startup state, and owner | treating environment variables as inherently typed or safe |
| service and workload lifecycle | Which requests, workers, dependencies, resources, deadlines, and durable effects must survive or stop? | call path, work identity, resource bounds, workload envelope, and accepted behavior | choosing health or shutdown semantics from framework defaults alone |
| observability and incident practice | Which signals, correlations, retention, alerts, dashboards, and operator actions are owned? | signal schema, query, alert, runbook, owner, last exercise, and blind spots | equating library presence with actionable diagnosis |
| schema and data migration | Which prior states, dialect, compatibility, data cleanup, ordering, and recovery rules govern change? | schema history, migration tool, production dialect, data profile, mixed-version contract, and data owner | calling local forward success rollback safety |
| package and platform | Which image, user, ports, filesystem, resources, network, proxy, orchestrator, and traffic states exist? | immutable artifact, build provenance, deployment definition, platform version, and owner | assuming a small image or non-root declaration proves runtime safety |
| CI and release | Which gates block pull request, package, promotion, canary, full integration, or production stages? | pipeline revision, environment, artifact identity, approvals, results, and release owner | treating a green stage as coverage for gates it did not execute |
| shutdown and recovery | Which in-flight requests, leases, queues, workers, migrations, and effects stop, drain, resume, or reconcile? | termination signal, grace period, work identity, restart state, observed result, and recovery owner | calling process exit graceful without effect evidence |

**Claim disposition record**

```text
Claim and changed runtime boundary
Frozen source path, complete region, SHA-256, and historical role
Current direct authority, version, and retrieval date when material
Target revision, exact artifact, effective configuration, and owner policy
Disposition: routing, promoted, adapted, conditional, rejected, superseded, or orientation-only
Normal, failure, shutdown, and recovery requirements affected
Exact action, environment, expected observation, result state, and limitation
Conflict, residual uncertainty, consumer, invalidation event, and fallback
```

**Evidence examples**

Good: the runtime source suggests typed startup validation. Target inspection finds an established binder and deployment-owned key source. A production-like startup fixture covers valid, missing, malformed, and redacted-secret states. The source contributes the question; project policy and observed startup make the target claim.

Bad: the Ktor documentation root is cited to declare readiness correct. Neither the target health semantics nor platform traffic behavior has been inspected.

Borderline: a migration succeeds on an empty local database and the source recommends production-dialect testing. The evidence supports file syntax and one forward path; existing data, mixed versions, locks, partial failure, and recovery remain conditional.

**Selective invalidation**

- Wrapper or dependency changes reopen build, compiler-plugin, package, and compatibility claims.
- Config or secret-platform changes reopen startup, precedence, access, redaction, rotation, and deployment evidence.
- Signal vocabulary or telemetry-platform changes reopen dashboards, alerts, runbooks, retention, and incident queries.
- Schema or migration-tool changes reopen supported prior states, production dialect, mixed versions, data repair, and recovery.
- Image, proxy, orchestrator, or traffic-policy changes reopen readiness, resources, shutdown, and staged rollout.
- Pipeline changes reopen gate coverage, artifact identity, promotion, approvals, and rollback evidence.
- Workload or effect changes reopen resource, deadline, backpressure, durable-work, and recovery assumptions.

A maintained source map should become more precise as target conventions settle, not merely longer. Promote proven local routes with owners and invalidation; retain the generic map for upgrades, incidents, and exceptions.

## Pattern Scoreboard Ranking Table

The inherited values 95, 91, and 88 are editorial seed ordering. No rubric, population, sample, denominator, scale, calibration, or observed runtime outcome supports interpreting them as confidence, reliability, adoption, coverage, effectiveness, or release priority. Preserve them as provenance only.

| Priority | Inherited value or role | Activate when | Failure prevented | Direct falsifier |
|---|---|---|---|---|
| Source Map First | 95; historical default | Selecting historical runtime questions and companion guidance | Agent invents an operational stack without knowing local doctrine | Route record names bounded source regions and the distinct target decision each changes |
| Evidence Boundary Split | 91; historical default | Frozen guidance, public material, target policy, execution, and synthesis appear together | Historical or generic advice is called current production fact | Every consequential claim retains evidence kind, revision, scope, and target gate |
| Verification Gate Coupling | 88; historical default | A recommendation changes build, config, data, signal, platform, release, or recovery behavior | Plausible operations prose cannot fail | Recommendation names target artifact, negative state, action, expected transition, result, and limitation |
| Runtime Outcome Before Tool | First intake gate | Production, robust, observable, scalable, or safe is vague | Tool adoption substitutes for accepted behavior | Normal, failure, degradation, shutdown, and recovery outcomes are observable and owned |
| Preserve Target Stance | Hard compatibility gate | Wrapper, Kotlin/JVM, framework, plugin, migration, telemetry, image, or platform is implicated | Bounded work becomes an unaccepted infrastructure migration | Effective target versions and established mechanisms are recorded with explicit migration authority |
| Immutable Artifact Identity | Hard provenance gate | Build output moves through CI, environments, or rollback | Different source or package is tested, promoted, and diagnosed | Revision, dependency set, build action, digest or artifact locator, and promotion lineage agree |
| Typed Startup Contract | Hard configuration gate | Keys, defaults, precedence, refresh, or environments change | Missing or malformed config reaches traffic or business logic | Production-like valid, absent, malformed, conflicting, and redacted states produce accepted startup behavior |
| Secret Boundary | Hard trust gate | Credentials, tokens, stores, rotation, logs, or errors change | Secret enters source, output, metrics, traces, or broad access | Fake-secret fixtures, access policy, redaction, rotation, and exposure response are exercised |
| Compatibility Before Migration | Hard data gate | Schema, data, protocol, event, job, or config shape changes | Old and new versions cannot coexist or partial migration corrupts state | Supported prior states, production dialect, mixed versions, data repair, and forward or rollback path are observed |
| Signal To Action | Hard observability gate | New logs, metrics, traces, audits, dashboards, or alerts are proposed | Telemetry creates cost and noise without diagnosis or recovery value | Representative failure is emitted, queried, interpreted, acted on, and recovered without sensitive data |
| Health And Traffic Truth | Hard platform gate | Startup, readiness, liveness, dependency policy, or canary changes | Automation sends traffic early or restarts a recoverable service | Slow start, degraded dependency, migration, traffic, and recovery scenarios produce intended platform state |
| Package And Least Privilege | Hard deployment gate | Image, user, port, filesystem, resource, network, or runtime command changes | Artifact is nonreproducible, overprivileged, or incompatible | Package provenance, user, permissions, required ports, resources, startup, and smoke behavior match policy |
| Gate Placement And Coverage | Promotion gate | CI tasks, long tests, environments, approvals, or release stages change | Green stages omit the changed boundary or rebuild unverified artifacts | Deliberate defect fails the intended stage and immutable artifact advances only after required evidence |
| Staged Rollout Control | Production gate | Canary, traffic, feature state, migration phase, or rollback changes | Blast radius grows before diagnosis and recovery can respond | Owner-defined signal stops progression and rollback or forward recovery restores accepted state |
| Graceful Termination | Hard lifecycle gate | HTTP requests, workers, queues, leases, or migrations can be active at stop | Accepted work is lost, duplicated, abandoned, or held indefinitely | Shutdown and restart scenarios show bounded drain, cancellation, durable identity, and reconciliation |
| Recovery Rehearsal | Promotion gate | Release can fail after state or traffic changes | Runbook describes an untested or unauthorized recovery path | Isolated exercise begins from partial failure and returns service, data, work, and signals to accepted state |
| Route Reassessment | Learning gate | First target evidence, incident, upgrade, workload, owner, or platform state changes | Initial operational assumptions persist after invalidation | Route narrows, expands, splits, demotes, or stops with retained causal evidence |

**Default delivery order**

For planned runtime change: define the observable lifecycle outcome; inspect and preserve target stance; identify immutable artifact and effective configuration; map data, service, dependency, and platform states; select only changed operational boundaries; define negative and recovery scenarios; run deterministic target gates; add production-like mechanism evidence; stage rollout with stop authority; verify shutdown and recovery; then retain the handoff and invalidation events.

Build and static gates occur early because they produce the artifact and fast feedback. They do not outrank data integrity, secret exposure, traffic safety, or recovery when those hazards activate. A formatter pass cannot compensate for a migration that lacks mixed-version compatibility.

**Incident and review overrides**

Start from the earliest observed causal break while preserving the failed artifact, revision, environment, traffic state, data state, and signals:

- missing config or unsafe default elevates Typed Startup Contract;
- exposed credential or private output elevates Secret Boundary and containment;
- data mismatch or partial migration elevates Compatibility Before Migration and Recovery Rehearsal;
- alert flood or silent failure elevates Signal To Action and telemetry integrity;
- readiness churn or premature traffic elevates Health And Traffic Truth;
- wrong artifact or dependency reaches an environment elevates Immutable Artifact Identity and Gate Placement;
- lost or duplicate work during termination elevates Graceful Termination and durable identity;
- canary degradation elevates Staged Rollout Control and owner-authorized recovery.

After containment, reconcile upstream build and policy plus downstream regression and runbook evidence. An incident starting point does not remove the need to correct the route that allowed the condition.

**Runtime profiles**

- **Focused config change:** target preservation, Typed Startup Contract, Secret Boundary if sensitive, configured tests, package startup, and handoff.
- **Signal change:** target preservation, Signal To Action, privacy and cardinality, alert or query exercise, telemetry failure, and runbook action.
- **Schema or data rollout:** Compatibility Before Migration, production dialect, data profile, mixed versions, Staged Rollout Control, and Recovery Rehearsal.
- **Container or platform change:** Immutable Artifact Identity, Package And Least Privilege, Health And Traffic Truth, configured resources, smoke, shutdown, and recovery.
- **Worker lifecycle:** artifact and config, durable work identity, signal and backlog semantics, Graceful Termination, restart, duplicate handling, and drain.
- **CI or release change:** Gate Placement And Coverage, immutable promotion, environment permissions, staged rollout, stop authority, and recovery.
- **Production hardening:** inspect every region, then prioritize findings by consequence and causal dependency rather than source order.

**Good prioritization**

A schema constraint change places production-dialect compatibility, historical data, old/new application coexistence, and recovery before dashboard refinements. Build and observability still run, but they do not turn migration safety into a lower priority merely because their checks are easier.

**Bad prioritization**

The route reports 95, 91, and 88 as confidence, adds a linter and health endpoint, and calls the service production-ready without inspecting config, data, traffic, shutdown, or owner recovery.

**Conditional prioritization**

A package starts locally and the image provenance is known, but the platform's readiness and termination behavior cannot be exercised. Artifact and local startup claims may pass; traffic and graceful-shutdown claims remain conditional and block only the rollout that depends on them.

Numeric rank cannot rescue a wrong artifact, leaked secret, incompatible schema, unowned alert, false readiness, missing gate, or unrehearsed recovery. Retain override reasons and review recurring failures. Change routing order from target evidence and incident causality, not from the apparent precision of inherited numbers.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The frozen runtime source provides historical questions and defaults for wrapper and version discipline, static gates, typed configuration, secrets, declarative environments, observability, migrations, containers, CI, shutdown, and operational review.

`external_mapping_unrefreshed_note`: The public locations inherited through the 2026-06-23 research brief were not retrieved during this evolution. They remain discovery leads, not current framework, coroutine, platform, compatibility, or security facts.

`combined_evidence_inference_note`: Idiomatic Kotlin backend runtime operations is an evidence-bounded lifecycle loop. It starts from an accepted runtime outcome, preserves the target build and platform stance, identifies the changed state transitions, proves them with target-owned gates, stages change under bounded traffic and authority, observes failure and recovery, and selectively revises or retires the route from results.

Use this loop:

1. **Name the runtime outcome.** Define normal behavior, degraded behavior, failure, shutdown, recovery, users or operators, and accountable owners.
2. **Inspect the target.** Read project instructions, wrapper, effective dependencies, config binding, secret integration, migrations, telemetry, health, package, pipeline, deployment, runbooks, and supported environments.
3. **Preserve the stance.** Keep established build, versions, framework, compiler plugins, migration tool, telemetry, image, and platform unless their change is accepted independently.
4. **Trace the lifecycle.** Follow source to artifact, artifact to environment, config to startup, migration to mixed versions, release to traffic, signal to action, termination to recovery, and incident to learning.
5. **Select changed boundaries.** Activate only build, config, secrets, observability, data, container, CI, traffic, shutdown, or recovery concerns whose behavior or policy changes.
6. **Write executable runtime requirements.** Convert reproducible, secure, observable, healthy, deployable, scalable, graceful, and recoverable into target-owned state and transition contracts.
7. **Design with recovery visible.** Compare the existing mechanism with alternatives, including compatibility, permissions, operational burden, failure amplification, and reversal.
8. **Run deterministic gates.** Use repository-native wrapper, configured analysis, startup, serialization, migration, packaging, and fixture checks where they can falsify the claim.
9. **Add production-like evidence.** Use representative dialect, platform, identity, traffic, dependency, resource, and lifecycle behavior only when the accepted claim depends on it.
10. **Stage under control.** Preserve immutable artifact identity, compatible states, owner authority, monitoring, stop conditions, and rollback or forward recovery.
11. **Exercise shutdown and recovery.** Observe requests, workers, leases, queues, migrations, dependencies, data, signals, and runbook action through return to an accepted state.
12. **Freeze and reassess.** Record evidence, limitations, consumers, invalidation events, and what should expand, narrow, split, stop, or retire.

**Governing principles**

- **Lifecycle outcome before tool.** Production terminology does not authorize a linter, telemetry vendor, container base, health endpoint, pipeline, or service objective.
- **Target before ecosystem preference.** Repository and platform policy choose established mechanisms within their scope; public authority informs selected current mechanisms.
- **Preserve artifact lineage.** The source, dependencies, build action, package, environment, and release result must refer to the intended artifact.
- **Configuration is an input contract.** Parse, type, validate, and inject settings at startup boundaries; avoid environment-name branches in business behavior.
- **Secrets are both data and authority.** Store, access, rotate, redact, test, and recover exposure according to target policy; environment variables alone are not a security model.
- **Signals answer decisions.** Logs, metrics, traces, audits, dashboards, and alerts earn cost when they distinguish a failure and support an authorized action.
- **Health controls automation.** Readiness, liveness, startup, and degraded states need platform-specific semantics because wrong signals can amplify harm.
- **Migrations are deployed behavior.** Production dialect, historical data, mixed versions, partial failure, data remediation, and recovery matter before rollout.
- **CI gates claims, not checkbox volume.** A green stage supports only the tasks, artifacts, environments, and boundaries it actually exercised.
- **Shutdown is correctness.** Request-scoped work should stop and release resources; deliberately durable work needs identity, ownership, restart, and reconciliation.
- **Recovery is observed, not promised.** A runbook remains a plan until an authorized scenario demonstrates containment and an accepted recovered state.
- **Every mechanism creates lifecycle cost.** New plugins, signals, stores, pipelines, and controls need owners, consumers, compatibility, tests, and retirement.

**Entry overrides**

New delivery normally follows the loop from outcome and target through stage and recovery. Known failures may begin elsewhere:

- begin with configuration and secret containment when startup or exposure has failed;
- begin with data compatibility and migration state when schema or historical data is at risk;
- begin with health and traffic when automation is routing incorrectly or restarting the service;
- begin with artifact lineage and pipeline when the wrong package or dependencies reached an environment;
- begin with observability when the service is failing but the condition cannot be distinguished or acted on;
- begin with shutdown and durable-work identity when termination loses, duplicates, or strands work;
- begin with recovery authority when production state is already partial or degraded.

Preserve target revision, artifact identity, configuration, data state, environment, traffic, timestamps, and bounded signals before changing them. Then reconcile the earlier lifecycle contracts so containment does not become an isolated workaround.

**Route sufficiency**

A focused runtime route is sufficient when every changed state transition has an owner, target artifact, failure scenario, evidence method, stop condition, recovery, and invalidation event. It does not require every source region or a new tool.

The route is insufficient when:

- wrapper, effective versions, package, or promoted artifact is guessed;
- a config or secret change lacks production-like startup and redaction behavior;
- signals have no bounded semantics, consumer, action, or telemetry-failure state;
- health behavior has not been reconciled with platform traffic and restart policy;
- a schema change lacks supported prior states, production dialect, historical data, mixed versions, or recovery;
- an image or deployment change lacks provenance, permissions, resources, startup, smoke, and termination evidence;
- a green pipeline cannot show which changed boundary it executed;
- a canary or rollout has no owner-authorized stop and recovery condition;
- shutdown behavior ignores in-flight requests, durable work, leases, effects, or restart;
- current external behavior is asserted from an unrefreshed mapping;
- an operational claim exceeds the observed environment, workload, or recovery range.

**Good, bad, and conditional outcomes**

Good: a Spring service adds a required external-client timeout. The route preserves Gradle, Kotlin, Spring, config binding, telemetry, and deploy platform; adds typed validation; exercises valid, missing, and malformed production-like config; traces the timeout through the client and total deadline; and adds one bounded failure signal plus runbook action only if the existing signals cannot distinguish it.

Bad: a Ktor worker change adds a new container base, logging stack, metrics backend, readiness plugin, CI system, and generic latency objective before target discovery. The result has more production vocabulary and more unsupported control planes.

Conditional: a versioned migration succeeds against an empty local database, while historical data, old/new application coexistence, and production recovery are unavailable. The route can be implementation-ready for migration syntax and blocked for rollout safety. It must not average those states into `mostly deployable`.

**Evidence ladder**

1. Confirm frozen source identity and the exact question being reused.
2. Confirm target instructions, wrapper, effective versions, artifacts, policies, and owners.
3. Trace changed lifecycle boundaries and deliberately unchanged boundaries.
4. Map each runtime requirement to a deterministic or production-like gate capable of failure.
5. Preserve pre-change or injected failure evidence where safe.
6. Execute the narrowest gate, then affected integration, platform, migration, traffic, shutdown, and recovery scenarios.
7. Confirm signals support diagnosis and action without sensitive data or unbounded cardinality.
8. Compare observed state with the route; add, remove, split, or stop operational scope deliberately.
9. Persist exact actions, results, limitations, residual owners, and invalidation triggers.

This thesis does not choose Gradle over Maven, Spring over Ktor, Flyway over Liquibase, one telemetry system, one image, one CI provider, one orchestrator, one service objective, or rollback over forward recovery. The target and accountable owners decide those mechanisms and policies; evidence demonstrates whether the accepted transition works in scope.

The durable artifact is a versioned route from one accepted runtime outcome to one reproducible recovery evidence set. Repeated growth across independent data, platform, security, and release decisions is a signal to split outcomes and reconcile their interfaces rather than loading a larger undifferentiated operations context.

## Local Corpus Source Map

`local_corpus_sourced_fact`: The primary frozen source is `agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/references/kotlin-backend-runtime-and-ops.md`. It was read completely for this evolution. Its SHA-256 digest at review time was `d0a218f3c5d7b07c561cd4aba94b7c943aa7575cd439d371fdbaf4e5415b1069`. The digest identifies the historical input; it does not prove that a target repository uses the same tools or that an operational recommendation still matches a current platform.

The source is a compact set of runtime review regions, not a complete production design. Retrieve by the lifecycle transition under change, then expand at every security, data, framework, test, or recovery dependency. A heading match is an orientation signal, not implementation authority.

| local_source_region | retrieve_when | durable_question_preserved | important_trap_or_companion | first_target_evidence_gate |
| --- | --- | --- | --- | --- |
| Build And Dependency Discipline | wrapper, dependency, plugin, compiler, packaging, or runtime artifact behavior changes | Are repository-owned build mechanisms and aligned versions producing the intended artifact reproducibly? | Do not add fashionable build machinery; pair compiler-plugin questions with framework idioms and package identity | locate project instructions and wrapper; resolve effective versions; run the configured build or package action; identify the resulting artifact |
| Static Analysis And Formatting | configured formatting, lint, static analysis, or maintainability policy changes | Which configured fast gate detects style or structural defects, and what claim does it actually support? | Formatter success is not architecture, security, migration, or runtime evidence; pair with affected behavioral tests | locate configured tasks and rules; run the narrow task; preserve violations and rule ownership; confirm CI invokes the same gate when that is claimed |
| Configuration And Secrets | keys, defaults, binding, validation, credentials, redaction, or dependency injection changes | Does startup produce one typed, validated runtime configuration without exposing secret material? | A secret location is not an authorization, rotation, redaction, or exposure-recovery design; pair with security and framework binding regions | exercise valid, absent, malformed, and sensitive inputs through the actual startup path; inspect bounded outputs for disclosure |
| Profiles And Environments | deployment behavior differs by environment or profile | Are differences declarative inputs rather than hidden branches in business behavior? | An environment name can become an untested feature flag; pair with configuration, package, deployment, and production-like tests | enumerate supported profiles and required keys; compare effective config; start the packaged artifact with representative non-secret values |
| Observability | logs, metrics, traces, health, alerting, or diagnostic behavior changes | Can a bounded signal distinguish the failure and lead an accountable consumer to a useful action? | More telemetry can leak data, explode cardinality, or obscure diagnosis; health also controls platform traffic and restart automation | inject or reproduce the failure; inspect signal semantics, identifiers, privacy, cardinality, propagation, consumer, and runbook action |
| Database Migrations | schema, constraints, indexes, data shape, persistence compatibility, or deployment order changes | Can old and new application versions plus historical data move through supported states without ambiguity or loss? | Empty local databases hide production-dialect and data-shape failures; pair with persistence tests, transaction boundaries, rollout, and recovery | run versioned migrations against the production dialect and representative prior data; exercise mixed versions and the authorized recovery path |
| Container And Deployment Safety | image, user, ports, resources, health, traffic, startup, or termination changes | Does the immutable package start with least privilege, report truthful lifecycle state, receive traffic safely, and terminate without losing required work? | A locally running image does not establish provenance, platform policy, readiness truth, or graceful worker behavior | inspect image inputs and identity; run package smoke; verify effective user and ports; exercise startup, readiness, liveness, traffic, signal, drain, and restart behavior |
| CI Expectations | pull-request, scheduled, package, release, migration, or environment gates change | Does each gate execute the changed boundary against the artifact and environment it claims to protect? | A green pipeline can be fast but irrelevant, or comprehensive but too late; pair with immutable promotion, permissions, and rollout control | trace source revision to task, environment, artifact digest, result, promotion, and failure retention; deliberately fail the changed gate |
| Operational Review Questions | production readiness, incident prevention, handoff, or recovery scope is broad or unclear | How do config, secrets, migration, diagnosis, shutdown, retries, and restarts fail and recover together? | A checklist can hide absent owners and untested transitions; pair every answer with a target mechanism, scenario, result, and residual limit | conduct a lifecycle review from build through recovery; assign owners and stop conditions; exercise the highest-consequence unresolved transition |

**Companion source routes**

The primary runtime file deliberately omits implementation detail owned elsewhere in the same frozen corpus. Open companions only when their boundary activates:

| companion_local_source | activate_for | contribution_to_runtime_route | boundary_not_proved_by_reading |
| --- | --- | --- | --- |
| `references/kotlin-backend-playbook.md` | transactions, coroutine/blocking boundaries, external clients, workers, DTO/domain/persistence separation, or service anatomy | explains application boundaries whose lifecycle must remain correct during config, release, and shutdown | does not prove the target framework, driver, broker, transaction, or deployment behavior |
| `references/kotlin-backend-security-and-resilience.md` | credentials, trust, authorization, retries, idempotency, external calls, background work, or coroutine cancellation | supplies trust and repeated-effect questions that runtime configuration and recovery must preserve | does not establish target policy, granted permissions, provider semantics, or containment results |
| `references/kotlin-backend-testing-and-fixtures.md` | framework, coroutine, persistence, contract, property, or integration evidence | helps choose a gate that can falsify the runtime requirement at the affected boundary | does not turn a test double or empty database into production-like evidence |
| `references/kotlin-spring-ktor-idioms.md` | Spring or Ktor binding, lifecycle, serialization, status handling, compiler plugins, or test mechanisms | maps general runtime questions onto framework-owned extension points already present in the target | does not authorize switching framework, execution model, or plugin versions |
| `references/reference-map.md` | task mode is unclear or several local files appear equally relevant | supplies historical read orders and cross-reference orientation | does not replace target discovery or the complete relevant source region |
| `references/sources-and-research-brief.md` | a current mechanism, compatibility range, or public authority must later be established | records historical public discovery leads and research provenance | remains unrefreshed in this no-browse evolution and cannot support a current external claim |

**Progressive retrieval profiles**

1. **Configuration key or binding change:** read Configuration And Secrets plus Profiles And Environments. Add framework Configuration for actual binding, Security And Resilience for sensitive values, and Testing And Fixtures for startup scenarios. Verify packaged startup with valid, absent, malformed, and redacted inputs.
2. **New metric, log, trace, or alert:** read Observability. Add Trust Boundaries when values can identify users or credentials, External Clients And Workers when propagation crosses an asynchronous boundary, and platform deployment material when health or alert routing controls automation. Inject a distinguishing failure and follow the signal to an owner action.
3. **Schema or data transition:** read Database Migrations. Add Persistence Defaults, Transaction Boundaries, Persistence Tests, Container And Deployment Safety, and CI Expectations as needed. Use production dialect, historical data, mixed application versions, partial failure, and authorized recovery.
4. **Image or platform behavior:** read Build And Dependency Discipline plus Container And Deployment Safety. Add Configuration And Secrets, Observability, and Security And Resilience where the image carries runtime inputs or permissions. Trace source revision to image digest, startup, traffic, resource pressure, termination, and restart.
5. **Pipeline or release control:** read CI Expectations and the changed implementation region. Add migration, package, health, or security regions only when the pipeline claims to gate them. Prove failure placement and immutable artifact promotion rather than counting stages.
6. **Worker shutdown or restart:** read Container And Deployment Safety, then External Clients And Workers, Background Work, Coroutine Resilience, Idempotency, Observability, and relevant broker or store behavior. Exercise cancellation, drain, timeout, lease or acknowledgment, restart, duplicates, and reconciliation.
7. **Production-readiness review:** read the complete runtime source and relevant companions. Build a lifecycle matrix rather than applying every listed tool. Route each unresolved high-consequence state to an owner, target gate, stop condition, and recovery scenario.
8. **Known incident:** begin with the region closest to the preserved failure. Expand upstream to the artifact, config, policy, or data state that admitted it and downstream to regression, recovery, and runbook evidence. Do not let source order delay containment.

**Retrieval failure patterns**

- Reading only the bullet that names a tool can discard the condition that the tool must already be configured or target-appropriate.
- Reading the whole corpus before inspecting the target can crowd out the actual wrapper, pipeline, platform, and incident evidence.
- Mapping by filename alone can miss that a telemetry change is also a privacy, health, client-propagation, or runbook change.
- Treating a local source as current public authority can preserve stale versions or provider behavior. Local provenance proves what was written, not present compatibility.
- Treating target convention as automatically safe can normalize a recurring defect. Use local doctrine to ask sharper questions, then let target and result evidence accept or reject the mechanism.
- A copied command without repository discovery can run the wrong task or bypass configured policy. Record actual target actions and results.
- A comprehensive checklist without owners or scenarios can produce optimistic completion language while recovery remains unknown.

**Region extraction record**

For each consequential route, retain:

```text
source_path:
source_hash:
source_region:
source_role: local fact | systems synthesis | historical lead
runtime_outcome:
changed_state_transition:
target_instruction_or_policy:
target_artifact_or_locator:
companion_regions_opened:
mechanism_preserved_or_changed:
failure_scenario:
verification_action:
observed_result:
recovery_result:
remaining_limit:
owner:
invalidation_event:
```

This record is useful only when populated from actual evidence. An unexecuted future command belongs in a planned gate, not an observed result. An inaccessible production-like environment should produce a conditional release claim, not a fabricated pass.

**Selective invalidation and reuse**

A change to the wrapper, Kotlin or Java level, compiler plugin, framework, migration tool, telemetry integration, image base, CI definition, secret provider, traffic policy, shutdown contract, or recovery authority invalidates the routes that depend on that mechanism. It need not invalidate unrelated decisions whose target artifacts and scenarios remain unchanged. Conversely, an incident can reveal a missing dependency between regions and should expand the map for future routes.

Stable platform conventions may compress later retrieval because target ownership and gates are already known. Keep an expansion path for upgrades, cross-owner changes, data transitions, and incidents. The goal is not the fewest source lines; it is the smallest evidence set that preserves the changed lifecycle, its counterexample, and its recovery boundary.

## External Research Source Map

`external_mapping_unrefreshed_note`: No public page was retrieved during this evolution. Every URL below was inherited from the frozen 2026-06-23 research brief or the 2026-06 generated reference. The map records where a future authorized investigation could begin; it does not assert present content, supported versions, defaults, maintenance status, redirect targets, compatibility, security posture, or target applicability.

External research should answer one named uncertainty after target discovery. Resolve the wrapper, effective dependencies, Kotlin and Java levels, framework mode, compiler plugins, persistence and migration components, telemetry integrations, image and platform, and deployed artifact before choosing a version-sensitive authority. When the target is being upgraded, record the current and candidate stances separately.

| runtime_claim_area | inherited_discovery_leads | preferred_authority_for_future_refresh | refresh_trigger | source_alone_does_not_prove |
| --- | --- | --- | --- | --- |
| Kotlin language and JVM behavior | `https://kotlinlang.org/docs/home.html`; brief also recorded server, coding, data-class, serialization, and compiler-plugin pages under `kotlinlang.org` | version-applicable Kotlin language or compiler documentation; compiler release material; implementation tests when documentation is ambiguous | Kotlin, Java, compiler, serialization, all-open, no-arg, target bytecode, or interop behavior changes | framework proxying, persistence construction, package startup, platform policy, or deployed compatibility |
| Coroutine cancellation, context, dispatchers, exceptions, and timeouts | `https://github.com/Kotlin/kotlinx.coroutines`; brief also recorded coroutine pages under `kotlinlang.org` | versioned coroutine documentation and API; repository release notes, source, and tests for exact library behavior | coroutine library, execution model, dispatcher, timeout, shutdown, worker, or cancellation boundary changes | that a framework, driver, broker, or blocking dependency propagates cancellation safely |
| Spring Boot and Spring Framework Kotlin integration | `https://github.com/spring-guides/tut-spring-boot-kotlin`; brief recorded Spring Boot Kotlin, Spring Kotlin, coroutine, testing, security, Actuator, metrics, health, Testcontainers, and Flyway pages under `docs.spring.io` | exact Spring Boot, Framework, Security, or integration reference matching the effective release train; official compatibility and release material | Spring, Boot, Security, web stack, test slice, configuration binding, Actuator, health, metric, or compiler-plugin integration changes | target bean graph, generated proxies, security policy, effective endpoints, platform traffic behavior, or production recovery |
| Ktor server and client integration | `https://ktor.io/docs/welcome.html`; brief recorded routing, type-safe routing, serialization, database, and testing pages plus `https://github.com/ktorio/ktor-samples` | version-applicable Ktor documentation and API; official source, release notes, and tests for exact plugin or engine behavior | Ktor, server engine, client engine, plugin, serialization, routing, test harness, lifecycle, or configuration changes | target plugin order, engine settings, provider behavior, package startup, or safe termination of target work |
| Persistence API and transaction semantics | brief recorded Exposed documentation under `jetbrains.com`, jOOQ documentation under `jooq.org`, and representative repositories | exact library manual and API plus database-driver and database-engine authority for the resolved versions and dialect | persistence library, driver, transaction, isolation, mapping, generated schema, query, or database version changes | historical-data compatibility, lock behavior under target workload, rollout order, or recovery correctness |
| Migration mechanism and schema history | brief recorded Flyway documentation under `documentation.red-gate.com` and a Spring Actuator Flyway endpoint page | versioned migration-tool documentation; database-engine DDL and transaction semantics; target migration history | migration tool, database dialect, schema, constraint, index, deployment order, or migration observability changes | that old and new applications coexist, existing data satisfies constraints, or rollback and roll-forward are safe |
| Testing, fixtures, and property evidence | brief recorded Kotest, MockK, Testcontainers Java, ktlint, and detekt locations | exact tool documentation and release material, subordinate to repository configuration and the behavior under test | test framework, mocking, coroutine scheduler, container fixture, static rule, or CI execution changes | production equivalence, architecture quality, provider policy, real latency, or recovery under live dependencies |
| Telemetry and health integration | brief recorded Spring Actuator and Micrometer-related pages; no complete vendor, collector, query, alert, or platform map was frozen | exact framework integration plus current telemetry protocol, SDK, backend, platform, privacy, and alert-provider authority selected from target dependencies | signal schema, exporter, collector, sampling, cardinality, health endpoint, platform probe, dashboard, or alert changes | signal delivery, bounded cost, redaction, consumer action, truthful readiness, or incident diagnosis in the target environment |
| Container, CI, secret store, traffic, and runtime platform behavior | no complete primary platform mapping appears in the four-row seed or frozen brief | target organization's platform policy and exact provider or orchestrator documentation for image, identity, secret, pipeline, health, traffic, termination, and recovery mechanisms | provider, runner, base image, architecture, identity, secret integration, deployment strategy, health policy, or termination behavior changes | organizational authorization, effective permissions, immutable promotion, traffic state, shutdown completion, or owner response |
| Security, compatibility, and urgent operational change | the frozen brief is a historical research synthesis rather than a live advisory feed | maintainer advisory, vulnerability database designated by target policy, release notes, compatibility matrix, provider notice, and accountable security or platform owner | security advisory, end-of-support notice, breaking release, deprecation, provider incident, or material compatibility change | exploitability, exposure, accepted risk, containment, patch success, or recovery for the deployed target |

The four URLs in the original generated reference remain useful discovery anchors, but their labels change from `external_research_sourced_fact` to `unrefreshed_historical_lead` in this evolved section. That distinction prevents a dated map from silently becoming a current recommendation.

**Claim-directed authority ladder**

Use the lowest rung that leaves the consequential uncertainty unresolved, then move upward deliberately:

1. **Target fact:** project instructions, wrapper, effective dependency report, configuration, artifact digest, deployment definition, policy, and observed state establish what is actually in scope.
2. **Versioned primary documentation:** use an official manual or API reference applicable to the resolved component and release for stated supported behavior.
3. **Compatibility, release, and advisory material:** use these when the decision depends on changed defaults, deprecations, support windows, interoperability, or security.
4. **Normative platform or provider authority:** use the owner of traffic, health, identity, secret, image, CI, database, broker, or shutdown semantics when that layer can override a library default.
5. **Official source and tests:** inspect them when documentation is silent or ambiguous, while distinguishing implementation detail from a supported contract.
6. **Official tutorials and samples:** use them for vocabulary and supported entry points, never as sole evidence for production configuration, security, compatibility, or recovery.
7. **Representative repositories and secondary explanation:** use them to discover alternatives or recurring integration shapes, then verify decisive claims with stronger evidence.
8. **Target exercise:** run the actual startup, cancellation, migration, health, package, rollout, shutdown, or recovery scenario. Public authority explains expected mechanism behavior; target evidence establishes the scoped outcome.

More sources are not automatically stronger. Three tutorials repeating the same default do not outweigh a versioned compatibility note or an effective target configuration. Stop researching when the exact claim, applicable version, authoritative owner, target consequence, verification action, and remaining limitation are explicit enough for the accepted risk.

**Future refresh workflow**

1. State the decision in falsifiable terms, such as: "For resolved coroutine library version X, cancellation of this parent scope reaches this worker boundary before platform termination deadline Y."
2. Capture target coordinates and mode: Kotlin, Java, framework, compiler plugins, coroutine library, engine, driver, database, migration tool, telemetry, image, CI, and platform components that matter.
3. Choose the authority that owns the uncertain behavior. Do not begin at a framework home page when the uncertainty belongs to a database engine or orchestrator.
4. Retrieve the exact page, version, release, commit, advisory, or provider policy. Record retrieval time and selector rather than relying on a search result summary.
5. Extract the smallest claim needed, with its prerequisites, exceptions, defaults, and version scope. Preserve disagreement rather than blending incompatible statements.
6. Compare it with the effective target mechanism. A correct external fact may be irrelevant because the target uses a different engine, profile, feature flag, or platform override.
7. Design a scenario capable of disproving the target consequence, including a negative or degraded path when failure semantics matter.
8. Execute available deterministic and production-like gates. Keep inaccessible environments and owner decisions conditional.
9. Record the result, stronger claim not proved, residual risk, accountable owner, and event that forces refresh.
10. Link the evidence to the runtime requirement, artifact, pipeline gate, rollout condition, runbook, and recovery action that consume it.

**Source selection counterexamples**

- Good: the target resolves a specific coroutine version and uses a framework-managed application scope. A shutdown change consults version-applicable cancellation documentation plus the framework lifecycle authority, then exercises cancellation, non-cooperative work, deadline expiry, resource release, restart, and duplicate handling in the packaged service.
- Bad: a tutorial demonstrates a health endpoint, so a route adds it and declares readiness solved without checking the target framework version, critical dependencies, platform probe semantics, startup windows, traffic policy, privacy, or induced failure.
- Good: a migration change uses migration-tool guidance for ordering, database-engine documentation for DDL behavior, target history for prior states, and mixed-version tests for application compatibility. Each source owns a distinct uncertainty.
- Bad: a generic Kotlin documentation page is cited for a container base, CI gate, secret delivery method, service objective, or rollback policy that Kotlin does not own.
- Conditional: current provider documentation cannot be accessed, but source-to-image identity, local package startup, and non-root execution are observed. Those claims may pass; traffic, managed identity, termination grace, and platform recovery remain unproved.
- Exploratory: a greenfield design compares Spring and Ktor official entry points before choosing either. Record option assumptions and expected tradeoffs; do not describe one as the target stance until the project decision and executable spike support it.

**Common external-evidence failure modes**

- The documentation selector silently shows the newest release while the target resolves an older train.
- A GitHub default branch contains behavior not present in the released dependency.
- A direct dependency version is known but a transitive engine, driver, telemetry SDK, or plugin owns the observed behavior.
- A language-level rule is applied to a framework-generated proxy, serializer, persistence constructor, or reflection path without integration evidence.
- An official sample optimizes readability and omits secrets, failure handling, permissions, scale, mixed versions, or recovery.
- Framework health semantics are mistaken for platform traffic and restart semantics.
- Library timeout or retry behavior is composed without a total deadline, idempotency, cancellation, or downstream quota analysis.
- A migration tool's supported syntax is mistaken for safe historical-data conversion and rolling deployment.
- An official source is current but too general to establish an organizational policy or accepted risk.
- A redirected, archived, renamed, or unmaintained source is retained without reassessing the consuming route.
- Public research displaces direct evidence from the failing artifact, effective config, data state, pipeline, or incident timeline.

**Future external evidence ledger**

```text
decision_id:
runtime_claim:
target_revision:
target_artifact_digest:
resolved_component_and_version:
execution_or_platform_mode:
authority_owner:
source_url_or_revision:
retrieved_at:
version_selector_or_commit:
source_role:
extracted_fact:
prerequisites_and_exceptions:
conflicting_evidence:
target_mechanism_locator:
verification_scenario:
verification_action:
observed_result:
stronger_claim_not_proved:
residual_risk_and_owner:
refresh_or_invalidation_event:
consuming_requirement_or_runbook:
```

Use `unrefreshed_historical_lead` until retrieval occurs. Use `refreshed_external_fact` only for the bounded extracted statement, never for the entire page. Label combinations across sources as synthesis. Label repository policy as target policy and command or scenario outcomes as observed results.

**Conflict and uncertainty handling**

When sources disagree, first check version, product edition, execution mode, default versus configured behavior, and which component owns the boundary. Prefer a normative or versioned authority over an example. If disagreement remains and the target consequence is material, preserve both claims, run a discriminating scenario, and escalate unsupported policy or risk acceptance to the accountable owner. Do not average incompatible semantics into a vague recommendation.

Currentness is event-driven rather than a universal expiry interval. Refresh when a resolved component, platform, integration mode, default, support status, advisory, provider policy, artifact, or consuming requirement changes; when a target test contradicts the source; or when an incident exposes an omitted state. Stable language syntax may remain useful longer than managed-platform behavior, but even stable material must still match the target version and claim.

This map intentionally does not choose Spring over Ktor, one coroutine architecture, one database or migration tool, one telemetry stack, one image, one CI service, one secret store, one platform, or one release strategy. It tells a future route how to find the authority that owns the selected mechanism and how to keep that authority subordinate to target evidence and accountable operational policy.

## Anti Pattern Registry Table

`combined_evidence_inference_note`: The entries below combine cautions in the frozen local runtime source with systems reasoning. They are investigation and design-review triggers, not proof that a target contains the defect. Classify the earliest broken lifecycle transition, preserve evidence, and verify the safer route against the target.

| anti_pattern_failure_name | activation_or_detection_signal | causal_runtime_risk | safer_default_replacement | falsification_or_recovery_gate | exception_or_limit |
| --- | --- | --- | --- | --- | --- |
| context_free_runtime_summary | output names generic Kotlin production practices without target wrapper, framework, artifact, platform, owners, or changed state | plausible advice can replace repository policy and leave the actual failure path untouched | begin with target stance and one accepted runtime outcome; retrieve only activated source regions | trace every consequential recommendation to a target locator, scenario, result, and remaining limit | broad orientation may precede target access if it is labeled exploratory and makes no adoption claim |
| inherited_source_as_current_fact | dated local URL or prose is presented as current framework or provider behavior | stale version, default, compatibility, or security assumptions can look authoritative | retain historical provenance; refresh the exact mechanism from applicable primary authority when authorized | record retrieval selector and version, compare effective target mechanism, then exercise the consequence | no refresh is needed when no current external claim consumes the historical lead |
| wrapper_bypass_delivery | build or verification uses an unapproved local tool or globally installed version | local success can produce a different dependency graph, bytecode, plugin set, or artifact than CI and release | use repository instructions and wrapper; preserve build machinery unless an upgrade is separately accepted | compare effective versions and artifact identity across local gate, CI, package, and promoted revision | an emergency recovery action may use a controlled alternate tool only with owner approval and retained artifact evidence |
| plugin_version_drift | Kotlin, framework, serialization, all-open, no-arg, or analysis plugin versions move independently | compilation can pass while proxying, reflection, generated code, or runtime construction changes | align versions according to target build and applicable compatibility authority; change them as one explicit upgrade route | compile and package affected framework paths; exercise proxy, serialization, persistence, and startup behavior | independent versions are acceptable when the resolved compatibility contract explicitly supports them |
| formatter_as_runtime_proof | formatting or lint success is cited as evidence for maintainability, security, compatibility, or production readiness | a cheap style signal masks behavioral, data, and lifecycle gaps | let each configured gate support only its stated claim; add behavioral and production-like evidence where activated | inject a defect outside the formatter's domain and show that another mapped gate detects it | style-only changes may legitimately stop at formatting plus relevant compile or documentation checks |
| deep_untyped_config_lookup | business logic repeatedly reads string keys or ambient environment state | missing, malformed, mutable, or inconsistently interpreted values fail late and scatter policy | bind and validate typed configuration at startup, then inject the narrow settings required by each boundary | exercise valid, absent, malformed, boundary, and restart cases through packaged startup and core behavior | a framework adapter may read raw config once at the composition boundary before producing typed values |
| environment_name_business_branch | core behavior switches on labels such as development, staging, or production | environment drift becomes hidden product behavior that is hard to enumerate and test | express capabilities and policy as validated declarative inputs or explicit feature contracts | compare effective config across supported profiles and run the same behavior scenarios with deliberate input differences | a composition root may select infrastructure adapters by environment when the mapping is explicit and tested |
| secret_location_as_security_model | a value is moved to an environment variable or secret store and declared secure | storage location alone does not define access, rotation, redaction, audit, revocation, or exposure recovery | follow target secret policy across storage, identity, injection, use, output, rotation, containment, and recovery | run missing and denied-access startup; inspect logs, errors, traces, dumps, and runbook actions for disclosure | low-sensitivity development credentials may use simpler handling when visibly fake and isolated from production authority |
| secret_bearing_diagnostics | config objects, exceptions, command output, health details, or telemetry serialize sensitive material | diagnosis and automation can spread credentials beyond the intended trust boundary | model sensitive values separately, redact by construction, minimize outputs, and test failure rendering | inject recognizable non-production canary values and scan bounded emitted surfaces without publishing real secrets | a tightly controlled forensic capture requires explicit authorization, access controls, retention, and deletion |
| telemetry_without_decision | new logs, metrics, traces, dashboards, or alerts lack a failure question, consumer, or response | cost and noise grow while diagnosis and recovery remain unchanged | add the smallest bounded signal that distinguishes a consequential state and maps to an owner action | inject that state, follow ingestion and query to alert or diagnosis, execute the runbook step, and test telemetry failure | temporary exploratory instrumentation is acceptable with scoped access, expiry, and no production-readiness claim |
| unbounded_signal_dimensions | request values, identifiers, stack text, or user-controlled data become metric labels or indexed fields | cardinality, cost, privacy exposure, and query instability can amplify the original incident | use bounded dimensions, sampled detail, correlation identifiers, and protected diagnostic stores | exercise adversarial and high-variety inputs; inspect series growth, redaction, retention, and degraded telemetry behavior | bounded tenant or operation dimensions may be approved when scale, privacy, and backend limits are measured |
| process_alive_as_readiness | a running process or open port reports ready before required startup and dependency conditions hold | automation sends traffic to a service unable to satisfy its accepted request contract | define readiness from target traffic semantics and only the dependencies necessary to serve safely | delay or fail each critical startup condition and observe readiness transition plus actual request behavior | a dependency-free service can use a simple readiness condition when its traffic contract truly requires no additional state |
| dependency_failure_as_liveness | liveness fails whenever a downstream system is slow or unavailable | platform restarts healthy instances, destroys diagnostic state, and amplifies a shared dependency incident | reserve liveness for local unrecoverable states; represent dependency degradation through readiness, status, or signals as policy requires | inject downstream latency and outage; observe restart count, traffic, recovery, and retained diagnosis | a locally wedged dependency client may justify liveness failure only when restart is the proven recovery action |
| empty_database_migration_confidence | migration succeeds only against a newly created local schema | historical values, production dialect, locks, constraints, and prior versions remain untested | exercise versioned migrations from supported prior states with representative data and the production dialect | include invalid legacy rows, scale-relevant data, mixed application versions, partial failure, and authorized recovery | an initial unreleased schema can use a fresh database if no prior data or deployed consumer exists |
| single_step_breaking_schema_change | application and schema remove or reinterpret an old contract in one release | rolling instances, jobs, replicas, and rollback paths observe incompatible states | separate expand, migrate or backfill, observe, switch, and contract stages where coexistence is required | run old and new versions against each intermediate state and verify data invariants plus stop conditions | a coordinated offline migration may be acceptable with proven exclusivity, bounded downtime, backup, and recovery authority |
| startup_coupled_unbounded_migration | every service instance performs long or contended schema work while starting | concurrent mutation, delayed readiness, liveness churn, and unclear ownership can block deployment | use the target's single-owner migration and rollout mechanism with explicit ordering, timeout, observability, and recovery | start multiple instances against a pending change; observe lock ownership, failure, retry, traffic, and final schema state | small idempotent initialization can occur at startup only when concurrency and recovery semantics are demonstrated |
| green_pipeline_wrong_claim | CI is green but did not run the changed boundary, production dialect, package, or platform mode | checkbox volume creates release confidence unrelated to the accepted runtime requirement | map each requirement to the earliest reliable gate and preserve later production-like evidence for boundaries that need it | deliberately break the changed behavior and confirm the intended stage fails on the same artifact | a later scheduled gate can own expensive evidence when release policy explicitly blocks or contains the intervening risk |
| rebuild_per_environment_promotion | source is rebuilt separately for each environment instead of promoting one identified artifact | dependencies, timestamps, inputs, or build hosts can change the bits under test | build once under controlled inputs and promote immutable identity with environment-specific validated config | compare digest and provenance from build through stage and production; reject substituted or rebuilt packages | platform-native source deployments need an equivalent immutable revision and reproducible build-attestation contract |
| permissive_container_by_default | image runs as root, exposes extra ports, carries unnecessary tools, or accepts broad write access without target need | compromise and operational mistakes gain a larger authority and attack surface | minimize deterministic runtime contents and grant only required user, files, ports, capabilities, and network access | inspect image and effective runtime identity; test read-only or restricted execution and required write paths | privileged behavior may be necessary for a specialized workload but requires explicit threat, platform, and owner review |
| rollout_without_stop_authority | release advances on elapsed time or optimistic health without named thresholds and an empowered owner | a partial failure can spread while teams debate who may stop, roll forward, or contain it | define stage, observation window, decision signals, stop conditions, authority, and recovery before traffic changes | inject a canary regression and exercise pause, containment, artifact selection, and recovery communication | very low-risk reversible internal changes may use simplified stages when consequence and authority are still explicit |
| shutdown_as_process_exit | termination closes the process without accounting for requests, transactions, workers, leases, acknowledgments, or external effects | work is lost, duplicated, stranded, or committed after ownership has moved | stop admission, propagate cancellation, drain bounded in-flight work, release resources, persist durable identity, and reconcile on restart | send termination during each work phase; observe deadlines, effects, acknowledgments, duplicates, restart, and backlog recovery | stateless request handlers with no external effects can use a simpler drain once that boundary is demonstrated |
| detached_background_coroutine | work escapes structured ownership into a process-global or untracked scope | cancellation, failure propagation, shutdown, and resource lifetime become ambiguous | give each task an explicit scope, supervisor policy, durable identity when needed, and observable completion contract | force parent cancellation, child failure, process termination, and restart; verify ownership and effect reconciliation | truly process-lifetime maintenance work may use an application scope with explicit lifecycle and failure policy |
| retry_without_effect_identity | a transient failure is retried without idempotency, deduplication, transaction, or reconciliation semantics | repeated calls can duplicate charges, messages, writes, notifications, or state transitions | classify the operation, bound retries under a total deadline, and add stable effect identity or compensating workflow | inject timeout before and after the external commit; retry and verify final state, duplicates, and operator recovery | read-only or provably idempotent operations may need only bounded backoff and cancellation |
| stacked_timeout_budget | independent client, coroutine, proxy, queue, and platform timeouts are chosen without one end-to-end budget | inner work continues after caller abandonment or outer deadlines fire before recovery can complete | derive nested deadlines from the accepted request or job budget and propagate cancellation across owned boundaries | exercise slow DNS, connection, response, processing, and shutdown phases; observe cancellation and resource release | independent asynchronous jobs may have separate budgets when ownership transfer and status are explicit |
| rollback_word_as_recovery | a route says rollback without accounting for schema, data, messages, caches, or external effects already changed | returning old code can deepen incompatibility or conceal partial irreversible state | choose rollback, roll-forward, repair, replay, or containment from the actual state transition and owner authority | rehearse the selected action after partial progress and verify invariants, compatibility, signals, and consumer state | code-only stateless releases with immutable prior artifacts may support straightforward rollback after smoke evidence |
| checklist_without_scenario | every review question is answered verbally but no failure or recovery transition is exercised | optimistic prose replaces evidence and leaves owners uncertain during a real event | convert high-consequence answers into target locators, executable scenarios, stop conditions, and runbook actions | sample a claimed control, induce its failure safely, and follow diagnosis through an accepted recovered state | low-consequence documentation decisions can remain review-only when no runtime claim depends on them |

**How to use the registry**

1. Preserve the target revision, artifact, effective config, data state, traffic state, timestamps, and bounded signals before changing a failing system.
2. Name the earliest state transition that no longer meets its contract. Use registry rows to generate hypotheses, not conclusions.
3. Select the row whose activation signal and causal mechanism fit the evidence. If none fits, keep the finding unclassified and investigate.
4. Check the exception column. A target convention is not unsafe merely because it resembles a compressed label.
5. Apply the safer replacement at the narrowest owned boundary. Avoid replacing one unverified fashion with another.
6. Run the discriminating scenario and observe whether the causal failure disappears without creating an adjacent failure.
7. Retain the result, residual limit, owner, runbook change, and event that invalidates the diagnosis.

**Good, bad, and conditional application**

Good: a worker loses jobs during termination. Evidence shows untracked process-local tasks and an acknowledgment after an external effect. The review uses `detached_background_coroutine`, `retry_without_effect_identity`, and `shutdown_as_process_exit` as hypotheses, then exercises cancellation at each phase and chooses durable ownership plus reconciliation from observed broker semantics.

Bad: a reviewer sees one raw config read in a framework adapter and rejects it as `deep_untyped_config_lookup` without noticing that the adapter validates once and injects a typed object. The label displaced the exception boundary and produced no runtime improvement.

Conditional: a deployment cannot reproduce provider termination behavior outside production. Package-level drain and cancellation tests can pass, while platform deadline and traffic claims remain conditional. The registry finding stays open for an authorized staged scenario instead of being marked resolved from local evidence.

**Registry quality and learning loop**

An entry is ready for shared enforcement when it has a stable causal description, a discriminating signal, at least one realistic counterexample, a safer route, an executable or review gate, an owner, and a recovery implication. Encode deterministic invariants in build, static, policy, or platform controls where doing so reduces noise. Keep contextual decisions in scenario-backed review.

After an incident or false positive, ask whether the entry found the earliest failure, whether its detector was precise, whether the replacement changed the causal mechanism, whether an exception was missing, and whether the runbook supported recovery. Version material changes. Retire an entry when the mechanism no longer exists, an automated invariant supersedes manual detection, or evidence shows the causal model was wrong. Preserve the reason so future reviewers do not reintroduce the same ambiguity.

## Verification Gate Command Set

`verification_gate_command_set`: The executable focused gate for this evolved reference is:

```bash
python3 tests/verify_idiomatic_reference_file.py \
  --path idiomatic-ref-202607/kotlin_backend_runtime_operations-20260710.md
```

That command verifies this reference's evolution contract. It does not build a Kotlin service, resolve a target's dependencies, start a package, migrate data, inspect an image, exercise platform health, drain work, or prove recovery. Runtime gates must be selected from the target repository and environment after discovery.

**Verification doctrine**

A gate is evidence for one bounded claim when all of the following are known:

- the requirement and failure it is intended to distinguish;
- the source revision, effective config, dependency graph, and artifact under test;
- the task or scenario definition, including filters and exclusions;
- the environment, fixture, identity, data state, traffic state, and external dependencies;
- the expected negative or degraded observation;
- the actual action, exit status, relevant output, and retained diagnostic artifacts;
- the stronger claim the gate does not establish;
- the owner and event that invalidate or require rerunning the result.

Command familiarity is not evidence. A broad `build` can omit integration, migration, image, or deployment behavior; a focused test can use the wrong engine or fixture; a platform smoke can pass while source-level regression coverage is absent. Map claims to gates before choosing commands.

**Safe preflight**

Before running a target command:

1. Read project and directory instructions, then inspect the working tree without reverting unrelated work.
2. Identify the checked-in wrapper and effective project/module. Do not substitute a globally installed Gradle, Maven, Kotlin, Java, linter, migration, container, or platform client without explicit target authority.
3. Inspect task definitions, CI invocation, profiles, test filters, skip flags, caches, environment variables, secret inputs, service dependencies, and output locations.
4. Determine whether the command writes a database, broker, filesystem, registry, cloud resource, shared cache, or deployment. Use isolated non-production state unless an accountable owner authorizes otherwise.
5. Record the source revision and intended artifact identity. Prevent a later stage from silently rebuilding different bits.
6. Preserve a reproduced failure or add a controlled negative case before implementation when the task changes a behavior or gate.
7. Bound time, output, credentials, cleanup, and cancellation. Never print real secret values to prove injection.
8. Run the narrowest discriminating gate, then expand only across affected boundaries and accepted claims.

**Target discovery patterns**

The following commands are candidates, not universal instructions. Use only the branch whose files and project guidance are present, and inspect output before selecting a task:

```bash
./gradlew projects
./gradlew tasks --all

./mvnw help:effective-pom
./mvnw help:active-profiles
```

Do not run Gradle and Maven merely because both examples appear here. Do not assume `check`, `test`, `build`, `verify`, static-analysis, migration, image, or integration tasks exist or include the same work across repositories. Locate the configured task and confirm its inputs and exclusions.

Useful target facts can also come from wrapper properties, build settings, version catalogs, dependency locks, resolved dependency reports, application config binding, migration directories, test source sets, container definitions, CI workflow files, deployment manifests, and runbooks. Read them with repository-native tools; avoid commands that mutate lockfiles or remote state during discovery.

**Claim-to-gate matrix**

| claim_under_test | earliest_useful_gate | expand_when | production_like_or_owner_gate | common_non_proof |
| --- | --- | --- | --- | --- |
| wrapper and version alignment | wrapper discovery, effective dependency and plugin resolution, compile | generated code, reflection, proxies, serialization, persistence construction, or bytecode changes | package startup on supported runtime and architecture | local compiler or IDE success |
| formatting and static policy | configured formatter, linter, and analysis task scoped to changed modules | shared rules, generated code, baseline, or CI task definition changes | CI invocation on clean source revision when enforcement is claimed | style pass as architecture or runtime proof |
| typed configuration | config binding and validation tests for valid, absent, malformed, boundary, and unknown values | framework startup, profile, dynamic source, secret provider, or packaged resource changes | packaged startup with representative non-secret environment and denied/missing secret scenarios | unit construction that bypasses the real binding path |
| secret handling | redaction tests, output serialization review, denied-access and missing-secret startup | identity, rotation, audit, provider, or incident-containment behavior changes | authorized provider integration and exposure-recovery drill | presence in an environment variable or secret store alone |
| environment profiles | effective config comparison and startup scenarios for supported profiles | package resources, platform injection, feature contracts, or adapter selection changes | deployed configuration inspection under target access controls | branching on an environment label without behavior tests |
| request and client behavior | unit plus framework test for contract, timeout, cancellation, error mapping, and propagation | real serialization, network, TLS, proxy, driver, or downstream semantics matter | isolated real dependency or controlled sandbox scenario | mocked success that cannot represent timeout or partial effect |
| coroutine and worker lifecycle | virtual-time or deterministic coroutine tests plus structured ownership assertions | blocking adapters, broker acknowledgment, leases, external effects, or application scope changes | packaged termination, drain, restart, duplicate, and reconciliation scenario | child completion in a test that never cancels the parent |
| persistence transaction | repository integration against the supported driver and dialect | isolation, concurrency, lock, retry, generated SQL, or pool behavior changes | representative load and failure scenario in an approved environment | in-memory substitute with different transaction semantics |
| schema migration | migrate from every supported prior version with representative historical data | constraints, indexes, backfills, large tables, dialect, or tool version changes | mixed application versions, partial failure, rollout stop, and authorized recovery | successful migration of an empty database |
| observability | deterministic signal shape and redaction checks under success, failure, and cancellation | exporter, collector, sampling, propagation, cardinality, dashboard, or alert changes | inject failure through ingestion and query to owner action; exercise telemetry degradation | log line presence without semantics, privacy, consumer, or action |
| health and traffic | framework health-state tests plus actual request behavior during startup and dependency failure | platform probes, startup windows, traffic policy, restart policy, or graceful drain changes | staged platform scenario observing readiness, liveness, traffic, restart, and recovery | process alive, open port, or endpoint status in isolation |
| package and image | reproducible package task, dependency contents, startup smoke, image inspection, effective user, files, and ports | base image, architecture, native library, resources, certificate, or filesystem changes | platform start under target identity, resources, network, and termination policy | local JVM run or image build exit status alone |
| CI and immutable promotion | inspect workflow, run changed tasks, trace revision to output artifact and digest | runner, cache, matrix, permission, secret, environment, or release definition changes | promote the same digest through a controlled stage and preserve failures | green stage that rebuilt, skipped, or tested another artifact |
| staged rollout | deterministic regression plus release-condition tests where possible | traffic policy, schema, dependency, objective, or rollback and roll-forward choice changes | authorized canary with bounded observation, stop authority, and recovery action | elapsed time or aggregate green dashboard without causal signals |
| shutdown and recovery | cancellation, drain, deadline, resource-release, and restart tests | requests, transactions, queues, jobs, leases, acknowledgments, or external effects are involved | terminate the packaged deployment in each consequential work phase and reconcile final state | clean process exit without checking work and effects |

**Conditional wrapper task families**

After task discovery, a Gradle target may expose combinations such as:

```bash
./gradlew <configured-format-or-analysis-task>
./gradlew <focused-test-task> --tests '<fully.qualified.TestName>'
./gradlew <configured-integration-task>
./gradlew <configured-build-or-package-task>
```

A Maven target may instead expose lifecycle or plugin goals through its wrapper:

```bash
./mvnw -Dtest='<TestName>' test
./mvnw <configured-verification-phase>
./mvnw <configured-package-phase>
```

Angle-bracket terms describe values to discover from the target; they are not literal commands to execute. Preserve repository quoting and module-selection conventions. Confirm that a filtered invocation actually selects a test and that a broad invocation does not silently skip integration work through profiles or properties.

For both build systems, capture the wrapper version, JVM, effective project, resolved relevant dependency versions, task selection, cache behavior, and produced artifact. A cached pass is acceptable only when cache inputs cover the changed source, config, dependency, toolchain, fixture, and environment assumptions.

**Atomic verification sequence**

1. **Requirement map:** write the normal, failure, degraded, shutdown, and recovery states accepted for this change.
2. **Gate discovery:** locate configured target tasks and operational mechanisms; note missing or inaccessible boundaries.
3. **Negative control:** preserve the current failure or introduce a safe defect that the new or changed gate must detect.
4. **Narrow deterministic run:** execute the smallest gate; verify expected failure before implementation and expected pass after it.
5. **Affected deterministic expansion:** run relevant compile, static, unit, framework, contract, and module gates, not an arbitrary full suite.
6. **Stateful integration:** use isolated production-dialect data, broker, external-service, clock, and concurrency behavior when the claim depends on them.
7. **Artifact verification:** package once, identify it, inspect it, and start that artifact with representative configuration and restricted permissions.
8. **Lifecycle verification:** exercise health, traffic, degraded dependencies, signal delivery, termination, restart, and recovery as activated.
9. **Release verification:** prove CI executes the mapped gates and promotes the intended immutable artifact with bounded permissions and retained results.
10. **Evidence retention:** save commands, versions, environment, fixtures, artifact identity, results, limitations, owners, and invalidation events.

**Operational examples**

Config change: a new external-client timeout begins with binding tests for missing, malformed, minimum, maximum, and valid values. The packaged application then starts with representative config, and a controlled slow dependency shows the timeout, cancellation, error mapping, bounded signal, and absence of secret output. A unit test of the settings data class alone is insufficient.

Migration change: the gate creates supported prior schemas and representative historical rows, runs the target migration tool against the production dialect, starts old and new application versions in permitted sequences, induces partial failure, observes locks and signals, and exercises the authorized roll-forward or repair route. An empty ephemeral database proves syntax only.

Image change: the route builds the configured package, records image inputs and digest, inspects effective user, ports, files, and entrypoint, runs with target-like config and resources, then observes startup, readiness, request handling, signal termination, drain, and restart. A successful image build does not prove any of those states.

Worker change: deterministic tests cover scope ownership, cancellation, deadline, and local state. A broker or store scenario then interrupts work before and after the external effect and acknowledgment, restarts the package, and checks duplicates, leases, backlog, and reconciliation. A clean coroutine test with no durable effect supports only the local ownership claim.

Conditional platform result: local gates and package smoke may pass while managed identity, traffic, health, or termination behavior remains inaccessible. Report the passed subset and block only the release claim that depends on the missing authorized scenario. Do not turn lack of access into either a fabricated pass or a claim that all implementation work failed.

**Gate qualification record**

```text
requirement_id:
claim_and_failure_class:
target_revision:
effective_versions_and_profiles:
gate_owner:
gate_definition_locator:
command_or_scenario:
selection_filters_and_exclusions:
environment_and_identity:
fixture_or_prior_state:
source_artifact_digest:
expected_negative_observation:
negative_control_result:
implementation_result:
recovery_result:
retained_output_locator:
stronger_claim_not_proved:
residual_risk_and_owner:
rerun_or_invalidation_event:
```

Qualify a new or materially changed gate by showing that it fails for its intended defect class. Later routine runs need not reintroduce the defect each time, but task-definition changes, unexplained pass-rate shifts, cache changes, or incidents should trigger requalification.

**Result interpretation**

- Report `pass` only for an action that completed successfully and observed its asserted state.
- Report `expected failure observed` when a negative control failed for the intended reason.
- Report `failed` with the earliest causal evidence rather than burying it under later cascading failures.
- Report `not run` when a gate was irrelevant, unavailable, unsafe, or deferred; state the reason and affected claim.
- Report `conditional` when available evidence supports a subset but an environment, owner, or recovery boundary remains unproved.
- Report `inconclusive` when flakiness, fixture drift, contamination, timeout, or telemetry loss prevents interpretation. Fix or isolate the evidence system before granting release authority.

Never run destructive migration, secret rotation, traffic mutation, production fault injection, deployment, or recovery commands merely because a reference lists their scenario. Those actions require target-specific procedure, access control, blast-radius review, accountable authorization, evidence preservation, and a stop plan.

Gate maintenance is part of runtime correctness. When tasks, dependencies, fixtures, artifacts, environments, or platform mechanisms change, invalidate only the results that depend on them and rerun the mapped graph. Retire redundant gates when a stronger deterministic control subsumes them, but preserve coverage and diagnosis. A well-maintained gate map accelerates both release decisions and incident localization because it shows which lifecycle transition each piece of evidence can actually distinguish.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference as the lead when the accepted outcome changes how a Kotlin backend is built, configured, observed, migrated, packaged, verified, released, admitted to traffic, terminated, or recovered. Use it as support when another domain owns the primary behavior but one of those lifecycle transitions also changes. Route away when runtime vocabulary is incidental, another owner controls the decision, or no Kotlin backend artifact or operational contract is in scope.

A theme mention is only a candidate activation signal. Before applying guidance, establish:

1. What normal, degraded, failed, shutdown, and recovered outcome is accepted?
2. Which repository, service, module, artifact, environment, users, and operators are affected?
3. What does the target already use for wrapper, versions, framework, configuration, secrets, telemetry, persistence, migration, package, CI, platform, traffic, shutdown, and runbooks?
4. Which state transition changes, and which adjacent transitions must remain stable?
5. Who owns application behavior, data, security, platform policy, release authority, and incident action?
6. What consequence, reversibility, uncertainty, and evidence access shape the route?
7. Which source region can resolve the next named uncertainty without loading unrelated doctrine?
8. What observation would cause a reroute, split, stop, or escalation?

**Route modes**

| route_mode | choose_when | first_action | expected_output | stop_or_handoff_condition |
| --- | --- | --- | --- | --- |
| runtime_lead | the primary accepted change is a build, config, secret, profile, signal, migration, package, CI, health, rollout, shutdown, or recovery behavior of a Kotlin backend | inspect target stance and trace the affected lifecycle from source to recovery | bounded runtime requirements, mechanism decision, gate map, evidence, limitations, and owner handoff | accepted states are observed or the unresolved decision moves to a named domain owner |
| runtime_support | endpoint, domain, framework, security, persistence, testing, or platform work leads, but its packaged or operational behavior changes | identify only the activated runtime transitions and compose the specialist reference | runtime constraints and gates attached to the lead domain's acceptance criteria | supporting transitions are reconciled without duplicating the lead design |
| incident_first | config, exposure, migration, health, artifact, traffic, shutdown, or recovery is already failing | preserve evidence, contain under authority, and start at the earliest observed break | incident-scoped state model, containment evidence, recovery decision, and regression route | immediate risk is controlled and upstream/downstream lifecycle corrections have owners |
| review_only | the request is a readiness, architecture, policy, or risk review with no accepted implementation yet | build a target evidence map and classify findings by consequence and confidence | findings, counterexamples, missing evidence, options, and decision owners | review questions become accepted work, rejected findings, or explicitly retained risks |
| exploratory | no target exists or a deliberate upgrade/platform option comparison is accepted | state hypotheses, candidate mechanisms, decision criteria, and experiment limits | option comparison and executable spikes labeled as non-target evidence | an option is selected, the question is answered, or the exploration budget is exhausted |
| route_away | another domain owns the causal behavior and no runtime transition changes | name the correct lead and preserve any narrow runtime interface question | concise handoff with reason, target facts, and unresolved interface | receiving route accepts ownership or new evidence activates runtime behavior |
| stop_and_escalate | action requires unavailable authority, unsafe production mutation, secret access, destructive data change, or unsupported risk acceptance | preserve evidence and identify the accountable owner and decision needed | blocker, consequence, safest available evidence, and exact authorization request | owner supplies policy, access, decision, or an alternate safe route |

**Strong lead signals**

| accepted_change_signal | runtime_regions_to_open_first | likely_companions | decisive_target_evidence |
| --- | --- | --- | --- |
| wrapper, Kotlin, Java, dependency, compiler plugin, or package changes | Build And Dependency Discipline; Static Analysis And Formatting if gates change | framework idioms; testing; security when supply chain or permissions change | wrapper and effective versions, configured tasks, compile/package result, artifact identity, startup behavior |
| configuration key, default, profile, credential, or secret-provider changes | Configuration And Secrets; Profiles And Environments | framework Configuration; Trust Boundaries; Input Validation; testing fixtures | binding path, valid and invalid startup, effective profile, denied secret access, redacted outputs |
| log, metric, trace, correlation, health, dashboard, or alert changes | Observability; Container And Deployment Safety when automation consumes health | security and resilience; external clients and workers; target telemetry and platform policy | induced failure, bounded signal, privacy and cardinality, ingestion, consumer action, telemetry degradation |
| schema, constraint, index, backfill, transaction, or database-version changes | Database Migrations; CI Expectations | persistence and transaction playbook; persistence tests; security when data sensitivity changes | production dialect, prior states, historical data, mixed versions, partial failure, rollout and recovery |
| image, runtime user, port, resource, architecture, startup, or deployment changes | Build And Dependency Discipline; Container And Deployment Safety | configuration, security, testing, target platform runbook | source-to-digest lineage, package smoke, effective permissions, resources, health, traffic, termination |
| CI task, cache, runner, artifact, promotion, environment, or release changes | CI Expectations plus every changed boundary the pipeline claims to gate | testing; security; migration; platform policy | deliberate gate failure, clean execution, permissions, retained output, immutable promotion, staged recovery |
| coroutine scope, worker, queue, lease, acknowledgment, retry, or restart changes | Container And Deployment Safety; Observability; Operational Review Questions | playbook External Clients And Workers; resilience Background Work, Idempotency, Retries, Coroutine Resilience | ownership, cancellation, deadline, effect identity, drain, restart, duplicates, backlog, reconciliation |
| canary, readiness, liveness, traffic, termination, or runbook changes | Container And Deployment Safety; Observability; Operational Review Questions | target platform authority; security; testing; incident process | induced degraded state, platform automation, stop authority, traffic result, shutdown, accepted recovery |

**Supporting and route-away boundaries**

| primary_task | appropriate_lead | runtime_reference_role | route_away_or_escalation_boundary |
| --- | --- | --- | --- |
| pure Kotlin types, nullability, collections, or API design | language or application-design guidance | support only if serialization, config, artifact, or runtime lifecycle changes | route away when no deployed behavior or operational contract changes |
| endpoint, domain rule, DTO, error, transaction, or client design | Kotlin backend playbook or framework idioms | add config, signal, package, and release gates activated by the behavior | do not let operations guidance redefine product semantics or API acceptance |
| authentication, authorization, input trust, token, retry, idempotency, or threat work | security and resilience guidance plus target policy | cover secret injection, audit signals, package identity, release, and recovery interfaces | escalate risk acceptance, identity policy, incident containment, and credential authority to owners |
| test architecture, fixture, coroutine scheduler, framework slice, or property testing | testing and fixtures guidance | ensure gates map to artifact and production-like lifecycle claims | do not prescribe target test tools solely from this runtime reference |
| framework selection, Spring bean or proxy behavior, Ktor plugin or engine behavior | framework idioms and accepted architecture decision | map the selected mechanism to config, package, health, shutdown, and release evidence | route framework switching and compatibility decisions to their owners and current authority |
| cloud account, cluster, network, secret service, database service, CI provider, or traffic policy administration | target platform runbook, policy, and provider authority | state application-side inputs, signals, health, artifact, and recovery requirements | stop before mutating shared or production resources without authorized procedure and access |
| frontend, mobile, desktop, data-science, or unrelated service work | the relevant domain guidance | none unless a Kotlin backend operational interface genuinely changes | a shared word such as build, config, or deploy is not sufficient activation |
| provider outage or organization-wide incident | incident command and accountable platform owner | contribute service evidence and recovery constraints | do not independently choose cross-system containment, failover, or risk acceptance |

**Default routing sequence**

1. **Clarify the outcome.** Replace requests such as "productionize it" or "improve observability" with accepted states, failures, users, operators, and owner decisions.
2. **Inspect before prescribing.** Read target instructions, wrapper, effective dependencies, config, migrations, telemetry, package, pipeline, deployment, and runbooks relevant to the outcome.
3. **Classify the route.** Choose lead, support, incident-first, review-only, exploratory, route-away, or stop-and-escalate. Record why.
4. **Open the smallest source region.** Use the Local Corpus Source Map and expand only at activated framework, testing, security, data, platform, or recovery boundaries.
5. **Preserve the stance.** Do not switch wrapper, framework, compiler plugins, migration tool, telemetry, image, CI, or platform unless that decision is accepted separately.
6. **Write lifecycle contracts.** Map source to artifact, config to startup, data to mixed versions, signal to action, release to traffic, termination to recovery, and incident to learning.
7. **Choose evidence before implementation.** Qualify deterministic and production-like gates, including a negative or degraded path.
8. **Act at the owned boundary.** Keep implementation and operational scope proportional to the accepted outcome and authority.
9. **Reassess during evidence.** Split or reroute when a new owner, state transition, security boundary, platform override, or recovery requirement appears.
10. **Retain the handoff.** Save route rationale, selected regions, target facts, actions, results, limitations, residual owners, and invalidation events.

**Incident override**

When a service is already unsafe or unavailable, do not delay containment to complete the normal read order. Preserve the failing revision, artifact, config, data, environment, traffic, timestamps, and bounded signals. Start at the earliest supported causal break:

- missing or malformed startup input routes to configuration;
- credential disclosure routes to secret containment and security ownership;
- data incompatibility routes to migration state and recovery authority;
- silent or indistinguishable failure routes to observability and direct target evidence;
- false readiness or restart amplification routes to health and platform traffic policy;
- wrong artifact routes to build, pipeline, and immutable promotion;
- lost or duplicated work routes to scope ownership, effect identity, shutdown, restart, and reconciliation.

After containment, restore the upstream gate and downstream regression and runbook route. An incident-first route is not permission to leave the normal delivery path capable of recreating the failure.

**Good routing examples**

Config lead: a Kotlin service adds a required outbound-client timeout. Runtime operations leads configuration and packaged-startup behavior; framework idioms supports binding; testing supplies valid, absent, malformed, and boundary fixtures; resilience owns total deadline and cancellation. The route does not introduce a new framework or telemetry stack.

Migration composition: a domain change requires a uniqueness constraint. Domain and persistence design lead the invariant and transaction behavior; runtime operations leads versioned migration, historical data, mixed versions, CI, staged rollout, signals, and recovery. Neither route claims the other boundary from prose alone.

Worker incident: jobs duplicate after termination. Incident-first handling preserves broker and effect evidence. Security and resilience leads idempotency and retry semantics; runtime operations leads application scope, signal, termination, restart, artifact, rollout, and recovery gates. Platform owners supply the actual grace and traffic policy.

Route away: a request asks how to model a sealed result type in a library that is not packaged or deployed as a service. Kotlin language guidance leads; this runtime reference adds no useful state transition and should not be loaded merely because the code may later be used on a server.

Conditional route: image startup and local drain are verified, but managed identity and platform termination cannot be exercised. Runtime operations remains the correct lead, yet deployment readiness is conditional and handed to an authorized platform scenario. Available implementation evidence is retained instead of being discarded or inflated.

Borderline route: latency increased after a framework upgrade and could arise from coroutine dispatch, database pool behavior, telemetry export, or platform resource policy. Preserve all four hypotheses; gather resolved versions, traces, pool and resource state, and a controlled workload. Let the earliest discriminating observation choose the specialist lead rather than committing from the symptom word `latency`.

**Route hygiene**

- Do not activate every region because a request says `production`, `backend`, or `deploy`.
- Do not add a new tool merely because the reference names its category; discover the target's established mechanism.
- Do not let a runtime route absorb product, framework, security, database, or platform policy decisions whose owners have not accepted them.
- Do not execute production mutations, destructive migrations, secret operations, traffic changes, or recovery actions from generic guidance.
- Do not duplicate a companion reference. State the interface question and hand off the primary design.
- Do not treat inaccessible evidence as success. Preserve conditional claims and exact authorization needs.
- Do not continue gathering context after the decision question is answered and the changed transitions have sufficient evidence.
- Do not retain stale route conventions after target architecture, platform ownership, or incidents invalidate them.

**Route decision record**

```text
request_and_accepted_outcome:
target_revision_and_artifact:
candidate_runtime_signals:
changed_lifecycle_transitions:
unchanged_boundaries:
route_mode:
lead_domain_and_owner:
supporting_domains_and_owners:
selected_local_regions:
external_refresh_needed:
target_facts_used:
requirements_and_failure_scenarios:
verification_actions_and_results:
production_or_authority_limits:
route_away_or_stop_reason:
reroute_trigger:
handoff_recipient:
invalidation_event:
```

Persist this record for implementation, shared guidance, production change, incident, or cross-owner handoff. A low-risk explanation can use a lighter record, but should still state why this reference is relevant and which stronger claims remain outside scope.

Evaluate route quality by evidence yield: did the selected regions expose the changed state, counterexample, gate, owner, and recovery boundary with less irrelevant context? Record misroutes and recurring compositions. Promote a stable route convention only after representative evidence, and retain overrides for incidents and architecture change. The guide should become concise where platform ownership and gates are stable, while remaining explicit at boundaries that repeatedly change or fail.

## User Journey Scenario

`role_based_opening_scenario`: A Kotlin backend engineer owns an existing asynchronous worker. During a rolling deployment, termination sometimes leaves a job unaccounted for; after restart, another job can repeat an external effect. The team has a build wrapper, a framework-managed application, a broker or durable work store, a database, CI, a packaged runtime, and a deployment platform, but this reference does not assume which products provide them.

`primary_user_starting_state`: The engineer has a target revision, one or more failure reports, and access to local tests. The precise moment of work ownership, external commit, durable completion, acknowledgment, termination deadline, restart behavior, and platform traffic policy is uncertain. Existing dashboards show process and queue symptoms but do not prove final business state.

`decision_being_made`: Choose the smallest target-compatible ownership, cancellation, effect-identity, drain, restart, and reconciliation design that prevents silent loss and bounds duplicates without replacing the framework, broker, database, telemetry, CI, or platform by fashion.

`reference_opening_trigger`: Use this journey when asynchronous requests, jobs, leases, queue messages, scheduled work, external effects, rolling termination, or restart correctness are the accepted runtime concern. Reduce it for genuinely stateless work. Route application semantics, security policy, broker administration, and platform mutation to their owners.

The scenario is illustrative. Every named mechanism must be replaced by discovered target behavior, and any inaccessible provider or production state remains conditional.

**Journey state model**

Before choosing code, enumerate the phases that actually exist:

| phase | ownership_question | interruption_hazard | required_observation |
| --- | --- | --- | --- |
| available | which system owns work before the application receives it? | duplicate delivery, stale lease, or missing visibility already exists | source identifier, availability state, attempt history, and provider semantics |
| acquired | what event transfers temporary or durable ownership to this process? | process dies after acquisition but before durable intent | lease or acknowledgment state, owner identity, expiry, and redelivery behavior |
| admitted | does shutdown stop new work before draining accepted work? | new work enters while readiness or intake is closing | admission state, readiness, intake pause, and accepted work count |
| processing | which coroutine or worker scope owns cancellation and child failure? | detached or blocking work outlives its owner | scope hierarchy, dispatcher, cancellation signal, deadline, and resource state |
| effect_prepared | is an external write, message, charge, file, or notification about to occur? | retry cannot distinguish attempted from committed | stable work and effect identity, transaction boundary, and intent state |
| effect_committed | can the effect commit while the application sees timeout or cancellation? | retry duplicates an already committed effect | provider response, idempotency key or reconciliation key, and target final state |
| completion_recorded | where is durable application completion stored? | effect exists but completion record is absent or inconsistent | durable state transition, transaction result, version, and correlation identity |
| acknowledged | when is source work removed or marked complete? | early acknowledgment loses work; late acknowledgment redelivers it | acknowledgment or lease transition, ordering, and retry semantics |
| draining | what work is allowed to finish after admission stops? | fixed delay expires without knowing what remains | in-flight identities, phase, remaining budget, and stop or handoff decision |
| terminated | what happens at graceful deadline or forced kill? | locks, leases, resources, or partial effects remain ambiguous | termination reason, unfinished work, released resources, and retained evidence |
| restarted | how are expired, pending, duplicate, or partial attempts found? | work is ignored or replayed blindly | startup reconciliation, redelivery, deduplication, and backlog state |
| recovered | who decides that final business state is acceptable? | process health returns while customer or data state remains wrong | invariant check, residual repair, signals, owner sign-off, and runbook result |

Delete phases that truly cannot occur; add target-specific phases such as transaction commit, object upload, downstream callback, outbox publish, or lease extension. The critical question is where ownership or externally visible state changes, not how many coroutine functions exist.

**Step 1: Preserve and bound the failure**

Capture the target revision, package or image identity, effective non-secret config, environment, instance, deployment event, termination signal and deadline, work identifiers, broker or store state, database rows, external effect identifiers, timestamps, correlation data, and bounded logs or traces. Redact sensitive values and follow incident access policy.

State the strongest supported symptom, such as: "For two observed termination windows, the application stopped after an external request but before a durable completion record; one source item was later redelivered." Do not convert that into "coroutines lose jobs" until scope ownership and provider state support it.

If production risk is active, contain under accountable authority. Possible target-owned actions include pausing a rollout, stopping new intake, extending a safe grace period, or starting reconciliation. This generic reference does not authorize any of them.

**Step 2: Inspect target stance**

Read project instructions and locate:

- repository wrapper, effective Kotlin and Java versions, framework, coroutine library, relevant compiler plugins, and configured verification tasks;
- worker entry point, application scope, child scope or supervisor policy, dispatchers, blocking adapters, timeout and retry composition;
- source-work acquisition, lease, visibility, acknowledgment, retry, dead-letter, and redelivery semantics;
- transaction boundaries, durable work and effect identifiers, completion records, and external-client idempotency or reconciliation support;
- typed configuration, secret injection, startup validation, environment profiles, and shutdown settings;
- structured logs, metrics, traces, health, backlog, attempt, failure, drain, and reconciliation signals plus their consumers;
- package or image definition, runtime identity, resources, readiness, liveness, termination deadline, and restart policy;
- CI tasks, artifact promotion, staged release controls, stop authority, runbook, and incident owner.

Preserve these choices unless a separate accepted decision changes one. A shutdown defect is not permission to migrate framework, broker, telemetry, build system, or deployment platform.

**Step 3: Split ownership across domains**

Runtime operations leads package lifecycle, config, signals, health, deployment, drain, restart, and recovery evidence. Security and resilience guidance leads idempotency, retry, timeout, trust, and external-effect safety. The application playbook leads worker and transaction boundaries. Framework guidance owns application lifecycle integration. Testing guidance owns fixture and gate design. Broker, database, and platform owners supply authoritative operational semantics and permissions.

Record disagreements instead of blending them. For example, a coroutine may be cancellable while a blocking driver call is not; an application may stop intake while a broker lease continues; a process may exit cleanly while an external effect remains ambiguous.

**Step 4: Write executable outcome contracts**

Adapt these contracts to target semantics:

- **Admission:** when termination begins, the worker stops acquiring new work before reporting drain complete.
- **Ownership:** every admitted work item has one durable identity and a discoverable owner or recoverable source state.
- **Cancellation:** termination reaches owned coroutine work and bounded blocking adapters within the configured deadline path.
- **Effect safety:** a retry after timeout or restart cannot silently repeat an effect beyond the accepted policy; ambiguous effects enter reconciliation.
- **Acknowledgment:** source completion occurs only after the durable state required by the target contract.
- **Drain:** work that can safely finish does so within a bounded budget; remaining work reaches an explicit retry, release, handoff, or reconciliation state.
- **Resource release:** connections, leases, locks, executors, files, and telemetry flush are released or intentionally transferred.
- **Restart:** expired, pending, duplicate, and partial attempts are detected and resolved without manual guesswork.
- **Signals:** operators can distinguish normal drain, deadline expiry, cancellation failure, duplicate suppression, unresolved ambiguity, and recovery.
- **Recovery:** a named owner can determine final business state and execute the authorized repair or replay route.

Do not attach arbitrary latency or success percentages. Derive deadlines, throughput, duplicate tolerance, retention, and alert thresholds from workload, platform limits, product consequence, and measured baseline.

**Step 5: Compare ownership and recovery alternatives**

| option | choose_when | main benefit | primary cost_or_risk | decisive_evidence |
| --- | --- | --- | --- | --- |
| finish synchronously before response or acknowledgment | work is bounded and caller or source can safely wait | simplest ownership and final-state reasoning | increases latency and couples availability to downstream work | end-to-end deadline, cancellation, effect, and failure behavior under representative load |
| bounded in-process drain | admitted work is short, recoverable, and platform grace is sufficient | small change preserving current architecture | forced kill still creates ambiguity without durable identity | termination at every phase, deadline pressure, resource release, and restart state |
| broker or durable-store ownership | work must survive process lifetime and target infrastructure supports redelivery | durable handoff and scalable workers | duplicate delivery, lease, acknowledgment, and backlog operations become first-class | exact source semantics, effect identity, redelivery, dead-letter, restart, and reconciliation tests |
| transactional intent or outbox style | durable state and emitted work must change atomically within supported storage semantics | closes a common commit-and-publish gap | adds relay, schema, cleanup, lag, and operational ownership | transaction atomicity, relay retries, ordering, duplicates, backlog signals, and recovery |
| idempotency plus reconciliation | external effects may commit ambiguously but expose stable keys or queryable state | bounds duplicate effects and enables repair | state retention, collision, provider, and operator complexity | timeout before and after commit, repeated attempt, lookup, final-state invariant, and repair |
| temporary operational containment | immediate risk is high and durable design needs more evidence | reduces near-term exposure | manual burden and hidden permanence if not retired | owner approval, bounded duration, signal, rollback or exit condition, and tracked replacement |

The right answer can combine options. For example, durable source ownership plus idempotent external effect and restart reconciliation may be necessary. Avoid selecting a complex pattern merely because it is recognizable; prove the target's actual gap.

**Step 6: Design failure-first verification**

Build a phase-interruption matrix before implementation:

| injected_or_observed_point | expected_owned_state | expected_restart_behavior | unacceptable_result |
| --- | --- | --- | --- |
| before acquisition | source retains work | later delivery is normal | application records completion without ownership |
| after acquisition, before processing | lease or durable intent identifies attempt | retry or resume follows target policy | item disappears when the process exits |
| during cancellable processing | parent cancellation reaches child | source or durable state makes next action explicit | detached work continues with no owner |
| during blocking call | deadline and adapter policy bound the call | unresolved attempt is discoverable | shutdown hangs indefinitely or effect commits invisibly |
| immediately before external effect | no final effect is assumed | retry can proceed under stable identity | completion is recorded before effect contract allows it |
| response lost after effect commit | attempt is marked ambiguous or queryable | reconciliation finds committed state before repeating | blind retry duplicates an irreversible effect |
| after completion record, before acknowledgment | durable completion is authoritative | redelivery is suppressed or reconciled | repeated effect occurs because source redelivered |
| during drain deadline | unfinished identities and phases are retained | restart or source recovery owns them | process reports graceful completion while state is unknown |
| after restart | pending and expired attempts are scanned or redelivered | each reaches complete, retry, repair, or quarantined state | backlog appears healthy while business state remains partial |

Use deterministic coroutine and state-machine tests for ownership and cancellation. Add isolated real broker, database, and external-client behavior when their semantics matter. Package the application and send the same termination signal used by the target. Exercise the platform in an authorized staged environment when traffic, grace, identity, or restart policy is part of the claim.

**Step 7: Implement the narrow correction**

A target-compatible correction might:

- move worker children under the framework-owned application scope;
- stop intake before drain and expose a bounded drain state;
- give each work item and external effect a stable durable identity;
- order completion and acknowledgment according to target transaction and source semantics;
- propagate one total deadline and cancellation through owned adapters;
- classify retriable, permanent, ambiguous, and reconciliation-required outcomes;
- persist enough state for restart without logging sensitive payloads;
- emit bounded signals for acquired, active, completed, retried, duplicate-suppressed, ambiguous, drain-expired, and recovered states;
- add startup reconciliation or an owner-operated repair path only where target evidence requires it.

Do not add every mechanism at once. If the observed failure is solely detached scope ownership and work has no external effect, structured lifecycle and termination evidence may be sufficient. If external commit ambiguity exists, a graceful delay alone is not sufficient.

**Step 8: Qualify the artifact and pipeline**

Run repository-native compile, configured analysis, focused tests, affected integration, package, and migration gates as activated. Preserve expected failure evidence, then pass after implementation. Build the intended package once, identify it, and show CI executes the mapped gates and promotes that artifact rather than rebuilding per environment.

Start the package with representative typed config and restricted identity. Verify missing and malformed config fails safely, secrets remain redacted, signals initialize, source dependencies are unavailable or slow as scenarios require, and readiness remains false until accepted traffic behavior is possible.

**Step 9: Stage termination and restart**

Under an authorized bounded rollout:

1. establish baseline throughput, backlog, failure, duplicate, resource, and signal behavior;
2. admit known test work with non-sensitive identifiers;
3. terminate instances at each consequential phase;
4. observe readiness or intake closure, cancellation, drain, deadline, acknowledgment, leases, external effects, and resource release;
5. restart the same artifact and verify redelivery, duplicate suppression, reconciliation, final state, and backlog recovery;
6. exercise stop or recovery authority when a defined condition fails;
7. retain exact artifact, config revision, platform state, action, result, and limitation.

Do not perform destructive or production fault injection from this generic scenario. Use target procedure, isolated fixtures, and accountable authorization.

**Step 10: Close the user journey**

The journey is complete when:

- the accepted normal, interrupted, deadline, restart, and recovered states are observed at the required fidelity;
- no work phase lacks an owner or discoverable recovery route;
- duplicate and ambiguous effects meet an explicit product and owner policy;
- signals distinguish failures and lead to an exercised action without sensitive or unbounded data;
- CI and release evidence refer to the promoted artifact;
- runbook steps, stop authority, residual risks, and unavailable environments are explicit;
- temporary containment has an owner and retirement condition;
- source, target, and external evidence boundaries are preserved.

Good outcome: interruption after external commit is reproduced, stable effect identity lets reconciliation discover the committed result, source redelivery does not repeat the effect, and the staged package drains or records remaining work before restart. The report states exactly which provider and workload ranges were exercised.

Bad outcome: the team adds a fixed sleep in shutdown, sees a clean local exit once, marks the worker production-safe, and leaves acknowledgment, external commit ambiguity, platform grace, duplicate handling, restart, signals, and owner recovery unexamined.

Conditional outcome: deterministic ownership, real database and broker integration, package termination, and restart reconciliation pass, but managed-platform grace and traffic cannot be exercised. Implementation can be ready for platform qualification; deployment safety remains conditional with a named owner and scenario.

**Second-order learning**

After delivery, review whether the incident exposed a missing target contract, an unqualified gate, a false health state, a noisy signal, an ownership gap, or an outdated runbook. Feed the smallest durable correction into CI, platform policy, monitoring, or reference routing. Watch whether added reconciliation or signal paths create retention, privacy, cardinality, capacity, or support costs. Remove temporary containment after its exit evidence passes.

The successful journey leaves a simpler ownership story: for every work item, an operator can determine who owns it, whether its effect occurred, what happens on retry, how termination changes state, and how the system reaches an accepted recovered condition. More dashboards or tests without that clarity are not completion.

## Decision Tradeoff Guide

`decision_tradeoff_default`: Preserve the target's established wrapper, versions, framework, compiler plugins, config mechanism, migration tool, telemetry, package, CI, and platform when they satisfy the accepted runtime outcome. Adapt or replace one mechanism only when a named gap, consequence, target-compatible alternative, owner, transition plan, evidence, and recovery justify the additional change.

This presumption minimizes simultaneous change dimensions; it does not make the status quo correct. An unsupported release, recurring incident, incompatible contract, exposed secret, false health state, unsafe migration, substituted artifact, or unrecoverable shutdown can override preservation immediately within accountable authority.

**Decision modes**

| decision_mode | choose_when | main_value | principal_cost_or_risk | evidence_needed_before_commitment | exit_or_reassessment_condition |
| --- | --- | --- | --- | --- | --- |
| preserve | the current mechanism meets the new contract and has owned gates, operations, and recovery | smallest blast radius and reuse of target knowledge | hidden drift or untested states may be mistaken for maturity | requalify the changed boundary, artifact, and failure scenario | target evidence fails, support status changes, or owner policy changes |
| adapt_in_place | the mechanism is sound but one bounded behavior, config, signal, gate, or lifecycle hook is missing | retains ecosystem fit while closing a specific gap | local customization can diverge from supported paths and add maintenance | compare existing extension points, test failure and upgrade behavior, assign owner | customization becomes unsupported, duplicated, or broader than its original outcome |
| compose | independent mechanisms own different parts of the contract, such as durable source plus idempotent effect | preserves authority boundaries and can close cross-system gaps | coordination, latency, state, signal, and recovery complexity | prove each interface, partial state, ordering, failure propagation, and joint recovery | one mechanism subsumes the other safely or interface burden exceeds accepted value |
| coexist_temporarily | old and new application, schema, signal, artifact, or platform states must overlap during migration | enables staged rollout and rollback or roll-forward options | dual compatibility, duplicated operations, and retirement can become permanent | define supported mixed states, observation, stop, recovery, deadline, and removal gate | transition evidence passes and every old consumer or state is retired |
| replace | the current mechanism cannot meet a hard contract, is unsupported, unsafe, or operationally unowned | removes a structural limitation or recurring failure source | largest implementation, migration, training, release, and recovery burden | establish disqualifier, evaluate target-compatible alternatives, run transition and failure scenarios | replacement fails acceptance, transition risk exceeds benefit, or a smaller adaptation works |
| split_outcome | one proposed change combines independently owned or independently releasable decisions | reduces context and isolates risk, evidence, and rollback | coordination and temporary interface work can increase | define boundaries, ordering, shared invariants, and intermediate states | split prevents an end-to-end usable state or introduces unsafe partial behavior |
| defer_with_evidence | current evidence cannot distinguish options and delay is acceptable | avoids irreversible choice while preserving learning | unresolved risk, temporary controls, and opportunity cost accumulate | document unknown, cheap discriminating experiment, owner, deadline, and safe interim state | evidence arrives, deadline or risk threshold is reached, or interim control fails |
| stop_and_contain | known harm is active or action requires unavailable authority | limits exposure and prevents unsupported mutation | service impact and manual burden may rise | preserve state, name authority, choose bounded containment, and monitor consequence | accountable owner approves recovery or target returns to an accepted state |
| route_away | another domain or platform owns the causal decision | keeps this reference from inventing policy or implementation | handoff latency and cross-owner ambiguity | record target facts, interface requirement, recipient, and urgency | receiving owner accepts action or evidence shows runtime owns the boundary after all |
| retire | a mechanism, temporary control, gate, signal, mixed state, or route no longer provides net value | reduces operational surface, cost, and false confidence | removal can strand consumers or erase recovery capability | inventory consumers, dependencies, retained evidence, removal scenario, and rollback | unexpected consumer or incident dependency appears during bounded removal |

**Hard gates before scoring tradeoffs**

Do not average these failures into a favorable aggregate score:

- target policy or accountable authority rejects the option;
- a supported artifact cannot be built, identified, promoted, or started reproducibly;
- required config or secret behavior leaks data, bypasses validation, or violates trust boundaries;
- data or migration states cannot preserve accepted invariants and supported consumers;
- health or rollout automation sends unsafe traffic or amplifies failure;
- shutdown, retry, or recovery can silently lose or repeat an unacceptable effect;
- the option depends on an inaccessible owner or environment while claiming production readiness;
- there is no feasible containment or recovery for a material partial transition.

A hard gate can be resolved with evidence or an authorized policy decision. It cannot be canceled by easier strengths such as developer familiarity, lower line count, faster unit tests, or a popular ecosystem path.

**Tradeoff dimensions**

| dimension | questions_to_compare | useful_evidence | common_blind_spot |
| --- | --- | --- | --- |
| target fit | Does the option preserve wrapper, framework mode, versions, extension points, and organizational policy? | effective build, config, dependency, platform, and owner records | choosing by generic Kotlin popularity |
| correctness | Which normal, degraded, interrupted, mixed-version, and recovered states satisfy the contract? | deterministic state tests, real-boundary integration, invariant and reconciliation checks | testing only steady-state success |
| compatibility | Which prior artifacts, data, clients, jobs, profiles, and platform states must coexist? | compatibility matrix, historical fixtures, rolling sequences, consumer inventory | treating build compatibility as runtime compatibility |
| reversibility | What state changes before failure, and can rollback, roll-forward, repair, or containment restore acceptance? | partial-transition rehearsal and immutable prior artifacts | saying rollback when data or effects are irreversible |
| operational burden | Who configures, observes, upgrades, responds, recovers, and retires it? | runbook exercise, ownership map, alert volume, maintenance history | counting implementation effort but not on-call work |
| failure amplification | Can retries, health, rollout, caches, or shared dependencies magnify a local defect? | fault injection, staged traffic, dependency outage, capacity behavior | evaluating components in isolation |
| security and authority | Which identities, secrets, permissions, data, and audit paths change? | threat and policy review, denied-access tests, redaction, effective permissions | assuming managed service means secure defaults |
| delivery evidence | Can CI gate the behavior and promote the same artifact through representative environments? | negative control, clean pipeline, digest lineage, package and platform smoke | relying on stage count or green status |
| performance and capacity | Which latency, throughput, memory, connection, queue, and cost effects are material? | representative workload, baseline, resource pressure, tail and saturation behavior | unsupported percentages or average-only comparison |
| complexity | Does the option reduce or add state transitions, control planes, dependencies, and failure modes? | architecture and lifecycle map, operational inventory, incident simulation | equating fewer source lines with lower system complexity |
| evidence cost | What is cheap to test, what requires production-like access, and what remains judgment? | gate map, environment availability, experiment safety and duration | selecting the option merely because it is easiest to demonstrate |
| future option value | Does the decision preserve compatible migration, provider, framework, data, and recovery choices? | staged design, interface stability, retirement plan, change-impact analysis | speculative abstraction without a plausible decision-sensitive future |

Use measured values only when the target workload, environment, method, and variability are explicit. Keep weighting and risk tolerance as owner judgments. A table can organize reasoning; it should not manufacture precision.

**Decision protocol**

1. **Name one decision.** Example: whether to preserve the existing migration tool while adding an expand-and-contract release, not whether to modernize all delivery.
2. **Define accepted outcomes and hard gates.** Include failure, partial transition, shutdown, and recovery states.
3. **Capture target baseline.** Record mechanism, version, owners, consumers, artifact, config, current gates, incidents, and operational cost that materially affect the decision.
4. **Generate feasible alternatives.** Include preservation and the smallest adaptation; add replacement or coexistence only when a gap warrants them.
5. **Reject non-starters explicitly.** State policy, compatibility, authority, data, security, or recovery disqualifiers.
6. **Map transition states.** Compare entering, operating, failing, recovering, and retiring each option, not only its final architecture.
7. **Choose discriminating evidence.** Prefer a cheap scenario that can eliminate an option before expensive staged evidence.
8. **Run target gates and retain uncertainty.** Separate result from forecast and label inaccessible environments.
9. **Assign the decision.** Record who accepts operational burden and residual risk, not only who writes the code.
10. **Stage commitment.** Use reversible experiments, canaries, compatibility periods, and stop conditions where consequence justifies them.
11. **Review second-order effects.** Check support skills, runbooks, alerts, capacity, permissions, incident response, and retirement.
12. **Set reevaluation events.** Tie them to versions, incidents, scale, policy, support, costs, or failed assumptions rather than an arbitrary calendar alone.

**Runtime-specific comparisons**

| decision_surface | preserve_when | adapt_or_compose_when | replace_or_stop_when | verification_focus |
| --- | --- | --- | --- | --- |
| build and plugins | wrapper and aligned versions produce the supported artifact and CI uses them | a bounded compiler, generated-code, or packaging gap has a supported extension | mechanism is unsupported, irreproducible, or cannot satisfy target runtime | effective versions, clean build, generated behavior, package identity, startup |
| configuration and secrets | typed startup binding and target secret integration meet policy | one new source, validation, rotation, or redaction boundary is needed | ambient lookup, exposure, or access model cannot be corrected safely in place | valid and invalid startup, denied access, redacted outputs, rotation and recovery |
| observability | existing signals distinguish the changed failure and lead to action | add one bounded dimension, propagation edge, alert, or runbook path | stack cannot meet privacy, reliability, cost, or platform support contract | induced failure through ingestion, query, consumer action, telemetry degradation |
| migrations | current tool and history support versioned production-dialect transitions | add staged expand, data remediation, mixed-version gate, or recovery procedure | tool or process cannot represent required compatibility or safe ownership | prior states, historical data, mixed versions, partial failure, recovery |
| package and image | deterministic package runs under target identity and lifecycle | tighten contents, permissions, health, resources, or architecture support | provenance or supported-runtime contract cannot be established | digest, effective user, config, resources, traffic, termination, restart |
| CI and release | mapped gates run on the promoted immutable artifact with bounded permissions | add or move a gate where it catches the changed boundary reliably | pipeline cannot establish artifact lineage, authority, or safe staged release | deliberate failure, clean run, digest promotion, stop and recovery action |
| worker ownership | current structured scope, durable identity, acknowledgment, and restart meet contract | compose drain, idempotency, reconciliation, or source semantics at a bounded gap | ownership remains ambiguous or repeated effects cannot meet accepted policy | interruption at every state, final effect, acknowledgment, restart, reconciliation |
| health and rollout | existing platform signals and stages reflect real traffic ability and bounded failure | adapt readiness, liveness, startup, observation, or stop conditions | automation repeatedly amplifies failure or cannot be controlled by an owner | degraded dependencies, traffic, restart, canary, containment, accepted recovery |

**Examples**

Good preservation: the repository already uses a versioned migration tool and has production-dialect fixtures. A new nullable column is added through an expansion compatible with old and new applications. The decision preserves the tool, adds historical-data and mixed-version scenarios, and stages contract removal later. Familiarity is not the reason; demonstrated fit is.

Justified adaptation: an existing telemetry stack carries request correlation but cannot distinguish drain deadline expiry. The route adds one bounded outcome signal and runbook action, verifies redaction and cardinality, and avoids replacing exporters, collectors, dashboards, or alert providers.

Unjustified replacement: a shutdown defect triggers a proposal to move from one framework and broker to another because their tutorials advertise structured concurrency. The proposal changes more state transitions, lacks target compatibility and migration evidence, and has no recovery plan. Preserve and repair the owned lifecycle first; evaluate replacement only if a demonstrated hard gap remains.

Conditional deferral: two image bases both start the package locally, but the candidate's target architecture and security-support status cannot be established without platform authority. Local evidence can narrow the options; release selection remains deferred with a specific owner and retrieval or staged test.

Good stop: a schema migration encounters unexpected historical rows that violate a new constraint. The route stops rollout, preserves data and artifact state, invokes the authorized remediation or roll-forward decision, and does not let green application tests override the data gate.

Borderline experiment: a worker could use bounded in-process drain or durable source handoff. Rather than debate architecture, the team injects termination across real work phases under representative duration and platform grace. If all admitted work finishes with margin and has no ambiguous external effects, drain may be sufficient; otherwise durable ownership becomes evidence-driven.

**Decision evidence record**

```text
decision_id_and_owner:
accepted_outcome:
target_baseline_and_artifact:
hard_gates:
options_considered:
options_rejected_and_reason:
transition_states_per_option:
measured_facts:
external_facts_and_version_scope:
judgment_and_weighting:
negative_or_degraded_scenarios:
results_and_limitations:
selected_mode_and_mechanism:
compatibility_period:
stop_and_recovery_conditions:
operational_owner_and_runbook:
temporary_controls_and_retirement:
reevaluation_or_invalidation_events:
```

The cost of being wrong includes more than implementation rework. It can include incompatible data, wrong artifacts, leaked credentials, misleading health, noisy or silent signals, duplicate effects, delayed incidents, support burden, and lost future options. Name which costs are plausible and who carries them.

Prefer staged decisions when evidence is incomplete: preserve a compatible interface, run a bounded spike, add a reversible gate, or coexist for a defined period. Staging is not free; dual paths and temporary controls need owners, signals, deadlines, and removal evidence. Revisit a choice when its version or support changes, a workload crosses an observed range, an incident contradicts the model, policy changes, operational burden exceeds acceptance, or a formerly inaccessible gate becomes available.

## Local Corpus Hierarchy

`local_corpus_hierarchy_note`: The frozen 2026-06 Kotlin backend delivery corpus provides historical doctrine and routing. Its runtime file is the primary local orientation source for this reference, not universal current policy. Claim authority still depends on target instructions, actual mechanisms, accountable owners, observed results, and, when needed, refreshed version-applicable primary documentation.

Classify source roles per claim or region. One file can be primary for selecting questions, supporting for mechanism design, conflicting with target state, and historical for current-version behavior at the same time.

**Frozen source inventory**

| local_source | frozen_sha256 | default_claim_role | activate_for | does_not_establish_alone |
| --- | --- | --- | --- | --- |
| `references/reference-map.md` | `7451085f357ed6af8fdd41f592e83f5f4b5c7aa858be8a5456390b377f00f180` | orientation and progressive-routing source | choosing Operations, Persistence, Coroutine, Resilience, Framework, Testing, Security, or Review paths | target applicability, source freshness, implementation correctness, or operational outcome |
| `SKILL.md` | `e3413837049aa6f31d325fa368bb8b9dcce7f298c770b42cd5f13c1217c3a410` | historical workflow and mode-selection source | reconstructing how the frozen skill combined modes, output contracts, guardrails, and context strategy | current tool availability, current repository policy, or authority to change production state |
| `references/kotlin-backend-runtime-and-ops.md` | `d0a218f3c5d7b07c561cd4aba94b7c943aa7575cd439d371fdbaf4e5415b1069` | primary local runtime-question source | build, static gates, config, secrets, profiles, observability, migrations, containers, CI, and operational review | exact target tool, provider semantics, measured safety, or current external behavior |
| `references/kotlin-backend-playbook.md` | `8654c3a4c68cda2514c546035e7a7908a99ad0f884088b7bf329abf807c31994` | supporting application-boundary source | service anatomy, requirements, domain and transport separation, errors, persistence, transactions, coroutines, clients, workers, and API contracts | platform policy, deployment result, broker or database provider behavior, or recovery authority |
| `references/kotlin-spring-ktor-idioms.md` | `02c20786240e893fc258f4e067557bc65dcdafcac11a6efbdd049710b827ac5d` | supporting framework-mechanism source | Spring package, bean, plugin, config, MVC/WebFlux, validation, persistence; Ktor application, serialization, status, routing, and testing | permission to switch framework, exact target version, package lifecycle, traffic, or production recovery |
| `references/kotlin-backend-testing-and-fixtures.md` | `92f45a34cc8ac472b930eba33e4ffb6a442719baa53dd8caabd43006dfa99e26` | supporting verification-design source | Spring, Ktor, coroutine, persistence, contract, property, fixture, matrix, and quality-gate choices | production equivalence, artifact promotion, platform semantics, or a pass without target execution |
| `references/kotlin-backend-security-and-resilience.md` | `8a07eb77e27a3b508224db76c60e20508b8b3d13b81fce86e87ea052be7d14a5` | supporting trust and failure-semantics source | auth, sessions, validation, coroutine resilience, blocking, retries, idempotency, clients, and background work | organizational risk acceptance, effective identities, provider guarantees, containment, or recovered production state |
| `references/sources-and-research-brief.md` | `2f73340890073548e7c9a723ba051528e0097581444889cc7a8fa400026a1ee1` | historical provenance and public-discovery source dated 2026-06-23 | checking how frozen doctrine described public sources, candidate approaches, and synthesis | current page content, supported releases, present maintenance, or target compatibility |

All paths above are relative to `agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/`. Hashes identify the exact frozen inputs read or routed during this evolution. A matching hash proves identity, not truth or applicability.

**Practical role vocabulary**

| role | meaning | next_evidence_action |
| --- | --- | --- |
| primary_orientation | best local starting point for the named question family | read the complete relevant region and identify its assumptions and companions |
| supporting_semantics | supplies detail for a boundary owned outside the primary source | reconcile its contract with the lead runtime outcome and target mechanism |
| target_instruction | repository or directory rule governing allowed work | follow within scope and surface conflicts rather than silently overriding it |
| target_policy | accountable organizational or platform rule | confirm ownership, enforcement, applicability, exception process, and current version |
| target_implementation_fact | effective wrapper, dependency, config, code, artifact, pipeline, or deployment state | verify through direct inspection and trace to the accepted outcome |
| observed_result | output from an executed gate or scenario in a named environment | retain action, artifact, fixture, result, limitation, and invalidation event |
| local_doctrine | frozen recommendation or warning from the corpus | use as a review hypothesis and test against target state |
| combined_synthesis | conclusion joining multiple local, target, or external facts | expose premises, counterargument, uncertainty, and owner judgment |
| unrefreshed_historical_lead | dated public location or summary not retrieved in the current work | refresh only if a current external claim matters and browsing is authorized |
| refreshed_external_fact | bounded statement retrieved from applicable primary authority | record URL or revision, retrieval time, version, prerequisites, and exact claim |
| legacy | material describing a mechanism no longer supported for the target | retain only for migration, archaeology, incident, or compatibility reasoning |
| duplicate_derived | repeated or generated guidance sharing an upstream origin | count as discoverability, not independent corroboration; track derivation |
| conflicting | evidence that cannot be reconciled by version, scope, mode, or ownership | preserve both, run a discriminating check, and escalate policy judgment if needed |
| superseded | a newer owned decision or source explicitly replaces the claim | migrate consumers and remove or mark the old route after verification |
| rejected_for_target | claim was considered but failed applicability, policy, or evidence | record why and what event would justify reopening it |

**Precedence and reconciliation**

There is no universal ranking that makes one source win every dispute. Use this claim-directed order:

1. **Safety and authority boundary:** stop unsupported production mutation, secret access, destructive data action, or risk acceptance regardless of source prestige.
2. **Applicable target instruction and policy:** these govern allowed mechanisms within their owned scope, unless they conflict with higher authority or an active safety obligation that requires escalation.
3. **Observed target result:** execution can disprove an assumed behavior, but interpret it with the actual artifact, environment, fixture, and gate quality.
4. **Target implementation fact:** effective config and resolved dependencies outrank a generic description of what the repository is expected to use.
5. **Version-applicable primary external authority:** use it for current language, library, framework, provider, compatibility, or security semantics after authorized refresh.
6. **Frozen local doctrine and specialist synthesis:** use it to select questions, alternatives, and failure modes, while preserving its date and scope.
7. **Tutorials, samples, representative repositories, and duplicated summaries:** use them for orientation and option discovery, not decisive production claims.

Observed behavior does not automatically override security or policy; it can reveal that implementation violates them. Target policy does not make an impossible mechanism work; it can trigger owner escalation or a policy update. A local source can challenge an unsafe target convention without independently authorizing its replacement.

**Progressive corpus routes**

| task_shape | lead_local_source | activated_support | intentionally_defer_until_needed |
| --- | --- | --- | --- |
| typed non-secret config key | runtime Configuration And Secrets | framework Configuration; testing startup cases | security if value is not sensitive; migration if no data state changes |
| secret-provider or redaction change | runtime Configuration And Secrets | security Trust Boundaries; framework binding; testing denied and output cases | persistence unless secrets or audit state enter storage |
| schema and rolling deployment | playbook persistence and transactions plus runtime Database Migrations | testing persistence; security idempotency when repeated effects matter | framework sections unrelated to persistence mechanism |
| external client timeout | playbook External Clients And Workers | security Coroutine Resilience, Retries, Idempotency, External API Clients; runtime config and signals; testing | migrations unless state schema changes |
| worker shutdown and restart | playbook worker and coroutine boundaries | security background work and idempotency; runtime package, signals, health, shutdown, and CI; testing | Spring or Ktor details until target framework is known |
| image or deployment change | runtime Build and Container regions | security for permissions and secrets; testing package smoke; target platform runbook | application domain guidance when business behavior is unchanged |
| production-readiness review | reference-map Review order | security, runtime, testing, then playbook, with framework regions activated by target | full external refresh until a version-sensitive decision is found |
| Kotlin type or domain-only design | playbook or language-oriented guidance | framework or testing if activated | runtime operations when no packaged lifecycle transition changes |

Focused route example: adding a required non-sensitive port range reads the runtime config region, the target's actual binding mechanism, and startup tests. It does not need every security, migration, persistence, worker, or public-source section. The route remains valid only if package and platform injection do not introduce additional boundaries.

Composed route example: changing acknowledgment order for a queue worker starts with playbook ownership and security idempotency, then uses runtime shutdown, signals, package, and CI regions plus target broker semantics. Framework idioms joins only for the actual application lifecycle hook.

Conflict example: frozen doctrine recommends one health pattern, while target platform policy distinguishes startup, readiness, and liveness differently. Record the local question, follow applicable platform ownership for mechanism, and exercise traffic and restart behavior. Do not call the local source wrong globally or the platform safe without evidence.

Excessive-context example: loading all seven files for a formatter rule change can crowd out the configured task and CI invocation that decide the result. Read Static Analysis And Formatting, inspect target configuration, run the gate, and expand only if the rule affects generated code, build, or policy.

**Conflict and duplicate handling**

- Check whether apparent conflict is caused by different versions, Spring versus Ktor, blocking versus coroutine mode, local versus managed infrastructure, development versus release policy, or recommendation versus requirement.
- Identify derivation. Two summaries copied from the same brief are one lineage, not independent confirmation.
- Preserve exact claims and scopes. Avoid merging incompatible statements into a broad compromise that neither source supports.
- Let a target scenario discriminate behavior where safe. Escalate policy, compliance, support, or risk disagreements to the accountable owner.
- Record rejected and superseded claims so future work does not repeatedly rediscover the same dead end.
- Consolidate duplicate doctrine when one maintained owner can serve all consumers; keep local pointers for discoverability.

**Corpus claim ledger**

```text
claim_id:
decision_or_requirement:
source_path_and_hash:
source_region:
source_role:
complete_region_read:
claim_extracted:
date_or_version_scope:
derived_from_or_duplicates:
supporting_sources:
conflicting_sources:
target_instruction_or_policy:
target_implementation_locator:
verification_action_and_result:
uncertainty_and_owner:
consuming_artifact_or_runbook:
invalidation_event:
supersession_or_retirement_action:
```

Verify that every path exists at the recorded identity, relevant regions were read completely, role labels match how the claim is used, conflicts are unresolved only when explicitly owned, and observed results refer to the intended artifact and environment. Presence in the corpus is not sufficient.

Use claim-level lineage for selective invalidation. A change to coroutine semantics should rerun dependent worker, timeout, shutdown, and recovery routes; it need not invalidate an unrelated formatter decision. A platform health-policy change should rerun traffic and restart scenarios even if application source is unchanged. A target incident can demote a previously trusted mechanism and promote a new review question without rewriting every source role.

The hierarchy is healthy when readers can open less context while retaining every consequential assumption, conflict, gate, and owner. It is unhealthy when canonical labels hide drift, duplicate prose looks like corroboration, or new summaries accumulate without retiring obsolete authority.

## Theme Specific Artifact

`theme_specific_artifact`: A versioned Kotlin backend runtime operations runbook for release, observation, stop, containment, recovery, service-objective breach, signal failure, shutdown, and incident review.

The runbook is complete only when an authorized responder can identify the intended artifact and state, choose the next action from observed evidence, execute or escalate through target-owned procedure, and verify an accepted recovered condition. A collection of commands without decision boundaries is not complete.

**Runbook depth tiers**

| tier | use_when | minimum_artifact | upgrade_trigger |
| --- | --- | --- | --- |
| bounded handoff | reversible non-production or low-consequence change with one owner | outcome, artifact or revision, configured gate, result, limitation, owner, and recovery or undo note | shared use, stateful behavior, external effect, release automation, or another operator must act |
| release runbook | repeated deployment or change affecting config, data, package, signals, traffic, or shutdown | full release identity, prerequisites, stage states, observation, stop authority, recovery choices, and validation | on-call response, partial state, mixed versions, service objective, destructive action, or cross-owner incident |
| incident-capable runbook | production service with material availability, data, security, external-effect, or recovery obligations | release runbook plus incident entry, containment, evidence preservation, escalation, signal failure, reconciliation, review, and rehearsal | remain at this tier while the operational consequence and support contract exist |

Service size is not the deciding factor. A small worker with irreversible effects can need a deeper runbook than a large stateless internal service.

**Artifact completion schema**

| artifact_field | completion_rule | authoritative_input | reject_when |
| --- | --- | --- | --- |
| purpose_and_scope | name accepted normal, degraded, failed, shutdown, and recovered states plus affected users and operators | executable requirements and owner decision | says only deploy, productionize, or keep healthy |
| target_identity | identify repository, service, module, environment class, and accountable team without exposing secrets | target instructions, service catalog, ownership record | service or environment could be confused with another target |
| release_identity | bind source revision, build inputs, package or image digest, migration set, and config revision | wrapper, CI provenance, artifact registry, deployment record | uses a mutable tag or rebuilds untracked bits per environment |
| supported_states | enumerate application, config, schema, consumer, dependency, traffic, worker, and platform states allowed during the procedure | compatibility and lifecycle contracts | mixed or partial states can occur but are not described |
| prerequisites | state required access, approvals, backups or recovery readiness, capacity, dependencies, maintenance state, and clean gates | policy, gate evidence, platform and data owners | action can begin without validating a hard precondition |
| secret_and_access_boundary | identify roles and access paths, redaction rules, break-glass ownership, and forbidden output | security policy and effective identity tests | real credentials, tokens, private payloads, or unrestricted access are embedded |
| baseline | record the bounded signals and state used to distinguish change impact from preexisting behavior | current artifact, representative observation, incident state | no comparison state or signal semantics exist |
| stage_plan | define artifact, environment, traffic or work slice, duration condition, owner, and expected state for each stage | release policy and target platform mechanism | progression occurs only because time elapsed |
| decision_signals | map each signal to failure hypothesis, bounded dimensions, query, consumer, action, and telemetry-failure behavior | observability design and exercised queries | says watch logs or dashboard without an operational decision |
| service_objective_breach | identify the target-owned objective, window or state, burn or consequence interpretation, and response authority without inventing values | service policy, measured baseline, objective owner | threshold lacks source, applicability, or action |
| health_and_traffic | distinguish startup, readiness, liveness, degraded state, intake, drain, traffic, and restart semantics | framework mechanism, platform policy, fault scenario | process status is treated as real traffic ability |
| data_and_migration | identify prior state, migration, historical data, mixed versions, partial failure, lock or capacity concern, and recovery choice | migration history, database authority, staged tests | rollback is named without accounting for changed data |
| worker_and_shutdown | define admission stop, owned work, cancellation, drain, deadline, durable identity, acknowledgment, restart, and reconciliation | application lifecycle, broker or store semantics, packaged termination test | graceful means only clean process exit or fixed delay |
| external_dependencies | state dependency, timeout and cancellation budget, retry and idempotency contract, degraded mode, quota, and owner | client design, provider authority, resilience tests | retries or fallback can repeat effects or amplify outage without bounds |
| stop_conditions | list observable conditions that pause progression or trigger containment, with decision owner | requirement hard gates, release policy, incident authority | responder must improvise whether a condition is severe enough |
| recovery_options | choose among rollback, roll-forward, repair, replay, reconciliation, failover, or containment from actual state | compatibility, artifact inventory, data and external-effect state, owner | recovery is a single optimistic verb detached from partial state |
| action_procedures | link repository and platform-native commands or automation by owned version, prerequisites, effects, expected output, and cleanup | maintained target procedure and access policy | copies generic commands or mutates production without explicit authorization |
| verification_after_action | specify final business, data, traffic, work, signal, and resource states that prove action success | executable requirement and scenario result | process or command status is the only acceptance signal |
| escalation_and_communications | name role-based contacts, severity and policy route, decision log, customer or stakeholder obligations, and handoff format | incident process and ownership system | depends only on an individual's memory or stale personal contact |
| evidence_preservation | record artifact, config, data, traffic, timestamps, work identifiers, bounded signals, actions, and access-safe storage | incident and audit policy | procedure destroys the only state needed for diagnosis or recovery |
| known_limits | state inaccessible environments, untested actions, unsupported versions, provider gaps, and conditional claims | verification record and owner review | silence is used to imply complete coverage |
| rehearsal_evidence | record scenario, participants, environment, injected condition, decisions, actions, timing, result, and correction | tabletop, staged drill, or incident evidence | only document review has occurred for consequential actions |
| invalidation_events | name changes to artifact, config, schema, dependencies, signals, platform, access, owners, policy, or recovery that force review | source and target change map | runbook relies on a calendar review alone |
| retirement | identify when the service, mechanism, temporary control, old artifact, or mixed state can be removed and how consumers are verified | ownership, consumer inventory, completed transition evidence | obsolete instructions remain discoverable as current action |

Target values must be populated from inspected policy, mechanism, and executed evidence. Unknown values remain explicitly unknown with an owner and blocking scope; do not fill gaps with plausible commands, thresholds, contacts, or deadlines.

**Runbook lifecycle states**

| state | entry_evidence | responder_decision | allowed_transition |
| --- | --- | --- | --- |
| candidate | accepted change and identified owner exist | is the runbook tier proportional and are target mechanisms discoverable? | qualification or stop for missing authority |
| qualified | prerequisites, gates, artifact lineage, stage, signals, stop, and recovery have rehearsal evidence at required fidelity | may this artifact enter the first bounded stage? | staged release or return to implementation |
| staged | intended artifact is running under bounded traffic or work with baseline and observation | continue, hold, stop, contain, or recover from named signals | next stage, qualification correction, or incident entry |
| active | rollout acceptance and post-release validation are observed | close release, continue enhanced observation, or open follow-up | steady operations or incident entry |
| degraded | accepted degraded state is present and owned | continue bounded operation, shed load, pause intake, contain, or recover | active, incident, or recovered |
| incident | normal or degraded contract is violated or state is ambiguous | preserve, classify, contain, escalate, and select recovery | contained, recovered, or owner-directed exception |
| contained | propagation is bounded but service or business state may remain incomplete | choose rollback, roll-forward, repair, replay, reconciliation, or monitored hold | recovered or incident if containment fails |
| recovered | business, data, work, traffic, resources, and signals meet the accepted recovered contract | return to service, retain monitoring, and schedule learning actions | active or review |
| under_review | evidence and actions are being reconciled after release, drill, or incident | update requirements, gates, runbook, ownership, or design | qualified revision or retirement |
| retired | mechanism or service has no active consumer and removal evidence passed | archive evidence and prevent accidental execution | reopen only through a new owned decision |

**Normal release entry**

1. Confirm the accepted outcome, owner, target instructions, change scope, and runbook version.
2. Confirm source revision, wrapper and effective versions, package or image digest, migration set, config revision, and promoted artifact are coherent.
3. Confirm mapped deterministic and production-like gates passed on the intended artifact; list conditional evidence.
4. Verify required access through the target identity without printing sensitive values. Confirm escalation and stop authority are reachable.
5. Capture baseline business, request, dependency, data, work, resource, health, and signal state applicable to this release.
6. Validate schema and application compatibility, historical-data assumptions, mixed states, and recovery before data mutation.
7. Enter the smallest release stage defined by policy. Observe named signals and actual service behavior, not a dashboard color alone.
8. At each decision point, continue only when expected state is observed and no stop condition activates. Retain decision and artifact identity.
9. After full progression, exercise post-release validation, shutdown or restart behavior when changed, and final business-state checks.
10. Close with result, limitations, enhanced observation period if required, temporary controls, owners, and invalidation events.

**Incident entry**

Enter from any state when a hard contract fails or state becomes materially ambiguous:

1. Establish incident authority and protect people, data, credentials, and evidence.
2. Record current and prior artifact, config, schema, traffic, work, dependency, and platform states plus timestamps.
3. Classify the earliest supported break: artifact, startup, secret, dependency, data, signal, health, traffic, work ownership, shutdown, or recovery.
4. Use decision signals to bound impact. If telemetry is suspected, verify from an independent state source before acting.
5. Apply only authorized containment whose effects and stop conditions are understood. Avoid destroying diagnostic or recovery state.
6. Select recovery from actual partial state. Rollback is appropriate only when prior artifact and all dependent data, messages, caches, and effects remain compatible.
7. Verify recovered business invariants, not merely process health. Reconcile work and external effects where ambiguity exists.
8. Hand off residual risk, repair, enhanced observation, customer or stakeholder obligations, and follow-up owners.
9. Preserve the decision log and compare observed behavior with runbook assumptions during review.

**Service-objective and signal path**

The runbook must not invent a service objective. For every target-owned objective it uses, record what user or operator outcome it represents, which population and window apply, where the data originates, how missing or delayed telemetry is handled, and which action is authorized at each condition. A breach signal is a hypothesis until correlated with service and business state.

For logs, metrics, and traces, specify bounded identifiers, privacy rules, query or view, expected normal and failure shapes, and consumer. Include a path for telemetry outage or corruption. A runbook that says `check logs` without a query, hypothesis, and next decision is incomplete.

**Recovery decision matrix**

| observed_partial_state | candidate_action | prerequisite | reject_action_when | final_validation |
| --- | --- | --- | --- | --- |
| code regression with unchanged compatible data and known prior artifact | rollback may be viable | immutable prior artifact, config compatibility, owner approval | schema, messages, caches, or effects are incompatible with old code | business behavior, traffic, data, work, and signals recover under prior artifact |
| compatible schema expansion with new-code failure | rollback code while retaining expansion may be viable | old code tolerates expanded schema and no new-only data contract is active | old application cannot read current state | old/new compatibility and target invariants pass |
| partially applied data transformation | roll-forward, repair, or containment is usually evaluated before rollback | exact completed state, idempotent continuation or repair, backup and owner authority | inverse operation is lossy or unsupported | data invariants, application compatibility, and audit record pass |
| external effect may have committed after timeout | reconcile before replay | stable effect identity or provider lookup and authorized repair | blind retry can repeat an unacceptable effect | final provider and business state agree; source work is resolved |
| wrong artifact promoted | stop and restore known intended artifact path | artifact inventory, promotion authority, compatibility | state created by wrong artifact is incompatible | digest, config, data, traffic, and behavior match accepted release |
| false readiness routes unsafe traffic | remove or hold traffic and correct health contract under platform authority | independent service-state evidence and controlled routing | restart or rollout would amplify failure | readiness matches real request ability through degraded and recovered states |
| worker drain deadline expires | stop intake, preserve unfinished identities, and use source recovery or reconciliation | observable ownership and restart semantics | killing process would strand or duplicate effects silently | every admitted item is complete, retryable, released, or reconciled |

This matrix frames decisions; target runbooks must supply the actual authorized procedure. Never copy provider, database, migration, traffic, credential, or production fault commands from generic guidance.

**Artifact qualification**

| qualification_level | evidence | claim_supported |
| --- | --- | --- |
| reviewed | builder and operator inspect completeness, ownership, commands, effects, signals, and recovery logic | textual coherence and identified gaps |
| tabletop | responders walk through a normal release, ambiguous signal, stop condition, partial migration or effect, and handoff | decision path and role clarity without mechanism execution |
| isolated_drill | safe environment executes package, signal, failure, stop, shutdown, restart, and recovery procedures with representative state | mechanism behavior within isolated fidelity |
| staged_rehearsal | authorized target-like or bounded platform environment exercises traffic, identity, dependency, data, lifecycle, and recovery | scoped operational behavior for the staged environment |
| incident_validated | a real event confirms or contradicts steps, evidence, timing, authority, and recovery | observed applicability to that incident, not universal future correctness |

Rehearsal should measure correctness of state recognition and decision, not reward fast command entry. Capture where responders searched, hesitated, lacked access, misread a signal, or found a stale link. Correct the artifact and rerun the affected path.

Good runbook entry: identifies one image digest and config revision, states the compatible schema range, defines canary state and stop conditions, links bounded queries to decisions, names authority, and distinguishes rollback from data repair. A drill induces readiness failure and confirms traffic stops before the next stage.

Bad runbook entry: says deploy latest, watch logs for a few minutes, and rollback if errors rise. It lacks immutable identity, objective source, signal meaning, data state, traffic semantics, owner, action effects, and final recovery validation.

Conditional entry: local package, migration, and shutdown procedures are rehearsed, while managed-platform traffic and identity actions have not been. Mark those actions unqualified, name the platform owner and required staged scenario, and prevent the runbook from claiming full deployment readiness.

Failed rehearsal example: a responder follows the documented rollback after a schema contract step and discovers the prior artifact cannot read new rows. The runbook is corrected to stop before contract, retain compatible expansion, and use an owner-approved roll-forward or repair path. The failure improves the artifact because it was found before production action.

**Maintenance and retirement**

Review the affected runbook path when wrapper or dependencies change, artifact packaging changes, config or secret integration changes, schema or migration history changes, signals or objectives change, platform behavior changes, owners or access change, a drill fails, or an incident contradicts an assumption. Use claim-level lineage so an alert query change does not force unrelated migration steps to be rewritten.

Track runbook use as evidence: which entry paths are used, which steps are skipped, where escalation stalls, which signals are misleading, and whether recovery reaches the expected state. Do not optimize for document-open counts. Retire old artifacts, mixed-state procedures, temporary controls, and obsolete contacts after consumer and recovery checks pass. Keep historical incident evidence separate from current executable procedure.

A qualified runbook is an integration test of organizational ownership. It demonstrates that builders, operators, security, data, platform, and incident owners agree on the artifact, state, decision, and recovery interfaces required to operate the Kotlin backend safely.

## Worked Example Set

These examples are scenario synthesis, not reports from a specific target. Product names, task names, provider behavior, thresholds, deadlines, and results must come from target discovery and execution. Transfer the state-transition reasoning; do not copy mechanisms by resemblance.

**Example 1: Typed outbound-client configuration**

Starting state: an existing Kotlin service calls a downstream dependency. The accepted change adds a bounded request timeout and a credential reference. The repository already has a wrapper, framework configuration binding, an external-client adapter, a target secret integration, and a telemetry path.

Good path:

1. Define outcomes: valid config starts; missing, malformed, or out-of-policy timeout does not enter service; missing or denied credential access fails according to target startup policy; secret material never appears in bounded outputs; a slow dependency ends within the accepted total deadline and releases owned work.
2. Inspect the actual binding and client path. Preserve Spring or Ktor, wrapper, client library, secret provider, and telemetry unless their change is separately accepted.
3. Bind raw values once at the composition boundary into typed settings. Separate sensitive handles or values from printable general config. Inject only the settings each adapter needs.
4. Derive client timeout from the accepted end-to-end budget rather than inserting a plausible duration. Reconcile framework, coroutine, proxy, and platform deadlines.
5. Test valid, absent, malformed, minimum, maximum, unknown-key, denied-secret, and restart cases through the real binding path. Use recognizably non-production secret canaries and scan errors, logs, traces, health, and serialized config views.
6. Start the packaged artifact with representative non-secret environment input. Exercise downstream delay, connection failure, response failure, cancellation, and recovery. Confirm bounded signal and runbook action.
7. Retain the config schema, target mechanism, package identity, results, inaccessible provider behavior, and invalidation events.

Why it is good: the route changes one accepted configuration and client behavior, preserves target machinery, separates storage from secret safety, and proves startup plus failure semantics instead of only constructing a data object.

Misleading path: read environment variables deep inside the client on every call, parse failure as a default, include the full config object in error output, choose a timeout from a tutorial, and add a new config library because it looks idiomatic. A unit test that calls the client with a valid string passes, while packaged startup, missing values, secret denial, total deadline, cancellation, and outputs remain untested.

Conditional path: typed binding, malformed input, package startup, cancellation, and redaction pass locally, but the managed secret identity and rotation path cannot be exercised. The config implementation can pass its local contract; secret-provider readiness remains conditional with a named owner and authorized scenario. Do not average them into one confidence score.

Target substitutions required: effective framework binding, supported value syntax and units, timeout budget owner, secret provider and identity, client cancellation semantics, package startup action, telemetry output surfaces, and deployment injection.

**Example 2: Signal and health change**

Starting state: operators cannot distinguish downstream saturation from application rejection during a bad release. The service already emits structured logs and metrics and exposes a framework health mechanism. The deployment platform consumes health to control traffic and restart.

Good path:

1. State the decision: when downstream capacity is exhausted, responders must distinguish that state from validation, application failure, network failure, and telemetry failure, then take a target-owned action.
2. Reproduce or safely inject the condition and inspect existing signals before adding any. Identify which bounded dimensions and correlation already exist.
3. Add only the missing classification or bounded measurement. Keep user-controlled values, credentials, payloads, stack text, and high-variety identifiers out of metric dimensions.
4. Preserve readiness and liveness ownership. If the service cannot satisfy its accepted request contract, test whether target policy should remove traffic; do not automatically fail liveness because a dependency is unavailable.
5. Trace the signal through SDK, exporter, collector, backend, query, dashboard or alert, consumer, and runbook. Inject telemetry delay or loss so absence is not confused with recovery.
6. Exercise dependency slow, dependency unavailable, application overload, and local unrecoverable state. Observe actual requests, traffic, restart count, signal privacy, cardinality, and recovered state.

Why it is good: telemetry is tied to one failure decision, and health behavior is verified through platform automation instead of inferred from an endpoint status.

Misleading path: install a new observability stack, add request paths and exception messages as metric labels, alert on an unowned threshold, and make liveness depend on every downstream system. A dashboard becomes more colorful while restarts amplify the dependency outage and cardinality obscures diagnosis.

Conditional path: application-level signal shape, redaction, and injected failure pass; the collector and platform traffic policy are unavailable in the test environment. The route can claim signal production and local health-state behavior, not end-to-end alert delivery or safe traffic automation.

Target substitutions required: signal backend, bounded dimensions, retention and privacy policy, actual service objective, consumers, alert route, framework health integration, platform startup/readiness/liveness policy, traffic mechanism, and restart authority.

**Example 3: Schema and rolling application change**

Starting state: a Kotlin backend must introduce a stricter data invariant while existing instances, background jobs, and stored rows may still use the old shape. The repository already has a migration tool and database integration tests.

Good path:

1. Inventory supported prior schema versions, application versions, consumers, historical data shapes, database dialect, migration ownership, deployment order, and recovery authority.
2. Express the invariant independently of migration syntax. Identify rows that violate it and how they will be remediated or quarantined.
3. Prefer a compatible expansion when rolling coexistence is required. Deploy code able to tolerate the intermediate shape, migrate or backfill under bounded ownership, observe completion and invariants, switch writers or readers deliberately, then contract only after old consumers are absent.
4. Store versioned migrations with the application and preserve the target tool. Do not rewrite applied history casually.
5. Test from each supported prior state against the production dialect with representative historical rows. Exercise old and new application versions in allowed orders, concurrent access where relevant, partial migration failure, retry or repair, and final invariant checks.
6. Map migration gates into CI and staged release. Record artifact, migration set, data state, locks or resource effects, stop condition, and selected roll-forward, repair, or rollback boundary.

Why it is good: compatibility is proven across transition states, and recovery is selected from actual data state rather than attached as a generic rollback promise.

Misleading path: update application validation and add a required database constraint in one release, verify it against an empty local database, and call the change reversible because the previous image still exists. Historical rows, old instances, jobs, locks, partial application, and the inability of old code to read new state remain invisible.

Conditional path: production-dialect migrations from all known prior schemas and mixed-version application tests pass with representative data, but target-scale lock and duration behavior cannot be reproduced. Syntax, compatibility, and fixture invariants pass; capacity and rollout timing remain conditional. The rollout must use target observation and stop authority rather than an invented duration claim.

Target substitutions required: actual database and version, migration tool and ownership, transaction and DDL semantics, historical profile, supported application coexistence, data sensitivity, maintenance or online policy, capacity limits, backup or recovery process, and artifact rollout.

**Example 4: CI gate and immutable artifact promotion**

Starting state: a release occasionally differs from the package tested in pull-request CI. The change request proposes more pipeline stages, but the artifact path is not yet traced.

Good path:

1. Map the accepted claim: configured build and affected runtime gates must execute on one source revision, then the resulting identified artifact must be promoted through environments without untracked rebuild.
2. Inspect repository wrapper, task definitions, profiles, test source sets, skip flags, caches, runner identity, artifact output, registry, promotion mechanism, and deployment input.
3. Add a safe negative control at the changed boundary and show the intended stage fails. Confirm a green stage does not hide skipped or empty test selection.
4. Build and package with repository-native mechanisms. Record wrapper, effective versions, source revision, inputs, package or image digest, and retained gate outputs.
5. Promote the same identity into an isolated or staged environment with environment-specific validated config. Verify package startup, relevant integration, signals, health, shutdown, and recovery activated by the change.
6. Restrict pipeline permissions and secrets to required stages. Preserve failure artifacts and make stop authority explicit.

Why it is good: stage count is irrelevant; each gate names a failure class and every environment refers to the intended bits.

Misleading path: use a globally installed build tool locally, run a broad task without inspecting exclusions, rebuild a mutable tag in each environment, and accept a green deployment step as proof. A source fix can pass while production receives different dependencies or package contents.

Conditional path: CI negative control, clean build, package digest, and isolated startup pass, but the production promotion system is controlled by another platform team and cannot be inspected. Build evidence remains valid; immutable end-to-end promotion remains a handoff requirement.

Target substitutions required: wrapper and tasks, cache keys, runner, artifact format, registry, signing or provenance policy, environment config, deployment mechanism, permissions, stage policy, and failure retention.

**Example 5: Worker shutdown and restart**

Starting state: a Kotlin background worker processes durable work and calls an external system. A rolling restart can occur between external commit and local acknowledgment.

Good path:

1. Model available, acquired, processing, effect-prepared, effect-committed, completion-recorded, acknowledged, draining, terminated, restarted, and recovered states that actually exist.
2. Inspect application scope, child ownership, blocking boundaries, source lease or acknowledgment, stable work identity, external idempotency or query support, transaction, config, signals, package, platform grace, and runbook.
3. Stop admission before drain. Propagate cancellation and one total deadline through owned work. Give durable effects a stable identity and preserve ambiguous outcomes for reconciliation rather than blind retry.
4. Order completion and acknowledgment according to target semantics. Make restart discover pending, expired, duplicate, and ambiguous attempts.
5. Interrupt each consequential phase in deterministic tests and real-boundary integration. Send target-like termination to the packaged artifact and verify drain, deadline, resource release, restart, redelivery, duplicate suppression, final business state, and operator action.
6. Stage under bounded work and exercise stop and recovery authority before broad rollout.

Why it is good: graceful shutdown is measured by work and effect state, not process exit; exact mechanisms stay owned by the target.

Misleading path: launch work in an untracked process scope, acknowledge on receipt, add a fixed sleep in the shutdown hook, and retry every timeout. Local logs say shutdown complete, while external effects can repeat and source work can disappear.

Conditional path: ownership, real database and source integration, package termination, and restart reconciliation pass, but managed-platform forced termination and grace behavior cannot be induced. Report the passed lifecycle subset and preserve platform qualification as a release gate.

Target substitutions required: framework lifecycle, coroutine version and scope, blocking adapters, source semantics, external-effect identity, transaction, platform termination, work duration profile, signals, and recovery authority.

**Cross-example incident trace**

A rollout shows increased failures after a schema and image change. A poor response immediately rolls back the image. A disciplined response preserves artifact, migration, data, traffic, and signals; determines whether old code remains compatible with current data; checks whether the promoted digest matches CI; distinguishes application failure from false readiness and telemetry loss; then selects rollback, roll-forward, repair, or containment from actual state. The correct action cannot be inferred from the word `rollback` in a runbook.

If telemetry is incomplete, use independent target state and mark diagnosis uncertainty. If data changed irreversibly, do not restore old code merely because it is available. If the wrong artifact was promoted but state remains compatible, restore the intended immutable path and validate business state, not only process health.

**Example qualification checklist**

An example is suitable for adaptation when:

- its accepted outcome and causal failure are explicit;
- target facts and illustrative assumptions are distinguishable;
- the existing mechanism and rejected scope are named;
- at least one plausible counterexample or degraded state is included;
- verification can fail for the intended reason;
- artifact, config, data, environment, and owner boundaries are visible;
- the result states what stronger claim remains unproved;
- no secret, threshold, deadline, service objective, provider guarantee, or command is invented as target policy;
- reroute and invalidation events are named;
- final acceptance includes business or operational state, not only command exit.

Adaptation record:

```text
example_family:
target_outcome:
scenario_assumptions_replaced:
target_mechanisms_and_owners:
states_removed_or_added:
counterexample_used:
verification_actions_and_results:
claims_supported:
claims_remaining_conditional:
route_changes:
invalidation_events:
```

Promote a recurring consequential example into a deterministic test, integration fixture, staged drill, or runbook scenario when the maintenance cost is justified. Keep the prose for rationale, alternatives, and boundaries. Retire or revise an example when versions, target architecture, provider semantics, policy, incidents, or accumulated adaptation evidence invalidate its causal model.

## Outcome Metrics and Feedback Loops

`outcome_metric_default`: Measure whether accepted runtime transitions become easier to deliver and safer to operate without weakening gates, artifact identity, data compatibility, signal quality, shutdown correctness, or recovery. Do not use a universal session limit, incident target, service objective, or refresh interval. Establish target-owned definitions and baselines before interpreting change.

A metric is complete only when it names the decision question, population, unit, event source, inclusion and exclusion rules, data quality, segmentation, interpretation, guardrail, owner action, and invalidation event. A dashboard value without an action path is telemetry, not a feedback loop.

**Balanced measurement map**

| measurement_area | decision_question | candidate_measure_definition | pair_with_guardrail | likely_owner_action |
| --- | --- | --- | --- | --- |
| accepted outcome coverage | Do requirements include normal, failure, degraded, shutdown, and recovery states activated by the change? | proportion or count of consequential transitions mapped to an owner and qualified gate within the defined change cohort | escaped state, unowned conditional claim, or unnecessary gate growth | add a missing contract or remove irrelevant scope before implementation |
| first discriminating feedback | How quickly does a change encounter a gate capable of exposing its primary defect class? | elapsed work time or pipeline path from accepted requirement to first qualified failure-capable gate, segmented by change type | gate escape, false pass, and developer waiting versus active work | move or narrow the gate; improve fixture or boundary isolation |
| gate qualification | Do new or changed gates fail for the defect they claim to block? | qualified gates with retained negative-control evidence over all materially changed gates in scope | flaky rate, no-op selection, mutation not representative, or unsafe injection | repair task selection, fixture, environment, or claimed coverage |
| deterministic gate health | Are fast configured gates reliable enough to guide changes? | pass, failure, rerun, flake, cache, duration, and diagnosis distributions by task and module | skipped work, changed filters, baseline suppression, and incident escape | isolate nondeterminism, fix ownership, split or retire low-value gates |
| artifact continuity | Does release promote the exact package that passed required gates? | releases with coherent source revision, build inputs, artifact digest, gate results, and environment promotion over releases sampled | mutable tags, environment rebuild, missing provenance, or substituted config | block promotion, repair lineage, and requalify affected releases |
| configuration safety | Are required and sensitive inputs failing at the intended boundary without disclosure? | startup failures and escapes classified by missing, malformed, denied, stale, or exposed input | false healthy state, secret-bearing output, restart loop, and manual production fix | strengthen binding, validation, redaction, provider integration, or runbook |
| migration compatibility | Do schema transitions preserve supported applications and historical data? | migrations exercised from supported prior states, mixed versions, and representative data, plus escaped incompatibilities | empty-database-only pass, partial state, lock or capacity impact, manual repair | add fixture or stage, split transition, improve stop and recovery |
| signal actionability | Do signals distinguish consequential failures and lead to correct owner action? | sampled or drilled failures whose signal reaches a consumer and results in the intended decision | privacy, cardinality, alert noise, telemetry loss, and wrong action | remove or refine signal, query, alert, ownership, or runbook step |
| health automation truth | Do readiness, liveness, startup, and degraded states cause safe platform behavior? | injected states where observed traffic and restart behavior match target policy | request failure hidden by green health or restart amplification | correct health contract, platform policy, startup window, or dependency treatment |
| staged release control | Do stages detect harm before wider exposure and support authorized stop? | releases with bounded stage evidence, explicit continue or stop decision, and retained recovery result | stage duration without evidence, missing owner, late signal, or recovery failure | change stage size, signals, stop conditions, authority, or gate placement |
| worker and shutdown reconciliation | Does termination leave every admitted item in a complete, retryable, released, or reconcilable state? | phase-interruption scenarios and observed terminations classified by final work and effect state | clean exit with unknown work, duplicate effect, stranded lease, or restart backlog | fix scope ownership, effect identity, drain, acknowledgment, or reconciliation |
| recovery effectiveness | Do responders restore accepted business, data, traffic, work, and signal state? | incidents and drills with preserved initial state, chosen action, final invariant, residual repair, and owner closure | process health only, reopened incident, hidden manual work, or customer state unresolved | update recovery choice, authority, automation, runbook, or system design |
| runbook usability | Can an authorized responder identify state and choose the correct next action? | reviewed, tabletop, isolated, staged, and incident paths with decisions, access gaps, hesitations, and corrections | fast command execution with wrong state, stale link, unowned step, or secret exposure | clarify decision boundary, repair access, rehearse, or retire obsolete action |
| temporary control burden | Are containment, dual states, compatibility paths, and manual checks being retired as promised? | age and usage of temporary controls relative to named exit evidence, segmented by consequence | expired owner, missing signal, growing manual effort, or permanent coexistence | complete durable fix, renew explicitly, narrow, or remove control |
| operational toil and cost | Is a mechanism shifting unreasonable recurring work or resource cost to operators? | bounded manual interventions, alert handling, failed deployments, reconciliation work, infrastructure use, and support effort | hidden contractor or platform work, user harm, or cost moved to another team | automate stable invariant, simplify mechanism, change ownership, or replace |
| evidence freshness | Are decisions still supported after relevant source and target changes? | consequential routes reviewed or rerun after named invalidation events | calendar review that misses change, stale public mapping, or target drift | selectively refresh authority and rerun dependent gates or runbooks |
| learning closure | Do incidents, drills, failed gates, and misroutes produce completed causal corrections? | learning actions tied to requirement, gate, runbook, owner, result, and retirement over closed events | action count without verified effect, repeated failure, or documentation-only closure | deepen diagnosis, change control, assign authority, or reject ineffective action |

These are candidate definitions, not a requirement to collect every row. Select the few measures that can change current decisions. If migration is absent, migration metrics add no confidence. If worker termination is the primary risk, final work state is more valuable than generic deployment frequency.

**Metric contract**

For each adopted measure, retain:

```text
metric_or_review_name:
decision_question:
owner_and_consumers:
population_and_change_cohort:
unit_and_event_definition:
numerator_and_denominator_if_applicable:
inclusions_and_exclusions:
source_systems_and_artifact_links:
segmentation:
baseline_or_initial_hypothesis:
target_owned_threshold_if_any:
data_quality_and_coverage:
privacy_and_retention:
guardrail_measure:
interpretation_limits:
action_for_expected_states:
collection_or_review_trigger:
invalidation_event:
retirement_condition:
```

If the numerator, denominator, event, or cohort changes, annotate the boundary rather than drawing one continuous trend. Separate source changes, deploys, migrations, incidents, drills, and manual interventions where their risk differs. Do not combine severity classes into an average that hides consequential failures.

**Metric qualification**

1. Trace the event from target action or state through collection, transformation, storage, query, display, and owner decision.
2. Inject a safe synthetic event or use a controlled drill. Confirm inclusion, classification, artifact linkage, timestamp semantics, and expected dimensions.
3. Reconcile a sample against independent source state, such as pipeline artifact records, database migration history, broker work state, or incident timeline.
4. Exercise missing, delayed, duplicate, reordered, and partially collected telemetry where those conditions are plausible.
5. Verify sensitive values are excluded or protected and high-variety dimensions are bounded.
6. Confirm the owner can perform the intended response and that the response changes the accepted outcome.
7. Record data coverage and stronger interpretations the metric cannot support.

Metric-pipeline failure must be visible. An empty alert stream or falling incident count is not improvement if collection, routing, classification, or reporting stopped.

**Feedback loops by event**

| event | immediate_feedback | deeper_review | durable_output |
| --- | --- | --- | --- |
| accepted requirement | check lifecycle states, owners, hard gates, and baseline availability | challenge scope and unsupported precision | requirement-to-gate map and explicit conditional claims |
| gate added or changed | preserve negative control and verify selection | inspect flakiness, cache, diagnosis, and CI placement | qualified gate record and owner |
| release | confirm artifact identity, stage signals, decisions, and final state | compare escaped defects, manual work, and conditional evidence | release evidence, gate correction, or runbook update |
| migration or stateful transition | observe prior state, progress, mixed versions, stop, and final invariant | inspect data profiles, locks, repair, and retirement of compatibility state | updated fixtures, transition contract, and recovery evidence |
| shutdown or worker change | interrupt consequential phases and reconcile work and effects | compare platform grace, workload distribution, duplicate and backlog behavior | lifecycle test, signal, or ownership correction |
| incident | preserve state, contain, recover, and classify earliest break | test causal model, controls, signals, authority, and runbook | verified corrective action, retired ineffective action, and changed route |
| drill | record decision accuracy, access, action, state, and gaps | qualify untested provider or recovery assumptions | runbook correction, access repair, or staged rehearsal plan |
| dependency, framework, or platform change | identify dependent claims and gates | refresh applicable authority and compatibility evidence | selective rerun and invalidated decision record |
| recurring manual intervention | classify why automation or design did not handle the state | compare control, mechanism, ownership, and replacement costs | automation, simplification, accepted runbook, or explicit risk decision |

Use calendar review only as a backstop for silent drift. Event-driven triggers are stronger because they follow the conditions that actually invalidate runtime evidence.

**Interpretation and anti-gaming guardrails**

- Faster requirement-to-pass time is not an improvement if the first discriminating gate moved later, was skipped, or production escapes rose.
- More tests are not better if they repeat one failure model, increase flakiness, or do not run on the promoted artifact.
- Fewer incidents can reflect lower exposure, changed reporting, missing telemetry, or merged severity; inspect denominators and coverage.
- Shorter recovery time can hide premature closure, unresolved customer state, manual repair shifted to another team, or data reconciliation after the clock stops.
- Fewer alerts can reflect better signals or broken routing. Validate with controlled failure and consumer readback.
- Higher deployment frequency is not a safety result. Pair it with artifact continuity, stage control, escapes, and recovery.
- Lower operational cost can shift risk to security, data, support, or future migration. Track material transfers.
- A favorable aggregate cannot override one hard failure involving secret exposure, incompatible data, wrong artifact, unsafe traffic, or unrecoverable effects.

When a metric becomes a target, review incentives. Ask what behavior could improve the number while worsening the accepted runtime outcome. Add the smallest guardrail or replace the measure if gaming dominates its decision value.

**Worked feedback examples**

Good flow measure: compare changes within the same runtime class from accepted requirement to first qualified failing gate, then to all required evidence. Segment config, migration, package, and worker changes. Pair speed with escaped state and rerun burden. If config feedback improves because binding tests move earlier while escapes remain stable, the team has a plausible process improvement.

Bad flow measure: require every endpoint or worker change to finish in one session. Developers split work artificially, skip production-like gates, or avoid difficult migrations so the measure looks healthy. The time limit has no workload or risk basis.

Good gate-efficacy loop: a migration gate is added after a historical-row failure. The team preserves a failing fixture, confirms the gate detects it, runs supported prior states and production dialect, links it to CI, and monitors whether similar defects escape. If the fixture stops representing target history, the gate is revised rather than counted forever.

Bad incident metric: count incidents without severity, exposure, release count, detection coverage, reopened state, or manual repair. A quieter reporting channel appears safer even while duplicate worker effects continue.

Conditional trend: three staged worker rehearsals show clean reconciliation, but production terminations are rare and provider-forced kills were not exercised. Report evidence for those rehearsal states and name the missing provider scenario. Do not infer a general shutdown failure rate.

Good runbook loop: a tabletop reveals responders cannot distinguish telemetry loss from service recovery and lack permission for the documented stop action. The team adds an independent state check, repairs role access, and reruns the scenario. The useful outcome is corrected decision capability, not the number of runbooks reviewed.

**Feedback action record**

```text
signal_or_review:
observed_population_and_period:
data_quality_and_limits:
artifact_and_environment_scope:
hypothesis:
counter_hypothesis:
owner_decision:
action_taken:
expected_change_and_guardrail:
verification_result:
unintended_effect:
control_or_guidance_updated:
next_trigger:
retirement_or_reversal_condition:
```

Close the loop only after the action's intended outcome and guardrail are checked. Publishing a dashboard, opening an action item, or editing a runbook is intermediate work.

**Measure lifecycle**

Introduce a measure to answer a named question. Qualify its data path, collect enough representative evidence for the intended decision, and review incentives and costs. Narrow or segment it when aggregation hides causal differences. Replace it when a better direct state becomes available. Retire it when the question is resolved, the mechanism disappears, no owner acts on it, or collection harm exceeds value.

Use incident and drill evidence to convert recurring surprises into earlier requirements, gates, platform controls, or runbook decisions. Preserve rare-event scenarios for hazards that cannot be inferred from averages or injected safely in production. A mature feedback system should reduce ambiguity and unowned recovery work, not merely increase the number of measurements.

## Completeness Checklist

Use this checklist at a decision or handoff boundary. It does not make every row mandatory for every task. Activate rows from changed lifecycle states and plausible consequences, then record exclusions explicitly.

**Status semantics**

| status | meaning | required_record | effect_on_claim |
| --- | --- | --- | --- |
| pass | required evidence was observed at the fidelity needed for the bounded claim | artifact, environment, action, result, reviewer or owner, and invalidation event | claim may proceed within stated scope |
| conditional | available evidence supports only part of the claim or an owner/environment remains unavailable | passed subset, missing boundary, consequence, owner, and exact next gate | block only the stronger claim that depends on missing evidence |
| not_applicable | the state transition or consequence cannot occur in the accepted scope | absent boundary, target fact proving absence, and reviewer | exclude the row; reopen if scope or mechanism changes |
| fail | evidence contradicts a hard gate or accepted state | earliest causal failure, preserved state, containment or next action, and owner | stop dependent action until resolved or explicitly accepted by authority |
| inconclusive | evidence cannot be interpreted because of flakiness, contamination, telemetry loss, or ambiguous state | uncertainty source, affected claim, isolation action, and owner | do not grant dependent readiness |

Do not compute an overall percentage. One failed secret, data, artifact, traffic, effect, or recovery invariant is not canceled by many passing prose checks. A conditional item partitions claims; it does not become a medium score.

**Reference artifact integrity**

| check | completion_criterion | evidence_or_failure |
| --- | --- | --- |
| original structure | all 26 original Markdown headings remain exact and ordered with no added heading-like lines | deterministic heading comparison against the archive seed |
| section expansion | every evolved section is strictly longer than its matching seed and adds relevant causal, boundary, alternative, example, verification, uncertainty, and second-order content | per-section length and skeptical content review; raw length alone is insufficient |
| packet contract | 26 packet sections contain the ten exact questions and six mandatory fields each | structural counter reports 26 sections, 260 questions, and 1,560 fields |
| packet uniqueness | all mandatory values remain distinct before and after Section and Question context prefixes are stripped | exact and normalized uniqueness verifier reports 1,560 unique values |
| source fidelity | frozen paths, headings, hashes, facts, and historical dates match inspected local sources | source map and hash comparison; no current external claim from unrefreshed links |
| Markdown integrity | tables have consistent columns and fences are closed without accidental headings inside code examples | structural Markdown check plus rendered or parser review where available |
| text hygiene | output is ASCII, has no trailing whitespace, banned unresolved markers, malformed tables, or duplicate generic filler | focused verifier and explicit scans |
| focused verification | repository's file-focused evolution verifier passes for this exact reference | retained command, exit status, and relevant output |
| complete reread | packet and reference are reread in bounded groups with persisted review checkpoints and corrections | journal evidence for all sections, including final skeptical pass |

The reference artifact gate proves the document contract, not a future Kotlin application's production readiness.

**Route and decision completeness**

- The accepted outcome names normal, degraded, failed, shutdown, and recovered states that matter, plus affected users, operators, and owners.
- The target repository, service, module, source revision, package, and environments are identified without guessing.
- Project and directory instructions, wrapper, effective versions, framework mode, compiler plugins, config, migrations, telemetry, package, CI, deployment, and runbook are inspected only as activated.
- The route mode is explicit: runtime lead, support, incident-first, review-only, exploratory, route-away, or stop-and-escalate.
- Changed and deliberately unchanged lifecycle transitions are listed; no unrelated framework, build, telemetry, or platform migration is smuggled into scope.
- Local source roles are claim-specific, complete relevant regions were read, and companion files open only for owned boundaries.
- External links remain historical leads unless a current claim was refreshed under authorization with version and retrieval evidence.
- Alternatives include preservation and the smallest feasible adaptation; hard gates and transition costs are visible.
- Owner judgments, measured facts, local doctrine, refreshed external facts, synthesis, forecasts, and observed results are labeled separately.
- Reroute, split, stop, and invalidation events are named.

**Build, dependency, and artifact completeness**

- Repository wrapper and configured tasks are used; a globally installed substitute is not treated as equivalent.
- Effective Kotlin, Java, framework, coroutine, compiler-plugin, driver, migration, telemetry, and relevant transitive versions are resolved where they affect the claim.
- Version or tool changes are explicitly accepted upgrades rather than incidental side effects.
- Configured formatting and analysis gates support only their actual claims; style success is not runtime evidence.
- A clean build or package action produces an identified artifact with known inputs and relevant contents.
- CI executes the mapped changed boundaries and deliberately fails for a representative defect when the gate is new or changed.
- Source revision, gate results, artifact digest, promotion, and deployment refer to the same intended bits or an equivalent target-owned immutable contract.
- Caches, filters, skipped tasks, profiles, generated code, and test source sets do not create a no-op pass.

**Configuration, secret, and profile completeness**

- Raw config is bound and validated at an owned boundary; business behavior receives typed values rather than ambient string lookups.
- Valid, absent, malformed, boundary, unknown, and restart cases exercise the actual binding and packaged startup path.
- Environment differences are declarative capabilities or settings, not hidden branches on environment names.
- Secret storage, identity, access, injection, use, redaction, rotation, revocation, and exposure recovery follow target policy.
- Non-production canary values verify logs, errors, traces, health, dumps, and serialized config do not disclose sensitive material.
- Denied and missing secret access produces the intended state without restart amplification or unsafe fallback.
- Effective profiles and required keys are documented from target behavior, and production-like injection is exercised when deployment changes.
- Unknown provider, dynamic refresh, or rotation behavior is marked conditional rather than inferred from local startup.

**Data and migration completeness**

- The invariant, supported prior schema and application states, consumers, historical data profile, dialect, and migration owner are explicit.
- Versioned migrations preserve the repository's target mechanism and do not casually rewrite applied history.
- Empty-database success is supplemented by representative prior states and rows when existing data is possible.
- Old and new application versions are exercised in allowed sequences across every intermediate schema state required by rollout.
- Partial application, retry, lock or resource behavior, invalid legacy data, backfill or remediation, and final invariants are covered where plausible.
- Rollback, roll-forward, repair, replay, or containment is chosen from actual data and effect state, not named generically.
- CI and release stages run the migration gates that protect their claimed boundary, and production-scale limits are explicit.
- Contract removal waits for verified consumer retirement and compatibility evidence.

**Signal, health, and operational objective completeness**

- Each new or relied-upon log, metric, trace, audit, dashboard, or alert answers a failure question and maps to a consumer action.
- Dimensions are bounded; sensitive or user-controlled values are excluded or protected according to policy.
- Success, target failure, cancellation, degraded dependency, and telemetry loss are exercised through ingestion and query where the claim depends on them.
- Service objectives and thresholds come from target ownership and measured semantics; no illustrative value is promoted to policy.
- Startup, readiness, liveness, degraded, intake, drain, traffic, and restart states are distinguished according to framework and platform behavior.
- Dependency failure does not trigger restart amplification unless restart is the proven recovery action.
- Actual request or work behavior is observed alongside health status.
- Signals show artifact, config, data, and work correlation sufficient for bounded diagnosis without exposing private material.

**Package, CI, release, and platform completeness**

- Package or image inputs, runtime, architecture, effective user, files, ports, permissions, resources, certificates, and startup are inspected as relevant.
- Least privilege and deterministic contents are demonstrated or deviations have owner-approved reasons and gates.
- Representative config starts the packaged artifact; missing input, dependency delay, signal initialization, and resource pressure are exercised when activated.
- Fast pull-request and longer integration gates have explicit ownership, timing, artifact relationship, and release policy.
- Release stages define artifact, scope, observation, continue and stop conditions, owner authority, and recovery before traffic or work changes.
- Managed identity, secret injection, health, traffic, termination, and restart behavior are exercised in an authorized target-like environment when claimed.
- Inaccessible platform behavior creates a conditional deployment claim and precise handoff, not a fabricated pass.
- Failure evidence and diagnostics remain available long enough for diagnosis and recovery.

**Worker, shutdown, and recovery completeness**

- Work acquisition, admission, scope ownership, processing, external effect, durable completion, acknowledgment, drain, termination, restart, and recovered states are modeled where they exist.
- Cancellation and one total deadline propagate through owned coroutine and blocking boundaries.
- Durable work and effect identity support accepted retry, duplicate suppression, or reconciliation semantics.
- Termination is injected before and after consequential ownership and effect transitions, not only during idle operation.
- Admission stops before drain; unfinished identities and phases remain discoverable at deadline.
- Resources, leases, locks, connections, executors, and telemetry are released or intentionally transferred.
- Restart detects pending, expired, duplicate, and ambiguous attempts and reaches an accepted final business state.
- Recovery is verified through work, data, external effects, traffic, signals, and owner action, not process health alone.
- Temporary containment has monitoring, owner, duration condition, durable correction, and retirement evidence.

**Runbook and handoff completeness**

- The runbook binds target and release identity, compatible states, prerequisites, access, baseline, stages, signals, stop authority, recovery, verification, escalation, evidence, limits, and invalidation events.
- Commands or automation are target-owned, versioned, effect-described, access-controlled, and rehearsed at the required fidelity.
- Service-objective breach and telemetry failure paths lead to state checks and authorized decisions.
- Rollback is rejected when data, messages, caches, or external effects make the prior artifact incompatible.
- Tabletop, isolated drill, staged rehearsal, or incident evidence supports consequential paths; unqualified actions are labeled.
- Role-based ownership is current and does not depend solely on one person's memory.
- Residual risk, unsupported versions, inaccessible environments, and manual repair are visible.
- Another engineer or operator can reproduce the evidence and understand what to inspect or undo next.

**Phase profiles**

At design handoff, require accepted states, target stance, alternatives, hard gates, planned evidence, owners, and conditional boundaries. Implementation completion additionally requires deterministic and affected integration evidence plus package identity. Release review requires artifact continuity, compatibility, target-like lifecycle, stop authority, and runbook. Incident closure requires preserved initial state, causal model, containment, recovered business state, regression evidence, runbook correction, and residual owners.

During an active incident, use a minimal immediate subset: authority, target state, artifact, config, data, traffic, signals, containment effects, recovery options, and evidence preservation. Complete the remaining checklist after risk is bounded.

**Skeptical completion review**

Before declaring complete, ask:

1. Which row was hardest to prove, and did the route weaken the claim instead of fabricating evidence?
2. Which apparently passing gate could be a no-op, wrong artifact, unrealistic fixture, or telemetry illusion?
3. Which state exists only in production or another owner's platform, and is its handoff precise?
4. What counterexample would reverse the chosen mechanism or recovery action?
5. Can any not-applicable row actually occur through a transitive dependency, worker, old consumer, or platform override?
6. Does a green process hide wrong data, work, traffic, external effect, or customer state?
7. Is any temporary path missing an owner or retirement event?
8. Did a source label substitute for target applicability or current authority?
9. Would a responder know what not to do when state is ambiguous?
10. Can a changed dependency, artifact, config, migration, signal, platform, owner, or incident selectively invalidate this evidence?

Qualify this checklist by sampling evidence, replaying representative negative or degraded scenarios, checking the promoted artifact, and tracking escaped consequential states. Update it from recurring escapes and conditional items. Promote stable deterministic invariants into automation; retire manual rows only when stronger controls preserve coverage and diagnosis.

## Adjacent Reference Routing

`adjacent_reference_guidance`: Keep one accepted outcome and one lead owner. Route a named uncertainty to the smallest adjacent source or authority that owns it, then reconcile the returned decision with artifact, configuration, data, traffic, shutdown, and recovery state. Do not load another reference merely because it shares a keyword.

**Frozen local reference routes**

Paths are relative to `agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/references/` and remain historical orientation sources.

| adjacent_local_source | route_when | question_it_should_answer | minimum_handoff | return_to_runtime_with |
| --- | --- | --- | --- | --- |
| `reference-map.md` | the task mode or first read order is unclear | Which historical Kotlin backend mode and source sequence best matches the accepted outcome? | outcome, target surface, candidate risks, and known owners | selected route, alternatives rejected, and uncertainty still unresolved |
| `kotlin-backend-playbook.md` | service anatomy, requirements, DTO/domain/persistence separation, errors, transactions, coroutine boundaries, external clients, workers, or API contracts lead | What application boundary and invariant own the behavior that runtime operations must preserve? | accepted behavior, target framework and storage stance, runtime transition, failure example | interface contract, ownership, transaction or work boundary, and tests needed at runtime edges |
| `kotlin-spring-ktor-idioms.md` | Spring or Ktor configuration, lifecycle, serialization, route, controller, proxy, plugin, status, persistence, or test mechanism is uncertain | Which target-framework extension point implements the accepted behavior without switching stance? | resolved framework and version, current mechanism locator, requirement, and lifecycle interface | version-bounded mechanism, integration constraints, target code location, and framework-specific gate |
| `kotlin-backend-testing-and-fixtures.md` | a unit, framework, coroutine, persistence, contract, property, or real-dependency gate must be selected | What is the lightest faithful test surface capable of failing for this runtime defect? | requirement, failure class, target task discovery, dependency fidelity, artifact claim | fixture, test type, negative control, result interpretation, and production-like gap |
| `kotlin-backend-security-and-resilience.md` | trust, auth, validation, blocking, cancellation, retry, idempotency, client, or background-work semantics lead | What trust or repeated-effect contract must config, release, shutdown, and recovery preserve? | identities, data or effect, timeout and retry path, failure state, target policy | threat or effect boundary, accepted outcome, disallowed state, owner, and executable scenario |
| `sources-and-research-brief.md` | provenance of frozen doctrine or historical public discovery leads must be reconstructed | Was this statement recorded as source fact, synthesis, or candidate guidance, and where could a future refresh begin? | exact claim, local source region, target version question, and authorized research scope | dated provenance, source role, candidate authority, and explicit currentness gap |

Do not route from this runtime reference to itself. Open the complete relevant region rather than passing an isolated bullet stripped of caveats.

**Target and external authority routes**

| receiving_owner_or_authority | route_when | runtime_interface_to_preserve | evidence_required_on_return |
| --- | --- | --- | --- |
| repository or service owner | target stance, scope, accepted behavior, ownership, or compatibility policy is unclear | changed and unchanged lifecycle boundaries plus proposed evidence | approved requirement, mechanism ownership, support range, and decision constraints |
| product or domain owner | duplicate, loss, degraded behavior, latency, downtime, or recovery has business meaning | observable business state and consequence separate from implementation | accepted normal, failure, partial, and recovered states plus risk decision |
| security or identity owner | secrets, permissions, data disclosure, auth, audit, break-glass, or exposure response changes | package, config, signal, release, and recovery interfaces | applicable policy, effective authority, denied and exposure scenarios, containment and residual risk |
| database or data owner | dialect, migration, lock, historical data, backup, repair, retention, or destructive action is consequential | application compatibility, artifact order, signals, stop, and recovery | supported states, operation procedure, data evidence, capacity or lock limits, and authorized recovery |
| broker or external-system owner | acknowledgment, lease, idempotency, timeout, quota, ordering, duplicate, or reconciliation semantics are uncertain | worker ownership, cancellation, signal, shutdown, restart, and effect identity | version and mode, supported contract, failure semantics, observable state, and sandbox or staged result |
| CI or artifact-platform owner | runner, cache, permission, provenance, registry, promotion, signing, or retention is controlled elsewhere | repository gates, intended artifact, environment config, stage and recovery requirements | effective workflow, artifact identity chain, access boundary, deliberate failure, and promotion evidence |
| runtime or deployment-platform owner | image, identity, resources, health, traffic, termination, restart, secret injection, or rollout policy is platform-owned | packaged application startup, readiness, signals, drain, and accepted recovery | applicable platform policy, exact mechanism, staged state transitions, stop authority, and limits |
| telemetry or incident-tooling owner | collector, exporter, query, dashboard, alert, paging, retention, or telemetry failure is outside the service | bounded signal semantics, privacy, correlation, health, and runbook decision | end-to-end signal path, consumer action, loss behavior, access, cost, and drill result |
| incident command | active harm spans services, owners, or shared infrastructure | service artifact, config, data, traffic, work, signal, containment constraints, and recovery options | authority decisions, common timeline, containment state, handoff, and closure criteria |
| current primary documentation | a version-sensitive language, library, framework, database, tool, or provider fact remains unresolved and browsing is authorized | exact target coordinate, mode, claim, and consequence | retrieved source, version selector, date, bounded fact, exceptions, conflict, and target scenario |

An external authority explains supported mechanism behavior. It does not replace target policy or observed outcome. A target owner can define policy but cannot make incompatible bits, data, or provider behavior work; conflicts require evidence and escalation.

**Routing protocol**

1. State the accepted outcome and current lead. If neither is clear, route first to requirements or ownership rather than a technology document.
2. Name one unresolved interface question. Examples: `When is this broker item durably acknowledged?` or `Which platform state removes traffic before drain?`
3. Identify who owns that behavior. Prefer target implementation and policy for what is used; use specialist local doctrine for questions; use current primary authority for version-sensitive semantics when authorized.
4. Send the smallest access-safe handoff: revision, artifact, mechanism, state, observed failure, requirement, evidence already run, and exact decision requested.
5. Preserve sensitive material by locator and access boundary. Do not paste raw credentials, private payloads, or an unbounded incident transcript.
6. Require the receiving route to return a decision, evidence, unresolved limit, owner, and event that changes the answer.
7. Reconcile the result with adjacent runtime states. A database answer can change rollout and recovery; a framework lifecycle answer can change shutdown and health.
8. Rerun the affected gate or scenario. A handoff response is not implementation evidence.
9. Record whether the route resolved the uncertainty, exposed another owner, or invalidated the causal model.
10. Stop routing when the accepted decision has sufficient authority and evidence. More context is not completion.

**Minimum handoff record**

```text
handoff_id:
accepted_outcome:
lead_route_and_owner:
target_revision_and_artifact:
effective_mechanism_and_version:
observed_state_or_failure:
unresolved_interface_question:
why_receiving_route_owns_it:
evidence_already_available:
constraints_and_sensitive_boundaries:
decision_or_action_requested:
required_return_evidence:
urgency_and_stop_condition:
return_recipient:
reroute_or_invalidation_event:
```

**Routing examples**

Worker composition: a termination defect leaves external effects ambiguous. Runtime operations remains lead for package, signals, platform termination, restart, and recovery. The playbook answers scope and worker ownership; security and resilience answers idempotency and retry; the broker owner answers lease and acknowledgment; testing supplies phase interruption. Each returns a bounded contract that the packaged shutdown scenario reconciles.

Migration composition: a new invariant changes database schema. Persistence and domain design lead the invariant and transaction. Runtime operations leads migration, old/new coexistence, CI, staged release, signals, stop, and recovery. The database owner supplies dialect, lock, and repair authority. Framework reference joins only if persistence integration behavior is uncertain.

Secret route: a config change adds a credential. Runtime operations leads typed startup and redacted operational surfaces; security owner leads identity, access, rotation, revocation, and exposure policy; framework guidance supplies binding; platform owner supplies secret injection. A generic environment-variable recommendation cannot replace any of those contracts.

Health handoff: application readiness passes locally, but managed traffic still reaches an instance during drain. The framework reference can establish local lifecycle integration, while the platform owner must establish probe, traffic, and termination ordering. Runtime operations reconciles both through staged requests and shutdown evidence.

Route away: a library author asks about a sealed Kotlin result type with no service artifact, config, data, release, or operational lifecycle change. Route to language or application design and do not retain runtime operations as lead.

Current-authority route: a compiler plugin upgrade changes framework proxy behavior. Frozen corpus identifies the question; target resolution identifies versions; authorized current Kotlin and framework authority supplies compatibility; target compile, package, and proxy scenarios establish adoption.

Incident route: a provider outage causes readiness churn across services. Incident command owns common containment and risk decisions. Each service returns artifact, traffic, dependency, and health evidence. Runtime reference does not independently change platform policy during shared response.

Borderline route: latency after an upgrade could arise from coroutine dispatch, database pool, telemetry exporter, or resource limits. Send no broad handoff yet. Gather resolved versions, traces, pool and resource state, and one controlled workload. Route to the owner selected by the first discriminating evidence, while preserving the other hypotheses.

**Anti-loop and quality rules**

- A route may return to a prior owner only when new evidence invalidates an earlier assumption; record the delta.
- Two references cannot both lead the same decision. Split outcomes or name one interface owner.
- Avoid `review everything` handoffs. State the exact state transition and requested decision.
- A receiving route must not change unrelated mechanisms to make its local solution easier.
- Target commands and production actions remain subject to access and owner authority; a document handoff grants none.
- If no owner accepts a consequential boundary, stop and escalate rather than routing indefinitely.
- If repeated routes always travel together, consider a stable interface checklist or composed gate rather than larger prose bundles.
- If a route produces no decision or evidence after a bounded attempt, reassess the objective and causal model.

Review routing quality from repeated work: uncertainty resolved, context required, reroutes, unowned boundaries, evidence yield, and post-handoff escapes. Organize durable routes around state ownership such as artifact, data, identity, traffic, work, and recovery, not around personal names. Retire paths when architecture, source ownership, or platform policy changes.

## Workload Model

`combined_evidence_inference_note`: Treat Kotlin Backend Runtime Operations as a backend service operating reference, not as a prose summary.

The seed's limits of one service boundary, twenty-five endpoints or workers, one thousand representative requests, and one rollback path have no target baseline or cited operational rationale. They are quarantined as unsupported scoping choices. Endpoint count and request count alone do not model concurrency, payload, data history, dependency delay, worker ownership, resource saturation, deploy transitions, or recovery.

Build a target workload envelope from observed, forecast, synthetic, and adversarial profiles. Label each source. A synthetic profile can prove a deterministic state transition; it cannot establish production capacity unless its distribution, environment, and limiting resources are representative.

**Workload dimensions**

| dimension | describe | why_it_changes_runtime_behavior | evidence_source_or_scenario |
| --- | --- | --- | --- |
| operation mix | routes, commands, queries, scheduled jobs, messages, callbacks, and administrative actions plus their relative occurrence | different paths use distinct CPU, memory, database, client, serialization, and effect boundaries | sanitized target traces, counters, job history, and accepted forecast |
| arrival shape | steady flow, burst, ramp, batch boundary, synchronized schedule, redelivery wave, or user-driven spike | queues, pools, autoscaling, retries, caches, and deadlines respond differently to temporal concentration | timestamp distribution, scheduled-work policy, controlled generator profiles |
| concurrency | active requests, coroutines, worker slots, partitions, leases, transactions, and downstream calls | contention and ownership failures can appear before aggregate volume is high | in-flight signals, pool state, broker or store state, staged concurrency sweep |
| payload and response shape | size, field count, nesting, compression, attachments, streaming, and error bodies | memory, serialization, network, logging, validation, and timeout costs can be nonlinear | privacy-safe distributions, boundary fixtures, streaming and malformed cases |
| data history and skew | row counts, null or legacy values, tenant or key skew, index selectivity, hot partitions, schema versions, and backfill state | migrations, queries, locks, caches, and invariants depend on prior data, not just new writes | sanitized profiles, production-dialect fixtures, generated edge distributions |
| database behavior | query mix, transaction duration, isolation, lock contention, connection use, replicas, and DDL or migration state | latency, deadlocks, capacity, retry, and rolling compatibility depend on engine state | database signals, query plans where authorized, integration and migration scenarios |
| external dependency behavior | connection setup, latency distribution, quota, error classes, partial response, cancellation, idempotency, and outage | total deadlines, retries, resource retention, duplicate effects, and degraded mode are cross-system | provider sandbox or simulator, client telemetry, fault injection, authority documentation |
| worker and queue state | backlog, age, priority, lease or visibility, attempts, duplicates, poison work, dead letter, and acknowledgment | throughput alone can hide starvation, stuck ownership, retry storms, and unreconciled effects | broker or store metrics, work ledger, controlled phase interruption and restart |
| cache and warm state | cold or warm code, data, connection, DNS, certificate, JIT, page, and application caches | startup, first request, deploy, memory, and tail behavior differ from steady state | explicit cold/warm runs, cache state record, package restart scenario |
| resource envelope | CPU, memory, thread and dispatcher use, file descriptors, connections, disk, network, ephemeral storage, and platform limits | saturation can amplify latency, health failure, restarts, and data or work loss | package and platform resource signals, bounded stress and recovery run |
| configuration and profile | effective timeouts, pools, worker limits, batching, retries, feature contracts, logging, and environment inputs | config changes transform the workload admitted to dependencies and resources | typed config record, effective profile, comparative startup and scenario evidence |
| artifact and topology | source revision, package digest, JVM, architecture, instance count, region, replica, shard, and deployment strategy | different bits and topology invalidate comparisons and alter failure domains | CI provenance, deployment state, artifact inventory, target platform record |
| lifecycle transitions | cold start, readiness, rollout, mixed versions, drain, termination, restart, failover, migration, and recovery | the service can fail during state change even when steady-state throughput is acceptable | staged lifecycle scenarios, incident timelines, runbook drills |
| failure and retry interaction | local errors, dependency errors, timeouts, cancellation, retry, fallback, circuit or shedding behavior | load can multiply through retries or transfer to queues and recovery work | injected failure classes, total-attempt accounting, downstream and backlog signals |
| observability overhead | log, metric, trace, audit volume, sampling, exporter queues, cardinality, and telemetry outage | diagnostics consume resources and can fail precisely during peak or incident state | telemetry pipeline signals, controlled signal volume, disabled or degraded comparison |
| security and identity path | authentication, authorization, token or secret retrieval, encryption, audit, and denied access | identity providers and cryptography add dependencies, latency, caching, and failure states | target policy, safe test identities, denied and rotation scenarios |
| final business state | accepted result, duplicate tolerance, data invariant, work completion, customer-visible state, and reconciliation | a fast process can still produce wrong or ambiguous external outcomes | invariant checks, effect lookup, reconciliation ledger, owner validation |

Do not collect sensitive raw traffic merely to increase realism. Preserve distributions and relationships needed for the decision, redact or synthesize content, follow retention policy, and document what sanitization removes.

**Representative profiles**

| profile | purpose | characteristic_state | claims_it_can_support |
| --- | --- | --- | --- |
| functional_minimum | expose deterministic behavior with the smallest state | one or a few operations chosen to cross the changed boundary | parsing, validation, state transition, cancellation, migration syntax, or effect ordering |
| typical_observed | represent common operation and data distributions | sanitized baseline under a named artifact, config, and environment | behavior and resource observations within that sampled envelope |
| peak_observed | reproduce a documented high-demand range without extrapolation | target-derived concurrency, mix, and resource pressure | bounded peak behavior and limiting resource for the observed range |
| burst_or_wave | test temporal concentration, scheduled work, redelivery, or retry amplification | rapid arrivals or backlog release with controlled duration and state | queue, pool, shedding, retry, health, and recovery transitions |
| tail_and_edge | exercise large, skewed, legacy, malformed, slow, or rare inputs | selected distribution extremes and historical exceptions | correctness and resource effects for explicit edge classes |
| cold_start | exercise uncached package and dependency initialization | new process, empty local caches, connection setup, config and secret access | startup, readiness, first-operation, and resource behavior under recorded conditions |
| degraded_dependency | distinguish slowdown, partial response, quota, denial, and outage | controlled dependency impairment with target client semantics | timeout, cancellation, retry, fallback, signal, health, and recovery behavior |
| migration_and_mixed_version | exercise data and application coexistence | supported prior schema, historical rows, old and new artifacts, partial transition | compatibility, migration, rollout, stop, repair, and contract-retirement decisions |
| rolling_release | exercise changing instance and artifact mix under traffic or work | staged replacement with one immutable artifact identity per version | readiness, traffic, compatibility, signal, stop, and promotion behavior |
| drain_and_termination | interrupt active requests and work at consequential phases | admission stop, in-flight identities, deadline, forced and graceful paths | cancellation, resource release, work ownership, effect safety, restart |
| restart_and_recovery | begin from pending, expired, partial, duplicate, or degraded state | same or recovered artifact plus retained external state | reconciliation, backlog recovery, invariant restoration, and runbook action |
| exploratory_stress | find first limiting resource and nonlinear failure without claiming a target objective | controlled increase beyond known envelope in an isolated environment | bottleneck hypotheses, failure shape, and follow-up test design |
| sustained_stability | reveal leaks, drift, queue accumulation, cache behavior, and telemetry loss | representative profile over a duration justified by the suspected mechanism | stability within observed duration; no universal long-term guarantee |

Activate profiles from the changed claim. A config parser does not require peak load. A worker drain change requires phase interruption even if throughput is low. A schema index change may require historical skew and lock behavior more than endpoint breadth.

**Method selection**

| method | strength | weakness | use_for |
| --- | --- | --- | --- |
| deterministic unit or state test | repeatable and easy to localize | omits framework, driver, network, package, and platform behavior | invariants, config parsing, cancellation ownership, state transitions, edge values |
| framework or component test | exercises real binding, serialization, lifecycle, or adapter integration | may replace external systems and package state | route or controller behavior, framework startup, local health, client adaptation |
| production-dialect or real-dependency fixture | captures engine, driver, broker, or protocol behavior | costs more and may still differ from managed target | migrations, transactions, acknowledgments, timeouts, retries, integration |
| sanitized replay | retains realistic operation timing and distributions | can reproduce historical bias, sensitive relationships, and no novel state | regression under known target patterns after privacy review |
| parameterized synthetic load | controllable and reproducible across edge profiles | realism depends on model quality and generator capacity | bursts, concurrency sweeps, payload bounds, stress, resource and recovery behavior |
| fault and lifecycle injection | directly exercises degraded, shutdown, restart, and partial states | can be unsafe and environment-specific | failure amplification, health, cancellation, effects, runbook, recovery |
| bounded staged observation | includes real platform identity, traffic, topology, and dependencies | higher consequence, access, cost, and confounding factors | final platform claims under owner-approved stop and recovery conditions |
| analytical bound or capacity model | cheap exploration of constraints and sensitivity | relies on assumptions and may omit nonlinear interactions | planning experiments, identifying likely pools, budgets, and bottlenecks |

Combine methods when they answer different uncertainty classes. Do not run a large synthetic load to compensate for missing cancellation or migration-state tests.

**Workload qualification protocol**

1. State the runtime claim, plausible failure, and final accepted business state.
2. Identify the target artifact, config, topology, data state, dependencies, and lifecycle state represented.
3. Classify inputs as observed, forecast, synthetic, adversarial, or provider-defined. Preserve source and date or version.
4. Select dimensions that can affect the claim. Record deliberately omitted dimensions and why they cannot change the result.
5. Define operation mix, arrival, concurrency, payload, data, failure, and lifecycle profile without inventing target thresholds.
6. Calibrate the generator or fixture. Observe its own CPU, memory, network, timing, queue, dropped samples, and retry behavior.
7. Establish baseline and negative control. Confirm the scenario crosses the intended boundary and the evidence pipeline sees it.
8. Run repeatable trials appropriate to the claim. Reset or record caches, data, connections, clocks, and external state between comparisons.
9. Observe requests or work, errors, latency distribution where relevant, resource saturation, pools, dependency state, health, retries, telemetry, and final invariants.
10. Let the system recover. Record backlog clearance, resource release, restart, data and effect reconciliation, and any manual action.
11. Report observed envelope and first limiting mechanism. Do not extrapolate beyond tested state without a labeled model and uncertainty.
12. Link material workload changes to selective reruns of config, pool, timeout, health, migration, shutdown, and runbook evidence.

**Environment and measurement controls**

- Keep artifact, JVM, architecture, config, data, topology, dependency mode, and generator version stable across comparisons unless that dimension is under test.
- Separate cold and warm observations. State which caches, pools, code paths, and connections were reused.
- Pace or generate input according to the profile; a client blocked waiting for responses may underproduce the overload condition being investigated.
- Account for retries and redirects as additional work, not as invisible implementation detail.
- Observe the generator, network, telemetry collector, database, broker, and external simulator for their own saturation and loss.
- Use synchronized clocks or causal identifiers where ordering matters; record clock uncertainty.
- Isolate data and external effects and clean them safely. Verify cleanup rather than assuming it.
- Avoid real credentials and private payloads. Use policy-approved synthetic identities and sanitized distributions.
- Preserve failures and final state. Throughput without correctness and recovery is incomplete.

**Worked workload examples**

Config example: one packaged startup each for valid, missing, malformed, and denied-secret inputs can be sufficient to prove deterministic binding behavior. Repeating one thousand successful starts adds little. Provider rotation and burst restarts remain separate operational profiles.

Migration example: a small fixture containing every relevant historical shape can expose a constraint failure that a much larger empty database cannot. Add target-scale and skew profiles only for lock, duration, storage, or capacity claims. Exercise mixed versions and partial transition regardless of row count when rolling deployment is accepted.

Worker example: interrupt a single item before and after acquisition, external effect, completion record, and acknowledgment to prove ownership semantics. Then use representative concurrency, work duration, backlog, and platform grace to test drain capacity. Correctness and capacity are distinct claims.

Health example: steady successful traffic cannot show whether liveness amplifies a dependency outage. Inject dependency delay and failure while observing actual requests, readiness, liveness, traffic, restarts, retries, and recovery.

Bad model: multiply one happy-path request until a round count is reached, report an average response time, and omit payload distribution, errors, concurrency, data, dependency state, resource saturation, generator limits, tail behavior, final invariants, and recovery. The precise request count does not rescue the model.

Conditional model: deterministic behavior, representative typical and burst profiles, and isolated resource recovery pass, but target peak, topology, and managed provider behavior are unavailable. Report the tested envelope and remaining staged qualification; do not claim production capacity.

**Workload evidence record**

```text
workload_model_id:
runtime_claim_and_failure:
artifact_config_topology:
input_source_and_classification:
operation_mix:
arrival_and_concurrency:
payload_and_data_profile:
dependency_and_failure_profile:
cache_and_start_state:
lifecycle_profile:
resource_limits:
generator_and_collector_capacity:
privacy_and_sanitization:
negative_control:
trial_method_and_repeatability:
observed_envelope:
first_limiting_mechanism:
correctness_and_final_state:
recovery_result:
uncertainty_and_non_extrapolation:
owner_threshold_or_decision:
invalidation_event:
```

**Split and invalidation criteria**

Split a workload review when independently owned data, worker, platform, or external-effect states require different artifacts, environments, or recovery decisions; when one result would average incompatible profiles; or when the context needed to explain a model crowds out target evidence. Do not split merely at an endpoint count.

Invalidate affected evidence when material operation mix, arrival burst, concurrency, payload, data skew, dependency behavior, retry policy, artifact, JVM, architecture, topology, resource limit, health policy, migration state, signal overhead, shutdown grace, or recovery mechanism changes. Define `material` relative to the mechanism and owner decision. Small traffic change may invalidate a pool saturation result but not a deterministic config parser test.

The runtime contract includes return to an accepted envelope. After overload, deploy, outage, or migration, observe whether queues clear, pools and memory recover, retries stop amplifying work, health stabilizes, data and effects reconcile, and manual controls can be retired. Capacity without recovery is only a partial workload result.

## Reliability Target

The seed's perfect percentage, eighteen-of-twenty routing sample, zero-rate statement, and universal recovery wording are unsupported by a population, baseline, measurement system, or owner. Do not reuse them as empirical targets.

Reliability has two distinct layers here:

1. **Reference conformance:** deterministic requirements for this evolved artifact can be binary because the complete files are inspectable.
2. **Target runtime reliability:** service objectives and operational limits must be supplied by target owners, measured over explicit populations, qualified against missing data, and guarded by correctness and recovery invariants.

**Reference conformance gates**

| conformance_gate | required_state | verification |
| --- | --- | --- |
| original headings | exactly 26 original Markdown headings with unchanged text and order | compare parsed heading sequence with archive seed |
| packet structure | exactly 26 packet sections and 260 exact question headings | structural count plus exact question-text comparison with governing specification |
| mandatory rationale | exactly 1,560 populated field lines with six required labels per question | structural parser rejects missing, empty, extra, or malformed fields |
| rationale uniqueness | all 1,560 values unique before and after Section and Question prefixes are stripped | exact and normalized uniqueness counts both equal 1,560 |
| section growth | every one of 26 evolved sections is longer than its matching seed section | heading-bounded per-section length comparison |
| source preservation | frozen local paths, headings, hashes, and dated evidence facts remain accurate | local source identity and complete-read review |
| content hygiene | no unresolved markers, non-ASCII text, trailing whitespace, malformed table, unclosed fence, or accidental added heading | focused verifier plus explicit structural scans |
| skeptical review | complete packet and reference rereads find no generic duplication, unsupported precision, hidden conflict, or unbounded claim | persisted bounded review checkpoints and correction log |

Failure of one gate means the reference artifact is nonconforming. These are not statistical service objectives and should not be averaged.

**Runtime reliability hierarchy**

| layer | purpose | example_shape | authority |
| --- | --- | --- | --- |
| user_or_operator_outcome | state what people and dependent systems must experience | accepted request, durable work completion, safe degraded response, recoverable release | product, service, and operational owners |
| hard invariant | state unacceptable secret, data, artifact, traffic, effect, or ownership outcomes | no successful acknowledgment before required durable completion; no promotion of an unidentified artifact | target policy and accepted requirement |
| measured objective | bound a recurring outcome over a defined population and window | target-owned successful request, freshness, work-age, or recovery objective without a universal value | accountable service owner using qualified data |
| degraded contract | define how the service behaves when a dependency, resource, telemetry, or maintenance state is impaired | reject, shed, queue, serve stale, remove traffic, or stop intake according to target policy | product, service, dependency, and platform owners |
| component indicator | support diagnosis and control without replacing the outcome | pool saturation, queue age, timeout class, migration state, readiness, drain work | mechanism owner and observed target behavior |
| recovery contract | define containment, restoration, reconciliation, and residual repair | return traffic safely, reconcile ambiguous effects, restore data invariant, clear backlog | incident, data, platform, and service owners |
| evidence and coverage | state how much of the contract has actually been exercised | deterministic, real-dependency, packaged, staged, incident, conditional | gate record and reviewer interpretation |

A component indicator is not an objective merely because it is easy to collect. A process can be healthy while data, work, or customer state is wrong. An aggregate objective cannot compensate for a hard invariant violation.

**Runtime reliability dimensions**

| dimension | contract_questions | failure_and_degraded_states | evidence_needed |
| --- | --- | --- | --- |
| artifact integrity | Are the intended source, dependencies, package, config, and promoted identity coherent? | wrong bits, mutable tag, environment rebuild, missing provenance | wrapper and CI resolution, digest trace, package startup, stage inspection |
| startup and configuration | Does valid input start and invalid or unavailable required input fail safely? | missing or malformed config, denied secret, partial initialization, restart loop | real binding tests, packaged startup, redaction, provider and profile scenarios |
| secret and identity safety | Are values and authority bounded through injection, use, output, rotation, and exposure response? | disclosure, overpermission, stale credential, denied access, compromised identity | policy, effective permissions, canary scan, rotation or containment drill |
| request and response correctness | Does each admitted operation reach an accepted result or explicit failure without hidden effect? | validation, domain, transport, dependency, timeout, cancellation, partial response | contract, framework, client, and real-boundary tests plus final-state checks |
| data integrity and freshness | Do reads and writes preserve accepted invariants and freshness across failures and versions? | stale state, partial commit, lost update, incompatible schema, replica lag | transaction and persistence tests, production dialect, historical and mixed-state scenarios |
| migration reliability | Can supported prior data and applications move through each intermediate state and recover? | invalid legacy row, lock, partial migration, old/new incompatibility, failed repair | versioned migration matrix, staged rollout, stop and recovery evidence |
| dependency resilience | Are deadlines, cancellation, retries, quotas, idempotency, and degraded behavior coherent? | slow, unavailable, partial, denied, rate-limited, ambiguous commit | fault injection, total-attempt accounting, external-state reconciliation |
| worker and effect durability | Is every admitted item complete, retryable, released, or reconcilable across termination? | lost work, duplicate effect, stale lease, early acknowledgment, ambiguous restart | phase interruption, broker or store semantics, packaged termination, final effect state |
| observability reliability | Can bounded signals distinguish failure and reach an owner without exposing data? | telemetry delay, loss, high cardinality, wrong classification, unowned alert | signal injection through query and action, privacy and loss scenarios |
| health and traffic safety | Do startup, readiness, liveness, degradation, drain, and restart control automation safely? | early traffic, stuck removal, restart amplification, false green, readiness churn | actual request behavior plus platform traffic and restart observation |
| release control | Can staged evidence detect harm and invoke an authorized stop before broad exposure? | late signal, wrong artifact, incompatible data, absent owner, ineffective containment | negative gate, immutable promotion, canary or stage, stop and recovery drill |
| shutdown and resource safety | Does termination stop admission, cancel and drain owned work, release resources, and preserve recovery state? | hanging call, forced kill, leaked lease, unknown in-flight work, incomplete telemetry | interruption across phases, resource observation, restart and reconciliation |
| recovery effectiveness | Can the system return business, data, traffic, work, resources, and signals to an accepted state? | process restored but customers, data, or effects remain wrong | runbook rehearsal, final invariants, residual repair and owner closure |

Activate only applicable dimensions, but justify every exclusion by an absent state transition. A stateless request parser may not need migration or worker targets. A queue worker with external effects does.

**Reliability contract record**

```text
reliability_contract_id:
accepted_user_or_operator_outcome:
population_and_unit:
normal_state:
degraded_state:
failure_state:
shutdown_state:
recovered_state:
hard_invariants:
target_owned_objective_and_source:
measurement_window_or_scenario:
numerator_denominator_or_state_rule:
inclusions_and_exclusions:
artifact_config_data_work_scope:
data_sources_and_coverage:
missing_or_delayed_data_behavior:
guardrails:
decision_signals_and_actions:
owner_and_risk_authority:
verification_tiers_completed:
conditional_boundaries:
recalibration_or_invalidation_event:
```

Do not fill this record with plausible percentages or deadlines. If the owner has not set a value, preserve the objective as unresolved and state which release or operational claim it blocks.

**Target selection protocol**

1. Begin with the user or operator outcome and the consequence of failure.
2. Identify hard invariants that cannot be traded for aggregate success.
3. Define population: operations, users, tenants, work items, data states, artifacts, deployments, or incidents actually represented.
4. Define normal, degraded, failed, shutdown, and recovered states, including partial success and external effects.
5. Choose a target-owned measured objective only where events and data quality support one. Use scenario contracts for rare or high-consequence states.
6. Map indicators to causal decisions. Avoid collecting component health with no action or user-state link.
7. Qualify measurement coverage, missing data, retries, duplicates, maintenance, and telemetry failure.
8. Add fault, lifecycle, and recovery evidence at the smallest safe fidelity that can disprove the contract.
9. Stage changes under owner-defined stop and recovery authority.
10. Review incentives, escaped states, manual repair, and populations omitted by the objective.

**Evidence tiers**

| tier | establishes | does_not_establish |
| --- | --- | --- |
| deterministic | state-machine, validation, cancellation, invariant, and selection behavior under controlled inputs | real driver, dependency, package, platform, workload, or provider behavior |
| real_boundary | framework, database, broker, or client semantics in an isolated integration | managed target policy, production topology, capacity, or full lifecycle |
| packaged | startup, config, resources, signal, and termination behavior of the intended artifact | immutable promotion or managed traffic unless those are exercised |
| staged_platform | scoped identity, traffic, health, dependency, resource, shutdown, and recovery behavior | universal production distribution or future provider behavior |
| incident_or_production_observation | actual behavior for the recorded artifact, state, workload, and event | all future states, absent counterfactuals, or complete detection coverage |

Confidence increases per bounded claim and environment. It does not become a universal percentage.

**Objective qualification and anti-aggregation**

- Define what counts as an attempt, success, failure, duplicate, canceled operation, maintenance state, and recovered event.
- Preserve retries and partial attempts instead of counting only final successful responses.
- Segment material change classes, workloads, tenants, artifacts, versions, and dependency modes where aggregation hides causal differences.
- Treat missing telemetry as unknown or failure according to policy; never silently exclude it.
- Include post-service recovery work when data, external effects, or users remain impacted after process health returns.
- Examine correlated failures and common dependencies; independent-event assumptions can be badly misleading.
- Keep privacy and access boundaries explicit in reliability data.
- Review whether teams can improve the number by rejecting hard work, delaying closure definitions, suppressing alerts, or moving toil elsewhere.

**Good, bad, and conditional targets**

Good config contract: all required target config has a typed startup rule; valid representative input starts; missing, malformed, and denied-secret paths reach explicit states; secret values remain absent from bounded outputs; restart behavior and owner action are exercised. A target owner may add a measured startup objective after baseline and population are known.

Bad config target: `startup succeeds almost always`. It has no artifact, profile, attempt definition, missing-secret treatment, restart-loop guardrail, or output-safety invariant.

Good migration contract: every supported prior schema and application state has an allowed path through expansion, data remediation, coexistence, and contract; historical data invariants and partial recovery are exercised. Duration or lock objectives are added only from target workload and database evidence.

Bad migration target: `zero migration failures`. It can exclude aborted runs, manual repair, incompatible old applications, and data damage while claiming perfection.

Good worker contract: every admitted item is eventually complete, explicitly retryable, released to a durable owner, or placed in reconciliation under target policy; external effects have acceptable duplicate semantics; termination and restart scenarios verify final state. Aggregate throughput does not override lost-work invariants.

Conditional health target: application readiness and request behavior pass under injected dependency failure, but managed-platform traffic and restart cannot be observed. Local health semantics pass; platform reliability remains conditional with a named staged gate.

Good recovery contract: a runbook drill begins from a preserved partial state, chooses rollback, roll-forward, repair, replay, or containment based on compatibility, and validates business, data, work, traffic, resources, and signals. Elapsed recovery time may be measured, but only the target owner sets its objective and closure definition.

**Reliability decision loop**

At each release, verify artifact and activated contract evidence. At a target violation, preserve state, apply owner-authorized containment, and classify the earliest broken dimension. After recovery, test whether measurement detected the right state, whether the objective drove the right action, and whether users, data, work, and external effects were truly restored. Update requirements, gates, runbook, or design; do not merely tune the dashboard.

Recalibrate when population, workload, artifact, versions, data, topology, dependency, platform, support policy, objective ownership, telemetry, or incident evidence changes materially. Retire targets with no consumer or action. Preserve hard invariants and rare-event drills even when aggregate objectives look healthy.

The aim is honest controlled behavior: the service exposes degraded and failed states, contains amplification, preserves critical invariants, and returns to an accepted condition under accountable authority. Concealing failure to protect a percentage is itself a reliability defect.

## Failure Mode Table

Treat each row as a hypothesis. Target runbooks and accountable owners govern executable containment and recovery. Before acting, preserve the failing revision, artifact, effective non-secret config, data and work state, traffic, environment, timestamps, and bounded signals. Avoid printing sensitive material.

| failure_mode | discriminating_evidence | likely_consequence | immediate_containment_question | durable_correction | recovery_proof | escalation_or_limit |
| --- | --- | --- | --- | --- | --- | --- |
| local_or_external_source_drift | frozen hash, date, target version, and current authority disagree with the claim being reused | stale mechanism or compatibility assumption guides implementation or operation | Can the consuming decision pause while provenance and target state are preserved? | refresh only the exact current claim when authorized; revise dependent routes and gates selectively | target scenario passes under applicable mechanism and source role is updated | route policy or unresolved authority conflict to source and target owners |
| generic_runtime_advice_escape | output names production practices without target wrapper, mechanism, artifact, scenario, or owner | tool proliferation, wrong scope, and unsupported safety language | Which recommendation would mutate the target or grant readiness without evidence? | re-route from accepted outcome and target stance; remove unrelated mechanisms | each retained recommendation traces to target locator, gate, result, limit, and owner | stop implementation if the route cannot identify the changed lifecycle boundary |
| wrapper_or_version_drift | local, CI, package, or deployed effective versions and plugins differ | compile, proxy, serialization, generated code, bytecode, or runtime behavior diverges | Can promotion stop before another artifact is built or deployed? | restore repository-owned wrapper and aligned versions or run an explicit upgrade route | clean build, package identity, framework integration, and staged startup agree | escalate unsupported-version and compatibility policy to service and platform owners |
| missing_or_malformed_config | actual startup path lacks a required key, value is invalid, or fallback differs by profile | partial initialization, unsafe default, restart loop, or late request failure | Should startup remain unavailable, or can a defined degraded mode operate safely? | typed boundary binding, startup validation, explicit defaults, profile contract, and tests | valid, absent, malformed, boundary, and restart scenarios reach expected states | owner decides whether degradation is acceptable; do not invent a fallback |
| secret_exposure | recognizable non-production canary appears in log, error, trace, health, dump, config view, or artifact | credential or private-data disclosure across broader trust boundaries | Who can contain access, revoke or rotate authority, preserve evidence, and notify required owners? | redact by construction, minimize outputs, separate sensitive types, correct access and diagnostic paths | canary scans pass; replacement authority works; exposure scope and residual state are reconciled | invoke security and incident policy; generic runtime guidance cannot accept risk |
| secret_or_identity_denial | target identity cannot retrieve or use required secret, certificate, token, or key | startup failure, request denial, retry storm, or unsafe fallback | Can traffic or intake be held while identity and provider state are checked? | correct least-privilege role, injection, renewal, denied-state behavior, and runbook | denied, expired, rotated, and restored scenarios behave as policy requires without disclosure | platform and security owners control provider action and break-glass paths |
| authorization_or_input_boundary_failure | unauthorized identity or invalid input reaches an action, or valid traffic is rejected inconsistently | data exposure, unintended effect, user harm, or availability loss | Which operation and trust boundary must be disabled or contained under authority? | explicit validation and authorization at owned boundary with consistent failure mapping | abuse, cross-identity, malformed, replay, and recovery cases preserve target invariants | security or product owner decides policy and incident obligations |
| dependency_latency_or_outage | controlled downstream slowdown or failure reproduces timeout, saturation, cancellation, or health symptoms | resource retention, request failure, retry amplification, false readiness, and backlog growth | Can load be bounded, intake reduced, or degraded behavior entered without worsening the dependency? | coherent total deadlines, cancellation, bounded retry, shedding or queue policy, signals, and recovery | slow, unavailable, partial, and recovered dependency scenarios release resources and restore service | dependency and product owners decide acceptable degradation and external action |
| retry_amplification | attempts per user operation or work item rise as dependency health falls | downstream overload, quota exhaustion, duplicate effects, queue growth, and delayed recovery | Can new retries or intake be bounded while preserving durable work ownership? | failure classification, total attempt and deadline budget, backoff, idempotency, and circuit or shedding policy where target-owned | fault scenario shows bounded attempts, no unacceptable duplicate, and backlog plus dependency recovery | coordinate across clients and shared dependency; local tuning alone may shift load |
| pool_or_resource_exhaustion | connections, threads, dispatchers, memory, CPU, files, disk, or exporter queues saturate before demand is served | latency tails, health churn, failed work, blocked shutdown, and cascading dependency pressure | Which admission, concurrency, or workload can be bounded safely while evidence is retained? | right-size from measured workload, bound queues, release resources, isolate blocking, and expose saturation | representative burst, degraded dependency, drain, and recovery restore pools and final state | platform or capacity owner controls resource and scaling policy; avoid blind limit increases |
| telemetry_blindness_or_corruption | independent service state contradicts logs, metrics, traces, dashboard, or alert delivery | responders misdiagnose recovery, miss harm, or take an amplifying action | Which independent artifact, data, traffic, work, or provider state can guide safe containment? | bounded signal semantics, delivery health, loss indication, privacy, cardinality, consumer, and fallback diagnosis | induced failure and telemetry loss reach the right decision and recover without hidden gaps | incident command may need alternate evidence; do not wait for broken telemetry to self-report |
| unbounded_or_sensitive_telemetry | signal dimensions grow with user input or private values appear | backend instability, cost surge, query failure, and disclosure during incidents | Can the offending signal be sampled, disabled, or access-contained without losing critical diagnosis? | bounded dimensions, redaction, protected detail store, sampling and retention policy, and tests | adversarial inputs show bounded growth and no sensitive output; diagnosis remains possible | security, privacy, and telemetry owners decide containment and retention |
| readiness_false_positive | health reports ready while representative requests or work cannot meet accepted contract | unsafe traffic reaches instances and amplifies release or dependency failure | Can traffic be held or removed under platform authority while actual state is checked? | align readiness with target traffic prerequisites and lifecycle; keep failures observable | startup, dependency degradation, migration window, drain, and recovery show correct traffic transitions | platform policy owns routing; framework endpoint status alone is insufficient |
| liveness_restart_amplification | dependency slowdown or startup work causes repeated platform restart of otherwise recoverable instances | diagnostic loss, cache churn, thundering restart, reduced capacity, and prolonged outage | Can restart automation be paused or corrected safely by its owner while state is preserved? | reserve liveness for local unrecoverable states; use startup, readiness, or degradation for other conditions | injected dependency and slow-start scenarios avoid unnecessary restart and return to service | platform and incident owners control automation changes and shared blast radius |
| historical_data_incompatibility | migration or new code fails on prior rows, nulls, encoding, scale, or invariant violations absent from fresh fixtures | rollout stops, data becomes unreadable, or application versions disagree | Should rollout stop before further mutation, and which data owner can assess actual state? | representative historical profiles, remediation or quarantine, compatible expansion, and explicit contract | supported prior states, old and new artifacts, final invariants, and residual rows are reconciled | data owner authorizes repair, deletion, or exception; do not infer from empty database success |
| partial_or_contended_migration | migration times out, locks, fails after some work, or runs concurrently from multiple instances | schema and data enter ambiguous state; traffic and rollback compatibility degrade | Can application rollout and migration ownership be paused without worsening state? | single owned versioned process, idempotent or resumable steps where feasible, bounded observation, and recovery plan | exact partial state moves through authorized roll-forward, repair, or rollback and all consumers pass | database and incident owners decide destructive or production operations |
| wrong_or_mutable_artifact | deployed digest, source revision, dependencies, or package contents do not match tested release | diagnosis and rollback assumptions refer to the wrong bits | Can promotion or traffic stop while artifact inventory and state impact are established? | build once, record provenance, promote immutable identity, reject substitution, and retain gate outputs | intended digest starts with compatible config and data; staged behavior and recovery pass | artifact and platform owners control registry, promotion, and credential actions |
| package_permission_or_runtime_mismatch | image or package fails under target user, architecture, filesystem, resource, certificate, or port policy | startup, write, network, native library, or health behavior fails only after deployment | Can release hold while effective identity and runtime constraints are inspected? | deterministic package for supported runtime with least required authority and explicit writable or network needs | restricted package smoke and target-like startup, traffic, termination, and restart pass | platform or security owner approves exceptions; local root execution is not proof |
| CI_gate_no_op_or_wrong_scope | test filter selects nothing, task skips integration, cache key misses input, or stage uses another module or artifact | green pipeline fails to block the changed defect | Can release stop until task selection and artifact lineage are qualified? | map requirement to configured task, preserve negative control, fix filter, cache, stage, and retention | deliberate defect fails intended stage; clean run passes on promoted artifact | pipeline owner decides shared runner, cache, and release-policy changes |
| staged_rollout_regression | canary or bounded stage shows worse user, data, dependency, resource, health, or work state | harm spreads if progression follows time or aggregate green signal | Which stop condition fired, who owns containment, and is current state rollback-compatible? | improve discriminating signals, stage design, artifact and data compatibility, stop authority, and recovery | containment halts spread and selected rollback, roll-forward, repair, or hold restores accepted state | incident, product, data, and platform owners may share the decision |
| lost_or_duplicate_worker_effect | work disappears or an external effect repeats across retry, acknowledgment, termination, or restart | financial, notification, data, or customer state diverges from work state | Can intake pause and affected identities enter reconciliation without blind replay? | structured ownership, durable work and effect identity, correct acknowledgment order, bounded retry, and reconciliation | phase interruptions produce complete, retryable, released, or reconciled final states | product and external-system owners define acceptable duplicate and repair policy |
| shutdown_deadline_or_drain_failure | in-flight requests or work remain at grace expiry, cancellation does not propagate, or resources stay held | forced kill creates ambiguous effects, lost work, stale leases, or delayed rollout | Can new admission stop and unfinished identities be preserved before forced termination? | explicit intake closure, owned scopes, bounded drain, resource release, durable state, and restart handling | terminate each phase; observe deadlines, effects, acknowledgments, resources, restart, and backlog recovery | platform grace and forced-kill policy require target owner evidence |
| ambiguous_external_commit | client times out or is canceled while downstream may have committed an effect | retry may duplicate; suppression may leave requested state incomplete | Can the affected operation be isolated and queried or reconciled before replay? | stable effect identity, provider-supported idempotency or lookup, explicit ambiguous state, and repair workflow | before and after commit fault scenarios reach one accepted final business state | provider, product, and incident owners control effect and customer remediation |
| recovery_action_incompatible | rollback, roll-forward, replay, or repair is started without matching current data, message, cache, or effect state | recovery deepens incompatibility or erases evidence | Can action pause while exact partial state and compatible artifacts are identified? | state-based recovery decision matrix, rehearsed procedures, authority, and final invariants | chosen action restores business, data, work, traffic, resources, and signals; residual repair closes | destructive or irreversible recovery belongs to accountable owners and incident process |
| correlated_platform_or_provider_failure | multiple service symptoms share identity, network, database, broker, telemetry, or deployment control plane | independent local mitigations amplify shared outage or compete for capacity | Can incident command establish common state and coordinate load or traffic decisions? | dependency mapping, common-cause signals, service degradation contracts, and shared recovery drill | controlled shared failure restores dependent services without synchronized retry or restart surge | cross-service authority supersedes isolated service action during shared incident |

**Operational response protocol**

1. Establish authority and preserve evidence. Protect people, secrets, data, and external effects.
2. Record current and prior artifact, config, schema, traffic, dependency, work, platform, and signal states.
3. Name the earliest observed contract violation, not the loudest symptom. Keep competing hypotheses when evidence is weak.
4. Choose an independent confirmation source when the suspected boundary includes telemetry or health automation.
5. Identify possible amplification through retries, restarts, traffic, queues, caches, migrations, or operator actions.
6. Apply the smallest reversible, authorized containment with explicit stop and observation conditions.
7. Reassess after containment. A changed symptom can invalidate the initial causal model.
8. Choose durable correction at the owning boundary; avoid compensating controls that hide state indefinitely.
9. Exercise recovery from actual partial state and validate business, data, work, traffic, resources, signals, and residual repair.
10. Convert repeated causal failures into an earlier requirement, gate, platform control, or rehearsed runbook only after side effects are checked.

**Failure interactions to inspect**

- Dependency slowdown can consume pools, trigger retries, fail readiness, induce liveness restarts, overload telemetry, and create shutdown ambiguity. Increasing a timeout or resource limit may only move the bottleneck.
- Migration contention can delay startup, fail readiness, cause rollout replacement loops, and make rollback incompatible. Treat database and application states together.
- Telemetry loss can make a stopped alert look like recovery. Cross-check artifact, traffic, data, work, and provider state.
- Wrong artifact and config drift can mimic code regression. Verify identity before debugging implementation details.
- Secret denial can cause startup churn or request retry; secret exposure can occur in the diagnostic response. Containment and evidence handling need security ownership.
- Worker acknowledgment, external commit, and termination interact. A clean process exit does not establish effect correctness.
- A shared provider incident can cause synchronized local retries and restarts. Coordinate through incident authority rather than optimizing each service independently.

**Good, bad, and conditional response examples**

Good config response: a release fails startup on a newly required key. The team confirms the exact artifact and profile, observes typed validation, holds rollout, corrects target config under owner authority, restarts the same artifact, and verifies readiness plus representative request behavior. It then adds the missing production-like startup gate.

Bad surge response: request failures and pool saturation appear during dependency latency. The team increases pool size, adds retries, and rolls forward without total deadline or downstream capacity evidence. The mitigation amplifies the dependency outage and prolongs recovery.

Good migration response: unexpected historical rows violate a new constraint. Rollout stops before contract, exact migration and data state are preserved, data owner selects remediation, old and new compatibility are rechecked, and final invariants plus signals pass before progression.

Bad recovery response: an image rollback starts immediately after a migration error, even though prior code cannot read the partially transformed data. Process health returns on some instances while data and customer state worsen.

Conditional telemetry response: application failures are confirmed through data and traffic state while the telemetry path is delayed. The team contains using independent evidence, labels dashboard interpretation inconclusive, and restores or validates telemetry before declaring recovery.

**Failure-mode qualification record**

```text
failure_mode_id:
target_contract_violated:
artifact_config_data_work_scope:
activation_or_injection:
primary_signal:
independent_confirmation:
competing_hypotheses:
amplification_paths:
containment_action_and_authority:
containment_result:
durable_correction:
recovery_scenario:
final_business_and_operational_state:
telemetry_or_health_behavior:
residual_risk_and_owner:
gate_or_runbook_change:
invalidation_or_retirement_event:
```

Qualify high-consequence rows with safe isolated or staged scenarios and real incident evidence. Do not assign universal likelihood or severity numbers. Prioritize from target consequence, irreversibility, recurrence, detection coverage, recovery difficulty, and owner judgment.

Retire a row or manual control when the mechanism no longer exists or stronger prevention and diagnosis subsume it. Preserve incident provenance so removal does not erase why the boundary mattered. Add a new row only when it introduces a distinct causal state or action interface; another symptom name is not enough.

## Retry Backpressure Guidance

`retry_backpressure_default`: Do not retry until the operation, failure, total deadline, repeated-effect semantics, capacity, cancellation, and owner are known. Fail fast for deterministic or unauthorized states. Reconcile before repeating an ambiguous effect. Admit only work the system can bound, observe, and recover.

Retry changes when work happens; backpressure changes whether and where work waits, fails, sheds, or transfers ownership. Both are runtime contracts, not client-library tuning details.

**Failure classification and disposition**

| failure_class | evidence_needed | default_disposition | retry_can_be_valid_when | primary_risk |
| --- | --- | --- | --- | --- |
| invalid_request_or_domain_state | deterministic validation or invariant result under current state | fail without automatic retry and return target-owned error | caller or upstream changes the invalid input or state | repeated load and confusing delayed failure |
| missing_or_malformed_config | actual startup or binding path identifies invalid required input | stop startup or enter an explicitly accepted degraded state | config revision changes and startup is re-evaluated as a new attempt | restart loop and unsafe fallback |
| denied_permission_or_identity | effective identity and policy show denial, expiry, or revocation | stop dependent action and route to security or platform owner | authority or credential state is deliberately corrected or renewed | lockout, audit noise, exposure, and unauthorized workaround |
| unsupported_version_or_contract | resolved versions, compatibility authority, or protocol response show mismatch | stop and select compatible artifact or explicit upgrade path | a compatible version, feature, or negotiated contract becomes effective | repeated incompatible traffic and state corruption |
| deterministic_implementation_defect | same input and state reproduce failure without external variation | fail and fix the causal code or data contract | implementation or relevant state changes and regression gate is rerun | amplification with no chance of success |
| optimistic_concurrency_conflict | target store reports a conflicting current version or ownership change | refresh state and reconsider operation | operation is safe to recompute, attempts are bounded, and caller deadline remains | starvation, lost update, and hot-key contention |
| transient_connection_setup | target client and dependency evidence indicate a short-lived connection failure before effect | retry within total budget if capacity and policy permit | connection attempt has no ambiguous effect and dependency is expected to recover | synchronized connection storm and deadline exhaustion |
| explicit_rate_or_quota_limit | provider returns an applicable limit signal with known scope and recovery semantics | respect target/provider policy, reduce admission, and defer or fail | delay is inside caller or work deadline and queued work remains bounded | thundering retry, unfairness, and extended backlog |
| dependency_unavailable | independent evidence confirms unavailable or degraded downstream state | bound or shed load; use accepted degradation or durable handoff | repeated operation is safe and recovery signal or target policy supports another attempt | retry amplification and shared outage extension |
| timeout_before_known_effect | target semantics establish the operation did not cross the effect boundary | retry may be considered within identity and total budget | pre-effect failure is observable and idempotency remains intact | misclassified ambiguous commit |
| timeout_with_ambiguous_effect | request ended without proof whether external effect committed | enter ambiguous state and reconcile before replay | stable effect identity or provider-supported idempotency proves repeat safety | duplicate or missing irreversible effect |
| cancellation_or_shutdown | owner deadline or termination stops work | propagate cancellation, preserve durable state, and release resources | durable owner or restarted process deliberately resumes from known state | abandoned work continuing invisibly or duplicate restart |
| capacity_or_pool_exhaustion | target resource and workload signals show saturation | reduce admission, concurrency, or work; allow recovery | capacity becomes available and retry does not recreate the overload wave | positive feedback, queue explosion, and long recovery |
| data_or_migration_failure | invariant, dialect, lock, prior state, or partial transition fails | stop mutation and route to data owner and recovery plan | state is repaired or a verified resumable or idempotent step permits continuation | repeated destructive mutation and incompatible rollback |
| stale_external_evidence | dated mapping cannot support a current claim | refresh exact authority once per bounded research decision when authorized | target version and claim are known and retrieval can change the decision | browsing loops and context displacement |
| missing_context_or_owner | action depends on unknown artifact, policy, state, or authority | pause dependent work and route a precise handoff | missing fact or owner decision is returned | repeated speculative implementation |
| telemetry_or_gate_inconclusive | flakiness, loss, contamination, or no-op selection prevents interpretation | repair or isolate the evidence system | a clean discriminating observation can be produced | retrying tests until a convenient pass |

An error label alone is not classification. The same timeout can occur before connection, during processing, after an external commit, or while telemetry is delayed. Each state has a different safe disposition.

**Retry contract**

Before enabling or changing a retry, define:

- the user or work operation and stable identity;
- the exact failure classes eligible and explicitly ineligible;
- the external effect boundary and whether attempts are idempotent, deduplicated, transactional, or reconcilable;
- the outer accepted deadline, cancellation source, and remaining budget calculation;
- which layer owns retry so nested libraries, proxies, queues, and workers do not multiply attempts invisibly;
- the attempt limit or stop rule set by target policy and measured workload, not copied from an example;
- delay and dispersion behavior appropriate to provider signals and synchronized-client risk;
- admission, concurrency, pool, queue, and downstream-capacity limits;
- per-attempt and total-work signals with bounded identifiers and privacy;
- final failure, ambiguous state, durable handoff, dead-letter or quarantine, and operator action;
- shutdown, restart, lease, acknowledgment, and recovery semantics;
- the condition that disables or recalibrates the policy.

Count total work across all layers. A user operation retried by a gateway, service client, message source, and worker can produce many downstream attempts even when each layer appears locally bounded. Prefer one explicit retry owner per effect boundary and observe effective attempts.

**Backpressure options**

| option | choose_when | state_created | benefit | cost_or_failure_to_verify |
| --- | --- | --- | --- | --- |
| fail_fast | invalid, unauthorized, incompatible, saturated, or deadline-exhausted work cannot succeed safely now | explicit rejected operation | preserves resources and clear ownership | user impact, caller retry behavior, and error classification |
| admission_limit | concurrent or incoming work must remain within measured service capacity | waiting before admission or explicit rejection | protects pools and downstreams before internal work begins | fairness, queue location, stale requests, and retry behavior |
| concurrency_limit | owned active work needs a hard bound around a scarce resource | bounded internal wait and active set | prevents resource saturation and improves diagnosis | head-of-line blocking, priority, cancellation, and work duration skew |
| bounded_memory_queue | short-lived work can wait inside the process and loss at process exit is acceptable or handled | volatile queued state | smooths brief bursts with low infrastructure cost | overflow policy, memory, shutdown, fairness, and lost work |
| durable_queue_or_store | work must survive process lifetime and target source supports ownership semantics | durable backlog, leases or visibility, attempts, and completion state | decouples producers and workers and enables recovery | age, poison work, duplicates, ordering, capacity, dead letter, and reconciliation |
| load_shedding | lower-value or excess work may be rejected to preserve critical outcomes | explicit shed result | protects core service and reduces cascading failure | policy, fairness, user effect, retries, and observability |
| degraded_response | a bounded stale, partial, queued, or reduced result is product-acceptable | explicit degraded state | preserves useful outcome during dependency failure | correctness, freshness, security, user expectation, and recovery |
| circuit_or_dependency_guard | repeated known dependency failure should stop expensive attempts temporarily | local open or guarded state | reduces amplification and improves recovery space | probe policy, shared state, false opening, fallback, and synchronized recovery |
| durable_handoff | responsibility can transfer to an owned asynchronous mechanism | accepted work identity and status | separates caller deadline from eventual work | acknowledgment, status, cancellation, duplicate, retention, and operator support |
| reconciliation | effect outcome is ambiguous or state can diverge across systems | explicit unresolved record or work list | prevents blind repeat and supports repair | lookup authority, retention, final decision, privacy, and manual burden |
| operator_hold | high-consequence state requires human or incident authority | paused release, traffic, migration, or work | prevents unsafe automatic progress | ownership, response time, evidence preservation, and stale hold retirement |

A queue does not remove load; it moves load into the future. Bound backlog, age, item size, attempts, retention, poison work, and drain rate. State what happens at overflow and how recovery avoids a second surge.

**Request and external-client guidance**

1. Derive inner connect, read, processing, and retry budgets from the accepted end-to-end deadline.
2. Propagate caller cancellation through owned coroutine and client boundaries. Isolate or bound blocking calls that cannot cooperate.
3. Classify connect failure, explicit refusal, partial response, rate limit, timeout, cancellation, and ambiguous commit separately.
4. Use stable operation or effect identity when repeat safety depends on it.
5. Observe original operations, attempts, final outcomes, downstream work, queueing, and resource release.
6. During dependency degradation, verify retries do not overwhelm pools, health, telemetry, or shutdown.
7. After recovery, verify attempt rate and queued work subside and normal latency or throughput returns within target acceptance.

Fallback is not automatically safer than failure. A stale or partial response must have an accepted correctness, security, and freshness contract. A fallback that calls another shared dependency can move or amplify the outage.

**Worker and durable-work guidance**

- Give every item a stable identity and define source ownership before acquisition, during lease or visibility, after effect, after completion record, and after acknowledgment.
- Bound active workers against actual resource and downstream capacity. Avoid an unbounded coroutine launch behind a bounded source poll.
- Make retry, redelivery, and restart one coherent attempt model. Persist or derive attempt state where target semantics require it.
- Do not acknowledge before the durable state required by the contract. Do not hold ownership indefinitely while waiting beyond a useful deadline.
- Route poison or permanently failing work to an explicit terminal, quarantined, or owner-review state with sensitive-data controls.
- During shutdown, stop admission, cancel and drain bounded work, release or preserve leases, and retain unresolved identities for restart.
- Reconcile ambiguous external effects before replay. Verify final business state and source backlog after recovery.

**Migration, release, and operational workflow guidance**

Migration retry is not an ordinary request retry. Confirm whether a step is transactional, idempotent, resumable, partially applied, lock-holding, and compatible with old and new artifacts. Stop and inspect actual state before repeating a failed data mutation.

Release backpressure means pausing progression when a mapped gate, staged signal, artifact identity, data compatibility, health, or recovery condition fails. Do not keep generating new artifacts or stages while the decision evidence is red. Preserve the failed artifact and state, classify, correct the causal boundary, then restart from the earliest invalidated gate.

During an incident, backpressure can include owner-authorized traffic hold, intake pause, concurrency reduction, or rollout stop. Generic guidance does not authorize those actions; target runbooks define them.

**Agent and evidence-workflow backpressure**

For long-running reference or implementation work:

- Persist one atomic packet or evidence unit before the matching artifact change when the workflow requires that order.
- Run an immediate structural or behavioral sanity check after each unit; do not accumulate unverified batches in memory.
- Stop new generation when exact structure, uniqueness, source identity, test, or heading gates fail. Repair the earliest incomplete boundary.
- Append a durable journal checkpoint at required batch and phase boundaries with exact counts, paths, test evidence, and nonempty next actions.
- Re-read governing instructions after interruption, spec change, or ownership change before broad edits.
- Assign one owner per shared file or theme boundary and reconcile at merge or handoff with exact path, heading, artifact, and evidence invariants.
- Do not retry an unavailable or contradictory source indefinitely. Narrow the question, preserve uncertainty, and escalate to the owner.
- Never use retry as permission for repeated destructive commands, production mutations, commits, or pushes outside explicit authority.

These workflow controls protect context and shared state; they are not evidence that a Kotlin service's runtime retry policy is correct.

**Verification matrix**

| scenario | observe | pass_condition_shape | hidden_failure_to_check |
| --- | --- | --- | --- |
| invalid input | attempts, status, CPU, logs, final state | no automatic repeat; clear bounded failure | caller or gateway silently retries |
| transient connect failure | per-layer attempts, deadline, connection use, downstream load | bounded attempts fit total deadline and recover | synchronized attempt wave after recovery |
| ambiguous effect timeout | effect identity, provider state, local attempt, retry | reconciliation or idempotency reaches one accepted final state | duplicate effect masked by final success |
| dependency outage | admission, retries, pools, queues, health, traffic, telemetry | load remains bounded; degraded or failure contract is visible | liveness restarts or fallback overload another system |
| rate or quota limit | provider signal, queue age, fairness, retries, final result | policy-respecting delay, failure, or handoff stays inside bounds | queued work expires or one tenant starves others |
| worker termination | admitted identities, phases, leases, acknowledgments, effects, restart | every item completes, retries, releases, or reconciles | process exits cleanly while effects are ambiguous |
| poison work | attempts, error class, queue position, terminal state, alerts | repeat stops and item reaches owned terminal handling | infinite redelivery or sensitive payload in diagnostics |
| recovery wave | backlog, attempt rate, dependency load, resources, latency, final state | queued work drains without a second overload and invariants hold | retry surge begins only after dependency returns |
| evidence refresh | exact claim, target version, retrieval, decision outcome | one bounded refresh resolves or preserves uncertainty | repeated broad browsing displaces target evidence |

**Examples**

Good transient retry: an outbound read fails before any effect, target client semantics confirm no request was accepted, the operation is idempotent, the outer deadline has budget, and one layer owns bounded attempts. Fault tests show attempts disperse, cancellation stops them, pools recover, and downstream load remains bounded. No universal attempt count is copied.

Bad timeout retry: a write times out after the provider may have committed. The client immediately repeats without stable effect identity. The final call succeeds, so request metrics look healthy while two external effects exist.

Good backpressure: a dependency slows and active work reaches a measured resource bound. The service stops admitting excess low-priority work according to product policy, exposes degraded state, preserves existing work, and avoids liveness restart. After dependency recovery, queues and attempts decline and normal state returns.

Bad queueing: every request is accepted into an unbounded in-memory queue. Latency and memory grow, shutdown loses queued work, and clients retry because status is invisible. The queue postponed failure and removed ownership clarity.

Conditional provider case: target documentation and sandbox show a rate signal, but production quota scope and recovery timing cannot be observed. The client can implement policy-compatible parsing and bounded behavior; production backpressure remains a staged or owner-confirmed claim.

Good agent backpressure: an immediate check finds normalized field duplication after one packet section. Work stops, only that section is corrected, uniqueness passes, the matching reference is saved, and the journal records the durable boundary. Regenerating the entire packet would increase risk and violate ownership cadence.

**Retry and backpressure record**

```text
policy_id_and_owner:
operation_and_stable_identity:
eligible_failure_classes:
ineligible_and_ambiguous_classes:
effect_boundary_and_repeat_safety:
outer_deadline_and_cancellation:
retry_owning_layer:
total_attempt_or_stop_rule:
delay_and_dispersion_policy_source:
admission_concurrency_pool_queue_bounds:
fairness_and_priority:
shutdown_restart_acknowledgment:
signals_and_final_state:
fault_and_recovery_results:
conditional_provider_behavior:
invalidation_or_disable_condition:
```

Review the policy when workload, dependency, provider, timeout, pool, queue, effect, artifact, platform, or incident evidence changes. Remove redundant retry layers and temporary limits when stronger ownership and capacity controls replace them. A stable design remains bounded and diagnosable while overloaded, and its recovery does not unleash hidden repeated work.

## Observability Checklist

`observability_default`: Begin with a failure or recovery decision, then choose the smallest bounded signal set that can distinguish the state and lead an accountable consumer to an action. Percentiles, counts, dashboards, and alerts are not mandatory by category; they are selected from target outcomes, workload, service objectives, and qualified measurement.

The frozen local runtime source supplies useful historical categories: structured logs with correlation, classified errors, request and dependency metrics, queue and worker outcomes, health checks, and trace propagation when the platform supports it. These are questions to reconcile with the target, not proof that a specific stack or signal is present or sufficient.

**Signal contract**

Every persistent operational signal should define:

| field | completion_rule |
| --- | --- |
| decision_question | state the failure, degraded, shutdown, or recovery distinction the signal supports |
| state_and_event | define what happened, when it begins and ends, and whether it represents an attempt, operation, work item, artifact, or final outcome |
| source_and_owner | identify the component that knows the state and the team responsible for schema and behavior |
| artifact_and_config_identity | correlate source revision, package or image digest, environment, profile, and relevant config revision without exposing sensitive values |
| dimensions | use bounded values needed for diagnosis; document controlled vocabularies and unknown state |
| sensitive_data_boundary | exclude or protect credentials, private payloads, user-controlled text, stack content, and identifiers according to target policy |
| temporal_semantics | state event time, processing delay, aggregation window, ordering, and clock uncertainty relevant to interpretation |
| retry_and_work_semantics | distinguish original operation, individual attempt, final result, queue age, work phase, duplicate, and reconciliation where applicable |
| emission_path | identify application, framework, client, database, broker, platform, or automation that emits the signal |
| delivery_path | identify SDK, exporter, collector, transport, storage, query, dashboard, alert, and paging boundaries actually used |
| retention_and_cost | define target-owned retention, sampling, indexing, volume, and cost constraints |
| consumer_and_query | name role-based consumer and the exact target-native query, view, or state lookup used |
| action_and_authority | map signal states to continue, hold, diagnose, shed, stop, contain, recover, or escalate decisions |
| missing_or_degraded_telemetry | define how delay, drop, sampling, exporter saturation, collector outage, or stale dashboard becomes visible |
| independent_confirmation | identify direct artifact, data, traffic, work, dependency, or provider state used when the signal is consequential or suspect |
| verification_scenario | inject or reproduce normal, failure, degraded, telemetry-loss, and recovery states at required fidelity |
| compatibility_and_consumers | version schema and inventory automation, dashboards, alerts, runbooks, and downstream analysis that depend on it |
| invalidation_and_retirement | name changes that force requalification and conditions for removing the signal safely |

If no consumer or action exists, question whether the signal should be persistent. Temporary exploratory instrumentation can have a narrower contract, but needs access scope, data boundary, retention, cost control, owner, and removal event.

**Signal-type selection**

| signal_or_state_source | strongest_use | important_limit | choose_when |
| --- | --- | --- | --- |
| structured event or log | detailed discrete context and diagnostic classification | volume, privacy, text drift, and expensive aggregation | a bounded event record helps reconstruct one failure or action |
| metric | aggregate rate, distribution, level, capacity, or state over repeated events | dimensions can explode and aggregation can hide individual effects | population and decision semantics are stable and repeated |
| trace | causal path and timing across owned or instrumented boundaries | sampling, propagation gaps, asynchronous work, and cost | request or work crosses services, clients, queues, or components and correlation matters |
| audit event | security or administrative action with identity and policy significance | sensitive access, retention, and completeness requirements | target policy requires accountable action history |
| health state | machine-readable startup, readiness, liveness, or degradation for automation | a small state can conceal actual request, data, or dependency behavior | platform policy consumes it and state transitions are exercised |
| work or effect ledger | durable ownership, attempts, external effects, completion, and reconciliation | schema and operational burden | queues, workers, retries, or ambiguous effects require final-state reasoning |
| database or broker direct state | authoritative data, schema, lock, backlog, lease, or acknowledgment view | access, cost, consistency, and owner boundaries | telemetry summaries are insufficient for migration or work recovery |
| profile or sample | detailed resource, stack, allocation, or execution evidence | sampling bias, overhead, and poor long-term actionability | bounded diagnosis of a reproduced performance or resource problem |
| synthetic or direct probe | independent check of a contract from outside the service | can be shallow, create load, or miss internal state | availability or traffic behavior needs independent confirmation |
| runbook decision log | operator interpretation, authority, action, and observed result | manual consistency and sensitive incident context | release, containment, recovery, or exception decisions need traceability |

Use complementary sources only where they reduce uncertainty. Duplicating the same unqualified state across logs, metrics, and traces does not create independent evidence.

**Runtime observability checklist**

| boundary | questions_to_answer | candidate_signal_shapes | negative_or_degraded_scenario |
| --- | --- | --- | --- |
| build and artifact | Which revision, effective versions, and artifact are running, and did required gates apply? | build provenance, package digest, deployment identity, gate result locator | deploy substituted or rebuilt artifact and confirm control detects it safely |
| configuration | Which config schema and profile loaded, and why did startup accept or reject it? | non-sensitive config revision, validation classification, startup state | missing, malformed, unknown, boundary, and profile mismatch |
| secrets and identity | Did required identity and secret access succeed without disclosing values? | role or provider reference, access classification, rotation state, redaction audit | denied, expired, rotated, and canary-output scan |
| requests and routes | What operation was attempted, admitted, completed, rejected, canceled, or degraded? | bounded operation, result class, duration distribution if target-relevant, correlation | invalid input, application error, dependency error, timeout, cancellation, overload |
| external calls | Which dependency, attempt, deadline, result, quota, and effect identity mattered? | bounded dependency and operation class, per-attempt and final outcome, remaining budget | connect failure, slow response, partial result, rate limit, ambiguous commit |
| persistence | Which query, transaction, pool, lock, and invariant state contributed? | bounded operation class, transaction result, pool saturation, lock state, data version | contention, replica lag, timeout, partial transaction, pool exhaustion |
| migration | Which version, prior state, progress, compatibility, lock, failure, and recovery apply? | migration identity and state, artifact versions, invalid-row and remediation counts | historical incompatibility, partial application, concurrent owner, old/new mismatch |
| queues and workers | Who owns each item, how old is backlog, which attempt and phase, and what final effect exists? | backlog and age, active work, attempt class, completion, duplicate suppression, reconciliation | poison item, lease expiry, external timeout, termination, restart, recovery wave |
| resource and capacity | Which resource is limiting and how does pressure affect latency, health, and work? | CPU, memory, pools, threads or dispatchers, files, disk, network, queue and exporter saturation | burst, slow dependency, cold start, sustained profile, constrained resource |
| health and traffic | Is the service starting, ready, live, degraded, draining, receiving traffic, or restarting as intended? | explicit lifecycle state, traffic and restart observation, representative request result | dependency outage, slow startup, migration window, drain, local unrecoverable state |
| rollout | Which artifact, stage, traffic or work slice, baseline, stop signal, decision, and recovery apply? | stage identity, artifact digest, bounded outcome and guardrails, owner action | canary regression, late telemetry, wrong artifact, failed stop or recovery |
| shutdown | Did admission stop, cancellation propagate, drain finish or preserve state, and resources release? | intake state, in-flight identities, phase, deadline, canceled and unfinished work, release state | terminate before and after effect, forced deadline, blocking call, telemetry flush failure |
| recovery | Are business, data, traffic, work, resources, and signals back in accepted state? | recovered invariant, backlog and reconciliation, artifact and config, residual repair | rollback incompatible with data, repeated recovery failure, stale failure signal |

Candidate signals are not a requirement to collect everything. Select those that answer the accepted outcome. For latency, use distributions and populations defined by target objectives and workload; do not import the seed's percentile names as universal policy.

**Privacy and cardinality gate**

- Define a controlled vocabulary for route, operation, result, dependency, artifact, version, work phase, and recovery state where used as dimensions.
- Do not use raw URLs, request bodies, SQL, exception text, user identifiers, credentials, tokens, arbitrary tenant strings, queue payloads, or stack traces as metric dimensions.
- Place detailed diagnostic content only in an access-controlled store with policy-aligned redaction and retention.
- Use correlation identifiers that do not encode sensitive payload and are sampled or retained according to target policy.
- Exercise high-variety and adversarial input; observe series count, index growth, exporter queues, query behavior, and cost.
- Verify redaction on success and failure paths, including config binding, secret denial, client errors, migration failures, health details, and incident actions.
- Record who can access signals and how exposure is contained and audited.

**Temporal and counting correctness**

- Distinguish event time from collection and query time when delay matters.
- Record clock uncertainty across services and providers; use causal or correlation identity for ordering where possible.
- Count original operations, individual attempts, final results, canceled work, duplicates, and reconciliation separately.
- Define whether a timeout is a failed attempt, ambiguous effect, or final user failure.
- Define asynchronous completion: a request accepted for durable work is not the same as work completed.
- Preserve artifact and config boundaries in comparisons so a rollout mix does not look like one homogeneous population.
- State sampling and missing-data effects before interpreting rates or tails.

**Telemetry self-observability**

Observe or otherwise detect:

- emission failures and dropped events;
- exporter or agent queue saturation;
- collector availability, rejection, and delay;
- trace propagation gaps and sampling changes;
- metric series or log-index growth;
- dashboard and query freshness;
- alert evaluation and delivery failures;
- paging, acknowledgment, and escalation gaps;
- discrepancies between telemetry and independent data, traffic, work, or provider state.

When telemetry is degraded, enter an explicit unknown state. Use independent evidence for high-consequence decisions and avoid declaring recovery from silence.

**End-to-end signal qualification**

1. State the failure question and owner decision.
2. Identify the source component and target artifact/config state.
3. Inject a safe known event with non-sensitive identifiers.
4. Observe emission, collection, storage, query, dashboard or alert, and consumer delivery.
5. Confirm dimensions, timestamps, counts, sampling, redaction, and correlation match source state.
6. Have the intended consumer interpret the signal and execute or simulate the authorized runbook decision.
7. Inject telemetry delay or loss and verify the fallback state source and escalation.
8. Recover the service condition and confirm signals resolve, backlog or delay drains, and stale alerts do not continue to drive action.
9. Retain exact query or view, artifact, environment, result, limits, and invalidation events.

**Evidence-provenance checklist for reference-driven work**

- Record which local source regions were read completely and which adjacent sources were intentionally not opened because their boundary was absent.
- Record frozen hashes for consequential local claims and label dated public mappings unrefreshed until an authorized retrieval occurs.
- Record exact target files, tasks, artifact, config, environment, and owner policies that established applicability.
- Record exact verification command or scenario, result summary, failure reason, and stronger claim not proved.
- Record changed paths, unresolved risks, conditional environments, handoff recipients, and next invalidation event.
- Keep audit evidence small and access-safe: concise command/result summaries and locators are preferable to raw transcript, secret-bearing logs, or entire incident dumps.
- Preserve journal checkpoints at required cadence so context and ownership state remain recoverable.

**Examples**

Good dependency signal: a target-approved operation class records original request, each client attempt, total deadline outcome, dependency result class, pool state, and final user result using bounded dimensions. A slow-dependency drill reaches a runbook action and shows attempts and pools recover after the dependency returns.

Bad dependency signal: one `error_count` rises, exception text becomes a label, retries are counted as independent requests, and no artifact or dependency identity is present. The dashboard cannot distinguish one user failure from amplified attempts and may overload itself.

Good worker signal: durable work identity links acquisition, attempt, phase, external effect, completion, acknowledgment, termination, restart, and reconciliation. Payload stays outside metric dimensions. A phase-interruption drill verifies final business state and alert resolution.

Bad health signal: liveness fails whenever the database is slow. Restarts increase, evidence disappears, and traffic state remains unknown. The endpoint is technically observable but operationally harmful.

Conditional signal: application emission, redaction, trace propagation, and local query pass, while managed alert delivery and paging are unavailable. Emission and local collection claims pass; incident-action readiness remains conditional.

Temporary instrumentation: a protected detailed event is introduced to diagnose a rare cancellation race. It has bounded sampling, no secret payload, restricted access, cost monitoring, and a removal event after causal evidence and a stable lower-volume signal exist.

**Signal inventory record**

```text
signal_id_and_schema_version:
decision_question:
source_component_and_owner:
artifact_config_environment:
event_and_population_semantics:
bounded_dimensions:
sensitive_data_and_access:
temporal_retry_work_semantics:
delivery_path_and_consumers:
query_alert_or_direct_state:
action_and_authority:
missing_telemetry_behavior:
independent_confirmation:
qualification_and_recovery_results:
cost_retention_sampling:
compatibility_consumers:
invalidation_and_retirement:
```

Treat signals as operational APIs. Version material schema or semantic changes, inventory consumers, preserve compatibility during transition, and requalify automation and runbooks. Retire signals with no decision consumer or when a stronger direct control replaces them, after verifying no hidden alert, audit, or recovery dependency remains.

## Performance Verification Method

The seed's local p95 and p99 latency limits and one-session delivery target have no target objective, baseline, workload, artifact, environment, or measurement evidence. They are not defaults. If a target has no authoritative objective, characterize current behavior or compare alternatives and report the limitation; do not manufacture deployment compliance.

`performance_verification_default`: Define one bounded performance claim, preserve correctness and reliability invariants, establish target workload and environment, qualify the generator and collector, compare like artifacts under controlled conditions, identify the first limiting mechanism, and observe recovery after pressure.

**Performance claim types**

| claim_type | outcome_to_define | material_inputs | required_guardrails |
| --- | --- | --- | --- |
| request_or_operation_latency | end-to-end time and, if useful, queue, service, dependency, and response components for a target population | operation mix, arrival, concurrency, payload, data, dependencies, retries, warm state | correctness, errors, cancellation, attempt count, resource and final state |
| throughput_or_capacity | accepted and completed operations or work per target unit at a defined resource and objective boundary | concurrency, mix, batching, data, dependency capacity, topology, resource limits | latency or work age, failures, fairness, data and effect correctness, recovery |
| startup_and_readiness | time and state from package start to accepted startup and traffic ability | cold or warm state, config, secret access, class loading, connections, migrations, platform probes | startup correctness, false readiness, resource spike, restart behavior |
| dependency_client | connect, request, response, cancellation, retry, and total operation behavior | provider mode, network, TLS, pools, timeout budget, failure class, effect semantics | bounded attempts, downstream load, ambiguous effects, resource release |
| database_or_query | query, transaction, lock, connection, and result behavior | dialect, schema, data size and skew, index, isolation, concurrency, cache | result invariants, transaction correctness, pool health, retry and recovery |
| migration | completion, lock, resource, and service compatibility through a versioned transition | prior schema, historical data, dialect, operation type, concurrency, old/new artifacts | data invariants, mixed versions, partial failure, stop and recovery |
| worker_and_queue | work age, processing, backlog, attempts, completion, and drain under target workload | arrival waves, work duration, partitions, concurrency, dependencies, effects | no lost or unacceptable duplicate work, bounded queue, restart reconciliation |
| resource_efficiency | CPU, memory, connections, threads or dispatchers, files, disk, network, and telemetry per accepted outcome | artifact, JVM, topology, workload, config, warm state | correctness, latency, throughput, health, garbage collection, cleanup |
| shutdown_and_drain | admission stop, cancellation, drain, deadline, resource release, and restart behavior under active work | work phase, duration distribution, blocking calls, leases, effects, platform grace | final work and effect state, no leaks, no false graceful result |
| recovery | return of requests, queues, pools, resources, health, signals, and business state after pressure or failure | prior overload or outage, backlog, retries, caches, topology, recovery action | no second surge, residual repair visible, final invariants and owner closure |
| reference_workflow | reviewer or agent time to reach the correct route, gate, and stop decision | task class, source volume, target access, interruption, reviewer expertise | decision accuracy, completeness, rework, source and evidence boundaries |

Do not collapse these into one score. A faster request path can use more memory, create longer recovery, or increase duplicate effects. A faster reference workflow can omit a required source or gate.

**Method selection**

| method | strongest_claim | controls_needed | cannot_prove_alone |
| --- | --- | --- | --- |
| deterministic behavior or timing test | algorithmic bound, timeout selection, cancellation sequence, or regression in controlled code | stable clock or virtual time where valid, isolated inputs, correctness assertion | JVM, driver, package, network, platform, or production workload performance |
| microbenchmark | isolated operation cost and comparative mechanism behavior | benchmark harness, warm-up state, dead-code resistance, stable inputs and environment | end-to-end latency, capacity, dependency, data, or recovery behavior |
| profiler or diagnostic sample | where CPU, allocation, lock, thread, or blocking time is spent during a reproduced state | representative workload, bounded overhead, artifact and warm state | user outcome or objective compliance without measurement |
| framework or component load | request, serialization, binding, lifecycle, or adapter behavior | real framework path, controlled dependencies, generator capacity | packaged runtime, managed platform, full external systems |
| database or broker integration | dialect, driver, transaction, lock, queue, acknowledgment, and pool behavior | representative schema, data, work, concurrency, real component version | managed provider topology, production scale, artifact promotion |
| packaged process test | startup, JVM, config, resource, health, shutdown, and local dependency behavior | intended artifact, target-like JVM and architecture, resource limits, clean state | managed identity, traffic, provider, autoscaling, and production topology |
| synthetic load or stress | response across controlled mix, burst, concurrency, payload, and resource profiles | qualified generator, representative model, stable environment, repeated trials | unmodeled production distributions and policy objectives |
| sanitized replay | behavior under observed historical operation timing and mix | privacy review, artifact/config identity, safe external effects, replay semantics | novel failures, future workload, unsampled state, complete population |
| sustained stability run | leak, drift, queue growth, cache, and telemetry behavior over an explicit duration | stable workload and environment, cleanup, resource and final-state checks | indefinite stability beyond observed duration |
| staged platform observation | scoped target identity, traffic, topology, resource, health, rollout, shutdown, and recovery behavior | accountable owner, baseline, stop conditions, immutable artifact, safe state | universal production behavior or future provider changes |
| analytical capacity model | sensitivity and likely limiting pools or resources | explicit assumptions, equations, calibration points, uncertainty | nonlinear interactions and objective compliance without observed validation |

Select the least costly method able to falsify the claim, then escalate fidelity when lower tiers cannot represent a material boundary. Profiling explains a measurement; it does not replace one.

**Preconditions**

Before a performance run:

1. Identify the target-owned objective or state that matters. If absent, write a comparative hypothesis and state that no objective pass will be claimed.
2. Confirm functional, data, security, artifact, retry, health, and recovery hard gates. Optimization cannot trade them away silently.
3. Record source revision, wrapper, effective versions, package or image digest, JVM, architecture, config, topology, resource limits, and observability state.
4. Define workload dimensions and profiles from the Workload Model: operation mix, arrival, concurrency, payload, data, dependency, cache, lifecycle, and failure state.
5. Define population and measurement boundaries. Distinguish queue wait, processing, dependency, end-to-end, asynchronous acceptance, and final completion.
6. Establish a comparable baseline or reference artifact when making a regression claim.
7. Qualify generator, simulator, dependency fixture, clocks, collection, and final-state checks. Ensure they have headroom and expose loss.
8. Define stop conditions for resource, error, data, dependency, cost, and environment harm.

**Kotlin and JVM controls**

- State whether the claim concerns cold startup, early warm-up, or steady warmed execution. Class loading, code compilation, caches, and connection establishment can make these distinct.
- Record JVM and runtime options that affect memory, garbage collection, threads, diagnostics, and container resource awareness where relevant.
- Observe garbage-collection activity and allocation when memory behavior can alter tails or throughput; do not infer cause from pause or heap summary alone.
- Distinguish coroutine suspension from blocking. A coroutine-friendly API can still call blocking JDBC, filesystem, DNS, native, or client work beneath it.
- Record dispatcher, executor, thread, connection, and worker bounds whose contention shapes the result.
- Ensure virtual-time coroutine tests are not used as wall-clock performance evidence.
- Separate framework startup, dependency initialization, application readiness, and actual representative request ability.
- Recreate generated-code, proxy, reflection, serialization, persistence, and compiler-plugin paths that the target artifact uses.

**Execution protocol**

1. Run a smoke and negative control to confirm the workload reaches the intended path and the evidence system detects a known distinction.
2. Establish cold or warm state explicitly. Reset data, caches, connections, queues, and external state where comparisons require it.
3. Run baseline and candidate under comparable artifact, environment, resource, dependency, and workload conditions. Randomize or alternate order when drift could bias one side.
4. Use enough observations and repetitions for the claimed statistic and variability. Do not report tail percentiles from a population too small or censored to support them.
5. Pace arrivals according to the model. A client that waits for each slow response may reduce offered load and hide overload queueing.
6. Observe accepted and completed operations, attempts, errors, cancellations, queue wait, service and dependency time, resources, pools, health, telemetry loss, and final state.
7. Increase stress only in an isolated or owner-approved environment with stop conditions. Identify the first resource or control that limits the outcome.
8. Remove pressure or restore the dependency. Observe backlog, retries, resources, health, latency or work age, and final invariants until accepted recovery or an explicit residual state.
9. Preserve results and confounders. An unexpected artifact, config, dependency, noisy neighbor, collector loss, or generator saturation can make the run inconclusive.
10. Reproduce material differences before claiming regression or improvement, unless one run reveals a deterministic hard failure that already blocks the change.

**Measurement and interpretation**

- Use the statistic appropriate to the target decision. A median can describe a typical population; a tail percentile can describe a qualified upper distribution; maximum values are highly sample-dependent; averages can hide multimodal behavior.
- Report sample or event count, inclusion rules, missing observations, retries, canceled operations, and asynchronous completion semantics.
- Preserve raw-enough bounded data or summaries to review distributions without retaining sensitive payloads.
- Compare both absolute target objective, when authoritative, and change from baseline when useful. Passing one does not imply the other.
- Report uncertainty and run-to-run variability. Do not use extra decimal places to disguise noise.
- Segment material routes, payloads, tenants, data states, artifacts, versions, and dependency modes rather than averaging incompatible cohorts.
- Treat timeouts and client abandonment carefully: missing completion observations can censor the slowest work and make the remaining distribution look better.
- Count retry attempts and downstream work separately from original user operations.
- Include measurement overhead when profiling or detailed telemetry materially changes the system.

No universal percentile names are required. Use target service objectives and measurement policy. If a target requires p50, p95, p99, or another statistic, record the population, window, estimator, sample sufficiency, missing-data behavior, and owner threshold.

**Correctness, reliability, and cost guardrails**

A performance improvement fails if it:

- changes accepted results, ordering, data invariants, authorization, or secret handling;
- loses or repeats work or external effects beyond policy;
- hides errors, disables useful signals, samples away consequential failures, or creates unbounded cardinality;
- shifts latency into queues, retries, background work, recovery, or another service without acceptance;
- increases restart, health churn, migration risk, shutdown ambiguity, or manual repair;
- depends on a different artifact, lower-fidelity fixture, incompatible config, or weaker gate;
- consumes resources or cost beyond target constraints;
- harms fairness or starves a target population hidden by aggregate throughput.

**Result states**

| result | meaning |
| --- | --- |
| pass_against_objective | qualified target population meets an authoritative objective and all guardrails at the tested envelope |
| comparative_improvement | candidate shows a reproducible improvement against comparable baseline with guardrails preserved; objective compliance may remain unknown |
| characterization | behavior, limiting resource, and recovery are measured without a pass threshold |
| failure | objective or hard guardrail is violated with interpretable evidence |
| inconclusive | harness, environment, artifact, data, dependency, telemetry, or variability prevents the claimed interpretation |
| conditional | lower-fidelity or narrower envelope supports a subset while target topology, provider, scale, or objective evidence remains missing |

**Worked examples**

Request regression: a serializer change is suspected of increasing endpoint latency. The test holds artifact inputs, JVM, framework, data, dependencies, resources, operation mix, arrival, payload, and warm state comparable. It observes end-to-end and serialization components, errors, allocation, garbage collection, retries, and response correctness. A profiler explains increased allocation; repeated runs confirm the candidate regression. No deployment objective is claimed if the target has none.

Bad request test: run one warmed local request, compare wall time to the seed's universal p95 limit, and report production readiness. The observation has no population, percentile, baseline, target artifact, dependency, workload, or variability.

Migration characterization: use production dialect, supported prior schemas, representative historical sizes and skew, old and new application compatibility, resource and lock signals, and partial recovery. Report observed duration and limiting state for the tested profile. Target owner decides the maintenance or online objective; local fixture time is not promoted.

Worker capacity: vary arrival waves and active worker bounds while observing backlog age, attempts, dependencies, pools, effects, termination, and recovery. The pass is not maximum throughput alone; every item must remain complete, retryable, released, or reconcilable and backlog must recover without a second surge.

Conditional package result: candidate reduces packaged startup under local target-like resources and preserves readiness correctness, but managed identity and platform probe timing are inaccessible. Package startup improvement passes locally; deployment readiness remains conditional.

Reference workflow: compare how reviewers handle representative task classes using the evolved route. Measure time to correct route and gate only alongside missed boundaries, rework, and decision quality. Do not require completion within one session or use fewer source reads as a success when a consequential source was omitted.

**Performance evidence record**

```text
claim_id_and_owner:
target_objective_or_hypothesis:
population_and_measurement_boundary:
baseline_artifact_and_result:
candidate_artifact_and_change:
wrapper_versions_jvm_architecture:
config_topology_resources:
workload_profile_and_source:
data_and_dependency_state:
cold_warm_cache_pool_state:
method_generator_collector:
negative_control_and_harness_headroom:
trial_order_repetitions_variability:
latency_throughput_resource_or_work_results:
attempt_error_cancellation_and_final_state:
first_limiting_mechanism:
guardrails_and_cost:
post_pressure_recovery:
confounders_missing_data_uncertainty:
result_classification:
invalidation_and_rerun_event:
```

Requalify when material workload, artifact, JVM, architecture, config, data, dependency, topology, resource, retry, telemetry, health, platform, or objective changes. Optimize only after the limiting mechanism is supported by evidence. Retire a benchmark that no longer represents an accepted target path or whose result drives no decision.

Sustainable performance preserves correctness and diagnosis at the boundary, fails or degrades explicitly beyond it, and returns resources, queues, attempts, health, and business state to an accepted condition after pressure is removed.

## Scale Boundary Statement

`scale_boundary_default`: This reference is sufficient when one accepted Kotlin backend runtime outcome has discoverable target stance, bounded changed transitions, named owners, feasible evidence, and an end-to-end recovery decision. It can compose across several components or owners if their interfaces are explicit. It stops being sufficient as the sole lead when independent artifacts, data states, release trains, policies, failure domains, or recovery authorities need separate decisions.

Do not use endpoint count, request count, file count, service count, or owner count as a universal threshold. Scale is the interaction among state independence, consequence, context, evidence fidelity, and coordination.

**Scale dimensions**

| dimension | bounded_for_this_reference_when | split_or_escalate_when | integration_invariant_to_preserve |
| --- | --- | --- | --- |
| accepted outcome | one coherent normal, degraded, failed, shutdown, and recovered contract can be stated | several outcomes can succeed or fail independently and have different owners or release decisions | user and operator state across all outcomes remains explicit |
| repositories and modules | target mechanisms and changed dependency path can be discovered without crowding out evidence | independent repositories have separate instructions, artifacts, gates, and release cadence | versioned interface, compatibility, artifact identity, and end-to-end scenario |
| runtime artifacts | one or a compatible set of artifacts has a single staged transition | artifacts promote independently or mixed combinations require separate support matrices | exact source-to-artifact lineage and supported version combinations |
| frameworks and execution modes | one target stance owns lifecycle behavior | Spring, Ktor, blocking, reactive, batch, or native modes need materially different contracts | transport, data, client, signal, health, and recovery interfaces |
| data stores and schemas | one owned compatibility and recovery plan covers state change | independent databases, replicas, caches, object stores, or event logs have distinct mutation and repair authority | cross-store invariant, ordering, effect identity, and reconciliation |
| external systems | dependencies fit one client, timeout, retry, degradation, and effect model | providers have independent quotas, identities, contracts, or irreversible effects | total deadline, repeated-effect safety, fallback, and final business state |
| traffic and work | admission, concurrency, queue, priority, and workload envelope share one control model | user traffic, scheduled work, queues, and administrative operations have separate capacity and fairness decisions | shared resource protection and accepted degradation |
| topology and platform | one platform policy governs package, identity, resources, health, traffic, termination, and restart | regions, clusters, clouds, architectures, or providers differ materially and fail independently | artifact/config compatibility, routing, state, failover, and recovery authority |
| security and compliance | one applicable trust and policy boundary covers change | identities, regulated data, tenant isolation, audit, or exception authority differ | least authority, data handling, audit continuity, and incident obligations |
| CI and release | one gate map and promotion route controls the accepted change | components deploy independently, require coordinated order, or use different artifact systems | interface tests, compatibility window, immutable promotion, stop and rollback or roll-forward |
| observability | one signal contract and owner can distinguish system state | telemetry domains, retention, privacy, automation, or incident tools differ | shared correlation, clock uncertainty, artifact identity, and independent state confirmation |
| ownership and authority | each consequential decision has a reachable owner and shared outcome | no one can accept cross-boundary risk or owners disagree on state and recovery | decision log, escalation, handoff, and final integration owner |
| failure and recovery | one runbook can contain and restore the bounded state | components require independent containment, destructive action, or different incident authority | common timeline, partial state, coordination, and accepted recovered business condition |
| context and evidence | relevant sources and target paths fit a progressive route with explicit omissions | discovery remains unbounded or critical evidence is repeatedly displaced by context | source roles, dependency map, exact question, and persisted decision record |

Several rows may trigger together. A one-repository service can still need a data migration owner, platform owner, and security owner. That does not force separate projects if one outcome and interface contract remain coherent. Conversely, two modules in one repository may need separate release and recovery plans.

**Sufficiency test**

Keep this reference as the sole or primary runtime lead only when all are true:

- the accepted outcome and strongest failure consequence are explicit;
- target instructions, wrapper, effective versions, framework mode, artifacts, config, data, signals, CI, platform, and runbooks can be discovered as activated;
- every changed state transition has one owner and a target mechanism;
- alternatives and hard gates fit one decision record;
- deterministic and production-like evidence can be assigned without contradictory environment assumptions;
- partial transition and mixed versions have a coherent compatibility model;
- stop, containment, recovery, and residual handoff authority are reachable;
- source and implementation context can be narrowed enough to preserve counterexamples and actual target evidence.

If one condition fails, do not necessarily abandon the reference. Use it as runtime integration guidance while routing the independent decision to a specialist, owner, program, or incident authority.

**Scale route modes**

| route_mode | choose_when | coordination_shape | completion_gate |
| --- | --- | --- | --- |
| single_runtime_route | one artifact and bounded lifecycle outcome dominate | one owner coordinates activated companions | all changed states and recovery pass in one evidence map |
| composed_specialist_route | security, testing, framework, data, or platform semantics are distinct but serve one outcome | runtime lead sends named interface questions and reconciles returns | each specialist contract and end-to-end lifecycle scenario pass |
| sequential_transition_program | intermediate compatibility states require ordered changes | one decision log and integration owner stages artifacts, data, consumers, and retirement | every intermediate state is usable, observable, stoppable, and recoverable |
| parallel_independent_work | tasks edit separate artifacts and do not redefine shared decisions | exclusive ownership, frozen interfaces, frequent integration, and one verifier per invariant | local gates plus interface and end-to-end gates pass before release |
| dedicated_domain_route | one boundary has enough independent state, evidence, and maintenance to need its own plan or reference | domain owner leads; runtime retains interface requirements | domain outcome and runtime integration both pass |
| platform_or_provider_program | target platform, topology, identity, traffic, or shared dependency changes across services | platform authority, service representatives, staged migration, and common incident plan | service compatibility, shared controls, capacity, rollout, and recovery pass |
| incident_command | active harm or shared failure spans owners and services | common authority, timeline, containment, service evidence, and coordinated recovery | accepted system and business state plus residual owner closure |
| stop_and_reframe | objective, ownership, authority, or recoverable intermediate state cannot be established | preserve evidence and resolve the missing decision before more implementation | a bounded outcome and accountable route are accepted |

**Split protocol**

1. Map the whole outcome from source to artifact, config, data, dependencies, traffic or work, signals, shutdown, and recovery.
2. Identify state transitions that can fail or recover independently and the owners who decide them.
3. Define safe intermediate states. If none exist, the work may need a coordinated atomic or maintenance transition rather than parallel implementation.
4. Split by decision and owned artifact, not by arbitrary file counts. Give each workstream inputs, outputs, exclusions, and authority.
5. Freeze interface contracts: versions, schema, operation, identity, effect, health, signal, artifact, and recovery expectations.
6. Assign one integration owner and one source of truth for shared decisions. Local workstream owners cannot silently redefine them.
7. Choose local gates and interface gates before implementation. Preserve a failure case at each boundary.
8. Integrate frequently enough to expose drift before every workstream completes independently.
9. Stage compatibility and mixed states with stop and recovery conditions.
10. Retire temporary adapters, dual writes or reads, compatibility gates, old artifacts, and coordination structures after consumer evidence passes.

**Interface contract checklist**

- caller and provider versions plus supported combinations;
- request, response, event, or work schema and unknown-field behavior;
- authentication, authorization, identity, secret, and audit ownership;
- timeout, cancellation, retry, idempotency, ordering, and duplicate semantics;
- transaction, migration, data freshness, cache, and reconciliation state;
- artifact, config, environment, and release ordering;
- readiness, liveness, degradation, traffic, termination, and restart;
- logs, metrics, traces, correlation, signal failure, and incident consumer;
- stop, rollback, roll-forward, repair, replay, failover, and recovery authority;
- compatibility retirement and invalidation events.

**Distributed agent and shared-workspace coordination**

When multiple agents or workers execute the split:

- assign exclusive write ownership per reference, packet, code module, or artifact; readers may inspect shared inputs but must not rewrite them;
- prohibit parallel edits to the same decision record unless a merge protocol and one final owner are explicit;
- persist atomic work immediately at the required cadence rather than holding several sections or components in transient context;
- run a local sanity gate after each atomic save and stop on heading, structure, uniqueness, test, artifact, or source-identity failure;
- append durable progress at required batch and phase boundaries with exact paths, counts, results, blockers, and nonempty next steps;
- freeze shared source and specification hashes and recheck them before final integration;
- do not revert or reformat unrelated work; reconcile changed interfaces with the owning worker;
- require interface and whole-artifact verification in addition to each worker's local pass;
- avoid commits, pushes, destructive actions, or production mutations outside explicit authorization;
- after interruption or spec change, resume from the latest durable evidence and reread governing constraints before editing.

Parallelism is unsafe when two workers choose the same architecture, edit the same schema or reference, mutate shared state, or depend on an interface still under negotiation. Run those decisions sequentially or through one owner.

**Large-codebase narrowing**

Before loading many files:

1. identify target instructions and build roots;
2. find the runtime entry point, composition root, worker, migration, pipeline, package, and deployment artifacts relevant to the outcome;
3. trace inbound and outbound dependencies at the changed boundary;
4. rank direct implementation, tests, config, data, operations, and owner policy by decision relevance;
5. allocate context to the failure path and counterexample before broad architecture prose;
6. persist a locator map and expand only when a discovered edge changes blast radius or authority.

Use repository-native graph or dependency tools where available and qualified; otherwise use focused text and build-system discovery. A long unranked file list is not context evidence.

**Examples**

Coherent single-service scope: one Kotlin service adds typed timeout config and bounded client retry. Security owns credential behavior and the dependency owner supplies rate semantics, but one artifact, request contract, rollout, and recovery remain. Runtime operations can lead with composed handoffs.

Safe split: a schema transition requires application compatibility, historical remediation, CI migration gates, and platform rollout. Data owner leads migration state, application owner leads old/new code compatibility, platform owner leads stage and traffic, and one integration owner controls intermediate states. Each workstream has independent artifacts and gates; mixed-version scenarios reconcile them.

Unsafe parallel split: one worker changes acknowledgment ordering while another changes retry and idempotency without a frozen effect contract. Both pass local tests but can jointly acknowledge before durable completion or suppress legitimate retries. The shared ownership/effect decision must be sequential or centrally owned.

Shared-provider incident: identity failure affects many services and telemetry. Local runtime guides service evidence and degradation, while incident command and platform authority lead containment and recovery. Independent service credential work could conflict and expand harm.

Large repository, bounded outcome: a monorepo contains many services, but the target change affects one package, one worker, one migration, and one deployment path. Dependency narrowing can keep one runtime route sufficient despite repository size.

Small topology, large operational scope: a single service controls regulated data, irreversible external effects, independent database and provider owners, and cross-region recovery. It needs specialist and authority composition despite few code modules.

Conditional discovery: dependency tracing identifies several possible consumers, but deploy ownership and actual traffic are unavailable. Implementation interfaces can be reviewed; scale and release sufficiency remain conditional until target owners confirm consumers and recovery.

**Scale decision record**

```text
accepted_outcome_and_consequence:
repositories_modules_artifacts:
frameworks_execution_modes:
data_stores_and_state_owners:
external_systems_and_effects:
traffic_workload_topology:
security_platform_policy:
release_trains_and_compatibility:
failure_domains_and_recovery_authority:
context_and_dependency_map:
sufficiency_result:
split_or_compose_decisions:
interface_contracts:
local_and_integration_gates:
intermediate_states:
integration_owner:
conditional_boundaries:
reroute_and_invalidation_events:
temporary_coordination_retirement:
```

Review scale from escaped interface defects, route loops, merge conflicts, stale summaries, delayed owner decisions, integration failures, and incidents. Promote recurring independently evolving boundaries into dedicated gates, artifacts, or references only when the maintenance value exceeds discovery cost. Dissolve temporary coordination after compatibility and recovery evidence closes the transition.

Healthy scaling preserves end-to-end accountability while allowing independent work. It turns recurring cross-boundary uncertainty into explicit interfaces and evidence, without pretending the whole system can be understood or operated by one undifferentiated runtime checklist.

## Future Refresh Search Queries

`future_research_only_note`: No query in this section was executed during this evolution. No current page content, release, compatibility, advisory, default, provider behavior, or result is asserted. Run a query only in a future task that authorizes browsing and needs the exact claim for a target decision.

Resolve public component coordinates from the target first. Fields in braces must be replaced with sanitized, non-sensitive values such as released component names and versions. Do not include private service names, customer or tenant details, credentials, incident payloads, internal URLs, account identifiers, or unreleased vulnerability details in public search.

**Query preflight fields**

| field | obtain_from | why_required |
| --- | --- | --- |
| `{resolved_kotlin_version}` | wrapper and effective dependency resolution | selects applicable language and compiler behavior |
| `{resolved_java_version}` | toolchain and packaged runtime | constrains JVM, bytecode, container, and library compatibility |
| `{framework_name}` and `{framework_version}` | effective target dependencies | distinguishes Spring, Ktor, and release-specific integration |
| `{coroutine_version}` | resolved coroutine dependency | scopes cancellation, dispatcher, timeout, and API behavior |
| `{compiler_plugin_name}` and `{plugin_version}` | configured build plugins | scopes proxy, no-arg, serialization, generated code, or analysis behavior |
| `{database_engine}` and `{database_version}` | target data platform and driver | scopes dialect, DDL, lock, transaction, and migration behavior |
| `{migration_tool}` and `{migration_tool_version}` | target migration config | scopes command, history, checksum, and recovery semantics |
| `{telemetry_component}` and `{telemetry_version}` | target SDK, exporter, collector, or framework integration | scopes signal schema, propagation, resource, and failure behavior |
| `{platform_or_provider}` and `{platform_mode}` | target deployment and owner policy | scopes identity, health, traffic, termination, resource, and rollout behavior |
| `{ci_or_artifact_system}` and `{runner_or_registry_version}` | target pipeline and artifact path | scopes cache, provenance, permissions, promotion, and retention behavior |
| `{claim_phrase}` | one unresolved runtime decision | prevents generic browsing and determines extraction boundaries |
| `{observed_failure_class}` | access-safe target evidence | narrows authority without exposing private logs or payloads |

If these fields cannot be established, return to target discovery rather than issuing another broad `best practices` search.

**Claim-directed query catalog**

| query_label | use_after | future_query_text | preferred_result_class | reject_or_stop_when |
| --- | --- | --- | --- | --- |
| kotlin_language_version_behavior | Kotlin and Java versions plus exact syntax or runtime question are resolved | `site:kotlinlang.org {resolved_kotlin_version} {resolved_java_version} {claim_phrase}` | version-applicable official Kotlin language or compiler documentation | result is a generic overview, wrong release, or the remaining question belongs to framework or JVM execution |
| kotlin_compiler_plugin_compatibility | exact plugin and framework versions are known | `site:kotlinlang.org {resolved_kotlin_version} {compiler_plugin_name} {plugin_version} {framework_name} compatibility` | official plugin documentation plus applicable compatibility or release material | source discusses latest only or target integration still needs framework proof |
| coroutine_cancellation_semantics | coroutine version, owner scope, execution mode, and failure question are known | `site:kotlinlang.org {coroutine_version} cancellation timeout dispatcher exception {claim_phrase}` | version-relevant official coroutine documentation or API | query answer cannot establish framework, blocking adapter, provider, or packaged shutdown behavior |
| coroutine_release_change | candidate or current coroutine versions are explicit | `site:github.com/Kotlin/kotlinx.coroutines {coroutine_version} release notes changelog {claim_phrase}` | official repository release, tag, issue, source, or test tied to exact behavior | default branch is substituted for released version or implementation is mistaken for supported contract |
| spring_kotlin_runtime_integration | target is Spring and exact Boot or Framework version is resolved | `site:docs.spring.io {framework_name} {framework_version} Kotlin {claim_phrase}` | versioned Spring Boot, Framework, Security, Data, or Actuator authority owning the claim | tutorial or different web stack is returned; target code and package behavior remain untested |
| spring_health_or_shutdown | target Spring integration and platform question are known | `site:docs.spring.io {framework_version} health readiness liveness graceful shutdown {claim_phrase}` | applicable Spring reference for framework lifecycle semantics | remaining uncertainty belongs to platform traffic, grace, or restart policy |
| ktor_runtime_integration | target is Ktor and engine, plugins, and version are resolved | `site:ktor.io {framework_version} {platform_mode} configuration health shutdown {claim_phrase}` | version-applicable official Ktor documentation or API | welcome/tutorial content omits engine or version; target plugin order and package behavior remain unknown |
| database_engine_semantics | exact engine, version, dialect, and operation are known | `site:{database_official_domain} {database_engine} {database_version} transaction lock DDL {claim_phrase}` | database-vendor manual owning transaction, DDL, lock, or recovery semantics | result is ORM or migration-tool advice for a database-owned behavior |
| migration_tool_behavior | migration tool, version, database, and partial-state question are known | `site:{migration_tool_official_domain} {migration_tool} {migration_tool_version} {database_engine} {claim_phrase}` | versioned official migration-tool documentation and release material | result omits database semantics, historical state, old/new compatibility, or target history |
| migration_compatibility_change | current and candidate versions plus target migration history are explicit | `site:{migration_tool_official_domain} {migration_tool} {migration_tool_version} release notes compatibility checksum migration` | official changelog, upgrade, compatibility, or migration guidance | query becomes a substitute for running target history and production-dialect scenarios |
| telemetry_integration_semantics | exact SDK, exporter, collector, framework integration, and version are known | `site:{telemetry_official_domain} {telemetry_component} {telemetry_version} {framework_name} {claim_phrase}` | official integration, protocol, API, or release authority | source cannot establish target backend, privacy, cardinality, consumer, or alert delivery |
| telemetry_failure_and_limits | target signal path and suspected loss or cost boundary are mapped | `site:{telemetry_official_domain} {telemetry_component} {telemetry_version} queue drop retry cardinality {claim_phrase}` | official component operations and limit guidance | remaining issue is target capacity, provider policy, or unobserved collector state |
| jvm_container_runtime | JVM, image, architecture, and resource question are resolved | `site:{jvm_or_image_official_domain} {resolved_java_version} container {platform_mode} memory CPU {claim_phrase}` | official JVM or image documentation applicable to target runtime | query is used to choose an image or runtime without target support and package evidence |
| platform_health_traffic | exact provider, platform mode, and service health states are mapped | `site:{platform_official_domain} {platform_or_provider} {platform_mode} readiness liveness traffic restart {claim_phrase}` | provider or orchestrator authority for actual automation semantics | result is generic orchestration advice or conflicts with target-owned platform policy |
| platform_termination | package shutdown path and target platform mode are known | `site:{platform_official_domain} {platform_or_provider} {platform_mode} termination grace signal drain restart {claim_phrase}` | provider authority for signal, grace, eviction, restart, or lifecycle behavior | production policy or workload still requires accountable staged validation |
| secret_provider_integration | provider, identity mode, framework, and rotation question are explicit | `site:{secret_provider_official_domain} {platform_or_provider} {framework_name} identity secret rotation {claim_phrase}` | official secret or identity provider integration and security guidance | search contains private credential context or is treated as organizational authorization |
| ci_artifact_provenance | actual CI, runner, artifact system, and promotion issue are mapped | `site:{ci_official_domain} {ci_or_artifact_system} {runner_or_registry_version} artifact provenance immutable promotion {claim_phrase}` | official pipeline or artifact-system documentation | result cannot prove target workflow, permissions, digest continuity, or release policy |
| provider_incident_or_deprecation | exact provider component and target impact question are known | `site:{platform_official_domain} {platform_or_provider} advisory deprecation incident {claim_phrase}` | official provider notice, advisory, status history, or deprecation material | live incident response needs incident command rather than solitary research |
| maintainer_security_advisory | exact component, version, and sensitive handling policy are established | `site:{maintainer_advisory_domain} {component_name} {component_version} security advisory` | maintainer advisory or target-approved vulnerability authority | query would expose private vulnerability details or risk acceptance is required |
| release_notes_exact_component | current and candidate component versions plus affected behavior are known | `site:{official_component_domain} {component_name} {component_version} release notes changelog {claim_phrase}` | official versioned release or upgrade notes | broad changelog does not answer the bounded target consequence |
| official_source_or_test | applicable docs are ambiguous and official repository/tag is known | `site:github.com/{official_org}/{official_repo} {version_tag} {symbol_or_behavior} test` | official source and tests at released tag used as implementation evidence | implementation detail is mistaken for promise or public fork outranks maintainer source |
| current_sample_discovery | an option needs executable orientation after primary behavior is known | `site:github.com/{official_org} {framework_name} {framework_version} sample {claim_phrase}` | official sample or guide used for vocabulary and entry points | sample becomes production policy or hides failure, security, data, and recovery work |

Brace fields such as `{database_official_domain}` and `{official_org}` must come from verified maintainer ownership, not from a search result that merely looks official.

**Future refresh protocol**

1. State the target decision and strongest currentness uncertainty in one sentence.
2. Record target revision, artifact, effective versions, execution mode, and owner policy relevant to the claim.
3. Select the authority that owns the behavior. Prefer direct versioned documentation or known official release material over open search when available.
4. Sanitize the query and confirm no private incident, customer, credential, account, or unreleased security detail is included.
5. Run the narrowest query or direct lookup. Record exact query, retrieval time, selected result, version selector, and rejected near-matches.
6. Open and read the complete relevant section. Do not adopt a result snippet or generated summary.
7. Extract one bounded fact with prerequisites, exceptions, defaults, version, and source role. Keep conflicts visible.
8. Compare the fact to effective target mechanism and policy. Stop if it is irrelevant or another owner controls the decision.
9. Design and run the target scenario capable of disproving the operational consequence.
10. Update only dependent decisions, gates, runbooks, and source roles. Preserve stronger claims not proved.

**Query result evaluation**

Reject or downgrade a result when:

- it defaults to latest while target uses another release;
- it describes a different framework, engine, platform mode, product edition, architecture, or execution model;
- it is a tutorial, representative repository, forum, generated summary, or search snippet used for a normative claim;
- it omits prerequisites, exceptions, compatibility, failure, or recovery that decide the target outcome;
- it is an official source for the wrong ownership layer;
- it redirects, is archived, unmaintained, or refers to a default branch rather than a release;
- it conflicts with target policy or observed behavior and the conflict is not resolved;
- the target scenario cannot exercise the consequence and the limitation is hidden.

Official status establishes provenance, not target applicability. Multiple secondary pages repeating one statement do not increase independent confidence.

**Research ledger**

```text
research_decision_id:
target_revision_artifact:
resolved_coordinates_and_mode:
claim_and_consequence:
query_or_direct_lookup:
sensitive_context_excluded:
retrieved_at:
selected_source_and_version:
source_owner_and_role:
rejected_results_and_reason:
extracted_fact:
prerequisites_exceptions_defaults:
conflicting_evidence:
target_mechanism_locator:
target_scenario_and_result:
stronger_claim_not_proved:
dependent_artifacts_updated:
refresh_or_invalidation_event:
```

Stop research when the exact claim is supported enough for the accepted risk, when target execution or owner policy is the remaining uncertainty, or when available sources cannot resolve conflict. Preserve a conditional decision rather than broadening queries indefinitely.

Curate queries from consequential reuse. Keep those that repeatedly reach the owning authority and change a target decision. Revise queries that return wrong versions or ownership layers. Retire queries whose component, terminology, provider, or decision no longer exists. Selective refresh should make future research smaller, not accumulate a permanent broad browsing ritual.

## Evidence Boundary Notes

Evidence labels apply to bounded claims, not whole documents or domains. A reputable source can be irrelevant to the target; a target result can disprove an assumption without explaining the cause; a recommendation can remain useful while its named tool becomes obsolete.

**Evidence role taxonomy**

| evidence_role | claim_it_can_support | required_locator_and_scope | cannot_support_alone |
| --- | --- | --- | --- |
| `local_corpus_sourced_fact` | what an identified frozen local source states, including historical doctrine, warnings, headings, and routes | path, hash or version, complete relevant region, and exact extracted claim | current public behavior, target adoption, target policy, or production outcome |
| `local_corpus_hierarchy_note` | how frozen local sources relate for a named question | source inventory, claim-level role, companion route, and conflict | universal precedence or current organizational ownership |
| `external_mapping_unrefreshed_note` | that a dated local brief or generated reference recorded a public location or summary | frozen path, date, URL or source name, and no-retrieval statement | current content, release, compatibility, maintenance, security, or applicability |
| `refreshed_external_fact` | one bounded statement retrieved from applicable primary authority in authorized future work | exact URL or revision, retrieval time, version selector, prerequisites, exceptions, and claim | target configuration, owner policy, deployment behavior, or stronger neighboring claims |
| `target_instruction_fact` | what applicable repository or directory instructions require | exact instruction locator, scope, target revision, and conflict status | runtime success or organizational policy outside its scope |
| `target_policy_fact` | what an accountable service, security, data, platform, release, or incident owner requires | owned policy version or decision, applicability, enforcement, exception path, and authority | technical feasibility or observed compliance |
| `target_implementation_fact` | what the target effectively uses for wrapper, versions, code, config, data, artifact, pipeline, platform, or runbook | revision, file or system locator, effective value or identity, and environment | supported future behavior or successful outcome without execution |
| `observed_result` | what a qualified command, gate, drill, staged scenario, incident, or measurement produced | artifact, config, environment, input or state, action, output, final state, and time | untested populations, other environments, causal certainty, or future behavior |
| `negative_or_contradictory_evidence` | that an expected state was absent or a claim failed under a qualified scenario | expected observation, gate validity, actual result, alternatives, and preserved state | the cause when several hypotheses remain plausible |
| `combined_evidence_inference_note` | a systems conclusion joining local, target, observed, and optionally refreshed external facts | premises by role, causal reasoning, counterargument, scope, and invalidation event | fact status or owner acceptance merely because the reasoning is coherent |
| `engineering_judgment` | a choice among supported alternatives based on consequence, reversibility, burden, and risk | decision owner, options, evidence, weighting, hard gates, and residual uncertainty | measurement or policy authority not actually obtained |
| `forecast_or_hypothesis` | an expected effect or causal model to test | baseline, mechanism, predicted observation, counter-hypothesis, and discriminating gate | observed improvement, capacity, reliability, or production readiness |
| `conditional_claim` | the exact subset supported while another environment, owner, version, or scenario remains unavailable | passed evidence, missing boundary, affected stronger claim, owner, and next gate | whole-route readiness or an average confidence value |
| `superseded_or_rejected_claim` | why prior guidance no longer applies or was not chosen for a target | prior source or decision, replacement or rejection reason, consumers, and reopening event | proof that every historical use was wrong |

`external_research_sourced_fact` from the seed should be used only as a compatibility alias for a truly retrieved and bounded `refreshed_external_fact`. In this evolution, no public source was retrieved, so no current external fact was created. The four original public rows and the broader 2026-06-23 research brief remain `external_mapping_unrefreshed_note` material.

**Application rules**

1. Break a consequential statement into claims when source role, version, target scope, confidence, or next evidence differs.
2. Attach the strongest accurate role, not the most prestigious available source.
3. Preserve source date or version and target artifact or environment. Evidence detached from scope decays into folklore.
4. Distinguish recommendation from requirement. Local doctrine may recommend typed config; target policy and implementation decide the mechanism; startup scenarios show the result.
5. Distinguish supported behavior from implementation detail. Official source can clarify a released mechanism without becoming a public contract.
6. Distinguish target state from target success. A configured readiness endpoint is a fact; safe platform traffic under dependency failure is an observed outcome only after exercise.
7. Label synthesis where several facts imply guidance. Include a counterargument and the event that would change it.
8. Keep inaccessible environments conditional. Name exactly which release or operational claim they block.
9. Preserve conflicts and failed results. Do not smooth them into confidence language or select the convenient source silently.
10. Link consumers and invalidation events so version, artifact, policy, platform, or incident changes trigger selective review.

**Evidence precedence and conflict**

No label universally wins. Resolve by ownership and applicability:

- Safety, access, and accountable authority constrain action even when another source recommends it.
- Applicable target policy governs accepted mechanism and risk within its scope, but cannot make incompatible behavior succeed.
- A qualified observed failure can disprove target readiness under its conditions, even when documentation says the mechanism is supported.
- Target implementation fact establishes what is used; version-applicable primary authority establishes what the component supports; execution establishes the scoped outcome.
- Frozen local doctrine selects questions and alternatives but does not override current target state or provider semantics.
- Tutorials, samples, duplicated summaries, and search snippets orient; they do not settle consequential compatibility, security, or recovery decisions.

When evidence conflicts, first check version, artifact, config, environment, product mode, owner scope, default versus effective behavior, and observation quality. If conflict remains, preserve both claims and run a scenario that discriminates them where safe. Escalate policy, compliance, risk, or destructive recovery to the accountable owner.

**Negative and absent evidence**

Absence is meaningful only when the observation path was expected and qualified. No alert during an incident may mean no failure, broken emission, delayed collection, wrong query, changed routing, or missing access. A test pass may mean correct behavior, empty selection, skipped task, stale cache, unrealistic fixture, or wrong artifact.

For a negative result, record:

- what should have been observed and why;
- which artifact, config, input, data, environment, and time were in scope;
- whether the gate, signal, and independent state source were healthy;
- what was actually observed;
- competing explanations;
- whether the result blocks, narrows, or reroutes the claim;
- the next discriminating action and owner.

A failed target scenario can outweigh a generic recommendation for adoption while leaving root cause uncertain. Do not promote uncertainty into a confident alternative mechanism.

**Mixed-claim examples**

Typed config:

- `local_corpus_sourced_fact`: the frozen runtime source recommends typed configuration, startup validation, and boundary injection.
- `target_implementation_fact`: the inspected service uses a specific framework binding mechanism and effective profile.
- `combined_evidence_inference_note`: preserving that mechanism and adding a bounded typed field minimizes scope while enforcing the new contract.
- `observed_result`: packaged startup accepts valid input and rejects missing and malformed values under the recorded artifact and environment.
- `conditional_claim`: managed secret rotation remains unproved because provider access was unavailable.

Migration:

- `local_corpus_sourced_fact`: frozen doctrine treats migrations as deployed code and recommends production dialect, versioned changes, compatibility, and recovery planning.
- `target_implementation_fact`: the repository contains a specific migration history and supported application artifacts.
- `engineering_judgment`: the data and release owners select staged expansion and later contract over one-step replacement.
- `observed_result`: supported prior schemas with representative rows pass mixed-version and partial-recovery scenarios.
- `forecast_or_hypothesis`: target-scale lock behavior is expected to remain bounded but requires staged measurement.

Health:

- `target_implementation_fact`: a framework endpoint reports a configured readiness state.
- `refreshed_external_fact` in future authorized work could establish version-specific framework semantics.
- `target_policy_fact`: the platform owner defines how readiness controls traffic and how liveness controls restart.
- `observed_result`: induced dependency failure removes or retains traffic and avoids restart amplification under the staged platform scenario.
- The framework fact alone cannot support the final traffic-safety claim.

Wrong artifact incident:

- `observed_result`: deployed digest differs from the artifact recorded by required CI gates.
- `negative_or_contradictory_evidence`: the release claim that tested bits reached the environment is false for that event.
- `combined_evidence_inference_note`: diagnosis should start at artifact promotion before attributing behavior to the source change.
- `engineering_judgment`: the release and incident owners choose containment and recovery after checking data and compatibility.

**Proportional evidence records**

| artifact_or_decision | minimum_durable_record |
| --- | --- |
| low-risk orientation | source role, question, target assumptions, and stronger claim not made |
| implementation decision | requirement, target facts, local doctrine, alternatives, synthesis, gate, result, and owner |
| public-currentness decision | target coordinate, refreshed source, version and retrieval, extracted fact, conflict, and target scenario |
| release decision | revision, artifact, config, data, gate results, stage, stop and recovery, owner, and conditional boundaries |
| runbook or automation | signal and state contract, action authority, procedure version, rehearsal, consumers, and invalidation |
| incident or recovery | initial state, timeline, artifacts, actions, observations, authority, final state, residual repair, and causal uncertainty |

**Claim ledger**

```text
claim_id:
claim_text_and_scope:
evidence_role:
source_or_target_locator:
hash_version_artifact_environment:
retrieval_or_observation_time:
prerequisites_exceptions_population:
supporting_evidence:
contradictory_or_negative_evidence:
inference_or_judgment:
verification_action_and_result:
stronger_claim_not_supported:
confidence_reason_and_uncertainty:
decision_owner:
consuming_artifact_gate_runbook:
invalidation_event:
supersession_or_retirement:
```

Verify ledger structure automatically where possible: required roles, path existence, frozen hashes, target locators, result identities, and unresolved conflicts. Sample the most consequential and weakest claims for semantic entailment; automation cannot decide whether nuanced prose truly follows from a source.

**Established boundary for this evolution**

Known directly:

- the archive seed and working reference began byte-identical before evolution;
- the complete archive seed, working reference, governing specification, focused verifier, Beta progress journal, and required frozen runtime source were read;
- frozen local paths, headings, source content, research date, and hashes recorded in this reference were inspected locally;
- no browsing occurred, so public mappings were not refreshed;
- the evolved guidance is systems synthesis unless a claim is explicitly tied to frozen local content or later target evidence.

Not established by this reference alone:

- which future repository uses Spring, Ktor, Gradle, Maven, a particular database, migration tool, telemetry stack, image, CI, provider, or platform;
- current public releases, defaults, compatibility, advisories, or provider behavior;
- any universal latency, throughput, capacity, reliability, retry, service-objective, or recovery value;
- production readiness, security acceptance, data safety, traffic behavior, shutdown correctness, or recovery for an uninspected target;
- authority to mutate shared or production systems.

Before this file is reported complete, deterministic verification must confirm exact heading order, all section expansions, packet counts, exact and normalized uniqueness, source hashes, tables, fences, ASCII, whitespace, unresolved-marker absence, focused verifier success, and bounded complete rereads. Those results belong in the lane journal and final work report; prose cannot self-certify them.

Evidence boundaries are lifecycle controls. When a source, version, artifact, config, data state, platform, owner policy, gate, workload, or incident changes, invalidate only dependent claims and rerun their evidence. Retire superseded claims and migrate consumers. Uncertainty then becomes maintained system state rather than a disclaimer detached from the decision.
