# Kotlin Backend Security Resilience

This reference helps a Kotlin backend implementer or reviewer decide **how to preserve trust, authority, side-effect, cancellation, durability, and recovery guarantees for a bounded service transition, and how to prove the negative and failure paths before rollout**. It is not a framework tutorial, a product permission policy, a substitute for threat modeling or qualified security review, or evidence of a production SLO.

The governing question is:

> Which actors and data cross which trust boundary, what server-owned state may change, how can execution or dependencies fail, which degraded/replay behaviors remain safe, and what evidence would reject an unsafe implementation?

`local_corpus_sourced_fact`: The mapped 137-line local source covers trust boundaries, Spring Security and Ktor authentication patterns, passwords/tokens/sessions, browser CSRF context, input validation, coroutine cancellation, blocking calls, retries, idempotency, external clients, durable background work, and a review checklist.

`combined_evidence_inference_note`: Treat those topics as a connected service-transition model. The source supplies bounded defaults; target code, current platform contracts, adversarial/failure fixtures, and accountable owners determine applicability and acceptance.

**Default security-resilience workflow**

| stage | required question | produced contract | stop or route signal |
| --- | --- | --- | --- |
| Bound the transition | Which actor invokes which route/message/job, from which client/network context, to read or change which asset? | Entry, outcome, side effect, consequence, and explicit non-goals. | Product/domain intent, data classification, or ownership is unresolved. |
| Map trust and authority | Which bytes/claims/credentials enter, where are they parsed/authenticated, and where is authorization decided? | Trust-boundary and permission-decision map with deny behavior. | Identity-provider, policy, tenant, or privilege semantics need an accountable owner. |
| Classify failures | Which validation, authentication, authorization, domain, conflict, dependency, timeout, cancellation, persistence, and overload outcomes exist? | Typed failure taxonomy and stable external response boundary. | Generic exception handling would merge security and recovery decisions. |
| Define execution model | Which work suspends, blocks, runs concurrently, outlives a request, or must survive restart? | Structured scope, dispatcher/executor, deadline, concurrency, and durability rules. | Event-loop or request lifetime cannot safely own the work. |
| Define side-effect integrity | Which writes may be duplicated, reordered, partially committed, or replayed? | Transaction, idempotency/deduplication, response replay, and reconciliation behavior. | Storage/broker/provider semantics are unknown or non-atomic. |
| Define dependency behavior | Which external calls occur, under what timeout/deadline, error normalization, correlation, credential, and retry policy? | Provider port and bounded client failure contract. | Provider contract, credential handling, or capacity policy is unavailable. |
| Implement repository-native controls | Which current framework security, validation, persistence, coroutine, client, worker, and observability mechanisms govern the path? | Minimal compatible code and configuration under one ownership model. | A parallel auth/retry/runtime system would be introduced without migration. |
| Verify denials and failures | Which wrong credential, forbidden action, malformed input, timeout, cancellation, duplicate, restart, and saturation fixtures can disprove the contract? | Claim-capable negative/failure evidence plus expected side-effect counts. | Only happy-path or annotation-presence evidence exists. |
| Prepare operation and recovery | How is unsafe work contained, secrets protected, retries/backpressure observed, rollback/replay performed, and incident ownership activated? | Bounded rollout/recovery and invalidation record. | Production target, telemetry, SLO, rollback, or owner acceptance is missing. |

This order is a dependency graph rather than a demand for a large document. A current validation rule or log-redaction correction can reuse a trusted path and run focused negative evidence. A payment-like callback, cross-tenant command, or durable consumer needs deeper side-effect and operational proof even when its code diff is small.

**Protected dimensions**

| dimension | minimum decision | common false positive | capable evidence |
| --- | --- | --- | --- |
| Trust boundary | Parse and constrain untrusted body, route/query/header/cookie/claim/message/env/provider data at the appropriate edge. | DTO deserialization succeeds, so input is called valid. | Malformed/boundary fixtures plus domain-invariant tests. |
| Authentication | Establish who or what presented a credential under the current identity contract. | Token parsing is mistaken for current validity or authorization. | Missing, malformed, expired, revoked/invalid as applicable, and valid-credential tests. |
| Authorization | Decide server-side whether the principal may perform this action on this resource/tenant/state. | Route is authenticated, annotation exists, or client hid a button. | Allowed and denied cross-owner/role/resource negative paths at the authoritative layer. |
| Secret/session safety | Keep passwords, tokens, session IDs, reset material, credentials, and raw authorization data out of logs and unsafe storage. | Redaction works on one success log but exceptions/debug output leak values. | Log-capture/serialization review across success and failure plus platform-secret policy. |
| Browser context | Match CSRF and cookie controls to the actual browser/authentication model. | CSRF is disabled because an endpoint is called an API. | Client/auth model record, cross-site negative behavior, and framework configuration tests. |
| Failure semantics | Separate expected client/domain denials from infrastructure and unexpected defects without leaking internals. | Every exception becomes the same success/failure envelope or stack trace. | Contract/integration tests for status/body/log/metric behavior and internal-cause preservation. |
| Coroutine lifecycle | Preserve structured concurrency, request/workflow cancellation, deadlines, and intentional sibling isolation. | Function is marked `suspend`, so execution is assumed nonblocking and cancellable. | Controlled cancellation/timeout tests and child-lifecycle observation. |
| Blocking isolation | Keep blocking JDBC/JPA/file/provider work off event-loop-limited execution or choose an intentionally blocking architecture. | Blocking dependency is wrapped in a coroutine and called nonblocking. | Thread/dispatcher trace, saturation fixture, and repository runtime contract. |
| Retry/backpressure | Retry only classified transient work inside deadline/load budgets with visible attempt and terminal state. | Repeated success after several attempts is reported without duplicate/load cost. | Fault injection, fake time where suitable, attempt/effect counts, saturation and exhaustion evidence. |
| Idempotency | Make replayed writes return or reconcile a defined result without multiplying effects. | HTTP method, client button disabling, or broker delivery mode is treated as exactly-once. | Concurrent/duplicate request or delivery fixtures with transactional state/idempotency inspection. |
| External clients | Bound time, normalize provider failures, preserve correlation, and protect credentials behind a stable port. | A generated SDK or one successful sandbox call is considered resilient. | Success, timeout, malformed, relevant 4xx/5xx, cancellation, retry, and credential-redaction tests. |
| Durable background work | Use a durable mechanism when work must outlive request/process; bound concurrency and classify terminal handling. | Fire-and-forget request coroutine appears to continue in a local run. | Restart/redelivery/duplicate/dead-letter or parking/concurrency evidence under the chosen platform. |

These controls are coupled. A timeout can initiate retry; retry can duplicate a write; duplicate protection may need the same transaction as the state change; background execution can lose request-scoped principal context; a fallback can expose data that the primary path would deny. Verify the composition, not just individual configuration.

**Minimum inputs**

- Actor/principal, entry protocol, client context, resource/tenant, data sensitivity, intended side effect, and consequence.
- Current Kotlin/JVM framework, security chain/plugins, coroutine/runtime model, persistence and transaction behavior, broker/worker platform, provider clients, and deployment topology.
- Existing authorization convention and accountable product/security/domain decisions.
- Failure and retry taxonomy, deadline ownership, idempotency identity, and durability expectations.
- Safe fixtures for malformed, unauthenticated, forbidden, cancelled, timed out, duplicated, overloaded, restarted, and provider-failed states that apply.
- Project-native build/test/integration/observability and rollback mechanisms.

**Required outputs for durable work**

| output | minimum content | what it must not imply |
| --- | --- | --- |
| Protected-transition statement | Actor, input, resource, decision, side effect, success, denials, consequence, and non-goals. | That a framework annotation supplies business policy. |
| Trust/authority map | Inbound fields/claims, parser/normalizer, authentication, authorization owner, tenant/resource lookup, and deny behavior. | That parsed or signed data is automatically authorized. |
| Failure/cancellation contract | Expected/domain/infrastructure/unexpected classes, deadline, cancellation propagation, sibling isolation, external response, and logs/metrics. | That retries or catches may erase cancellation. |
| Side-effect/replay contract | Transaction boundary, idempotency identity/store, duplicate response, conflict, partial failure, and reconciliation. | That exactly-once behavior exists without evidence. |
| Execution/durability contract | Request versus durable lifetime, blocking isolation, concurrency bound, queue/worker terminal behavior, and shutdown/restart. | That `suspend` makes blocking code safe or request coroutines durable. |
| Implementation | Repository-native security/configuration/code with typed boundaries and least additional machinery. | That local compilation proves runtime or security behavior. |
| Evidence matrix | Negative auth/input, cancellation, timeout, duplicate, provider, saturation, restart, log-secret, recovery, and no-claim states as applicable. | That one test or scanner proves production security/reliability. |
| Handoff | Changed paths/config, commands/results, residual risks, rollback/containment, operations/security owners, and invalidation triggers. | That acceptance survives identity, provider, traffic, persistence, or policy changes. |

**Fit and route-away guide**

| pending question | use this reference? | stronger or preceding route |
| --- | --- | --- |
| Harden or review a bounded Kotlin route, client, coroutine flow, or worker | Yes. | Target repository implementation and negative/failure verification. |
| Choose business roles, tenant permissions, data retention, credential lifetime, or acceptable threat | Only to expose required decision fields. | Product/domain/identity/security/privacy owner. |
| Diagnose an unknown timeout, race, deadlock, duplicate, or saturation incident | Use after evidence narrows the mechanism. | Systematic reproduction, traces, metrics, thread/coroutine dumps, and incident diagnosis. |
| Select Spring Boot, Ktor, persistence, broker, or resilience library | Use for evaluation constraints. | Architecture/dependency compatibility, current official evidence when authorized, and target spike. |
| Establish cryptographic algorithm parameters or compliance | No independent authority here. | Current platform/security policy and qualified review. |
| Claim throughput, latency, availability, capacity, or failure rate | Use to define safety/equivalence gates only. | Controlled performance/reliability study and production SLO/telemetry owner. |
| Operate rollout, incident response, key rotation, revocation, or disaster recovery | Supporting traceability only. | Current operations/security runbooks, access, telemetry, and accountable command. |

**Evidence states**

- `local_source_observed`: the mapped security-resilience source was read under a named path/hash; its wording is known, target applicability is not automatic.
- `target_contract_identified`: product/security/framework/persistence/operations authority for the bounded transition is explicit.
- `negative_path_reproduced`: at least one intended deny/failure fixture demonstrates the pre-change or protected boundary.
- `implemented_for_scope`: target code/configuration expresses the stated trust, execution, side-effect, and recovery contracts.
- `verified_for_scope`: complementary negative/failure checks support the exact service/environment population.
- `owner_accepted`: accountable owner accepts policy, rollout, or residual risk under named evidence and expiry.
- `unresolved_or_blocked`: threat, policy, environment, provider, production, or evidence is unavailable; the dependent claim cannot proceed.
- `invalidated`: identity/security configuration, claims, domain policy, persistence, provider, runtime, traffic, deployment, or evidence harness changed.

Good use: a webhook consumer validates transport shape, verifies provider identity, authorizes the target account, stores its idempotency key transactionally with the state change, bounds concurrency/retries, preserves correlation, and tests duplicate, malformed, unauthorized, timeout, and redelivery paths.

Bad use: a route trusts a signed token's tenant field, catches every throwable, retries a database write after timeout, logs the raw authorization header for diagnosis, and is called resilient because the happy path passes.

Conditional use: an internal read-only diagnostic endpoint can use a smaller side-effect/retry contract when network, authentication, authorization, data sensitivity, and exposure are bounded explicitly. It cannot inherit that narrow evidence when later opened to browsers, tenants, writes, or durable workers.

This reference is complete for a bounded backend decision when another reviewer can identify the protected transition, locate each trust and authority decision, explain cancellation/blocking/retry/idempotency behavior, run intended denials and injected failures, count side effects, see what remains unknown, and know which future contract change reopens acceptance.

## Source Evidence Mapping Table

The source map routes claims; it does not count links. Local bytes establish what the mapped reference says. Product/security policy chooses the intended authority boundary. Target configuration, source, transactions, tests, runtime, and operational evidence establish implemented behavior. A retained public URL remains a future pointer until it is opened under authorization and reconciled with the installed version.

No public query or page retrieval was performed while evolving this reference.

**Mapped local source and process controls**

| source_location_path_key | observed identity | evidence class | strongest legitimate use | important boundary |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/references/kotlin-backend-security-and-resilience.md` | 137 lines; SHA-256 `8a07eb77e27a3b508224db76c60e20508b8b3d13b81fce86e87ea052be7d14a5`. | Dated local reference detail file. | Establish inherited guidance for ingress, auth, secrets/sessions, CSRF, validation, coroutines, blocking, retries, idempotency, clients, workers, and review. | It does not establish a target threat model, installed framework behavior, cryptographic parameters, production capacity, or accepted residual risk. |
| `agents-used-monthly-archive/idiomatic-references-202606/generated-references/kotlin_backend_security_resilience.md` | Frozen seed SHA-256 `74c1872fa32c445a33abb9458634322c71e71af25b21c59cecc2fa631c53d507`. | Structural and historical seed. | Establish the exact 26 headings, source pointers, inherited prose/numbers, and expansion baseline. | Its scores, endpoint/request bounds, reliability percentages, session target, and latency values are not measured target facts. |
| `idiomatic-reference-evolution-spec-202607.md` and `tests/test_idiomatic_reference_evolution.py` | Current shared process controls read by this lane. | Evolution specification and structural verifier. | Define packet questions/fields, persistence, uniqueness, exact headings/order, strict expansion, and placeholder requirements. | Passing them cannot establish service security, resilience, performance, or operability. |

The local detail file is the first semantic source for this theme, not the final authority for every Kotlin backend. Read it completely when security or failure behavior is material, then compare its defaults with the target's actual contracts.

**Target evidence map**

| pending claim | first authority | corroborating evidence | evidence that must not overrule it |
| --- | --- | --- | --- |
| Which actor may perform which action on which resource/tenant/state? | Product/domain/security/identity policy under an accountable owner. | Current authorization decisions, resource ownership model, threat/abuse cases, and denied-request tests. | A token field, route name, framework annotation, or client-visible control cannot invent permission. |
| What reaches the trust boundary? | Actual protocol/gateway/router/message contract and deployed topology. | DTO/schema, headers/cookies/claims, broker envelope, gateway config, and malformed-input traces. | The local source's generic ingress list cannot prove target exposure. |
| How are credentials authenticated? | Current identity provider, key/session/token validation configuration, and security chain/plugins. | Missing/malformed/expired/invalid/valid tests and provider contract. | Successful decode, signature library presence, or remembered framework behavior cannot settle validity. |
| Where is authorization enforced? | Repository convention plus authoritative application/domain/security decision. | Route/method/service configuration, data lookup, cross-tenant/resource negative tests, and code review. | Authentication success or UI hiding cannot establish authorization. |
| Which password/token/session/cookie controls apply? | Current platform/security policy and actual browser/client model. | Storage/config, redaction tests, cookie attributes, expiry/revocation/reset flows, abuse/rate-limit evidence. | An archived algorithm example cannot select current parameters or compliance. |
| Which validation is transport versus domain? | Schema/transport contract and current domain invariants. | Parser/validator/conversion code, malformed/boundary/cross-field/stateful tests, stable error contract. | DTO validation alone cannot authorize or prove business validity. |
| Is coroutine cancellation and timeout behavior correct? | Target runtime/framework and structured scope/deadline ownership. | Source, controlled cancellation/timeout/child tests, thread/coroutine traces, and provider behavior. | `suspend`, one library example, or successful completion cannot prove cancellation safety. |
| Is blocking work isolated safely? | Actual JDBC/JPA/file/provider behavior and runtime execution model. | Dispatcher/executor configuration, thread trace, saturation test, shutdown behavior. | Coroutine wrappers cannot relabel a blocking dependency. |
| Is a retry safe? | Failure taxonomy, side-effect semantics, deadline/load budget, and dependency contract. | Fault injection, attempt/effect counts, idempotency/transaction evidence, backpressure and exhaustion. | A retry library configuration or eventual success cannot prove safety. |
| Does idempotency prevent duplicate effects? | Transaction/persistence/broker contract and operation identity. | Concurrent duplicate/restart/redelivery tests, stored record/state inspection, response replay and conflict behavior. | HTTP method, client button disabling, or delivery marketing language cannot prove exactly-once. |
| Is an external client resilient and safe? | Current provider contract plus target client port/configuration. | Success, timeout, relevant 4xx/5xx, malformed, cancellation, retry, correlation, and secret-redaction tests. | Generated SDK or public docs alone cannot prove target integration. |
| Must background work survive restart? | Product durability requirement and current worker/broker/scheduler platform. | Persistence/ack/transaction, restart/redelivery/dead-letter or parking, concurrency and lag evidence. | A request-scoped launched coroutine cannot satisfy durable work by observation in one process. |
| Does a quantitative reliability/performance claim hold? | Controlled target study or approved production SLO/telemetry under an operations owner. | Frozen workload/environment, raw observations/failures, functional/security equivalence, rollout/rollback. | Seed values, one local run, or generic framework benchmark cannot set a target. |
| Is residual risk acceptable? | Accountable security/product/domain/engineering/operations owner under current policy. | Threat/abuse cases, negative/failure evidence, exposure, containment, recovery, dissent, and expiry. | A reference, build, or automated scanner cannot accept organizational risk. |

**Retained public research pointers**

| external_source_url_value | seed description | current state | future promotion gate |
| --- | --- | --- | --- |
| `https://kotlinlang.org/docs/home.html` | Kotlin language documentation pointer. | `unrefreshed_no_browse`; current content, route stability, version, and applicability were not checked. | Retrieve an exact current language/type-system claim only when authorized, then match compiler/toolchain and target code. |
| `https://github.com/Kotlin/kotlinx.coroutines` | Kotlin coroutines repository pointer. | `unrefreshed_no_browse`; no current cancellation, timeout, dispatcher, API, or release behavior is asserted. | Inspect versioned primary docs/source/releases for the installed dependency and reproduce positive plus cancellation/failure behavior. |
| `https://github.com/spring-guides/tut-spring-boot-kotlin` | Spring Boot Kotlin guide pointer. | `unrefreshed_no_browse`; no security-chain, coroutine, framework, or production recommendation is derived from it. | Retrieve only when a known Spring/Kotlin integration question requires it, match installed Spring Boot/Security configuration, and test target negative paths. |
| `https://ktor.io/docs/welcome.html` | Ktor documentation pointer. | `unrefreshed_no_browse`; no plugin, principal, routing, coroutine, or deployment behavior is claimed. | Retrieve feature/version-specific official guidance under authorization and verify target configuration plus missing/malformed/insufficient credentials. |

These descriptions are locally observed seed metadata, not refreshed public facts. Familiarity with the sites, search snippets, or remembered APIs cannot promote a row.

**Claim-specific read route**

1. Read the complete user request, newest instructions, repository rules, current progress, and authorized data/environment boundary.
2. Identify actor, asset/resource, entry protocol, side effect, failure consequence, and policy owner.
3. Inspect current security chain/plugins, routes/controllers, application/domain authorization, schemas/DTOs, persistence/transactions, coroutine scopes/dispatchers, clients, workers, and tests.
4. Read the complete local detail source for inherited defaults and cautions.
5. Separate product/security policy, local guidance, implementation facts, target observations, owner decisions, inference, and unknowns.
6. Select complete target modules and negative/failure fixtures needed for the pending transition; do not reason from annotations or function names alone.
7. Refresh a public source only when browsing is authorized and a version-sensitive contract can change the decision.
8. Bind each durable recommendation to its target state, check/fault fixture, owner, recovery, and invalidation trigger.

**Evidence promotion rules**

| starting evidence | permitted use | promotion requirement |
| --- | --- | --- |
| Local reference statement | Default, risk vocabulary, and candidate review question. | Target applicability, repository-native implementation, negative/failure evidence, and owner scope. |
| Product/security requirement | Intended policy and consequence. | Exact actor/resource/state semantics plus implementation and denial tests. |
| Current source/configuration | Implementation structure and candidate behavior. | Run/build/integration/runtime evidence for dynamic security and failure claims. |
| Unit/component test | Local deterministic behavior under one fixture. | Integrated security chain, persistence/dependency, concurrency, and environment evidence as claim requires. |
| Denied/failure request trace | Target observation for one named state. | Broader matrix and stable oracle before support or reliability claims. |
| Log/metric/dashboard | Operational observation under collection/sampling. | Schema, denominator, privacy, blind spots, correlation, and action contract. |
| Public documentation pointer | Future research location. | Authorized direct access, publisher/version/scope, narrow extraction, and target reproduction. |
| Owner approval | Authorized policy or residual-risk decision. | Recorded authority, evidence reviewed, affected population, recovery, expiry, and invalidation. |

**Conflict handling**

| conflict | required response |
| --- | --- |
| Local source recommends a default but platform/security policy differs | Preserve source wording historically; follow current authorized policy and verify target implementation. |
| Token/session claim conflicts with database/resource ownership | Treat authenticated claims as input; resolve authorization through the authoritative resource/policy path and deny safely. |
| Source configuration and runtime denial differ | Verify revision/deployment/gateway/security chain/cache; preserve both observations and diagnose before editing policy. |
| Unit test passes but integrated security chain permits forbidden action | Integrated denial blocks acceptance; repair fixture or enforcement at the authoritative layer. |
| Retry configuration says transient but duplicate side effects appear | Stop retries for the affected write, contain exposure, inspect transaction/idempotency, and reconcile state. |
| Official future guidance conflicts with installed behavior | Match versions/configuration and reproduce locally; route compatibility rather than averaging. |
| Target measurement contradicts copied latency/capacity values | Use target data only for its workload and return target selection to the accountable owner. |

Good source use says, "The local reference recommends preserving cancellation and bounded classified retries; this target path uses the named request scope and transactional idempotency record; cancellation and duplicate fixtures support the bounded behavior." Bad source use says, "Kotlin and coroutine links prove this service is secure, nonblocking, and resilient."

The map is causal and versioned. Policy and source guidance constrain the protected transition; configuration/code/persistence implement it; negative/failure and runtime evidence support or refute it; owners accept bounded risk; incidents and changed contracts create a new trajectory. A later correction must not rewrite what an earlier source actually contained.

## Pattern Scoreboard Ranking Table

The seed's values are preserved as **inherited editorial scores**. The local source supplies no formula, denominator, service cohort, threat or incident sample, workload, reviewer rubric, outcome study, or uncertainty. The values are historical emphasis, not percentages of risk reduction or universal control priorities.

**Preserved inherited scoreboard**

| pattern_identifier_stable_key | inherited_score_value | inherited_tier | protected failure | current interpretation |
| --- | ---: | --- | --- | --- |
| `security_source_context_first` | 95 | `default_adoption_pattern_tier` | Agent emits generic hardening advice without reading the mapped Kotlin security-resilience source or target service. | Load complete local guidance and current repository/platform context before selecting controls. |
| `security_evidence_boundary_split` | 91 | `default_adoption_pattern_tier` | Local guidance, remembered public behavior, target observation, policy, and inference are presented as one authority. | Type evidence and make each target recommendation name applicability and owner. |
| `negative_failure_gate_coupling` | 88 | `default_adoption_pattern_tier` | A control is declared secure/resilient because code/configuration exists, without exercising intended denial or failure. | Attach each material claim to a capable negative, fault, side-effect, or recovery gate. |

The repeated seed key `kotlin_backend_security_resilience` names the theme rather than independently addressable controls. The evolved keys preserve values while making each failure and gate reviewable.

**Causal adoption order**

1. `protected_transition_boundary`: actor, entry, asset/resource, side effect, consequence, and non-goals.
2. `trust_authority_boundary_split`: untrusted inputs/claims, authentication, resource/tenant lookup, authorization owner, and deny state.
3. `typed_failure_response_contract`: validation/auth/domain/conflict/dependency/timeout/cancellation/unexpected classes and stable external response.
4. `structured_execution_lifecycle`: request/workflow scope, child ownership, cancellation, deadline, sibling isolation, and blocking model.
5. `transactional_side_effect_integrity`: transaction, idempotency/deduplication, duplicate response, partial failure, and reconciliation.
6. `bounded_dependency_recovery`: provider port, timeout, error normalization, retry/backpressure, correlation, credential redaction, and fallback.
7. `durable_worker_execution`: process-independent work storage, bounded concurrency, retry classification, terminal parking/dead-letter, and restart/redelivery.
8. `negative_failure_gate_coupling`: malformed/denied/cancelled/timed-out/duplicate/saturated/restarted fixtures and log/metric evidence.
9. `operational_recovery_invalidation`: rollout, containment, rollback/replay, owner acceptance, incident route, and changed-premise revalidation.

This order is causal, not ceremonial. An existing platform may already implement several layers. Reuse is adoption only when the target transition and rejection behavior remain observable.

**Current qualitative register**

| pattern | default posture | apply when | adapt or avoid when | verification gate | counter-signal |
| --- | --- | --- | --- | --- | --- |
| Boundary parse then domain recheck | Default for every inbound trust boundary. | Body, path/query, header, cookie, claim, message, environment, or provider data enters the service. | Internal typed calls may skip transport parsing but still enforce domain invariants. | Malformed/boundary/cross-field/stateful fixtures fail at the intended layer with stable safe errors. | Validation logic is duplicated or transport constraints become business authorization. |
| Explicit authentication chain | Required where identity matters. | Credential/session/token/provider identity controls access. | Public endpoints still need abuse/data controls; do not add identity ceremony without policy. | Missing, malformed, expired/invalid, and valid states traverse the actual chain. | Tests bypass filters/plugins or mocked principal cannot represent deployment. |
| Server-owned authorization | Required for protected resources/actions. | Role, tenant, ownership, state, scope, or policy changes permission. | Method/route checks may be used only under a coherent single authorization convention. | Allowed and forbidden cross-role/resource/tenant cases exercise authoritative lookup and deny response. | Authorization is scattered across annotations, controller branches, database filters, and clients without ownership. |
| Secret/token/session hygiene | Required for credential-bearing paths. | Passwords, tokens, sessions, reset material, authorization headers, or provider secrets exist. | Parameter/algorithm values come from current security/platform policy, not this register. | Log/serialization/storage/config review across success and exception paths; abuse/rate-limit tests as applicable. | Debugging requires raw credentials or redaction destroys necessary nonsecret correlation. |
| Browser-auth CSRF analysis | Required when ambient browser credentials can authorize requests. | Cookie-authenticated browser flow or another automatic credential context exists. | Non-browser bearer clients can have different threats; document exact client/auth model. | Cross-site/CSRF configuration and negative behavior are tested in the deployed security model. | "API" label or disabled framework default substitutes for analysis. |
| Typed failure taxonomy | Default for all service boundaries. | Client/domain denials must differ from transient infrastructure and unexpected defects. | Keep types proportional; one local pure function may need a smaller set. | Contract tests assert safe status/body while internal cause, logs, metrics, and retry class remain distinguishable. | Generic catch/exception mapper erases cancellation, authorization, or retry semantics. |
| Structured cancellation preservation | Default for coroutine workflows. | Request, parent workflow, timeout, or shutdown should stop child work. | Supervisor isolation is valid when sibling independence is intentional and side effects remain safe. | Controlled parent/timeout cancellation stops children, propagates `CancellationException`, and prevents stale completion. | Broad `catch (Throwable)` or detached scope reports success after cancellation. |
| Honest blocking isolation | Default when any dependency blocks. | JDBC/JPA/file/legacy SDK or blocking client runs in coroutine flow. | A simple intentionally blocking service can be safer than mixed fake nonblocking execution. | Thread/dispatcher/executor trace and saturation/shutdown fixture under target runtime. | `suspend` label or dispatcher hopping spreads unbounded blocking rather than containing it. |
| Deadline-bounded external calls | Default for network/provider work. | Service calls a remote dependency or long-running operation. | Deadline values and timeout composition are local policy; avoid arbitrary copied constants. | Controlled connect/read/total timeout and cancellation tests preserve remaining budget and terminal response. | Layered timeouts exceed parent deadline or timeout is treated as retry permission automatically. |
| Classified bounded retry | Conditional, not universal. | Failure is transient, operation replay-safe, deadline/load budget remains, and dependency policy permits. | Validation, auth, deterministic domain errors, cancellation, overload, and unsafe writes are terminal or need new premise. | Fault sequence, attempt/effect counts, delay/budget/backpressure, exhaustion, and first-failure evidence. | Eventual success hides retry storm, duplicate effect, or user wait. |
| Transactional idempotent write | Required where duplicate delivery/request is plausible and effects matter. | Payment-like action, webhook, callback, queue consumer, or client-retriable mutation. | Read-only work or naturally idempotent state set may use a simpler proof. | Concurrent duplicate/restart/redelivery tests inspect state, idempotency record, response replay, and conflict behavior. | Idempotency store is separate from state transaction or key scope allows cross-actor collision. |
| Provider port/error normalization | Default for consequential external clients. | Provider API affects service result, retry, credentials, or correlation. | Tiny low-risk read can use lighter abstraction if testability and error boundary remain clear. | Success, relevant client/server error, malformed response, timeout, cancellation, retry, and redaction tests. | Wrapper hides provider distinctions needed for recovery or leaks provider internals into domain. |
| Durable critical background work | Required when work must outlive request/process. | Long-running side effect, scheduled job, queue consumption, or callback must survive restart. | Noncritical best-effort telemetry may have a deliberately weaker contract under owner policy. | Restart/redelivery, duplicate, concurrency, terminal parking/dead-letter, lag, and graceful shutdown evidence. | Fire-and-forget request coroutine appears reliable only because local process stays alive. |
| Negative and failure evidence | Required before consequential completion. | Trust, authority, cancellation, retry, durability, or recovery is claimed. | Focused correction can use one direct negative state plus neighboring regression. | At least one representative forbidden/failure fixture fails pre-change or under injected defect for the promised reason. | Suite checks only configuration presence, mocks away security chain, or retries until green. |

**Adoption profiles**

| profile | minimum visible controls | prohibited promotion |
| --- | --- | --- |
| Focused correction | Current transition/policy authority, exact defect, nearest negative/failure fixture, scoped implementation, side-effect/log check, and invalidation. | Cannot establish service-wide security, all-client compatibility, production reliability, or capacity. |
| Standard protected transition | Actor/asset/trust map, auth/validation, typed failures, execution/cancellation/blocking, side effects/idempotency, dependency recovery, negative/fault evidence, and handoff. | Cannot claim every attack, identity state, provider behavior, traffic level, or incident outcome. |
| Shared platform control | Consumer/service inventory, version/config contract, migration/compatibility, negative matrix, rollout/rollback, observability, and platform/security ownership. | One service fixture cannot authorize organization-wide adoption. |
| High-assurance transition | Standard controls plus qualified threat/domain/privacy/security review, sensitive data handling, independent negative evidence, production controls, incident/recovery exercise, and accepted residual risk. | Unavailable required authority or realistic environment remains a blocker, not an inferred pass. |

**Pattern admission and lifecycle**

A new register pattern enters only when it:

- prevents a distinct recurring trust, authority, execution, persistence, dependency, durability, or evidence failure;
- states protocol/framework/client/persistence preconditions and exceptions;
- names the unsafe transition, side effect, and containment response;
- has a gate that can fail without merely searching for the pattern's name;
- records latency/load/complexity/operational and migration costs;
- exposes a counter-signal for overuse or misplaced enforcement;
- identifies which policy, dependency, runtime, data, traffic, or threat change invalidates adoption.

Promote a candidate after target negative/fault fixtures demonstrate the protected behavior and relevant operations remain reviewable. Adapt it when an existing platform control provides equivalent enforcement. Retire or narrow it when it creates split authority, hidden retries, unbounded resources, or ceremony without preventing a distinct failure.

Good use: a callback path maps provider identity and target account authorization, stores idempotency with the state change, bounds transient retries, and proves malformed, forbidden, timeout, duplicate, and redelivery behavior. Bad use: an agent says score 95 proves a coroutine framework or security library is 95 percent safer. Conditional reuse: a platform authorization filter can satisfy the chain implicitly, but target resource/tenant denials and downstream side effects still need evidence.

Future calibration must separate conformance from outcome. Conformance asks whether boundaries, side effects, and rejection gates exist and work in the target matrix. Outcome research asks whether comparable services reduce incidents, escapes, or recovery cost under defined threats and workloads. Only bounded evidence can support a new empirical ranking.

## Idiomatic Thesis Synthesis Statement

**Governing thesis:** A secure and resilient Kotlin backend preserves one explicit protected transition across untrusted ingress, authentication, authorization, domain invariants, coroutine/blocking execution, transactions and side effects, dependency failure, retries/idempotency, durable work, and operational recovery. Configuration presence, successful requests, coroutine syntax, or eventual retry success are insufficient when denial, cancellation, duplication, overload, restart, or secret-handling behavior is wrong.

Evidence labels are used narrowly:

- `local_corpus_sourced_fact`: one mapped 137-line local source establishes inherited guidance for the listed security/resilience topics; it does not establish target policy, installed behavior, or measured effectiveness.
- `external_research_sourced_fact`: no refreshed fact of this type was created. All four public URLs remain `unrefreshed_no_browse` because browsing was prohibited.
- `combined_evidence_inference_note`: local guidance plus security/distributed-systems reasoning supports the pipeline below; target adoption still requires repository, platform, negative/fault, operational, and owner evidence.

**Evidence-to-protected-transition pipeline**

| conversion | required input | emitted artifact | gate before promotion | failure state |
| --- | --- | --- | --- | --- |
| Request -> protected outcome | Actor, client/protocol, resource/asset, intended read/write, consequence, and owner. | Bounded transition, success, non-goals, and open policy decisions. | Product/domain/security owner confirms intended behavior and authority. | Clarify, threat-sketch, prototype, or owner route. |
| Outcome -> trust/authority model | Inbound bytes/claims/credentials, topology, identity, tenant/resource/state, and privilege. | Trust-boundary map with authentication, authorization, and deny behavior. | Every consequential authority decision has one owner and negative state. | No implementation may invent permission. |
| Authority -> validation/failure contract | Transport schema, normalization, domain invariants, conflicts, dependency and unexpected failures. | Typed input/denial/failure taxonomy and stable safe response. | Each class has external semantics, internal cause/log/metric handling, and retryability. | Generic mapper/catch is nonaccepting. |
| Failure contract -> execution model | Request/workflow lifetime, child work, blocking calls, deadlines, concurrency, shutdown, and sibling dependence. | Structured scope, cancellation, dispatcher/executor, timeout, and backpressure rules. | Cancellation and blocking behavior are target-observable and preserve side-effect safety. | Simplify architecture or route runtime diagnosis. |
| Execution -> side-effect integrity | Persistence, transaction, operation identity, duplicates, ordering, partial failure, and reconciliation. | Transaction/idempotency/deduplication and response-replay contract. | Concurrent duplicate and failure behavior can be inspected atomically. | Unsafe retry/write remains blocked. |
| Side effects -> dependency recovery | Provider/client contract, credentials, correlation, timeout/deadline, error classes, retry and fallback. | Stable client port plus bounded recovery/exhaustion behavior. | Fault sequence preserves authority, remaining budget, side-effect count, and truthful response. | Fail/degrade/route instead of blind retry. |
| Request work -> durable work | Need to outlive request/process, delivery/ack model, concurrency, terminal failure, and restart. | Worker/job durability and redelivery contract. | Restart/duplicate/parking or dead-letter plus graceful shutdown evidence exists. | Request-scoped fire-and-forget is rejected. |
| Contracts -> repository-native implementation | Current Spring/Ktor/runtime/security/persistence/client/worker conventions and versions. | Minimal code/configuration under existing ownership boundaries. | Build/static/unit checks plus integrated security/failure harness pass. | Reuse/migration or implementation revision required. |
| Implementation -> negative/fault evidence | Malformed/denied/cancelled/timed-out/duplicate/overloaded/restarted scenarios and safe data. | Direct request/message, log/metric, state/effect, and recovery evidence. | Gates fail for representative unsafe state and pass after the correct premise changes. | Fix, narrow, reject, or specialist route. |
| Evidence -> operational acceptance | Threat/consequence, support/load environment, telemetry, rollout/rollback, residual risk, and owners. | Proceed, scoped proceed, revise, reject, or escalation decision. | Evidence depth and production controls match policy and consequence. | Acceptance remains blocked or explicitly limited. |

