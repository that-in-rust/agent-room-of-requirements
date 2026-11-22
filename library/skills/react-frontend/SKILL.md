---
name: react-frontend
description: >-
  Reliability-first React with TypeScript, Three.js / react-three-fiber / react-force-graph
  visualisation, and front-end design quality: decide the client boundary, sort state into
  server, app and scene lanes, model screens as exhaustive unions, keep forms schema-driven,
  keep per-frame work out of React, choose one coherent visual direction, and prove the
  result in a real browser. Use when the task touches .tsx or .jsx files, hooks, Zustand or
  TanStack Query code, zod or react-hook-form forms, a canvas, WebGL scene, force graph,
  camera or picking code, Tailwind or CSS for a component, Vitest / React Testing Library /
  MSW / Playwright front-end tests, or when asked to "build this component", "fix the
  re-render storm", "add optimistic update", "the graph is slow", "make this page look
  designed", "review this React diff" or "check it on mobile". Not for Node or server-only
  TypeScript, tsconfig and compiler policy (use typescript-backend), not for static diagram
  or slide pages (use visual-explainers), not for generative art or image prompts (use
  generative-art-and-images), and not for product discovery or brand strategy decisions.
---

# React Frontend

This skill builds, refactors and reviews React user interfaces in TypeScript, including 3D scenes and force graphs, and holds them to a design-quality bar that is checked in a browser.
It treats the UI as a typed state machine around trustworthy server-state boundaries, keeps the mutable per-frame 3D world out of React's render path, and accepts a screen only on rendered evidence.

## When to use and when not

Use it for:

- `.tsx` components, hooks, route modules, App Router style client/server split decisions.
- Forms, query or cache layers, optimistic mutations, external stores, route contracts, event payloads.
- 3D canvases, graph exploration, camera controls, scene state, realtime visual interaction in React.
- Building or refining a known component, page, app, dashboard, portal, editor or game, followed by browser verification.
- Reviews that ask whether the UI survives slow data, bad data, retries, navigation changes, growth in data volume, or a narrow viewport.

Requests that should trigger it:

1. "Implement the workspace rename with an optimistic update and make sure it rolls back on a 500."
2. "Design or implement this React plus Three.js visualisation with clean state boundaries and performance-aware rendering."
3. "Hover on the force graph re-renders the whole sidebar. Fix it."
4. "Build the exceptions dashboard. It must look like a real product, not a template, and work on a phone."
5. "Review this `.tsx` diff: are there impossible states, missing cleanup, or untested journeys?"

Requests that should not trigger it:

1. "Tighten `tsconfig` strictness and fix the Express handlers." Use `typescript-backend`.
2. "Make an architecture diagram page for the workshop." Use `visual-explainers`.
3. "Who are our users and what should the product do?" That is product discovery; this skill only supplies evaluation criteria for it.

Also out of scope: legal, medical, financial, privacy or regulated content decisions; product-wide design-system replacement without an owner, consumer inventory and migration plan; exploratory prototypes that have no reliability requirement. A keyword such as "dashboard" or "redesign" never authorises a redesign on its own.

## Pick the part and the mode

The subject has three parts. Most tasks use more than one. Pick the lead part by where the hard problem sits.

| Part | Pick it when | Lead question |
|---|---|---|
| A. React reliability | components, hooks, forms, queries, mutations, stores, tests | Can the UI reach an impossible or unrecoverable state? |
| B. Three.js scene | canvas, WebGL, react-three-fiber, react-force-graph, camera, picking, large scenes | Which paradigm owns each object: React's re-render or the scene's frame loop? |
| C. Design quality | look and feel, layout, responsive behaviour, accessibility, visual review | Who is doing what, in which states, and what rendered evidence would expose failure? |

If the request is mostly look and feel rather than 3D systems, lead with C and pair B. If a data-sounding question is about node identity, label culling or graph layout, it is B. Plain component state inside a 3D app is A.

Working modes:

- **Planning only**: no file changes; hand back the plan sections of the output contract.
- **End-to-end implementation**: full workflow below.
- **Focused correction**: fix the named state or defect; no unrelated redesign; reduced evidence profile.
- **Design exploration**: isolated, labelled with assumptions and gaps; never promoted to production without the gates.
- **Review**: start from the anti-pattern list, not the pattern list.
- **Recovery / incident**: open the specific recovery or cleanup rule directly; do not walk the whole workflow during a live incident.

Evidence profiles: *focused* (authority, affected state, reproduction, scoped change, rendered regression), *standard* (adds workflow, state matrix, responsive and accessibility checks, visual system, recovery), *high-assurance* (adds domain owner, localisation, zoom, assistive technology, device and browser matrix, security, privacy, rollback, accountable acceptance). No profile supports a claim outside its matrix.

## Workflow

1. **Read the request and the repository.** Instructions, framework, routes, existing components, tokens, icons, tests, pinned versions in `package.json`. Decide reuse, adapt or diverge. In a mature product, reuse is the default; diverge only for a named failure or an owned migration.
2. **State the task.** User, job, frequency, consequence, non-goals. If behaviour, audience or authority is undecided, stop and ask, or build a labelled prototype.
3. **Decide the client boundary.** Mark code client-side only when it needs hooks, event handlers, browser APIs or local mutable UI state. Record the decision. This step is load-bearing: skipping it drags whole trees into the client.
4. **Split state into lanes.**
   - *Server state*: fetched data, subscriptions, cache invalidation.
   - *App state*: selection, filters, layout mode, panel visibility.
   - *Scene state*: mutable objects, camera state, transient hover, animation data.
   The lane chooses the container: query layer, store, or scene ref.
