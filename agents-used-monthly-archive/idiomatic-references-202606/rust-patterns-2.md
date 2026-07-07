# Rust Patterns 202606 Part 2

Purpose: capture Rust and Rust-adjacent architecture, idiom, parser, Tree-sitter, code-intelligence, async, CLI, API, storage, verification, and operational patterns discovered repo-by-repo under `/Users/amuldotexe/Desktop`.

Evidence policy: every non-obvious pattern should name the repository, file path, and why the code is reusable. Codebase-memory graph evidence is useful for discovery, but source paths and snippets are the authority.

Shard owner: parallel worker 2.
Shard repo count: 31.

## Assigned Repository Shard

- `/Users/amuldotexe/Desktop/methods-agents-hub/agent-room-of-requirements`
- `/Users/amuldotexe/Desktop/oss-read-only/alien`
- `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs`
- `/Users/amuldotexe/Desktop/oss-read-only/cocoindex`
- `/Users/amuldotexe/Desktop/oss-read-only/feldera`
- `/Users/amuldotexe/Desktop/oss-read-only/korrela-deployiq`
- `/Users/amuldotexe/Desktop/oss-read-only/pandas`
- `/Users/amuldotexe/Desktop/oss-read-only/polars`
- `/Users/amuldotexe/Desktop/oss-read-only/superset`
- `/Users/amuldotexe/Desktop/oss-read-only/wry`
- `/Users/amuldotexe/Desktop/personal-repos-lane/DSA108`
- `/Users/amuldotexe/Desktop/personal-repos-lane/algo-free-twitter-marination`
- `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go-org-github`
- `/Users/amuldotexe/Desktop/personal-repos-lane/dsa2024`
- `/Users/amuldotexe/Desktop/personal-repos-lane/felix-felicis`
- `/Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science-2026.03`
- `/Users/amuldotexe/Desktop/personal-repos-lane/law-diagrams`
- `/Users/amuldotexe/Desktop/personal-repos-lane/mp4-to-mp3`
- `/Users/amuldotexe/Desktop/personal-repos-lane/notes202408`
- `/Users/amuldotexe/Desktop/personal-repos-lane/priori-incantatem`
- `/Users/amuldotexe/Desktop/personal-repos-lane/rust-sop`
- `/Users/amuldotexe/Desktop/personal-repos-lane/transfiguration-cozo-graph-compiler`
- `/Users/amuldotexe/Desktop/personal-repos-lane/vscode-lumos`
- `/Users/amuldotexe/Desktop/personal-repos-lane/zzlow-drama-rust2023`
- `/Users/amuldotexe/Desktop/reference-repos-yard/Rudra`
- `/Users/amuldotexe/Desktop/reference-repos-yard/cargo-scan`
- `/Users/amuldotexe/Desktop/reference-repos-yard/dylint`
- `/Users/amuldotexe/Desktop/reference-repos-yard/hax`
- `/Users/amuldotexe/Desktop/reference-repos-yard/memelord`
- `/Users/amuldotexe/Desktop/reference-repos-yard/prusti-dev`
- `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_plugin`

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

## Repo Coverage: `/Users/amuldotexe/Desktop/methods-agents-hub/agent-room-of-requirements`

### Repo note: skipped implementation extraction because this workspace has Rust guidance but no Rust source
Evidence: `/Users/amuldotexe/Desktop/methods-agents-hub/agent-room-of-requirements/unclassified-yet/Rust Executable Specifications - single MD file.md`; `rg --files -g 'Cargo.toml'` and `rg --files -g '*.rs'` returned zero files for the repo.
Why it matters: This repository is useful as process doctrine for Rust agents, but the Worker 2 extraction target is source-backed Rust or Rust-adjacent implementation patterns. Treating markdown-only guidance as implementation evidence would blur the archive's standard.
Reusable code shape:
```rust
// No implementation snippet: repository contains Rust process notes, not Rust source.
```
Transfer rule: Use this repo for workflow language, quality gates, and executable-spec phrasing; avoid citing it as proof that a concrete Rust API shape compiles or scales.
Verification hook: `rg --files /Users/amuldotexe/Desktop/methods-agents-hub/agent-room-of-requirements -g 'Cargo.toml' -g '*.rs'` remains empty for implementation files.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/alien`

Codebase-memory: succeeded with smoke output at `/tmp/codex-code-intel/codebase-memory/alien-20260706-223409`; used only as discovery and verified against source below.

### Concept: Structured error metadata trait plus generic serializable error envelope
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alien/crates/alien-error/src/lib.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/alien-20260706-223409`.
Why it matters: The crate separates stable error semantics (`AlienErrorData`) from transport/rendering concerns (`AlienError<T>`). The trait requires every domain error to expose a machine-readable code, retryability, internal/external visibility, HTTP status, optional structured JSON context, and optional human remediation hint. The container then serializes those fields with `serde(rename_all = "camelCase")` and feature-gates OpenAPI schema derivation. This is a reusable pattern for agentic services because callers, CLIs, APIs, retry loops, and human renderers can reason about failures without string parsing.
Reusable code shape:
```rust
pub trait DomainErrorData {
    fn code(&self) -> &'static str;
    fn retryable(&self) -> bool;
    fn internal(&self) -> bool;
    fn message(&self) -> String;
    fn http_status_code(&self) -> u16 { 500 }
    fn context(&self) -> Option<serde_json::Value> { None }
    fn hint(&self) -> Option<String> { None }
}

#[derive(Debug, serde::Serialize, serde::Deserialize, Clone)]
#[serde(rename_all = "camelCase")]
pub struct DomainError<T: DomainErrorData + Clone + std::fmt::Debug + serde::Serialize> {
    pub code: String,
    pub message: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub context: Option<serde_json::Value>,
    pub retryable: bool,
    pub internal: bool,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub http_status_code: Option<u16>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub source: Option<Box<DomainError<GenericError>>>,
    #[serde(skip)]
    pub error: Option<T>,
}
```
Transfer rule: Apply when errors cross process, API, CLI, or agent boundaries and need policy-bearing metadata. Avoid for tiny private modules where `thiserror` plus `anyhow::Context` is enough and no machine policy consumes retryability/status/privacy fields.
Verification hook: Unit-test each error variant for `(code, retryable, internal, http_status_code, context, hint)` and snapshot the serialized JSON envelope so API clients do not receive accidental field-name or privacy regressions.

