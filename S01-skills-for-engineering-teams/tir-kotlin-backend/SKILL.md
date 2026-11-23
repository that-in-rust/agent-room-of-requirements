---
name: tir-kotlin-backend
description: Plan, build, harden and review Kotlin backend services and the Kotlin code inside them, with Spring Boot or Ktor, coroutines, typed configuration, persistence, migrations, tests and fixtures, security, resilience and runtime operations. Use when the task is a Kotlin HTTP API, worker, scheduled job, message consumer, external client or migration; when Kotlin code crosses a Java, serialization, database or coroutine boundary (platform types, `!!`, `lateinit`, `GlobalScope`, a broad catch around suspend work, blocking code marked `suspend`); when choosing a Spring test slice, Ktor `testApplication` or Testcontainers; when adding retries, idempotency, timeouts, health checks, graceful shutdown or rollout gates to a JVM service; or when reviewing agent-written Kotlin before merge. Not for Android UI or Kotlin Multiplatform client work, not for Kotlin/JS or other non-JVM targets, not for basic Kotlin syntax tutoring, not for migrating between Spring and Ktor inside a feature task, and not for Java-only services.
---

# Kotlin Backend

## Purpose

Turn a Kotlin backend request into a decision-complete work packet and then into verified code. The packet is spec-first, Kotlin-idiomatic, framework-aware and biased toward production behavior. The Kotlin inside the service is held to one standard:

> Reliable Kotlin makes ambiguity visible at boundaries and keeps the core small, non-null, typed and cancellation-aware.

Syntax serves the contract. It is not the contract. A `.kt` file alone proves nothing about which rules apply; the accepted outcome, the surface and the strongest failure decide.

This skill does two jobs that share one code base:

- **Backend delivery.** Service anatomy, Spring Boot and Ktor rules, persistence and transactions, tests and fixtures, security, resilience, configuration, observability, migrations, CI and rollout.
- **Kotlin language reliability.** Nullability, Java platform types, value classes, sealed outcomes, data classes, scope functions, coroutines, cancellation, blocking boundaries, Java interop and public compatibility.

When the backend outcome leads (transactions, authentication, migrations, health, deployment, recovery), the language rules act in support and answer one named interface question. When Kotlin or JVM semantics own the outcome (a type, a null, a coroutine scope, a Java signature), the language rules lead and the backend rules join only when a remote call, lifecycle or deployment concern appears.

## When to use

- A Kotlin HTTP API, Spring MVC or WebFlux service, Ktor service, worker, scheduled job, message consumer, migration, external client or review pass.
- A service refactor, a production-readiness review or a JVM backend architecture decision inside an existing service.
- Untrusted data enters through a route, message, callback, scheduler, configuration value, token claim or provider response.
- A timeout, cancellation, retry, duplicate, restart or partial commit can change the result.
- Agent-authored Kotlin is about to be reviewed or committed. This includes modified adapters, new suspend paths and Java wrapping, not only new files.
- A reviewer needs to decide whether `!!`, `lateinit`, `GlobalScope`, a broad catch, a data-class entity, a boolean result or a mutable global is acceptable in one place.
- A security, resilience, performance or readiness claim needs proof, or a framework default conflicts with the owner's policy.

## When not to use

- Android UI work or Kotlin Multiplatform client work.
- Kotlin/JS or other non-JVM targets. The Java interop rules here are meaningless there; scope the work to JVM modules or split it.
- Basic Kotlin syntax or "what is a data class" questions. Use the language documentation.
- Platform selection: a Spring-to-Ktor or Ktor-to-Spring migration, mixed servlet, reactive and coroutine models without an owned boundary, or unknown production constraints. Those need an architecture decision with workload, team and operations evidence. Recommending Ktor because coroutine syntax is concise is the standard wrong answer.
- Deciding business permissions, tenant rules, retention, credential lifetime, acceptable threat, cryptographic parameters, compliance scope or service level objectives. Route those to their accountable owners; this skill supplies constraints and gates, not authority.
- Authorizing production changes. Nothing here authorizes a destructive migration, secret rotation, traffic change, production fault injection, deployment or recovery command. Those need the target procedure, authorization, a blast-radius review, a stop plan and a named owner.
- A pure behavior-preserving edit. Do not run the whole workflow merely because the code is Kotlin or mentions authentication. Use focused checks until discovery shows a changed transaction scope, retry behavior, principal mapping or secret exposure.

## Framework stance

- Prefer Kotlin plus Spring Boot when the repository already uses Spring, JPA, Spring Security, Actuator, servlet MVC or WebFlux, or enterprise JVM conventions.
- Prefer Ktor when the repository is explicitly Ktor-first, lightweight and plugin-first, coroutine-native or multiplatform-adjacent.
- Preserve the existing framework, build tool, wrapper, Java target, Kotlin version, Spring Boot or Ktor version, compiler settings, database stack, test framework, static-analysis baseline, telemetry, CI and deployment model unless the request explicitly includes a migration.
- Spring and Ktor are not interchangeable syntax. Framework idioms are dependency-topology decisions: scheduler, transaction, serializer, proxy and lifecycle assumptions matter more than concise code.
- Select Spring MVC for blocking persistence. Use WebFlux or coroutines only when the dependencies are non-blocking. Use coroutine-first Ktor when its dependencies support that model. Isolate mixed models at one explicit boundary.

## Mode selection

Choose the modes before planning or coding. One mode leads; add a support mode only for a named interface question.

Backend modes:

| Mode | Use for |
| --- | --- |
| `Spec Mode` | Vague requests, missing acceptance criteria, greenfield service work that needs `REQ-KOTLIN-BACKEND-*` contracts |
| `Spring Boot Mode` | Controllers, services, repositories, validation, configuration properties, Spring Security, Actuator, MVC or WebFlux, Spring Data, Flyway or Liquibase, Spring test slices |
| `Ktor Mode` | Routes, plugins, content negotiation, status pages, resources and type-safe routing, Ktor auth, `testApplication`, coroutine-native request handling |
| `Persistence Mode` | JPA or Hibernate, Spring Data, Exposed, jOOQ, JDBC or R2DBC, transaction scope, migrations, repository boundaries, query performance |
| `Coroutine Mode` | Suspend APIs, Flow, dispatcher choice, cancellation, timeouts, structured concurrency, blocking-call isolation |
| `Security Mode` | Auth, sessions, JWT, OAuth2 and resource-server flows, CSRF, password storage, reset flows, validation, anti-enumeration behavior |
| `Resilience Mode` | Retries, idempotency, external clients, durable background work, transaction boundaries, timeout budgets, failure classification |
| `Operations Mode` | Typed config, secrets, profiles, logging, tracing, metrics, health checks, CI, containers, deployment, rollout safety |
| `Review Mode` | Architecture drift, production readiness, framework misuse, Kotlin anti-patterns, test strategy review |

Language modes (lead when Kotlin or JVM semantics own the outcome):

| Mode | Use for | Decides |
| --- | --- | --- |
| `Core Kotlin` | Pure functions, collections, extensions, visibility | Ownership, receiver, return, mutation |
| `Nullability` | Nullable, Java, generated, reflection or deserialized values | Convert uncertainty once |
| `Type Boundary` | Identifiers, units, parsers, DTOs, states, results, public APIs | Prevent accidental states |
| `Coroutine` | Suspend, Flow, children, timeout, retry, blocking | Lifetime, cancellation, failure, dispatcher, cleanup |
| `Interop` | Java callers, Java libraries, platform types, checked exceptions, overloads, SAM adapters | Nullability, names, overloads, exceptions, generics, binary contract |
| `Testing` | An unclear or high-risk boundary | The lightest faithful failure |
| `Review` | An existing change | Compile-safe but unsafe, ambiguous or incompatible boundaries |

Default combinations:

- New endpoint or feature: `Spec Mode` plus the framework mode, plus `Persistence Mode` if storage changes.
- Auth or account flow: `Spec Mode` plus the framework mode plus `Security Mode`.
- External API or workflow: `Spec Mode` plus `Coroutine Mode` plus `Resilience Mode`.
- Migration or deployment change: `Persistence Mode` plus `Operations Mode`.
- Review or hardening pass: `Review Mode` plus the most relevant risk mode.
- Mixed Java and Kotlin lookup: `Nullability` leads, `Interop` owns the Java shape, `Coroutine` owns lifetime and blocking, `Testing` owns evidence. The backend modes join only for remote auth, retry, rate limit, health, shutdown or deployment recovery.

Order of attention by task. Each row lists sections of this file in the order to apply them:

| Task | Order |
| --- | --- |
| New Spring Boot endpoint | Service anatomy; Spring Boot rules; Testing and fixtures; Security or Runtime operations only if the feature touches them |
| New Ktor service or route | Service anatomy; Ktor rules; Testing and fixtures; Security or Runtime operations as needed |
| Persistence or migration work | Persistence and transaction rules in Service anatomy; Testing and fixtures; migration and rollout rules in Runtime operations; transaction and idempotency rules in Resilience |
| External API, queue or worker flow | Coroutine and external-client rules; Security and Resilience; Runtime operations; contract and integration tests in Testing and fixtures |
| Production readiness review | Security and Resilience; Runtime operations; Testing and fixtures; Service anatomy |

## Workflow

