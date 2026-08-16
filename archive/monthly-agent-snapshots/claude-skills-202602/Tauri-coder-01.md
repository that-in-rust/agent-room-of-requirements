---
name: tauri-coder-01
description: tauri-code-01
model: sonnet
color: teal
---

# Tauri Coder 01

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

pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet_user])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
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

```rust
use std::sync::Mutex;
use tauri::State;

#[derive(Default)]
struct AppState {
    counter: i32,
    user_name: Option<String>,
}

type ManagedAppState = Mutex<AppState>;

#[tauri::command]
fn increment_counter(state: State<'_, ManagedAppState>) -> Result<i32, AppError> {
    let mut state = state.lock().map_err(|_| AppError::StatePoisoned)?;
    state.counter += 1;
    Ok(state.counter)
}

pub fn run() {
    tauri::Builder::default()
        .manage(Mutex::new(AppState::default()))
        .invoke_handler(tauri::generate_handler![increment_counter])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

Rules:

- Use `std::sync::Mutex` for short synchronous access.
- Use `tauri::async_runtime::Mutex` only when the lock must live across `.await`.
- Do not wrap managed state in `Arc` before `.manage(...)`; Tauri already handles shared ownership.
- Prefer dedicated state types and aliases so command signatures stay consistent.

## Pattern 3: `handle_thiserror_results_serializably`

**Score:** `96/100`

Make every frontend-visible failure explicit and serializable.

```rust
use serde::Serialize;
use thiserror::Error;

#[derive(Debug, Error)]
enum AppError {
    #[error("state lock poisoned")]
    StatePoisoned,
    #[error("io error: {0}")]
    Io(String),
    #[error("file not found: {0}")]
    FileNotFound(String),
    #[error("permission denied: {0}")]
    PermissionDenied(String),
    #[error("invalid request: {0}")]
    InvalidRequest(&'static str),
    #[error("sidecar failed: {0}")]
    Sidecar(String),
}

impl Serialize for AppError {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        serializer.serialize_str(self.to_string().as_str())
    }
}
```

Reliability contract:

```text
WHEN a command fails
THEN it SHALL reject with a typed error
AND the error SHALL serialize cleanly for the frontend
AND the command SHALL NOT panic
```

Avoid:

- `unwrap()` in commands
- raw `String` errors everywhere
- leaking opaque backend-only error types to JS

## Pattern 4: `configure_capability_permissions_minimally`

**Score:** `98/100`

Tauri 2 reliability starts with capability discipline. The safest bug is the one the window cannot perform.

```json
{
  "identifier": "default",
  "description": "Main window capability",
  "windows": ["main"],
  "permissions": [
    "core:default",
    "dialog:allow-open",
    "fs:allow-read-text-file",
    {
      "identifier": "fs:scope",
      "allow": ["$APPDATA/*", "$DOCUMENT/MyApp/**"]
    }
  ]
}
```

Rules:

- Capability files live in `src-tauri/capabilities/`.
- Grant permissions per window, not per app by default.
- Prefer granular permissions such as `fs:allow-read-text-file` over `fs:default`.
- Scope filesystem access to exact directories and patterns.
- Sidecars need explicit shell permissions for execute or spawn.

Anti-pattern:

```json
{
  "permissions": ["fs:default", "shell:default"]
}
```

## Pattern 5: `resolve_path_scopes_safely`

**Score:** `92/100`

Treat paths as capability-bound resources, not free-form strings.

```typescript
import {
  BaseDirectory,
  exists,
  mkdir,
  readTextFile,
  writeTextFile,
} from '@tauri-apps/plugin-fs';

export async function loadSettings(): Promise<Settings> {
  const name = 'settings.json';

  if (!(await exists(name, { baseDir: BaseDirectory.AppData }))) {
    return defaultSettings;
  }

  const text = await readTextFile(name, {
    baseDir: BaseDirectory.AppData,
  });

  return JSON.parse(text) as Settings;
}

export async function saveSettings(settings: Settings): Promise<void> {
  await mkdir('.', { baseDir: BaseDirectory.AppData, recursive: true });
  await writeTextFile('settings.json', JSON.stringify(settings, null, 2), {
    baseDir: BaseDirectory.AppData,
  });
}
```

Rules:

- Prefer `BaseDirectory`-anchored access over hand-built absolute paths.
- Keep user data in app-specific directories when possible.
- Match all accessed paths in `fs:scope`.
- Assume path bugs become cross-platform bugs unless you constrain them early.

## Pattern 6: `use_official_plugin_safely`

**Score:** `89/100`

Use official plugins first, but never forget the second half of the contract: matching capability entries.

```rust
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_store::Builder::default().build())
        .plugin(tauri_plugin_fs::init())
        .plugin(tauri_plugin_shell::init())
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

