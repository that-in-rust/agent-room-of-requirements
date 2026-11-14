# Rust Patterns 202606 Part 3

Purpose: capture Rust and Rust-adjacent architecture, idiom, parser, Tree-sitter, code-intelligence, async, CLI, API, storage, verification, and operational patterns discovered repo-by-repo under `/Users/amuldotexe/Desktop`.

Evidence policy: every non-obvious pattern should name the repository, file path, and why the code is reusable. Codebase-memory graph evidence is useful for discovery, but source paths and snippets are the authority.

Shard owner: parallel worker 3.
Shard repo count: 31.

## Assigned Repository Shard

- `/Users/amuldotexe/Desktop/notes-plans-hub/Notes2026`
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien`
- `/Users/amuldotexe/Desktop/oss-read-only/arroyo`
- `/Users/amuldotexe/Desktop/oss-read-only/codex`
- `/Users/amuldotexe/Desktop/oss-read-only/great_expectations`
- `/Users/amuldotexe/Desktop/oss-read-only/materialize`
- `/Users/amuldotexe/Desktop/oss-read-only/parseltongue-rust-LLM-companion`
- `/Users/amuldotexe/Desktop/oss-read-only/risingwave`
- `/Users/amuldotexe/Desktop/oss-read-only/tao`
- `/Users/amuldotexe/Desktop/oss-read-only/xarray`
- `/Users/amuldotexe/Desktop/personal-repos-lane/DailyJournal202309`
- `/Users/amuldotexe/Desktop/personal-repos-lane/amuldotexe.github.io`
- `/Users/amuldotexe/Desktop/personal-repos-lane/codecrafters-http-server-rust`
- `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis`
- `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network`
- `/Users/amuldotexe/Desktop/personal-repos-lane/hackerrank-exploration-202604`
- `/Users/amuldotexe/Desktop/personal-repos-lane/low-drama-insights`
- `/Users/amuldotexe/Desktop/personal-repos-lane/neo4j`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion`
- `/Users/amuldotexe/Desktop/personal-repos-lane/proof-of-effort-2024`
- `/Users/amuldotexe/Desktop/personal-repos-lane/rustASCII`
- `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool`
- `/Users/amuldotexe/Desktop/personal-repos-lane/wandlorelabs2025`
- `/Users/amuldotexe/Desktop/personal-repos-lane/zztweetbook202408`
- `/Users/amuldotexe/Desktop/reference-repos-yard/aeneas`
- `/Users/amuldotexe/Desktop/reference-repos-yard/charon`
- `/Users/amuldotexe/Desktop/reference-repos-yard/eurydice`
- `/Users/amuldotexe/Desktop/reference-repos-yard/iggy`
- `/Users/amuldotexe/Desktop/reference-repos-yard/mempalace`
- `/Users/amuldotexe/Desktop/reference-repos-yard/rust-gpu`
- `/Users/amuldotexe/Desktop/reference-repos-yard/tauri`

## Pattern Entries

Entries are appended one concept at a time. Use this shape:

```text
### Concept: <specific reusable Rust pattern>
Evidence: <repo-relative or absolute source path>
Why it matters: <architecture or idiom value>
Reusable code shape: <short snippet or pseudocode>
Transfer rule: <when to apply / avoid>
Verification hook: <test, command, invariant, benchmark, or review signal>
```

## Repo Coverage: `/Users/amuldotexe/Desktop/notes-plans-hub/Notes2026`

### Concept: Skip note for notes-only Rust references
Evidence: `/Users/amuldotexe/Desktop/notes-plans-hub/Notes2026/ab_09_parseltongue_research/docs202603/stable/archive-docs-v2/archive-p1/A-20260227164745-test_watcher_v143.rs`
Why it matters: `rg --files` found two `.rs` paths and several parser-themed Markdown notes, but the sampled Rust file is only a one-line archival marker (`// v1.4.3 test`) rather than an implementation. This repo can still be useful as human research context, but it should not be mined as source-backed Rust architecture evidence.
Reusable code shape:
```rust
// No reusable implementation in this shard scan; sampled .rs file was archival.
```
Transfer rule: Treat note vaults as secondary references unless a real `Cargo.toml`, crate source tree, or executable test corpus exists. Avoid extracting patterns from filenames or prose-only parser notes when the job requires implementation evidence.
Verification hook: `rg --files /Users/amuldotexe/Desktop/notes-plans-hub/Notes2026 -g '*.rs' -g 'Cargo.toml'` returned no manifest and only two `.rs` files; direct `sed` verification showed the sampled file had no runnable code.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network`

### Concept: Skip note for empty Rust placeholder crate
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network/src/main.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network/Cargo.toml`
Why it matters: This repo looks Rust-shaped by path, but both the manifest and `src/main.rs` are empty. The Rust inventory script reported `error: no Rust packages discovered from scanned manifests`, so there is no implementation pattern to transfer.
Reusable code shape:
```rust
// Empty placeholder; no reusable source-backed pattern.
```
Transfer rule: Skip empty scaffolds in extraction jobs. Do not infer CLI, service, or crate patterns from directory layout alone.
Verification hook: `wc -c /Users/amuldotexe/Desktop/personal-repos-lane/floo-network/src/main.rs /Users/amuldotexe/Desktop/personal-repos-lane/floo-network/Cargo.toml` reported `0` bytes for both files.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/zztweetbook202408`

### Concept: Skip note for Git LFS pointer-only Rust checkout
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/zztweetbook202408/p002_thread_extractor_202409v1/src/main.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/zztweetbook202408/p003/src/processor.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/zztweetbook202408/p003/Cargo.toml`
Why it matters: `rg --files` finds Rust-looking manifests and modules, but direct reads show Git LFS pointer stubs such as `version https://git-lfs.github.com/spec/v1` instead of source. This is a strong extraction anti-pattern: file extension and manifest names are not evidence when the working tree lacks object contents.
Reusable code shape:
```rust
// Not available: source files are Git LFS pointer records, not Rust modules.
```
Transfer rule: When a repo contains LFS pointer files, mark implementation evidence unavailable unless `git lfs pull` has materialized the real content. Avoid treating pointer metadata like `size 7862` as source.
Verification hook: `sed -n '1,5p' .../p003/src/processor.rs` returned the Git LFS pointer header; Cargo inventory failed with `no Rust packages discovered from scanned manifests`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/codecrafters-http-server-rust`

### Concept: Minimal blocking TCP accept loop for challenge scaffolds
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/codecrafters-http-server-rust/src/main.rs`
Why it matters: This is a compact learning scaffold for a network service: bind a loopback listener, iterate over incoming streams, and handle accept errors without crashing the entire process. It is intentionally not production-grade async Rust, but it is useful for agentic assistants because it gives a tiny, observable starting shape before HTTP parsing, response writing, and concurrency are introduced.
Reusable code shape:
```rust
use std::net::TcpListener;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:4221").unwrap();

    for stream in listener.incoming() {
        match stream {
            Ok(_stream) => println!("accepted new connection"),
            Err(e) => println!("error: {}", e),
        }
    }
}
```
Transfer rule: Apply for single-threaded kata stages or smoke listeners where the test harness only checks that a port accepts connections. Avoid in production services because it uses blocking I/O, unwraps bind errors, and does no per-connection work or graceful shutdown.
Verification hook: Run the CodeCrafters harness or `cargo run` in `/Users/amuldotexe/Desktop/personal-repos-lane/codecrafters-http-server-rust`, then connect to `127.0.0.1:4221` and verify the accept log appears.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis`

### Concept: Deterministic catalog generation with typed YAML, sorted entries, templates, and JSON sidecars
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis/data/render/src/bin/main.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis/data/render/src/lib.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis/data/render/src/types.rs`
Why it matters: The renderer converts a directory of YAML tool descriptions into both Markdown and machine-readable JSON. The reusable architecture is: parse CLI paths into a typed `Args`, read YAML into `ParsedEntry`, validate against a tag catalog, convert into richer `Entry` values, sort them, partition multi-language tools, render Markdown through Askama, and write denormalized JSON sidecars. `BTreeMap`/`BTreeSet` are used where deterministic render order matters, which is exactly what agent-generated docs and catalogs need for stable diffs.
Reusable code shape:
```rust
let parsed_tools = read_tools(args.tools)?;
let tools: Result<Vec<Entry>> = parsed_tools
    .into_iter()
    .map(|t| Entry::from_parsed(t, &tags))
    .collect();
let mut tools = tools?;
tools.sort();

let catalog = create_catalog(&tools, &languages, &other_tags)?;
fs::write(&args.md_out, catalog.render()?)
    .context(format!("Cannot write Markdown output to {}", args.md_out.display()))?;

let api = create_api(catalog, &languages, &other_tags)?;
fs::write(args.json_out.join("tools.json"), serde_json::to_string_pretty(&api)?)?;
```
Transfer rule: Apply when one source-of-truth content model must produce human and API artifacts with stable ordering. Avoid `HashMap`/`HashSet` for rendered catalogs unless nondeterministic output order is acceptable.
Verification hook: Run `cargo test` in `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis/data/render`; the local `test_slugify` test verifies stable key generation and the render path is guarded by `anyhow::Context` errors.

