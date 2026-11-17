---
name: rust-infra-parsers
description: Self-contained guide for Rust that reads and transforms source or structured text - parsers, lexers, linters, rule engines, code indexers and analysers (tree-sitter, `syn`, `nom`, `winnow`), compilers and lowering passes, diagnostics with spans, text edits and refactoring tools, registries of rules or back ends. Use when the task parses untrusted or user-written input, walks syntax trees, reports positions, rewrites text, or builds a pipeline of analysis passes. Not for the binary around the tool, or for on-disk formats and network protocols.
---

# Rust for parsers, analysers and source tools

This is the Rust of tools that read text people or programs wrote and say something
exact about it. Its defects are a panic on malformed input, an offset counted in the wrong
unit, a partial parse reported as success, an edit applied over a stale range, output that
changes between runs, and a recursive walk that overflows the stack on deep input.

## When to use this skill

- **Use it when** the change parses, walks, analyses, lowers, lints or rewrites source code or other structured text.
- **Signals:** `tree-sitter`, `syn`, `nom`, `winnow`, `chumsky`, `logos`, span or offset types, visitors, rule registries, diagnostics.
- **Skip it for** the command-line shell around the tool (the command-line skill) and binary file formats or wire protocols (the storage and protocols skill).
- **It is complete on its own.** The Rust essentials, the gate commands and the definition of done are at the end.

## The defaults, in priority order

If unsure what matters most, work down the list.

1. **No input panics the tool.** Slicing and arithmetic on anything derived from input are checked, and input size and nesting depth are bounded.
2. **Offsets name their unit** (bytes, characters, UTF-16 units, lines and columns) in the type, and are converted in one place. Text is taken by byte range, never by counting `chars()`.
3. **A parse says what it could not do.** Partial results are labelled partial; "no results" and "could not parse" are different outcomes.
4. **Diagnostics keep their location** through every layer: file, span, and the rule that produced them.
5. **Output is deterministic.** Sort before emitting; never let `HashMap` order or thread timing decide.
6. **Edits are validated before any is applied:** in bounds, on character boundaries, non-overlapping, against the text they were computed from.
7. **Depth controlled by input is walked with an explicit stack or cursor,** not recursion.
8. **Closed sets are enums matched exhaustively;** an unknown rule, kind or key is an error with a suggestion, not a silent default.
9. **Property tests, a malformed-input corpus and a fuzz target** accompany every parser.

**How this kind of Rust differs from application Rust.** These are the answers for
infrastructure code, stated flatly:

- **Allocation, layout and algorithmic cost are design inputs,** not afterthoughts. They are still decided by measurement, never by instinct.
- **Errors are typed,** carry positions or keys, and never erase which failure happened. `anyhow` stops at the binary.
- **Input is hostile.** Every length, offset, depth and count from outside is bounded and checked; no input may panic the code.
- **Output is deterministic:** the same input gives the same bytes on every run and machine.
- **Evidence is heavier:** property tests and fuzzing for anything that reads bytes, `loom` or a model for hand-written synchronisation, benchmarks with a baseline for every speed claim.
- **Data structures and traits are the design.** Choosing them is the work, where in a service one concrete type would do.

## Parsers, rule engines and linters

Rules for the cases where a task builds or extends one.

- **Operators that share a parse shape are a table,** `const BINARY_OPS: &[(Token, Prec, Assoc)]`, driving one precedence-climbing function. A new operator is a row.
- **Try the most specific alternative first.** Add a broad fallback only after a real input proves the need, and give every fallback branch a corpus case.
- **Context-sensitive lexing is explicit lexer state:** a closing delimiter that must match its opener (heredocs, raw strings with a variable number of `#`) stores the opener and clears it on close. Indentation-sensitive layout is an indent stack, with no indent or dedent tokens inside brackets. If the parser is incremental, that state serialises and the round trip is tested.
- **A large grammar, schema or rule set is composed from modules,** and composition fails on a duplicate name. A later module never silently wins.
- **A translator from a specific tree to a common model is pure:** no I/O, no logging, no global state. Queries are compiled once, not per file. The caller adds file and repository context one layer up.
- **Names emitted by a parser stage are a contract** with the stage that consumes them. Each new one gets a fixture that follows it to its destination. Same-named items (overloads) get a disambiguator so one does not overwrite another.
- **A rule engine filters once and buckets by kind,** so each item meets only the rules that can apply; route on the enum variant, not on a string prefix. The walker visits the tree once and dispatches by node kind. With a handful of rules, plain `if` statements are clearer.
- **A rule trait with default no-op hooks** lets a rule opt into raw source, selected nodes, or a final pass:

```rust
pub trait Rule {
    fn node_kinds(&self) -> &[&str] { &[] }
    fn check_source(&mut self, _source: &str) -> Vec<Issue> { Vec::new() }
    fn check_node(&mut self, _node: &Node, _source: &str) -> Vec<Issue> { Vec::new() }
    fn finish(&mut self, _source: &str) -> Vec<Issue> { Vec::new() }
}
```

- **Parser inputs are hostile.** Bound recursion depth, input size and time; return an error with a byte offset; never panic on malformed input. A fuzz target or a property test (`parse` never panics; `print(parse(x))` re-parses to the same tree) finds what examples miss.

## Text, positions and source

**A node travels with its source.** When every operation on a syntax node needs the original
text, pass a wrapper holding both; children are derived with the same source, so a node and
its text cannot drift apart.

```rust
#[derive(Clone, Copy)]
pub struct NodeWithSource<'a> {
    pub node: Node<'a>,
    pub source: &'a str,
}

impl<'a> NodeWithSource<'a> {
    pub fn child(&self, field: u16) -> Option<Self> {
        self.node.child_by_field_id(field).map(|node| Self { node, source: self.source })
    }
    pub fn text(&self) -> Result<&'a str, Utf8Error> {
        self.node.utf8_text(self.source.as_bytes())
    }
}
```

- The general rule: when two values are only meaningful together (an index and its collection, an offset and its text, a handle and its arena), give them one type.
- *Unnecessary when* the tree owns its text.

**Coordinates exist in several units; convert in one place.** Parsers count bytes, editors and
LSP count UTF-16 code units by default, people count lines and columns, and a "character" on
screen may be several `char`s.

