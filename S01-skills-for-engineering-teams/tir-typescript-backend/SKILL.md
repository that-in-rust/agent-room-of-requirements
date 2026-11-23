---
name: tir-typescript-backend
description: >-
  Reliability-first TypeScript for shared libraries, Node/Bun/Deno back ends and classic
  MERN applications (React + Express + Mongoose + MongoDB): parse every input at the
  boundary, brand identifiers, keep expected failures in signatures, propagate deadlines
  and cancellation, make writes idempotent, use safe Mongoose read and write paths, and
  prove the result with typecheck, lint and boundary tests. Use when the task touches
  .ts, .mts, .cts or tsconfig.json; Express routes, middleware, controllers or services;
  Mongoose models and queries; webhooks, queue consumers, cron jobs, workers or CLIs; env
  and config bootstrapping; or when asked to "validate this request", "harden this API",
  "add strict mode", "why does this retry create duplicates", "fix pagination", "review
  this Node service" or "make this handler cancellable". Not for React component,
  rendering or Three.js work beyond the server-state and form contract (use the
  react-frontend skill), Next.js App Router or GraphQL-first doctrine, WebSocket-heavy
  real-time systems, sharded or multi-region MongoDB, cross-service sagas and
  distributed transactions, bundler or deployment setup, or Python, Kotlin and Rust code.
---

# TypeScript Backend Reliability

## Purpose

This skill makes TypeScript code survive bad inputs, schema drift, retries, timeouts and
old stored data. It does that by making every IO boundary explicit: data enters as
`unknown`, is parsed once, and travels inward as typed values, while failures, deadlines
and database semantics stay visible in the code.

Two sentences carry the whole skill:

- **Treat the type system as a guardrail, not a costume.** Every type claim is backed by
  compilation or by parsing.
- **Make IO lies impossible to ignore.** TypeScript is erased at runtime, so every JSON
  body, token, query string, env var, queue payload, stored document and provider
  response must re-establish trust.

This is not a TypeScript tutorial. It is a gate and a router: it names the risks, the
rules that close them, and the commands that prove the result.

## When to use

- `.ts`, `.mts`, `.cts` or `tsconfig.json` work where correctness matters more than style.
- HTTP handlers, RPC endpoints, webhooks, queue consumers, cron jobs, workers and CLIs on
  Node.js, Bun, Deno, serverless or edge runtimes.
- Config and env bootstrapping, transport adapters, provider clients, repositories and
  service layers.
- Shared domain models, schema codecs, serialization, persistence, stream and event
  handling, protocol types.
- Classic REST-style MERN work: Express routes, Mongoose queries and writes, MongoDB
  modelling and indexes, auth routes, and the client data contract (forms, query layer).
- Reviews where the real question is whether the code stays correct under malformed
  input, retries, timeouts, storage drift or a teammate's later change.

Requests that should trigger this skill:

1. "Add a `POST /orders` endpoint to our Express API and make sure bad payloads never
   reach Mongoose."
2. "Our Stripe-style webhook handler sometimes creates two records. Find out why and fix
   it."
3. "Turn on strict mode in this shared package without breaking its consumers."
4. "Review `user.service.ts`. It uses `findByIdAndUpdate` everywhere. Is that safe?"
5. "The list endpoint shows duplicates on page 3. Fix the pagination."

Requests that should not trigger it:

1. "Split this React component and fix its re-renders." That is component work; use the
   `react-frontend` skill. Only the server-state, form-schema and request-mocking rules
   live here.
2. "Design a saga across the billing and inventory services." Cross-service consistency
   needs outbox, saga and idempotent-consumer machinery; this skill stops at one service.
3. "Configure webpack and the Docker image." Bundler and deployment setup beyond
   `tsconfig` is not covered. Say so instead of stretching these rules.

When part of a task belongs to another skill, hand off one named, disputed decision, not
a keyword. Carry the workflow, the contracts, the evidence, the failed gate, the
constraints, the answer you expect and the condition for coming back. Reconcile any
returned contract or test change here. If the same decision bounces between owners
without new evidence, stop routing and decide it or escalate to one named owner.

## Pick the mode

The subject spans three bodies of guidance. Classify the task first, then load the
matching mode. Modes stack: MERN work uses all three.

