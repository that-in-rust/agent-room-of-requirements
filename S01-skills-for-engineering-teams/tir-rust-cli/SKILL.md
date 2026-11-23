---
name: tir-rust-cli
description: Self-contained guide for command-line Rust - binaries, developer tools, batch jobs, cargo subcommands and tools that other programs or agents drive. Use when the task touches argument parsing (`clap`), `main.rs`, exit codes, stdout and stderr, configuration files and environment variables, file discovery and traversal, reading and writing files, running child processes, progress and terminal output, or packaging a binary. Not for long-running network services, desktop apps, or the internals of a parser or index the tool happens to contain.
---

# Rust for command-line tools

A command-line tool is judged at its edges: what it prints, where it prints it, what it
exits with, and what it does with the inputs real machines hold. Its defects are a
diagnostic on stdout that corrupts a pipe, a panic on a non-UTF-8 path, a hang on a child
process, a half-written file after Ctrl-C, output that changes order between runs, and a
configuration typo silently ignored.

## When to use this skill

- **Use it when** the change touches a binary's arguments, output, exit status, configuration, file handling or the processes it starts.
- **Signals:** `src/main.rs` or `src/bin/`, `clap`, `std::process`, `ExitCode`, `walkdir` or `ignore`, a `cargo-*` binary name.
- **Skip it for** a network service (the application-service skill), a Tauri application, and the hot core of a parser or indexer the tool wraps (the infra skill).
- **It is complete on its own.** The Rust essentials, the gate commands and the definition of done are at the end.

## The defaults, in priority order

If unsure what matters most, work down the list.

1. **User-visible behaviour is a written contract:** data on stdout, diagnostics and logs on stderr, documented exit codes. A program that speaks a protocol on stdout prints nothing else there.
2. **`main.rs` is thin.** It parses arguments, calls a `run` function that takes its inputs as parameters, and maps the result to an `ExitCode`. The core never reads `std::env::args()` or the environment itself.
3. **Errors are ones a user can act on:** the path, the line, what was expected, what to do next. No panic on anything a user can type or a file can contain.
4. **Real inputs are handled:** non-UTF-8 paths and arguments (`Path`, `OsStr`), files larger than memory, an empty input, a closed pipe (exit quietly), no terminal (no colour or progress bars when piped).
5. **Configuration is resolved once at start-up:** flag, then environment variable, then file, then default, validated into one typed value. A broken configuration file is an error that names the file.
6. **Output is deterministic.** Sort what a parallel walk or a `HashMap` produced before printing or hashing it.
7. **Child processes run without a shell,** with a timeout, both pipes drained and the child reaped.
8. **Files are written atomically,** and traversal does not follow links unless asked.
9. **Tests run the real binary** and assert on stdout, stderr and the exit code; large outputs are snapshot tests.
10. **Threads before async.** A tool that reads files and runs to completion is usually simpler and as fast with threads or `rayon`.

**How this kind of Rust differs from service Rust.** `anyhow` with context at the top is
the norm, and cloning is not a concern. There is no operator and no log pipeline: the
message printed at the moment of failure is the only diagnostic the user gets, so it must
be complete on its own. And the tool runs on machines you have never seen, so paths,
encodings, terminals and platforms are inputs, not assumptions.

## Dependencies, resources and real inputs

**Depend on the trait, not the concrete adapter.**

```rust
// Bad: the component can only ever be built with a real database and a real watcher.
pub struct Indexer {
    database: SqliteConnection,
    watcher: NotifyWatcher,
}

// Good: the dependencies are parameters.
pub struct Indexer<D, W> {
    database: D,
    watcher: W,
}

impl<D: Database, W: FileWatcher> Indexer<D, W> {
    pub fn new(database: D, watcher: W) -> Self {
        Self { database, watcher }
    }
}

pub type ProductionIndexer = Indexer<SqliteDatabase, NotifyFileWatcher>;
```

- **Bounds go on the `impl`, not on the struct definition.** A bound on the struct must be repeated on every `impl` and every function that mentions the type. Put it on the struct only when a field's type or the `Drop` impl needs it.
- **Ask for `Send + Sync` where it is needed** (the function that spawns), not on every type by reflex.
- **Wrap in `Arc` only what is shared.** A component with a single owner holds its dependencies by value.
- **Two or three type parameters is the practical ceiling.** Beyond that, signatures and error messages become unreadable; switch to `Arc<dyn Trait>` fields, or group the dependencies behind one context trait.

**Resources are released by RAII, with an explicit path for teardown that can fail.**

```rust
pub struct Session {
    connection: Option<Connection>,
}

impl Session {
    /// Flushes and closes. Call this on the normal path; it reports failure.
    pub fn close(mut self) -> Result<(), CloseError> {
        match self.connection.take() {
            Some(connection) => connection.close(),
            None => Ok(()),
        }
    }
}

impl Drop for Session {
    fn drop(&mut self) {
        // Fallback for early returns and panics: best effort, never panics.
        if let Some(connection) = self.connection.take() {
            if let Err(error) = connection.close() {
                tracing::warn!(%error, "session dropped without close(); close failed");
            }
        }
    }
}
```

- `Option::take` lets `close(self)` and `Drop` share the resource without closing it twice.
- **Drop order is part of the design.** Struct fields drop in declaration order; local variables drop in reverse order of declaration. If the pool must outlive the workers that use it, declare the workers first, or shut down explicitly.
- A guard whose only job is cleanup is bound to a name (`let _guard = ...`), never to `_`.
- *Anti-patterns:* a `Drop` that blocks on a network call or joins a thread with no timeout; a `Drop` that panics (a panic during unwinding aborts the process); async cleanup attempted in `Drop` by spawning a task nobody waits for; `mem::forget` used to skip cleanup.

**Model the input you will really receive.** A type sketched from the simplest example breaks
on the first real file.

```rust
// Sketch: fine until a generic, async or pub(crate) function shows up.
pub struct Function {
    pub name: String,
    pub signature: String,
}

// Model: every part a requirement reads has a field with a type.
pub struct Function {
    pub name: Ident,
    pub visibility: Visibility,
    pub generics: Option<GenericParams>,
    pub where_clause: Option<WhereClause>,
    pub is_async: bool,
    pub signature: Signature,
}
```

- **Test against samples taken from real code,** including the awkward ones: nested generics, `where` clauses, attributes, macros, unusual whitespace, non-ASCII identifiers.
- **Model what a requirement uses, and be explicit about the rest.** Either keep the unparsed remainder (a span or the raw text) or return an "unsupported" error. Never drop it silently, because a quietly incomplete result is worse than a failure.
- *Skip the full model when* the tool needs one fact (a name, a count). Extract that fact, and still test it against the awkward samples.

## Modules and the shape of a binary

