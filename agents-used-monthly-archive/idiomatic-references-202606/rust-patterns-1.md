# Rust Patterns 202606 Part 1

Purpose: capture Rust and Rust-adjacent architecture, idiom, parser, Tree-sitter, code-intelligence, async, CLI, API, storage, verification, and operational patterns discovered repo-by-repo under `/Users/amuldotexe/Desktop`.

Evidence policy: every non-obvious pattern should name the repository, file path, and why the code is reusable. Codebase-memory graph evidence is useful for discovery, but source paths and snippets are the authority.

Shard owner: parallel worker 1.
Shard repo count: 32.

## Assigned Repository Shard

- `/Users/amuldotexe/Desktop/TauriAppsOSS`
- `/Users/amuldotexe/Desktop/oss-read-only/airflow`
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit`
- `/Users/amuldotexe/Desktop/oss-read-only/claude-peers-mcp`
- `/Users/amuldotexe/Desktop/oss-read-only/dbt-core`
- `/Users/amuldotexe/Desktop/oss-read-only/iggy`
- `/Users/amuldotexe/Desktop/oss-read-only/openobserve`
- `/Users/amuldotexe/Desktop/oss-read-only/plotly.py`
- `/Users/amuldotexe/Desktop/oss-read-only/streamlit`
- `/Users/amuldotexe/Desktop/oss-read-only/warp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/CodeEDA`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools`
- `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go`
- `/Users/amuldotexe/Desktop/personal-repos-lane/dobby-subagent-code-summarizer`
- `/Users/amuldotexe/Desktop/personal-repos-lane/fawkes-body-doubling-phoenix`
- `/Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker`
- `/Users/amuldotexe/Desktop/personal-repos-lane/mordor-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-union-find`
- `/Users/amuldotexe/Desktop/personal-repos-lane/pm2dev`
- `/Users/amuldotexe/Desktop/personal-repos-lane/rust-100-exercises-notes`
- `/Users/amuldotexe/Desktop/personal-repos-lane/that-in-rust-org-github`
- `/Users/amuldotexe/Desktop/personal-repos-lane/useful-rc-files`
- `/Users/amuldotexe/Desktop/personal-repos-lane/zz_archived_journal2023`
- `/Users/amuldotexe/Desktop/reference-repos-yard/RAPx`
- `/Users/amuldotexe/Desktop/reference-repos-yard/cachebro`
- `/Users/amuldotexe/Desktop/reference-repos-yard/creusot`
- `/Users/amuldotexe/Desktop/reference-repos-yard/flux`
- `/Users/amuldotexe/Desktop/reference-repos-yard/marker`
- `/Users/amuldotexe/Desktop/reference-repos-yard/polonius`
- `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_jvm`
- `/Users/amuldotexe/Desktop/reference-repos-yard/zed`

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

## Repo Coverage: /Users/amuldotexe/Desktop/TauriAppsOSS

### Concept: Repo skipped because no Rust implementation was present
Evidence: `/Users/amuldotexe/Desktop/TauriAppsOSS` (`rg --files -g 'Cargo.toml'` and `rg --files -g '*.rs'` both returned zero files during the shard inventory)
Why it matters: This repo appears to be documentation/content oriented rather than a Rust or Rust-adjacent implementation. Recording the skip prevents the shard from looking incomplete and keeps extraction effort focused on repos with source-backed Rust patterns.
Reusable code shape:
```text
N/A: no Cargo manifest or Rust source files found.
```
Transfer rule: Skip Rust-pattern extraction when both Cargo manifests and Rust files are absent; only revisit if a later branch adds `src-tauri`, `Cargo.toml`, or generated Rust tooling.
Verification hook: `rg --files /Users/amuldotexe/Desktop/TauriAppsOSS -g 'Cargo.toml' -g '*.rs'`

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/airflow

### Concept: Repo skipped because parser files are Python-adjacent, not Rust-adjacent
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/airflow` (`rg --files -g 'Cargo.toml'` and `rg --files -g '*.rs'` returned zero; parser-ish filenames exist but no Rust parser implementation was present)
Why it matters: Airflow is a Python project in this checkout. It has parser-related files, but without Rust source, Cargo metadata, or Rust parser crates, it cannot supply source-backed Rust idioms for this shard.
Reusable code shape:
```text
N/A: no Rust code to quote or transfer.
```
Transfer rule: Do not mine non-Rust parser terminology as Rust patterns unless there is actual Rust source implementing parser, AST, lexer, or binding behavior.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/airflow -g 'Cargo.toml' -g '*.rs' -g '*parser*'`

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit

### Concept: URI-resolved async storage trait with in-memory test factory
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-storage/src/lib.rs`; `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-storage/src/ram_storage.rs`
Why it matters: Quickwit keeps search/indexing code independent from local files, object stores, and test storage by routing all storage through `Arc<dyn Storage>` plus a `StorageFactory` keyed by URI protocol. The pattern is especially useful for agent-written services because it turns storage selection into configuration and gives tests a fast, deterministic `RamStorage` implementation that still exercises the production trait.
Reusable code shape:
```rust
#[async_trait]
impl Storage for RamStorage {
    async fn put(&self, path: &Path, payload: Box<dyn PutPayload>) -> StorageResult<()> {
        let payload_bytes = payload.read_all().await?;
        self.files.write().await.insert(path.to_path_buf(), payload_bytes);
        Ok(())
    }

    async fn get_slice(&self, path: &Path, range: Range<usize>) -> StorageResult<OwnedBytes> {
        let bytes = self.files.read().await.get(path).cloned().ok_or_else(not_found)?;
        Ok(bytes.slice(range.start..range.end))
    }
}

#[async_trait]
impl StorageFactory for RamStorageFactory {
    async fn resolve(&self, uri: &Uri) -> Result<Arc<dyn Storage>, StorageResolverError> {
        match uri.filepath() {
            Some(prefix) if uri.protocol() == Protocol::Ram => {
                Ok(add_prefix_to_storage(self.ram_storage.clone(), prefix.to_path_buf(), uri.clone()))
            }
            _ => Err(StorageResolverError::InvalidUri(format!("URI `{uri}` is not RAM"))),
        }
    }
}
```
Transfer rule: Apply when production code must support multiple storage backends or when tests need an in-memory backend behind the same API. Avoid if every call site genuinely requires backend-specific features; otherwise the trait becomes a leaky lowest-common-denominator interface.
Verification hook: Quickwit verifies the contract with `storage_test_suite(&mut ram_storage).await?` plus URI-specific factory tests in `ram_storage.rs`; run `cargo test -p quickwit-storage ram_storage`.

### Concept: Two-phase external cleanup with explicit partial-failure accounting
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-index-management/src/garbage_collection.rs`
Why it matters: Deleting distributed search splits is a cross-system operation: storage files and metastore rows can fail independently. Quickwit models that reality instead of flattening it into one opaque error. `DeleteSplitsError` carries successes, storage failures, metastore failures, and the original backend errors, so retry logic and operators know which side of the system needs repair.
Reusable code shape:
```rust
#[derive(Error, Debug)]
#[error("failed to delete splits from storage and/or metastore")]
pub struct DeleteSplitsError {
    successes: Vec<SplitInfo>,
    storage_error: Option<BulkDeleteError>,
    storage_failures: Vec<SplitInfo>,
    metastore_error: Option<MetastoreError>,
    metastore_failures: Vec<SplitInfo>,
}

let delete_result = storage.bulk_delete(&split_paths).await;
match delete_result {
    Ok(_) => successes.extend(split_infos.into_values()),
    Err(err) => classify_successes_and_storage_failures(err, split_infos),
}

if !successes.is_empty() {
    metastore.delete_splits(DeleteSplitsRequest { index_uid: Some(index_uid), split_ids }).await
        .map_err(|err| DeleteSplitsError { metastore_error: Some(err), metastore_failures: successes, ..partial })?;
}
```
Transfer rule: Use for any job that mutates two durable systems where "storage succeeded, metadata failed" is materially different from "storage failed, metadata untouched." Avoid all-or-nothing error enums for cleanup and reconciliation flows unless a real transaction boundary exists.
Verification hook: Quickwit has focused async tests for happy path, storage error, and metastore error in the same file (`test_delete_splits_from_storage_and_metastore_*`); run `cargo test -p quickwit-index-management delete_splits_from_storage_and_metastore`.