- One type per coordinate system. A conversion is an explicit function that takes the text; nobody does range arithmetic across units by hand.
- Compute all units in one pass over a line so they cannot drift, and keep a table of line-start offsets when conversion is frequent.
- Test with ASCII, a two-byte character, an emoji outside the basic plane (two UTF-16 units, four UTF-8 bytes), a combining mark, a tab, and CRLF line endings.
- A column shown to a person is one-based and, for alignment, depends on display width (`unicode-width`), which is a fourth number.
- **A fragment parser tries a small set of wrapping contexts** (as an expression, as a statement, as an item), records the wrapper offsets so the fragment's own range can be recovered, and reports which context parsed. Many contexts mean ambiguous matches.
- **A whole-file follow-up found during a tree walk** (reformat, fix imports) is registered as a deferred pass that runs once afterwards. A node visit does not restart from the root.

## Transformations that must not lose data

These apply to anything that rewrites, merges, formats or migrates someone else's content.

**A smart algorithm over a trusted conservative one.** Guard the smart path with cheap
preconditions, check its output, and fall back.

```rust
if is_binary(base) || is_binary(ours) || is_binary(theirs) {
    return fallback(base, ours, theirs, FallbackReason::Binary);
}
if [base, ours, theirs].iter().any(|text| text.len() > MAX_SMART_BYTES) {
    return fallback(base, ours, theirs, FallbackReason::TooLarge);
}
let merged = smart_merge(base, ours, theirs)?;
if !postconditions_hold(&merged, ours, theirs) {
    return fallback(base, ours, theirs, FallbackReason::SuspiciousOutput);
}
```

- Preconditions cover what the smart path cannot handle (binary, size, unsupported syntax). Postconditions look for lost or duplicated content.
- **Every fallback is recorded with its reason and counted.** A silent fallback hides that the smart path stopped working; a fallback rate that climbs is a bug report.
- Tests include an adversarial input that forces each fallback, and one that proves the smart path leaves untouched content byte-identical.
- *Skip when* there is no trusted simpler implementation to fall back to. Then the failure is an error, not a guess.

**Pair every structural rewrite with a cheap conservation check.** Count what must be conserved
before and after, and return the original on any difference.

```rust
let mut balance = HashMap::<ItemSignature, i32>::new();
for signature in signatures_of(original)? {
    *balance.entry(signature).or_insert(0) += 1;
}
for signature in signatures_of(&rewritten)? {
    *balance.entry(signature).or_insert(0) -= 1;
}
if balance.values().any(|count| *count != 0) {
    return Ok(original.to_owned()); // something was lost or duplicated
}
```

- **Formatters and codemods are idempotent and output still parses.** Both are tests: `format(format(x)) == format(x)`, and the result parses to an equivalent tree.
- **Re-parse after every change to the text.** No pass reads a tree built from an earlier version of the string.
- **Protected regions round-trip byte for byte.** Replace each opt-out region with a placeholder that cannot collide with real content, run the passes, restore, on every path including errors.
- **Reordering uses a stable sort,** carries comments and attributes with their item, and leaves unknown nodes in place. Do not reorder where order has meaning (macro definitions, `mod` declarations with `#[macro_use]`, trait-impl overlap, SQL migrations).

**A plan carries unsupported work as data.** A planner for migrations, rollouts or refactors
returns the whole plan, with the parts it cannot do as typed steps, so a reviewer sees
everything at once. It does not stop at the first incompatible change.

```rust
#[derive(Serialize, Deserialize)]
#[serde(tag = "kind", rename_all = "snake_case")]
pub enum MigrationStep {
    AddType { name: String },
    RenameType { from: String, to: String },
    Unsupported { entity: String, reason: String },
}

pub struct MigrationPlan {
    pub steps: Vec<MigrationStep>,
}

impl MigrationPlan {
    pub fn is_executable(&self) -> bool {
        !self.steps.iter().any(|step| matches!(step, MigrationStep::Unsupported { .. }))
    }
}
```

- Planning is pure and separate from execution: plan, show, confirm, apply. The executor refuses a plan that contains an unsupported step; it never skips one.
- The plan is serialisable, so it can be reviewed, stored and replayed.

**Coordinating several writers.** A claim ("agent A is editing this") is an advisory lock; it is
not proof that nothing else changed. Detect concurrent edits with a version (a counter, a
content hash, or a version vector with one counter per writer) checked at write time, and
expire stale claims with a heartbeat. *For one writer, or where a hard lock is acceptable, a
database transaction is simpler and stronger.*

## Trees, lowering and decision gates

**Recursion control is a value.** A tree walk's hooks return what to do next, and a node type
implements only `apply_children` to get the walk for free.

```rust
pub enum Recursion {
    Continue, // keep walking
    Jump,     // skip this subtree
    Stop,     // end the whole walk
}

pub trait TreeNode: Sized {
    fn apply_children<F>(&self, f: F) -> Result<Recursion>
    where
        F: FnMut(&Self) -> Result<Recursion>;

    fn visit<V: Visitor<Node = Self>>(&self, visitor: &mut V) -> Result<Recursion> {
        match visitor.pre_visit(self)? {
            Recursion::Stop => return Ok(Recursion::Stop),
            Recursion::Jump => return visitor.post_visit(self),
            Recursion::Continue => {}
        }
        if let Recursion::Stop = self.apply_children(|child| child.visit(visitor))? {
            return Ok(Recursion::Stop);
        }
        visitor.post_visit(self)
    }
}
```

- Visitors do not smuggle control flow through side-effect flags. Each early exit has a comment, and the continue, jump and stop cases each have a test.
- **Recursion depth follows input depth.** For trees built from untrusted or generated input, cap the depth and return an error, or walk with an explicit stack. A stack overflow is an abort, not a `Result`.
- *Skip for* shallow data of fixed shape: a `match` is simpler.

**Lower the parse tree to a small typed tree first.** Do not run domain logic on generic parser
nodes with string kinds. Convert into the smallest typed tree that holds what the algorithm
needs, keeping a span on every node for diagnostics.

```rust
pub enum Statement {
    Simple { text: String, span: Range<usize> },
    Return { text: String, span: Range<usize> },
    If { cond: String, then: Box<Statement>, otherwise: Option<Box<Statement>>, span: Range<usize> },
    While { cond: String, body: Box<Statement>, span: Range<usize> },
    Block(Vec<Statement>),
}
```

- The lowering is where "unsupported construct" is reported, once, with a span. After it, the algorithm matches exhaustively and has no string comparisons.
- A tree with single ownership is `Box` and `Vec`. `Rc<RefCell<_>>` is for real sharing; a graph is usually better as an arena, a `Vec` of nodes addressed by index.
- Test the conversion before building anything on it.
- *Skip when* the work needs full fidelity: comments, whitespace, exact tokens (formatters, refactoring tools).

