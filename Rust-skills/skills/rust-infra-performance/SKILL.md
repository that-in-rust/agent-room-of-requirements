---
name: rust-infra-performance
description: Self-contained guide for performance-critical and data-intensive Rust - hot loops, allocation and memory layout, benchmarks, caches, large collections, bulk and columnar data, CPU parallelism with threads and `rayon`, atomics and lock-heavy components, arenas, `no_std` and fixed-capacity code. Use when the task makes code faster or smaller, states a latency, throughput or memory target, adds a cache, changes a data structure for speed, or parallelises work. Not for ordinary services or command-line glue, where clarity wins.
---

# Rust for performance and data-intensive code

This is the Rust where cost is part of the requirement: a kernel that runs millions of
times, data larger than memory, a structure shared by many threads. Its defects are a
speed-up that changed the answer, a benchmark that measured the wrong thing, a cache that
served stale or another tenant's data, a pool that pinned peak memory, and a lock-free
trick that is a data race.

## When to use this skill

- **Use it when** the change has a stated speed, memory or throughput goal, or touches a hot path, a cache, a large data structure or CPU-parallel code.
- **Signals:** `criterion` or `divan` benches, `rayon`, `Atomic*`, `bumpalo`, `smallvec`, `dashmap`, `moka`, `#[global_allocator]`, `no_std`, profile settings in `Cargo.toml`.
- **Skip it for** code with no measured problem. An extra clone in a request handler is not a performance task.
- **It is complete on its own.** The Rust essentials, the gate commands and the definition of done are at the end.

## The defaults, in priority order

If unsure what matters most, work down the list.

1. **Correct, then measured, then faster.** Confirm the fast version gives the same result before timing it.
2. **Profile before changing anything.** The bottleneck is rarely where it looks. No number, no claim.
3. **Algorithm and data structure first,** then allocation, then memory layout, then parallelism. Stop at the stated target.
4. **Keep the checks.** Do not trade bounds checks, overflow checks or validation for speed because a benchmark moved; restructure so the check is cheap or provably unneeded.
5. **Measure the release build on representative input,** report the spread and the tail, and name the machine, toolchain and features.
6. **A cache is a correctness risk bought for speed:** state its key, bound, invalidation and the cost of a stale read before adding it.
7. **Bound memory:** pools, caches, queues and arenas each have a cap and a reset point.
8. **Parallel code is exercised under contention,** and anything built on atomics has a model or a written argument.
9. **`unsafe`, SIMD, prefetching and lock-free structures need a benchmark that proves the gain,** and are removed when it is not there.

**How this kind of Rust differs from application Rust.** These are the answers for
infrastructure code, stated flatly:

- **Allocation, layout and algorithmic cost are design inputs,** not afterthoughts. They are still decided by measurement, never by instinct.
- **Errors are typed,** carry positions or keys, and never erase which failure happened. `anyhow` stops at the binary.
- **Input is hostile.** Every length, offset, depth and count from outside is bounded and checked; no input may panic the code.
- **Output is deterministic:** the same input gives the same bytes on every run and machine.
- **Evidence is heavier:** property tests and fuzzing for anything that reads bytes, `loom` or a model for hand-written synchronisation, benchmarks with a baseline for every speed claim.
- **Data structures and traits are the design.** Choosing them is the work, where in a service one concrete type would do.

## Performance

**Defaults.**

- **Correct first, then measured, then faster.** Do not optimise without a profile showing where time or memory goes, and do not keep an optimisation without a benchmark showing it helped.
- **The largest wins are algorithmic and structural:** a better complexity class, less work, fewer allocations, fewer passes, data laid out for the cache. Micro-tuning comes last and matters least.
- **Build in release mode to measure.** A debug build can be ten to a hundred times slower and has a different profile.
- Clear, idiomatic Rust (iterators, slices, borrowed arguments) is usually already fast. Optimisation that costs clarity must pay for it in numbers.

### Speed that keeps the checks

- **A performance change is verified on two axes:** the benchmark delta, and that no checked operation became unchecked and no cached value can outlive its input. Do not replace `.get()` with indexing because a benchmark improved.
- **Prefer speed-ups that add named structure to ones that remove checks.** A precomputed view as its own type is safer than a skipped validation.
- **"Already proved above" stops being true when code moves.** If a check is removed, the invariant is stated where the check was, and ideally carried by a type.
- **On external input, use `checked_*` arithmetic and `.get()`** for offsets, lengths and cursor movement. Use `saturating_*` only where saturation is the documented meaning, never to hide an overflow.
- **Prepare once, query many.** Compile, normalise or index once into a named value (a compiled pattern set, a routing table), then reuse it. *Not when* the preparation costs more than the reuse saves, or the prepared value can go stale unnoticed.
- **Accumulate, then build.** Structures that can only be optimised when the whole batch is known (pattern sets, registries) collect their inputs, and per-item errors, then build once. Do not rebuild on every addition.
- **A builder is mutable; the configuration it produces is frozen** and cheap to share during execution.

### Benchmarks you can trust

- **State the conditions:** input sizes and distribution, toolchain, target, profile and features, machine. A number without them cannot be reproduced.
- **Check both versions return the same result** before comparing their speed.
- **Stop the optimiser deleting the work:** pass inputs and results through `std::hint::black_box`. A benchmark that reports a fraction of a nanosecond measured nothing.
- **Report spread, not one number.** Use `criterion` or `divan` for statistics, and look at the tail (p99) for latency, since an average hides it. Reproduce a result on a second run before acting.
- **Noise sources:** frequency scaling, other processes, cache warmth, allocator state, hash seeds, runtime start-up. For CI, instruction counts (`iai-callgrind`) are steadier than wall time.
- **A microbenchmark supports a claim about that operation on that machine.** Confirm with an end-to-end measurement before claiming the program is faster.
- **Let the measurement reject work.** The most useful result is often that the optimisation is unnecessary; keep the simpler code when the requirement is already met.

### Structural speed-ups

**Per-stage timings at the orchestration boundary.** A multi-stage pipeline takes one borrowed
options struct and returns how long each stage took, so a regression can be attributed.

```rust
pub struct SearchOptions<'a> {
    pub path: &'a Path,
    pub queries: &'a [String],
    pub language: Option<Language>,
    pub max_results: Option<usize>,
    pub timeout: Duration,
}

#[derive(Default)]
pub struct SearchTimings {
    pub query_preprocessing: Option<Duration>,
    pub file_searching: Option<Duration>,
    pub result_processing: Option<Duration>,
    pub total: Option<Duration>,
}
```

- `None` means the stage did not run, which is different from running in zero time.
- Options are typed: a `Duration`, not a bare `u64`; an enum, not a string. The struct holds what the pipeline needs and does not become a dumping ground for every flag in the program.
- Measure with `Instant`, never the wall clock. For anything finer than stages, use spans and a profiler instead of more fields.

**Parse once, plan once, evaluate many.** When one query is evaluated against many inputs,
build a plan up front: resolved term indices, required and excluded sets, and shortcut flags
such as "matches everything". The scan never walks the syntax tree again. *Not for*
single-shot evaluation, where the plan is pure overhead.

**Per-thread caches for worker state.** State that is expensive to build, mutable or not
`Send` (parsers, compiled queries, scratch buffers) is cached per worker thread, not behind
one shared `Mutex` that every worker queues on.

```rust
thread_local! {
    static PARSERS: RefCell<HashMap<Language, Parser>> = RefCell::new(HashMap::new());
}

fn with_parser<R>(
    language: Language,
    work: impl FnOnce(&mut Parser) -> R,
) -> Result<R, ParseSetupError> {
    PARSERS.with(|parsers| {
        let mut parsers = parsers.borrow_mut();
        let parser = match parsers.entry(language) {
            Entry::Occupied(slot) => slot.into_mut(),
            Entry::Vacant(slot) => {
                let mut parser = Parser::new();
                parser.set_language(&language.grammar())?;
                slot.insert(parser)
            }
        };
        Ok(work(parser))
    })
}
```

