# Git Worktrees: ELI5

**Date**: February 14, 2026

---

## What Is a Worktree?

Imagine your repo is a **library book**. Normally you can only read one chapter (branch) at a time — to switch chapters you have to bookmark, close, flip pages.

**Git worktrees** let you photocopy the book and open multiple chapters on separate desks. Desk A has Chapter 5, Desk B has Chapter 12, Desk C has Chapter 3 — all at the same time. But they're all the **same book** (same git history, same remotes).

```
Normal git:
  iggy/  ← can only be on ONE branch at a time
    (switch branch = stash everything, rebuild, lose context)

With worktrees:
  iggy/              ← branch: master (your main work)
  iggy-hotfix/       ← branch: hotfix/crash-fix (separate desk)
  iggy-connector/    ← branch: feat/influxdb-sink (separate desk)

  All three share the SAME .git history. Just different desks.
```

---

## Commands

| Command | What It Does | Example |
|---|---|---|
| `git worktree add <path> <branch>` | New desk for an existing branch | `git worktree add ../iggy-hotfix master` |
| `git worktree add -b <new> <path>` | New branch + new desk | `git worktree add -b feat/auth ../iggy-auth` |
| `git worktree list` | Show all desks | |
| `git worktree remove <path>` | Clean up a desk | `git worktree remove ../iggy-hotfix` |
| `git worktree prune` | Clean stale refs (if you `rm -rf` instead of `remove`) | |

---

## Why Not Just Switch Branches?

| | Branch Switch | Multiple Clones | Worktrees |
|---|---|---|---|
| Shared history? | Yes | No (separate .git) | Yes |
| Disk usage | Low | HIGH (full copy each) | Low (only working files) |
| Context switch cost | HIGH (stash, rebuild) | None | None (just `cd`) |
| Can work in parallel? | No | Yes but wasteful | Yes |

**Worktrees = isolation of clones + efficiency of one repo.**

---

## Worktrees + Claude Code

This is where it gets powerful. You can run **multiple Claude Code sessions in parallel**, each on a different worktree:

```bash
# Your main work
cd ~/Desktop/A01_20260131/iggy
claude

# Terminal 2: Claude fixes a bug in isolation
cd ~/Desktop/A01_20260131/iggy-hotfix
claude -p "Fix the connector timeout issue in #42"

# Terminal 3: Claude writes docs
cd ~/Desktop/A01_20260131/iggy-docs
claude -p "Update the Python SDK documentation"
```

**Key Claude Code features with worktrees:**
- `--add-dir` flag: reference your `cross-repo-knowledge-base` from any worktree
- `/resume` picker shows sessions from all worktrees of the same repo
- Each worktree gets its own session, no interference
- incident.io runs 4-5 parallel Claude agents this way routinely

**The `--add-dir` combo:**
```bash
cd ../iggy-connector
claude --add-dir ~/cross-repo-knowledge-base/agent-room-of-requirements
# Now Claude can see your research docs while working in the worktree
```

---

## Concrete Workflow

**Scenario**: You're mid-feature on iggy. A bug report comes in.

```bash
# Step 1: You're deep in feature work on ab_202602_issue01
cd ~/Desktop/A01_20260131/iggy
# Don't touch anything. Leave this desk as-is.

# Step 2: Create a new desk for the bugfix
git worktree add ../iggy-hotfix master
cd ../iggy-hotfix
git checkout -b hotfix/fix-crash

# Step 3: Fix it (with Claude or manually)
claude
# > Fix the TLS crash...

# Step 4: Done. Go back to feature work. Zero cost.
cd ~/Desktop/A01_20260131/iggy
# Everything exactly as you left it.

# Step 5: Clean up after merge
git worktree remove ../iggy-hotfix
```

---

## Gotchas

1. **Can't check out same branch in two worktrees.** Git enforces this. Use separate branches.
2. **Build artifacts aren't shared.** Each worktree needs its own `cargo build`, `npm install`. (Disk cost: `target/` or `node_modules/` per worktree.)
3. **Submodules don't auto-init** in new worktrees. Run `git submodule update --init`.
4. **Don't `rm -rf` worktrees.** Use `git worktree remove` or run `git worktree prune` after.
5. **Two Claude sessions editing related code = merge conflicts later.** Coordinate task boundaries.

---

## Sources

- [Git Official Worktree Docs](https://git-scm.com/docs/git-worktree)
- [Shipping Faster with Claude Code and Git Worktrees (incident.io)](https://incident.io/blog/shipping-faster-with-claude-code-and-git-worktrees)
- [Git Worktrees for Parallel AI Coding Agents (Upsun)](https://devcenter.upsun.com/posts/git-worktrees-for-parallel-ai-coding-agents/)
- [Mastering Git Worktrees with Claude Code (Medium)](https://medium.com/@dtunai/mastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe)
- [Claude Code Common Workflows (Official Docs)](https://code.claude.com/docs/en/common-workflows)
- [Crystal: Parallel AI Sessions Manager](https://github.com/stravu/crystal)