**Scoped context is passed by value.** A recursive pass that needs "where does `break` go from
here" carries the answer in a small `Copy` struct, not in mutable state it must remember to
restore.

```rust
#[derive(Clone, Copy)]
struct Scope {
    break_target: Option<NodeIndex>,
    continue_target: Option<NodeIndex>,
}

let body_scope = Scope { break_target: Some(loop_exit), continue_target: Some(loop_update) };
build(body, graph, body_scope)?;
// the caller's scope is untouched here
```

- With a mutable context the save and restore must bracket every recursive call, including the early-return paths; a missed restore leaks one branch's state into the next. If mutation is unavoidable, restore through a guard whose `Drop` does it.
- Every new control construct gets a test with nesting.

**Placeholders never leave the builder.** Internal scaffolding (dummy nodes, sentinel entries)
is acceptable while building, provided a normalisation pass removes it and the boundary rejects
any survivor with a hard error before the value is returned, serialised or rendered.

```rust
while remove_unreachable_nodes(&mut graph) {}
while remove_placeholder_nodes(&mut graph)? {}
ensure_no_placeholders(&graph)?;
```

- A cleanup loop runs to a fixed point: the function returns whether it changed anything, and each iteration must make progress, or the loop does not terminate.
- Stronger still is two types, a builder node with a `Placeholder` variant and a final node without one, so the conversion is the check.

**Ordered pure rules with evidence.** A decision gate (access, quota, deployment, safety)
evaluates pure rules in priority order, with the rule name as tie-breaker. Each returns a
decision, structured evidence and a readable reason.

- Rules do no I/O. Facts are gathered first and passed in, which makes every rule a table test and makes the decision reproducible from the recorded inputs.
- Record the decision, the deciding rule and the evidence. "Denied" with no rule name cannot be debugged.
- State the combination policy (first match, or deny overrides allow) and what happens when no rule matches. For anything security-relevant, no match means deny.
- Each rule is tested alone and in interaction with the rules above it.

**Render back ends behind one trait.** Parse, then build the model, then render. The model
knows nothing about output formats, and each format is one small implementation over it.

```rust
pub trait Render {
    fn render(&self, graph: &Graph) -> Result<String>;
}

pub enum Backend { Dot, Tikz, D2 }

impl Render for Backend {
    fn render(&self, graph: &Graph) -> Result<String> {
        match self {
            Backend::Dot => dot::render(graph),
            Backend::Tikz => tikz::render(graph),
            Backend::D2 => d2::render(graph),
        }
    }
}
```

- For a closed set of back ends an enum with a `match` needs no macro and no boxing. The `enum_dispatch` crate generates the same thing when the trait has many methods.
- Escaping belongs to the back end. Every back end is tested with labels containing its own special characters (quotes, braces, backslashes, newlines).
- Output is deterministic: iterate in a defined order, so the rendered text can be compared in a snapshot test.

**Fetch context in rungs.** When gathering context is expensive (for an agent or a tool), order
the sources from cheapest to dearest (summary, outline, the relevant path, raw source). Start at
the cheapest and go up a rung only when the current one did not answer the question, under a
hard cap.

## Pipelines, registries and handler chains

**A phased pipeline is data.** A compiler, indexer or ETL job is an ordered table of passes,
each with a name and a failure policy.

```rust
struct Pass {
    name: &'static str,
    required: bool,
    run: fn(&mut Context) -> anyhow::Result<()>,
}

for pass in PASSES {
    let started = Instant::now();
    let result = (pass.run)(&mut ctx);
    tracing::info!(pass = pass.name, elapsed = ?started.elapsed(), ok = result.is_ok());
    match result {
        Err(error) if pass.required => return Err(error.context(pass.name)),
        Err(error) => {
            tracing::warn!(pass = pass.name, %error, "optional pass failed");
            ctx.degraded.push(pass.name);
        }
        Ok(()) => {}
    }
}
```

- **Order is behaviour.** A new pass states what it needs from earlier passes and where it sits, and gets a test for cancellation after it.
- **"Optional" is rare and visible.** An optional pass that fails is recorded in the result (`degraded` above), not only logged, so the caller and the tests can see it. Default to required; a pass nobody would miss should not exist.
- *Skip the table for* two or three steps. Three function calls in a row are clearer than a pass framework.

**A handler chain where a handler can say "not mine".** In a chain of plugins, codecs,
authentication schemes or planners, each handler returns `Result<Option<T>>`: `Ok(None)` means
"not mine", `Err` means "mine, and it failed".

```rust
let mut plan = None;
for planner in &self.planners {
    plan = planner.plan(node, inputs).await?;
    if plan.is_some() {
        break;
    }
}
let plan = plan.ok_or_else(|| PlanError::NoPlannerFor { node: format!("{node:?}") })?;
self.ensure_schema_matches(node.schema(), &plan)?;
```

- The first `Some` wins, so registration order is behaviour: document it and test two handlers that both accept an input.
- "Nothing accepted this" is its own error and names the input.
- Validate what a handler returns before trusting it; a plugin is not your code.
- *Anti-pattern:* a handler that returns `Ok(None)` on its own failure. The chain then moves on and the real error is lost.
- If every handler must handle every input, use plain `Result`.

**Check every rewrite rule where it runs.** A rewrite pipeline (optimiser, tree or graph
transform) wraps each rule in a postcondition that names the rule, so a bad rewrite is caught
next to its cause and not three passes later.

```rust
let before = plan.schema();
let plan = rule.rewrite(plan, config)?;
if !is_allowed_schema_change(&before, &plan.schema()) {
    return Err(OptimizerError::SchemaChanged { rule: rule.name().to_owned() });
}
#[cfg(debug_assertions)]
check_invariants(&plan)?;
```

- Cheap checks always run. Whole-structure walks run under `cfg(debug_assertions)` or a flag, and CI runs the test suite with them on.
- Each rule ships with a negative test built on a deliberately invalid rewrite, which proves the check can fire.
- Say what the check does not cover. A partial invariant read as a full one gives false confidence.

**Registries.**

