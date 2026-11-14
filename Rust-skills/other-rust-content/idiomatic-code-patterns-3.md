# Idiomatic Code Patterns Part 3

Purpose: encyclopedia-grade extraction of idiomatic production-code patterns from Desktop repositories.

Assigned repo slice: `idiomatic-code-patterns-3-repos.txt`

Coverage status: initial scaffold created; extraction in progress.

## Extraction Protocol

- Capture repository evidence, not generic advice.
- Prefer exact file paths and concise snippets when they teach a reusable shape.
- Explain transferable principles across languages and stacks.
- Include when to use, when not to use, risks, and agent-generation guidance.
- Keep concepts deduplicated inside this part; cross-reference adjacent parts when needed.

## Repo Slice

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
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/LiveMCPBench`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/confido-exploration-01`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/lazy-tool`
- `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench`
- `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go`
- `/Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129`
- `/Users/amuldotexe/Desktop/personal-repos-lane/extract_twitter202304`
- `/Users/amuldotexe/Desktop/personal-repos-lane/games-001`
- `/Users/amuldotexe/Desktop/personal-repos-lane/journal-202401`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/graph-data-science-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-dotnet-driver-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-javascript-driver-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4rs-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-rs-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-jena-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/blazegraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-python-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/falkordb-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-pointers-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/janusgraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/materialize-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nebula-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/petgraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redisgraph-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sled-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tantivy-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/timely-dataflow-src`
- `/Users/amuldotexe/Desktop/personal-repos-lane/mermish`
- `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aaron-212__tree-sitter-mojo`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Akzestia__tree-sitter-cql`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-xml`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrendanJamesLynskey__CodingAgents_01_Repo_Understanding`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Crysthamus__tree-sitter-sln`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Flakebi__tree-sitter-llvm-mir`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GumTreeDiff__tree-sitter-parser`
- `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Himujjal__tree-sitter-svelte`
- ... 122 additional repos in slice file.

## Patterns

## Worker 3 Batch 1 Evidence Notes

- Codebase-memory smoke/index succeeded for `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity`, `/Users/amuldotexe/Desktop/oss-read-only/tao`, and `/Users/amuldotexe/Desktop/oss-read-only/parseltongue-rust-LLM-companion`.
- Follow-up direct `search_graph` attempts for those runs returned `project not found or not indexed` even when using the listed project names, so graph output was treated as smoke status only for this batch.
- For larger repos in this batch (`alien`, `arroyo`, `codex`, `great_expectations`, `materialize`, `risingwave`, `xarray`, `lazy-tool`, `neo4j-dotnet-driver-src`, Spring Boot samples), codebase-memory was not run in this pass; evidence below is from `rg --files`, `rg`, and direct source reads.

### Schema-Validated Resource Stack Builder
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien`; `packages/core/src/resource.ts`, `packages/core/src/stack.ts`.
- Language / framework / stack: TypeScript, generated schemas, cloud resource SDK.
- Evidence snippet:
```ts
public add(resource: Resource, lifecycle: ResourceLifecycle, options?: AddResourceOptions): this {
  const entry: ResourceEntry = { config: resource.config, lifecycle, dependencies: [] }
  if (options?.remoteAccess) {
    entry.remoteAccess = true
  }
  this._config.resources![resource.config.id] = entry
  return this
}

public build(): StackConfig {
  return StackSchema.parse(this._config)
}
```
- Why it matters: The builder gives users a fluent API but keeps final validation centralized in the generated schema, so invalid partial state does not leak as a deployable config.
- When to use: Use for SDKs that assemble infrastructure, workflow, or policy objects across many small calls.
- When not to use: Avoid when object construction is trivial and direct schema parsing is clearer.
- Transferable principle: Let builders accumulate intent, then use one schema-backed boundary to convert intent into a validated artifact.
- Related patterns: Cached Binding Context with Lifecycle Drain; Typed SQL WITH Option Conversion Traits.
- Risks / caveats: The internal `Partial<StackConfig>` means builder methods must preserve invariants until `build()`.
- Agentic coding guidance: When adding new resource types, add schema fields first, then builder affordances, and finish with tests that call `build()` rather than inspecting private builder state.

### Cached Binding Context With Lifecycle Drain
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/alien`; `packages/sdk/src/context.ts`.
- Language / framework / stack: TypeScript, gRPC SDK runtime.
- Evidence snippet:
```ts
private getBinding<T>(key: string, factory: () => T): T {
  let binding = this.bindingCache.get(key) as T | undefined
  if (!binding) {
    binding = factory()
    this.bindingCache.set(key, binding)
  }
  return binding
}

async shutdown(): Promise<void> {
  this.eventLoop?.stop()
  await this.waitUntilManager?.waitForAll()
  await this.waitUntilManager?.notifyDrainComplete(tasksDrained, allSuccess, errorMessage)
}
```
- Why it matters: Resource bindings are identity-stable per context, while shutdown drains background work before notifying the control plane.
- When to use: Use in runtimes where many typed clients share one transport channel and background tasks need graceful completion.
- When not to use: Avoid if bindings are stateful per operation or need fresh auth/materialized state every call.
- Transferable principle: Cache transport-bound facade objects by semantic key, and make lifecycle shutdown explicit rather than relying on process exit.
- Related patterns: Schema-Validated Resource Stack Builder; Shutdown Guard With Cascading Cancellation.
- Risks / caveats: Cache keys become part of correctness; inconsistent key naming can create duplicate clients.
- Agentic coding guidance: Generate accessors through a single `getBinding` helper, and add shutdown tests whenever introducing a new background task manager.

### Explicit Async State Machine Transitions
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/arroyo`; `crates/arroyo-controller/src/states/mod.rs`, `crates/arroyo-controller/src/states/running.rs`.
- Language / framework / stack: Rust, Tokio, async controller.
- Evidence snippet:
```rust
pub enum Transition {
    Stop,
    Advance(StateHolder),
}

#[async_trait::async_trait]
impl State for Running {
    async fn next(mut self: Box<Self>, ctx: &mut JobContext) -> Result<Transition, StateError> {
        tokio::select! {
            msg = ctx.rx.recv() => { /* config, restart, rescale */ }
            _ = tokio::time::sleep(Duration::from_millis(200)) => { /* progress */ }
            _ = log_interval.tick() => { /* telemetry */ }
        }
    }
}
```
- Why it matters: Each job state owns its event loop and returns an explicit transition, making controller behavior easier to audit than a single giant mutable loop.
- When to use: Use for long-running workflows with named lifecycle states, retries, terminal handling, and async external events.
- When not to use: Avoid for short request handlers where a plain enum plus `match` is enough.
- Transferable principle: Model lifecycle movement as returned transition values, not scattered mutation of a global status variable.
- Related patterns: Shutdown Guard With Cascading Cancellation; Trait-Driven Dev Service Tasks.
- Risks / caveats: State-specific files can hide shared invariants unless transitions are centrally declared and reviewed.
- Agentic coding guidance: When adding a state, update both the state module and transition declarations; do not smuggle new lifecycle paths through ad hoc status flags.

### Shutdown Guard With Cascading Cancellation
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/arroyo`; `crates/arroyo-server-common/src/shutdown.rs`.
- Language / framework / stack: Rust, Tokio, cancellation tokens, broadcast channels.
- Evidence snippet:
```rust
impl Drop for ShutdownGuard {
    fn drop(&mut self) {
        if !self.temporary {
            self.token.cancel();
        }
        let count = self.ref_count.fetch_sub(1, Ordering::SeqCst);
        if count == 1 {
            let _ = self.tx.send(());
        }
    }
}

pub fn spawn_task<F, T>(&self, name: &'static str, task: T) -> JoinHandle<Option<T::Output>>
where
    T: Future<Output = anyhow::Result<F>> + Send + 'static,
```
- Why it matters: Task ownership is represented by guard lifetimes, so cancellation and "all children dropped" notification are encoded in one reusable primitive.
- When to use: Use for services that spawn many related async tasks and need coordinated shutdown on errors or signals.
- When not to use: Avoid if task ownership is one-shot and simple `JoinSet` orchestration is enough.
- Transferable principle: Make cancellation a clonable capability and make task lifetime observable through reference counting.
- Related patterns: Cached Binding Context With Lifecycle Drain; Explicit Async State Machine Transitions.
- Risks / caveats: Dropping a non-temporary guard cancels the token, so cloning rules must be obvious to callers.
- Agentic coding guidance: Prefer adding child guards through provided methods instead of hand-cloning tokens and channels; this keeps shutdown accounting intact.

### Normalized Boundary Value Objects For Network Policy
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/codex`; `codex-rs/network-proxy/src/policy.rs`, `codex-rs/network-proxy/src/network_policy.rs`.
- Language / framework / stack: Rust, network proxy, policy enforcement.
- Evidence snippet:
```rust
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct Host(String);

impl Host {
    pub fn parse(input: &str) -> Result<Self> {
        let normalized = normalize_host(input);
        ensure!(!normalized.is_empty(), "host is empty");
        Ok(Self(normalized))
    }
}

pub enum NetworkDecision {
    Allow,
    Deny { reason: String, source: NetworkDecisionSource, decision: NetworkPolicyDecision },
}
```
- Why it matters: Host parsing, wildcard expansion, loopback detection, and audit decisions all pass through named types instead of raw strings.
- When to use: Use at security boundaries where normalization, logging, and policy semantics must be consistent.
- When not to use: Avoid wrapping every scalar in tiny apps where there is no boundary or policy distinction.
- Transferable principle: Parse and normalize once at the edge, then pass typed domain concepts internally.
- Related patterns: Filesystem Trait With Sandbox Adapters; Config Template Secret String Type.
- Risks / caveats: Boundary objects must preserve the raw information still needed for diagnostics or audit.
- Agentic coding guidance: Add tests for weird inputs first, including bracketed IPv6, trailing dots, ports, wildcard patterns, and empty hosts.

### Filesystem Trait With Sandbox Adapters
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/codex`; `codex-rs/file-system/src/lib.rs`, `codex-rs/exec-server/src/local_file_system.rs`, `codex-rs/exec-server/src/sandboxed_file_system.rs`.
- Language / framework / stack: Rust, async trait, executor filesystem, sandboxing.
- Evidence snippet:
```rust
#[async_trait]
pub trait ExecutorFileSystem: Send + Sync {
    async fn read_file(&self, path: &AbsolutePathBuf, sandbox: Option<&FileSystemSandboxContext>)
        -> FileSystemResult<Vec<u8>>;
    async fn write_file(&self, path: &AbsolutePathBuf, contents: Vec<u8>, sandbox: Option<&FileSystemSandboxContext>)
        -> FileSystemResult<()>;
}

if sandbox.is_some_and(FileSystemSandboxContext::should_run_in_sandbox) {
    Ok((self.sandboxed()?, sandbox))
} else {
    Ok((&self.unsandboxed, sandbox))
}
```
- Why it matters: Local, remote, and sandboxed filesystem operations share one contract, while the adapter decides which backend is safe for a request.
- When to use: Use when code must operate over local and remote workspaces or swap enforcement modes without changing callers.
- When not to use: Avoid if a direct `std::fs` call is the whole domain and no policy boundary exists.
- Transferable principle: Put environment-dependent side effects behind a small trait and pass policy context alongside the operation.
- Related patterns: Normalized Boundary Value Objects For Network Policy; Shutdown Guard With Cascading Cancellation.
- Risks / caveats: Async traits around filesystem operations can hide blocking work; direct implementations must use blocking-safe APIs where needed.
- Agentic coding guidance: Do not add new direct filesystem calls in higher-level modules; extend `ExecutorFileSystem` or its adapters so sandbox behavior remains uniform.

### Backend-Specific Execution Engine With Metric Bundling
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/great_expectations`; `great_expectations/execution_engine/execution_engine.py`, `great_expectations/execution_engine/pandas_execution_engine.py`, `great_expectations/execution_engine/sqlalchemy_execution_engine.py`, `great_expectations/validator/validation_graph.py`.
- Language / framework / stack: Python, data validation, Pandas, SQLAlchemy.
- Evidence snippet:
```python
class ExecutionEngine(ABC, Generic[TFilter]):
    recognized_batch_spec_defaults: Set[str] = set()
    def load_batch_data(self, batch_id: str, batch_data: BatchDataUnion) -> None:
        self._batch_manager.save_batch_data(batch_id=batch_id, batch_data=batch_data)

def resolve_metric_bundle(self, metric_fn_bundle) -> dict[MetricConfigurationID, Any]:
    return {}  # NO-OP for PandasExecutionEngine
```
```python
def _organize_metrics_by_domain(self, metric_fn_bundle, limit: int | None = None) -> list[dict]:
    domain_batches: dict[IDDictID, dict] = {}
    for bundled_metric_configuration in metric_fn_bundle:
        domain_id = domain_kwargs.to_id()
        domain_batches[domain_id]["select"].append(metric_fn.label(metric_to_resolve.metric_name))
```
- Why it matters: Immediate engines and deferred engines share an API, but only SQL-like engines batch metrics by compute domain.
- When to use: Use for libraries that expose one conceptual operation over backends with very different execution models.
- When not to use: Avoid if backend behavior diverges so far that a shared base class becomes a fake abstraction.
- Transferable principle: Share orchestration and cache contracts while letting each backend decide batching, filtering, and IO.
- Related patterns: Backend Plugin Discovery With Explicit Signatures; Picklable LRU File Managers.
- Risks / caveats: Base-class defaults like a no-op bundle resolver must be clearly documented or callers may assume unsupported optimization.
- Agentic coding guidance: When adding a backend, implement the minimal base contract first, then add backend-specific bundling only where it reduces real round trips.

### Config Template Secret String Type
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/great_expectations`; `great_expectations/datasource/fluent/config_str.py`, `tests/datasource/fluent/test_sqlite_datasource.py`.
- Language / framework / stack: Python, Pydantic, datasource configuration.
- Evidence snippet:
```python
class ConfigStr(SecretStr):
    def get_config_value(self, config_provider: _ConfigurationProvider) -> str:
        return config_provider.substitute_config(self.template_str)

    @classmethod
    def validate_template_str_format(cls, v: str) -> str | None:
        if cls.str_contains_config_template(v):
            return v
        raise ValueError("ConfigStr - contains no config template strings")
```
- Why it matters: Secret-bearing template strings are a distinct type, so runtime substitution and serialization behavior are explicit instead of convention-based.
- When to use: Use for config fields that may contain secret placeholders and need validation during assignment.
- When not to use: Avoid for ordinary strings where a placeholder requirement would reject valid non-secret values.
- Transferable principle: Encode special configuration semantics in the field type, not in scattered string checks.
- Related patterns: Normalized Boundary Value Objects For Network Policy; Type-Erased Session Variable Definitions With Typed Constraints.
- Risks / caveats: Over-strict validation can reject literal values; Great Expectations handles plain connection strings through alternate union types like `SqliteDsn`.
- Agentic coding guidance: If a field accepts both templated and concrete values, model it as a union and add assignment tests so updates keep the intended type.

### Type-Erased Session Variable Definitions With Typed Constraints
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/materialize`; `src/sql/src/session/vars/definitions.rs`, `src/sql/src/session/vars/constraints.rs`, `src/sql/src/session/vars/value.rs`.
- Language / framework / stack: Rust, SQL session variables.
- Evidence snippet:
```rust
pub struct VarDefinition {
    pub name: &'static UncasedStr,
    pub value: VarDefaultValue,
    pub constraint: Option<ValueConstraint>,
    parse: fn(VarInput) -> Result<Box<dyn Value>, VarParseError>,
    type_name: fn() -> Cow<'static, str>,
}

pub trait DomainConstraint: Debug + Send + Sync + 'static {
    type Value;
    fn check(&self, var: &dyn Var, v: &Self::Value) -> Result<(), VarError>;
}
```
- Why it matters: Materialize stores many heterogeneous variables in one registry without losing typed parsing and validation.
- When to use: Use for configuration registries with many value types, defaults, feature gates, and domain constraints.
- When not to use: Avoid if a simple typed struct with direct fields is sufficient and no dynamic lookup is needed.
- Transferable principle: Use type erasure at the registry boundary, but keep parsing and constraints attached to the original concrete type.
- Related patterns: Config Template Secret String Type; Typed SQL WITH Option Conversion Traits.
- Risks / caveats: Downcasts in type-erased constraints rely on registry construction being correct.
- Agentic coding guidance: When adding a variable, choose the concrete `Value` type first, then attach constraints through `with_constraint` rather than validating after parse elsewhere.

### Typed SQL WITH Option Conversion Traits
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/materialize`; `src/sql/src/plan/with_options.rs`.
- Language / framework / stack: Rust, SQL planner.
- Evidence snippet:
```rust
pub trait TryFromValue<T>: Sized {
    fn try_from_value(v: T) -> Result<Self, PlanError>;
    fn try_into_value(self, catalog: &dyn SessionCatalog) -> Option<T>;
    fn name() -> String;
}

impl TryFromValue<WithOptionValue<Aug>> for Secret {
    fn try_from_value(v: WithOptionValue<Aug>) -> Result<Self, PlanError> {
        match StringOrSecret::try_from_value(v)? {
            StringOrSecret::Secret(id) => Ok(Secret(id)),
            StringOrSecret::String(_) => sql_bail!("must provide a secret value"),
        }
    }
}
```
- Why it matters: SQL option parsing becomes a set of typed conversions, including reverse conversion for display or catalog serialization.
- When to use: Use when a DSL or config format has many syntactic value forms that must map to domain-specific types.
- When not to use: Avoid if parsing is one-off and reverse conversion is never needed.
- Transferable principle: Give each target type responsibility for accepting, rejecting, naming, and rendering its option value.
- Related patterns: Type-Erased Session Variable Definitions With Typed Constraints; Schema-Validated Resource Stack Builder.
- Risks / caveats: Error messages are only as good as each conversion's `name()` and failure path.
- Agentic coding guidance: Add conversion impls near existing domain conversions and test both valid syntax and wrong-kind syntax such as string where secret is required.

### Trait-Driven Dev Service Tasks
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/risingwave`; `src/risedevtool/src/task/mod.rs`, `src/risedevtool/src/task/docker_service.rs`, `src/risedevtool/src/task/task_tcp_ready_check.rs`.
- Language / framework / stack: Rust, local dev orchestration, Docker, tmux.
- Evidence snippet:
```rust
pub trait Task: 'static + Send {
    fn execute(&mut self, ctx: &mut ExecuteContext<impl std::io::Write>) -> anyhow::Result<()>;
    fn id(&self) -> String { "<task>".into() }
}

pub trait DockerServiceConfig: Send + 'static {
    fn id(&self) -> String;
    fn is_user_managed(&self) -> bool;
    fn image(&self) -> String;
    fn ports(&self) -> Vec<(String, String)> { vec![] }
}
```
- Why it matters: Service-specific configuration is separated from the common mechanics of logs, progress bars, tmux commands, Docker lifecycle, and readiness checks.
- When to use: Use for local environment launchers that coordinate many services with shared operational behavior.
- When not to use: Avoid for a single service wrapper where traits add indirection without reuse.
- Transferable principle: Split "what service is this" from "how services are started, logged, checked, and stopped."
- Related patterns: Explicit Async State Machine Transitions; Macro Registry For Connector Variants.
- Risks / caveats: Command construction and environment variables are still side-effect heavy; tests need seams around command execution.
- Agentic coding guidance: Add new services by implementing config traits and composing existing ready-check tasks before adding bespoke orchestration code.

### Macro Registry For Connector Variants
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/risingwave`; `src/connector/src/macros.rs`.
- Language / framework / stack: Rust, connector framework, macros.
- Evidence snippet:
```rust
macro_rules! for_all_classified_sources {
    ($macro:path $(, $extra_args:tt)*) => {
        $macro! {
            { { Mysql }, { Postgres }, { Citus }, { Mongodb }, { SqlServer } },
            {
                { Kafka, $crate::source::kafka::KafkaProperties, $crate::source::kafka::KafkaSplit },
                { Pulsar, $crate::source::pulsar::PulsarProperties, $crate::source::pulsar::PulsarSplit }
            }
            $(,$extra_args)*
        }
    };
}
```
- Why it matters: The list of source variants, property types, and split types is centralized, then reused to generate dispatch code.
- When to use: Use when a Rust system has many typed variants that must stay in sync across enum matching, string matching, and registration.
- When not to use: Avoid when normal enums and direct matches are small enough to read and maintain manually.
- Transferable principle: Centralize variant inventories when the same matrix drives multiple code-generation sites.
- Related patterns: Trait-Driven Dev Service Tasks; Type-Erased Session Variable Definitions With Typed Constraints.
- Risks / caveats: Macros can obscure generated code and make compiler errors harder to read.
- Agentic coding guidance: Before adding a connector, update the central macro inventory and compile all generated dispatch sites; do not add a one-off match arm elsewhere.

### Platform Facade With Private cfg Backends
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/tao`; `src/lib.rs`, `src/platform_impl/mod.rs`, `src/event_loop.rs`, `tests/send_objects.rs`, `tests/sync_object.rs`.
- Language / framework / stack: Rust, cross-platform windowing library.
- Evidence snippet:
```rust
#[cfg(target_os = "windows")]
#[path = "windows/mod.rs"]
mod platform;
#[cfg(target_os = "macos")]
#[path = "macos/mod.rs"]
mod platform;

pub use platform::*;

compile_error!("The platform you're compiling for is not supported by tao");
```
```rust
pub struct EventLoop<T: 'static> {
  pub(crate) event_loop: platform_impl::EventLoop<T>,
  pub(crate) _marker: ::std::marker::PhantomData<*mut ()>, // Not Send nor Sync
}
```
- Why it matters: The public API stays stable while target-specific implementation modules are selected at compile time, with trait guarantees checked by compile tests.
- When to use: Use for libraries that must expose one API over OS-specific backends.
- When not to use: Avoid if runtime plugin selection is required or targets can be discovered dynamically.
- Transferable principle: Hide platform modules behind a public facade and make unsupported targets fail at compile time.
- Related patterns: Filesystem Trait With Sandbox Adapters; Backend Plugin Discovery With Explicit Signatures.
- Risks / caveats: Public types must deliberately encode Send/Sync behavior; accidental auto-traits can become unsound API promises.
- Agentic coding guidance: When touching platform-specific internals, run or add compile tests for Send/Sync and serialization behavior of public wrapper types.

### Picklable LRU File Managers
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/xarray`; `xarray/backends/file_manager.py`.
- Language / framework / stack: Python, scientific IO, backend resource management.
- Evidence snippet:
```python
FILE_CACHE: LRUCache[Any, Closable] = LRUCache(
    maxsize=OPTIONS["file_cache_maxsize"], on_evict=lambda k, v: v.close()
)

class CachingFileManager(FileManager[T_File]):
    def _acquire_with_cache_info(self, needs_lock: bool = True) -> tuple[T_File, bool]:
        with self._optional_lock(needs_lock):
            try:
                file = self._cache[self._key]
            except KeyError:
                file = self._opener(*self._args, **kwargs)
                self._cache[self._key] = file
                return file, False
```
- Why it matters: Many dataset objects can safely share and reacquire file handles without leaking descriptors or breaking multiprocessing.
- When to use: Use for data libraries that create many logical objects backed by fewer expensive open resources.
- When not to use: Avoid for short-lived scripts where a normal context manager is simpler and sufficient.
- Transferable principle: Decouple logical object lifetime from physical resource lifetime with a small manager that owns cache, lock, and close behavior.
- Related patterns: Backend-Specific Execution Engine With Metric Bundling; Backend Plugin Discovery With Explicit Signatures.
- Risks / caveats: Cache keys must include enough opener arguments to prevent handle aliasing across different files or modes.
- Agentic coding guidance: Never hand-close a file acquired from a manager; add backend code that calls manager `close()` so the global cache stays coherent.

### Backend Plugin Discovery With Explicit Signatures
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/xarray`; `xarray/backends/plugins.py`, `xarray/backends/common.py`.
- Language / framework / stack: Python, importlib entry points, optional backend plugins.
- Evidence snippet:
```python
def detect_parameters(open_dataset: Callable) -> tuple[str, ...]:
    signature = inspect.signature(open_dataset)
    for name, param in signature.parameters.items():
        if param.kind in (inspect.Parameter.VAR_KEYWORD, inspect.Parameter.VAR_POSITIONAL):
            raise TypeError("All the parameters ... should be explicit")
        if name != "self":
            parameters_list.append(name)

@functools.lru_cache(maxsize=1)
def list_engines() -> dict[str, BackendEntrypoint]:
    entrypoints = entry_points(group="xarray.backends")
    return build_engines(entrypoints)
```
- Why it matters: Third-party backends can register themselves, while xarray rejects ambiguous `*args` and `**kwargs` APIs that are hard to document or validate.
- When to use: Use for plugin ecosystems where optional dependencies should be discovered lazily and cached.
- When not to use: Avoid if all implementations are built in and the extension surface is not public.
- Transferable principle: Let plugins register through standard packaging, but enforce explicit callable signatures at load time.
- Related patterns: Platform Facade With Private cfg Backends; Picklable LRU File Managers.
- Risks / caveats: Entry point loading can fail because optional dependencies are missing; xarray warns and continues.
- Agentic coding guidance: When adding a backend plugin, make `open_dataset` parameters explicit and add a refresh path for tests that mutate installed engines.

### Fixed-Capacity no_std Buffer With Invariant Tests
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-fmt-fixed-capacity`; `src/lib.rs`, `src/error.rs`, `tests/write_to_fixed_buffer_tests.rs`, `tests/property_based_fuzzing_tests.rs`.
- Language / framework / stack: Rust, `no_std`, const generics, `core::fmt::Write`, quickcheck.
- Evidence snippet:
```rust
#![no_std]
#![deny(unsafe_code)]

pub struct FixedBuffer<const N: usize> {
    buffer: [u8; N],
    length: usize,
}

pub fn write_bytes_to_buffer_safe(&mut self, bytes: &[u8]) -> Result<()> {
    let remaining = self.capacity_remaining_bytes_available();
    if bytes.len() > remaining {
        return Err(FixedBufferError::CapacityExceeded { bytes_needed: bytes.len(), bytes_available: remaining });
    }
    self.buffer[self.length..self.length + bytes.len()].copy_from_slice(bytes);
    self.length += bytes.len();
    Ok(())
}
```
- Why it matters: Stack allocation, capacity checks, UTF-8 invariant preservation, and property tests make the zero-allocation claim concrete.
- When to use: Use for embedded, `no_std`, logging, formatting, or protocol code where heap allocation is forbidden or expensive.
- When not to use: Avoid if dynamic strings are acceptable and `String` makes the code simpler.
- Transferable principle: State invariants in the type, enforce them at every write boundary, and use property tests for "always" claims.
- Related patterns: Config Template Secret String Type; Type-Erased Session Variable Definitions With Typed Constraints.
- Risks / caveats: `as_str()` uses an invariant-based `expect`; any future byte-writing path must preserve UTF-8.
- Agentic coding guidance: Add a property test before adding mutation methods; confirm failed writes leave the buffer unchanged.

