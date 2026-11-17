---
name: rust-tauri
description: Self-contained guide for building, changing, reviewing or hardening Tauri 2 desktop apps (Rust core plus web front end). Use when the repository has `src-tauri/`, a `tauri` dependency, `@tauri-apps/*` packages, `tauri.conf.json` or capability files, or when the task involves commands and `invoke`, managed state, capabilities and permissions, windows, plugins, filesystem scope, IPC channels and events, sidecars, the updater, tray, deep links, single instance, window state or packaging. Not for a front-end change that never crosses IPC, or for Rust services, CLIs and libraries with no webview.
---

# Rust for Tauri desktop apps

A Tauri application is two programs with a trust boundary between them: a webview running
front-end code, and a Rust process with the user's privileges. Most Tauri-specific defects
live at that boundary or in the desktop lifecycle, not in either half alone.

Where Tauri's security or lifecycle rules conflict with a general Rust habit, the Tauri
rule wins.

Everything here was written against Tauri 2 (capability and permission formats changed
between 1 and 2). Plugin names, permission identifiers and
configuration keys are the parts most likely to have moved: confirm each against the
versions in `Cargo.lock` and `package.json` before relying on it.

## When to use this skill

- **Use it when** the change touches the Rust side of a Tauri application, its capability or configuration files, or the front-end code that calls into Rust.
- **Signals:** a `src-tauri/` directory, `tauri` in `Cargo.toml`, `@tauri-apps/*` in `package.json`, `tauri.conf.json`, files under `capabilities/`.
- **Skip it for** styling and front-end logic that never crosses IPC, for plugin internals, and for mobile-only APIs.
- **It is complete on its own.** The Rust essentials (ownership, errors, async, tests, anti-patterns), the gate commands and the definition of done are at the end, and they apply to every task here.

## The five boundaries and the eight rules

Reliability in a Tauri application comes mostly from five boundaries being explicit, typed
and least-privilege: **the command boundary, the window capability boundary, the
filesystem scope, the sidecar process, and the size of persisted state.**

**The rules.** These target Tauri 2 application code. They do not cover plugin internals or mobile-only APIs. If unsure what to prioritise, work down the list.

1. **Front-end-to-command contracts are explicit and typed** on both sides.
2. **Every fallible command returns `Result<T, AppError>` with a serialisable error.** No `unwrap()`, `expect()` or panic in a path a user can reach.
3. **Shared mutable state lives in Tauri-managed state,** behind the narrowest lock that fits. No ad hoc globals.
4. **Capabilities are least-privilege and scoped by window label.** Filesystem, shell, plugin and updater permissions name exact paths and commands.
5. **Large, long-running or high-volume IPC uses a channel or a binary response,** not a stream of events and not a giant JSON string.
6. **Every sidecar has a supervisor:** a start-up check, a bounded wait, a restart rule, a log cap, and a declared binary per target.
7. **Updater, tray, deep links, single instance, window state and setup are correctness concerns,** tested on each platform.
8. **Command names, event names and window labels are public API.** Keep them stable, and keep registration in one place.

**The trade-offs are decided by an observable condition, not by taste:**

| Choice | Decided by |
|---|---|
| `std` mutex or async mutex | Whether the guard must be held across an await |
| Event or channel | Volume and duration of the stream |
| Store or file | Payload size |
| Mock or built-application test | Whether the behaviour can be mocked faithfully; lifecycle usually cannot |

Start on the cheap side, and move when the condition is observed. Do not shrink a volume
estimate to keep the cheap tool. A rule from the list above is fixed, not quietly excepted:
"owned inputs are optional for internal commands" is a shadow rule nobody reviewed. A
temporary exception during a migration is dated, recorded and expires.

A new command lands with its boundary test in the same change. Coverage that grows with the
IPC surface is the only kind that keeps up with it.

## How to work

### Classify the change

| The change touches | Decide first | Verify with |
|---|---|---|
| A command or event (IPC) | The typed contract: arguments, result, error shape | Rust tests of the core, a contract check both sides share, mocked-IPC front-end tests |
| Managed state | Who owns it, which lock, what crosses an await | Rust unit and concurrency tests |
| Filesystem, shell, plugin or capability scope | The narrowest permission, per window | A test that the out-of-scope call is denied |
| Sidecar or external binary | Who supervises it, how it is packaged per platform | A packaged-build check; a kill-and-restart test |
| Updater | Signing key custody, endpoint, rollback | A staged update on each platform |
| Tray, single instance, deep link, window state | The lifecycle path: cold start, already running, shutdown | Manual or automated runs on each platform |
| Front-end only, never crossing IPC | Nothing Tauri-specific | Front-end tests |

### The steps

1. **Name the boundary crossed** before anything else: which window, which command, which permission. A plan that never names a window, a permission or an IPC shape has not yet dealt with Tauri.
2. **Write requirements with a checkable outcome.** "Safer" and "more reliable" are not requirements. Do not quietly reword a vague request into a different vague one; ask.
3. **Design across four layers:** the front-end contract, the command layer, the Rust core, and the desktop permissions and lifecycle.
4. **Keep commands thin** over a core that tests without a desktop runtime. A trivial command needs no extra layer.
5. **Match each test to the boundary where the risk lives.** Passing front-end tests say nothing about the IPC contract. A permission requirement proved only by a unit test is tested in the wrong place.
6. **Run the gates and record each result:** format, lints, Rust tests, Rust build, front-end checks, Tauri build. A gate that could not run on this platform is recorded as skipped, not passed.

**Size the effort by the trust boundaries crossed, not by the diff.** A small diff that
rewrites every window's permissions is a large change. Styling that never crosses IPC needs
none of this.

**Tauri-specific failure classes to look for:**

- **A permission gap that appears only in the packaged build.** It often surfaces in the webview as a generic error. Catch it with a mocked-IPC or denied-call test before packaging.
- **Payload drift** between the front end and a command: a renamed field, a changed casing, an optional that became required.
- **An unsupervised sidecar** that dies and nothing notices.
- **A broken single-instance handoff:** the second launch's arguments or deep link never reach the first instance.
- **Behaviour that differs by platform:** paths, tray, window decorations, webview engine.

**Notes on working this way:**

- A wrong permission or an untyped payload ships inside a binary on users' machines and cannot be hot-fixed like a server. These come before general tidiness.
- Front-end code calling `window.__TAURI__` globals with no typed wrapper has skipped the contract.
- A gate command copied from another repository can run nothing and still exit zero. Confirm it did real work.
- Classify a failing gate before rerunning it. One rerun for a transient cause; repeated silent reruns hide a real failure.
- Split the work by window or capability domain when window labels, capability files, sidecars or platform differences multiply, and add a dedicated security review.

### Requirements and design

**When a request would widen permissions or weaken lifecycle safety, do not simply
comply.** Say what it weakens and propose the least-privilege version.

- Keep a repository's established permission model. Tighten it where it is broader than needed; never widen it to match an example from documentation.
- Replacing hand-written plugin bridging with an official plugin is a change to argue for, not to assume.

**Requirements name the window, the action and the bound.** Use explicit units for latency,
payload size, retries and start-up time. Keep security, lifecycle and operability as
separate requirements, not clauses of one.

| Vague | Checkable |
|---|---|
| "Add a sync feature." | A typed command validates its input, reports progress on a channel, and returns a serialisable result or a typed error. |
| "Make permissions safer." | Filesystem and plugin permissions for the `main` window are limited to the named paths and commands; a call outside them is denied. |
| "Handle start-up better." | Required state is initialised in setup without blocking the main thread; the window is interactive within the stated bound. |
| "Support tray and deep links." | Tray actions and deep links reach the primary instance, start no second set of background workers, and focus the existing window. |
| "Improve reliability." | No panic in a command or lifecycle path; errors reach the front end typed; sidecar start-up and retries are bounded. |

**Design questions, one per layer.**

| Layer | Holds | Ask |
|---|---|---|
| Front-end contract | Typed invoke arguments, results, events, channels | What exact shape may the UI rely on? |
| Command layer | `#[tauri::command]` functions, input validation, error mapping | What belongs here, and what belongs deeper? |
| Rust core | Domain logic, adapters, sidecar supervision | What must test without a desktop runtime? |
| Managed state | Shared state and its lock | What is shared, and is the lock ever held across an await? |
| Capabilities | Capability files, window labels, filesystem and plugin scope | What is the least set for these windows and these actions? |
| Lifecycle and packaging | Setup, tray, updater, single instance, deep links, bundled binaries | Who owns each background thing, and what is guaranteed per platform? |

- **Fix the invoke contract before implementing either side.** Choose the narrowest request, response or stream the UI needs.
- **Scope permissions by real window labels and concrete actions,** not by UI titles or by what a future feature might want.
- **Sidecars, updater, tray and single-instance behaviour are design decisions.** Left to the end, they become packaging surprises.

## Commands, errors and state

```rust
#[derive(Debug, thiserror::Error, Serialize)]
#[serde(tag = "kind", rename_all = "snake_case")]
pub enum AppError {
    #[error("invalid request: {field}")]
    InvalidRequest { field: String },
    #[error("not found")]
    NotFound,
    #[error("io: {message}")]
    Io { message: String },
}

impl From<std::io::Error> for AppError {
    fn from(error: std::io::Error) -> Self {
        AppError::Io { message: error.to_string() }
    }
}

#[derive(Default)]
pub struct Session {
    open_workspace: Option<PathBuf>,
}

#[tauri::command]
async fn open_workspace(
    path: String,
    session: State<'_, Mutex<Session>>,
) -> Result<WorkspaceSummary, AppError> {
    let request = OpenRequest::parse(&path)?;              // validate at the boundary
    let summary = workspace::open(&request).await?;        // the core does the work
    session.lock().unwrap_or_else(PoisonError::into_inner).open_workspace = Some(request.into_path());
    Ok(summary)
}

tauri::Builder::default()
    .manage(Mutex::new(Session::default()))
    .invoke_handler(tauri::generate_handler![open_workspace])
```

- **Anything touching disk, network or a child process is an `async` command.** A synchronous command runs on the main thread and freezes the window. Never `std::thread::sleep` in a command.
- **Async commands take owned arguments** (`String`, not `&str`). `State<'_, T>` is allowed when the command returns `Result`.
- **Do not wrap state in `Arc` before `.manage(...)`;** Tauri already shares it.
- **`std::sync::Mutex` for short synchronous access, released before any await,** as above. `tokio::sync::Mutex` only when the lock must be held across an await.
- A `State<T>` whose type was never managed fails at run time, when the command is invoked. Register state and handlers together, and cover each command with one invocation test.
- **The error is a tagged enum,** so the front end branches on `kind` and not on message text. Sources that are not serialisable are converted to a message at this boundary; log the full source in Rust.
- Everything arriving from the webview is untrusted input, even from your own front end. Validate it in the command.

**On the front end, wrap `invoke` once per command** in a typed function, and normalise
results and errors there. No string-named `invoke` calls scattered through components.

```ts
export async function openWorkspace(path: string): Promise<Result<WorkspaceSummary, AppError>> {
  try {
    return { ok: true, value: await invoke<WorkspaceSummary>("open_workspace", { path }) };
  } catch (error) {
    return { ok: false, error: toAppError(error) };
  }
}
```

- Argument names are camelCase on the JavaScript side by default and snake_case in Rust. A mismatch is a run-time "missing argument" error.

**Managed state is keyed by type.** Only one value of each concrete type can be managed, and
managing a second one of the same type does not replace the first.

```rust
struct PrimaryDb(Pool);
struct AuditDb(Pool);

app.manage(PrimaryDb(primary));
app.manage(AuditDb(audit));

#[tauri::command]
async fn audit_count(db: State<'_, AuditDb>) -> Result<u64, AppError> { /* ... */ }
```

- Wrap two values of the same type in distinct newtypes.
- **A poisoned lock is a decision, not an `unwrap`.** Either map it to an error variant, or recover the guard with `into_inner` when the state is valid after any partial update. Say which in a comment.

**An error serialised as a plain string** (`serializer.serialize_str(&self.to_string())`) is
the shortest way to satisfy Tauri, and enough for an application that only displays
messages. Once the front end must branch (retry, re-authenticate, show a field error), use
the tagged form shown earlier. Do not parse message text.

**Integers beyond 2^53 − 1 do not survive JavaScript.** A command that returns a `u64` or `i64` identifier sends it as a string.

```rust
#[derive(Serialize, Deserialize)]
pub struct Event {
    #[serde(with = "u64_as_string")]
    pub id: u64,
}

`u64_as_string` is a small serde helper module that writes the number as a string and parses it back.

### Command modules and registration

```rust
// src-tauri/src/commands/settings.rs
#[tauri::command]
pub async fn read_settings(app: AppHandle) -> Result<Settings, AppError> {
    let path = app.path().app_config_dir()?.join("settings.json");
    settings::load(&path).await
}

// src-tauri/src/lib.rs
mod commands;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            commands::settings::read_settings,
            commands::windows::show_main_window,
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

- **Call `invoke_handler` once, with one `generate_handler!` list.** A second call replaces the first, and the commands in it silently vanish.
- **Command names are global, not module-scoped.** Two modules cannot both export `save`.
- Commands in their own modules are `pub`; commands defined in `lib.rs` itself must not be.
- **Resolve paths from the application's directories, never relative to the working directory.** A packaged application's working directory is wherever it was launched from.
- **No blocking `std::fs` call in an async command.** Use async I/O or `spawn_blocking`; see "Async and blocking" below.
- The `expect` on `run` is the accepted exception to the no-panic rule: there is no application to report to yet.
- A command that takes a `WebviewWindow` or `AppHandle` gets the calling window or the application injected; the front end does not pass them.

