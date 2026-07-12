# Kotlin Backend Reference Routing

Use this reference to choose the smallest ordered Kotlin-backend source set that can turn a request into an executable next action without hiding a changed failure boundary. It is a router, not a substitute for target code, requirements, framework documentation, tests, or accountable product and operational decisions.

The routing result should contain:

- the backend surface and existing framework;
- the primary mode and any activated risk modes;
- the ordered local references to read;
- target artifacts and owners still required;
- the first behavior or failure to verify;
- the condition that expands, narrows, supersedes, or stops the route.

**Default routing sequence**

1. Classify the surface as Spring MVC, Spring WebFlux, Ktor, worker, message consumer, scheduled job, persistence change, external client, migration, deployment, or review.
2. Preserve the repository's Spring or Ktor stance, Gradle or Maven wrapper, Kotlin and Java targets, dependency versions, persistence stack, and deployment model unless migration is explicitly requested.
3. State the dominant risk: ambiguous behavior, framework integration, domain modeling, persistence, coroutine cancellation, security, resilience, testing, or operations.
4. Read `reference-map.md` to select modes and an order.
5. Read `kotlin-backend-playbook.md` for service anatomy and shared boundary decisions when implementation shape is involved.
6. Read the Spring or Ktor portions of `kotlin-spring-ktor-idioms.md` only after the framework stance is known.
7. Read `kotlin-backend-testing-and-fixtures.md` for the boundary that must prove the requirement.
8. Add `kotlin-backend-security-and-resilience.md` when auth, validation, cancellation, retries, idempotency, external systems, or durable background work changes.
9. Add `kotlin-backend-runtime-and-ops.md` when config, secrets, observability, migrations, CI, containers, deployment, or rollback changes.
10. Use `sources-and-research-brief.md` when evaluating provenance or revising doctrine; do not treat its dated public-source summary as current retrieval.
11. Inspect the routed target files, write observable requirements, discover repository-native commands, and verify the changed boundary.
12. Reassess the route after the first failing or passing evidence; expand only when the result exposes another consequential dependency.

**Mode router**

| Mode | Activate from changed behavior | First local destination | Typical companion |
|---|---|---|---|
| Spec | Request is vague, acceptance is absent, or a non-functional claim is not measurable | `kotlin-backend-playbook.md` | Testing reference after requirements identify the failing boundary |
| Spring Boot | Controllers, services, repositories, configuration, MVC, WebFlux, Spring Data, or Spring Security change | Spring sections of `kotlin-spring-ktor-idioms.md` | Playbook first for a new service boundary; testing for slices and wiring |
| Ktor | Routes, plugins, serialization, status pages, auth, resources, or `testApplication` change | Ktor sections of `kotlin-spring-ktor-idioms.md` | Playbook for service boundaries; testing for route and plugin behavior |
| Persistence | JPA, JDBC, Exposed, jOOQ, transaction scope, query behavior, or schema changes | Persistence sections of `kotlin-backend-playbook.md` | Testing for real dialect behavior; runtime/ops for migration rollout |
| Coroutine | Suspend, Flow, dispatcher, cancellation, timeout, or blocking isolation changes | Coroutine sections of `kotlin-backend-playbook.md` | Security/resilience for cancellation and external-call failure semantics |
| Security | Authentication, authorization, sessions, tokens, CSRF, passwords, validation, or reset flow changes | `kotlin-backend-security-and-resilience.md` | Framework lane for configuration and testing reference for denied paths |
| Resilience | Retry, idempotency, external API, timeout, queue, worker, or transaction failure changes | `kotlin-backend-security-and-resilience.md` | Runtime/ops for operational signals and testing for failure injection |
| Operations | Typed config, secrets, logs, metrics, health, CI, container, deploy, or rollback changes | `kotlin-backend-runtime-and-ops.md` | Testing for production-like config, migration, and smoke behavior |
| Review | Modernization, production readiness, framework misuse, or hardening is requested | Security/resilience, then runtime/ops | Testing, then playbook to reconcile service design |

Mode selection is additive but not indiscriminate. A new Spring MVC read endpoint normally needs Spec, Spring, and Testing modes. It does not automatically need coroutine or persistence guidance when it calls an existing synchronous application service and changes no storage behavior. An external write with retry may need Spec, framework, Coroutine, Resilience, Operations, and Testing because cancellation, idempotency, timeout budgets, telemetry, and failure injection are part of the same correctness chain.

**Routing invariants**

- Preserve the existing framework by default. Do not turn feature delivery into an unrequested Spring-to-Ktor or Ktor-to-Spring migration.
- Select modes from behavior and failure consequence, not from imported keywords or fashionable tools.
- Load the service playbook before framework detail when ownership, transaction, domain, or integration boundaries are unclear.
- Load testing guidance early enough to shape the design, not after implementation is fixed.
- Treat suspend syntax as an execution-model question, not proof that blocking work is non-blocking.
- Treat a valid parser or framework result as distinct from authorization, business semantics, migration safety, and operational readiness.
- Use repository wrappers and configured tools; a generic command is a discovery lead, not observed evidence.
- Preserve dated local research as provenance and mark current external behavior unverified until retrieved and reconciled.

**Direct fit**

Use this router for Kotlin/JVM HTTP APIs, services, workers, queue consumers, scheduled jobs, persistence changes, external clients, auth flows, migrations, production-readiness reviews, and backend architecture decisions. It is especially useful when several references could apply and context must be narrowed without dropping security, cancellation, persistence, testing, or rollout obligations.

Route elsewhere for Android UI, Kotlin Multiplatform client work, general Kotlin syntax questions unrelated to backend delivery, or non-Kotlin services. Use a framework migration plan when changing Spring and Ktor is the actual task. Use product, security, data, or operations ownership when the unresolved decision is policy rather than reference selection.

**Good, bad, and conditional routes**

Good: a new Spring MVC endpoint with a database write reads the playbook, Spring idioms, testing, persistence, and migration sections. The route preserves Spring and the existing database stack, writes behavior and migration requirements, and discovers focused test plus build commands from the repository.

Bad: a request mentions coroutines, so the agent loads every Kotlin reference, recommends Ktor despite an established Spring MVC service, and calls the design non-blocking without inspecting JDBC. Keyword matching expanded context while weakening the target boundary.

Conditional: a Ktor route calls an external provider through an existing client. Start with Ktor, Coroutine, Resilience, and Testing. Add Operations when timeout, retry, metrics, config, or deployment behavior changes; omit persistence if no durable state or idempotency record changes. The route remains provisional until target call and cancellation paths are inspected.

**Routing evidence record**

```text
Task and observable outcome
Backend surface, framework, build, Java target, and deployment stance
Primary mode and activated risk modes
Ordered local references and relevant sections
Target code, config, schema, tests, and owner evidence required
Rejected modes and why their boundary is unchanged
First failing or passing behavior to reproduce
Repository-native commands discovered and observed results
Open uncertainty, expansion trigger, stop condition, and route owner
```

The local corpus establishes the historical mode vocabulary and read orders. It does not establish current public API behavior, the target repository's versions, or the correctness of a future implementation. A route can be structurally correct yet insufficient for one service; confidence rises only when its target artifacts and verification results agree.

Repeated route expansion is a decomposition signal. If one request requires unrelated framework, data, security, migration, and operations changes that cannot be accepted independently, split the work into decision-complete slices rather than treating a larger context window as architecture.

## Source Evidence Mapping Table

The two seed paths are the first retrieval surface, not the whole evidence graph. `reference-map.md` routes work and `sources-and-research-brief.md` explains the dated doctrine. The routes point to the entrypoint and five specialized references whose actual scope determines whether the route is accurate.

Complete local reads and hashes establish frozen content. They do not establish current public APIs, target repository conventions, or that a future implementation works.

**Fully read local artifacts**

| Artifact and SHA-256 | Direct local contribution | Important non-authority boundary | First applicability gate |
|---|---|---|---|
| `references/reference-map.md`, `7451085f357ed6af8fdd41f592e83f5f4b5c7aa858be8a5456390b377f00f180` | Nine routing modes and five common read orders; directs doctrine updates to the research brief | Does not define target code, versions, requirements, commands, or implementation correctness | Classify one changed surface and confirm every destination exists and contributes a distinct decision |
| `references/sources-and-research-brief.md`, `2f73340890073548e7c9a723ba051528e0097581444889cc7a8fa400026a1ee1` | Research date, premise check, expert lenses, chosen Spring/Ktor thesis, evidence summary, and provenance questions | Summarizes public research as of 2026-06-23; no external content was refreshed in this evolution | Use for historical rationale; retrieve direct current authority only when a selected mechanism requires it |
| `SKILL.md`, `e3413837049aa6f31d325fa368bb8b9dcce7f298c770b42cd5f13c1217c3a410` | Trigger boundary, mode combinations, delivery workflow, output contract, guardrails, and progressive context strategy | An entrypoint can coordinate references but cannot prove target wiring or runtime outcomes | Compare requested work with target framework, build, service surface, and failure boundary |
| `references/kotlin-backend-playbook.md`, `8654c3a4c68cda2514c546035e7a7908a99ad0f884088b7bf329abf807c31994` | Service anatomy, framework preservation, executable requirements, Kotlin boundary types, persistence, transactions, coroutines, clients, workers, and API defaults | Shared service guidance does not settle framework-specific APIs, policy, schema, or operational targets | Map target transport, application, domain, persistence, integration, and runtime boundaries and test the changed one |
| `references/kotlin-spring-ktor-idioms.md`, `02c20786240e893fc258f4e067557bc65dcdafcac11a6efbdd049710b827ac5d` | Separate Spring and Ktor structure, compiler plugins, configuration, execution models, validation, persistence, route plugins, testing, and cross-framework Kotlin idioms | Framework examples do not authorize migration or match every pinned version | Preserve the existing framework and inspect its actual plugins, annotations, dependency line, and tests |
| `references/kotlin-backend-testing-and-fixtures.md`, `92f45a34cc8ac472b930eba33e4ffb6a442719baa53dd8caabd43006dfa99e26` | Boundary-first test selection across unit, Spring slices, Ktor test host, real persistence, contracts, migrations, retries, and quality gates | Generic test types and command names may be absent or configured differently | Discover repository wrappers and prove the boundary whose behavior can actually change |
| `references/kotlin-backend-security-and-resilience.md`, `8a07eb77e27a3b508224db76c60e20508b8b3d13b81fce86e87ea052be7d14a5` | Trust boundaries, auth, sessions, CSRF, validation, coroutine cancellation, blocking, retries, idempotency, external clients, and durable work | Does not define target threat model, approved algorithms, auth policy, or provider semantics | Exercise allowed and denied paths, cancellation, timeout, retry classification, duplicate effects, and secret redaction |
| `references/kotlin-backend-runtime-and-ops.md`, `d0a218f3c5d7b07c561cd4aba94b7c943aa7575cd439d371fdbaf4e5415b1069` | Build discipline, static analysis, typed config, secrets, observability, migrations, containers, CI, deployment, and operational review | Does not establish a target service objective, platform, rollout policy, or configured tool | Inspect build, config, deploy, migration, observability, health, shutdown, and rollback artifacts in the repository |

The entrypoint and reference map overlap intentionally as navigation. They are distinct files, but repeated mode names are not independent proof that a backend design is safe. The testing, security, and runtime files also contain complementary checks; loading all three does not make an unexecuted recommendation observed fact.

**Inherited public locations**

No browsing occurred. The following are `external_mapping_unrefreshed_note` records inherited from the seed and research brief, not current external facts:

| Location | Likely future authority question | What it cannot establish here | Refresh and target gate |
|---|---|---|---|
| `https://kotlinlang.org/docs/home.html` | Current Kotlin language, compiler, interop, and server-side documentation after a concrete feature is selected | Target framework, build, service architecture, or repository support | Retrieve the direct mechanism page for the pinned Kotlin line and run target compilation and behavior checks |
| `https://github.com/Kotlin/kotlinx.coroutines` | Current coroutine library release, API, and implementation evidence for a selected cancellation or dispatcher question | Correct use in Spring, Ktor, JDBC, provider clients, or a production request path | Inspect the pinned dependency and direct docs or source, then exercise cancellation, timeout, and blocking boundaries |
| `https://github.com/spring-guides/tut-spring-boot-kotlin` | Current Spring-maintained Kotlin sample for a narrowly comparable application shape | Target architecture, security, persistence, version compatibility, or production policy | Compare pinned Spring and Kotlin versions and reproduce the relevant target behavior rather than copying structure wholesale |
| `https://ktor.io/docs/welcome.html` | Current Ktor documentation root for a selected route, plugin, serialization, auth, or test mechanism | Target plugin installation, DI, error contract, external client, or deployment behavior | Retrieve the exact Ktor page for the pinned version and run target route or plugin fixtures |

Recognizable publishers do not convert these mappings into current evidence. The 2026-06-23 research brief records historical retrieval and synthesis; a new compatibility, upgrade, security, or API claim requires a new direct source and target reconciliation.

**Target applicability evidence**

| Evidence class | Routing question answered | Required identity | Frequent overreach |
|---|---|---|---|
| Project instructions and ownership | Which conventions, scope, and review authority govern the change? | Instruction path, owner, revision, and applicable directory | Treating generic skill guidance as project policy |
| Build and dependency model | Which Kotlin, Java, Spring, Ktor, compiler plugins, database, and test tools are actually pinned? | Wrapper, manifest, lock or catalog, effective versions, and build result | Recommending a plugin or framework from memory |
| Service topology | Which transport, application, domain, persistence, integration, worker, and runtime boundaries exist? | Entry points, packages, dependency edges, and owning modules | Mapping filenames to architecture without callers and runtime wiring |
| API and schema contract | Which request, response, message, database, and migration semantics are authoritative? | Contract or schema revision, compatibility policy, and owner | Treating DTO annotations as the whole business invariant |
| Execution model | Where are blocking calls, suspend boundaries, dispatchers, pools, deadlines, and cancellation scopes? | Call path, runtime configuration, dependency behavior, and observed task | Assuming suspend means non-blocking |
| Security and policy | Which identities, permissions, validation, secrets, abuse cases, and data rules apply? | Threat or policy owner, config, tests, and negative-path result | Inferring authorization from authenticated routing |
| Verification infrastructure | Which unit, slice, host, integration, migration, contract, and smoke gates are available? | Test target, fixture, command, environment, result, and limitation | Calling a generic Gradle command observed evidence |
| Operations and rollout | How are config, observability, health, deployment, migration, rollback, and incidents handled? | Deployment artifact, environment, service objective, runbook, and owner | Treating Actuator or logging presence as operational readiness |

**Source disposition record**

```text
Source path, region, revision, and SHA-256
Evidence role: route, shared doctrine, framework, test, risk, runtime, or provenance
Exact task and changed service boundary
Recommendation extracted and important omitted concern
Target framework, versions, code, config, schema, and owner inspected
Behavior, negative path, command, environment, and observed result
Conflicts, rejected alternatives, residual uncertainty, and invalidation event
```

Good use routes a new Spring persistence endpoint through map, playbook, Spring idioms, testing, migration, and transaction guidance, then verifies target repository wiring and production dialect behavior. Bad use copies a coroutine recommendation from the dated research brief and calls a blocking JDBC path non-blocking. Borderline use selects a migration order correctly but cannot identify the repository's migration tool or rolling-deploy policy; keep the route provisional and stop before rollout claims.

A source change should invalidate only its consumers. Mode-order changes reopen route records; service-anatomy changes reopen shared design; Spring or Ktor changes reopen their framework lane; test-strategy changes reopen verification matrices; security or resilience changes reopen affected trust and failure paths; runtime changes reopen deployment and migration evidence. This dependency model makes progressive disclosure maintainable instead of merely shorter.

## Pattern Scoreboard Ranking Table

The inherited values 95, 91, and 88 are editorial seed ordering. No rubric, population, sample, scale, calibration, or routing outcome supports interpreting them as confidence, quality, coverage, priority weight, adoption, or effectiveness. Preserve them for provenance only.

| Priority | Inherited value or role | Activate when | Failure prevented | Direct falsifier |
|---|---|---|---|---|
| Source Map First | 95; historical default | Selecting among the local Kotlin backend references | Agent loads a broad or fashionable source set without knowing the available routes | Route record names map entry, destinations, relevant sections, and why each changes the next action |
| Evidence Boundary Split | 91; historical default | Local doctrine, dated public summaries, target behavior, and synthesis appear together | Historical or generic guidance is presented as current repository fact | Every consequential claim is labeled by evidence role, scope, version, and target gate |
| Verification Gate Coupling | 88; historical default | A route recommends a framework, boundary, test, migration, retry, or operational action | Plausible advice has no way to fail | Recommendation names target artifact, behavior, command or review task, expected result, and limitation |
| Surface Before Mode | First routing gate | A request arrives as a feature label or technology list | Modes are selected from keywords rather than changed behavior | Transport, worker, persistence, integration, migration, deployment, or review surface is named |
| Preserve Framework And Versions | Hard compatibility gate | Spring, Ktor, build, compiler plugin, database, or runtime choice is implicated | Feature work becomes an unrequested migration or version churn | Route records existing framework, wrappers, Kotlin and Java targets, dependencies, and explicit migration authority |
| Executable Outcome | Hard specification gate | Success is vague or non-functional language appears | Sources are loaded before the behavior and consequence are testable | Observable requirement identifies valid, invalid, failure, and recovery behavior |
| Service Boundary Map | Hard design gate | Ownership, transaction, blocking, or external-call placement is uncertain | Framework syntax hardens around the wrong layer | Transport, application, domain, persistence, integration, and runtime responsibilities are located or explicitly absent |
| Framework Lane | Hard implementation gate | Controller, route, plugin, configuration, serialization, DI, or framework testing changes | Spring and Ktor idioms are blended or wrong-version APIs are assumed | Only the existing framework lane is selected and target wiring confirms its scope |
| Risk Mode Activation | Consequence gate | Persistence, coroutine, security, resilience, or operations behavior changes | Cross-cutting risk is omitted because the visible task is small | Each activated mode maps to changed behavior and each omitted mode has a bounded reason |
| Boundary-First Testing | Hard evidence gate | Requirements and design identify a boundary that can fail | Full startup or unit tests are chosen by habit rather than proof need | Verification matrix selects the lightest target test that exercises the real boundary and negative path |
| Cancellation And Blocking Truth | Hard execution gate | Suspend, Flow, WebFlux, Ktor coroutine, JDBC, JPA, files, or provider clients interact | Blocking work is called non-blocking and cancellation or pool pressure disappears | Call path identifies blocking operations, dispatcher or intentional blocking model, timeout, and cancellation observation |
| Transaction And Migration Truth | Hard data gate | Writes, schema, queries, rolling deploys, or idempotency change | Data design is routed as ordinary endpoint code | Transaction scope, migration compatibility, production dialect, roll-forward, and duplicate-effect behavior are explicit |
| Security Negative Paths | Hard trust gate | Auth, claims, sessions, input, secrets, or public error behavior changes | Happy-path authentication is mistaken for authorization and abuse resistance | Allowed, unauthenticated, denied, malformed, expired, and sensitive-log paths are tested as applicable |
| Runtime And Rollout | Promotion gate | Config, health, metrics, deployment, shutdown, or live traffic changes | Code-level success is mistaken for deployable safety | Production-like config, readiness, migration, smoke, rollback or roll-forward, and observability evidence are named |
| Route Reassessment | Learning gate | First target evidence passes, fails, or exposes another boundary | Initial routing assumptions persist after the task shape changes | Route expands, narrows, splits, or stops with an evidence-backed reason |

**Default construction order**

For new feature work: define observable behavior; classify surface; preserve framework and versions; inspect service boundaries; select one framework lane; activate changed risk modes; choose verification at the boundary that can fail; then read and implement. Add runtime and rollout guidance before deployment behavior is fixed when configuration, migrations, or external effects change.

**Repair and review overrides**

Preserve the failing artifact and start at the earliest known causal break:

- a leaked token or unintended access elevates Security before general service design;
- a request that continues after disconnect elevates Coroutine and Resilience;
- duplicate provider writes elevate idempotency, transaction, and external-client boundaries;
- a migration failure during rollout elevates Runtime/Operations and Persistence;
- a Ktor route returning the wrong error envelope elevates framework error mapping and route testing;
- a Spring slice passing while production wiring fails elevates full wiring, configuration, and deployment evidence.

After containment, reconcile the failure with executable requirements and the full state-to-runtime path. An incident-specific starting point does not eliminate upstream design or downstream regression work.

**Route profiles**

- **Focused endpoint:** Spec, existing framework, playbook boundary, and testing; add persistence or security only when behavior changes there.
- **External workflow:** Spec, framework, Coroutine, Resilience, Testing, and Operations when timeout, retry, metrics, or deployment behavior changes.
- **Persistence or migration:** Playbook persistence, Testing, Runtime/Operations migration and rollout, then Security/Resilience for transaction and idempotency semantics.
- **Auth or account flow:** Spec, framework, Security, Testing, and Operations where secrets, sessions, metrics, or deployment config change.
- **Production hardening:** Security/Resilience, Runtime/Operations, Testing, then Playbook and framework sections to reconcile design.

Good prioritization identifies the first omitted contract that can make behavior wrong, unsafe, unrecoverable, or undeployable. Bad prioritization loads every file, counts coverage as confidence, and changes the framework before inspecting target code. Borderline orientation may select a provisional route when repository access is incomplete, but it must name the missing artifact and prohibit implementation-ready claims.

Numeric rank cannot rescue a wrong surface, incompatible framework choice, fake non-blocking design, missing denied path, unsafe migration, or unobserved rollout. Retain override reasons and review recurring route failures. Repeated wrong-framework suggestions may require a stronger preservation gate; repeated missing migration work may move runtime guidance earlier; repeated broad context with no changed decisions may justify a narrower map. Change ordering from evidence, not from the apparent precision of seed numbers.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The frozen entrypoint and reference map define progressive Kotlin backend modes and ordered destinations. The routed files separate service anatomy, Spring and Ktor idioms, testing, security and resilience, runtime operations, and provenance.

`external_mapping_unrefreshed_note`: Public URLs and summaries in the 2026-06-23 research brief were not retrieved during this evolution. They provide historical research lineage and future retrieval targets, not current framework, coroutine, or compatibility facts.

`combined_evidence_inference_note`: Idiomatic Kotlin backend routing is an evidence-bounded feedback loop. It classifies the target surface and failure boundary, preserves the repository's framework and versions, loads only the local references needed to resolve changed risks, converts them into observable requirements and target-specific verification, then revises the route from results.

Use this loop:

1. **Name the outcome.** State who needs what backend behavior, valid and invalid conditions, failure consequence, and accountable owner.
2. **Inspect the target.** Read applicable instructions, wrappers, dependency versions, entry points, configs, schemas, migrations, tests, deployment artifacts, and service ownership.
3. **Classify the surface.** Identify Spring MVC, WebFlux, Ktor, worker, consumer, scheduled job, persistence, external client, migration, deployment, or review.
4. **Preserve compatibility.** Keep Spring versus Ktor, Gradle versus Maven, Kotlin and Java targets, compiler plugins, database stack, test framework, and runtime model unless change is explicitly accepted.
5. **Map service boundaries.** Locate transport, application, domain, persistence, integration, and runtime responsibilities; identify blocking, transaction, trust, and effect edges.
6. **Select modes.** Choose one primary mode and only the risk modes whose behavior or consequence changes.
7. **Retrieve progressively.** Read the map, shared playbook where service shape matters, one framework lane, testing for the failing boundary, then activated security, resilience, persistence, and runtime material.
8. **Write executable requirements.** Convert vague terms such as idiomatic, secure, non-blocking, resilient, fast, and production-ready into observable contracts.
9. **Design with the proof boundary visible.** Select DTO, domain, persistence, coroutine, transaction, client, worker, config, and rollout shapes that the target can verify.
10. **Execute target gates.** Use repository-native wrappers, fixtures, database dialect, framework test host, negative paths, build, static analysis, migration, smoke, and operational review as applicable.
11. **Reassess the route.** Expand when evidence exposes a missing consequential boundary; narrow when a source contributes no changed action; split when outcomes can be accepted independently.
12. **Freeze the handoff.** Record route, requirements, decisions, observed results, unresolved owners, stop condition, and invalidation events.

**Core principles**

- **Outcome before mode.** Technology words do not select references until the changed behavior and consequence are understood.
- **Target before generic preference.** Local code and explicit project policy decide framework, versions, build, and established architecture within their scope.
- **Framework preservation.** Spring and Ktor are separate lanes. Feature work is not permission to migrate between them.
- **Service shape before framework syntax.** A controller or route cannot own business invariants, transaction choreography, or durable external effects merely because the framework makes it convenient.
- **Modes follow failure boundaries.** Persistence, coroutine, security, resilience, operations, and review modes activate when their behavior or risk changes.
- **Testing shapes design.** The lightest test that proves the real boundary should be identifiable before implementation, with real infrastructure where dialect, migration, broker, or provider behavior matters.
- **Suspend is not non-blocking evidence.** Execution model, blocking dependencies, dispatcher or pool behavior, deadlines, and cancellation remain explicit.
- **Authentication is not authorization evidence.** Allowed, denied, malformed, expired, and sensitive-output paths need target policy and tests.
- **Migration is deployable behavior.** Schema compatibility, production dialect, expand and contract, roll-forward, rolling deploy, and recovery can affect the route before code is written.
- **Locality is not automatic authority.** A local source can be historically relevant, outdated, or weaker than explicit target policy and observation.
- **Public prestige is not target applicability.** A current official source can document a mechanism but cannot choose product semantics, repository conventions, or operational acceptance.
- **Every source earns context.** A loaded reference should retire an uncertainty, constrain a decision, add a gate, or expose a dependency; otherwise remove it from the route.

**Entry overrides**

New work normally follows the loop from outcome through target and route. Incident repair and production review may begin elsewhere:

- begin with Security and Resilience when access, secret, duplicate effect, provider failure, or cancellation is already reproduced;
- begin with Runtime and Operations when config, readiness, migration, deployment, shutdown, or rollback has failed;
- begin with Testing when a fixture exposes a contract gap and the design boundary is unclear;
- begin with Framework idioms when Spring or Ktor wiring is the observed fault;
- begin with the Playbook when ownership, transaction, domain, persistence, or integration placement is the disputed decision.

Preserve the failing input, versions, environment, and result before changing anything. Then reconcile executable requirements and upstream design so the repair does not become a one-off workaround.

**Route sufficiency**

A focused route is sufficient when every changed behavior has an owner, source, design boundary, negative path, verification method, and stop condition. It does not need every reference. A broad production-readiness review can legitimately load all specialized references because its acceptance scope includes trust, data, execution, verification, and operations.

The route is insufficient when:

- the framework or versions are guessed;
- the target service boundary cannot be located;
- a new public contract has no executable requirement;
- a coroutine route hides blocking work or cancellation;
- a write can retry without idempotency or effect observation;
- a storage change lacks migration and rollout evidence;
- security behavior has no denied path;
- the test type cannot exercise the real failing dependency;
- deployment or operational claims have no platform owner;
- current external behavior is asserted from the dated research brief.

**Examples**

Good: a Ktor route that calls a provider is classified as Spec, Ktor, Coroutine, Resilience, and Testing. Target inspection shows no persistence change. The route reads only those sections, defines timeout and cancellation behavior, normalizes provider errors, selects `testApplication` plus an HTTP mock or contract fixture, and adds Operations only when metrics or deployment config changes.

Bad: a Spring Data service request is routed from the word Kotlin to generic language advice. The agent proposes value classes and coroutines before inspecting JPA proxying, transaction scope, compiler plugins, or repository tests. The advice may be idiomatic in isolation and wrong in context.

Conditional: target files are unavailable during orientation. The router can identify likely modes and required artifacts, but the output remains provisional. It cannot claim a framework version, command result, migration safety, or production readiness.

**Verification ladder**

1. Confirm every routed path exists and its relevant heading supports the claimed role.
2. Confirm target framework, build, versions, surface, and owners from repository evidence.
3. Trace each mode to changed behavior and each omitted mode to a stable boundary.
4. Map each requirement to a target test or review that can fail for the right reason.
5. Execute the narrowest gate, then broader wiring, integration, migration, or operational gates only where required.
6. Compare observed failure with the route; add, remove, reorder, or split references deliberately.
7. Preserve results, limitations, and invalidation triggers in the handoff.

The thesis does not establish a universal Spring preference, Ktor preference, coroutine architecture, persistence library, test framework, latency threshold, or deployment model. The local corpus records one production-biased synthesis whose current target fit must be observed.

The durable artifact is a versioned route from an accepted backend outcome to a reproducible evidence set. Repeated route expansion is not a reason to load more indefinitely; it is evidence that independent changes may need separate requirements, owners, and delivery slices.

## Local Corpus Source Map

Use the map and entrypoint for orientation, then read complete relevant sections rather than isolated bullets. Load a companion reference when the chosen mechanism crosses its risk boundary. The paths below are frozen archive artifacts; target repositories may organize equivalent responsibilities differently.

**Routing and shared doctrine regions**

