---
name: rust-infra-storage
description: Self-contained guide for Rust that persists, frames or synchronises data - on-disk formats and caches, write-ahead logs and snapshots, content-addressed and incremental indexes, atomic file updates and text edits, binary and length-prefixed wire protocols, streaming decoders, patch and sync protocols, bounded queues and event pipelines. Use when the task defines or changes a file or wire format, a storage layer, an index that updates incrementally, a decoder for a byte stream, or a pipeline between producers and consumers. Not for SQL-backed CRUD in a service, or for parsing source text.
---

# Rust for storage, formats and protocols

This is the Rust that must stay correct across crashes, versions and partial input. Its
defects are a file half-written at power loss, a format change that old readers misread, a
decoder that trusts a length field, an index that drifts from its source, a corrupt store
treated as an empty one, and a queue with no bound.

## When to use this skill

- **Use it when** the change touches bytes that outlive the process or cross a connection: files, caches, logs, indexes, frames, messages.
- **Signals:** `serde` with a versioned format, `bytes`, `tokio_util::codec`, `memmap2`, `rocksdb`, `redb`, `rusqlite`, checksums and content hashes, `fsync`, sequence numbers.
- **Skip it for** CRUD over a relational database in a service (the application-service skill) and parsing source code (the parsers skill).
- **It is complete on its own.** The Rust essentials, the gate commands and the definition of done are at the end.

## The defaults, in priority order

If unsure what matters most, work down the list.

1. **Every persisted or wire format carries a version,** and a reader rejects or migrates what it does not know.
2. **Writes are atomic:** temporary file in the same directory, sync, rename over the target. Readers see the old file or the new one.
3. **A corrupt or unreadable store is an error, never an empty store.** Missing and broken are different outcomes; only a regenerable cache may treat broken as a miss.
4. **Every length, count and offset read from bytes is bounded before it is used** to allocate, slice or loop.
5. **One read is never one message.** Decoders are state machines over a buffer and report how much more they need.
6. **Know the state after a crash at every step,** and test recovery from each.
7. **Derived data has one invalidation path** and a full-rebuild command that the incremental path is tested against.
8. **Identity hashes are stable and canonical:** a named algorithm, a versioned canonical form, never `Debug` output or the default hasher.
9. **Everything that buffers is bounded,** with a stated policy when full.
10. **Round-trip, old-version and split-at-every-byte tests** accompany every format and decoder.

**How this kind of Rust differs from application Rust.** These are the answers for
infrastructure code, stated flatly:

- **Allocation, layout and algorithmic cost are design inputs,** not afterthoughts. They are still decided by measurement, never by instinct.
- **Errors are typed,** carry positions or keys, and never erase which failure happened. `anyhow` stops at the binary.
- **Input is hostile.** Every length, offset, depth and count from outside is bounded and checked; no input may panic the code.
- **Output is deterministic:** the same input gives the same bytes on every run and machine.
- **Evidence is heavier:** property tests and fuzzing for anything that reads bytes, `loom` or a model for hand-written synchronisation, benchmarks with a baseline for every speed claim.
- **Data structures and traits are the design.** Choosing them is the work, where in a service one concrete type would do.

## Storage, artifacts and edits

**One core crate, several thin adapters.** When one engine serves a desktop UI, a CLI, a server
and tests, the core owns the request and response types and the orchestration. Each adapter
converts input, calls the core and maps the error, and nothing else. Review check: an adapter
file containing an `if` about domain rules has logic in the wrong place.

**A storage factory with an in-memory back end.** The back end is chosen by configuration (a
URI scheme: file, object store, memory). The in-memory one implements the same trait and passes
the same contract suite, which gives tests a fast, deterministic store.

```rust
// One suite, run against every back end.
pub fn contract_suite(store: &dyn Storage) {
    put_then_get_returns_same_bytes(store);
    get_missing_key_is_not_found(store);
    overwrite_replaces_value(store);
    list_is_sorted_and_complete(store);
}

#[test]
fn memory_store_meets_contract() { contract_suite(&MemoryStore::default()); }
#[test]
fn file_store_meets_contract() { contract_suite(&FileStore::new(tempfile::tempdir().unwrap().path())); }
```

- The contract suite is what keeps a fake honest. Without it, tests pass against behaviour the real back end does not have (ordering, case sensitivity, atomicity).
- *Skip the trait when* every call site needs back-end-specific features; a lowest common denominator that leaks is worse than a concrete type.
- **An enum for which, a trait for how.** A persisted enum of provider kinds maps each variant to an implementation that can detect, install and run it, and every variant passes the same contract tests. Renaming a persisted variant is a data migration.

**Artifacts on disk.**

- **Any artifact of more than one file has a manifest** naming each file, its layout and the format version. The reader opens files through the manifest, never by file-name convention. Tests round-trip the manifest and open an artifact written by the previous version.
- **A format carries a version from its first release,** and the reader rejects a version it does not know with an error that states both versions.
- **A manifest does not store its own path.** A type that saves itself keeps the path in a `#[serde(skip)]` field set by the reader. A missing file is `Ok(None)`, not an error, when absence is normal.
- **Memory-mapped data sits behind typed cursors.** Validate the ID at the edge and return a typed view over `offsets[n]..offsets[n + 1]`; higher layers never index the raw mapping. A mapped file is untrusted input: check every offset and length before slicing, and remember that another process truncating the file makes the mapping fault.
- **Write atomically:** write to a temporary file in the same directory, flush, then rename over the target.

**A validated edit set, applied back to front.** A tool that modifies text computes every edit
as a byte range against the original, rejects out-of-range and overlapping edits, and applies
from the end backward so earlier offsets stay valid.

```rust
pub struct TextEdit {
    pub start: usize,
    pub end: usize,
    pub replacement: String,
}

pub struct EditSet {
    edits: Vec<TextEdit>,
}

impl EditSet {
    pub fn new(mut edits: Vec<TextEdit>, source: &str) -> Result<Self, EditConflict> {
        edits.sort_by_key(|e| (e.start, e.end));
        for e in &edits {
            let in_bounds = e.start <= e.end
                && e.end <= source.len()
                && source.is_char_boundary(e.start)
                && source.is_char_boundary(e.end);
            if !in_bounds {
                return Err(EditConflict::OutOfBounds { start: e.start, end: e.end });
            }
        }
        for pair in edits.windows(2) {
            if pair[1].start < pair[0].end {
                return Err(EditConflict::Overlap { at: pair[1].start });
            }
        }
        Ok(Self { edits })
    }

    /// `source` must be the string the set was validated against.
    pub fn apply(&self, source: &str) -> String {
        let mut out = source.to_owned();
        for e in self.edits.iter().rev() {
            out.replace_range(e.start..e.end, &e.replacement);
        }
        out
    }
}
```

