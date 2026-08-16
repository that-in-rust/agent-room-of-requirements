# Tauri Conventions and Gates

Use this file near the end of planning, implementation, or review to apply selective local conventions and to enforce final Tauri delivery gates.

## 1) Selective Local Conventions

- Use four-word naming for new functions and commands when feasible.
- Preserve existing API, window label, command identifier, and event compatibility when renaming is risky.
- Keep command registration centralized and module structure explicit.
- Keep modules cohesive and purpose-specific.
- Treat Mermaid as a documentation convention only when the project already expects it. Do not apply it as a universal Tauri rule.

## 2) Tauri Implementation Conventions

- Return `Result<T, AppError>` or an equivalent serializable error surface from fallible command paths.
- Make I/O-heavy commands async and keep async command inputs owned.
- Keep shared mutable state in Tauri-managed state with the narrowest mutex that fits the access pattern.
- Scope capabilities by real window label and least privilege.
- Scope filesystem, plugin, and sidecar permissions exactly instead of broadly.
- Keep plugin-store for small structured state, not large blobs.
- Use channels or binary responses for long-running or high-volume payloads instead of event spam.
- Supervise sidecars with startup checks, bounded waits, explicit restart rules, and explicit binary packaging declarations.
- Keep docs, examples, tests, and capability/config files synchronized with behavior changes.

## 3) Runtime and Safety Gates

- Verify no blocking work runs directly in async command contexts.
- Verify no lock guard or mutable access pattern crosses `.await` unless the chosen async mutex model explicitly requires it.
- Verify no `unwrap()` or `expect()` remains in user-reachable command or lifecycle paths.
- Verify no secrets or sensitive payloads are logged.
- Verify updater, sidecar, filesystem, and plugin boundaries stay least-privilege.
- Verify lifecycle ownership for tray, deep links, single-instance handoff, sidecars, and startup/setup work.

## 4) Verification Command Gate

Run and require success:

```bash
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --all-targets --all-features
cargo build --all-targets --all-features
```

Also run the repo-normal frontend and Tauri checks that correspond to the changed boundary, for example:

```bash
pnpm test
pnpm build
pnpm tauri build
```

Use the repo's actual package manager and scripts rather than forcing these exact command names.

## 5) Release Readiness Checklist

- [ ] Requirements are executable and measurable.
- [ ] Each `REQ-TAURI-*` has at least one linked test.
- [ ] Command, IPC, and UI-state behavior are covered at the right boundary.
- [ ] Capability, filesystem, plugin, sidecar, and lifecycle choices are explicit.
- [ ] Rust quality gates pass.
- [ ] Repo-normal frontend or desktop checks pass for the changed surface.
- [ ] No `TODO`, `STUB`, or `FIXME` placeholders remain in finalized code.

## 6) Anti-Patterns to Reject

- vague desktop requirements with no measurable assertions
- generic Rust rules overriding Tauri-specific capability or lifecycle safety guidance
- broad filesystem, plugin, or shell permissions used as convenience defaults
- event spam for large payload or progress streams
- sidecar spawning without bounded startup, permission scoping, or packaging declarations
- command surfaces that panic or return opaque, unserializable failures
- duplicated doctrine copied into multiple outputs instead of routing through the references

## 7) Rules Not to Universalize

Do not treat these as default Tauri quality rules:

- repeated doctrine duplication across skill files and references
- "run `cargo clean` constantly"
- generic Rust guidance that weakens Tauri-specific security choices
- four-word naming when it would break stable command, API, or window compatibility
- Mermaid-only documentation as a universal Tauri requirement
