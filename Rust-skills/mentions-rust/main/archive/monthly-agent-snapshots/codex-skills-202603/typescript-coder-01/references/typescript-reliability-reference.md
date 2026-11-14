---
name: typescript-coder-01
description: typescript-code-01
model: sonnet
color: blue
---

# TypeScript Coder 01

> Reliability-first TypeScript patterns selected from `Notes2026` and verified against primary TypeScript documentation.
>
> Selection rule: only patterns scoring **above 80/100** are included.
>
> Goal: bias toward **error-free, production-reliable code**, not fashion.

---

## Premise Check

- This is **not** a general TypeScript tutorial.
- This is a **curated reference** for writing TypeScript that survives bad inputs, schema drift, storage failures, async complexity, and frontend/backend boundary mistakes.
- The existing `rust-coder-01.md` is useful, but it is closer to a high-signal manifesto than a complete scored reference. This document fixes that by:
  - using explicit selection criteria
  - separating language-specific patterns from general architecture advice
  - keeping only patterns with strong reliability evidence

## Companion Splits

- Backend/server companion:
  - [backend-reliability-reference.md](../../typescript-backend-coder-01/references/backend-reliability-reference.md)
- React/frontend companion:
  - [react-reliability-reference.md](../../typescript-react-coder-01/references/react-reliability-reference.md)

---

## Expert Lenses

Patterns were selected through four lenses:

1. **Type-system safety**
2. **Runtime boundary integrity**
3. **Operational resilience**
4. **Skeptical production lens**

The skeptical question was simple:

> "Does this pattern still help when inputs are malformed, the browser is weird, persistence drifts across versions, or a teammate changes one branch and forgets another?"

---

## Scoring Rubric

Each candidate pattern was scored out of 100:

- **40 pts**: failure prevention impact
- **25 pts**: evidence strength across `Notes2026`
- **20 pts**: breadth of applicability
- **15 pts**: maintainability under change

Only patterns scoring **81+** made the cut.

---

## Chosen Thesis

**Reliable TypeScript comes from treating the type system as a guardrail, not a costume.**

That means:

- compile with strictness that exposes ambiguity
- make type/value module boundaries explicit
- accept `unknown` at boundaries
- parse once at the edge with schemas
- infer types from schemas instead of duplicating them
- preserve literal precision when contracts need exactness
- model state and protocol flows with discriminated unions
- use assertion functions when invalid states must stop execution
- distinguish recoverable error results from invariant violations
- normalize transport shapes before business logic touches them
- make persistence version-tolerant
- propagate cancellation and deadlines explicitly
- partition large repos with project references
- test behavior across unit, component, integration, and end-to-end layers

---

## Pattern Scoreboard

