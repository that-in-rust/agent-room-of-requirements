#!/usr/bin/env python3
"""Verify the five-part Rust pattern reference corpus."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK_DIR = ROOT / "agents-used-monthly-archive/idiomatic-references-202606"
INVENTORY = WORK_DIR / "rust-patterns-repo-inventory.json"
CODEGRAPHCONTEXT_EVIDENCE = WORK_DIR / "rust-patterns-codegraphcontext-evidence.json"


def load_inventory() -> dict[str, object]:
    assert INVENTORY.exists(), f"missing inventory: {INVENTORY}"
    data = json.loads(INVENTORY.read_text())
    assert data["repo_count"] == 156, f"unexpected repo_count={data['repo_count']}"
    assert data["shard_count"] == 5, f"unexpected shard_count={data['shard_count']}"
    return data


def verify_shard_file(name: str, repos: list[str]) -> tuple[int, int]:
    path = WORK_DIR / name
    assert path.exists(), f"missing output file: {path}"
    text = path.read_text()
    assert text.startswith("# Rust Patterns 202606 Part "), f"{name}: missing title"
    assert "## Assigned Repository Shard" in text, f"{name}: missing shard section"
    assert "## Pattern Entries" in text, f"{name}: missing entries section"
    for repo in repos:
        assert repo in text, f"{name}: assigned repo absent from file header: {repo}"
    entries_text = text.split("## Pattern Entries", 1)[1]
    concept_count = len(re.findall(r"^### Concept:", entries_text, flags=re.M))
    evidence_count = len(re.findall(r"^Evidence:", entries_text, flags=re.M))
    coverage_markers = len(re.findall(r"^## Repo Coverage:", entries_text, flags=re.M))
    skip_markers = len(re.findall(r"^## Skipped Repo:", entries_text, flags=re.M))
    missing_entry_repos = [
        repo
        for repo in repos
        if f"Repo Coverage: {repo}" not in entries_text
        and f"Repo Coverage: `{repo}`" not in entries_text
        and f"Skipped Repo: {repo}" not in entries_text
        and f"Skipped Repo: `{repo}`" not in entries_text
    ]
    assert not missing_entry_repos, (
        f"{name}: repos absent from entries section: {missing_entry_repos[:5]}"
    )
    assert coverage_markers + skip_markers >= len(repos), (
        f"{name}: repo coverage markers={coverage_markers + skip_markers} repos={len(repos)}"
    )
    assert concept_count >= 1, f"{name}: no concept entries yet"
    assert evidence_count >= concept_count, f"{name}: evidence lines fewer than concepts"
    assert "Transfer rule:" in text, f"{name}: missing transfer rules"
    assert "Verification hook:" in text, f"{name}: missing verification hooks"
    assert "## CodeGraphContext Evidence Appendix" in text, (
        f"{name}: missing CodeGraphContext appendix"
    )
    assert text.endswith("\n"), f"{name}: missing final newline"
    return concept_count, coverage_markers + skip_markers


def verify_codegraphcontext_evidence() -> tuple[int, int]:
    assert CODEGRAPHCONTEXT_EVIDENCE.exists(), (
        f"missing CodeGraphContext evidence: {CODEGRAPHCONTEXT_EVIDENCE}"
    )
    data = json.loads(CODEGRAPHCONTEXT_EVIDENCE.read_text())
    assert "cgc" in data["tool"], f"unexpected CodeGraphContext tool={data['tool']}"
    attempts = data["attempts"]
    assert len(attempts) == 5, f"unexpected CodeGraphContext attempts={len(attempts)}"
    by_shard = {attempt["shard_file"]: attempt for attempt in attempts}
    for index in range(1, 6):
        shard_name = f"rust-patterns-{index}.md"
        assert shard_name in by_shard, f"missing CodeGraphContext attempt for {shard_name}"
        attempt = by_shard[shard_name]
        assert attempt["repo_path"].startswith("/Users/amuldotexe/Desktop/"), (
            f"{shard_name}: CodeGraphContext repo outside Desktop"
        )
        assert attempt["output_dir"].startswith("/tmp/codex-code-intel/codegraphcontext/"), (
            f"{shard_name}: CodeGraphContext output outside expected tmp root"
        )
    usable_statuses = {"complete", "usable_partial_index"}
    usable_count = sum(1 for attempt in attempts if attempt["status"] in usable_statuses)
    assert usable_count >= 3, f"too few usable CodeGraphContext attempts={usable_count}"
    return len(attempts), usable_count


def main() -> int:
    data = load_inventory()
    shards = data["shards"]
    total_concepts = 0
    total_markers = 0
    for name, repos in sorted(shards.items()):
        concepts, markers = verify_shard_file(name, repos)
        total_concepts += concepts
        total_markers += markers
        print(f"{name}: PASS concepts={concepts} repo_markers={markers} repos={len(repos)}")
    assert total_markers >= data["repo_count"], (
        f"total repo markers={total_markers} repo_count={data['repo_count']}"
    )
    cgc_attempts, cgc_usable = verify_codegraphcontext_evidence()
    print(
        f"VERIFY_RUST_PATTERNS PASS concepts={total_concepts} "
        f"repo_markers={total_markers} cgc_attempts={cgc_attempts} "
        f"cgc_usable={cgc_usable}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VERIFY_RUST_PATTERNS FAIL - {exc}")
        raise SystemExit(1)