### Concept: Proc-macro derives exhaustive error-policy match arms from enum variants
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alien/crates/alien-error-derive/src/lib.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/alien-20260706-223409`.
Why it matters: `AlienErrorData` is implemented by a derive macro that rejects non-enums with `compile_error!` and generates one `match self` arm set per error-policy method. This keeps domain errors declarative at call sites while preserving static exhaustiveness: adding a variant forces the derive to assign code, retryability, internality, HTTP status, context, message, hint, and inheritance behavior. For agentic code assist, this is a strong pattern because the extension point is the enum attribute, not hand-edited boilerplate scattered through response mappers.
Reusable code shape:
```rust
#[proc_macro_derive(DomainErrorData, attributes(error))]
pub fn derive_domain_error_data(input: proc_macro::TokenStream) -> proc_macro::TokenStream {
    let input = syn::parse_macro_input!(input as syn::DeriveInput);
    let name = &input.ident;
    let syn::Data::Enum(data_enum) = input.data else {
        return quote::quote! {
            compile_error!("DomainErrorData can only be derived for enums");
        }.into();
    };

    let code_arms = data_enum.variants.iter().map(|variant| {
        let ident = &variant.ident;
        let matcher = quote::quote! { #name::#ident { .. } };
        let code = variant.ident.to_string().to_ascii_uppercase();
        quote::quote! { #matcher => #code }
    });

    quote::quote! {
        impl domain_error::DomainErrorData for #name {
            fn code(&self) -> &'static str {
                match self { #(#code_arms),* }
            }
        }
    }.into()
}
```
Transfer rule: Apply when a domain enum is the canonical error taxonomy and every variant must publish consistent operational metadata. Avoid when error variants are generic wrappers around arbitrary sources; in that case a manual `From` implementation or `thiserror` display may be clearer.
Verification hook: Add compile-fail UI tests for invalid derive targets and attribute mistakes; add ordinary tests that instantiate representative variants and assert generated method values.

### Concept: SDK boundary conversion that preserves documented API errors and transport causes
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alien/client-sdks/platform/rust/src/lib.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/alien-20260706-223409`.
Why it matters: The SDK extension trait maps a generated Progenitor `Result<ResponseValue<T>, Error<ApiError>>` into the house error envelope without losing status, retryability, structured context, or server-provided source chains. It treats `ErrorResponse` as first-class domain data and maps communication/body/validation cases separately. This is safer than `map_err(anyhow::Error::from)` for agentic systems because retry loops and user-facing tooling can distinguish server rejections from network failures.
Reusable code shape:
```rust
pub trait SdkResultExt<T> {
    fn into_sdk_error(self) -> Result<T, DomainError<GenericError>>;
}

impl<T> SdkResultExt<ResponseValue<T>> for Result<ResponseValue<T>, Error<ApiError>> {
    fn into_sdk_error(self) -> Result<ResponseValue<T>, DomainError<GenericError>> {
        self.map_err(convert_sdk_error)
    }
}

pub fn convert_sdk_error(err: Error<ApiError>) -> DomainError<GenericError> {
    match err {
        Error::ErrorResponse(response) => {
            let status = response.status().as_u16();
            let api_error = response.into_inner();
            DomainError {
                code: api_error.code.to_string(),
                message: api_error.message.to_string(),
                context: api_error.context,
                retryable: api_error.retryable,
                internal: false,
                http_status_code: Some(status),
                source: api_error.source.and_then(parse_source_error),
                error: Some(GenericError { message: api_error.message.to_string() }),
                hint: None,
            }
        }
        Error::CommunicationError(e) => DomainError {
            code: "COMMUNICATION_ERROR".to_string(),
            message: format!("Communication Error: {e}"),
            retryable: e.is_connect() || e.is_timeout() || e.is_request(),
            http_status_code: e.status().map(|s| s.as_u16()),
            source: build_reqwest_source(&e),
            internal: false,
            context: None,
            hint: None,
            error: Some(GenericError { message: format!("Communication Error: {e}") }),
        },
        other => map_remaining_generated_client_error(other),
    }
}
```
Transfer rule: Apply at generated-client boundaries, especially where OpenAPI/Protobuf clients already expose typed API error bodies. Avoid converting all errors to one variant unless no downstream component needs retry/status/context policy.
Verification hook: Table-test each generated client error variant. Include one server error with nested `source`, one timeout/connect error marked retryable, and one client-side invalid request marked non-retryable with status `400`.

### Concept: Ephemeral health listener registered with an outer runtime before spawning accept loop
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alien/examples/endpoint-agent/src/http.rs` and `/Users/amuldotexe/Desktop/oss-read-only/alien/examples/endpoint-agent/src/main.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/alien-20260706-223409`.
Why it matters: The endpoint agent binds `127.0.0.1:0`, reads the assigned port, registers that port with `AlienContext`, and only then spawns a lightweight Hyper HTTP/1 accept loop. This pattern decouples platform readiness from the main `ctx.run().await` event loop and avoids hard-coded ports in multi-agent or test environments. The service returns the chosen port to the caller, which can log or expose it.
Reusable code shape:
```rust
pub async fn start_health_server(ctx: &RuntimeContext) -> Result<u16, Box<dyn std::error::Error>> {
    let listener = tokio::net::TcpListener::bind("127.0.0.1:0").await?;
    let port = listener.local_addr()?.port();

    ctx.register_http_server(port).await?;

    tokio::spawn(async move {
        if let Err(error) = run_server(listener).await {
            tracing::error!("HTTP server error: {error}");
        }
    });

    Ok(port)
}

async fn run_server(listener: tokio::net::TcpListener) -> Result<(), Box<dyn std::error::Error>> {
    loop {
        let (stream, _) = listener.accept().await?;
        let io = hyper_util::rt::TokioIo::new(stream);
        tokio::spawn(async move {
            let _ = hyper::server::conn::http1::Builder::new()
                .serve_connection(io, hyper::service::service_fn(handle_request))
                .await;
        });
    }
}
```
Transfer rule: Apply for plugin/worker/agent runtimes that need an HTTP readiness shim but should not own a public fixed port. Avoid in production internet-facing services without shutdown, backpressure, request limits, and structured error propagation around the spawned tasks.
Verification hook: Integration-test that `start_health_server` returns a bound port, the runtime registration mock sees the same port, and `GET /` returns `200 ok` while the main event loop remains free to run.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs`

Codebase-memory: succeeded with smoke output at `/tmp/codex-code-intel/codebase-memory/arrow-rs-20260706-223552`; used only as discovery and verified against source below.

### Concept: Flat-struct derive macro that emits Parquet column readers and writers in source order
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs/parquet_derive/src/lib.rs` and `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs/parquet_derive/src/parquet_field.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/arrow-rs-20260706-223552`.
Why it matters: `ParquetRecordWriter` parses a `syn::DeriveInput`, accepts only structs, converts every named field into a `parquet_field::Field`, and emits a `RecordWriter` implementation whose generated snippets call `row_group_writer.next_column()` in the same order as the Rust struct fields. The companion `Field::writer_snippet` builds `vals`, optional `definition_levels`, and the typed `write_batch` call. The macro documents and enforces its intentional limitation: flat/simple structs and definition levels up to the supported depth. For agents, this is a reliable derive-macro shape: parse once into a small semantic model, generate narrow snippets, and make unsupported grammar obvious.
Reusable code shape:
```rust
#[proc_macro_derive(RecordWriter)]
pub fn record_writer(input: proc_macro::TokenStream) -> proc_macro::TokenStream {
    let input: syn::DeriveInput = syn::parse_macro_input!(input as syn::DeriveInput);
    let fields = match input.data {
        syn::Data::Struct(syn::DataStruct { fields, .. }) => fields,
        syn::Data::Enum(_) | syn::Data::Union(_) => unimplemented!("only structs are supported"),
    };

    let field_infos: Vec<_> = fields.iter().map(FieldInfo::from).collect();
    let writer_snippets: Vec<_> = field_infos.iter().map(FieldInfo::writer_snippet).collect();
    let name = input.ident;
    let generics = input.generics;

    quote::quote! {
        impl #generics record::RecordWriter<#name #generics> for &[#name #generics] {
            fn write_to_row_group<W: std::io::Write + Send>(&self, writer: &mut RowGroupWriter<W>) -> Result<()> {
                #( { #writer_snippets } );*
                Ok(())
            }
        }
    }.into()
}
```
Transfer rule: Apply when Rust type layout maps directly to a storage schema and generated code should look like hand-written per-field code. Avoid for recursively nested schemas unless the macro first grows a real intermediate representation for levels, repetition, and projection.
Verification hook: Add trybuild/compile-fail tests for enum/union/unnamed-field cases, plus round-trip tests that write and read a struct with nullable and non-nullable fields and assert field order matches the Parquet schema.

### Concept: Lazy validity bitmap materialization for null-aware column builders
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs/arrow-buffer/src/builder/null.rs` and `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs/arrow-array/src/builder/primitive_builder.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/arrow-rs-20260706-223552`.
Why it matters: `PrimitiveBuilder<T>` always appends values but delegates validity to `NullBufferBuilder`. The null builder stores `bitmap_builder: Option<BooleanBufferBuilder>` and only materializes the bitmap after a null is appended. If all values are non-null, `finish()` returns `None`, saving an allocation and the later cost of carrying a redundant all-true bitmap. This is a compact pattern for data systems where nullable columns are common in the type system but many concrete batches have no nulls.
Reusable code shape:
```rust
pub struct ValidityBuilder {
    bitmap: Option<BooleanBitmapBuilder>,
    len_before_materialized: usize,
    capacity_bits: usize,
}

impl ValidityBuilder {
    pub fn append_non_nulls(&mut self, n: usize) {
        if let Some(bitmap) = self.bitmap.as_mut() {
            bitmap.append_n(n, true);
        } else {
            self.len_before_materialized += n;
        }
    }

    pub fn append_null(&mut self) {
        if self.bitmap.is_none() {
            let mut bitmap = BooleanBitmapBuilder::new(self.capacity_bits);
            bitmap.append_n(self.len_before_materialized, true);
            self.bitmap = Some(bitmap);
        }
        self.bitmap.as_mut().unwrap().append(false);
    }

    pub fn finish(self) -> Option<NullBuffer> {
        self.bitmap.map(BooleanBitmapBuilder::finish)
    }
}
```
Transfer rule: Apply to columnar buffers, sparse validity masks, dirty flags, or optional side-channel metadata where the all-default case dominates. Avoid if downstream consumers require an explicit bitmap regardless of content or if materialization branches would complicate real-time code more than the allocation costs.
Verification hook: Test that appending only non-nulls leaves `finish()` as `None`; appending a null after non-nulls yields the expected bitmap length and booleans; benchmarks should include all-valid, first-null, and late-null workloads.

### Concept: Positional primitive builder stores default values for null slots and validity separately
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs/arrow-array/src/builder/primitive_builder.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/arrow-rs-20260706-223552`.
Why it matters: `PrimitiveBuilder<T>` appends a real `T::Native` value for every logical row, including `T::Native::default()` when appending nulls, and updates validity independently. This preserves index alignment between the values buffer and the logical array length, which makes slicing, SIMD/vectorized operations, FFI layout, and later array construction simpler. Null semantics become a bitmap concern instead of a `Vec<Option<T>>` layout concern.
Reusable code shape:
```rust
pub struct PrimitiveColumnBuilder<T: Default + Copy> {
    values: Vec<T>,
    validity: ValidityBuilder,
}

impl<T: Default + Copy> PrimitiveColumnBuilder<T> {
    pub fn append_value(&mut self, value: T) {
        self.validity.append_non_nulls(1);
        self.values.push(value);
    }

    pub fn append_null(&mut self) {
        self.validity.append_null();
        self.values.push(T::default());
    }