1. **Preflight the target.** Read the repository instructions. Inspect the working tree and preserve existing changes. Find the wrapper, modules, version catalogs, compiler options and plugins, source sets, generated code, tests, static-analysis configuration, CI and public consumers. Confirm what you are authorized to do: research, destructive actions, commits, pushes, production access. Keep credentials and private data out of every record.

   ```bash
   rg --files -g 'build.gradle*' -g 'settings.gradle*' -g 'gradle.properties' -g 'gradlew' -g 'pom.xml' -g 'mvnw'
   rg 'kotlin|jvmToolchain|languageVersion|apiVersion|ktlint|detekt|kotest|junit|mockk|turbine|kotlinx-coroutines-test' .
   ```

   Limit large searches to configuration roots. Generated output and caches are not source configuration.

2. **Classify the backend surface.** Name it first: Spring MVC API, Spring WebFlux service, Ktor service, worker, scheduled job, message consumer, migration, external client or review pass. State whether the main risk is ambiguity, Kotlin or JVM framework compatibility, persistence correctness, coroutine safety, security, resilience or operations. When the work is language-led, name the Kotlin surface instead: library API, domain module, CLI, Gradle script, coroutine workflow, Java interop adapter, serialization boundary or review pass. Then state whether the main risk is nullability, API misuse, platform types, cancellation, blocking IO, mutation or test gaps.

3. **Write executable requirements.** Use `REQ-KOTLIN-BACKEND-<NNN>.<REV>` identifiers, or `REQ-KOTLIN-<NNN>.<REV>` when the work is language-led. Express behavior as `WHEN ... THEN ... SHALL`. Reject vague claims such as "production-ready", "idiomatic", "secure" or "fast" without observable criteria. Cover the normal, absent, malformed, boundary, failed, cancelled, duplicate and compatible states that can occur.

4. **Select the framework stance before coding.** Preserve Spring Boot versus Ktor unless a migration is requested. Preserve Gradle or Maven, Java target, Kotlin version, framework version, database stack and runtime style. Decide whether the feature belongs in the controller or route, application service, domain model, persistence adapter, external client or background worker.

5. **Design Kotlin and service boundaries.** Keep transport DTOs, domain types, persistence models and API responses distinct when they carry different invariants. Prefer Kotlin nullability, value classes, sealed result and error types and immutable data for business boundaries. Do not leak platform types, nullable surprises, framework annotations or ORM lifecycle concerns into the domain core. Locate each uncertain ingress and normalize it once in an adapter.

6. **Apply framework-specific constraints.** In Spring Boot prefer constructor injection, a slim application bootstrap, typed `@ConfigurationProperties`, focused test slices, explicit transactions, and the Kotlin Spring and JPA compiler plugins when framework proxying or JPA construction requires them. In Ktor keep plugins explicit, install serialization, auth and status pages deliberately, test with the Ktor test host and do not hide route behavior behind global mutable state.

7. **Treat coroutines as correctness-sensitive.** Preserve structured concurrency. Do not use `GlobalScope` for request work. Propagate cancellation and deadlines across service and client calls. Isolate blocking JDBC, JPA or file calls onto an appropriate dispatcher, or keep the service intentionally blocking instead of pretending it is non-blocking.

8. **Choose the verification mix deliberately.** Pick from unit tests, Spring slices, `@SpringBootTest`, Ktor `testApplication`, Testcontainers, migration tests, HTTP mock tests, contract tests, property tests and production smoke checks. Prefer the lightest test that proves the behavior, but use real infrastructure when persistence, messaging or external service behavior is part of the requirement. Write the verification matrix before production changes. Observe the intended failing test first.

9. **Implement the smallest coherent change.** Keep formatting separate from semantic change. Do not perform repository-wide lexical replacement, install unrequested tools, replace frameworks, invent domain states or guess dispatcher limits.

10. **Run quality gates before handoff.** Use the repository wrapper. Iterate with a focused test, finish with the full supported gate. Require evidence for requirement coverage, migration safety, security behavior and non-functional claims. Record the command, working directory, exit status, selected tests, exclusions and every gate that could not run.

11. **Hand off.** Return the output contract below. State what is verified, what is conditional, what is blocked and what stronger claim the evidence does not support. Stopping on a precise missing fact is a successful outcome.

## Service anatomy

Treat a Kotlin backend request path as six boundaries:

1. **Transport boundary:** controller, Ktor route, request parser, authentication principal, response mapping.
2. **Application boundary:** use-case service, transaction choreography, idempotency decision, external-call sequencing.
3. **Domain boundary:** value objects, invariants, state transitions, domain errors.
4. **Persistence boundary:** repository or DAO, SQL and query design, transaction scope, migration compatibility.
5. **Integration boundary:** HTTP clients, message brokers, queues, third-party APIs, retry and timeout policy.
6. **Runtime boundary:** config, secrets, logging, metrics, health, deployment and rollback behavior.

Keep these boundaries visible unless the code base is intentionally tiny. Kotlin reduces boilerplate; it does not remove the need to name risky boundaries.

For any one request, trace decode, authorization, service, persistence or remote I/O, response mapping, and cancellation or error handling using the actual framework configuration.

### Executable requirement template

```markdown
### REQ-KOTLIN-BACKEND-001.0: Create Account Endpoint

WHEN a valid create-account request is submitted
THEN the service SHALL create one account record
AND SHALL return HTTP 201 with the public account id
AND SHALL reject duplicate email addresses with HTTP 409
AND SHALL not leak whether an inactive account exists.
```

Every non-functional claim needs evidence: a p95 latency threshold, retry count, timeout budget, migration safety check or security assertion. The threshold itself comes from the service owner, not from this skill.

### DTO, domain and persistence separation

Use separate shapes when invariants differ:

- **Request DTO:** external input, validation annotations, serialization concerns.
- **Domain command:** trusted application input after parsing and authentication.
- **Domain entity or value:** business invariants and transitions.
- **Persistence model or entity:** ORM or SQL mapping concerns.
- **Response DTO:** stable public contract.

Small apps can map manually. Larger apps can use explicit mappers. Avoid an implicit "one class for everything" unless the domain is intentionally CRUD-only and the tradeoff is named.

### Error modeling

Prefer explicit expected failures:

- **Domain errors:** duplicate account, invalid state transition, insufficient balance.
- **Transport errors:** malformed JSON, missing auth, invalid route parameter.
- **Infrastructure errors:** database unavailable, external timeout, broker failure.

Map expected domain errors to stable response codes at the transport boundary. Do not let exceptions be the only documented business API. Do not expose exception class names as a contract.

### Persistence defaults

Choose the persistence style deliberately:

- **Spring Data JPA or Hibernate:** good for conventional CRUD and aggregate persistence, but check Kotlin all-open, no-arg and JPA plugin needs, lazy-loading behavior, `equals` and `hashCode`, and transaction boundaries.
- **Spring Data JDBC:** good for simpler aggregate persistence with less ORM magic.
- **Exposed DSL:** good for Kotlin-first SQL with explicit transaction blocks.
- **jOOQ:** good for SQL-first teams that want generated, type-safe query building and direct database control.
- **R2DBC and reactive stores:** useful only when the whole stack is reactive and non-blocking and the operational complexity is justified.

Migration safety matters more than ORM preference. Schema changes require migration files, compatibility checks, and rollback or roll-forward thought.

### Transaction boundaries

Keep transactions around application service workflows, not controllers or routes. Name the transaction scope before coding:

- Single write transaction.
- Read-modify-write transaction.
- Outbox transaction.
- Saga or workflow with durable steps.
- No transaction because the operation is read-only or external-only.

Do not wrap slow external calls inside a database transaction unless the tradeoff is explicit. Do not back off or retry inside a transaction.

### External clients and workers

For outbound HTTP, queue or worker flows:

- Define a port or interface at the application boundary.
- Normalize provider-specific errors in the adapter.
- Set connect, read and total timeouts.
- Classify retryable versus permanent failures.
- Use idempotency keys or deduplication for retryable writes.
- Consider an outbox or durable queue for work that must survive process restarts.

### API contract defaults

- Validate request body, route params, query params, headers and auth principal at the edge.
- Treat client-side validation as user experience, not trust.
- Return stable error envelopes when the service already has one.
- Use cursor or range pagination for growing collections.
- Use deterministic ordering for paginated reads.
- Keep public response fields intentional; do not serialize persistence entities directly by default.

## Kotlin reliability rules

Apply these fifteen patterns as a review baseline for agent-authored Kotlin, boundary first and core second. Kotlin's ergonomics are powerful, but they can hide Java platform types, receiver confusion, coroutine leaks and mutable domain models when used casually. The scores are the author's emphasis. They are not measured defect rates, probabilities or an implementation order. Read the scoreboard first, apply only the rules for the boundary being touched, and finish with the anti-pattern tables and the closing self-check.