- Initialise lazily and return the construction error. `work` must not call `with_parser` again: the `RefCell` is borrowed, and the second borrow panics.
- The cache lives as long as the thread, and a pool has many threads, so memory is cache size times thread count. Bound it.
- **In async code a thread-local is not per task:** a task moves between worker threads at each `.await`. Use it only within one synchronous stretch, or in `rayon` and `spawn_blocking` work.
- A shared cache that must be shared is sharded (`dashmap`, or an array of locks indexed by hash), not one `Mutex<LruCache>`.
- *Not for* small single-threaded tools; it only complicates lifecycle and tests.

**The runtime chooses the representation.** When a step can run over a sparse or a dense form
(a frontier as a list or a bitmap), the shared runtime picks from a cheap estimate against a
threshold, not each algorithm. A bad threshold costs speed, never correctness. A flag forces
either mode, and a test runs both and compares results.

**Cache a stable yes-or-no at the call site.** When a hot path asks "is this enabled?" and
the answer changes only with configuration, cache it in an atomic so the path costs one
load. Every reconfiguration must run the rebuild, or sites stay wrongly on or off; test
reconfiguration after the sites exist. Logging and tracing crates already do this for level
checks. *Not when* the answer depends on per-record state.

**Slow side effects leave the hot path through a bounded channel.** Log and telemetry I/O
goes to a worker thread, and the constructor returns a guard whose `Drop` flushes.

```rust
let (writer, _guard) = tracing_appender::non_blocking(file);
// `_guard` lives to the end of scope. `let _ = ...` would drop it now and lose the logs.
```

- Choose the pressure policy and write it down: lossy (drops counted and exposed as a metric) or blocking (producers feel backpressure).
- Never for audit or transactional records, which must be durable before the program continues.

**Data larger than memory.**

- The decision sits beside the storage metadata: if the budget is smaller than the data, stream partitions; otherwise read it in.
- The algorithm is a callback over partitions the storage layer has already filtered, so "what to compute" stays apart from "how to stream". State what the callback may mutate: atomics, or partition-local state merged afterwards.
- **Memory mapping is not free.** It gives no crash-consistent writes, an I/O error arrives as a signal instead of a `Result`, and another process truncating the file is undefined behaviour, which is why creating a map is `unsafe`. It suits large read-only files you control. Not small files, and not files others may modify.

**Manual prefetching and similar micro-techniques** (staging a ring of independent lookups so
cache misses overlap) help only memory-bound pointer-chasing over large data. Keep the simple
path, and adopt the staged one only with benchmark evidence on the target CPUs; it can make
other machines slower.

### Allocating less

**Borrow when nothing changes; allocate only when something does.**

```rust
pub fn normalize_newlines(content: &str) -> Cow<'_, str> {
    if content.contains('\r') {
        Cow::Owned(content.replace("\r\n", "\n"))
    } else {
        Cow::Borrowed(content)
    }
}

pub fn mentions(content: &str) -> impl Iterator<Item = &str> {
    content
        .split_whitespace()
        .filter_map(|word| word.strip_prefix('@'))
}
```

- `Cow` pays off when the unchanged case is common. If nearly every input is rewritten, return `String` and keep the signature simple.
- Returning an iterator of borrowed slices lets the caller decide whether to collect at all.

**In order of how often they pay off:**

1. **Do not allocate in the loop.** Hoist the buffer out and `clear()` it each iteration; `clear` keeps the capacity.
2. **Reserve when the size is known:** `Vec::with_capacity`, `String::with_capacity`, `extend` from an exact-size iterator.
3. **Borrow instead of cloning:** take `&str` and `&[T]`, return slices or iterators, share with `Arc` when ownership really is shared.
4. **Avoid intermediate collections:** chain iterators instead of `collect` and then iterate again; `write!` into an existing `String` instead of `format!` and then `push_str`.
5. **Then, with a profile:** small-size-optimised containers, arenas, pools, a different global allocator.

```rust
let mut line = String::new();
while reader.read_line(&mut line)? != 0 {
    handle(line.trim_end());
    line.clear(); // keeps the allocation for the next line
}
```

- **A `match` on string literals is already compiled to efficient comparisons.** It needs no macro. For a large static lookup table, `phf` builds a perfect hash at compile time.

**A buffer pool, when reuse in place is not possible** (buffers handed between tasks). The
guard returns the buffer on drop.

```rust
pub struct PooledBuffer {
    buffer: Option<Vec<u8>>, // an Option so that Drop can take it
    pool: Weak<Pool>,        // a buffer that outlives the pool is simply freed
}

impl Drop for PooledBuffer {
    fn drop(&mut self) {
        if let (Some(mut buffer), Some(pool)) = (self.buffer.take(), self.pool.upgrade()) {
            buffer.clear();
            if buffer.capacity() <= MAX_RETAINED_CAPACITY {
                pool.put_back(buffer);
            }
        }
    }
}
```

- **A pool holds on to peak memory.** Cap both the number of buffers kept and the capacity of each, or one huge request pins that memory for the life of the process.
- Clear on return, so data from one request can never be read by the next.
- The allocator is already a good pool for small short-lived objects. Add a pool only when a profile shows allocation of large buffers is the cost.

**Inline small case, heap for the rest.** `SmallVec`, a small-string type, or an enum such
as `Inline(InlineData) | Heap(Arc<HeapData>)` keeps the common small case free of
allocation.

- Adopt after profiling shows allocation or cache misses dominate. An inline container is larger to move, and every access branches on which form it is; with the wrong inline size it is slower than `Vec`.
- Pin the size where it matters: `const _: () = assert!(size_of::<Node>() == 16);`.
- A layout change touches every copy, free and tag path. It is never a local edit.

**Permissive builder, compact final form.** Accept entries in any order (edges, sparse
triplets), then convert once to a compressed form: count per row, prefix-sum to offsets,
fill one contiguous array, merging duplicates in that pass. Lookups then read one cache-
friendly array instead of chasing a `Vec<Vec<T>>`. The converting constructor is fallible
for untrusted input; it does not `assert!`.

**Dense internal ids.** Map external keys (strings, sparse numbers) to `0..n` at the input
boundary, run the kernel on plain arrays indexed by id, and map back at the output. The
mapping never leaks into the kernel. "No result" is `Option`, or one named sentinel
constant where the array's size matters.

**Scoped memory accounting.** A child tracker forwards each `allocate(bytes)` to its parent
and remembers the total; on drop it releases the total in one call. A query or a collection
is then accounted for without tracking each element.

```rust
pub struct ScopedTracker<'parent> {
    parent: &'parent Tracker,
    tracked: usize,
}

impl ScopedTracker<'_> {
    pub fn allocate(&mut self, bytes: usize) -> Result<(), OutOfBudget> {
        self.parent.allocate(bytes)?;
        self.tracked += bytes;
        Ok(())
    }
}

impl Drop for ScopedTracker<'_> {
    fn drop(&mut self) {
        self.parent.release(self.tracked);
    }
}
```

- The budget check happens before the allocation it accounts for, and running out is an error the query can report, not an abort.

### Without a heap

**Capacity is a const generic, and running out is an error.** In `no_std`, embedded or
deterministic code, storage is on the stack or static, and every write that could exceed it
returns a structured error.

```rust
pub struct FixedBuffer<const N: usize> {
    buffer: [u8; N],
    length: usize, // invariant: length <= N
}

impl<const N: usize> FixedBuffer<N> {
    pub fn write_bytes(&mut self, bytes: &[u8]) -> Result<(), CapacityExceeded> {
        let remaining = N - self.length;
        if bytes.len() > remaining {
            return Err(CapacityExceeded {
                needed: bytes.len(),
                available: remaining,
            });
        }
        self.buffer[self.length..self.length + bytes.len()].copy_from_slice(bytes);
        self.length += bytes.len();
        Ok(())
    }
}
```

