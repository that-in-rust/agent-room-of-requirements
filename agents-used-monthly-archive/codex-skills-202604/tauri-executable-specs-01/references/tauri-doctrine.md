# Tauri Doctrine

Use this file as the primary Tauri-specific reliability, security, and operability reference behind `tauri-executable-specs-01`.

It preserves the scored Tauri app-layer patterns, anti-patterns, TDD-first checks, and final boundary claim from `tauri-coder-01`.

## Premise Check

`rust-coder-01.md` is useful, but it is not complete.

- It repeats core sections near the top.
- Its later sections drift into heading-only inventories instead of executable guidance.
- It has too few concrete anti-patterns, desktop-specific failure modes, and verification rules.

This file is intentionally narrower and more operational:

- Tauri-first, not generic Rust-first
- reliability and security over feature breadth
- only patterns scored above `80/100`
- focused on error-free production desktop code

## Source Base

Primary source notes from `Notes2026`:

- `IdiomaticPatterns2026/RustTauri/01-Tauri-Patterns-Level1-WebResearch.md`
- `IdiomaticPatterns2026/RustTauri/02-CrashCourse-MCU-MintoPyramid.md`
- `UnclassifiedDocs/10_Miscellaneous_Technical/parseltongue-opencode-integration-spec.md`
- `MDWisdom202601/LibraryIdioms/LibOpenCode/01-persist-payload-limits.md`
- `UnclassifiedDocs/10_Miscellaneous_Technical/opencode-genius-idiomatic-patterns.md`

Official docs cross-checked:

- commands
- capabilities
- capabilities for windows and platforms
- sidecars
- filesystem plugin
- updater plugin
- tests
- mocking
- system tray
- configuration files
- cli plugin
- deep-link plugin
- single-instance plugin
- window-state plugin

## Selection Rubric

Each candidate pattern was rescored for this file:

- Correctness and bug prevention: `35`
- Security and least privilege: `25`
- Operability and recovery: `20`
- Tauri-specific leverage: `20`

Cut line: `81+`

## Coverage Verdict

Before this revision: `no`.

Why not:

- it was strong on backend reliability boundaries
- it was weaker on command/module structure
- it under-covered binary IPC and raw request handling
- it under-covered window-label privilege design, tray lifecycle, and testing boundaries

After this revision:

- strong enough for most app-layer Tauri coding tasks
- still not a full encyclopedia for plugin authoring internals, mobile-only APIs, or every official plugin
- intentionally biased toward patterns that keep generated code correct, secure, and operable

## Chosen Patterns

| Score | Pattern | Why It Made The Cut |
| --- | --- | --- |
| 98 | `configure_capability_permissions_minimally` | Biggest security and blast-radius reducer in Tauri 2 |
| 96 | `handle_thiserror_results_serializably` | Prevents panics and preserves readable frontend failures |
| 95 | `manage_mutex_state_globally` | Shared state is where desktop race bugs start |
| 94 | `define_async_command_handler` | Prevents UI stalls and async lifetime traps |
| 93 | `supervise_sidecar_lifecycle_explicitly` | Sidecars are powerful but fragile without health checks |
| 92 | `resolve_path_scopes_safely` | Filesystem bugs become security bugs quickly |
| 91 | `bound_store_payload_sizes` | Prevents runaway persistence and slow restores |
| 90 | `persist_blob_payloads_outofband` | Fixes the most expensive desktop persistence mistake |
| 89 | `use_official_plugin_safely` | Plugin power needs matching permissions discipline |
| 89 | `wire_setup_lifecycle_cleanly` | App startup is where initialization bugs and UI stalls often begin |
| 88 | `stream_channel_progress_efficiently` | Correct IPC shape for long-running or high-volume work |
| 88 | `label_window_capabilities_explicitly` | Window labels, not titles, define security boundaries |
| 88 | `test_mocked_tauri_boundaries` | Prevents frontend regressions without requiring a live desktop runtime |
| 87 | `structure_command_modules_explicitly` | Tauri command naming and registration rules are easy for LLMs to get subtly wrong |
| 86 | `apply_csp_headers_strictly` | Production XSS hardening still matters in desktop apps |
| 85 | `configure_updater_signatures_securely` | Safe updates are part of reliability, not just distribution |
| 84 | `invoke_typed_commands_frontend` | Prevents silent IPC contract drift |
| 84 | `inspect_raw_requests_carefully` | Important when JSON is the wrong transport and request validation matters |
| 83 | `emit_backend_events_sparingly` | Good for progress and notifications, bad for bulk streams |
| 83 | `return_binary_payloads_optimally` | Prevents large IPC responses from degrading into slow JSON blobs |
| 82 | `scope_sidecar_permissions_exactly` | Sidecars need command and argument boundaries, not just process management |
| 81 | `configure_tray_menu_lifecycle` | Common desktop shell pattern that benefits from stable event handling |
| 85 | `configure_build_hooks_consistently` | Tauri apps fail surprisingly often at the frontend/backend seam |
| 84 | `merge_platform_configs_deliberately` | Platform drift is easier to manage in config than in runtime branches |
| 85 | `declare_external_bins_explicitly` | Sidecar packaging breaks unless naming and target triples are exact |
| 84 | `configure_single_instance_handoff` | Desktop apps need deterministic handoff on second launch |
| 84 | `handle_deep_links_with_single_instance` | Deep links are part IPC, part OS integration, part trust boundary |
| 83 | `declare_cli_contracts_explicitly` | Desktop launch semantics should be modeled, not improvised |
| 82 | `restore_window_state_without_flash` | Window state is a real UX and lifecycle concern, not cosmetic sugar |