The pipeline fails early. A retry library cannot repair an authorization policy no owner chose. A cancellation test cannot make a nontransactional duplicate write safe. A threat checklist cannot prove deployed security-chain behavior. Production telemetry cannot retroactively justify shipping a known forbidden transition.

**Operational principles**

1. **Model a protected transition, not a generic endpoint.** Name actor, resource/tenant/state, side effect, consequence, denial, and recovery.
2. **Treat all inbound data as untrusted at its boundary.** Parse and constrain transport shape, then recheck cross-field and stateful invariants after authentication/normalization where the domain owns them.
3. **Separate authentication from authorization.** A valid credential identifies under a contract; it does not by itself permit an action on a resource.
4. **Keep enforcement ownership explicit.** Spring method security or Ktor route/plugin checks can be useful under a coherent convention; scattered checks create gaps and conflicting decisions.
5. **Protect credentials and sessions across failures.** Raw passwords/tokens/session/reset/authorization material must not escape through logs, exceptions, metrics, traces, fixtures, or debug responses.
6. **Match CSRF controls to client and credential context.** Cookie-authenticated browser flows and non-browser bearer clients have different boundaries; the label "API" is not analysis.
7. **Preserve structured cancellation.** Parent/request/workflow cancellation and deadlines should stop owned children; supervisor isolation must be intentional; broad catches must not swallow cancellation.
8. **Be honest about blocking.** JDBC/JPA/file and blocking SDK calls remain blocking inside `suspend`; isolate them deliberately or use a simple blocking architecture under bounded resources.
9. **Retry only classified replay-safe work.** Transience, deadline/load budget, side-effect safety, backoff policy, attempt visibility, and terminal behavior must all be explicit.
10. **Make duplicate handling transactional where needed.** Store operation identity with state change when possible and define response replay/conflict/reconciliation; do not claim exactly-once from protocol labels.
11. **Give external clients stable failure boundaries.** Normalize provider errors, set target-owned time budgets, preserve correlation, hide credentials, and test malformed as well as ordinary error responses.
12. **Use durable execution for durable obligations.** Critical work that outlives request/process belongs in an owned queue/job platform with bounded concurrency, redelivery, terminal handling, and lag/failure signals.
13. **Prove denials and failure behavior.** A representative unsafe state should make the gate fail before the implementation is trusted.

**Strong defaults without dogma**

| principle | useful interpretation | misuse to reject |
| --- | --- | --- |
| Deny by default | Unknown/missing/insufficient authority cannot perform a protected action; responses remain safe and observable. | Turning every dependency uncertainty into an unhandled outage or hiding legitimate recovery without policy. |
| Validate at boundaries and domain | Transport shape is checked early; domain invariants remain close to authoritative state. | Repeating inconsistent rules at every layer or treating syntax validation as authorization. |
| Structured concurrency | Parent lifetime and child failure/cancellation are explicit. | Wrapping work in scopes/supervisors without side-effect or sibling semantics. |
| Timeout every external call | Dependency work cannot consume an unbounded request/workflow budget. | Copying arbitrary constants, stacking timeouts past parent deadline, or retrying because timeout occurred. |
| Bounded classified retries | Temporary safe failures can recover without storm or duplicate effect. | Retrying auth, validation, deterministic domain failure, cancellation, overload, or unsafe write. |
| Idempotency for replayable writes | Duplicate requests/deliveries produce a defined single logical outcome. | Treating key existence, HTTP method, or client suppression as transactional exactly-once. |
| Durable background processing | Obligations survive request/process and have redelivery/terminal ownership. | Launching detached fire-and-forget coroutines for critical work. |
| Framework-native security | Current Spring/Ktor mechanisms reduce custom parsing and fit lifecycle. | Delegating product authorization or target verification to framework defaults blindly. |

**Verification modes and blind spots**

| mode | strongest use | blind spot | complement when consequential |
| --- | --- | --- | --- |
| Unit/property test | Parser, validation, domain invariant, error mapping, pure idempotency decision. | Real security chain, transactions, concurrency, provider/runtime behavior. | Integrated request/message and persistence fixture. |
| Framework route/security test | Authentication/plugin/filter/method/route behavior and external response. | Production gateway/identity, actual database race, all client contexts. | Deployed config review, resource authorization, and concurrency tests. |
| Persistence integration | Transaction, uniqueness, idempotency, conflicts, rollback, and state inspection. | Broker/provider/network and production contention. | Duplicate/redelivery and controlled fault evidence. |
| Coroutine/time control test | Cancellation, deadline, sibling isolation, stale completion, and scheduling semantics. | Real blocking dependencies, thread pools, external systems. | Thread/dispatcher trace and integration saturation. |
| Dependency fault fixture | Timeout/error/malformed/cancellation/retry/fallback behavior. | Provider production contract and rare outages. | Versioned provider contract and authorized operational evidence. |
| Log/metric/trace audit | Secret redaction, attempts, correlation, saturation, terminal failure, and recovery. | Missing instrumentation, sampling, privacy, and causal ambiguity. | Direct state/effect evidence and privacy review. |
| Load/saturation/restart exercise | Concurrency bounds, backpressure, blocking starvation, worker durability, and recovery. | Unmodeled production traffic/topology and full adversarial scope. | SLO/operations owner and controlled rollout. |
| Security/domain owner review | Threat/policy/content/risk acceptance and abuse-case challenge. | Hidden implementation defects and stale environment. | Reproducible technical negative/failure evidence. |

Choose the least costly complementary bundle that can expose the pending consequential failure. More tools do not guarantee independence: a route test and service test can share the same mocked principal and miss the same resource-authorization defect.

**False security-resilience checks**

Reject or narrow a claim when:

- actor, asset/resource, side effect, client context, or policy owner is absent;
- signed or parsed claims are treated as resource authorization;
- only allowed/authenticated happy paths are tested;
- validation, auth, domain, conflict, dependency, and unexpected failures collapse into one retryable exception;
- raw credentials or sensitive payloads can reach logs, traces, errors, fixtures, or metrics;
- CSRF is enabled or disabled without naming browser and credential behavior;
- `CancellationException` can be swallowed or child work escapes its owned lifetime;
- blocking calls run on event-loop-limited execution because a function is `suspend`;
- timeout and retry budgets are copied without parent deadline, dependency, load, and effect analysis;
- write retries lack atomic idempotency/deduplication and response replay behavior;
- critical work is launched from a request without durable ownership;
- a build, annotation scan, or eventual success is reported as production security/reliability;
- a precise latency, throughput, reliability, or risk-reduction number lacks target workload and method;
- a shared platform control changes without consumer, migration, rollback, and operational ownership.

Good example: a tenant-scoped webhook validates transport and provider identity, resolves current account ownership server-side, stores operation ID with state atomically, propagates shutdown/cancellation, bounds transient provider retries, and proves malformed, forbidden, duplicate, timeout, and restart states.

Bad example: a handler accepts a token's tenant claim, launches a global coroutine for the write, catches every throwable, logs the authorization header, and retries after timeout until a success response appears.

Conditional example: a read-only internal health detail can use a simpler transaction/idempotency model when exposure, identity, data sensitivity, blocking cost, and no-write behavior are explicit and tested. That evidence invalidates if writes, external clients, browser access, or tenant data are added.

**Second-order consequences**

The protected transition is an intermediate representation consumed by security configuration, route/controller code, domain authorization, persistence, coroutine scopes, provider clients, workers, tests, telemetry, and runbooks. Missing one failure or authority branch multiplies ambiguity across all consumers.

The evidence also forms an invalidation graph. An identity-provider/key/session change reopens authentication; domain permission or tenant-model change reopens authorization; schema/content change reopens validation; runtime/dispatcher/dependency change reopens cancellation/blocking; transaction/broker/provider change reopens idempotency/retry; deployment/traffic/SLO change reopens operational acceptance. Unrelated verified transitions can remain intact.

Kotlin backend security resilience is therefore not a single framework, score, or checklist finish. It is controlled coherence across trust, authority, execution, effects, dependency failure, durability, and operation, with explicit contradiction and recovery when a premise changes.

## Local Corpus Source Map

The local corpus contains one concise Kotlin backend security/resilience detail file. Read it completely for every new consequential transition. Use the map to route decisions and preserve caveats; do not convert its bullets into target policy or current framework claims automatically.

**Content-family inventory**

| family | local path | observed identity | read strategy | authority boundary |
| --- | --- | --- | --- | --- |
| Kotlin backend security and resilience | `agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/references/kotlin-backend-security-and-resilience.md` | 137 lines; SHA-256 `8a07eb77e27a3b508224db76c60e20508b8b3d13b81fce86e87ea052be7d14a5`. | Read complete body for new durable security/failure work; reuse hash-bound locators for focused unchanged-source tasks. | Specialist local guidance, not target permission policy, installed framework proof, cryptographic parameter authority, threat completeness, SLO, or production acceptance. |

**Complete source-section routing**

| source heading | load when the pending question is | useful contribution | required caution and next evidence |
| --- | --- | --- | --- |
| Opening | Whether this source applies to validation, auth, external calls, retries, idempotency, cancellation, or failure behavior. | Defines intended topic trigger. | Trigger intent does not prove target fit; inspect actor/asset/side effect and current repository. |
| `Trust Boundaries` | Which inbound values require parsing/validation and where domain invariants live. | Names body, route/query, headers, cookies, claims, messages, environment, and provider data as untrusted; separates transport shape from domain invariants. | Determine actual topology, sources, normalization, sensitivity, schema, and stateful authority in target. |
| `Authentication And Authorization` | How Spring/Ktor identity and permission paths should remain explicit and negatively tested. | Recommends explicit configuration/plugins, deliberate principal extraction/authorization, and missing/malformed/expired/insufficient tests. | Framework/version/configuration and business authorization convention remain target-specific; inspect full deployed chain. |
| `Passwords, Tokens, And Sessions` | How credential storage/logging, reset, rate-limit, enumeration, and cookie concerns enter review. | Supplies conservative secret/session control categories and defers parameters to current platform/security approval. | Do not copy algorithm parameters, cookie policy, lifetimes, or public error behavior without current owner/client/threat evidence. |
| `CSRF And Browser Context` | Whether ambient browser credentials make cross-site requests consequential. | Ties CSRF to cookie-authenticated browser context and warns against disabling it without a client/auth rationale. | Map actual browser/non-browser clients, credentials, CORS/origin and framework chain; "API" is not enough. |
| `Input Validation` | Where DTO parsing, structural checks, normalization, domain conversion, cross-field/stateful invariants, and safe errors belong. | Provides layered validation model and nonleaking error boundary. | Validate mass-assignment/unknown-field/coercion/content-size and target domain behavior as applicable; validation is not authorization. |
| `Coroutine Resilience` | How parent/child failure, cancellation, supervisor isolation, and timeouts should behave. | Preserves structured concurrency and cancellation; warns against broad throwable catches and accidental sibling semantics. | Verify installed coroutine/runtime/framework scopes and side effects; no syntax alone proves behavior. |
| `Blocking And Dispatchers` | Whether blocking dependencies run in coroutine/event-loop paths. | Calls JDBC/JPA/file work blocking and permits appropriate dispatcher/executor or intentionally simple blocking design. | Identify real dependency behavior, thread pools, bounds, shutdown, and saturation; dispatcher changes are not infinite capacity. |
| `Retries` | Whether a failure may be retried and how load/deadline/side effects are bounded. | Limits retry to transient infrastructure, excludes validation/auth/deterministic domain, asks backoff/jitter, budgets, attempts, and idempotency/outbox for writes. | Choose target policy from dependency, workload, deadline and transaction; cancellation/overload are not automatically retryable. |
| `Idempotency` | Which payment-like writes, webhooks, consumers, callbacks, or client retries need duplicate control. | Recommends transactional coupling where possible and defined duplicate response replay. | Define key scope/auth binding, storage lifecycle, concurrency, body/result compatibility, conflict and reconciliation; do not claim exactly-once casually. |
| `External API Clients` | How provider calls should be isolated and fail. | Recommends a port, connect/read/total timeouts, normalized errors, correlation, credential hygiene, and broad success/failure tests. | Match current provider/version/client library, parent deadline, rate-limit/retry contract, malformed payload and fallback/product policy. |
| `Background Work` | Whether work must outlive request/process and how workers handle delivery. | Distinguishes durable processing from request fire-and-forget and requires idempotency, bounded concurrency, failure classes, terminal handling, and metrics. | Verify broker/scheduler persistence, ack/transaction, restart/redelivery, ordering, shutdown, retention, lag and operations ownership. |
| `Security And Resilience Review Checklist` | Final challenge across boundaries, failures, secrets, retries, timeout, cancellation, blocking, and durability. | Supplies a concise cross-topic review floor. | A checklist is an index; each active item needs target authority and rejection evidence. |

The headings are causally linked. A timeout may trigger retry; a retry may duplicate a write; idempotency may require transactional persistence; cancellation or restart may interrupt that transaction; worker redelivery may repeat the operation under a different request context.

**Source-to-operational translation**

| local guidance | preserved intent | operational boundary | capable target evidence |
| --- | --- | --- | --- |
| Treat inbound data as untrusted. | Do not let transport or external claims enter domain/state changes unchecked. | Trust level, normalization, schema, size, source, and sensitivity vary by protocol/topology. | Malformed/boundary/property fixtures and target domain-invariant checks. |
| Keep security configuration explicit and test auth negative paths. | Identity and permission must be visible and deny correctly. | Product authorization and installed Spring/Ktor chain are not supplied by the reference. | Full-chain missing/malformed/expired/invalid/insufficient/resource/tenant tests. |
| Never log credentials and use approved password/session controls. | Avoid credential compromise and abuse-friendly flows. | Current algorithms/parameters/lifetimes/cookies/rates/error language need platform/security/client authority. | Config/storage/log capture plus abuse and session lifecycle evidence. |
| CSRF depends on client context. | Match protection to ambient credential and browser threat. | Cookie, bearer, origin, browser, gateway, CORS, and framework details matter. | Client/auth model and cross-site negative behavior under deployed config. |
| Separate transport validation and domain invariants. | Keep parse errors early and business truth near authoritative state. | Layering must avoid duplicated contradiction and unsafe normalization order. | DTO/domain conversion, cross-field/state/authorization and stable error tests. |
| Preserve structured concurrency/cancellation. | Owned work stops with its parent/deadline unless isolation is intentional. | Persistence/external side effects may need shielded/transactional completion or reconciliation rather than casual detachment. | Parent/child cancellation, timeout, supervisor, stale-completion and effect-count tests. |
| Isolate blocking work or choose a blocking architecture. | Do not starve constrained event-loop/runtime threads under false nonblocking claims. | Dispatcher/executor sizing and architecture need workload and runtime evidence. | Thread trace, pool saturation, cancellation/shutdown and target performance study. |
| Retry only classified transient work. | Recovery must not repeat deterministic or unauthorized operations or exceed budget. | Transience, deadline, idempotency and backpressure are dependency/operation-specific. | Fault sequence, fake-time scheduling, attempt/effect/exhaustion and load evidence. |
| Couple idempotency to state change where possible. | Duplicate delivery should produce one logical effect and defined response. | Atomicity depends on database/broker/outbox/transaction semantics and failure windows. | Concurrent duplicate, rollback, restart/redelivery and stored record/state inspection. |
| Use durable processing for durable work. | Request/process lifetime must not own critical obligations. | Delivery, acknowledgment, ordering, retention, terminal handling and operations differ by platform. | Restart, redelivery, duplicate, concurrency, lag, shutdown and recovery exercise. |

**Target corpus to inspect before implementation**

For an established service, inspect the complete relevant portions of:

- user/repository instructions and current product/domain/security/privacy requirements;
- deployment topology, gateway/proxy, routes/controllers/plugins/filters/security chains, and client types;
- principal/claim mapping, resource/tenant authorization, method-security convention, and denied response mapping;
- DTO/schema/parsers/normalizers and domain commands/invariants;
- password/token/session/reset/cookie/key handling and redaction/logging/telemetry configuration;
- coroutine scopes, exception boundaries, supervisors, timeouts, dispatchers/executors, blocking dependencies, and shutdown;
- persistence/transactions/constraints/outbox/idempotency records and migration/cleanup behavior;
- external client ports/configuration, credential storage, provider contracts, rate limits and error normalization;
- broker/scheduler/worker durability, ack/redelivery/dead-letter or parking, concurrency and lag;
- unit, framework, integration, persistence, fault, duplicate, load/restart, security and operational tests;
- rollout, telemetry, SLO, alert, incident, rollback/replay and accountable owner decisions.

Do not load every file or sensitive production artifact indiscriminately. Select complete semantic modules and safe evidence that can change the pending transition, and record why other candidates were excluded or inaccessible.

**Observed tensions and synthesis**

| local guidance pressure | target-system counterpressure | synthesis |
| --- | --- | --- |
| Keep authorization explicit. | Platform convention centralizes checks in gateway/filter/method policy. | Use the current single authoritative convention, but prove target resource/tenant denials and avoid split ownership. |
| Propagate cancellation. | A committed/critical side effect may need atomic completion or durable handoff. | Preserve request cancellation while making transaction/durable transfer and response reconciliation explicit; do not detach silently. |
| Isolate blocking work. | Service and dependencies are entirely blocking and operationally bounded. | Prefer coherent bounded blocking architecture to fake nonblocking layers; measure before migration. |
| Retry transient infrastructure. | Dependency overload and deadline exhaustion make more attempts harmful. | Require remaining budget, dependency guidance, coordinated backpressure and terminal state before retry. |
| Store idempotency with state change. | Cross-system effect cannot share one transaction. | Use outbox/saga/reconciliation or narrower guarantee; expose partial state and do not claim atomic exactly-once. |
| Use durable background processing. | Best-effort low-consequence telemetry need not block requests or persist indefinitely. | Classify consequence and choose deliberate loss/retention semantics with an owner. |
| Rate-limit login/reset/verification. | Gateway/identity platform already owns distributed limits. | Reuse authoritative control and test integration/visibility; avoid inconsistent per-instance duplicates. |

**Retrieval profiles**

| profile | required local reads | safe stopping point |
| --- | --- | --- |
| Focused correction | Current instructions/policy, exact target module/config, nearest failure/negative test, governing source heading and direct consumers. | Defect is reproduced, corrected, denied/failure behavior passes, and no shared contract broadens. |
| Standard protected transition | Complete local source plus complete target trust/auth/validation/execution/persistence/dependency/worker modules and relevant tests. | Transition, failure/recovery, side effects, and no-claim boundary are reviewable. |
| Shared platform control | Standard reads plus service/consumer inventory, version/configuration, migration history, governance, rollout, observability and rollback. | Supported consumers and operational owner are explicit. |
| Incident/recovery | Current deployment/runtime evidence, exact failed transition, logs/metrics/traces under policy, changes/history, local headings relevant to hypotheses. | Cause/containment/recovery and invalidated controls are bounded. |
| Historical comparison | Archive source, target past/current versions, incidents/decisions and deployment context. | Temporal claim separates observed changes from inferred rationale/effect. |

**Map integrity rules**

1. Verify source path/hash/headings before relying on its content.
2. Read the complete body for every new consequential transition.
3. Treat framework and algorithm examples as dated guidance, not current target values.
4. Preserve client-context, cancellation, blocking, retry, and transactional caveats beside mechanisms.
5. Reconcile source defaults with target policy, installed versions, runtime, persistence, provider, and worker contracts.
6. Bind selected guidance to negative/fault fixtures and actual side-effect/recovery evidence.
7. Rebuild the map after source hash, product/security policy, framework/runtime, persistence, provider, or worker changes.
8. Escalate to broader target and specialist reads when the transition affects shared controls or high-consequence assets.

Good retrieval: an engineer changing a webhook reads the whole source, maps provider identity and account authorization, inspects transaction/idempotency storage and worker redelivery, then verifies malformed, forbidden, duplicate, timeout, and restart paths. Bad retrieval: the engineer copies all retry bullets into middleware and applies them to every exception. Conditional use: a team can standardize one coroutine/client pattern after installed-version, blocking, cancellation, side-effect, load and owner evidence make it platform policy.

## External Research Source Map

No external query or page retrieval was performed. Every URL is preserved exactly from the seed with state `unrefreshed_no_browse`. The local fact is that the seed associates each pointer with a role; current content, branch/release, version, authority detail, route stability, and target applicability are unknown until a future authorized refresh.

**Decision-bound external queue**

| external_source_url_value | seed role | trigger to refresh | primary question | required target closure | current state |
| --- | --- | --- | --- | --- | --- |
| `https://kotlinlang.org/docs/home.html` | Kotlin language/type-system documentation pointer. | A compiler/language/nullability/type/exception/interoperability rule is version-sensitive and changes boundary implementation. | For the installed compiler/toolchain, which exact language contract governs the target code and Java/framework interoperability? | Match compiler/build flags and reproduce accepted/rejected target behavior without expanding into security policy. | `unrefreshed_no_browse` |
| `https://github.com/Kotlin/kotlinx.coroutines` | Coroutine library/repository pointer. | Cancellation, timeout, supervisor, dispatcher, context, testing, or release behavior affects a protected transition. | Which installed-version contract governs parent/child cancellation, failure propagation, timeout, context, and blocking isolation? | Match dependency/runtime/framework scope and run positive, cancellation, timeout, sibling, stale-completion, and blocking tests as applicable. | `unrefreshed_no_browse` |
| `https://github.com/spring-guides/tut-spring-boot-kotlin` | Spring Boot Kotlin application example pointer. | A known Spring Boot/Kotlin integration or upgrade question affects wiring, route, validation, persistence, or test setup. | What narrow maintained example or versioned contract informs the installed Spring Boot stack, and what belongs to Spring Security or local policy instead? | Inspect dependency/config/security chain and prove target allowed/denied/failure behavior; examples cannot authorize production design. | `unrefreshed_no_browse` |
| `https://ktor.io/docs/welcome.html` | Ktor framework documentation pointer. | Ktor authentication/plugin/routing/status/coroutine/testing/deployment behavior is version-sensitive and decision-relevant. | Which exact installed-version Ktor contract governs plugin order, principal extraction, route protection, failure response, and lifecycle? | Match configuration and run missing/malformed/valid/insufficient credentials plus cancellation/failure tests in target. | `unrefreshed_no_browse` |

These are hypotheses about where primary evidence may live. They do not assert feature existence, current branch content, installed compatibility, or security suitability.

**Local-first and external-first routes**

| situation | first move | external move | stop condition |
| --- | --- | --- | --- |
| Existing transition behavior is clear | Read target config/source/tests and exercise denied/failure state. | Do not browse unless public version/support changes the decision. | Local evidence settles the bounded claim without portability assertion. |
| Known dependency upgrade caused mismatch | Freeze lock/build, wrappers/plugins, runtime, deployment config, and exact symptom. | Retrieve official release/migration/API material for the involved versions. | Change is confirmed/reproduced or remains version-ambiguous with owner route. |
| New coroutine pattern is proposed | Define parent lifetime, children, side effects, blocking dependencies, deadline, sibling semantics, and cancellation evidence. | Retrieve only exact installed-version contracts needed. | Target cancellation/failure/blocking fixtures pass without stale/duplicate effect. |
| New Spring/Ktor auth path is proposed | Define actor, credential/client, resource authorization, negative states, and current platform policy. | Retrieve feature/version-specific primary docs or maintained source under authorization. | Full target chain denies missing/malformed/insufficient access and permits intended access. |
| Framework comparison is exploratory | Record trust, lifecycle, persistence, testing, operations, ecosystem/maintenance, and migration criteria. | Time-box primary-source candidate discovery. | No production contract changes until selected candidates are implemented and fault-tested. |
| Required identity/gateway/provider/production environment is unavailable | Preserve blocked claim and consequence. | Documentation cannot substitute for inaccessible target enforcement. | Access changes, scope narrows under owner acceptance, or route is rejected. |

**Source-quality ladder**

| source class | strongest use | limitation |
| --- | --- | --- |
| Versioned official language/API/manual/specification | Establish publisher-supported contract for a named version/date. | Does not prove local wrapper/configuration/deployment or product policy. |
| Official release notes, migration guide, or maintained source history | Explain changed behavior and compatibility boundaries. | Unreleased/default-branch behavior or implementation detail may not be supported contract. |
| Installed package source/types/bytecode/lock/build help | Establish actual local capability and integration shape. | Can omit support guarantees and runtime/deployment behavior. |
| Controlled route/coroutine/persistence fixture | Establish causal behavior for selected state/configuration. | Does not prove all principals, threats, load, topology, or production failures. |
| Representative protected service transition | Establish bounded applicability to actor/resource/side-effect/recovery. | Remains scoped to selected environment and failure population. |
| Maintainer issue/community example/discussion | Generate terminology, alternatives, edge-case hypotheses. | Not final authority; confirm through primary and target evidence. |

**External evidence promotion protocol**

1. State the blocked Kotlin backend claim and consequence of being wrong.
2. Confirm browsing authorization, sensitive-data/security boundaries, and acceptable source classes.
3. Record exact query, access date, publisher/maintainer, direct URL, title/section, branch/release/version, and source class.
4. Paraphrase only the narrow contract needed, including prerequisites, defaults, and limitations.
5. Match compiler, dependency, wrapper/plugin/security chain, build, runtime, persistence, provider, and deployment configuration.
6. Reproduce a positive and relevant negative/failure case in a safe target fixture or record why environment authority is unavailable.
7. Compare with product/security policy, repository convention, actual side effects, and operational constraints.
8. Decide adopt, adapt, reject, no change, or escalation required.
9. Name producer release, local dependency/configuration, identity/policy, persistence/provider, runtime, or deployment change that invalidates the result.

Finding a plausible page or code sample completes retrieval only. Refresh completes when the extracted claim confirms or changes a bounded target decision under explicit applicability.

**Refresh result card**

| field | required content |
| --- | --- |
| `research_identifier` | Stable link to protected transition and unresolved trust/execution/failure claim. |
| `trigger_and_consequence` | Why producer behavior matters to authorization, side effect, recovery, compatibility, or release. |
| `retrieval_identity` | Query, direct source, publisher, access/publication date, version/branch/release, section, and source class. |
| `narrow_claim` | Bounded paraphrase with prerequisites, defaults, and exclusions. |
| `target_identity` | Service revision, compiler/dependencies, wrappers/plugins, security/config, runtime, persistence, deployment, and fixture. |
| `reproduction` | Positive, denied/failure, conflicting, unavailable, or not-applicable result. |
| `decision_effect` | Requirement, configuration, implementation, test, runbook, or explicit no-change outcome. |
| `counterevidence` | Local source, target behavior, version difference, product/security policy, incident, or owner constraint. |
| `invalidation` | Producer/local/policy/runtime/deployment change that reopens the result. |
| `owner_and_next_action` | Accountable reviewer, follow-up mechanism, recovery, and stop condition. |

**Research failure states**

| failure | response |
| --- | --- |
| URL unavailable or moved | Search within official publisher/maintainer only under authorization, retain old pointer historically, and do not invent continuity. |
| Current page/default branch lacks version identity | Record access date/commit when appropriate, narrow the claim, and rely on installed source plus target reproduction. |
| Official contract conflicts with target behavior | Verify dependency/runtime/config/wrapper/security chain; preserve both and route compatibility or diagnosis. |
| Guide/example appears sufficient | Read surrounding primary contract and exercise relevant denial/failure; examples often omit security, transaction, and operations boundaries. |
| Maintainer issue/community guidance is sole source | Keep as hypothesis and require target fixture plus owner review for consequential action. |
| Restricted identity/provider/production behavior cannot run safely | Preserve blocked evidence and define required authorized environment; do not use public docs as deployed proof. |
| External result does not affect decision | Close/retire item rather than add ceremonial citation or code. |

Good coroutine research use: cancellation behavior differs after a known dependency/runtime change. The engineer freezes versions and scope ownership, retrieves the exact primary contract, reproduces parent/child/cancellation and side effects, and updates the target regression.

Good Ktor/Spring research use: missing or insufficient credentials traverse a changed filter/plugin path unexpectedly. The engineer records installed versions and configuration, retrieves exact versioned guidance, tests the actual chain and resource authorization, and updates only the affected integration.

Bad research use: "Kotlin, coroutines, Spring, and Ktor documentation prove this service is secure, nonblocking, and production-ready." Documentation roots cannot establish product permission, target configuration, blocking dependencies, transaction/idempotency, runtime load, or incident recovery.

Conditional exploration: a team may compare Spring Boot and Ktor before selection. The result is a candidate matrix, not an adopted framework, until target build, auth/validation, coroutine/blocking, persistence, failure, operations, maintenance, and migration evidence exists.

**Queue lifecycle**

- Prioritize a release blocker or consequential mismatch before a planned upgrade or exploratory item.
- Assign one owner and one decision effect to each active research question.
- Close an item when installed source and target fixtures settle it more directly.
- Retire a pointer when the dependency/integration disappears, preserving historical rationale.
- Refresh event-driven claims after relevant producer or installed-version/configuration change; do not invent periodic schedules.
- Preserve prior retrieval identity when guidance changes so earlier decisions remain interpretable.

The external map is a queue of falsifiable future questions, not current source attribution. Success includes not browsing when target code and negative/failure evidence already answer the narrower question.

## Anti Pattern Registry Table

Use this registry to find the earliest failed premise and change what the service may execute or claim. A matched label is not a root cause by itself. Preserve the actor, input, resource, state, revision, environment, side effects, and direct evidence needed to distinguish alternatives.

**Common containment and recovery**

1. Stop or narrow the affected transition, retry, worker, rollout, or security/reliability claim.
2. Preserve safe evidence: request/message shape, principal/claims without raw secrets, target resource/state, configuration revision, logs/metrics/traces, attempts, and persisted effects.
3. Identify the earliest layer: product/policy, trust/input, authentication, authorization, failure mapping, coroutine/blocking, transaction/idempotency, dependency, worker, verification, or operation.
4. Contain user/system harm with a truthful deny, fail, degrade, pause, rollback, or parking route; do not destroy diagnostic state.
5. Correct the nearest authoritative contract or route the missing policy/environment to its owner.
6. Replay the original unsafe/failure state plus an allowed or neighboring state; count effects and inspect recovery.
7. Promote a preventive primitive or shared gate only when the mechanism is recurring, severe, transferable, owned, and migration-safe.

**Cross-cutting backend anti-pattern registry**

| anti_pattern_failure_name | stage and mechanism | observable signal | consequence | safer default and containment | release evidence |
| --- | --- | --- | --- | --- | --- |
| `context_free_security_summary` | Orientation: agent emits generic Kotlin hardening without local source or target transition. | Advice could apply unchanged to any service. | Wrong framework/policy/lifecycle assumptions and wasted implementation. | Stop; define actor/asset/side effect, read local source and target contracts. | Reviewer connects each control to one target failure or policy. |
| `source_authority_blending` | Evidence: source, remembered public behavior, target observation, policy, and inference share one voice. | No retrieval/version/owner/fixture boundary. | Unsupported security or production claim becomes hard to challenge. | Type claims and preserve unknown/conflicting states. | Claim-to-source/target/owner audit passes. |
| `public_pointer_as_current_fact` | Research: retained URL is treated as opened/current/version-matched. | Recommendation cites root link without retrieval record. | Stale or inapplicable framework/runtime behavior enters code. | Keep `unrefreshed_no_browse`; retrieve narrowly only under authorization. | Direct source identity plus installed-version positive/negative reproduction. |
| `trusted_transport_or_claim_input` | Trust: body/path/header/cookie/JWT/message/provider/environment value enters domain unchecked. | Parser or signature success is called validation. | Injection, invalid state, cross-boundary confusion, or unsafe effect. | Parse/limit at edge, normalize deliberately, recheck domain invariants. | Malformed/boundary/cross-field/stateful fixtures reject safely. |
| `authentication_equals_authorization` | Authority: valid credential is treated as permission for route/resource/tenant/action. | Tests cover unauthenticated only; resource ownership absent. | Horizontal/vertical privilege violation and cross-tenant access. | Keep authn and server-owned authz decisions explicit. | Allowed plus wrong-role/resource/tenant/state negative tests. |
| `client_or_gateway_only_permission` | Authority: UI hiding or undocumented gateway rule is sole protection. | Direct service invocation succeeds without local/declared enforcement. | Bypass path performs protected action. | Document authoritative gateway and enforce defense required by architecture; never trust UI. | Direct and routed negative tests under deployed topology. |
| `scattered_authorization_ownership` | Design: filter, annotation, controller, service, query, and client each make partial decisions. | Inconsistent outcomes across paths or tests. | Permission gaps, duplicate policy, and unreviewable migration. | Choose one coherent convention with explicit supporting checks at boundaries. | Policy-to-enforcement map and all entry-path denials pass. |
| `credential_secret_log_leak` | Observability: passwords/tokens/session/reset/auth headers/provider credentials or sensitive payloads reach logs/traces/errors. | Captured success/failure output contains raw or reversible secret. | Credential compromise, privacy incident, and unsafe diagnostics. | Redact at source, keep nonsecret correlation, restrict evidence access, rotate/contain if exposed. | Log/serialization/exception/metric tests across failure paths. |
| `account_enumeration_response_split` | Public auth flow: existence changes message/status/timing/rate behavior without approved policy. | Login/reset/verify responses reveal account presence. | Targeted abuse and privacy leak. | Use owner-approved public semantics and internal correlation; rate-limit authoritative layer. | Existing/nonexisting abuse fixtures and operational control evidence. |
| `csrf_context_assumption` | Browser security: CSRF is disabled/enabled based on "API" label rather than credential/client behavior. | Cookie-auth browser route has no rationale/negative test or bearer flow receives irrelevant ceremony. | Cross-site unauthorized state change or brittle clients. | Model ambient credentials, browser/nonbrowser clients, origins and framework chain. | Cross-site/config/credential negative behavior under target deployment. |
| `transport_validation_as_domain_policy` | Validation: DTO constraints replace cross-field/state/business/authorization invariants. | Structurally valid command violates current state or resource policy. | Invalid or unauthorized side effect. | Convert validated transport to domain command after auth/normalization and recheck authoritative invariants. | Structural plus stateful/domain and permission negative fixtures. |
| `internal_error_detail_exposure` | Response mapping: stack/class/provider/database detail leaks to clients. | Error body reveals internals, secrets, SQL, host, or class names. | Information disclosure and unstable public contract. | Stable bounded error response; preserve detailed cause only in protected diagnostics. | Contract tests and sensitive-string scan across unexpected/provider failures. |
| `catch_every_throwable_boundary` | Coroutine/failure: broad catch maps all failures without preserving cancellation/fatal semantics. | `CancellationException` becomes ordinary failure/retry/success or child continues. | Wasted work, stale effect, shutdown delay, false recovery. | Catch expected classes narrowly; rethrow cancellation; central unexpected handling remains truthful. | Parent/timeout cancellation and unexpected-failure tests. |
| `detached_unstructured_coroutine` | Lifecycle: global/ad-hoc scope launches request or critical work without owner. | Work outlives request/shutdown, loses context, or disappears on restart. | Secret/context leak, duplicate/stale effect, lost obligation. | Structured request/workflow scope or durable worker depending required lifetime. | Cancellation/shutdown/restart and effect-state evidence. |
| `supervisor_without_sibling_contract` | Lifecycle: supervisor isolates failures by default without defining independent siblings. | One child fails while dependent siblings commit or report aggregate success. | Partial inconsistent result and hidden failure. | Use ordinary structured scope unless isolation, aggregation, and recovery are explicit. | Sibling fault fixture verifies intended partial/aggregate semantics. |
| `suspend_means_nonblocking` | Execution: JDBC/JPA/file/blocking SDK runs on event-loop-limited context because function is `suspend`. | Thread trace shows blocking; latency/queue rises under concurrency. | Starvation, timeout cascade, and unavailable service. | Isolate blocking on bounded executor/dispatcher or choose coherent blocking architecture. | Thread/pool saturation, cancellation and shutdown evidence. |
| `unbounded_coroutine_fanout` | Capacity: input creates unlimited child tasks or provider/database calls. | In-flight work, memory, connections, or rate-limit errors grow with input/traffic. | Self-induced overload and dependency harm. | Bound concurrency/queue, propagate cancellation, coordinate backpressure and deadline. | Saturation fixture proves maximum in-flight and truthful rejection/degradation. |
| `independent_timeout_budget_stack` | Deadlines: each layer starts full timeout without parent remaining budget. | End-to-end work exceeds request/job deadline and late children complete. | Resource leak, stale response/effect, retry amplification. | Propagate deadline/remaining budget and define terminal cancellation/reconciliation. | Fake-time/trace test covers nested client and persistence phases. |
| `retry_every_exception` | Recovery: validation/auth/domain/conflict/cancellation/unexpected errors enter generic retry policy. | Same deterministic failure repeats; denied action generates load. | Storm, delayed truth, repeated effects, incident masking. | Classify transient infrastructure separately; terminal failures expose correction/escalation. | Fault matrix asserts attempts by class and no retry for forbidden classes. |
| `nested_retry_amplification` | Recovery: gateway/client/service/worker each retries independently. | Downstream attempts multiply beyond visible top-level budget. | Dependency overload, latency explosion, difficult attribution. | Assign one owner or coordinate budgets/attempt metadata across layers. | End-to-end fault fixture counts all physical attempts and exhaustion. |
| `unsafe_write_retry_without_idempotency` | Side effect: timeout/unknown completion causes mutation replay without deduplication. | Duplicate rows, charges, notifications, callbacks, or state transitions. | Financial/data/user harm and difficult reconciliation. | Stop retry, contain exposure, add transactionally scoped idempotency/outbox or explicit reconciliation. | Concurrent timeout/duplicate fixture proves one logical effect and response. |
| `nontransactional_idempotency_record` | Persistence: key record and state change commit independently. | Crash/failure leaves consumed key without effect or effect without key. | Lost operation or duplicate effect on replay. | Couple atomically where possible; otherwise define recoverable state machine and reconciliation. | Failure injection at each commit window plus restart/replay inspection. |
| `unscoped_or_unbound_idempotency_key` | Authority: key is not bound to actor/resource/operation/body/version or retained appropriately. | Collision replays another principal/result or key reuse masks changed command. | Cross-user disclosure, wrong response, or denied legitimate work. | Define authenticated scope, request fingerprint policy, lifecycle, conflict, and safe replay. | Cross-principal/body/concurrent/expired-key negative tests. |
| `provider_error_leaks_domain_boundary` | Client: raw status/classes/payloads/credentials escape through domain or public response. | Controllers branch on provider internals or client sees raw provider detail. | Coupling, information leak, unstable recovery. | Port/interface with normalized typed errors, protected diagnostics, and correlation. | Relevant success/error/malformed/timeout/redaction contract tests. |
| `external_call_without_total_budget` | Dependency: connect/read/call can occupy request/worker indefinitely or beyond parent deadline. | Hung child, exhausted thread/connection, shutdown stall. | Cascading saturation and unavailable recovery. | Target-owned connect/read/total/deadline behavior with cancellation and terminal response. | Controlled hang/slow phases, remaining-budget and cleanup tests. |
| `request_fire_and_forget_critical_work` | Durability: request handler launches critical notification/write/callback without durable handoff. | Success response precedes durable ownership; process restart loses work. | Silent obligation loss and false success. | Persist/enqueue transactionally under owned worker or keep request synchronous with truthful outcome. | Crash/restart at handoff window and eventual state/recovery evidence. |
| `unbounded_worker_delivery_loop` | Worker: concurrency, retry, lag, poison-message, or shutdown behavior is undefined. | Hot retry, queue lag, memory/connection growth, stuck partition/message. | Outage amplification and unbounded failure backlog. | Bound concurrency/attempts, classify failures, park/dead-letter, expose lag and operator action. | Poison/transient/duplicate/restart/saturation/shutdown fixtures. |
| `mocked_security_false_green` | Verification: tests inject principals or bypass filters/plugins/transactions/providers. | Unit suite passes while deployed chain denies/permits differently. | Unsafe rollout and misplaced confidence. | Keep unit speed but add integrated chain and negative resource tests at claim boundary. | Representative full-stack denial and failure fixture fails under injected defect. |
| `configuration_presence_as_proof` | Verification: annotation/plugin/timeout/retry/idempotency table existence is checked without behavior. | Search/lint passes despite wrong order/scope/transaction or no effect. | Ceremonial controls and hidden runtime failure. | Assert external transition, internal state/effect, logs/metrics, and recovery. | Controlled wrong configuration makes the promised gate fail. |
| `copied_security_or_latency_threshold` | Measurement/policy: seed/example number becomes target requirement without method/owner. | Precise value lacks workload, threat, environment, sample, or policy provenance. | False assurance, wrong tuning, or blocked legitimate service. | Keep proposal unexecuted; run target study or obtain current policy. | Measurement card and owner decision with bounded scope. |
| `stale_evidence_reuse` | Lifecycle: source/config/test/runbook result is reused after identity/policy/dependency/topology change. | Old hash/version/environment differs but status remains green. | Obsolete control or recovery guides release. | Invalidate dependent claims and replay selected negative/fault evidence. | Staleness injection proves prior acceptance downgrades visibly. |