5. **Shape the data model before visuals.** Typed transport payloads, a pure adapter, typed nodes, edges, selections and view models. Rendering code never parses raw transport shapes.
6. **Model the states.** Write one discriminated union per screen or workflow. Cover the states that apply: default, loading, empty, partial, error, disabled, permission denied, offline or disconnected, pending, success, recovery.
7. **Set constraints.** Accessibility, keyboard paths, content lengths, viewports and containers, browsers, locale, performance budget and its owner, security and data limits.
8. **Choose one visual direction** (part C). A small coherent system of type, colour roles, density, composition, media and motion that fits the product mode.
9. **Implement behaviour with repository-native pieces**, in dependency order: types, adapter, query hooks or store, hooks, components, scene, overlays. Apply the default patterns in this order: schema-validated forms, feature-collocated query layer, exhaustive UI unions, minimal store subscriptions, navigation-aware error recovery, rollback-ready optimistic updates.
10. **Refine.** Stable dimensions, responsive transformations, hierarchy, assets, micro-interaction. Polish after behaviour works.
11. **Verify in layers.** Static checks, unit and component tests, network-boundary integration tests, end-to-end journeys, then rendered evidence at the named viewports with console and network inspected. For a scene: loading, empty, degraded and disconnected states, camera reset, selection persistence across refresh, event cleanup, behaviour as data volume grows, WebGL fallback.
12. **Hand back** the output contract below, with what was not verified stated plainly.

A one-line fix may collapse steps 2 to 8 into one sentence each, if that judgement is recorded. A mock-data visual spike is acceptable only when its shape is the eventual typed shape.

## Rules

### Baseline TypeScript (inherited)

Strict compiler settings; explicit type and value imports; schema-first parsing; `unknown` at boundaries; assertion functions; exhaustive unions; literal exactness. Loose compiler settings recreate widened state. Compiler policy itself belongs to `typescript-backend`.

### Client and server boundary

- Do not drag a whole tree into the client because one leaf needs interactivity.
- Not every feature needs a client-side state machine. Prefer server-rendered defaults, progressive enhancement and a smaller JavaScript dependency for core journeys. The best way to remove a hydration bug is to not need hydration there.
- Default to server-capable code. Deviate with a written reason.

### State

- Prefer one explicit union over three booleans and two nullable fields. Use unions for async screen states, modal workflows, wizard steps and mutation progress.
- Lift shared state to the lowest common ancestor. Compute derived state during render; use `useMemo` only when the computation is expensive.
- Do not mirror props into state. Use a controlled component (`value`, `onChange`), or `key={initialValue}` when a reset on change is intended.
- Pass an initialiser function to expensive `useState`: `useState(() => createExpensiveArray())`.
- The store API can be global. The subscription should stay local: subscribe to the smallest slice, derive broad views outside render, never grab the whole store.
- Use the store for durable app state, not for every transient pointer movement.
- Context is for cross-cutting concerns only (authentication, theme or locale, feature flags, a WebSocket connection). Keep it single-purpose and typed, at most two levels deep, split by change frequency, with memoised provider values. A consumer hook throws when used outside its provider.

### Server state

- Server state is not component state. Query keys are part of the contract.
- Keep fetching next to the feature that owns the view and its mutations. Prefer a query layer to ad hoc fetching.
- Parse or normalise transport data before it becomes props. Components render domain-friendly view models, not wire noise.
- Check `response.ok` and throw `HTTP ${status}: ${statusText}`; set an error state the UI can show.
- Never ship an optimistic write without a rollback path, even for a low-stakes toggle. Treat it as a transaction: snapshot, apply, restore on error. Complete the rollback before any retry.
- Errors move the UI into a recoverable state, not a dead end: retry buttons, query invalidation on retry, route-level error boundaries, reset flows after navigation.

### Forms

- One schema powers field-level feedback and final submit validation. Do not duplicate form rules in JSX and API code.

### Effects and cleanup

- `useEffect` synchronises with something external. `useLayoutEffect` reads layout or focuses before paint. Deriving values, responding to a user event and transforming data are not effects.
- If an effect can outlive the component instance, give it a cleanup path: `AbortController` for fetches, `clearInterval` for timers, unsubscribe for subscriptions, close for sockets.
- Guard state writes after an await with `!signal.aborted`; ignore `AbortError`.
- Depend on primitives or memoised objects; an object prop recreated on every render makes the effect loop.

### Components and lists

- Composition and children over prop explosion. Compound components (`Card.Header`, `Card.Body`, `Card.Footer`) beat twenty configuration props.
- Containers own route params, fetching, mutations and side effects. Presenters are pure and easy to test.
- Stable unique keys (`item.id`). Never an array index for a dynamic list.
- Do not define components inside render. Hoist constant objects and styles outside the component.
- Virtualise lists in the thousands; prefer server-driven pagination when the backend can bound the data.

### Memoisation

Default to unmemoised simplicity. Memoise only for a named row. The 100 ms threshold is a rule of thumb, not a measurement:

| Scenario | Choice |
|---|---|
| Expensive computation (over 100 ms), or object/array whose reference is a dependency | `useMemo` |
| Referential equality needed for a dependency | `useMemo` |
| Callback passed to a memoised or identity-sensitive child | `useCallback` |
| Callback passed to a normal child | none |
| Frequently re-rendered list item | `React.memo` |
| Infrequent re-render (under once per second), primitive computation | none |

### Scene (Three.js, react-three-fiber, force graphs)

- React owns structure and orchestration: layout, composition, panels, controls, suspense boundaries. The scene layer owns mutable meshes, materials, camera interpolation and transient hover.
- Do not put large mutable Three.js objects in React state. Do not use React state as a generic container for scene objects.
- Keep render-loop work in scene hooks or frame handlers (`useFrame`, a render-loop callback), not in parent re-renders. Hover and animation churn must not re-render the app shell.
- No global store writes on hover or per frame. Selection belongs in the store; transient hover belongs in a scene ref. Mirroring camera state to the store at interaction end is a deliberate, documented crossing.
- Do not hide expensive scene transforms inside JSX without measuring the cost.
- Treat camera, controls and picking as first-class interaction systems. Bound camera animation so repeated events cannot queue visual thrash.
- Select by stable id, not object identity: a data refresh rebuilds node objects and identity-based selection silently empties.
- Dispose explicitly: geometry, every material, every texture map, listeners, sockets, observers, the renderer. Garbage collection does not free GPU resources. `scene.remove(mesh)` alone leaks.
- Never allocate `Vector3`, `Quaternion` or `Matrix4` per frame; reuse module-level scratch objects. Clamp the frame delta (`Math.min(delta, 0.1)`).
- Reuse geometries and materials. Use `InstancedMesh` for thousands of identical objects. Use `ResizeObserver` on the container, not only `window.onresize`. One `WebGLRenderer` per canvas.
- Add a graceful fallback for no-WebGL or low-power devices when the view is core to the product.
- Lane purity shows in imports: the store imports no Three.js, the canvas imports no fetch, the adapter imports neither React nor Three.js.