- **A failed write leaves the buffer unchanged.** Check first, then mutate.
- The error says how much was needed and how much was available.
- If `as_str()` relies on the contents being UTF-8, every write path preserves that and never splits a multi-byte character; a `write_str` that takes `&str` and writes all or nothing does.
- Implement `core::fmt::Write` so `write!` works.
- Prefer `heapless` (`Vec`, `String`, queues, maps) or `arrayvec` to writing these by hand.
- **A large `[T; N]` lives wherever its owner does.** On the stack, a big `N` overflows it, and moves copy all `N` elements; put large fixed storage in a `static` or behind a reference.
- When allocation is acceptable, use `Vec` and `String`. Fixed capacity is a constraint to satisfy, not an optimisation to reach for.

### Arenas, drops and the allocator

**An arena's lifetime matches one phase of work.** Many small allocations that die together
(one file's syntax tree, one request's scratch data) go into a bump arena such as
`bumpalo::Bump`, which is reset at the phase boundary and reused.

- Name the owning phase. Nothing arena-backed escapes it; the `&'bump` borrow enforces that.
- **A bump arena does not run destructors** for what it holds unless you use its owning `Box`. Keep plain data in it, not types that own files, locks or heap memory.
- **A long-lived arena is a leak in disguise.** It grows to the largest workload it has seen and frees nothing until reset.
- *Not for* objects with independent lifetimes, or data that must outlive the phase.

**Move an expensive drop off the latency-critical thread.** When freeing a large structure
(a deep tree, a big index) stalls a UI or request thread, send the value to a long-lived
background thread that only receives and drops.

```rust
// Fails only if the background thread is gone; then the value drops here, as before.
let _ = self.drop_queue.send(std::mem::take(&mut self.tree));
```

- *Not for* a resource that must be released before the next step (a lock, a file another process waits on). Confirm with a profile that the drop was the stall.
- A deep recursive structure can also overflow the stack while dropping. Write an iterative `Drop`, or hold the nodes in a `Vec` or arena.

**The global allocator** is changed only when allocation is a measured bottleneck, typically
a multi-threaded server with many small allocations.

```rust
#[global_allocator]
static GLOBAL: mimalloc::MiMalloc = mimalloc::MiMalloc;
```

- Measure throughput, tail latency and resident memory before and after; an allocator can win on speed and lose on memory. Only a binary sets it, never a library.

**Build settings.**

```toml
[profile.release]
lto = "thin"        # "fat" for a little more speed and much longer builds
codegen-units = 1   # better optimisation, slower builds
panic = "abort"     # smaller and slightly faster; only if nothing relies on unwinding
```

- These trade build time for run time. Measure the gain; on I/O-bound programs it is often nil. Keep them out of the dev profile.
- **`panic = "abort"` changes behaviour:** no `catch_unwind`, no destructors on panic, and one panicking task ends the whole server.
- **`target-cpu=native` makes a binary that may crash on other machines.** Use it only when you build on, or for, the machine that runs it. Otherwise detect features at run time (`is_x86_feature_detected!`).
- **`#[inline]` matters for small functions called across crates,** which cannot otherwise be inlined without LTO. Generic functions already can be. `#[inline(always)]` is for measured cases only; applied widely it bloats code and slows it down. `#[cold]` on error paths is the cheaper hint.
- Profile-guided optimisation (`cargo-pgo`) is worth setting up for a long-lived hot binary with a representative workload, and not before.

### Caches

**A cache is a correctness risk bought for speed.** Before adding one, state the key, what
invalidates an entry, the size bound and what a stale read costs.

- **Bound it:** a maximum size, usually a time to live as well. An unbounded map used as a cache is a memory leak. `moka` for a concurrent cache with eviction; a `HashMap` or `lru` behind the owner's lock for a small one.
- **The key contains every input that changes the answer.** Tenant, authorisation scope, locale, version, options. A key that omits the user serves one user's data to another.
- **Never cache what is not a pure function of the key** unless staleness is accepted and bounded.
- **Policy is part of a cache's identity.** Settings that change validity (time to live, capacity, persistence, scope) belong in the type or key that decides whether an existing cache may be reused.
- **Negative results are cached separately,** with a shorter life: "not found" goes stale as soon as the thing is created.
- **Many concurrent misses for one key should compute once.** Use the cache's get-or-insert-with, or single-flight, not a check followed by an insert.
- **Measure the hit rate.** A cache that rarely hits costs memory, locking and complexity for nothing.
- A process-wide cache needs an invalidation path, and tests need a way to start with it empty.

**Build-style cache keys come from every semantic input.**

```rust
let mut entries: Vec<_> = fs::read_dir(dir)?.collect::<Result<_, _>>()?;
entries.sort_by_key(|entry| entry.file_name()); // traversal order must not change the key
for entry in entries {
    hasher.update(b"file\0");
    hasher.update(entry.file_name().as_encoded_bytes());
    hasher.update(b"\0");
    hasher.update(&fs::read(entry.path())?);
}
```

- Hash the tool version, the input contents, the options and each environment setting that affects output. Separate fields with a tag and a delimiter, so `("ab", "c")` and `("a", "bc")` differ.
- **Size and modification time may shortcut re-reading an unchanged file; they are never the identity.**
- Use a stable hash (BLAKE3, SHA-256) for anything persisted. `DefaultHasher` is not stable across Rust versions.
- Namespace cached output by the producer's version, write with a temporary file and an atomic rename, treat an unreadable entry as a miss, and keep a `--force` or `--no-cache` escape hatch.
- **Invalidate by interface when that is what dependants use.** Hash the sorted public facts (names, signatures, imports) and classify a change as none, cosmetic or structural. The hash ignores bodies by design; add behaviour inputs explicitly if they matter.
- **Cache a compiled intermediate form** (a lowered plan, a compiled template) with `OnceLock` or a keyed cache, and know what invalidates it before the source is allowed to change.

### Bulk data

- **Per-thread worker state in `rayon`:** `for_each_init` or `map_init` builds the non-thread-safe state per worker split; shared immutable data goes in an `Arc`.

```rust
let outcomes: Vec<(usize, Result<(), ProcessError>)> = files
    .par_iter()
    .enumerate()
    .map_init(
        || Highlighter::with_store(Arc::clone(&store)), // per worker, not per item
        |highlighter, (index, path)| (index, process(highlighter, path)),
    )
    .collect();
```

- Return per-item results and report them from one place. Printing from inside workers interleaves output and loses the count of failures.
- **Parallel export with one sink per chunk** works only where independent output chunks are acceptable. Where order or one transaction is required, keep a single ordered writer.
- **Batch writes by statement shape,** not only by count, so each batch is one prepared statement. Parallel batches each need their own connection and a first-error policy.
- **An append-only chunk writer** reuses one buffer, writes a placeholder header, streams records through the compressor and checksum, backfills length and checksum, and issues one `write_all`. Shrink the buffer after an unusually large batch. A round-trip reader test accompanies every format change.
- **Columnar engines** (Polars, Arrow with DataFusion): use the lazy or SQL API so the engine can plan, push filters down and stream. Do not convert columns to row structs early; that discards the vectorisation you adopted the engine for. Fix the query plan before tuning thread or memory settings.

### Derived data, hashing and streaming input

**Derived data cached on its owner has one invalidation function.** Derived facts (a
transpose, degree counts, a sorted flag) are computed lazily and reused.