## Non-Negotiables

- All fallible commands return `Result<T, AppError>`.
- Async commands use owned inputs.
- Shared mutable state lives in Tauri-managed mutexes, not ad hoc globals.
- Capabilities are window-scoped and least-privilege.
- `plugin-store` is for small structured state, not binary payloads.
- Large or streaming IPC uses channels or binary responses, not event spam.
- Sidecars get health checks, bounded startup waits, explicit restart rules, and log caps.
- No `unwrap()` or `expect()` in command paths that can be hit by users.

## Pattern 1: `define_async_command_handler`

**Score:** `94/100`

Use this for commands that touch disk, network, process spawning, or anything that can stall the UI.

```rust
use serde::Serialize;

#[derive(Serialize)]
struct GreetResponse {
    message: String,
}

#[tauri::command]
async fn greet_user(name: String) -> Result<GreetResponse, AppError> {
    tokio::time::sleep(std::time::Duration::from_millis(50)).await;
    Ok(GreetResponse {
        message: format!("Hello, {name}!"),
    })
}
```

Reliability contract:

```text
WHEN a frontend invokes a backend command
THEN I/O commands SHALL be async
AND async commands SHALL use owned inputs
AND command registration SHALL stay centralized
```

Avoid:

- borrowed inputs like `&str` in async commands
- `std::thread::sleep` inside async commands
- scattered `generate_handler!` registration

## Pattern 2: `manage_mutex_state_globally`

**Score:** `95/100`

Let Tauri manage global state and only add interior mutability where it is actually needed.

Rules:

- Use `std::sync::Mutex` for short synchronous access.
- Use `tauri::async_runtime::Mutex` only when the lock must live across `.await`.
- Do not wrap managed state in `Arc` before `.manage(...)`; Tauri already handles shared ownership.
- Prefer dedicated state types and aliases so command signatures stay consistent.

## Pattern 3: `handle_thiserror_results_serializably`

**Score:** `96/100`

Make every frontend-visible failure explicit and serializable.

Key rule:

- frontend-reachable failures should preserve readable structured error surfaces instead of panicking or collapsing into opaque strings too late

## Pattern 4: `configure_capability_permissions_minimally`

**Score:** `98/100`

Capabilities are the primary Tauri 2 security boundary. Scope them as narrowly as possible by window label, platform, and permission set.

Rules:

- grant the minimum command/plugin access each window needs
- treat broad filesystem or shell permissions as security decisions, not convenience defaults
- model labels as security boundaries, not cosmetic names

## Pattern 5: `resolve_path_scopes_safely`

**Score:** `92/100`

Filesystem mistakes become security mistakes quickly.

Rules:

- resolve paths through approved scope-aware APIs
- keep path decisions close to capability definitions
- reject over-broad path assumptions and unchecked traversal

## Pattern 6: `use_official_plugin_safely`

**Score:** `89/100`

Prefer official plugins, but match every plugin with explicit permission discipline.

Rules:

- plugin choice is not enough; permission scope is the safety story
- prefer official plugin contracts over custom ad hoc OS bridging

## Pattern 7: `invoke_typed_commands_frontend`

**Score:** `84/100`

Frontend invoke wrappers should preserve a typed contract rather than scattering stringly typed calls.

Rules:

- keep the invoke contract centralized and typed
- normalize error/result shapes at the boundary

## Pattern 8: `stream_channel_progress_efficiently`

**Score:** `88/100`

Use channels for long-running or high-volume progress instead of flooding the app with events.

Rules:

- channels for sustained streams
- events for sparse notifications
- keep payloads bounded and explicit

## Pattern 9: `emit_backend_events_sparingly`

**Score:** `83/100`

Events are useful, but they are the wrong default for bulk transport.

Rules:

- use backend events for notifications and coarse progress
- avoid event spam for large payloads or continuous streams

## Pattern 10: `apply_csp_headers_strictly`

**Score:** `86/100`

Desktop apps still need browser-hardening discipline.

Rules:

- keep CSP explicit
- do not widen policy casually to unblock convenience code

## Pattern 11: `supervise_sidecar_lifecycle_explicitly`