- The `is_char_boundary` check is what stops `replace_range` panicking on multi-byte text.
- **Positions are converted once, in one tested function.** Editors count lines and UTF-16 code units, parsers count bytes, humans count from one. Tests include a multi-byte character and an emoji before the edited position.
- Two inserts at the same offset need a stated order (a priority field, or input order with a stable sort).
- Tests: one edit, several disjoint edits, same-position inserts, overlap rejected, out-of-bounds rejected, non-ASCII text.

**Editor back ends.** Translate each change into the parser's native edit, apply it to the old
tree and re-parse incrementally; recompute highlights and diagnostics on a debounce. Keep a
bounded map from buffer version to tree, and cancel a stale parse when a newer edit arrives.
Test insert, delete and multi-line edits, not only the first parse. *For small files or
parse-once input, a full re-parse is simpler and none of this is needed.*

**A stdio tool server is a loop over a registry.** Read one JSON-RPC request per line, dispatch
by method, write exactly one JSON line per response.

- **Stdout carries the protocol and nothing else.** Logs go to stderr. One stray `println!`, from your code or a dependency, corrupts the stream.
- Invalid JSON gets a parse-error response and the loop continues. An unknown method gets a method-not-found response. A handler that panics must not take the server down: isolate it and answer with an internal error.
- Flush after every response, and exit cleanly when stdin reaches end of file.
- Integration tests send initialise, list, an unknown method, invalid JSON and one real call, and assert that every response is one line of valid JSON.

**Invariants over a whole collection.**

- **A collection invariant lives in a wrapper.** When no single element can enforce it (every batch has the declared schema, every part belongs to one tenant), a wrapper owns the collection and `try_new` rejects the first violation, naming the expected and the actual value. `TryFrom` impls reuse that constructor; `into_inner` gives the parts back. Do not hand out `&mut` to the inner collection, or the invariant is gone.
- **A duplicate registration is a typed error.** Whatever owns scarce names (routes, URL schemes, sockets, commands) refuses a second registration with an error carrying the name, and leaves its state unchanged. Nothing is overwritten silently.
- **Typed attributes for composed views.** When several views share one graph or document model, the view-specific meaning is a typed attribute (`enum EdgeKind { Ast, ControlFlow, DataFlow }`), not a free-form string that degrades silently when misspelled.
- **Emulating a missing platform feature** with a narrower one is a small pure module of three functions (match, apply, revert) with a round-trip test and a test that names sharing a prefix do not match. Not where security depends on the original semantics, such as a page's origin.

## Protocols, messages and state

**Parse bytes without doing I/O.** A codec takes a byte slice and returns a frame plus the
number of bytes consumed. The transport owns reads, timeouts, encryption and backpressure.

```rust
pub enum Decoded<'a> {
    Frame { frame: Frame<'a>, consumed: usize },
    NeedMore { at_least: usize },
}

pub fn decode(buf: &[u8]) -> Result<Decoded<'_>, FrameError> {
    let Some(header) = buf.get(..HEADER_LEN) else {
        return Ok(Decoded::NeedMore { at_least: HEADER_LEN - buf.len() });
    };
    let len = u32::from_be_bytes([header[0], header[1], header[2], header[3]]) as usize;
    if len > MAX_FRAME_LEN {
        return Err(FrameError::TooLarge { len });
    }
    let total = HEADER_LEN + len;
    match buf.get(HEADER_LEN..total) {
        Some(payload) => Ok(Decoded::Frame { frame: Frame { payload }, consumed: total }),
        None => Ok(Decoded::NeedMore { at_least: total - buf.len() }),
    }
}
```

- "Not enough bytes yet" is not an error; it is distinct from "malformed". Conflating them either drops slow connections or accepts garbage.
- **Check the declared length against a maximum before allocating or waiting for it.** A length field from the network is an allocation request from a stranger. Use `get(..)` and checked arithmetic, never indexing.
- The same codec then works over TCP, a file, a test vector and a fuzzer. Tests: a short header, a length beyond the buffer, a length over the maximum, several frames back to back, a round trip. A fuzz target asserts that decoding never panics.
- **A stream that ends at a record boundary is `Ok(None)`; one that ends inside a record is an error.**
- A format that leaves the process family gets a version header and compatibility tests.

**An envelope for every message on a shared bus.**

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BusEvent<T> {
    pub id: Uuid,
    pub subject: String,
    pub timestamp: DateTime<Utc>,
    pub source: String,
    pub payload: T,
}
```

- Subjects are constants shared by publisher and subscriber. The subject and source stay in the body, not only in broker headers, so an event can be stored, replayed and inspected on its own.
- **Delivery is at least once, so consumers are idempotent,** keyed on `id`. Order across subjects is not guaranteed unless the broker says so.
- Adding an optional payload field is compatible; renaming or removing one is not. Version the subject or the payload when it must break.
- Tests round-trip real payloads and cover acknowledge, reject and redelivery against a real broker, not a mock.

**Wire types and internal types are different types.**

- **Internal events are translated, not serialised.** One function maps each internal event to an optional protocol message; internal enums never go on the wire, or every refactor becomes a protocol change. Snapshot-test each mapping.
- **Nothing unwraps a wire field.** Required fields go through a helper that returns an error naming the missing field. Each variant has a golden fixture, plus a negative one with a required field removed.
- **A name resolved on demand needs an allow-list.** A lookup that falls back to treating an unknown name as a URL or a path accepts only explicit schemes and rejects the rest clearly. This is how a convenient fallback becomes a file-read or request-forgery hole.

**Actors behind a typed mailbox.** Callers hold a handle with methods; the channel is private.

```rust
#[derive(Clone)]
pub struct CounterHandle {
    tx: mpsc::Sender<Command>,
}

enum Command {
    Add { amount: u64, reply: oneshot::Sender<u64> },
}

