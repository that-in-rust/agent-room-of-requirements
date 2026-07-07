# Idiomatic Code Patterns Part 2

Purpose: encyclopedia-grade extraction of idiomatic production-code patterns from Desktop repositories.

Assigned repo slice: `idiomatic-code-patterns-2-repos.txt`

Coverage status: initial scaffold created; extraction in progress.

## Extraction Protocol

- Capture repository evidence, not generic advice.
- Prefer exact file paths and concise snippets when they teach a reusable shape.
- Explain transferable principles across languages and stacks.
- Include when to use, when not to use, risks, and agent-generation guidance.
- Keep concepts deduplicated inside this part; cross-reference adjacent parts when needed.

## Repo Slice

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
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ElBruno.ModelContextProtocol`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolBench`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/benchmarking-tool-retrieval`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/graph-tool-call`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/semantic-router`
- `/Users/amuldotexe/Desktop/personal-repos-lane/backlog-experiments`
- `/Users/amuldotexe/Desktop/personal-repos-lane/confido-exploration-01/git-ref-repo/repos-to-be-ignored/confido-exploration-01`
- `/Users/amuldotexe/Desktop/personal-repos-lane/ebooks2024`
- `/Users/amuldotexe/Desktop/personal-repos-lane/floo-network-message-queue-visual-lab`
- `/Users/amuldotexe/Desktop/personal-repos-lane/iiwii01`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/gds-agent-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-docs-bolt-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-java-driver-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-testkit-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-ballista-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-iggy-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/arcadedb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-comet-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/eclipse-rdf4j-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graph-csr-openmp-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphscope-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/indradb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/lagraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_driver-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ligra-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ndarray-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/orientdb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/rustworkx-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/surrealdb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tikv-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/low-drama-insights`
- `/Users/amuldotexe/Desktop/personal-repos-lane/neo4j`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AKrichevski__Lodebrook`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aider-AI__aider`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-properties`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Artemarius__Engram`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__sem`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Bpolat0__atlasmemory`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CNCSMonster__show-tree-sitter-ast`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditLanguages`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Cranot__roam-code`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-math`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/EdgarOrtegaRamirez__codemetrics`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/FaizaanAlFaisal__code-search`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Freakboy__sd`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GrayJack__tree-sitter-janet`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/HiPhish__rainbow-delimiters.nvim`
- ... 122 additional repos in slice file.

## Patterns

Graph evidence status for this batch:
- `/Users/amuldotexe/Desktop/oss-read-only/wry`: codebase-memory smoke/index succeeded at `/tmp/codex-code-intel/codebase-memory/wry-20260706-224602`; graph candidates were confirmed against source files.
- `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs`: codebase-memory smoke/index succeeded at `/tmp/codex-code-intel/codebase-memory/arrow-rs-20260706-224918`; graph candidates were confirmed against source files.
- Other repos in this first pass were inspected with `rg --files`, `rg`, and direct source reads; graph indexing remains an unresolved follow-up for those repos.

### Checked Constructor Paired With Unsafe Fast Path
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs`, `arrow-array/src/record_batch.rs`, `arrow-array/src/array/byte_array.rs`
- Language / framework / stack: Rust, Apache Arrow columnar arrays
- Evidence snippet:
```rust
pub fn try_new(schema: SchemaRef, columns: Vec<ArrayRef>) -> Result<Self, ArrowError> {
    let options = RecordBatchOptions::new();
    Self::try_new_impl(schema, columns, &options)
}

pub unsafe fn new_unchecked(
    schema: SchemaRef,
    columns: Vec<Arc<dyn Array>>,
    row_count: usize,
) -> Self { ... }
```
- Why it matters: The public API makes invariants cheap to check at boundaries, while performance-critical internals can skip repeated validation with an explicit `unsafe` contract.
- When to use: Use when a data structure has expensive but crisp invariants such as matching schemas, lengths, offsets, or buffer validity.
- When not to use: Avoid if the unchecked path cannot be documented in simple preconditions or if downstream misuse can corrupt user data.
- Transferable principle: Pair every unsafe or unchecked constructor with a checked constructor that describes and enforces the same invariants.
- Related patterns: Sealed Representation Trait; Push Builder With Validity Mask; Typed Domain Error Enum.
- Risks / caveats: Agent-generated code must not call `new_unchecked` just to silence compiler errors; require a nearby proof that `try_new` would pass.
- Agentic coding guidance: Generate the safe constructor first, add tests for invalid shape combinations, and only introduce the unchecked path after profiling shows validation is duplicated.

### Sealed Representation Trait
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs`, `arrow-buffer/src/native.rs`
- Language / framework / stack: Rust, Arrow buffer memory model
- Evidence snippet:
```rust
mod private {
    pub trait Sealed {}
}

pub trait ArrowNativeType:
    std::fmt::Debug + Send + Sync + Copy + PartialOrd + Default + private::Sealed + 'static
{
    fn from_usize(_: usize) -> Option<Self>;
    fn to_usize(self) -> Option<usize>;
}
```
- Why it matters: The trait encodes a memory-layout promise and prevents external crates from implementing it for unsound types.
- When to use: Use for traits that carry safety, layout, serialization, or protocol guarantees beyond ordinary behavior.
- When not to use: Avoid sealing extension-point traits where third-party implementers are the point of the API.
- Transferable principle: If a trait is a proof of representation safety, keep its implementation set closed.
- Related patterns: Checked Constructor Paired With Unsafe Fast Path; Cache-Aligned Buffer Wrapper.
- Risks / caveats: Sealing reduces ecosystem flexibility and should be explicit in docs.
- Agentic coding guidance: When proposing a trait around `unsafe`, FFI, binary encoding, or zero-copy casts, ask whether external implementation would be sound; if not, seal it.

### Push Builder With Validity Mask
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs`, `arrow-array/src/builder/boolean_builder.rs`, `arrow-array/src/builder/mod.rs`
- Language / framework / stack: Rust, Arrow array builders
- Evidence snippet:
```rust
pub struct BooleanBuilder {
    values_builder: BooleanBufferBuilder,
    null_buffer_builder: NullBufferBuilder,
}

pub fn append_value(&mut self, v: bool) {
    self.values_builder.append(v);
    self.null_buffer_builder.append_non_null();
}

pub fn append_null(&mut self) {
    self.null_buffer_builder.append_null();
    self.values_builder.advance(1);
}
```
- Why it matters: Values and validity advance together, so null handling remains a structural property rather than scattered conditional logic.
- When to use: Use for columnar data, vectorized execution, sparse values, or stream builders that need stable row positions.
- When not to use: Avoid for small scalar collections where `Vec<Option<T>>` is simpler and performance does not matter.
- Transferable principle: Model missingness as a parallel validity channel when positional alignment is essential.
- Related patterns: Checked Constructor Paired With Unsafe Fast Path; Physical Representation Dispatch.
- Risks / caveats: Builders must keep value length and null-mask length synchronized after every append path.
- Agentic coding guidance: When generating builder APIs, add tests for `append_value`, `append_null`, `append_slice`, and `finish` length/null-count invariants.

### Cache-Aligned Buffer Wrapper
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/arrow-rs`, `arrow-buffer/src/buffer/mutable.rs`
- Language / framework / stack: Rust, Arrow memory buffers
- Evidence snippet:
```rust
pub struct MutableBuffer {
    data: NonNull<u8>,
    len: usize,
    layout: Layout,
}

pub fn with_capacity(capacity: usize) -> Self {
    let capacity = bit_util::round_upto_multiple_of_64(capacity);
    let layout = Layout::from_size_align(capacity, ALIGNMENT)
        .expect("failed to create layout for MutableBuffer");
    ...
}
```
- Why it matters: A tiny wrapper centralizes alignment, capacity rounding, allocation, and ownership invariants.
- When to use: Use when raw allocation details are repeated or need a consistent hardware/protocol alignment guarantee.
- When not to use: Avoid for ordinary typed collections where `Vec<T>` already provides the needed semantics.
- Transferable principle: Hide unsafe allocation mechanics behind a narrow type that owns its invariants.
- Related patterns: Sealed Representation Trait; Checked Constructor Paired With Unsafe Fast Path.
- Risks / caveats: Manual memory wrappers need careful drop, clone, and conversion semantics.
- Agentic coding guidance: Prefer existing buffer abstractions; if adding one, keep the public API small and test zero-capacity, large-capacity, and conversion cases.

### Fluent Builder With Deferred Validation
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/wry`, `src/lib.rs`
- Language / framework / stack: Rust, Tauri/Wry WebView builder
- Evidence snippet:
```rust
pub struct WebViewBuilder<'a> {
  attrs: WebViewAttributes<'a>,
  platform_specific: PlatformSpecificWebViewAttributes,
  error: crate::Result<()>,
}

pub fn with_custom_protocol<F>(mut self, name: String, handler: F) -> Self {
  if self.attrs.custom_protocols.contains_key(&name) {
    self.error = self.error.and(Err(crate::Error::DuplicateCustomProtocol(name)));
    return self;
  }
  self.attrs.custom_protocols.insert(name, Box::new(handler));
  self
}

pub fn build<W: HasWindowHandle>(self, window: &'a W) -> Result<WebView> {
  self.error?;
  InnerWebView::new(window, self.attrs, self.platform_specific).map(|webview| WebView { webview })
}
```
- Why it matters: The builder preserves method chaining while still returning a `Result` at the boundary where the platform object is created.
- When to use: Use when many optional settings should compose fluently but some settings can conflict before final construction.
- When not to use: Avoid when immediate validation feedback is necessary for interactive configuration flows.
- Transferable principle: Accumulate configuration immutably, accumulate errors explicitly, and fail once at the build boundary.
- Related patterns: Cfg-Gated Platform Error Surface; Platform Workaround Module.
- Risks / caveats: Deferred errors can hide the source call site unless variants contain enough context.
- Agentic coding guidance: When adding builder methods, update the central attribute struct, default implementation, setter, and build-time validation together.

### Platform Workaround Module
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/wry`, `src/custom_protocol_workaround.rs`, `examples/streaming.rs`
- Language / framework / stack: Rust, desktop/mobile WebView protocols
- Evidence snippet:
```rust
pub fn apply_uri_work_around(uri: &str, http_or_https: &str, protocol: &str) -> String {
  uri.replace(
    &original_uri_prefix(protocol),
    &work_around_uri_prefix(http_or_https, protocol),
  )
}

pub fn revert_uri_work_around(uri: &str, http_or_https: &str, protocol: &str) -> String {
  uri.replace(
    &work_around_uri_prefix(http_or_https, protocol),
    &original_uri_prefix(protocol),
  )
}
```
- Why it matters: Non-portable URL rewriting is isolated in pure functions with a focused test, instead of leaking across every protocol handler.
- When to use: Use when an OS, browser, database, or vendor API needs a compatibility transform.
- When not to use: Avoid if the workaround changes security semantics and cannot be audited independently.
- Transferable principle: Make portability shims small, reversible, and testable.
- Related patterns: Fluent Builder With Deferred Validation; Cfg-Gated Platform Error Surface.
- Risks / caveats: URI replacement can be too broad if prefixes are not constrained and tested.
- Agentic coding guidance: Put workaround code in a named module, write round-trip tests, and keep platform-specific comments near the transform.

### Cfg-Gated Platform Error Surface
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/wry`, `src/error.rs`
- Language / framework / stack: Rust, cross-platform desktop/mobile library
- Evidence snippet:
```rust
#[non_exhaustive]
#[derive(thiserror::Error, Debug)]
pub enum Error {
  #[cfg(gtk)]
  #[error(transparent)]
  GlibError(#[from] gtk::glib::Error),
  #[cfg(target_os = "windows")]
  #[error("WebView2 error: {0}")]
  WebView2Error(webview2_com::Error),
  #[error("Duplicate custom protocol '{0}' registered on the WebViewBuilder")]
  DuplicateCustomProtocol(String),
}
```
- Why it matters: The public error type exposes only variants relevant to the compiled target while leaving room for future variants.
- When to use: Use in cross-platform crates or libraries with optional features.
- When not to use: Avoid if consumers need exhaustive matching across all variants as part of a stable protocol.
- Transferable principle: Make platform variability explicit in the type system instead of burying it in strings.
- Related patterns: Platform Workaround Module; Typed Domain Error Enum.
- Risks / caveats: Feature-gated variants need docs and tests per target or they rot quietly.
- Agentic coding guidance: When adding platform-specific code, add a cfg-gated error variant and conversion only under the same cfg condition.

### Typed Error Macros With Debug Strategy
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/polars`, `crates/polars-error/src/lib.rs`
- Language / framework / stack: Rust, Polars error handling
- Evidence snippet:
```rust
static ERROR_STRATEGY: LazyLock<ErrorStrategy> = LazyLock::new(|| {
    if env::var("POLARS_PANIC_ON_ERR").as_deref() == Ok("1") {
        ErrorStrategy::Panic
    } else if env::var("POLARS_BACKTRACE_IN_ERR").as_deref() == Ok("1") {
        ErrorStrategy::WithBacktrace
    } else {
        ErrorStrategy::Normal
    }
});

macro_rules! polars_ensure {
    ($cond:expr, $($tt:tt)+) => {
        if !$cond { $crate::polars_bail!($($tt)+); }
    };
}
```
- Why it matters: Call sites stay terse while error classes, backtraces, and panic-on-error debugging remain centralized.
- When to use: Use in libraries with many invariant checks and domain-specific error categories.
- When not to use: Avoid macro error layers if ordinary `Result` constructors are already clear and rare.
- Transferable principle: Standardize error construction at the boundary between domain checks and user-visible diagnostics.
- Related patterns: Cfg-Gated Platform Error Surface; Checked Constructor Paired With Unsafe Fast Path.
- Risks / caveats: Macros can obscure control flow and make IDE navigation weaker.
- Agentic coding guidance: Prefer existing project macros for validation and do not invent new error helpers unless repeated call sites justify them.

### Python Lazy Facade Over Rust Plan
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/polars`, `py-polars/src/polars/lazyframe/frame.py`
- Language / framework / stack: Python facade, Rust execution engine
- Evidence snippet:
```python
class LazyFrame:
    _ldf: PyLazyFrame

    @classmethod
    def _from_pyldf(cls, ldf: PyLazyFrame) -> LazyFrame:
        self = cls.__new__(cls)
        self._ldf = ldf
        return self

    def select(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> LazyFrame:
        pyexprs = parse_into_list_of_expressions(*exprs, **named_exprs)
        return self._from_pyldf(self._ldf.select(pyexprs))
```
- Why it matters: Python exposes an ergonomic immutable API while delegating query planning and execution to a compiled core.
- When to use: Use when Python is the product API but performance or memory semantics belong in Rust/C++/native code.
- When not to use: Avoid if the wrapper adds substantial behavior divergence from the core engine.
- Transferable principle: Keep language bindings thin: normalize inputs, call the core, wrap the returned core handle.
- Related patterns: Cached Arena IR; Host-Language Error Bridge; Typed Context Keys.
- Risks / caveats: Wrapper and core APIs can drift; overloads and deprecation adapters need tests.
- Agentic coding guidance: When editing wrapper methods, inspect both the Python facade and native method name; preserve `_from_pyldf` wrapping style.

### Cached Arena IR For Repeated Planning
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/polars`, `crates/polars-lazy/src/frame/cached_arenas.rs`, `crates/polars-lazy/src/frame/mod.rs`
- Language / framework / stack: Rust, Polars lazy query optimizer
- Evidence snippet:
```rust
pub(crate) struct CachedArena {
    lp_arena: Arena<IR>,
    expr_arena: Arena<AExpr>,
}

pub fn collect_schema(&mut self) -> PolarsResult<SchemaRef> {
    let mut cached_arenas = self.cached_arena.lock().unwrap();
    match &mut *cached_arenas {
        None => { ... *cached_arenas = Some(CachedArena { lp_arena, expr_arena }); ... }
        Some(arenas) => { ... }
    }
}
```
- Why it matters: Logical-plan conversion is expensive, so schema and optimization calls reuse arena-backed IR where possible.
- When to use: Use when a graph/tree representation is repeatedly derived from a stable high-level DSL.
- When not to use: Avoid caching mutable IR if invalidation is unclear or stale versions can affect correctness.
- Transferable principle: Cache compiled intermediate representations behind a versioned or locked boundary.
- Related patterns: Python Lazy Facade Over Rust Plan; Physical Representation Dispatch.
- Risks / caveats: Locks and cloned arenas can become contention or memory-growth points.
- Agentic coding guidance: When adding plan transforms, ensure cache invalidation/version behavior is understood before mutating stored IR.

### Physical Representation Dispatch
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/polars`, `crates/polars-ops/src/frame/join/mod.rs`, `crates/polars-ops/src/frame/join/asof/mod.rs`
- Language / framework / stack: Rust, Polars join kernels
- Evidence snippet:
```rust
let keys = s
    .iter()
    .map(|s| {
        let phys = s.to_physical_repr();
        match phys.dtype() {
            DataType::Float32 => phys.f32().unwrap().to_canonical().into_column(),
            DataType::Float64 => phys.f64().unwrap().to_canonical().into_column(),
            _ => phys.into_owned().into_column(),
        }
    })
    .collect::<Vec<_>>();
```
- Why it matters: Logical dtypes are normalized before generic kernels run, making joins compare canonical physical values.
- When to use: Use in data engines where many logical types share a smaller set of execution representations.
- When not to use: Avoid if logical semantics cannot survive physical normalization.
- Transferable principle: Normalize once at the kernel boundary, then keep the hot path type-specific and simple.
- Related patterns: Sealed Representation Trait; Push Builder With Validity Mask; Cached Arena IR.
- Risks / caveats: `unwrap()` in dtype branches is acceptable only if the branch proves the downcast.
- Agentic coding guidance: Match on dtype first, downcast immediately inside the proven branch, and add feature-gated arms near related dtypes.

### Sentinel Enum For Unspecified Defaults
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/pandas`, `pandas/_libs/lib.pyi`, `pandas/core/indexes/base.py`
- Language / framework / stack: Python, pandas API compatibility
- Evidence snippet:
```python
class _NoDefault(Enum):
    no_default = ...

no_default: Final = _NoDefault.no_default
NoDefault: TypeAlias = Literal[_NoDefault.no_default]
```
```python
if allow_fill is no_default:
    if fill_value is None:
        warnings.warn(..., Pandas4Warning, stacklevel=find_stack_level())
        allow_fill = False
    else:
        allow_fill = fill_value is not no_default
```
- Why it matters: The API can distinguish "argument omitted" from "argument explicitly passed as None" during long deprecation windows.
- When to use: Use when `None` is a valid user value but omission has separate semantics.
- When not to use: Avoid for new APIs where keyword-only parameters and explicit enums can be cleaner.
- Transferable principle: Represent omission with an identity-stable sentinel, not with a value from the domain.
- Related patterns: API Evolution Decorator; Extension Protocol Hooks.
- Risks / caveats: Sentinels leak into downstream helpers unless translated before generic algorithms.
- Agentic coding guidance: Use `is no_default` identity checks, not equality checks, and convert the sentinel before calling lower-level code that does not understand it.

### API Evolution Decorator
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/pandas`, `pandas/util/_decorators.py`
- Language / framework / stack: Python, mature public API maintenance
- Evidence snippet:
```python
def deprecate_nonkeyword_arguments(
    klass: type[PandasChangeWarning],
    allowed_args: list[str] | None = None,
    name: str | None = None,
) -> Callable[[F], F]:
    ...
    new_sig = old_sig.replace(parameters=new_params)
    ...
    wrapper.__signature__ = new_sig
```
- Why it matters: The decorator changes runtime warnings and introspection signatures together, reducing migration ambiguity.
- When to use: Use in libraries that must move APIs gradually without breaking existing users immediately.
- When not to use: Avoid for application-internal functions where direct signature changes are cheaper.
- Transferable principle: API migration tools should update behavior, warnings, docs, and introspection in one place.
- Related patterns: Sentinel Enum For Unspecified Defaults; Descriptor-Based Accessor Registration.
- Risks / caveats: Decorators can stack poorly and hide true call signatures if not tested.
- Agentic coding guidance: Before changing a public signature, search for existing deprecation decorators and mirror the project pattern.