| Score | Pattern | Why it survived the cutoff | Primary notes |
|---|---|---|---|
| **98** | Schema-First Boundary Parsing | Single strongest guard against invalid runtime data | `opencode-genius-idiomatic-patterns`, React synthesis |
| **97** | Behavior-First Test Pyramid | Most reliable way to catch cross-layer regressions | MERN TypeScript patterns, React synthesis, Once Campfire |
| **96** | Exhaustive Union Flow Control | Prevents "forgot a case" bugs at compile time | OpenCode stream parser |
| **96** | Strict Compiler Railguards | Turns silent ambiguity into visible errors | MERN TypeScript patterns |
| **95** | Module-Boundary Import Hygiene | Prevents emit confusion and hidden side-effect bugs | TypeScript 3.8/5.0 docs |
| **95** | Unknown-Until-Proven Typed | Stops unsafe trust at system edges | OpenCode data-flow analysis |
| **94** | Versioned Persistence Migration | Handles old data, partial data, and lazy upgrades | OpenCode persistence patterns |
| **94** | Satisfies Configuration Contracts | Validates config shapes without sacrificing inference | TypeScript 4.9 docs |
| **93** | Schema-Validated Forms | Same contract powers UX and runtime checks | React synthesis |
| **93** | Assertion-Function Narrowing | Encodes "must be true now" flow in the type system | TypeScript 3.7 docs |
| **92** | Typed Transport Normalization | Makes provider/API differences somebody else's problem | OpenCode data-flow analysis |
| **92** | Branded Identifier Types | Stops mixing semantically different strings or numbers | Idiom96 polyglot patterns |
| **91** | Deep Merge Forward Compatibility | Keeps persistence robust across schema drift | OpenCode persistence patterns, `schemas.md` |
| **91** | AbortSignal Deadline Propagation | Makes async cancellation and time budgets explicit | Idiom96 patterns, MDN |
| **90** | Explicit Result Error Algebra | Keeps recoverable failures visible in signatures | Idiom96 polyglot patterns |
| **90** | Feature-Collocated Query Layer | Reduces stale-fetch bugs and duplicate state | React synthesis |
| **89** | Layered Boundary Adapters | Keeps domain logic from being polluted by IO details | Design101, Once Campfire |
| **89** | Literal Exactness Preservation | Keeps route/config/action tables precise instead of widened | TypeScript 5.0 docs |
| **88** | Quota-Aware Storage Degradation | Plans for browser storage failure instead of pretending | OpenCode persistence patterns |
| **86** | Stable-Key Stream State Machines | Critical for streaming/event-heavy systems | OpenCode stream analysis |
| **85** | Project-Reference Build Partitions | Improves build speed and enforces repo boundaries | TypeScript project references docs |
| **84** | Progressive Enhancement Minimal Client | Reliability improves when fewer features depend on JS | Once Campfire analysis |

---

## Tier S: Adopt By Default

### 1. Strict Compiler Railguards

**Score: 96/100**

**Pattern**: Turn on strictness that exposes uncertainty early.

**Why it matters**:

- `strict` catches broad type unsafety
- `noUncheckedIndexedAccess` forces you to acknowledge missing keys
- `exactOptionalPropertyTypes` stops "optional means undefined-ish" confusion
- `noFallthroughCasesInSwitch` reduces silent branch bugs
- `useUnknownInCatchVariables` stops implicit trust in thrown values
- `verbatimModuleSyntax` makes emitted module behavior match what you wrote
- `noUncheckedSideEffectImports` forces scrutiny around side-effectful imports

**Reference signals**:

- `MERN-TypeScript-IdiomaticPatterns_20251206.md` enables:
  - `strict`
  - `noUncheckedIndexedAccess`
  - `exactOptionalPropertyTypes`
  - `noFallthroughCasesInSwitch`
  - `isolatedModules`
- recent official TypeScript `tsc --init` guidance also includes:
  - `verbatimModuleSyntax`
  - `noUncheckedSideEffectImports`
  - `moduleDetection: "force"`

**Recommended baseline**:

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

**Reliability rule**:

- If a flag makes you write one extra line today, but prevents a 2 a.m. bug next month, keep the flag.

---

### 2. Module-Boundary Import Hygiene

**Score: 95/100**

**Pattern**: Separate type-only imports from runtime imports, and preserve that distinction in emit.

**Why it matters**:

- avoids accidental runtime imports that exist only for types
- makes side effects visible
- keeps transpilation predictable across bundlers and runtimes
- reduces LLM confusion around "imported for type" vs "imported for behavior"

**Reference signals**:

- TypeScript 3.8 introduced type-only imports/exports
- TypeScript docs for `verbatimModuleSyntax` emphasize matching written module syntax to runtime emit

**Preferred shape**:

```typescript
import type { UserProfile, UserRepositoryPort } from "./user-types";
import { parseUserProfileSafely } from "./user-codec";

export type { UserProfile };

export async function loadUserProfileSafely(
  repository: UserRepositoryPort,
  userId: string,
): Promise<UserProfile> {
  const raw = await repository.fetchUserById(userId);
  return parseUserProfileSafely(raw);
}
```

**Reliability rule**:

- If an import is only used in the type system, write `import type`.
- Let runtime imports mean runtime behavior.

---

### 3. Schema-First Boundary Parsing

**Score: 98/100**