## Capabilities, windows and permissions

**Capabilities are the security boundary.** Each capability names the windows it applies to
and the exact permissions granted.

```json
{
  "identifier": "main-window",
  "windows": ["main"],
  "permissions": [
    "core:default",
    { "identifier": "fs:allow-read-text-file", "allow": [{ "path": "$APPDATA/notes/**" }] }
  ]
}
```

- **Window labels, not titles, are what a capability matches.** A second window gets its own, smaller capability. A window that loads remote content gets none of the privileged ones.
- **Broad filesystem or shell access is a security decision,** written down with its reason. `$HOME/**` and unrestricted shell execution are almost never needed.
- **Resolve paths through the path APIs and the scope,** and re-validate in the command. The front end choosing a path does not make it allowed.
- **Prefer an official plugin with a narrow permission** over custom OS bridging. The permission scope is the safety argument; the plugin choice is not.
- Custom commands are callable from any window that can reach IPC unless restricted. Check sensitive ones against the calling window's label.
- Capability and permission formats change between major versions. Check the schema of the version in `Cargo.lock` before editing.
- **Grant per window, not per application.** Prefer a granular permission (`fs:allow-read-text-file`) over a default set (`fs:default`).
- **Never grant `fs:default` plus `shell:default` as a convenience.** Together they are close to arbitrary file access and code execution for anything running in the webview.
- **A sidecar needs its own explicit execute or spawn permission,** naming the binary and its arguments.
- The safest bug is the one the window is not permitted to perform.

### Windows and labels

**Each window has a unique, stable label, and capabilities attach to labels:**

```rust
.setup(|app| {
    WebviewWindowBuilder::new(app, "main", WebviewUrl::App("index.html".into()))
        .title("Notes")
        .build()?;
    WebviewWindowBuilder::new(app, "preview", WebviewUrl::App("preview.html".into()))
        .title("Preview")
        .build()?;
    Ok(())
})
```

```json
[
  { "identifier": "main-window", "windows": ["main"], "permissions": ["core:default", "dialog:allow-open"] },
  { "identifier": "preview-window", "windows": ["preview"], "permissions": ["core:window:allow-close"] },
  { "identifier": "desktop-only", "windows": ["main"], "platforms": ["macOS", "windows", "linux"], "permissions": ["global-shortcut:allow-register"] }
]
```

- **Capabilities that name the same window add up.** A window's real permission set is the union of every capability listing its label, including any with a wildcard. Review the union, not one file.
- **Keep a high-privilege window isolated:** its own label, its own capability, and no shared wildcard.
- **A window that renders untrusted or remote content gets the smallest set,** ideally none. Markdown previews, embedded web pages and anything showing user-supplied HTML are in this group.
- **The ability to create windows is itself a privilege.** A low-privilege window that can open a window with a privileged label has escalated. Create windows from Rust, with labels chosen there.
- **Dynamic labels** (`editor-1`, `editor-2`) need a capability pattern; make the pattern as narrow as the naming scheme.
- Use the `platforms` field for a capability that should exist only on some operating systems.
- Key all runtime window logic by label. Titles are for people and get translated.

### Plugins

**Plugins are registered explicitly, each with its matching permission:**

```rust
tauri::Builder::default()
    .plugin(tauri_plugin_store::Builder::default().build())
    .plugin(tauri_plugin_fs::init())
    .plugin(tauri_plugin_shell::init())
```

- **Every plugin widens what the application can do.** Keep the list intentional, and remove a plugin when its last use goes.
- A plugin registered in Rust with no permission in any capability fails at run time with a permission error; a permission for an unregistered plugin fails the build. Change both together.
- Keep the Rust crate and the JavaScript package of a plugin on matching versions.

## IPC volume: channels, bytes and events

| Need | Use | Avoid |
|---|---|---|
| One request, one small result | A command returning JSON | |
| Progress or a sustained stream for one call | `tauri::ipc::Channel<T>` passed as a command argument | Global events at high frequency |
| Sparse notifications to any listener | Events | Events as a data stream |
| Bytes (images, files) | `tauri::ipc::Response`, or a custom protocol | Base64 or number arrays inside JSON |

```rust
#[derive(Clone, Serialize)]
#[serde(tag = "event", rename_all = "snake_case")]
enum SyncEvent {
    Progress { done: u64, total: u64 },
    Finished,
}

#[tauri::command]
async fn sync_workspace(on_event: Channel<SyncEvent>) -> Result<(), AppError> {
    for (done, total) in sync::run().await? {
        let _ = on_event.send(SyncEvent::Progress { done, total }); // the window may be gone
    }
    let _ = on_event.send(SyncEvent::Finished);
    Ok(())
}
```

- **Throttle progress.** A message per item floods the webview; send at a fixed interval or on a percentage change.
- **A long-running command needs a way to stop:** a cancel command with a token, and cancellation when the window closes.
- Listeners registered on the front end are removed on unmount, or they accumulate across navigations.

### A download with progress

**A download reports progress on a channel as chunks arrive, and returns bytes as a binary
response:**

```rust
#[derive(Clone, Serialize)]
struct DownloadProgress {
    received: u64,
    total: Option<u64>,
}

#[tauri::command]
async fn download_asset(
    asset: AssetId,                               // an identifier, not a URL
    on_progress: Channel<DownloadProgress>,
    state: State<'_, AppState>,
) -> Result<Response, AppError> {
    let mut response = state.http.get(state.catalog.url_for(&asset)?).send().await?.error_for_status()?;
    let total = response.content_length();
    let mut bytes = Vec::new();
    while let Some(chunk) = response.chunk().await? {
        if bytes.len() + chunk.len() > MAX_ASSET_BYTES {
            return Err(AppError::TooLarge);
        }
        bytes.extend_from_slice(&chunk);
        let _ = on_progress.send(DownloadProgress { received: bytes.len() as u64, total });
    }
    Ok(Response::new(bytes))
}
```

- **Report progress while the work happens.** Downloading the whole body and then sending one progress message at 100% is not progress.
- **The front end names what to fetch; Rust decides the URL.** A command that fetches any URL the webview supplies is a request-forgery proxy with the user's network position. If arbitrary URLs are the feature, apply the URL rules under "Security at the edges" below.
- **Bound the size,** and for anything large write to a file and return its path, not the bytes.
- **Map errors to the right variant.** Reusing an unrelated variant (a network failure reported as a sidecar failure) defeats the typed error.
- Do not imitate streaming with hundreds of small `invoke` calls.

### Events

**An event aimed at one window:**

```rust
fn notify_window(app: &AppHandle, label: &str, notice: &Notice) {
    if let Some(window) = app.get_webview_window(label) {
        let _ = window.emit_to(label, "notice", notice);
    }
}
```

- **Use events for state changes that any listener may care about:** a background job finished, settings changed, a window-targeted notice. Keep payloads small.
- **A global `emit` reaches every window,** including ones with fewer privileges. Target the window when the payload is not for all of them.
- Do not put secrets in event payloads.
- An event emitted before the front end has registered its listener is lost. For state the window needs on load, expose a command it can call, and use the event only for later changes.

### Bytes and raw requests

**Reading bytes for the front end:**

```rust
#[tauri::command]
async fn read_attachment(id: AttachmentId, state: State<'_, AppState>) -> Result<Response, AppError> {
    let path = state.attachments.path_for(&id)?;     // looked up, never supplied
    Ok(Response::new(tokio::fs::read(path).await?))
}
```

- **A command that reads whatever path the webview sends is an arbitrary-file-read primitive** for any script that runs there. Accept an identifier and resolve it in Rust, or check the path against an allowed base with `resolve_inside` (under "Files, paths and persisted state").
- Use a binary response for file, image and download bytes. Keep JSON for structured metadata.
- For media the webview displays directly, the asset protocol with a narrow scope avoids copying bytes through IPC at all.

**A raw request is a privileged entry point.** Use it only when a typed JSON argument will
not do, such as an upload body.

```rust
#[tauri::command]
async fn upload_attachment(request: Request<'_>, state: State<'_, AppState>) -> Result<AttachmentId, AppError> {
    let InvokeBody::Raw(bytes) = request.body() else {
        return Err(AppError::InvalidRequest { field: "body".into() });
    };
    if bytes.is_empty() || bytes.len() > MAX_UPLOAD_BYTES {
        return Err(AppError::InvalidRequest { field: "body".into() });
    }
    let kind = request.headers().get("x-attachment-kind").and_then(|v| v.to_str().ok());
    let kind = AttachmentKind::parse(kind)?;
    state.attachments.store(kind, bytes).await
}
```

- **Validate the body kind, its size, and every header you read.** Parse headers into types.
- **Checking that a header is present is not a check.** A header set by your own front end authenticates nothing; authorisation comes from the calling window and the application's own session state.
- Sniff or verify content you will later interpret (an image, an archive); do not trust a declared type.

## Files, paths and persisted state

- **The store plugin holds small structured settings.** Large or binary data goes in files under the application data directory, with metadata in the store or a database.
- **Write files atomically** (temporary file, then rename), since a desktop application can be killed at any time.

**File access from the front end is anchored to a base directory:**

```typescript
import { BaseDirectory, exists, mkdir, readTextFile, writeTextFile } from "@tauri-apps/plugin-fs";

const options = { baseDir: BaseDirectory.AppData };

export async function loadSettings(): Promise<Settings> {
  if (!(await exists("settings.json", options))) {
    return defaultSettings;                    // first run: nothing saved yet
  }
  try {
    return parseSettings(JSON.parse(await readTextFile("settings.json", options)));
  } catch (error) {
    reportSettingsProblem(error);              // corrupt, or written by another version
    return defaultSettings;
  }
}

export async function saveSettings(settings: Settings): Promise<void> {
  await mkdir("", { ...options, recursive: true });
  await writeTextFile("settings.json", JSON.stringify(settings, null, 2), options);
}
```

- **A corrupt file is not an empty one.** Missing means first run. Unreadable is reported to the user, and the bad file is kept or moved aside, so the next save does not destroy what could be recovered.
- **Paths are capability-bound resources, not free-form strings.** Prefer `BaseDirectory`-anchored access to hand-built absolute paths, and keep user data in the application's own directories.
- **Every path accessed must fall inside the declared scope.** A path that works in development and is denied when packaged usually means the scope was never checked.
- **Validate what you read back.** `JSON.parse(text) as Settings` is a cast, not a check; a file from an older version or a partial write passes it. Parse through a schema, and fall back or migrate.
- **This write is not atomic.** For data that must survive a crash mid-write, do the write in a Rust command with a temporary file and a rename.
- **Choose one side to own each file.** If both the front end and a Rust command write `settings.json`, they will overwrite each other.
- Path separators, case sensitivity and reserved names differ by platform. Constrain paths early, and test on each platform you ship.

**The atomic write, in Rust:**

```rust
fn save_atomically(content: &str, target: &Path) -> io::Result<()> {
    let dir = target.parent().unwrap_or(Path::new("."));
    let mut file = tempfile::NamedTempFile::new_in(dir)?;
    file.write_all(content.as_bytes())?;
    file.as_file().sync_all()?;
    file.persist(target).map_err(|e| e.error)?;
    Ok(())
}

- On Unix the temporary file is created readable by the owner only, and keeps that mode after `persist`. Set permissions explicitly if others must read it.

### Paths that come from the webview or the user

**Paths from input.** Canonicalise, then require the result to lie inside the allowed base.

```rust
fn resolve_inside(base: &Path, requested: &Path) -> Result<PathBuf, PathError> {
    let base = base.canonicalize()?;
    let candidate = base.join(requested).canonicalize()?;
    if candidate.starts_with(&base) {
        Ok(candidate)
    } else {
        Err(PathError::OutsideBase)
    }
}
```

- `canonicalize` requires the path to exist. For a file about to be created, canonicalise the parent and validate the file name separately.
- Compare with `Path::starts_with`, which works on whole components. A string prefix test accepts `/data-evil` for base `/data`.
- A check followed by a later open can be raced by a symlink swap. Where that matters, open relative to a directory handle (`cap-std`, `openat`) and do not re-resolve.

### Size budgets for persisted state

**Persisted keys have byte budgets.** A settings store is read and written whole, so one
growing key (history, a terminal buffer, a draft with a pasted image) slows every start and
every save.

```typescript
type PersistPolicy = {
  warnBytes: number;
  maxBytes: number;
  onOversize: "drop" | "truncate" | "blobRef";
};

const policies: Record<string, PersistPolicy> = {
  promptHistory: { warnBytes: 128 * 1024, maxBytes: 256 * 1024, onOversize: "blobRef" },
  terminal: { warnBytes: 64 * 1024, maxBytes: 128 * 1024, onOversize: "truncate" },
};