- **An open set is a trait plus registration; a closed set is a `match`.** Use a registry when the set is meant to grow without edits to the orchestration (languages, providers, formats). For one or two cases a `match` is simpler and exhaustive.
- **An unknown key is a typed error that lists the supported values.** Never a panic on a missing map entry, never a silent default.
- **Decide the duplicate policy** (reject, or last wins) and test it. Reject is the safer default.
- **Capabilities are read from the registry.** Do not keep a second hand-written support matrix; it will drift. Capability tests and help output query the registry.
- **A new member is added to every per-member table in one change,** with one smoke fixture that exercises the whole path.
- **The fallback arm of a dispatcher returns a domain error naming the operation and the back end** ("no translation for `X` in back end `Y`"), raised at the dispatch point. Not `unreachable!()`, and not a missing-function error from deep inside.

**Extension traits: each default states what it means.** Required methods form the core
contract. For every default method decide whether it means *unsupported* (an error naming the
operation), *no-op* or *delegate*. A default encoder that returns `Ok(())` loses data silently;
prefer the explicit unsupported error unless a round-trip test proves the no-op is lossless.
Decode failures are always explicit.

**Inject content access.** An analyser or parser takes a narrow reader, for example
`impl Fn(&Path) -> io::Result<Vec<u8>>`, and does not call `std::fs::read` itself. The same
logic then runs over the working tree, a Git revision or an in-memory fixture. Document whether
paths are absolute or relative to a root. *Skip when* the code needs metadata, streaming or
directory walking; pass a small file-system trait then.

**A storage capability in front of handlers.** Handlers depend on a few domain operations
(`begin_upload`, `reader`, `finalize_upload`), not on file paths or bucket names. Add a method
when a second call site needs it. *Skip when* there is one back end, no test double, or the
call sits in a hot loop where a boxed reader per item costs too much.

**Derived state is computed, not stored.** `plan.is_executable()` is derived from the steps; a
stored `supported: bool` can disagree with them. Store a derived value only as a measured
cache, with one function that updates both.

## Registries, back ends and generated code

**One declaration line per variant, when the same list drives several sites.** A small macro
turns a list of names into the enum and its dispatch, so the two cannot drift.

```rust
pub trait Phase {
    fn apply(&self, items: &mut Vec<Item>);
}

macro_rules! declare_phase_kind {
    ($($name:ident = $phase:expr),* $(,)?) => {
        #[derive(Clone, Copy, Debug, PartialEq, Eq)]
        pub enum PhaseKind { $($name,)* }

        impl PhaseKind {
            pub const ALL: &'static [PhaseKind] = &[$(PhaseKind::$name,)*];
        }

        impl Phase for PhaseKind {
            fn apply(&self, items: &mut Vec<Item>) {
                match *self { $(Self::$name => $phase.apply(items),)* }
            }
        }
    };
}

declare_phase_kind! {
    Desugar = DesugarPhase,
    Inline = InlinePhase { threshold: 8 },
}
```

- The enum is `Copy` and can be named in configuration and in ordered phase lists. `ALL` lets a test assert that every kind appears in at least one pipeline.
- *Skip the macro* for a list used in one place. A plain enum with an exhaustive `match` already fails to compile when a variant is missing, and anyone can read it.
- A phase with run-time state does not fit a `Copy` variant; that calls for a registry of boxed values.

**When one matrix drives many sites, keep one inventory macro that takes a callback.**

```rust
macro_rules! for_all_sources {
    ($callback:ident) => {
        $callback! {
            { Kafka, KafkaProperties, KafkaSplit },
            { Pulsar, PulsarProperties, PulsarSplit },
        }
    };
}

macro_rules! declare_properties_enum {
    ($({ $name:ident, $props:ty, $split:ty }),* $(,)?) => {
        pub enum SourceProperties { $($name($props),)* }
    };
}
for_all_sources!(declare_properties_enum);
```

- Adding a row updates every generated site at once. That is the whole benefit, and it is real only from about three sites up.
- Callback macros are hard to read and produce poor errors. Keep each callback small, and keep the row shape identical everywhere.

**A back end is a narrow trait: shared flow provided, the difference required.**

```rust
pub trait Backend {
    type Printer: Printer;
    const NAME: &'static str = <Self::Printer as Printer>::NAME;

    fn phases(&self) -> Vec<PhaseKind> {
        Vec::new()
    }

    /// The one thing every target must supply.
    fn module_path(&self, module: &Module) -> PathBuf;

    fn emit(&self, modules: Vec<Module>, printer: Self::Printer) -> Vec<File> {
        /* shared flow, written once */
    }
}
```

- Preparation (phases) stays separate from rendering (the printer); escaping rules for a target live only in its printer.
- A shared phase can carry one target's assumptions into another. Review each back end's phase list on its own.
- *Not for* targets whose pipelines have nothing in common; forcing them under one trait produces a trait of optional methods.

**Capabilities become parser settings before parsing.** Permissions and feature gates are
turned into settings by one function, and the parser consults the settings. Checking the tree
afterwards means every new syntax needs a second, forgettable check.

```rust
pub fn settings_from(capabilities: &Capabilities) -> ParserSettings {
    ParserSettings {
        files_enabled: capabilities.allows(Experimental::Files),
        ..ParserSettings::default()
    }
}
```

- The same text can be valid under one setting and invalid under another, so the diagnostic names the disabled capability, not just "unexpected token".
- The entry point rejects input longer than the offset type can address (a `u32` offset means inputs up to 4 GiB) with a typed error, before parsing.

**A recursive parser spends a depth budget, and every exit restores it.** Unbounded recursion
on untrusted input is a stack overflow, which aborts the process and cannot be caught.

```rust
fn nested<T>(
    &mut self,
    span: Span,
    parse: impl FnOnce(&mut Self) -> Result<T, SyntaxError>,
) -> Result<T, SyntaxError> {
    if self.depth_left == 0 {
        return Err(SyntaxError::too_deep(span));
    }
    self.depth_left -= 1;
    let result = parse(self);
    self.depth_left += 1;
    result
}
```

- Every recursive production goes through the one helper (or one `Drop` guard). Nobody edits the counter by hand, and `?` inside the closure cannot skip the restore.
- Pick the limit from the smallest stack the parser runs on: a spawned thread defaults to 2 MiB, less than the main thread. Test the limit on that stack, in a debug build, where frames are largest.
- Test both the depth error and that a parse succeeds after one failed, which proves the budget came back.
- The same applies to every recursive walk over the tree afterwards: visitors, printers, `Drop` of a deeply nested tree. A parser limit protects them all only if they recurse no deeper than it did.

**Generated bindings come from a typed spec list and are written atomically.** What to
generate is data (an enum of wrapper kinds), so adding an item is one entry plus a generator
test; nobody edits generated files by hand.

