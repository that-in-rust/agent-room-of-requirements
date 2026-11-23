# Skills Library

One stand-alone `SKILL.md` per subject (with an optional companion `reference.md` for deeper tradeoffs, failure modes, and refresh queries). Every skill is self-contained so an agent or workshop participant can load the single right file for a task.

## Core Engineering & Workflow Skills (18)

| Subject | Skill | Reference | Covers |
|---|---|---|---|
| **Executable Specs** | [SKILL.md](skills/executable-specs/SKILL.md) | [reference.md](skills/executable-specs/reference.md) | WHEN/THEN/SHALL contracts, outside-in test mapping, traceability, completion gates |
| **TDD, Progress & Resume** | [SKILL.md](skills/tdd-progress-and-resume/SKILL.md) | [reference.md](skills/tdd-progress-and-resume/reference.md) | Red-green-refactor cycles, durable progress journals, context checkpoints, handoff resume |
| **Codebase Navigation** | [SKILL.md](skills/codebase-navigation/SKILL.md) | [reference.md](skills/codebase-navigation/reference.md) | Parseltongue, dependency maps, GitHub repo context capture, Clarity, Strata |
| **Explore & Decide** | [SKILL.md](skills/explore-and-decide/SKILL.md) | [reference.md](skills/explore-and-decide/reference.md) | Deep exploration, structured multi-perspective debate, timeline traversal, architecture tradeoffs |
| **Review, Verify & Debug** | [SKILL.md](skills/review-verify-debug/SKILL.md) | [reference.md](skills/review-verify-debug/reference.md) | Code review, systematic root-cause debugging, evidence-based verification before completion |
| **Git Delivery Flow** | [SKILL.md](skills/git-delivery-flow/SKILL.md) | [reference.md](skills/git-delivery-flow/reference.md) | Branching, commits, worktrees, pull requests, stacked diffs, safe release hygiene |
| **Structured Writing** | [SKILL.md](skills/structured-writing/SKILL.md) | [reference.md](skills/structured-writing/reference.md) | Minto Pyramid, executive briefs, technical narratives, concise documentation |
| **Visual Explainers** | [SKILL.md](skills/visual-explainers/SKILL.md) | [reference.md](skills/visual-explainers/reference.md) | Self-contained HTML explainers, ASCII diagrams, visual storytelling, layout verification |
| **Generative Art & Images** | [SKILL.md](skills/generative-art-and-images/SKILL.md) | [reference.md](skills/generative-art-and-images/reference.md) | Seeded algorithmic art (p5.js/canvas), image-generation prompt specs, local Ollama vision |
| **Kotlin Backend** | [SKILL.md](skills/kotlin-backend/SKILL.md) | [reference.md](skills/kotlin-backend/reference.md) | Idiomatic Kotlin, Ktor, coroutines, Arrow, persistence, testing, and production hardening |
| **Python** | [SKILL.md](skills/python/SKILL.md) | [reference.md](skills/python/reference.md) | Idiomatic Python, typing, async, packaging, testing, CLI and service patterns |
| **TypeScript Backend** | [SKILL.md](skills/typescript-backend/SKILL.md) | [reference.md](skills/typescript-backend/reference.md) | Node/TypeScript services, strict typing, schema validation, database/API contracts, testing |
| **React Frontend** | [SKILL.md](skills/react-frontend/SKILL.md) | [reference.md](skills/react-frontend/reference.md) | React architecture, state boundaries, accessibility, Playwright page-object testing |
| **System Design & Polyglot** | [SKILL.md](skills/system-design-and-polyglot/SKILL.md) | [reference.md](skills/system-design-and-polyglot/reference.md) | Distributed systems, polyglot idioms (TS, Go, Java, Kafka, K8s, Terraform), .NET and Angular |
| **Stripe Payments** | [SKILL.md](skills/stripe-payments/SKILL.md) | [reference.md](skills/stripe-payments/reference.md) | Server-owned payment state machines, Stripe surface selection, idempotency, webhooks, reconciliation |
| **Authoring Skills & References** | [SKILL.md](skills/authoring-skills-and-references/SKILL.md) | [reference.md](skills/authoring-skills-and-references/reference.md) | Designing, testing, evolving, and validating agent skills and idiomatic references |
| **Claude Plugin Development** | [SKILL.md](skills/claude-plugin-development/SKILL.md) | [reference.md](skills/claude-plugin-development/reference.md) | Claude Code plugins, slash commands, hooks, MCP integration, settings, agents, setup, and Codex plugins |
| **Agent Context & Orchestration** | [SKILL.md](skills/agent-context-and-orchestration/SKILL.md) | [reference.md](skills/agent-context-and-orchestration/reference.md) | `AGENTS.md` design, context budgets, subagent orchestration, prompt patterns, and parallel workflows |

## Stand-Alone Rust Skills (9)

Each Rust skill embeds the shared core from [Rust-skills/skills/_core.md](../Rust-skills/skills/_core.md) (kept in sync by `Rust-skills/skills/sync-core.sh`) so it works independently when loaded alone.

| Subject | Skill | Covers |
|---|---|---|
| **Rust Application Service** | [SKILL.md](../Rust-skills/skills/rust-app-service/SKILL.md) | HTTP services, Axum/Actix, SQLx/Diesel, Tower, Tokio, auth, idempotency, health checks |
| **Rust CLI** | [SKILL.md](../Rust-skills/skills/rust-cli/SKILL.md) | `clap`, exit codes, stdin/stdout/stderr, config/env, filesystem traversal, child processes |
| **Rust Infra: Parsers** | [SKILL.md](../Rust-skills/skills/rust-infra-parsers/SKILL.md) | Tree-sitter, `syn`, `nom`/`winnow`, compilers, spans, diagnostics, rewrites |
| **Rust Infra: Performance** | [SKILL.md](../Rust-skills/skills/rust-infra-performance/SKILL.md) | Hot loops, allocation/layout, benchmarks, caches, `rayon`, atomics, arenas, `no_std` |
| **Rust Infra: Storage** | [SKILL.md](../Rust-skills/skills/rust-infra-storage/SKILL.md) | On-disk formats, WALs, snapshots, atomic writes, wire protocols, streaming decoders, queues |
| **Rust Library** | [SKILL.md](../Rust-skills/skills/rust-library/SKILL.md) | Public API design, traits, generics, `thiserror`, builders, feature flags, semver, MSRV |
| **Rust Review** | [SKILL.md](../Rust-skills/skills/rust-review/SKILL.md) | Pre-merge/pre-release review checklists, anti-patterns, gate audits, severity levels |
| **Rust Tauri** | [SKILL.md](../Rust-skills/skills/rust-tauri/SKILL.md) | Tauri 2 desktop apps, IPC commands, capabilities, managed state, plugins, packaging |
| **Rust Unsafe & FFI** | [SKILL.md](../Rust-skills/skills/rust-unsafe-ffi/SKILL.md) | `unsafe` invariants, raw pointers, `MaybeUninit`, `repr(C)`, C/Python/Node FFI, `Pin` |

## Curated Third-Party Skills (MIT)

Verbatim MIT-licensed upstream skills live under `third-party/`, with licences and upstream links for non-MIT references recorded in [third-party/ATTRIBUTION.md](third-party/ATTRIBUTION.md):

- **Superpowers** (`third-party/superpowers/`, MIT): 14 skills including brainstorming, TDD, systematic debugging, verification before completion, writing plans, writing skills, and git worktrees.
- **Stripe Best Practices** (`third-party/stripe/stripe-best-practices/SKILL.md`, MIT): official Stripe integration best practices.
