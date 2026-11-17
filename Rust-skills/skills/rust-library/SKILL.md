---
name: rust-library
description: Self-contained guide for library Rust - crates other code depends on, published or internal. Use when the task designs or changes a public API, types, traits, generics, error types, builders, conversions, feature flags, macros, procedural macros, build scripts, documentation, semantic versioning, minimum Rust version or crate packaging. Not for services, command-line glue, performance-critical kernels or unsafe code, which have their own skills.
---

# Rust for libraries and public APIs

A library is code whose callers you cannot see. Every public item is a promise, every
public type is something a caller will match on, store and wrap, and a mistake in the
interface is paid for by everyone downstream until the next major version. The defects of
this kind of Rust are interface defects: an error callers cannot handle, a dependency type
that leaked, an enum that cannot grow, a feature that changes behaviour for another crate,
a panic where a caller expected a `Result`.

## When to use this skill

- **Use it when** the change touches what other crates see: public functions, types, traits, errors, features, macros, documentation, versions.
- **Signals:** a `lib.rs`, `pub` items, `[features]`, `rust-version`, a crate published or shared across a workspace, `proc-macro = true`, `build.rs`.
- **Skip it for** application wiring (the service and command-line skills), hot loops and data structures (the infra skill), and `unsafe` (the unsafe and FFI skill).
- **It is complete on its own.** The Rust essentials, the gate commands and the definition of done are at the end.

## The defaults, in priority order

If unsure what matters most, work down the list.

1. **The public interface is a promise.** Start private, widen to `pub(crate)`, make an item `pub` only on purpose. Name every re-export at the crate root.
2. **Errors are typed and matchable.** No `anyhow::Error` or `Box<dyn Error>` in a public signature. Variants say what happened in terms the caller can act on, and keep their source.
3. **Room to grow without a breaking change:** `#[non_exhaustive]` on public enums and structs that will gain members, private fields with constructors, sealed traits where outside implementations must not exist.
4. **No dependency types in the interface,** apart from vocabulary crates such as `bytes`, `http` and `serde`. A dependency upgrade must not become your breaking change.
5. **Misuse is harder than correct use.** Borrowed inputs, validated newtypes, explicit conversions (`From` when it cannot fail, `TryFrom` when it can), a builder when construction has many options.
6. **A library never decides for its caller:** no printing, no global state, no chosen async runtime, logger or allocator, no configured global thread pool, no panic on a path input can reach. Panics, errors and safety conditions are documented.
7. **Features are additive.** Enabling one never removes an item or changes behaviour for another crate.
8. **Documentation is tested.** Every public item says what it does, when it errors and when it panics; examples are doc tests.
9. **Compatibility is checked, not hoped for:** the minimum Rust version is declared and built, interface changes go through `cargo semver-checks`, and the supported feature combinations are tested.
10. **Concrete first.** One implementation; a generic or a trait arrives with the second real use.

**How this kind of Rust differs from application Rust.**

- **Typed errors, not `anyhow`.** The application decides how to report; the library tells it what happened.
- **Cost matters more, because the caller is unknown.** Offer borrowed inputs and iterator outputs so the caller chooses whether to allocate. That is interface design, not optimisation; speculative tuning is still wrong.
- **A rename is a breaking change.** Add the new name, deprecate the old, remove it in the next major version.
- **Tests include misuse:** compile-fail tests for what must not compile, doc tests for what must.

## The contract on a function

An agent cannot ask the author what a function is supposed to do, so the contract sits on the
function: what it needs, what it guarantees, what it changes and how it fails. Use the rustdoc
headings tools already understand (`# Errors`, `# Panics`, `# Safety`), and move every
precondition you can into a parameter type.

```rust
/// Stores a message, or returns the stored one if `client_message_id` was seen before.
///
/// On success: inserts one row, updates the room's `last_message_at` and broadcasts to
/// the room's subscribers. A repeated `client_message_id` causes none of these.
///
/// # Errors
/// - [`MessageError::Forbidden`] if the user has no access to the room.
/// - [`MessageError::Database`] if the write fails; nothing is broadcast.
pub async fn create_message(
    &self,
    content: MessageContent, // 1..=10_000 chars, checked when the value was built
    room: RoomId,
    user: UserId,
    client_message_id: Uuid,
) -> Result<Message, MessageError>;
```

- **A precondition a type can carry is not written in prose.** "Content must be 1 to 10,000 characters" became `MessageContent`, and the `InvalidContent` error left this function for the constructor.
- **Document side effects and their order on failure.** "Nothing is broadcast if the write fails" is the line a caller needs and the signature cannot say.
- **Every documented error and effect has a test.** A contract line with no test drifts.
- **Do not restate the signature.** "Takes a room ID and returns a message" adds nothing.
- `# Panics` lists every way the function can panic; the best version of that section is absent because there is none. `# Safety` is mandatory on every `unsafe fn`.

*Use when* the function is public, has side effects, or has failure behaviour a caller must
plan for. *Skip for* private helpers whose name and types say everything.

### Concrete first, abstract on the second use

- Write the concrete type and function first. Introduce a trait, a generic parameter or a builder when a second real implementation or caller exists, or when a test needs a fake at an I/O boundary.
- Use libraries with known behaviour; benchmark a choice only when the operation is on a path with a stated budget.
- Where a timing or memory limit is a requirement, write its test before the implementation (a threshold in a test is a tripwire; the measurement itself belongs in a benchmark).
- One lock guards one invariant. A design that needs two locks held together needs a documented lock order, or a redesign that puts both pieces of state under one lock.

*Use this strictly when* limits are hard and known: constrained memory or CPU, a latency budget,
well-defined concurrent access. *Relax it for* a prototype or exploration, where the aim is to
learn the shape of the problem; say so in the handover so nobody mistakes it for production code.

**Anti-patterns.** A trait with one implementation and no test fake. A generic parameter that
is always the same type. A `Config` option nobody asked for. A plugin system for two fixed cases
(use an enum). Each adds a seam that must be kept working and proves nothing yet.

## Type-level techniques

Stronger tools. Each costs readability and compile-error quality, so each needs a reason.

**Typestate, for a protocol that is wrong when used out of order.**

```rust
pub struct Request<State> {
    parts: Parts,
    _state: PhantomData<State>,
}
pub struct NoBody;
pub struct HasBody;

impl Request<NoBody> {
    pub fn body(self, bytes: Vec<u8>) -> Request<HasBody> { /* ... */ }
}
impl Request<HasBody> {
    pub fn send(self) -> Result<Response, SendError> { /* ... */ }
}
```

- `send` does not exist on `Request<NoBody>`, so the mistake is a compile error, and consuming `self` stops the old state being reused.
- *Use for* builders with required steps, connections (connected, authenticated), transactions, and resources that must be finalised.
- *Skip when* the state is chosen at run time (then it is an enum and a `match`), when there are more than a handful of states (the types multiply), or when the object must be stored in a collection with others in different states.
- **A must-complete object can carry a drop bomb:** `Drop` does `debug_assert!` that it was finished or explicitly abandoned. Keep it to debug builds, and never panic in `Drop` while already unwinding (check `std::thread::panicking()`), or the process aborts.

**Phantom-typed handles bind a name to its types.**

```rust
pub struct Table<K, V> {
    name: &'static str,
    _types: PhantomData<fn() -> (K, V)>,
}

impl<K, V> Table<K, V> {
    pub const fn new(name: &'static str) -> Self {
        assert!(!name.is_empty());
        Self { name, _types: PhantomData }
    }
}

pub const USERS: Table<u64, String> = Table::new("users");
```

