# Rust Patterns 202606 Part 5

Purpose: capture Rust and Rust-adjacent architecture, idiom, parser, Tree-sitter, code-intelligence, async, CLI, API, storage, verification, and operational patterns discovered repo-by-repo under `/Users/amuldotexe/Desktop`.

Evidence policy: every non-obvious pattern should name the repository, file path, and why the code is reusable. Codebase-memory graph evidence is useful for discovery, but source paths and snippets are the authority.

Shard owner: parallel worker 5.
Shard repo count: 31.

## Assigned Repository Shard

- `/Users/amuldotexe/Desktop/oss-read-only/agent-debate`
- `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/dockdash`
- `/Users/amuldotexe/Desktop/oss-read-only/clarity-cli`
- `/Users/amuldotexe/Desktop/oss-read-only/datafusion`
- `/Users/amuldotexe/Desktop/oss-read-only/ibis`
- `/Users/amuldotexe/Desktop/oss-read-only/opendal`
- `/Users/amuldotexe/Desktop/oss-read-only/pinot`
- `/Users/amuldotexe/Desktop/oss-read-only/scikit-learn`
- `/Users/amuldotexe/Desktop/oss-read-only/vaex`
- `/Users/amuldotexe/Desktop/personal-repos-lane/Arithmancy2025`
- `/Users/amuldotexe/Desktop/personal-repos-lane/Viz-Wizard`
- `/Users/amuldotexe/Desktop/personal-repos-lane/backlog-experiments`
- `/Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129`
- `/Users/amuldotexe/Desktop/personal-repos-lane/extract_twitter202304`
- `/Users/amuldotexe/Desktop/personal-repos-lane/games-001`
- `/Users/amuldotexe/Desktop/personal-repos-lane/journal-202401`
- `/Users/amuldotexe/Desktop/personal-repos-lane/mission-grindelwald`
- `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm`
- `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve2024`
- `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement`
- `/Users/amuldotexe/Desktop/personal-repos-lane/smallest-exp-20260404`
- `/Users/amuldotexe/Desktop/personal-repos-lane/txt-sectumsempra`
- `/Users/amuldotexe/Desktop/personal-repos-lane/zzJS-TS-notes-2023`
- `/Users/amuldotexe/Desktop/reference-repos-yard/GitNexus`
- `/Users/amuldotexe/Desktop/reference-repos-yard/argus`
- `/Users/amuldotexe/Desktop/reference-repos-yard/create-tauri-app`
- `/Users/amuldotexe/Desktop/reference-repos-yard/flowistry`
- `/Users/amuldotexe/Desktop/reference-repos-yard/lockbud`
- `/Users/amuldotexe/Desktop/reference-repos-yard/paralegal`
- `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_cranelift`
- `/Users/amuldotexe/Desktop/reference-repos-yard/twitter-circle`

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

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/alienplatform/dockdash

Codebase-memory: succeeded at `/tmp/codex-code-intel/codebase-memory/dockdash-20260706-223352`; used as discovery only. Source verification used `rg` plus direct reads of `src/error.rs`, `src/blobcache.rs`, `src/layer.rs`, and `src/image.rs`.

### Concept: Non-exhaustive domain error enum with boxed source escape hatches
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/dockdash/src/error.rs`
Why it matters: This is a pragmatic library error pattern for crates that integrate many third-party systems. The enum keeps common categories typed (`Io`, `Join`, `ImagePull`, `ImageConfig`, `OciArchive`, `Cache`, `InvalidPath`) while retaining an extension slot via `Option<Box<dyn std::error::Error + Send + Sync + 'static>>`. `#[non_exhaustive]` lets the public API grow without breaking downstream matches. The helper `is_manifest_not_found` shows how to recover typed knowledge by downcasting the boxed source only at decision points, keeping most callers on a simple domain error surface.
Reusable code shape:
```rust
#[derive(thiserror::Error, Debug)]
#[non_exhaustive]
pub enum Error {
    #[error("I/O error: {message}: {source}")]
    Io {
        message: String,
        #[source]
        source: std::io::Error,
    },
    #[error("Registry error for {image_ref}: {message}")]
    ImagePull {
        image_ref: String,
        message: String,
        #[source]
        source: Option<Box<dyn std::error::Error + Send + Sync + 'static>>,
    },
}

impl Error {
    pub fn is_manifest_not_found(&self) -> bool {
        match self {
            Error::ImagePull { source: Some(source), .. } => source
                .downcast_ref::<oci_client::errors::OciDistributionError>()
                .is_some_and(is_oci_manifest_not_found),
            _ => false,
        }
    }
}
```
Transfer rule: Apply when a library has stable public error categories but unstable dependency internals. Avoid as the only error strategy in small binaries where `anyhow::Context` is simpler and no downstream code needs structured matching.
Verification hook: Review every `map_err` site for a human-actionable `message`, and add focused tests for semantic helpers like `is_manifest_not_found` so boxed sources do not become opaque forever.

### Concept: Async content-addressed disk cache returning `Option` for misses
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/dockdash/src/blobcache.rs`
Why it matters: `BlobCache` wraps `cacache` behind a small domain API where cache miss is a value (`Ok(None)`), not an error. This is especially useful for agentic build systems because callers can express "try cache, then compute" without mixing expected misses with operational failures. The constructor chooses a writable default path but provides `with_path` for deterministic tests and tool-controlled cache directories.
Reusable code shape:
```rust
#[derive(Debug, Clone)]
pub struct BlobCache {
    cache_path: PathBuf,
}

impl BlobCache {
    pub fn with_path(path: PathBuf) -> Result<Self> {
        Self::init(path)
    }

    pub async fn get_blob(&self, digest: &str) -> Result<Option<Vec<u8>>> {
        match cacache::read(&self.cache_path, digest).await {
            Ok(data) => Ok(Some(data)),
            Err(cacache::Error::EntryNotFound(_, _)) => Ok(None),
            Err(e) => Err(Error::Cache {
                message: format!("failed to read blob {digest}"),
                source: Some(Box::new(e)),
            }),
        }
    }

    pub async fn put_blob(&self, digest: &str, data: &[u8]) -> Result<()> {
        cacache::write(&self.cache_path, digest, data).await.map_err(|e| Error::Cache {
            message: format!("failed to write blob {digest}"),
            source: Some(Box::new(e)),
        })
    }
}
```
Transfer rule: Apply to build, parser-index, artifact, or AI-context caches where misses are routine and corruption/I/O failures are exceptional. Avoid hiding integrity errors as misses; only translate the dependency's explicit not-found variant.
Verification hook: The repo verifies this with async tempdir tests: put/get roundtrip, nonexistent blob returns `None`, remove is idempotent.

### Concept: Two-stage artifact cache with fast input metadata key before expensive content key
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/dockdash/src/layer.rs`
Why it matters: `LayerBuilder::build` first hashes sorted input metadata (`archive_path`, size, mtime, mode, directory flag, optional content hash) to find a cached compressed layer before finalizing and hashing the tar. On a miss, it finalizes/syncs the tar, computes a content key, and then stores metadata under both keys. This is a reusable "cheap fingerprint first, canonical fingerprint second" pattern for expensive transformations such as compression, code generation, parser table generation, embeddings, or package builds.
Reusable code shape:
```rust
fn calculate_input_key(&self) -> String {
    let mut sorted = self.file_metadata.clone();
    sorted.sort_by(|a, b| a.archive_path.cmp(&b.archive_path));

    let mut hasher = Sha256::new();
    for meta in &sorted {
        hasher.update(meta.archive_path.to_string_lossy().as_bytes());
        hasher.update(meta.size.to_le_bytes());
        hasher.update(meta.mtime.to_le_bytes());
        hasher.update(meta.mode.to_le_bytes());
        hasher.update([meta.is_dir as u8]);
        if let Some(hash) = &meta.content_hash {
            hasher.update(hash);
        }
    }
    format!("layer-input-{:x}", hasher.finalize())
}

pub async fn build(mut self) -> Result<Layer> {
    let input_key = self.calculate_input_key();
    if let Some(metadata) = cache.get_blob(&input_key).await? {
        if let Some(layer) = try_restore_cached_layer(metadata, &cache).await? {
            return Ok(layer);
        }
    }

    finalize_and_sync_tar(&mut self)?;
    let content_key = Self::calculate_content_key(&self.uncompressed_tar_path)?;
    // try content cache, otherwise compress and then store under both keys
    cache.put_blob(&content_key, &metadata_bytes).await?;
    cache.put_blob(&input_key, &metadata_bytes).await?;
    Ok(layer)
}
```
Transfer rule: Apply when the transformation is expensive and the input set can be summarized deterministically. Avoid if metadata can lie about content changes; in that case include content hashes or fall back to the content key before trusting the fast key.
Verification hook: Add tests that change only metadata fields and assert cache invalidation, plus tests that same logical input order produces the same key. Benchmark hit path versus full transform path.