### Concept: Unordered per-unit fanout with `tokio::task::JoinSet` and result tags
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/quickwit/quickwit/quickwit-lambda-server/src/handler.rs`
Why it matters: Lambda leaf search fans out work per split and intentionally discards completion order. Each spawned task returns its `split_id` alongside the result, letting the collector aggregate successes and failures as they complete without requiring an ordered join vector or shared mutable state. This is a compact pattern for embarrassingly parallel search, scraping, checks, or per-shard RPC work.
Reusable code shape:
```rust
let mut joinset: tokio::task::JoinSet<(String, Result<Response, String>)> = JoinSet::new();

for split in splits {
    let split_id = split.id.clone();
    let client = client.clone();
    joinset.spawn(async move {
        let result = client.query(split).await.map_err(|err| err.to_string());
        (split_id, result)
    });
}

while let Some(join_result) = joinset.join_next().await {
    match join_result {
        Ok((id, Ok(response))) => successes.push((id, response)),
        Ok((id, Err(error))) => failures.push((id, error)),
        Err(join_error) => task_failures.push(join_error),
    }
}
```
Transfer rule: Apply when each unit of work is independent and output order is either irrelevant or recoverable from an explicit tag. Avoid when downstream semantics require stable input order; in that case, include the original ordinal or use a futures stream that preserves order.
Verification hook: Review invariant: every spawned task must return a stable identifier; collector capacity should be initialized from `joinset.len()` before draining; failed task joins must be counted separately from domain errors.

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/iggy

### Concept: One process-wide Tokio runtime for synchronous FFI surfaces
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/iggy/foreign/cpp/src/lib.rs`
Why it matters: Iggy exposes async Rust behavior through a C++ bridge. Instead of creating a runtime per call, it stores a `tokio::runtime::Runtime` in `std::sync::LazyLock`, making runtime construction explicit, amortized, and shared across FFI entrypoints. This is the right shape when foreign callers need synchronous methods but the Rust client underneath is async.
Reusable code shape:
```rust
static RUNTIME: LazyLock<tokio::runtime::Runtime> = LazyLock::new(|| {
    tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .build()
        .expect("runtime")
});

#[cxx::bridge(namespace = "my::ffi")]
mod ffi {
    extern "Rust" {
        type Client;
        fn connect(self: &Client) -> Result<()>;
    }
}

impl Client {
    pub fn connect(&self) -> Result<()> {
        RUNTIME.block_on(self.inner.connect()).map_err(Into::into)
    }
}
```
Transfer rule: Apply at FFI boundaries where the host language cannot `await` Rust futures. Avoid inside normal Rust libraries or async applications, where nested runtimes and `block_on` can deadlock or waste threads.
Verification hook: Review for exactly one static runtime per FFI library, no runtime creation in hot methods, and bridge tests that call multiple methods through the foreign ABI.

### Concept: Async BDD steps backed by a typed `World` state object
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/iggy/bdd/rust/tests/steps/streams.rs`; `/Users/amuldotexe/Desktop/oss-read-only/iggy/bdd/rust/tests/common/global_context.rs`
Why it matters: Iggy maps human-readable feature steps to async Rust functions while keeping scenario state in a typed `GlobalContext`. The pattern gives acceptance tests a shared vocabulary without collapsing into stringly typed state bags. Agents can reuse this shape when generating end-to-end tests that need durable handles such as clients, created IDs, and last observed payloads.
Reusable code shape:
```rust
#[derive(Debug, World, Default)]
pub struct GlobalContext {
    pub client: Option<IggyClient>,
    pub last_stream_id: Option<u32>,
    pub last_stream_name: Option<String>,
}

#[when(regex = r"^I create a stream with name (.+)$")]
pub async fn when_create_stream(world: &mut GlobalContext, name: String) {
    let client = world.client.as_ref().expect("client");
    let stream = client.create_stream(&name).await.expect("create stream");
    world.last_stream_id = Some(stream.id);
    world.last_stream_name = Some(stream.name.clone());
}

#[then(regex = r"^the stream should have name (.+)$")]
pub async fn then_stream_has_name(world: &mut GlobalContext, expected: String) {
    assert_eq!(world.last_stream_name.as_deref(), Some(expected.as_str()));
}
```
Transfer rule: Apply when product behavior is naturally described as scenarios and requires live async clients. Avoid for tight unit tests where BDD indirection would hide the actual invariant.
Verification hook: Run the Cucumber/Bdd crate tests; review that each step mutates only explicit `World` fields and that `expect` messages name missing test setup rather than production failure modes.

### Concept: Append-only segment writer with vectored positioned I/O and fsync policy
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/iggy/core/partitions/src/messages_writer.rs`; `/Users/amuldotexe/Desktop/oss-read-only/iggy/core/partitions/src/offset_storage.rs`
Why it matters: Iggy writes message batches to segment files with `write_vectored_all_at`, an atomic byte counter, and an explicit fsync flag. The write position is computed from the tracked segment size, chunks are capped by `MAX_IOV_COUNT`, and durability is policy-driven. This gives a reusable shape for log/journal writers that need high throughput but must make fsync cost visible.
Reusable code shape:
```rust
pub async fn save_batches<const ALIGN: usize>(&self, buffers: &[Frozen<ALIGN>]) -> Result<ByteSize> {
    let bytes: u64 = buffers.iter().map(|buf| buf.len() as u64).sum();
    if bytes == 0 {
        return Ok(ByteSize::from(0));
    }

    let position = self.size_bytes.load(Ordering::Relaxed);
    for chunk in buffers.chunks(MAX_IOV_COUNT) {
        let chunk_size: usize = chunk.iter().map(Frozen::len).sum();
        self.file.write_vectored_all_at(chunk.to_vec(), position).await.0?;
        position += chunk_size as u64;
    }
    if self.fsync {
        self.file.sync_all().await?;
    }
    self.size_bytes.fetch_add(bytes, Ordering::Release);
    Ok(ByteSize::from(bytes))
}
```
Transfer rule: Apply for append-only logs, WAL segments, or message stores where batches are already encoded as immutable buffers. Avoid when concurrent writers can reserve overlapping positions; then reserve with `fetch_add` before writing or serialize writes.
Verification hook: Review invariant: byte counter equals file metadata after recovery; write chunks never exceed OS vectored-I/O limits; fsync policy is covered by tests or crash-recovery simulation.

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/openobserve