**Pattern**: Parse incoming data once at the boundary, infer types from the schema, and only then hand data to the rest of the system.

**Why it matters**:

- runtime data is untrusted even if TypeScript says otherwise
- schemas give runtime validation and static types together
- removes the "types lie, runtime disagrees" class of bugs

**Reference signals**:

- OpenCode notes: "Schemas are Types", "Parse at Boundary", "Schema as Documentation"
- React synthesis scores `Schema-Validated-Form` at **96**

**Preferred shape**:

```typescript
import { z } from "zod";

const userProfileSchema = z.object({
  id: z.string(),
  email: z.string().email(),
  role: z.enum(["user", "admin"]),
});

type UserProfile = z.infer<typeof userProfileSchema>;

export function parseUserProfileSafely(input: unknown): UserProfile {
  return userProfileSchema.parse(input);
}
```

**Reliability rule**:

- Never write a TypeScript interface for external data and call it done.
- If the data crosses a process, network, storage, or browser boundary, it needs a runtime schema.

---

### 4. Unknown-Until-Proven Typed

**Score: 95/100**

**Pattern**: Use `unknown` for untrusted payloads, task data, cache payloads, and tool arguments until parsing or narrowing proves the shape.

**Why it matters**:

- `any` spreads unsafety downstream
- `unknown` forces explicit proof before use

**Reference signals**:

- `opencode-data-flow-analysis.md` models task payloads and cached data as `unknown`
- tool arguments are modeled as `Record<string, unknown>`

**Preferred shape**:

```typescript
type TaskDefinition<T> = {
  type: string;
  data: unknown;
  timeout?: number;
  decode: (input: unknown) => T;
};

export async function runWorkerTaskSafely<T>(task: TaskDefinition<T>): Promise<T> {
  const value = await executeRawTask(task.type, task.data);
  return task.decode(value);
}
```

**Reliability rule**:

- `unknown` is a boundary marker.
- If you see `any`, assume you just turned the smoke alarm off.

---

### 5. Exhaustive Union Flow Control

**Score: 96/100**

**Pattern**: Represent protocol states, events, async results, and UI state as discriminated unions with exhaustive handling.

**Why it matters**:

- compiler catches missing cases
- makes invalid states harder to represent
- scales much better than boolean soup

**Reference signals**:

- OpenCode event handlers rely on discriminated unions plus exhaustive `switch`
- parser notes explicitly say unions are mandatory at scale

**Preferred shape**:

```typescript
type StreamEvent =
  | { type: "text"; text: string }
  | { type: "tool-call"; callId: string; name: string }
  | { type: "reasoning"; summary: string }
  | { type: "done"; finishReason: "stop" | "tool_calls" | "error" };

function assertExhaustiveCaseNever(value: never): never {
  throw new Error(`Unhandled case: ${JSON.stringify(value)}`);
}

export function handleStreamEventExhaustively(event: StreamEvent): void {
  switch (event.type) {
    case "text":
      appendTextChunk(event.text);
      return;
    case "tool-call":
      beginToolExecution(event.callId, event.name);
      return;
    case "reasoning":
      appendReasoningChunk(event.summary);
      return;
    case "done":
      finishActiveStream(event.finishReason);
      return;
    default:
      assertExhaustiveCaseNever(event);
  }
}
```

**Reliability rule**:

- Prefer one union over three loosely related booleans.

---

### 6. Satisfies Configuration Contracts

**Score: 94/100**

**Pattern**: Use `satisfies` for config tables, route manifests, action maps, and declarative metadata where you want validation without losing literal inference.

**Why it matters**:

- plain type annotations often widen literals too early
- `as` assertions can silence real mistakes
- `satisfies` checks the contract while keeping precise inferred values

**Reference signals**:

- official TypeScript 4.9 documentation introduced the `satisfies` operator for this exact tradeoff

**Preferred shape**:

