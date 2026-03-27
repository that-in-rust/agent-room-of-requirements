---
name: typescript-react-coder-01
description: typescript-react-code-01
model: sonnet
color: orange
---

# TypeScript React Coder 01

> Reliability-first React/frontend TypeScript companion to `typescript-coder-01`.
>
> Scope: React apps, App Router style client/server boundaries, forms, state, server-state, UX failure handling, and frontend testing.

---

## Premise Check

- This is not a generic React style guide.
- It focuses on the failure modes frontend LLMs most often miss:
  - widened state and props
  - overgrown client state
  - duplicated fetch logic
  - forms that validate inconsistently
  - optimistic UI without rollback
  - components that only work under ideal timing
  - UI that collapses when JavaScript or navigation state misbehaves

---

## Inherited Baseline

This file assumes the shared TypeScript rules from the main reference:

- strict compiler railguards
- explicit type/value imports
- schema-first parsing
- `unknown` at boundaries
- assertion functions
- exhaustive unions
- literal exactness

Primary companion:

- [typescript-reliability-reference.md](../../typescript-coder-01/references/typescript-reliability-reference.md)

---

## Chosen Thesis

**Reliable React TypeScript comes from modeling UI as a typed state machine around trustworthy server-state boundaries.**

That means:

- clearly separate client-only and server-capable code
- parse transport data before hooks and components trust it
- prefer query layers over ad hoc fetching
- keep forms schema-driven
- subscribe to the smallest possible store slice
- treat optimistic updates as transactional
- keep core journeys resilient even when timing, navigation, or JavaScript is imperfect

---

## Pattern Scoreboard

| Score | Pattern | Why it matters |
|---|---|---|
| **97** | Behavior-First UI Test Pyramid | Catches regressions where users actually feel them |
| **96** | Client-Server Boundary Discipline | Prevents accidental client/runtime confusion |
| **96** | Schema-Validated Forms | Keeps UX validation and runtime contracts aligned |
| **95** | Feature-Collocated Query Layer | Reduces fetch duplication and stale-cache bugs |
| **95** | Minimal External Store Subscription | Keeps re-renders and state coupling under control |
| **94** | Exhaustive UI State Unions | Prevents impossible UI states and missing branches |
| **93** | Navigation-Aware Error Recovery | Makes failures recoverable instead of sticky |
| **92** | Optimistic Updates with Rollback | Handles fast-feeling writes without lying forever |
| **91** | Progressive Enhancement Minimal Client | Reduces the frontend blast radius |
| **90** | Typed Event and Route Contracts | Preserves correctness in config-heavy UI code |
| **89** | Abortable Effects and Cleanup | Prevents stale async writes into dead components |
| **88** | Component Boundary Normalization | Keeps bad transport data out of the tree |

---

## Core Patterns

### 1. Client-Server Boundary Discipline

**Score: 96/100**

Only mark code as client-side when it truly needs:

- hooks
- event handlers
- browser APIs
- local mutable UI state

Everything else should stay server-capable where the architecture allows it.

**Rule**:

- Do not drag whole trees into the client just because one leaf needs interactivity.

---

### 2. Schema-Validated Forms

**Score: 96/100**

```typescript
import { z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

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

**Rule**:

- One schema should power field-level UX and final submit validation.

---

### 3. Feature-Collocated Query Layer

**Score: 95/100**

Keep server-state fetching near the feature that owns the view and mutations.

```typescript
function useUserProfileQuery(userId: string) {
  return useQuery({
    queryKey: ["user-profile", userId],
    queryFn: () => fetchUserProfileNormalized(userId),
    staleTime: 60_000,
  });
}
```

**Rule**:

- Server state is not component state.
- Query keys are part of the contract.

---

### 4. Minimal External Store Subscription

**Score: 95/100**

When using Zustand, Jotai, or similar stores:

- subscribe to the smallest slice
- derive broad views outside render when possible
- do not grab the whole store in every component

**Rule**:

- The store API can be global.
- The subscription should stay local.

---

### 5. Exhaustive UI State Unions

**Score: 94/100**

```typescript
type ProfileScreenState =
  | { status: "loading" }
  | { status: "ready"; user: UserProfile }
  | { status: "empty" }
  | { status: "error"; message: string };