### Concept: Async optional deprecation enrichment gated by environment token
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/dynamic-analysis/data/render/src/lib.rs`
Why it matters: `check_deprecated` is a good example of optional network enrichment that does not contaminate the core data model. The binary only performs GitHub checks if `GITHUB_TOKEN` exists, and the function mutates an already-parsed `Vec<Entry>` by setting `deprecated` based on last commit age. This keeps offline rendering deterministic while allowing CI or release jobs to opt into freshness metadata.
Reusable code shape:
```rust
if !args.skip_deprecated {
    if let Ok(token) = env::var("GITHUB_TOKEN") {
        check_deprecated(token, &mut tools)?;
    }
}

#[tokio::main]
pub async fn check_deprecated(token: String, entries: &mut Vec<Entry>) -> Result<()> {
    let github = Github::new("analysis tools bot".to_string(), Credentials::Token(token))?;
    for entry in entries {
        if entry.source.is_none() {
            continue;
        }
        // Parse github.com/<owner>/<repo>; skip deep links.
        // Mark entries deprecated when last commit is older than policy threshold.
    }
    Ok(())
}
```
Transfer rule: Apply when external API calls are enrichment, not required correctness. Avoid hard-requiring tokens for local docs builds or tests.
Verification hook: Review signal: rendering should work with no `GITHUB_TOKEN`; CI can add an integration check with a token and a fixture repo older than the deprecation threshold.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/proof-of-effort-2024`

### Concept: Learning harness that explicitly sequences small Rust modules from `main`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/proof-of-effort-2024/src/main.rs`
Why it matters: This project is a personal learning harness rather than a reusable library. The pattern still matters for agentic code assist because it shows a low-friction way to accumulate small runnable experiments: each topic gets its own module, `main` calls them in a known order, and one Tokio example is driven from a manually-created runtime. This makes it easy for an assistant to add a new exercise without perturbing earlier ones.
Reusable code shape:
```rust
mod f01_shadowing;
mod f02_panic;
mod f03_factorial;
mod f04_tokio_01;
mod f05_some_none;

fn main() {
    f01_shadowing::f01_shadowing();
    f02_panic::f02_panic();
    f03_factorial::f03_factorial(5);

    let rt = tokio::runtime::Runtime::new().unwrap();
    rt.block_on(f04_tokio_01::async_main());

    match f05_some_none::f05_some_division(1.0, 2.0) {
        Some(value) => println!("Some valid result {:?}", value),
        None => println!("Denominator is 0"),
    }
}
```
Transfer rule: Apply for notebooks, workshops, or kata repos where linear execution is clearer than library abstraction. Avoid this shape for production binaries because panicking examples and manual runtime setup can obscure real error handling.
Verification hook: `cargo run` in `/Users/amuldotexe/Desktop/personal-repos-lane/proof-of-effort-2024` should execute all module demos in sequence.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool`

### Concept: Typed folder-first CLI validation before async processing
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool/src/cli.rs`
Why it matters: `CliConfig` centralizes archive validation before the rest of the pipeline runs. It checks argument count, verifies the archive path exists and is a directory, requires `tweets.js`, and exposes optional DM files through methods returning `Option<PathBuf>`. That makes downstream async processing consume a validated configuration object instead of rechecking paths at every call site.
Reusable code shape:
```rust
#[derive(Debug)]
pub struct CliConfig {
    pub archive_folder: PathBuf,
    pub output_dir: Option<PathBuf>,
    pub non_interactive: bool,
}

impl CliConfig {
    pub fn from_args() -> Result<Self> {
        let args: Vec<String> = env::args().collect();
        if args.len() < 2 {
            print_usage();
            bail!("Missing required argument: archive folder path");
        }

        let archive_folder = PathBuf::from(&args[1]);
        if !archive_folder.exists() {
            bail!("Archive folder does not exist: {}", archive_folder.display());
        }
        if !archive_folder.is_dir() {
            bail!("Path is not a directory: {}", archive_folder.display());
        }
        if !archive_folder.join("tweets.js").exists() {
            bail!("tweets.js not found in archive folder");
        }

        Ok(Self {
            archive_folder,
            output_dir: args.get(2).map(PathBuf::from),
            non_interactive: true,
        })
    }
}
```
Transfer rule: Apply when a CLI command operates on a required directory contract. Avoid scattering file existence checks inside business logic; keep discovery methods like `tweets_file`, `dms_file`, and `dm_headers_file` on the config type.
Verification hook: `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool/src/cli.rs` has `#[tokio::test] async fn test_file_detection()` that creates temporary archive files and verifies optional file detection.

