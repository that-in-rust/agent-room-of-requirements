---
name: clarity202606
description: Use Clarity, the LegacyCodeHQ structural design CLI, for dependency impact graphs, architecture/refactoring verification, before-commit design checks, code review context, cycle/module/workspace exploration, AGENTS.md Clarity setup, or rebuilding/probing Clarity command availability. Use when Codex needs to run or interpret clarity show, watch, languages, extensions, modules, cycles, workspace, setup, or version-specific Clarity commands.
---

# Clarity202606

Use this skill to run Clarity as a structural verification tool for code changes and repo architecture. Clarity works at file granularity: it shows coupling, impact, boundaries, cycles, and change shape; it does not prove runtime behavior, API contracts, or semantic correctness.

## First Move

Probe the active binary before choosing commands:

```bash
/Users/amuldotexe/.codex/skills/clarity202606/scripts/probe_clarity.sh
```

If the script reports no binary, do not install or rebuild automatically unless the user asks. If a repo has uncommitted changes, do not pull or rebuild in place; use a clean worktree or temp clone.

## Workflow

1. Resolve context.
- Run from the target repo root when possible.
- If working from another directory, pass `--repo <path>`.
- Check `git status --short --branch` before recommending commit/range commands.

2. Pick the analysis mode.
- Current uncommitted work: `clarity show -f mermaid` or `clarity show -f dot`.
- Latest commit or branch range: `clarity show -c HEAD` or `clarity show -c main...HEAD`.
- Specific files or directories: prefer the syntax shown by `clarity show --help`.
- Refactor blast radius: on current `main`, use `clarity show <file> --reach up|down|both --depth <n>`.
- Path explanation: use `--between a,b` or old-release `-w a,b`, depending on help output.
- Live feedback during active editing: `clarity watch`, usually with `--port` if 4900 is busy.
- Module/cycle/workspace analysis: only use `modules`, `cycles`, or `workspace` if `clarity --help` exposes them.

3. Choose output for the environment.
- Use `-f mermaid` when the client can render Mermaid or when the user wants Markdown-friendly output.
- Use DOT when Graphviz tooling or raw graph parsing is better.
- Use `-u` only for shareable/browser visualization; do not assume it auto-opens a browser.

4. Interpret cautiously.
- Look for unexpected cross-boundary edges, missing tests near changed code, high-degree files, cycles, and module leakage.
- Treat Clarity output as structural evidence, not proof of correctness.
- Pair with tests/typechecks for implementation claims.

5. Report results.
- State the exact Clarity command and binary/version used.
- Summarize the graph in plain engineering terms.
- Call out caveats: unsupported extensions, dirty repo state, command-surface mismatch, or a graph that is too broad/noisy.

## Version Awareness

The local installed binary may lag fetched `origin/main`. Always trust live `clarity --help` for available commands and flags.

Observed split while creating this skill:

- Installed binary `0.19.2` exposed `extensions`, `languages`, `setup`, `show`, `watch`, and `workspace`.
- Fetched `origin/main` also documented `modules`, `cycles`, positional `clarity show <paths...>`, `--reach`, `--all`, `--collapse`, and module selection.

Read [references/clarity-command-reference.md](references/clarity-command-reference.md) when you need command recipes, rebuild guidance, or old-vs-main compatibility notes.

## Rebuild Guidance

Rebuild only when the user wants current `main` behavior or the installed binary lacks needed commands.

Use a clean worktree when the repo is dirty:

```bash
git fetch origin main --prune
git worktree add --detach /tmp/clarity-main-build origin/main
cd /tmp/clarity-main-build
make build-dev
./clarity --version
```

Requirements: Go 1.21+ with CGO enabled, plus Node/npm for the watch web assets. If Go or Node is missing, ask before installing system tooling.

## Resources

- `scripts/probe_clarity.sh`: locate a usable Clarity binary and print live command help.
- `references/clarity-command-reference.md`: command recipes, compatibility notes, and interpretation checklist.