### Concept: Tar archive parent directory synthesis with a created-directory set
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/dockdash/src/layer.rs`
Why it matters: Archive builders often append files into nested paths but forget explicit directory entries, causing inconsistent permissions, tar readers, or extraction behavior. `ensure_parent_dirs_exist` walks ancestors, filters root/empty paths, emits headers from top-level downward, and records created directories in a `HashSet<PathBuf>` to avoid duplicates.
Reusable code shape:
```rust
fn ensure_parent_dirs_exist(&mut self, path_in_archive: impl AsRef<Path>) -> Result<()> {
    let path_in_archive = path_in_archive.as_ref();
    let Some(parent) = path_in_archive.parent() else { return Ok(()); };
    if parent.as_os_str().is_empty() {
        return Ok(());
    }

    let mut paths_to_create = Vec::new();
    let mut current = parent;
    loop {
        let s = current.to_string_lossy();
        if !s.is_empty() && s != "/" {
            paths_to_create.push(current.to_path_buf());
        }
        match current.parent() {
            Some(parent) => current = parent,
            None => break,
        }
    }

    for dir in paths_to_create.iter().rev() {
        if self.created_archive_dirs.insert(dir.clone()) {
            let mut header = tar::Header::new_gnu();
            header.set_path(dir)?;
            header.set_entry_type(tar::EntryType::Directory);
            self.tar_writer.append(&header, std::io::empty())?;
        }
    }
    Ok(())
}
```
Transfer rule: Apply to any Rust tool producing tar/OCI/package archives from arbitrary file paths. Avoid if the archive format automatically synthesizes directory entries with correct metadata, which tar does not reliably do across consumers.
Verification hook: Integration tests should extract the archive and assert nested paths exist with expected directory metadata; include root path and already-created directory cases.

### Concept: Async progress callback option with custom `Debug` and lossy `Clone`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/alienplatform/dockdash/src/image.rs`
Why it matters: `PushOptions` stores an optional boxed async callback trait for push progress. Because trait objects are not clonable or printable by default, the code implements `Debug` by exposing only `progress_callback.is_some()` and implements `Clone` by cloning ordinary fields while intentionally dropping the callback. This is a clear API tradeoff for options structs that must remain cloneable for retry/config flows but can treat observers as non-essential.
Reusable code shape:
```rust
#[async_trait::async_trait]
pub trait PushProgressCallback: Send + Sync {
    async fn on_progress(&self, progress: PushProgressInfo);
}

pub struct PushOptions {
    pub auth: RegistryAuth,
    pub progress_callback: Option<Box<dyn PushProgressCallback>>,
}

impl std::fmt::Debug for PushOptions {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("PushOptions")
            .field("auth", &self.auth)
            .field("progress_callback", &self.progress_callback.is_some())
            .finish()
    }
}

impl Clone for PushOptions {
    fn clone(&self) -> Self {
        Self {
            auth: self.auth.clone(),
            progress_callback: None,
        }
    }
}
```
Transfer rule: Apply when callbacks are observers and losing them during cloning is acceptable and documented. Avoid for callbacks that enforce behavior, authorization, cancellation, or resource cleanup; use `Arc<dyn Trait>` when cloned callback identity must survive.
Verification hook: Unit-test `Debug` output to avoid leaking callback internals and test clone semantics explicitly so future maintainers do not assume observers propagate.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm

Codebase-memory: succeeded at `/tmp/codex-code-intel/codebase-memory/nostd-toposort-kahns-algorithm-20260706-223352`; used as discovery only. Source verification used `rg` plus direct reads of `Cargo.toml`, `src/lib.rs`, `src/error.rs`, `tests/toposort_correctness_tests.rs`, `tests/property_based_toposort_tests.rs`, and `benches/toposort_performance_benchmarks.rs`.

### Concept: Const-generic no-std graph capacity with `heapless::Vec`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm/src/lib.rs`
Why it matters: `TopoSort<const N: usize>` makes maximum graph size a type-level capacity and stores adjacency lists as `[heapless::Vec<usize, N>; N]` plus fixed arrays for in-degree. This gives predictable memory use, no allocator dependency, and compile-time capacity selection. It is a strong pattern for embedded schedulers, dependency resolvers inside parsers, or deterministic agent tools that should not allocate while operating.
Reusable code shape:
```rust
#![no_std]

use heapless::Vec;

#[derive(Debug, Clone)]
pub struct TopoSort<const N: usize> {
    adjacency: [Vec<usize, N>; N],
    in_degree: [usize; N],
    num_nodes: usize,
}

impl<const N: usize> TopoSort<N> {
    #[inline]
    pub fn new() -> Self {
        Self {
            adjacency: [const { Vec::new() }; N],
            in_degree: [0; N],
            num_nodes: N,
        }
    }
}
```
Transfer rule: Apply when the maximum problem size is known or can be conservatively bounded. Avoid for large, sparse, user-provided graphs where `N * N` adjacency capacity would waste memory or make compile-time types explode.
Verification hook: Build with `cargo test --no-default-features` if the crate has feature flags; otherwise keep `#![no_std]` at crate root and ensure only `core`/`heapless` appear in production dependencies.

### Concept: Kahn topological sort using a vector plus cursor instead of queue allocation
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm/src/lib.rs`
Why it matters: The implementation uses `heapless::Vec` as a FIFO queue by keeping `queue_idx` rather than popping from the front. That avoids `Vec::remove(0)` shifting costs and avoids needing a separate deque type. It copies the in-degree array, processes zero-in-degree nodes, decrements neighbors, detects cycles by comparing processed count to `num_nodes`, then reverses the result because this project models edges as "dependent -> dependency".
Reusable code shape:
```rust
pub fn sort_all_nodes_topologically(&self) -> Result<Vec<usize, N>, TopoSortError> {
    let mut in_degree = self.in_degree;
    let mut queue: Vec<usize, N> = Vec::new();
    for node in 0..self.num_nodes {
        if in_degree[node] == 0 {
            let _ = queue.push(node);
        }
    }

    let mut result: Vec<usize, N> = Vec::new();
    let mut queue_idx = 0;
    while queue_idx < queue.len() {
        let node = queue[queue_idx];
        queue_idx += 1;
        let _ = result.push(node);

        for &neighbor in self.adjacency[node].iter() {
            in_degree[neighbor] -= 1;
            if in_degree[neighbor] == 0 {
                let _ = queue.push(neighbor);
            }
        }
    }

    if result.len() < self.num_nodes {
        return Err(TopoSortError::CycleDetected { processed_count: result.len() });
    }
    result.reverse();
    Ok(result)
}
```
Transfer rule: Apply in fixed-capacity graph algorithms where FIFO order matters and allocation is forbidden. Avoid silently ignoring `push` errors unless an invariant proves capacity is sufficient; otherwise propagate capacity failures.
Verification hook: Tests must assert both ordering semantics and cycle detection. This repo verifies dependencies-first ordering by mapping every node to its result position and asserting `position[from] > position[to]` for each edge.

### Concept: no-std-compatible error enum with `core::fmt::Display`
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm/src/error.rs`
Why it matters: The crate defines `TopoSortError` with `Debug`, `Clone`, `PartialEq`, and `Eq`, then manually implements `core::fmt::Display` instead of relying on `std::error::Error`. That keeps the algorithm usable in no-std environments while still giving tests and callers structured variants for matching.
Reusable code shape:
```rust
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum TopoSortError {
    CycleDetected { processed_count: usize },
    IndexOutOfBounds { index: usize, capacity: usize },
    CapacityExceeded { current: usize, max: usize },
}

impl core::fmt::Display for TopoSortError {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            Self::CycleDetected { processed_count } => {
                write!(f, "Cycle detected: only {processed_count} nodes processed")
            }
            Self::IndexOutOfBounds { index, capacity } => {
                write!(f, "Index {index} out of bounds (capacity: {capacity})")
            }
            Self::CapacityExceeded { current, max } => {
                write!(f, "Capacity exceeded: {current} > {max}")
            }
        }
    }
}
```
Transfer rule: Apply to no-std libraries that still need useful diagnostics. Avoid deriving or implementing `std::error::Error` in the core crate; add it behind an optional `std` feature if needed.
Verification hook: Unit tests should pattern-match exact variants rather than string output; use Display tests only for user-facing messages.

### Concept: Algorithm properties as executable tests plus Criterion shape benchmarks
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm/tests/property_based_toposort_tests.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/nostd-toposort-kahns-algorithm/benches/toposort_performance_benchmarks.rs`
Why it matters: The tests name durable algorithmic properties: dependencies precede dependents, all nodes appear exactly once, deterministic construction produces deterministic ordering, insertion order may change order but not validity, cycles are consistently detected, and acyclic graphs succeed. The Criterion benches cover graph sizes and graph shapes (linear chain, binary tree, diamond pattern), which is better evidence than a single happy-path microbenchmark.
Reusable code shape:
```rust
#[test]
fn property_valid_ordering_dependencies_first() {
    let result = graph.sort_all_nodes_topologically().unwrap();
    let positions: Vec<_> = (0..node_count)
        .map(|node| result.iter().position(|&x| x == node).unwrap())
        .collect();

    for (from, to) in edges {
        assert!(positions[from] > positions[to]);
    }
}

