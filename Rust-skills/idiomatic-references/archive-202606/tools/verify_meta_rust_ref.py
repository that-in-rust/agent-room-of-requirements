#!/usr/bin/env python3
"""Verify the five-part Desktop meta Rust reference workstream."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


WORK_DIR = Path("agents-used-monthly-archive/idiomatic-references-202606")
INVENTORY_PATH = WORK_DIR / "meta-rust-ref-202606-repo-inventory.json"
PROGRESS_PATH = WORK_DIR / "meta-rust-ref-202606-progress.md"
REQUIRED_LENS_TERMS = [
    "Module",
    "Interface",
    "Implementation",
    "Depth",
    "Seam",
    "Adapter",
    "Leverage",
    "Locality",
]


def load_inventory() -> list[dict[str, object]]:
    assert INVENTORY_PATH.exists(), f"missing inventory: {INVENTORY_PATH}"
    records = json.loads(INVENTORY_PATH.read_text())
    assert isinstance(records, list), "inventory must be a list"
    assert len(records) == 911, f"expected 911 repos, found {len(records)}"
    return records


def assert_inventory_valid(records: list[dict[str, object]]) -> None:
    paths = [str(record["repo_path"]) for record in records]
    assert len(paths) == len(set(paths)), "duplicate repo path in inventory"
    for path in paths:
        repo_path = Path(path)
        assert repo_path.exists(), f"repo path missing on disk: {path}"
        assert (repo_path / ".git").exists(), f"repo path lacks .git: {path}"
    parts = {int(record["assigned_part"]) for record in records}
    assert parts == {1, 2, 3, 4, 5}, f"bad assigned parts: {sorted(parts)}"


def assert_slice_files_valid(records: list[dict[str, object]]) -> None:
    expected_paths = {str(record["repo_path"]) for record in records}
    seen: list[str] = []
    for part in range(1, 6):
        slice_path = WORK_DIR / f"meta-rust-ref-202606-Part{part}-repos.txt"
        assert slice_path.exists(), f"missing slice file: {slice_path}"
        paths = [line.strip() for line in slice_path.read_text().splitlines() if line.strip()]
        assert paths, f"empty slice file: {slice_path}"
        seen.extend(paths)
    assert set(seen) == expected_paths, "slice files do not match inventory"
    assert len(seen) == len(set(seen)), "duplicate repo path across slice files"


def assert_target_files_valid(records: list[dict[str, object]], stage: str) -> None:
    by_part: dict[int, list[str]] = {part: [] for part in range(1, 6)}
    for record in records:
        by_part[int(record["assigned_part"])].append(str(record["repo_path"]))

    for part in range(1, 6):
        target = WORK_DIR / f"meta-rust-ref-202606-Part{part}.md"
        assert target.exists(), f"missing target file: {target}"
        text = target.read_text()
        assert text.startswith(f"# Meta Rust Reference 202606 Part {part}\n"), (
            f"bad title: {target}"
        )
        assert "## Architecture Lens" in text, f"missing architecture lens: {target}"
        assert "## Extraction Protocol" in text, f"missing extraction protocol: {target}"
        assert "## Pattern Entries" in text, f"missing pattern entries section: {target}"
        missing_terms = [term for term in REQUIRED_LENS_TERMS if term not in text]
        assert not missing_terms, f"{target}: missing lens terms {missing_terms}"

        if stage in {"progress", "final"}:
            entries_text = text.split("## Pattern Entries", 1)[1]
            coverage_count = len(re.findall(r"^## Repo Coverage:", entries_text, flags=re.M))
            skipped_count = len(re.findall(r"^## Skipped Repo:", entries_text, flags=re.M))
            concept_count = len(re.findall(r"^### Concept:", entries_text, flags=re.M))
            assert concept_count > 0, f"no concept entries yet: {target}"
            assert coverage_count + skipped_count > 0, f"no repo markers yet: {target}"

        if stage == "final":
            entries_text = text.split("## Pattern Entries", 1)[1]
            markers = [
                match.group(2).strip()
                for match in re.finditer(
                    r"^## (Repo Coverage|Skipped Repo): `?([^`\n]+)`?\s*$",
                    entries_text,
                    flags=re.M,
                )
            ]
            duplicate_repos = sorted({repo for repo in markers if markers.count(repo) > 1})
            extra_repos = sorted(repo for repo in set(markers) if repo not in by_part[part])
            missing_repos = [
                repo
                for repo in by_part[part]
                if repo not in markers
            ]
            assert not missing_repos, (
                f"{target}: missing repo entries: {missing_repos[:10]}"
            )
            assert not duplicate_repos, (
                f"{target}: duplicate repo entries: {duplicate_repos[:10]}"
            )
            assert not extra_repos, f"{target}: extra repo entries: {extra_repos[:10]}"
            assert len(markers) == len(by_part[part]), (
                f"{target}: marker count {len(markers)} != assigned repos {len(by_part[part])}"
            )
            assert "Coverage status: scaffold created" not in text, (
                f"{target}: still marked as scaffold"
            )
            assert "Evidence:" in text, f"{target}: missing evidence lines"
            assert "Architecture lens:" in text, f"{target}: missing architecture lens entries"
            assert "Transfer rule:" in text, f"{target}: missing transfer rules"
            assert "Verification hook:" in text, f"{target}: missing verification hooks"


def assert_progress_valid() -> None:
    assert PROGRESS_PATH.exists(), f"missing progress journal: {PROGRESS_PATH}"
    text = PROGRESS_PATH.read_text()
    required = [
        "#### Current Phase:",
        "#### Tests Written:",
        "#### Implementation Progress:",
        "#### Current Focus:",
        "#### Next Steps:",
        "#### Context Notes:",
        "#### Performance/Metrics:",
    ]
    missing = [marker for marker in required if marker not in text]
    assert not missing, f"progress journal missing markers: {missing}"
    assert "#### Next Steps:\n\n" not in text, "progress journal has empty next steps"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=["red", "progress", "final"], default="progress")
    args = parser.parse_args()

    records = load_inventory()
    checks = [
        ("TEST-META-RUST-001", lambda: assert_inventory_valid(records)),
        ("TEST-META-RUST-002", lambda: assert_slice_files_valid(records)),
        ("TEST-META-RUST-003", lambda: assert_target_files_valid(records, args.stage)),
        ("TEST-META-RUST-004", assert_progress_valid),
    ]
    failures: list[tuple[str, str]] = []
    for test_id, check in checks:
        try:
            check()
            print(f"{test_id}: PASS")
        except AssertionError as exc:
            print(f"{test_id}: FAIL - {exc}")
            failures.append((test_id, str(exc)))
            if args.stage != "red":
                break
    if failures:
        print(f"VERIFY_META_RUST_REF FAIL failures={len(failures)} stage={args.stage}")
        return 1
    print(f"VERIFY_META_RUST_REF PASS stage={args.stage}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
