---
name: capture-github-repo-context
description: Capture GitHub repository evolution and conversation context with GHCLI, gh api, and GraphQL. Use when Codex needs to reconstruct how a repository changed, trace a commit to the pull request and comments around it, collect issue or PR discussion history, harvest GitHub Discussions, or produce a source-linked Markdown digest for onboarding, incident review, code archaeology, or design-history analysis.
---

# Capture GitHub Repo Context

## Goal

Use GitHub CLI as the primary read-only interface for harvesting repository history and conversation context, then return a source-linked Markdown digest instead of a raw terminal dump.

## Choose The Right Mode

1. Use `Repo Survey` when the user wants a broad picture of how a repository evolved.
2. Use `Artifact Trace` when the user wants the story behind one commit, PR, issue, or discussion.
3. Use `Digest Mode` when the user wants a reusable Markdown summary after collection.

## Workflow

1. Run preflight checks.
- Confirm `gh` is available.
- Confirm authentication with `gh auth status --active`.
- If auth is broken, stop early and ask the user to re-run `gh auth login` or provide `GH_TOKEN` or `GITHUB_TOKEN`.
- Confirm the target repository and host.
- Check repository capabilities with `gh repo view --json hasDiscussionsEnabled,...`.

2. Decide scope before collecting.
- Repo-wide snapshot
- Since-date snapshot
- Single PR
- Single issue
- Single commit
- Single discussion

For large repositories, start with a bounded repo survey and widen only if the user explicitly wants deeper capture.

3. Pick the right GHCLI surface.
- Use high-level `gh` commands for orientation and small focused views.
- Use `gh api` REST endpoints for exhaustive list capture and pagination.
- Use `gh api graphql` for GitHub Discussions and nested discussion replies.

4. Keep conversation surfaces separate.
- Issue comments are not the same as PR review comments.
- Commit comments are not the same as issue or PR thread comments.
- Timeline events are metadata about state changes, not free-form discussion.
- GitHub Discussions are their own conversation system and require their own query path.

5. Produce a digest with provenance.
- Name the repo and scope.
- List which surfaces were queried.
- Summarize chronology, major threads, and unresolved gaps.
- Link back to the original GitHub URLs when available.
- State permission or coverage limits explicitly.

## Command Selection Guide

Use this bias by default:

| Need | Preferred path |
| --- | --- |
| Quick repo capability check | `gh repo view --json ...` |
| Quick PR or issue inspection | `gh pr view --json ...`, `gh issue view --json ...` |
| Paginated repo-wide list capture | `gh api --paginate --slurp` |
| Commit-to-PR linkage | `gh api repos/{owner}/{repo}/commits/<sha>/pulls` |
| Issue or PR timeline events | `gh api repos/{owner}/{repo}/issues/<n>/timeline` |
| GitHub Discussions | `gh api graphql` |
| Human-readable report | `scripts/render_repo_context_digest.py` |

## Use The Bundled Scripts

- Use [collect_repo_context.sh](scripts/collect_repo_context.sh) for repo-wide snapshots.
- The repo-wide collector defaults to a bounded page cap so surveys stay practical on large repositories; raise `--max-pages` or set it to `0` only when the user wants a broader crawl.
- Use [collect_artifact_context.sh](scripts/collect_artifact_context.sh) for a focused commit, PR, issue, or discussion trace.
- Use [render_repo_context_digest.py](scripts/render_repo_context_digest.py) to turn captured JSON into a Markdown digest.

## Guardrails

- Stay read-only unless the user explicitly asks to write, comment, or mutate GitHub state.
- Do not rely on `gh search commits` as the primary archival path for “all commits”; prefer canonical commit-list endpoints for exhaustive history capture.
- Do not flatten all comments into one bucket.
- Do not assume Discussions are available; check `hasDiscussionsEnabled`.
- Do not promise a perfect “entire repo conversation history” if permissions, rate limits, or pagination boundaries prevent it.
- Do not default to repo-wide timeline harvesting; use focused traces for issue and PR timelines.
- Do not default to unlimited repo-wide pagination on very large repositories; start bounded and expand intentionally.
- Do not scrape the website when GHCLI and official APIs already cover the task.

## Output Contract

Return results in this order when the collection is substantial:

1. `Scope`
2. `Surfaces Queried`
3. `Chronology`
4. `Key Conversations`
5. `Linked Artifacts`
6. `Gaps And Limits`
7. `Raw Output Paths`

## Context Strategy

Load progressively:

1. Load this `SKILL.md`.
2. Load [GitHub repo context thesis](references/github-repo-context-thesis.md) for scope, priorities, and exclusions.
3. Load [GHCLI surface map](references/ghcli-surface-map.md) for endpoint and command selection.
4. Load [Discussions GraphQL patterns](references/discussions-graphql-patterns.md) when Discussions are in scope.
5. Load [Output contract](references/output-contract.md) before writing the final digest.

## References

- [GitHub repo context thesis](references/github-repo-context-thesis.md)
- [GHCLI surface map](references/ghcli-surface-map.md)
- [Discussions GraphQL patterns](references/discussions-graphql-patterns.md)
- [Output contract](references/output-contract.md)