    pub fn append_option(&mut self, value: Option<T>) {
        match value {
            Some(value) => self.append_value(value),
            None => self.append_null(),
        }
    }
}
```
Transfer rule: Apply in vectorized engines, file decoders, and FFI-safe memory layouts where row position must be recoverable without chasing enum variants. Avoid if `T::default()` is expensive or semantically dangerous and the system cannot guarantee consumers always check the validity mask.
Verification hook: Property-test that `values.len() == validity.len()` after any sequence of `append_value`, `append_null`, `append_option`, and `append_values`; test that null rows never expose their default payload through safe APIs.

### Concept: Boundary wrapper validates schema invariants before crossing FFI/table APIs
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs/arrow-pyarrow/src/lib.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/arrow-rs-20260706-223552`.
Why it matters: The `Table` wrapper owns `Vec<RecordBatch>` plus a `SchemaRef`, and `Table::try_new` rejects any batch whose schema differs from the declared schema. `TryFrom<Box<dyn RecordBatchReader>>` collects a reader, keeps its schema, and reuses the same constructor. This pattern localizes a cross-language invariant before exporting/importing through PyArrow, making downstream conversion code work with a validated object instead of repeatedly checking every batch.
Reusable code shape:
```rust
pub struct BatchTable {
    batches: Vec<RecordBatch>,
    schema: SchemaRef,
}

impl BatchTable {
    pub fn try_new(batches: Vec<RecordBatch>, schema: SchemaRef) -> Result<Self, ArrowError> {
        for batch in &batches {
            if schema != batch.schema() {
                return Err(ArrowError::SchemaError(format!(
                    "all batches must have the same schema; expected {schema:?}, got {:?}",
                    batch.schema()
                )));
            }
        }
        Ok(Self { batches, schema })
    }

    pub fn into_inner(self) -> (Vec<RecordBatch>, SchemaRef) {
        (self.batches, self.schema)
    }
}
```
Transfer rule: Apply at FFI, plugin, serialization, or stream-materialization boundaries where a collection has a global invariant that individual elements cannot enforce. Avoid wrapping if the invariant is cheap and already encoded in the type system.
Verification hook: Unit-test mixed-schema inputs fail with a schema error; test `TryFrom<RecordBatchReader>` preserves the reader schema and rejects any collected inconsistent batch.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/cocoindex`

Codebase-memory: succeeded with smoke output at `/tmp/codex-code-intel/codebase-memory/cocoindex-20260706-223726`; used only as discovery and verified against source below.

### Concept: Optional app-wide semaphore with owned permits stored in per-component context
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/cocoindex/rust/core/src/engine/context.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/cocoindex-20260706-223726`.
Why it matters: `AppContext` accepts `max_inflight_components: Option<usize>` and converts it into `Option<Arc<tokio::sync::Semaphore>>`. `ComponentProcessorContext` stores an `Option<tokio::sync::OwnedSemaphorePermit>` behind a mutex, with `set_inflight_permit` and idempotent `release_inflight_permit`. This design lets deployments opt into bounded component execution without infecting every API with mandatory throttling, and it ties the permit lifetime to the component processing context rather than a temporary local variable that could be dropped too early.
Reusable code shape:
```rust
struct AppContextInner {
    inflight: Option<Arc<tokio::sync::Semaphore>>,
}

#[derive(Clone)]
pub struct AppContext {
    inner: Arc<AppContextInner>,
}

impl AppContext {
    pub fn new(max_inflight: Option<usize>) -> Self {
        Self {
            inner: Arc::new(AppContextInner {
                inflight: max_inflight.map(|n| Arc::new(tokio::sync::Semaphore::new(n))),
            }),
        }
    }

    pub fn inflight(&self) -> Option<&Arc<tokio::sync::Semaphore>> {
        self.inner.inflight.as_ref()
    }
}

struct ProcessorContext {
    permit: std::sync::Mutex<Option<tokio::sync::OwnedSemaphorePermit>>,
}

impl ProcessorContext {
    fn set_permit(&self, permit: tokio::sync::OwnedSemaphorePermit) {
        *self.permit.lock().unwrap() = Some(permit);
    }

    fn release_permit(&self) {
        *self.permit.lock().unwrap() = None;
    }
}
```
Transfer rule: Apply when concurrency limits are deployment policy and each work unit has a natural context object. Avoid if permit acquisition/release cannot be made exception-safe; then prefer RAII guards held directly on the stack.
Verification hook: Integration-test with `max_inflight = Some(1)` that two component builds do not overlap; assert `release_permit` is idempotent and permits are returned on cancellation/error paths.

### Concept: Fingerprint-keyed async memo entries model in-flight and ready states explicitly
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/cocoindex/rust/core/src/engine/context.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/cocoindex-20260706-223726`.
Why it matters: `FnCallMemoEntry<Prof>` has only two states: `Pending` and `Ready(Option<FnCallMemo<Prof>>)`, and `ComponentBuildingState` stores entries as `HashMap<Fingerprint, Arc<tokio::sync::RwLock<FnCallMemoEntry<Prof>>>>`. This is a compact concurrent memoization pattern: a fingerprint identifies deterministic work, an entry exists before computation finishes, and waiters can coordinate around a shared lock instead of launching duplicate work. The `Option` inside `Ready` also distinguishes “computed but memoization disabled/not applicable” from “still pending.”
Reusable code shape:
```rust
pub enum MemoEntry<T> {
    Pending,
    Ready(Option<T>),
}

impl<T> Default for MemoEntry<T> {
    fn default() -> Self {
        Self::Pending
    }
}

pub struct BuildState<T> {
    memos: HashMap<Fingerprint, Arc<tokio::sync::RwLock<MemoEntry<T>>>>,
}

async fn publish_ready<T>(entry: &tokio::sync::RwLock<MemoEntry<T>>, value: Option<T>) {
    *entry.write().await = MemoEntry::Ready(value);
}
```
Transfer rule: Apply for deterministic function calls, code-index chunks, embeddings, expensive parser passes, and workflow steps where duplicate concurrent execution is wasteful. Avoid if work is non-idempotent or side-effectful unless the fingerprint includes every side-effect dimension.
Verification hook: Race-test two concurrent requests for the same fingerprint and assert exactly one producer path runs; test `Ready(None)` does not get confused with `Pending`.

### Concept: Lazy language registry stores aliases and Tree-sitter terminal kind IDs once
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/cocoindex/rust/ops_text/src/prog_langs.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/cocoindex-20260706-223726`.
Why it matters: The registry maps `UniCase<&'static str>` aliases and extensions to shared `Arc<ProgrammingLanguageInfo>`. `TreeSitterLanguageInfo::new` converts a parser language plus terminal node kind names into numeric node kind IDs at registry construction time. Lookup is then cheap and case-insensitive, and parser-specific terminal logic is attached to language metadata instead of scattered through chunking code. The map panics on duplicate aliases, catching registry ambiguity at startup/tests.
Reusable code shape:
```rust
pub struct TreeSitterLanguageInfo {
    pub language: tree_sitter::Language,
    pub terminal_kind_ids: HashSet<u16>,
}

impl TreeSitterLanguageInfo {
    fn new(language: impl Into<tree_sitter::Language>, terminal_kinds: impl IntoIterator<Item = &'static str>) -> Self {
        let language = language.into();
        let terminal_kind_ids = terminal_kinds
            .into_iter()
            .filter_map(|kind| {
                let id = language.id_for_node_kind(kind, true);
                (id != 0).then_some(id)
            })
            .collect();
        Self { language, terminal_kind_ids }
    }
}

static LANGUAGE_INFO_BY_NAME: LazyLock<HashMap<UniCase<&'static str>, Arc<LanguageInfo>>> =
    LazyLock::new(|| {
        let mut map = HashMap::new();
        let mut add = |name: &'static str, aliases: &[&'static str], ts: Option<TreeSitterLanguageInfo>| {
            let info = Arc::new(LanguageInfo { name: Arc::from(name), treesitter: ts });
            for key in std::iter::once(name).chain(aliases.iter().copied()) {
                if map.insert(key.into(), info.clone()).is_some() {
                    panic!("Language `{key}` already exists");
                }
            }
        };
        add("rust", &[".rs"], Some(TreeSitterLanguageInfo::new(tree_sitter_rust::LANGUAGE, [])));
        map
    });
```
Transfer rule: Apply in code search, chunking, syntax-aware splitting, and language-router tools. Avoid hard-coding one-off extension matches once the system supports more than a handful of languages or needs parser metadata.
Verification hook: Unit-test canonical names, aliases, uppercase extensions, unknown extensions, and duplicate-alias panics; for each configured terminal node kind, test that `id_for_node_kind` does not silently return zero unless absence is intentionally allowed.

### Concept: Rust future wrapper cancels Python asyncio task on drop via thread-safe event-loop callback
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/cocoindex/rust/py_utils/src/future.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/cocoindex-20260706-223726`.
Why it matters: `from_py_future` captures `TaskLocals` event loop and context, schedules task creation with `call_soon_threadsafe`, bridges the Python task result through a Rust `oneshot`, and returns `CancelOnDropPy`. The wrapper implements `Future`, marks completion with an `AtomicBool`, and in `Drop` calls `task.cancel()` on the Python event loop if the Rust side is dropped before completion. This prevents orphaned asyncio tasks when Rust cancellation, timeout, or shutdown occurs.
Reusable code shape:
```rust
struct CancelOnDropPy {
    inner: futures::future::BoxFuture<'static, PyResult<Py<PyAny>>>,
    task_ref: Arc<Mutex<Option<Py<PyAny>>>>,
    event_loop: Py<PyAny>,
    ctx: Py<PyAny>,
    done: AtomicBool,
}