- Code passes `USERS`, never the string `"users"`, so the key and value types cannot be mismatched at a call site.
- `PhantomData<fn() -> T>` says "produces `T`, owns none": the handle stays `Send`, `Sync` and `Copy` regardless of `T`, and drop-check is not affected. `PhantomData<T>` claims ownership of a `T`, which is rarely what a handle means. For a handle whose parameter must not be coerced at all (invariance), use `PhantomData<fn(T) -> T>`.
- *Not for* schemas defined by users at run time; those need validation, not types.

**Queries as a typed tree, not a string.**

```rust
pub enum Query {
    AllVertices,
    Edges(EdgeQuery),
    Pipe(Box<Query>, Direction),
    Count(Box<Query>),
}
```

- Callers compose values; an invalid composition fails at construction; execution is one interpreter with an exhaustive `match`. There is no injection, because there is no string.
- *Not when* users need an open textual language. Then parse the text into this tree and keep the rest.

## Boundary types

**Normalise once at a security boundary.** Parse and normalise into a named type; every policy
check, comparison and audit line then uses that type, never the raw string. Two code paths
that normalise differently are how allow-lists get bypassed.

```rust
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct Host(String);

impl Host {
    pub fn parse(input: &str) -> Result<Self, HostError> {
        let normalised = normalise_host(input)?; // lower-case, strip trailing dot, unbracket IPv6
        if normalised.is_empty() {
            return Err(HostError::Empty);
        }
        Ok(Self(normalised))
    }
}

pub enum NetworkDecision {
    Allow,
    Deny { reason: DenyReason, source: PolicySource },
}
```

- A denial carries its reason and which rule produced it. "Denied" alone cannot be debugged or audited.
- Keep the raw input beside the parsed value only when diagnostics need it, and never compare on it.
- Write the tests for odd inputs first: bracketed IPv6, a trailing dot, an embedded port, mixed case, an internationalised name, a wildcard, the empty string.
- The same rule applies to paths (canonicalise, then check the root), URLs and identifiers used in access checks.

**Capability arguments for dangerous operations.** Running a process, opening the network,
writing outside a root: require a token in the signature that only trusted code can create.

```rust
pub struct ExecCap(()); // private field: constructed only in one trusted module

pub fn run_tool(_cap: &ExecCap, program: &Path, args: &[OsString]) -> io::Result<Output> {
    std::process::Command::new(program).args(args).output()
}
```

- The signature now shows which functions can spawn processes, and a reviewer can follow the token.
- **Back it with a lint, or it is only a convention.** In `clippy.toml`: `disallowed-methods = ["std::process::Command::new", "std::env::set_var"]`, with `#[allow]` in the wrapper module alone.
- This is a tool for auditability inside one code base. It is not a sandbox: it does not constrain dependencies or unsafe code.
- *Skip when* the program is small enough that the dangerous calls are all visible in one file.

**Opaque text offsets and ranges.** Parsers, editors and diagnostics pass a named offset and
range, never a bare `usize`.

```rust
#[derive(Clone, Copy, Default, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct TextSize(u32); // a byte offset

#[derive(Clone, Copy, PartialEq, Eq, Hash)]
pub struct TextRange {
    start: TextSize,
    end: TextSize, // private: the constructor checks start <= end
}
```

- `u32` halves the size of every span and caps a file at 4 GiB, so conversion from `usize` is `TryFrom`, not `as`.
- Offsets into `str` must fall on character boundaries; slicing at any other offset panics. Check with `is_char_boundary` wherever an offset arrives from outside.

**Unit-bearing values are parsed once, at the edge.** Sizes such as `10MB`, durations, rates
and percentages become a domain type in the argument parser (a `clap` `value_parser` returning
`ByteSize` or `Duration`); nothing downstream parses units again.

- State the suffix policy: `KB` is 10^3 and `KiB` is 2^10, or say which you chose.
- An unknown suffix is an error that quotes the input. Multiplication is checked for overflow.
- Test a bare number, each suffix, upper and lower case, a fractional value, a negative value and rubbish.

**A join states what was missing.** A view that joins stored records with live state marks
each joined part: `enum Joined<T> { Present(T), Missing }`, or simply `Option<T>` with a
documented meaning. Never a `bool` beside an `Option`; the two can disagree.

## Builders

Use a builder when construction has many optional settings, or when validity depends on
several fields together. For two or three required fields, a `new` function is clearer.

```rust
pub struct ServerBuilder {
    addr: SocketAddr,
    workers: Option<usize>,
    tls: Option<TlsConfig>,
}

impl ServerBuilder {
    pub fn new(addr: SocketAddr) -> Self {
        Self { addr, workers: None, tls: None }
    }
    #[must_use]
    pub fn workers(mut self, workers: usize) -> Self {
        self.workers = Some(workers);
        self
    }
    pub fn build(self) -> Result<Server, BuildError> {
        let workers = self.workers.unwrap_or_else(default_workers);
        if workers == 0 {
            return Err(BuildError::ZeroWorkers);
        }
        Ok(Server { addr: self.addr, workers, tls: self.tls })
    }
}
```

- **Required inputs go in `new`; options go in setters.** A builder whose `build()` fails because a required field was never set has moved a compile error to run time.
- **`build()` is the one validation boundary.** It rejects incompatible combinations with an error naming both options. Tests call `build()`; they do not inspect the builder's fields.
- **Defaults are applied in one place** (`build` or `Default`), and documented.
- Consuming setters (`self -> Self`) chain cleanly; `&mut self -> &mut Self` suits builders configured in loops or conditionals. Pick one per builder.
- **A deferred error keeps the chain intact.** A setter that can fail may record the first error in the builder and return `self`; `build()` starts by returning it. *Not when* the caller needs to react at the failing call.
- **A builder that tracks a "current" item** (the current group, the current subject) documents which methods set and reset it, and returns an error when a method needs context that is absent.
- A new option touches the field, the setter, the default, the validation and a test, together.
- Use typestate only when a step is required *and* must come in order; otherwise it is weight without benefit.
- **Make a choice visible at the call site.** When an argument affects correctness or layout (row-major or column-major, inclusive or exclusive), take a small named type, not a tuple or `true`.

## Smaller API rules

- **Lazy values are `#[must_use]`** with a message saying they do nothing until consumed. So are builders and guards. `Result` already is.
- **Commands as data.** For a protocol with many commands, write one descriptor per command (its code, how to encode the request, how to decode the response) and one generic executor. A new command is a descriptor and a round-trip test, not new transport code.
- **Variants as a table of typed specs.** When variants differ only in data (names, extensions, flags), keep one table and a generic engine. Move a variant into code only when its control flow really differs.
- **A validated resource issues its children.** A checked directory, session or connection hands out child handles through its own methods; callers do not open things beside it.
- **Extension points are explicit.** A hook is registered by name and type, never inferred from a naming pattern. Hook order is part of the contract: document and test it. A plugin gets a registry narrowed to its own namespace.
- **Selection is not traversal.** A selector value (all, one, a range, neighbours) describes a subset without the data; a method applies it to a collection and returns an iterator. Common selections then allocate nothing.
- **An extension trait separates required from optional.** A few required methods; the rest have default implementations in terms of them, which an implementer may override for speed. Test that an override agrees with the default.
- **A mutating business action is one unit:** validate, run in one transaction, fail with a typed error. Transport handlers stay thin. Do not turn every helper into a command object.
- **A deep deserialisation error reads as a path** from root to leaf (`serde_path_to_error`). Bound the size of any input fragment quoted in a message.
- **A small language is a long-term promise** about syntax and error text. Prefer existing structured selectors; if a DSL is needed, the parser, the printer and a `parse(print(x)) == x` test change together.

