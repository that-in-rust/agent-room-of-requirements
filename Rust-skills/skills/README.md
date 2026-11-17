# Rust skills

Each folder holds one `SKILL.md` that is complete on its own: an agent needs only the skill for the kind of Rust it is writing. They were built from `../Rust-agent-mega-02.md`, which stays as the archive.

| Skill | Tokens | For |
|---|---:|---|
| `rust-app-service` | 31,500 | application Rust - HTTP services, CRUD back ends, workers and queue consumers (Axum, Actix, sqlx, Diesel, Tower, Tokio) |
| `rust-cli` | 27,700 | command-line Rust - binaries, developer tools, batch jobs, cargo subcommands and tools that other programs or agents drive |
| `rust-infra-parsers` | 26,800 | Rust that reads and transforms source or structured text - parsers, lexers, linters, rule engines, code indexers and analysers (tree-sitter, `syn`, `nom`, `winnow`), compilers and lowering passes, diagnostics with spans, text edits and refactoring tools, registries of rules or back ends |
| `rust-infra-performance` | 30,000 | performance-critical and data-intensive Rust - hot loops, allocation and memory layout, benchmarks, caches, large collections, bulk and columnar data, CPU parallelism with threads and `rayon`, atomics and lock-heavy components, arenas, `no_std` and fixed-capacity code |
| `rust-infra-storage` | 26,600 | Rust that persists, frames or synchronises data - on-disk formats and caches, write-ahead logs and snapshots, content-addressed and incremental indexes, atomic file updates and text edits, binary and length-prefixed wire protocols, streaming decoders, patch and sync protocols, bounded queues and event pipelines |
| `rust-library` | 29,600 | library Rust - crates other code depends on, published or internal |
| `rust-review` | 10,900 | reviewing a Rust change or checking your own work before handoff |
| `rust-tauri` | 28,900 | building, changing, reviewing or hardening Tauri 2 desktop apps (Rust core plus web front end) |
| `rust-unsafe-ffi` | 24,600 | unsafe Rust and foreign-function interfaces |

Token counts are from the `o200k_base` tokenizer; other models differ somewhat.

**How to use them.** Write with the skill for the kind of Rust in the task, then check the result in a fresh pass with `rust-review`. A task that spans two kinds (a Tauri app with a sidecar parser) uses the skill for each part.

**Shared blocks.** Every writer skill ends with the same two blocks, copied in by `sync-core.sh`:

- `_essentials.md`: ownership, types, errors, async, tests, names and anti-patterns.
- `_core.md`: how to work, the gate commands and the definition of done. `rust-review` carries this one only.

Edit the shared files, never the copies, then run `./sync-core.sh`. The repetition is deliberate: no skill depends on another.
