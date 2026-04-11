---
name: typescript-react-coder-01
description: Reliability-first React and TypeScript skill for .tsx apps, client and server boundaries, forms, query layers, optimistic UI, navigation recovery, and behavior-first frontend tests. Use when working on React components, hooks, App Router style boundaries, server-state flows, schema-driven forms, or resilient UI state machines.
---

# TypeScript React Reliability

## Overview

Use this skill for React and TSX work where UI correctness depends on typed state transitions, trustworthy server-state boundaries, and resilient recovery paths. It focuses on the frontend failures LLMs often miss: widened props and state, duplicated fetching, brittle optimistic updates, and components that only work under ideal timing.

## When To Use

- `.tsx` components, hooks, route modules, App Router style boundaries, or client/server split decisions
- Forms, query or cache layers, optimistic mutations, external stores, route contracts, or event payloads
- Frontend reviews where the question is whether the UI will survive slow data, bad data, retries, or navigation changes
- React refactors that should reduce client-side blast radius or impossible UI states

## Workflow

1. Decide what truly needs to be client-side. Keep as much code server-capable as the architecture allows.
2. Read [references/reference-map.md](references/reference-map.md), then load only the relevant sections in [references/react-reliability-reference.md](references/react-reliability-reference.md). Pull in `typescript-coder-01` when you need the shared TypeScript baseline.
3. Apply the default frontend patterns in order: schema-validated forms, feature-collocated query layers, exhaustive UI unions, minimal store subscriptions, navigation-aware error recovery, and rollback-ready optimistic updates.
4. Normalize transport data before hooks and components trust it.
5. Validate with behavior-first UI tests that cover the user-visible boundary, not only isolated helpers.

## Reference Use

- Use [references/reference-map.md](references/reference-map.md) first for fast routing.
- Use [references/react-reliability-reference.md](references/react-reliability-reference.md) for the full scored React patterns and anti-patterns.
- For large-file navigation, prefer heading search such as `rg '^##|^###' references/react-reliability-reference.md`.

## Output Expectations

- Prefer one explicit UI state union over scattered booleans and nullable fields.
- Keep server-state and client-state responsibilities separate.
- Treat optimistic UI as a transaction with a rollback story.
- Leave the component tree simpler to reason about than before.