```rust
pub struct Graph {
    edges: Vec<Edge>,              // private: mutated only through methods below
    degrees: OnceCell<Vec<u32>>,
    is_symmetric: Option<bool>,    // None means "not yet known"
}

impl Graph {
    pub fn add_edge(&mut self, edge: Edge) {
        self.edges.push(edge);
        self.invalidate_derived();
    }

    fn invalidate_derived(&mut self) {
        self.degrees = OnceCell::new();
        self.is_symmetric = None;
    }
}
```

- The base field is private and every mutating method calls the one invalidation function. A stale derived fact gives wrong answers silently, so this is not left to each caller.
- "Not computed" and "unknown" are explicit (`Option`, a three-state enum), never a default that looks like an answer.
- *Not when* the base changes on nearly every operation: recompute, or maintain the fact incrementally.

**Canonical hashing of structured values.** Raw bytes hash directly. A structured value is
hashed in a canonical form: object keys sorted, only identity-bearing fields included,
arrays left in order when order has meaning.

- Write down which fields define identity before adding the hash.
- Test both directions: the same content in another key order gives the same hash, and different content of the same shape gives a different one. Over-normalising merges distinct inputs; under-normalising causes needless misses.
- **Canonicalise floats used as keys:** `-0.0` and `0.0` compare equal but have different bits, and NaN has many bit patterns and equals nothing. Normalise both before hashing, or do not key on floats.

**On-disk caches of regenerable results.**

- The cache version combines a hand-bumped schema number with the package version; a mismatch means start empty. Any change to what is stored bumps the schema number in the same commit.
- A missing, truncated or unreadable entry is a miss, never an error. The cache can always be deleted.
- **A key is validated so that it cannot be a path:** no separators, no `..`. Better, name files by the hex hash of the key.
- A small index stays in memory; payloads load on demand.

**Stream a large top-level JSON array** one element at a time instead of deserialising the
whole document. With `serde`, a `Visitor` whose `visit_seq` handles each element as it
arrives does this without hand-parsing brackets and commas:

```rust
struct ForEach<F>(F);

impl<'de, F: FnMut(Record)> Visitor<'de> for ForEach<F> {
    type Value = usize;

    fn expecting(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str("an array of records")
    }

    fn visit_seq<A: SeqAccess<'de>>(mut self, mut seq: A) -> Result<usize, A::Error> {
        let mut count = 0;
        while let Some(record) = seq.next_element::<Record>()? {
            (self.0)(record);
            count += 1;
        }
        Ok(count)
    }
}

let mut deserializer = serde_json::Deserializer::from_reader(BufReader::new(file));
let count = deserializer.deserialize_seq(ForEach(|record| sink.push(record)))?;
```

- `serde_json`'s `StreamDeserializer` (`into_iter`) handles concatenated or newline-separated values, not a comma-separated array. If you control the format, newline-delimited JSON is simpler to stream, append to and resume.
- Wrap the reader in a `BufReader`, and make errors name the element index.
- *Not when* validation needs the whole document before any element may be acted on.

**A prefilter may give false positives and never false negatives.** A cheap test in front of
an expensive match can say "maybe" wrongly; it can never say "no" wrongly.

- Decide what "cannot translate this condition" means before writing the combinators. In an `And`, an untranslatable term is dropped: fewer conditions still admit every real match. In an `Or`, one untranslatable branch makes the whole `Or` unknown, because dropping the branch would drop real matches.
- An evaluation error in the prefilter counts as "maybe".
- Test it as a property: everything the full matcher accepts, the prefilter also accepts.

**Greedy selection under a budget.**

```rust
scored.sort_by(|a, b| b.score.total_cmp(&a.score).then_with(|| a.id.cmp(&b.id)));

let mut used = 0;
let mut selected = Vec::new();
for candidate in scored {
    if used + candidate.cost <= budget {
        used += candidate.cost;
        selected.push(candidate);
    }
}
```

- `f64::total_cmp` gives a total order that tolerates NaN; `partial_cmp().unwrap()` panics on it. The tie-break makes the selection deterministic.
- An item that does not fit is skipped and a smaller later one may still fit. This is a heuristic, not optimal packing; say so, and return the amount used.

**Caches that own live resources.**

- **A manager owns expensive open handles** (files, sessions): a bounded LRU, its lock, and close-on-evict. The key includes every argument that distinguishes handles (path, mode, options). Callers never close what the manager gave them.
- **Eviction of an async resource only signals stop,** because eviction is synchronous and clean-up is not. Each session runs in a task that holds its resources and waits for the signal. Shutdown makes an explicit pass that awaits every such task; fire-and-forget eviction is not a shutdown guarantee.
- **A cache addressed by two keys** keeps the forward and reverse maps in one struct and updates both in every add, move, remove and clear.
- **A shortened hash used as an identifier can collide.** Detect it; do not assume it away.
- **A fixed table of `OnceLock` indexed by a small parameter space** is a cache bounded by construction.

**Smaller rules.**

- **Hidden reordering stays hidden.** A batching optimisation that reorders its inputs (sorting by length to reduce padding) restores the original order before returning.
- **A per-call override is a parameter.** Pass `top_k` with the request or apply it to a per-request copy. Never mutate a shared component and restore it afterwards: concurrent requests race, and an early return leaves it changed.
- **Variants are chosen by exact identifier,** not by substring match with a silent default.
- **A long batch run checkpoints each finished unit** under a deterministic key, written with a temporary file and a rename, and skips saved keys on resume. Replacing a unit that failed for infrastructure reasons is a separate, explicit operation.
- **Randomness is injected** (`&mut impl Rng`, or a seed that is logged), so a run can be reproduced.
- **At the boundary of a typed kernel,** match on the type tag once and downcast inside the arm that proved the type, not repeatedly in the inner loop.
- **In an incremental framework** (`salsa`), every changing fact is a typed input, and each new query is checked for what invalidates it: one query that reads global data makes everything recompute. A tool that runs once and exits needs no such framework.
- **When several ranking signals are fused,** keep each signal's contribution on the result so the ranking can be explained and tuned. Demote with a negative signal instead of excluding.
- **A vector index compares like with like.** Inner product equals cosine similarity only for normalised vectors, so never mix normalised and unnormalised embeddings. Never hold the index lock across the call that computes an embedding.

### Numbers you state

- **State the gate before measuring, and report a miss plainly.** Write the threshold down first. If the run misses it, the headline says so. A feature that fails its gate ships off by default, or not at all.
- **A projected number is labelled a projection,** with the measurement that would confirm it. An estimate written like a result will be quoted as one.
- **A performance figure names its conditions:** build profile, machine, input, warm or cold, tool version. A debug-build number says nothing about release.
- **A size or cost reduction is reported with the quality it kept.** A smaller context or a faster search with unmeasured recall is not a result.
- **One or two inputs do not support a general claim.** Say how many were used and which.
- **A later result that contradicts an earlier one supersedes it visibly.** Mark the earlier document superseded; do not delete it.
- **A backtest uses only what was known at the time.** Evaluate each historical case at its own commit, and exclude signals that leak the answer.
- **A memory benchmark says which lifetime it measures.** Constructing the object fresh per iteration shows the peak a batch job would cause; reusing it shows steady state. Report allocations and peak memory, not only time.
- **Inputs that once caused a failure stay as benchmark inputs:** the huge literal, the deep nesting, the very long function.
- **A benchmark file says how to run it:** the command and features in its header, fixtures built outside the timed closure, one named case per input shape, and `Throughput::Bytes` when sizes differ so results compare as bytes per second.
- **Benchmark settings are documented environment variables, parsed once.** A malformed value is an error naming the variable, not a panic in a lazy static. Generator parameters are named constants shared with the benchmark.
- **A count names its unit and method.** A token count names its tokenizer; a line count says whether blanks and comments are included.
- **A report opens with tool version, input and totals,** so two runs can be compared.

Two last structural notes for this section:

- **Order conditions cheap and selective first.** Test the inexpensive predicate that rejects most inputs before a regex or a parse.
- **A sparse set** gives constant-time insert, membership and clear over a bounded integer universe: a dense vector of members plus a vector mapping value to dense index. It beats a bitmap that must be cleared between many small sets. Adopt it on a measurement from the real workload.

## Collections, sharing and iterators

- **`IndexMap` removal:** `swap_remove` is O(1) and breaks insertion order; `shift_remove` keeps it and is O(n). Choose deliberately; plain `remove` is deprecated for this reason.
- **Never change a key in place** in a way that alters its hash or order (through interior mutability). The entry becomes unfindable. Remove, change, reinsert.
- **`BinaryHeap::from(vec)` builds in O(n);** pushing n items one at a time is O(n log n). For the k largest of a stream, keep a min-heap of size k rather than sorting everything. For the k largest of a slice, `select_nth_unstable` is linear.
- **A min-heap, or a heap over floats, needs an explicit total order.** `Reverse(x)` flips a key that is already `Ord`. For floats, define the order with `total_cmp` and add a tie-break so equal priorities pop in a deterministic order.

```rust
struct Candidate {
    cost: f64,
    node: NodeId,
}

impl Ord for Candidate {
    fn cmp(&self, other: &Self) -> Ordering {
        other
            .cost
            .total_cmp(&self.cost) // reversed: the smallest cost is popped first
            .then_with(|| self.node.cmp(&other.node))
    }
}
impl PartialOrd for Candidate {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}
impl PartialEq for Candidate {
    fn eq(&self, other: &Self) -> bool {
        self.cmp(other) == Ordering::Equal
    }
}
impl Eq for Candidate {}
```

  All four traits agree because three are defined from `cmp`. A derived `PartialEq` on a float beside a hand-written `Ord` disagrees on NaN and on signed zero, and collections misbehave quietly when they disagree.
- **Packed bits:** `Vec<bool>` spends a byte per flag, which is fine for small sets. For large bitmaps or wire layouts use `bitvec` or a fixed-size bitset, with bit order and storage type written out (`BitVec<u8, Msb0>`).
- **A read-mostly shared map** is best published as an immutable snapshot: `ArcSwap<HashMap<K, V>>` (or `RwLock<Arc<HashMap<K, V>>>`), where a writer builds a new map and swaps it in. Readers never block and always see a consistent whole. For many concurrent writers, a sharded map such as `DashMap`; do not hold one of its references while touching the same map again, which can deadlock on the shard lock.
- **`SmallVec<[T; N]>`** avoids the heap when a small bound usually holds. It makes the value larger and every access branch; adopt it from a profile, not from a hunch.

**Edit-heavy, then read-heavy: two types.** Mutations go into a builder; an explicit
`finish(self) -> Frozen` sorts, deduplicates and computes totals; read-optimised algorithms
take only `Frozen`. A convention that says "call `update()` before reading" will be broken;
the type cannot be. *Not for* data where every mutation must be visible at once.

**Compressed sparse row layout for a static graph.** Neighbours of `u` are a contiguous
slice, which is cache-friendly and trivially partitioned for parallel work.

```rust
pub struct Csr {
    offsets: Vec<usize>, // length: vertices + 1
    targets: Vec<u32>,
}

impl Csr {
    pub fn neighbours(&self, u: usize) -> &[u32] {
        &self.targets[self.offsets[u]..self.offsets[u + 1]]
    }
}
```

- The constructor checks the invariants once: `offsets.len() == vertices + 1`, offsets never decrease, the last equals `targets.len()`, and every target is a valid vertex. Every reader then relies on them.
- Rebuild for large updates; in-place insertion is O(edges). For a graph that changes constantly, use adjacency lists.

**Values and validity in parallel buffers, for columnar data.** A null still advances the
value buffer by one slot, so both buffers always have the same length and position `i` means
the same row in each. For anything small, `Vec<Option<T>>` is simpler and right.

- **NaN in a priority is usually a bug upstream.** `total_cmp` gives it a place in the order, which keeps the heap consistent but can hide a bad cost calculation. Where NaN should not occur, reject it when the value is created.

**Intern immutable values that repeat heavily.** One canonical `Arc<str>` per distinct value
saves memory and makes clones cheap.

```rust
#[derive(Default)]
pub struct Interner {
    seen: Mutex<HashSet<Arc<str>>>,
}

impl Interner {
    pub fn intern(&self, text: &str) -> Arc<str> {
        let mut seen = self.seen.lock().unwrap_or_else(PoisonError::into_inner);
        if let Some(existing) = seen.get(text) {
            return Arc::clone(existing);
        }
        let value: Arc<str> = Arc::from(text);
        seen.insert(Arc::clone(&value));
        value
    }
}
```

- **Pointer equality (`Arc::ptr_eq`) is valid only if every value of the type comes from the interner.** Enforce that with a newtype whose only constructor is `intern`; otherwise compare contents.
- **An index handle** (`Symbol(u32)` into a table) is `Copy`, four bytes and trivially hashable. It is meaningful only with its table; never compare or serialise symbols from different tables.
- **Never hand out `&'static T` into a `Vec<T>` that can grow.** Growth moves the items. Store `Box` or `Arc` per item, use an arena with stable addresses, or return a clone.
- **The table only grows.** Do not intern unbounded or attacker-controlled input without a cap or scoped lifetime. Evicting by reference count is racy unless done under the table's lock.
- *Skip interning* for values that rarely repeat or are short-lived: it adds a lock and a hash to every construction.

**Deduplicate live resources by canonical identity, holding `Weak`.** A registry of open files
or connections is keyed by the canonical form (absolute path, case-folded where the platform
is case-insensitive) and stores `Weak` references, so it does not keep anything alive. A
failed `upgrade()` removes the entry. A second open with conflicting options is an error, not
a silent share.

**Borrowed or owned, without a `Clone` bound.** `Cow` needs `ToOwned`. For a value that is
sometimes borrowed from a larger structure and sometimes built on demand, and is not
cloneable, a two-variant enum with `Deref` gives one API instead of two.

```rust
pub enum MaybeOwned<'a, T> {
    Owned(T),
    Borrowed(&'a T),
}

impl<T> Deref for MaybeOwned<'_, T> {
    type Target = T;

    fn deref(&self) -> &T {
        match self {
            Self::Owned(value) => value,
            Self::Borrowed(value) => value,
        }
    }
}
```

**Smaller rules.**

- **An RAII guard acquires in its constructor and releases in `Drop`.** Bind it to a name (`let _guard = ...`); `let _ = ...` drops it at once.
- **A handle with several ownership states** (cached, owned, borrowed, transferred) is one type with a state enum and a single release path in `Drop`.
- **A resumable handle checks that it is still valid in every method that advances it,** not only at construction; a stale handle returns a clear error.
- **A point-in-time snapshot is handed out as an iterator or guard that releases on drop,** so callers never manage the underlying commit handle. An empty store yields an empty iterator, not an error.
- **Which wrapper:** `Cow` when the borrowed value may need changing; `MaybeOwned` when the type cannot be cloned; `Arc` when ownership is really shared; a plain owned value when handing it over is the point.

**Accept `impl IntoIterator`, return `impl Iterator`.**

```rust
pub fn total_len<'a>(names: impl IntoIterator<Item = &'a str>) -> usize {
    names.into_iter().map(str::len).sum()
}

pub fn active(users: &[User]) -> impl Iterator<Item = &User> + '_ {
    users.iter().filter(|user| user.active)
}
```