Checklist:

- Register every plugin explicitly via `.plugin(...)`.
- Add the corresponding capability permissions.
- Prefer official plugins before rolling custom invoke wrappers.
- Keep plugin count intentional; every plugin expands the authority surface.

## Pattern 7: `invoke_typed_commands_frontend`

**Score:** `84/100`

Typed frontend wrappers stop IPC drift from turning into runtime bugs.

```typescript
import { invoke } from '@tauri-apps/api/core';

interface GreetResponse {
  message: string;
}

export async function greetUser(name: string): Promise<GreetResponse> {
  return invoke<GreetResponse>('greet_user', { name });
}
```

Rules:

- Never scatter raw command strings across the UI.
- Wrap `invoke` calls in typed helpers.
- Prefer generated bindings when using `specta` or similar tooling.

## Pattern 8: `stream_channel_progress_efficiently`

**Score:** `88/100`

Use channels for ordered progress streams or frequent updates. Use binary responses for large payloads.

```rust
use serde::Serialize;
use tauri::ipc::{Channel, Response};

#[derive(Clone, Serialize)]
struct DownloadProgress {
    bytes_downloaded: u64,
    total_bytes: u64,
}

#[tauri::command]
async fn download_file(
    url: String,
    on_progress: Channel<DownloadProgress>,
) -> Result<Response, AppError> {
    let bytes = reqwest::get(url)
        .await
        .map_err(|e| AppError::Sidecar(e.to_string()))?
        .bytes()
        .await
        .map_err(|e| AppError::Sidecar(e.to_string()))?;

    on_progress
        .send(DownloadProgress {
            bytes_downloaded: bytes.len() as u64,
            total_bytes: bytes.len() as u64,
        })
        .map_err(|e| AppError::Sidecar(e.to_string()))?;

    Ok(Response::new(bytes.to_vec()))
}
```

Rules:

- Events are fine for sparse notifications.
- Channels are better for high-frequency, ordered progress.
- Large binary payloads should use `tauri::ipc::Response`.
- Do not fake streaming with hundreds of tiny `invoke` calls.

## Pattern 9: `emit_backend_events_sparingly`

**Score:** `83/100`

Events are great for user-visible state changes, background completion, or window-targeted notifications.

```rust
use tauri::{AppHandle, Emitter, Manager};

fn notify_window(app: &AppHandle, label: &str, message: &str) {
    if let Some(window) = app.get_webview_window(label) {
        let _ = window.emit("notification", message);
    }
}
```

Rules:

- Always clean up listeners on unmount.
- Keep payloads small and serializable.
- Do not use events as a bulk transport layer.

## Pattern 10: `apply_csp_headers_strictly`

**Score:** `86/100`

Desktop does not mean XSS no longer matters.

```json
{
  "app": {
    "security": {
      "csp": {
        "default-src": "'self'",
        "script-src": "'self'",
        "style-src": "'self' 'unsafe-inline'",
        "img-src": "'self' data: https:",
        "connect-src": "'self' https://api.example.com",
        "frame-src": "'none'"
      },
      "dangerousDisableAssetCspModification": false
    }
  }
}
```

Rules:

- Keep `default-src` and `script-src` tight.
- Avoid remote script execution.
- Only allow outbound connections you truly need.
- Leave `dangerousDisableAssetCspModification` set to `false`.

## Pattern 11: `supervise_sidecar_lifecycle_explicitly`

**Score:** `93/100`

If your app spawns a sidecar, treat it like a subsystem, not a shell command.