### Design quality

- Design the task, not the screen. A landing page cannot stand in for a requested app.
- Reuse the product's language deliberately. A second, unowned design system is a defect.
- States are first-class: every material async or data state has a coherent UI.
- Accessibility is behaviour: native semantics, accessible names (also for icon-only controls), visible focus, equivalent keyboard, pointer and touch paths, announcements, zoom, contrast, reduced motion. Never state by colour alone.
- Choose one visual point of view and match expression to product mode. Boldness means a few memorable, relevant choices. Restraint means precise hierarchy, not generic emptiness.
- Familiar controls for repeated commands.
- Responsive behaviour is structural: transform the layout, do not shrink the desktop. Test long, localised and error content. Reserve stable dimensions for controls, toolbars and status areas.
- Colour needs semantic roles and non-colour cues. Motion needs a causal role, must be interruptible and must respect reduced motion. Overlap must be safe for DOM order, focus, zoom and long content.
- Show the real subject. Decorative media that hides the product, place or person fails.
- Observe pixels and interactions. A green build, a token set or a screenshot alone is not proof.

### Naming

The owner's convention is four semantic words per name. See "Where the sources disagree" for when it binds.

| Kind | Shape | Good | Too short |
|---|---|---|---|
| Function (camelCase) | verb + constraint + target + qualifier | `transformDiffToForcegraph`, `fetchWorkspaceListData`, `parseJsonResponseSafely` | `transformDiff`, `handleToggle`, `createManager` |
| Component (PascalCase) | Entity + Context + Purpose + Variant (3-4 words accepted in the visualisation code) | `WorkspaceListSidebar`, `DiffGraphCanvasView`, `UserProfileCardCompact` | `Sidebar`, `Graph`, `UserCard` |
| Hook | `use` + Domain + Action + Qualifier | `useWorkspaceListData`, `useWebsocketDiffStream`, `useFormValidationErrors` | `useWorkspaces`, `useWebsocket`, `useAuth` |
| Event handler | `handle` + Target + Event + Action | `handleFormSubmitValidation`, `handleWorkspaceWatchToggle` | `handleSubmit`, `handleClick` |
| Store | noun + `Store` or `State` | `workspaceStore`, `diffVisualizationStore`, `connectionStateStore` | `store`, `state` |
| Scene object | Entity + Geometry + Material + Purpose | `TerrainMeshHeightmapped`, `BuildingGroupInstanced` | `Terrain`, `Player` |
| Scene function | verb + target + operation/property + qualifier | `disposeSceneResourcesComplete`, `updateCameraPositionSmooth`, `tweenOpacityFadeOut` | `update`, `dispose`, `load` |

Six or more units is also wrong: `UserProfileCardWithAvatarAndStatusBadge`.

### Import layers

- Components: `Pages -> Features -> UI -> Primitives`. Allowed: `pages -> features`, `features -> ui`, `ui -> primitives`, `hooks -> utils`, `components -> hooks`, `components -> types`. Forbidden: skipping a layer, reverse imports (`ui -> features`), any import out of `primitives`, cycles.
- Imperative Three.js code: `Application -> Managers -> Components -> Utils -> THREE.*`. Forbidden: application code importing utilities or `THREE.*` directly, manager cycles, `Utils -> Components`.

### Tests

- Test what the user can do and see, not implementation trivia.
- Layers: unit tests for pure helpers; component tests for behaviour; integration tests with mocked network boundaries; end-to-end tests for core journeys. Stack: Vitest or Jest, React Testing Library, MSW, Playwright.
- Stable selectors: `data-testid` in `noun-noun` form (`submit-button`, `email-input`, `error-message`), never class or tag selectors. Use a page-object model when the end-to-end suite grows.
- No arbitrary `waitForTimeout`. Wait on a visible state or a network response.
- Every liveness or loading condition has a rendered representation and a test id: connection status, data freshness, loading, empty, degraded, disconnected, fallback.
- A canvas makes direct assertions hard: assert the DOM shell and canvas visibility, mock the API, and use screenshot comparison only when pixels are the contract. A visible canvas is not a sufficient green check.

## Part A: React reliability

The twelve patterns are reliability countermeasures ordered by failure cost, not style options. Scores are the owner's editorial calibration, not measurements.

| Score | Pattern | Why it matters |
|---|---|---|
| 97 | Behaviour-first UI test pyramid | Catches regressions where users feel them |
| 96 | Client-server boundary discipline | Prevents accidental client/runtime confusion |
| 96 | Schema-validated forms | Keeps UX validation and runtime contracts aligned |
| 95 | Feature-collocated query layer | Reduces fetch duplication and stale-cache bugs |
| 95 | Minimal external store subscription | Keeps re-renders and state coupling under control |
| 94 | Exhaustive UI state unions | Prevents impossible UI states and missing branches |
| 93 | Navigation-aware error recovery | Makes failures recoverable instead of sticky |
| 92 | Optimistic updates with rollback | Fast-feeling writes without lying forever |
| 91 | Progressive enhancement, minimal client | Reduces the front-end blast radius |
| 90 | Typed event and route contracts | Preserves correctness in config-heavy UI code |
| 89 | Abortable effects and cleanup | Prevents stale async writes into dead components |
| 88 | Component boundary normalisation | Keeps bad transport data out of the tree |

Greenfield work applies all twelve. Legacy triage goes in descending score. The order is a default: progressive enhancement outranks optimistic rollback in a content-heavy app and the reverse in an interaction-heavy one; abortable effects move up when background-fetch timing dominates incidents. Do not start with memoisation while form validation is inconsistent.

Failure modes this part exists to catch: widened state and props; overgrown client state; duplicated fetch logic; forms that validate inconsistently; optimistic UI without rollback; components that only work under ideal timing; UI that collapses when JavaScript or navigation state misbehaves.