fn benchmark_graph_structures(c: &mut Criterion) {
    let mut group = c.benchmark_group("graph_structures");
    group.bench_function("linear_chain_50", |b| {
        b.iter(|| black_box(graph.sort_all_nodes_topologically()))
    });
    group.finish();
}
```
Transfer rule: Apply to parser dependency graphs, build graphs, task DAGs, and scheduling code where the exact ordering may vary but invariants matter. Avoid asserting one golden ordering unless the algorithm deliberately guarantees a tie-breaker.
Verification hook: Run `cargo test` for contracts and `cargo bench --bench toposort_performance_benchmarks` before changing adjacency, tie-breaking, or edge-direction semantics.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/txt-sectumsempra

Codebase-memory: succeeded at `/tmp/codex-code-intel/codebase-memory/txt-sectumsempra-20260706-223356`; used as discovery only. Source verification used `rg` plus direct reads of `src/lib.rs`, `src/main.rs`, `src/error.rs`, `tests/integration_tests.rs`, and `Cargo.toml`.

### Concept: Streaming file chunker with cleanup-on-error guard list
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/txt-sectumsempra/src/lib.rs`
Why it matters: `Chunker::split_file` uses `BufReader`, `BufWriter`, an 8 KiB buffer, and a `created_chunks` list to split large files without loading them into memory. The body is wrapped in a closure returning `Result<Vec<PathBuf>>`; after it runs, the outer function removes every created chunk and the output directory if an error occurred. This pattern gives most of the value of RAII cleanup without introducing a custom guard type.
Reusable code shape:
```rust
pub fn split_file(path: &Path, size_mb: f64) -> Result<Vec<PathBuf>> {
    let input_file = File::open(path)?;
    let file_size = input_file.metadata()?.len();
    let chunk_size = (size_mb * 1024.0 * 1024.0) as u64;
    let output_dir = make_timestamped_output_dir(path)?;
    fs::create_dir_all(&output_dir)?;

    let mut created_chunks = Vec::new();
    let result: Result<Vec<PathBuf>> = (|| {
        let mut reader = BufReader::with_capacity(BUFFER_SIZE, input_file);
        let mut buffer = vec![0; BUFFER_SIZE];
        let mut chunk_paths = Vec::new();
        let mut bytes_remaining = file_size;

        while bytes_remaining > 0 {
            let current_chunk_size = bytes_remaining.min(chunk_size);
            let chunk_path = output_dir.join(format!("part-{}.txt", chunk_paths.len()));
            created_chunks.push(chunk_path.clone());
            let mut writer = BufWriter::with_capacity(BUFFER_SIZE, File::create(&chunk_path)?);
            copy_exact_window(&mut reader, &mut writer, &mut buffer, current_chunk_size)?;
            writer.flush()?;
            chunk_paths.push(chunk_path);
            bytes_remaining = bytes_remaining.saturating_sub(current_chunk_size);
        }
        Ok(chunk_paths)
    })();

    if result.is_err() {
        for chunk in created_chunks {
            let _ = fs::remove_file(chunk);
        }
        let _ = fs::remove_dir(&output_dir);
    }
    result
}
```
Transfer rule: Apply to command-line file transforms that create multiple outputs and can fail midstream. For production libraries, prefer a small guard type with `Drop` and a `commit` flag so panics and early returns also clean up.
Verification hook: Integration tests should create multi-megabyte deterministic files, assert exact chunk sizes except the last chunk, validate roundtrip content, and inject missing chunks/errors to confirm cleanup and validation behavior.

### Concept: Hash-concatenation validation for split artifacts
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/txt-sectumsempra/src/lib.rs`
Why it matters: `Chunker::validate` verifies all chunks exist, then hashes the original file and the ordered concatenation of chunks using `Sha256`. It avoids reconstructing a temporary full file and keeps memory bounded by streaming each input through `io::copy`. This is a concise integrity check for archive, chunk upload, and resumable transfer tools.
Reusable code shape:
```rust
pub fn validate(original: &Path, chunks: &[PathBuf]) -> Result<bool> {
    if chunks.is_empty() {
        return Err(ChunkError::InvalidInput("No chunks provided for validation"));
    }
    for chunk in chunks {
        if !chunk.exists() {
            return Err(ChunkError::InvalidInput("Missing chunk file"));
        }
    }

    let mut original_hasher = Sha256::new();
    let mut chunk_hasher = Sha256::new();

    let mut reader = BufReader::with_capacity(BUFFER_SIZE, File::open(original)?);
    io::copy(&mut reader, &mut original_hasher)?;

    for chunk_path in chunks {
        let mut reader = BufReader::with_capacity(BUFFER_SIZE, File::open(chunk_path)?);
        io::copy(&mut reader, &mut chunk_hasher)?;
    }

    Ok(original_hasher.finalize() == chunk_hasher.finalize())
}
```
Transfer rule: Apply when chunk order is already authoritative and byte-for-byte reconstruction is the invariant. Avoid if chunks can be reordered, duplicated, or partially trusted; then include per-chunk indices, sizes, and hashes in a manifest.
Verification hook: Delete one chunk and assert validation returns a typed error; reorder chunks and assert validation returns `Ok(false)`; mutate one byte and assert hash mismatch.

### Concept: Thin Clap binary over a reusable library API
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/txt-sectumsempra/src/main.rs`, `/Users/amuldotexe/Desktop/personal-repos-lane/txt-sectumsempra/src/error.rs`
Why it matters: The binary owns CLI parsing, existence checks, user-facing messages, and exit codes. The library owns `Chunker::split_file`, `Chunker::validate`, and `ChunkError`. That separation lets tests call the library directly without shelling out, while the CLI stays readable and explicit.
Reusable code shape:
```rust
#[derive(clap::Parser)]
struct Args {
    #[arg(value_name = "FILE")]
    input: PathBuf,
    #[arg(short, long, default_value_t = 1.0)]
    size: f64,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = Args::parse();
    if !args.input.is_file() {
        eprintln!("Error: Input path is not a file");
        std::process::exit(1);
    }

    let chunks = match txt_sectumsempra::Chunker::split_file(&args.input, args.size) {
        Ok(chunks) => chunks,
        Err(e) => {
            eprintln!("Error splitting file: {e}");
            std::process::exit(1);
        }
    };
    if !txt_sectumsempra::Chunker::validate(&args.input, &chunks)? {
        std::process::exit(1);
    }
    Ok(())
}
```
Transfer rule: Apply to Rust CLIs where business logic should remain testable as a library. Avoid putting progress printing inside library functions if the library is meant for non-terminal consumers; pass a callback or writer instead.
Verification hook: Unit-test library errors directly and add CLI integration tests for parse/exit behavior if the command is user-facing.

## Repo Coverage: /Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement

Codebase-memory: succeeded at `/tmp/codex-code-intel/codebase-memory/room-of-requirement-20260706-223353`; used as discovery only. Source verification used `rg` plus direct reads of `src/cli.rs`, `src/errors.rs`, `src/models.rs`, `src/github.rs`, `src/database.rs`, `src/github/tests.rs`, `tests/unit/cli_tests.rs`, `tests/unit/database_tests.rs`, and `Cargo.toml`.

### Concept: Clap builder CLI that merges flags with environment fallback and validates immediately
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/src/cli.rs`
Why it matters: `CliConfig::parse` delegates to `build_cli().get_matches()` and `from_matches`, while `parse_from` uses `try_get_matches_from` for tests. The config layer pulls `--github-token`/`--database-url` first and falls back to `GITHUB_TOKEN`/`DATABASE_URL`, then validates query length, token length/whitespace, and PostgreSQL URL shape before returning a `CliConfig`. This creates a clear "config is valid after construction" invariant.
Reusable code shape:
```rust
impl CliConfig {
    pub fn parse_from<I, T>(args: I) -> Result<Self>
    where
        I: IntoIterator<Item = T>,
        T: Into<std::ffi::OsString> + Clone,
    {
        let matches = Self::build_cli()
            .try_get_matches_from(args)
            .map_err(|e| AppError::configuration(format!("Argument parsing failed: {e}")))?;
        Self::from_matches(&matches)
    }