```rust
use std::collections::VecDeque;
use std::sync::Mutex;
use std::time::{Duration, Instant};
use tauri::{AppHandle, Manager, State};
use tauri_plugin_shell::{
    process::{CommandChild, CommandEvent},
    ShellExt,
};

#[derive(Default)]
struct SidecarState {
    child: Mutex<Option<CommandChild>>,
    logs: Mutex<VecDeque<String>>,
}

#[tauri::command]
async fn ensure_sidecar_ready(
    app: AppHandle,
    state: State<'_, SidecarState>,
) -> Result<String, AppError> {
    let url = "http://127.0.0.1:7780".to_string();
    if check_local_health(&url).await {
        return Ok(url);
    }

    if let Some(mut child) = state
        .child
        .lock()
        .map_err(|_| AppError::StatePoisoned)?
        .take()
    {
        let _ = child.kill();
    }

    let (mut rx, child) = app
        .shell()
        .sidecar("my-sidecar")
        .map_err(|e| AppError::Sidecar(e.to_string()))?
        .args(["serve"])
        .spawn()
        .map_err(|e| AppError::Sidecar(e.to_string()))?;

    *state
        .child
        .lock()
        .map_err(|_| AppError::StatePoisoned)? = Some(child);

    tauri::async_runtime::spawn(async move {
        while let Some(event) = rx.recv().await {
            match event {
                CommandEvent::Stdout(bytes) | CommandEvent::Stderr(bytes) => {
                    let _line = String::from_utf8_lossy(&bytes);
                }
                _ => {}
            }
        }
    });

    wait_until_healthy(&url, Duration::from_secs(30)).await?;
    Ok(url)
}

async fn check_local_health(url: &str) -> bool {
    let Ok(parsed) = reqwest::Url::parse(url) else {
        return false;
    };

    let Ok(client) = reqwest::Client::builder()
        .timeout(Duration::from_secs(3))
        .no_proxy()
        .build()
    else {
        return false;
    };

    let Ok(health_url) = parsed.join("/health") else {
        return false;
    };

    client
        .get(health_url)
        .send()
        .await
        .map(|r| r.status().is_success())
        .unwrap_or(false)
}

async fn wait_until_healthy(url: &str, timeout: Duration) -> Result<(), AppError> {
    let started = Instant::now();
    while started.elapsed() < timeout {
        if check_local_health(url).await {
            return Ok(());
        }
        tokio::time::sleep(Duration::from_millis(100)).await;
    }
    Err(AppError::Sidecar("startup timed out".into()))
}
```

Sidecar rules:

- keep child handle in managed state
- kill old child before spawning a replacement
- poll health with a bounded timeout
- disable proxy use for loopback health checks
- cap sidecar logs with a ring buffer
- whitelist executable name and allowed args in capabilities

## Pattern 12: `bound_store_payload_sizes`

**Score:** `91/100`

Do not let `plugin-store` quietly become an accidental blob database.

```typescript
type PersistPolicy = {
  warnBytes: number;
  maxBytes: number;
  onOversize: 'drop' | 'truncate' | 'blobRef';
};

const policies: Record<string, PersistPolicy> = {
  promptHistory: { warnBytes: 128 * 1024, maxBytes: 256 * 1024, onOversize: 'blobRef' },
  promptDraft: { warnBytes: 64 * 1024, maxBytes: 128 * 1024, onOversize: 'blobRef' },
  terminal: { warnBytes: 64 * 1024, maxBytes: 128 * 1024, onOversize: 'truncate' },
};

function estimatePersistedBytes(value: unknown): number {
  return new TextEncoder().encode(JSON.stringify(value)).length;
}
```

Rules:

- Store small structured settings in `plugin-store`.
- Put hard byte caps on hot keys.
- Truncate or externalize oversize payloads.
- Log oversize writes before enforcing them if you need a rollout period.

## Pattern 13: `persist_blob_payloads_outofband`

**Score:** `90/100`

Binary payloads and giant base64 strings belong in files, not key-value storage.

```text
Small JSON state -> plugin-store
Large binary payloads -> app data files
Persisted state -> blob reference only
Hydration -> lazy, only when needed
```

Good design:

- image/file metadata lives in store
- blob bytes live under app data
- state stores `blob_id`, not base64
- hydration happens on demand
- cleanup is TTL-based or reference-scan based

This pattern came through strongly in the OpenCode desktop notes and is one of the easiest wins for Tauri apps that accumulate screenshots, chat attachments, or terminal snapshots.

## Pattern 14: `configure_updater_signatures_securely`

**Score:** `85/100`

Updater reliability is really trust-chain reliability.

```json
{
  "plugins": {
    "updater": {
      "pubkey": "YOUR_PUBLIC_KEY",
      "endpoints": [
        "https://releases.example.com/{{target}}/{{arch}}/{{current_version}}"
      ]
    }
  }
}
```

Rules:

- Sign updates.
- Embed only the public key.
- Never commit the private signing key.
- Surface download progress through a channel or explicit progress callback.
- On Windows, account for quit-and-install behavior.

## Pattern 15: `structure_command_modules_explicitly`

**Score:** `87/100`

Tauri command rules are subtle enough that LLMs often get them wrong unless the reference is explicit.

```rust
// src-tauri/src/commands/files.rs
#[tauri::command]
pub async fn read_settings_file() -> Result<String, AppError> {
    std::fs::read_to_string("settings.json").map_err(|e| AppError::Io(e.to_string()))
}

// src-tauri/src/commands/windows.rs
#[tauri::command]
pub fn show_main_window(window: tauri::WebviewWindow) -> Result<(), AppError> {
    window.show().map_err(|e| AppError::Io(e.to_string()))?;
    Ok(())
}

// src-tauri/src/commands/mod.rs
pub mod files;
pub mod windows;

// src-tauri/src/lib.rs
mod commands;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            commands::files::read_settings_file,
            commands::windows::show_main_window,
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

Rules:

- Commands in `lib.rs` must not be `pub`.
- Commands in separate modules should be `pub`.
- Command names are global, not module-scoped, so they must be unique even across modules.
- `invoke_handler(...)` should be called once with a single `generate_handler![...]` list.

## Pattern 16: `wire_setup_lifecycle_cleanly`

**Score:** `89/100`

Use `.setup(...)` for app-wide startup orchestration and use `AppHandle` injection for runtime access to windows, paths, and app services.

```rust
use tauri::{AppHandle, Manager};

async fn warm_start_services(app: AppHandle) {
    if let Some(window) = app.get_webview_window("main") {
        let _ = window.emit("app-warm-started", ());
    }
}

#[tauri::command]
async fn reveal_main_window(app: AppHandle) -> Result<(), AppError> {
    if let Some(window) = app.get_webview_window("main") {
        window.show().map_err(|e| AppError::Io(e.to_string()))?;
        window.set_focus().map_err(|e| AppError::Io(e.to_string()))?;
    }
    Ok(())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let handle = app.handle().clone();
            tauri::async_runtime::spawn(async move {
                warm_start_services(handle).await;
            });
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![reveal_main_window])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

Rules:

- Put app-wide initialization in `.setup(...)`, not scattered across commands.
- Avoid heavy blocking work directly inside `.setup(...)`.
- Use `AppHandle` for path resolution, restart/update access, and cross-window orchestration.
- Key runtime window logic by stable labels, not titles.

## Pattern 17: `return_binary_payloads_optimally`

**Score:** `83/100`

JSON is the wrong transport for large binary data.

```rust
use tauri::ipc::Response;

#[tauri::command]
fn read_image_file(path: std::path::PathBuf) -> Result<Response, AppError> {
    let data = std::fs::read(path).map_err(|e| AppError::Io(e.to_string()))?;
    Ok(Response::new(data))
}
```

Rules:

- Use `tauri::ipc::Response` for file bytes, image bytes, or download payloads.
- Do not serialize large binary responses into JSON.
- Keep JSON responses for structured metadata and small payloads.

## Pattern 18: `inspect_raw_requests_carefully`

**Score:** `84/100`

When frontend code needs to send raw bytes or explicit headers, validate the request boundary instead of assuming shape.

```rust
use tauri::ipc::{InvokeBody, Request};

#[tauri::command]
fn upload_binary(request: Request) -> Result<(), AppError> {
    let InvokeBody::Raw(bytes) = request.body() else {
        return Err(AppError::InvalidRequest("raw body required"));
    };

    let Some(_authorization) = request.headers().get("Authorization") else {
        return Err(AppError::InvalidRequest("missing Authorization header"));
    };

    if bytes.is_empty() {
        return Err(AppError::InvalidRequest("empty upload body"));
    }

    Ok(())
}
```

Rules:

- Use raw requests only when the JSON command model is the wrong fit.
- Validate headers and body shape explicitly.
- Treat raw IPC handlers as privileged ingress points.

## Pattern 19: `scope_sidecar_permissions_exactly`

**Score:** `82/100`

Sidecars need capability boundaries in addition to lifecycle management.

```json
{
  "$schema": "../gen/schemas/desktop-schema.json",
  "identifier": "default",
  "windows": ["main"],
  "permissions": [
    "core:default",
    {
      "identifier": "shell:allow-spawn",
      "allow": [
        {
          "name": "binaries/my-sidecar",
          "sidecar": true,
          "args": ["serve", { "validator": "\\d+" }]
        }
      ]
    }
  ]
}
```

