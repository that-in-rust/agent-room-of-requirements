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
| 1 | `meta-rust-ref-202606-Part1.md` | 1003-5319 | RED | 0 | 0 | 0 |
| 2 | `meta-rust-ref-202606-Part2.md` | 754-5188 | STUB | 0 | 0 | 0 |
| 3 | `meta-rust-ref-202606-Part3.md` | 1112-5162 | STUB | 0 | 0 | 0 |
| 4 | `meta-rust-ref-202606-Part4.md` | 975-5761 | STUB | 0 | 0 | 0 |
| 5 | `meta-rust-ref-202606-Part5.md` | 1214-5715 | STUB | 0 | 0 | 0 |
| 6 | `critique-JD-01.md` | 1-4166 | STUB | 0 | 0 | 0 |
| 7 | `critique-SD-01.md` (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |
| 8 | 19 June `generated-references` files (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |
| 9 | 7 JSON index files (deleted in pass 1, read from history) | all | STUB | 0 | 0 | 0 |

## Checkpoints

Newest first.

### Checkpoint 0
- Phase: STUB done for all nine units; RED started on file 1.
- Next step: read `meta-rust-ref-202606-Part1.md` from line 1003.
- Blockers: none.
