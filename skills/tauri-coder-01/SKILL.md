---
name: tauri-coder-01
description: Reliability-first Tauri coding guide for desktop apps in Rust with a web frontend. Use when Codex needs to implement, refactor, review, or harden Tauri 2 applications involving commands, managed state, capabilities, windows, plugins, sidecars, filesystem access, updater or tray lifecycle, deep links, single-instance handling, or desktop security and operability.
---

# Tauri Coder 01

## Overview

Apply a Tauri-first reliability and security baseline for desktop app work.
Keep this skill lean: use `references/doctrine.md` as the detailed playbook and load only the sections needed for the current task.

## Workflow

1. Classify the task before making changes.
   Common buckets: commands, shared state, capabilities and permissions, filesystem or plugin access, sidecars, IPC payload shape, desktop lifecycle, or testing.
2. Map the doctrine quickly with:
   `rg -n "^## |^### " references/doctrine.md`
3. Read the smallest relevant set of sections.
4. Apply the default rules below while matching the repo's runtime and plugin choices.
5. Verify with the repo's normal Rust, frontend, and Tauri test/build commands.
6. If a requested change weakens permissions or lifecycle safety, pause and choose the least-privilege version explicitly.

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

## Reference Map

Read these sections from `references/doctrine.md` based on the task:

- `Pattern 1: define_async_command_handler`
- `Pattern 2: manage_mutex_state_globally`
- `Pattern 3: handle_thiserror_results_serializably`
- `Pattern 15: structure_command_modules_explicitly`
  Use these for commands, state, error flow, and registration structure.
- `Pattern 4: configure_capability_permissions_minimally`
- `Pattern 5: resolve_path_scopes_safely`
- `Pattern 6: use_official_plugin_safely`
- `Pattern 20: label_window_capabilities_explicitly`
  Use these for permissions, filesystem access, plugins, and window security boundaries.
- `Pattern 8: stream_channel_progress_efficiently`
- `Pattern 9: emit_backend_events_sparingly`
- `Pattern 17: return_binary_payloads_optimally`
- `Pattern 18: inspect_raw_requests_carefully`
  Use these for IPC design, streaming, binary payloads, and request validation.
- `Pattern 11: supervise_sidecar_lifecycle_explicitly`
- `Pattern 19: scope_sidecar_permissions_exactly`
- `Pattern 25: declare_external_bins_explicitly`
  Use these for sidecars, packaging, and command/argument permissions.
- `Pattern 10: apply_csp_headers_strictly`
- `Pattern 14: configure_updater_signatures_securely`
- `Pattern 16: wire_setup_lifecycle_cleanly`
- `Pattern 21: configure_tray_menu_lifecycle`
- `Pattern 26: configure_single_instance_handoff`
- `Pattern 27: handle_deep_links_with_single_instance`
- `Pattern 28: declare_cli_contracts_explicitly`
- `Pattern 29: restore_window_state_without_flash`
  Use these for lifecycle, platform integration, and desktop-operability work.
- `High-Confidence Anti-Patterns`
- `TDD-First Checks For Tauri`
  Read these before finalizing risky command, permission, or plugin changes.

## Boundary Notes

- Treat this skill as partial guidance for plugin-author internals, mobile-only APIs, or non-Tauri desktop shells.
- If the repo uses an established permission model or plugin stack, preserve it unless it is broader than needed.