**Severity and handling**

| class | meaning | default response |
| --- | --- | --- |
| Advisory | A reversible implementation/evidence choice could be clearer but protected outcome remains intact. | Record rationale and improve without inventing a blocker. |
| Implementation blocking | Target code cannot demonstrate trust, lifecycle, side-effect, or failure contract safely. | Stop dependent implementation promotion and add/fix the nearest capable evidence. |
| Release blocking | Forbidden access, credential leak, duplicate/lost consequential effect, unbounded resource, or missing recovery affects supported path. | Contain and block release/scope until target negative/fault and owner gates pass. |
| High-assurance stop | Qualified security/privacy/domain/operations authority or realistic production evidence is required and unavailable. | Route with exact evidence request; no local framework default may accept residual risk. |

**Registry admission and maintenance**

Add an entry only when the mechanism is observed or strongly supported, recurs or has serious consequence, exposes a stable target signal, and offers safer behavior plus replayable evidence. Preserve an unclassified state for novel threats and failures. A registry entry passes when a controlled target or fixture shows that its gate rejects the defect and releases only after the correct premise changes.

Good recovery: an external write times out and a retry creates duplicate records. The team stops automatic replay, bounds exposure, adds transactionally scoped operation identity and response replay, injects failure around commit, and verifies one logical effect plus truthful terminal behavior. Bad recovery: increase retries and suppress duplicate-key exceptions. Conditional supervisor: sibling isolation is valid when outputs are independent, partial results are explicit, cancellation and aggregate status are defined, and a child fault fixture proves that behavior.

The registry feeds security chains, domain authorization, validators, coroutine/executor helpers, transaction/idempotency primitives, client ports, worker runtimes, negative fixtures, observability, and runbooks. Retire rules whose complexity exceeds the distinct failure they prevent or whose semantics moved into a stronger owned platform control.

## Verification Gate Command Set

`verification_gate_command_set`: Select gates by the protected transition and evidence population. Run cheap identity/structural checks first, repository-native source and unit checks next, integrated denials/faults after that, and controlled load/restart/operational review only when the claim requires them.

**Gate dependency order**

| gate | property checked | evidence produced | what a pass does not prove | failure response |
| --- | --- | --- | --- | --- |
| A. Environment and authority | Correct root, newest instructions, owned paths, data/credential boundary, product/security owners, allowed side effects. | Preflight and authority record. | Source freshness, intended policy, or runtime safety. | Stop before writes, network, migrations, or secret access. |
| B. Frozen identity | Seed/source hashes, target revision/dirty state, compiler/dependencies/config, security chain, schema/migrations, runtime/deployment identity. | Reproducible input manifest. | That current policy or implementation is correct. | Mark stale and reconcile rather than guessing. |
| C. Packet/reference integrity | Exact headings/questions/fields, normalized uniqueness, expansion, evidence boundaries, and hygiene. | Focused evolution result. | Target backend security or resilience. | Fix the atomic section before continuing. |
| D. Project static/build | Repository-native compile, static, formatting, unit, configuration, migration/schema, and packaging properties. | Source/build evidence under target profile. | Deployed auth chain, transactions, cancellation, external systems, or capacity. | Repair source/config or narrow claim. |
| E. Trust/auth/validation | Parsing, normalization, authentication, authorization, domain invariants, safe responses, and secret handling. | Allowed plus malformed/missing/expired/insufficient/resource-denied behavior. | Coroutine, persistence, provider, worker, or production behavior. | Block protected transition and fix/reroute policy. |
| F. Coroutine/blocking lifecycle | Parent/child failure, cancellation, timeout/deadline, supervisor semantics, blocking isolation, concurrency, shutdown. | Controlled execution/thread/effect evidence. | Transaction atomicity or provider production contract. | Simplify/fix scope or execution model before retry/load. |
| G. Transaction/idempotency | Commit/rollback, duplicate/concurrent operation, key scope, response replay, conflict, and reconciliation. | Persistence state and logical effect count under failure windows. | Cross-system exactly-once or broker/provider behavior not in fixture. | Stop unsafe retry; repair atomicity or narrow guarantee. |
| H. External client/recovery | Provider success/error/malformed/timeout/cancellation, correlation, redaction, retry/backpressure/fallback. | Stable client/domain behavior and physical attempt count. | Every provider outage, rate, or production network. | Correct client/recovery or preserve unavailable evidence. |
| I. Worker durability | Enqueue/handoff, ack/transaction, redelivery/duplicate, concurrency, terminal parking/dead-letter, restart/shutdown, lag. | Durable state and recovery under chosen platform. | Production retention/capacity or incident readiness. | Repair handoff/worker or block durability claim. |
| J. Load/observability/operation | Bounds, saturation, queues/pools, error/retry/timeout/lag, secret-safe logs/metrics/traces, rollback/replay and owner action. | Controlled workload and operational evidence. | Unmeasured traffic, attacks, topology, or future reliability. | Reject target/SLO claim or route operations/security. |
| K. Handoff/invalidation | Changed paths/config/migrations, evidence, residual risk, rollback, owners, and changed-premise replay. | Bounded proceed/revise/reject/escalate decision. | Permanent validity. | Block completion until reconstructable. |

**Current 202607 shared structural checks**

These read-only tests validate shared inventory and hygiene properties without requiring other owners to complete every reference:

```bash
python3 -m pytest -q \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_inventory_matches_specification \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_owner_mapping_unique \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_assignment_manifests_match \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_packet_content_uniqueness \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_reference_placeholders_absent
```

The complete module also checks all 99 references, packets, and shared queue rows. While other owners are active, preserve the exact external unfinished population rather than editing another lane.

```bash
python3 -m pytest -q tests/test_idiomatic_reference_evolution.py
```

**Assignment-focused verifier contract**

After each atomic section and after the complete reread, assert:

- all 26 reference headings retain exact levels, text, and seed order;
- every evolved section is strictly longer than its matching seed section;
- packet contains 26 exact section headings and 260 exact question headings;
- every question has six ordered nonempty fields;
- all 1,560 values are unique raw and after current context-prefix normalization;
- outputs are ASCII with final newline, balanced fences/tables, no tabs/trailing whitespace, and no prohibited placeholders;
- frozen seed/local-source and all assignment queue-span hashes remain unchanged;
- only authorized reference, packet, and Delta journal paths changed.

This proves the evolution contract. A complete semantic reread proves that packet conclusions inform the reference. Neither proves target security/resilience.

**Scoped diff check**

```bash
git diff --check -- \
  idiomatic-ref-202607/kotlin_backend_security_resilience-20260710.md \
  idiomatic-reference-evolution-work/delta/packets/kotlin_backend_security_resilience-20260710-question-packets.md \
  idiomatic-reference-evolution-work/delta/progress.md
```

**Legacy archive verifier**

The seed command is preserved only for the 202606 generated archive:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

Its implementation does not certify this 202607 packet or a Kotlin service. Report it as historical archive-generation evidence only.

**Target project gate discovery**

This reference cannot name one universal Kotlin command. Before execution:

1. Read repository instructions and inspect Gradle/Maven wrappers, settings/build files, version catalogs, compiler/plugins, source sets, and scripts.
2. Identify the actual application/framework/runtime, security configuration, persistence/migrations, provider clients, brokers/workers, test containers/fixtures, and deployment profiles.
3. Discover repository-native static, unit, framework, integration, migration, security, coroutine, persistence, worker, load, and packaging commands.
4. Record command side effects: network, credentials, databases, migrations, ports, queues, containers, files, and long-lived processes.
5. Use isolated synthetic data and target profiles; never run destructive or production commands without explicit authorization.
6. Record which command observes which transition claim and which important boundary remains mocked or unavailable.

| pending claim | likely gate family | mandatory rejection question |
| --- | --- | --- |
| DTO/parser/domain validation | Unit/property/schema plus target error contract. | Would malformed, oversized/boundary, unknown/coerced, cross-field, and invalid-state input fail at the intended layer? |
| Authentication chain | Framework route/security integration. | Do missing, malformed, expired/invalid, and valid credentials traverse the real filter/plugin/configuration? |
| Resource/tenant authorization | Full-chain route/service/persistence negative tests. | Can a valid principal access another role/tenant/resource/state through any entry path? |
| Secret/session handling | Log/serialization/config/storage and abuse-flow review. | Could raw credential/session/reset/provider material escape during success or exception? |
| Browser/CSRF model | Framework/config integration and cross-site/client fixture. | Does the declared browser credential model justify the control and reject the harmful case? |
| Failure response | Unit/contract/framework integration. | Are validation/auth/domain/conflict/dependency/unexpected classes safe externally and distinct internally? |
| Coroutine cancellation | Coroutine test scheduler/time control plus integration. | Does parent/timeout/shutdown cancellation stop owned children and preserve `CancellationException`? |
| Blocking isolation | Thread/dispatcher/executor trace and saturation. | Can blocking dependency starve event-loop/constrained threads or outlive cancellation? |
| Timeout/deadline | Fake-time/controlled slow dependency and trace. | Do nested phases respect parent remaining budget and clean up late work? |
| Retry/backpressure | Fault sequence, fake time where applicable, and saturation. | Are attempts limited to classified replay-safe failures with bounded physical calls and terminal state? |
| Idempotent write | Real persistence/transaction plus concurrent duplicate/failure injection. | Can any commit/crash window create effect-without-key, key-without-effect, or cross-principal replay? |
| External client | Simulated service or controlled provider sandbox plus redaction. | Do relevant status, malformed, timeout, cancellation, retry, and correlation paths normalize safely? |
| Durable worker | Broker/scheduler/container integration with restart/redelivery. | Does critical work survive process loss, avoid duplicate effect, bound concurrency, and reach terminal handling? |
| Performance/capacity | Controlled workload under frozen environment with security/functional equivalence. | Is the same actor/state/effect/failure contract measured, including errors, retries, saturation, and cleanup? |

**Negative and fault evidence matrix**

For each consequential transition, identify applicability and exact fixture for:

| dimension | candidate states |
| --- | --- |
| Input | Missing, malformed syntax, boundary size/range, unknown/coerced fields, cross-field conflict, invalid current state. |
| Identity | Missing, malformed, invalid signature/session, expired/revoked where supported, valid credential. |
| Permission | Wrong role/scope/tenant/resource owner/state, disabled account, stale permission, direct-entry bypass. |
| Browser/session | Cross-site request, cookie attributes/lifetime, logout/revocation/reset, enumeration/rate-limit behavior as applicable. |
| Coroutine | Parent cancellation, timeout, child failure, sibling failure, supervisor branch, stale completion, shutdown. |
| Blocking/capacity | Slow/blocking dependency, pool/connection exhaustion, bounded concurrency, queue rejection/degradation. |
| Persistence | Validation after read, conflict, rollback, concurrent update, duplicate operation, crash windows, response replay. |
| Provider | Connection/read/total timeout, relevant client/server errors, malformed body, cancellation, retry exhaustion, correlation/redaction. |
| Worker | Enqueue failure, restart before/after ack, redelivery, poison message, concurrency, dead-letter/parking, graceful shutdown. |
| Observability/recovery | Secret redaction, attempts/effects/correlation, saturation/lag, rollback/replay, owner escalation, stale evidence. |

Do not require every generic state for every transition. Require every state whose omission can change authorization, side effects, durability, or the claimed recovery.

**Gate-harness verification**

| injected defect | expected rejection |
| --- | --- |
| Duplicate normalized packet answer | Focused packet uniqueness gate fails. |
| Changed seed heading or unexpanded section | Reference evolution gate fails. |
| Valid principal accesses another tenant/resource | Authorization gate blocks the transition. |
| Raw token appears in exception log | Secret evidence gate fails and containment/rotation route activates as policy requires. |
| Broad catch consumes parent cancellation | Coroutine lifecycle gate fails despite ordinary error mapping passing. |
| Blocking call runs on constrained event-loop thread | Execution/saturation gate fails. |
| Timeout followed by duplicate write | Idempotency/transaction gate fails even when retry eventually returns success. |
| Provider malformed body leaks raw exception | Client normalization/response gate fails. |
| Process dies after request success but before critical work ownership | Durability gate fails. |
| Faster candidate omits authorization or error handling | Functional/security equivalence rejects performance adoption. |

Good use: source/static/unit checks pass, but an integrated wrong-tenant request succeeds. The denial gate blocks only dependent transitions, the enforcement boundary is corrected, and allowed plus denied and side-effect evidence reruns.

Bad use: the archive verifier exits successfully and the agent declares a Spring or Ktor service secure, cancellation-safe, idempotent, and production-ready.

Conditional partial use: a pure domain validator can rely on focused unit/property evidence when transport/auth/persistence are explicitly outside the function. Broader route/security claims require the missing integrated gates.

Verification is an invalidation graph. Product permission changes reopen authorization; dependency/runtime changes reopen cancellation/blocking; transaction/schema changes reopen idempotency; provider/broker changes reopen retry/durability; deployment/traffic/SLO changes reopen operation. Selective replay is stricter and cheaper than ignoring a red gate or rerunning everything blindly.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference to decide how a bounded Kotlin backend transition should preserve authority, effect safety, failure semantics, and operational proof. A theme keyword is only a discovery hint. Activation depends on the behavior being changed.

**Activation Decision**

Open this reference when at least one answer is yes:

1. Does untrusted data enter through an HTTP route, message, callback, scheduled trigger, configuration value, identity claim, or provider response?
2. Can the change read or mutate a protected resource, emit an external effect, disclose sensitive data, or alter who may act?
3. Can timeout, cancellation, retry, duplicate delivery, process restart, or partial commit change the result?
4. Does the task claim secure, resilient, idempotent, durable, production-ready, or non-blocking behavior that needs observable proof?
5. Does a framework or infrastructure default need to be reconciled with local policy rather than accepted implicitly?

Do not run the complete workflow solely because a file is Kotlin or contains an authentication term. A pure, isolated, behavior-preserving edit may use its normal focused checks. If discovery shows that a seemingly small edit changes transaction scope, caller retry behavior, principal mapping, or secret exposure, activate this guide at that point.

**Protected-Transition Unit**

Scope the work around one observable state transition, not automatically around one class or ticket:

```text
untrusted trigger
  -> authenticated identity or trusted system actor
  -> authorization and domain preconditions
  -> bounded effect and commit point
  -> externally visible response or durable acknowledgement
  -> retry, cancellation, duplicate, and restart behavior
```

Name the actor, target resource, permitted effect, commit point, failure classes, and replay identity. If any of those cannot yet be named, the task remains in orientation or policy resolution rather than implementation.

**Agent State Model**

| State | Entry condition | Required work | Exit evidence |
|---|---|---|---|
| `orienting` | The relevant route, worker, client, or policy owner is not yet known. | Read local conventions, trace the entry point and effect path, and list unresolved ownership. | A bounded transition and evidence map exist. |
| `policy_or_threat_blocked` | Authority, retention, identity, cryptographic, or incident policy is unresolved. | Preserve current behavior or apply only an approved reversible containment; route the decision to its owner. | A recorded decision identifies the rule, owner, and affected gates. |
| `contract_specified` | Actor, resource, effect, failure classes, and replay behavior are explicit. | Write positive, negative, duplicate, timeout, cancellation, and restart acceptance cases as applicable. | Tests or equivalent executable checks fail for the expected pre-change reason. |
| `implemented` | Contract evidence exists and the minimal behavior is present. | Keep framework adapters thin, enforce domain invariants at the owning layer, and preserve cancellation and transaction boundaries. | Focused positive checks pass without weakening denial or fault cases. |
| `negative_verified` | The happy path passes. | Exercise absent, malformed, expired, unauthorized, cross-tenant, and information-leak cases relevant to the transition. | Every applicable rejection has a stable, non-leaking result and no protected effect. |
| `fault_verified` | Denial behavior is established. | Exercise timeout, cancellation, transient failure, duplicate delivery, partial dependency failure, and restart where relevant. | Effects are bounded, retry classes are explicit, and replay behavior is deterministic. |
| `operationally_ready` | Code-level evidence is green. | Verify redaction, correlation, metrics, alerts, deployment compatibility, rollback, and any required migration. | A reviewer can connect each claim to current repository or operational evidence. |
| `invalidated` | A claim-critical dependency changed after evidence was recorded. | Reopen only checks affected by authority, transaction, replay, deadline, dependency, or secret-handling changes. | Replacement evidence is current and unaffected checks remain traceable. |

Readiness is not a one-way label. For example, changing an idempotency key derivation reopens duplicate and replay checks but need not erase unrelated input-shape evidence. Changing principal mapping reopens authorization and audit attribution even if endpoint serialization did not change.

**Usage Modes**

| Mode | Suitable entry condition | Minimum output | Escalate when |
|---|---|---|---|
| Planning | Behavior is requested but design is unsettled. | Protected-transition map, policy questions, alternatives, acceptance matrix, and verification plan. | No accountable owner can decide a claim-critical policy. |
| Focused repair | One bounded defect has a known expected behavior. | Reproducing check, minimal correction, adjacent negative case, and scoped regression evidence. | The defect exposes a wider shared-boundary failure. |
| Implementation | A new or changed transition has approved behavior. | Executable contracts, implementation, denial and fault evidence, and operational handoff. | Persistence, identity, or deployment contracts must change outside the owned component. |
| Review | Existing code makes safety or resilience claims. | Findings ordered by effect severity, evidence gaps, and exact verification needed. | The review requires inaccessible production facts or authority decisions. |
| Incident recovery | Harm is active or likely and rapid containment is required. | Reversible mitigation, observed evidence, blast-radius statement, rollback trigger, and deferred gate owner. | Incident command, forensic preservation, credential rotation, or provider coordination is required. |
| Shared platform | A library, filter, authentication component, client policy, or worker runtime affects multiple services. | Compatibility map, migration plan, representative consumer checks, rollout guardrails, and rollback. | Consumers have conflicting policy or runtime requirements. |
| High assurance | Effects are irreversible, regulated, financially material, or broadly exposed. | Independent policy approval, threat review, adversarial tests, durable audit evidence, and staged release proof. | Required review authority or evidence is unavailable. |

Mode changes evidence breadth, not the definition of correctness. Every claimed property still needs an acceptance condition; a low-risk mode simply has fewer applicable claims and dependencies.

**Default Agent Sequence**

1. Start with the local corpus source map and repository-specific conventions.
2. Define one protected transition and classify exposure, effect severity, reversibility, and dependency fan-out.
3. Resolve or explicitly route policy ownership before inventing authorization, identity, retention, or compromise-response rules.
4. Specify success, denial, malformed input, duplicate, timeout, cancellation, and restart behavior where applicable.
5. Capture failing pre-change evidence for the intended contract.
6. Implement the smallest coherent change without moving domain policy into framework glue.
7. Run positive, negative, fault, and replay gates in dependency order.
8. Verify secret redaction, correlation, metrics, deployment compatibility, and rollback evidence.
9. Record what is locally supported, what was observed in the target repository, what was approved by an owner, and what remains uncertain.

An emergency may enter at containment, but it must record skipped stages and the owner and trigger for returning to them. Urgency changes order; it does not convert missing evidence into proof.

**Route Before Proceeding**

| Unresolved decision | Appropriate owner or adjacent workflow | Work that may continue safely |
|---|---|---|
| Who may perform an effect, under which business conditions | Product/domain policy owner plus security review when exposure warrants it | Map existing behavior, write characterization checks, and identify denial cases. |
| Identity-provider claims, key rotation, token issuance, or trust federation | Identity/platform security owner | Keep claim parsing isolated and avoid assuming undocumented claim meaning. |
| Encryption algorithms, signing protocol, key custody, or compromise response | Security/cryptography authority | Preserve evidence and apply only approved, reversible containment. |
| Transaction isolation, schema uniqueness, deduplication retention, or outbox migration | Data/persistence owner | Specify duplicate and partial-commit outcomes and model migration hazards. |
| Queue capacity, dead-letter policy, deployment rollback, or incident thresholds | Operations/platform owner | Add bounded instrumentation and deterministic failure classification. |
| Latency, throughput, or saturation target | Service owner with workload and capacity evidence | Define a reproducible measurement method without inventing a target. |

**Minimum Agent Handoff**

Every completed use should leave:

- the bounded transition and actor/resource/effect model;
- evidence sources with claim-level status;
- policy decisions and accountable owners;
- applicable success, denial, duplicate, timeout, cancellation, and restart outcomes;
- changed paths and gates actually run, including meaningful configuration;
- unresolved uncertainty, selective invalidation triggers, rollout guardrails, and next action.

Good invocation: "Make the signed provider callback update one tenant's invoice exactly once; the signature policy is owned by Platform Security, and retries may arrive after a timeout." The agent can map authority, tenant binding, transaction and idempotency boundaries, replay semantics, and fault tests.

Bad invocation: "Make authentication production-ready." The scope, policy, protected effect, framework, threat, and acceptance evidence are unknown; the correct first result is an orientation packet, not a readiness claim.

Borderline invocation: "Add a two-second timeout to this repository call." First determine whether the call blocks a coroutine thread, whether cancellation reaches the dependency, whether a transaction remains open, and whether the caller retries. Activate the full guide only for the newly exposed transition risks.

Treat external material as a freshness and ecosystem check, never as a replacement for local contracts. Because no browsing was performed for this edition, external entries cannot establish current versions or defaults. Preserve evidence labels whenever guidance is reused.

## User Journey Scenario

**Role-based opening scenario:** A Kotlin backend builder owns an endpoint that receives signed invoice-payment callbacks from an external provider. The provider may retry after a timeout, two deliveries may overlap, and the service must update only the intended tenant's invoice. The builder needs to decide whether the endpoint can complete synchronously or must durably accept work before acknowledgement.

This is an illustrative reasoning scenario, not a claim about a particular provider, signature algorithm, framework version, status code, or deployment. The target repository and approved provider contract must supply those details.

**Starting state**

- The endpoint accepts an untrusted request body and signature-related headers.
- A payload contains a provider event identifier, an external account reference, an invoice reference, an event type, and event data.
- A locally configured provider account maps to one tenant; payload text is not itself authority for that mapping.
- The business effect is to record a payment transition at most once within a defined replay horizon.
- A duplicate must not repeat the effect, even when two deliveries race.
- Logs and metrics may identify a bounded correlation value but must not expose signatures, raw authorization material, full payloads, or sensitive payment fields.
- The provider's timeout, retry schedule, signed representation, timestamp policy, event-ID scope, and required response semantics remain assumptions until verified from owned evidence.

**Decision being made:** Choose the smallest coherent transition whose acknowledgement corresponds to durable, replay-safe state. The choice is between completing the local effect in one bounded request transaction and durably accepting an authenticated event for later idempotent processing.

**Journey boundary**

```text
provider delivery
  -> bounded raw request capture
  -> authenticity and freshness decision
  -> structural parse and domain conversion
  -> provider-account-to-tenant binding
  -> resource authorization and state preconditions
  -> replay reservation plus business effect or durable work record
  -> commit
  -> stable acknowledgement
  -> possible provider retry, service restart, or worker recovery
```

The endpoint must not let a later stage retroactively justify an earlier one. Successful JSON parsing does not establish authenticity. A valid signature does not authorize an invoice in another tenant. A known invoice does not establish that the event is new. A successful local commit does not prove that the provider received the response.

**Step-by-step user journey**

1. The provider sends a callback. The adapter applies configured body and header bounds before expensive parsing or cryptographic work. Oversized or structurally impossible input is rejected without logging the sensitive raw body.
2. The adapter verifies the exact representation and freshness rules required by the approved provider contract. Verification occurs before untrusted event fields drive protected lookups or state changes. Failure produces no business effect and a deliberately non-leaking response.
3. After authenticity succeeds, the adapter parses a transport DTO and converts it into a domain command. Structural validation reports bounded errors; domain conversion rejects impossible identifiers, unsupported event types, and invalid cross-field combinations.
4. The service resolves the configured provider identity and maps its external account to a local tenant. A tenant string inside the payload may be checked for consistency but cannot grant authority.
5. The service resolves the invoice through a tenant-scoped query and checks that the authenticated provider account may report this transition for that resource. Missing, foreign, and unauthorized resources return policy-approved outcomes without revealing cross-tenant existence.
6. The service derives a replay identity from a provider-scoped event identifier or another approved key. The key's scope, normalization, retention, and collision behavior are part of the contract, not incidental string handling.
7. In one database transaction, the service reserves the replay identity under an enforced uniqueness rule and applies the allowed state transition. If a remote side effect is needed, the same transaction records an outbox entry or durable work item instead of making an unprotected network call inside an uncertain transaction.
8. After commit, the endpoint returns the configured acknowledgement. If the connection disappears after commit, the provider may retry; the uniqueness and replay path return a stable duplicate result without repeating the effect.
9. If processing was durably deferred, a bounded worker claims the record, performs an idempotent transition, classifies failures, and records retry or parking state. A process restart must rediscover accepted unfinished work from durable storage.
10. Operators observe accepted, rejected, duplicate, transient-failure, permanently-failed, and aged-work counts through redacted telemetry. Correlation supports investigation without turning a replay key or secret into a broadly visible identifier.

**State and outcome table**

| Observed state | Decision | Protected effect | Durable evidence | Response behavior |
|---|---|---|---|---|
| Body exceeds configured bound | Reject before full processing. | None | Bounded rejection metric, subject to cardinality policy. | Stable client error defined by the adapter contract. |
| Signature or freshness check fails | Reject as unauthenticated. | None | Redacted failure category; no signature value. | Policy-approved non-leaking failure. |
| Authenticated body cannot form a valid command | Reject as malformed or unsupported. | None | Bounded validation category. | Stable contract error without internal exception detail. |
| Provider account is unknown or inactive | Reject or quarantine according to owned policy. | None | Auditable provider-identity decision. | Deliberately avoids tenant enumeration. |
| Invoice is absent, foreign, or not authorized | Deny the transition. | None | Tenant-safe denial category. | Does not disclose another tenant's resource. |
| Event is new and transition is allowed | Reserve replay identity and commit the effect or durable intent. | Exactly one local transition within the stated replay scope. | Replay row, state mutation, and optional outbox/work row in one commit. | Success only after the promised durable state exists. |
| Same event arrives sequentially | Load the recorded replay outcome. | No additional effect. | Existing replay evidence remains authoritative. | Stable duplicate acknowledgement chosen by contract. |
| Same event arrives concurrently | Database uniqueness or equivalent atomic arbitration selects one winner. | One winner may apply the effect; all others observe duplicate state. | One committed reservation and result. | Each delivery receives a deterministic allowed outcome. |
| Cancellation occurs before commit | Roll back the transition and propagate cancellation. | None committed. | No false success record. | Connection may end; a later retry can attempt normally. |
| Connection fails after commit but before response is observed | Preserve committed result. | No effect on retry beyond replay lookup. | Committed replay outcome proves prior acceptance. | Retry receives the duplicate-compatible result. |
| Durable worker encounters a classified transient dependency failure | Release or reschedule within bounded policy. | No repeated committed remote effect unless its own idempotency contract permits it. | Attempt count, next eligibility, and redacted error class. | Request acknowledgement remains truthful because work was durably accepted. |
| Durable worker encounters a deterministic or exhausted failure | Park or dead-letter according to owned policy. | No blind retry loop. | Failure state with investigation context and retention. | Operator workflow, not automatic endless replay, owns recovery. |
| Event arrives after replay retention expires | Apply the explicitly chosen late-replay policy. | Depends on domain evidence; never assume novelty solely because the record expired. | Retention boundary and resulting decision are observable. | Stable response defined for late replay. |

**Two coherent acknowledgement models**

| Model | Use when | Commit before response | Principal advantage | Principal risk and required control |
|---|---|---|---|---|
| Synchronous local completion | Verification and one local transaction fit comfortably inside the provider deadline. | Replay reservation and local effect commit together. | Simple ownership and one visible business-state transition. | Avoid network calls or long blocking work in the transaction; verify timeout and cancellation behavior. |
| Durable acceptance then worker | Processing can exceed the deadline, must survive restart, or requires bounded external work. | Authenticated event plus replay identity and work intent commit together. | Fast truthful acknowledgement and recoverable processing. | Requires worker idempotency, claim/lease recovery, bounded retries, parking, lag telemetry, and data retention. |

Returning success before either commit is not a third model; it is an untruthful acknowledgement because a crash can erase the only copy of accepted work. Likewise, launching an untracked coroutine from request scope does not create durability.

**Illustrative transaction shape**

```kotlin
suspend fun acceptProviderEvent(command: AuthenticatedProviderEvent): ReplayOutcome =
    transactionRunner.inTransaction {
        val tenant = providerAccounts.requireMappedTenant(command.providerAccount)
        val invoice = invoices.requireTenantInvoice(tenant, command.invoiceReference)
        paymentPolicy.requireAllowedTransition(invoice, command.eventType)

        replayStore.insertOrLoadOutcome(
            provider = command.providerIdentity,
            eventKey = command.replayKey,
        ) {
            val updated = invoices.applyPaymentTransition(invoice, command.payment)
            outbox.recordRequiredEffects(updated, command.correlation)
            ReplayOutcome.Accepted(updated.version)
        }
    }
```

This sketch communicates boundaries, not a ready implementation. The target data layer must establish whether `insertOrLoadOutcome` is atomic under concurrent delivery and whether transaction cancellation rolls back cleanly. The domain must define replay response data, resource-state conflicts, late events, and out-of-order transitions.

**Unsafe contrast**

```text
parse payload
  -> trust payload tenant
  -> call remote dependency
  -> update invoice
  -> insert duplicate marker
  -> return success
```

This order permits unauthenticated lookup work, cross-tenant confusion, a remote effect outside local atomicity, and a race before the duplicate marker. Moving only the duplicate insert earlier is insufficient if it commits separately and strands an event that never applied its effect.

**Verification journey**

| Check | Fault placement or input | Expected observation |
|---|---|---|
| Authentication denial | Invalid, missing, stale, or policy-incompatible signature material. | No protected lookup driven by payload authority, no mutation, and no secret in output or telemetry. |
| Tenant isolation | Authenticated provider account paired with another tenant's invoice reference. | No cross-tenant effect and a non-enumerating policy result. |
| Sequential replay | Submit the same authenticated event after a successful commit. | One business transition and a stable recorded replay outcome. |
| Concurrent replay | Release two authenticated deliveries against the same key at a synchronization barrier. | One committed winner under the actual persistence constraint. |
| Pre-commit failure | Inject persistence failure immediately before commit. | No replay success and no business transition; a retry can proceed. |
| Post-commit response loss | Commit, then sever or fail the response path. | Retry reads the committed outcome and does not repeat the effect. |
| Cancellation | Cancel request scope during verification, waiting, and persistence separately. | Cancellation propagates; transaction and resource cleanup match the documented boundary. |
| Restart recovery | Terminate after durable acceptance and before worker completion. | Restarted worker discovers and safely resumes the unfinished record. |
| Retry exhaustion | Return a classified transient failure until the attempt/deadline budget ends. | Work becomes parked or otherwise terminal according to policy; no hot loop occurs. |
| Redaction | Exercise all denial and provider-error paths with recognizable synthetic secrets. | Logs, traces, metrics labels, and responses contain none of the synthetic secret values. |

