# Cross-Repo Knowledge Base: How It Works

## The Problem

You contribute to multiple OSS repos (iggy, arrow, datafusion, etc.). You generate research, analysis, and notes for each. But:
- Committing research into the fork pollutes PRs to upstream
- Keeping research in a separate repo means it's disconnected from the project
- Copying between repos means multiple stale copies

## The Solution

One repo. One clone. Symlinked everywhere. Invisible to upstream.

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        YOUR MACHINE                                 │
│                                                                     │
│  ~/cross-repo-knowledge-base/                                       │
│  └── agent-room-of-requirements/          <-- ONE clone (source     │
│      ├── .git/                                of truth)             │
│      ├── cross-repo-link.sh               <-- automation script    │
│      ├── HOW-IT-WORKS.md                  <-- this file            │
│      ├── CROSS-REPO-SETUP.md                                       │
│      ├── A00-LLM-Principles01.md                                   │
│      ├── A01-LLM-Workflow01.md                                     │
│      └── iggy/                            <-- per-project research │
│          ├── connector-issues-resolved-summary.md                   │
│          ├── connector-best-practices-patterns.md                   │
│          └── connector-minto-pyramid-summary.md                     │
│                         ^                                           │
│                         |                                           │
│                    (symlink)                                        │
│                         |                                           │
│  ~/Desktop/A01_20260131/iggy/             <-- fork of apache/iggy  │
│      ├── .git/                                                      │
│      │   └── info/exclude                 <-- "cross-repo-          │
│      │       ├── cross-repo-knowledge-base     knowledge-base"      │
│      │       └── parseltongue*/                (LOCAL ONLY,         │
│      │                                          never committed)    │
│      ├── core/                                                      │
│      ├── docs/                            <-- original project docs │
│      ├── foreign/                              (no research here)   │
│      ├── cross-repo-knowledge-base -------> SYMLINK                 │
│      └── parseltongue20260208*/           <-- also excluded         │
│                                                                     │
│                                                                     │
│  ~/Desktop/future-project/                <-- ANY future project    │
│      ├── .git/                                                      │
│      │   └── info/exclude                                           │
│      │       └── cross-repo-knowledge-base                          │
│      └── cross-repo-knowledge-base -------> SAME SYMLINK            │
│                                                  |                  │
│                                                  |                  │
│                                                  v                  │
│                                            SAME FOLDER              │
│                                            SAME FILES               │
│                                            INSTANT SYNC             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                              |
                         git push/pull
                              |
                              v
┌─────────────────────────────────────────────────────────────────────┐
│  GITHUB                                                             │
│                                                                     │
│  that-in-rust/agent-room-of-requirements    <-- shared research     │
│      (public, main branch)                      repo on GitHub      │
│                                                                     │
│  apache/iggy                                <-- upstream, sees      │
│      (has NO idea this exists)                  NOTHING              │
│                                                                     │
│  amuldotexe/iggy                            <-- your fork, also     │
│      (clean commits, no research files)         sees NOTHING         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## The Key Trick

`.git/info/exclude` works exactly like `.gitignore` but is **local-only** — it's inside `.git/` so it never gets committed, never shows up in diffs, and upstream never knows it exists.

## Central Location

Everything is driven from one directory:

```
~/cross-repo-knowledge-base/agent-room-of-requirements/
```

This is the only real copy. Every project just has a symlink pointing here. Edit a file from iggy, it's the same file if you open it from another project. No syncing, no copying, no conflicts.

## Quick Start

### First time (once ever)
```bash
# Clone to central location
mkdir -p ~/cross-repo-knowledge-base
git clone https://github.com/that-in-rust/agent-room-of-requirements.git \
    ~/cross-repo-knowledge-base/agent-room-of-requirements
```

### Link into any project (once per project)
```bash
cd ~/Desktop/your-project
~/cross-repo-knowledge-base/agent-room-of-requirements/cross-repo-link.sh
```

That's it. The script:
1. Creates the symlink
2. Adds it to `.git/info/exclude`
3. Creates a project subfolder if needed

### Daily use
```bash
# Check status
cross-repo-link.sh status

# Pull latest research from GitHub
cross-repo-link.sh sync

# Push your changes
cross-repo-link.sh push

# Remove from a project
cross-repo-link.sh unlink
```

## Folder Convention

Each project gets its own subfolder in the knowledge base:

```
agent-room-of-requirements/
    iggy/                    <-- Apache Iggy research
    arrow/                   <-- future: Apache Arrow
    datafusion/              <-- future: DataFusion
    ...
```

## Why Not Submodules?

| | Submodule | This approach |
|---|-----------|---------------|
| Visible to upstream? | Yes (.gitmodules is committed) | No |
| Auto-sync across projects? | No (pinned to SHA) | Yes (same folder) |
| Needs manual update? | Yes (`git submodule update`) | No (it's a symlink) |
| Modifies tracked files? | Yes | No |
| Setup per project | `git submodule add ...` + commit | 1 command, no commit |
