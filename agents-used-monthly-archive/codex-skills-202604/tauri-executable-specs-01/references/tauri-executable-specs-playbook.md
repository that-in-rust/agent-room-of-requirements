# Tauri Executable Specs Playbook

Use this playbook when a Tauri task needs executable requirements, frontend-to-Rust design planning, TDD sequencing, or a concrete verification plan before implementation.

## Table of Contents

1. Tauri Work Packet Template
2. Requirement Contract Template
3. Tauri Design Scaffold
4. Verification Matrix Template
5. TDD Loop
6. Tauri and Rust Test Skeletons
7. Vague-to-Executable Rewrite Patterns
8. Review Questions

## 1) Tauri Work Packet Template

Use this output shape when the request is not ready for immediate coding:

```markdown
## Tauri Work Mode
- Spec Mode
- App Architecture Mode

## Executable Requirements
### REQ-TAURI-001.0: <title>
**WHEN** ...
**THEN** the system SHALL ...
**AND** SHALL ...
**SHALL** ...

## Tauri Design (Frontend/IPC/Rust Core + Permissions/Lifecycle)
- Frontend contract:
- Command layer:
- Rust core:
- Managed state:
- Capabilities and permissions:
- Sidecars and external binaries:
- Lifecycle and platform behavior:

## Verification Matrix
| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |

## Implementation Plan
1. STUB
2. RED
3. GREEN
4. REFACTOR
5. VERIFY

## Quality Gate Results
- fmt:
- clippy:
- rust tests:
- rust build:
- frontend checks:
- tauri checks:
```

## 2) Requirement Contract Template

```markdown
### REQ-TAURI-001.0: <short title>

**WHEN** <trigger or input condition>
**THEN** the system SHALL <primary behavior>
**AND** SHALL <secondary measurable behavior>
**SHALL** <edge-case or default behavior>
```

Authoring rules:

- Keep one independently testable behavior per `SHALL` line.
- Use explicit units for latency, payload size, retries, startup bounds, or resource limits.
- Split security, lifecycle, and operability requirements when one clause would blur too many concerns.
- Use `REQ-TAURI-*` for this union even when the request begins as a generic desktop feature.

## 3) Tauri Design Scaffold

Plan the design before coding:

| area | role | design question |
| --- | --- | --- |
| Frontend contract | typed invoke payloads, event/channel consumption, UI-state expectations | what is the narrowest typed request/response or stream contract the UI should rely on? |
| Command layer | Tauri commands, request validation, serialization boundary | which behavior belongs in commands versus in deeper Rust services? |
| Rust core | domain logic, adapters, state types, sidecar supervision | what should stay testable and framework-light behind Tauri entrypoints? |
| Managed state | Tauri-managed state and synchronization model | what shared mutable state exists, and what mutex or async mutex discipline fits it? |
| Capabilities and permissions | capability files, window labels, filesystem/plugin access | what is the least-privilege set of permissions for the exact windows and operations involved? |
| Sidecars and lifecycle | sidecar spawn policy, startup/setup, updater, tray, deep links, single-instance, window state | what lifecycle ownership and packaging guarantees are needed for desktop correctness? |

Planning rules:

- Keep the frontend contract explicit before writing command code.
- Keep Tauri command surfaces thin when Rust core logic can be tested separately.
- Scope capabilities by real window labels, not UI titles or future hopes.
- Treat sidecars, updater, tray, and single-instance behavior as design decisions, not afterthoughts.

## 4) Verification Matrix Template

```markdown
| req_id | test_id | test_type | assertion | metric |
| --- | --- | --- | --- | --- |
| REQ-TAURI-001.0 | TEST-RUST-UNIT-001 | rust-unit | command service validates normalized request shape | correctness |
| REQ-TAURI-001.0 | TEST-RUST-INTEG-002 | rust-integration | command returns serializable `AppError` on invalid input | boundary |
| REQ-TAURI-002.0 | TEST-FRONTEND-003 | frontend | typed invoke caller handles success and failure shapes | contract |
| REQ-TAURI-003.0 | TEST-MOCK-004 | mocked-tauri | UI reacts correctly to mocked IPC and window behavior | desktop-boundary |
| REQ-TAURI-004.0 | TEST-LIFECYCLE-005 | desktop-boundary | second launch triggers single-instance handoff | lifecycle |
| REQ-TAURI-005.0 | TEST-PERF-006 | performance | p99 command latency < 100ms for stated fixture | latency |
```

