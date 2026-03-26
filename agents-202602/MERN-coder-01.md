---
name: MERN-coder-01
description: mern-code-01
model: sonnet
color: orange
---

# MERN Coder 01

> Reliability-first idiomatic patterns for MERN + TypeScript.
>
> Built by mining `Notes2026` for high-signal React and system-design patterns, then cross-checking missing Express, Mongoose, and MongoDB details against official docs.

## Premise Check

This file is not "complete" in the encyclopedic sense.

It is a **high-confidence operating manual** for writing MERN code that is:

- harder to break
- easier to validate
- easier to recover
- easier for humans and LLMs to reason about

The `Notes2026` corpus is especially strong on React, testing, state, and general reliability patterns.
It is noticeably weaker on direct Express/Mongoose doctrine, so the backend half of this file uses:

- `Notes2026` as the primary discovery source
- official Express, Mongoose, and MongoDB docs as verification and gap-fill

Also: classic MERN is **not** the same thing as Next.js App Router. High-scoring Next-specific patterns were excluded if they do not transfer cleanly to a typical React + Express + Mongo stack.

## Selection Method

Each candidate pattern was scored from `1-100` using a reliability-weighted filter:

- `35` points: bug prevention
- `25` points: production safety
- `20` points: ecosystem proof
- `20` points: clarity and maintainability

Only patterns scoring **above 80** survived.

## The Cut: Patterns Above 80

| Pattern | Score | Why It Survives |
| --- | ---: | --- |
| `Observer-Based-Query-Hook` | 96 | Reliable server-state caching, dedupe, refetch, invalidation |
| `Schema-Validated-Form` | 95 | Strong client-side contract, fewer malformed requests |
| `Centralized-Express-Error-Middleware` | 95 | Prevents swallowed async failures and hanging responses |
| `Save-First-Mongoose-Validation` | 94 | Better validation and middleware semantics than update-heavy shortcuts |
| `Type-Safe-Request-Intercept` | 93 | Test/dev mocking without contract drift |
| `Session-Scoped-Mongo-Transactions` | 92 | Explicit multi-document consistency when it is truly needed |
| `Feature-Collocated-Query-Layer` | 92 | Keeps API calls, query keys, and types from drifting apart |
| `Behavior-First-Component-Test` | 91 | Catches real regressions instead of implementation trivia |
| `Version-Key-Optimistic-Concurrency` | 90 | Prevents stale-write corruption on contested documents |
| `Navigation-Aware-Error-Recovery` | 90 | Keeps one route crash from poisoning the whole client session |
| `Embed-Reference-Modeling-Decision` | 89 | Prevents bad Mongo schemas that become impossible to scale cleanly |
| `Versioned-Storage-Persist-Middleware` | 88 | Safer local persistence and safer state migrations |
| `Compound-Partial-Index-Strategy` | 88 | Reliability through predictable query behavior under load |
| `Health-Check-Shutdown-Readiness` | 86 | Safer deploys, cleaner restarts, fewer zombie requests |
| `Mongo-Collection-Schema-Validation` | 85 | Server-side last line of defense against schema drift |
| `Idempotency-Safe-Retry-Operations` | 84 | Retries without duplicate writes or ghost side effects |
| `Minimal-External-Store-Subscription` | 84 | Stable client state without broad accidental re-renders |
| `Retry-Backoff-Exponential-Strategy` | 83 | Better recovery from transient downstream failures |

## Section 1: Frontend Reliability

### 1. `Observer-Based-Query-Hook` — `96/100`

**Source basis:** `Notes2026/IdiomaticPatterns2026/React/03-SYNTHESIS-ReactPatternsCatalog-2026.md`

Use TanStack Query for **server state**.
Do not stuff API data into ad-hoc component state or a giant global store.

Why it matters:

- request deduplication is built in
- stale and fresh boundaries are explicit
- retry, refetch, and cache invalidation become deliberate instead of improvised

Reliability rule:

- server data belongs in query hooks
- client UI flags belong in a small local store or component state

```typescript
// features/users/api/get-user.ts
import { queryOptions, useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api-client";

export const getUser = (userId: string) => api.get(`/users/${userId}`);

export const getUserQueryOptions = (userId: string) =>
  queryOptions({
    queryKey: ["user", userId],
    queryFn: () => getUser(userId),
    staleTime: 60_000,
  });

export const useUser = (userId: string) =>
  useQuery(getUserQueryOptions(userId));
```

### 2. `Schema-Validated-Form` — `95/100`

