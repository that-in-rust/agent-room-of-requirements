# Kotlin Backend Testing And Fixtures

Use this reference to choose the lightest verification that proves backend behavior.

## Testing Philosophy

Start from the boundary that can break:

- Pure domain invariant: unit test.
- Controller/route mapping: Spring slice or Ktor test host.
- Persistence query/mapping: repository test or real database test.
- Cross-layer request behavior: app integration test.
- External API behavior: HTTP mock/contract test.
- Migration behavior: migration test against a real database.
- Retry/idempotency behavior: integration or focused workflow test with failure injection.

Do not default to full application startup for every test. Do use full startup when the requirement depends on real wiring.

## Spring Boot Tests

Prefer focused slices first:

- `@WebMvcTest` for MVC controller request/response behavior.
- `@JsonTest` for serialization contracts.
- `@DataJpaTest` for JPA repository and mapping behavior.
- `@SpringBootTest` when cross-layer wiring, security filters, configuration, or infrastructure integration must be proven.

Use Testcontainers when a real database, broker, or dependent service changes the behavior under test. H2-only tests are not proof of PostgreSQL/MySQL-specific SQL behavior.

## Ktor Tests

Use Ktor `testApplication` for route and plugin behavior. It exercises application calls internally without binding a real socket, which is usually faster and less flaky than booting a network server for route tests.

Ktor route tests should cover:

- Installed content negotiation and request parsing.
- Authentication/authorization path.
- Status page/error mapping.
- Serialization response shape.
- Route parameter and query validation.

Use real infrastructure only when repository, transaction, broker, or external service behavior is part of the requirement.

## Kotlin Test Frameworks

Use the repository's existing test framework. Common choices:

- JUnit 5: default for Spring Boot and many JVM services.
- Kotest: expressive Kotlin test styles, assertions, and property testing.
- MockK: Kotlin-native mocking, including coroutine-aware mocking.
- SpringMockK or equivalent helpers only if already adopted or necessary.

Prefer fakes over mocks for domain services when the dependency behavior is simple. Prefer mocks for hard-to-construct collaborators, provider adapters, and behavior verification at narrow boundaries.

## Coroutine Testing

For coroutine-heavy code:

- Use coroutine test utilities when controlling dispatchers, delays, or virtual time.
- Verify cancellation propagation for long-running work.
- Verify timeout behavior for external clients.
- Avoid tests that pass only because real sleeps happen to be long enough.

## Persistence Tests

Persistence tests should prove:

- Migrations apply from empty database.
- Critical queries match production dialect behavior.
- Transaction boundaries commit and roll back as expected.
- Optimistic locking or concurrency behavior works when used.
- Repository methods do not accidentally trigger N+1 query patterns on hot paths.

For Exposed, remember that database operations run inside transactions. For jOOQ, prefer generated schema-backed queries when the project uses code generation.

## Contract And API Tests

For public APIs:

- Test HTTP status, headers, response envelope, and error body.
- Test invalid JSON, invalid route parameter, invalid query parameter, and missing auth.
- Test duplicate/idempotent submissions where retry is possible.
- Test pagination stability and deterministic ordering.
- Test serialization of Kotlin value classes and date/time types when exposed.

## Property Tests

Use property tests for parsers, validators, canonicalizers, pagination cursors, idempotency keys, and state transitions with large input space. Do not use property tests as a replacement for concrete examples that document the API contract.

## Verification Matrix Template

| req_id | test_id | test_type | assertion | target |
| --- | --- | --- | --- | --- |
| REQ-KOTLIN-BACKEND-001.0 | createAccountReturns201 | Spring `@WebMvcTest` or Ktor `testApplication` | valid request returns 201 and public id | transport boundary |
| REQ-KOTLIN-BACKEND-001.0 | duplicateEmailReturns409 | integration/database test | duplicate normalized email is rejected atomically | service plus persistence |
| REQ-KOTLIN-BACKEND-002.0 | migrationAppliesCleanly | Testcontainers migration test | schema migrates from empty database | migration path |

## Quality Gates

Prefer the repo's wrapper commands:

- `./gradlew test`
- `./gradlew build`
- `./gradlew detekt`
- `./gradlew ktlintCheck`
- `./mvnw test`
- `./mvnw verify`

If a command is missing, report that it is not configured instead of pretending the gate passed.