impl Future for CancelOnDropPy {
    type Output = PyResult<Py<PyAny>>;
    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        match Pin::new(&mut self.inner).poll(cx) {
            Poll::Ready(out) => {
                self.done.store(true, Ordering::SeqCst);
                Poll::Ready(out)
            }
            Poll::Pending => Poll::Pending,
        }
    }
}

impl Drop for CancelOnDropPy {
    fn drop(&mut self) {
        if self.done.load(Ordering::SeqCst) || unsafe { pyo3::ffi::Py_IsInitialized() == 0 } {
            return;
        }
        if let Some(task) = self.task_ref.lock().unwrap().take() {
            Python::attach(|py| {
                let _ = self.event_loop.bind(py).call_method(
                    "call_soon_threadsafe",
                    (task.bind(py).getattr("cancel")?,),
                    Some(&context_kwargs(py, &self.ctx)?),
                );
                Ok::<_, PyErr>(())
            }).ok();
        }
    }
}
```
Transfer rule: Apply when bridging Rust futures to Python awaitables in services, notebooks, or agent plugin runtimes where cancellation must propagate both ways. Avoid direct `create_task` from arbitrary Rust threads; schedule via the event loop to satisfy asyncio debug/runtime invariants.
Verification hook: Test that dropping the Rust future before completion calls Python task `cancel`; test completed futures do not cancel; run with `PYTHONASYNCIODEBUG=1` to catch cross-thread event-loop misuse.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/feldera`

Codebase-memory: succeeded with smoke output at `/tmp/codex-code-intel/codebase-memory/feldera-20260706-223854`; used only as discovery and verified against source below.

### Concept: Procedural macro output can be development-dumped and parsed back as `syn::File`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/feldera/crates/feldera-macros/src/lib.rs` and `/Users/amuldotexe/Desktop/oss-read-only/feldera/crates/feldera-macros/src/tuples.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/feldera-20260706-223854`.
Why it matters: `declare_tuple!` parses a custom `TupleDef`, generates tuple code, and, when `FELDERA_DEV_MACROS_DUMP` is set, reparses the generated `TokenStream` as `syn::File` and pretty-prints it with `prettyplease`. Tests do the same parse-back step and assert expected generated structures. This is a practical macro-development pattern: generated code is not only emitted but also treated as parseable Rust during development and tests, which catches malformed token generation before downstream users hit opaque compiler errors.
Reusable code shape:
```rust
#[proc_macro]
pub fn declare_model(input: proc_macro::TokenStream) -> proc_macro::TokenStream {
    let model = syn::parse_macro_input!(input as ModelDef);
    let expanded = declare_model_impl(model);

    if std::env::var_os("DEV_MACROS_DUMP").is_some() {
        let parsed: syn::File = syn::parse2(expanded.clone()).expect("generated invalid Rust");
        eprintln!("{}", prettyplease::unparse(&parsed));
    }

    expanded.into()
}

#[test]
fn generated_model_parses() {
    let model: ModelDef = syn::parse2(quote::quote!(Model<T0, T1>)).unwrap();
    let expanded = declare_model_impl(model);
    let parsed: syn::File = syn::parse2(expanded).expect("generated invalid Rust");
    assert!(prettyplease::unparse(&parsed).contains("pub struct Model"));
}
```
Transfer rule: Apply to nontrivial procedural macros that generate structs, impl blocks, storage layouts, or trait matrices. Avoid relying on pretty-printed string assertions for semantics; use them as smoke checks alongside compile-fail and runtime tests.
Verification hook: Run the macro crate tests with and without the dump env var; include `syn::parse2::<syn::File>` smoke tests for representative small and large expansions.

### Concept: Controller error enum owns HTTP status, machine code, serialization, and retry kind
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/feldera/crates/adapterlib/src/errors/controller.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/feldera-20260706-223854`.
Why it matters: `ControllerError` is a large operational enum with `serde(untagged)` variants, variant-specific serializers for `anyhow::Error`, storage, IO, encode, and transport errors, an `impl ResponseError` that maps variants to HTTP statuses, an `impl DbspDetailedError` that exposes stable error codes, and a `kind()` method that collapses errors to `std::io::ErrorKind`-like categories such as `ResourceBusy` and `Unsupported`. This pattern centralizes boundary behavior for a runtime/controller service: API clients, logs, metrics, and retry decisions see the same taxonomy.
Reusable code shape:
```rust
#[derive(Debug, serde::Serialize)]
#[serde(untagged)]
pub enum ControllerError {
    Config { config_error: Box<ConfigError> },
    UnknownInputEndpoint { endpoint_name: String },
    ParseError { endpoint_name: String, error: Box<ParseError> },
    #[serde(serialize_with = "serialize_anyhow_error")]
    OutputTransportError { endpoint_name: String, fatal: bool, error: anyhow::Error },
    StorageError { context: String, error: StorageError, backtrace: Box<std::backtrace::Backtrace> },
    TransactionInProgress,
    NoTransactionInProgress,
}

impl ResponseError for ControllerError {
    fn status_code(&self) -> StatusCode {
        match self {
            Self::Config { .. } | Self::ParseError { .. } => StatusCode::BAD_REQUEST,
            Self::UnknownInputEndpoint { .. } => StatusCode::NOT_FOUND,
            Self::TransactionInProgress => StatusCode::CONFLICT,
            Self::NoTransactionInProgress => StatusCode::BAD_REQUEST,
            _ => StatusCode::INTERNAL_SERVER_ERROR,
        }
    }
}

impl DetailedError for ControllerError {
    fn error_code(&self) -> Cow<'static, str> {
        match self {
            Self::Config { config_error } => Cow::from(format!("ConfigError.{}", config_error.error_code())),
            Self::UnknownInputEndpoint { .. } => Cow::from("UnknownInputEndpoint"),
            Self::TransactionInProgress => Cow::from("TransactionInProgress"),
            _ => Cow::from("InternalControllerError"),
        }
    }
}
```
Transfer rule: Apply to service/controller layers with many operational failure modes and stable clients. Avoid creating a monolithic error enum for low-level libraries; there, smaller typed errors composed upward are easier to maintain.
Verification hook: Table-test every externally visible variant for status code, error code, serialized shape, and retry/error kind; add a review check that new variants cannot land without explicit status/code/kind decisions.

### Concept: JSON tracing formatter injects runtime identity and preserves typed event fields
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/feldera/crates/feldera-observability/src/json_logging.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/feldera-20260706-223854`.
Why it matters: `JsonPipelineFormat` implements `tracing_subscriber::fmt::FormatEvent`, captures event fields with a custom `SerdeVisitor`, injects `LogIdentity` defaults such as service name, pipeline name, and pipeline ID, and lets structured event fields like `pipeline-name`, `pipeline`, `pipeline-id`, and `feldera-service` override those defaults. The visitor records typed values into `serde_json::Value` instead of forcing all fields through debug strings. This is a reusable logging shape for multi-tenant runtimes and agent workers where every log line must carry routing identity.
Reusable code shape:
```rust
#[derive(Clone)]
pub enum LogIdentity {
    Service { service_name: Option<&'static str> },
    Pipeline { pipeline_name: Option<String>, pipeline_id: Option<String> },
}

pub struct JsonFormat {
    identity: LogIdentity,
}

impl<S, N> tracing_subscriber::fmt::FormatEvent<S, N> for JsonFormat
where
    S: tracing::Subscriber + for<'a> tracing_subscriber::registry::LookupSpan<'a>,
    N: for<'a> tracing_subscriber::fmt::FormatFields<'a> + 'static,
{
    fn format_event(&self, _ctx: &FmtContext<'_, S, N>, mut writer: Writer<'_>, event: &tracing::Event<'_>) -> std::fmt::Result {
        let mut visitor = SerdeVisitor::default();
        event.record(&mut visitor);
        let mut pipeline_id = default_pipeline_id(&self.identity);
        if let Some(value) = visitor.fields.remove("pipeline-id") {
            pipeline_id = value_to_string(value);
        }
        let line = serde_json::json!({
            "timestamp": now_timestamp(),
            "pipeline_id": pipeline_id,
            "fields": visitor.fields,
            "target": event.metadata().target(),
            "level": event.metadata().level().to_string(),
        });
        writeln!(writer, "{line}")
    }
}

#[derive(Default)]
pub struct SerdeVisitor {
    pub fields: serde_json::Map<String, serde_json::Value>,
}
```
Transfer rule: Apply when a process emits logs for multiple services, tenants, agents, pipelines, or jobs and logs must be machine-routable. Avoid if plain text logs are the only target and no log aggregation layer consumes JSON.
Verification hook: Unit-test that identity defaults appear, event fields override identity, numeric/bool/string fields remain typed JSON, and the subscriber switches between JSON and plain-text formats based on the configured environment flag.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/korrela-deployiq`

Codebase-memory: succeeded with smoke output at `/tmp/codex-code-intel/codebase-memory/korrela-deployiq-20260706-224013`; used only as discovery and verified against source below.

### Concept: Async circuit breaker gates calls without holding a mutex across `.await`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/korrela-deployiq/crates/deployiq-core/src/circuit_breaker.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/korrela-deployiq-20260706-224013`.
Why it matters: `CircuitBreaker::call` locks state only for the gate check, transitions `Open` to `HalfOpen` on timeout, rejects immediately if still open, then drops the guard before awaiting the user future. Success/failure state is updated in separate short critical sections. The state machine is explicit (`Closed`, `Open { opened_at }`, `HalfOpen { successes }`), and tests verify threshold trip and reset-timeout recovery. This shape is easy for agents to reuse safely because it avoids the common bug of holding a `MutexGuard` across `.await`.
Reusable code shape:
```rust
#[derive(Debug, Clone, PartialEq)]
enum State {
    Closed,
    Open { opened_at: Instant },
    HalfOpen { successes: u32 },
}

#[derive(Clone)]
pub struct CircuitBreaker {
    inner: Arc<Mutex<Inner>>,
}

impl CircuitBreaker {
    pub async fn call<F, Fut, T, E>(&self, f: F) -> Result<T, CircuitBreakerError<E>>
    where
        F: FnOnce() -> Fut,
        Fut: Future<Output = Result<T, E>>,
    {
        {
            let mut guard = self.inner.lock().expect("circuit breaker mutex poisoned");
            guard.transition_if_timeout();
            if matches!(guard.state, State::Open { .. }) {
                return Err(CircuitBreakerError::Open);
            }
        }

        match f().await {
            Ok(value) => {
                self.on_success();
                Ok(value)
            }
            Err(error) => {
                self.on_failure();
                Err(CircuitBreakerError::Upstream(error))
            }
        }
    }
}
```
Transfer rule: Apply around flaky downstream ML/API/storage calls where fast failure plus recovery probes are better than piling on more load. Avoid wrapping non-idempotent operations unless callers can tolerate a half-open probe.
Verification hook: Async tests should cover threshold trip, immediate open rejection, reset-timeout half-open probe, success-threshold close, and static review/lint that no mutex guard lives across `.await`.