| Source region | Retrieve when | Durable question | Companion or trap | Target gate |
|---|---|---|---|---|
| `reference-map.md`: Mode To Reference Routing | Selecting primary and risk modes | Which behavior changed and which source owns the next question? | Keyword-only mode selection ignores target framework and consequence | Trace modes to changed requirements and omitted modes to stable boundaries |
| `reference-map.md`: Common Read Orders | Starting a known endpoint, route, migration, external workflow, or review | In which causal order should shared, framework, test, risk, and runtime guidance be read? | Read order is historical guidance, not target architecture proof | Confirm each destination exists and changes design or verification |
| `SKILL.md`: Mode Selection | Translating a user request into one or more modes | Which mode combination covers the complete accepted outcome? | Selecting every mentioned technology creates context without ownership | Record primary mode, companions, rejected modes, and reassessment trigger |
| `SKILL.md`: Workflow | Planning delivery end to end | Which requirements, boundaries, framework constraints, and quality gates must be visible? | Generic workflow can outrun target commands and project policy | Bind every stage to a target artifact, owner, or observed result |
| `SKILL.md`: Guardrails | Reviewing likely Kotlin backend mistakes | Which shortcuts require explicit exception evidence? | A guardrail can be wrong for a tiny intentional service or changed version | Reproduce the prohibited failure or document the bounded exception |
| `SKILL.md`: Context Strategy | Controlling long reference loads | What is the next smallest source that can reduce uncertainty? | Loading headings without caveats creates false sufficiency | Read complete relevant section and retain omitted-boundary note |
| `kotlin-backend-playbook.md`: Service Anatomy | Ownership or layering is unclear | Where do transport, application, domain, persistence, integration, and runtime decisions belong? | Layer count is not a mandate for needless abstraction in tiny services | Trace one request or job through actual target calls and effects |
| `kotlin-backend-playbook.md`: Framework Choice | Spring versus Ktor is questioned | What existing ecosystem and deployment facts should preserve the framework? | Feature delivery can hide an unrequested migration | Verify target framework, versions, dependencies, team ownership, and explicit migration scope |
| `kotlin-backend-playbook.md`: Executable Requirements | Success or non-functional language is vague | Which behavior and failure must become observable? | Example IDs and values are illustrative | Map accepted requirements to tests and operational checks |
| `kotlin-backend-playbook.md`: Domain And Error Modeling | Raw primitives, nullability, or exceptions cross boundaries | Which Kotlin types encode intent and expected outcomes? | Value classes and sealed hierarchies can conflict with serialization or framework reflection | Test target JSON, persistence, Java interop, and response mapping |
| `kotlin-backend-playbook.md`: Persistence And Transactions | Storage, queries, or writes change | Which persistence style, transaction scope, and migration contract apply? | ORM preference can distract from dialect and rollout safety | Run real-dialect query, transaction, migration, and duplicate-effect fixtures |
| `kotlin-backend-playbook.md`: Coroutines, Clients, And Workers | Suspend, external calls, queues, or background work change | How do cancellation, blocking, timeout, retry, and durability interact? | Suspend syntax can conceal blocking or fire-and-forget loss | Trace dispatcher or executor, deadline, cancellation, idempotency, and restart behavior |

**Framework regions**

| Source region | Retrieve when | Preserve | Important caveat | Focused target evidence |
|---|---|---|---|---|
| `kotlin-spring-ktor-idioms.md`: Spring package and bean structure | Controllers, services, repositories, scans, or DI change | Slim bootstrap, constructor injection, thin transport, service orchestration | Existing architecture may use deliberate module or bean conventions | Context or slice test proves wiring and dependency ownership |
| Spring compiler plugins | Proxying, AOP, configuration, or JPA entities change | Kotlin Spring/all-open and JPA/no-arg alignment questions | Plugin needs depend on framework use and pinned Kotlin version | Effective build plugins plus proxy, entity, and persistence tests |
| Spring configuration | Structured config or secrets change | Typed configuration and startup validation | Target may have an established binding and secret platform | Missing, malformed, and production-like config startup fixtures |
| Spring MVC, WebFlux, and coroutines | Execution model or suspend endpoints change | Conventional blocking versus genuinely non-blocking distinction | Blocking JPA/JDBC inside event loops can make fake reactive design | Call-path, thread or pool, cancellation, timeout, and load evidence |
| Spring validation and errors | DTO constraints or error contract changes | Transport validation plus domain invariants and centralized mapping | Annotation-only validation does not encode stateful business rules | Invalid JSON, cross-field, domain conflict, and infrastructure failure tests |
| Spring persistence | Transactions, JPA entities, lazy data, or schema change | Service transaction scope and explicit migrations | Data-class equality, generated IDs, proxies, no-arg, and lazy loading require scrutiny | Entity mapping, transaction rollback, query, migration, and serialization fixtures |
| Ktor application structure | Routes, modules, plugins, DI, or global state change | Small bootstrap, deliberate plugins, capability-oriented routes, thin handlers | Plugin installation and order are target-specific | `testApplication` exercises routing, plugins, auth, status pages, and serialization |
| Ktor serialization and errors | Content negotiation, DTOs, or error envelopes change | Intentional unknown keys, defaults, naming, dates, and central error mapping | kotlinx.serialization versus Jackson follows target interoperability | Valid, malformed, unknown-field, date, and stable error-contract fixtures |
| Ktor type-safe routing | Complex route parameters or nesting changes | Typed route identity where it reduces misuse | DSL complexity is unnecessary for a few simple routes | Route generation, parameter parsing, link construction, and failure tests |
| Cross-framework Kotlin idioms | Nullability, data classes, value classes, or sealed outcomes change | Kotlin style and explicit interop checks | Kotlin elegance can conflict with ORM, reflection, serialization, and public API needs | Compile, serialization, persistence, Java interop, and exhaustive mapping evidence |

**Verification regions**

| Source region | Use for | Do not infer | Required pairing |
|---|---|---|---|
| Testing Philosophy | Selecting the lightest proof boundary | Unit tests are sufficient for wiring or real infrastructure | Accepted requirement and actual failure boundary |
| Spring Boot Tests | MVC, JSON, JPA, full wiring, security filters, config, or infrastructure | One slice proves every filter and bean in production | Use `@WebMvcTest`, `@JsonTest`, `@DataJpaTest`, or `@SpringBootTest` according to behavior |
| Ktor Tests | Route and plugin behavior | Internal test host proves external deployment and networking | Add real infrastructure or smoke evidence when acceptance depends on it |
| Coroutine Testing | Dispatcher, delay, timeout, and cancellation | Real sleeps are deterministic or cancellation propagates automatically | Controlled scheduler plus target client and blocking-boundary tests |
| Persistence Tests | Migrations, dialect, transaction, locking, and query behavior | H2 or mocks prove production SQL | Production-dialect container or equivalent target database evidence |
| Contract And API Tests | Status, headers, errors, invalid input, idempotency, and pagination | Schema shape proves business authorization or operational behavior | Target consumer, auth policy, and deterministic ordering checks |
| Property Tests | Parsers, validators, cursors, keys, and state transitions | Generated cases replace readable contract examples | Concrete examples plus generator and invariant review |
| Quality Gates | Repository wrappers and configured static analysis | Missing command has passed or formatter proves architecture | Discover actual scripts and record observed result and limitation |

**Security, resilience, and runtime regions**

| Region | Activate when | Core question | Target evidence |
|---|---|---|---|
| Trust Boundaries And Validation | Any inbound request, message, claim, header, cookie, environment, or provider data changes | Where is transport parsed and where are domain invariants rechecked? | Malformed, boundary, cross-field, stateful, and leak-resistant error fixtures |
| Authentication, Authorization, Sessions, And CSRF | Identity or browser auth behavior changes | Which principal, permission, session, token, cookie, and client-context rules apply? | Allowed, denied, unauthenticated, expired, malformed, enumeration, cookie, and CSRF tests |
| Coroutine Resilience And Blocking | Cancellation, supervisor scope, broad catches, JDBC/JPA/files, or event loops change | Can failure and cancellation propagate without starving runtime resources? | Cancellation injection, timeout, dispatcher or executor, pool, and blocked-thread evidence |
| Retries And Idempotency | Transient failures or repeated writes can occur | Which failures are retryable and how are duplicate effects prevented? | Failure classification, bounded policy, deadline, transaction, deduplication, and response replay tests |
| External Clients And Background Work | Provider or durable asynchronous work changes | Which timeouts, normalized errors, correlation, restart, lag, and dead-letter behavior apply? | Provider matrix, process restart, bounded concurrency, lag, retry, and parking fixtures |
| Build And Dependency Discipline | Versions, plugins, wrappers, or packaging change | Which target versions and build systems remain authoritative? | Wrapper build, effective dependency report, compiler-plugin alignment, and package result |
| Config, Secrets, And Profiles | Environment behavior changes | Which typed settings fail startup and which values must never enter logs? | Missing, malformed, fake-secret, production-like profile, and redaction checks |
| Observability And Health | Production diagnosis or dependency status changes | Which signals distinguish transport, domain, infrastructure, dependency, and worker failure? | Structured log, metric, trace, readiness, liveness, and degraded dependency exercises |
| Migrations And Deployment | Schema, container, rollout, readiness, or shutdown changes | Can old and new versions coexist and recover safely? | Empty and existing schema migration, expand-contract, rolling compatibility, smoke, shutdown, and rollback or roll-forward checks |
| CI Expectations | Gate placement changes | Which fast and integration checks must block which stage? | Actual PR and full pipeline configuration, known-failure run, artifact, and status evidence |

**Progressive retrieval profiles**

- **New Spring endpoint:** map; playbook service and requirements; Spring sections; testing; add persistence, security, or runtime only where behavior changes.
- **New Ktor route:** map; playbook service and requirements; Ktor sections; testing; add coroutine and resilience for external or long-running work.
- **External API or worker:** playbook client, worker, and coroutine regions; security/resilience; runtime operations; testing contracts and failure injection.
- **Persistence or migration:** playbook persistence and transactions; persistence testing; runtime migration and rollout; resilience idempotency where repeated effects exist.
- **Auth or account flow:** framework auth configuration; security trust, sessions, CSRF, and validation; testing negative paths; runtime secrets and observability.
- **Production readiness review:** security/resilience; runtime/ops; testing; playbook; framework sections implicated by findings.
- **Doctrine update:** reference map, all affected destination regions, and research brief; retrieve current external authority only under an authorized mechanism-specific refresh.

**Region traps**

- Constructor injection does not prove that a dependency belongs in the selected layer.
- A suspend controller does not make blocking persistence safe on an event loop.
- Bean Validation does not replace domain and stateful authorization checks.
- A Spring slice does not prove production configuration or every security filter.
- Ktor `testApplication` does not prove container, proxy, or live-network behavior.
- H2 success does not prove production-dialect queries or migrations.
- Retry guidance without idempotency and effect observation can duplicate writes.
- Readiness presence does not prove that the service can handle real traffic.
- Formatter and static analysis success do not prove architecture or behavior.
- A dated official-source summary does not prove current API compatibility.

**Extraction record**

```text
Task outcome, target surface, framework, versions, and owner
Primary mode, activated risk modes, and rejected modes
Source path, complete region, revision, and hash
Question answered, recommendation extracted, and caveat retained
Target code, config, schema, migration, or deploy artifact inspected
Requirement, test type, command, environment, and observed result
Residual uncertainty, route expansion, invalidation, and stop condition
```

Good retrieval combines target evidence, the map, shared service anatomy, one framework lane, and the test or risk regions that change the accepted outcome. Bad retrieval opens every Kotlin file and treats volume as completeness. Borderline snippet reuse is acceptable for orientation when caveats and uninspected companion sections are explicit; it is not implementation-ready until target evidence passes.

Region provenance supports selective invalidation. A framework upgrade reopens its idiom and test regions; a persistence change reopens transaction, migration, dialect, and rollout evidence; a retry change reopens cancellation, idempotency, provider, metrics, and failure injection. Stable project conventions can later compress routes into local shortcuts, but the fallback map remains available when those conventions change.

## External Research Source Map

No browsing occurred. These inherited locations are `external_mapping_unrefreshed_note` records, not current facts, recommendations, or evidence that a target uses the associated versions or mechanisms. The local research brief was dated 2026-06-23; it preserves research lineage but does not refresh itself.

| Inherited location | Possible future role | Permitted use after inspection | Current disposition | Target gate |
|---|---|---|---|---|
| `https://kotlinlang.org/docs/home.html` | Kotlin language, compiler, interop, serialization, and server-side documentation root | Locate direct current pages for a selected language or compiler mechanism | Retain as Kotlin-owned retrieval root; current page and target relevance unverified | Compare direct source with pinned Kotlin and Java targets, compile, and exercise serialization or interop behavior |
| `https://github.com/Kotlin/kotlinx.coroutines` | Coroutine library release, API, implementation, and issue history | Resolve a selected cancellation, context, dispatcher, Flow, test, or compatibility question | Retain as project-owned repository mapping; pinned dependency and current content unverified | Inspect dependency version and direct mechanism, then test cancellation, timeout, error, and blocking interaction |
| `https://github.com/spring-guides/tut-spring-boot-kotlin` | Spring-maintained Kotlin application example | Compare a narrowly similar Spring setup after versions and purpose are known | Retain as example mapping, not architecture or production authority | Match Spring Boot and Kotlin lines and reproduce only the relevant configuration, web, persistence, or test behavior |
| `https://ktor.io/docs/welcome.html` | Ktor server and client documentation root | Locate exact route, plugin, auth, serialization, client, testing, or deployment guidance | Retain as Ktor-owned retrieval root; current sections and target fit unverified | Inspect the pinned Ktor line and exercise target plugin installation, route, error, and test behavior |

These locations cannot choose the target framework, domain model, transaction boundary, database, auth policy, service objective, migration strategy, deployment platform, or acceptable product behavior.

**Authority categories activated by target decisions**

| Decision | Preferred future authority | Local reconciliation required |
|---|---|---|
| Kotlin nullability, platform types, value or data classes, sealed types, compiler plugins, and Java interop | Direct current Kotlin documentation and compiler or library contract | Compile against pinned versions and test reflection, serialization, persistence, and Java boundaries used by the target |
| Coroutine context, structured concurrency, cancellation, timeout, Flow, dispatchers, and tests | Direct current coroutine documentation, pinned library source or release, and framework integration guidance | Exercise request or worker cancellation, broad catches, blocking calls, dispatcher or executor, timeout, and child failure |
| Spring Boot Kotlin support, MVC, WebFlux, configuration, AOP, JPA, security, testing, and Actuator | Direct current Spring project documentation for the pinned line | Run target context, slice, security, persistence, config, health, and production-build tests as applicable |
| Ktor routing, plugins, resources, serialization, auth, status pages, clients, and testing | Direct current Ktor documentation and pinned source or release | Run target `testApplication`, plugin order, auth, serialization, client failure, and deployment smoke behavior |
| Database and query library | Current owner documentation for JPA provider, JDBC/R2DBC driver, Exposed, jOOQ, or other selected stack | Test production dialect, mappings, transactions, concurrency, query plans where material, and compatibility |
| Migration tooling | Current owner documentation for the selected migration tool and platform | Apply from empty and existing schemas, test rolling compatibility, failure, repair, and roll-forward or rollback policy |
| Testing libraries and infrastructure | Current owner documentation for JUnit, Kotest, MockK, Testcontainers, framework test hosts, and target CI | Run the configured repository wrappers and prove fixtures, lifecycle, infrastructure, and failure behavior |
| Security mechanism | Current framework and security authority plus target threat model and policy | Test allowed, unauthenticated, denied, malformed, expired, enumeration, CSRF, secret, and log-redaction paths |
| JVM, container, and runtime platform | Current JDK, image, orchestration, proxy, observability, and deployment authorities | Run production-like startup, readiness, shutdown, traffic, config, resource, smoke, and recovery exercises |
| External provider or broker | Provider contract, SDK, protocol, rate-limit, retry, idempotency, and incident authority | Test success, timeout, malformed response, transient and permanent failure, duplicate effect, cancellation, and reconciliation |

Do not invent direct URLs while mechanism, version, provider, database, test runner, or platform is unknown. Record the authority class and exact question. Add a locator only when retrieval can change an accepted route or target decision.

**Refresh triggers**

Refresh an external contract when Kotlin, Java, Spring, Ktor, a compiler plugin, coroutine library, persistence library, database, migration tool, auth mechanism, test framework, provider client, or deployment platform changes; when a security advisory affects the selected mechanism; when target compilation or behavior contradicts recorded guidance; or when a route depends on an API not covered by local evidence.

Local success can rely on deprecated behavior. Current public documentation can describe a version the target does not run. Preserve both observations and reconcile them rather than forcing agreement.

**Future refresh record**

```text
Frozen task, route, requirement, and affected call or deployment path
Target framework, library, tool, mechanism, and pinned version
Primary source, publisher, status, release or revision, and retrieval date
Relevant section and bounded paraphrased finding
Evidence role: language, framework, coroutine, data, security, test, provider, JVM, or operations
Applicability, conflicts, migration effect, and changed route action
Target fixture, command, environment, expected and observed result
Disposition, residual uncertainty, owner, and invalidation trigger
```

Classify a result as `inspected`, `applicable`, `reproduced`, `reconciled`, `rejected`, `superseded`, or `no_material_impact`. Reading a Spring example does not prove target bean wiring. Reading coroutine documentation does not prove cancellation across a provider client. Passing compilation does not prove a migration or denied auth path.

**Examples**

Good future use starts from a pinned Ktor client cancellation failure, retrieves direct current Ktor and coroutine authority for that mechanism, inspects the target dependency graph, and reruns timeout, cancellation, provider, and stale-response fixtures. The route changes only if the evidence warrants it.

Bad use cites a Spring Kotlin tutorial to migrate a stable Ktor route during unrelated feature work. The publisher may be authoritative for its example while remaining irrelevant to the target framework decision.

Borderline use consults database library documentation for transaction semantics. It becomes applicable only after the target library and driver versions, coroutine or blocking boundary, production dialect, and transaction fixture agree. Documentation alone cannot establish rollout safety.

Good no-browse handling records the exact compatibility question, current target behavior, pinned versions, likely authority, and an owner retrieval request. It narrows guidance instead of filling the gap from memory.

Prefer event-driven retrieval over bibliography growth. Retire an irrelevant mapping while preserving why and what future mechanism would reopen it. External evidence is complete only when the affected target call, framework wiring, data path, or rollout behavior is reproduced and reconciled.

## Anti Pattern Registry Table

Apply an anti-pattern label only after identifying the target outcome, framework, service boundary, source role, verification edge, or lifecycle contract it violates. Similar syntax or package shape is insufficient. Contain unsafe access, secret exposure, data corruption, duplicate effects, and rollout risk before context optimization.

| Anti-pattern | Cause and consequence | Detection signal | Safer response | Valid boundary or exception |
|---|---|---|---|---|
| `keyword_mode_selection` | Modes are selected from words such as coroutine, reactive, security, or migration without changed behavior | Loaded references cannot be tied to accepted requirements | Classify surface and failure consequence, then activate modes | Keyword can start orientation when route remains provisional |
| `full_corpus_context_dump` | Every Kotlin backend file is loaded to appear complete | Context grows while next action and uncertainties remain unchanged | Load map, shared boundary, one framework lane, testing, then activated risks | Comprehensive production review can intentionally read the family |
| `route_without_target_discovery` | Generic doctrine precedes project instructions, build, versions, code, tests, and deployment | Recommendation cannot name target files or configured commands | Inspect target evidence before implementation-ready routing | Conceptual orientation may list required artifacts explicitly |
| `framework_by_preference` | Agent chooses Spring or Ktor from personal or ecosystem preference | Existing framework and migration authority are absent from route | Preserve target framework unless migration is the explicit outcome | A versioned migration plan can compare frameworks deliberately |
| `cross_framework_blending` | Spring annotations, Ktor plugins, MVC, WebFlux, and coroutine assumptions are combined generically | Route recommends mechanisms unavailable in the selected stack | Keep separate framework lanes and reconcile only shared Kotlin concerns | Mixed repositories can route each service independently |
| `feature_as_framework_migration` | A bounded feature becomes package, framework, build, or runtime replacement | Diff and test scope exceed accepted behavior without migration requirement | Deliver feature in current framework or create separate migration decision | Explicit migration owns compatibility and rollout work |
| `service_boundary_by_package_name` | Filenames or package names are treated as architecture truth | Calls, transactions, effects, and ownership contradict inferred layers | Trace real request or job path and map responsibilities | Consistent target package conventions can accelerate discovery after verification |
| `one_model_for_every_boundary` | Transport DTO, domain state, persistence entity, and response are collapsed without invariant review | Framework annotations, nullability, persistence, and public contract leak across layers | Separate shapes where invariants differ and test mappings | Intentional CRUD-only service may keep one shape with named tradeoff |
| `kotlin_idiom_over_framework_reality` | Value classes, data classes, sealed outcomes, or immutability are applied without reflection, ORM, or serializer checks | Compile passes while mapping, proxying, equality, or runtime serialization fails | Route to framework and target compatibility fixtures | Pure domain types without framework crossing can use stronger Kotlin idioms |
| `suspend_equals_nonblocking` | Suspend syntax is treated as proof of non-blocking execution | JDBC, JPA, file, or provider call blocks event loop or shared pool | Trace dependencies; isolate blocking work or choose intentional blocking architecture | Blocking Spring MVC service can remain blocking and scale accordingly |
| `dispatcher_magic` | One dispatcher wrapper is added without pool, transaction, context, or cancellation analysis | Throughput shifts while deadlock, starvation, or transaction behavior remains unknown | Define execution model, pool ownership, deadline, and test | Narrow blocking adapter can use a reviewed dedicated executor |
| `cancellation_as_optional` | Request or worker cancellation is swallowed or never routed | Work continues after caller timeout or shutdown | Activate Coroutine and Resilience; preserve cancellation through children and clients | Deliberately durable work should leave request scope through a real queue |
| `broad_catch_hides_cancellation` | Generic exception handling converts cancellation into ordinary failure | Cancelled work retries, logs as error, or commits effects | Rethrow cancellation and map only intended failures | Framework-specific terminal boundaries may translate cancellation carefully |
| `transaction_in_transport` | Controller or route owns a long transaction and external calls | Connection and locks survive slow I/O; rollback semantics blur | Put transaction around application workflow and separate remote effects | Tiny repository operation can have a clearly scoped transaction |
| `migration_as_schema_file_only` | Migration presence is treated as deployment safety | Old and new application versions are incompatible during rollout | Route through persistence testing and runtime expand-contract evidence | Offline single-version deployment can use a different explicit policy |
| `test_type_by_habit` | Every change uses unit tests or full startup regardless of failing boundary | Tests are slow yet miss wiring, dialect, provider, or migration behavior | Select the lightest test that proves the real boundary | Full startup is correct when acceptance depends on complete wiring |
| `mocked_infrastructure_confidence` | Mocks or H2 are treated as proof of production database, broker, or provider behavior | Production-specific SQL, transaction, protocol, or timeout fails later | Use real disposable infrastructure or contract evidence where behavior differs | Pure application orchestration can use fakes for stable ports |
| `test_after_architecture` | Verification is chosen after abstractions and framework decisions are fixed | Design becomes difficult to observe and negative paths are omitted | Define requirement-to-test matrix before implementation | Existing regression can guide an immediate minimal repair first |
| `auth_happy_path_only` | Authentication success is tested while denial, expiry, malformed input, and authorization are ignored | Protected behavior leaks or errors reveal sensitive distinctions | Route Security plus framework and test negative paths | Public unauthenticated endpoints still need validation and abuse boundaries |
| `validation_annotations_are_domain` | DTO annotations are treated as complete business validation | Cross-field, stateful, and permission invariants are bypassed elsewhere | Parse at edge and recheck domain invariants in application or domain code | Simple shape-only contract can remain at transport boundary |
| `retry_without_effect_identity` | Transient failure triggers repeated writes with no idempotency or status check | Payments, callbacks, messages, or provider operations duplicate | Classify failure and add idempotency, deduplication, outbox, or reconciliation | Read-only idempotent requests can retry under bounded policy |
| `timeout_without_budget` | Each client adds a timeout independently | Nested calls exceed request deadline or retry after useful work is impossible | Define end-to-end deadline and allocate local budgets | Isolated batch work can use a separate documented deadline model |
| `fire_and_forget_request_work` | Critical work launches in request scope without durable ownership | Process restart, cancellation, or exception loses work | Use durable queue, outbox, or owned worker | Best-effort telemetry can be explicitly lossy if privacy and shutdown are handled |
| `operations_after_code` | Config, secrets, health, metrics, migration, shutdown, and rollback are considered at handoff | Implementation passes tests but cannot deploy or diagnose safely | Activate Operations when behavior affects runtime or rollout | Pure library change may not alter service operations |
| `actuator_or_plugin_as_readiness` | Presence of a health endpoint, logging plugin, or metric library is called operational readiness | Signals do not reflect critical dependencies or real traffic capability | Define semantics and exercise degraded dependencies and startup | A narrow liveness probe can intentionally report process health only |
| `generic_command_claimed_pass` | Suggested Gradle, Maven, lint, or test command is reported without target configuration or execution | Verification status is fabricated | Discover wrapper tasks, execute, and record output or absence | Generic commands may remain future gate suggestions when labeled |
| `dated_brief_as_current_fact` | Research summary or familiar URL becomes current API or compatibility evidence | Upgrade or security guidance relies on stale behavior | Retrieve direct authority under authorization and reconcile target | Historical rationale remains valid as provenance |
| `source_count_as_confidence` | Number of files or links substitutes for independence and applicability | Overlapping navigation is treated as corroboration | Record source role, distinct contribution, and target result | Multiple independent target observations can increase bounded confidence |
| `route_never_reassessed` | Initial mode set survives failing evidence and scope changes | New persistence, security, or rollout risk remains outside context | Reassess after first evidence and every lifecycle transition | Stable focused work can retain its route when no boundary changes |
| `route_expansion_without_split` | One route accumulates unrelated outcomes and owners | Context, implementation, and verification become inseparable | Split independently acceptable changes and preserve interfaces | Broad hardening review can remain one coordinated assessment artifact |

**Repair order**

1. Stop unsafe access, secret leakage, corrupting migration, duplicate effect, and unowned production change.
2. Freeze target framework, versions, failing input, environment, command, and observed result.
3. Prevent wrong-framework or unsupported guidance from driving additional implementation.
4. Restate the accepted outcome and changed service boundary.
5. Repair mode selection and progressive source order.
6. Reconcile service, framework, test, data, coroutine, security, resilience, and runtime decisions activated by the failure.
7. Execute focused regression and broader affected gates.
8. Record invalidated route artifacts, remaining uncertainty, and reassessment trigger.

**Controlled probes**

- Remove the word coroutine from a request while keeping cancellation behavior; confirm the route still selects Coroutine mode.
- Present a Spring repository and a Ktor example; confirm framework preservation defeats example preference.
- Insert a blocking repository under a suspend handler and verify execution-model review activates.
- Make a write retry after an unknown provider response and confirm idempotency or reconciliation blocks blind repetition.
- Change a schema during rolling deployment and confirm migration plus runtime routing activates before rollout.
- Pass a controller slice while breaking production configuration and confirm full wiring or startup evidence is requested.
- Deny authorization after successful authentication and confirm the route includes negative security behavior.
- Remove a configured lint task and confirm the reference reports absence rather than success.
- Add a new external effect after the first route and confirm reassessment expands or splits the work.
- Load every source and confirm the route removes files that add no distinct decision or gate.

Good routing fails visibly when framework, service boundary, evidence, or lifecycle claims exceed target support. Bad routing can be locally sourced and neatly structured while selecting the wrong architecture. Cascades matter: a vague outcome can trigger keyword modes, wrong framework detail, shallow tests, hidden effects, and false rollout confidence. Repair the earliest supported cause and invalidate dependent plans and evidence.

## Verification Gate Command Set

Run the focused assignment verifier from the repository root after changing this reference and packet:

```bash
python3 tests/verify_idiomatic_reference_file.py --path idiomatic-ref-202607/kotlin_backend_reference_routing-20260710.md
```

Then run the archived shared-generation contract:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

These commands verify reference artifacts. They do not compile Kotlin, start Spring or Ktor, execute a route, connect a database, inject cancellation, test authorization, apply a migration, or prove deployment safety.

Discover the target before binding commands:

```bash
rg --files | rg '(^|/)(gradlew|mvnw|build.gradle.kts|build.gradle|pom.xml|settings.gradle.kts|libs.versions.toml|src|test|integrationTest|db/migration|application.*\.(yml|yaml|properties)|Dockerfile|compose.*\.ya?ml|workflows)(/|$|\.)'
```

Inspect project instructions, wrapper tasks, dependency versions, source sets, framework bootstrapping, compiler plugins, database and migration tool, test fixtures, CI, deployment, and target consumer. Filename discovery is not behavioral evidence.

Conditional target commands can include the repository's configured forms of:

```bash
./gradlew test
./gradlew build
./gradlew detekt
./gradlew ktlintCheck
./mvnw test
./mvnw verify
```

Do not report any of these as passed unless the wrapper and task exist and the command was executed. If absent, record that fact and discover the repository's actual gate.

| Route claim | Required target gate | Passing observation | Important limit |
|---|---|---|---|
| Framework and versions are preserved | Inspect effective build, plugins, dependency management, source bootstrapping, and runtime packaging | Route names actual Spring or Ktor line, Kotlin and Java targets, wrappers, plugins, and no unrequested migration | Build metadata does not prove runtime behavior |
| Requirement is observable | Trace requirement ID or accepted behavior to tests and implementation boundary | Valid, invalid, failure, and recovery outcomes have expected results | Traceability can encode the wrong product decision |
| Service boundary fits | Trace controller or route through service, domain, persistence, integration, and runtime effects | Ownership, transaction, blocking, trust, and effect boundaries are explicit or intentionally collapsed | Static structure cannot prove all runtime calls |
| Spring web contract works | Use the configured focused MVC, JSON, JPA, security, or full-context test according to behavior | Request, response, validation, error, filter, wiring, or persistence behavior matches the requirement | A slice omits unrelated production wiring by design |
| Ktor route contract works | Use target `testApplication` or configured host fixture | Installed plugins, auth, parsing, status mapping, serialization, and route behavior match expectation | Internal test host does not prove proxy, container, or live network behavior |
| Kotlin boundary type is compatible | Compile and run JSON, database, reflection, and Java interop fixtures activated by the type | Nullability, value class, data class, sealed outcome, and mapper behavior remain exact | One framework version does not establish universal compatibility |
| Coroutine behavior is safe | Control dispatcher or scheduler, delay, timeout, cancellation, child failure, and blocking dependency | Cancellation propagates, obsolete work stops, errors map correctly, and blocking work uses the intended execution model | Synthetic scheduling may omit provider or production pool behavior |
| Persistence behavior is correct | Run repository tests with production dialect or equivalent real database | Query, mapping, transaction, rollback, locking, ordering, and constraints match expected behavior | Container success does not prove production capacity or rollout |
| Migration is deployable | Apply migrations from empty and supported prior states and test old/new application compatibility | Schema reaches expected version; failure and expand-contract behavior are explicit | Local migration does not prove platform rollback policy |
| Authentication and authorization are correct | Exercise allowed, unauthenticated, denied, malformed, expired, and scope or role paths | Stable public contract prevents unauthorized behavior and sensitive leakage | Passing auth tests do not prove broader threat resistance |
| Retry and idempotency are coherent | Inject transient, permanent, unknown-effect, timeout, and duplicate requests | Only classified failures retry within deadline and duplicate writes replay or deduplicate safely | Test provider may not reproduce all real failure ordering |
| External client contract is bounded | Exercise success, 4xx, 5xx, timeout, malformed response, cancellation, and correlation | Adapter normalizes failures, preserves deadlines, redacts secrets, and supports route requirements | Mock server does not prove live provider availability or policy |
| Worker is durable and bounded | Restart process or worker fixture, inject duplicate and poison messages, vary concurrency | Required work survives, deduplicates, parks or dead-letters, and emits useful outcomes | Local queue may differ from production broker semantics |
| Configuration fails safely | Start with valid, missing, malformed, and production-like settings | Typed config validates early, secrets stay out of output, and environment differences remain declarative | Startup success does not prove live credentials or dependencies |
| Observability and health are truthful | Trigger domain, transport, infrastructure, dependency, and worker failures | Logs, metrics, traces, readiness, and liveness distinguish the conditions without sensitive data | Signal presence does not prove alerting or operator response |
| Deployment can recover | Build production artifact and exercise startup, readiness, smoke, graceful shutdown, migration window, and recovery | Service handles traffic only when ready and follows accepted rollback or roll-forward path | Staging evidence is scoped to that environment and load |

