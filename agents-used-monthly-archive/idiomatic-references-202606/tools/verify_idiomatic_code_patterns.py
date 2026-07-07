#!/usr/bin/env python3
"""Verify the Desktop idiomatic-code-patterns extraction workstream."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


WORK_DIR = Path("agents-used-monthly-archive/idiomatic-references-202606")
INVENTORY_PATH = WORK_DIR / "idiomatic-code-patterns-repo-inventory.json"
SUMMARY_PATH = WORK_DIR / "idiomatic-code-patterns-scan-summary.json"
PROGRESS_PATH = WORK_DIR / "idiomatic-code-patterns-progress.md"


def load_inventory() -> list[dict[str, object]]:
    assert INVENTORY_PATH.exists(), f"missing inventory: {INVENTORY_PATH}"
    data = json.loads(INVENTORY_PATH.read_text())
    assert isinstance(data, list), "inventory must be a list"
    return data


def assert_inventory_valid(records: list[dict[str, object]]) -> None:
    assert len(records) > 0, "inventory is empty"
    paths = [str(record["repo_path"]) for record in records]
    assert len(paths) == len(set(paths)), "duplicate repo path in inventory"
    for path in paths:
        assert Path(path).exists(), f"repo path missing on disk: {path}"
        assert (Path(path) / ".git").exists(), f"repo path lacks .git: {path}"
    parts = {int(record["assigned_part"]) for record in records}
    assert parts == {1, 2, 3, 4, 5}, f"bad assigned parts: {sorted(parts)}"


def assert_slice_files_valid(records: list[dict[str, object]]) -> None:
    expected_paths = {str(record["repo_path"]) for record in records}
    seen: list[str] = []
    for part in range(1, 6):
        slice_path = WORK_DIR / f"idiomatic-code-patterns-{part}-repos.txt"
        assert slice_path.exists(), f"missing slice file: {slice_path}"
        paths = [line.strip() for line in slice_path.read_text().splitlines() if line.strip()]
        assert paths, f"empty slice file: {slice_path}"
        seen.extend(paths)
    assert set(seen) == expected_paths, "slice files do not match inventory"
    assert len(seen) == len(set(seen)), "duplicate repo path across slice files"


def assert_target_files_valid(records: list[dict[str, object]], stage: str) -> None:
    for part in range(1, 6):
        target = WORK_DIR / f"idiomatic-code-patterns-{part}.md"
        assert target.exists(), f"missing target file: {target}"
        text = target.read_text()
        assert text.startswith(f"# Idiomatic Code Patterns Part {part}\n"), f"bad title: {target}"
        assert "## Extraction Protocol" in text, f"missing extraction protocol: {target}"
        assert "## Patterns" in text, f"missing patterns section: {target}"
        assert text.count("```") % 2 == 0, f"unbalanced markdown code fences: {target}"
        conflict_markers = ["<<<<<<< ", "=======", ">>>>>>> "]
        present_markers = [marker for marker in conflict_markers if marker in text]
        assert not present_markers, f"merge conflict markers in {target}: {present_markers}"
        if stage in {"progress", "final"}:
            pattern_count = len(re.findall(r"^### ", text, flags=re.M))
            assert pattern_count > 0, f"no extracted patterns yet: {target}"
        if stage == "final":
            assert "Coverage status: initial scaffold created" not in text, f"still scaffolded: {target}"


def assert_progress_valid() -> None:
    assert PROGRESS_PATH.exists(), f"missing progress journal: {PROGRESS_PATH}"
    text = PROGRESS_PATH.read_text()
    required = [
        "### Current Phase:",
        "### Tests Written:",
        "### Implementation Progress:",
        "### Current Focus:",
        "### Next Steps:",
        "### Context Notes:",
        "### Performance/Metrics:",
    ]
    missing = [marker for marker in required if marker not in text]
    assert not missing, f"progress journal missing markers: {missing}"
    assert "### Next Steps:\n\n" not in text, "progress journal has empty next steps"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=["red", "progress", "final"], default="progress")
    args = parser.parse_args()

    checks = [
        ("TEST-IDIOMATIC-001", lambda records: assert_inventory_valid(records)),
        ("TEST-IDIOMATIC-002", lambda records: assert_slice_files_valid(records)),
        ("TEST-IDIOMATIC-003", lambda records: assert_target_files_valid(records, args.stage)),
        ("TEST-IDIOMATIC-004", lambda records: assert_progress_valid()),
    ]
    records = load_inventory()
    failures: list[tuple[str, str]] = []
    for test_id, check in checks:
        try:
            check(records)
            print(f"{test_id}: PASS")
        except AssertionError as exc:
            print(f"{test_id}: FAIL - {exc}")
            failures.append((test_id, str(exc)))
            if args.stage != "red":
                break
    if failures:
        print(f"VERIFY FAIL failures={len(failures)} stage={args.stage}")
        return 1
    print(f"VERIFY PASS stage={args.stage}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