### Concept: File chunking utility with explicit config, result metadata, and edge-case tests
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool/src/utils/file_splitter.rs`
Why it matters: Large-file operations are usually where agent-written scripts become brittle. This module packages chunking into `SplitConfig`, `SplitResult`, and `ChunkInfo`, validates input before doing I/O, preserves compound extensions like `.tar.gz`, supports custom prefixes/output directories, and implements `Display` for operator-friendly summaries. The tests cover parsing sizes, chunk sizes, empty files, extension preservation, and custom output paths.
Reusable code shape:
```rust
pub fn split_file(config: &SplitConfig) -> Result<SplitResult> {
    validate_config(config)?;

    let input_path = config.input_path
        .canonicalize()
        .context("Failed to resolve input file path")?;
    let output_dir = determine_output_dir(config, &input_path)?;
    let (base_name, extension) = determine_filename_parts(config, &input_path);

    let file_size = input_path.metadata()
        .context("Failed to read input file metadata")?
        .len();
    if file_size == 0 {
        bail!("Input file is empty");
    }

    let chunks = create_chunks(&input_path, &output_dir, &base_name, &extension, config)?;
    Ok(SplitResult { input_path, output_dir, chunk_size: config.chunk_size, chunks, total_size: file_size })
}
```
Transfer rule: Apply when generated outputs may exceed LLM upload, editor, email, or filesystem ergonomics. Avoid reading the entire file into memory when fixed-size buffered reads are enough.
Verification hook: `cargo test test_split_small_file test_complex_extension_preservation test_parse_size_string` in `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool`.

### Concept: Async ingestion pipeline that isolates CPU-heavy thread grouping with `spawn_blocking`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool/src/processing/tweets.rs`
Why it matters: The tweet pipeline reads a Twitter export asynchronously, slices the JSON payload out of the JavaScript wrapper, parses with `serde_json`, filters retweets, builds a `HashMap` by tweet id, then moves CPU-ish reply-thread grouping into `tokio::task::spawn_blocking`. That preserves async file I/O while keeping synchronous graph/grouping code from monopolizing the runtime worker.
Reusable code shape:
```rust
let script_content = async_fs::read_to_string(input_file)
    .await
    .context("Failed to read input file")?;
let json_start = script_content.find('[').context("Invalid JSON format: missing opening bracket")?;
let json_end = script_content.rfind(']').context("Invalid JSON format: missing closing bracket")?;
let tweets: Vec<TweetWrapper> = serde_json::from_str(&script_content[json_start..=json_end])
    .context("Failed to parse JSON")?;

let tweets_map: HashMap<String, Tweet> = tweets
    .into_iter()
    .map(|tw| tw.tweet)
    .filter(|tweet| !tweet.retweeted)
    .map(|tweet| (tweet.id_str.clone(), tweet))
    .collect();

let screen_name = screen_name.to_string();
let threads = task::spawn_blocking(move || {
    crate::processing::reply_threads::process_reply_threads(
        &tweets_map.values().cloned().collect::<Vec<_>>(),
        &screen_name,
    )
}).await?;
```
Transfer rule: Apply when async ingestion feeds CPU-bound parsing, clustering, compression, or graph building. Avoid capturing borrowed data in `spawn_blocking`; clone or own what crosses the thread boundary.
Verification hook: `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool/src/processing/tweets.rs` includes tests for missing-file error behavior, retweet filtering, and reply relationship setup.

### Concept: LLM-ready text artifact generation with file-structure tests
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool/tests/file_generation_tests.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool/src/models/timeline.rs`
Why it matters: The relationship-analysis tests assert that generated text contains stable headers such as `USER RELATIONSHIP PROFILE`, `INTERACTION TIMELINE`, and `LLM ANALYSIS PROMPTS`, and that output directories/files are created with predictable names. This is a good Rust-adjacent pattern for agent tooling: text artifacts for downstream LLM analysis should be schema-like enough to test with substring and filesystem invariants.
Reusable code shape:
```rust
#[test]
fn test_file_output_structure() {
    let temp_dir = tempdir().unwrap();
    let generator = LLMFileGenerator::new(temp_dir.path().to_str().unwrap(), "testuser", 1234567890);

    let result = generator.generate_all_files(&profiles, &interactions);
    assert!(result.is_ok());

    let base_dir = temp_dir.path().join("relationship_profiles_testuser_1234567890");
    assert!(base_dir.join("interaction_timeline.txt").exists());
    assert!(base_dir.join("communication_patterns.txt").exists());
    assert!(base_dir.join("relationship_network.txt").exists());
    assert!(base_dir.join("llm_analysis_prompts.txt").exists());
}
```
Transfer rule: Apply when Rust programs prepare context packs for AI systems, analysts, or batch review. Avoid relying only on golden full-file snapshots when lightweight section/header invariants would be less brittle.
Verification hook: `cargo test --test file_generation_tests` in `/Users/amuldotexe/Desktop/personal-repos-lane/tweet_scrolls_convert_tool`.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien`

### Concept: Typed error container with sanitized external HTTP projection and detailed internal projection
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien/crates/alien-error/src/lib.rs`, `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien/crates/alien-commands/src/server/axum_handlers.rs`
Why it matters: `alien-error` separates error semantics from presentation. Domain variants implement `AlienErrorData` to provide machine codes, retryability, internal/external visibility, messages, context, hints, and HTTP status. `AlienError<T>` stores those fields plus an optional source chain. With the `axum` feature, `IntoResponse` defaults to `into_external_response`, which replaces internal errors with a generic 500 while `into_internal_response` preserves details for service-to-service calls. This gives agents a reusable answer to a common Rust backend problem: one error type can be serialized for APIs, rendered for humans, chained across layers, and sanitized at trust boundaries.
Reusable code shape:
```rust
pub trait AlienErrorData {
    fn code(&self) -> &'static str;
    fn retryable(&self) -> bool;
    fn internal(&self) -> bool;
    fn message(&self) -> String;
    fn http_status_code(&self) -> u16 { 500 }
    fn context(&self) -> Option<serde_json::Value> { None }
    fn hint(&self) -> Option<String> { None }
}

#[derive(Debug, Serialize, Deserialize, Clone)]
#[serde(rename_all = "camelCase")]
pub struct AlienError<T: AlienErrorData + Clone + std::fmt::Debug + Serialize> {
    pub code: String,
    pub message: String,
    pub context: Option<serde_json::Value>,
    pub hint: Option<String>,
    pub retryable: bool,
    pub internal: bool,
    pub http_status_code: Option<u16>,
    pub source: Option<Box<AlienError<GenericError>>>,
    #[serde(skip)]
    pub error: Option<T>,
}