**Verification profiles**

- **Focused pure behavior:** compile, unit tests, static checks configured by the target, and direct requirement traceability.
- **Spring endpoint:** focused slice for transport behavior; full context only when filters, configuration, or wiring are part of acceptance; add database or provider infrastructure when behavior depends on it.
- **Ktor route:** `testApplication` for route and plugins; add real persistence, provider, container, or smoke evidence when acceptance crosses those boundaries.
- **Persistence or migration:** production-dialect database, transaction and query fixtures, migration from supported states, rolling compatibility, and runtime recovery.
- **External workflow or worker:** coroutine control, provider or broker contract, cancellation, timeout, retry, idempotency, restart, metrics, and bounded concurrency.
- **Auth or account flow:** framework security wiring, allowed and denied matrices, validation, anti-enumeration, token or session handling, secrets, and operational abuse signals.
- **Production hardening:** build, static analysis, framework and integration tests, migrations, config, security, resilience, observability, health, container, deployment, smoke, and recovery evidence selected from actual target scope.

**Evidence protocol**

1. Record exact repository revision, wrappers, effective dependencies, environment, fixture, and relevant configuration.
2. Run the narrowest gate expected to fail before repair when practical.
3. Confirm failure is caused by the targeted route or implementation boundary, not a broken fixture.
4. Apply the smallest decision-complete correction.
5. Rerun the focused gate, then affected wiring, infrastructure, migration, security, or rollout gates.
6. Record command, result, limitation, skipped gates, and owner decisions.
7. Reassess the route when evidence identifies a missing mode or shows a loaded source is irrelevant.

Good evidence binds one requirement to target code, a focused negative-path test, configured wrapper output, and the broader boundary needed for handoff. Bad evidence says `./gradlew build` without confirming the task exists or what it exercised. Borderline evidence has a passing Spring slice but no production-dialect or migration result for a data change; it supports transport behavior only.

Stop implementation when the target framework or versions are unknown, requirements are not observable, blocking and cancellation are unresolved, a write can duplicate, denied paths are missing, migration compatibility is unknown, or the release path lacks an owner. Repair the earliest contract and rerun affected evidence plus core framework and security invariants.

## Agent Usage Decision Guide

Use this reference when the agent must decide which Kotlin/JVM backend sources, modes, target artifacts, and gates should drive delivery or review. Do not trigger from the word Kotlin alone.

| Usage profile | Choose when | Minimum route | Completion boundary |
|---|---|---|---|
| New Spring endpoint | MVC, WebFlux, controller, service, Spring Data, config, or Spring Security behavior changes | Spec, Playbook, Spring idioms, Testing; add changed risk modes | Observable contract passes appropriate slice or wiring test and affected data, trust, and runtime gates |
| New Ktor route | Route, plugin, content negotiation, status page, auth, resources, or Ktor client changes | Spec, Playbook, Ktor idioms, Testing; add Coroutine or Resilience as needed | Route and plugin behavior pass `testApplication` or broader target gate required by acceptance |
| Domain or service refactor | Kotlin types, error model, application service, transaction choreography, or boundary ownership changes | Playbook, framework interop region, Testing | Mappings, behavior, public contract, and affected wiring remain exact |
| Persistence or query work | JPA, JDBC, Exposed, jOOQ, transaction, query, lock, or schema changes | Persistence, Testing, Runtime migration; Resilience for repeated effects | Production-dialect, transaction, migration, compatibility, and rollout evidence meet accepted scope |
| Coroutine or Flow work | Suspend, Flow, dispatcher, cancellation, timeout, child failure, or blocking isolation changes | Playbook coroutine, Security/Resilience, Testing | Cancellation, timeout, failure, and blocking behavior are observed at the target call path |
| Auth or account flow | Auth, authorization, session, token, CSRF, password, reset, validation, or enumeration changes | Spec, framework, Security, Testing, Runtime secrets or signals | Allowed and negative paths, secret handling, stable errors, and owner policy agree |
| External API flow | Provider client, timeout, retry, idempotency, callback, or unknown effect changes | Playbook integration, Coroutine, Resilience, Testing, Operations | Provider matrix, deadline, duplicate-effect, cancellation, and observability evidence pass |
| Queue or worker | Consumer, scheduler, durable job, concurrency, retry, dead-letter, or restart behavior changes | Playbook workers, Coroutine, Resilience, Runtime, Testing | Idempotency, restart, bounded concurrency, retry classification, parking, lag, and shutdown are verified |
| Migration or deployment | Build, config, secret, schema rollout, container, health, CI, startup, shutdown, or rollback changes | Persistence and Runtime/Operations, Testing, Security where trust changes | Production-like migration, config, health, smoke, shutdown, and recovery evidence exist |
| Production readiness review | Scope includes architecture drift, security, resilience, data, test, and operations | Security/Resilience, Runtime/Operations, Testing, Playbook, then implicated framework regions | Findings are prioritized by consequence and each recommendation has target evidence or an explicit blocker |
| Doctrine or router update | Local mode, order, recommendation, or source role changes | Map, affected destinations, entrypoint, research brief, verifier | Source identity, conflicts, affected routes, packet rationale, and focused conformance pass |
| Orientation only | Target access is incomplete or user wants route options | Map, source roles, likely profiles, required target artifacts | Output remains provisional and makes no target command, API, or production claim |
| Avoid as primary | Android UI, multiplatform client, generic syntax tutoring, non-Kotlin service, or product/legal policy is primary | Route to the owning domain; retain only a bounded backend contract if needed | Primary owner returns accepted constraint or evidence before backend delivery proceeds |

**Preflight before selecting sources**

Record:

- user, accepted outcome, valid and invalid behavior, failure consequence, and owner;
- backend surface and whether work is feature, repair, migration, hardening, or orientation;
- project instructions and current repository state;
- framework, build wrapper, Kotlin and Java targets, dependency management, compiler plugins, database, and deployment model;
- transport, application, domain, persistence, integration, worker, and runtime boundaries affected;
- inbound trust, identity, authorization, sensitive data, and public error concerns;
- blocking calls, suspend and Flow boundaries, dispatcher or pool, deadline, cancellation, and child lifetime;
- transaction, migration, consistency, external effect, retry, idempotency, and recovery semantics;
- configured unit, framework, integration, contract, migration, property, static, build, smoke, and operational gates;
- config, secrets, observability, health, CI, container, rollout, shutdown, and recovery changes;
- current external authority needed, if any, and whether retrieval is permitted;
- primary mode, companions, rejected modes, first evidence, stop condition, and reassessment trigger.

A reduced preflight fits a small local fix: confirm outcome, existing framework and versions, changed call path, relevant source section, focused regression, repository wrapper, and why data, security, coroutine, and runtime boundaries are unchanged.

**Start blockers**

Keep work in orientation, split it, or escalate when:

- accepted backend behavior or owner cannot be named;
- target framework, versions, wrapper, or source path is unknown;
- the request implies framework migration without accepting migration scope;
- business, authorization, privacy, or operational policy is unresolved;
- a write can repeat but effect identity and idempotency are unknown;
- a suspend path includes unknown blocking dependencies or cancellation behavior;
- storage changes have no target schema, dialect, migration tool, or rollout model;
- the proposed test cannot exercise the dependency that determines behavior;
- production-ready, secure, resilient, non-blocking, or fast has no observable criterion;
- public compatibility is required but current authority cannot be retrieved;
- one route combines outcomes that cannot be accepted or rolled back together.

An orientation route can proceed without implementation. It should return likely modes, required target artifacts, uncertainties, and the first observation that would select or reject the route.

**Route transitions**

Re-run usage selection when:

- an endpoint gains persistence or external effects;
- authentication becomes authorization-sensitive;
- blocking storage enters a coroutine or reactive path;
- a local callback becomes a retryable provider write;
- in-request work becomes durable background work;
- a schema change enters rolling deployment;
- target versions or framework change;
- a test failure exposes missing wiring or real infrastructure;
- config, secrets, metrics, health, or shutdown behavior changes;
- a local feature becomes shared, high-traffic, regulated, or production-critical.

Good use selects the Spring endpoint profile, confirms existing Spring MVC and JPA, adds persistence and migration only because the write changes data, and maps each requirement to focused plus real-database evidence. Bad use opens the entire corpus and recommends Ktor because coroutine-first design sounds cleaner. Borderline use identifies an external workflow profile without repository access; it may list target questions but cannot invent provider, timeout, command, or idempotency details.

**Usage evidence record**

```text
Accepted outcome, user, consequence, and owner
Backend surface, current framework, build, versions, and deployment stance
Target call path and changed service boundaries
Primary profile, companion modes, and rejected profiles
Ordered local sources and exact regions
Target code, config, schema, migration, test, and platform artifacts
Requirement and first expected failing or passing observation
Commands executed, results, limitations, and unavailable gates
Companion owners, return artifacts, route changes, and stop condition
```

Correct usage minimizes duplicated decisions. Product and domain owners return accepted semantics; security owners return policy and abuse criteria; data owners return schema and rollout contracts; platform owners return runtime and recovery constraints. This router connects those artifacts to implementation references without pretending to own their authority.

## User Journey Scenario

Use this hypothetical journey to hold one outcome constant: an existing Ktor service needs a read-only route that obtains a price from an external provider and returns the service's stable response or error contract. The router must select enough evidence for framework wiring, serialization, deadline, cancellation, provider failure, testing, config, and observability without inventing persistence, retries, or a framework migration.

**Starting state**

- The target repository, not this example, determines Ktor, Kotlin, Java, build, serialization, client, auth, config, logging, and deployment versions.
- An existing application service or provider port may already own outbound calls; inspect before adding another abstraction or dependency.
- The request is read-only. No database, cache, queue, or idempotency record is assumed.
- Product and platform owners must define acceptable price freshness, provider failure mapping, total deadline, and degraded behavior.
- Public provider documentation and current Ktor behavior remain unverified until target-specific retrieval is authorized and reconciled.

| Phase | Action | Route and evidence retained | Stop, add, split, or escalate condition |
|---|---|---|---|
| Intake | Restate user-visible success, invalid input, provider failure, cancellation, and recovery | Accepted outcome, owner, public contract, and non-goals | Stop when fallback, freshness, or public error semantics lack ownership |
| Target discovery | Inspect instructions, wrapper, build, pinned Ktor and Kotlin, module, routes, plugins, client, config, tests, deployment, and existing error envelope | Exact paths, effective versions, service call path, and available gates | Keep orientation-only when target artifacts are unavailable |
| Surface classification | Identify Ktor route plus outbound client under request scope | Primary Ktor mode; no framework migration | Route elsewhere if target is Spring or a non-Kotlin service |
| Risk classification | Identify suspend execution, external failure, timeout, cancellation, config, secret, and telemetry edges | Coroutine, Resilience, Testing, and Operations companions | Add Security only if identity, authorization, secret, or abuse behavior changes beyond existing boundary |
| Source order | Read map; playbook service, coroutine, and client regions; Ktor idioms; security/resilience client and cancellation regions; testing; runtime config and observability | Region disposition and question answered by each | Remove any source that changes no decision or gate |
| Requirements | Define valid request, invalid parameter, provider success, provider client error, provider timeout, malformed provider response, caller cancellation, and output mapping | Observable contracts with target-specific status and envelope left to owner | Do not substitute illustrative HTTP codes for target conventions |
| Service design | Keep route thin; call application service or existing port; normalize provider errors in adapter; pass deadline and cancellation | Call graph, ownership, effect classification, and rejected alternatives | Split if target inspection discovers durable writes, cache semantics, queueing, or background refresh |
| Execution model | Identify whether provider client is suspend/non-blocking or blocking and how it uses event-loop or worker resources | Client implementation, dispatcher or executor, pool, deadline, and child scope | Stop fake non-blocking claims when dependency behavior is unknown |
| Retry decision | Classify the read request, provider failures, caller deadline, cost, and rate limits | Explicit no-retry or bounded retry policy plus reason | Escalate unknown provider effect, policy, or deadline; never add retry by habit |
| Framework wiring | Confirm content negotiation, route parsing, auth boundary if unchanged, status pages, DI, and client lifecycle | Ktor module and plugin evidence | Add Security mode if authorization behavior changes or principal is used in pricing |
| Focused tests | Use configured Ktor test host and a controllable provider adapter | Valid, invalid, timeout, malformed, cancellation, and error-mapping fixtures | Add real provider contract evidence if mock behavior is insufficient |
| Runtime evidence | Bind timeout and endpoint config, redact credentials, emit bounded provider and outcome signals, preserve readiness semantics | Config keys, startup validation, logs or metrics, and owner | Add deployment scope when container, proxy, health, or rollout changes |
| Handoff | Record route, files, requirements, decisions, tests run, results, limitations, and refresh triggers | Reviewable routing packet and exact target evidence | No production-safe claim without the required runtime and owner acceptance |

**Mode decision**

The primary route is Ktor because the target already uses Ktor and the change is a route. Coroutine mode activates because request-scoped suspend work and cancellation are part of correctness. Resilience activates because an external provider can timeout, fail, or return malformed data. Testing activates to prove route, plugin, provider, and cancellation behavior. Operations activates only for timeout config, secret handling, metrics, health, or deployment behavior that actually changes.

Persistence is omitted while the route remains read-only and stores nothing. Security can remain a verified unchanged companion if existing auth is merely inherited; it becomes active when principal data changes authorization, provider credentials change, or public abuse controls are part of acceptance. These omissions are route decisions, not assumptions that the risks do not exist.

**Illustrative route record**

```yaml
task: Add a read-only Ktor pricing route backed by an external provider.
status: planning-target-evidence-required
target:
  framework: existing-ktor-service
  build: repository-wrapper
  versions: inspect-effective-build
primary_mode: ktor
companion_modes:
  - spec
  - coroutine
  - resilience
  - testing
  - operations-if-config-or-signals-change
omitted_modes:
  persistence: No durable state is accepted in this scenario.
  migration: No schema or deployment compatibility change is accepted.
required_artifacts:
  - Existing route and module wiring.
  - Provider client or port.
  - Stable response and error envelope.
  - Timeout and credential configuration.
  - Ktor test-host and provider fixtures.
first_negative_case: Provider call exceeds the accepted request deadline.
stop_condition: Target owner accepts behavior and required target gates pass.
reopen_when:
  - Provider contract, client library, Ktor version, auth policy, or deployment boundary changes.
  - Durable cache, persistence, queue, retrying write, or background refresh is added.
```

All values are illustrative routing state, not target findings.

**Verification matrix**

| Behavior | Best initial evidence | Required observation | Expansion trigger |
|---|---|---|---|
| Valid request and provider success | Ktor target test host with controlled provider success | Route parses input, calls current service boundary, and emits exact target response | Add live contract when provider schema or SDK behavior is material |
| Invalid route or query value | Ktor route fixture | Stable target validation response and no provider call | Add domain validation when validity depends on business state |
| Provider timeout | Controlled provider delay and request deadline | Target timeout mapping occurs within total budget and work terminates | Add operational load or provider evidence when scheduler and network matter |
| Caller cancellation | Cancel test request or application scope | Child provider work and resources stop unless deliberately durable | Add worker route if accepted behavior must outlive the request |
| Provider client error | Controlled 4xx, 5xx, connection, and malformed response | Adapter normalizes failure without leaking provider internals or secrets | Add policy owner when fallback or retry differs by error |
| Stale completion | Delay provider result and terminate or supersede request | Old work cannot mutate unrelated shared state or emit a late response | Add cache or concurrency evidence if state becomes shared |
| Missing config | Production-like startup fixture | Required timeout or credential binding fails early and safely | Add deployment test when secret injection is platform-owned |
| Observability | Trigger success, timeout, cancellation, and provider failure | Bounded signals distinguish outcomes without raw credentials or private payload | Add alert and runbook evidence only when operational acceptance includes them |

**Route branches**

- If the provider SDK blocks, choose intentional blocking architecture or isolate it with a target-owned executor and capacity evidence; suspend syntax alone is not a fix.
- If a cache is added, define freshness, key identity, invalidation, concurrency, and failure semantics, then activate Persistence or Runtime guidance according to storage.
- If quote refresh becomes asynchronous and must survive restart, split a durable worker outcome and activate worker, idempotency, broker, operations, and restart evidence.
- If the provider operation becomes a write or has unknown effect status, classify retries and add effect identity or reconciliation before repetition.
- If auth claims change pricing eligibility, activate Security and test allowed, denied, malformed, expired, and sensitive-output paths.
- If Ktor or the provider library is upgraded, retrieve current direct authority and rerun compatibility and target behavior.

**Good outcome:** the route preserves Ktor, every source answers a distinct question, request cancellation reaches provider work, target errors remain stable, config fails safely, and executed target fixtures support only the claims reported.

**Bad outcome:** the agent recommends Spring WebClient in a Ktor service, adds a generic retry, wraps a blocking SDK in suspend code, and reports `./gradlew test` as passed without target execution.

**Borderline outcome:** a cached price is proposed during provider outage. It remains a product and data decision until freshness, privacy, invalidation, storage, and fallback ownership are accepted. The router can name the required modes but cannot authorize the policy.

The durable handoff contains the accepted behavior, target framework and versions, route and client boundaries, mode set, source regions, rejected modes, requirements, executed results, owner decisions, unresolved provider evidence, and invalidation events. Its product is a replayable route from request to proof, not a generic list of Kotlin practices.

## Decision Tradeoff Guide

Hold one accepted backend outcome and target revision constant while comparing routes. Add context or process only when it protects a compatibility, behavior, trust, data, proof, or rollout boundary that a narrower route cannot preserve.

| Decision | Lightweight default | Choose the stronger alternative when | Cost if misapplied | Verification and reversal signal |
|---|---|---|---|---|
| Target trace or source map first | Begin with target instructions, build, framework, and changed call path when repository access exists | Begin with the map for orientation, ambiguous surface, or doctrine update | Target-first can inherit local mistakes; map-first can produce generic advice | Compare route after target inspection and retain only sources that alter a decision or gate |
| One primary mode or broad mode set | Select one outcome and only changed risk modes | Use broad review modes when acceptance explicitly spans architecture, security, data, tests, and operations | Narrow route omits risk; broad route hides priority and consumes context | Map every mode to a changed behavior, owner, and expected observation |
| Preserve framework or plan migration | Preserve Spring or Ktor and pinned versions for feature delivery | Consider migration only when it is the accepted outcome with compatibility and rollout ownership | Preservation can retain debt; migration creates large unaccepted scope | Separate feature and migration requirements and prove independent value and transition safety |
| Shared playbook or framework region first | Read playbook first when service ownership, transaction, or integration shape is unclear | Read framework region first for a reproduced Ktor or Spring wiring defect | Shared advice can stay abstract; framework syntax can harden wrong boundaries | Trace target call path and identify earliest unresolved contract |
| Complete relevant section or extracted checklist | Read complete source region by default | Use a bounded extraction for repeated stable project workflow | Full section costs context; extraction can lose caveats and invalidation | Compare extraction with source hash, scope, companion risks, and target result |
| Narrow local route or current external refresh | Use frozen local doctrine plus target evidence for settled mechanisms | Retrieve current primary authority for upgrades, security, compatibility, or disputed API behavior | Local source may be stale; retrieval can be irrelevant or wrong-version | Record mechanism, pinned version, direct source, changed action, and reproduced result |
| Focused test or full application wiring | Use the lightest test that proves the changed boundary | Use full context when filters, config, dependency wiring, or cross-layer behavior is acceptance | Focused test omits wiring; full test is slow and may localize poorly | Break the relevant wiring and confirm the selected gate detects it |
| Fake or real infrastructure | Use fakes for stable application ports and pure orchestration | Use real database, broker, provider contract, or container when behavior depends on it | Fakes create false confidence; real infra adds cost and flakiness | Identify one behavior that differs and run a controlled target fixture |
| Blocking or coroutine execution | Keep established intentional blocking model when dependencies are blocking | Use coroutine/non-blocking path when the stack and workload justify it | Blocking may limit capacity; fake non-blocking starves event loops | Trace calls, pools, dispatcher or executor, cancellation, and load profile |
| Local validation or domain and state validation | Use transport validation for shape and simple constraints | Add application or domain validation for cross-field, stateful, authorization, or business invariants | Duplication can drift; annotation-only checks are bypassed elsewhere | Exercise alternative entry paths and state changes against one invariant |
| No retry or bounded retry | Do not retry by default | Retry classified transient operations within deadline and effect-safety contract | No retry reduces resilience; blind retry duplicates effects and load | Inject transient, permanent, timeout, unknown-effect, and duplicate attempts |
| In-request work or durable worker | Keep work in request scope when completion and cancellation follow the caller | Use queue or durable worker when work must survive restart or outlive request | Request work can be lost; durable work adds concurrency and operations | Cancel request and restart process; observe accepted durability behavior |
| No persistence mode or persistence route | Omit data guidance when state and schema do not change | Add it for queries, writes, transaction, migration, locking, or durable idempotency | Omission hides data risk; inclusion can invent unnecessary storage | Trace actual writes and schema and run production-dialect or migration evidence |
| No operations expansion or runtime route | Omit when config, deploy, health, signals, and recovery are unchanged | Add when behavior changes startup, secret, dependency, migration, traffic, shutdown, or diagnosis | Omission blocks safe rollout; inclusion creates process noise | Name changed runtime contract and execute a production-like gate |
| One route or split outcomes | Keep one route when changes share owner, rollback, and acceptance | Split when framework, schema, security, provider, or deployment changes can be accepted independently | One route entangles work; splitting can duplicate state and coordination | Verify each slice has complete requirements, interfaces, gates, and rollback boundary |
| Static route or reassessed route | Retain route while target facts and behavior remain stable | Reassess after failure, version change, new effect, owner change, or lifecycle transition | Constant rerouting creates churn; static routing misses risk | Record trigger and show which source, mode, or gate changes |
| Orientation or implementation-ready output | Stay orientation-only when target evidence is incomplete | Promote after target framework, path, requirements, gates, and owners are known | Orientation can be mistaken for action; full plan can fabricate details | Check every concrete target claim has a locator or observed result |
| Project-local shortcut or generic router | Use a proven local route for recurring service patterns | Fall back to generic route when conventions, versions, or boundaries change | Shortcut becomes stale; generic route repeats settled discovery | Version the shortcut and retain invalidation plus expansion path |

**Adopt, adapt, avoid, or escalate**

- **Adopt** a local routing pattern when target obligations match and focused evidence demonstrates a useful next action.
- **Adapt** source order or mode composition when repository architecture, framework, versions, tests, and operations differ.
- **Avoid** references that add no distinct decision, risk, gate, owner, or recovery path.
- **Escalate** product semantics, framework migration, threat model, data policy, provider contract, service objective, and production rollout to accountable owners.

**Worked choices**

Good narrow route: a pure domain parser change in a Spring service reads target instructions, playbook type guidance, and testing. It preserves framework and excludes persistence, coroutine, security, and operations because the call path and accepted behavior do not change there. Unit and property examples prove the parser contract.

Bad broad route: the same parser change loads every framework and operations reference, recommends Ktor and Testcontainers, and adds telemetry. Context and implementation grow without protecting the parser outcome.

Borderline migration choice: a Spring service has recurring framework pain and Ktor is proposed. Keep feature delivery in Spring while a separate migration route measures compatibility, security, data, operations, team ownership, and rollout. Do not let the migration hide inside one endpoint.

**Decision ledger**

```text
Accepted backend outcome and target revision held constant
Mandatory project, policy, and platform constraints
Selected routing option and boundary protected
Narrower or current route rejected because
Source, target, requirement, test, and owner evidence
Compatibility, data, security, runtime, and rollout effects
Known untested dependency or environment
Route owner, invalidation event, and reversal condition
```

This guide does not establish current framework APIs, target commands, provider contracts, database behavior, or service objectives. Uncertainty should keep routes narrow, reversible, and explicit. A broader mechanism earns its place only when it protects an accepted boundary that the simpler route demonstrably cannot.

## Local Corpus Hierarchy

Classify authority per claim and source region, not once per file. A source can be canonical for the historical read order, supporting for a design rationale, conditional for a framework mechanism, and silent about the target service. Calling the whole file canonical would erase those distinctions and allow a strong navigation artifact to masquerade as current implementation or production evidence.

The frozen corpus is evidence of what the June 2026 skill contained. It is not automatically current team policy, current public documentation, or proof that a mechanism works in the target repository. The target's accepted requirements, governing project instructions, effective build, observed call path, executed tests, and accountable owner decisions determine applicability. Current direct authority is needed when a version-sensitive or security-sensitive mechanism cannot be resolved locally; this reference did not browse and does not refresh those public claims.

**Claim-level role vocabulary**

| Role | What the role authorizes | What the role does not authorize | Promotion or retention evidence |
|---|---|---|---|
| routing entrypoint | Which question or mode to inspect next | Framework syntax, target architecture, or successful behavior | Stable map relationship plus a target question the destination can answer |
| shared design candidate | Service, type, transaction, integration, or coroutine considerations independent of one framework | Automatic adoption in Spring, Ktor, or a target domain | Target call-path fit and a requirement or test changed by the guidance |
| framework candidate | Spring- or Ktor-specific wiring and lifecycle questions | Current API compatibility or permission to migrate frameworks | Effective target version, existing convention, and focused target execution |
| verification candidate | Test shape, fixture boundary, and negative-path questions | Proof that a named command, container, or fixture exists or passed | Discovered target gate, controlled failure, and observed result |
| risk candidate | Security, resilience, retry, cancellation, and abuse questions | A universal threat model, retry policy, or provider contract | Accepted risk boundary, owner, negative cases, and recovery observation |
| runtime candidate | Config, observability, health, deployment, and shutdown questions | A service objective, platform topology, alert policy, or production result | Target runtime contract, production-like gate, and operations ownership |
| provenance evidence | What a frozen source said and how local sources related | Present correctness, target adoption, or public-source freshness | Frozen path, bounded region, content hash, and accurate paraphrase |
| target authority | What the current repository, policy, and accepted behavior require | Facts outside the inspected revision and environment | Exact locator, revision, effective configuration, executed gate, and owner scope |
| conditional claim | A plausible choice with a named missing observation | Implementation-ready guidance or a success claim | Resolve the named version, behavior, policy, or environment uncertainty |
| rejected claim | Why a source mechanism does not apply to this outcome | Permanent invalidity in every Kotlin backend | Reopen only on the recorded target or requirement change |
| promoted project shortcut | A recurring local route that may replace repeated generic discovery | Applicability beyond its versioned scope or invalidation boundary | Owner, consumers, version, enforcement, regression gate, fallback, and review date |
| legacy or superseded evidence | Historical rationale and migration context | Preferred new implementation | Explicit successor, compatibility boundary, and retention reason |
| conflicting evidence | A disagreement that must be resolved before consequential use | Permission to choose the newest, most polished, or broadest statement | Compare authority, versions, target fit, behavior, owners, and cost of error |

`Canonical` is therefore a qualified statement such as "canonical routing entrypoint for the frozen corpus," not an unbounded badge. `Supporting` names a contribution to a specific decision. `Duplicate` applies only when two claims have the same scope, authority, consequence, and verification; similar wording alone is insufficient. Two sources that recommend the same mechanism for different frameworks or failure modes are complementary, not duplicates.

**Corpus responsibility map**

| Frozen local source | Strongest historical responsibility | Conditional regions or limitations | Target question before use |
|---|---|---|---|
| `reference-map.md` | Entry mode, destination file, and common read-order navigation | Does not prove target framework, feature boundary, source freshness, or implementation outcome | Which target decision or risk requires the proposed destination? |
| `SKILL.md` | Top-level workflow, mode selection, framework preservation, output expectations, and reference index | Broad workflow can overroute a narrow task; named commands and versions require discovery | Which accepted outcome and target evidence activate each selected mode? |
| `kotlin-backend-playbook.md` | Shared service boundaries, Kotlin type choices, transactions, persistence, coroutines, clients, security, resilience, delivery, and review questions | Examples span concerns not present in every route and cannot establish target conventions | Which shared boundary changes, and which focused gate observes it? |
| `kotlin-spring-ktor-idioms.md` | Separate Spring and Ktor wiring, validation, error, dependency, and lifecycle questions | Framework branches are alternatives; APIs and versions are not refreshed here | Which framework and effective version does the target already use? |
| `kotlin-backend-testing-and-fixtures.md` | Test levels, framework fixtures, database and broker evidence, property checks, and verification discipline | A fixture name is not evidence that its dependency or infrastructure exists | What behavior differs between a fake and the production-like boundary? |
| `kotlin-backend-security-and-resilience.md` | Authorization, input and output trust, secrets, timeouts, retry, idempotency, abuse, cancellation, and dependency failure | Does not supply the target threat model, provider semantics, or recovery owner | Which trust or failure boundary changed, and what is denied or recovered? |
| `kotlin-backend-runtime-and-ops.md` | Configuration, telemetry, health, deployment, migration, shutdown, and operational review questions | Illustrative signals and commands do not establish platform policy or service objectives | Which runtime contract changes and who acts on the observed signal? |
| `sources-and-research-brief.md` | Dated provenance, premise checks, expert lenses, and public-source leads as of 2026-06-23 | Public mappings remain unrefreshed and summaries are not direct current authority | Does a consequential mechanism require current primary-source retrieval? |

