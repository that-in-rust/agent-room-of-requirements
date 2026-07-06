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

### REQ-REF-011.0: Produce Shreyas-Doshi critique coverage

**WHEN** the `generated-references/` directory contains the verified `99` Markdown reference files
**THEN** the workstream SHALL create `agents-used-monthly-archive/idiomatic-references-202606/critique-SD-01.md`
**AND** SHALL include one section per generated reference with the file name as a Markdown header, the exact generated file path, and a fenced `text` critique block
**SHALL** fail verification when any generated reference file lacks exactly one critique section

### REQ-REF-012.0: Capture decision-quality critique findings

**WHEN** a generated reference is critiqued from a Shreyas Doshi product-strategy lens
**THEN** the critique block SHALL identify missing user journey clarity, missing decision tradeoffs, missing comprehensiveness, missing source synthesis, and concrete additions
**AND** SHALL include at least one theme-specific missing artifact such as a threat model, decision table, worked example, runbook, rubric, or checklist
**SHALL** avoid generic praise or summary-only review text

### REQ-REF-013.0: Upgrade references beyond evidence indexes

**WHEN** a generated reference is revised after critique
**THEN** the reference SHALL include a role-based opening scenario, primary user starting state, decision being made, and the trigger for opening that reference
**AND** SHALL include adopt/adapt/avoid guidance with the cost of being wrong for that theme
**SHALL** fail review when the file only lists sources, scores, and generic anti-patterns without guiding a concrete user decision

### REQ-REF-014.0: Synthesize local corpus hierarchy

**WHEN** a generated reference includes multiple local corpus paths or extracted heading signals
**THEN** the reference SHALL classify local sources as canonical, supporting, legacy, duplicate, or conflicting
**AND** SHALL convert the most important heading signals into ordered guidance or review questions
**SHALL** include a confidence warning when only one local corpus source exists

### REQ-REF-015.0: Add theme-specific completeness apparatus

**WHEN** a generated reference is intended for agent or human reuse
**THEN** it SHALL include one theme-specific artifact required by the critique, one good example, one bad example, one borderline case, and a completeness checklist
**AND** SHALL include metrics, leading indicators, or failure signals that show whether the reference improved the next task outcome
**SHALL** include adjacent-reference routing for cases where a neighboring reference is more appropriate

### REQ-REF-016.0: Track critique pass with TDD journal

**WHEN** the Shreyas-Doshi critique pass starts
**THEN** the workstream SHALL initialize `agents-used-monthly-archive/idiomatic-references-202606/critique-SD-progress.md` using `tdd-task-progress-context-retainer`
**AND** SHALL record RED and GREEN checkpoints for critique file existence, all-99 path coverage, and filename-header-plus-text-block formatting
**SHALL** keep the latest critique journal checkpoint aligned with the final verification output

### REQ-REF-017.0: Produce Jeff-Dean systems critique coverage

**WHEN** the `generated-references/` directory contains the verified `99` Markdown reference files
**THEN** the workstream SHALL create `agents-used-monthly-archive/idiomatic-references-202606/critique-JD-01.md`
**AND** SHALL include one section per generated reference with the file name as a Markdown header, the exact generated file path, and a fenced `text` critique block
**SHALL** fail verification when any generated reference file lacks exactly one Jeff-Dean critique section

### REQ-REF-018.0: Capture production-systems critique findings

**WHEN** a generated reference is critiqued from a Jeff Dean systems-engineering lens
**THEN** the critique block SHALL identify missing scale limits, reliability guarantees, operational robustness, technical grounding, production-load risks, and simplification opportunities
**AND** SHALL include explicit critique markers for scale model, reliability model, instrumentation, failure modes, backpressure, observability, and `p50/p95/p99 latency`
**SHALL** avoid generic framework enthusiasm, opinion-only advice, or recommendations without measurable production constraints

### REQ-REF-019.0: Upgrade references with production-readiness apparatus