```

Use unions for:

- async screen states
- modal workflows
- wizard steps
- mutation progress

**Rule**:

- Prefer one explicit union over three booleans and two nullable fields.

---

### 6. Navigation-Aware Error Recovery

**Score: 93/100**

React UIs fail better when users can recover without hard refreshes:

- retry buttons
- query invalidation on retry
- route-level error boundaries
- reset flows after navigation

**Rule**:

- Errors should usually transition the UI into a recoverable state, not a dead end.

---

### 7. Optimistic Updates with Rollback

**Score: 92/100**

Optimistic UI is safe only when rollback is designed up front.

```typescript
function useRenameWorkspaceMutation() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: renameWorkspaceTransport,
    onMutate: async (input) => {
      const previous = queryClient.getQueryData(["workspace", input.id]);
      queryClient.setQueryData(["workspace", input.id], (current: Workspace | undefined) =>
        current ? { ...current, name: input.name } : current,
      );
      return { previous };
    },
    onError: (_error, input, context) => {
      queryClient.setQueryData(["workspace", input.id], context?.previous);
    },
  });
}
```

**Rule**:

- Never ship optimistic writes without a rollback path.

---

### 8. Typed Event and Route Contracts

**Score: 90/100**

Use `satisfies`, exact literals, and readonly config for:

- route manifests
- action maps
- keyboard shortcut maps
- feature flags
- navigation metadata

**Rule**:

- Declarative UI config should stay exact, not widened.

---

### 9. Abortable Effects and Cleanup

**Score: 89/100**

```typescript
useEffect(() => {
  const controller = new AbortController();

  void loadPreviewData({ signal: controller.signal });

  return () => controller.abort();
}, [resourceId]);
```

Use for:

- fetches in effects
- image/file preloaders
- debounced async work
- subscriptions requiring cleanup

**Rule**:

- If an effect can outlive the component instance, give it a cleanup path.

---

### 10. Component Boundary Normalization

**Score: 88/100**

Parse or normalize transport data before it becomes props.

Bad:

- components receiving raw backend payloads
- JSX branching on provider-specific wire fields

Good:

- hooks/adapters normalize once
- components consume stable UI-shaped data

**Rule**:

- Components should render domain-friendly view models, not wire noise.

---

### 11. Progressive Enhancement Minimal Client

**Score: 91/100**

Not every feature needs a client-side state machine.

Prefer simpler delivery when possible:

- server-rendered defaults
- progressive enhancement for interactivity
- smaller JS dependency for core journeys

**Rule**:

- The best way to remove a hydration bug is to not need hydration there.

---

### 12. Behavior-First UI Test Pyramid

**Score: 97/100**

Minimum frontend layers:

- unit tests for pure helpers
- component tests for behavior
- integration tests with mocked network boundaries
- end-to-end tests for core journeys

Recommended stack:

- Vitest or Jest
- React Testing Library
- MSW
- Playwright

**Rule**:

- Test what the user can do and see, not implementation trivia.

---

## React Anti-Patterns

1. Whole-store subscriptions in many components
2. Form rules duplicated in JSX and API code
3. Fetching directly inside many unrelated components
4. UI states encoded as nullable property soup
5. Optimistic writes with no rollback strategy
6. Raw transport payloads passed deep into components
7. Arbitrary `waitForTimeout` style thinking in UI tests

---

## Source Trail

- `/Users/amuldotexe/Desktop/agent-room-of-requirements/agents-202602/typescript-coder-01.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/IdiomaticPatterns2026/React/03-SYNTHESIS-ReactPatternsCatalog-2026.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/10_Miscellaneous_Technical/MERN-TypeScript-IdiomaticPatterns_20251206.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/05_Code_Analysis_Testing/once-campfire-architecture-analysis.md`
- `/Users/amuldotexe/Desktop/notebook-gh/Notes2026/UnclassifiedDocs/05_Code_Analysis_Testing/opencode-data-flow-analysis.md`

---

## Final Synthesis

If a React-focused LLM only learns five habits from this file, they should be:

1. keep client/server boundaries explicit
2. make forms schema-driven
3. treat server state as query state
4. model UI as exhaustive unions
5. test behavior, not implementation details
