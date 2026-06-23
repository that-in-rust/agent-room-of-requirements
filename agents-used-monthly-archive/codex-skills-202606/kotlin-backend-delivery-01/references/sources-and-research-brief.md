# Sources And Research Brief

Research date: 2026-06-23.

This brief synthesizes official Kotlin, Spring, Ktor, JetBrains, and ecosystem documentation plus representative GitHub repositories. Treat sourced facts as stronger than synthesis; treat design recommendations as inference when they combine multiple sources.

## Premise Check

- Sound premise: Kotlin backend delivery needs a dedicated skill, because Kotlin backend risk is not just language syntax. The risk clusters around Spring/Ktor framework integration, nullability, coroutines, persistence, testing, and JVM operations.
- Correction: There is no single universal "Kotlin backend best practice" source. The skill should preserve local framework choices and route progressively across Spring Boot, Ktor, persistence, security, testing, and operations.
- Important constraint: Kotlin/Spring and Kotlin/Ktor share language concerns, but their framework ergonomics differ enough to require separate modes.

## Expert Lenses

- Kotlin/JVM language specialist: emphasizes nullability, platform types, value classes, data classes, sealed outcomes, compiler plugins, and coroutine semantics.
- Backend operator: emphasizes migrations, config, secrets, observability, health checks, timeouts, retries, and deployment safety.
- Spring/Ktor framework implementer: emphasizes test slices, plugins, typed config, DI, transaction scope, and route/controller boundaries.
- Skeptical reviewer: challenges over-broad claims, fake non-blocking designs, all-purpose data classes, and full-stack rewrites disguised as feature work.

## Candidate Approaches

| option | upside | downside | verdict |
| --- | --- | --- | --- |
| Generic `kotlin-coder-01` | Broad and easy to trigger | Too shallow for backend production risk | Reject for this goal |
| `spring-boot-kotlin-coder-01` only | Strong enterprise focus | Misses Ktor and generic Kotlin backend work | Useful subset, too narrow |
| `kotlin-backend-delivery-01` with Spring/Ktor modes | Covers the user journey and preserves local choices | Higher maintenance cost than a single-framework skill | Chosen |

## Chosen Thesis

Build `kotlin-backend-delivery-01` as a production backend delivery skill. Use Spring Boot as the default enterprise lane, Ktor as an explicit lightweight/coroutine-native lane, and shared references for Kotlin language, persistence, testing, runtime, security, and resilience concerns.

## Evidence Summary

### Kotlin Language And Server-Side

- Kotlin's official backend overview frames Kotlin as suitable for server-side applications while preserving compatibility with Java technology stacks: https://kotlinlang.org/docs/server-overview.html
- Kotlin official coding conventions define style and organization guidance for Kotlin projects: https://kotlinlang.org/docs/coding-conventions.html
- Kotlin coroutine docs emphasize structured concurrency, coroutine context, cancellation, timeouts, and exception handling: https://kotlinlang.org/docs/coroutines-basics.html, https://kotlinlang.org/docs/cancellation-and-timeouts.html, https://kotlinlang.org/docs/coroutine-context-and-dispatchers.html, https://kotlinlang.org/docs/exception-handling.html
- Kotlin data classes and serialization docs support DTO/value-carrier guidance: https://kotlinlang.org/docs/data-classes.html, https://kotlinlang.org/docs/serialization.html
- Kotlin all-open and no-arg plugin docs explain why frameworks such as Spring AOP and JPA need compiler-plugin support around final classes and no-arg construction: https://kotlinlang.org/docs/all-open-plugin.html, https://kotlinlang.org/docs/no-arg-plugin.html

### Spring Boot And Spring Framework Kotlin