const persistedBytes = (value: unknown) => new TextEncoder().encode(JSON.stringify(value)).length;
```

- **Each hot key gets a hard cap and a stated action when over it:** drop, truncate, or move the bytes out and keep a reference.
- **When introducing a cap on existing data, log oversize writes for a release before enforcing,** so real sizes are known.
- **Large bytes live in files under the application data directory; state holds a `blob_id`, never base64.** Load a blob only when it is displayed.
- **Blobs need garbage collection:** by age, or by scanning for references. Write the blob before the reference and delete the reference before the blob, so a crash leaves an orphan file, not a dangling reference.
- This matters most for applications that accumulate screenshots, attachments or terminal snapshots.
- Debounce saves. Writing the store on every keystroke is the usual cause of input lag.

## Security at the edges

### Content security policy

```json
{
  "app": {
    "security": {
      "csp": {
        "default-src": "'self'",
        "script-src": "'self'",
        "style-src": "'self' 'unsafe-inline'",
        "img-src": "'self' data:",
        "connect-src": "'self' https://api.example.com",
        "frame-src": "'none'"
      }
    }
  }
}
```

- **`script-src` stays `'self'`.** A remote or inline script in a window with IPC access can call every command that window is permitted.
- **`connect-src` lists the hosts the application talks to.** A wildcard there lets injected content send data anywhere.
- `'unsafe-inline'` for styles is a common concession to UI libraries and a much smaller risk than for scripts; remove it if the libraries allow.
- `img-src https:` allows any remote image, which leaks requests to third parties. Add it only when the application displays arbitrary remote images.
- Leave `dangerousDisableAssetCspModification` off. Any option whose name starts with `dangerous` needs a written reason.
- A policy too strict for the dev server is fixed with a dev-only override, not by loosening the shipped one.

### A command that fetches a URL

Prefer the design where the front end names a thing and Rust decides the URL. When
fetching a user-supplied URL is the feature, one `validate_url` runs before every fetch.

- Allow only `http` and `https`. Reject loopback, private, link-local and cloud-metadata addresses, and internal hostnames.
- **Checking the hostname is not enough.** Resolve it, check the address, and connect to the address you checked, so a second DNS answer cannot differ.
- Validate every redirect the same way, or disable redirects. Cap the response size and set a timeout.
- Test IPv4, IPv6, IPv4-mapped IPv6 (`::ffff:127.0.0.1`), and decimal or octal spellings of an address.
- An intranet exception is an explicit allow-list, not a weaker default.

### Running other programs from Rust

- **Use `Command` with a program and separate arguments. No shell.** Arguments passed this way are not re-parsed, which removes injection at its source.
- An argument beginning with `-` can still be read as an option. Put `--` before data-derived positional arguments where the program supports it.
- **Do not pass credentials as arguments;** they appear in process listings. Use the environment, standard input or a file with restricted permissions.
- Success is the exit status or structured output, not a phrase in the text. A failed write to the child's standard input is an error.
- If shell text must be accepted, parsing it against an allow-list of programs and rejecting redirects and subshells lowers the risk. It does not make arbitrary shell text safe; say so.
- A run-to-completion child needs a timeout, both output pipes drained while waiting, a cap on captured output, and a kill followed by a wait at the deadline. A long-lived child is a sidecar and gets a supervisor.

### Logs and secrets

**Desktop logs live on the user's machine and cannot be recalled.**

- **Check logging by absence:** read the output of the release configuration for tokens, payloads, file contents and personal paths. Debug builds log more than what ships.
- Log-everything-and-filter-later is a server habit. It does not fit here.
- Cap logs at the source, by size and count. Nobody rotates them on a user's disk.
- **`#[instrument]` records every argument with `Debug` unless told otherwise.** Skip bodies, credentials and large values, and name the fields you want. An un-skipped request or config struct is the usual way a secret reaches a log.

- Deep links, launch arguments and sign-in callbacks are covered under "Lifecycle". Updater key custody is under "Build, packaging and updates".

## Sidecars

Treat a sidecar as a subsystem with an owner, not as a shell command.

```rust
pub struct SidecarSupervisor {
    running: tokio::sync::Mutex<Option<Running>>,   // held across the whole start: single flight
    logs: Arc<Mutex<VecDeque<String>>>,
    http: reqwest::Client,                          // built once: short timeout, no proxy
}

struct Running {
    child: CommandChild,
    endpoint: Endpoint,                             // loopback URL plus a per-launch token
}

impl SidecarSupervisor {
    pub async fn ensure_ready(&self, app: &AppHandle) -> Result<Endpoint, AppError> {
        let mut running = self.running.lock().await;
        if let Some(current) = running.as_ref() {
            if self.is_healthy(&current.endpoint).await {
                return Ok(current.endpoint.clone());
            }
        }
        if let Some(stale) = running.take() {
            let _ = stale.child.kill();
        }

        let endpoint = Endpoint::allocate()?;       // free loopback port, fresh random token
        let (mut events, child) = app
            .shell()
            .sidecar("indexer")?
            .args(["serve", "--port", &endpoint.port().to_string()])
            .env("INDEXER_TOKEN", endpoint.token())
            .spawn()?;

        let logs = Arc::clone(&self.logs);
        let (exited_tx, mut exited) = tokio::sync::oneshot::channel();
        tauri::async_runtime::spawn(async move {
            while let Some(event) = events.recv().await {
                match event {
                    CommandEvent::Stdout(line) | CommandEvent::Stderr(line) => {
                        push_capped(&logs, String::from_utf8_lossy(&line).into_owned());
                    }
                    CommandEvent::Terminated(status) => {
                        let _ = exited_tx.send(status.code);
                        break;
                    }
                    _ => {}
                }
            }
        });

        let deadline = tokio::time::Instant::now() + STARTUP_TIMEOUT;
        loop {
            if self.is_healthy(&endpoint).await {
                *running = Some(Running { child, endpoint: endpoint.clone() });
                return Ok(endpoint);
            }
            if let Ok(code) = exited.try_recv() {
                return Err(AppError::SidecarExited { code });
            }
            if tokio::time::Instant::now() >= deadline {
                let _ = child.kill();
                return Err(AppError::SidecarStartTimeout);
            }
            tokio::time::sleep(Duration::from_millis(100)).await;
        }
    }
}
```

What the example is doing, and why:

- **One owner holds the child handle,** in managed state. Nothing else spawns the binary.
- **Starting is single-flight.** Two windows calling `ensure_ready` together must not spawn two children; the async mutex is held across the start on purpose, which is the legitimate case for one.
- **The old child is killed before a replacement starts,** and a child that never became healthy is killed too, not abandoned.
- **Start-up has a deadline, and an early exit ends the wait at once.** Waiting thirty seconds for a process that died in the first is a poor failure.
- **Logs go into a ring buffer with a cap.** Collecting them and discarding them, or keeping all of them, are both wrong.
- **The health client disables proxies and has a short timeout.** A system proxy must not intercept a loopback request.
- **The capability names the executable and its allowed arguments.**

What to decide beyond it:

- **A fixed port is a liability.** It collides with another program, and a health check on it will accept whatever is listening. Allocate a port per launch.
- **A loopback HTTP server is reachable by every local process and, without care, by web pages in a browser.** Require a per-launch token on every request, bind to `127.0.0.1` only, and reject unexpected `Origin` and `Host` headers.
- **State the restart rule:** restart on unexpected exit, with backoff, at most N times in a window, then surface a persistent error. An unbounded restart loop hides a crash.
- **Kill the child when the application exits,** in the exit handler. An orphaned sidecar holds its port and files, and blocks the next launch or an update.
- Where the child must die even if the parent is killed, use an operating-system mechanism: a job object on Windows, a parent-death signal on Linux, or have the child watch its stdin close.
- If stdio is enough, prefer it to HTTP: there is no port, and nothing else can connect.

### Permission scope for a sidecar

```json
{
  "identifier": "main-window",
  "windows": ["main"],
  "permissions": [
    "core:default",
    {
      "identifier": "shell:allow-spawn",
      "allow": [
        { "name": "binaries/indexer", "sidecar": true, "args": ["serve", "--port", { "validator": "\\d{1,5}" }] }
      ]
    }
  ]
}
```

- **Capabilities restrict what the webview may invoke.** Rust code in the application is not restricted by them. If only Rust starts the sidecar, as in the supervisor above, give the webview no shell permission at all. That is the safer design.
- **If the front end must start it:** `shell:allow-spawn` for `spawn()`, `shell:allow-execute` for `execute()`, the name matching the configured binary exactly, and arguments listed literally or by a tight validator.
- **A validator is a pattern for one whole argument.** `.*` or a pattern that admits a leading `-` lets the caller inject options.
- **Never grant broad shell access because the application needs one safe sidecar.**
- The binary is declared in the bundle configuration (`externalBin`) and exists on disk once per target, with the target triple as a suffix. A missing triple fails only when building for that platform.

### Declaring and shipping the binary

```json
{ "bundle": { "externalBin": ["binaries/indexer"] } }
```

- **The path is relative to the Tauri configuration file,** and each binary exists on disk with a `-<target-triple>` suffix, for example `binaries/indexer-aarch64-apple-darwin`.
- **`shell().sidecar("indexer")` takes the file name alone,** not the path from `externalBin`.
- **One name, three places:** the bundle configuration, the capability file and the runtime call. Rename all together.
- **Build the sidecar in CI for every target you ship,** in the same pipeline. A binary copied in by hand is the one that is stale or built for the wrong architecture.
- **A bundled binary is part of your release:** it is signed and notarised with the application where the platform requires it, and its licence and vulnerabilities are yours.
- Read-only resources go in `bundle.resources` and are located through the path API at run time. The installation directory is not writable; anything the application modifies is copied to the data directory first.

## Lifecycle

### Setup

**Setup registers state, then starts background work without waiting for it:**

```rust
tauri::Builder::default()
    .setup(|app| {
        let settings = Settings::load(&app.path().app_config_dir()?)?;   // small and required
        app.manage(AppState::new(settings));
        let handle = app.handle().clone();
        tauri::async_runtime::spawn(async move {
            match services::warm_start(&handle).await {
                Ok(()) => handle.state::<AppState>().mark_ready(),
                Err(error) => handle.state::<AppState>().mark_degraded(error),
            }
            let _ = handle.emit("startup-state-changed", ());
        });
        Ok(())
    })
```

- **Application-wide initialisation belongs in `.setup(...)`,** not scattered across the first command that happens to need it.
- **Nothing slow runs inline in setup.** It runs before the event loop, so the window does not appear until it returns.
- **Readiness is state the front end can query,** plus an event when it changes. An event alone is lost if it fires before the window has registered its listener.
- **A background start-up failure is recorded and shown,** not swallowed by the spawned task.
- Use `AppHandle` for path resolution, window lookup by label, and restart or update access. Clone it into tasks; do not hold window references across awaits.
- **The setup hook returns `Result`, and an error aborts start-up.** Decide which failures deserve that; the rest become a degraded state the window can show.

### Deep links and single instance

A deep link can arrive three ways: as the launch argument of a cold start, as the argument
of a second launch that the single-instance plugin hands over, or as an event while the
application runs. **All three go through one parser and one router.**

```rust
pub fn run() {
    let mut builder = tauri::Builder::default();

    #[cfg(desktop)]
    {
        // First, so no other plugin starts work in a process that is about to exit.
        builder = builder.plugin(tauri_plugin_single_instance::init(|app, args, _cwd| {
            window::reveal_main(app);
            links::route_all(app, args.iter().skip(1).map(String::as_str));
        }));
    }

    builder
        .plugin(tauri_plugin_deep_link::init())
        .setup(|app| {
            #[cfg(any(windows, target_os = "linux"))]
            app.deep_link().register_all()?;                 // development and unpackaged runs

            if let Some(urls) = app.deep_link().get_current()? {
                links::route_all(app.handle(), urls.iter().map(|url| url.as_str()));
            }
            let handle = app.handle().clone();
            app.deep_link().on_open_url(move |event| {
                links::route_all(&handle, event.urls().iter().map(|url| url.as_str()));
            });
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}

// links.rs
pub enum LinkAction {
    OpenNote(NoteId),
    CompleteSignIn { state: OAuthState, code: AuthCode },
}

pub fn parse(raw: &str) -> Result<LinkAction, LinkError> {
    let url = Url::parse(raw)?;
    if url.scheme() != "notes-app" {
        return Err(LinkError::WrongScheme);
    }
    match (url.host_str(), url.path()) {
        (Some("note"), path) => Ok(LinkAction::OpenNote(path.trim_start_matches('/').parse()?)),
        (Some("auth"), "/callback") => parse_sign_in(&url),
        _ => Err(LinkError::UnknownAction),
    }
}
```

```json
{ "plugins": { "deep-link": { "desktop": { "schemes": ["notes-app"] } } } }
```

- **Register single-instance first.** It has no JavaScript interface; drive it from Rust.
- **Parse every link into a closed set of typed actions.** Reject the rest and log it. Never pass a link's text to a shell, a file path, a navigation or an `eval`.
- **Matching the scheme proves nothing about the sender.** Any web page, e-mail or local program can open `notes-app://...`, and a user can type one as a launch argument.
- **A link may navigate; it may not act.** Opening a note is fine. Deleting, sending, paying or changing settings needs a confirmation the user sees inside the application.
- **A sign-in callback is checked against a pending request:** the `state` value the application generated, unexpired, used once. An unsolicited callback is dropped.
- **Second-launch arguments are filtered:** only arguments that parse as a link (or as your launch options) are routed. The rest are ignored.
- A link that arrives before the window or the session is ready is queued in state and handled when ready, not dropped and not handled twice.
- Runtime registration (`register_all`) is for development, AppImage-style runs and portable builds. Installed applications get the scheme from the bundle; on macOS it comes from the bundle only, so it works only in a built application.
- If the front end listens for the link event itself, its capability needs the event and deep-link permissions. Routing in Rust and sending the front end a typed action keeps the parser in one place.
- Another application can register the same scheme. Do not send secrets through a custom scheme without a binding such as PKCE.

