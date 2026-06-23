# Reference Map

Use this file first to route the task before loading heavier Kotlin backend references.

## 1) Mode To Reference Routing

| mode | use when | read |
| --- | --- | --- |
| `Spec Mode` | Feature request is vague, acceptance criteria are missing, or success is not measurable | `kotlin-backend-playbook.md`, then relevant testing sections |
| `Spring Boot Mode` | Work touches controllers, services, repositories, config, Spring Security, MVC/WebFlux, or Spring Data | `kotlin-spring-ktor-idioms.md`, Spring sections first |
| `Ktor Mode` | Work touches Ktor routes, plugins, serialization, status pages, auth, or testApplication | `kotlin-spring-ktor-idioms.md`, Ktor sections first |
| `Persistence Mode` | Work touches JPA, Spring Data, Exposed, jOOQ, migrations, transactions, or query design | `kotlin-backend-playbook.md`, then `kotlin-backend-runtime-and-ops.md` |
| `Coroutine Mode` | Work touches suspend functions, Flow, dispatcher choice, cancellation, or blocking isolation | `kotlin-backend-playbook.md`, then `kotlin-backend-security-and-resilience.md` |
| `Security Mode` | Work touches auth, sessions, JWT/OAuth2, CSRF, passwords, validation, or reset flows | `kotlin-backend-security-and-resilience.md` |
| `Resilience Mode` | Work touches retries, idempotency, external APIs, timeout behavior, workers, or transactions | `kotlin-backend-security-and-resilience.md`, then runtime/ops |
| `Operations Mode` | Work touches config, profiles, secrets, logging, metrics, health checks, CI, Docker, or deployment | `kotlin-backend-runtime-and-ops.md` |
| `Review Mode` | Task is a review, modernization pass, or production-hardening pass | security/resilience, runtime/ops, testing, then playbook |

## 2) Common Read Orders

### New Kotlin Spring Boot Endpoint

1. `kotlin-backend-playbook.md`
2. Spring sections of `kotlin-spring-ktor-idioms.md`
3. `kotlin-backend-testing-and-fixtures.md`
4. Security or runtime references only if the feature touches those surfaces

### New Ktor Service Or Route

1. `kotlin-backend-playbook.md`
2. Ktor sections of `kotlin-spring-ktor-idioms.md`
3. `kotlin-backend-testing-and-fixtures.md`
4. Security or runtime references as needed

### Persistence Or Migration Work

1. Persistence sections of `kotlin-backend-playbook.md`
2. `kotlin-backend-testing-and-fixtures.md`
3. Migration and rollout sections of `kotlin-backend-runtime-and-ops.md`
4. Transaction and idempotency sections of `kotlin-backend-security-and-resilience.md`

### External API, Queue, Or Worker Flow

1. Coroutine and external-client sections of `kotlin-backend-playbook.md`
2. `kotlin-backend-security-and-resilience.md`
3. `kotlin-backend-runtime-and-ops.md`
4. Contract and integration testing sections of `kotlin-backend-testing-and-fixtures.md`

### Production Readiness Review

1. `kotlin-backend-security-and-resilience.md`
2. `kotlin-backend-runtime-and-ops.md`
3. `kotlin-backend-testing-and-fixtures.md`
4. `kotlin-backend-playbook.md`

## 3) Source Provenance

Use `sources-and-research-brief.md` when updating the doctrine or checking whether a rule is sourced, inferred from multiple sources, or repo-local synthesis.