- **A module has one reason to exist** and a name that states it. `utils`, `common` and `misc` are where unrelated code goes to be forgotten.
- **Name what the crate root exports.** Write named re-exports (`pub use counter::{LineStats, count_file};`), so the public API is readable in one place and an internal addition cannot leak. A glob re-export is acceptable only for a deliberate prelude.
- **Default to private.** `pub(crate)` for what the crate shares internally; `pub` is a promise.
- **Binary orchestration is not library API.** Argument handling and the main flow live in the binary or in private modules. `main.rs` parses, calls the library and maps the result to an exit code.
- **One module per subcommand** in a CLI, under `commands/`, with the parent module only declaring them.
- Split a file when it holds two things that change for different reasons, not at a line count.

## Command-line shapes

**A verification runner records skipped steps as skipped.** Step order encodes dependency
(format, lint, types, tests), cheapest first. When a step fails, later ones do not run and
are reported with the reason, so a summary never shows a step as missing or as passed.

```rust
pub enum StepStatus {
    Pass,
    Fail,
    Skipped { reason: String },
}
```

- Tool output is parsed into a typed result. Status is an enum, never a string compared by text.
- **"Skipped" is not "passed".** A report with skipped steps is not a green report, and must not be summarised as one.
- Stopping early hides unrelated later failures. Offer a keep-going mode for when a complete inventory is wanted.

**A generate, validate, retry loop keeps its state in one typed struct:** attempt count,
limit, last validation result and error history. The retry decision is a pure function of
that state, so it can be tested without running the generator.

- **Bound the history.** An append-only error log grows without limit, anchors a model on its earlier failures, and can carry secrets from tool output back into prompts.
- **Stop when attempts stop making progress,** not only at the limit: the same validation error twice in a row is a reason to give up or change approach.
- Isolate attempts (a fresh copy of the workspace) when a failed attempt could leave damage behind.

**Run the expensive fallback only when the cheap pass is measurably weak.** A wider search,
a second model call or a slower algorithm runs when the first result falls below a named
threshold, so the common case pays nothing.

```rust
const SEARCH_LIMIT: usize = 10;
const MINIMUM_RESULTS: usize = SEARCH_LIMIT / 2;

let mut results = self.search(&query, SEARCH_LIMIT).await?;
if results.len() < MINIMUM_RESULTS {
    tracing::debug!(found = results.len(), "first pass weak; widening search");
    results.extend(self.widened_search(&query, SEARCH_LIMIT).await?);
    dedup_and_sort(&mut results);
}
```

- The threshold is a named constant, the fallback is logged, and merged results are deduplicated and ordered deterministically.
- Not for exact lookups or security-sensitive searches, where a looser second pass adds false positives.

**Degradation under a size budget has named modes:** the full content if it fits, otherwise
a compressed form, otherwise a listing of what was left out. Log the mode taken and tell
the consumer what was omitted. Never cut raw text blindly, and cut at a line or item
boundary. Where an omission would be unsafe (compliance, legal, safety review), stop
instead of pruning.

**Command-line and tooling shapes.**

- **Resolve configuration once, at start-up:** flag, then environment variable, then file, then default, validated together into one typed value. Nothing below that boundary reads the environment. Secrets are masked in any printed summary.
- **Offer a parse entry point that does not exit:** `try_parse_from(args)` returns an error where `parse()` would end the process, so argument handling is testable.
- **Sibling subcommands that share options embed one struct** with `#[command(flatten)]`.
- **A `cargo foo` subcommand** is a binary named `cargo-foo` whose parser expects `foo` as its first argument, since Cargo passes it along. Set `bin_name = "cargo"` so help reads correctly, and forward everything after `--` with a trailing `#[arg(last = true)] Vec<String>`.
- **Get build outputs from Cargo's JSON messages** (`--message-format=json` read with `cargo_metadata::Message::parse_stream`), not by guessing paths under `target`. Check the exit status after reading the stream.
- **A bad log-level setting never stops the program.** Print one line to stderr and use the default.
- **Libraries do not print progress.** They take a callback or a writer; the binary decides whether there is a terminal.
- **Validate a directory layout once.** A tool that needs a particular folder structure checks it at start-up into one value, with errors that name the path. Later code takes that value and does no existence checks of its own.
- **A path that will be written and a path that must exist are different types** after validation, and the writable one owns its clean-up. Errors show the path as the user typed it.
- **Paths handed to other programs on Windows:** `std::fs::canonicalize` returns extended-length paths (`\\?\C:\...`) that many tools reject. Use `dunce::canonicalize` for paths passed to a child process, written to a generated file or shown to a user.
- **A batch tool that parses source on a thread pool sets the worker stack size explicitly,** since deeply nested input overflows the default. The binary builds the global Rayon pool once, before any parallel work. **A library never configures the global pool.**
- **Syntax-level metrics with `syn::visit`** suit counting and risk scouting (unsafe blocks, nesting). Anything that needs types, macro expansion or borrow facts needs the compiler; say which the tool is.
- **Findings are printed as labelled source snippets** with a bounded context window, clamped at both ends of the file. Snapshot a finding at the first line and at the last.
- **One model, two outputs.** A generator that writes a human document and a machine-readable file renders both from one validated, sorted model.
- **Generated files are checked in CI:** run each generator and fail if the working tree differs.
- **Binding crates forward.** A Python or Node binding holds no behaviour of its own, and its smoke test uses the same fixtures as the Rust tests.
- **A plugin checks the host's version** against the range it was built for, and warns clearly on a mismatch instead of failing obscurely later.

## Configuration

**Configuration discovery is one function returning an ordered list,** project-local before
the user directory.

```rust
pub fn discover() -> Result<Option<Self>, ConfigError> {
    for path in config_search_paths() {
        match fs::read_to_string(&path) {
            Ok(text) => {
                return Self::parse(&text)
                    .map(Some)
                    .map_err(|source| ConfigError::Parse { path, source });
            }
            Err(error) if error.kind() == io::ErrorKind::NotFound => continue,
            Err(source) => return Err(ConfigError::Read { path, source }),
        }
    }
    Ok(None)
}
```

- **The first file found wins, and a broken one is an error naming its path.** It never falls through to the next file or to defaults: the user would run with settings they did not write.
- Read and match on `NotFound`, as above. An `exists()` check followed by a read is a race, and it treats "permission denied" as "absent".
- `Ok(None)` means no configuration. Using defaults is then the caller's deliberate choice.
- A search up parent directories has a depth limit.
- *Skip discovery entirely* where security or reproducibility matters: take an explicit path.

**A relative path in a configuration file is relative to that file,** not to the working
directory. The single load function records the file's directory, and every path field is
read through a resolver.

```rust
impl AppConfig {
    pub fn load(path: &Path) -> Result<Self, ConfigError> {
        let mut config: AppConfig = parse(&fs::read_to_string(path)?)?;
        config.base_dir = path.parent().unwrap_or(Path::new(".")).to_path_buf();
        Ok(config)
    }

    pub fn auth_env_file(&self) -> Option<PathBuf> {
        let path = Path::new(self.auth.env_file.as_deref()?);
        Some(if path.is_absolute() { path.to_path_buf() } else { self.base_dir.join(path) })
    }
}
```

