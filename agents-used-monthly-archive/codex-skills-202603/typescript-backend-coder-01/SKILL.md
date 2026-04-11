---
name: typescript-backend-coder-01
description: Reliability-first backend TypeScript skill for APIs, workers, queues, CLIs, and long-running services. Use when writing Node, Bun, Deno, or worker code that needs request and env parsing, branded identifiers, explicit result errors, cancellation propagation, idempotent writes, persistence evolution, or contract and integration tests.
---

# TypeScript Backend Reliability

## Overview

Use this skill for server-side TypeScript where IO lies can corrupt business logic. It concentrates on safe request parsing, domain-safe IDs, adapter boundaries, cancellation, retry safety, and persistence evolution.

## When To Use

- HTTP handlers, RPC endpoints, webhooks, queues, cron jobs, workers, or CLIs
- `.ts` backend modules in Node.js, Bun, Deno, serverless, or edge runtimes
- Config and environment bootstrapping, transport adapters, provider clients, repositories, or service layers
- Reviews where the main risks are bad inputs, retries, timeouts, or storage drift

## Workflow

1. Assume all inbound data is untrusted. Parse requests, events, queue payloads, and env at the boundary.
2. Read [references/reference-map.md](references/reference-map.md), then the relevant sections in [references/backend-reliability-reference.md](references/backend-reliability-reference.md). Pull in `typescript-coder-01` as the shared baseline when needed.
3. Apply the default backend patterns in order: schema-first parsing, branded IDs, explicit result error algebra, deadline propagation, transport normalization, ports-and-adapters, and idempotent mutation boundaries.
4. Keep the service core framework-light. Push HTTP, queue, database, and provider quirks to adapters.
5. Validate with contract or integration tests for the real boundary, not only unit tests inside the core.

## Reference Use

- Use [references/reference-map.md](references/reference-map.md) first for fast routing.
- Use [references/backend-reliability-reference.md](references/backend-reliability-reference.md) for the full scored backend patterns and anti-patterns.
- For large-file navigation, prefer heading search such as `rg '^##|^###' references/backend-reliability-reference.md`.

## Output Expectations

- Expected business failures stay visible in signatures.
- Writes should be retry-safe when the environment can retry them.
- Deadline and cancellation handling should flow through the whole call chain.
- The final design should make the risky boundary obvious from a quick skim.