The map and brief are not the corpus by themselves. The map tells an agent where historical material lives; the destination files contain the candidate guidance; the brief records the provenance boundary; and the target determines whether any candidate is usable. Omitting that chain can produce two opposite errors: treating navigation metadata as implementation doctrine or treating a detailed source example as target fact.

**Default extraction procedure**

1. State the accepted backend outcome, target revision, current framework, changed call path, non-goals, and cost of a wrong route.
2. Use the map to select one primary mode and only companion modes attached to changed risks.
3. Read the complete relevant source region, including warnings, alternatives, and verification prompts; do not lift a single attractive example out of its boundary.
4. Create one claim record for each consequential recommendation. Include source path, heading, frozen hash, bounded paraphrase, role, target boundary, confidence, and refresh status.
5. Inspect the target for governing instructions, effective versions, existing abstractions, test fixtures, deployment constraints, and owner policy.
6. Mark the claim `promoted`, `adapted`, `conditional`, `rejected`, `superseded`, or `orientation-only`. Record why, not merely the label.
7. Bind every promoted or adapted mechanism to an observable requirement and the smallest target gate that can falsify it.
8. Retain unresolved currentness and environment gaps. A missing observation is not permission to fill it with a familiar Kotlin default.
9. Remove a source from the active route when it changes no decision, risk, gate, owner, or recovery path.
10. Version any recurring shortcut and record its invalidation event, generic fallback route, and retirement owner.

**Claim disposition record**

```text
Claim identifier and bounded paraphrase
Frozen source path, heading, and SHA-256
Role: routing, shared, framework, test, risk, runtime, or provenance
Target outcome, revision, framework, and affected call path
Disposition: promoted, adapted, conditional, rejected, superseded, orientation-only
Reason and rejected baseline
Observable requirement and negative case
Executed target gate and result, or exact missing evidence
Current-authority refresh status where version or security matters
Owner, consumers, review date, invalidation event, and fallback route
```

For this evolved reference, the frozen source hashes recorded during local review are:

| Source | SHA-256 |
|---|---|
| `reference-map.md` | `7451085f357ed6af8fdd41f592e83f5f4b5c7aa858be8a5456390b377f00f180` |
| `sources-and-research-brief.md` | `2f73340890073548e7c9a723ba051528e0097581444889cc7a8fa400026a1ee1` |
| `SKILL.md` | `e3413837049aa6f31d325fa368bb8b9dcce7f298c770b42cd5f13c1217c3a410` |
| `kotlin-backend-playbook.md` | `8654c3a4c68cda2514c546035e7a7908a99ad0f884088b7bf329abf807c31994` |
| `kotlin-spring-ktor-idioms.md` | `02c20786240e893fc258f4e067557bc65dcdafcac11a6efbdd049710b827ac5d` |
| `kotlin-backend-testing-and-fixtures.md` | `92f45a34cc8ac472b930eba33e4ffb6a442719baa53dd8caabd43006dfa99e26` |
| `kotlin-backend-security-and-resilience.md` | `8a07eb77e27a3b508224db76c60e20508b8b3d13b81fce86e87ea052be7d14a5` |
| `kotlin-backend-runtime-and-ops.md` | `d0a218f3c5d7b07c561cd4aba94b7c943aa7575cd439d371fdbaf4e5415b1069` |

These hashes establish source identity, not currentness or applicability. Rehashing a mutable copy without recording its revision would weaken rather than strengthen provenance.

**Conflict and lifecycle rules**

- Project instructions and accepted target policy govern their declared scope; repository behavior and executed tests describe the inspected revision; frozen skill files describe historical guidance; current direct public authority resolves version-sensitive mechanisms when retrieval is allowed.
- When authorities disagree, do not average them. Identify whether the conflict concerns outcome, policy, API compatibility, environment, or observed behavior, then send it to the corresponding owner or gate.
- Prefer the smallest reversible route while a conflict is unresolved. Security, data integrity, irreversible effects, and rollout hazards may instead require a stop because experimentation itself has consequence.
- Promote a repeated route only after representative success and failure cases demonstrate that it preserves the same boundary across its declared consumers.
- Demote a shortcut when target versions, framework, call shape, ownership, provider behavior, threat model, data semantics, deployment platform, or gate coverage leaves its scope.
- Supersede rather than silently overwrite historical rationale. Preserve the predecessor, successor, migration boundary, and reason enough for future diagnosis.
- Retire guidance when no supported consumer remains or when its fallback route is safer and no more costly. Delete generated shortcuts only under the repository's own ownership and history policy.

**Worked classifications**

Good: the map routes a Ktor endpoint task to the Ktor region, target inspection confirms Ktor and the configured test host, and a focused route fixture proves plugin plus error behavior. The map remains routing authority; the target build and result become applicability evidence; the mechanism is promoted only for the inspected version and boundary.

Bad: a reviewer calls the whole playbook canonical, copies a Spring transaction example into a read-only Ktor service, invents a Gradle command, and cites the clean source table as proof. Navigation, implementation, framework, data, and verification roles have collapsed into one unsupported claim.

Borderline: the security source recommends bounded retry for a transient read, but provider effect semantics and total deadline are unknown. Keep the recommendation conditional and record the missing provider contract. The absence of a confirmed write does not prove repetition is safe.

Another valid rejection: a historical source names Testcontainers, while the target has no database or broker boundary and its pure service test proves the accepted behavior. Reject that infrastructure mechanism for this route without declaring Testcontainers generally wrong. Reopen if a production-dialect, broker, or lifecycle difference becomes consequential.

**Hierarchy verification**

- Can each consequential statement be traced to a bounded frozen source region, target observation, owner policy, executed result, or clearly labeled synthesis?
- Does every source in the active route answer a different question or strengthen a required gate?
- Are Spring and Ktor alternatives kept separate unless migration itself is accepted?
- Are public-source dates and no-browse status visible where currentness matters?
- Can a reviewer distinguish source identity, semantic relevance, target applicability, successful behavior, and lifecycle ownership?
- Does each conditional item name the missing observation and the action that could resolve it?
- Does each rejected or superseded item retain a reopen condition rather than disappearing from provenance?
- Can the route be reversed without losing accepted requirements, target evidence, or historical rationale?

The hierarchy is successful when it makes a wrong source role easy to detect before implementation. Its deeper purpose is context control: high-authority evidence should narrow decisions, while low-authority detail should remain searchable but unable to silently expand scope. Once a routing shortcut is shared, generated, or enforced, it becomes maintained project behavior and needs the same ownership, regression, compatibility, and retirement discipline as other development infrastructure.

## Theme Specific Artifact

The required artifact is a **Kotlin Backend Route Evidence Record**. It is a reviewable contract between source selection and target action: what outcome is accepted, which target facts were observed, why each mode and source region is present, which alternatives were rejected, what behavior must hold, what evidence was executed, and what change invalidates the route.

This record is not a source summary, a generic Kotlin checklist, or a claim that every field is known. It can stop at orientation when repository evidence is unavailable. It becomes implementation-ready only when concrete target claims have locators and planned gates. It becomes a verified handoff only after required gates have executed and their results, limitations, and owners are recorded.

**Completion levels**

| Level | Minimum legitimate content | Prohibited claim | Exit condition |
|---|---|---|---|
| orientation | accepted question, known non-goals, provisional surface, candidate modes, frozen source regions, and missing target evidence | exact target architecture, version, command result, or production safety | target inspection can begin or an explicit evidence blocker is handed off |
| planning | target revision, governing instructions, effective framework and build, changed call path, requirements, risk modes, source dispositions, owners, and proposed gates | a proposed command or fixture is reported as executed | every implementation decision is linked to accepted behavior and a falsifiable gate |
| implementation-ready | exact target files, interfaces, dependencies, mechanism decisions, negative cases, rollout boundary, and runnable discovered gates | compatibility, latency, security, or recovery success before observation | reviewer can identify the next edit, test, stop condition, and reversal path |
| verified handoff | executed commands and environments, results, requirement coverage, known gaps, owner acceptance, rollback or recovery, and invalidation triggers | unqualified production guarantee beyond the observed revision and environment | all accepted gates pass or every residual risk has an accountable disposition |

Do not upgrade the level because prose is detailed. Evidence state controls the level.

**Required core fields**

| Record field | Completion rule | Failure prevented |
|---|---|---|
| `record_identity` | unique route identifier, creation time, authoring lane, target revision, and current completion level | stale evidence being attached to a different target state |
| `accepted_outcome` | user-visible or operator-visible success, failure, and recovery in observable terms | implementation activity replacing the actual decision |
| `scope_and_non_goals` | changed service, route, worker, call path, owners, and explicit exclusions | hidden framework migration, persistence, infrastructure, or rollout expansion |
| `target_facts` | governing instructions, effective Kotlin and framework versions, build wrapper, modules, existing abstractions, test surfaces, and deployment boundary with exact locators | local examples being presented as target facts |
| `primary_and_companion_modes` | one primary mode plus each companion's changed boundary and activation reason | loading every source without prioritization |
| `source_dispositions` | frozen path, heading, hash, bounded claim, role, target question, and promoted, adapted, conditional, rejected, or orientation-only status | whole-file canonization and untraceable synthesis |
| `requirements_and_risks` | stable identifiers for normal, boundary, failure, cancellation, duplicate, security, data, and recovery behavior that actually applies | happy-path-only implementation and review |
| `decision_ledger` | chosen mechanism, rejected baseline, causal reason, assumptions, owner, and reversal signal | familiar framework patterns winning without comparison |
| `verification_plan` | discovered command or reviewer gate, environment, fixture, expected observation, and deliberate failure probe | invented commands and green tests that cannot falsify the claim |
| `observed_results` | exact executed action, revision, environment, status, concise result, timestamp, and limitation | plans being mistaken for test evidence |
| `uncertainty_register` | unresolved fact, consequence, evidence kind, confidence boundary, resolution action, owner, and deadline or stop | ambiguity being filled with unsupported precision |
| `release_and_recovery` | compatibility boundary, rollout unit, monitoring signal, stop trigger, rollback or forward recovery, and authority to act | correct code becoming an unsafe release |
| `lifecycle` | consumers, review event, invalidation triggers, successor, generic fallback route, retention, and retirement owner | promoted shortcuts silently becoming stale infrastructure |

Conditional blocks are required only when their boundary changes. For example, omit persistence details when no state or schema changes, but record that rejection and its reopen condition. A security block can state that the existing authorization boundary is unchanged and cite the focused regression gate; it need not invent a new threat model. A runtime block becomes mandatory when config, secret injection, health, telemetry, deployment, migration, traffic, or shutdown behavior changes.

**Source disposition entry**

```yaml
claim_id: ROUTE-KBRR-013-01
claim: Preserve the target Ktor framework for the accepted route change.
source:
  frozen_file: reference-map.md
  region: New Ktor Service Or Route
  sha256: 7451085f357ed6af8fdd41f592e83f5f4b5c7aa858be8a5456390b377f00f180
  role: routing-entrypoint
target:
  observation: Existing application module and configured Ktor test host are present.
  locator_kind: repository-path-and-effective-build
disposition: promoted-for-inspected-revision
decision_effect: Route to Ktor idioms and exclude Spring implementation guidance.
gate: Existing Ktor route fixture must observe plugin, validation, and error behavior.
reopen_when: Framework migration is accepted or effective Ktor wiring changes.
```

The example illustrates record shape. Its target observation is not a finding about an unspecified repository.

**Decision entry**

Every consequential choice should answer the following compact sequence:

```text
Accepted behavior protected
Target boundary and revision observed
Selected option and owner
Simpler or current baseline rejected because
Source evidence and target evidence kept separate
Assumptions and unknowns
Negative case that could disprove the choice
Executed or planned gate, with state labeled
Rollback, adaptation, or escalation path
Event that requires routing again
```

Do not duplicate an ADR, requirement catalog, test report, or deployment runbook inside this record. Link the authoritative artifact by stable locator and retain only the route-specific disposition. Promote a decision into an ADR when it changes durable architecture across tasks. Promote behavior into executable requirements when multiple implementations or releases must preserve it. Use a trace matrix when audit or cross-system coverage warrants it. The route record remains the index that explains why those artifacts were activated.

**Illustrative bounded record**

```yaml
record_identity:
  route: KBRR-EXAMPLE-READ-PRICE
  completion_level: planning
  target_revision: inspected-revision-required-before-reuse
accepted_outcome:
  success: A valid request returns the service-owned price response.
  failure: Invalid input and provider failure retain the service-owned error contract.
  recovery: Caller cancellation terminates request-scoped provider work.
scope_and_non_goals:
  primary_surface: existing Ktor route
  exclusions:
    - no framework migration
    - no durable storage
    - no background refresh
modes:
  primary: ktor
  companions:
    - coroutine for request scope and cancellation
    - resilience for provider deadline and failure
    - testing for target route and provider fixtures
    - operations when timeout config or signals change
source_dispositions:
  - map region routes to Ktor and remains historical navigation evidence
  - Ktor idiom region is conditional on effective target version
  - persistence guidance is rejected while the outcome stores no state
first_negative_case: Provider completion arrives after caller cancellation.
unresolved_owner_decisions:
  - acceptable price freshness
  - provider fallback semantics
stop_condition: Do not implement fallback until its product and operations owners agree.
reopen_when:
  - provider call becomes an effectful write
  - cache or queue is introduced
  - framework or deployment boundary changes
```

This record is deliberately `planning`: its target revision, exact locators, discovered commands, and executed results are still required before implementation-ready or verified status. Good records expose that gap. Bad records replace it with plausible paths such as `src/main/kotlin`, a guessed `./gradlew test`, or an arbitrary latency objective.

**Validation layers**

| Layer | Reviewer or machine check | Evidence required |
|---|---|---|
| schema | identifier, level, outcome, target revision, modes, dispositions, requirements, gates, uncertainty, owner, and invalidation fields satisfy level rules | parsed record and deterministic validation result |
| identity | frozen source hashes, target revision, effective build, and locators refer to the intended inputs | hash output, revision identifier, and repository inspection |
| semantic | selected modes and source regions correspond to changed target boundaries; alternatives remain separated | call-path review and decision ledger |
| authority | observations, owner policy, historical facts, external facts, synthesis, plans, and results are labeled independently | evidence-kind review and accountable acceptance |
| behavior | each consequential requirement has a gate that observes success and at least one relevant failure or boundary case | executed focused and production-like results as required |
| falsifiability | the gate fails when the claimed boundary is deliberately broken in a controlled fixture | mutation, negative control, or pre-fix failure evidence |
| lifecycle | route has consumers, invalidation events, fallback, successor handling, and retirement ownership proportional to reuse | ownership record and review trigger |

**Acceptance probes**

- Can a reviewer identify which facts came from frozen sources and which were observed in the target?
- Does each selected mode protect a named changed boundary, and does each omitted mode have a defensible reopen condition?
- Can every concrete path, version, command, fixture, and result be located or reproduced?
- Is the earliest unowned product, security, data, provider, or operations decision an explicit stop rather than a hidden assumption?
- Do negative controls show that required gates can catch a wrong framework route, error mapping, transaction, cancellation, retry, or rollout choice?
- Can the next agent resume without reading conversation history and without treating planned work as completed evidence?
- Can the route be reversed or rerun after the target, source, owner, or environment changes?

**Good record:** one bounded outcome, exact target revision, Ktor and Spring branches kept separate, each source assigned a claim role, persistence rejected for a read-only path, discovered fixtures executed, unresolved provider behavior owned, and route invalidation tied to concrete changes.

**Bad record:** every mode selected, source filenames pasted without claims, generic commands marked green, framework version inferred from examples, retry called safe without effect classification, and no owner or recovery path.

**Borderline record:** target inspection and focused tests are complete, but production proxy cancellation behavior is unknown. Keep the route verified for application behavior and conditional for deployment behavior; require the production-like observation before making the broader operational claim.

When recurring route records demonstrate the same target pattern across representative success and failure cases, a team may promote their stable core into a generated template or local shortcut. Version that template, identify consumers, test its validator, preserve a generic fallback, and demote it when its framework, versions, ownership, or risk assumptions change. The artifact then acts as a compact context cache, but only while it remains reversible and evidence-linked.

## Worked Example Set

These examples teach routing decisions, not copyable repository facts. Framework versions, file paths, wrappers, dependency behavior, commands, owners, service objectives, and production policy must be rediscovered. Each family holds an accepted outcome steady while changing the evidence route so the reason for `good`, `bad`, or `borderline` is inspectable.

**Example family A: pure domain rule inside a Spring service**

Accepted outcome: reject a booking interval whose end precedes its start, regardless of whether the rule is reached from HTTP, a worker, or an internal service call.

| Variant | Route taken | Why it receives that classification | Required next evidence |
|---|---|---|---|
| good | Inspect target type and call sites; select Spec, Type, Domain Validation, and Testing; keep the rule framework-free; exercise valid, equal-boundary, reversed, and alternate-entry cases | The route follows the invariant across entry surfaces and excludes unrelated framework, persistence, and runtime work | Target unit or property fixture plus one test through each materially different entry path |
| bad | Put the rule only in a Spring request annotation, load the full Spring stack, and call the endpoint test sufficient | Correct HTTP behavior can coexist with worker or internal bypass because the invariant was routed to transport validation | A non-HTTP call demonstrates the missing domain enforcement |
| borderline | Existing policy deliberately treats equality differently for two booking categories, but category ownership is unclear | The technical location can be selected, while the actual domain rule cannot be invented | Product or domain owner resolves the category semantics before implementation-ready status |

Good route record excerpt:

```text
Primary mode: specification
Companions: Kotlin type design, domain validation, focused testing
Rejected: Spring implementation guidance beyond verifying unchanged request mapping
First negative case: reversed interval through a non-HTTP entry path
Gate: discovered domain test surface plus representative alternate caller
Reopen: persistence constraint or authorization changes the invariant
```

Seductive shortcut: request annotations look concise and idiomatic in Spring. They are still the wrong route when the accepted invariant must survive outside request binding. The problem is not annotation quality; it is boundary mismatch.

**Example family B: read-only Ktor route calling an external provider**

Accepted outcome: return the service-owned price response for valid input, preserve stable errors on provider failure, and stop request-scoped provider work on cancellation.

| Variant | Route taken | Why it receives that classification | Required next evidence |
|---|---|---|---|
| good | Confirm existing Ktor and client wiring; select Ktor, Coroutine, Resilience, Testing, and conditional Operations; reject persistence; classify provider effects and deadlines; use a controllable provider adapter | The route preserves framework, treats cancellation and dependency failure as correctness, and avoids invented state | Effective target build, Ktor test host, client behavior, timeout config, cancellation fixture, and owner policy for fallback |
| bad | Recommend Spring WebClient, add a generic retry, wrap a blocking provider SDK in `suspend`, and report a guessed Gradle command as passed | Familiar Kotlin mechanisms replace target framework, effect classification, execution model, and observed proof | Target inspection should reject the framework and command claims before code is edited |
| borderline | A stale-price fallback could improve availability, but freshness, privacy, invalidation, storage, and outage policy are unowned | Routing identifies Persistence, Security, Resilience, and Operations questions, but cannot authorize the fallback | Product, data, security, and operations owners define the fallback contract and representative failure gate |

Good route record excerpt:

```text
Primary mode: Ktor
Companions: coroutine, resilience, testing, operations if config or signals change
Rejected: persistence while the accepted outcome stores no price
Conditional: retry until provider effect, rate, deadline, and duplicate semantics are known
First negative case: provider completes after caller cancellation
Gate: configured Ktor test host with controlled timeout and cancellation
Reopen: provider write, cache, queue, auth-policy, or deployment change
```

Seductive shortcut: `suspend` syntax can make a blocking SDK look asynchronous. The route remains wrong until actual dependency calls, dispatcher or executor use, pool capacity, deadline, and cancellation are observed.

**Example family C: Spring persistence change with a schema migration**

Accepted outcome: store a unique external request key with a new order so repeated accepted requests return the original result and concurrent distinct requests remain independent.

| Variant | Route taken | Why it receives that classification | Required next evidence |
|---|---|---|---|
| good | Select Spring, Persistence, Idempotency, Migration, Testing, and Operations; define key ownership and transaction boundary; use the production dialect for uniqueness and migration evidence; plan compatibility and rollback or forward recovery | The route recognizes that duplicate behavior depends on database atomicity and deployment ordering, not only service code | Target schema, ORM mapping, transaction call path, concurrent duplicate fixture, production-dialect migration run, and rollout plan |
| bad | Check for an existing key in memory, insert later, use an in-memory database, and call the handler retry-safe | The route ignores races, multi-instance state, dialect behavior, unknown commit outcomes, and migration compatibility | Concurrent same-key attempts and real uniqueness enforcement reveal the defect |
| borderline | A unique index is straightforward, but the table already contains duplicate historical keys | The desired invariant is clear while cleanup, winner selection, downtime, and reversibility require owner decisions | Data profile, deterministic remediation policy, migration rehearsal, and rollout authority |

Good route record excerpt:

```text
Primary mode: persistence
Companions: Spring, transaction, idempotency, migration, testing, operations
Chosen boundary: database uniqueness inside the accepted transaction
Rejected baseline: process-local pre-check because it races across requests and instances
First negative case: concurrent duplicate requests before either transaction commits
Gate: production-dialect constraint and migration fixture under representative concurrency
Reopen: key scope, retention, partitioning, or deployment ordering changes
```

Seductive shortcut: a mock repository can prove service branching but cannot prove database uniqueness, isolation, constraint mapping, or migration behavior. It remains useful for orchestration and insufficient for the claimed atomicity.

**Example family D: Ktor-triggered durable export worker**

Accepted outcome: acknowledge an export request, execute the export after the request ends, survive process restart according to the accepted durability contract, and avoid duplicate published artifacts.

| Variant | Route taken | Why it receives that classification | Required next evidence |
|---|---|---|---|
| good | Split request acceptance from worker completion; select Ktor for the ingress and Coroutine, Broker or Durable Work, Idempotency, Resilience, Testing, and Operations for execution; define work identity, lease or delivery semantics, restart, and shutdown | The route does not pretend request-scoped coroutines provide durable background work | Broker or durable store behavior, duplicate delivery fixture, crash and restart observation, shutdown test, and recovery owner |
| bad | Launch an untracked coroutine from the route, return success, and rely on application logs to notice losses | Work is detached from request success without durable ownership, bounded scope, retry identity, or restart semantics | Cancel request and restart process to expose lost or duplicated work |
| borderline | The export is currently small enough for request scope, but product proposes future large datasets | Present behavior may remain synchronous; anticipated scale alone does not authorize queue infrastructure | Define current deadline and size envelope, measure representative work, and reopen only when accepted bounds fail |

Good route record excerpt:

```text
Primary mode: worker outcome after an explicit split
Companions: Ktor ingress, durable work, idempotency, resilience, testing, operations
Rejected baseline: untracked request coroutine because completion must survive request and restart
First negative case: process stops after work acceptance and before artifact publication
Gate: restart plus duplicate-delivery scenario with one accepted artifact identity
Reopen: durability, artifact ownership, broker, or workload envelope changes
```

Seductive shortcut: structured concurrency is valuable for scoped work, but a correctly scoped request child should be cancelled with the request. Durability requires a different owner and persistence boundary rather than a wider untracked scope.

**Cross-example evaluation rubric**

Score the route, not the fluency of its prose or code.

| Criterion | Acceptable evidence | Common wrong answer |
|---|---|---|
| outcome boundary | one observable success, failure, recovery, and explicit non-goals | a list of implementation tasks without accepted behavior |
| target fidelity | exact framework, effective build, call path, and existing conventions from inspected target | framework inferred from the reference or filename |
| mode economy | one primary mode and companions tied to changed risks | every mode selected because each seems generally useful |
| source roles | bounded claims with navigation, implementation, target, and result authority separated | a whole source called canonical for all decisions |
| alternatives | simpler baseline and consequential alternative compared causally | preferences such as modern, clean, or idiomatic without boundary analysis |
| negative path | earliest representative failure, race, cancellation, abuse, or recovery case | only a normal response example |
| verification | discovered gate that can fail when the claimed behavior is broken | plausible command copied from generic guidance |
| uncertainty | missing fact, consequence, owner, resolution, and safe interim state | vague confidence warning followed by implementation anyway |
| lifecycle | target revision, invalidation event, fallback, and route owner | static advice with no refresh trigger |

**How to verify the examples themselves**

1. Hide the good, bad, and borderline labels.
2. Ask a reviewer to state the accepted outcome, primary mode, companion modes, earliest unsafe assumption, next source region, and next target gate.
3. Compare the response with the explicit reason table, not with exact wording.
4. Mutate one fact: change Ktor to Spring, read to write, request scope to durable work, mock database to production dialect, or planned gate to executed result.
5. Confirm the reviewer changes the route and can explain the causal boundary.
6. Add a controlled behavior observation where a mechanism claim is central; reviewer consensus alone is not runtime proof.

Strong disagreement is a signal to inspect authority: product semantics go to product ownership, threat behavior to security ownership, data remediation to data ownership, current API compatibility to direct current authority plus target execution, and release behavior to platform or operations ownership.

**Transfer limits**

- Reuse the question sequence and evidence categories, not the example's paths, commands, status codes, time budgets, dependencies, or topology.
- Keep Spring and Ktor examples as separate branches unless framework migration is itself accepted and tested.
- A route that is good under one target revision can become borderline after a dependency, policy, provider, schema, or deployment change.
- A borderline route is not a weaker implementation plan. It is a deliberate stop at the earliest unresolved consequential decision.
- A bad route can contain locally idiomatic Kotlin. The classification concerns evidence and boundary fit, not surface syntax.

These scenario families can become decision fixtures for future reference review. Rotate frameworks, target facts, effects, failures, and ownership gaps so agents must investigate rather than memorize. When an incident reveals a new routing failure, add the smallest matched variant that would have exposed it and record the source or target change that invalidates the old lesson.

## Outcome Metrics and Feedback Loops

Measure whether routing produces a smaller, more accurate, more falsifiable path from accepted outcome to target evidence. Do not treat paragraph count, source count, test count, pass rate, tool calls, or elapsed time as success by themselves. A fast route that guesses Ktor versus Spring, labels a planned command as executed, or misses a transaction race is a faster failure.

The measurement unit is one **routed outcome** under one target revision: a feature slice, defect investigation, review question, migration step, or operational change with a route record and an accountable disposition. Compare outcomes within a consequence and complexity cohort. A pure type rule, a schema migration, and a durable worker should not share an undifferentiated speed baseline.

**Minimal route-health scorecard**

| Signal | Definition and denominator | Why it matters | Misleading interpretation to reject |
|---|---|---|---|
| target discovery completeness | required target facts observed before concrete implementation claims divided by required facts for that route level | detects framework, build, path, convention, and environment guessing | more discovered files always means better context |
| mode precision | selected modes that protect a named changed boundary divided by all selected modes | exposes loading every reference defensively | a narrow route is automatically complete |
| mode omission escapes | reviewer- or outcome-confirmed changed boundaries absent from the route, per eligible outcome | detects under-routing of data, security, concurrency, runtime, or release risk | every later-added mode proves the original route was wrong; scope may legitimately change |
| source decision yield | active source regions that alter a decision, requirement, gate, owner, or recovery path divided by active source regions read | makes progressive disclosure measurable | unused source reading has no orientation value, or maximum yield is always optimal |
| unsupported claim escape | concrete target, API, compatibility, security, performance, or result claims that reach handoff without adequate evidence, per reviewed outcome | directly measures authority collapse | an unverified but explicitly conditional statement is an escape |
| first-pass route acceptance | routes accepted without material source, framework, boundary, or evidence correction, divided by reviewed routes | identifies avoidable routing churn | reviewer acceptance proves runtime correctness |
| material decision reversal | selected mechanisms reversed after target evidence that should have been available at routing time, per eligible outcome | reveals premature recommendations | reversal after a new requirement or environment change is a defect |
| uncertainty resolution quality | consequential unknowns with consequence, owner, resolution action, and safe interim state divided by consequential unknowns found | rewards honest stops and actionable handoff | fewer recorded unknowns necessarily means more certainty |
| gate coverage | accepted consequential behaviors linked to an appropriate executed or explicitly planned gate, divided by those behaviors | traces requirements to proof | one broad integration test covers every boundary equally |
| gate falsifiability | sampled gates that fail under a controlled relevant defect divided by sampled gates | distinguishes proof-capable tests from ceremonial green checks | mutation survival always means application behavior is wrong; the probe may be invalid |
| verification truthfulness | reported results whose exact command, revision, environment, and status match retained evidence, divided by reported results sampled | prevents planned or guessed commands from becoming facts | truthful reporting means the selected gate is sufficient |
| downstream route defect | implementation, review, release, or incident defect whose root cause includes a wrong or missing route decision, per eligible delivered outcome | connects reference quality to consequence | all downstream defects belong to the router |
| recovery clarity | failed or conditional outcomes with an executable rollback, adaptation, escalation, or next-reference route, divided by such outcomes | measures whether failure leads somewhere safe | a named owner without an action path is recovery |
| invalidation recognition lag | elapsed target or source change to route demotion, reroute, or explicit acceptance of retained validity | tests lifecycle responsiveness | shortest lag is always best; investigation and coordinated rollout may be necessary |