**WHEN** a generated reference is revised after Jeff-Dean critique
**THEN** the reference SHALL include a workload model, reliability target, failure-mode table, retry/backpressure guidance, observability checklist, and measurable performance verification method
**AND** SHALL state where the guidance stops applying under distributed execution, long-running agent workflows, or large-codebase scale
**SHALL** fail review when the file contains best-practice claims without concrete capacity, latency, durability, or error-rate verification

### REQ-REF-020.0: Track Jeff-Dean critique pass with TDD journal

**WHEN** the Jeff-Dean critique pass starts
**THEN** the workstream SHALL initialize `agents-used-monthly-archive/idiomatic-references-202606/critique-JD-progress.md` using `tdd-task-progress-context-retainer`
**AND** SHALL record RED and GREEN checkpoints for critique file existence, all-99 path coverage, filename-header-plus-text-block formatting, and systems-marker coverage
**SHALL** keep the latest Jeff-Dean critique journal checkpoint aligned with the final verification output

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
| REQ-REF-011.0 | TEST-SPEC-011 | critique coverage | critique file has one filename header, exact path, and fenced text block per generated file | `critique-SD-01.md` |
| REQ-REF-012.0 | TEST-SPEC-012 | critique quality | every critique block names missing user journey, tradeoffs, comprehensiveness, source synthesis, and concrete additions | `critique-SD-01.md` |
| REQ-REF-013.0 | TEST-SPEC-013 | decision utility | revised references include role scenario and adopt/adapt/avoid decision guidance | generated theme files |
| REQ-REF-014.0 | TEST-SPEC-014 | source synthesis | revised references classify local corpus sources and convert heading signals into guidance | generated theme files |
| REQ-REF-015.0 | TEST-SPEC-015 | completeness | revised references include theme artifact, good/bad/borderline examples, metrics, adjacent routing, and checklist | generated theme files |
| REQ-REF-016.0 | TEST-SPEC-016 | critique journal | critique progress journal records RED and GREEN checkpoints with latest verification metrics | `critique-SD-progress.md` |
| REQ-REF-017.0 | TEST-SPEC-017 | systems critique coverage | Jeff-Dean critique file has one filename header, exact path, and fenced text block per generated file | `critique-JD-01.md` |
| REQ-REF-018.0 | TEST-SPEC-018 | systems critique quality | every Jeff-Dean critique block names scale, reliability, instrumentation, failure modes, production-load risk, and simplification markers | `critique-JD-01.md` |
| REQ-REF-019.0 | TEST-SPEC-019 | production readiness | revised references include workload model, reliability target, failure table, retry/backpressure guidance, observability checklist, and measurable performance method | generated theme files |
| REQ-REF-020.0 | TEST-SPEC-020 | systems critique journal | Jeff-Dean critique progress journal records RED and GREEN checkpoints with final verification metrics | `critique-JD-progress.md` |

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
5. Promote generated files from evidence indexes into decision-quality operating references by adding user journey, source hierarchy, examples, and metrics.
6. Run a Shreyas-Doshi critique pass to identify missing comprehensiveness and convert the findings into a rewrite backlog.
7. Run a Jeff-Dean critique pass to identify missing scale models, reliability contracts, instrumentation, production-load boundaries, and simplification opportunities.
8. Convert Jeff-Dean findings into production-readiness apparatus for each reference: workload model, failure-mode table, retry/backpressure guidance, observability checklist, and measurable performance verification.

### VERIFY

1. Run the complete verification harness.
2. Confirm `99` generated files, `99` coverage rows, and `99` completed themes.
3. Confirm every generated file references all local source paths from its PRD row.
4. Confirm every generated file includes external evidence or an explicit unavailable reason.
5. Confirm `critique-SD-01.md` covers every generated file exactly once with filename header, exact path, and fenced critique block.
6. Confirm critique blocks name missing user journey, missing decision quality, missing comprehensiveness, missing source synthesis, and concrete additions.
7. Confirm `critique-JD-01.md` covers every generated file exactly once with filename header, exact path, and fenced critique block.
8. Confirm Jeff-Dean critique blocks name scale model, reliability model, instrumentation, failure modes, backpressure, observability, `p50/p95/p99 latency`, production-load risk, and simplification opportunities.
9. Confirm revised references include production-readiness apparatus before treating `REQ-REF-019.0` as complete.
10. Capture final generation and critique journal checkpoints with phase `Refactor` or `Green`, exact verification status, and next steps.

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