| ID | Score | Pattern |
| --- | ---: | --- |
| `KC1-01` | 98 | Contain platform types at Java boundaries |
| `KC1-02` | 96 | Prefer non-null domain types and explicit absence |
| `KC1-03` | 94 | Use value classes for meaningful primitive identifiers |
| `KC1-04` | 93 | Use sealed outcomes for closed result and state spaces |
| `KC1-05` | 91 | Keep data classes for value data, not lifecycle-heavy entities |
| `KC1-06` | 90 | Prefer immutable collections and constructor-injected state |
| `KC1-07` | 90 | Parse raw inputs once before domain logic |
| `KC1-08` | 89 | Use scope functions only when receiver and return semantics stay obvious |
| `KC1-09` | 95 | Preserve structured concurrency and cancellation propagation |
| `KC1-10` | 94 | Do not swallow `CancellationException` |
| `KC1-11` | 91 | Isolate blocking calls from coroutine dispatchers |
| `KC1-12` | 88 | Make Java interop contracts explicit with annotations and overload choices |
| `KC1-13` | 87 | Use focused extension functions at stable ownership boundaries |
| `KC1-14` | 86 | Keep public API growth binary- and source-compatible where possible |
| `KC1-15` | 85 | Test cancellation, nullability, and serialization boundaries directly |

Review the rows that apply and stop when the remaining rows cannot apply. Scope out the interop rows only when there are no Java callers, and record that decision. `KC1-13` and `KC1-14` are easy to skip but bind strongly for published libraries. A hard categorical failure (a platform-type crash, swallowed cancellation, an unauthorized data state, an incompatible public signature) blocks every claim that depends on it; no aggregate score offsets it.

### API and type design

**`KC1-03` Value classes for meaningful primitive identifiers.**

```kotlin
@JvmInline
value class UserId(val value: String)
```

Prefer this for IDs, keys, units, offsets and validated strings. It prevents passing a raw `String` or the wrong ID type through a large call chain. Keep value classes small and invariant-bearing. If the constructor cannot enforce the invariant directly, expose a factory such as `parse` or `from`. Use a value class only when framework serialization and persistence support are understood; the advice stays provisional until serializer and persistence mapping tests pass. Keep raw `String`, `Long` and `UUID` values from drifting across layers when they represent domain identifiers. A raw local identifier with no confusion risk may not need a wrapper.

Worked identifier example. Two raw strings represent `UserId` and `InvoiceId` across many domain calls, and both have a validated non-blank format. Inspection finds Kotlin callers, one serializer and no supported Java or framework-generated consumer. The public constructor above cannot enforce the format, so close it and parse once at the adapter:

```kotlin
@JvmInline
value class UserId private constructor(val value: String) {
    companion object {
        fun parse(raw: String): UserId? =
            raw.trim().takeIf(String::isNotEmpty)?.let(::UserId)
    }
}
```

- **Evidence:** parser tests for empty, whitespace, valid and round-trip values; compile checks that `UserId` and `InvoiceId` cannot be interchanged; tests against the target serializer and the generated surface, with the serializer configuration and Kotlin version preserved; Java and API or ABI gates only if such consumers exist.
- **Bad route:** wrap every `String` because wrappers score high, leave public construction unrestricted, and skip the serializer and consumer checks. More types exist, but the invariant and the migration stay unclear.
- **Borderline route:** Java callers or framework binding are discovered after the design. Keep the type internal, or preserve the raw public signature, while investigating generated representation, annotations, boxing, reflection and compatibility. Do not call the public wrapper safe yet.

**`KC1-04` Sealed outcomes for closed result and state spaces.**

```kotlin
sealed interface PaymentDecision {
    data class Approved(val authorizationId: String) : PaymentDecision
    data class Declined(val reason: DeclineReason) : PaymentDecision
    data object RequiresReview : PaymentDecision
}
```

Prefer sealed outcomes over booleans, sentinel strings or exception-only business flow. This gives exhaustiveness checks in `when` expressions and makes new states visible during refactors. Use sealed types only for states the owner controls and closes. For an open external protocol, preserve the raw wire value and an internal `Unknown(code)`; a public sealed type of "today's three states" that throws on a future code converts evolution into an outage.

**`KC1-05` Data classes for value data.** Use data classes for immutable values, DTOs, read models, events and pure state snapshots. Do not make them the default for objects with identity, lifecycle hooks, lazy loading or mutable behavior. Good defaults:

- Constructor parameters express required state.
- Properties are `val` unless mutation is part of the invariant.
- Copy semantics are safe for the domain.
- Equality is value equality, not identity or persistence identity.

**`KC1-06` Immutable collections and constructor-injected state.** Expose snapshots or owned mutation, never a mutable alias. Inject state through constructors or an explicit lifecycle instead of a mutable global.

**`KC1-07` Parse raw inputs once before domain logic.** At boundaries, turn strings, maps, JSON, CLI args, environment values or Java objects into typed Kotlin values before business logic runs. Keep parse errors close to the boundary and domain logic close to non-null validated types.

**`KC1-08` Scope functions.** Use `let`, `also`, `apply` and `run` only when the receiver and the return value stay obvious. Replace opaque nested chains with named locals or small functions. Fewer lines prove no benefit.

**`KC1-13` Extension functions.** Keep them focused and place them at a stable ownership boundary.

**`KC1-14` Public API growth.** Keep it binary- and source-compatible where possible. Private is not isolated if reflection, generated code, serialization, a framework or tests reach it.

Type selection in one place:

| Need | Choose |
| --- | --- |
| Stable meaningful invariant, supported consumers | Value class |
| Exactly one meaningful absence, and every caller acts the same way | `T?` |
| Small fixed set of labels with no payload | Enum |
| Owner-controlled closed states with distinct payloads or actions | Sealed interface or class |
| Immutable value data | Data class |
| Identity or lifecycle | Plain or framework class with explicit identity |
| Expected closed outcomes | Typed result |
| Exception-oriented framework or Java contract | Typed exception with an explicit taxonomy |
| One understood failure channel | `Result<T>` (a generic `Result<Any>` or broad `runCatching` erases cancellation and defects) |
| Obvious exhaustive binary predicate with no differing diagnostics or recovery | `Boolean` |

Do not wrap every primitive, replace every exception with a sealed result, mark every function `suspend` or use scope functions for appearance. Add structure only to prevent a real invalid state, reduce repeated checks, clarify an obligation or make ownership testable. Do not distinguish states that no caller, test, operation or policy treats differently.

### Nullability and Java interop

**`KC1-01` Contain platform types at Java boundaries.** Java interop can expose platform types whose nullability Kotlin cannot prove. Do not let them flow into the domain core.

- Convert Java return values into nullable or non-null Kotlin types immediately.
- Prefer Java APIs with nullability annotations when available.
- Wrap uncertain values with explicit checks and typed failure messages.
- Do not assign platform types directly to non-null domain fields without validation.

An unannotated `String findDisplayName(String userId)` is a platform type. When a non-null annotation conflicts with an observed null, investigate the dependency version, the generated signature and the fixture; do not silently trust the annotation.

**`KC1-02` Prefer non-null domain types and explicit absence.** Use `T?` only when absence is a real domain state. If absence means "not loaded", "forbidden", "invalid", "not found" or "not yet computed", model the distinction with a sealed type or result. Avoid:

- `String?` for every field because the source is nullable.
- `!!` as a migration shortcut.
- `lateinit` for required dependencies outside lifecycle-managed frameworks.

**`KC1-12` Make Java interop contracts explicit.** When Kotlin APIs are called from Java, check names, nullability, overloads, default parameters, exceptions, generics and binary compatibility. Consider `@JvmName`, `@JvmOverloads` or explicit facade functions when they make Java call sites safer. Do not optimize only for Kotlin call sites if Java is a supported consumer. A public artifact with no local Java caller remains externally conditional.

### Coroutines and Flow

Kotlin coroutines make asynchronous code readable. They do not make blocking dependencies non-blocking.

**`KC1-09` Preserve structured concurrency and cancellation propagation.** Keep work tied to a caller-owned scope. Prefer `coroutineScope`; use `supervisorScope` only when independent child failure is intentional and the results are still accounted for; use explicit lifecycle scopes supplied by the application. Avoid `GlobalScope` for request, command, job or user-visible work. It disconnects work from the caller's cancellation and error handling. Each asynchronous task needs a lifetime owner, a cancellation path, a failure destination and cleanup. Use `withTimeout` or deadline propagation for bounded external calls, and derive inner budgets from the outer deadline.

**`KC1-10` Do not swallow `CancellationException`.** Cancellation is cooperative. Broad catches must rethrow it:

```kotlin
try {
    runWork()
} catch (error: CancellationException) {
    throw error
} catch (error: Exception) {
    recordFailure(error)
}
```

Any retry, logging or error-normalization layer around suspend work must preserve cancellation. A sealed-result mapper needs an explicit cancellation branch. Treat a catch-all that logs and continues as a cancellation leak until the rethrow-first shape is shown. Cancellation preservation comes before retry tuning.

**`KC1-11` Isolate blocking calls from coroutine dispatchers.** Name blocking calls honestly. File IO, JDBC, JPA, legacy SDK calls and CPU-heavy operations use an appropriate dispatcher or stay in an intentionally blocking API. Do not label a function `suspend` if it only hides blocking work without isolation or a stated operational tradeoff. Choose one of four routes:

| Situation | Route |
| --- | --- |
| The dependency genuinely cooperates | Call it directly in a structured scope; do not add a dispatcher switch |
| The adapter owns a confirmed blocking dependency | Run it on an owned, bounded dispatcher matched to the backing pool |
| The caller owns execution policy | Expose a named blocking API such as `readInvoiceBlocking` |
| The work must survive the request or process | Use a durable, idempotent job |