### Launch arguments

**Declare launch arguments in the CLI plugin's configuration and read them through it:**

```json
{
  "plugins": {
    "cli": {
      "description": "Notes",
      "args": [{ "name": "verbose", "short": "v", "description": "Verbose logging" }],
      "subcommands": {
        "open": {
          "description": "Open a note",
          "args": [{ "name": "path", "index": 1, "takesValue": true }]
        }
      }
    }
  }
}
```

```rust
.plugin(tauri_plugin_cli::init())
.setup(|app| {
    match app.cli().matches() {
        Ok(matches) => launch::apply(app.handle(), LaunchOptions::from_matches(&matches)?),
        Err(error) => tracing::warn!(%error, "ignoring unparseable launch arguments"),
    }
    Ok(())
})
```

- **One declared argument surface, one conversion into a typed `LaunchOptions`.** No second hand-written parser for the same arguments.
- **The single-instance handler receives raw arguments,** not plugin matches. Route them into the same `LaunchOptions` conversion so a second launch means what a first one does.
- **Decide what bad arguments do.** A desktop application launched from an icon has no console to print usage to; ignoring with a log entry is usually right, while a headless subcommand should exit non-zero.
- **On Windows a packaged GUI application cannot reliably write to the calling console.** Do not build a flow that depends on its stdout. Offer a separate console binary if scripting matters.
- A path given as an argument is relative to the launching directory, which on handoff is the *second* process's. Resolve it against the working directory the handler is given.
- The front end reads matches only with the plugin's permission in its capability. Prefer applying them in Rust.

### Tray and menus

**Tray and menu events are handled in one place, by stable identifier:**

```rust
.setup(|app| {
    let show = MenuItem::with_id(app, "show", "Show window", true, None::<&str>)?;
    let quit = MenuItem::with_id(app, "quit", "Quit", true, None::<&str>)?;
    let menu = Menu::with_items(app, &[&show, &quit])?;

    TrayIconBuilder::with_id("main-tray")
        .icon(app.default_window_icon().cloned().ok_or("missing application icon")?)
        .menu(&menu)
        .on_menu_event(|app, event| match event.id().as_ref() {
            "show" => window::reveal_main(app),
            "quit" => lifecycle::request_quit(app),
            other => tracing::warn!(id = other, "unhandled tray menu item"),
        })
        .build(app)?;
    Ok(())
})
```

- **Menu item identifiers are stable and machine-readable;** labels are display text.
- **Quit goes through one function** that stops sidecars and flushes state, whether it came from the tray, a menu, a shortcut or the last window closing.
- The tray needs the `tray-icon` feature enabled on the `tauri` crate.
- Build the tray once. Rebuilding it on every state change leaves duplicate icons on some platforms; update the existing menu items.
- Tray behaviour differs by platform: left click, right click and whether a tray exists at all (some Linux desktops have none). Never make the tray the only way to reach a function.
- **Closing the last window either quits or hides to the tray.** Decide which, per platform, and keep quitting reachable.

### Window state

```rust
#[cfg(desktop)]
app.handle().plugin(tauri_plugin_window_state::Builder::default().build())?;
```

- **Create the window with `visible: false` and show it after restoration,** to avoid a flash at the default size.
- **The plugin saves on close.** Where layout is part of the work (a multi-window workspace), save explicitly at meaningful moments too, since a crash or forced quit skips the close.
- A restored position may be on a display that is no longer attached. Verify the window is visible on some monitor, and fall back to centred.
- Decide which properties are restored. Restoring "maximised" and "fullscreen" is usually wanted; restoring "hidden" is how a window becomes unreachable.

### Exit

- **On exit, stop what you started:** sidecars, background tasks, file watchers. Flush state before the process ends, since exit does not wait for detached work.
- Every route to quitting (tray, menu, shortcut, last window closed) calls the same function.

## Async and blocking on the Rust side

- **Never block the runtime.** No blocking I/O, `std::thread::sleep`, long CPU work or blocking lock inside an async command or task.
- **Never hold a `std` lock guard across `.await`.** Copy out what you need and drop the guard. Use `tokio::sync::Mutex` only where the guard must span an await, as in the sidecar start above.
- **Every spawned task has an owner** that can stop it and learns how it ended. A failure inside a detached task is otherwise invisible.
- **Everything is bounded:** channels, retries, waits, log buffers, payload sizes.

The table of where blocking work runs, cancellation safety and task ownership are in the Rust essentials below.

**Performance is gated by structure before any benchmark.** Each structural rule bounds the
load on one shared resource: the runtime (no blocking in async commands), the IPC channel
(channels and binary responses for volume), the store (small structured state only), the
start-up path (bounded setup and sidecar waits). For a new case, ask which shared resource
the change loads without a bound.

- **A benchmark at test volume passes designs that collapse at user volume.** An event per row is fine for a hundred rows and freezes the window at a million.
- **`spawn_blocking` keeps the runtime responsive; it does not make the work faster.** An async command that runs for a minute still needs progress and cancellation. Responsiveness and completion time are separate budgets.
- **Choose the lane for each payload at design time.** An export keeps metadata in the store, sends progress on a channel, and hands the archive over as a file path.
- **A fixed sleep is not a bounded wait.** A bound is a deadline on a polled readiness condition.

**No operator watches a user's machine.** The application supervises its own children:
sidecars, setup tasks and update flows.

## Build, packaging and updates

### The build seam

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

- **The hooks call the real front-end scripts,** and `devUrl` and `frontendDist` match what the front-end tool serves and emits. A port that is not fixed on the front-end side breaks `devUrl` when it is taken.
- **The configuration is the source of truth for how the application is built,** not the README.
- **Commit both lock files,** so the Rust and front-end halves reproduce together. Keep the `@tauri-apps/*` packages and the `tauri*` crates on matching minor versions.
- The dev server is plain HTTP on localhost and behaves differently from the packaged protocol: different origin, different CSP effects, different path resolution. A feature is not verified until it has run in a built application.

### Platform differences

**Platform differences go in platform configuration files first:**

- `tauri.windows.conf.json`, `tauri.macos.conf.json`, `tauri.linux.conf.json` and the mobile variants are merged over the base file. The merge follows JSON Merge Patch: objects merge key by key, **arrays are replaced whole**, and `null` removes a key.
- Use them for packaging, identifiers, bundle resources and plugin shape before reaching for runtime `cfg` branches.
- Use `--config` with a small overlay for a flavour such as a beta build. Do not copy the whole configuration tree.
- A beta that can be installed beside the stable release needs its own identifier, or the two share data directories and updater state.

### Updater

```json
{
  "plugins": {
    "updater": {
      "pubkey": "<public key>",
      "endpoints": ["https://releases.example.com/{{target}}/{{arch}}/{{current_version}}"]
    }
  }
}
```

- **Updates are signed; only the public key is in the repository.** The private key and its password live in the CI secret store and are never echoed. Losing the key means shipped installations cannot update; leaking it means anyone can update them.
- **Endpoints are HTTPS.** The signature protects the artefact; transport security protects the metadata and the user's privacy.
- **Check for updates off the start-up path,** and treat a failed check as a non-event for the user.
- **Show download progress, and ask before restarting.** On Windows the installer quits the application; save state first.
- **Test the update from the previous released version,** not only a fresh install. The updater that runs is the old one.
- Decide whether a downgrade is allowed, and whether a bad release can be withdrawn by the endpoint.
- Migrations of local data run on first launch after an update and must tolerate being interrupted.

## Tests and gates

**What each kind of test can show.**

| Test | Shows | Cannot show |
|---|---|---|
| Rust unit | Core logic is correct | Anything about IPC or permissions |
| Rust integration | Commands, adapters and serialisation agree | Front-end expectations |
| Front-end test with mocked IPC | The UI handles each result and error | That the real command returns that shape |
| Shared contract check (generated bindings, or one fixture both sides parse) | The two sides agree on the payload | Behaviour |
| Mocked runtime test (`tauri::test`) | A command runs with state and a mock app handle | Real windows, permissions as packaged |
| Packaged-build run on each platform | Capabilities, sidecars, tray, deep links, updater | Nothing quickly: keep these few |
| Performance | A stated latency or payload bound | Anything, if no bound was stated |

- **Generated bindings remove payload drift at its source.** Tools such as `tauri-specta` or `ts-rs` derive the TypeScript types from the Rust ones. Without them, keep one fixture that both a Rust test and a front-end test parse.

### Test examples

Write one test per requirement, and name it after the behaviour.

**The command's core, with no runtime:**

```rust
#[tokio::test]
async fn sync_rejects_an_empty_workspace_path() {
    let result = sync_workspace(&test_state(), SyncRequest { path: String::new() }).await;
    assert!(matches!(result, Err(AppError::InvalidRequest { .. })));
}

#[test]
fn app_error_serialises_to_the_shape_the_front_end_expects() {
    let json = serde_json::to_value(AppError::InvalidRequest { field: "path".into() }).unwrap();
    assert_eq!(json, serde_json::json!({ "kind": "invalid_request", "field": "path" }));
}
```

The second test pins the error's wire shape. That shape is a contract with the front end,
and a serde attribute change would otherwise break it silently.

**The front end, with IPC mocked:**

```ts
import { mockIPC, clearMocks } from "@tauri-apps/api/mocks";

afterEach(() => clearMocks());

it("shows a recoverable error when the sync command is denied", async () => {
  mockIPC((cmd) => {
    if (cmd === "sync_workspace") {
      throw { kind: "permission_denied" };
    }
  });
  render(<SyncWorkspaceScreen />);
  await userEvent.click(screen.getByRole("button", { name: /sync/i }));
  expect(await screen.findByText(/permission/i)).toBeVisible();
  expect(screen.getByRole("button", { name: /retry/i })).toBeEnabled();
});
```

- Throw the same shape the real command rejects with. A mock that throws `new Error("...")` when the command returns a tagged object tests a path that does not exist.
- Test the failure and the recovery, not only the success.

**The lifecycle, on a real build:**

1. Launch the primary instance.
2. Trigger a second launch, or open a deep link.
3. Assert the arguments or link reach the primary window, and that it takes focus.
4. Assert there is still one process and one set of background workers.

**A latency bound** belongs in a benchmark or a dedicated performance job with a named
fixture and machine. A wall-clock assertion inside an ordinary unit test fails on a loaded
CI runner and gets deleted.

### Mocked IPC

**Test layers.** Two carry most of the weight: front-end tests with IPC mocked, and Rust
tests of commands and the core. End-to-end tests on a built application add confidence
about packaging and lifecycle, and are kept few.

```typescript
import { clearMocks, mockIPC, mockWindows } from "@tauri-apps/api/mocks";

afterEach(() => clearMocks());

test("the settings screen shows the stored theme", async () => {
  mockWindows("main");
  mockIPC((cmd, args) => {
    if (cmd === "read_settings") return { theme: "dark" };
    throw new Error("unexpected command " + cmd);
  });
  render(<SettingsScreen />);
  expect(await screen.findByLabelText(/theme/i)).toHaveValue("dark");
});
```

- **Test your code through the mock, not the mock itself.** A test that calls `invoke` and asserts the value the mock just returned verifies nothing.
- **Make the mock reject unexpected commands.** A handler that returns `undefined` for unknown names hides a renamed command.
- **Assert the arguments** the code sent, since argument drift is the common failure.
- **`clearMocks()` after every test,** or later tests pass against a stale handler.
- Use `mockWindows(...)` for logic that depends on window labels, and `shouldMockEvents: true` for flows driven by events.
- The WebDriver-based end-to-end support does not cover the macOS desktop webview. Plan another check for macOS-only behaviour: a manual run list, or a smoke script.

### Contract drift

**Mocks pin the contract only if they return what the real command serialises.**

- **A mock that returns an object where the command returns a string** (or the reverse) changes the contract under test without anyone noticing. Derive mock payloads from the shared fixture or generated types.
- **Test both ends of a changed boundary.** Green front-end mocks can sit over a broken command, and green Rust tests under a drifted `invoke` call.
- **When a contract changes on both ends but not in the mocks,** the application works and the mocked suite fails. Update the stale mocks; the code has not regressed. The reverse case, mocks updated and one end forgotten, is the dangerous one, and only a shared contract check catches it.
- A Rust-only refactor that leaves the contract unchanged may skip the mocked layer. Say so in the change.
- The mocking imports and the list of supported platforms depend on the Tauri version. Check them against the documentation for the version in the project.

### Gates

**Green `cargo` gates are required and not sufficient.** Clippy and `cargo test` do not see
an over-broad grant, a blocked main thread in a packaged build, or a drifted payload. A
review fails a broad shell or filesystem permission even when every test passes. Use this
list at the end of the work; do not design from it.

Alongside the required Rust gates at the end of this skill, run the repository's own front-end and Tauri
scripts with its own package manager, for example:

```bash
pnpm test
pnpm build
pnpm tauri build
```

- **Run both families in CI:** the Rust gates and the front-end and bundle commands. Spend human review time on what commands cannot see.
- **The bundle build is the slowest gate and the first one skipped.** Running it nightly, or only on changes under the Tauri directory, is an acceptable compromise when written down. Deleting it is not.
- **Copy gate commands with their flags intact.** A command missing `-D warnings` looks the same in a skim and checks less. Where `--all-features` conflicts with feature-gated plugins, use the project's feature matrix.
- **A failed gate is information.** Rerun only after something changed, and say what changed. Do not answer a red lint with `#[allow]`, or a failed bundle by dropping the command. Fix a flaky front-end test; rerun-until-green teaches a team to distrust the gate.
- The same check failing across several changes points to a gap earlier in the work, not to a check that should be loosened.