```rust
let (_rx, _child) = app
    .shell()
    .sidecar("my-sidecar")
    .map_err(|e| AppError::Sidecar(e.to_string()))?
    .args(["serve", "7780"])
    .spawn()
    .map_err(|e| AppError::Sidecar(e.to_string()))?;
```

Rules:

- Use `shell:allow-execute` for `execute()` and `shell:allow-spawn` for `spawn()`.
- Match the sidecar name exactly with the configured binary reference.
- Whitelist exact arguments or validators.
- Never grant broad shell authority just because the app needs one safe sidecar.

## Pattern 20: `label_window_capabilities_explicitly`

**Score:** `88/100`

In Tauri, window labels define security boundaries. Capabilities attach to labels, and overlapping capabilities merge.

```rust
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let webview_url = tauri::WebviewUrl::App("index.html".into());

            tauri::WebviewWindowBuilder::new(app, "first", webview_url.clone())
                .title("First")
                .build()?;

            tauri::WebviewWindowBuilder::new(app, "second", webview_url)
                .title("Second")
                .build()?;

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```json
{
  "identifier": "dialog",
  "windows": ["first", "second"],
  "permissions": ["dialog:allow-ask"]
}
```

Rules:

- Labels must be unique and stable.
- Capabilities attach to labels, not window titles.
- Overlapping capabilities merge, so keep high-privilege windows isolated.
- Use the `platforms` field when a capability should only exist on certain operating systems.
- Only expose window-creation ability to windows you trust with privilege.

## Pattern 21: `configure_tray_menu_lifecycle`

**Score:** `81/100`

Tray apps are common enough that the pattern should be present in the reference, but they need stable IDs and central event handling.

```rust
use tauri::{
    menu::{Menu, MenuItem},
    tray::TrayIconBuilder,
};

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let quit_item = MenuItem::with_id(app, "quit", "Quit", true, None::<&str>)?;
            let menu = Menu::with_items(app, &[&quit_item])?;

            let _tray = TrayIconBuilder::new()
                .menu(&menu)
                .menu_on_left_click(true)
                .build(app)?;

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

Rules:

- Enable the `tray-icon` feature explicitly.
- Keep menu item IDs stable and machine-readable.
- Handle tray and menu events in one obvious place.
- Tray behavior is part of app lifecycle, not a UI afterthought.

## Pattern 22: `test_mocked_tauri_boundaries`

**Score:** `88/100`

Reliable Tauri code needs two test layers: mocked frontend IPC tests and runtime-backed Rust tests. End-to-end WebDriver tests are useful, but they are not the whole story.

```typescript
import { afterEach, expect, test } from 'vitest';
import { clearMocks, mockIPC, mockWindows } from '@tauri-apps/api/mocks';
import { invoke } from '@tauri-apps/api/core';

afterEach(() => {
  clearMocks();
});

test('loads settings through IPC', async () => {
  mockWindows('main', 'settings');
  mockIPC((cmd) => {
    if (cmd === 'read_settings_file') {
      return '{"theme":"dark"}';
    }
  });

  const result = await invoke<string>('read_settings_file');
  expect(result).toContain('"theme":"dark"');
});
```

Rules:

- Call `clearMocks()` after each test.
- Use `mockIPC(...)` to validate command usage and simulate backend responses.
- Use `shouldMockEvents: true` when testing event-driven flows.
- Use `mockWindows(...)` for label-oriented frontend logic.
- Remember that Tauri’s WebDriver-based desktop end-to-end support excludes macOS desktop clients.

## High-Confidence Anti-Patterns

### 1. Blocking async commands

```rust
#[tauri::command]
async fn bad_command() -> String {
    std::thread::sleep(std::time::Duration::from_secs(5));
    "done".into()
}
```

Fix: use async APIs or `spawn_blocking`.

### 2. Borrowed async inputs

```rust
#[tauri::command]
async fn bad_command(name: &str) -> String {
    format!("hello {name}")
}
```

Fix: use `String`.

### 3. Broad filesystem permissions

```json
{ "permissions": ["fs:default"] }
```

Fix: use exact commands plus scoped directories.

### 4. Panicking command paths

```rust
#[tauri::command]
fn read_file_now() -> String {
    std::fs::read_to_string("file.txt").unwrap()
}
```