Set thresholds from local baselines, consequence, and owner policy. This reference does not establish a universal number of minutes, sources, tests, accepted routes, or allowable defects. For trust-boundary violations, fabricated results, or irreversible data hazards, owners may set a zero-tolerance gate. For noisy review labels, use ranges and case inspection rather than false precision.

**Domain-specific additions**

Activate only the metrics attached to the changed boundary.

| Boundary | Useful routed outcome signal | Required interpretation context |
|---|---|---|
| framework wiring | wrong-framework recommendation rate; focused versus full-context defect detection | effective framework version, configured plugins or filters, and test slice |
| coroutines and blocking | cancellation propagation observation; event-loop or pool saturation under representative load | actual dependency behavior, dispatcher or executor, concurrency, deadline, and workload |
| persistence | production-dialect discrepancy; concurrent invariant violation; migration compatibility result | schema revision, database version, isolation, data profile, and rollout order |
| external integration | timeout, retry, duplicate-effect, malformed-response, and unknown-effect outcomes | provider contract, client behavior, total deadline, rate policy, and effect identity |
| security | deny-path coverage, sensitive-output escape, secret exposure, and abuse-control observation | accepted threat boundary, principal source, policy owner, and environment |
| runtime | config startup failure, health semantics, signal actionability, shutdown completion, and recovery result | deployment platform, dependency ownership, traffic state, and service objective |
| routing workflow | reviewer decision time, material correction loops, source yield, and resume completeness | task cohort, reviewer role, target access, and route completion level |

Do not import the archive seed's illustrative latency guidance into this measurement model. Runtime latency needs a target-owned service objective, representative workload, environment, warmup, concurrency, percentile method, and error accounting. Reviewer time likewise needs a comparable task cohort and must be paired with correction and escape rates.

**Event record for measurement**

```text
Routed outcome identifier, consequence class, and target revision
Route completion level and selected primary plus companion modes
Source regions read, dispositions, and decisions changed
Target facts available before routing and facts discovered later
Requirements, negative cases, planned gates, and executed results
Reviewer corrections with material or editorial classification
Implementation or release defect and root-cause contribution
Unknowns, owners, resolution actions, and recovery result
Source or target invalidation event and recognition time
Metric evidence kind: observed, reviewer-labeled, inferred, or forecast
```

Deduplicate retries and revisions under the same routed outcome. Preserve correction lineage rather than counting each regenerated response as a new success. Record excluded samples and why. Never let the author alone adjudicate semantic correctness for a shared or consequential route.

**Feedback loop**

1. **Capture:** persist the route record, target revision, selected sources, decisions, gates, results, corrections, and unresolved risks.
2. **Detect:** identify a threshold breach, trend, reviewer disagreement, controlled-failure survival, incident, dependency change, or shortcut invalidation.
3. **Classify:** locate the earliest broken link: intake, target discovery, mode selection, source role, mechanism decision, requirement, gate, result reporting, handoff, or lifecycle.
4. **Bound:** state one hypothesis about why the route failed and the smallest source, example, validator, workflow, or adjacent-routing change that addresses it.
5. **Test:** replay representative decision fixtures, including a negative control and an exception that should retain the old route.
6. **Deploy:** version the guidance change, identify consumers, preserve fallback, and record expected metric movement plus possible harm.
7. **Observe:** compare the same eligible cohort and inspect cases behind aggregate movement.
8. **Retain, adapt, or revert:** keep the change only when evidence supports the intended improvement without unacceptable mode omission, false stops, or review cost.

**Worked feedback case**

Observed event: a generated plan recommends Spring WebClient for a target that already uses Ktor. A reviewer catches it before implementation.

| Step | Recorded interpretation |
|---|---|
| direct signals | one material first-pass correction; one wrong-framework candidate; no downstream implementation escape |
| earliest failure | target framework was not inspected before framework-specific retrieval |
| non-cause | the Spring source itself may be valid for Spring targets; deleting it does not solve routing |
| bounded change | strengthen target preflight and make Spring and Ktor branches mutually exclusive absent an accepted migration |
| fixture | replay matched Spring, Ktor, unknown-target, and explicit-migration cases with labels hidden |
| success evidence | Ktor and Spring route correctly, unknown target remains orientation-only, migration activates both with transition gates |
| regression risk | overstrict branching could hide shared playbook guidance or block legitimate migration analysis |
| lifecycle action | version the routing rule and reopen on framework-detection or project-policy changes |

Bad metric response: declare improvement because reviewer time fell after removing framework checks. The speed movement is uninterpretable while wrong-framework escapes rise.

Borderline metric response: route acceptance improves over a small sample while source yield falls. Inspect cases before acting. The router may have become more focused, or reviewers may be accepting shallow routes that omit risks.

**Audit questions**

- Are event definitions stable enough that two reviewers classify the same material correction similarly?
- Are cohorts separated by outcome type, boundary count, consequence, target access, and completion level?
- Can every reported pass or failure be traced to retained evidence rather than author recollection?
- Do speed and volume signals have correction, escape, and consequence guards?
- Has a sampled gate been shown to fail under a relevant controlled defect?
- Are unknowns counted as healthy when they prevent unsupported action, and unhealthy when they lack owners or resolution?
- Does every collected signal have an owner, review cadence, and predeclared action range?
- Are metric changes explained with direct observations, labeled judgments, and uncertainty rather than causal overclaiming?

**Review cadence**

- After every generated-reference edit: run structural, heading, packet, uniqueness, unresolved-marker, table, fence, ASCII, whitespace, and focused verification gates.
- At a locally selected sample cadence: review route records for semantic fit, authority separation, source yield, unsupported claims, and gate falsifiability.
- On framework, language, database, provider, build, security policy, or deployment change: reassess affected claims and promoted shortcuts.
- On material reviewer disagreement: identify the authority and update a decision fixture if the ambiguity can recur.
- On incident or escaped defect: trace the earliest route failure and test a bounded correction against representative and exception cases.
- On sustained unexplained metric movement: inspect raw cases before changing thresholds or guidance.

Known facts in this model are recorded events and executed observations, subject to instrumentation quality. Reviewer labels are judgments. Prevented incidents, counterfactual time saved, and business impact are inferences or forecasts and must be presented as such. Confidence can rise when route records, independent review, controlled failures, target tests, and production signals converge, but none makes the router the sole cause.

The mature feedback goal is not perfect first-choice accuracy. It is bounded error: unsupported routes stop early, escaped assumptions are diagnosable, corrections update the right layer, and target or source drift invalidates shared shortcuts before they silently govern new work.

## Completeness Checklist

Declare one completion level before applying this checklist: `orientation`, `planning`, `implementation-ready`, or `verified handoff`. A route is complete only for the promise attached to that level. Orientation may end with explicit missing target evidence; verified handoff may not present a planned command as an observed result.

Use four result states:

- **satisfied:** required evidence exists and supports the check for the named target revision.
- **not applicable:** the boundary does not change, with a concise reason and reopen condition.
- **conditional:** a named fact or owner decision is missing, with consequence and resolution action.
- **blocked:** continuing would create unsupported or unsafe target action.

An empty field has no valid meaning. Selecting every mode, source, or test to avoid a not-applicable decision is also incomplete because priority and scope have been lost.

**Level exit contract**

| Check family | Orientation | Planning | Implementation-ready | Verified handoff |
|---|---|---|---|---|
| accepted outcome | question, user or operator, and consequence stated | success, failure, recovery, and non-goals accepted | stable requirement identifiers and owners | accepted behavior and residual-risk disposition retained |
| target | missing evidence named | revision, instructions, framework, build, call path, and test surfaces inspected | exact edit and dependency boundaries known | executed revision and environment recorded |
| routing | candidate primary and companion modes | selected modes tied to changed boundaries | source regions have claim dispositions | reroute triggers and rejected modes retained |
| mechanism | no implementation claim required | alternatives and owner decisions identified | chosen mechanisms, assumptions, and reversal signals explicit | observed behavior supports only reported mechanism claims |
| verification | target gate classes identified | discovered commands or reviewer gates planned | fixtures, negative cases, environments, and expected observations runnable | exact commands and results retained; required gates pass or risks are accepted |
| release | consequence and likely owner identified | compatibility and rollout questions activated as needed | recovery, telemetry, and stop conditions ready for changed runtime boundary | rollout evidence, recovery authority, and known gaps handed off |
| lifecycle | source dates and target gap visible | invalidation events named | route owner and fallback identified | consumers, review trigger, successor, and retirement path recorded as needed |

**Intake and scope**

- [ ] The record names one accepted backend outcome rather than a bundle of loosely related implementation tasks.
- [ ] The user-visible or operator-visible success, relevant failures, and recovery behavior are observable.
- [ ] The starting state distinguishes target facts, frozen local evidence, current external evidence, owner policy, synthesis, and unknowns.
- [ ] The cost of a wrong route is stated in terms of compatibility, behavior, trust, data, proof, rollout, or recovery.
- [ ] Non-goals exclude unaccepted framework migration, schema, infrastructure, telemetry, performance, or deployment work.
- [ ] Independently acceptable or reversible outcomes have separate route records, owners, gates, and rollback boundaries.
- [ ] Orientation-only work says so before offering concrete implementation action.

Hard stop: the requested behavior, accountable product decision, or governing scope is contradictory or absent in a way that would change implementation.

**Target discovery**

- [ ] Governing repository instructions and ownership boundaries were read for the inspected target.
- [ ] The exact target revision or equivalent immutable locator is recorded.
- [ ] Effective Kotlin, Java, framework, plugin, and dependency versions come from the target build rather than source examples.
- [ ] The repository wrapper and available build, test, lint, and packaging surfaces were discovered before naming commands.
- [ ] Existing module, route or controller, service, repository, client, worker, configuration, and error-envelope conventions were inspected along the changed call path.
- [ ] Existing focused, integration, production-dialect, contract, and runtime test surfaces were inventoried without assuming all are required.
- [ ] Deployment, proxy, secret, database, broker, and platform boundaries are known or explicitly outside the current completion level.

Hard stop: a concrete implementation-ready target claim lacks a locator, or a named command is not discovered in the target.

**Mode and source route**

- [ ] One primary mode corresponds to the accepted outcome.
- [ ] Every companion mode protects a named changed boundary such as framework wiring, type, validation, persistence, transaction, coroutine, integration, security, resilience, testing, migration, or operations.
- [ ] Every omitted mode has either no changed boundary or a recorded reopen condition.
- [ ] Spring and Ktor implementation branches remain separate unless an explicit migration outcome activates a transition plan.
- [ ] The reference map acts as navigation evidence, destination regions provide candidate guidance, and target observations decide applicability.
- [ ] Each consequential source claim has a bounded path and region, frozen hash where provenance matters, role, target question, disposition, and refresh status.
- [ ] A source remains active only when it changes a decision, requirement, gate, owner, recovery path, or necessary orientation.
- [ ] Version- or security-sensitive public claims are current direct authority when retrieval is allowed, or are labeled unrefreshed and conditional here.

Hard stop: historical source wording is presented as current target or public fact, or incompatible framework branches are combined without migration acceptance.

**Decision quality**

- [ ] The chosen option is compared with the simplest viable baseline and any consequential alternative.
- [ ] The causal reason names the boundary protected, not only adjectives such as modern, clean, robust, scalable, or idiomatic.
- [ ] Blocking versus non-blocking behavior follows actual dependencies, dispatchers or executors, pools, deadlines, cancellation, and workload.
- [ ] Retry follows transient classification, total deadline, effect safety, duplicate identity, provider policy, and overload risk rather than habit.
- [ ] Request-scoped and durable work have different owners, cancellation, restart, and recovery contracts.
- [ ] Persistence decisions include transaction, concurrency, uniqueness, dialect, migration, and rollout implications only when state changes.
- [ ] Security decisions identify principal, policy owner, deny behavior, sensitive output, secrets, and abuse boundary only when relevant.
- [ ] Unknown product, data, security, provider, performance, or operations semantics have owners and safe interim states.
- [ ] Every material choice has a reversal or escalation path and an invalidation event.

Hard stop: an irreversible effect, trust decision, data remediation, or production rollout depends on an unowned assumption.

**Requirements and counterexamples**

- [ ] Requirements use stable identifiers and observable outcomes rather than internal implementation steps.
- [ ] Normal, boundary, invalid, dependency failure, timeout, cancellation, duplicate, concurrency, security, recovery, and compatibility cases are included when their boundaries activate.
- [ ] The earliest negative case capable of disproving the route is identified.
- [ ] Framework status and error behavior follow target policy rather than arbitrary illustrative codes.
- [ ] Performance or capacity requirements have an owner, workload, environment, percentile or throughput method, and error accounting.
- [ ] Good, bad, and borderline examples explain evidence, consequence, and resolution rather than merely applying labels.
- [ ] A seductive locally idiomatic alternative is tested when it can satisfy the happy path while violating the accepted boundary.

Hard stop: the route claims correctness while only a normal case is defined for a consequential failure, race, trust, or recovery boundary.

**Verification readiness**

- [ ] Each consequential requirement maps to the smallest gate that can observe it.
- [ ] The gate is a discovered target command, configured fixture, reviewer procedure, or production-like observation, with environment and expected result.
- [ ] Unit tests prove pure logic; framework fixtures prove configured wiring; real infrastructure proves dialect, broker, provider, scheduler, or lifecycle behavior when those distinctions matter.
- [ ] Mock and fake evidence is not used to claim production infrastructure semantics it cannot model.
- [ ] At least one relevant controlled defect, pre-fix failure, or negative control shows the gate can fail.
- [ ] Planned, running, passed, failed, skipped, blocked, and not-applicable states are reported distinctly.
- [ ] Exact commands, revisions, environments, concise results, and limitations are retained for executed evidence.
- [ ] Full-suite or production-like verification is added when shared wiring, cross-module contracts, deployment, or broad behavior changes.

Hard stop: completion depends on a reported pass that cannot be traced to an executed action and target revision.

**Release and recovery**

- [ ] Compatibility is evaluated for API, data, events, jobs, config, and deployment interfaces actually changed.
- [ ] Migration ordering, mixed-version operation, rollback or forward recovery, and data remediation are defined where schema or protocol changes.
- [ ] Configuration has production-like binding, validation, precedence, and secret handling where runtime input changes.
- [ ] Telemetry signals distinguish actionable outcomes with bounded cardinality and sensitive-data control.
- [ ] Health checks represent service and dependency policy rather than merely process liveness.
- [ ] Shutdown and cancellation semantics preserve accepted in-flight and durable work behavior.
- [ ] Rollout unit, stop signal, authority to act, and recovery path correspond to the changed production boundary.
- [ ] Residual risks have explicit owners and are accepted only under target policy.

Hard stop: a changed production boundary has no owner-authorized recovery or stop path.

**Handoff and lifecycle**

- [ ] Changed reference, packet, route record, target files, and linked authoritative artifacts are listed exactly.
- [ ] Accepted outcome, selected route, rejected alternatives, requirements, commands, results, unknowns, and owner decisions can be reconstructed without conversation history.
- [ ] The handoff distinguishes evidence observed in this revision from forecasts and unrefreshed external claims.
- [ ] Adjacent routing names a more appropriate reference and activation trigger when this file is no longer sufficient.
- [ ] Target, source, framework, dependency, provider, schema, policy, ownership, and environment changes have bounded reroute triggers.
- [ ] Promoted project shortcuts name version, consumers, enforcement, regression gate, generic fallback, review event, successor, and retirement owner.
- [ ] Superseded evidence retains enough rationale and lineage for diagnosis instead of disappearing silently.
- [ ] A fresh reviewer can identify the next action, stop condition, and recovery route from persisted artifacts.

Hard stop: a shared or generated shortcut has no invalidation or fallback path.

**Completion review matrix**

| Layer | Passing question | Controlled challenge |
|---|---|---|
| structural | Are required fields present for the declared completion level? | Remove one required field and confirm validation fails |
| semantic | Do modes, sources, and mechanisms correspond to the changed target boundary? | Swap Spring and Ktor or read and write effects and confirm the route changes |
| authority | Can every claim be classified as observation, policy, historical fact, current external fact, synthesis, plan, result, or forecast? | Relabel a plan as a result and confirm review rejects it |
| behavioral | Do representative gates observe accepted success, failure, and recovery? | Inject the earliest relevant defect and confirm a required gate fails |
| operational | Can rollout stop and recovery proceed under the changed runtime boundary? | Exercise an isolated startup, shutdown, migration, or dependency-failure path as applicable |
| lifecycle | Does target or source drift reopen only affected decisions with lineage intact? | Change one version or policy fact and trace which checks become stale |

**Example completion judgments**

Good planning completion: a Ktor route has exact target framework and module evidence, selected Coroutine and Resilience companions, persistence rejected, provider fallback owned but unresolved, and discovered tests planned. It is planning-complete and blocked from fallback implementation, not globally incomplete.

Bad verified claim: a route record lists `./gradlew test` as green because the archive suggested Gradle, but no wrapper or output was inspected. Structural fields are populated; evidence and verification completion fail.

Borderline handoff: application cancellation tests pass, while proxy disconnect propagation is unavailable in local fixtures. The record may be verified for application scope and conditional for deployment scope. Production-safe cancellation language remains blocked until the platform observation or owner-approved limitation exists.

**Final exit statement**

Before advancing, record:

```text
Declared completion level
Satisfied checks and retained evidence
Not-applicable checks with reopen conditions
Conditional checks with consequence, owner, and resolution
Blocked checks and prohibited next action
Executed gates, exact results, and limitations
Residual risk acceptance and authority
Target revision and events that selectively invalidate completion
```

If an upstream outcome, target, authority, or mechanism changes, reopen dependent checks rather than discarding every result or preserving all results blindly. Completeness should decay selectively: stale evidence becomes visible, while still-valid observations retain revision lineage.

## Adjacent Reference Routing

Remain in this reference while the governing decision is **which evidence route should be used for a Kotlin backend outcome**. Compose a specialist when one changed boundary needs deeper guidance. Transfer primary ownership when the governing question becomes the specialist's decision. Split the work when outcomes have independent acceptance, owners, or rollback. Escalate outside the corpus when product semantics, current authority, target policy, or production risk cannot be decided by reference prose.

Keywords discover candidates; changed behavior activates them. The word `security` in a source filename does not prove a changed trust boundary, and the word `runtime` does not make deployment guidance relevant to a pure value-object edit.

**Adjacent destination map**

| Candidate reference | Activate when the governing question becomes | Keep this router's responsibility | Negative trigger or escalation |
|---|---|---|---|
| `kotlin_backend_playbook_reference-20260710.md` | shared service boundary, Kotlin type, validation, transaction, persistence, coroutine, client, worker, or delivery design | retain accepted outcome, target revision, selected mode set, and integrated handoff | do not use a broad playbook to bypass framework or target discovery |
| `kotlin_spring_ktor_idioms-20260710.md` | exact Spring or Ktor wiring, validation, error handling, dependency, lifecycle, or framework test shape | preserve the confirmed framework branch and migration non-goal | stop if framework or effective version is unknown; migration requires a separate transition outcome |
| `kotlin_backend_testing_fixtures-20260710.md` | which test level, fixture, fake, real dependency, property, concurrency, or framework host can falsify behavior | retain requirement identifiers and decide whether returned evidence is sufficient for the route claim | do not let mock evidence claim database, broker, provider, scheduler, or platform semantics |
| `kotlin_backend_security_resilience-20260710.md` | identity, authorization, input or output trust, secret, abuse, timeout, retry, idempotency, dependency failure, or cancellation becomes primary | reconcile threat and failure decisions with product behavior and target owner policy | escalate unknown threat model, provider effect, or risk acceptance to accountable owners |
| `kotlin_backend_runtime_operations-20260710.md` | config, secret injection, telemetry, health, deployment, migration execution, traffic, shutdown, diagnosis, or recovery becomes primary | carry forward accepted behavior, compatibility boundary, and required release evidence | omit for unchanged runtime; do not invent service objectives or platform topology |
| `kotlin_quality_antipattern_gates-20260710.md` | quality gate, prohibited construct, static policy, or review failure is the central outcome | retain the causal target behavior that the gate protects | avoid cargo-cult bans that have no target policy, consequence, or false-positive analysis |
| `kotlin_reliability_reference_patterns-20260710.md` | reliability mechanism and failure semantics require focused comparison | keep framework, effect, data, and owner assumptions visible | do not replace target service objectives or provider contracts with generic reliability language |
| `kotlin_reference_routing_sources-20260710.md` | provenance, source lineage, duplicate evidence, conflict, or refresh policy is the primary question | decide how source findings affect the active target route | source freshness cannot substitute for target behavior or owner policy |
| `kotlin_backend_skill_entrypoint-20260710.md` | the task needs top-level Kotlin backend skill activation, intake, or workflow entry rather than an already selected route | accept the entrypoint's classified outcome and return to this router for evidence selection | avoid bouncing between entrypoint and router without a changed governing question |
| `kotlin_language_skill_entrypoint-20260710.md` | the question is primarily Kotlin language design outside a backend delivery boundary | retain only backend constraints that materially affect the language decision | pure language questions should not inherit framework, database, or deployment work |

These are candidate paths observed in the working directory, not assertions that every adjacent reference is complete, current, or applicable. Before handoff, verify the destination exists, inspect its current evidence boundary, and preserve a fallback to the frozen local source region if the evolved artifact is unavailable or unsuitable.

**Stay, compose, transfer, split, or escalate**

| Routing action | Choose when | Required record |
|---|---|---|
| stay | this file can select sources, state boundaries, and identify the next target gate without specialist mechanism detail | reason no adjacent reference changes a decision or gate |
| compose | a specialist owns one changed risk while the accepted outcome remains integrated | activation condition, question sent, evidence returned, and reconciliation decision |
| transfer | the original routing question is resolved and the specialist now owns the primary decision | transferred outcome, target revision, constraints, non-goals, authority, and return condition |
| split | two outcomes can be accepted, implemented, verified, released, or reversed independently | separate identifiers, owners, requirements, gates, compatibility, and recovery paths |
| parallel challenge | independent specialist verdicts are needed for a high-consequence or disputed boundary | immutable shared intake, separate assumptions and verdicts, and adjudication authority |
| escalate | product, legal, security, data, provider, service-objective, or production policy lacks accountable resolution | earliest blocked decision, consequence, evidence gathered, safe interim state, and requested owner action |

**Handoff packet**

```text
Parent route identifier and target revision
Accepted outcome, success, failure, recovery, and non-goals
Observed framework, build, call path, and existing conventions
Question the adjacent reference must decide
Changed boundary and cost of a wrong answer
Frozen source regions and target evidence already inspected
Assumptions, unknowns, owner policy, and prohibited inventions
Expected returned artifact, decision, negative case, and gate
Return, split, stop, and escalation conditions
Visited references and unresolved conflicts
```

The receiving reference returns a bounded result:

```text
Decision and boundary protected
Evidence role and target applicability
Alternative rejected and causal reason
Requirements and earliest negative case
Executed or planned gate with state labeled
Residual uncertainty and accountable owner
Impact on parent modes, source order, release, and recovery
Reopen event and generic fallback
```

Do not forward an undifferentiated source dump. The receiving reference should know which question it owns and what evidence would change the parent route.

**Ordering rules**

1. Resolve accepted behavior and target identity before specialist mechanism selection.
2. Resolve framework branch before framework-specific idioms or fixtures.
3. Resolve effect, data, trust, and durability classifications before retry, transaction, background work, or infrastructure decisions.
4. Define requirements before asking testing guidance to choose evidence.
5. Resolve compatibility and runtime boundary before production rollout claims.
6. Reconcile specialist outputs in the parent route before implementation when their assumptions overlap.

Sequential routing is appropriate when one decision constrains the next, such as effect classification before retry policy or schema semantics before migration recovery. Parallel challenge is appropriate when security and operations can independently review a frozen design, provided an owner resolves conflicts before action. Parallel specialists must not independently edit the same target assumption and then merge by prose aggregation.

**Loop prevention**

- Carry one route identifier and an ordered visited-reference list.
- A repeated edge requires new target evidence, a changed governing question, or an explicit challenge purpose.
- Every handoff has an expected return or terminal owner; `read the adjacent reference` is not a return condition.
- If two references refer each other without resolving a question, stop and define the authority, outcome, or boundary they are both missing.
- Limit active companions to those that change a decision, gate, owner, or recovery path; archive orientation-only candidates from the active route.
- On conflict, compare authority and target evidence. Do not select the newest filename, longest document, or majority recommendation automatically.

**Worked transitions**

Good composition: a Ktor provider route remains one parent outcome. Framework idioms returns plugin and lifecycle questions; security/resilience returns timeout, cancellation, and retry disposition; testing returns a configured route and provider fixture; runtime returns only changed config and signals. The parent record reconciles them under one deadline and error contract.

Bad composition: a pure domain parser loads playbook, Spring/Ktor, testing, security, runtime, and reliability references. Each gives sensible general advice, but none protects a changed boundary beyond type and domain tests. Context expansion hides the accepted invariant.

Good transfer: a request described as `Kotlin` proves to be a library-level value type with no backend lifecycle. Transfer primary ownership to the language entrypoint and retain only serialization or compatibility constraints actually imposed by consumers.

Bad transfer: a database migration is sent only to runtime operations because deployment is involved. Persistence semantics, data remediation, transaction compatibility, and production-dialect evidence lose their primary owner. Split or compose playbook/persistence, testing, and runtime responsibilities instead.

Borderline route: a Ktor endpoint needs an SDK whose current cancellation behavior is disputed, and browsing remains prohibited. The local security/resilience source can frame the question; it cannot establish current SDK behavior. Keep the claim conditional, request current direct authority or a target experiment, and avoid both generic cancellation assurance and loading unrelated references.

**Verification**

- Confirm each named destination exists and its heading/evidence contract matches the forwarded question.
- Run matched classification fixtures that vary Spring/Ktor, read/write, request/durable, state/no-state, trust unchanged/changed, and runtime unchanged/changed.
- Mutate one route to a plausible wrong destination and confirm review identifies the missing authority or boundary.
- Check the route graph for cycles, terminal-less handoffs, duplicate primary owners, and specialist outputs never reconciled.
- Ask a fresh reviewer to reconstruct the accepted outcome and next action from parent plus returned packets without conversation history.
- Observe whether destination evidence changes a decision or gate; remove recurring zero-yield edges.

Promote a recurring adjacent edge into a local shortcut only after representative target cases and exceptions establish its value. Version the edge, own its fixtures, state invalidation events, and retain the generic classification route. Specialist results may improve future routing labels and examples, but should not be copied wholesale into the parent until their boundary and lifecycle genuinely become shared.

## Workload Model

Use two linked workload models:

1. **Routing-context workload** measures how much evidence, decision complexity, ownership, and verification the reference must coordinate.
2. **Target-service workload** measures the requests, jobs, data, dependencies, resources, failures, and recovery behavior that can make a backend mechanism right or wrong.

Do not substitute one for the other. A one-line code change to authorization can have a small routing surface and high consequence. A broad documentation cleanup can involve many sources and no runtime traffic. Endpoint count and total request count are weak proxies unless effects, concurrency, shared resources, distributions, environment, and accepted objectives are also known.

This reference sets no universal cap such as a fixed number of endpoints or sample requests. Target owners establish representative envelopes from observed data, accepted forecasts, risk, and platform constraints.

**Routing-context workload**

| Dimension | Narrow route signal | Expansion trigger | Appropriate response |
|---|---|---|---|
| accepted outcomes | one behavior and one rollback boundary | independently acceptable feature, migration, security, data, or rollout outcomes | split route records and reconcile interfaces explicitly |
| target surface | one bounded call path and owner | multiple services, generated code, shared libraries, or unknown entrypoints | dependency or source-graph narrowing before mechanism advice |
| framework state | one confirmed Spring or Ktor branch | explicit migration, mixed framework transition, or unknown effective version | isolate branches; add compatibility and transition evidence |
| effect and data | pure or one classified effect with no schema change | writes, unknown outcomes, transactions, concurrency, schema, cache, or durable identity | activate persistence, idempotency, migration, and production-dialect evidence as applicable |
| trust boundary | existing policy unchanged and regression-testable | identity, authorization, sensitive output, secrets, tenant scope, or abuse changes | add security ownership and deny-path evidence |
| execution model | one observed request or worker scope | blocking dependency, shared pool, fan-out, parallel children, cancellation, queue, or restart durability | trace execution and resource ownership; split durable work if needed |
| dependency failure | local deterministic call | external timeout, malformed response, retry, rate, partial failure, or unknown effect | add resilience and provider-contract evidence |
| runtime surface | no changed config, deploy, health, signal, or shutdown | startup, secret, migration, traffic, telemetry, health, shutdown, or recovery changes | compose runtime operations and production-like gates |
| source state | one clear frozen region and target confirmation | duplicate, conflict, stale version, disputed API, or missing current authority | add claim records, conflict resolution, and authorized refresh or target experiment |
| owners | one accountable decision owner | product, platform, security, data, provider, or operations decisions differ | split decisions and establish adjudication before action |
| verification | one focused target gate can falsify the behavior | infrastructure semantics, concurrency, compatibility, load, or rollout cannot be observed locally | climb the evidence ladder and retain completion limits |
| reuse | one task-local record | generated workflow, recurring route, multiple consumers, or enforced shortcut | version, validate, own, monitor, and retire the route asset |

Context expansion is not automatically the correct response. When source breadth rises, prefer sharper outcome boundaries, graph narrowing, bounded regions, specialist ownership, and evidence links. One larger undifferentiated prompt makes authority and invalidation harder to track.

**Target-service workload envelope**

