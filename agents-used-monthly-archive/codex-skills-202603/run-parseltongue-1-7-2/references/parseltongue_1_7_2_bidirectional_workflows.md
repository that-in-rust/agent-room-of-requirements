# Parseltongue 1.7.2 Bidirectional Workflows

Use this reference when the basic forward and backward traces are not enough and the user needs a stronger investigation pattern.

Resolve `SERVER_URL` from `run.config` first.

## Workflow Index

1. Meet-in-the-middle hypothesis test
2. Symptom-to-system corridor trace
3. Change choreography for staged migrations
4. Narrow-waist seam discovery
5. Boundary-leak detector
6. Cycle-breaker scout
7. Deletion-safety classifier
8. Hotspot pressure-versus-sink split
9. Parse-frontier probe
10. Ownership and review router
11. Source-to-sink convergence trace
12. Sink-to-source accountability trace
13. Orchestrator split planner

## 1) Meet-in-the-Middle Hypothesis Test

Use when:
- You have a suspected root cause and a visible symptom, but you do not yet know whether they are truly connected.

Steps:

```bash
# Symptom side: who reaches the broken point?
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=SYMPTOM_NAME"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=SYMPTOM_ENTITY"

# Root-cause side: what does the suspected culprit reach?
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=ROOT_NAME"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ROOT_ENTITY"

# Quantify each side
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=SYMPTOM_ENTITY&hops=2"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ROOT_ENTITY&hops=2"
```

Readout:
- If the reverse side and forward side converge on the same mid-layer entities, your hypothesis is strengthened.
- If they stay disjoint, your hypothesis is weak and you should search for a different trigger or root candidate.

## 2) Symptom-to-System Corridor Trace

Use when:
- A local bug may actually be a corridor problem that spans entrypoints, orchestration, and downstream helpers.

Steps:

```bash
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=FUNCTION_NAME"
curl -fsS "${SERVER_URL}/code-entity-detail-view?key=ENTITY_KEY"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=3"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=8000"
```

Readout:
- Reverse callers expose upstream triggers.
- Forward callees expose downstream sinks and collaborators.
- Blast radius tells you whether the bug corridor is local, layered, or systemic.

## 3) Change Choreography for Staged Migrations

Use when:
- You want to replace, deprecate, rename, or re-contract an entity without breaking dependents.

Steps:

```bash
curl -fsS "${SERVER_URL}/code-entity-detail-view?key=ENTITY_KEY"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=3"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=8000"
```

Readout:
- Reverse callers define migration sites.
- Forward callees define hidden implementation coupling.
- Blast radius helps split the rollout into phases.

Suggested phase order:
1. Stabilize downstream dependencies.
2. Update a small caller slice.
3. Reindex and re-query.
4. Expand to the next caller slice.

## 4) Narrow-Waist Seam Discovery

Use when:
- You want to extract an interface, isolate a service boundary, or identify the best “waist” between many callers and a bounded dependency set.

Steps:

```bash
curl -fsS "${SERVER_URL}/complexity-hotspots-ranking-view?top=20"
curl -fsS "${SERVER_URL}/centrality-measures-entity-ranking?method=pagerank&top=20"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=8000"
```

Readout:
- Good seam candidates usually have substantial inbound pressure, bounded outbound spread, and clear local context.
- Avoid extracting around entities whose forward graph is chaotic and unbounded; those are usually unstable seams.

## 5) Boundary-Leak Detector

Use when:
- You suspect a module boundary is leaking across layers or semantic clusters.

Steps:

```bash
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
curl -fsS "${SERVER_URL}/folder-structure-discovery-tree"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/circular-dependency-detection-scan"
curl -fsS "${SERVER_URL}/strongly-connected-components-analysis"
```

Readout:
- Reverse callers from unexpected modules suggest inbound leakage.
- Forward callees into unexpected modules suggest outbound leakage.
- SCC or cycle evidence raises the urgency because boundary leaks inside cycles are harder to unwind.

## 6) Cycle-Breaker Scout

Use when:
- The architecture has cycles and you need the least painful break point.

Steps:

```bash
curl -fsS "${SERVER_URL}/circular-dependency-detection-scan"
curl -fsS "${SERVER_URL}/strongly-connected-components-analysis"
curl -fsS "${SERVER_URL}/kcore-decomposition-layering-analysis"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
```

Readout:
- Favor break candidates with fewer reverse callers, tighter forward dependency sets, and lower core-ness.
- Be cautious breaking nodes with high inbound pressure and centrality; they are often structural hubs rather than accidental cycle participants.

## 7) Deletion-Safety Classifier

Use when:
- You want to know whether an entity is removable, merely obscure, or actually critical.

Steps:

```bash
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=ENTITY_KEY&hops=2"
curl -fsS "${SERVER_URL}/centrality-measures-entity-ranking?method=pagerank&top=50"
```