Typed contracts: use `satisfies`, exact literals and readonly config for route manifests, action maps, keyboard shortcut maps, feature flags and navigation metadata. Declarative UI config stays exact, not widened.

Five habits, if nothing else is remembered: explicit client/server boundaries; schema-driven forms; server state as query state; UI as exhaustive unions; test behaviour, not implementation.

## Part B: Three.js, react-three-fiber and force graphs

Ownership split:

| Layer | Owns |
|---|---|
| React | layout, composition, panels, controls, suspense boundaries |
| Query layer | remote fetch and cache lifecycle |
| Store layer | user-visible app state worth preserving across components |
| Scene layer | mutable meshes, materials, camera interpolation, transient hover |

Build order for a graph view: typed transport payloads, pure adapter, store with an actions object and selector exports, WebSocket hook with reconnect and a resubscription ref, scene component with memoised accessors and camera focus on click, then verification and DOM-shell end-to-end specs. A reconnect must resubscribe: a socket that reopens without resubscribing looks healthy while delivering nothing.

Keep the scene composable: separate data hooks, stores, scene components, overlays and controls; feature-level modules, not one canvas component. Keep overlays and inspector panels outside the render loop.

Force graph and scene checklist (ask all fourteen in review):

- *Interaction*: Is selection stable after data refresh? Can the user recover orientation with reset or fit-to-view? Are hover and click distinct in code and behaviour? Does keyboard or panel navigation mirror what the pointer can do?
- *Data volume*: Can labels be culled or simplified? Can expensive node geometry degrade at high counts? Are derived metrics cached instead of recomputed per frame?
- *Rendering*: Are materials and geometries reused? Are heavy textures, sprites or labels lazily enabled? Is camera animation bounded so it cannot thrash on repeated events?
- *Reliability*: Does the canvas handle disconnects, empty graphs and partial data? Are subscriptions and animation loops torn down on unmount? Is there a plain fallback if WebGL is unavailable?

Performance: attribute cost to a lane before changing code. React lane: memoised callbacks and selectors. Scene lane: cached metrics, instancing, pooling, culling, reusable materials, degrading geometry, delta-clamped loops. Socket lane: debouncing. Instancing cannot fix store-driven shell re-renders; memoisation cannot fix per-frame allocation. Count re-renders first: a hover wired to the store shows shell churn before the frame rate drops. Lazy-load the 3D view with `React.lazy`.

Stack the owner's examples were written against (a dated, tested-together snapshot; verify each pin against the target repository before relying on an API): React 18.x, TypeScript 5.x, react-force-graph-3d 1.24.x, zustand 4.x, @tanstack/react-query 5.x, tailwindcss 3.x, vite 5.x, Playwright.

## Part C: Design quality

Sequence, with the condition that stops each stage:

| Stage | Decide | Stop or route when |
|---|---|---|
| Understand product | user, job, context, content, frequency, consequence | behaviour, audience or authority undecided |
| Inspect system | routes, components, tokens, assets, tests, rendered behaviour | a parallel design system has no owner |
| Model states | the state graph | a static composition hides runtime behaviour |
| Establish constraints | accessibility, keyboard, content, viewport, browser, locale, performance, security, data | a target or domain owner is needed |
| Choose direction | type, colour, density, composition, media, motion | novelty conflicts with trust, readability or conventions |
| Implement behaviour | native components, semantics, controls, recovery | a placeholder or decorative facade replaces the app |
| Refine | stable dimensions, responsive constraints, hierarchy | hidden overflow, inaccessible semantics, brittle positioning |
| Verify | behaviour, keyboard, desktop and mobile renders, console | source looks plausible but pixels or state are unobserved |

Choosing a direction:

- Write down purpose, tone, constraints and the one thing a person should remember. Commit to it before code. Intent matters more than intensity; a maximal and a minimal direction can both be right.
- Typography: a deliberate pairing that fits glyph coverage, loading and brand. Colour: neutral, semantic and accent roles as CSS variables; a dominant colour with a sharp accent reads better than an evenly spread palette. Motion: a few high-impact moments, such as one staggered reveal on load, in CSS where that is enough. Composition: either generous space or controlled density, chosen on purpose.
- Detail: backgrounds, texture, shadow and border treatment belong to the direction; they are not filler. Asymmetry, overlap or a broken grid are available where the content stays safe.
- Signs of an undirected result: the default font stack, a stock gradient on white, a predictable layout, the same choices as the last project.
- Match implementation effort to the direction: an elaborate direction needs elaborate code; a refined one needs precision in spacing and type.
- Product mode sets the bias: *operational* tools favour repeated action, scanability, density and recovery; *commerce* favours product, trust, forms and totals; *editorial* favours reading and media; *brand, place or person* foregrounds the literal subject and real media; *editors* favour a stable workspace, tools and undo; *games and 3D* favour legible play, input, feedback and performance.

Reject: a preselected aesthetic, app-to-landing substitution, missing material states, wrong control semantics, nested or decorative card and pill overload, overflow, generalising from one viewport, harmful motion, hidden or broken subject media, source-only or build-only proof, a parallel design system.

Evidence states for any claim: `source_observed`, `design_inference`, `specified`, `rendered_for_scope`, `verified_for_scope`, `unresolved`, `invalidated`. Compiling without rendering is not `rendered_for_scope`. Never report "looks polished", or an unscoped "accessible" or "responsive".

## Where the sources disagree

Keep both positions. The selector says which applies.