A dispatcher switch does not create capacity and does not prove interruption. `withContext(blockingContext)` preserves coroutine cancellation at its boundary but cannot interrupt a noncooperative Java call; document whether cancellation interrupts the operation or only stops waiting. A thread switch can reduce event-loop blocking while creating an unbounded IO queue. An intentionally bounded blocking architecture can be safer than fake non-blocking layers. Do not scatter dispatcher switches across services; adapt at one explicit adapter.

**Flow and callback bridges.** Before writing or reviewing a Flow or a callback bridge, state:

- Whether the producer is cold (it runs once per collector) or shared (one producer, many collectors), and which scope owns the producer.
- When the callback is registered and when it is unregistered. Completion, failure and cancellation of the collector must all release it.
- The collector, the buffer, the terminal event and the cleanup owner.
- An explicit overflow policy: drop, conflate, buffer, suspend or fail. Conflate only obsolete intermediate state. Distinguish state from events; conflation may fit state and corrupts event semantics.

Prove it with collect, cancel, fail and restart scenarios that show producers and resources are released. An application-wide stream may be long-lived when an explicit lifecycle manages it.

**Child creation and waiting.** Bound the number of child coroutines before launching them. A bounded downstream client does not make an unlimited launch harmless, and a detached scope is not an overflow strategy. Distinguish waiting from active work and observe them separately: cancellation while waiting must remove ownership cleanly, while a noncooperative blocking call can continue after cancellation, so make its residual work and effects visible. Cleanup must not restart cancelled business work.

### Constructs are signals, not bans

| Construct | Acceptable only when |
| --- | --- |
| `!!` | An adjacent proven invariant exists, plus an impossible-state test or a framework contract; or it is a test fixture |
| Broad `lateinit` | Initialization is lifecycle-owned (framework injection), race-free and safe at teardown, and the lifecycle clause is recorded |
| Java platform type past the adapter | It stays in one reviewed shim because earlier conversion is impossible |
| `GlobalScope` | The work is genuinely process-lifetime and has explicit supervision, shutdown, durable state, failure reporting and an owner |
| Broad catch around suspend work | It rethrows cancellation first, then translates known failures deliberately |
| Data class for an entity | Identity, proxy, lazy-loading, copy and equality tests pass |

Every exception records the exact construct and path, the excluded danger, the invariant, the owner and scope, the evidence, the consequence of failure and a review or removal trigger. "The framework needs it" and "tests pass" are not sufficient.

Classify each construct by the contract it can erase, not by its spelling: `!!` erases where a null came from, `lateinit` erases initialization order, `GlobalScope` erases lifetime ownership, a broad `catch (Exception)` erases cancellation, a data class erases identity, and `Dispatchers.IO` erases who owns blocking capacity. Then give every observed candidate exactly one disposition:

| Disposition | Meaning | What it requires |
| --- | --- | --- |
| `confirmed_defect` | The contract loss and its consequence in the target are observed | A repair plus regression evidence |
| `conditional_hazard` | The dangerous interpretation is plausible | A named invariant or behavior test that is still outstanding |
| `bounded_exception` | Invariant, owner, scope and verification make the construct acceptable on this path | The exception record above |
| `accepted_risk` | An accountable owner accepts a stated consequence | The owner, the consequence and a review trigger. Accepted is not the same as safe |
| `not_applicable` | Generated, framework-owned or non-production context, or the mechanism is absent | The reason, recorded |
| `blocked` | Domain, framework, dependency, security or operational authority is missing | Route to the owner. Do not manufacture a replacement |

A conditional case becomes a bounded exception only when it records the exact path, the invariant, the owner, the failure consequence, the test or framework evidence and the review trigger. Without that it stays a finding; it is not a stylistic disagreement.

## Spring Boot rules

Prefer Spring Boot defaults unless the requirement proves a customization is necessary.

**Package and bean structure**

- Keep the `@SpringBootApplication` class slim and in a root package above application components.
- Use constructor injection. Kotlin primary constructors make this natural. Do not flag an established factory merely because it is not constructor injection.
- Prefer small configuration classes over broad component scans.
- Keep controllers thin: parse, authorize, call the application service, map the result.
- Keep application services responsible for transaction workflows and orchestration.
- Keep repositories focused on persistence, not business decisions.

**Kotlin compiler plugins.** Kotlin classes are final by default. Spring AOP and proxying, and JPA, can require openness or no-arg constructors.

- Use the Kotlin Spring (all-open) plugin when Spring proxying needs open classes.
- Use Kotlin JPA (no-arg) support when JPA entities need synthetic no-arg constructors.
- Do not add `open` everywhere by hand unless the repository has deliberately avoided compiler plugins.
- Keep plugin versions aligned with the Kotlin version managed by the build.
- Never assume a final Kotlin class is proxyable without compiler support. Watch for self-invocation that bypasses the proxy.

**Configuration**

- Prefer typed `@ConfigurationProperties` for structured settings.
- Validate required settings at startup.
- Avoid scattered `@Value` for multi-field configuration.
- Keep secrets out of source and test fixtures.
- Keep environment-specific differences in configuration layers, not in branching application code.

**MVC, WebFlux and coroutines**

- Use Spring MVC for conventional blocking servlet services.
- Use WebFlux or coroutines only when the repository and its dependencies are actually non-blocking, or the team accepts the complexity.
- Do not call blocking JPA or JDBC from a reactive event-loop path without explicit isolation.
- Use suspend controller and service functions only when the surrounding stack supports the execution model.

**Validation and error handling**

- Use Bean Validation for transport-level shape and simple constraints.
- Put business invariants in domain and application code, not only in annotations on transport DTOs.
- Centralize exception and response mapping with controller advice or the repository's existing error mapper.
- Keep public error contracts stable and do not leak implementation exception names.

**Persistence with Spring**

- Put `@Transactional` on service workflows or clearly scoped repository operations.
- Avoid long transactions that include external API calls.
- For JPA entities, check data-class equality, generated IDs, lazy relations, proxying and no-arg needs before using idiomatic Kotlin shortcuts.
- Prefer migrations for schema changes; do not rely on auto-DDL in production.

**Operations defaults when Spring is the target stack**

- Actuator for health and operational endpoints, with exposure and access configured intentionally.
- Micrometer for metrics and observation integration.
- Spring Security defaults reviewed before customizing.
- Profile-specific configuration only for real environment differences.

## Ktor rules

Use Ktor when explicit plugin composition and coroutine-first request handling are part of the project shape.

**Application structure**

- Keep `Application.module` or the equivalent bootstrap small.
- Install plugins deliberately: content negotiation, authentication, status pages, call logging, compression, CORS, rate limiting, resources and type-safe routing.
- Group routes by business capability, not by HTTP verb alone.
- Keep route handlers thin and delegate to application services. Do not put repository or authorization logic in a route.
- Avoid global mutable singletons for services, clients and repositories unless the repository has an intentional DI or container pattern.

**Serialization**

- Use Ktor content negotiation consistently.
- Prefer kotlinx.serialization for Kotlin-first DTOs when it matches the project. Use Jackson when Spring or Jackson compatibility or existing Java ecosystem integration is the project norm.
- Configure unknown keys, defaults, naming and date-time serialization intentionally. Do not choose a serializer without contract tests.

**Status pages and errors**

- Install status pages or the repository's equivalent central error mapper.
- Map expected domain failures to stable responses. Incomplete status-page mappings are a common failure signal.
- Log infrastructure failures with correlation context, but never log secrets or raw credentials.

**Type-safe routing**

- Consider Ktor Resources (type-safe routing) for APIs where route parameters and nesting are easy to misuse.
- Do not introduce route DSL complexity if the service has only a few simple endpoints.

**Ktor testing**

- Use `testApplication` for route and plugin behavior without binding sockets. Do not mock away the installed plugins.
- Use fake repositories for pure route contract tests. A fake repository proves a route contract only; a real persistence gate is required before release.
- Use Testcontainers when the route behavior depends on real persistence, broker or external service behavior.

**Operations defaults when Ktor is the target stack**

- Explicit plugins for call logging, metrics, tracing, status pages, authentication and serialization.
- Typed configuration loading at application startup.
- Health routes that separate liveness from readiness when the deployment platform uses both.

## Cross-framework idioms

- **Naming.** Follow official Kotlin style for packages, classes, functions and properties. Do not force a four-word naming convention onto idiomatic Kotlin public APIs when it makes the code un-Kotlin-like. Use descriptive names and stable domain vocabulary.
- **Null safety.** Treat platform types from Java libraries as unsafe until checked. Avoid `!!` in production code except at narrow, documented interop boundaries. Convert nullable transport data to non-null domain data explicitly.
- **Data classes.** Use them for DTOs, commands and immutable value carriers. Be cautious for entities with identity, lazy loading, mutation or framework lifecycle hooks.
- **Value classes.** Use them for identifiers and constrained wrappers when serialization and persistence support them. Add tests for JSON mapping, database mapping and reflection-heavy frameworks before relying on them broadly.
- **Sealed outcomes.** Use sealed result types for closed business outcomes when they improve exhaustiveness and response mapping. Do not create a custom result hierarchy for every trivial branch.

## Testing and fixtures

Test the risk, not the syntax. Start from the boundary that can break and pick the lightest test that exercises it. Realism follows semantic risk, not layer prestige.