**Score:** `93/100`

Sidecars should have health checks, bounded startup waits, explicit restart rules, and log caps.

Rules:

- make startup bounded and observable
- define lifecycle ownership rather than hoping the child process behaves

## Pattern 12: `bound_store_payload_sizes`

**Score:** `91/100`

`plugin-store` is for small structured state, not unbounded desktop blobs.

Rules:

- bound payload sizes
- keep large data out of store-backed persistence

## Pattern 13: `persist_blob_payloads_outofband`

**Score:** `90/100`

Large binary or document payloads should live outside store-backed configuration state.

Rules:

- store metadata in structured state
- store large blobs in files with explicit path and lifecycle handling

## Pattern 14: `configure_updater_signatures_securely`

**Score:** `85/100`

Updater behavior is a trust boundary, not only a distribution detail.

Rules:

- treat signatures, channels, and artifact provenance as part of correctness

## Pattern 15: `structure_command_modules_explicitly`

**Score:** `87/100`

Keep command modules and registration structure explicit so naming and handler wiring stay easy to audit.

Rules:

- centralize registration
- avoid hidden command sprawl

## Pattern 16: `wire_setup_lifecycle_cleanly`

**Score:** `89/100`

Startup should initialize just enough state without blocking the UI into oblivion.

Rules:

- setup logic should be bounded
- hand off long-running work to owned, supervised paths

## Pattern 17: `return_binary_payloads_optimally`

**Score:** `83/100`

Do not degrade binary IPC into giant JSON blobs.

Rules:

- use the transport shape that matches the payload
- keep binary responses explicit and efficient

## Pattern 18: `inspect_raw_requests_carefully`

**Score:** `84/100`

Raw request handling is for cases where JSON helpers are not enough; validate carefully when you drop lower-level.

Rules:

- validate early
- keep request parsing logic narrow and auditable

## Pattern 19: `scope_sidecar_permissions_exactly`

**Score:** `82/100`

Sidecars need precise command and argument permissions, not just spawn permission.

Rules:

- whitelist the executable and expected arguments
- avoid generic shell escape hatches

## Pattern 20: `label_window_capabilities_explicitly`

**Score:** `88/100`

Window labels are the real security boundary in Tauri capabilities.

Rules:

- reason in labels, not titles
- scope window capability differences intentionally

## Pattern 21: `configure_tray_menu_lifecycle`

**Score:** `81/100`

Tray interactions should have stable event handling and deterministic state transitions.

Rules:

- keep tray behavior lifecycle-aware
- avoid duplicate or conflicting event wiring

## High-Confidence Anti-Patterns

### 1. Blocking async commands

- do not block inside async command handlers

### 2. Borrowed async inputs

- do not use borrowed inputs for async command boundaries

### 3. Broad filesystem permissions

- do not widen filesystem access beyond the actual paths and windows involved

### 4. Panicking command paths

- do not leave `unwrap()` or `expect()` in user-reachable command or lifecycle paths

### 5. Double-wrapping managed state

- do not add unnecessary `Arc` ownership around state already managed by Tauri

### 6. Using plugin-store as a blob sink

- do not treat structured store state as a large binary persistence layer

### 7. Unchecked sidecar spawning

- do not spawn sidecars without command scoping, startup bounds, or lifecycle ownership

## TDD-First Checks For Tauri

- write or update typed boundary tests before widening the command surface
- validate serializable error shapes before UI handling depends on them
- test lifecycle-sensitive behavior where tray, updater, single-instance, or deep links are involved
- prefer mocked desktop-boundary tests when full runtime integration is heavier than necessary

## Pattern 23: `configure_build_hooks_consistently`

**Score:** `85/100`

Treat frontend/backend build seams as part of the design.

## Pattern 24: `merge_platform_configs_deliberately`

**Score:** `84/100`

Platform drift belongs in explicit config decisions, not scattered runtime branching.

## Pattern 25: `declare_external_bins_explicitly`

**Score:** `85/100`

External binary packaging must be exact about names, target triples, and ownership.

## Pattern 26: `configure_single_instance_handoff`

**Score:** `84/100`

Second-launch behavior should be deterministic and routed to the primary instance.

## Pattern 27: `handle_deep_links_with_single_instance`

**Score:** `84/100`

Deep links mix OS integration, IPC, and trust boundaries.

## Pattern 28: `declare_cli_contracts_explicitly`

**Score:** `83/100`

Desktop launch semantics should be modeled rather than improvised.

## Pattern 29: `restore_window_state_without_flash`

**Score:** `82/100`

Window state restore is a real lifecycle concern, not cosmetic polish.

## Final Thesis

Use Tauri-specific rules first when they sharpen desktop safety, reliability, or operability.

This doctrine is strong for Tauri 2 app-layer work, but it is not a full guide for:

- plugin-author internals
- mobile-only APIs
- non-Tauri desktop shells