### Endpoint-Per-File Router With Structured HTTP Errors
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/parseltongue-rust-LLM-companion`; `crates/pt08-http-code-query-server/src/route_definition_builder_module.rs`, `crates/pt08-http-code-query-server/src/http_endpoint_handler_modules/mod.rs`, `crates/pt08-http-code-query-server/src/structured_error_handling_types.rs`.
- Language / framework / stack: Rust, Axum, thiserror.
- Evidence snippet:
```rust
Router::new()
    .route("/server-health-check-status", get(server_health_check_handler::handle_server_health_check_status))
    .route("/codebase-statistics-overview-summary", get(codebase_statistics_overview_handler::handle_codebase_statistics_overview_summary))
    .route("/smart-context-token-budget", get(smart_context_token_budget_handler::handle_smart_context_token_budget))
    .with_state(state)
```
```rust
impl IntoResponse for HttpServerErrorTypes {
    fn into_response(self) -> Response {
        let (status, error_message) = match &self {
            HttpServerErrorTypes::EntityNotFoundQueryError(_) => (StatusCode::NOT_FOUND, self.to_string()),
            HttpServerErrorTypes::InvalidRequestParameterError(_) => (StatusCode::BAD_REQUEST, self.to_string()),
            _ => (StatusCode::INTERNAL_SERVER_ERROR, self.to_string()),
        };
        (status, Json(json!({ "success": false, "error": error_message }))).into_response()
    }
}
```
- Why it matters: Routes are discoverable in one builder, while each endpoint keeps handler code isolated and shares one error-to-response policy.
- When to use: Use for small and medium HTTP APIs where endpoint behavior should stay file-local but routing should be auditable.
- When not to use: Avoid if endpoints are generated from an OpenAPI framework or need deeply nested routers by domain.
- Transferable principle: Centralize route registration and error conversion; localize endpoint implementation.
- Related patterns: Token-Budget Smart Context Greedy Selection; Normalized Boundary Value Objects For Network Policy.
- Risks / caveats: A central route file can grow long; split by route groups once the list stops being scannable.
- Agentic coding guidance: When adding an endpoint, create the handler module, add it to `mod.rs`, register it in the route builder, and return the shared error type.

### Token-Budget Smart Context Greedy Selection
- Where found: `/Users/amuldotexe/Desktop/oss-read-only/parseltongue-rust-LLM-companion`; `crates/pt08-http-code-query-server/src/http_endpoint_handler_modules/smart_context_token_budget_handler.rs`.
- Language / framework / stack: Rust, Axum, graph traversal, context engineering.
- Evidence snippet:
```rust
scored_entities.sort_by(|a, b| {
    b.relevance_score.partial_cmp(&a.relevance_score).unwrap_or(std::cmp::Ordering::Equal)
});

let mut selected = Vec::new();
let mut used_tokens = 0;
for entity in scored_entities {
    if used_tokens + entity.estimated_tokens <= budget {
        used_tokens += entity.estimated_tokens;
        selected.push(entity);
    }
}
```
- Why it matters: The endpoint turns a graph neighborhood into an explicit relevance-ranked context set bounded by token budget.
- When to use: Use for code intelligence, retrieval, review prep, or agent context selection where "everything related" is too large.
- When not to use: Avoid when exact optimal packing is required; this is a greedy heuristic.
- Transferable principle: Score candidates by task relevance, sort, and greedily select until the context budget is exhausted.
- Related patterns: Endpoint-Per-File Router With Structured HTTP Errors; Backend-Specific Execution Engine With Metric Bundling.
- Risks / caveats: Token estimation and relevance weights are heuristics; validate with real downstream task quality.
- Agentic coding guidance: When changing weights or depth limits, add examples that show selected entities and tokens used for a known focus node.

### Inspect View With Trust Flags
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/lazy-tool`; `internal/catalog/inspect_view.go`, `internal/app/sourceregistry.go`, `internal/catalog/inspect_view_test.go`.
- Language / framework / stack: Go, SQLite-backed catalog, MCP/tool registry.
- Evidence snippet:
```go
type InspectView struct {
    Record models.CapabilityRecord `json:"record"`
    Source *models.Source `json:"source,omitempty"`
    LastReindex *ReindexHealthView `json:"last_reindex,omitempty"`
    SourceInConfig bool `json:"source_in_config"`
    LastReindexRecorded bool `json:"last_reindex_recorded"`
}

if src, ok := reg.Get(rec.SourceID); ok {
    cp := src
    v.Source = &cp
    v.SourceInConfig = true
}
```
- Why it matters: The inspect API tells callers whether joined config and health data exist, rather than making absence ambiguous.
- When to use: Use for diagnostic views that merge persisted records, live config, and operational health.
- When not to use: Avoid if a plain domain object is enough and consumers do not need provenance or trust state.
- Transferable principle: Add explicit trust/provenance flags when joining state from sources with different freshness guarantees.
- Related patterns: Schema-Validated Resource Stack Builder; Backend Plugin Discovery With Explicit Signatures.
- Risks / caveats: Flags must be kept consistent with omitted optional fields or clients will misinterpret partial data.
- Agentic coding guidance: When adding fields to inspect views, add tests for present and missing joins, not just the happy path.

### Exponential Retry With Jitter And Semantic Tests
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-dotnet-driver-src`; `Neo4j.Driver/Neo4j.Driver/Internal/AsyncRetryLogic.cs`, `Neo4j.Driver/Neo4j.Driver.Reactive/Internal/RxRetryLogic.cs`, `Neo4j.Driver/Neo4j.Driver.Tests/AsyncRetryLogicTests.cs`.
- Language / framework / stack: C#, .NET async, Reactive Extensions.
- Evidence snippet:
```csharp
catch (Exception e) when (e.CanBeRetried())
{
    exceptions.Add(e);
    shouldRetry = retryCount < 2 || timer.ElapsedMilliseconds < _maxRetryTimeMs;
    if (shouldRetry)
    {
        delay = TimeSpan.FromMilliseconds(ComputeDelayWithJitter(delayMs));
        await Task.Delay(delay).ConfigureAwait(false);
        delayMs *= _multiplier;
    }
}
```
- Why it matters: Retry behavior is centralized, exception-gated, jittered, logged, and covered by tests for non-transient errors, timeout, logging, and at-least-twice retry semantics.
- When to use: Use for database drivers, message clients, and external service calls with known transient error classes.
- When not to use: Avoid retrying non-idempotent operations unless the protocol guarantees transaction safety.
- Transferable principle: Retry policy should be a named component with semantic tests, not a loop copied into every call site.
- Related patterns: Shutdown Guard With Cascading Cancellation; Trait-Driven Dev Service Tasks.
- Risks / caveats: Jitter based on a fresh random source is harder to test deterministically; keep tests focused on semantics, not exact delay values.
- Agentic coding guidance: Before adding retries, define which exceptions are retryable and write tests proving non-retryable failures are attempted once.

### Feign Client Fallback For Degraded Cross-Service Calls
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/.research-corpus/springboot-java/repos/sqshq__piggymetrics`; `account-service/src/main/java/com/piggymetrics/account/client/StatisticsServiceClient.java`, `account-service/src/main/java/com/piggymetrics/account/client/StatisticsServiceClientFallback.java`, `account-service/src/main/java/com/piggymetrics/account/controller/ErrorHandler.java`.
- Language / framework / stack: Java, Spring Boot, Spring Cloud OpenFeign.
- Evidence snippet:
```java
@FeignClient(name = "statistics-service", fallback = StatisticsServiceClientFallback.class)
public interface StatisticsServiceClient {
    @RequestMapping(method = RequestMethod.PUT, value = "/statistics/{accountName}", consumes = MediaType.APPLICATION_JSON_UTF8_VALUE)
    void updateStatistics(@PathVariable("accountName") String accountName, Account account);
}

@Component
public class StatisticsServiceClientFallback implements StatisticsServiceClient {
    public void updateStatistics(String accountName, Account account) {
        LOGGER.error("Error during update statistics for account: {}", accountName);
    }
}
```
- Why it matters: A cross-service dependency can fail without crashing the account service path, while the degradation is visible in logs.
- When to use: Use for non-critical downstream updates where eventual consistency or loss-tolerant behavior is acceptable.
- When not to use: Avoid for critical writes where silent fallback would hide data loss or violate user expectations.
- Transferable principle: Put degraded behavior beside the client contract and make the failure mode explicit.
- Related patterns: Exponential Retry With Jitter And Semantic Tests; Backend-Specific Execution Engine With Metric Bundling.
- Risks / caveats: Logging-only fallback can lose work permanently unless paired with retry queues or reconciliation.
- Agentic coding guidance: When generating Feign clients, ask whether each method needs fail-fast, fallback, retry, or enqueue-on-failure behavior; do not default to a no-op fallback.

## Worker 3 Batch 2 - Prioritized High-Signal Repos

CodeGraphContext status: smoke indexing was attempted with `/Users/amuldotexe/.codex/skills/codegraphcontext-evidence-reader/scripts/scan_current_repo_only.sh /Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter`. It printed the target output directory `/tmp/codex-code-intel/codegraphcontext/tree-sitter__tree-sitter-20260706-230210` and then produced no further output during repeated 30 second polls. Worker 3 terminated only that smoke process tree after roughly two minutes to avoid leaving a long-running background job. All claims below are based on direct source reads.

### Conservative Boolean Formula Prefiltering
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__semgrep`; `src/prefiltering/Formula.ml`, `src/prefiltering/Analyze_rule.ml`, `src/prefiltering/Predicate.ml`.
- Language / framework / stack: OCaml, Semgrep rule prefiltering, Pcre2.
- Evidence snippet:
```ocaml
type 'a t =
  | And of 'a t list
  | Or of 'a t list
  | Pred of 'a

let rec map_opt f = function
  | And xs -> List.filter_map (map_opt f) xs |> and_
  | Or xs -> (
      match List_.map (map_opt f) xs |> Common2.option_all with
      | Some xs -> or_ xs
      | None -> None)
  | Pred x -> f x
```
- Why it matters: Unknown conditions are not treated the same inside `AND` and `OR`; the analyzer preserves soundness by dropping true-like terms from conjunctions but collapsing disjunctions to unknown when any branch cannot be handled.
- When to use: Use for static-analysis prefilters, query planners, and rule engines where cheap textual predicates can avoid expensive full matching.
- When not to use: Avoid when false negatives are unacceptable and you cannot model unknown predicate behavior conservatively.
- Transferable principle: Represent filter logic as an algebra first, then lower only the safe subset into executable predicates.
- Related patterns: Type-Safe Set Operation Helpers; Capability Tokens Plus Static Forbid Rules.
- Risks / caveats: Simplification semantics are subtle; an incorrect `OR` simplification can silently drop real matches.
- Agentic coding guidance: When adding a prefilter optimization, write down whether `None` means false, true, or unknown before changing boolean combinators.

### Predicate Objects With Fast Literal And Regex Paths
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__semgrep`; `src/prefiltering/Predicate.ml`, `src/prefiltering/Analyze_rule.ml`.
- Language / framework / stack: OCaml, string search, Pcre2 regex.
- Evidence snippet:
```ocaml
type t =
  | String of string
  | Regex of Pcre2_.t

let eval predicate content =
  match predicate with
  | String needle -> Base.String.Search_pattern.(matches (create needle) content)
  | Regex re -> Pcre2_.unanchored_match ~on_error:true re content
```
- Why it matters: Literal containment and regex evaluation stay in a single predicate abstraction while retaining the faster path for simple strings.
- When to use: Use when matching engines can cheaply reject most inputs with literals but still need expressive regex fallback.
- When not to use: Avoid when regex compilation cost dominates and the compiled form cannot be cached.
- Transferable principle: Keep the public predicate interface uniform, but preserve specialized execution paths internally.
- Related patterns: Conservative Boolean Formula Prefiltering; Byte Size CLI Param Parser With Units.
- Risks / caveats: `~on_error:true` can turn some regex errors into matches; document whether that is conservative behavior or user-visible tolerance.
- Agentic coding guidance: If a rule accepts both literals and regexes, do not normalize everything to regex by default; keep cheap literal evaluation visible.

### Type-Safe Set Operation Helpers
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__semgrep`; `cli/src/semgrep/safe_set.py`.
- Language / framework / stack: Python, mypy typing, immutable set helpers.
- Evidence snippet:
```python
T = TypeVar("T")

def intersection(a: FrozenSet[T], b: Collection[T]) -> FrozenSet[T]:
    return a.intersection(b)

def union(a: FrozenSet[T], b: Collection[T]) -> FrozenSet[T]:
    return a.union(b)
```
- Why it matters: Tiny wrappers force the type checker to verify set operation element types instead of relying on permissive built-in method stubs.
- When to use: Use around standard library APIs whose type hints are broader than the project wants to allow.
- When not to use: Avoid wrapping every trivial operation; reserve it for places where the type checker otherwise misses real mistakes.
- Transferable principle: A small helper can make a weakly typed library edge stricter for the rest of the codebase.
- Related patterns: Conservative Boolean Formula Prefiltering; Diagnostic Context Combinators.
- Risks / caveats: Helper names must remain obvious, or they become indirection for no practical gain.
- Agentic coding guidance: When mypy cannot express a local invariant through a stdlib method, prefer a narrow helper with one type variable over repeated casts.

### Byte Size CLI Param Parser With Units
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/semgrep__semgrep`; `cli/src/semgrep/bytesize.py`.
- Language / framework / stack: Python, Click CLI, typed parsing.
- Evidence snippet:
```python
UNITS = {
    "": 1,
    "B": 1,
    "KIB": 2**10,
    "MIB": 2**20,
    "KB": 10**3,
    "MB": 10**6,
}

def parse_size(input: str) -> int:
    import re

    s = input.upper()
    s = re.sub(r"([BKMGT][A-Z]*)", r" \1", s)
    tokens = [sub.strip() for sub in s.split()]
    n = len(tokens)
    if n == 1:
        number = tokens[0]
        unit = ""
    elif n == 2:
        number, unit = tokens
    else:
        raise ValueError(f"Invalid representation for a number of bytes: '{input}'")
    if unit in UNITS:
        return int(float(number) * UNITS[unit])
    else:
        raise ValueError(f"Invalid representation for a number of bytes: '{input}'")

class ByteSizeType(click.ParamType):
    name = "BYTES"
```
- Why it matters: Human CLI input like `10MB` becomes a normalized integer at the boundary, so downstream code does not repeat unit parsing.
- When to use: Use for CLI options that humans naturally express with units, durations, percentages, memory sizes, or rates.
- When not to use: Avoid if ambiguous suffixes or locale-specific formats need a full parsing library.
- Transferable principle: Parse and validate user-friendly input once at the command boundary, then pass domain-native values internally.
- Related patterns: Predicate Objects With Fast Literal And Regex Paths; Bounded Config Discovery Ladder.
- Risks / caveats: Unit suffix policy must be explicit; decimal vs binary units can surprise users.
- Agentic coding guidance: When adding CLI flags, ask what type the application actually needs and move conversion into the CLI parameter type.

### Capability Tokens Plus Static Forbid Rules
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/opengrep__opengrep`; `TCB/Cap.ml`, `TCB/CapSys.ml`, `TCB/CapUnix.ml`, `TCB/forbid_exec.jsonnet`, `TCB/No_TCB.ml`.
- Language / framework / stack: OCaml, Semgrep/OpenGrep rules, trusted computing base.
- Evidence snippet:
```ocaml
type cap = unit

module Network = struct type t = cap end
module FS = struct type root_r = cap type root_w = cap type tmp = cap end
module Exec = struct type t = cap end

type fs = < root ; root_all ; cwd ; home ; dotfiles ; tmp ; files_argv >
type exec = < exec : Exec.t >
```
```ocaml
let execvp _caps = Unix.execvp
let create_process _caps = Unix.create_process
let system _caps = Unix.system
```
- Why it matters: Dangerous operations require explicit capability arguments, while static rules forbid direct calls to raw process APIs.
- When to use: Use when a codebase has security-sensitive filesystem, network, process, or shell access that should be visible in function signatures.
- When not to use: Avoid if the language cannot prevent easy construction of the capability token and there is no lint/static rule backup.
- Transferable principle: Pair type-level permission markers with repository-level lint rules so bypasses are easy to detect.
- Related patterns: Conservative Boolean Formula Prefiltering; Public ABI Version Gate And Opaque Handles.
- Risks / caveats: In OCaml this pattern depends on module abstraction and social discipline; implementation files inside the TCB can still perform privileged operations.
- Agentic coding guidance: When generating code near process execution, route through the capability wrapper module and never call `Unix.system` or `Sys.command` directly.

### Streaming JSON-RPC Reader State Machine
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__biome`; `packages/@biomejs/backend-jsonrpc/src/transport.ts`.
- Language / framework / stack: TypeScript, JSON-RPC, Node streams.
- Evidence snippet:
```ts
enum ReaderStateKind {
	Header = 0,
	Body = 1,
}

private processIncoming(data: Buffer) {
	this.pendingData = Buffer.concat([this.pendingData, data]);
	while (this.pendingData.length > 0) {
		if (this.readerState.kind === ReaderStateKind.Header) {
			const lineBreakIndex = this.pendingData.indexOf("\n");
			if (lineBreakIndex < 0) {
				break;
			}
			const header = this.pendingData.subarray(0, lineBreakIndex + 1);
			this.pendingData = this.pendingData.subarray(lineBreakIndex + 1);
			this.processIncomingHeader(this.readerState, header.toString("utf-8"));
		} else if (this.pendingData.length >= this.readerState.contentLength) {
			const body = this.pendingData.subarray(0, this.readerState.contentLength);
			this.pendingData = this.pendingData.subarray(this.readerState.contentLength);
			this.processIncomingBody(body);
			this.readerState = {
				kind: ReaderStateKind.Header,
			};
		} else {
			break;
		}
	}
}
```
- Why it matters: Stream chunks can split headers and bodies arbitrarily; an explicit reader state prevents partial reads from corrupting message boundaries.
- When to use: Use for LSP, JSON-RPC, SMTP-like, or custom protocols with length-prefixed frames over byte streams.
- When not to use: Avoid if a mature framing library already handles buffering, backpressure, and malformed input.
- Transferable principle: Treat byte-stream protocols as state machines, not as one-read-per-message conveniences.
- Related patterns: Public ABI Version Gate And Opaque Handles; Opaque Text Offsets And Ranges.
- Risks / caveats: The parser must bound pending data and handle malformed headers to avoid memory growth or stuck connections.
- Agentic coding guidance: When editing streaming protocol code, test split headers, split bodies, multiple messages in one chunk, and invalid content lengths.

### Pending Request Map For JSON-RPC Correlation
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__biome`; `packages/@biomejs/backend-jsonrpc/src/transport.ts`.
- Language / framework / stack: TypeScript, JSON-RPC client transport.
- Evidence snippet:
```ts
request(method: string, params: unknown): Promise<any> {
	return new Promise((resolve, reject) => {
		const id = this.nextRequestId++;
		this.pendingRequests.set(id, { resolve, reject });
		this.sendMessage({
			jsonrpc: "2.0",
			id,
			method,
			params,
		});
	});
}
```
- Why it matters: Outgoing request IDs and pending resolvers make asynchronous responses deterministic even when replies arrive out of order.
- When to use: Use for multiplexed request/response protocols where many calls share one connection.
- When not to use: Avoid for fire-and-forget notification-only protocols where request correlation adds unneeded state.
- Transferable principle: Correlation IDs belong at the transport boundary, with one map owning request lifecycle.
- Related patterns: Streaming JSON-RPC Reader State Machine; Diagnostic Context Combinators.
- Risks / caveats: Pending maps need timeout or connection-close cleanup, otherwise lost responses can leak promises.
- Agentic coding guidance: When adding a new transport request path, verify that success, error, missing response, and connection close all remove the pending entry.

### Opaque Text Offsets And Ranges
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__biome`; `crates/biome_text_size/src/size.rs`, `crates/biome_text_size/src/range.rs`.
- Language / framework / stack: Rust, text model primitives.
- Evidence snippet:
```rust
#[derive(Clone, Copy, Default, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct TextSize {
    pub(crate) raw: u32,
}

#[repr(C)]
pub struct TextRange {
    start: TextSize,
    end: TextSize,
}
```
- Why it matters: Offsets and ranges are not raw integers at call sites, so APIs communicate byte-offset semantics and enforce basic range invariants.
- When to use: Use for parsers, editors, diagnostics, and formatters that pass source offsets across many layers.
- When not to use: Avoid if offsets have multiple units in the same domain and the wrapper name does not encode which unit is used.
- Transferable principle: Make primitive domain units opaque before they spread through public APIs.
- Related patterns: Diagnostic Context Combinators; Public ABI Version Gate And Opaque Handles.
- Risks / caveats: `u32` limits maximum file size; conversion from `usize` must stay fallible.
- Agentic coding guidance: When generating diagnostics or text edits, convert into `TextSize`/`TextRange` at the boundary instead of carrying naked `usize` offsets.

### Diagnostic Context Combinators
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__biome`; `crates/biome_diagnostics/src/context.rs`.
- Language / framework / stack: Rust, diagnostics, extension traits.
- Evidence snippet:
```rust
pub trait DiagnosticExt: internal::Sealed + Sized {
    fn context<M>(self, message: M) -> Error
    where
        Self: 'static,
        M: fmt::Display + 'static,
        Error: From<internal::ContextDiagnostic<M, Self>>;