### Concept: Body-aware router proxy that rehydrates consumed payloads
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/openobserve/src/router/http/mod.rs`
Why it matters: OpenObserve runs a router node that sometimes must inspect the request body to choose a consistent querier node. Because reading an Axum request consumes the body, the code parses the payload into a typed enum (`QuerierPayload`) and then rebuilds the upstream `reqwest::RequestBuilder` with the same JSON/form semantics. This is a reusable shape for routers that need body-based sharding without losing the original request.
Reusable code shape:
```rust
enum QueryPayload {
    Empty,
    Form(HashMap<String, String>),
    Search(Box<SearchRequest>),
}

let (routing_key, payload) = parse_query_payload(req, path).await?;
let node = consistent_hash_node(&routing_key).await?;
target.full_url = format!("{}{}", node.http_addr, target.path);

let upstream = match payload {
    QueryPayload::Empty => client.get(&target.full_url).headers(headers),
    QueryPayload::Form(form) => client.post(&target.full_url).headers(headers).form(&form),
    QueryPayload::Search(json) => client.post(&target.full_url).headers(headers).json(&*json),
};
send_and_respond(upstream, &target, is_streaming, start).await
```
Transfer rule: Apply when routing decisions depend on request body fields such as SQL, tenant, or partition key. Avoid casual body inspection in pass-through proxies unless you also rebuild the upstream request exactly once and reject unsupported endpoints clearly.
Verification hook: OpenObserve has unit tests around route classification (`test_is_querier_route`) and target resolution; add tests that parse each payload variant and assert the selected routing key plus rebuilt upstream method/body type.

### Concept: Queue-backed WAL writer with pre-processing outside the IO loop
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/openobserve/src/ingester/src/writer.rs`
Why it matters: The ingester writer separates CPU-heavy batch preparation from WAL/memtable mutation. `write_batch` preprocesses entries before enqueueing, then a single consumer loop serializes IO work. Configuration chooses direct writes, queued writes that wait, or `try_send` rejection when the queue is full. This makes backpressure policy explicit and keeps the hot IO loop focused.
Reusable code shape:
```rust
pub async fn write_batch(&self, entries: Vec<Entry>, fsync: bool) -> Result<()> {
    if entries.is_empty() {
        return Ok(());
    }
    let processed = self.preprocess_batch(entries)?;

    if !cfg.queue_enabled {
        return self.consume_processed(processed, fsync).await;
    }
    if cfg.queue_full_reject {
        self.write_queue
            .try_send((WriterSignal::Produce, processed, fsync))
            .map_err(|_| Error::WriteQueueFull)?;
    } else {
        self.write_queue
            .send((WriterSignal::Produce, processed, fsync))
            .await?;
    }
    Ok(())
}
```
Transfer rule: Apply for ingestion paths where encoding/validation can be done before a serialized writer owns locks. Avoid if pre-processing depends on mutable writer state; that would reintroduce race conditions or stale decisions.
Verification hook: Review metrics for queue length and lock time; test both full-queue policies (`try_send` rejection and awaited send), plus the direct-write path when queueing is disabled.

### Concept: Cross-platform graceful shutdown function as server dependency
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/openobserve/src/report_server/src/server.rs`
Why it matters: OpenObserve keeps shutdown wiring out of route construction. The server binds an Axum router and passes a dedicated `shutdown_signal()` future to `with_graceful_shutdown`; the signal future has separate Unix and Windows branches using `tokio::select!`. That makes lifecycle behavior reviewable and portable.
Reusable code shape:
```rust
let listener = TcpListener::bind(addr).await?;
axum::serve(listener, app.into_make_service())
    .with_graceful_shutdown(shutdown_signal())
    .await?;

async fn shutdown_signal() {
    #[cfg(unix)]
    {
        let mut sigterm = tokio::signal::unix::signal(SignalKind::terminate()).unwrap();
        let mut sigint = tokio::signal::unix::signal(SignalKind::interrupt()).unwrap();
        tokio::select! {
            _ = sigterm.recv() => tracing::info!("SIGTERM received"),
            _ = sigint.recv() => tracing::info!("SIGINT received"),
        }
    }
}
```
Transfer rule: Apply for small services and sidecars where shutdown should be easy to audit. Avoid burying signal handling inside application state or route handlers; graceful shutdown is process lifecycle, not request business logic.
Verification hook: Manual smoke: start server, send SIGTERM/SIGINT, assert listener stops cleanly and logs the selected signal; add platform-gated tests around address parsing where possible.

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/warp

### Concept: Incremental Tree-sitter state keyed by buffer version
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/syntax_tree/src/lib.rs`
Why it matters: Warp treats syntax highlighting as derived editor state, not as inline text data. It keeps a bounded map of `BufferVersion -> Tree`, uses Tree-sitter `InputEdit` for incremental parsing, aborts stale parsing via `AbortHandle`, and caches highlight ranges for the latest viewport. This is a strong pattern for editors and agentic code viewers where parsing must follow rapidly changing buffers without blocking rendering.
Reusable code shape:
```rust
thread_local! {
    static PARSER: RefCell<Parser> = RefCell::new(Parser::new());
}

pub struct SyntaxTreeState {
    syntax_tree: Mutex<HashMap<BufferVersion, Tree>>,
    parsing_handle: Option<AbortHandle>,
    highlight_cache: RefCell<Option<HighlightCache>>,
}

async fn parse_text(content: BufferSnapshot, old_tree: Option<Tree>, language: &Language) -> Tree {
    PARSER.with(|parser| {
        let mut parser = parser.borrow_mut();
        parser.set_language(&language.grammar).expect("grammar");
        let mut bytes = content.bytes();
        parser.parse_with_options(&mut |byte_offset, _| {
            bytes.seek(ByteOffset::from(byte_offset + 1));
            bytes.next().unwrap_or_default()
        }, old_tree.as_ref(), None).expect("parse")
    })
}
```
Transfer rule: Apply when parsing editor buffers, notebooks, or generated code views that change incrementally. Avoid if the source is immutable and parsed once; the version map, abort handle, and cache add unnecessary moving parts.
Verification hook: Review invariant: old syntax trees are truncated (`MAX_SYNTAX_TREES`) and highlight cache keys include buffer version, range set, and language id; run syntax tree query/highlight tests for edits and viewport changes.