impl CounterHandle {
    pub async fn add(&self, amount: u64) -> Result<u64, ActorGone> {
        let (reply, rx) = oneshot::channel();
        self.tx.send(Command::Add { amount, reply }).await.map_err(|_| ActorGone)?;
        rx.await.map_err(|_| ActorGone)
    }
}
```

- The mailbox is bounded, and what happens when it is full is decided (wait, or `try_send` and reject).
- The actor ends when every handle is dropped (`recv` returns `None`) or on a shutdown signal, and its exit is observable through its `JoinHandle`.
- Tests work at the handle: send after exit, a full queue, a dropped reply, a panic inside the actor.
- *Use when* state has one logical owner and several async callers. *Skip when* a mutex held briefly with no `.await` inside does the job; it is simpler and faster.

**Smaller rules.**

- **Lifecycle metadata lives apart from payloads.** For jobs with large bodies, one store holds the record (ID, state, attempts, deadlines, last error) and another holds the bodies. Leases, retries and polling then change without touching payload storage.
- **A journal sits on narrow storage.** The storage trait offers positioned read and write; the journal above it owns append, lookup and recovery. The same tests run against a temporary file and memory, including reopen, a torn final record and a corrupted entry.
- **Lazy loading state is an enum in the registry:** not loaded, loading with its waiters, loaded, failed with the cached error. Concurrent requests join the one load (`tokio::sync::OnceCell` covers the simple case). Decide whether a failure is cached or retried.
- **Detection is pure; verification is a later step.** Classify arguments with slice patterns in a function with no side effects; file-system checks and execution come after, explicitly.
- **A rewrite reports whether it changed anything,** and an unchanged node must say so, or a fixed-point loop never ends. The driver also has a pass limit and checks an invariant after every rule.
- **Variants of one algorithm share one output type,** and a compare mode runs the simple and the optimised variant and fails when they differ. It is the cheapest oracle available for an optimisation.
- **An operator that returns a stream does no work until polled** and never blocks inside `poll`. Tests poll it, check the schema and drop it early.
- **A guard fixes the order of unlock and side effect.** When an effect must follow a lock release, a guard's `Drop` releases and then runs the effect, so no path can do them in the wrong order.
- **Versions are explicit in storage.** A read states the version it reads as of, and a held read blocks compaction below that version. Operations that combine versions or timestamps return `None` on overflow.
- **A schema states capabilities per field** (queryable, stored, sortable); ingestion and query parsing both read it, and a query on an unsupported field is an error, not an empty result.
- **Constrained choices are `Copy` enums with `ALL` and `const fn` relations** (valid partners, command names, defaults), so prompts, validation and docs read one source.

**Small languages and analysis hosts.**

- **A public parse entry point consumes the whole input:** skip surrounding whitespace, then require end of input, so trailing garbage fails. Inner rules never require end of input, because they must compose.
- **Two entry points:** one returning the domain error for programs, one returning a rendered diagnostic with a source span for people. The parsing library's types stay inside the module; the API returns owned nodes.
- **Grammar first, meaning second.** The grammar accepts the shape. Rules that need context (duplicates, unknown names) live in a later check with domain messages, and negative tests assert the message.
- **Owned output keeps byte ranges.** When results outlive the source text, convert to owned values paired with their source ranges. Never drop the ranges; diagnostics and navigation map back through them.
- **A hand-written mini-language stays tiny.** Acceptable for a controlled internal format with a handful of constructs. Once it needs expressions, escaping, includes or untrusted input, use a maintained parser crate.
- **A virtual file system sits between I/O and analysis.** Analyses never read the disk; a loader does, and the VFS assigns file identities and merges changes. Tests use an in-memory loader.
- **Extraction is pure; storage is incremental.** Functions turn input into facts; a store keeps them. A test changes one file and checks that only its dependents are recomputed. An incremental result is compared with a from-scratch run on the final input: that golden test catches most incremental bugs.
- **One context owns the caches,** with a memoised "derive this" method; individual checks consume the context. A test runs two checks over one item and asserts a single derivation.
- **Anything touching unstable compiler internals sits in one thin adapter,** and the toolchain version is pinned and treated as part of the interface.
- **External tools are candidates behind a trait** (detect, installed, install, version) that receives a command runner; tests pass a fake runner.

## Strategies, formats and bounds

**One operation, several strategies, chosen in one place.** A public operation may have
several implementations (memory map, whole buffer, incremental reader) selected from
configuration, input shape and platform. The selection is one function.

- Impossible configurations are rejected up front with a typed error, before any work starts.
- **A fast path never removes the slow path,** and the two are tested against each other. The rarely taken path gets its own tests; configuration bugs live there.
- Let a test force each strategy. If only the heuristic can choose, the fallback is never exercised.
- *Not for* callers who need one exact algorithm; give them the named function.

**Permissive on the way in, canonical inside.** A forgiving input form (unsorted, duplicates
allowed) accepts messy data. The compute form has a documented invariant (sorted, unique)
established once, at conversion.

- The canonical type's constructor is the only way to make one, so every holder may rely on the invariant. Operations that receive raw parts check and return a typed error; they do not compute a wrong answer.
- Canonicalising can change the element count (duplicates merge). Do not carry counts across the conversion.
- Do not canonicalise silently on a hot path where a sort would surprise, or where duplicates mean something.

**Bundle repeated bounds into one named trait.**

```rust
pub trait Scalar:
    Copy + PartialEq + Add<Output = Self> + Sub<Output = Self> + Mul<Output = Self> + Default
{
}