## Traits

- **Object safety (dyn compatibility) is a design decision made early.** A trait is usable as `dyn Trait` only if its methods take `&self`, `&mut self`, `Box<Self>`, `Rc<Self>`, `Arc<Self>` or `Pin<..>`, have no generic type parameters, and do not return `Self`. Keep a method off the trait object, and the trait usable, with `where Self: Sized`:

```rust
pub trait Shape {
    fn area(&self) -> f64;

    fn scaled(self, factor: f64) -> Self
    where
        Self: Sized;
}
```

  Add a test that names `dyn Shape` (`fn _assert(_: &dyn Shape) {}`), so a later method cannot silently break it.
- **Async methods in traits.** `async fn` in a trait works with generics and static dispatch, but the trait is then not usable as `dyn`, and the returned future's `Send`-ness cannot be named by callers. For a `dyn` trait, return `Pin<Box<dyn Future<Output = T> + Send + '_>>` by hand or through `async-trait`; the cost is one allocation per call, which is negligible beside I/O. In a public trait whose futures must be `Send`, write `fn f(&self) -> impl Future<Output = T> + Send`.
- **Seal a trait you are not ready to let others implement.** Then adding a method is not a breaking change.

```rust
mod private {
    pub trait Sealed {}
}
pub trait Format: private::Sealed {
    fn name(&self) -> &'static str;
}
```

  Document that it is sealed. *Do not seal* a trait that exists to be an extension point.
- **Coherence.** Either the trait or the type must be local. Extend a foreign type with an extension trait; implement a foreign trait for a foreign type through a newtype. A blanket `impl<T: Other> Mine for T` prevents you and everyone else from writing any other overlapping impl later: add one only when it is the whole story.
- **Higher-ranked bounds for callbacks that borrow.** `F: for<'a> Fn(&'a Row) -> &'a str` says the callback works for any lifetime. Elision usually writes this for you in `Fn(&Row) -> &str`. Do not demand `'static` from a callback that is only called before the function returns.
- **Generic associated types for lending.** When an associated type must borrow from `self` (a lending iterator, a cursor over a buffer), a GAT (`type Item<'a> where Self: 'a;`) expresses it without allocation. It also makes the trait harder to use and not `dyn`-compatible. Reach for it when returning owned items is measurably too slow, not before.
- **Trait-object lifetimes default to `'static` in a `Box`.** `Box<dyn Trait>` means `Box<dyn Trait + 'static>`. To box something that borrows, write `Box<dyn Trait + 'a>`. The error "borrowed value does not live long enough" on a boxed closure is often this.
- **Lifetime elision** covers one input reference, or `&self`. With two input references and a returned reference, write the lifetimes; that is the place to decide which input the output borrows from.
- **Upcasting** from `&dyn Sub` to `&dyn Super` works directly on recent toolchains (1.86 and later). Older code needs an `as_super(&self) -> &dyn Super` method; check the project's minimum supported version before removing one.
- **No specialisation in library code.** It is unstable and its soundness questions are open. Design the trait explicitly, or dispatch on an enum.
- **`where` clauses** take bounds that do not fit on the signature line.
- **A crate `prelude` is for traits users must import to call methods,** plus a few ubiquitous types. Keep it small; a glob import that brings in fifty names causes collisions.
- **`NonZero`, zero-sized and uninhabited types** when they are the honest model: `Option<NonZeroU32>` for an ID where zero means absent (and it is the size of a `u32`); a zero-sized marker for compile-time state; `Infallible` for an error that cannot occur. Use them because the model is clearer, not because the layout is clever.
- **Edition 2024** changes how `ref` and `mut` interact with default binding modes in patterns, among other things. Migrate with `cargo fix --edition` and read the diff; do not hand-edit patterns in bulk.

### Traits as seams

**Absent behaviour is an implementation, not an `Option`.** "No hook installed" is a no-op
implementation, so call sites do not branch.

```rust
pub trait RegistryHooks: Send + Sync {
    fn on_manifest_uploaded(&self, _reference: &ManifestRef) {}
    fn on_blob_deleted(&self, _digest: &Digest) {}
}

impl RegistryHooks for () {}

let hooks: Box<dyn RegistryHooks> = builder.hooks.take().unwrap_or_else(|| Box::new(()));
```

- Default method bodies mean a new hook does not break existing implementers.
- Document where each hook is called, in what order, and whether its failure is ignored or aborts the operation.
- **A silent no-op hides missing wiring,** so the wiring itself has a test: install a recording hook and assert it was called.
- *Not for* a step that must be confirmed, retried or rolled back with the core operation. That is part of the operation, not a hook.
- With many optional callbacks and one author composing a few, a builder holding one boxed closure per hook is lighter than a trait. With one required callback, a trait is clearer.

**A family of related types goes through associated types tied back to `Self`,** so the
handles and events of one back end cannot be mixed with another's.

```rust
pub trait Runtime: Sized + 'static {
    type Handle: RuntimeHandle<Runtime = Self>;
    type Window: WindowDispatch<Runtime = Self>;

    fn new(args: InitArgs) -> Result<Self, RuntimeError>;
    fn handle(&self) -> Self::Handle;
}
```

- Extending the trait changes the trait, the mock back end and every real back end in the same commit.
- An API heavy in associated types needs a worked example of the common path; the signatures alone are hard to read.
- **One back end does not need the trait.** Add it with the second implementation, or with the mock if tests need one.

**A behavioural trait needs semantic tests.** Implementing the methods does not prove they
agree with each other. Test the laws that relate them: `a == b` implies equal hashes; `len`
equals the number of items iterated; `Ord` is consistent with `Eq`; `decode(encode(x)) == x`.
Write these once as a generic function and run it for every implementer.

**Smaller rules.**

- **A checked constructor's error quotes both sides of the mismatch:** "expected 4 columns, row has 3", not "column count mismatch".
- **A scalar-or-collection argument** is a small trait that reports which it is, not a second copy of every entry point. Keep separate functions when the two differ in meaning, and test collection-collection, collection-scalar and scalar-scalar.
- **Extract and repack.** An API that processes some leaves of a nested container returns the caller's own shape, by splitting the walk into an extract phase and a repack phase.

Define the trait before the adapter when I/O should be kept out of domain logic, when tests
need a fake, or when behaviour should be settled before storage or transport is chosen.

```rust
pub trait EntityStore {
    fn load(&self, id: EntityId) -> Result<Option<StoredEntity>, StoreError>;
}

pub struct EntityService<S> {
    store: S,
}

impl<S: EntityStore> EntityService<S> {
    pub fn describe(&self, id: EntityId) -> Result<String, ServiceError> {
        let entity = self.store.load(id)?.ok_or(ServiceError::NotFound(id))?;
        Ok(entity.summary())
    }
}
```