### Concept: `nom` parser with explicit indentation context held in `RefCell`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/markdown_parser/src/markdown_parser.rs`; `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/markdown_parser/src/lib.rs`
Why it matters: Markdown list indentation depends on preceding lines, so Warp threads a small mutable `ListIndentationContext` through parser combinators using `RefCell`. The parser still returns typed `FormattedTextLine` variants, and release builds intentionally hide detailed parse errors while debug builds include them. This is useful when a mostly-functional parser needs a narrowly scoped piece of contextual state.
Reusable code shape:
```rust
#[derive(Debug, Clone)]
struct ListIndentationContext {
    indentation_stack: Vec<(usize, usize)>,
}

impl ListIndentationContext {
    fn get_and_register_indent_level(&mut self, spaces: usize) -> usize {
        while let Some(&(prev_spaces, _)) = self.indentation_stack.last() {
            if prev_spaces <= spaces { break; }
            self.indentation_stack.pop();
        }
        let (reference_spaces, reference_level) =
            self.indentation_stack.last().copied().unwrap_or((spaces, 0));
        let level = if spaces - reference_spaces >= 2 { reference_level + 1 } else { reference_level };
        self.indentation_stack.push((spaces, level));
        level
    }
}

let indentation_context = RefCell::new(ListIndentationContext::new());
```
Transfer rule: Apply when parser combinators need localized state such as indentation, heredoc mode, or table alignment. Avoid broad mutable parser globals; keep the context small, resettable, and covered by parser tests.
Verification hook: Warp has `markdown_parser_test.rs`; add regression tests for nested lists, outdented lines, and mixed code blocks because those are the cases where stack-based indentation usually breaks.

### Concept: Language-server installation as async candidate trait plus enum registry
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/lsp/src/language_server_candidate.rs`; `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/lsp/src/supported_servers.rs`
Why it matters: Warp separates "which LSP server supports this language" from "how do I detect, install, and run that server." The enum registry owns stable persisted server kinds and maps each kind to a boxed `LanguageServerCandidate`; the trait owns async detection/installation hooks and metadata lookup. Agents can reuse this to add tool providers without stuffing all provider logic into one match-heavy service.
Reusable code shape:
```rust
#[async_trait]
pub trait LanguageServerCandidate: Send + Sync {
    async fn should_suggest_for_repo(&self, path: &Path, executor: &CommandBuilder) -> bool;
    async fn is_installed_in_data_dir(&self, executor: &CommandBuilder) -> bool;
    async fn is_installed_on_path(&self, executor: &CommandBuilder) -> bool;
    async fn install(&self, metadata: LanguageServerMetadata, executor: &CommandBuilder) -> Result<()>;
    async fn fetch_latest_server_metadata(&self) -> Result<LanguageServerMetadata>;
}

impl LSPServerType {
    pub fn candidate(&self, client: Arc<http_client::Client>) -> Box<dyn LanguageServerCandidate> {
        match self {
            Self::RustAnalyzer => Box::new(RustAnalyzerCandidate::new(client)),
            Self::Pyright => Box::new(PyrightCandidate::new(client)),
            // ...
        }
    }
}
```
Transfer rule: Apply for plugin/provider ecosystems where each provider has different installation heuristics but the product needs one orchestration surface. Avoid if there are only one or two hard-coded providers and no install/update lifecycle.
Verification hook: Add provider contract tests: suggestion predicate, data-dir detection, PATH fallback, command args, and metadata fetch for each enum variant; treat enum renames as persistence migrations.

### Concept: Generic sync queue with retry classification and per-task versus streaming result modes
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/warp/crates/warp_core/src/sync_queue.rs`
Why it matters: Warp’s `SyncQueue<T>` abstracts a background task pipeline over a task trait with an associated error type that can declare whether it is transient. The queue supports per-task oneshot results or broadcast streaming results, rate limiting, retry options, and abort handles for active work. This is a reusable foundation for cloud sync, telemetry uploads, indexing jobs, and agent work queues.
Reusable code shape:
```rust
pub trait IsTransientError {
    fn is_transient(&self) -> bool;
}

pub trait SyncQueueTaskTrait: Send + 'static {
    type Error: Error + Send + Sync + IsTransientError + 'static;
    type Result: Send + Sync;
    type Fut: Future<Output = Result<Self::Result, Self::Error>> + Send;
    fn run(&mut self) -> Self::Fut;
}

enum SyncQueueMode<T: SyncQueueTaskTrait> {
    PerTask,
    Streaming { _keepalive: InactiveReceiver<BroadcastResult<T>> },
}
```
Transfer rule: Apply when the application has heterogeneous tasks with shared lifecycle semantics: rate limit, retry, cancellation, and result delivery. Avoid for simple fire-and-forget tasks where a channel and a loop would be clearer.
Verification hook: Tests should cover transient retry, non-transient failure, queue close behavior, subscriber keepalive, rate-limit wait, and aborting the active task.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/CodeEDA

### Concept: Repo skipped because no Rust implementation was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/CodeEDA` (`rg --files -g 'Cargo.toml'` and `rg --files -g '*.rs'` returned zero files)
Why it matters: No Rust source or Cargo metadata exists in this assigned repo, so extracting idiomatic Rust patterns would be speculative.
Reusable code shape:
```text
N/A: no Rust files found.
```
Transfer rule: Skip until a Rust crate, Tauri shell, parser, or code-generation component is added.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/CodeEDA -g 'Cargo.toml' -g '*.rs'`

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/accio-tools

### Concept: Workspace shell with shared core surfaced through Tauri commands and a CLI
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/A02-routers-solutions/solution01/Cargo.toml`; `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/A02-routers-solutions/solution01/src/lib.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/A02-routers-solutions/solution01/src-tauri/src/commands.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/A02-routers-solutions/solution01/crates/router-cli-command-surface/src/main.rs`
Why it matters: The same routing core is consumed by a Tauri UI and a command-line interface. The app crate owns serializable request/response DTOs and pure orchestration (`run_cpu_preview_only`, `route_tools_with_judge`), while `src-tauri` is a thin `#[tauri::command]` adapter and the CLI is another thin adapter that parses args and prints JSON. This keeps UI-specific code from infecting the domain engine.
Reusable code shape:
```rust
// shared app/core crate
pub async fn route_tools_with_judge(
    request: RouteToolsRequestData,
) -> Result<RouteToolsResponseData, AppError> {
    let mut response = run_cpu_preview_only(request.clone())?;
    let Some(api_key) = request.api_key.as_deref().map(str::trim).filter(|v| !v.is_empty()) else {
        return Ok(response);
    };
    response.judge_decision = Some(judge_candidate_tools_with_openai(&judge_request, &config).await?);
    Ok(response)
}

// Tauri adapter
#[tauri::command]
pub async fn route_tools_for_query(
    request: RouteToolsRequestData,
) -> Result<RouteToolsResponseData, AppError> {
    route_query_inner(request).await
}

// CLI adapter
let response = run_route_with_runtime(create_route_request_data(&options, true)?)?;
serde_json::to_string_pretty(&response)?;
```
Transfer rule: Apply when a Rust domain engine must serve desktop UI, CLI, tests, and later automation. Avoid duplicating business logic in Tauri command handlers; keep handlers as serialization/error-boundary adapters.
Verification hook: Run core tests plus CLI command tests; review that `src-tauri/src/commands.rs` contains no routing logic beyond forwarding to the shared crate.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/before-i-go

