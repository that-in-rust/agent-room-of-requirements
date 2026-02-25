# Iggy Fork Sync Status — February 14, 2026

## Current State

| Metric | Value |
|---|---|
| Fork | `amuldotexe/iggy` |
| Upstream | `apache/iggy` |
| Default branch | `master` (not main) |
| Feature branch | `ab_202602_issue01` |
| Fork `master` vs upstream | **18 commits BEHIND** |
| Feature branch vs fork `master` | **2 commits ahead** |

## Remotes

```
origin    https://github.com/amuldotexe/iggy.git (fetch/push)
```

**No `upstream` remote configured.** Needs to be added.

## To Sync

```bash
# 1. Add upstream
git remote add upstream https://github.com/apache/iggy.git

# 2. Fetch upstream
git fetch upstream

# 3. Update fork's master
git checkout master
git merge upstream/master
git push origin master

# 4. Rebase feature branch
git checkout ab_202602_issue01
git rebase master
```

## Feature Branch Commits

1. `9403c37d` — docs: add connector analysis and best practices documentation
2. `9d266822` — docs: move connector research to cross-repo-knowledge-base

Note: Both commits are docs-only (research files added then moved to cross-repo). If planning to PR to upstream, this branch may need to be rebased or started fresh from synced master.
