# Rust Patterns 202606 Part 4

Purpose: capture Rust and Rust-adjacent architecture, idiom, parser, Tree-sitter, code-intelligence, async, CLI, API, storage, verification, and operational patterns discovered repo-by-repo under `/Users/amuldotexe/Desktop`.

Evidence policy: every non-obvious pattern should name the repository, file path, and why the code is reusable. Codebase-memory graph evidence is useful for discovery, but source paths and snippets are the authority.

Shard owner: parallel worker 4.
Shard repo count: 31.

## Assigned Repository Shard

- `/Users/amuldotexe/Desktop/notes-plans-hub/hogwarts202603`
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs`
- `/Users/amuldotexe/Desktop/oss-read-only/auron`
- `/Users/amuldotexe/Desktop/oss-read-only/dask`
- `/Users/amuldotexe/Desktop/oss-read-only/hermes-agent`
- `/Users/amuldotexe/Desktop/oss-read-only/omnigraph`
- `/Users/amuldotexe/Desktop/oss-read-only/pi_agent_rust`
- `/Users/amuldotexe/Desktop/oss-read-only/sail`
- `/Users/amuldotexe/Desktop/oss-read-only/tauri`
- `/Users/amuldotexe/Desktop/oss-read-only/zed-gpui`
- `/Users/amuldotexe/Desktop/personal-repos-lane/JobSearchGames`
- `/Users/amuldotexe/Desktop/personal-repos-lane/apache-spark-shallow`
- `/Users/amuldotexe/Desktop/personal-repos-lane/confido-exploration-01`
- `/Users/amuldotexe/Desktop/personal-repos-lane/ebooks2024`
- `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network-message-queue-visual-lab`
- `/Users/amuldotexe/Desktop/personal-repos-lane/iiwii01`
- `/Users/amuldotexe/Desktop/personal-repos-lane/mermish`
- `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity`
- `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve-local-llm-server`
- `/Users/amuldotexe/Desktop/personal-repos-lane/reducto`
- `/Users/amuldotexe/Desktop/personal-repos-lane/servo-test-202411`
- `/Users/amuldotexe/Desktop/personal-repos-lane/tweetbook202409`
- `/Users/amuldotexe/Desktop/personal-repos-lane/zip-revelio`
- `/Users/amuldotexe/Desktop/personal-repos-lane/zztweets-of-amuldotexe2023`
- `/Users/amuldotexe/Desktop/reference-repos-yard/aquascope`
- `/Users/amuldotexe/Desktop/reference-repos-yard/codemogger`
- `/Users/amuldotexe/Desktop/reference-repos-yard/fff.nvim`
- `/Users/amuldotexe/Desktop/reference-repos-yard/kani`
- `/Users/amuldotexe/Desktop/reference-repos-yard/miri`
- `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_clr`
- `/Users/amuldotexe/Desktop/reference-repos-yard/tauri-template`

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

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/container_registry-rs-20260706-223352`; generated discovery query files were empty, so the patterns below are verified directly against source.

### Concept: Async object-safe storage boundary with boxed IO streams
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs/src/storage.rs`
Why it matters: The registry keeps HTTP routing independent from persistence by hiding the filesystem backend behind a `Send + Sync` async trait. The trait returns `Option` for lookup miss, domain errors for invalid operations, and boxed `AsyncRead`/`AsyncWrite` streams for blob bodies. This is a reusable shape when an agent needs to make a service testable without committing every caller to one concrete storage type.
Reusable code shape:
```rust
#[async_trait]
trait RegistryStorage: Send + Sync {
    async fn begin_new_upload(&self) -> Result<Uuid, Error>;

    async fn get_blob_reader(
        &self,
        digest: Digest,
    ) -> Result<Option<Box<dyn AsyncRead + Send + Unpin>>, Error>;

    async fn get_upload_writer(
        &self,
        start_at: u64,
        upload: Uuid,
    ) -> Result<Box<dyn AsyncWrite + Send + Unpin>, Error>;

    async fn finalize_upload(&self, upload: Uuid, hash: Digest) -> Result<(), Error>;
}
```
Transfer rule: Apply when service handlers should depend on capabilities instead of a storage implementation, especially for upload/download services that stream data. Avoid if the backend type is always known and monomorphization is more valuable than object safety.
Verification hook: Handler code should only call trait methods through the boundary; add integration tests with temporary storage and compile-check object safety by storing `Box<dyn RegistryStorage>`.

### Concept: Blocking hash validation offloaded from async filesystem workflow
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs/src/storage.rs`
Why it matters: `finalize_upload` performs async existence checks and async rename, but pushes CPU/blocking file hashing into `tokio::task::spawn_blocking`. It also uses a heap buffer because a large fixed stack buffer would be risky. This is the right shape for async services that must validate content without starving the runtime.
Reusable code shape:
```rust
let actual = {
    let upload_path = upload_path.clone();
    tokio::task::spawn_blocking::<_, Result<Digest, Error>>(move || {
        let mut src = fs::File::open(upload_path).map_err(Error::Io)?;
        let mut buf = vec![0; BUFFER_SIZE];
        let mut hasher = sha2::Sha256::new();

        loop {
            let read = src.read(buf.as_mut()).map_err(Error::Io)?;
            if read == 0 {
                break;
            }
            hasher.update(&buf[..read]);
        }

        Ok(Digest::new(hasher.finalize().into()))
    })
}
.await
.map_err(Error::BackgroundTaskPanicked)??;

if actual != digest {
    return Err(Error::DigestMismatch);
}
```
Transfer rule: Apply when a request path needs synchronous filesystem or CPU-heavy validation before an async commit step. Avoid spawning for tiny in-memory checks where task handoff costs more than the work.
Verification hook: Test digest mismatch and missing upload paths; review for `.await` only outside the blocking closure and for `JoinError` being preserved as a distinct error.