| Dimension | Record | Why routing depends on it |
|---|---|---|
| operation mix | reads, writes, updates, deletes, jobs, events, and administrative paths with proportions or qualitative dominance | retry, transaction, cache, idempotency, and test choices differ by effect |
| arrival shape | steady, burst, periodic, synchronized, replayed, or externally throttled work | averages can hide queue growth, pool exhaustion, and admission behavior |
| concurrency | in-flight requests, worker parallelism, key contention, tenant skew, and shared-resource competition | determines races, isolation needs, dispatcher or executor pressure, and fairness |
| input and data shape | size distribution, key cardinality, hot keys, null or invalid frequency, historical anomalies, and growth | affects validation, query plans, memory, locking, migration, and fixture representativeness |
| dependency behavior | fan-out, latency distribution, error classes, rate limits, blocking model, connection pools, cancellation, and malformed results | controls deadline, backpressure, retry, isolation, and failure mapping |
| deadline budget | end-to-end owner objective and allocation across queues, application work, dependencies, retries, and response | a locally fast handler can still violate the total contract |
| duplicate and effect identity | client repeats, broker redelivery, timeout ambiguity, idempotency scope, retention, and reconciliation | distinguishes safe repetition from duplicated irreversible effects |
| durable backlog | enqueue rate, service rate, backlog age, lease or visibility, poison work, restart, and drain expectations | request behavior cannot prove worker capacity or recovery |
| resource bounds | effective thread, dispatcher, executor, connection, memory, CPU, file, and queue limits | syntax such as `suspend` does not establish non-blocking capacity |
| environment | hardware, JVM, runtime flags, container limits, database, broker, network, proxy, region, and dependency versions | measurements do not transfer automatically across environments |
| failure phases | normal, slow dependency, partial failure, timeout, cancellation, saturation, restart, and recovery | resilience claims require behavior during and after pressure, not only steady success |
| correctness under load | response and error contract, invariant, duplicate effect, ordering, data integrity, and recovery result | throughput without correctness is not accepted capacity |
| observability | offered and completed work, errors, timeouts, cancellations, saturation, queue age, retries, and recovery signals | unobserved overload cannot support operational conclusions |

Every numeric workload claim needs provenance: observed trace, target configuration, owner forecast, controlled generator, production sample, or explicit assumption. Record range, time window, revision, environment, exclusions, and confidence. Do not turn an owner forecast into an observed baseline or extrapolate beyond the measured envelope without labeling it.

**Evidence ladder**

| Evidence step | Useful for | Cannot establish alone |
|---|---|---|
| static call and resource trace | identifying effects, pools, fan-out, cancellation, transactions, and likely pressure points | runtime scheduling, provider behavior, actual capacity, or recovery |
| focused deterministic fixture | mechanism correctness, boundary and failure mapping, controlled concurrency | production distributions, platform contention, or external service behavior |
| production-dialect or real dependency fixture | database, broker, serialization, protocol, and lifecycle distinctions | full production topology or sustained capacity |
| synthetic target load | repeatable concurrency, burst, saturation, and regression comparison | real data skew, organic dependency correlation, or future demand |
| sanitized trace replay | observed distribution and edge-shape reproduction | behavior outside historical traces or changed downstream conditions |
| isolated staging failure test | deployment, proxy, restart, shutdown, and dependency degradation | exact production traffic and shared-resource interaction |
| shadow or staged production observation | target environment fidelity with bounded exposure | every future peak, regional failure, or untested effect |

Choose the cheapest evidence that can falsify the claim. A smoke load can prove wiring and gross failure; label it that way. It cannot prove a capacity objective without representative arrival, concurrency, data, dependencies, environment, correctness, and recovery.

**Workload evidence packet**

```text
Accepted behavior and target-owned objective
Target revision, framework, JVM, deployment, and dependency versions
Operation mix, effect classification, and duplicate identity
Arrival, concurrency, data, fan-out, and failure distributions
Effective resource, pool, queue, and deadline bounds
Fixture or generator provenance and sanitization
Warmup, duration, repetitions, and comparison baseline
Correctness, error, cancellation, saturation, and recovery assertions
Observed throughput or percentile method where applicable
Environment differences and extrapolation limit
Owner interpretation, stop signal, and reroute trigger
```

No field requires unsupported precision. Use an explicit unknown with consequence and resolution action when measurements are unavailable.

**Scenario analysis**

Good low-volume route: an external provider is slow enough to occupy a small blocking pool even though request count is modest. The model traces actual SDK behavior, executor capacity, total deadline, cancellation, and pool saturation. It does not infer safety from low volume or infer non-blocking behavior from `suspend`.

Bad load claim: a route sends a fixed number of uniform successful requests on a developer laptop and declares production scalability. Arrival distribution, concurrency, data skew, provider errors, container limits, tail method, correctness, and recovery are absent.

Good persistence route: a duplicate-write fixture concentrates concurrent attempts on the same idempotency key and verifies one accepted durable effect under the production dialect. A high volume of distinct keys would not test the race that governs correctness.

Good worker route: offered load exceeds service rate for a bounded phase, then stops. Evidence records backlog age, duplicate delivery, poison work, resource saturation, shutdown, restart, and drain. Measurement continues through recovery because a stable enqueue response can hide accumulating work.

Borderline growth case: product expects larger exports but current representative measurements remain inside the request deadline. Keep the simpler request path, add size and duration signals, define the accepted envelope and stop threshold, and reopen durable-worker routing when evidence or an accountable forecast crosses it. Do not build a queue solely because future scale is conceivable.

**Failure-focused scenarios**

- Slow one dependency while others remain healthy to observe deadline allocation and pool isolation.
- Cancel callers at different phases to observe child work, connections, transactions, and late completion.
- Repeat effectful operations after timeout to observe idempotency or reconciliation rather than only response status.
- Concentrate requests on hot keys to expose lock, cache, and partition behavior hidden by uniform input.
- Inject malformed dependency responses and partial data to verify error normalization and sensitive-output boundaries.
- Restart during accepted durable work and during migration to observe recovery ownership.
- Stop offered load after saturation and measure whether queues, pools, and health return to the accepted state.

Do not run destructive failure scenarios against shared or production systems without target authorization, isolation, recovery, and monitoring. Static models and isolated fixtures can still identify required production observations.

**Scale-triggered rerouting**

Reroute when observed or owner-accepted workload crosses a mechanism assumption: a blocking pool saturates, a request must outlive its caller, a write gains ambiguous outcomes, a data invariant becomes concurrent, a cache gains shared freshness semantics, a queue requires durable backpressure, a provider fan-out changes the deadline, or a deployment needs staged recovery. Record which modes, sources, requirements, gates, and owners activate.

Do not retain added infrastructure merely because the forecast that justified it disappeared. If measured demand, product requirements, or ownership changes remove the boundary, compare the simpler route again and plan safe retirement. Scale architecture has lifecycle cost in code, operations, incident surface, and future context.

Known workload facts are effective configuration and observations inside their recorded environment and range. Forecasts, safety margins, provider degradation, and cross-service contention remain judgment or uncertainty. Treat the workload model as a versioned hypothesis; make its invalidation signals observable and rerun the route when those signals move.

## Reliability Target

The reliability promise of this reference is **bounded evidence routing**. Given an accepted outcome and available target evidence, it should select a proportionate source and verification route, preserve authority boundaries, stop before unsupported consequential action, make failures diagnosable, and leave a recoverable handoff.

It does not guarantee that target code is correct, a provider is available, a migration succeeds, or a service meets an objective. Those outcomes belong to target implementation, infrastructure, and accountable owners. The router's responsibility is to activate and trace the evidence needed for those claims without inventing it.

**Reliability properties**

| Property | Required behavior | Failure example | Recovery behavior |
|---|---|---|---|
| evidence integrity | historical local, current external, target observation, owner policy, synthesis, plan, executed result, and forecast remain distinguishable | a suggested Gradle command is reported as passed | retract the result, identify affected decisions, execute a discovered gate or downgrade completion |
| target fidelity | concrete guidance follows the inspected framework, versions, call path, conventions, and environment | Spring mechanism is routed into an existing Ktor service | stop implementation, restore target facts, reroute framework guidance, and retest affected work |
| scope containment | one accepted outcome and its changed boundaries control source and mode expansion | pure parser work gains database, telemetry, and deployment changes | remove unearned modes and preserve only evidence that changes a requirement or gate |
| decision traceability | consequential choices retain alternatives, causal reason, assumptions, owner, gate, and reversal signal | retry is added because it is generally resilient | classify failure and effects, compare no-retry, obtain owner policy, and reopen the route |
| safe uncertainty | missing evidence produces an explicit conditional, orientation-only, blocked, or escalation result | unknown provider effect is treated as safe read | prohibit repetition, name consequence and owner, and request contract or target experiment |
| falsifiable verification | required gates can fail under relevant defects and match the mechanism claimed | mock repository is used to prove database uniqueness | add production-dialect and concurrency evidence or narrow the claim to orchestration |
| truthful completion | orientation, plan, running work, result, and release evidence are never collapsed | implementation-ready plan is labeled production-safe | downgrade state and enumerate missing runtime, owner, or rollout evidence |
| bounded failure | wrong routes are detected before irreversible or trust-sensitive action where controls can reasonably do so | schema cleanup policy is guessed and migration runs | stop before mutation; restore or forward-recover under data owner authority if escape occurs |
| resumable recovery | persisted artifacts identify the earliest broken decision, affected evidence, next action, and safe fallback | a new agent repeats the same source mistake after handoff | invalidate the stale claim, preserve valid work, and resume from the recorded blocker |
| lifecycle response | source, target, requirement, policy, owner, or environment changes reopen affected route decisions | promoted local shortcut silently survives framework upgrade | demote shortcut, use generic fallback, rerun fixtures, and version any successor |

**Hard integrity invariants**

The following are completion gates rather than statistically budgeted conveniences:

- No executed command, test result, benchmark, target path, target version, owner decision, or production observation may be fabricated or inferred from an example.
- No historical local claim may be presented as current public or target authority without the evidence transition being explicit.
- No known incompatible Spring and Ktor implementation branches may be merged unless framework migration is the accepted outcome with transition evidence.
- No unauthorized irreversible data, security, or production action may proceed through an unresolved consequential assumption.
- Every blocked, avoided, or failed consequential route must preserve an actionable recovery, escalation, or adjacent-reference path.
- Every promoted shared shortcut must have an owner, scope, invalidation event, generic fallback, and review mechanism.

These are intended zero-tolerance properties, but `zero observed violations` is not proof that no latent violation exists. Each invariant needs detection: schema and marker checks, source and target locators, reviewer sampling, controlled mutations, retained execution evidence, and incident feedback. Report detection gaps alongside observed compliance.

**Calibrated routing indicators**

| Indicator | Event definition | Local target-setting question | Guard signal |
|---|---|---|---|
| correct action | reviewer- and evidence-supported route selects the appropriate primary mode, companions, source regions, and next gate | what rate is acceptable for this consequence class and cohort? | unsupported claim and downstream defect escapes |
| correct abstention | route stops or remains conditional because a consequential missing fact cannot be safely inferred | are legitimate stops recognized rather than scored as non-completion? | false-stop rate and resolution time |
| false action | route recommends concrete consequential action that available evidence contradicts or cannot support | which false actions are never budgetable, and which are recoverable? | severity, detection stage, and rollback outcome |
| false stop | route blocks despite sufficient available evidence and no owner or safety reason | how much delay is acceptable before process improvement is required? | consequence class and missed discovery step |
| material correction | reviewer changes framework, source role, boundary, mechanism, gate, or authority rather than wording | what baseline exists for comparable route levels? | corrections caused by new scope rather than avoidable routing error |
| detection coverage | seeded or known routing defects detected by the applicable controls | which defect classes are represented and who maintains them? | fixture realism and undetectable classes |
| containment stage | wrong route detected at intake, planning, implementation, review, release, or production | how early must each severity class be contained? | false confidence from many trivial early catches |
| recovery success | affected action is stopped, valid evidence preserved, wrong claim corrected, and next safe route resumed | what recovery evidence is required by consequence? | lingering stale artifacts or repeated defect |
| invalidation response | stale route recognized and demoted after its source or target trigger | how quickly must shared consumers be protected? | false churn from irrelevant changes |

Set numerical objectives only after defining eligible population, target access, completion level, consequence class, sample period, adjudication, and data quality. The archive seed's `18 of 20` has no such basis and is not retained as a target. Rare high-consequence work should use stronger per-case assurance rather than a percentage built from a tiny denominator.

**Consequence classes**

| Class | Example route effect | Assurance posture |
|---|---|---|
| informational | orientation or explanation with no target action | clear evidence boundary and useful next route |
| reversible local | isolated pure logic or configuration plan with easy rollback | focused target evidence and negative case |
| shared implementation | public API, framework wiring, reusable library, or cross-module contract | independent review, compatibility, and broader gates |
| effect or data | writes, transactions, duplicate handling, migration, durable work, or provider side effects | production-like semantics, concurrency or recovery evidence, accountable owner |
| trust | authorization, sensitive output, secrets, tenant boundary, or abuse behavior | deny-path evidence, security authority, no unsupported action |
| production control | traffic, deploy, health, shutdown, migration execution, or incident recovery | operations ownership, staged evidence, stop and recovery authority |

A failure's severity and reversibility matter more than raw count. Do not average an unauthorized destructive migration with a harmless extra source read.

**Degraded modes**

| Evidence condition | Reliable degraded response | Unsafe response |
|---|---|---|
| target unavailable | provide orientation, candidate modes, exact target evidence request, and prohibited concrete claims | invent common paths, versions, and commands |
| public currentness unavailable | retain dated local claim as historical or conditional and request direct authority or target experiment | call the frozen summary current documentation |
| owner decision missing | state consequence, safe interim behavior, owner, and stop or escalation condition | choose product, data, security, or rollout policy by convention |
| target gate unavailable | identify the closest credible evidence and narrow completion or claim | report a generic command as passed or substitute unrelated green tests |
| conflicting evidence | preserve both claims with authority, target fit, and resolution path | average recommendations or choose the newest-looking source |
| specialist unavailable | use bounded frozen region and generic route with confidence limits | imply the absent adjacent reference approved the decision |

Safe abstention is a successful reliability outcome when action would exceed evidence or authority. It becomes a false stop when the needed fact was available, consequence did not justify blocking, and the route failed to inspect or use it. Track both so conservatism does not become unexamined delay.

**Reliability evidence plan**

| Assurance goal | Verification method | Limitation |
|---|---|---|
| prevent malformed records | schema, exact heading, packet, uniqueness, unresolved-marker, ASCII, whitespace, table, and fence validation | cannot establish semantic route fit |
| detect authority collapse | source-role audit and mutation from historical fact or plan into target result | reviewers may share the same source bias |
| detect wrong surface | matched Spring, Ktor, pure Kotlin, persistence, worker, and unknown-target fixtures | fixture set may become predictable or stale |
| test safe uncertainty | remove framework, effect, owner, or current-authority evidence and inspect degraded response | synthetic absence may not reproduce real organizational pressure |
| test falsifiability | inject a relevant controlled defect or retain pre-fix failure evidence | unsafe or expensive against shared systems; isolate appropriately |
| test handoff recovery | resume from a persisted conditional or partially wrong route with fresh context | does not prove production rollback |
| observe real quality | sample comparable route records, corrections, results, and downstream defects | attribution remains shared with implementation and review |
| learn from escapes | reconstruct earliest broken route link after incident or defect | incident records can omit near misses and undetected failures |

Rotate fixtures and score the evidence requests and causal rationale, not exact prose. Include exception cases in which the expected route should remain unchanged so a new guard does not simply block everything.

**Worked reliability judgments**

Correct action: target inspection confirms Ktor, the route selects Ktor plus cancellation and provider-failure guidance, and a configured target fixture supports the reported application behavior. Production proxy behavior remains explicitly outside the claim.

Correct abstention: the target framework is unavailable and the user requests concrete wiring. The router stays orientation-only, names Spring and Ktor as exclusive candidate branches, requests the build and module evidence, and does not fabricate code.

False action: a frozen source describes bounded retry for transient reads, but provider effect status is unknown. The route adds retry anyway. This violates safe uncertainty even if no duplicate effect is observed in a small test.

False stop: the target build, configured Ktor module, existing route, and fixtures are available, but the router refuses to classify the framework because it never inspects them. The issue is failed discovery, not prudent uncertainty.

Borderline calibration: target tests prove cancellation reaches an application adapter, while a production proxy may buffer disconnects. Accept reliability for the application boundary, retain a deployment conditional, and block broader end-to-end cancellation language until platform evidence exists.

**Recovery protocol**

1. Stop the unsupported action and preserve current artifacts, target revision, and observed results.
2. Identify the earliest broken link: outcome, target fact, mode, source role, mechanism, requirement, gate, result label, release, or lifecycle.
3. Determine which downstream decisions and artifacts depend on that link; invalidate selectively.
4. Restore the last evidence-supported completion level and route.
5. Obtain missing authority or run the smallest credible target gate.
6. Correct implementation, plan, or handoff under the proper owner; use rollback or forward recovery according to target policy.
7. Add or revise a decision fixture, validator, source role, example, or adjacent edge if the failure can recur.
8. Recheck both the corrected case and an exception that should remain valid.

Reliability reporting must state observed events, reviewer judgments, inferred contribution, sample limits, detection gaps, and unresolved risk. A disagreement adjudicated by the correct owner is a successful control even when the initial route changes.

The router's reliability ceiling is determined by accessible target evidence, current authority, representative gates, and governance. More fluent guidance cannot compensate for missing policy or observation. Its strongest behavior under degraded evidence is therefore bounded honesty: narrow the claim, preserve reversibility, and make the path to stronger evidence explicit.

## Failure Mode Table

Select failure modes from the accepted outcome, changed boundaries, workload, source route, and target history. Do not apply every mitigation in this catalog. A control earns its place when a concrete failure can reach the target boundary, the control interrupts that causal path, an owner accepts its cost, and a representative observation can challenge it.

**Routing and evidence failures**

| Failure mode | Causal trigger and vulnerable boundary | Earliest useful signal | Containment and recovery | Evidence and owner |
|---|---|---|---|---|
| wrong governing outcome | implementation tasks begin before user-visible success, failure, and recovery are accepted | route record contains several independent verbs or no observable result | stop, split outcomes, restore owner decisions, and invalidate dependent routes | intake review and product or operator owner |
| target access treated as optional | generic source advice is made concrete before repository instructions, framework, build, or call path are inspected | concrete path, version, or command lacks target locator | downgrade to orientation, inspect target, and reroute affected decisions | target preflight and implementation owner |
| wrong framework branch | Spring and Ktor keywords or examples are selected without effective target evidence | source route disagrees with build, module, plugins, or configured test host | stop edits, preserve target facts, choose one branch, and retest | framework fixture and service owner |
| hidden framework migration | feature work introduces a new framework or major mechanism without accepted transition scope | new dependency or module appears outside non-goals | separate migration outcome, compatibility, rollout, and rollback | dependency diff, architecture owner, and release owner |
| whole-file authority collapse | a navigation or historical source is labeled canonical for implementation, target, and currentness | claim lacks role, target question, or disposition | reclassify claim-level authority and retract unsupported conclusions | source audit and reference owner |
| stale public mechanism | dated summary is used for version- or security-sensitive behavior | source date predates target version or currentness is absent | retrieve direct current authority when allowed or keep claim conditional and test target | source owner, framework owner, or security owner |
| conflicting evidence averaged | incompatible policies, versions, or observed results are blended into one recommendation | route record contains mutually exclusive assumptions | identify conflict type and authority; stop consequential action until resolved | decision ledger and accountable adjudicator |
| adjacent routing loop | references forward the task without changing the governing question or returning evidence | repeated route identifier and edge with no new target fact | stop, define primary owner, question, expected return, and terminal escalation | route graph check and reference owner |
| context overexpansion | every mode and source is loaded to avoid omission | sources have no decision, gate, owner, or recovery yield | remove zero-yield context, narrow outcome, and use specialist links | source-yield review and route owner |
| premature local shortcut | recurring route is promoted before representative exceptions or invalidation are known | shared template has no version, fixtures, fallback, or owner | demote to generic route, preserve consumers, and add bounded evidence | shortcut registry and owning team |

**Mechanism and target failures**

| Failure mode | Causal trigger and vulnerable boundary | Earliest useful signal | Containment and recovery | Evidence and owner |
|---|---|---|---|---|
| fake non-blocking path | blocking SDK or database call is wrapped in suspend syntax on an event loop | call trace shows blocking operation without intentional isolation | use established blocking model or isolate with bounded executor and capacity evidence | call trace, saturation fixture, and runtime owner |
| cancellation stops at API surface | request cancellation is not propagated to child work, client, transaction, or resource | controlled cancellation leaves active work or late completion | wire structured scope and cleanup, or move deliberately durable work to another owner | cancellation fixture and service owner |
| untracked background work | route launches work that must outlive caller without durable ownership | process restart loses accepted work or shutdown abandons it | split durable outcome, persist identity and state, and define restart recovery | restart scenario and worker owner |
| retry amplifies failure | retries ignore total deadline, effect safety, provider rate, or saturation | attempt count and in-flight work rise while success does not | stop retries, classify failure and effect, apply bounded policy or reconciliation | failure injection, provider owner, and resilience owner |
| unknown outcome duplicates effect | timeout occurs after an effect may have committed and caller repeats | same business identity produces multiple durable effects | use idempotency key, query or reconcile outcome, and repair duplicates under owner policy | duplicate fixture and domain or data owner |
| transaction boundary mismatch | remote call, validation, or dependent write occurs outside intended atomic boundary | partial state persists under injected failure or concurrency | redesign transaction and integration boundary; compensate or reconcile existing state | production-dialect test and data owner |
| check-then-act race | application pre-check and write are not atomically enforced | concurrent same-key operations both pass precondition | enforce invariant at authoritative store and map conflicts consistently | concurrent real-store fixture and persistence owner |
| migration assumes clean data | new constraint or type ignores historical anomalies | preflight profile finds violating rows or rehearsal fails | stop rollout, define deterministic remediation and forward or rollback plan | data profile, rehearsal, and data owner |
| sensitive data escapes | errors, logs, metrics, traces, or responses include secrets or private payload | controlled failure emits disallowed field | redact or restructure output, rotate exposed secret if needed, and audit sinks | security test and security owner |
| authorization drifts by entry path | policy is enforced only in one controller or route and bypassed elsewhere | alternate entry path permits denied operation | centralize policy at correct boundary and exercise allowed and denied paths | abuse-case fixture and policy owner |

**Verification, release, and lifecycle failures**

| Failure mode | Causal trigger and vulnerable boundary | Earliest useful signal | Containment and recovery | Evidence and owner |
|---|---|---|---|---|
| mock-only infrastructure proof | fake repository, broker, client, or scheduler is used to claim real semantics | claimed behavior depends on dialect, protocol, lifecycle, or timing absent from fake | narrow claim or add representative real dependency evidence | test-plan review and test owner |
| green gate cannot falsify claim | broad or shallow test passes even when relevant behavior is broken | controlled mutation survives required gate | replace or supplement gate with boundary-specific observation | negative control and test owner |
| planned result reported as executed | suggested command, benchmark, or review is phrased as passed | no retained command, revision, environment, or output | retract completion, execute discovered gate, and reassess dependent decisions | evidence audit and handoff owner |
| workload sample hides pressure | uniform successful requests omit burst, skew, slow dependency, cancellation, or recovery | averages look stable while pool, queue, or tails degrade | revise envelope and run representative steady, failure, and recovery phases | workload packet and performance owner |
| retry or queue hides overload | admission continues after capacity is exhausted and backlog or attempts accumulate | queue age, saturation, timeouts, or attempt amplification rise | apply owner-approved backpressure, shed or defer work, and recover backlog deliberately | load and recovery test plus operations owner |
| health signal causes harm | readiness, liveness, or dependency policy triggers restart or traffic loops | healthy process churns or unavailable dependency removes all capacity | separate health semantics, stop automation, and restore stable traffic policy | platform scenario and operations owner |
| mixed-version incompatibility | rollout changes API, event, schema, config, or job contract without coexistence plan | canary or compatibility fixture fails across versions | halt rollout, rollback or forward-fix under compatibility plan | mixed-version gate and release owner |
| shutdown loses or duplicates work | process stops without bounded drain, lease, commit, or cancellation semantics | restart reveals missing or repeated accepted work | restore work identity, reconcile effects, and fix lifecycle ownership | shutdown/restart drill and worker owner |
| observability cannot drive action | signals lack route identity, outcome, owner, bounds, or recovery context | alert cannot distinguish dependency, cancellation, saturation, or defect | improve bounded signals and runbook; avoid high-cardinality payload logging | signal review and operations owner |
| source or target drift stays hidden | framework, provider, schema, policy, or environment changes without invalidating route | promoted shortcut and target facts disagree | demote stale route, use generic fallback, rerun affected fixtures, and version successor | invalidation monitor and shortcut owner |
| handoff loses uncertainty | conditional claim becomes definite after context transfer | next agent cannot find blocker, owner, or evidence state | restore persisted route record, downgrade completion, and request missing authority | fresh-context replay and handoff owner |
| incident fixes symptom only | runtime patch leaves wrong source role or route rule unchanged | same failure recurs in another target or generated plan | trace earliest route link, add fixture or guard, and verify exceptions | incident review and reference owner |

**Failure record schema**

```text
Failure identifier and activated target boundary
Accepted behavior placed at risk
Causal trigger, preconditions, and common cause
Earliest route-stage and runtime-stage detection signal
Severity, reversibility, and affected owners or consumers
Prevention control and its own cost or failure modes
Containment action and prohibited continuation
Rollback, forward recovery, reconciliation, or escalation
Representative verification and last observed result
Residual risk, confidence basis, and reopen trigger
Incident, fixture, source, target, and decision lineage
```

Do not assign numerical likelihood or risk scores unless the organization has a calibrated method and sufficient data. Ordinal priority can be justified by consequence, irreversibility, recurrence, exposure, detectability, and recovery cost. Low-frequency security, data-loss, or unauthorized production hazards may require strong prevention even when rate estimation is weak.

**Selection and prioritization**

1. Trace the accepted outcome through target call path, effects, data, trust, dependencies, resources, deployment, and recovery.
2. Select failures that can violate a named requirement or make required evidence misleading.
3. Identify common causes such as stale target revision, shared pool, provider outage, clock or identity mismatch, migration order, or missing owner policy.
4. Prefer controls at the earliest reliable boundary while retaining runtime detection for escapes.
5. Evaluate the control's cost and new failure surface: retries add load, queues add durability and duplication, caches add freshness, health automation can add churn.
6. Bind the chosen control to a representative negative scenario and a recovery observation.
7. Route unresolved risk to the owner with authority to accept, change, or stop it.

**Correlated failures**

Independent rows are insufficient when failures share resources or timing. Analyze at least these combinations when activated:

- Slow provider plus retry policy plus shared client pool can amplify saturation and consume the total deadline.
- Request cancellation plus late database commit plus client retry can create an unknown-outcome duplicate effect.
- Schema migration plus mixed application versions plus health automation can turn compatibility failure into restart and traffic churn.
- Stale framework guidance plus generic green tests can allow wrong wiring to pass review and reach rollout.
- Missing route identity plus high-cardinality telemetry can increase cost while making the incident harder to correlate.
- Backlog growth plus shutdown plus broker redelivery can duplicate durable work during recovery.

Use a causal tree, timeline, or isolated scenario when ordering matters. Record which assumption or resource links the rows and which control could fail in common.

**Worked failure chain: unsafe retry**

```text
Accepted behavior: one durable provider-side order per business request.
Trigger: client deadline expires after provider may have accepted the order.
Route defect: operation was called transient without effect and unknown-outcome analysis.
Amplifier: generic retry repeats immediately within the same total deadline.
Consequence: duplicate provider orders and additional pressure during degradation.
Early signal: no idempotency identity or reconciliation path in the route record.
Containment: stop automatic repetition on unknown outcome.
Recovery: query or reconcile provider state under domain ownership; repair duplicates by policy.
Prevention: provider-supported idempotency or an explicit durable effect protocol.
Verification: controlled delayed response with stable business identity and duplicate observation.
Residual uncertainty: real provider commit and timeout timing until direct contract or staged evidence exists.
```

Good response: the route blocks retry before implementation, obtains provider semantics, and tests one business effect under timeout ambiguity.

Bad response: add exponential backoff and call the route resilient. Backoff may reduce frequency while retaining duplicate effects and deadline amplification.

Borderline response: provider documentation claims idempotency but target SDK forwarding and retention behavior are unverified. Keep the control conditional, inspect outgoing requests, test the target adapter, and retain reconciliation for uncertain outcomes.

**Control verification**

- Use static mutation for wrong authority, framework branch, completion label, or route edge.
- Use focused deterministic fixtures for validation, error mapping, cancellation, duplicate identity, and service orchestration.
- Use production-dialect or real dependency fixtures for constraint, protocol, broker, client, scheduler, and lifecycle claims.
- Use isolated load and failure scenarios for saturation, backpressure, timeout, retry, and recovery.
- Use tabletop or staged rollout drills for data remediation, mixed versions, traffic, incident authority, and destructive recovery.
- Continue observation after the trigger ends to verify pools, queues, health, data, and durable work return to an accepted state.

Never run destructive failure injection against shared or production systems without authorization, isolation, monitoring, and recovery. When direct exercise is unsafe, document the residual and use the strongest safe evidence available.

An incident review should preserve route lineage. Ask which intake, target fact, source role, mechanism, requirement, gate, result label, release decision, or lifecycle trigger first failed. Update the smallest recurring control and test both the incident case and an exception. A runtime patch without route learning leaves generated plans and future targets exposed to the same failure.

## Retry Backpressure Guidance

Classify the retry plane before choosing policy. A backend request, durable worker delivery, deployment action, test rerun, source refresh, and agent generation loop do not share the same effects or owners. They do share one warning: repetition without changed conditions, effect safety, remaining budget, available capacity, and observable progress is amplification rather than recovery.

The default is **no automatic retry until justified**. A retry decision must establish:

1. the exact failed operation and business or workflow effect;
2. transient, permanent, overloaded, cancelled, unknown-outcome, stale-evidence, missing-authority, or deterministic-defect classification;
3. the identity that makes repeated effects safe or reconcilable;
4. the total deadline, attempt budget, queue or concurrency bound, and cancellation owner;
5. why another attempt can see a changed condition or new evidence;
6. the terminal behavior after exhaustion;
7. the signal that stops admission before recovery capacity is lost.

