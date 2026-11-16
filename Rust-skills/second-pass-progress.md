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
| 4 | `meta-rust-ref-202606-Part4.md` | 975-5761 | DONE | 4,787 | 71 | 61 |
| 5 | `meta-rust-ref-202606-Part5.md` | 1214-5715 | DONE | 4,502 | 77 | 55 |
| 6 | `critique-JD-01.md` | 1-4166 | DONE | 4,166 of 4,166 | 34 | 19 |
| 7 | `critique-SD-01.md` (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |
| 8 | 19 June `generated-references` files (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |
| 9 | 7 JSON index files (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |

## Checkpoints

Newest first.

### Checkpoint 6: `critique-JD-01.md`
- Phase: DONE.
- Lines read: 1 to 4166, all displayed. The file is 99 sections of one 42-line template; about
  35 lines per section repeat word for word and the rest come from roughly 12 topic variants.
- Gaps found: 34 candidate items. 15 were already in the mega file from the first pass (the
  production-readiness questions, the Rust and back-end signals, the Tauri block, test-loop
  health) or were not about Rust (front-end, Kotlin, Python, creative-art metrics).
- Gaps added: the other 19, as 19 rules: 4 working habits (debugging loop, boundary as a
  hypothesis, repository preflight, bounded agent steps), 2 documentation rules (reversible
  decision records, documentation checks), 1 back-end rule (replay-safe webhooks) and 12
  review checks (command, hook, integration, configuration, plugin, reproducible output,
  terminal width, operations model, threat model, crate health, rerunnable evidence, deferred
  refactoring).
- Checks: code fences balanced (756 fence lines), no source paths in the mega file, which went
  from 9,949 to 9,968 lines. The rustdoc command in the documentation rule was run on a scratch
  crate with a broken link. No other new rule contains code.
- Decision: the source is a critique of documents, not Rust code, so each rule is the Rust or
  agent practice the critique implies.
- Next step: restore `critique-SD-01.md` from git history and read it in 500-line steps,
  committing after each step.
- Blockers: none. Open question: whether unit 9 (the JSON index files) should be read.

### Checkpoint 5: `meta-rust-ref-202606-Part5.md` done
- Phase: DONE (RED, GREEN and REFACTOR complete).
- Lines read: 1214 to 5715, all 4,502, displayed page by page. About a third of the generated
  sections are identical generated parser headers or "skipped repo" records; the useful ones
  are Rust modules, query and grammar files, benchmarks, test files and tool documents.
- Gaps found: 77 candidate items. 22 were already in the mega file or not universal (a parser
  per worker thread, speed reported beside quality, benchmark set-up outside the measured
  closure, caller location in fail-fast helpers, minimum-version checks in CI, symbol-level
  context, scope queries, a small parser interface, an enclosing-declaration lookup, ordered
  type inference, glue code without language branches, a parse cache keyed by content hash,
  a search facade, a sink trait for lexer output, extension tie-breaks, folding queries, typed
  request models, kinds as enums, fixtures shared with benchmarks, public-API snapshots, and
  two product documents with nothing for Rust).
- Gaps added: the other 55, written as 52 rules in 11 places of the mega file:
  - Parsers and code intelligence (15): listener defaults with an error-node hook, two parsers
    behind one switch with a differential test, text edits applied from the highest offset,
    one macro line per bundled language, chunking through a strategy table with a fallback,
    a line-start index built once, incremental indexing that states what it can miss, named
    chunk limits, spans on every node, one thin binary per language, prose-bearing nodes only,
    linting query files with a query, dialect grammars that extend a base, lending query
    cursors, peeling wrapper nodes in one loop.
  - Types and inputs (12): sign against zero extension, named values at nullable C arguments,
    prompting only at a terminal, a child handle that borrows its parent, a parameters struct
    per algorithm, an empty trait with a blanket impl for a bound set, aliases for supported
    generic instantiations, constants without defaults and `Default` that cannot panic, derived
    views that borrow, arguments validated before expensive work, unsupported against empty,
    structs instead of documented tuple aliases.
  - Packaging and upkeep (6): an `include` allowlist checked with `cargo package --list`,
    workspace discovery through `cargo metadata`, pinned vendored sources with a drift check,
    narrow deprecation suppressions, the version as a compile-time constant, dependency
    reports with denominators and a cycle gate.
  - Fixtures and tests (4): one snapshot per case of a standard suite, a conservation invariant
    for binning, a grammar contract test, generated tests cut down after review.
  - Benchmarks and performance (4): token counts that name their tokenizer, cheap predicates
    first, one benchmark case per syntactic feature, the sparse set.
  - Foreign interfaces (3): binding-generator fixtures per macro form, one binding test per API
    member on every target, a binding crate as a thin shim.
  - Documentation (3): a page per stable error code, complete example programs, a legend and
    provenance line in shared data files.
  - Errors (2): a cause printed in one place only, the last good configuration kept on a failed
    reload.
  - Concurrency (1), web back ends (1), agent guardrails (1): an accept error that does not end
    the server, an allowlist for caller-supplied service URLs, review comments that record the
    commit they reviewed.
- Checks: code fences are balanced (756 markers) and no source path, evidence line or scan
  count is in the mega file. The Rust in 12 of the new rules (casts, the listener assertion,
  the blanket impl, the alias, borrowed views and handles, the sparse set, the terminal check,
  the version constant) compiles and runs in a scratch crate against stand-in types. The
  query-cursor loop, the `cargo metadata` rule and the manifest keys were not run.
- Limits: duplicates were checked by keyword search, so a rule worded differently may repeat
  an existing one. Most rules are inferred from 15-line fragments, many of them not Rust.
- Mega file: 9,896 to 9949 lines.
- Next: file 6, `critique-JD-01.md`, lines 1 to 4166.

### Checkpoint 4: `meta-rust-ref-202606-Part4.md` done
- Phase: DONE (RED, GREEN and REFACTOR complete).
- Lines read: 975 to 5761, all 4,787, displayed page by page. As in Part 3, most generated
  sections show a generated parser header, a non-Rust fragment, a "skipped repo" record or a
  "could not read" record; the useful ones are Rust modules, query files, test files and tool
  documents.
- Gaps found: 71 candidate items. 10 were already in the mega file (naming an anonymous
  function from its enclosing binding, 1-based inclusive spans, one precedence table for
  operators, namespaced output captures, a periodic task with an owned handle, one-time
  runtime initialisation, grammars behind Cargo features, one extractor per language behind a
  trait, a native handle released by its owner, a chunk callback for parsing a rope).
- Gaps added: the other 61, written as 60 rules in 11 places of the mega file:
  - Parsers and code intelligence (25): a parse result that keeps its source, analysis in side
    tables, a parse deadline that scales with input size, inheritance-only query files,
    identical per-language modules that re-export the grammar crate's queries, a registry that
    rejects duplicate extensions, stated unsupported edge kinds, keeping a kind a consumer
    needs, item spans that include attributes, containment edges, skipping minified and
    generated files, redaction before code leaves the machine, structural-clone hashing,
    checking proposed identifiers against the index, cheap-to-expensive exploration, smallest
    reproducer plus parser trace, reasons for grammar conflicts, conversion failures as parse
    errors, a 256-entry byte-class table, an enum per escape-sequence kind, a resumable framing
    decoder, inner selections, a plain-data query AST with a reserved prefix, a cookbook of
    executed queries, no numbered file parts glued by glob imports.
  - Tests (4): chunking equivalence for streaming parsers, out-parameters started at the wrong
    value, proof that a pre-built artefact was used, a test constructor for an embeddable
    service.
  - Types (6): several input shapes into one type, typed options per back end, a documented
    inference order, strings parsed to numbers and times at the boundary, operations with a
    result type and an id, a tagged command enum for a line protocol.
  - Errors (4): a corrupt store is not an empty one, progress in an algorithm's failure, the
    limit formatted from its constant, message and detail kept apart for a front end.
  - Concurrency (3): latest request wins for a debounced call, state through a callback via
    thread-local storage, parallel workers with one writer.
  - Measurement (7): gates stated before measuring and "NOT MET" reported plainly, backtests at
    historical commits, the allocator belongs to the binary, benchmark knobs from documented
    environment variables, one case per input shape, shared synthetic-data constants, reports
    that open with tool version and totals.
  - Documentation (5), macros (1), tooling and release (3), agent guardrails (2).
- Checks: code fences balanced; no source paths, evidence lines or repo names added. The two
  longer Rust snippets (the untagged input enum and the macro input parser) pass
  `cargo check` with warnings denied in a scratch crate with `serde` and `syn`. The
  per-language module snippet needs grammar crates and was not compiled. No tests, clippy or
  fmt apply to the Markdown file itself.
- Decisions: instruction-like text inside the source (an agent definition, a launch QA plan,
  a skill document) was read as source content and not acted on. Repository names, tool names
  and paths from the fragments were left out of the rules.
- Next: Part 5, lines 1214 to 5715.
- Open question: whether to read the 7 deleted JSON index files line by line.

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