- **The trait is owned by its consumer and sized to it.** It lists the few operations the service needs, in domain terms (`load`, `save_order`), not the adapter's whole API (`execute_sql`).
- **The error type belongs to the trait,** not to the adapter. `StoreError` does not expose `sqlx::Error`.
- **Generic or `dyn`.** A generic parameter (`S: EntityStore`) costs nothing at run time and suits one implementation per binary. `Arc<dyn EntityStore>` suits a choice made at run time, heterogeneous collections, and stopping a type parameter spreading through every signature. Default to generics inside a library and `dyn` at the application's wiring layer.
- **Async methods.** `async fn` in a trait works with generics but makes the trait unusable as `dyn`, and promises nothing about `Send`. For `dyn` use, return a boxed future or use the `async-trait` crate; for a public trait, write the return type as `impl Future<Output = T> + Send` so spawned callers compile.
- **A fake is a real implementation,** usually an in-memory map, kept in the test support code and run through the same contract tests as the real adapter. A fake that only ever returns `Ok` tests nothing about failure.

*Skip the trait when* there is one implementation, no test needs a fake, and the dependency is
pure (a parser, a formatter, a calculation). Call the function.

**Algorithms over the smallest capability traits.** When a library has several representations
of one concept (graph storage, matrix layouts, byte sources), write each algorithm against the
smallest set of capability traits it needs, and implement those per representation:

```rust
pub fn dijkstra<G, F, K>(graph: G, start: G::NodeId, edge_cost: F) -> HashMap<G::NodeId, K>
where
    G: IntoEdges + Visitable,
    G::NodeId: Eq + Hash,
    F: FnMut(G::EdgeRef) -> K,
    K: Measure + Copy,
```

- Start from the weakest bounds; add a stronger trait only when an operation needs it.
- Each representation passes one shared conformance suite for every capability it claims.
- *Skip when* there is one representation, or the algorithm relies on layout, mutation or complexity guarantees the traits cannot express. The bounds above are hard to read and hard to debug; they must buy real reuse.

**A closed set of variants: one trait, one factory.** When each member of a family (languages,
file formats, back ends) supplies the same handful of operations, give the family one trait
with defaults for optional parts, and build members in one place:

```rust
pub trait Format: Send + Sync {
    fn name(&self) -> &'static str;
    fn extensions(&self) -> &'static [&'static str];
    fn parse(&self, text: &str) -> Result<Document, ParseError>;
    fn imports(&self, _doc: &Document) -> Vec<String> {
        Vec::new() // optional capability: the default says "none"
    }
}

pub fn format_named(name: &str) -> Result<Box<dyn Format>, UnknownFormat> {
    match name {
        "json" => Ok(Box::new(Json)),
        "toml" => Ok(Box::new(Toml)),
        other => Err(UnknownFormat { name: other.to_owned(), supported: &["json", "toml"] }),
    }
}
```

- The pipeline is written once against `dyn Format`; adding a member touches its own file and the factory.
- An unknown name is an error that lists what is supported, not a silent `None`.
- If the members share no behaviour and differ only in data, a table of structs is simpler. If the set is fixed and small and the logic is a `match`, an enum keeps exhaustiveness checking, which a trait object gives up.
- **Plugins loaded at run time** come from an explicit registry or manifest, one coordinator calls their hooks in a stated order, and a plugin that fails to load is reported at startup, never skipped silently.
- **A default method can lie.** An empty default silently drops data for every member that has not implemented the richer method, and nothing fails. When "not supported" and "supported, found nothing" must be told apart, return `Option` from the default or split the capability into its own trait. Every non-default method callers rely on gets a fixture per member.

## Identifiers and conversions

**Many IDs over one primitive: one generic wrapper, one marker per kind.** Shared trait
implementations are written once, and the IDs still cannot be mixed.

```rust
pub struct Id<T> {
    raw: u32,
    _kind: PhantomData<fn() -> T>,
}

impl<T> Clone for Id<T> {
    fn clone(&self) -> Self { *self }
}
impl<T> Copy for Id<T> {}
impl<T> PartialEq for Id<T> {
    fn eq(&self, other: &Self) -> bool { self.raw == other.raw }
}
impl<T> Eq for Id<T> {}

pub struct TableKind;
pub struct JobKind;
pub type TableId = Id<TableKind>;
pub type JobId = Id<JobKind>;
```

- **Write the trait impls by hand, or use `derive-where`.** `#[derive(Clone)]` on `Id<T>` adds `T: Clone`, which the marker types do not satisfy.
- `Debug` should print the kind (`TableId(7)`), or logs are full of bare numbers.
- A handful of IDs is simpler as hand-written or macro-generated newtypes. An ID with its own invariant (a checksum, a format) is always its own type.
- IDs from different instances of the same store are still mixable. If that matters, the handle carries the store's identity too, checked in debug builds.

**Withhold a `From` that would lose context.** If `?` would silently turn a low-level error
into yours while dropping what the caller needs to know, do not implement the conversion.
Provide named constructors that demand the context.

```rust
#[derive(Debug, thiserror::Error)]
pub enum RpcError {
    #[error("{service}: {status}")]
    Status { service: &'static str, status: Box<tonic::Status> },
    #[error(transparent)]
    Internal(#[from] anyhow::Error),
}

// Deliberately no From<tonic::Status>: a status must say which service produced it.
impl RpcError {
    pub fn from_status(service: &'static str, status: tonic::Status) -> Self {
        Self::Status { service, status: Box::new(status) }
    }
}
```

- The call site becomes `.map_err(|s| RpcError::from_status("meta", s))?`: one visible line instead of an invisible lossy one.
- Leave a comment where the impl would be, so nobody "helpfully" adds it.
- Boxing a large payload keeps the error enum, and every `Result` that carries it, small.
- **`let _ = fallible();` needs a comment saying why the error does not matter.** Without one it reads as an oversight, and usually is.

**One exhaustive serialiser per export format.** Writing typed values back into a replayable
text format puts every escaping rule (identifier quoting, string escapes, float precision,
date syntax) behind one `match` with no wildcard arm. A new value type then fails to compile
until its arm exists, and arrives with an export-then-import round-trip test. Formatting
scattered across call sites is how one path forgets to escape.

## Handles, options and dependencies

**A cloneable handle, with a builder per call.** An SDK or client entry point is a small
handle around `Arc`-shared internals: `Clone + Send + Sync`, cheap to clone, every method on
`&self`. Options for one call come from an operation builder that implements `IntoFuture`, so
the plain call stays short.

```rust
let bytes = op.read("hello.txt").await?;

let bytes = op
    .read_with("hello.txt")
    .range(0..8 * 1024 * 1024)
    .concurrent(4)
    .await?;
```

- Callers clone the handle into tasks; they never wrap it in their own `Arc<Mutex<_>>`. If they have to, the handle is wrong.
- Per-call options do not mutate the handle. Settings on the handle are defaults fixed at construction.
- *Skip the per-call builder* when an operation has one or two options; a plain argument or an options struct is enough.

**Dependencies are injected, never read from a hidden global.** A shared cache, credential
source, clock or policy is passed through the constructor or builder, with a default so simple
callers need not supply one.

- Callers can then share one instance across several builds, and tests can substitute it.
- Show the shared-instance path in the example; it is the one callers get wrong.
- `build` may return the product together with its diagnostics (`(Image, BuildReport)`), so callers need no second call to learn what happened.

**A callback in an options struct: decide what `Clone` and `Debug` do.**