**Failure classification**

| Failure class | Default retry disposition | Required evidence before exception | Terminal or reopen behavior |
|---|---|---|---|
| invalid input or domain rejection | do not retry unchanged request | corrected input or changed domain state | return stable rejection; new input is a new operation |
| authentication or authorization denial | do not retry unchanged credentials or principal | confirmed credential refresh or policy-state transition | deny safely and escalate policy questions to owner |
| unsupported schema, version, or protocol | do not retry identical mechanism | compatibility change, negotiation, or corrected payload | fail with actionable incompatibility evidence |
| deterministic code or test defect | do not hide with reruns | code, fixture, dependency, or environment change tied to diagnosis | preserve original failure and rerun as a new verification event |
| cancellation | do not restart implicitly | separate accepted durable outcome and owner | terminate scoped work and release resources |
| deadline exhausted | do not reset budget at an inner layer | new user operation or owner-approved asynchronous continuation | return timeout or accepted durable status according to contract |
| overload or saturation | suppress retries and apply admission control | measured recovered capacity and coordinated policy | shed, defer, degrade, or fail according to owner semantics |
| transient read-like dependency error | bounded retry may apply | provider classification, total budget, rate policy, capacity, and low effect risk | return normalized failure or accepted fallback after exhaustion |
| optimistic concurrency conflict | bounded reread and retry may apply | operation recomputes from fresh state and preserves invariant | surface conflict when progress or budget ends |
| unknown effect outcome | do not repeat blindly | idempotency identity, provider outcome query, or reconciliation protocol | reconcile first; repair duplicates under domain policy |
| stale source evidence | refresh may apply when authorized | current direct authority exists and could change the decision | retain dated boundary or escalate if refresh is unavailable |
| missing target context | inspect available target once; not a blind generation retry | concrete repository artifact or owner answer becomes available | remain orientation-only and request the missing fact |
| true evidence contradiction | do not select by repetition | authority adjudication, target experiment, or owner decision | preserve conflict and stop consequential action |

HTTP method, function name, coroutine syntax, or exception class is not enough to classify effects. A read can consume quota, create audit records, or return an inconsistent snapshot. A nominally idempotent write can have retention limits or key-scope errors. Inspect target and provider semantics.

**Retry planes**

| Plane | Identity and budget | Backpressure signal | Required recovery evidence |
|---|---|---|---|
| request and dependency | business operation, caller deadline, nested attempt tree, client pool | in-flight work, pool saturation, timeouts, cancellations, provider rate response | terminal error or fallback, resource release, no unintended effect |
| persistence and transaction | domain identity, transaction attempt, lock or conflict budget | contention, deadlock, queueing, connection saturation | invariant preserved, conflict mapped, transaction outcome known or reconciled |
| durable worker or broker | work identifier, delivery attempt, lease or visibility, retry schedule | backlog age, poison work, worker saturation, redelivery amplification | one accepted effect, dead-letter or escalation policy, restart and drain |
| deployment or migration | release identifier, stage, compatibility window, rollback or forward budget | failing canary, health or data signal, recovery capacity | traffic stabilized, schema or version state reconciled, owner-authorized continuation |
| test and CI | target revision, test invocation, environment, deterministic or flaky classification | repeated identical failure, queue usage, hidden pass-after-retry | root cause or explicit flake evidence; original failures retained |
| source refresh | claim identifier, frozen source, current-authority request | repeated retrieval with no authority or changed content | disposition changes or dated uncertainty remains explicit |
| agent generation | route and section identifier, source hashes, user revision, write ownership | red gate, duplicate rationale, stale target, shared-file conflict, no progress | checkpoint, narrow context, preserve user work, correct one bounded unit |

**Backpressure choices**

| Choice | Appropriate when | Cost and new obligation |
|---|---|---|
| fail fast | failure is permanent, invalid, unauthorized, deterministic, or unsafe to repeat | callers need stable error and recovery guidance |
| admission limit | work can be rejected before consuming saturated resources | fairness, overload response, and client behavior need ownership |
| bounded queue | delayed work is accepted and capacity can recover within an owned envelope | durability, queue age, memory or storage, shutdown, and poison handling become required |
| load shed | preserving core or existing work is more valuable than accepting all new work | product prioritization and explicit rejection semantics are required |
| stale or degraded response | product accepts reduced freshness or completeness | freshness, privacy, provenance, and recovery to normal must be defined |
| circuit state | repeated dependency calls should pause during known failure | state transitions, probe behavior, distributed coordination, and observability add complexity |
| manual escalation | consequence or uncertainty exceeds automatic policy | owner availability and actionable evidence become part of reliability |
| reconcile | operation may have succeeded but response is unknown | stable identity, outcome query, repair authority, and audit trail are required |
| narrow agent work | source or validation pressure makes continued broad generation unsafe | checkpoint and resumed context must preserve decisions and exact boundaries |

Backpressure is not simply `slow down`. It allocates delay, failure, degraded service, or manual work among users, tenants, dependencies, reviewers, and operators. Product and operations owners must accept those semantics.

**Attempt budget and amplification audit**

Trace the complete attempt tree. A route handler with two attempts, an SDK with three internal attempts, a proxy replay, and a worker redelivery can multiply work even when each local setting appears bounded. Record:

```text
Original operation and stable effect identity
Every layer capable of repeating or redelivering
Maximum concurrent and sequential attempts per layer
Total deadline and whether inner layers can reset it
Delay, jitter, coordination, and rate-policy behavior
Shared pool, queue, connection, and dependency pressure
Cancellation propagation and resource cleanup
Terminal result, fallback, reconciliation, and owner
```

Do not infer acceptable amplification from attempt count alone. Concurrency, fan-out, payload cost, key contention, and queued age determine pressure.

**Backend examples**

Good bounded read retry: a target adapter classifies a documented transient provider error, the operation has no unowned side effect, one total request deadline bounds all attempts, jitter avoids synchronization, client pool capacity remains available, cancellation stops further work, and exhaustion returns the service-owned error. The route records provider and target evidence; it does not prescribe a universal count.

Bad write retry: a provider order times out after an unknown commit, and the client repeats without an idempotency key or outcome query. Backoff changes timing but not duplicate-effect safety. Stop repetition and reconcile provider state.

Borderline read: the provider call is semantically read-only but billed and rate-limited. A bounded retry may be correct, but product cost and provider policy are part of the decision. `GET` alone does not authorize it.

Good optimistic concurrency retry: the application rereads current state, recomputes the decision, and retries a bounded compare-and-set while the invariant and total budget remain valid. Replaying the stale write unchanged is not equivalent.

Bad worker policy: poison work is retried indefinitely, keeping queue age and cost high while no input or dependency condition changes. Bound attempts, preserve diagnostics, route to a target-owned terminal state, and prove normal work continues fairly.

**Agent and verification examples**

Good source refresh: a claim is version-sensitive, browsing or direct retrieval is authorized, and a current primary source can resolve a material conflict. The refreshed authority changes or confirms a disposition, the target gate reruns, and source date plus result are persisted.

Bad refresh loop: current authority is unavailable, but the agent repeats search or generation with identical inputs and then treats repeated wording as confidence. Stop, retain dated evidence, narrow the claim, and request authority.

Good test rerun: diagnosis changes code, fixture, dependency state, or controlled timing; the original failure remains visible; the rerun is a new evidence event. Bad test rerun: CI repeats until green and reports only the passing attempt, hiding deterministic or flaky behavior.

Good section workflow: after each packet section and reference section, run a bounded sanity check. On failure, preserve durable work, correct that section, and rerun the specific gate before proceeding. Stop broader generation when headings, uniqueness, expansion, ownership, or source identity is red.

Bad shared-workspace retry: an agent sees a write conflict, re-applies a broad patch from stale context, and overwrites user or peer changes. Re-read the exact owned file, preserve unrelated edits, narrow the patch, and escalate only if exclusive ownership is contradicted.

**Verification matrix**

| Scenario | Inject or vary | Required observation |
|---|---|---|
| transient then success | controlled dependency fails transiently before success | attempts remain within total budget, use stable identity, and stop after success |
| permanent failure | validation, authorization, or protocol error | no unchanged automatic retry; stable terminal response |
| unknown effect | delay response after possible commit | no blind repeat; outcome query or reconciliation path activates |
| overload | slow dependency or saturated pool while arrivals continue | retries suppress, admission policy activates, and existing work can recover |
| synchronized clients | many callers receive the same transient signal | attempts do not form an unbounded synchronized wave |
| cancellation | cancel before and between attempts | timers, child work, connections, and further attempts terminate as required |
| poison work | deterministic worker failure across deliveries | bounded terminal handling, diagnostics, and fairness for other work |
| nested policy | enable retries in multiple layers | observed attempt tree matches accepted global budget |
| no-progress source refresh | retrieval returns no new authority or target fact | workflow stops and retains explicit uncertainty |
| red generation gate | introduce duplicate packet value or wrong heading | agent halts next section, repairs only owned artifact, and rechecks |
| recovery | remove pressure or restore dependency | pools, queues, backlog, health, and route state return to accepted bounds |

Use isolated adapters, production-like infrastructure, or staged environments according to the claim and consequence. Never inject destructive retries or migrations into shared or production systems without authorization and recovery.

**Observability and stop conditions**

Record original operations separately from attempts. Observe terminal outcomes, retries by class, elapsed budget, queue age, in-flight work, pool and connection saturation, cancellation, duplicate identities, reconciliation, and recovery. Avoid raw credentials, private payloads, and unbounded labels.

Stop automatic repetition when any of these occurs:

- failure is reclassified as permanent, unauthorized, deterministic, or unknown-effect without reconciliation;
- total deadline or attempt budget is exhausted;
- cancellation or caller abandonment governs the work;
- saturation, backlog age, provider rate response, or recovery capacity crosses owner policy;
- repeated attempts produce no new evidence or progress;
- target revision, source authority, or shared workspace state changes beneath the attempt;
- a required owner decision or destructive-action authorization is absent.

A materially changed input, authority, target revision, dependency state, or owner decision can justify a new operation. Preserve lineage so it is not reported as uninterrupted retry success.

Retries alter workload, tails, cancellation, costs, and recovery. Queues alter durability and duplication. Fallbacks alter semantics and freshness. Therefore every added retry or backpressure mechanism must reroute affected Testing, Resilience, Persistence, Security, or Operations evidence. Keep the original failure observable so the control does not improve apparent availability by hiding a growing defect.

## Observability Checklist

Observe two planes and connect them by route identity:

- **Route plane:** which outcome, target revision, modes, sources, decisions, gates, results, corrections, unknowns, owners, and invalidation events shaped the work.
- **Service plane:** what requests, jobs, effects, errors, dependencies, resources, data, security outcomes, deployment states, and recovery behavior occurred.

The route plane explains what should have been true and why. The service plane observes what happened. Neither replaces the other. A green dashboard does not prove the source route was valid, and a perfect route record does not prove runtime behavior.

Add or change telemetry only when a changed boundary creates a consequential blind spot. Existing platform signals should be reused when they answer the question with correct semantics. This reference does not mandate p50, p95, p99, or any vendor field by default; percentiles require a target-owned objective, representative workload, distribution method, and error context.

**Signal design record**

| Field | Required question |
|---|---|
| accepted decision | What behavior, failure, or recovery decision will this signal support? |
| source requirement | Which route decision or stable requirement gives the signal meaning? |
| event unit | Is this an original operation, attempt, durable work item, effect, deployment, route, review, or recovery? |
| outcome vocabulary | Which bounded normal, failure, cancellation, duplicate, degraded, blocked, and recovered states exist? |
| correlation | Which request, business effect, work, trace, route, target revision, or release identity joins evidence? |
| dimensions | Which labels are bounded, necessary, non-sensitive, and stable enough to query? |
| measure | Is the value a count, duration, size, age, saturation, state transition, or retained artifact? |
| freshness | How is missing, delayed, duplicated, sampled, or stale telemetry detected? |
| owner and action | Who reads it, under what condition, and what can they safely do? |
| privacy and retention | What data is prohibited, redacted, sampled, access-controlled, or expired? |
| verification | Which scenario emits it, which query finds it, and which controlled absence must remain absent? |
| lifecycle | Which schema, owner, target, or policy change invalidates or retires it? |

**Route-plane checklist**

- [ ] A stable route identifier links the accepted outcome, packet, reference, target revision, and handoff.
- [ ] Source paths, bounded regions, hashes, dispositions, and intentionally skipped candidates are retained without copying raw source dumps.
- [ ] Target facts have exact locators and observations; missing target evidence is a visible state.
- [ ] Primary and companion modes record the changed boundary each protects.
- [ ] Consequential decisions retain rejected baseline, causal reason, owner, gate, and reversal signal.
- [ ] Requirements and negative cases link to planned and executed verification states.
- [ ] Exact commands, revisions, environments, statuses, concise outputs, and limitations support reported results.
- [ ] Material reviewer corrections distinguish source, target, boundary, mechanism, gate, result-label, and lifecycle defects.
- [ ] Conditional and blocked items retain consequence, owner, resolution, and prohibited action.
- [ ] Invalidation events show which promoted shortcuts and downstream claims became stale.
- [ ] Resume evidence is small enough for a fresh reviewer to identify next action and stop condition without transcript replay.

Do not log hidden reasoning or raw conversations as the required evidence. Persist explicit high-level decision rationale, source and target facts, tests, results, limitations, and ownership.

**Service-plane checklist**

Activate only rows connected to the changed outcome.

| Boundary | Minimal useful observations | Decision or recovery question |
|---|---|---|
| request or route | original operations, accepted outcome class, terminal status, duration if owned, cancellation, and stable correlation | is the public contract succeeding or failing within its accepted boundary? |
| dependency | dependency identity, attempt versus original operation, error class, timeout, deadline consumption, pool pressure, cancellation, and terminal mapping | is failure local, dependent, amplified, or unrecovered? |
| coroutine or blocking | dispatcher or executor use, active work, queueing, saturation, cancellation, and late completion | is execution behaving as designed under representative concurrency? |
| persistence | operation class, constraint or conflict, transaction outcome, lock or pool pressure, duplicate identity, and migration revision | are invariants and effects preserved, including uncertain outcomes? |
| durable worker | accepted work, delivery attempt, backlog age, lease or visibility, poison state, completion, duplicate effect, restart, and drain | is durable work progressing fairly and recoverably? |
| security | allowed and denied outcome classes, policy revision, abuse-control state, and redacted failure category | is policy enforced without leaking principal, secret, or sensitive payload? |
| retry and backpressure | original operations, attempts, total budget, suppression, shedding or defer state, saturation, and recovery | does the control reduce harm or amplify load and tails? |
| configuration | effective non-secret configuration revision, validation failure, source precedence, and refresh state | did the service start and operate under the intended runtime contract? |
| health and deployment | process state, readiness semantics, dependency policy, release revision, traffic stage, stop signal, rollback or forward recovery | can automation route traffic and recover without causing loops? |
| migration | migration identity, preflight result, phase, compatibility, data remediation, lock or duration observation, and recovery state | can mixed versions and data move safely through the rollout? |

**Correlation and identity**

Request identifiers are not business-effect identifiers. One business operation may span client retries, proxy replays, service attempts, worker deliveries, and reconciliation. Use target conventions to correlate:

```text
route decision identifier
target and release revision
original operation or business effect identity
request and trace identity
attempt number and retry owner
durable work and delivery identity
schema or migration revision
terminal outcome and recovery identity
```

Never place raw credentials, authorization tokens, full request bodies, personal data, arbitrary user identifiers, exception dumps with secrets, or unbounded URLs and SQL in labels. Hashing does not automatically make sensitive or high-cardinality data safe. Follow target privacy, access, and retention policy.

**Cardinality and cost controls**

- Use bounded outcome and error categories; keep detailed diagnostics in access-controlled events when necessary.
- Count original operations and attempts separately so retries do not inflate demand or success.
- Record dependency class rather than arbitrary endpoint strings when the specific endpoint is not operationally necessary.
- Avoid stack trace, message text, tenant, user, business key, route path parameters, and dynamic query values as metric labels.
- Define sampling by question. Sampling may preserve trends while losing rare tails, denied events, duplicate effects, or forensic lineage.
- Observe exporter failure, dropped events, queue pressure, and stale collection for action-critical signals.
- Estimate telemetry volume and query cost under the workload envelope before broad rollout.
- Retire dashboards and alerts whose semantics, owners, or consumers no longer exist.

**Signal-to-action table**

| Observed condition | First diagnostic split | Owner action |
|---|---|---|
| timeout rises | caller deadline, application queue, dependency latency, retry amplification, or saturation | contain attempts or admission, preserve original failure, and diagnose the owning boundary |
| cancellation rises | user abandonment, deadline policy, proxy behavior, or server overload | verify propagation and resource release before changing timeout policy |
| attempts rise without completions | transient classification, nested retries, provider outage, or overload | suppress amplification and preserve terminal failure evidence |
| queue age grows | arrival exceeds service, poison work, worker loss, dependency slowdown, or drain failure | apply accepted backpressure, isolate poison work, and protect recovery capacity |
| duplicate effects appear | identity scope, unknown outcome, redelivery, transaction race, or reconciliation gap | stop blind repetition and repair under domain ownership |
| denied outcomes change | policy revision, principal source, route bypass, or abuse pattern | verify deny behavior and escalate unauthorized policy drift |
| readiness churns | dependency policy, migration, exporter, resource pressure, or platform automation loop | stabilize traffic and health semantics before restarting repeatedly |
| route corrections cluster | target preflight, source role, adjacent edge, or gate guidance is weak | update bounded route fixtures and invalidate affected shortcuts |
| telemetry disappears | exporter, sampling, schema, access, or query drift | mark blind spot, avoid false healthy conclusions, and restore evidence path |

An alert with no authority to act is an unresolved ownership issue. A dashboard without a question is decoration. A runbook action that can worsen data, security, or availability needs authorization and recovery evidence.

**Worked runtime example: external provider timeout**

Good signal set:

```text
original pricing operation count and terminal outcome
provider attempt count by bounded failure class
total deadline consumed and provider duration distribution under an owned objective
client pool or executor saturation
caller cancellation and child termination
retry suppression, fallback decision, and recovery state
route, target revision, and provider adapter version
```

The operator can distinguish slow provider, local queueing, retry amplification, and caller abandonment. Sensitive request and credential data is absent.

Bad signal set: a metric labeled by full URL, customer identifier, exception message, and attempt ID, plus a single `request_failed` count. It creates privacy and cardinality risk while hiding original operations, failure class, saturation, and recovery.

Borderline set: timeout and dependency duration are visible, but client pool saturation is not. If the accepted rollout claims capacity under concurrency, that blind spot blocks the claim or requires a representative target experiment. If the change is low-consequence error mapping only, document the limitation without inventing new production telemetry.

**Worked route-plane example: wrong framework correction**

Good evidence records target build and module, initial wrong Spring source edge, reviewer correction to Ktor, stage of detection, affected decisions, no target edits made, updated classification fixture, and shortcut invalidation. It does not record private reviewer conversation.

Bad evidence records only `review failed`. Future agents cannot determine whether the source, target, mechanism, or reviewer wording caused the correction.

**Verification procedure**

1. Trigger representative success, validation failure, dependency failure, timeout, cancellation, duplicate, overload, and recovery scenarios that apply.
2. Confirm emitted signals use the intended unit, outcome vocabulary, correlation, target revision, and bounded dimensions.
3. Run expected queries or traces and verify they distinguish the causal branches needed for action.
4. Confirm success does not emit failure alarms and prohibited sensitive or dynamic fields never appear.
5. Drop, delay, duplicate, or stale the telemetry path in an isolated environment and verify blind-state detection.
6. Exercise the runbook or tabletop action with its owner; confirm containment and recovery rather than alert acknowledgement alone.
7. Observe signal behavior under representative volume for cardinality, export pressure, storage, and query cost.
8. Record environment, last verification, limitations, and invalidation event.

Use vendor-specific commands only after discovering the target stack. The semantic checks remain the same whether signals use structured logs, metrics, traces, audit events, or another platform.

**Lifecycle**

Shared outcome categories, correlation identifiers, audit schemas, and alerts are contracts. Version them when consumers depend on semantics. Update route records and runbooks together when names or meanings change. Preserve enough lineage for incidents that cross revisions, then retire obsolete fields, dashboards, alerts, and high-cost diagnostics deliberately.

Observability remains an operational hypothesis. Instrumentation and queries can be inspected directly; future diagnostic value and peak cost remain uncertain until drills and incidents test them. Record known blind spots, and let incidents improve both runtime signals and the routing examples that should have activated them.

## Performance Verification Method

Performance verification has two independent subjects:

1. **Target runtime performance:** whether a Kotlin backend operation meets an owner-approved objective under a representative workload while preserving correctness, resource, failure, and recovery constraints.
2. **Routing workflow performance:** whether this reference reduces the effort and delay needed to reach a correct, evidence-backed next action without increasing unsupported claims, material corrections, omissions, or recovery cost.

Do not use one as evidence for the other. A short routing session does not prove handler latency. A fast handler does not prove that the source route, framework choice, or production boundary was correct.

This reference does not set generic handler thresholds. The seed values of p95 under 200 ms and p99 under 500 ms are not retained because no target service objective, operation class, environment, workload, dependency distribution, or error policy supports them.

**Performance applicability decision**

| Question | If yes | If no |
|---|---|---|
| Does the accepted outcome make a runtime performance or capacity claim? | obtain target owner objective and workload envelope | do not invent a latency threshold |
| Could the change alter algorithmic cost, allocation, blocking, pool use, fan-out, query plan, queue, serialization, logging, or retry behavior? | run baseline-relative regression evidence even if no production objective exists | existing functional gates may be sufficient |
| Does the claim depend on external provider, database, broker, proxy, scheduler, or platform behavior? | add representative integration or staged evidence | keep component claim narrow |
| Does the route promise faster engineering or review? | compare comparable cohorts with correction and evidence-quality guards | omit workflow speed claims |

`Not applicable` needs a reason and reopen condition. It is better than a benchmark against an arbitrary number.

**Target runtime objective contract**

Before measuring acceptance, record:

```text
Operation and user or operator outcome
Target-owned objective and accountable owner
Measurement boundary: client, proxy, route, service, dependency, worker, or end-to-end
Workload envelope: operation mix, arrival, concurrency, data, fan-out, failures, and recovery
Correctness, duplicate-effect, security, and error guards
Latency, throughput, backlog, age, resource, or capacity statistic and calculation method
Treatment of failures, cancellations, retries, warmup, and timeouts
Target revision, framework, JVM, environment, limits, and dependency versions
Comparison baseline and decision rule established before results
Rollout, stop, and recovery behavior if the objective is not met
```

An owner may choose latency percentiles, throughput, queue age, batch duration, memory, allocation, CPU, pool saturation, recovery time, or another measure. Use only those that represent the accepted outcome. Include failed, cancelled, shed, timed-out, and retried work according to a declared policy so the system cannot appear faster by dropping difficult operations.

**Method selection**

| Method | Best question | Required guard | Claim boundary |
|---|---|---|---|
| complexity or static analysis | did algorithmic shape, query count, fan-out, or allocation risk change? | inspect actual target call path and compiler or tool assumptions | hypothesis, not measured runtime |
| microbenchmark | did a pure or isolated hot operation regress? | stable input distribution, warmup, harness overhead, correctness assertion | component only |
| focused component load | how do handler, client, pool, query, or worker mechanics behave under controlled pressure? | real mechanism where it matters and observed saturation | selected component and environment |
| production-dialect or real dependency test | do database, broker, serialization, protocol, or lifecycle differences affect performance? | representative schema, data, configuration, and cleanup | dependency integration, not full topology |
| end-to-end synthetic load | does the target service meet an objective under controlled representative phases? | production-like limits, failures, correctness, telemetry, and recovery | recorded environment and range |
| sanitized trace replay | how does a change behave under observed distributions and skew? | privacy controls, trace provenance, and changed-system awareness | historical shapes, not future extremes |
| profiler or allocation analysis | where are CPU, blocking, contention, memory, or allocations spent? | measure perturbation and comparable conditions | diagnostic explanation |
| canary or staged comparison | does behavior hold in the target platform with bounded exposure? | owner authorization, traffic comparability, stop and recovery | staged population and time window |
| routing cohort study | does the reference reduce correct-decision and handoff effort? | comparable consequence, target access, completion level, and independent corrections | workflow population studied |

Use isolation to diagnose and integration to accept. A microbenchmark can explain a parser improvement; it cannot establish end-to-end service capacity. A staged result can support platform behavior; it may not isolate the code change without a comparable baseline.

**Runtime performance evidence packet**

| Field | Completion rule |
|---|---|
| hypothesis | name the mechanism expected to change and causal reason |
| baseline | immutable target revision, environment, configuration, result, and known noise |
| candidate | one comparable revision and intentional differences |
| workload | generator, input provenance, arrival, concurrency, operation mix, data skew, dependency and failure phases |
| environment | hardware or limits, JVM, flags, container, network, database, broker, proxy, and versions |
| method | warmup, run duration, repetitions, measurement boundary, clocks, sampling, percentile or aggregation method |
| correctness guards | output contract, invariant, duplicate effect, ordering, error, cancellation, and recovery assertions |
| resource signals | CPU, memory, allocation, thread or dispatcher, executor, connection, lock, queue, and dependency pressure as applicable |
| result | raw bounded artifacts, summary, variability, errors, and excluded data with reasons |
| interpretation | measured claim, uncertainty, confounders, extrapolation limit, and owner decision |
| recovery | behavior after load or failure stops, including backlog, pools, health, and durable work |

Re-run the baseline in the same measurement session when practical. If both baseline and candidate move together, environment drift may dominate. Do not discard inconvenient runs without a predeclared invalidation reason.

**Anti-benchmark checks**

- Does the generator preserve intended arrival behavior, or does it pause with the system and hide coordinated omission?
- Are warmup, compilation, cache state, connection establishment, and cold start separated or intentionally included?
- Are success, failure, timeout, cancellation, shedding, retry, and fallback represented and counted correctly?
- Are original operations distinct from attempts and redeliveries?
- Does uniform synthetic data hide hot keys, historical anomalies, large payloads, or query-plan changes?
- Are target resource limits effective, or is the local process using unconstrained host capacity?
- Does a faster response come from weaker validation, omitted work, stale data, dropped telemetry, or early failure?
- Is queue growth observed during load and recovery after offered load ends?
- Can the correctness assertion fail if the optimization violates the accepted invariant?
- Are sensitive inputs and traces sanitized without removing performance-relevant shape?

**Worked runtime case: external provider route**

Good method: hold the target revision, client configuration, and environment constant; vary provider success, slow response, transient failure, cancellation, and malformed response under the accepted arrival and concurrency envelope. Observe end-to-end deadline, attempt tree, client pool or executor saturation, terminal errors, correctness, cancellation cleanup, and recovery. Compare baseline and candidate with a predeclared owner decision rule.

Bad method: send uniform successful requests to a fake provider on a developer laptop, report one percentile, omit failed requests, and claim production scalability. The evidence can at most compare local route overhead under that fixture.

Borderline result: local component latency improves while staging tails worsen and client pool pressure rises. Do not choose the preferred result. Investigate environment, concurrency, retry, and dependency interactions; narrow the component claim until the integrated conflict is resolved.

**Worked data case: uniqueness change**

A throughput-only test is insufficient. Use representative key distribution and concurrent duplicate keys, verify one accepted effect and stable conflict behavior, observe database locks and connections, and include migration state. An optimization that increases throughput while allowing duplicate durable records fails correctness.

**Routing workflow method**

The unit is one routed outcome under one target revision, not one response or tool call. Compare cohorts by accepted outcome type, changed boundary count, consequence, target access, completion level, and reviewer role.

| Workflow signal | Guard against false improvement |
|---|---|
| time to evidence-backed next action | material correction, unsupported claim, and mode omission rate |
| reviewer decision time | route complexity, source access, and handoff completeness |
| source decision yield | missed caveat, wrong-source escape, and orientation value |
| number of routing loops | legitimate scope change and newly available evidence |
| time to verified handoff | verification depth, environment availability, and residual risk |
| time to recovery after wrong route | consequence, artifact preservation, repeated defect, and owner dependency |

Do not optimize workflow speed by skipping target discovery, suppressing unknowns, loading fewer sources indiscriminately, or using shallow gates. A faster first answer with more material corrections increases total correct-delivery cost.

**Routing performance experiment**

1. Define eligible tasks and hold consequence and target access comparable.
2. Establish a baseline from route records and independent reviewer labels.
3. Change one routing mechanism, such as preflight order, source index, artifact schema, or adjacent edge.
4. Measure time and effort together with correct action, correct abstention, false action, false stop, source yield, gate falsifiability, and handoff recovery.
5. Inspect cases behind aggregate movement and retain disagreements.
6. Test an exception cohort so the mechanism does not merely overfit common tasks.
7. Version, retain, adapt, or revert the routing change with an invalidation event.

**Pass, fail, and conditional interpretation**

- **Pass:** the predeclared target-owned objective or baseline-relative rule is met, correctness and resource guards hold, recovery returns to the accepted state, and evidence supports only the recorded boundary.
- **Fail:** the objective is missed, a correctness or security guard fails, resources saturate outside policy, recovery does not complete, or methodology cannot support the claim.
- **Conditional:** results conflict, variance or environment drift dominates, workload is not representative, target ownership is missing, or the measured range is too narrow. State the next evidence and safe interim decision.
- **Not applicable:** no performance claim or meaningful mechanism change exists; retain the trigger that would reopen measurement.

Performance is multi-objective. An optimization may trade latency for memory, throughput for fairness, availability for stale data, or reviewer speed for evidence quality. Predeclare the primary objective and guardrails with owners. Report measured results separately from production extrapolation and business forecasts.

The fastest route is not the shortest response. It is the route that reduces total time and cost to correct, verified, recoverable delivery without shifting hidden work into queues, incidents, reviewer correction, or future context reconstruction.

## Scale Boundary Statement

