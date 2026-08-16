# Kotlin Backend Security And Resilience

Use this reference when work touches validation, auth, external calls, retries, idempotency, coroutine cancellation, or failure behavior.

## Trust Boundaries

Treat all inbound data as untrusted:

- JSON body.
- route parameters.
- query parameters.
- headers.
- cookies.
- JWT/session claims.
- message payloads.
- environment variables.
- data loaded from external APIs.

Validate transport shape at the edge. Re-check business invariants in application/domain code.

## Authentication And Authorization

Spring Boot:

- Prefer Spring Security's Kotlin DSL when the service is Kotlin-first.
- Keep security configuration explicit and tested.
- Use method security only when the team has a clear convention for where authorization lives.
- Test allowed, denied, unauthenticated, expired, and malformed-token paths.

Ktor:

- Install authentication plugins deliberately.
- Keep principal extraction and authorization decisions explicit.
- Test route behavior with missing, malformed, valid, and insufficient credentials.

Do not ship auth changes without negative-path tests.

## Passwords, Tokens, And Sessions

- Use memory-hard password hashing such as Argon2id or bcrypt with current parameters approved by the platform/security team.
- Never log passwords, tokens, session ids, reset tokens, or raw Authorization headers.
- Store reset tokens hashed when feasible.
- Rate-limit login, reset, and verification endpoints.
- Avoid account enumeration in public error messages.
- Set secure cookie flags for cookie sessions: HttpOnly, Secure, SameSite, domain/path scope, and appropriate lifetime.

## CSRF And Browser Context

CSRF depends on client context:

- Cookie-authenticated browser flows usually need CSRF protection.
- Bearer-token APIs used by non-browser clients usually have different tradeoffs.
- Do not disable CSRF in Spring Security without naming why the client/auth model makes that acceptable.

## Input Validation

- Parse JSON into DTOs at the transport boundary.
- Validate simple structural constraints with framework validation.
- Convert DTOs into domain commands after authentication and normalization.
- Validate cross-field and stateful invariants in application/domain code.
- Return stable error responses without leaking stack traces or internal class names.

## Coroutine Resilience

Coroutines require explicit failure and cancellation design:

- Preserve structured concurrency.
- Propagate cancellation from request/workflow scope.
- Use supervisor scopes only when sibling failure isolation is intended.
- Set timeout budgets on external calls.
- Do not swallow `CancellationException`.
- Do not wrap every coroutine in broad `catch (Throwable)` without rethrowing cancellation.

## Blocking And Dispatchers

- Treat blocking JPA/JDBC/file calls as blocking even inside suspend functions.
- Use an appropriate dispatcher or dedicated executor when blocking calls are unavoidable in coroutine flows.
- Avoid starving event-loop threads with blocking work.
- Prefer a simple blocking architecture over a fake non-blocking architecture when dependencies are blocking.

## Retries

Retries are safe only when bounded and classified:

- Retry transient infrastructure failures.
- Do not retry validation failures, auth failures, or deterministic domain errors.
- Use backoff and jitter for remote systems.
- Respect timeout/deadline budgets.
- Record retry attempts in logs/metrics.
- Combine retryable writes with idempotency keys, deduplication, or transactional outbox patterns.

## Idempotency

Use idempotency for:

- payment-like writes.
- webhook receivers.
- queue consumers.
- external API callbacks.
- user actions that clients may retry.

Store idempotency records transactionally with the state change when possible. Define response replay behavior for duplicate requests.

## External API Clients

For each provider client:

- Define a port/interface.
- Configure connect/read/total timeouts.
- Normalize provider errors.
- Preserve correlation ids.
- Hide credentials from logs.
- Test success, timeout, 4xx, 5xx, malformed response, and retry behavior.

## Background Work

Use durable background processing when work must survive process restart or outlive the request. Avoid launching fire-and-forget coroutines from request handlers for critical work.

For workers:

- Make handlers idempotent.
- Bound concurrency.
- Classify retryable failures.
- Use dead-letter or parking behavior.
- Emit metrics for success, failure, retry, lag, and processing time.

## Security And Resilience Review Checklist

- Are all inbound boundaries parsed and validated?
- Are expected domain failures distinct from infrastructure failures?
- Are auth negative paths tested?
- Are secrets redacted?
- Are retries bounded and idempotent?
- Are external calls timed out?
- Is cancellation preserved?
- Is blocking work isolated or intentionally blocking?
- Is background work durable if it must be durable?