- `base_dir` is private and skipped by serde. Do not derive `Default` on such a type: an empty base directory resolves silently against the working directory.

**User-edited configuration reports typos with their path.** Collect unknown keys with the
full path, and make a type error name the field.

```rust
let mut unknown = Vec::new();
let deserializer = serde_ignored::Deserializer::new(value, |path| unknown.push(path.to_string()));
let settings: Settings = serde_path_to_error::deserialize(deserializer)?; // error names the path
if !unknown.is_empty() {
    return Err(ConfigError::UnknownKeys(unknown));
}
```

- *Not when* a file written for a newer version must still load. Then warn about unknown keys and keep going.

**A setting is a typed key** carrying its name, description, default and parser, read
through one getter that applies precedence: explicit value, environment, default.

```rust
pub struct Setting<T> {
    pub key: &'static str,
    pub description: &'static str,
    pub default: fn() -> T,
    pub parse: fn(&str) -> Result<T, SettingError>,
}
```

- **A value that fails to parse is an error naming the key and the value.** Falling back to the default silently means the operator's setting is ignored and nobody knows.
- The one tolerable exception is a pure tuning knob, and even that logs a warning.

**A knob read on a hot path is parsed once** into a `OnceLock` or `LazyLock`. Put the
parsing in a pure function that tests call directly, since the cell cannot be reset.

```rust
fn parse_budget(raw: Option<&str>) -> usize {
    raw.map(str::trim)
        .and_then(|text| text.parse::<usize>().ok())
        .filter(|budget| *budget > 0)
        .unwrap_or(DEFAULT_BUDGET)
}
```

- **Tests do not mutate the process environment.** `std::env::set_var` is `unsafe` from edition 2024 and races with other test threads. Pass the value in.
- Not for configuration that must change while the process runs.

**Ambient state.**

- **Avoid thread-local context in async code;** a task moves between threads. Pass the handle, or use `tokio::task_local!`.
- **A temporary override restores the exact previous value in `Drop`,** not a default, so nested overrides unwind correctly. Offer it as one function taking a closure, and test nesting.

## Errors at external edges

**Only "not found" selects the defaults.** A loader for an optional file opens it and matches
on the error kind. Do not test `exists()` first: the file can change between the check and
the read, and a permission error would be treated as absence.

```rust
fn load_rules(path: &Path) -> Result<Rules, LoadError> {
    match fs::read_to_string(path) {
        Ok(text) => Rules::parse(&text).map_err(LoadError::Parse),
        Err(error) if error.kind() == io::ErrorKind::NotFound => Ok(Rules::default()),
        Err(error) => Err(LoadError::Read(error)),
    }
}
```

- **A corrupt store is not an empty store.** A reader that returns "empty" for both a missing file and one that fails to parse lets the next write destroy the data. Absent means empty; unparsable is an error, or the file is moved aside before anything is written.
- **A reloaded configuration that fails to parse leaves the last good one in force.** Parse and validate fully, then swap; on failure, log and keep serving.
- Reading and parsing are two functions, so the parser is tested without a file system.

**Smaller rules.**

- **HTTP client: status first, then a typed decode, then a bounded snippet.** Check the status before treating the body as data. If decoding fails, the error carries the status and a length-capped piece of the body, never the whole payload and never an untyped value.
- **Read the OS error immediately.** After a failing libc or FFI call, `io::Error::last_os_error()` goes on the very next line, before any other call can overwrite `errno`.
- **A status variable assigned along the way starts as failure,** so an early return cannot report success.
- **A missing optional capability is a typed state.** Do not catch a load failure at start-up, print a warning and leave a `None` that every later use must check. Gate it with a Cargo feature, or return an explicit "unsupported" error when it is used.
- **A failure says how far it got** when that helps the caller: `CycleDetected { processed }`, `Truncated { read, expected }`.
- **A message takes its limit from the constant.** Format `MAX_SIZE` into the text; a literal "4 GB" beside the constant goes stale.
- **A structured variant, not a static string.** `InvalidInput { field, reason }` can name the offending value; `Invalid(&'static str)` cannot. A catch-all `Other(String)` belongs at an application edge, not in a library's public enum.
- **An error sent to a user interface has a short message and a separate detail,** so the UI can show a title and an expandable cause.
- **Distinct misses get distinct codes.** In a routed or distributed service, "no such resource", "not the leader" and "lease expired" lead a client to different actions (fail, re-route, retry), so they are different codes.
- **A drop-in replacement keeps the original's error contract:** the codes, the structured fields and any wording that callers are known to match on.
- **Three-valued logic is `Option` and `?`.** Write the inner computation to return `Option<T>` so a null operand short-circuits, and convert to the public error type in an outer function.

## Untrusted input: paths, commands and data

These apply to any Rust program that takes input from outside, not only to web services.

**Server-side fetch of a user-supplied URL.** One `validate_url` runs before every such
fetch.

- Allow only `http` and `https`. Reject loopback, private, link-local and cloud-metadata addresses, and internal hostnames.
- **Checking the hostname is not enough.** Resolve it, check the address, and connect to the address you checked, so a second DNS answer cannot differ.
- Validate every redirect the same way, or disable redirects. Cap the response size and set a timeout.
- Test IPv4, IPv6, IPv4-mapped IPv6 (`::ffff:127.0.0.1`), and decimal or octal spellings of an address.
- An intranet exception is an explicit allow-list, not a weaker default.

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

**Recursive walkers use no-follow calls.** `Path::exists` and `fs::metadata` follow links,
so a walker using them can loop forever or leave the tree. Use `fs::symlink_metadata`.

```rust
pub fn is_symlink_or_junction(path: &Path) -> bool {
    let Ok(meta) = fs::symlink_metadata(path) else { return false };
    if meta.file_type().is_symlink() {
        return true;
    }
    #[cfg(windows)]
    {
        use std::os::windows::fs::MetadataExt;
        const FILE_ATTRIBUTE_REPARSE_POINT: u32 = 0x400;
        if meta.file_attributes() & FILE_ATTRIBUTE_REPARSE_POINT != 0 {
            return true;
        }
    }
    false
}
```

- Windows junctions are reparse points, not symlinks, so check both.
- Following links is an opt-in mode with cycle detection.

**Deserialising across a trust boundary.** Use a closed schema: named fields, closed enums,
`#[serde(deny_unknown_fields)]` where an unknown field signals a mistake, and limits on
size and nesting depth. Never let untrusted input choose which type gets constructed.

**Running commands.**

- **Use `Command` with a program and separate arguments. No shell.** Arguments passed this way are not re-parsed, which removes injection at its source.
- An argument beginning with `-` can still be read as an option. Put `--` before data-derived positional arguments where the program supports it.
- **Do not pass credentials as arguments;** they appear in process listings. Use the environment, standard input or a file with restricted permissions.
- Success is the exit status or structured output, not a phrase in the text. A failed write to the child's standard input is an error.
- If shell text must be accepted, parsing it against an allow-list of programs and rejecting redirects and subshells lowers the risk. It does not make arbitrary shell text safe; say so.