impl<T> Scalar for T where
    T: Copy + PartialEq + Add<Output = T> + Sub<Output = T> + Mul<Output = T> + Default
{
}
```

- The blanket impl makes it an alias: every qualifying type gets it for free. Leave the blanket impl out only when implementers must opt in or supply methods.
- Create it after the same bound list has appeared three times, not before. Its supertraits are exactly what the algorithms call; a bound nobody uses still shuts types out.
- Long supertrait lists make compiler errors long. Split the trait if implementers must supply much more than each algorithm uses.

**A scoped helper makes the safe lifetime the default.** If the caller must remember cleanup,
offer `with_x(|resource| ...)` beside the raw constructor.

```rust
pub fn with_temp_dir<T>(f: impl FnOnce(&Path) -> io::Result<T>) -> io::Result<T> {
    let dir = tempfile::tempdir()?;
    let result = f(dir.path());
    dir.close()?; // explicit, so a clean-up failure is reported
    result
}
```

- The borrow checker stops the resource escaping the closure, and clean-up runs on the error path too.
- An RAII guard is the more flexible form and composes with `?` and early return. Use the closure when the resource must not outlive a scope under any circumstances, or when clean-up can fail and the caller should hear about it.
- An async closure borrowing the resource is awkward to type; there a guard, or an owned handle with an explicit `close().await`, is usually simpler.
- Where native handles are exposed to JavaScript (Tauri, WebAssembly), provide the scoped form on that side too, and test both the throwing and the resolving callback.

**One `apply_update` for a streamed record.** A record built up progressively (a job status,
a trace) changes only through `apply(&mut self, update: Update) -> Result<(), UpdateError>`
over a typed update enum.

- An impossible or out-of-order update is a typed error, never a panic, since updates may come from outside.
- The full internal record and the form sent to clients are different types, and the conversion is where redaction and trimming happen. It runs before anything leaves the process.

**A conversion that only reads its source takes a reference.** `impl From<&Dense> for Sparse`
lets the caller keep the original; add `From<Dense>` only when consuming the source saves a
copy. Have the impl delegate to a named function, which can be tested and benchmarked alone.

## Streams, formats and protocols

**Streamed text becomes lines first.** Before any diff, patch or parse logic, turn chunks
into complete lines: append each chunk to a buffer, emit every complete line, keep the
trailing partial line, and flush the remainder when the stream ends.

```rust
pub struct LineBuffer {
    pending: Vec<u8>,
}

impl LineBuffer {
    pub fn push(&mut self, chunk: &[u8]) -> Vec<String> {
        self.pending.extend_from_slice(chunk);
        let mut lines = Vec::new();
        while let Some(end) = self.pending.iter().position(|byte| *byte == b'\n') {
            let line: Vec<u8> = self.pending.drain(..=end).collect();
            lines.push(String::from_utf8_lossy(&line).into_owned());
        }
        lines
    }

    pub fn finish(self) -> Option<String> {
        (!self.pending.is_empty())
            .then(|| String::from_utf8_lossy(&self.pending).into_owned())
    }
}
```

- **Buffer bytes, not `String`s.** A chunk boundary can fall inside a multi-byte character; decoding each chunk separately corrupts it. A complete line is safe to decode because `\n` never occurs inside a UTF-8 sequence.
- Tests feed chunks that split mid-line, mid-character, and a stream with no final newline.
- Bound the pending buffer if the peer is untrusted: a stream with no newline grows it without limit.
- Fuzzy matching of edit anchors (accepting lines equal after trimming) suits prose and code edits. It is wrong for data formats where one character matters, and it never matches on blank lines.

**A line-oriented format with a few exclusive regions is a state enum and one `match` per
line.** Write the enum first.

```rust
#[derive(Debug, Clone, Copy)]
enum Region { Outside, Left, Base, Right }

let mut state = Region::Outside;
let mut opened_at = None;
for (index, line) in input.split_inclusive('\n').enumerate() {
    if line.starts_with(LEFT_MARKER) {
        state = Region::Left;
        opened_at = Some(index);
        continue;
    }
    // The base, right and end markers change `state` the same way.
    match state {
        Region::Outside => { left.push_str(line); right.push_str(line); }
        Region::Left => left.push_str(line),
        Region::Right => right.push_str(line),
        Region::Base => {}
    }
}
if let (Region::Left | Region::Base | Region::Right, Some(line)) = (state, opened_at) {
    return Err(ParseError::Unterminated { opened_at: line });
}
```

- `split_inclusive('\n')` keeps line endings, so content is rebuilt byte for byte, including `\r\n`. `lines()` discards them.
- **Record where the open region began,** so an unterminated region at the end of input is an error with a location, not silently accepted.
- A marker in the wrong state (an end with no start) is an error too. Nested or escaped markers need a stack or a real parser.

**Cross-language contracts.**

- **Integers beyond 2^53 − 1 do not survive JavaScript.** A Rust service exposing `u64` or `i64` identifiers to a JavaScript client sends them as strings.

```rust
#[derive(Serialize, Deserialize)]
pub struct Event {
    #[serde(with = "u64_as_string")]
    pub id: u64,
}
```

- **Parity tests compare canonical structure,** ignoring object key order. Compare bytes only when the exact bytes are the contract (signatures, hashes).
- Shared fixtures include large integers, dates and time zones, binary data, empty and nested arrays, `null` versus absent, and non-ASCII text.
- **Variants are a tagged enum** (`#[serde(tag = "type")]`) whose variants carry only the fields valid for that kind. A flat struct of optional fields lets illegal mixtures through.
- Add the discriminant and its validation before adding consumers.

**Incremental update protocols define their conflicts.** A patch stream (live graph, index
deltas, UI state) says what happens when one patch both removes and upserts the same id,
and reconciles before publishing.

- With upsert-wins, the removal is netted away, so a client applying removals and upserts in either order reaches the same state.
- Replication and audit logs want delete-wins with tombstones instead. Choose deliberately.
- Test removing and recreating one id in a single patch.
- Patches carry a sequence number, so a client can detect a gap and ask for a full snapshot.

**Smaller rules.**

- **An optional enhancement sits behind a capability check with the plain path as fallback.** Initialise it once and remember failure (`OnceLock<Option<T>>`), so it is not retried per item. **A silent fallback makes deployments behave differently:** log the capability state at start-up and record it with any output that depends on it.
- **Resources that survive reconnects get identifiers from a stable property** (a fixed name, a hash of the canonical path), never a process-local counter. A short hash prefix is fine as a local key and wrong as a global identity. Do not leak a sensitive path through a public id.
- **A list that is capped says so.** Return a `truncated` flag or the total beside it, and sort before capping by a documented, deterministic order.
- **Dangling references found while projecting data are skipped and counted,** as a signal of index integrity, not ignored.
- **A fixed-point loop converges on a canonical form.** If equal states can be represented differently (unsorted, with cancelling entries), the loop never sees "no change". Normalise each round, and cap the iterations with an error that says the cap was hit.
- **An append-only segment writer** uses positioned writes at its tracked offset, takes `fsync` as an explicit policy so the caller sees the cost, and publishes the new size only after the write succeeds. Concurrent writers reserve their range first or are serialised. After recovery, the counter equals the file length.
- **A null-aware column builder appends a value for every row,** a default for null rows, and tracks validity separately, so the values buffer and logical length always agree. The validity bitmap is created at the first null and back-filled.