Do not summarize this journey as universal exactly-once delivery. The bounded claim is that one owned business transition is protected against duplicate effect for a defined provider/key scope and retention horizon. Remote networks can still make delivery and acknowledgement ambiguous. The design makes that ambiguity recoverable and testable rather than pretending it does not exist.

**Data-lifecycle consequence:** A replay record may be security evidence, operational recovery state, and potentially sensitive linkage at once. Define its minimum contents, access, retention, deletion behavior, and late-replay outcome. Shortening retention changes duplicate-effect protection; extending it changes storage and privacy exposure. That decision therefore belongs in the transition contract and its verification, not only in a cleanup job.

## Decision Tradeoff Guide

Choose security and resilience patterns as a coherent bundle around one protected transition. Every option that removes complexity from one layer transfers authority, state, latency, recovery, or operating cost somewhere else. A decision is incomplete until that receiving layer and its verification are named.

**General default:** Keep framework adapters thin, keep state-dependent authorization and domain invariants at their owning application/domain boundary, use one coherent execution model, create durable state before acknowledging durable work, classify and bound retries, make write replay explicit, and expose redacted structured evidence. These are contextual defaults, not universal prescriptions.

| decision_surface | recommended_default | choose_an_alternative_when | cost_or_risk_moves_to | decisive_evidence_and_revisit_signal |
| --- | --- | --- | --- | --- |
| Authentication versus authorization placement | Let the security framework authenticate and enforce coarse route requirements; let the application/domain layer enforce tenant, resource, relationship, and state-dependent permission. | The component is a pure edge proxy with no domain state, or an independently governed policy engine is the authoritative decision point. | Domain enforcement adds explicit context passing and tests; edge-only enforcement risks divergent or incomplete business policy. | Negative tests for missing identity, wrong role, foreign tenant, wrong resource owner, and forbidden state; revisit when identity or resource ownership changes. |
| Browser CSRF posture | Preserve the framework's protection for cookie-authenticated browser requests and configure it according to the actual client model. | Requests cannot carry ambient browser credentials and another authenticated request-integrity design is proven. | Disabling protection transfers responsibility to token transport, origin controls, cookie settings, and every browser integration. | Cross-origin and missing-token negative tests using the deployed authentication mechanism; revisit when client or credential transport changes. |
| Input validation ownership | Parse and structurally validate transport DTOs at the edge, then convert to domain types and enforce cross-field and stateful invariants in the owning layer. | A generated protocol type already establishes a narrow transport invariant, while domain rules still remain separate. | Edge-only validation duplicates policy and drifts; domain-only parsing leaks transport concerns and weakens bounded errors. | Malformed shape, boundary values, invalid combinations, and state-dependent rejection tests; revisit when schema or domain invariants evolve. |
| Password hashing parameters | Use the current platform or security-approved Argon2id or bcrypt configuration and centralize migration policy. | Compatibility requires verifying legacy hashes and upgrading them after successful authentication under an approved plan. | Custom parameter choices create security review and operational migration obligations. | Approved configuration identity, representative verification cost, legacy migration test, and secret-safe failure behavior; revisit on policy or capacity change. |
| Blocking versus coroutine execution | Choose one coherent service model; if coroutines are used, isolate unavoidable blocking work on an appropriate bounded execution resource. | The service is deliberately blocking end to end and its thread, timeout, and capacity model is measured and supported. | Mixed execution can starve coroutine threads, hide queueing, and break cancellation assumptions; isolation adds dispatch and capacity management. | Thread/dispatcher observations under representative concurrency, timeout and cancellation tests, and pool saturation evidence; revisit when dependency or load shape changes. |
| Request completion versus durable background work | Complete bounded local work in request scope; move work out of scope only after a durable record exists. | The effect fits the request deadline and must commit before response, or the operation is explicitly best-effort and loss is acceptable. | Durable work adds storage, claiming, retries, parking, lag metrics, and retention; request work couples availability to caller lifetime. | Restart between acceptance and completion, duplicate claim, cancellation, and recovery tests; revisit when duration, dependency fan-out, or durability promise changes. |
| Immediate remote call versus outbox/work intent | Commit local state and an outbox or durable intent together when a remote effect must follow a local transition. | The remote operation is read-only, independently retry-safe, or inconsistency is explicitly tolerated and recoverable. | An outbox adds worker and reconciliation operations; direct calls create partial-commit and ambiguous-response exposure. | Failure before and after local commit, remote timeout, replay, and reconciliation evidence; revisit when effect reversibility or provider idempotency changes. |
| Fail fast versus retry | Retry only failures classified as transient, within an end-to-end deadline and attempt budget, with backoff and jitter where concurrency warrants them. | A caller owns retry, the operation is deterministic failure, the write is not replay-safe, or latency budget cannot absorb another attempt. | Local retry adds latency and amplification; no retry transfers transient recovery to callers or operators. | Inject each error class, inspect attempt count and total deadline, and measure concurrent retry load; revisit on provider contract or SLO change. |
| Degrade versus reject | Reject when correctness, authority, or protected-state freshness cannot be established; degrade only to a documented safe capability. | A stale or partial response is acceptable, labeled, bounded, and cannot authorize or mutate protected state. | Degradation creates cache age, disclosure, UX, and reconciliation obligations; rejection reduces availability. | Dependency-outage tests proving the degraded path cannot escalate authority or emit stale writes; revisit when data sensitivity or staleness tolerance changes. |
| Idempotency record versus natural state transition | Persist a replay key and stable outcome transactionally with the effect for retriable state-changing operations. | A constrained state replacement is demonstrably idempotent and duplicate execution has no extra external effect. | Stored keys add uniqueness, retention, privacy, and replay-response policy; natural idempotency requires proof across all secondary effects. | Sequential and concurrent duplicates, timeout after commit, and retention-boundary tests; revisit when event key scope or side effects change. |
| Provider key versus derived replay key | Prefer a provider-scoped stable identifier whose uniqueness and replay semantics are contractually known. | The source lacks such an identifier and an approved canonical derivation can represent the business operation without collision or attacker-controlled ambiguity. | Derived keys add canonicalization, collision, privacy, and migration risk. | Property tests for canonicalization plus concurrency and cross-tenant collision tests; revisit on protocol or normalization change. |
| Optimistic versus pessimistic concurrency | Prefer optimistic version or uniqueness checks for short, low-contention transitions with explicit conflict handling. | Contention is high, ordering is mandatory, and a short bounded lock materially simplifies correctness. | Optimism moves cost to retries and conflict UX; locking moves cost to wait time, deadlock handling, and reduced concurrency. | Contention tests with realistic transaction duration and failure injection; revisit when conflict rate or workload distribution shifts. |
| Gateway versus service rate control | Use gateway controls for broad abuse and connection pressure, plus service-level limits for authenticated actor, tenant, resource, or expensive operation where domain identity is known. | One layer has complete trustworthy identity and can enforce all required dimensions without bypass paths. | Layered controls add policy coordination; gateway-only limits miss domain cost, while service-only limits consume resources before rejection. | Bypass, distributed-node, burst, fairness, and recovery tests using actual key derivation; revisit when routing or identity topology changes. |
| Detailed versus stable external errors | Return a bounded stable error contract and keep diagnostic detail in access-controlled telemetry. | A trusted internal client has an approved richer contract that does not reveal protected existence or secrets. | Minimal errors increase support correlation needs; detailed errors increase enumeration and information-disclosure risk. | Snapshot/contract tests across denial paths plus synthetic-secret scans of responses and logs; revisit when caller trust or support model changes. |
| Rich telemetry versus data minimization | Emit structured event class, bounded outcome, duration, attempt, dependency, and correlation fields without credentials, raw tokens, session IDs, or sensitive payloads. | Additional fields have a defined diagnostic purpose, classification, access policy, and retention. | More detail improves diagnosis but increases leakage, cardinality, storage, and privacy exposure. | Redaction tests, label-cardinality review, access checks, and incident query rehearsal; revisit when payload or observability platform changes. |
| Circuit breaking versus direct bounded calls | Begin with explicit timeout, concurrency bound, and error classification; add a breaker when repeated dependency failure otherwise amplifies load and a safe open-state response exists. | Failure volume is low, calls are isolated, or open-state behavior would be less correct than bounded individual failure. | Breakers add shared state, threshold tuning, half-open probes, and surprising rejection; direct calls can sustain harmful pressure. | Controlled outage and recovery tests including half-open concurrency and fallback correctness; revisit with dependency failure evidence. |

**Selection procedure**

1. Define the actor, protected resource, effect, commit point, acknowledgement, and failure classes.
2. State the simplest option that satisfies those constraints under the known workload.
3. For every alternative, name the complexity removed locally and the component that inherits it.
4. Compare behavior under denial, cancellation, timeout, duplicate delivery, partial commit, restart, and overload, not only normal latency.
5. Choose the option whose obligations have clear ownership and testable evidence.
6. Record a revisit trigger such as contention rate, queue lag, provider contract change, client-model change, or saturation.

**Compatibility constraints**

- Durable acceptance without a recoverable worker is incomplete.
- Retry without write replay safety can multiply effects.
- Coroutine endpoints around blocking dependencies do not become non-blocking by declaration.
- Gateway authentication without resource-level authorization cannot establish tenant ownership.
- An outbox without bounded claim, retry, parking, and monitoring merely moves ambiguous work into storage.
- A stable external error without a correlation path can protect information while making incidents unnecessarily opaque.
- Idempotency retention without a late-replay policy leaves correctness undefined after cleanup.

**Worked choices**

Good: A callback must survive restart and may exceed the sender deadline. The service transactionally records authenticated event identity and work intent, acknowledges only after commit, and verifies worker recovery, concurrent duplicates, bounded retry, parking, and lag alerts. The queue is chosen with its obligations.

Unsafe: A team introduces asynchronous launch only to lower endpoint latency, returns success immediately, and has no durable work record. The design moves caller-owned work beyond request scope but gives it no persistent owner.

Conditional: A small internal service uses blocking JDBC and a blocking web stack. That can remain coherent when thread pools, database capacity, deadlines, and overload rejection are bounded and measured. Introducing coroutines around the same calls would not improve resilience unless the blocking boundary and capacity model change.

**Evidence posture**

| posture | use_when | required_record | principal_warning |
| --- | --- | --- | --- |
| Adopt | The local source constraint matches target architecture and repository evidence confirms its assumptions. | Cite the source claim, target convention, acceptance checks, and result. | Local guidance can still be stale for framework-specific configuration. |
| Adapt | The constraint is sound but framework, workload, persistence, or client model differs. | Separate sourced constraint, observed target fact, chosen inference, and invalidation trigger. | Do not present the combined inference as directly sourced. |
| Defer | Policy authority, production evidence, or claim-critical dependency is missing. | Record the exact unresolved decision, owner, safe interim state, and work that can proceed. | Deferral must not silently become acceptance of current unsafe behavior. |
| Reject | The pattern contradicts owned policy, target evidence, or the protected-transition contract. | Preserve the conflicting evidence and identify the safer alternative and rollback. | A newer or more popular pattern is not enough reason by itself. |

No current external ecosystem check was performed for this edition. External entries elsewhere in the reference remain research routes, not evidence that a framework default or library behavior is current.

## Local Corpus Hierarchy

The hierarchy is claim-specific. The mapped local source is the primary topical evidence for this synthesis, but it is not automatically organization policy, current framework documentation, target-repository fact, or runtime proof. A source role answers what kind of claim an artifact may support; it does not award the entire file a universal rank.

**Confidence warning:** Only one local topical source is mapped. Its breadth improves coverage, but it does not provide independent corroboration. Claims about current APIs, deployed configuration, workload behavior, incident policy, cryptographic parameters, or provider contracts require evidence from their owning lane.

| local_artifact | hierarchy_role | permitted_use | prohibited_inference |
| --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/references/kotlin-backend-security-and-resilience.md` | Primary topical local source; complete file read; SHA-256 `8a07eb77e27a3b508224db76c60e20508b8b3d13b81fce86e87ea052be7d14a5` | Support conceptual security and resilience constraints, review questions, and target discovery requirements. | Does not prove current framework syntax, organization approval, target implementation, production capacity, or passing behavior. |
| `agents-used-monthly-archive/idiomatic-references-202606/generated-references/kotlin_backend_security_resilience.md` | Legacy synthesis seed; SHA-256 `74c1872fa32c445a33abb9458634322c71e71af25b21c59cecc2fa631c53d507` | Preserve the original 26-heading contract, inherited mappings, research routes, and provenance baseline. | Does not independently corroborate the topical source or certify inherited scores and numeric targets. |
| `idiomatic-reference-evolution-spec-202607.md` | Evolution process authority for this edition | Define packet shape, expansion, uniqueness, reread, integrity, and verifier requirements. | Does not decide Kotlin security policy or application architecture. |
| `tests/test_idiomatic_reference_evolution.py` | Executable structural process evidence | Check document structure, packet counts, exact questions, uniqueness, hashes, queue constraints, and related acceptance rules. | A passing document test does not prove a backend implementation is secure or resilient. |
| This evolved reference | Derived synthesis and decision aid | Reconcile source constraints, evidence boundaries, alternatives, examples, and verification guidance. | Cannot cite itself as independent proof of its recommendations or of target behavior. |
| Target repository policy, code, configuration, tests, and run evidence | Required target corroboration; not supplied by this edition | Establish actual framework, service architecture, ownership, executable behavior, and observed results. | Existing code alone does not prove that behavior is intended, safe, or current policy. |
| External source routes in this reference | Unrefreshed research queue because browsing was prohibited | Identify future primary-source freshness checks. | A listed URL is not evidence that its content was opened, current, relevant, or consistent with local policy. |

**Role vocabulary**

| role | meaning_at_claim_level | promotion_or_demotion_rule |
| --- | --- | --- |
| Primary topical | Best mapped local explanation of a conceptual constraint. | Retain while relevant; demote for a claim when owned policy or current primary documentation contradicts it. |
| Supporting implementation | Target code or configuration showing how a constraint is represented. | Promote only after exact path and behavior are inspected; demote when it is dead, bypassed, or the defect under review. |
| Policy authority | Accountable decision governing authorization, identity, retention, cryptography, incident action, or risk acceptance. | Requires an owned and applicable decision record; popularity or code prevalence cannot substitute. |
| Process authority | Specification or test controlling how this reference is produced and accepted. | Applies to document workflow only unless it explicitly owns a topical rule. |
| Runtime evidence | Reproducible test, benchmark, trace, metric, log, or controlled observation. | Preserve environment and configuration; invalidate when workload or runtime assumptions change materially. |
| Legacy context | Earlier synthesis, historical design, or retired implementation useful for provenance. | Use to explain lineage, not to override current authority or evidence. |
| Duplicate | Artifact repeating a claim without independent provenance or observation. | Do not count as corroboration; trace to the common upstream source. |
| Conflicting | Applicable evidence disagrees about behavior, ownership, or recommendation. | Stop confidence promotion, identify the disputed claim, and resolve by responsible authority plus executable evidence. |
| Unrefreshed research route | Candidate external source not opened in this edition. | Promote only after future retrieval, scope review, date/version assessment, and claim extraction. |

**Primary topical heading map**

| source_heading | claim_contribution | what_it_cannot_establish | target_corroboration_needed |
| --- | --- | --- | --- |
| Kotlin Backend Security And Resilience | Frames Kotlin backends as typed boundaries plus explicit failure and operational behavior. | Which target stack, topology, or policy applies. | Build files, service entry points, deployment model, and owned requirements. |
| Trust Boundaries | Treats inbound transport, identity, messaging, environment, and provider data as untrusted until validated. | Exact size limits, schemas, or trust anchors. | Adapter configuration, DTO/domain conversion, identity mapping, and rejection tests. |
| Authentication And Authorization | Supports explicit framework authentication and negative authorization testing, with domain-aware permission enforcement. | Actual principals, role semantics, tenant policy, or framework DSL version. | Security configuration, principal mapping, policy ownership, and resource-level denial tests. |
| Passwords, Tokens, And Sessions | Supports approved password hashing, secret-safe logging, secure session cookies, and bounded sensitive flows. | Current approved parameters, session architecture, or rotation process. | Security policy, dependency/config identity, cookie tests, redaction checks, and operational rotation procedure. |
| CSRF And Browser Context | Establishes that CSRF posture depends on credential and browser client model and should not be disabled blindly. | Whether a target endpoint is browser-reachable or carries ambient credentials. | Deployed client architecture, cookie/token transport, origin behavior, and cross-site negative tests. |
| Input Validation | Separates transport parsing, structural checks, domain conversion, stateful invariants, and stable non-leaking errors. | Concrete domain constraints or external error schema. | DTOs, value types, policy code, stateful integration tests, and response contracts. |
| Coroutine Resilience | Supports structured concurrency, cancellation propagation, and intentional supervision. | Target scope ownership, dispatcher configuration, or library cancellation behavior. | Coroutine call paths, timeout ownership, cancellation injection, and resource cleanup observations. |
| Blocking And Dispatchers | Warns that blocking JDBC, JPA, and file work remains blocking and must fit a coherent architecture or isolated resource. | Pool size, saturation point, or safe dispatcher choice for the service. | Dependency behavior, execution configuration, representative concurrency, and thread observations. |
| Retries | Supports transient-only retry, bounded attempts and deadlines, backoff, jitter, and write safety. | Exact retry count, delay, error taxonomy, or provider tolerance. | Client contract, failure classifier, deadline propagation, attempt telemetry, and fault tests. |
| Idempotency | Supports explicit replay control for payment-like writes, callbacks, webhooks, consumers, and retriable actions. | Key scope, retention, outcome replay, or storage transaction semantics. | Domain contract, schema uniqueness, concurrent duplicate tests, timeout-after-commit tests, and cleanup policy. |
| External API Clients | Supports provider ports, timeouts, error normalization, correlation, redaction, and controlled test matrices. | Current provider behavior, quotas, protocol versions, or service-level objectives. | Client implementation, approved provider documentation, sandbox/controlled service behavior, and operational evidence. |
| Background Work | Supports durable work when processing must survive restart or outlive requests, with idempotent bounded workers and terminal handling. | Queue technology, lease model, capacity, parking policy, or recovery objective. | Persistence/queue design, restart tests, duplicate claims, retry exhaustion, lag metrics, and runbooks. |
| Security And Resilience Review Checklist | Supplies broad review prompts across the preceding themes. | Completion by assertion or proof that every prompt applies. | Applicability decisions and claim-specific gates recorded for the target transition. |

**Source-consumption order**

1. Read the full topical source and identify the exact heading supporting each conceptual constraint.
2. Read target repository instructions, build/configuration files, entry points, policy implementations, persistence constraints, and tests.
3. Identify policy decisions that code and documentation cannot legitimately settle.
4. Build a claim chain from topical constraint to target representation to executable or operational observation.
5. Use external primary-source research only for freshness or ecosystem questions that remain relevant; record date, version scope, and conflict with local evidence.

**Claim ledger format**

| claim | source_role_and_location | freshness_or_scope | target_corroboration | confidence_and_open_condition |
| --- | --- | --- | --- | --- |
| Example: duplicate callbacks do not repeat the invoice transition within the configured retention horizon | Primary topical heading `Idempotency`; target schema and transaction implementation; concurrent replay test | Local source is conceptual; key scope and retention are target-specific | Unique constraint, transaction boundary, two-delivery barrier test, and timeout-after-commit test | High only for the tested store, key scope, and horizon; reopen when any of those change. |

**Conflict procedure**

1. State one disputed claim without blending recommendation, policy, code, and observation.
2. Identify which artifact owns that claim class. Policy decides permitted behavior; primary technical documentation informs mutable API behavior; tests and observations show executable outcomes.
3. Determine applicability, version, environment, and whether two sources share the same upstream origin.
4. Preserve the conflict and reduce confidence until an authorized decision and current gate resolve it.
5. Revalidate dependent claims only; do not discard unrelated evidence.

Good chain: The topical source says cancellation should propagate. Target code shows a coroutine client with an explicit timeout. A fault test cancels the parent and observes client cancellation and transaction cleanup. The recommendation, representation, and outcome have separate evidence.

Bad chain: This evolved reference says retries are resilient, therefore the target client's three attempts are safe. That is circular and ignores error class, deadline, write replay, and provider behavior.

Borderline chain: A repository comment says a route is internal. Treat it as a discovery lead, then verify routing, authentication, network exposure, ownership, and negative tests before using it to lower the threat model.

Refresh the policy lane when ownership or risk acceptance changes, the ecosystem lane when framework or dependency assumptions change, the implementation lane when target code/configuration changes, and the runtime lane when workload or deployment conditions change. This selective hierarchy preserves stable conceptual learning without granting stale details permanent authority.

## Theme Specific Artifact

The theme-specific artifact is a **Protected Transition Review Packet**. It is a semantic schema that can be represented in Markdown, an issue form, tests, or a governed architecture record. It covers one externally observable transition from untrusted trigger to authorized effect, acknowledgement, and recovery.

Use one packet when a single owner can identify the entry point and commit boundary. Split linked packets when independently owned services or queues have distinct authorization, commit, and recovery semantics. A system-wide threat model, data-governance review, cryptographic design, architecture decision, or incident plan remains a linked governed artifact rather than being compressed into this packet.

**Field states**

| state | meaning | completion_effect |
| --- | --- | --- |
| `verified` | Current target evidence supports the field and its assumptions. | May satisfy readiness if dependent gates also pass. |
| `approved` | An accountable owner decided a policy or risk question. | Supplies authority, but executable representation still needs verification. |
| `inherited_checked` | An existing artifact is linked and applicability was revalidated for this change. | Avoids duplication while preserving freshness and ownership. |
| `provisional` | A reversible working assumption is explicit and has an invalidation trigger. | Allows bounded discovery or implementation that cannot make the assumption irreversible. |
| `blocked` | A claim-critical decision or evidence source is unavailable. | Prevents readiness for dependent behavior and identifies the route to resolution. |
| `not_applicable` | The field does not apply under a named assumption. | Remains reopenable when that assumption changes. |

**Required packet schema**

| field_group | required_content | completion_rule | primary_evidence_lane |
| --- | --- | --- | --- |
| Identity and ownership | Packet identifier, protected transition name, change owner, policy owners, review mode, current state, and related change reference. | Every claim-critical decision has an accountable owner distinct from mere code authorship where necessary. | Repository ownership, issue/change record, policy authority. |
| User and system goal | Concrete actor goal, protected business outcome, and explicit non-goals. | Describes an observable result without embedding a preferred implementation. | Product/domain requirement and transition journey. |
| Trigger and trust boundary | Entry point, transport or message form, size/resource bounds, and all data treated as untrusted. | Identifies where validation and resource consumption begin. | Route/consumer/client configuration and boundary tests. |
| Actor and identity | Human, service, provider, or scheduler identity; authentication mechanism; principal mapping; lifecycle and revocation assumptions. | Identity is derived from trusted evidence rather than payload authority. | Security configuration, identity policy, negative authentication tests. |
| Authorization and tenancy | Resource, action, tenant/account binding, relationship/state predicates, denial semantics, and policy owner. | Positive and negative permissions are explicit at the resource level. | Domain policy, tenant-scoped queries, authorization matrix. |
| Inputs and invariants | Transport shape, bounded parsing, domain conversion, cross-field rules, stateful preconditions, and stable external errors. | Malformed, impossible, and disallowed states are distinguishable without leaking internals. | DTO/value types, validators, integration and contract tests. |
| Protected effect | State read, mutation, disclosure, remote effect, or expensive computation; reversibility and severity. | Names exactly what must not occur on denial, duplicate, cancellation, or failed commit. | Domain behavior, persistence design, provider contract. |
| Commit and acknowledgement | Commit point, transaction boundaries, response or message acknowledgement, and ambiguity window. | Acknowledgement truthfully corresponds to the promised durable state. | Persistence/queue semantics and pre/post-commit fault tests. |
| Concurrency and replay | Replay identity, key scope, uniqueness mechanism, duplicate outcome, ordering, retention, and late-replay policy. | Sequential and concurrent duplicate behavior is deterministic for the stated horizon. | Schema constraints, transaction code, barrier tests, cleanup policy. |
| Deadline and cancellation | Caller deadline, child timeouts, cancellation propagation, cleanup, and any intentionally supervised work. | No request-scoped work escapes ownership and cancellation does not produce false success. | Coroutine structure, client configuration, cancellation injection. |
| Blocking and capacity | Blocking dependencies, execution resource, concurrency bound, queues, saturation response, and resource budget. | Blocking work cannot silently exhaust a shared event or coroutine execution pool. | Dependency inspection, runtime configuration, representative concurrency evidence. |
| Failure classification | Validation, authentication, authorization, conflict, transient dependency, rate, timeout, cancellation, deterministic domain, and unknown failure classes. | Each class has one owned response, retry eligibility, telemetry category, and effect rule. | Typed/domain errors, adapter mapping, fault matrix. |
| Retry and backpressure | Retry owner, eligible errors, attempts, total deadline, delay/jitter policy, concurrency/rate bound, overload behavior, and write safety. | Retried work remains within the end-to-end budget and cannot amplify unbounded load or effects. | Client/worker policy, attempt telemetry, overload and replay tests. |
| Durable/background work | Persistence before response, claim/lease model, worker idempotency, recovery, terminal handling, lag, and retention. | Accepted work survives process termination and has bounded automated recovery. | Queue/store design, restart and duplicate-claim tests, operations evidence. |
| External dependencies | Provider port, credential handling, timeout, error normalization, correlation, quotas, and degradation policy. | Provider-specific behavior is isolated and no credential or sensitive payload crosses observability boundaries. | Client adapter, approved provider contract, controlled service tests. |
| Abuse and fault cases | Relevant misuse, cross-tenant access, malformed input, replay, concurrency, timeout, cancellation, restart, partial dependency failure, and overload states. | Every applicable case maps to an expected effect, response, durable state, and evidence gate. | Threat analysis plus negative and fault tests. |
| Observability and operations | Redacted event fields, metrics, traces, alerts, runbook query, deployment/rollback, migration, and incident owner. | Operators can distinguish rejection, duplicate, saturation, aged work, and dependency failure without secret exposure. | Telemetry schema, synthetic-secret scans, staged rollout and runbook rehearsal. |
| Evidence ledger | Claim, authority/source, target representation, gate or observation, result, environment/configuration, confidence, and timestamp or artifact version. | No decision-driving claim or gate is orphaned. | Claim-specific provenance and verification records. |
| Invalidation map | Assumption or dependency, claims affected, gates to rerun, owner, and safe interim state. | A change selectively reopens dependent evidence instead of silently preserving readiness. | Change review and dependency reasoning. |
| Handoff and closeout | Changed paths, gates run, skipped or unavailable evidence, remaining risk, rollout guardrails, rollback trigger, and next owner/action. | Another reviewer can resume at the first unresolved transition without reconstructing the task. | Change record, journal, deployment evidence. |

**Conditional field triggers**

| condition | additional_required_content | unsafe_omission |
| --- | --- | --- |
| Cookie-authenticated browser request | CSRF design, cookie flags, origin behavior, and browser negative tests. | Treating authentication as sufficient request integrity. |
| Password, reset, verification, or login flow | Approved hashing/migration, enumeration resistance, rate controls, token lifecycle, and redaction. | Exposing account state or creating reusable credentials in logs. |
| Retriable state-changing request or message | Idempotency key, transactional outcome, duplicate response, retention, and concurrent replay test. | Assuming network retries cannot repeat an effect. |
| Remote effect follows local mutation | Outbox/work intent or explicit reconciliation and compensation design. | Leaving partial commit and ambiguous timeout unowned. |
| Work outlives request or process | Durable record, worker claim, recovery, terminal handling, lag and age evidence. | Launching work that can disappear after acknowledgement. |
| Blocking dependency under coroutines | Dispatcher/executor ownership, concurrency bound, pool interaction, cancellation, and saturation test. | Calling blocking code from a constrained shared execution context without capacity evidence. |
| Sensitive or regulated data | Classification, minimum fields, access, retention, deletion, audit, and policy approval. | Copying real secrets or sensitive payloads into examples or broad telemetry. |
| Shared component or platform change | Consumer inventory, compatibility, migration, representative tests, staged rollout, and rollback. | Proving one consumer while breaking another. |

**Artifact routing**

| adjacent_artifact | embed_in_packet | link_to_governed_record | escalation_condition |
| --- | --- | --- | --- |
| Threat model or abuse-case analysis | Decision-critical attacker goals and affected transition states. | System data flows, asset inventory, and broad threat catalogue. | New trust zone, identity architecture, or material threat class. |
| Architecture decision | Chosen option, rejected alternatives, transition-specific consequence, and revisit trigger. | Cross-service topology, platform standard, and migration program. | Choice affects multiple owners or establishes a reusable platform rule. |
| Test plan | Applicability matrix and claim-to-gate links. | Large test implementation detail and environment setup. | Regulated independent validation or broad compatibility matrix is required. |
| Runbook | Observable states, alert ownership, safe replay or containment action, and rollback trigger. | Full incident procedures and access-controlled operational commands. | Incident command, credential rotation, or forensic preservation is needed. |
| Data-governance record | Minimum retained fields, purpose, access, retention, and deletion dependency. | Formal classification, legal basis, and organization-wide retention policy. | Sensitive linkage or regulated data changes. |

**Populated compact example: signed invoice callback**

The values below are illustrative assumptions derived from the user-journey model, not facts about a deployed provider.

| packet_field | populated_value | state_and_evidence |
| --- | --- | --- |
| Protected transition | Authenticated provider event records one tenant-scoped invoice payment transition within the replay horizon. | `provisional`; must be reconciled with the target requirement. |
| Trigger and actor | Bounded callback body from a configured provider account; authenticity uses the approved signed representation and freshness policy. | `blocked` for exact protocol until provider policy is supplied. |
| Authority | Configured provider account maps to one local tenant; payload tenant text cannot grant access; invoice lookup is tenant-scoped. | `provisional`; requires identity mapping and negative tests in target code. |
| Effect and commit | Replay reservation and invoice state transition commit atomically; required remote work is recorded as outbox intent in the same transaction. | `provisional`; requires target persistence support. |
| Acknowledgement | Success follows local commit or durable acceptance, never volatile coroutine launch. | `inherited_checked` from topical guidance; target response contract remains open. |
| Replay | Provider-scoped event key, database-enforced concurrency, stable duplicate outcome, explicit retention and late-replay behavior. | `blocked` for key scope and retention owner. |
| Cancellation | Cancellation before commit rolls back and propagates; response loss after commit is recovered by replay lookup. | `provisional`; requires pre/post-commit fault injection. |
| Adverse cases | Oversized body, invalid/stale signature, malformed command, unknown provider account, foreign invoice, sequential and concurrent duplicate, timeout, restart, exhaustion, and synthetic-secret redaction. | `verified` only after each target gate records an expected result. |
| Operations | Count bounded outcomes, attempt and work age; correlate without signature, raw body, session, token, or sensitive payment fields. | `provisional`; telemetry access and cardinality review required. |
| Invalidation | Reopen auth tests on principal mapping change; replay tests on key/schema/retention change; fault tests on transaction or acknowledgement change; redaction checks on telemetry schema change. | `approved` only after owners accept the dependency map. |

**Acceptance rules**

1. Every field is in a defined state and includes the evidence or assumption that justifies that state.
2. Every `not_applicable` field names the condition that makes it irrelevant and the trigger that reopens it.
3. Every adverse case maps to expected effect count, external response, durable state, and observable evidence.
4. Every claim-critical policy comes from an accountable owner; code prevalence cannot approve policy.
5. Every executable gate names the property it proves, and every readiness property has a gate or accountable observation.
6. Examples and test data use synthetic non-sensitive values, and redaction checks cover failure paths.
7. A `blocked` field prevents operational readiness only for dependent behavior, while safe independent work remains resumable.
8. The handoff records changed paths, evidence actually run, remaining uncertainty, rollback, and the next concrete action.

The packet is complete when it constrains implementation and review, not when it has accumulated prose. Its strongest outcome is a short, traceable chain from authority and assumptions to protected behavior, adverse cases, executable evidence, and operational ownership.

## Worked Example Set

These examples are boundary sketches, not framework-complete recipes. They do not establish current APIs, compilation, transaction semantics, dispatcher behavior, or organization policy. Adapt them only after inspecting the target repository and proving the named guarantee with its actual framework, persistence layer, and runtime configuration.

| concern | unsafe_form | coherent_form | borderline_deciding_fact | falsifying_gate |
| --- | --- | --- | --- | --- |
| Resource authorization | Authenticate a principal, then load a resource globally by payload ID. | Bind principal to tenant/account and enforce action plus resource/state policy through tenant-scoped access. | A pure edge proxy may delegate policy to an authoritative downstream decision point. | Authenticated actor requests another tenant's known resource ID and produces no disclosure or effect. |
| Coroutine cancellation | Catch every throwable and convert it into a normal domain fallback. | Let cancellation propagate and map only owned failure classes. | Intentional supervision may isolate sibling failure, but it still needs explicit lifetime and result ownership. | Cancel the parent while the dependency is suspended and observe prompt child cancellation and cleanup. |
| Blocking dependency | Call JDBC, JPA, file, or blocking SDK work directly from a constrained coroutine execution context. | Use a coherent blocking architecture or isolate unavoidable blocking work on an owned bounded resource. | A fully blocking service can be acceptable when its pools and overload behavior are measured. | Run representative concurrency and observe threads, queueing, pool saturation, timeout, and recovery. |
| Retry of writes | Retry all exceptions around a state-changing call. | Classify transient failures, bound attempts and total deadline, and require replay-safe write semantics. | A caller may own retry, making an inner retry harmful amplification. | Inject validation, auth, timeout, ambiguous commit, and transient dependency results and inspect attempts/effects. |
| Idempotency | Check for a replay row, perform the effect, then insert the row. | Atomically arbitrate replay identity with the effect or durable intent and return a stable recorded outcome. | A naturally idempotent state replacement may not need a separate key if all secondary effects are also idempotent. | Release concurrent identical requests at a barrier and verify one committed protected effect. |
| External client handling | Expose provider exceptions and log request credentials or raw bodies for diagnosis. | Normalize errors into owned classes, bound time, correlate safely, and redact sensitive material. | Rich internal diagnostics can be retained in restricted systems under explicit data policy. | Exercise every provider failure with recognizable synthetic secrets and scan responses and telemetry. |
| Deferred work | Launch an untracked coroutine from request scope and respond success. | Persist work before acknowledgement and process it with an idempotent, bounded, observable worker. | Explicit best-effort work is permissible only when loss is an accepted outcome and the response does not promise completion. | Terminate after acknowledgement and before execution, restart, and verify either durable recovery or the documented best-effort outcome. |
| Browser request integrity | Disable CSRF because authentication already succeeds. | Derive CSRF posture from actual browser and credential transport, preserving framework protection for ambient credentials. | Non-browser or non-ambient credential designs may use a different integrity model. | Cross-site request attempts with deployed cookies/tokens cannot perform the protected effect. |

**Example 1: Resource authorization is not principal presence**

Contract: An authenticated user may view an invoice only through a tenant/account relationship that permits the action. Foreign resource existence must not leak through different externally visible errors.

Unsafe shape:

```kotlin
suspend fun getInvoice(principal: Principal, request: InvoiceRequest): InvoiceView {
    require(principal.isAuthenticated)
    return invoiceRepository.findById(request.invoiceId).toView()
}
```

The principal check establishes identity but not authority over the requested resource. A valid ID from another tenant can cross the boundary if the repository lookup is global.

Coherent shape:

```kotlin
suspend fun getInvoice(
    actor: AuthenticatedActor,
    request: InvoiceRequest,
): InvoiceView {
    val tenant = actor.requireActiveTenantContext()
    val invoice = invoiceRepository.findAuthorizedInvoice(
        tenantId = tenant.id,
        invoiceId = InvoiceId.parse(request.invoiceId),
    ) ?: throw InvoiceAccessDenied

    invoicePolicy.requireViewAllowed(actor, invoice)
    return invoice.toAuthorizedView()
}
```

Target guarantees to establish: principal-to-tenant mapping cannot be supplied by the request body; the query enforces tenant scope; policy handles role, relationship, and state; missing and forbidden outcomes meet enumeration policy; logs do not disclose a foreign resource.

Falsifying checks: unauthenticated, inactive principal, wrong role, foreign tenant with a known invoice ID, deleted/forbidden state, and an allowed owner. All denied cases produce no protected data and the policy-approved external distinction.

**Example 2: Cancellation is control flow, not a recoverable business error**

Contract: Caller cancellation or deadline expiry ends request-owned work, releases resources, and cannot be converted into a successful fallback that continues side effects.

Unsafe shape:

```kotlin
suspend fun loadAccountSummary(id: AccountId): AccountSummary =
    try {
        providerClient.fetchAccountSummary(id)
    } catch (failure: Throwable) {
        logger.warn("provider failed", failure)
        AccountSummary.empty(id)
    }