| Boundary that can break | Test |
| --- | --- |
| Pure domain invariant | Unit test |
| Controller or route mapping | Spring slice or Ktor test host |
| Persistence query or mapping | Repository test or real database test |
| Cross-layer request behavior | Application integration test |
| External API behavior | HTTP mock or contract test |
| Migration behavior | Migration test against a real database |
| Retry or idempotency behavior | Integration or focused workflow test with failure injection |

Do not default to full application startup for every test. Do use full startup when the requirement depends on real wiring.

**Spring Boot tests.** Prefer focused slices first:

- `@WebMvcTest` for MVC controller request and response behavior. A slice proves security and serialization only when the filters are included; transaction semantics stay outside it.
- `@JsonTest` for serialization contracts.
- `@DataJpaTest` for JPA repository and mapping behavior.
- `@SpringBootTest` when cross-layer wiring, security filters, configuration or infrastructure integration must be proven.

Use Testcontainers when a real database, broker or dependent service changes the behavior under test. H2-only tests are not proof of PostgreSQL- or MySQL-specific SQL or locking behavior. H2 may still serve repository-independent service tests.

**Ktor tests.** Use `testApplication` for route and plugin behavior. It exercises application calls internally without binding a real socket, which is usually faster and less flaky than booting a network server. A real socket test is for network integration, not for ordinary plugin mapping. Ktor route tests cover:

- Installed content negotiation and request parsing.
- The authentication and authorization path. With the auth plugin installed, this proves deny-by-default routing and plugin wiring: unauthenticated and denied requests are rejected by the route tree. It does not prove integration with the production identity provider (real token issuance and verification), which needs separate contract evidence.
- Status page and error mapping.
- Serialization response shape.
- Route parameter and query validation.

Use real infrastructure only when repository, transaction, broker or external service behavior is part of the requirement.

**Test frameworks.** Use the repository's existing test framework. Never switch between JUnit and Kotest silently. Common choices:

- JUnit 5: default for Spring Boot and many JVM services.
- Kotest: expressive Kotlin test styles, assertions and property testing.
- MockK: Kotlin-native mocking, including coroutine-aware mocking.
- SpringMockK or equivalent helpers only if already adopted or necessary.

Prefer fakes over mocks for domain services when the dependency behavior is simple. Prefer mocks for hard-to-construct collaborators, provider adapters and behavior verification at narrow boundaries. Never mock the boundary under test.

**Coroutine tests**

- Use coroutine test utilities when controlling dispatchers, delays or virtual time.
- Verify cancellation propagation for long-running work.
- Verify timeout behavior for external clients, using virtual time and a fake client that records cancellation. A happy-path route test does not cover it.
- Avoid tests that pass only because real sleeps happen to be long enough.
- A fake clock fits timeout policy. It cannot prove HTTP-client cancellation integration.

**Persistence tests** prove that:

- Migrations apply from an empty database. This alone does not prove safety on populated data; see the migration rules.
- Critical queries match production dialect behavior.
- Transaction boundaries commit and roll back as expected.
- Optimistic locking or concurrency behavior works when used.
- Repository methods do not trigger N+1 query patterns on hot paths.

For Exposed, database operations run inside transactions. For jOOQ, prefer generated schema-backed queries when the project uses code generation. A duplicate-insert race belongs against the production dialect: a real database test proves one commit plus one stable conflict, while a mock that throws a duplicate exception does not prove atomicity.

**Contract and API tests** for public APIs:

- Test HTTP status, headers, response envelope and error body.
- Test invalid JSON, invalid route parameter, invalid query parameter and missing auth.
- Test duplicate and idempotent submissions where retry is possible.
- Test pagination stability and deterministic ordering.
- Test serialization of Kotlin value classes and date-time types when exposed.

**Kotlin risk tests** for every touched boundary:

- Nullability and platform-type boundaries using Java fakes or adapter tests.
- Sealed outcome exhaustiveness through behavior tests.
- Value-class parse and round-trip tests.
- Coroutine cancellation tests and timeout behavior.
- Serialization compatibility tests when external contracts exist.
- Property tests for parsers, validators, canonicalizers, pagination cursors, idempotency keys, reversible transforms and state transitions with a large input space, when the repository has a property-test stack. Property tests do not replace concrete examples that document the API contract.

**Fixture rules**

- Keep fixtures explicit and small. Use builders only when they remove irrelevant noise without hiding required fields.
- Each fixture row makes one claim, creates only the state it needs, owns its cleanup, is deterministic under repeat and parallel execution, and exposes its target failure.
- Use inline values for tiny pure units, reusable builders for stable objects, scenario fixtures for workflows, per-test containers for strong isolation, and suite-level infrastructure with unique namespaces when startup dominates. Container reuse requires an isolated namespace and leakage checks.
- Reject silent invalid defaults, wall clocks, global dispatchers, transaction cleanup that cannot be undone, personal data, over-complex fixture APIs, random data without a seed, order-dependent cleanup and retries used as flake handling.
- Builders, random-data privacy, cleanup, parallel execution, snapshots, CI sharding and fixture factories are repository decisions. Read them from the build files, neighboring tests and harness configuration. Do not invent a fixture library.
- Use characterization tests for legacy behavior before changing it. Do not replace fixtures without an inventory.
- Keep one fixture plan per owned service capability. Split it by independently deployable system, data store, external contract, security boundary or verification environment when ownership, lifecycle or failure semantics diverge. Each split keeps an owner, a requirement subset, a fixture namespace, a gate, a dependency contract and an evidence handoff. A named integration owner keeps one higher-level cross-split contract test that proves the interactions no single split can. Run contract compatibility in both directions, and trace one requirement across every split gate.
- Good: separate producer and consumer fixture plans with a versioned contract test and one integration owner. Bad: two agents rewriting one global fixture file at the same time. Borderline: a shared Testcontainers utility is fine when lifecycle and schema isolation stay owned by each service suite.

**When a test fails,** classify first: product defect, assertion defect, fixture leak, scheduling nondeterminism, unavailable dependency, stale evidence or contradiction. Rerun only for a named hypothesis with a bounded count, one controlled variable and the retained seed or trace. Preserve the first-run evidence. A transient container pull may justify one infrastructure retry; automatic retries cannot turn a failed assertion green. Alternating results are flakiness, not permission to report the passing attempt. Quarantine only with an owner and an expiry.

### Verification matrix template

| req_id | test_id | test_type | assertion | target |
| --- | --- | --- | --- | --- |
| REQ-KOTLIN-BACKEND-001.0 | createAccountReturns201 | Spring `@WebMvcTest` or Ktor `testApplication` | valid request returns 201 and public id | transport boundary |
| REQ-KOTLIN-BACKEND-001.0 | duplicateEmailReturns409 | integration/database test | duplicate normalized email is rejected atomically | service plus persistence |
| REQ-KOTLIN-BACKEND-002.0 | migrationAppliesCleanly | Testcontainers migration test | schema migrates from empty database | migration path |

## Security

Use this section when work touches validation, authentication, authorization, sessions, tokens or sensitive flows.

Start from the **protected transition**: an untrusted trigger, then an authenticated identity or system actor, then authorization and domain preconditions, then a bounded effect and commit, then a visible response or durable acknowledgement, then defined retry, cancellation, duplicate and restart behavior. Define the actor, asset, side effect, commit point, acknowledgement, failure classes and replay identity before implementation.

Defaults: deny by default; validate at both the transport and the domain boundary; prefer framework-native security while keeping product authorization explicit.

**Trust boundaries.** Treat all inbound data as untrusted:

- JSON body.
- Route parameters.
- Query parameters.
- Headers.
- Cookies.
- JWT and session claims.
- Message payloads.
- Environment variables.
- Data loaded from external APIs.

Validate transport shape at the edge. Re-check business invariants in application and domain code. Validation is not authorization, and a parsed or signed claim is not authorization either. Never derive identity, tenant or role from payload text.

**Authentication and authorization**

Spring Boot:

- Prefer Spring Security's Kotlin DSL when the service is Kotlin-first.
- Keep security configuration explicit and tested.
- Use method security only when the team has a clear convention for where authorization lives.
- Test allowed, denied, unauthenticated, expired and malformed-token paths.

Ktor:

- Install authentication plugins deliberately.
- Keep principal extraction and authorization decisions explicit.
- Test route behavior with missing, malformed, valid and insufficient credentials.

Both: authorization is a server-side decision about resource, tenant, role and state. Test cross-owner, cross-role and cross-resource denials at the authoritative layer. A platform filter can supply the authentication convention; downstream resource authorization still has to be explicit. Use one authoritative convention instead of ownership split across gateway, controller and database. Do not ship auth changes without negative-path tests.

**Passwords, tokens and sessions**

- Use memory-hard password hashing such as Argon2id or bcrypt, with current parameters approved by the platform or security team.
- Never log passwords, tokens, session ids, reset tokens or raw `Authorization` headers.
- Store reset tokens hashed when feasible.
- Rate-limit login, reset and verification endpoints. Reuse the authoritative distributed rate limit instead of inconsistent per-instance copies.
- Avoid account enumeration in public error messages.
- Set secure cookie flags for cookie sessions: `HttpOnly`, `Secure`, `SameSite`, domain and path scope, and an appropriate lifetime.

**CSRF and browser context.** CSRF depends on the client context:

- Cookie-authenticated browser flows usually need CSRF protection.
- Bearer-token APIs used by non-browser clients usually have different tradeoffs.
- Do not disable CSRF in Spring Security without naming why the client and auth model make that acceptable. An "API" label is not enough. Verify cookies, CORS and origin, the gateway and the deployed framework behavior.

