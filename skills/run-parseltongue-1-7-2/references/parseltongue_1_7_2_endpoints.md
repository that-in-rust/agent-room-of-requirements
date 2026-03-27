# Parseltongue 1.7.2 Endpoints

Use this reference when running `parseltongue 1.7.2`.

## Orientation Sequence

Run these first:

```bash
curl -fsS "http://localhost:7777/server-health-check-status"
curl -fsS "http://localhost:7777/file-watcher-status-check"
curl -fsS "http://localhost:7777/codebase-statistics-overview-summary"
curl -fsS "http://localhost:7777/folder-structure-discovery-tree"
curl -fsS "http://localhost:7777/api-reference-documentation-help"
```

Use the setup script's `run.config` as the source of truth for `DB_URI`, `WORKSPACE_PATH`, `CODEBASE_PATH`, and `PORT`.
Do not assume the index lives at a guessed `db/codegraph.db` path.

## Search and Read

```bash
curl -fsS "http://localhost:7777/code-entities-list-all"
curl -fsS "http://localhost:7777/code-entities-search-fuzzy?q=main"
curl -fsS "http://localhost:7777/code-entity-detail-view?key=ENTITY_KEY"
```

## Dependency Traversal

```bash
curl -fsS "http://localhost:7777/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "http://localhost:7777/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "http://localhost:7777/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=2"
```

## Architecture and Risk

```bash
curl -fsS "http://localhost:7777/circular-dependency-detection-scan"
curl -fsS "http://localhost:7777/complexity-hotspots-ranking-view?top=10"
curl -fsS "http://localhost:7777/semantic-cluster-grouping-list"
curl -fsS "http://localhost:7777/strongly-connected-components-analysis"
curl -fsS "http://localhost:7777/technical-debt-sqale-scoring"
curl -fsS "http://localhost:7777/coupling-cohesion-metrics-suite"
```

## Context Budgeting

```bash
curl -fsS "http://localhost:7777/smart-context-token-budget?focus=ENTITY_KEY&tokens=4000"
```

## Scoped Queries

Add `scope` to query endpoints:

```bash
curl -fsS "http://localhost:7777/code-entities-list-all?scope=crates||parseltongue-core"
curl -fsS "http://localhost:7777/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=2&scope=crates||parseltongue-core"
```

## Diagnostics

```bash
curl -fsS "http://localhost:7777/file-watcher-status-check"
curl -fsS "http://localhost:7777/ingestion-coverage-folder-report?depth=2"
curl -fsS "http://localhost:7777/ingestion-diagnostics-coverage-report?section=summary"
curl -X POST -fsS "http://localhost:7777/incremental-reindex-file-update?path=src/main.rs"
```

If live edits are not appearing:

1. Check `server-health-check-status` for `"file_watcher_active": true`.
2. Check `file-watcher-status-check` for watcher state and event counters.
3. Inspect `<run-folder>/logs/index.log` and `<run-folder>/logs/server.log`.
4. If watcher is inactive or the workspace is stale, run the reindex script.

When proving auto-reindex, trust the server log plus a query for the changed symbol more than the watcher event counter alone.
