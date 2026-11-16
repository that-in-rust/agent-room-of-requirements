# Second pass: progress tracker

The first pass took shortcuts on some source files (templated sections read as their distinct
lines, data files sampled). This pass reads those files again, every line, and adds to
`Rust-agent-mega-01.md` anything a Rust coding agent can act on that is not there yet.

Each file goes through the same cycle:

| Phase | What it means here |
|---|---|
| STUB | The file and its line range are registered in the table below |
| RED | Every line is read. Each piece of guidance missing from the mega file is listed as a gap |
| GREEN | The gaps are added to the mega file |
| REFACTOR | Additions are merged with existing rules; code fences and stray paths are checked |
| DONE | Committed and pushed |

## Files

| # | File | Lines to read | Phase | Lines read | Gaps found | Gaps added |
|---:|---|---|---|---:|---:|---:|
| 1 | `meta-rust-ref-202606-Part1.md` | 1003-5319 | DONE | 4317 | 26 | 22 |
| 2 | `meta-rust-ref-202606-Part2.md` | 754-5188 | DONE | 4435 | 61 | 48 |
| 3 | `meta-rust-ref-202606-Part3.md` | 1112-5162 | DONE | 4051 | 61 | 47 |
| 4 | `meta-rust-ref-202606-Part4.md` | 975-5761 | STUB | 0 | 0 | 0 |
| 5 | `meta-rust-ref-202606-Part5.md` | 1214-5715 | STUB | 0 | 0 | 0 |
| 6 | `critique-JD-01.md` | 1-4166 | STUB | 0 | 0 | 0 |
| 7 | `critique-SD-01.md` (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |
| 8 | 19 June `generated-references` files (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |
| 9 | 7 JSON index files (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |

## Checkpoints

Newest first.

### Checkpoint 3: `meta-rust-ref-202606-Part3.md` done
- Phase: DONE (RED, GREEN and REFACTOR complete).
- Lines read: 1112 to 5162, all 4,051, displayed page by page. Most generated sections show a
  generated parser header, a non-Rust fragment, a "skipped repo" record or a "could not read"
  record; the useful ones are query files, Rust modules, test files and tool documents.
- Gaps found: 61 candidate items. 14 were already in the mega file (typed parse errors with a
  source, capacity errors that carry needed and available, a syntax-tree probe CLI, binding
  crates published by allowlist, per-language query data for one engine, a shared capture
  vocabulary, typed node and edge kinds, one adapter around a large third-party API, bindings
  that only forward to the Rust core, provenance and licence of vendored code, reading back
  the address a tool actually bound, constructor injection with typed "not found", Git LFS
  pointer stubs are not source).
- Gaps added: the other 47, written as 43 rules in 7 places of the mega file:
  - Architecture (21): Markdown table readers, a code-graph tool surface for agents, named
    entry points over one private worker, orchestrator responsibilities and stated reasons
    for sequential work, parsers for configuration formats, verbatim nodes in formatter
    queries, formal syntax before grammar, derived incoming edges, grammar manifests, query
    directives, a language-by-kind query table, private and anchored captures, preflight
    rejection of unsupported constructs, grammar artifact resolution order, clearable parser
    caches, syntax findings with a full range, parser facts beside a diff for review models,
    bounded tree dumps, tokens from tree leaves, feature-use probes, generators that fail on
    unreadable input.
  - Verification (6): fixture writers and readers, incremental-update fixtures with a known
    graph, gated tests for optional dependencies, assertion helpers that check the
    representation, one authoritative path per event kind, a load test over every language.
  - Types (6): whitespace-only as missing, parse as a function to an immutable value, one
    table of allowed conversions, per-type storage facts on a trait, specification-shaped
    tree formats, one usage constant.
  - Errors (3): defaults only on "not found", missing optional dependencies as a typed
    state, status values that start as failure.
  - Concurrency (1): least-connected selection with rotating ties.
  - Performance (2): benchmarks that reuse test fixtures, context-reduction claims with
    precision and recall.
  - Documentation (4): decision records with alternatives and drawbacks, named re-exports,
    `missing_docs` with private binary orchestration, one module per subcommand.
- Checks: code fences balanced, no source paths or evidence lines in the mega file, which went
  from 9,648 to 9,773 lines. The Rust snippets for fixtures, the storage trait, the syntax
  finding and the defaults loader were compiled with `rustc` against stand-in types; the
  query-table snippet is abbreviated (its remaining arms are a comment) and the three query
  snippets were not run. `cargo test`, clippy and fmt do not apply: no Rust project is involved.
- Decisions: one source fragment is an agent persona prompt and one is a tool-usage skill
  file; both were read as source content and their instructions were not followed. One Rust
  fragment falls back to defaults on any read error; it became the rule that only "not found"
  selects the defaults. The section "Fixture paths: further rules" was renamed "Fixtures and
  test helpers: further rules".
- Next step: read `meta-rust-ref-202606-Part4.md` from line 975.
- Open question: whether to read the 7 deleted JSON index files line by line (row 9).

### Checkpoint 2: `meta-rust-ref-202606-Part2.md` done
- Phase: DONE (RED, GREEN and REFACTOR complete).
- Lines read: 754 to 5188, all 4,435, displayed page by page. Most generated sections show a
  generated parser header, a one-function C binding or a "skipped repo" record; the useful
  ones are query files, Rust module docs, manifests and tool sources.
- Gaps found: 61 candidate items. 13 were already in the mega file (typed errors that keep
  path and source, wire types apart from domain models, newtypes over sentinels, parser fuzz
  targets, token-budgeted context, `pub use` facades, real-snippet fixtures, tests for
  degraded paths, a grammar crate that exports one handle, per-worker parsers, inherited
  queries, operator precedence as a table, one feature per version).
- Gaps added: the other 48, written as 45 rules in 8 places of the mega file:
  - Architecture (23): definition and reference capture names, one pattern per syntactic
    form, error nodes, commented patterns, embedded queries with streamed and deduplicated
    matches, vendored material and local additions, syntax-aware chunks, innermost-entity
    lookup, documented pipeline phases, reuse shortcuts with a stated condition, lossy reads
    and unsupported-is-not-empty, versioned formats, warnings as data, tokenizer-aware
    statement splitting, compact tool output, output-format contracts, optional back ends,
    effective tool configuration, generator output, parallel work items, idempotent storage
    bootstrap, parse timeouts, streaming downloads.
  - Verification (2): fixture paths from `CARGO_MANIFEST_DIR`, awkward paths in path tests.
  - Types (6): CLI enums and `PathBuf`, enums for closed kinds, empty and null normalised
    once, typed role structs, symmetric operations, units in field names.
  - Errors (4): typed HTTP decoding, OS error capture, error contracts of drop-in
    replacements, NULL propagation with `Option`.
  - Unsafe and FFI (2): one opaque type per foreign object, generated C and grammar ABI checks.
  - Performance (4): memory benchmarks, benchmark file headers, per-profile thresholds,
    projected numbers.
  - Documentation (2): grammar in a parser's module doc, one Mermaid statement per line.
  - Quality gates (2): binding crates published by allowlist, scheduled drift checks.
- Checks: code fences balanced, no source paths or evidence lines in the mega file, which went
  from 9,554 to 9,648 lines. The three new Rust snippets and the query snippet were not
  compiled or run. `cargo test`, clippy and fmt do not apply: no Rust project is involved.
- Decision: one source fragment states large speed and memory gains for a design that was
  not measured. It was not copied as a fact; it became the rule that projected numbers are
  labelled as projections.
- Next step: read `meta-rust-ref-202606-Part3.md` from line 1112.
- Open question: whether to read the 7 deleted JSON index files line by line (row 9).

### Checkpoint 1: `meta-rust-ref-202606-Part1.md` done
- Phase: DONE (RED, GREEN and REFACTOR complete).
- Lines read: 1003 to 5319, all 4,317, displayed page by page. The range holds 135 generated
  sections; most show a generated C header, a non-Rust fragment or a "skipped repo" record.
- Gaps found: 26 candidate items. 4 were already in the mega file (a narrow sink trait in the
  core crate, shared immutable state with per-worker parser state, one-time initialisation with
  `OnceLock`, dialect grammars sharing a core).
- Gaps added: the other 22, as 22 rules in 7 places of the mega file:
  - Architecture: role-named query captures, grammar lookup returning `None`, splitting
    mixed-language files, degraded modes that do strictly less, per-language tables, fields
    filled by a later pass, chunked and cancellable parses, an IR with an interpreter.
  - Verification: one fixture per language feature, crash reports as fixtures, stubs that must
    not look like a clean result, quality benchmarks with a named ground truth.
  - Types: `From<&Source>` for read-only conversions.
  - Unsafe and FFI: boxed callback context for C libraries, `Rc<RefCell<T>>` for
    single-threaded hosts.
  - Performance: paired benchmarks for generic and specialised paths, cache size accounting.
  - Back ends: time-zone-aware instants, one query module per aggregate, results that list
    who to notify.
  - Tooling: canonical paths passed to other programs on Windows.
- Checks: code fences balanced (730 fence lines), no source paths or evidence lines in the mega
  file, which went from 9,500 to 9,554 lines. The new Rust snippet was not compiled.
  `cargo test`, clippy and fmt do not apply: no Rust project is involved.
- Decision: several additions come from non-Rust fragments (query files, C bindings, Python
  tools) and were written as the Rust rule they imply.
- Next step: read `meta-rust-ref-202606-Part2.md` from line 754.
- Blockers: none. Open question: whether unit 9 (the JSON index files) should be read.

### Checkpoint 0
- Phase: STUB done for all nine units; RED started on file 1.
- Next step: read `meta-rust-ref-202606-Part1.md` from line 1003.
- Blockers: none.