### Descriptor-Based Accessor Registration
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/pandas`, `pandas/core/accessor.py`
- Language / framework / stack: Python descriptors, pandas extension API
- Evidence snippet:
```python
class Accessor:
    def __get__(self, obj, cls):
        if obj is None:
            return self._accessor
        return self._accessor(obj)

def _register_accessor(name: str, cls: type[NDFrame | Index]) -> Callable[[TypeT], TypeT]:
    def decorator(accessor: TypeT) -> TypeT:
        setattr(cls, name, Accessor(name, accessor))
        cls._accessors.add(name)
        return accessor
    return decorator
```
- Why it matters: Third-party namespaces such as `df.geo` can be added without subclassing core frame types.
- When to use: Use when a central object needs optional domain-specific namespaces.
- When not to use: Avoid when extension names are untrusted or likely to collide with core attributes.
- Transferable principle: Use descriptors to attach lazy, namespaced behavior to stable host classes.
- Related patterns: Extension Protocol Hooks; API Evolution Decorator.
- Risks / caveats: Accessor collisions are runtime warnings, not compile-time errors.
- Agentic coding guidance: Register accessors through the public decorator and make the accessor `__init__` validate host compatibility.

### Extension Protocol Hooks
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/pandas`, `pandas/core/arrays/base.py`
- Language / framework / stack: Python, pandas ExtensionArray API
- Evidence snippet:
```python
@set_module("pandas.api.extensions")
class ExtensionArray:
    @classmethod
    def _from_sequence(cls, scalars, *, dtype: Dtype | None = None, copy: bool = False) -> Self:
        raise AbstractMethodError(cls)

    @classmethod
    def _from_factorized(cls, values, original):
        raise AbstractMethodError(cls)
```
- Why it matters: Pandas defines a narrow protocol for third-party column types while leaving storage details to implementations.
- When to use: Use when many external implementations need to plug into a common algorithm surface.
- When not to use: Avoid if the extension surface is not stable enough to document and test.
- Transferable principle: Separate required construction/reconstruction hooks from optional optimization hooks.
- Related patterns: Descriptor-Based Accessor Registration; Sentinel Enum For Unspecified Defaults.
- Risks / caveats: Broad protocols become maintenance commitments; abstract hooks need thorough docs.
- Agentic coding guidance: When implementing an extension type, satisfy required hooks first, then add optimized methods only after correctness tests pass.

### Command Run-Validate Boundary
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/superset`, `superset/commands/base.py`, `superset/commands/tag/create.py`
- Language / framework / stack: Python, Flask/Superset service layer
- Evidence snippet:
```python
class BaseCommand(ABC):
    @abstractmethod
    def run(self) -> Any: ...

    @abstractmethod
    def validate(self) -> None: ...

class CreateCustomTagCommand(CreateMixin, BaseCommand):
    @transaction(on_error=partial(on_error, reraise=TagCreateFailedError))
    def run(self) -> None:
        self.validate()
        TagDAO.create_custom_tagged_objects(...)
```
- Why it matters: Mutation workflows are explicit objects with validation, transaction handling, and typed exceptions instead of ad hoc controller code.
- When to use: Use for service actions that combine validation, authorization-sensitive state changes, and persistence.
- When not to use: Avoid for trivial CRUD pass-throughs where a command adds ceremony without isolation.
- Transferable principle: Put business actions behind command objects; keep transport handlers thin.
- Related patterns: Generic DAO With Model Inference; Layered REST Decorator Stack.
- Risks / caveats: Command sprawl can occur if every tiny helper becomes a class.
- Agentic coding guidance: For new Superset-like actions, create a command with `validate()` and `run()`, then call DAOs from `run()` under the project transaction decorator.

### Generic DAO With Model Inference
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/superset`, `superset/daos/base.py`
- Language / framework / stack: Python, SQLAlchemy, generic DAO layer
- Evidence snippet:
```python
class BaseDAO(CoreBaseDAO[T], Generic[T]):
    model_cls: ClassVar[type[Any] | None] = None

    def __init_subclass__(cls) -> None:
        cls.model_cls = get_args(cls.__orig_bases__[0])[0]

    @classmethod
    def create(cls, item: T | None = None, attributes: dict[str, Any] | None = None) -> T:
        if not item:
            item = cls.model_cls()
        ...
        db.session.add(item)
        return item
```
- Why it matters: Child DAOs get typed CRUD behavior by declaring their model type, reducing repeated SQLAlchemy boilerplate.
- When to use: Use when many model-specific DAOs share identical persistence mechanics.
- When not to use: Avoid if model operations have divergent consistency, authorization, or transaction requirements.
- Transferable principle: Put uniform persistence mechanics in a generic base and domain-specific queries in child DAOs.
- Related patterns: Command Run-Validate Boundary; Layered REST Decorator Stack.
- Risks / caveats: `__orig_bases__` introspection is clever and can break under unusual inheritance.
- Agentic coding guidance: Follow existing DAO inheritance style; do not duplicate CRUD methods in child classes unless behavior truly differs.

### Layered REST Decorator Stack
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/superset`, `superset/databases/api.py`, `superset/datasets/api.py`
- Language / framework / stack: Python, Flask-AppBuilder REST APIs
- Evidence snippet:
```python
@expose("/", methods=("POST",))
@protect()
@statsd_metrics
@event_logger.log_this_with_context(
    action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.post",
    log_to_statsd=False,
)
@requires_json
def post(self) -> FlaskResponse:
    ...
```
- Why it matters: Routing, authorization, metrics, event logging, and request-shape validation are declared at the endpoint boundary.
- When to use: Use in service APIs where every route needs a predictable envelope of cross-cutting behavior.
- When not to use: Avoid if decorator order is unclear or if hidden side effects make request flow hard to debug.
- Transferable principle: Compose cross-cutting endpoint concerns declaratively and consistently.
- Related patterns: Command Run-Validate Boundary; Generic DAO With Model Inference.
- Risks / caveats: Decorator order is behavior; changing order can alter auth, logging, or validation.
- Agentic coding guidance: Copy decorator order from nearby endpoints with the same method type, then change only the command/schema pieces.

### Configurable Feature Flag Manager
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/superset`, `superset/utils/feature_flag_manager.py`
- Language / framework / stack: Python, Flask configuration
- Evidence snippet:
```python
def init_app(self, app: Flask) -> None:
    self._get_feature_flags_func = app.config["GET_FEATURE_FLAGS_FUNC"]
    self._is_feature_enabled_func = app.config["IS_FEATURE_ENABLED_FUNC"]
    self._feature_flags = app.config["DEFAULT_FEATURE_FLAGS"]
    self._feature_flags.update(app.config["FEATURE_FLAGS"])

def is_feature_enabled(self, feature: str) -> bool:
    if self._is_feature_enabled_func:
        return self._is_feature_enabled_func(feature, self._feature_flags[feature])
    ...
```
- Why it matters: Static defaults, deployment overrides, and custom evaluation logic are all supported behind one call site.
- When to use: Use when product behavior must vary by deployment, tenant, environment, or rollout.
- When not to use: Avoid using feature flags as permanent architecture branches without ownership and cleanup.
- Transferable principle: Centralize feature checks and allow host applications to override evaluation.
- Related patterns: Layered REST Decorator Stack; Command Run-Validate Boundary.
- Risks / caveats: Missing feature keys can become silent false negatives.
- Agentic coding guidance: When adding a flag, add the default, use the manager helper, and avoid direct config dict reads in business logic.

### Dataclass Content With Auto-Registered Plugin Base
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/superset`, `superset/reports/notifications/base.py`
- Language / framework / stack: Python dataclasses, plugin registry
- Evidence snippet:
```python
@dataclass
class NotificationContent:
    name: str
    header_data: HeaderDataType
    csv: Optional[bytes] = None
    pdf: Optional[bytes] = None

class BaseNotification:
    plugins: list[type["BaseNotification"]] = []
    type: Optional[ReportRecipientType] = None

    def __init_subclass__(cls, *args: Any, **kwargs: Any) -> None:
        super().__init_subclass__(*args, **kwargs)
        cls.plugins.append(cls)
```
- Why it matters: Payload shape is explicit and implementations self-register when imported.
- When to use: Use for a small closed-ish family of plugins selected by a type field.
- When not to use: Avoid auto-registration if import order is uncertain or plugins come from untrusted packages.
- Transferable principle: Use dataclasses for message payloads and `__init_subclass__` for lightweight internal plugin catalogs.
- Related patterns: Configurable Feature Flag Manager; Command Run-Validate Boundary.
- Risks / caveats: Global plugin lists can include duplicates in reload-heavy environments.
- Agentic coding guidance: Keep plugin constructors uniform and test that each subclass sets its selector field.

### Typed Context Keys With Memoized Pipeline Functions
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/cocoindex`, `examples/text_embedding_qdrant/main.py`
- Language / framework / stack: Python async data pipeline, CocoIndex, Qdrant
- Evidence snippet:
```python
QDRANT_DB = coco.ContextKey[QdrantClient]("text_embedding_qdrant")
EMBEDDER = coco.ContextKey[SentenceTransformerEmbedder]("embedder", detect_change=True)

@coco.lifespan
async def coco_lifespan(builder: coco.EnvironmentBuilder) -> AsyncIterator[None]:
    builder.provide(QDRANT_DB, qdrant.create_client(QDRANT_URL, prefer_grpc=True))
    builder.provide(EMBEDDER, SentenceTransformerEmbedder(EMBED_MODEL))
    yield

@coco.fn(memo=True)
async def process_file(file: FileLike, target: qdrant.CollectionTarget) -> None:
    ...
```
- Why it matters: Runtime resources are named, typed, and change-tracked, while expensive file transforms can be memoized declaratively.
- When to use: Use in dataflow systems where functions depend on runtime resources such as clients, models, or pools.
- When not to use: Avoid if hidden context makes function dependencies harder to test than explicit parameters.
- Transferable principle: Model long-lived resources as typed context keys and make change detection explicit.
- Related patterns: Python Lazy Facade Over Rust Plan; Host-Language Error Bridge.
- Risks / caveats: Context keys are global-ish; names and change-detection policy must be stable.
- Agentic coding guidance: Define context keys near app constants, provide them in lifespan setup, and mark model/config resources with `detect_change=True` when outputs depend on them.

### Host-Language Error Bridge
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/cocoindex`, `rust/py_utils/src/error.rs`
- Language / framework / stack: Rust, PyO3, Python interop
- Evidence snippet:
```rust
pub trait FromPyResult<T> {
    fn from_py_result(self) -> CResult<T>;
}

impl<T> FromPyResult<T> for PyResult<T> {
    fn from_py_result(self) -> CResult<T> {
        self.map_err(|err| CError::host(HostedPyErr(err)))
    }
}

impl<T> IntoPyResult<T> for CResult<T> {
    fn into_py_result(self) -> PyResult<T> {
        self.map_err(cerror_to_pyerr)
    }
}
```
- Why it matters: Python exceptions can cross into Rust as hosted errors and cross back as Python exceptions without losing cancellation semantics.
- When to use: Use at FFI or embedding boundaries where both languages have meaningful error taxonomies.
- When not to use: Avoid if one side only needs stringified diagnostics and no structured handling.
- Transferable principle: Build explicit bidirectional error adapters at language boundaries.
- Related patterns: Asyncio Future Bridge With Cancellation; Python Lazy Facade Over Rust Plan.
- Risks / caveats: Error conversion must preserve cancellation/interruption signals, not wrap them as generic runtime failures.
- Agentic coding guidance: When adding new cross-language calls, convert at the boundary using existing traits rather than mapping errors ad hoc.

### Asyncio Future Bridge With Cancellation
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/cocoindex`, `rust/py_utils/src/future.rs`
- Language / framework / stack: Rust, PyO3, asyncio, futures
- Evidence snippet:
```rust
impl Drop for CancelOnDropPy {
    fn drop(&mut self) {
        if self.done.load(Ordering::SeqCst) { return; }
        let task = self.task_ref.lock().unwrap().take();
        if let Some(task) = task {
            Python::attach(|py| {
                self.event_loop.bind(py).call_method(
                    "call_soon_threadsafe",
                    (task.bind(py).getattr("cancel")?,),
                    Some(&kwargs),
                )?;
                Ok(())
            });
        }
    }
}
```
- Why it matters: Dropping the Rust future cancels the Python task on the owning event loop thread instead of leaking work.
- When to use: Use when bridging async runtimes with different cancellation and thread-affinity rules.
- When not to use: Avoid hand-rolled bridges if a maintained runtime adapter already covers lifecycle and cancellation semantics.
- Transferable principle: Cross-runtime futures need cancellation, result forwarding, and event-loop affinity as first-class design points.
- Related patterns: Host-Language Error Bridge; Typed Context Keys With Memoized Pipeline Functions.
- Risks / caveats: Incorrect cancellation can deadlock, leak tasks, or raise debug-mode runtime errors.
- Agentic coding guidance: Preserve the project's bridge utilities; do not call Python event-loop methods directly from arbitrary Rust threads.

Additional evidence status: the second pass used the evidence index to prioritize `feldera`, `apache-iggy-src`, `redb-src`, `rust-lang__rust-analyzer`, and `openai__codex`. A `codebase-memory` smoke attempt on `redb-src` failed before indexing with a locale panic (`LC_CTYPE` / `C.UTF-8`), so the redb entries below are based on direct source reads only. For Knight Bus `gitrefrepo` references, direct source reads were preferred over broad graph indexing.

### Source-Copied Adapter With Upstream Provenance
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/feldera`, `crates/adapters/src/format/csv/deserializer.rs`
- Language / framework / stack: Rust, Serde, CSV adapters
- Evidence snippet:
```rust
//! This is a copy of the deserialization code from the `csv` crate...
//! It is modified to expose the `Deserializer` implementation...
#![allow(clippy::manual_strip)]
#![allow(clippy::map_clone)]
```
- Why it matters: The forked implementation is explicitly justified, attributed, licensed, and kept close to upstream by suppressing inherited style warnings rather than rewriting it heavily.
- When to use: Use when a dependency has the needed behavior internally but does not expose the extension point and a full fork would be heavier.
- When not to use: Avoid when the upstream API can be extended, when security updates are frequent, or when the copied code is too large to audit.
- Transferable principle: If copying upstream code is the least bad option, preserve provenance and isolate local changes.
- Related patterns: Trait-Erased Record Variant Deserializer; Platform Workaround Module.
- Risks / caveats: Copied code can drift from upstream bug fixes; license compatibility and update tracking become ongoing responsibilities.
- Agentic coding guidance: Do not casually reformat copied upstream blocks. Keep local deltas minimal and document why the copy exists.

### Trait-Erased Record Variant Deserializer
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/feldera`, `crates/adapters/src/format/csv/deserializer.rs`
- Language / framework / stack: Rust, Serde deserialization
- Evidence snippet:
```rust
trait DeRecord<'r> {
    fn next_field(&mut self) -> Result<&'r str, DeserializeError>;
    fn next_field_bytes(&mut self) -> Result<&'r [u8], DeserializeError>;
    fn infer_deserialize<'de, V: Visitor<'de>>(
        &mut self,
        visitor: V,
    ) -> Result<V::Value, DeserializeError>;
}

pub struct DeRecordWrap<T>(T);
pub type StringRecordDeserializer<'r> = DeRecordWrap<DeStringRecord<'r>>;
pub type ByteRecordDeserializer<'r> = DeRecordWrap<DeByteRecord<'r>>;
```
- Why it matters: A single Serde implementation can support string and byte CSV records while preserving UTF-8 guarantees and avoiding repeated validation.
- When to use: Use when two representations share most state-machine logic but differ in field extraction and validation rules.
- When not to use: Avoid if the variants are simple enough that duplication is clearer than a private trait layer.
- Transferable principle: Put representation-specific operations behind a small internal trait and keep the public API as type aliases or constructors.
- Related patterns: Source-Copied Adapter With Upstream Provenance; Physical Representation Dispatch.
- Risks / caveats: Private traits can become opaque quickly if too many behavioral branches accumulate.
- Agentic coding guidance: Keep wrapper traits narrow and back them with tests for each representation, especially around invalid encoding and end-of-row errors.

### HTTP Error Type Implements Response Contract
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/feldera`, `crates/pipeline-manager/src/compiler/error.rs`
- Language / framework / stack: Rust, Actix Web, Serde
- Evidence snippet:
```rust
#[derive(Debug, Serialize)]
#[serde(untagged)]
pub enum CompilerError {
    PrecompilationError { error: String },
}

impl ResponseError for CompilerError {
    fn status_code(&self) -> StatusCode { ... }

    fn error_response(&self) -> HttpResponse<BoxBody> {
        HttpResponseBuilder::new(self.status_code()).json(ErrorResponse::from_error(self))
    }
}
```
- Why it matters: Domain errors carry their own HTTP status and serialized error-body contract, so endpoint handlers can return typed failures without hand-building responses.
- When to use: Use in web services where subsystem errors should map consistently to status codes and JSON diagnostics.
- When not to use: Avoid putting transport concerns into very low-level core libraries that are reused outside HTTP.
- Transferable principle: Convert domain errors into transport responses at the service boundary, with one implementation per error family.
- Related patterns: Typed Error Macros With Debug Strategy; Host-Language Error Bridge.
- Risks / caveats: If every internal error implements HTTP directly, layering can blur.
- Agentic coding guidance: Add new variants with `Display`, `DetailedError`, and `ResponseError` coverage together; do not return ad hoc JSON errors from handlers.

### Transactional Operation Module Contract
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/feldera`, `crates/pipeline-manager/src/db/operations.rs`
- Language / framework / stack: Rust, database operation layer
- Evidence snippet:
```rust
// Every operation is implemented to be part of a transaction.
// These operations are building blocks...
//
// An operation should:
// * Upon success, always result in a consistent database state
// * Otherwise:
//   - An error if the parameterized operation failed...
//   - Panic if the operation is invalid in any database state...
pub mod api_key;
pub mod cluster_monitor;
pub mod pipeline;
```
- Why it matters: The module-level contract distinguishes recoverable state-dependent failures from programmer errors, making transaction semantics explicit before individual functions are read.
- When to use: Use for service data layers where operations are composable but must preserve invariants.
- When not to use: Avoid panics in user-input validation paths or storage layers that need crash-only guarantees.
- Transferable principle: State the consistency and failure contract at the module boundary, not just in scattered function docs.
- Related patterns: Command Run-Validate Boundary; Generic DAO With Model Inference.
- Risks / caveats: The panic/error split must be applied consistently or callers cannot reason about rollback behavior.
- Agentic coding guidance: When adding database operations, classify failure modes first: invalid in current state returns an error; invalid in every state is a programmer bug.