**Input validation**

- Parse JSON into DTOs at the transport boundary.
- Validate simple structural constraints with framework validation.
- Convert DTOs into domain commands after authentication and normalization.
- Validate cross-field and stateful invariants in application and domain code.
- Return stable error responses without leaking stack traces or internal class names.

**Conditional triggers.** Cookie browser flow: CSRF, cookie and origin tests. Password, reset or login: approved hashing and migration, enumeration, rate, token lifecycle and redaction. Sensitive data: classification, access, retention, deletion and audit. Shared security component: consumer inventory, compatibility, migration, rollout and rollback.

## Resilience

Use this section when work touches external calls, retries, idempotency, coroutine cancellation, background work or failure behavior.

Controls are coupled. A timeout can trigger a retry, a retry can duplicate a write, duplicate protection may need the state transaction, background work can lose the request principal, and a fallback can expose data the primary path would deny. Design them together.

**Coroutine resilience**

- Preserve structured concurrency.
- Propagate cancellation from the request or workflow scope.
- Use supervisor scopes only when sibling failure isolation is intended, with explicit ownership of each result.
- Set timeout budgets on external calls. A nested deadline must not exceed its parent.
- Do not swallow `CancellationException`.
- Do not wrap every coroutine in a broad `catch (Throwable)` without rethrowing cancellation.

**Blocking and dispatchers**

- Treat blocking JPA, JDBC and file calls as blocking even inside suspend functions.
- Use an appropriate dispatcher or dedicated executor when blocking calls are unavoidable in coroutine flows. Bound it and match it to the backing pool.
- Do not starve event-loop threads with blocking work.
- Prefer a simple blocking architecture over a fake non-blocking architecture when dependencies are blocking.

**Retries.** Retries are safe only when bounded and classified:

- Retry transient infrastructure failures.
- Do not retry validation failures, auth failures or deterministic domain errors.
- Use backoff and jitter for remote systems.
- Respect timeout and deadline budgets.
- Record retry attempts in logs and metrics.
- Combine retryable writes with idempotency keys, deduplication or transactional outbox patterns.

A retry needs both **semantic eligibility** (the outcome can plausibly change, the failure class is transient, the operation is replay-safe or read-only, and the prior commit state is known well enough) and **load permission** (remaining deadline, no cancellation, attempts left, queue, concurrency and rate capacity, dependency health). When either fails: fail, reject, reconcile, degrade, durably delay, park, shed or escalate.

| Failure | Action |
| --- | --- |
| Validation, identity, authorization, deterministic business rejection | No unchanged retry |
| Caller cancellation or exhausted deadline | Never retry; propagate |
| Optimistic conflict | Re-read and recompute with a bounded rate, revalidation and the deadline |
| Read timeout | Retry only if duplicate or stale reads are safe |
| Write timeout or unknown commit | Never retry blind; reconcile by stable identity or return an explicit unknown |
| Local deadlock or conflict | Retry only for a known rollback-safe data-layer class with no external effect inside the transaction |
| Overload, queue full, concurrency limit | Reject, shed or delay |

Count amplification across caller, gateway, client, driver, broker and worker. Prefer one explicit retry owner per effect boundary. Avoid nested Spring and client retries. Retry and backpressure share one capacity budget. Never catch `CancellationException` as retryable, and never infer idempotency from a read-like name. This skill sets no universal attempt count, timeout, delay, jitter, queue size or concurrency; copy none from another service.

**Idempotency.** Use it for:

- Payment-like writes.
- Webhook receivers.
- Queue consumers.
- External API callbacks.
- User actions that clients may retry.

Store idempotency records transactionally with the state change when possible. Define response replay behavior for duplicate requests. Define key scope and auth binding, uniqueness, concurrency arbitration, retention, conflict, late replay and reconciliation. Do not claim exactly-once from an HTTP method, client-side suppression, the existence of a key or a broker delivery mode. A check-then-insert is a replay race; use atomic uniqueness, a lock or a state machine. When systems cannot share a transaction, use an outbox, saga, compensation or reconciliation and expose the partial or unknown state.

**External API clients.** For each provider client:

- Define a port or interface.
- Configure connect, read and total timeouts.
- Normalize provider errors.
- Preserve correlation ids.
- Hide credentials from logs.
- Test success, timeout, 4xx, 5xx, malformed response and retry behavior.

**Background work.** Use durable background processing when work must survive process restart or outlive the request. Do not launch fire-and-forget coroutines from request handlers for critical work. Acknowledge only after the local commit or durable acceptance, never after a volatile coroutine launch. Say which acknowledgement you mean: completed effect, durable acceptance or volatile scheduling. For workers:

- Make handlers idempotent.
- Bound concurrency.
- Classify retryable failures.
- Use dead-letter or parking behavior.
- Emit metrics for success, failure, retry, lag and processing time.

Name the scope of every control: coroutine or request, process or instance, partition or shard, service, region, or global. A local mutex is not cross-replica idempotency. An instance counter is not tenant-wide rate limiting. One service's success is not an end-to-end terminal outcome.

**Negative and fault cases to cover.** Every adverse case states the expected effect count, response, durable state and evidence.

- Input: missing, malformed, boundary, unknown, coerced, cross-field.
- Identity: missing, malformed, expired, revoked.
- Authority: wrong role, scope, tenant, resource or state; direct-entry bypass.
- Browser: cross-site request, session reset, enumeration, rate.
- Execution: parent cancellation, timeout, child or sibling failure, stale completion, shutdown.
- Capacity: blocking, pool exhaustion, queue rejection.
- Persistence: rollback, conflict, concurrent duplicate, crash, response replay.
- Provider: timeout, error status, malformed body, cancel, retry exhaustion.
- Worker: enqueue, restart, acknowledgement, redelivery, poison, dead-letter.
- Operations: secret leakage, correlation, saturation, lag, rollback.

A timeout followed by a duplicate write is a failure even if the final response succeeds. A request error does not reveal stranded reservations, open transactions, duplicate effects, abandoned claims or leaked secrets; check the aftermath.

## Runtime operations

Use this section when work touches configuration, observability, deployment, CI, migrations or production safety. Do not treat Actuator, metrics, logging, migrations and secrets as afterthoughts for a production service.

Start with the lifecycle outcome, not the tool. Do not add a runtime mechanism merely because the task says "production", "robust", "scalable" or "best practice". Convert the word into observable behavior and an owner decision first. Name the outcome for the normal, failure, degradation, shutdown and recovery states, inspect the target, and change only the boundaries the outcome touches. Preserve the established wrapper, versions, framework, plugins, configuration system, migration tool, telemetry, package, CI and platform when they satisfy the accepted outcome. Preservation limits how many things change at once; it does not make the status quo correct. An unsupported release, recurring incident, exposed secret, false health state, unsafe migration, substituted artifact or unrecoverable shutdown overrides preservation immediately.

**Build and dependency discipline**

- Use the repository's Gradle or Maven wrapper.
- Preserve Kotlin, Java, Spring Boot, Ktor and plugin versions unless the task is an upgrade.
- Keep Kotlin compiler plugin versions aligned with the Kotlin version.
- Prefer Gradle Kotlin DSL in Kotlin-first projects when it is already present.
- Do not add dependency-management systems or build plugins because they are fashionable.

**Static analysis and formatting**

- Official Kotlin coding conventions for style and organization.
- ktlint or an equivalent formatter and linter for consistent formatting.
- detekt for Kotlin-specific static analysis and maintainability rules.

Do not conflate formatter success with architecture quality. Use ktlint for style. Use detekt and review for complexity, long functions, risky exception handling and maintainability. A formatter pass cannot compensate for a migration that lacks mixed-version compatibility.

**Configuration and secrets**

- Prefer typed configuration objects. Configuration is an input contract.
- Validate required settings at startup. Test valid, absent, malformed, conflicting and redacted states.
- Keep secrets in environment or secret stores, not repository files. Secrets are both data and authority; environment variables alone are not a security model.
- Keep test secrets fake and obviously non-production.
- Avoid config lookups deep inside business logic; inject typed config at the boundary. A parse failure must not fall back silently to a default.

For Spring Boot, use `@ConfigurationProperties` for structured configuration. For Ktor, bind config once at startup and pass typed settings into modules and services. Separate sensitive handles from printable configuration and inject only the settings each adapter needs.

**Profiles and environments**

- Keep environment differences declarative.
- Do not branch business behavior on the environment name.
- Document required environment variables and config keys.
- Test production-like config paths when deployment behavior changes.

**Observability.** Minimum for a production service:

- Structured logs with a request or correlation id.
- Error logs that classify domain, transport and infrastructure failures.
- Metrics for request count, latency, failures, external calls, queue lag and worker outcomes.
- Health and readiness checks that reflect critical dependencies.
- Trace propagation for inbound and outbound calls when the platform supports it.

For Spring Boot, Actuator and Micrometer are the default ecosystem path. For Ktor, install and configure equivalent call logging, metrics, health and tracing integrations deliberately.

Every signal answers an operator decision. Begin with the failure or recovery decision and pick the smallest bounded signal set. Keep credentials, private payloads, user-controlled text, arbitrary identifiers, raw SQL, stack traces and unbounded values out of metric labels. Distinguish original operations, attempts, final results, cancellations, duplicates and reconciliations. When telemetry itself is degraded, say the state is unknown and use an independent source; never render missing data as a healthy zero.

