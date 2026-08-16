# Kotlin Backend Runtime And Ops

Use this reference when work touches configuration, observability, deployment, CI, migrations, or production safety.

## Build And Dependency Discipline

- Use the repository's Gradle or Maven wrapper.
- Preserve Kotlin, Java, Spring Boot, Ktor, and plugin versions unless the task is an upgrade.
- Keep Kotlin compiler plugin versions aligned with the Kotlin version.
- Prefer Gradle Kotlin DSL in Kotlin-first projects when already present.
- Do not add dependency-management systems or build plugins just because they are fashionable.

## Static Analysis And Formatting

Common Kotlin gates:

- Official Kotlin coding conventions for style and organization.
- ktlint or an equivalent formatter/linter for consistent formatting.
- detekt for Kotlin-specific static analysis and maintainability rules.

Do not conflate formatter success with architecture quality. Use ktlint for style; use detekt and review for complexity, long functions, risky exception handling, and maintainability.

## Configuration And Secrets

- Prefer typed configuration objects.
- Validate required settings at startup.
- Keep secrets in environment/secret stores, not repository files.
- Keep test secrets fake and obviously non-production.
- Avoid config lookups deep inside business logic; inject typed config at the boundary.

For Spring Boot, use `@ConfigurationProperties` for structured configuration. For Ktor, bind config once at startup and pass typed settings into modules/services.

## Profiles And Environments

- Keep environment differences declarative.
- Avoid branching business behavior on environment name.
- Document required environment variables and config keys.
- Test production-like config paths when deployment behavior changes.

## Observability

Minimum production service observability:

- Structured logs with request/correlation id.
- Error logs that classify domain, transport, and infrastructure failures.
- Metrics for request count, latency, failures, external calls, queue lag, and worker outcomes.
- Health/readiness checks that reflect critical dependencies.
- Trace propagation for inbound and outbound calls when the platform supports it.

For Spring Boot, Actuator and Micrometer are the default ecosystem path. For Ktor, install and configure equivalent call logging, metrics, health, and tracing integrations deliberately.

## Database Migrations

Treat migrations as deployable code:

- Store migration files with the application.
- Use versioned migrations for schema evolution.
- Test migrations against the production dialect when possible.
- Separate expand and contract steps for backwards-incompatible changes.
- Plan rollback or roll-forward behavior.
- Verify application compatibility during rolling deploys.

Flyway and Liquibase are both acceptable if already used by the repo. Preserve the repo's migration tool.

## Container And Deployment Safety

- Keep the runtime image small and deterministic.
- Run as non-root when possible.
- Expose only required ports.
- Configure graceful shutdown for HTTP servers and workers.
- Ensure readiness does not pass before the service can handle real traffic.
- Ensure liveness does not flap during slow startup or migration windows.

## CI Expectations

At minimum, backend CI should run:

- format/lint/static analysis if configured.
- unit and focused framework tests.
- integration tests for changed infrastructure boundaries.
- build/package task.
- migration checks when schema changes.

For long-running or Docker-dependent tests, make the split explicit: fast PR gates versus nightly/full integration gates.

## Operational Review Questions

- How does the service fail when config is missing?
- Are secrets redacted from logs and errors?
- Can the deployment roll forward if a migration fails?
- Are metrics and logs enough to debug a bad release?
- Is graceful shutdown safe for in-flight requests and workers?
- Are background jobs idempotent across retries and restarts?
