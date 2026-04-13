# React Three.js Patterns

## Core Separation

Use this ownership split:

- `React`: layout, composition, panels, controls, suspense boundaries
- `Query layer`: remote data fetch and cache lifecycle
- `Store layer`: user-visible app state worth preserving across components
- `Scene layer`: mutable meshes, materials, camera interpolation, transient hover

## Recommended Shape

```text
src/
  components/
    layout/
    scene/
    panels/
  hooks/
    useSceneData.ts
    useGraphSelection.ts
    useCameraBehavior.ts
  stores/
    appViewStore.ts
    graphSelectionStore.ts
  services/
    api.ts
    adapters.ts
  types/
    graph.ts
```

## Good Defaults

- Keep transport parsing in `services/adapters.ts`
- Keep typed scene entities in `types/graph.ts`
- Keep scene-specific hooks small and focused
- Keep overlays and inspector panels outside the render loop

## Anti-Patterns

- One giant `GraphCanvas.tsx` containing fetching, transforms, controls, camera logic, and side panels
- Global store writes on every hover or animation frame
- Raw API payloads flowing directly into mesh creation
- Scene objects recreated on every React render