#[cfg(feature = "axum")]
impl<T> axum::response::IntoResponse for AlienError<T>
where
    T: AlienErrorData + Clone + std::fmt::Debug + Serialize + Send + Sync + 'static,
{
    fn into_response(self) -> axum::response::Response {
        self.into_external_response()
    }
}
```
Transfer rule: Apply when a Rust service needs one error path for CLI output, JSON API responses, OpenAPI schemas, and cross-service calls. Avoid exposing `into_internal_response` at public HTTP edges; defaulting `IntoResponse` to sanitized behavior is the important safety invariant.
Verification hook: `rg -n "into_external_response|into_internal_response|impl IntoResponse" /Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien/crates/alien-error/src/lib.rs`; run `cargo test -p alien-error --features axum,anyhow` when dependencies are available.

### Concept: Command registry as lifecycle source of truth separate from payload storage
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien/crates/alien-commands/src/server/command_registry.rs`, `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien/crates/alien-commands/src/server/axum_handlers.rs`, `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien/crates/alien-commands/tests/integration_tests.rs`
Why it matters: The command server splits metadata from blobs. `CommandRegistry` owns command id, deployment id, command name, state, attempts, deadlines, timestamps, request/response sizes, errors, deployment model, and project routing; a separate KV store holds params/response blobs and pending indices. That boundary lets the same lifecycle support push and pull dispatch plus inline and storage-backed bodies. The integration tests explicitly enumerate the eight core scenarios: `(Push, Pull) x (Small Params, Large Params) x (Small Response, Large Response)`.
Reusable code shape:
```rust
#[async_trait]
pub trait CommandRegistry: Send + Sync {
    async fn create_command(
        &self,
        deployment_id: &str,
        command_name: &str,
        initial_state: CommandState,
        deadline: Option<DateTime<Utc>>,
        request_size_bytes: Option<u64>,
    ) -> Result<CommandMetadata>;

    async fn get_command_metadata(&self, command_id: &str)
        -> Result<Option<CommandEnvelopeData>>;

    async fn get_command_status(&self, command_id: &str)
        -> Result<Option<CommandStatus>>;

    async fn update_command_state(
        &self,
        command_id: &str,
        state: CommandState,
        dispatched_at: Option<DateTime<Utc>>,
        completed_at: Option<DateTime<Utc>>,
        response_size_bytes: Option<u64>,
        error: Option<serde_json::Value>,
    ) -> Result<()>;
}
```
Transfer rule: Apply when commands/jobs have stateful lifecycle metadata and potentially large request/response bodies. Avoid storing everything in one row/blob if leases, retries, upload completion, payload retrieval, and status polling evolve independently.
Verification hook: `cargo test -p alien-commands --features test-utils`; specific invariants appear in tests such as `test_core_push_large_params_large_response` and `test_core_pull_small_params_small_response`.

### Concept: Generic Axum router over a state capability trait
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien/crates/alien-commands/src/server/axum_handlers.rs`
Why it matters: `create_axum_router<S>()` does not hard-code the application state type. Instead, it requires `S: HasCommandServer + Clone + Send + Sync + 'static`, and handlers call `state.command_server()` to access an `Arc<CommandServer>`. This is a neat pattern for library crates that want to provide routes embeddable in many hosts: the route module owns endpoint definitions, while the host state only has to prove it contains the required service.
Reusable code shape:
```rust
pub trait HasCommandServer {
    fn command_server(&self) -> &Arc<CommandServer>;
}

impl HasCommandServer for Arc<CommandServer> {
    fn command_server(&self) -> &Arc<CommandServer> { self }
}

pub fn create_axum_router<S>() -> Router<S>
where
    S: HasCommandServer + Clone + Send + Sync + 'static,
{
    Router::new()
        .route("/commands", post(create_command::<S>))
        .route("/commands/{command_id}", get(get_command_status::<S>))
        .route("/commands/leases", post(acquire_leases::<S>))
}
```
Transfer rule: Apply in reusable Axum libraries, plugin route modules, or monoliths with a large shared state object. Avoid global singletons; explicit capability traits make test state and production state interchangeable.
Verification hook: Review handlers for generic `State(state): State<S>` plus `where S: HasCommandServer`; route compilation itself verifies the capability contract.

### Concept: Proc-macro state-machine DSL for resource controllers
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien/crates/alien-macros/src/controller.rs`, `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien/crates/alien-infra/src/vault/kubernetes.rs`
Why it matters: `alien-macros` turns annotated controller structs and impl blocks into a full `ResourceController` implementation. The macro adds hidden state fields to named structs, derives serde/default traits, parses handler attributes, generates a state enum, creates a controller-specific `HandlerAction`, validates illegal transitions at compile time, tracks repeated `Stay` loops, and maps states to `ResourceStatus`. The user-facing controller remains readable: lifecycle handlers are ordinary async methods with `#[flow_entry]`, `#[handler]`, and `terminal_state!` annotations.
Reusable code shape:
```rust
#[controller]
pub struct KubernetesVaultController {
    pub(crate) namespace: Option<String>,
    pub(crate) vault_prefix: Option<String>,
}

#[controller]
impl KubernetesVaultController {
    #[flow_entry(Create)]
    #[handler(
        state = CreateStart,
        on_failure = CreateFailed,
        status = ResourceStatus::Provisioning,
    )]
    async fn create_start(&mut self, ctx: &ResourceControllerContext<'_>) -> Result<HandlerAction> {
        self.namespace = Some(self.get_kubernetes_namespace(ctx)?);
        Ok(HandlerAction::Continue {
            state: Ready,
            suggested_delay: None,
        })
    }

    terminal_state!(state = CreateFailed, status = ResourceStatus::ProvisionFailed);
    terminal_state!(state = Deleted, status = ResourceStatus::Deleted);
}
```
Transfer rule: Apply when dozens of resource controllers must share state-machine semantics but differ in provider-specific handler bodies. Avoid proc-macro DSLs for one-off workflows; the payoff appears when generated invariants and repeated boilerplate elimination outweigh macro opacity.
Verification hook: Compile-time checks reject missing `#[flow_entry(Create)]`, duplicate handlers, `Delete` entries with `from` lists, and failure states in `from` lists; runtime tests should cover `Stay { max_times, suggested_delay }` leading to `PollingTimeout`.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/arroyo`

### Concept: Streaming operator trait with optional lifecycle hooks and checkpoint/watermark extension points
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/arroyo/crates/arroyo-operator/src/operator.rs`, `/Users/amuldotexe/Desktop/oss-read-only/arroyo/crates/arroyo-worker/src/engine.rs`
Why it matters: Arroyo’s `ArrowOperator` trait makes the hot path (`process_batch`) required and turns everything else into explicit optional hooks: `on_start`, partition-aware `process_batch_index`, async future polling, watermark handling, checkpoint handling, commit handling, periodic ticks, and close behavior. `ConstructedOperator` separates source operators from ordinary Arrow operators, while `ChainedOperator` can run a linked list of operators with a shared collector and control stream. This is a strong pattern for agent runtimes that need many plugin-like processing units without forcing every unit to implement every lifecycle method.
Reusable code shape:
```rust
#[async_trait::async_trait]
pub trait ArrowOperator: Send + 'static {
    fn name(&self) -> String;

    fn tables(&self) -> HashMap<String, TableConfig> { HashMap::new() }
    fn is_committing(&self) -> bool { false }
    fn tick_interval(&self) -> Option<Duration> { None }

    async fn on_start(&mut self, ctx: &mut OperatorContext) -> DataflowResult<()> { Ok(()) }

    async fn process_batch(
        &mut self,
        batch: RecordBatch,
        ctx: &mut OperatorContext,
        collector: &mut dyn Collector,
    ) -> DataflowResult<()>;

    async fn handle_watermark(
        &mut self,
        watermark: Watermark,
        ctx: &mut OperatorContext,
        collector: &mut dyn Collector,
    ) -> DataflowResult<Option<Watermark>> {
        Ok(Some(watermark))
    }

    async fn handle_checkpoint(
        &mut self,
        barrier: CheckpointBarrier,
        ctx: &mut OperatorContext,
        collector: &mut dyn Collector,
    ) -> DataflowResult<()> {
        Ok(())
    }
}
```
Transfer rule: Apply when a runtime needs a stable operator/plugin contract with optional advanced capabilities. Avoid putting every hook in required trait methods unless all implementors genuinely need them.
Verification hook: Review `ChainedOperator::handle_control_message` and `handle_control_message` barrier handling; compile-time implementor checks enforce `process_batch`, while checkpoint/watermark behavior needs integration tests over a small graph.

