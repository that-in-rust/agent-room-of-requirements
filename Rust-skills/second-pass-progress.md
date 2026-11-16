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
| 2 | `meta-rust-ref-202606-Part2.md` | 754-5188 | RED | 0 | 0 | 0 |
| 3 | `meta-rust-ref-202606-Part3.md` | 1112-5162 | STUB | 0 | 0 | 0 |
| 4 | `meta-rust-ref-202606-Part4.md` | 975-5761 | STUB | 0 | 0 | 0 |
| 5 | `meta-rust-ref-202606-Part5.md` | 1214-5715 | STUB | 0 | 0 | 0 |
| 6 | `critique-JD-01.md` | 1-4166 | STUB | 0 | 0 | 0 |
| 7 | `critique-SD-01.md` (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |
| 8 | 19 June `generated-references` files (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |
| 9 | 7 JSON index files (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |

## Checkpoints

Newest first.

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