| Topic | Position 1 | Position 2 | What selects |
|---|---|---|---|
| Remote data | Zustand store actions fetch and hold `isLoading` / `error` | TanStack Query owns remote data; Zustand holds only durable app state | Position 2 when the data needs caching, deduplication, invalidation or optimistic writes, or the repository already has a query layer. Position 1 for a small app or an existing store-based code base; keep the `response.ok` check and selector hooks. |
| Fetch in an effect | A hook with `useEffect` returning a `FetchState` union | Query layer over ad hoc fetching | Effect hook only where no query library exists or when teaching the union; always abortable. |
| Four-word names | Mandatory for functions, hooks, handlers, components, scene objects | A team choice, not required | Binding in the owner's repositories and where the project already follows it; elsewhere follow the repository's convention. Components: exactly four units in the general rule, three to four accepted in the visualisation code. |
| Directory layout | `stores/ hooks/ components/{Layout,Visualization,Details}/ utils/ types/ e2e/` | `components/{layout,scene,panels}/ hooks/ stores/ services/{api,adapters}.ts types/graph.ts`; or `pages/ features/ ui/ primitives/` | Follow the existing tree. For a new scene app use the second; for a layered product use the third. |
| Importing `three` | Application code never imports `THREE.*`; manager classes wrap it | react-three-fiber scene components import it directly | Imperative manager architecture selects position 1; R3F selects position 2. Either way the lanes and frame-budget ownership stay. |
| Scene mechanics | Class-based scene manager, object pools and a hand-written render loop | react-three-fiber owns the scene graph and the loop; `useFrame` and `useLoader` replace the managers | A plain Three.js code base keeps the managers. In R3F keep the mechanics that still apply (disposal, scratch objects, instancing, delta clamp) and drop the manager classes. |
| Callbacks | Memoise callbacks passed to `ForceGraph3D` | Callback to a normal child: no memo | The graph component is identity-sensitive: new accessor functions trigger re-evaluation. Ordinary children are not. |
| Visual boldness | Commit to a bold, distinctive direction; avoid default fonts and stock palettes | Novelty is never evidence; reuse the current system; familiar controls | Greenfield, brand, marketing or creative surfaces with no governing design system select position 1. Mature products and high-frequency operational tools select position 2. |
| Socket events | Debounce rapid WebSocket events before updating state | Debouncing is wrong when lateness matters | Visualisation: debounce. Alerting: do not. |
| Index keys | Safe in a static, never-reordered list | Forbidden | Use a stable id everywhere; the exception is not worth teaching. |
| Latency target | Local interaction p95 under 100 ms | A target without workload, device, sample and owner is not a budget | Treat 100 ms as a starting proposal (not measured); it becomes a gate only when an owner fixes the workload. |

## Templates

### Screen state union and exhaustive render

```tsx
type ProfileScreenState =
  | { status: "loading" }
  | { status: "ready"; user: UserProfile }
  | { status: "empty" }
  | { status: "error"; message: string };

function renderProfileScreenContent(state: ProfileScreenState): JSX.Element {
  switch (state.status) {
    case "loading": return <LoadingSpinnerIndicator />;
    case "ready":   return <UserProfilePresenterPure user={state.user} />;
    case "empty":   return <EmptyProfilePlaceholderMessage />;
    case "error":   return <ErrorMessageDisplay message={state.message} />;
    default: {
      const unreachable: never = state;
      return unreachable;
    }
  }
}
```

### Schema-validated form

```tsx
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
      <input data-testid="email-input" {...form.register("email")} />
      <input data-testid="password-input" type="password" {...form.register("password")} />
      <button data-testid="submit-button" type="submit">Sign in</button>
    </form>
  );
}
```

### Query hook and optimistic mutation with rollback

```tsx
function useUserProfileQuery(userId: string) {
  return useQuery({
    queryKey: ["user-profile", userId],
    queryFn: () => fetchUserProfileNormalized(userId),
    staleTime: 60_000,
  });
}

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

### Abortable effect

```tsx
useEffect(() => {
  const controller = new AbortController();

  void loadPreviewData({ signal: controller.signal });

  return () => controller.abort();
}, [resourceId]);
```

Use it for fetches in effects, image and file preloaders, debounced async work, and subscriptions that need cleanup.

### Store with an actions object and selector hooks

```typescript
// stores/workspaceStore.ts
import { create } from 'zustand';

interface WorkspaceState {
  workspaces: WorkspaceMetadata[];
  selectedWorkspaceId: string | null;
  isLoading: boolean;
  error: string | null;
  actions: {
    fetchWorkspaceListData: () => Promise<void>;
    selectWorkspaceById: (id: string) => void;
    toggleWorkspaceWatchState: (id: string, enabled: boolean) => Promise<void>;
  };
}

export const useWorkspaceStore = create<WorkspaceState>((set, get) => ({
  workspaces: [],
  selectedWorkspaceId: null,
  isLoading: false,
  error: null,

  actions: {
    fetchWorkspaceListData: async () => {
      set({ isLoading: true, error: null });
      try {
        const response = await fetch('/workspace-list-all');
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        const data = await response.json();
        set({ workspaces: data.workspaces, isLoading: false });
      } catch (error) {
        set({ error: String(error), isLoading: false });
      }
    },

    selectWorkspaceById: (id) => {
      set({ selectedWorkspaceId: id });
    },

    toggleWorkspaceWatchState: async (id, enabled) => {
      const response = await fetch('/workspace-watch-toggle', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          workspace_identifier_value: id,
          watch_enabled_flag_status: enabled,
        }),
      });
      if (response.ok) {
        await get().actions.fetchWorkspaceListData();
      }
    },
  },
}));

// Selector hooks: one slice each, never the whole store
export const useWorkspaceList = () => useWorkspaceStore((s) => s.workspaces);
export const useSelectedWorkspaceId = () => useWorkspaceStore((s) => s.selectedWorkspaceId);
export const useWorkspaceActions = () => useWorkspaceStore((s) => s.actions);
```

When a query layer owns the remote data, the store keeps only `selectedWorkspaceId` and its action.

### Pure adapter from transport to scene data

```typescript
// utils/transformDiffToForcegraph.ts (or services/adapters.ts)
export function transformDiffToForcegraph(
  apiResponse: ApiDiffVisualization
): ForceGraphData {
  return {
    nodes: apiResponse.nodes.map((node) => ({
      id: node.id,
      name: node.label,
      nodeType: node.node_type,
      changeType: node.change_type,
      filePath: node.file_path,
      lineStart: node.line_start,
    })),
    links: apiResponse.edges.map((edge) => ({
      source: edge.source,
      target: edge.target,
      edgeType: edge.edge_type,
    })),
  };
}
```

### WebSocket hook with resubscription and capped backoff

```typescript
// hooks/useWebsocketDiffStream.ts
import { useState, useEffect, useCallback, useRef } from 'react';