### Concept: Typed event-bus envelope separates routing metadata from domain payload
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/korrela-deployiq/crates/deployiq-core/src/event_bus.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/korrela-deployiq-20260706-224013`.
Why it matters: `BusEvent<T>` wraps every JetStream message with UUID, NATS subject, UTC timestamp, producing source, and generic payload. The `serde(bound(...))` annotation keeps the generic payload serializable/deserializable without forcing a concrete event enum too early. Well-known subjects are constants, and the bus owns stream configuration such as max delivery, ack wait, retention, and max pending acknowledgements. This creates a durable, inspectable event shape for multi-agent systems.
Reusable code shape:
```rust
#[derive(Debug, Clone, serde::Serialize, serde::Deserialize)]
#[serde(bound(
    serialize = "T: serde::Serialize",
    deserialize = "T: serde::de::DeserializeOwned"
))]
pub struct BusEvent<T> {
    pub id: String,
    pub subject: String,
    pub timestamp: chrono::DateTime<chrono::Utc>,
    pub source: String,
    pub payload: T,
}

impl<T: serde::Serialize> BusEvent<T> {
    pub fn new(subject: impl Into<String>, source: impl Into<String>, payload: T) -> Self {
        Self {
            id: uuid::Uuid::new_v4().to_string(),
            subject: subject.into(),
            timestamp: chrono::Utc::now(),
            source: source.into(),
            payload,
        }
    }
}
```
Transfer rule: Apply to NATS/Kafka/SQS/pubsub systems where multiple producers share infrastructure and consumers need consistent audit metadata. Avoid hiding subject/source only in broker headers if events are also persisted, replayed, or inspected as JSON.
Verification hook: Round-trip serialize/deserialize representative payloads, assert subject constants match broker subscriptions, and integration-test ack/nak/redelivery behavior for failed consumers.

### Concept: Redis `NX` plus TTL implements idempotent active-work marker under concurrency
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/korrela-deployiq/crates/deployiq-store/src/redis.rs` and `/Users/amuldotexe/Desktop/oss-read-only/korrela-deployiq/tests/integration/storage.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/korrela-deployiq-20260706-224013`.
Why it matters: `RedisStore::mark_active` stores an `ActiveDeployment` JSON record with `SetOptions::conditional_set(ExistenceCheck::NX)` and an expiration. It returns `bool`, making the caller handle “I won the idempotency race” versus “someone else already marked this active.” The integration test spawns 10 concurrent `mark_active` calls and asserts exactly one wins. This is a simple distributed coordination pattern for deployment agents and workers.
Reusable code shape:
```rust
pub async fn mark_active(&self, work: &ActiveWork) -> Result<bool> {
    let key = format!("active_work:{}", work.id);
    let value = serde_json::to_string(work)?;
    let mut conn = self.conn.clone();

    let inserted: bool = conn
        .set_options::<_, _, bool>(
            &key,
            value,
            redis::SetOptions::default()
                .with_expiration(redis::SetExpiry::EX(ACTIVE_TTL_SECS as usize))
                .conditional_set(redis::ExistenceCheck::NX),
        )
        .await?;

    Ok(inserted)
}
```
Transfer rule: Apply for best-effort idempotency and “only one worker starts this job” markers where eventual expiry is acceptable. Avoid for strict distributed locks that require fencing tokens, renewal, or linearizable ownership guarantees.
Verification hook: Integration-test first insert true, second insert false, post-delete insert true, and concurrent N-call race with exactly one `true`; test TTL expiry behavior separately if expiry is part of correctness.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/pandas`

### Repo note: skipped because no Rust or Rust-adjacent implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/oss-read-only/pandas -g 'Cargo.toml' -g '*.rs'` returned zero files; the initial Worker 2 signal pass also showed `Cargo=0` and `Rust=0`.
Why it matters: Pandas is relevant to data-frame architecture in general, but this shard is specifically mining Rust/Rust-adjacent source patterns. Without Rust manifests or Rust source, there is no source-backed Rust implementation pattern to extract here.
Reusable code shape:
```rust
// No Rust implementation snippet available in this checkout.
```
Transfer rule: Use Pandas as conceptual background only if a separate task asks for Python data-frame patterns; avoid citing it in this Rust pattern archive.
Verification hook: Re-run `rg --files /Users/amuldotexe/Desktop/oss-read-only/pandas -g 'Cargo.toml' -g '*.rs'` before future extraction attempts.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/polars`

Codebase-memory: succeeded with smoke output at `/tmp/codex-code-intel/codebase-memory/polars-20260706-224150`; used only as discovery and verified against source below.

### Concept: Error message wrapper chooses panic/backtrace/normal strategy from environment
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/polars/crates/polars-error/src/lib.rs` and `/Users/amuldotexe/Desktop/oss-read-only/polars/crates/polars-time/src/replace.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/polars-20260706-224150`.
Why it matters: `PolarsError` variants carry an `ErrString`, and `ErrString::from` consults a `LazyLock<ErrorStrategy>` driven by `POLARS_PANIC_ON_ERR` and `POLARS_BACKTRACE_IN_ERR`. The same `polars_bail!` and `polars_ensure!` call sites can therefore behave normally in production, panic for aggressive debugging, or attach forced backtraces to error strings. The call sites remain concise and semantic, e.g. `polars_ensure!(length == n || length == 1, length_mismatch = "dt.replace", ...)`.
Reusable code shape:
```rust
enum ErrorStrategy {
    Panic,
    WithBacktrace,
    Normal,
}

static ERROR_STRATEGY: LazyLock<ErrorStrategy> = LazyLock::new(|| {
    if std::env::var("APP_PANIC_ON_ERR").as_deref() == Ok("1") {
        ErrorStrategy::Panic
    } else if std::env::var("APP_BACKTRACE_IN_ERR").as_deref() == Ok("1") {
        ErrorStrategy::WithBacktrace
    } else {
        ErrorStrategy::Normal
    }
});

impl<T: Into<Cow<'static, str>>> From<T> for ErrString {
    #[track_caller]
    fn from(msg: T) -> Self {
        match &*ERROR_STRATEGY {
            ErrorStrategy::Panic => panic!("{}", msg.into()),
            ErrorStrategy::WithBacktrace => ErrString(Cow::Owned(format!(
                "{}\n\nRust backtrace:\n{}",
                msg.into(),
                std::backtrace::Backtrace::force_capture()
            ))),
            ErrorStrategy::Normal => ErrString(msg.into()),
        }
    }
}

macro_rules! app_ensure {
    ($cond:expr, $($tt:tt)+) => {
        if !$cond {
            return Err(app_err!($($tt)+));
        }
    };
}
```
Transfer rule: Apply in libraries with many validation sites where debug builds need stronger failure visibility without changing every call site. Avoid for externally stable error messages if embedding backtraces into messages would break clients; expose debug strategy behind a clearly documented flag.
Verification hook: Unit-test representative error creation under normal strategy; integration-test subprocesses with panic/backtrace env vars because `LazyLock` only reads environment once.