    fn from_matches(matches: &ArgMatches) -> Result<Self> {
        let search_query = matches.get_one::<String>("query").cloned()
            .ok_or_else(|| AppError::configuration("Search query is required"))?;
        Self::validate_search_query(&search_query)?;

        let github_token = matches.get_one::<String>("github-token").cloned()
            .or_else(|| std::env::var("GITHUB_TOKEN").ok())
            .ok_or_else(|| AppError::environment("GITHUB_TOKEN"))?;
        Self::validate_github_token(&github_token)?;

        let database_url = matches.get_one::<String>("database-url").cloned()
            .or_else(|| std::env::var("DATABASE_URL").ok())
            .ok_or_else(|| AppError::environment("DATABASE_URL"))?;
        Self::validate_database_url(&database_url)?;

        Ok(Self { search_query, github_token, database_url, /* flags */ })
    }
}
```
Transfer rule: Apply to service CLIs and agent tools where runtime work should never see half-valid configuration. Avoid reading environment variables deep inside business logic; do it once at the boundary.
Verification hook: Use `parse_from` in unit tests, property-test validators over accepted ranges, and assert sensitive fields are masked in summaries.

### Concept: API DTOs with explicit business validation after Serde deserialization
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/src/models.rs`
Why it matters: `Repository`, `RepositoryOwner`, `RepositoryLicense`, `SearchResponse`, and `QueryMetadata` derive `Serialize`/`Deserialize` for API/storage movement, but correctness is enforced in explicit `validate` methods. The validation checks non-empty required fields, URL prefixes/suffixes, visibility enum values, non-negative counters, and recursively validates nested owner/license structures. This keeps "shape parsing" and "domain acceptance" separate.
Reusable code shape:
```rust
impl Repository {
    pub fn validate(&self) -> Result<()> {
        if self.full_name.is_empty() {
            return Err(AppError::validation("full_name", "cannot be empty"));
        }
        if !self.html_url.starts_with("https://github.com/") {
            return Err(AppError::validation("html_url", "must be a valid GitHub URL"));
        }
        if !self.clone_url.starts_with("https://github.com/") || !self.clone_url.ends_with(".git") {
            return Err(AppError::validation("clone_url", "must be a valid GitHub clone URL"));
        }
        if !["public", "private", "internal"].contains(&self.visibility.as_str()) {
            return Err(AppError::validation("visibility", "must be public/private/internal"));
        }
        if self.stargazers_count < 0 {
            return Err(AppError::validation("stargazers_count", "cannot be negative"));
        }
        self.owner.validate()?;
        if let Some(license) = &self.license {
            license.validate()?;
        }
        Ok(())
    }
}
```
Transfer rule: Apply when consuming third-party JSON into types that will be persisted or trusted by downstream logic. Avoid relying on Serde alone for business rules unless the invariant is purely structural.
Verification hook: Add table-driven tests for every validation branch and make storage insertion call `repo.validate()` before binding values.

### Concept: Reqwest API client with status-specific error taxonomy and exponential backoff
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/src/github.rs`
Why it matters: `GitHubClient` builds a `reqwest::Client` with timeout and user-agent, carries a testable `base_url`, and maps statuses to domain errors: `200` parses JSON, `403`/`429` retry with jittered exponential backoff until `RateLimit`, `401` becomes `Authentication`, `422` parses validation JSON into `InvalidQuery`, and other statuses include response body in `GitHubApi`. The retry knobs live in `RateLimitConfig`.
Reusable code shape:
```rust
pub async fn search_repositories_with_config(
    &self,
    query: &str,
    per_page: Option<u32>,
    page: Option<u32>,
    config: &RateLimitConfig,
) -> Result<SearchResponse> {
    let per_page = per_page.unwrap_or(30).clamp(1, 100);
    let page = page.unwrap_or(1).max(1);
    let mut attempt = 0;
    let mut backoff_ms = config.initial_backoff_ms;

    loop {
        let response = self.client.get(&url)
            .header("Authorization", format!("Bearer {}", self.token))
            .header("Accept", "application/vnd.github.v3+json")
            .query(&[("q", query), ("per_page", &per_page.to_string())])
            .send()
            .await?;

        match response.status() {
            StatusCode::OK => return Ok(response.json().await?),
            StatusCode::FORBIDDEN | StatusCode::TOO_MANY_REQUESTS if attempt < config.max_retries => {
                let jitter = fastrand::u64(0..=backoff_ms / 4);
                tokio::time::sleep(Duration::from_millis(backoff_ms + jitter)).await;
                backoff_ms = ((backoff_ms as f64 * config.backoff_multiplier) as u64)
                    .min(config.max_backoff_ms);
                attempt += 1;
            }
            StatusCode::UNAUTHORIZED => return Err(AppError::authentication("Invalid or expired GitHub token")),
            StatusCode::UNPROCESSABLE_ENTITY => {
                let body = response.text().await.unwrap_or_default();
                return Err(AppError::invalid_query(query, self.extract_validation_error(&body)));
            }
            status => return Err(AppError::github_api(format!("HTTP {status}: {}", response.text().await.unwrap_or_default()))),
        }
    }
}
```
Transfer rule: Apply to external API clients where callers need actionable error classes, not just HTTP failures. Avoid sleeping directly in tests; expose retry config with tiny delays or inject a sleep strategy if tests need to cover retry timing.
Verification hook: Unit-test parameter clamping, validation-error JSON extraction, empty-token and empty-query errors; integration-test status mapping with `wiremock` or a real mock server.

### Concept: SQLx manager with pool cloneability, dynamic per-query tables, and transactional upserts
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/src/database.rs`
Why it matters: `DatabaseManager` wraps `PgPool` in a cloneable struct, initializes shared `query_history`, creates repository tables with indexes, and inserts repository batches inside a transaction. Values are bound with SQLx placeholders while dynamic table names are formatted into SQL. The code validates names in `drop_table`; the reusable lesson is to centralize identifier generation/validation for every dynamic SQL entrypoint, not only destructive ones.
Reusable code shape:
```rust
#[derive(Clone)]
pub struct DatabaseManager {
    pool: PgPool,
}

impl DatabaseManager {
    pub async fn insert_repositories(&self, table_name: &str, repositories: &[Repository]) -> Result<i64> {
        validate_dynamic_identifier(table_name)?;
        if repositories.is_empty() {
            return Ok(0);
        }

        let mut tx = self.pool.begin().await?;
        for repo in repositories {
            repo.validate()?;
            let sql = format!(
                "INSERT INTO {table_name} (github_id, full_name) VALUES ($1, $2) \
                 ON CONFLICT (github_id) DO UPDATE SET full_name = EXCLUDED.full_name"
            );
            sqlx::query(&sql)
                .bind(repo.id)
                .bind(&repo.full_name)
                .execute(&mut *tx)
                .await?;
        }
        tx.commit().await?;
        Ok(repositories.len() as i64)
    }
}

fn validate_dynamic_identifier(table_name: &str) -> Result<()> {
    if table_name.starts_with("repos_") && table_name.chars().all(|c| c.is_alphanumeric() || c == '_') {
        Ok(())
    } else {
        Err(AppError::validation("table_name", "Invalid table name format"))
    }
}
```
Transfer rule: Apply when each query/job needs its own physical table and SQLx compile-time macros cannot be used because identifiers are dynamic. Avoid formatting user-controlled identifiers unless every public method validates them through the same helper.
Verification hook: Testcontainers-backed tests should cover create/list/stats/drop lifecycle, duplicate upsert behavior, invalid table names, and concurrent inserts via cloned managers.

### Concept: Testcontainers database tests with serial isolation and async concurrency probes
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/room-of-requirement/tests/unit/database_tests.rs`
Why it matters: The tests start a Postgres container, build a runtime database URL from the mapped host port, and construct `DatabaseManager` against real SQL. They mark tests `#[serial]` to avoid Docker/database interference, then still test application-level concurrency by cloning the manager and spawning five insert tasks into one table. This separates "environment isolation" from "code concurrency".
Reusable code shape:
```rust
fn setup_test_database() -> (Cli, Container<'static, Postgres>) {
    let docker = Cli::default();
    let image = Postgres::default()
        .with_db_name("test_db")
        .with_user("test_user")
        .with_password("test_password");
    (docker, docker.run(image))
}

#[tokio::test]
#[serial]
async fn test_concurrent_operations() {
    let (_docker, container) = setup_test_database();
    let db = create_database_manager(&container).await;
    db.create_repository_table(&table_name).await.unwrap();

    let mut handles = Vec::new();
    for i in 0..5 {
        let db_clone = db.clone();
        let table = table_name.clone();
        handles.push(tokio::spawn(async move {
            db_clone.insert_repositories(&table, &make_repos(i)).await.unwrap()
        }));
    }

    let total = futures::future::join_all(handles).await.into_iter().sum::<Result<i64, _>>()?;
    assert_eq!(total, 10);
}
```
Transfer rule: Apply to storage code where mocks would miss DDL, indexes, transactions, and connection-pool behavior. Avoid global shared database names; randomize table names and clean up.
Verification hook: Run the database test suite with Docker available; ensure cleanup paths drop generated tables even when assertions fail.

## Repo Coverage: /Users/amuldotexe/Desktop/reference-repos-yard/create-tauri-app

Codebase-memory: succeeded at `/tmp/codex-code-intel/codebase-memory/create-tauri-app-20260706-223356`; used as discovery only. Source verification used `rg` plus direct reads of `src/template.rs`, `src/utils/lte.rs`, `src/manifest.rs`, `src/package_manager.rs`, `src/args.rs`, `node/src/lib.rs`, and `node/build.rs`.