**Release readiness** is judged from the artefact: code, capability files, configuration,
documentation, and command output. Intentions are not inputs.

- Tick an item only against something checkable: a linked test, a command log, a capability file.
- If commands could not be run, say the review was by inspection only.
- Scale the walk to the boundary changed. A documentation change skips the bundle build, with the reason. A sidecar change is the longest walk: supervision, bounded start-up, permission scope and packaging are checked separately.
- **Ask how costly a choice is to undo.** Naming and diagram style are conventions, waived with a reason. Exposure that outlives the change (a granted permission, a panic in a shipped command, a leaked log line) is a gate and is not waived.
- Repeated waivers of one convention mean it does not fit the project. Amend it locally and openly.

## Review

### Questions

- **Trace one interaction end to end:** front-end event, command, permission declaration, Rust handler, packaged-application behaviour. Does each step have a strict input type, a timeout and a recovery path?
- What belongs in the front-end contract, the command layer and the core respectively? Is anything in the wrong one?
- Which boundary needed a capability, sidecar or lifecycle-ownership decision, and where is that decision written down?
- Which command names, event names and window labels must stay stable? They are public API to the front end and to capability files.
- Which risk is covered only by a unit test but lives at IPC, permission or lifecycle level?

**What to measure in a shipped desktop application:** command duration, front-end error
rate, start-up time, bundle size, failure rate by platform, update success and rollback
count.

**Failure modes to model:** permission drift, unvalidated command input, a blocked main
thread, path behaviour that differs by platform, a failed or half-applied update, and a
serialisation mismatch across IPC.

### Anti-patterns

```rust
// Blocking in an async command: freezes a runtime worker for five seconds.
#[tauri::command]
async fn export() -> String {
    std::thread::sleep(Duration::from_secs(5));
    "done".into()
}
// Fix: async I/O, tokio::time::sleep, or spawn_blocking for CPU-bound and blocking work.

// Borrowed argument in an async command: does not compile as written.
#[tauri::command]
async fn greet(name: &str) -> String { format!("hello {name}") }
// Fix: take String.

// Panic on a reachable path, and a path relative to the working directory.
#[tauri::command]
fn read_now() -> String { std::fs::read_to_string("file.txt").unwrap() }
// Fix: async, Result<T, AppError>, path resolved from the application directories.

// Double-wrapped state.
builder.manage(Arc::new(Mutex::new(AppState::default())));
// Fix: manage(Mutex::new(AppState::default())).
```

Reject by default:

- **`"permissions": ["fs:default", "shell:default"]`,** or any broad grant used as a convenience. *Fix:* exact commands with scoped paths, per window.
- **A command that takes a path, URL or shell fragment from the webview and uses it directly.** *Fix:* accept an identifier, or validate against an allow-list in Rust.
- **Events used as a data stream,** or large payloads sent as JSON. *Fix:* a channel, a binary response, or a file path.
- **The store as a blob sink.** A theme preference is fine; base64 screenshot history and multi-megabyte scrollback are not. *Fix:* files with a reference.
- **A sidecar spawned and then assumed ready, well-behaved and quiet.** *Fix:* a supervisor with a health check, a deadline, an argument scope and capped logs.
- **Opaque or unserialisable command errors,** or a front end that parses error message text.
- **String-named `invoke` calls scattered across components.**
- **Updater, tray, single-instance or deep-link behaviour verified only in `tauri dev`.**
- **Generic Rust habits overriding Tauri's rules** where they conflict: for example, renaming a command or window label for style when the name is a compatibility surface.
- **Requirements with nothing measurable** ("more reliable", "safer").

### Pre-ship check

**Before shipping a Tauri feature, verify:**

- **Commands:** structured success and structured failure; no blocking call in an async command; no `unwrap()` or `expect()` on a reachable path; names unique across modules; bytes returned as a binary response.
- **State:** the right lock for each piece; no guard across an await unless an async mutex was chosen for that reason.
- **Permissions:** each new permission is the narrowest that works; a high-privilege window inherits nothing through merged capabilities; sidecar scope names the binary and its arguments; the CSP was not widened.
- **Persistence:** stored payloads stay under their caps; files are written atomically.
- **Sidecars:** start-up has a deadline and a health check; the child is stopped on exit.
- **Lifecycle:** single-instance is registered first; deep links are validated beyond the scheme; the window does not flash on restore; tray and quit paths were run on each platform.
- **Front end:** listeners are removed on unmount; mocks are cleared between tests.
- **Build:** hooks and output paths match the front-end tooling; platform overrides are intentional and small; updater keys are not in the repository; no secret or sensitive payload is logged.

## Out of scope

- **Tauri plugin internals and mobile-only APIs.** Read the plugin's own documentation for the locked version.
- **The front-end framework itself** (components, state management, styling). Only the IPC boundary is covered here.
- **A sidecar's own internals.** If it is a Rust service, a parser or a command-line tool, write it with the skill for that kind of Rust; this skill covers only how the application owns it.
- **Unsafe code and FFI.** A native bridge beyond what a plugin offers needs the unsafe and FFI skill.

<!-- essentials:begin -->
## Rust essentials shared by every writer skill

This block is the same in every Rust writer skill. It holds the language-level rules that
decide whether Rust code is correct whatever it is for: ownership, types at boundaries,
errors, async, tests and the anti-patterns to reject. Where the skill above states a rule
for its own kind of Rust more firmly, that statement wins.

### Ownership and borrowing

**Defaults.**

- Borrow to read, take ownership to keep, `&mut` to change in place. The signature tells the caller which.
- Clone when the design calls for a second owner, not to make an error go away. A clone of a small value on a cold path is fine and often the clearest code; a clone in a loop over large data is worth a second look.
- `Arc` for shared ownership across threads, `Rc` within one. Neither is a substitute for deciding who owns the data.
- Hold locks and `RefCell` borrows for the shortest scope that is correct, and never across an `.await`.

**The error usually describes a real overlap.** Find which borrow is still alive and why,
then shorten it, instead of reaching for `clone` or `Rc<RefCell<_>>`.

```rust
// Rejected: first borrows items while push needs it mutably.
let first = &items[0];
items.push(first.clone());

// End the shared borrow before the mutation.
let first = items[0].clone();
items.push(first);
```

- **A method borrows all of `self`.** Calling `self.helper()` while a field is borrowed fails even if the helper touches other fields. Borrow the fields separately, which the compiler tracks, or make the helper take the fields it needs.

```rust
let Self { index, scratch, .. } = self;
for id in index.keys() {
    scratch.push(*id); // index is borrowed shared, scratch mutably: disjoint fields
}
```

- **Collect, then mutate.** Gather the keys or indices to change in one pass and apply them in a second. Often clearer as well as accepted.
- **Use indices or IDs instead of long-lived references** into a collection that also needs mutation. This is the normal shape for graphs and trees with parent links.
- **Move out through `&mut` with `std::mem::take`, `replace` or `Option::take`,** instead of cloning a field in order to consume it.
- **The `entry` API** does "look up, then insert or update" with one borrow and one hash.

```rust
*counts.entry(word).or_insert(0) += 1;
```

- **Separate the read phase from the write phase in an API.** A method that returns a reference into `self` keeps `self` borrowed for as long as the caller holds it; returning a small owned value or an ID frees the caller.
- `vec.push(vec.len())` compiles through two-phase borrows. Do not design an API that only works because of that rule; write the temporary.
- **Stop and reconsider the design** when a structure wants references to itself, or when lifetimes spread through many signatures. Owned data plus indices, or an arena, is nearly always the answer; `unsafe` is not.

### Interior mutability

| Need | Use | Watch for |
|---|---|---|
| A `Copy` value, one thread | `Cell<T>` | nothing; it cannot fail |
| Any value, one thread | `RefCell<T>` | a second overlapping `borrow_mut` panics at run time |
| Shared across threads | `Mutex<T>` | poisoning, lock order, holding it across `.await` |
| Read-mostly across threads | `RwLock<T>` | writer starvation; often no faster than `Mutex`, so measure |
| A counter or flag | `AtomicUsize`, `AtomicBool` | choosing an ordering; `SeqCst` unless you can argue for less |
| Set once, read often | `OnceLock<T>`, `LazyLock<T>` | initialisation that can fail |

- `RefCell` moves a compile-time rule to run time. Keep each borrow to one statement where possible, and prefer `try_borrow_mut` where re-entrancy is conceivable (callbacks, observers).
- Do not use a `Mutex` in single-threaded code to quiet the borrow checker, and do not make a type `Sync` by wrapping it in one without deciding what the lock protects.
- Interior mutability behind `&self` is part of the API's contract. Say so in the docs when a `&self` method changes observable state.

### Choosing a pointer

| Need | One thread | Across threads |
|---|---|---|
| One owner on the heap (recursive type, large value, trait object) | `Box<T>` | `Box<T>` |
| Several owners, read-only | `Rc<T>` | `Arc<T>` |
| Several owners, mutation | `Rc<RefCell<T>>` | `Arc<Mutex<T>>` or `Arc<RwLock<T>>` |
| A reference back to an owner | `rc::Weak<T>` | `sync::Weak<T>` |

- **Shared and immutable is the cheap case.** Prefer `Arc<T>` of immutable data, replaced whole, over `Arc<Mutex<T>>` mutated in place. `Arc::make_mut` gives copy-on-write when a private change is needed.
- **`Rc<RefCell<T>>` throughout a design is a sign** that ownership was never decided. It suits a few shared nodes (a GUI tree, an observer list), not a whole data model. Indices into an owning `Vec` are usually simpler and faster.
- **Parent-to-child strong, child-to-parent `Weak`,** or the cycle never frees.
- `Arc::clone(&x)` rather than `x.clone()` makes it visible that only the count is bumped.
- Before `Arc<Mutex<T>>` across tasks, ask whether one task could own the state and receive messages on a channel.

### Iterators and collections

- **A fallible pipeline short-circuits.** An iterator of `Result<T, E>` collects into `Result<Vec<T>, E>` and stops at the first error. `try_for_each` and `try_fold` do the same without collecting. Never `unwrap` inside a chain.

```rust
let ports: Vec<u16> = fields
    .iter()
    .map(|field| field.parse::<u16>())
    .collect::<Result<_, _>>()?;
```

- **Iterator promises are contracts.** `size_hint` must bracket the true length; implement `ExactSizeIterator` only when the length is exact. Unsafe code must not rely on either for memory safety, since safe code can implement them wrongly.
- Offer `iter()`, `iter_mut()` and `IntoIterator` for `&T`, `&mut T` and `T` on a collection type, so `for x in &collection` works.
- Iterators are lazy. A `map` with side effects that is never consumed does nothing; use `for` when the point is the effect.

| Need | Collection |
|---|---|
| A sequence; the default | `Vec` |
| Push and pop at both ends | `VecDeque` |
| Lookup by key, order irrelevant | `HashMap`, `HashSet` |
| Sorted order, range queries, deterministic iteration | `BTreeMap`, `BTreeSet` |
| Insertion order with lookup | `IndexMap` |
| Repeatedly take the largest | `BinaryHeap` (wrap in `Reverse` for the smallest) |
| A handful of items | a `Vec` and a linear scan, or `SmallVec` if measured |

- **`HashMap` iteration order is arbitrary and differs between runs.** Anything that reaches output, a hash, a snapshot or a test goes through a sort or an ordered map.
- `LinkedList` is almost never right: a `Vec` or `VecDeque` is faster for nearly every workload.
- The default hasher resists collision attacks and is slower for it. A faster hasher (`FxHashMap`, `ahash`) is for keys an attacker does not control, after a profile says hashing matters.
- `Vec::with_capacity` when the size is known; it is free and removes reallocations.

### Types and API basics

Each with when it pays and when it does not.

- **Accept borrowed inputs.** `&str`, `&[T]` and `&Path`, not `&String`, `&Vec<T>` and `&PathBuf`. The API then commits to meaning, not to a container. *When the function stores the value,* take it owned (`String`, or `impl Into<String>`) so the caller who already owns one does not pay for a clone. `impl AsRef<Path>` is right for path arguments; `impl AsRef<str>` everywhere is noise and bloats code through monomorphisation.
- **Newtypes, and parse instead of validating.** Turn raw data plus repeated checks into a type that can only hold a valid value. IDs, units, offsets, validated strings and handles stop being interchangeable primitives. *Skip when* the wrapper carries no invariant and no distinction anyone could confuse; a newtype around every `String` is ceremony.

```rust
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct Email(String);

impl Email {
    pub fn parse(raw: &str) -> Result<Self, EmailError> {
        let trimmed = raw.trim();
        if trimmed.is_empty() {
            return Err(EmailError::Empty);
        }
        if !trimmed.contains('@') {
            return Err(EmailError::MissingAt);
        }
        Ok(Self(trimmed.to_owned()))
    }
    pub fn as_str(&self) -> &str { &self.0 }
}
```

  Keep the field private and offer no constructor that skips the check, or the guarantee is gone. That includes `Deserialize`: derive it through `#[serde(try_from = "String")]`, not on the raw field. Do not implement `DerefMut` or hand out `&mut` to the inner value.