### Stable Numeric Error Enum With Discriminants
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-iggy-src`, `core/common/src/error/iggy_error.rs`
- Language / framework / stack: Rust, thiserror, strum, protocol errors
- Evidence snippet:
```rust
#[derive(Clone, Debug, Error, EnumDiscriminants, IntoStaticStr, FromRepr, Default)]
#[repr(u32)]
#[strum(serialize_all = "snake_case")]
pub enum IggyError {
    #[default]
    #[error("Error")]
    Error = 1,
    #[error("Invalid configuration")]
    InvalidConfiguration = 2,
    #[error("Resource with key: {0} was not found.")]
    ResourceNotFound(String) = 20,
}
```
- Why it matters: Error values double as human messages and stable wire/protocol codes, with generated discriminant utilities for parsing and telemetry.
- When to use: Use in services, SDKs, or protocols where errors cross process or language boundaries.
- When not to use: Avoid fixed discriminants for purely internal errors that change frequently.
- Transferable principle: Treat protocol errors as versioned data, not just Rust enum variants.
- Related patterns: Host-Language Error Bridge; HTTP Error Type Implements Response Contract.
- Risks / caveats: Numeric gaps and backwards compatibility become part of the API surface.
- Agentic coding guidance: Never renumber existing variants; append new codes intentionally and keep display strings stable enough for users.

### Denormalized Permission Index Sets
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-iggy-src`, `core/metadata/src/permissioner/mod.rs`, `core/metadata/src/permissioner/permissioner_rules/streams.rs`
- Language / framework / stack: Rust, authorization, in-memory indexes
- Evidence snippet:
```rust
pub struct Permissioner {
    pub users_permissions: AHashMap<UserId, GlobalPermissions>,
    pub users_streams_permissions: AHashMap<(UserId, usize), StreamPermissions>,
    pub users_that_can_poll_messages_from_all_streams: AHashSet<UserId>,
    pub users_that_can_send_messages_to_specific_streams: AHashSet<(UserId, usize)>,
}

pub fn get_stream(&self, user_id: u32, stream_id: usize) -> Result<(), IggyError> {
    if let Some(global_permissions) = self.users_permissions.get(&user_id)
        && (global_permissions.manage_streams || global_permissions.read_streams)
    {
        return Ok(());
    }
    ...
}
```
- Why it matters: Common authorization questions are pre-indexed into maps and sets, so checks stay simple and fast.
- When to use: Use when permissions are read much more often than updated and checks sit on a hot path.
- When not to use: Avoid if permission updates are frequent enough that duplicated indexes become a consistency burden.
- Transferable principle: Denormalize authorization data around the questions the runtime actually asks.
- Related patterns: Configurable Feature Flag Manager; Transactional Operation Module Contract.
- Risks / caveats: Every update/delete path must maintain all derived sets.
- Agentic coding guidance: When adding a new permission dimension, update initialization, mutation, deletion, and rule-check modules together.

### Strategy Trait With Ordering Tradeoff
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-iggy-src`, `core/sdk/src/clients/producer_sharding.rs`
- Language / framework / stack: Rust, async messaging SDK
- Evidence snippet:
```rust
pub trait Sharding: Send + Sync + std::fmt::Debug + 'static {
    fn pick_shard(&self, num_shards: usize, messages: &[IggyMessage],
        stream: &Identifier, topic: &Identifier) -> usize;
}

pub struct BalancedSharding {
    counter: AtomicUsize,
}

pub struct OrderedSharding;
```
- Why it matters: Routing strategy is pluggable and the built-ins make the throughput-vs-ordering tradeoff visible at the type level.
- When to use: Use when product semantics vary between balanced load and stable ordering.
- When not to use: Avoid if one strategy is mandated by correctness and alternatives would be footguns.
- Transferable principle: Encode operational tradeoffs as named strategy types rather than hidden booleans.
- Related patterns: Physical Representation Dispatch; Feature-Gated Tool Backend Selection.
- Risks / caveats: Custom strategies must be deterministic enough for the ordering guarantees they claim.
- Agentic coding guidance: Name strategies after the guarantee they optimize, and document any semantics they do not preserve.

### Semaphore Permit Attached To Message
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-iggy-src`, `core/sdk/src/clients/producer_sharding.rs`
- Language / framework / stack: Rust, Tokio, producer backpressure
- Evidence snippet:
```rust
pub struct ShardMessageWithPermit {
    pub inner: ShardMessage,
    _bytes_permit: Option<OwnedSemaphorePermit>,
}

impl ShardMessageWithPermit {
    pub fn new(msg: ShardMessage, permit_bytes: OwnedSemaphorePermit) -> Self {
        Self { inner: msg, _bytes_permit: Some(permit_bytes) }
    }
}
```
- Why it matters: Resource accounting travels with the queued work item and releases automatically when the message is dropped.
- When to use: Use for bounded async queues where permits represent bytes, slots, or other scarce capacity.
- When not to use: Avoid if permits must be released before work-item drop or transferred independently.
- Transferable principle: Attach RAII resource permits to the data whose lifetime consumes the resource.
- Related patterns: Asyncio Future Bridge With Cancellation; Push Builder With Validity Mask.
- Risks / caveats: Hidden permit fields can surprise maintainers if queue ownership becomes complex.
- Agentic coding guidance: Preserve the unused-looking permit field; it is a lifetime guard, not dead data.

### Phantom-Typed Table Definition
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redb-src`, `src/db.rs`, `examples/multithread.rs`
- Language / framework / stack: Rust, embedded database API
- Evidence snippet:
```rust
pub struct TableDefinition<'a, K: Key + 'static, V: Value + 'static> {
    name: &'a str,
    _key_type: PhantomData<K>,
    _value_type: PhantomData<V>,
}

pub const fn new(name: &'a str) -> Self {
    assert!(!name.is_empty());
    Self { name, _key_type: PhantomData, _value_type: PhantomData }
}
```
- Why it matters: The table name remains runtime data, while key/value types are carried at compile time so `open_table(TABLE)` enforces typed access.
- When to use: Use for stores, registries, and protocol channels whose identifiers are strings but whose payloads have stable types.
- When not to use: Avoid if table schemas are genuinely dynamic or user-defined at runtime.
- Transferable principle: Use `PhantomData` handles to bind runtime names to compile-time payload contracts.
- Related patterns: Sealed Representation Trait; Checked Constructor Paired With Unsafe Fast Path.
- Risks / caveats: Runtime-created names still need validation and can conflict despite static key/value typing.
- Agentic coding guidance: Prefer `const TABLE: TableDefinition<K, V>` for fixed schema tables and avoid passing raw table names through application code.

### Concurrent Snapshot Read Transactions
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redb-src`, `src/db.rs`, `examples/multithread.rs`
- Language / framework / stack: Rust, embedded database concurrency
- Evidence snippet:
```rust
pub trait ReadableDatabase {
    /// Captures a snapshot of the database...
    /// Read transactions may exist concurrently with writes
    fn begin_read(&self) -> Result<ReadTransaction, TransactionError>;
}

pub fn begin_write(&self) -> Result<WriteTransaction, TransactionError> {
    self.begin_write_with_allocation_policy(AllocationPolicy::Default)
}
```
- Why it matters: The public API communicates isolation semantics directly: many snapshot readers can coexist, but only one writer proceeds at a time.
- When to use: Use for embedded stores and local caches where predictable transaction isolation matters more than hiding concurrency.
- When not to use: Avoid exposing transaction primitives if callers cannot safely choose transaction lifetimes.
- Transferable principle: Make concurrency guarantees visible in method names and docs at the boundary where handles are created.
- Related patterns: Transactional Operation Module Contract; Phantom-Typed Table Definition.
- Risks / caveats: Long-lived readers can retain old state or block cleanup depending on storage internals.
- Agentic coding guidance: Keep read transactions short in examples and tests; do not wrap broad application workflows in one transaction by default.

### FFI Transaction State Machine With Drop Order
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redb-src`, `crates/redb-python/src/transaction.rs`, `crates/redb-python/test/test_transactions.py`
- Language / framework / stack: Rust, PyO3, Python bindings
- Evidence snippet:
```rust
// Field order is load-bearing: `txn` MUST be dropped before `db`.
struct ActiveWrite {
    txn: ::redb::WriteTransaction,
    db: Py<PyDatabase>,
}

enum State {
    Pending(ActiveWrite),
    InWith(ActiveWrite),
    Finalized,
}
```
- Why it matters: Python context-manager behavior is modeled as a Rust state machine, and the field order explicitly prevents a self-deadlock during drop.
- When to use: Use at FFI boundaries where host-language object lifetimes differ from core resource lifetimes.
- When not to use: Avoid relying on field drop order unless the invariant is documented and tested.
- Transferable principle: Treat binding-layer lifetimes as first-class correctness logic, not incidental glue.
- Related patterns: Host-Language Error Bridge; Asyncio Future Bridge With Cancellation.
- Risks / caveats: Mutex poisoning, re-entry, and finalization order are easy to mishandle across FFI.
- Agentic coding guidance: Preserve the `Pending/InWith/Finalized` states and transaction lifetime tests when modifying the Python binding.

### Incremental Database Inputs With Durability
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rust-lang__rust-analyzer`, `crates/base-db/src/lib.rs`
- Language / framework / stack: Rust, Salsa incremental computation, language server internals
- Evidence snippet:
```rust
#[salsa_macros::input(debug)]
pub struct FileText {
    #[returns(ref)]
    pub text: Arc<str>,
    pub file_id: vfs::FileId,
}

#[salsa_macros::db]
pub trait SourceDatabase: salsa::Database {
    fn file_text(&self, file_id: vfs::FileId) -> FileText;
    fn set_file_text_with_durability(
        &mut self,
        file_id: vfs::FileId,
        text: &str,
        durability: Durability,
    );
}
```
- Why it matters: Mutable editor state becomes typed incremental inputs, and durability lets the system distinguish stable library data from frequently changing workspace files.
- When to use: Use in compilers, analyzers, and IDEs where recomputation must be scoped by dependency tracking.
- When not to use: Avoid for simple batch tools where a plain immutable context is easier.
- Transferable principle: Model changing facts as explicit database inputs with invalidation policy attached.
- Related patterns: Cached Arena IR For Repeated Planning; Search Scope Builder Over Semantic Graph.
- Risks / caveats: One over-broad query can destroy incrementality across the graph.
- Agentic coding guidance: When adding queries, think about invalidation blast radius before reaching for global workspace data.

### Search Scope Builder Over Semantic Graph
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rust-lang__rust-analyzer`, `crates/ide-db/src/search.rs`
- Language / framework / stack: Rust, IDE semantic search
- Evidence snippet:
```rust
#[derive(Clone, Debug)]
pub struct SearchScope {
    entries: FxHashMap<EditionedFileId, Option<TextRange>>,
}

fn reverse_dependencies(db: &RootDatabase, of: hir::Crate) -> SearchScope {
    let mut entries = FxHashMap::default();
    for rev_dep in of.transitive_reverse_dependencies(db) {
        ...
        entries.extend(source_root.iter().map(|id| {
            (EditionedFileId::new(db, id, rev_dep.edition(db)), None)
        }));
    }
    SearchScope { entries }
}
```
- Why it matters: Search is constrained by semantic relationships such as crate graph, reverse dependencies, module children, and editioned file IDs rather than raw filesystem globs.
- When to use: Use in tooling where search precision depends on language semantics or dependency direction.
- When not to use: Avoid for plain-text repository search where semantic setup costs more than it saves.
- Transferable principle: Build search scopes from domain graph relationships before scanning text.
- Related patterns: Incremental Database Inputs With Durability; Smart Context Algorithm from the archive instructions.
- Risks / caveats: Scope construction must stay cheap and edition-aware.
- Agentic coding guidance: Prefer existing `SearchScope` builders over ad hoc file collection when implementing refactors, rename, or usage queries.

### Thread-Local Panic Context Guard
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/rust-lang__rust-analyzer`, `crates/stdx/src/panic_context.rs`
- Language / framework / stack: Rust, diagnostics utility
- Evidence snippet:
```rust
#[must_use]
pub struct PanicContext {
    _priv: (),
}

impl Drop for PanicContext {
    fn drop(&mut self) {
        with_ctx(|ctx| assert!(ctx.pop().is_some()));
    }
}

pub fn enter(frame: String) -> PanicContext {
    SET_HOOK.call_once(set_hook);
    with_ctx(|ctx| ctx.push(frame));
    PanicContext { _priv: () }
}
```
- Why it matters: Context frames are pushed and popped with lexical scope, so panic diagnostics can include the nested operation stack without manually unwinding state.
- When to use: Use in complex compilers, analyzers, and background workers where panics need domain context.
- When not to use: Avoid for normal error handling; this is diagnostic context, not control flow.
- Transferable principle: Use RAII guards for scoped diagnostic state, especially when unwinding may skip manual cleanup.
- Related patterns: Semaphore Permit Attached To Message; Platform Workaround Module.
- Risks / caveats: Thread-local context does not automatically cross async task or thread boundaries.
- Agentic coding guidance: Bind the guard to a local variable and keep it in scope for the operation that should appear in panic output.

### Feature-Gated Tool Backend Selection
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/openai__codex`, `codex-rs/tools/src/tool_config.rs`
- Language / framework / stack: Rust, feature flags, CLI/tool runtime
- Evidence snippet:
```rust
pub fn unified_exec_feature_mode_for_features(features: &Features) -> UnifiedExecFeatureMode {
    if !features.enabled(Feature::ShellTool) || !features.enabled(Feature::UnifiedExec) {
        UnifiedExecFeatureMode::Disabled
    } else if features.enabled(Feature::ShellZshFork) {
        if features.enabled(Feature::UnifiedExecZshFork) {
            UnifiedExecFeatureMode::ZshFork
        } else {
            UnifiedExecFeatureMode::Disabled
        }
    } else {
        UnifiedExecFeatureMode::Direct
    }
}
```
- Why it matters: Backend selection is a pure policy function that composes feature gates without silently enabling dependent behavior.
- When to use: Use when runtime behavior depends on multiple rollout flags, enterprise controls, or platform capabilities.
- When not to use: Avoid if a single static configuration field is enough.
- Transferable principle: Centralize feature-gate composition in named functions and return explicit mode enums.
- Related patterns: Configurable Feature Flag Manager; Strategy Trait With Ordering Tradeoff.
- Risks / caveats: Feature interactions need tests because policy regressions can be subtle.
- Agentic coding guidance: Add new feature gates by extending the mode function and its tests, not by sprinkling `features.enabled(...)` checks across call sites.

### Session-Source Aware Agent Policy
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/openai__codex`, `codex-rs/core/src/session/multi_agents.rs`
- Language / framework / stack: Rust, agent orchestration, session policy
- Evidence snippet:
```rust
fn configured_usage_hint_text_for_source<'a>(
    multi_agent_v2: &'a MultiAgentV2Config,
    session_source: &SessionSource,
) -> Option<&'a str> {
    match session_source {
        SessionSource::SubAgent(SubAgentSource::ThreadSpawn { .. }) => {
            multi_agent_v2.subagent_usage_hint_text.as_deref()
        }
        SessionSource::Cli | SessionSource::VSCode | SessionSource::Exec => {
            multi_agent_v2.root_agent_usage_hint_text.as_deref()
        }
        SessionSource::Internal(_) | SessionSource::SubAgent(_) => None,
    }
}
```
- Why it matters: The same agent runtime can apply different policies and hints for root sessions, thread-spawned subagents, and internal work.
- When to use: Use in orchestration systems where caller identity changes how much autonomy or guidance is appropriate.
- When not to use: Avoid if source-specific behavior would make sessions unpredictable for users.
- Transferable principle: Make caller/session source explicit and route policy through it instead of implicit flags.
- Related patterns: Dataclass Content With Auto-Registered Plugin Base; Deferred Tool Search Index Entries.
- Risks / caveats: Policy matrices can become hard to reason about as sources multiply.
- Agentic coding guidance: When adding a new session source, decide whether it inherits root-agent, subagent, or internal behavior deliberately.

### Deferred Tool Search Index Entries
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/openai__codex`, `codex-rs/tools/src/tool_search.rs`
- Language / framework / stack: Rust, tool discovery, Responses API tool specs
- Evidence snippet:
```rust
pub fn from_spec(
    search_text: String,
    spec: ToolSpec,
    source_info: Option<ToolSearchSourceInfo>,
) -> Option<Self> {
    let output = match spec {
        ToolSpec::Function(mut tool) => {
            tool.defer_loading = Some(true);
            tool.output_schema = None;
            LoadableToolSpec::Function(tool)
        }
        ToolSpec::Namespace(mut namespace) => {
            ...
        }
        ToolSpec::ToolSearch { .. } | ToolSpec::ImageGeneration { .. } => return None,
    };
    Some(Self { entry: ToolSearchEntry { search_text, output }, source_info })
}
```
- Why it matters: Search exposes enough metadata for retrieval while deferring full tool loading and dropping output schemas from the search payload.
- When to use: Use when many tools exist but only a few should enter the model context for a given turn.
- When not to use: Avoid for small fixed tool sets where discovery overhead is unnecessary.
- Transferable principle: Separate searchable metadata from loadable executable definitions.
- Related patterns: Progressive Disclosure from the archive instructions; Session-Source Aware Agent Policy.
- Risks / caveats: Search text must include enough schema/property vocabulary or tools become undiscoverable.
- Agentic coding guidance: When adding a tool, ensure names, descriptions, and parameter descriptions contain the retrieval terms an agent would search for.

### Strict Config Validation With Ignored Field Paths
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/openai__codex`, `codex-rs/config/src/strict_config.rs`
- Language / framework / stack: Rust, Serde, TOML config diagnostics
- Evidence snippet:
```rust
let mut ignored_paths = Vec::new();
let mut ignored_callback = |ignored_path: serde_ignored::Path<'_>| {
    let path_segments = ignored_path_segments(&ignored_path);
    if !path_segments.is_empty() {
        ignored_paths.push(path_segments);
    }
};
let deserializer = serde_ignored::Deserializer::new(value, &mut ignored_callback);
let result: Result<T, _> = serde_path_to_error::deserialize(deserializer);
```
- Why it matters: Unknown config keys are reported with path-aware diagnostics instead of being silently ignored by deserialization.
- When to use: Use for user-editable configuration where typos should fail loudly with source locations.
- When not to use: Avoid when forward compatibility requires preserving unknown fields.
- Transferable principle: Wrap permissive deserializers with ignored-field tracking and path-to-error reporting at config boundaries.
- Related patterns: Sentinel Enum For Unspecified Defaults; Configurable Feature Flag Manager.
- Risks / caveats: Strict validation can reject configs from newer versions unless migrations or compatibility rules are considered.
- Agentic coding guidance: Add config fields with schema, strict-validation tests, and unknown-field diagnostics together.

## Worker 2 Second Batch Notes

- CodeGraphContext status: attempted `/Users/amuldotexe/.codex/skills/codegraphcontext-evidence-reader/scripts/scan_current_repo_only.sh` on `/Users/amuldotexe/Desktop/reference-repos-yard/hax`; output directory `/tmp/codex-code-intel/codegraphcontext/hax-20260706-230205`; cancelled after roughly 3 minutes with no progress beyond initial indexing output. Partial `ladybugdb.sqlite` and WAL existed, but no graph evidence was used.
- CodeGraphContext status: attempted the same wrapper on `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/apple__tree-sitter-pkl`; output directory `/tmp/codex-code-intel/codegraphcontext/apple__tree-sitter-pkl-20260706-230857`; cancelled after roughly 90 seconds with no progress beyond initial indexing output. Partial `ladybugdb.sqlite` and WAL existed, but no graph evidence was used.
- Evidence policy: the following entries rely on direct source reads from the listed files.