### Concept: Row-count backpressure wrapper around unbounded Tokio channels
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/arroyo/crates/arroyo-operator/src/context.rs`
Why it matters: Arrow dataflow messages vary drastically in size: one `RecordBatch` may contain one row or thousands. Arroyo uses an unbounded Tokio channel internally but wraps it with `BatchSender`/`BatchReceiver` that track queued row counts and bytes with atomics. `send` waits on a `Notify` when adding a message would exceed the row-count capacity, and `recv` decrements counters and wakes senders. This preserves the ergonomics of unbounded channels while bounding meaningful work-in-flight.
Reusable code shape:
```rust
#[derive(Clone)]
pub struct BatchSender {
    size: u32,
    tx: UnboundedSender<QueueItem>,
    queued_messages: Arc<AtomicU32>,
    queued_bytes: Arc<AtomicU64>,
    notify: Arc<Notify>,
}

impl BatchSender {
    pub async fn send(&self, item: QueueItem) -> Result<(), SendError<QueueItem>> {
        let count = message_count(&item, self.size);
        loop {
            let cur = self.queued_messages.load(Ordering::Acquire);
            if cur as usize + count as usize <= self.size as usize {
                if self.queued_messages
                    .compare_exchange(cur, cur + count, Ordering::SeqCst, Ordering::SeqCst)
                    .is_ok()
                {
                    self.queued_bytes.fetch_add(message_bytes(&item), Ordering::AcqRel);
                    return self.tx.send(item);
                }
            } else {
                let notified = self.notify.notified();
                if self.queued_messages.load(Ordering::Acquire) as usize + count as usize <= self.size as usize {
                    continue;
                }
                notified.await;
            }
        }
    }
}
```
Transfer rule: Apply when the unit of backpressure is not “number of messages” but records, bytes, tokens, cost, or another semantic size. Avoid this shape if bounded `mpsc` capacity already matches real resource use.
Verification hook: Add concurrency tests that send one oversized batch, many small batches, and a receiver that drains slowly; assert capacity and `queued_bytes()` change monotonically with sends/receives.

### Concept: Checkpoint backend with stable object paths, protobuf metadata, parallel cleanup, and table-specific compaction
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/arroyo/crates/arroyo-state/src/parquet.rs`
Why it matters: `ParquetBackend` implements `BackingStore` around object storage and protobuf-encoded checkpoint metadata. Paths are deterministic (`{job_id}/checkpoints/checkpoint-{epoch:0>7}/metadata` and per-operator metadata paths), metadata load/write is centralized, cleanup runs per-operator futures concurrently with `FuturesUnordered`, and compaction delegates by table kind (`GlobalKeyValue` vs `ExpiringKeyedTimeTable`). This creates a clear pattern for resumable agents or streaming workers: checkpoint metadata is small and canonical, while table files can be compacted or cleaned independently.
Reusable code shape:
```rust
fn base_path(job_id: &str, epoch: u32) -> String {
    format!("{job_id}/checkpoints/checkpoint-{epoch:0>7}")
}

#[async_trait::async_trait]
impl BackingStore for ParquetBackend {
    async fn load_checkpoint_metadata(job_id: &str, epoch: u32)
        -> Result<CheckpointMetadata, StateError>
    {
        let storage = get_storage_provider().await?;
        let data = storage.get(format!("{}/metadata", base_path(job_id, epoch)).as_str()).await?;
        Ok(CheckpointMetadata::decode(&data[..])?)
    }

    async fn cleanup_checkpoint(
        mut metadata: CheckpointMetadata,
        old_min_epoch: u32,
        min_epoch: u32,
    ) -> Result<(), StateError> {
        let mut futures: FuturesUnordered<_> = metadata.operator_ids.iter()
            .map(|operator_id| Self::cleanup_operator(
                metadata.job_id.clone(), operator_id.clone(), old_min_epoch, min_epoch,
            ))
            .collect();
        while let Some(result) = futures.next().await {
            let operator_id = result?;
            // delete old per-operator metadata after table cleanup succeeds
        }
        metadata.min_epoch = min_epoch;
        Self::write_checkpoint_metadata(metadata).await
    }
}
```
Transfer rule: Apply for long-running jobs that need object-store checkpoints and independent per-operator/table cleanup. Avoid deleting data solely by epoch without computing the files still referenced by the retained checkpoint.
Verification hook: Unit-test `base_path` formatting and integration-test cleanup by creating metadata where a compacted file is still referenced by `new_min_epoch`; it must survive cleanup.

### Concept: DataFusion physical aggregate split for checkpointable streaming aggregation
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/arroyo/crates/arroyo-planner/src/builder.rs`
Why it matters: `Planner::split_physical_plan` creates a DataFusion physical plan for an aggregate, extracts the partial aggregation from the final aggregate’s input, reconstructs a final plan that reads from an in-memory `ArroyoMemExec`, and builds an `ArroyoSchema` for checkpointed partial state. This is a sophisticated parser/planner-adjacent pattern: reuse the SQL engine’s physical plan representation, but surgically split it at the point where streaming state must be persisted.
Reusable code shape:
```rust
let physical_plan = self.sync_plan(aggregate)?;
let codec = ArroyoPhysicalExtensionCodec { context: DecodingContext::Planning };
let mut node = PhysicalPlanNode::try_from_physical_plan(physical_plan.clone(), &codec)?;

let PhysicalPlanType::Aggregate(mut final_aggregate) = node.physical_plan_type.take().unwrap() else {
    return plan_err!("unexpected physical plan type");
};
let AggregateMode::Final = final_aggregate.mode() else {
    return plan_err!("unexpected physical plan type");
};

let partial_aggregation_plan = *final_aggregate.input.take().unwrap();
let partial_exec = partial_aggregation_plan.try_into_physical_plan(
    self.schema_provider,
    &RuntimeEnvBuilder::new().build().unwrap(),
    &codec,
)?;

