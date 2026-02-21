# Cross-Repo Knowledge Base: Setup Guide

## How It Works

This repo (`agent-room-of-requirements`) is cloned once to a central location and symlinked into every project you work on. All repos see the same folder, changes are instant everywhere, and it's invisible to upstream.

```
~/cross-repo-knowledge-base/agent-room-of-requirements/  <- ONE clone, source of truth
    iggy/                  <- per-project research
    CROSS-REPO-SETUP.md   <- this file

~/Desktop/project-A/cross-repo-knowledge-base  ->  symlink
~/Desktop/project-B/cross-repo-knowledge-base  ->  symlink
```

## Initial Setup (done once)

```bash
mkdir -p ~/cross-repo-knowledge-base
git clone https://github.com/that-in-rust/agent-room-of-requirements.git ~/cross-repo-knowledge-base/agent-room-of-requirements
```

## Add to Any Project (2 commands)

From any project root:

```bash
ln -s ~/cross-repo-knowledge-base/agent-room-of-requirements cross-repo-knowledge-base
echo "cross-repo-knowledge-base" >> .git/info/exclude
```

- `.git/info/exclude` works like `.gitignore` but is LOCAL-ONLY
- Never committed, never seen by upstream
- No .gitmodules, no submodule references

## Why Symlink Over Submodules

| Feature | Submodule | Symlink |
|---------|-----------|---------|
| Invisible to upstream | No | Yes |
| Synced across repos | No (per-repo copy) | Yes (one source) |
| Changes instant everywhere | No | Yes |
| Easy to add to new projects | Medium | 2 commands |
| Modifies tracked files | Yes (.gitmodules) | No |

## Project Research Folders

Each project gets its own subfolder:

```
agent-room-of-requirements/
    iggy/                    <- Apache Iggy connector research
    <next-project>/          <- future projects go here
```
