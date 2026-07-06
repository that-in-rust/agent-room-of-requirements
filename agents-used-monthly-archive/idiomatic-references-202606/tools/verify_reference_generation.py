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