### Concept: Heterogeneous JSON schema inference deduplicates observed types and coerces to one Arrow dtype
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/polars/crates/polars-json/src/json/infer_schema.rs`; graph discovery: `/tmp/codex-code-intel/codebase-memory/polars-20260706-224150`.
Why it matters: `infer` maps scalar JSON nodes to Arrow dtypes, `infer_array` infers each element and collects into an index set to deduplicate types, and `coerce_dtype` merges the observed set. Structs are handled by unioning field names and coercing each field's observed dtypes; lists and scalars coerce to a compatible `LargeList`; null disappears in favor of the non-null type; incompatible types fall back to `LargeUtf8`. This pattern is reusable for schema-on-read parsers because it encodes messy-input policy in one coercion function.
Reusable code shape:
```rust
pub fn infer_json(value: &JsonValue) -> Result<DataType> {
    Ok(match value {
        JsonValue::Bool(_) => DataType::Boolean,
        JsonValue::I64(_) => DataType::Int64,
        JsonValue::F64(_) => DataType::Float64,
        JsonValue::Null => DataType::Null,
        JsonValue::String(_) => DataType::Utf8,
        JsonValue::Array(values) => infer_array(values)?,
        JsonValue::Object(fields) => infer_object(fields)?,
    })
}

fn infer_array(values: &[JsonValue]) -> Result<DataType> {
    let types = values.iter().map(infer_json).collect::<Result<IndexSet<_>>>()?;
    let dtype = if types.is_empty() {
        DataType::Null
    } else {
        coerce_dtype(&types.into_iter().collect::<Vec<_>>())
    };
    Ok(DataType::List(Box::new(Field::new("item", dtype, true))))
}

fn coerce_dtype(types: &[DataType]) -> DataType {
    match types {
        [] => DataType::Null,
        [only] => only.clone(),
        _ if all_structs(types) => union_struct_fields(types),
        _ if all_lists(types) => list_of_coerced_inner(types),
        _ if contains_float_and_int(types) => DataType::Float64,
        _ if contains_null(types) => coerce_without_null(types),
        _ => DataType::Utf8,
    }
}
```
Transfer rule: Apply to JSON/CSV/NDJSON ingestion, log parsing, or schema discovery where type instability must produce a deterministic schema. Avoid if lossy fallback to string is unacceptable; then return a typed schema conflict instead.
Verification hook: Table-test scalar, empty array, mixed int/float, null-plus-type, list-plus-scalar, heterogeneous struct fields, and incompatible values that must fall back to string.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/superset`

### Repo note: skipped because no Rust or Rust-adjacent implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/oss-read-only/superset -g 'Cargo.toml' -g '*.rs'` returned zero files; the initial Worker 2 signal pass showed `Cargo=0` and `Rust=0`.
Why it matters: Superset may contain useful analytics and service design ideas, but this archive requires source-backed Rust/Rust-adjacent patterns. This checkout has no Rust implementation surface to cite.
Reusable code shape:
```rust
// No Rust implementation snippet available in this checkout.
```
Transfer rule: Skip for Rust pattern extraction; revisit only for Python/TypeScript web analytics patterns.
Verification hook: Re-run `rg --files /Users/amuldotexe/Desktop/oss-read-only/superset -g 'Cargo.toml' -g '*.rs'` before future Rust extraction.

## Repo Coverage: `/Users/amuldotexe/Desktop/oss-read-only/wry`

Codebase-memory: not run after coordinator switched Worker 2 to bounded completion mode; `rg` sampling plus direct source snippets were used.

### Concept: Webview context owns platform state and rejects duplicate custom protocols
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/wry/src/web_context.rs` and `/Users/amuldotexe/Desktop/oss-read-only/wry/src/error.rs`.
Why it matters: `WebContext` carries optional data-directory state, platform implementation state, and a `HashSet<String>` of registered custom protocols. On Linux/BSD targets, `register_custom_protocol` returns `ContextDuplicateCustomProtocol` if the same protocol is registered twice on one context. This makes a platform-level global-ish resource explicit and prevents late webview failures from duplicate URL-scheme registration.
Reusable code shape:
```rust
pub struct WebContext {
    data_directory: Option<PathBuf>,
    os: PlatformContext,
    custom_protocols: HashSet<String>,
}

impl WebContext {
    pub fn register_custom_protocol(&mut self, name: String) -> Result<(), Error> {
        if self.custom_protocols.contains(&name) {
            return Err(Error::ContextDuplicateCustomProtocol(name));
        }
        self.custom_protocols.insert(name);
        Ok(())
    }
}
```
Transfer rule: Apply when a builder/context owns scarce platform registrations, names, sockets, routes, or schemes. Avoid silently overwriting registrations; duplicate setup should be a typed error.
Verification hook: Unit-test duplicate registration returns the duplicate-protocol error and leaves the set unchanged.

### Concept: Custom-protocol workaround rewrites unsupported schemes into interceptable HTTP(S) host prefixes
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/wry/src/custom_protocol_workaround.rs`.
Why it matters: Some platforms cannot register arbitrary URL schemes. Wry converts `{protocol}://localhost/path` into `{http_or_https}://{protocol}.localhost/path`, intercepts matching HTTP(S) requests, then reverts the URI before passing it to the custom protocol handler. The logic is a tiny pure module with prefix builders and tests, isolating platform workaround behavior from the main webview API.
Reusable code shape:
```rust
pub fn is_workaround_uri(uri: &str, http_or_https: &str, protocol: &str) -> bool {
    uri.strip_prefix(http_or_https)
        .and_then(|rest| rest.strip_prefix("://"))
        .and_then(|rest| rest.strip_prefix(protocol))
        .and_then(|rest| rest.strip_prefix("."))
        .is_some()
}

pub fn apply_workaround(uri: &str, http_or_https: &str, protocol: &str) -> String {
    uri.replace(&format!("{protocol}://"), &format!("{http_or_https}://{protocol}."))
}
```
Transfer rule: Apply when a platform lacks a feature but supports a narrower primitive that can be made equivalent with a reversible encoding. Avoid if security policy depends on exact origin semantics and the rewritten host would weaken isolation.
Verification hook: Unit-test apply/revert round-trips and matcher false positives for adjacent protocol names.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/DSA108`

### Repo note: skipped because no Rust implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/DSA108 -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: No source-backed Rust pattern can be extracted from this checkout.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Skip for Rust archive coverage unless Rust files are added later.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/DSA108 -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/algo-free-twitter-marination`

### Repo note: skipped because no Rust implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/algo-free-twitter-marination -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: The repo may be useful for product or content context, but not for source-backed Rust pattern extraction.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Skip for Rust archive coverage unless a Rust crate appears.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/algo-free-twitter-marination -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go-org-github`

### Repo note: skipped because no Rust implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/before-i-go-org-github -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: No Rust/Rust-adjacent implementation pattern is available to cite.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Skip for Rust pattern extraction.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/before-i-go-org-github -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/dsa2024`

Codebase-memory: not run in bounded completion mode; `rg` sampling plus source snippets were used.

### Concept: Educational algorithm variants expose ownership and complexity tradeoffs side by side
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/dsa2024/zzArchivePre202409/zzA010ArchivePre202407/rust blind75/src/a001_contains_duplicates.rs`.
Why it matters: The same “contains duplicate” problem is implemented as brute force over `Vec<i32>`, in-place `sort_unstable` over `&mut [i32]`, cloned sort over `Vec<i32>`, and `HashSet::insert` early return. This is useful for agentic teaching and code review because the signatures surface ownership tradeoffs: consuming a vector, mutating a borrowed slice, cloning to preserve input order, or allocating a set for O(n) average time.
Reusable code shape:
```rust
pub fn contains_duplicate_sorted(nums: &mut [i32]) -> bool {
    nums.sort_unstable();
    nums.windows(2).any(|window| window[0] == window[1])
}

pub fn contains_duplicate_hashset(nums: Vec<i32>) -> bool {
    let mut seen = std::collections::HashSet::new();
    for num in nums {
        if !seen.insert(num) {
            return true;
        }
    }
    false
}
```
Transfer rule: Apply when teaching or benchmarking alternative Rust API ownership shapes. For production, prefer the `&mut [T]` sorting variant when mutation is allowed and allocation should be avoided; prefer the `HashSet` variant when preserving order/input and average linear time matter.
Verification hook: Replace the current placeholder tests with duplicate/no-duplicate/empty/singleton tests for all variants; review that `contains_duplicate_01` handles empty input before using it.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/felix-felicis`

### Repo note: skipped because no Rust implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/felix-felicis -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: No Rust/Rust-adjacent implementation pattern is available to cite from this checkout.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Skip for Rust archive coverage unless Rust files are added later.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/felix-felicis -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science-2026.03`

Codebase-memory: not run in bounded completion mode; `rg` sampling plus source snippets were used.