**User-supplied expressions** (formulas, filters) are parsed into a syntax tree, validated
recursively against an allow-list of node kinds, operators, functions and variable names,
then evaluated in a constrained scope, with limits on depth and cost. Never hand one to a
general evaluator. An unknown name gets an error with a close-match suggestion.

**Embedding one query language in another.** Where a position cannot take a bound
parameter:

- Validate identifiers against a strict pattern such as `^[A-Za-z_][A-Za-z0-9_]*$` and reject everything else.
- Quote a free-form body with a delimiter proven absent from it. Never assume a delimiter cannot occur.
- Prefer real bind parameters wherever the driver allows them.

**Authorisation before the body.** On an upload or import route, the authorisation check
runs before anything buffers the body or spools it to disk.

- In Actix, extractors run in parameter order: put the authorising extractor first and leave a comment saying why.
- In Axum, the body extractor must be last anyway; authorise in an earlier extractor or in middleware.
- Test that an unauthorised upload creates no temporary file.

**Untrusted commands and repository configuration.** A bot, webhook handler or agent bridge
dispatches through a static table (an enum and a `match`), never by loading something named
by the input.

- **Configuration found in a repository is untrusted.** It cannot set host-only keys: secrets, filesystem paths, endpoints, the commands to run.
- Security-relevant settings are refused on the command line with a pointer to the host configuration.

**Text handed to a model or agent** passes a policy step between retrieval and
presentation: exclude by path (`.env`, `*.pem`, `*.key`, `id_rsa`), replace secret-shaped
text with a marker, and report how many items were excluded. Pattern scans miss unusual
secrets, so treat this as reduction, not a guarantee.

**Secret carriers are wiped on drop.** A struct holding key material derives
`ZeroizeOnDrop`.

```rust
#[derive(Zeroize, ZeroizeOnDrop)]
pub struct Pkcs12Archive {
    der: Vec<u8>,
    passphrase: String,
}
```

- An `into_parts()` that moves the fields out hands the duty to the caller, and says so.
- **Wiping is best effort.** It does not reach copies made by a reallocating `Vec`, a clone, a log line, or a library that kept its own buffer. Do not claim more.

**Authorisation data is indexed by the questions asked.** For hot-path checks, keep maps
shaped like the questions (`HashMap<(UserId, StreamId), Permissions>`), so a check is a
lookup or two. Every update and delete path maintains every derived set. Test that a
revoked permission is denied: a stale allow is the dangerous failure.

**State the level of evidence behind a security claim.** Documented is not configured;
configured is not reachable; tested is not deployed; observed once is not attacker-proof.
Compilation proves no authorisation property. After a framework upgrade or an advisory,
re-check behaviour against the locked version and rerun the abuse tests.

## Running other programs

**A timed child process, without pipe deadlock.** A parent that waits for exit before
reading the child's output deadlocks as soon as the child fills a pipe buffer. Drain both
pipes while waiting.

```rust
use std::io::Read;
use std::process::{Command, Stdio};
use wait_timeout::ChildExt;                       // adds wait_timeout to std's Child

pub enum TimedOutput {
    Finished { status: ExitStatus, stdout: Vec<u8>, stderr: Vec<u8> },
    TimedOut { stdout: Vec<u8>, stderr: Vec<u8> },
}

fn drain(pipe: Option<impl Read + Send + 'static>, cap: u64) -> JoinHandle<Vec<u8>> {
    std::thread::spawn(move || {
        let mut kept = Vec::new();
        if let Some(pipe) = pipe {
            let mut limited = pipe.take(cap);
            let _ = limited.read_to_end(&mut kept);
            // Keep reading and discarding, so a noisy child never blocks on a full pipe.
            let _ = std::io::copy(&mut limited.into_inner(), &mut std::io::sink());
        }
        kept
    })
}

pub fn run_with_timeout(mut command: Command, timeout: Duration) -> io::Result<TimedOutput> {
    let mut child = command
        .stdin(Stdio::null())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()?;
    let stdout = drain(child.stdout.take(), OUTPUT_CAP_BYTES);
    let stderr = drain(child.stderr.take(), OUTPUT_CAP_BYTES);

    let status = match child.wait_timeout(timeout)? {
        Some(status) => Some(status),
        None => {
            let _ = child.kill();
            let _ = child.wait();                 // reap it, or it stays a zombie
            None
        }
    };
    let stdout = stdout.join().unwrap_or_default();
    let stderr = stderr.join().unwrap_or_default();
    Ok(match status {
        Some(status) => TimedOutput::Finished { status, stdout, stderr },
        None => TimedOutput::TimedOut { stdout, stderr },
    })
}
```

- **One wrapper owns the child's lifecycle and pipes.** Every external command goes through it.
- **A timeout is data, with the partial output kept.** After the deadline: kill, then wait.
- **Cap what is captured, and keep draining past the cap.** Stopping the read at the cap brings the deadlock back.
- **Give the child no terminal input** (`Stdio::null()`) unless it needs some. A tool that prompts would otherwise hang until the deadline.
- **Killing the child does not kill its children.** A grandchild that inherited the pipes keeps them open, and the drain threads never finish. Where the tool spawns its own processes, put it in a process group (Unix) or a job object (Windows) and kill the group.
- In async code, `tokio::process::Command` with `kill_on_drop(true)` and `tokio::time::timeout` around `wait_with_output` does the same job, with the same grandchild caveat.
- Test: a timeout, a non-zero exit, and output larger than the pipe buffer on both streams.
- This is for run-to-completion tools. Interactive and long-lived children need a supervisor that owns start-up, health checks, restarts and shutdown.

**When a child's stdio is a protocol transport,** stdout carries framed messages only and
stderr carries its logs.

- Deny `clippy::print_stdout` in that crate, and point the logger at stderr.
- Each direction (stdin writer, stdout reader, stderr reader) is its own task or thread. Reading stderr is not optional: an unread stderr pipe fills and blocks the child.
- Use a socket or a named pipe when stdout must stay user-facing.

**Classify a failure before retrying it.** Automation that retries CI or a flaky command
decides first whether the failure is transient, and **deterministic is the default.**

```rust
const MAX_CLASSIFY_INPUT_SIZE: usize = 1024 * 1024;

pub fn classify_failure(output: &str) -> FlakeClassification {
    let mut end = output.len().min(MAX_CLASSIFY_INPUT_SIZE);
    while !output.is_char_boundary(end) {
        end -= 1;                 // slicing inside a multi-byte character panics
    }
    for line in output[..end].lines() {
        let line = line.trim().to_lowercase();
        if line.contains("eaddrinuse") || line.contains("address already in use") {
            return FlakeClassification::Transient {
                category: FlakeCategory::PortConflict,
                matched_line: line,
            };
        }
    }
    FlakeClassification::Deterministic
}
```

