# Kotlin Spring And Ktor Idioms

Use this reference for framework-specific decisions after the service boundary is clear.

## Spring Boot With Kotlin

Prefer Spring Boot defaults unless the requirement proves a customization is necessary.

### Package And Bean Structure

- Keep the `@SpringBootApplication` class slim and in a root package above application components.
- Use constructor injection. Kotlin primary constructors make this natural.
- Prefer small configuration classes over broad component scans.
- Keep controllers thin: parse, authorize, call application service, map result.
- Keep application services responsible for transaction workflows and orchestration.
- Keep repositories focused on persistence, not business decision logic.

### Kotlin Compiler Plugins

Kotlin classes are final by default. Spring AOP/proxying and JPA can require openness or no-arg constructors.

- Use the Kotlin Spring/all-open plugin when Spring proxying needs open classes.
- Use Kotlin JPA/no-arg support when JPA entities need synthetic no-arg constructors.
- Do not add `open` everywhere manually unless the repo has deliberately avoided compiler plugins.
- Keep plugin versions aligned with the Kotlin version managed by the build.

### Configuration

- Prefer typed `@ConfigurationProperties` for structured settings.
- Validate required settings at startup.
- Avoid scattered `@Value` usage for multi-field configuration.
- Keep secrets out of source and test fixtures.
- Keep environment-specific differences in configuration layers, not branching application code.

### MVC, WebFlux, And Coroutines

- Use Spring MVC for conventional blocking servlet services.
- Use WebFlux/coroutines only when the repository and dependencies are actually non-blocking or the team accepts the complexity.
- Do not call blocking JPA/JDBC from a reactive event-loop path without explicit isolation.
- Use suspend controller/service functions only when the surrounding stack supports the execution model.

### Validation And Error Handling

- Use Bean Validation for transport-level shape and simple constraints.
- Put business invariants in domain/application code, not only annotations.
- Centralize exception/response mapping with controller advice or the repo's existing error mapper.
- Keep public error contracts stable and avoid leaking implementation exception names.

### Persistence With Spring

- Put `@Transactional` on service workflows or clearly scoped repository operations.
- Avoid long transactions that include external API calls.
- For JPA entities, check data-class equality, generated IDs, lazy relations, proxying, and no-arg needs before using idiomatic Kotlin shortcuts.
- Prefer migrations for schema changes; do not rely on auto-DDL in production.

## Ktor With Kotlin

Use Ktor when explicit plugin composition and coroutine-first request handling are part of the project shape.

### Application Structure

- Keep `Application.module` or equivalent bootstrapping small.
- Install plugins deliberately: content negotiation, authentication, status pages, call logging, compression, CORS, rate limiting, resources/type-safe routing.
- Group routes by business capability, not by HTTP verb alone.
- Keep route handlers thin and delegate to application services.
- Avoid global mutable singletons for services, clients, and repositories unless the repo has an intentional DI/container pattern.

### Serialization

- Use Ktor content negotiation consistently.
- Prefer kotlinx.serialization for Kotlin-first DTOs when it matches the project; use Jackson when Spring/Jackson compatibility or existing Java ecosystem integration is the project norm.
- Configure unknown keys, defaults, naming, and date/time serialization intentionally.

### Status Pages And Errors

- Install status pages or the repo's equivalent central error mapper.
- Map expected domain failures to stable responses.
- Log infrastructure failures with correlation context but avoid logging secrets or raw credentials.

### Type-Safe Routing

- Consider Ktor Resources/type-safe routing for APIs where route parameters and nesting are easy to misuse.
- Do not introduce route DSL complexity if the service has only a few simple endpoints.

### Ktor Testing

- Use `testApplication` for route/plugin behavior without binding sockets.
- Use fake repositories for pure route contract tests.
- Use Testcontainers when the route behavior depends on real persistence, broker, or external service behavior.

## Cross-Framework Idioms

### Naming

Follow official Kotlin style for packages, classes, functions, and properties. Do not force four-word naming onto idiomatic Kotlin public APIs when it makes the code un-Kotlin-like; use descriptive names and stable domain vocabulary instead.

### Null Safety

- Treat platform types from Java libraries as unsafe until checked.
- Avoid `!!` in production code except at narrow, documented interop boundaries.
- Prefer explicit conversion from nullable transport data to non-null domain data.

### Data Classes

Use data classes for DTOs, commands, and immutable value carriers. Be cautious for entities with identity, lazy loading, mutation, or framework lifecycle hooks.

### Value Classes

Use value classes for identifiers and constrained wrappers when supported by serialization/persistence. Add tests for JSON mapping, database mapping, and reflection-heavy frameworks before relying on them broadly.

### Sealed Outcomes

Use sealed result types for closed business outcomes when it improves exhaustiveness and response mapping. Avoid creating custom result hierarchies for every trivial branch.