### Model Editor Endpoint Classification
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__codeql`, `ruby/ql/src/utils/modeleditor/ModelEditor.qll`
- Language / framework / stack: CodeQL QL, Ruby dataflow modeling, VS Code model editor support
- Evidence snippet:
```ql
abstract class Endpoint instanceof DataFlow::Node {
  abstract string getType();
  abstract string getName();
  abstract string getParameters();
}

class MethodEndpoint extends Endpoint instanceof DataFlow::MethodNode {
  pragma[nomagic]
  predicate hasSummary() { this.getNode() instanceof SummaryCallable }
  pragma[nomagic]
  predicate isSource() { this.getNode() instanceof SourceCallable }
  pragma[nomagic]
  predicate isSink() { this.getNode() instanceof SinkCallable }
}
```
- Why it matters: User-facing model editing needs stable endpoint metadata plus explicit supported-source/sink/summary classification.
- When to use: Use when a tool must expose a queryable catalog of APIs and model coverage to editors or automation.
- When not to use: Avoid if the analyzer only needs internal flow facts and no stable endpoint view.
- Transferable principle: Create a small endpoint abstraction that normalizes names, parameters, locations, and support status across richer internal node types.
- Related patterns: Dataflow Boundary Object Model; Explicit Capability Surface.
- Risks / caveats: Overapproximated public APIs can produce noisy model suggestions unless filtered by relevant-file and test-file predicates.
- Agentic coding guidance: When extending model editors, add the endpoint metadata and the support predicate together so agents can tell whether an API is unmodeled or already covered.

### Functorized Dataflow Model Generation
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__codeql`, `rust/ql/src/utils/modelgenerator/internal/CaptureModels.qll`
- Language / framework / stack: CodeQL QL, Rust dataflow, model generator
- Evidence snippet:
```ql
private module RustDataFlowInput implements DataFlowImpl::RustDataFlowInputSig {
  predicate includeDynamicTargets() { none() }
}

module RustDataFlow = DataFlowImpl::RustDataFlowGen<RustDataFlowInput>;
module RustTaintTracking = TaintTrackingImpl::RustTaintTrackingGen<RustDataFlowInput>;

module ModelGeneratorCommonInput implements ModelGeneratorCommonInputSig<R::Location, RustDataFlow> {
  class Callable = QualifiedCallable;
}
```
- Why it matters: The language-specific model generator plugs Rust facts into shared dataflow and taint-tracking generators instead of duplicating engine logic.
- When to use: Use when multiple languages share an analysis algorithm but need language-specific node, callable, or type adapters.
- When not to use: Avoid for a one-off analyzer where the adapter surface is larger than the reused algorithm.
- Transferable principle: Put language variance behind a signature/module input and instantiate shared analysis engines from that input.
- Related patterns: Backend Trait With Phase And Printer; Strategy Adapter Module.
- Risks / caveats: The adapter must be precise about what it overapproximates, such as public Rust functions or trait method implementations.
- Agentic coding guidance: When adding a new language generator, first implement the smallest input signature and keep generator logic in shared modules.

### Extensible Threat Model Configuration Predicate
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__codeql`, `shared/threat-models/codeql/threatmodels/ThreatModels.qll`
- Language / framework / stack: CodeQL QL, MaD models, threat-model configuration
- Evidence snippet:
```ql
extensible predicate threatModelConfiguration(string kind, boolean enable, int priority);
extensible private predicate threatModelGrouping(string kind, string group);

private predicate threatModelEnabled(string kind) {
  knownThreatModel(kind) and
  max(boolean enabled, int priority |
    exists(string configuredKind | configuredKind = getParentThreatModel*(kind) |
      threatModelConfiguration(configuredKind, enabled, priority)
    )
  |
    enabled order by priority
  ) = true
}
```
- Why it matters: Query behavior can be configured through data-extension rows with grouping and priority, without hard-coding every threat source in query logic.
- When to use: Use for security analyzers where users need policy-level toggles such as local, remote, environment, or all.
- When not to use: Avoid when all analysis modes are compile-time fixed and no external configuration is expected.
- Transferable principle: Model policy as extensible data plus deterministic priority resolution.
- Related patterns: Feature Flag Registry; Policy Table With Override Priority.
- Risks / caveats: Priority ordering must be documented because later rows can re-enable kinds disabled by earlier groups.
- Agentic coding guidance: When adding a threat model, add its grouping row and a test that exercises enable, disable, and group override behavior.

### Cached SSA Predicates With Solver Pragmas
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__codeql`, `shared/ssa/codeql/ssa/Ssa.qll`
- Language / framework / stack: CodeQL QL, SSA construction, dataflow performance tuning
- Evidence snippet:
```ql
pragma[nomagic]
private predicate inReadDominanceFrontier(BasicBlock bb, SourceVariable v) { ... }

private predicate synthPhiRead(BasicBlock bb, SourceVariable v) {
  inReadDominanceFrontier(bb, v) and
  liveAtEntry(bb, v) and
  not any(PhiNode def).definesAt(v, bb, _)
}

cached
private newtype TDefinitionExt =
  TWriteDef(SourceVariable v, BasicBlock bb, int i) { ... }
  or TPhiNode(SourceVariable v, BasicBlock bb) { ... }
  or TPhiReadNode(SourceVariable v, BasicBlock bb) { synthPhiRead(bb, v) }
```
- Why it matters: SSA queries can explode combinatorially; the file marks expensive frontier and definition construction points with explicit solver guidance.
- When to use: Use when declarative analysis contains recursive reachability, dominance, liveness, or generated node sets.
- When not to use: Avoid cargo-culting `cached` or `pragma` on cheap predicates where materialization costs more than recomputation.
- Transferable principle: Treat query optimizer directives as part of the algorithm, not as incidental annotations.
- Related patterns: Precomputed QueryPlan Metadata; Memoized Fact Decode Cache.
- Risks / caveats: Incorrect caching boundaries can hide performance regressions or increase database size.
- Agentic coding guidance: When touching hot CodeQL predicates, inspect call fanout and add benchmark or query-eval evidence before changing `cached`, `noinline`, or `nomagic`.

### Read/Write Retry Backend Decorators
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/facebookincubator__Glean`, `glean/backend-api/Glean/Backend/Retry.hs`
- Language / framework / stack: Haskell, Glean backend API, retry policy decorator
- Evidence snippet:
```haskell
data RetryWritesBackend = RetryWritesBackend RetryPolicy (Some Backend)

backendRetryWrites :: Backend b => b -> RetryPolicy -> RetryWritesBackend
backendRetryWrites backend policy = RetryWritesBackend policy (Some backend)

instance Backend RetryWritesBackend where
  queryFact (RetryWritesBackend _ backend) = queryFact backend
  deriveStored (RetryWritesBackend policy backend) log repo q =
    retryChannelExceptions policy $ deriveStored backend log repo q
  enqueueBatch (RetryWritesBackend policy backend) batch =
    retryChannelExceptions policy $ enqueueBatch backend batch
```
- Why it matters: Retry behavior is added by wrapping a backend instance, and the code keeps write retries separate from read retries.
- When to use: Use when cross-cutting resilience policy should be selectable at the backend boundary without modifying every backend implementation.
- When not to use: Avoid if retries require operation-specific idempotency decisions that cannot be captured by broad read/write categories.
- Transferable principle: Decorate a trait/typeclass implementation at the boundary where failure semantics are known.
- Related patterns: Middleware Wrapper For Client Policy; Async Write Queue With Wait Handles.
- Risks / caveats: Retrying writes is only safe if batch submission and polling semantics handle duplicate or forgotten server work.
- Agentic coding guidance: Add retry wrappers around complete interface groups, not individual call sites, and document which methods intentionally pass through.

### STM Bounded Send Queue With Wait Handles
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/facebookincubator__Glean`, `glean/write/Glean/Write/SendQueue.hs`
- Language / framework / stack: Haskell, STM, async writes, Glean service batching
- Evidence snippet:
```haskell
data SendQueue = SendQueue
  { sqOutQueue :: TQueue (Batch, Callback)
  , sqWaitQueue :: TQueue Wait
  , sqMemory :: TVar Int
  , sqCount :: TVar Int
  , sqMaxMemory :: Int
  , sqMaxCount :: Int
  , sqStatus :: TVar QueueStatus
  }

acquireBatch sq size = do
  mem <- readTVar $ sqMemory sq
  count <- readTVar $ sqCount sq
  when (mem > sqMaxMemory sq || count > sqMaxCount sq) retry
```
- Why it matters: The queue enforces backpressure with STM and tracks both unsent batches and sent-but-uncommitted wait handles.
- When to use: Use for asynchronous writes where server acknowledgement is separate from request submission.
- When not to use: Avoid for simple fire-and-forget writes where an unbounded queue would still be safe and observable.
- Transferable principle: Represent queue lifecycle, resource limits, and in-flight server state explicitly in the queue data type.
- Related patterns: Read/Write Retry Backend Decorators; Split Submit And Poll Workflow.
- Risks / caveats: Soft memory limits checked before increment can briefly overshoot, so limits should be sized with batch variance in mind.
- Agentic coding guidance: When adding batch types, update size accounting, enqueue paths, wait callbacks, and failure flushing together.

### Cached Recursive Fact Decoding
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/facebookincubator__Glean`, `glean/typed/Glean/Typed/Fact.hs`
- Language / framework / stack: Haskell, typed fact decoding, `Dynamic`, `IntMap`
- Evidence snippet:
```haskell
decodeRef :: forall p. (Predicate p, Typeable p) => Decoder p
decodeRef = Decoder $ \env@DecoderEnv{..} -> do
  (fid :: IdOf p) <- runDecoder decodeRtsValue env
  cache <- liftIO $ readIORef cacheRef
  let id = fromIntegral (fromFid (idOf fid))
  case IntMap.lookup id cache of
    Just dyn
      | Just p <- fromDynamic dyn -> return p
    Nothing ->
      case IntMap.lookup id serialized of
        Nothing -> return (justId fid)
        Just fact -> do
          f <- decodeFact serialized cacheRef fid fact
          liftIO $ modifyIORef' cacheRef $ IntMap.insert id (toDyn f) cache
          return f
```
- Why it matters: Nested facts can reference each other; caching decoded values avoids repeated recursive decoding and preserves sharing.
- When to use: Use when decoding graph-like serialized data where references may appear multiple times.
- When not to use: Avoid if values are tiny, acyclic, and decoding cache complexity outweighs the savings.
- Transferable principle: Decode references through an identity-indexed cache and fall back to lightweight id-only placeholders when full payloads are absent.
- Related patterns: Cached SSA Predicates With Solver Pragmas; Global Interned Handles.
- Risks / caveats: `Dynamic` requires correct type recovery, and the code throws if a cached id is retrieved with the wrong predicate type.
- Agentic coding guidance: When changing serialized fact formats, update the reference decoder and add tests for repeated nested references and absent payloads.

### Composable Indexer Records
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/facebookincubator__Glean`, `glean/index/Glean/Indexer.hs`
- Language / framework / stack: Haskell, Options.Applicative, Glean indexing
- Evidence snippet:
```haskell
data Indexer opts = Indexer
  { indexerShortName :: String
  , indexerDescription :: String
  , indexerOptParser :: Parser opts
  , indexerRun :: opts -> RunIndexer
  }

indexerThen :: Indexer opts -> (opts -> RunIndexer) -> Indexer opts
indexerThen indexer run2 = indexer
  { indexerRun = \opts -> indexerRun indexer opts <> run2 opts
  }
```
- Why it matters: Indexers package metadata, option parsing, and execution into a first-class value that can be composed.
- When to use: Use for plugin-like CLIs where each backend has its own options but shares a common execution environment.
- When not to use: Avoid for one-off commands where a record abstraction adds indirection without reuse.
- Transferable principle: Make operational capabilities composable by storing parser and runner together.
- Related patterns: Tool Metadata Search Entry; Backend Trait With Phase And Printer.
- Risks / caveats: Composition order matters, and the restricted right-hand indexer shape should be kept intentional.
- Agentic coding guidance: When adding an indexer, provide the short name, description, option parser, and runner in the same definition.

### Move-Only Scope Guard Helpers
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kythe__kythe`, `kythe/cxx/common/scope_guard.h`
- Language / framework / stack: C++17-style templates, RAII, Kythe indexer utilities
- Evidence snippet:
```cpp
template <typename F>
class ABSL_MUST_USE_RESULT ScopeGuard {
 public:
  explicit ScopeGuard(F&& Fn) : Fn(std::forward<F>(Fn)) {}
  ScopeGuard(ScopeGuard&& O) : Released(O.Released), Fn(std::move(O.Fn)) {
    O.Released = true;
  }
  ~ScopeGuard() {
    if (!Released) Fn();
  }
 private:
  bool Released = false;
  F Fn;
};
```
- Why it matters: Temporary stack, scope, or value mutations are restored deterministically even when later code returns early.
- When to use: Use around parser/indexer state stacks, temporary configuration values, and nested visitor state.
- When not to use: Avoid when the cleanup action can fail and must report errors.
- Transferable principle: Use small RAII sentinels to make state restoration lexical and exception-safe.
- Related patterns: Value Restorer; Scoped Context Push.
- Risks / caveats: The guard has no explicit release method, so moving it incorrectly or binding it to an unused temporary can change cleanup timing.
- Agentic coding guidance: When adding temporary state to C++ visitors, prefer `RestoreStack`, `PushScope`, or `RestoreValue` over manual paired push/pop code.

### Schema Enum To Recorder Boundary
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kythe__kythe`, `kythe/cxx/common/indexing/KytheGraphRecorder.h`
- Language / framework / stack: C++, Kythe graph schema, indexing output streams
- Evidence snippet:
```cpp
enum class NodeKindID { kAnchor, kFile, kVariable, kFunction, kPackage, kDiagnostic, kName };
enum class PropertyID { kLocation, kText, kComplete, kNodeKind, kCode, kVisibility };
enum class EdgeKindID { kDefinesFull, kHasType, kRef, kChildOf, kOverrides, kTagged };

absl::string_view spelling_of(NodeKindID node_kind_id);
absl::string_view spelling_of(PropertyID property_id);
absl::string_view spelling_of(EdgeKindID edge_kind_id);

class KytheGraphRecorder {
 public:
  void AddProperty(const VNameRef& node_vname, PropertyID property_id, absl::string_view value);
  void AddEdge(const VNameRef& edge_from, EdgeKindID edge_kind_id, const VNameRef& edge_to);
};
```
- Why it matters: Indexing code uses typed enum identifiers while the recorder owns conversion to schema spellings and output stream entries.
- When to use: Use when a graph or event writer has a finite protocol vocabulary that should not be scattered as strings.
- When not to use: Avoid for truly open extension vocabularies where enum churn would block downstream additions.
- Transferable principle: Keep schema literals behind a typed recorder API.
- Related patterns: Extensible Threat Model Configuration Predicate; Event Enum Queue Logging.
- Risks / caveats: Enums must track the external schema version, and missing spellings can silently prevent downstream consumers from recognizing facts.
- Agentic coding guidance: When adding a graph fact, update enum, spelling conversion, recorder call site, and schema tests together.

### Provenance Token Graph Observer
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/kythe__kythe`, `kythe/cxx/indexer/cxx/KytheGraphObserver.h`
- Language / framework / stack: C++, Clang indexer, Kythe graph observer
- Evidence snippet:
```cpp
class KytheClaimToken : public GraphObserver::ClaimToken {
 public:
  void DecorateVName(VNameRef* target) const {
    target->set_corpus(vname_.corpus());
    target->set_root(vname_.root());
    target->set_path(vname_.path());
  }
  bool rough_claimed() const { return rough_claimed_; }
 private:
  kythe::proto::VName vname_;
  bool rough_claimed_ = true;
};

class KytheGraphObserver : public GraphObserver {
  explicit KytheGraphObserver(KytheGraphRecorder* recorder, KytheClaimClient* client, ...);
};
```
- Why it matters: Semantic graph emission carries provenance and claim status separately from the recorder that serializes facts.
- When to use: Use when an analyzer must decide ownership or provenance before emitting shared graph records.
- When not to use: Avoid if all emitted nodes have the same corpus/root/path and no ownership arbitration.
- Transferable principle: Pass provenance as a token that can decorate identifiers at emission time.
- Related patterns: Schema Enum To Recorder Boundary; Claim Token Ownership Boundary.
- Risks / caveats: The header warns the observer should not be used by multiple threads.
- Agentic coding guidance: When adding graph observer methods, preserve claim-token propagation and avoid bypassing the recorder for direct output writes.

### Timed Search Pipeline Record
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/probelabs__probe`, `src/search/search_options.rs`, `src/search/search_runner.rs`
- Language / framework / stack: Rust, CLI search pipeline, Rayon, Tree-sitter/LSP-adjacent search
- Evidence snippet:
```rust
pub struct SearchOptions<'a> {
    pub path: &'a Path,
    pub queries: &'a [String],
    pub files_only: bool,
    pub custom_ignores: &'a [String],
    pub language: Option<&'a str>,
    pub max_results: Option<usize>,
    pub timeout: u64,
    pub lsp: bool,
}

pub struct SearchTimings {
    pub query_preprocessing: Option<Duration>,
    pub pattern_generation: Option<Duration>,
    pub file_searching: Option<Duration>,
    pub result_processing_ast_parsing: Option<Duration>,
    pub total_search_time: Option<Duration>,
}
```
- Why it matters: Search behavior is configured through one borrowed options struct and measured through a stage-by-stage timing struct.
- When to use: Use for CLI/library search APIs where many flags shape one pipeline and performance regressions need attribution.
- When not to use: Avoid when options are independent enough that a single struct becomes a dumping ground with unclear ownership.
- Transferable principle: Centralize pipeline inputs and observability at the orchestration boundary.
- Related patterns: Search Options Object; Structured Query Plan With Precomputed Metadata.
- Risks / caveats: Large option records need tests for default propagation and flag interactions.
- Agentic coding guidance: When adding search flags, thread them through `SearchOptions`, pipeline destructuring, and timing/debug output in one change.

### Structured Query Plan With Precomputed Metadata
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/probelabs__probe`, `src/search/query.rs`, `src/search/search_runner.rs`
- Language / framework / stack: Rust, Elasticsearch-like query AST, LRU cache
- Evidence snippet:
```rust
pub struct QueryPlan {
    pub ast: elastic_query::Expr,
    pub term_indices: HashMap<String, usize>,
    pub excluded_terms: HashSet<String>,
    pub required_terms_indices: HashSet<usize>,
    pub has_only_excluded_terms: bool,
    pub evaluation_cache: Arc<Mutex<LruCache<u64, bool>>>,
    pub is_universal_query: bool,
    pub special_case_indices: HashSet<usize>,
}

let initial_ast = crate::search::elastic_query::parse_query(&combined_query, *exact)?;
let (search_filters, simplified_ast) =
    SearchFilters::extract_and_simplify_with_autodetect(initial_ast);