## Hashes, prefilters and storage invariants

**More on identity hashes.**

- **Put a format version in the hashed data,** so a change to the canonical form cannot be mistaken for unchanged content.
- **Normalise per domain type through a trait.** Never hash `Debug` output or default serialisation and hope it is stable: field order, float formatting and map order are not promises.
- For each new field, decide whether it is semantic or presentation-only, and change the canonical form and the hash-stability tests in the same commit.
- A value that cannot be hashed deterministically is an explicit error.
- **An identity hash is not a security proof.** For anything an attacker can influence, use a keyed MAC or a signature.
- **A semantic hash over a syntax tree** skips noise nodes (comments, whitespace), emits kind and text for value-bearing nodes and kind only for structural ones. Those three sets define "semantic": a value-bearing kind left out reports "unchanged" for a real change. Changing them is a version bump. *Not where* exact text or comments are part of the record.

**A cheap bit test in front of expensive scoring.**

```rust
#[derive(Clone, Copy, Default)]
pub struct CharBag(u64); // one bit per lowercased a-z and 0-9

impl CharBag {
    pub fn is_superset(self, other: CharBag) -> bool {
        self.0 & other.0 == other.0
    }
}
```

- A candidate whose bag lacks any query character cannot match, so most are rejected with one AND. The filter rejects only the impossible and is never the only check.
- **Scratch matrices are fields reused across candidates** (`clear()` then `resize`), stored as one flat `Vec` indexed `row * width + column`. A `Vec<Vec<T>>` allocates per row and scatters rows across the heap.
- Cost grows with query length times candidate length, so a long search keeps its cancellation checks.

**A rolling hash nominates; comparison decides.** Finding repeated fixed-size windows with a
rolling hash costs one pass over the input.

```rust
hash = hash.wrapping_mul(BASE).wrapping_add(incoming);
hash = hash.wrapping_sub(POWER.wrapping_mul(outgoing)); // POWER = BASE^window
```

- Equal hashes mean "probably equal". Confirm by comparing the blocks. This holds for any hash used as a shortcut for equality.
- Use explicit `wrapping_*` arithmetic; plain `*` and `+` panic on overflow in debug builds.
- Long runs of identical items produce a quadratic number of matches; collapse them first.

**A snapshot is a leased read instant.** Opening one registers its sequence number and
returns a guard whose `Drop` deregisters it. Garbage collection frees only versions below
the lowest number still registered.

```rust
pub fn open(&self) -> SnapshotGuard {
    let _gc = self.gc_lock.read(); // collection cannot run between the load and the insert
    let sequence = self.sequence.load(Ordering::Acquire);
    *self.open.entry(sequence).or_insert(0) += 1;
    SnapshotGuard::new(sequence, self.clone())
}

pub fn publish(&self, batch_sequence: u64) {
    self.sequence.fetch_max(batch_sequence + 1, Ordering::AcqRel); // never moves backwards
}
```

- **A leaked or long-held snapshot blocks collection for ever.** Export the age of the oldest open snapshot as a metric.
- Test that an old snapshot still reads old values after later writes and an explicit collection.

**Shared durable artefacts are deleted only when every dependant is past them.** A
write-ahead-log segment serving several partitions records one sequence number per
partition. Deletion walks from the oldest segment and stops at the first one that some live
partition has not yet persisted beyond. A deleted partition stops holding segments back.
Test crash recovery with mixed and deleted partitions.

**Durable formats.**

- **Every serialised field has a permanent tag or name,** never reused and never renumbered. Retired tags are reserved.
- **New fields arrive as optional.** A reader distinguishes absent from zero or false with `Option<T>`, not a defaulted scalar, and tolerates unknown fields. Use `#[serde(default)]` only where the default truly means "absent".
- Test three cases: field absent (old writer), field present, unknown field present (newer writer).
- **Separate physical storage from logical meaning:** a small stable set of storage types, plus tagged logical annotations carrying their parameters (`Decimal { precision, scale }`, `Timestamp { unit, utc }`). A new logical type also updates reader validation and round-trip tests.
- `#[serde(deny_unknown_fields)]` suits configuration files, where a typo should fail. It is wrong for a wire format that newer writers will extend.

**Smaller rules.**

- **A cache miss is a value.** Absence in a cache or content-addressed store is `Ok(None)`; `Err` is for real failures. Removing an entry that is already gone is success.
- **Non-overlapping chunks by line ownership.** Sort symbol spans longest first and assign each span's lines to it in that order, so a nested span overrides its parent; emit runs of one owner as chunks and window the unowned gaps. A file that fails to parse falls back to plain windows instead of failing the index. *Not when* retrieval benefits from overlapping context.
- **Expansion signals are opt-in and down-weighted** (graph neighbours of a hit), so they cannot outrank direct matches. Inspect each ranked list separately before changing weights.

## Incremental and amortised work

**Append cheaply, consolidate lazily.** For frequent signed updates where many increments
and decrements cancel (reference counts, change logs, multiset deltas), push each update and
consolidate only when a clean view is needed or the unsorted tail outgrows the clean prefix.

```rust
pub struct ChangeBatch<T> {
    updates: Vec<(T, i64)>,
    clean: usize, // updates[..clean] is sorted, merged and free of zeros
}

impl<T: Ord> ChangeBatch<T> {
    pub fn update(&mut self, item: T, delta: i64) {
        self.updates.push((item, delta));
        if self.updates.len() > 2 * self.clean.max(MIN_BATCH) {
            self.compact();
        }
    }

    /// Compacts first, so it takes `&mut self`.
    pub fn is_empty(&mut self) -> bool {
        self.compact();
        self.updates.is_empty()
    }

    fn compact(&mut self) {
        self.updates.sort_by(|a, b| a.0.cmp(&b.0));
        self.updates.dedup_by(|later, earlier| {
            if later.0 == earlier.0 {
                earlier.1 += later.1;
                true
            } else {
                false
            }
        });
        self.updates.retain(|(_, delta)| *delta != 0);
        self.clean = self.updates.len();
    }
}
```