### Concept: Safe HTTP error enum with `IntoResponse` as the only leak boundary
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs/src/lib.rs`
Why it matters: The registry centralizes user-visible error conversion in one enum, keeping source errors attached with `thiserror` while mapping each variant to stable HTTP status and sanitized response bodies. This pattern keeps handlers ergonomic with `?` without leaking internals or losing observability.
Reusable code shape:
```rust
#[derive(Debug, Error)]
pub enum RegistryError {
    #[error("missing item")]
    NotFound,
    #[error("permission denied")]
    PermissionDenied(#[from] MissingPermission),
    #[error(transparent)]
    Storage(#[from] storage::Error),
    #[error("failed to read incoming data stream")]
    IncomingReadFailed(#[source] axum::Error),
    #[error("local write failed")]
    LocalWriteFailed(#[source] io::Error),
}

impl IntoResponse for RegistryError {
    fn into_response(self) -> Response {
        match self {
            RegistryError::NotFound => (StatusCode::NOT_FOUND, "missing item").into_response(),
            RegistryError::PermissionDenied(_) => {
                (StatusCode::FORBIDDEN, "access to request resource was denied").into_response()
            }
            RegistryError::Storage(err) => err.into_response(),
            RegistryError::IncomingReadFailed(_) => {
                (StatusCode::INTERNAL_SERVER_ERROR, "could not read input stream").into_response()
            }
            RegistryError::LocalWriteFailed(_) => {
                (StatusCode::INTERNAL_SERVER_ERROR, "could not write locally").into_response()
            }
        }
    }
}
```
Transfer rule: Apply in axum services where domain errors need explicit status codes. Avoid returning raw `anyhow::Error` from handlers that face clients.
Verification hook: Add table tests for each error variant to assert status code and response body; review that sensitive source errors are not formatted into public 5xx bodies.

### Concept: Request body streaming into an async trait writer
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs/src/lib.rs`
Why it matters: Upload handlers avoid buffering the whole body by converting the body into a data stream and writing chunks into the storage writer. The handler also tracks completed bytes and flushes explicitly. This is a compact reusable shape for ingestion endpoints.
Reusable code shape:
```rust
let mut writer = registry.storage.get_upload_writer(0, upload).await?;
let mut body = request.into_body().into_data_stream();

let mut completed: u64 = 0;
while let Some(result) = body.next().await {
    let chunk = result.map_err(RegistryError::IncomingReadFailed)?;
    completed += chunk.len() as u64;
    writer
        .write_all(chunk.as_ref())
        .await
        .map_err(RegistryError::LocalWriteFailed)?;
}

writer.flush().await.map_err(RegistryError::LocalWriteFailed)?;
```
Transfer rule: Apply for HTTP ingestion where payloads can be large and backpressure matters. Avoid if the endpoint must validate a complete body before any write; in that case use a bounded body extractor and document the size limit.
Verification hook: Exercise uploads larger than a single HTTP body chunk and assert stored length and digest; review that body read errors and local write errors remain distinguishable.

### Concept: Feature-gated background service test harness with RAII shutdown
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/container_registry-rs/src/test_support.rs`
Why it matters: The crate exposes `build_for_testing` only behind the `test-support` feature. The harness owns temporary storage, starts axum on a background thread with its own Tokio runtime, and shuts down in `Drop` by closing a channel and joining the thread. This is a strong pattern for library crates that need realistic service tests without forcing test-only dependencies onto production users.
Reusable code shape:
```rust
pub struct RunningRegistry {
    bound_addr: SocketAddr,
    join_handle: Option<thread::JoinHandle<()>>,
    _temp_storage: Option<tempdir::TempDir>,
    shutdown: Option<tokio::sync::mpsc::Sender<()>>,
}

impl Drop for RunningRegistry {
    fn drop(&mut self) {
        drop(self.shutdown.take());
        if let Some(join_handle) = self.join_handle.take() {
            join_handle.join().expect("failed to join");
        }
    }
}
```
Transfer rule: Apply when integration tests need a real socket server and owned temporary resources. Avoid hidden background threads in unit tests that can be expressed as `tower::Service` calls.
Verification hook: Run tests under `--features test-support`; add a smoke test that starts the server, calls `bound_addr`, drops the handle, and verifies no temp directory or runtime keeps the process alive.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/omnigraph`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/omnigraph-20260706-223515`; pest parser files and compiler tests were verified directly with `rg` and source reads.

### Concept: Pest grammar module lowered through a diagnostic wrapper before AST construction
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/omnigraph/crates/omnigraph-compiler/src/query/parser.rs`
Why it matters: The parser exposes both a simple `parse_query` API and a richer `parse_query_diagnostic` API. The pest error is converted to a project diagnostic with an optional rendered span before ordinary parser lowering begins. This lets CLI/service callers choose between friendly diagnostics and a normal domain error while keeping the grammar-derived parser private.
Reusable code shape:
```rust
#[derive(Parser)]
#[grammar = "query/query.pest"]
struct QueryParser;

pub fn parse_query(input: &str) -> Result<QueryFile> {
    parse_query_diagnostic(input).map_err(|e| NanoError::Parse(e.to_string()))
}

pub fn parse_query_diagnostic(input: &str) -> std::result::Result<QueryFile, ParseDiagnostic> {
    let pairs = QueryParser::parse(Rule::query_file, input).map_err(pest_error_to_diagnostic)?;
    let mut queries = Vec::new();
    for pair in pairs {
        if let Rule::query_file = pair.as_rule() {
            for inner in pair.into_inner() {
                if let Rule::query_decl = inner.as_rule() {
                    queries.push(parse_query_decl(inner).map_err(nano_error_to_diagnostic)?);
                }
            }
        }
    }
    Ok(QueryFile { queries })
}
```
Transfer rule: Apply when building a DSL parser where human-facing diagnostics are first-class. Avoid exposing pest `Rule` and `Pair` types from the crate API; keep them in the parser module and return owned AST nodes.
Verification hook: Include parser tests for both successful AST shape and rejected syntax; for diagnostics, assert that parse failures include the expected message and, where available, a rendered span.

### Concept: Semantic parser validation layered after grammar acceptance
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/omnigraph/crates/omnigraph-compiler/src/query/parser.rs`; `/Users/amuldotexe/Desktop/oss-read-only/omnigraph/crates/omnigraph-compiler/src/query/parser_tests.rs`
Why it matters: The grammar accepts query annotations, but semantic rules such as "no duplicate @description" live in Rust lowering code. This separation keeps the grammar readable and lets semantic validation produce domain-specific messages that tests can assert exactly.
Reusable code shape:
```rust
match annotation_name {
    "description" => {
        if description.replace(value).is_some() {
            return Err(NanoError::Parse(format!(
                "query `{}` cannot include duplicate @description annotations",
                name
            )));
        }
    }
    "instruction" => {
        if instruction.replace(value).is_some() {
            return Err(NanoError::Parse(format!(
                "query `{}` cannot include duplicate @instruction annotations",
                name
            )));
        }
    }
    other => {
        return Err(NanoError::Parse(format!("unsupported query annotation: @{}", other)));
    }
}
```
Transfer rule: Apply when a grammar can recognize a construct syntactically but correctness depends on accumulated context. Avoid pushing all such checks into the grammar; tests become less expressive and errors become less domain-aware.
Verification hook: Add negative tests like `test_duplicate_query_description_is_rejected` and assert the exact domain phrase, not just that parsing failed.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/fff.nvim`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/fff.nvim-20260706-223515`; query parser claims were verified in `crates/fff-query-parser/src`.

### Concept: Borrowed query AST that preserves raw text while extracting constraints
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/fff.nvim/crates/fff-query-parser/src/parser.rs`; `/Users/amuldotexe/Desktop/reference-repos-yard/fff.nvim/crates/fff-query-parser/src/constraints.rs`
Why it matters: The parser returns `FFFQuery<'a>` that borrows from the original query string instead of allocating owned tokens. It keeps the raw query, extracted constraints, fuzzy text, and optional location together. This is a useful agent-assist pattern for fast interactive search: preserve user input for fallback/display while giving downstream rankers structured filters.
Reusable code shape:
```rust
pub enum FuzzyQuery<'a> {
    Parts(TextPartsBuffer<'a>),
    Text(&'a str),
    Empty,
}

pub struct FFFQuery<'a> {
    pub raw_query: &'a str,
    pub constraints: ConstraintVec<'a>,
    pub fuzzy_query: FuzzyQuery<'a>,
    pub location: Option<Location>,
}

pub enum Constraint<'a> {
    Extension(&'a str),
    Glob(&'a str),
    PathSegment(&'a str),
    FilePath(&'a str),
    FileType(&'a str),
    GitStatus(GitStatusFilter),
    Not(Box<Constraint<'a>>),
}
```
Transfer rule: Apply when parsing happens in a hot UI/search path and all token lifetimes can be tied to one input string. Avoid if parsed queries must outlive the input buffer or cross thread boundaries without ownership.
Verification hook: Unit tests should assert both structured constraints and fuzzy text preservation for mixed queries such as `src name *.rs !test /lib/ status:modified`.

### Concept: Single-token parser special cases protect fuzzy-search intent
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/fff.nvim/crates/fff-query-parser/src/parser.rs`
Why it matters: The parser treats one-token queries differently from multi-token queries: a lone filename-like token is fuzzy text, not a restrictive file path filter, and absolute paths with `:line` suffixes are allowed to reach location parsing. This is an important UX pattern for agentic tools because a technically valid parse can still violate user intent.
Reusable code shape:
```rust
if whitespace_count == 0 {
    if let Some(constraint) = parse_token(query, config) {
        let has_location_suffix = matches!(constraint, Constraint::PathSegment(_))
            && query.bytes().any(|b| b == b':')
            && query.bytes().rev().take_while(|&b| b != b':').all(|b| b.is_ascii_digit());

        let treat_as_text = matches!(constraint, Constraint::PathSegment(_))
            && config.treat_lone_path_as_text();

        if !matches!(constraint, Constraint::FilePath(_))
            && !has_location_suffix
            && !treat_as_text
        {
            constraints.push(constraint);
            return FFFQuery { raw_query, constraints, fuzzy_query: FuzzyQuery::Empty, location: None };
        }
    }
}
```
Transfer rule: Apply when a parser feeds a human-facing search box and some constraint syntax overlaps with ordinary search text. Avoid in strict configuration languages where ambiguity should be rejected instead of interpreted.
Verification hook: Add regression tests for lone filenames, escaped tokens such as `\\*.rs`, absolute paths with line suffixes, and multi-token queries where the same token should become a constraint.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/nostd-fmt-fixed-capacity-20260706-223515`; core buffer implementation was verified in `src/lib.rs`.

### Concept: `no_std` const-generic formatting buffer with `core::fmt::Write`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity/src/lib.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity/src/error.rs`
Why it matters: The crate uses `#![no_std]`, `#![deny(unsafe_code)]`, a stack-allocated `[u8; N]`, and a `core::fmt::Write` impl so callers can use `write!` without heap allocation. The important reusable idea is the invariant: only append valid UTF-8 `&str` data, update length after capacity checks, and expose `&str` views from the initialized prefix.
Reusable code shape:
```rust
#![no_std]
#![deny(unsafe_code)]

pub struct FixedBuffer<const N: usize> {
    buffer: [u8; N],
    length: usize,
}

impl<const N: usize> FixedBuffer<N> {
    pub const fn new() -> Self {
        Self { buffer: [0; N], length: 0 }
    }

    pub fn write_bytes_to_buffer_safe(&mut self, bytes: &[u8]) -> Result<()> {
        let remaining = self.capacity_remaining_bytes_available();
        if bytes.len() > remaining {
            return Err(FixedBufferError::CapacityExceeded {
                bytes_needed: bytes.len(),
                bytes_available: remaining,
            });
        }
        self.buffer[self.length..self.length + bytes.len()].copy_from_slice(bytes);
        self.length += bytes.len();
        Ok(())
    }

    pub fn as_str(&self) -> &str {
        core::str::from_utf8(&self.buffer[0..self.length])
            .expect("FixedBuffer invariant: buffer contents are always valid UTF-8")
    }
}

impl<const N: usize> core::fmt::Write for FixedBuffer<N> {
    fn write_str(&mut self, s: &str) -> core::fmt::Result {
        self.write_bytes_to_buffer_safe(s.as_bytes()).map_err(|_| core::fmt::Error)
    }
}
```
Transfer rule: Apply in embedded, kernel, WASM, logging, and parser formatting paths where allocation must be explicit or absent. Avoid writing arbitrary byte slices unless the API validates UTF-8 first; otherwise `as_str` can panic despite `unsafe` being absent.
Verification hook: Run normal tests plus Miri if available; add tests proving overflow leaves the buffer unchanged and Unicode writes do not split code points.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/zip-revelio`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/zip-revelio-20260706-223515`; archive reader and CLI were verified in `src/lib.rs`, `src/zip.rs`, and `src/main.rs`.

### Concept: Bounded archive reader trait separates size gate from directory scan
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/zip-revelio/src/lib.rs`; `/Users/amuldotexe/Desktop/personal-repos-lane/zip-revelio/src/zip.rs`
Why it matters: The crate models archive inspection as a trait with two async operations: validate the input size first, then read the central directory into simple metadata structs. Even though the concrete implementation is small, the shape is good for agentic code assist because the safety gate is explicit and testable before expensive parsing begins.
Reusable code shape:
```rust
pub const MAX_SIZE: u64 = 4 * 1024 * 1024 * 1024;

pub trait ZipReader: Send + Sync {
    fn validate_size(&self) -> impl Future<Output = Result<()>> + Send;
    fn read_directory(&self) -> impl Future<Output = Result<Directory>> + Send;
}

impl ZipReader for FileZipReader {
    async fn validate_size(&self) -> Result<()> {
        let metadata = tokio::fs::metadata(&self.path).await?;
        if metadata.len() > crate::MAX_SIZE {
            return Err(Error::SizeLimit { size: metadata.len() });
        }
        Ok(())
    }

    async fn read_directory(&self) -> Result<Directory> {
        let file = File::open(&self.path).map_err(|e| Error::Format(e.to_string()))?;
        let archive = ZipArchive::new(file).map_err(|e| Error::Format(e.to_string()))?;
        /* map archive entries into Entry metadata */
        Ok(Directory { entries })
    }
}
```
Transfer rule: Apply when processing large user-supplied archives or bundles: make limit checks a named operation and test it independently. Avoid claiming parallel speedup when the archive reader is protected by a single mutex; central-directory metadata extraction may still be serialized.
Verification hook: Keep tests for oversize files, empty zips, valid zips, and nonexistent files; add a malicious path/zip-slip fixture before supporting extraction.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve-local-llm-server`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/pensieve-local-llm-server-20260706-223658`; workspace crates were verified with `rg` and direct source reads.

### Concept: Thread-safe blackboard trait for multi-agent proposal handoff
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve-local-llm-server/crates/blackboard-handoff-protocol-core/src/lib.rs`
Why it matters: The blackboard crate separates the storage interface from the in-memory implementation. Proposal storage is keyed by conversation id, returns cloned proposal vectors, reports missing conversations as a domain error, and has an `Arc` constructor for task sharing. This is a reusable architecture for agentic workflows where independent proposers need to leave artifacts for an aggregator.
Reusable code shape:
```rust
pub trait Blackboard: Send + Sync {
    fn store_proposal_in_blackboard(&self, entry: ProposalEntry) -> Result<(), BlackboardError>;
    fn get_proposals_for_conversation(
        &self,
        conversation_id: Uuid,
    ) -> Result<Vec<ProposalEntry>, BlackboardError>;
    fn clear_conversation_from_blackboard(&self, conversation_id: Uuid)
        -> Result<(), BlackboardError>;
    fn count_proposals_for_conversation(&self, conversation_id: Uuid) -> usize;
}

#[derive(Debug, Default)]
pub struct InMemoryBlackboard {
    proposals: RwLock<HashMap<Uuid, Vec<ProposalEntry>>>,
}

impl InMemoryBlackboard {
    pub fn create_shared_blackboard_arc() -> Arc<Self> {
        Arc::new(Self::create_blackboard_in_memory())
    }
}
```
Transfer rule: Apply when several async workers produce intermediate artifacts for a later reducer. Avoid unbounded in-memory storage for long-running production agents unless retention and persistence are explicit.
Verification hook: Tests should cover store/retrieve, multiple proposals per conversation, missing conversation errors, clearing, and `Arc` sharing.

### Concept: Generic orchestrator over LLM, blackboard, and router capabilities
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve-local-llm-server/crates/debate-orchestrator-state-machine/src/lib.rs`
Why it matters: `MoaLiteOrchestrator<L, B, R>` is generic over three trait families: LLM client, blackboard storage, and complexity router. Construction takes `Arc` instances, then the local debate workflow runs proposers, enforces a minimum proposal count, stores proposals, and builds aggregator input. This is a clean shape for agent systems because runtime composition remains testable with mock clients and in-memory storage.
Reusable code shape:
```rust
pub struct MoaLiteOrchestrator<L, B, R>
where
    L: LlmClient + 'static,
    B: Blackboard + 'static,
    R: ComplexityRouter + 'static,
{
    llm_client: Arc<L>,
    blackboard: Arc<B>,
    router: Arc<R>,
    proposer_configs: [ProposerConfig; PROPOSER_COUNT],
    aggregator_config: AggregatorConfig,
    timeout_secs: u64,
}

async fn execute_local_debate_workflow(
    &self,
    query: &str,
    conversation_id: Uuid,
) -> Result<DebateResult, OrchestratorError> {
    let proposals = self.run_proposers_in_parallel(query, conversation_id).await?;
    if proposals.len() < MIN_PROPOSALS_REQUIRED {
        return Err(OrchestratorError::InsufficientProposals { required, received });
    }
    for proposal in &proposals {
        self.blackboard.store_proposal_in_blackboard(proposal.clone())?;
    }
    let aggregator_input = self.build_aggregator_input_text(&proposals);
    self.generate_aggregator_final_response(&aggregator_input).await
}
```
Transfer rule: Apply when orchestration should be independent from provider clients and routing policy. Avoid generic type explosion at public API edges; type aliases or builder constructors help keep caller ergonomics.
Verification hook: Mock `LlmClient`, `Blackboard`, and `ComplexityRouter` to assert local path, cloud handoff path, timeout path, and insufficient proposal path.

### Concept: SSE byte stream parsing with typed chunk fallback
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve-local-llm-server/crates/llama-server-client-streaming/src/lib.rs`
Why it matters: The streaming client posts a request, checks HTTP status, then wraps `response.bytes_stream()` in `async_stream::try_stream!`. It handles `data:` lines, ignores done markers, parses typed chunks, and falls back to extracting `content` from generic JSON when the strict struct parse fails. This is practical for local LLM servers where streaming schemas can drift.
Reusable code shape:
```rust
let stream = async_stream::try_stream! {
    let mut byte_stream = response.bytes_stream();

    while let Some(chunk_result) = byte_stream.next().await {
        let chunk = chunk_result.map_err(|e| LlmClientError::StreamError(e.to_string()))?;
        let text = String::from_utf8_lossy(&chunk);

        for line in text.lines() {
            if let Some(data) = line.strip_prefix(SSE_DATA_PREFIX) {
                let data = data.trim();
                if data == SSE_DONE_MARKER || data.is_empty() {
                    continue;
                }

                match serde_json::from_str::<StreamingChunk>(data) {
                    Ok(chunk) => yield chunk,
                    Err(_) => {
                        if let Ok(json) = serde_json::from_str::<serde_json::Value>(data) {
                            if let Some(content) = json["content"].as_str() {
                                yield StreamingChunk { content: content.to_string(), stop: false, tokens_predicted: 0, model: String::new() };
                            }
                        }
                    }
                }
            }
        }
    }
};
```
Transfer rule: Apply for SSE APIs where typed payloads are preferred but tolerant degradation is useful. Avoid if protocol correctness is security-sensitive; in that case reject malformed chunks loudly.
Verification hook: Unit-test streams containing valid chunks, `[DONE]`, blank data lines, malformed typed chunks with fallback JSON, and split UTF-8/chunk boundaries.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/reducto`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/reducto-20260706-223658`; metrics and CLI snippets were verified directly.

### Concept: Feature-gated observability state with cheap default config
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/reducto/src/metrics_collector.rs`
Why it matters: `EnterpriseMetricsCollector` keeps core metrics in `Arc<Mutex<_>>` fields, while optional Prometheus/system-monitoring fields are gated behind `#[cfg(feature = "metrics")]`. The constructor creates all shared state in one place and uses a serializable `MetricsConfig` with defaults. This lets a crate expose observability without forcing all deployments to pay for external metrics dependencies.
Reusable code shape:
```rust
pub struct EnterpriseMetricsCollector {
    compression_metrics: Arc<Mutex<Vec<CompressionMetrics>>>,
    decompression_metrics: Arc<Mutex<Vec<DecompressionMetrics>>>,
    performance_metrics: Arc<Mutex<PerformanceMetrics>>,
    economic_data: Arc<Mutex<EconomicData>>,
    #[cfg(feature = "metrics")]
    prometheus_registry: Arc<Registry>,
    config: MetricsConfig,
    session_start: Instant,
}

impl EnterpriseMetricsCollector {
    pub fn new(config: MetricsConfig) -> Result<Self> {
        #[cfg(feature = "metrics")]
        let prometheus_registry = Arc::new(Registry::new());

        Ok(Self {
            compression_metrics: Arc::new(Mutex::new(Vec::new())),
            decompression_metrics: Arc::new(Mutex::new(Vec::new())),
            performance_metrics: Arc::new(Mutex::new(PerformanceMetrics::default())),
            economic_data: Arc::new(Mutex::new(EconomicData::default())),
            #[cfg(feature = "metrics")]
            prometheus_registry,
            config,
            session_start: Instant::now(),
        })
    }
}
```
Transfer rule: Apply when metrics are valuable but should be optional at compile time. Avoid `Arc<Mutex<Vec<_>>>` for very high-cardinality metrics without retention and backpressure.
Verification hook: Run tests with and without `--features metrics`; add assertions for default config values and for bounded retention behavior.

### Concept: CLI cancellation through `tokio::select!` and typed exit codes
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/reducto/src/bin/reducto.rs`
Why it matters: The CLI wraps the runtime manually, initializes logging, constructs app state, starts a Ctrl-C listener, and races command execution against cancellation. Known `CliError` values print richer diagnostics and exit with their own codes. This is a reusable shape for async CLIs that need graceful cancellation without burying all errors in `anyhow`.
Reusable code shape:
```rust
fn main() -> Result<()> {
    let rt = tokio::runtime::Runtime::new()?;
    rt.block_on(async_main())
}

async fn async_main() -> Result<()> {
    let (tx, mut rx) = tokio::sync::mpsc::channel::<()>(1);
    tokio::spawn(async move {
        tokio::signal::ctrl_c().await.ok();
        let _ = tx.send(()).await;
    });

    let result = tokio::select! {
        result = execute_command(&app, cli.command) => result,
        _ = rx.recv() => {
            let error = CliError::OperationCancelled { operation: "CLI command".to_string(), partial_results: None };
            error.print_error();
            std::process::exit(error.exit_code());
        }
    };

    if let Err(e) = result {
        if let Some(cli_err) = e.downcast_ref::<CliError>() {
            cli_err.print_error();
            std::process::exit(cli_err.exit_code());
        }
    }
    Ok(())
}
```
Transfer rule: Apply when a CLI command can run long enough that cancellation should produce a deliberate outcome. Avoid `std::process::exit` deep in library code; keep it at binary edges.
Verification hook: Integration-test invalid config, Ctrl-C behavior if harness supports signals, and exit-code mapping for typed CLI errors.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/confido-exploration-01`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/confido-exploration-01-20260706-223658`; Rust implementation lives under `Sol-variant-01` and was verified there.

### Concept: Mutex-guarded SQLite version store with deterministic schema initialization
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/confido-exploration-01/Sol-variant-01/src/version_store.rs`
Why it matters: `SqliteVersionStore` owns a single `rusqlite::Connection` behind a `Mutex`, initializes schema immediately for both in-memory and file-backed stores, and maps poisoned locks into a domain error. It records payload size, analysis run id, model label, and timestamped version names. This is a reusable persistence shape for local-first review or prompt-evaluation tools.
Reusable code shape:
```rust
pub struct SqliteVersionStore {
    connection: Mutex<Connection>,
}

impl SqliteVersionStore {
    pub fn open_store_at_path(path: impl AsRef<Path>) -> Result<Self, PieError> {
        if let Some(parent) = path.as_ref().parent() {
            std::fs::create_dir_all(parent)?;
        }
        let connection = Connection::open(path)?;
        let store = Self { connection: Mutex::new(connection) };
        store.initialize_schema()?;
        Ok(store)
    }

    fn initialize_schema(&self) -> Result<(), PieError> {
        let connection = self.connection.lock().map_err(|_| PieError::Sqlite {
            message: "version store lock poisoned".to_string(),
        })?;
        connection.execute_batch("create table if not exists prompt_versions (...);")?;
        Ok(())
    }
}
```
Transfer rule: Apply for small desktop/local services where one process owns the database and simplicity matters. Avoid sharing one mutexed connection for high-concurrency server workloads; use a pool instead.
Verification hook: Tests should open in-memory and file stores, store/load versions, assert parent directory creation, and exercise duplicate primary-key behavior.

### Concept: Tauri commands wrap core async logic with diagnostics at the boundary
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/confido-exploration-01/Sol-variant-01/src-tauri/src/commands.rs`
Why it matters: Tauri command functions are thin adapters: they accept serializable request data and managed `State`, start a timer, record command start/outcome in a diagnostic logger, and delegate the real work to core functions. This keeps desktop IPC glue small and preserves a testable non-Tauri core.
Reusable code shape:
```rust
#[tauri::command]
pub async fn reverify_prompt(
    request: ReverifyPromptRequest,
    client: State<'_, OpenAiHttpClient>,
    logger: State<'_, DiagnosticLogger>,
) -> Result<ReverifyPromptResult, AppError> {
    let started = Instant::now();
    record_command_started(logger.inner(), "reverify_prompt");
    let result = reverify_prompt_core(request, client.inner()).await;
    record_command_outcome(logger.inner(), "reverify_prompt", started, &result);
    result
}
```
Transfer rule: Apply in Tauri apps and other RPC boundaries where command handlers should be observable but not own business logic. Avoid putting parsing, network protocols, and persistence directly in command functions.
Verification hook: Contract tests should call the core functions directly and separate smoke tests should verify command serialization/error mapping.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/mermish`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/mermish-20260706-223658`; extracted pattern from runnable Tokio dashboard example, not archival placeholder crates.

### Concept: Tokio task dashboard with explicit shared-state and message-passing lanes
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/mermish/A03_RUNNABLE_CODE/tokio-mcu-dashboard/src/main.rs`
Why it matters: The dashboard creates one `McuDashboard` containing shared `Arc<Mutex<_>>` state and one `mpsc` command lane. It spawns independent tasks for periodic LED blinking, sensor updates, relay commands, and monitor heartbeats. Each task returns a `JoinHandle`, releases mutex guards before async logging, and uses `interval` instead of blocking sleeps. This is a compact reference for teaching or building small async control planes.
Reusable code shape:
```rust
let dashboard = McuDashboard {
    led: Arc::new(Mutex::new(LedState::default())),
    sensors: Arc::new(Mutex::new(SensorData::default())),
    relay: Arc::new(Mutex::new(RelayState::default())),
    logs: Arc::new(Mutex::new(Vec::new())),
};

let (command_tx, command_rx) = mpsc::channel::<McuCommand>(100);

let _led_handle = spawn_led_blinker_task_with_interval(dashboard.clone(), Duration::from_millis(500)).await;
let _relay_handle = spawn_relay_controller_task_with_channel(dashboard.clone(), command_rx).await;
let _monitor_handle = spawn_monitor_task_with_select(dashboard.logs.clone(), Duration::from_secs(5)).await;
```
Transfer rule: Apply for UI demos, device dashboards, local automation, and teaching async Rust. Avoid unbounded task lifetimes in production; add shutdown channels or cancellation tokens.
Verification hook: Review that mutex guards are dropped before awaited operations; add tests with paused Tokio time for interval behavior and channel-close termination.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/iiwii01`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/iiwii01-20260706-223718`; repo is mostly exploratory Rust experiments, with reusable patterns verified in `zzPre20241017/attempt04`.

### Concept: Parallel ignore-aware file assimilation with concurrent aggregation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/iiwii01/zzPre20241017/attempt04/src/main.rs`
Why it matters: The analyzer uses `ignore::WalkBuilder` with hidden and gitignore controls, `build_parallel`, `DashMap` for directory/file aggregation, and atomics for counts/sizes. It then chunks consolidated source output by capacity. This is a useful shape for agent context builders that need to walk large repos, honor ignore rules, and emit bounded context chunks.
Reusable code shape:
```rust
let file_tree: Arc<DashMap<PathBuf, Vec<String>>> = Arc::new(DashMap::new());
let walker = WalkBuilder::new(&self.path)
    .hidden(false)
    .ignore(true)
    .git_ignore(true)
    .build_parallel();

walker.run(|| {
    let file_tree = Arc::clone(&file_tree);
    Box::new(move |entry| {
        if let Ok(entry) = entry {
            if entry.file_type().map_or(false, |ft| ft.is_file()) && self.should_include_file(entry.path()) {
                let path = entry.into_path();
                if let (Some(file_name), Some(parent)) = (path.file_name().and_then(|f| f.to_str()), path.parent()) {
                    file_tree.entry(parent.to_path_buf()).or_default().push(file_name.to_string());
                    total_files.fetch_add(1, Ordering::Relaxed);
                }
            }
        }
        ignore::WalkState::Continue
    })
});
```
Transfer rule: Apply for repository scanners and context-pack generation where ignore semantics and throughput matter. Avoid capturing non-`Send` state in the parallel walker closure; avoid reading huge binary files into `String`.
Verification hook: Fixture repo with hidden files, `.gitignore`, include/exclude patterns, and binary files; assert chunk size ceilings and deterministic enough output ordering if downstream diffs matter.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/tweetbook202409`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/tweetbook202409-20260706-223718`; source-backed pattern taken from the archived processor and CSV writer.

### Concept: Async ingestion plus blocking CPU grouping for thread extraction
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/tweetbook202409/zzArchive/Failed20240925/processor.rs`
Why it matters: The processor reads a JavaScript-wrapped tweet export asynchronously, slices out the JSON array, deserializes into typed wrappers, filters in parallel with Rayon, then uses `tokio::task::spawn_blocking` for thread grouping and date sorting. The reusable architecture is splitting IO-bound file reading from CPU-bound grouping so an async CLI does not block the runtime.
Reusable code shape:
```rust
let script_content = async_fs::read_to_string(input_file).await?;
let json_start = script_content.find('[').context("missing opening bracket")?;
let json_end = script_content.rfind(']').context("missing closing bracket")?;
let tweets: Vec<TweetWrapper> = serde_json::from_str(&script_content[json_start..=json_end])?;

let tweets: Vec<Tweet> = tweets
    .into_par_iter()
    .map(|tw| tw.tweet)
    .filter(|tweet| !tweet.retweeted && should_keep(tweet, screen_name))
    .collect();

let tweets_map: HashMap<String, Tweet> = tweets.into_iter().map(|t| (t.id_str.clone(), t)).collect();
let threads: Vec<Vec<Tweet>> = task::spawn_blocking(move || group_threads(tweets_map)).await??;
```
Transfer rule: Apply for local data-mining CLIs that parse large exports and do graph-like grouping. Avoid O(n^2) `.values().find(...)` reply-chain construction on large datasets; build a reply index first.
Verification hook: Use fixtures with root tweets, reply chains, retweets, off-screen-name replies, malformed export wrappers, and invalid dates.

### Concept: Buffered CSV writer behind an async channel
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/tweetbook202409/zzArchive/Failed20240925/csv_writer.rs`
Why it matters: `CsvWriter` owns an `mpsc::Receiver<Vec<String>>`, accumulates records into a fixed-size buffer, drains to a `BufWriter`, and flushes at channel close. This decouples producers from disk writes and gives a simple backpressure point through the channel capacity.
Reusable code shape:
```rust
pub struct CsvWriter {
    output_path: String,
    receiver: mpsc::Receiver<Vec<String>>,
    buffer_size: usize,
}

pub async fn run(mut self) -> Result<()> {
    let file = File::create(&self.output_path)?;
    let mut writer = BufWriter::new(file);
    let mut buffer = Vec::with_capacity(self.buffer_size);

    while let Some(record) = self.receiver.recv().await {
        buffer.push(record);
        if buffer.len() >= self.buffer_size {
            self.flush_buffer(&mut writer, &mut buffer)?;
        }
    }

    if !buffer.is_empty() {
        self.flush_buffer(&mut writer, &mut buffer)?;
    }
    writer.flush()?;
    Ok(())
}
```
Transfer rule: Apply when many async producers emit flat records to one file. Avoid hand-joining fields with commas for production CSV; use the `csv` crate to handle quoting and embedded separators.
Verification hook: Test buffer flush at exact capacity, final partial flush, channel close, and records containing commas/newlines.

## Repo Coverage: `/Users/amuldotexe/Desktop/notes-plans-hub/hogwarts202603`

Codebase-memory: not run; `rg --files -g 'Cargo.toml' -g '*.rs'` found no Rust crate or Rust source to index in this assigned checkout.

### Concept: Skipped because the checkout has no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/notes-plans-hub/hogwarts202603`
Why it matters: Coverage still needs to record that this repository was inspected. The useful transfer signal is negative: do not infer Rust architecture patterns from notes-only or non-code planning material.
Reusable code shape:
```text
No Rust source files or Cargo manifests were present in this checkout.
```
Transfer rule: Apply this skip classification when `rg --files -g 'Cargo.toml' -g '*.rs'` returns no Rust surfaces. Avoid inventing Rust-adjacent patterns from prose-only folders.
Verification hook: Re-run `rg --files -g 'Cargo.toml' -g '*.rs' /Users/amuldotexe/Desktop/notes-plans-hub/hogwarts202603` and expect no matches.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/auron`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/auron-20260706-224043`; source-backed patterns below were verified against the native-engine Rust files.

### Concept: JNI filesystem wrappers with Rust-owned global references and metrics
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/auron/native-engine/datafusion-ext-commons/src/hadoop_fs.rs`
Why it matters: The `Fs`, `FsDataInputWrapper`, and `FsDataOutputWrapper` types isolate Hadoop/JVM filesystem handles behind Rust structs that own `GlobalRef`s, time every operation with DataFusion metrics, pass buffers through JNI direct byte buffers, and close Java `AutoCloseable`s in `Drop`. This is a strong pattern for Rust services that must call into JVM infrastructure without leaking raw JNI handles throughout the query engine.
Reusable code shape:
```rust
#[derive(Clone)]
pub struct Fs {
    fs: GlobalRef,
    io_time: Time,
}

impl Fs {
    pub fn open(&self, path: &str) -> Result<Arc<FsDataInputWrapper>> {
        let _timer = self.io_time.timer();
        let path = jni_new_string!(path)?;
        let wrapper = jni_call_static!(
            JniBridge.openFileAsDataInputWrapper(self.fs.as_obj(), path.as_obj()) -> JObject
        )?;
        Ok(Arc::new(FsDataInputWrapper {
            obj: jni_new_global_ref!(wrapper.as_obj())?,
            io_time: self.io_time.clone(),
        }))
    }
}

impl FsDataInputWrapper {
    pub fn read_fully(&self, pos: u64, buf: &mut [u8]) -> Result<()> {
        let _timer = self.io_time.timer();
        let buf = jni_new_direct_byte_buffer!(buf)?;
        jni_call!(AuronFSDataInputWrapper(self.obj.as_obj())
            .readFully(pos as i64, buf.as_obj()) -> ())?;
        Ok(())
    }
}

impl Drop for FsDataInputWrapper {
    fn drop(&mut self) {
        if let Err(e) = jni_call!(JavaAutoCloseable(self.obj.as_obj()).close() -> ()) {
            log::warn!("error closing hadoop FSDataInputStream: {e:?}");
        }
    }
}
```
Transfer rule: Apply when Rust owns a long-lived JVM resource and needs to expose it to DataFusion, Arrow, or async query operators. Avoid exposing `JObject`/local refs from the wrapper; local JNI references have scope-sensitive lifetimes.
Verification hook: Unit or integration tests should force early drop paths and read/write paths, and metrics should show IO time accumulation around every JNI call.

### Concept: Arrow RecordBatch binary serde with recursive data-type dispatch
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/auron/native-engine/datafusion-ext-commons/src/io/batch_serde.rs`
Why it matters: `write_batch` and `read_batch` serialize row counts followed by typed Arrow arrays. The implementation dispatches on `DataType`, recurses through `List`, `Map`, and `Struct`, and returns `Ok(None)` on clean EOF. This is a reusable shape for high-throughput local shuffle or IPC code that needs a compact internal wire format while preserving Arrow schemas.
Reusable code shape:
```rust
pub fn write_batch(num_rows: usize, cols: &[ArrayRef], mut output: impl Write) -> Result<()> {
    write_len(num_rows, &mut output)?;
    let mut transpose_opt =
        TransposeOpt::with_transpose(num_rows, cols.iter().map(|col| col.data_type()));
    for col in cols {
        write_array(col, &mut output, &mut transpose_opt)?;
    }
    Ok(())
}

pub fn read_batch(mut input: impl Read, schema: &SchemaRef) -> Result<Option<(usize, Vec<ArrayRef>)>> {
    let num_rows = match read_len(&mut input) {
        Ok(n) => n,
        Err(e) if e.kind() == ErrorKind::UnexpectedEof => return Ok(None),
        Err(e) => return Err(e.into()),
    };
    let mut transpose_opt =
        TransposeOpt::with_transpose(num_rows, schema.fields().iter().map(|f| f.data_type()));
    let cols = schema
        .fields()
        .into_iter()
        .map(|field| read_array(&mut input, field.data_type(), num_rows, &mut transpose_opt))
        .collect::<Result<_>>()?;
    Ok(Some((num_rows, cols)))
}
```
Transfer rule: Apply for private, version-controlled binary transport between components sharing Arrow types. Avoid using this as an external stable file format unless you add schema/version headers and compatibility tests.
Verification hook: Round-trip RecordBatches containing primitive, string, binary, list, map, struct, decimal, timestamp, nulls, and clean EOF.

### Concept: Protobuf physical plans lowered into `Arc<dyn ExecutionPlan>` with typed conversion macros
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/auron/native-engine/auron-planner/src/planner.rs`
Why it matters: `PhysicalPlanner::create_plan` turns Spark/Auron protobuf plan variants into DataFusion physical plan nodes. The pattern is a large match over wire variants, with every child input converted through helper macros and every vector conversion collected as `Result<Vec<_>, PlanError>`. It keeps the untrusted/protobuf boundary explicit while the internal engine receives trait objects with normal Rust error flow.
Reusable code shape:
```rust
pub fn create_plan<'a>(
    &'a self,
    spark_plan: &'a protobuf::PhysicalPlanNode,
) -> Result<Arc<dyn ExecutionPlan>, PlanError> {
    let plan = spark_plan.physical_plan_type.as_ref().ok_or_else(|| {
        proto_error(format!("physical_plan::from_proto() Unsupported physical plan '{spark_plan:?}'"))
    })?;
    match plan {
        PhysicalPlanType::Projection(projection) => {
            let input: Arc<dyn ExecutionPlan> = convert_box_required!(self, projection.input)?;
            let input_schema = input.schema();
            let exprs = projection
                .expr
                .iter()
                .zip(projection.expr_name.iter())
                .map(|(expr, name)| {
                    let physical_expr = self.try_parse_physical_expr(expr, &input_schema)?;
                    Ok((physical_expr, name.to_string()))
                })
                .collect::<Result<Vec<_>, PlanError>>()?;
            Ok(Arc::new(ProjectExec::try_new(exprs, input)?))
        }
        PhysicalPlanType::Filter(filter) => {
            let input: Arc<dyn ExecutionPlan> = convert_box_required!(self, filter.input)?;
            let predicates = filter
                .expr
                .iter()
                .map(|expr| self.try_parse_physical_expr(expr, &input.schema()))
                .collect::<Result<_, PlanError>>()?;
            Ok(Arc::new(FilterExec::try_new(predicates, input)?))
        }
        _ => todo!("other physical nodes follow the same boundary pattern"),
    }
}
```
Transfer rule: Apply when a wire protocol has many variants but the runtime wants trait objects. Avoid panicking on missing protobuf fields in new code; prefer `required("field")?` helpers so malformed plans produce diagnosable errors.
Verification hook: Golden protobuf fixtures for each plan variant, plus a negative fixture for missing `physical_plan_type`.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/dask`

Codebase-memory: not run; `rg --files -g 'Cargo.toml' -g '*.rs'` found no Rust crate or Rust source in this checkout.

### Concept: Skipped because the checkout has no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/dask`
Why it matters: Dask is a large Python project. It may contain parser-like or scheduler architecture ideas, but it is outside the Rust/Rust-adjacent extraction scope for this worker file.
Reusable code shape:
```text
No Cargo manifest or Rust source was present.
```
Transfer rule: Apply only as a coverage marker. Avoid treating Python scheduler code as source-backed Rust idiom evidence.
Verification hook: Re-run `rg --files -g 'Cargo.toml' -g '*.rs' /Users/amuldotexe/Desktop/oss-read-only/dask`.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/hermes-agent`

Codebase-memory: not run; `rg --files -g 'Cargo.toml' -g '*.rs'` found no Rust crate or Rust source in this checkout.

### Concept: Skipped because the checkout has no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/hermes-agent`
Why it matters: The repository may still be agent-related, but this extraction pass is for Rust and Rust-adjacent implementation patterns. No source-backed Rust pattern was available.
Reusable code shape:
```text
No Cargo manifest or Rust source was present.
```
Transfer rule: Use as negative coverage only. Avoid extracting TypeScript or JavaScript agent protocol patterns into a Rust pattern archive unless a Rust implementation exists.
Verification hook: Re-run `rg --files -g 'Cargo.toml' -g '*.rs' /Users/amuldotexe/Desktop/oss-read-only/hermes-agent`.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/pi_agent_rust`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/pi_agent_rust-20260706-224043`; source-backed patterns were verified in `src/acp.rs` and `src/rpc.rs`.

### Concept: Stdio JSON-RPC server splits blocking terminal IO from async dispatch
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/pi_agent_rust/src/acp.rs`
Why it matters: `run_stdio` uses ordinary blocking threads for stdin/stdout and bounded channels to feed an async core loop. This avoids mixing blocking terminal reads with async session dispatch, while preserving backpressure through `try_send` retry loops and a sync output channel.
Reusable code shape:
```rust
pub async fn run_stdio(options: AcpOptions) -> Result<()> {
    let (in_tx, in_rx) = asupersync::channel::mpsc::channel::<String>(256);
    let (out_tx, out_rx) = std::sync::mpsc::sync_channel::<String>(1024);

    std::thread::spawn(move || {
        let stdin = io::stdin();
        let mut reader = io::BufReader::new(stdin.lock());
        let mut line = String::new();
        loop {
            line.clear();
            match reader.read_line(&mut line) {
                Ok(0) | Err(_) => break,
                Ok(_) => {
                    let mut to_send = line.trim().to_string();
                    while let Err(asupersync::channel::mpsc::SendError::Full(unsent)) =
                        in_tx.try_send(to_send)
                    {
                        to_send = unsent;
                        std::thread::sleep(std::time::Duration::from_millis(10));
                    }
                }
            }
        }
    });

    std::thread::spawn(move || {
        let stdout = io::stdout();
        let mut writer = io::BufWriter::new(stdout.lock());
        for line in out_rx {
            let _ = writer.write_all(line.as_bytes());
            let _ = writer.write_all(b"\n");
            let _ = writer.flush();
        }
    });

    run(options, in_rx, out_tx).await
}
```
Transfer rule: Apply for line-oriented JSON-RPC, LSP-like, ACP-like, or MCP-like CLIs. Avoid unbounded channels for model streams; slow clients should exert pressure.
Verification hook: Protocol tests should feed invalid JSON, closed stdin/stdout, full channels, and permission response messages without `method`.

### Concept: Agent event to protocol notification adapter with intentional event dropping
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/pi_agent_rust/src/acp.rs`
Why it matters: `build_acp_event_handler` translates internal `AgentEvent`s into ACP `session/update` notifications and deliberately skips events that would duplicate already streamed text or tool metadata. This is a useful adapter pattern when one internal event model fans out into multiple external protocols with different rendering expectations.
Reusable code shape:
```rust
fn build_acp_event_handler(
    out_tx: std::sync::mpsc::SyncSender<String>,
    session_id: String,
) -> impl Fn(AgentEvent) + Send + Sync + 'static {
    move |event: AgentEvent| {
        let update = match &event {
            AgentEvent::MessageUpdate { assistant_message_event, .. } => match assistant_message_event {
                AssistantMessageEvent::TextDelta { delta, .. } => Some(json!({
                    "sessionUpdate": "agent_message_chunk",
                    "content": { "type": "text", "text": delta },
                })),
                AssistantMessageEvent::ThinkingDelta { delta, .. } => Some(json!({
                    "sessionUpdate": "agent_thought_chunk",
                    "content": { "type": "text", "text": delta },
                })),
                _ => None,
            },
            AgentEvent::ToolExecutionStart { tool_call_id, tool_name, args } => Some(json!({
                "sessionUpdate": "tool_call",
                "toolCallId": tool_call_id,
                "title": tool_name,
                "status": "pending",
                "rawInput": args,
            })),
            _ => None,
        };

        if let Some(update) = update {
            let _ = out_tx.send(json_rpc_notification(
                "session/update",
                json!({ "sessionId": session_id, "update": update }),
            ));
        }
    }
}
```
Transfer rule: Apply at protocol edges. Avoid passing internal event enums directly over the wire; protocol stability and UI semantics usually need a narrower vocabulary.
Verification hook: Snapshot tests for text deltas, thought deltas, tool start/update/end, and no-output cases for intentionally skipped events.

### Concept: Streaming output pressure coalesces low-semantic deltas but flushes before semantic events
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/pi_agent_rust/src/rpc.rs`
Why it matters: `RpcOutputPressureState` classifies events as `Semantic`, `MessageDelta`, or `ToolUpdate`. If the bounded output channel is full, it keeps only the latest event per low-semantic class; before sending a semantic event, it flushes pending coalesced updates. This preserves important protocol milestones while preventing token-delta floods from stalling the agent.
Reusable code shape:
```rust
enum RpcOutputPressureClass {
    Semantic,
    MessageDelta,
    ToolUpdate,
}

impl RpcOutputPressureState {
    fn send_agent_event(
        &mut self,
        tx: &std::sync::mpsc::SyncSender<String>,
        event: &AgentEvent,
        serialized: String,
    ) {
        match rpc_output_pressure_class(event) {
            RpcOutputPressureClass::Semantic => {
                self.flush_pending(tx);
                let _ = tx.send(serialized);
            }
            class => self.try_send_or_coalesce(tx, class, serialized),
        }
    }

    fn coalesce(&mut self, class: RpcOutputPressureClass, serialized: String) {
        if let Some(pending) = self.pending.iter_mut().find(|p| p.class == class) {
            pending.serialized = serialized;
        } else {
            self.pending.push(PendingRpcPressureEvent { class, serialized });
        }
    }
}
```
Transfer rule: Apply for chat, TUI, or RPC streams where deltas are supersedable but boundaries like turn start/end, tool start/end, and errors are not. Avoid coalescing events that carry unique causal information.
Verification hook: Unit tests should fill a one-slot channel, send many deltas, then send a semantic event and assert only the latest delta plus the semantic event is delivered.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/sail`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/sail-20260706-224043`; parser patterns were verified in `crates/sail-sql-parser` and `crates/sail-sql-macro`.

### Concept: Chumsky recursive parser graph declares cycles first, then defines AST parsers
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/sail/crates/sail-sql-parser/src/parser.rs`
Why it matters: SQL grammar has mutually recursive statements, queries, expressions, data types, and joins. Sail declares all recursive parser handles first, then defines each parser with clones of its dependencies. This keeps recursion explicit and composable while avoiding ad hoc global parser state.
Reusable code shape:
```rust
fn statement<'a, I, E>(options: &'a ParserOptions) -> impl Parser<'a, I, Statement, E> + Clone
where
    I: Input<'a, Token = Token<'a>> + ValueInput<'a>,
    I::Span: Into<TokenSpan> + Clone,
    E: ParserExtra<'a, I> + 'a,
    E::Error: LabelError<'a, I, TokenLabel>,
{
    let mut statement = Recursive::declare();
    let mut query = Recursive::declare();
    let mut expression = Recursive::declare();
    let mut data_type = Recursive::declare();
    let mut table_with_joins = Recursive::declare();

    statement.define(Statement::parser(
        (statement.clone(), query.clone(), expression.clone(), data_type.clone()),
        options,
    ));
    query.define(Query::parser(
        (query.clone(), expression.clone(), table_with_joins.clone()),
        options,
    ));
    expression.define(Expr::parser(
        (expression.clone(), query.clone(), data_type.clone()),
        options,
    ));
    data_type.define(DataType::parser(data_type.clone(), options));
    table_with_joins.define(TableWithJoins::parser(
        (query.clone(), expression.clone(), table_with_joins.clone()),
        options,
    ));
    statement
}
```
Transfer rule: Apply for recursive grammars in Chumsky where several AST nodes refer to each other. Avoid this pattern for operator precedence alone; Sail's macro docs say precedence-heavy or left-recursive grammars still need manual parsers.
Verification hook: Golden parser suites for nested subqueries, nested data types, joins with subqueries, and invalid recursive constructs.

### Concept: Derive macro turns AST structs/enums into parser combinators with dependency attributes
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/sail/crates/sail-sql-macro/src/lib.rs`, `/Users/amuldotexe/Desktop/oss-read-only/sail/crates/sail-sql-macro/src/tree/parser.rs`
Why it matters: Sail derives `TreeParser` for AST nodes, letting fields parse sequentially and enum variants parse as choices. Attributes declare recursive dependencies, labels for better errors, and custom field parser functions. For large enums, the macro chunks choices and boxes parsers to reduce compile times.
Reusable code shape:
```rust
const MAX_CHOICES: usize = 20;
const BOXED_ENUM_MIN_VARIANTS: usize = 5;

fn derive_choices(choices: Vec<TokenStream>) -> TokenStream {
    let choices = if choices.len() <= MAX_CHOICES {
        choices
    } else {
        let chunk_size = choices.len().div_ceil(MAX_CHOICES);
        choices
            .chunks(chunk_size)
            .map(|chunk| derive_choices(chunk.to_vec()))
            .collect()
    };
    if choices.len() > 1 {
        quote! { chumsky::prelude::choice((#(#choices),*)) }
    } else {
        quote! { #(#choices),* }
    }
}

// Generated impl shape:
impl<'a, I, E, P> crate::tree::TreeParser<'a, I, E, P> for SomeAstNode
where
    P: chumsky::Parser<'a, I, DependencyNode, E> + Clone + 'a,
{
    fn parser(args: P, options: &'a ParserOptions) -> impl chumsky::Parser<'a, I, Self, E> + Clone {
        /* derived parser */
    }
}
```
Transfer rule: Apply when a grammar has many product/sum AST nodes with repetitive parser assembly. Avoid deriving for terminals, left-recursive nodes, and precedence-sensitive expressions that need hand-written control.
Verification hook: Macro expansion tests or compile-fail tests for unit variants, empty structs, invalid `parser(dependency = "...")`, and large enums.

### Concept: Parser entrypoints consume padding and enforce end-of-input at the boundary
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/sail/crates/sail-sql-parser/src/parser.rs`
Why it matters: Sail wraps sub-parsers with a macro that pads by whitespace and then `then_ignore(end())`. This prevents "partial parse succeeded" bugs where trailing garbage survives a successful parse.
Reusable code shape:
```rust
macro_rules! define_sub_parser {
    ($name:ident, $type:ty, $parse:ident $(,)?) => {
        pub fn $name<'a, I, E>(options: &'a ParserOptions) -> impl Parser<'a, I, $type, E> + Clone
        where
            I: Input<'a, Token = Token<'a>> + ValueInput<'a>,
            I::Span: Into<TokenSpan> + Clone,
            E: ParserExtra<'a, I> + 'a,
            E::Error: LabelError<'a, I, TokenLabel>,
        {
            $parse(options)
                .padded_by(whitespace().repeated())
                .then_ignore(end())
        }
    };
}
```
Transfer rule: Apply to public parse functions and test helpers. Avoid burying `end()` inside inner grammar nodes where composition needs to continue.
Verification hook: Tests should assert `parse_expression("a trailing")` fails or reports trailing tokens unless the grammar explicitly allows them.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/tauri`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/tauri-20260706-224043`; source-backed patterns were verified in runtime, plugin build, and macOS signing crates.

### Concept: Singleton async runtime abstraction accepts either owned runtime or borrowed handle
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/tauri/crates/tauri/src/async_runtime.rs`
Why it matters: Tauri exposes one global async runtime surface while allowing applications to supply an existing Tokio handle. `GlobalRuntime` stores either an owned `Runtime` plus handle, or only a `RuntimeHandle`, and every `spawn`, `spawn_blocking`, and `block_on` goes through that abstraction. This is useful for libraries that need async internals but must coexist with host applications that already own a runtime.
Reusable code shape:
```rust
static RUNTIME: OnceLock<GlobalRuntime> = OnceLock::new();

struct GlobalRuntime {
    runtime: Option<Runtime>,
    handle: RuntimeHandle,
}

impl GlobalRuntime {
    fn spawn<F>(&self, task: F) -> JoinHandle<F::Output>
    where
        F: Future + Send + 'static,
        F::Output: Send + 'static,
    {
        if let Some(r) = &self.runtime {
            r.spawn(task)
        } else {
            self.handle.spawn(task)
        }
    }
}

pub fn set(handle: TokioHandle) {
    RUNTIME
        .set(GlobalRuntime { runtime: None, handle: RuntimeHandle::Tokio(handle) })
        .unwrap_or_else(|_| panic!("runtime already initialized"));
}
```
Transfer rule: Apply for framework crates that need global async helpers. Avoid this in ordinary application code where passing an explicit handle is simpler and easier to test.
Verification hook: Tests should cover default runtime spawn/block_on, injected handle spawn/block_on, and the "set only once" invariant.

### Concept: Plugin build script materializes permission schema and allowed-command metadata
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/tauri/crates/tauri-plugin/src/build/mod.rs`
Why it matters: `Builder::try_build` validates plugin naming conventions, requires `CARGO_MANIFEST_LINKS`, generates autogenerated command permissions, produces permission schemas/docs, and writes allowed-command metadata into `OUT_DIR`. The pattern turns runtime ACL drift into build-time generated artifacts.
Reusable code shape:
```rust
pub fn try_build(self) -> Result<()> {
    let name = build_var("CARGO_PKG_NAME")?;
    if name.contains('_') {
        anyhow::bail!("plugin names cannot contain underscores");
    }
    if RESERVED_PLUGIN_NAMES.contains(&name.as_str()) {
        anyhow::bail!("plugin name `{name}` is reserved");
    }

    let out_dir = PathBuf::from(build_var("OUT_DIR")?);
    let _links = std::env::var("CARGO_MANIFEST_LINKS").map_err(|_| Error::LinksMissing)?;

    let autogenerated = Path::new("permissions").join(acl::build::AUTOGENERATED_FOLDER_NAME);
    std::fs::create_dir_all(&autogenerated).expect("unable to create permissions dir");

    let commands_dir = autogenerated.join("commands");
    if !self.commands.is_empty() {
        acl::build::autogenerate_command_permissions(&commands_dir, self.commands, "", true);
    }

    let permissions =
        acl::build::define_permissions("./permissions/**/*.*", &name, &out_dir, |_| true)?;
    let mut permissions_map = BTreeMap::new();
    permissions_map.insert(name.clone(), permissions);
    tauri_utils::acl::build::generate_allowed_commands(&out_dir, None, permissions_map)?;
    Ok(())
}
```
Transfer rule: Apply when plugin commands need declarative permission manifests. Avoid deferring permission discovery to runtime if host applications need static review.
Verification hook: Build-script fixture that asserts generated command permissions and allowed commands change when command list or permission files change.

### Concept: RAII keychain lifecycle around command-line signing tools
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/tauri/crates/tauri-macos-sign/src/keychain.rs`
Why it matters: The macOS signing crate creates temporary keychains, imports certificates, updates keychain search lists, and deletes the keychain in `Drop`. Every shell command is routed through `assert_command` and mapped to structured errors. This is a clean pattern for high-stakes OS automation where secrets and temp state must be cleaned up.
Reusable code shape:
```rust
pub struct Keychain {
    path: Option<PathBuf>,
    signing_identity: SigningIdentity,
}

impl Drop for Keychain {
    fn drop(&mut self) {
        if let Some(path) = &self.path {
            let _ = Command::new("security")
                .arg("delete-keychain")
                .arg(path)
                .piped();
        }
    }
}

pub fn with_certificate_file(cert_path: &Path, certificate_password: &OsString) -> Result<Self> {
    let keychain_path = dirs::home_dir()
        .ok_or(Error::ResolveHomeDir)?
        .join("Library")
        .join("Keychains")
        .join(format!("{}.keychain-db", Alphanumeric.sample_string(&mut rand::rng(), 16)));

    assert_command(
        Command::new("security")
            .args(["create-keychain", "-p", &keychain_password])
            .arg(&keychain_path)
            .piped(),
        "failed to create keychain",
    )?;
    /* unlock, import, set settings, discover signing identity */
    Ok(Self { path: Some(keychain_path), signing_identity })
}
```
Transfer rule: Apply to CLIs that provision temporary OS resources. Avoid relying solely on `Drop` for critical cleanup; also expose explicit cleanup or use temp directories where possible for crash resilience.
Verification hook: Mock command runner tests for command sequence plus integration smoke on macOS CI that verifies the temporary keychain is removed after scope exit.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/zed-gpui`

Codebase-memory: smoke scan succeeded at `/tmp/codex-code-intel/codebase-memory/zed-gpui-20260706-224108`; bounded source sampling covered language, Markdown, and CSV parser surfaces.

### Concept: Tree-sitter syntax snapshots offload expensive tree drops to a background thread
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/zed-gpui/crates/language/src/syntax_map.rs`
Why it matters: `SyntaxSnapshot` stores syntax layers in a `SumTree`. Dropping deep Tree-sitter trees can be slow, so the `Drop` impl moves the existing tree to a static background channel and replaces it with an empty summary. This protects the UI/main thread from deallocation pauses.
Reusable code shape:
```rust
impl Drop for SyntaxSnapshot {
    fn drop(&mut self) {
        static DROP_TX: LazyLock<std::sync::mpsc::Sender<SumTree<SyntaxLayerEntry>>> =
            LazyLock::new(|| {
                let (tx, rx) = std::sync::mpsc::channel();
                std::thread::Builder::new()
                    .name("SyntaxSnapshot::drop".into())
                    .spawn(move || while let Ok(_) = rx.recv() {})
                    .expect("failed to spawn drop thread");
                tx
            });

        let _ = DROP_TX.send(std::mem::replace(
            &mut self.layers,
            SumTree::from_summary(SyntaxLayerSummary {
                min_depth: Default::default(),
                max_depth: Default::default(),
                range: Anchor::min_min_range_for_buffer(BufferId::new(1).unwrap()),
                last_layer_range: Anchor::min_min_range_for_buffer(BufferId::new(1).unwrap()),
                last_layer_language: Default::default(),
                contains_unknown_injections: Default::default(),
            }),
        ));
    }
}
```
Transfer rule: Apply for UI applications holding large parse trees, rope indexes, or GPU resources whose destructors can stall interaction. Avoid using this for resources that must be synchronously released before a later operation.
Verification hook: Profiling or test instrumentation should show snapshot replacement is cheap on the caller thread; stress tests should drop deeply nested syntax maps without UI jank.

### Concept: Markdown parse cache uses owned static events plus byte ranges instead of borrowed parser output
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/zed-gpui/crates/markdown/src/parser.rs`
Why it matters: Pulldown-cmark yields events borrowing from input. Zed converts them into owned `MarkdownEvent` values paired with source byte ranges, plus derived indexes for headings, footnotes, root blocks, and optional parsed HTML. This makes parse results cacheable and renderable without unsafe lifetime extension.
Reusable code shape:
```rust
pub(crate) fn parse_markdown_with_options(
    text: &str,
    parse_html: bool,
    parse_heading_slugs: bool,
) -> ParsedMarkdownData {
    let mut state = ParseState::default();
    let mut html_blocks = BTreeMap::default();
    let mut parser = Parser::new_ext(text, PARSE_OPTIONS)
        .into_offset_iter()
        .peekable();

    while let Some((pulldown_event, range)) = parser.next() {
        match pulldown_event {
            pulldown_cmark::Event::Start(tag) => {
                if let pulldown_cmark::Tag::HtmlBlock = &tag {
                    state.push_event(range.clone(), MarkdownEvent::Start(MarkdownTag::HtmlBlock));
                    if parse_html {
                        if let Some(block) =
                            html::html_parser::parse_html_block(&text[range.clone()], range.clone())
                        {
                            html_blocks.insert(range.start, block);
                        }
                    }
                    continue;
                }
                /* convert borrowed tag into owned MarkdownTag */
            }
            _ => {}
        }
    }

    ParsedMarkdownData { events: state.events, html_blocks, /* indexes */ ..Default::default() }
}
```
Transfer rule: Apply when parser output borrows source text but UI rendering, incremental updates, or caching need owned event streams. Avoid losing byte ranges; downstream link, selection, and diagnostics code need source mapping.
Verification hook: Snapshot tests for links, headings with duplicate slugs, HTML blocks, code fences, footnotes, and entity substitutions.

### Concept: Debounced background parsing from immutable editor snapshots
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/zed-gpui/crates/csv_preview/src/parser.rs`
Why it matters: CSV preview reads an immutable `BufferSnapshot`, waits only if the debounce cooldown has not elapsed, parses on a background executor, then updates UI state in one `view.update` closure. The parser tracks byte ranges for every cell so table cells can map back to editor positions.
Reusable code shape:
```rust
fn parse_csv_in_background(
    &mut self,
    wait_for_debounce: bool,
    editor: Entity<Editor>,
    cx: &mut Context<Self>,
) -> Task<anyhow::Result<()>> {
    cx.spawn(async move |view, cx| {
        if wait_for_debounce {
            if let Some(wait_duration) = view.update(cx, |view, _| {
                view.last_parse_end_time
                    .and_then(|last| (Instant::now() < last + REPARSE_DEBOUNCE)
                        .then_some(last + REPARSE_DEBOUNCE - Instant::now()))
            })? {
                cx.background_executor().timer(wait_duration).await;
            }
        }

        let buffer_snapshot = view.update(cx, |_, cx| {
            editor.read(cx).buffer().read(cx).as_singleton().map(|b| b.read(cx).text_snapshot())
        })?;
        let Some(buffer_snapshot) = buffer_snapshot else { return Ok(()); };

        let parsed_csv = cx.background_spawn(async move { from_buffer(&buffer_snapshot) }).await;
        view.update(cx, move |view, cx| {
            view.engine.contents = parsed_csv;
            view.last_parse_end_time = Some(Instant::now());
            view.apply_filter_sort();
            cx.notify();
        })
    })
}
```
Transfer rule: Apply for editor plugins that parse active documents into side panels. Avoid parsing directly against mutable editor state across await points; snapshot first, then background parse.
Verification hook: Tests for quoted fields, escaped quotes, CRLF, multiline rows, empty files, byte-offset preservation, debounce timing, and stale parse result handling.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/JobSearchGames`

Codebase-memory: not run; `rg --files -g 'Cargo.toml' -g '*.rs'` found no Rust crate or Rust source in this checkout.

### Concept: Skipped because the checkout has no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/JobSearchGames`
Why it matters: This repo was assigned but does not provide source-backed Rust patterns for this archive.
Reusable code shape:
```text
No Cargo manifest or Rust source was present.
```
Transfer rule: Record coverage and move on. Avoid treating unrelated frontend/game code as Rust evidence.
Verification hook: Re-run `rg --files -g 'Cargo.toml' -g '*.rs' /Users/amuldotexe/Desktop/personal-repos-lane/JobSearchGames`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/apache-spark-shallow`

Codebase-memory: not run; `rg --files -g 'Cargo.toml' -g '*.rs'` found no Rust crate or Rust source in this checkout.

### Concept: Skipped because the checkout has no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/apache-spark-shallow`
Why it matters: Spark contains many parser and distributed system ideas, but this shallow checkout is not a Rust implementation surface.
Reusable code shape:
```text
No Cargo manifest or Rust source was present.
```
Transfer rule: Use as coverage only. Avoid translating Scala/Java patterns into Rust claims without a Rust source implementation.
Verification hook: Re-run `rg --files -g 'Cargo.toml' -g '*.rs' /Users/amuldotexe/Desktop/personal-repos-lane/apache-spark-shallow`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/ebooks2024`

Codebase-memory: not run; `rg --files -g 'Cargo.toml' -g '*.rs'` found no Rust crate or Rust source in this checkout.

### Concept: Skipped because the checkout has no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/ebooks2024`
Why it matters: No Rust or Rust-adjacent implementation files were available to extract.
Reusable code shape:
```text
No Cargo manifest or Rust source was present.
```
Transfer rule: Apply as a skip marker only.
Verification hook: Re-run `rg --files -g 'Cargo.toml' -g '*.rs' /Users/amuldotexe/Desktop/personal-repos-lane/ebooks2024`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network-message-queue-visual-lab`

Codebase-memory: not run; `rg --files -g 'Cargo.toml' -g '*.rs'` found no Rust crate or Rust source in this checkout.

### Concept: Skipped because the checkout has no Rust implementation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network-message-queue-visual-lab`
Why it matters: The repository name suggests queue visualization, but the assigned checkout did not contain Rust source-backed queue or concurrency implementations.
Reusable code shape:
```text
No Cargo manifest or Rust source was present.
```
Transfer rule: Use as negative coverage. Avoid extrapolating Rust queue patterns from non-Rust visual lab code.
Verification hook: Re-run `rg --files -g 'Cargo.toml' -g '*.rs' /Users/amuldotexe/Desktop/personal-repos-lane/floo-network-message-queue-visual-lab`.


## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/servo-test-202411`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From servo-test-202411
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/servo-test-202411/ports/servoshell/parser.rs:13` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 1049 Rust files, 58 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
use servo::servo_url::ServoUrl;

#[cfg(not(any(target_os = "android", target_env = "ohos")))]
pub fn parse_url_or_filename(cwd: &Path, input: &str) -> Result<ServoUrl, ()> {
    match ServoUrl::parse(input) {
        Ok(url) => Ok(url),
        Err(url::ParseError::RelativeUrlWithoutBase) => {
            url::Url::from_file_path(&*cwd.join(input)).map(ServoUrl::from_url)
        },
        Err(_) => Err(()),
    }
}

#[cfg(not(any(target_os = "android", target_env = "ohos")))]
pub fn get_default_url(
    url_opt: Option<&str>,
    cwd: impl AsRef<Path>,
    exists: impl FnOnce(&PathBuf) -> bool,
) -> ServoUrl {
    // If the url is not provided, we fallback to the homepage in prefs,
    // or a blank page in case the homepage is not set either.
    let mut new_url = None;
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/personal-repos-lane/servo-test-202411 -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/zztweets-of-amuldotexe2023`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/zztweets-of-amuldotexe2023`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/zztweets-of-amuldotexe2023 -g 'Cargo.toml' -g '*.rs'`


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/aquascope`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From aquascope
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/aquascope/crates/aquascope_front/src/plugin.rs:19` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 49 Rust files, 6 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
initialize_error_tracking, silent::silent_session, track_body_diagnostics,
  },
};
use clap::{Parser, Subcommand};
use fluid_let::fluid_set;
use rustc_hir::BodyId;
use rustc_interface::interface::Result as RustcResult;
use rustc_middle::ty::TyCtxt;
use rustc_plugin::{CrateFilter, RustcPlugin, RustcPluginArgs, Utf8Path};
use rustc_utils::{mir::borrowck_facts, source_map::find_bodies::find_bodies};
use serde::{self, Deserialize, Serialize};

const VERSION: &str = env!("CARGO_PKG_VERSION");

#[derive(Debug, Parser, Serialize, Deserialize)]
#[clap(version = VERSION)]
pub struct AquascopePluginArgs {
  #[clap(long)]
  should_fail: bool,

  #[clap(subcommand)]
  command: AquascopeCommand,
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/aquascope -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Skipped Repo: `/Users/amuldotexe/Desktop/reference-repos-yard/codemogger`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/codemogger`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/reference-repos-yard/codemogger -g 'Cargo.toml' -g '*.rs'`


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/kani`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From kani
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/kani/src/setup.rs:209` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 1762 Rust files, 213 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
Ok(String::from_utf8(output.stdout).map(|s| s.trim().to_string())?)
            } else {
                bail!(
                    "Could not parse rustc version string. Toolchain installation likely invalid. "
                );
            }
        }
        Err(_) => bail!("Could not get rustc version. Toolchain installation likely invalid"),
    }
}

/// The download URL for this version of Kani
fn download_url() -> String {
    let tag: &str = &format!("kani-{VERSION}");
    let file: &str = &download_filename();
    format!("https://github.com/model-checking/kani/releases/download/{tag}/{file}")
}

/// Give users a better error message than "404" if we're on an unsupported platform.
/// This is called just before we try to download the release bundle.
fn fail_if_unsupported_target() -> Result<()> {
    // This is basically going to be reduced to a compile-time constant
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/kani -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/miri`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From miri
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/miri/test-cargo-miri/src/main.rs:54` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 1270 Rust files, 27 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
#[cfg(unix)]
        for line in io::stdin().lock().lines() {
            let num: i32 = line.unwrap().parse().unwrap();
            println!("{}", 2 * num);
        }
        // On non-Unix, reading from stdin is not supported. So we hard-code the right answer.
        #[cfg(not(unix))]
        {
            println!("24");
            println!("42");
        }
    }
}

#[cfg(test)]
mod test {
    use byteorder_2::{BigEndian, ByteOrder};

    // Make sure in-crate tests with dev-dependencies work
    #[test]
    fn dev_dependency() {
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/miri -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_clr`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Rust Architecture Slice From rustc_codegen_clr
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_clr/src/function_sig.rs:15` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 400 Rust files, 23 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
ctx: &mut MethodCompileCtx<'tcx, '_>,
    sig: rustc_middle::ty::FnSigTys<TyCtxt<'tcx>>,
) -> FnSig {
    let output = get_type(ctx.monomorphize(sig.output()), ctx);
    let inputs: Box<[Type]> = sig
        .inputs()
        .iter()
        .map(|input| get_type(ctx.monomorphize(*input), ctx))
        .collect();
    FnSig::new(inputs, output)
}
/// Returns the signature of function behind `function`.
pub fn sig_from_instance_<'tcx>(
    function: Instance<'tcx>,
    ctx: &mut MethodCompileCtx<'tcx, '_>,
) -> Result<FnSig, CodegenError> {
    let fn_abi = ctx
        .tcx()
        .fn_abi_of_instance(rustc_middle::ty::PseudoCanonicalInput {
            typing_env: rustc_middle::ty::TypingEnv::fully_monomorphized(),
            value: (function, List::empty()),
        });
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_clr -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/tauri-template`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From tauri-template
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/tauri-template/src-tauri/src/types.rs:6` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 12 Rust files, 1 Cargo manifests, and 20 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
use regex::Regex;
use serde::{Deserialize, Serialize};
use specta::Type;
use std::sync::LazyLock;

/// Default shortcut for the quick pane
pub const DEFAULT_QUICK_PANE_SHORTCUT: &str = "CommandOrControl+Shift+.";

/// Maximum size for recovery data files (10MB)
pub const MAX_RECOVERY_DATA_BYTES: u32 = 10_485_760;

/// Pre-compiled regex pattern for filename validation.
/// Only allows alphanumeric characters, dashes, underscores, and a single extension.
pub static FILENAME_PATTERN: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(r"^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9]+)?$")
        .expect("Failed to compile filename regex pattern")
});

// ============================================================================
// Preferences
// ============================================================================
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/tauri-template -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.

## CodeGraphContext Evidence Appendix

### Concept: Interrupted Graph Index Must Fall Back To Source Evidence
Evidence: CodeGraphContext run `/tmp/codex-code-intel/codegraphcontext/tauri-20260706-225543` was started for `/Users/amuldotexe/Desktop/oss-read-only/tauri`, but `cgc stats` returned `Corrupted wal file` after the bounded interruption.
Why it matters: This is an agentic research pattern, not a Tauri code pattern. When a graph index is interrupted and the database cannot answer stats cleanly, the agent must not cite partial graph relationships as facts. The correct move is to record the attempt, keep the output directory for auditability, and rely on the direct source-backed entries already present in this shard.
Reusable code shape:
```text
graph index usable -> cite graph as navigation, then verify source
graph index unreadable -> cite only the attempt boundary, then verify source
```
Transfer rule: Use this boundary whenever a local code-intelligence database is interrupted, stale, or reports storage errors. Do not transfer architecture claims from a corrupted graph store.
Verification hook: Re-run `cgc stats` against `/tmp/codex-code-intel/codegraphcontext/tauri-20260706-225543/ladybugdb.sqlite`; if it still reports WAL corruption, ignore graph relationships and re-open the Tauri source files cited in this shard before reuse.