```
- Why it matters: Expensive query interpretation is moved to planning, so file scanning can use indices, flags, and caches rather than repeatedly walking the AST.
- When to use: Use when a parsed query is evaluated against many candidate documents or files.
- When not to use: Avoid for single-shot evaluation where precomputation costs dominate.
- Transferable principle: Parse once, precompute hot metadata, then evaluate against many inputs.
- Related patterns: Cached SSA Predicates With Solver Pragmas; Timed Search Pipeline Record.
- Risks / caveats: Cached evaluation behind `Mutex<LruCache<...>>` can become contention if many threads evaluate the same plan.
- Agentic coding guidance: When adding query syntax, update AST parsing, term collection, precomputed flags, and exact/universal-query tests.

### No-Follow Path Safety Utilities
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/probelabs__probe`, `src/path_safety.rs`
- Language / framework / stack: Rust, filesystem traversal safety, Windows junction handling
- Evidence snippet:
```rust
pub fn exists_no_follow(path: &Path) -> bool {
    fs::symlink_metadata(path).is_ok()
}

pub fn is_symlink_or_junction(path: &Path) -> bool {
    if let Ok(meta) = fs::symlink_metadata(path) {
        if meta.file_type().is_symlink() {
            return true;
        }
        #[cfg(target_os = "windows")]
        {
            use std::os::windows::fs::MetadataExt;
            const FILE_ATTRIBUTE_REPARSE_POINT: u32 = 0x400;
            if meta.file_attributes() & FILE_ATTRIBUTE_REPARSE_POINT != 0 {
                return true;
            }
        }
    }
    false
}
```
- Why it matters: Directory scanning avoids following symlinks or Windows junctions that can create cycles and stack overflows.
- When to use: Use in recursive file walkers, ignore-file discovery, and CI-safe scanning tools.
- When not to use: Avoid if symlink traversal is a required feature and cycle detection is implemented elsewhere.
- Transferable principle: Put platform-specific path safety in a small named module instead of sprinkling raw metadata calls through traversal code.
- Related patterns: Boundary Guard Module; Safe Filesystem Walker.
- Risks / caveats: No-follow checks can skip legitimate linked workspaces unless callers provide an opt-in traversal mode.
- Agentic coding guidance: When touching traversal code, call these helpers instead of `Path::exists` or metadata APIs that may follow links.

### Hybrid Structural Semantic Analyzer
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/probelabs__probe`, `lsp-daemon/src/analyzer/hybrid_analyzer.rs`
- Language / framework / stack: Rust, async traits, Tree-sitter, LSP, code intelligence daemon
- Evidence snippet:
```rust
pub struct HybridAnalyzer {
    structural_analyzer: TreeSitterAnalyzer,
    semantic_analyzer: Box<dyn CodeAnalyzer + Send + Sync>,
    lsp_enhancer: Option<Arc<LspRelationshipEnhancer>>,
    relationship_merger: Arc<HybridRelationshipMerger>,
    uid_generator: Arc<SymbolUIDGenerator>,
    config: HybridAnalyzerConfig,
}

pub struct HybridAnalyzerConfig {
    pub prefer_lsp_symbols: bool,
    pub merge_relationships: bool,
    pub fallback_to_structural: bool,
    pub lsp_timeout_seconds: u64,
}
```
- Why it matters: Structural parsing and LSP semantics are composed with explicit fallback, timeout, and merge policy.
- When to use: Use when syntax trees are fast and universal but semantic servers provide higher-quality symbol relationships.
- When not to use: Avoid when the language has no reliable LSP server and Tree-sitter alone meets the accuracy target.
- Transferable principle: Make accuracy/performance tradeoffs configuration, not hidden branches.
- Related patterns: Strategy Adapter Module; Accuracy And Performance Presets.
- Risks / caveats: Merged symbol identity must be stable or duplicate relationships will leak into callers.
- Agentic coding guidance: When changing analyzer behavior, update both `accuracy()` and `performance()` preset expectations.

### Declarative Grammar With External Scanner Escape Hatch
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/apple__tree-sitter-pkl`, `grammar.js`, `src/scanner.c`
- Language / framework / stack: Tree-sitter, JavaScript grammar DSL, C external scanner, Pkl language
- Evidence snippet:
```javascript
externals: $ => [
  $._sl_string_chars,
  $._ml_string_chars,
  $._open_subscript_bracket,
  $._open_argument_paren,
  $._binary_minus,
],

rules: {
  module: $ => seq(
    optional($.shebangComment),
    optional($.moduleHeader),
    repeat(choice($.importClause, $.importGlobClause)),
    repeat($._moduleMember)
  ),
}
```
```c
if (sl) return parse_sl_string_chars(lexer);
if (ml) return parse_ml_string_chars(lexer);
if (osb || oap || bminus) {
  return parse_symbol_no_preceding_newline_or_semicolon(lexer, osb, oap, bminus);
}
```
- Why it matters: The grammar remains declarative for most syntax while the scanner handles context-sensitive string and newline-sensitive tokens.
- When to use: Use in Tree-sitter grammars when a token depends on delimiter depth, lookahead, or preceding newline/semicolon state.
- When not to use: Avoid external scanners for syntax that can be expressed clearly with the grammar DSL.
- Transferable principle: Keep most syntax in a declarative grammar and isolate imperative lexing to the irreducible edge cases.
- Related patterns: Query Files As Tooling Contracts; Scanner Escape Hatch.
- Risks / caveats: Scanner state and error-recovery behavior must be carefully tested because it bypasses much of the grammar DSL's transparency.
- Agentic coding guidance: When adding syntax, first try a grammar rule; only add scanner tokens with focused corpus tests for recovery and delimiter variants.

