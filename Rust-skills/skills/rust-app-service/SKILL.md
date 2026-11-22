---
name: rust-app-service
description: Self-contained guide for application Rust - HTTP services, CRUD back ends, workers and queue consumers (Axum, Actix, sqlx, Diesel, Tower, Tokio). Use when the task adds or changes an endpoint, handler, extractor, middleware, database query, migration, transaction, background job, message consumer, outbound API client, configuration, authentication, sessions, idempotency, retries, health checks or tracing in a service. Not for parsers, storage engines, performance-critical kernels, unsafe code, published libraries, or desktop apps.
---

# Rust for application services

This is the Rust of web back ends and CRUD services: handlers, a database, a few remote
systems, workers and queues. Its defects are rarely about memory or speed. They are a
write that happened twice, a transaction held across a remote call, a migration that broke
the running version, a secret in a log, an endpoint that forgot its authorisation check.

The costly mistake is to treat a service as a generic library: sessions, migrations and
idempotency then go unexamined. Framework details differ between versions, so write
against the versions in `Cargo.lock`.

## When to use this skill

- **Use it when** the change touches an HTTP service or its workers: routes, handlers, extractors, middleware, queries, migrations, jobs, consumers, outbound clients, configuration, auth.
- **Signals:** `axum`, `actix-web`, `tower`, `sqlx`, `diesel`, `sea-orm`, `tokio` with a listener, a `migrations/` directory, queue or broker clients.
- **Skip it for** parsers, indexers, storage engines and hot loops (the infra skill), published crates (the library skill), unsafe and FFI, command-line tools, and Tauri applications.
- **It is complete on its own.** The Rust essentials, the gate commands and the definition of done are at the end, and they apply to every task here.

## The defaults, in priority order

If unsure what matters most, work down the list.

1. **Parse at the edge.** A request becomes a DTO, the DTO becomes a domain type through a fallible conversion, and only domain types travel inward. A DTO that deserialised is well-formed, not valid.
2. **One error family maps to responses.** Handlers return `Result<_, ApiError>`. Internal detail is logged with the correlation id and never returned. No `unwrap()` or `expect()` on a path a request can reach.
3. **Know what a crash leaves behind.** No database transaction is held across a remote call. A side effect that must follow a commit goes through an outbox. Every mutation a client may retry has an idempotency definition.
4. **Authentication is a type, authorisation is a check.** A protected handler takes the verified extractor in its signature, then checks whether this user may touch this resource. New routes are protected until someone decides otherwise.
5. **Configuration is parsed once at start-up** into typed settings and fails the boot when wrong. Secrets are wrapped in a redacting type.
6. **Every listener and every outbound call is bounded:** request timeout, body limit, concurrency limit, a timeout on each remote call, an acquire timeout on the pool.
7. **Never block the runtime, never hold a lock or a pooled connection across a slow await.**
8. **A schema change is a rollout:** expand, deploy code that handles both shapes, backfill, tighten.
9. **Test over the wire against a real, migrated database,** with mock servers for outbound calls.
10. **Make each request explainable:** one correlation id, structured spans, readiness separate from liveness, counters for errors, timeouts, retries and saturation.

**How this kind of Rust differs from systems Rust.** These are the answers for a service,
stated flatly:

- **Clone freely.** Clarity beats allocation counts. An extra `String` or `Arc::clone` per request is noise beside one database round trip.
- **`anyhow` with context is fine inside the application.** Use typed errors where something branches on them: the API error family, domain errors that map to a status, the failure classes of a remote client.
- **No `unsafe`, no hand-written lock-free code, no custom data structures.** If one seems necessary, the design is wrong or the code belongs in a library with its own review.
- **Use the well-known crate** for routing, SQL, serialisation, tracing, secrets and time, at the locked version.
- **One concrete implementation.** Add a trait only at a boundary a test fakes today.
- **Performance work means pool reuse, transaction scope, inline-or-worker placement and fan-out,** in that order, before any micro-optimisation.

## Start from the risk

**Name the task's dominant risk before designing.** It is often not the ticket's topic.

| Risk | Typical task | What must exist before code |
|---|---|---|
| Ambiguity | New endpoint, vague request | Testable requirements, including each invalid-input case |
| Sequencing | Schema change, deploy-order change | A rollout plan with a rollback answer per step |
| Security | Auth, sessions, credentials, reset flows | Storage, failure behaviour, what an attacker learns from each response |
| Resilience | External calls, retries, workers | Failure classes, idempotency definition, the state left by a crash |
| Operations | Configuration, tracing, health, CI | Boot behaviour, what is observable, what is reversible |

- A migration's topic is schema; its risk is rollout order. A retry question is about idempotency, not about the HTTP client.
- **Re-classify mid-task.** When delivery work uncovers an auth or durability question, stop and apply that risk's rules. Consulted after the code is written, they arrive too late.
- **A task that will not classify is two tasks.** Split a migration-plus-worker ticket.
- **One service slice per change:** an endpoint or a worker, with its requirements and tests. An endpoint, its schema change and a new worker loop are three changes. Trivial read endpoints that share every boundary may be batched.
- **Version-specific crate questions are answered from `Cargo.lock` and the changelog,** not from memory. Web framework APIs change between versions.

## Layers give every failure an owner

| Layer | Owns |
|---|---|
| Transport (extractors, DTOs) | Parsing, shape and size limits, authentication of the request |
| Handler | Orchestration, mapping domain errors to responses |
| Domain types | Invariants; values that cannot be invalid |
| Persistence | Queries, transactions |
| Typed clients | Remote calls: timeouts, retries, failure classification |

- Walk a request end to end and name the owner of each step. A step with no owner is a boundary the design still owes.
- **Transport validation is not domain validation.** A DTO that deserialised is well-formed, not valid. Convert it to domain types at the edge, and pass only those inward.
- **Pools and clients are built once,** held in application state and wired in one place. A client constructed per request pays connection set-up on every call and defeats pooling.
- The layers are the rule. The crates are replaceable.

**Reject on sight in a back-end review:**

- business rules inside extractor or middleware glue;
- SQL or client construction inside handlers;
- unchecked strings travelling through the core;
- a multi-write workflow with no named transaction owner;
- a transaction held open across a remote call;
- a mutation with no idempotency definition that clients will retry;
- secrets in logs, errors or panic messages;
- environment variables read outside the settings module.

**When refactoring an existing service, fix in this order:** layer separation, edge
validation, transaction ownership, typed clients, then the worker split. Do not tune
connection pools while unchecked strings still travel through the core. Validation and
transaction ownership come first because their failures corrupt data.

## A service skeleton

```rust
#[derive(Clone)]
pub struct AppState {
    db: Database,
    settings: Arc<Settings>,
}

pub fn build_router(state: AppState) -> Router {
    Router::new()
        .route("/health/live", get(|| async { StatusCode::OK }))
        .route("/health/ready", get(readiness))
        .route("/api/users", post(create_user))
        .route("/api/users/{id}", get(get_user))
        .layer(
            ServiceBuilder::new()
                .layer(TraceLayer::new_for_http())
                .layer(TimeoutLayer::new(state.settings.request_timeout))
                .layer(DefaultBodyLimit::max(state.settings.max_body_bytes))
                .layer(cors_layer(&state.settings)),
        )
        .with_state(state)
}

async fn create_user(
    State(state): State<AppState>,
    Json(request): Json<CreateUserRequest>,
) -> Result<(StatusCode, Json<UserResponse>), ApiError> {
    let new_user = NewUser::try_from(request)?; // DTO to domain type; validation lives here
    let user = state.db.insert_user(&new_user).await?;
    Ok((StatusCode::CREATED, Json(UserResponse::from(user))))
}

async fn get_user(
    State(state): State<AppState>,
    Path(id): Path<UserId>,
) -> Result<Json<UserResponse>, ApiError> {
    let user = state.db.find_user(id).await?.ok_or(ApiError::NotFound)?;
    Ok(Json(UserResponse::from(user)))
}
```

- **CORS is an allow-list from settings.** `CorsLayer::permissive()` is for local development only; combined with credentials it lets any site act as the user.
- **The router is built by a function that takes state,** so a test can build the same router against a test database.
- **Request and response types are separate from the domain type.** `User` may hold a password hash; `UserResponse` cannot.
- A create returns 201; an absent resource returns 404 through the error type, not through an `Option` serialised as `null`.
- Timeouts, body limits and state are set from typed settings, not literals in the router.
- Path syntax, layer order and extractor rules differ between framework versions. Write against the version in `Cargo.lock`.

## Service building blocks

**One error family implements the response contract.** At the service boundary, one
implementation maps each variant to a status and a serialised body. Handlers never
hand-build JSON errors.

```rust
impl IntoResponse for ApiError {
    fn into_response(self) -> Response {
        let (status, code) = match &self {
            ApiError::NotFound { .. } => (StatusCode::NOT_FOUND, "not_found"),
            ApiError::Invalid { .. } => (StatusCode::UNPROCESSABLE_ENTITY, "invalid"),
            ApiError::Conflict { .. } => (StatusCode::CONFLICT, "conflict"),
            ApiError::Internal(source) => {
                tracing::error!(error = ?source, "internal error");
                (StatusCode::INTERNAL_SERVER_ERROR, "internal")
            }
        };
        (status, Json(ErrorBody { code, message: self.public_message() })).into_response()
    }
}
```

- **Internal detail is logged, not returned.** The client gets a stable code and a safe message; the cause, the SQL and the stack stay on the server, joined by the correlation id.
- A new variant gets its message, code and status in the same change. Narrow cases first, catch-all last.
- Core crates do not implement HTTP traits. The mapping lives in the service crate.

**A failure table for each route.** For every dependency a handler calls, one row: the
failure (timeout, refused, malformed reply), the status and body the client receives, what
is logged or counted, and whether the call is retried. A dependency with no row has
undecided behaviour. Each row has a test that injects the failure.

**Required and enhancing dependencies.** A required dependency fails the request. An
enhancing one degrades, with a warning and a result tagged by the path that produced it.

```rust
let primary = primary_result.map_err(SearchError::Primary)?;
let enriched = match secondary_result {
    Ok(extra) => merge(primary, extra, Source::Both),
    Err(error) => {
        tracing::warn!(%error, "secondary search failed; serving primary only");
        metrics::counter!("search_degraded_total").increment(1);
        tag(primary, Source::PrimaryOnly)
    }
};
```

- **Count each path.** A silent fallback hides an outage for as long as the primary holds.
- *No degradation* where audit or exactness requires every back end.

**One wrapper around outbound clients.** Correlation ids, trace propagation, timeouts, token
refresh and retry logging live in one wrapper, so every operation gets them.

