# Find a skill by task

All repository-owned skills are prefixed with **`tir-`** (*That in Rust*). Start with one skill. Open its companion reference for examples or tradeoffs, not as a prerequisite. New here? [Try the workshop walkthrough](../S03-how-to-use-skills/README.md).

## Understand the code and choose a change

| Task | Skill | Reference | Covers |
|---|---|---|---|
| **TIR Codebase Navigation** | [SKILL.md](tir-codebase-navigation/SKILL.md) | [reference.md](tir-codebase-navigation/reference.md) | Parseltongue, dependency maps, GitHub repo context capture, Clarity, Strata |
| **TIR Explore & Decide** | [SKILL.md](tir-explore-and-decide/SKILL.md) | [reference.md](tir-explore-and-decide/reference.md) | Deep exploration, structured multi-perspective debate, timeline simulation, design approval, roadmap gaps |
| **TIR Plan & Execute** | [SKILL.md](tir-plan-and-execute/SKILL.md) | [reference.md](tir-explore-and-decide/reference.md) | Turning approved designs into ordered implementation plans and executing in verified batches |
| **TIR System Design** | [SKILL.md](tir-system-design/SKILL.md) | [reference.md](tir-system-design/reference.md) | Distributed systems architecture, service boundaries, reliability tradeoffs |
| **TIR Polyglot Idioms** | [SKILL.md](tir-polyglot-idioms/SKILL.md) | [reference.md](tir-system-design/reference.md) | Cross-language idioms (TS, Go, Java, Kafka, K8s, Terraform), ASP.NET Core + Angular, reference extraction |

## Specify, test, review and ship

| Task | Skill | Reference | Covers |
|---|---|---|---|
| **TIR Executable Specs** | [SKILL.md](tir-executable-specs/SKILL.md) | [reference.md](tir-executable-specs/reference.md) | WHEN/THEN/SHALL contracts, outside-in test mapping, traceability, completion gates |
| **TIR TDD, Progress & Resume** | [SKILL.md](tir-tdd-progress-and-resume/SKILL.md) | [reference.md](tir-tdd-progress-and-resume/reference.md) | Red-green-refactor cycles, durable progress journals, context checkpoints, handoff resume |
| **TIR Code Review** | [SKILL.md](tir-code-review/SKILL.md) | [reference.md](tir-code-review/reference.md) | Requesting reviews, reviewing diffs rigorously, handling feedback without blind compliance |
| **TIR Verification Gates** | [SKILL.md](tir-verification-gates/SKILL.md) | [reference.md](tir-code-review/reference.md) | Fresh-command verification before claiming any task, build, or fix is complete |
| **TIR Root-Cause Debugging** | [SKILL.md](tir-root-cause-debugging/SKILL.md) | [reference.md](tir-code-review/reference.md) | Reproducing, isolating, and proving root causes before proposing code edits |
| **TIR Git Delivery Flow** | [SKILL.md](tir-git-delivery-flow/SKILL.md) | [reference.md](tir-git-delivery-flow/reference.md) | Branching, commits, worktrees, pull requests, stacked diffs, safe release hygiene |

## Implement a product change

| Task | Skill | Reference | Covers |
|---|---|---|---|
| **TIR Kotlin Backend** | [SKILL.md](tir-kotlin-backend/SKILL.md) | [reference.md](tir-kotlin-backend/reference.md) | Idiomatic Kotlin, Ktor, coroutines, Arrow, persistence, testing, and production hardening |
| **TIR Python** | [SKILL.md](tir-python/SKILL.md) | [reference.md](tir-python/reference.md) | Idiomatic Python, typing, async, packaging, testing, CLI and service patterns |
| **TIR TypeScript Backend** | [SKILL.md](tir-typescript-backend/SKILL.md) | [reference.md](tir-typescript-backend/reference.md) | Node/TypeScript services, strict typing, schema validation, database/API contracts, testing |
| **TIR React Frontend** | [SKILL.md](tir-react-frontend/SKILL.md) | [reference.md](tir-react-frontend/reference.md) | React architecture, state boundaries, accessibility, Playwright page-object testing |
| **TIR Stripe Payments** | [SKILL.md](tir-stripe-payments/SKILL.md) | [reference.md](tir-stripe-payments/reference.md) | Server-owned payment state machines, Stripe surface selection, idempotency, webhooks, reconciliation |

## Teach a method or equip an agent

