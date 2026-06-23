---
name: kotlin-backend-delivery-01
description: Plan, build, harden, and review Kotlin backend services with Spring Boot, Ktor, coroutines, typed configuration, persistence, migrations, testing, security, resilience, and operations. Use for Kotlin HTTP APIs, workers, service refactors, production-readiness reviews, or JVM backend architecture decisions.
---

# Kotlin Backend Delivery 01

Use this skill to turn Kotlin backend requests into decision-complete work packets that are spec-first, Kotlin-idiomatic, framework-aware, and production-biased.

Prefer Kotlin plus Spring Boot as the default enterprise path when the repository already uses Spring, JPA, Spring Security, Actuator, or the JVM ecosystem. Prefer Ktor when the repository is explicitly Ktor-first, lightweight plugin-first, coroutine-native, or multiplatform-adjacent. Preserve the existing framework, build tool, Java target, dependency versions, and deployment model unless the request explicitly includes a migration.

## Mode Selection

Choose one or more modes before planning or coding:

- `Spec Mode`: vague backend requests, missing acceptance criteria, or greenfield service work that needs `REQ-KOTLIN-BACKEND-*` contracts.
- `Spring Boot Mode`: controllers, services, repositories, validation, configuration properties, Spring Security, Actuator, MVC/WebFlux, Spring Data, Flyway/Liquibase, or Spring test slices.
- `Ktor Mode`: routes, plugins, content negotiation, status pages, resources/type-safe routing, Ktor auth, testApplication, and coroutine-native request handling.
- `Persistence Mode`: JPA/Hibernate, Spring Data, Exposed, jOOQ, JDBC/R2DBC, transaction scope, migrations, repository boundaries, or query performance.
- `Coroutine Mode`: suspend APIs, Flow, dispatcher choice, cancellation, timeouts, structured concurrency, and blocking-call isolation.
- `Security Mode`: auth, sessions, JWT/OAuth2/resource server flows, CSRF, password storage, reset flows, validation, and anti-enumeration behavior.
- `Resilience Mode`: retries, idempotency, external clients, durable background work, transaction boundaries, timeout budgets, and failure classification.
- `Operations Mode`: typed config, secrets, profiles, logging, tracing, metrics, health checks, CI, containers, deployment, and rollout safety.
- `Review Mode`: architecture drift, production readiness, framework misuse, Kotlin anti-patterns, and test strategy review.

Default combinations:

- new endpoint or feature: `Spec Mode` + framework mode + `Persistence Mode` if storage changes.
- auth or account flow: `Spec Mode` + framework mode + `Security Mode`.
- external API or workflow: `Spec Mode` + `Coroutine Mode` + `Resilience Mode`.
- migration or deployment change: `Persistence Mode` + `Operations Mode`.
- review or hardening pass: `Review Mode` plus the most relevant risk mode.

## Workflow

1. Classify the backend surface.
- Name the surface first: Spring MVC API, Spring WebFlux service, Ktor service, worker, scheduled job, message consumer, migration, external client, or review pass.
- State whether the main risk is ambiguity, Kotlin/JVM framework compatibility, persistence correctness, coroutine safety, security, resilience, or operations.

2. Write executable requirements.
- Use `REQ-KOTLIN-BACKEND-<NNN>.<REV>` identifiers.
- Express behavior as `WHEN...THEN...SHALL`.
- Reject vague claims such as "production-ready", "idiomatic", "secure", or "fast" without observable criteria.

3. Select the framework stance before coding.
- Preserve Spring Boot versus Ktor unless a migration is requested.
- Preserve Gradle/Maven, Java target, Kotlin version, Spring Boot/Ktor version, database stack, and runtime style.
- Decide whether the feature belongs in controller/route, application service, domain model, persistence adapter, external client, or background worker.

4. Design Kotlin and service boundaries.
- Keep transport DTOs, domain types, persistence models, and API responses distinct when they carry different invariants.
- Prefer Kotlin nullability, value classes, sealed result/error types, and immutable data for business boundaries.
- Avoid leaking platform types, nullable surprises, framework annotations, or ORM lifecycle concerns into the domain core.

