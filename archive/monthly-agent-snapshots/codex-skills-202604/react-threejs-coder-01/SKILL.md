---
name: react-threejs-coder-01
description: Build, refactor, and review React plus TypeScript plus Three.js frontends, especially interactive 3D visualization UIs using react-force-graph, Zustand, TanStack Query, Vite, and performance-sensitive scene logic. Use when the task involves 3D canvases, graph exploration, camera controls, scene state, or realtime visual interaction in React.
---

# React Threejs Coder 01

## Overview

Use this skill for React-based 3D frontends where the hard part is keeping declarative UI, scene mutation, async data, and performance in the right lanes.

## Workflow

1. Split the problem into lanes.
- `server state`: fetched data, subscriptions, and cache invalidation
- `app state`: selection, filters, layout mode, panel visibility
- `scene state`: mutable objects, camera state, transient hover, animation data

2. Pick the ownership boundary.
- Keep React responsible for structure and orchestration.
- Keep per-frame math and mutable scene objects outside broad React rerender paths.

3. Shape the data model before visuals.
- Define typed nodes, edges, selections, and derived view models.
- Normalize incoming data so rendering code does not parse raw transport shapes.

4. Keep the scene composable.
- Separate data hooks, stores, scene components, overlays, and controls.
- Default to feature-level modules rather than dumping everything into one canvas component.

5. Verify user experience and render cost.
- Check loading, empty, degraded, and disconnected states.
- Check camera reset, selection persistence, and event cleanup.
- Verify the scene remains usable when data volume grows.

## Default Rules

- Use TanStack Query for remote data and cache lifecycle.
- Use Zustand for durable app state, not for every transient pointer movement.
- Do not put large mutable Three.js objects directly in React state.
- Keep render-loop work in scene hooks or frame handlers, not in parent component rerenders.
- Treat camera, controls, and picking as first-class interaction systems.
- Prefer typed adapters between transport data and scene data.
- Add a graceful fallback for no-WebGL or low-power cases when the view is core to the product.

## Reference Use

- Read [React Three.js patterns](references/react-threejs-patterns.md) first for structure and ownership rules.
- Read [Force graph and scene checklist](references/force-graph-scene-checklist.md) when the task involves graph exploration, node rendering, camera behavior, or large-scene performance.

## Output Contract

Return results in this order when the task is substantial:

1. `Rendering Architecture`
2. `State Ownership`
3. `Performance Risks`
4. `Implementation Plan`
5. `Code Changes`

## Guardrails

- Do not use React state as a generic container for mutable scene objects.
- Do not let hover or animation churn rerender the full app shell.
- Do not hide expensive scene transforms inside JSX without measuring the cost.
- If the request is mostly about product look-and-feel rather than 3D systems, pair with `frontend-design`.