type ConnectionStatus = 'connecting' | 'connected' | 'disconnected' | 'error';

interface UseWebsocketDiffStreamReturn {
  connectionStatus: ConnectionStatus;
  lastDiffEvent: DiffEvent | null; // DiffEvent: the typed event union from types/api.ts
  subscribe: (workspaceId: string) => void;
  unsubscribe: () => void;
}

const RECONNECT_DELAY_MS = 3000;
const MAX_RECONNECT_ATTEMPTS = 5;

export function useWebsocketDiffStream(): UseWebsocketDiffStreamReturn {
  const [connectionStatus, setConnectionStatus] = useState<ConnectionStatus>('disconnected');
  const [lastDiffEvent, setLastDiffEvent] = useState<DiffEvent | null>(null);
  const wsRef = useRef<WebSocket | null>(null);
  const subscribedWorkspaceRef = useRef<string | null>(null);

  useEffect(() => {
    let attempts = 0;
    let disposed = false;
    let retryTimer: ReturnType<typeof setTimeout> | undefined;

    const connect = () => {
      setConnectionStatus('connecting');
      const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      const ws = new WebSocket(`${protocol}//${window.location.host}/websocket-diff-stream`);
      wsRef.current = ws;

      ws.onopen = () => {
        attempts = 0;
        setConnectionStatus('connected');
        // Re-subscribe if we had a previous subscription
        if (subscribedWorkspaceRef.current) {
          ws.send(JSON.stringify({
            action: 'subscribe',
            workspace_id: subscribedWorkspaceRef.current,
          }));
        }
      };

      ws.onmessage = (event) => {
        try {
          setLastDiffEvent(JSON.parse(event.data));
        } catch (e) {
          console.error('Failed to parse WebSocket message:', e);
        }
      };

      ws.onerror = () => setConnectionStatus('error');

      ws.onclose = () => {
        if (disposed) return;
        if (attempts >= MAX_RECONNECT_ATTEMPTS) {
          setConnectionStatus('error'); // surface degraded status; no uncapped loop
          return;
        }
        setConnectionStatus('disconnected');
        retryTimer = setTimeout(connect, RECONNECT_DELAY_MS * 2 ** attempts);
        attempts += 1;
      };
    };

    connect();

    return () => {
      disposed = true;
      if (retryTimer) clearTimeout(retryTimer);
      wsRef.current?.close();
    };
  }, []);

  const subscribe = useCallback((workspaceId: string) => {
    subscribedWorkspaceRef.current = workspaceId;
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({ action: 'subscribe', workspace_id: workspaceId }));
    }
  }, []);

  const unsubscribe = useCallback(() => {
    subscribedWorkspaceRef.current = null;
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({ action: 'unsubscribe' }));
    }
  }, []);

  return { connectionStatus, lastDiffEvent, subscribe, unsubscribe };
}
```

### Force graph canvas

```tsx
// components/Visualization/DiffGraphCanvasView.tsx
import { useRef, useCallback } from 'react';
import ForceGraph3D, { ForceGraphMethods } from 'react-force-graph-3d';

const CHANGE_TYPE_COLORS = {
  added: '#22c55e',     // green-500
  removed: '#ef4444',   // red-500
  modified: '#f59e0b',  // amber-500
  affected: '#3b82f6',  // blue-500
  unchanged: '#6b7280', // gray-500
} as const;

interface GraphNode {
  id: string;
  name: string;
  nodeType: string;
  changeType: keyof typeof CHANGE_TYPE_COLORS | null;
  filePath?: string;
  lineStart?: number;
  x?: number; // set by the force engine
  y?: number;
  z?: number;
}

interface GraphLink {
  source: string;
  target: string;
  edgeType: string;
}

interface ForceGraphData {
  nodes: GraphNode[];
  links: GraphLink[];
}

interface DiffGraphCanvasViewProps {
  graphData: ForceGraphData;
  onNodeClick?: (node: GraphNode) => void;
  onBackgroundClick?: () => void;
}

export function DiffGraphCanvasView({
  graphData,
  onNodeClick,
  onBackgroundClick,
}: DiffGraphCanvasViewProps) {
  const fgRef = useRef<ForceGraphMethods>();

  const handleNodeClick = useCallback((node: GraphNode) => {
    // Focus on clicked node (bounded: 1000 ms)
    if (fgRef.current) {
      fgRef.current.centerAt(node.x, node.y, 1000);
      fgRef.current.zoom(2, 1000);
    }
    onNodeClick?.(node);
  }, [onNodeClick]);

  const getNodeColor = useCallback((node: GraphNode) => {
    return CHANGE_TYPE_COLORS[node.changeType ?? 'unchanged'];
  }, []);

  const getNodeSize = useCallback((node: GraphNode) => {
    return node.changeType ? 15 : 5; // changed nodes are larger
  }, []);

  return (
    <ForceGraph3D
      ref={fgRef}
      graphData={graphData}
      nodeColor={getNodeColor}
      nodeVal={getNodeSize}
      nodeLabel={(node: GraphNode) => `${node.name} (${node.nodeType})`}
      linkColor={() => '#4b5563'}
      linkWidth={1}
      linkOpacity={0.6}
      onNodeClick={handleNodeClick}
      onBackgroundClick={onBackgroundClick}
      controlType="orbit"
      backgroundColor="#111827" // gray-900
    />
  );
}
```

The ref methods are version-sensitive. Check them against the installed `react-force-graph-3d`; if `centerAt` and `zoom` are not on the 3D component's ref in that version, use its camera-position and fit-to-view methods instead. Wrap the component in a `data-testid="diff-graph-canvas"` container.

### react-three-fiber frame work

```tsx
function RotatingBoxMeshAnimated({ speed }: { speed: number }) {
  const meshRef = useRef<THREE.Mesh>(null);

  useFrame((_state, delta) => {
    if (meshRef.current) meshRef.current.rotation.y += delta * speed; // mutate the ref, no setState
  });

  return (
    <mesh ref={meshRef}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial />
    </mesh>
  );
}

<Canvas>
  <ambientLight intensity={0.5} />
  <pointLight position={[10, 10, 10]} />
  <Suspense fallback={<LoadingPlaceholderMesh />}>
    <RotatingBoxMeshAnimated speed={2} />
  </Suspense>