```typescript
type RouteContract = Record<string, { path: `/${string}`; authRequired: boolean }>;

const applicationRoutes = {
  home: { path: "/", authRequired: false },
  settings: { path: "/settings", authRequired: true },
  billing: { path: "/billing", authRequired: true },
} satisfies RouteContract;

type RouteName = keyof typeof applicationRoutes;
```

**Reliability rule**:

- Prefer `satisfies` over `as` for declarative objects that must obey a contract.

---

### 7. Assertion-Function Narrowing

**Score: 93/100**

**Pattern**: When execution must stop unless a condition holds, encode that once with assertion functions instead of scattering non-null assertions and ad hoc checks.

**Why it matters**:

- centralizes invariant enforcement
- narrows types after the check
- removes repeated `if (!x) throw` boilerplate
- gives LLMs a reusable proof primitive

**Reference signals**:

- official TypeScript 3.7 documentation added assertion functions for type-aware runtime checks

**Preferred shape**:

```typescript
export function assertUserProfilePresent(
  value: UserProfile | null | undefined,
): asserts value is UserProfile {
  if (!value) {
    throw new Error("User profile must be present");
  }
}

export function renderUserMenuSafely(
  maybeUser: UserProfile | null,
): string {
  assertUserProfilePresent(maybeUser);
  return maybeUser.email;
}
```

**Reliability rule**:

- Use assertion functions for invariants.
- Use schema parsing for untrusted inputs.

---

### 8. Behavior-First Test Pyramid

**Score: 97/100**

**Pattern**: Test pure logic, then components, then service/API integration, then full end-to-end behavior.

**Why it matters**:

- unit tests catch local regressions
- component tests catch interaction regressions
- integration tests catch contract failures
- e2e tests catch real user journey breakage

**Reference signals**:

- MERN notes include unit, hook, integration, and Playwright e2e examples
- React synthesis recommends `Vitest + React Testing Library + MSW + Playwright`
- Once Campfire highlights comprehensive controller and system tests

**Recommended stack**:

- **Unit**: Vitest or Jest
- **Component**: React Testing Library
- **Network mocking**: MSW
- **Integration**: Supertest or equivalent
- **E2E**: Playwright

**Reliability rule**:

- Test user-observable behavior first.
- Mock only one layer below the thing under test.

---

## Tier A: Strong Defaults For Most Codebases

### 9. Typed Transport Normalization

**Score: 92/100**

**Pattern**: Normalize provider-specific or API-specific responses into one internal canonical shape before application logic sees them.

**Why it matters**:

- isolates vendor quirks
- simplifies business logic
- makes retries, metrics, and caching consistent

**Reference signals**:

- `opencode-data-flow-analysis.md` defines a normalized provider response with stable internal fields

**Preferred shape**:

```typescript
type NormalizedProviderResponse = {
  provider: "openai" | "anthropic" | "google" | "local";
  model: string;
  content: string | null;
  toolCalls: Array<{
    id: string;
    name: string;
    arguments: Record<string, unknown>;
  }>;
  finishReason: "stop" | "length" | "tool_calls" | "content_filter";
};

export function normalizeProviderResponseStrictly(
  provider: string,
  raw: unknown,
): NormalizedProviderResponse {
  return providerNormalizers[provider](raw);
}
```

**Reliability rule**:

- Application code should not care which backend or provider produced the payload.

---

### 10. Versioned Persistence Migration

**Score: 94/100**

**Pattern**: Read persisted data through an adapter that can:

- migrate old versions lazily
- read legacy keys
- merge partial persisted data with defaults
- expose readiness when async storage is involved

**Why it matters**:

- old client data survives upgrades
- desktop and browser storage can share one conceptual interface
- avoids "new release broke stored state" bugs

**Reference signals**:

- OpenCode `persisted()` pattern scores **94**
- migration-on-read, legacy key fallback, async/sync adapter split

**Reliability rule**:

- Prefer migration on read over giant one-shot migrations.
- Version the storage contract even if you think you will "never need it."

---

### 11. Branded Identifier Types

**Score: 92/100**

**Pattern**: Use branded or opaque primitives for IDs and domain-critical scalar values that should never be mixed accidentally.