### Concept: Repo skipped because no Rust implementation was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go` (`rg --files -g 'Cargo.toml'` and `rg --files -g '*.rs'` returned zero files)
Why it matters: This assigned repo has no Rust files in the checkout, so there is no source-backed Rust pattern to extract.
Reusable code shape:
```text
N/A: no Rust code found.
```
Transfer rule: Skip for Rust pattern mining unless a Rust implementation is later added.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/before-i-go -g 'Cargo.toml' -g '*.rs'`

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/dobby-subagent-code-summarizer

### Concept: Shared inference engine with semaphore-gated blocking work
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/dobby-subagent-code-summarizer/src/parallel_agents.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/dobby-subagent-code-summarizer/src/inference.rs`
Why it matters: The repo aims to reuse one initialized inference engine behind `Arc<OptimizedInferenceEngine>` and gate concurrent summarization with a `tokio::sync::Semaphore`. CPU-bound inference is pushed into `spawn_blocking`, while async tasks own the concurrency permit and collect `(chunk, summary)` pairs. This is a useful shape for local ML workloads where model/tokenizer initialization is expensive but per-input work can be parallelized up to a hardware-safe limit.
Reusable code shape:
```rust
pub struct ParallelAgentSystem {
    engine: Arc<OptimizedInferenceEngine>,
    semaphore: Arc<Semaphore>,
}

let handle = tokio::spawn(async move {
    let permit = semaphore.acquire().await.expect("semaphore open");
    let chunk_for_worker = chunk.clone();
    let result = tokio::task::spawn_blocking(move || {
        engine.summarize_chunk_with_generation_config(&chunk_for_worker, &prompt, &generation_config)
    }).await;
    drop(permit);

    let summary = match result {
        Ok(Ok(summary)) => summary,
        Ok(Err(err)) => format!("ERROR: {err}"),
        Err(err) => format!("TASK ERROR: {err}"),
    };
    (chunk, summary)
});
```
Transfer rule: Apply when a heavyweight, read-mostly engine can be shared safely and work is CPU-bound or blocking. Avoid copying the weaker pattern that throttles by popping one handle after reaching a limit; prefer spawning all tasks with a semaphore permit acquired inside each task, or use `JoinSet`/`FuturesUnordered` for clearer completion handling.
Verification hook: Run `cargo test` before reuse; review that the engine type is actually `Send + Sync`, all spawned blocking work owns its data, and the number of concurrent permits matches memory/CPU limits rather than the number of logical "agents."

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/fawkes-body-doubling-phoenix

### Concept: Repo skipped because no Rust implementation was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/fawkes-body-doubling-phoenix` (`rg --files -g 'Cargo.toml'` and `rg --files -g '*.rs'` returned zero files)
Why it matters: The assigned repository does not contain Rust source in this checkout, so there are no Rust idioms to extract.
Reusable code shape:
```text
N/A: no Rust implementation files found.
```
Transfer rule: Skip until the project adds a Rust backend, Tauri shell, CLI, parser, or generator.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/fawkes-body-doubling-phoenix -g 'Cargo.toml' -g '*.rs'`

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science

### Concept: Single-file `rust-script` generator with typed CLI include/exclude flags
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science/core/src/main/java/org/neo4j/gds/core/compression/packed/gen_packing.rs`
Why it matters: A Java project uses one Rust script to generate repetitive Java packing code. The script embeds Cargo dependencies in a `rust-script` header, validates CLI inputs with `clap`, represents generated sections as bitflag-like enum variants, and defaults to stdout unless `--output` is explicitly requested. This is a pragmatic pattern for bringing Rust's type system and code-generation ergonomics into non-Rust repositories without adding a full Cargo workspace.
Reusable code shape:
```rust
#!/usr/bin/env rust-script
//! ```cargo
//! [dependencies]
//! clap = "3"
//! gen_java = { git = "https://github.com/knutwalker/gen_java" }
//! ```

fn parse_block_size(s: &str) -> Result<u32, String> {
    let n = s.parse().map_err(|e| format!("must be a number: {e}"))?;
    if !(1..=u64::BITS).contains(&n) || !n.is_power_of_two() {
        return Err("must be a power-of-two block size in range".into());
    }
    Ok(n)
}

#[derive(Copy, Clone)]
#[repr(u8)]
enum Includes { Pack = 1, Unpack = 2, PackLoop = 4, UnpackLoop = 8 }

let includes = matches.get_many::<Includes>("include")
    .map(|xs| xs.map(|x| *x as u8).fold(0, |a, b| a | b))
    .unwrap_or(default_includes);
```
Transfer rule: Apply for deterministic source generation where introducing a full Rust crate would be too heavy. Avoid for production runtime logic; scripts should be reproducible, idempotent, and preferably checked by regenerated-output diffs.
Verification hook: Run the script once to stdout and once with `--output --force`, then compare generated Java against the checked-in file; test invalid `--block-size` values for validation errors.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker

### Concept: Mmap-backed graph runtime hidden behind query and adjacency traits
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/src/runtime.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/tests/graph_adjacency_runtime_contract.rs`
Why it matters: Knight Bus exposes memory-mapped graph snapshots through small traits: `WalkQueryRuntime` for product-level neighbor queries and `GraphAdjacencyRuntime` for low-level cursor access. The concrete `MmapWalkRuntime` owns mmap files and validates dense node IDs, while callers consume iterators (`NeighborCursor`, `EdgeCursor`) instead of raw bytes. This separates binary layout from graph algorithms and tests.
Reusable code shape:
```rust
pub trait GraphAdjacencyRuntime {
    fn node_count(&self) -> u64;
    fn relationship_count(&self) -> u64;
    fn neighbors(&self, node: DenseNodeId, direction: WalkDirection)
        -> Result<NeighborCursor<'_>, Error>;
}

impl GraphAdjacencyRuntime for MmapWalkRuntime {
    fn neighbors(&self, node: DenseNodeId, direction: WalkDirection) -> Result<NeighborCursor<'_>, Error> {
        self.validate_dense_id_now(node.get())?;
        let (offsets, peers) = match direction {
            WalkDirection::Forward => (&self.forward_offsets, &self.forward_peers),
            WalkDirection::Backward => (&self.reverse_offsets, &self.reverse_peers),
        };
        let start = read_u64_from_mmap(offsets, node.get() as usize) as usize;
        let end = read_u64_from_mmap(offsets, node.get() as usize + 1) as usize;
        Ok(NeighborCursor::new(peers, start, end))
    }
}
```
Transfer rule: Apply when a binary artifact should be queryable without loading the whole graph into heap memory. Avoid exposing mmap slices directly to higher-level logic; use typed cursors and validate bounds at the runtime edge.
Verification hook: Contract tests should assert node/relationship counts, forward/reverse cursor contents, out-of-range dense IDs, and parity with a simple truth index loaded from CSV.

### Concept: Snapshot manifest as compatibility contract for binary sidecar artifacts
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/src/snapshot.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/tests/snapshot_manifest_v3_contract.rs`
Why it matters: The snapshot writer emits multiple binary files plus a JSON manifest naming each file, data width, storage mode, generation metadata, logical orientations, and sidecar catalog entries. Tests force the manifest to round-trip, prove older v2 manifests still open, and assert size accounting. This is a durable-artifact pattern for graph snapshots, indexes, embeddings, and agent cache formats.
Reusable code shape:
```rust
pub trait SnapshotArtifactWriter {
    fn write_snapshot_artifacts(
        &self,
        graph_data: &NormalizedGraphData,
        output_dir: &Path,
    ) -> Result<SnapshotBuildSummary, Error>;
}