let final_input = ArroyoMemExec::new("partial".into(), partial_exec.schema());
final_aggregate.input = Some(Box::new(
    PhysicalPlanNode::try_from_physical_plan(Arc::new(final_input), &codec)?
));
```
Transfer rule: Apply when a batch SQL planner knows how to build the desired operation, but a streaming runtime needs to checkpoint or distribute an internal stage. Avoid string-level SQL rewrites when a typed physical plan can be transformed.
Verification hook: Planner tests should compare graph/plan output for aggregate queries and assert partial schemas include key indices and timestamp fields as expected.

### Concept: CLI-runner shutdown handler that requests a final checkpoint before process exit
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/arroyo/crates/arroyo/src/run.rs`
Why it matters: `PipelineShutdownHandler` stores the active pipeline id behind `Arc<Mutex<Option<String>>>`. On shutdown, it patches the pipeline with `StopType::Checkpoint`, waits up to 120 seconds for `Stopped` or `Failed`, logs timeout as an immediate-shutdown fallback, and triggers a final DB backup notification. This is exactly the kind of operational pattern agentic systems need: graceful cancellation attempts to produce a resumable state artifact, but the process still has a bounded exit path.
Reusable code shape:
```rust
#[derive(Clone)]
struct PipelineShutdownHandler {
    client: Arc<Client>,
    pipeline_id: Arc<Mutex<Option<String>>>,
}

#[async_trait]
impl ShutdownHandler for PipelineShutdownHandler {
    async fn shutdown(&self) {
        let Some(pipeline_id) = self.pipeline_id.lock().unwrap().clone() else { return; };

        if let Err(e) = self.client
            .patch_pipeline()
            .id(&pipeline_id)
            .body(PipelinePatch::builder().stop(StopType::Checkpoint))
            .send()
            .await
        {
            warn!("Unable to stop pipeline with a final checkpoint: {}", e);
        }

        if timeout(Duration::from_secs(120), wait_for_state(&self.client, &pipeline_id, &["Stopped", "Failed"]))
            .await
            .is_err()
        {
            error!("Pipeline did not complete checkpoint within timeout; shutting down immediately");
        }
    }
}
```
Transfer rule: Apply to CLIs that manage long-running jobs, workers, or local services with resumable state. Avoid unbounded shutdown waits; always combine “try to checkpoint” with a timeout and clear warning.
Verification hook: Simulate SIGINT in an integration test with a fake API client; assert `StopType::Checkpoint` is sent and timeout behavior logs or returns predictably.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/great_expectations`

### Concept: Skip note for non-Rust Python/data-quality repository
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/great_expectations`
Why it matters: `rg --files` found no `Cargo.toml` and no `*.rs` files in this checkout. The parser-ish matches are not Rust parser implementations, so there is no source-backed Rust/Rust-adjacent implementation to extract for this shard.
Reusable code shape:
```rust
// Skipped: no Rust source or Cargo manifests found.
```
Transfer rule: Use this repo only as product/domain inspiration for validation systems, not as Rust implementation evidence.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/great_expectations -g 'Cargo.toml' -g '*.rs'` returned zero paths.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/xarray`

### Concept: Skip note for non-Rust Python array library
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/xarray`
Why it matters: `xarray` is a Python scientific-computing repository in this checkout, with no Cargo manifests or Rust source. It is out of scope for Rust pattern extraction.
Reusable code shape:
```rust
// Skipped: no Rust source or Cargo manifests found.
```
Transfer rule: Do not infer Rust array-processing patterns from a Python implementation unless a Rust binding or extension crate exists in the inspected tree.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/xarray -g 'Cargo.toml' -g '*.rs'` returned zero paths.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/DailyJournal202309`

### Concept: Skip note for journal repository with no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/DailyJournal202309`
Why it matters: The repo contains no Rust source or Cargo manifests. It should be excluded from implementation-pattern synthesis.
Reusable code shape:
```rust
// Skipped: no Rust source or Cargo manifests found.
```
Transfer rule: Treat personal journal repos as context only; do not mine them for code patterns unless concrete source files exist.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/DailyJournal202309 -g 'Cargo.toml' -g '*.rs'` returned zero paths.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/amuldotexe.github.io`

### Concept: Skip note for static-site repository with no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/amuldotexe.github.io`
Why it matters: This checkout has no Rust source or Cargo manifests. It is likely a static/site repository, not a Rust implementation source.
Reusable code shape:
```rust
// Skipped: no Rust source or Cargo manifests found.
```
Transfer rule: Skip static-site repos in Rust extraction passes unless they contain WASM, mdBook preprocessors, or Rust-backed build tooling.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/amuldotexe.github.io -g 'Cargo.toml' -g '*.rs'` returned zero paths.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/hackerrank-exploration-202604`

### Concept: Skip note for non-Rust practice/reference repository
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/hackerrank-exploration-202604`
Why it matters: `rg --files` found parser-ish filenames but no `Cargo.toml` and no `*.rs` source files. Without Rust source, the repo cannot provide source-backed Rust parser or algorithm patterns for this shard.
Reusable code shape:
```rust
// Skipped: parser-ish file names exist, but no Rust implementation exists.
```
Transfer rule: Parser keyword hits are discovery signals only; require direct Rust source before extracting implementation patterns.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/hackerrank-exploration-202604 -g 'Cargo.toml' -g '*.rs'` returned zero paths.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/low-drama-insights`

### Concept: Skip note for no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/low-drama-insights`
Why it matters: This repo has no Rust files or Cargo manifests in the assigned checkout.
Reusable code shape:
```rust
// Skipped: no Rust source or Cargo manifests found.
```
Transfer rule: Skip unless a future commit adds concrete Rust tooling.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/low-drama-insights -g 'Cargo.toml' -g '*.rs'` returned zero paths.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/neo4j`

### Concept: Skip note for non-Rust Neo4j-related repository
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/neo4j`
Why it matters: The repo produced many parser-ish hits, but no Rust manifests or `.rs` files. It should not be used as Rust code evidence.
Reusable code shape:
```rust
// Skipped: no Rust source or Cargo manifests found.
```
Transfer rule: For graph/database repos, verify language before extraction; query or Cypher assets are not Rust patterns.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/neo4j -g 'Cargo.toml' -g '*.rs'` returned zero paths.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/rustASCII`

### Concept: Skip note for Rust-named repository without Rust source
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/rustASCII`
Why it matters: Despite the repository name, `rg` found no Rust files and no Cargo manifests. Name-based routing would be misleading here.
Reusable code shape:
```rust
// Skipped: Rust-like repo name, but no Rust source exists.
```
Transfer rule: Always verify repository contents with `rg --files`; never trust names as evidence.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/rustASCII -g 'Cargo.toml' -g '*.rs'` returned zero paths.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/wandlorelabs2025`

### Concept: Skip note for no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/wandlorelabs2025`
Why it matters: The assigned checkout has no Rust source and no Cargo manifests.
Reusable code shape:
```rust
// Skipped: no Rust source or Cargo manifests found.
```
Transfer rule: Keep as non-code context only.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/wandlorelabs2025 -g 'Cargo.toml' -g '*.rs'` returned zero paths.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/mempalace`