```

This broad catch can absorb coroutine cancellation, blur programming failures with provider outcomes, log sensitive exception content, and present a fabricated empty account as a normal result.

Coherent shape:

```kotlin
suspend fun loadAccountSummary(id: AccountId): AccountSummary =
    try {
        providerClient.fetchAccountSummary(id)
    } catch (cancelled: CancellationException) {
        throw cancelled
    } catch (failure: ProviderUnavailable) {
        throw AccountSummaryTemporarilyUnavailable(failure.correlationId)
    }
```

Often the first catch is unnecessary if no broader catch exists. The essential rule is to map only failures owned by this boundary and preserve cancellation. If stale fallback is permitted, it must be a policy-approved labeled state with bounded age, never an accidental result of catching everything.

Falsifying checks: cancel the parent while the client is suspended; cancel during transaction acquisition; return a typed provider unavailability; throw an unexpected programming failure. Observe child cancellation, cleanup, external error mapping, and absence of false success.

**Example 3: `suspend` does not make a blocking call non-blocking**

Contract: A blocking dependency must consume a known bounded execution resource whose capacity and timeout behavior fit the service workload.

Unsafe shape:

```kotlin
suspend fun loadInvoice(id: InvoiceId): Invoice =
    blockingInvoiceDao.load(id)
```

The function modifier changes call composition, not the DAO's blocking behavior. Under concurrency, the call may occupy threads needed by unrelated coroutine work.

Conditional coherent shape:

```kotlin
class InvoiceReader(
    private val blockingExecutor: CoroutineDispatcher,
    private val invoiceDao: BlockingInvoiceDao,
) {
    suspend fun loadInvoice(id: InvoiceId): Invoice =
        withContext(blockingExecutor) {
            invoiceDao.load(id)
        }
}
```

This sketch is not sufficient evidence by itself. The dispatcher/executor, database pool, upstream concurrency, queueing, timeout, and shutdown behavior must be designed together. An end-to-end blocking stack can be simpler and safer when it is deliberate, bounded, and measured.

Falsifying checks: hold database calls at a barrier, raise concurrent demand to a representative bound, and observe execution threads, queue wait, connection pool use, timeout propagation, unrelated endpoint latency, and recovery after release. A thread-name assertion alone does not prove healthy capacity.

**Example 4: Retry requires classification, budget, and replay safety**

Contract: Only classified transient provider failures may be retried, all attempts share an end-to-end deadline, and a state-changing operation has a stable replay identity.

Unsafe shape:

```kotlin
suspend fun charge(command: ChargeCommand): ChargeResult {
    repeat(3) {
        try {
            return paymentProvider.charge(command)
        } catch (failure: Exception) {
            delay(100)
        }
    }
    throw ChargeFailed
}
```

The loop retries validation, authorization, deterministic rejection, and ambiguous write failures alike. It ignores caller deadline, fixed-delay synchronization, cancellation details, provider idempotency, and the evidence needed to distinguish a committed charge from a lost response.

Coherent boundary shape:

```kotlin
suspend fun charge(command: AuthorizedCharge): ChargeOutcome =
    retryPolicy.executeWithinDeadline(
        operation = "provider_charge",
        replayKey = command.replayKey,
    ) { attempt ->
        when (val result = paymentPort.charge(command, attempt.remainingDeadline)) {
            is ChargeResult.Accepted -> ChargeOutcome.Accepted(result.providerReference)
            is ChargeResult.Rejected -> throw PermanentChargeRejection(result.reason)
            is ChargeResult.TransientFailure -> throw RetryableProviderFailure(result.category)
            is ChargeResult.UnknownCommit -> reconcileOrReturnUnknown(command.replayKey)
        }
    }
```

The target must define `executeWithinDeadline`, error classification, backoff, jitter, maximum concurrency, cancellation, provider replay semantics, and the unknown-commit reconciliation path. A retry helper cannot make a write safe without these contracts.

Falsifying checks: validation and authorization failures cause one attempt; a transient failure retries only within budget; parent cancellation stops delay and calls; concurrent retries remain bounded; timeout after provider commit reconciles rather than issuing an unrelated second write; logs expose category and correlation but not credentials or sensitive payload.

**Example 5: Idempotency must arbitrate concurrent delivery**

Contract: Two deliveries with the same approved replay identity cannot both apply the protected local transition.

Unsafe timeline:

```text
delivery A: lookup key -> absent
delivery B: lookup key -> absent
delivery A: apply effect
delivery B: apply effect
delivery A: insert replay row
delivery B: insert replay row or fail too late
```

Coherent timeline:

```text
delivery A: atomically reserve key within effect transaction -> winner
delivery B: same atomic reservation -> existing/in-progress outcome
delivery A: apply effect and commit recorded outcome
delivery B: load or await policy-defined stable outcome without repeating effect
```

The exact primitive may be a unique constraint, lock, compare-and-set, transactional insert, state-machine row, or a proven local abstraction. The key requirement is atomic arbitration with the protected transition or durable intent. An in-memory mutex is insufficient across processes and restart unless the deployment contract makes that scope explicit.

Falsifying checks: synchronize two or more deliveries immediately before reservation; run on the actual persistence implementation; inject failure before effect, before commit, and after commit; verify one effect, deterministic recovery, and no permanently stranded reservation without a defined recovery state.

**Example 6: Deferred work needs durable ownership**

Contract: If the response promises acceptance and work must outlive request cancellation or process termination, accepted work is durable before the response.

Unsafe shape:

```kotlin
suspend fun submitReport(request: ReportRequest): AcceptedResponse {
    backgroundScope.launch { reportService.generate(request) }
    return AcceptedResponse()
}
```

Even a long-lived scope does not make the work durable. A crash can lose it, duplicate submissions can create repeated effects, and no bounded retry or terminal state is visible.

Coherent shape:

```kotlin
suspend fun submitReport(
    actor: AuthenticatedActor,
    request: ReportRequest,
): AcceptedResponse {
    val command = reportPolicy.authorizeAndValidate(actor, request)
    val accepted = reportWorkStore.acceptIdempotently(command)
    return AcceptedResponse(workId = accepted.publicReference)
}
```

A separately owned worker must claim durably, process idempotently, bound concurrency, classify retry, recover abandoned claims, park terminal failures, expose age/lag, and apply data retention. The endpoint and worker share a state contract; they are not independent conveniences.

Falsifying checks: terminate after acceptance but before claim, during processing, and after effect but before completion record; restart; submit duplicates; exhaust retry; verify recovery, effect count, terminal state, telemetry, and authorization on result retrieval.

**Example 7: CSRF posture follows the client and credential model**

| request_model | decision_question | coherent_evidence | unsafe_shortcut |
| --- | --- | --- | --- |
| Browser automatically sends authenticated cookies | Can a cross-site origin cause a protected state change with ambient credentials? | Framework configuration, cookie attributes, token/origin behavior, and browser-level negative requests. | Disable protection because the route also requires login. |
| Browser sends an explicit non-cookie credential | Can another origin obtain or cause transmission of that credential, and are cookies still accepted? | Client storage/transport review, CORS/origin behavior, rejected cookie-only request, and authorization tests. | Assume all bearer-style requests are immune without inspecting deployment. |
| Non-browser service client | Is the endpoint reachable from browsers or through a credential-bearing intermediary? | Routing, authentication mechanism, network boundary, and negative integration evidence. | Copy browser settings or disable controls by endpoint label alone. |

**Cross-cutting ownership diagnostic**

For any proposed correction, ask:

1. Who owns identity after transport parsing?
2. Who owns resource and state authorization after authentication?
3. Who owns work after caller cancellation or response completion?
4. Who owns an effect after timeout makes its result ambiguous?
5. Who owns retries, concurrency bounds, terminal failure, and replay retention?
6. Who can investigate without receiving credentials or sensitive payloads?

If an answer is "the framework," "the queue," "the retry helper," or "operations" without an inspected contract and accountable boundary, the example has named a mechanism but not an owner. That gap is the next design and verification task.

## Outcome Metrics and Feedback Loops

Outcome measurement starts from the protected-transition contract. This edition does not prescribe a universal delivery time, latency percentile, retry count, queue age, error rate, or review interval because no target workload, baseline, objective, capacity, or incident policy is supplied. The owning service must set values from risk and representative evidence.

A metric is useful only when it has a defined event, unit, denominator where applicable, bounded dimensions, collection boundary, missing-data behavior, owner, interpretation limit, and response action. Distinguish request attempts, logical operations, committed effects, and externally observed outcomes; retry makes those counts diverge.

**Metric contract**

| contract_field | completion_question | failure_if_omitted |
| --- | --- | --- |
| Protected claim | Which safety, resilience, capacity, or delivery decision does this signal inform? | Dashboard activity can masquerade as evidence. |
| Event and unit | Does it count attempts, logical operations, unique replay keys, committed effects, work records, durations, bytes, or people? | Numerators are compared despite different meanings. |
| Population and denominator | Which requests, tenants, endpoints, event classes, versions, and time windows are included or excluded? | Ratios move because the population changed. |
| Dimensions | Which bounded labels support diagnosis without secrets, personal data, raw identifiers, or unbounded cardinality? | Telemetry creates privacy, cost, and availability risk. |
| Source and aggregation | Where is the event emitted, transformed, sampled, delayed, deduplicated, and stored? | Zero can mean pipeline loss rather than healthy behavior. |
| Threshold and owner | Who chooses the action boundary using workload, policy, baseline, and capacity evidence? | Conventional-looking values acquire unearned authority. |
| Response action | What query, gate, containment, rollback, scaling, or policy review follows the signal? | Alerts create noise without changing outcomes. |
| Interpretation limit | What cannot be concluded from this measure, and which confounders matter? | Correlation becomes a false causal claim. |
| Definition version | When did semantics change, and can historical values still be compared? | Long-term trends combine incompatible data. |

**Leading delivery and evidence indicators**

| indicator | definition_or_question | decision_supported | interpretation_limit_and_action |
| --- | --- | --- | --- |
| Protected-transition field closure | Applicable packet fields in `verified`, `approved`, or `inherited_checked` state, with blocked dependencies listed separately. | Whether implementation or release review has enough authority and evidence to proceed. | Completion percentage is not safety proof; inspect claim-critical blocked fields and route owners. |
| Claim-to-gate traceability | Material claims with current executable or accountable observational evidence, plus gates that have no stated claim. | Detect orphan promises and ritual checks. | A linked gate may still be weak; review its falsifying case and environment. |
| Negative-path closure | Applicable authentication, authorization, tenant, malformed-input, enumeration, and redaction cases with expected rejection evidence. | Prevent happy-path-only completion. | Coverage is bounded to enumerated cases; incident findings may add classes. |
| Fault-path closure | Applicable cancellation, timeout, duplicate, partial-commit, restart, retry-exhaustion, and overload cases with current evidence. | Determine whether the failure contract was exercised. | Passing controlled faults does not establish production capacity or every timing interleaving. |
| Selective invalidation age | Claim-critical evidence reopened by a dependency change but not yet reverified, grouped by owner and impact. | Prevent stale readiness after identity, schema, transaction, client, or telemetry changes. | Age alone does not set severity; prioritize by protected effect and exposure. |
| Unsafe-form gate sensitivity | Representative unsafe implementation or fault state makes the promised gate fail for the intended reason. | Detect vacuous tests and gate harness drift. | Use controlled examples; never weaken production protection to create the unsafe state. |
| Review finding recurrence | Repeated root-cause class after a prior correction or documented anti-pattern. | Decide whether local fixes need a shared abstraction, rule, or training artifact. | Similar labels can hide different causes; inspect evidence before consolidating. |

**Security outcome signals**

| signal | bounded_definition | useful_interpretation | required_caution |
| --- | --- | --- | --- |
| Denied-operation effect violation | Observed protected effect associated with a transition classified as denied. | Any confirmed instance contradicts the authorization contract and requires containment and investigation. | Absence in telemetry does not prove absence; reconcile with durable audit/state where feasible. |
| Authentication and authorization outcome mix | Counts by bounded outcome class, endpoint/transition class, and deployment marker. | Changes can reveal attack traffic, client regression, policy change, or rollout defects. | Do not label every increase a security incident; avoid user/token/resource labels. |
| Cross-tenant denial evidence | Synthetic and controlled tests plus permitted aggregate operational category for foreign-scope attempts. | Confirms tenant boundaries are actively tested and observable. | Operational events may be hostile or accidental and must not disclose foreign identifiers. |
| Sensitive-flow throttle outcome | Allowed, delayed, rejected, and infrastructure-failure states for login, reset, verification, or other approved flows. | Detect bypass, abuse pressure, and accidental lockout behavior. | Distributed enforcement and shared identities complicate interpretation; protect account privacy. |
| Secret redaction gate | Synthetic recognizable secret values absent from responses, logs, traces, metric labels, and error reports across success and failure paths. | Validates the telemetry boundary for known fields. | Cannot prove unknown future fields are safe; rerun when schemas or error handling change. |
| External error contract drift | Responses whose status/category/body violate the bounded non-leaking contract. | Detect framework exception leakage or inconsistent denial mapping. | Stable errors still need an internal correlation and support path. |

**Resilience and effect-integrity signals**

| signal | bounded_definition | useful_interpretation | required_caution |
| --- | --- | --- | --- |
| Retry amplification | Dependency attempts divided by eligible logical operations, segmented by bounded error class and deployment. | Shows load and latency growth hidden by final success rate. | Include hedges and caller retries only if trace/correlation semantics support the comparison. |
| Deadline budget consumption | End-to-end duration and child-attempt time by outcome under a declared workload. | Reveals retries or queueing consuming the caller's recovery budget. | Clock, sampling, and async handoff semantics must be documented. |
| Unknown-commit outcome count | Logical writes whose dependency response cannot establish committed or rejected state. | Drives reconciliation, provider contract, and idempotency review. | Do not auto-retry this class unless replay safety is proven. |
| Duplicate decision mix | New, duplicate-success, duplicate-in-progress, conflict, late-replay, and replay-store failure outcomes by bounded transition class. | Exposes replay pressure, races, retention boundary, and storage health. | Request duplicates are not equivalent to duplicate effects; reconcile with committed state. |
| Duplicate-effect violation | More protected effects than the approved business/replay contract permits for one logical operation. | Any confirmed violation reopens idempotency, transaction, and response-ambiguity gates. | Requires trustworthy logical-operation correlation without exposing sensitive identifiers. |
| Cancellation cleanup evidence | Controlled cancellations and sampled runtime outcomes showing child termination, transaction cleanup, and no false success. | Detects swallowed cancellation and escaped request-owned work. | Runtime sampling alone can miss rare leaks; retain deterministic tests. |
| Blocking-resource saturation | Active, queued, rejected, timed-out, and wait-duration signals for owned blocking executors and backing pools. | Identifies starvation, pool mismatch, and overload behavior. | Averages hide queue tails; environment and workload must accompany conclusions. |
| Durable work age and lag | Age distribution of accepted unfinished work, plus oldest bounded age by work class. | Detects stalled claiming, dependency failure, and insufficient capacity. | Age targets belong to service objectives; avoid work or tenant IDs as labels. |
| Worker attempt and terminal outcomes | Claim, success, transient reschedule, permanent failure, exhaustion, parking, and recovery counts. | Shows whether bounded retry and terminal ownership operate as designed. | A low failure count can coexist with silent lost work; reconcile accepted versus terminal records. |
| Abandoned-claim recovery | Claims recovered after worker termination, with time-to-eligibility under the lease/ownership policy. | Validates restart and crash recovery assumptions. | Recovery that is too aggressive can duplicate active work; verify fencing or ownership semantics. |
| Dependency concurrency pressure | In-flight, queued, rejected, timed-out, and completed calls by bounded dependency class. | Supports retry, breaker, rate, and capacity decisions. | Instrumentation must not itself create high-cardinality provider or request labels. |

**Delivery and operating feedback cadence**

| feedback_point | trigger | evidence_reviewed | resulting_action |
| --- | --- | --- | --- |
| Contract formation | Before implementation of a changed protected transition. | Policy ownership, adverse states, metric contract, and acceptance gates. | Resolve blocked decisions or limit implementation to reversible discovery. |
| Pre-merge | Every relevant change. | Focused positive, negative, fault, replay, redaction, static/build, and integration evidence. | Correct the change or record a justified unavailable gate with owner and consequence. |
| Staged rollout | Deployment to a representative bounded cohort or environment. | Outcome mix, latency/resource behavior, retry amplification, duplicate decisions, work lag, and telemetry health against baseline. | Continue, hold, roll back, or adjust capacity/policy under owned criteria. |
| Steady operation | Service-owned interval and event triggers. | Objectives, saturation, dependency behavior, aged work, terminal failures, denied-effect violations, and missing-data health. | Investigate, scale, contain, repair, or revise objectives and gates. |
| Dependency or policy change | Framework, provider, identity, schema, transaction, client model, or policy assumption changes. | Invalidation map and dependent evidence. | Reopen only affected claims and update definition versions. |
| Incident or near miss | Unexpected effect, disclosure, loss, delay, amplification, or control bypass. | Timeline, durable state, telemetry gaps, policy, tests, and rollout evidence. | Contain, correct, add a reproducing gate, update anti-patterns and packet assumptions, and verify recurrence control. |
| Metric definition review | Signal no longer changes decisions, semantics drift, cardinality/privacy cost rises, or a new failure class appears. | Query use, alerts, response actions, definition history, and data classification. | Revise, replace, or retire the measure while preserving semantic history. |

**Telemetry verification**

1. Emit known synthetic transitions for success, denial, duplicate, transient failure, terminal failure, cancellation, saturation, and recovery as applicable.
2. Verify local events contain the intended bounded fields and exclude recognizable synthetic credentials, tokens, session IDs, signatures, and sensitive payload values.
3. Trace transformation, aggregation, sampling, delay, and loss through a representative pipeline.
4. Reconcile counts with durable replay, effect, and work state for a controlled interval; explain expected divergence between attempts and logical operations.
5. Exercise dashboard or query definitions and confirm deployment/version annotations support comparisons.
6. Trigger an alert or review condition in a controlled environment and rehearse the first runbook decision.
7. Disable or interrupt telemetry and verify that missing data is visible rather than rendered as a healthy zero.

**Interpretation examples**

Good: A rollout increases retry amplification while final error rate is unchanged. The team correlates the change with a client policy edit, reproduces transient-failure load in a controlled test, and adjusts or rolls back under an owned latency and capacity criterion.

Misleading: A low HTTP failure percentage is reported as proof of idempotency. The measure does not distinguish provider retries, logical operation keys, post-commit response loss, or committed effect count.

Ambiguous: Authorization denials rise after deployment. Possible causes include attack traffic, a client sending stale identity, a deliberate policy tightening, broken principal mapping, or improved instrumentation. Use deployment markers, bounded outcome classes, controlled negative tests, and identity-policy evidence before assigning cause.

**Feedback loop**

```text
signal or incident
  -> validate telemetry and scope
  -> form competing causal hypotheses
  -> reproduce with a focused negative or fault gate
  -> correct policy, code, configuration, capacity, or runbook
  -> stage and observe under owned criteria
  -> update the transition packet, anti-pattern registry, and invalidation map
  -> version or retire the metric if its meaning changed