Choose the smallest useful set:

- Rust unit and integration tests for Rust core and command paths
- frontend tests for typed invoke consumers and UI-state behavior
- mocked Tauri boundary tests when desktop runtime behavior needs frontend confidence
- desktop boundary or integration tests for tray, deep links, single-instance, updater, or sidecars
- performance only when thresholds are explicitly stated

## 5) TDD Loop

```text
STUB -> RED -> GREEN -> REFACTOR -> VERIFY
```

Execution policy:

1. `STUB`
- Write tests or test skeletons for each `REQ-TAURI-*`.
- Define command payloads, expected responses, window/capability assumptions, and fixtures.

2. `RED`
- Run the selected checks and confirm the failure matches the missing behavior or missing interface.

3. `GREEN`
- Implement the minimum code that satisfies the failing contract.

4. `REFACTOR`
- Improve decomposition, naming, and boundary ownership while the chosen tests stay green.

5. `VERIFY`
- Run the full chosen verification mix and confirm requirement traceability plus gate completion.

## 6) Tauri and Rust Test Skeletons

### Rust Unit

```rust
#[test]
fn test_req_tauri_001_command_validates_payload() {
    let input = create_valid_request_payload();
    let output = normalize_command_request(input).unwrap();
    assert_eq!(output.command_name, "sync-workspace");
}
```

### Rust Integration

```rust
#[tokio::test]
async fn test_req_tauri_002_command_returns_serializable_error() {
    let result = run_sync_workspace_command(invalid_request()).await;
    assert!(matches!(result, Err(AppError::InvalidRequest(_))));
}
```

### Frontend Typed Invoke

```ts
it("TEST-FRONTEND-001 handles typed invoke contract", async () => {
  const result = await invokeSyncWorkspaceSafely(validPayload);
  expect(result.status).toBe("completed");
});
```

### Mocked Tauri Boundary

```ts
it("TEST-MOCK-002 recovers from desktop command failure", async () => {
  mockIPC((cmd) => {
    if (cmd === "sync_workspace") {
      throw new Error("permission denied");
    }
  });
  render(<SyncWorkspaceScreen />);
  expect(await screen.findByText(/permission denied/i)).toBeVisible();
});
```

### Lifecycle Boundary

```markdown
Lifecycle boundary test idea:
- Launch primary instance
- Trigger second launch or deep-link open
- Assert handoff reaches the primary window
- Assert no duplicate long-running background service remains active
```

### Performance Contract

```rust
#[test]
fn test_req_tauri_003_command_performance_contract() {
    use std::time::{Duration, Instant};
    let fixture = create_large_fixture();
    let start = Instant::now();
    let _ = evaluate_preview_command(fixture).unwrap();
    assert!(start.elapsed() < Duration::from_millis(100));
}
```

## 7) Vague-to-Executable Rewrite Patterns

| vague statement | executable rewrite |
| --- | --- |
| "Add a Tauri sync feature." | "Expose a typed frontend invoke contract and a Rust command that validates input, reports progress, and returns a serializable result for the sync operation." |
| "Make permissions safer." | "Restrict filesystem and plugin capabilities to the minimum paths and commands needed by the named windows and sidecars." |
| "Handle app startup better." | "Initialize required state during setup without blocking the UI thread and restore the app to a ready state within the stated startup bound." |
| "Support tray and deep links." | "Route tray actions and deep-link events to the primary instance without spawning duplicate background workers or losing window focus semantics." |
| "Improve reliability." | "Return typed frontend-visible errors, avoid panics in command and lifecycle paths, and bound sidecar startup/retry behavior." |

## 8) Review Questions

- Which mode or combination of modes is active, and which one is primary?
- What is the smallest set of `REQ-TAURI-*` contracts that makes the work testable?
- What belongs in the frontend contract, command layer, and Rust core respectively?
- Which boundaries require capabilities, sidecar policy, or lifecycle ownership decisions?
- Which risks deserve Rust tests, frontend tests, mocked desktop tests, or desktop boundary checks instead of unit tests alone?
- Which names, command IDs, or window labels must stay stable even if a cleaner new name exists?