- The caller can pass a `Vec`, a slice, a set or another iterator, and decides whether to collect the result.
- A returned iterator is lazy: nothing happens until it is consumed, and it borrows its source until then. Say so in the docs when the work is expensive or has effects.
- `Box<dyn Iterator>` when the concrete type differs by branch or must be stored. The cost is an allocation and a virtual call per item; it matters only in inner loops.
- **Do not build intermediate `Vec`s** between stages, and do not `collect` only to iterate again.
- Implement `FromIterator` for a custom collection so `collect()` works, and `Extend` so it can be appended to.
- **Do not call `next()` after `None` unless the iterator is fused.** Call `.fuse()` if the code might; make your own iterators fused when that is cheap, and implement `FusedIterator` to say so.
- Implement `DoubleEndedIterator` only where going backwards is natural, and test that `next` and `next_back` meet in the middle without overlap.

**Closure bounds: ask for the least you need.**

| You will call it | Ask for | Callers may pass |
|---|---|---|
| At most once | `FnOnce` | any closure, including one that consumes its captures |
| Several times, one at a time | `FnMut` | closures that mutate their captures |
| Several times, possibly at once or through `&` | `Fn` | closures that only read |

- Asking for `Fn` when you call once rejects closures for no reason.
- A closure sent to a thread or task is `move`, and its captures must be `Send + 'static`. Clone the `Arc` outside the closure and move the clone in.
- Do not require `'static` or `Send` from a callback that is only called before the function returns.

**A lending iterator, when items must borrow from the iterator itself.** A cursor that
decodes into its own buffer cannot be a standard `Iterator`, whose items must outlive the
next call. A generic associated type expresses the loan:

```rust
pub trait LendingIterator {
    type Item<'a>
    where
        Self: 'a;

    fn next(&mut self) -> Option<Self::Item<'_>>;
}
```

- The previous item must be dropped before the next call, which is exactly the constraint the buffer needs. The price: no `for` loop (use `while let`), none of the standard adapters, and no `dyn`.
- *First ask* whether returning owned items is fast enough, or whether a callback (`for_each(|row| ...)`) would do. Both are simpler.
- Never fake it by extending a lifetime with `unsafe` to fit `Iterator`. That is a use-after-free as soon as a caller collects.

**An iterator that owns a resource releases it on every path.** Exhaustion, an error, an
explicit close and an early drop all reach one idempotent clean-up.

```rust
pub struct Rows {
    cursor: Option<Cursor>,
}

impl Rows {
    fn release(&mut self) {
        if let Some(cursor) = self.cursor.take() {
            cursor.close();
        }
    }
}

impl Iterator for Rows {
    type Item = Result<Row, DbError>;

    fn next(&mut self) -> Option<Self::Item> {
        let cursor = self.cursor.as_mut()?;
        match cursor.advance() {
            Ok(Some(row)) => Some(Ok(row)),
            Ok(None) => {
                self.release();
                None
            }
            Err(error) => {
                self.release();
                Some(Err(error))
            }
        }
    }
}

impl Drop for Rows {
    fn drop(&mut self) {
        self.release();
    }
}
```

- Releasing on exhaustion alone leaks when the caller stops early (`.take(10)`, `?` in the loop body). `Drop` covers that.
- After an error the iterator yields `None`, so a caller who ignores the error cannot loop forever.
- If closing can fail and the failure matters, offer `close(self) -> Result<()>` as well; `Drop` can only log.

## Threads and CPU parallelism

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

**Lock ranks, checked in debug builds.** When a component has more than a handful of locks,
"one documented order" stops being checkable by reading. Give each lock a rank and assert on
every acquisition that it is higher than every rank the thread already holds.

```rust
#[cfg(debug_assertions)]
thread_local! {
    static HELD: RefCell<Vec<LockRank>> = const { RefCell::new(Vec::new()) };
}

pub struct RankedMutex<T> {
    rank: LockRank,
    inner: Mutex<T>,
}

pub struct RankedGuard<'a, T> {
    guard: MutexGuard<'a, T>,
    rank: LockRank,
}

impl<T> RankedMutex<T> {
    pub fn lock(&self) -> RankedGuard<'_, T> {
        // Checked before blocking, so a violation panics instead of deadlocking.
        #[cfg(debug_assertions)]
        HELD.with(|held| {
            let mut held = held.borrow_mut();
            assert!(
                held.iter().all(|other| *other < self.rank),
                "lock order violation: {:?} taken while holding {:?}",
                self.rank,
                held
            );
            held.push(self.rank);
        });
        RankedGuard {
            guard: self.inner.lock().unwrap_or_else(PoisonError::into_inner),
            rank: self.rank,
        }
    }
}

impl<T> Drop for RankedGuard<'_, T> {
    fn drop(&mut self) {
        #[cfg(debug_assertions)]
        HELD.with(|held| {
            let mut held = held.borrow_mut();
            if let Some(position) = held.iter().rposition(|other| *other == self.rank) {
                held.remove(position);
            }
        });
    }
}
```

- The check fires on the first run that takes locks in a bad order, even when no deadlock happens that time. That is its whole value: a deadlock needs an unlucky interleaving, a rank violation does not.
- Every lock gets a rank when it is added. One unranked lock makes the check meaningless.
- It is per-thread, so it does not see a guard held across `.await` on another thread; that case is already forbidden.
- For two or three locks, a comment stating the order is enough.

**Per-thread accumulators, one merge.** A counter, map or histogram updated inside a parallel
loop becomes one accumulator per worker, merged at the end, instead of a lock or atomic
touched on every iteration.

```rust
let histogram = items
    .par_iter()
    .fold(Histogram::default, |mut local, item| {
        local.record(item);
        local
    })
    .reduce(Histogram::default, Histogram::merge);
```

- The identity must be a true identity and the merge associative. `rayon` splits the work differently on each run, so a merge that depends on grouping gives different answers on different runs. Floating-point sums are the usual trap: they are not associative, so parallel totals differ in the last bits.
- *Not when* updates need one global order.

**Index-stealing workers** are the dependency-free form of the same thing: a shared atomic
"next index" hands each item out exactly once and balances uneven items without pre-split
ranges.

```rust
let next = AtomicUsize::new(0);
let per_worker: Vec<Vec<(usize, Output)>> = thread::scope(|scope| {
    let handles: Vec<_> = (0..workers)
        .map(|_| {
            scope.spawn(|| {
                let mut local = Vec::new();
                loop {
                    let index = next.fetch_add(1, Ordering::Relaxed);
                    let Some(item) = items.get(index) else { break };
                    local.push((index, process(item)));
                }
                local
            })
        })
        .collect();
    handles
        .into_iter()
        .map(|handle| handle.join().expect("worker panicked"))
        .collect()
});
```

- Results carry their index and are sorted after the merge when order matters. `Relaxed` is correct here: `fetch_add` is atomic, and nothing else is published through the counter.
- Run serially when there are few items or one worker. Not for dependent jobs or ordered execution.

**Smaller rules.**

- **Write the algorithm against an execution policy** with a sequential and a parallel adapter over the same body. Tests run the sequential one, which separates "the algorithm is wrong" from "the scheduling is wrong". Abstract the execution, never the data model.
- **Chunked CPU work** sizes chunks as `ceil(items / threads)` clamped to a minimum and maximum, and gives each worker a stable index for its scratch buffers. **Cancellation stops pulling new chunks;** discarding results while the work continues is not cancellation.
- **Parallel workers, one writer.** Workers send whole results to a single thread that owns the `BufWriter`, so output lines never interleave.
- **A metric or timer guard records in `Drop`,** so early returns and `?` are covered. Held across an `.await`, it also times the suspension, which may or may not be what you want to measure.
- **An `accept` error does not end the server.** Log it and continue, with a short pause on resource exhaustion (`EMFILE`) so the loop does not spin. Only a bind failure is fatal. Each connection is handed off under a concurrency bound, so one slow client cannot block the next accept.
- **A lock held in a database row** for long background work records the owner, what is locked and a heartbeat the holder refreshes, so a stale lock can be detected and explained. A constraint enforces the single row. It is a single-host convenience, not a distributed lock.
- **State for a callback whose signature cannot carry it** may go in a `thread_local!` `RefCell`, set before the call and read inside. Keep borrows short and never hold `borrow_mut` across a call that may re-enter. Valid only while the whole call runs on one thread.