- **`From` for conversions that cannot fail, `TryFrom` for those that can.** *Use a named constructor instead* when the operation does real work, loses information or has more than one sensible meaning. `From` must be cheap and unsurprising, because `?` and `.into()` call it invisibly.
- **Combinators for straight-line flows, `match` for branching.** `map`, `and_then`, `ok_or_else` and `transpose` keep a linear transformation linear. When there are several arms with different work, or a chain of four closures, a `match` or `let ... else` reads better.
- **Generics or `dyn`, chosen on purpose.** Generics for hot paths and when the caller knows the type. `dyn Trait` for heterogeneous collections, plugin points, and to keep compile time and code size down. For a call that does I/O, the virtual call is immeasurable; do not make a service generic over five type parameters to avoid it.
- **Return `impl Iterator` to stay lazy** and hide adapter types. Use `Box<dyn Iterator>` when branches return different iterator types or the type must be stored in a struct field without a generic parameter. Return a `Vec` when the caller always needs all of it and the size is bounded.
- **A named enum over a boolean or a sentinel.** A `bool` says something happened; an enum says what the caller must do next. `enum Inserted { New, Replaced(Old) }` beats `true`; `Option<usize>` beats `-1`. *A `bool` is fine* for a real yes-or-no question (`is_empty`).
- **A flat public facade with `pub use`.** Internal file layout and public paths are separate decisions; re-exports let internals move without breaking callers. Re-export deliberately, item by item. Do not re-export a dependency's types unless they are part of your contract, because then its version is too.
- **Blanket impls for `&T`, `&mut T` and `Box<T>`** make a trait usable through references and boxes without wrappers. Add them when the trait is naturally delegating and its methods take `&self`.
- **Omitted is not the same as explicitly empty.** For a partial update, "not provided" and "set to nothing" are different inputs:

```rust
pub enum Patch<T> {
    Keep,
    Clear,
    Set(T),
}
```

  `Option<Option<T>>` works with serde but is hard to read; the enum is clearer in domain code. Never use a magic value from the domain (an empty string, zero) to mean either.
- **Name the unit of an offset.** Bytes, `char`s and UTF-16 code units are different numbers for the same position. Put the unit in the type (`ByteOffset`, `Utf16Offset`) wherever offsets cross a boundary, and test on multi-byte text.
- **Strategies are named for the guarantee they give.** An operational choice is a named type behind a small trait, not a hidden boolean, and its documentation says what it does *not* preserve:

```rust
pub trait Sharding: Send + Sync {
    fn pick_shard(&self, shard_count: usize, key: &Key) -> usize;
}
pub struct Balanced { next: AtomicUsize } // spreads load; does not keep per-key order
pub struct Ordered;                       // keeps per-key order; load may skew
```

  Offer no alternatives where correctness needs one behaviour.

### Core idioms

- **Expressions over statements.** `if`, `match` and blocks are expressions; bind their value instead of declaring a `mut` and assigning in each branch. Use an iterator chain where it reads as a description of the result; use a loop where there are side effects, early exits or several accumulators.

```rust
let label = match status {
    Status::Active => "active",
    Status::Suspended { .. } => "suspended",
    Status::Closed => "closed",
};
```

- **`Cow<'_, str>` when the value is usually borrowed and sometimes changed:** normalisation, escaping, lossy decoding.

```rust
pub fn normalise(input: &str) -> Cow<'_, str> {
    if input.contains('\t') {
        Cow::Owned(input.replace('\t', "    "))
    } else {
        Cow::Borrowed(input)
    }
}
```

  *Skip it* when the value is always owned or always borrowed, and in struct fields unless profiling asks for it: the lifetime spreads to every holder. Calling `.into_owned()` on every result means it should have returned `String`.
- **A `type` alias is not a new type.** `type UserId = u64;` documents and checks nothing. Use a newtype for distinction; use an alias to shorten a long generic type.
- **`#[repr(transparent)]` on a newtype** is needed only when its layout is relied on: across FFI, or for a reference cast between the wrapper and its field. Elsewhere it is harmless and unnecessary.
- **The orphan rule:** to implement a foreign trait for a foreign type, wrap the type in a local newtype.
- **Do not return `Result` from something that cannot fail,** and do not return `Option` where an error would explain why.
- **`impl Fn` for callbacks, `fn` pointers for tables.** `impl Fn(T) -> U` accepts closures and inlines. A plain `fn(T) -> U` pointer rejects capturing closures; use it in static dispatch tables, in `const` contexts and across FFI, where a nameable, `Copy` type is the point. `&dyn Fn` or `Box<dyn Fn>` when the callback is stored or code size matters more than the call.
- **Keep generic bounds as simple as the use.** `fn f(s: &str)` beats `fn f<S: AsRef<str>>(s: S)` unless callers really pass several types; over-generic signatures hurt inference and error messages. When a generic wrapper is wanted, make it thin and delegate at once to a non-generic inner function, so the body is compiled once.

```rust
pub fn read_config(path: impl AsRef<Path>) -> Result<Config, ConfigError> {
    fn inner(path: &Path) -> Result<Config, ConfigError> { /* the real body */ }
    inner(path.as_ref())
}
```

- **Visibility is the narrowest that works.** Start private; widen to `pub(crate)`, then `pub` when something outside needs it. Every `pub` item in a library is a promise.
- **Do not clone to quiet the borrow checker.** The error is usually pointing at an ownership question: who should own this, and for how long. Answer that. `Rc` or `Arc` is for when several owners really exist.
- **Monomorphisation has a cost.** If generics inflate compile time or binary size, use `dyn Trait` at boundaries and on cold paths, and measure the effect (`cargo llvm-lines`, `cargo bloat`).
- **Name the collection type where it reads best:** `let v: Vec<_> = iter.collect();` or `iter.collect::<Vec<_>>()`. Collect into `Result<Vec<_>, _>` to stop at the first error.
- **Pick the pattern form by the number of cases.** `match` when every case matters; `if let` for one case where the rest is nothing; `let ... else` to unwrap or leave early and keep the happy path unindented; `while let` to drain; `matches!` for a boolean test.

```rust
let Some(user) = users.get(&id) else {
    return Err(Error::UnknownUser(id));
};
```

- **`#[non_exhaustive]` keeps room to grow.** On a public enum, other crates must write a wildcard arm, so adding a variant is not a breaking change; on a struct, they cannot construct it literally, so adding a field is not either. *Use on* public error enums and option structs expected to grow. *Do not use on* an enum callers are meant to match exhaustively (a closed set of states), because it takes the compiler's check away from them. It has no effect inside the defining crate.
- **Avoid a wildcard arm on your own enums.** `_ =>` silences the compiler exactly when a new variant arrives. List the variants, or group them explicitly.

### Destructors, guards and temporaries

- `Drop` cannot fail, must not block and should have almost no side effects. If teardown can fail, block or needs `.await`, expose `close`, `flush` or `shutdown` returning `Result`, and let `Drop` release only local state as a fallback.
- If correctness needs teardown to happen before later work, show it in control flow (an explicit `drop(guard)` or an inner block) and test it.
- `let _ = mutex.lock();` drops the guard at once; `let _guard = mutex.lock();` holds it to the end of the scope. Choose on purpose.
- A temporary created in a `match` or `if let` scrutinee lives to the end of the whole statement:

```rust
// Bad: the guard lives for the whole match, so the second lock deadlocks.
match cache.lock().unwrap().get(&key).cloned() {
    Some(v) => v,
    None => compute_and_insert(&cache, key), // locks the cache again
}

// Good: the guard is dropped at the end of the let statement.
let hit = cache.lock().unwrap().get(&key).cloned();
match hit {
    Some(v) => v,
    None => compute_and_insert(&cache, key),
}
```

- A task that can outlive its caller documents how it is cancelled and how it shuts down.

### Errors

**Defaults.**

- A function that can fail returns `Result`; `?` propagates. Panics are for bugs: a broken invariant that no caller could handle.
- **Libraries return typed errors** (an enum or struct, usually via `thiserror`) that callers can match on. **Applications use `anyhow` or `eyre`** at the top, where errors are reported, not matched. Never export `anyhow::Error` from a library: it tells callers nothing and takes away their ability to react.
- No `unwrap` or `expect` on a path that input, I/O or another system can make fail. Where an invariant truly guarantees success, `expect("why this cannot fail")` states it.
- Never swallow an error. Handle it, return it, or log it with a reason for going on.

### Designing an error type

```rust
#[derive(Debug, thiserror::Error)]
pub enum StoreError {
    #[error("record {id} not found")]
    NotFound { id: RecordId },

    #[error("query timed out after {elapsed:?} (limit {limit:?})")]
    Timeout { elapsed: Duration, limit: Duration },

    #[error("reading {}", .path.display())]
    Read {
        path: PathBuf,
        #[source]
        source: io::Error,
    },

    #[error(transparent)]
    Database(#[from] DatabaseError),
}
```

- **One variant per thing a caller might do differently** (retry, report to the user, treat as absent), not one per call site and not one per underlying library.
- **A variant carries the data needed to act or to explain:** the ID, the path, the limit. A variant holding only a `String` is a message, not a type.
- **Keep the cause as `#[source]`, and do not repeat its text in your message.** Reporters print the chain; a message that embeds the source prints it twice. `cause: String` throws the chain away.
- Messages are lower case, without a trailing full stop, and say what was being attempted.
- **`#[from]` only where the conversion needs no context.** A blanket `From<io::Error>` makes every `?` on a file operation produce an error that does not say which file.
- Errors are `Send + Sync + 'static` so they can cross threads and be boxed. Keep them small; box a large payload, since the size of `E` is paid by every `Result<T, E>`.
- **`#[non_exhaustive]` on a public error enum that will grow,** so adding a variant is not a breaking change.

**An opaque error with a kind, when the error space will evolve.** A public enum freezes its
variants and their fields. A struct with a private representation and a public `kind()` keeps
room to change.

```rust
#[derive(Debug)]
pub struct Error {
    kind: ErrorKind,
    source: Option<Box<dyn std::error::Error + Send + Sync>>,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
#[non_exhaustive]
pub enum ErrorKind {
    NotFound,
    Timeout,
    InvalidInput,
}

impl Error {
    pub fn kind(&self) -> ErrorKind {
        self.kind
    }

    pub fn is_retryable(&self) -> bool {
        matches!(self.kind, ErrorKind::Timeout)
    }
}
```

- Callers cannot construct it, so only your crate decides which states exist. Predicates such as `is_retryable()` answer the question callers actually have.
- *Use a plain enum* when the set is small, stable and callers benefit from matching on fields. Most internal crates are in that case.

### Context and reporting

**Add context where the operation is still meaningful.** `?` alone says what failed, not what
was being done.

```rust
pub fn load_config(path: &Path) -> anyhow::Result<Config> {
    let text = fs::read_to_string(path)
        .with_context(|| format!("reading config {}", path.display()))?;
    let config = toml::from_str(&text)
        .with_context(|| format!("parsing config {}", path.display()))?;
    Ok(config)
}
```

- Context belongs at I/O and orchestration boundaries: opening a file, sending a request, decoding a payload, calling another service. Adding it at every helper repeats the same sentence down the chain.
- `with_context` takes a closure, so the message is formatted only on failure.
- In a library, the equivalent is a variant that carries the context plus the `#[source]`, built with `map_err`.

**A diagnostic for a person says where and what to do.** For user-facing input (configuration,
flags, patterns, file formats): the file, line and column or byte offset, what was found, what
was expected, and a hint when there is an obvious repair. An abstract variant name helps
nobody.

- Rich reports with source snippets and labelled spans (`miette`, `ariadne`, `color-eyre`) belong in the binary. Do not put their types in a library's public API; expose spans and messages as plain data and let the binary render them.
- **Diagnostics must survive non-UTF-8 data.** Paths, command output and protocol bytes are not always valid UTF-8. Print paths with `.display()`, bytes with an escaping formatter, and do not convert to `String` early with `unwrap` or lose data with a silent lossy conversion.
- Never put secrets, tokens or whole payloads in an error message. Errors travel to logs and to users.

**The binary owns the exit code.**

```rust
fn main() -> ExitCode {
    match run() {
        Ok(()) => ExitCode::SUCCESS,
        Err(error) if is_broken_pipe(&error) => ExitCode::SUCCESS,
        Err(error) => {
            eprintln!("error: {error:#}");
            ExitCode::from(2)
        }
    }
}
```

- Returning `ExitCode` from `main` lets destructors run; `std::process::exit` does not, so buffered output and temporary files can be lost.
- A closed pipe (`tool | head`) is not a failure. Look for `io::ErrorKind::BrokenPipe` in the chain and exit quietly.
- `{error:#}` prints an `anyhow` error with its causes on one line; `{error:?}` prints the multi-line report with a backtrace if one was captured.
- Distinct exit codes for distinct classes (usage error, runtime failure) are part of a CLI's interface; document them. Errors go to stderr, results to stdout.
- **A library never exits the process,** prints to stdout or stderr, or installs global handlers.

### Panics

- **Audit production paths before a release:** `unwrap`, `expect`, `panic!`, `unreachable!`, `todo!`, slice indexing and arithmetic on external input. Each becomes a `Result` or gets a comment stating the invariant.

```sh
cargo clippy -- -W clippy::unwrap_used -W clippy::expect_used \
  -W clippy::indexing_slicing -W clippy::panic
```