```rust
fn save_atomically(content: &str, target: &Path) -> io::Result<()> {
    let dir = target.parent().unwrap_or(Path::new("."));
    let mut file = tempfile::NamedTempFile::new_in(dir)?;
    file.write_all(content.as_bytes())?;
    file.as_file().sync_all()?;
    file.persist(target).map_err(|e| e.error)?;
    Ok(())
}
```

- The temporary file is created in the target's directory. A rename is atomic only within one filesystem; a temp file under `/tmp` may not be.
- On Unix the temporary file is created readable by the owner only, and keeps that mode after `persist`. Set permissions explicitly if others must read it.
- `sync_all` matters when the file must survive a crash; skip it for build outputs that can be regenerated.
- Generation is idempotent: the same spec gives the same bytes, and unchanged output is not rewritten, so timestamps do not trigger rebuilds.
- Validate each spec at generation time. A wrong signature that is only discovered at the foreign call is a run-time crash.

## Closed sets and normalised inputs

**A closed set is an enum, decoded at the edge.**

- **Finite command-line choices derive `clap::ValueEnum`; paths are `PathBuf`.** The parser then validates, lists the choices in `--help` and reports a typo with the alternatives.
- **A kind is never a `String` explained in a comment.** Parse it once (file extensions case-insensitively, with `eq_ignore_ascii_case`), returning `None` or a typed error for anything unknown.
- **A `type` discriminator in data is an enum** with `#[serde(tag = "type")]`, not an `Option<String>` beside a bag of optional fields. Model a published format the way its specification writes it, and link the specification from the type's docs.
- **Options are typed per back end:** `enum Backend { Embedded(EmbeddedOptions), Remote(RemoteOptions) }`, decoded once. A `HashMap<String, Value>` read by string key defers every typo to run time.
- **A fixed set of roles is a struct with a field per role,** not a map from name to value. A missing role is then a compile error instead of a silent default.
- **Allowed combinations are one table:** a `match (from, to)` or a `const` slice of pairs. Evaluation consults it first; anything absent is an error. Scattered `if` checks will disagree.
- *An open set stays open.* If users or plugins may add kinds, an enum with `Other(String)` or a validated newtype is the honest model; an enum that must be edited for each new customer is a bottleneck.

**Several input shapes become one type at the edge.**

```rust
#[derive(Deserialize)]
#[serde(untagged)]
enum SpecInput {
    One(String),
    Many(Vec<String>),
    WithMetric(BTreeMap<String, String>),
}

impl SpecInput {
    fn into_specs(self) -> Vec<Spec> {
        match self {
            Self::One(name) => vec![Spec { name, metric: None }],
            Self::Many(names) => names
                .into_iter()
                .map(|name| Spec { name, metric: None })
                .collect(),
            Self::WithMetric(map) => map
                .into_iter()
                .map(|(name, metric)| Spec { name, metric: Some(metric) })
                .collect(),
        }
    }
}
```

- Document the accepted shapes; they are public API, each with a test.
- **`untagged` tries variants in order and takes the first that fits.** Put the most specific first, and check that no input fits two. Its error on failure is "data did not match any variant", which tells the user nothing: for user-edited configuration, a hand-written `Deserialize` or a custom error naming the accepted shapes is worth the code.

**Normalise once, at the boundary.**

- **Empty, null and absent** that mean the same thing decode into one representation (`Option<NonEmptyString>`); code past the boundary never calls `is_empty()` again. *Where they differ* (a partial update: absent keeps, null clears), keep the distinction in a type such as `Patch<T>` and do not collapse it.
- **Whitespace-only is missing** for a required human-entered field: check `trim().is_empty()` and report one variant carrying the field name. *Do not trim* secrets, passwords or anything where whitespace is data.
- **Numbers, times and IDs that arrive as strings are parsed at the boundary** (`serde_with::DisplayFromStr`, a `deserialize_with` function, a newtype), so later code never parses again.
- **Units live in the type or the field name:** a `Duration` with an explicit serde adapter (`humantime_serde`), or `timeout_ms`. A unit that exists only in a comment will be misread.
- **Inferring types from untyped text has a stated, tested order.** If a loader tries "date" before "text", a string that merely looks like a date changes type silently. Document the order, test the ambiguous cases (`"1e5"`, `"NaN"`, `"2024-01-01"`, leading zeros), and let an explicit schema override inference. When several formats are tried, the error names the value and the formats tried.
- **Keep the decoding error as the source,** not flattened into a string, so line and column survive.
- **A parse is a function from input to a finished value.** No parser object whose fields fill in step by step and can be read half-done.
- **Normalise a symmetric operation by ordering its arguments once** (`let (lo, hi) = if a <= b { (a, b) } else { (b, a) };`) instead of writing both branches.
- **A hand-rolled entry point has one usage constant.** Where no argument parser is available (a host function, an FFI command), every arity or type error prints the same `USAGE` text.

**Per-type facts live on a trait; one generic function does the work.**

```rust
pub trait Record: Send + Sync + 'static {
    const TABLE: &'static str;

    fn to_batch(rows: &[Self], embeddings: &[Vec<f32>]) -> Result<Batch, StoreError>
    where
        Self: Sized;
}

fn store<R: Record>(db: &Db, rows: &[R], embeddings: &[Vec<f32>]) -> Result<(), StoreError> {
    if rows.len() != embeddings.len() {
        return Err(StoreError::LengthMismatch {
            rows: rows.len(),
            embeddings: embeddings.len(),
        });
    }
    db.append(R::TABLE, R::to_batch(rows, embeddings)?)
}
```

- **Parallel slices are checked for equal length at entry,** with both lengths in the error. Better still, take one slice of pairs so the mismatch cannot be written.
- Where operations carry a numeric type code (`const TYPE: u16`), a test asserts the codes are unique. Duplicates otherwise dispatch to the wrong handler without any error.

**Smaller rules.**

