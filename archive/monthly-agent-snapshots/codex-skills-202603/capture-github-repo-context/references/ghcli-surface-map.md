# GHCLI Surface Map

## Table Of Contents

1. Command choice rules
2. Surface matrix
3. Common traps
4. Suggested command patterns

## Command Choice Rules

- Use `gh repo view`, `gh pr view`, and `gh issue view` for orientation and focused reads.
- Use `gh api --paginate --slurp` for repo-wide collection.
- Use `gh api graphql` for GitHub Discussions.
- Use search commands as discovery helpers, not as a complete historical record.

## Surface Matrix

| Surface | Preferred GHCLI path | Why |
| --- | --- | --- |
| Repo metadata | `gh repo view --json ...` | Quick capability and visibility check |
| Default branch commit history | `gh api repos/{owner}/{repo}/commits?...` | Canonical list capture |
| Commit detail | `gh api repos/{owner}/{repo}/commits/<sha>` | Includes metadata and stats |
| Commit comments | `gh api repos/{owner}/{repo}/commits/<sha>/comments` or repo-wide `repos/{owner}/{repo}/comments` | Separate from issue and review comments |
| Commit to PR linkage | `gh api repos/{owner}/{repo}/commits/<sha>/pulls` | Best explanation bridge from code to review thread |
| PR quick read | `gh pr view <n> --json ...` | Structured focused summary |
| PR repo-wide list | `gh api repos/{owner}/{repo}/pulls?state=all...` | Full pagination |
| PR review comments | `gh api repos/{owner}/{repo}/pulls/<n>/comments` or repo-wide `repos/{owner}/{repo}/pulls/comments` | Code-review layer |
| PR reviews | `gh api repos/{owner}/{repo}/pulls/<n>/reviews` | Review state and summary comments |
| Issue quick read | `gh issue view <n> --json ...` | Structured focused summary |
| Issue / PR timeline | `gh api repos/{owner}/{repo}/issues/<n>/timeline` | State changes and event chronology |
| Issue comments | `gh api repos/{owner}/{repo}/issues/comments` or `gh issue view --json comments` | Thread comments, not review comments |
| GitHub Discussions | `gh api graphql` | No dedicated first-class top-level gh command |

## Common Traps

### Trap 1: Treating issue comments as all PR discussion

PRs inherit issue-thread comments, but review comments are separate. You usually need both surfaces.

### Trap 2: Treating commit comments as review comments

Commit comments are attached to commits, not PR review threads.

### Trap 3: Relying on `gh search commits` for full history

Use it for discovery shortcuts, hashes, phrases, or author lookups. Do not use it as the only source for exhaustive repo history.

### Trap 4: Forgetting that repo-wide issues endpoints include PRs

The issues API mixes plain issues and pull requests. Filter accordingly during synthesis.

### Trap 5: Assuming Discussions support exists

Always check `hasDiscussionsEnabled` before attempting discussion capture.

## Suggested Command Patterns

### Repo capability check

```bash
gh repo view owner/repo --json nameWithOwner,hasDiscussionsEnabled,isPrivate,visibility,url
```

### Repo-wide commit snapshot

```bash
gh api --paginate --slurp \
  "repos/owner/repo/commits?sha=main&per_page=100"
```

### Commit to PR linkage

```bash
gh api --paginate --slurp \
  "repos/owner/repo/commits/<sha>/pulls?per_page=100"
```

### Focused PR trace

```bash
gh pr view 123 -R owner/repo \
  --json number,title,body,comments,commits,files,reviews,url,createdAt,updatedAt
```

### Focused issue timeline

```bash
gh api --paginate --slurp \
  "repos/owner/repo/issues/123/timeline?per_page=100"
```
