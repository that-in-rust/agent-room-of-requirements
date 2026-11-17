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
- **It is complete on its own.** The Rust working rules, the gate commands and the definition of done are at the end, and they apply to every task here.

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