```

No-alert and zero-event states are not automatically healthy. They can mean correct behavior, insufficient traffic, telemetry loss, sampling, a broken query, or an unobserved attack path. Preserve deterministic gates and data-pipeline health evidence alongside operational signals.

## Completeness Checklist

Completeness has two independent layers:

1. **Reference-edition conformance** asks whether this document and its rationale packet satisfy the evolution contract and preserve evidence honestly.
2. **Target-transition readiness** asks whether a real Kotlin backend behavior has approved policy, coherent implementation, adverse-path proof, operational ownership, and current evidence.

A structurally complete reference does not certify an application. A secure-looking implementation does not excuse a malformed or unsupported reference. Record each target item as verified, approved, inherited and checked, provisional, blocked, not applicable with rationale, failed, or unavailable with consequence. Do not mark an item complete by assertion.

**Reference-edition conformance**

| completion_item | acceptable_evidence | invalid_completion |
| --- | --- | --- |
| Original structure preserved | Exact 26 original heading texts and order compared with the frozen archive seed. | Visual similarity or heading count without text/order comparison. |
| Every section substantively evolved | Per-section body length strictly exceeds its seed and a complete reread confirms added decisions, boundaries, alternatives, counterexamples, verification, uncertainty, and deductions without generic repetition. | Adding duplicated prose, empty verbosity, or unsupported precision. |
| Complete rationale packet | 26 packet sections, 260 exact specification questions, six mandatory fields per question, and 1,560 populated values. | Missing fields, altered question text, or answers unrelated to their section/question. |
| Packet answer uniqueness | All mandatory values are unique both literally and after required Section/Question context prefixes are stripped. | Repeated generic answer shells with only prefixes changed. |
| Source integrity | Frozen local source and queue-span hashes verify; complete mapped sources were read before synthesis. | Selective excerpt use or modifying archive/input evidence. |
| Evidence boundary | Local facts, target unknowns, inference, and unrefreshed external routes are labeled; no browsing is implied. | Treating listed URLs or inherited scores as current corroboration. |
| Document hygiene | Forbidden work markers absent; ASCII, whitespace, Markdown tables, and code fences pass the focused verifier. | Ignoring malformed tables/fences because prose renders approximately. |
| Complete QA trail | Green follows completed packet/reference production; full rereads are checkpointed in bounded groups; focused verifier and hashes are recorded; Refactor follows final QA. | Declaring completion before whole-file reread and focused verification. |
| Shared-workspace isolation | Only authorized reference, packet, and lane journal paths change; frozen shared queue rows remain intact. | Reformatting or repairing another lane or shared input. |

**Target-transition scope and authority**

| completion_item | acceptable_evidence | reopen_trigger |
| --- | --- | --- |
| Bounded transition | Actor, untrusted trigger, protected resource/effect, commit, acknowledgement, and recovery path are named. | Entry point, owner, effect, or commit boundary changes. |
| Policy ownership | Authorization, tenant binding, identity meaning, retention, cryptographic, and risk decisions have accountable owners where applicable. | Role/claim semantics, product rule, provider trust, or risk acceptance changes. |
| Evidence classification | Each material claim separates topical guidance, target fact, approved policy, executable result, operational observation, and remaining inference. | Source applicability, version, environment, or ownership changes. |
| Non-goals and scale boundary | Excluded behavior, workload dimensions, dependency assumptions, and split/escalation conditions are explicit. | Workload, fan-out, sensitivity, or deployment topology exceeds the declared boundary. |

**Trust, identity, and protected access**

| completion_item | acceptable_evidence | reopen_trigger |
| --- | --- | --- |
| Untrusted inputs bounded | Body, path, query, header, cookie, claims, message, environment, and provider data are bounded and validated at appropriate layers. | Schema, transport, parser, provider, or resource limits change. |
| Authentication explicit | Framework configuration and principal mapping are inspected; absent, malformed, expired, revoked, and wrong-audience/issuer cases apply as policy requires. | Identity provider, credential transport, framework security configuration, or claim mapping changes. |
| Resource authorization proven | Tenant, resource, relationship, role, and state-dependent denials produce no protected effect or disclosure. | Resource ownership, tenant model, policy, route delegation, or query path changes. |
| Enumeration and errors bounded | External outcomes follow an owned stable contract and internal detail remains access-controlled. | Error mapping, exception handler, resource lookup, or client trust changes. |
| Browser integrity decided | Cookie flags, CSRF, origin, and client credential model are verified when browser ambient credentials apply; otherwise inapplicability names the decisive fact. | Browser reachability, cookie use, CORS/origin behavior, or credential transport changes. |
| Sensitive-flow abuse bounded | Login, reset, verification, token, or other applicable flows have enumeration resistance, rate/fairness controls, and secret-safe telemetry. | Flow exposure, attacker cost, rate-control topology, or token lifecycle changes. |

**Execution, effects, and recovery**

| completion_item | acceptable_evidence | reopen_trigger |
| --- | --- | --- |
| Coroutine lifetime owned | Structured scopes, deadlines, cancellation propagation, supervision, and cleanup are explicit and fault-tested. | Scope owner, timeout, exception mapping, child task, or dependency cancellation behavior changes. |
| Blocking capacity coherent | Blocking dependencies and execution resources are identified, bounded, measured, and matched to backing pools. | Driver/SDK, dispatcher/executor, pool, concurrency, or workload changes. |
| Transaction and acknowledgement coherent | The commit point and response/message acknowledgement correspond to the promised durable state under pre/post-commit failure. | Transaction scope, database/queue semantics, response timing, or async handoff changes. |
| Retry classified and bounded | Only eligible transient failures retry under one total deadline, with bounded attempts/concurrency and cancellation; writes are replay-safe. | Error taxonomy, provider contract, deadline, caller retry, or write semantics change. |
| Idempotency concurrency-safe | Key scope, atomic arbitration, stable outcome, retention, and late-replay policy pass sequential, concurrent, and response-loss tests. | Key derivation, schema/index, transaction, retention, tenant scope, or side effect changes. |
| External clients isolated | Provider port, credentials, timeout, error normalization, correlation, quotas, degradation, and redaction are explicit. | Provider API, credential policy, client dependency, quota, or fallback behavior changes. |
| Deferred work durable when promised | Acceptance persists before response; claim/recovery, idempotency, retries, terminal handling, age/lag, and retention are verified. | Queue/store, lease/fencing, worker concurrency, retry policy, deployment, or recovery objective changes. |
| Overload fails deliberately | Admission, concurrency, queue, rate, and saturation behavior protect critical dependencies and avoid hidden unbounded wait. | Traffic distribution, resource capacity, dependency limit, or routing changes. |

**Verification and operations**

| completion_item | acceptable_evidence | reopen_trigger |
| --- | --- | --- |
| Positive contract | Allowed actor and valid input produce the intended bounded result and durable state. | Domain requirement or representation changes. |
| Negative matrix | Applicable malformed, unauthenticated, unauthorized, cross-tenant, forbidden-state, and disclosure cases reject without protected effect. | Trust, identity, authorization, validation, or error mapping changes. |
| Fault matrix | Applicable timeout, cancellation, transient/permanent dependency, partial commit, duplicate, restart, exhaustion, and overload cases match defined outcomes. | Failure policy, transaction, client, worker, or capacity changes. |
| Gate sensitivity | A representative unsafe state makes each claim-critical gate fail for the promised reason. | Test harness, fixture, assertion, or implementation boundary changes. |
| Secret-safe evidence | Synthetic recognizable secrets are absent from responses, logs, traces, metrics, and error reports across failure paths. | Logged fields, serializers, exceptions, telemetry exporters, or payload schemas change. |
| Metric definitions owned | Signals distinguish attempts, logical operations, effects, and outcomes; dimensions are bounded; missing data is visible; thresholds and actions have owners. | Metric pipeline, semantics, label set, objective, or runbook changes. |
| Performance and capacity evidence scoped | Workload, environment, warm-up, samples, configuration, contention, and uncertainty accompany any latency/throughput/resource claim. | Runtime, hardware, deployment, data distribution, pool, or workload changes. |
| Deployment and migration guarded | Compatibility, configuration, schema/data migration, staged observation, rollback trigger, and owner are explicit. | Release shape, dependency version, schema, client compatibility, or rollout topology changes. |
| Handoff resumable | Changed paths, exact gates/results, unavailable evidence, remaining risk, invalidation links, and next action are recorded. | New work or evidence supersedes the handoff. |

**Review-depth routing**

| transition_profile | minimum_review_shape | escalate_when |
| --- | --- | --- |
| Narrow and reversible | Focused transition fields, reproducing gate, adjacent negative/fault case, and scoped regression. | Discovery reveals protected cross-tenant access, external effects, durable work, or shared behavior. |
| Externally exposed or state-changing | Full packet, policy confirmation, negative/fault/replay evidence, operational signals, staged rollout, and rollback. | Effects are irreversible, sensitive, high-fan-out, or recovery is uncertain. |
| Shared platform boundary | Consumer inventory, compatibility/migration, representative service evidence, staged adoption, and central rollback. | Consumers have conflicting policy, framework, or runtime assumptions. |
| High-assurance transition | Independent threat/policy review, adversarial and recovery evidence, durable audit, controlled release, and governed acceptance. | Required authority, environment, or independent evidence is unavailable. |

**Evidence-quality examples**

Good: "Foreign-tenant invoice access is rejected by `InvoiceRouteAuthorizationTest`; the assertion verifies the configured external response and unchanged invoice/audit-effect state. The test uses the target security chain and tenant-scoped repository."

Bad: "Security is configured and tests pass." This identifies neither policy, denied actor, protected effect, target gate, nor evidence scope.

Borderline: "The gateway blocks unauthorized requests." This becomes sufficient only for the delegated coarse control after gateway configuration, bypass paths, identity propagation, and failure behavior are verified. Resource-level authorization still belongs wherever resource and tenant context exist.

Unavailable evidence is not a pass. Record the missing environment or owner, the claim it leaves open, the risk of proceeding, any compensating review, rollout limitation, and the concrete next action. A failed gate likewise remains failed until corrected or an accountable owner changes the underlying requirement; changing an assertion to match unintended behavior does not close the claim.

Closeout is valid only for the declared transition, assumptions, code/configuration, environment, and evidence versions. Use the invalidation map to reopen dependent items when those facts change. This preserves reusable evidence without granting readiness a permanent lifetime.

## Adjacent Reference Routing

Route by the **dominant unresolved decision**, not by a Kotlin, backend, or security keyword. Keep this reference primary while the blocking question concerns a protected transition's trust boundary, authentication/authorization, validation, cancellation, blocking capacity, retry safety, idempotency, durable ownership, external failure, or secret-safe operation.

An adjacent reference is accepted only after its path exists, its actual headings and evidence boundary are inspected, its scope matches the pivot question, and its output closes a named field in the Protected Transition Review Packet. Filename existence was confirmed locally for the routes below; this assignment did not reread and reverify every adjacent reference's contents. Treat each as a candidate at use time.

| candidate_reference_path | route_when_the_dominant_question_is | expected_return_artifact | responsibility_that_stays_here |
| --- | --- | --- | --- |
| `idiomatic-ref-202607/kotlin_backend_playbook_reference-20260710.md` | Broad backend delivery sequence, service boundary, or lifecycle must be established before a protected transition can be scoped. | Delivery plan with service components, ownership, dependency order, and verification stages. | Security/resilience contract for each protected transition. |
| `idiomatic-ref-202607/kotlin_backend_reference_routing-20260710.md` | The user has several Kotlin backend references and cannot determine the primary one. | Reference selection with scope and handoff rationale. | The bounded security/resilience decision after routing returns. |
| `idiomatic-ref-202607/kotlin_backend_skill_entrypoint-20260710.md` | The task needs the broader backend agent/skill entry contract rather than one topical decision guide. | Entrypoint context, role boundaries, and initial workflow. | Claim-level authority and adverse-path proof for protected behavior. |
| `idiomatic-ref-202607/kotlin_spring_ktor_idioms-20260710.md` | Spring or Ktor configuration, dependency injection, routing, plugin, or framework idiom is the unresolved implementation question. | Framework-conforming implementation shape and framework-specific gates. | Resource policy, denial outcomes, failure contract, and operational evidence. |
| `idiomatic-ref-202607/kotlin_backend_testing_fixtures-20260710.md` | The contract is known but database, container, HTTP, coroutine, provider, clock, or fault fixture design blocks executable proof. | Deterministic fixture and test-harness design tied to named cases. | Which negative, duplicate, cancellation, restart, and fault outcomes are required. |
| `idiomatic-ref-202607/kotlin_backend_runtime_operations-20260710.md` | Deployment, configuration, telemetry pipeline, runbook, rollback, incident response, or day-two operation is dominant. | Operational controls, staged verification, query/alert path, and rollback evidence. | The transition states and safety properties those controls must observe. |
| `idiomatic-ref-202607/kotlin_quality_antipattern_gates-20260710.md` | Static quality patterns, code-review gates, or recurring Kotlin anti-pattern detection is the primary task. | Quality finding or automated gate with scope and false-positive boundary. | Threat, policy, effect integrity, and runtime recovery not established by quality scanning. |
| `idiomatic-ref-202607/kotlin_reliability_reference_patterns-20260710.md` | A broader Kotlin reliability primitive, typed error, concurrency, or lifecycle pattern needs focused treatment beyond backend security context. | Language/runtime reliability decision and focused verification. | Security authority, tenant/resource policy, and protected effect contract. |
| `idiomatic-ref-202607/kotlin_language_skill_entrypoint-20260710.md` | The question is Kotlin-language-wide rather than backend-specific. | Language skill route and local convention set. | Backend boundary, persistence, network, and operational behavior. |
| `idiomatic-ref-202607/kotlin_reference_routing_sources-20260710.md` | The provenance and routing among Kotlin reference sources is itself under review. | Source-level map and evidence lineage. | Applying selected evidence to the protected transition. |
| `idiomatic-ref-202607/executable_specification_skill_patterns-20260710.md` | Requirements remain ambiguous and need executable acceptance criteria before implementation. | Requirement identifiers, preconditions, outcomes, and test plan. | Security/resilience content of the acceptance matrix. |
| `idiomatic-ref-202607/executable_traceability_template_patterns-20260710.md` | Many claims, tests, and artifacts require a formal traceability representation. | Claim-to-source-to-gate ledger with change impact. | Deciding which security/resilience claims are material and correct. |
| `idiomatic-ref-202607/dependency_map_cli_patterns-20260710.md` | Entry points, callers, side effects, or blast radius cannot be found reliably in the target repository. | Pointer-first dependency map and bounded context set. | Semantic policy and failure decisions after code paths are located. |
| `idiomatic-ref-202607/executable_metapattern_reference_digest-20260710.md` | The task needs a broad executable-pattern synthesis across several delivery concerns. | Higher-level pattern selection and acceptance framing. | Concrete protected-transition implementation and evidence. |

**Non-reference routes**

| unresolved_question | accountable_route | safe_output_before_resolution |
| --- | --- | --- |
| Who may perform the effect or see the resource | Product/domain policy owner, with security review proportional to exposure. | Current-behavior characterization, threat cases, and exact policy question. |
| Identity claim meaning, trust federation, credential rotation | Identity/platform security owner. | Claim parsing boundary and negative cases without assuming undocumented semantics. |
| Cryptographic protocol, key custody, compromise response | Security/cryptography authority. | Evidence preservation and approved reversible containment only. |
| Data classification, legal retention, deletion, audit obligation | Data governance/privacy/legal owner as appropriate. | Minimum-data inventory and dependent replay/audit decisions. |
| Production incident command or forensic action | Incident commander and governed response process. | Bounded observed evidence, blast radius, reversible containment, and handoff. |
| Capacity objective, recovery objective, or risk acceptance | Service/platform owner and accountable business/security authority. | Measurement method, baseline needs, and decision alternatives without invented values. |

**Routing algorithm**

1. Write the unresolved question as one decision: for example, "How do we force two deliveries to race deterministically in the actual database fixture?"
2. Keep the protected-transition packet as the source of actor, effect, failure, and acceptance context.
3. Select the candidate whose scope owns the missing mechanism or lifecycle stage; inspect its actual contents before relying on it.
4. State which claim remains governed by this reference and which artifact the adjacent route must return.
5. Return the result as a decision, path, gate, evidence status, assumption, and invalidation trigger rather than copying an entire reference into context.
6. If the adjacent source is incomplete, stale, or conflicting, preserve that result and continue through target evidence or accountable escalation.

**Composition rules**

- Compose references only when they own distinct decisions required for the same transition. A typical composition might keep security/resilience primary, use testing fixtures for a deterministic concurrent-replay harness, and use runtime operations for lag/rollback evidence.
- Do not use framework idioms to invent authorization policy, fixture guidance to decide retry eligibility, runtime metrics to prove absence of a vulnerability, or static quality gates to certify distributed recovery.
- When two references appear to decide the same claim, identify their source authority and assumptions before combining them. Do not average incompatible defaults.
- End a route when the named packet field is closed or the missing authority is identified. Avoid reading-list escalation that adds context but no decision.

**Examples**

Good route: The callback contract already requires concurrent duplicate protection, but the team cannot create a deterministic race against its real persistence layer. Route fixture mechanics to `kotlin_backend_testing_fixtures-20260710.md`; return a barrier-based integration harness. Keep replay key, effect count, and expected duplicate outcome governed here.

Bad route: The team does not know whether support users may view another tenant's invoices, so it opens `kotlin_spring_ktor_idioms-20260710.md` and copies an annotation. Framework syntax cannot decide business authority. Route the policy question to its owner first.

Borderline composition: Spring Security principal mapping is incorrect and foreign-tenant access is possible. Use the framework idioms reference for configuration shape and this reference for principal meaning, tenant/resource policy, and negative outcomes. Completion requires both framework-level and domain-level evidence.

Broad-first route: A greenfield service has no established entry point, persistence boundary, or deployment model. Begin with the backend playbook and entrypoint references, then create one transition packet per owned protected behavior.

**Route acceptance check**

| check | pass_condition | failure_response |
| --- | --- | --- |
| Existence | Exact local path is present. | Search local manifests/reference maps or record absence. |
| Scope | Inspected headings and sources own the pivot question. | Select another route or escalate the authority gap. |
| Output | Returned artifact directly closes or clarifies a named packet field. | Restate the question; stop indiscriminate context loading. |
| Evidence | Result distinguishes source guidance, target fact, inference, and verification. | Keep the field provisional or blocked. |
| Return | Primary transition and dependent gates are updated without losing assumptions. | Restore the packet as the handoff and reconcile conflicts. |

The durable result of routing is the resolved decision and its evidence. The full text of consulted references need not remain active once their output, assumptions, and invalidation links are recorded.

## Workload Model

`combined_evidence_inference_note`: Treat Kotlin Backend Security Resilience as a backend transition and operating reference, not as a prose summary. Workload values belong to the target service and must come from requirements, measured observations, provider contracts, capacity policy, or clearly labeled synthetic scenarios. This reference supplies dimensions and verification pressure points, not invented capacity.

Model at least two units when retry or duplicate delivery is possible:

- **logical operation:** the business intent identified by actor, resource, and approved replay semantics;
- **attempt:** each transport request, message delivery, dependency call, or worker execution made on behalf of that intent.

Also distinguish accepted work, committed effects, externally observed outcomes, rejected work, and unfinished durable work. These counts diverge under timeout, response loss, retry, cancellation, and restart.

**Workload envelope**

| workload_dimension | target_values_or_distribution_to_obtain | security_resilience_pressure | evidence_source |
| --- | --- | --- | --- |
| Transition classes | Route, callback, consumer, scheduled job, provider call, login/reset flow, read/disclosure, and state-changing operation mix. | Different classes have different authority, replay, deadline, and recovery semantics. | Route/consumer inventory, requirements, traces, and packet scope. |
| Logical demand | Logical operations by class over normal, peak, burst, and recovery periods. | Separates business demand from retry amplification. | Bounded operational aggregation or declared synthetic model. |
| Attempt amplification | Requests/deliveries/calls per logical operation, including caller, broker, client, and worker retries. | Reveals duplicate pressure, latency growth, and potential repeated effects. | Correlation/replay records, client/broker policy, and attempt telemetry. |
| Arrival model | Open external arrivals, closed client concurrency, scheduled batches, broker delivery, and synchronized retry behavior. | Determines queueing and whether latency feeds back into offered load. | Client/provider/broker contract and load-generator design. |
| Burst and seasonality | Burst duration, ramp, quiet/peak cycles, deploy/restart catch-up, and scheduled concentration. | Short bursts can exhaust auth, signature, pool, queue, and telemetry resources despite moderate averages. | Historical observations, product schedule, or explicit synthetic boundary. |
| Actor and tenant distribution | Active actors/tenants, per-actor concentration, fairness needs, anonymous/authenticated mix, and credential churn. | Hot tenants and abuse can evade global averages or starve others. | Privacy-safe aggregates and policy-owned fairness requirements. |
| Resource and replay-key skew | Hot resources, same-key duplicates, key collision assumptions, ordering, and late replay. | Drives lock/uniqueness contention and duplicate arbitration. | Domain distribution, replay store, provider contract, and adversarial scenarios. |
| Input shape | Body/message sizes, header count/size, nesting, field lengths, invalid ratios, compression, and parsing complexity. | Untrusted input can consume memory/CPU before policy checks. | Schema, gateway/framework bounds, fixtures, and controlled hostile cases. |
| Authentication work | Credential types, valid/invalid/expired mix, hashing/signature/JWK or provider verification costs, cache behavior, and revocation latency. | Expensive verification can become a denial-of-service surface; stale identity can alter authorization. | Security configuration, controlled measurements, and identity contract. |
| Authorization work | Policy lookups, tenant/resource queries, relationship/state checks, cache dependencies, and denial mix. | Policy cost and failure must not create bypass, leakage, or unfair starvation. | Domain policy, query plans, negative tests, and representative observations. |
| Dependency behavior | Latency distribution, concurrency/quotas, timeout, error classes, connection behavior, and recovery pattern for each dependency. | Slow or failing dependencies drive retries, queueing, circuit state, and ambiguous writes. | Provider/database/queue contracts plus controlled failure injection. |
| Blocking resources | Blocking calls, executor threads, database/file/SDK pools, queue limits, wait behavior, and shutdown. | Pool mismatch or unbounded queueing can starve unrelated work and delay cancellation. | Runtime configuration and concurrency observations. |
| Coroutine structure | Scope owners, child fan-out, deadlines, supervision, cancellation support, and cleanup cost. | Escaped work, cancellation swallowing, and fan-out can amplify resources and effects. | Code path, coroutine tests, and trace/thread evidence. |
| Persistence contention | Transaction duration, lock/index/key distribution, isolation behavior, conflict handling, connection pool, and data size. | Replay and authorization correctness may fail or stall under race and hot keys. | Schema/query plans, database integration tests, and controlled contention. |
| Durable work | Arrival, service rate, worker concurrency, claim duration, lease/fencing, retry delay, terminal outcomes, backlog age, and retention. | Accepted work can accumulate, duplicate, disappear, or monopolize capacity during recovery. | Queue/store state, worker telemetry, restart tests, and recovery objective. |
| Failure mix and timing | Validation/auth/policy failures, transient/permanent dependency errors, timeouts, cancellation, process termination, network partition, and telemetry loss. | Failure timing around commit/acknowledgement determines replay and recovery. | Fault model, incident history, provider contract, and injected scenarios. |
| Overload behavior | Admission limit, concurrency/rate controls, queue bounds, rejection, fairness, shedding, fallback, and recovery. | Unbounded work can exhaust resources; unsafe degradation can bypass protected behavior. | Configuration, policy, overload tests, and staged observations. |
| Deployment topology | Instances, zones/processes, shared pools/stores, routing affinity, rollout overlap, and restart order. | In-memory locks/rates and local observations may not hold across replicas. | Deployment manifests, architecture, and representative environment. |
| Observability load | Event volume, label cardinality, sampling, payload/redaction cost, pipeline capacity, and loss behavior. | Telemetry can leak data or fail exactly when diagnosis is needed. | Telemetry schema, pipeline configuration, synthetic-secret and loss tests. |

**Scenario families**

| scenario_family | construction | properties_to_observe | stopping_or_split_condition |
| --- | --- | --- | --- |
| Normal baseline | Representative valid/invalid mix, data distribution, dependencies healthy, and target deployment/configuration. | Correct outcomes, resource use, latency distribution, attempt/logical ratio, and telemetry semantics. | Baseline is unstable or environment does not represent the claimed scope. |
| Boundary input | Maximum approved sizes/complexity, empty/minimum values, malformed structure, and invalid combinations. | Early bounded rejection, no sensitive leakage, memory/CPU behavior, and stable errors. | Test risks uncontrolled resource exhaustion; move to isolated environment. |
| Authority/adversarial | Missing/invalid/expired identity, foreign tenant/resource, forbidden state, credential abuse, and expensive invalid input. | No protected effect/disclosure, fairness, throttle behavior, and bounded verification cost. | Scenario requires security testing authorization or sensitive production data. |
| Concurrency and replay | Same logical key concurrently, hot resources, conflicting updates, out-of-order and late events. | Atomic arbitration, effect count, conflict behavior, lock/queue wait, and recovery. | The transition spans independently owned commits; split and add coordination evidence. |
| Dependency failure | Inject classified latency, transient/permanent errors, unknown commit, connection churn, and recovery. | Deadline, cancellation, retries, amplification, breaker/degradation, and reconciliation. | Controlled service cannot emulate claim-critical provider semantics; obtain sandbox/staged evidence. |
| Overload | Offer work beyond an owned resource boundary with realistic arrivals and retries. | Accepted/rejected/queued accounting, fairness, bounded memory/threads/connections, protected behavior, and recovery. | Environment is shared or cannot contain impact. |
| Restart and backlog recovery | Accumulate accepted unfinished work, terminate at defined states, restart while new demand continues. | Rediscovery, claim ownership, duplicate effects, lag/age, retry synchronization, and time to controlled state. | Recovery objective or production topology is unknown; retain qualitative evidence only. |
| Deployment transition | Old/new versions overlap with schema/configuration and rolling restart behavior. | Compatibility, replay/state interpretation, migration, rollback, and telemetry versioning. | Change is not backward/forward compatible; require migration choreography and separate release gates. |

**Open versus closed workload models**

| model | useful_for | principal_risk | required_record |
| --- | --- | --- | --- |
| Open arrival | External providers, public requests, brokers, or attackers whose arrivals do not wait for completion. | Offered load can exceed service rate and build queues or rejection. | Arrival process, burst/skew, client retry, and accounting for work not completed. |
| Closed concurrency | Interactive clients or controlled workers with a fixed number of outstanding operations. | Slow service reduces new offered work, which can hide overload and coordinated omission. | Client think/wait behavior, timeout, retry, and measured queueing. |
| Trace replay | Reproducing an observed mix and sequence. | Sensitive data, historical bias, changed environment, and missing future adverse states. | Sanitization, preserved distributions, time scaling, and added fault/adversarial cases. |
| Synthetic generation | Deterministic boundaries, races, and controlled distributions. | Unrealistic uniformity or arbitrary values can produce false confidence. | Rationale for every distribution and comparison against available target evidence. |

**Workload evidence record**

| evidence_field | required_content |
| --- | --- |
| Claim under test | Functional, security, resilience, latency, throughput, resource, fairness, or recovery statement with bounded scope. |
| Generator/trace identity | Exact source, version/hash where applicable, sanitization, random seed, and logical-operation construction. |
| Environment | Runtime/JDK, framework/dependencies, deployment shape, hardware/container resources, data store, network, and co-tenancy. |
| Service configuration | Thread/dispatcher/executor, connection pools, timeouts, retries, rate/concurrency/queue limits, logging/telemetry, and feature flags. |
| Data distribution | Tenant/resource/key skew, payload sizes, valid/invalid mix, initial database/work state, and sensitive-data controls. |
| Timeline | Warm-up, ramp, steady intervals, injected faults, recovery, sample inclusion, and deployment markers. |
| Accounting | Offered attempts, logical operations, accepted, rejected, cancelled/abandoned, queued, completed, committed effects, duplicates, and terminal unfinished states. |
| Observations | Distribution rather than average alone, resource/pool/queue state, error classes, retry amplification, effect integrity, fairness, and telemetry health. |
| Uncertainty | Run-to-run variation, instrumentation loss, fidelity gaps, confounders, and conclusions the evidence cannot support. |
| Decision | Owner, accepted boundary or rejected claim, corrective action, rollout implication, and revisit trigger. |

**Measurement-quality checks**

1. Count offered and rejected/abandoned work, not only completed operations.
2. Confirm the generator's wait behavior does not hide latency through coordinated omission.
3. Record warm-up and avoid combining initialization, migration, or cache-fill behavior with steady-state claims unless that is the scenario.
4. Observe hidden queues in clients, executors, connection pools, brokers, and load generators.
5. Keep injected failure from accidentally reducing offered load unless reduction is part of the client contract.
6. Reconcile logical operations with durable effects and unfinished work so loss or duplication cannot look like throughput.
7. Repeat quantitative scenarios enough to characterize variation; do not infer a precise bound from one run.
8. Isolate or disclose shared-environment noise and compare only compatible definition/environment versions.
9. Verify telemetry remains bounded and available under load; missing data must not be rendered as a healthy zero.

**Examples**

Good callback model: Derive normal unique-event and provider-retry distributions from approved privacy-safe evidence; add controlled invalid-signature load, concurrent same-key races, response loss after commit, database latency, process restart, and backlog recovery. Account for deliveries, logical event keys, committed invoice transitions, duplicates, rejected events, and unfinished records.

Incomplete callback model: Send independent valid events at a fixed average request rate and report successful responses per second. This omits signature failure cost, replay contention, retries, response ambiguity, durable effects, and recovery.

Risk-tailored administrative endpoint: Low normal volume may make throughput a secondary claim, but known-resource cross-tenant denial, audit/redaction, input bounds, expensive-operation throttling, and dependency timeout still need deterministic evidence. Low average traffic is not evidence of low attacker demand or low effect severity.

Recovery is a distinct workload, not merely a return to normal. Backlog, synchronized retries, cache coldness, migrations, and live arrivals can compete for the same resources. Model how admission and worker policy protect current critical work while draining old work, and define the owner who chooses when recovery is complete.

## Reliability Target

Reliability targets must describe the **correct protected outcome**, not merely a favorable transport response. This reference does not supply target percentages, percentiles, durations, attempt counts, observation windows, or error budgets for an unknown service. Those values require a workload model, consequence analysis, measured capability, and accountable owner.

Keep exact reference-process acceptance criteria separate. Counts such as the required 26 sections, 260 exact questions, and 1,560 mandatory packet fields come from the evolution specification; they are deterministic conformance rules, not production reliability estimates.

**Target classes**

| target_class | use_for | expression_shape | breach_or_uncertainty_handling |
| --- | --- | --- | --- |
| Protected-transition invariant | Outcomes that are not permitted within the declared contract, such as a denied actor receiving protected data or one replay identity causing more effects than allowed. | State actor, scope, prohibited/required effect, commit/replay horizon, and falsifying cases. | A confirmed violation triggers containment, investigation, and dependent gate invalidation; absence of observation is not proof. |
| Correctness objective | Eligible logical operations that reach the defined correct terminal outcome. | Numerator, denominator, eligibility, terminal state, window, exclusions, and reconciliation source. | Owner sets target from harm and capability; inspect unknown/unfinished states rather than hiding them. |
| Availability objective | Authorized valid operations for which the service provides a correct usable outcome. | Eligible business intent and valid success result, not status code alone. | Security, durability, and effect-integrity invariants remain guardrails and cannot be traded away. |
| Latency or deadline objective | Time from defined start to correct outcome, durable acceptance, or terminal response. | Distribution, population, clock boundary, async handoff semantics, and workload. | Record timeout/cancellation/queue outcomes and avoid aggregating incompatible classes. |
| Durability objective | Accepted work or acknowledged writes that remain recoverable and reach a defined terminal state. | Acceptance point, durable record, loss/recovery state, retention, and reconciliation. | Restart and fault evidence complement operational ratios; unknown state remains visible. |
| Recovery objective | Time and correctness of return to controlled service after dependency failure, overload, restart, or backlog. | Starting fault state, available capacity, live traffic, backlog, desired controlled state, and owner-set boundary. | Do not call recovery complete while accepted work, duplicate risk, or observability remains unknown. |
| Capacity and backpressure objective | Work accepted and completed correctly within declared resource and workload bounds while overload is rejected or deferred safely. | Arrival model, concurrency, pools/queues, fairness, saturation, and recovery. | Revisit when workload, topology, limits, or dependency behavior changes. |
| Detection and response objective | Time and evidence quality for identifying, containing, and learning from defined security/resilience events. | Event class, signal path, missing-data behavior, owner, first action, and resolution state. | Rare-event targets may rely on exercises and audits rather than unstable percentages. |
| Reference decision quality | Whether this synthesis leads to bounded, evidence-labeled decisions and routes unresolved authority correctly. | Scenario review and traceability to source, target evidence, inference, and next action. | Use qualitative finding classes until a representative evaluation set and scoring authority exist. |

**Reliability target contract**

| field | required_definition | why_it_matters |
| --- | --- | --- |
| User and protected outcome | Who experiences what correct effect, disclosure, acknowledgement, or recovery. | Prevents optimizing an internal proxy detached from user harm. |
| Eligibility | Which authenticated/authorized operations, data states, request/message classes, and workload are included. | Keeps invalid or hostile traffic from distorting user reliability while retaining separate abuse signals. |
| Success and terminal states | Correct success, valid rejection, duplicate outcome, conflict, cancellation, unknown, parked, and unfinished semantics. | A quick response or retry exhaustion is not automatically success. |
| Unit and correlation | Attempt, logical operation, replay identity, accepted work item, committed effect, or user journey. | Retry and distributed acknowledgement make these counts diverge. |
| Measurement boundary | Start/end clocks, synchronous versus durable acceptance, aggregation, sampling, and reconciliation source. | Establishes what the number actually observes. |
| Workload and environment | Arrival model, distributions, faults, deployment, runtime/configuration, dependencies, and data state. | A target without operating conditions is not portable. |
| Objective and window | Owner-approved target value and evaluation window, supplied outside this generic reference. | Makes tolerance and decision authority explicit without invented precision. |
| Guardrails | Security, effect-integrity, durability, fairness, privacy, and cost rules that cannot be improved away. | Prevents one objective from rewarding unsafe behavior. |
| Error budget or breach rule | What level of tolerable service unreliability changes release/investment decisions, or which invariant violation triggers immediate action. | Turns measurement into a control. |
| Missing and uncertain data | Telemetry loss, sparse volume, unknown commit, unfinished work, and confidence limitations. | Distinguishes healthy observation from absent evidence. |
| Verification | Definition tests, deterministic scenarios, workload/fault runs, durable reconciliation, staged observation, and review. | Validates behavior and measurement together. |
| Owner and response | Person/team responsible for target, investigation, containment, rollback, capacity, and policy decisions. | Prevents an alert from ending at an unowned dashboard. |
| Invalidation trigger | Policy, client model, schema, transaction, replay, dependency, topology, workload, or telemetry changes that require recalibration. | Stops stale targets from retaining authority after assumptions change. |

**Protected guardrails before service objectives**

- A denied transition is not successful merely because it responds quickly or reduces load; it succeeds only by enforcing the owned denial contract without protected effect or disclosure.
- A state-changing operation is not available merely because it returns a success-looking response; the promised commit or durable acceptance must exist.
- Retrying a write cannot improve availability at the cost of exceeding its approved effect/replay contract.
- A degraded response cannot count as success unless the caller can distinguish it and the degraded data/capability is policy-approved and safe.
- Dropping, hiding, or indefinitely queueing accepted work cannot improve latency or availability measurements.
- Disabling expensive authentication, authorization, hashing, signature verification, redaction, or audit cannot be used to meet a capacity target.
- Rejecting overload safely can be more reliable than accepting work that will time out, duplicate, leak, or disappear; eligibility and outcome definitions must represent that choice.

**Target maturity path**

| maturity_state | available_evidence | permitted_claim | next_action |
| --- | --- | --- | --- |
| Semantic contract | Protected outcome, adverse states, and owners are known; operational distribution is not. | Qualitative invariant and measurement plan only. | Instrument bounded outcomes and establish workload/environment evidence. |
| Measured baseline | Definitions are tested and representative observations exist with uncertainty. | Scoped current capability, not a committed objective. | Review consequence, capacity, user need, and variation with owners. |
| Owned objective | Target/window, guardrails, breach action, and error-budget or invariant response are approved. | Reliability commitment within declared eligibility and environment. | Stage, monitor, reconcile, and preserve missing-data health. |
| Operationally exercised | Fault, overload, restart, rollback, alert, and runbook behavior have current evidence. | Stronger confidence in recovery and response within exercised scope. | Learn from drift, incidents, and changed assumptions. |
| Invalidated | A claim-critical definition, workload, topology, policy, or telemetry dependency changed. | Prior result remains historical, not current proof. | Recalibrate affected targets and rerun dependent evidence. |

**Illustrative callback target package**

The following defines target semantics without inventing values:

| property | semantic_contract | target_owner_must_supply | evidence |
| --- | --- | --- | --- |
| Foreign-tenant safety | An authenticated provider account cannot read or mutate an invoice outside its mapped tenant. | Applicable policy owner, exposure scope, and incident response. | Cross-tenant negative tests plus durable no-effect and non-enumeration assertions. |
| Replay effect integrity | One approved provider/key scope produces no more invoice transitions than the domain replay contract permits during retention. | Key uniqueness scope, retention, late-replay, and conflict policy. | Sequential/concurrent duplicate tests, schema/transaction inspection, and effect reconciliation. |
| Correct valid processing | Eligible authenticated valid logical events reach accepted, duplicate-compatible, or policy-defined terminal outcomes. | Objective, window, eligibility, and treatment of unknown/unfinished state. | Outcome telemetry reconciled with replay and invoice/work records. |
| Acknowledgement latency | Correct acknowledgement occurs within the provider and service deadline for the chosen synchronous or durable-acceptance model. | Target distribution boundary, workload, environment, and action at breach. | Controlled workload with timeout, retry, and post-commit response-loss scenarios. |
| Durable completion | Durably accepted deferred events survive restart and reach a defined success or terminal investigation state. | Recovery objective, retry/parking policy, retention, and operating owner. | Restart/claim recovery tests, work-age evidence, and accepted-to-terminal reconciliation. |
| Dependency recovery | Provider/database failure and restoration do not create unbounded retry, duplicate effects, or unsafe degradation. | Capacity, concurrency, retry, fallback, and recovery boundaries. | Fault timeline, attempt amplification, resource state, effect count, and staged recovery. |
| Secret-safe diagnosis | Required operational evidence excludes credentials, signatures, session/token material, and sensitive payloads. | Data classification, permitted fields, access, and retention. | Synthetic-secret scans through local and representative telemetry pipelines. |

**Target acceptance review**

1. Can two reviewers independently classify a representative event as eligible, success, valid rejection, duplicate, unknown, or unfinished from the written definition?
2. Does the denominator use logical operations where retries would distort request attempts?
3. Can the measurement distinguish committed effect from response status and durable acceptance from volatile launch?
4. Are telemetry absence, sampling, and pipeline failure visible?
5. Do deterministic negative/fault tests cover counterexamples where the aggregate objective might look healthy despite unsafe behavior?
6. Does a representative workload record environment, offered/rejected/queued work, configuration, and uncertainty?
7. Are objective values and breach actions approved by the people who own consequence, policy, capacity, and operation?
8. Are invalidation triggers linked to the transition packet and deployment/change process?

Good target: "For eligible authorized invoice events, measure correct terminal outcomes by provider-scoped logical event key, reconcile with replay and invoice state, keep foreign-tenant and duplicate-effect rules as guardrails, and use an owner-approved objective/window under a declared workload."

Bad target: "Successful HTTP responses demonstrate reliable payment processing." This omits authentication, eligibility, duplicate effects, durable state, response loss, retry, unfinished work, and target ownership.

Sparse high-severity path: For a low-volume administrative transition, an unstable percentage may add little. Use explicit invariants, exhaustive scenario evidence for known actors/states, controlled recovery exercises, access-controlled audit reconciliation, and an owner-defined response to any confirmed violation.

Objective conflicts must be reviewed before rollout. When latency, availability, cost, fairness, security, and durability point in different directions, preserve protected-effect and disclosure rules, state the tradeoff, identify the authority, and define rollback or capacity action. Do not defer that decision until an outage forces an implicit choice.

## Failure Mode Table

Use this register for one protected transition. Mark a row applicable, not applicable with the decisive assumption, provisional pending discovery, or verified with target evidence. Impact and likelihood are target judgments; this reference does not fabricate a score. A complete row separates prevention, detection, containment, and recovery because those actions have different owners and timing.

**Evidence and decision failures**

| failure_mode | trigger_and_unsafe_mechanism | protected_consequence_and_signal | prevention_containment_recovery | falsifying_or_confirmation_evidence |
| --- | --- | --- | --- | --- |
| Source drift retains stale authority | Framework, provider, policy, topology, or local guidance changes while an old claim remains promoted. | Incorrect configuration or behavior is implemented; source/version mismatch may be the earliest signal. | Track claim-level source role and invalidation; hold dependent release, refresh owned evidence, and reverify affected gates. | Compare frozen/local identity and target versions; exercise the behavior under current configuration. |
| Generic advice escapes review | Plausible pattern is copied without target path, policy, adverse case, or gate. | Wrong abstraction or safety claim reaches code despite polished prose; review cannot trace authority. | Require protected-transition scope and claim-to-gate ledger; revert/contain unsupported behavior and route missing authority. | Ask a representative unsafe case to fail the named gate; inspect exact source and target representation. |
| Synthesis certifies itself | Evolved reference or duplicate prose is cited as independent proof of target readiness. | Unsupported confidence hides missing policy or execution evidence. | Enforce no-circular-promotion rule; demote claim and obtain policy, target, and runtime evidence from independent lanes. | Trace each claim upstream and identify whether purported corroboration shares the same source. |
| Passing document verifier is treated as backend proof | Structural tests pass and are reported as security/resilience validation. | Application defects remain untested while completion is declared. | Keep reference conformance and target readiness separate; block application claim until target gates exist. | Inspect command scope and assertions; confirm whether target code/configuration was executed at all. |

**Trust, identity, and input failures**

| failure_mode | trigger_and_unsafe_mechanism | protected_consequence_and_signal | prevention_containment_recovery | falsifying_or_confirmation_evidence |
| --- | --- | --- | --- | --- |
| Unbounded input exhausts resources | Large, deeply nested, numerous, compressed, or expensive invalid inputs consume CPU/memory before rejection. | Availability loss can delay identity/policy checks and recovery; saturation or process termination may appear before useful errors. | Bound transport and parser resources, reject early, rate/concurrency control expensive paths, and isolate recovery. | Boundary and hostile-shape tests observe CPU/memory, rejection, telemetry cardinality, and protected behavior. |
| Authentication chain is bypassed or misordered | Route/plugin/filter coverage changes, alternate path omits enforcement, or exception handling treats missing principal as anonymous success. | Unauthenticated actor reaches protected behavior; denial mix or route inventory drift may signal it. | Centralize explicit configuration, inventory paths, deny protected routes without trusted principal, contain exposure, and repair coverage. | Exercise each entry path with missing, malformed, expired, revoked, and policy-incompatible credentials. |
| Payload-derived identity or tenant grants authority | Request/message fields are trusted as account, tenant, role, or owner without binding to authenticated identity. | Cross-tenant read/write or confused-deputy effect; durable state may reveal foreign linkage. | Derive authority from trusted principal/provider mapping, scope queries, deny and investigate affected transitions. | Authenticated actor supplies another tenant/resource identifiers; assert non-disclosure and no effect. |
| Coarse role check replaces resource policy | Framework verifies a role but relationship, tenant, resource, or state predicate is omitted. | Authorized-in-general actor performs forbidden specific effect. | Enforce domain-aware policy at the owning layer; contain affected actions and audit exposure. | Role-positive but resource-negative matrix across ownership, tenant, relationship, and state. |
| Error mapping enables enumeration | Missing, forbidden, inactive, or invalid states have distinguishable details not approved by policy. | Actor learns account/resource existence or internal topology; response category drift is observable. | Use stable bounded external contract and internal correlation; repair handler and assess disclosure history. | Compare status/body/timing within controlled tolerance across foreign, missing, and forbidden cases. |
| Browser request integrity is misclassified | CSRF is disabled because authentication succeeds, while ambient credentials remain browser-sent. | Cross-site origin can perform protected effect as victim. | Derive control from actual client/credential model, preserve/configure framework protection, and contain affected browser routes. | Browser-level cross-site attempts using deployed cookie/token behavior produce no protected effect. |
| Sensitive material leaks through diagnostics | Raw credentials, signatures, tokens, sessions, reset values, payloads, or provider errors enter responses/logs/traces/labels. | Credential compromise, privacy exposure, or high-cardinality telemetry; synthetic-secret match is early signal. | Minimize/redact fields, restrict access/retention, rotate or revoke exposed secrets, and investigate sinks. | Exercise success and failure paths with recognizable synthetic secrets through the representative telemetry pipeline. |
| Validation is split inconsistently | Adapter and domain duplicate or omit cross-field/state rules, or deserialization creates partially trusted objects. | Invalid state commits or clients receive unstable leaking errors. | Separate transport parsing, domain conversion, stateful policy, and stable error mapping; repair invalid data if necessary. | Malformed, boundary, invalid-combination, and state-race tests at actual entry points. |

**Coroutine, blocking, and resource failures**

| failure_mode | trigger_and_unsafe_mechanism | protected_consequence_and_signal | prevention_containment_recovery | falsifying_or_confirmation_evidence |
| --- | --- | --- | --- | --- |
| Cancellation is swallowed | Broad exception handling converts cancellation into fallback, retry, or success. | Work/effects continue after caller deadline; active tasks and false success may outlive request. | Preserve cancellation, map only owned failures, cancel affected scopes, and reconcile ambiguous effects. | Cancel parent during each suspension/transaction phase; inspect child termination, cleanup, response, and durable state. |
| Request-scoped work escapes ownership | Detached/global scope performs side effects after response without durable record or owner. | Crash loses accepted work; retries duplicate it; no terminal state exists. | Keep request work structured or durably accept before response; stop unsafe launch and reconcile recent requests. | Terminate after response before/during work, restart, submit duplicate, and inspect recoverability/effect count. |
| Blocking work starves coroutine execution | JDBC/JPA/file/SDK call occupies constrained shared threads under concurrency. | Unrelated work stalls, deadlines fire, retries amplify, and cancellation may be delayed; thread/pool queues rise. | Use coherent blocking architecture or owned bounded isolation matched to backing pool; shed load and recover capacity. | Hold blocking calls, apply representative concurrency, and observe threads, queues, connections, timeouts, and post-release recovery. |
| Pool and executor capacities conflict | Executor admits more blocking calls than database/provider pool can serve, or hidden queues accumulate. | Long waits consume deadlines/resources and hide overload. | Design capacities together, bound queues/concurrency, expose wait state, and reject/defer safely. | Saturate backing pool and reconcile admitted, queued, rejected, timed-out, and completed work. |
| Nested deadlines contradict ownership | Child timeout exceeds parent or retries consume budget without propagating remaining time. | Work continues after usefulness, or later required stages have no time; cancellation/attempt telemetry diverges. | Use one end-to-end deadline with bounded child allocations and propagated cancellation. | Inject delays at each stage and confirm total time, attempts, cleanup, and no post-deadline effect. |
| Supervision hides failed child result | Supervisor isolates failure but no owner observes or persists the child outcome. | Partial work silently disappears while parent reports success. | Supervise only intentional independent work with explicit result collection, durability, and terminal handling. | Fail one child under supervision and verify parent contract, recorded outcome, alert, and recovery. |

**Retry, transaction, and effect-integrity failures**

| failure_mode | trigger_and_unsafe_mechanism | protected_consequence_and_signal | prevention_containment_recovery | falsifying_or_confirmation_evidence |
| --- | --- | --- | --- | --- |
| Deterministic failure is retried | Validation, authentication, authorization, conflict, or permanent provider rejection is classified as transient. | Added latency/load, account abuse, repeated denial, and misleading availability. | Typed classification, bounded policy, and immediate terminal mapping; disable bad retry and inspect amplification. | Inject each deterministic class and assert one owned decision without retry. |
| Retry storm amplifies dependency outage | Many callers/workers retry synchronized failures without total deadline, jitter, or concurrency bounds. | Pool/queue exhaustion prolongs outage and starves recovery; attempt ratio and queue age rise. | Bound attempts/deadline/concurrency, apply backoff/jitter where warranted, admission control, and recovery ramp. | Controlled outage and restoration with live demand; observe attempts, resources, fairness, and recovery. |
| Check-then-insert replay race | Concurrent deliveries both see absent key before effect and marker insertion. | Duplicate protected effect despite sequential idempotency tests. | Atomic uniqueness/lock/state-machine arbitration with effect or durable intent; contain and reconcile duplicates. | Barrier-controlled concurrent delivery on actual persistence plus durable effect count. |
| Replay reservation strands work | Key is reserved separately, then processing fails before effect/outcome with no recoverable state. | Retries are suppressed while intended effect never occurs. | Transactional coupling or explicit in-progress/lease/recovery state; repair stranded records under policy. | Inject failure after reservation at each phase and verify retry/recovery semantics. |
| Response is lost after commit | Service commits but sender times out or connection fails and retries. | Duplicate effect if replay outcome is absent or unstable; unknown-commit events rise. | Persist stable replay outcome with effect, return duplicate-compatible response, and reconcile ambiguous dependencies. | Fault response path after commit and resubmit identical logical operation. |
| External effect occurs inside uncertain local transaction | Remote call succeeds, local transaction rolls back or retries, or lock is held during latency. | Remote/local divergence, duplicate remote effect, contention, and difficult compensation. | Use outbox/durable intent or an explicitly idempotent/reconcilable protocol; stop retries and reconcile affected keys. | Fail before/after remote success and local commit; inspect both systems and recovery. |
| Replay retention expires without late policy | Cleanup removes key while late duplicate remains possible. | Old event is treated as new and repeats effect, or storage grows indefinitely if cleanup is avoided. | Own retention and late-replay semantics with data/privacy policy; quarantine or reconcile ambiguous late events. | Advance controlled time across retention and replay with known durable state. |
| Out-of-order event overwrites newer state | Consumer applies events by arrival rather than domain sequence/version rules. | State regresses or forbidden transition occurs; version conflict/late-event signal may appear. | Enforce domain ordering/state machine and define late/conflict outcome. | Deliver valid events in reversed and duplicated order under concurrency. |

**Durable work and operational failures**

| failure_mode | trigger_and_unsafe_mechanism | protected_consequence_and_signal | prevention_containment_recovery | falsifying_or_confirmation_evidence |
| --- | --- | --- | --- | --- |
| Acknowledged work exists only in memory | Endpoint responds before durable enqueue/record. | Crash silently loses promised work; accepted-to-terminal reconciliation diverges. | Commit durable acceptance first; contain endpoint or change truthful response until repaired. | Terminate immediately after acknowledgement and verify rediscovery or documented non-durable semantics. |
| Abandoned worker claim never recovers | Worker dies while record remains permanently owned or invisible. | Durable work stalls; oldest age rises without attempts. | Lease/fencing/recovery policy, heartbeat only where justified, and operator visibility. | Terminate claimant at multiple phases, wait policy interval, and verify safe reclaim without duplicate effect. |
| Aggressive reclaim duplicates active work | Lease expires while slow valid worker still acts and another worker claims. | Concurrent duplicate external/local effects. | Size/renew/fence ownership under workload, make worker idempotent, and bound long operations. | Delay worker beyond lease, trigger reclaim, and verify fencing/effect contract. |
| Poison work hot-loops | Deterministic event repeatedly retries without terminal classification or delay. | Queue capacity and dependency load consumed; healthy work starves. | Classify, cap, park/dead-letter under policy, expose terminal state, and support controlled replay. | Submit deterministic failure among healthy work and observe attempts, fairness, parking, and operator path. |
| Unsafe degradation bypasses policy or freshness | Dependency outage returns stale/partial data or permits write without approved bounds. | Unauthorized disclosure/effect or misleading success during outage. | Reject when correctness/authority unknown; permit only labeled policy-approved safe degradation. | Outage tests prove degraded path cannot escalate authority or mutate with invalid state. |
| Telemetry fails during overload | Pipeline saturates, labels explode, sampling drops critical events, or logging blocks request threads. | Operators see healthy-looking silence while effects/backlog fail; service load worsens. | Bounded labels, non-blocking/bounded export, pipeline health, missing-data alert, and durable reconciliation. | Load/fault telemetry path and verify loss visibility, service behavior, redaction, and query semantics. |
| Rollout mixes incompatible state semantics | Old/new versions interpret replay rows, queue records, errors, or schema differently. | Duplicate/lost work, rollback failure, or misleading metrics. | Backward/forward compatibility, expand/migrate/contract sequence, versioned records, staged cohort, and rollback. | Run mixed-version integration and rollback against representative state transitions. |
| Recovery work starves behind live traffic | Backlog, synchronized retries, and current demand share exhausted pools/queues without reservation or fairness. | Recovery objective is missed and aged protected work grows. | Protect bounded recovery capacity, admission/fairness policy, ramp retries, and monitor oldest work. | Restore dependency with backlog plus live arrivals and observe fairness, effects, and time to controlled state. |
| Credential/config rotation breaks only part of fleet | Mixed secrets/configuration during rollout cause intermittent auth/client failures and retries. | Partial outage, lockout, or unexpected fallback; failures correlate with instance/version. | Overlap/rotation protocol, version observability, staged validation, and rollback/revocation ownership. | Mixed-instance rotation rehearsal with old/new credentials and failure-safe behavior. |

**Row-quality contrast**

Good: "The provider commits a charge, the response is lost, and the service retries with a different or absent replay key, causing a second charge. Detect unknown-commit outcomes, stop blind retries, reconcile by the approved key, and verify by failing the response path after provider commit."

Bad: "Payment API error; add retries." The row does not identify error class, commit ambiguity, effect risk, owner, bound, signal, or recovery.

Conditional: A transient idempotent read can retry under one deadline and concurrency bound when the caller does not also amplify it. The same timeout around a non-idempotent write may require reconciliation rather than another attempt.

**Compound failure cascades**

| initiating_event | cascade | protected_intervention_points |
| --- | --- | --- |
| Dependency latency spike | Calls occupy pools, parent deadlines expire, callers retry, queues grow, telemetry volume rises, and recovery probes compete with backlog. | Admission/concurrency bounds, propagated deadline, classified retry, bounded telemetry, and reserved/fair recovery capacity. |
| Database contention on replay key | Transactions wait, callback responses time out, provider redelivers, same key contention grows, and claims may expire. | Atomic short transaction, stable duplicate/in-progress outcome, timeout policy, and hot-key/backoff observation. |
| Identity provider degradation | Authentication latency/failure rises, clients retry/login flows intensify, cache/fallback pressure grows, and unsafe fail-open temptation appears. | Fail-safe policy, bounded verification resources, sensitive-flow rate controls, explicit degradation, and incident authority. |
| Worker fleet restart with backlog | Claims are abandoned, retries synchronize, stale leases overlap new workers, external dependencies saturate, and live work ages. | Fencing/reclaim proof, jitter/ramp, concurrency limits, fairness, idempotency, and oldest-work monitoring. |
| Telemetry pipeline outage during deployment | New behavior lacks signals, missing data resembles healthy baseline, rollback trigger is delayed, and diagnostic logging may be increased unsafely. | Pipeline health signal, staged hold on missing evidence, durable-state reconciliation, preapproved redacted diagnostics, and rollback. |

For each applicable cascade, identify shared resources used by normal work, control paths, and recovery. Protect the ability to authenticate, reject, reconcile, drain, and observe before saturation occurs. After fault injection or containment, inspect durable aftermath and cleanup; a request-level error alone does not reveal stranded reservations, open transactions, duplicate effects, abandoned claims, or leaked secrets.

## Retry Backpressure Guidance

Retry is permitted only when **both** gates pass:

1. **Semantic eligibility:** another attempt can plausibly change the outcome, the failure is classified transient, the operation is replay-safe or read-only as defined, and the prior commit state is sufficiently known.
2. **Load permission:** the total deadline, attempt policy, cancellation state, concurrency/rate capacity, queue bound, caller behavior, and dependency health permit another attempt without destabilizing the system.

If either gate fails, choose fail, reject, reconcile, degrade safely, durably delay, park, shed, or escalate according to the transition contract. Retry is one action among these, not the default meaning of resilience.

**Failure classification and action**

| observed_failure_class | immediate_retry_default | alternative_action | evidence_needed_before_override |
| --- | --- | --- | --- |
| Transport-shape or domain validation failure | Do not retry unchanged input. | Return bounded stable rejection; correct input or contract. | Proof that a distinct transient parser/dependency failure, not input, caused the result. |
| Missing, invalid, expired, or unauthorized identity | Do not retry automatically with the same credential. | Reauthenticate/refresh through the owned client flow, deny, rate-control sensitive path, or escalate policy. | Identity-provider contract and proof that one layer owns credential refresh without loops. |
| Resource/tenant authorization denial | Do not retry unchanged actor/resource state. | Return policy-approved denial; obtain legitimate policy/state change outside the immediate loop. | Accountable policy decision or newly established authorization context. |
| Deterministic business rejection | Do not retry unchanged command/state. | Return terminal domain result or wait for an explicit external state transition. | Evidence that the rejection is a concurrency snapshot expected to change and retry remains within policy. |
| Optimistic conflict | Re-read/recompute may be eligible when command semantics permit it. | Return conflict or require caller resolution. | Bounded conflict rate, side-effect safety, total deadline, and revalidation of authorization/invariants. |
| Connection/setup failure before request acceptance is known | May be eligible under client contract and budget. | Fail fast or durably reschedule. | Provider/client semantics, attempt ownership, concurrency bound, and remaining deadline. |
| Explicit transient provider response | May be eligible if the provider and operation contract allow it. | Honor owned delay, shed, queue durably, or fail. | Error classification, provider guidance, replay safety, deadline, and aggregate load. |
| Read timeout | Conditional: retry only when stale/duplicate reads are safe and budget remains. | Return unavailable/degraded safe response or fail. | Caller retries, dependency load, read side effects, consistency requirement, and total deadline. |
| Write timeout or unknown commit | Do not issue a blind new write. | Reconcile by stable replay identity, query outcome, or return explicit unknown state. | Provider idempotency/reconciliation contract and proof repeated attempt cannot exceed effect contract. |
| Local transaction conflict/deadlock class | Conditional under data-layer classification and short transaction semantics. | Surface conflict, reschedule durable work, or redesign contention. | Actual database error class, rollback completion, retry budget, and no external effect inside transaction. |
| Local overload, queue full, or concurrency limit | Do not add internal attempts to the same constrained path. | Reject/shed, signal caller, route to bounded durable queue, or reduce admission. | Proven spare alternate capacity and non-amplifying caller behavior. |
| Parent cancellation or expired deadline | Never continue request-owned retry. | Propagate cancellation and clean up; reconcile any ambiguous committed effect separately. | A separately durable owner already accepted the work before cancellation. |
| Permanent provider rejection | Do not retry unchanged operation. | Map stable terminal outcome; park for policy/operator action only if useful. | Provider contract or new data showing rejection classification changed. |
| Unknown/unclassified failure | Default to no automatic repetition for protected writes. | Fail safely, record bounded diagnostics, investigate, and add classification. | Controlled evidence establishes transient nature and safe effect semantics. |

**Retry ownership ledger**

Inventory the full stack. A locally small policy can multiply across layers:

| layer | questions_to_answer | hidden_amplification_risk |
| --- | --- | --- |
| User/client SDK | Does it retry on timeout, connection close, or status category; does it reuse the same replay identity? | User-visible retry combines with server/client attempts and changes logical-operation accounting. |
| Gateway/proxy/load balancer | Can it replay requests, fail over, queue, or hedge; which methods/bodies qualify? | Infrastructure may repeat a write without application awareness. |
| Route/service | Does application code retry; who owns total deadline and cancellation? | Nested policies reset counters or continue after caller usefulness. |
| External client/driver | Does library or connection pool transparently retry setup, transaction, or request? | Helper semantics add attempts and hide commit ambiguity. |
| Broker/queue | What triggers redelivery, visibility expiry, negative acknowledgement, or dead-letter/parking? | Redelivery overlaps an active slow worker or bypasses local attempt count. |
| Worker scheduler | How are attempts, delays, claims, terminal failures, and manual replay represented durably? | Process restart resets in-memory counters or releases many jobs simultaneously. |
| Database transaction layer | Which conflicts are automatically retried and what code executes again? | External calls or non-transactional effects may repeat inside transaction callback. |

The potential attempt count is shaped by the composition of retrying layers, not by the largest local count. Record the stack and test it end to end; do not multiply configured values into a reliability claim unless all conditional paths and cancellation behavior are known.

**Retry envelope**

| envelope_dimension | required_decision | unsafe_absence |
| --- | --- | --- |
| Total deadline | One owner defines elapsed budget across queue wait, attempts, delays, and reconciliation. | Later attempts continue after the result has no value or leave no time for commit/cleanup. |
| Attempt eligibility | Typed/normalized error classes and operation semantics decide whether another attempt can help. | Validation, authorization, overload, and unknown writes repeat. |
| Attempt bound | Owner-approved bound derived from deadline, provider behavior, and consequence. | Failure loops consume capacity indefinitely. |
| Delay policy | Backoff and provider-directed delay semantics, with jitter when synchronized concurrency can amplify load. | Immediate or synchronized repeats prolong outage. |
| Cancellation | Parent cancellation stops delay and in-flight owned work; cleanup and ambiguous effects are explicit. | Work escapes caller lifetime or returns false success. |
| Replay safety | Stable logical identity, atomic local idempotency, provider support, or reconciliation for writes. | Attempts multiply protected effects. |
| Concurrency | Maximum in-flight initial plus retry work per dependency/tenant/operation under an owned fairness model. | Retry consumes all capacity and starves fresh or recovery work. |
| Admission/rate | New demand is accepted, deferred, or rejected before expensive work under bounded keys and distributed semantics. | Internal queues and expensive auth/validation saturate first. |
| Queue | Capacity, persistence, priority/fairness, expiry, and behavior when full. | Memory grows, deadlines expire unseen, or accepted work is lost. |
| Recovery ramp | How delayed/backlogged attempts become eligible after dependency restoration. | A synchronized wave immediately causes another outage. |
| Telemetry | Logical operation, layer, attempt, error class, remaining budget, delay, terminal outcome, and bounded correlation. | Operators see final errors but not amplification or effect ambiguity. |

**Backpressure controls by boundary**

| control | appropriate_purpose | precondition | failure_mode_to_test |
| --- | --- | --- | --- |
| Early input bounds | Reject excessive untrusted work before parsing/auth/provider cost grows. | Correct limit and stable non-leaking error owned by transition. | Boundary bypass, compressed/nested input, and telemetry cardinality. |
| Admission control | Refuse work when required downstream capacity is unavailable. | Correct signal and caller/durable alternative defined. | Unfair tenant starvation, fail-open behavior, and retrying callers. |
| Concurrency limiter | Bound simultaneous work against a dependency or expensive operation. | Queue/rejection behavior and cancellation of waiters defined. | Permit leak, cancellation leak, priority inversion, and recovery surge. |
| Rate control | Bound work per actor/tenant/resource/global dimension over time. | Trusted key derivation, distributed consistency, and sensitive-flow policy. | Key evasion, hot-tenant fairness, instance bypass, and accidental lockout. |
| Bounded queue | Absorb a measured short mismatch between arrival and service rate. | Capacity, expiry, ownership, durability promise, and full behavior explicit. | Hidden timeout, memory pressure, stale work, and loss on restart. |
| Durable delayed work | Move recoverable work beyond request lifetime with persistent attempts and terminal state. | Idempotent worker, recovery, lag/age, parking, and retention. | Restart, duplicate claim, poison work, and backlog recovery. |
| Circuit breaker | Stop calls during sustained dependency failure when an open-state response is safe. | Error classification, shared-state scope, probe policy, and safe fallback/rejection. | Incorrect trips, half-open surge, stale state, and unsafe degradation. |
| Load shedding | Preserve critical capacity by rejecting lower-priority work under an approved policy. | Priority cannot be attacker-controlled and protected behavior remains enforced. | Starvation, policy bypass, misleading success, and recovery fairness. |
| Caller signal | Return explicit overload/retry guidance or terminal state the caller understands. | Caller behavior is known and does not synchronize or exceed deadline. | Retry storm, ignored delay, duplicate write, and client incompatibility. |

**Illustrative Kotlin boundary model**

```kotlin
sealed interface AttemptDecision {
    data class RetryAfter(
        val delay: Duration,
        val remainingDeadline: Duration,
    ) : AttemptDecision