- It maps transport status to domain errors with context from the call site: service, method and the most specific resource name (a key, a path, a secret's name and never its value). `NotFound` for a known key becomes `KeyNotFound { key }`; the rest become a generic call error carrying the code.
- Endpoint methods are domain-specific and return domain types. Status handling, decoding and URL building sit in one helper beneath them.
- It does not retry non-idempotent writes. Generated clients (gRPC, OpenAPI) are always called through it.

**Background work after the response.** Before offering a "run this later" helper, define
how tasks are registered, observed, drained and reported.

- Track them (`JoinSet`, `TaskTracker`) and await what is pending at shutdown, with a deadline. One task's failure is recorded and never blocks the drain.
- **This is not a durable queue.** Work that must survive process death goes through the outbox or a job table.

**Smaller rules.**

- **Start a new service with one thin slice** through every layer: typed input, one domain function, persistence, error mapping, a spawned-app test of success and of one failure. It settles the boundaries and the harness while they are cheap to change.
- **A module of database operations states its transaction contract:** each operation runs inside the caller's transaction; a failure that depends on current state is an error; never panic on a path user input can reach.
- **Per-tenant services** share expensive resources and cache one facade per tenant in a registry with single creation under concurrency. Tenant identity travels in request-scoped state and is validated before anything is created. *Not when* tenants need separate processes or credentials.
- **Size results for the consumer and never clip silently.** One function caps every list-returning operation and returns what was cut and how to get the next page.
- **Tool and RPC schemas are checked on the server** before dispatch, whatever the client claims to have read. One registry lists every operation; a test proves each has an implementation.
- **Pipelined protocols** enqueue a handler for each expected reply as the request is sent, and pop one per reply. A reply with no handler waiting is a protocol error. Out-of-order replies need correlation ids instead.
- **Canonical ids come from one module** (Unicode normalisation, case, separators) that every producer calls. Normalisation can collide, so pair the id with its source when uniqueness matters.
- **One function builds the invariant part of an external command,** with the variable part passed in. A logged command line can expose credentials.
- **Turning on autoscaling or rolling deploys makes the service multi-instance that day,** not at the first scale-out. Stepwise migrations become mandatory in the same change.

## Routes, authentication and readiness

**The verified type is the only way into a protected handler.** Split authentication into
an extractor that parses and one that verifies.

```rust
pub struct ValidCredentials(pub UserId);

impl FromRequestParts<Arc<App>> for ValidCredentials {
    type Rejection = StatusCode;

    async fn from_request_parts(parts: &mut Parts, state: &Arc<App>) -> Result<Self, StatusCode> {
        // `Unverified` only parses the header: malformed is 400.
        let unverified = Unverified::from_request_parts(parts, state).await?;
        state
            .auth
            .check_credentials(&unverified)
            .await
            .map(ValidCredentials)
            .ok_or(StatusCode::UNAUTHORIZED)
    }
}
```

- A protected handler takes `ValidCredentials` in its signature, so forgetting the check is a compile error, not a missing middleware line.
- **Authentication is not authorisation.** The extractor proves who; the handler, in its first lines, checks whether this user may touch this resource. 401 for no valid identity, 403 for a valid one without permission, and 404 where even existence must not leak.
- The rejection is a bare status: no detail about why verification failed.
- Multi-step flows (redirects, sessions) need middleware; an extractor does not fit them.

**Route layout.**

- One builder registers every route; each endpoint lives in its own handler module; one error type maps to responses. Split the route file by group once it stops being scannable.
- **Every path segment and query value built from data is percent-encoded.** Use the URL type's segment API, not `format!`.
- **Degraded behaviour for each downstream call is decided per method** and written beside the client: fail fast, fallback value, retry, or enqueue. Never a no-op by default: a fallback that only logs loses the work for good unless something reconciles it.
- **A handler offering buffered and streamed responses** runs one parse, validate and authorise path and branches on output mode last. An error after the first chunk cannot become a status code, so errors after headers are sent get their own tests.
- **Version negotiation is an explicit parameter** from route to domain (requested in, actual out and echoed in a header), never ambient state. When an option can arrive by query string or body, document and test the precedence.

**Readiness that depends on an expensive condition is a flag that flips once.** The probe's
fast path is one atomic load; the expensive check runs in a background task that the probe
wakes.

```rust
pub async fn check_ready(&self) -> bool {
    if self.ready.load(Ordering::Acquire) {
        return true;
    }
    self.wake_checker.notify_one();
    tokio::time::timeout(PROBE_TIMEOUT, self.wait_ready()).await.is_ok()
}

fn set_ready(&self) {
    self.ready.store(true, Ordering::Release);
    self.ready_signal.notify_waiters();
}
```

- The waiter registers its `Notified` future before re-checking the flag, or a `notify_waiters` between the check and the wait is lost.
- Once ready it stays ready. Later regressions belong to a separate health check; decide for each new criterion which of the two it is.
- Tell operators what "ready" means.

**Wire payloads become small internal types at the boundary.** JSON-RPC, server-sent events
and webhooks are framed and parsed by a real parser, then converted to a minimal internal
type with explicit defaults.

- **A malformed payload is an error, never an empty list.** "No results" and "could not parse" are different outcomes.

**One wrapper retries a transactional callback.** It owns begin, commit and rollback, the
backoff (initial delay, multiplier, jitter), an overall deadline, cancellation, and which
errors are retryable (serialisation failure, deadlock). Non-retryable errors propagate at
once.

- **The callback may run more than once,** and its documentation says so. It contains database work only: no emails, no remote calls, no mutation of outside state.

**Smaller rules.**

- **A logical write spanning several tables** is turned by one function into an ordered list of statements, parent first. A separate executor applies the list in one transaction. Parameters are bound, never formatted into SQL.
- **Recursive SQL suits graph traversal** when the graph is relational and the result joins back to relational data. Review the base case, the recursive case, the termination or depth cap, and the path reconstruction separately. A reusable path service with complex policy belongs in application code that can be unit-tested.
- **Graph and path results are parsed by the grammar,** then hydrated through an identity cache keyed by entity id, so a vertex repeated in a path is one object. Never split such values by hand.

## Database access

```rust
#[derive(Clone)]
pub struct Database {
    pool: PgPool,
}

impl Database {
    pub async fn connect(settings: &DatabaseSettings) -> Result<Self, sqlx::Error> {
        let pool = PgPoolOptions::new()
            .max_connections(settings.max_connections)
            .acquire_timeout(settings.acquire_timeout)
            .connect_with(settings.connect_options())
            .await?;
        Ok(Self { pool })
    }

    pub async fn find_user(&self, id: UserId) -> Result<Option<User>, sqlx::Error> {
        sqlx::query_as!(User, "SELECT id, name, email FROM users WHERE id = $1", id.0)
            .fetch_optional(&self.pool)
            .await
    }
}
```

- **Size the pool deliberately.** Instances times `max_connections` must fit under the database's connection limit, with room for migrations and operators. Set an acquire timeout, so pool exhaustion surfaces as an error, not as requests that hang.
- **A pooled connection held is a connection denied to others.** Do not hold one across a remote call, a long computation or a slow client.
- **Compile-time checked queries** (`query!`, `query_as!`) verify SQL and types against a real schema. They need a database at build time, or prepared metadata (`cargo sqlx prepare`) committed and checked for staleness in CI. *Use the unchecked functions* for SQL assembled at run time, with bound values.
- **Where migrations run is a deployment decision.** Running them at start-up is fine for one instance. With several replicas or stepwise rollouts, run them as a separate step: replicas otherwise race, and a tightening migration applies before old code is gone.
- `fetch_optional` for zero-or-one, `fetch_one` only when absence is a bug, and a `LIMIT` on anything a user can make large.
- Map database errors to domain errors in this layer: a unique-constraint violation becomes `Conflict`, not a 500.

**A lazy result stream owns its connection.** Bundle the stream with the resource it reads
from, so a caller cannot consume rows after the transport is gone.

```rust
pub struct DetachedRowStream {
    stream: RowStream,
    connection: ManagedConnection,
}

impl DetachedRowStream {
    pub async fn next(&mut self) -> Result<Option<Row>> {
        self.stream.next(&mut self.connection).await
    }

    pub async fn finish(mut self) -> Result<RunSummary> {
        self.stream.finish(&mut self.connection).await
    }
}
```

- An open stream holds a pooled connection, so a slow consumer can starve the pool. Bound it with a timeout, or buffer fully when results are small.
- Test partial consumption followed by drop, and `finish()`.

**A query macro may read like `format!` only if every value becomes a bound parameter.**
Test both the rendered text and the parameter map. Identifiers and dynamic clauses never go
through value parameters; they have their own validation.

## Transactions, remote calls and retries

**Saving intent and calling a remote system in one block is correct until one half fails.**
The remote call succeeds and the commit does not, or the reverse.

- **Never hold a database transaction open across a remote call.** Remote slowness becomes pool exhaustion.
- **Use an outbox:** in one transaction, commit the state change and a row describing the side effect. A worker performs the side effect with an idempotency key and marks the row done. A crash at any point leaves a state the worker can resume.

```rust
let mut tx = pool.begin().await?;
orders::mark_paid(&mut tx, order_id).await?;
outbox::enqueue(&mut tx, OutboxMessage::SendReceipt { order_id }).await?;
tx.commit().await?;
// The worker delivers SendReceipt at least once; the receiver deduplicates on order_id.
```

- For every multi-step workflow, write down the state left by a crash after each step, and what resumes or compensates it.

**Classify remote failures before choosing a retry policy.**

| Failure | Default policy |
|---|---|
| Client error (4xx other than 408, 429) | Fail fast. A retry burns quota and cannot succeed |
| 429, 503 with `Retry-After` | Retry after the stated delay, within a budget |
| Server error, transport failure | Retry with backoff and jitter, if idempotent |
| Timeout | Outcome unknown: retry only with an idempotency key |
| Malformed response | Fail and surface to an operator; do not retry blindly |

- **A retry is safe only under an idempotency definition:** the key, what counts as the same request, what is replayed to a duplicate, and what happens when two arrive at once. A reused key with a different body is an error, not a replay.
- No blanket retry count. Retries that must outlive the request go behind a worker, and unbounded worker retries need a dead-letter state and an alert.
- Test each failure class with simulated faults, and assert that no side effect ran twice.

### Inline or worker

**Keep work inline in the request until one of these holds:** retries must outlive the
request; the call fans out to unreliable systems; the client would wait longer than it
reasonably keeps a connection open.

- A slow remote call kept inline holds connections open and turns client retries into duplicate side effects. Keeping it inline needs a stated reason.
- **A queue needs a durability reason.** A worker hiding a simple request flow adds a second failure domain for nothing.
- When you split, define four things: what the endpoint commits, what the worker consumes, what "already processed" means, and what an operator can observe.
- Re-ask as traffic grows. An inline call that was fine at ten requests a day duplicates side effects at ten thousand, though the code never changed.

### Transaction helpers, several databases and the outbox record

**A transaction helper commits only what it began.** If it joined the caller's transaction,
it neither commits nor rolls back; the outer owner does. It retries only errors classified
as retryable, rolling back first, and its closure must be safe to run more than once.

**Several databases.** Each pool is a named field or newtype
(`struct Pools { primary: PgPool, reporting: PgPool }`), each repository takes the pool it
owns, and no transaction spans pools. Two writes to two databases are a workflow with
intermediate states, not a transaction: use the outbox.

**The outbox record.**

```rust
pub struct OutboxEntry {
    pub id: Uuid,
    pub aggregate_id: Uuid,
    pub operation: OutboxOperation,
    pub payload: serde_json::Value,
    pub created_at: DateTime<Utc>,
    pub processed_at: Option<DateTime<Utc>>,
    pub attempt_count: u32,
}
```

- The relay stamps `processed_at` on success and increments `attempt_count` on failure. After a bound, the row is parked for an operator.
- Delivery is at least once: the target deduplicates on the outbox id, and the payload carries every identifier a replay needs.
- With several relay instances, claim rows with `FOR UPDATE SKIP LOCKED` or a lease. Ordering across aggregates is not guaranteed; if order per aggregate matters, process each aggregate's rows in sequence.
- Processed rows are pruned, or the table grows without bound.
- *Not when* the second effect must be synchronous.

### Retries in code

**Whether an error may be retried is a property of the error type,** decided where the error
is created, never by matching message text.

```rust
pub trait Retryable {
    /// Permanent unless a variant opts in.
    fn is_retryable(&self) -> bool {
        false
    }
}

pub struct RetryPolicy {
    pub max_attempts: NonZeroU32,
    pub base_delay: Duration,
    pub max_delay: Duration,
    pub max_total: Duration,
}

pub async fn retry<T, E, Fut>(
    policy: &RetryPolicy,
    sleeper: &impl Sleeper,
    mut op: impl FnMut() -> Fut,
) -> Result<T, E>
where
    E: Retryable,
    Fut: Future<Output = Result<T, E>>,
{
    let started = sleeper.now();
    let mut attempt = 1;
    loop {
        match op().await {
            Ok(value) => return Ok(value),
            Err(error) if !error.is_retryable() => return Err(error),
            Err(error) if attempt >= policy.max_attempts.get() => return Err(error),
            Err(error) => {
                let delay = policy.jittered_delay(attempt);
                if sleeper.now() - started + delay > policy.max_total {
                    return Err(error);
                }
                sleeper.sleep(delay).await;
                attempt += 1;
            }
        }
    }
}
```

- **Retry only idempotent operations,** or ones made idempotent with a key the server deduplicates on. Retrying a non-idempotent write duplicates it.
- **Bound attempts and total time, back off exponentially, add jitter.** Without jitter, clients that failed together retry together.
- **Default to permanent.** A wrong "retryable" turns one outage into a retry storm; a wrong "permanent" only surfaces an error.
- **Typical classification for HTTP:** retry timeouts, connection resets, 429, 502, 503 and 504; honour `Retry-After`. Do not retry 400, 401, 403, 404 or 422: the request is wrong and will stay wrong. Treat 500 as retryable only for idempotent calls.
- **Inject the clock and the sleep** (the `Sleeper` above), so tests of the retry loop run instantly and can assert the delays.
- **One layer retries.** Retries at three layers multiply: three by three by three is twenty-seven calls. Put the loop at the operation boundary; inner layers return classified errors.
- **A closure passed to a retrying helper may run more than once.** Say so in the docs. It must not move out of captured state or leave partial effects behind.
- **Retrying a stream restarts it.** Either the caller tolerates repeated partial output, or only committed chunks are passed on and the retry resumes from the last committed position.
- Stop when the caller's deadline or cancellation fires; a retry loop that outlives its request is a leak.
- When retries are exhausted, return the last error together with the attempt count, not a generic "retries exhausted".

### Resilience patterns

**Retry as a decorator.** A wrapper that implements the same trait as the backend it holds
(`struct Retrying<B> { policy: RetryPolicy, inner: B }`) keeps retry out of every call site
and every backend. Wrap reads and writes separately: reads are usually safe to repeat, writes
only when the backend deduplicates them. One policy object serves the blocking, async and
streaming entry points, so their rules cannot drift.

**A circuit breaker records exactly one outcome per admitted call.**

| State | Behaviour |
|---|---|
| Closed | Calls pass; failures are counted |
| Open | Calls are rejected at once until the cooldown ends |
| Half-open | Exactly one probe is admitted; others are rejected with a retry-after |

```rust
pub enum Outcome {
    Success,
    Failure,
    /// Says nothing about the dependency's health.
    Neutral,
}

pub struct Permit<'a> {
    breaker: &'a Breaker,
    recorded: bool,
}

impl Permit<'_> {
    pub fn record(mut self, outcome: Outcome) {
        self.recorded = true;
        self.breaker.record(outcome);
    }
}

impl Drop for Permit<'_> {
    fn drop(&mut self) {
        if !self.recorded {
            self.breaker.record(Outcome::Neutral);
        }
    }
}
```

- **Caller cancellation, a caller-side timeout and a client error (a 4xx) are neutral.** They release the probe without changing health. Counting them as failures opens the breaker because of bad requests; never recording them wedges it half-open for ever.
- The permit's `Drop` guarantees a record on every path, including a cancelled future. Call sites never touch breaker state.
- Release the breaker's lock before awaiting the wrapped call.
- "Rejected because open" is its own error variant, distinct from the upstream failure, so callers and dashboards can tell them apart.
- Inject the clock. *Use for* remote dependencies that fail for a while; not for cheap local operations, where it only adds a failure mode.

**Partial failure across two systems is reported item by item.** An operation that changes
two durable systems (object storage and a metadata table) returns which items succeeded, which
failed on each side, and each side's error. One opaque error hides which system needs repair.

```rust
#[derive(Debug, thiserror::Error)]
#[error("deleted {} items; {} failed in storage, {} in metadata",
    .deleted.len(), .storage_failed.len(), .metadata_failed.len())]
pub struct DeleteError {
    pub deleted: Vec<ItemId>,
    pub storage_failed: Vec<(ItemId, StorageError)>,
    pub metadata_failed: Vec<(ItemId, MetadataError)>,
}
```

- Change the second system only for the items that succeeded in the first.
- Choose the order so that the leftover state after a crash is the harmless one: an orphaned blob can be garbage-collected, a metadata row pointing at nothing is a user-visible error.
- The same shape suits any batch API: return per-item results, not the first error.

## Configuration and secrets

- **Parse configuration once at start-up into typed settings and fail fast.** A missing or invalid value stops the process at boot with a specific error. No `std::env::var` scattered through handlers, and no flag read lazily at first use.
- Settings hold types, not raw strings: `Url`, `Duration`, `SocketAddr`, validated newtypes.
- **Unknown keys fail the boot,** so a typo is caught at deploy. Strict-in-production and tolerant-in-development are configuration layers, not code branches.
- Configuration is supplied to the image, never baked into it.
- **Each secret field is wrapped in a redacting type** (`secrecy::SecretString` or equivalent). A derived `Debug` on the settings struct otherwise prints every secret the first time anything logs it, and a hand-written `Debug` breaks when the next field is added.
- Test it: boot with deliberately broken configuration and expect a loud, specific failure.

**Layered configuration:** defaults, then a file, then the environment, deserialised into
one typed struct in one place.

```rust
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
struct Settings {
    database_url: SecretString,
    workers: usize,
}

let settings: Settings = config::Config::builder()
    .set_default("workers", 4)?
    .add_source(config::File::with_name("config").required(false))
    .add_source(config::Environment::with_prefix("APP").separator("__"))
    .build()?
    .try_deserialize()?;
```

- Document the precedence. A prefix keeps unrelated environment variables out.
- Each option has one parser, one default and one range check, applied at this boundary. Test a wrong type and an out-of-range value.
- A `.env` file is a development convenience. It is not loaded in production and never committed with real secrets.

### Settings in practice

**User-edited configuration reports typos with their path.** Collect unknown keys with the
full path, and make a type error name the field.

```rust
let mut unknown = Vec::new();
let deserializer = serde_ignored::Deserializer::new(value, |path| unknown.push(path.to_string()));
let settings: Settings = serde_path_to_error::deserialize(deserializer)?; // error names the path
if !unknown.is_empty() {
    return Err(ConfigError::UnknownKeys(unknown));
}
```

- *Not when* a file written for a newer version must still load. Then warn about unknown keys and keep going.

**A setting is a typed key** carrying its name, description, default and parser, read
through one getter that applies precedence: explicit value, environment, default.

```rust
pub struct Setting<T> {
    pub key: &'static str,
    pub description: &'static str,
    pub default: fn() -> T,
    pub parse: fn(&str) -> Result<T, SettingError>,
}
```

- **A value that fails to parse is an error naming the key and the value.** Falling back to the default silently means the operator's setting is ignored and nobody knows.
- The one tolerable exception is a pure tuning knob, and even that logs a warning.

**A knob read on a hot path is parsed once** into a `OnceLock` or `LazyLock`. Put the
parsing in a pure function that tests call directly, since the cell cannot be reset.

```rust
fn parse_budget(raw: Option<&str>) -> usize {
    raw.map(str::trim)
        .and_then(|text| text.parse::<usize>().ok())
        .filter(|budget| *budget > 0)
        .unwrap_or(DEFAULT_BUDGET)
}
```

- **Tests do not mutate the process environment.** `std::env::set_var` is `unsafe` from edition 2024 and races with other test threads. Pass the value in.
- Not for configuration that must change while the process runs.

**Ambient state.**

- **Avoid thread-local context in async code;** a task moves between threads. Pass the handle, or use `tokio::task_local!`.
- **A temporary override restores the exact previous value in `Drop`,** not a default, so nested overrides unwind correctly. Offer it as one function taking a closure, and test nesting.

**External formats with several versions.** Detect the version once (an unknown version is
an error listing what was seen), convert each version to one internal form at the boundary,
and keep the raw input for audit. Everything downstream is version-agnostic; a new dialect
is a new converter.

- The same applies to files: probe at the edge (magic bytes), convert legacy formats once. A missing file, an unsupported format and a malformed one are three different errors.
- **A loader that writes a converted copy says so in its signature.** A caller expecting a read-only load must not find new files.

**A relative path in a configuration file is relative to that file,** not to the working
directory. The single load function records the file's directory, and every path field is
read through a resolver.

```rust
impl AppConfig {
    pub fn load(path: &Path) -> Result<Self, ConfigError> {
        let mut config: AppConfig = parse(&fs::read_to_string(path)?)?;
        config.base_dir = path.parent().unwrap_or(Path::new(".")).to_path_buf();
        Ok(config)
    }

    pub fn auth_env_file(&self) -> Option<PathBuf> {
        let path = Path::new(self.auth.env_file.as_deref()?);
        Some(if path.is_absolute() { path.to_path_buf() } else { self.base_dir.join(path) })
    }
}
```

- `base_dir` is private and skipped by serde. Do not derive `Default` on such a type: an empty base directory resolves silently against the working directory.

## Choosing components

**Choosing components.** Pick on the property you need, and measure the rest.

| Need | Options | Watch for |
|---|---|---|
| Relational queries | `sqlx` (checked SQL), Diesel (typed query builder, generated `schema.rs` kept in sync), SeaORM | Async or sync; build-time database access |
| Embedded key-value | RocksDB (write-heavy, needs tuning, C++ build), LMDB (memory-mapped, fast reads, one writer), `redb` (pure Rust) | Space and write amplification; maintenance status of the crate |
| Local coordination | SQLite in WAL mode with a `busy_timeout` | One host only |
| Cache, ephemeral state | Redis through a pool | Timeouts; connections held across awaits |
| Simple pub/sub | NATS; JetStream for at-least-once | Ack waits, redelivery |
| Partitioned log | Kafka (`rdkafka`) | Rebalances, commit policy, C library build |
| Search | The official OpenSearch or Elasticsearch client | 429 with backoff; bulk requests chunked |
| Compact binary payloads | MessagePack (`rmp-serde`), Protobuf (`prost`) | Size caps; a version field |

- Check a crate's maintenance and the client library's current API before adopting it. Examples in old guides often use deprecated clients.

## Queues, payloads and local state

**Message consumers.**

- **Assume at-least-once.** Handlers are idempotent, with a dedupe key. Exactly-once is not available end to end.
- **Acknowledge or commit after processing,** not before. Committing first turns a crash into a lost message.
- **A consume loop handles its errors.** `while let Some(Ok(message)) = stream.next().await` exits silently on the first error and the consumer stops. Match on the error: log, back off and continue, or fail loudly.
- **A message that always fails goes to a dead-letter destination** after a bounded number of attempts. Otherwise it blocks its partition forever.
- Bound in-flight work, and size ack deadlines above the worst handler time.
- Choose manual or automatic offset commit explicitly, and handle rebalances: work in flight for a revoked partition may be redone elsewhere.

```rust
loop {
    match consumer.recv().await {
        Ok(message) => {
            if let Err(error) = handle(&message).await {
                dead_letter_or_retry(&message, error).await?;
            }
            consumer.commit_message(&message, CommitMode::Async)?;
        }
        Err(error) => {
            tracing::warn!(%error, "consumer error");
            tokio::time::sleep(backoff.next_delay()).await;
        }
    }
}
```

**Pooled connections** (Redis, databases) are taken for a short operation and returned. Set
a maximum size and timeouts, and do not hold one across a long chain of awaits.

**Persisted and queued payloads.**

- **Every payload carries a format version.** The version and the old-version decode branches sit beside the serialiser, not at call sites. Keep at least one old-version fixture.
- **No raw struct bytes on disk or wire.** Write fields explicitly (`to_le_bytes`) or use a derive that guarantees a padding-free layout. Padding leaks memory and breaks across compilers.
- **Untrusted binary input is size-capped** before decoding, including nested lengths. Do not rely on map key order.
- A change to serialised state updates the encoder, decoder, size constants and tests together.

**Local state and coordination.**

- **A process id does not prove identity;** ids are reused. Store the start time with it and verify before acting on a liveness record. Reconcile and delete rows of dead processes.
- **Checkpoint before side effects.** Before asynchronous work that edits user files, write the rollback data and register the pending state. Define what happens when the checkpoint itself fails.
- **Coalesced snapshot writes** (an atomic "write queued" flag, separate locks for state and file) lose the newest progress on a crash. Fine for convenience state; wrong for audit-critical state.
- **Human- or agent-edited text that updates a store is an input format:** parse into typed records, validate, apply in one transaction, verify, and only then remove or advance the input.
- **Reload is idempotent.** Remove the entries owned by a source before registering its replacement, debounce file-watch events, and keep the old entries when a reload fails on a half-written file.
- **A shared key-value store hands out scoped handles,** so the owner of each namespace is explicit.
- **Continuation tokens and bookmarks are replaced as a set** under one lock: remove the old, add the new.

**Transaction guarantees are documented where handles are created:** a read transaction is
a snapshot that may coexist with writes; a write transaction is the single writer. Keep
read transactions short, because a long-lived reader pins old state and blocks space
reclamation. Do not wrap a whole workflow in one transaction by default.

## Schema changes are rollouts

**A schema change that alters what running code assumes ships as ordered steps,** each its
own release:

1. **Expand:** add the new shape compatibly, with no strict constraint.
2. **Deploy code that reads and writes both shapes.** This is application work, and it is routinely underestimated because the schema diff already looks finished.
3. **Backfill.**
4. **Tighten:** add the constraint; later, remove the old shape.

- **Never merge expand and tighten because the data looks clean.** During a rolling deploy, old code is still writing the old shape. A required column added in one migration is a defect.
- **Answer five questions in writing with the code:** what lands first; which code works against both shapes; when the backfill runs; when constraints tighten; what rollback still works after each step.
- **Reversibility expires step by step.** After a backfill, some changes need a forward fix. Re-answer the rollback question after every step.
- The trigger is the kind of change, not its size, and not whether a migration file was touched: a code-only change that alters rollout behaviour needs the same plan.
- Rehearse on production-shaped data. An empty database hides lock times, foreign keys and bad rows.
- **A failed migration step is never simply rerun.** Stop, assess, and start from that step's rollback answer. A failed boot or health check changed nothing durable and may be retried automatically, under a crash-loop limit.
- Do not batch two unrelated migrations into one sequence: their rollback answers become entangled.
- Any change touching the schema runs tests against a real database with migrations applied. Green unit tests over a stale schema prove nothing.

**Additive schema repair for an embedded database.** An embedded SQLite application may add
missing nullable or defaulted columns at start-up by comparing `PRAGMA table_info` with the
schema in the code.

- Identifiers come from the code, never from input.
- Type changes, backfills, index rebuilds and anything destructive stay ordered migrations, tracked by a version (`PRAGMA user_version` or a migrations table).
- Test against saved copies of old database files.

## Process, state and storage edges

**Shutdown is a process concern.** One future, passed to the framework's graceful-shutdown
hook, waits for SIGTERM or SIGINT on Unix and Ctrl-C on Windows, and logs which arrived.
Signal handling stays out of application state and handlers.

```rust
async fn shutdown_signal() {
    let ctrl_c = async { tokio::signal::ctrl_c().await.ok(); };
    #[cfg(unix)]
    let terminate = async {
        let mut signal = signal(SignalKind::terminate()).expect("install SIGTERM handler");
        signal.recv().await;
    };
    #[cfg(not(unix))]
    let terminate = std::future::pending::<()>();
    tokio::select! { _ = ctrl_c => {}, _ = terminate => {} }
}

axum::serve(listener, app).with_graceful_shutdown(shutdown_signal()).await?;
```

- Graceful shutdown has a deadline shorter than the orchestrator's kill timeout. After the server stops accepting, drain tracked background tasks, then flush telemetry.
- A container's default stop signal is SIGTERM. A service that handles only Ctrl-C is killed mid-request on every deploy.

**A library that ships routes is generic over a state capability.** It does not fix the
host's state type. It defines a small trait for what its handlers need.

```rust
pub trait HasCommandServer {
    fn command_server(&self) -> &Arc<CommandServer>;
}

pub fn create_router<S>() -> Router<S>
where
    S: HasCommandServer + Clone + Send + Sync + 'static,
{
    Router::new()
        .route("/commands", post(create_command::<S>))
        .route("/commands/{command_id}", get(get_command_status::<S>))
}
```

- The host implements the trait on its own state, and a test uses the service itself as the state. No global singleton.
- In Axum, `FromRef` gives the same result for extracting a sub-state. Inside one application, use that and skip the trait.

**Bind to port 0 and read the port back.** A worker, agent or test server binds
`127.0.0.1:0`, takes the assigned port from `local_addr`, registers it, and only then
starts accepting. Fixed ports collide across instances and parallel tests.

**Reading a request body consumes it.** A router that picks an upstream from a body field
parses the body once into a typed enum of the payloads it supports, derives the key, and
rebuilds the upstream request from that value. Forwarding the original request after
inspecting it sends an empty body. Unsupported payloads are rejected, not passed through.

**Uploads stream into storage.** Write each chunk to the storage writer, count bytes
against a limit as they arrive, and flush explicitly.

- Body-read errors and storage-write errors are separate variants: one is the client's fault.
- A failed or oversized upload removes its partial object.
- When the whole body must be validated before any write, use a size-limited extractor with a documented limit.
- Test with a body larger than one chunk, and assert the stored length and digest.

**Archives are inspected behind a size gate,** counting uncompressed size and entry count,
not the size on the wire. Before supporting extraction, add fixtures for an entry that
escapes the target directory (`../`, an absolute path, a symlink).

**Database layer.**

- **Identifiers formatted into SQL go through one validating helper;** values are always bound parameters. There is no third case.
- **One module per aggregate,** with methods named after the domain operation (`join_channel`, not `insert_row`), taking id newtypes.
- **The database layer never sends notifications.** An operation that others must hear about returns a result naming them; the caller notifies after the commit. A notification sent inside the transaction announces something that may roll back.
- **An instant is stored in a time-zone-aware column** and mapped to `DateTime<Utc>`. When migrating a zone-less column, the migration states which zone the old values were in.
- A batch write runs in one transaction; an empty batch returns early.
- Database tests use unique table or schema names, so they can run in parallel.
- **A single-process tool may keep one SQLite connection behind a mutex.** A server uses a pool. With async code, the mutex guard must not be held across an await: run the query in `spawn_blocking`, or use an async driver.

**Clients of external APIs.**

- **The base URL is a parameter,** so tests point the client at a mock server.
- Every client sets a timeout and a user agent, and clamps paging to the provider's limits.
- Each status maps to a domain error: authentication, rate limit (after its retries), and invalid request with the provider's message parsed out.
- Tests inject the delay or use a paused clock. No real sleeps.

**Optional exporters sit behind a cargo feature;** core metrics are always compiled, and
tests run with and without the feature. An in-memory metric store has a retention bound.

## Security of a service

This is a floor, not a threat model. Authorisation design, CSRF, SSRF, key management,
dependency risk and data retention each need their own review.

**Limits on every public listener.**

| Control | Guards against | Typical tool |
|---|---|---|
| Request timeout | Slow clients holding connections | `tower_http::timeout::TimeoutLayer` |
| Body size limit | Memory exhaustion | `DefaultBodyLimit`, per-route where uploads differ |
| Rate limit | Brute force, abuse | `tower_governor`, or the gateway |
| Concurrency limit, bounded queues | Overload collapse | `ConcurrencyLimitLayer`, bounded channels |
| TLS | Interception | `rustls`, or termination at a trusted proxy |

- **Middleware order is behaviour.** A body limit placed after a layer that buffers the body protects nothing. Check order against the framework version in `Cargo.lock`.
- A rate limit keyed on client address is only as good as the address: behind a proxy, take it from the header your proxy sets, not from one the client can send.

**Secrets and credentials.**

- Credentials and tokens are typed, redacting values (`secrecy`), exposed at the one place they are used. Sensitive buffers are wiped (`zeroize`).
- **Passwords are hashed with a memory-hard function** (Argon2id) using parameters from current guidance, and verified on the blocking pool: a hash takes tens of milliseconds of CPU.
- **Secret comparison is constant-time** (`subtle`, or the verify function of the MAC or hash crate). `==` on tokens leaks through timing.
- **Reset tokens are not sessions:** random, single use, short-lived, scoped to one action, stored hashed.
- **Sessions have a revocation path.** A stateless token that cannot be revoked needs a short lifetime.
- A type wrapper is not access control. A typed `UserId` says the id is well-formed, not that the caller may use it.

**One public shape for authentication failures.** Login and reset return the same body,
status, redirect and timing whether or not the account exists. Diagnostics go to logs.

- "Same timing" means doing the same work: verify against a dummy hash when the user is unknown.
- **A product-required disclosure is an isolated exception.** If an invitation flow must reveal account state, confine it to that flow, rate-limit it and test its abuse boundary.
- A test that asserts a distinguishable response for unknown accounts encodes a defect.

**Idempotency and replay.**

- **An idempotency key is bound to the caller and the request content.** A replay never returns a response the caller is no longer authorised to see. Keys expire, and their records do not hold sensitive payloads longer than policy allows.
- **Workers acknowledge a job only after durable completion,** and tolerate duplicate delivery. Exactly-once delivery cannot be assumed, least of all across services.
- **A timeout after the remote may have acted is ambiguous, not failed.** Do not retry a charge-like effect blindly: query the provider with the idempotency key or reconcile first. A cancellation is not a failure to replay.
- **Webhook handlers verify the signature over the raw body** before parsing, store each provider event id and ignore repeats, apply status changes through explicit transitions (events arrive out of order), and are backed by periodic reconciliation with the provider.
- **Every externally visible result corresponds to a durable, authorised state.** Model each sensitive flow as an explicit state machine. An unmodelled intermediate state is the most dangerous defect: it can leak information and duplicate an effect at once.

**Observability without leaks.**

- Link events by an opaque flow id, never an email, token or key.
- No metric label or log field that reveals whether a user exists. No payload data inside idempotency keys.
- Log failures and cancellations as well as successes. Operator records have access control and bounded retention.

**Tests these flows need.**

- Compare public responses and timing for known and unknown accounts.
- Race identical writes; send concurrent requests, not only sequential ones.
- Reuse and replay reset tokens, including concurrently.
- Crash before and after the commit. Inject each remote failure class, and a timeout after the remote succeeded.
- Fixtures: an isolated database, a controlled clock and randomness, and a fake remote that can fail both before and after its effect.
- **Benchmark with the controls on.** Removing hashing, durable writes or failure shaping makes an unsafe path look fast.

**Design order for a sensitive flow:** assets and actors; what each party can observe;
durable states and effects; typed boundaries and error classes; idempotency and transaction
scope; inline or worker; abuse and crash tests; staged rollout with a rehearsed rollback.

**Release blockers:**

- raw credentials past the adapter, or secrets in logs;
- public failures that depend on whether an identity exists;
- reusable, long-lived or over-broad reset tokens;
- idempotency keys not bound to actor and request;
- a lock or transaction held across a remote effect;
- a remote call with no timeout, or a retry of a permanent failure;
- an acknowledgement before durable completion.

**Judgement calls.**

- **Deny by default.** A new route is protected until someone decides otherwise.
- **A queue moves a failure; it does not remove it.** Add background work only with a durable owner and a way for an operator to see and recover stuck jobs.
- **Retries can amplify an outage.** Bound them, add jitter, and stop when the dependency is clearly down.
- **A deploy rollback does not roll back data.**
- Prefer the design with the fewest ambiguous states over the one with the lowest latency or least code.
- When state is unclear during an incident, slow or stop intake. More requests obscure which effects already happened. Keep the evidence: do not restart in a way that erases it.

### Untrusted input at the edges

These apply to any Rust program that takes input from outside, not only to web services.

**Server-side fetch of a user-supplied URL.** One `validate_url` runs before every such
fetch.

- Allow only `http` and `https`. Reject loopback, private, link-local and cloud-metadata addresses, and internal hostnames.
- **Checking the hostname is not enough.** Resolve it, check the address, and connect to the address you checked, so a second DNS answer cannot differ.
- Validate every redirect the same way, or disable redirects. Cap the response size and set a timeout.
- Test IPv4, IPv6, IPv4-mapped IPv6 (`::ffff:127.0.0.1`), and decimal or octal spellings of an address.
- An intranet exception is an explicit allow-list, not a weaker default.

**Paths from input.** Canonicalise, then require the result to lie inside the allowed base.

```rust
fn resolve_inside(base: &Path, requested: &Path) -> Result<PathBuf, PathError> {
    let base = base.canonicalize()?;
    let candidate = base.join(requested).canonicalize()?;
    if candidate.starts_with(&base) {
        Ok(candidate)
    } else {
        Err(PathError::OutsideBase)
    }
}
```

- `canonicalize` requires the path to exist. For a file about to be created, canonicalise the parent and validate the file name separately.
- Compare with `Path::starts_with`, which works on whole components. A string prefix test accepts `/data-evil` for base `/data`.
- A check followed by a later open can be raced by a symlink swap. Where that matters, open relative to a directory handle (`cap-std`, `openat`) and do not re-resolve.

**Recursive walkers use no-follow calls.** `Path::exists` and `fs::metadata` follow links,
so a walker using them can loop forever or leave the tree. Use `fs::symlink_metadata`.

```rust
pub fn is_symlink_or_junction(path: &Path) -> bool {
    let Ok(meta) = fs::symlink_metadata(path) else { return false };
    if meta.file_type().is_symlink() {
        return true;
    }
    #[cfg(windows)]
    {
        use std::os::windows::fs::MetadataExt;
        const FILE_ATTRIBUTE_REPARSE_POINT: u32 = 0x400;
        if meta.file_attributes() & FILE_ATTRIBUTE_REPARSE_POINT != 0 {
            return true;
        }
    }
    false
}
```

- Windows junctions are reparse points, not symlinks, so check both.
- Following links is an opt-in mode with cycle detection.

**Deserialising across a trust boundary.** Use a closed schema: named fields, closed enums,
`#[serde(deny_unknown_fields)]` where an unknown field signals a mistake, and limits on
size and nesting depth. Never let untrusted input choose which type gets constructed.

**Running commands.**

- **Use `Command` with a program and separate arguments. No shell.** Arguments passed this way are not re-parsed, which removes injection at its source.
- An argument beginning with `-` can still be read as an option. Put `--` before data-derived positional arguments where the program supports it.
- **Do not pass credentials as arguments;** they appear in process listings. Use the environment, standard input or a file with restricted permissions.
- Success is the exit status or structured output, not a phrase in the text. A failed write to the child's standard input is an error.
- If shell text must be accepted, parsing it against an allow-list of programs and rejecting redirects and subshells lowers the risk. It does not make arbitrary shell text safe; say so.

**User-supplied expressions** (formulas, filters) are parsed into a syntax tree, validated
recursively against an allow-list of node kinds, operators, functions and variable names,
then evaluated in a constrained scope, with limits on depth and cost. Never hand one to a
general evaluator. An unknown name gets an error with a close-match suggestion.

**Embedding one query language in another.** Where a position cannot take a bound
parameter:

- Validate identifiers against a strict pattern such as `^[A-Za-z_][A-Za-z0-9_]*$` and reject everything else.
- Quote a free-form body with a delimiter proven absent from it. Never assume a delimiter cannot occur.
- Prefer real bind parameters wherever the driver allows them.

**Authorisation before the body.** On an upload or import route, the authorisation check
runs before anything buffers the body or spools it to disk.

- In Actix, extractors run in parameter order: put the authorising extractor first and leave a comment saying why.
- In Axum, the body extractor must be last anyway; authorise in an earlier extractor or in middleware.
- Test that an unauthorised upload creates no temporary file.

**Untrusted commands and repository configuration.** A bot, webhook handler or agent bridge
dispatches through a static table (an enum and a `match`), never by loading something named
by the input.

- **Configuration found in a repository is untrusted.** It cannot set host-only keys: secrets, filesystem paths, endpoints, the commands to run.
- Security-relevant settings are refused on the command line with a pointer to the host configuration.

**Text handed to a model or agent** passes a policy step between retrieval and
presentation: exclude by path (`.env`, `*.pem`, `*.key`, `id_rsa`), replace secret-shaped
text with a marker, and report how many items were excluded. Pattern scans miss unusual
secrets, so treat this as reduction, not a guarantee.

**Secret carriers are wiped on drop.** A struct holding key material derives
`ZeroizeOnDrop`.

```rust
#[derive(Zeroize, ZeroizeOnDrop)]
pub struct Pkcs12Archive {
    der: Vec<u8>,
    passphrase: String,
}
```

- An `into_parts()` that moves the fields out hands the duty to the caller, and says so.
- **Wiping is best effort.** It does not reach copies made by a reallocating `Vec`, a clone, a log line, or a library that kept its own buffer. Do not claim more.

**Authorisation data is indexed by the questions asked.** For hot-path checks, keep maps
shaped like the questions (`HashMap<(UserId, StreamId), Permissions>`), so a check is a
lookup or two. Every update and delete path maintains every derived set. Test that a
revoked permission is denied: a stale allow is the dangerous failure.

**State the level of evidence behind a security claim.** Documented is not configured;
configured is not reachable; tested is not deployed; observed once is not attacker-proof.
Compilation proves no authorisation property. After a framework upgrade or an advisory,
re-check behaviour against the locked version and rerun the abuse tests.

**A read-only query gate.** When users or agents may submit queries but only reads are
allowed:

- **The database enforces it:** a read-only role or connection (`SQLITE_OPEN_READ_ONLY`, a role with only `SELECT`), plus a statement timeout and a row limit.
- A validator in front is defence in depth: one shared function for every entry point, which strips literals and comments, rejects statement separators, and rejects mutating keywords on word boundaries.
- **A keyword scan alone is not a sandbox.** Functions with side effects, pragmas and writable common table expressions get past it.
- Test forbidden keywords in comments, in strings and in mixed case.

**A service address taken from the request is checked against an allow-list.** A handler
that forwards to a `url` parameter is a request-forgery hole. The default is a named
constant, overrides come from configuration, and traversal parameters such as `depth` are
bounded in the typed query struct.

## Operability

Three properties, each proven before it is relied on: **state is explicit at boot,
behaviour is explainable per request, and change is reversible per step.**

- **One correlation identifier per request,** propagated through every layer, into outbound calls and into worker hand-offs. A batch job correlates by job id. Test: follow one real request by identifier alone.
- **Structured traces, not formatted strings.** Record high-value fields once on the span and let them propagate. Do not trace every function entry.
- **Readiness is separate from liveness,** and reflects the dependencies the service cannot work without. Document which. Removing a slow dependency check from readiness is how a green endpoint ends up in front of a failing service.
- **Count errors, timeouts, retries and saturation** (pool waits, queue depth). Sampling high-volume reads is fine; mutations stay unsampled.
- **Before rollout, plan for a surge:** rate limits, bounded queues, request timeouts, load shedding, and the rollback procedure.
- Adopt in order: typed fail-fast configuration and redaction, then correlated tracing, then honest health checks, then CI gates and migration sequencing. Runbooks are premature for a service that prints passwords or crash-loops on a malformed variable.

**Decay happens through additions.** A new setting bypasses the settings module; a new code
path skips the correlation field; a health check stops matching the real dependency list;
each successful migration justifies less care on the next. Probe for each periodically.

### Tracing without leaking

**Observability and secrets.**

```rust
#[tracing::instrument(skip(request, state), fields(method = %request.method(), path = %request.uri().path()))]
pub async fn handle(state: AppState, request: Request) -> Result<Response, Error> {
    // ...
}

let api_key = SecretString::from(load_key()?);
tracing::info!(has_key = !api_key.expose_secret().is_empty());   // never the key itself
```

- **`#[instrument]` records every argument with `Debug` unless told otherwise.** Skip bodies, credentials and large values, and name the fields you want. An un-skipped request or config struct is the usual way a secret reaches a log.
- Propagate a trace identifier across service boundaries. A user identifier is personal data: record it only where policy allows.
- **Libraries emit through `tracing` or `log` and never `println!`.** The application chooses where output goes.
- **Do not spread a secret:** no wide cloning, expose it only at the call that needs it, and keep it out of `Debug`, `Display`, errors and panics.

### Errors on the wire

**One metadata trait and one envelope, when a machine acts on the error.** Errors that cross
an API, CLI or agent boundary need a stable code, a retry hint and a decision about what is
safe to show. Every domain error implements one trait; one envelope carries the fields.

```rust
pub trait ErrorData {
    fn code(&self) -> &'static str;
    fn retryable(&self) -> bool;
    /// Internal errors are not shown to external callers.
    fn internal(&self) -> bool;
    fn http_status(&self) -> u16 {
        500
    }
    /// What the caller can do about it.
    fn hint(&self) -> Option<String> {
        None
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ErrorEnvelope {
    pub code: String,
    pub message: String,
    pub retryable: bool,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub hint: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub context: Option<serde_json::Value>,
}
```

- **`code`, `retryable` and `internal` have no defaults,** so a new variant cannot be added without deciding them. Prefer a `match` with no wildcard arm, or a derive that generates one.
- **Two projections of one error.** The external one replaces an internal error's message with a generic text and a correlation ID; the detailed one goes to logs. The web framework's response conversion uses only the external one. An internal message reaching a client (a SQL fragment, a file path, a host name) is an information leak.
- **A table test covers every visible variant:** status, code, serialised shape and retry class. A snapshot of the envelope catches a renamed field.
- **A public code is a compatibility promise.** Put a new error in the narrowest existing class (client error, transient, server error); clients decide to retry from the class, never from the message.
- *Not for* a small private module, where `thiserror` and context are enough.

**Translate a generated client's errors once, at the SDK boundary.** An extension trait on the
generated `Result` maps into the house error type. A documented API error keeps its status,
code and source; a transport error becomes a communication error that is retryable for
connect and timeout failures. Do not flatten everything into one variant while a caller still
needs the status or the retry decision.

**Classify from the whole chain.** When errors are wrapped with context, the type that decides
retryability is the innermost one.

```rust
fn is_transient(error: &anyhow::Error) -> bool {
    error
        .chain()
        .find_map(|cause| cause.downcast_ref::<BackendError>())
        .is_some_and(BackendError::is_transient)
}
```

- Retry only what is explicitly temporary. A typed permanent error passes through unchanged; an unknown error is treated as permanent.
- In a stack of backends or plugins, one wrapper adds the operation, service and path as structured fields, and retry policy reads a typed field, never a substring.

### Cancellation, saturation and shutdown

**Say what each long-running operation does when it is cancelled:** cancel-safe (nothing is
lost), restartable (safe to run again from the start), resumable (continues from a persisted
point) or lossy. If partial progress matters, persist the intent before acting, so an
interruption leaves something to resume from and not a silent half-change.

**Name the saturation policy.** When producers can outpace consumers, the choices are: make
the producer wait, reject, shed the oldest or newest, batch, or spill to durable storage.
"The queue should stay small" is not a policy. One unbounded producer anywhere defeats every
bounded channel downstream of it.

**The shutdown contract** states who starts it, how the signal reaches every task, how
completion is awaited, and that calling it twice is harmless.

- **Rust has no async destructors.** Clean-up that must be awaited (flush, close a protocol properly, deregister) is an explicit `async fn shutdown(self)`. It belongs in the API documentation and in a test; `Drop` is the best-effort fallback.
- **At shutdown, every accepted job has a known fate:** it ran, or it was closed without running and its submitter was told. Nothing is left silently in a queue.
- `tokio_util` supplies the pieces: `CancellationToken` (with `drop_guard()`, so that dropping an owner cancels its group) and `TaskTracker` (wait until every tracked task has finished). Prefer them to a hand-built guard with a reference count and a channel; a `JoinSet` is enough when one owner spawns and joins.
- **Test shutdown under load.** Inject cancellation while messages are in flight and assert that none is lost or handled twice. It is where bounded channels, tokens and cancel-safe branches either work together or fail together.

**Retries interact with cancellation.** A retry loop around a future that is not cancel-safe
re-enters half-consumed state on each attempt. The hazards: a timeout after the remote effect
already happened, a library retry nested inside an application retry, cancellation between
an effect and its acknowledgement, and a backoff that outlasts the caller's deadline. Keep
the first error as well as the last; the first usually names the cause.

**Do not hold a span guard across `.await`.**

```rust
// Wrong: the span stays "entered" on this thread while the task is suspended,
// so unrelated tasks polled here are recorded inside it.
let _entered = span.enter();
fetch().await;

// Right.
fetch().instrument(span).await;
```

- Useful telemetry follows the design: each task's parent and how it ended, queue depth beside its capacity, and cancellation recorded as its own outcome and not as an error. Metric labels never come from user input, since each distinct value is a new time series.

### State owned by one task

One task owns the state; everyone else holds a cheap handle and sends typed messages. There is
no lock, the state's lifecycle is the task's, and every operation is one message, so multi-step
updates cannot interleave.

```rust
enum Command {
    Get {
        key: Key,
        reply: oneshot::Sender<Option<Value>>,
    },
    Put {
        key: Key,
        value: Value,
        reply: oneshot::Sender<Result<(), StoreError>>,
    },
}

#[derive(Clone)]
pub struct StoreHandle {
    commands: mpsc::Sender<Command>,
}

impl StoreHandle {
    pub fn spawn(capacity: usize) -> (Self, JoinHandle<()>) {
        let (commands, inbox) = mpsc::channel(capacity);
        let task = tokio::spawn(run(Store::default(), inbox));
        (Self { commands }, task)
    }

    pub async fn get(&self, key: Key) -> Result<Option<Value>, StoreError> {
        let (reply, response) = oneshot::channel();
        self.commands
            .send(Command::Get { key, reply })
            .await
            .map_err(|_| StoreError::Stopped)?;
        response.await.map_err(|_| StoreError::Stopped)
    }
}

async fn run(mut store: Store, mut inbox: mpsc::Receiver<Command>) {
    while let Some(command) = inbox.recv().await {
        match command {
            Command::Get { key, reply } => {
                let _ = reply.send(store.get(&key)); // the caller may have given up
            }
            Command::Put { key, value, reply } => {
                let _ = reply.send(store.put(key, value));
            }
        }
    }
    // Every handle is gone: flush and release here.
}
```

- **Messages are a typed enum, one variant per operation.** A generic "run this closure on the state" message gives back the unstructured access the pattern was meant to remove.
- **The mailbox is bounded,** so a slow actor slows its callers instead of growing memory.
- **The loop ends when every handle is dropped;** that is the shutdown path, and the place for final clean-up. Keep the `JoinHandle` so something can wait for it.
- **Both the send and the reply can fail** (the actor stopped or panicked). The handle maps both to an error; it never `unwrap`s.
- **Do not do slow work in the loop.** While the actor awaits an HTTP call, every other message waits. Spawn the slow part and have it send its result back as a message.
- **Two actors that await each other's replies can deadlock** exactly like two locks. Keep the call graph between actors acyclic, or use one-way messages.
- *Use a `Mutex` instead* for a small piece of state with short, independent updates. An actor is worth its ceremony when the state has a lifecycle, owns I/O, or needs operations to be serialised.

**`select!` details.**

- Branches are polled in random order by default, which is fair. `biased;` polls them top to bottom: put shutdown first so it is noticed promptly, and be aware that a branch that is always ready then starves those below it.
- A branch whose future is created inside the loop is created afresh each iteration. A timer that should span iterations (`sleep`, `interval`) is created outside and pinned.
- Use a `CancellationToken`, not a shared boolean: a flag cannot wake a task that is waiting on something else.

## Performance of a service

**Audit four mechanisms before reading latency numbers:** pool and client reuse,
transaction scope, inline-or-worker placement, and fan-out.

- **Fix the mechanism, not the symptom.** Do not put a cache over an endpoint whose pool is exhausted by held transactions; move the remote call after the commit.
- **Averages hide the tail.** One password hash run on the async executor stalls every request on that worker thread. Measure p95 and p99.
- Require a service-specific latency objective before deployment. Absent one, a local default such as p95 under 200 ms and p99 under 500 ms for representative handlers is a starting point, not a fact about your users.
- Image builds: order layers so dependency compilation is cached separately from application source (`cargo-chef` or equivalent).

### Caches

**A cache is a correctness risk bought for speed.** Before adding one, state the key, what
invalidates an entry, the size bound and what a stale read costs.

- **Bound it:** a maximum size, usually a time to live as well. An unbounded map used as a cache is a memory leak. `moka` for a concurrent cache with eviction; a `HashMap` or `lru` behind the owner's lock for a small one.
- **The key contains every input that changes the answer.** Tenant, authorisation scope, locale, version, options. A key that omits the user serves one user's data to another.
- **Never cache what is not a pure function of the key** unless staleness is accepted and bounded.
- **Policy is part of a cache's identity.** Settings that change validity (time to live, capacity, persistence, scope) belong in the type or key that decides whether an existing cache may be reused.
- **Negative results are cached separately,** with a shorter life: "not found" goes stale as soon as the thing is created.
- **Many concurrent misses for one key should compute once.** Use the cache's get-or-insert-with, or single-flight, not a check followed by an insert.
- **Measure the hit rate.** A cache that rarely hits costs memory, locking and complexity for nothing.
- A process-wide cache needs an invalidation path, and tests need a way to start with it empty.

**Build-style cache keys come from every semantic input.**

```rust
let mut entries: Vec<_> = fs::read_dir(dir)?.collect::<Result<_, _>>()?;
entries.sort_by_key(|entry| entry.file_name()); // traversal order must not change the key
for entry in entries {
    hasher.update(b"file\0");
    hasher.update(entry.file_name().as_encoded_bytes());
    hasher.update(b"\0");
    hasher.update(&fs::read(entry.path())?);
}
```

- Hash the tool version, the input contents, the options and each environment setting that affects output. Separate fields with a tag and a delimiter, so `("ab", "c")` and `("a", "bc")` differ.
- **Size and modification time may shortcut re-reading an unchanged file; they are never the identity.**
- Use a stable hash (BLAKE3, SHA-256) for anything persisted. `DefaultHasher` is not stable across Rust versions.
- Namespace cached output by the producer's version, write with a temporary file and an atomic rename, treat an unreadable entry as a miss, and keep a `--force` or `--no-cache` escape hatch.
- **Invalidate by interface when that is what dependants use.** Hash the sorted public facts (names, signatures, imports) and classify a change as none, cosmetic or structural. The hash ignores bodies by design; add behaviour inputs explicitly if they matter.
- **Cache a compiled intermediate form** (a lowered plan, a compiled template) with `OnceLock` or a keyed cache, and know what invalidates it before the source is allowed to change.

## Tests

- **Unit tests cover the layer back ends break least.** Wiring, routing, serialisation and state set-up fail in integration. Default stack: spawned-app tests on a random port with an isolated database and migrations applied; mock-server contract tests for each outbound client; property tests for domain constructors; migration tests when the schema moves.
- **Each empty, malformed and duplicate input is a named test.**
- **Ambiguity under failure passes every deterministic test.** Kill a worker mid-workflow in staging and check the state it leaves.
- Passing format, lint, tests and build is no evidence for "faster" or "safer". Each such claim needs its own measurement.

**Choose the test kind by concern, not by rank.**

| Concern | Cheapest test that catches it |
|---|---|
| Endpoint behaviour, routing, serialisation, wiring | Spawned-app integration test over the wire |
| Domain invariants | Unit or property test |
| Queries and transactions | Integration test against a real, migrated database |
| Outbound calls | Mock-server contract test |
| Auth flows | Both: unit tests for rules, an integration pass for the wire |
| Migration safety | Schema tests plus the rollout plan |

- **Build the suite in order:** a harness that boots the app under test configuration; isolation (random port, database state per test); mocks for external calls; then helpers and property tests. If a service has no harness, building one is the first task.
- **A test reads as a user journey:** "create user, post order, expect 201 and a stored row". A helper states intent; a helper that hides the logic under test turns every failure into a harness investigation.
- **Start from the concerns a change touches,** not from the modules in the diff. No mirror tests that assert a handler returns what it returns.
- **Existing tests are copied as the style guide.** Fix a fixed-port or live-API test before adding more beside it, and stop the first bypass of the harness.
- **A mock that matches any request passes everything.** Assert the shape of the outbound request, and see that assertion fail once before trusting it.
- **Mocks drift on the provider's schedule.** Re-check each against the real contract periodically, not only when tests change.
- **A fake states what it does not reproduce.** An in-memory repository certifies domain rules, never database behaviour.
- Repair fixtures in the same change as the migration that breaks them.
- A second service in one journey calls for a contract pair, one harness test per service, not one test that spawns three services by hand.

**Reject in a service suite:** a fixed port; shared state with no documented boundary; a
live external call in the deterministic suite; automatic retries of failing tests.

**Flaky tests.**

- A deterministic failure is fixed; rerunning it changes nothing. Never merge on the third rerun's green.
- An intermittent failure is usually shared state or a missing mock. Check what the test shares first, and run the suite in shuffled order now and then.
- **Quarantine is triage, not a fix.** A quarantined test has an owner and a date, and the list is capped. A falling flake rate may only mean a growing quarantine.
- **Sharing state is the easiest speed-up and the wrong one.** Parallel runs and template databases cut set-up cost without touching isolation. A suite developers stop running locally has lost its value.

## Review

**Seven questions for any back-end review:** Are credentials typed? Are logs redacted? Are
failures shaped for the client? Are transactions explicit? Is idempotency defined for each
mutation? What state is left if the process dies mid-workflow? Should this work be
asynchronous?

**Per release, four things should be zero:** unowned transactions; retried writes with no
idempotency definition; unclassified remote failure paths; rollout steps with no rehearsed
rollback.

The reject-on-sight list is under "Layers", and the release blockers are under "Security
of a service". Check a change against both before handing it over.

## Patterns seen in production repositories

Each entry names the project it was observed in. Treat them as shapes to adapt, not as APIs to copy.

- **An "already in progress" marker with Redis.** `SET key value NX` with a TTL lets one caller claim a piece of work; the expiry frees it if the holder dies. Test it with ten concurrent callers and assert that exactly one wins.
- **Concurrency tests against a real database.** Run Testcontainers-based tests serially for isolation, then spawn several tasks (five is enough) that insert at once, to exercise the application's own concurrency against real Postgres.
- **Embedding one query language in another.** When Cypher is wrapped in a PostgreSQL call, allow-list every graph and SQL identifier and choose a dollar-quote delimiter that cannot occur in the embedded text.
- **A typed local event broker.** Keep one subscription map per event type in a type-keyed map. Subscribing returns a handle that unsubscribes when dropped, and each callback runs under a timeout so one slow subscriber cannot stall publishing.
- **Shutdown with a final checkpoint.** On a stop signal, request a checkpoint and wait for it with a limit (120 seconds in the observed runner); after the limit, shut down immediately.
- **When to change the test strategy.** A second service in one user journey calls for contract tests. A datastore shared between suites calls for isolation at schema level. A suite that has grown too slow calls for tiers that are named for what they skip.

## Out of scope

- **Hot loops, parsers, indexes, storage engines and custom data structures.** A service that contains one hands that part to the infra skill.
- **A published crate's public interface and versioning.** Use the library skill.
- **Unsafe code and FFI.**
- **Threat modelling.** The security sections here are a floor: authorisation design, key management, dependency risk and data retention each need their own review.
- **The front end and the deployment platform.**

<!-- essentials:begin -->
## Rust essentials shared by every writer skill

This block is the same in every Rust writer skill. It holds the language-level rules that
decide whether Rust code is correct whatever it is for: ownership, types at boundaries,
errors, async, tests and the anti-patterns to reject. Where the skill above states a rule
for its own kind of Rust more firmly, that statement wins.

### Ownership and borrowing

**Defaults.**

- Borrow to read, take ownership to keep, `&mut` to change in place. The signature tells the caller which.
- Clone when the design calls for a second owner, not to make an error go away. A clone of a small value on a cold path is fine and often the clearest code; a clone in a loop over large data is worth a second look.
- `Arc` for shared ownership across threads, `Rc` within one. Neither is a substitute for deciding who owns the data.
- Hold locks and `RefCell` borrows for the shortest scope that is correct, and never across an `.await`.

**The error usually describes a real overlap.** Find which borrow is still alive and why,
then shorten it, instead of reaching for `clone` or `Rc<RefCell<_>>`.

```rust
// Rejected: first borrows items while push needs it mutably.
let first = &items[0];
items.push(first.clone());

// End the shared borrow before the mutation.
let first = items[0].clone();
items.push(first);
```

- **A method borrows all of `self`.** Calling `self.helper()` while a field is borrowed fails even if the helper touches other fields. Borrow the fields separately, which the compiler tracks, or make the helper take the fields it needs.

```rust
let Self { index, scratch, .. } = self;
for id in index.keys() {
    scratch.push(*id); // index is borrowed shared, scratch mutably: disjoint fields
}
```

- **Collect, then mutate.** Gather the keys or indices to change in one pass and apply them in a second. Often clearer as well as accepted.
- **Use indices or IDs instead of long-lived references** into a collection that also needs mutation. This is the normal shape for graphs and trees with parent links.
- **Move out through `&mut` with `std::mem::take`, `replace` or `Option::take`,** instead of cloning a field in order to consume it.
- **The `entry` API** does "look up, then insert or update" with one borrow and one hash.

```rust
*counts.entry(word).or_insert(0) += 1;
```

- **Separate the read phase from the write phase in an API.** A method that returns a reference into `self` keeps `self` borrowed for as long as the caller holds it; returning a small owned value or an ID frees the caller.
- `vec.push(vec.len())` compiles through two-phase borrows. Do not design an API that only works because of that rule; write the temporary.
- **Stop and reconsider the design** when a structure wants references to itself, or when lifetimes spread through many signatures. Owned data plus indices, or an arena, is nearly always the answer; `unsafe` is not.

### Interior mutability

| Need | Use | Watch for |
|---|---|---|
| A `Copy` value, one thread | `Cell<T>` | nothing; it cannot fail |
| Any value, one thread | `RefCell<T>` | a second overlapping `borrow_mut` panics at run time |
| Shared across threads | `Mutex<T>` | poisoning, lock order, holding it across `.await` |
| Read-mostly across threads | `RwLock<T>` | writer starvation; often no faster than `Mutex`, so measure |
| A counter or flag | `AtomicUsize`, `AtomicBool` | choosing an ordering; `SeqCst` unless you can argue for less |
| Set once, read often | `OnceLock<T>`, `LazyLock<T>` | initialisation that can fail |

- `RefCell` moves a compile-time rule to run time. Keep each borrow to one statement where possible, and prefer `try_borrow_mut` where re-entrancy is conceivable (callbacks, observers).
- Do not use a `Mutex` in single-threaded code to quiet the borrow checker, and do not make a type `Sync` by wrapping it in one without deciding what the lock protects.
- Interior mutability behind `&self` is part of the API's contract. Say so in the docs when a `&self` method changes observable state.

### Choosing a pointer

| Need | One thread | Across threads |
|---|---|---|
| One owner on the heap (recursive type, large value, trait object) | `Box<T>` | `Box<T>` |
| Several owners, read-only | `Rc<T>` | `Arc<T>` |
| Several owners, mutation | `Rc<RefCell<T>>` | `Arc<Mutex<T>>` or `Arc<RwLock<T>>` |
| A reference back to an owner | `rc::Weak<T>` | `sync::Weak<T>` |

- **Shared and immutable is the cheap case.** Prefer `Arc<T>` of immutable data, replaced whole, over `Arc<Mutex<T>>` mutated in place. `Arc::make_mut` gives copy-on-write when a private change is needed.
- **`Rc<RefCell<T>>` throughout a design is a sign** that ownership was never decided. It suits a few shared nodes (a GUI tree, an observer list), not a whole data model. Indices into an owning `Vec` are usually simpler and faster.
- **Parent-to-child strong, child-to-parent `Weak`,** or the cycle never frees.
- `Arc::clone(&x)` rather than `x.clone()` makes it visible that only the count is bumped.
- Before `Arc<Mutex<T>>` across tasks, ask whether one task could own the state and receive messages on a channel.

### Iterators and collections

- **A fallible pipeline short-circuits.** An iterator of `Result<T, E>` collects into `Result<Vec<T>, E>` and stops at the first error. `try_for_each` and `try_fold` do the same without collecting. Never `unwrap` inside a chain.

```rust
let ports: Vec<u16> = fields
    .iter()
    .map(|field| field.parse::<u16>())
    .collect::<Result<_, _>>()?;
```

- **Iterator promises are contracts.** `size_hint` must bracket the true length; implement `ExactSizeIterator` only when the length is exact. Unsafe code must not rely on either for memory safety, since safe code can implement them wrongly.
- Offer `iter()`, `iter_mut()` and `IntoIterator` for `&T`, `&mut T` and `T` on a collection type, so `for x in &collection` works.
- Iterators are lazy. A `map` with side effects that is never consumed does nothing; use `for` when the point is the effect.

| Need | Collection |
|---|---|
| A sequence; the default | `Vec` |
| Push and pop at both ends | `VecDeque` |
| Lookup by key, order irrelevant | `HashMap`, `HashSet` |
| Sorted order, range queries, deterministic iteration | `BTreeMap`, `BTreeSet` |
| Insertion order with lookup | `IndexMap` |
| Repeatedly take the largest | `BinaryHeap` (wrap in `Reverse` for the smallest) |
| A handful of items | a `Vec` and a linear scan, or `SmallVec` if measured |

- **`HashMap` iteration order is arbitrary and differs between runs.** Anything that reaches output, a hash, a snapshot or a test goes through a sort or an ordered map.
- `LinkedList` is almost never right: a `Vec` or `VecDeque` is faster for nearly every workload.
- The default hasher resists collision attacks and is slower for it. A faster hasher (`FxHashMap`, `ahash`) is for keys an attacker does not control, after a profile says hashing matters.
- `Vec::with_capacity` when the size is known; it is free and removes reallocations.

### Types and API basics

Each with when it pays and when it does not.

- **Accept borrowed inputs.** `&str`, `&[T]` and `&Path`, not `&String`, `&Vec<T>` and `&PathBuf`. The API then commits to meaning, not to a container. *When the function stores the value,* take it owned (`String`, or `impl Into<String>`) so the caller who already owns one does not pay for a clone. `impl AsRef<Path>` is right for path arguments; `impl AsRef<str>` everywhere is noise and bloats code through monomorphisation.
- **Newtypes, and parse instead of validating.** Turn raw data plus repeated checks into a type that can only hold a valid value. IDs, units, offsets, validated strings and handles stop being interchangeable primitives. *Skip when* the wrapper carries no invariant and no distinction anyone could confuse; a newtype around every `String` is ceremony.

```rust
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct Email(String);

impl Email {
    pub fn parse(raw: &str) -> Result<Self, EmailError> {
        let trimmed = raw.trim();
        if trimmed.is_empty() {
            return Err(EmailError::Empty);
        }
        if !trimmed.contains('@') {
            return Err(EmailError::MissingAt);
        }
        Ok(Self(trimmed.to_owned()))
    }
    pub fn as_str(&self) -> &str { &self.0 }
}
```

  Keep the field private and offer no constructor that skips the check, or the guarantee is gone. That includes `Deserialize`: derive it through `#[serde(try_from = "String")]`, not on the raw field. Do not implement `DerefMut` or hand out `&mut` to the inner value.
- **`From` for conversions that cannot fail, `TryFrom` for those that can.** *Use a named constructor instead* when the operation does real work, loses information or has more than one sensible meaning. `From` must be cheap and unsurprising, because `?` and `.into()` call it invisibly.
- **Combinators for straight-line flows, `match` for branching.** `map`, `and_then`, `ok_or_else` and `transpose` keep a linear transformation linear. When there are several arms with different work, or a chain of four closures, a `match` or `let ... else` reads better.
- **Generics or `dyn`, chosen on purpose.** Generics for hot paths and when the caller knows the type. `dyn Trait` for heterogeneous collections, plugin points, and to keep compile time and code size down. For a call that does I/O, the virtual call is immeasurable; do not make a service generic over five type parameters to avoid it.
- **Return `impl Iterator` to stay lazy** and hide adapter types. Use `Box<dyn Iterator>` when branches return different iterator types or the type must be stored in a struct field without a generic parameter. Return a `Vec` when the caller always needs all of it and the size is bounded.
- **A named enum over a boolean or a sentinel.** A `bool` says something happened; an enum says what the caller must do next. `enum Inserted { New, Replaced(Old) }` beats `true`; `Option<usize>` beats `-1`. *A `bool` is fine* for a real yes-or-no question (`is_empty`).
- **A flat public facade with `pub use`.** Internal file layout and public paths are separate decisions; re-exports let internals move without breaking callers. Re-export deliberately, item by item. Do not re-export a dependency's types unless they are part of your contract, because then its version is too.
- **Blanket impls for `&T`, `&mut T` and `Box<T>`** make a trait usable through references and boxes without wrappers. Add them when the trait is naturally delegating and its methods take `&self`.
- **Omitted is not the same as explicitly empty.** For a partial update, "not provided" and "set to nothing" are different inputs:

```rust
pub enum Patch<T> {
    Keep,
    Clear,
    Set(T),
}
```

  `Option<Option<T>>` works with serde but is hard to read; the enum is clearer in domain code. Never use a magic value from the domain (an empty string, zero) to mean either.
- **Name the unit of an offset.** Bytes, `char`s and UTF-16 code units are different numbers for the same position. Put the unit in the type (`ByteOffset`, `Utf16Offset`) wherever offsets cross a boundary, and test on multi-byte text.
- **Strategies are named for the guarantee they give.** An operational choice is a named type behind a small trait, not a hidden boolean, and its documentation says what it does *not* preserve:

```rust
pub trait Sharding: Send + Sync {
    fn pick_shard(&self, shard_count: usize, key: &Key) -> usize;
}
pub struct Balanced { next: AtomicUsize } // spreads load; does not keep per-key order
pub struct Ordered;                       // keeps per-key order; load may skew
```

  Offer no alternatives where correctness needs one behaviour.

### Core idioms

- **Expressions over statements.** `if`, `match` and blocks are expressions; bind their value instead of declaring a `mut` and assigning in each branch. Use an iterator chain where it reads as a description of the result; use a loop where there are side effects, early exits or several accumulators.

```rust
let label = match status {
    Status::Active => "active",
    Status::Suspended { .. } => "suspended",
    Status::Closed => "closed",
};
```

- **`Cow<'_, str>` when the value is usually borrowed and sometimes changed:** normalisation, escaping, lossy decoding.

```rust
pub fn normalise(input: &str) -> Cow<'_, str> {
    if input.contains('\t') {
        Cow::Owned(input.replace('\t', "    "))
    } else {
        Cow::Borrowed(input)
    }
}
```

  *Skip it* when the value is always owned or always borrowed, and in struct fields unless profiling asks for it: the lifetime spreads to every holder. Calling `.into_owned()` on every result means it should have returned `String`.
- **A `type` alias is not a new type.** `type UserId = u64;` documents and checks nothing. Use a newtype for distinction; use an alias to shorten a long generic type.
- **`#[repr(transparent)]` on a newtype** is needed only when its layout is relied on: across FFI, or for a reference cast between the wrapper and its field. Elsewhere it is harmless and unnecessary.
- **The orphan rule:** to implement a foreign trait for a foreign type, wrap the type in a local newtype.
- **Do not return `Result` from something that cannot fail,** and do not return `Option` where an error would explain why.
- **`impl Fn` for callbacks, `fn` pointers for tables.** `impl Fn(T) -> U` accepts closures and inlines. A plain `fn(T) -> U` pointer rejects capturing closures; use it in static dispatch tables, in `const` contexts and across FFI, where a nameable, `Copy` type is the point. `&dyn Fn` or `Box<dyn Fn>` when the callback is stored or code size matters more than the call.
- **Keep generic bounds as simple as the use.** `fn f(s: &str)` beats `fn f<S: AsRef<str>>(s: S)` unless callers really pass several types; over-generic signatures hurt inference and error messages. When a generic wrapper is wanted, make it thin and delegate at once to a non-generic inner function, so the body is compiled once.

```rust
pub fn read_config(path: impl AsRef<Path>) -> Result<Config, ConfigError> {
    fn inner(path: &Path) -> Result<Config, ConfigError> { /* the real body */ }
    inner(path.as_ref())
}
```

- **Visibility is the narrowest that works.** Start private; widen to `pub(crate)`, then `pub` when something outside needs it. Every `pub` item in a library is a promise.
- **Do not clone to quiet the borrow checker.** The error is usually pointing at an ownership question: who should own this, and for how long. Answer that. `Rc` or `Arc` is for when several owners really exist.
- **Monomorphisation has a cost.** If generics inflate compile time or binary size, use `dyn Trait` at boundaries and on cold paths, and measure the effect (`cargo llvm-lines`, `cargo bloat`).
- **Name the collection type where it reads best:** `let v: Vec<_> = iter.collect();` or `iter.collect::<Vec<_>>()`. Collect into `Result<Vec<_>, _>` to stop at the first error.
- **Pick the pattern form by the number of cases.** `match` when every case matters; `if let` for one case where the rest is nothing; `let ... else` to unwrap or leave early and keep the happy path unindented; `while let` to drain; `matches!` for a boolean test.

```rust
let Some(user) = users.get(&id) else {
    return Err(Error::UnknownUser(id));
};
```

- **`#[non_exhaustive]` keeps room to grow.** On a public enum, other crates must write a wildcard arm, so adding a variant is not a breaking change; on a struct, they cannot construct it literally, so adding a field is not either. *Use on* public error enums and option structs expected to grow. *Do not use on* an enum callers are meant to match exhaustively (a closed set of states), because it takes the compiler's check away from them. It has no effect inside the defining crate.
- **Avoid a wildcard arm on your own enums.** `_ =>` silences the compiler exactly when a new variant arrives. List the variants, or group them explicitly.

### Destructors, guards and temporaries

- `Drop` cannot fail, must not block and should have almost no side effects. If teardown can fail, block or needs `.await`, expose `close`, `flush` or `shutdown` returning `Result`, and let `Drop` release only local state as a fallback.
- If correctness needs teardown to happen before later work, show it in control flow (an explicit `drop(guard)` or an inner block) and test it.
- `let _ = mutex.lock();` drops the guard at once; `let _guard = mutex.lock();` holds it to the end of the scope. Choose on purpose.
- A temporary created in a `match` or `if let` scrutinee lives to the end of the whole statement:

```rust
// Bad: the guard lives for the whole match, so the second lock deadlocks.
match cache.lock().unwrap().get(&key).cloned() {
    Some(v) => v,
    None => compute_and_insert(&cache, key), // locks the cache again
}

// Good: the guard is dropped at the end of the let statement.
let hit = cache.lock().unwrap().get(&key).cloned();
match hit {
    Some(v) => v,
    None => compute_and_insert(&cache, key),
}
```

- A task that can outlive its caller documents how it is cancelled and how it shuts down.

### Errors

**Defaults.**

- A function that can fail returns `Result`; `?` propagates. Panics are for bugs: a broken invariant that no caller could handle.
- **Libraries return typed errors** (an enum or struct, usually via `thiserror`) that callers can match on. **Applications use `anyhow` or `eyre`** at the top, where errors are reported, not matched. Never export `anyhow::Error` from a library: it tells callers nothing and takes away their ability to react.
- No `unwrap` or `expect` on a path that input, I/O or another system can make fail. Where an invariant truly guarantees success, `expect("why this cannot fail")` states it.
- Never swallow an error. Handle it, return it, or log it with a reason for going on.

### Designing an error type

```rust
#[derive(Debug, thiserror::Error)]
pub enum StoreError {
    #[error("record {id} not found")]
    NotFound { id: RecordId },

    #[error("query timed out after {elapsed:?} (limit {limit:?})")]
    Timeout { elapsed: Duration, limit: Duration },

    #[error("reading {}", .path.display())]
    Read {
        path: PathBuf,
        #[source]
        source: io::Error,
    },

    #[error(transparent)]
    Database(#[from] DatabaseError),
}
```

- **One variant per thing a caller might do differently** (retry, report to the user, treat as absent), not one per call site and not one per underlying library.
- **A variant carries the data needed to act or to explain:** the ID, the path, the limit. A variant holding only a `String` is a message, not a type.
- **Keep the cause as `#[source]`, and do not repeat its text in your message.** Reporters print the chain; a message that embeds the source prints it twice. `cause: String` throws the chain away.
- Messages are lower case, without a trailing full stop, and say what was being attempted.
- **`#[from]` only where the conversion needs no context.** A blanket `From<io::Error>` makes every `?` on a file operation produce an error that does not say which file.
- Errors are `Send + Sync + 'static` so they can cross threads and be boxed. Keep them small; box a large payload, since the size of `E` is paid by every `Result<T, E>`.
- **`#[non_exhaustive]` on a public error enum that will grow,** so adding a variant is not a breaking change.

**An opaque error with a kind, when the error space will evolve.** A public enum freezes its
variants and their fields. A struct with a private representation and a public `kind()` keeps
room to change.

```rust
#[derive(Debug)]
pub struct Error {
    kind: ErrorKind,
    source: Option<Box<dyn std::error::Error + Send + Sync>>,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
#[non_exhaustive]
pub enum ErrorKind {
    NotFound,
    Timeout,
    InvalidInput,
}

impl Error {
    pub fn kind(&self) -> ErrorKind {
        self.kind
    }

    pub fn is_retryable(&self) -> bool {
        matches!(self.kind, ErrorKind::Timeout)
    }
}
```

- Callers cannot construct it, so only your crate decides which states exist. Predicates such as `is_retryable()` answer the question callers actually have.
- *Use a plain enum* when the set is small, stable and callers benefit from matching on fields. Most internal crates are in that case.

### Context and reporting

**Add context where the operation is still meaningful.** `?` alone says what failed, not what
was being done.

```rust
pub fn load_config(path: &Path) -> anyhow::Result<Config> {
    let text = fs::read_to_string(path)
        .with_context(|| format!("reading config {}", path.display()))?;
    let config = toml::from_str(&text)
        .with_context(|| format!("parsing config {}", path.display()))?;
    Ok(config)
}
```

- Context belongs at I/O and orchestration boundaries: opening a file, sending a request, decoding a payload, calling another service. Adding it at every helper repeats the same sentence down the chain.
- `with_context` takes a closure, so the message is formatted only on failure.
- In a library, the equivalent is a variant that carries the context plus the `#[source]`, built with `map_err`.

**A diagnostic for a person says where and what to do.** For user-facing input (configuration,
flags, patterns, file formats): the file, line and column or byte offset, what was found, what
was expected, and a hint when there is an obvious repair. An abstract variant name helps
nobody.

- Rich reports with source snippets and labelled spans (`miette`, `ariadne`, `color-eyre`) belong in the binary. Do not put their types in a library's public API; expose spans and messages as plain data and let the binary render them.
- **Diagnostics must survive non-UTF-8 data.** Paths, command output and protocol bytes are not always valid UTF-8. Print paths with `.display()`, bytes with an escaping formatter, and do not convert to `String` early with `unwrap` or lose data with a silent lossy conversion.
- Never put secrets, tokens or whole payloads in an error message. Errors travel to logs and to users.

**The binary owns the exit code.**

```rust
fn main() -> ExitCode {
    match run() {
        Ok(()) => ExitCode::SUCCESS,
        Err(error) if is_broken_pipe(&error) => ExitCode::SUCCESS,
        Err(error) => {
            eprintln!("error: {error:#}");
            ExitCode::from(2)
        }
    }
}
```

- Returning `ExitCode` from `main` lets destructors run; `std::process::exit` does not, so buffered output and temporary files can be lost.
- A closed pipe (`tool | head`) is not a failure. Look for `io::ErrorKind::BrokenPipe` in the chain and exit quietly.
- `{error:#}` prints an `anyhow` error with its causes on one line; `{error:?}` prints the multi-line report with a backtrace if one was captured.
- Distinct exit codes for distinct classes (usage error, runtime failure) are part of a CLI's interface; document them. Errors go to stderr, results to stdout.
- **A library never exits the process,** prints to stdout or stderr, or installs global handlers.

### Panics

- **Audit production paths before a release:** `unwrap`, `expect`, `panic!`, `unreachable!`, `todo!`, slice indexing and arithmetic on external input. Each becomes a `Result` or gets a comment stating the invariant.

```sh
cargo clippy -- -W clippy::unwrap_used -W clippy::expect_used \
  -W clippy::indexing_slicing -W clippy::panic
```

- Compiling and passing unit tests does not show that a panic is unreachable. For each boundary, one test feeds the bad input and asserts the returned error.
- These lints are noisy in tests; allow them there (`#![cfg_attr(test, allow(clippy::unwrap_used))]`) instead of weakening them everywhere.
- **A panic must not cross an FFI boundary.** Catch it with `catch_unwind` at every exported `extern "C"` function and turn it into an error code.

### Recovery by error class

| Class | Where it arises | Recovery | Represent as |
|---|---|---|---|
| Validation | parsing, input edge | reject with the reason | typed parse or validation error |
| Business rule | domain workflow | reject with a precise outcome | named domain error or outcome enum |
| Transient external | network, storage, subprocess | retry with bounds, degrade, reschedule | retryable variant or flag |
| Permanent external | auth, contract or schema mismatch | fail fast, name the repair | typed permanent error |
| Timeout | async orchestration | fail, retry or cancel, explicitly | timeout error carrying the limit |
| Cancellation | task or workflow boundary | stop cooperatively, clean up | its own path, not a failure |
| Overload | queue, pool, stream | reject, shed or wait with a bound | explicit "saturated" result |
| Invariant breach | core logic | make impossible by construction, else fail fast | a narrow panic or an internal error |
| Clean-up failure | close, shutdown | explicit `close`, best-effort `Drop` | close error or shutdown report |
| FFI boundary | ABI, foreign ownership | convert, isolate or abort | the safe wrapper's error |

- **A message answers three questions:** what failed, where, and what the reader should do next.
- **If callers branch on it, give them structure; if they only pass it up, give them context.** Most errors are the second kind.
- Cancellation and overload are not failures of the operation and should not be logged or counted as such.
- A dependency's error type in your public signature makes its version part of your API. Wrap it or re-export it deliberately.

**Smaller rules.**

- **An undo log for in-memory mutations that need rollback.** Record each mutation's inverse as data (`enum UndoOp { CreateNode(NodeId), UpdateAttr { id, old } }`) and replay it backwards on failure. A new mutation kind adds its undo record in the same change; an exhaustive `match` enforces it. Use real transactions when the storage engine has them.
- **`no_std` errors:** implement `core::fmt::Display` by hand and `core::error::Error` directly (stable since Rust 1.81), or put `std::error::Error` behind a `std` feature on older toolchains.
- **Tests assert the variant or code, not message text,** so wording can improve. Retry tests assert behaviour (a permanent error is attempted once; the deadline stops the loop), not exact jittered delays.

### Async and concurrency

**Defaults.**

- **Never block the executor.** No blocking I/O, `std::thread::sleep`, long CPU work or blocking lock inside an async function. Blocking work goes to `spawn_blocking`; CPU-heavy work to a thread pool such as `rayon`.
- **Never hold a lock guard across `.await`.**
- **Everything is bounded:** channels, concurrency, retries, timeouts, buffers.
- **Every task has an owner** that can cancel it and learns how it ended.
- **Every long-running operation can be cancelled** and has a deadline.
- First ask whether you need async at all. A CLI, a build tool or a CPU-bound pipeline is usually simpler and as fast with threads. Async earns its place with many concurrent I/O waits.

### Blocking and locks

**How long is too long without an `.await`?** As a rule of thumb, more than about 100
microseconds of work between yield points starts to hurt other tasks' latency.

| Work | Where it runs |
|---|---|
| Short CPU work, non-blocking calls | inline in the task |
| Blocking I/O, a synchronous client, file-system calls | `tokio::task::spawn_blocking` |
| Heavy CPU work, parallel across cores | `rayon`, with the result sent back over a `oneshot` |
| A long-lived blocking loop | a dedicated `std::thread` |

- `spawn_blocking` tasks cannot be cancelled once started, and the pool is large but finite. Do not park an endless loop there.
- `tokio::fs` uses the blocking pool underneath. For many small file operations, one `spawn_blocking` around the whole batch is faster.

**Locks.**

```rust
// Wrong: the guard lives across the await.
let mut state = shared.lock().unwrap();
state.total += fetch_amount().await?;

// Right: await first, then lock briefly.
let amount = fetch_amount().await?;
shared.lock().unwrap().total += amount;
```

- **Use `std::sync::Mutex` (or `parking_lot`) for short critical sections, even in async code.** It is faster than an async mutex, and its guard is not `Send`, so the compiler rejects holding it across an `.await` in a spawned task.
- **Use `tokio::sync::Mutex` only when the guard must be held across an `.await`,** such as serialising access to a connection. Then ask whether a single owning task with a channel would be clearer.
- A guard in a temporary lives to the end of the statement, and in `if let` or `match` on editions before 2024 to the end of the block. When in doubt, bind the value you need and `drop(guard)` explicitly.
- The same rule holds for a `RefCell` borrow and for anything else that must be released: a pooled connection, a permit, a transaction.
- **Lock order:** when two locks are ever held together, one documented order, everywhere. Better, restructure so that no code holds two.

### Cancellation

**In async Rust, any `.await` is a point where the future may be dropped and never resumed.**
That happens on `select!`, on a timeout, when a `JoinHandle` is aborted, and when a client
disconnects.

- **A future is cancel-safe if dropping it between polls loses nothing.** `recv()` on a Tokio channel is. Reading "exactly n bytes" into a local buffer is not: the bytes already read vanish with the future.
- **In `select!`, keep state outside the branch futures.** A half-filled buffer or a half-advanced parser lives in a variable that survives the loop iteration; the branch only awaits the next piece.

```rust
let mut buffer = BytesMut::new(); // outlives each select! iteration
loop {
    tokio::select! {
        _ = shutdown.cancelled() => break,
        read = socket.read_buf(&mut buffer) => {
            if read? == 0 { break; }
            while let Some(frame) = try_parse(&mut buffer)? {
                handle(frame).await?;
            }
        }
    }
}
```

- **A multi-step change that must not be half-done** is either made atomic (one transaction, one message to an owning task) or run in a spawned task the caller waits on, so that dropping the caller does not stop it midway.
- **Clean-up after cancellation runs in `Drop`, which cannot `.await`.** Hand async clean-up to an owner task, or offer an explicit async `shutdown()` and treat `Drop` as the fallback.
- **Use a `CancellationToken` for cooperative shutdown.** Pass it down, check it in loops and `select!`, and give children `child_token()` so a subtree can be cancelled alone.
- Document, for every public async function, whether it is cancel-safe.

### Tasks and their owners

**A spawned task belongs to something that waits for it.** A detached `tokio::spawn` whose
handle is dropped keeps running, its panic goes unnoticed, and shutdown cannot wait for it.

```rust
let mut tasks = JoinSet::new();
for job in jobs {
    tasks.spawn(process(job));
}
while let Some(joined) = tasks.join_next().await {
    match joined {
        Ok(Ok(report)) => reports.push(report),
        Ok(Err(error)) => return Err(error), // dropping the set aborts the rest
        Err(join_error) => return Err(Error::TaskPanicked(join_error)),
    }
}
```

- `JoinSet` aborts its remaining tasks when dropped, so an early return does not leak work. A `JoinError` is a panic or an abort; handle it, do not `unwrap` it.
- **Bound the fan-out.** A `Semaphore` permit per task, or `futures::stream::iter(jobs).map(f).buffer_unordered(limit)` when the futures need not be spawned.
- **`join!` and `try_join!` for a fixed, small set** of futures on the current task: no spawn, no `'static` bound, borrowing allowed. `tokio::spawn` when the work should run in parallel on other threads or outlive the caller.
- **A background task for the life of the service** is held by the component that starts it: store the `JoinHandle` and the cancellation token, and have `shutdown()` cancel and then await it with a time limit.
- **Carry trace context across the spawn.** Do it in the project's one spawn helper, so tasks inherit the caller's span by default.

```rust
tokio::spawn(work().instrument(tracing::Span::current()));

let span = tracing::Span::current();
tokio::task::spawn_blocking(move || span.in_scope(blocking_work));
```

- **Threads:** name them (`thread::Builder::new().name(...)`), join them, and prefer `std::thread::scope` when they only need to borrow local data for a bounded time.

**A supervisor fails in-flight jobs before it restarts the worker.** A worker that can crash
(a thread, a child process, a WASM instance) has a supervisor holding a registry of pending
replies.

```rust
struct Supervisor {
    in_flight: HashMap<JobId, oneshot::Sender<Result<Output, WorkerError>>>,
    consecutive_restarts: u32,
}

impl Supervisor {
    fn on_worker_exit(&mut self) -> Result<(), WorkerError> {
        for (_, reply) in self.in_flight.drain() {
            let _ = reply.send(Err(WorkerError::Crashed)); // the caller may have gone away
        }
        self.consecutive_restarts += 1;
        if self.consecutive_restarts > MAX_RESTARTS {
            return Err(WorkerError::GaveUp);
        }
        self.spawn_worker()
    }

    fn on_worker_ready(&mut self) {
        self.consecutive_restarts = 0; // only a successful start resets the count
    }
}
```

- **A clean error beats a future that never completes.** Jobs are failed, not replayed: only the caller knows whether a retry is safe.
- Restart with backoff and a cap. A worker that dies at start-up must not be restarted in a tight loop.
- Per-job resources are freed by an owning guard's `Drop`, so the crash path releases them too.

**A timeout does not mean the work stopped.** Dropping a timed-out future stops async work at
its next `.await`, but a `spawn_blocking` closure, a thread or a child process carries on.

```rust
match self.running.get(&job) {
    Some(handle) if !handle.is_finished() => return Tick::StillRunning, // skip this tick
    Some(_) => {
        self.running.remove(&job);
    }
    None => {}
}
let handle = tokio::task::spawn_blocking({
    let job = job.clone();
    move || run(job)
});
self.running.insert(job, handle);
```

- For a periodic job, skip the tick while the previous run is alive, or runs pile up on the same data.
- For work that must stop, give it a flag or token it checks, or run it in a child process that can be killed.
- Report "timed out, still running" differently from "failed".

### Tests and evidence

| Evidence | Choose it when | It does not show |
|---|---|---|
| Unit test | Behaviour is local and deterministic | That the parts work together |
| Integration test | Behaviour crosses a module, process or adapter boundary | Every edge case; too slow for that |
| Doctest | A public example is part of the contract | Anything about error paths, unless written |
| Compile-fail test (`trybuild`) | Misuse must not compile: typestate, `Send` bounds, lifetimes | Run-time behaviour |
| Property test (`proptest`) | An invariant or a round trip matters more than examples | That the stated property is the right one |
| Fuzzing (`cargo-fuzz`) | A parser, decoder or other frontier takes untrusted bytes | Semantic correctness; it finds panics, hangs and whatever you assert |
| `loom` | A small concurrent state machine built on atomics or locks | Anything about async I/O or large systems; the model must be tiny |
| Miri | Unsafe code, aliasing, uninitialised memory | Paths the tests do not execute; no FFI |
| Benchmark | A latency or memory threshold was stated | Production behaviour, unless the input is representative |
| Snapshot test (`insta`) | Output is large and structured: rendered text, plans, diagnostics | Correctness of the first snapshot; a person must read it |

- **Pick the rows at the start and record which ones the change triggers.** A matrix filled in after the code only justifies the evidence that already exists. Formatting, lints, tests and a build can all pass over a parser that was never fuzzed and a lock whose interleavings were never explored.
- **No threshold, no performance claim.** The benchmark row is owed only when a number was stated; without one, do not write "fast" in the report either.
- **Choose the smallest set that covers the risk,** not the largest that can be listed.
- **A missing test is written as missing.** An empty row marked "not covered" is honest; an invented test name is not.
- Coverage is a tool for finding untested code. It is not evidence that the tested code is right, and it is a poor target.

**The test-first loop.**

```text
STUB -> RED -> GREEN -> REFACTOR -> VERIFY
```

- **STUB.** Write the signature with a `todo!()` body, and the tests against it. At least one test per requirement.
- **RED.** Run it and *read the failure*. The first failure should be the missing behaviour. An unrelated compile error or a panic in the set-up means the test is not yet testing the thing. A test that has never failed has not been shown to test anything.
- **GREEN.** The least code that passes. Resist generalising here.
- **REFACTOR.** Improve names, decomposition and ownership with the tests green. No behaviour change in this step.
- **VERIFY.** Formatting, lints, the full test suite and a build, plus whichever rows from the table the change triggered.

For each requirement, cover three paths: the normal one, the error one, and an edge (empty,
one, maximum, boundary). State the empty case in the requirement itself: no matches is an empty
`Vec`, not an error and not `None`.

**When to apply it strictly, and when not.**

- *Strictly* for a bug fix (the failing test is the reproduction and stays as the regression test), for logic with a clear input-to-output contract, and for anything behind a public API.
- *Loosely* for exploratory work where the interface is not known yet: spike without tests, learn the shape, then throw the spike away or write the tests before it is merged. Do not let a spike become the implementation untested.
- *Not test-first* for pure wiring, generated code and thin adapters; an integration test afterwards covers them better than unit tests written in advance.
- Anti-pattern: writing the implementation, then writing tests that assert whatever it does. Those tests pin the bugs.
- Anti-pattern: changing the assertion to make a failing test pass, without first deciding whether the code or the test was wrong.

**Cheap checks before commit.** Search the added lines of the diff for `TODO`, `FIXME`,
`todo!`, `unimplemented!` and `dbg!`, and the added non-test lines for `.unwrap()` and
`.expect(`. Each hit is either removed or justified.

### Names

**A name says what the thing is or does at the call site,** in the vocabulary of the domain.
Length follows scope: a loop index may be `i`; a public function may not be `process`.

- **Follow the Rust API naming conventions:** `as_`, `to_`, `into_` by cost; `iter`, `iter_mut`, `into_iter`; `new` and `with_` constructors; `try_` for the fallible twin; `is_` and `has_` for predicates; getters without a `get_` prefix; `_mut` and `_unchecked` suffixes.
- **Casing:** `UpperCamelCase` types and traits, `snake_case` functions and modules, `SCREAMING_SNAKE_CASE` constants. Acronyms are words: `HttpClient`, `parse_url`. Crate names avoid `-rs` and `rust-`.
- **A name carries its unit when the type does not:** `timeout_ms`, `size_bytes`. Better, let the type carry it (`Duration`, a newtype).
- **Do not repeat the module in the item:** `cache::Config`, not `cache::CacheConfig`, unless items are usually imported bare.
- **One concept, one word.** If the code says `fetch`, `load` and `get` for the same operation, the reader assumes three operations.
- **Avoid names that say nothing:** `data`, `info`, `manager`, `helper`, `util`, `handle_it`, `do_work`.
- **Booleans read as assertions,** positively: `is_enabled`, not `not_disabled` or `flag`.
- **Follow the repository's own scheme where it has one.** Some codebases adopt a fixed pattern such as four-word `verb_constraint_target_qualifier` names (`filter_implementation_entities_only`). That is a local convention: apply it there, and nowhere else by default. Never count words where the result is a worse name.
- **A risky rename of a public item is done in two steps:** add the new name, deprecate the old with `#[deprecated(note = "use `new_name`")]`, and remove it in the next major version.

### Anti-patterns

This is the list to scan before handing work over. Each
has an exception, because the opposite mistake exists too.

### Reject by default

| Smell | Do instead | Legitimate exception |
|---|---|---|
| A requirement with nothing measurable ("make it faster") | A testable statement: input, expected result, threshold | Exploratory spikes, labelled as such and thrown away |
| A performance claim with no measurement | A benchmark, or a contract test that enforces the number | None; say "not measured" |
| `&Vec<T>`, `&String`, `&Box<T>` parameters | `&[T]`, `&str`, `&T` | You need `capacity()` or another method of the container itself |
| `anyhow::Error` or `Box<dyn Error>` in a library's public API | A typed error enum | Applications and binaries, where nobody matches on the error |
| `unwrap()` or `expect()` on a path input can reach | `?` and a typed error | A proven invariant, stated in the `expect` message; tests |
| Blocking work on an async executor | `spawn_blocking`, a dedicated thread, or an async API | Work bounded well under a millisecond |
| A lock guard or `RefCell` borrow held across `.await` | Copy out and drop the guard; or an async mutex where the await is the point | An async mutex guarding an I/O resource that must be used serially |
| An unbounded channel or queue | A bound, plus a stated policy when full | A provably bounded producer, with the proof in a comment |
| A spawned task with no owner | `JoinSet` or a supervisor; a cancellation path; observed failures | None in a long-running service |
| Concurrency never exercised under contention | Stress tests, `loom` for small lock-free cores, TSan | Code that is trivially confined to one thread |
| Text handling that assumes UTF-8, or one byte per character | `&[u8]`, `OsStr`, `Path`; `char_indices` for boundaries | Input already validated as `str` |
| I/O, runtime or framework types in the core domain | Pure core; adapters at the edge | Small programs where the split would be the bulk of the code |
| A struct holding the concrete database or HTTP client it uses | Depend on a narrow trait or pass a function; construct at the edge | The adapter itself |
| A "manager" struct with twenty fields | Split by responsibility and by what changes together | A plain configuration record |
| A domain model that ignores real cases | Model the cases the input actually has, or reject them explicitly | A stated, enforced subset |
| A public enum that will grow, without `#[non_exhaustive]` | Add it before the first release | Enums that are closed by definition |
| A diagnostic that drops the location | Carry file, line, column or byte span through to the message | None |
| Tests that only replay examples | Add the invariant: a property test, a round trip, a boundary table | Glue code with no invariant to state |
| Generic "so we can swap it later" | One concrete implementation; abstract at the second real use | A boundary you must fake in tests today |

A note on resource leaks: Rust closes files, sockets and locks when their owner is dropped,
so "forgot to close" is rare. The leaks that do happen are tasks and threads nobody joins,
child processes nobody waits for, temporary files, `Rc` or `Arc` cycles, entries never
removed from a long-lived map, and anything whose clean-up is async and so cannot run in
`Drop`.

### Subtler ones

- **Borrowing by habit.** Lifetimes threaded through a design, or clones hidden inside, only to avoid taking ownership of data the callee keeps anyway. If it is stored, moved to a task or outlives the call, take it owned.
- **Recovery logic keyed on message text.** Retry or fallback chosen by a substring of an error message breaks silently when the wording or a wrapper changes. Match typed variants or a retryability method.
- **The kitchen-sink error enum.** One public enum with a variant per dependency and a catch-all string. Callers cannot tell what is actionable, and every internal change is an API change. Use errors local to each boundary, expressed in that boundary's terms.
- **Dependency types in a public API.** A dependency upgrade becomes your breaking change. Wrap them. *Exception:* crates whose purpose is to extend that dependency, and vocabulary crates such as `bytes`, `http` or `serde`.
- **Trait and module sprawl.** Tiny traits and wrappers that exist to look abstract. A seam belongs at a real external or semantic boundary.
- **Accumulator soup.** Nested loops with pushes, flags and branch-specific state. Use an iterator chain or small named helpers. Keep the loop when control flow is heavy (early exits, `?`, several outputs) and the chain would be harder to read.
- **A mutable configuration blob,** patched by many call sites before use, so validity depends on timing. Validate once and hand out a frozen value.
- **A build that works only by folklore:** undocumented features, a remembered toolchain, commands that work only from one directory. Pin the toolchain, keep features additive, and run the gates from the workspace root.
- **Transport types used as domain types.** When handlers, services and storage share one DTO, every layer re-decides what is valid. Convert at the edge.
- **Speculative `unsafe` or lock-free code.** Build the safe version, measure, and only then narrow `unsafe` to the proven hot spot, with a proof plan.
- **"It compiles" offered as proof of behaviour.** The compiler proves memory and thread safety, not logic, liveness, ordering or performance. Each of those needs its own evidence.
- **Hand-edited generated code.** Regeneration discards the edit. Change the schema, the generator configuration or a wrapper module.
- **Broad desktop privilege:** wide filesystem grants, generic shell access, sidecar processes with no owner or health check. Running on the user's own machine is not an exception.
- **Hazards a signature does not show:** a guard kept alive by an iterator or a temporary in a `match` scrutinee; an `Arc` cycle; a new trait method that breaks object safety; a new auto-trait-breaking field (`Rc`, a raw pointer) that silently removes `Send` from a public type.

### Mistakes in applying this list

- **Over-correcting.** Removing every clone, making every `&str` parameter `impl AsRef<str>`, giving every function its own error enum, adding a trait to mock one call. A clone is right when it makes ownership clear and the cost is unmeasured or small. Fix the instance that hurts.
- **Fixing the symptom.** Similar symptoms need opposite fixes: a borrow error may want a clone, a restructured scope, or a different owner. Reproduce the failure in the smallest case, confirm the mechanism, then change the code. Adding a clone, a retry, a lock or a trait before that is guessing.
- **Moving a cost instead of removing it.** A convenience in one function often transfers a panic, an allocation, a queue or a compatibility burden to callers and operators. Ask who pays now.
- **The unnamed shortcut.** A design that deliberately avoids a tempting default (a clone per call, `Arc<Mutex<_>>` around everything, `Box<dyn Error>` in a public API) says so at the boundary. Otherwise the next change puts it back.
<!-- essentials:end -->

<!-- core:begin -->
## Working rules shared by every Rust skill

This block is the same in every Rust skill. It covers how to work, the gates, and what
"done" means. Where the repository you are in has its own convention or gate, that wins.

**If nothing else is in reach:**

1. **Say what "correct" means before writing code,** in terms something can check.
2. **Put invariants in types** where that is cheap, and in tests where it is not.
3. **Make ownership, errors, cancellation and shutdown deliberate.** Each should be a decision someone can point to.
4. **Bound everything that can grow:** queues, buffers, retries, recursion, waits, output.
5. **Treat everything from outside the process as untrusted** until it has been parsed into a type that cannot hold the invalid form.
6. **Measure before optimising, and state the method with the number.**
7. **Follow the repository you are in** over any general convention, this skill included.
8. **Report what you ran and what you saw.** Unverified is a legitimate status; passing it off as verified is not.

### Size the process to the task

| Task | Process that fits |
|---|---|
| Rename, comment, one-line fix covered by an existing test | Read the code and its callers, change it, run the gates |
| Bug fix | Reproduce it with a failing test, fix, run the gates |
| Feature inside one module | A short list of checkable requirements, tests first, implement |
| New public API, a change that crosses a boundary, concurrency, unsafe | Requirements, design of types and boundaries, a chosen test mix, then code |

Process heavier than the task buries the change the reviewer has to check. Process lighter
than the task is how a "small" change to an error type or a lock ships a regression.

### Working with the compiler and the ecosystem

- **Fix the first error first.** Later errors are often cascades. Read the whole message, including the `help:` and `note:` lines. Run `cargo check` after each small edit, not after three hundred lines.
- **A borrow-checker error is design information.** Before adding `.clone()`, `Rc<RefCell<_>>`, `Arc<Mutex<_>>` or `'static` to make it compile, say who owns the value and how long the borrow must live. A clone is fine when the value is small or the path is cold; it is wrong when it silently forks state that was meant to be shared.
- **Never guess an API.** Find the version in `Cargo.lock`, then read the documentation for that version or the source under `~/.cargo/registry/src`. Widely used crates change shape between major versions, and code remembered from one version fails on another.
- **Check the edition and the minimum Rust version** (`edition` and `rust-version` in `Cargo.toml`) before using a newer language feature.
- **Match the codebase.** Use its error crate, runtime, logging, naming and module layout. A second way of doing the same thing is a cost every later reader pays.
- **Keep the diff to the task.** No drive-by reformatting, renames or dependency upgrades. Report what you noticed; do not fix it uninvited.
- **Add a dependency deliberately.** Check that std or an existing dependency does not already do it, look at maintenance and licence, enable only the features needed, and say in the handover that you added it.
- **Read before you write.** Read the function you change, its callers and its tests.
- **A red test must be red for the right reason:** it fails on the assertion, not on a compile error or a set-up mistake.
- **Debug in a loop with a stop condition.** Reduce to the smallest reproduction, test one hypothesis per probe, and stop when a regression test fails for the confirmed cause. A plausible story is not a diagnosis.

### What the compiler does not prove

- It proves memory and type properties. It proves nothing about domain correctness, performance, cancellation behaviour or compatibility.
- Code that compiles with clones everywhere has not shown the clones are right.
- No data race does not mean no logical race: check-then-act across two lock acquisitions, dropped work and stale reads all compile.

### The required gates

Cheapest first, so the fastest check fails first:

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-targets --all-features
cargo test --workspace --doc --all-features
```

- **Use the repository's own gate if it has one** (a `just` or `make` target, a CI script). These commands are the default when there is none.
- **`--all-targets` does not run doc tests.** They need the separate `--doc` run.
- **Clippy without `-D warnings` is not the gate.** It prints and passes.
- **`--all-features` is wrong for crates with mutually exclusive features.** Test the supported combinations explicitly.
- Run from the workspace root you mean. A command run in one member checks that member only.
- **A zero exit code can hide tests that did not run.** Read the count: how many ran, how many were ignored or filtered out.

Run a heavier gate when the change touches its risk, and say so when you skip one:

| Gate | Run it when |
|---|---|
| `cargo test --release` | Behaviour could differ with optimisation: overflow checks, `debug_assert`, timing, unsafe code |
| `cargo +nightly miri test` | Unsafe code changed |
| `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps` | Public items or documentation changed |
| `cargo deny check` or `cargo audit` | Dependencies changed |
| `cargo semver-checks` | A published library's public interface changed |
| Benchmarks against a baseline | A performance claim is made, or a hot path changed |

### Before claiming done

1. Identify the command that would prove the claim.
2. Run it fresh and in full, after the last edit.
3. Read the output and the exit status.
4. Report what happened, and only then say done or not done.

- **"It compiles" is not done.** Done is: the required gates green on the final code, and the claimed behaviour covered by tests.
- **If you could not run a command, say so and list it for a human.** Never report an unrun command as passed, and never describe output you did not see. "Skipped" is not "passed".
- **Do not weaken a check to make it pass:** no deleted or `#[ignore]`d test, no loosened assertion, no blanket `#[allow]`, no special case for the test's input. If a test is wrong, say so and fix the test as its own visible change.
- **Before handoff, search your own diff** for `todo!()`, `unimplemented!()`, `dbg!`, stray `println!`, commented-out code and placeholder `TODO` markers.
- **Never invent an identifier, a number or a citation** to satisfy a checklist. If an item does not apply, say why.
- **No secret reaches a log, an error message or a `Debug` output.** No compiler checks this; look at debug, error and crash paths.

**The record at handoff:** the commands run, their results and the toolchain version;
which heavier gates ran or were skipped, with the reason; what was verified by test, what
by reading, and what not at all; known limitations and anything left for a human.
<!-- core:end -->