**Database migrations.** Treat migrations as deployable code and as deployed behavior, not as syntax:

- Store migration files with the application.
- Use versioned migrations for schema evolution. Do not rewrite applied history.
- Test migrations against the production dialect when possible.
- Separate expand and contract steps for backwards-incompatible changes: expand, deploy tolerant code, backfill, observe, switch, and contract only after old consumers are gone.
- Plan rollback or roll-forward behavior.
- Verify application compatibility during rolling deploys. Old and new application versions must be able to coexist with each schema state.

Flyway and Liquibase are both acceptable if the repository already uses them. Preserve the repository's migration tool. A migration that passes on an empty database says nothing about populated data, and a previous image existing does not make a data change reversible.

**Container and deployment safety**

- Keep the runtime image small and deterministic. A smaller or newer image is not automatically safer when compatibility and provenance are unverified.
- Run as non-root when possible.
- Expose only required ports.
- Configure graceful shutdown for HTTP servers and workers.
- Ensure readiness does not pass before the service can handle real traffic. A live process is not readiness.
- Ensure liveness does not flap during slow startup or migration windows. Do not fail liveness because a dependency is unavailable.
- Build the artifact once and promote that same artifact; do not rebuild per environment.

**Shutdown is correctness.** Stop intake, let accepted work finish or hand it back with its identity preserved, and prove after restart that each item is either completed once or recoverable. A fixed sleep in a shutdown hook, an acknowledgement on receipt and one clean local exit are not evidence. For every work item an operator must be able to tell who owns it, whether its effect occurred, what a retry does, how termination changes its state and how the system recovers.

**CI expectations.** At minimum, backend CI runs:

- Format, lint and static analysis if configured.
- Unit and focused framework tests.
- Integration tests for changed infrastructure boundaries.
- The build or package task.
- Migration checks when the schema changes.

For long-running or Docker-dependent tests, make the split explicit: fast pull-request gates versus nightly or full integration gates. Whatever the split, a consequential changed boundary needs a blocking gate somewhere. CI gates claims, not checkbox volume: each gate names the failure class it stops, and a deliberate defect should fail the intended stage. Confirm that a green stage does not hide a skipped or empty test selection.

**Recovery is observed, not promised.** A runbook is a plan until it is exercised. Rollback is appropriate only when the prior artifact and all dependent data, messages, caches and effects remain compatible. After a partial data transformation, evaluate roll-forward, repair or containment before rollback. After an external effect that may have committed, reconcile before replay.

## Worked example: Java client behind a Kotlin adapter

The unsafe shape. A platform null can crash, the work is detached from the caller, cancellation and defects are swallowed, a mutable global is written, and every outcome collapses into a boolean:

```kotlin
suspend fun checkRisk(orderId: String): Boolean {
    return try {
        GlobalScope.async {
            cache[orderId] = javaRiskClient.lookup(orderId)!!.score
            true
        }.await()
    } catch (error: Exception) { false }
}
```

Before changing it, ask the owner what a Java null means and who owns the blocking policy. If that is undecided, keep null, client failure and value distinct internally. Write the discriminating fixtures first: a Java null; a known dependency exception; parent cancellation after the call has started, with cleanup, no fallback and no cache mutation; callers that need different actions; repeated and parallel cache tests.

The outcome type, used only because callers act differently on each case (use `T?` when they all act the same):

```kotlin
sealed interface RiskLookup {
    data class Found(val score: RiskScore) : RiskLookup
    object Missing : RiskLookup
    data class DependencyFailure(val cause: RiskClientFailure) : RiskLookup
}
```

The adapter:

```kotlin
suspend fun lookupRisk(orderId: OrderId): RiskLookup =
    withContext(blockingClientDispatcher) {
        try {
            javaRiskClient.lookup(orderId.value)
                ?.let { raw -> RiskLookup.Found(RiskScore.parse(raw.score)) }
                ?: RiskLookup.Missing
        } catch (cancelled: CancellationException) { throw cancelled
        } catch (failure: KnownRiskClientException) {
            RiskLookup.DependencyFailure(RiskClientFailure.from(failure))
        }
    }
```

This assumes the adapter owns the dispatcher policy and that parsing does not fail silently. Cancelling the continuation does not prove that an uninterruptible Java call was interrupted; observe prompt return versus delayed return and never claim underlying interruption without evidence. Report completion in parts: platform containment, outcome distinction and cancellation without fallback are verified; underlying interruption, dispatcher capacity and cache safety are unverified unless separately shown. If a migration fails, keep the adapter normalization and add one compatibility translation; never revert to platform leakage. Saturation routes to client replacement, a bounded pool or a durable design, not to detached coroutines.

Requirements for this kind of mixed Java and Kotlin lookup:

```markdown
REQ-KOTLIN-101.0  WHEN the Java client returns a non-null value THEN the adapter SHALL return a validated found state AND no platform type SHALL escape.
REQ-KOTLIN-102.0  WHEN the Java client returns its documented null-as-not-found THEN the adapter SHALL return an explicit missing state AND SHALL NOT use `!!`.
REQ-KOTLIN-103.0  WHEN the caller is cancelled THEN the adapter SHALL propagate cancellation AND SHALL NOT normalize it into a result.
REQ-KOTLIN-104.0  WHEN a supported Java facade calls the Kotlin API THEN it SHALL remain source and runtime compatible unless a migration is approved.
REQ-KOTLIN-105.0  WHEN the provider fails in an ordinary way THEN the adapter SHALL return a failure that is distinct from missing.
```

## Output contract

Return results in this order:

1. `Kotlin Backend Work Mode`
2. `Executable Requirements`
3. `Service Design`
4. `Kotlin/Framework Constraints`
5. `Verification Matrix`
6. `Implementation Plan`
7. `Quality Gates`
8. `Open Questions`

Use this traceability shape:

| req_id | test_id | test_type | assertion | target |
| --- | --- | --- | --- | --- |

Never silently skip `Open Questions`. Real intake surfaces unknowns; if there are none, say so in that section. A review pass, a trivial fix or a hotfix may compress the packet (a two-line requirement and a test can be enough, and a review-shaped packet carries findings in place of an implementation plan), but only when the handoff states three things: that the packet is compressed, its provenance (written before the change, or reconstructed after it; the two look identical otherwise), and the limitation that follows from the missing sections. Record the requirements as the literal delivered text, not a paraphrase. A lifecycle diagram without requirements behind it is not a sufficient packet; the diagram is an attachment to `Service Design`.

When the task is language-led (no backend surface changes), the same packet applies with these section names: `Kotlin Work Mode`, `Executable Requirements`, `Type And Boundary Design`, `Coroutine/Interop Constraints`, `Verification Matrix`, `Implementation Plan`, `Quality Gates`, `Open Questions`. A review leads with findings ordered by severity, each tied to an observable failure and a `KC1` identifier where one applies. A finding without an identifier is opinion and cannot be re-audited.

For a pre-merge review of a boundary-touching diff, record: the diff identifier, the `KC1` rows that apply, the rows scoped out with reasons, findings keyed to identifiers, answers to the six review questions in the self-check, and gate outcomes. A full fifteen-row record is ceremony for a trivial diff; use the six questions alone.

Report each gate in one of these states: `pass`, `fail`, `blocked`, `unavailable`, `not_applicable`, `expected_external_red`. Report completion as one of: `orientation_complete`, `containment_complete`, `semantic_complete`, `integration_complete`, `operationally_promoted`, `blocked`, `no_claim`. Never collapse these into "done". `not_applicable` needs a claim-specific reason, and "covered by tests" without a named behavior and test is not evidence.

## Quality gates

Use the repository wrapper. These are candidates; run only what the target configures:

```bash
./gradlew test
./gradlew build
./gradlew detekt
./gradlew ktlintCheck
./mvnw test
./mvnw verify
```

Focused iteration:

```bash
./gradlew :module:test --tests 'package.ClassName.testName'
./mvnw -pl module -Dtest=ClassName#testName test
```

If a command is missing, report that it is not configured instead of pretending the gate passed. Do not add ktlint or detekt merely because they are mentioned here. `ktlintCheck` may be skipped explicitly only when the repository has never configured it. Do not loosen the static-analysis baseline to make a gate pass. Do not substitute a global Gradle or Maven for the wrapper, and do not call a filtered test run the final gate.

The gate ladder. Later gates do not repair missing earlier evidence:

| Gate | What it does | What it proves |
| --- | --- | --- |
| G0 Target and tool discovery | Wrappers, modules, version catalogs, compiler options, CI, custom scripts | Which gates exist |
| G1 Focused behavior | The focused test above, failing first for the intended reason | The named behavior; an environment failure is not defect evidence |
| G2 Compile and build | Wrapper build | Exhaustive sealed handling, interop, visibility, API shape; not semantic or runtime proof |
| G3 Configured lint and static analysis | Only when configured; record versions, baseline, source population, exclusions | Only the rules and files it covered |
| G4 Semantic review | The scans below plus manual reading | Boundary, state, identity, coroutine, blocking and failure contracts |
| G5 Broader regression | Full supported suite or matrix | Wider behavior; report unrelated failures and their owners separately |
| G6 Runtime experiment | Controlled workload with build, environment and workload identity, warmup, concurrency, samples and counter-metrics | A bounded runtime claim; nothing else supports one |