Fix: return `Result<T, AppError>`.

### 5. Double-wrapping managed state

```rust
use std::sync::{Arc, Mutex};

let state = Arc::new(Mutex::new(AppState::default()));
tauri::Builder::default().manage(state);
```

Fix: `manage(Mutex::new(...))`.

### 6. Using plugin-store as a blob sink

```text
settings.json -> fine
theme preference -> fine
base64 screenshot history -> not fine
multi-megabyte terminal scrollback -> not fine
```

Fix: externalize large payloads.

### 7. Unchecked sidecar spawning

```text
spawn process
assume it is ready
assume args are safe
assume logs stay small
```

Fix: capabilities + health check + timeout + bounded logs.

## TDD-First Checks For Tauri

Before shipping any meaningful Tauri feature, verify:

- capability file proves least privilege for every new permission
- command returns structured success and structured failure
- async command has no blocking call sites
- managed state has the right mutex type
- persisted payload size stays below explicit caps
- sidecar startup has a timeout and health endpoint
- updater keys are not in git
- listeners are cleaned up on unmount
- command names are unique across modules
- sidecar permissions whitelist the binary and args
- high-privilege windows do not accidentally inherit merged capabilities
- binary responses do not go through JSON if raw bytes are intended
- mocked frontend tests clear state between runs
- build hooks and frontend dist paths match the real toolchain
- platform-specific config overrides are intentional and minimal
- single-instance is registered first if the app uses it
- deep links are validated beyond scheme matching
- CLI access has the right plugin config and capability
- window-state restore avoids first-paint flash

## Pattern 23: `configure_build_hooks_consistently`

**Score:** `85/100`

Tauri sits at the seam between a frontend toolchain and a Rust runtime. That seam needs to be explicit in config.

```json
{
  "build": {
    "beforeDevCommand": "pnpm dev",
    "beforeBuildCommand": "pnpm build",
    "devUrl": "http://localhost:1420",
    "frontendDist": "../dist"
  }
}
```

Rules:

- Wire `beforeDevCommand` and `beforeBuildCommand` to the real frontend scripts.
- Keep `devUrl` and `frontendDist` aligned with the actual frontend toolchain.
- Treat the config as the source of truth for the build seam, not README prose.
- Commit lockfiles so frontend and Rust builds stay reproducible together.

## Pattern 24: `merge_platform_configs_deliberately`

**Score:** `84/100`

Use platform-specific Tauri config files when the OS is the source of variation.

```json
// src-tauri/tauri.conf.json
{
  "productName": "MyApp",
  "bundle": {
    "resources": ["./resources"]
  },
  "plugins": {
    "deep-link": {}
  }
}
```

```json
// src-tauri/tauri.windows.conf.json
{
  "productName": "MyApp Windows",
  "plugins": {
    "cli": {
      "description": "Windows CLI entrypoint"
    }
  }
}
```

Rules:

- Use `tauri.windows.conf.json`, `tauri.macos.conf.json`, `tauri.linux.conf.json`, and mobile variants when platform behavior diverges.
- Remember that Tauri merges platform config with the base config using JSON Merge Patch semantics.
- Prefer config-layer overrides for platform packaging, identifiers, or plugin shape before adding runtime `cfg` branches.
- Use `--config` for flavors such as beta builds instead of cloning entire config trees.

## Pattern 25: `declare_external_bins_explicitly`

**Score:** `85/100`

External binary packaging must be exact or the sidecar story falls apart at bundle time.

```json
{
  "bundle": {
    "externalBin": [
      "binaries/my-sidecar"
    ]
  }
}
```

```rust
use tauri_plugin_shell::ShellExt;

let sidecar = app
    .shell()
    .sidecar("my-sidecar")
    .map_err(|e| AppError::Sidecar(e.to_string()))?;
```

Rules:

- `bundle.externalBin` entries are resolved relative to `src-tauri/tauri.conf.json` when relative paths are used.
- Each bundled binary needs the correct `-$TARGET_TRIPLE` suffix for the target architecture.
- `shell().sidecar(...)` expects the filename alias, not the full path from `externalBin`.
- Keep sidecar naming stable across config, capability files, and runtime calls.

## Pattern 26: `configure_single_instance_handoff`

**Score:** `84/100`

Single-instance desktop apps need a deterministic second-launch handoff.

