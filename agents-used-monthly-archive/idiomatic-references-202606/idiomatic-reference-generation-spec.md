# Idiomatic Reference Generation Spec

## Executable Requirements

### REQ-REF-001.0: Load authoritative theme inventory

**WHEN** the generation workstream starts from `agents-used-monthly-archive/idiomatic-references-202606/prd-idiomatic-202606.md`
**THEN** the system SHALL parse exactly the current table rows whose first column is a backticked four-word theme
**AND** SHALL treat each row as one required idiomatic reference file
**SHALL** fail verification when the parsed theme count differs from `99`

### REQ-REF-002.0: Create one file per theme

**WHEN** the theme inventory contains `99` themes
**THEN** the system SHALL create exactly `99` Markdown files under `agents-used-monthly-archive/idiomatic-references-202606/generated-references/`
**AND** SHALL name each file `<four_word_theme_label>.md`
**SHALL** reject extra, missing, duplicate, or differently named generated reference files

### REQ-REF-003.0: Consume complete local corpus

**WHEN** a theme row lists local source paths separated by `__`
**THEN** the generated reference file for that theme SHALL include every listed local path in a `local_corpus_source_map`
**AND** SHALL summarize the role of each local source path in the theme synthesis
**SHALL** fail verification when any listed local path is absent from that theme file

### REQ-REF-004.0: Research internet evidence sources

**WHEN** a theme has a public ecosystem, product, library, framework, API, or agent-design analogue
**THEN** the generated reference file SHALL include current internet research from primary documentation or maintainers where available
**AND** SHALL include GitHub repository, issue, release, discussion, or source-code evidence where available
**SHALL** label unavailable external evidence as `external_evidence_unavailable_reason` with a reason instead of inventing support

### REQ-REF-005.0: Follow A02 minimum structure

**WHEN** an idiomatic reference file is generated
**THEN** the file SHALL follow the minimum useful structure from `A02-Mega-Idiomatic-Prompt.md`
**AND** SHALL include source mapping, pattern scoring, idiomatic thesis, anti-pattern registry, verification gates, agent usage guidance, and refresh queries
**SHALL** allow additional parameters and deeper coverage when the theme requires them

### REQ-REF-006.0: Preserve four-word label discipline

**WHEN** a generated file introduces a reusable label, table column, pattern family, scoring factor, source category, risk category, output artifact, or verification gate
**THEN** that reusable label SHALL use exactly four semantic words in snake_case or prose form
**AND** SHALL avoid weak labels such as `metrics`, `tracing`, `security`, `tests`, `sources`, or `quality`
**SHALL** fail verification when a new backticked snake_case label is not four underscore-separated words

### REQ-REF-007.0: Produce reusable agent artifacts

**WHEN** a theme reference is complete
**THEN** it SHALL help an agent decide what to load, what to prefer, what to avoid, and how to verify work for that theme
**AND** SHALL include an `agent_usage_decision_guide` and `verification_gate_command_set`
**SHALL** avoid generic tutorials that do not change agent behavior

### REQ-REF-008.0: Track progress with TDD journal

**WHEN** implementation begins
**THEN** the workstream SHALL initialize a TDD progress journal using `tdd-task-progress-context-retainer`
**AND** SHALL record checkpoints after each batch of generated reference files, each verification failure, and each phase transition
**SHALL** keep the journal `Next Steps` section non-empty at every checkpoint

### REQ-REF-009.0: Maintain coverage manifest

**WHEN** each theme reference is generated or verified
**THEN** the workstream SHALL update `agents-used-monthly-archive/idiomatic-references-202606/reference-generation-coverage.md`
**AND** SHALL record theme, generated file path, local source count, external source count, verification status, and journal checkpoint link
**SHALL** fail completion when any of the 99 themes lacks a coverage row

### REQ-REF-010.0: Separate sourced facts from inference

**WHEN** a generated reference makes a recommendation
**THEN** it SHALL mark whether the claim is sourced from local corpus, sourced from external research, or inferred from combined evidence
**AND** SHALL include uncertainty notes for conflicts, stale sources, or missing primary documentation
**SHALL** reject unsourced recommendations that are presented as fact