- Spring Boot Kotlin support and Spring Kotlin docs establish Kotlin as a first-class Spring path: https://docs.spring.io/spring-boot/reference/features/kotlin.html, https://docs.spring.io/spring-framework/reference/languages/kotlin.html
- Spring coroutine support documents coroutine integration points in the Spring ecosystem: https://docs.spring.io/spring-framework/reference/languages/kotlin/coroutines.html
- Spring Boot testing docs support focused test slices such as web MVC tests and full app tests when appropriate: https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html
- Spring Security Kotlin configuration docs support using the native Kotlin DSL for security configuration: https://docs.spring.io/spring-security/reference/servlet/configuration/kotlin.html
- Spring Boot Actuator health and metrics docs support health/readiness and Micrometer-backed metrics guidance: https://docs.spring.io/spring-boot/api/rest/actuator/health.html, https://docs.spring.io/spring-boot/reference/actuator/metrics.html
- Spring Boot Testcontainers docs support real-dependency integration tests: https://docs.spring.io/spring-boot/reference/testing/testcontainers.html
- Spring's official Kotlin tutorial repository is a useful canonical sample: https://github.com/spring-guides/tut-spring-boot-kotlin

### Ktor

- Ktor official docs frame Ktor as a Kotlin framework for asynchronous servers and clients: https://ktor.io/
- Ktor routing, type-safe routing, serialization, and testing docs support route/plugin/testing recommendations: https://ktor.io/docs/routing.html, https://ktor.io/docs/type-safe-routing.html, https://ktor.io/docs/server-serialization.html, https://ktor.io/docs/server-testing.html
- Ktor's database integration tutorial uses Exposed and repository injection patterns: https://ktor.io/docs/server-integrate-database.html
- The official Ktor samples repository provides implementation precedents: https://github.com/ktorio/ktor-samples

### Persistence

- JetBrains Exposed docs describe Exposed as a Kotlin SQL library with DSL and DAO APIs, and require database work inside transactions: https://www.jetbrains.com/help/exposed/home.html, https://www.jetbrains.com/help/exposed/transactions.html
- jOOQ documentation describes type-safe SQL generation and Kotlin usage: https://www.jooq.org/, https://www.jooq.org/doc/latest/manual/getting-started/jooq-and-kotlin/, https://www.jooq.org/doc/latest/manual/sql-building/kotlin-sql-building/
- Flyway documentation and Spring Boot Actuator Flyway endpoint docs support migration visibility and versioned migration thinking: https://documentation.red-gate.com/fd, https://docs.spring.io/spring-boot/api/rest/actuator/flyway.html

### Testing And Static Analysis

- Kotest documentation supports expressive Kotlin testing and property testing: https://kotest.io/, https://kotest.io/docs/proptest/property-based-testing.html
- MockK documentation supports Kotlin-native mocking and coroutine-aware testing concerns: https://mockk.io/
- Testcontainers Java docs support disposable real infrastructure for integration tests: https://java.testcontainers.org/
- ktlint and detekt are common Kotlin style/static-analysis tools: https://github.com/pinterest/ktlint, https://detekt.dev/

### Representative GitHub Repositories

- Spring guide: https://github.com/spring-guides/tut-spring-boot-kotlin
- Spring Kotlin demo: https://github.com/sdeleuze/spring-boot-kotlin-demo
- Ktor official samples: https://github.com/ktorio/ktor-samples
- RealWorld Kotlin Spring example: https://github.com/gothinkster/kotlin-spring-realworld-example-app
- RealWorld Kotlin Ktor example: https://github.com/Rudge/kotlin-ktor-realworld-example-app
- Exposed: https://github.com/JetBrains/Exposed
- kotlinx.serialization: https://github.com/Kotlin/kotlinx.serialization
- detekt: https://github.com/detekt/detekt
- Kotest: https://github.com/kotest/kotest
- MockK: https://github.com/mockk/mockk

## Verification Questions

1. Does the doctrine distinguish Spring Boot and Ktor instead of pretending one framework rule covers both? Yes: it uses separate modes and framework-specific references.
2. Does it cover Kotlin-specific backend risks? Yes: nullability, data/value classes, compiler plugins, coroutines, cancellation, and platform interop are represented.
3. Does it cover production backend risks? Yes: persistence, migrations, auth, retries, idempotency, metrics, health, config, secrets, deployment, and CI are represented.
4. Does it avoid overclaiming "all best practices"? Yes: it records that no universal source exists and treats the skill as a synthesis from primary docs and representative repos.
5. Does it support progressive disclosure? Yes: `SKILL.md` routes to targeted references rather than embedding all details.
