#!/usr/bin/env python3
"""Verify generated idiomatic reference files against the 202606 spec."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[3]
WORK_DIR = ROOT_DIR / "agents-used-monthly-archive/idiomatic-references-202606"
PRD_PATH = WORK_DIR / "prd-idiomatic-202606.md"
GENERATED_DIR = WORK_DIR / "generated-references"
COVERAGE_PATH = WORK_DIR / "reference-generation-coverage.md"
JOURNAL_PATH = WORK_DIR / "reference-generation-progress.md"
CRITIQUE_PATH = WORK_DIR / "critique-SD-01.md"
CRITIQUE_JOURNAL_PATH = WORK_DIR / "critique-SD-progress.md"
JEFF_CRITIQUE_PATH = WORK_DIR / "critique-JD-01.md"
JEFF_CRITIQUE_JOURNAL_PATH = WORK_DIR / "critique-JD-progress.md"

REQUIRED_SECTIONS = [
    "## Source Evidence Mapping Table",
    "## Pattern Scoreboard Ranking Table",
    "## Idiomatic Thesis Synthesis Statement",
    "## Local Corpus Source Map",
    "## External Research Source Map",
    "## Anti Pattern Registry Table",
    "## Verification Gate Command Set",
    "## Agent Usage Decision Guide",
    "## Future Refresh Search Queries",
    "## Evidence Boundary Notes",
    "## User Journey Scenario",
    "## Decision Tradeoff Guide",
    "## Local Corpus Hierarchy",
    "## Theme Specific Artifact",
    "## Worked Example Set",
    "## Outcome Metrics and Feedback Loops",
    "## Completeness Checklist",
    "## Adjacent Reference Routing",
    "## Workload Model",
    "## Reliability Target",
    "## Failure Mode Table",
    "## Retry Backpressure Guidance",
    "## Observability Checklist",
    "## Performance Verification Method",
    "## Scale Boundary Statement",
]

JOURNAL_SECTIONS = [
    "### Current Phase:",
    "### Tests Written:",
    "### Implementation Progress:",
    "### Current Focus:",
    "### Next Steps:",
    "### Context Notes:",
    "### Performance/Metrics:",
]


@dataclass(frozen=True)
class ThemeRow:
    theme: str
    local_paths: list[str]


def parse_theme_rows() -> list[ThemeRow]:
    rows: list[ThemeRow] = []
    for line in PRD_PATH.read_text().splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 2:
            raise AssertionError(f"bad table row shape: {line[:120]}")
        theme = cells[0].strip("`")
        local_paths = [path.strip() for path in cells[1].split("__") if path.strip()]
        rows.append(ThemeRow(theme=theme, local_paths=local_paths))
    return rows


def assert_inventory_valid(rows: list[ThemeRow]) -> None:
    assert len(rows) == 99, f"expected 99 themes, found {len(rows)}"
    themes = [row.theme for row in rows]
    assert len(set(themes)) == len(themes), "duplicate themes found"
    for theme in themes:
        assert len(theme.split("_")) == 4, f"theme is not four words: {theme}"
    local_paths = [path for row in rows for path in row.local_paths]
    assert len(local_paths) == len(set(local_paths)), "duplicate local source path found"
    missing = [path for path in local_paths if not (ROOT_DIR / path).exists()]
    assert not missing, f"local source paths missing: {missing[:5]}"


def assert_generated_files_valid(rows: list[ThemeRow]) -> None:
    assert GENERATED_DIR.exists(), f"missing generated directory: {GENERATED_DIR}"
    expected = {row.theme for row in rows}
    actual = {path.stem for path in GENERATED_DIR.glob("*.md")}
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    assert not missing and not extra, f"generated file mismatch missing={missing[:5]} extra={extra[:5]}"


def assert_theme_file_valid(row: ThemeRow) -> None:
    path = GENERATED_DIR / f"{row.theme}.md"
    assert path.exists(), f"{path}: generated theme file missing"
    text = path.read_text()
    missing_sections = [section for section in REQUIRED_SECTIONS if section not in text]
    assert not missing_sections, f"{path}: missing sections {missing_sections}"
    missing_paths = [local_path for local_path in row.local_paths if local_path not in text]
    assert not missing_paths, f"{path}: missing local paths {missing_paths[:5]}"
    assert (
        "external_research_sourced_fact" in text
        or "external_evidence_unavailable_reason" in text
    ), f"{path}: missing external evidence accounting"
    assert "local_corpus_sourced_fact" in text, f"{path}: missing local fact boundary"
    assert "combined_evidence_inference_note" in text, f"{path}: missing inference boundary"
    assert "agent_usage_decision_guide" in text, f"{path}: missing agent usage guide key"
    assert "verification_gate_command_set" in text, f"{path}: missing verification command key"
    decision_markers = [
        "Role based opening scenario:",
        "Primary user starting state:",
        "Decision being made:",
        "Reference opening trigger:",
        "Adopt when",
        "Adapt when",
        "Avoid when",
        "Cost of being wrong",
        "canonical",
        "supporting",
        "Theme specific artifact:",
        "Good example:",
        "Bad example:",
        "Borderline case:",
        "Leading indicator:",
        "Failure signal:",
        "Adjacent reference",
    ]
    missing_decision_markers = [marker for marker in decision_markers if marker not in text]
    assert not missing_decision_markers, f"{path}: missing decision markers {missing_decision_markers}"
    production_markers = [
        "primary_usage_surface",
        "bounded_capacity_model",
        "source_pressure_model",
        "artifact_pressure_model",
        "source_boundary_preservation",
        "decision_accuracy_sample",
        "unsupported_claim_rate",
        "recovery_path_clarity",
        "p50/p95/p99 latency",
        "backpressure",
        "distributed execution",
        "long-running agent workflows",
        "large-codebase scale",
    ]
    missing_production_markers = [marker for marker in production_markers if marker not in text]
    assert not missing_production_markers, f"{path}: missing production markers {missing_production_markers}"
    for label in re.findall(r"`([a-z][a-z0-9]*(?:_[a-z0-9]+)+)`", text):
        assert len(label.split("_")) == 4, f"{path}: non-four-word label `{label}`"
    assert not any(line.rstrip() != line for line in text.splitlines()), f"{path}: trailing whitespace"
    assert all(ord(ch) < 128 for ch in text), f"{path}: non-ascii character present"
    assert text.endswith("\n"), f"{path}: missing final newline"


def assert_coverage_manifest_valid(rows: list[ThemeRow]) -> None:
    assert COVERAGE_PATH.exists(), f"missing coverage manifest: {COVERAGE_PATH}"
    coverage_rows = [
        line for line in COVERAGE_PATH.read_text().splitlines() if line.startswith("| `")
    ]
    assert len(coverage_rows) == 99, f"expected 99 coverage rows, found {len(coverage_rows)}"
    themes = [line.split("|")[1].strip().strip("`") for line in coverage_rows]
    expected = {row.theme for row in rows}
    assert set(themes) == expected, "coverage themes do not match PRD themes"
    assert len(set(themes)) == len(themes), "duplicate coverage theme found"


def assert_progress_journal_valid() -> None:
    assert JOURNAL_PATH.exists(), f"missing progress journal: {JOURNAL_PATH}"
    text = JOURNAL_PATH.read_text()
    missing_sections = [section for section in JOURNAL_SECTIONS if section not in text]
    assert not missing_sections, f"journal missing sections: {missing_sections}"
    assert "### Next Steps:\n\n" not in text, "journal next steps are empty"
    assert "TEST-SPEC-" in text, "journal does not mention verification tests"


def assert_critique_coverage_valid(rows: list[ThemeRow]) -> None:
    assert CRITIQUE_PATH.exists(), f"missing critique file: {CRITIQUE_PATH}"
    text = CRITIQUE_PATH.read_text()
    headers = re.findall(r"^## ([^\n]+\.md)$", text, flags=re.M)
    blocks = re.findall(r"```text\n(.*?)\n```", text, flags=re.S)
    assert len(headers) == 99, f"expected 99 critique headers, found {len(headers)}"
    assert len(set(headers)) == len(headers), "duplicate critique headers found"
    assert len(blocks) == 99, f"expected 99 critique text blocks, found {len(blocks)}"
    for row in rows:
        generated_path = GENERATED_DIR / f"{row.theme}.md"
        assert f"## {generated_path.name}" in text, f"missing critique header for {generated_path.name}"
        assert (
            text.count(f"Exact path: `{generated_path.relative_to(ROOT_DIR)}`") == 1
        ), f"critique exact path not once: {generated_path.relative_to(ROOT_DIR)}"


def assert_critique_quality_valid() -> None:
    assert CRITIQUE_PATH.exists(), f"missing critique file: {CRITIQUE_PATH}"
    blocks = re.findall(r"```text\n(.*?)\n```", CRITIQUE_PATH.read_text(), flags=re.S)
    required_markers = [
        "What is missing:",
        "What to add next:",
        "User and situation clarity:",
        "Decision quality:",
        "Evidence shape:",
        "Source synthesis gap:",
        "Theme-specific gap:",
        "Build the missing theme-specific artifact:",
    ]
    failures: list[tuple[int, list[str]]] = []
    for index, block in enumerate(blocks, 1):
        missing = [marker for marker in required_markers if marker not in block]
        if missing:
            failures.append((index, missing))
    assert not failures, f"critique quality failures: {failures[:5]}"


def assert_critique_journal_valid() -> None:
    assert CRITIQUE_JOURNAL_PATH.exists(), f"missing critique journal: {CRITIQUE_JOURNAL_PATH}"
    text = CRITIQUE_JOURNAL_PATH.read_text()
    required = [
        "Current Phase: Green",
        "test_critique_file_exists: passing",
        "test_all_99_reference_paths_present: passing",
        "test_each_section_has_header_and_text_block: passing",
        "verification_errors=0",
    ]
    missing = [marker for marker in required if marker not in text]
    assert not missing, f"critique journal missing markers: {missing}"


def assert_jeff_critique_coverage_valid(rows: list[ThemeRow]) -> None:
    assert JEFF_CRITIQUE_PATH.exists(), f"missing Jeff Dean critique file: {JEFF_CRITIQUE_PATH}"
    text = JEFF_CRITIQUE_PATH.read_text()
    headers = re.findall(r"^## ([^\n]+\.md)$", text, flags=re.M)
    blocks = re.findall(r"```text\n(.*?)\n```", text, flags=re.S)
    assert len(headers) == 99, f"expected 99 Jeff Dean critique headers, found {len(headers)}"
    assert len(set(headers)) == len(headers), "duplicate Jeff Dean critique headers found"
    assert len(blocks) == 99, f"expected 99 Jeff Dean critique text blocks, found {len(blocks)}"
    for row in rows:
        generated_path = GENERATED_DIR / f"{row.theme}.md"
        relative_path = generated_path.relative_to(ROOT_DIR)
        assert f"## {generated_path.name}" in text, f"missing Jeff Dean critique header for {generated_path.name}"
        assert (
            text.count(f"Exact path: `{relative_path}`") == 1
        ), f"Jeff Dean critique exact path not once: {relative_path}"


def assert_jeff_critique_quality_valid() -> None:
    assert JEFF_CRITIQUE_PATH.exists(), f"missing Jeff Dean critique file: {JEFF_CRITIQUE_PATH}"
    blocks = re.findall(r"```text\n(.*?)\n```", JEFF_CRITIQUE_PATH.read_text(), flags=re.S)
    required_markers = [
        "Jeff Dean-style systems critique",
        "What is missing for scale, reliability, and operational robustness:",
        "Where the reference is too hand-wavy or not technically grounded:",
        "What concrete systems thinking should be added:",
        "Where it would fail under production load or large-codebase use:",
        "What should be simplified, made composable, or made measurable:",
        "Scale model:",
        "Reliability model:",
        "Instrumentation:",
        "Failure modes:",
        "backpressure",
        "observability",
        "p50/p95/p99 latency",
    ]
    failures: list[tuple[int, list[str]]] = []
    for index, block in enumerate(blocks, 1):
        missing = [marker for marker in required_markers if marker not in block]
        if missing:
            failures.append((index, missing))
        if len(block.splitlines()) < 35:
            failures.append((index, ["critique block shorter than 35 lines"]))
    assert not failures, f"Jeff Dean critique quality failures: {failures[:5]}"


def assert_jeff_critique_journal_valid() -> None:
    assert (
        JEFF_CRITIQUE_JOURNAL_PATH.exists()
    ), f"missing Jeff Dean critique journal: {JEFF_CRITIQUE_JOURNAL_PATH}"
    text = JEFF_CRITIQUE_JOURNAL_PATH.read_text()
    required = [
        "Current Phase: Green",
        "test_jd_critique_file_exists: passing",
        "test_all_99_reference_paths_present: passing",
        "test_each_section_has_header_and_text_block: passing",
        "test_jd_systems_markers_present: passing",
        "verification_errors=0",
    ]
    missing = [marker for marker in required if marker not in text]
    assert not missing, f"Jeff Dean critique journal missing markers: {missing}"


def run_verification(stage: str) -> int:
    checks = [
        ("TEST-SPEC-001", lambda rows: assert_inventory_valid(rows)),
        ("TEST-SPEC-002", lambda rows: assert_generated_files_valid(rows)),
        ("TEST-SPEC-003", lambda rows: [assert_theme_file_valid(row) for row in rows]),
        ("TEST-SPEC-004", lambda rows: [assert_theme_file_valid(row) for row in rows]),
        ("TEST-SPEC-005", lambda rows: [assert_theme_file_valid(row) for row in rows]),
        ("TEST-SPEC-006", lambda rows: [assert_theme_file_valid(row) for row in rows]),
        ("TEST-SPEC-007", lambda rows: [assert_theme_file_valid(row) for row in rows]),
        ("TEST-SPEC-008", lambda rows: assert_progress_journal_valid()),
        ("TEST-SPEC-009", lambda rows: assert_coverage_manifest_valid(rows)),
        ("TEST-SPEC-010", lambda rows: [assert_theme_file_valid(row) for row in rows]),
        ("TEST-SPEC-011", lambda rows: assert_critique_coverage_valid(rows)),
        ("TEST-SPEC-012", lambda rows: assert_critique_quality_valid()),
        ("TEST-SPEC-013", lambda rows: [assert_theme_file_valid(row) for row in rows]),
        ("TEST-SPEC-014", lambda rows: [assert_theme_file_valid(row) for row in rows]),
        ("TEST-SPEC-015", lambda rows: [assert_theme_file_valid(row) for row in rows]),
        ("TEST-SPEC-016", lambda rows: assert_critique_journal_valid()),
        ("TEST-SPEC-017", lambda rows: assert_jeff_critique_coverage_valid(rows)),
        ("TEST-SPEC-018", lambda rows: assert_jeff_critique_quality_valid()),
        ("TEST-SPEC-019", lambda rows: [assert_theme_file_valid(row) for row in rows]),
        ("TEST-SPEC-020", lambda rows: assert_jeff_critique_journal_valid()),
    ]
    rows = parse_theme_rows()
    failures: list[tuple[str, str]] = []
    for test_id, check in checks:
        try:
            check(rows)
            print(f"{test_id}: PASS")
        except AssertionError as exc:
            print(f"{test_id}: FAIL - {exc}")
            failures.append((test_id, str(exc)))
            if stage == "red":
                continue
    if failures:
        print(f"VERIFY FAIL failures={len(failures)}")
        return 1
    print("VERIFY PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=["red", "final"], default="final")
    args = parser.parse_args()
    return run_verification(args.stage)


if __name__ == "__main__":
    sys.exit(main())