</Canvas>
```

`useLoader(GLTFLoader, url)` caches and suspends; render a clone (`<primitive object={gltf.scene.clone()} />`) inside `<Suspense>`.

### Complete disposal in effect cleanup

```typescript
const TEXTURE_KEYS = [
  'map', 'lightMap', 'bumpMap', 'normalMap', 'specularMap', 'envMap', 'alphaMap',
  'aoMap', 'displacementMap', 'emissiveMap', 'metalnessMap', 'roughnessMap', 'gradientMap',
] as const;

function disposeSingleMaterialComplete(material: THREE.Material): void {
  for (const key of TEXTURE_KEYS) {
    const texture = (material as unknown as Record<string, unknown>)[key];
    if (texture instanceof THREE.Texture) texture.dispose();
  }
  material.dispose();
}

function disposeObject3DRecursive(object: THREE.Object3D): void {
  while (object.children.length > 0) disposeObject3DRecursive(object.children[0]); // bottom-up
  if (object instanceof THREE.Mesh || object instanceof THREE.Line || object instanceof THREE.Points) {
    object.geometry?.dispose();
    const material = object.material as THREE.Material | THREE.Material[];
    (Array.isArray(material) ? material : [material]).forEach(disposeSingleMaterialComplete);
  }
  object.removeFromParent();
  object.userData = {};
}

useEffect(() => {
  return () => {
    while (scene.children.length > 0) disposeObject3DRecursive(scene.children[0]);
    scene.environment?.dispose();
    if (scene.background instanceof THREE.Texture) scene.background.dispose();
    renderer.dispose();
    renderer.forceContextLoss();
    renderer.domElement.parentElement?.removeChild(renderer.domElement);
  };
}, []);
```

### End-to-end spec for a canvas view

```typescript
// e2e/workspace.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Workspace Management', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:7777');
  });

  test('should display workspace list', async ({ page }) => {
    await expect(page.getByTestId('workspace-list-sidebar')).toBeVisible();
  });

  test('should toggle watch mode', async ({ page }) => {
    await page.getByTestId('watch-toggle-ws_test').click();
    await expect(page.getByTestId('connection-status-indicator')).toHaveText('Connected');
  });

  test('should show 3D visualization', async ({ page }) => {
    await expect(page.getByTestId('diff-graph-canvas')).toBeVisible();
    await expect(page.locator('canvas')).toBeVisible();
  });

  test('should show entity details on click', async ({ page }) => {
    // Needs a mocked API response or fixed test data; coordinates are brittle
    await page.getByTestId('diff-graph-canvas').click({ position: { x: 400, y: 300 } });
    await expect(page.getByTestId('entity-detail-panel')).toBeVisible();
  });
});
```

### Ownership map row

Keep one row per feature beside the source, created at design time and updated in the same change as any boundary change.

```text
feature/component | lane (server/app/scene) | client or server | state union | query hooks / data source | normalisation site | store or scene ref | re-render triggers | per-frame work (none / bounded / measured ms) | test layers
checkout          | server + app            | client leaf      | CheckoutScreenState (4 states) | useCartQuery, useSubmitOrderMutation (rollback) | services/adapters.ts | - | cart query, form | none | RTL + MSW + E2E
```

A row with only component names and owner initials is useless. A stale map is worse than none. A single-canvas toy may skip it.

### Evidence packet

```text
decision: <journey/state/outcome and bounded claim>
sources:  <identities, versions, exclusions, conflicts>
change:   <exact paths, components/consumers, revision>
matrix:   <states/content/containers/browsers/inputs/assets>
proof:    <commands, checks, renders/traces, reviewer questions, result classes>
failures: <observations, attempts, containment/recovery, unresolved risk>
owners:   <decision/review/recovery owners and invalidation/expiry>
next:     <one concrete action or completed boundary>
```

Each render cited under `proof` gets one record, so a reviewer can tell what it shows and when it goes stale:

```text
render:       <stable id; target revision, state, check, attempt>
route/state:  <exact URL or entry; data, auth and async state; representative and extreme content; selected element>
environment:  <container/viewport, DPR, browser/device, theme, locale, preferences, network, graphics>
artifact:     <authorised locator of screenshot/video/trace/DOM/accessibility tree/log; size and hash; retention and privacy>
geometry:     <text fit, overlap, clipping, spacing, stable dimensions, image/canvas visibility, first viewport>
interaction:  <focus, input, animation, state change, console/page/network errors, recovery>
review:       <direction fit, hierarchy, coherence, subject signal, density, alternatives, dissent, owner decision>
stale when:   <component, token, content, fixture, asset, browser or capture-harness change>
```

Also record in the packet: which checks, states, users, browsers and assistive paths are outside the claim; expected and actual kept separate for every mismatch; each verification outcome as pass, fail, contradiction, not applicable (with reason) or not run (with blocker); who owns the residual risk. Byte-identical guidance files count as one source, not as independent support. Store evidence and assets under the project's privacy, security, licensing and retention policy.

## Output contract

For substantial work, return these sections in this order. Do not lead with code.

1. `Rendering Architecture`: client boundary, layers, where the canvas boundary sits (omit the scene parts for non-3D work).
2. `State Ownership`: each piece of state, its lane and container; the screen unions.
3. `Performance Risks`: priced per lane, with what was and was not measured.
4. `Implementation Plan`
5. `Code Changes`: changed paths.

Then add, for any work with a visual or behavioural claim:

6. `Experience decision and visual direction`: user, task, mode, direction, non-goals.
7. `Verification and limits`: commands run, states and viewports rendered, console and network result, the evidence state of each claim, known gaps.
8. `Recovery, invalidation, next action`: rollback path, what change would reopen the evidence, one next executable step.

Expectations on the result: one explicit UI state union instead of scattered booleans and nullable fields; server-state and client-state responsibilities separate; optimistic UI is a transaction with a rollback story; the component tree is simpler to reason about than before.

## Quality gates

Discover the project's own scripts first (`package.json`, CI config). Use them in preference to the generic forms below, and note which gate starts a process or writes files.

```bash
# Static
npx tsc --noEmit
npx eslint .

