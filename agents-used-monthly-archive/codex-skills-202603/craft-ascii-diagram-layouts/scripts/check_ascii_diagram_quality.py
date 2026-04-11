#!/usr/bin/env python3
"""Validate basic quality rules for file-backed ASCII diagrams."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to a diagram file, or '-' to read from stdin")
    parser.add_argument("--max-width", type=int, default=100, help="Maximum allowed line width")
    parser.add_argument(
        "--allow-unicode",
        action="store_true",
        help="Allow non-ASCII characters instead of failing on them",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of plain text",
    )
    return parser.parse_args()


def read_text(path_arg: str) -> tuple[str, str]:
    if path_arg == "-":
        return sys.stdin.read(), "<stdin>"
    path = Path(path_arg).expanduser().resolve()
    return path.read_text(encoding="utf-8"), str(path)


def main() -> int:
    args = parse_args()
    text, source = read_text(args.input)
    issues: list[dict[str, object]] = []

    lines = text.splitlines()

    if not lines:
        issues.append({"line": 0, "kind": "empty", "message": "diagram is empty"})

    connector_chars = set("+-|/\\<>^v")
    has_connector = any(any(ch in connector_chars for ch in line) for line in lines)
    if lines and not has_connector:
        issues.append(
            {
                "line": 0,
                "kind": "structure",
                "message": "diagram does not appear to contain box or connector characters",
            }
        )

    for index, line in enumerate(lines, start=1):
        if "\t" in line:
            issues.append({"line": index, "kind": "tab", "message": "tab character found"})

        if line.rstrip(" ") != line:
            issues.append(
                {"line": index, "kind": "trailing_whitespace", "message": "trailing whitespace found"}
            )

        if len(line) > args.max_width:
            issues.append(
                {
                    "line": index,
                    "kind": "width",
                    "message": f"line width {len(line)} exceeds max width {args.max_width}",
                }
            )

        if not args.allow_unicode:
            for column, ch in enumerate(line, start=1):
                if ord(ch) > 127:
                    issues.append(
                        {
                            "line": index,
                            "column": column,
                            "kind": "non_ascii",
                            "message": f"non-ASCII character {ch!r} found",
                        }
                    )

    result = {
        "source": source,
        "ok": not issues,
        "issue_count": len(issues),
        "issues": issues,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        status = "PASS" if result["ok"] else "FAIL"
        print(f"{status}: {source}")
        for issue in issues:
            line = issue.get("line", 0)
            column = issue.get("column")
            location = f"line {line}"
            if column is not None:
                location += f", column {column}"
            print(f"- {location}: {issue['kind']} - {issue['message']}")

    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