Readout:
- Low reverse usage, low forward spread, and low centrality suggest deletion might be safe.
- Low reverse usage but high forward spread often means hidden infrastructure glue rather than dead code.
- High reverse usage or high blast radius means do not delete casually.

## 8) Hotspot Pressure-Versus-Sink Split

Use when:
- A hotspot is clearly painful, but you do not yet know whether the main issue is too many upstream demands or too much downstream entanglement.

Steps:

```bash
curl -fsS "${SERVER_URL}/complexity-hotspots-ranking-view?top=20"
curl -fsS "${SERVER_URL}/coupling-cohesion-metrics-suite"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
```

Readout:
- Heavy reverse pressure means too many callers are forcing the hotspot to serve incompatible needs.
- Heavy forward spread means the hotspot is acting as an unstable orchestrator or dependency magnet.
- The remedy differs: caller consolidation for pressure problems, dependency reduction for sink problems.

## 9) Parse-Frontier Probe

Use when:
- You want to reason carefully near low-coverage or partially parsed areas without over-trusting the graph.

Steps:

```bash
curl -fsS "${SERVER_URL}/ingestion-coverage-folder-report?depth=2"
curl -fsS "${SERVER_URL}/ingestion-diagnostics-coverage-report?section=summary"
curl -fsS "${SERVER_URL}/ingestion-diagnostics-coverage-report?section=ignored_files"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
```

Readout:
- Treat the graph as strong evidence inside well-covered zones.
- Treat it as partial evidence near parse frontiers.
- If the interesting corridor runs into ignored or low-coverage files, escalate to direct file reads there rather than pretending the graph is complete.

## 10) Ownership and Review Router

Use when:
- You need to decide who should review or own a change based on graph position rather than file names alone.

Steps:

```bash
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=4000"
```

Readout:
- Reverse callers often reveal product-facing or API-facing owners.
- Forward callees often reveal infra, storage, or platform reviewers.
- Semantic clusters help separate local ownership from cross-cutting reviewers.

## 11) Source-to-Sink Convergence Trace

Use when:
- You know a likely source entity and a likely sink entity and want to test whether they really belong to the same corridor.

Steps:

```bash
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=SOURCE_NAME"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=SOURCE_ENTITY"
curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=SINK_NAME"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=SINK_ENTITY"
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=SOURCE_ENTITY&tokens=8000"
```

Readout:
- If the source-side forward graph and sink-side reverse graph overlap in the same middle entities or clusters, the corridor hypothesis is strong.
- If they do not meet, either the source or sink guess is wrong, or the missing segment lives in dynamic or low-coverage code.

## 12) Sink-to-Source Accountability Trace

Use when:
- You start from a side effect such as persistence, publishing, or logging and need the upstream initiators and review surface.

Steps:

```bash
curl -fsS "${SERVER_URL}/code-entity-detail-view?key=SINK_ENTITY"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=SINK_ENTITY"
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=SINK_ENTITY&hops=3"
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=SINK_ENTITY&tokens=8000"
```

Readout:
- Reverse callers identify who can trigger the side effect.
- Blast radius distinguishes one local write path from a shared cross-cutting sink.
- Cluster spread helps route the change or investigation to the right owners.

## 13) Orchestrator Split Planner

Use when:
- One node appears to coordinate too many scenarios and you want to split it along clean caller-side or callee-side seams.

Steps:

```bash
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=ENTITY_KEY"
curl -fsS "${SERVER_URL}/complexity-hotspots-ranking-view?top=20"
curl -fsS "${SERVER_URL}/semantic-cluster-grouping-list"
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=ENTITY_KEY&tokens=8000"
```

Readout:
- If callers naturally separate into a few clusters, split by upstream scenario.
- If callees separate into a few domains, split by downstream responsibility.
- If both sides are chaotic, do not split yet; first stabilize the boundary or introduce a narrower waist.

## Selection Heuristic

Choose the workflow by the user’s real question:

- “Is X really causing Y?” → Meet-in-the-middle hypothesis test
- “Why does this local break feel systemic?” → Symptom-to-system corridor trace
- “How do I change this safely in phases?” → Change choreography
- “Where should I extract an interface?” → Narrow-waist seam discovery
- “Why do these modules feel too entangled?” → Boundary-leak detector
- “Where do I cut the cycle?” → Cycle-breaker scout
- “Can I delete this?” → Deletion-safety classifier
- “Why is this hotspot miserable?” → Hotspot pressure-versus-sink split
- “How much should I trust the graph here?” → Parse-frontier probe
- “Who should review this?” → Ownership and review router
- “Does this source really feed that sink?” → Source-to-sink convergence trace
- “Who can cause this side effect?” → Sink-to-source accountability trace
- “How should I split this orchestrator safely?” → Orchestrator split planner
