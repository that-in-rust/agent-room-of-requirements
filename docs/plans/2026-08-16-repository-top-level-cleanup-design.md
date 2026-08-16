# Repository Top-Level Cleanup Design

## Goal

Make the repository immediately understandable to a new reader while preserving the
three established root-level entry documents:

- `A00-LLM-Principles01.md`
- `A01-LLM-Workflow01.md`
- `A02-Mega-Idiomatic-Prompt.md`

## Root Contract

The repository root contains only durable entry points and configuration:

```text
README.md
A00-LLM-Principles01.md
A01-LLM-Workflow01.md
A02-Mega-Idiomatic-Prompt.md
.gitignore
```

## Destination Areas

- `library/`: material intended for direct reuse, including the current idiomatic
  references and provider-specific skill collections.
- `methodology/`: prompts, templates, and executable-specification methods.
- `projects/`: specifications, progress journals, queues, tests, scripts, and
  retained review evidence belonging to a particular production effort.
- `research/`: strategic analysis and exploratory material.
- `roadmap/`: future portfolio and capability decisions.
- `archive/`: dated historical snapshots and backups.
- `docs/plans/`: approved design and implementation records.

## Key Decisions

- Preserve the 99 filenames under `library/idiomatic/202607/`; add navigational
  indexes rather than destabilizing their file-level links.
- Keep the section-review packets tracked, but move them beside the project they
  audit instead of leaving them as a root-level working area.
- Keep `CLAUDE.md` and `DOCUMENT_INDEX.md` in `unclassified-yet/`, outside the
  root-level user journey.
- Move dated Codex skill snapshots into the archive. Do not present them as a
  current `library/skills/codex/` collection until the external active collection
  has been intentionally curated and imported.
- Remove only empty, untracked local scaffolding after confirming that it has no
  tracked content.

## Validation

1. Confirm the root contains only the root contract plus purposeful directories.
2. Regenerate the Markdown document index and ensure every indexed target exists.
3. Search the repository for stale old-path references and repair internal links.
4. Run the idiomatic-reference evolution test suite from its new project location.
5. Verify the final working tree with `git diff --check` and `git status`.