- Compacting when the tail doubles the clean part keeps the amortised cost per update logarithmic, the same argument as `Vec` growth.
- **An observer that compacts takes `&mut self` and says so.** Hiding the mutation behind a `RefCell` to keep `&self` trades a compile-time rule for a run-time panic.
- The same shape serves any "write-optimised log plus periodic merge": tombstones in an index, pending edits to a sorted array.

**Incremental indexing by content hash.** Keep the set of content hashes per source file.
After a change, new minus old is inserted and old minus new is deleted; nothing else is
touched.

```rust
let to_insert: Vec<&Chunk> = new_chunks
    .iter()
    .filter(|chunk| !old_hashes.contains(&chunk.hash))
    .collect();
let to_remove: Vec<&Hash> = old_hashes
    .iter()
    .filter(|hash| !new_hashes.contains(*hash))
    .collect();
```

- **The hash inputs decide what counts as a change.** Including line numbers makes a pure move look like a change and redoes the expensive work; leaving them out means stored positions must be updated separately. Choose from the invalidation behaviour you want.
- Insert the new before deleting the old, or do both in one transaction, so a crash between them never leaves a file with no entries.
- Changing how content is chunked changes every hash: bump the index version and rebuild.
- Keep a full-rebuild command. It is the recovery path and the oracle for testing the incremental one: both must produce the same index.

**Smaller rules.**

- **Text enriched for retrieval is stripped before display.** If a chunk is indexed with a context preamble (file, language, defined symbols), one paired function removes it, so snippets and line numbers shown to people are those of the source.
- **Scores from two retrieval systems are not comparable; ranks are.** Fuse through stable ids, each source adding `weight / (rank + k)`. The weights and `k` are configuration tuned by evaluation, not constants in code. With calibrated, comparable scores, use the scores.
- **Cross-cutting behaviour lives in the framework, not in each plugin.** A linter owns traversal and suppression comments; rules only report. A rule that accumulates state is constructed per file or cleared in a finalisation hook, or findings leak from one file into the next.
- **In a streaming operator ordered by logical time,** buffered work is released when input progress proves that nothing earlier can arrive, never by a wall-clock timer. A held capability or watermark blocks everything downstream; drop it as soon as its output is emitted.
- **A parameter outside the supported range is a typed error before any work,** never an unbounded build. The bound is a product decision, since cost often grows steeply with it.

## Pipelines, sync and derived indexes

**Decorate, compute, undecorate.** When an algorithm compares heavy values many times (diff,
longest common subsequence, deduplication over long strings), map each distinct value to a
small integer once, run the algorithm on integers, and map back at the end.

```rust
fn intern<'a, T: Eq + Hash>(
    values: &'a [T],
    ids: &mut HashMap<&'a T, u32>,
    by_id: &mut Vec<&'a T>,
) -> Vec<u32> {
    values
        .iter()
        .map(|value| {
            *ids.entry(value).or_insert_with(|| {
                by_id.push(value);
                (by_id.len() - 1) as u32
            })
        })
        .collect()
}
```

- The reverse table is a `Vec` indexed by id: no second map, no `unwrap`.
- Interned ids make equality exact, unlike a hash, which can collide. The same idea gives subtrees an identity: intern each node's shape plus its children's ids.
- *Not worth it* when values are small or compared only a few times.

**Batch each stage to its own bottleneck.** In an offline job, slow external calls
(inference, remote APIs) run in fixed-size chunks with bounded concurrency; results land in
a pre-sized `Vec` by index, so order is preserved; one bulk write follows when everything
exists. Report progress per chunk. *Not for* streaming ingestion, where partial results
must be usable at once.

**Synchronise an inventory by diff, not rebuild.** Build maps of the existing and the
discovered items on a stable key, compare a fingerprint of the meaningful fields, and return
what happened.

```rust
pub struct SyncReport {
    pub added: Vec<Key>,
    pub updated: Vec<Key>,
    pub removed: Vec<Key>,
    pub unchanged: usize,
    pub errors: Vec<(Key, SyncError)>,
}
```

- One bad item is recorded in `errors`; it does not fail the whole run.
- The key must be unique within its scope, or a rename looks like a removal plus an addition.
- **An empty or failed discovery is not "delete everything".** Distinguish "source returned nothing" from "source could not be read" before removing.

**An incremental plan keeps four outcomes apart.** The timestamp decides when to hash; the
hash decides what changed.

| Observation | Step |
|---|---|
| Modified time newer, hash differs | index the new version, retire the old |
| Modified time newer, hash equal | record the new time only |
| Path gone | remove |
| Modified time not newer | nothing |

- **Metadata is a shortcut, not proof.** Timestamp precision varies by filesystem, and clocks and checkouts can move times backwards. Where a missed change is costly, compare with "different", not "newer", or hash regardless.
- A two-stage key does the same for caches: a cheap metadata key first, the content key as the authority. Write down what the cheap key assumes.

**Derived structures change together.**

- **After a registry change, everything derived from it is rebuilt and swapped as one unit:** one `ArcSwap` or one lock over a struct holding all of them. Readers never see a new index beside an old lookup table.
- **A derived index is keyed by everything that produced it:** source identity (repository and commit), tool version, schema version and relevant settings. Commit alone goes stale on a tool upgrade, and is wrong when uncommitted or generated files feed the index.
- **A content-addressed store shared by several tags** (branches, workspaces) tracks which tags use each artefact. Adding a tag recomputes nothing; removing the last tag deletes the artefact. Tag changes are transactional when writers run concurrently. *Skip it* when artefacts are cheap to rebuild.

**Graph results cross a boundary ready to use.** Return analysed structures, not raw
traversal order.

```rust
let has_self_edge = component.len() == 1
    && graph
        .get(&component[0])
        .is_some_and(|children| children.contains(&component[0]));
components.push(Component {
    is_cycle: component.len() > 1 || has_self_edge,
    nodes: component,
});
```

- A single-node component is a cycle only when it has an edge to itself.
- Sort roots and children before traversal, so output is deterministic.
- **Recursive graph algorithms overflow the stack on deep input.** Use an explicit stack for anything whose depth the input controls.

**Smaller rules.**