- **A width-changing cast says whether it sign-extends.** `-1i8 as u64` is `u64::MAX`; `-1i8 as u8 as u64` is `255`. Write the intent in named steps (`u64::from(x as u8)`), use `From` for lossless widening and `try_from` for narrowing, reinterpret same-width bits with `to_ne_bytes` or `to_bits` and never `transmute`. Test with `-1` and the extremes. `clippy::cast_possible_truncation`, `cast_sign_loss` and `cast_possible_wrap` find the rest.
- **"Unsupported" differs from "supported and empty".** A field populated only for some inputs is `Option<Vec<_>>`, with `None` meaning unsupported and the schema saying when. An empty list that might mean either is a wrong answer waiting to be trusted.
- **A handler validates its arguments before any expensive or state-dependent work.** Decode raw input into a typed struct; an unknown enum-like value is an error listing the accepted ones, never a silent default. Otherwise an argument mistake is hidden behind an unrelated later failure.
- **A required per-implementation constant has no default.** `const EXTENSIONS: &'static [&'static str];` without a default makes forgetting it a compile error; an empty default silently supports nothing.
- **`Default` and `new` never fail or panic, and are cheap.** A constructor that looks something up is `try_new() -> Result<Self, _>`. Expensive construction has a verb name (`Index::build(&source)`). When both `new()` and `Default` exist, one calls the other.
- **A derived view borrows its source** (`struct Graph<'a> { parse: &'a ParseResult, .. }`), so it cannot outlive or drift from what it was built from.
- **A child handle may borrow its parent** (`Connection<'db>` holding `&'db Database`), and the compiler then enforces drop order for free. *The cost:* the lifetime makes the handle awkward to store in a struct or move into a spawned task. For handles that travel, share the parent through an `Arc` instead.
- **An algorithm takes its own small parameter struct** of validated values (`NonZeroUsize`, a ratio newtype), built from user configuration in one conversion. The algorithm crate does not depend on the configuration or CLI crate.
- **A command prompts only when attached to a terminal.** If `std::io::stdin().is_terminal()` is false, a missing argument is an error naming the flag. A prompt in CI is a hang.
- **A line-oriented protocol is a tagged enum, and its parse errors carry the line number.** Responses echo the request ID.
- **A tuple that needs a comment to explain its positions is a struct.** `(usize, usize, bool)` becomes named fields and an enum for the flag.

## Algorithms, dispatch and dynamic data

**An algorithm is written against the smallest contract it needs.** Not against one concrete
container: a trait with the few operations used (node count, neighbours, degree), which each
representation implements. Run it against at least two implementers in tests. *Skip the trait*
while there is one representation and no second in sight.

**Results cannot be read before the run.** `fn run(self) -> Finished`, or a `run` that returns
the result, makes "read before running" and "read after a failed run" impossible to write.

- Where a flag is unavoidable (bindings to another language), set it false at the start, true only after complete results exist, never on the error path, and every getter checks it.
- A reusable algorithm object separates its state (with `reset`) from its driver. Test by running the same instance twice; stale state from the first run is the usual bug.

**Shared scaffolding lives in a provided method.** The trait's provided method sets up what
every implementation needs (progress, naming, accounting) and calls one small required
method. Implementers write only that. A change to the provided method changes every
implementation at once, so keep it conservative, and do not let implementers override it.

**Register by type, dispatch by dense index.** Registration stays ergonomic and typed; at
start-up it is compiled once into a `Vec` indexed by a compact, stable code.

- Before the hot loop, check that every advertised code has a handler and is in range.
- Codes that are sparse, untrusted or change at run time use a map, and an unknown code is an error, not an index panic.

**Dynamic side data has typed handles.** Attributes chosen at run time live in a registry of
type-erased storages; reads and writes go through a typed handle. Attaching rejects a duplicate
name; a typed read checks the stored type and returns an error on mismatch; a handle is
invalid after detach. *A fixed set of attributes is plain struct fields.*

**Smaller rules.**

- **An optional consistency check is an explicit value on the request** (`Option<ExpectedVersion>`), not a side channel in the executor. Test "absent" and "mismatch".
- **A command that can return several shapes carries the expected shape** beside the statement, so encoding, execution and decoding share one contract.
- **Dynamic, stringly-typed access is for the edge only:** a remote API whose endpoints are not known when the client ships. Wherever a typo must fail at compile time, write typed methods.
- **Operator overloading must not surprise.** Use `std::ops` where the algebra is the ordinary one (vectors, durations, money in one currency). For a DSL, where precedence or laziness would mislead, prefer named methods.
- **Messy input forms are normalised once** into a small typed value; the accepted forms and their error messages are public API with a test each.
- **One gate owns timing policy.** A scheduler or load driver asks one place "may this run now", backed by an injectable clock. Tests use a fake clock; callers never repeat schedule checks.

## Diagnostics at scale