### Query Files As Tooling Contracts
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/apple__tree-sitter-pkl`, `queries/highlights.scm`, `queries/locals.scm`, `queries/injections.scm`
- Language / framework / stack: Tree-sitter queries, editor highlighting, locals, language injection
- Evidence snippet:
```scheme
(clazz (identifier) @type)
(classMethod (methodHeader (identifier)) @function.method)
(stringInterpolation "\\(" @punctuation.special ")" @punctuation.special) @embedded
```
```scheme
(module) @local.scope
(typedIdentifier (identifier) @local.definition)
(unqualifiedAccessExpr (identifier) @local.reference)
```
```scheme
((unqualifiedAccessExpr (identifier) @methodName (argumentList (slStringLiteralExpr) @injection.content))
  (#set! injection.language "regex"))
```
- Why it matters: Editor semantics are expressed as versioned query files beside the grammar rather than embedded in editor-specific code.
- When to use: Use for parser packages that need highlighting, locals, and injections across multiple editor integrations.
- When not to use: Avoid if the parser is embedded in a single host with a different semantic-token pipeline.
- Transferable principle: Treat query files as public tooling contracts alongside the grammar.
- Related patterns: Declarative Grammar With External Scanner Escape Hatch; Semantic Token Mapping.
- Risks / caveats: The injection query notes imprecision for methods named `Regex`, so tooling contracts can deliberately trade precision for simplicity.
- Agentic coding guidance: When renaming grammar nodes, update highlights, locals, injections, and editor tests in the same patch.

### Macro-Declared Phase Kind Dispatcher
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/hax`, `rust-engine/src/phase.rs`, `rust-engine/src/phase/filter_unprintable_items.rs`
- Language / framework / stack: Rust, compiler phases, AST rewriting
- Evidence snippet:
```rust
pub trait Phase {
    fn apply(&self, items: &mut Vec<Item>);
}

macro_rules! declare_phase_kind {
    {$($name:ident = $phase:expr),*$(,)?} => {
        #[derive(Clone, Debug, Copy, serde::Serialize, serde::Deserialize)]
        pub enum PhaseKind { $($name,)* Legacy(crate::phase::legacy::LegacyOCamlPhase) }
        impl crate::phase::Phase for PhaseKind {
            fn apply(&self, items: &mut Vec<Item>) {
                match *self { $(Self::$name => $phase.apply(items),)* Self::Legacy(phase) => phase.apply(items) }
            }
        }
    };
}
```
- Why it matters: New Rust AST phases are registered once and become serializable, dispatchable pipeline units next to legacy OCaml phases.
- When to use: Use when a compiler has many small passes that need a stable enum for configuration, serialization, or backend phase lists.
- When not to use: Avoid if phases need runtime state that cannot fit a copyable enum variant.
- Transferable principle: Generate repetitive enum dispatch from a single phase registry.
- Related patterns: Backend Trait With Phase And Printer; Composable Indexer Records.
- Risks / caveats: Macro-generated dispatch can hide per-phase initialization needs; stateful phases may require a different registry shape.
- Agentic coding guidance: Add a new phase by implementing `Phase`, adding it to `declare_phase_kind!`, and verifying it appears in the relevant backend phase list.

### Backend Trait With Phase And Printer
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/hax`, `rust-engine/src/backends.rs`, `rust-engine/src/backends/lean.rs`, `rust-engine/src/backends/fstar.rs`
- Language / framework / stack: Rust, compiler backend architecture, pretty printing, AST transformations
- Evidence snippet:
```rust
pub trait Backend {
    type Printer: Printer;
    const NAME: &'static str = Self::Printer::NAME;
    fn phases(&self) -> Vec<crate::phase::PhaseKind> { vec![] }
    fn items_to_module(&self, items: Vec<Item>) -> Vec<Module> { ... }
    fn modules_to_files(&self, modules: Vec<Module>, mut printer: Self::Printer) -> Vec<File> { ... }
    fn module_path(&self, module: &Module) -> Utf8PathBuf;
}

impl<B: Backend> crate::phase::Phase for B {
    fn apply(&self, items: &mut Vec<Item>) {
        for phase in group_consecutive_ocaml_phases(self.phases()) {
            phase.apply(items);
        }
    }
}
```
- Why it matters: A backend is explicitly modeled as transformation phases plus a printer, and can itself be used as a phase.
- When to use: Use in compilers or code generators that target multiple languages with shared AST normalization and per-target printing.
- When not to use: Avoid if each target has a completely unrelated IR pipeline and sharing a backend trait would create false uniformity.
- Transferable principle: Separate target preparation from target rendering, then provide a narrow orchestration trait.
- Related patterns: Macro-Declared Phase Kind Dispatcher; Functorized Dataflow Model Generation.
- Risks / caveats: Shared phases can leak target-specific assumptions unless backend phase lists are reviewed independently.
- Agentic coding guidance: When adding a backend, implement `module_path`, choose phases deliberately, and keep printer-specific escaping in the printer.

### Global Interned Handles With Static Table
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/hax`, `rust-engine/src/interning.rs`
- Language / framework / stack: Rust, global interning, `LazyLock`, `Mutex`, Serde/Schemars
- Evidence snippet:
```rust
pub struct InterningTable<T> {
    items: Vec<T>,
    ids: HashMap<T, Interned<T>>,
}

#[derive(Hash, Eq, PartialEq)]
pub struct Interned<T> {
    phantom: PhantomData<T>,
    index: u32,
}

pub trait Internable: Sized + Hash + Eq + Clone + Send + 'static {
    fn interning_table() -> &'static Mutex<InterningTable<Self>>;
}

pub fn get(self) -> &'static T {
    let table = T::interning_table().lock().unwrap();
    let local_reference = table.get(self);
    let static_reference: &'static T = unsafe { std::mem::transmute(local_reference) };
    static_reference
}
```
- Why it matters: Large repeated identifiers or symbols can be represented as compact copyable handles with O(1) equality and stable serialization behavior.
- When to use: Use for compiler identifiers, symbols, or paths that repeat heavily and live for the process lifetime.
- When not to use: Avoid for short-lived data, unbounded attacker-controlled values, or contexts that require unloading interned values.
- Transferable principle: Use stable small handles for repeated immutable values, and state the lifetime invariant at the unsafe boundary.
- Related patterns: Cached Recursive Fact Decoding; Symbol UID Generator.
- Risks / caveats: The `'static` reference depends on never removing table entries, and the table can grow without reclamation.
- Agentic coding guidance: When adding a new interned type, implement `Internable`, bound the input source where possible, and document table lifetime expectations.

## Worker 2 Batch 3

### Typed Setting Object With Default And Override
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/eclipse-rdf4j-src`, `core/rio/api/src/main/java/org/eclipse/rdf4j/rio/RioSetting.java`, `core/rio/api/src/main/java/org/eclipse/rdf4j/rio/RioConfig.java`, `core/rio/api/src/main/java/org/eclipse/rdf4j/rio/ParserConfig.java`
- Language / framework / stack: Java, RDF4J Rio parser/writer configuration
- Evidence snippet:
```java
public interface RioSetting<T extends Object> extends Serializable {
	String getKey();
	String getDescription();
	T getDefaultValue();
	default T convert(String stringRepresentation) {
		throw new RioConfigurationException("Conversion not implemented for setting: " + getKey());
	}
}

public <T extends Object> T get(RioSetting<T> setting) {
	Object result = settings.get(setting);
	...
	String stringRepresentation = System.getProperty(setting.getKey());
	if (stringRepresentation != null) {
		T typesafeSystemProperty = setting.convert(stringRepresentation);
		systemPropertyCache.put((RioSetting<Object>) setting, typesafeSystemProperty);
		return typesafeSystemProperty;
	}
	return setting.getDefaultValue();
}
```
- Why it matters: Configuration keys carry their own type, default, conversion, and human description, so parser behavior is not driven by stringly typed maps.
- When to use: Use for library configuration surfaces where settings are referenced across parsers, writers, tests, and system properties.
- When not to use: Avoid for one-off internal options where a local constructor parameter is clearer.
- Transferable principle: Model configuration keys as typed domain objects, not bare strings.
- Related patterns: Strict Config Validation With Ignored Field Paths; Sentinel Enum For Unspecified Defaults.
- Risks / caveats: Generic casts remain at the storage boundary; setting implementations must provide correct conversion or system property overrides silently fall back to defaults.
- Agentic coding guidance: When adding a setting, add the `RioSetting<T>` constant and conversion behavior before wiring it into parser logic.

### Stateful RDF Model Builder With Namespace Inference
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/eclipse-rdf4j-src`, `core/model/src/main/java/org/eclipse/rdf4j/model/util/ModelBuilder.java`
- Language / framework / stack: Java, RDF4J model construction, fluent builder
- Evidence snippet:
```java
public ModelBuilder namedGraph(Resource namedGraph) {
	this.currentSubject = null;
	this.currentNamedGraph = namedGraph;
	return this;
}

public ModelBuilder add(IRI predicate, Object object) {
	if (currentSubject == null) {
		throw new ModelException("subject not set");
	}
	return add(currentSubject, predicate, object);
}

private IRI convertPrefixedName(String prefixedName) {
	...
	for (Namespace ns : getDefaultNamespaces()) {
		if (prefix.equals(ns.getPrefix())) {
			model.setNamespace(ns);
			return vf.createIRI(ns.getName(), prefixedName.substring(prefixedName.indexOf(':') + 1));
		}
	}
	return null;
}
```
- Why it matters: The builder lets client code express RDF graph, subject, and predicate context once, while still failing fast when required context is absent.
- When to use: Use for verbose data construction APIs where a small amount of current context removes repeated arguments.
- When not to use: Avoid in concurrent builders or APIs where hidden mutable context would make call order surprising.
- Transferable principle: Fluent builders can hold domain-local context, but must reset it deliberately at boundaries and validate it before use.
- Related patterns: Fluent Builder With Deferred Validation; Push Builder With Validity Mask.
- Risks / caveats: The current subject and graph are mutable state, so reuse across helper methods can accidentally leak context.
- Agentic coding guidance: When adding fluent methods, state exactly which contextual fields they mutate or reset, and add tests for missing-context failures.

### Branching Source Sink Transaction Contract
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/eclipse-rdf4j-src`, `core/sail/base/src/main/java/org/eclipse/rdf4j/sail/base/SailSource.java`, `core/sail/base/src/main/java/org/eclipse/rdf4j/sail/base/SailSink.java`
- Language / framework / stack: Java, RDF4J Sail storage abstraction, transactional RDF store
- Evidence snippet:
```java
public interface SailSource extends SailClosable {
	SailSource fork();
	SailSink sink(IsolationLevel level) throws SailException;
	SailDataset dataset(IsolationLevel level) throws SailException;
	void prepare() throws SailException;
	void flush() throws SailException;
}

public interface SailSink extends SailClosable {
	void prepare() throws SailException;
	void flush() throws SailException;
	void observe(Resource subj, IRI pred, Value obj, Resource... contexts) throws SailException;
	void approve(Resource subj, IRI pred, Value obj, Resource ctx) throws SailException;
	void deprecate(Statement statement) throws SailException;
}
```
- Why it matters: Read snapshots, write sinks, conflict checks, and commit visibility are separated into explicit lifecycle methods.
- When to use: Use for storage engines that need snapshot reads, staged writes, and conflict detection under multiple isolation levels.
- When not to use: Avoid for simple repositories where a single transaction object is enough and source/sink branching would obscure control flow.
- Transferable principle: Split storage APIs into immutable views, mutable sinks, and explicit prepare/flush phases.
- Related patterns: Transactional Operation Module Contract; Concurrent Snapshot Read Transactions.
- Risks / caveats: Callers must respect close/prepare/flush ordering; otherwise the interface can make partial writes look valid.
- Agentic coding guidance: When implementing a new Sail backend, implement snapshot and sink behavior together and test serializable conflict cases.

### Scoped Memory Tracker With Bulk Release
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/neo4j`, `community/common/src/main/java/org/neo4j/memory/MemoryTracker.java`, `community/common/src/main/java/org/neo4j/memory/DefaultScopedMemoryTracker.java`, `community/common/src/main/java/org/neo4j/memory/LocalMemoryTracker.java`
- Language / framework / stack: Java, Neo4j memory accounting
- Evidence snippet:
```java
public interface MemoryTracker extends AutoCloseable, HeapMemoryTracker {
	void allocateNative(long bytes);
	void releaseNative(long bytes);
	void allocateHeap(long bytes);
	void releaseHeap(long bytes);
	default void close() {
		reset();
	}
	MemoryTracker getScopedMemoryTracker();
}

public class DefaultScopedMemoryTracker implements ScopedMemoryTracker {
	public void allocateHeap(long bytes) {
		throwIfClosed();
		delegate.allocateHeap(bytes);
		trackedHeap += bytes;
	}

	public void close() {
		if (!(delegate instanceof ScopedMemoryTracker) || !((ScopedMemoryTracker) delegate).isClosed()) {
			delegate.releaseNative(trackedNative);
			delegate.releaseHeap(trackedHeap);
		}
		trackedNative = 0;
		trackedHeap = 0;
		isClosed = true;
	}
}
```
- Why it matters: Collections and query execution contexts can account for many allocations, then release them without retaining every element.
- When to use: Use when resource accounting must follow nested scopes and parent pools need deterministic release.
- When not to use: Avoid if the runtime can rely solely on garbage collection and no quota or leak diagnostics are needed.
- Transferable principle: Give temporary resource groups a closeable child tracker that aggregates deltas.
- Related patterns: Move-Only Scope Guard Helpers; Thread-Local Panic Context Guard.
- Risks / caveats: A closed tracker throws on later use, so ownership must be clear when passing trackers through APIs.
- Agentic coding guidance: Prefer `getScopedMemoryTracker()` for per-operation allocations and ensure close paths are covered in failure tests.

### Public Status Taxonomy Enum
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/neo4j`, `community/common/src/main/java/org/neo4j/kernel/api/exceptions/Status.java`
- Language / framework / stack: Java, Neo4j public API status codes
- Evidence snippet:
```java
public interface Status {
	enum Request implements Status {
		Invalid(ClientError, "The client provided an invalid request."),
		InvalidFormat(ClientError, "The client provided a request that was missing required fields, or had values that are not allowed."),
		NoThreadsAvailable(TransientError, "There are no available threads to serve this request at the moment. You can retry at a later time "
				+ "or consider increasing max thread pool size for bolt connector(s)."),
		ResourceExhaustion(TransientError, "The server has rejected this request as a resource is exhausted at the moment. "
				+ "You can retry at a later time. For further details see server logs.");

		private final Code code;
		public Code code() {
			return code;
		}
	}
}
```
- Why it matters: User-visible error names, classifications, and descriptions live in one codified taxonomy instead of being scattered across throw sites.
- When to use: Use when clients depend on stable error codes and retry decisions.
- When not to use: Avoid for private exceptions where a typed exception hierarchy is sufficient.
- Transferable principle: Treat public error codes as a versioned API with explicit classification metadata.
- Related patterns: Stable Numeric Error Enum With Discriminants; Typed Error Macros With Debug Strategy.
- Risks / caveats: Once public, names become compatibility commitments and require review discipline.
- Agentic coding guidance: When adding errors, place them in the narrowest status category and include enough description for client behavior.

### Thread Local Database Context Stack
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/arcadedb-src`, `engine/src/main/java/com/arcadedb/database/DatabaseContext.java`
- Language / framework / stack: Java, ArcadeDB embedded database, transactions
- Evidence snippet:
```java
public class DatabaseContext extends ThreadLocal<Map<String, DatabaseContext.DatabaseContextTL>> {
	public static final  DatabaseContext INSTANCE = new DatabaseContext();
	private static final ConcurrentHashMap<Long, Map<String, DatabaseContextTL>> CONTEXTS = new ConcurrentHashMap<>();

	public DatabaseContextTL init(final DatabaseInternal database, final TransactionContext firstTransaction) {
		if (INIT_CALL_COUNTER.incrementAndGet() % CLEANUP_INTERVAL == 0)
			cleanupDeadThreads();
		Map<String, DatabaseContextTL> map = get();
		final String key = database.getDatabasePath();
		...
		CONTEXTS.put(Thread.currentThread().threadId(), map);
		if (current.transactions.isEmpty())
			current.transactions.add(firstTransaction != null ? firstTransaction : new TransactionContext(database.getWrappedDatabaseInstance()));
		return current;
	}

	public void removeCurrentThreadContexts() {
		super.remove();
		CONTEXTS.remove(Thread.currentThread().threadId());
	}
}
```
- Why it matters: The database can resolve the current transaction per thread and per database path while still offering cleanup hooks for virtual threads.
- When to use: Use when legacy or embedded APIs need ambient transaction context and explicit handles would be too invasive.
- When not to use: Avoid in request-scoped async code where work hops threads unless context propagation is explicit.
- Transferable principle: If thread-local state is unavoidable, add a global cleanup index and documented finally-block cleanup.
- Related patterns: Scoped Thread Mode Restoration; Thread-Local Panic Context Guard.
- Risks / caveats: Thread-local transaction stacks can leak or become ambiguous when multiple databases are active.
- Agentic coding guidance: When adding code paths that call `init`, also identify the matching `removeContext` or `removeCurrentThreadContexts` path.

### Retryable Transaction Scope Wrapper
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/arcadedb-src`, `engine/src/main/java/com/arcadedb/database/LocalDatabase.java`
- Language / framework / stack: Java, ArcadeDB transaction API
- Evidence snippet:
```java
public boolean transaction(final TransactionScope txBlock, final boolean joinCurrentTx, int attempts,
		final OkCallback ok, final ErrorCallback error) {
	if (txBlock == null)
		throw new IllegalArgumentException("Transaction block is null");
	if (attempts < 1)
		attempts = 1;

	for (int retry = 0; retry < attempts; ++retry) {
		boolean createdNewTx = true;
		try {
			if (joinCurrentTx && wrappedDatabaseInstance.isTransactionActive())
				createdNewTx = false;
			else
				wrappedDatabaseInstance.begin();
			txBlock.execute();
			if (createdNewTx && wrappedDatabaseInstance.isTransactionActive())
				wrappedDatabaseInstance.commit();
			if (ok != null)
				ok.call();
			return createdNewTx;
		} catch (final NeedRetryException | DuplicatedKeyException e) {
			if (wrappedDatabaseInstance.isTransactionActive())
				wrappedDatabaseInstance.rollback();
			if (retry < attempts - 1)
				delayBetweenRetries(retryDelay);
		}
	}
	throw lastException;
}
```
- Why it matters: Transaction ownership, joining, retry behavior, callbacks, commit, and rollback are centralized in one API instead of repeated at call sites.
- When to use: Use for database APIs where callers should provide a unit of work and the library owns transaction mechanics.
- When not to use: Avoid if callers need fine-grained savepoint control or streaming work across transaction boundaries.
- Transferable principle: Encapsulate retryable transactional work as a scope function that returns whether it created the transaction.
- Related patterns: Command Run-Validate Boundary; Bounded Exponential Backoff Across API Styles.
- Risks / caveats: Retrying a scope is only safe when the callback is idempotent or its side effects are inside the transaction.
- Agentic coding guidance: When using this wrapper, keep external side effects outside the retried block or guard them with idempotency keys.

### Callback Framed Wire Protocol IO
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/arcadedb-src`, `postgresw/src/main/java/com/arcadedb/postgres/PostgresNetworkExecutor.java`
- Language / framework / stack: Java, PostgreSQL wire protocol compatibility layer
- Evidence snippet:
```java
private interface ReadMessageCallback {
	void read(char type, long length) throws IOException;
}

private interface WriteMessageCallback {
	void write() throws IOException;
}

private void writeMessage(final String messageName, final WriteMessageCallback callback, final char messageCode,
		final long length) {
	channel.writeByte((byte) messageCode);
	channel.writeUnsignedInt((int) length);
	if (callback != null)
		callback.write();
	channel.flush();
}

private boolean readMessage(final String messageName, final ReadMessageCallback callback, final char... expectedMessageCodes) {
	final char type = (char) readNextByte();
	final long length = channel.readUnsignedInt();
	...
	callback.read(type, length - 4);
	return true;
}
```
- Why it matters: Common framing, validation, logging, flushing, and error handling are centralized while each message supplies only its payload logic.
- When to use: Use for binary protocols with repeated frame headers and many message-specific payloads.
- When not to use: Avoid for protocols where a generated codec already owns framing and schema evolution.
- Transferable principle: Separate wire-frame mechanics from payload serialization through small callbacks.
- Related patterns: Binary Request Object With Executor Visitor; Host-Language Error Bridge.
- Risks / caveats: Callback code must respect the declared payload length; otherwise stream alignment breaks.
- Agentic coding guidance: When adding a protocol message, implement payload reads/writes through the framing helpers instead of writing directly to the channel.

### Binary Request Object With Executor Visitor
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/orientdb-src`, `client/src/main/java/com/orientechnologies/orient/client/remote/OBinaryRequest.java`, `client/src/main/java/com/orientechnologies/orient/client/binary/OBinaryRequestExecutor.java`
- Language / framework / stack: Java, OrientDB binary client protocol
- Evidence snippet:
```java
public interface OBinaryRequest<T extends OBinaryResponse> {
	void write(final OChannelDataOutput network, ORemoteClientSession session) throws IOException;
	void read(OChannelDataInput channel, int protocolVersion, ORecordSerializer serializer) throws IOException;
	byte getCommand();
	T createResponse();
	OBinaryResponse execute(OBinaryRequestExecutor executor);
	String getDescription();
	default boolean requireDatabaseSession() {
		return true;
	}
}

public interface OBinaryRequestExecutor {
	OBinaryResponse executeListDatabases(OListDatabasesRequest request);
	OBinaryResponse executeCreateDatabase(OCreateDatabaseRequest request);
	OBinaryResponse executeReadRecord(OReadRecordRequest request);
	OBinaryResponse executeCommit(OCommitRequest request);
	OBinaryResponse executeQuery(OQueryRequest request);
}
```
- Why it matters: Each request owns serialization and response creation while the executor provides type-specific dispatch without `instanceof` chains.
- When to use: Use for command protocols with many request types and separate client/server execution strategies.
- When not to use: Avoid if request schemas are generated and dispatch can be table-driven.
- Transferable principle: Put wire encoding on the request object and semantic handling in a visitor-like executor.
- Related patterns: Callback Framed Wire Protocol IO; Trait-Erased Record Variant Deserializer.
- Risks / caveats: Adding a request requires touching the executor interface, which is explicit but can create broad compile churn.
- Agentic coding guidance: When adding a protocol command, implement `write`, `read`, `createResponse`, and the matching executor method in one patch.

### Scoped Thread Mode Restoration
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/orientdb-src`, `core/src/main/java/com/orientechnologies/orient/core/db/OScenarioThreadLocal.java`, `core/src/main/java/com/orientechnologies/orient/core/db/DistributedQueryContext.java`
- Language / framework / stack: Java, OrientDB thread-local database/run-mode context
- Evidence snippet:
```java
public static Object executeAsDistributed(final Callable<? extends Object> iCallback) {
	final OScenarioThreadLocal.RUN_MODE currentDistributedMode =
			OScenarioThreadLocal.instance().getRunMode();
	if (currentDistributedMode != OScenarioThreadLocal.RUN_MODE.RUNNING_DISTRIBUTED)
		OScenarioThreadLocal.instance().setRunMode(OScenarioThreadLocal.RUN_MODE.RUNNING_DISTRIBUTED);
	try {
		return iCallback.call();
	} finally {
		if (currentDistributedMode != OScenarioThreadLocal.RUN_MODE.RUNNING_DISTRIBUTED)
			OScenarioThreadLocal.instance().setRunMode(OScenarioThreadLocal.RUN_MODE.DEFAULT);
	}
}

ODatabaseDocumentInternal prev = ODatabaseRecordThreadLocal.instance().getIfDefined();
try {
	db.activateOnCurrentThread();
	resultSet.close();
	db.close();
} finally {
	if (prev == null) {
		ODatabaseRecordThreadLocal.instance().remove();
	} else {
		ODatabaseRecordThreadLocal.instance().set(prev);
	}
}
```
- Why it matters: Temporary ambient state changes are scoped and restored even when callbacks fail.
- When to use: Use when an API depends on thread-local state but specific operations must impersonate another mode or database.
- When not to use: Avoid if explicit context parameters can be threaded through the API without large rewrites.
- Transferable principle: Capture previous ambient state, set the temporary state, and restore in `finally`.
- Related patterns: Thread Local Database Context Stack; Thread-Local Panic Context Guard.
- Risks / caveats: Nested scopes must restore the exact previous value, not just a default value.
- Agentic coding guidance: Any new thread-local override should be expressed as a helper like `executeAs...` and tested with nested calls.

### Capability Derived Parser Settings
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/surrealdb-src`, `surrealdb/core/src/syn/mod.rs`, `surrealdb/core/src/syn/parser/mod.rs`
- Language / framework / stack: Rust, SurrealDB parser, capability-gated syntax
- Evidence snippet:
```rust
pub fn parse_with_settings<F, R>(input: &[u8], settings: ParserSettings, f: F) -> Result<R>
where
	F: for<'a> AsyncFnOnce(&'a mut Parser<'a>, &'a mut Stk) -> ParseResult<R>,
{
	ensure!(input.len() <= u32::MAX as usize, Error::QueryTooLarge);
	let mut parser = Parser::new_with_settings(input, settings);
	let mut stack = Stack::new();
	stack.enter(|stk| f(&mut parser, stk)).finish()
		.map_err(|e| e.render_on_bytes(input))
		.map_err(Error::InvalidQuery)
		.map_err(anyhow::Error::new)
}

pub fn settings_from_capabilities(cap: &Capabilities) -> ParserSettings {
	ParserSettings {
		object_recursion_limit: *MAX_OBJECT_PARSING_DEPTH as usize,
		query_recursion_limit: *MAX_QUERY_PARSING_DEPTH as usize,
		files_enabled: cap.allows_experimental(&ExperimentalTarget::Files),
		surrealism_enabled: cap.allows_experimental(&ExperimentalTarget::Surrealism),
		..Default::default()
	}
}
```
- Why it matters: Syntax availability and parser resource limits are derived from the same capability object used elsewhere in the database.
- When to use: Use when parsing must respect deployment-level permissions or feature gates.
- When not to use: Avoid if syntax is purely static and cannot vary by execution context.
- Transferable principle: Convert authorization/features into parser settings before parsing, not after AST construction.
- Related patterns: Feature-Gated Tool Backend Selection; Strict Config Validation With Ignored Field Paths.
- Risks / caveats: Capability-derived parsing can make the same input valid in one context and invalid in another, so diagnostics must mention the disabled capability.
- Agentic coding guidance: When adding experimental syntax, add a `ParserSettings` flag and wire it through `settings_from_capabilities`.

### RAII Parser Recursion Budget Macro
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/surrealdb-src`, `surrealdb/core/src/syn/parser/mac.rs`
- Language / framework / stack: Rust, recursive parser macros, RAII drop guards
- Evidence snippet:
```rust
macro_rules! enter_object_recursion {
	($name:ident = $this:expr_2021 => { $($t:tt)* }) => {{
		if $this.settings.object_recursion_limit == 0 {
			return Err($crate::syn::parser::SyntaxError::new("Exceeded query recursion depth limit")
				.with_span($this.last_span(), $crate::syn::error::MessageKind::Error))
		}
		struct Dropper<'a, 'b>(&'a mut $crate::syn::parser::Parser<'b>);
		impl Drop for Dropper<'_, '_> {
			fn drop(&mut self) {
				self.0.settings.object_recursion_limit += 1;
			}
		}
		$this.settings.object_recursion_limit -= 1;
		let mut $name = Dropper($this);
		{ $($t)* }
	}};
}
```
- Why it matters: The parser decrements recursion budget on entry and automatically restores it on every exit path.
- When to use: Use for recursive parsers or evaluators where limits must be restored after nested calls, including early returns.
- When not to use: Avoid if ordinary functions or a reusable guard type can express the same logic more transparently.
- Transferable principle: Use RAII guards to pair budget acquisition and release in recursive code.
- Related patterns: Move-Only Scope Guard Helpers; Thread-Local Panic Context Guard.
- Risks / caveats: Macros hide control flow; diagnostics and borrow behavior need focused parser tests.
- Agentic coding guidance: When adding new recursive parser branches, wrap the branch in the recursion macro rather than manually changing counters.

### Typed Config Key With Override Precedence
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphscope-src`, `interactive_engine/compiler/src/main/java/com/alibaba/graphscope/common/config/Config.java`, `interactive_engine/compiler/src/main/java/com/alibaba/graphscope/common/config/Configs.java`
- Language / framework / stack: Java, GraphScope compiler configuration, Calcite context
- Evidence snippet:
```java
public class Config<T> {
	private String key;
	private String defaultVal;
	private Function<String, T> parseFunc;

	public T get(Configs configs) {
		String valStr = configs.get(key, defaultVal);
		try {
			T val = parseFunc.apply(valStr);
			return val;
		} catch (Exception e) {
			throw new IllegalArgumentException("key [" + key + "] val [" + valStr + "] parse failed", e);
		}
	}

	public static Config<Integer> intConfig(String key, int defaultVal) {
		return new Config<>(key, String.valueOf(defaultVal), (s) -> new BigDecimal(s).intValue());
	}
}

public String get(String name, String defaultValue) {
	if (!StringUtils.isEmpty(value = System.getenv(name))) {
		return value;
	} else if (!StringUtils.isEmpty(value = System.getProperty(name))) {
		return value;
	} else {
		return this.properties.getProperty(name, defaultValue);
	}
}
```
- Why it matters: Callers read typed values while the backing config still supports environment, JVM property, and file overrides in a fixed order.
- When to use: Use in server/compiler tooling where operators need several override layers but code wants typed options.
- When not to use: Avoid if a mature configuration library already provides typed binding and validation.
- Transferable principle: Put parsing and precedence in the config layer, not at every call site.
- Related patterns: Typed Setting Object With Default And Override; Strict Config Validation With Ignored Field Paths.
- Risks / caveats: Parsing is eager at access time, so invalid config may surface late unless critical keys are validated during startup.
- Agentic coding guidance: Add new config values with a `Config<T>` factory and include a failing parse test for bad input.

### Logical To FFI Physical Builder
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphscope-src`, `interactive_engine/compiler/src/main/java/com/alibaba/graphscope/common/ir/runtime/PhysicalBuilder.java`, `interactive_engine/compiler/src/main/java/com/alibaba/graphscope/common/ir/runtime/ffi/FfiPhysicalBuilder.java`
- Language / framework / stack: Java, GraphScope interactive compiler, Calcite, JNA FFI
- Evidence snippet:
```java
public abstract class PhysicalBuilder implements AutoCloseable {
	protected final LogicalPlan logicalPlan;
	public abstract PhysicalPlan build();
}

public class FfiPhysicalBuilder extends RegularPhysicalBuilder<Pointer> {
	public void appendNode(PhysicalNode<Pointer> node) {
		Pointer ptrPlan = this.planPointer.ptrPlan;
		IntByReference oprIdx = new IntByReference(this.planPointer.lastIdx);
		RelNode original = node.getOriginal();
		if (original instanceof GraphLogicalSource) {
			checkFfiResult(LIB.appendScanOperator(ptrPlan, node.getNode(), oprIdx.getValue(), oprIdx));
		} else if (original instanceof GraphLogicalExpand || original instanceof GraphPhysicalExpand) {
			checkFfiResult(LIB.appendEdgexpdOperator(ptrPlan, node.getNode(), oprIdx.getValue(), oprIdx));
		} else if (original instanceof GraphLogicalGetV) {
			checkFfiResult(LIB.appendGetvOperator(ptrPlan, node.getNode(), oprIdx.getValue(), oprIdx));
		}
	}
}
```
- Why it matters: Logical relational nodes are converted into native IR builder calls behind a physical builder abstraction.
- When to use: Use when a Java planner must emit an execution plan owned by a native engine.
- When not to use: Avoid if the target runtime can consume a serialized logical plan directly.
- Transferable principle: Keep planner traversal in a builder layer and isolate native pointer mutation behind checked append calls.
- Related patterns: Backend Trait With Phase And Printer; Functorized Dataflow Model Generation.
- Risks / caveats: The `instanceof` dispatch must stay aligned with logical node evolution and native operator availability.
- Agentic coding guidance: When adding a logical operator, update the FFI builder and add a plan test that exercises the native append path.

### Multi Provider Telemetry Fanout With No Op Fallback
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cline__cline`, `apps/vscode/src/services/telemetry/TelemetryProviderFactory.ts`, `apps/vscode/src/services/telemetry/providers/ITelemetryProvider.ts`, `apps/vscode/src/services/telemetry/TelemetryService.ts`
- Language / framework / stack: TypeScript, VS Code extension services, telemetry providers
- Evidence snippet:
```typescript
export type TelemetryProviderConfig =
	| { type: "posthog"; apiKey?: string; host?: string }
	| { type: "opentelemetry"; config: OpenTelemetryClientValidConfig; bypassUserSettings: boolean }
	| { type: "no-op" }

public static async createProviders(): Promise<ITelemetryProvider[]> {
	const configs = TelemetryProviderFactory.getDefaultConfigs()
	const providers: ITelemetryProvider[] = []
	for (const config of configs) {
		try {
			const provider = await TelemetryProviderFactory.createProvider(config)
			providers.push(provider)
		} catch (error) {
			Logger.error(`Failed to create telemetry provider: ${config.type}`, error)
		}
	}
	if (providers.length === 0) {
		providers.push(new NoOpTelemetryProvider())
	}
	return providers
}

private captureToProviders(event: string, properties: TelemetryProperties, required: boolean): void {
	this.providers.forEach((provider) => {
		try {
			required ? provider.logRequired(event, properties) : provider.log(event, properties)
		} catch (error) {
			Logger.error(`[TelemetryService] Provider failed for event ${event}:`, error)
		}
	})
}
```
- Why it matters: Telemetry can be dual-written during migrations, disabled in self-hosted mode, and isolated so one provider failure does not break the product.
- When to use: Use for integrations where multiple backends may be active and observability must not be on the critical path.
- When not to use: Avoid if exactly one mandatory backend must provide transactional guarantees.
- Transferable principle: Model providers as a fanout list with per-provider failure isolation and a no-op implementation.
- Related patterns: Feature-Gated Tool Backend Selection; Host-Language Error Bridge.
- Risks / caveats: Fanout can produce inconsistent observability if providers differ in enabled settings or event schemas.
- Agentic coding guidance: When adding telemetry features, update the provider interface once and make unsupported providers no-op safely.

### Hook Process Registry With Idempotent Cleanup
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/cline__cline`, `apps/vscode/src/core/hooks/HookProcessRegistry.ts`, `apps/vscode/src/core/hooks/HookProcess.ts`
- Language / framework / stack: TypeScript, Node child processes, VS Code extension hooks
- Evidence snippet:
```typescript
export class HookProcessRegistry {
	private static activeProcesses = new Set<HookProcess>()

	static register(process: HookProcess): void {
		HookProcessRegistry.activeProcesses.add(process)
	}

	static unregister(process: HookProcess): void {
		HookProcessRegistry.activeProcesses.delete(process)
	}

	static async terminateAll(): Promise<void> {
		const processes = Array.from(HookProcessRegistry.activeProcesses)
		await Promise.all(processes.map((p) => p.terminate()))
		HookProcessRegistry.activeProcesses.clear()
	}
}

private safeUnregister(): void {
	if (this.isRegistered) {
		HookProcessRegistry.unregister(this)
		this.isRegistered = false
	}
}
```
- Why it matters: Hook processes are globally visible for shutdown, yet each process can unregister itself repeatedly without double-cleanup bugs.
- When to use: Use for spawned subprocesses, background tasks, or subscriptions that need both local ownership and global teardown.
- When not to use: Avoid for short synchronous work where a registry adds unnecessary mutable global state.
- Transferable principle: Pair global active-resource registries with idempotent local unregister helpers.
- Related patterns: Semaphore Permit Attached To Message; Move-Only Scope Guard Helpers.
- Risks / caveats: A static registry can retain leaked objects if every launch path does not register and unregister consistently.
- Agentic coding guidance: When adding a new process exit path, call `safeUnregister()` and include cancellation/error tests.

### Bounded Exponential Backoff Across API Styles
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-java-driver-src`, `driver/src/main/java/org/neo4j/driver/internal/retry/RetryLogic.java`, `driver/src/main/java/org/neo4j/driver/internal/retry/ExponentialBackoffRetryLogic.java`, `driver/src/main/java/org/neo4j/driver/internal/retry/RetrySettings.java`
- Language / framework / stack: Java, Neo4j driver, sync/async/reactive retry logic
- Evidence snippet:
```java
public interface RetryLogic {
	<T> T retry(Supplier<T> work);
	<T> CompletionStage<T> retryAsync(Supplier<CompletionStage<T>> work);
	<T> Publisher<T> retryRx(Publisher<T> work);
}

public <T> T retry(Supplier<T> work) {
	...
	if (canRetryOn(error)) {
		var elapsedTime = currentTime - startTime;
		if (elapsedTime < maxRetryTimeMs) {
			var delayWithJitterMs = computeDelayWithJitter(nextDelayMs);
			sleep(delayWithJitterMs);
			nextDelayMs = (long) (nextDelayMs * multiplier);
			errors = recordError(error, errors);
			continue;
		}
	}
	addSuppressed(throwable, errors);
	throw throwable;
}

private long computeDelayWithJitter(long delayMs) {
	var jitter = (long) (delayMs * jitterFactor);
	var min = delayMs - jitter;
	var max = delayMs + jitter;
	return ThreadLocalRandom.current().nextLong(min, max + 1);
}
```
- Why it matters: The same retry semantics apply to blocking, `CompletionStage`, and reactive publisher flows.
- When to use: Use for client libraries that expose multiple API styles but need one retry policy.
- When not to use: Avoid for non-idempotent operations unless the server provides retry-safe transaction semantics.
- Transferable principle: Define retry as a policy interface, then implement sync/async/reactive adapters with shared predicates and timing.
- Related patterns: Retryable Transaction Scope Wrapper; Read/Write Retry Backend Decorators.
- Risks / caveats: Retried errors are attached as suppressed exceptions, so downstream logging should preserve them.
- Agentic coding guidance: When changing retry rules, update all three API-style paths and test deadline, jitter bounds, and suppressed errors.

### Observation Context And Convention Split
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-java-driver-src`, `observation/micrometer/src/main/java/org/neo4j/driver/observation/micrometer/SessionRunContext.java`, `observation/micrometer/src/main/java/org/neo4j/driver/observation/micrometer/AbstractSessionContext.java`, `observation/micrometer/src/main/java/org/neo4j/driver/observation/micrometer/DefaultSessionRunConvention.java`
- Language / framework / stack: Java, Neo4j driver, Micrometer observation
- Evidence snippet:
```java
public class SessionRunContext extends AbstractSessionContext {
	private final String query;
	private final MapAccessor parameters;

	public SessionRunContext(Class<? extends BaseSession> sessionType, String query, MapAccessor parameters) {
		super(sessionType);
		this.query = Objects.requireNonNull(query);
		this.parameters = Objects.requireNonNull(parameters);
	}
}

public class DefaultSessionRunConvention implements SessionRunConvention {
	public String getName() {
		return "neo4j.db.client.session.run.duration";
	}

	public KeyValues getLowCardinalityKeyValues(SessionRunContext context) {
		return KeyValues.of(DB_SYSTEM_NAME, sessionType(context));
	}

	public KeyValues getHighCardinalityKeyValues(SessionRunContext context) {
		return KeyValuesUtil.queryAndParameters(..., context.query(), context.parameters(), ...);
	}
}
```
- Why it matters: Runtime event data is separated from metric naming and cardinality decisions, making observability policy replaceable.
- When to use: Use when instrumentation needs stable context objects but different deployments may want different metric conventions.
- When not to use: Avoid for tiny internal metrics where a direct counter call is sufficient.
- Transferable principle: Split observation payloads from naming/tagging conventions.
- Related patterns: Multi Provider Telemetry Fanout With No Op Fallback; HTTP Error Type Implements Response Contract.
- Risks / caveats: High-cardinality tags like query text and parameters must be opt-in or controlled.
- Agentic coding guidance: When adding an observation, create a context class first and keep cardinality choices inside the convention implementation.

## Worker 2 Batch 4

Graph evidence status for this batch:
- Codebase-memory skipped: direct `rg --files`, `rg`, and source reads across the target repos yielded enough evidence, so the optional extra graph-backed repo was not needed.
- CodeGraphContext was not used.

### Versioned Sharded Parse Cache With Lazy Payloads
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/abhigyanpatwari__GitNexus`, `gitnexus/src/storage/parse-cache.ts`
- Language / framework / stack: TypeScript, Node.js, tree-sitter worker cache
- Evidence snippet:
```typescript
const SCHEMA_BUMP = 10;
const GITNEXUS_PKG_VERSION = (() => { ... })();
export const PARSE_CACHE_VERSION = `${SCHEMA_BUMP}+${GITNEXUS_PKG_VERSION}`;

interface ShardedParseCacheIndex {
  version: string;
  keys: string[];
}

export interface ParseCache {
  version: string;
  entries: Map<string, ParseWorkerResult[]>;
  usedKeys: Set<string>;
  storagePath?: string;
  onDiskKeys?: Set<string>;
}

const loadShardedParseCache = async (storagePath: string): Promise<ParseCache | null> => {
  const raw = await fs.readFile(indexPath, 'utf-8');
  const data = JSON.parse(raw) as ShardedParseCacheIndex;
  if (data.version !== PARSE_CACHE_VERSION || !Array.isArray(data.keys)) {
    return emptyCache(storagePath);
  }
  return {
    version: PARSE_CACHE_VERSION,
    entries: new Map<string, ParseWorkerResult[]>(),
    usedKeys: new Set<string>(),
    storagePath,
    onDiskKeys,
  };
};
```
- Why it matters: The cache keeps a small index resident while loading large parse result shards on demand, and it invalidates both schema and parser-version changes before stale worker output can replay.
- When to use: Use for expensive batch work where outputs are content-addressed, large enough to pressure memory, and safe to regenerate.
- When not to use: Avoid for tiny caches where sharding adds failure modes without meaningful memory savings.
- Transferable principle: Version the cache by every input that changes serialized meaning, and keep the memory-resident index separate from lazy payloads.
- Related patterns: Cached Arena IR For Repeated Planning; Incremental Database Inputs With Durability.
- Risks / caveats: Missing shards must be treated as cache misses, and key validation must reject arbitrary path-like values.
- Agentic coding guidance: When adding cache-affecting worker fields, update the schema bump or key namespace in the same patch and add a warm-cache regression test.

### Half Open Circuit Breaker With Neutral Outcomes
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/abhigyanpatwari__GitNexus`, `gitnexus-shared/src/integrations/circuit-breaker.ts`, `gitnexus-shared/src/integrations/resilient-fetch.ts`
- Language / framework / stack: TypeScript, runtime-agnostic HTTP integration resilience
- Evidence snippet:
```typescript
type State = 'closed' | 'open' | 'half-open';

check(): void {
  if (this.state === 'open' && this.openedAt !== null) {
    const elapsed = this.now() - this.openedAt;
    if (elapsed < this.cooldownMs) {
      throw new CircuitOpenError(this.cooldownMs - elapsed, this.key);
    }
    this.state = 'half-open';
  }

  if (this.state === 'half-open') {
    if (this.probeInFlight) {
      throw new CircuitOpenError(this.halfOpenRetryAfterMs, this.key);
    }
    this.probeInFlight = true;
  }
}

recordNeutral(): void {
  this.probeInFlight = false;
}
```
- Why it matters: The breaker distinguishes backend-health evidence from caller cancellations, timeouts, and terminal client errors, so recovery probes do not wedge or erase outage signal.
- When to use: Use around flaky remote dependencies where fail-fast behavior matters and some outcomes should not count as success or failure.
- When not to use: Avoid for low-volume calls where the complexity of breaker state outweighs the outage protection.
- Transferable principle: Pair every admitted protected call with an explicit outcome classification, including a neutral path that releases permits without mutating health.
- Related patterns: Bounded Exponential Backoff Across API Styles; Read/Write Retry Backend Decorators.
- Risks / caveats: A successful `check()` without a matching `record*()` leaves the half-open permit consumed.
- Agentic coding guidance: Generate protected-call wrappers with `try`/`catch` classification in one place; do not let call sites manipulate breaker state ad hoc.

### Parenthesized SMT Proxy With Loggable Policy Checks
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/prusti-dev`, `prusti-smt-solver/src/subprocess.rs`, `prusti-smt-solver/src/context.rs`, `prusti-smt-solver/src/solver.rs`
- Language / framework / stack: Rust, async-std, Z3/SMT subprocess proxy
- Evidence snippet:
```rust
fn are_parens_balanced(line: &str) -> bool {
    let openning_parens = line.chars().filter(|c| *c == '(').count();
    let closing_parens = line.chars().filter(|c| *c == ')').count();
    openning_parens == closing_parens
}

while not_finished && read_command(&mut command).await? {
    context.write_to_log("in ", &command).await?;
    let now = std::time::Instant::now();
    solver_stdin.write_all(command.as_bytes()).await?;
    solver_stdin.flush().await?;
    read_response(&mut solver_stdout, &mut response).await?;
    context.write_number_to_log("elapsed-time", now.elapsed().as_millis()).await?;
    stdout.write_all(response.as_bytes()).await?;
    context.check(&command, &response).await?;
}
```
- Why it matters: The wrapper preserves the solver protocol while adding timing, transcript logging, stderr forwarding, and optional policy checks around quantifier instantiation.
- When to use: Use when an external process speaks a line-oriented or delimiter-balanced protocol and you need observability without changing callers.
- When not to use: Avoid if the protocol is binary, streaming, or requires full grammar parsing rather than a cheap frame delimiter.
- Transferable principle: Put protocol framing, logging, and policy enforcement in a transparent proxy layer between the caller and subprocess.
- Related patterns: Callback Framed Wire Protocol IO; Command Run-Validate Boundary.
- Risks / caveats: Parenthesis balance is a protocol heuristic; quoted strings or comments can make a richer parser necessary.
- Agentic coding guidance: When adding solver policies, keep them in `Context::check` and ensure normal pass-through behavior remains byte-compatible.

### Declarative JNI Wrapper Specs With Atomic Emission
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/prusti-dev`, `jni-gen/src/wrapper_spec.rs`, `jni-gen/src/wrapper_generator.rs`
- Language / framework / stack: Rust, JNI wrapper generation
- Evidence snippet:
```rust
pub enum ItemWrapperSpec {
    ScalaObjectGetter(),
    Constructor { signature: Option<String>, suffix: Option<String> },
    Method { name: String, signature: Option<String>, suffix: Option<String> },
    FieldGetterSetter { field_name: String },
    TraitFieldGetterSetter { field_name: String },
}

#[macro_export]
macro_rules! method {
    ($name:expr, $signature:expr, $suffix:expr) => {
        ItemWrapperSpec::Method {
            name: $name.into(),
            signature: Some($signature.into()),
            suffix: Some($suffix.into()),
        }
    };
}

fn save_file_atomic(content: &str, temp_dir: &Path, file_path: &Path) -> LocalResult<()> {
    let mut mod_file = tempfile::NamedTempFile::new_in(temp_dir)?;
    mod_file.write_all(content.as_bytes())?;
    mod_file.into_temp_path().persist(file_path)?;
    Ok(())
}
```
- Why it matters: JNI wrapper generation is driven by a small typed specification language, then emitted with atomic writes so interrupted generation does not leave partial Rust modules.
- When to use: Use when many foreign-language bindings share a mechanical shape but differ in class, method, field, or signature metadata.
- When not to use: Avoid for small hand-written bindings where macro-generated indirection makes debugging harder.
- Transferable principle: Represent generated API surfaces as typed specs, then make generation idempotent and crash-tolerant.
- Related patterns: Macro-Declared Phase Kind Dispatcher; Source-Copied Adapter With Upstream Provenance.
- Risks / caveats: Spec macros must stay aligned with the generator; missing signature validation can push errors to runtime JNI calls.
- Agentic coding guidance: Add a new wrapped class by extending the spec list and running generator tests; do not edit generated wrappers by hand.

### Version Sliced Compatibility Shim Traits
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-comet-src`, `spark/src/main/spark-3.5/org/apache/comet/shims/CometExprShim.scala`, `spark/src/main/spark-4.0/org/apache/comet/shims/CometExprShim.scala`
- Language / framework / stack: Scala, Apache Spark extension, DataFusion Comet
- Evidence snippet:
```scala
trait CometExprShim extends CommonStringExprs {
  protected def evalMode(c: Cast): CometEvalMode.Value =
    CometEvalModeUtil.fromSparkEvalMode(c.evalMode)

  protected def binaryOutputStyle: BinaryOutputStyle = BinaryOutputStyle.HEX_DISCRETE

  def versionSpecificExprToProtoInternal(
      expr: Expression,
      inputs: Seq[Attribute],
      binding: Boolean): Option[Expr] = {
    expr match {
      case s: StringDecode =>
        stringDecode(expr, s.charset, s.bin, inputs, binding)
      case _ => None
    }
  }
}
```
- Why it matters: Spark-version differences live in version-sliced shim files, allowing common serializer code to call a stable trait while each Spark line handles its own expression quirks.
- When to use: Use for libraries that support multiple host-framework versions whose APIs differ in small but recurring ways.
- When not to use: Avoid when version behavior is almost identical and conditional compilation or a tiny adapter is clearer.
- Transferable principle: Keep the common integration contract stable and isolate host-version deltas behind narrow shim traits.
- Related patterns: Platform Workaround Module; Feature-Gated Tool Backend Selection.
- Risks / caveats: Shims can drift semantically; cross-version tests must assert equivalent behavior where compatibility is expected.
- Agentic coding guidance: When adding Spark-specific expression support, change only the relevant version shim and add a compatibility note if behavior differs by Spark line.

### Compatibility Support Level As Serialization Contract
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-comet-src`, `spark/src/main/scala/org/apache/comet/serde/SupportLevel.scala`, `spark/src/main/scala/org/apache/comet/serde/CometExpressionSerde.scala`
- Language / framework / stack: Scala, Spark expression serialization, compatibility documentation
- Evidence snippet:
```scala
sealed trait SupportLevel
case class Compatible(notes: Option[String] = None) extends SupportLevel
case class Incompatible(notes: Option[String] = None) extends SupportLevel
case class Unsupported(notes: Option[String] = None) extends SupportLevel

trait CometExpressionSerde[T <: Expression] {
  def getCompatibleNotes(): Seq[String] = Seq.empty
  def getIncompatibleReasons(): Seq[String] = Seq.empty
  def getUnsupportedReasons(): Seq[String] = Seq.empty
  def getSupportLevel(expr: T): SupportLevel = Compatible(None)
  def convert(expr: T, inputs: Seq[Attribute], binding: Boolean): Option[ExprOuterClass.Expr]
}
```
- Why it matters: Serialization support is not a boolean; it carries compatibility status and documentation hooks alongside conversion behavior.
- When to use: Use when an accelerator, transpiler, or adapter supports a feature with known semantic gaps.
- When not to use: Avoid if support is strictly all-or-nothing and no user-facing compatibility documentation is needed.
- Transferable principle: Make compatibility a typed return value, not a comment beside the conversion code.
- Related patterns: Public Status Taxonomy Enum; Observation Context And Convention Split.
- Risks / caveats: If `convert` returns `None` without tagging reasons, users see unexplained fallback.
- Agentic coding guidance: When adding a serializer, implement support-level logic and documentation methods before wiring the expression into planning.

### Domain Error Chaining Around Generated gRPC Calls
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/alien`, `packages/sdk/src/grpc-utils.ts`, `packages/sdk/src/bindings/queue.ts`
- Language / framework / stack: TypeScript, nice-grpc SDK bindings
- Evidence snippet:
```typescript
export async function grpcErrorToAlienError(
  error: unknown,
  service: string,
  method: string,
  context?: { bindingName?: string; path?: string; key?: string; secretName?: string },
): Promise<AlienError<any>> {
  const baseError = await AlienError.from(error)

  if (error && typeof error === "object" && "code" in error) {
    const grpcError = error as { code: number; details?: string; message?: string }
    if (grpcError.code === Status.NOT_FOUND && context?.key && context?.bindingName) {
      return baseError.withContext(
        KvKeyNotFoundError.create({ bindingName: context.bindingName, key: context.key }),
      )
    }
    return baseError.withContext(
      GrpcCallError.create({ service, method, grpcCode: Status[grpcError.code], details }),
    )
  }
}

export async function wrapGrpcCall<T>(
  service: string,
  method: string,
  call: () => Promise<T>,
  context?: { bindingName?: string; path?: string; key?: string },
): Promise<T> {
  try { return await call() } catch (error) {
    throw await grpcErrorToAlienError(error, service, method, context)
  }
}
```
- Why it matters: Generated transport errors become SDK-domain errors with binding, key, path, or secret context while preserving the original error chain.
- When to use: Use when generated clients expose low-level status codes but application callers need actionable domain exceptions.
- When not to use: Avoid when the generated client already provides stable domain errors.
- Transferable principle: Put transport-to-domain error mapping in one wrapper and pass operation context at each call site.
- Related patterns: Host-Language Error Bridge; HTTP Error Type Implements Response Contract.
- Risks / caveats: Incomplete context produces generic errors; binding methods must pass the most specific available fields.
- Agentic coding guidance: Wrap every new gRPC SDK method with `wrapGrpcCall` and include the resource identifier that best explains failures.

### Runtime Drainable Background Task Registry
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/alien`, `packages/sdk/src/wait-until.ts`
- Language / framework / stack: TypeScript, serverless runtime SDK, gRPC coordination
- Evidence snippet:
```typescript
const tasks: Map<string, TaskTracker> = new Map()
let taskIdCounter = 0

async register(promise: Promise<unknown>, description?: string): Promise<TaskTracker> {
  const id = `task-${++taskIdCounter}`
  const tracker: TaskTracker = { id, promise, registeredAt, completed: false }
  tasks.set(id, tracker)
  await this.client.notifyTaskRegistered({ applicationId: this.applicationId, taskDescription: description })
  promise
    .then(() => { tracker.completed = true })
    .catch(error => {
      tracker.completed = true
      tracker.error = error instanceof Error ? error : new Error(String(error))
    })
  return tracker
}

async waitForAll(): Promise<void> {
  const pending = Array.from(tasks.values())
    .filter(t => !t.completed)
    .map(t => t.promise.catch(() => {}))
  await Promise.all(pending)
}
```
- Why it matters: Background work is visible to the runtime, can be drained before shutdown, and does not let individual task failures block drain completion.
- When to use: Use in serverless or request/response runtimes where post-response work must be tracked explicitly.
- When not to use: Avoid for durable job queues where tasks must survive process death.
- Transferable principle: Register background promises in a central tracker, notify the runtime, and provide a drain path that observes all pending work.
- Related patterns: Hook Process Registry With Idempotent Cleanup; Semaphore Permit Attached To Message.
- Risks / caveats: In-memory tracking is process-local and cannot guarantee completion across crashes.
- Agentic coding guidance: When adding background APIs, define how tasks are registered, observed, drained, and reported on failure before exposing the public helper.

### MCP Cold Start Envelope Guard
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Cranot__roam-code`, `src/roam/mcp_extras/preflight.py`
- Language / framework / stack: Python, MCP server/tooling, code index preflight
- Evidence snippet:
```python
_NO_INDEX_NEEDED: frozenset[str] = frozenset({
    "roam_init",
    "roam_reindex",
    "roam_doctor",
    "roam_catalog",
    "roam_expand_toolset",
    "roam_session_metrics",
})

def needs_index(tool_name: str) -> bool:
    return tool_name not in _NO_INDEX_NEEDED

def cold_start_envelope(tool_name: str) -> dict[str, Any]:
    return {
        "command": tool_name,
        "isError": True,
        "status": "index_not_built",
        "next_command": "roam init",
        "retry_after_seconds": 60,
        "agent_contract": {
            "next_commands": ["roam init", "# then retry the MCP tool that returned this envelope"],
        },
    }
```
- Why it matters: Missing prerequisites return a structured, actionable response instead of timing out, hanging, or producing empty output that an agent cannot interpret.
- When to use: Use for tool servers where many operations require a precomputed index, login, database migration, or other bootstrap step.
- When not to use: Avoid when the prerequisite is cheap and safe to create automatically without surprising the caller.
- Transferable principle: Gate by default, exempt only explicitly safe tools, and make the failure envelope tell the agent exactly what to run next.
- Related patterns: Strict Config Validation With Ignored Field Paths; Command Run-Validate Boundary.
- Risks / caveats: The exemption set must be audited; adding a DB-reading tool to `_NO_INDEX_NEEDED` reintroduces cold-start hangs.
- Agentic coding guidance: When adding an MCP tool, assume it needs the index unless source evidence proves otherwise; update description hints and preflight tests together.

### AST Read Surface Counts With Duplicate Fail Loud
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Cranot__roam-code`, `src/roam/surface_counts.py`
- Language / framework / stack: Python, AST inspection, CLI/MCP documentation automation
- Evidence snippet:
```python
def mcp_tool_names() -> list[str]:
    mcp_path = _package_file("mcp_server.py")
    module = _load_ast(mcp_path)
    names = _decorated_tool_names_from_loaded_mcp_ast(module)
    duplicates = sorted(name for name, c in Counter(names).items() if c > 1)
    if duplicates:
        raise ValueError(f"duplicate @_tool(name=...) decorations in mcp_server.py: {duplicates}")
    return sorted(names)

def _iter_tool_decorations(module: ast.Module):
    for node in ast.walk(module):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for decorator in node.decorator_list:
            if _is_tool_decorator(decorator):
                yield node, decorator
```
- Why it matters: Documentation and coverage counts derive from source syntax without importing the server, while duplicate registrations fail loudly instead of being hidden by `set()`.
- When to use: Use for build-time audits of CLI commands, decorators, routes, migrations, or generated docs where imports may have side effects.
- When not to use: Avoid when dynamic runtime registration is the intended source of truth and cannot be represented in AST literals.
- Transferable principle: Use static AST readers for drift audits, but preserve raw multiplicity long enough to detect duplicates.
- Related patterns: Query Files As Tooling Contracts; Strict Config Validation With Ignored Field Paths.
- Risks / caveats: AST-only readers miss runtime plugin registrations unless a separate dynamic audit covers them.
- Agentic coding guidance: When adding surface-count automation, keep traversal helpers separate from reporting policy and add tests for duplicate names.

### Memoized Env Knobs With Test Reset
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/odvcencio__gotreesitter`, `parser_config.go`, `parser_memory_budget_test.go`
- Language / framework / stack: Go, parser runtime configuration
- Evidence snippet:
```go
var (
	parseMemoryBudgetOnce  sync.Once
	parseMemoryBudgetMBVal int
)

func ResetParseEnvConfigCacheForTests() {
	parseMemoryBudgetOnce = sync.Once{}
	parseMemoryBudgetMBVal = 0
}

func parseMemoryBudgetMB() int {
	parseMemoryBudgetOnce.Do(func() {
		parseMemoryBudgetMBVal = 512
		raw := strings.TrimSpace(os.Getenv("GOT_PARSE_MEMORY_BUDGET_MB"))
		if raw == "" {
			return
		}
		n, err := strconv.Atoi(raw)
		if err == nil && n >= 0 {
			parseMemoryBudgetMBVal = n
		}
	})
	return parseMemoryBudgetMBVal
}
```
- Why it matters: Environment-derived parser knobs are read once for production speed, while tests can reset memoized values after mutating `t.Setenv`.
- When to use: Use for process-level feature flags or resource limits read on hot paths.
- When not to use: Avoid if configuration must respond live to environment changes during normal operation.
- Transferable principle: Pair `sync.Once` environment caching with a narrow test reset hook.
- Related patterns: Typed Config Key With Override Precedence; Capability Derived Parser Settings.
- Risks / caveats: Reset hooks should be clearly test-only by convention; production code using them can make behavior non-deterministic.
- Agentic coding guidance: When adding an env knob, include parsing defaults, false/off handling if boolean, and a reset line in the test helper.

### Synthetic Reparse Recovery With Byte Remapping
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/odvcencio__gotreesitter`, `parser_result_swift_conditions.go`
- Language / framework / stack: Go, tree-sitter parser recovery, Swift grammar compatibility
- Evidence snippet:
```go
func normalizeSwiftRecoveredTrailingClosureConditions(root *Node, source []byte, p *Parser, lang *Language) {
	inserts := swiftCollectConditionParenInserts(root, source, lang)
	if len(inserts) == 0 {
		return
	}
	transformed, insTPos := swiftApplyParenInserts(source, inserts)
	tree, err := p.parseForRecovery(transformed)
	if err != nil || tree == nil || tree.RootNode() == nil {
		return
	}
	defer tree.Release()
	tRoot := tree.RootNode()
	if tRoot.HasError() || tRoot.Type(lang) != "source_file" || tRoot.endByte != uint32(len(transformed)) {
		return
	}
	rm := &swiftRemap{tsrc: transformed, insSet: make(map[uint32]bool, len(insTPos)), insPos: insTPos, arena: root.ownerArena}
	newRoot, ok := rm.remap(tRoot)
	if !ok || newRoot == nil {
		return
	}
	root.children = cloneNodeSliceIfArena(root.ownerArena, newRoot.children)
}
```
- Why it matters: A known grammar ambiguity is repaired by adding synthetic tokens, reparsing, verifying a clean transformed tree, and remapping nodes back to original byte coordinates.
- When to use: Use for parser compatibility layers where a small source transform can disambiguate syntax without changing the upstream grammar immediately.
- When not to use: Avoid if the transform cannot be proven byte-faithful or if it masks unrelated parse errors.
- Transferable principle: Recovery transforms need a clean reparse gate and a coordinate remapper that removes synthetic structure before returning.
- Related patterns: RAII Parser Recursion Budget Macro; Declarative Grammar With External Scanner Escape Hatch.
- Risks / caveats: Byte remapping must handle all synthetic insertions, comments, and nested constructs; otherwise source spans become untrustworthy.
- Agentic coding guidance: Add recovery only with before/after parse tests that assert no errors, original byte spans, and unchanged unaffected files.

### Grammar Update Script With Filesystem Discovered Aliases
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__ocaml-tree-sitter-semgrep`, `scripts/update-grammar`, `scripts/test_update_grammar.py`
- Language / framework / stack: Python, tree-sitter grammar maintenance, git submodules
- Evidence snippet:
```python
LANGUAGE_ALIASES = {
    "gomod": "go-mod",
    "apex": "sfapex",
}

def discover_valid_languages(root: Path) -> dict[str, str]:
    sg_src = root / "lang" / "semgrep-grammars" / "src"
    wrappers = {
        p.name.removeprefix("semgrep-")
        for p in sg_src.glob("semgrep-*")
        if p.is_dir()
    }
    result: dict[str, str] = {}
    for name in wrappers:
        submodule = LANGUAGE_ALIASES.get(name, name)
        if has("tree-sitter", submodule):
            result[name] = name
    for key, target in LANGUAGE_ALIASES.items():
        if has("semgrep", target) and has("tree-sitter", target):
            result[key] = target
    return result
```
- Why it matters: A maintenance script validates user input against actual wrapper/submodule directories, supports historical aliases, and rejects path-traversal or typo inputs before touching git state.
- When to use: Use for repo maintenance CLIs that operate on a known set of generated or vendored components.
- When not to use: Avoid when component names come from a remote registry and filesystem discovery would be incomplete.
- Transferable principle: Discover legal targets from the repo shape, then layer explicit aliases for human-facing compatibility.
- Related patterns: Query Files As Tooling Contracts; No-Follow Path Safety Utilities.
- Risks / caveats: Alias tables must be tested so target renames do not make valid user input disappear.
- Agentic coding guidance: When extending such scripts, add fake-filesystem tests for direct names, aliases, missing paired directories, and invalid names.

### Qualifier Scoped Multi DataSource Wiring
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/ityouknow__spring-boot-examples`, `spring-boot-jpa/spring-boot-multi-Jpa/src/main/java/com/neo/config/DataSourceConfig.java`, `spring-boot-jpa/spring-boot-multi-Jpa/src/main/java/com/neo/config/PrimaryConfig.java`, `spring-boot-jpa/spring-boot-multi-Jpa/src/main/java/com/neo/config/SecondaryConfig.java`
- Language / framework / stack: Java, Spring Boot, Spring Data JPA, multiple data sources
- Evidence snippet:
```java
@Bean(name = "primaryDataSource")
@Primary
@ConfigurationProperties("spring.datasource.primary")
public DataSource firstDataSource() {
    return DataSourceBuilder.create().build();
}

@EnableJpaRepositories(
    entityManagerFactoryRef="entityManagerFactoryPrimary",
    transactionManagerRef="transactionManagerPrimary",
    basePackages= { "com.neo.repository.test1" })
public class PrimaryConfig {
    @Autowired
    @Qualifier("primaryDataSource")
    private DataSource primaryDataSource;

    @Bean(name = "entityManagerFactoryPrimary")
    @Primary
    public LocalContainerEntityManagerFactoryBean entityManagerFactoryPrimary(EntityManagerFactoryBuilder builder) {
        return builder.dataSource(primaryDataSource).packages("com.neo.model").persistenceUnit("primaryPersistenceUnit").build();
    }
}
```
- Why it matters: Each repository package is bound to its own data source, entity manager factory, and transaction manager, while one primary path remains the default for ambiguous injection.
- When to use: Use when a Spring app must read/write multiple databases with separate repository packages.
- When not to use: Avoid if the app only needs one database; extra qualifiers add ceremony and failure modes.
- Transferable principle: Name every bean in the persistence stack and connect repository scanning to the matching transaction boundary.
- Related patterns: Typed Setting Object With Default And Override; Layered REST Decorator Stack.
- Risks / caveats: Reusing entity packages across persistence units can hide accidental cross-database writes unless tests cover both repositories.
- Agentic coding guidance: When adding another data source, add the `DataSource`, entity manager, transaction manager, repository base package, and integration test together.

### Dynamic Plugin Registry With ABI Gate
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tikv-src`, `src/coprocessor_v2/plugin_registry.rs`, `src/coprocessor_v2/endpoint.rs`
- Language / framework / stack: Rust, TiKV coprocessor plugins, dynamic library loading
- Evidence snippet:
```rust
fn err_on_mismatch(
    plugin_build_info: &BuildInfo,
    tikv_build_info: &BuildInfo,
) -> Result<(), PluginLoadingError> {
    if plugin_build_info.api_version != tikv_build_info.api_version {
        Err(PluginLoadingError::ApiMismatch { ... })
    } else if plugin_build_info.rustc != tikv_build_info.rustc {
        Err(PluginLoadingError::CompilerMismatch { ... })
    } else if plugin_build_info.target != tikv_build_info.target {
        Err(PluginLoadingError::TargetMismatch { ... })
    } else {
        Ok(())
    }
}

pub unsafe fn new<P: AsRef<OsStr>>(file_path: P) -> Result<Self, PluginLoadingError> {
    let lib = Library::new(&file_path)?;
    let get_build_info: Symbol<'_, PluginGetBuildInfoSignature> =
        lib.get(PLUGIN_GET_BUILD_INFO_SYMBOL)?;
    let plugin_constructor: Symbol<'_, PluginConstructorSignature> =
        lib.get(PLUGIN_CONSTRUCTOR_SYMBOL)?;
    err_on_mismatch(&get_build_info(), &BuildInfo::get())?;
    let boxed_raw_plugin = plugin_constructor(host_allocator);
    let plugin = Box::from_raw(boxed_raw_plugin);
    std::mem::forget(lib);
    Ok(LoadedPlugin { name, version, plugin })
}
```
- Why it matters: Unsafe dynamic loading is guarded by API, compiler, and target checks before the plugin constructor runs, then the library is intentionally leaked so plugin code stays mapped.
- When to use: Use when a host process loads third-party native extensions with a narrow ABI.
- When not to use: Avoid if plugin code is untrusted and should run out-of-process with sandboxing.
- Transferable principle: Validate compatibility metadata before crossing the unsafe constructor boundary.
- Related patterns: Checked Constructor Paired With Unsafe Fast Path; Sealed Representation Trait.
- Risks / caveats: Leaking libraries is deliberate but means plugins are not fully unloaded; hot reload semantics must explain that old code may still run.
- Agentic coding guidance: When adding plugin metadata, verify it before `plugin_constructor` and add a test with a mismatched build-info fixture.

### Plugin Storage API Error Shim
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tikv-src`, `src/coprocessor_v2/raw_storage_impl.rs`, `src/coprocessor_v2/endpoint.rs`
- Language / framework / stack: Rust, TiKV raw storage adapter, coprocessor plugin API
- Evidence snippet:
```rust
async fn put(&self, key: Key, value: Value) -> PluginResult<()> {
    let ctx = self.context.clone();
    let (cb, f) = paired_future_callback();
    let res = self.storage.raw_put(ctx, String::new(), key, value, ttl, cb);
    match res {
        Err(e) => Err(e),
        Ok(_) => f.await.map_err(PluginErrorShim::from)?,
    }
    .map_err(PluginErrorShim::from)?;
    Ok(())
}

impl From<storage::errors::Error> for PluginErrorShim {
    fn from(error: storage::errors::Error) -> Self {
        let inner = match *error.0 {
            storage::errors::ErrorInner::Kv(KvError(box KvErrorInner::Timeout(duration))) => {
                PluginError::Timeout(duration)
            }
            _ => PluginError::Other(format!("{}", &error), Box::new(storage::Result::<()>::Err(error))),
        };
        PluginErrorShim(inner)
    }
}
```
- Why it matters: The plugin-facing storage trait exposes domain-specific errors while preserving internal storage errors inside an opaque box for region-error extraction.
- When to use: Use when an extension API wraps a richer internal subsystem and needs a stable public error surface.
- When not to use: Avoid if callers need the complete internal error type as part of the public contract.
- Transferable principle: Translate errors at the boundary, but retain enough original error payload for privileged downstream handling.
- Related patterns: Domain Error Chaining Around Generated gRPC Calls; Host-Language Error Bridge.
- Risks / caveats: Boxing internal results relies on both sides knowing how to downcast; document that escape hatch carefully.
- Agentic coding guidance: When adding storage operations, route both immediate call errors and callback future errors through the same shim.

### Admission Before Enqueue With Delay Slot Release
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tikv-src`, `src/read_pool.rs`
- Language / framework / stack: Rust, TiKV read pool scheduling, resource control
- Evidence snippet:
```rust
async fn admission_and_enqueue(
    resource_manager: Option<Arc<ResourceGroupManager>>,
    resource_limiter: Option<Arc<ResourceLimiter>>,
    task_priority: TaskPriority,
    gauge: IntGauge,
    max_tasks: usize,
    remote: Remote<TaskCell>,
    task_cell: TaskCell,
    resource_ctl: Option<Arc<ResourceController>>,
    estimated_priority: u64,
) -> Result<(), ReadPoolError> {
    let delay = match (resource_manager.as_deref(), resource_limiter.as_deref()) {
        (Some(rm), Some(limiter)) => match rm.admission_decision(true, limiter) {
            AdmissionDecision::Reject => return Err(ReadPoolError::Rejected),
            AdmissionDecision::Delay(d) => Some((d, resource_manager)),
            AdmissionDecision::Allow => None,
        },
        _ => None,
    };
    if let Some((d, slot)) = delay {
        let mut _guard = slot.as_ref().map(|rm| rm.delay_slot_guard());
        futures_timer::Delay::new(d).await;
        if let Some(guard) = _guard.as_mut() {
            guard.release();
        }
    }
    if gauge.get() as usize >= max_tasks {
        return Err(ReadPoolError::UnifiedReadPoolFull);
    }
    gauge.inc();
    remote.spawn(task_cell);
    Ok(())
}
```
- Why it matters: Delayed or rejected tasks are handled before queue capacity and eviction logic, so a task that never runs cannot evict already accepted work.
- When to use: Use for schedulers with resource groups, priority classes, or admission delays ahead of bounded queues.
- When not to use: Avoid for simple executors where admission and queue capacity are the same decision.
- Transferable principle: Perform admission before enqueue side effects, and release delay/accounting slots explicitly after sleeping.
- Related patterns: Semaphore Permit Attached To Message; Retryable Transaction Scope Wrapper.
- Risks / caveats: The delay guard must be released on every delayed path; otherwise admission capacity can leak under cancellation.
- Agentic coding guidance: When modifying scheduler admission, assert the order: reject/delay first, capacity/evict second, gauge increment immediately before spawn.