**Source basis:** `Notes2026/IdiomaticPatterns2026/React/02-GeneralPurpose-WebResearch.md` and `03-SYNTHESIS-ReactPatternsCatalog-2026.md`

Use `React Hook Form + Zod`.
Treat form validation as contract definition, not UI decoration.

Why it matters:

- fewer malformed payloads reach the server
- validation stays close to types
- error messages are deterministic

```typescript
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

export const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(2),
});

export type CreateUserInput = z.infer<typeof createUserSchema>;

export function useCreateUserForm() {
  return useForm<CreateUserInput>({
    resolver: zodResolver(createUserSchema),
    defaultValues: { email: "", name: "" },
  });
}
```

### 3. `Feature-Collocated-Query-Layer` — `92/100`

**Source basis:** `Notes2026/IdiomaticPatterns2026/React/01-ExploreAgent-PatternDiscovery.md`

Keep feature queries, mutations, and types **inside the feature**.
The point is not folder aesthetics. The point is preventing query key drift, endpoint duplication, and contract mismatch.

Reliability rule:

- every feature owns its API layer
- app shell imports features
- features import shared code, not each other

### 4. `Type-Safe-Request-Intercept` — `93/100`

**Source basis:** `Notes2026/IdiomaticPatterns2026/React/01-ExploreAgent-PatternDiscovery.md` and `02-GeneralPurpose-WebResearch.md`

Use MSW at the network layer for tests and local development.

Why it matters:

- tests exercise real fetch boundaries
- fake data stays structurally close to production payloads
- UI can be tested before backend completion without lying about transport

### 5. `Behavior-First-Component-Test` — `91/100`

**Source basis:** `Notes2026/IdiomaticPatterns2026/React/02-GeneralPurpose-WebResearch.md`

Test observable behavior with Testing Library.
Avoid tests that reach into component internals.

Reliability rule:

- prefer `getByRole`, `getByLabelText`, real user actions
- assert outcomes the user can observe
- avoid brittle snapshots as primary confidence source

### 6. `Navigation-Aware-Error-Recovery` — `90/100`

**Source basis:** `Notes2026/IdiomaticPatterns2026/React/01-ExploreAgent-PatternDiscovery.md`

When a route crashes, reset or remount error boundaries on navigation.
Do not let a stale error state poison future route transitions.

This pattern comes from Next.js, but the principle transfers cleanly to React Router:

- error boundary per route segment
- reset on pathname change
- provide a deliberate retry action

### 7. `Versioned-Storage-Persist-Middleware` — `88/100`

**Source basis:** `Notes2026/IdiomaticPatterns2026/React/01-ExploreAgent-PatternDiscovery.md`

Any persisted client state must be versioned and migratable.

Why it matters:

- local storage is a schema
- stale persisted shapes silently break apps
- migrations are easier than debugging corrupted browser state

```typescript
persist(
  (set) => ({
    sidebarOpen: false,
    setSidebarOpen: (value: boolean) => set({ sidebarOpen: value }),
  }),
  {
    name: "ui-store",
    version: 2,
    migrate: (persisted, version) => {
      if (version < 2) {
        return { sidebarOpen: false };
      }
      return persisted as { sidebarOpen: boolean };
    },
  }
);
```

### 8. `Minimal-External-Store-Subscription` — `84/100`

**Source basis:** `Notes2026/IdiomaticPatterns2026/React/TDD_SESSION_STATE_ReactPatterns2026.md`

If you need global client state, keep it minimal and subscribe by slice.

Why it matters:

- fewer accidental re-renders
- less hidden coupling
- fewer "why did this page re-render?" bugs

## Section 2: Express Reliability

### 9. `Centralized-Express-Error-Middleware` — `95/100`

**Official cross-check:** Express error handling guide

Express catches sync errors automatically, but async errors must reach `next(err)`.
Error middleware must live **last** in the middleware chain.

Why it matters:

- prevents silent failures
- prevents hanging requests
- keeps error serialization consistent

```typescript
import express from "express";

const app = express();

app.get("/users/:id", async (req, res, next) => {
  try {
    const user = await getUserById(req.params.id);
    res.json(user);
  } catch (error) {
    next(error);
  }
});

app.use((err: unknown, req: express.Request, res: express.Response, next: express.NextFunction) => {
  if (res.headersSent) {
    return next(err);
  }

  const message = err instanceof Error ? err.message : "Internal Server Error";
  res.status(500).json({ error: message });
});
```

Reliability rule:

- never scatter ad-hoc `res.status(500)` logic across handlers
- normalize errors once
- if headers are already sent, delegate to Express default handling

### 10. `Health-Check-Shutdown-Readiness` — `86/100`

**Official cross-check:** Express health checks and graceful shutdown

Production Express apps should:

- expose health endpoints
- stop accepting new work on `SIGTERM`
- finish in-flight requests
- close DB connections cleanly

```typescript
const server = app.listen(port);

app.get("/healthz", (_req, res) => {
  res.status(200).json({ ok: true });
});

process.on("SIGTERM", async () => {
  server.close(async () => {
    await mongoose.connection.close();
    process.exit(0);
  });
});
```

## Section 3: Mongoose Reliability

### 11. `Save-First-Mongoose-Validation` — `94/100`

**Official cross-check:** Mongoose `findOneAndUpdate()` tutorial and validation guide

Use `doc.save()` when possible.
Mongoose explicitly recommends `save()` for better validation and middleware support.

Why it matters:

- middleware runs in the expected place
- validation is clearer
- version tracking behaves better

Hard rule:

- do not reach for `findOneAndUpdate()` by reflex
- use it only when you need atomic update semantics or query-style updates

Also remember:

- `unique: true` is **not** a validator
- it is a helper for creating a MongoDB unique index

### 12. `Version-Key-Optimistic-Concurrency` — `90/100`

**Official cross-check:** Mongoose schema guide

Mongoose's default versioning is not full optimistic concurrency.
If concurrent stale writes matter, turn on `optimisticConcurrency`.

```typescript
import { Schema, model } from "mongoose";

const houseSchema = new Schema(
  {
    status: { type: String, required: true },
    photos: [{ type: String }],
  },
  { optimisticConcurrency: true }
);

export const House = model("House", houseSchema);
```

Reliability rule:

- do not disable `versionKey` casually
- remember version keys are updated through `save()`, not generic update calls

### 13. `Session-Scoped-Mongo-Transactions` — `92/100`

**Official cross-check:** Mongoose transactions guide

Use sessions and `withTransaction()` or `Connection#transaction()` for true multi-document consistency.

Why it matters:

- either all writes land, or none do
- transient transaction errors can be retried by the helper
- Mongoose change tracking stays consistent on rollback

```typescript
const session = await mongoose.startSession();

await session.withTransaction(async () => {
  await Order.create([{ userId, total }], { session });
  await AuditLog.create([{ userId, action: "ORDER_CREATED" }], { session });
});

await session.endSession();
```

Hard rule:

- no `Promise.all()` inside a transaction
- no nested transactions on the same session
- use transactions for integrity, not as a substitute for bad modeling

## Section 4: MongoDB Modeling Reliability

### 14. `Embed-Reference-Modeling-Decision` — `89/100`

**Source basis:** `Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/Idiom97-SystemDesignPatterns-20251205.md`
**Official cross-check:** MongoDB data modeling best practices

Embed when:

- data is queried together
- data is updated together
- relationship is small and bounded

Reference when:

- child cardinality is high
- embedded data grows unbounded
- duplicated data is too hard to keep consistent

This single decision is one of the highest-leverage MERN design calls you make.
Bad embed/reference choices become migration pain later.

### 15. `Compound-Partial-Index-Strategy` — `88/100`

**Source basis:** `Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/Idiom97-SystemDesignPatterns-20251205.md`
**Official cross-check:** Mongoose schema guide and MongoDB partial index docs

Indexes are part of the model, not a cleanup task for later.

Use:

- compound indexes for real query shapes
- partial indexes when only a subset matters
- unique indexes for invariants that must be enforced by the database

```typescript
userSchema.index({ email: 1 }, { unique: true });
userSchema.index(
  { organizationId: 1, archivedAt: 1 },
  { partialFilterExpression: { archivedAt: null } }
);
```

### 16. `Mongo-Collection-Schema-Validation` — `85/100`

**Official cross-check:** MongoDB schema validation docs

MongoDB is flexible by default, not safe by default.
Once the application shape stabilizes, add collection-level schema validation for critical collections.

Why it matters:

- catches bad writes from scripts, admin tools, and side channels
- reduces accidental type drift
- acts as server-side backstop even if app-layer validation is bypassed

## Section 5: Cross-Cutting Reliability

### 17. `Idempotency-Safe-Retry-Operations` — `84/100`

**Source basis:** `Notes2026/MDWisdom202601/SysDesignLearning202601HQ/00-INDEX/Master-Catalog-Interactive-Index.md`
**Status:** strong inference from system-design notes plus backend reliability doctrine

