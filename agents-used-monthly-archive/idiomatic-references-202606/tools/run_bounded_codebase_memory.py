#!/usr/bin/env python3
"""Run a repo-scoped codebase-memory smoke scan with a Python timeout."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


SCAN_SCRIPT = Path(
    "/Users/amuldotexe/.codex/skills/codebase-memory-evidence-reader/scripts/"
    "scan_current_repo_only.sh"
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_path")
    parser.add_argument("--seconds", type=int, default=120)
    args = parser.parse_args()

    repo = Path(args.repo_path).expanduser().resolve()
    result: dict[str, object] = {
        "repo_path": str(repo),
        "started_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "timeout_seconds": args.seconds,
        "scan_script": str(SCAN_SCRIPT),
    }

    if not repo.exists():
        result.update({"status": "missing_repo"})
        print(json.dumps(result, indent=2))
        return 2
    if not (repo / ".git").exists():
        result.update({"status": "missing_git_dir"})
        print(json.dumps(result, indent=2))
        return 2
    if not SCAN_SCRIPT.exists():
        result.update({"status": "missing_scan_script"})
        print(json.dumps(result, indent=2))
        return 2

    try:
        completed = subprocess.run(
            [str(SCAN_SCRIPT), str(repo)],
            check=False,
            capture_output=True,
            text=True,
            timeout=args.seconds,
        )
    except subprocess.TimeoutExpired as exc:
        result.update(
            {
                "status": "timeout",
                "stdout_tail": (exc.stdout or "")[-4000:],
                "stderr_tail": (exc.stderr or "")[-4000:],
            }
        )
        print(json.dumps(result, indent=2))
        return 124

    stdout = completed.stdout or ""
    stderr = completed.stderr or ""
    out_dir = None
    for line in stdout.splitlines() + stderr.splitlines():
        if "/tmp/codex-code-intel/codebase-memory/" in line:
            out_dir = line.strip().split()[-1]

    result.update(
        {
            "status": "pass" if completed.returncode == 0 else "fail",
            "returncode": completed.returncode,
            "out_dir": out_dir,
            "stdout_tail": stdout[-4000:],
            "stderr_tail": stderr[-4000:],
        }
    )
    print(json.dumps(result, indent=2))
    return completed.returncode


if __name__ == "__main__":
    sys.exit(main())