### Concept: Enums as scaffolder capability matrices
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/create-tauri-app/src/template.rs`, `/Users/amuldotexe/Desktop/reference-repos-yard/create-tauri-app/src/package_manager.rs`, `/Users/amuldotexe/Desktop/reference-repos-yard/create-tauri-app/src/args.rs`
Why it matters: `Template`, `Flavor`, `PackageManager`, and `TauriVersion` are small enums that encode the product matrix: display strings, parse strings, valid package managers for each template, available flavors, command names, and defaults. This keeps prompt/CLI choices out of stringly typed conditionals and makes unsupported combinations explicit.
Reusable code shape:
```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
#[non_exhaustive]
pub enum PackageManager {
    #[default]
    Cargo,
    Pnpm,
    Yarn,
    Npm,
    Bun,
}

impl PackageManager {
    pub const ALL: &'static [PackageManager] = &[
        PackageManager::Cargo,
        PackageManager::Pnpm,
        PackageManager::Yarn,
        PackageManager::Npm,
        PackageManager::Bun,
    ];

    pub const fn templates(&self) -> &[Template] {
        match self {
            PackageManager::Cargo => &[Template::Vanilla, Template::Yew, Template::Leptos],
            PackageManager::Pnpm | PackageManager::Yarn | PackageManager::Npm | PackageManager::Bun => {
                &[Template::Vanilla, Template::VanillaTs, Template::React, Template::ReactTs]
            }
        }
    }

    pub const fn run_cmd(&self) -> &str {
        match self {
            PackageManager::Cargo => "cargo",
            PackageManager::Npm => "npm run",
            PackageManager::Pnpm => "pnpm",
            PackageManager::Yarn => "yarn",
            PackageManager::Bun => "bun run",
        }
    }
}
```
Transfer rule: Apply to scaffolding agents and project generators where choices form a compatibility matrix. Avoid parallel arrays in JSON/TOML when the matrix drives Rust control flow; encode it in enums and expose `ALL` for UI prompts.
Verification hook: Unit-test `FromStr`, `Display`, and every compatibility relation, especially when adding a new package manager or template.

### Concept: Embedded template tree with base layer, override layer, manifest extras, and conditional filenames
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/create-tauri-app/src/template.rs`
Why it matters: The generator embeds the entire `templates` folder with `rust_embed`, reads a per-template `.manifest`, prepares template data, writes `_base_` files first, then writes `template-{self}` files that can override base files, then appends extra assets declared by the manifest. File names can carry flags like `%(pnpm-npm-yarn-v1)%package.json`, and `.lte` suffixes opt into template rendering. This is a concise pattern for single-binary project generators.
Reusable code shape:
```rust
#[derive(rust_embed::Embed)]
#[folder = "templates"]
struct EmbeddedTemplates;

let write_file = |file: &str, data: &HashMap<&str, String>| -> anyhow::Result<()> {
    let p = PathBuf::from(file).components().skip(1).collect::<PathBuf>();
    let p = target_dir.join(p);
    let file_name = p.file_name().unwrap().to_string_lossy();

    let file_name = match &*file_name {
        "_gitignore" => ".gitignore",
        ".manifest" => return Ok(()),
        name if name.starts_with("%(") && name[1..].contains(")%") => {
            if !flags_match(name, pkg_manager, tauri_version) {
                return Ok(());
            }
            strip_flags(name)
        }
        name => name,
    };

    let (file_data, file_name) = if let Some(new_name) = file_name.strip_suffix(".lte") {
        let bytes = EmbeddedTemplates::get(file).unwrap().data.to_vec();
        (lte::render(bytes, data)?.into_bytes(), new_name)
    } else {
        (EmbeddedTemplates::get(file).unwrap().data.to_vec(), file_name)
    };

    fs::create_dir_all(p.parent().unwrap())?;
    fs::write(p.parent().unwrap().join(lte::render(file_name, data)?), file_data)?;
    Ok(())
};
```
Transfer rule: Apply when a CLI must generate many starter files without shipping an external template directory. Avoid for user-editable template packs; external directories are easier to override and debug.
Verification hook: Snapshot-test generated projects for each template/package-manager/version combination; assert `_base_` files are overridden by template-specific files where intended.