    data class Reconcile(val replayKey: ReplayKey) : AttemptDecision
    data class ReturnTerminal(val outcome: OperationOutcome) : AttemptDecision
    data class RejectOverload(val reason: BoundedOverloadReason) : AttemptDecision
}

fun decideNextAttempt(
    operation: ProtectedOperation,
    failure: NormalizedFailure,
    budget: AttemptBudget,
    capacity: CapacitySnapshot,
): AttemptDecision
```

The target implementation must define and verify these types and decisions. A policy function should not make remote calls or hide delays; it should make eligibility inspectable. The executor then honors structured cancellation, remaining deadline, concurrency permits, redacted telemetry, and stable replay identity. Do not infer atomicity or provider safety from this sketch.

**Worker-specific flow**

```text
claim durable work with ownership/fencing
  -> revalidate policy/state assumptions that may have changed
  -> classify attempt result
  -> success: commit terminal outcome
  -> transient and within deadline/attempt/load budget: persist next eligibility
  -> unknown commit: persist reconciliation state
  -> deterministic or exhausted: persist parked/terminal state
  -> release capacity and emit bounded outcome
```

Never hold a database transaction open during backoff delay. Persist attempt and next-eligibility state atomically with the worker state transition where the storage model permits it. A process restart must not erase attempt history or make all delayed work immediately eligible without an owned recovery rule.

**Verification matrix**

| scenario | required_observation |
| --- | --- |
| Validation, authentication, authorization, and permanent domain/provider rejection | No automatic repeat of unchanged operation; stable terminal response and no protected effect. |
| One classified transient read failure followed by success | Attempts stay within total deadline and configured ownership; correlation and result remain correct. |
| Write response lost after commit | No blind unrelated write; reconciliation or stable replay returns one permitted effect. |
| Parent cancelled during call or delay | Delay and in-flight owned call stop promptly; permits/resources release; ambiguous effect follows reconciliation path. |
| Many concurrent transient failures | In-flight attempts, queue, memory, threads/connections, and telemetry remain bounded; fresh/critical work fairness matches policy. |
| Caller plus client plus worker retries | End-to-end attempt trace reveals complete composition and no counter reset loophole. |
| Queue full or limiter exhausted | Work is rejected or durably deferred according to contract; no hidden unbounded wait. |
| Dependency restores with backlog | Eligibility is ramped/jittered as designed, recovery does not re-overload dependency, and oldest work progresses. |
| Breaker opens and half-opens | Open-state behavior is safe, probes are bounded, cancellation works, and recovery avoids a surge. |
| Poison work among healthy jobs | Deterministic item reaches parked/terminal state and does not starve healthy work. |

**Required telemetry** should distinguish logical operation from attempt, identify the retrying layer and bounded operation/dependency class, record normalized failure, remaining deadline, delay class, limiter/queue outcome, terminal/reconciliation state, and deployment/configuration version. Do not place credentials, tokens, sessions, raw replay keys, tenant IDs, resource IDs, or provider payloads into broad metric labels.

Good: A provider client owns transient read retries under one propagated deadline, while the route does not repeat again. Concurrency is bounded, parent cancellation stops attempts, and outage/recovery tests observe amplification and fairness.

Bad: A catch-all loop retries a payment call after any exception with fixed delay. It cannot distinguish validation, authorization, unknown commit, cancellation, or overload and has no stable replay or aggregate capacity bound.

Borderline: Broker redelivery can be the retry owner for a consumer when message acknowledgement, visibility/claim semantics, idempotent effect, attempt persistence, delay, terminal handling, and restart recovery are all explicit. Adding another in-process loop may only multiply work and obscure broker ownership.

Backpressure is effective only when it reaches the demand source or a durable owner. Slowing an internal stage while continuing to admit unbounded work moves pressure into memory, queues, deadlines, cancellations, and caller retries. During recovery, reserve or fairly allocate enough capacity to authenticate, reject, reconcile, drain, and observe; otherwise the controls needed to recover are starved by the backlog they are meant to manage.

## Observability Checklist

Observability for a protected transition must answer three questions without creating a new disclosure or availability failure:

1. What logical outcome occurred, including denial, duplicate, unknown, unfinished, and terminal states?
2. How did attempts, dependencies, cancellation, resources, and deployment state produce that outcome?
3. Can an authorized operator act safely when signals are incomplete, delayed, or unavailable?

Do not require latency percentiles by habit. Record a distribution when a latency/deadline claim is material and the workload and measurement boundary are defined. For sparse or high-severity transitions, deterministic scenarios, durable audit/state reconciliation, and runbook exercises may be more informative than unstable percentile summaries.

**Signal selection**

| signal_type | best_question | source_of_truth_limit | data_and_operating_risk |
| --- | --- | --- | --- |
| Structured log/event | What bounded transition or failure class occurred at this point? | Emission does not prove delivery, ordering, or durable effect. | Sensitive fields, volume, blocking export, retention, and access. |
| Metric | Is a bounded outcome, resource, or failure pattern changing? | Aggregation loses individual causality and can hide missing data. | Label cardinality, privacy, sampling, and misleading denominator. |
| Trace | Where did time, attempts, and dependency calls flow for a sampled operation? | Sampling and propagation gaps mean traces are incomplete. | Baggage/tag leakage, high volume, and confusing attempt with logical outcome. |
| Security audit record | Who or what performed/attempted an accountable protected action under which policy context? | Audit purpose and access differ from general diagnostics. | Sensitive identity/resource linkage, tamper resistance, retention, and legal policy. |
| Durable application state | What effect, replay outcome, or accepted work actually committed? | Explains result but not always timing or causal failure. | Data classification, query load, retention, and migration semantics. |
| Alert/runbook signal | Which owned condition requires a decision now? | Depends on metric/query correctness and delivery. | Noise, missing owner, alert storms, and unsafe automated action. |

Use durable state to arbitrate committed effect and work ownership when response or telemetry disagrees. Use telemetry to explain path, timing, load, and failure. Keep audit identity in its governed lane rather than copying it into broad metric labels.

**Core transition event semantics**

| field_category | examples_of_bounded_content | rule |
| --- | --- | --- |
| Transition | Stable operation/transition class and schema/definition version. | No raw route parameters or user-controlled operation names as labels. |
| Outcome | Accepted, valid rejection class, unauthorized, duplicate, conflict, unknown, cancelled, overloaded, parked, recovered, or terminal class as applicable. | Vocabulary is owned and bounded; external errors may be coarser than internal categories. |
| Logical versus attempt | Opaque safe logical correlation where permitted, layer, attempt ordinal/category, and terminal flag. | Do not expose raw replay keys or business identifiers; document whether joins are partial. |
| Authority context | Authentication mechanism class, policy decision category, and tenant-scope presence where allowed. | Avoid principal, credential, tenant, resource, role set, or claim values in broad telemetry. |
| Dependency | Bounded provider/database/queue class, normalized result, timeout/cancellation, and remaining-budget category. | No URLs containing secrets, raw response bodies, or exception text as metric labels. |
| Resource | Owned executor/pool/queue class, admitted/queued/rejected state, saturation category, and work-age class. | Detailed values may be metrics/distributions; configuration version must be recoverable. |
| Deployment | Service/build/configuration/schema/feature cohort identifiers with bounded cardinality. | Support comparison and rollback without embedding host-unique churn unnecessarily. |
| Correlation | Opaque non-secret value with defined scope, access, collision, and retention. | Correlation must not grant access, reveal a stable sensitive identity, or be accepted as authorization. |

**Never place these values in general logs, traces, metric labels, exception reports, or examples unless a separately governed forensic process explicitly authorizes minimum collection:**

- passwords or password-derived values;
- raw access, refresh, reset, verification, API, or session tokens;
- raw `Authorization`, cookie, signature, or secret headers;
- private keys, client secrets, database credentials, or connection strings;
- full request/provider payloads containing sensitive or attacker-controlled data;
- raw replay/idempotency keys, payment details, personal data, or unrestricted user/resource identifiers;
- unbounded exception messages, SQL, URLs, stack metadata, or user-provided labels that may contain secrets.

A stable hash is not automatically safe. Low-entropy values can be enumerated, and stable hashes can create long-lived linkage. Treat hashed sensitive identifiers according to classification, purpose, access, and retention rather than assuming transformation removes risk.

**Security observability checklist**

| question | required_evidence | unsafe_gap |
| --- | --- | --- |
| Can operators distinguish missing/invalid identity, authorization denial, foreign scope, malformed input, abuse control, and infrastructure failure without leaking protected existence? | Bounded outcome schema and contract tests across negative paths. | One generic error hides control failure, or detailed error enables enumeration. |
| Can a confirmed denied-effect or disclosure violation be correlated to durable state and deployment? | Restricted audit/state query plus safe operational correlation and version markers. | Transport response is the only evidence of what committed. |
| Are sensitive flows observable without account/token values? | Aggregate bounded outcome and throttle states, restricted audit where required, and privacy review. | Account identifiers or raw error text become metric labels. |
| Are telemetry access and retention proportional to data sensitivity? | Owner, access control, purpose, storage locations, retention/deletion, and review evidence. | Broad developer access or indefinite retention accumulates sensitive linkage. |
| Can secret leakage be detected during change review? | Synthetic canaries exercised through success, denial, dependency-error, exception, and retry paths. | Redaction is asserted from logger configuration alone. |
| Does incident diagnostic escalation remain governed? | Predefined authorization, minimum fields, restricted destination, expiry, and rollback to normal level. | Emergency logging captures payloads broadly and remains enabled. |

**Resilience and effect observability checklist**

| question | required_evidence | unsafe_gap |
| --- | --- | --- |
| Are logical operations separated from requests, deliveries, dependency attempts, and worker executions? | Correlation model and reconciliation sample against replay/effect/work state. | Retry amplification and duplicate effects look like ordinary traffic. |
| Are timeout, cancellation, unknown commit, and terminal rejection distinct? | Normalized outcome types plus injected fault observations. | All failures map to one exception/error counter and invite blind retry. |
| Can retry ownership and amplification be located by layer? | Layer/attempt/error/deadline/delay categories with bounded dimensions. | Only final failure is visible while hidden layers multiply attempts. |
| Can blocking and pool pressure be diagnosed? | Executor/thread, connection/resource pool, queue, wait, timeout, and rejection signals aligned to configuration. | Handler latency rises with no visibility into the constrained resource. |
| Can duplicate and replay behavior be reconciled? | New/duplicate/in-progress/conflict/late/replay-store outcomes plus committed effect state. | Request duplicate count is mistaken for effect-integrity proof. |
| Can durable work be followed from acceptance to terminal state? | Accepted, claim, attempt, retry eligibility, age/lag, success, parked, recovery, and retention states. | Lost or abandoned work disappears between endpoint and worker dashboards. |
| Can overload and recovery be distinguished? | Offered/accepted/rejected/queued work, resource state, oldest work, dependency health, and recovery cohort. | Completed operations alone make overload and starvation invisible. |
| Are deployment and configuration changes correlated? | Build/config/schema/feature cohort markers and rollback timeline. | Regression is averaged across incompatible versions. |

**Telemetry pipeline checklist**

| concern | completion_evidence |
| --- | --- |
| Local emission | Contract tests assert event category, bounded fields, omitted sensitive data, and no emission-induced business failure. |
| Export behavior | Queue/buffer bounds, drop/block policy, shutdown/flush semantics, and request-thread isolation are inspected. |
| Transformation | Relabeling, parsing, aggregation, sampling, redaction, and schema version behavior are known in a representative environment. |
| Cardinality | Label value sets are bounded or budgeted; user input, IDs, URLs, exception text, and replay values cannot create unbounded series. |
| Delivery health | Delay, drop, exporter failure, storage/query availability, and alert delivery have their own visible health state. |
| Missing data | Dashboards/alerts distinguish unavailable/partial evidence from an observed healthy count. |
| Access and retention | Authentication/authorization, audit of access where required, retention, deletion, export, and incident exception are governed. |
| Cost and backpressure | Telemetry under load cannot exhaust memory, threads, network, storage, or the same pools needed for recovery. |
| Query/runbook | An owner can execute the first diagnosis query, interpret its limits, correlate with durable state, and choose a safe action. |

**Verification matrix**

| scenario | expected_observability_result |
| --- | --- |
| Valid accepted transition | One logical outcome can be reconciled to its durable effect/work state without exposing sensitive identity. |
| Authentication/authorization denial | Bounded denial category and deployment/correlation evidence; no credential, foreign resource, or protected existence detail. |
| Sequential and concurrent duplicate | Attempts are distinct, logical replay outcome is stable, and effect reconciliation shows the permitted count. |
| Timeout/cancellation before commit | Cancellation/timeout and cleanup are visible; no false accepted terminal event. |
| Response lost after commit | Committed durable outcome remains discoverable and retry is correlated as duplicate/reconciliation, not new effect. |
| Dependency outage with retry | Layer attempts, error classes, remaining budget, admission/queue state, and amplification are visible with bounded cardinality. |
| Worker termination and recovery | Accepted work, abandoned claim/recovery, attempts, age, and terminal state form one explainable lifecycle. |
| Overload | Offered, accepted, rejected, queued, abandoned, completed, and resource states remain interpretable; telemetry health is not silently absent. |
| Synthetic secret failures | Canary values are absent from local output, exported data, traces, metric labels, alert payloads, and error reporting. |
| Telemetry interruption | Missing/partial state is visible, protected behavior remains enforced, and rollout/operation follows the predeclared degraded-evidence rule. |

**Field examples**

Good event: transition class `provider_callback`, outcome `duplicate_accepted`, dependency class `database`, attempt layer `route`, build/config cohort, and an opaque short-lived correlation available only to authorized diagnostics. Durable replay state, not the event, proves effect outcome.

Bad event: log the raw signature header, callback body, tenant ID, invoice ID, provider exception message, and replay key, then place exception text and tenant in metric labels. This creates credential/privacy and cardinality failures while still not proving what committed.

Conditional field: Per-tenant fairness analysis may require tenant-level grouping. Prefer approved restricted query-time joins, coarser buckets, or short-lived access-controlled analysis over persistent broad labels. Record purpose, owner, access, retention, collision, and reidentification risk.

**Telemetry-degraded operation**

- Enforcement, transactionality, idempotency, and durable work ownership must not depend exclusively on a dashboard or exporter.
- When rollout acceptance requires outcome, effect, saturation, or rollback evidence, missing pipeline data is a hold/rollback input under the owned release rule, not a healthy observation.
- Use durable state and narrowly approved diagnostics for containment, but do not silently broaden sensitive logging.
- After restoration, reconcile the evidence gap, determine which claims remain unobserved, and rerun or restage affected checks.

For reference-driven work, continue to record local sources loaded/skipped, exact gates and results, changed paths, evidence status, and unresolved risk in the lane journal. Summaries should be reviewable and preserve decisive output without dumping raw transcripts or sensitive target data.

## Performance Verification Method

Performance verification begins with correctness and an owner-supplied objective. This reference does not prescribe handler latency, throughput, worker lag, recovery duration, allocation, pool size, or reviewer-time thresholds. If no service objective exists, collect a reproducible baseline and the evidence needed for an owner to choose one; do not promote the baseline or a conventional number into a commitment.

**Claim-to-method routing**

| performance_claim | minimum_suitable_method | correctness_or_safety_oracle | escalation_condition |
| --- | --- | --- | --- |
| Pure parser, validator, mapper, or policy computation cost | Focused microbenchmark with representative value distributions and allocation evidence where material. | Identical parse/validation/policy outcomes including boundaries and invalid inputs. | Runtime behavior includes I/O, locks, caches, framework, or coroutine scheduling. |
| Route/service latency | Component or integration workload through actual framework and material dependencies/configuration. | Authorized valid result, denial behavior, commit/durable acceptance, and error contract remain correct under load. | Deployment topology, network, managed dependency, or shared capacity materially affects claim. |
| Blocking/coroutine capacity | Integration load with real execution resources and backing pools plus thread/queue observations. | Cancellation, timeout, resource cleanup, authorization, and no lost/duplicated effects. | Shared production-like infrastructure or autoscaling/instance topology determines saturation. |
| Authentication/signature/hash cost | Controlled valid/invalid/boundary workload against approved configuration. | Security policy and rejection remain unchanged; sensitive material absent from evidence. | Identity/provider infrastructure, cache, rotation, or attacker distribution is not represented. |
| Retry/backpressure behavior | Controlled dependency failure with realistic open/closed arrivals and complete attempt accounting. | Eligible classes retry only within budget; ineligible classes do not; protected writes remain replay-safe. | Provider rate/timeout or network semantics cannot be simulated faithfully. |
| Persistence/idempotency contention | Integration test on actual database/schema/transaction behavior with hot and concurrent replay keys. | Permitted effect count, conflict/duplicate outcome, no stranded reservation, and rollback cleanup. | Production data distribution, isolation, or topology differs materially. |
| Durable worker throughput/lag | End-to-end accepted-work workload including claim, processing, retry, parking, restart, and recovery. | Accepted-to-terminal reconciliation, effect integrity, fairness, and no lost work. | Broker/store/worker deployment and shared dependency limits differ. |
| Recovery performance | Fault, backlog, restart, and live-traffic scenario in a representative isolated or staged environment. | Controlled state is restored without policy bypass, duplicate effects, or hidden unfinished work. | Test cannot safely represent production failure or capacity interactions. |
| Documentation/reference usability | Scenario-based reviewer evaluation and deterministic structural verifier, not runtime handler percentiles. | Reviewer selects correct next action, gate, stop/escalation, and evidence boundary. | A representative evaluation set and scoring authority are needed for quantitative claims. |

**Evidence tiers**

| tier | strength | limitation | valid_conclusion |
| --- | --- | --- | --- |
| Micro | Isolates local code path and supports repeatable mechanism comparison. | Omits framework, scheduling, I/O, queues, contention, and distributed failure. | Scoped local cost under recorded input/runtime configuration. |
| Component/integration | Exercises actual adapters, persistence, framework, pools, and controlled dependencies. | Environment and provider fidelity may differ from deployment. | Behavior and capacity within recorded test topology/workload. |
| Representative staged | Exercises deployment shape, managed dependencies, telemetry, rollout, and contention more faithfully. | Expensive, potentially noisy, and still not all production distributions. | Release decision under declared cohort/environment and guardrails. |
| Passive operational | Captures real traffic, dependencies, topology, and seasonality. | Confounding, sampling, missing data, ethical/privacy constraints, and limited controlled faults. | Observed capability/trend for the instrumented population, not universal causality. |

Use the lowest tier that can falsify the claim, then escalate when omitted boundaries can decide the result. Do not combine tier results into one number; preserve what each tier actually establishes.

**Correctness-first protocol**

1. **Define the claim.** State user/protected outcome, unit, eligible population, workload, environment, target or comparison, and owner. Separate endpoint acknowledgement, dependency time, queue wait, service time, and time to terminal outcome.
2. **Define guardrails.** Name authorization/tenant behavior, validation/error contract, cancellation, replay/effect count, durable acceptance, secret handling, fairness, and resource limits that performance work must preserve.
3. **Discover the actual harness.** Inspect target build wrappers, benchmark/test plugins, profiles, container/service fixtures, deployment configuration, and existing performance conventions before selecting commands.
4. **Freeze the workload record.** Version/hash generator or trace, record random seed, sanitize data, define logical operations and attempts, input/key/tenant distributions, arrival model, valid/invalid/duplicate mix, and fault timeline.
5. **Capture environment and configuration.** Runtime/JDK, Kotlin/framework/dependency versions, process/container resources, topology, dispatchers/executors, connection pools, timeouts, retries, limiters, queues, database state, telemetry, and co-tenancy.
6. **Establish measurement behavior.** Define warm-up, run/sample inclusion, clock boundaries, aggregation, coordinated-omission handling, timer/profiler overhead, and missing/abandoned work accounting.
7. **Run the correctness oracle during load.** Count offered attempts, logical operations, admitted/rejected/cancelled/queued work, correct terminal outcomes, durable effects, duplicates, unknowns, and unfinished records.
8. **Observe distributions and resources.** Record latency or age distributions where meaningful, throughput, CPU, memory/allocation/GC evidence, threads/dispatchers, pools, queues, locks/contention, dependency calls, retries, telemetry health, and fairness dimensions allowed by policy.
9. **Exercise failure, overload, and recovery.** Inject relevant slow/error/unknown-commit/cancellation/restart states without accidentally reducing offered demand unless that behavior is part of the model.
10. **Repeat and compare.** Run compatible repetitions/order randomization where appropriate, report variation and outliers, compare one primary variable at a time, and explain environment drift.
11. **Reconcile durable aftermath.** After load and faults stop, inspect replay/effect/work state, open claims/leases, transactions/resources, parked items, and telemetry gaps.
12. **Make the bounded decision.** Pass, fail, hold for missing evidence, or recalibrate through the accountable owner. Record rollback/revisit triggers and do not extrapolate beyond tested scope.

**Kotlin/JVM and asynchronous measurement checks**

| concern | verification_question | misleading_result_if_ignored |
| --- | --- | --- |
| JIT and warm-up | Are compilation, class loading, caches, connection establishment, and steady behavior separated or intentionally included? | Initialization dominates one version or cold behavior is mislabeled steady state. |
| Allocation and garbage collection | Are allocations, heap pressure, pauses, and collection behavior observed when material? | Lower average latency hides periodic pauses or memory instability. |
| Runtime/GC configuration | Is runtime and relevant configuration identical and recorded across comparison? | Environment change is attributed to code. |
| Coroutine dispatcher | Which threads execute CPU and blocking work, and are waiters/cancellation visible? | `suspend` function appears scalable while blocking shared execution. |
| Backing pools | Do database, HTTP, file, or SDK pools align with executor/concurrency admission? | Hidden queue wait is attributed to handler code or omitted entirely. |
| Structured cancellation | Are cancelled/expired operations counted and do they release permits/resources? | Slow operations disappear from completed latency while continuing work or effects. |
| Async acknowledgement | Does endpoint success mean completed effect, durable acceptance, or volatile scheduling? | Fast response hides queue wait, lost work, or delayed terminal failure. |
| Retry layers | Are caller, gateway, client, driver, broker, and worker attempts counted by logical operation? | Final throughput/latency hides amplification. |
| Telemetry/profiler overhead | Is instrumentation consistent, bounded, and represented in comparison? | Measurement changes behavior or one run pays extra cost. |
| Clock and aggregation | Are start/end clocks, process boundaries, histogram/percentile method, and sample loss documented? | Incompatible distributions are compared or tail behavior is distorted. |

**Validity threats and controls**

| validity_threat | control | prohibited_inference |
| --- | --- | --- |
| Average-only reporting | Report an appropriate distribution plus count, rejects, timeouts, cancelled/unfinished work, and variation. | Average cannot establish tail/deadline behavior. |
| Completed-only denominator | Count offered/admitted/rejected/abandoned/logical/effect states. | Fast completion set cannot prove overload handling or absence of loss. |
| Coordinated omission | Use an arrival model and generator accounting that preserve intended offered schedule where claim requires it. | Closed-loop latency cannot be generalized to open external demand. |
| Mock dependency | State simulated latency/error/commit behavior and corroborate material provider/store semantics. | Mock result cannot establish real integration capacity or failure semantics. |
| Uniform keys/data | Add representative skew, hot replay/resource keys, payload boundaries, and invalid mix. | Uniform workload cannot establish contention/fairness behavior. |
| One run | Repeat and report variation/configuration. | One observed duration cannot establish a stable target. |
| Several simultaneous changes | Isolate variables or use staged attribution with explicit confounders. | Aggregate before/after cannot identify causal improvement. |
| Cache/state contamination | Reset or deliberately preserve state consistently and record it. | Warm/cold or growing dataset differences cannot be attributed to code. |
| Fault reduces offered demand | Keep/open-loop schedule or report demand feedback explicitly. | Lower latency during outage cannot be called resilience improvement. |
| Security control disabled | Keep guardrails enabled and compare control cost only under approved isolated analysis. | Faster unsafe configuration cannot qualify as optimization. |

**Required measurement packet**

| packet_field | required_content |
| --- | --- |
| Claim and owner | Exact bounded claim, objective/comparison, decision owner, and consequence of miss. |
| Outcome semantics | Eligible logical operation, correct success/rejection/duplicate/unknown/unfinished definitions, and effect oracle. |
| Method/tier | Harness, exact command or deployment procedure, tool/plugin version, generator identity, and why tier fits claim. |
| Workload | Arrival, concurrency, duration phases, input/data/key/tenant mix, attempts/retries, faults, and recovery. |
| Environment/configuration | Runtime, dependencies, resources, topology, pools/dispatchers, timeouts/retries, stores, telemetry, and state. |
| Sampling/analysis | Warm-up, included samples, clocks, distributions, aggregation, repetitions, variation, and missing-data behavior. |
| Results | Offered/admitted/rejected/cancelled/queued/completed/logical/effect states plus performance/resource distributions. |
| Guardrails | Negative, cancellation, replay, durability, secret, fairness, and overload outcomes during the run. |
| Uncertainty | Noise, fidelity gaps, confounders, sample/exposure limits, and conclusions not supported. |
| Decision | Pass/fail/hold, owner approval, corrective action, rollout/rollback, and invalidation trigger. |

**Illustrative callback measurement design**

Claim: Under a target-supplied provider callback workload, the chosen synchronous or durable-acceptance path meets its owned acknowledgement objective while preserving authentication, tenant binding, replay effect integrity, bounded resource use, and recovery.

Workload: Target-derived valid events plus invalid/stale signatures, malformed commands, foreign resources, sequential/concurrent duplicates, hot keys, response loss after commit, dependency latency/errors, process restart, and backlog with live arrivals. Record logical event keys separately from deliveries and dependency attempts.

Oracle: For each logical event, reconcile response/acknowledgement, replay record, invoice transition, outbox/work record, and terminal worker outcome. Denied events have no protected effect; duplicates remain within the domain replay contract; accepted deferred work remains recoverable.

Observations: Acknowledgement distribution by outcome, queue wait and work age for deferred model, database/dispatcher/connection/worker resources, contention, retries, attempt amplification, offered/rejected/unfinished work, recovery progression, and telemetry health. Exact target values come from the service owner.

Good evidence: The packet records actual environment and generator, runs correctness assertions during representative load, repeats compatible scenarios, reconciles durable outcomes, and reports variation and fidelity gaps against an owner-approved objective.

Bad evidence: A mock handler is invoked with independent valid inputs, one percentile is compared to inherited numbers, rejected and unfinished work are ignored, and a faster response is called production-ready.

Conditional microbenchmark: Replacing a parsing or canonicalization implementation can be justified locally if property/contract tests prove identical behavior over representative valid and hostile inputs and allocation/runtime effects are measured. If the change alters input bounds, exceptions, coroutine blocking, or downstream call count, escalate to integration evidence.

For this reference itself, structural verifier wall-clock time may be recorded as evidence of one command run. It is not a universal performance target. Reference usability passes qualitatively when a reviewer can identify the correct next decision, gate, stop/escalation, and evidence boundary without unrelated context; quantitative usability claims require a representative evaluation design and owner.

A performance change fails review if it reaches implementation or release before its workload, reliability target, failure modes, correctness oracle, and evidence tier are explicit. It also fails if measured speed comes from weaker authorization, omitted durable work, hidden rejection, cancellation that discards slow samples, repeated effects, or disabled observability.

## Scale Boundary Statement

This reference is sufficient as the primary decision guide for **one protected transition** when one accountable owner can identify the untrusted trigger, actor/authority, resource/effect, commit and acknowledgement boundaries, retry/replay semantics, failure model, operational evidence, and rollback or recovery path.

It remains useful but is no longer sufficient by itself when authority, state, commit, deployment, data jurisdiction, or recovery crosses independently owned boundaries. Add a system-level coordination artifact while retaining one packet per local transition.

**Control scope vocabulary**

Every material control should name its effective scope:

| scope | examples | scale_question |
| --- | --- | --- |
| Coroutine/request | Structured child work, deadline, cancellation, and response. | Does work or effect outlive the caller scope? |
| Process/instance | In-memory limiter, cache, mutex, local telemetry buffer. | Can another instance bypass or conflict with the control? |
| Partition/shard | Broker partition ordering, keyed worker, tenant shard. | Is routing stable and does failover preserve the scope? |
| Service | Database uniqueness, service authorization policy, durable work store. | Do other services emit or mutate the same logical effect? |
| Region/zone | Regional data, routing, identity cache, provider path. | How do failover, replication, and policy versions interact? |
| Organization/global | Identity policy, key custody, data governance, shared replay namespace, platform migration. | Which authority and change process owns consistency? |

Do not describe a local mutex as idempotency across replicas, an instance counter as a tenant-wide rate, a regional record as global uniqueness, or one service's success as an end-to-end terminal outcome unless routing and state contracts prove that scope.

**Scale dimensions and insufficiency signals**

| scale_dimension | this_reference_can_own | signal_to_add_or_escalate | additional_artifact_or_authority |
| --- | --- | --- | --- |
| Authority | One transition's authentication mapping and resource/state authorization under an owned policy. | Several products/services interpret identity or roles differently; policy owner is unclear. | Shared identity/policy decision, compatibility map, and accountable security/domain owners. |
| Commits and effects | One local transaction or durable-acceptance boundary with explicit remote intent. | User outcome spans several independently committed stores/services or irreversible external effects. | Journey state model, saga/compensation or reconciliation design, and terminal-outcome owner. |
| Replay and ordering | One service/partition key scope and retention contract. | Same logical operation can enter through several channels, regions, services, or key versions. | Global/partitioned identity namespace, canonicalization/versioning, conflict and late-replay policy. |
| Deployment | One service rollout with compatible local state and rollback. | Mixed versions across producers/consumers/stores interpret schema, events, or outcomes differently. | Compatibility matrix, migration choreography, versioned contracts, staged rollout, and rollback plan. |
| Data boundary | One owned classification, tenant scope, storage, and retention. | Cross-jurisdiction transfer, regulated processing, shared analytics, or deletion/audit obligations span systems. | Data-governance/privacy/legal review and end-to-end lineage. |
| Cryptography and keys | Use an approved local client/configuration boundary. | Protocol design, key custody, rotation, federation, or compromise response changes. | Security/cryptography authority and governed key/incident lifecycle. |
| Workload and capacity | Declared workload on one service and its material dependencies. | Multi-region traffic, shared platform contention, fleet-wide retry/recovery, or unknown production objective decides behavior. | System capacity model, service objectives, staged load/failover evidence, and platform ownership. |
| Failure and recovery | Local fault, restart, retry, parking, rollback, and dependency recovery. | Partial outage, failover, disaster recovery, or incident command spans independent systems. | System reliability plan, incident process, recovery objectives, and cross-service exercises. |
| Shared component | Representative behavior for one component and known consumers. | Library/filter/client/runtime change has broad or unknown consumer blast radius. | Consumer inventory, compatibility/migration, representative matrices, rollout guardrails, and central rollback. |
| Source/code discovery | Bounded files, owners, paths, and dependency/effect graph for the transition. | Search is unbounded, generated/dynamic paths obscure behavior, or source authority conflicts. | Dependency/source graph narrowing, ownership map, runtime/configuration discovery, and evidence hierarchy. |
| Assurance | Normal engineering review proportional to effect/exposure. | Irreversible, regulated, high-sensitivity, high-fan-out, or material financial/safety effect needs independent acceptance. | Governed threat/risk review, independent validation, audit evidence, and formal approval. |

**Split strategy**

Use authority and commit boundaries as the primary split, then align team and theme work around them:

```text
end-to-end user promise
  -> transition A: ingress/authentication/durable acceptance (owner A, commit A)
  -> transition B: worker/domain effect (owner B, commit B)
  -> transition C: provider effect/reconciliation (owner C, external state)
  -> terminal outcome and user/operator visibility (journey owner)