```rust
#[derive(Clone)]
pub struct PushOptions {
    pub retries: u32,
    pub on_progress: Option<Arc<dyn Fn(Progress) + Send + Sync>>,
}

impl fmt::Debug for PushOptions {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("PushOptions")
            .field("retries", &self.retries)
            .field("on_progress", &self.on_progress.is_some())
            .finish()
    }
}
```

- `Arc<dyn Fn>` makes the clone carry the callback, which is what a reader of `.clone()` expects. A hand-written `Clone` that silently drops a field is a trap; if a callback must not be shared, do not implement `Clone`.
- `Debug` says whether a callback is present and prints nothing of it.
- Say on which thread or task the callback runs, and that it must not block.

**Raw and resolved paths are different types.** Untrusted path input is one type; a
canonical path known to be inside an allowed root is another. One resolver, built from an
explicit base directory, converts the first into the second.

```rust
pub struct ResolvedPath(PathBuf);

impl Resolver {
    pub fn resolve(&self, raw: &RawPath) -> Result<ResolvedPath, PathError> {
        let joined = self.base.join(raw.as_path());
        let canonical = joined.canonicalize().map_err(PathError::Io)?;
        if !canonical.starts_with(&self.base) {
            return Err(PathError::OutsideBase);
        }
        Ok(ResolvedPath(canonical))
    }
}
```

- Never join a user-supplied path onto a root and open it. `..`, an absolute path (which replaces the base in `join`) and a symlink all escape.
- `canonicalize` needs the path to exist and follows symlinks; the base must itself be canonical. For a file about to be created, canonicalise the parent and validate the final component separately.
- A check followed by an open is a race if someone else can modify the directory. Where that matters, open relative to a directory handle (`cap-std`, `openat`) instead of checking a string.
- Case sensitivity, symlinks and prefixes differ by platform; test each supported one.

## State, transitions and atomic change

**A multi-step change that must not be half-done is a typestate transaction.** For a
multi-file edit, a migration or a generated patch, where a wrong call order corrupts user
data, each irreversible phase is a type and each transition consumes `self`.

```rust
pub struct Pending;
pub struct Staged;
pub struct Applied;

pub struct Transaction<State = Pending> {
    root: PathBuf,
    edits: Vec<ValidatedEdit>,
    backups: Option<BackupSet>,
    _state: PhantomData<State>,
}

impl Transaction<Pending> {
    pub fn stage(self) -> Result<Transaction<Staged>, BatchError> { /* ... */ }
}
impl Transaction<Staged> {
    pub fn apply(self) -> Result<Transaction<Applied>, BatchError> { /* ... */ }
}
impl Transaction<Applied> {
    pub fn commit(self) -> Result<Report, BatchError> { /* ... */ }
    pub fn rollback(self) -> Result<(), BatchError> { /* ... */ }
}
```

- Committing before applying does not compile. Inputs are already validated types.
- Decide what happens when an `Applied` transaction is dropped without commit or rollback: roll back in `Drop` on a best-effort basis and log, since `Drop` cannot return the error.
- For a single file, write a temporary file in the same directory and rename it over the target. That is atomic and needs no machinery.

**Apply a group of options atomically.** An update of several settings never leaves the
object half-changed. Build the next value and swap:

```rust
let mut next = self.clone();
next.apply(&options)?;
*self = next;
```

- If cloning is too expensive, validate everything first and mutate only after nothing can fail.
- Options with irreversible side effects (opening a port, deleting a file) are validated with the rest and performed last.

**Every status write goes through one setter that consults the transition table.**

```rust
impl Job {
    pub fn transition(&mut self, next: Status) -> Result<(), IllegalTransition> {
        if !self.status.can_become(next) {
            return Err(IllegalTransition { from: self.status, to: next });
        }
        self.status = next;
        Ok(())
    }
}
```

- The field is private; nothing assigns it directly. The table is one `match` on `(from, to)`.
- Adding a status changes the table first, then every handler that enters or leaves it.
- Do not add a second stored status when the state can be derived from data already held; two sources will disagree.

**Publish an immutable result from a mutable builder.** Analysis that needs mutable working
state keeps it inside the builder and publishes through `finish(self) -> Catalog`. Consuming
the builder means nothing can change after publication, and the result can be shared in an
`Arc` without locks. Callers that need live updates get an explicit session type instead.

**Protocol state that is not concurrent says so in its type.** A cursor, session, transaction
or result stream with hidden protocol state has `&mut self` methods and is neither `Clone` nor
`Sync`, so interleaved use does not compile. Where sharing is forced on you (a foreign handle),
a guard fails loudly on a second concurrent entry (`try_lock`, then an error) instead of
interleaving silently.

**Read and write entry points can be separate types.** A marker parameter such as
`Batch<Read>` and `Batch<Write>` makes a write inside a read batch a compile error. Worth it
when the distinction has consequences (a read replica, a read-only transaction); otherwise a
run-time check is simpler.

**Preflight checks cannot be skipped when the context is only reachable through them.** When
one operation is shared by several entry points with different checks, the shared helper does
not take the raw context. It takes a provider that hands the context out only after running
that entry point's checks.

```rust
pub trait CheckedAccess {
    async fn checked(&self, request: &Request, auth: &Auth) -> Result<&Store, AccessError>;
}
```

- The provider is chosen at the API boundary, never inside the helper.
- The bypass implementation has an alarming name (`UncheckedAccess`) and does not appear in a public handler. A search for the name is then an audit.
- If the check changes what the operation means, it is two operations.

**Smaller rules.**

- **A heuristic score explains itself:** the number, its named factor contributions and the inputs that were missing. A missing signal is reported as missing, never replaced with a default that looks like data. Weights are a struct with `Default`. Do not let such a score trigger an irreversible action unattended.
- **A writer finalised in `Drop` flushes when the temporary dies,** which is the end of the statement unless it is bound to a name. Errors in `Drop` are lost, so offer an explicit `finish()` for callers who need them.
- **A replayable view is a list of immutable snapshots and an index.** One pure function computes the steps; previous, next and reset only move the index. For long runs, keep a window or compute lazily.
- **Configuration round-trips.** A type rebuilt from its configuration stores the declared values verbatim and derives the rest in a build step. A test rebuilds, reads the configuration back and compares.

## Callbacks and sinks

**Push events to a caller-defined sink when the traversal is complex.** The traversal strategy
(search, scan, parse) stays internal; the caller supplies what to do with each event.

```rust
pub trait Sink {
    type Error;

    /// Return `Ok(false)` to stop early.
    fn matched(&mut self, mat: &Match<'_>) -> Result<bool, Self::Error>;

    fn context(&mut self, _line: &Context<'_>) -> Result<bool, Self::Error> {
        Ok(true)
    }

    fn finish(&mut self, _summary: &Summary) -> Result<(), Self::Error> {
        Ok(())
    }
}
```

- One required method; the rest default, so a simple sink is a few lines.
- The sink borrows event data for the call (`Match<'_>`), so the traversal can reuse its buffers and nothing is allocated per event. A sink that needs to keep data copies it.
- State the contract: `finish` is called exactly once, including after an early stop, and not after an error.
- *Prefer an iterator* when the traversal is simple enough to be one. Iterators compose and the caller keeps control. A sink is for when borrowing rules or internal buffering make an iterator awkward or slow.
- An enum for the return (`ControlFlow<()>`) reads better than a `bool` whose meaning has to be remembered.

## Error surfaces for callers

**Answer the caller's question with a method.** Callers want to know "was it not found?",
"should I retry?", "can I fall back?". Give them `is_*` methods, so they never match on
message text or on a dependency's error type.

