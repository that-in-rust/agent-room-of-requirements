---
name: typescript-backend-coder-01
description: typescript-backend-code-01
model: sonnet
color: green
---

# TypeScript Backend Coder 01

> Reliability-first backend/server TypeScript companion to `typescript-coder-01`.
>
> Scope: Node.js, Bun, Deno, workers, APIs, queues, CLIs, long-running services.

---

## Premise Check

- This file assumes the baseline guardrails from `typescript-coder-01` already apply.
- It narrows the focus to backend failure modes:
  - invalid inbound data
  - mixed-up identifiers
  - hidden transport drift
  - timeout and cancellation bugs
  - retry/idempotency mistakes
  - storage and config evolution

---

## Inherited Baseline

Use these from the general TypeScript reference without re-debating them:

- strict compiler railguards
- `import type` and module-boundary hygiene
- `unknown` at trust boundaries
- schema-first parsing
- exhaustive unions
- assertion functions
- `satisfies`
- explicit cancellation
- project references when scale requires them

Primary companion:

- [typescript-reliability-reference.md](../../typescript-coder-01/references/typescript-reliability-reference.md)

---

## Chosen Thesis

**Reliable backend TypeScript is mostly about making IO lies impossible to ignore.**

That means:

- requests, events, env, and queue payloads enter as `unknown`
- domain IDs are branded before business logic uses them
- recoverable failures stay explicit in signatures
- outbound provider/database/http shapes are normalized
- deadlines and cancellation propagate through the full call chain
- writes are idempotent when retries can happen
- persistence and config formats evolve without breaking old data

---

## Pattern Scoreboard

| Score | Pattern | Why it matters |
|---|---|---|
| **98** | Schema-First Request Parsing | Stops invalid input before it contaminates the core |
| **96** | Strict Compiler and Module Railguards | Prevents silent widening and emit mistakes |
| **95** | Explicit Result Error Algebra | Makes recoverable failures impossible to ignore |
| **94** | Branded Identifier Types | Stops mixing semantically different scalars |
| **94** | Deadline and Cancellation Propagation | Prevents orphaned async work and timeout drift |
| **93** | Typed Transport Normalization | Isolates provider and wire-level quirks |
| **92** | Ports-and-Adapters Service Core | Keeps domain rules testable and framework-light |
| **90** | Idempotent Mutation Boundaries | Makes retries safe for writes |
| **90** | Boot-Time Env Validation | Fails fast instead of failing weird |
| **89** | Persistence Evolution Contracts | Prevents upgrades from corrupting stored state |
| **88** | Contract and Integration Tests | Verifies real HTTP/DB/queue behavior |
| **85** | Project-Reference Build Partitions | Helps large backends stay separable and fast |

---

## Core Patterns

### 1. Schema-First Request Parsing

**Score: 98/100**

Parse HTTP bodies, headers, params, queue payloads, and cron/job inputs at the edge.

```typescript
import { z } from "zod";

const createUserRequestSchema = z.object({
  email: z.string().email(),
  displayName: z.string().min(2).max(80),
});

type CreateUserRequest = z.infer<typeof createUserRequestSchema>;

export function parseCreateUserRequestSafely(input: unknown): CreateUserRequest {
  return createUserRequestSchema.parse(input);
}
```

**Rule**:

- Parse once.
- Pass typed data inward.
- Never let raw `req.body` travel through the app.

---

### 2. Boot-Time Env Validation

**Score: 90/100**

Environment config is just another untrusted boundary.

```typescript
import { z } from "zod";

const environmentSchema = z.object({
  NODE_ENV: z.enum(["development", "test", "production"]),
  PORT: z.coerce.number().int().min(1).max(65535),
  DATABASE_URL: z.string().min(1),
  JWT_SECRET: z.string().min(32),
});

export const environmentConfig = environmentSchema.parse(process.env);
```

**Rule**:

- Crash early at boot if config is invalid.
- Do not defer env parsing to the first request.

---

### 3. Branded Identifier Types

**Score: 94/100**

```typescript
declare const userIdBrand: unique symbol;
declare const workspaceIdBrand: unique symbol;

export type UserId = string & { readonly [userIdBrand]: "UserId" };
export type WorkspaceId = string & { readonly [workspaceIdBrand]: "WorkspaceId" };
```

Use them for:

- database primary keys
- tenant/workspace IDs
- idempotency keys
- message/job IDs

**Rule**:

- If two IDs should never be swapped, they should never share the same bare type.

---

### 4. Explicit Result Error Algebra

**Score: 95/100**

Expected business failures should not disappear into generic exceptions.

```typescript
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

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
  if (existing) {
    return { ok: false, error: { type: "email-already-exists" } };
  }

  const userId = await insertUserRecord(parsed.data);
  return { ok: true, value: userId };
}
```

**Rule**:

- Throw for invariant violations and programmer bugs.
- Return explicit results for expected operational/business outcomes.

---

### 5. Deadline and Cancellation Propagation

**Score: 94/100**