**Why it matters**:

- stops `UserId`, `OrderId`, and raw `string` from collapsing into one type
- reduces primitive obsession
- makes illegal argument swaps much harder for both humans and LLMs

**Reference signals**:

- `Idiom96-polyglot-basic-patterns-20251205.md` includes branded types as a production-grade TypeScript pattern

**Preferred shape**:

```typescript
declare const userIdBrand: unique symbol;
type UserId = string & { readonly [userIdBrand]: "UserId" };

export function createUserIdSafely(raw: string): UserId {
  if (!isValidUuid(raw)) {
    throw new Error("Invalid user id");
  }
  return raw as UserId;
}

export async function fetchUserByIdStrictly(id: UserId): Promise<UserProfile> {
  const raw = await fetchUserTransport(id);
  return parseUserProfileSafely(raw);
}
```

**Reliability rule**:

- Brand IDs and other semantically unique scalars at the domain edge, not after bugs appear.

---

### 12. Deep Merge Forward Compatibility

**Score: 91/100**

**Pattern**: When loading partial persisted state, recursively merge with defaults while preserving arrays, primitives, nulls, and unknown future keys correctly.

**Why it matters**:

- shallow merge is not enough
- future versions add fields
- old versions omit fields

**Reference signals**:

- OpenCode `merge()` keeps unknown keys for forward compatibility
- `schemas.md` explicitly advises against hard-denying unknown fields in evolving formats

**Preferred shape**:

```typescript
function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

export function mergePersistedStateForward(
  defaults: unknown,
  value: unknown,
): unknown {
  if (value === undefined) return defaults;
  if (value === null) return null;

  if (Array.isArray(defaults)) {
    return Array.isArray(value) ? value : defaults;
  }

  if (isRecord(defaults)) {
    if (!isRecord(value)) return defaults;
    const result: Record<string, unknown> = { ...defaults };
    for (const key of Object.keys(value)) {
      result[key] = key in defaults
        ? mergePersistedStateForward(defaults[key], value[key])
        : value[key];
    }
    return result;
  }

  return value;
}
```

**Reliability rule**:

- `undefined` means "missing."
- `null` means "intentionally empty."
- Do not collapse those concepts.

---

### 13. Schema-Validated Forms

**Score: 93/100**

**Pattern**: Drive forms from a schema, not from scattered inline checks.

**Why it matters**:

- same rules power field validation and final submission parsing
- form state stays aligned with actual domain rules
- fewer drift bugs between UI and API

**Reference signals**:

- React synthesis scores `Schema-Validated-Form` at **96**
- MERN notes include shared validation objects for requests

**Preferred shape**:

```typescript
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

const loginFormSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
});

type LoginFormData = z.infer<typeof loginFormSchema>;

export function LoginFormValidated(): JSX.Element {
  const form = useForm<LoginFormData>({
    resolver: zodResolver(loginFormSchema),
  });

  return (
    <form onSubmit={form.handleSubmit(submitLoginFormSafely)}>
      <input {...form.register("email")} />
      <input type="password" {...form.register("password")} />
      <button type="submit">Sign in</button>
    </form>
  );
}
```

**Reliability rule**:

- Prefer one schema feeding both client and server over duplicated validation logic.

---

### 14. Explicit Result Error Algebra

**Score: 90/100**

**Pattern**: Represent expected recoverable failures explicitly in return types instead of throwing everything.

**Why it matters**:

- callers must handle failure paths intentionally
- recoverable validation/network/business errors stop hiding in exceptions
- signatures become more honest for LLM-generated code

**Reference signals**:

- `Idiom96-polyglot-basic-patterns-20251205.md` uses both custom `Result` unions and `neverthrow`

**Preferred shape**:

```typescript
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

type CreateUserError =
  | { type: "email-taken" }
  | { type: "invalid-input"; messages: string[] };

export async function createUserWithResult(
  input: unknown,
): Promise<Result<UserProfile, CreateUserError>> {
  const parsed = userProfileCreateSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: { type: "invalid-input", messages: parsed.error.issues.map((i) => i.message) },
    };
  }

  const created = await tryCreateUser(parsed.data);
  if (!created) {
    return { ok: false, error: { type: "email-taken" } };
  }

  return { ok: true, value: created };
}
```