- **A ranking is sorted by score, then by a stable key.** `HashMap` iteration order must never decide the order of equal scores.
- **A fused score is relative evidence,** not a probability. Validate that the number of weights equals the number of lists.
- **One connection boundary for a subsystem with several services.** `connect` is idempotent, checks every dependency before any work, and fails with a message that says how to fix it. Keep health per dependency visible when they can degrade independently.
- **Export files follow the importer's boundaries** (one file per table or relation). Write a header only when creating the file, put the path in every I/O error, and remove partial files after a failed write.
- **Oversized inputs are skipped before expensive work,** by a stated size cap, and the skip is reported.

## Lazy side structures, memos and multi-file output

**Create an optional side structure on first need.** When the all-default case dominates
(no nulls, nothing dirty, no overrides), keep only a count until the first exception, then
build the structure and back-fill it.

```rust
pub struct ValidityBuilder {
    bitmap: Option<BitmapBuilder>,
    valid_before_bitmap: usize,
}

impl ValidityBuilder {
    pub fn append_valid(&mut self, count: usize) {
        match self.bitmap.as_mut() {
            Some(bitmap) => bitmap.append_n(count, true),
            None => self.valid_before_bitmap += count,
        }
    }

    pub fn append_null(&mut self) {
        let seen = self.valid_before_bitmap;
        self.bitmap
            .get_or_insert_with(|| {
                let mut bitmap = BitmapBuilder::new();
                bitmap.append_n(seen, true);
                bitmap
            })
            .append(false);
    }

    pub fn finish(self) -> Option<Bitmap> {
        self.bitmap.map(BitmapBuilder::finish)
    }
}
```

- The common case pays one integer add and no allocation; consumers get `None` and skip the check entirely.
- Property-test that the side structure's length equals the main length after any sequence of appends.
- *Not when* a placeholder stored for an absent row is costly, or could be read by a consumer that skips the validity check.

**An async memo entry has a pending state.** Keyed by a fingerprint of the inputs, each
entry is `Pending` or `Ready(Option<T>)`: a second caller waits for the first, and a
finished empty result is not mistaken for unfinished work.

- *Only for* deterministic work, or with every side-effect dimension in the fingerprint.
- **A producer that fails or is cancelled must clear or fail its pending entry,** or every waiter hangs. A guard that removes the entry on drop covers cancellation.
- Decide whether errors are cached. Usually they are not, or a transient failure becomes permanent.
- Race test: two concurrent requests for one fingerprint, and assert that one producer ran.

**Schema inference is deterministic.** To infer one schema from heterogeneous JSON or CSV,
infer a type per value and merge with fixed, written rules: nothing seen gives null, one
type stays, structs union their fields, lists merge element types, integer with float gives
float, null with a type gives that type made nullable.

- **Incompatible types are a typed conflict error or an explicit, documented fallback.** A silent fall back to string loses data and hides the bad rows.
- Field order follows first appearance (an insertion-ordered map), so the same input gives the same schema. Table-test each merge rule.
- Inference from a sample is a guess. Say how many rows were sampled, and validate the remaining rows against the result.

**Files written in parts.**

- **Clean up on failure.** A step that creates several outputs records each path as it is created and removes them all if a later step fails. A guard whose `Drop` removes them unless committed also covers panics and early returns.

```rust
pub struct OutputSet {
    paths: Vec<PathBuf>,
    committed: bool,
}

impl OutputSet {
    pub fn commit(mut self) {
        self.committed = true;
    }
}

impl Drop for OutputSet {
    fn drop(&mut self) {
        if !self.committed {
            for path in &self.paths {
                let _ = std::fs::remove_file(path); // best effort; the original error is what matters
            }
        }
    }
}
```

- A kill or power loss skips `Drop`. Write under temporary names and rename on commit, so leftovers are recognisable and a start-up sweep can remove them.
- **Validate a split by hashing:** the original through one hasher, the ordered parts through another, and compare. Where part order is not authoritative, keep a manifest with each part's index, size and hash. Tests delete a part, reorder two and flip one byte.
- **Archives need explicit parent directories.** A tar writer emits an entry for every ancestor, top-down, once each.
- **Retention deletes by reference, never by age alone.** Cleaning up old checkpoints removes a file only when no retained checkpoint refers to it: a compacted file from an old epoch may still be live. Delete data before the metadata that names it, advance the "oldest kept" marker last, and test the still-referenced case.
- Zero-pad sequence numbers in paths (`checkpoint-{epoch:07}`), so lexical order is numeric order.

**Smaller rules.**

- **Optional enrichment stays optional.** A network lookup that only improves data runs when its credential is present and its skip flag is unset, and only on entries already valid without it. The offline path and the tests work without the credential.
- **A vector with a read cursor is a queue** in allocation-free code: push to the back and advance an index. Otherwise use `VecDeque`; `Vec::remove(0)` in a loop is quadratic.
- **A failed push to a fixed-capacity container is handled,** not discarded, unless an invariant proves the capacity.
- **A size-bounded cache keeps a running total,** updated on insert and evict. Re-summing entries on every insert makes each insert linear.

**More on benchmarks.**

- **A fast path and the general path are two benchmarks over the same input,** named for the path (`dot_generic`, `dot_dense`). A specialisation with no paired benchmark has no evidence behind it.
- **A harness comparing several back ends has one outcome type,** normalised at the harness and not in each adapter. Format for display last; never mix numbers and words such as "timeout" in one column.

```rust
pub enum Outcome {
    Elapsed(Duration),
    Timeout,
    Failed(String),
}
```

- Each operation gets the same wall-clock budget, enforced per operation (`tokio::time::timeout`, or a child process killed at the deadline).
- **Name the phases** (load, start, readiness, measured loop, clean-up) and attach every metric to one. Set-up shortcuts stay out of the measured phase, and the measured path is the one users actually run.
- A run that reuses loaded data needs an explicit reset switch, and the report says whether the run was warm or cold.

## Queues and event pipelines

**The capacity permit travels with the queued item.**

```rust
pub struct Queued {
    pub message: Message,
    // Held only for its Drop: returns the capacity when the item is dropped.
    _capacity: OwnedSemaphorePermit,
}
```

- Capacity is returned wherever the item ends up: processed, discarded or cancelled. The field looks unused and is load-bearing, so the comment stays.
- **Count what is sent but not yet acknowledged.** A send queue limited by bytes must include batches awaiting acknowledgement, or memory is unbounded while the peer is slow.
- **Admit before enqueueing.** Ask the admission policy first, make room second, and increase the running count immediately before the spawn. Then a task that never runs cannot have displaced accepted work or leaked a count. Anything held while waiting is released by a guard, so cancellation of the wait releases it.