### Concept: Rust generator CLI uses const arithmetic, custom clap parsers, and enum value filters for foreign-language code generation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/graph-data-science-2026.03/core/src/main/java/org/neo4j/gds/core/compression/packed/gen_packing.rs`.
Why it matters: This Java project embeds a Rust code generator for packed-compression classes. It computes packing dimensions with `const fn`, validates `--block-size` with a custom parser that enforces range and power-of-two invariants, and implements `clap::ValueEnum` for include/exclude filters. The pattern is useful when Rust is the safest/fastest generator implementation even if the generated artifact targets another language.
Reusable code shape:
```rust
const fn words_for_bits(block_size: u32, bits: u32) -> u32 {
    (block_size * bits + LONG_BITS - 1) / LONG_BITS
}

fn parse_block_size(s: &str) -> Result<u32, String> {
    let bs = s.parse().map_err(|e| format!("must be a number: {e}"))?;
    if !(1..=LONG_BITS).contains(&bs) {
        return Err(format!("must be between 1 and {LONG_BITS}"));
    }
    if !bs.is_power_of_two() {
        return Err("must be a power of two".into());
    }
    Ok(bs)
}

let matches = clap::Command::new(file!())
    .arg(clap::Arg::new("block-size").long("block-size").value_parser(parse_block_size))
    .arg(clap::Arg::new("include").long("include").action(clap::ArgAction::Append)
        .value_parser(clap::builder::EnumValueParser::<Includes>::new()))
    .get_matches();
```
Transfer rule: Apply for deterministic source generation where validation and arithmetic are easier to express in Rust than shell/templates. Avoid if the generator cannot be run in the target repo's normal build/tooling flow.
Verification hook: Add golden-file tests for generated output, parser tests for invalid block sizes, and CI that runs the generator and checks no generated file diff remains.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/law-diagrams`

### Repo note: skipped because no Rust implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/law-diagrams -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: No Rust source-backed implementation pattern is available.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Skip for Rust archive coverage.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/law-diagrams -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/mp4-to-mp3`

### Repo note: skipped because no Rust implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/mp4-to-mp3 -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: No Rust source-backed implementation pattern is available.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Skip for Rust archive coverage.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/mp4-to-mp3 -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/notes202408`

### Repo note: skipped because no Rust implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/notes202408 -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: Notes-only repositories can inform process but cannot support concrete Rust implementation claims.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Skip for Rust archive coverage.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/notes202408 -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/priori-incantatem`

### Repo note: skipped because no Rust implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/priori-incantatem -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: The repo contains Rust architecture notes and deconstruction documents, but no Rust source files or manifests in this checkout.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Use only as secondary conceptual reading, not source-backed Rust evidence.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/priori-incantatem -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/rust-sop`

### Repo note: skipped because it contains Rust SOP/reference notes but no Rust implementation files
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/rust-sop -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: The repository is relevant to Rust workflow doctrine, but the extraction job requires implementation-backed Rust patterns.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Use for SOP language only; avoid citing as compiling source.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/rust-sop -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/transfiguration-cozo-graph-compiler`

### Repo note: skipped because it contains graph/compiler reference notes but no Rust implementation files
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/transfiguration-cozo-graph-compiler -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: The repo mentions Tree-sitter, `syn`, and graph-compiler references, but has no checked-in Rust source to verify concrete implementation shapes.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Treat as reference-roadmap material only, not pattern evidence.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/transfiguration-cozo-graph-compiler -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/vscode-lumos`

### Repo note: skipped because no Rust implementation files were present
Evidence: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/vscode-lumos -g 'Cargo.toml' -g '*.rs'` returned zero files.
Why it matters: No Rust/Rust-adjacent implementation pattern is available.
Reusable code shape:
```rust
// No Rust implementation snippet available.
```
Transfer rule: Skip for Rust archive coverage.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/vscode-lumos -g 'Cargo.toml' -g '*.rs'`.

## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/zzlow-drama-rust2023`

Codebase-memory: not run in bounded completion mode; `rg` sampling plus source snippets were used.

### Concept: Beginner CLI input loop shows owned `String` buffer passed mutably to stdin
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/zzlow-drama-rust2023/zzArchive/WorkingExamples20240119/prac_20231021p1/src/main.rs`.
Why it matters: The repo only contains minimal archived Rust examples, but the guessing-game file demonstrates the canonical beginner shape for reading a line: create an owned mutable `String`, pass `&mut` to `io::stdin().read_line`, and then use the captured text. It is not advanced, but it is a useful reminder for agent-generated teaching examples.
Reusable code shape:
```rust
use std::io;

fn main() {
    let mut guess = String::new();
    io::stdin()
        .read_line(&mut guess)
        .expect("failed to read line");
    println!("You guessed: {guess}");
}
```
Transfer rule: Apply only in tutorials or throwaway CLIs. In production CLIs, return `io::Result<()>` or add structured error context instead of `expect`.
Verification hook: `cargo run` in the tiny example crate should prompt, accept one line, and echo it.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/Rudra`

Codebase-memory: not run in bounded completion mode; `rg` sampling plus source snippets were used.

### Concept: `syn::Visit` stack tracks unsafe blocks, unsafe functions, and loops inside unsafe regions
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/Rudra/crawl/src/stat.rs`.
Why it matters: Rudra's crawl tool combines `tokei` line statistics with a custom `syn::Visit` traversal. The visitor pushes `FunctionStat` on function entry, increments nested unsafe depth in `visit_expr_unsafe`, marks loops while inside unsafe code, and folds visitor counters back into a per-file `Stat`. This is a reusable lightweight static-analysis pattern for pre-rustc scans where full compiler integration is too expensive.
Reusable code shape:
```rust
struct FunctionStat {
    is_unsafe: bool,
    contains_unsafe: bool,
    loop_in_unsafe: bool,
    nested_unsafe_block: usize,
}

impl<'ast> syn::visit::Visit<'ast> for StatVisitor<'ast> {
    fn visit_item_fn(&mut self, node: &'ast syn::ItemFn) {
        self.enter_fn(&node.sig);
        syn::visit::visit_item_fn(self, node);
        self.leave_fn();
    }

    fn visit_expr_unsafe(&mut self, node: &'ast syn::ExprUnsafe) {
        self.enter_unsafe();
        syn::visit::visit_expr_unsafe(self, node);
        self.leave_unsafe();
    }
}
```
Transfer rule: Apply for repository-wide metrics, lint prototypes, and risk scouting. Avoid for semantic analyses that need type information, macro expansion, or borrow-checker facts.
Verification hook: Fixture files should cover unsafe fn, safe fn containing unsafe block, global unsafe block, and loops nested inside/outside unsafe.

### Concept: Parser-heavy Rayon crawls can set explicit worker stack size
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/Rudra/crawl/src/bin/unsafe-counter.rs`.
Why it matters: The unsafe counter initializes a global Rayon pool with `num_cpus::get()` threads and `stack_size(8 * 1024 * 1024)` because `syn` parsing requires a larger stack. This is a practical pattern for batch AST crawlers: the default thread stack may work on small files but fail on deeply nested/generated code.
Reusable code shape:
```rust
fn setup_rayon_for_syn() {
    rayon::ThreadPoolBuilder::new()
        .num_threads(num_cpus::get())
        .stack_size(8 * 1024 * 1024)
        .build_global()
        .expect("failed to initialize parser thread pool");
}
```
Transfer rule: Apply to parallel parsers over untrusted or generated Rust source. Avoid changing the global Rayon pool inside libraries; let binaries own global pool setup.
Verification hook: Run crawler fixtures with deeply nested generated Rust and confirm no stack overflow; review that setup runs once before any Rayon work starts.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/cargo-scan`

Codebase-memory: not run in bounded completion mode; `rg` sampling plus source snippets were used.

### Concept: Audit-chain manifest serializes crate policies while skipping runtime manifest path
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/cargo-scan/src/audit_chain.rs`.
Why it matters: `AuditChain` stores `crate_path`, a `HashMap<CrateId, (PathBuf, AuditVersion)>`, and scanned effect types, but marks `manifest_path` with `#[serde(skip)]`. `read_audit_chain` restores the manifest path from the file being read, while `save_to_file` takes the path out before TOML serialization. This separates persisted audit policy from runtime location state, a useful pattern for local security/audit manifests.
Reusable code shape:
```rust
#[derive(serde::Serialize, serde::Deserialize)]
pub struct AuditChain {
    #[serde(skip)]
    manifest_path: PathBuf,
    crate_path: PathBuf,
    crate_policies: HashMap<CrateId, (PathBuf, AuditVersion)>,
    scanned_effects: Vec<EffectType>,
}

impl AuditChain {
    pub fn read(path: PathBuf) -> anyhow::Result<Option<Self>> {
        if path.is_file() {
            let raw = std::fs::read_to_string(&path)?;
            let mut chain: Self = toml::from_str(&raw)?;
            chain.manifest_path = path;
            Ok(Some(chain))
        } else {
            Ok(None)
        }
    }
}
```
Transfer rule: Apply when a manifest needs a runtime source path for saving/reloading but should not serialize that path into portable configuration. Avoid if path identity is itself part of the manifest's meaning.
Verification hook: Round-trip a manifest through TOML and assert `manifest_path` is restored from the read path, not the serialized content.