## Atomics, locks and shared resources

**A read followed by a write is not atomic, whatever the orderings.**

```rust
// Lost update: two threads can both read 5 and both store 6.
let current = counter.load(Ordering::Acquire);
counter.store(current + 1, Ordering::Release);

// One atomic operation.
counter.fetch_add(1, Ordering::Relaxed);

// A conditional update: retry until no one else changed it in between.
let mut current = high_water.load(Ordering::Relaxed);
while candidate > current {
    match high_water.compare_exchange_weak(
        current,
        candidate,
        Ordering::Relaxed,
        Ordering::Relaxed,
    ) {
        Ok(_) => break,
        Err(actual) => current = actual,
    }
}
```

- Use the single-operation forms: `fetch_add`, `fetch_max`, `fetch_update`, `swap`, `compare_exchange`. Orderings govern what other memory becomes visible; they do not join two operations into one.
- `compare_exchange_weak` may fail spuriously and belongs in a loop; the strong form is for a single attempt.
- **A fence or an atomic store does not make plain data shareable.** Non-atomic mutable state reached from two threads needs a lock or an atomic of its own, or it is a data race and undefined behaviour.
- **Do not hand-roll a spin lock, a lock-free queue or memory reclamation.** Use `Mutex`, `crossbeam`'s queues and deques, `crossbeam-epoch` for deferred reclamation, and `AtomicCell` for a small `Copy` slot. Freeing a node another thread may still be reading is the classic lock-free bug, and it passes most tests.
- **Lock-free is not automatically faster.** An uncontended mutex costs a few nanoseconds. Go lock-free only when a profile shows contention on that lock, and after trying to shrink the critical section, shard the data, or give each thread its own copy.
- A `loom` test joins its threads and asserts the invariant; without the assertion it checks nothing. No timers, randomness or I/O inside the model.
- `std::sync::OnceLock` and `LazyLock` replace `lazy_static!` and most of `once_cell`; reach for the crates only to support an older toolchain.
- **Several keyed locks are taken in one global order.** Sort the keys, lock in that order, keep the guards together and release them together. No call site picks its own order. Striped locks cap the number of locks at the price of unrelated keys sharing a stripe.
- **`rayon` for CPU-bound loops over large collections.** Items must be independent, with no locks and no I/O inside. Do not parallelise tiny tasks: below roughly a microsecond of work per item, the scheduling overhead wins. Measure the speed-up; memory-bound loops often do not scale.
- **A hand-built work-stealing pool** (a global injector plus a deque per worker, from `crossbeam-deque`) is for building a scheduler. Application code should use `rayon` or the async runtime, which already are one.
- **Double-buffered work sets.** An iterative scheduler keeps a current and a next set and swaps them at the start of each round (`mem::swap(&mut current, &mut next); next.clear();`), so work scheduled during a round cannot change the set being consumed, and both allocations are reused.
- **The scheduler owns the cross-cutting concerns:** dependency order, timeouts, error propagation and removal of failed work. A task exposes `run` and its dependencies; it does not start its dependents itself.
- **An engine with user callbacks** owns loading, scheduling and iteration; user code implements a trait with one required method and a few defaulted hooks. Add a hook only when an algorithm needs it: an empty default can hide a step that an implementer should have handled.

**One key, two states: connecting and connected.** When a miss starts slow async set-up, the
map holds both states under the key, and the decision is taken under the lock as a plain
value. All awaiting happens after the guard is gone.

```rust
enum Slot {
    Connecting(watch::Receiver<()>),
    Connected(Arc<Tunnel>),
}

enum Action {
    Use(Arc<Tunnel>),
    Wait(watch::Receiver<()>),
    Connect(watch::Sender<()>),
}

let action = match self.slots.lock().expect("slot map poisoned").entry(key.clone()) {
    Entry::Occupied(slot) => match slot.get() {
        Slot::Connected(tunnel) => Action::Use(Arc::clone(tunnel)),
        Slot::Connecting(ready) => Action::Wait(ready.clone()),
    },
    Entry::Vacant(slot) => {
        let (done, ready) = watch::channel(());
        slot.insert(Slot::Connecting(ready));
        Action::Connect(done)
    }
};
// The guard ended with the statement above.
```

- **If the connecting caller fails or is cancelled, a drop guard removes the `Connecting` entry.** Without it, every waiter waits for ever. This is the part most often missed.
- **Waiters look the key up again after being woken;** the attempt may have failed and the entry gone.
- The entry is removed when its last user releases it, or by an idle timeout.
- *Do not share* when callers need separate credentials, quotas or independent cancellation.

**A `Mutex<()>` can serialise an external side effect.** For "download once, then everyone
reads", probe without the lock, take the lock, probe again, then do the work. The second probe
is what makes concurrent first use perform one download. In a service, bound the wait with a
timeout, since the lock hides a long operation.

**Never run a callback while holding your own lock.** A timer or delayed-task scheduler keeps
a heap of due times (`BinaryHeap<Reverse<(Instant, TaskId)>>`) under a mutex that guards only
the heap. It pops the due task, drops the guard, runs the callback, and locks again. A
callback that schedules or cancels would otherwise deadlock, and a slow one would block every
insertion. Say what cancelling a task that is already running does: wait for it, or report
that it was too late.

**Active and pending copies.** Readers use a stable active structure while a replacement is
prepared on the side. A change clones the active copy into pending if there is none and
edits only pending; promotion swaps it in atomically (`ArcSwap`, or a short write lock) and
fixes everything that referred to the old copy in the same step. Readers never see a half
built structure. The cost is two copies in memory during preparation.

**Multi-key batches take their locks in key order, before anything else.** Keep the batch in
a `BTreeMap` so it iterates in lock order; acquire every lock; only then start the change.
Keep the phases apart (lock, mutate, publish, mark dirty), and bound the batch size, since a
large batch holds many locks. Where persistence progress has several stages, model them as an
enum keyed by epoch and object, and assert that a final state is never overwritten. This is
storage-engine machinery; a simple cache needs none of it.

**A scoped thread-local restores the previous value.** A guard that sets ambient context at a
callback or FFI boundary puts back what was there before, so nested scopes unwind correctly.

```rust
thread_local! {
    static CURRENT: Cell<Option<Tracker>> = const { Cell::new(None) };
}

pub struct TrackerGuard {
    previous: Option<Tracker>,
}

impl TrackerGuard {
    pub fn enter(tracker: Tracker) -> Self {
        Self { previous: CURRENT.with(|cell| cell.replace(Some(tracker))) }
    }
}

impl Drop for TrackerGuard {
    fn drop(&mut self) {
        CURRENT.with(|cell| cell.set(self.previous.take()));
    }
}
```

- Clearing instead of restoring breaks the outer scope as soon as two are nested.
- Thread-local context does not follow an async task across threads; use `tokio::task_local!` or pass the value explicitly.
- Ambient context is a hidden parameter. Prefer an explicit argument, and keep thread-locals for boundaries where the signature is not yours to change.

## Embedded and `no_std` essentials

This file is not an embedded manual. These are the rules an agent needs so as not to break a
firmware project it is asked to touch. HAL and executor APIs (Embassy, RTIC, the chip HALs)
change between releases: read the versions in `Cargo.lock` and the project's own examples
before writing any of it from memory.