**Reliability rule**:

- Use `Result` for expected recoverable outcomes.
- Throw for programmer mistakes, impossible states, and invariant violations.

---

### 15. AbortSignal Deadline Propagation

**Score: 91/100**

**Pattern**: Accept an `AbortSignal` in async boundaries, compose it with deadlines, and propagate it downward instead of inventing disconnected timeout logic.

**Why it matters**:

- cancellation becomes consistent across layers
- time budgets become explicit
- async work can stop cleanly when callers no longer care

**Reference signals**:

- `Idiom96-polyglot-basic-patterns-20251205.md` uses `AbortController` for timeout-driven cancellation
- MDN documents `AbortSignal.timeout()` for deadline signals

**Preferred shape**:

```typescript
export async function fetchJsonWithDeadline<T>(
  url: string,
  options: { signal?: AbortSignal; timeoutMs?: number } = {},
): Promise<T> {
  const deadlineSignal =
    options.timeoutMs === undefined
      ? undefined
      : AbortSignal.timeout(options.timeoutMs);

  const signal =
    options.signal && deadlineSignal
      ? AbortSignal.any([options.signal, deadlineSignal])
      : options.signal ?? deadlineSignal;

  const response = await fetch(url, { signal });
  const raw = await response.json();
  return raw as T;
}
```

**Reliability rule**:

- Every long-running async boundary should decide:
  - how cancellation arrives
  - how deadlines are enforced
  - how abort reasons are surfaced

---

### 16. Feature-Collocated Query Layer

**Score: 90/100**

**Pattern**: Keep server-state fetching close to the feature that owns it, use stable query keys, and let a query library manage freshness, retries, and invalidation.

**Why it matters**:

- reduces duplicate fetch logic
- reduces cache inconsistency bugs
- makes invalidation explicit instead of magical

**Reference signals**:

- React synthesis scores `Observer-Based-Query-Hook` at **98**
- `Feature-Collocated-Query-Layer` scores **92**

**Reliability rule**:

- Server state is not local component state.
- Query keys are part of your contract surface.

---

### 17. Literal Exactness Preservation

**Score: 89/100**

**Pattern**: Preserve exact literal information in config helpers, tuples, and lookup tables using `as const` and `const` type parameters when appropriate.

**Why it matters**:

- widened types lose information LLMs and compilers could have used
- exact literals improve route tables, action maps, event names, and tuple APIs
- readonly exactness prevents accidental mutation of declarative metadata

**Reference signals**:

- official TypeScript 5.0 documentation introduced `const` type parameters

**Preferred shape**:

```typescript
export function defineRoutesPrecisely<
  const TRoutes extends Record<string, { path: `/${string}`; authRequired: boolean }>
>(routes: TRoutes): TRoutes {
  return routes;
}

const applicationRoutes = defineRoutesPrecisely({
  home: { path: "/", authRequired: false },
  settings: { path: "/settings", authRequired: true },
});
```

**Reliability rule**:

- Preserve literals when the exact set of keys or values is part of the contract.

---

### 18. Layered Boundary Adapters

**Score: 89/100**

**Pattern**: Separate domain logic from transport, storage, and framework concerns.

**Suggested TypeScript adaptation**:

- **L1 Core**: domain types, invariants, pure functions
- **L2 Application**: use-cases, orchestration, ports
- **L3 Adapters**: HTTP, database, browser APIs, queues, providers

**Reference signals**:

- `design101-tdd-architecture-principles.md` pushes layered architecture and dependency injection
- Once Campfire analysis highlights clean layering and zero circular dependencies

**Preferred shape**:

```typescript
export interface UserRepositoryPort {
  findUserById(id: string): Promise<User | null>;
  saveUser(user: User): Promise<void>;
}

export class UpdateUserProfileUseCase {
  constructor(private readonly repository: UserRepositoryPort) {}

  async execute(command: UpdateUserProfileCommand): Promise<void> {
    const user = await this.repository.findUserById(command.userId);
    if (!user) throw new Error("User not found");
    const updated = applyUserProfileUpdate(user, command);
    await this.repository.saveUser(updated);
  }
}
```

**Reliability rule**:

- Frameworks should plug into your core, not colonize it.

---

## Tier B: High-Value Operational Patterns

### 19. Project-Reference Build Partitions

**Score: 85/100**

**Pattern**: Split large TypeScript repos into referenced composite projects with explicit dependency direction.

**Why it matters**:

- improves build times
- reduces editor memory and typecheck churn
- enforces logical separation between packages/modules
- gives LLMs clearer architectural partitions in large workspaces

**Reference signals**:

- official TypeScript project references documentation says they can greatly improve build times and enforce logical separation

**Preferred shape**:

```json
{
  "files": [],
  "references": [
    { "path": "./packages/core" },
    { "path": "./packages/app" },
    { "path": "./packages/web" }
  ]
}
```

**Reliability rule**:

- Small repos do not need this.
- Large repos benefit when the dependency graph becomes an explicit build contract.

---

### 20. Quota-Aware Storage Degradation

**Score: 88/100**

**Pattern**: Treat storage quota errors as a normal failure mode and design fallbacks.

**Why it matters**:

- browsers disagree on quota error names and codes
- storage can fail after long healthy periods
- graceful degradation is better than immediate app failure

**Reference signals**:

- OpenCode persistence notes score quota-aware storage at **91**
- includes cross-browser quota detection, eviction, memory fallback

**Reliability rule**:

- Failure mode order:
  1. write directly
  2. repair corrupted key
  3. evict old entries
  4. fall back to memory

---

### 21. Stable-Key Stream State Machines

**Score: 86/100**

**Pattern**: In streaming or event-heavy systems, do not assume every identifier is stable. Track state using the identifier that is stable across event boundaries.

**Why it matters**:

- logical operations can span multiple events
- provider IDs can rotate or be partial
- state machines need durable correlation keys

**Reference signals**:

- OpenCode stream notes use `output_index` instead of rotating item IDs

**Reliability rule**:

- Protocol correctness beats "looks unique enough."

---

### 22. Progressive Enhancement Minimal Client

**Score: 84/100**

**Pattern**: Keep core user journeys working with minimal client-side JavaScript whenever the product allows it.

**Why it matters**:

- fewer hydration and client-state failure modes
- lower dependency on fragile browser conditions
- smaller blast radius when JS fails

**Reference signals**:

- Once Campfire analysis highlights:
  - minimal JavaScript
  - progressive enhancement
  - zero circular dependencies
  - comprehensive test coverage

**Reliability rule**:

- If a feature does not need a client-side state machine, do not invent one.

---

## TypeScript Reliability SOP

### 1. Boundary Rule

- network
- local storage
- file system
- browser APIs
- worker messages
- queue payloads
- provider SDK responses

All of them enter the system as `unknown`.

### 2. Parsing Rule

- Define schema once
- Infer type from schema
- Parse at the boundary
- Pass typed data inward

### 3. Control-Flow Rule

- Use discriminated unions for state and protocols
- Use exhaustive `switch`
- Use `never` checks for impossible branches

### 4. Module Rule

- use `import type` for type-only imports
- prefer `verbatimModuleSyntax`
- keep runtime imports visibly runtime

### 5. Error Rule

- recoverable failures return explicit results
- invariant violations throw
- thrown values from `catch` are narrowed from `unknown`

### 6. Async Rule

- accept `AbortSignal` at async boundaries
- compose deadlines rather than inventing disconnected timers
- propagate cancellation downward

### 7. Persistence Rule

- version storage
- migrate on read
- preserve unknown future keys
- merge partial state carefully

### 8. Testing Rule

- unit for pure logic
- component for behavior
- integration for contracts
- e2e for journeys

### 9. Architecture Rule