### Shreyas Critique Coverage Gate

```bash
python3 - <<'PY'
from pathlib import Path
import re
base = Path('agents-used-monthly-archive/idiomatic-references-202606')
critique = base / 'critique-SD-01.md'
generated = sorted((base / 'generated-references').glob('*.md'))
text = critique.read_text()
headers = re.findall(r'^## ([^\n]+\.md)$', text, flags=re.M)
blocks = re.findall(r'```text\n(.*?)\n```', text, flags=re.S)
assert len(generated) == 99, len(generated)
assert len(headers) == 99, len(headers)
assert len(set(headers)) == 99, len(set(headers))
assert len(blocks) == 99, len(blocks)
for path in generated:
    assert f'## {path.name}' in text, path.name
    assert text.count(f'Exact path: `{path}`') == 1, str(path)
print('shreyas_critique_coverage_ok', len(blocks))
PY
```

### Shreyas Critique Quality Gate

```bash
python3 - <<'PY'
from pathlib import Path
import re
critique = Path('agents-used-monthly-archive/idiomatic-references-202606/critique-SD-01.md')
blocks = re.findall(r'```text\n(.*?)\n```', critique.read_text(), flags=re.S)
required_markers = [
    'What is missing:',
    'What to add next:',
    'User and situation clarity:',
    'Decision quality:',
    'Evidence shape:',
    'Source synthesis gap:',
    'Theme-specific gap:',
    'Build the missing theme-specific artifact:',
]
failures = []
for index, block in enumerate(blocks, 1):
    missing = [marker for marker in required_markers if marker not in block]
    if missing:
        failures.append((index, missing))
assert not failures, failures[:5]
print('shreyas_critique_quality_ok', len(blocks))
PY
```

### Decision-Quality Reference Upgrade Gate

```bash
python3 - <<'PY'
from pathlib import Path
out = Path('agents-used-monthly-archive/idiomatic-references-202606/generated-references')
required_markers = [
    '## User Journey Scenario',
    '## Decision Tradeoff Guide',
    '## Local Corpus Hierarchy',
    '## Theme Specific Artifact',
    '## Worked Example Set',
    '## Completeness Checklist',
    '## Adjacent Reference Routing',
]
failures = []
for path in out.glob('*.md'):
    text = path.read_text()
    missing = [marker for marker in required_markers if marker not in text]
    if missing:
        failures.append((str(path), missing))
assert not failures, failures[:3]
print('decision_quality_reference_upgrade_ok')
PY
```

This gate is required for completed post-critique rewrite passes that implement `REQ-REF-013.0` through `REQ-REF-015.0`.

### Critique Progress Journal Gate

```bash
python3 - <<'PY'
from pathlib import Path
journal = Path('agents-used-monthly-archive/idiomatic-references-202606/critique-SD-progress.md')
text = journal.read_text()
required = [
    'Current Phase: Green',
    'test_critique_file_exists: passing',
    'test_all_99_reference_paths_present: passing',
    'test_each_section_has_header_and_text_block: passing',
    'verification_errors=0',
]
missing = [marker for marker in required if marker not in text]
assert not missing, missing
print('critique_progress_journal_ok')
PY
```

### Jeff Dean Critique Coverage Gate

