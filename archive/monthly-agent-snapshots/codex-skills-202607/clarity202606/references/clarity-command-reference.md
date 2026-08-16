# Clarity Command Reference

Use this reference after `SKILL.md` when you need concrete Clarity command recipes.

## Command-Surface Rule

Run `clarity --help` and the relevant subcommand help before relying on a flag. Clarity changed materially between the installed 0.19.2 binary and fetched `origin/main`.

Known local evidence at skill creation:

| Source | Evidence |
| --- | --- |
| Installed binary | `clarity version 0.19.2`, commit `eb4eba6`, built 2026-05-07 |
| Fetched source | `origin/main` at `99bc1f2`, pushed 2026-07-08 |
| Build attempt | Clean worktree created, but `go` was not installed locally |

## Find the Binary

Prefer:

```bash
CLARITY_BIN="${CLARITY_BIN:-$(command -v clarity)}"
"$CLARITY_BIN" --version
"$CLARITY_BIN" --help
```

Useful local fallbacks observed on this machine:

```bash
/Users/amuldotexe/Desktop/oss-read-only/_tools/clarity/clarity
/Users/amuldotexe/Desktop/oss-read-only/clarity-cli/clarity
```

## Common Recipes

| Goal | Current main style | Older installed style |
| --- | --- | --- |
| Probe version | `clarity --version` | same |
| Supported languages | `clarity languages` | same |
| Extension map | `clarity extensions --format text` | if `extensions` exists |
| Uncommitted impact | `clarity show -f mermaid` | same |
| Latest commit | `clarity show -c HEAD -f mermaid` | same |
| Branch range | `clarity show -c main...HEAD -f mermaid` | same |
| Scope to paths | `clarity show src tests` | `clarity show -i src,tests` |
| File blast radius | `clarity show path/to/file --reach both --depth 2` | `clarity show -p path/to/file --level 2` |
| Upstream dependents | `clarity show path/to/file --reach up` | may not be available |
| Path coupling | `clarity show --between a,b` | `clarity show -w a,b` |
| Shareable graph | `clarity show -u` | same |
| Live graph | `clarity watch src --reach both` | `clarity watch -i src` |
| Module summary | `clarity modules` | may not be available |
| Module graph | `clarity show --module name --reach both` | may not be available |
| Cycle audit | `clarity cycles src` | may not be available |
| Workspace graph | `clarity workspace --language auto` | same if exposed |

## Main-Only Features

Use these only after help confirms them:

- `clarity modules`: list `.clarity/modules.json` modules with file counts.
- `clarity cycles [path...]`: list circular file dependencies; `-u` can emit URLs.
- `clarity show --reach up|down|both`: walk dependencies from an anchor.
- `clarity show --all --collapse`: render whole tree collapsed into declared modules.
- `clarity show --module <name>`: render a declared module in context.
- `clarity show --prune <path>`: show a node but skip its subtree.
- `clarity show --also <glob>`: add matching files that connect to the reach graph.

## Output Interpretation

For a developer-facing summary, answer:

- What files or modules are central in the graph?
- Which edges cross expected boundaries?
- Are tests or docs connected to the changed production files?
- Are cycles present?
- Is the graph too broad because the command lacked a tight anchor?
- Which Clarity limitations matter for the conclusion?

Avoid saying Clarity proves behavior. Say it shows structural coupling or impact.

## Rebuild From Main

Use this when the installed binary lacks commands needed for the task:

```bash
git fetch origin main --prune
git worktree add --detach /tmp/clarity-main-build origin/main
cd /tmp/clarity-main-build
make build-dev
./clarity --version
./clarity --help
```

Do not run this inside a dirty checkout unless the user explicitly wants to use the dirty worktree. `make build-dev` depends on Go 1.21+ with CGO enabled and Node/npm for the watch UI assets.

## Setup Command

`clarity setup` writes Clarity guidance into `AGENTS.md`. Use it only when the user wants repo instructions changed. Check the diff afterward.
