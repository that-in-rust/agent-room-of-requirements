---
name: typescript-coder-01
description: Reliability-first TypeScript skill for implementing, refactoring, or reviewing .ts code in shared libraries, services, browser code, and cross-layer contracts. Use when work needs strict tsconfig guardrails, schema-first parsing, unknown-at-boundary handling, discriminated unions, persistence/version safety, explicit async cancellation, or behavior-first testing.
---

# TypeScript Reliability

## Overview

Use this skill when the task is primarily about writing, refactoring, or reviewing reliable TypeScript across shared libraries, services, browser code, schemas, and protocol boundaries. It biases toward the patterns that prevent silent widening, runtime trust bugs, persistence drift, and async edge-case failures.

## When To Use

- `.ts`, `.mts`, `.cts`, or `tsconfig.json` work where correctness matters more than style
- Shared domain models, schema codecs, serialization, persistence, stream/event handling, or protocol types
- Refactors that need stronger type/value boundaries or less hidden runtime trust
- Code reviews where the real question is whether the TypeScript will stay correct under change

## Workflow

1. Classify the task. Stay in this skill for shared TypeScript baselines; bring in `typescript-backend-coder-01` for API or worker concerns and `typescript-react-coder-01` for React or TSX concerns.
2. Skim [references/reference-map.md](references/reference-map.md), then open only the relevant sections in [references/typescript-reliability-reference.md](references/typescript-reliability-reference.md).
3. Default to the highest-scoring patterns first: strict compiler railguards, `import type` hygiene, `unknown` at trust boundaries, schema-first parsing, discriminated unions, and explicit result types for expected failures.
4. Implement or review with the skeptical question: what happens when the input is malformed, old, partial, cancelled, or missing?
5. Validate with `tsc`, focused tests, and any boundary tests. Re-check the anti-patterns before finishing.

## Reference Use

- Use [references/reference-map.md](references/reference-map.md) first for quick routing.
- Use [references/typescript-reliability-reference.md](references/typescript-reliability-reference.md) for the full scored patterns, SOP, anti-patterns, and pre-commit ritual.
- For large-file navigation, prefer heading search such as `rg '^##|^###' references/typescript-reliability-reference.md`.

## Output Expectations

- Prefer explicitness over cleverness.
- Keep type/value boundaries obvious in both code and imports.
- Avoid unchecked casts; if one is unavoidable, fence it tightly and explain why.
- Leave the code with better boundary hygiene, not just passing types.