- Compiling and passing unit tests does not show that a panic is unreachable. For each boundary, one test feeds the bad input and asserts the returned error.
- These lints are noisy in tests; allow them there (`#![cfg_attr(test, allow(clippy::unwrap_used))]`) instead of weakening them everywhere.
- **A panic must not cross an FFI boundary.** Catch it with `catch_unwind` at every exported `extern "C"` function and turn it into an error code.

### Recovery by error class

| Class | Where it arises | Recovery | Represent as |
|---|---|---|---|
| Validation | parsing, input edge | reject with the reason | typed parse or validation error |
| Business rule | domain workflow | reject with a precise outcome | named domain error or outcome enum |
| Transient external | network, storage, subprocess | retry with bounds, degrade, reschedule | retryable variant or flag |
| Permanent external | auth, contract or schema mismatch | fail fast, name the repair | typed permanent error |
| Timeout | async orchestration | fail, retry or cancel, explicitly | timeout error carrying the limit |
| Cancellation | task or workflow boundary | stop cooperatively, clean up | its own path, not a failure |
| Overload | queue, pool, stream | reject, shed or wait with a bound | explicit "saturated" result |
| Invariant breach | core logic | make impossible by construction, else fail fast | a narrow panic or an internal error |
| Clean-up failure | close, shutdown | explicit `close`, best-effort `Drop` | close error or shutdown report |
| FFI boundary | ABI, foreign ownership | convert, isolate or abort | the safe wrapper's error |

- **A message answers three questions:** what failed, where, and what the reader should do next.
- **If callers branch on it, give them structure; if they only pass it up, give them context.** Most errors are the second kind.
- Cancellation and overload are not failures of the operation and should not be logged or counted as such.
- A dependency's error type in your public signature makes its version part of your API. Wrap it or re-export it deliberately.

**Smaller rules.**

- **An undo log for in-memory mutations that need rollback.** Record each mutation's inverse as data (`enum UndoOp { CreateNode(NodeId), UpdateAttr { id, old } }`) and replay it backwards on failure. A new mutation kind adds its undo record in the same change; an exhaustive `match` enforces it. Use real transactions when the storage engine has them.
- **`no_std` errors:** implement `core::fmt::Display` by hand and `core::error::Error` directly (stable since Rust 1.81), or put `std::error::Error` behind a `std` feature on older toolchains.
- **Tests assert the variant or code, not message text,** so wording can improve. Retry tests assert behaviour (a permanent error is attempted once; the deadline stops the loop), not exact jittered delays.

### Async and concurrency

**Defaults.**

- **Never block the executor.** No blocking I/O, `std::thread::sleep`, long CPU work or blocking lock inside an async function. Blocking work goes to `spawn_blocking`; CPU-heavy work to a thread pool such as `rayon`.
- **Never hold a lock guard across `.await`.**
- **Everything is bounded:** channels, concurrency, retries, timeouts, buffers.
- **Every task has an owner** that can cancel it and learns how it ended.
- **Every long-running operation can be cancelled** and has a deadline.
- First ask whether you need async at all. A CLI, a build tool or a CPU-bound pipeline is usually simpler and as fast with threads. Async earns its place with many concurrent I/O waits.

### Blocking and locks

**How long is too long without an `.await`?** As a rule of thumb, more than about 100
microseconds of work between yield points starts to hurt other tasks' latency.

| Work | Where it runs |
|---|---|
| Short CPU work, non-blocking calls | inline in the task |
| Blocking I/O, a synchronous client, file-system calls | `tokio::task::spawn_blocking` |
| Heavy CPU work, parallel across cores | `rayon`, with the result sent back over a `oneshot` |
| A long-lived blocking loop | a dedicated `std::thread` |

- `spawn_blocking` tasks cannot be cancelled once started, and the pool is large but finite. Do not park an endless loop there.
- `tokio::fs` uses the blocking pool underneath. For many small file operations, one `spawn_blocking` around the whole batch is faster.

**Locks.**

```rust
// Wrong: the guard lives across the await.
let mut state = shared.lock().unwrap();
state.total += fetch_amount().await?;

// Right: await first, then lock briefly.
let amount = fetch_amount().await?;
shared.lock().unwrap().total += amount;
```

- **Use `std::sync::Mutex` (or `parking_lot`) for short critical sections, even in async code.** It is faster than an async mutex, and its guard is not `Send`, so the compiler rejects holding it across an `.await` in a spawned task.
- **Use `tokio::sync::Mutex` only when the guard must be held across an `.await`,** such as serialising access to a connection. Then ask whether a single owning task with a channel would be clearer.
- A guard in a temporary lives to the end of the statement, and in `if let` or `match` on editions before 2024 to the end of the block. When in doubt, bind the value you need and `drop(guard)` explicitly.
- The same rule holds for a `RefCell` borrow and for anything else that must be released: a pooled connection, a permit, a transaction.
- **Lock order:** when two locks are ever held together, one documented order, everywhere. Better, restructure so that no code holds two.

### Cancellation

**In async Rust, any `.await` is a point where the future may be dropped and never resumed.**
That happens on `select!`, on a timeout, when a `JoinHandle` is aborted, and when a client
disconnects.

- **A future is cancel-safe if dropping it between polls loses nothing.** `recv()` on a Tokio channel is. Reading "exactly n bytes" into a local buffer is not: the bytes already read vanish with the future.
- **In `select!`, keep state outside the branch futures.** A half-filled buffer or a half-advanced parser lives in a variable that survives the loop iteration; the branch only awaits the next piece.

```rust
let mut buffer = BytesMut::new(); // outlives each select! iteration
loop {
    tokio::select! {
        _ = shutdown.cancelled() => break,
        read = socket.read_buf(&mut buffer) => {
            if read? == 0 { break; }
            while let Some(frame) = try_parse(&mut buffer)? {
                handle(frame).await?;
            }
        }
    }
}
```

- **A multi-step change that must not be half-done** is either made atomic (one transaction, one message to an owning task) or run in a spawned task the caller waits on, so that dropping the caller does not stop it midway.
- **Clean-up after cancellation runs in `Drop`, which cannot `.await`.** Hand async clean-up to an owner task, or offer an explicit async `shutdown()` and treat `Drop` as the fallback.
- **Use a `CancellationToken` for cooperative shutdown.** Pass it down, check it in loops and `select!`, and give children `child_token()` so a subtree can be cancelled alone.
- Document, for every public async function, whether it is cancel-safe.

### Tasks and their owners

**A spawned task belongs to something that waits for it.** A detached `tokio::spawn` whose
handle is dropped keeps running, its panic goes unnoticed, and shutdown cannot wait for it.

```rust
let mut tasks = JoinSet::new();
for job in jobs {
    tasks.spawn(process(job));
}
while let Some(joined) = tasks.join_next().await {
    match joined {
        Ok(Ok(report)) => reports.push(report),
        Ok(Err(error)) => return Err(error), // dropping the set aborts the rest
        Err(join_error) => return Err(Error::TaskPanicked(join_error)),
    }
}
```

- `JoinSet` aborts its remaining tasks when dropped, so an early return does not leak work. A `JoinError` is a panic or an abort; handle it, do not `unwrap` it.
- **Bound the fan-out.** A `Semaphore` permit per task, or `futures::stream::iter(jobs).map(f).buffer_unordered(limit)` when the futures need not be spawned.
- **`join!` and `try_join!` for a fixed, small set** of futures on the current task: no spawn, no `'static` bound, borrowing allowed. `tokio::spawn` when the work should run in parallel on other threads or outlive the caller.
- **A background task for the life of the service** is held by the component that starts it: store the `JoinHandle` and the cancellation token, and have `shutdown()` cancel and then await it with a time limit.
- **Carry trace context across the spawn.** Do it in the project's one spawn helper, so tasks inherit the caller's span by default.

```rust
tokio::spawn(work().instrument(tracing::Span::current()));

let span = tracing::Span::current();
tokio::task::spawn_blocking(move || span.in_scope(blocking_work));
```

- **Threads:** name them (`thread::Builder::new().name(...)`), join them, and prefer `std::thread::scope` when they only need to borrow local data for a bounded time.

**A supervisor fails in-flight jobs before it restarts the worker.** A worker that can crash
(a thread, a child process, a WASM instance) has a supervisor holding a registry of pending
replies.

```rust
struct Supervisor {
    in_flight: HashMap<JobId, oneshot::Sender<Result<Output, WorkerError>>>,
    consecutive_restarts: u32,
}

impl Supervisor {
    fn on_worker_exit(&mut self) -> Result<(), WorkerError> {
        for (_, reply) in self.in_flight.drain() {
            let _ = reply.send(Err(WorkerError::Crashed)); // the caller may have gone away
        }
        self.consecutive_restarts += 1;
        if self.consecutive_restarts > MAX_RESTARTS {
            return Err(WorkerError::GaveUp);
        }
        self.spawn_worker()
    }

    fn on_worker_ready(&mut self) {
        self.consecutive_restarts = 0; // only a successful start resets the count
    }
}
```

- **A clean error beats a future that never completes.** Jobs are failed, not replayed: only the caller knows whether a retry is safe.
- Restart with backoff and a cap. A worker that dies at start-up must not be restarted in a tight loop.
- Per-job resources are freed by an owning guard's `Drop`, so the crash path releases them too.

**A timeout does not mean the work stopped.** Dropping a timed-out future stops async work at
its next `.await`, but a `spawn_blocking` closure, a thread or a child process carries on.

```rust
match self.running.get(&job) {
    Some(handle) if !handle.is_finished() => return Tick::StillRunning, // skip this tick
    Some(_) => {
        self.running.remove(&job);
    }
    None => {}
}
let handle = tokio::task::spawn_blocking({
    let job = job.clone();
    move || run(job)
});
self.running.insert(job, handle);
```

- For a periodic job, skip the tick while the previous run is alive, or runs pile up on the same data.
- For work that must stop, give it a flag or token it checks, or run it in a child process that can be killed.
- Report "timed out, still running" differently from "failed".

### Tests and evidence

| Evidence | Choose it when | It does not show |
|---|---|---|
| Unit test | Behaviour is local and deterministic | That the parts work together |
| Integration test | Behaviour crosses a module, process or adapter boundary | Every edge case; too slow for that |
| Doctest | A public example is part of the contract | Anything about error paths, unless written |
| Compile-fail test (`trybuild`) | Misuse must not compile: typestate, `Send` bounds, lifetimes | Run-time behaviour |
| Property test (`proptest`) | An invariant or a round trip matters more than examples | That the stated property is the right one |
| Fuzzing (`cargo-fuzz`) | A parser, decoder or other frontier takes untrusted bytes | Semantic correctness; it finds panics, hangs and whatever you assert |
| `loom` | A small concurrent state machine built on atomics or locks | Anything about async I/O or large systems; the model must be tiny |
| Miri | Unsafe code, aliasing, uninitialised memory | Paths the tests do not execute; no FFI |
| Benchmark | A latency or memory threshold was stated | Production behaviour, unless the input is representative |
| Snapshot test (`insta`) | Output is large and structured: rendered text, plans, diagnostics | Correctness of the first snapshot; a person must read it |

- **Pick the rows at the start and record which ones the change triggers.** A matrix filled in after the code only justifies the evidence that already exists. Formatting, lints, tests and a build can all pass over a parser that was never fuzzed and a lock whose interleavings were never explored.
- **No threshold, no performance claim.** The benchmark row is owed only when a number was stated; without one, do not write "fast" in the report either.
- **Choose the smallest set that covers the risk,** not the largest that can be listed.
- **A missing test is written as missing.** An empty row marked "not covered" is honest; an invented test name is not.
- Coverage is a tool for finding untested code. It is not evidence that the tested code is right, and it is a poor target.

**The test-first loop.**

```text
STUB -> RED -> GREEN -> REFACTOR -> VERIFY
```

- **STUB.** Write the signature with a `todo!()` body, and the tests against it. At least one test per requirement.
- **RED.** Run it and *read the failure*. The first failure should be the missing behaviour. An unrelated compile error or a panic in the set-up means the test is not yet testing the thing. A test that has never failed has not been shown to test anything.
- **GREEN.** The least code that passes. Resist generalising here.
- **REFACTOR.** Improve names, decomposition and ownership with the tests green. No behaviour change in this step.
- **VERIFY.** Formatting, lints, the full test suite and a build, plus whichever rows from the table the change triggered.

For each requirement, cover three paths: the normal one, the error one, and an edge (empty,
one, maximum, boundary). State the empty case in the requirement itself: no matches is an empty
`Vec`, not an error and not `None`.

**When to apply it strictly, and when not.**

- *Strictly* for a bug fix (the failing test is the reproduction and stays as the regression test), for logic with a clear input-to-output contract, and for anything behind a public API.
- *Loosely* for exploratory work where the interface is not known yet: spike without tests, learn the shape, then throw the spike away or write the tests before it is merged. Do not let a spike become the implementation untested.
- *Not test-first* for pure wiring, generated code and thin adapters; an integration test afterwards covers them better than unit tests written in advance.
- Anti-pattern: writing the implementation, then writing tests that assert whatever it does. Those tests pin the bugs.
- Anti-pattern: changing the assertion to make a failing test pass, without first deciding whether the code or the test was wrong.

**Cheap checks before commit.** Search the added lines of the diff for `TODO`, `FIXME`,
`todo!`, `unimplemented!` and `dbg!`, and the added non-test lines for `.unwrap()` and
`.expect(`. Each hit is either removed or justified.

### Names