# Unit, component and network-boundary integration (use the repository's runner)
npx vitest run            # or: npx jest

# End-to-end journeys
npx playwright test
npx playwright test --headed e2e/visualization.spec.ts   # watch the canvas once

# Review greps (each hit needs a reason or a fix)
rg -n "waitForTimeout" e2e src
rg -n "key=\{(index|idx|i)\}" src
rg -n "use[A-Za-z]+Store\(\)" src                 # whole-store subscription
rg -n "useState\((?:new )?THREE\.|useState<THREE\." src   # scene objects in React state
rg -n "new THREE\.(Vector3|Quaternion|Matrix4)" src       # check none sit inside a frame callback
rg -n "addEventListener|setInterval|new WebSocket|new ResizeObserver" src   # each needs a cleanup
rg -n "from ['\"]three['\"]" src/stores src/services       # lane purity: expect no hits
rg -n "fetch\(" src/components                             # canvas and presenters do not fetch

# Dependency and blast-radius check with Parseltongue, when the repository uses it
parseltongue pt01 --path ./src --output rocksdb:react-base.db
# make component changes
parseltongue pt01 --path ./src --output rocksdb:react-live.db
parseltongue diff --base rocksdb:react-base.db --live rocksdb:react-live.db
```

Rendered gate, by hand or scripted: open the real route at each named viewport (at least one narrow and one wide), in each material state (loading, empty, error, populated, long content), with the console and network panel open. For a canvas: meaningful non-blank pixels, the subject framed, input and animation working, resize handled, cleanup on unmount, fallback shown when WebGL is off. Operate the primary journey with the keyboard only. Turn on reduced motion once.

Release bar per feature: zero unhandled union states; zero optimistic writes without a registered rollback; zero "state update on an unmounted component" style warnings; a journey test for every core flow; one keyboard-only path exercised. Run the full pyramid on core journeys and behaviour tests on changed components. Rerun a failed check only after something changed, and keep the first failure in the report.

## Anti-patterns

React:

1. Whole-store subscriptions in many components.
2. Form rules duplicated in JSX and API code.
3. Fetching directly inside many unrelated components.
4. UI states encoded as nullable property soup or independent booleans.
5. Optimistic writes with no rollback strategy.
6. Raw transport payloads passed deep into components.
7. Arbitrary `waitForTimeout` thinking in UI tests.
8. Prop-to-state syncing with an effect; stored derived state; eager `useState(createExpensiveArray())`.
9. Effects with object dependencies that loop; timers, listeners or fetches without cleanup.
10. Index keys; inline object props into memoised children; components defined inside render; memoising everything.
11. One massive context, or context used for component state.

Scene:

1. One giant `GraphCanvas.tsx` holding fetching, transforms, controls, camera logic and side panels.
2. Global store writes on every hover or animation frame.
3. Raw API payloads flowing directly into mesh creation.
4. Scene objects recreated on every React render.
5. Undisposed geometry, materials and textures; orphan listeners.
6. Per-frame allocation, uncached metrics, unbounded work; thousands of individual meshes instead of instancing.
7. Overwriting `matrixWorld` by hand; several renderers on one canvas; an uncapped reconnect loop.

Design (each has a registry id, signal, containment and release evidence in `reference.md`, "Anti Pattern Registry Table"):

1. A visual direction chosen before reading the user, product and current system: it could fit any company after swapping logo and copy. Stop, write the task and product statement, inspect the existing system.
2. A marketing hero or card grid delivered for a requested tool. Released only when a user-flow fixture completes the primary task without a marketing detour.
3. A happy-path static mockup: only the populated state is designed; loading, empty, partial, error, permission, disabled or recovery states are missing. Define the state graph before polish.
4. A client failure with no recovery: an auth, network, hydration, asset or mutation error ends in a dead screen. Preserve context, explain the state, offer retry, back or correction.
5. Cards inside cards, verbose pill controls for familiar commands, feature explanations inside the product UI.
6. One-note palette, decorative orbs, a hero that hides or splits the subject, atmospheric media that hides the subject, an asset failure with no layout fallback.
7. Motion with no causal role; shrink-only responsive layout, fixed-copy assumptions, viewport-scaled type, controls that change size.
8. Icon without an accessible name; state by colour only; visual order that differs from DOM order.
9. Acceptance from source, from one viewport, or from a screenshot alone; a baseline screenshot treated as the design authority; a blank or unframed 3D scene.
10. Guidance, preference, inference and target fact stated in one authoritative voice; two byte-identical guidance files counted as independent support.
11. A new design system without migration; hiding overflow or shortening copy to make a layout pass.

## Bundled scripts

None. This skill ships no scripts or assets. `reference.md` in this directory adds depth: the full pattern catalogue with code for contexts, virtualisation, refs, page objects, scene architecture, pooling, texture and model loading, render loop, instancing, camera, animation and shaders; the anti-pattern registry; worked examples; failure modes; measurement method. Read its scoreboard first, then the subsection that matches the work, then the anti-pattern registry.

The wider method this skill sits in: [LLM principles](../../../A00-LLM-Principles01.md), [workflow](../../../A01-LLM-Workflow01.md), [executable specifications](../../../A03-Executable-Specs01.md).

## Self-check before handing back

- Is the client boundary decision written down, with a reason for every client component?
- Is every piece of state in exactly one lane, and is no scene object or per-frame value in React state or a global store?
- Does each screen have one union, and does every branch render something with a test id?
- Does transport data pass through a parser or adapter before any hook or component uses it?
- Does every optimistic write have a rollback, and every effect a cleanup?
- Does every recoverable error offer a next action?
- For a scene: do reconnects resubscribe, is selection kept by id across refresh, is everything disposed on unmount, is there a no-WebGL fallback?
- Was the page rendered at a narrow and a wide viewport, in loading, empty, error and long-content states, with a clean console and a keyboard-only pass?
- Does the look follow one stated direction that fits the product mode, using the existing system where one exists?
- Does the report separate what was verified from what was inferred, and name what would invalidate it?
- Is every number in the report either measured under a stated workload or labelled as a target or as not measured?