| Task | Skill | Reference | Covers |
|---|---|---|---|
| **TIR Structured Writing** | [SKILL.md](tir-structured-writing/SKILL.md) | [reference.md](tir-structured-writing/reference.md) | Minto Pyramid, executive briefs, technical narratives, concise documentation |
| **TIR Visual Explainers** | [SKILL.md](tir-visual-explainers/SKILL.md) | [reference.md](tir-visual-explainers/reference.md) | Self-contained HTML explainers, ASCII diagrams, visual storytelling, layout verification |
| **TIR Algorithmic Art** | [SKILL.md](tir-algorithmic-art/SKILL.md) | [reference.md](tir-algorithmic-art/reference.md) | Seeded algorithmic art (p5.js/canvas) and deterministic parameter exploration |
| **TIR Image Prompts & Vision** | [SKILL.md](tir-image-prompts-and-vision/SKILL.md) | [reference.md](tir-algorithmic-art/reference.md) | Structured image-generation prompt specs and local Ollama vision inspection |
| **TIR Authoring Skills & References** | [SKILL.md](tir-authoring-skills-and-references/SKILL.md) | [reference.md](tir-authoring-skills-and-references/reference.md) | Designing, testing, evolving, and validating agent skills and idiomatic references |
| **TIR Agent Context & Prompts** | [SKILL.md](tir-agent-context-and-prompts/SKILL.md) | [reference.md](tir-agent-context-and-prompts/reference.md) | `AGENTS.md` / `CLAUDE.md` design, context budgets, agent creation, prompt contracts |
| **TIR Multi-Agent Orchestration** | [SKILL.md](tir-multi-agent-orchestration/SKILL.md) | [reference.md](tir-agent-context-and-prompts/reference.md) | Parallel dispatch, subagent-driven development, and multi-agent workflow boundaries |
| **TIR Claude Plugin Development** | [SKILL.md](tir-claude-plugin-development/SKILL.md) | [reference.md](tir-claude-plugin-development/reference.md) | Claude Code plugins, slash commands, hooks, MCP integration, settings, agents, setup, and Codex plugins |

## Build or review Rust

Pick the skill for the component you are changing, then use **TIR Rust Review** for a fresh review pass. Each Rust guide embeds the [core](_core.md); the eight writer guides also embed the [essentials](_essentials.md). Edit the sources, not the copies, and run `S01-skills-for-engineering-teams/sync-core.sh` from the repository root.

| Subject | Skill | Covers |
|---|---|---|
| **TIR Rust Application Service** | [SKILL.md](tir-rust-app-service/SKILL.md) | HTTP services, Axum/Actix, SQLx/Diesel, Tower, Tokio, auth, idempotency, health checks |
| **TIR Rust CLI** | [SKILL.md](tir-rust-cli/SKILL.md) | `clap`, exit codes, stdin/stdout/stderr, config/env, filesystem traversal, child processes |
| **TIR Rust Infra: Parsers** | [SKILL.md](tir-rust-infra-parsers/SKILL.md) | Tree-sitter, `syn`, `nom`/`winnow`, compilers, spans, diagnostics, rewrites |
| **TIR Rust Infra: Performance** | [SKILL.md](tir-rust-infra-performance/SKILL.md) | Hot loops, allocation/layout, benchmarks, caches, `rayon`, atomics, arenas, `no_std` |
| **TIR Rust Infra: Storage** | [SKILL.md](tir-rust-infra-storage/SKILL.md) | On-disk formats, WALs, snapshots, atomic writes, wire protocols, streaming decoders, queues |
| **TIR Rust Library** | [SKILL.md](tir-rust-library/SKILL.md) | Public API design, traits, generics, `thiserror`, builders, feature flags, semver, MSRV |
| **TIR Rust Review** | [SKILL.md](tir-rust-review/SKILL.md) | Pre-merge/pre-release review checklists, anti-patterns, gate audits, severity levels |
| **TIR Rust Tauri** | [SKILL.md](tir-rust-tauri/SKILL.md) | Tauri 2 desktop apps, IPC commands, capabilities, managed state, plugins, packaging |
| **TIR Rust Unsafe & FFI** | [SKILL.md](tir-rust-unsafe-ffi/SKILL.md) | `unsafe` invariants, raw pointers, `MaybeUninit`, `repr(C)`, C/Python/Node FFI, `Pin` |

Looking for the verbatim Superpowers or Stripe guides? See [upstream snapshots and licences](../S02-curated-upstream-skill-snapshots/ATTRIBUTION.md).