### Concept: Lightweight template engine with borrowed byte-slice tokens and AST execution
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/create-tauri-app/src/utils/lte.rs`
Why it matters: The `lte` module implements a tiny template language rather than pulling in a full templating crate. The lexer yields borrowed byte-slice tokens (`Var(&[u8])`, `Text(&[u8])`) and tracks whether it is inside `{% ... %}` brackets. The parser builds `Stmt::Text`, `Stmt::Var`, and `Stmt::If { negated, condition, else_condition }`; execution writes into any `Write` target and resolves variables from `HashMap<&str, V>` where `V: AsRef<[u8]>`. This is an agent-useful shape for narrowly scoped DSLs.
Reusable code shape:
```rust
enum Token<'a> {
    OBracket,
    CBracket,
    Bang,
    If,
    Var(&'a [u8]),
    Else,
    EndIf,
    Text(&'a [u8]),
    Invalid(usize, char),
}

enum Stmt<'a> {
    Text(&'a [u8]),
    Var(&'a [u8]),
    If {
        var: &'a [u8],
        negated: bool,
        condition: Vec<Stmt<'a>>,
        else_condition: Option<Vec<Stmt<'a>>>,
    },
}

pub fn render<T, V>(template: T, data: &HashMap<&str, V>) -> Result<String>
where
    T: AsRef<[u8]>,
    V: AsRef<[u8]>,
{
    let tokens: Vec<Token> = Lexer::new(template.as_ref()).collect();
    let mut parser = Parser::new(&tokens);
    let mut stmts = Vec::new();
    while let Some(stmt) = parser.next()? {
        stmts.push(stmt);
    }
    let mut out = Vec::new();
    for stmt in stmts {
        stmt.execute(&mut out, data)?;
    }
    String::from_utf8(out).map_err(|e| e.to_string().into())
}
```
Transfer rule: Apply only when the language is intentionally tiny and must be dependency-light. Avoid hand-rolled parsing when requirements include expressions, loops, escaping, includes, source maps, or untrusted templates; use a maintained parser/template crate then.
Verification hook: Keep tests for variable replacement, newlines, if/else, nested conditions, negation, missing variables, and invalid tokens. Review parser loop conditions carefully because small parser bugs often survive happy-path tests.

### Concept: Comment-stripping manifest parser with borrowed values and section-aware key handling
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/create-tauri-app/src/manifest.rs`
Why it matters: The manifest parser borrows string slices from the input, strips comments by splitting on `#`, ignores blank lines, switches behavior after `[files]`, and lets later repeated keys override earlier ones. That makes parsing cheap and adequate for a controlled template metadata file without introducing a TOML dependency.
Reusable code shape:
```rust
#[derive(Default, Clone, PartialEq, Eq, Debug)]
pub struct Manifest<'a> {
    pub before_dev_command: Option<&'a str>,
    pub before_build_command: Option<&'a str>,
    pub files: HashMap<&'a str, &'a str>,
}

impl<'a> Manifest<'a> {
    pub fn parse(s: &'a str) -> anyhow::Result<Self> {
        let mut manifest = Self::default();
        let mut in_files_section = false;

        for (i, line) in s.split('\n').enumerate() {
            let line_number = i + 1;
            let line = line.split('#').next().unwrap().trim();
            if line.is_empty() { continue; }
            if line == "[files]" {
                in_files_section = true;
                continue;
            }

            let Some((k, v)) = line.split_once('=') else { continue; };
            let (k, v) = (k.trim(), v.trim());
            if k.is_empty() || v.is_empty() {
                anyhow::bail!("parsing manifest: empty key/value in line {line_number}");
            }
            match k {
                "beforeDevCommand" => manifest.before_dev_command = Some(v),
                "beforeBuildCommand" => manifest.before_build_command = Some(v),
                _ if in_files_section => { manifest.files.insert(k, v); }
                _ => {}
            }
        }
        Ok(manifest)
    }
}
```
Transfer rule: Apply to controlled internal metadata where the grammar is tiny and comments/sections are enough. Avoid for user-facing config with escaping, arrays, nested sections, or values that may contain `#` or `=`.
Verification hook: Test comment stripping, repeated-key override, empty value failure, and `[files]` routing.

### Concept: Minimal N-API wrapper around a Rust CLI library entrypoint
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/create-tauri-app/node/src/lib.rs`, `/Users/amuldotexe/Desktop/reference-repos-yard/create-tauri-app/node/build.rs`
Why it matters: The Node binding crate exposes a single `#[napi]` function that forwards arguments to the Rust library, while `build.rs` calls `napi_build::setup()`. This keeps packaging concerns in the binding crate and leaves the main crate as the source of behavior. It is a clean shape for distributing a Rust scaffolder to npm without duplicating logic.
Reusable code shape:
```rust
// node/src/lib.rs
#[napi_derive::napi]
fn run(args: Vec<String>, bin_name: Option<String>, pkg_manager: Option<String>) {
    create_tauri_app::run(args, bin_name, pkg_manager);
}

// node/build.rs
fn main() {
    napi_build::setup();
}
```
Transfer rule: Apply when JavaScript users need a thin invocation bridge to a Rust core. Avoid putting CLI parsing or template generation in the binding crate; keep it as a forwarding shell.
Verification hook: Run the npm package smoke test and the Rust CLI tests against the same fixture arguments so both entrypoints stay behaviorally aligned.

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/datafusion

Codebase-memory: succeeded at `/tmp/codex-code-intel/codebase-memory/datafusion-20260706-223407`; used as discovery only. Source verification used `rg` plus direct reads of `datafusion/physical-plan/src/execution_plan.rs`, `datafusion/common/src/tree_node.rs`, `datafusion/optimizer/src/optimizer.rs`, `datafusion/core/src/execution/session_state.rs`, `datafusion-cli/src/cli_context.rs`, `datafusion-cli/src/catalog.rs`, and `datafusion-cli/src/object_storage.rs`.

### Concept: Pull-based physical operators return `SendableRecordBatchStream`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/datafusion/datafusion/physical-plan/src/execution_plan.rs`
Why it matters: DataFusion's `ExecutionPlan::execute` API returns a pinned stream of Arrow `RecordBatch` values rather than eagerly computing output. The docs show three shapes: wrap a precomputed batch with `futures::stream::once`, lazily compute a batch when the stream is polled, or asynchronously create a stream and flatten it with `TryStreamExt::try_flatten`. This is the core async/concurrency shape for a query engine: plans describe work; streams perform work under task context and backpressure.
Reusable code shape:
```rust
fn execute(
    &self,
    partition: usize,
    context: Arc<TaskContext>,
) -> Result<SendableRecordBatchStream> {
    let fut = get_batch_stream();
    let stream = futures::stream::once(fut).try_flatten();
    Ok(Box::pin(RecordBatchStreamAdapter::new(
        self.schema.clone(),
        stream,
    )))
}
```
Transfer rule: Apply to Rust data-processing engines, parser pipelines, indexers, and agent tools that need lazy execution and backpressure. Avoid blocking inside stream polling; move CPU-heavy or blocking I/O work to cooperative tasks or `spawn_blocking`.
Verification hook: Operator tests should poll the returned stream, assert schema consistency, and include cancellation/drop tests for long-running streams.

### Concept: Generic tree traversal separates algorithms from AST/plan structure
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/datafusion/datafusion/common/src/tree_node.rs`
Why it matters: `TreeNode` abstracts inspection and rewriting over logical plans, physical plans, expressions, and plan-context wrappers. Implementors only provide `apply_children` and `map_children`; users get top-down `apply`, visitor-style `visit`, bottom-up `transform`, top-down `transform_down`, combined `transform_down_up`, and object-based `rewrite`. This avoids duplicating traversal logic across every AST and lets optimizer/analyzer code express "what changes" separately from "how to walk".
Reusable code shape:
```rust
pub trait TreeNode: Sized {
    fn rewrite<R: TreeNodeRewriter<Node = Self>>(
        self,
        rewriter: &mut R,
    ) -> Result<Transformed<Self>> {
        handle_transform_recursion!(
            rewriter.f_down(self),
            |child| child.rewrite(rewriter),
            |node| rewriter.f_up(node)
        )
    }

    fn exists<F: FnMut(&Self) -> Result<bool>>(&self, mut f: F) -> Result<bool> {
        let mut found = false;
        self.apply(|n| {
            Ok(if f(n)? {
                found = true;
                TreeNodeRecursion::Stop
            } else {
                TreeNodeRecursion::Continue
            })
        }).map(|_| found)
    }

    fn apply_children<'n, F: FnMut(&'n Self) -> Result<TreeNodeRecursion>>(&'n self, f: F)
        -> Result<TreeNodeRecursion>;
    fn map_children<F: FnMut(Self) -> Result<Transformed<Self>>>(self, f: F)
        -> Result<Transformed<Self>>;
}
```
Transfer rule: Apply when several tree-like types need the same visitors/rewriters, especially parsers, compilers, query plans, and code intelligence graphs. Avoid if the tree is tiny and only one traversal exists; the abstraction cost is only worth it when algorithms multiply.
Verification hook: Add traversal-order tests and early-stop tests; for rewriters, assert unchanged nodes return `Transformed::no` to avoid fixed-point loops.

### Concept: Fixed-point optimizer with ordered rules, apply-order delegation, and invariant checks
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/datafusion/datafusion/optimizer/src/optimizer.rs`, `/Users/amuldotexe/Desktop/oss-read-only/datafusion/datafusion/core/src/execution/session_state.rs`
Why it matters: `OptimizerRule` has a human-readable `name`, optional `ApplyOrder` (`TopDown`, `BottomUp`, or `None` if the rule owns recursion), and a `rewrite` method returning `Transformed<LogicalPlan>`. The optimizer applies a carefully ordered rule list across multiple passes, tracks logical-plan signatures to stop at a fixed point, checks invariants before and after rules, and optionally skips failed rules by restoring the previous plan. `SessionStateBuilder` exposes hooks to replace or append logical and physical optimizer rules.
Reusable code shape:
```rust
pub trait OptimizerRule: Debug {
    fn name(&self) -> &str;
    fn apply_order(&self) -> Option<ApplyOrder> { None }
    fn rewrite(
        &self,
        plan: LogicalPlan,
        config: &dyn OptimizerConfig,
    ) -> Result<Transformed<LogicalPlan>, DataFusionError>;
}

for rule in &self.rules {
    let prev_plan = options.optimizer.skip_failed_rules.then(|| new_plan.clone());
    let result = match rule.apply_order() {
        Some(order) => new_plan.rewrite_with_subqueries(
            &mut Rewriter::new(order, rule.as_ref(), config),
        ),
        None => rule.rewrite(new_plan, config),
    }
    .and_then(|tnr| {
        assert_valid_optimization(&tnr.data, &starting_schema)?;
        Ok(tnr)
    });
    // success: keep data; skipped failure: restore prev_plan; hard failure: return Err
}
```
Transfer rule: Apply to compiler passes, AST simplifiers, dataflow optimizers, and agent planning rewrites where rules must compose until stable. Avoid name-based semantic rewrites for overridable functions; DataFusion explicitly warns rules should consult function traits/semantics instead of checking names like `"sum"`.
Verification hook: Track fixed-point signatures, cap max passes, run invariants after each rule, and expose an observer callback for plan snapshots in tests.

### Concept: CLI abstraction over `SessionContext` for testable query-shell commands
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/datafusion/datafusion-cli/src/cli_context.rs`
Why it matters: The CLI defines a `CliSessionContext` trait implemented for DataFusion's `SessionContext`. Commands depend on the trait instead of the concrete session, which lets tests or embedding applications provide alternate contexts while preserving access to task context, session state, object-store registration, table-option extensions, and logical-plan execution.
Reusable code shape:
```rust
#[async_trait::async_trait]
pub trait CliSessionContext {
    fn task_ctx(&self) -> Arc<TaskContext>;
    fn session_state(&self) -> SessionState;
    fn register_object_store(
        &self,
        url: &url::Url,
        object_store: Arc<dyn ObjectStore>,
    ) -> Option<Arc<dyn ObjectStore + 'static>>;
    fn register_table_options_extension_from_scheme(&self, scheme: &str);
    async fn execute_logical_plan(&self, plan: LogicalPlan) -> Result<DataFrame, DataFusionError>;
}

#[async_trait::async_trait]
impl CliSessionContext for SessionContext {
    fn task_ctx(&self) -> Arc<TaskContext> { self.task_ctx() }
    fn session_state(&self) -> SessionState { self.state() }
    async fn execute_logical_plan(&self, plan: LogicalPlan) -> Result<DataFrame, DataFusionError> {
        self.execute_logical_plan(plan).await
    }
}
```
Transfer rule: Apply to CLIs over large runtime contexts where commands need a narrow, mockable boundary. Avoid exposing the entire concrete context when commands only need a handful of capabilities.
Verification hook: Command parser tests can use `SessionContext` directly for default behavior and custom trait implementations for edge cases.

### Concept: Dynamic object-store schema provider resolves table names as URLs on demand
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/datafusion/datafusion-cli/src/catalog.rs`, `/Users/amuldotexe/Desktop/oss-read-only/datafusion/datafusion-cli/src/object_storage.rs`
Why it matters: `DynamicObjectStoreSchemaProvider::table` first asks the inner schema provider. If no table exists, it treats the table name as a `ListingTableUrl`, substitutes `~`, checks whether the runtime has an object store for the URL, inserts cloud-specific table option extensions by scheme, constructs the object store (`s3`, `oss`, `cos`, `gs`/`gcs`, `http`/`https`, or registry fallback), registers it, and then asks the inner provider again. This turns ad-hoc CLI references like remote paths into registered queryable tables lazily.
Reusable code shape:
```rust
async fn table(&self, name: &str) -> Result<Option<Arc<dyn TableProvider>>> {
    if let Some(table) = self.inner.table(name).await? {
        return Ok(Some(table));
    }

    let mut state = self.state.upgrade().ok_or_else(|| plan_datafusion_err!("locking error"))?
        .read()
        .clone();
    let mut builder = SessionStateBuilder::from(state.clone());
    let table_url = ListingTableUrl::parse(substitute_tilde(name.to_owned()).as_str())?;
    let url = table_url.as_ref();

    if state.runtime_env().object_store_registry.get_store(url).is_err() {
        match table_url.scheme() {
            "s3" | "oss" | "cos" => builder.table_options().unwrap().extensions.insert(AwsOptions::default()),
            "gs" | "gcs" => builder.table_options().unwrap().extensions.insert(GcpOptions::default()),
            _ => {}
        }
        state = builder.build();
        let store = get_object_store(&state, table_url.scheme(), url, &state.default_table_options(), false).await?;
        state.runtime_env().register_object_store(url, store);
    }

    self.inner.table(name).await
}
```
Transfer rule: Apply to query shells and data tools where identifiers may reference local or remote datasets. Avoid silently treating arbitrary missing table names as URLs in security-sensitive systems; require explicit schemes or allowlists.
Verification hook: Test every scheme branch with fake/in-memory object stores; assert unsupported schemes produce a clear `DataFusionError`.

## Repo Coverage: /Users/amuldotexe/Desktop/oss-read-only/opendal

Codebase-memory: scan succeeded at `/tmp/codex-code-intel/codebase-memory/opendal-20260706-223405`; graph output was used only for discovery and these claims were verified against source.

### Concept: Capability-oriented storage backend trait with unsupported defaults
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/opendal/core/core/src/raw/accessor.rs`
Why it matters: OpenDAL's low-level `Access` trait makes every storage backend advertise an `AccessorInfo` and associated operation types (`Reader`, `Writer`, `Lister`, `Deleter`) while giving every operation a default `Unsupported` error. This is a strong plugin shape: implementors can add only the operations a service supports, and the public operator layer can ask capabilities without encoding backend-specific branches everywhere.
Reusable code shape:
```rust
pub trait Access: Send + Sync + Debug + Unpin + 'static {
    type Reader: oio::Read;
    type Writer: oio::Write;
    type Lister: oio::List;
    type Deleter: oio::Delete;

    fn info(&self) -> Arc<AccessorInfo>;

    fn read(&self, path: &str, args: OpRead)
        -> impl Future<Output = Result<(RpRead, Self::Reader)>> + MaybeSend {
        let _ = (path, args);
        async { Err(Error::new(ErrorKind::Unsupported, "operation is not supported")) }
    }
}
```
Transfer rule: Apply when building provider ecosystems over many backends with partial feature support. Avoid pretending every backend supports every verb; default to explicit `Unsupported` and expose capability metadata.
Verification hook: Backend conformance tests should assert unsupported operations produce `ErrorKind::Unsupported`, and capability tests should match `AccessorInfo` flags to implemented methods.

### Concept: Static-dispatch middleware layers with type erasure only at the boundary
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/opendal/core/core/src/raw/layer.rs`, `/Users/amuldotexe/Desktop/oss-read-only/opendal/core/core/src/types/operator/builder.rs`
Why it matters: `Layer<A>` transforms one concrete accessor into another concrete accessor, preserving static dispatch while composing middleware such as error context, simulation, completion, and correctness checks. `OperatorBuilder::finish` type-erases the layered stack once, after the stack is complete. This keeps extension points cheap and strongly typed without leaking a huge generic type to users.
Reusable code shape:
```rust
pub trait Layer<A: Access> {
    type LayeredAccess: Access;
    fn layer(&self, inner: A) -> Self::LayeredAccess;
}

impl<A: Access> OperatorBuilder<A> {
    pub fn layer<L: Layer<A>>(self, layer: L) -> OperatorBuilder<L::LayeredAccess> {
        OperatorBuilder::new(layer.layer(self.accessor))
    }

    pub fn finish(self) -> Operator {
        let accessor = TypeEraseLayer.layer(self.accessor);
        Operator::from_inner(Arc::new(accessor))
    }
}
```
Transfer rule: Apply to HTTP clients, storage stacks, compiler services, and parsers that need reusable middleware but should keep a simple public handle. Avoid type erasure at every layer; erase after composition.
Verification hook: Unit-test layer ordering by injecting a tracing layer, and compile-test custom layers to ensure the associated `LayeredAccess` satisfies the backend trait.

### Concept: Error-context middleware that enriches every failing operation
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/opendal/core/core/src/layers/error_context.rs`, `/Users/amuldotexe/Desktop/oss-read-only/opendal/core/core/src/types/error.rs`
Why it matters: The error context layer wraps each operation and maps errors to include service name, operation, path, range, and contextual fields. The core error type separates `ErrorKind`, retry status (`Permanent`, `Temporary`, `Persistent`), operation, context pairs, source, and optional backtrace. This gives agentic debuggers structured facts instead of parsing free-form error strings.
Reusable code shape:
```rust
fn read(&self, path: &str, args: OpRead)
    -> impl Future<Output = Result<(RpRead, Self::Reader)>> + MaybeSend {
    let path = path.to_string();
    let range = args.range().to_string();
    async move {
        self.inner.read(&path, args).await.map_err(|err| {
            err.with_operation(Operation::Read)
                .with_context("service", self.info.name())
                .with_context("path", &path)
                .with_context("range", range)
        })
    }
}
```
Transfer rule: Apply whenever errors cross service or plugin boundaries. Avoid replacing structured context with formatted strings; keep fields queryable for retries, logs, and tests.
Verification hook: Assert representative failures render with operation and context, and assert retry policy keys off `ErrorStatus` rather than substring matching.

### Concept: Awaitable operation builder using `IntoFuture`
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/opendal/core/core/src/types/operator/operator_futures.rs`, `/Users/amuldotexe/Desktop/oss-read-only/opendal/core/core/src/raw/ops.rs`
Why it matters: OpenDAL exposes ergonomic calls like `op.read_with("path").range(..).concurrent(4).await` by storing the accessor, path, operation arguments, and function pointer in an `OperatorFuture`. Builder methods mutate the operation arguments, and `IntoFuture` converts the configured object into the real async operation. This gives fluent APIs without making every option method async.
Reusable code shape:
```rust
pub struct OperatorFuture<I, O, F> {
    acc: Accessor,
    path: String,
    args: I,
    f: F,
}

impl FutureRead {
    pub fn range(mut self, range: impl RangeBounds<u64>) -> Self {
        self.inner.args.set_range(range.into());
        self
    }
}

impl IntoFuture for FutureRead {
    type Output = Result<Buffer>;
    type IntoFuture = BoxedStaticFuture<Self::Output>;

    fn into_future(self) -> Self::IntoFuture {
        Box::pin(async move { (self.inner.f)(self.inner.acc, self.inner.path, self.inner.args).await })
    }
}
```
Transfer rule: Apply to async clients with many per-call options: storage reads, HTTP requests, query execution, or parser configuration. Avoid consuming network resources before `.await`; the builder should stay side-effect-free.
Verification hook: Builder tests can inspect internal `OpRead` values before execution, while integration tests assert fluent chains behave identically to explicit options structs.


## Skipped Repo: `/Users/amuldotexe/Desktop/oss-read-only/agent-debate`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/agent-debate`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/agent-debate -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/oss-read-only/clarity-cli`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/clarity-cli`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/clarity-cli -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/oss-read-only/ibis`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/ibis`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/ibis -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/oss-read-only/pinot`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/pinot`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/pinot -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/oss-read-only/scikit-learn`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/scikit-learn`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/scikit-learn -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/oss-read-only/vaex`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/oss-read-only/vaex`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/oss-read-only/vaex -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/Arithmancy2025`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/Arithmancy2025`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/Arithmancy2025 -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/Viz-Wizard`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/Viz-Wizard`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/Viz-Wizard -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/backlog-experiments`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/backlog-experiments`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/backlog-experiments -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/dima-20241129 -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/extract_twitter202304`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/extract_twitter202304`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/extract_twitter202304 -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/games-001`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/games-001`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/games-001 -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/journal-202401`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/journal-202401`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/journal-202401 -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/mission-grindelwald`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/mission-grindelwald`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/mission-grindelwald -g 'Cargo.toml' -g '*.rs'`


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve2024`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/pensieve2024`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/pensieve2024 -g 'Cargo.toml' -g '*.rs'`


## Repo Coverage: `/Users/amuldotexe/Desktop/personal-repos-lane/smallest-exp-20260404`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From smallest-exp-20260404
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/smallest-exp-20260404/smallest-ai-python-sdk-realtime/rust-core/crates/smallest_sidecar_server/src/main.rs:23` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 6 Rust files, 5 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
create_default_provider()
    };

    runtime.block_on(async {
        let (listener, address) = bind_local_listener(&LocalServerConfig::default()).await?;
        println!("smallest_sidecar_server_listening={address}");
        serve_listener_forever(listener, provider).await
    })
}
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/personal-repos-lane/smallest-exp-20260404 -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Skipped Repo: `/Users/amuldotexe/Desktop/personal-repos-lane/zzJS-TS-notes-2023`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/personal-repos-lane/zzJS-TS-notes-2023`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/personal-repos-lane/zzJS-TS-notes-2023 -g 'Cargo.toml' -g '*.rs'`


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/GitNexus`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Rust Architecture Slice From GitNexus
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/GitNexus/gitnexus/test/fixtures/sample-code/simple.rs` (sample Rust source file)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 1 Rust files, 0 Cargo manifests, and 0 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. No parser keyword sample was captured; treat this as a general Rust architecture or idiom candidate.
Reusable code shape:
```rust
pub fn public_function(x: i32) -> i32 {
    x + 1
}

fn private_function() -> &'static str {
    "private"
}

pub struct Config {
    pub name: String,
}

impl Config {
    pub fn new(name: &str) -> Self {
        Config { name: name.to_string() }
    }
}
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/GitNexus -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/argus`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From argus
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/argus/examples/hello-server/src/main.rs:14` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 89 Rust files, 19 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
}

#[tokio::main]
async fn main() {
  let app = Router::new()
    .route("/login", get(login));

  let listener = TcpListener::bind("0.0.0.0:3000")
    .await.unwrap();
  axum::serve(listener, app).await.unwrap();
}
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/argus -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/flowistry`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From flowistry
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/flowistry/crates/flowistry/src/extensions.rs:24` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 52 Rust files, 8 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
match s {
      "DistinguishMut" => Ok(Self::DistinguishMut),
      "IgnoreMut" => Ok(Self::IgnoreMut),
      _ => Err(format!("Could not parse: {s}")),
    }
  }
}

/// Whether Flowistry should attempt to recurse into call-sites to analyze them
#[derive(Debug, PartialEq, Eq, Clone, Copy, Deserialize, Serialize, Hash)]
pub enum ContextMode {
  /// Imprecise behavior, only use the modular approximation
  SigOnly,
  /// Precise behavior, recurse into call sites when possible
  Recurse,
}

impl FromStr for ContextMode {
  type Err = String;
  fn from_str(s: &str) -> Result<Self, Self::Err> {
    match s {
      "SigOnly" => Ok(Self::SigOnly),
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/flowistry -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/lockbud`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From lockbud
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/lockbud/src/callbacks.rs:117` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 52 Rust files, 18 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
})
            .collect();
        let mut callgraph = CallGraph::new();
        let typing_env = TypingEnv::fully_monomorphized();
        callgraph.analyze(instances.clone(), tcx, typing_env);
        let mut alias_analysis = AliasAnalysis::new(tcx, &callgraph);
        match self.options.detector_kind {
            DetectorKind::Deadlock => {
                debug!("Detecting deadlock");
                let mut deadlock_detector = DeadlockDetector::new(tcx, typing_env);
                let reports = deadlock_detector.detect(&callgraph, &mut alias_analysis);
                if !reports.is_empty() {
                    let j = serde_json::to_string_pretty(&reports).unwrap();
                    warn!("{}", j);
                    let stats = report_stats(&crate_name, &reports);
                    warn!("{}", stats);
                }
            }
            DetectorKind::AtomicityViolation => {
                debug!("Detecting atomicity violation");
                let mut atomicity_violation_detector = AtomicityViolationDetector::new(tcx);
                let reports = atomicity_violation_detector.detect(&callgraph, &mut alias_analysis);
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/lockbud -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/paralegal`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Parser Boundary Pattern From paralegal
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/paralegal/crates/paralegal-compiler/src/optimizer.rs:92` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 143 Rust files, 32 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
right: _,
                            typ,
                        } => !matches!(typ, Binop::AssociatedCallSite),
                        Relation::Negation(_) => unreachable!("Double negation should not parse"),
                        Relation::IsMarked(..) => true,
                    },
                    Relation::IsMarked(..) => true,
                };
                if !is_eligible {
                    handle_ineligibility(relation, &mut intros);
                }
            }
            // The body of the always_happens_before() call uses contains() to check for membership,
            // which doesn't exist if we
            ASTNodeType::OnlyVia(_, _, _) => {
                return;
            }
        }
    }

    // Get all the variables that are only introduced once in the whole policy
    // We can reclassify these as definitions and initialize them once, so we don't repeat graph traversals in inner loops.
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/paralegal -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Repo Coverage: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_cranelift`

