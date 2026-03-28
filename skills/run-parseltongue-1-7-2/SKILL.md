---
name: run-parseltongue-1-7-2
description: Install and run parseltongue 1.7.2 in an isolated user-space run folder, verify the actual bound server URL, and query a codebase through the HTTP API for orientation, entity lookup, forward and backward dependency tracing, blast radius, architecture scans, incremental reindexing, and higher-order graph workflows such as meet-in-the-middle debugging, safe refactoring, seam discovery, boundary audits, cycle breaking, migration choreography, and derived control-flow or data-flow investigations. Use when Codex must pin to version 1.7.2, needs graph-based code understanding, or must refresh an existing run folder without version drift.
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
7. Do not assume `http://localhost:7777` is the live server after setup or refresh; Parseltongue can auto-select the next available port.
8. Prefer `SERVER_URL` in `run.config` when present. If it is missing, read the actual bound server URL from `<run-folder>/logs/server.log`.
9. Treat `api-reference-documentation-help` as the live source of truth for endpoint names and parameters.

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

## Flow Modeling Guardrail

Treat control-flow and data-flow conclusions from Parseltongue as graph-derived approximations, not perfect runtime truth.
These APIs are strongest for dependency topology, caller pressure, downstream spread, cluster boundaries, architectural reach, and change risk.
When a flow question depends on branch conditions, exact value propagation, dynamic dispatch, reflection, generated code, or low-coverage files, use Parseltongue to narrow the search space first and then confirm with direct code reads.

## Run Workflow

1. Run installer and setup script:
```bash
./scripts/setup_parseltongue_1_7_2.sh /path/to/codebase
```
2. Capture the printed run folder path, workspace path, DB URI, and actual server URL. If the requested port is busy, setup may bind to the next available port.
3. Load `<run-folder>/run.config` and prefer `SERVER_URL`, `DB_URI`, `WORKSPACE_PATH`, and `CODEBASE_PATH` from there.
4. Verify health, watcher status, and the new-codebase orientation queries:
```bash
curl -fsS "${SERVER_URL}/server-health-check-status"
curl -fsS "${SERVER_URL}/file-watcher-status-check"
curl -fsS "${SERVER_URL}/codebase-statistics-overview-summary"
curl -fsS "${SERVER_URL}/circular-dependency-detection-scan"
curl -fsS "${SERVER_URL}/complexity-hotspots-ranking-view?top=10"
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
curl -fsS "${SERVER_URL}/ingestion-coverage-folder-report?depth=2"
curl -fsS "${SERVER_URL}/folder-structure-discovery-tree"
curl -fsS "${SERVER_URL}/api-reference-documentation-help"
```
5. If watcher health is false or stale, inspect `<run-folder>/logs/server.log` and `<run-folder>/logs/index.log` before assuming the index is usable.
   If watcher status looks ambiguous, confirm with a small code edit and a `code-entities-search-fuzzy` query for the new symbol.
6. Run focused analysis queries or a bidirectional investigation workflow:
```bash
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=main"
curl -fsS "${SERVER_URL}/code-entity-detail-view?key=ENTITY_KEY"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=2"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=4000"
```
7. Stop server when done:
```bash
./scripts/stop_parseltongue_server.sh /path/to/run-folder
```

## Bidirectional Workflows

- Trace backward from a symptom:
  Search the broken function, read its code, inspect `reverse-callers-query-graph`, then quantify depth with `blast-radius-impact-analysis`. Use this for bug hunting and trigger discovery.
- Trace forward from a candidate change:
  Read the entity, inspect `forward-callees-query-graph`, then quantify downstream impact with `blast-radius-impact-analysis` and pull the surrounding code with `smart-context-token-budget`. Use this for implementation planning and dependency drilling.
- Quantify refactor risk:
  Check direct callers, blast radius with `hops=3`, circular dependencies, and then request a larger smart-context budget such as `tokens=8000`. Treat 0-5 direct callers as low risk, 6-15 as medium, and more than 15 as high. If blast radius exceeds 100 at `hops=2`, assume you are touching critical infrastructure.
- Load advanced recipes when the user wants creative graph workflows such as meet-in-the-middle debugging, cycle-breaking, deletion safety, migration choreography, boundary-leak detection, or seam discovery:
  Read [references/parseltongue_1_7_2_bidirectional_workflows.md](references/parseltongue_1_7_2_bidirectional_workflows.md).
- Load derived flow recipes when the user wants approximated control flow, data flow, lineage, ingress-to-egress tracing, transformer ladders, orchestrator detection, or boundary-crossing analysis:
  Read [references/parseltongue_1_7_2_flow_patterns.md](references/parseltongue_1_7_2_flow_patterns.md).

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
- `SERVER_URL`
- `DB_URI`
- `WORKSPACE_PATH`
- `CODEBASE_PATH`
- `PORT`
- `REQUESTED_PORT`

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
- the server URL or bound port may have changed after restart and must be re-read from `run.config` or `server.log`

## Global Shortcuts

Use global shell wrappers (available from any directory):

```bash
pt172-setup /path/to/codebase
pt172-refresh /path/to/run-folder
pt172-stop /path/to/run-folder
```

## Query Guidance

Read [references/parseltongue_1_7_2_endpoints.md](references/parseltongue_1_7_2_endpoints.md) for:
- the 5-query orientation pass
- endpoint selection by question
- backward bug-hunting flow
- forward dependency-tracing flow
- safe-refactoring risk checks
- diagnostics and incremental reindex examples

Read [references/parseltongue_1_7_2_bidirectional_workflows.md](references/parseltongue_1_7_2_bidirectional_workflows.md) for:
- meet-in-the-middle hypothesis testing
- symptom-to-system corridor tracing
- migration choreography
- narrow-waist seam discovery
- boundary-leak detection
- cycle-breaker scouting
- deletion-safety classification

Read [references/parseltongue_1_7_2_flow_patterns.md](references/parseltongue_1_7_2_flow_patterns.md) for:
- control-flow approximations from the dependency graph
- data-flow and lineage approximations from the dependency graph
- ingress-to-egress tracing
- orchestrator versus transformer classification
- model or payload gravity analysis
