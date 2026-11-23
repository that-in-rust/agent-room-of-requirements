#!/usr/bin/env python3
"""Initialize and update TDD progress journals for long-running work."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, List, Tuple


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")


def parse_test_fields(raw_values: Iterable[str]) -> List[Tuple[str, str, str]]:
    parsed: List[Tuple[str, str, str]] = []
    for value in raw_values:
        parts = [p.strip() for p in value.split("|", maxsplit=2)]
        while len(parts) < 3:
            parts.append("")
        name, status, detail = parts
        parsed.append((name or "(unnamed test)", status or "unknown", detail))
    return parsed


def ensure_parent_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def normalize_phase(phase: str) -> str:
    phase_map = {
        "red": "Red",
        "green": "Green",
        "refactor": "Refactor",
    }
    return phase_map[phase.lower()]


def format_bullets(items: Iterable[str], fallback: str) -> str:
    normalized = [item.strip() for item in items if item and item.strip()]
    if not normalized:
        return f"- {fallback}\n"
    return "".join(f"- {item}\n" for item in normalized)


def render_test_bullets(tests: List[Tuple[str, str, str]]) -> str:
    if not tests:
        return "- (none recorded)\n"
    lines = []
    for name, status, detail in tests:
        tail = f" - {detail}" if detail else ""
        lines.append(f"- {name}: {status}{tail}\n")
    return "".join(lines)


def render_session_block(
    phase: str,
    focus: str,
    tests: List[Tuple[str, str, str]],
    implementation: List[str],
    next_steps: List[str],
    notes: List[str],
    metrics: List[str],
) -> str:
    timestamp = utc_now_iso()
    return (
        f"\n### Session: {timestamp}\n\n"
        f"#### Current Phase: {phase}\n\n"
        "#### Tests Written:\n"
        f"{render_test_bullets(tests)}\n"
        "#### Implementation Progress:\n"
        f"{format_bullets(implementation, '(none recorded)')}\n"
        "#### Current Focus:\n"
        f"{focus.strip() if focus.strip() else '(not set)'}\n\n"
        "#### Next Steps:\n"
        f"{format_bullets(next_steps, '(none recorded)')}\n"
        "#### Context Notes:\n"
        f"{format_bullets(notes, '(none recorded)')}\n"
        "#### Performance/Metrics:\n"
        f"{format_bullets(metrics, '(none recorded)')}"
    )


def init_journal(path: Path, task: str, phase: str, status: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"Journal already exists: {path}")
    ensure_parent_dir(path)
    now = utc_now_iso()
    content = (
        "# TDD Progress Journal\n\n"
        f"- Task: {task.strip()}\n"
        f"- Created: {now}\n"
        f"- Updated: {now}\n"
        f"- Current Phase: {phase}\n"
        f"- Status: {status.strip()}\n\n"
        "## Sessions\n"
    )
    path.write_text(content, encoding="utf-8")


def replace_header_field(content: str, field: str, value: str) -> str:
    pattern = rf"^- {re.escape(field)}: .*$"
    replacement = f"- {field}: {value}"
    return re.sub(pattern, replacement, content, flags=re.MULTILINE)


def update_journal(
    path: Path,
    phase: str,
    focus: str,
    tests: List[Tuple[str, str, str]],
    implementation: List[str],
    next_steps: List[str],
    notes: List[str],
    metrics: List[str],
) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Journal not found: {path}")
    content = path.read_text(encoding="utf-8")
    content = replace_header_field(content, "Updated", utc_now_iso())
    content = replace_header_field(content, "Current Phase", phase)
    session_block = render_session_block(
        phase=phase,
        focus=focus,
        tests=tests,
        implementation=implementation,
        next_steps=next_steps,
        notes=notes,
        metrics=metrics,
    )
    if not content.endswith("\n"):
        content += "\n"
    content += session_block
    path.write_text(content, encoding="utf-8")


def extract_snapshot(content: str) -> str:
    session_positions = [m.start() for m in re.finditer(r"^### Session:", content, re.MULTILINE)]
    if not session_positions:
        return "No sessions recorded yet."
    start = session_positions[-1]
    return content[start:].strip()


def read_header_summary(content: str) -> str:
    wanted = ["Task", "Created", "Updated", "Current Phase", "Status"]
    lines = []
    for field in wanted:
        match = re.search(rf"^- {re.escape(field)}: (.*)$", content, flags=re.MULTILINE)
        if match:
            lines.append(f"{field}: {match.group(1)}")
    return "\n".join(lines)


def snapshot_journal(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Journal not found: {path}")
    content = path.read_text(encoding="utf-8")
    header = read_header_summary(content)
    latest = extract_snapshot(content)
    print("## Journal Header")
    print(header if header else "(header not found)")
    print("\n## Latest Session")
    print(latest)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Manage a markdown TDD progress journal.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize a new journal.")
    init_parser.add_argument("--path", required=True, help="Path to journal markdown file.")
    init_parser.add_argument("--task", required=True, help="Short task title.")
    init_parser.add_argument(
        "--phase",
        default="Red",
        choices=["Red", "Green", "Refactor", "red", "green", "refactor"],
        help="Initial TDD phase.",
    )
    init_parser.add_argument("--status", default="active", help="Workstream status.")
    init_parser.add_argument("--force", action="store_true", help="Overwrite existing file.")

    update_parser = subparsers.add_parser("update", help="Append a session checkpoint.")
    update_parser.add_argument("--path", required=True, help="Path to journal markdown file.")
    update_parser.add_argument(
        "--phase",
        required=True,
        choices=["Red", "Green", "Refactor", "red", "green", "refactor"],
        help="Current TDD phase.",
    )
    update_parser.add_argument("--focus", default="", help="Current focus text.")
    update_parser.add_argument(
        "--test",
        action="append",
        default=[],
        help="Test row in format name|status|detail (repeatable).",
    )
    update_parser.add_argument(
        "--implementation",
        action="append",
        default=[],
        help="Implementation progress bullet (repeatable).",
    )
    update_parser.add_argument(
        "--next-step",
        action="append",
        default=[],
        help="Next step bullet (repeatable).",
    )
    update_parser.add_argument(
        "--note",
        action="append",
        default=[],
        help="Context note bullet (repeatable).",
    )
    update_parser.add_argument(
        "--metric",
        action="append",
        default=[],
        help="Performance or metric bullet (repeatable).",
    )

    snapshot_parser = subparsers.add_parser("snapshot", help="Print latest checkpoint.")
    snapshot_parser.add_argument("--path", required=True, help="Path to journal markdown file.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "init":
        path = Path(args.path)
        init_journal(
            path=path,
            task=args.task,
            phase=normalize_phase(args.phase),
            status=args.status,
            force=args.force,
        )
        print(f"Initialized journal: {path}")
        return

    if args.command == "update":
        path = Path(args.path)
        tests = parse_test_fields(args.test)
        update_journal(
            path=path,
            phase=normalize_phase(args.phase),
            focus=args.focus,
            tests=tests,
            implementation=args.implementation,
            next_steps=args.next_step,
            notes=args.note,
            metrics=args.metric,
        )
        print(f"Updated journal: {path}")
        return

    if args.command == "snapshot":
        path = Path(args.path)
        snapshot_journal(path=path)
        return

    parser.error("Unknown command")


if __name__ == "__main__":
    main()