- core logic stays framework-light
- adapters own IO details
- query/cache logic stays feature-local
- use project references when repo scale justifies explicit partitions

---

## Anti-Patterns To Avoid

These were rejected or intentionally de-emphasized because they score poorly for reliability:

1. **Type-only API contracts**
   - Interface without runtime parsing is false confidence.

2. **`any` at trust boundaries**
   - Short-term speed, long-term invisible corruption.

3. **Boolean soup state**
   - `isLoading && hasError && isEmpty` is weaker than a union.

4. **Shallow persisted-state merge**
   - Breaks nested defaults and schema drift.

5. **Framework-first business logic**
   - Hooks, routers, and SDK calls inside core invariants make testing harder.

6. **JS-required core journeys**
   - If login, navigation, or submission dies without client JS, failure surface is too wide.

7. **Single-layer testing**
   - Unit-only and e2e-only are both incomplete.

8. **Transport leakage**
   - If application code knows six provider quirks, normalization is missing.

9. **`as` used as a duct-tape strategy**
   - If `satisfies`, parsing, or a branded constructor can prove the shape, prefer that.

10. **Type/value import ambiguity**
   - If the code generator or bundler has to guess intent, the module boundary is underspecified.

11. **Stringly typed IDs**
   - `userId`, `orderId`, and `workspaceId` should not all be bare `string`.

12. **Timeouts without cancellation propagation**
   - A timer that aborts nothing is observability theater.

---

## Pre-Commit Reliability Ritual

Use a ritual like this before merging:

```bash
pnpm exec tsc --noEmit
pnpm exec eslint . --max-warnings=0
pnpm exec vitest run
pnpm exec playwright test
```

Then manually verify:

- all new external inputs are parsed at the boundary
- no new `any` leaked into core logic
- new unions are handled exhaustively
- persisted shapes are version-tolerant
- retries, timeouts, and loading states are explicit

---

## Repo Alignment Notes

To stay in the same spirit as this repository:

1. **4WNC still applies**
   - Prefer four semantic segments in names where possible.
   - TypeScript examples in this document follow that spirit:
     - `parseUserProfileSafely`
     - `handleStreamEventExhaustively`
     - `normalizeProviderResponseStrictly`
     - `mergePersistedStateForward`

2. **Executable specs beat vague tickets**
   - For important flows, write contracts with:
     - preconditions
     - postconditions
     - error conditions
     - verification path

3. **Mermaid-only diagrams if visuals are added later**
   - Keeps GitHub rendering predictable.

---

## Source Trail

Primary notes explored:

- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/MERN-TypeScript-IdiomaticPatterns_20251206.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/Idiom96-polyglot-basic-patterns-20251205.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/Idiom-DotNet-CSharp-Angular-TypeScript-Patterns.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/IdiomaticPatterns2026/React/03-SYNTHESIS-ReactPatternsCatalog-2026.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/05_Code_Analysis_Testing/opencode-data-flow-analysis.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/03_API_Documentation_Specs/opencode-genius-idiomatic-patterns__76d4afea.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/schemas.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/05_Code_Analysis_Testing/once-campfire-architecture-analysis.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/design101-tdd-architecture-principles.md`

Primary verification references:

- TypeScript official docs for:
  - assertion functions
  - type-only imports/exports
  - `useUnknownInCatchVariables`
  - `satisfies`
  - `const` type parameters
  - project references
  - `verbatimModuleSyntax`
- MDN docs for:
  - `AbortController`
  - `AbortSignal.timeout()`
  - abort-aware fetch patterns

---

## Final Synthesis

If you only remember seven things from this file, make them these:

1. **Strict compiler settings are non-negotiable**
2. **Type-only imports should be explicit**
3. **External data starts as `unknown`**
4. **Schemas define both runtime truth and inferred types**
5. **Unions should be exhaustive**
6. **Cancellation and deadlines should be explicit**
7. **Behavior-first tests are the final backstop**

That combination does more for reliable TypeScript than most style guides, framework trends, or "clean code" slogans.