```typescript
export async function fetchProviderJsonStrictly<T>(
  url: string,
  options: { signal?: AbortSignal; timeoutMs?: number } = {},
): Promise<T> {
  const timeoutSignal =
    options.timeoutMs === undefined
      ? undefined
      : AbortSignal.timeout(options.timeoutMs);

  const signal =
    options.signal && timeoutSignal
      ? AbortSignal.any([options.signal, timeoutSignal])
      : options.signal ?? timeoutSignal;

  const response = await fetch(url, { signal });
  return (await response.json()) as T;
}
```

**Rule**:

- Every backend boundary should answer:
  - who can cancel this?
  - how long can this run?
  - what happens downstream when it aborts?

---

### 6. Typed Transport Normalization

**Score: 93/100**

Normalize wire formats before they hit business logic.

```typescript
type NormalizedWebhookEvent =
  | { type: "user-created"; userId: UserId }
  | { type: "workspace-deleted"; workspaceId: WorkspaceId };

export function normalizeWebhookEventStrictly(input: unknown): NormalizedWebhookEvent {
  const parsed = webhookEnvelopeSchema.parse(input);
  return parsed.event_type === "user.created"
    ? { type: "user-created", userId: createUserIdSafely(parsed.data.user_id) }
    : { type: "workspace-deleted", workspaceId: createWorkspaceIdSafely(parsed.data.workspace_id) };
}
```

**Rule**:

- Provider-specific drift belongs in adapter code, not use-case code.

---

### 7. Ports-and-Adapters Service Core

**Score: 92/100**

```typescript
export interface UserRepositoryPort {
  findUserByEmail(email: string): Promise<UserRecord | null>;
  insertUser(data: CreateUserRequest): Promise<UserId>;
}

export interface AuditLogPort {
  recordUserCreated(userId: UserId): Promise<void>;
}

export class CreateUserUseCase {
  constructor(
    private readonly users: UserRepositoryPort,
    private readonly audit: AuditLogPort,
  ) {}

  async execute(input: CreateUserRequest): Promise<Result<UserId, CreateUserError>> {
    const existing = await this.users.findUserByEmail(input.email);
    if (existing) return { ok: false, error: { type: "email-already-exists" } };
    const userId = await this.users.insertUser(input);
    await this.audit.recordUserCreated(userId);
    return { ok: true, value: userId };
  }
}
```

**Rule**:

- Framework code should wrap the core, not define it.

---

### 8. Idempotent Mutation Boundaries

**Score: 90/100**

If clients or queues can retry, your writes need deduplication keys.

```typescript
declare const clientMessageIdBrand: unique symbol;
type ClientMessageId = string & { readonly [clientMessageIdBrand]: "ClientMessageId" };

type CreateMessageCommand = {
  roomId: WorkspaceId;
  authorId: UserId;
  clientMessageId: ClientMessageId;
  content: string;
};

export async function createMessageDeduplicated(
  command: CreateMessageCommand,
): Promise<Result<MessageRecord, { type: "duplicate" }>> {
  const existing = await findMessageByClientId(command.clientMessageId);
  if (existing) return { ok: false, error: { type: "duplicate" } };
  return { ok: true, value: await insertMessageRecord(command) };
}
```

**Rule**:

- Retries without idempotency are duplicate bugs waiting for traffic.

---

### 9. Persistence Evolution Contracts

**Score: 89/100**

Stored shapes need a migration story:

- add fields safely
- preserve unknown keys when possible
- migrate old versions lazily
- never assume today’s format is forever

**Rule**:

- Treat persisted JSON as a public contract with your future self.

---

### 10. Contract and Integration Tests

**Score: 88/100**

Minimum backend layers:

- unit tests for pure domain logic
- integration tests for repositories/adapters
- HTTP contract tests for handlers
- end-to-end tests for critical user journeys

**Rule**:

- The adapter boundary is where “typed code” meets reality. Test it there.

---

### 11. Project-Reference Build Partitions

**Score: 85/100**

Large backend repos benefit from explicit build partitions:

- `core`
- `application`
- `adapters`
- `services`
- `workers`

**Rule**:

- Use project references when the repo is large enough that architectural boundaries need compiler support.

---

## Backend Anti-Patterns

1. Accepting `req.body as MyType`
2. Using raw `string` for every identifier
3. Throwing generic `Error` for normal business failures
4. Retrying writes without idempotency keys
5. Starting async work that cannot be cancelled
6. Letting provider response shapes leak into domain logic
7. Treating env vars as trustworthy strings

---

## Source Trail

- `/Users/amuldotexe/Desktop/agent-room-of-requirements/agents-202602/typescript-coder-01.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/MERN-TypeScript-IdiomaticPatterns_20251206.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/Idiom96-polyglot-basic-patterns-20251205.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/design101-tdd-architecture-principles.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/05_Code_Analysis_Testing/opencode-data-flow-analysis.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/03_API_Documentation_Specs/opencode-genius-idiomatic-patterns__76d4afea.md`

---

## Final Synthesis

If a backend LLM only learns five habits from this file, they should be:

1. parse all inbound data
2. brand all important IDs
3. model recoverable failures explicitly
4. propagate cancellation and deadlines
5. keep adapters outside the core