```rust
#![no_std]
#![no_main]

use embassy_executor::Spawner;
use embassy_time::Timer;
use {defmt_rtt as _, panic_probe as _};

#[embassy_executor::main]
async fn main(spawner: Spawner) {
    let p = embassy_stm32::init(Default::default());
    spawner.spawn(blink(p.PA5.into())).unwrap(); // spawn fails only if the task pool is full
    loop {
        Timer::after_secs(1).await;
    }
}
```

- **No heap by default.** Use fixed-size buffers, `heapless` collections and `&'static` data. Add a global allocator only if the project already uses `alloc`, and never allocate in an interrupt handler.
- **Never block in an async task.** Use the executor's timer (`Timer::after_millis`), not a busy-wait delay, which stalls every other task on that executor.
- **Exactly one panic handler,** minimal and non-allocating: signal the fault, then halt or reset. In a debug build `panic-probe` reports over the probe; decide separately what production does (usually reset).

```rust
#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! {
    // put outputs in a safe state, then halt or reset
    loop {}
}
```

- **Write against `embedded-hal` traits** so a driver is not tied to one chip, and so it can be tested on the host with a fake pin or bus. Keep logic in a `no_std` library crate that also builds for the host; keep the chip-specific binary thin.
- **Serialisation:** `postcard` into a fixed buffer. Check lengths and treat every received frame as untrusted.

```rust
let mut buf = [0u8; 64];
let written: &mut [u8] = postcard::to_slice(&reading, &mut buf)?; // Err if it does not fit
let back: Reading = postcard::from_bytes(written)?;
```

- **Target and memory layout live in configuration, not in code.** The target goes in `.cargo/config.toml`; flash, RAM and stack go in `memory.x`. Take the numbers from the chip's datasheet, never from another project.

```toml
# .cargo/config.toml
[build]
target = "thumbv7em-none-eabihf" # Cortex-M4F / M7F
```

```text
/* memory.x */
MEMORY {
  FLASH : ORIGIN = 0x08000000, LENGTH = 512K
  RAM   : ORIGIN = 0x20000000, LENGTH = 128K
}
```

- **Logging:** `defmt` over RTT. No semihosting in production, no formatting or blocking prints in interrupt handlers, no verbose logs on time-critical paths.
- **Shared state between an interrupt and the main code** goes through a critical-section mutex, an atomic or a channel made for it. `static mut` is the anti-pattern.
- **Pin dependency versions.** `"*"` as a version requirement makes a firmware build unreproducible.
- **Verification an agent can do without hardware:** `cargo build --release --target <target>`, `cargo clippy --target <target>`, host-side unit tests of the logic crate, and a check of the binary size against flash (`cargo size`). Say plainly that the code was not run on a device.
- **Flashing names the chip explicitly** (`probe-rs run --chip <CHIP> <elf>`); never rely on auto-detection in a script.
- `#![cfg_attr(not(test), no_std)]` keeps `std` for host tests only. A `no_std` error enum that is `Copy + PartialEq + Eq` and implements `core::error::Error` can be compared directly in tests.
- **Fixed-capacity structures are property-tested for their laws** (idempotence, symmetry, transitivity, no-op operations), and recursion is replaced by a loop where stack depth is constrained.

## Tests

**Concurrency: a stress run is a smoke check, a model is a proof.**

```rust
#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn req_005_no_lost_updates_under_load() -> anyhow::Result<()> {
    let counter = Arc::new(Counter::default());

    let tasks: Vec<_> = (0..100)
        .map(|_| {
            let counter = Arc::clone(&counter);
            tokio::spawn(async move { counter.increment().await })
        })
        .collect();
    for task in tasks {
        task.await??;
    }

    assert_eq!(counter.get().await, 100);
    Ok(())
}
```

- Assert the final state, not only that every task returned `Ok`. One hundred successful tasks and a lost update is exactly the bug.
- The default `#[tokio::test]` runtime is single-threaded; real parallelism needs `flavor = "multi_thread"`.
- This sees only the schedules the runtime happened to choose. Where the order of operations on shared state matters, model it:

```rust
#[cfg(loom)]
#[test]
fn req_005_two_writers_never_lose_an_update() {
    loom::model(|| {
        let counter = loom::sync::Arc::new(Counter::default());
        let other = counter.clone();
        let handle = loom::thread::spawn(move || other.increment());
        counter.increment();
        handle.join().unwrap();
        assert_eq!(counter.get(), 2);
    });
}
```

- `loom` explores every interleaving, so the model must be tiny: two or three threads and a few operations. The code under test must use `loom`'s `sync` and `atomic` types behind a `cfg`, and it runs with `RUSTFLAGS="--cfg loom"`.
- `loom` does not fit code that does real I/O or uses an async runtime. A stress test is the legitimate fallback there; write down that it is a substitute and why.
- A limit stated in a requirement (retries, concurrency, queue depth) has a test that reaches it.
- **Test that nothing is left running.** After shutdown, every spawned task has been joined or aborted. No detached task survives its owner.

**Performance: a threshold in a test is a tripwire, not a measurement.**

```rust
#[test]
#[ignore = "timing; run with: cargo test --release -- --ignored"]
fn req_006_filter_10k_stays_under_budget() {
    let input = entities(10_000);
    let mut samples: Vec<Duration> = (0..200)
        .map(|_| {
            let start = Instant::now();
            std::hint::black_box(filter_implementation_entities(std::hint::black_box(&input)));
            start.elapsed()
        })
        .collect();
    samples.sort();
    let p99 = samples[samples.len() * 99 / 100];
    assert!(p99 < Duration::from_micros(500), "p99 was {p99:?}");
}
```

- `cargo test` builds without optimisation, where a latency number means little. Timing tests run with `--release`, and are `#[ignore]`d from the default run so a loaded CI machine does not fail unrelated work.
- One `Instant` reading is noise. Repeat, discard nothing silently, and assert on a percentile. `black_box` stops the optimiser deleting the work.
- For a real measurement or a comparison of two versions use `criterion`; for CI gating that must not flake, count instructions (`iai-callgrind`) or allocations instead of wall-clock time.
- **A performance claim has four parts:** the current value, the target, the percentile and the population ("from 5 ms to under 1 ms at p99 for 10,000 entities"). A new system with no current value still states percentile and population.

**Layout claims as tests.** When a size or an identity is part of the design (a cache-line
budget, an interning guarantee, a niche-optimised `Option`), pin it.

```rust
#[test]
fn node_layout_stays_within_budget() {
    assert!(std::mem::size_of::<Node>() <= 64, "Node must fit one cache line");
    assert_eq!(std::mem::size_of::<Option<NodeId>>(), std::mem::size_of::<NodeId>());
}

#[test]
fn interning_returns_the_same_allocation() {
    let a = Interned::new("common_name");
    let b = Interned::new("common_name");
    assert!(std::ptr::eq(a.as_str(), b.as_str()));
}
```

- Prefer an upper bound (`<=`) to an exact size unless the exact size is the contract (FFI, an on-disk format). Exact sizes differ between 32-bit and 64-bit targets and may change with the compiler for `repr(Rust)` types.
- For a hard guarantee, check at compile time: `const _: () = assert!(std::mem::size_of::<Node>() <= 64);`.
- *Skip* for types whose size nobody depends on; the test then only blocks harmless refactors.

## Review

- Which performance claim lacks a threshold, a baseline or stated conditions?
- Was the result checked to be the same before and after the change?
- Did any speed-up remove a check that input can reach?
- What bounds each cache, pool, queue and arena, and what resets it?
- Does each cache key contain every input that changes the answer, including tenant and authorisation scope?
- Was the parallel path run under contention, and is output order still deterministic?
- Is any `unsafe` or lock-free code here justified by a measurement?

## Out of scope

- **Service latency caused by pools, transactions or fan-out.** Use the application-service skill first.
- **Unsafe code and FFI in detail.** Use the unsafe and FFI skill beside this one.
- **Parsers and source tools; storage formats and protocols.** They have their own infra skills.

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
