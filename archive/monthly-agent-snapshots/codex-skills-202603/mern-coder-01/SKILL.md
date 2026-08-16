---
name: mern-coder-01
description: Reliability-first MERN + TypeScript coding guide for Express, React, Mongoose, and MongoDB. Use when Codex needs to implement, refactor, review, or harden classic MERN applications with validated request boundaries, safe Mongoose query and write patterns, auth and security defaults, pagination or indexing decisions, and production-ready frontend or API reliability.
---

# MERN Coder 01

## Overview

Apply a reliability-first baseline for classic React + Express + Mongoose + MongoDB work.
Keep this skill lightweight: load only the relevant sections from `references/doctrine.md` instead of reading the whole doctrine file by default.

## Workflow

1. Classify the task before coding.
   Common buckets: request boundary, frontend state, Express/API flow, Mongoose query/write logic, MongoDB modeling, auth/security, observability.
2. Map the doctrine quickly with:
   `rg -n "^## |^### " references/doctrine.md`
3. Read only the relevant doctrine section.
4. Apply the default rules below while preserving repo conventions.
5. Verify with the repo's normal build, typecheck, and test commands.
6. If the task requires deviating from the doctrine, say why and preserve the same reliability property another way.

## Default Rules

- Validate `req.body`, `req.params`, and `req.query` at the server edge.
- Treat client validation as UX help, not a trust boundary.
- Keep shared DTOs, validation schemas, and API contracts in a shared layer when the repo has both client and server code.
- Use TanStack Query for server state and keep client-only UI state separate.
- Centralize Express async error handling.
- Prefer `load -> mutate -> save()` for document behavior.
- If query-style updates are required, make validation intent explicit with `runValidators: true`.
- Use `lean()` for read-only serialization paths.
- Populate only the fields the response actually needs.
- Use deterministic sorts and range or cursor pagination for growing collections.
- Rate-limit auth routes and use memory-hard password hashing.
- Add request correlation ids and graceful shutdown behavior to production services.
- Keep entity types, DTOs, and API response wrappers distinct instead of reusing one shape everywhere.

## Reference Map

Read these sections from `references/doctrine.md` based on the task:

- `Section 1: Contract Boundaries`
  Use for request validation, form contracts, collocated query layers, and MSW-backed transport testing.
- `Section 2: Frontend Reliability`
  Use for TanStack Query, behavior-first testing, route error recovery, and persisted client state.
- `Section 3: Express and API Reliability`
  Use for centralized error middleware, security headers, readiness and shutdown, and request correlation.
- `Section 4: Mongoose Query and Write Reliability`
  Use for `save()` vs update methods, `lean()`, update validators, optimistic concurrency, transactions, and selective populate.
- `Section 5: MongoDB Modeling Reliability`
  Use for embed vs reference decisions, index design, range pagination, and collection schema validation.
- `Section 6: Auth and Cross-Cutting Reliability`
  Use for password hashing, idempotency, auth throttling, and retry strategy.
- `Operational MERN Defaults for LLMs`
  Use as the shortest end-to-end playbook for shaping new endpoints safely.
- `Practical MERN Baseline`
  Use when the repo has a shared types layer or the task touches DTO boundaries and response-envelope consistency.
- `Patterns Intentionally Excluded` and `Anti-Patterns to Avoid`
  Read before adopting convenience patterns that look attractive but weaken reliability.

## Boundary Notes

- Treat this skill as partial guidance for Next.js App Router, GraphQL-first, WebSocket-heavy, or sharded MongoDB systems.
- If the repo already has stronger local conventions, follow them unless they reduce the reliability guarantees this skill is protecting.
