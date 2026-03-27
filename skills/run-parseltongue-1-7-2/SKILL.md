---
name: run-parseltongue-1-7-2
description: Install and run parseltongue 1.7.2 in an isolated user-space run folder, keep the generated workspace inside that run folder, verify watcher health, then index and query a codebase through the HTTP API. Use when Codex must pin parseltongue to version 1.7.2, create a new folder per setup away from the current workspace, confirm live auto-reindex behavior, avoid version drift while doing code graph queries, or refresh/reindex an existing run folder on demand.
---

# Run Parseltongue 1.7.2

Use this skill to install `parseltongue 1.7.2`, create a fresh run folder, index a target codebase, launch the query server, and run initial API queries.
Default retention policy: clean run folders older than 1 day before each new setup.
Default storage location: `${CODEX_HOME:-$HOME/.codex}/tool-runs/parseltongue-1-7-2`.

## Ground Truth

Treat these as non-obvious but binding:

1. Do not assume `pt01-folder-to-cozodb-streamer --db ...` will honor the requested DB path.
2. Trust the `DB_URI` and `WORKSPACE_PATH` recorded in `run.config`, not an assumed `db/codegraph.db` path.
3. Verify both health and watcher status before assuming live auto-reindex works.
4. Treat server logs and changed-symbol queries as the strongest proof of incremental reindex; watcher counters can lag or stay at zero.
5. Keep the Parseltongue run folder outside any directory that may later be zipped or uploaded.
6. Prefer the default user-space run home unless the user explicitly wants a different `--base-dir`.

## Enforce Version Policy

Follow these rules on every use:

1. Pin to `v1.7.2` only.
2. Verify `parseltongue --version` contains `1.7.2` before indexing or querying.
3. Create a new timestamped run folder every setup.
   Default name pattern: `parseltongue-1.7.2-<codebase-slug>-<timestamp>`.
4. Keep binary, workspace DB, logs, and query artifacts inside that run folder.
5. Refuse to proceed if version check fails.
6. Clean folders older than 1 day by default during setup.

## Code Reading Preference

Prefer Parseltongue queries to read and understand code.
Use direct file reads (`rg`, `cat`, editor open) only if relevant entities or relationships cannot be found through Parseltongue, or coverage/endpoint diagnostics show the needed area is not available.

## Run Workflow

1. Run installer and setup script:
```bash
./scripts/setup_parseltongue_1_7_2.sh /path/to/codebase
```
2. Capture the printed run folder path, workspace path, DB URI, and server URL.
3. Run orientation queries:
```bash
curl -fsS "http://localhost:7777/server-health-check-status"
curl -fsS "http://localhost:7777/file-watcher-status-check"
curl -fsS "http://localhost:7777/codebase-statistics-overview-summary"
curl -fsS "http://localhost:7777/folder-structure-discovery-tree"
```
4. If watcher health is false or stale, inspect `<run-folder>/logs/server.log` and `<run-folder>/logs/index.log` before assuming the index is usable.
   If watcher status looks ambiguous, confirm with a small code edit and a `code-entities-search-fuzzy` query for the new symbol.
5. Run focused analysis queries:
```bash
curl -fsS "http://localhost:7777/code-entities-search-fuzzy?q=main"
curl -fsS "http://localhost:7777/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "http://localhost:7777/smart-context-token-budget?focus=ENTITY_KEY&tokens=4000"
```
6. Stop server when done:
```bash
./scripts/stop_parseltongue_server.sh /path/to/run-folder
```

## Script Parameters

Use setup script options as needed:

```bash
./scripts/setup_parseltongue_1_7_2.sh /path/to/codebase \
  --base-dir "${CODEX_HOME:-$HOME/.codex}/tool-runs/parseltongue-1-7-2" \
  --port 7777 \
  --hops 2 \
  --cleanup-days 1
```

- `--base-dir`: Parent directory that receives a new timestamped run folder. Default: `${CODEX_HOME:-$HOME/.codex}/tool-runs/parseltongue-1-7-2`.
- `--port`: HTTP server port.
- `--hops`: Blast radius hop count for initial query capture.
- `--cleanup-days`: Remove run folders older than this many days before setup (default `1`).

After setup, use `<run-folder>/run.config` as the canonical source for:
- `DB_URI`
- `WORKSPACE_PATH`
- `CODEBASE_PATH`
- `PORT`

## Reindex Existing Run

Reindex an existing run folder without re-downloading:

```bash
./scripts/reindex_parseltongue_1_7_2.sh /path/to/run-folder
```

Optional overrides:

```bash
./scripts/reindex_parseltongue_1_7_2.sh /path/to/run-folder \
  --codebase-path /path/to/codebase \
  --port 7777
```

If the user says "refresh", "refresh index", or "reindex", run this reindex script.
Use refresh when:
- watcher health is false
- live file edits are not appearing in queries
- the workspace DB is stale or suspect

## Global Shortcuts

Use global shell wrappers (available from any directory):

```bash
pt172-setup /path/to/codebase
pt172-refresh /path/to/run-folder
pt172-stop /path/to/run-folder
```

## Query Guidance

Read [references/parseltongue_1_7_2_endpoints.md](references/parseltongue_1_7_2_endpoints.md) for endpoint workflows and exact query examples.
