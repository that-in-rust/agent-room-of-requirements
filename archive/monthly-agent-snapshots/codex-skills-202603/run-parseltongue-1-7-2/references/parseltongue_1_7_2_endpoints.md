# Parseltongue 1.7.2 Endpoints

Use this reference when running `parseltongue 1.7.2`.

For higher-order recipes that combine these endpoints into creative forward and backward investigations, read [parseltongue_1_7_2_bidirectional_workflows.md](./parseltongue_1_7_2_bidirectional_workflows.md).
For derived control-flow and data-flow investigations built from the current graph APIs, read [parseltongue_1_7_2_flow_patterns.md](./parseltongue_1_7_2_flow_patterns.md).

## Resolve the Base URL First

Do not assume `http://localhost:7777`.

Use the actual server URL for the current run:

```bash
# shellcheck source=/dev/null
source /path/to/run-folder/run.config
SERVER_URL="${SERVER_URL:-http://localhost:${PORT}}"
```

If `SERVER_URL` is missing or looks stale, inspect `/path/to/run-folder/logs/server.log` and extract the last `http://localhost:PORT` line.

Use `api-reference-documentation-help` as the live source of truth for endpoint names and parameters.

## Orientation Sequence

Run these first on a new codebase:

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

After this pass, you should know scale, parse confidence, structural hotspots, module groupings, and whether circular dependencies are present.

## Search and Read

```bash
curl -fsS "${SERVER_URL}/code-entities-list-all"
curl -fsS "${SERVER_URL}/code-entities-list-all?entity_type=function"
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=main"
curl -fsS "${SERVER_URL}/code-entity-detail-view?key=ENTITY_KEY"
```

## Dependency Traversal

```bash
curl -fsS "${SERVER_URL}/dependency-edges-list-all"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=2"
```

These endpoints support strong topology-based flow reasoning, but not exact runtime branch execution or precise value propagation.

## Bidirectional Workflows

### Trace Backward from a Symptom

Use this for bug hunting:

```bash
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=FUNCTION_NAME"
curl -fsS "${SERVER_URL}/code-entity-detail-view?key=ENTITY_KEY"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=2"
```

Interpretation:
- `reverse-callers-query-graph` answers "who uses this?"
- `blast-radius-impact-analysis` answers "how far does the problem spread?"

### Trace Forward from a Candidate Change

Use this for dependency drill-down and implementation planning:

```bash
curl -fsS "${SERVER_URL}/code-entity-detail-view?key=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=2"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=4000"
```

Interpretation:
- `forward-callees-query-graph` answers "what does this use?"
- `smart-context-token-budget` packages the highest-value local context around that entity for LLM work.

### Quantify Refactor Risk Before Changing

```bash
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=3"
curl -fsS "${SERVER_URL}/circular-dependency-detection-scan"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=8000"
```

Risk heuristics:
- 0-5 direct callers usually means low risk.
- 6-15 direct callers usually means medium risk.
- More than 15 direct callers usually means high risk.
- Blast radius greater than 100 at `hops=2` usually means critical infrastructure or broad cross-cutting behavior.

## Architecture and Risk

```bash
curl -fsS "${SERVER_URL}/circular-dependency-detection-scan"
curl -fsS "${SERVER_URL}/complexity-hotspots-ranking-view?top=10"
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
curl -fsS "${SERVER_URL}/strongly-connected-components-analysis"
curl -fsS "${SERVER_URL}/technical-debt-sqale-scoring"
curl -fsS "${SERVER_URL}/kcore-decomposition-layering-analysis"
curl -fsS "${SERVER_URL}/centrality-measures-entity-ranking?method=pagerank&top=20"
curl -fsS "${SERVER_URL}/entropy-complexity-measurement-scores"
curl -fsS "${SERVER_URL}/coupling-cohesion-metrics-suite"
curl -fsS "${SERVER_URL}/leiden-community-detection-clusters"
```

## Context Budgeting

```bash
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=4000"
```

Use larger budgets such as `8000` for refactors or complex debugging passes.

## Scoped Queries

Add `scope` when you want to limit the search space:

```bash
curl -fsS "${SERVER_URL}/code-entities-list-all?scope=crates||parseltongue-core"
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=main&scope=crates||parseltongue-core"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=2&scope=crates||parseltongue-core"
```

## Which Endpoint Fits Which Question

| Question | Endpoint |
| --- | --- |
| How big is this? | `/codebase-statistics-overview-summary` |
| Where is X? | `/code-entities-search-fuzzy` |
| What is X? | `/code-entity-detail-view` |
| Who uses X? | `/reverse-callers-query-graph` |
| What does X use? | `/forward-callees-query-graph` |
| What breaks if I change X? | `/blast-radius-impact-analysis` |
| Is architecture healthy? | `/circular-dependency-detection-scan` |
| Where is the complexity? | `/complexity-hotspots-ranking-view` |
| What are the modules? | `/semantic-cluster-grouping-list` |
| Give me LLM context | `/smart-context-token-budget` |
| How much was parsed? | `/ingestion-coverage-folder-report` |
| What folders exist? | `/folder-structure-discovery-tree` |
| Parse quality diagnostics? | `/ingestion-diagnostics-coverage-report` |
| Find dependency cycles with SCC | `/strongly-connected-components-analysis` |
| Score technical debt | `/technical-debt-sqale-scoring` |
| Separate core from peripheral code | `/kcore-decomposition-layering-analysis` |

## Diagnostics and Incremental Reindex

```bash
curl -fsS "${SERVER_URL}/file-watcher-status-check"
curl -fsS "${SERVER_URL}/ingestion-coverage-folder-report?depth=2"
curl -fsS "${SERVER_URL}/ingestion-diagnostics-coverage-report?section=summary"
curl -fsS "${SERVER_URL}/ingestion-diagnostics-coverage-report?section=word_coverage"
curl -fsS "${SERVER_URL}/ingestion-diagnostics-coverage-report?section=test_entities"
curl -fsS "${SERVER_URL}/ingestion-diagnostics-coverage-report?section=ignored_files"
curl -X POST -fsS "${SERVER_URL}/incremental-reindex-file-update?path=src/main.rs"
```

If live edits are not appearing:

1. Check `server-health-check-status` for `"file_watcher_active": true`.
2. Check `file-watcher-status-check` for watcher state and event counters.
3. Inspect `/path/to/run-folder/logs/index.log` and `/path/to/run-folder/logs/server.log`.
4. If the watcher is inactive, the server URL is stale, or the workspace is suspect, run the reindex script and then reload `run.config`.

When proving auto-reindex, trust the server log plus a query for the changed symbol more than the watcher event counter alone.