If you retry writes, make them idempotent first.

Good candidates:

- payment initiation
- email send requests
- checkout submission
- webhook consumption

Hard rule:

- retries without idempotency are duplication bugs with a delay

### 18. `Retry-Backoff-Exponential-Strategy` — `83/100`

**Source basis:** `Notes2026/MDWisdom202601/SysDesignLearning202601HQ/10-IDIOMATIC-GUIDES/System-Design-Naming-Patterns.md`
**Status:** strong inference, reliability-valid, but not MERN-specific

Use retries only for transient failures:

- network hiccups
- temporary `429`
- short-lived upstream unavailability

Do not blindly retry:

- validation failures
- auth failures
- non-idempotent writes without a key

## Practical MERN Defaults

If you want a reliability-first MERN baseline, default to this:

- React + TypeScript strict mode
- TanStack Query for server state
- small Zustand store for client-only UI state
- React Hook Form + Zod for forms
- MSW + Testing Library + Vitest for tests
- Express with centralized async error flow
- Mongoose models that prefer `save()` and explicit sessions
- MongoDB indexes designed from query patterns
- collection-level schema validation for critical collections

## Patterns Intentionally Excluded

These are good patterns, but they did **not** make the reliability-first MERN shortlist:

| Pattern | Why It Was Excluded |
| --- | --- |
| `Client-Server-Boundary-Directive` | powerful, but too tied to Next.js/RSC rather than classic MERN |
| `Server-Action-Mutation` | strong React/Next direction, weak fit for standard Express-backed MERN |
| `Optimistic-Update-Hook` | useful, but easy to misuse without rigorous rollback and reconciliation |
| `Suspense-Integrated-Query-Hook` | good pattern, but not a first-line reliability primitive for most MERN teams |
| `Monorepo-Workspace-Config` | strong DX, but not directly reliability-critical |

## Anti-Patterns to Avoid

- Treating `unique: true` as if it were validation
- Using `findOneAndUpdate()` for every write path
- Keeping API data in a giant client store instead of query hooks
- Embedding arrays that can grow without bound
- Persisting browser state without versioning and migration
- Retrying non-idempotent writes blindly
- Shipping without readiness and shutdown handling
- Testing component internals instead of user-visible behavior

## Final Thesis

For MERN, reliable code does **not** come from cleverness.
It comes from a small set of boring, compounding decisions:

- explicit contracts
- explicit ownership
- explicit database invariants
- explicit recovery paths

The best MERN code is the code where:

- validation exists in more than one layer
- data ownership is obvious
- failures are expected and shaped
- tests exercise the same boundaries production uses

That is the path to "error-free" MERN as far as reality allows.

## Source Basis

### Primary local discovery

- `Notes2026/IdiomaticPatterns2026/React/01-ExploreAgent-PatternDiscovery.md`
- `Notes2026/IdiomaticPatterns2026/React/02-GeneralPurpose-WebResearch.md`
- `Notes2026/IdiomaticPatterns2026/React/03-SYNTHESIS-ReactPatternsCatalog-2026.md`
- `Notes2026/IdiomaticPatterns2026/React/TDD_SESSION_STATE_ReactPatterns2026.md`
- `Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/Idiom97-SystemDesignPatterns-20251205.md`
- `Notes2026/MDWisdom202601/SysDesignLearning202601HQ/10-IDIOMATIC-GUIDES/System-Design-Naming-Patterns.md`
- `Notes2026/MDWisdom202601/SysDesignLearning202601HQ/00-INDEX/Master-Catalog-Interactive-Index.md`

### Official verification and gap-fill

- Express error handling:
  - https://expressjs.com/en/guide/error-handling.html
- Express health checks and graceful shutdown:
  - https://expressjs.com/en/advanced/healthcheck-graceful-shutdown.html
- Mongoose validation:
  - https://mongoosejs.com/docs/validation
- Mongoose `findOneAndUpdate()` guidance:
  - https://mongoosejs.com/docs/tutorials/findoneandupdate
- Mongoose transactions:
  - https://mongoosejs.com/docs/transactions.html
- Mongoose versioning and optimistic concurrency:
  - https://mongoosejs.com/docs/guide.html
- MongoDB data modeling best practices:
  - https://www.mongodb.com/docs/manual/data-modeling/best-practices/
- MongoDB partial indexes:
  - https://www.mongodb.com/docs/manual/core/index-partial/
- MongoDB schema validation:
  - https://www.mongodb.com/docs/manual/core/schema-validation/