```rust
impl Error {
    pub fn is_not_found(&self) -> bool {
        match self {
            Error::Pull { source: Some(source), .. } => source
                .downcast_ref::<RegistryError>()
                .is_some_and(RegistryError::is_not_found),
            _ => false,
        }
    }
}
```

- The dependency's error stays a boxed `#[source]`, out of your public API, so upgrading the dependency is not a breaking change for your callers.
- A probe built on `downcast_ref` breaks silently if the dependency changes its error type. Keep each probe small and cover it with a test that produces the real error.

**An API client's error carries what recovery needs as fields:** the HTTP status, the parsed
`Retry-After` delay, and the rate-limit limit, remaining count and reset time. Callers never
scrape strings. An empty or non-JSON error body still produces a sensible message that
includes the status. Rate-limit state is kept per credential, not in one global.

**Absent, unsupported and failed are three outcomes.** An optional converter, accelerator or
plugin lookup says which happened, and the fallback is a visible decision.

```rust
pub enum Conversion<T> {
    Converted(T),
    NoConverter,
    Unsupported(Reason),
    Failed(Error),
}
```

- Collapsing the last three into `None` hides real failures behind a silent fallback. If a fallback is taken, log or count the reason.
- A mandatory transformation's failure is an error, never a fallback.

**A plugin-facing error is a small stable type.** An extension trait returns a public error
with the few variants an extension can act on (a timeout with its duration, invalid input) and
an opaque `Other` for the rest. One `From<InternalError>` does the mapping, so internal errors
can change freely. *Not when* callers need the full internal error as a contract.

**Diagnostics that accumulate context.** In compilers, linters and language servers, an error
gains a file path, span, category and severity as it travels up. Build that into the error
type (`error.with_file_path(path).with_span(span)`), each call wrapping and keeping the
source, and decide at each `?` whether this layer knows something worth adding. The rendered
result still has one clear primary message. A plain internal error enum does not need this.

**Scoped panic context, for debugging only.** A thread-local stack of "what I am doing"
frames, printed by a panic hook installed once, turns a bare panic into one with a story.

```rust
let _ctx = panic_context::enter(format!("request: {method}"));
```

- The guard pops its frame on drop; `let _ = ...` would drop it at once.
- It is thread-local, so it does not follow an async task that moves between threads. There, use `tracing` spans.
- It explains crashes. It is not error handling and must not replace a `Result`.

## Features, macros and targets

- **Features are additive.** Enabling a feature never removes or changes existing API, and no two features are mutually exclusive, because Cargo unifies features across the whole dependency graph and some crate will enable both. For a real either-or (two TLS back ends), pick a documented precedence or fail with `compile_error!` that names both.
- Name features for what they add (`serde`, `tokio`), without `use-`, `with-` or `no-` prefixes. `default` features are a compatibility surface: removing one is a breaking change.
- **Macro hygiene.** A macro bug repeats at every expansion. In `macro_rules!`, use `$crate::` paths. In a procedural macro, emit absolute paths (`::core::option::Option`), never rely on the caller's imports, and report user errors with `syn::Error` at the offending span, not with a panic.
- **Prefer a function, then a generic, then `macro_rules!`, then a procedural macro.** Each step costs compile time, tooling support and readability of errors.
- **Native and WebAssembly bounds behind local aliases.** A library for both targets defines a few traits once per target (`MaybeSend`: `Send` on native, nothing on wasm) and uses those, never a bare `Send`. Build both targets in CI before any bound changes.
- **One wrapper around the HTTP request builder,** so hooks, authentication, timeouts and target-specific execution apply to every request. Call sites never reach the underlying client.
- **External tools share one lifecycle trait** (minimum version, install, update, instructions) and one logging command runner. Check the version again after an automatic update, and remember that command transcripts can contain environment values.
- **Optional dependencies use `dep:`,** so the feature name is yours and the dependency does not create an implicit feature. Each feature has a line of documentation saying what it adds.

```toml
[features]
default = []
serde = ["dep:serde"]

[dependencies]
serde = { version = "1", optional = true, features = ["derive"] }
```

- **Test the feature combinations you support:** none, default, all, and each alone (`cargo hack --each-feature check`). Code behind a feature CI never enables rots.

### More type details

- **An associated type when the implementer fixes the answer; a generic parameter when the caller chooses.** `Iterator::Item` is associated: one iterator has one item type. `From<T>` is generic: one type converts from many. Choosing wrongly shows up as ambiguity errors or as impls you cannot write.
- **An empty enum models "cannot happen" in a generic position.** Prefer `std::convert::Infallible` to a home-made `Void`. A `Result<T, Infallible>` is unwrapped without a panic path:

```rust
fn into_ok<T>(result: Result<T, Infallible>) -> T {
    match result {
        Ok(value) => value,
        Err(never) => match never {},
    }
}
```

  Never pass an uninhabited type across FFI.
- **`..` in a pattern is a decision about future fields.** Destructuring your own struct *without* `..` makes the compiler stop you when a field is added, which is what you want in `Hash`, `PartialEq`, serialisation and anything else that must consider every field. Use `..` when the code truly does not care about the others, and you must use it for `#[non_exhaustive]` types from other crates.

```rust
impl PartialEq for Account {
    fn eq(&self, other: &Self) -> bool {
        let Self { id, email, cached_score: _ } = self; // a new field fails to compile here
        *id == other.id && *email == other.email
    }
}
```

- **Seal a trait that vouches for a representation.** A trait promising layout, a wire format, zero-copy casting or FFI safety must not be implementable outside the crate, because unsafe code relies on every implementer being correct. If outsiders must implement it, make it an `unsafe trait` with the obligations written down.

```rust
mod private {
    pub trait Sealed {}
}
pub trait NativeType: Copy + Send + Sync + private::Sealed + 'static {}

impl private::Sealed for u32 {}
impl NativeType for u32 {}
```

### Macros and build scripts

**Choosing.** A derive generates impls from a type's structure. An attribute macro wraps or
rewrites an item. A function-like macro is for syntax a function cannot take: variadic
arguments, a small DSL, compile-time checks of a literal. If a function or a generic does the
job, write that.

**`macro_rules!`.**

```rust
#[macro_export]
macro_rules! hashmap {
    ($($key:expr => $value:expr),* $(,)?) => {{
        let mut map = ::std::collections::HashMap::new();
        $( map.insert($key, $value); )*
        map
    }};
}
```

- Absolute paths (`::std::`, `$crate::`) so the expansion does not depend on the caller's imports. Accept a trailing comma.
- Each `$x:expr` is evaluated where it is written: once if used once, twice if used twice. Bind it to a `let` in the expansion if it appears more than once.
- Use the narrowest fragment specifier that works (`ident`, `ty`, `expr`, `path`); `tt` is the escape hatch. Keep matchers simple; a recursive muncher has a recursion limit and awful errors.
- Test the expansion like any API, including a compile-fail case for misuse. `cargo expand` shows what it produces.

**Procedural macros.**

- Parse with `syn`, generate with `quote!`, and put the logic in a function over `proc_macro2::TokenStream` so it can be unit-tested without a compiler. Never build code by string concatenation.
- **A user error is a `syn::Error` at the offending span,** returned as `to_compile_error()`. A panic in a macro gives the user a message with no location. Collect several errors and report them together where possible.
- A procedural macro runs arbitrary code at build time with the developer's privileges, and adds `syn` to everyone's compile. Keep it small and deterministic: no network, no clock, no reading files outside the crate without telling Cargo.
- Generated code that users will see in errors should be as plain as hand-written code.