```bash
python3 - <<'PY'
from pathlib import Path
import re
base = Path('agents-used-monthly-archive/idiomatic-references-202606')
critique = base / 'critique-JD-01.md'
generated = sorted((base / 'generated-references').glob('*.md'))
text = critique.read_text()
headers = re.findall(r'^## ([^\n]+\.md)$', text, flags=re.M)
blocks = re.findall(r'```text\n(.*?)\n```', text, flags=re.S)
assert len(generated) == 99, len(generated)
assert len(headers) == 99, len(headers)
assert len(set(headers)) == 99, len(set(headers))
assert len(blocks) == 99, len(blocks)
for path in generated:
    rel = path.as_posix()
    assert f'## {path.name}' in text, path.name
    assert text.count(f'Exact path: `{rel}`') == 1, rel
print('jeff_dean_critique_coverage_ok', len(blocks))
PY
```

### Jeff Dean Critique Quality Gate

```bash
python3 - <<'PY'
from pathlib import Path
import re
critique = Path('agents-used-monthly-archive/idiomatic-references-202606/critique-JD-01.md')
blocks = re.findall(r'```text\n(.*?)\n```', critique.read_text(), flags=re.S)
required_markers = [
    'Jeff Dean-style systems critique',
    'What is missing for scale, reliability, and operational robustness:',
    'Where the reference is too hand-wavy or not technically grounded:',
    'What concrete systems thinking should be added:',
    'Where it would fail under production load or large-codebase use:',
    'What should be simplified, made composable, or made measurable:',
    'Scale model:',
    'Reliability model:',
    'Instrumentation:',
    'Failure modes:',
    'backpressure',
    'observability',
    'p50/p95/p99 latency',
]
failures = []
for index, block in enumerate(blocks, 1):
    missing = [marker for marker in required_markers if marker not in block]
    if missing:
        failures.append((index, missing))
    if len(block.splitlines()) < 35:
        failures.append((index, ['critique block shorter than 35 lines']))
assert not failures, failures[:5]
print('jeff_dean_critique_quality_ok', len(blocks))
PY
```

### Production Readiness Reference Gate

```bash
python3 - <<'PY'
from pathlib import Path
out = Path('agents-used-monthly-archive/idiomatic-references-202606/generated-references')
required_markers = [
    '## Workload Model',
    '## Reliability Target',
    '## Failure Mode Table',
    '## Retry Backpressure Guidance',
    '## Observability Checklist',
    '## Performance Verification Method',
    '## Scale Boundary Statement',
]
failures = []
for path in out.glob('*.md'):
    text = path.read_text()
    missing = [marker for marker in required_markers if marker not in text]
    if missing:
        failures.append((str(path), missing))
assert not failures, failures[:3]
print('production_readiness_reference_ok')
PY
```

This gate is required for completed post-critique rewrite passes that implement `REQ-REF-019.0`.

### Jeff Dean Progress Journal Gate

```bash
python3 - <<'PY'
from pathlib import Path
journal = Path('agents-used-monthly-archive/idiomatic-references-202606/critique-JD-progress.md')
text = journal.read_text()
required = [
    'Current Phase: Green',
    'test_jd_critique_file_exists: passing',
    'test_all_99_reference_paths_present: passing',
    'test_each_section_has_header_and_text_block: passing',
    'test_jd_systems_markers_present: passing',
    'verification_errors=0',
]
missing = [marker for marker in required if marker not in text]
assert not missing, missing
print('jeff_dean_progress_journal_ok')
PY
```

## Open Questions

1. Should `REQ-REF-013.0` through `REQ-REF-015.0` become blockers for the current generated corpus, or should they define the next rewrite pass after `critique-SD-01.md`?
2. Should internet/GitHub research require a minimum number of external sources per theme, or is `external_evidence_unavailable_reason` acceptable for internal-only agent workflow themes?
3. Should Shreyas-Doshi critique output remain a separate review artifact, or should each critique item be converted into tracked rewrite issues per generated reference?
4. Should `REQ-REF-019.0` be applied to all 99 references immediately, or should production-readiness upgrades start with the highest-risk themes such as backend security, agent orchestration, observability, and long-running workflows?
5. Should production readiness use one universal SLO template, or should each theme define its own workload, latency, reliability, and failure-mode thresholds?