## Test Matrix

| req_id | test_id | test_type | assertion | target |
| --- | --- | --- | --- | --- |
| REQ-REF-001.0 | TEST-SPEC-001 | inventory | parses 99 backticked four-word themes from PRD table | `prd-idiomatic-202606.md` |
| REQ-REF-002.0 | TEST-SPEC-002 | filesystem | generated directory contains exactly 99 theme-named Markdown files | `generated-references/` |
| REQ-REF-003.0 | TEST-SPEC-003 | corpus | every row source path appears in its matching generated file | generated theme files |
| REQ-REF-004.0 | TEST-SPEC-004 | research | every theme records external sources or explicit unavailable reason | generated theme files |
| REQ-REF-005.0 | TEST-SPEC-005 | structure | every generated file contains the required A02-derived sections | generated theme files |
| REQ-REF-006.0 | TEST-SPEC-006 | naming | every backticked snake_case reusable label has four words | generated theme files |
| REQ-REF-007.0 | TEST-SPEC-007 | utility | every file includes agent usage and verification guidance | generated theme files |
| REQ-REF-008.0 | TEST-SPEC-008 | journal | progress journal exists and latest checkpoint has non-empty next steps | progress journal |
| REQ-REF-009.0 | TEST-SPEC-009 | coverage | coverage manifest has one row for each theme and no duplicates | coverage manifest |
| REQ-REF-010.0 | TEST-SPEC-010 | evidence | recommendations distinguish local fact, external fact, and inference | generated theme files |

## TDD Plan

### STUB

1. Create verification harness stubs before generating references.
2. Define parser tests for the 99-theme PRD table.
3. Define fixture expectations for one representative theme with multiple local paths.
4. Initialize the TDD journal path:

```bash
python3 scripts/progress_journal_orchestrator.py init \
  --path agents-used-monthly-archive/idiomatic-references-202606/reference-generation-progress.md \
  --task "Generate 99 idiomatic reference files from PRD themes"
```

If the script is unavailable in this repo, create the journal manually using the schema from `tdd-task-progress-context-retainer`.

### RED

1. Run the verification harness before generating files.
2. Capture expected failures for missing `generated-references/`, missing coverage manifest, and absent theme files.
3. Record the RED checkpoint with failing test names and missing deliverables.

### GREEN

1. Process themes in small batches.
2. For each theme, read all listed local corpus paths.
3. Research current internet and GitHub evidence for that theme.
4. Generate `<four_word_theme_label>.md` using the A02-derived output contract.
5. Update `reference-generation-coverage.md`.
6. Update the progress journal after each completed batch.

### REFACTOR

1. Normalize repeated source-map and verification-gate structures.
2. Remove duplicated prose that does not improve agent decisions.
3. Tighten labels that fail the four-word reusable-label rule.
4. Preserve sourced fact, external fact, and inference boundaries.

### VERIFY

1. Run the complete verification harness.
2. Confirm `99` generated files, `99` coverage rows, and `99` completed themes.
3. Confirm every generated file references all local source paths from its PRD row.
4. Confirm every generated file includes external evidence or an explicit unavailable reason.
5. Capture a final journal checkpoint with phase `Refactor` or `Green`, exact verification status, and next steps.

## Quality Gates

### Inventory Verification Gate

```bash
python3 - <<'PY'
from pathlib import Path
prd = Path('agents-used-monthly-archive/idiomatic-references-202606/prd-idiomatic-202606.md')
themes = []
for line in prd.read_text().splitlines():
    if line.startswith('| `'):
        theme = line.split('|')[1].strip().strip('`')
        themes.append(theme)