fn write_snapshot_artifacts(...) -> Result<SnapshotBuildSummary, Error> {
    let manifest = SnapshotManifest::new_immutable_dual_csr(node_count, edge_count, ...);
    write_manifest_file(output_dir, &manifest)?;
    write_node_records_file(output_dir, &node_records)?;
    write_u64_values_file(output_dir.join(&manifest.forward_offsets), &forward_offsets)?;
    write_u32_values_file(output_dir.join(&manifest.forward_peers), &forward_peers)?;
    let snapshot_size_bytes = compute_snapshot_size_bytes(output_dir, &manifest)?;
    Ok(SnapshotBuildSummary { snapshot_size_bytes, ..summary })
}
```
Transfer rule: Apply when a generated artifact has more than one file or must survive version upgrades. Avoid implicit filename conventions without a manifest; future migrations and compatibility tests become much harder.
Verification hook: Add contract tests that serialize/deserialize the manifest, mutate it to the previous version, open it with the runtime, and assert `snapshot_size_bytes == topology_bytes + sidecar_bytes`.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/mordor-mcp

### Concept: MCP stdio server as a thin JSON-RPC loop over a tool registry
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/mordor-mcp/crates/fe-mcp-server/src/server.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/mordor-mcp/crates/fe-mcp-server/src/tools/mod.rs`
Why it matters: Mordor keeps the MCP transport boring: read newline-delimited JSON-RPC from stdin, parse into a request enum, dispatch `initialize`, `tools/list`, and `tools/call`, and write one JSON response per line to stdout. Tool behavior lives behind an async `Tool` trait and a registry. This isolates protocol mechanics from tool implementation and makes it easy for agents to add tools without changing the server loop.
Reusable code shape:
```rust
#[async_trait]
pub trait Tool: Send + Sync {
    fn definition(&self) -> ToolDefinition;
    async fn call(&self, params: Value, project_root: &Path) -> ToolCallResult;
}

while let Some(line) = lines.next_line().await? {
    let request: JsonRpcRequest = match serde_json::from_str(line.trim()) {
        Ok(req) => req,
        Err(err) => {
            write_response(&mut stdout, &JsonRpcResponse::error(None, -32700, err.to_string())).await?;
            continue;
        }
    };
    if let Some(response) = handle_request(&request, &registry, &project_root).await {
        write_response(&mut stdout, &response).await?;
    }
}
```
Transfer rule: Apply when building local MCP tools where stdio is enough and each tool can own its own JSON schema. Avoid mixing logs into stdout; stdout must remain protocol-only, with tracing/logging on stderr.
Verification hook: Integration-test `initialize`, `tools/list`, unknown method, invalid JSON, and one `tools/call`; assert each response is exactly one JSON line and no log text appears on stdout.

### Concept: Cascading verification pipeline with tool-specific runners and parsers
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/mordor-mcp/crates/fe-verify/src/runners/mod.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/mordor-mcp/crates/fe-verify/src/pipeline.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/mordor-mcp/crates/fe-verify/src/runners/typescript.rs`
Why it matters: Frontend verification is modeled as lint -> typecheck -> tests. Each external command implements `VerificationRunner`, returns raw stdout/stderr plus exit code, and the pipeline selects the matching parser based on the detected active tool. The pipeline early-terminates on lint/type failures and marks later phases skipped, giving agents a structured summary instead of a wall of terminal output.
Reusable code shape:
```rust
#[async_trait]
pub trait VerificationRunner: Send + Sync {
    fn name(&self) -> &str;
    async fn run(&self, root: &Path, files: &[&Path]) -> Result<RunnerOutput, VerifyError>;
}

if let Some(linter) = &self.linter {
    let output = linter.run(project_root, affected_files).await?;
    let step = parse_linter_output(&output.stdout);
    if step.status == "fail" {
        summary.types = StepResult::skipped("Skipped due to lint errors");
        summary.tests = TestStepResult::skipped("Skipped due to lint errors");
        summary.finalize();
        return Ok(summary);
    }
}
```
Transfer rule: Apply when verification has a natural dependency order and later checks create noise if earlier checks already fail. Avoid running the whole suite blindly in agent loops; structured skipped phases are often more actionable.
Verification hook: Fixture tests should cover lint failure skips type/tests, type failure skips tests, and all-pass path; parser tests should use captured stdout for ESLint/Biome/tsc/Jest/Vitest.

### Concept: Validated byte-range edit set applied in reverse order
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/mordor-mcp/ast-surgeon/crates/ast-surgeon-core/src/edit.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/mordor-mcp/ast-surgeon/crates/ast-surgeon-core/src/operations/mod.rs`
Why it matters: AST/code-mod operations compute byte-range `TextEdit`s against the original source. Mordor sorts edits, rejects out-of-bounds and overlapping ranges, then applies replacements from the end of the source backward so earlier byte offsets remain valid. This is the core safety pattern behind reliable code modification tools.
Reusable code shape:
```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TextEdit {
    pub start: usize,
    pub end: usize,
    pub replacement: String,
    pub label: String,
    #[serde(default)]
    pub priority: i32,
}

impl EditSet {
    pub fn new(mut edits: Vec<TextEdit>, source_len: usize) -> Result<Self, EditConflict> {
        edits.sort_by(|a, b| a.start.cmp(&b.start).then(a.end.cmp(&b.end)).then(a.priority.cmp(&b.priority)));
        validate_bounds_and_overlaps(&edits, source_len)?;
        Ok(Self { edits })
    }

    pub fn apply(&self, source: &str) -> String {
        let mut result = source.to_string();
        for edit in self.edits.iter().rev() {
            result.replace_range(edit.start..edit.end, &edit.replacement);
        }
        result
    }
}
```
Transfer rule: Apply to any code-editing, AST rewrite, or multi-replacement tool. Avoid line/column replacement for source mutation unless you convert once to byte ranges and validate against the exact source string being edited.
Verification hook: Unit tests must cover single edit, multiple non-overlapping edits, same-position insert priorities, overlap rejection, out-of-bounds rejection, and merging edit sets from multiple operations.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/nostd-union-find