- **Only a named transient category retries,** under a capped policy, and each retry is logged with the line that matched.
- Each category has a positive fixture and a near-miss negative one.
- **Count the retries and review them.** A category that fires weekly is a defect to fix, not a flake to absorb. A test that fails because of a real race is not "transient".
- Do not add a classifier before the failure kinds are understood. It hides regressions.
- The boundary loop above is the general rule for cutting a `str` at a byte limit. `str::floor_char_boundary` does it in one call on toolchains where it is stable.

**Integration metadata lives in one table.** Identifiers, aliases, credential environment
keys and defaults for each provider are one `const` table, not conditionals spread through
the code.

```rust
pub struct ProviderMetadata {
    pub canonical_id: &'static str,
    pub aliases: &'static [&'static str],
    pub auth_env_keys: &'static [&'static str],
    pub routing_defaults: Option<ProviderRoutingDefaults>,
}

pub const PROVIDER_METADATA: &[ProviderMetadata] = &[/* one entry per provider */];
```

- Adding an integration starts with its entry. A test checks that identifiers and aliases are unique across the table.
- A static table suits a set known at build time. It does not suit plugins registered at run time, or data that changes faster than releases.

**Telemetry names are an interface.** Attribute keys, metric names and propagation header
names that cross crates, or that a dashboard or alert reads, are constants in one module.

```rust
pub mod attribute {
    pub const RETRY_ATTEMPT: &str = "retry.attempt";
    pub const JOB_ID: &str = "execution.job.id";
    pub const SESSION_ID: &str = "session.id";
}
```