5. Apply framework-specific constraints.
- In Spring Boot, prefer constructor injection, slim application bootstrap, typed `@ConfigurationProperties`, focused test slices, explicit transactions, and Kotlin Spring/JPA compiler plugins when framework proxying or JPA construction requires them.
- In Ktor, keep plugins explicit, install serialization/auth/status-pages deliberately, test with the Ktor test host, and avoid hiding route behavior behind global mutable state.

6. Treat coroutines as correctness-sensitive.
- Preserve structured concurrency.
- Do not use `GlobalScope` for request work.
- Propagate cancellation and deadlines across service and client calls.
- Isolate blocking JDBC/JPA/file calls onto an appropriate dispatcher or keep the service intentionally blocking instead of pretending it is non-blocking.

7. Choose the verification mix deliberately.
- Pick from unit tests, Spring slices, `@SpringBootTest`, Ktor `testApplication`, Testcontainers, migration tests, HTTP mock tests, contract tests, property tests, and production smoke checks.
- Prefer the lightest test that proves the behavior, but use real infrastructure when persistence, messaging, or external service behavior is part of the requirement.

8. Run quality gates before handoff.
- Use the repository wrapper: `./gradlew test`, `./gradlew build`, `./gradlew detekt`, `./gradlew ktlintCheck`, or the Maven equivalents if present.
- Require evidence for requirement coverage, migration safety, security behavior, and non-functional claims.

## Output Contract

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

## Guardrails

- Do not use this skill for Android UI work, Kotlin Multiplatform client work, or generic Kotlin syntax questions unless they affect backend delivery.
- Do not default to `@SpringBootTest` when a slice test proves the behavior.
- Do not put business invariants only in Bean Validation annotations on transport DTOs.
- Do not model JPA entities as ideal Kotlin data classes without checking proxying, no-arg construction, equality, and lazy-loading implications.
- Do not mix blocking persistence into reactive/coroutine flows without naming the dispatcher and operational tradeoff.
- Do not recommend retries without idempotency, timeout budgets, and failure classification.
- Do not treat Actuator, metrics, logging, migrations, and secrets as afterthoughts for production services.

## Context Strategy

Load progressively:

1. Read [Reference map](./references/reference-map.md) first.
2. Read [Kotlin backend playbook](./references/kotlin-backend-playbook.md) for service anatomy, framework choice, boundaries, and delivery defaults.
3. Read [Kotlin Spring and Ktor idioms](./references/kotlin-spring-ktor-idioms.md) for framework-specific design rules.
4. Read [Kotlin backend testing and fixtures](./references/kotlin-backend-testing-and-fixtures.md) for verification strategy.
5. Read [Kotlin backend runtime and ops](./references/kotlin-backend-runtime-and-ops.md) for configuration, observability, deployment, migrations, and static analysis.
6. Read [Kotlin backend security and resilience](./references/kotlin-backend-security-and-resilience.md) for auth, validation, idempotency, retries, coroutine cancellation, and external systems.
7. Read [Sources and research brief](./references/sources-and-research-brief.md) when checking provenance or updating the doctrine.

For large references, prefer heading search:

- `rg '^##|^###' references/kotlin-backend-playbook.md`
- `rg '^##|^###' references/kotlin-spring-ktor-idioms.md`
- `rg '^##|^###' references/kotlin-backend-testing-and-fixtures.md`
- `rg '^##|^###' references/kotlin-backend-runtime-and-ops.md`
- `rg '^##|^###' references/kotlin-backend-security-and-resilience.md`

## References

- [Reference map](./references/reference-map.md)
- [Kotlin backend playbook](./references/kotlin-backend-playbook.md)
- [Kotlin Spring and Ktor idioms](./references/kotlin-spring-ktor-idioms.md)
- [Kotlin backend testing and fixtures](./references/kotlin-backend-testing-and-fixtures.md)
- [Kotlin backend runtime and ops](./references/kotlin-backend-runtime-and-ops.md)
- [Kotlin backend security and resilience](./references/kotlin-backend-security-and-resilience.md)
- [Sources and research brief](./references/sources-and-research-brief.md)