    fn with_category(self, category: &'static Category) -> Error
    where
        Error: From<internal::CategoryDiagnostic<Self>>;

    fn with_file_path(self, path: impl AsResource) -> Error
    where
        Error: From<internal::FilePathDiagnostic<Self>>;

    fn with_file_span(self, span: impl AsSpan) -> Error
    where
        Error: From<internal::FileSpanDiagnostic<Self>>;

    fn with_severity(self, severity: Severity) -> Error
    where
        Error: From<internal::SeverityDiagnostic<Self>>;
}
```
- Why it matters: Errors accumulate category, file path, span, severity, and message context without losing the original diagnostic source.
- When to use: Use in CLI, compiler, linter, or language-server code where user-facing errors need progressive annotation.
- When not to use: Avoid when a simple internal error enum is enough and additional context would never be displayed or logged.
- Transferable principle: Build context attachment into error types so call sites enrich failures instead of replacing them.
- Related patterns: Opaque Text Offsets And Ranges; Type-Safe Set Operation Helpers.
- Risks / caveats: Chained contexts can become noisy; make sure rendered diagnostics have a clear primary message.
- Agentic coding guidance: When adding `?` propagation in diagnostic-heavy code, check whether the boundary should add category, path, span, or severity before returning.

### Generated Workspace API From Codegen Boundary
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/biomejs__biome`; `packages/@biomejs/backend-jsonrpc/src/workspace.ts`, `xtask/codegen`.
- Language / framework / stack: TypeScript, generated JSON-RPC client API, Rust xtask codegen.
- Evidence snippet:
```ts
// Generated file, do not edit by hand, see `xtask/codegen`
import type { Transport } from "./transport";

export interface SupportsFeatureParams {
	features: FeatureName;
	inlineConfig?: Configuration;
}
```
- Why it matters: A large typed API surface is generated rather than manually mirrored, reducing drift between protocol definitions and client code.
- When to use: Use for protocol DTOs, config schemas, RPC clients, and bindings whose source of truth lives elsewhere.
- When not to use: Avoid codegen for small stable APIs where the generated layer is harder to inspect than handwritten code.
- Transferable principle: Put generated files behind an explicit regeneration command and keep hand edits out of the generated surface.
- Related patterns: Polyglot Binding Specification With Generated Parity Tests; Public ABI Version Gate And Opaque Handles.
- Risks / caveats: Generated files can hide bad abstractions; reviewers need to inspect the generator and representative output.
- Agentic coding guidance: If a generated file says not to edit by hand, locate the generator and patch the source schema or template instead.

### Public ABI Version Gate And Opaque Handles
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter`; `lib/include/tree_sitter/api.h`, `lib/binding_rust/lib.rs`.
- Language / framework / stack: C public ABI, Rust FFI binding.
- Evidence snippet:
```c
#define TREE_SITTER_LANGUAGE_VERSION 15
#define TREE_SITTER_MIN_COMPATIBLE_LANGUAGE_VERSION 13

typedef struct TSLanguage TSLanguage;
typedef struct TSParser TSParser;
typedef struct TSTree TSTree;
```
```rust
pub const LANGUAGE_VERSION: usize = ffi::TREE_SITTER_LANGUAGE_VERSION as usize;
pub const MIN_COMPATIBLE_LANGUAGE_VERSION: usize =
    ffi::TREE_SITTER_MIN_COMPATIBLE_LANGUAGE_VERSION as usize;
```
- Why it matters: Consumers can check generated language ABI compatibility without depending on private parser internals.
- When to use: Use for libraries with generated plugins, shared objects, FFI consumers, or independently versioned language grammars.
- When not to use: Avoid if all components are statically linked and released in lockstep with no external ABI boundary.
- Transferable principle: Expose stable opaque handles and explicit version constants at public boundaries.
- Related patterns: Capability Tokens Plus Static Forbid Rules; Generated Workspace API From Codegen Boundary.
- Risks / caveats: ABI constants must be updated intentionally and documented when compatibility changes.
- Agentic coding guidance: When binding C libraries, mirror version constants and opaque handle types instead of reaching into private structs.

### Macro-Generic C Arrays With Strict-Aliasing-Aware Helpers
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter`; `lib/src/array.h`.
- Language / framework / stack: C, macro generic containers.
- Evidence snippet:
```c
#define Array(T) struct { T *contents; uint32_t size; uint32_t capacity; }
#define array_init(self) \
  ((self)->size = 0, (self)->capacity = 0, (self)->contents = NULL)
#define array_push(self, element) \
  do { \
    (self)->contents = _array__grow((self)->contents, sizeof(*(self)->contents), \
      (self)->size, &(self)->capacity); \
    (self)->contents[(self)->size++] = (element); \
  } while (0)
```
- Why it matters: The codebase gets reusable vector-like behavior in C while preserving element type at use sites.
- When to use: Use in C projects that need lightweight generic collections without introducing code generation or C++.
- When not to use: Avoid when ownership, destructors, or nested allocation semantics require richer container APIs.
- Transferable principle: In C, a small macro layer can recover repetitive generic container ergonomics if helper functions avoid aliasing pitfalls.
- Related patterns: Inline-Or-Heap Compact Syntax Nodes; Public ABI Version Gate And Opaque Handles.
- Risks / caveats: Macro containers require disciplined ownership and bounds checking; debuggability is worse than ordinary functions.
- Agentic coding guidance: When editing macro containers, expand mentally for the concrete element type and verify capacity updates, ownership, and aliasing.

### Inline-Or-Heap Compact Syntax Nodes
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/tree-sitter__tree-sitter`; `lib/src/subtree.h`.
- Language / framework / stack: C parser runtime, compact AST representation.
- Evidence snippet:
```c
typedef struct {
  union {
    char *long_data;
    char short_data[24];
  };
  uint32_t length;
} ExternalScannerState;

typedef union {
  SubtreeInlineData data;
  const SubtreeHeapData *ptr;
} Subtree;
```
- Why it matters: Small leaf nodes can stay inline while larger, parent, external, or error nodes move to heap storage.
- When to use: Use in parsers, token streams, game engines, and runtimes with many tiny immutable-ish nodes.
- When not to use: Avoid until profiling shows allocation or cache locality is a real bottleneck.
- Transferable principle: Compact representations should make the common case cheap while preserving a fallback for complex cases.
- Related patterns: Macro-Generic C Arrays With Strict-Aliasing-Aware Helpers; Opaque Text Offsets And Ranges.
- Risks / caveats: Tagged pointer and inline-storage layouts are easy to break across platforms; keep invariants documented near the struct definitions.
- Agentic coding guidance: Before changing compact node layout, search all tag-bit, alignment, copy, and free paths; this is not a local edit.

### Polyglot Binding Specification With Generated Parity Tests
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/xberg-io__tree-sitter-language-pack`; `alef.toml`, `packages/go/binding.go`, `e2e/python/tests/test_registry.py`.
- Language / framework / stack: Alef, Rust core, generated Go/Python bindings, tree-sitter.
- Evidence snippet:
```toml
[workspace]
alef_version = "0.32.1"
languages = [
    "python",
    "node",
    "ruby",
    "php",
    "ffi",
    "go",
    "java",
    "csharp",
    "elixir",
    "wasm",
    "dart",
    "kotlin_android",
    "swift",
    "zig",
    "jni",
]

[workspace.opaque_types]
Language = "tree_sitter_language_pack::Language"
```
```go
// This file is auto-generated by alef — DO NOT EDIT.
// To regenerate: alef generate
// To verify freshness: alef verify --exit-code
```
- Why it matters: One binding specification drives multiple language surfaces and gives every generated package the same opaque core type.
- When to use: Use when a native core library must expose equivalent APIs to many ecosystems.
- When not to use: Avoid if each language binding needs deeply idiomatic behavior that cannot share a common schema.
- Transferable principle: Treat binding APIs as generated products of a central contract, then verify parity with per-language tests.
- Related patterns: Generated Workspace API From Codegen Boundary; Public ABI Version Gate And Opaque Handles.
- Risks / caveats: Generator upgrades can create broad diffs; keep generated output fresh and review templates carefully.
- Agentic coding guidance: When adding a binding method, update the Alef source contract and e2e tests rather than hand-editing one language package.

### Lock-Free Probe Then Locked Download Registry
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/xberg-io__tree-sitter-language-pack`; `crates/ts-pack-core/src/lib.rs`.
- Language / framework / stack: Rust, tree-sitter language registry, lazy globals, download cache.
- Evidence snippet:
```rust
static REGISTRY: LazyLock<LanguageRegistry> = LazyLock::new(LanguageRegistry::new);
static DOWNLOAD_CACHE_LOCK: Mutex<()> = Mutex::new(());

pub fn get_language(name: &str) -> Result<Language, Error> {
    if let Ok(lang) = REGISTRY.get_language(name) {
        return Ok(lang);
    }
    let _cache_guard = DOWNLOAD_CACHE_LOCK
        .lock()
        .map_err(|e| Error::LockPoisoned(e.to_string()))?;
    if let Ok(lang) = REGISTRY.get_language(name) {
        return Ok(lang);
    }
    ensure_cache_registered()?;
```
- Why it matters: The common path avoids locking, while the miss path serializes cache registration and download work with a double-check after acquiring the mutex.
- When to use: Use for lazy registries where most lookups are already resident but cache misses require expensive or side-effectful setup.
- When not to use: Avoid when every lookup needs mutation or when stale negative lookups are dangerous.
- Transferable principle: Probe cheaply first, lock only around the side effect, then re-check under the lock.
- Related patterns: Bounded Config Discovery Ladder; Opaque Text Offsets And Ranges.
- Risks / caveats: Global locks can hide long network/download operations; consider cancellation and observability for production services.
- Agentic coding guidance: When adding lazy loading, separate the no-lock read path from the miss path and test concurrent first access.

### Bounded Config Discovery Ladder
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/xberg-io__tree-sitter-language-pack`; `crates/ts-pack-core/src/config.rs`.
- Language / framework / stack: Rust, filesystem config discovery, environment variables.
- Evidence snippet:
```rust
pub fn discover() -> Result<Option<Self>, Error> {
    let search_paths = config_search_paths();
    for path in search_paths {
        if path.exists() {
            let config = Self::load(&path)
                .map_err(|e| Error::Config(format!("Failed to parse config at {}: {e}", path.display())))?;
            return Ok(Some(config));
        }
    }
    Ok(None)
}
```
- Why it matters: The library has a deterministic order for local project config and user config directories, rather than scattering ad hoc path checks.
- When to use: Use for CLI and library configuration where project-local settings should override user defaults.
- When not to use: Avoid if config discovery must be explicit for security or reproducibility.
- Transferable principle: Put config search order in one bounded function and make the fallback to defaults deliberate.
- Related patterns: Byte Size CLI Param Parser With Units; Lock-Free Probe Then Locked Download Registry.
- Risks / caveats: Parent-directory search needs depth limits and symlink care to avoid surprising or slow traversals.
- Agentic coding guidance: When adding a new config location, add it to the centralized discovery ladder and document its precedence.

### Opaque SQLite Store With Prepared Statement Cache
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/win4r__codebase-memory-mcp-pro`; `src/store/store.h`, `src/store/store.c`.
- Language / framework / stack: C, SQLite, graph store.
- Evidence snippet:
```c
typedef struct cbm_store cbm_store_t;

struct cbm_store {
    sqlite3 *db;
    const char *db_path;
    char errbuf[CBM_SZ_512];
    /* Prepared statements (lazily initialized, cached for lifetime) */
    sqlite3_stmt *stmt_upsert_node;
    sqlite3_stmt *stmt_find_node_by_id;
    sqlite3_stmt *stmt_insert_edge;
    /* ... */
};

static sqlite3_stmt *prepare_cached(cbm_store_t *s, sqlite3_stmt **slot, const char *sql) {
    if (*slot) {
        sqlite3_reset(*slot);
        sqlite3_clear_bindings(*slot);
        return *slot;
    }
    int rc = sqlite3_prepare_v2(s->db, sql, CBM_NOT_FOUND, slot, NULL);
    if (rc != SQLITE_OK) {
        store_set_error_sqlite(s, "prepare");
        return NULL;
    }
    return *slot;
}
```
- Why it matters: Callers see a stable opaque handle, while the implementation owns SQLite handles, cached statements, error buffers, schema setup, and finalization.
- When to use: Use in C libraries that expose a database-backed API but should not leak database implementation details.
- When not to use: Avoid sharing one opaque handle across threads unless the API explicitly documents synchronization.
- Transferable principle: Hide resource-heavy internals behind an opaque handle and centralize statement lifecycle in the implementation file.
- Related patterns: Public ABI Version Gate And Opaque Handles; Bounded Discovery With Excluded Subtree Reporting.
- Risks / caveats: Every cached statement must be finalized on close; leaks are easy when adding new statement slots.
- Agentic coding guidance: When adding a new query, add the statement slot, prepare path, reset/clear behavior, and close finalizer in the same edit.

### Bounded Discovery With Excluded Subtree Reporting
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/win4r__codebase-memory-mcp-pro`; `src/discover/discover.h`, `src/discover/discover.c`.
- Language / framework / stack: C, filesystem traversal, gitignore-style matching.
- Evidence snippet:
```c
bool cbm_should_skip_dir(const char *dirname, cbm_index_mode_t mode) {
    if (str_in_list(dirname, ALWAYS_SKIP_DIRS)) {
        return true;
    }
    if (mode != CBM_MODE_FULL && str_in_list(dirname, FAST_SKIP_DIRS)) {
        return true;
    }
    return false;
}

int cbm_discover_ex(const char *repo_path, const cbm_discover_opts_t *opts,
                    cbm_file_info_t **out, int *count,
                    char ***excluded_out, int *excluded_count_out);
```
- Why it matters: Discovery filters build outputs, caches, vendored code, generated files, and ignored paths while also reporting skipped subtrees to callers.
- When to use: Use for indexers and analyzers that need fast traversal but must explain why files were absent.
- When not to use: Avoid if complete archival fidelity matters more than speed.
- Transferable principle: Make aggressive filtering observable by returning both included files and excluded roots.
- Related patterns: Opaque SQLite Store With Prepared Statement Cache; Bounded Config Discovery Ladder.
- Risks / caveats: Hardcoded skip lists can accidentally hide source files; provide full mode and tests for mode enum consistency.
- Agentic coding guidance: When tuning index filters, add or update tests for both selected files and excluded-directory reporting.

### Tree-Sitter Import Extractor Dispatch Table
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/win4r__codebase-memory-mcp-pro`; `internal/cbm/extract_imports.c`.
- Language / framework / stack: C, tree-sitter, multi-language import extraction.
- Evidence snippet:
```c
static char *strip_quotes(CBMArena *a, const char *s);
static const char *path_last(CBMArena *a, const char *path);
static void parse_go_imports(CBMExtractCtx *ctx);
static void parse_python_imports(CBMExtractCtx *ctx);
static void parse_es_imports(CBMExtractCtx *ctx);

void cbm_extract_imports(CBMExtractCtx *ctx) {
    switch (ctx->language) {
    case CBM_LANG_JAVA:
    case CBM_LANG_KOTLIN:
    case CBM_LANG_CSHARP:
    case CBM_LANG_PHP:
        capture_namespace_decl(ctx);
        break;
    default:
        break;
    }
    switch (ctx->language) {
    case CBM_LANG_GO:
        parse_go_imports(ctx);
        break;
    case CBM_LANG_PYTHON:
        parse_python_imports(ctx);
        break;
    /* additional language cases dispatch to dedicated or generic parsers */
    }
}
```
- Why it matters: Language-specific AST quirks stay isolated in parser functions while shared helpers normalize quotes, aliases, and local names.
- When to use: Use for multi-language analyzers where each grammar exposes imports differently but downstream graph edges share one shape.
- When not to use: Avoid if query files or tree-sitter queries can express the language differences more declaratively.
- Transferable principle: Dispatch by language at the boundary, then emit one normalized internal DTO.
- Related patterns: Conservative Boolean Formula Prefiltering; Bounded Discovery With Excluded Subtree Reporting.
- Risks / caveats: Large switch dispatches can become difficult to audit; unsupported languages should fail silently only if callers expect partial extraction.
- Agentic coding guidance: When adding a new language extractor, reuse shared helpers for quote stripping and local-name derivation, then add focused grammar fixture tests.

## Worker 3 Batch 3

Codebase-memory status: skipped for this batch because the requested `timeout` wrapper was unavailable on macOS. No CodeGraphContext was used. Evidence below is from `rg`, `rg --files`, and direct source reads only.

### Native-Backing Adapter Conversion
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-jena-src`; `jena-commonsrdf/src/main/java/org/apache/jena/commonsrdf/JenaCommonsRDF.java`.
- Language / framework / stack: Java, Apache Jena, Commons RDF adapter layer.
- Evidence snippet:
```java
public static org.apache.jena.graph.Triple toJena(Triple triple) {
    if ( triple instanceof JenaTriple )
        return ((JenaTriple)triple).getTriple();
    return org.apache.jena.graph.Triple.create(toJena(triple.getSubject()), toJena(triple.getPredicate()), toJena(triple.getObject()) );
}

public static org.apache.jena.graph.Graph toJena(Graph graph) {
    if ( graph instanceof JenaGraph )
        return ((JenaGraph)graph).getGraph();
    org.apache.jena.graph.Graph g = GraphFactory.createGraphMem();
    graph.stream().forEach(t->g.add(toJena(t)));
    return g;
}
```
- Why it matters: The adapter preserves identity and avoids copying when values already came from Jena, but still supports foreign Commons RDF implementations through explicit conversion.
- When to use: Use at library boundaries where callers may pass either native objects or interface-compatible objects from another implementation.
- When not to use: Avoid when aliasing native mutable state would surprise the caller or break isolation.
- Transferable principle: Check for native-backed wrappers first, then fall back to a clear structural copy.
- Related patterns: Backend-Specific Execution Engine With Metric Bundling; Generated Workspace API From Codegen Boundary.
- Risks / caveats: The fast path exposes the original backing object, so mutation and lifecycle semantics follow the native implementation.
- Agentic coding guidance: When generating adapter code, preserve native identity only when the wrapper type is explicit; do not use brittle class-name checks or reflection.

### Context Symbol Extension Surface
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-jena-src`; `jena-arq/src/main/java/org/apache/jena/query/ARQ.java`.
- Language / framework / stack: Java, SPARQL query engine configuration.
- Evidence snippet:
```java
public static final Symbol stageGenerator = SystemARQ.allocSymbol("stageGenerator");
public static final Symbol regexImpl =  SystemARQ.allocSymbol("regexImpl");
public static final Symbol httpRequestModifer = SystemARQ.allocSymbol("httpRequestModifer");

public static void enableOptimizer(Context context, boolean state) {
    context.set(ARQ.optimization, state);
}

public static final Symbol optimization = SystemARQ.allocSymbol("optimization");
```
- Why it matters: Engine behavior is extended through named context keys instead of constructor explosion or global-only switches.
- When to use: Use for query engines, compilers, and protocol stacks with many optional behaviors scoped to execution contexts.
- When not to use: Avoid when configuration keys are untyped, undocumented, and only consumed by one call site.
- Transferable principle: Centralize extension keys in one namespace and pass a context object through execution paths.
- Related patterns: Type-Erased Session Variable Definitions With Typed Constraints; Capability Tokens Plus Static Forbid Rules.
- Risks / caveats: Misspelled or semantically overloaded symbols can become invisible configuration bugs.
- Agentic coding guidance: Add new context symbols beside existing ones, document expected value types, and search for both producers and consumers before changing semantics.

### AutoCloseable Analysis With Callback Sink
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pmd__pmd`; `pmd-ant/src/main/java/net/sourceforge/pmd/ant/CPDTask.java`.
- Language / framework / stack: Java, PMD CPD, Ant task integration.
- Evidence snippet:
```java
try (CpdAnalysis cpd = CpdAnalysis.create(config)) {
    addFiles(cpd);

    log("Starting to analyze code", Project.MSG_INFO);
    long start = System.currentTimeMillis();
    cpd.performAnalysis(this::report);
    long timeTaken = System.currentTimeMillis() - start;
    log("Done analyzing code; that took " + timeTaken + " milliseconds");
}
```
- Why it matters: Analysis owns resources for a bounded lifetime, while reporting is inverted into a callback so the Ant task controls rendering and build-failure policy.
- When to use: Use for batch analysis APIs that need setup, file registration, execution, and caller-specific reporting.
- When not to use: Avoid when analysis results are small and simpler as a returned value.
- Transferable principle: Make expensive analysis sessions closeable and stream results to caller-owned sinks.
- Related patterns: Backend-Specific Execution Engine With Metric Bundling; Feign Client Fallback For Degraded Cross-Service Calls.
- Risks / caveats: Callback exceptions must be translated into the host framework's error model.
- Agentic coding guidance: When adding a new analysis entry point, keep resource ownership in the analysis object and adapt only status/log/report behavior in the host task.

### Renderer Metadata Drives CLI Help
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/pmd__pmd`; `pmd-cli/src/main/java/net/sourceforge/pmd/cli/commands/internal/PmdCommand.java`, `pmd-ant/src/main/java/net/sourceforge/pmd/ant/Formatter.java`.
- Language / framework / stack: Java, Picocli, PMD renderer plugins.
- Evidence snippet:
```java
for (final String rendererName : RendererFactory.supportedRenderers()) {
    final Renderer renderer = RendererFactory.createRenderer(rendererName, emptyProps);

    if (!renderer.getPropertyDescriptors().isEmpty()) {
        reportPropertiesHelp.append(rendererName + ":" + lineSeparator);
        for (final PropertyDescriptor<?> property : renderer.getPropertyDescriptors()) {
            reportPropertiesHelp.append("  ").append(property.name()).append(" - ")
                .append(property.description()).append(lineSeparator);
        }
    }
}
```
- Why it matters: CLI help and completion candidates are computed from the same renderer registry used at runtime, reducing drift between documentation and plugins.
- When to use: Use when plugins expose named properties, output formats, codecs, or strategies.
- When not to use: Avoid if plugin construction has side effects or requires expensive external state.
- Transferable principle: Let runtime extension metadata generate user-facing option help.
- Related patterns: Backend Plugin Discovery With Explicit Signatures; Generated Workspace API From Codegen Boundary.
- Risks / caveats: Static initialization can slow command startup if plugin discovery is heavy.
- Agentic coding guidance: When adding renderer properties, update the `PropertyDescriptor` definitions first; the CLI should pick up names, descriptions, and defaults automatically.

### Newtype Language Term Adapter
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__semantic`; `semantic-java/src/Language/Java.hs`, `semantic-php/src/Language/PHP.hs`.
- Language / framework / stack: Haskell, tree-sitter ASTs, semantic tagging.
- Evidence snippet:
```haskell
newtype Term a = Term { getTerm :: Java.Program a }
  deriving MarshalJSON

instance TS.SymbolMatching Term where
  matchedSymbols _ = TS.matchedSymbols (Proxy :: Proxy Java.Program)
  showFailure _ = TS.showFailure (Proxy :: Proxy Java.Program)

instance TS.Unmarshal Term where
  matchers = fmap (fmap (TS.hoist Term)) TS.matchers

instance Tags.ToTags Term where
  tags src = Tags.runTagging src . JavaTags.tags . getTerm
```
- Why it matters: A language module exposes one public `Term` facade while delegating JSON, parse matching, and tagging to the generated AST type.
- When to use: Use when generated ASTs need a stable language-specific API surface without duplicating generated internals.
- When not to use: Avoid if the wrapper adds no new typeclass instances or boundary semantics.
- Transferable principle: Wrap generated syntax trees in thin newtypes that implement the domain capabilities expected by the platform.
- Related patterns: Generated Workspace API From Codegen Boundary; Polyglot Binding Specification With Generated Parity Tests.
- Risks / caveats: Thin wrappers can hide performance-costly traversals if instances are too broad.
- Agentic coding guidance: When adding a language, mirror the wrapper module shape and implement capability instances by delegating through `Proxy`, `hoist`, and a language-specific tagger.

### Continuation-Based Assignment Desugaring
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/github__semantic`; `semantic-python/src/Language/Python/Core.hs`.
- Language / framework / stack: Haskell, Python AST lowering, algebraic effects.
- Evidence snippet:
```haskell
desugar :: [Located Name]
        -> RHS Span
        -> Either String ([Located Name], Desugared Span)
desugar acc = \case
  Prj Py.Assignment { left = SingleIdentifier name, right = Just rhs, ann} ->
    desugar (Located ann name : acc) rhs
  R1 any -> pure (acc, any)
  other -> Left ("desugar: couldn't desugar RHS " <> show other)

collapseDesugared (Located loc n) cont rem =
  let assigning = fmap (Core.annAt loc . ((Name.named' n :<- rem) >>>=))
  in assigning (local (def n) (cont (pure n)))
```
- Why it matters: Chained assignment lowering separates discovery of assigned names from reconstruction of sequenced core expressions.
- When to use: Use when source syntax has right-associated or chainable forms that need ordered, scope-aware lowering.
- When not to use: Avoid when a direct recursive AST-to-AST translation is clearer.
- Transferable principle: Desugar complex syntax into a terminal expression plus accumulated obligations, then fold obligations back with explicit continuations.
- Related patterns: Conservative Boolean Formula Prefiltering; Diagnostic Context Combinators.
- Risks / caveats: Continuation-style lowering is powerful but hard to read; keep local types like `Located`, `RHS`, and `Desugared` explicit.
- Agentic coding guidance: When changing language lowering, write tests for nested/chained cases first and preserve span annotation at every generated core node.

### Workspace Directory As Project Ledger
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joernio__joern`; `console/src/main/scala/io/joern/console/workspacehandling/WorkspaceManager.scala`.
- Language / framework / stack: Scala, Joern console workspace management, JSON metadata.
- Evidence snippet:
```scala
private var workspace: Workspace[ProjectType] = loader.load(path)
private val dirPath = Paths.get(path).toAbsolutePath

private def createProjectDirectory(inputPath: String, name: String): Unit = {
  val dirPath = projectNameToDir(name)
  Files.createDirectories(dirPath)
  val absoluteInputPath = Paths.get(inputPath).absolutePathAsString
  Files.createDirectories(Paths.get(overlayDir(name)))
  val projectFile = ProjectFile(absoluteInputPath, name)
  writeProjectFile(projectFile, dirPath)
  (dirPath / "cpg.bin").createWithParentsIfNotExists()
}
```
- Why it matters: Workspace state is recoverable from project directories, `project.json`, overlay directories, and a known CPG filename.
- When to use: Use for developer tools that need persistent project lists without a separate database.
- When not to use: Avoid if concurrent writers, transactions, or remote synchronization require a real store.
- Transferable principle: Make filesystem layout the durable ledger, then load in-memory workspace state from it.
- Related patterns: Opaque SQLite Store With Prepared Statement Cache; Bounded Discovery With Excluded Subtree Reporting.
- Risks / caveats: Filesystem ledgers need careful cleanup on partial project creation.
- Agentic coding guidance: When adding workspace metadata, update both the writer and loader paths; do not add in-memory-only fields that cannot survive restart.

### Generator Factory With Format Normalization
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joernio__joern`; `console/src/main/scala/io/joern/console/cpgcreation/package.scala`, `console/src/main/scala/io/joern/console/cpgcreation/CpgGeneratorFactory.scala`.
- Language / framework / stack: Scala, Joern CPG generation, multi-language frontends.
- Evidence snippet:
```scala
def cpgGeneratorForLanguage(
  language: String,
  config: FrontendConfig,
  rootPath: Path,
  args: List[String]
): Option[CpgGenerator] = {
  lazy val conf = config.withArgs(args)
  language match {
    case Languages.C | Languages.NEWC => Some(CCpgGenerator(conf, rootPath))
    case Languages.JSSRC | Languages.JAVASCRIPT =>
      val jssrc = JsSrcCpgGenerator(conf, rootPath)
      if (jssrc.isAvailable) Some(jssrc)
      else Some(JsCpgGenerator(conf, rootPath))
    case Languages.RUST => Some(RustCpgGenerator(conf, rootPath))
    case _ => None
  }
}
```
- Why it matters: Language detection, frontend availability, and legacy output normalization are centralized before a project is opened.
- When to use: Use when one command surface must route many language/toolchain implementations.
- When not to use: Avoid if the factory becomes a dumping ground for frontend-specific flags and post-processing.
- Transferable principle: Normalize language selection and artifact format at the boundary before the rest of the workflow sees the result.
- Related patterns: Macro Registry For Connector Variants; Tree-Sitter Import Extractor Dispatch Table.
- Risks / caveats: A growing match table needs tests for fallback precedence and unsupported languages.
- Agentic coding guidance: When adding a frontend, update known languages, guessing rules, factory construction, and availability tests in the same change.

### Restricted Imports As Architecture Rules
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/joernio__joern`; `linter-rules/src/main/scala/fix/RestrictedImports.scala`.
- Language / framework / stack: Scala, Scalafix syntactic linter.
- Evidence snippet:
```scala
private val rules: Map[String, ImportRule] = Seq(
  ImportRule(
    "BetterFiles",
    "Avoid the 'Better Files' library, use `io.shiftleft.semanticcpg.utils.FileUtil`, `os-lib` or `java.nio.file` instead.",
    "better.files"
  ),
  ImportRule(
    "ScalaSysProcess",
    "Do not manually create processes with `scala.sys.process`, use `io.shiftleft.semanticcpg.utils.ExternalCommand` instead.",
    "scala.sys.process"
  )
).map(x => x.path -> x).toMap
```
- Why it matters: Architectural preferences are enforced as code-level import diagnostics rather than living only in review comments.
- When to use: Use when specific libraries bypass project wrappers, sandboxing, logging, or portability policies.
- When not to use: Avoid if the replacement API is not mature or the rule would create noisy exceptions.
- Transferable principle: Encode dependency boundaries as lint rules with actionable replacement messages.
- Related patterns: Capability Tokens Plus Static Forbid Rules; Filesystem Trait With Sandbox Adapters.
- Risks / caveats: Package-level exceptions can grow; keep ignored packages small and justified.
- Agentic coding guidance: When introducing a forbidden dependency, add the lint rule and its recommended alternative before refactoring callers.

### Min-Heap Cron Scheduler Releasing Callback Lock
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/falkordb-src`; `src/cron/cron.c`.
- Language / framework / stack: C, pthreads, Redis module background scheduler.
- Evidence snippet:
```c
typedef struct {
	struct timespec due;
	CronTaskCB cb;
	CronTaskFree free;
	void *pdata;
} CRON_TASK;

while (_CRON_PeekDue (&task, &due_time)) {
	if (!_CRON_RemoveCurrentTask (task)) {
		continue ;
	}

	CRON_UNLOCK () ;
	CRON_PerformTask (task) ;
	cron->current_task = NULL ;
	CRON_FreeTask (task) ;
	CRON_LOCK () ;
}
```
- Why it matters: The scheduler protects heap state with a mutex but releases it while callbacks run, so task insertion and aborts are not blocked by long work.
- When to use: Use for lightweight in-process schedulers with many short delayed tasks and explicit task ownership.
- When not to use: Avoid for distributed scheduling, persistent jobs, or callbacks that cannot safely run outside the scheduler lock.
- Transferable principle: Hold locks for queue bookkeeping, not for user callback execution.
- Related patterns: Shutdown Guard With Cascading Cancellation; Explicit Async State Machine Transitions.
- Risks / caveats: Callback code must tolerate concurrent scheduler operations and task abort races.
- Agentic coding guidance: When adding scheduler behavior, identify whether code touches heap state or user work, and keep those sections separated by lock boundaries.

### Function-Pointer Constraint Vtable
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/falkordb-src`; `src/constraint/constraint.h`, `src/constraint/unique_constraint.c`.
- Language / framework / stack: C, graph constraints, opaque structs.
- Evidence snippet:
```c
typedef struct _Constraint *Constraint;

typedef bool (*Constraint_EnforcementCB)
(
	const Constraint c,
	const GraphEntity *e,
	char **err_msg
);

struct _UniqueConstraint {
	ConstraintType t;
	Constraint_EnforcementCB enforce;
	Constraint_SetPrivateDataCB set_pdata;
	Constraint_GetPrivateDataCB get_pdata;
	ConstraintStatus status;
	Index idx;
};
```
- Why it matters: Different constraint implementations can share one opaque `Constraint` API while dispatching enforcement and private data through function pointers.
- When to use: Use in C modules that need plugin-like behavior without exposing implementation structs.
- When not to use: Avoid if there is only one concrete type and direct calls are simpler.
- Transferable principle: Put the pseudo-vtable at the beginning of every concrete opaque struct and access it through a shared handle.
- Related patterns: Opaque SQLite Store With Prepared Statement Cache; Public ABI Version Gate And Opaque Handles.
- Risks / caveats: Manual casts make layout invariants critical; every concrete struct must keep the function-pointer fields consistent.
- Agentic coding guidance: When adding a constraint type, mirror the existing field layout, initializer, free path, and dispatch tests before exposing it through `Constraint_New`.

### Active Pending Index Double Buffer
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/falkordb-src`; `src/schema/schema.c`.
- Language / framework / stack: C, graph schema indexes, background index population.
- Evidence snippet:
```c
Index active  = ACTIVE_IDX(s);
Index pending = PENDING_IDX(s);
Index altered = (pending != NULL) ? pending : active;

_idx = pending;
if(pending == NULL) {
	if(active != NULL) {
		_idx = Index_Clone(active);
	} else {
		_idx = Index_New(s->name, s->id, et);
	}
}
PENDING_IDX(s) = _idx;
```
```c
ACTIVE_IDX(s) = pending;
PENDING_IDX(s) = NULL;
Constraint_SetPrivateData(c, active);
```
- Why it matters: Index modifications build in a pending copy, then activation swaps it into the active slot and updates constraints that depend on the index.
- When to use: Use when readers need stable active indexes while background work prepares a replacement.
- When not to use: Avoid if in-place mutation is already protected by stronger transactional guarantees.
- Transferable principle: Clone or create pending state, populate it independently, then atomically promote and repair dependent pointers.
- Related patterns: Lock-Free Probe Then Locked Download Registry; Conservative Boolean Formula Prefiltering.
- Risks / caveats: Dependent objects must be updated at promotion time or they will retain stale private data.
- Agentic coding guidance: When editing schema index flow, trace active, pending, populate, activate, and constraint private-data updates as one lifecycle.

### Zeroizing Secret Transfer Object
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/materialize-src`; `src/tls-util/src/lib.rs`.
- Language / framework / stack: Rust, TLS utilities, OpenSSL PKCS #12, secure memory hygiene.
- Evidence snippet:
```rust
pub struct Pkcs12Archive {
    pub der: Vec<u8>,
    pub pass: String,
}

impl Zeroize for Pkcs12Archive {
    fn zeroize(&mut self) {
        self.der.zeroize();
        self.pass.zeroize();
    }
}

impl Drop for Pkcs12Archive {
    fn drop(&mut self) {
        self.zeroize();
    }
}
```
- Why it matters: Sensitive archive bytes and passwords are cleared on drop, with tests asserting both `needs_drop` and `Zeroize` behavior.
- When to use: Use for short-lived structs that carry key material, passwords, tokens, or serialized credentials.
- When not to use: Avoid claiming full secrecy if data is copied elsewhere, interned, logged, or passed into libraries that retain buffers.
- Transferable principle: Wrap sensitive data in a domain type that owns zeroization and tests the cleanup contract.
- Related patterns: Config Template Secret String Type; Normalized Boundary Value Objects For Network Policy.
- Risks / caveats: `into_parts` deliberately uses `ManuallyDrop` to transfer ownership; callers then inherit the zeroization responsibility.
- Agentic coding guidance: When adding secret carriers, implement `Zeroize` and `Drop` together, then add tests proving fields are cleared and the type needs drop.

### Concurrent Tunnel Dedup State Map
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/materialize-src`; `src/ssh-util/src/tunnel_manager.rs`.
- Language / framework / stack: Rust, Tokio, SSH tunnel management, watch channels.
- Evidence snippet:
```rust
enum Action {
    Return(ManagedSshTunnelHandle),
    AwaitConnection(watch::Receiver<()>),
    StartConnection(watch::Sender<()>),
}

let action = match self.tunnels.lock().expect("lock poisoned").entry(key.clone()) {
    btree_map::Entry::Occupied(mut occupancy) => match occupancy.get_mut() {
        SshTunnelState::Connected(handle) => Action::Return(ManagedSshTunnelHandle {
            handle: Arc::clone(handle),
            manager: self.clone(),
            key: key.clone(),
        }),
        SshTunnelState::Connecting(rx) => Action::AwaitConnection(rx.clone()),
    },
    btree_map::Entry::Vacant(vacancy) => {
        let (tx, rx) = watch::channel(());
        vacancy.insert(SshTunnelState::Connecting(rx));
        Action::StartConnection(tx)
    }
};
```
- Why it matters: Concurrent requests for the same tunnel share an in-flight connection attempt instead of racing duplicate SSH sessions.
- When to use: Use for expensive keyed resources where a miss triggers async setup and all callers can share the eventual handle.
- When not to use: Avoid when each caller needs isolated credentials, independent cancellation, or separate resource quotas.
- Transferable principle: Store `Connecting` and `Connected` states under the same key, decide an action under lock, then await outside the lock.
- Related patterns: Lock-Free Probe Then Locked Download Registry; Shutdown Guard With Cascading Cancellation.
- Risks / caveats: Cancellation safety depends on clearing `Connecting` state if the starter future is dropped.
- Agentic coding guidance: When modifying this pattern, preserve the local `Action` enum shape so no mutex guard crosses an `.await`.

### Domain DSL For Rust Item Names
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/charon`; `charon-ml/src/NameMatcher.ml`, `charon-ml/name_matcher_parser/Ast.ml`, `charon-ml/name_matcher_parser/Interface.ml`.
- Language / framework / stack: OCaml, Rust MIR extraction, parser-generated DSL.
- Evidence snippet:
```ocaml
type var = VarName of string | VarIndex of int
and pattern = pattern_elem list

and pattern_elem =
  | PIdent of string * int * generic_args
  | PImpl of expr
  | PWild

let parse_pattern (s : string) : pattern =
  let lexbuf = Lexing.from_string s in
  try Parser.full_pattern Lexer.token lexbuf
  with Parser.Error ->
    raise
      (Failure ("Parse error at " ^ pos_string lexbuf.lex_curr_p ^ ":\n" ^ s))
```
- Why it matters: Charon names Rust definitions with a compact language that handles impl blocks, generics, lifetimes, wildcards, and disambiguators.
- When to use: Use when user-facing filters must identify rich language entities that simple strings cannot address safely.
- When not to use: Avoid creating a DSL when existing language paths or structured selectors are sufficient.
- Transferable principle: Model complex names with a parsed AST, then provide printers for pattern, pretty, and generated-name targets.
- Related patterns: Token-Budget Smart Context Greedy Selection; Bounded Config Discovery Ladder.
- Risks / caveats: A DSL creates long-term compatibility obligations for syntax and error messages.
- Agentic coding guidance: When adding matcher syntax, update the AST, parser, pretty-printer, and round-trip tests together.

### Context-Rich JSON Deserialization Combinators
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/charon`; `charon-ml/src/OfJsonBasic.ml`, `charon-ml/src/GAstOfJson.ml`.
- Language / framework / stack: OCaml, Yojson, generated and handwritten deserializers.
- Evidence snippet:
```ocaml
let combine_error_msgs (js : json) (msg : string) (res : ('a, string) result) :
    ('a, string) result =
  match res with
  | Ok x -> Ok x
  | Error e -> Error ("[" ^ msg ^ "]" ^ " failed on: " ^ show js ^ "\n\n" ^ e)

let option_of_json (a_of_json : 'ctx -> json -> ('a, string) result)
    (ctx : 'ctx) (js : json) : ('a option, string) result =
  combine_error_msgs js "option_of_json"
    (match js with
    | `Null -> Ok None
    | _ ->
        let* x = a_of_json ctx js in
        Ok (Some x))
```
- Why it matters: Generated deserializers share small typed combinators that attach local JSON context to failures, while handwritten cases handle Rust-side generic mismatches.
- When to use: Use for schema-heavy deserialization where errors must identify the failing field and raw JSON fragment.
- When not to use: Avoid if a mature deriving library already produces equally clear errors and matches the source format.
- Transferable principle: Build deserialization from composable typed parsers and wrap every nested layer with contextual error labels.
- Related patterns: Diagnostic Context Combinators; Generated Workspace API From Codegen Boundary.
- Risks / caveats: Recursive combinators should avoid quadratic error construction on huge JSON documents.
- Agentic coding guidance: When adding a JSON field parser, route it through `combine_error_msgs` and preserve ordering constraints documented for hash-consed values.

### Fluent Shader Compilation Contract
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/rust-gpu`; `crates/spirv-builder/src/lib.rs`, `examples/runners/wgpu/src/lib.rs`.
- Language / framework / stack: Rust, rust-gpu, SPIR-V builder, Cargo integration.
- Evidence snippet:
```rust
pub fn new(path_to_crate: impl AsRef<Path>, target: impl Into<String>) -> Self {
    Self {
        path_to_crate: Some(path_to_crate.as_ref().to_owned()),
        target: Some(target.into()),
        ..SpirvBuilder::default()
    }
}

#[must_use]
pub fn capability(mut self, capability: Capability) -> Self {
    self.capabilities.push(capability);
    self
}

target_features.extend(builder.capabilities.iter().map(|cap| format!("+{cap:?}")));
target_features.extend(builder.extensions.iter().map(|ext| format!("+ext:{ext}")));
```
- Why it matters: Shader crate compilation is configured through a fluent, serializable builder whose settings lower into Cargo target features and rustc flags.
- When to use: Use for build orchestration APIs with many optional flags but one final `build()` boundary.
- When not to use: Avoid if options interact in ways that need typestate or compile-time sequencing.
- Transferable principle: Accumulate build intent in a builder, validate incompatible options at the boundary, and make lowering to tool flags explicit.
- Related patterns: Schema-Validated Resource Stack Builder; Bounded Config Discovery Ladder.
- Risks / caveats: Fluent setters can hide incompatible combinations unless `build()` performs clear validation.
- Agentic coding guidance: When adding a SPIR-V option, add the field, fluent setter, clap/serde metadata if appropriate, lowering into flags, and an incompatibility test.

### Hot Shader Module Reload Boundary
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/rust-gpu`; `examples/runners/wgpu/src/lib.rs`, `examples/runners/ash/src/graphics.rs`.
- Language / framework / stack: Rust, wgpu/ash, SPIR-V hot reload, Vulkan pipeline recreation.
- Evidence snippet:
```rust
if let Some(mut f) = on_watch {
    let mut watcher = builder.watch().unwrap();
    let first_compile = loop {
        match watcher.recv() {
            Ok(e) => break e,
            Err(e) => println!("Shader compiling failed: {e}"),
        }
    };

    let shader_modules = handle_compile_result(first_compile);
    std::thread::spawn(move || {
        loop {
            match watcher.recv() {
                Ok(compile_result) => {
                    f(handle_compile_result(compile_result));
                }
                Err(e) => println!("Shader compiling failed: {e}"),
            }
        }
    });
    shader_modules
}
```
```rust
pub fn set_shader_code(&mut self, shader_code: Vec<u32>) {
    self.shader_code = shader_code;
    self.should_recreate();
}

pub fn get_pipeline(&mut self) -> anyhow::Result<&MyRenderPipeline> {
    if self.should_recreate {
        self.rebuild_pipeline()?;
    }
    Ok(self.pipeline.as_ref().unwrap())
}
```
- Why it matters: Compilation watching and GPU pipeline recreation are separated by a small module-replacement boundary.
- When to use: Use for graphics or compute tools where shader iteration speed matters and the renderer can tolerate pipeline rebuilds.
- When not to use: Avoid in production render loops without throttling, validation, and graceful fallback to the previous good pipeline.
- Transferable principle: Convert compiler outputs into runtime module descriptors, then mark dependent runtime objects dirty instead of mutating them in place.
- Related patterns: Streaming JSON-RPC Reader State Machine; Explicit Async State Machine Transitions.
- Risks / caveats: Background watcher threads need lifecycle control in non-demo applications.
- Agentic coding guidance: When adding hot reload, keep compile errors non-fatal, retain the last working module, and isolate renderer recreation behind a `should_recreate` flag.

## Worker 3 Batch 4

Codebase-memory status for this batch: attempted only on `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-rs-src` with the repo-local bounded runner. Summary: `{"status":"pass","returncode":0,"timeout_seconds":120,"out_dir":"/tmp/codex-code-intel/codebase-memory/apache-arrow-rs-src-20260706-234543"}`. No CodeGraphContext was used. All pattern claims below are verified with `rg`, `rg --files`, and direct source reads.

### Validating Constructor With Unsafe Escape Hatch
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-rs-src`; `arrow-array/src/record_batch.rs`.
- Language / framework / stack: Rust, Apache Arrow columnar arrays.
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
) -> Self {
    Self { schema, columns, row_count }
}

if schema.fields().len() != columns.len() {
    return Err(ArrowError::InvalidArgumentError(format!(
        "number of columns({}) must match number of fields({}) in schema",
        columns.len(),
        schema.fields().len(),
    )));
}
```
- Why it matters: The public constructor protects schema, nullability, type, and row-count invariants while still allowing carefully audited internal fast paths.
- When to use: Use for data containers whose invariants are expensive enough to centralize but important enough to enforce at construction.
- When not to use: Avoid exposing unchecked constructors to ordinary application code or plugin boundaries.
- Transferable principle: Put validation in one `try_new` boundary and make invariant-bypassing APIs explicitly unsafe or otherwise visually loud.
- Related patterns: Schema-Validated Resource Stack Builder; Fixed-Capacity no_std Buffer With Invariant Tests.
- Risks / caveats: The unchecked path must document every invariant that callers inherit.
- Agentic coding guidance: Generate new constructors by routing through the checked implementation first; add an unchecked variant only after proving the hot path and documenting the safety contract.

### Scalar-Or-Array Kernel Datum
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/apache-arrow-rs-src`; `arrow-array/src/scalar.rs`.
- Language / framework / stack: Rust, Apache Arrow compute kernels.
- Evidence snippet:
```rust
pub trait Datum {
    /// Returns the value for this [`Datum`] and a boolean indicating if the value is scalar
    fn get(&self) -> (&dyn Array, bool);
}

impl<T: Array> Datum for T {
    fn get(&self) -> (&dyn Array, bool) {
        (self, false)
    }
}

#[derive(Debug, Copy, Clone)]
pub struct Scalar<T: Array>(T);

impl<T: Array> Datum for Scalar<T> {
    fn get(&self) -> (&dyn Array, bool) {
        (&self.0, true)
    }
}
```
- Why it matters: Kernels can accept either a full array or a single-value scalar without building repeated constant arrays.
- When to use: Use in vectorized compute APIs where scalar broadcasting is common and allocation-sensitive.
- When not to use: Avoid when scalar and vector operations have fundamentally different semantics or null handling.
- Transferable principle: Represent broadcastability as a tiny trait-level capability instead of duplicating every kernel entry point.
- Related patterns: Typed SQL WITH Option Conversion Traits; Function-Pointer Constraint Vtable.
- Risks / caveats: Kernel implementors must correctly interpret the boolean scalar flag and scalar null state.
- Agentic coding guidance: When adding a compute kernel, write array-array and array-scalar tests before optimizing the inner loop.

### Buffer-First Wire Codec
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/iggy`; `core/binary_protocol/src/codec.rs`, `core/common/src/traits/binary_impls/messages.rs`.
- Language / framework / stack: Rust, binary protocol, Bytes/BytesMut.
- Evidence snippet:
```rust
pub trait WireEncode {
    fn encode(&self, buf: &mut BytesMut);
    fn encoded_size(&self) -> usize;

    #[must_use]
    fn to_bytes(&self) -> Bytes {
        let mut buf = BytesMut::with_capacity(self.encoded_size());
        self.encode(&mut buf);
        buf.freeze()
    }
}

let size = SendMessagesEncoder::encoded_size(
    &wire_stream_id, &wire_topic_id, &wire_partitioning, &raw_messages,
);
let mut buf = BytesMut::with_capacity(size);
SendMessagesEncoder::encode(&mut buf, &wire_stream_id, &wire_topic_id, &wire_partitioning, &raw_messages);
```
- Why it matters: Hot paths can reuse or pre-size buffers, while convenience callers still get `to_bytes()`.
- When to use: Use for wire protocols, log records, and persistence formats where encoded size is knowable.
- When not to use: Avoid when the format is streaming-only or cannot know size without doing the work twice.
- Transferable principle: Make allocation a caller-controlled concern, then layer ergonomic allocation helpers on top.
- Related patterns: Streaming JSON-RPC Reader State Machine; Byte Size CLI Param Parser With Units.
- Risks / caveats: `encoded_size()` and `encode()` must remain in lockstep.
- Agentic coding guidance: Every new wire type should include a round-trip test plus `assert_eq!(encoded_size(), to_bytes().len())`.

### Compile-Time Fixed Header Layout
- Where found: `/Users/amuldotexe/Desktop/reference-repos-yard/iggy`; `core/binary_protocol/src/consensus/header.rs`.
- Language / framework / stack: Rust, consensus protocol, bytemuck zero-copy decode.
- Evidence snippet:
```rust
pub const HEADER_SIZE: usize = 256;

pub trait ConsensusHeader: Sized + CheckedBitPattern + NoUninit {
    const COMMAND: Command2;
    fn validate(&self) -> Result<(), ConsensusError>;
    fn operation(&self) -> Operation;
    fn command(&self) -> Command2;
    fn size(&self) -> u32;
}

#[repr(C)]
#[derive(Debug, Clone, Copy, CheckedBitPattern, NoUninit)]
pub struct GenericHeader { /* fields */ }

const _: () = {
    assert!(size_of::<GenericHeader>() == HEADER_SIZE);
    assert!(offset_of!(GenericHeader, reserved_command) + size_of::<[u8; 128]>() == HEADER_SIZE);
};
```
- Why it matters: Protocol compatibility is defended at compile time before zero-copy deserialization is allowed.
- When to use: Use for fixed-width network, disk, or shared-memory records that need direct byte casting.
- When not to use: Avoid for extensible formats where fields evolve independently or alignment is not controlled.
- Transferable principle: Pair `repr(C)` layout with compile-time size and offset assertions before exposing pointer-cast decoding.
- Related patterns: Public ABI Version Gate And Opaque Handles; Macro-Generic C Arrays With Strict-Aliasing-Aware Helpers.
- Risks / caveats: Cross-platform integer sizes, alignment, and enum representation must be pinned.
- Agentic coding guidance: When editing a fixed header, update offset assertions and invalid-byte tests in the same change.

### Embedded Operator Vtable Struct
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redisgraph-src`; `src/execution_plan/ops/op.h`, `src/execution_plan/ops/op_node_by_label_scan.c`.
- Language / framework / stack: C, Redis module, graph query execution plans.
- Evidence snippet:
```c
typedef OpResult(*fpInit)(struct OpBase *);
typedef Record(*fpConsume)(struct OpBase *);
typedef OpResult(*fpReset)(struct OpBase *);
typedef struct OpBase *(*fpClone)(const struct ExecutionPlan *, const struct OpBase *);

struct OpBase {
    OPType type;
    fpInit init;
    fpFree free;
    fpReset reset;
    fpClone clone;
    fpConsume consume;
    fpToString toString;
    struct OpBase **children;
    bool writer;
};

OpBase_Init((OpBase *)op, OPType_NODE_BY_LABEL_SCAN, "Node By Label Scan",
    NodeByLabelScanInit, NodeByLabelScanConsume, NodeByLabelScanReset, ...);
```
- Why it matters: C operators get polymorphic lifecycle hooks while concrete structs can embed `OpBase` as their first field.
- When to use: Use in C systems that need many pluggable node types with uniform traversal, cloning, reset, and teardown.
- When not to use: Avoid when a simple enum switch is smaller and easier to audit.
- Transferable principle: Model object behavior explicitly with function pointers and a shared base struct when the language lacks native interfaces.
- Related patterns: Function-Pointer Constraint Vtable; Active Pending Index Double Buffer.
- Risks / caveats: Function-pointer initialization order is correctness-critical and not type-safe beyond signatures.
- Agentic coding guidance: When adding an operator, implement all lifecycle functions first, then wire `OpBase_Init`, and verify clone/free symmetry.

### Tagged Value Union With Ownership Flags
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redisgraph-src`; `src/value.h`, `src/value.c`.
- Language / framework / stack: C, RedisGraph Cypher values.
- Evidence snippet:
```c
typedef enum {
    M_NONE = 0,
    M_SELF = (1 << 0),
    M_VOLATILE = (1 << 1),
    M_CONST = (1 << 2)
} SIAllocation;

typedef struct SIValue {
    union {
        int64_t longval;
        double doubleval;
        char *stringval;
        void *ptrval;
        struct SIValue *array;
        Point point;
    };
    SIType type;
    SIAllocation allocation;
} SIValue;

void SIValue_MakeVolatile(SIValue *v);
void SIValue_Persist(SIValue *v);
void SIValue_Free(SIValue v);
```
- Why it matters: A single value representation supports Cypher types while explicitly tracking whether nested memory is owned, shared, volatile, or constant.
- When to use: Use for interpreters and query engines that need compact dynamic values in C.
- When not to use: Avoid if a managed runtime or safer sum type is available and performance pressure is low.
- Transferable principle: If values are tagged unions, make ownership a first-class tag too.
- Related patterns: Zeroizing Secret Transfer Object; Opaque Text Offsets And Ranges.
- Risks / caveats: Every constructor, clone, and free path must preserve ownership flags.
- Agentic coding guidance: When adding an `SIType`, add constructor, comparison, hashing, stringification, clone, persist, and free behavior together.

### Reverse-Grouped Undo Log Rollback
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/redisgraph-src`; `src/undo_log/undo_log.h`, `src/undo_log/undo_log.c`.
- Language / framework / stack: C, graph mutation rollback.
- Evidence snippet:
```c
UndoLog UndoLog_New(void) {
    return (UndoLog)DataBlock_New(UNDOLOG_INIT_SIZE, UNDOLOG_INIT_SIZE, sizeof(UndoOp), NULL);
}

// apply undo operations in reverse order for rollback correctness
int seq_end = count - 1;
while (seq_end >= 0) {
    UndoOp *op = UNDOLOG_GET_ITEM(_log, seq_end);
    UndoOpType cur_type = op->type;
    int seq_start = seq_end;
    seq_end--;
    while(seq_end >= 0) {
        op = UNDOLOG_GET_ITEM(_log, seq_end);
        if(op->type != cur_type) break;
        seq_end--;
    }
    switch(cur_type) { /* bulk rollback by op type */ }
}
```
- Why it matters: Mutations can be undone in reverse order, while contiguous operations of the same type are bulk-rolled back for efficiency.
- When to use: Use for non-transactional in-memory or hybrid mutation systems that need best-effort rollback on query failure.
- When not to use: Avoid when the storage engine already provides atomic transactions with durable rollback.
- Transferable principle: Log inverse operations as data, then replay them backward and batch adjacent compatible inverses.
- Related patterns: Active Pending Index Double Buffer; Explicit Async State Machine Transitions.
- Risks / caveats: Missing one mutation kind from the undo log creates silent consistency gaps.
- Agentic coding guidance: When introducing a graph mutation, add the undo record type and rollback/free paths in the same patch.

### Typed Config Namespace With Mutability Scope
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/janusgraph-src`; `janusgraph-core/src/main/java/org/janusgraph/diskstorage/configuration/ConfigOption.java`, `janusgraph-core/src/main/java/org/janusgraph/graphdb/configuration/GraphDatabaseConfiguration.java`.
- Language / framework / stack: Java, JanusGraph configuration.
- Evidence snippet:
```java
public class ConfigOption<O> extends ConfigElement {
    public enum Type {
        FIXED, GLOBAL_OFFLINE, GLOBAL, MASKABLE, LOCAL
    }

    private final Type type;
    private final Class<O> datatype;
    private final O defaultValue;
    private final Predicate<O> verificationFct;
}

public static final ConfigNamespace GRAPH_NS = new ConfigNamespace(ROOT_NS,"graph",
        "General configuration options");

public static final ConfigOption<TimestampProviders> TIMESTAMP_PROVIDER =
    new ConfigOption<>(GRAPH_NS, "timestamps", "...",
        ConfigOption.Type.FIXED, TimestampProviders.class, TimestampProviders.MICRO);
```
- Why it matters: Configuration keys carry namespace, Java type, default, validation, and mutability rules in one declaration.
- When to use: Use for systems with many settings whose runtime mutability differs by deployment scope.
- When not to use: Avoid for small apps where typed config objects are enough.
- Transferable principle: Treat config definitions as schema objects, not string constants.
- Related patterns: Bounded Config Discovery Ladder; Schema-Validated Resource Stack Builder.
- Risks / caveats: Large static config registries can become hard to navigate without generated docs or search tooling.
- Agentic coding guidance: When adding a config option, choose mutability scope deliberately and add validation rather than relying on downstream failures.

### Temporary-Only Backend Retry Loop
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/janusgraph-src`; `janusgraph-core/src/main/java/org/janusgraph/diskstorage/util/BackendOperation.java`.
- Language / framework / stack: Java, storage backends, retry/backoff.
- Evidence snippet:
```java
public static <V> V executeDirect(Callable<V> exe, Duration totalWaitTime) throws BackendException {
    Duration waitTime = pertubTime(BASE_REATTEMPT_TIME);
    BackendException lastException;
    while (true) {
        try {
            return exe.call();
        } catch (final Throwable e) {
            Throwable ex = e;
            BackendException storeEx = null;
            do {
                if (ex instanceof BackendException) storeEx = (BackendException)ex;
            } while ((ex=ex.getCause())!=null);
            if (storeEx!=null && storeEx instanceof TemporaryBackendException) {
                lastException = storeEx;
            } else if (e instanceof BackendException) {
                throw (BackendException)e;
            } else {
                throw new PermanentBackendException("Permanent exception while executing backend operation "+exe.toString(),e);
            }
        }
        Thread.sleep(waitTime.toMillis());
        waitTime = pertubTime(waitTime.multipliedBy(2));
    }
}
```
- Why it matters: Retrying is reserved for explicitly temporary backend failures, while permanent failures surface immediately.
- When to use: Use around storage or network operations where exception taxonomy distinguishes transient and permanent faults.
- When not to use: Avoid if operations are not idempotent or retries can amplify overload.
- Transferable principle: Classify errors before retrying and jitter exponential backoff to avoid synchronized retries.
- Related patterns: Exponential Retry With Jitter And Semantic Tests; Feign Client Fallback For Degraded Cross-Service Calls.
- Risks / caveats: The operation must tolerate duplicate attempts.
- Agentic coding guidance: Do not add broad `catch Exception` retries; first define which exception means temporary and add tests for permanent pass-through.

### ErrorOr Partition Lookup Boundary
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/nebula-src`; `src/kvstore/NebulaStore.cpp`.
- Language / framework / stack: C++, NebulaGraph KV store, Raft partitions.
- Evidence snippet:
```cpp
ErrorOr<nebula::cpp2::ErrorCode, std::shared_ptr<Part>> NebulaStore::part(
    GraphSpaceID spaceId, PartitionID partId) {
  folly::RWSpinLock::ReadHolder rh(&lock_);
  auto it = spaces_.find(spaceId);
  if (UNLIKELY(it == spaces_.end())) {
    return nebula::cpp2::ErrorCode::E_SPACE_NOT_FOUND;
  }
  auto partIt = it->second->parts_.find(partId);
  if (UNLIKELY(partIt == it->second->parts_.end())) {
    return nebula::cpp2::ErrorCode::E_PART_NOT_FOUND;
  }
  return partIt->second;
}

auto ret = part(spaceId, partId);
if (!ok(ret)) { return error(ret); }
auto part = nebula::value(ret);
if (!checkLeader(part, canReadFromFollower)) {
  return part->isLeader() ? E_LEADER_LEASE_FAILED : E_LEADER_CHANGED;
}
```
- Why it matters: Missing space, missing partition, and leadership failure stay explicit at the store API boundary without exceptions.
- When to use: Use in distributed storage services where callers need machine-readable error codes.
- When not to use: Avoid when local invariants should crash fast rather than become recoverable status values.
- Transferable principle: Return either a domain error code or the resolved resource, then perform leadership/permission checks immediately after lookup.
- Related patterns: Normalized Boundary Value Objects For Network Policy; Backend-Specific Execution Engine With Metric Bundling.
- Risks / caveats: Callers must check `ok(ret)` before dereferencing.
- Agentic coding guidance: When adding a KV operation, start with `part(...)`, propagate its error, then apply leader/read-follower rules before touching the engine.

### Lazy Iterator Pipeline Compilation
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/blazegraph-src`; `ctc-striterators/src/main/java/cutthecrap/utils/striterators/Striterator.java`, `ctc-striterators/src/main/java/cutthecrap/utils/striterators/Filterator.java`.
- Language / framework / stack: Java, iterator combinators.
- Evidence snippet:
```java
private volatile List<IFilter> filters = null;
private volatile Iterator realSource;
private volatile Iterator m_src = null;

public boolean hasNext() {
    if (m_src == null)
        compile(realSource);
    boolean ret = m_src.hasNext();
    if (!ret) close();
    return ret;
}

public void compile(final Iterator src, final Object context) {
    if (m_src != null) throw new IllegalStateException();
    m_src = realSource = src;
    if (filters != null)
        for (IFilter filter : filters) {
            m_src = filter.filter(m_src, context);
        }
}
```
- Why it matters: Filters can be accumulated fluently, but the actual iterator chain is built only when consumed.
- When to use: Use when pipeline setup is conditional and the source may never be iterated.
- When not to use: Avoid when lazy compilation makes error timing surprising or thread ownership unclear.
- Transferable principle: Separate pipeline declaration from pipeline compilation, and compile once at the first consumption boundary.
- Related patterns: Picklable LRU File Managers; Backend Plugin Discovery With Explicit Signatures.
- Risks / caveats: Lazy state plus mutation requires clear lifecycle guards.
- Agentic coding guidance: When adding a new iterator transform, implement it as an `IFilter` wrapper and preserve single-compile semantics.

### Effectively Immutable Operator Annotation Map
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/blazegraph-src`; `bigdata-core/bigdata/src/java/com/bigdata/bop/BOpBase.java`.
- Language / framework / stack: Java, Blazegraph query operator tree.
- Evidence snippet:
```java
private final BOp[] args;
private final Map<String,Object> annotations;

public BOpBase(final BOpBase op) {
    if (op.args == BOp.NOARGS || op.args.length == 0) {
        args = BOp.NOARGS;
    } else {
        args = Arrays.copyOf(op.args, op.args.length);
    }
    annotations = new LinkedHashMap<String, Object>(op.annotations);
}

final public Map<String, Object> annotations() {
    return Collections.unmodifiableMap(annotations);
}
```
- Why it matters: Query operators can be cloned and shared with predictable visibility because args and annotations follow an effectively immutable contract.
- When to use: Use for planner or AST nodes that are transformed by copying instead of in-place mutation.
- When not to use: Avoid if nodes are intentionally mutable working objects.
- Transferable principle: Keep operator metadata final, expose read-only views, and require copy constructors for transformation.
- Related patterns: Inline-Or-Heap Compact Syntax Nodes; Native-Backing Adapter Conversion.
- Risks / caveats: `annotationsRef()` exists for hot spots, so local inspection must prove it is not mutated after construction.
- Agentic coding guidance: When adding fields to a `BOp`, update the copy constructor and avoid caching derived annotation references that can go stale after clone.

### Base Grammar Extension With Conflict Guards
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/intersystems__tree-sitter-objectscript`; `common/define_grammar.js`, `objectscript/grammar.js`, `objectscript_routine/grammar.js`.
- Language / framework / stack: JavaScript, tree-sitter grammar DSL.
- Evidence snippet:
```js
function define_grammar(baseGrammar, options) {
  if (baseGrammar.grammar.name == options.name) {
    throw 'Name conflict ';
  }
  for (const name in baseGrammar.grammar.rules) {
    if (options.rules[name] != undefined) {
      console.warn(`WARN: Duplicate rule name ${name}`);
    }
  }
  return grammar(baseGrammar, options);
}

module.exports = define_grammar(objectscript_core, {
  name: 'objectscript_routine',
  externals: ($, previous) => previous.concat([$.compiled_header, $.rtn_dot]),
  extras: ($, previous) => previous.concat([/\s/, $.documatic_line, $.rtn_dot]),
});
```
- Why it matters: Related language variants share a core grammar while dialect grammars append externals, extras, and rules deliberately.
- When to use: Use for parser families with a shared core plus dialect-specific top-level forms.
- When not to use: Avoid if dialects diverge enough that inheritance hides more than it saves.
- Transferable principle: Put grammar inheritance behind a helper that warns on rule collisions and forbids name conflicts.
- Related patterns: Generator Factory With Format Normalization; Domain DSL For Rust Item Names.
- Risks / caveats: Warnings are not hard failures for duplicate rules, so CI should still parse representative corpora.
- Agentic coding guidance: When adding a dialect rule, check whether it belongs in the shared core first, then add corpus tests for both base and derived grammars.

### External Scanner Wrapper With Serialized Core State
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/intersystems__tree-sitter-objectscript`; `common/scanner.h`, `objectscript/src/scanner.c`.
- Language / framework / stack: C, tree-sitter external scanner.
- Evidence snippet:
```c
struct ObjectScript_Udl_Scanner {
  char in_body;
  struct ObjectScript_Core_Scanner core_scanner;
};

struct ObjectScript_Udl_Scanner *scanner =
    (struct ObjectScript_Udl_Scanner *)payload;
return ObjectScript_Core_Scanner_scan(&scanner->core_scanner, lexer, valid_symbols);

unsigned tree_sitter_objectscript_external_scanner_serialize(void *payload, char *buffer) {
  struct ObjectScript_Udl_Scanner *scanner = (struct ObjectScript_Udl_Scanner *)payload;
  memcpy(buffer, scanner, sizeof(struct ObjectScript_Udl_Scanner));
  return sizeof(struct ObjectScript_Udl_Scanner);
}
```
- Why it matters: Dialect scanners can add special cases while delegating most lexing to a shared scanner and preserving incremental parser state.
- When to use: Use for tree-sitter grammars whose external tokens need state across incremental parses.
- When not to use: Avoid raw struct serialization if the scanner owns pointers or platform-dependent state.
- Transferable principle: Wrap shared scanner state compositionally, and serialize only plain data that tree-sitter can restore.
- Related patterns: Streaming JSON-RPC Reader State Machine; Opaque Text Offsets And Ranges.
- Risks / caveats: `memcpy` serialization is brittle if the struct layout changes or contains non-POD members.
- Agentic coding guidance: When adding scanner fields, confirm they are serializable, initialize them in `create`, and update corpus tests that exercise incremental/error recovery.

### Bookmark Manager For Causal Consistency
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4j-javascript-driver-src`; `packages/core/src/bookmark-manager.ts`, `packages/core/src/session.ts`.
- Language / framework / stack: TypeScript, Neo4j JavaScript driver.
- Evidence snippet:
```ts
class Neo4jBookmarkManager implements BookmarkManager {
  async updateBookmarks (previousBookmarks: Iterable<string>, newBookmarks: Iterable<string>): Promise<void> {
    const bookmarks = this._bookmarks
    for (const bm of previousBookmarks) {
      bookmarks.delete(bm)
    }
    for (const bm of newBookmarks) {
      bookmarks.add(bm)
    }
    if (typeof this._bookmarksConsumer === 'function') {
      await this._bookmarksConsumer([...bookmarks])
    }
  }

  async getBookmarks (): Promise<Iterable<string>> {
    const bookmarks = new Set(this._bookmarks)
    const suppliedBookmarks = await this._bookmarksSupplier?.() ?? []
    for (const bm of suppliedBookmarks) bookmarks.add(bm)
    return [...bookmarks]
  }
}
```
- Why it matters: Sessions can share causal-consistency bookmarks without coupling driver internals to a specific persistence mechanism.
- When to use: Use for clients that need to coordinate read-after-write consistency across sessions or processes.
- When not to use: Avoid sharing one manager across unrelated workloads if the added dependencies reduce routing freedom.
- Transferable principle: Model consistency tokens as a mergeable set with update and supplier/consumer hooks.
- Related patterns: Cached Binding Context With Lifecycle Drain; Concurrent Tunnel Dedup State Map.
- Risks / caveats: The session intentionally swallows bookmark-manager update failures, so external persistence must be monitored separately.
- Agentic coding guidance: When changing session completion, preserve `previousBookmarks` deletion and new bookmark insertion semantics.

### Dual-Mapped Project Cache With Watcher Cleanup
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/nendotools__tree-sitter-mcp`; `src/project/persistent-manager.ts`.
- Language / framework / stack: TypeScript, tree-sitter MCP server, in-memory project cache.
- Evidence snippet:
```ts
export interface PersistentProjectManager {
  memory: MemoryManager
  directoryToProject: Map<string, string>
  projectToDirectory: Map<string, string>
  watchers: Map<string, () => void>
}

const existingDirectory = manager.projectToDirectory.get(dirName)
if (!existingDirectory || existingDirectory === directory) {
  return dirName
}
const hash = createHash('md5').update(directory).digest('hex').substring(0, 8)
return `${dirName}-${hash}`

function stopWatching(manager: PersistentProjectManager, projectId: string): void {
  const stopWatcher = manager.watchers.get(projectId)
  if (stopWatcher) {
    stopWatcher()
    manager.watchers.delete(projectId)
  }
}
```
- Why it matters: Directory lookups, project-id lookups, collision-safe generated IDs, LRU eviction, and watcher teardown are handled as one cache lifecycle.
- When to use: Use for language servers, MCP servers, and indexers that cache many parsed workspaces.
- When not to use: Avoid if project identity is externally assigned and stable, making generated IDs unnecessary.
- Transferable principle: Keep forward and reverse identity maps together, and make eviction stop side-effectful resources before removing cache entries.
- Related patterns: Lock-Free Probe Then Locked Download Registry; Bounded Discovery With Excluded Subtree Reporting.
- Risks / caveats: Hash-shortened IDs can still collide in theory; critical systems should detect and resolve that explicitly.
- Agentic coding guidance: When touching project cache code, update add, update-directory, remove, clear, and watcher cleanup paths as a single lifecycle.

## Worker 3 Batch 5

Counts: inspected 7 requested repos with `find`, `rg`, `sed`, `sort`, and direct source reads; added 13 source-backed entries from 6 repos; skipped 1 repo. Skipped `/Users/amuldotexe/Desktop/personal-repos-lane/before-i-go` because `find` surfaced prose/text files only (`Readme.txt`, `sectionsList.txt`, and section `.txt` articles), not useful source-code evidence.

### Evicting MCP Session Cache With Async ExitStack Cleanup
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/LiveMCPBench`; `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/LiveMCPBench/utils/mcp_client.py`.
- Language / framework / stack: Python, asyncio, MCP client sessions, cachetools LRU, `AsyncExitStack`.
- Code shape / snippet:
```python
class LRUCacheWithCallback(LRUCache):
    def popitem(self):
        key, value = super().popitem()
        if self.on_evict:
            self.on_evict(key, value)
        return key, value

def on_eviction(server_id, session):
    asyncio.create_task(self.cleanup_server(server_id))

async def mcp_session_runner() -> None:
    exit_stack = AsyncExitStack()
    try:
        await self.connect_to_server(server_id, command, args, env, exit_stack)
        stop_event = asyncio.Event()
        self.stop_event[server_id] = stop_event
        self.task[server_id] = asyncio.current_task()
        await stop_event.wait()
    finally:
        await exit_stack.aclose()
```
- Why it matters: Long-lived MCP transports are cached by server id, bounded by LRU size, and tied to a cleanup signal so subprocess/SSE resources are not leaked when sessions churn.
- When to use: Use for agent runtimes that connect to many external tool servers but should keep only a bounded working set warm.
- When not to use: Avoid when every call must run in a fresh isolated process or when server sessions carry request-specific credentials.
- Transferable principle: Put connection lifetime, eviction, and async resource cleanup in one owner rather than scattering stop events across call sites.
- Related patterns: Two-Stage Embedding Router With Structured Tool Tags; Bounded Agent Routing Memory With Sample Floors.
- Risks / caveats: `asyncio.create_task` cleanup is fire-and-forget; shutdown paths still need an explicit `cleanup()` pass to await outstanding session teardown.
- Agentic coding guidance: When adding a new MCP transport, route it through the same `AsyncExitStack` and `stop_event` lifecycle, then test eviction and explicit cleanup separately.

### Two-Stage Embedding Router With Structured Tool Tags
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/LiveMCPBench`; `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/LiveMCPBench/baseline/mcp_copilot/matcher.py`, `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/LiveMCPBench/baseline/mcp_copilot/router.py`.
- Language / framework / stack: Python, OpenAI-compatible embeddings, MCP router, NumPy cosine similarity.
- Code shape / snippet:
```python
self.tool_assistant_pattern = re.compile(
    r"<tool_assistant>\s*server:\s*(.*?)\s*tool:\s*(.*?)\s*</tool_assistant>",
    re.DOTALL,
)

matched_servers = self.match_servers(server_desc)
matched_tools = self.match_tools(matched_servers, tool_desc)

final_score = (server_score * tool_similarity) * max(
    server_score, tool_similarity
)
tool_scores.sort(key=lambda x: x["final_score"], reverse=True)
```
- Why it matters: The router first narrows candidate servers, then ranks tools inside those servers, which reduces false positives compared with one flat nearest-neighbor search over every tool.
- When to use: Use when tool catalogs are large and each tool belongs to a meaningful server/provider grouping.
- When not to use: Avoid when the catalog is tiny, when embeddings are unavailable, or when deterministic policy rules must dominate similarity scoring.
- Transferable principle: Split retrieval into coarse entity selection and fine-grained action selection, and make the handoff format explicit.
- Related patterns: Evicting MCP Session Cache With Async ExitStack Cleanup; Pure Word-Boundary Signal Router.
- Risks / caveats: The `<tool_assistant>` tag is a brittle protocol; malformed model output returns no matches even if the natural-language intent is obvious.
- Agentic coding guidance: Generate tests for missing tags, bad tags, empty embeddings, and low-similarity ties before changing the score formula.

### Pure Word-Boundary Signal Router
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute`; `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute/src/lib/model-routing.ts`.
- Language / framework / stack: TypeScript, Next.js support library, deterministic LLM model routing.
- Code shape / snippet:
```ts
function matchesWordBoundary(lower: string, keywords: string[]): boolean {
  for (const kw of keywords) {
    const escaped = kw.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
    if (new RegExp(`\\b${escaped}\\b`, 'i').test(lower)) return true
  }
  return false
}

export function detectTaskSignals(task: string): TaskSignals {
  const tools_needed = matchesWordBoundary(lower, SIGNAL_KEYWORDS.tools_needed)
  const code_present = matchesWordBoundary(lower, SIGNAL_KEYWORDS.code_present)
  const signal_count = [tools_needed, code_present, complex_reasoning].filter(Boolean).length
  return { tools_needed, structured_output_needed, code_present, complex_reasoning, creative_writing, signal_count }
}
```
- Why it matters: Routing signals are pure functions and use word boundaries to prevent substring mistakes such as `class` matching `classification` or `plan` matching unrelated text.
- When to use: Use for fast, explainable routing heuristics where false-positive keywords are expensive.
- When not to use: Avoid as the only classifier for nuanced product decisions where live context or semantic intent is required.
- Transferable principle: Keep routing heuristics pure, testable, and conservative; make keyword matching precise before adding more keywords.
- Related patterns: Two-Stage Embedding Router With Structured Tool Tags; Bounded Agent Routing Memory With Sample Floors.
- Risks / caveats: Regex word boundaries can still miss domain phrases with punctuation, casing conventions, or non-English text.
- Agentic coding guidance: Whenever adding a keyword, add a positive example and at least one near-miss negative example that proves it does not overfire.

### Bounded Agent Routing Memory With Sample Floors
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute`; `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute/src/lib/routing-memory.ts`, `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/ToolRoute/src/app/api/route/model/route.ts`.
- Language / framework / stack: TypeScript, Supabase, Next.js API routes, agent personalization.
- Code shape / snippet:
```ts
export const MIN_SAMPLES = 3
const DEFAULT_TIMEOUT_MS = 200

const work = lookup(supabase, agentIdentityId, taskCluster, limit)
const timer = new Promise<null>(resolve => setTimeout(() => resolve(null), timeoutMs))
return await Promise.race([work, timer])

if (paired.length < MIN_SAMPLES) return null
const success_rate = Math.round((successful.length / sample_size) * 100) / 100
const historical_model = successful[0]?.dec.recommended_model_slug ?? null
```
- Why it matters: Historical routing advice is useful only when it is fast and backed by enough outcomes; the lookup never blocks the primary route for more than 200ms.
- When to use: Use for agent-specific personalization where stale or sparse history should be advisory, not authoritative.
- When not to use: Avoid when the route must be fully deterministic or when historical outcomes are biased, untrusted, or not comparable by task cluster.
- Transferable principle: Treat memory as a bounded hint with a sample floor and timeout, not as a mandatory dependency in latency-sensitive handlers.
- Related patterns: Pure Word-Boundary Signal Router; Atomic Checkpoint Closures For Resumable Batch Runs.
- Risks / caveats: Cluster keys determine whether history is comparable; too-broad clusters can reinforce the wrong past choice.
- Agentic coding guidance: Before using memory to override a recommendation, verify the sample size, success threshold, and cluster derivation in tests.

### Docstring-Derived Tool Schemas With Prebound Arguments
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench`; `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench/src/tau2/environment/tool.py`, `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench/src/tau2/environment/toolkit.py`.
- Language / framework / stack: Python, Pydantic, docstring parser, LLM tool calling.
- Code shape / snippet:
```python
doc = parse(docstring or "")
for name, param in sig.parameters.items():
    if name in doc_param:
        default = Field(default, description=doc_param[name].description)
    if name not in predefined:
        params[name] = (anno, default)
data["params"] = create_model("parameters", **params)

def _call(self, *args: Any, **kwargs: Any) -> Any:
    kwargs.update(self._predefined)
    return self._func(*args, **kwargs)
```
- Why it matters: Ordinary Python functions become callable LLM tools with JSON schemas, parameter descriptions, return schemas, and hidden prebound dependencies such as environment handles.
- When to use: Use in simulation frameworks where domain actions should be real functions but also exposed to agents as structured tools.
- When not to use: Avoid when docstrings are incomplete or untrusted; generated schemas will be only as good as the function signatures and docs.
- Transferable principle: Derive tool contracts from function boundaries, then prebind runtime-only dependencies so the model sees only user-relevant parameters.
- Related patterns: Registry-Composed Retrieval Pipeline With Scoped Overrides; Arrow-Native Python UDF Bridge.
- Risks / caveats: Missing type annotations fall back to `Any`, which weakens schema validation and can hide agent argument errors.
- Agentic coding guidance: When adding a tool, write the typed function and docstring first, then inspect `openai_schema` in a test before exposing it to an agent prompt.

### Registry-Composed Retrieval Pipeline With Scoped Overrides
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench`; `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench/src/tau2/knowledge/pipeline.py`.
- Language / framework / stack: Python, dataclasses, retrieval/reranking pipeline, registry-resolved components.
- Code shape / snippet:
```python
self.doc_preprocessors = [
    get_document_preprocessor(dp["type"], dp.get("params", {}))
    for dp in config.get("document_preprocessors", [])
]
self.retrievers = [
    get_retriever(ret["type"], ret.get("params", {}))
    for ret in config["retrievers"]
]

if self._retriever_top_k_override is not None:
    original_retriever_top_ks.append((retriever, retriever.top_k))
    retriever.top_k = self._retriever_top_k_override
...
for retriever, orig_top_k in original_retriever_top_ks:
    retriever.top_k = orig_top_k
```
- Why it matters: Retrieval is assembled from named components, supports multiple retrievers, records timings, and restores temporary `top_k` overrides after each call.
- When to use: Use for RAG systems where indexing, query preprocessing, retrieval, and postprocessing need to vary by config.
- When not to use: Avoid when a single direct database lookup is enough or when mutable component overrides could race across concurrent requests.
- Transferable principle: Compose retrieval from registry-resolved stages and restore temporary state before returning.
- Related patterns: Docstring-Derived Tool Schemas With Prebound Arguments; Bounded Agent Routing Memory With Sample Floors.
- Risks / caveats: Overrides mutate retriever instances; shared pipelines need synchronization or per-request clones.
- Agentic coding guidance: When adding a retriever or postprocessor, implement single-query and batch paths together and test that overrides are restored after exceptions.

### Atomic Checkpoint Closures For Resumable Batch Runs
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench`; `/Users/amuldotexe/Desktop/personal-repos-lane/accio-tools/ignore-references/git-ref-repo/tau2-bench/src/tau2/runner/checkpoint.py`.
- Language / framework / stack: Python, multiprocessing locks, Pydantic simulation models, atomic filesystem writes.
- Code shape / snippet:
```python
def create_checkpoint_fns(save_path: Optional[Path], lock: multiprocessing.Lock):
    _key_to_sim_id: dict[tuple, str] = {}
    _saved_keys: set[tuple] = set()

    def _save_dir(simulation: SimulationRun):
        sim_key = (simulation.trial, simulation.task_id, simulation.seed)
        with lock:
            if sim_key in _saved_keys:
                return
            fd, tmp_path = tempfile.mkstemp(suffix=".json", prefix=".sim_", dir=sims_dir)
            with os.fdopen(fd, "w") as fp:
                fp.write(simulation.model_dump_json(indent=2))
            os.replace(tmp_path, sim_path)
            _key_to_sim_id[sim_key] = simulation.id
            _flush_index()
```
- Why it matters: Batch runs can append or replace simulations safely while avoiding duplicate saves, partial files, and expensive directory scans.
- When to use: Use for long-running evaluations where individual run results arrive over time and crashes should be resumable.
- When not to use: Avoid for transactional databases or object stores that already provide atomic writes and indexes.
- Transferable principle: Return paired save/replace closures that share just enough in-memory index state to make checkpoint updates cheap and consistent.
- Related patterns: Bounded Agent Routing Memory With Sample Floors; Evicting MCP Session Cache With Async ExitStack Cleanup.
- Risks / caveats: In-memory `_key_to_sim_id` is seeded only from metadata; external file edits can desynchronize the index.
- Agentic coding guidance: When changing checkpoint formats, test resume, duplicate save, infrastructure-error replacement, and crash-during-write behavior.

### Observable Grid State With Validated Tile Values
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129`; `/Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129/app/game/game-board.ts`, `/Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129/app/game/tile.ts`.
- Language / framework / stack: TypeScript, NativeScript `Observable`, simple game state model.
- Code shape / snippet:
```ts
export class Tile {
  constructor(color: ColorValue) {
    if (!Object.values(COLORS).includes(color)) {
      throw new Error(`Invalid color: ${color}`);
    }
    this._color = color;
  }
}

public async tryMatch(row: number, col: number) {
  const matches = this.findMatches(row, col);
  if (matches.length >= GAME_CONFIG.MIN_MATCH - 1) {
    this._score += GAME_CONFIG.MIN_MATCH * GAME_CONFIG.POINTS_PER_TILE;
    this.notifyPropertyChange('score', this._score);
    matches.forEach(([r, c]) => this._grid[r][c] = new Tile(this.getRandomColor()));
    this.notifyPropertyChange('grid', this._grid);
    return true;
  }
  return false;
}
```
- Why it matters: The board owns scoring and match replacement, while tile values guard invalid colors at construction and mutation boundaries.
- When to use: Use for small UI games or interactive widgets where view updates should follow domain state changes.
- When not to use: Avoid for complex games that need deterministic replay, animation timelines, or a separate physics/event engine.
- Transferable principle: Keep UI notification at state mutation boundaries and wrap primitive domain values when invalid states are easy to create.
- Related patterns: Docstring-Derived Tool Schemas With Prebound Arguments; Pure Word-Boundary Signal Router.
- Risks / caveats: Random replacement inside the domain object makes deterministic tests harder unless randomness is injectable.
- Agentic coding guidance: When extending this game logic, inject or seed randomness in tests and keep `notifyPropertyChange` calls close to the mutations they publish.

### Retryable Error Typing Around Cypher Requests
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4rs-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4rs-src/lib/src/retry.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4rs-src/lib/src/query.rs`.
- Language / framework / stack: Rust, async Neo4j driver, Bolt protocol, typed errors.
- Code shape / snippet:
```rust
pub enum Retry<E> {
    Yes(E),
    No(E),
}

fn wrap_error<T>(resp: impl IntoError, req: &'static str) -> QueryResult<T> {
    let error = resp.into_error(req);
    let can_retry = match &error {
        Error::Neo4j(e) => e.can_retry(),
        _ => false,
    };
    if can_retry { Err(Retry::yes(error)) } else { Err(Retry::no(error)) }
}

self.pool.get(...).await.map_err(Retry::No)
```
- Why it matters: Retryability travels with the error value, so retry loops can distinguish transient Neo4j failures from permanent connection-pool failures.
- When to use: Use in clients that need safe retries across network/database operations with protocol-specific transient error classes.
- When not to use: Avoid if retries are always forbidden or if the underlying operation is not idempotent and cannot be made safe.
- Transferable principle: Encode retry policy in result types near the operation boundary, not as an undocumented side channel.
- Related patterns: Format-Like Query Macro With Named Parameters; Detached Row Stream Owns Its Connection.
- Risks / caveats: Marking too many errors retryable can duplicate writes; marking too few retryable can reduce resilience.
- Agentic coding guidance: When adding a new protocol error, classify retryability in one place and write tests for both `Retry::Yes` and `Retry::No` paths.

### Format-Like Query Macro With Named Parameters
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4rs-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4rs-src/lib/src/query.rs`.
- Language / framework / stack: Rust, declarative macros, Neo4j Cypher query builder.
- Code shape / snippet:
```rust
impl<T: Into<BoltType>> std::fmt::Display for QueryParameter<'_, T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let Some(v) = self.value.replace(None) else {
            return Err(std::fmt::Error);
        };
        self.params.borrow_mut().put(self.name.into(), v.into());
        write!(f, "${}", self.name)
    }
}

(@internal $query:expr, [$($acc:tt)*]; $value:expr $(, $($rest:tt)*)?) => {
    compile_error!("Only named parameter syntax (`name = value`) is supported");
};
```
- Why it matters: Users get `format!`-style ergonomics while named values become Bolt parameters instead of string interpolation.
- When to use: Use for query DSLs where developers want inline readability but the runtime must preserve parameter binding.
- When not to use: Avoid for arbitrary SQL/Cypher fragments where identifier interpolation, dynamic clauses, or schema names need separate escaping rules.
- Transferable principle: Let ergonomic macros produce safe parameter maps, and reject ambiguous unnamed forms at compile time.
- Related patterns: Retryable Error Typing Around Cypher Requests; Python DataFrame Facade Over Rust Async Plan Execution.
- Risks / caveats: Implicit `{name}` without a `name = value` argument falls back to normal interpolation, so documentation and tests must make that limitation visible.
- Agentic coding guidance: When generating query code, prefer explicit `name = value` macro arguments and add assertions for both rendered query text and parameter map contents.

### Detached Row Stream Owns Its Connection
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4rs-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/neo4rs-src/lib/src/stream.rs`.
- Language / framework / stack: Rust, async streaming, futures `TryStream`, Neo4j connection pool.
- Code shape / snippet:
```rust
pub struct DetachedRowStream {
    stream: RowStream,
    connection: ManagedConnection,
}

pub async fn next(&mut self) -> Result<Option<Row>> {
    self.stream.next(&mut self.connection).await
}

pub fn into_stream(&mut self) -> impl TryStream<Ok = Row, Error = Error> + '_ {
    self.stream.into_stream(&mut self.connection)
}

pub async fn finish(mut self) -> Result<RunResult> {
    self.stream.finish(&mut self.connection).await
}
```
- Why it matters: A result stream returned outside a transaction still owns the connection it needs, and the connection is released when the detached stream is dropped.
- When to use: Use when streaming results must outlive the immediate query call but still need exclusive access to a network connection.
- When not to use: Avoid when results are always fully buffered or when a connection must remain managed by an explicit transaction scope.
- Transferable principle: Bundle dependent resources with lazy streams so callers cannot accidentally consume data after its transport is gone.
- Related patterns: Retryable Error Typing Around Cypher Requests; Python DataFrame Facade Over Rust Async Plan Execution.
- Risks / caveats: Holding a detached stream open also holds a pooled connection, so slow consumers can starve the pool.
- Agentic coding guidance: When adding stream helpers, preserve the owned-connection wrapper and include tests for partial consumption plus `finish()`.

### Python DataFrame Facade Over Rust Async Plan Execution
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-python-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-python-src/python/datafusion/dataframe.py`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-python-src/crates/core/src/dataframe.rs`.
- Language / framework / stack: Python, Rust, PyO3, Apache Arrow, DataFusion logical/physical plans.
- Code shape / snippet:
```python
def collect(self) -> list[pa.RecordBatch]:
    """Execute this DataFrame and collect results into memory."""
    return self.df.collect()
```
```rust
fn create_and_cache_plan(
    &self,
    py: Python,
) -> PyDataFusionResult<(Arc<dyn DFExecutionPlan>, Arc<TaskContext>)> {
    let new_plan = wait_for_future(py, df.create_physical_plan())??;
    *self.last_plan.lock() = Some(Arc::clone(&new_plan));
    Ok((new_plan, Arc::new(self.df.as_ref().task_ctx())))
}

fn collect<'py>(&self, py: Python<'py>) -> PyResult<Vec<Bound<'py, PyAny>>> {
    let (plan, task_ctx) = self.create_and_cache_plan(py)?;
    let batches = wait_for_future(py, df_collect(plan, task_ctx))?;
    batches?.into_iter().map(|rb| rb.to_pyarrow(py)).collect()
}
```
- Why it matters: The Python API stays small and lazy, while Rust owns plan creation, execution, metrics caching, and Arrow conversion.
- When to use: Use when exposing a high-performance Rust engine through a Pythonic API without duplicating execution logic in Python.
- When not to use: Avoid when Python-level behavior needs to be independently extensible without recompiling native bindings.
- Transferable principle: Keep language bindings ergonomic and thin; centralize execution semantics in the native core.
- Related patterns: Arrow-Native Python UDF Bridge; Format-Like Query Macro With Named Parameters.
- Risks / caveats: Async execution hidden behind synchronous Python methods can surprise users if long queries block their thread.
- Agentic coding guidance: When adding a DataFrame method, implement the Rust binding first, then keep the Python wrapper as a typed one-line facade plus documentation.

### Arrow-Native Python UDF Bridge
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-python-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-python-src/crates/core/src/udf.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/datafusion-python-src/python/datafusion/context.py`.
- Language / framework / stack: Rust, Python, PyO3, Apache Arrow C data interface, DataFusion scalar UDFs.
- Code shape / snippet:
```rust
fn invoke_with_args(&self, args: ScalarFunctionArgs) -> datafusion::common::Result<ColumnarValue> {
    Python::attach(|py| {
        let py_args = args.args.into_iter().zip(args.arg_fields)
            .map(|(arg, field)| {
                let array = arg.to_array(num_rows)?;
                PyArrowArrayExportable::new(array, field).to_pyarrow(py)
            })
            .collect::<Result<Vec<_>, _>>()?;
        let value = self.func.call(py, PyTuple::new(py, py_args)?, None)?;
        let array_data = ArrayData::from_pyarrow_bound(value.bind(py))?;
        Ok(ColumnarValue::Array(make_array(array_data)))
    })
}
```
- Why it matters: Python UDFs receive Arrow arrays and return Arrow-compatible arrays, so vectorized execution crosses the Python/Rust boundary without row-by-row marshalling.
- When to use: Use for analytics engines that need Python extensibility but want to preserve columnar execution.
- When not to use: Avoid for scalar Python functions that are inherently row-oriented or have side effects per row.
- Transferable principle: Bridge extension hooks with the engine's native batch format, not with per-record adapter objects.
- Related patterns: Python DataFrame Facade Over Rust Async Plan Execution; Docstring-Derived Tool Schemas With Prebound Arguments.
- Risks / caveats: Python callable failures are converted into execution errors; equality/hash behavior around Python functions is intentionally conservative.
- Agentic coding guidance: When creating new UDF bindings, test Arrow type conversion, null handling, Python exceptions, and cross-process/capsule reconstruction paths.

## Worker 3 Batch 6

Counts: inspected 8 requested repos with `rg`, `find`, `sed`, `awk`, `sort`, and direct source reads; added 14 source-backed entries from 7 repos; skipped 1 repo. Skipped `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/graphblas-pointers-src` because `rg --files` and `find | awk | sort` showed a pointer README, PDFs, and config/index files, but no implementation source suitable for idiomatic code-pattern extraction.

### Polyglot Parameterized Cypher Driver Session
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/graph-data-science-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/graph-data-science-src/code/python/example.py`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/graph-data-science-src/code/java/Example.java`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/Neo4j family/graph-data-science-src/code/javascript/example.js`.
- Language / framework / stack: Neo4j drivers across Python, Java, and JavaScript; Bolt sessions; parameterized Cypher.
- Code shape / snippet:
```python
with driver.session(database="neo4j") as session:
    results = session.read_transaction(
        lambda tx: tx.run(cypher_query, name="Jaime Lannister").data())
```
```java
var result = session.readTransaction(
    tx -> tx.run(cypherQuery, parameters("name", "Jaime Lannister")).list());
```
```javascript
session.run(query, {"name": "Jaime Lannister})
  .then((result) => result.records.forEach((record) => {
    console.log(record.get('person'));
  }));
```
- Why it matters: The examples keep one Cypher shape and one parameter name across languages, so users learn the session/transaction boundary instead of language-specific string interpolation habits.
- When to use: Use when documenting a database feature that must feel equivalent across client ecosystems.
- When not to use: Avoid for deep driver internals or advanced transaction control where each language exposes materially different capabilities.
- Transferable principle: Keep the domain query stable and let each host language express only connection, session, and resource cleanup idioms.
- Related patterns: Format-Like Query Macro With Named Parameters; Retryable Error Typing Around Cypher Requests.
- Risks / caveats: Example-level cleanup can be incomplete on failure paths, especially in promise chains; production snippets should use `finally`/try-with-resources consistently.
- Agentic coding guidance: When generating cross-language examples, preserve query text and parameter names exactly, then adapt only the smallest surrounding resource-management shell.

### Memory-Budgeted Partition Edge Streaming
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src/core/graph.hpp`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src/examples/bfs.cpp`.
- Language / framework / stack: C++, OpenMP, direct I/O, shard-partitioned graph processing.
- Code shape / snippet:
```cpp
if (memory_bytes < total_bytes) {
    read_mode = O_RDONLY | O_DIRECT;
} else {
    read_mode = O_RDONLY;
}

tasks.push(std::make_tuple(fin, offset, IOSIZE));
...
if (bitmap==nullptr || bitmap->get_bit(e.source)) {
    local_value += process(e);
}
```
- Why it matters: Edge traversal is expressed as a callback while the graph runtime chooses shard access, direct-vs-buffered I/O, and task partitioning from the memory budget.
- When to use: Use for out-of-core graph algorithms where the algorithm should say "process matching edges" and the storage layer should decide how to stream them.
- When not to use: Avoid for small in-memory graphs where the I/O scheduler and partition metadata add complexity without payoff.
- Transferable principle: Put memory-budget decisions beside storage metadata, then expose algorithm callbacks over already-filtered partitions.
- Related patterns: Mmap-Backed BigVector Windowing; Frontier-Gated Notification Session.
- Risks / caveats: The callback can hide random writes into vertex state; algorithms still need atomic updates or partition-local ownership to stay correct.
- Agentic coding guidance: When adding a GridGraph algorithm, call `graph.hint(...)`, pass active bitmaps when available, and keep mutation rules explicit in the callback.

### Mmap-Backed BigVector Windowing
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src/core/bigvector.hpp`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/gridgraph-src/core/partition.hpp`.
- Language / framework / stack: C++, POSIX `mmap`, `pread`/`pwrite`, OpenMP.
- Code shape / snippet:
```cpp
data = (T *)mmap(NULL, sizeof(T) * length,
                 PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

void load(size_t begin_i, size_t end_i) {
    close_mmap();
    data_in_memory = (T *)mmap(0, bytes, PROT_READ | PROT_WRITE,
                               MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    bytes = pread(fd, data_in_memory + offset, length, offset);
}
```
- Why it matters: The same vector abstraction supports full-file memory mapping and explicit hot-window loading when vertex state exceeds the configured budget.
- When to use: Use when algorithms need array-like syntax over state too large to assume resident in RAM.
- When not to use: Avoid when the vector is small, when portability beyond POSIX is required, or when crash-consistent writes need a journaling layer.
- Transferable principle: Keep the indexing API stable while swapping storage residency strategies underneath it.
- Related patterns: Memory-Budgeted Partition Edge Streaming; Dirty-State Flush Epoch Pipeline.
- Risks / caveats: Alignment, page rounding, and direct I/O constraints are easy to break; the abstraction relies on assertions rather than recoverable errors.
- Agentic coding guidance: When editing `BigVector`, verify load/save offsets, page alignment, and `in_memory` transitions together; never change `operator[]` semantics without checking window bounds.

### Abstract Algorithm Validation Fixture With Epsilon Matching
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src/graphalytics-validation/src/main/java/science/atlarge/graphalytics/validation/algorithms/pr/PageRankValidationTest.java`.
- Language / framework / stack: Java, JUnit, Hamcrest, Graphalytics algorithm validation.
- Code shape / snippet:
```java
public abstract PageRankOutput executeDirectedPageRank(
        GraphStructure graph, PageRankParameters parameters) throws Exception;

@Test
public final void testDirectedPageRankOnValidationGraph() throws Exception {
    GraphStructure inputGraph = GraphParser.parseGraphStructureFromVertexBasedDataset(
            getClass().getResourceAsStream(inputPath), true);
    validatePageRank(executionResult, outputPath);
}

assertThat("vertex " + vertexId + " has correct value",
        deviation, is(closeTo(0.0, EPSILON)));
```
- Why it matters: Platform integrations implement only the abstract execution hooks, while the shared fixture owns canonical inputs, expected outputs, and numeric tolerance.
- When to use: Use when many backends must prove conformance to the same graph algorithm contract.
- When not to use: Avoid when each backend has legitimately different semantics or when expected output cannot be captured independently of the implementation.
- Transferable principle: Separate "run this backend" from "validate this algorithm" so conformance tests stay reusable and comparable.
- Related patterns: Comment-Tolerant Graph Dataset Parser; Classpath Plugin Lifecycle Fanout.
- Risks / caveats: Relative deviation can behave poorly around expected zero values; validation fixtures should choose absolute or mixed tolerances per metric.
- Agentic coding guidance: When adding a new algorithm fixture, define abstract directed/undirected execution hooks first, then add sample-resource tests before backend code.

### Comment-Tolerant Graph Dataset Parser
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src/graphalytics-validation/src/main/java/science/atlarge/graphalytics/validation/io/GraphParser.java`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src/graphalytics-validation/src/main/java/science/atlarge/graphalytics/validation/GraphValues.java`.
- Language / framework / stack: Java, buffered stream parsing, generic value parsers.
- Code shape / snippet:
```java
line = line.trim();
if (line.isEmpty() || line.startsWith("#")) {
    continue;
}

String tokens[] = line.split(" ");
long sourceVertex = Long.parseLong(tokens[0]);
edges.put(sourceVertex, new HashSet<Long>());
...
if (!directed) {
    edges.get(destinationVertex).add(sourceVertex);
}
```
- Why it matters: Validation resources can include comments and sparse adjacency rows, and the parser expands undirected inputs into symmetric edges in one place.
- When to use: Use for benchmark fixture loaders and golden-test data where human-readable files need forgiving comments but deterministic parsing.
- When not to use: Avoid for high-throughput production ingestion; repeated string splitting and boxed collections are tuned for clarity, not bulk loading.
- Transferable principle: Normalize fixture data at the parser boundary so every validation test consumes the same graph model.
- Related patterns: Abstract Algorithm Validation Fixture With Epsilon Matching; Polyglot Parameterized Cypher Driver Session.
- Risks / caveats: `split(" ")` treats only a single literal space as the separator; tabs or repeated spaces can produce surprising tokens.
- Agentic coding guidance: When extending fixture formats, add parser tests for blank lines, comments, directed/undirected expansion, and value-parser failures.

### Classpath Plugin Lifecycle Fanout
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_graphalytics-src/graphalytics-core/src/main/java/science/atlarge/graphalytics/plugin/Plugins.java`.
- Language / framework / stack: Java, classpath resource discovery, plugin factories, benchmark lifecycle hooks.
- Code shape / snippet:
```java
Enumeration<URL> resources = Plugins.class.getClassLoader()
        .getResources("META-INF/graphalytics/plugins");

Class<? extends PluginFactory> pluginFactoryClass =
        Class.forName(pluginFactoryClassName).asSubclass(PluginFactory.class);
PluginFactory pluginFactory = pluginFactoryClass.newInstance();
return pluginFactory.instantiatePlugin(targetPlatform, benchmark, reportWriter);
```
- Why it matters: Plugins can be added by classpath resource declaration, then receive lifecycle fanout for suite setup, per-run preparation, termination, reporting, and shutdown.
- When to use: Use when benchmark/report integrations should be optional modules discovered at runtime.
- When not to use: Avoid when plugin loading must be sandboxed, version-negotiated, or isolated from the host classloader.
- Transferable principle: Discover extension factories from a tiny manifest, then keep lifecycle invocation explicit and ordered in one coordinator.
- Related patterns: Abstract Algorithm Validation Fixture With Epsilon Matching; Named Tokenizer Pipeline Registry.
- Risks / caveats: Reflection failures are logged and skipped, which can hide missing observability plugins unless startup logs are monitored.
- Agentic coding guidance: When adding lifecycle hooks, update both `Plugin` and the `Plugins` fanout class, then test classpath discovery with a fake `META-INF` resource.

### Trait-Templated Graph Traversal Surface
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/petgraph-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/petgraph-src/crates/petgraph/src/visit/mod.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/petgraph-src/crates/petgraph/src/algo/dijkstra.rs`.
- Language / framework / stack: Rust, graph traits, generic algorithms, macro-assisted trait delegation.
- Code shape / snippet:
```rust
pub trait IntoEdges : IntoEdgeReferences + IntoNeighbors {
    type Edges: Iterator<Item=Self::EdgeRef>;
    fn edges(self, a: Self::NodeId) -> Self::Edges;
}

pub fn dijkstra<G, F, K>(graph: G, start: G::NodeId, goal: Option<G::NodeId>, edge_cost: F)
where
    G: IntoEdges + Visitable,
    F: FnMut(G::EdgeRef) -> K,
{
    /* generic traversal over graph.edges(node) */
}
```
- Why it matters: Algorithms target small composable traversal traits instead of concrete graph structs, so `Graph`, `StableGraph`, `GraphMap`, and CSR-like types can share code.
- When to use: Use when a library has multiple graph representations but wants one algorithm implementation surface.
- When not to use: Avoid when the algorithm depends on representation-specific mutation, storage layout, or asymptotic guarantees not captured by traits.
- Transferable principle: Define the minimum behavioral traits an algorithm needs, then implement those traits across storage backends.
- Related patterns: Total-Order Score Wrapper For BinaryHeap; Memory-Budgeted Partition Edge Streaming.
- Risks / caveats: Trait families can become hard to navigate; adding a new representation means proving many small trait contracts.
- Agentic coding guidance: When writing a new Petgraph algorithm, start from bounds like `IntoEdges + Visitable`, and add stronger traits only after a concrete operation requires them.

### Total-Order Score Wrapper For BinaryHeap
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/petgraph-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/petgraph-src/crates/petgraph/src/scored.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/petgraph-src/crates/petgraph/src/algo/dijkstra.rs`.
- Language / framework / stack: Rust, `BinaryHeap`, pathfinding priority queues, total ordering wrappers.
- Code shape / snippet:
```rust
pub struct MinScored<K, T>(pub K, pub T);

impl<K: PartialOrd, T> Ord for MinScored<K, T> {
    fn cmp(&self, other: &MinScored<K, T>) -> Ordering {
        let a = &self.0;
        let b = &other.0;
        if a < b { Ordering::Greater }
        else if a > b { Ordering::Less }
        else if a.ne(a) { Ordering::Less }
        else { Ordering::Equal }
    }
}

visit_next.push(MinScored(next_score, next));
```
- Why it matters: A max-heap becomes a min-heap, and partially ordered scores such as floats get deterministic `Ord` behavior including NaN handling.
- When to use: Use when a standard priority queue needs domain-specific ordering without rewriting heap logic.
- When not to use: Avoid when NaN or incomparable values should be rejected rather than pushed to the back of ordering.
- Transferable principle: Wrap priority keys with explicit ordering semantics at the type boundary.
- Related patterns: Trait-Templated Graph Traversal Surface; Bounded Fuzzy Automaton Query Weight.
- Risks / caveats: Defining total order over floats is a policy choice; it can mask invalid cost calculations in shortest-path code.
- Agentic coding guidance: When introducing a scored wrapper, add tests for equal scores, reversed ordering, and invalid/sentinel values such as NaN.

### Lexicographic Two-Phase Batch Mutation
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sled-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sled-src/src/tree.rs`.
- Language / framework / stack: Rust, sled key-value tree, `BTreeMap`, lock ordering, batch writes.
- Code shape / snippet:
```rust
pub fn apply_batch(&self, batch: Batch) -> io::Result<()> {
    let mut acquired_locks: BTreeMap<InlineArray, (...)> = BTreeMap::new();

    for key in batch.writes.keys() {
        if last.is_none() {
            last = Some(self.page_in(key, self.cache.current_flush_epoch())?);
        }
    }

    let flush_epoch_guard = self.cache.check_into_flush_epoch();
    for (key, value_opt) in batch.writes {
        /* mutate locked leaves, split, merge, then mark dirty */
    }
}
```
- Why it matters: Batch mutation acquires leaf locks in lexicographic order before entering a flush epoch, reducing deadlock risk and preventing "future dirty epoch" anomalies.
- When to use: Use for atomic multi-key updates over ordered storage where keys map to lockable ranges.
- When not to use: Avoid when batch keys cannot be globally ordered or when each mutation must stream independently without holding range locks.
- Transferable principle: Sort by the same key space used for locking, then separate lock acquisition, mutation, visibility, and dirty marking.
- Related patterns: Dirty-State Flush Epoch Pipeline; Mmap-Backed BigVector Windowing.
- Risks / caveats: Holding multiple leaf locks raises contention and memory pressure for large batches.
- Agentic coding guidance: When changing `apply_batch`, keep lexicographic acquisition and flush-epoch check-in order intact; add concurrency tests before altering lock scope.

### Dirty-State Flush Epoch Pipeline
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sled-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sled-src/src/object_cache.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/sled-src/src/tree.rs`.
- Language / framework / stack: Rust, persistent storage cache, flush epochs, write batches, fault-injection-aware durability.
- Code shape / snippet:
```rust
pub enum Dirty<const LEAF_FANOUT: usize> {
    NotYetSerialized { low_key: InlineArray, node: Object<LEAF_FANOUT>, collection_id: CollectionId },
    CooperativelySerialized { object_id: ObjectId, data: Arc<Vec<u8>>, mutation_count: u64, .. },
    MergedAndDeleted { object_id: ObjectId, collection_id: CollectionId },
}

let last_dirty_opt = self.dirty.insert((flush_epoch, object_id), dirty);
assert!(!last_dirty.is_final_state());
```
- Why it matters: Dirty leaves move through explicit states, and final states cannot be overwritten within an epoch, making flush responsibility auditable.
- When to use: Use in storage engines where in-memory mutation, cooperative serialization, deletion, and durable write batching must be coordinated.
- When not to use: Avoid in simple caches where eventual eviction is enough and persistence does not require epoch ordering.
- Transferable principle: Model persistence progress as explicit state transitions keyed by epoch and object id.
- Related patterns: Lexicographic Two-Phase Batch Mutation; Atomic Checkpoint Closures For Resumable Batch Runs.
- Risks / caveats: State-machine correctness depends on assertions and exhaustive match handling; a missing transition can panic under concurrency.
- Agentic coding guidance: When adding dirty states, update `is_final_state`, `install_dirty`, flush matching, event verifier transitions, and crash-recovery tests together.

### Named Tokenizer Pipeline Registry
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tantivy-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tantivy-src/src/tokenizer/tokenizer_manager.rs`.
- Language / framework / stack: Rust, Tantivy text analysis, `Arc<RwLock<HashMap<...>>>`, tokenizer pipelines.
- Code shape / snippet:
```rust
pub struct TokenizerManager {
    tokenizers: Arc<RwLock<HashMap<String, TextAnalyzer>>>,
}

pub fn register<T>(&self, tokenizer_name: &str, tokenizer: T)
where TextAnalyzer: From<T> {
    self.tokenizers.write().unwrap()
        .insert(tokenizer_name.to_string(), TextAnalyzer::from(tokenizer));
}

manager.register("default", TextAnalyzer::builder(SimpleTokenizer::default())
    .filter(RemoveLongFilter::limit(40))
    .filter(LowerCaser)
    .build());
```
- Why it matters: Text analysis is configured by stable names while each analyzer remains a composable pipeline of tokenizer and filters.
- When to use: Use when schema/config files should refer to analyzers by name but applications need to register custom pipelines.
- When not to use: Avoid when analysis must be immutable after startup or when per-request analyzer mutation would cause racey search behavior.
- Transferable principle: Separate named lookup from pipeline construction; store the pipeline behind shared read access.
- Related patterns: Classpath Plugin Lifecycle Fanout; Bounded Fuzzy Automaton Query Weight.
- Risks / caveats: Runtime registration can replace an existing name, so schema/index compatibility needs external discipline.
- Agentic coding guidance: When adding tokenizers, register them under explicit names and test both lookup success and missing-tokenizer behavior.

### Bounded Fuzzy Automaton Query Weight
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tantivy-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/tantivy-src/src/query/fuzzy_query.rs`.
- Language / framework / stack: Rust, Tantivy queries, Levenshtein automata, FST automaton weights, `OnceCell`.
- Code shape / snippet:
```rust
static AUTOMATON_BUILDER: [[OnceCell<LevenshteinAutomatonBuilder>; 2]; 3] = [
    [OnceCell::new(), OnceCell::new()],
    [OnceCell::new(), OnceCell::new()],
    [OnceCell::new(), OnceCell::new()],
];

let automaton_builder = AUTOMATON_BUILDER
    .get(self.distance as usize)
    .ok_or_else(|| InvalidArgument(format!("Levenshtein distance of {} is not allowed", self.distance)))?
    .get_or_init(|| LevenshteinAutomatonBuilder::new(self.distance, self.transposition_cost_one));
```
- Why it matters: Fuzzy matching is powerful but bounded: only supported distances get cached builders, and non-string terms fail before query execution.
- When to use: Use for search queries that need typo tolerance without unbounded automaton construction cost.
- When not to use: Avoid for arbitrary edit distances, non-text fields, or cases where approximate search should be replaced by analyzer normalization.
- Transferable principle: Cache expensive query machinery in a bounded table and reject inputs outside the supported envelope.
- Related patterns: Named Tokenizer Pipeline Registry; Total-Order Score Wrapper For BinaryHeap.
- Risks / caveats: Hard-coded distance bounds are a product decision; raising them can sharply increase memory and query expansion cost.
- Agentic coding guidance: When changing fuzzy behavior, test distance bounds, prefix mode, JSON string path handling, and invalid term types.

### Frontier-Gated Notification Session
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/timely-dataflow-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/timely-dataflow-src/timely/src/dataflow/operators/generic/notificator.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/timely-dataflow-src/timely/src/dataflow/operators/generic/operator.rs`.
- Language / framework / stack: Rust, Timely Dataflow, frontiers, capabilities, operator notifications.
- Code shape / snippet:
```rust
pub struct Notificator<'a, T: Timestamp> {
    frontiers: &'a [&'a MutableAntichain<T>],
    inner: &'a mut FrontierNotificator<T>,
}

pub fn notify_at(&mut self, cap: Capability<T>) {
    self.inner.notify_at_frontiered(cap, self.frontiers);
}

pub fn for_each<F>(&mut self, mut logic: F) {
    while let Some((cap, count)) = self.next() {
        logic(cap, count, self);
    }
}
```
- Why it matters: Operators can request future work with capabilities, but notifications are delivered only once input frontiers make that timestamp safe.
- When to use: Use in streaming/dataflow operators that buffer by timestamp and must release data when all earlier input is complete.
- When not to use: Avoid for stateless per-record operators or systems without a notion of logical time/frontier progress.
- Transferable principle: Treat delayed work as capability-owned requests gated by observed progress, not as ad hoc timers.
- Related patterns: Lazy Consolidating Change Batch; Memory-Budgeted Partition Edge Streaming.
- Risks / caveats: Holding capabilities retains progress obligations; forgotten or over-retained capabilities can stall downstream computation.
- Agentic coding guidance: When writing Timely operators, pair every stash keyed by timestamp with notificator tests that advance frontiers and prove release order.

### Lazy Consolidating Change Batch
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/timely-dataflow-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/timely-dataflow-src/timely/src/progress/change_batch.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/timely-dataflow-src/timely/src/dataflow/operators/core/probe.rs`.
- Language / framework / stack: Rust, Timely Dataflow progress tracking, `SmallVec`, antichain/frontier updates.
- Code shape / snippet:
```rust
pub struct ChangeBatch<T, const X: usize = 2> {
    updates: SmallVec<[(T, i64); X]>,
    clean: usize,
}

pub fn update(&mut self, item: T, value: i64) {
    self.updates.push((item, value));
    self.maintain_bounds();
}

pub fn compact(&mut self) {
    self.updates.sort_unstable_by(|x, y| x.0.cmp(&y.0));
    self.updates.retain(|x| x.1 != 0);
}
```
- Why it matters: Progress deltas are appended cheaply and consolidated only when a method needs a clean view or the dirty portion grows too large.
- When to use: Use for high-frequency signed updates where many increments/decrements cancel out before observers need the final state.
- When not to use: Avoid when every update must be externally visible immediately or when sorting keys is more expensive than direct map maintenance.
- Transferable principle: Accumulate cheaply, expose only operations that can pay compaction knowingly, and make mutability signal possible cleanup work.
- Related patterns: Frontier-Gated Notification Session; Dirty-State Flush Epoch Pipeline.
- Risks / caveats: Methods like `is_empty` require mutable access because they may compact; API users must understand that observation can mutate representation.
- Agentic coding guidance: When modifying progress structures, preserve lazy compaction invariants and add tests for cancellation, `drain_into`, and zero-retention behavior.

## Worker 3 Batch 7

### Typed Driver Operation Registry
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src/graphdb/src/main/java/com/ldbc/impls/workloads/ldbc/snb/graphdb/interactive/GraphDBInteractive.java`.
- Language / framework / stack: Java, LDBC SNB interactive driver, GraphDB, RDF4J, benchmark operation handlers.
- Code shape / snippet:
```java
protected void onInit(Map<String, String> properties, LoggingService loggingService) throws DbException {
    super.onInit(properties, loggingService);

    registerOperationHandler(LdbcQuery1.class, InteractiveQuery1.class);
    registerOperationHandler(LdbcShortQuery1PersonProfile.class, ShortQuery1PersonProfile.class);
    registerOperationHandler(LdbcUpdate1AddPerson.class, Update1AddPerson.class);
    registerOperationHandler(LdbcUpdate8AddFriendship.class, Update8AddFriendship.class);
}
```
- Why it matters: The database implementation exposes one explicit dispatch table from driver operation types to handler classes, making benchmark coverage auditable without scanning reflection or naming conventions.
- When to use: Use when a framework supplies typed operation classes and each operation needs a backend-specific handler.
- When not to use: Avoid when handlers are loaded dynamically from plugins or when operation registration must be data-driven at runtime.
- Transferable principle: Put cross-framework wiring in one registration boundary so unsupported operations are visible as missing registrations.
- Related patterns: Query Template Expansion With Converter Boundary; Stable Security Finding Identity.
- Risks / caveats: Manual tables drift when new operations are added; tests should assert every workload operation has a registered handler.
- Agentic coding guidance: When adding an operation, update the registry and its query-store method in the same patch, then run a handler inventory check rather than relying on compile success alone.

### Query Template Expansion With Converter Boundary
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src`; `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src/graphdb/src/main/java/com/ldbc/impls/workloads/ldbc/snb/graphdb/GraphDBQueryStore.java`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src/graphdb/src/main/java/com/ldbc/impls/workloads/ldbc/snb/graphdb/converter/GraphDBConverter.java`, `/Users/amuldotexe/Desktop/personal-repos-lane/knight-bus-graph-walker/gitrefrepo/ldbc_snb_interactive_v1_impls-src/graphdb/queries/interactive-update-1-add-person.rq`.
- Language / framework / stack: Java, SPARQL update templates, LDBC `QueryStore`, GraphDB/RDF4J converters.
- Code shape / snippet:
```java
list.add(prepare(
    QueryType.InteractiveUpdate1AddPerson,
    new ImmutableMap.Builder<String, Object>()
        .put(LdbcUpdate1AddPerson.PERSON_ID, getConverter().convertIdForInsertion(operation.getPersonId()))
        .put(LdbcUpdate1AddPerson.PERSON_FIRST_NAME, getConverter().convertString(operation.getPersonFirstName()))
        .put(SUBJECT_ID, getConverter().convertId(operation.getPersonId()))
        .build()
));
```
```sparql
INSERT DATA {
    sn:pers%subjectId% rdf:type snvoc:Person ;
    snvoc:id "%personId%"^^xsd:long ;
    snvoc:firstName "%personFirstName%" ;
};
```
- Why it matters: The query store keeps database syntax in `.rq` files while Java code owns parameter conversion and multi-statement assembly.
- When to use: Use when query text is large, benchmark-defined, or needs review by database specialists.
- When not to use: Avoid if parameters are user-controlled and the template engine does raw substitution without robust escaping.
- Transferable principle: Separate query text, domain operation extraction, and database-specific literal conversion into different layers.
- Related patterns: Typed Driver Operation Registry; Stable Security Finding Identity.
- Risks / caveats: String substitution can become injection-prone; converter behavior must match every placeholder's expected literal or IRI shape.
- Agentic coding guidance: When changing query placeholders, search both `.rq` templates and `GraphDBQueryStore` builders, then add a validation fixture that prepares the final query string.

### Deadlock-Safe Timed Child Process
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard/src/engine/process.rs`.
- Language / framework / stack: Rust, `std::process`, `wait_timeout`, threaded pipe draining.
- Code shape / snippet:
```rust
let stdout_pipe = child.stdout.take();
let stderr_pipe = child.stderr.take();

let stdout_thread = std::thread::spawn(move || {
    let mut buf = Vec::new();
    if let Some(mut pipe) = stdout_pipe {
        let _ = pipe.read_to_end(&mut buf);
    }
    buf
});

let status = child.wait_timeout(timeout)?;
match status {
    Some(exit_status) => Ok(TimedOutput::Finished(Output { status: exit_status, stdout, stderr })),
    None => {
        let _ = child.kill();
        let _ = child.wait();
        Ok(TimedOutput::TimedOut { stdout, stderr })
    }
}
```
- Why it matters: The helper avoids the classic deadlock where a parent waits for exit before draining full stdout/stderr pipes.
- When to use: Use for wrappers around scanners, compilers, formatters, and external security tools that can emit large output or hang.
- When not to use: Avoid for interactive subprocesses, long-lived daemons, or streams that must be processed incrementally.
- Transferable principle: Own the child process lifecycle and its output pipes as one API, including timeout outcome as data.
- Related patterns: Stable Security Finding Identity; Structural Edit Verification Gate.
- Risks / caveats: Threads buffer all output in memory, so hostile or very noisy tools still need output caps.
- Agentic coding guidance: When introducing external CLI calls, route them through the shared process wrapper and add tests for timeout, nonzero exit, and large stdout/stderr.

### Declarative Taint Matcher Algebra
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard/src/rules/taint_engine.rs`.
- Language / framework / stack: Rust, tree-sitter AST analysis, Semgrep-compatible taint specifications.
- Code shape / snippet:
```rust
#[derive(Debug, Clone)]
pub enum NodeMatcher {
    Attribute { root: String, field: String, description: String },
    Call { canonical: String, description: String },
    MethodNameRegex { regex: CompiledRegex, description: String },
    TypedAssignTarget { type_name: String, description: String },
    LiteralString { description: String, regex: Option<String> },
}

#[derive(Debug, Clone, Default)]
pub struct TaintSpec {
    pub sources: Vec<NodeMatcher>,
    pub sinks: Vec<NodeMatcher>,
    pub sanitizers: Vec<NodeMatcher>,
}
```
- Why it matters: Rule parsing compiles many language-specific AST shapes into a small algebra of source, sink, sanitizer, propagator, and label rules.
- When to use: Use when a static analyzer needs multiple frontend languages but one shared data-flow vocabulary.
- When not to use: Avoid when the domain needs full type inference or path-sensitive interprocedural analysis before basic matching is useful.
- Transferable principle: Model rule semantics as explicit variants, and document each variant's precision boundary at the type definition.
- Related patterns: Deadlock-Safe Timed Child Process; Stable Security Finding Identity.
- Risks / caveats: Carrying unsupported matcher variants through languages can look complete while silently no-oping; registry coverage tests are essential.
- Agentic coding guidance: Add new rule shapes by extending `NodeMatcher` plus at least one language engine and parity test; do not encode new semantics as raw strings.

### Stable Security Finding Identity
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard/src/baseline.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/0sec-labs__foxguard/src/report/sarif.rs`.
- Language / framework / stack: Rust, serde JSON baselines, SHA-256, SARIF 2.1.0.
- Code shape / snippet:
```rust
fn fingerprint_finding_with_file(finding: &Finding, file: &str) -> String {
    let mut hasher = Sha256::new();
    hasher.update(finding.rule_id.as_bytes());
    hasher.update([0]);
    hasher.update(file.as_bytes());
    hasher.update([0]);
    hasher.update(finding.line.to_string().as_bytes());
    hasher.update([0]);
    hasher.update(finding.description.as_bytes());
    hasher.finalize().iter().map(|b| format!("{:02x}", b)).collect()
}
```
- Why it matters: Baseline suppression and SARIF partial fingerprints depend on deterministic identities rather than mutable object IDs.
- When to use: Use for security scanners, linters, and review bots that need suppressions to survive process restarts and report format changes.
- When not to use: Avoid if line numbers churn heavily and snippets or AST anchors would be more stable.
- Transferable principle: Build finding identity from normalized domain facts and keep compatibility paths for older fingerprints.
- Related patterns: Declarative Taint Matcher Algebra; Batch Graph Normalization With Repair Stats.
- Risks / caveats: Too many fields make fingerprints fragile; too few fields over-suppress unrelated findings.
- Agentic coding guidance: When changing finding fields, update fingerprint tests and legacy deserialization tests in the same patch.

### Guarded Semantic Merge Fallback
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave/crates/weave-core/src/merge.rs`.
- Language / framework / stack: Rust, tree-sitter-backed semantic entities, git merge-file fallback, parser registry.
- Code shape / snippet:
```rust
if is_binary(base) || is_binary(ours) || is_binary(theirs) {
    let mut stats = MergeStats::default();
    stats.used_fallback = true;
    return git_merge_file(base, ours, theirs, &mut stats);
}

if base.len() > 1_000_000 || ours.len() > 1_000_000 || theirs.len() > 1_000_000 {
    return line_level_fallback(base, ours, theirs, file_path);
}

let plugin = match registry.get_plugin(file_path) {
    Some(p) if p.id() != "fallback" => p,
    _ => return line_level_fallback(base, ours, theirs, file_path),
};
```
- Why it matters: Semantic merge is attempted only inside a safe operating envelope; unsupported, binary, huge, duplicate-heavy, or suspicious output falls back to line merge.
- When to use: Use when adding a smarter algorithm on top of a trusted conservative algorithm.
- When not to use: Avoid if fallback output is not acceptable or if semantic parsing is the source of truth rather than an optimization.
- Transferable principle: Wrap ambitious analysis in cheap preconditions, postconditions, and fallback paths.
- Related patterns: Enhanced Conflict Markers With Hints; Version Vector Entity Claims.
- Risks / caveats: Fallbacks can mask parser quality problems if stats are not monitored.
- Agentic coding guidance: When adding semantic merge cases, include an adversarial test that forces fallback and one that proves clean semantic output keeps unchanged lines.

### Enhanced Conflict Markers With Hints
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave/crates/weave-core/src/conflict.rs`.
- Language / framework / stack: Rust, merge conflict rendering, conflict complexity taxonomy.
- Code shape / snippet:
```rust
let (prefix_len, suffix_len) = narrow_conflict_lines(&ours_lines, &theirs_lines);
let label = format!(
    "{} `{}` ({}, confidence: {})",
    self.entity_type, self.entity_name, self.complexity, confidence
);
out.push_str(&format!("{} ours \u{2014} {}\n", open, label));
out.push_str(&format!("// hint: {}\n", hint));
```
- Why it matters: Conflict markers carry entity type, name, complexity, confidence, and a human/agent hint while narrowing markers to only differing lines.
- When to use: Use when unresolved conflicts are expected to be consumed by humans and agents, not just by git.
- When not to use: Avoid enhanced markers when downstream tools require strict standard git marker syntax; this repo supports standard mode for that case.
- Transferable principle: Put structured metadata at the point of interruption, but keep a compatibility mode for existing tooling.
- Related patterns: Guarded Semantic Merge Fallback; Token-Budgeted Minimal Edit Context.
- Risks / caveats: Enhanced markers become part of user-visible code and can break parsers if not cleaned before commit.
- Agentic coding guidance: When generating conflicts, prefer parsable metadata and deterministic hints; add round-trip parse tests for every marker format.

### Version Vector Entity Claims
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave/crates/weave-crdt/src/merge.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave/crates/weave-crdt/src/ops.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Ataraxy-Labs__weave/crates/weave-crdt/src/state.rs`.
- Language / framework / stack: Rust, Automerge CRDT, multi-agent entity coordination.
- Code shape / snippet:
```rust
pub fn record_modification(
    state: &mut EntityStateDoc,
    agent_id: &str,
    entity_id: &str,
    content_hash: &str,
) -> Result<()> {
    let vv = read_version_vector(&state.doc, &entity_obj);
    let mut new_vv = vv;
    new_vv.increment(agent_id);
    write_version_vector(&mut state.doc, &entity_obj, &new_vv)?;
    state.doc.put(&entity_obj, "content_hash", content_hash)?;
    log_operation(state, agent_id, entity_id, "modify")?;
    Ok(())
}
```
- Why it matters: Claims are advisory locks, while version vectors record causal edit history so concurrent changes can be detected rather than overwritten.
- When to use: Use for collaborative agent systems where multiple workers may touch semantic entities in the same repository.
- When not to use: Avoid for single-writer local state or hard-lock workflows where a database transaction is simpler.
- Transferable principle: Separate human-friendly ownership intent from machine-checkable causal history.
- Related patterns: Guarded Semantic Merge Fallback; Stable Security Finding Identity.
- Risks / caveats: Advisory claims do not prevent edits; stale-agent cleanup and conflict detection must run regularly.
- Agentic coding guidance: When an agent edits an entity, update claim, heartbeat, content hash, and version vector together; do not infer safety from `claimed_by` alone.

### Token-Budgeted Minimal Edit Context
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp/src/analysis/minimal_edit_context.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp/src/common/budget.rs`.
- Language / framework / stack: Rust, MCP tools, tree-sitter, `tiktoken_rs`, compact JSON rows.
- Code shape / snippet:
```rust
out.insert("h".to_string(), json!(TARGET_HEADER));
out.insert("target".to_string(), json!(target_to_row(&target, target_code.as_str())));

let dep_rows = signatures_to_rows(&deps);
if !dep_rows.is_empty() {
    out.insert("dh".to_string(), json!(DEP_HEADER));
    out.insert("deps".to_string(), json!(dep_rows));
}

enforce_budget(&mut out, max_tokens)?;
```
- Why it matters: The tool returns the target symbol, called dependencies, relevant imports, and relevant types, then trims lower-priority fields until the serialized JSON fits the token budget.
- When to use: Use for agent tools that must hand back enough context for one precise edit without flooding the context window.
- When not to use: Avoid for global refactors where transitive blast radius matters more than local edit precision.
- Transferable principle: Order context by edit utility, serialize compactly, and enforce a hard budget before returning to the model.
- Related patterns: Structural Edit Verification Gate; Layered Ignore Filter.
- Risks / caveats: Dependency selection by called names can miss dynamic dispatch, macros, reflection, or framework conventions.
- Agentic coding guidance: Ask this tool for the symbol you intend to edit, then verify the result includes all imported types you plan to touch before writing code.

### Structural Edit Verification Gate
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp/src/analysis/verify_edit.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Christoph__treesitter-mcp/src/analysis/diff.rs`.
- Language / framework / stack: Rust, git diff analysis, tree-sitter structural changes, MCP result formatting.
- Code shape / snippet:
```rust
let analysis = diff::analyze_diff(file_path, compare_to.clone())?;
let changed_symbols = analysis
    .structural_changes
    .iter()
    .map(|change| change.name.clone())
    .collect::<Vec<_>>();

let unexpected = analysis
    .structural_changes
    .iter()
    .filter(|change| change.name != target_symbol)
    .map(|change| change.name.clone())
    .collect::<Vec<_>>();
```
- Why it matters: After an edit, the tool checks whether the intended symbol changed and whether unexpected symbols also changed.
- When to use: Use after agent-generated patches, codemods, and tight bug fixes.
- When not to use: Avoid as the only verifier for behavior; it checks structural scope, not runtime correctness.
- Transferable principle: Verify the blast radius of an edit with structural diff data before claiming the change stayed scoped.
- Related patterns: Token-Budgeted Minimal Edit Context; Deadlock-Safe Timed Child Process.
- Risks / caveats: Rename-heavy changes or parser failures can produce false alarms or miss textual changes outside symbols.
- Agentic coding guidance: Run structural verification with `target_symbol` for narrow fixes, then pair it with tests or build commands for behavioral proof.

### Rope-Backed Range Runs
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor/Sources/CodeEditSourceEditor/RangeStore/RangeStore.swift`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor/Sources/CodeEditSourceEditor/RangeStore/RangeStore+Coalesce.swift`.
- Language / framework / stack: Swift, `_RopeModule`, text editor ranges, syntax/style storage.
- Code shape / snippet:
```swift
mutating func set(runs: [Run], for range: Range<Int>) {
    _guts.replaceSubrange(
        range,
        in: OffsetMetric(),
        with: runs.map { StoredRun(length: $0.length, value: $0.value) }
    )

    coalesceNearby(range: range)
    cache = nil
}
```
```swift
if thisRun.compareValue(nextRun) {
    _guts.update(at: &index, by: { $0.length += nextRun.length })
    _guts.remove(at: nextIndex)
}
```
- Why it matters: Large text documents can update style or metadata ranges by replacing rope runs and coalescing adjacent equal runs.
- When to use: Use for editors, highlighters, diff viewers, or annotation stores that attach values to character ranges.
- When not to use: Avoid for small documents where a simple sorted interval array is easier and fast enough.
- Transferable principle: Store dense per-character metadata as run-length encoded ranges over a rope, not as one object per character.
- Related patterns: Incremental Layered Tree-Sitter Edits; Token-Budgeted Minimal Edit Context.
- Risks / caveats: Offset metrics and edit deltas must be correct; a bad range update corrupts downstream highlighting.
- Agentic coding guidance: When changing range storage, add tests for insertion, deletion, replacement, coalescing, and repeated identical range queries.

### Incremental Layered Tree-Sitter Edits
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor/Sources/CodeEditSourceEditor/TreeSitter/TreeSitterClient.swift`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/CodeEditApp__CodeEditSourceEditor/Sources/CodeEditSourceEditor/TreeSitter/TreeSitterClient+Edit.swift`.
- Language / framework / stack: Swift, SwiftTreeSitter, CodeEdit text editor, async executor, injected language layers.
- Code shape / snippet:
```swift
let pendingEdits = pendingEdits.value()
let edits = pendingEdits + [edit]

for (idx, layer) in state.layers.enumerated().reversed() {
    if layer.id != state.primaryLayer.id {
        applyEditTo(layer: layer, edits: edits)
        if layer.ranges.isEmpty {
            state.removeLanguageLayer(at: idx)
            continue
        }
    }
    layer.parser.includedRanges = layer.ranges.map { $0.tsRange }
    let ranges = layer.findChangedByteRanges(edits: edits, timeout: Constants.parserTimeout, readBlock: readBlock)
    invalidatedRanges.insert(ranges: ranges)
}
```
- Why it matters: Edits are applied to copied parser state across primary and injected language layers, producing invalidated byte ranges for highlighting.
- When to use: Use in editors that embed languages inside other languages, such as HTML with scripts or Markdown with code fences.
- When not to use: Avoid for batch parsers where reparsing the whole file is cheaper and simpler.
- Transferable principle: Queue edits, apply them to isolated parser state, and return only invalidated ranges to downstream consumers.
- Related patterns: Rope-Backed Range Runs; Structural Edit Verification Gate.
- Risks / caveats: Cancellation and pending edit queues must be correct or parser state can lag behind text state.
- Agentic coding guidance: When modifying parser edit flow, test long edits, cancellation, injected language removal, and invalidation range unioning.

### Batch Graph Normalization With Repair Stats
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything/understand-anything-plugin/packages/core/src/analyzer/normalize-graph.ts`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything/understand-anything-plugin/packages/core/src/analyzer/graph-builder.ts`.
- Language / framework / stack: TypeScript, knowledge graph normalization, analyzer batch output repair.
- Code shape / snippet:
```ts
const newId = normalizeNodeId(oldId, {
  type: nodeType,
  filePath: typeof raw.filePath === "string" ? raw.filePath : undefined,
  name: typeof raw.name === "string" ? raw.name : undefined,
  parentFlowSlug: nodeType === "step" ? stepToFlowSlug.get(oldId) : undefined,
});

if (!validNodeIds.has(newSource) || !validNodeIds.has(newTarget)) {
  stats.danglingEdgesDropped++;
  stats.droppedEdges.push({ source: newSource, target: newTarget, type: String(raw.type ?? ""), reason });
  continue;
}
```
- Why it matters: LLM or batch analyzer graph output is repaired before ingestion: IDs are canonicalized, complexity values normalized, edges rewritten, duplicate edges removed, and dangling edges reported.
- When to use: Use at the boundary between generative analysis and deterministic graph storage.
- When not to use: Avoid if repair would hide upstream contract violations that should fail hard.
- Transferable principle: Normalize, deduplicate, and count repairs at ingestion boundaries; expose stats so repair is visible.
- Related patterns: Stable Security Finding Identity; Layered Ignore Filter.
- Risks / caveats: Over-aggressive repair can merge distinct nodes, especially when IDs omit flow or file discriminators.
- Agentic coding guidance: When adding node types, update prefix maps, normalization tests, and edge rewrite cases together.

### Layered Ignore Filter
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything/understand-anything-plugin/packages/core/src/ignore-filter.ts`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Egonex-AI__Understand-Anything/understand-anything-plugin/packages/core/src/languages/language-registry.ts`.
- Language / framework / stack: TypeScript, Node.js filesystem APIs, `ignore` package, language registry.
- Code shape / snippet:
```ts
const ig: Ignore = ignore();
ig.add(DEFAULT_IGNORE_PATTERNS);

const projectIgnorePath = join(projectRoot, ".understand-anything", ".understandignore");
if (existsSync(projectIgnorePath)) {
  ig.add(readFileSync(projectIgnorePath, "utf-8"));
}

const rootIgnorePath = join(projectRoot, ".understandignore");
if (existsSync(rootIgnorePath)) {
  ig.add(readFileSync(rootIgnorePath, "utf-8"));
}
```
- Why it matters: The analyzer starts with conservative defaults, then lets project-specific ignore files override or extend them.
- When to use: Use for codebase scanners that need safe defaults but must respect local project intent.
- When not to use: Avoid for compliance scans where ignored binaries, lockfiles, and vendored code are in scope.
- Transferable principle: Layer default policy, tool-local policy, and project-root policy in a documented order.
- Related patterns: Batch Graph Normalization With Repair Stats; Token-Budgeted Minimal Edit Context.
- Risks / caveats: Default lockfile exclusion may hide dependency evidence; negation behavior depends on rule ordering.
- Agentic coding guidance: Before scanning a repo, surface the active ignore sources and allow explicit include overrides for audit tasks.

### Static Slide Deck As Knowledge Artifact
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrendanJamesLynskey__CodingAgents_01_Repo_Understanding`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrendanJamesLynskey__CodingAgents_01_Repo_Understanding/index.html`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/BrendanJamesLynskey__CodingAgents_01_Repo_Understanding/README.md`.
- Language / framework / stack: Single-file HTML/CSS/JavaScript, static educational site, intersection observer.
- Code shape / snippet:
```html
<section class="slide" id="slide-02">
    <div class="slide-number">02</div>
    <h2>ripgrep Heuristics That Beat Embeddings</h2>
    <div class="code-block">
        <div class="code-header">ripgrep - key flags an agent runtime actually sets</div>
        <pre><code>rg 'connection_pool_acquire' --type rust --word-regexp --context 4 --json</code></pre>
    </div>
</section>
```
```js
document.querySelectorAll('.slide').forEach(slide => {
    slide.style.opacity = '0';
    slide.style.transform = 'translateY(30px)';
    observer.observe(slide);
});
```
- Why it matters: A repo-understanding playbook is packaged as a static artifact with semantic slide anchors, responsive CSS, embedded code examples, and tiny progressive enhancement.
- When to use: Use for durable agent guidance, onboarding decks, and architecture explanations that should work without a build step.
- When not to use: Avoid for data-heavy dashboards or content that needs runtime search, editing, or personalization.
- Transferable principle: For long-lived technical knowledge, prefer a portable artifact with stable anchors and source-visible examples.
- Related patterns: Token-Budgeted Minimal Edit Context; Layered Ignore Filter.
- Risks / caveats: Hard-coded benchmark claims and tool versions can go stale; static decks need periodic review.
- Agentic coding guidance: When creating agent-facing docs, include concrete command snippets, failure cases, and linkable section IDs rather than prose-only advice.

### VS Code Disposable Command Lifecycle
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JavierPrior845__clean-ast-linter`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/JavierPrior845__clean-ast-linter/src/extension.ts`.
- Language / framework / stack: TypeScript, VS Code extension API.
- Code shape / snippet:
```ts
export function activate(context: vscode.ExtensionContext) {
    const disposable = vscode.commands.registerCommand('clean-ast-linter.helloWorld', () => {
        vscode.window.showInformationMessage('Clean AST Linter is now active!');
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
```
- Why it matters: Even the minimal extension follows the VS Code lifecycle: register a command on activation and hand the disposable to the extension context for cleanup.
- When to use: Use as the smallest safe skeleton for editor extensions before adding diagnostics, language services, or tree-sitter parsing.
- When not to use: Avoid stopping here for a real linter; activation alone does not analyze documents or report diagnostics.
- Transferable principle: Framework resources should be registered through the host lifecycle and disposed by the host context.
- Related patterns: Structural Edit Verification Gate; Incremental Layered Tree-Sitter Edits.
- Risks / caveats: A command-only extension can give a false sense of implementation completeness; tests and diagnostics are still absent.
- Agentic coding guidance: When expanding this extension, keep activation thin and move parser loading, subscriptions, diagnostics, and command handlers into separately testable modules.

## Worker 3 Batch 8

### Case-Variant Keyword Nodes
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Akzestia__tree-sitter-cql`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Akzestia__tree-sitter-cql/grammar.js`.
- Language / framework / stack: JavaScript tree-sitter grammar for Cassandra CQL.
- Code shape / snippet:
```js
kw_use: ($) => choice("USE", "use"),
kw_alter: ($) => token(choice("ALTER", "alter")),
kw_create: ($) => choice("CREATE", "create"),

cql_types_constructor_map: ($) =>
  seq($.type_map, "<", $.cql_types, ",", $.cql_types, ">"),
cql_types_union: ($) =>
  choice(
    $.cql_types,
    $.cql_types_constructor_list,
    $.cql_types_constructor_tuple,
    $.cql_types_constructor_map,
    $.cql_types_constructor_frozen,
  ),
```
- Why this matters: The grammar models SQL-like case-insensitive keywords as named rules instead of scattering raw strings through statement rules, and it gives compound collection types their own constructor nodes.
- When to use: Use for dialect grammars where upper/lowercase spelling is part of syntax tolerance and downstream tools benefit from named keyword/type nodes.
- When not to use: Avoid when the parser generator or lexer already supports case-insensitive tokens centrally; duplicating every keyword can become noisy.
- Transferable principle: Normalize lexical variability at the grammar boundary, then build higher-level constructs from stable named tokens.
- Related patterns: Grammar Modules Composed By Domain Slice; Precedence-Mapped Operator Families.
- Risks / caveats: Hand-written keyword lists can drift, duplicate entries, or miss mixed-case variants unless generated or tested against a corpus.
- Agentic coding guidance: When extending dialect keywords, add the keyword node first, then wire it into the statement/type rule and add a corpus example for both common spellings.

### Field-Labeled Markup Grammar
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-xml`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/AndroidIDEOfficial__tree-sitter-xml/grammar.js`.
- Language / framework / stack: JavaScript tree-sitter grammar for XML.
- Code shape / snippet:
```js
empty_element: $ => seq(
    '<',
    field("tag_name", $.name),
    repeat(seq($._ws, $.attribute)),
    optional($._ws),
    '/',
    '>'
),

xml_attr: $ => seq(
    optional(seq(field("ns_prefix", $.name), ':')),
    field("attr_name", $.name),
    $.eq,
    $.attr_value,
),
```
- Why this matters: XML tag names, namespace prefixes, attribute names, and values are field-labeled at parse time, making editor queries and semantic tooling simpler than position-based child walking.
- When to use: Use for markup, config, and protocol grammars where downstream consumers need stable access to named parts of a record-like syntax.
- When not to use: Avoid over-labeling tokens that no consumer reads; excessive fields can make grammar maintenance feel heavier without adding semantic value.
- Transferable principle: Parse trees become better APIs when repeated structural roles are named at the producer boundary.
- Related patterns: Record Format Grammar With Negative Precedence; Lazy Native Binding Query Loader.
- Risks / caveats: This grammar does not validate matching start/end tag names, so structural labels improve extraction but not full XML correctness.
- Agentic coding guidance: When adding markup rules, prefer `field(...)` for semantic roles and leave validation that requires cross-node comparison to a later analysis pass.

### Grammar Modules Composed By Domain Slice
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql/grammar.js`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql/grammar/statements/index.js`.
- Language / framework / stack: JavaScript tree-sitter grammar, modular SQL dialect parser.
- Code shape / snippet:
```js
import keyword_rules from "./grammar/keywords.js";
import type_rules from "./grammar/types.js";
import expression_rules from "./grammar/expressions.js";
import statement_rules from "./grammar/statements/index.js";

rules: {
  program: $ => seq(repeat(seq(choice($.transaction, $.statement, $.block), ';'))),
  ...keyword_rules,
  ...type_rules,
  ...expression_rules,
  ...statement_rules,
}
```
- Why this matters: A large SQL grammar stays navigable by separating keywords, types, expressions, transactions, and statement families, then composing them at the grammar root.
- When to use: Use for broad DSLs or language parsers where rule groups have clear domain ownership and can be tested or reviewed in slices.
- When not to use: Avoid for tiny grammars where indirection makes every rule harder to trace.
- Transferable principle: Compose large declarative specifications from domain-sized modules while keeping a single top-level integration point.
- Related patterns: Case-Variant Keyword Nodes; Precedence-Mapped Operator Families.
- Risks / caveats: Spread-based composition can hide duplicate rule names and import order dependencies unless naming is disciplined.
- Agentic coding guidance: When adding a SQL feature, place the rule in the smallest matching slice, export through that slice index, and only touch the root grammar when a new domain slice is truly needed.

### Precedence-Mapped Operator Families
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql/grammar.js`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql/grammar/expressions.js`.
- Language / framework / stack: JavaScript tree-sitter grammar, SQL expression parser.
- Code shape / snippet:
```js
precedences: $ => [[
  'binary_is',
  'unary_not',
  'binary_exp',
  'binary_times',
  'binary_plus',
  'binary_relation',
  'between',
  'clause_connective',
]],

binary_expression: $ => choice(
  ...[
    ['+', 'binary_plus'],
    ['*', 'binary_times'],
    [$.keyword_is, 'binary_is'],
    [$.keyword_like, 'pattern_matching'],
  ].map(([operator, precedence]) =>
    prec.left(precedence, seq(field('left', $._expression), field('operator', operator), field('right', $._expression)))
  ),
),
```
- Why this matters: Operators are represented as data pairs that map token families to named precedence slots, so adding a new operator is a table edit rather than a new bespoke rule.
- When to use: Use for expression-heavy languages where many operators share the same parse shape but differ in precedence or operand restrictions.
- When not to use: Avoid when each operator has genuinely different AST shape or semantic constraints that a table would obscure.
- Transferable principle: Convert repetitive grammar alternatives into data-driven rule generation when the parse shape is uniform.
- Related patterns: Grammar Modules Composed By Domain Slice; Case-Variant Keyword Nodes.
- Risks / caveats: Data-driven grammar code can become opaque if the precedence names are not documented and corpus tests do not cover ambiguous combinations.
- Agentic coding guidance: When adding operators, identify the precedence family first, add a focused ambiguity corpus case, and resist copying a standalone rule unless the operator changes the child shape.

### Matched-Delimiter External Scanner State
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/DerekStride__tree-sitter-sql/src/scanner.c`.
- Language / framework / stack: C tree-sitter external scanner for SQL dollar-quoted strings.
- Code shape / snippet:
```c
typedef struct LexerState {
  char* start_tag;
} LexerState;

if (valid_symbols[DOLLAR_QUOTED_STRING_START_TAG] && state->start_tag == NULL) {
  char* start_tag = scan_dollar_string_tag(lexer);
  state->start_tag = start_tag;
  lexer->result_symbol = DOLLAR_QUOTED_STRING_START_TAG;
  return true;
}

if (valid_symbols[DOLLAR_QUOTED_STRING_END_TAG] && state->start_tag != NULL) {
  char* end_tag = scan_dollar_string_tag(lexer);
  if (end_tag != NULL && strcmp(end_tag, state->start_tag) == 0) {
    free(state->start_tag);
    state->start_tag = NULL;
    lexer->result_symbol = DOLLAR_QUOTED_STRING_END_TAG;
    return true;
  }
}
```
- Why this matters: The scanner stores the opening dollar tag and only emits an end token when a later tag matches, which is not expressible as a simple regular token.
- When to use: Use when lexical validity depends on a runtime delimiter, heredoc marker, indentation level, or other state discovered earlier in the stream.
- When not to use: Avoid for fixed delimiters or simple escape sequences that the grammar or lexer can express declaratively.
- Transferable principle: Promote dynamic lexical context into a small serialized scanner state instead of forcing context-sensitive syntax into grammar recursion.
- Related patterns: Indentation Stack Scanner With Comment Gating; Precedence-Mapped Operator Families.
- Risks / caveats: Manual allocation and serialization need careful ownership, especially on failed scans and partial parse recovery.
- Agentic coding guidance: When writing external scanners, keep state minimal, free replaced state on every path, and include serialization/deserialization tests for incremental parsing.

### Indentation Stack Scanner With Comment Gating
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aaron-212__tree-sitter-mojo`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aaron-212__tree-sitter-mojo/grammar.js`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aaron-212__tree-sitter-mojo/src/scanner.c`.
- Language / framework / stack: JavaScript tree-sitter grammar plus C external scanner for Mojo.
- Code shape / snippet:
```js
externals: ($) => [
  $._newline,
  $._indent,
  $._dedent,
  $.string_start,
  $._string_content,
  $.comment,
  "]",
  ")",
  "}",
],
```
```c
if (valid_symbols[INDENT] && indent_length > current_indent_length) {
    array_push(&scanner->indents, indent_length);
    lexer->result_symbol = INDENT;
    return true;
}

if ((valid_symbols[DEDENT] || (!valid_symbols[NEWLINE] && !within_brackets)) &&
    indent_length < current_indent_length &&
    first_comment_indent_length < (int32_t)current_indent_length) {
    array_pop(&scanner->indents);
    lexer->result_symbol = DEDENT;
    return true;
}
```
- Why this matters: The scanner turns whitespace into block tokens while avoiding dedents inside brackets and delaying dedents until same-block comments are consumed.
- When to use: Use for indentation-sensitive languages where layout, comments, and bracketed expressions interact.
- When not to use: Avoid for brace-delimited languages or DSLs where indentation is stylistic only.
- Transferable principle: Treat layout as parse state, not as trivia, when indentation changes program structure.
- Related patterns: Matched-Delimiter External Scanner State; Field-Labeled Markup Grammar.
- Risks / caveats: Scanner logic can affect error recovery globally; comments are marked external here specifically so the scanner keeps enough structure during recovery.
- Agentic coding guidance: When changing indentation scanners, test blank lines, comment-only lines, bracketed continuations, EOF dedents, and serialization of the indent stack.

### Record Format Grammar With Negative Precedence
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Crysthamus__tree-sitter-sln`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Crysthamus__tree-sitter-sln/grammar.js`.
- Language / framework / stack: JavaScript tree-sitter grammar for Visual Studio `.sln` files.
- Code shape / snippet:
```js
project_block: ($) =>
  seq(
    "Project", "(", field("guid", $.guid), ")", "=",
    field("name", $.string), ",",
    field("path", $.string), ",",
    field("guid", $.guid),
    repeat($.project_section),
    "EndProject",
  ),

key: ($) =>
  choice(
    $.guid_key,
    $.identifier,
    prec(-1, $.config_key),
    prec(-2, $.guid),
    prec(-3, $.string),
  ),
```
- Why this matters: The grammar models a line-oriented project file as structured records with named fields and uses negative precedence to prefer more specific key forms before generic string/guid fallbacks.
- When to use: Use for legacy config formats where several token shapes overlap but consumers need typed access to project IDs, names, paths, and sections.
- When not to use: Avoid when the input is free-form text or when a simpler line parser is enough and no incremental parse tree is needed.
- Transferable principle: Put the most semantic record alternatives first and demote broad fallback tokens so parse trees preserve intent.
- Related patterns: Field-Labeled Markup Grammar; Lazy Native Binding Query Loader.
- Risks / caveats: Negative precedence choices can mask ambiguous syntax until corpus examples cover each fallback branch.
- Agentic coding guidance: When adding record forms, first identify the most specific shape, then add a lower-precedence fallback only after a corpus case proves it is necessary.

### Bucketed Compatibility Rule Engine
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian/src/classifier/engine.ts`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian/src/classifier/types.ts`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian/src/classifier/rules/index.ts`.
- Language / framework / stack: TypeScript, tree-sitter-derived API diff classifier.
- Code shape / snippet:
```ts
const activeRules = allRules.filter(r => r.languages === 'all' || r.languages.includes(language));

const ruleBuckets = {
  function: activeRules.filter((r): r is FunctionRule => r.target === 'function'),
  interface: activeRules.filter((r): r is InterfaceRule => r.target === 'interface'),
  enum: activeRules.filter((r): r is EnumRule => r.target === 'enum'),
  type_alias: activeRules.filter((r): r is TypeAliasRule => r.target === 'type_alias'),
};

if (key.startsWith('interface:')) {
  rulesToRun = buckets.interface;
} else if (key.startsWith('enum:')) {
  rulesToRun = buckets.enum;
} else if (key.startsWith('type:')) {
  rulesToRun = buckets.type_alias;
} else {
  rulesToRun = buckets.function;
}
```
- Why this matters: Rules are filtered by language and bucketed by symbol target once per file, avoiding repeated dynamic checks and unsafe casts during classification.
- When to use: Use when a rule engine has many independent detectors that apply to different entity kinds or languages.
- When not to use: Avoid when the rule count is tiny and direct conditionals are clearer.
- Transferable principle: Precompute dispatch buckets around stable dimensions so each entity only sees the rules that can apply.
- Related patterns: Typed Signature Translator With Query Cache; Linter Rule Lifecycle With Finalize Hook.
- Risks / caveats: Prefix-based key routing is fast but must stay aligned with the translator's key format.
- Agentic coding guidance: When adding a new symbol kind, update the signature type, translator key prefix, rule target union, bucket map, and at least one rule fixture together.

### Typed Signature Translator With Query Cache
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian/src/parsers/ast-mapper.ts`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Aryan0628__diff-guardian/src/parsers/translators/typescript.ts`.
- Language / framework / stack: TypeScript, `web-tree-sitter`, polyglot signature extraction.
- Code shape / snippet:
```ts
const allFnMatches = [
  ...q.fn.matches(tree.rootNode),
  ...q.arrow.matches(tree.rootNode),
  ...q.ctor.matches(tree.rootNode),
];

for (const match of allFnMatches) {
  const sig = buildFunctionSignature(match, overloadCounts);
  if (!sig) continue;
  result.set(sig.name, sig);
}

for (const [key, sig] of rawMap.entries()) {
  if (!key.includes(':')) {
    (sig as FunctionSignature).filePath = filePath;
  }
}
```
- Why this matters: The translator stays pure over a tree-sitter tree, compiles reusable queries per language, tracks overload counts, and leaves file-path injection to the mapper boundary.
- When to use: Use when turning language-specific ASTs into a common semantic model consumed by a separate analysis engine.
- When not to use: Avoid if the translator needs I/O, logging, or global state; those side effects belong at orchestration boundaries.
- Transferable principle: Keep AST translators deterministic and side-effect-free, then enrich their outputs at a higher layer with file or repository context.
- Related patterns: Bucketed Compatibility Rule Engine; Language Trait For Semantic Extraction.
- Risks / caveats: Query captures and key formats are a contract; changing either can silently break downstream rule routing.
- Agentic coding guidance: When expanding a translator, add a query, a builder function, and a classifier fixture that proves the emitted key reaches the expected rule bucket.

### Protected-Region Formatter Pipeline
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter/src/formatter.rs`.
- Language / framework / stack: Rust, Topiary, tree-sitter GDScript formatter.
- Code shape / snippet:
```rust
formatter
    .preprocess()
    .format()?
    .postprocess()
    .validate_formatting()?
    .reorder()?;

fn extract_disabled_regions(&mut self) {
    // stores literal "# fmt: off" regions and replaces them with placeholders
    result.push_str(&format!("# fmt:preserved-region:{}\n", region_index));
}

fn restore_disabled_regions(&mut self) -> &mut Self {
    if let Some(original) = self.disabled_regions.get(index) {
        result.push_str(original);
        continue;
    }
    self.content = result;
    self.tree = self.parser.parse(&self.content, Some(&self.tree)).unwrap();
    self
}
```
- Why this matters: The formatter preserves explicitly disabled regions byte-for-byte by replacing them before formatting and restoring them after all normal cleanup.
- When to use: Use for formatters, codemods, and generators that must allow hand-maintained sections to opt out safely.
- When not to use: Avoid when the transformation is semantic and must inspect every line, including disabled regions, to remain correct.
- Transferable principle: Fence user-owned text with reversible placeholders before destructive or opinionated formatting passes.
- Related patterns: Semantic Reorder With Multiset Safety Signature; Linter Rule Lifecycle With Finalize Hook.
- Risks / caveats: Placeholder comments must be unlikely to collide with real source and must be restored after every post-processing path.
- Agentic coding guidance: When adding a formatter pass, verify whether it should run before or after protected-region restoration and reparse the tree whenever `content` changes.

### Semantic Reorder With Multiset Safety Signature
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter/src/reorder.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter/src/formatter.rs`.
- Language / framework / stack: Rust, tree-sitter GDScript source rewriter.
- Code shape / snippet:
```rust
tokens.sort_by(|a, b| {
    let priority_cmp = a.token_kind.get_priority().cmp(&b.token_kind.get_priority());
    if priority_cmp != std::cmp::Ordering::Equal {
        return priority_cmp;
    }
    let privacy_cmp = a.token_kind.is_private().cmp(&b.token_kind.is_private());
    if privacy_cmp != std::cmp::Ordering::Equal {
        return privacy_cmp;
    }
    std::cmp::Ordering::Equal
});

let mut diff = std::collections::HashMap::<TopLevelTokenSignature, i32>::new();
for signature in parse_top_level_token_signatures(original_source)? {
    *diff.entry(signature).or_insert(0) += 1;
}
for signature in top_level_token_signatures_from_tree(current_tree, current_source)? {
    *diff.entry(signature).or_insert(0) -= 1;
}
```
- Why this matters: Reordering is not just a sort. It carries comments with declarations, preserves unknown nodes, and verifies that top-level declaration signatures are neither lost nor duplicated.
- When to use: Use for style-guide reorderers and codemods that move declarations but should not alter program structure.
- When not to use: Avoid when dependencies between declarations make order semantically significant and no analyzer verifies those dependencies.
- Transferable principle: Pair structural rewrites with a cheap multiset invariant that proves the important entities survived.
- Related patterns: Protected-Region Formatter Pipeline; Structural Edit Verification Gate.
- Risks / caveats: Signature equality can miss semantic dependencies and may need expansion when new syntax appears.
- Agentic coding guidance: When adding a new reorderable element, update classification, priority, rebuilding, and safe-mode signature keys in the same patch.

### Linter Rule Lifecycle With Finalize Hook
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter/src/linter.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter/src/linter/rules.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/GDQuest__GDScript-formatter/src/linter/rules/duplicated_load.rs`.
- Language / framework / stack: Rust, tree-sitter GDScript linter.
- Code shape / snippet:
```rust
pub trait Rule {
    fn get_target_ast_nodes(&self) -> &[&str] { &[] }
    fn check_source(&mut self, _source_code: &str) -> Vec<LintIssue> { Vec::new() }
    fn check_node(&mut self, _node: &Node, _source_code: &str) -> Vec<LintIssue> { Vec::new() }
    fn finalize(&mut self, _source_code: &str) -> Vec<LintIssue> { Vec::new() }
}

let mut node_kind_map: HashMap<String, Vec<usize>> = HashMap::new();
for (current_index, checker) in checkers.iter().enumerate() {
    for &kind in checker.get_target_ast_nodes() {
        node_kind_map.entry(kind.to_string()).or_default().push(current_index);
    }
}
```
- Why this matters: Rules can run on raw source, selected AST nodes, or accumulated state after traversal, and the linter walks the tree once while dispatching only relevant node rules.
- When to use: Use for AST linters where some diagnostics need global accumulation and others are local node checks.
- When not to use: Avoid when rules need complex control-flow or type information; a tree walk alone may not be enough.
- Transferable principle: Give analysis rules a lifecycle that matches their data needs, then centralize traversal and ignore filtering.
- Related patterns: Bucketed Compatibility Rule Engine; Protected-Region Formatter Pipeline.
- Risks / caveats: Stateful rules must clear accumulated data in `finalize` or they can leak findings across files.
- Agentic coding guidance: When adding a linter rule, declare target node kinds narrowly, put cross-node reports in `finalize`, and add ignore-directive tests for the rule name.

### Context-Enriched Retrieval Blocks
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/indexer/contextual.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/indexer/batch_processor.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/indexer/search.rs`.
- Language / framework / stack: Rust, tree-sitter indexing, embeddings, BM25/FTS, LanceDB.
- Code shape / snippet:
```rust
pub fn build_structural_context(block: &CodeBlock) -> String {
    let mut parts = Vec::with_capacity(4);
    parts.push(format!("# File: {}", block.path));
    parts.push(format!("# Language: {}", block.language));
    if !block.symbols.is_empty() {
        parts.push(format!("# Defines: {}", block.symbols.join(", ")));
    }
    parts.join("\n")
}

let enriched_blocks: Vec<CodeBlock> = blocks
    .iter()
    .zip(contents.iter())
    .map(|(b, enriched)| {
        let mut nb = b.clone();
        nb.content = enriched.clone();
        nb
    })
    .collect();
```
- Why this matters: The same enriched text used for embeddings is stored in the search column so dense retrieval, BM25, and reranking all see file path, language, and symbol context.
- When to use: Use for code search where raw chunks are too local and queries often mention filenames, types, or responsibilities not present in the snippet.
- When not to use: Avoid when exact raw text fidelity in the indexed content is mandatory and no display-time stripping exists.
- Transferable principle: Retrieval quality improves when indexing content includes cheap structural context, but rendering should strip that context back out for humans.
- Related patterns: Weighted Hybrid RRF Reranker; Hash Differential Indexing With Obsolete Removal.
- Risks / caveats: Enrichment can pollute snippets or line numbers unless display code removes the preamble.
- Agentic coding guidance: When enriching index rows, add a paired `strip_*_preamble` renderer and confirm both vector and keyword paths use the same stored representation.

### Weighted Hybrid RRF Reranker
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/store/weighted_rrf.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/config.rs`.
- Language / framework / stack: Rust, LanceDB reranker, Arrow record batches.
- Code shape / snippet:
```rust
pub struct WeightedRRFReranker {
    k: f32,
    vector_weight: f32,
    keyword_weight: f32,
}

for (i, id) in vec_ids.values().iter().enumerate() {
    let score = self.vector_weight / (i as f32 + self.k);
    rrf_scores.entry(*id).and_modify(|e| *e += score).or_insert(score);
}

for (i, id) in fts_ids.values().iter().enumerate() {
    let score = self.keyword_weight / (i as f32 + self.k);
    rrf_scores.entry(*id).and_modify(|e| *e += score).or_insert(score);
}
```
- Why this matters: Hybrid search can tune semantic vector matches separately from keyword/BM25 matches while still using rank fusion and row-id deduplication.
- When to use: Use when different query classes need different balance between lexical identifier matches and semantic paraphrase matches.
- When not to use: Avoid if you have calibrated comparable scores from both retrieval systems; RRF intentionally ignores raw score magnitudes.
- Transferable principle: Fuse rankings through stable IDs and configurable source weights when individual retrieval scores are not directly comparable.
- Related patterns: Context-Enriched Retrieval Blocks; Generic Block Trait For Storage Operations.
- Risks / caveats: Bad weights can bury exact matches or overfit to one benchmark; expose weights as config and run evaluation sweeps.
- Agentic coding guidance: When changing hybrid retrieval, preserve dedup by row id, add tests for vector-only/keyword-only overlap, and report final `_relevance_score` for observability.

### Hash Differential Indexing With Obsolete Removal
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/indexer/differential_processor.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/store/table_ops.rs`.
- Language / framework / stack: Rust, incremental indexer, tree-sitter, LanceDB.
- Code shape / snippet:
```rust
let existing_hashes = if force_reindex {
    Vec::new()
} else {
    ctx.store.get_file_blocks_metadata(file_path, "code_blocks").await?
};

let mut new_hashes = HashSet::new();
for region in code_regions {
    let content_hash = calculate_content_hash_with_lines(
        &region.content,
        file_path,
        region.start_line,
        region.end_line,
    );
    new_hashes.insert(content_hash.clone());
    let exists = !force_reindex && ctx.store.content_exists(&content_hash, "code_blocks").await?;
    if !exists {
        code_blocks_batch.push(code_block.clone());
    }
}

let hashes_to_remove: Vec<String> = existing_hashes
    .into_iter()
    .filter(|hash| !new_hashes.contains(hash))
    .collect();
```
- Why this matters: The indexer only embeds changed regions and removes rows for regions that no longer exist, keeping a persistent search index consistent without full rebuilds.
- When to use: Use for repository indexes, document stores, and caches where content changes incrementally and embedding is expensive.
- When not to use: Avoid if the hashing inputs are unstable, such as generated line ranges that shift too often and cause needless re-embedding.
- Transferable principle: Maintain per-file old/new content hash sets so incremental updates can add missing rows and delete stale rows deterministically.
- Related patterns: Context-Enriched Retrieval Blocks; Atomic Metadata Batch After Block Persistence.
- Risks / caveats: Including line ranges in hashes improves uniqueness but can trigger reindexing after pure movement; choose hash dimensions based on desired invalidation semantics.
- Agentic coding guidance: When modifying chunking, update hash construction and stale-removal tests together, because both define cache identity.

### Language Trait For Semantic Extraction
- Where found: `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode`; `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/indexer/languages/mod.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/indexer/languages/rust.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/Muvon__octocode/src/indexer/code_region_extractor.rs`.
- Language / framework / stack: Rust, polyglot tree-sitter indexer.
- Code shape / snippet:
```rust
pub trait Language: Send + Sync {
    fn name(&self) -> &'static str;
    fn get_ts_language(&self) -> tree_sitter::Language;
    fn get_meaningful_kinds(&self) -> Vec<&'static str>;
    fn extract_symbols(&self, node: Node, contents: &str) -> Vec<String>;
    fn extract_imports_exports(&self, node: Node, contents: &str) -> (Vec<String>, Vec<String>) {
        let _ = (node, contents);
        (Vec::new(), Vec::new())
    }
    fn resolve_import(&self, import_path: &str, source_file: &str, all_files: &[String]) -> Option<String>;
}

pub fn get_language(name: &str) -> Option<Box<dyn Language>> {
    match name {
        "rust" => Some(Box::new(Rust {})),
        "typescript" => Some(Box::new(TypeScript {})),
        "python" => Some(Box::new(Python {})),
        _ => None,
    }
}
```
- Why this matters: Each language owns its tree-sitter grammar, meaningful node kinds, symbol extraction, import/export extraction, and import resolution behind a common trait.
- When to use: Use for polyglot indexing, static analysis, or code intelligence systems where language-specific details must plug into a shared pipeline.
- When not to use: Avoid a single broad trait if most methods are unsupported for most languages; split capabilities when defaults become misleading.
- Transferable principle: Put language-specific AST knowledge behind a trait and keep the indexer pipeline generic over that capability surface.
- Related patterns: Typed Signature Translator With Query Cache; Hash Differential Indexing With Obsolete Removal.
- Risks / caveats: Default empty implementations can silently omit graph edges for languages that have not implemented richer extraction.
- Agentic coding guidance: When adding a language, implement meaningful kinds, symbols, import resolution, and at least one fixture for each non-default method you rely on.
