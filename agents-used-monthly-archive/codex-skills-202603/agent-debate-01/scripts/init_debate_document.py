#!/usr/bin/env python3
"""Create a shared markdown debate file for structured multi-agent review."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Initialize a debate markdown file.")
    parser.add_argument("--path", required=True, help="Output markdown path.")
    parser.add_argument("--topic", required=True, help="Debate topic or question.")
    parser.add_argument(
        "--agent",
        action="append",
        required=True,
        help="Agent display name. Repeat 2 or 3 times.",
    )
    parser.add_argument("--max-rounds", type=int, default=3, help="Maximum debate rounds.")
    parser.add_argument("--context", default="", help="Problem statement or debate context.")
    parser.add_argument(
        "--evidence",
        action="append",
        default=[],
        help="Evidence bullet. Repeat as needed.",
    )
    parser.add_argument(
        "--relevant-file",
        action="append",
        default=[],
        help="Relevant file or file:line reference. Repeat as needed.",
    )
    parser.add_argument(
        "--constraint",
        action="append",
        default=[],
        help="Constraint or non-negotiable. Repeat as needed.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing file.")
    return parser


def render_bullets(items: list[str], empty_text: str) -> str:
    cleaned = [item.strip() for item in items if item.strip()]
    if not cleaned:
        return empty_text
    return "\n".join(f"- {item}" for item in cleaned)


def render_document(args: argparse.Namespace) -> str:
    agents = args.agent
    if len(agents) < 2 or len(agents) > 3:
        raise ValueError("Provide 2 or 3 --agent values.")
    if args.max_rounds < 1:
        raise ValueError("--max-rounds must be at least 1.")

    padded_agents = agents + ["-"] * (3 - len(agents))

    evidence_block = render_bullets(
        args.evidence,
        "{Add concrete data, log paths, event counts, actual vs expected values, or runtime output here.}",
    )
    files_block = render_bullets(
        args.relevant_file,
        "{Add relevant file paths and key sections, ideally with file:line pointers.}",
    )
    constraints_block = render_bullets(
        args.constraint,
        "{Add constraints or non-negotiables here.}",
    )

    context_text = args.context.strip() or "{Describe the problem and what is being decided.}"

    return f"""# Debate: {args.topic}

**Created:** {date.today().isoformat()}
**Agent 1:** {padded_agents[0]}
**Agent 2:** {padded_agents[1]}
**Agent 3:** {padded_agents[2]}
**Max Rounds:** {args.max_rounds}
**Status:** OPEN

## Context

{context_text}

### Evidence

{evidence_block}

### Relevant Files

{files_block}

### Constraints

{constraints_block}

---

## Proposal

STATUS: OPEN

{{Agent 1 writes the initial proposal here in Round 1.
Other agents edit in-place in later rounds.
Every fix must cite exact file:line, what the code does now, and what it should do instead.}}

---

## Parking Lot

{{Out-of-scope or related issues go here. Format: - [A1-R2] issue description}}

---

## Dispute Log

| Round | Agent | Section | What Changed | Why | Status |
|-------|-------|---------|--------------|-----|--------|
| | | | | | |

**Status values:** `OPEN` = unresolved, `CLOSED` = resolved, `PARKED` = deferred and not blocking convergence.
"""


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    path = Path(args.path)
    if path.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {path}")

    content = render_document(args)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Created debate file: {path}")


if __name__ == "__main__":
    main()