### Concept: Audit effect printer converts source line ranges into codespan diagnostics with bounded context
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/cargo-scan/src/auditing/info.rs`.
Why it matters: `print_effect_src` reads the source file, builds a map of line numbers to byte ranges, bounds context with saturating arithmetic around the effect location, and uses `codespan_reporting` labels to highlight both the effect and optionally the caller signature if it lies outside the context window. This is a reusable UX pattern for security scanners: findings should point at exact source bytes with just enough surrounding code.
Reusable code shape:
```rust
let bounded_start = start_line.saturating_sub(config.lines_before as usize);
let bounded_end = std::cmp::min(end_line + config.lines_after as usize, line_ranges.len());
let effect_start = line_ranges.get(&start_line).unwrap().0;
let effect_end = line_ranges.get(&end_line).unwrap().1;

let mut files = codespan_reporting::files::SimpleFiles::new();
let file_id = files.add(file_path.display().to_string(), source);
let labels = vec![codespan_reporting::diagnostic::Label::primary(
    file_id,
    effect_start..effect_end,
)];
let diagnostic = codespan_reporting::diagnostic::Diagnostic::help()
    .with_code("Audit location")
    .with_labels(labels);
```
Transfer rule: Apply to analyzers, linters, and audit tools that need actionable review output. Avoid raw line-number-only reports for findings that humans must triage.
Verification hook: Snapshot terminal output for findings at file start, file end, and with caller signatures outside the local context range.

## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/dylint`

Codebase-memory: not run in bounded completion mode; `rg` sampling plus source snippets were used.

### Concept: Cargo subcommand CLI wraps real command under `cargo <subcommand>` parser shape
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/dylint/cargo-dylint/src/main.rs`.
Why it matters: `cargo-dylint` declares `#[clap(bin_name = "cargo", display_name = "cargo")]` and parses a top-level `CargoSubcommand::Dylint(Dylint)`. The `Dylint` struct uses flattened reusable option groups, optional nested operations, `ArgAction::Append` package selectors, and `#[clap(last = true)]` to forward trailing args to `cargo check`. This is a strong pattern for Rust tools that should feel native as Cargo subcommands.
Reusable code shape:
```rust
#[derive(Debug, clap::Parser)]
#[clap(bin_name = "cargo", display_name = "cargo")]
struct Opts {
    #[clap(subcommand)]
    subcmd: CargoSubcommand,
}

#[derive(Debug, clap::Parser)]
enum CargoSubcommand {
    Mytool(Mytool),
}

#[derive(Debug, clap::Parser)]
struct Mytool {
    #[clap(action = clap::ArgAction::Append, short, long = "package")]
    packages: Vec<String>,
    #[clap(last = true, help = "Arguments for cargo check")]
    cargo_args: Vec<String>,
    #[clap(flatten)]
    output: OutputOptions,
}
```
Transfer rule: Apply for `cargo-foo` binaries that users invoke as `cargo foo`. Avoid hand-parsing `std::env::args` once subcommands, forwarded args, and reusable option groups appear.
Verification hook: CLI snapshot tests should cover `cargo dylint -- --features x`, repeated `--package`, subcommands, and help text.

### Concept: Integration tests build temporary lint libraries and assert discovery across toolchains/paths
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/dylint/cargo-dylint/tests/integration/list.rs`.
Why it matters: Tests create temporary library templates, patch rust-toolchain and `clippy_utils` revisions, build each template with sanitized environment, set `DYLINT_LIBRARY_PATH`, and assert `cargo-dylint list --all --no-metadata` reports both `name@toolchain` entries or both paths. This is a reusable testing strategy for plugin systems where discovery depends on filesystem layout, compiled artifacts, and toolchain metadata.
Reusable code shape:
```rust
let tempdir = tempfile::tempdir().unwrap();
new_template(tempdir.path()).unwrap();
patch_template(tempdir.path(), channel, clippy_utils_rev)?;
cargo_build("template")
    .sanitize_environment()
    .current_dir(&tempdir)
    .success()?;

cargo_bin_cmd!("cargo-mytool")
    .env("MYTOOL_LIBRARY_PATH", target_debug(tempdir.path())?)
    .args(["mytool", "list", "--all"])
    .assert()
    .success()
    .stdout(predicate::str::contains(format!("plugin@{channel}")));
```
Transfer rule: Apply to dynamic lint/plugin/driver loaders where unit tests cannot prove discovery behavior. Avoid relying on the developer's ambient rustup/cargo env; sanitize and construct the fixture explicitly.
Verification hook: Tests should cover duplicate names across toolchains, duplicate names across paths, missing metadata, and explicit environment variable overrides.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/hax`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Proc Macro Expansion Pattern From hax
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/hax/engine/names/src/lib.rs:223` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 363 Rust files, 80 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
fn while_loop_return() {}
    fn repeat() {}
    fn update_at() {}
    mod monomorphized_update_at {
        fn update_at_usize() {}
        fn update_at_range() {}
        fn update_at_range_from() {}
        fn update_at_range_to() {}
        fn update_at_range_full() {}
    }
    // TODO: Should that live here? (this is F* specific)
    fn array_of_list() {}
    fn never_to_any() {}

    mod folds {
        fn fold_range() {}
        fn fold_range_cf() {}
        fn fold_range_return() {}
        fn fold_range_step_by() {}
        fn fold_range_step_by_cf() {}
        fn fold_range_step_by_return() {}
        fn fold_enumerated_slice() {}
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/hax -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Skipped Repo: `/Users/amuldotexe/Desktop/reference-repos-yard/memelord`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/memelord`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/reference-repos-yard/memelord -g 'Cargo.toml' -g '*.rs'`


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/prusti-dev`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From prusti-dev
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/prusti-dev/prusti-server/src/driver.rs:7` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 1941 Rust files, 43 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

use clap::Parser;
use prusti_utils::config;

/// A verification server to handle Prusti verification requests.
#[derive(Parser, Debug)]
#[clap(version, about, long_about = None)]
struct Args {
    /// Sets the port on which to listen for incoming verification requests.
    /// Pass 0 to get a free one assigned by the OS.
    #[clap(short, long, value_name = "PORT", default_value_t = 0)]
    port: u16,
}

fn main() {
    env_logger::init_from_env(
        env_logger::Env::new()
            .filter_or("PRUSTI_LOG", config::log())
            .write_style_or("PRUSTI_LOG_STYLE", config::log_style()),
    );
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/prusti-dev -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_plugin`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From rustc_plugin
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_plugin/crates/rustc_utils/src/mir/borrowck_facts.rs:3` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 39 Rust files, 9 Cargo manifests, and 34 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
//! Polonius integration to extract borrowck facts from rustc.

use std::sync::atomic::{AtomicBool, Ordering};

use rustc_borrowck::consumers::{BodyWithBorrowckFacts, ConsumerOptions};
use rustc_data_structures::fx::FxHashSet as HashSet;
use rustc_hir::def_id::LocalDefId;
use rustc_middle::{
  mir::{Body, ConcreteOpaqueTypes, StatementKind, TerminatorKind},
  ty::TyCtxt,
  util::Providers,
};
use rustc_span::ErrorGuaranteed;

use crate::{BodyExt, block_timer, cache::Cache};

/// MIR pass to remove instructions not important for Flowistry.
///
/// This pass helps reduce the number of intermediates during dataflow analysis, which
/// reduces memory usage.
pub fn simplify_mir(body: &mut Body<'_>) {
  let return_blocks = body
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/rustc_plugin -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.

## CodeGraphContext Evidence Appendix

### Concept: Graph-Indexed DataFrame And Lazy Plan Separation
Evidence: CodeGraphContext run `/tmp/codex-code-intel/codegraphcontext/polars-20260706-225543` produced readable stats for 1 repository, 719 files, 8,723 functions, 196 traits, 293 structs, 70 enums, and 870 modules; `cgc find name DataFrame` returned `/Users/amuldotexe/Desktop/oss-read-only/polars/crates/polars-core/src/frame/dataframe.rs:85`.
Why it matters: CodeGraphContext made the core data surface visible, while direct source reads confirmed the split between eager `DataFrame`, lazy `LazyFrame`, DSL `Expr`, and runtime `PhysicalExpr`. This is a strong pattern for agentic code assist because it tells an agent where to put pure query modeling versus execution behavior.
Reusable code shape:
```rust
#[derive(Clone)]
pub struct DataFrame {
    height: usize,
    columns: Vec<Column>,
    cached_schema: OnceLock<SchemaRef>,
}

#[derive(Clone, Default)]
#[must_use]
pub struct LazyFrame {
    pub logical_plan: DslPlan,
    pub(crate) opt_state: OptFlags,
    pub(crate) cached_arena: Arc<Mutex<Option<CachedArena>>>,
}
```
Transfer rule: Use the eager/lazy/physical split when a Rust backend needs a stable user-facing object, a rewriteable logical plan, and a late-bound execution trait. Avoid merging these layers just because one agent prompt can generate all of them.
Verification hook: Re-run `cgc stats` and `cgc find name DataFrame` against the Polars output directory, then re-open `/Users/amuldotexe/Desktop/oss-read-only/polars/crates/polars-core/src/frame/dataframe.rs:85`, `/Users/amuldotexe/Desktop/oss-read-only/polars/crates/polars-lazy/src/frame/mod.rs:70`, `/Users/amuldotexe/Desktop/oss-read-only/polars/crates/polars-plan/src/dsl/expr/mod.rs:98`, and `/Users/amuldotexe/Desktop/oss-read-only/polars/crates/polars-expr/src/expressions/mod.rs:691`.