### Concept: `no_std` const-generic data structure with structured no-std errors
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-union-find/src/lib.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-union-find/src/error.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-union-find/tests/property_based_union_find.rs`
Why it matters: The crate implements union-find without heap allocation by storing `parent` and `rank` arrays as `[usize; N]`, where `N` is a const generic. It uses `#![cfg_attr(not(test), no_std)]` and `thiserror_no_std::Error`, so the library remains embedded-friendly while tests and benches can use `std`. This is a clean pattern for small algorithms that need deterministic memory.
Reusable code shape:
```rust
#![cfg_attr(not(test), no_std)]

#[derive(Debug, Clone)]
pub struct UnionFind<const N: usize> {
    parent: [usize; N],
    rank: [usize; N],
}

#[derive(thiserror_no_std::Error, Debug, Clone, Copy, PartialEq, Eq)]
pub enum UnionFindError {
    #[error("Index {index} out of bounds (capacity: {capacity})")]
    IndexOutOfBounds { index: usize, capacity: usize },
}

impl<const N: usize> UnionFind<N> {
    pub fn find_set_with_compression(&mut self, x: usize) -> Result<usize, UnionFindError> {
        if x >= N { return Err(UnionFindError::IndexOutOfBounds { index: x, capacity: N }); }
        if self.parent[x] != x {
            self.parent[x] = self.find_set_with_compression(self.parent[x])?;
        }
        Ok(self.parent[x])
    }
}
```
Transfer rule: Apply for bounded data structures in embedded, kernel, WASM, or deterministic-memory contexts. Avoid if capacity is not known at compile time or if large `N` would put too much data on the stack; then use an allocator-backed variant behind a feature.
Verification hook: Run unit tests, property tests, and Criterion benches; property tests should assert commutativity, transitivity, idempotent find, bounds errors, and equivalence against a simple reference implementation.

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/plotly.py

### Concept: Repo skipped because no Rust implementation was present
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/plotly.py` (`rg --files -g 'Cargo.toml'` and `rg --files -g '*.rs'` returned zero files)
Why it matters: The checkout is a Python visualization library. It does not provide Rust source, Rust bindings, or parser implementation evidence for this shard.
Reusable code shape:
```text
N/A: no Rust implementation files found.
```
Transfer rule: Skip for Rust idiom extraction; revisit only if Rust extension modules or build tooling appear.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/plotly.py -g 'Cargo.toml' -g '*.rs'`

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/streamlit

### Concept: Repo skipped because no Rust implementation was present
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/streamlit` (`rg --files -g 'Cargo.toml'` and `rg --files -g '*.rs'` returned zero files)
Why it matters: Streamlit may contain useful app architecture ideas, but this shard requires Rust/Rust-adjacent implementation evidence. No Rust source was available in this checkout.
Reusable code shape:
```text
N/A: no Rust code to quote.
```
Transfer rule: Skip for this Rust pattern archive unless a Rust backend, native extension, or Rust parser component is added.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/streamlit -g 'Cargo.toml' -g '*.rs'`

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/claude-peers-mcp

### Concept: Repo skipped because no Rust implementation was present
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/claude-peers-mcp` (`rg --files -g 'Cargo.toml'` and `rg --files -g '*.rs'` returned zero files)
Why it matters: The repository may still be relevant to MCP behavior, but this shard is constrained to Rust/Rust-adjacent implementation patterns. Without Rust files or Cargo metadata, there is no source-backed Rust pattern to extract.
Reusable code shape:
```text
N/A: no Rust code in this checkout.
```
Transfer rule: Skip for Rust pattern extraction; revisit only if a Rust MCP server, Rust SDK binding, or `Cargo.toml` appears.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/claude-peers-mcp -g 'Cargo.toml' -g '*.rs'`

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/dbt-core

### Concept: Repo skipped because parser references are not Rust parser implementations
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/dbt-core` (`rg --files -g 'Cargo.toml'` and `rg --files -g '*.rs'` returned zero files; parser-ish files exist in the Python project)
Why it matters: dbt-core contains architecture and parser concepts, but this pass requires source-backed Rust/Rust-adjacent patterns. Mining Python parser structure as Rust guidance would blur the evidence boundary.
Reusable code shape:
```text
N/A: no Rust implementation files found.
```
Transfer rule: Do not transfer non-Rust parser architecture into this Rust reference unless a Rust crate, generated Rust parser, or Rust binding layer is present.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/dbt-core -g 'Cargo.toml' -g '*.rs' -g '*parser*'`


## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/pm2dev`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Rust Architecture Slice From pm2dev
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/pm2dev/gitignored-references/refer-repo/rustc_codegen_jvm/shim-metadata-gen/src/main.rs` (sample Rust source file)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 9910 Rust files, 800 Cargo manifests, and 0 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. No parser keyword sample was captured; treat this as a general Rust architecture or idiom candidate.
Reusable code shape:
```rust
use std::collections::BTreeMap;
use std::env;
use std::fs;
use std::io::{Cursor, Read, Write};
use std::path::PathBuf;
use std::process::exit;

use ristretto_classfile::{
    ClassFile, MethodAccessFlags,
};
use serde::Serialize;
use zip::ZipArchive;

#[derive(Serialize, Debug, Clone)]
struct ShimInfo {
    descriptor: String,
    is_static: bool,
}

// Use BTreeMap to keep the shims sorted by function (key) name
type ShimMap = BTreeMap<String, ShimInfo>;
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/personal-repos-lane/pm2dev -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/rust-100-exercises-notes`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From rust-100-exercises-notes
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/rust-100-exercises-notes/helpers/mdbook-exercise-linker/src/main.rs:34` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 135 Rust files, 102 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
}