| Mode | Pick it when | Section |
| --- | --- | --- |
| L. Language baseline | Any `.ts` or `tsconfig.json` change; shared libraries; types, unions, casts, module imports, persisted shapes | [Mode L](#mode-l-typescript-language-baseline) |
| B. Backend service | The code receives or sends IO: requests, events, env, queues, provider calls, storage; retries and timeouts matter | [Mode B](#mode-b-backend-services) |
| M. MERN stack | Express + Mongoose + MongoDB, with or without the React client | [Mode M](#mode-m-mern-stack) |

Mode L is the baseline for B and M. Do not re-debate it there. A two-function endpoint
may skip ports and adapters; it may not skip parsing or idempotency.

## Workflow

1. **State the visible behaviour.** Name the success state and the failure states the
   caller or user can see: validation, authorization, not found, conflict, dependency
   timeout, retry, empty.
2. **Classify the boundary.** One of: request contract, env/config, provider or transport
   adapter, queue or cron input, service invariant, Mongoose read, Mongoose write,
   MongoDB model or index, auth and security, client server-state, observability,
   language-only (types, modules, persistence shape).
3. **Map the path.** Trace one action end to end: client form → network → server schema →
   authorization → service invariant → database operation → response envelope → client
   cache update → UI state → logs → rollback. A strong layer cannot repair an unvalidated
   one next to it.
4. **Inspect the repository.** Read its `tsconfig.json`, lockfile, lint config, test
   runner, validator library and existing conventions. Follow stronger local conventions.
   Deviate from them only when they reduce a reliability property this skill protects.
5. **Select the smallest set of patterns that closes the failure path.** Apply in this
   order: schema-first parsing, branded IDs, explicit result errors, deadline
   propagation, transport normalization, ports and adapters, idempotent mutation
   boundaries. Scores in the reference are ordering aids, not measurements; an idempotency
   rule can outrank a higher-scored pattern on a payment path.
6. **Ask the skeptical question** of each new piece of code: what happens when the input
   is malformed, old, partial, cancelled or missing?
7. **Write the boundary test first**, at the real boundary (HTTP contract, repository
   against a real database, recorded webhook envelope), then implement. Writing the
   happy-path handler before the parser is the usual way parsing gets skipped.
8. **Keep the core framework-light.** HTTP, queue, database and provider quirks belong in
   adapters. The core takes typed commands and returns typed results.
9. **Run the gates** (see [Quality gates](#quality-gates)) with the repository's own
   commands. Record command, working directory and exit status.
10. **Sweep the anti-patterns**, then hand back the output contract. If you deviated from
    a rule, say why and show how the same reliability property is preserved another way.
    Stop and ask when ownership is missing or a change is irreversible (schema migration,
    token format, multi-system contract).

## Rules

### Boundaries

- Everything from the network, env, file system, local storage, browser APIs, worker
  messages, queue payloads, cron inputs and provider SDKs enters as `unknown`.
- Define the schema once, infer the type from it (`z.infer`), parse at the boundary, pass
  typed data inward. Never write an interface for external data and call it done.
- Validate `req.body`, `req.params` and `req.query` at the server edge even when the
  client validates. Client validation is UX help, not a trust boundary and not
  authorization.
- Reject unknown or malformed shapes before any side effect.
- Parse env at boot and crash if it is invalid. Do not defer env parsing to the first
  request.
- Never let raw `req.body` travel through the app, and never pass it to a Mongoose call.
- Keep entity types, DTOs, commands and API response wrappers distinct. Do not reuse one
  `User` shape for the database document, the request and the response.
- In a repository with client and server code, keep DTOs, validation schemas and API
  contracts in a shared layer. Separate client and server schemas are acceptable only
  when ownership and drift tests are clearer than a shared package.

### Types and modules

- Compile with the strict baseline in [tsconfig baseline](#tsconfig-baseline). If a flag
  costs one extra line today and prevents a production bug later, keep the flag.
- Use `import type` for type-only imports. Runtime imports mean runtime behaviour.
- `any` at a trust boundary is forbidden. Treat every `any`, cast and lint suppression as
  a documented hole.
- Proof ladder, in order of preference: `satisfies` → schema parsing → branded
  constructor → cast. A cast is an escape hatch: fence it tightly and write why. "Never
  cast" is too absolute; "fence and explain" alone is a licence for duct tape.
- Use `satisfies` for config tables, route manifests and action maps. Use `as const` or
  `const` type parameters when the exact set of keys or values is part of the contract.
- Brand IDs and other scalars that must never be swapped: primary keys, tenant and
  workspace IDs, idempotency keys, message and job IDs. Brand at the domain edge. Skip
  the ceremony for a value used inside one function.
- Hand-written types are fine where there is no runtime boundary.

### Control flow

- Model protocol states, events, async results and UI state as discriminated unions.
  Prefer one union over three loosely related booleans.
- Handle unions with an exhaustive `switch` and a `never` check in the default branch.
- Use assertion functions for invariants. Use schema parsing for untrusted input.

### Errors

- Return an explicit `Result` for expected, recoverable outcomes (validation, conflict,
  not found, business rule). Throw for programmer mistakes, impossible states and
  invariant violations. The test is expectedness. Do not wrap pure maths in `Result`.
- Narrow caught values from `unknown` before use.
- In Express, async errors must reach `next(err)`. One error middleware, registered last,
  normalizes every error. If headers are already sent, delegate to Express.
- Normalize unique-index, cast and not-found errors into stable response shapes. Return
  generic credential errors on auth routes.

### Async, deadlines and retries

- Every async boundary accepts an `AbortSignal`, composes it with its own deadline and
  passes it down. Answer three questions: who can cancel this, how long can it run, and
  what happens downstream when it aborts?
- A timer that rejects while the work continues is not a timeout. Never time out without
  aborting.
- Retry only transient failures: network hiccups, a temporary `429`, short upstream
  unavailability. Never retry validation failures, auth failures or writes without an
  idempotency key.
- Make writes idempotent before adding retries. The key must come from the client or the
  message (client message ID, provider delivery ID). A server-generated key deduplicates
  nothing. A queue consumer checks the delivery ID before it writes.
- One layer owns retries. Do not stack client-library retries on top of HTTP-client
  retries. Use backoff with jitter and stay inside the caller's deadline.

### Persistence

- Treat persisted JSON as a public contract with your future self. Version the stored
  shape, migrate lazily on read, preserve unknown future keys, and merge partial state
  with defaults recursively. `undefined` means missing; `null` means intentionally empty.
- Mongoose reads: explicit projection, `lean()` unless document behaviour is needed,
  selective `populate`, deterministic sort with a unique tiebreaker, cursor or range
  pagination for growing collections.
- Mongoose writes: prefer load → mutate → `save()`. Use query-style updates only for
  atomic transitions, with explicit operators and `runValidators: true`.
- `unique: true` is an index helper, not a validator. Indexes are part of the model.
- Use a session and `withTransaction()` only when several documents must move together.
  No `Promise.all()` inside a transaction. No nested transactions on one session.

### Architecture and tests

- Three layers: core (domain types, invariants, pure functions), application (use cases,
  ports), adapters (HTTP, database, queues, providers). Frameworks plug into the core.
- Provider-specific shapes stop in the adapter. Application code does not know which
  provider produced a payload.
- Test behaviour, not internals: unit tests for pure logic, integration tests for
  repositories and adapters, HTTP contract tests for handlers, end-to-end tests for
  critical journeys. Mock only one layer below the thing under test. Weight adapter and
  contract tests over unit tests; the adapter boundary is where typed code meets reality.
- Use project references only when the repository is large enough that boundaries need
  compiler support. Small repos do not need them.

## Mode L: TypeScript language baseline

Use for any TypeScript change. Patterns come in three tiers. Adopt tier S wholesale,
evaluate tier A per codebase, use tier B only when its trigger appears. Do not flatten
the tiers, and do not apply the whole list to a 50-line script.

- **Tier S (adopt by default):** strict compiler flags; `import type` hygiene;
  schema-first boundary parsing; `unknown` until proven typed; exhaustive unions;
  `satisfies` for config contracts; assertion-function narrowing; behaviour-first test
  pyramid.
- **Tier A (strong defaults):** typed transport normalization; versioned persistence
  migration; branded identifiers; deep merge for forward compatibility; schema-validated
  forms; explicit result errors; `AbortSignal` deadline propagation; feature-collocated
  query layer; literal exactness preservation; layered boundary adapters.
- **Tier B (when triggered):** project-reference build partitions (large repo, slow
  typecheck); quota-aware storage degradation (browser storage only); stable-key stream
  state machines (streaming or event-heavy protocols); progressive enhancement with a
  minimal client (browser journeys only).

Hardening an existing loosely typed package, in dependency order:

1. Enable strict flags per file or module cohort. Ratchet the error count down; do not
   turn flags back off. Enabling strict mode and then reverting it is a failure.
2. Convert boundaries to schemas and infer the contracts from them.
3. Replace boolean state with discriminated unions plus `never` checks.
4. Brand identifiers.
5. Version persisted shapes.
6. Install the merge gate.

Narrower or renamed exports change the public API. Own the consumers or plan a semver
bump. In a large repository keep a strictness ledger beside `tsconfig.json`: one row per
module cohort with strictness state, boundary-parse coverage, union exhaustiveness, cast
inventory (with justification and removal trigger) and gate compliance.

Naming: prefer four semantic segments so a name says what, on what, and how safely:
`parseUserProfileSafely`, `handleStreamEventExhaustively`,
`normalizeProviderResponseStrictly`, `mergePersistedStateForward`. For important flows,
write the contract first: preconditions, postconditions, error conditions, verification
path (see [../executable-specs/SKILL.md](../tir-executable-specs/SKILL.md)). Diagrams, when
needed, are Mermaid.

Version notes: assertion functions need TypeScript 3.7, `import type` 3.8, `satisfies`
4.9, `verbatimModuleSyntax` and `const` type parameters 5.0. Check the repository's
compiler version before using them. JavaScript with JSDoc can adopt the boundary rules
but not the compiler flags.

## Mode B: Backend services

Use for APIs, workers, queues, CLIs and long-running services. The failure modes are
invalid inbound data, mixed-up identifiers, hidden transport drift, timeout and
cancellation bugs, retry and idempotency mistakes, and storage and config evolution.

Five habits, if nothing else is remembered:

1. Parse all inbound data.
2. Brand all important IDs.
3. Model recoverable failures explicitly.
4. Propagate cancellation and deadlines.
5. Keep adapters outside the core.

Keep a boundary inventory beside each service, one row per endpoint, queue, cron job and
env seam, and update it in every change that adds or alters a seam:

| Seam | Parse schema | Branded types | Error union | Deadline source | Idempotency key | Test layer |
| --- | --- | --- | --- | --- | --- | --- |
| `POST /users` | `createUserRequestSchema` | `UserId` | `CreateUserError` | request signal + 2 s | `Idempotency-Key` header | HTTP contract |
| env at boot | `environmentSchema` | none | throws at boot | n/a | n/a | unit |

Route-table generators miss env reads and cron jobs. The inventory makes forgotten admin
endpoints and startup env reads visible.

Webhook recipe: parse the envelope at the edge; brand the extracted IDs; normalize
provider event names into a domain union; put ports around the use case; key the write
with the provider delivery ID; propagate the request deadline; add contract tests against
recorded envelopes. Assume redelivery even when the provider does not document it. The
step most often skipped is normalization.

The same rules scale down to a CLI: parse `argv`, brand paths, return `Result` failures,
bound the runtime. Edge and serverless functions multiply the number of boundaries while
shrinking the code; each one still parses.

Runtime note: the examples use zod, `AbortSignal.timeout` and `AbortSignal.any`. Older
runtimes may lack `AbortSignal.any`. Re-express the pattern with an `AbortController` or
polyfill it deliberately; do not drop the principle. Another validator is fine if
schema-inferred types and one boundary parse remain.

## Mode M: MERN stack

Use for classic React + Express + Mongoose + MongoDB applications: CRUD systems,
dashboards, internal tools, line-of-business products, auth-backed consumer apps. Treat
it as partial guidance for Next.js App Router, GraphQL-first, WebSocket-heavy,
queue-heavy, search-heavy or sharded systems.

Classify into a bucket, then apply the matching defaults.

**Read endpoints**

- Validate `params` and `query`.
- Use explicit projection.
- Use `lean()` unless document methods, getters, setters, virtuals or `save()` are needed.
- Keep `populate` selective: only the fields the response needs. No auto-populate of
  large relation graphs.
- Sort deterministically with a unique tiebreaker such as `_id`.
- Prefer cursor or range pagination for growing lists. Keep page contract, sort contract
  and indexes aligned.

**Write endpoints**

- Validate `body` at the route boundary and map it to a command.
- Prefer load → mutate → `save()` for document logic: middleware, validation and version
  tracking run where expected.
- If an atomic query-style update is required, use explicit operators (`$set`, `$inc`)
  and `runValidators: true`, and test the concurrent case.
- Turn on `optimisticConcurrency` when stale concurrent writes matter. Do not disable
  `versionKey` casually; version keys move through `save()`, not generic updates.
- Use transactions only when several documents must move together, never as a substitute
  for a bad model.
- Normalize unique-index and not-found errors into stable response shapes.

**Auth endpoints**

- Rate-limit login, password reset, OTP verify and invitation accept more tightly than
  the rest of the API.
- Hash passwords with Argon2id, or a carefully configured fallback (scrypt, then bcrypt).
  Never plain text, never SHA-256, never a synchronous hash inside a request handler.
- Return generic credential errors.
- With cookie auth, set `httpOnly`, `secure` and an explicit `sameSite`.

**App bootstrap**

- `helmet()`, an explicit CORS origin list (not `*` by reflex), `x-powered-by` disabled.
- Health endpoint; on `SIGTERM` stop accepting work, finish in-flight requests, close the
  database connection.
- One request ID per request, carried through async work with `AsyncLocalStorage`.

**MongoDB modelling**

- Embed when data is queried together, updated together and small and bounded.
  Reference when child cardinality is high, the embedded data grows without bound, or
  duplicated data is too hard to keep consistent.
- Compound indexes for real query shapes, partial indexes when only a subset matters,
  unique indexes for invariants the database must enforce.
- Once the shape stabilizes, add collection-level schema validation to critical
  collections as a backstop for scripts, admin tools and side channels.

**Client data flow**

- TanStack Query for server state; a small local or global store only for client UI
  state. Query keys are part of the contract surface.
- React Hook Form + Zod for forms. Share the schema concept with the server; never trust
  the client copy.
- Each feature owns its API layer, query keys and types. The app shell imports features;
  features import shared code, not each other.
- MSW at the network layer for tests and local development; Testing Library queries by
  role and label; assert what the user can observe.
- Error boundary per route segment, reset on navigation, with a deliberate retry action.
- Persisted client state is versioned and migratable. Subscribe to stores by slice.
- Component-level depth belongs to the `react-frontend` skill.

**Baseline stack** when starting fresh: React + TypeScript strict; TanStack Query; a small
Zustand store; React Hook Form + Zod; MSW + Testing Library + Vitest; Express with
validated boundaries and centralized async errors; `helmet()` and explicit CORS;
route-specific auth throttling; Mongoose models that prefer `save()` and explicit
sessions; `lean()` on read paths; query-style updates only with explicit validation
intent; indexes designed from query patterns; collection-level validation for critical
collections; request correlation IDs in logs.

**Deliberately not defaults:** Next.js client/server directives and server actions (not
classic MERN); optimistic-update hooks (easy to misuse without rollback and
reconciliation); Suspense-integrated query hooks; monorepo workspace config (developer
experience, not reliability); autopopulate plugins; offset pagination as the default.

## Where sources disagree

Keep both positions. The selector says which applies.

| Topic | Position A | Position B | What selects |
| --- | --- | --- | --- |
| Request validation library | Zod, types inferred from the schema | Yup with `abortEarly: false`, errors mapped to `{field, message}` | New code: Zod. Existing Yup codebase: keep Yup unless the task is a migration; the rule is one schema parsed at the edge. |
| Client server-state | TanStack Query plus a small store | Redux Toolkit with async thunks | New code: TanStack Query. Keep a Redux flow only when migration risk exceeds the reliability cost and contract tests guard it. |
| Token storage | `httpOnly`, `secure`, `sameSite` cookies | Bearer token read from `localStorage` with a refresh interceptor | Decide by threat model. The `localStorage` form is a legacy example; do not adopt it as a default. |
| Password hashing | Argon2id first, scrypt fallback | bcrypt with cost 12 in a pre-save hook | New code: Argon2id. Existing bcrypt hashes are acceptable when configured correctly and hashed asynchronously. |
| Pagination | Cursor or range with `(createdAt, _id)` | `skip`/`limit` with `countDocuments` and `totalPages` | Offset is fine for a small, fixed admin list with a deterministic sort and a documented size bound. Everything that grows uses cursors. |
| Updates | load → mutate → `save()` | `findByIdAndUpdate` with `{ new: true, runValidators: true }` | `save()` when middleware, optimistic concurrency or document semantics matter; query update for a true atomic transition, with operators, validators and a concurrency test. |
| Auth rate limit | 10 requests per 15 minutes on auth routes | 5 per 15 minutes skipping successful requests, 3 per hour for password reset, 100 per 15 minutes general | Both are starting values, not measured thresholds. Tune to the threat model; use a shared store (Redis) when there is more than one instance. |
| 500 response body | Error message returned to the caller | Details hidden in production, stack only in development | Production services hide internals. The message form is for development and internal tools. |
| Pattern scores | Language baseline: result errors 90, branded IDs 92, deadlines 91 | Backend: 95, 94, 94 | Context. The same pattern matters more at an API boundary. Do not compare scores across lists. |
| Shared schema | One schema package feeds client and server | Separate client and server schemas | Shared by default. Separate only with clear ownership and drift tests. |

When the selector lands on the legacy or borderline position (a kept Redux flow, a
`localStorage` token, offset pagination, a query-style update), record two things with
it: the containment that stops it spreading (contract tests, a size bound, a concurrency
test) and an expiry, meaning the date or condition at which it is revisited or removed.

## Templates and commands

### tsconfig baseline

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noFallthroughCasesInSwitch": true,
    "useUnknownInCatchVariables": true,
    "verbatimModuleSyntax": true,
    "noUncheckedSideEffectImports": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "isolatedModules": true,
    "moduleDetection": "force"
  }
}
```

### Boundary schema, branded ID, result error

```typescript
import { z } from "zod";

const createUserRequestSchema = z.object({
  email: z.string().email(),
  displayName: z.string().min(2).max(80),
});
type CreateUserRequest = z.infer<typeof createUserRequestSchema>;

declare const userIdBrand: unique symbol;
export type UserId = string & { readonly [userIdBrand]: "UserId" };

export function createUserIdSafely(raw: string): UserId {
  if (!isValidUuid(raw)) throw new Error("Invalid user id");
  return raw as UserId; // the one fenced cast: the check above is the proof
}

type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

type CreateUserError =
  | { type: "email-already-exists" }
  | { type: "invalid-request"; messages: string[] };

export async function createUserWithResult(
  input: unknown,
): Promise<Result<UserId, CreateUserError>> {
  const parsed = createUserRequestSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: { type: "invalid-request", messages: parsed.error.issues.map((i) => i.message) },
    };
  }
  const existing = await findUserByEmail(parsed.data.email);
  if (existing) return { ok: false, error: { type: "email-already-exists" } };
  return { ok: true, value: await insertUserRecord(parsed.data) };
}
```

### Env at boot

```typescript
const environmentSchema = z.object({
  NODE_ENV: z.enum(["development", "test", "production"]),
  PORT: z.coerce.number().int().min(1).max(65535),
  DATABASE_URL: z.string().min(1),
  JWT_SECRET: z.string().min(32),
});
export const environmentConfig = environmentSchema.parse(process.env);
```

### Exhaustive union

```typescript
function assertExhaustiveCaseNever(value: never): never {
  throw new Error(`Unhandled case: ${JSON.stringify(value)}`);
}

switch (event.type) {
  case "text": appendTextChunk(event.text); return;
  case "done": finishActiveStream(event.finishReason); return;
  default: assertExhaustiveCaseNever(event);
}
```

### Deadline and cancellation

```typescript
export async function fetchJsonWithDeadline<T>(
  url: string,
  decode: (input: unknown) => T,
  options: { signal?: AbortSignal; timeoutMs?: number } = {},
): Promise<T> {
  const deadline =
    options.timeoutMs === undefined ? undefined : AbortSignal.timeout(options.timeoutMs);
  const signal =
    options.signal && deadline
      ? AbortSignal.any([options.signal, deadline])
      : options.signal ?? deadline;
  const response = await fetch(url, { signal });
  return decode(await response.json()); // parse, do not cast
}
```

### Express: validate, centralize errors, harden, correlate, shut down

```typescript
import { AsyncLocalStorage } from "node:async_hooks";
import crypto from "node:crypto";
import cors from "cors";
import express, { type NextFunction, type Request, type Response } from "express";
import { rateLimit } from "express-rate-limit";
import helmet from "helmet";
import mongoose from "mongoose";

const app = express();
app.use(express.json());

export function validateCreateUserRequest(req: Request, res: Response, next: NextFunction) {
  const parsed = createUserBodySchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: "Invalid request body", details: parsed.error.flatten() });
  }
  req.body = parsed.data;
  next();
}