This reference is sufficient while one bounded Kotlin backend outcome, target revision, primary route, set of changed boundaries, and recovery path can be reviewed coherently. It can compose several specialist references; it should not pretend to own decisions whose authorities, interfaces, verification environments, or rollout paths are independently governed.

No file, endpoint, request, source, or agent count defines the boundary universally. Transition when one record can no longer keep conflicts, assumptions, evidence, invalidation, and recovery local enough for a reviewer to act safely.

**Sufficiency test**

Remain in one route when all applicable statements hold:

- One accepted outcome has a clear success, failure, recovery, and non-goal boundary.
- Target framework, build, revision, and changed call path are knowable as one coherent snapshot.
- Primary and companion modes can be reconciled without mutually exclusive assumptions.
- Product, data, security, platform, and operations owners have explicit decisions or bounded handoffs.
- Effects, transaction, durability, and retry identity can be traced through one outcome.
- Source conflicts can be resolved or retained as conditionals without blocking unrelated slices.
- Required gates fit one integration and recovery plan.
- Rollout and reversal do not force independently acceptable changes to move together.
- A fresh reviewer can understand the route record without an unbounded source or transcript dump.

If one statement fails, choose composition, split, phase, or escalation based on the specific boundary rather than making the whole task larger.

**Scale dimensions and transitions**

| Scale pressure | Keep one route when | Transition signal | Response |
|---|---|---|---|
| outcome | behaviors share acceptance and recovery | parts can ship, fail, or roll back independently | split outcome records and define integration contract |
| systems | one call path and compatibility boundary remain reviewable | several services, providers, stores, or brokers have independent versions and owners | assign component routes plus end-to-end integration owner |
| framework | one confirmed Spring or Ktor state | migration, mixed runtime, or framework coexistence is accepted | separate current feature, transition, and retirement phases |
| data and effects | one transaction and effect identity govern behavior | schemas, stores, unknown outcomes, or remediations have independent risk | split data, application, and rollout evidence with shared invariants |
| trust | one policy owner and principal boundary apply | tenant, identity, secret, external exposure, or abuse policies diverge | specialist security route and explicit adjudication |
| runtime | config, deploy, health, and recovery move together | regions, platforms, migrations, traffic stages, or recovery authorities differ | phased operations routes with compatible state transitions |
| source corpus | bounded regions answer the target questions | source discovery is unbounded, conflicting, duplicated, or version-fragmented | source-graph narrowing and claim-level ownership |
| verification | one gate set observes the accepted behavior | tests require independent infrastructure, environments, or destructive authorization | evidence slices plus integration matrix and residual gaps |
| ownership | owners can decide within one handoff | decisions have different authorities, schedules, or risk acceptance | owner-specific decision packets and terminal escalation |
| execution | work is sequential or shares stable assumptions | parallel work would mutate shared facts or artifacts | freeze common intake and assign exclusive write ownership |
| lifecycle | one invalidation event set applies | consumers, versions, or review cadences diverge | versioned shortcuts or references with independent retirement |

**Routing topologies**

| Topology | Use when | Main risk | Required safeguard |
|---|---|---|---|
| integrated route | changed boundaries are tightly coupled and one reviewer can reconcile them | context growth hides priority | active-source yield and explicit mode boundaries |
| specialist composition | specialists answer distinct questions under one outcome | outputs carry incompatible assumptions | immutable shared intake and parent reconciliation |
| sequential phases | later decisions depend on earlier evidence, such as data profile before migration | early shortcut constrains later work incorrectly | phase exit contract and ability to reopen upstream decision |
| parallel evidence collection | target areas are read independently and no shared mutation occurs | snapshots drift or evidence is duplicated | target revision freeze, exclusive artifacts, and comparison owner |
| parallel implementation slices | outcomes and interfaces are stable and independently testable | local green states fail integration | contract fixtures, merge gates, and integration owner |
| map-reduce review | many similar artifacts need consistent checks | summary loses exceptions and dissent | retain per-item evidence and sample skeptical reread |
| migration waves | compatibility and rollback require controlled cohorts | mixed versions or data states become unowned | state-machine rollout, telemetry, stop, and recovery authority |
| human or external escalation | policy, current authority, destructive action, or production risk exceeds corpus ownership | delay or ambiguous return | exact blocked decision, evidence packet, safe interim state, and requested verdict |

Parallelism is not a default optimization. It is safest for independent evidence collection under a frozen target snapshot. It is riskiest when several agents or teams modify the same assumptions, files, schema, or rollout state before authority is resolved.

**Minimum split contract**

Every slice must contain:

```text
Parent route and immutable target revision
One accepted slice outcome and explicit non-goals
Exclusive artifact and write ownership
Inputs and assumptions received from other slices
Output interface, compatibility, and consumers
Source roles and owner decisions within the slice
Requirements, first negative case, and focused gates
Executed evidence state and unresolved gaps
Rollback, forward recovery, and terminal escalation
Return packet and invalidation events
```

The parent route owns cross-slice reconciliation:

```text
Shared requirement and interface matrix
Assumption versions and conflict ledger
Dependency ordering and mixed-state compatibility
End-to-end correctness, trust, data, and recovery gates
Release sequencing, traffic, and stop authority
Integrated result, residual risk, and owner acceptance
```

A locally green slice is provisional until its assumptions and outputs are compatible with every consuming slice.

**Shared-workspace safeguards**

- Assign one owner per reference, packet, target file, generated artifact, or manifest region.
- Freeze the accepted target revision and common intake before parallel reads or edits.
- Do not let parallel workers rewrite the same reference or packet without a deliberate merge owner and conflict review.
- Preserve user and peer changes; re-read an owned file before applying a patch after interruption or conflict.
- Persist packet section, reference section, and immediate gate before moving to the next atomic unit.
- Journal at bounded intervals with exact files, counts, tests, blockers, and non-empty next steps.
- Treat heading drift, normalized duplicate rationale, source-hash mismatch, stale target revision, and ownership conflict as stop signals.
- Reconcile returned specialist decisions before implementation or integration, not by concatenating prose afterward.

**Context-scale safeguards**

Large codebases require dependency or source-graph narrowing before concrete guidance. Use pointers and bounded regions rather than raw repository dumps. Rank sources by the question they answer and authority they carry. Offload durable route state to files, then reread in bounded groups with checkpoints. When context grows, split by accepted decision or evidence owner, not arbitrary line count.

Unbounded source discovery is itself a blocker for implementation-ready status. Establish a search stop rule such as: the target call path, governing policy, effective build, relevant source regions, and required gates are known; additional sources no longer change a decision or risk. This is a local sufficiency judgment, not proof that every relevant fact was found.

**Worked scale choices**

Good retained route: a pure parser invariant touches several callers but one domain owner, one shared type, no state or runtime change, and one coherent test set. Splitting among framework, database, and operations specialists adds coordination without protecting a changed boundary.

Good composition: a Ktor provider route uses framework, resilience, testing, and runtime specialists. They share one target revision and return plugin, deadline, fixture, and config evidence to a parent outcome. No specialist independently changes the public error or fallback policy.

Good split: a Spring service adds a unique request key and deploys a schema constraint. Split data profiling and remediation, application mixed-version compatibility, production-dialect migration rehearsal, and rollout traffic. Share one invariant and key definition; integrate with a staged state machine and recovery plan.

Bad split: several agents each select framework, timeout, and error behavior for the same endpoint from different snapshots. All local documents look complete, but no owner reconciles assumptions. More parallel output has reduced evidence coherence.

Borderline case: a route currently fits one service, while a second consumer is planned but not accepted. Keep one target route and define interface plus expansion trigger. Do not create cross-service governance solely from a forecast; do not hard-code assumptions that make the accepted future consumer impossible without noting the tradeoff.

**Verification at scale**

- Validate every slice's exact target revision, owner, inputs, outputs, requirements, and recovery.
- Build an assumption matrix and deliberately change one shared fact; dependent slices must become stale.
- Exercise contract fixtures before full integration exists, then retain unverified end-to-end boundaries.
- Run compatibility across mixed application, schema, event, config, and job states that rollout permits.
- Test a failure in each slice and one correlated failure across shared resource or timing boundaries.
- Rehearse stop and recovery at the integration layer, not only component rollback.
- Resume from persisted handoff with fresh context to detect implicit decisions.
- Sample merged artifacts for lost dissent, duplicate claims, stale source roles, and false completion.

**Scale exit conditions**

Escalate beyond this reference when current legal or security authority is required, production action is destructive or irreversible, multiple organizations must negotiate policy, distributed consistency needs formal system design beyond a bounded Kotlin route, or target evidence cannot be safely obtained. Provide the exact blocked decision, causal consequence, gathered evidence, rejected options, safe interim state, and requested authority.

Scaled routing infrastructure such as manifests, source indexes, validators, shared templates, and merge gates becomes maintained project behavior. Give it consumers, versioning, fixtures, observability, fallback, and retirement. If scale pressure disappears, compare the simpler route again and decommission coordination machinery whose cost no longer protects an accepted boundary.

The objective is not maximum concurrent work. It is local reasoning with global coherence: each slice can be understood, tested, and recovered independently, while interfaces, assumptions, ownership, and end-to-end behavior remain explicitly reconciled.

## Future Refresh Search Queries

No browsing was performed for this evolution. The local research brief is dated 2026-06-23, and its public mappings remain unrefreshed. The query catalog below is a future protocol, not evidence that a result was retrieved, current, applicable, or accepted.

Refresh only when an external claim can materially change a target route: version compatibility, framework behavior, coroutine or client semantics, security advisory, migration, database or broker mechanism, provider contract, build tool, or deployment integration. Stable principles such as claim-level authority, progressive disclosure, and target verification do not need routine searching merely because time passed.

**Refresh trigger**

| Trigger | Question to resolve | Do not refresh when |
|---|---|---|
| target dependency upgrade | what changed between effective old and new versions, and which target gates must move? | version and behavior remain unchanged and existing evidence still applies |
| disputed API or lifecycle behavior | what does current direct authority specify for the pinned target version? | the dispute is actually project policy or domain semantics |
| security-sensitive mechanism | is there a current advisory, mitigation, or configuration requirement affecting the target? | no trust boundary or affected component exists in scope |
| local source conflict | which claim has current authority, and does the target reproduce it? | conflict can be resolved from target policy and observed behavior alone |
| provider contract change | how do effect, timeout, idempotency, rate, schema, or error semantics change? | no external integration or accepted provider change exists |
| migration or deprecation | what transition, compatibility window, and removal behavior are documented? | framework migration is not an accepted outcome |
| unexplained target failure | is the failure a known current defect, incompatibility, or changed default? | diagnosis has not yet localized the target mechanism |
| promoted shortcut review | do its external assumptions still hold for supported consumers? | invalidation events have not occurred and target fixtures remain representative |

**Query construction record**

```text
Claim or decision the search may change
Target framework, library, tool, provider, database, or platform
Effective version and comparison version if migrating
Mechanism, failure, configuration, or lifecycle term
Preferred direct-authority domain or repository
Document type: API, guide, release, migration, advisory, issue, or source
Expected result and route or gate impact
Retrieval authorization and privacy boundary
Stop rule and fallback if authority is unavailable
```

Search terms are discovery instructions. The resulting page, version, date, scope, and authority must still be verified.

**Future query families**

Convert each recipe into a concrete query using the inspected target version and named mechanism; the recipe itself is not proof.

| Query purpose | Precise query pattern | Preferred authority | Target reconciliation |
|---|---|---|---|
| Kotlin language change | query Kotlin official compatibility and migration material using the effective target version and the exact language or standard-library feature | Kotlin official language, API, compatibility, or release material | compile and test the target construct under the effective toolchain |
| coroutine semantics | query official coroutine documentation and release notes using the effective library version and the exact cancellation, dispatcher, flow, or context behavior | coroutine library official API, guide, release, or source | exercise target scope, cancellation, dispatcher, and failure behavior |
| Spring upgrade | query the official Spring migration guide between the target's current and proposed versions, scoped to the named mechanism | Spring official reference, API, release notes, and migration material | run configured target slice and compatibility gates |
| Spring behavior | query the official Spring reference for the effective framework version and exact MVC, reactive, transaction, or security mechanism | Spring official reference or API | inspect effective stack and reproduce behavior in target context |
| Ktor upgrade | query the official Ktor migration guide between the target's current and proposed versions, scoped to the affected plugin or client | Ktor official documentation, API, release, or migration material | run target module, plugin, client, and test-host fixtures |
| Ktor behavior | query official Ktor documentation for the effective version and exact routing, status, negotiation, client, or cancellation mechanism | Ktor official API and documentation | verify configured plugins and target error or cancellation contract |
| build and plugin | query official build-tool and plugin compatibility material using effective Gradle or Maven plus Kotlin and framework plugin versions | official build-tool and plugin compatibility material | use repository wrapper and effective dependency resolution |
| serialization | query official serialization documentation for the effective version and exact polymorphism, null, default, or unknown-field behavior | official library API, guide, release, or source | run target wire-contract fixtures including malformed input |
| database or driver | query primary database, driver, ORM, and migration documentation using effective versions and the exact transaction, lock, or migration feature | database, driver, ORM, and migration-tool primary documentation | use production dialect, schema, isolation, and migration rehearsal |
| broker or worker | query official broker and client documentation using effective versions and the exact delivery, acknowledgement, visibility, or ordering mechanism | broker and client official protocol or reference | test duplicate delivery, failure, restart, and drain in target setup |
| security advisory | query the vendor and recognized advisory sources using the exact component version and advisory identifier or vulnerability mechanism | vendor advisory, recognized advisory database, and fixed release material | confirm target exposure, configuration, mitigation, and regression |
| provider effect | query the provider's versioned contract using the exact operation and its idempotency, timeout, retry, rate, and error semantics | provider's versioned API and operational contract | inspect actual target request, identity, outcome query, and failure fixture |
| known defect | query the official issue tracker, release history, and source using the exact target version plus sanitized error or mechanism | official issue tracker, release notes, source, or maintainer statement | reproduce target defect and verify fix or workaround on pinned versions |
| deployment integration | query official platform or proxy documentation using the effective version and exact health, shutdown, secret, traffic, or disconnect mechanism | platform, proxy, or runtime official documentation | run production-like startup, traffic, disconnect, health, and shutdown evidence |

Quoted exact error text may help discovery but can expose sensitive data. Sanitize credentials, personal data, tenant values, payloads, internal hosts, and proprietary identifiers before any external query, following target policy.

**Authority ladder by claim**

| Claim type | Strong candidates | Limits |
|---|---|---|
| intended API and configuration | versioned official API and reference documentation | documentation can lag, omit edge behavior, or describe a different version |
| changed behavior | release notes, migration guide, compatibility statement, and source diff | omission is not proof that behavior did not change |
| known defect | official issue, minimal reproducer, fixing change, and fixed release | open discussion may be unresolved or target-specific |
| vulnerability | vendor advisory, recognized advisory record, patched release, and target exposure analysis | identifier match does not prove target exploitability or safe mitigation |
| provider effect and rate policy | versioned provider contract and operational documentation | real failure and commit timing may still need target reconciliation |
| project policy | repository instructions and accountable owner | public best practice cannot override local governance automatically |
| observed target behavior | reproducible target test or production-like observation | observation does not define intended external policy and may be environment-specific |

Secondary tutorials, examples, answer sites, and search summaries can supply terminology or leads. They should not carry consequential compatibility, security, data, or production claims when direct authority is available. A popular code sample can be current, compile, and still violate the target's framework, effect, or owner policy.

**Refresh evidence packet**

```text
Refresh identifier and retrieval date
Trigger, disputed claim, and target decision at stake
Target revision, effective versions, and mechanism
Exact query and any domain or repository restriction
Direct source URL, document identity, version, and publication or update date
Bounded paraphrase and relevant scope
Authority role and known limitations
Contradictory or superseded evidence considered
Disposition: confirms, changes, narrows, conflicts, or does not answer
Target requirement, implementation, and gate impact
Executed target result or planned verification with state labeled
Consumers, invalidation, next review, and fallback
```

Line references to mutable web pages are insufficient by themselves. Retain version, heading or anchor, bounded paraphrase, retrieval date, and stable document identity. Respect copyright and quotation limits; the record needs evidence, not copied documentation.

**Skeptical refresh sequence**

1. Inspect target version and local decision first; otherwise the query cannot be scoped.
2. State what result would change, confirm, or fail to answer the route.
3. Prefer direct official authority for the mechanism and pinned version.
4. Search release or migration history when comparing versions; current reference pages alone can hide the transition.
5. Look for explicit limitations, negative behavior, and known defects rather than only the desired mechanism.
6. Reconcile source scope with target framework, configuration, dependencies, and environment.
7. Run the smallest target gate that can distinguish the competing claims.
8. Record unchanged decisions as well as changes, with no-result or unresolved-conflict state allowed.
9. Propagate semantic changes to examples, shortcuts, adjacent edges, requirements, tests, operations, and consumers.
10. Stop when direct authority and target evidence answer the material decision, or when unavailable authority is explicitly escalated.

Repeated broad searching with no new authority is not stronger evidence. Stop and retain the uncertainty boundary.

**Worked refresh cases**

Good Ktor upgrade refresh: target discovery identifies old and new Ktor versions plus the exact plugin and client behavior at risk. Search is restricted to official migration, release, and API material for those versions. The route records changed plugin behavior, updates the target fixture, and keeps provider semantics outside the claim.

Bad Ktor refresh: search `Ktor best practices 2026`, copy a tutorial snippet, and recommend it without comparing target version or plugins. Recency wording and ranking do not establish authority or applicability.

Good advisory refresh: a target dependency and version match an official advisory range. The team confirms actual exposure, uses the prescribed fixed release or mitigation, and runs security plus compatibility gates. A package-name match alone is not enough.

Borderline provider refresh: official documentation states idempotency, while retention duration and target SDK header forwarding are unclear. Preserve the contract claim as bounded, inspect outgoing requests, test duplicate identity, and retain reconciliation for uncertain outcomes.

Good no-refresh decision: a route only needs the local rule that source roles remain separate and target commands must be discovered. New public content cannot change that process decision, so no external context is loaded.

**Validation and maintenance**

- Every executed refresh has a trigger, target version, query, direct source, retrieval date, disposition, and target impact.
- Every currentness claim can be traced to a source that actually supports the mechanism and version.
- No query result overrides project policy or observed contradiction silently.
- No-browse or unavailable-authority states remain visible in downstream wording.
- Refresh tests include a target gate or explain why only orientation changed.
- Query families that repeatedly return irrelevant or secondary results are refined or retired.
- Semantic changes invalidate only affected claims and shared shortcuts, preserving still-valid lineage.

The query catalog is evidence infrastructure. Give promoted queries an owner, version scope, consumers, success and zero-yield feedback, and retirement. The goal is not permanent freshness theater; it is timely resolution of material uncertainty with direct authority and target proof.

## Evidence Boundary Notes

Evidence boundaries limit what an accurate statement can authorize. A frozen source can prove what historical guidance said; it cannot prove current API behavior, target applicability, team policy, or production success. A target test can prove behavior inside its revision and environment; it cannot define an external provider's intended contract or a product owner's risk decision.

**Evidence kinds and authority**

| Evidence kind | Can support | Cannot support alone | Required locator |
|---|---|---|---|
| frozen local corpus fact | exact historical text, source relationship, examples, warnings, and dated research mapping | current external behavior, target adoption, owner policy, or successful execution | frozen path, bounded heading or region, and SHA-256 |
| routing synthesis | recommended read order, claim roles, mode composition, alternatives, and stop conditions derived from bounded premises | universal Kotlin doctrine or target-specific implementation fact | premises, causal rationale, scope, and countercondition |
| current external authority | intended API, compatibility, migration, advisory, provider, or platform claim for a stated version and date | target configuration, project policy, or production behavior | direct source, version, retrieval date, bounded paraphrase, and authority role |
| target observation | repository instruction, effective build, framework, path, call graph, configuration, fixture, or environment state at a revision | future revisions, intended external semantics, or owner acceptance | immutable target revision and exact artifact or command locator |
| owner decision or policy | accepted product, data, security, operations, legal, or platform behavior within declared scope | technical behavior not observed and policy outside the owner's authority | accountable role, decision artifact, scope, date, and review trigger |
| planned verification | a proposed way to test a requirement and expected observation | an executed result or evidence that the gate is sufficient | target-discovered command or procedure, fixture, environment, and state `planned` |
| executed result | observed pass, failure, output, measurement, or recovery in a recorded target and environment | production guarantee beyond the range, environment, and mechanism tested | exact action, revision, environment, timestamp, concise result, and limitation |
| reviewer judgment | semantic fit, sufficiency, risk interpretation, and requested correction | direct runtime fact or policy beyond reviewer authority | reviewer role, rubric, rationale, dissent, and adjudication when needed |
| forecast or inference | expected workload, future value, risk, or causal conclusion combining premises | observed outcome or certainty outside the premises | premises, model, confidence boundary, owner, and invalidation signal |

The old three-label vocabulary remains useful only after refinement:

- `local_corpus_sourced_fact` must name the frozen source and bounded claim.
- `external_research_sourced_fact` must name the direct source, version, retrieval date, and scope; none were refreshed during this evolution.
- `combined_evidence_inference_note` must expose the premises, target boundary, causal step, alternative, and remaining uncertainty.

Do not attach one label to a paragraph whose sentences change authority. Split the claim when source, scope, version, confidence, disposition, or required owner changes.

**Frozen local evidence used for this evolution**

| Frozen source | SHA-256 | Strongest use in this reference |
|---|---|---|
| `reference-map.md` | `7451085f357ed6af8fdd41f592e83f5f4b5c7aa858be8a5456390b377f00f180` | historical navigation and read-order evidence |
| `sources-and-research-brief.md` | `2f73340890073548e7c9a723ba051528e0097581444889cc7a8fa400026a1ee1` | dated premise, expert-lens, and public-source mapping evidence |
| `SKILL.md` | `e3413837049aa6f31d325fa368bb8b9dcce7f298c770b42cd5f13c1217c3a410` | historical top-level activation, workflow, and mode index |
| `kotlin-backend-playbook.md` | `8654c3a4c68cda2514c546035e7a7908a99ad0f884088b7bf329abf807c31994` | shared Kotlin backend design and review candidates |
| `kotlin-spring-ktor-idioms.md` | `02c20786240e893fc258f4e067557bc65dcdafcac11a6efbdd049710b827ac5d` | separate historical Spring and Ktor mechanism candidates |
| `kotlin-backend-testing-and-fixtures.md` | `92f45a34cc8ac472b930eba33e4ffb6a442719baa53dd8caabd43006dfa99e26` | verification and fixture selection candidates |
| `kotlin-backend-security-and-resilience.md` | `8a07eb77e27a3b508224db76c60e20508b8b3d13b81fce86e87ea052be7d14a5` | trust, failure, timeout, retry, idempotency, and cancellation candidates |
| `kotlin-backend-runtime-and-ops.md` | `d0a218f3c5d7b07c561cd4aba94b7c943aa7575cd439d371fdbaf4e5415b1069` | configuration, signal, health, deployment, shutdown, and recovery candidates |

The research brief identifies its local synthesis date as 2026-06-23. No browsing was performed while evolving this reference on 2026-07-11. Public URLs and ecosystem claims mentioned in the frozen corpus are therefore historical leads, not refreshed current authority. File hashes establish source identity, not truth, freshness, or applicability.

**Claim record**

```text
Claim identifier and exact bounded statement
Evidence kind and authority role
Source or target locator, version, date, and hash where applicable
Scope: outcome, target revision, framework, environment, and consumers
Disposition: routing, promoted, adapted, conditional, rejected, superseded, or orientation-only
Premises and causal inference, if synthesized
Counterargument, counterexample, and boundary where the claim fails
Requirement or decision affected
Planned or executed gate with state labeled
Confidence dimensions: identity, semantic support, applicability, behavior, and currentness
Owner, invalidation event, fallback, and review date
```

Confidence is multidimensional. A frozen hash can make identity certain while semantic relevance is moderate and target applicability unknown. Do not average those dimensions into a single confident-sounding adjective.

**Evidence transition rules**

1. **Source identity:** verify path, bounded region, revision or hash, and document role.
2. **Semantic support:** confirm the source directly supports the paraphrased claim, including caveats and version scope.
3. **Target applicability:** inspect framework, versions, call path, configuration, dependencies, policy, workload, and changed boundary.
4. **Behavior:** run the smallest credible gate, including a relevant negative control, in the appropriate environment.
5. **Operational acceptance:** obtain owner decision, compatibility, rollout, signal, stop, and recovery evidence when production behavior changes.
6. **Lifecycle:** name consumers, invalidation, fallback, successor, and retirement when a claim becomes shared guidance.

Passing one transition does not imply the next. A direct official API page can pass semantic authority and fail target applicability. A focused target test can pass application behavior and leave proxy or production recovery conditional.

**Inference rules**

- State each premise with its evidence kind before the synthesis.
- Explain the causal step from premise to recommendation; do not rely on `best practice` as the bridge.
- Compare the simplest viable alternative and the cost of a wrong conclusion.
- Preserve missing owner policy or currentness as an unresolved premise rather than filling it from convention.
- Narrow wording and permitted action to the weakest consequential premise.
- Record what observation would falsify, strengthen, or invalidate the inference.
- Keep source omission separate from proof. A source not mentioning a failure can justify a question or test, not one predetermined implementation.

**Conflict resolution**

| Conflict | Resolution authority | Required evidence |
|---|---|---|
| two frozen local sources | claim roles, dates, intended scopes, and target fit | both bounded claims and source relationship |
| frozen source versus current official authority | current mechanism authority plus target compatibility | versioned direct source and target gate |
| documentation versus target behavior | inspect version, configuration, environment, defect, and intended policy | reproducible target result and direct source scope |
| target behavior versus project policy | accountable project owner decides whether behavior is defect or accepted exception | target observation, policy artifact, and correction or exception plan |
| reviewer disagreement | authority and evidence adjudicate, not majority or fluency | separate verdicts, assumptions, rubric, and owner decision |
| security or data consequence unresolved | stop unauthorized action and escalate to the proper owner | threat or data boundary, consequence, safe interim state, and requested decision |

Do not average conflicts. Preserve dissent and uncertainty until the correct authority or experiment resolves the consequential premise.

**Worked evidence records**

Good Ktor routing claim:

```text
Historical premise: the frozen map routes a new Ktor route to Ktor idioms and shared companions.
Target premise: the inspected build and module show the service already uses Ktor at the recorded revision.
Synthesis: preserve Ktor and select framework-specific guidance; reject Spring implementation guidance.
Behavior evidence: configured target route fixture exercises plugin, validation, and error behavior.
Residual: current public Ktor documentation and production proxy behavior are not established by those facts.
Reopen: framework version, module wiring, migration outcome, or proxy boundary changes.
```

Bad claim: `The map proves this endpoint should use Ktor and will handle cancellation correctly.` The map can route historical guidance; it cannot prove target framework or cancellation behavior.

Borderline claim: local guidance and target adapter tests indicate cancellation reaches the provider port, while the real SDK and production proxy remain unobserved. Report application-boundary support and keep end-to-end cancellation conditional. Do not average the evidence into `mostly verified`.

Good retry claim:

```text
Owner policy: a named transient read class may be retried within one total deadline.
Provider authority: the operation and rate policy permit repetition under stable identity.
Target observation: actual client forwards the required identity and cancellation.
Executed result: controlled transient and exhaustion fixtures preserve terminal error and resource bounds.
Inference: bounded retry is acceptable for the recorded class and environment.
Residual: correlated provider outage and production pool behavior need staged observation before capacity claims.
```

Bad performance claim: a local fake-provider run meets an arbitrary percentile, therefore production latency is safe. The threshold lacks owner authority, and the fixture lacks provider and platform applicability.

**Evidence verification layers**

- Recompute frozen hashes to detect source substitution or corruption.
- Compare exact Markdown headings with the archive to preserve section identity.
- Check packet question text, mandatory fields, exact uniqueness, and prefix-stripped normalized uniqueness.
- Inspect bounded source regions to verify paraphrase and caveats.
- Verify target locators, effective versions, and discovered commands at the recorded revision.
- Challenge one consequential gate with a relevant controlled defect.
- Reproduce conflict resolution and owner disposition from persisted artifacts.
- Change a source hash, target revision, or policy fact in an isolated fixture and confirm dependent claims become stale.
- Resume with fresh context and verify next action, stop, and recovery are reconstructable.

**Known in this evolved artifact**

- The eight frozen local files listed above were read and their identities recorded.
- The original 26 Markdown heading texts and order are the structural contract for this reference.
- The question packet uses the ten exact specification questions and six mandatory rationale fields for every section.
- The evolved guidance is a bounded engineering synthesis that prioritizes target discovery, framework preservation, progressive disclosure, falsifiable verification, honest uncertainty, and reversible routing.
- Artifact verification performed for this evolution can support claims about file structure and saved content only when its exact result is retained.

**Not established by this generic artifact**

- The current latest Kotlin, Spring, Ktor, coroutine, database, broker, build-tool, or platform API behavior.
- Any unspecified target repository's framework, versions, paths, commands, policies, workload, service objective, provider contract, or production topology.
- Production correctness, security, capacity, availability, migration safety, or recovery for a future implementation.
- Universal numerical thresholds, mandatory dependencies, or one framework-independent implementation recipe.

**Transfer and lifecycle rules**

- Rediscover target facts and effective versions before concrete reuse.
- Refresh direct external authority only when authorized and material, then retain query, source, date, disposition, and target impact.
- Link authoritative requirements, ADRs, tests, and runbooks instead of copying them into multiple evidence records.
- Invalidate only claims dependent on a changed source, target, owner, policy, or environment; preserve valid lineage.
- Version shared shortcuts and examples, test exceptions, and retain the generic fallback route.
- Retire evidence whose consumers or supported versions no longer exist, while preserving enough supersession history for diagnosis.

Evidence-bound routing is reversible context compression. A future reviewer should recover why a claim was safe enough, what it did not establish, which gate observed it, and what change requires a new decision without recovering the entire source corpus or conversation.
