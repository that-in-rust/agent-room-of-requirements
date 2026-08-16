---
name: tauri-coder-01
description: Reliability-first Tauri coding guide for desktop apps in Rust with a web frontend. Use when Codex needs to implement, refactor, review, or harden Tauri 2 applications involving commands, managed state, capabilities, windows, plugins, sidecars, filesystem access, updater or tray lifecycle, deep links, single-instance handling, or desktop security and operability.
---

# Tauri Coder 01

## Overview

Apply a Tauri-first reliability and security baseline for desktop app work. Keep this skill lean: use [references/reference-map.md](references/reference-map.md) for routing and [references/doctrine.md](references/doctrine.md) as the detailed playbook.

## Workflow

1. Classify the task before making changes. Common buckets are commands, shared state, capabilities and permissions, filesystem or plugin access, sidecars, IPC payload shape, desktop lifecycle, or testing.
2. Skim [references/reference-map.md](references/reference-map.md), then open only the relevant sections in [references/doctrine.md](references/doctrine.md).
3. Apply the default rules below while matching the repo's runtime and plugin choices.
4. Verify with the repo's normal Rust, frontend, and Tauri test or build commands.
5. If a requested change weakens permissions or lifecycle safety, pause and choose the least-privilege version explicitly.

## Default Rules

- Make I/O-heavy commands async and give async commands owned inputs.
- Return `Result<T, AppError>` or an equivalent serializable error type from fallible commands.
- Keep command registration centralized and module structure explicit.
- Put shared mutable state in Tauri-managed state with the narrowest mutex that fits the access pattern.
- Scope capabilities by window label and least privilege.
- Scope filesystem, plugin, and sidecar permissions exactly instead of broadly.
- Use channels or binary responses for large payloads or long-running progress.
- Keep plugin-store for small structured state, not large blobs.
- Supervise sidecars with startup checks, bounded waits, restart rules, and explicit packaging declarations.
- Avoid `unwrap()` and `expect()` in user-reachable command and lifecycle paths.

## Reference Use

- Use [references/reference-map.md](references/reference-map.md) first for quick routing.
- Use [references/doctrine.md](references/doctrine.md) for the full scored patterns, anti-patterns, and TDD checks.
- For large-file navigation, prefer heading search such as `rg '^##|^###' references/doctrine.md`.

## Boundary Notes

- Treat this skill as partial guidance for plugin-author internals, mobile-only APIs, or non-Tauri desktop shells.
- If the repo uses an established permission model or plugin stack, preserve it unless it is broader than needed.