app.disable("x-powered-by");
app.use(helmet());
app.use(cors({ origin: ["https://app.example.com"], credentials: true }));

const requestContext = new AsyncLocalStorage<{ requestId: string }>();
app.use((_req, _res, next) => requestContext.run({ requestId: crypto.randomUUID() }, next));

app.use("/auth/login", rateLimit({ windowMs: 15 * 60 * 1000, max: 10, standardHeaders: true, legacyHeaders: false }));

app.get("/users/:id", async (req, res, next) => {
  try { res.json(await getUserById(req.params.id)); } catch (error) { next(error); }
});

app.get("/healthz", (_req, res) => res.status(200).json({ ok: true }));

// last in the chain
app.use((err: unknown, _req: Request, res: Response, next: NextFunction) => {
  if (res.headersSent) return next(err);
  res.status(500).json({ error: "Internal Server Error" });
});

const server = app.listen(port);
process.on("SIGTERM", () => {
  server.close(async () => { await mongoose.connection.close(); process.exit(0); });
});
```

### Mongoose: read, update, transaction, cursor page, indexes

```typescript
const users = await User.find({ organizationId })
  .select("name email role createdAt")
  .sort({ createdAt: -1, _id: -1 })
  .limit(50)
  .lean();

const updated = await User.findByIdAndUpdate(
  userId,
  { $set: { name: input.name } },
  { new: true, runValidators: true },
);