Coordinator completion note: this section was added after parallel workers stopped, using `rust-patterns-scan-summary.json` plus direct source reads. Codebase-memory graph indexing was not rerun here; source paths below are the authority.

### Concept: Rust Architecture Slice From rustc_codegen_cranelift
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_cranelift/src/common.rs:75` (parser keyword hit)
Why it matters: This repo contributes a bounded source-backed Rust pattern during coordinator completion. The scan saw 76 Rust files, 2 Cargo manifests, and 50 sampled parser or parser-adjacent hits. The reusable value is not the whole project; it is the transfer shape visible in the cited source window. Parser-adjacent terms were present in the scan, so treat this as a syntax/code-intelligence candidate.
Reusable code shape:
```rust
},
        ty::FnPtr(..) => pointer_ty(tcx),
        ty::RawPtr(pointee_ty, _) | ty::Ref(_, pointee_ty, _) => {
            if tcx.type_has_metadata(*pointee_ty, ty::TypingEnv::fully_monomorphized()) {
                return None;
            } else {
                pointer_ty(tcx)
            }
        }
        ty::Param(_) => bug!("ty param {:?}", ty),
        _ => return None,
    })
}

fn clif_pair_type_from_ty<'tcx>(
    tcx: TyCtxt<'tcx>,
    ty: Ty<'tcx>,
) -> Option<(types::Type, types::Type)> {
    Some(match ty.kind() {
        ty::Tuple(types) if types.len() == 2 => {
            (clif_type_from_ty(tcx, types[0])?, clif_type_from_ty(tcx, types[1])?)
        }
```
Transfer rule: Apply this pattern when a new Rust task has the same boundary shape as the cited source: parser lowering, async boundary, no-std core, workspace structure, or verification harness. Avoid copying it blindly when the cited project context depends on generated code, project-specific macros, or external runtime contracts not present in the target system.
Verification hook: Re-open the cited file, run `rg -n "parser|parse|tree-sitter|tokio|async|Result|Error|test|trait|impl" /Users/amuldotexe/Desktop/reference-repos-yard/rustc_codegen_cranelift -g '*.rs' -g 'Cargo.toml'`, and add a smaller task-specific test before reusing the shape.


## Skipped Repo: `/Users/amuldotexe/Desktop/reference-repos-yard/twitter-circle`

### Concept: Repo skipped because no Rust source or Cargo manifest was present
Evidence: `/Users/amuldotexe/Desktop/reference-repos-yard/twitter-circle`; coordinator scan found rust_file_count=0 and cargo_manifest_count=0.
Why it matters: The Desktop-wide objective requires every repo to be browsed, but Rust reference volume quality improves when non-Rust repositories are recorded as explicit skips instead of being silently ignored.
Reusable code shape:
```text
N/A: no Rust source, Cargo manifest, or Rust parser implementation was present in the bounded scan.
```
Transfer rule: Skip Rust pattern extraction for this repo unless future work adds `Cargo.toml`, `*.rs`, a Rust binding, or a parser implementation relevant to Rust transfer.
Verification hook: `rg --files /Users/amuldotexe/Desktop/reference-repos-yard/twitter-circle -g 'Cargo.toml' -g '*.rs'`

## CodeGraphContext Evidence Appendix

### Concept: Interrupted Large-Repo Graph Index Requires Bounded Claims
Evidence: CodeGraphContext run `/tmp/codex-code-intel/codegraphcontext/datafusion-20260706-225543` was started for `/Users/amuldotexe/Desktop/oss-read-only/datafusion`, but `cgc stats` returned `Corrupted wal file` after the bounded interruption.
Why it matters: DataFusion is large enough that an interrupted local graph run can leave a database that looks present on disk but is not trustworthy for relationships. This gives agents a concrete rule: file presence is not evidence; a clean graph query plus source confirmation is evidence.
Reusable code shape:
```text
if cgc_stats_succeeds:
    use graph output as navigation
    confirm important findings in source
else:
    mark graph attempt as non-authoritative
    use rg plus source reads as authority
```
Transfer rule: Apply bounded graph claims to every large Rust research run. Never cite a CodeGraphContext database as authoritative unless a read query succeeds and the source confirms the finding.
Verification hook: Re-run `cgc stats` against `/tmp/codex-code-intel/codegraphcontext/datafusion-20260706-225543/ladybugdb.sqlite`; if it still reports WAL corruption, use the DataFusion source paths cited earlier in this shard as the only authority.