assert len(themes) == 99, len(themes)
assert all(len(theme.split('_')) == 4 for theme in themes)
assert len(set(themes)) == len(themes)
print('inventory_ok', len(themes))
PY
```

### Generated File Count Gate

```bash
python3 - <<'PY'
from pathlib import Path
prd = Path('agents-used-monthly-archive/idiomatic-references-202606/prd-idiomatic-202606.md')
out = Path('agents-used-monthly-archive/idiomatic-references-202606/generated-references')
themes = [line.split('|')[1].strip().strip('`') for line in prd.read_text().splitlines() if line.startswith('| `')]
files = sorted(p.stem for p in out.glob('*.md')) if out.exists() else []
assert set(files) == set(themes), {'missing': sorted(set(themes)-set(files))[:5], 'extra': sorted(set(files)-set(themes))[:5]}
print('generated_files_ok', len(files))
PY
```

### Local Corpus Coverage Gate

```bash
python3 - <<'PY'
from pathlib import Path
prd = Path('agents-used-monthly-archive/idiomatic-references-202606/prd-idiomatic-202606.md')
out = Path('agents-used-monthly-archive/idiomatic-references-202606/generated-references')
failures = []
for line in prd.read_text().splitlines():
    if not line.startswith('| `'):
        continue
    cells = [cell.strip() for cell in line.strip('|').split('|')]
    theme = cells[0].strip('`')
    local_paths = [path.strip() for path in cells[1].split('__')]
    target = out / f'{theme}.md'
    text = target.read_text() if target.exists() else ''
    missing = [path for path in local_paths if path not in text]
    if missing:
        failures.append((theme, missing[:3]))
assert not failures, failures[:3]
print('local_corpus_ok')
PY
```

### A02 Structure Gate

```bash
python3 - <<'PY'
from pathlib import Path
out = Path('agents-used-monthly-archive/idiomatic-references-202606/generated-references')
required = [
    '## Source Evidence Mapping Table',
    '## Pattern Scoreboard Ranking Table',
    '## Idiomatic Thesis Synthesis Statement',
    '## Anti Pattern Registry Table',
    '## Verification Gate Command Set',
    '## Agent Usage Decision Guide',
    '## Future Refresh Search Queries',
]
failures = []
for path in out.glob('*.md'):
    text = path.read_text()
    missing = [section for section in required if section not in text]
    if missing:
        failures.append((str(path), missing))
assert not failures, failures[:3]
print('a02_structure_ok')
PY
```

### Four-Word Label Gate

```bash
python3 - <<'PY'
from pathlib import Path
import re
out = Path('agents-used-monthly-archive/idiomatic-references-202606/generated-references')
bad = []
for path in out.glob('*.md'):
    for label in re.findall(r'`([a-z][a-z0-9]*(?:_[a-z0-9]+)+)`', path.read_text()):
        if len(label.split('_')) != 4:
            bad.append((str(path), label))
assert not bad, bad[:10]
print('four_word_labels_ok')
PY
```

### Progress Journal Gate

```bash
python3 - <<'PY'
from pathlib import Path
journal = Path('agents-used-monthly-archive/idiomatic-references-202606/reference-generation-progress.md')
text = journal.read_text()
required = ['### Current Phase:', '### Tests Written:', '### Implementation Progress:', '### Current Focus:', '### Next Steps:', '### Context Notes:', '### Performance/Metrics:']
missing = [section for section in required if section not in text]
assert not missing, missing
assert '### Next Steps:\\n\\n' not in text
print('progress_journal_ok')
PY
```

### Coverage Manifest Gate

```bash
python3 - <<'PY'
from pathlib import Path
manifest = Path('agents-used-monthly-archive/idiomatic-references-202606/reference-generation-coverage.md')
rows = [line for line in manifest.read_text().splitlines() if line.startswith('| `')]
themes = [line.split('|')[1].strip().strip('`') for line in rows]
assert len(rows) == 99, len(rows)
assert len(set(themes)) == 99
print('coverage_manifest_ok', len(rows))
PY
```

## Open Questions

1. Should generated references live under `generated-references/` as specified, or should they be flat beside `prd-idiomatic-202606.md`?
2. Should internet/GitHub research require a minimum number of external sources per theme, or is `external_evidence_unavailable_reason` acceptable for internal-only agent workflow themes?
3. Should completion require committing the 99 generated files, coverage manifest, and journal, or only leaving them verified in the worktree?
