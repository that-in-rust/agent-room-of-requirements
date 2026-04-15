---
name: tauri-executable-specs-01
description: Unify executable specifications, Tauri-first reliability, and Rust/Tauri architecture for desktop apps with a Rust backend and web frontend. Use when Codex needs to convert Tauri requests into REQ-TAURI contracts, choose command/state/capability/lifecycle boundaries, apply typed error and async safety patterns, select verification strategy, scope permissions and sidecars safely, or produce implementation plans and quality gates for Tauri 2 applications.
---

# Tauri Executable Specs 01

Use this skill to turn Tauri requests into decision-complete work packets that are spec-first, desktop-security-aware, and biased toward reliable Tauri 2 delivery.

## Mode Selection

Choose one or more modes before planning, implementation, or review:

- `Spec Mode`: use for vague feature requests, missing acceptance criteria, greenfield Tauri planning, or any request that needs `REQ-TAURI-*` contracts first.
- `App Architecture Mode`: use for commands, managed state, IPC shape, frontend/backend contracts, module structure, build hook seams, and Rust core boundary decisions.
- `Desktop Security Mode`: use for capabilities, permission scoping, filesystem/plugin access, CSP, sidecars, updater trust boundaries, and least-privilege design.
- `Lifecycle Mode`: use for tray, single-instance, deep links, window state, startup/setup flow, external binary packaging, and platform config drift.
- `Review Mode`: use for code or design review when the main question is desktop safety, reliability, or operability under change.

Default combinations:

- vague feature request: `Spec Mode` + `App Architecture Mode`
- command/state/frontend IPC work: `Spec Mode` + `App Architecture Mode`
- filesystem/plugin/capability/sidecar work: `App Architecture Mode` + `Desktop Security Mode`
- updater/tray/deep-link/single-instance/window-state work: `Desktop Security Mode` + `Lifecycle Mode`
- review or hardening pass: `Review Mode` + one or more of the above

## Workflow

1. Classify the Tauri task and choose the active mode set.
2. Write `REQ-TAURI-<NNN>.<REV>` contracts in `WHEN...THEN...SHALL`.
3. Define the design split across frontend contract, command layer, Rust core, and desktop capability/lifecycle boundaries.
4. Choose the verification mix deliberately.
5. Apply reliability rules.
6. Apply local conventions selectively.
7. Run quality gates and anti-pattern checks.

## Output Contract

Return results in this order:

1. `Tauri Work Mode`
2. `Executable Requirements`
3. `Tauri Design (Frontend/IPC/Rust Core + Permissions/Lifecycle)`
4. `Verification Matrix`
5. `Implementation Plan`
6. `Quality Gate Results`
7. `Open Questions`

Use traceability tables like:

| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |

## Guardrails

- Prefer Tauri-specific security and lifecycle rules over generic Rust defaults when they conflict.
- Make I/O-heavy commands async and use owned inputs for async command boundaries.
- Keep fallible command surfaces serializable with `Result<T, AppError>` or an equivalent boundary shape.
- Use least-privilege capabilities and scoped filesystem/plugin/sidecar permissions.
- Keep sidecar lifecycle explicit, bounded, and packaged deterministically.
- Apply four-word naming when feasible for new surfaces, but preserve API/window/command compatibility when renaming would be risky.

## Context Strategy

Load progressively:

1. Read [references/reference-map.md](./references/reference-map.md) first.
2. Read [references/tauri-executable-specs-playbook.md](./references/tauri-executable-specs-playbook.md) for vague requests, new features, contract writing, and Tauri design planning.
3. Read only the relevant sections of [references/tauri-doctrine.md](./references/tauri-doctrine.md) for Tauri-specific reliability, desktop security, IPC, and lifecycle boundaries.
4. Read [references/tauri-conventions-and-gates.md](./references/tauri-conventions-and-gates.md) before final verification and when selective local conventions might matter.

For large files, prefer heading search such as:

- `rg '^##|^###' references/tauri-executable-specs-playbook.md`
- `rg '^##|^###' references/tauri-doctrine.md`
- `rg '^##|^###' references/tauri-conventions-and-gates.md`

## References

- [Reference map](./references/reference-map.md)
- [Tauri executable specs playbook](./references/tauri-executable-specs-playbook.md)
- [Tauri doctrine](./references/tauri-doctrine.md)
- [Tauri conventions and gates](./references/tauri-conventions-and-gates.md)