```

Each transition packet specifies local authority, input, effect, acknowledgement, replay, failure, evidence, and recovery. The coordination artifact specifies how identity/policy context, correlation/replay identity, version, order, terminal outcome, timeout, compensation/reconciliation, and ownership cross the handoff.

| split_option | advantage | principal_risk | use_condition |
| --- | --- | --- | --- |
| By protected transition/commit | Preserves causal behavior and local proof. | May cross team/file boundaries and need coordination. | Preferred foundation for state-changing distributed workflows. |
| By service/team ownership | Aligns delivery and operational responsibility. | User journey and duplicate/terminal semantics can fall between teams. | Map each service packet to an explicit journey owner and interface contract. |
| By theme (security, testing, operations) | Enables specialist depth and parallel review. | Specialists can make incompatible assumptions or leave implementation gaps. | Freeze shared transition/policy facts and return claim-specific artifacts to one owner. |
| By data/jurisdiction | Makes access, retention, and transfer authority explicit. | Functional workflow can fragment and duplicate transformations. | Data governance materially differs across stores/regions. |
| By release/migration unit | Supports compatibility and rollback. | Temporary mixed state may be under-modeled. | Version overlap and migration sequence determine safety. |

**Minimum cross-boundary coordination contract**

| contract_item | required_decision |
| --- | --- |
| End-to-end outcome | What the user/provider is promised and which state proves terminal success, valid rejection, unknown, or failure. |
| Authority propagation | Which identity/policy facts cross boundaries, who may trust them, how freshness/revocation works, and where resource authorization repeats. |
| Message/interface schema | Version, compatibility, bounds, sensitive fields, validation ownership, and unknown/unsupported behavior. |
| Logical/replay identity | Scope, canonicalization, privacy, propagation, uniqueness, retention, and conflict across entry paths. |
| Ordering and concurrency | Partition/key guarantees, reordering, concurrent versions, late messages, and conflict arbitration. |
| Commit/acknowledgement | What each acknowledgement proves, ambiguity windows, and the owner of unfinished or unknown outcomes. |
| Retry and deadline | Attempt owner per layer, total journey deadline, durable delay, backpressure propagation, and recovery ramp. |
| Compensation/reconciliation | Which effects are reversible, how divergence is detected, who acts, and what durable state records completion. |
| Observability/audit | Safe correlation, independent durable state, bounded outcomes, version/deployment markers, access, and missing-data behavior. |
| Change and invalidation | Which schema/policy/configuration changes reopen which component and end-to-end gates. |
| Incident/rollback owner | Who may contain, halt, roll back, replay, rotate, or accept risk across owners. |

**Verification at scale**

1. Keep focused component positive, negative, cancellation, replay, fault, resource, and redaction gates.
2. Add producer-consumer contract and compatibility tests across supported versions and unknown fields/outcomes.
3. Exercise mixed-version rollout and rollback against representative durable state, queues, replay records, and configuration.
4. Inject partial dependency/service/region failure and verify deadline, backpressure, authority, durable handoff, and reconciliation.
5. Exercise duplicate, delayed, reordered, concurrent, and cross-entry-path logical operations across independently committed stores.
6. Reconcile end-to-end terminal outcomes from independently durable states rather than relying on one service response.
7. Run backlog plus live traffic during recovery and observe fairness, shared capacity, retry synchronization, and oldest unfinished work.
8. Validate safe correlation, audit access, telemetry health, and rollback signals across versions/owners.
9. Record fidelity gaps and require staged or governed evidence for claims that local environments cannot establish.

**Examples**

Good distributed split: An endpoint verifies and durably accepts a callback, a worker applies the tenant-scoped invoice transition, and an outbox worker notifies a provider. Each has a packet and commit. A journey contract owns replay identity, policy context, terminal state, unknown outcome, compensation/reconciliation, and cross-service tests.

Bad distributed scope: One checklist says the three services process the callback exactly once and are secure. It does not identify separate commits, redeliveries, policy versions, effect ownership, or recovery, so local green tests cannot establish the claim.

Conditional shared database: Two services can coordinate through one transactional store, but that may create schema ownership, lock contention, deployment coupling, and rollback constraints. Treat them as one commit boundary only when transaction authority, migration compatibility, and operating ownership are explicit.

Shared platform change: A small authentication filter or provider client can exceed local scale because many services depend on it. Inventory consumers, preserve compatibility, test representative principal/error/retry behavior, stage adoption, and retain a central rollback. Small diff size is not small blast radius.

**Large-codebase discovery**

- Narrow from service entry points, security configuration, consumers/workers, persistence writes, external clients, and deployment manifests.
- Use dependency/source graph tooling when available, but verify dynamic framework registration, reflection, configuration, generated code, and runtime routes separately.
- Rank evidence by claim authority; a long source list without ownership, relevance, and target execution is not sufficient.
- Stop discovery when the protected transition, affected paths, owners, and verification surface are bounded; reopen when evidence contradicts the model.

**Parallel agent/shared-workspace execution**

- Assign one exclusive writer per reference, packet, transition, or other atomic artifact. Parallel agents must not rewrite the same file without an explicit integration owner and merge checkpoint.
- Freeze shared policy, schema, heading, source, and evidence inputs or record coordinated versions before independent work begins.
- Save packet/decision evidence before implementation, persist at each atomic boundary, and journal in bounded intervals so handoff does not depend on conversational memory.
- Treat unexpected shared-file changes as external state: do not revert them; verify whether they invalidate the owned work and escalate only when coexistence is impossible.
- Integrate through exact paths, hashes or versions where required, contract tests, cross-boundary scenarios, and one owner for final end-to-end verification.

Long-running work should treat context drift as a reliability failure. Persist current state, completed evidence, unresolved owners, changed paths, and the next concrete action; reread the governing specification and affected artifact in bounded groups. This keeps scale from turning implicit memory into an unreviewable coordination dependency.

Escalation adds the missing system/governance layer; it does not discard local evidence. The end state is a graph of bounded transition packets with explicit handoffs and a journey owner, not one enormous document that no individual can verify or a collection of local proofs with no owner for the user-visible outcome.

## Future Refresh Search Queries

No query below was executed for this edition because browsing was prohibited. Every row has status `unexecuted_no_browse`; it is a future research route, not external evidence. Preserve the three inherited query strings exactly when comparing editions.

Before executing any query, inspect the target build files, dependency locks/catalogs, framework configuration, deployment manifests, client model, and provider contracts. Add the exact discovered version and feature to the future search when version-specific behavior matters. Current documentation for a different release line is not automatically applicable.

| search_query_label_name | search_query_text_value | intended_source_lane_and_claim | execution_status |
| --- | --- | --- | --- |
| `official_docs_query_phrase` | kotlin backend security resilience official documentation best practices | Broad vocabulary/orientation only; narrow to official Kotlin/framework/security sources before claim promotion. | `unexecuted_no_browse` |
| `github_repository_query_phrase` | kotlin backend security resilience GitHub repository examples | Example discovery only; inspect provenance, version, license, policy, tests, and upstream primary sources before use. | `unexecuted_no_browse` |
| `release_notes_query_phrase` | kotlin backend security resilience changelog release notes migration | Broad release/migration discovery; narrow to actual target dependencies and versions. | `unexecuted_no_browse` |
| `kotlin_coroutine_cancellation_official_query` | site:kotlinlang.org/docs coroutines cancellation structured concurrency exception handling Kotlin | Official Kotlin guidance for cancellation propagation, child ownership, and exception behavior. | `unexecuted_no_browse` |
| `kotlin_coroutine_timeout_official_query` | site:kotlinlang.org/docs coroutines timeout cancellation blocking thread Kotlin | Official Kotlin guidance for timeout/cancellation semantics and limits of suspending versus blocking work. | `unexecuted_no_browse` |
| `kotlin_coroutines_release_history_query` | site:github.com/Kotlin/kotlinx.coroutines releases migration cancellation dispatcher | Maintainer release/migration history for target coroutine dependency behavior after local version discovery. | `unexecuted_no_browse` |
| `spring_security_kotlin_configuration_query` | site:docs.spring.io/spring-security/reference Kotlin DSL authentication authorization servlet current | Official Spring Security reference for target-stack Kotlin configuration and auth boundary behavior. | `unexecuted_no_browse` |
| `spring_security_resource_authorization_query` | site:docs.spring.io/spring-security/reference method authorization request authorization Kotlin | Official Spring Security mechanisms; domain resource policy still requires local authority and tests. | `unexecuted_no_browse` |
| `spring_security_csrf_browser_query` | site:docs.spring.io/spring-security/reference CSRF cookie browser client Kotlin | Official Spring Security CSRF behavior and configuration for the discovered client/credential model. | `unexecuted_no_browse` |
| `spring_security_password_storage_query` | site:docs.spring.io/spring-security/reference password storage Argon2 bcrypt migration | Official password encoder/storage and migration guidance, reconciled with current organization security policy. | `unexecuted_no_browse` |
| `spring_security_release_migration_query` | site:docs.spring.io/spring-security/reference migration release notes security configuration Kotlin | Official migration guidance for changed defaults, deprecations, and configuration after target version discovery. | `unexecuted_no_browse` |
| `ktor_authentication_official_query` | site:ktor.io/docs server authentication authorization Ktor | Official Ktor authentication/authorization plugin guidance for the target version and principal model. | `unexecuted_no_browse` |
| `ktor_validation_error_query` | site:ktor.io/docs server request validation status pages error handling Ktor | Official Ktor request-validation and error-mapping mechanisms; domain invariants remain local. | `unexecuted_no_browse` |
| `ktor_release_migration_query` | site:ktor.io/docs migration release notes server authentication Ktor | Official Ktor migration/release behavior after local version and plugin discovery. | `unexecuted_no_browse` |
| `owasp_password_storage_query` | site:owasp.org Password Storage Cheat Sheet Argon2id bcrypt | Security-standard guidance to reconcile with organization-approved password policy and platform support. | `unexecuted_no_browse` |
| `owasp_csrf_query` | site:owasp.org Cross Site Request Forgery Prevention Cheat Sheet cookie | Security-standard browser request-integrity guidance, scoped to actual credential transport. | `unexecuted_no_browse` |
| `owasp_logging_query` | site:owasp.org Logging Cheat Sheet secrets tokens session identifiers | Security-standard logging/redaction guidance for field classification, access, and incident diagnostics. | `unexecuted_no_browse` |
| `owasp_rest_security_query` | site:owasp.org REST Security Cheat Sheet authentication authorization input validation | Security-standard API boundary guidance to compare with framework and local domain policy. | `unexecuted_no_browse` |
| `jvm_runtime_measurement_query` | site:docs.oracle.com Java performance JIT garbage collection measurement benchmarking | Primary runtime documentation for JVM measurement assumptions after target runtime discovery. | `unexecuted_no_browse` |
| `database_retry_transaction_query` | official database documentation transaction retry deadlock serialization failure idempotency | Target database primary documentation for exact retryable transaction failures and rollback semantics. | `unexecuted_no_browse` |
| `message_broker_redelivery_query` | official message broker documentation redelivery acknowledgement visibility lease dead letter | Target broker primary documentation for claim, redelivery, ordering, parking, and restart semantics. | `unexecuted_no_browse` |
| `provider_idempotency_query` | official provider API documentation idempotency retry timeout reconciliation | Target provider primary documentation for replay key, unknown commit, retry, and reconciliation after provider identity is known. | `unexecuted_no_browse` |
| `provider_security_callback_query` | official provider API documentation webhook callback signature verification replay timestamp | Target provider primary documentation for signed representation, freshness, replay, rotation, and error behavior. | `unexecuted_no_browse` |

The final four generic primary-source queries must be rewritten with the actual database, broker, and provider names and discovered versions before execution. Their current text is an explicit route-construction instruction and cannot support a technical claim.

**Query-lane priority**

| source_lane | use | caution | stop_condition |
| --- | --- | --- | --- |
| Official current guide/API reference | Determine supported mechanism, default, configuration, and semantic contract for the target version. | Current page may describe a different release line or omit target customization. | Applicable claim and version scope are explicit and target behavior has a verification path. |
| Official release/migration/security advisory | Identify changed defaults, deprecations, compatibility, and security-relevant fixes. | Publication date differs from affected/released versions; advisory may require a migration path. | Affected target state and required change are established. |
| Organization policy/decision | Decide permitted algorithms, identity semantics, authorization, data, risk, and incident actions. | External best practice cannot override accountable local policy. | Decision is approved and linked to implementation/evidence. |
| Maintainer source/tests/issues | Clarify implementation edge cases or documentation gaps. | Issue/comment may be provisional, version-specific, or unresolved. | Behavior is corroborated in applicable source/tests/release and target gate. |
| Independent security standard | Add threat/control context and challenge local assumptions. | Must be reconciled with framework, target, and organization policy. | Decision-driving control is scoped and verified locally. |
| Repository example/blog/forum | Discover vocabulary and candidate practice. | May be stale, insecure, unlicensed, incomplete, or context-free. | Trace to primary evidence or keep as an unpromoted lead. |

**Future refresh record**

For each executed query, record:

| record_field | required_content |
| --- | --- |
| Trigger | Invalidated policy, version, provider, incident, test failure, or unresolved target decision that required research. |
| Query | Exact text, search system, date/time, and any domain/version filters. |
| Result identity | Canonical URL, publisher/maintainer, document title, publication/update date when available, and version scope. |
| Claim extraction | Concise paraphrase tied to exact page location; avoid excessive quotation. |
| Source role | Primary documentation, release/advisory, policy, source/test, standard, example, or duplicate. |
| Applicability | Target dependency/configuration/client/deployment match and assumptions. |
| Conflict | Local or external disagreement, authority for resolution, and confidence effect. |
| Target representation | Exact code/configuration/schema/policy path that adopts or contradicts the claim. |
| Verification | Executable negative/fault/compatibility/performance gate or accountable observation. |
| Decision | Adopt, adapt, reject, defer, and the reason plus invalidation trigger. |

**Promotion checklist**

1. Open and read the complete relevant primary page, not only a result snippet.
2. Confirm publisher, canonical location, target version/release line, and effective date.
3. Extract only the claim needed for the decision and record its scope and exceptions.
4. Check release/migration history when behavior or defaults may have changed.
5. Inspect target code/configuration to determine whether the documented mechanism applies or is overridden.
6. Resolve policy-sensitive choices through accountable local authority.
7. Identify duplicate upstream sources and do not count repeated summaries as corroboration.
8. Preserve conflicts and uncertainty rather than selecting the most convenient result.
9. Verify material behavior in target tests or a controlled representative environment.
10. Update only affected claims, evidence labels, examples, gates, and invalidation links.

**Result rejection conditions**

- Search snippet or generated summary without the underlying source.
- Page for an inapplicable major/version/configuration or an archived/unsupported line presented as current.
- Repository example without relevant negative/fault tests, policy context, license/provenance, and target compatibility.
- Recommendation that invents authorization, cryptographic, retention, or risk policy outside its authority.
- Performance or reliability claim without workload, environment, measurement method, and uncertainty.
- Source that repeats this reference or the same upstream prose and is presented as independent confirmation.

Good future query: After local discovery finds Spring Security and a cookie-authenticated browser route, execute a version-narrowed official CSRF/configuration query to decide framework mechanism, then verify the actual client and negative cross-site behavior. Keep domain authorization separate.

Bad future query: Search "secure Kotlin backend," copy the first repository's configuration, and mark the reference refreshed. The result has no target version, authority, threat model, or behavior evidence.

Borderline inherited query: `kotlin backend security resilience official documentation best practices` can discover vocabulary and likely primary domains, but no result should be promoted until it is narrowed to a decision and applicable source.

Stop searching when the decision has sufficient authority, target applicability, conflict resolution, and a verification path. More result volume is not greater confidence. Retire a query when its claim no longer exists, split it when several decisions have become entangled, and add a new route when an incident or dependency change reveals a previously unmodeled assumption.

## Evidence Boundary Notes

Evidence status attaches to a claim, not to the document as a whole. A claim can have strong source integrity but uncertain authority, currentness, target applicability, or execution coverage. Preserve these distinctions when copying guidance into plans, reviews, tests, or agent prompts.

**Evidence labels**

| evidence_label | use_when | minimum_record | does_not_prove |
| --- | --- | --- | --- |
| `local_corpus_sourced_fact` | The claim is directly supported by a mapped local source heading or passage. | Exact local path, heading/location, frozen identity where required, and faithful paraphrase. | Current ecosystem behavior, organization approval, target adoption, or passing execution. |
| `external_research_sourced_fact` | A future edition has opened and reviewed an applicable external primary source. | Canonical URL, publisher, retrieval date, document/update and target version scope, exact claim, and source role. | Local policy, target configuration, or runtime outcome. No claim in this edition has this status because browsing did not occur. |
| `combined_evidence_inference_note` | Guidance combines sourced constraints with explicit assumptions or reasoning. | Input claims, inference, alternatives, boundary, counterexample, and verification route. | Direct source wording or universal truth. In this no-browse edition, combination is local evidence plus systems reasoning, not local-plus-refreshed-public corroboration. |
| `target_repository_verified_fact` | Exact target code, configuration, schema, ownership, or tests were inspected. | Path/location, relevant version/configuration, observed fact, and scope. | Intended policy, production behavior, or correctness merely because code exists. |
| `accountable_policy_decision` | A responsible owner approves authorization, identity, cryptography, data, retention, incident, objective, or risk choice. | Decision, owner/authority, scope, date/version, rationale, and review trigger. | Correct implementation or effective enforcement. |
| `executable_verification_result` | A command/test/analysis was run and its assertions support a bounded property. | Exact command, code/configuration under test, environment/profile, result, meaningful output, and coverage limit. | Untested cases, production topology, policy legitimacy, or permanent readiness. |
| `operational_observation` | A deployed or representative environment produced a metric, trace, log, audit, state, or runbook result. | Environment/cohort, time/window, definition version, query, data health, observation, uncertainty, and owner interpretation. | Causality, absence outside observed coverage, or correctness when telemetry is incomplete. |
| `illustrative_scenario_assumption` | An example uses invented actors, provider behavior, data, or code shape to explain a decision. | Explicit illustration label, assumptions, omitted contracts, and target-replacement requirement. | Existence, API compatibility, compilation, policy, or production fitness. |
| `unresolved_judgment_or_unknown` | Authority, applicability, target fact, objective, or evidence is unavailable or disputed. | Exact question, consequence, safe interim state, responsible owner/source, next action, and dependent claims. | Permission to guess or present a provisional choice as ready. |
| `process_conformance_result` | Structural tests and workflow checks establish this reference edition's acceptance criteria. | Exact verifier/command, paths, result, hashes/counts, and external failing scope if any. | Security or resilience of an application described by the reference. |

The inherited label `combined_evidence_inference_note` originally described synthesis combining local and public evidence. Because this edition performed no browsing, use it only with an explicit note that the external side remains unrefreshed. Do not imply that the URLs or future search queries were opened.

**Edition-level knowns**

| edition_fact | evidence_status | boundary |
| --- | --- | --- |
| The archive seed is `agents-used-monthly-archive/idiomatic-references-202606/generated-references/kotlin_backend_security_resilience.md` with baseline SHA-256 `74c1872fa32c445a33abb9458634322c71e71af25b21c59cecc2fa631c53d507`. | Local integrity/process fact. | Identifies the seed and original 26-heading baseline; does not validate its recommendations or inherited numeric targets. |
| One topical local source is mapped: `agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/references/kotlin-backend-security-and-resilience.md`, SHA-256 `8a07eb77e27a3b508224db76c60e20508b8b3d13b81fce86e87ea052be7d14a5`. | `local_corpus_sourced_fact` plus integrity. | The complete source was read; one file provides breadth but not independent corroboration, current framework proof, or organization policy. |
| The mapped source covers trust boundaries, authentication/authorization, passwords/tokens/sessions, CSRF/browser context, validation, coroutine resilience, blocking/dispatchers, retries, idempotency, external clients, background work, and review checks. | `local_corpus_sourced_fact`. | Supports concern categories and conceptual constraints, not target-specific values or APIs. |
| The shared evolution specification and structural tests were read before editing. | Process workflow fact. | Establishes awareness of edition requirements, not topical authority. |
| No external URL or search query was opened. | Process/evidence-boundary fact. | External maps and Section 025 are unrefreshed discovery routes; no current external corroboration exists in this edition. |
| Operational examples, matrices, workload dimensions, target schemas, and verification methods in evolved sections extend beyond the source's concise prose. | `combined_evidence_inference_note`. | They are systems reasoning constrained by local guidance and must be reconciled with target policy, architecture, dependencies, and evidence. |
| Inherited scores, fixed workload counts, latency thresholds, routing sample counts, and one-session targets lacked target measurement/authority. | Critical synthesis finding. | This edition reframes them as editorial provenance or target-owned decisions rather than preserving unsupported precision. |

**Confidence dimensions**

Do not compress confidence into one high/medium/low label when the decision is material:

| dimension | question | example_of_divergence |
| --- | --- | --- |
| Integrity | Is this the exact artifact/version that was read or executed? | A hash can be exact while the content is outdated. |
| Authority | Does the source or person own this kind of decision? | Framework docs explain a mechanism but cannot approve business authorization. |
| Relevance | Does the claim address the same transition, effect, client, and failure mode? | General retry guidance may not apply to an unknown-commit write. |
| Freshness | Does version/date/configuration match the target? | Current docs for another release line may be less applicable than older target-version docs. |
| Target adoption | Is the recommendation represented in target code/configuration/schema/policy? | Well-sourced CSRF guidance does not show that a route preserves protection. |
| Execution coverage | Did a gate exercise the promised positive, negative, concurrency, fault, and recovery behavior? | Unit tests can pass while concurrent replay remains untested. |
| Operational coverage | Was deployed/representative behavior observed with healthy telemetry and appropriate workload? | Integration success does not establish fleet recovery under backlog. |
| Independence | Do corroborating artifacts have distinct provenance or observations? | Several summaries may all repeat one upstream paragraph. |
| Uncertainty | What remains unobserved, disputed, sampled, inferred, or environment-dependent? | No alert is weak evidence if the telemetry pipeline was unavailable. |

**Evidence-state transition**

```text
discovery lead
  -> reviewed sourced claim
  -> applicable authority/policy decision
  -> target representation
  -> executable bounded result
  -> staged/operational observation
  -> maintained claim with invalidation triggers

At any stage:
  contradiction, version change, failed gate, telemetry loss, or scope change
  -> demote affected claim and reopen dependent transitions
```

Skipping a step creates a category error: a listed URL is not a reviewed claim; a reviewed claim is not local policy; policy is not implementation; implementation is not verified behavior; a test is not production observation; silence is not operational success.

**Prohibited inferences**

| observed_artifact | prohibited_conclusion | required_next_evidence |
| --- | --- | --- |
| Local topical guidance | "The target is secure/resilient." | Target policy, representation, adverse gates, and operational evidence. |
| External URL or unexecuted query | "Current official guidance agrees." | Open/read applicable primary source and record version/claim. |
| Current official documentation | "The target uses this behavior." | Inspect configuration/code and execute behavior-specific gate. |
| Existing target code | "This is intended policy and correct." | Accountable decision plus reproducing/negative/fault evidence. |
| Passing happy-path test | "Authorization, retry, replay, and recovery are complete." | Relevant negative, concurrency, fault, restart, and effect assertions. |
| Integrity hash | "The source is true or authoritative." | Semantic review, role, applicability, and corroboration as needed. |
| Many citations | "The claim is independently corroborated." | Trace upstream provenance and distinct observation. |
| Successful response | "The effect committed once and durably." | Durable state/replay/work reconciliation and response-loss test. |
| No operational alert | "No violation occurred." | Telemetry health/coverage plus durable/audit and deterministic evidence. |
| Passing document verifier | "A Kotlin backend implementation is production-ready." | Target build/test/security/fault/operational gates. |

**Minimum evidence chains**

| claim_strength | minimum_chain |
| --- | --- |
| Conceptual recommendation | Topical source or explicit inference, applicability assumptions, alternatives/limit, and target verification question. |
| Implementation plan | Recommendation plus target architecture/code/configuration discovery, policy owners, acceptance/fault matrix, and exact planned gates. |
| Corrected implementation | Plan plus current changed paths, target gate results, adverse evidence, residual uncertainty, and invalidation triggers. |
| Deployment readiness | Corrected implementation plus compatibility/migration, representative workload, observability/data health, staged/rollback evidence, and accountable acceptance. |
| High-assurance claim | Deployment chain plus independent threat/policy review, adversarial/recovery evidence, governed audit, and explicit risk authority. |

**Boundary audit procedure**

1. Select each decision-driving claim, numeric target, security assertion, framework behavior, performance statement, and readiness conclusion.
2. Identify exact source/artifact location and assign the claim-specific evidence label.
3. Check integrity, authority, relevance, freshness, target adoption, execution/operational coverage, independence, and uncertainty.
4. Split paragraphs or table rows that mix sourced fact, target fact, and inference in ways that change action.
5. Trace duplicates to upstream provenance and remove false corroboration.
6. Rerun current gates or mark evidence historical/unavailable; inspect whether the gate would fail for a representative unsafe state.
7. Demote claims whose source, version, assumptions, or evidence no longer support the stated scope.
8. Update only dependent guidance, examples, targets, and invalidation links; preserve unaffected evidence.

**Examples**

Good chain: `local_corpus_sourced_fact` supports transient-only bounded retry and replay safety. `target_repository_verified_fact` identifies the actual external client, lower-layer attempt behavior, and stable key. `accountable_policy_decision` defines eligible errors and unknown-commit response. `executable_verification_result` proves deterministic failures do not retry, transient attempts remain within deadline/capacity, cancellation propagates, and response loss does not repeat the effect. `operational_observation` later confirms amplification and resource behavior under the owned workload. Each link supports a different conclusion.

Bad chain: "This reference says retries are resilient, the code uses a retry helper, and tests pass; therefore production writes are safe." The reference certifies itself, helper semantics are uninspected, policy/commit ambiguity is absent, and test scope is unknown.

Borderline future chain: An official documentation query is listed for Spring Security CSRF. In this edition it remains `unresolved_judgment_or_unknown`, not `external_research_sourced_fact`. After future review it may establish current mechanism for the target version; target client/credential analysis, configuration inspection, and browser negative tests are still required.

**Reuse protocol**

- Copy the claim with its label, source/authority, target assumptions, limitation, and verification status; do not copy only the recommendation sentence.
- Replace illustrative provider/framework/code details with inspected target facts.
- Preserve `unexecuted_no_browse` status until external primary sources are actually reviewed.
- Do not turn owner-supplied fields for reliability, workload, scale, retention, retry, or performance into generic defaults.
- When a new target fact conflicts, record the contradiction and demote the affected inference rather than rationalizing it to preserve completion.
- At handoff, record unresolved decisions, owners, safe interim state, exact gates/results, changed paths, and next concrete action.

The evidence graph is intentionally non-monotonic. New information can reduce confidence. That is a feature: a failed negative test, changed identity mapping, incompatible provider release, or missing telemetry should reopen the affected claim instead of being hidden by earlier green evidence. Strong guidance remains decisive by naming the default, its assumptions, the counterexample that defeats it, and the evidence that can confirm or overturn it.
