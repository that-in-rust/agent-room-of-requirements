# Reference Map

Use this file first to route the request before loading heavier Tauri references.

## 1) Choose the Work Mode

| mode | use when | read next |
| --- | --- | --- |
| `Spec Mode` | Feature request is vague, acceptance criteria are missing, or success is not measurable yet | `tauri-executable-specs-playbook.md` |
| `App Architecture Mode` | Work needs command boundaries, managed state, IPC design, frontend/backend contracts, module structure, or build seam decisions | `tauri-executable-specs-playbook.md`, then relevant sections of `tauri-doctrine.md` |
| `Desktop Security Mode` | Main risk is permissions, capabilities, filesystem/plugin access, CSP, sidecars, or updater trust boundaries | `tauri-doctrine.md`, then `tauri-conventions-and-gates.md` |
| `Lifecycle Mode` | Main risk is tray, single-instance, deep links, window state, startup/setup, external binary packaging, or platform config drift | `tauri-doctrine.md`, then `tauri-conventions-and-gates.md` |
| `Review Mode` | The task is code review or design review and the main question is long-term desktop safety and operability | `tauri-doctrine.md`, then `tauri-conventions-and-gates.md`, then `tauri-executable-specs-playbook.md` only if contracts are missing |

## 2) Choose by Task Type

### Commands and Frontend IPC

Read in this order:
1. `tauri-executable-specs-playbook.md`
2. `tauri-doctrine.md`
   - `Pattern 1` to `Pattern 3`
   - `Pattern 7`
   - `Pattern 8`, `Pattern 17`, and `Pattern 18`
3. `tauri-conventions-and-gates.md`

### Shared State and Rust Core

Read in this order:
1. `tauri-executable-specs-playbook.md`
2. `tauri-doctrine.md`
   - `Pattern 2`
   - `Pattern 15`
   - `Pattern 16`
3. `tauri-conventions-and-gates.md`

### Capabilities, Permissions, and Filesystem or Plugin Access

Read in this order:
1. `tauri-executable-specs-playbook.md`
2. `tauri-doctrine.md`
   - `Pattern 4` to `Pattern 6`
   - `Pattern 10`
   - `Pattern 19` and `Pattern 20`
3. `tauri-conventions-and-gates.md`

### Sidecars and External Binaries

Read in this order:
1. `tauri-executable-specs-playbook.md`
2. `tauri-doctrine.md`
   - `Pattern 11`
   - `Pattern 19`
   - `Pattern 25`
3. `tauri-conventions-and-gates.md`

### IPC Payloads, Streaming, and Request Handling

Read in this order:
1. `tauri-executable-specs-playbook.md`
2. `tauri-doctrine.md`
   - `Pattern 8`
   - `Pattern 9`
   - `Pattern 17`
   - `Pattern 18`
3. `tauri-conventions-and-gates.md`

### Lifecycle and Platform Integration

Read in this order:
1. `tauri-executable-specs-playbook.md`
2. `tauri-doctrine.md`
   - `Pattern 14`
   - `Pattern 16`
   - `Pattern 21`
   - `Pattern 23` to `Pattern 29`
3. `tauri-conventions-and-gates.md`

### Testing and Verification

Read in this order:
1. `tauri-executable-specs-playbook.md`
2. `tauri-doctrine.md`
   - `Pattern 22`
   - `TDD-First Checks For Tauri`
3. `tauri-conventions-and-gates.md`

### Review or Hardening Pass

Read in this order:
1. `tauri-doctrine.md`
   - `Chosen Patterns`
   - `Non-Negotiables`
   - `High-Confidence Anti-Patterns`
   - `Final Thesis`
2. `tauri-conventions-and-gates.md`
3. `tauri-executable-specs-playbook.md` only if requirements, traceability, or verification planning are missing

## 3) Default Read Order for Large Tauri Tasks

1. Read this file.
2. Read `tauri-executable-specs-playbook.md`.
3. Read only the relevant sections of `tauri-doctrine.md`.
4. Finish with `tauri-conventions-and-gates.md`.

## 4) Heading Search

- `rg '^##|^###' references/tauri-executable-specs-playbook.md`
- `rg '^##|^###' references/tauri-doctrine.md`
- `rg '^##|^###' references/tauri-conventions-and-gates.md`