**Build scripts.**

```rust
// build.rs
use std::{env, fs, path::PathBuf};

fn main() {
    println!("cargo::rerun-if-changed=schema/api.json");
    println!("cargo::rerun-if-env-changed=API_SCHEMA_STRICT");

    let out = PathBuf::from(env::var_os("OUT_DIR").expect("set by Cargo"));
    let code = generate_from(&fs::read_to_string("schema/api.json").expect("read schema"));
    fs::write(out.join("api.rs"), code).expect("write generated code");
}
```

```rust
// lib.rs
include!(concat!(env!("OUT_DIR"), "/api.rs"));
```

- **Write only under `OUT_DIR`.** A build script that edits the source tree breaks read-only checkouts, vendoring and reproducibility.
- **Declare every input.** Without any `rerun-if` line the script re-runs on every change to the package; with one, it runs only when a listed input changes, so a forgotten input means stale output.
- Output is deterministic: sort what you iterate, embed no timestamps.
- `expect` with a message is acceptable here; a panic is how a build script reports failure. Make the message say what to fix.
- The `cargo::` prefix needs Cargo 1.77 or later; older toolchains use `cargo:`. Check the project's minimum supported version.
- A custom `cfg` set by the script is declared with `cargo::rustc-check-cfg=cfg(has_foo)`, or every use warns.
- Linking: `cargo::rustc-link-lib` and `cargo::rustc-link-search`. A crate that links a native library sets `links = "name"` in its manifest so two versions cannot both be linked.
- **Prefer checked-in generated code plus a test that it is current** when the generator is slow, needs tools users may lack, or the output is worth reviewing in diffs.
- A procedural-macro crate sets `proc-macro = true` under `[lib]` and can export nothing else, so the runtime types it refers to live in a sibling crate that re-exports the macro.

### Procedural macros in practice

**Parse a macro's own syntax into a typed input, apart from code generation.**

```rust
mod kw {
    syn::custom_keyword!(accessors);
}

pub struct MacroInput {
    pub name: Ident,
    pub fields: Punctuated<Field, Token![,]>,
}

impl Parse for MacroInput {
    fn parse(input: ParseStream) -> syn::Result<Self> {
        input.parse::<kw::accessors>()?;
        input.parse::<Token![=]>()?;
        let name: Ident = input.parse()?;
        input.parse::<Token![,]>()?;

        let body;
        braced!(body in input);
        let fields = body.parse_terminated(Field::parse_named, Token![,])?;
        Ok(Self { name, fields })
    }
}
```

- Keywords are `custom_keyword!` types matched with `parse` or `lookahead.peek`, never identifier strings compared by hand. A `Lookahead1` error lists what was expected for free.
- The pipeline is parse, then validate into a model, then generate. Generation never sees raw tokens, and each stage is tested alone.

**The expansion is an ordinary function.** `fn expand(input: TokenStream2) -> syn::Result<TokenStream2>`
holds the logic; the `#[proc_macro]` entry point only converts types and turns an error into
`to_compile_error()`.

- Tests call `expand`, parse the result with `syn::parse2::<syn::File>` and assert on the items. That proves the output is at least syntactically Rust.
- For reading, print it with `prettyplease`, or run `cargo expand`. Text comparisons of pretty-printed output are smoke checks; the meaning is carried by tests that compile and run the generated code, and by compile-fail tests for misuse.

**A derive states what it accepts and rejects the rest.** One that maps a struct onto a
storage schema takes structs with named fields only, emits per-field code in declaration
order (so column order equals source order), and gives every other input a `compile_error!`
at its span. Compile-fail tests cover enums, tuple structs and unions; a round-trip test
asserts the order. Reordering fields is then a schema change, which the docs must say.

## Modules, crate roots and documentation

- **A module has one reason to exist** and a name that states it. `utils`, `common` and `misc` are where unrelated code goes to be forgotten.
- **Name what the crate root exports.** Write named re-exports (`pub use counter::{LineStats, count_file};`), so the public API is readable in one place and an internal addition cannot leak. A glob re-export is acceptable only for a deliberate prelude.
- **Default to private.** `pub(crate)` for what the crate shares internally; `pub` is a promise.
- **Binary orchestration is not library API.** Argument handling and the main flow live in the binary or in private modules. `main.rs` parses, calls the library and maps the result to an exit code.
- **One module per subcommand** in a CLI, under `commands/`, with the parent module only declaring them.
- Split a file when it holds two things that change for different reasons, not at a line count.
- **Document the contract, not the implementation:** what it does, what it returns, when it errors (`# Errors`), when it panics (`# Panics`), what the caller must uphold (`# Safety`).
- **Comments say why.** The code already says what. A comment that restates the next line will drift from it.
- **Documentation is checked like code.** Examples are doctests, and `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps` fails on a broken intra-doc link. Libraries set `#![warn(missing_docs)]`.
- **Crate docs open with one complete example** of the main use. Mark it `no_run` when it needs a real service, and hide a `fn main() -> Result<..>` wrapper so `?` works.
- **A shipped example is a complete program:** `fn main() -> Result<(), Error>`, inputs from arguments, usage printed when one is missing.
- **A hand-written parser carries its grammar in the module doc,** and states what the module does not check.
- **Field comments give meaning, unit and format.** An analogy is not a definition.
- **Docs do not describe code that is not there.** A doc naming a crate the module no longer uses is drift; fix it in the same change as the code.
- **A workaround cites its issue.** A bound, attribute or pin that exists because of an upstream limitation carries the reference, so it can be removed later.
- **Each stable error code has a page:** what happened, usual causes, the fix. The message prints the code.
- **A shared data file opens with a legend and provenance:** every field defined, and the date and source it was synced from.
- **Diagrams follow the project's convention.** Where Mermaid is used: one statement per line, direction in the header. Do not add a diagram format the repository does not already use.
- **Never log or document secrets or sensitive payloads,** including in examples.

**Decision records** are for choices that are expensive to reverse: a foundational
dependency, a storage format, a public protocol.

- State the problem, the options considered, the choice, what was rejected and why, and **what the choice costs**.
- Give it a status: draft, accepted, superseded.
- **Say how it could be reversed:** the assumptions, the signal that would show one is wrong, and the migration in bounded steps.
- *Not for* decisions that a later commit can undo cheaply. A record for every choice is noise.
- **Judge a module by its depth.** A module's interface is everything a caller must know: signatures, invariants, ordering rules, errors, configuration and performance. A deep module hides a lot of behaviour behind a small interface. *Deletion test:* if deleting the module would push the same complexity into every caller, it earns its place; if the complexity simply disappears, it was a pass-through.
- **A seam needs two adapters.** Put a trait where behaviour really varies: several back ends, or a production and a test implementation. A trait with one implementation and no test double is not a seam yet; it is an indirection.
- **Semantics belong to the interface.** If correctness depends on conflict rules, scan order, write ordering or atomicity, the trait's documentation states them and each adapter either implements them or returns an explicit unsupported error. A contract suite checks it.
- **One required method, many provided.** When many wrapper types share operations, the trait requires one accessor to the core and supplies the rest as default methods.
- **Plugin seams are object-safe.** A trait called through `dyn` has no generic methods and no `Self` by value; generic conveniences live in an extension trait or a builder. Publish one implementation-independent test suite that every adapter runs.
- **Back ends advertise what they support.** Default bodies return an explicit unsupported error, capability flags say which are real, and a conformance test checks the flags against the behaviour.

