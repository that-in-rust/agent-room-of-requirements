# Rust Agent Mega 01

One file for an AI coding agent that plans, writes, reviews or hardens Rust: libraries, CLIs,
async services, web backends, parsers, FFI wrappers and Tauri desktop apps. Read section 1
first; it routes you to the sections a task needs.

## 1. Operating principles and workflow

Rust work is not only a syntax problem. For every task decide three things before writing code:

1. what must be specified;
2. what must be designed at the type and boundary level;
3. what must be verified before the result can be trusted.

The aim is a decision-complete work packet or implementation that stays correct beyond the happy path.

### Default workflow

1. **Classify the task.** Name the component type first: library, CLI, async service, backend, parser or protocol, FFI wrapper, Tauri app, or review. Pick the primary work mode (section 2).
2. **Write executable requirements** (section 3). Reject vague claims such as "faster" or "more reliable" unless they carry a threshold.
3. **Define the architecture before coding** (section 4): layers, and trait seams where substitution or testability matters.
4. **Choose the verification mix deliberately** (section 5). Match tests to the real risk surface; do not default to unit tests only.
5. **Apply the reliability rules** (sections 6 to 10).
6. **Apply local conventions selectively** (section 12).
7. **Run quality gates and anti-pattern checks before handoff** (sections 13 and 16).

### Guardrails

- Keep invalid states unrepresentable where practical.
- Treat async, cancellation and concurrency as correctness problems, not only performance concerns.
- Do not force every repo-local convention onto every Rust task.
- Do not recommend unsafe, lock-free or proc-macro-heavy designs as defaults; use them only when the task truly requires them.
- Stay skeptical about: malformed input, non-UTF-8 boundaries, backpressure, cancellation, semver surface changes, and detached task lifecycles.

## 2. Work modes and output contract

Choose one or more modes before planning or coding.

| Mode | Use when |
| --- | --- |
| Spec Mode | The request is vague, acceptance criteria are missing, success is not measurable yet, or the work needs `REQ-RUST-*` contracts first |
| Delivery Mode | The task needs layer boundaries, trait seams, TDD order, decomposition and implementation sequencing |
| Reliability Mode | The main risk is public API design, error surfaces, async and cancellation, concurrency, diagnostics, unsafe, FFI or release hardening |
| Review Mode | The task is a code or design review, and the question is whether the Rust will stay safe, diagnosable and maintainable under change |

Default combinations:

- vague feature request: Spec + Delivery
- library or public API work: Spec + Reliability
- async service, parser or protocol work: Delivery + Reliability
- review or hardening pass: Review + Reliability

### Output contract

Return results in this order:

1. Rust Work Mode
2. Executable Requirements
3. Rust Design (L1/L2/L3 + Traits)
4. Verification Matrix
5. Implementation Plan
6. Quality Gate Results
7. Open Questions

Trace every requirement to a test in a concise table:

| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |

## 3. Executable specifications

- Give every requirement an identifier of the form `REQ-RUST-<NNN>.<REV>`.
- Express behavior as `WHEN ... THEN ... SHALL`.
- A requirement without a measurable threshold or an observable effect is not a requirement yet; send it back.

## 4. Architecture and boundaries

- Separate code into three layers: **L1 core** (pure domain logic), **L2 std** (standard-library facilities), **L3 external** (third-party crates and the outside world).
- Keep L3 dependencies out of L1.
- Define trait seams before concrete adapters when substitution or testability matters.

## 5. Verification and test-first delivery

Pick the verification mix from: unit, integration, doctest, compile-fail, property, fuzz, `loom`, `Miri`, performance, and coverage gates. Choose by risk surface.

## 6. Types and API design

- Prefer newtypes, explicit conversions, and designs that make invalid states unrepresentable.

## 7. Ownership, borrowing and data handling

## 8. Errors and recovery

- Keep library errors typed and boundary-aware.

## 9. Async and concurrency

- Never block inside async code, and never hold a lock guard across `.await`.
- Prefer bounded concurrency and cancellation-aware code.

## 10. Unsafe and FFI

- Keep unsafe surfaces minimal.

## 11. Performance

## 12. Naming, modules and documentation

- Use four-word names for new functions and commands when feasible.
- Preserve public API compatibility when a rename is risky.
- Keep modules cohesive and docs synchronized with behavior.

## 13. Anti-patterns

## 14. Rust web backends

## 15. Tauri desktop apps

Tauri work is neither only frontend work nor only Rust work. Decide what must be specified, what must be designed across the frontend, command, Rust core and desktop boundaries, and what must be verified. Where Tauri-specific security or lifecycle guidance conflicts with a generic Rust default, the Tauri guidance wins.

### Tauri work modes

| Mode | Use when |
| --- | --- |
| Spec Mode | The request is vague, acceptance criteria are missing, or the work needs `REQ-TAURI-*` contracts first |
| App Architecture Mode | The task needs command boundaries, managed state, IPC shape, frontend/backend contracts, module structure or build seam decisions |
| Desktop Security Mode | The main risk is capabilities, permission scoping, filesystem or plugin access, CSP, sidecars or updater trust boundaries |
| Lifecycle Mode | The main risk is tray, single-instance, deep links, window state, startup/setup, external binary packaging or platform config drift |
| Review Mode | The question is whether the app will stay safe, reliable and operable under change |

Default combinations:

- vague feature request: Spec + App Architecture
- command, state or frontend IPC work: Spec + App Architecture
- filesystem, plugin, capability or sidecar work: App Architecture + Desktop Security
- updater, tray, deep-link, single-instance or window-state work: Desktop Security + Lifecycle
- review or hardening pass: Review + one or more of the above

### Tauri workflow

1. **Classify the task and choose modes.** Name the component type first: feature request, command or IPC surface, permission boundary, sidecar or external binary, lifecycle path, or review.
2. **Write executable requirements** as `REQ-TAURI-<NNN>.<REV>` in `WHEN ... THEN ... SHALL` form. Reject "safer" or "more reliable" without a threshold or an explicit boundary effect.
3. **Define the design before coding.** Split it across the frontend contract, the command layer, the Rust core, and the desktop capability and lifecycle boundaries. Keep the frontend invoke contract explicit. Keep command functions thin so the deeper Rust logic stays testable.
4. **Choose the verification mix:** Rust unit, Rust integration, frontend tests, typed invoke contract checks, mocked Tauri boundary tests, desktop boundary tests; performance tests only when a metric is stated. Do not default to one layer only.
5. **Apply the Tauri reliability rules** (below).
6. **Apply local conventions selectively:** four-word names for new functions and commands when feasible; preserve API, window, command and event compatibility when a rename is risky; keep modules cohesive and the registration structure explicit.
7. **Run quality gates and anti-pattern checks before handoff.**

Output order: Tauri Work Mode, Executable Requirements, Tauri Design (Frontend/IPC/Rust Core + Permissions/Lifecycle), Verification Matrix, Implementation Plan, Quality Gate Results, Open Questions. Use the same traceability table as section 2.

### Tauri reliability and security rules

- Command errors are serializable and visible to the frontend. Never panic in a command.
- Keep managed state disciplined.
- Capabilities are least-privilege by default. Scope filesystem, plugin, sidecar and updater permissions.
- Bound the sidecar lifecycle; keep binary packaging and lifecycle ownership explicit.
- Async command inputs are owned values.
- Treat tray, deep links, single-instance and startup/setup behavior as correctness concerns, not polish.
- Stay skeptical about: malformed input, permission creep, event spam, detached sidecars, updater trust, and lifecycle drift across platforms.

## 16. Quality gates and commands

## 17. Review checklist