```rust
use tauri::Manager;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    let mut builder = tauri::Builder::default();

    #[cfg(desktop)]
    {
        builder = builder.plugin(tauri_plugin_single_instance::init(|app, _args, _cwd| {
            if let Some(window) = app.get_webview_window("main") {
                let _ = window.unminimize();
                let _ = window.show();
                let _ = window.set_focus();
            }
        }));
    }

    builder
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

Rules:

- Register the single-instance plugin first so other plugins cannot interfere.
- Second-launch behavior should focus or route to the existing main window.
- On desktop this is a lifecycle policy, not just a plugin toggle.
- This plugin currently has no JavaScript API, so drive it from Rust lifecycle code.

## Pattern 27: `handle_deep_links_with_single_instance`

**Score:** `84/100`

Deep links are part OS integration and part trust boundary. Treat them carefully.

```rust
use tauri_plugin_deep_link::DeepLinkExt;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    let mut builder = tauri::Builder::default();

    #[cfg(desktop)]
    {
        builder = builder.plugin(tauri_plugin_single_instance::init(|_app, argv, _cwd| {
            println!("new instance argv: {argv:?}");
        }));
    }

    builder
        .plugin(tauri_plugin_deep_link::init())
        .setup(|app| {
            #[cfg(any(windows, target_os = "linux"))]
            {
                app.deep_link().register_all()?;
            }

            if let Some(urls) = app.deep_link().get_current()? {
                println!("startup deep links: {urls:?}");
            }

            app.deep_link().on_open_url(|event| {
                println!("deep link URLs: {:?}", event.urls());
            });

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```json
{
  "plugins": {
    "deep-link": {
      "desktop": {
        "schemes": ["my-tauri-app"]
      }
    }
  }
}
```

Rules:

- When combining with deep links, register single-instance first.
- On Linux and Windows, `register_all()` is useful in development and for AppImage-style environments.
- Validate deep link format even after scheme matching; users can still pass fake-looking arguments manually.
- Runtime-registered schemes require manual argument inspection for safety.
- If the frontend listens for deep-link events, capabilities usually need `core:event:default` plus `deep-link:default`.

## Pattern 28: `declare_cli_contracts_explicitly`

**Score:** `83/100`

If the app exposes a CLI, define it in config and read it through the plugin API instead of inventing ad hoc argument parsing.

```json
{
  "plugins": {
    "cli": {
      "description": "My app CLI",
      "args": [
        {
          "short": "v",
          "name": "verbose",
          "description": "Verbosity level"
        }
      ],
      "subcommands": {
        "run": {
          "description": "Run the application",
          "args": [
            { "name": "debug", "description": "Run in debug mode" },
            { "name": "release", "description": "Run in release mode" }
          ]
        }
      }
    }
  }
}
```

```rust
use tauri_plugin_cli::CliExt;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_cli::init())
        .setup(|app| {
            if let Ok(matches) = app.cli().matches() {
                println!("{matches:?}");
            }
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```json
{
  "permissions": ["cli:default"]
}
```

Rules:

- Define root args and subcommands under `plugins.cli`.
- Use `app.cli().matches()` in Rust or `getMatches()` in JavaScript.
- Add `cli:default` capability if the frontend needs access to CLI matches.
- On Windows, production apps cannot reliably write text back to the calling console by default, so do not design critical flows around stdout output.

## Pattern 29: `restore_window_state_without_flash`

**Score:** `82/100`

Window state restoration is a first-class desktop behavior. If done poorly, users see flash, jump, and geometry drift.

```rust
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            #[cfg(desktop)]
            app.handle().plugin(tauri_plugin_window_state::Builder::default().build());

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```json
{
  "permissions": ["window-state:default"]
}
```

```typescript
import { saveWindowState, StateFlags } from '@tauri-apps/plugin-window-state';

await saveWindowState(StateFlags.ALL);
```

Rules:

- Initialize the window-state plugin on desktop targets.
- Add `window-state:default` capability when using its guest APIs.
- To avoid visual flash during restore, create the window with `visible: false` and let restoration show it.
- Use explicit save/restore when window persistence is part of workflow correctness, not just convenience.

## Final Thesis

For Tauri, reliability mostly comes from getting the boundaries right:

- Rust command boundary
- window capability boundary
- filesystem scope boundary
- sidecar process boundary
- persistence size boundary

If those boundaries are explicit, typed, and least-privilege, the rest of the app gets dramatically calmer.
