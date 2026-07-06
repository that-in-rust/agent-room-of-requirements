# Tauri Executable Specs Reference

Use this file as the standalone reference behind `tauri-executable-specs-01`.

It merges the strongest parts of:

- executable specs and TDD-first planning
- Tauri-first command, capability, IPC, and lifecycle design
- desktop security and operability guidance
- selective Rust/Tauri local conventions such as four-word naming where feasible

## 1) Work Modes

| mode | use when | emphasis |
| --- | --- | --- |
| `Spec Mode` | Request is vague or not yet measurable | `REQ-TAURI-*`, acceptance criteria, traceability |
| `App Architecture Mode` | Work needs frontend/IPC/command/core structure | invoke contracts, managed state, module shape, build seams |
| `Desktop Security Mode` | Main risk is permissions or trust boundaries | capabilities, filesystem/plugin scope, CSP, sidecars, updater trust |
| `Lifecycle Mode` | Main risk is desktop runtime behavior | tray, single-instance, deep links, window state, setup, packaging |
| `Review Mode` | Main task is critique or hardening | anti-patterns, safety, operability, compatibility, final gates |

Default combinations:

- vague feature request -> `Spec Mode` + `App Architecture Mode`
- command/state/frontend IPC work -> `Spec Mode` + `App Architecture Mode`
- filesystem/plugin/capability/sidecar work -> `App Architecture Mode` + `Desktop Security Mode`
- updater/tray/deep-link/single-instance/window-state work -> `Desktop Security Mode` + `Lifecycle Mode`
- review or hardening pass -> `Review Mode` + one or more of the above

## 2) Choose by Task Type

### Commands and Frontend IPC

Prioritize:

- typed invoke contracts
- serializable command errors
- async command ownership rules
- clear split between command layer and deeper Rust core
- Rust integration plus frontend contract tests

### Shared State and Rust Core

Prioritize:

- managed state discipline
- explicit state ownership and synchronization choice
- centralized command registration and module structure
- Rust unit and integration tests around the core boundary

### Capabilities, Permissions, and Filesystem or Plugin Access

Prioritize:

- capability scoping by window label
- least-privilege filesystem and plugin access
- CSP hardening where relevant
- permission review before feature convenience

### Sidecars and External Binaries

Prioritize:

- exact sidecar permissions and arguments
- startup bounds, health checks, restart policy, and log caps
- explicit external binary packaging
- lifecycle ownership and failure visibility

### Lifecycle and Platform Integration

Prioritize:

- setup/startup boundaries
- tray event flow
- single-instance handoff
- deep-link routing
- window-state restore
- platform config drift management

### Review or Hardening Pass

Prioritize:

- panic and serialization risks in command paths
- permission creep
- lifecycle ownership gaps
- event spam and binary payload misuse
- final gate completeness

## 3) Requirement Contract Template

```markdown
### REQ-TAURI-001.0: <short title>

**WHEN** <trigger or input condition>
**THEN** the system SHALL <primary behavior>
**AND** SHALL <secondary measurable behavior>
**SHALL** <edge-case or default behavior>
```

Rules:

- Keep each `SHALL` independently testable.
- Use explicit units for latency, payload size, retries, startup bounds, or resource limits.
- Split security, lifecycle, and operability requirements rather than hiding them in one broad clause.

## 4) Tauri Design Scaffold

Plan the design before coding:

| area | role | question |
| --- | --- | --- |
| Frontend contract | typed invoke payloads, responses, events, or channels | what exact UI-facing boundary should stay stable? |
| Command layer | Tauri commands and request validation | what belongs in the command boundary versus deeper Rust services? |
| Rust core | domain logic, adapters, state types, sidecar supervision | what should stay testable and framework-light? |
| Managed state | Tauri-managed shared state and synchronization | what state is shared, and what mutex model fits it? |
| Capabilities and permissions | capability files, labels, filesystem/plugin scope | what is the least privilege set for the actual windows and actions? |
| Lifecycle and packaging | setup, tray, updater, single-instance, deep links, external binaries | what lifecycle ownership and packaging guarantees are required? |

Planning rules:

- keep the frontend invoke contract explicit before implementation
- keep Tauri command surfaces thin where deeper Rust logic can stay testable
- scope permissions by real window labels and concrete actions
- treat lifecycle and packaging as part of design, not deployment cleanup

## 5) Verification Selection Matrix

| verification type | choose it when |
| --- | --- |
| Rust unit | behavior is local and deterministic inside Rust core |
| Rust integration | behavior crosses command, adapter, or serialization boundaries |
| frontend test | UI logic depends on typed command/event results |
| typed invoke contract check | stringly IPC drift is a material risk |
| mocked Tauri boundary test | desktop runtime behavior must be validated without a full live shell |
| desktop boundary test | tray, deep links, single-instance, updater, or window-state behavior is central |
| performance | latency or payload thresholds were explicitly stated |

## 6) TDD Loop

```text
STUB -> RED -> GREEN -> REFACTOR -> VERIFY
```

Execution policy:

- `STUB`: write tests or test skeletons for each `REQ-TAURI-*`
- `RED`: confirm the failure matches the missing contract or boundary
- `GREEN`: implement the minimum code that satisfies the contract
- `REFACTOR`: improve decomposition, ownership, and naming while staying green
- `VERIFY`: run all chosen gates and confirm requirement traceability

## 7) Default Reliability and Security Stack

If you do not know what to prioritize, start here:

1. make frontend-to-command contracts explicit and typed
2. keep command failures serializable and user-reachable paths panic-free
3. keep shared mutable state in disciplined Tauri-managed boundaries
4. make permissions least-privilege by window label and action
5. use channels or binary responses for large or long-running IPC
6. supervise sidecars and external binaries explicitly
7. treat updater, tray, deep links, single-instance, and window state as correctness concerns

## 8) Conventions and Gates

Selective local conventions:

- use four-word naming when feasible for new functions and commands
- preserve stable APIs, command IDs, event names, and window labels when renaming is risky
- keep command registration centralized and module structure explicit
- treat Mermaid as a project convention only when already expected

Required command gates:

```bash
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --all-targets --all-features
cargo build --all-targets --all-features
```

Also require the repo-normal frontend and Tauri checks for the changed boundary.

## 9) High-Value Anti-Patterns

Reject these by default:

- vague desktop requirements with no measurable assertions
- generic Rust rules overriding Tauri-specific capability or lifecycle safety guidance
- borrowed inputs on async command boundaries
- `unwrap()` or `expect()` in user-reachable command or lifecycle paths
- broad filesystem, plugin, or sidecar permissions used as convenience defaults
- event spam for large payloads or streaming progress
- plugin-store used as a blob sink
- unchecked sidecar spawning with no lifecycle ownership
- updater, tray, or deep-link behavior treated as post-hoc polish

## 10) Output Contract

When producing a substantial Tauri response, return results in this order:

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
