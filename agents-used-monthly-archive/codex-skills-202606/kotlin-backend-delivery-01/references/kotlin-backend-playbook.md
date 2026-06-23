# Kotlin Backend Playbook

Use this reference for the service-level shape of Kotlin backend work before choosing framework-specific details.

## Service Anatomy

Treat a Kotlin backend request path as six boundaries:

1. Transport boundary: controller, Ktor route, request parser, authentication principal, response mapping.
2. Application boundary: use-case service, transaction choreography, idempotency decision, external-call sequencing.
3. Domain boundary: value objects, invariants, state transitions, domain errors.
4. Persistence boundary: repository or DAO, SQL/query design, transaction scope, migration compatibility.
5. Integration boundary: HTTP clients, message brokers, queues, third-party APIs, retry/timeout policy.
6. Runtime boundary: config, secrets, logging, metrics, health, deployment, and rollback behavior.

Keep these boundaries visible unless the codebase is intentionally tiny. Kotlin reduces boilerplate; it does not remove the need to name risky boundaries.

## Framework Choice

Preserve the existing framework by default.

- Prefer Spring Boot when the service already uses Spring Data, Spring Security, Actuator, dependency injection, enterprise deployment conventions, servlet MVC, or WebFlux.
- Prefer Ktor when the service already uses Ktor plugins, explicit routing, coroutine-first request handling, lightweight deployment, or multiplatform-adjacent shared models.
- Do not migrate Spring to Ktor or Ktor to Spring while delivering a feature unless the migration is the explicit task.

## Executable Requirements

Use `REQ-KOTLIN-BACKEND-<NNN>.<REV>` requirements.

Example:

```markdown
### REQ-KOTLIN-BACKEND-001.0: Create Account Endpoint

WHEN a valid create-account request is submitted
THEN the service SHALL create one account record
AND SHALL return HTTP 201 with the public account id
AND SHALL reject duplicate email addresses with HTTP 409
AND SHALL not leak whether an inactive account exists.
```

Every non-functional claim needs evidence: p95 latency threshold, retry count, timeout budget, migration safety check, or security assertion.

## Kotlin Domain Modeling

Prefer Kotlin types that encode intent:

- Use `data class` for immutable DTOs and read models.
- Use `@JvmInline value class` for identifiers and small validated wrappers when framework serialization and persistence support are understood.
- Use sealed interfaces/classes for closed business outcomes, domain errors, and state machines.
- Use nullable types only when absence is a real domain state.
- Keep raw `String`, `Long`, and `UUID` values from drifting across multiple layers when they represent domain-specific identifiers.

Avoid overusing data classes for mutable persistence entities. JPA entities often need proxying, no-arg construction, identity semantics, and lifecycle rules that conflict with ideal data-class behavior.

## DTO, Domain, And Persistence Separation

Use separate shapes when invariants differ:

- Request DTO: external input, validation annotations, serialization concerns.
- Domain command: trusted application input after parsing and authentication.
- Domain entity/value: business invariants and transitions.
- Persistence model/entity: ORM or SQL mapping concerns.
- Response DTO: stable public contract.

Small apps can map manually. Larger apps can use explicit mappers. Avoid implicit "one class for everything" unless the domain is intentionally CRUD-only and the tradeoff is named.

## Error Modeling

Prefer explicit expected failures:

- Domain errors: duplicate account, invalid state transition, insufficient balance.
- Transport errors: malformed JSON, missing auth, invalid route parameter.
- Infrastructure errors: database unavailable, external timeout, broker failure.

Map expected domain errors to stable response codes at the transport boundary. Do not let exceptions be the only documented business API.

## Persistence Defaults

Choose the persistence style deliberately:

- Spring Data JPA/Hibernate: good for conventional CRUD and aggregate persistence, but check Kotlin all-open/no-arg/JPA plugin needs, lazy-loading behavior, equals/hashCode, and transaction boundaries.
- Spring Data JDBC: good for simpler aggregate persistence with less ORM magic.
- Exposed DSL: good for Kotlin-first SQL with explicit transaction blocks.
- jOOQ: good for SQL-first teams that want generated, type-safe query building and direct database control.
- R2DBC/reactive stores: useful only when the whole stack is reactive/non-blocking and the operational complexity is justified.

Migration safety matters more than ORM preference. Schema changes require migration files, compatibility checks, and rollback/roll-forward thought.

## Transaction Boundaries

Keep transactions around application service workflows, not controllers/routes.

Name the transaction scope before coding:

- Single write transaction.
- Read-modify-write transaction.
- Outbox transaction.
- Saga/workflow with durable steps.
- No transaction because the operation is read-only or external-only.

Do not wrap slow external calls inside a database transaction unless the tradeoff is explicit.

## Coroutine And Blocking Boundaries

Kotlin coroutines make asynchronous code readable; they do not automatically make blocking dependencies non-blocking.

- Keep structured concurrency: child work should be tied to a parent request/workflow scope.
- Avoid `GlobalScope` for request or workflow work.
- Use `withTimeout`/deadline propagation for bounded external calls.
- Use the right dispatcher for blocking calls, or keep the service blocking and scale it as a blocking service.
- Do not mix blocking JPA/JDBC with WebFlux/Ktor coroutine paths without naming the dispatcher and pool impact.

## External Clients And Workers

For outbound HTTP, queue, or worker flows:

- Define a port/interface at the application boundary.
- Normalize provider-specific errors in the adapter.
- Set timeouts.
- Classify retryable versus permanent failures.
- Use idempotency keys or deduplication for retryable writes.
- Consider an outbox or durable queue for work that must survive process restarts.

## API Contract Defaults

- Validate request body, route params, query params, headers, and auth principal at the edge.
- Treat client-side validation as UX, not trust.
- Return stable error envelopes when the service already has one.
- Use cursor/range pagination for growing collections.
- Use deterministic ordering for paginated reads.
- Keep public response fields intentional; do not serialize persistence entities directly by default.

## Review Checklist

- Are Kotlin nullability and domain absence aligned?
- Are framework annotations contained to framework layers?
- Are transactions located around service workflows?
- Are blocking calls isolated or intentionally blocking?
- Are request validation and domain validation both represented?
- Are expected business errors visible and mapped?
- Are migrations and rollouts covered when storage changes?
- Are tests proving the boundary that can actually break?