- **Renaming one breaks dashboards and alerts silently.** Treat a rename as a breaking change.
- Search the module before adding a key. Follow an existing convention (OpenTelemetry's semantic conventions) where one covers the concept.
- One-off debug labels stay local. Give the module naming rules and an owner, or it becomes a dumping ground.

**Resolve resource locations before entering a sandbox.** Resolve and cache the paths the
process needs before dropping privileges, and derive the sandbox's access list from the
same function. A new location then cannot be added to one and forgotten in the other.
Development-only fallbacks, such as searching the working directory, are compiled out or
guarded in production.

**Smaller rules from editing and analysis tools.**

- **After an automated edit, confirm structurally that the intended item changed and report every unexpected one.** Pair this with a build or tests: structure does not prove behaviour.
- **A scanner layers its ignore rules in a documented order** (built-in defaults, the tool's ignore file, the project's; `ignore::WalkBuilder`), reports which are active, and offers an explicit include override for audits.
- **A repair pass at an ingestion boundary returns counts and reasons** for what it normalised or dropped. It does not hide a violation that should fail.
- **Read parse-tree children by field name, not by position** (`node.child_by_field_name("name")`). Positions change when the grammar adds an optional child.
- **Dense per-character metadata over a large text is stored as runs,** not one object per character.
- **An excerpt shown to a reader or a model is cut on structure:** whole lines, with the enclosing signature, overlapping ranges merged, in a deterministic order.

## Files: traversal, batches and shared state

**Commit the public interface of a published library as a golden file.** CI regenerates it
(`cargo public-api`), fails with a diff, and one explicit command overwrites it. The diff is
reviewed, never edited by hand. This makes every interface change visible in review,
including accidental ones such as a newly public helper or a changed auto trait. Not worth
it for an application crate nobody links against.

**Build-time registries.** When the source tree already holds the truth (one module per
command, one file per migration), generate the registry in a build script or a derive, and
sort the output so diffs are reviewable. Plugins loaded at run time keep a run-time
registry.

**A build step that produces named artefacts emits metadata for them** (name, source
location, attributes), so later phases select, run and report without re-parsing source or
scraping command output. Selecting by substring surprises when names overlap: keep an exact
mode, and make it the only mode where selection has security consequences.

**Recursive traversal that follows links needs cycle detection.**

- Track the canonical identity of each directory **on the current ancestor path**, and skip one that is already there. Remove it when the directory is finished, so a sibling can still reach a shared target.
- A broken link is skipped with a warning, not an error that ends the walk.
- `walkdir` with `follow_links(true)` detects loops itself; the `ignore` crate builds on it. Prefer them to a hand-written walk.
- **Not following links is the safer default.** Follow them only when the tool's purpose requires it, and then re-check that each resolved path is still inside the allowed root.

**Walk a deep tree with a cursor, not recursion,** when depth is controlled by input.
Recursion over a parse tree of generated or hostile source overflows the stack.

```rust
let mut cursor = root.walk();
'walk: loop {
    visit(cursor.node());
    if cursor.goto_first_child() {
        continue;
    }
    loop {
        if cursor.goto_next_sibling() {
            break;
        }
        if !cursor.goto_parent() {
            break 'walk;                  // back at the node the cursor started from
        }
    }
}
```

- **Node offsets are bytes.** Take text with `&source[node.byte_range()]`, never by skipping that many `chars()`.
- The same applies to your own recursive types: a deeply nested value can overflow the stack in a derived `Drop`, `Debug` or `Clone` as well as in your visitor. Bound the depth at the parser, or use an explicit stack.

**An ordered list of recognisers** ending in a catch-all is a reasonable design for a small
markup or token pipeline. The order is behaviour: a new recogniser goes beside its most
specific competitor, with tests that nothing earlier or later is shadowed. It does not fit
a grammar that needs context or backtracking; use a real parser.

**Fail-fast in a parallel batch carries a typed payload.**

```rust
let outcome = pool.install(|| {
    sorted_units
        .par_iter()
        .enumerate()
        .map(|(index, unit)| {
            let result = check(unit)?;
            if fail_fast && result.failed() {
                Err(BatchStop::FailFast { index, result })
            } else {
                Ok(UnitResult { unit, result })
            }
        })
        .collect::<Result<Vec<_>, BatchStop>>()      // short-circuits
});
```

- **Use a private enum for the early stop,** and convert it to the ordinary result at the orchestrator. That is clearer than hiding the payload in `anyhow` and downcasting, and the stop type never crosses the public interface.
- **Short-circuiting in Rayon is cooperative:** units already running finish, and which failure is reported first is not deterministic. Sort inputs so the *successful* output order is stable, and do not assert on which unit failed first when several can.
- Do not use fail-fast when every failure must be reported, or when units have side effects that must not be half-done.

**Running several actions concurrently.**

- **Run a batch concurrently only when a policy function shows every action in it is read-only.** Otherwise run them serially, in order. An action declares this when registered, and an unknown one is treated as a write.
- **A loop with several ceilings (tokens, turns, time) checks all of them through one gate** at the top of each iteration, before the next expensive call. Stop reasons are distinct variants, so the caller knows whether to retry, resume or ask.
- **A reply from a worker, subprocess or sandbox is an untrusted frame.** Give each request a fresh random token, set it after copying payload fields so the payload cannot overwrite it, and reject a reply whose token is missing or different. The token proves correlation, not correctness: still validate the fields and enforce a timeout.

**Command approval by prefix lists is a convenience, not a security boundary.**

- Reject first any syntax that changes what a command means: command and process substitution, backticks, chaining, redirection, pipes.
- Then resolve by specificity: the longest matching prefix wins; with equal specificity, deny wins; a wildcard allow loses to any deny.
- Test each of those cases. **Prefix matching cannot reason about what an allowed program does with its arguments** (`git -c core.pager=...`, `find -exec`, an interpreter given a script). Real containment comes from running without a shell and inside a sandbox with limited filesystem and network access.

**Updating a small state file shared between processes** is a read-modify-write cycle, so
it needs a lock as well as an atomic write.

1. Take an advisory lock on a separate lock file (`File::lock` on recent toolchains, or the `fs4` / `fd-lock` crates), with bounded retries.
2. Read the current content **after** taking the lock.
3. Write the new content to a uniquely named temporary file in the same directory, and sync it.
4. Rename it over the target. Release the lock.

- **Rename directly over the target.** Moving the old file aside first leaves a moment with no file at all, which a concurrent reader sees as "no state".
- The temporary file is in the same directory because a rename across filesystems is a copy, not an atomic replace.
- **Readers need no lock:** they see the old file or the new one, never a mixture.
- Prefer a lock the operating system releases when the process dies. A lock implemented as "the file exists" needs a stale timeout, and the timeout can steal a lock from a slow but live holder.
- Advisory locks are unreliable on some network filesystems. If several processes update state often, that is the sign to use SQLite.

**Caching results of external calls.**

- **Cache only successful, idempotent, non-personalised responses.** Never cache errors, rate-limit pages or empty results without an explicit, short negative-caching rule.
- The key hashes the endpoint, the operation and the parameters serialised canonically with sorted keys. Decide freshness per operation before caching anything.
- SQLite shared by several processes runs in WAL mode with a busy timeout, and each thread or process has its own connection.

**Many external sessions belong to one owning scope.** Connect on entry, close all on exit
even after a failure, through an explicit async `close()` on every path, with `Drop` only as
a backstop since it cannot await. A clean-up error is logged and never replaces the task's
own error. In a long-running host, surface clean-up errors: swallowed ones hide leaks.

**Staged selection pipelines account for every item.** When candidates pass through
filter, score, deduplicate and pack stages, each stage returns what survived and what it
dropped, with a reason. Test that `included + dropped == total`. Stage order is semantic: a
sensitivity filter that runs after packing has already leaked.

### File discovery, generated text and partial results

**Discover files with the `ignore` crate,** so a tool sees what Git sees by default, and
make the ignore policy an explicit option.

```rust
let (sender, receiver) = crossbeam_channel::unbounded();
builder.git_ignore(options.git_ignore).build_parallel().run(|| {
    let sender = sender.clone();
    Box::new(move |entry| {
        let stop = entry.is_err();
        match sender.send(entry) {
            Ok(()) if !stop => ignore::WalkState::Continue,
            _ => ignore::WalkState::Quit,
        }
    })
});
drop(sender);                                       // or the drain below never ends
let mut entries: Vec<_> = receiver.iter().collect::<Result<_, _>>()?;
entries.sort_by(|a, b| a.path().cmp(b.path()));     // parallel walk order is not deterministic
```

- **The parallel walk only discovers.** Parsing and analysis happen afterwards, on the sorted list.
- **`run` returns only when the walk ends,** so with this shape the channel must be unbounded, or the walkers block on a full channel that nobody is reading. To bound memory on a huge tree, consume from another thread while the walk runs.
- Decide whether one unreadable directory should end the walk, as here, or be reported and skipped. A tool run over a home directory usually wants the second.
- **A security or audit scanner must be able to include ignored files.** Secrets and build outputs live exactly there.
- Test the default, the no-ignore mode, and several roots.

**Overlapping matches are arbitrated by a total order.** When several rules claim byte
ranges of the same source (diagnostics, highlights, suggested fixes), sort by specificity,
then width, then start position, and accept a candidate only if it overlaps nothing already
accepted. A total order makes output independent of rule registration order. A new rule
states what it claims and has an overlap test against a broader neighbour.

**Analysis returns a message key with typed parameters; a catalogue renders the prose.**

- Rule code contains no sentences, so wording changes and translation do not touch analysis, and tests assert on keys, not on text.
- A missing key is a hard error, and a test checks that every key exists in every required catalogue.
- Worth it for a tool with many diagnostics or more than one language. For a small tool, a `Display` implementation on a typed error is the same idea at lower cost.

**A result assembled from several optional sources says when it is partial.**

- Each source is fetched independently. A failing one adds a labelled error, and the rest still return.
- A source is recorded as used only after its data is present. The output shows its errors and provenance, so a partial result never looks complete.
- **Do not return partial output where a missing part changes the meaning:** an authorisation decision, a financial total, a safety check. Fail instead.
- **Trimming to a budget follows an explicit ladder,** ordered by how cheaply a part can be fetched again and how much the decision depends on it, not by section order or size. Items the caller named explicitly are placed first and never trimmed.
- When items are ranked and the rendered size grows with the prefix length, binary-search the longest prefix that fits. Measure with the real tokenizer or byte count, not an estimate.

**A managed block in a file the user also edits** is delimited by stable start and end
markers, and a rerun replaces only that range.

- The operation is idempotent: running the installer twice leaves one block.
- **Handle the damaged cases explicitly:** a start marker with no end, markers in the wrong order, two blocks. Stop and report; do not guess and delete user text.
- Preserve the file's line endings and trailing newline, and write atomically.
- **If the format has a real parser or merge interface, use it** instead of text markers (`toml_edit` keeps comments and layout).

**Generate near-identical variants from one source.** When several consumers need almost
the same declarative text (configuration flavours, query dialects), generate each from one
canonical source through a table of flavours. Adding a flavour is one table entry, never a
copied file. Generated files carry a "do not edit" header, and CI regenerates and fails on a
difference.

**Documented examples are checked.**

- Rust examples in documentation are doc tests; keep them compiling (`no_run` for those that need a network, never `ignore` as a convenience).
- Examples in other documents (a README table of commands and outputs, an API reference) are parsed into the same data a hand-written test uses and run. When a signature changes, the code and the example change together.
- Runnable request examples take the base URL and credentials from a per-environment file that is not committed. They do not replace a regression suite.

**Long multi-step work keeps its state in one durable, readable artefact** with explicit
status fields and a log of what changed and why, not in conversation memory or scattered
notes. A plain text file has weak concurrency: simultaneous writers conflict, so
high-frequency machine coordination needs structured storage with locking.

**A small vocabulary of named combinators before a large grammar.** With `nom`, `winnow` or
`chumsky`, define helpers for the recurring shapes (separated list, delimited form, optional
argument list), so the domain rules read like the grammar. Keep the helpers shallow: they
can hide precedence and recovery behaviour, so forms with unusual recovery stay
hand-written. Each helper has a test with nesting and an ambiguous case.

**Rolling back a multi-file change.** One file is written atomically
(temporary file in the same directory, `write_all`, `sync_all`, rename; sync the parent
directory for stronger crash guarantees). For a batch:

- Every error carries the target path and the I/O source.
- **Record each step as it succeeds, and roll back in reverse order:** remove created files, then restore the saved originals of edited files.
- **Rollback can fail too.** Report which files were restored and which were not; never report a clean rollback that was not verified.
- A batch of renames is not atomic as a whole. If readers must never see a mixed state, write a new directory and switch one pointer (a symlink or a manifest file) at the end.
- Test edits, creates, nested directories, and a failure injected at each step.

## Protocols, logging and operations

**Observability and secrets.**

```rust
#[tracing::instrument(skip(request, state), fields(method = %request.method(), path = %request.uri().path()))]
pub async fn handle(state: AppState, request: Request) -> Result<Response, Error> {
    // ...
}

let api_key = SecretString::from(load_key()?);
tracing::info!(has_key = !api_key.expose_secret().is_empty());   // never the key itself
```

- **`#[instrument]` records every argument with `Debug` unless told otherwise.** Skip bodies, credentials and large values, and name the fields you want. An un-skipped request or config struct is the usual way a secret reaches a log.
- Propagate a trace identifier across service boundaries. A user identifier is personal data: record it only where policy allows.
- **Libraries emit through `tracing` or `log` and never `println!`.** The application chooses where output goes.
- **Do not spread a secret:** no wide cloning, expose it only at the call that needs it, and keep it out of `Debug`, `Display`, errors and panics.

**Processes and protocols.**

- **Protocol on stdout, logs on stderr.** A binary that speaks JSON lines, LSP or a stdio tool protocol never prints diagnostics to stdout, including from dependencies. One stray line corrupts the stream.
- **A detached helper daemon** gets a health check before another is spawned, and stale instances are cleaned up.
- **Every spawned child process and background task is registered in one place,** so shutdown can stop all of them. Handles unregister themselves idempotently (a flag, or `Drop`), and every exit path does it: success, error, cancellation, timeout. Test the cancellation and error exits.
- **A transparent proxy around a subprocess protocol** can add a transcript, timing and policy checks without changing either side, provided it frames messages correctly. A newline or bracket-counting delimiter works only for simple text protocols; it breaks when the delimiter can appear inside a string.
- **A command protocol with many request types:** each request owns its encoding, command code and response type through a trait with an associated `Response`; handling is a separate executor with one method per request, or an exhaustive match. No downcast chains.
- **Fallback ladders have a fixed order and are logged.** When a dependency can come from several places (installed, then vendored, then built), log each step taken and report an unavailable one clearly. An automatic download needs a pinned checksum and a retry limit, and is off in offline and reproducible builds.

**Validation and schemas.**

- **Accumulate issues where a complete list helps:** configuration intake, registries, admin and import tools. Collect field, message and severity, report together, and treat the input as invalid only if an error-severity issue exists. Keep hot paths and security checks fail-fast.
- **One source for the type, the validation and the advertised schema** (for example `serde` with `schemars`), so they cannot drift. Checks the schema cannot express still live in one constructor.
- **A diagnostic log for a local application** is append-only JSON lines with typed entries: timestamp, level, event, error code. Redact on write and again on export, with a test per credential shape. Redaction is a second line of defence, not permission to log secrets.

**Registries, flags and policy.**

- **A command registry rejects a duplicate name or alias at registration,** and is the only place that dispatches on strings. In a first-match table, order is priority: an earlier broad matcher shadows later ones, so test each new matcher with varied case and whitespace. Use this only when the argument parser does not already give you the tree.
- **Audit registered surfaces statically, and fail on duplicates before deduplicating.** Collecting commands, routes or migrations straight into a `HashSet` hides a double registration. Static readers miss run-time registration, which needs its own check.
- **Self-registering plugin lists** (`inventory`, `linkme`, `ctor`) depend on linking and can be dropped by the linker or registered twice. Prefer an explicit list; if you use them, test that every expected plugin is present.
- **Feature flags are read through one helper with a declared default per flag.** A missing key never silently reads as `false`. Each flag has an owner and a removal plan.
- **Several flags combine in one pure function that returns a mode enum.** Call sites match on the mode and never test flags themselves. One flag never silently enables another. Test the combinations.

```rust
fn exec_mode(features: &Features) -> ExecMode {
    match (features.enabled(Feature::Exec), features.enabled(Feature::DirectExec)) {
        (false, _) => ExecMode::Disabled,
        (true, false) => ExecMode::Fork,
        (true, true) => ExecMode::Direct,
    }
}
```

- **Policy that depends on the caller matches exhaustively on a source enum, with no wildcard arm.** A new kind of caller then forces a decision about what it inherits.

```rust
fn hint_for_source<'a>(config: &'a Config, source: &SessionSource) -> Option<&'a str> {
    match source {
        SessionSource::SubAgent(SubAgentSource::ThreadSpawn { .. }) => config.subagent_hint.as_deref(),
        SessionSource::Cli | SessionSource::VSCode | SessionSource::Exec => config.root_hint.as_deref(),
        SessionSource::Internal(_) | SessionSource::SubAgent(_) => None,
    }
}
```

- **Optional telemetry providers are isolated.** Build a list from configuration, log and skip one that fails to construct, fall back to a no-op, and never let one provider's failure break the product or the other providers. High-cardinality values such as query text are opt-in.

**Tools that serve agents or scripts.**

- **A tool that needs a prerequisite (a built index, a login, a migration) fails at once with a structured error naming the next command to run,** instead of hanging or returning empty output. Gate every tool by default and exempt a short, tested allow-list.
- **A loop driven by a model or a search has explicit budgets** (depth, calls, tokens, time) and ends in a typed outcome, including an explicit give-up. It never ends by parsing free text, and an invalid finish is an error, not a success.
- **When a query is rewritten or expanded, keep the original as the baseline** and merge results, so a bad rewrite cannot make results worse than no rewrite.
- **Maintenance scripts discover valid targets from what exists on disk** plus a small alias table, and validate a user-supplied name against that set before touching files or git. That also rejects typos and path traversal.

**Workspace hygiene.**

- Declare dependency versions once at the workspace root; local crates depend on each other by path.
- Keep optional dependencies behind features, and re-export the public interface deliberately from `lib.rs`.
- A shared-types crate is useful when it holds a small, stable vocabulary. One that every crate depends on and everyone edits rebuilds the whole workspace on each change.
- `cargo clean` is a last resort for build errors that make no sense, usually after a toolchain or workspace-configuration change. If it is needed routinely, a build script or cache key is wrong; find it.
- Fuzz targets live in the repository (`cargo fuzz init`, `cargo fuzz add parse`), with a committed seed corpus and every minimised crash kept as a regression test. CI runs each target briefly; long runs are scheduled.

## Threads

**Scoped threads borrow; no `Arc` and no `'static` needed.** Every thread spawned in the
scope is joined before it returns, so borrowing local data is sound.

```rust
let (left, right) = data.split_at_mut(data.len() / 2);
let (sum_left, sum_right) = thread::scope(|scope| {
    let a = scope.spawn(|| process(left));
    let b = scope.spawn(|| process(right));
    (a.join(), b.join())
});
```

- Split mutable data into disjoint parts first (`split_at_mut`, `chunks_mut`); each thread then owns its part exclusively. Do not wrap data in `Arc<Mutex<_>>` only to satisfy a `'static` bound.
- **`join()` returns `Err` if the thread panicked.** Decide what that means: propagate it, or record it. An unjoined, unnamed thread that panics is a silent loss of work.
- For "apply this to every item in parallel", `rayon`'s `par_iter` is less code and balances load. Keep I/O out of the `rayon` pool; a blocked worker stalls unrelated parallel work.
- **Async has no equivalent of a borrowing scope.** A spawned Tokio task must be `'static`. To run borrowing futures concurrently, keep them on the current task with `join!` or `FuturesUnordered`.

**Thread-side channels and locks.**

- `std::sync::mpsc` is enough for many producers and one consumer. For several consumers, `select` over channels, or timers and deadlines, use `crossbeam-channel` or `flume`. Pick one family per project.
- **Every receive loop handles disconnection.** A `recv` error means all senders are gone and is the normal way a worker learns to stop. Dropping the last sender is the shutdown signal; a clone kept alive by accident is a worker that never exits.
- **A zero-capacity (rendezvous) channel** makes the producer wait until the consumer takes the item; a small capacity throttles. `send_timeout` gives a producer a bounded wait and a point at which to shed load. Never busy-wait in place of a blocking receive.
- **`parking_lot` locks** are smaller, do not poison, and can be faster under contention; `std`'s are good since 1.62 and need no dependency. Choose from a measurement, and use one kind per project so guards and conventions are not mixed.
- **Poisoning:** a `std` mutex is poisoned when a holder panicked, since the data may be half-updated. `lock().unwrap()` spreads the panic, which is right when the invariant may be broken. Recover with `into_inner` only where every critical section leaves the data valid at each step.

**Runtime choice.** Tokio is the default and has the ecosystem. Other runtimes
(single-threaded, or thread-per-core over `io_uring`) are specialist choices that follow from
a measured need. Do not mix runtimes in one process without a clear boundary: a future built
on one runtime's I/O types generally fails on another. A library should depend on `futures`
traits and take the runtime's pieces from its caller where it can.

## Tests

- **Run the real binary** in integration tests (for example with `assert_cmd`), in a temporary directory, and assert on stdout, stderr and the exit status separately.
- Cover: no arguments, `--help`, a missing file, an unreadable file, an empty file, a non-UTF-8 path, output to a closed pipe, and a broken configuration file.
- Test the parser without exiting the process: `try_parse_from(args)`.

**Snapshots, where the whole text is the contract.**

```rust
use expect_test::expect;

#[test]
fn renders_a_two_node_graph() {
    let got = render(&two_node_graph());
    expect![[r#"
        digraph {
          a -> b
        }
    "#]]
    .assert_eq(&got);
}
```

- Good for parsers, formatters, diagnostics, plans and macro expansion. `expect-test` keeps the text inline and updates with `UPDATE_EXPECT=1`; `insta` keeps files and has a review command.
- **A snapshot nobody reads is not a test.** Keep each one small enough to review in a diff, and read the diff on every update. An update accepted blindly records the bug as the expected output.
- Remove what varies before comparing: timestamps, temporary paths, addresses, map order, durations.
- Anti-pattern: one huge snapshot of a whole response where three fields matter. Assert the three fields.

## Packaging

- **A published crate lists exactly what it ships.** Set `include` to an allow-list and check it with `cargo package --list`. Otherwise fixtures, CI files and occasionally secrets get published, and a published version cannot be deleted, only yanked.
- A crate whose Rust sources sit in a subdirectory of a polyglot repository sets `build` and `[lib] path` explicitly, and `autoexamples = false` when `examples/` holds sample inputs, not Rust programs.
- **Discover a workspace with `cargo metadata`** (the `cargo_metadata` crate), not by walking manifests. Hand-rolled discovery gets glob members, `exclude`, path dependencies and inherited keys wrong.
- **A program's own version is a compile-time constant:** `env!("CARGO_PKG_VERSION")` or the argument parser's version attribute. `Cargo.toml` is not shipped with the binary. A Git hash comes from a build script through `cargo:rustc-env`, with a fallback for builds outside a checkout, such as from a published crate.
- **A deprecation warning is fixed, or suppressed at one wrapper** with `#[allow(deprecated)]` and a comment naming the version or event that removes it. Never crate-wide.
- **Vendored sources are pinned, with the upstream version recorded.** Advance one at a time to a chosen commit, regenerate, run the tests, commit. Never bulk-advance to branch tips. A scheduled job reports drift from upstream.
- **Subcommands share output flags and one emitter.** Format flags are one flattened struct; commands emit typed messages through one trait with a human and a JSON-lines implementation, and do not call `println!` themselves.
- **The second occurrence of an architectural violation becomes a machine-checked rule:** a `disallowed_methods` or `disallowed_types` entry, a structural-search rule or a custom lint, run in CI. Its message says what to do instead.
- **A dependency or analysis report states its denominators:** what was scanned and what was excluded. "No cycles" or "no findings" means nothing without the scope.
- **A release review is split into named areas, each with its own verdict** (security, correctness, compatibility, documentation). One failing area blocks. A headline claim gets its own validation.

## Review

- Is anything other than data written to stdout? Does every failure exit non-zero with a message on stderr that names the input and the fix?
- What happens on a non-UTF-8 path, a file larger than memory, an empty input, and output piped into `head`?
- Is the output order the same on every run and every machine?
- Can any child process hang the tool, fill a pipe or outlive it?
- Does an interrupted run leave a half-written file?
- Is configuration read in one place, and does a typo in it fail loudly?
- Does any library crate print, call `process::exit` or read the environment?

**Reject by default:** `unwrap()` on user input or file contents; `process::exit` below
`main`; diagnostics on stdout; a shell string built from input; `Path::exists` followed by
an open; colour codes in piped output; `String` for paths; a fixed sleep used as a wait.

## Patterns seen in production repositories

Each entry names the project it was observed in. Treat them as shapes to adapt, not as APIs to copy.

- **A path resolver bounded to the repository.** Keep raw user paths and resolved absolute paths as two types. Resolve symlinks before checking containment. Access outside the repository needs an explicit `allow_outside` capability passed by the caller, never a default.

## Out of scope

- **A long-running server or worker.** Use the application-service skill.
- **The core of a parser, index or analysis engine.** Use the infra skill; this one covers the binary around it.
- **A public library interface.** Use the library skill.
- **Unsafe code and FFI.**

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