fn handle_preprocessing(pre: &dyn Preprocessor) -> Result<(), Error> {
    let (ctx, book) = CmdPreprocessor::parse_input(io::stdin())?;

    let book_version = Version::parse(&ctx.mdbook_version)?;
    let version_req = VersionReq::parse(mdbook::MDBOOK_VERSION)?;

    if !version_req.matches(&book_version) {
        eprintln!(
            "Warning: The {} plugin was built against version {} of mdbook, \
             but we're being called from version {}",
            pre.name(),
            mdbook::MDBOOK_VERSION,
            ctx.mdbook_version
        );
    }

    let processed_book = pre.run(&ctx, book)?;
    serde_json::to_writer(io::stdout(), &processed_book)?;

    Ok(())
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/personal-repos-lane/rust-100-exercises-notes -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/that-in-rust-org-github`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/that-in-rust-org-github`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/that-in-rust-org-github -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/useful-rc-files`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/useful-rc-files`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/useful-rc-files -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/zz_archived_journal2023`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/zz_archived_journal2023`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/zz_archived_journal2023 -g 'Cargo.toml' -g '*.rs'`


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/RAPx`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From RAPx
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/RAPx/rapx/src/utils/log.rs:14` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 205 Rust files, 71 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
fn log_level() -> LevelFilter {
    if let Ok(s) = std::env::var("RAP_LOG") {
        match s.parse() {
            Ok(level) => return level,
            Err(err) => eprintln!("RAP_LOG is invalid: {err}"),
        }
    }
    LevelFilter::Info
}

/// Detect `RAP_LOG` environment variable first; if it's not set,
/// default to INFO level.
pub fn init_log() -> Result<(), fern::InitError> {
    let dispatch = Dispatch::new().level(log_level());

    let color_line = ColoredLevelConfig::new()
        .error(Color::Red)
        .warn(Color::Yellow)
        .info(Color::White)
        .debug(Color::Blue)
        .trace(Color::Cyan);
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/RAPx -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Skipped Repo: `/Users/amuldotexe/Desktop/reference-repos-yard/cachebro`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/cachebro`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/reference-repos-yard/cachebro -g 'Cargo.toml' -g '*.rs'`


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/creusot`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From creusot
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/creusot/cargo-creusot/src/new.rs:3` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 642 Rust files, 16 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
use anyhow::Result;
use cargo_metadata::semver::Version;
use clap::Parser;
use creusot_setup::creusot_paths;
use std::{
    fs,
    io::Write,
    path::{Path, PathBuf},
};

#[derive(Debug, Parser)]
pub struct NewArgs {
    /// Package name
    pub name: String,
    #[clap(flatten)]
    pub args: NewInitArgs,
}

#[derive(Debug, Parser)]
pub struct InitArgs {
    /// Package name (default: name of the current directory)
    pub name: Option<String>,
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/creusot -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/flux`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From flux
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/flux/xtask/src/main.rs:614` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 1130 Rust files, 24 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
let mut artifacts = vec![];
        let reader = std::io::BufReader::new(child.stdout.take().unwrap());
        for message in cargo_metadata::Message::parse_stream(reader) {
            match message.unwrap() {
                Message::CompilerMessage(msg) => {
                    println!("{msg}");
                }
                Message::CompilerArtifact(artifact) => {
                    artifacts.push(artifact);
                }
                _ => (),
            }
        }

        check_status(child.wait()?)?;

        Ok(artifacts)
    }
}

fn remove_path(path: &Path) -> anyhow::Result<()> {
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/flux -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/marker`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Proc Macro Expansion Pattern From marker
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/marker/marker_rustc_driver/src/context.rs:219` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 178 Rust files, 10 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
pos: marker_api::span::SpanPos,
    ) -> Option<marker_api::span::FilePos<'ast>> {
        self.marker_converter.try_to_span_pos(
            self.rustc_converter.to_syntax_context(file.span_src()),
            self.rustc_converter.to_byte_pos(pos),
        )
    }

    fn span_expn_info(
        &'ast self,
        expn_id: marker_api::common::ExpnId,
    ) -> Option<&'ast marker_api::span::ExpnInfo<'ast>> {
        let id = self.rustc_converter.to_expn_id(expn_id);
        self.marker_converter.try_to_expn_info(id)
    }

    fn symbol_str(&'ast self, api_id: SymbolId) -> &'ast str {
        let sym = self.rustc_converter.to_symbol(api_id);
        // The lifetime is fake, as documented in [`rustc_span::Span::as_str()`].
        // It'll definitely live longer than the `'ast` lifetime, it's transmuted to.
        let rustc_str: &str = sym.as_str();
        // # Safety
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/marker -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/polonius`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From polonius
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/polonius/src/cli.rs:114` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 39 Rust files, 3 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
(duration, output)
}

// Parses the provided CLI arguments into `Options`
pub fn options_from_args() -> Result<Options, Error> {
    let mut args = pico::Arguments::from_env();

    // 1) print optional information before exiting: help, version
    let show_help = args.contains(["-h", "--help"]);
    if show_help {
        let variants: Vec<_> = Algorithm::variants()
            .iter()
            .map(|s| s.to_string())
            .collect();

        println!(
            r#"{name} {version}
{description}

USAGE:
    polonius [FLAGS] [OPTIONS] <fact_dirs>...
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/polonius -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_jvm`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From rustc_codegen_jvm
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_jvm/src/lower2.rs:106` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 46 Rust files, 20 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
method.name_index = name_index;
            method.descriptor_index = descriptor_index;
            method.attributes.push(code_attribute);
            // Add MethodParameters attribute (skip for constructors as they often have synthetic params)
            if function.name != "<init>" {
                method.attributes.push(method_parameters_attribute);
            }

            methods.push(method);
        }

        // Add a default constructor if none was provided in OOMIR
        if !has_constructor && !module.functions.contains_key("<init>") {
            methods.push(create_default_constructor(&mut main_cp, super_class_index)?);
        }

        let mut class_file = ClassFile {
            version: Version::Java8 { minor: 0 },
            constant_pool: main_cp, // Move the main constant pool here
            access_flags: ClassAccessFlags::PUBLIC | ClassAccessFlags::SUPER,
            this_class: this_class_index,
            super_class: super_class_index,
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_jvm -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/zed`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From zed
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/zed/crates/acp_tools/src/acp_tools.rs:1` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 1763 Rust files, 242 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
use std::{collections::HashSet, fmt::Display, rc::Rc, sync::Arc};

use agent_client_protocol::schema as acp;
use agent_servers::{AcpDebugMessage, AcpDebugMessageContent, AcpDebugMessageDirection};
use agent_ui::agent_connection_store::AgentConnectionStatus;
use agent_ui::{Agent, AgentConnectionStore, AgentPanel};
use collections::HashMap;
use gpui::{
    App, Empty, Entity, EventEmitter, FocusHandle, Focusable, ListAlignment, ListState,
    SharedString, StyleRefinement, Subscription, Task, TextStyleRefinement, WeakEntity, Window,
    actions, list, prelude::*,
};
use language::LanguageRegistry;
use markdown::{CodeBlockRenderer, CopyButtonVisibility, Markdown, MarkdownElement, MarkdownStyle};
use project::{AgentId, Project};
use settings::Settings;
use theme_settings::ThemeSettings;
use ui::{
    ContextMenu, CopyButton, DropdownMenu, DropdownStyle, IconPosition, Tooltip, WithScrollbar,
    prelude::*,
};
use util::ResultExt as _;
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/zed -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.

## CodeGraphContext Evidence Appendix

### Concept: Graph-Indexed Snapshot Boundary Cross-Check
Evidence: CodeGraphContext run `/tmp/codex-code-intel/codegraphcontext/knight-bus-graph-walker-20260706-225543` reported 1 repository, 258 files, 560 functions, 6 traits, 66 structs, 25 enums, and 80 modules; `cgc find name build_snapshot_from_paths` returned `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/src/app.rs:17`.
Why it matters: CodeGraphContext gave a graph-shaped map of the snapshot builder and runtime boundary, then direct source reads confirmed the actual transfer shape. `build_snapshot_from_paths()` delegates into `build_snapshot_from_paths_with_options()`, which delegates to the low-RAM builder; `MmapWalkRuntime::open()` reads and validates `SnapshotManifest` before exposing query APIs. This is a useful Rust-agent pattern for separating public ergonomic functions from memory-sensitive implementation and read-only runtime validation.
Reusable code shape:
```rust
pub fn build_snapshot_from_paths(
    nodes_path: &Path,
    edges_path: &Path,
    output_dir: &Path,
) -> Result<SnapshotBuildSummary, KnightBusError> {
    build_snapshot_from_paths_with_options(
        nodes_path,
        edges_path,
        output_dir,
        &SnapshotBuildOptions::default(),
    )
}
```
Transfer rule: Use CodeGraphContext to identify likely API seams, then verify the actual behavior in source before asking an agent to copy the shape. Transfer this pattern when a project needs a small public facade over a heavier builder plus a manifest-validated mmap runtime.
Verification hook: Re-run `cgc stats` and `cgc find name build_snapshot_from_paths` against the recorded output directory, then re-open `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/src/app.rs:17`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/src/low_ram.rs:44`, and `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/src/runtime.rs:170` before adapting it.
