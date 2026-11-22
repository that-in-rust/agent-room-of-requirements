# Library Reduction: Executable Specification

Status: `implementation-ready`. Baseline: commit `0dc7115` (993 tracked files).

This repository is being reduced to a small library in which each subject has exactly one
skill. The contracts below define "done". Each one is checked by
[`check.py`](check.py); the reduction is finished when every check passes.

```bash
python3 docs/specs/library-reduction/check.py
```

The method is the one in [A03](../../../A03-Executable-Specs01.md): the checks were written
first and fail against the baseline (RED), each merge commit turns some of them green (GREEN),
and cleanup happens only while they stay green (REFACTOR).

## Unchanged baseline

- The root documents A00, A01, A02 and A03 keep their content.
- The nine Rust skills keep their shared core embedded, so each works when loaded alone.
- No unique guidance is removed. Content leaves the tree only when it is a copy, a record of
  how documents were produced, or already present in a merged file.

## Contracts

### REQ-LIB-001.0: One copy of every file

**WHEN** the tracked files are hashed
**THEN** the repository SHALL contain no two files with identical content
**SHALL** ignore empty files.

### REQ-LIB-002.0: A small library

**WHEN** the tracked files are counted
**THEN** the repository SHALL contain at most 120 files.

### REQ-LIB-003.0: One skill per subject

**WHEN** an agent looks for guidance on one of the 18 subjects listed in `check.py`
**THEN** the repository SHALL provide `library/skills/<subject>/SKILL.md`
**AND** that file SHALL start with front matter holding a `name` and a `description`.

### REQ-LIB-004.0: A skill is one file, plus at most one reference

**WHEN** a directory under `library/skills/` is listed
**THEN** it SHALL hold `SKILL.md` and at most one more Markdown file, `reference.md`.

### REQ-LIB-005.0: No records of how documents were produced

**WHEN** the tree is listed
**THEN** `archive/`, `projects/` and `Rust-skills/sources/` SHALL be absent
**AND** no tracked file name SHALL contain `progress`, `coverage-ledger`, `evidence-index`,
`task-queue` or `question-packets`.

### REQ-LIB-006.0: References describe the subject, not their own production

**WHEN** a `reference.md` under `library/skills/` is read
**THEN** it SHALL NOT contain the phrases `seed bullet`, `the seed offers`, `in this pass`,
`this session` or `was read completely`.

### REQ-LIB-007.0: Third-party skills live in one attributed place

**WHEN** a skill copied from another project is kept
**THEN** it SHALL sit under `library/third-party/<project>/`
**AND** that directory SHALL hold the project's `LICENSE`
**AND** `library/third-party/ATTRIBUTION.md` SHALL name the project, its source URL and its
licence
**SHALL** keep verbatim only projects under the MIT licence; other projects appear in
`ATTRIBUTION.md` as links.

### REQ-LIB-008.0: The Rust skills still stand alone

**WHEN** any of the nine `Rust-skills/skills/rust-*/SKILL.md` files is read
**THEN** it SHALL contain the shared core block from `Rust-skills/skills/_core.md`.

### REQ-LIB-009.0: Root documents are untouched

**WHEN** A00, A01, A02 and A03 are compared with the baseline commit
**THEN** they SHALL be identical to it.

### REQ-LIB-010.0: One index for the whole library

**WHEN** `library/README.md` is read
**THEN** it SHALL link to every `SKILL.md` in the repository
**AND** every link in it SHALL resolve.

### REQ-LIB-011.0: No broken links

**WHEN** the relative links in tracked Markdown files outside `library/third-party/` are
resolved
**THEN** every target SHALL exist.

### REQ-LIB-012.0: No unique content lost

**WHEN** a source file is deleted after a merge
**THEN** each distinctive item recorded for it in the pre-reduction catalogue SHALL appear in
a merged file, or on the list of intentionally dropped items in the pull request.

This contract is checked during the work against the catalogue, which is a working file and
is not committed. `check.py` reports it as `MANUAL`.

## Requirement-to-check matrix

| Requirement | Check in `check.py` | Kind |
|---|---|---|
| REQ-LIB-001.0 | `check_no_identical_copies_remain` | script |
| REQ-LIB-002.0 | `check_tracked_file_count_limit` | script |
| REQ-LIB-003.0 | `check_every_subject_skill_exists` | script |
| REQ-LIB-004.0 | `check_skill_directories_stay_small` | script |
| REQ-LIB-005.0 | `check_no_production_records_remain` | script |
| REQ-LIB-006.0 | `check_references_omit_process_talk` | script |
| REQ-LIB-007.0 | `check_third_party_is_attributed` | script |
| REQ-LIB-008.0 | `check_rust_skills_embed_core` | script, baseline guard |
| REQ-LIB-009.0 | `check_root_documents_stay_unchanged` | script, baseline guard |
| REQ-LIB-010.0 | `check_library_index_links_skills` | script |
| REQ-LIB-011.0 | `check_relative_links_all_resolve` | script |
| REQ-LIB-012.0 | catalogue comparison, reported in the pull request | manual |
