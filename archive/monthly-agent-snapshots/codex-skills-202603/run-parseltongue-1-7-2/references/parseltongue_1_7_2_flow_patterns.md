# Parseltongue 1.7.2 Flow Patterns

Use this reference when the user asks for control flow, data flow, lineage, ingress-to-egress tracing, or "where does the data actually go?"

These are graph-derived approximations built from Parseltongue's dependency and architecture APIs, not perfect runtime traces.

Resolve `SERVER_URL` from `run.config` first.

## Modeling Limits

- Strong for stable caller/callee corridors, layered transitions, shared hubs, sinks, and change risk.
- Weak for branch predicates, exact value propagation, reflection, generated code, queues, config-driven routing, and dynamic dispatch beyond what parsing captured.
- If the conclusion matters and the corridor touches low-coverage files, confirm with direct code reads.

## Pattern Index

1. Ingress-to-sink corridor
2. Gatekeeper choke point
3. Orchestrator versus leaf worker
4. Branch-hub suspicion
5. Feedback loop and re-entry
6. Source-to-sink convergence
7. Sink-to-source accountability trace
8. Transformer ladder
9. Payload gravity well
10. Boundary-crossing lineage
11. Normalizer funnel
12. Parse-frontier caution

## 1) Ingress-to-Sink Corridor

Use when:
- You know an entrypoint, handler, command, job runner, or adapter and want the likely control corridor toward storage, publishing, or network sinks.

Steps:

```bash
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=ENTRY_NAME"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTRY_ENTITY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTRY_ENTITY&hops=3"
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTRY_ENTITY&tokens=8000"
```

Readout:
- A forward path that crosses semantic clusters and ends near obvious sinks approximates the control corridor.
- If the spread stays local, the entrypoint is probably a thin adapter and the real orchestration sits one layer deeper.

## 2) Gatekeeper Choke Point

Use when:
- You want to find the narrow control node that many flows must pass through, such as auth, validation, policy, or routing glue.

Steps:

```bash
curl -fsS "${SERVER_URL}/centrality-measures-entity-ranking?method=pagerank&top=20"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=2"
```

Readout:
- High inbound pressure, bounded outbound spread, and high centrality suggest a gatekeeper.
- If outbound spread is wide and multi-cluster, it is more likely an orchestrator than a true choke point.

## 3) Orchestrator Versus Leaf Worker

Use when:
- You need to decide whether an entity is coordinating flow or just performing one local step.

Steps:

```bash
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/complexity-hotspots-ranking-view?top=20"
curl -fsS "${SERVER_URL}/coupling-cohesion-metrics-suite"
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
```

Readout:
- Orchestrators usually show non-trivial inbound usage, multi-cluster outbound spread, and elevated coupling or hotspot signals.
- Leaf workers usually have bounded outbound reach, local cluster membership, and low blast radius.

## 4) Branch-Hub Suspicion

Use when:
- You suspect a function or module is acting like a dispatcher, strategy switch, or mode router.

Steps:

```bash
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/entropy-complexity-measurement-scores"
curl -fsS "${SERVER_URL}/complexity-hotspots-ranking-view?top=20"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=4000"
```

Readout:
- Wide forward fan-out plus entropy or hotspot evidence suggests branch-heavy control logic.
- Treat this as a prompt to inspect the code for actual branch conditions; the graph alone cannot prove which branch runs when.

## 5) Feedback Loop and Re-Entry

Use when:
- Flow appears to re-enter a prior layer, or behavior looks cyclic rather than cleanly layered.

Steps:

```bash
curl -fsS "${SERVER_URL}/circular-dependency-detection-scan"
curl -fsS "${SERVER_URL}/strongly-connected-components-analysis"
curl -fsS "${SERVER_URL}/kcore-decomposition-layering-analysis"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
```

Readout:
- SCC membership plus meaningful reverse and forward pressure suggests a feedback loop or re-entry corridor.
- Lower-core nodes inside a cycle are often easier break points than the central hubs.

## 6) Source-to-Sink Convergence

Use when:
- You know a likely source and a likely sink and want to see whether they plausibly belong to the same data corridor.

Steps:

```bash
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=SOURCE_NAME"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=SOURCE_ENTITY"
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=SINK_NAME"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=SINK_ENTITY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=SOURCE_ENTITY&hops=3"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=SINK_ENTITY&hops=3"
```

Readout:
- If the forward source side and reverse sink side converge on the same middle entities, the lineage hypothesis is strengthened.
- If they stay disjoint, the sink is probably fed by a different route or an unparsed dynamic path.

## 7) Sink-to-Source Accountability Trace

Use when:
- You start from a write, publish, emit, log, or external side effect and want the most plausible upstream initiators.

Steps:

```bash
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=SINK_NAME"
curl -fsS "${SERVER_URL}/code-entity-detail-view?key=SINK_ENTITY"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=SINK_ENTITY"
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=SINK_ENTITY&tokens=8000"
```

Readout:
- Reverse callers identify who can cause the side effect.
- Callers from different clusters often represent distinct upstream business flows sharing the same sink.

## 8) Transformer Ladder

Use when:
- You suspect the codebase has a chain of parse, validate, normalize, map, enrich, and persist steps.

Steps:

```bash
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=map"
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=transform"
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=normalize"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
```

Readout:
- A bounded chain that crosses a few layers in sequence often approximates a transformer ladder.
- If an entity has extreme inbound usage from unrelated areas, it is probably shared utility code rather than one pipeline rung.

## 9) Payload Gravity Well

Use when:
- You want to find the models, records, or shared payload abstractions that many flows orbit around.

Steps:

```bash
curl -fsS "${SERVER_URL}/centrality-measures-entity-ranking?method=pagerank&top=50"
curl -fsS "${SERVER_URL}/dependency-edges-list-all"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=2"
```

Readout:
- High centrality plus strong inbound and outbound attachment suggests a payload gravity well.
- Changes there are usually schema or contract changes in disguise and deserve broader review.

## 10) Boundary-Crossing Lineage

Use when:
- You need to describe how control or data moves across architectural boundaries such as API to domain to persistence.

Steps:

```bash
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
curl -fsS "${SERVER_URL}/folder-structure-discovery-tree"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=SOURCE_ENTITY"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=SINK_ENTITY"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=SOURCE_ENTITY&tokens=8000"
```

Readout:
- Each cluster or folder transition approximates a boundary crossing.
- Unexpected jumps across unrelated clusters suggest leakage, hidden coupling, or misplaced responsibility.

## 11) Normalizer Funnel

Use when:
- You want to locate the parsing, validation, or normalization step that many inputs converge through before wider downstream use.

Steps:

```bash
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/coupling-cohesion-metrics-suite"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=4000"
```

Readout:
- Many reverse callers paired with a small, stable downstream set suggests a normalizer funnel.
- These nodes are often the safest place to enforce invariants once the code confirms the guess.

## 12) Parse-Frontier Caution

Use when:
- The interesting corridor may pass through files the graph did not fully parse.

Steps:

```bash
curl -fsS "${SERVER_URL}/ingestion-coverage-folder-report?depth=2"
curl -fsS "${SERVER_URL}/ingestion-diagnostics-coverage-report?section=summary"
curl -fsS "${SERVER_URL}/ingestion-diagnostics-coverage-report?section=ignored_files"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
```

Readout:
- Treat well-covered zones as strong graph evidence.
- When the corridor enters ignored or low-coverage files, stop making strong flow claims and verify directly in code.