### Documentation that is checked

Every public item that can fail, panic or be misused says so. An undocumented panic or unsafe
precondition is a defect.

```rust
/// Parses a port from text.
///
/// # Errors
/// Returns [`PortError::NotANumber`] if `text` is not a decimal integer, and
/// [`PortError::OutOfRange`] if it is zero or above 65535.
///
/// # Examples
/// ```
/// # use my_crate::parse_port;
/// assert_eq!(parse_port("8080")?.get(), 8080);
/// assert!(parse_port("0").is_err());
/// # Ok::<(), my_crate::PortError>(())
/// ```
pub fn parse_port(text: &str) -> Result<Port, PortError> { /* ... */ }
```

- `# Errors` names the variants and their conditions; "returns an error if something goes wrong" documents nothing. `# Panics` lists every condition, or the function does not panic. `# Safety` on an `unsafe fn` lists what the caller must guarantee.
- A doctest asserts something. An example that only calls the function checks that it compiles and nothing else.
- Show the error case in the example when the error is part of what a caller must handle.
- Keep doctests small; each is compiled as its own crate, so hundreds of them slow the suite. Long scenarios belong in `tests/`.
- Use `no_run` for examples that need a network or a device (still compiled), and avoid `ignore`, which checks nothing.
- In compile-fail tests, do not depend on exact compiler wording more than the tool forces you to; the message changes between releases.

## Tests a library needs

**Doctest.** The hidden last line lets the example use `?`.

```rust
/// ```
/// # use my_crate::{UserId, UserIdError};
/// let user_id = UserId::try_from("user_123")?;
/// assert_eq!(user_id.as_str(), "user_123");
/// # Ok::<(), UserIdError>(())
/// ```
```

**Compile-fail.** Each file under `tests/ui/` is one misuse, with its expected error beside it.

```rust
#[test]
fn req_003_misuse_does_not_compile() {
    let cases = trybuild::TestCases::new();
    cases.compile_fail("tests/ui/*.rs");
}
```

- The `.stderr` files change with the compiler version. Pin the toolchain for this test or expect to refresh them on upgrade. For a single small case, a `compile_fail` doctest is lighter.
- Review the expected error once: a file can fail to compile for the wrong reason (a typo, a missing import) and the test still passes.

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

## Tooling, versions and packaging

- **Clippy with warnings denied is a correctness gate.** A real share of its lints catch bugs, needless allocation and interface hazards. Warnings left optional become background noise. Suppress one lint at one site with a reason (`#[expect(lint, reason = "...")]` on recent toolchains); do not switch off a whole class without understanding why it fires.
- **`rustfmt` is not negotiable.** It removes style from review and keeps diffs and blame readable. Do not hand-format against it. Commit the configuration:

```toml
# rustfmt.toml
edition = "2024"
max_width = 100
```

- **Many attractive `rustfmt` options, including `group_imports` and `imports_granularity`, are unstable** and take effect only on a nightly toolchain. Putting them in a project formatted with stable makes contributors disagree with CI. Use them only if formatting is pinned to nightly everywhere.
- **State the minimum supported Rust version, and test on it:**

```toml
[package]
rust-version = "1.76"
```

  A declared version that CI never builds with is a guess. Raising it is a compatibility change for a library; document it. Libraries do not depend on nightly-only features.

- **Pin the toolchain for an application or a workspace:**

```toml
# rust-toolchain.toml
[toolchain]
channel = "1.80.1"
components = ["rustfmt", "clippy"]
```

  A pin makes builds and lint results reproducible, and must be raised on a schedule or it becomes a blocker for dependencies. A published library is different: it tests on its minimum version *and* on current stable, since its users choose the compiler.

- **Supply chain is policy, not a lock file.** `Cargo.lock` fixes versions; it does not tell you one of them has an advisory, an unacceptable licence or was yanked.

```toml
# deny.toml
[licenses]
allow = ["MIT", "Apache-2.0", "BSD-3-Clause", "ISC", "Unicode-3.0"]

[bans]
multiple-versions = "warn"

[sources]
unknown-registry = "deny"
unknown-git = "deny"
```

  - Run the licence, ban and source checks on every change. **Run the advisory check on a schedule as well,** since a new advisory appears without any commit. If it only runs on changes, an unrelated change gets blocked by it and someone disables it.
  - `cargo audit` covers advisories alone; `cargo deny` adds licences, bans and sources; `cargo vet` records who reviewed what. Choose by the risk carried.
  - An ignored advisory has a reason and a review date.

- **Workspaces:** one `Cargo.lock` and one `target`; profiles only at the root; shared versions in `[workspace.dependencies]`; shared lint levels in `[workspace.lints]`. **Features are additive:** enabling one must never remove an item or change behaviour for another crate, since Cargo unifies features across the workspace.
- Aliases belong in a committed `.cargo/config.toml`. **`[net] offline = true` belongs there only with vendored dependencies;** otherwise a fresh clone cannot build.
- **Coverage in CI:** exclude generated code with `--ignore-filename-regex`, emit a machine-readable report, and prefer a floor on the critical modules to a global one. Branch coverage helps where line coverage flatters.
- **A typical CI set:** format check, clippy with warnings denied, tests (`cargo nextest` is faster, and does not run doc tests, so add `cargo test --doc`), documentation build, dependency policy, and a semver check for published libraries. With SQLx, add `cargo sqlx prepare --check` so offline query data cannot go stale.
- **Wrap secrets in a type that resists display** (`secrecy::SecretString`), expose them only at the point of use, and never pass them as plain `String` "because the code is internal".
- **Use `tracing` with spans, fields and correlation identifiers,** so a concurrent failure can be reconstructed. Record identifiers and sizes, not whole payloads.

**Commit the public interface of a published library as a golden file.** CI regenerates it
(`cargo public-api`), fails with a diff, and one explicit command overwrites it. The diff is
reviewed, never edited by hand. This makes every interface change visible in review,
including accidental ones such as a newly public helper or a changed auto trait. Not worth
it for an application crate nobody links against.

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

- Does any public signature expose a dependency's type, a concrete container the crate may want to change, or an error the caller cannot match on?
- Can every public enum and struct that will grow do so without a breaking change?
- Which public names must stay stable, even if a cleaner name exists?
- Is any invariant carried only by a comment, where a newtype, an enum or `TryFrom` would carry it in the type?
- Are `Send` and `Sync` asserted in a test for public types, so a new field cannot remove them silently?
- Does every public item document its errors and panics, and does every example compile as a doc test?
- Did the interface change go through `cargo semver-checks`, and was the minimum Rust version built?
- Do the supported feature combinations build and pass, including no default features if the crate claims that?

**Reject by default:** `anyhow` or `Box<dyn Error>` in a public signature; `&Vec<T>`,
`&String` or `&Box<T>` parameters; a public enum that will grow without
`#[non_exhaustive]`; a glob re-export that is not a deliberate prelude; a feature that
removes items; `println!` in library code; a panic on a path input can reach; a public
item renamed in place for style.

## Out of scope

- **Hot loops, allocation tuning, custom data structures, parsers and indexes.** Use the infra skill.
- **Unsafe code and FFI bindings.**
- **Binaries built on the library:** argument parsing, configuration, exit codes, services.

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