### Concept: Skip note for no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/mempalace`
Why it matters: This reference repo has no Rust source or Cargo manifests in the assigned checkout.
Reusable code shape:
```rust
// Skipped: no Rust source or Cargo manifests found.
```
Transfer rule: Do not include in Rust architecture synthesis unless a Rust crate is added later.
Verification hook: `rg --files /Users/amuldotexe/Desktop/reference-repos-yard/mempalace -g 'Cargo.toml' -g '*.rs'` returned zero paths.


## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/codex`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From codex
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/codex/codex-rs/terminal-detection/src/terminal_tests.rs:47` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 1769 Rust files, 114 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
term_program: Option<&str>,
    version: Option<&str>,
    term: Option<&str>,
    multiplexer: Option<Multiplexer>,
) -> TerminalInfo {
    TerminalInfo {
        name,
        term_program: term_program.map(ToString::to_string),
        version: version.map(ToString::to_string),
        term: term.map(ToString::to_string),
        multiplexer,
    }
}

#[test]
fn detects_term_program() {
    let env = FakeEnvironment::new()
        .with_var("TERM_PROGRAM", "iTerm.app")
        .with_var("TERM_PROGRAM_VERSION", "3.5.0")
        .with_var("WEZTERM_VERSION", "2024.2");
    let terminal = detect_terminal_info_from_env(&env);
    assert_eq!(
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/oss-read-only/codex -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/materialize`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Proc Macro Expansion Pattern From materialize
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/materialize/src/aws-secrets-controller/src/lib.rs:11` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 1249 Rust files, 123 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
// by the Apache License, Version 2.0.

use std::collections::BTreeMap;
use std::sync::Arc;
use std::time::Instant;

use anyhow::anyhow;
use async_trait::async_trait;
use aws_config::SdkConfig;
use aws_sdk_secretsmanager::Client;
use aws_sdk_secretsmanager::config::Builder as SecretsManagerConfigBuilder;
use aws_sdk_secretsmanager::error::SdkError;
use aws_sdk_secretsmanager::primitives::Blob;
use aws_sdk_secretsmanager::types::{Filter, FilterNameStringType, Tag};
use mz_repr::CatalogItemId;
use mz_secrets::{SecretsController, SecretsReader};
use tracing::info;
use uuid::Uuid;

#[derive(Clone, Debug)]
pub struct AwsSecretsController {
    pub client: AwsSecretsClient,
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/oss-read-only/materialize -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/parseltongue-rust-LLM-companion`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From parseltongue-rust-LLM-companion
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/parseltongue-rust-LLM-companion/crates/pt08-http-code-query-server/tests/http_server_integration_tests.rs` (sample Rust source file)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 61 Rust files, 5 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
use axum::{
    body::Body,
    http::{Request, StatusCode},
};
use tower::ServiceExt;

use pt08_http_code_query_server::{
    SharedApplicationStateContainer,
    build_complete_router_instance,
};
use parseltongue_core::storage::CozoDbStorage;

/// Create test server instance
///
/// # 4-Word Name: create_test_server_instance
fn create_test_server_instance() -> axum::Router {
    let state = SharedApplicationStateContainer::create_new_application_state();
    build_complete_router_instance(state)
}

// =============================================================================
// Phase 1: Foundation Tests (Tests 1.1 - 1.7)
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/oss-read-only/parseltongue-rust-LLM-companion -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/risingwave`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Proc Macro Expansion Pattern From risingwave
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/risingwave/src/rpc_client/src/compactor_client.rs:15` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 2626 Rust files, 80 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
// See the License for the specific language governing permissions and
// limitations under the License.

use std::sync::Arc;
use std::time::Duration;

use risingwave_common::monitor::EndpointExt;
use risingwave_common::util::addr::HostAddr;
use risingwave_pb::configured_monitor_service_client;
use risingwave_pb::hummock::hummock_manager_service_client::HummockManagerServiceClient;
use risingwave_pb::hummock::{
    GetNewObjectIdsRequest, GetNewObjectIdsResponse, ReportCompactionTaskRequest,
    ReportCompactionTaskResponse,
};
use risingwave_pb::meta::system_params_service_client::SystemParamsServiceClient;
use risingwave_pb::meta::{GetSystemParamsRequest, GetSystemParamsResponse};
use risingwave_pb::monitor_service::monitor_service_client::MonitorServiceClient;
use risingwave_pb::monitor_service::{StackTraceRequest, StackTraceResponse};
use tokio::sync::RwLock;
use tokio_retry::strategy::{ExponentialBackoff, jitter};
use tonic::transport::{Channel, Endpoint};
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/oss-read-only/risingwave -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/tao`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Proc Macro Expansion Pattern From tao
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/tao/src/event_loop.rs:36` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 118 Rust files, 2 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
/// To wake up an `EventLoop` from a another thread, see the `EventLoopProxy` docs.
///
/// Note that the `EventLoop` cannot be shared across threads (due to platform-dependant logic
/// forbidding it), as such it is neither `Send` nor `Sync`. If you need cross-thread access, the
/// `Window` created from this `EventLoop` _can_ be sent to an other thread, and the
/// `EventLoopProxy` allows you to wake up an `EventLoop` from another thread.
///
pub struct EventLoop<T: 'static> {
  pub(crate) event_loop: platform_impl::EventLoop<T>,
  pub(crate) _marker: ::std::marker::PhantomData<*mut ()>, // Not Send nor Sync
}

/// Target that associates windows with an `EventLoop`.
///
/// This type exists to allow you to create new windows while Tao executes
/// your callback. `EventLoop` will coerce into this type (`impl<T> Deref for
/// EventLoop<T>`), so functions that take this as a parameter can also take
/// `&EventLoop`.
#[derive(Clone)]
pub struct EventLoopWindowTarget<T: 'static> {
  pub(crate) p: platform_impl::EventLoopWindowTarget<T>,
  pub(crate) _marker: ::std::marker::PhantomData<*mut ()>, // Not Send nor Sync
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/oss-read-only/tao -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From parseltongue-rust-LLM-companion
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/crates/pt01-folder-to-cozodb-streamer/src/cli.rs:1` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 18697 Rust files, 1265 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
//! Command-line interface for parseltongue-01.
//!
//! # CLI Architecture
//!
//! This crate has two CLI modes:
//!
//! 1. **Unified Binary** (production): Defined in `parseltongue/src/main.rs`
//!    - Usage: `parseltongue folder-to-cozodb-streamer <directory> [--db <path>] [--verbose] [--quiet]`
//!    - `<directory>` is a required positional argument
//!
//! 2. **Standalone Binary** (development): Defined in this file
//!    - Same CLI as unified binary (for consistency)
//!    - Internal fields (max_file_size, include_patterns, etc.) use hardcoded defaults
//!
//! ## Philosophy (S01 Ultra-Minimalist)
//!
//! Following ultra-minimalist principles:
//! - NO unused arguments (removed: --parsing-library, --chunking, --max-size, --include, --exclude)
//! - NO configuration complexity
//! - Hardcoded sensible defaults matching unified binary

use clap::{Arg, ArgAction, Command};
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/aeneas`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Verification Harness Pattern From aeneas
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/aeneas/tests/src/closures.rs:13` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 68 Rust files, 3 Cargo manifests, and 1 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
read(i)
}

// TODO: monomorphisation in Charon
/*
fn call_fn_mut(a: &mut [u8], i: usize) {
    let mut write = |i: usize| { a[i] = 0 };
    write(i)
}
*/

// TODO: typing issue when defining the impl
/*
// TODO: https://github.com/AeneasVerif/charon/issues/989
fn call_fn_parameters<T: Clone>(x: &T) {
    let y = x.clone();
    let consume = |x: T| {};
}
*/

fn call_closure<F: Fn() -> u32>(f: F) -> u32 {
    f()
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/aeneas -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/charon`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From charon
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/charon/charon/src/common.rs:106` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 426 Rust files, 14 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
marker::PhantomData,
    };

    pub trait Mappable = Any + Send + Sync;

    pub trait Mapper {
        type Value<T: Mappable>: Mappable;
    }

    /// A map that maps types to values in a generic manner: we store for each type `T` a value of
    /// type `M::Value<T>`.
    pub struct TypeMap<M> {
        data: HashMap<TypeId, Box<dyn Mappable>>,
        phantom: PhantomData<M>,
    }

    impl<M: Mapper> TypeMap<M> {
        pub fn get<T: Mappable>(&self) -> Option<&M::Value<T>> {
            self.data
                .get(&TypeId::of::<T>())
                // We must be careful to not accidentally cast the box itself as `dyn Any`.
                .map(|val: &Box<dyn Mappable>| &**val)
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/charon -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/eurydice`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Verification Harness Pattern From eurydice
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/eurydice/test/traits2.rs:6` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 63 Rust files, 0 Cargo manifests, and 7 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
fn from_i16_array(array: &[i16]) -> Self;
}

pub(crate) struct PolynomialRingElement<Vector: Operations> {
    pub(crate) coefficients: [Vector; 16],
}

fn re_zero<Vector: Operations>() -> PolynomialRingElement<Vector> {
    PolynomialRingElement {
        coefficients: [Vector::zero(); 16],
    }
}

fn re_from_i16_array<Vector: Operations>(a: &[i16]) -> PolynomialRingElement<Vector> {
    let mut result = re_zero();
    for i in 0..16 {
        result.coefficients[i] = Vector::from_i16_array(&a[i * 16..(i + 1) * 16]);
    }
    result
}

impl<Vector: Operations> PolynomialRingElement<Vector> {
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/eurydice -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/iggy`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From iggy
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/iggy/foreign/python/src/iterator.rs:19` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 1392 Rust files, 46 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
* under the License.
 */

use std::sync::Arc;

use futures::StreamExt;
use iggy::prelude::IggyConsumer as RustIggyConsumer;
use pyo3::exceptions::PyStopIteration;

use crate::receive_message::ReceiveMessage;
use pyo3::prelude::*;
use pyo3_async_runtimes::tokio::future_into_py;
use tokio::sync::Mutex;

#[pyclass]
pub struct ReceiveMessageIterator {
    pub(crate) inner: Arc<Mutex<RustIggyConsumer>>,
}

#[pymethods]
impl ReceiveMessageIterator {
    pub fn __anext__<'a>(&self, py: Python<'a>) -> PyResult<Bound<'a, PyAny>> {
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/iggy -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/rust-gpu`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From rust-gpu
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/rust-gpu/examples/runners/ash/src/main.rs:78` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 522 Rust files, 71 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
use crate::swapchain::MySwapchainManager;
use anyhow::{Context, anyhow};
use ash::util::read_spv;
use clap::{Parser, ValueEnum};
use raw_window_handle::HasDisplayHandle as _;
use shared::ShaderConstants;
use spirv_builder::SpirvBuilder;
use std::{
    fs::File,
    path::PathBuf,
    sync::mpsc::{TryRecvError, sync_channel},
    thread,
};
use winit::event_loop::ActiveEventLoop;
use winit::{
    event::{Event, WindowEvent},
    event_loop::{ControlFlow, EventLoop},
};

pub mod device;
pub mod graphics;
pub mod single_command_buffer;
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/rust-gpu -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/tauri`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From tauri
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/tauri/packages/cli/src/lib.rs:7` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 321 Rust files, 26 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
#![cfg(any(target_os = "macos", target_os = "linux", windows))]

use std::sync::Arc;

use napi::{
  threadsafe_function::{ThreadsafeFunction, ThreadsafeFunctionCallMode},
  Error, Result, Status,
};

#[napi_derive::napi]
pub fn run(
  args: Vec<String>,
  bin_name: Option<String>,
  callback: Arc<ThreadsafeFunction<bool>>,
) -> Result<()> {
  // we need to run in a separate thread so Node.js consumers
  // can do work while `tauri dev` is running.
  std::thread::spawn(move || {
    let res = match std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| {
      tauri_cli::try_run(args, bin_name).inspect_err(|e| eprintln!("{e:#}"))
    })) {
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/tauri -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.

## CodeGraphContext Evidence Appendix

### Concept: Graph-Indexed Shell Parser Boundary
Evidence: CodeGraphContext run `/tmp/codex-code-intel/codegraphcontext/codex-20260706-225543` produced readable stats for 1 repository, 1,383 files, 5,589 functions, 1,076 structs, 320 enums, and 2,892 modules; `cgc find name Parser` returned tree-sitter parser imports in `/Users/amuldotexe/Desktop/oss-read-only/codex/codex-rs/apply-patch/src/invocation.rs:7`.
Why it matters: The graph pass surfaced parser-related entry points, and direct source reads confirmed a layered command-detection boundary: shell classification, heredoc extraction, patch parsing, and verified file-system resolution are separated instead of collapsed into one string parser. This is a useful Rust pattern for agent tools that must accept shell-shaped input without trusting shell text blindly.
Reusable code shape:
```rust
fn parse_shell_script(argv: &[String]) -> Option<(ApplyPatchShell, &str)> {
    match argv {
        [shell, flag, script] => classify_shell(shell, flag).map(|shell_type| {
            let script = script.as_str();
            (shell_type, script)
        }),
        [shell, skip_flag, flag, script] if can_skip_flag(shell, skip_flag) => {
            classify_shell(shell, flag).map(|shell_type| {
                let script = script.as_str();
                (shell_type, script)
            })
        }
        _ => None,
    }
}
```
Transfer rule: Use this shape when an agent-facing Rust tool accepts multiple invocation forms and must distinguish command detection from command execution. Keep the parser side-effect-free and put file-system verification behind a later explicit step.
Verification hook: Re-run `cgc stats` and `cgc find name Parser` against the Codex output directory, then re-open `/Users/amuldotexe/Desktop/oss-read-only/codex/codex-rs/apply-patch/src/invocation.rs:7`, `/Users/amuldotexe/Desktop/oss-read-only/codex/codex-rs/apply-patch/src/invocation.rs:317`, and `/Users/amuldotexe/Desktop/oss-read-only/codex/codex-rs/apply-patch/src/streaming_parser.rs:20`.