Candidate scans for G4. They are review prompts, not verdicts:

```bash
rg -n '!!|lateinit|GlobalScope|catch\s*\(\s*(?:[A-Za-z_][A-Za-z0-9_]*\s*:\s*)?Exception' src
rg -n 'withContext\s*\(\s*Dispatchers\.IO|runCatching|object\s+[A-Za-z_][A-Za-z0-9_]*' src
rg -n '\.let\s*\{|\.also\s*\{|\.apply\s*\{|\.run\s*\{' src
```

Run them on the diff before style review. They miss aliases, fully qualified or custom dispatchers, Java catches, generated code and semantic equivalents, and they flag legitimate fixtures and rethrow-first catches. Read every hit. Swallowed cancellation and suspend-wrapped blocking compile, pass ordinary unit tests and fail under cancellation or load; reading and targeted tests are what catch them.

Manual questions for G4: where does each uncertain value enter and where is it normalized; does a null or boolean collapse states that callers act on differently; are identity, equality and copy aligned; who owns each coroutine, its state, cancellation, failure and cleanup; what actually blocks and who owns its concurrency; is expected failure translated deliberately, or are cancellation and defects captured by accident.

Rerun a gate only after code, fixture, configuration, dependency, environment or the command premise has changed. A green build proves compilation and style, not boundary reliability. A skipped or unavailable gate is not green.

Stop promotion to public or production use when: a state, identity, authorization or accepted risk has no owner; durability or idempotency is absent for a replayable effect; a migration lacks rollback or roll-forward; a capacity claim lacks a representative measurement and an objective owner; or tests cannot distinguish the fix from an environment failure.

## Anti-patterns

Kotlin code:

| Anti-pattern | What is lost | Safer default |
| --- | --- | --- |
| `!!` on an uncertain path | A distant null failure after the boundary context is gone | Parse once; typed failure or deliberate `T?` |
| Broad `lateinit` | Temporal state, races, stale values at teardown | Constructor injection, explicit lifecycle state, narrow framework binding |
| Java platform type in the domain | Hidden nullability spreads assertions and defensive branches | Adapter exports `T`, `T?` or a typed failure |
| `GlobalScope` or detached work | Lifetime, cancellation, failure, cleanup and shutdown ownership | Caller, structured or lifecycle scope; durable job for work that must survive |
| Broad `catch (Exception)` around suspend work | Cancellation becomes failure, fallback or retry | Rethrow `CancellationException`, then translate known failures |
| Opaque nested `let`/`also`/`apply`/`run` | Receiver, return value, mutation, null branch and exception point | Named locals, guards, extraction, or one clear scope function |
| Nullable field state collapse | Null merges absent, invalid, forbidden, unknown, not-loaded and failed | Value object, enum or sealed state; null only if all callers act identically |
| Data class for an identity-heavy entity | Generated equality, hash, copy and `componentN` conflict with identity, proxy and lifecycle | Plain class with explicit equality, or the framework model |
| Hidden blocking in `suspend` | Constrained threads starve; cancellation may only stop waiting | Named blocking API or owned bounded dispatcher |
| Boolean outcome erasure | True and false hide rejection, absence, conflict, retryable and terminal failure | Named enum, sealed outcome or typed exception |
| Mutable global singleton | Hidden dependencies, test leakage, races, unclear reset and shutdown | Constructor, lifecycle, request or session injection; owned synchronized cache |
| Generic `Result<Any>` or broad `runCatching` | Expected failures, cancellation and defects become one channel | Narrow taxonomy and typed translation; preserve cancellation and defects |

Fix the earliest loss of information or ownership first. A downstream fix alone is incomplete:

- Removing a downstream `!!` while platform types still spread only moves the crash.
- Adding `Dispatchers.IO` while the work is still detached hides saturation.
- Adding a sealed outcome while every caller maps it back to a boolean adds ceremony without preserving meaning.

| Area | Earliest contract loss | Tempting incomplete fix | Root-first action |
| --- | --- | --- | --- |
| Platform nullability | Interop uncertainty leaves the adapter | Replace `!!` with `?: return null` | Decide and encode the boundary states before the value reaches the domain |
| Cancellation | Parent control becomes an ordinary failure | Add another fallback or retry | Preserve cancellation before translating known failures |
| Identity | Value syntax is applied to a lifecycle object | Customize one equality test without defining identity | Name the identity and the framework or persistence contract first |
| Blocking | The suspend signature hides execution behavior | Add `Dispatchers.IO` and claim scalability | Identify the dependency's behavior and the execution owner, then measure capacity separately |
| Global state | Mutable lifetime and synchronization are implicit | Clear the singleton in one test teardown | Scope or inject the state and define its lifecycle and concurrency policy |
| Scope functions and booleans | Several failure states collapse into null or false | Add comments to the chain | Separate the steps and model the outcomes callers act on |

Backend delivery:

- Defaulting to `@SpringBootTest` when a slice test proves the behavior.
- Business invariants that live only in Bean Validation annotations on transport DTOs.
- JPA entities modeled as ideal Kotlin data classes without checking proxying, no-arg construction, equality and lazy loading.
- Blocking persistence mixed into reactive or coroutine flows without naming the dispatcher and the operational tradeoff.
- Retries recommended without idempotency, timeout budgets and failure classification.
- A framework migration smuggled into a feature task.
- A transaction held across a remote call.
- Serializing persistence entities as the public response.
- Fire-and-forget coroutines from request handlers for critical work.
- H2 accepted as proof of production-dialect SQL or locking.
- Sleep-based coroutine tests, shared mutable fixtures, and mocked repositories that hide transaction races.
- Identity or tenant taken from the payload; coarse role checks instead of resource policy; CSRF disabled under ambient cookies; secrets or raw provider errors in diagnostics.
- Readiness that is only "the process is alive"; liveness that fails on a dependency outage.
- A breaking schema change in a single step; migration confidence from an empty database; an unbounded migration coupled to startup.
- A green pipeline that proves a different claim; an artifact rebuilt per environment; a rollout with nobody authorized to stop it.
- Telemetry with no decision behind it; unbounded metric dimensions.
- Using the word "rollback" as if it were a recovery plan.
- Precise latency, capacity or risk numbers quoted without a method and a workload.

## Bundled scripts

This skill bundles no scripts, templates or assets. Every command above runs against the target repository's own wrapper and tools. Check that a task exists before reporting on it, and never report a remembered command as executed evidence.

## Closing self-check

Before finishing any Kotlin work, verify:

1. Boundary inputs are parsed or normalized before domain logic.
2. Domain types are non-null unless absence is meaningful.
3. No new `!!`, broad `lateinit` or platform-type leakage exists.
4. Expected failures are modeled with typed outcomes or typed exceptions.
5. Coroutine code preserves structured concurrency and cancellation.
6. Blocking calls are isolated or intentionally exposed as blocking.
7. Tests cover the highest-risk behavior, not only the happy path.
8. Existing build, format, lint and static-analysis gates were run, or explicitly skipped with a reason.

Compact pass before handoff:

- **Nullability:** are nullable values introduced only where absence is real?
- **Interop:** are Java platform types contained?
- **Types:** are primitive IDs, units and closed states made explicit?
- **Coroutines:** does cancellation propagate and does blocking stay named?
- **Tests:** does the suite prove malformed input, cancellation and boundary behavior?
- **Gates:** were the repository's own tests and static checks run?

Six Kotlin review questions:

1. Does any platform type escape past an adapter?
2. Could `!!` fail in production from malformed or old data?
3. Are business outcomes modeled as data instead of log messages or generic exceptions?
4. Does cancellation propagate through every suspend boundary?
5. Is a scope function hiding which object is being read or returned?
6. Are tests proving nullability, cancellation, parse errors and interop behavior where those are the risks?

Service design:

- Are Kotlin nullability and domain absence aligned?
- Are framework annotations contained to framework layers?
- Are transactions located around service workflows?
- Are blocking calls isolated or intentionally blocking?
- Are request validation and domain validation both represented?
- Are expected business errors visible and mapped?
- Are migrations and rollouts covered when storage changes?
- Are tests proving the boundary that can actually break?

Security and resilience:

- Are all inbound boundaries parsed and validated?
- Are expected domain failures distinct from infrastructure failures?
- Are auth negative paths tested?
- Are secrets redacted?
- Are retries bounded and idempotent?
- Are external calls timed out?
- Is cancellation preserved?
- Is background work durable if it must be durable?

Operations:

- How does the service fail when config is missing?
- Are secrets redacted from logs and errors?
- Can the deployment roll forward if a migration fails?
- Are metrics and logs enough to debug a bad release?
- Is graceful shutdown safe for in-flight requests and workers?
- Are background jobs idempotent across retries and restarts?

Evidence:

- Did the framework, build tool and versions stay as found, or is the migration explicit in the request?
- Does every requirement have a row in the verification matrix, and did each test fail first for the intended reason?
- Is every gate reported in its real state, with commands, exit status and exclusions?
- Is every non-functional number tied to an owner's objective or labeled as unmeasured?
- Does the handoff say what is verified, what is conditional, what is blocked and who owns each open question?

Depth on scoring, tradeoffs, worked examples, failure modes, workload, retry and backpressure, observability, performance verification, source mapping and refresh queries is in [reference.md](reference.md).