**A name says what the thing is or does at the call site,** in the vocabulary of the domain.
Length follows scope: a loop index may be `i`; a public function may not be `process`.

- **Follow the Rust API naming conventions:** `as_`, `to_`, `into_` by cost; `iter`, `iter_mut`, `into_iter`; `new` and `with_` constructors; `try_` for the fallible twin; `is_` and `has_` for predicates; getters without a `get_` prefix; `_mut` and `_unchecked` suffixes.
- **Casing:** `UpperCamelCase` types and traits, `snake_case` functions and modules, `SCREAMING_SNAKE_CASE` constants. Acronyms are words: `HttpClient`, `parse_url`. Crate names avoid `-rs` and `rust-`.
- **A name carries its unit when the type does not:** `timeout_ms`, `size_bytes`. Better, let the type carry it (`Duration`, a newtype).
- **Do not repeat the module in the item:** `cache::Config`, not `cache::CacheConfig`, unless items are usually imported bare.
- **One concept, one word.** If the code says `fetch`, `load` and `get` for the same operation, the reader assumes three operations.
- **Avoid names that say nothing:** `data`, `info`, `manager`, `helper`, `util`, `handle_it`, `do_work`.
- **Booleans read as assertions,** positively: `is_enabled`, not `not_disabled` or `flag`.
- **Follow the repository's own scheme where it has one.** Some codebases adopt a fixed pattern such as four-word `verb_constraint_target_qualifier` names (`filter_implementation_entities_only`). That is a local convention: apply it there, and nowhere else by default. Never count words where the result is a worse name.
- **A risky rename of a public item is done in two steps:** add the new name, deprecate the old with `#[deprecated(note = "use `new_name`")]`, and remove it in the next major version.

### Anti-patterns

This is the list to scan before handing work over. Each
has an exception, because the opposite mistake exists too.

### Reject by default

| Smell | Do instead | Legitimate exception |
|---|---|---|
| A requirement with nothing measurable ("make it faster") | A testable statement: input, expected result, threshold | Exploratory spikes, labelled as such and thrown away |
| A performance claim with no measurement | A benchmark, or a contract test that enforces the number | None; say "not measured" |
| `&Vec<T>`, `&String`, `&Box<T>` parameters | `&[T]`, `&str`, `&T` | You need `capacity()` or another method of the container itself |
| `anyhow::Error` or `Box<dyn Error>` in a library's public API | A typed error enum | Applications and binaries, where nobody matches on the error |
| `unwrap()` or `expect()` on a path input can reach | `?` and a typed error | A proven invariant, stated in the `expect` message; tests |
| Blocking work on an async executor | `spawn_blocking`, a dedicated thread, or an async API | Work bounded well under a millisecond |
| A lock guard or `RefCell` borrow held across `.await` | Copy out and drop the guard; or an async mutex where the await is the point | An async mutex guarding an I/O resource that must be used serially |
| An unbounded channel or queue | A bound, plus a stated policy when full | A provably bounded producer, with the proof in a comment |
| A spawned task with no owner | `JoinSet` or a supervisor; a cancellation path; observed failures | None in a long-running service |
| Concurrency never exercised under contention | Stress tests, `loom` for small lock-free cores, TSan | Code that is trivially confined to one thread |
| Text handling that assumes UTF-8, or one byte per character | `&[u8]`, `OsStr`, `Path`; `char_indices` for boundaries | Input already validated as `str` |
| I/O, runtime or framework types in the core domain | Pure core; adapters at the edge | Small programs where the split would be the bulk of the code |
| A struct holding the concrete database or HTTP client it uses | Depend on a narrow trait or pass a function; construct at the edge | The adapter itself |
| A "manager" struct with twenty fields | Split by responsibility and by what changes together | A plain configuration record |
| A domain model that ignores real cases | Model the cases the input actually has, or reject them explicitly | A stated, enforced subset |
| A public enum that will grow, without `#[non_exhaustive]` | Add it before the first release | Enums that are closed by definition |
| A diagnostic that drops the location | Carry file, line, column or byte span through to the message | None |
| Tests that only replay examples | Add the invariant: a property test, a round trip, a boundary table | Glue code with no invariant to state |
| Generic "so we can swap it later" | One concrete implementation; abstract at the second real use | A boundary you must fake in tests today |

A note on resource leaks: Rust closes files, sockets and locks when their owner is dropped,
so "forgot to close" is rare. The leaks that do happen are tasks and threads nobody joins,
child processes nobody waits for, temporary files, `Rc` or `Arc` cycles, entries never
removed from a long-lived map, and anything whose clean-up is async and so cannot run in
`Drop`.

### Subtler ones

- **Borrowing by habit.** Lifetimes threaded through a design, or clones hidden inside, only to avoid taking ownership of data the callee keeps anyway. If it is stored, moved to a task or outlives the call, take it owned.
- **Recovery logic keyed on message text.** Retry or fallback chosen by a substring of an error message breaks silently when the wording or a wrapper changes. Match typed variants or a retryability method.
- **The kitchen-sink error enum.** One public enum with a variant per dependency and a catch-all string. Callers cannot tell what is actionable, and every internal change is an API change. Use errors local to each boundary, expressed in that boundary's terms.
- **Dependency types in a public API.** A dependency upgrade becomes your breaking change. Wrap them. *Exception:* crates whose purpose is to extend that dependency, and vocabulary crates such as `bytes`, `http` or `serde`.
- **Trait and module sprawl.** Tiny traits and wrappers that exist to look abstract. A seam belongs at a real external or semantic boundary.
- **Accumulator soup.** Nested loops with pushes, flags and branch-specific state. Use an iterator chain or small named helpers. Keep the loop when control flow is heavy (early exits, `?`, several outputs) and the chain would be harder to read.
- **A mutable configuration blob,** patched by many call sites before use, so validity depends on timing. Validate once and hand out a frozen value.
- **A build that works only by folklore:** undocumented features, a remembered toolchain, commands that work only from one directory. Pin the toolchain, keep features additive, and run the gates from the workspace root.
- **Transport types used as domain types.** When handlers, services and storage share one DTO, every layer re-decides what is valid. Convert at the edge.
- **Speculative `unsafe` or lock-free code.** Build the safe version, measure, and only then narrow `unsafe` to the proven hot spot, with a proof plan.
- **"It compiles" offered as proof of behaviour.** The compiler proves memory and thread safety, not logic, liveness, ordering or performance. Each of those needs its own evidence.
- **Hand-edited generated code.** Regeneration discards the edit. Change the schema, the generator configuration or a wrapper module.
- **Broad desktop privilege:** wide filesystem grants, generic shell access, sidecar processes with no owner or health check. Running on the user's own machine is not an exception.
- **Hazards a signature does not show:** a guard kept alive by an iterator or a temporary in a `match` scrutinee; an `Arc` cycle; a new trait method that breaks object safety; a new auto-trait-breaking field (`Rc`, a raw pointer) that silently removes `Send` from a public type.

### Mistakes in applying this list

- **Over-correcting.** Removing every clone, making every `&str` parameter `impl AsRef<str>`, giving every function its own error enum, adding a trait to mock one call. A clone is right when it makes ownership clear and the cost is unmeasured or small. Fix the instance that hurts.
- **Fixing the symptom.** Similar symptoms need opposite fixes: a borrow error may want a clone, a restructured scope, or a different owner. Reproduce the failure in the smallest case, confirm the mechanism, then change the code. Adding a clone, a retry, a lock or a trait before that is guessing.
- **Moving a cost instead of removing it.** A convenience in one function often transfers a panic, an allocation, a queue or a compatibility burden to callers and operators. Ask who pays now.
- **The unnamed shortcut.** A design that deliberately avoids a tempting default (a clone per call, `Arc<Mutex<_>>` around everything, `Box<dyn Error>` in a public API) says so at the boundary. Otherwise the next change puts it back.
<!-- essentials:end -->

<!-- core:begin -->
## Working rules shared by every Rust skill

This block is the same in every Rust skill. It covers how to work, the gates, and what
"done" means. Where the repository you are in has its own convention or gate, that wins.

**If nothing else is in reach:**

1. **Say what "correct" means before writing code,** in terms something can check.
2. **Put invariants in types** where that is cheap, and in tests where it is not.
3. **Make ownership, errors, cancellation and shutdown deliberate.** Each should be a decision someone can point to.
4. **Bound everything that can grow:** queues, buffers, retries, recursion, waits, output.
5. **Treat everything from outside the process as untrusted** until it has been parsed into a type that cannot hold the invalid form.
6. **Measure before optimising, and state the method with the number.**
7. **Follow the repository you are in** over any general convention, this skill included.
8. **Report what you ran and what you saw.** Unverified is a legitimate status; passing it off as verified is not.

### Size the process to the task

| Task | Process that fits |
|---|---|
| Rename, comment, one-line fix covered by an existing test | Read the code and its callers, change it, run the gates |
| Bug fix | Reproduce it with a failing test, fix, run the gates |
| Feature inside one module | A short list of checkable requirements, tests first, implement |
| New public API, a change that crosses a boundary, concurrency, unsafe | Requirements, design of types and boundaries, a chosen test mix, then code |

Process heavier than the task buries the change the reviewer has to check. Process lighter
than the task is how a "small" change to an error type or a lock ships a regression.

### Working with the compiler and the ecosystem

- **Fix the first error first.** Later errors are often cascades. Read the whole message, including the `help:` and `note:` lines. Run `cargo check` after each small edit, not after three hundred lines.
- **A borrow-checker error is design information.** Before adding `.clone()`, `Rc<RefCell<_>>`, `Arc<Mutex<_>>` or `'static` to make it compile, say who owns the value and how long the borrow must live. A clone is fine when the value is small or the path is cold; it is wrong when it silently forks state that was meant to be shared.
- **Never guess an API.** Find the version in `Cargo.lock`, then read the documentation for that version or the source under `~/.cargo/registry/src`. Widely used crates change shape between major versions, and code remembered from one version fails on another.
- **Check the edition and the minimum Rust version** (`edition` and `rust-version` in `Cargo.toml`) before using a newer language feature.
- **Match the codebase.** Use its error crate, runtime, logging, naming and module layout. A second way of doing the same thing is a cost every later reader pays.
- **Keep the diff to the task.** No drive-by reformatting, renames or dependency upgrades. Report what you noticed; do not fix it uninvited.
- **Add a dependency deliberately.** Check that std or an existing dependency does not already do it, look at maintenance and licence, enable only the features needed, and say in the handover that you added it.
- **Read before you write.** Read the function you change, its callers and its tests.
- **A red test must be red for the right reason:** it fails on the assertion, not on a compile error or a set-up mistake.
- **Debug in a loop with a stop condition.** Reduce to the smallest reproduction, test one hypothesis per probe, and stop when a regression test fails for the confirmed cause. A plausible story is not a diagnosis.

### What the compiler does not prove

- It proves memory and type properties. It proves nothing about domain correctness, performance, cancellation behaviour or compatibility.
- Code that compiles with clones everywhere has not shown the clones are right.
- No data race does not mean no logical race: check-then-act across two lock acquisitions, dropped work and stale reads all compile.

### The required gates

Cheapest first, so the fastest check fails first:

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-targets --all-features
cargo test --workspace --doc --all-features
```

- **Use the repository's own gate if it has one** (a `just` or `make` target, a CI script). These commands are the default when there is none.
- **`--all-targets` does not run doc tests.** They need the separate `--doc` run.
- **Clippy without `-D warnings` is not the gate.** It prints and passes.
- **`--all-features` is wrong for crates with mutually exclusive features.** Test the supported combinations explicitly.
- Run from the workspace root you mean. A command run in one member checks that member only.
- **A zero exit code can hide tests that did not run.** Read the count: how many ran, how many were ignored or filtered out.

Run a heavier gate when the change touches its risk, and say so when you skip one:

| Gate | Run it when |
|---|---|
| `cargo test --release` | Behaviour could differ with optimisation: overflow checks, `debug_assert`, timing, unsafe code |
| `cargo +nightly miri test` | Unsafe code changed |
| `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps` | Public items or documentation changed |
| `cargo deny check` or `cargo audit` | Dependencies changed |
| `cargo semver-checks` | A published library's public interface changed |
| Benchmarks against a baseline | A performance claim is made, or a hot path changed |

### Before claiming done

1. Identify the command that would prove the claim.
2. Run it fresh and in full, after the last edit.
3. Read the output and the exit status.
4. Report what happened, and only then say done or not done.

- **"It compiles" is not done.** Done is: the required gates green on the final code, and the claimed behaviour covered by tests.
- **If you could not run a command, say so and list it for a human.** Never report an unrun command as passed, and never describe output you did not see. "Skipped" is not "passed".
- **Do not weaken a check to make it pass:** no deleted or `#[ignore]`d test, no loosened assertion, no blanket `#[allow]`, no special case for the test's input. If a test is wrong, say so and fix the test as its own visible change.
- **Before handoff, search your own diff** for `todo!()`, `unimplemented!()`, `dbg!`, stray `println!`, commented-out code and placeholder `TODO` markers.
- **Never invent an identifier, a number or a citation** to satisfy a checklist. If an item does not apply, say why.
- **No secret reaches a log, an error message or a `Debug` output.** No compiler checks this; look at debug, error and crash paths.

**The record at handoff:** the commands run, their results and the toolchain version;
which heavier gates ran or were skipped, with the reason; what was verified by test, what
by reading, and what not at all; known limitations and anything left for a human.
<!-- core:end -->