const session = await mongoose.startSession();
await session.withTransaction(async () => {
  await Order.create([{ userId, total }], { session });
  await AuditLog.create([{ userId, action: "ORDER_CREATED" }], { session });
});
await session.endSession();

const page = await Post.find({
  published: true,
  ...(cursor
    ? { $or: [
        { createdAt: { $lt: cursor.createdAt } },
        { createdAt: cursor.createdAt, _id: { $lt: cursor.id } },
      ] }
    : {}),
}).sort({ createdAt: -1, _id: -1 }).limit(20).lean();

userSchema.index({ email: 1 }, { unique: true });
userSchema.index(
  { organizationId: 1, archivedAt: 1 },
  { partialFilterExpression: { archivedAt: null } },
);
```

### Password hashing

```typescript
import argon2 from "argon2";
export const hashPassword = (password: string) => argon2.hash(password, { type: argon2.argon2id });
export const verifyPassword = (hash: string, password: string) => argon2.verify(hash, password);
```

## Output contract

Hand back:

1. **Boundary classification**: mode(s), bucket, and the path that was traced.
2. **The change**, where:
   - expected business failures are visible in signatures;
   - writes are retry-safe wherever the environment can retry them;
   - deadline and cancellation handling flows through the whole call chain;
   - type and value boundaries are obvious in code and imports;
   - the risky boundary is obvious from a quick skim.
3. **Selected and rejected patterns**, with one line of reason each, and any deviation
   from a rule plus how the property is preserved.
4. **Casts and suppressions added**, each with its justification. Ideally none.
5. **Gate results**: each command, where it ran, exit status, and what boundary it
   exercised. Planned commands are not executed commands; say which is which.
6. **Public-contract changes**: response envelopes, DTOs, indexes, stored shapes, and the
   migration or rollback for each.
7. **Open risks**: what is unverified, version-sensitive, or needs an owner's decision.

Leave the code with better boundary hygiene than you found, not just passing types.

## Quality gates

Use the repository's package manager and runners. With pnpm, Vitest and Playwright:

```bash
pnpm exec tsc --noEmit
pnpm exec eslint . --max-warnings=0
pnpm exec vitest run
pnpm exec playwright test
```

npm equivalents: `npx tsc --noEmit`, `npx eslint . --max-warnings=0`, `npx vitest run` or
`npx jest`, `npx playwright test`. A monorepo with split scripts runs `npm run type-check`,
`npm run lint`, `npm test` and `npm run build` at the root, each running client then
server. `--max-warnings=0` makes warnings binding. A headless library may have no
end-to-end layer; say that it is absent rather than leaving it out silently.

Quick searches for the common holes:

```bash
grep -rn --include='*.ts' -E "req\.(body|query|params) as |: any\b|as any\b|as unknown as" src
grep -rn --include='*.ts' -E "@ts-ignore|@ts-expect-error|eslint-disable" src
grep -rn --include='*.ts' -E "findOneAndUpdate|findByIdAndUpdate|updateOne|updateMany" src | grep -v runValidators
grep -rn --include='*.ts' -E "\.skip\(|populate\(['\"][a-zA-Z.]+['\"]\)|hashSync|compareSync" src
```

Each hit is a question, not a verdict. A single-line `grep -v` misses options on the
next line; open the call.

Then check by hand:

- every new external input is parsed at the boundary;
- no new `any` leaked into core logic;
- new unions are handled exhaustively;
- persisted shapes are version-tolerant;
- retries, timeouts and loading states are explicit;
- contract or integration tests hit the real boundary, with a real database where
  database behaviour matters.

Green commands do not prove the rules were followed. Typecheck is not request validation,
mocks are not transaction proof, and snapshots are not user behaviour.

## Anti-patterns

Language:

1. Type-only API contracts: an interface without runtime parsing.
2. `any` at trust boundaries.
3. Boolean-soup state instead of a union.
4. Shallow merge of persisted state.
5. Business logic written inside framework hooks, routers or SDK calls.
6. Single-layer testing: unit-only or end-to-end-only.
7. Transport leakage: application code that knows provider quirks.
8. `as` as duct tape where `satisfies`, parsing or a branded constructor would prove it.
9. Type and value imports mixed so the bundler has to guess.
10. Stringly typed IDs.
11. Timeouts that abort nothing.
12. Core user journeys that die without client JavaScript (browser code only).

Backend:

1. `req.body as MyType`. This is the gateway failure: it fabricates evidence that every
   downstream signature then repeats.
2. Throwing generic `Error` for normal business failures.
3. Retrying writes without idempotency keys.
4. Starting async work that cannot be cancelled.
5. Treating env vars as trustworthy strings.

MERN:

1. Validating only in the browser.
2. Treating `unique: true` as validation.
3. `findOneAndUpdate()` for every write path; forgetting `runValidators: true`.
4. `lean()` on paths that depend on document methods, virtuals or `save()`.
5. Populating entire relation trees by default; N+1 queries in a loop.
6. Embedding arrays that grow without bound.
7. Persisting browser state without versioning and migration.
8. Shipping without readiness and shutdown handling.
9. Testing component internals instead of user-visible behaviour.
10. Hashing passwords synchronously inside request handlers.
11. Omitting request correlation from logs; logging `req.body`, tokens or PII.
12. Scattering `res.status(500)` across handlers.
13. One `User` shape reused as entity, DTO and response; returning a hydrated document.

Each of these can pass a demo and fail in production.

## Bundled scripts

None. The source skills contained no scripts or templates beyond the code shown above.
[reference.md](reference.md) holds the full pattern catalogue, the scoreboards, longer
examples, failure modes and operations guidance.

## Self-check

Before handing back, answer each with yes or a stated reason:

- Did I classify the mode and the boundary before writing code?
- Does every new external input pass through one schema parse at the edge, with the type
  inferred from that schema?
- Is env parsed at boot?
- Are IDs that could be swapped branded?
- Are expected failures in the return type, and do throws mean invariant violations only?
- Does every new async boundary take a signal and a deadline, and pass them down?
- Can every write that might be retried be deduplicated by a client- or message-derived
  key?
- For Mongoose: projection, `lean()` where safe, selective populate, stable sort,
  validators on query updates, indexes matching the query?
- Did I add a cast, `any` or suppression? Is each fenced and explained?
- Did the gates run, and did I report exit status rather than intent?
- Did I name what remains unverified or version-sensitive?