**`try_send` from a thread that must not block.** A blocking send from an event-loop or
reactor thread onto a full inbox parks the thread that drives everything else.

```rust
match inbox.try_send(message) {
    Ok(()) => {}
    Err(TrySendError::Full(_)) => {
        dropped.increment(1);
        warn!(shard, "inbox full, message dropped");
    }
    Err(TrySendError::Closed(_)) => return Err(Error::ShardStopped { shard }),
}
```

- A dropped message needs a written recovery path (retransmission, a log to replay). Without one, this is data loss with a log line.

**Discard results from superseded requests.** For typeahead, search or preview, cancelling
the previous request is not enough: its result may already be on the way.

```rust
let generation = self.latest.fetch_add(1, Ordering::Relaxed) + 1;
let results = search(&query).await;
if generation == self.latest.load(Ordering::Relaxed) {
    self.show(results); // otherwise a newer request has started; drop this one
}
```

- Use an ordered queue instead when every request must complete.
- **Coalesce level-triggered state, never edge-triggered events.** "Needs a rerun" can be merged into one flag. One-shot triggers and queued items must each be kept, or they are lost.
- **A guard can signal completion on every exit path** by sending in `Drop`. It cannot tell success from failure from cancellation, so use it only where "finished, somehow" is the whole message.

**One event enum drives a terminal UI or long-running client.** Ticks, input and loaded data
become one stream consumed by one state machine.

```rust
pub enum Event {
    Key(KeyEvent),
    Tick,
    Loaded(Result<Data, LoadError>),
}

loop {
    let event = tokio::select! {
        _ = ticker.tick() => Event::Tick,
        Some(key) = keys.recv() => Event::Key(key),
        Some(loaded) = results.recv() => Event::Loaded(loaded),
    };
    if app.update(event) == Flow::Quit {
        break;
    }
    terminal.draw(|frame| app.render(frame))?;
}
```

- A new action is a new variant handled in `update`. Rendering reads state and performs no I/O; loading happens in tasks that report back as events.
- Bound the channel or coalesce ticks, or a slow render builds an unseen backlog.
- *Not when* the UI framework already owns the event loop.

**Smaller rules.**

- **An in-process event broker** keys subscriptions by event type, returns a `#[must_use]` handle that unsubscribes on drop, keeps payloads cheap to clone, and bounds what a slow subscriber can hold up. Not for cross-process or durable delivery.
- **A resource that is expensive or not thread-safe belongs to one worker;** only job payloads cross the queue, and failures come back through the job's result. Cancellation covers queued and in-flight jobs alike.
- **Blocking reads behind an async API** run in `spawn_blocking` under a configurable semaphore. Too many permits overload the storage; too few slow every reader.
- **Round-robin by `fetch_add(1, Relaxed) % len`** is fine for spreading load over candidates that are already filtered. A least-loaded picker rotates its ties, or the first candidate always wins.
- **Bridging to a foreign event loop** (a UI loop, another language's runtime): the Rust future holds a guard that cancels the foreign task if dropped early, and all calls into the foreign loop go through its thread-safe entry point. Prefer a maintained adapter crate to a hand-written bridge.

**Hedged requests, for idempotent reads only.** Start the primary; start a backup on another
replica only if the primary has not answered after a grace period. The first success wins.

```rust
let primary = fetch(replica_a, &key);
tokio::pin!(primary);

tokio::select! {
    result = &mut primary => match result {
        Ok(value) => return Ok(value),
        Err(_) => return fetch(replica_b, &key).await, // failed early: fall back now
    },
    _ = tokio::time::sleep(grace) => {}
}

tokio::select! {
    Ok(value) = &mut primary => Ok(value),
    Ok(value) = fetch(replica_b, &key) => Ok(value),
    else => Err(Error::BothReplicasFailed),
}
```

- Set the grace period near the 95th-percentile latency, so only the slow tail is duplicated: a few per cent more load for a much shorter tail.
- Dropping the loser cancels it locally; the remote server may still do the work.
- **Never hedge a write or anything with a side effect.** Never hedge into an overloaded cluster: the duplicates make the overload worse. Cap hedges as a fraction of traffic.

**A stream ends when its channel closes.** Turning a blocking producer (a database cursor, a
directory walk) into an async stream: a thread or `spawn_blocking` task sends items on a
bounded channel and the receiver is the stream.

- The end is the last sender being dropped, which also happens on early return and on panic. Never an in-band magic value that a real item could equal. If "finished cleanly" must be distinguished from "producer died", send `Result` items and a final explicit `Done`.
- The producer stops when the send fails, which means the consumer went away. That is the cancellation path, so check every send.
- Fan-out width comes from an explicit limit, never from the size of the input.
- A small result-set type over a stream offers `one`, `all` and the raw stream, with an idempotent `close` and a terminal error that can still be read after the drain.

**Check for cancellation every N iterations of a tight loop.** Synchronous CPU work cannot be
dropped like a future; it has to look.

```rust
const CHECK_EVERY: usize = 10_000;

for (index, item) in items.iter().enumerate() {
    if index % CHECK_EVERY == 0 && cancelled.load(Ordering::Relaxed) {
        return Err(Error::Cancelled);
    }
    process(item);
}
```

- N trades cancellation latency against overhead; choose it from the cost of one iteration so the check runs every few milliseconds. The flag is passed in, not global.
- In an async task, a long loop also needs `tokio::task::yield_now().await` at intervals, or it starves its neighbours and cannot be cancelled either.

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

## Review

- What does a reader of the previous version do with data written by this one, and the reverse?
- What is on disk if the process dies at each step of a write, and what does start-up do with it?
- Is any length, count or offset from the bytes used before it is bounded?
- Is a corrupt, truncated or missing file ever read as valid empty data?
- Can the incremental index be rebuilt from scratch, and is it tested to equal the rebuild?
- What bounds each buffer and queue, and what happens when it is full?
- Are there round-trip tests, a fixture from each old version, and a decoder test split at every byte?

## Out of scope

- **SQL schema migrations and transactions in a service.** Use the application-service skill.
- **Parsing source code and reporting diagnostics.** Use the parsers skill.
- **Tuning for speed.** Use the performance skill, with a benchmark.
- **Distributed consensus and replication protocols** need specialist material.

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
