# Find a skill by task

Start with one skill. Open its companion reference for examples or tradeoffs, not as a prerequisite. New here? [Try the workshop walkthrough](../S03-how-to-use-skills/README.md).

## Understand the code and choose a change

| Task | Skill | Reference | Covers |
|---|---|---|---|
| **Codebase Navigation** | [SKILL.md](codebase-navigation/SKILL.md) | [reference.md](codebase-navigation/reference.md) | Parseltongue, dependency maps, GitHub repo context capture, Clarity, Strata |
| **Explore & Decide** | [SKILL.md](explore-and-decide/SKILL.md) | [reference.md](explore-and-decide/reference.md) | Deep exploration, structured multi-perspective debate, timeline traversal, architecture tradeoffs |
| **System Design & Polyglot** | [SKILL.md](system-design-and-polyglot/SKILL.md) | [reference.md](system-design-and-polyglot/reference.md) | Distributed systems, polyglot idioms (TS, Go, Java, Kafka, K8s, Terraform), .NET and Angular |

## Specify, test, review and ship

| Task | Skill | Reference | Covers |
|---|---|---|---|
| **Executable Specs** | [SKILL.md](executable-specs/SKILL.md) | [reference.md](executable-specs/reference.md) | WHEN/THEN/SHALL contracts, outside-in test mapping, traceability, completion gates |
| **TDD, Progress & Resume** | [SKILL.md](tdd-progress-and-resume/SKILL.md) | [reference.md](tdd-progress-and-resume/reference.md) | Red-green-refactor cycles, durable progress journals, context checkpoints, handoff resume |
| **Review, Verify & Debug** | [SKILL.md](review-verify-debug/SKILL.md) | [reference.md](review-verify-debug/reference.md) | Code review, systematic root-cause debugging, evidence-based verification before completion |
| **Git Delivery Flow** | [SKILL.md](git-delivery-flow/SKILL.md) | [reference.md](git-delivery-flow/reference.md) | Branching, commits, worktrees, pull requests, stacked diffs, safe release hygiene |

## Implement a product change

| Task | Skill | Reference | Covers |
|---|---|---|---|
| **Kotlin Backend** | [SKILL.md](kotlin-backend/SKILL.md) | [reference.md](kotlin-backend/reference.md) | Idiomatic Kotlin, Ktor, coroutines, Arrow, persistence, testing, and production hardening |
| **Python** | [SKILL.md](python/SKILL.md) | [reference.md](python/reference.md) | Idiomatic Python, typing, async, packaging, testing, CLI and service patterns |
| **TypeScript Backend** | [SKILL.md](typescript-backend/SKILL.md) | [reference.md](typescript-backend/reference.md) | Node/TypeScript services, strict typing, schema validation, database/API contracts, testing |
| **React Frontend** | [SKILL.md](react-frontend/SKILL.md) | [reference.md](react-frontend/reference.md) | React architecture, state boundaries, accessibility, Playwright page-object testing |
| **Stripe Payments** | [SKILL.md](stripe-payments/SKILL.md) | [reference.md](stripe-payments/reference.md) | Server-owned payment state machines, Stripe surface selection, idempotency, webhooks, reconciliation |

## Teach a method or equip an agent

| Task | Skill | Reference | Covers |
|---|---|---|---|
| **Structured Writing** | [SKILL.md](structured-writing/SKILL.md) | [reference.md](structured-writing/reference.md) | Minto Pyramid, executive briefs, technical narratives, concise documentation |
| **Visual Explainers** | [SKILL.md](visual-explainers/SKILL.md) | [reference.md](visual-explainers/reference.md) | Self-contained HTML explainers, ASCII diagrams, visual storytelling, layout verification |
| **Generative Art & Images** | [SKILL.md](generative-art-and-images/SKILL.md) | [reference.md](generative-art-and-images/reference.md) | Seeded algorithmic art (p5.js/canvas), image-generation prompt specs, local Ollama vision |
| **Authoring Skills & References** | [SKILL.md](authoring-skills-and-references/SKILL.md) | [reference.md](authoring-skills-and-references/reference.md) | Designing, testing, evolving, and validating agent skills and idiomatic references |
| **Agent Context & Orchestration** | [SKILL.md](agent-context-and-orchestration/SKILL.md) | [reference.md](agent-context-and-orchestration/reference.md) | `AGENTS.md` design, context budgets, subagent orchestration, prompt patterns, and parallel workflows |
| **Claude Plugin Development** | [SKILL.md](claude-plugin-development/SKILL.md) | [reference.md](claude-plugin-development/reference.md) | Claude Code plugins, slash commands, hooks, MCP integration, settings, agents, setup, and Codex plugins |

## Build or review Rust

Pick the skill for the component you are changing, then use **Rust Review** for a fresh review pass. Each Rust guide embeds the [core](_core.md); the eight writer guides also embed the [essentials](_essentials.md). Edit the sources, not the copies, and run `S01-skills-for-engineering-teams/sync-core.sh` from the repository root.

| Subject | Skill | Covers |
|---|---|---|
| **Rust Application Service** | [SKILL.md](rust-app-service/SKILL.md) | HTTP services, Axum/Actix, SQLx/Diesel, Tower, Tokio, auth, idempotency, health checks |
| **Rust CLI** | [SKILL.md](rust-cli/SKILL.md) | `clap`, exit codes, stdin/stdout/stderr, config/env, filesystem traversal, child processes |
| **Rust Infra: Parsers** | [SKILL.md](rust-infra-parsers/SKILL.md) | Tree-sitter, `syn`, `nom`/`winnow`, compilers, spans, diagnostics, rewrites |
| **Rust Infra: Performance** | [SKILL.md](rust-infra-performance/SKILL.md) | Hot loops, allocation/layout, benchmarks, caches, `rayon`, atomics, arenas, `no_std` |
| **Rust Infra: Storage** | [SKILL.md](rust-infra-storage/SKILL.md) | On-disk formats, WALs, snapshots, atomic writes, wire protocols, streaming decoders, queues |
| **Rust Library** | [SKILL.md](rust-library/SKILL.md) | Public API design, traits, generics, `thiserror`, builders, feature flags, semver, MSRV |
| **Rust Review** | [SKILL.md](rust-review/SKILL.md) | Pre-merge/pre-release review checklists, anti-patterns, gate audits, severity levels |
| **Rust Tauri** | [SKILL.md](rust-tauri/SKILL.md) | Tauri 2 desktop apps, IPC commands, capabilities, managed state, plugins, packaging |
| **Rust Unsafe & FFI** | [SKILL.md](rust-unsafe-ffi/SKILL.md) | `unsafe` invariants, raw pointers, `MaybeUninit`, `repr(C)`, C/Python/Node FFI, `Pin` |

Looking for the verbatim Superpowers or Stripe guides? See [upstream snapshots and licences](../S02-curated-upstream-skill-snapshots/ATTRIBUTION.md).
