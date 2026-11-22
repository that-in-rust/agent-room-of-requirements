#!/usr/bin/env python3
"""Render a Markdown digest from GHCLI-captured repo context files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def flatten_pages(payload: Any) -> list[Any]:
    if not isinstance(payload, list):
        return payload if isinstance(payload, list) else [payload]

    flattened: list[Any] = []
    for page in payload:
        if isinstance(page, list):
            flattened.extend(page)
        else:
            flattened.append(page)
    return flattened


def safe_login(node: Any) -> str:
    if isinstance(node, dict):
        return str(node.get("login") or "unknown")
    return "unknown"


def bullet(text: str) -> str:
    return f"- {text}"


def repo_summary(root: Path, manifest: dict[str, Any]) -> str:
    raw = root / "raw"
    repo = load_json(raw / "repo.json")
    commits = flatten_pages(load_json(raw / "commits.json")) if (raw / "commits.json").exists() else []
    pulls = flatten_pages(load_json(raw / "pulls.json")) if (raw / "pulls.json").exists() else []
    mixed_issues = flatten_pages(load_json(raw / "issues_and_pull_requests.json")) if (raw / "issues_and_pull_requests.json").exists() else []
    issue_comments = flatten_pages(load_json(raw / "issue_comments.json")) if (raw / "issue_comments.json").exists() else []
    review_comments = flatten_pages(load_json(raw / "review_comments.json")) if (raw / "review_comments.json").exists() else []
    commit_comments = flatten_pages(load_json(raw / "commit_comments.json")) if (raw / "commit_comments.json").exists() else []

    discussions: list[dict[str, Any]] = []
    if (raw / "discussions_index.json").exists():
        for page in flatten_pages(load_json(raw / "discussions_index.json")):
            nodes = (
                page.get("data", {})
                .get("repository", {})
                .get("discussions", {})
                .get("nodes", [])
            )
            discussions.extend(nodes)

    issues_only = [item for item in mixed_issues if "pull_request" not in item]

    lines = [
        "# GitHub Repo Context Digest",
        "",
        "## Scope",
        bullet(f"Repository: `{manifest['repo']}`"),
        bullet("Capture type: repo survey"),
        bullet(f"Collected at: `{manifest['collected_at']}`"),
        bullet(f"Default branch: `{manifest['default_branch']}`"),
    ]

    if manifest.get("since"):
        lines.append(bullet(f"Since filter: `{manifest['since']}`"))
    if manifest.get("max_pages") is not None:
        lines.append(bullet(f"Page cap per paginated surface: `{manifest['max_pages']}`"))

    lines.extend(
        [
            "",
            "## Surfaces Queried",
            bullet(f"Commits: {len(commits)}"),
            bullet(f"Pull requests: {len(pulls)}"),
            bullet(f"Issues: {len(issues_only)}"),
            bullet(f"Issue comments: {len(issue_comments)}"),
            bullet(f"Review comments: {len(review_comments)}"),
            bullet(f"Commit comments: {len(commit_comments)}"),
            bullet(f"Discussions: {len(discussions)}"),
            "",
            "## Chronology",
        ]
    )

    for commit in commits[:10]:
        sha = str(commit.get("sha", ""))[:8]
        author = safe_login(commit.get("author"))
        date = commit.get("commit", {}).get("author", {}).get("date", "unknown-date")
        title = str(commit.get("commit", {}).get("message", "")).splitlines()[0]
        lines.append(bullet(f"`{sha}` {date} by `{author}`: {title}"))

    lines.extend(["", "## Key Conversations"])

    for pr in pulls[:8]:
        lines.append(
            bullet(
                f"PR #{pr.get('number')} [{pr.get('state')}] {pr.get('title')} "
                f"({pr.get('html_url') or pr.get('url')})"
            )
        )

    for discussion in discussions[:6]:
        lines.append(
            bullet(
                f"Discussion #{discussion.get('number')} in `{discussion.get('category', {}).get('name', 'unknown')}`: "
                f"{discussion.get('title')} ({discussion.get('comments', {}).get('totalCount', 0)} comments)"
            )
        )

    lines.extend(
        [
            "",
            "## Linked Artifacts",
            bullet("Repo-wide snapshot preserves separate files for commits, PRs, issues, issue comments, review comments, commit comments, and discussions."),
            bullet("Use the focused artifact collector when you need timeline events or a commit-to-PR story for one item."),
            "",
            "## Gaps And Limits",
            bullet("Repo-wide issues capture includes pull-request issue records because GitHub exposes issues and PR threads on a shared issues surface."),
            bullet("Repo-wide snapshot does not capture per-item timeline events by default."),
            bullet("Discussion index is lightweight; run a focused discussion trace for full thread details."),
            "",
            "## Raw Output Paths",
            bullet(f"Manifest: `{root / 'manifest.json'}`"),
            bullet(f"Raw directory: `{raw}`"),
            bullet(f"Repository URL: {repo.get('url', 'unknown')}"),
        ]
    )

    return "\n".join(lines) + "\n"


def artifact_summary(root: Path, manifest: dict[str, Any]) -> str:
    raw = root / "raw"
    kind = manifest["kind"]
    artifact_id = manifest["id"]

    lines = [
        "# GitHub Repo Context Digest",
        "",
        "## Scope",
        bullet(f"Repository: `{manifest['repo']}`"),
        bullet("Capture type: focused artifact trace"),
        bullet(f"Kind: `{kind}`"),
        bullet(f"Identifier: `{artifact_id}`"),
        bullet(f"Collected at: `{manifest['collected_at']}`"),
        "",
        "## Surfaces Queried",
    ]

    if kind == "pr":
        pr = load_json(raw / "pr.json")
        timeline = flatten_pages(load_json(raw / "timeline.json"))
        review_comments = flatten_pages(load_json(raw / "review_comments.json"))
        reviews = flatten_pages(load_json(raw / "reviews.json"))
        lines.extend(
            [
                bullet("PR metadata via `gh pr view`"),
                bullet(f"Timeline events: {len(timeline)}"),
                bullet(f"Review comments: {len(review_comments)}"),
                bullet(f"Reviews: {len(reviews)}"),
                "",
                "## Chronology",
                bullet(f"PR #{pr.get('number')} [{pr.get('state')}] {pr.get('title')}"),
                bullet(f"Created: {pr.get('createdAt')}"),
                bullet(f"Updated: {pr.get('updatedAt')}"),
                bullet(f"Merged: {pr.get('mergedAt') or 'not merged'}"),
                "",
                "## Key Conversations",
                bullet(f"Issue-thread comments captured in PR view: {len(pr.get('comments', []))}"),
                bullet(f"Code review comments captured separately: {len(review_comments)}"),
                bullet(f"Review summaries captured separately: {len(reviews)}"),
                "",
                "## Linked Artifacts",
                bullet(f"URL: {pr.get('url')}"),
                bullet(f"Commits listed in PR view: {len(pr.get('commits', []))}"),
                bullet(f"Files listed in PR view: {len(pr.get('files', []))}"),
            ]
        )
    elif kind == "issue":
        issue = load_json(raw / "issue.json")
        timeline = flatten_pages(load_json(raw / "timeline.json"))
        lines.extend(
            [
                bullet("Issue metadata via `gh issue view`"),
                bullet(f"Timeline events: {len(timeline)}"),
                "",
                "## Chronology",
                bullet(f"Issue #{issue.get('number')} [{issue.get('state')}] {issue.get('title')}"),
                bullet(f"Created: {issue.get('createdAt')}"),
                bullet(f"Updated: {issue.get('updatedAt')}"),
                bullet(f"Closed: {issue.get('closedAt') or 'open'}"),
                "",
                "## Key Conversations",
                bullet(f"Comments captured in issue view: {len(issue.get('comments', []))}"),
                bullet(f"Timeline events captured separately: {len(timeline)}"),
                "",
                "## Linked Artifacts",
                bullet(f"URL: {issue.get('url')}"),
            ]
        )
    elif kind == "commit":
        commit = load_json(raw / "commit.json")
        commit_comments = flatten_pages(load_json(raw / "commit_comments.json"))
        associated_pulls = flatten_pages(load_json(raw / "associated_pulls.json"))
        lines.extend(
            [
                bullet("Commit detail via REST commit endpoint"),
                bullet(f"Commit comments: {len(commit_comments)}"),
                bullet(f"Associated pull requests: {len(associated_pulls)}"),
                "",
                "## Chronology",
                bullet(f"Commit SHA: `{commit.get('sha', '')[:12]}`"),
                bullet(f"Authored: {commit.get('commit', {}).get('author', {}).get('date')}"),
                bullet(f"Committed: {commit.get('commit', {}).get('committer', {}).get('date')}"),
                "",
                "## Key Conversations",
                bullet(str(commit.get("commit", {}).get("message", "")).splitlines()[0]),
                bullet(f"Commit comments captured separately: {len(commit_comments)}"),
                "",
                "## Linked Artifacts",
            ]
        )
        for pr in associated_pulls[:8]:
            lines.append(bullet(f"Associated PR #{pr.get('number')}: {pr.get('title')}"))
    elif kind == "discussion":
        pages = flatten_pages(load_json(raw / "discussion_thread.json"))
        discussion = (
            pages[0].get("data", {}).get("repository", {}).get("discussion", {})
            if pages
            else {}
        )
        comment_count = 0
        reply_count = 0
        for page in pages:
            nodes = (
                page.get("data", {})
                .get("repository", {})
                .get("discussion", {})
                .get("comments", {})
                .get("nodes", [])
            )
            comment_count += len(nodes)
            for node in nodes:
                reply_count += len(node.get("replies", {}).get("nodes", []))

        lines.extend(
            [
                bullet("Discussion detail via GraphQL"),
                bullet(f"Discussion comment pages: {len(pages)}"),
                bullet(f"Discussion comments captured: {comment_count}"),
                bullet(f"Nested replies captured: {reply_count}"),
                "",
                "## Chronology",
                bullet(f"Discussion #{discussion.get('number')} {discussion.get('title')}"),
                bullet(f"Created: {discussion.get('createdAt')}"),
                bullet(f"Updated: {discussion.get('updatedAt')}"),
                bullet(f"Answered at: {discussion.get('answerChosenAt') or 'not marked answered'}"),
                "",
                "## Key Conversations",
                bullet(f"Category: {discussion.get('category', {}).get('name', 'unknown')}"),
                bullet(f"Top-level comments captured: {comment_count}"),
                bullet(f"Nested replies captured: {reply_count}"),
                "",
                "## Linked Artifacts",
                bullet(f"URL: {discussion.get('url')}"),
            ]
        )
    else:
        raise ValueError(f"unsupported kind: {kind}")

    lines.extend(
        [
            "",
            "## Gaps And Limits",
            bullet("This digest reports only the surfaces present in the capture directory."),
            bullet("Use raw files for a second-pass synthesis if more detail is needed."),
            "",
            "## Raw Output Paths",
            bullet(f"Manifest: `{root / 'manifest.json'}`"),
            bullet(f"Raw directory: `{raw}`"),
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", required=True, help="Directory containing manifest.json and raw/")
    parser.add_argument("--output", required=True, help="Markdown file to write")
    args = parser.parse_args()

    input_dir = Path(args.input_dir).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    manifest = load_json(input_dir / "manifest.json")

    capture_type = manifest.get("capture_type")
    if capture_type == "repo":
      markdown = repo_summary(input_dir, manifest)
    elif capture_type == "artifact":
      markdown = artifact_summary(input_dir, manifest)
    else:
      raise ValueError(f"unsupported capture_type: {capture_type}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