- **Explain the known cause, keep the original.** At startup and configuration boundaries, match the typed causes you recognise and print what it means plus one concrete action ("port 8080 is in use; pass `--port` or stop the other process"), with the original error attached. Do not guess at causes you have not matched: a confident wrong hint is worse than the raw error.
- **Presentation is owned by helpers, facts by the error.** Quote and escape every interpolated identifier, path and value through shared helpers, so messages are consistent and hostile input cannot inject control characters or fake log lines.
- **Rate-limit a log line on a hot failure path, and count it.** Keep the state per call site (a `static` atomic counter and timestamp), and pair it with a metric, since suppressed lines hide how often it happens. Never rate-limit security or audit events.
- **One `ensure!`/`bail!` pair per crate** that builds the crate's typed error, if invariant checks are numerous. Use the project's existing macros; a new error macro hides control flow and must earn its place through repetition.
- **A debug switch for backtraces, not a second code path.** Capture a `Backtrace` in the error when `RUST_BACKTRACE` (or a project variable read once) asks for it. Keep the default path cheap.
- Install a report handler (`color_eyre::install()`, `miette`'s hook) once, at the top of `main`, in the binary only.
- `snafu` is an alternative to `thiserror` when most call sites need to attach context to the same underlying error: its context selectors make "this I/O error, while reading this path" one short expression. Use one of the two per crate.

**An error that crosses a process or language boundary is versioned data.** Its numeric code
and stable name are a wire contract.

```rust
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
#[repr(u32)]
pub enum WireCode {
    Unknown = 1,
    InvalidConfiguration = 2,
    ResourceNotFound = 20,
}

impl WireCode {
    pub fn from_u32(raw: u32) -> Self {
        match raw {
            2 => Self::InvalidConfiguration,
            20 => Self::ResourceNotFound,
            _ => Self::Unknown,
        }
    }
}
```

- Every variant has an explicit number. Never renumber or reuse one; retire it and leave a comment.
- **Decoding an unknown code yields `Unknown`, not a failure,** so an old client survives a new server.
- Send the code, a stable machine name and a human message as separate fields. Clients branch on the code, never on the message, which is then free to improve.
- Use the stable name in metrics and logs. *Not for* internal errors, which should stay free to change.

## Rules for tools that process source

- **Read back what an external tool actually did.** After starting a tool or service, read the port, path and URL it recorded and check health before using it; do not assume the values you asked for took effect. Give each run its own directory and pin the tool's version.
- **Bound the time of work you do not control.** Parsing an arbitrary file, calling a plugin or running a subprocess gets a deadline, and a timeout is a per-item result, not a crash. A deadline may scale with input size under a named ceiling. On timeout take the unoptimised but correct path; never use a partial result.
- **Bootstrap is idempotent.** Schema and index creation can run on every start, and writes that may repeat are explicit upserts.
- **A downloader streams.** Decompress as bytes arrive, keep URLs and references as typed values, report progress through a channel, verify the checksum, and set the executable bit only after the file is complete.
- **A generator fails or omits the record when an input is unreadable.** The error is a diagnostic; its text is never written into the artefact where content belongs. Every generated file starts with a `@generated` marker, and indexers, formatters and reviewers skip marked, vendored and minified files.
- **A code generator returns its fragments and its shared definitions separately,** and the caller emits each shared definition once.
- **Extra context gets a named entry point over one private worker.** `parse_file(source, lang)` and `parse_path(source, lang, path)` both call a private function taking `Option<&Path>`. Callers never write `None`.
- **A table with two enum keys is one exhaustive `match` on the pair,** with no wildcard arm. Nested string-keyed maps hide a missing combination; the `match` refuses to compile.

```rust
fn query_for(language: Language, kind: QueryKind) -> Option<&'static str> {
    match (language, kind) {
        (Language::Rust, QueryKind::Definitions) => Some(include_str!("queries/rust/definitions.scm")),
        (Language::Tsx, QueryKind::Definitions) => query_for(Language::TypeScript, kind),
        (Language::Rust, QueryKind::Folds) => None,
        // every remaining pair is listed
    }
}
```

- **A partial implementation rejects what it does not support before it starts.** A preflight pass returns a typed error naming the construct, so unsupported input is never half-understood.
- **Resolve an artefact in a fixed order and report which source was used.** A silent fallback location turns "works on my machine" into a mystery.
- **A process-wide cache has a reset,** for tests and for long-running hosts.
- **A finding carries the whole range and a context line.** A start position alone cannot be underlined or deduplicated.
- **A parse result keeps the tree with the bytes it came from** (`struct ParsedFile { tree, source: Arc<[u8]>, .. }`), so a byte range is never applied to a different buffer. Derived facts live in side tables keyed by node ID, so they can be dropped without re-parsing.
- **Extract one direction, derive the other.** Record outgoing references; build the incoming index from them. Two independently extracted directions will disagree.
- **Listings are computed from the registry.** Supported languages and extensions are derived from what is registered, and an ambiguous key (`.h` is C or C++) has a documented default and an override.
- **Say what is not produced.** If a language's support covers definitions but not call edges, the tool reports that per language. "Not supported" must never read as "no callers".
- **A dump is bounded.** Serialising a tree takes options (depth, include text) with no unbounded default.
- **Redact secrets before code leaves the machine,** record what was redacted, and send a chunk again only when its content hash changed.
- **Check proposed identifiers against the index.** Before accepting generated code that names a function or type, look the name up; an unknown name is reported, not assumed.
- **A relaxed format is normalised by a tested pure helper before a strict parse** (strip comments and trailing commas outside strings, then parse JSON).
- **Conversion failures inside a parser are parse errors at their position** (`map_res` in combinator libraries), never panics.
- **A byte classifier is a 256-entry table** built by a `const fn` and indexed by `u8`, so no index can be out of range.
- **One enum variant per kind of parsed thing,** not a tag plus unrelated optional fields. Unknown input is handled by an explicit arm.
- **A streaming decoder is resumable.** It keeps partial state between reads, and a test checks that any chunking of the input gives the same output as one call.
- **Reserved names have a prefix users cannot use** (`__name`), declared as a `pub const` and rejected in user input.
- **Documentation examples are files a test runs,** so a cookbook cannot rot.
- **Do not split a long file into numbered parts joined by `use super::*`.** Split by responsibility into named modules with explicit imports.
- **Two implementations of one thing share a trait, a documented default and a differential test** that compares them over a corpus, with the reference implementation as the oracle.
- **Parallel work items declare the files they modify,** and run concurrently only when those sets are disjoint.
- **An orchestrator's module doc lists its responsibilities,** and gives the reason when work is deliberately sequential, so nobody parallelises it without measuring.
- **Reduce a misparse to the smallest input and read the parser's trace** before changing the grammar. Every declared grammar conflict has a comment and a test input that needs it.
- **Build a line-start index once per file** and binary-search it. Calling `source.lines().collect()` or counting newlines for every symbol is quadratic in the file size.
- **An incremental command says how it detects change and what that can miss.** Modification time plus size is cheap and misses a same-size edit within the timestamp's granularity, so offer a content-hash mode. Do the CPU work in parallel and write from one thread in one transaction. The summary counts what was skipped and why.
- **Limits are a named struct, and every limit is enforced.** `ChunkLimits { max_lines, max_chars, overlap_lines }` replaces three positional numbers of the same type. Construction rejects nonsense (an overlap not smaller than the maximum). A limit that is accepted and never checked is a bug.
- **Unknown input falls back to a named strategy,** such as one whole-file chunk, so nothing is dropped silently. User configuration overrides the built-in table entry by entry.
- **Invented positions use one named constant** (`Span::DUMMY`), never a zero range written inline, so diagnostics can tell real positions from synthesised ones.
- **Wrappers are peeled in one loop into a flat result.** For modifiers, parentheses or reference markers around an inner node, walk inward with an exhaustive `match`, set a flag per wrapper and stop at the innermost name. A new wrapper kind is then a compile error in one place.
- **Copy out of a lending iterator inside the loop.** A streaming cursor's item borrows from the cursor, so use `while let Some(m) = matches.next()` and take what you need before the next step; it cannot be collected.
- **Do not glob re-export enum variants** (`pub use self::Kind::*`); it pollutes the namespace and a later variant can shadow a type. A type with an argument-free `new` also implements `Default`.

### Tools that serve automated callers

**A runner emits a typed event for every transition,** independent of how events are
transported, and takes its side-effecting call as an injected trait or closure so it can be
tested without the effect.

```rust
enum PlanEvent {
    PlanStarted { plan_id: PlanId, step_count: usize },
    StepCompleted { step_id: StepId, tool: String, output_preview: String },
    StepFailed { step_id: StepId, tool: String, error: StepError },
    PlanAborted { plan_id: PlanId, failed_step: StepId },
    PlanCompleted { plan_id: PlanId },
}
```

- A failure to bind arguments is a different error kind from a failure of the tool itself.
- Previews are length-capped. Extend behaviour by adding variants, not by changing existing ones.
- This fits a linear plan. Replanning, fan-out and conditionals need a real state machine.

**Limits and truncation.**

```rust
pub(crate) const READ_FILE_SOFT_CAP_BYTES: usize = 500 * 1024;       // truncate, and say so
pub(crate) const READ_FILE_HARD_CAP_BYTES: usize = 2 * 1024 * 1024;  // refuse
pub(crate) const CALL_GRAPH_DEFAULT_LIMIT: usize = 200;
```

- **Size limits are named constants with a soft cap and a hard cap,** and every list-returning operation has a default limit.
- **Apply a cap before formatting, and carry the truncation fact with the data** (the original count beside the kept rows), not in a side channel. Later transformations preserve it, and the warning is rendered from it at the end. Test under the limit, over it, and an invalid limit setting.
- **An empty result is a first-class response,** with a hint about what to try next, and is tested as carefully as a success. Keep hints from being so prescriptive that they steer callers off valid paths.
- **When evidence is quoted from files, re-check it is current before emitting it.** A snippet whose source range no longer hashes to the stored value is dropped; stale evidence is worse than none. Say what was omitted.
- **A threshold is `Option<f32>` when "no threshold" is a valid setting.** `0.0` and absent are different.

**Wire-level details.**

- **Chunked framing:** each chunk is a length followed by that many bytes, and a zero-length chunk ends the message. The sender need not know the total size, and the receiver can skip an unknown message whole. Decoder tests: one chunk, several, two messages back to back, the end marker, and **the input split at every byte boundary.** That last test finds most framing bugs.
- **Version negotiation:** the opening frame is fixed-size, the server answers with one chosen version or an explicit "none", and any reserved escape value is a protocol constant, never treated as an ordinary version. Test rejection, highest-common selection and the escape. Use a standard negotiator (TLS ALPN, HTTP) where one is available.
- **A tool's advertised schema and its handler are separate,** and the schema is derived from the typed argument struct (`schemars::JsonSchema`, doc comments as descriptions). An unknown tool name is an explicit error. A test inspects the generated schema.

**Heuristics and hints.**

- **Keyword heuristics are pure functions that match on word boundaries** (`\b` with `regex::escape`, compiled once in a `LazyLock`), so `class` does not match `classification`. Each keyword has one positive test and one near-miss negative test.
- **Model output handed to code is parsed into a contract.** "Could not parse" is a typed result, distinct from "parsed, no match".
- **Historical data is a bounded hint, never a dependency of a latency-sensitive path.** The lookup runs under a timeout, and a miss or timeout yields `None`. Advice from it applies only above a named sample floor and success threshold.
- Deterministic policy rules win over similarity scores.

**A local environment launcher** separates "what this service is" from "how services are
started, logged, checked and stopped". A new service implements a small description trait
(identifier, image, ports) and reuses the shared tasks for logs, lifecycle and readiness.
Keep a seam around command execution so the launcher is testable without starting anything.

**Encode a dependency boundary as a lint with an actionable message:**

```toml
# clippy.toml
disallowed-methods = [
    { path = "std::process::Command::new", reason = "use crate::exec::run_command (sandboxed, logged)" },
]
```

- **Deny `clippy::disallowed_methods` at the crate root;** the wrapper module carries the only `#[allow]`, with a reason.
- **Add the rule only once the replacement exists and is good enough.** A ban with no usable alternative produces a scatter of `#[allow]` attributes.
- `disallowed-types` and `disallowed-macros` work the same way. Keep exceptions few and justified.
- The lint matches the resolved path, so it does not catch the same function reached through a re-export it does not know, or through a dependency. It is a guard-rail for your own code, not a sandbox.

## Tests

**Property.** State the property, then let the generator find the counter-example.

```rust
proptest! {
    #[test]
    fn req_004_wire_round_trip(input in valid_entity()) {
        let encoded = encode(&input)?;
        let decoded = decode(&encoded)?;
        prop_assert_eq!(decoded, input);
    }
}
```

- Properties that pay for themselves: a round trip; agreement with a simple reference implementation; idempotence (`f(f(x)) == f(x)`); an invariant kept by every operation; "never panics" on arbitrary bytes.
- Commit the regression file `proptest` writes, and turn each counter-example it finds into a named unit test as well.
- A generator that produces only tidy values proves little. Include empty, maximal, non-ASCII and boundary values.
- Anti-pattern: a property that re-implements the function under test and compares the two copies.

**Fuzzing, for anything that takes bytes from outside.**

```rust
#![no_main]
use libfuzzer_sys::fuzz_target;

fuzz_target!(|data: &[u8]| {
    if let Ok(value) = my_crate::parse(data) {
        // Not only "does not panic": what parsed must survive a round trip.
        let again = my_crate::parse(&value.to_bytes()).expect("re-parse of own output");
        assert_eq!(value, again);
    }
});
```

- A target that only ignores the result finds panics, overflows (in debug) and hangs. Add an assertion and it finds logic errors: a round trip, agreement with a reference implementation, an invariant on the output.
- Seed the corpus with real inputs, and keep it. Every crash becomes a checked-in regression test with the minimised input.
- For structured input derive `arbitrary::Arbitrary` instead of hand-decoding bytes.
- Run it with a time limit on a schedule, not on every push. Set a per-input timeout and a memory limit so a hang or an allocation bomb is reported as a finding.
- *Use for* parsers, decoders, decompressors, protocol state machines, and unsafe code reachable from input. *Skip for* code whose input is already a validated domain type.

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

## Review

- Can any input, however malformed, deep or large, cause a panic, a hang or unbounded memory?
- Does every offset say what it counts, and is each conversion between units in one place?
- Is a partial or failed parse ever reported as a clean, empty result?
- Does every diagnostic carry its location and its rule?
- Is the output identical on every run for the same input?
- Is any edit applied to text other than the text it was computed from?
- Is there a property test, a corpus of malformed input and a fuzz target?

## Out of scope

- **Argument parsing, exit codes and file discovery for the tool's binary.** Use the command-line skill.
- **Binary formats, storage and wire protocols.** Use the storage and protocols skill.
- **Speed work on the parser's hot path.** Use the performance skill, with a benchmark.
- **Compiler internals beyond a lowering pipeline** (borrow checking, code generation) need specialist material.

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
