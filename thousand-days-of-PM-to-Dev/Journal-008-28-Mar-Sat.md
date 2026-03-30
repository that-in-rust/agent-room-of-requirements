# 28 Mar 2026 Saturday

## Joy session

```

- do not interrupt the LLM on what it is good at, they are testing the baseline and trying to improve it
- technology wise skills
- instruction depends on how you believe that skill to be, FE philosophy can be homogenuous


He asked us to delete code for several reasons:
- Counter sunk cost fallacy
- Prefer process over outcomes
- Detach developers' identity from code
- Force you to rethink different approaches to the same problem statement



```


# Apache Iggy exploration

```

- Consumption patterns should be random and interspersed and natural rather than being very, very forced
- Learn QUIC protocol only in adjacency of Apache Iggy this way you will cover more ground around Apache Iggy
- I am feeling angrythat why I could not have thought through this
-


### How Iggy Persists Data: Not a Database, Not JSON

**Summary:**  
Iggy is *not* a database. It is a persistent, append-only message log (similar to Kafka). Data is stored as raw, little-endian binary files on disk—no JSON, no SQL, no B-trees involved.

| Question           | Answer                                                     |
|--------------------|------------------------------------------------------------|
| Is it a database?  | **No** — It’s a message log                                |
| Is it JSON?        | **No** — Raw binary (little-endian)                        |
| Is it in RAM?      | **Both** — Fresh writes are in RAM, then flushed to disk   |
| What file format?  | Custom binary: `.log` files + `.index` files               |



```

## Questions to explore from apache iggy


```

- Iggy supports QUIC what does it mean?
- What is the difference between different protocols supported by Iggy like QUIC TCP WebSocket HTTP?




```




# Parseltongue Ideation 01

```
For the bi-directional aspect, the most valuable workflows let users explore both downstream effects (blast radius, dependents) and upstream causes (root cause, dependencies) within the same session, rather
than having one direction be trivially answerable without a graph or requiring data the system doesn't have.

Now I'm sketching out the concrete HTTP API endpoints: search for ranked candidates, resolve entities to their boundaries, fetch ego networks within token budgets, retrieve full context packets, compute
forward impact and reverse dependency chains, and identify hotspots—each serving a specific part of the navigation journey.

I'm also adding endpoints for cycle detection, community detection via Leiden, dead code identification, and cross-module coupling analysis to round out the structural insights.

But stepping back, I need to think about what LLMs actually require from this API: compact JSON responses with entity IDs for chaining queries, human-readable summaries paired with machine-parseable data,
token counts upfront so they can budget their context, and navigation hints suggesting what to query next.

Now I'm ready to write this out thoroughly but without unnecessary bloat, and I need to nail down the build order—what ships first to deliver real user value.

For the rollout, v1 needs to work end-to-end from search through anchoring, clustering, and deep dives, with basic call graph traversal and blast radius calculation. v1.1 adds hotspots, dead code, cycles, and
community detection for a full architecture overview. v1.2 brings simulation capabilities—mutating code and diffing the impact to identify safe change boundaries and extraction candidates. Everything else
can wait.

⏺ ---
Principal Architect Review: Parseltongue Bi-Directional Workflow Analysis

---
1. Premise Check

What this system actually is, in blunt terms:

A macOS desktop app that indexes a local codebase into SQLite, builds an in-memory graph in Python (igraph/NetworKit), and exposes a localhost HTTP API that returns small, structured JSON packets. LLMs and
humans query it. No cloud. No GPU. No embeddings. No compiler in the loop (tree-sitter only for most languages).

Most important implications of this stack:

1. Process boundary is real. Tauri is Rust. Graph compute is Python. Every query-time graph operation crosses an IPC boundary. This means: precompute aggressively, keep the Python process warm as a sidecar,
never invoke Python per-request as a cold subprocess. Latency budget for query-time graph ops is ~50-200ms, not seconds.
2. Edge quality is the ceiling. Tree-sitter gives you AST structure, not semantic resolution. Edges are symbolic name-based, not type-resolved. Dynamic dispatch, trait resolution, generic monomorphization —
all invisible. Every workflow's quality is capped by edge extraction quality. This is not a weakness to apologize for — it is the defining constraint.
3. The graph is a snapshot, not a live mirror. The user indexes, then queries. Between indexes, the graph is stale. File watching can help, but the fundamental model is snapshot-based. Workflows that assume
continuous freshness will lie.
4. LLM consumption is the primary interface, not human eyeballs. The HTTP API must return packets that an LLM can parse in <500 tokens to decide, <5000 tokens for a deep dive. If a response requires a human
to visually scan a graph, it has failed.
5. Python libraries are trusted for correctness, but integration is where bugs live. igraph's PageRank is correct. Your node ID remapping from SQLite integer keys to igraph vertex indices is where you'll ship
bugs. The risk surface is data shaping, not algorithm implementation.

Two constraints that shape product truth:

- Constraint 1: No type resolution across files. Without a compiler, "who calls process()" can match the wrong process() in a different module. This limits multi-hop traversals to ~2-3 hops before noise
overwhelms signal. (Direct consequence of tree-sitter-only.)
- Constraint 2: Precomputation latency vs freshness tradeoff. Betweenness centrality on 50K nodes takes seconds. Leiden community detection takes seconds. You cannot run these per-query. But if they're stale
by 1 commit, the hotspot ranking is wrong. The product must be honest about freshness timestamps on every cached metric.

---
2. Hard Thesis

1. This product is a structural navigation engine, not a code intelligence platform. It knows shapes and connections. It does not know types, semantics, or intent. Every workflow should stay within what
structural graph traversal can actually prove.
2. The core value loop is: search → converge → contextualize. Not "analyze everything." Not "find all bugs." The product reduces a vague question to a precise subgraph, then packs that subgraph into tokens.
That is the job.
3. Bi-directionality is not a feature — it is the graph's native advantage over grep. Grep can search forward. Only a graph can answer "who depends on this?" and "what is this reachable from?" in the same
data structure. If a workflow doesn't exploit both directions, it doesn't justify the graph.
4. The strongest moat is not algorithms — it is the progressive disclosure loop. Leiden, PageRank, PPR are commodities. What is not a commodity: a deterministic, token-budgeted, graph-guided narrowing from
50K entities to 5 entities in 3 hops. That workflow is hard to replicate by dumping files into a 1M context window.
5. Precomputation is the product. The user waits during indexing, not during querying. Every metric that can be precomputed must be. Query-time graph operations must be BFS/PPR-class (milliseconds), never
Betweenness-class (seconds).
6. This product should refuse to optimize for: real-time type-checked refactoring (use an IDE), security vulnerability scanning (needs taint analysis the stack can't do), code generation (not the job), and
anything that requires runtime profiling data.
7. The honest positioning is: "We know your codebase's shape. We don't know its meaning." Shape is enough for navigation, impact analysis, and architecture review. Meaning is the LLM's job. The separation of
labor is: graph computes structure, LLM interprets consequence.
8. The biggest risk is not missing features — it is shipping confident answers from bad edges. A wrong blast radius is worse than no blast radius. The product must surface confidence signals (edge resolution
rate, unresolved references, snapshot age) alongside every answer.

---
3. Workflow Universe

(editor: turn Word Wrap off here so box-drawing lines stay one line wide)

┌─────┬────────────────────┬─────────────────────────┬──────────────────────┬─────────┬────────────┬────────────────────────────────────┬────────────────────┬───────────────────┬─────────────────────┐
│  #  │      Workflow      │    Forward Question     │   Reverse Question   │ Primary │  Journey   │   Required Algorithms/Primitives   │  Precomputed or    │   Product Value   │      Judgment       │
│     │                    │                         │                      │  Actor  │  Stage(s)  │                                    │     Query-Time     │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│ 1   │ Call graph         │ What does X call?       │ Who calls X?         │ LLM,    │ DEEP DIVE  │ BFS on call edges                  │ Query-time         │ Navigation        │ Must have           │
│     │ forward/reverse    │                         │                      │ Human   │            │                                    │                    │ foundation        │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Public boundary    │ Which public API        │ What internals are   │         │            │ BFS reverse on call+contains edges │                    │                   │                     │
│ 2   │ resolution         │ exposes this private    │ beneath this public  │ LLM     │ ANCHOR     │  with visibility filter            │ Query-time         │ Core journey step │ Must have           │
│     │                    │ helper?                 │ API?                 │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │                    │ What breaks if I change │ What upstream change │ LLM,    │            │ BFS forward (hops), In-degree for  │ Query-time BFS +   │                   │                     │
│ 3   │ Blast radius       │  X?                     │  could explain this  │ Human   │ POST-DIVE  │ severity ranking                   │ precomputed degree │ Impact planning   │ Must have           │
│     │                    │                         │ breakage?            │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│ 4   │ Dependency chain   │ What does X             │ What transitively    │ LLM     │ DEEP DIVE, │ BFS/DFS forward/reverse on         │ Query-time         │ Onboarding,       │ Must have           │
│     │                    │ transitively depend on? │ depends on X?        │         │  POST-DIVE │ dependency edges                   │                    │ understanding     │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│ 5   │ Ego network        │ What is the immediate   │ What entity has X in │ LLM     │ CLUSTER    │ PPR from seed X, ego network       │ Query-time         │ Core journey step │ Must have           │
│     │ context            │ neighborhood of X?      │  its neighborhood?   │         │            │ extraction, token budget packing   │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │                    │ What are the most       │ What is connected to │ Human,  │            │ PageRank + In-degree + k-core      │                    │ Architecture      │                     │
│ 6   │ Hotspot ranking    │ critical/coupled        │  this hotspot?       │ LLM     │ POST-DIVE  │ composite                          │ Precomputed        │ review            │ Strong              │
│     │                    │ entities?               │                      │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │                    │ What has zero incoming  │                      │         │            │                                    │ Precomputed (dead  │                   │                     │
│ 7   │ Dead code          │ call edges from public  │ What would become    │ Human   │ POST-DIVE  │ In-degree = 0 filter + BFS         │ set) + query-time  │ Cleanup, tech     │ Strong              │
│     │ detection          │ entry points?           │ dead if I removed X? │         │            │ reachability from public roots     │ (removal           │ debt              │                     │
│     │                    │                         │                      │         │            │                                    │ simulation)        │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │                    │ Is X part of a circular │ What are all the     │ Human,  │            │ SCC (igraph                        │                    │ Architecture      │                     │
│ 8   │ Cycle membership   │  dependency?            │ members of X's       │ LLM     │ POST-DIVE  │ strongly_connected_components)     │ Precomputed        │ health            │ Strong              │
│     │                    │                         │ cycle?               │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│ 9   │ Community/module   │ What natural cluster    │ What entities define │ LLM     │ CLUSTER,   │ Leiden                             │ Precomputed        │ Architecture map  │ Strong              │
│     │ boundary           │ does X belong to?       │  this cluster?       │         │ POST-DIVE  │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Cross-module       │ How tightly are modules │ What are the         │         │            │ Cross-community edge count +       │ Precomputed count  │ Refactoring       │                     │
│ 10  │ coupling           │  A and B coupled?       │ specific coupling    │ Human   │ POST-DIVE  │ enumeration                        │ + query-time edges │ planning          │ Strong              │
│     │                    │                         │ edges?               │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │                    │ This entity is broken — │ If X has a bug, what │         │            │ Reverse BFS + PageRank-weighted    │ Query-time BFS +   │                   │                     │
│ 11  │ Root cause trace   │  trace backward to      │  downstream entities │ LLM     │ POST-DIVE  │ path ranking                       │ precomputed PR     │ Debugging         │ Strong              │
│     │                    │ likely root             │  are affected?       │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │                    │                         │ What internal        │         │            │                                    │                    │                   │                     │
│ 12  │ Interface surface  │ What is the public      │ implementation       │ LLM     │ ANCHOR,    │ Visibility filter + contains edges │ Query-time         │ Onboarding        │ Strong              │
│     │ map                │ surface of module M?    │ supports this        │         │ DEEP DIVE  │  + BFS inward                      │                    │                   │                     │
│     │                    │                         │ surface?             │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Change impact on   │ Which test files are    │ What code path could │         │            │ BFS forward to test-tagged         │                    │                   │                     │
│ 13  │ tests              │ reachable from changed  │  have caused this    │ LLM, CI │ POST-DIVE  │ entities / reverse BFS from test   │ Query-time         │ CI integration    │ Strong              │
│     │                    │ entity X?               │ test failure?        │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Extraction         │ Is module M loosely     │ What would break if  │         │            │ Leiden boundary + cross-boundary   │ Precomputed        │ Architecture      │                     │
│ 14  │ candidate scoring  │ coupled enough to       │ I extracted M?       │ Human   │ POST-DIVE  │ edge ratio + blast radius          │ community +        │ planning          │ Strong              │
│     │                    │ extract?                │                      │         │            │                                    │ query-time blast   │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Bridge/chokepoint  │ What entities are       │ What alternative     │         │            │                                    │                    │ Architecture      │                     │
│ 15  │ detection          │ bridges between         │ paths exist around   │ Human   │ POST-DIVE  │ Betweenness centrality             │ Precomputed        │ review            │ Strong              │
│     │                    │ subsystems?             │ this bridge?         │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│ 16  │ Core/periphery     │ What is the dense       │ What entities are    │ Human   │ POST-DIVE  │ k-core decomposition               │ Precomputed        │ Architecture      │ Strong              │
│     │ layering           │ architectural core?     │ peripheral?          │         │            │                                    │                    │ review            │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Trait/interface    │ Which impls satisfy     │ Which traits does    │         │            │ Edge-type filter on implements     │                    │                   │ Strong (limited by  │
│ 17  │ dispatch           │ this trait?             │ this type implement? │ LLM     │ DEEP DIVE  │ edges                              │ Query-time         │ Navigation        │ tree-sitter edge    │
│     │                    │                         │                      │         │            │                                    │                    │                   │ quality)            │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Safe change        │ What is the minimal     │ What is the maximal  │         │            │ Subgraph extraction with boundary  │                    │                   │                     │
│ 18  │ boundary           │ change set that doesn't │ safe set within B?   │ LLM     │ POST-DIVE  │ constraint + blast radius          │ Query-time         │ Change planning   │ Strong              │
│     │                    │  leak past boundary B?  │                      │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│ 19  │ Import/dependency  │ What does this file     │ Who imports this     │ LLM     │ DEEP DIVE  │ Edge-type filter on import edges   │ Query-time         │ Table stakes      │ Must have (but      │
│     │ listing            │ import?                 │ file?                │         │            │                                    │                    │ navigation        │ table stakes)       │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│ 20  │ Containment        │ What module contains X? │ What does module M   │ LLM     │ ANCHOR     │ Contains edges, trivial lookup     │ Query-time         │ Table stakes      │ Must have (but      │
│     │ hierarchy          │                         │ contain?             │         │            │                                    │                    │                   │ table stakes)       │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Architecture       │ If I add/remove this    │ What mutation would  │         │            │ Shadow graph clone +               │ Query-time         │ Differentiation   │                     │
│ 21  │ simulation         │ edge, what structural   │ fix this structural  │ Human   │ POST-DIVE  │ BFS/SCC/community diff             │ (expensive)        │ play              │ Strong (but v1.2+)  │
│     │                    │ changes result?         │ problem?             │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │                    │ Where can values of     │ Where did this value │         │            │                                    │                    │                   │ Weak (tree-sitter   │
│ 22  │ Type flow tracing  │ type T flow?            │  originate?          │ LLM     │ DEEP DIVE  │ DDG edges (data-flow)              │ Query-time         │ Understanding     │ can't reliably      │
│     │                    │                         │                      │         │            │                                    │                    │                   │ extract this)       │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Temporal           │ How has X's             │ What was X connected │         │            │ Snapshot diff (requires            │                    │ Long-term         │ Weak (v1.2+ at      │
│ 23  │ architecture drift │ connectivity changed    │  to N commits ago?   │ Human   │ POST-DIVE  │ dual-snapshot storage)             │ Precomputed diff   │ tracking          │ earliest)           │
│     │                    │ since last snapshot?    │                      │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Similar entity     │ What entities have      │ Why are X and Y      │         │            │ Graph kernel or structural         │                    │ Research-grade,   │                     │
│ 24  │ discovery          │ similar graph structure │ structurally         │ Human   │ POST-DIVE  │ similarity                         │ Precomputed        │ low repeat use    │ Kill                │
│     │                    │  to X?                  │ similar?             │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Semantic module    │ What should this        │ What entities define │         │            │ Leiden + entity name frequency     │ Precomputed +      │ Nice-to-have      │                     │
│ 25  │ naming             │ cluster be called?      │  the semantics of    │ Human   │ POST-DIVE  │ analysis                           │ heuristic          │ naming            │ Weak                │
│     │                    │                         │ this name?           │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ God function       │ What functions have too │ What clean split     │         │            │ Out-degree + community             │ Precomputed degree │ Refactoring       │ Weak                │
│ 26  │ decomposition      │  many outgoing edges?   │ would reduce         │ Human   │ POST-DIVE  │ sub-partitioning                   │  + query-time      │ suggestion        │ (opinion-heavy, low │
│     │                    │                         │ fan-out?             │         │            │                                    │                    │                   │  confidence)        │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │                    │ What entities are       │ What is the nearest  │         │            │ Degree = 0 filter +                │                    │ Usually indicates │                     │
│ 27  │ Orphan detection   │ disconnected from the   │ reachable entity     │ Human   │ POST-DIVE  │ nearest-connected BFS              │ Precomputed        │  bad extraction   │ Weak                │
│     │                    │ main graph?             │ from this orphan?    │         │            │                                    │                    │                   │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Dependency depth   │ What is the longest     │ What is on the       │         │            │ Longest path in DAG (topological   │                    │ Moderate          │                     │
│ 28  │ ranking            │ dependency chain?       │ critical path?       │ Human   │ POST-DIVE  │ sort)                              │ Precomputed        │ architecture      │ Weak                │
│     │                    │                         │                      │         │            │                                    │                    │ insight           │                     │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│     │ Multi-language     │ Where do Rust and       │ What TypeScript      │         │            │                                    │                    │                   │ Strong (if edge     │
│ 29  │ boundary           │ TypeScript interact?    │ depends on this Rust │ LLM     │ DEEP DIVE  │ Cross-language edge filtering      │ Query-time         │ Polyglot value    │ extraction supports │
│     │                    │                         │  function?           │         │            │                                    │                    │                   │  it)                │
├─────┼────────────────────┼─────────────────────────┼──────────────────────┼─────────┼────────────┼────────────────────────────────────┼────────────────────┼───────────────────┼─────────────────────┤
│ 30  │ Fan-in / fan-out   │ What are the highest    │ What are the highest │ Human   │ POST-DIVE  │ In-degree / Out-degree sorted      │ Precomputed        │ Quick             │ Must have (cheap,   │
│     │ heatmap            │ fan-in entities?        │  fan-out entities?   │         │            │                                    │                    │ architecture read │ high signal)        │
└─────┴────────────────────┴─────────────────────────┴──────────────────────┴─────────┴────────────┴────────────────────────────────────┴────────────────────┴───────────────────┴─────────────────────┘

---
4. Kill List

1. Similar Entity Discovery (#24)

Sounds clever: "find structurally similar functions." In practice, structural similarity without semantic understanding produces noise. Two functions with identical fan-out patterns but completely different
purposes will match. No user will trust this more than once. Graph kernels (WL, etc.) are research tools, not product features. The compute cost is high, the signal is low, and the repeat usage is zero.

2. God Function Decomposition (#26)

"What clean split would reduce fan-out?" — the system has no idea what a clean split is. It can count edges. It cannot reason about responsibilities. Suggesting decomposition from out-degree alone will
produce wrong answers (a well-designed orchestrator has high fan-out by design). This is opinion territory dressed as analysis. Ship the raw metric (fan-out ranking); do not ship the suggestion.

3. Semantic Module Naming (#25)

"What should this cluster be called?" is an LLM job, not a graph job. The graph can identify the cluster. Naming it from entity name frequency is cute in demos and wrong in production (the most common token
in a cluster is often impl or new or test). Let the LLM name things. The graph's job is grouping, not labeling.

4. Orphan Detection (#27)

Disconnected entities usually mean your edge extraction is broken, not that the code is dead. Shipping "orphan detection" as a feature will train users to distrust the graph when the extraction misses edges.
Fix extraction quality instead. If you must expose it, expose it as a data quality diagnostic, not an analysis feature.

5. Dependency Depth Ranking (#28)

"What is the longest dependency chain?" sounds architectural but rarely drives action. The user can't do anything with "your deepest chain is 14 hops." Contrast with blast radius, which answers "if I change
X, these 7 things break." Depth is trivia. Impact is actionable. The topological sort is trivially correct, but the product value is trivially low.

6. Type Flow Tracing (#22) — partial kill

Tree-sitter cannot reliably extract data-flow edges. It can see variable assignments within a function, not across function boundaries. Shipping "data flow" as a feature when the underlying edges are
intra-function-only will disappoint anyone who tries to trace a value across a call chain. If you build this, scope it honestly as "intra-function data flow" and do not promise cross-function tracing.

---
5. Top 10 Workflows (Ranked)

1. Call Graph Forward/Reverse (#1)

Why users come back: Every debugging session, every code review, every "I need to understand this function" starts here. "What does it call?" and "Who calls it?" are the two questions developers ask 50x per
day.

Why the graph is necessary: Grep finds string matches. The graph knows actual call relationships with direction. process as a grep hit gives you 200 matches. process in the call graph gives you 3 callers and
5 callees, correctly.

Why this stack works: BFS on igraph adjacency is sub-millisecond. No precomputation needed. The call edge extraction from tree-sitter is the most reliable edge type (function calls are syntactically
unambiguous in most languages).

2. Public Boundary Resolution (#2)

Why users come back: LLMs search for implementation details and find private helpers. The user doesn't care about the helper — they care about the entry point. "You searched for validate_token — that's
exposed through login_handler" is worth the entire product.

Why the graph is necessary: No flat search can answer "walk callers upward until you hit a public function." This requires reverse traversal with a visibility predicate. The graph is the only data structure
that supports this.

Why this stack works: BFS reverse with a filter is trivial in igraph. The limiting factor is visibility extraction from tree-sitter (Rust pub is syntactically visible; Python/JS visibility is heuristic).
Honest confidence signals per language are needed.

3. Blast Radius (#3)

Why users come back: Before every change. Before every PR review. "If I touch this, what else is affected?" is the single most repeated architectural question in software engineering.

Why the graph is necessary: Blast radius is multi-hop forward reachability. Grep cannot compute it. File-level dependency lists undercount it. Only the graph can say "changing auth::validate affects 3 direct
callers, which affect 11 transitive dependents, 2 of which are in test files."

Why this stack works: BFS forward with hop limit. Sub-millisecond. In-degree precomputed as severity ranking within the blast set. Token budget can cap the response at exactly what the LLM can consume.

4. Ego Network Context Packing (#5)

Why users come back: This is the CLUSTER step — the moment the product proves it's smarter than grep. Instead of "here are 50 search results," the user gets "here is the 3000-token neighborhood of the entity
you care about, ranked by relevance to that entity."

Why the graph is necessary: PPR from a seed node produces a relevance-ranked neighborhood that a keyword search cannot replicate. The graph knows which neighbors matter most to X, not just which neighbors
contain similar text.

Why this stack works: igraph's personalized_pagerank() with a seed vector is fast and correct. Token budget packing is a second pass: sort PPR scores descending, pack entities into the budget greedily.

5. Hotspot Ranking (#6)

Why users come back: New developer onboarding, architecture review, tech debt triage. "What are the 10 most critical entities in this codebase?" is a question with high repeat value for team leads and LLM
agents doing codebase-level analysis.

Why the graph is necessary: A function that appears in many files (grep frequency) is not the same as a function that sits at the center of the dependency graph (PageRank). HashMap::new appears everywhere but
is not a hotspot. UserService::authenticate has moderate frequency but maximum centrality.

Why this stack works: Composite of precomputed PageRank + In-degree + k-core shell. All precomputed, all cached. The HTTP API serves this from SQLite in <10ms.

6. Dead Code Detection (#7)

Why users come back: Every quarter, someone asks "what can we delete?" This is the only tool that gives a graph-verified answer instead of a guess.

Why the graph is necessary: Dead code = unreachable from any public entry point. This is a reachability problem. Grep cannot solve it (a function that is referenced in a comment is not alive). The graph can
compute: run BFS from all public entry points, anything not visited is dead.

Why this stack works: Precompute the reachable set from tagged public entry points. Store the dead set. The query-time reverse ("what would become dead if I removed X?") is a BFS minus operation.

7. Cycle Membership (#8)

Why users come back: Circular dependencies are the #1 architecture smell that teams actively hunt. "Show me all cycles" is a common CI gate. "Is my entity in a cycle?" is a common question during refactoring.

Why the graph is necessary: Cycle detection requires SCC computation. Grep cannot find cycles. Even file-level dependency tools often miss transitive cycles.

Why this stack works: igraph clusters(mode="strong") is correct and fast. Precompute SCC membership per snapshot. Query-time lookup is O(1).

8. Community/Module Boundary (#9)

Why users come back: "What are the natural modules in this codebase?" is the starting question for architecture review. Leiden communities often reveal module structures that don't match folder structure —
that's the insight.

Why the graph is necessary: Folder structure is a human convention. The graph reveals actual coupling structure. When Leiden says "these 15 entities from 4 different folders form one community," that's a
finding you can't get from tree.

Why this stack works: igraph community_leiden() is the reference implementation. Precompute per snapshot. Store community assignments in SQLite. Serve as metadata on every entity response.

9. Root Cause Trace (#11)

Why users come back: "This test is failing. Why?" → trace backward through the call graph from the failing assertion, ranked by PageRank (most important upstream entities first). This is the reverse of blast
radius, and equally useful.

Why the graph is necessary: The reverse dependency chain IS the root cause candidate list. PageRank ranking within that chain prioritizes the most likely culprits (high-centrality entities that changed
recently).

Why this stack works: Reverse BFS is query-time. PageRank ranking is precomputed. Combine at serve time. If git recency is wired, it further sharpens the ranking.

10. Cross-Module Coupling Analysis (#10)

Why users come back: "Should we split this service?" starts with "how coupled are these two modules?" The coupling metric (cross-community edge count / total edge count) is a number that directly drives
architectural decisions.

Why the graph is necessary: Coupling is not "how many imports." It's "how many actual dependency edges cross this boundary, relative to the total edge budget." The graph computes this exactly.

Why this stack works: Precomputed Leiden boundaries + edge table query in Polars. The specific coupling edges are query-time (filter edge table by source community ≠ target community).

---
6. API Consequences

SEARCH

POST /search
Body: { "q": "authentication", "top_k": 10 }
Returns: ranked entity list (id, name, location, score, match_source)

One endpoint. RRF fuses all signals server-side. The client never sees individual retrieval channels. Return compact: entity ID, display name, file:line:line, RRF score, which signal contributed most. ~30-50
tokens per result. Cached: FTS5 index + symbol trie + trigram index are all prebuilt at index time.

ANCHOR

GET /anchor?entity={id}
Returns: resolved public boundary entity + path from query to boundary

One endpoint. Takes any entity, returns the public API boundary it belongs to. If the entity is already public, returns itself. Returns the traversal path (chain of callers) so the LLM understands how they're
connected. ~50-100 tokens. Never cached — this is a BFS per query, but it's sub-millisecond.

CLUSTER

GET /cluster?entity={id}&budget={tokens}
Returns: ego network under token budget, ranked by PPR

One endpoint. The budget parameter is critical — it forces the response to fit within what the LLM can consume. Returns entity summaries (name, kind, signature, location, PPR score), not full source code.
~200-500 tokens. Query-time PPR from seed, precomputed PageRank as global prior for tie-breaking.

DEEP DIVE

GET /deep-dive?entity={id}&depth={hops}&budget={tokens}
Returns: full context packet (source spans, callers, callees, type sigs, community, metrics)

One endpoint. This is the big payload — up to 5K-20K tokens. Source code is read from disk at serve time (not stored in DB). Includes callers, callees, implementations, containing module, community
membership, centrality scores, git recency. Hard call: source is read from disk, not DB. Graph context is from precomputed cache + query-time BFS.

GET /deep-dive/source?entity={id}
Returns: raw source span for the entity

Separate endpoint for source-only. Sometimes the LLM just wants the code, not the graph context.

POST-DIVE

These are separate endpoints, each with a clear single purpose:

GET /blast-radius?entity={id}&hops={n}
Returns: affected entities, ranked by severity (in-degree), grouped by hop distance

GET /upstream-trace?entity={id}&hops={n}
Returns: reverse dependency chain, ranked by PageRank

GET /hotspots?top={n}&metric={pagerank|degree|kcore|composite}
Returns: ranked entity list with metric scores

GET /dead-code?scope={all|module_id}
Returns: entities unreachable from public entry points

GET /cycles?entity={id}
Returns: SCC membership for entity, or all non-trivial SCCs if no entity

GET /communities
Returns: Leiden community assignments, modularity score, cross-boundary edge counts

GET /coupling?community_a={id}&community_b={id}
Returns: coupling metric + specific crossing edges

GET /core-periphery
Returns: k-core shell assignments for all entities

Hard calls:

- Blast radius and upstream trace are separate endpoints, not one parameterized endpoint. The mental models are different (forward impact vs reverse diagnosis).
- Hotspots, dead code, cycles, communities, core-periphery are all precomputed and cached. These endpoints read from SQLite, not from igraph.
- Coupling is mixed: community assignments are precomputed, specific edges are query-time filtered.
- No endpoint should return >100 entities without explicit pagination. Default limits everywhere.

META

GET /health
Returns: snapshot age, entity count, edge count, edge resolution rate, stale files count

GET /stats
Returns: per-language entity counts, edge type distribution, community count, SCC count

The /health endpoint is critical for trust. It must report snapshot age and edge resolution rate (what % of edges resolved to real entity PKs vs symbolic names). An LLM that knows the graph is 3 hours stale
can adjust its confidence.

---
7. Algorithm Accountability

┌─────────────────────┬──────────────────────┬──────────────────────────────┬───────────────────┬───────────────────────────┬────────────────────┬────────────────────────────────────────────────────────┐
│ Algorithm/Primitive │    Why It Exists     │  Workflows That Justify It   │   Compute Mode    │          Library          │   Expected Data    │                    Risk If Misused                     │
│                     │                      │                              │                   │                           │       Shape        │                                                        │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│                     │ Forward/reverse      │ #1 call graph, #2 anchor, #3 │                   │                           │ Directed edge      │ Low risk. Cap hop depth to prevent full-graph walks.   │
│ BFS                 │ graph traversal      │  blast radius, #4 dependency │ Query-time        │ python-igraph             │ list, integer      │ Max 4 hops for query-time.                             │
│                     │                      │  chain, #11 root cause       │                   │                           │ vertex IDs         │                                                        │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│                     │ Global importance    │ #5 ego network tie-breaking, │                   │                           │ Directed weighted  │ Must handle dangling nodes (no outgoing edges). Add    │
│ PageRank            │ ranking              │  #6 hotspots, #11 root cause │ Precomputed       │ python-igraph             │ adjacency          │ damping correction. Recompute per snapshot only.       │
│                     │                      │  ranking                     │                   │                           │                    │                                                        │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│ Personalized        │ Local relevance from │ #5 ego network, CLUSTER      │ Query-time (or    │                           │ Directed adjacency │ Seed vector must be single-node. Multi-seed PPR is     │
│ PageRank            │  a seed              │ packing                      │ cached per hot    │ python-igraph             │  + seed vector     │ ambiguous. Cache top-20 hot anchors.                   │
│                     │                      │                              │ anchor)           │                           │                    │                                                        │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│                     │ Fan-in signal,       │ #3 blast radius severity, #6 │                   │                           │ Edge table dst_id  │                                                        │
│ In-Degree           │ importance proxy     │  hotspots, #7 dead code      │ Precomputed       │ Polars grouped count      │ column             │ Trivially correct. Zero risk.                          │
│                     │                      │ (degree=0), #30 heatmap      │                   │                           │                    │                                                        │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│ Out-Degree          │ Fan-out signal,      │ #6 hotspots, #30 heatmap,    │ Precomputed       │ Polars grouped count      │ Edge table src_id  │ Trivially correct. Zero risk. High out-degree is not   │
│                     │ complexity proxy     │ god function detection       │                   │                           │ column             │ always bad (orchestrators).                            │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│                     │ Bridge/chokepoint    │ #15 bridge detection,        │                   │                           │ Undirected or      │ Expensive. O(VE) on large graphs. Must precompute,     │
│ Betweenness         │ detection            │ architecture review          │ Precomputed       │ NetworKit                 │ directed graph     │ never query-time. On 50K+ nodes, consider approximate  │
│                     │                      │                              │                   │                           │ object             │ betweenness (NetworKit ApproxBetweenness).             │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│ k-core              │ Core/periphery       │ #16 core-periphery, hotspot  │ Precomputed       │ NetworKit                 │ Graph object,      │ Low risk. Ensure the graph is undirected for k-core    │
│                     │ layering             │ composite                    │                   │                           │ unweighted         │ (or use directed variant explicitly).                  │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│                     │                      │ #9 module boundaries, #10    │                   │                           │ Weighted edge      │ Resolution parameter is critical. Default              │
│ Leiden              │ Community detection  │ coupling, #14 extraction     │ Precomputed       │ python-igraph             │ list, resolution   │ resolution=1.0 is rarely optimal for code graphs. Test │
│                     │                      │ scoring                      │                   │                           │ parameter          │  multiple resolutions, pick the one maximizing         │
│                     │                      │                              │                   │                           │                    │ modularity. Expose resolution as a config knob.        │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│                     │                      │                              │                   │                           │ Ranked lists per   │ k=60 is standard. Risk: if one signal is garbage       │
│ RRF                 │ Multi-signal search  │ SEARCH phase                 │ Query-time        │ Custom Python             │ signal:            │ (e.g., trigram on very short queries), it contaminates │
│                     │ fusion               │                              │                   │                           │ [(entity_id,       │  the fusion. Weight signals by query length heuristic. │
│                     │                      │                              │                   │                           │ rank)]             │                                                        │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│                     │ Exact/prefix symbol  │                              │ Precomputed       │                           │ Static string      │ Must rebuild on re-index. Stale trie after code change │
│ Symbol trie         │ lookup               │ SEARCH phase                 │ (built at index   │ marisa-trie or Rust fst   │ vocabulary →       │  is a silent correctness bug.                          │
│                     │                      │                              │ time)             │                           │ entity ID mapping  │                                                        │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│                     │                      │                              │ Precomputed       │                           │                    │                                                        │
│ Trigram retrieval   │ Fuzzy/partial name   │ SEARCH phase                 │ (index) +         │ RapidFuzz                 │ Symbol strings     │ Garbage on queries <3 characters. Gate: skip trigram   │
│                     │ matching             │                              │ query-time        │                           │                    │ signal for single-word queries shorter than 4 chars.   │
│                     │                      │                              │ (match)           │                           │                    │                                                        │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│ Ego network         │                      │                              │                   │ python-igraph             │ Directed adjacency │ Budget overflow risk: ego network at depth=2 can be    │
│ extraction          │ Neighborhood packing │ CLUSTER                      │ Query-time        │ (neighborhood + PPR)      │  + seed node       │ 500+ entities on hub nodes. Always enforce token       │
│                     │                      │                              │                   │                           │                    │ budget truncation.                                     │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│ Token budget        │ Constrain output     │                              │                   │                           │ Sorted entity list │ Must use actual word count (from DB), not estimated.   │
│ packing             │ size                 │ CLUSTER, DEEP DIVE           │ Query-time        │ Custom Python             │  + per-entity      │ Greedy packing by PPR score. Do not approximate.       │
│                     │                      │                              │                   │                           │ token cost         │                                                        │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│ DFS                 │ Deep path trace,     │ DEEP DIVE path drilling      │ Query-time        │ python-igraph             │ Directed adjacency │ Stack overflow risk on deep recursive graphs. Use      │
│                     │ reachability         │                              │                   │                           │                    │ iterative DFS with explicit stack. Cap depth.          │
├─────────────────────┼──────────────────────┼──────────────────────────────┼───────────────────┼───────────────────────────┼────────────────────┼────────────────────────────────────────────────────────┤
│ SCC (Tarjan)        │ Cycle detection      │ #8 cycle membership          │ Precomputed       │ python-igraph             │ Directed edge list │ Correct out of the box. Only risk: SCC of size 1 is    │
│                     │                      │                              │                   │ clusters(mode="strong")   │                    │ not a cycle — filter to size ≥ 2.                      │
└─────────────────────┴──────────────────────┴──────────────────────────────┴───────────────────┴───────────────────────────┴────────────────────┴────────────────────────────────────────────────────────┘

---
8. Moat Analysis

Table Stakes (anyone can build these)

┌─────────────────────────────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│            Workflow             │                                                             Why It's Table Stakes                                                              │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Call graph forward/reverse (#1) │ Every IDE, every code intelligence tool, every LSP server does this. The graph makes it more reliable for cross-file, but the UX is not novel. │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Import/dependency listing (#19) │ go mod graph, cargo tree, pydeps — commodity.                                                                                                  │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Containment hierarchy (#20)     │ File browser. Folder tree. Every editor has this.                                                                                              │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Fan-in / fan-out heatmap (#30)  │ A better wc -l for dependencies. Useful, not differentiating.                                                                                  │
└─────────────────────────────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

Strong Value (worth the product, not a moat)

┌──────────────────────────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│         Workflow         │                                                                Why It's Strong But Not A Moat                                                                │
├──────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Blast radius (#3)        │ Very useful. But GitHub Copilot will eventually compute this from context. The graph is better today; context windows are catching up.                       │
├──────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Dead code detection (#7) │ Useful, but tree-shaking tools, IDE warnings, and linters compete. The graph-verified version is better, but not uniquely so.                                │
├──────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Cycle membership (#8)    │ Useful, but cargo clippy, pylint circular import detection exist. Graph version is more complete, but the workflow is established.                           │
├──────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Hotspot ranking (#6)     │ Useful for leads, but code climate / CodeScene already do this with git churn. The graph version is structurally better but competes with established tools. │
├──────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Community detection (#9) │ Strong insight, but a Leiden partition on its own is "here are some clusters." The value comes from what you DO with the clusters.                           │
└──────────────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

Actual Moat Candidates

┌────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    Workflow                    │                                                                     Why It's A Moat                                                                      │
├────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Public boundary resolution (#2)                │ No other tool answers "what public API exposes this private implementation?" This requires reverse graph traversal with visibility predicates. IDEs can  │
│                                                │ "find usages" but cannot walk callers to the boundary. Grep certainly cannot.                                                                            │
├────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Ego network context packing (#5)               │ Token-budgeted, PPR-ranked neighborhood packing is not a feature any existing tool offers. It's the core of the progressive disclosure loop. Dumping     │
│                                                │ files into context windows is the competitor, and this is structurally better.                                                                           │
├────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Architecture simulation (#21)                  │ "What if I moved this module?" with exact structural consequences (new cycles, broken reachability, changed centrality) does not exist anywhere. It      │
│                                                │ requires a mutable shadow graph. This is the endgame moat.                                                                                               │
├────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Root cause trace with graph ranking (#11)      │ Reverse BFS + PageRank ranking produces a structurally-ranked "suspect list" for a bug. No other debugging tool uses graph centrality to rank root cause │
│                                                │  candidates.                                                                                                                                             │
├────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Cross-module coupling quantification (#10)     │ "Modules A and B have 14 crossing edges out of 200 total, coupling ratio 0.07" — this exact number does not come from any current tool. Code climate     │
│                                                │ gives heuristics. This gives graph truth.                                                                                                                │
├────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Progressive disclosure journey (SEARCH →       │ The entire journey is the moat. Each step narrows from 50K entities to 5, using graph structure at every step. No tool does this. Context window dumping │
│ ANCHOR → CLUSTER → DIVE)                       │  is the only alternative, and it scales worse.                                                                                                           │
└────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

Honest callout: Some "graph" workflows (blast radius, dead code, cycles) are really just better packaging of existing concepts. They are strong product features but not moats. The moat is in workflows that
require graph-guided progressive narrowing — things that fundamentally cannot be replicated by throwing more tokens at the problem.

---
9. Failure Modes

┌────────────────────┬─────────────────────────────────────────────────┬────────────────────────────────────────────────────┬─────────────────────────────────────────────────────────────────────────────┐
│    Failure Mode    │                 What Goes Wrong                 │                  How It Manifests                  │                                 Mitigation                                  │
├────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│                    │ User edits 5 files, queries without             │ Blast radius misses newly added call. Dead code    │ File watcher marks files as dirty. Every API response includes              │
│ Stale snapshot     │ re-indexing. Graph doesn't reflect current      │ includes a function that was just connected.       │ snapshot_age_seconds and stale_file_count. LLM/human can decide to re-index │
│                    │ code.                                           │ Anchor resolves to a deleted function.             │  or proceed with caveat.                                                    │
├────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│                    │ Tree-sitter extracts call("process") but can't  │ BFS traverses through a wrong connection. Blast    │ 2-pass ingestion with name resolution (same-file > same-dir > first-match > │
│ Unresolved edges   │ resolve which process. Edge points to wrong     │ radius includes unrelated code. Cycle detection    │  drop). Report edge_resolution_rate on /health. Warn on responses when      │
│                    │ entity or to a phantom node.                    │ finds phantom cycles.                              │ resolution is <80%.                                                         │
├────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Bad anchor         │ BFS upward from private function finds a test   │ "This private function is exposed via              │ Tag test files/functions during extraction. BFS anchor should skip          │
│ resolution         │ helper before the production API boundary.      │ test_auth_helper" — wrong and confusing.           │ test-tagged entities. Allow manual boundary tagging via config.             │
├────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Meaningless        │ Leiden on a sparse graph with poor edges        │ "These 30 entities from 12 folders are one         │ Compute modularity score. If modularity < 0.3, suppress community features  │
│ communities        │ produces random-looking communities that don't  │ community" — user loses trust.                     │ and fall back to folder-based grouping. Surface modularity in /communities  │
│                    │ match any human intuition about modules.        │                                                    │ response.                                                                   │
├────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Expensive          │ Betweenness centrality recomputed on every      │ 2-5 second latency on what should be <200ms        │ Strict rule: Betweenness, k-core, Leiden, PageRank, SCC are ONLY            │
│ analytics in hot   │ query. Leiden run per request.                  │ endpoints.                                         │ precomputed. Never query-time. Store in SQLite cached_metrics table. Serve  │
│ path               │                                                 │                                                    │ from cache.                                                                 │
├────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ LLM-unfriendly     │ Deep dive returns 500 entities with full source │ LLM context overflows. LLM hallucinates from noisy │ Enforce budget parameter on CLUSTER and DEEP DIVE. Default budget of 4000   │
│ payloads           │  code. Token budget ignored.                    │  context. User sees degraded LLM performance.      │ tokens. Hard cap at 20K. Return truncated: true if budget was hit.          │
├────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Hub node explosion │ Entity with 200 callers produces ego network of │ CLUSTER response is enormous. PPR is slow on dense │ Cap ego network to depth=1 for entities with degree > 50. Use PPR top-k     │
│                    │  2000 entities at depth 2.                      │  subgraph.                                         │ truncation (return top 20 neighbors by PPR score, not all neighbors).       │
├────────────────────┼─────────────────────────────────────────────────┼────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Node ID remapping  │ SQLite entity IDs don't match igraph vertex     │ PageRank score for entity 42 is actually the score │ Single source of truth for ID mapping. Build mapping table once at graph    │
│ bugs               │ indices after graph rebuild. Cached metrics     │  for entity 71. Silent data corruption.            │ construction. Validate: assert len(mapping) == igraph.vcount(). Store       │
│                    │ point to wrong entities.                        │                                                    │ mapping version in cache metadata. Invalidate all caches on re-index.       │
└────────────────────┴─────────────────────────────────────────────────┴────────────────────────────────────────────────────┴─────────────────────────────────────────────────────────────────────────────┘

---
10. Build Order

v1 — "The Journey Works"

User feels: "I searched, it showed me the right neighborhood, I got useful context."

┌────────────────────────────────────────────────────────────────────┬───────────────────────────────┐
│                             What ships                             │       Workflows enabled       │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┤
│ Tree-sitter entity + edge extraction (2-pass with name resolution) │ Foundation for everything     │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┤
│ SQLite schema: entities, edges, indexed_files, snapshots           │ Durable storage               │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┤
│ RRF search (FTS5 + symbol trie + trigram)                          │ SEARCH (#3 workflow)          │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┤
│ BFS anchor resolution with visibility filter                       │ ANCHOR (#2)                   │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┤
│ PPR ego network + token budget packing                             │ CLUSTER (#5)                  │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┤
│ Deep dive: source from disk + callers + callees + signatures       │ DEEP DIVE (#1, #4)            │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┤
│ Precomputed PageRank + In-degree + Out-degree                      │ Ranking signals for all above │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┤
│ Blast radius (forward BFS + degree-ranked)                         │ POST-DIVE (#3)                │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┤
│ File-level invalidation (SHA-256 hash comparison)                  │ Incremental re-index          │
├────────────────────────────────────────────────────────────────────┼───────────────────────────────┤
│ /health with snapshot age + edge resolution rate                   │ Trust signal                  │
└────────────────────────────────────────────────────────────────────┴───────────────────────────────┘

v1 endpoint count: 7 (/search, /anchor, /cluster, /deep-dive, /deep-dive/source, /blast-radius, /health)

v1.1 — "The Architecture View"

User feels: "I can see the architecture, find the problems, and understand the shape."

┌─────────────────────────────────────────────────────────────┬──────────────────────────────────┐
│                         What ships                          │        Workflows enabled         │
├─────────────────────────────────────────────────────────────┼──────────────────────────────────┤
│ Precomputed SCC (cycle detection)                           │ Cycle membership (#8)            │
├─────────────────────────────────────────────────────────────┼──────────────────────────────────┤
│ Precomputed Leiden communities + modularity score           │ Community/module boundaries (#9) │
├─────────────────────────────────────────────────────────────┼──────────────────────────────────┤
│ Precomputed k-core decomposition                            │ Core-periphery layering (#16)    │
├─────────────────────────────────────────────────────────────┼──────────────────────────────────┤
│ Upstream trace (reverse BFS + PageRank ranking)             │ Root cause trace (#11)           │
├─────────────────────────────────────────────────────────────┼──────────────────────────────────┤
│ Dead code detection (reachability from public entry points) │ Dead code (#7)                   │
├─────────────────────────────────────────────────────────────┼──────────────────────────────────┤
│ Hotspot composite metric (PR + degree + k-core)             │ Hotspot ranking (#6)             │
├─────────────────────────────────────────────────────────────┼──────────────────────────────────┤
│ Cross-module coupling metric                                │ Coupling analysis (#10)          │
└─────────────────────────────────────────────────────────────┴──────────────────────────────────┘

v1.1 adds: 6 endpoints (/upstream-trace, /cycles, /communities, /dead-code, /hotspots, /core-periphery, /coupling)

v1.2 — "The Planning Tool"

User feels: "I can plan changes, evaluate extraction candidates, and simulate mutations."

┌────────────────────────────────────────────────────────────────────┬────────────────────────────┐
│                             What ships                             │     Workflows enabled      │
├────────────────────────────────────────────────────────────────────┼────────────────────────────┤
│ Precomputed Betweenness centrality (approximate for large graphs)  │ Bridge detection (#15)     │
├────────────────────────────────────────────────────────────────────┼────────────────────────────┤
│ Change impact on tests (BFS to test-tagged entities)               │ Test impact (#13)          │
├────────────────────────────────────────────────────────────────────┼────────────────────────────┤
│ Extraction candidate scoring (community boundary + coupling ratio) │ Extraction scoring (#14)   │
├────────────────────────────────────────────────────────────────────┼────────────────────────────┤
│ Safe change boundary computation                                   │ Safe change planning (#18) │
├────────────────────────────────────────────────────────────────────┼────────────────────────────┤
│ Interface surface map (visibility filter + contains)               │ Interface surface (#12)    │
├────────────────────────────────────────────────────────────────────┼────────────────────────────┤
│ Architecture simulation (shadow graph clone, mutate, diff)         │ Simulation (#21)           │
└────────────────────────────────────────────────────────────────────┴────────────────────────────┘

v1.2 adds: 4 endpoints (/bridge-points, /test-impact, /extraction-candidates, /simulate)

Later

┌──────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────────────────────┐
│                  What ships                  │                                       Why later                                        │
├──────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────┤
│ Temporal snapshot comparison                 │ Requires dual-snapshot storage, low repeat usage until the product has traction        │
├──────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────┤
│ Multi-language boundary detection            │ Requires cross-language edge extraction quality that tree-sitter alone can't guarantee │
├──────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────┤
│ Spectral clustering, Infomap, Walktrap       │ P2 algorithms with diminishing returns over Leiden                                     │
├──────────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────────────┤
│ Closeness, Harmonic, Eigenvector, Katz, HITS │ P2 centrality variants — PageRank + Betweenness cover 90% of use cases                 │
└──────────────────────────────────────────────┴────────────────────────────────────────────────────────────────────────────────────────┘

---
11. Final Verdict

The single best workflow category: Forward/reverse navigation with progressive disclosure (SEARCH → ANCHOR → CLUSTER → DIVE). This is the daily-use loop. Every other workflow is built on top of this.

The most overrated workflow category: Advanced centrality variants (Closeness, Harmonic, Eigenvector, Katz, HITS). They all answer slightly different flavors of "how important is this node" and PageRank +
Betweenness already cover the product-relevant cases. The remaining variants are academic distinctions that no user will ever ask for by name.

The best moat workflow: Public boundary resolution (anchor detection). It is the single workflow that most clearly demonstrates why the graph exists and that cannot be replicated by dumping files into
context. It transforms a search hit into an architectural understanding in one step.

The best workflow for LLM consumption: Ego network context packing under token budget. It gives the LLM exactly the right amount of context, ranked by graph-computed relevance, fitting within a specified
token constraint. This is what makes graph-guided context fundamentally better than "here are the top 10 files that matched your query."

The one-sentence product thesis:

Parseltongue is a local-first structural navigation engine that uses graph traversal to progressively narrow 50,000 entities to the 5 that matter, delivering deterministic, token-budgeted context packets that
no context-window dump can replicate.

```

## Parseltongue Ideation 02

``` text

⏺ ---
  Parseltongue: Code Reading Companion — Product Design

  ---
  1. Premise Check

  What this product actually is, in practical terms:

  A macOS desktop app where a developer drags in a Rust project folder, waits
  5-30 seconds for indexing, and then has a persistent local environment for
  reading, browsing, and learning that codebase. The app shows visual maps,
  source code with graph annotations, and an embedded LLM that acts as a reading
   guide — not a chatbot. Behind the scenes: SQLite stores entities and edges,
  Python computes graph metrics, and a local HTTP API serves structured packets
  to both the Tauri frontend and the LLM.

  Most important implications for human code reading:

  1. The app is the reading surface, not a terminal. (Direct.) Tauri gives us a
  native window with WebView. This means: side-by-side panels, clickable graph
  nodes, hover cards, breadcrumbs, visual navigation. The reading experience is
  a GUI, not curl commands. This is the fundamental shift from the LLM-query
  framing.
  2. The graph provides reading structure that file trees cannot. (Direct.) A
  file tree says "here are 400 files in 30 folders." The graph says "here are 12
   communities with 3 that matter for authentication." For a newcomer, the graph
   replaces folder-browsing with concept-browsing.
  3. Source code is read from disk, not stored in DB. (Direct from v180
  architecture.) Entities store location pointers (file:line:line). Source is
  read on demand. This means the reading surface can always show current source
  even if the graph snapshot is slightly stale — with a visual indicator when
  they diverge.
  4. The LLM is a reading companion, not the primary interface. (Inference.) The
   human reads code. The LLM explains what they're looking at, suggests what to
  read next, and answers questions about what they just read. The LLM should
  never be the bottleneck for browsing. Visual navigation must work without the
  LLM.
  5. Latency budget is ~100ms for navigation, ~2s for LLM responses.
  (Inference.) Clicking a function in the map and seeing its source + callers +
  callees must be instant. Asking "explain this module" can take 2 seconds
  because the human expects to wait for a thoughtful answer.

  Biggest constraint shaping the UX:

  Edge quality caps explanation depth. Tree-sitter knows that foo() calls bar()
  but not which bar() when there are multiple. This means: the product must be
  honest about its limits. Show "3 possible targets" instead of confidently
  picking one. The reading companion earns trust by showing uncertainty, not by
  hiding it. Every visual and every LLM explanation should be grounded in what
  the graph actually knows — nothing more.

  ---
  2. Product Thesis

  1. Parseltongue should become a reading environment, not a query tool. The
  mental model is "I'm spending 2 hours reading this codebase" — not "I have a
  question, give me an answer." The app should feel like an instrumented book,
  not a search engine.
  2. The core experience is: land somewhere, understand the neighborhood, decide
   where to go next. Every interaction is a micro-loop of orientation →
  comprehension → navigation. The graph provides orientation ("you are here,
  these are nearby"). The source pane provides comprehension. The LLM provides
  explanation. Navigation links provide the next step.
  3. The graph's job is to replace folder-browsing with concept-browsing. A
  newcomer to Iggy shouldn't start with src/ and click through 30 folders. They
  should start with a map that says "there are 4 major subsystems: streaming,
  server, client, storage" and click into one.
  4. The LLM should behave like a senior engineer walking you through code — not
   like a chatbot. It should say "Read this function first. Notice the where
  clause — that constrains which types can be used here. When you're ready, I'll
   show you the three implementations." It should not say "Here is a 500-word
  summary of the module."
  5. Progressive disclosure is spatial, not conversational. The user zooms in
  visually (workspace → module → function → control flow), not by asking
  increasingly specific questions. The conversation is a companion to the zoom,
  not the zoom mechanism itself.
  6. Reading history is a first-class feature. A newcomer reads the same
  codebase over multiple sessions. "Where was I?" and "What have I read?" and
  "What's left?" are essential questions. The app should track reading state
  like a book reader tracks pages.
  7. The product should not become: a full IDE (no editing), a CI tool, a code
  review tool, a refactoring assistant, or a "vibe coding" tool. It is for
  reading and understanding. That's the job.
  8. The difference between "code search tool" and "code reading companion": A
  search tool answers questions. A reading companion helps you form questions.
  It shows you things you didn't know to ask about. It says "you've read the
  Consumer trait but not the ConsumerGroup that coordinates them — that's
  probably why the ownership model seems confusing."

  ---
  3. Reading Modes

  Mode 1: Architecture Overview

  Problem it solves: "I just cloned this repo. What is it?"
  Who it's for: Day-1 newcomers.
  Why it's useful: Replaces 30 minutes of folder-clicking with a 10-second
  visual orientation.
  What the user sees: A workspace-level map showing 8-15 Leiden communities as
  labeled clusters, sized by entity count, colored by language density, with
  inter-cluster edges showing coupling strength. Each cluster has a 2-3 word
  label derived from its most central entity names. Click any cluster to zoom
  in.

  Mode 2: Module Deep Read

  Problem it solves: "I need to understand how the streaming module works."
  Who it's for: Developers assigned to a specific area.
  Why it's useful: Provides a structured reading order within a module instead
  of alphabetical file listing.
  What the user sees: Left panel: module entity list sorted by PageRank (most
  important first). Center: source code pane with inline annotations showing
  callers/callees as clickable chips. Right panel: mini-map showing the module's
   internal graph with the currently-read entity highlighted.

  Mode 3: Call Chain Explorer

  Problem it solves: "I see process_message() is called but I don't know what
  happens step by step."
  Who it's for: Anyone tracing execution flow.
  Why it's useful: Visualizes the call sequence as a vertical chain, not just
  caller/callee lists.
  What the user sees: A vertical lane showing the call chain from entry point
  down to leaf. Each node is a card with function signature, file location, and
  1-line summary. Click any card to see source. Branching calls shown as
  parallel lanes. Depth limited to 5 hops by default. User can expand or
  collapse levels.

  Mode 4: Trait/Impl Browser

  Problem it solves: "I see impl MessageHandler for Consumer — what other types
  implement MessageHandler? What methods does it require?"
  Who it's for: Rust newcomers confused by trait dispatch and polymorphism.
  Why it's useful: Makes the abstract (trait definitions) and concrete (impls)
  visible as a connected pair.
  What the user sees: Split view. Left: trait definition with required methods,
  associated types, and supertraits. Right: scrollable list of all implementing
  types, each expandable to show their impl block source. Edges connect trait
  methods to their impl counterparts. Color-coded by whether the impl is in the
  same module or external.

  Mode 5: Guided Tour

  Problem it solves: "I don't know where to start reading."
  Who it's for: Complete newcomers who want structure.
  Why it's useful: Converts a large codebase into a chapter-by-chapter reading
  experience.
  What the user sees: A sidebar with a numbered reading plan (generated by LLM
  from graph structure). Each step is a card: "Chapter 3: The Streaming Pipeline
   — Read StreamProcessor::run() to understand how messages flow from topic to
  consumer." Clicking a chapter loads the source with annotations. Progress
  tracked with checkmarks. The LLM can generate multiple tour paths:
  "Architecture Tour" (breadth-first, 12 stops), "Message Flow Tour"
  (depth-first, 8 stops), "Ownership Patterns Tour" (thematic, 6 stops).

  Mode 6: "You Are Here" Navigator

  Problem it solves: "I'm looking at this function but I don't know where it
  fits in the codebase."
  Who it's for: Anyone who followed a link and lost context.
  Why it's useful: Shows the current entity's position in the containment
  hierarchy and dependency neighborhood simultaneously.
  What the user sees: A breadcrumb trail at the top (workspace → crate → module
  → impl → function). Below it, a small neighborhood graph (ego network, 8-12
  nodes) showing callers, callees, and sibling functions in the same impl block.
   The current entity is centered and highlighted. Every node is clickable.

  Mode 7: "What Should I Read Next?" Recommender

  Problem it solves: "I just read this function. Where should I go?"
  Who it's for: Anyone mid-reading session who wants direction.
  Why it's useful: Replaces random browsing with graph-guided suggestions ranked
   by relevance to what you've already read.
  What the user sees: A dropdown/panel showing 3-5 suggestions. Each suggestion
  is a card: entity name, relationship to current entity ("calls this",
  "implements the same trait", "in the same community"), and a relevance score.
  Suggestions are computed as: PPR from current entity, filtered to exclude
  already-read entities, ranked by combined PPR + PageRank. The LLM adds a
  1-sentence reason: "Read this next because it's the error handling path for
  the function you just read."

  Mode 8: Dependency Ladder

  Problem it solves: "What does this module depend on, and what depends on it?"
  Who it's for: Developers building a mental model of module boundaries.
  Why it's useful: Shows the upward (what I need) and downward (who needs me)
  dependency chains as a clean visual.
  What the user sees: The current entity or module in the center. Above:
  upstream dependencies as a tree expanding upward. Below: downstream dependents
   as a tree expanding downward. Each level is one hop. Nodes show entity names
  and edge counts. Color intensity indicates coupling strength (more edges =
  darker). Click any node to re-center the ladder.

  Mode 9: Hotspot Heatmap

  Problem it solves: "Where is the complex/critical code in this codebase?"
  Who it's for: Tech leads, architecture reviewers, anyone deciding where to
  invest reading time.
  Why it's useful: Immediately shows which areas are structurally important
  without reading anything.
  What the user sees: The architecture map (Mode 1) overlaid with a heat
  gradient. Heat is a composite of PageRank + in-degree + k-core shell number.
  Hottest areas are the most structurally central, most-depended-upon code.
  Clicking a hot spot zooms into the module with the heat metric visible
  per-entity.

  Mode 10: Reading History & Bookmarks

  Problem it solves: "I was reading this codebase yesterday. Where was I?"
  Who it's for: Anyone returning to a multi-session reading effort.
  Why it's useful: Codebases take days to learn. Without reading state, every
  session starts from scratch.
  What the user sees: A timeline/list view showing every entity the user has
  viewed, in chronological order. Entities can be bookmarked (starred). The
  architecture map shows read/unread as a visual overlay (read entities are
  dimmed or checkmarked). A "resume" button takes the user to their last-read
  entity with "You Are Here" context. The "What Should I Read Next?" recommender
   accounts for reading history.

  Mode 11: Side-by-Side Comparison

  Problem it solves: "How is TopicConsumer different from ConsumerGroup? They
  seem similar."
  Who it's for: Anyone confused by two similarly-named or similarly-connected
  entities.
  Why it's useful: Explicit comparison prevents the slow confusion of reading
  two things separately and trying to hold both in memory.
  What the user sees: Two source panes side by side. Between them, a diff-like
  view showing: shared dependencies, unique dependencies, shared callers, unique
   callers, shared trait implementations, unique ones. The LLM provides a
  3-sentence explanation: "TopicConsumer handles a single topic. ConsumerGroup
  coordinates multiple TopicConsumers across partitions. The key difference is
  that ConsumerGroup owns the offset management."

  Mode 12: Ownership & Borrow Visualizer

  Problem it solves: "Why does this function take &mut self instead of &self?
  What is it mutating?"
  Who it's for: Rust newcomers struggling with ownership.
  Why it's useful: Rust's ownership model is the #1 source of confusion for
  newcomers. Making it visual helps.
  What the user sees: Source code with color-coded annotations: owned values
  (solid), shared references (dashed blue), mutable references (dashed red),
  moves (arrows), clones (copy icons). This is limited to what tree-sitter can
  extract (function signatures, &, &mut, self patterns, .clone() calls) — it is
  NOT borrow-checker-level analysis. The LLM explains the pattern: "This takes
  &mut self because process() modifies the internal buffer. Notice the Vec::push
   on line 42 — that's the mutation."

  Honest scope note: This mode is approximate. Tree-sitter sees syntax, not
  borrow-checker semantics. The annotations show what the code declares, not
  what the compiler verifies. The LLM fills the gap with explanations, but this
  mode should be labeled "Ownership Patterns (syntactic)" to set expectations.

  ---
  4. Workflow Catalog

  #: 1
  Workflow: Open codebase, get orientation
  Human Action/Prompt: Drags folder into app
  LLM Role: Generates 3-sentence overview from graph stats
  Parseltongue API Role: /stats, /communities
  Journey Stage: SEARCH
  Visual/Textual: Visual (arch map)
  Required Algorithms: Leiden, PageRank
  Why It Matters: First impression determines whether user keeps using the app
  ────────────────────────────────────────
  #: 2
  Workflow: Click community to zoom
  Human Action/Prompt: Clicks cluster on arch map
  LLM Role: Silent — visual navigation
  Parseltongue API Role: /community/{id}/entities, /community/{id}/graph
  Journey Stage: ANCHOR
  Visual/Textual: Visual (module map)
  Required Algorithms: Leiden membership lookup
  Why It Matters: Replaces aimless folder browsing
  ────────────────────────────────────────
  #: 3
  Workflow: Read most important function in module
  Human Action/Prompt: Clicks top-ranked entity in module view
  LLM Role: Optional: "This is the entry point for X because..."
  Parseltongue API Role: /entity/{id}, /deep-dive?entity={id}
  Journey Stage: DEEP DIVE
  Visual/Textual: Text (source + annotations)
  Required Algorithms: PageRank ranking, BFS callers/callees
  Why It Matters: Guides user to start reading at the most important place
  ────────────────────────────────────────
  #: 4
  Workflow: "What does this call?"
  Human Action/Prompt: Clicks "callees" chip on current entity
  LLM Role: Silent
  Parseltongue API Role: /callees?entity={id}
  Journey Stage: DEEP DIVE
  Visual/Textual: Visual (call chain)
  Required Algorithms: BFS forward on call edges
  Why It Matters: Basic navigation, table stakes
  ────────────────────────────────────────
  #: 5
  Workflow: "Who calls this?"
  Human Action/Prompt: Clicks "callers" chip
  LLM Role: Silent
  Parseltongue API Role: /callers?entity={id}
  Journey Stage: DEEP DIVE
  Visual/Textual: Visual (call chain)
  Required Algorithms: BFS reverse on call edges
  Why It Matters: Basic navigation, table stakes
  ────────────────────────────────────────
  #: 6
  Workflow: "Explain this module to me"
  Human Action/Prompt: Types in LLM panel
  LLM Role: Generates structured explanation using entity list + community +
    callers/callees data
  Parseltongue API Role: /community/{id}/entities, /cluster?entity={anchor}
  Journey Stage: CLUSTER
  Visual/Textual: Text (LLM narration)
  Required Algorithms: PPR, PageRank, Leiden
  Why It Matters: The killer LLM workflow — structured explanation, not summary
  ────────────────────────────────────────
  #: 7
  Workflow: "What should I read next?"
  Human Action/Prompt: Clicks "Next" button or asks LLM
  LLM Role: Ranks suggestions with 1-sentence reasons
  Parseltongue API Role: /suggest-next?entity={id}&history=[...]
  Journey Stage: CLUSTER
  Visual/Textual: Visual (suggestion cards)
  Required Algorithms: PPR from current, filtered by history
  Why It Matters: Keeps reading momentum alive
  ────────────────────────────────────────
  #: 8
  Workflow: Follow a guided tour
  Human Action/Prompt: Selects a tour from sidebar
  LLM Role: Generates tour plan from graph structure
  Parseltongue API Role: /tour/generate?focus={topic}&depth={n}
  Journey Stage: TOUR
  Visual/Textual: Visual (numbered chapter list)
  Required Algorithms: BFS path, PageRank for stop selection, Leiden for scope
  Why It Matters: Converts intimidating codebase into structured reading
  ────────────────────────────────────────
  #: 9
  Workflow: Find a trait's implementations
  Human Action/Prompt: Clicks trait name or asks "who implements X?"
  LLM Role: Explains dispatch pattern
  Parseltongue API Role: /impls?trait={id}
  Journey Stage: DEEP DIVE
  Visual/Textual: Visual (trait/impl split view)
  Required Algorithms: Edge-type filter on implements edges
  Why It Matters: Rust-specific, high-value for newcomers
  ────────────────────────────────────────
  #: 10
  Workflow: Find what trait a type implements
  Human Action/Prompt: Clicks type name, "traits" tab
  LLM Role: Explains what capabilities this type has
  Parseltongue API Role: /traits?type={id}
  Journey Stage: DEEP DIVE
  Visual/Textual: Visual (trait list + method overlay)
  Required Algorithms: Reverse edge-type filter
  Why It Matters: Rust-specific, high-value
  ────────────────────────────────────────
  #: 11
  Workflow: View blast radius before a change
  Human Action/Prompt: Clicks "impact" on an entity
  LLM Role: Explains risk level
  Parseltongue API Role: /blast-radius?entity={id}&hops=3
  Journey Stage: POST-DIVE
  Visual/Textual: Visual (blast radius tree)
  Required Algorithms: BFS forward + In-degree severity
  Why It Matters: Practical for anyone about to make a change
  ────────────────────────────────────────
  #: 12
  Workflow: Trace backward from a confusing entity
  Human Action/Prompt: Asks "why does this exist?" or clicks "trace back"
  LLM Role: Narrates the chain
  Parseltongue API Role: /upstream-trace?entity={id}&hops=4
  Journey Stage: POST-DIVE
  Visual/Textual: Visual (reverse chain)
  Required Algorithms: Reverse BFS + PageRank ranking
  Why It Matters: Makes sense of code that seems random in isolation
  ────────────────────────────────────────
  #: 13
  Workflow: Compare two entities
  Human Action/Prompt: Selects two entities, clicks "compare"
  LLM Role: Generates comparison explanation
  Parseltongue API Role: /compare?a={id}&b={id}
  Journey Stage: DEEP DIVE
  Visual/Textual: Visual (side-by-side)
  Required Algorithms: Shared/unique neighbor sets, community overlap
  Why It Matters: Resolves "these seem similar" confusion
  ────────────────────────────────────────
  #: 14
  Workflow: Identify the core vs periphery
  Human Action/Prompt: Clicks "core/periphery" view
  LLM Role: Explains what core means architecturally
  Parseltongue API Role: /core-periphery
  Journey Stage: POST-DIVE
  Visual/Textual: Visual (k-core overlay on map)
  Required Algorithms: k-core decomposition
  Why It Matters: Quick architecture gut-check
  ────────────────────────────────────────
  #: 15
  Workflow: Find cycles
  Human Action/Prompt: Clicks "cycles" view
  LLM Role: Explains which cycles are intentional vs problematic
  Parseltongue API Role: /cycles
  Journey Stage: POST-DIVE
  Visual/Textual: Visual (cycle highlight on graph)
  Required Algorithms: SCC
  Why It Matters: Architecture health check
  ────────────────────────────────────────
  #: 16
  Workflow: Find dead code
  Human Action/Prompt: Clicks "dead code" view
  LLM Role: Explains what's likely safe to ignore
  Parseltongue API Role: /dead-code
  Journey Stage: POST-DIVE
  Visual/Textual: Visual (dimmed unreachable entities on map)
  Required Algorithms: BFS reachability from public roots
  Why It Matters: Focuses reading effort on living code
  ────────────────────────────────────────
  #: 17
  Workflow: Bookmark an entity for later
  Human Action/Prompt: Clicks star/pin icon
  LLM Role: Silent
  Parseltongue API Role: /bookmark (POST, local storage)
  Journey Stage: HISTORY
  Visual/Textual: Visual (star icon)
  Required Algorithms: None
  Why It Matters: Multi-session reading support
  ────────────────────────────────────────
  #: 18
  Workflow: Resume reading session
  Human Action/Prompt: Opens app, clicks "Resume"
  LLM Role: "Welcome back. Last time you were reading X. You've covered 23% of
    the streaming module."
  Parseltongue API Role: /history/last, /history/coverage
  Journey Stage: HISTORY
  Visual/Textual: Visual (resume card)
  Required Algorithms: Reading history + community coverage %
  Why It Matters: Retention — keeps users coming back
  ────────────────────────────────────────
  #: 19
  Workflow: View reading progress
  Human Action/Prompt: Clicks "Progress" tab
  LLM Role: Optional summary of what's been learned
  Parseltongue API Role: /history/coverage
  Journey Stage: HISTORY
  Visual/Textual: Visual (heatmap overlay: read/unread)
  Required Algorithms: Reading history overlay on Leiden communities
  Why It Matters: Motivation, sense of progress
  ────────────────────────────────────────
  #: 20
  Workflow: "What is this pattern?"
  Human Action/Prompt: Selects code block, asks LLM
  LLM Role: Identifies Rust patterns (builder, newtype, typestate, etc.)
  Parseltongue API Role: /entity/{id} (source + signature context)
  Journey Stage: DEEP DIVE
  Visual/Textual: Text (LLM narration)
  Required Algorithms: None (LLM-only)
  Why It Matters: Rust learning acceleration
  ────────────────────────────────────────
  #: 21
  Workflow: Dependency ladder for a module
  Human Action/Prompt: Clicks "dependencies" on module view
  LLM Role: Optional: explains why key dependencies exist
  Parseltongue API Role: /dependency-ladder?entity={id}&direction=both&hops=3
  Journey Stage: ANCHOR
  Visual/Textual: Visual (vertical tree)
  Required Algorithms: BFS forward + reverse
  Why It Matters: Mental model of module boundaries
  ────────────────────────────────────────
  #: 22
  Workflow: View hotspot map
  Human Action/Prompt: Clicks "hotspots" toggle on arch map
  LLM Role: Explains what hot means
  Parseltongue API Role: /hotspots?top=20
  Journey Stage: POST-DIVE
  Visual/Textual: Visual (heatmap overlay)
  Required Algorithms: PageRank + In-degree + k-core composite
  Why It Matters: Focuses reading on what matters
  ────────────────────────────────────────
  #: 23
  Workflow: Public boundary resolution
  Human Action/Prompt: Clicks a private function, asks "where is this exposed?"
  LLM Role: Explains the exposure chain
  Parseltongue API Role: /anchor?entity={id}
  Journey Stage: ANCHOR
  Visual/Textual: Visual (path to boundary)
  Required Algorithms: Reverse BFS with visibility filter
  Why It Matters: Moat workflow — nobody else does this
  ────────────────────────────────────────
  #: 24
  Workflow: "How does data flow through this?"
  Human Action/Prompt: Asks about a pipeline or handler
  LLM Role: Narrates the path, limited to call-chain level
  Parseltongue API Role: /call-chain?from={id}&to={id}
  Journey Stage: DEEP DIVE
  Visual/Textual: Visual (path highlight)
  Required Algorithms: BFS/DFS path finding
  Why It Matters: Understanding execution flow
  ────────────────────────────────────────
  #: 25
  Workflow: Search for a function by name
  Human Action/Prompt: Types in search bar
  LLM Role: Silent
  Parseltongue API Role: /search
  Journey Stage: SEARCH
  Visual/Textual: Visual (result list with context)
  Required Algorithms: RRF (FTS5 + trie + trigram)
  Why It Matters: Table stakes entry point
  ────────────────────────────────────────
  #: 26
  Workflow: Cross-module coupling view
  Human Action/Prompt: Clicks edge between two communities
  LLM Role: Explains the coupling
  Parseltongue API Role: /coupling?a={id}&b={id}
  Journey Stage: POST-DIVE
  Visual/Textual: Visual (specific crossing edges)
  Required Algorithms: Leiden + cross-boundary edge enumeration
  Why It Matters: Architecture insight
  ────────────────────────────────────────
  #: 27
  Workflow: "Show me the error handling"
  Human Action/Prompt: Asks LLM or clicks filter
  LLM Role: Identifies Result/Error paths in call chain
  Parseltongue API Role: /entities?filter=error_handling + /call-chain
  Journey Stage: DEEP DIVE
  Visual/Textual: Visual (filtered call chain)
  Required Algorithms: Edge filter + BFS
  Why It Matters: Rust-specific high-value reading
  ────────────────────────────────────────
  #: 28
  Workflow: Neighborhood browser
  Human Action/Prompt: Right-clicks entity, "Show neighborhood"
  LLM Role: Silent
  Parseltongue API Role: /cluster?entity={id}&budget=3000
  Journey Stage: CLUSTER
  Visual/Textual: Visual (ego network graph)
  Required Algorithms: PPR, ego network extraction
  Why It Matters: Contextual understanding

  ---
  5. Top 10 UX Flows (Ranked)

  1. Architecture Overview → Community Zoom → Read (#1 + #2 + #3)

  Why a newcomer uses it repeatedly: This is the landing experience. Every
  session starts here. The user opens the app, sees the codebase as 8-15
  clusters instead of 400 files, clicks one, and starts reading the most
  important entity. In 30 seconds, they've gone from "I have no idea what this
  codebase is" to "I'm reading the most critical function in the streaming
  module."

  Better than plain IDE browsing: VS Code shows a file tree. This shows a
  concept map. The file tree says src/streaming/consumer/consumer_group.rs. The
  concept map says "Consumer Group (k-core: 8, PageRank: 0.04, calls: 12,
  callers: 8) — this is a core entity in the streaming subsystem."

  Data/API support needed: /communities (precomputed Leiden assignments with
  labels), /community/{id}/entities (ranked by PageRank), /entity/{id} with
  source from disk + callers + callees.

  Human-driven vs LLM-driven: 90% human-driven. The user clicks. The LLM
  provides a 1-sentence orientation label per community and a 1-sentence note on
   the entity they click. No chat required.

  2. Guided Tour (#8)

  Why a newcomer uses it repeatedly: Because "I don't know where to start" is
  the #1 blocker for codebase learning. A guided tour converts paralysis into a
  checklist. The user opens "Architecture Tour," reads 12 entities in order, and
   at the end has a working mental model. They can do this across 3 sessions and
   pick up where they left off.

  Better than plain IDE browsing: An IDE has no concept of "reading order." It
  shows files alphabetically. A tour says "read this first, then this, then this
   — and here's why."

  Data/API support needed: /tour/generate (LLM generates tour from graph
  structure — entry points, most central entities, community representatives,
  key trait definitions). /history/tour-progress (which stops have been read).

  Human-driven vs LLM-driven: 60% LLM-driven (tour generation and narration),
  40% human-driven (clicking through, deciding to skip or go deeper).

  3. "What Should I Read Next?" (#7)

  Why a newcomer uses it repeatedly: Because after reading one function, the
  natural question is "now what?" Without guidance, the user either follows a
  random call or goes back to the file tree. The recommender keeps flow state
  alive.

  Better than plain IDE browsing: "Go to definition" shows you ONE thing. The
  recommender shows you 3-5 things ranked by relevance to your current reading
  context, filtered by what you've already read.

  Data/API support needed: /suggest-next?entity={id}&history=[list]. Computed as
   PPR from current entity, excluding read entities, ranked by PPR × global
  PageRank. LLM adds 1-sentence reasoning per suggestion.

  Human-driven vs LLM-driven: 50/50. The graph computes the ranking. The LLM
  explains why. The human chooses.

  4. "Explain This Module To Me" (#6)

  Why a newcomer uses it repeatedly: Because modules are the unit of
  understanding, not files. "Explain the consumer module" is the question a
  newcomer would ask a senior engineer. The LLM, fed with graph-structured data,
   can answer it far better than chat-with-no-context.

  Better than plain IDE browsing: An IDE can't explain anything. A plain LLM
  hallucinates about code it hasn't read. This LLM reads a graph-verified entity
   list with centrality scores, community membership, and call relationships —
  then explains using actual structure.

  Data/API support needed: /community/{id}/entities (top 20 by PageRank),
  /cluster?entity={anchor}&budget=4000 (neighborhood context),
  /community/{id}/graph (internal edges). LLM synthesizes into structured
  explanation: "This module has 3 main responsibilities..."

  Human-driven vs LLM-driven: 80% LLM-driven (the explanation is the value), 20%
   human-driven (asking the question, clicking entities mentioned in the
  explanation).

  5. Trait/Impl Browser (#9 + #10)

  Why a newcomer uses it repeatedly: Because Rust's trait system is the #1
  confusion point for newcomers. "I see impl Stream for Consumer but I don't
  understand what methods it requires or what other types implement it." This
  browser makes the abstract concrete.

  Better than plain IDE browsing: "Go to definition" on a trait shows you the
  trait. It does NOT show you all implementations side by side, which is what
  you actually need to understand polymorphism.

  Data/API support needed: /impls?trait={id}, /traits?type={id}, /entity/{id}
  for source.

  Human-driven vs LLM-driven: 70% human-driven (clicking, browsing impls). LLM
  explains the pattern: "This trait uses associated types to allow each
  implementation to define its own error type."

  6. "You Are Here" Navigator (#6 in modes)

  Why a newcomer uses it repeatedly: Because getting lost is the #1 frustration
  in code reading. You follow three call chains and suddenly have no idea where
  you are. The breadcrumb + neighborhood view re-orients instantly.

  Better than plain IDE browsing: VS Code shows the file tab. This shows
  workspace → crate → module → impl → function PLUS the 8 nearest entities in
  the dependency graph.

  Data/API support needed: /entity/{id}/context (containment chain + ego
  network, ~10 nodes).

  Human-driven vs LLM-driven: 95% human-driven. Pure navigation. LLM is silent.

  7. Reading History & Resume (#18 + #19)

  Why a newcomer uses it repeatedly: Because they close the app and come back
  tomorrow. Without reading state, they restart from scratch. With it, they
  click "Resume" and are immediately back in context with a reminder of what
  they've read.

  Better than plain IDE browsing: IDEs have "recent files." This has "reading
  coverage of the streaming module: 40%, next suggested:
  ConsumerGroup::rebalance()."

  Data/API support needed: /history/last, /history/coverage, /history/entities
  (all stored locally in SQLite).

  Human-driven vs LLM-driven: 95% human-driven. LLM provides the welcome-back
  message.

  8. Call Chain Explorer (#3 in modes)

  Why a newcomer uses it repeatedly: Because "what happens when a message
  arrives?" is answered by a call chain, not by a single function. The vertical
  lane visualization makes the execution path readable as a sequence.

  Better than plain IDE browsing: "Go to definition" is one hop. This shows 5
  hops as a visual chain with parallel branches.

  Data/API support needed: /call-chain?from={id}&depth=5 or
  /callees?entity={id}&depth=5&tree=true.

  Human-driven vs LLM-driven: 80% human-driven (visual browsing). LLM annotates:
   "This branch handles the error case."

  9. Side-by-Side Comparison (#13)

  Why a newcomer uses it repeatedly: Because large codebases have many
  similar-looking types and functions. "What's the difference between Consumer
  and ConsumerGroup?" is a question they'll ask 10 times.

  Better than plain IDE browsing: No IDE has "compare two entities by their
  graph structure." This shows shared dependencies, unique dependencies, shared
  traits, and a natural-language explanation.

  Data/API support needed: /compare?a={id}&b={id} returns shared/unique callers,
   callees, traits, community overlap.

  Human-driven vs LLM-driven: 50/50. Human selects entities. LLM explains the
  difference.

  10. Hotspot Heatmap (#22)

  Why a newcomer uses it repeatedly: Because not all code is equally important.
  A newcomer with 4 hours should read the hotspots, not the utility functions.
  The heatmap immediately shows where to focus.

  Better than plain IDE browsing: No IDE tells you "this function is
  structurally the most important in the codebase." Line count doesn't equal
  importance. Graph centrality does.

  Data/API support needed: /hotspots?top=20 (precomputed composite), rendered as
   overlay on architecture map.

  Human-driven vs LLM-driven: 90% human-driven. Visual. LLM explains what "hot"
  means on first use.

  ---
  6. Three-Level Interaction Model

  Layer 1: Human Prompting

  The human interacts through 4 modalities:

  1. Click navigation — clicking entities, communities, edges on visual
  surfaces. This is the primary modality. It should feel like Google Maps: click
   a region, zoom in, click a building, see details.
  2. Search bar — typing entity names, keywords, questions. Dual-purpose: RRF
  search for known entities, LLM-routed for questions ("explain the consumer
  module").
  3. Context menus — right-clicking an entity to see "show callers," "show
  callees," "compare with...," "start tour from here," "bookmark."
  4. LLM chat panel — a side panel where the human asks questions. But this is
  NOT the primary interface. It is a companion. The human should spend 70% of
  time looking at visual surfaces and source code, 30% interacting with the LLM.

  Layer 2: LLM Prompting

  The LLM operates in 4 behavioral modes:

  Mode A: Silent annotations. The LLM pre-generates short labels and
  descriptions that appear on visual elements. Community labels ("Streaming
  Pipeline"), entity summaries ("Main consumer loop — polls messages and
  dispatches to handlers"), tour step descriptions. These are cached after
  generation.

  Mode B: Reactive explanation. User clicks an entity or asks a question. LLM
  receives the entity's graph context (callers, callees, community, centrality,
  source snippet) and generates an explanation. The LLM prompt is structured:

  You are a senior Rust engineer explaining code to a newcomer.
  The user is looking at: [entity name, signature, file:line:line]
  Graph context: [5 callers, 3 callees, community: "streaming pipeline",
  PageRank: 0.04]
  Source: [first 50 lines]
  Reading history: [user has already read: entity A, B, C]

  Explain what this code does and why it exists.
  Do NOT dump a full summary. Explain as if you are sitting next to the
  developer.
  Point out: the key pattern, one thing that might be confusing, and what to
  read next.

  Mode C: Tour planner. User requests a guided tour. LLM receives the community
  structure, the top entities per community, and the cross-community edges. It
  generates a reading plan:

  Generate a reading tour for the "{community_name}" subsystem.
  Available entities (ranked by importance): [list with PageRank scores]
  Key internal edges: [list]
  Key external edges (to other modules): [list]
  User has already read: [list]

  Generate a 6-10 stop tour. For each stop: entity name, 1-sentence why to read
  it, and what the reader should notice.

  Mode D: Confusion resolver. User says something like "I don't understand why
  this takes Arc<Mutex<>>>." LLM receives the entity source + the type's graph
  neighborhood and explains the specific pattern. The LLM is explicitly prompted
   to:
  - Not lecture about Rust generics in the abstract
  - Explain THIS specific usage
  - Point to the specific line that motivated the pattern
  - Suggest what to read to understand the broader context

  Layer 3: Parseltongue APIs

  The APIs serve both the visual frontend and the LLM:

  - For visuals: APIs return graph-layout-friendly structures (node positions
  from community assignments, edge lists for rendering, metric values for
  color/size encoding). Response shape: { nodes: [{id, label, x, y, size, color,
   metrics}], edges: [{source, target, kind, weight}] }.
  - For LLM context: APIs return token-budgeted text packets. Response shape: { 
  entity: {name, signature, location}, callers: [{name, location, edge_kind}], 
  callees: [...], community: {name, size, modularity}, metrics: {pagerank, 
  in_degree, k_core} }.
  - For reading state: APIs store and retrieve local bookmarks, reading history,
   tour progress. Pure SQLite, no graph computation.

  How the layers interact:

  Human clicks entity on map
    → Tauri frontend requests /entity/{id}/context
    → API returns graph context (callers, callees, community, metrics)
    → Frontend renders source pane + neighborhood mini-map + breadcrumbs
    → Frontend sends context to LLM with prompt: "Explain this entity"
    → LLM returns 3-sentence explanation
    → Frontend shows explanation in side panel
    → Human reads source, reads explanation, clicks a callee to navigate
    → Frontend updates /history with the read entity
    → "What to read next?" updates based on new PPR from current position

  Critical design rule: The LLM never blocks navigation. If the LLM takes 2
  seconds, the source code and visual surfaces appear immediately. The LLM
  explanation appears asynchronously in the side panel. The human can keep
  clicking without waiting.

  ---
  7. Visual System

  Surface 1: Workspace Overview Map

  What it shows: All Leiden communities as force-directed clusters. Nodes sized
  by PageRank. Edges between communities sized by coupling strength. Community
  labels generated by LLM.
  When it appears: On first open, as the landing page.
  APIs that power it: /communities (precomputed), /community-graph
  (inter-community edges).
  Useful vs decorative: Useful if communities map to real subsystems. Decorative
   if Leiden produces random groupings. Mitigation: Only show community map if
  modularity > 0.3. Fall back to folder-based tree below that threshold.

  Surface 2: Module Map

  What it shows: Entities within one community, laid out as a force-directed
  graph. Nodes sized by PageRank within the community. Edges show
  call/dependency relationships. Currently-read entity highlighted.
  When it appears: When user zooms into a community from the workspace overview.
  APIs: /community/{id}/graph, /community/{id}/entities.
  Useful vs decorative: Useful — it replaces file-tree browsing within a module.
   The layout reveals structure (central nodes, peripheral nodes,
  clusters-within-clusters) that a file list hides.

  Surface 3: Source Pane with Graph Annotations

  What it shows: Source code with inline clickable chips. Each function call has
   a small "→" chip linking to the callee. Each function definition has a "← N
  callers" badge. Trait impls have a "⇐ trait: X" badge. Types that appear in
  signatures are clickable.
  When it appears: Whenever the user clicks an entity.
  APIs: /entity/{id} (source from disk), /entity/{id}/annotations
  (caller/callee/impl links).
  Useful vs decorative: Useful — these are the hyperlinks that make code
  browsable like a wiki. Without them, the source pane is just a read-only VS
  Code. With them, every function call is a portal.

  Surface 4: Neighborhood Mini-Map

  What it shows: An 8-15 node ego network graph centered on the current entity.
  Callers above, callees below, siblings to the sides. Each node is a small
  circle with a label, clickable.
  When it appears: Alongside the source pane (right panel or floating overlay).
  APIs: /cluster?entity={id}&budget=2000 (PPR-ranked ego network).
  Useful vs decorative: Useful — it provides spatial context that a breadcrumb
  alone cannot. "This function is called by 2 things and calls 5 things" is
  instantly visible.

  Surface 5: Breadcrumb Trail

  What it shows: workspace → crate → module → impl → function. Clickable at
  every level.
  When it appears: Always visible at the top of the source pane.
  APIs: /entity/{id}/containment-chain (trivial lookup on contains edges).
  Useful vs decorative: Useful — the cheapest, most reliable orientation
  mechanism. Never remove this.

  Surface 6: Reading Queue / Tour Sidebar

  What it shows: A numbered list of entities to read, with checkmarks for
  completed items. Can be a guided tour or a manually-curated list.
  When it appears: When the user starts a tour or manually adds entities to
  their reading queue.
  APIs: /tour/generate, /history/tour-progress, /bookmark/list.
  Useful vs decorative: Useful — transforms unstructured browsing into
  structured reading. The checkmarks provide a sense of progress.

  Surface 7: LLM Companion Panel

  What it shows: A narrow side panel with the LLM's context-sensitive
  explanations. Updates automatically when the user navigates. Shows: 1-3
  sentence explanation of the current entity, followed by a "What to read next"
  section, followed by any responses to direct questions.
  When it appears: Always visible (collapsible).
  APIs: LLM receives data from /entity/{id}/context + /suggest-next.
  Useful vs decorative: Useful IF the LLM is concise and context-aware.
  Decorative if it rambles. Mitigation: Hard limit of 150 words per automatic
  explanation. User can ask for more.

  Surface 8: Trait/Impl Relationship Panel

  What it shows: When viewing a trait: all implementing types. When viewing a
  type: all implemented traits. Methods mapped across.
  When it appears: When the user clicks a trait or type entity.
  APIs: /impls?trait={id}, /traits?type={id}.
  Useful vs decorative: Useful — this is one of the most valuable Rust-specific
  surfaces. Nowhere in a standard IDE can you see all implementations of a trait
   side-by-side with method correspondence.

  Surface 9: Hotspot Overlay

  What it shows: A gradient overlay on the workspace map or module map. Hotter =
   more structurally central (composite of PageRank + in-degree + k-core).
  When it appears: Toggle-able overlay on any map view.
  APIs: /hotspots?top=50 (precomputed).
  Useful vs decorative: Useful as a reading guide ("where should I focus?").
  Decorative if the metric doesn't correlate with user-perceived importance.
  Mitigation: Composite metric is more robust than any single metric. Allow user
   to switch between PageRank / in-degree / k-core as heat source.

  Surface 10: Reading Coverage Overlay

  What it shows: On the workspace or module map, entities the user has read are
  dimmed or checkmarked. Unread entities remain vivid.
  When it appears: Toggle-able overlay, or default after the first session.
  APIs: /history/coverage (local reading state).
  Useful vs decorative: Useful — it turns the architecture map into a progress
  tracker. The user can see "I've covered 60% of the streaming module but 0% of
  storage." This drives reading decisions.

  ---
  8. API Consequences

  SEARCH

  POST /search
    Body: { "q": "consumer group", "top_k": 10 }
    Returns: [{ id, name, kind, location, score, match_source, community_name,
  pagerank }]
  Text packet. Precomputed indexes (FTS5, trie, trigram). Query-time RRF fusion.
   ~40 tokens per result. Include community_name and pagerank so the frontend
  can show context badges on results.

  ANCHOR

  GET /anchor?entity={id}
    Returns: { boundary: {id, name, location, visibility}, path: [{id, name,
  edge_kind}] }
  Text packet. Query-time BFS reverse. ~80 tokens.

  GET /entity/{id}/containment-chain
    Returns: [{ id, name, kind, level }]  // workspace → crate → module → impl →
   function
  Text packet. Query-time lookup on contains edges. ~30 tokens. Powers
  breadcrumbs.

  CLUSTER

  GET /cluster?entity={id}&budget={tokens}
    Returns: { center: {id, name}, neighbors: [{id, name, kind, location,
  ppr_score, relation}] }
  Text packet for LLM. Query-time PPR. Budget-capped.

  GET /cluster?entity={id}&budget={tokens}&layout=true
    Returns: { nodes: [{id, label, x, y, size, group}], edges: [{source, target,
   kind}] }
  Graph-layout packet for visual rendering. Same computation, different output
  format. Node positions from force-directed layout (computed in Python, or just
   return adjacency and let the frontend layout with d3-force).

  DEEP DIVE

  GET /entity/{id}
    Returns: { id, name, kind, signature, location, source, metrics: {pagerank,
  in_degree, out_degree, k_core, community_id} }
  Text + source packet. Source read from disk. Metrics from cache. ~500-5000
  tokens depending on source length.

  GET /entity/{id}/annotations
    Returns: { callers: [{id, name, location}], callees: [{id, name, location}],
   impls: [{id, name}], traits: [{id, name}] }
  Text packet. Powers source pane annotations. Query-time BFS (1-hop).

  GET /entity/{id}/context
    Returns: { entity: {...}, callers: [...], callees: [...], community: {name,
  size}, containment: [...], metrics: {...} }
  Combined context packet. This is what the LLM receives to generate
  explanations. Budget-capped. ~1000-4000 tokens.

  GET /impls?trait={id}
    Returns: [{ id, name, location, methods: [{name, signature}] }]

  GET /traits?type={id}
    Returns: [{ id, name, location, methods: [{name, signature}] }]

  TOUR / GUIDE

  POST /tour/generate
    Body: { focus: "streaming", style: "architecture" | "depth-first" |
  "thematic", max_stops: 10, exclude: [already_read_ids] }
    Returns: { title, description, stops: [{ order, entity_id, name, location,
  reason, what_to_notice }] }
  LLM-generated from graph data. The API fetches community structure + top
  entities, sends to LLM, caches the result. ~200 tokens per stop.

  GET /suggest-next?entity={id}&history=[id1,id2,...]
    Returns: [{ id, name, location, relation_to_current, reason, relevance_score
   }]
  Mixed: PPR is query-time, PageRank is precomputed, history filtering is
  in-memory. Returns 3-5 suggestions. ~50 tokens per suggestion.

  GET /call-chain?from={id}&depth=5
    Returns: { root: {id, name}, levels: [[ {id, name, location} ]] }
  Tree-structured text packet. Query-time BFS. Powers call chain explorer.

  GET /compare?a={id}&b={id}
    Returns: { shared_callers: [...], unique_a_callers: [...], unique_b_callers:
   [...], shared_callees: [...], shared_traits: [...], unique_a_traits: [...],
  community_overlap: bool }
  Text packet. Query-time set operations on neighbor lists.

  VISUAL

  GET /communities?layout=true
    Returns: { communities: [{ id, label, x, y, size, modularity, entity_count
  }], inter_edges: [{ source_community, target_community, weight }] }
  Visual-layout packet. Precomputed Leiden + positions cached. Powers workspace
  overview map.

  GET /community/{id}/graph?layout=true
    Returns: { nodes: [{id, label, x, y, size, pagerank}], edges: [{source,
  target, kind}] }
  Visual-layout packet. Precomputed node positions within community. Powers
  module map.

  GET /hotspots?top=50
    Returns: [{ id, name, location, composite_score, pagerank, in_degree, k_core
   }]
  Precomputed. Powers heatmap overlay.

  GET /core-periphery
    Returns: [{ id, k_core_shell }]
  Precomputed. Powers k-core overlay.

  HISTORY / BOOKMARK / READING STATE

  POST /history/read
    Body: { entity_id, timestamp, duration_seconds }

  GET /history/recent?limit=20
    Returns: [{ entity_id, name, location, timestamp }]

  GET /history/coverage?community_id={id}
    Returns: { total_entities, read_entities, percentage, unread_top: [{id,
  name, pagerank}] }

  POST /bookmark
    Body: { entity_id, note }

  GET /bookmark/list
    Returns: [{ entity_id, name, location, note, timestamp }]

  GET /history/last
    Returns: { entity_id, name, location, timestamp, context_summary }
  All local SQLite. No graph computation. Instant.

  Hard calls:
  - Layout computation (force-directed) should happen in Python and be cached,
  not computed in the browser on every render. The frontend receives positions,
  not raw adjacency.
  - Source code is ALWAYS read from disk, never stored in DB. This keeps the DB
  small and source always fresh.
  - Reading history is stored per-user per-workspace. Never transmitted.
  Local-first.
  - Tour generation involves an LLM call — cache the result. Don't regenerate on
   every click.

  ---
  9. Algorithm-to-Experience Mapping

  Algorithm: BFS
  Reading/Browsing Experience: Call chain explorer, anchor resolution, blast
    radius, "what to read next" neighborhood, tour path generation
  Compute Mode: Query-time
  Library: python-igraph
  Expected Data Shape: Directed edge list, integer vertex IDs
  Bad UX If Misused: If unbounded: returns 10,000 entities for a hub node.
  Always
    cap depth (max 5 hops) and output size (max 50 nodes).
  ────────────────────────────────────────
  Algorithm: PageRank
  Reading/Browsing Experience: Entity importance ranking in module view, hotspot

    overlay, "most important function" sorting, LLM context selection
  Compute Mode: Precomputed
  Library: python-igraph
  Expected Data Shape: Directed weighted adjacency
  Bad UX If Misused: If used as sole ranking: overweights utility functions
    called everywhere (like log()). Composite with in-degree and k-core is
    better.
  ────────────────────────────────────────
  Algorithm: Personalized PageRank
  Reading/Browsing Experience: "What to read next?" suggestions, ego network
    ranking, CLUSTER packing
  Compute Mode: Query-time (or cached for hot entities)
  Library: python-igraph
  Expected Data Shape: Directed adjacency + single seed node
  Bad UX If Misused: If multi-seed: ambiguous results. Always single-seed from
    current reading position. If uncapped: returns all 50K entities ranked.
    Always top-k truncation (k=10-20).
  ────────────────────────────────────────
  Algorithm: In-Degree
  Reading/Browsing Experience: Fan-in badges on source pane, severity ranking in

    blast radius, "most depended upon" sorting
  Compute Mode: Precomputed
  Library: Polars grouped count
  Expected Data Shape: Edge table dst_id
  Bad UX If Misused: Trivially correct. No misuse risk beyond confusing high
    in-degree with "good code" — it just means "widely used."
  ────────────────────────────────────────
  Algorithm: Out-Degree
  Reading/Browsing Experience: Fan-out badges on source pane, "this function
    calls 15 things" warnings, orchestrator detection
  Compute Mode: Precomputed
  Library: Polars grouped count
  Expected Data Shape: Edge table src_id
  Bad UX If Misused: Risk: labeling high out-degree as "god function" when it's
  a
    legitimate orchestrator. Show the number, don't editorialize.
  ────────────────────────────────────────
  Algorithm: Betweenness
  Reading/Browsing Experience: Bridge entity highlighting on architecture map,
    "bottleneck" identification
  Compute Mode: Precomputed
  Library: NetworKit (ApproxBetweenness for large graphs)
  Expected Data Shape: Graph object
  Bad UX If Misused: Expensive. Never query-time. On graphs >50K nodes, must use

    approximate. If shown without explanation, users won't understand
    "betweenness 0.34." Convert to ordinal: "3rd most central bridge."
  ────────────────────────────────────────
  Algorithm: k-core
  Reading/Browsing Experience: Core/periphery overlay, hotspot composite, "focus

    your reading on the core" guidance
  Compute Mode: Precomputed
  Library: NetworKit
  Expected Data Shape: Graph object, unweighted
  Bad UX If Misused: Low risk. But k-core values alone are not interpretable by
    users. Convert to labels: "core (k≥6)", "mid (k=3-5)", "periphery (k≤2)."
  ────────────────────────────────────────
  Algorithm: Leiden
  Reading/Browsing Experience: Community labels on workspace map, module maps,
    community coverage tracking, tour scoping, cross-module coupling
  Compute Mode: Precomputed
  Library: python-igraph
  Expected Data Shape: Weighted edge list + resolution parameter
  Bad UX If Misused: Resolution parameter determines granularity. Too low: 3
    giant clusters. Too high: 200 micro-clusters. Need to test multiple
    resolutions and pick best modularity. If modularity < 0.3, communities are
    meaningless — fall back to folder structure.
  ────────────────────────────────────────
  Algorithm: RRF
  Reading/Browsing Experience: Search results ranking
  Compute Mode: Query-time
  Library: Custom Python
  Expected Data Shape: Ranked lists from 3-4 signals
  Bad UX If Misused: If one signal returns garbage for short queries (trigram on

    2-char input), it contaminates results. Gate: skip trigram for queries < 4
    chars.
  ────────────────────────────────────────
  Algorithm: Symbol trie
  Reading/Browsing Experience: Exact/prefix search in search bar
  Compute Mode: Precomputed
  Library: marisa-trie or Rust fst
  Expected Data Shape: Static string vocab → entity ID
  Bad UX If Misused: Must rebuild on re-index. Stale trie = missing entities in
    search.
  ────────────────────────────────────────
  Algorithm: Trigram
  Reading/Browsing Experience: Fuzzy search for partial/misspelled names
  Compute Mode: Precomputed index, query-time match
  Library: RapidFuzz
  Expected Data Shape: Symbol strings
  Bad UX If Misused: Garbage below 3 chars. High false positive rate for common
    trigrams. Cap results at top-10.
  ────────────────────────────────────────
  Algorithm: Ego network
  Reading/Browsing Experience: Neighborhood mini-map, CLUSTER packing, context
    for LLM
  Compute Mode: Query-time
  Library: python-igraph
  Expected Data Shape: Directed adjacency + seed + depth
  Bad UX If Misused: Hub node explosion at depth=2 (200+ nodes). Auto-reduce to
    depth=1 for high-degree entities. Always enforce token/node budget.
  ────────────────────────────────────────
  Algorithm: SCC
  Reading/Browsing Experience: Cycle detection and display
  Compute Mode: Precomputed
  Library: python-igraph clusters(mode="strong")
  Expected Data Shape: Directed edge list
  Bad UX If Misused: Filter SCCs of size 1 (trivial). Only show non-trivial
    cycles (size ≥ 2).

  ---
  10. LLM-Guided Reading Patterns

  Pattern 1: Narrated Reading Companion

  Behavior: When the user navigates to any entity, the LLM panel automatically
  shows a 2-3 sentence explanation. Not a summary of the code — an explanation
  of why this code exists and what to pay attention to.
  Concrete prompt:
  Entity: stream_processor::poll_next (src/streaming/processor.rs:142:198)
  Callers: [consumer_loop::run, batch_processor::flush]
  Callees: [message_queue::dequeue, offset_tracker::advance]
  Community: "Streaming Pipeline" (12 entities)

  In 2-3 sentences, explain to a newcomer: what does this function do, why does
  it exist, and what is one thing that might confuse them? Point to a specific
  line number if relevant.
  Why it's not generic: The LLM sees the graph neighborhood, not just the
  source. It can say "This is called from two places — the main consumer loop
  and the batch flusher — which is why it handles both single and batch modes."

  Pattern 2: Codebase Tutor

  Behavior: User says "teach me about the streaming module." LLM generates a
  structured lesson plan, then walks the user through it step by step, waiting
  for them to read each entity before continuing.
  Concrete interaction:
  LLM: "The streaming module has 3 key concepts:
  1. **Message** — the unit of data (read MessageEnvelope first)
  2. **Topic** — a named stream of messages (read Topic::publish)
  3. **Consumer** — reads messages from a topic (read Consumer::poll)

  Let's start with MessageEnvelope. Click it when you're ready, and I'll explain
   what to look for."

  [User clicks MessageEnvelope]

  LLM: "Notice the `payload: Bytes` field on line 14. This is a zero-copy
  reference, which means messages are never cloned as they move through the
  system. Keep this in mind — it explains why many downstream functions take
  `&Message` instead of `Message`. Ready for Topic?"

  Pattern 3: Confusion Resolver

  Behavior: User highlights a confusing line or asks "why does this use
  Pin<Box<dyn Future>>?" The LLM explains THIS specific usage, not a generic
  Rust tutorial.
  Concrete prompt:
  User is confused about line 67 of src/streaming/consumer.rs:
  `fn poll_next(self: Pin<&mut Self>, cx: &mut Context<'_>) ->
  Poll<Option<Self::Item>>`

  This is the implementation of the `Stream` trait for `Consumer`.
  The trait requires `Pin<&mut Self>` because async streams may contain
  self-referential futures.

  Explain in 2 sentences why this specific function signature exists. Do not
  give a general Rust tutorial about Pin.

  Pattern 4: "Ask Before Dump"

  Behavior: When the user asks a broad question ("how does message delivery
  work?"), the LLM does NOT dump 500 words. Instead, it asks a clarifying
  question:
  LLM: "Message delivery involves 3 stages:
  1. Producer publishes to a topic
  2. Server routes to the correct partition
  3. Consumer polls from the partition

  Which stage would you like to explore? Or should I walk you through all three
  in order?"
  This is critical. The LLM must resist the urge to explain everything at once.
  Progressive disclosure applies to the LLM's own output.

  Pattern 5: Next-Best-Reading Suggestion

  Behavior: After the user finishes reading an entity, the LLM automatically
  suggests what to read next with a reason.
  LLM: "You just read `Consumer::poll`. Three suggestions:
  1. **ConsumerGroup::rebalance** — this decides which consumer reads which
  partition (you'll understand why `Consumer` has a `partition_id` field)
  2. **OffsetTracker::commit** — this is called after `poll` to mark progress
  (explains the `offset` parameter you saw)
  3. **MessageBatch::iter** — this is what `poll` returns (explains the `Item`
  associated type)

  Pattern 6: Compare Two Things

  Behavior: User asks "what's the difference between TopicConsumer and
  ConsumerGroup?" LLM receives the /compare data and generates a concise
  structural comparison.
  LLM: "TopicConsumer handles a single topic's messages. ConsumerGroup
  coordinates multiple TopicConsumers across partitions.

  Key structural difference: ConsumerGroup has 8 callers (it's a coordination
  point) while TopicConsumer has 2 callers (it's a leaf worker). They share the
  `MessageHandler` trait but ConsumerGroup also implements `Rebalancer`.

  Read ConsumerGroup::rebalance to see how it distributes work."

  ---
  11. Risks and Failure Modes

  Risk: Too much text
  What Goes Wrong: LLM generates wall-of-text explanations for every entity.
  User
    starts ignoring the LLM panel.
  How It Manifests: User closes the LLM panel after 10 minutes.
  Mitigation: Hard limit: 150 words for automatic explanations. User can
    explicitly ask for more. Default state: short and specific.
  ────────────────────────────────────────
  Risk: Fake visual novelty
  What Goes Wrong: Architecture map looks cool on first use but communities
  don't
    match real subsystems.
  How It Manifests: User stops trusting the map after seeing 2 bad clusters.
  Mitigation: Modularity gate: suppress community view if modularity < 0.3. Show

    folder structure as fallback. Display modularity score openly.
  ────────────────────────────────────────
  Risk: Stale snapshot
  What Goes Wrong: User edits code, graph doesn't update, entities shown in map
    don't exist anymore.
  How It Manifests: User clicks entity, gets "file not found" or sees wrong
    source.
  Mitigation: File hash check on every source read. Show "stale" badge on
    entities where source has changed since last index. One-click re-index
    button.
  ────────────────────────────────────────
  Risk: Wrong edges
  What Goes Wrong: Tree-sitter resolves process() to the wrong target. Call
  chain
    shows incorrect path.
  How It Manifests: User follows a call chain into unrelated code. Loses trust.
  Mitigation: Edge resolution rate displayed on architecture overview. Visual
    confidence indicators: solid lines for high-confidence edges, dashed for
    ambiguous. Tooltip: "3 possible targets for this call."
  ────────────────────────────────────────
  Risk: Bad guided tours
  What Goes Wrong: LLM generates a tour that starts with utility functions
    instead of entry points. Tour is boring or confusing.
  How It Manifests: User abandons the tour after 3 stops.
  Mitigation: Tour generation must use PageRank to prioritize important
  entities.
    Tours should start with public entry points (high in-degree, public
    visibility). Test tours on 3 real codebases before shipping. Allow user to
    rate tour quality.
  ────────────────────────────────────────
  Risk: Overwhelming newcomers
  What Goes Wrong: Architecture map shows 500 nodes on first open. Newcomer is
    more confused than before.
  How It Manifests: User closes the app.
  Mitigation: Default view: community-level only (8-15 clusters, not individual
    entities). Zoom-to-detail is opt-in. First-launch wizard: "Click a cluster
  to
     explore" with a pulsing highlight.
  ────────────────────────────────────────
  Risk: LLM over-explaining
  What Goes Wrong: LLM lectures about Rust generics for 300 words when the user
    just wanted to know what a function does.
  How It Manifests: User stops reading LLM output.
  Mitigation: Prompt engineering: "Do not explain general Rust concepts. Explain

    THIS specific code. Maximum 3 sentences unless the user asks for more."
  ────────────────────────────────────────
  Risk: Meaningless hotspot heatmap
  What Goes Wrong: Utility module (logging, error handling) shows as #1 hotspot
    because everything calls it.
  How It Manifests: User wastes time reading the logging module.
  Mitigation: Filter: allow user to exclude specific entities/communities from
    hotspot calculation. Default: exclude entities with "log", "error", "util"
  in
     path. Better: let user mark entities as "infrastructure — exclude from
    hotspot."
  ────────────────────────────────────────
  Risk: Slow LLM blocking navigation
  What Goes Wrong: Every entity click triggers an LLM call. Network latency or
    LLM rate limit makes the app feel slow.
  How It Manifests: User waits 3 seconds between clicks.
  Mitigation: LLM explanations are async and non-blocking. Source pane + visual
    navigation render immediately. LLM panel shows "thinking..." and populates
    when ready. Pre-cache LLM explanations for top-20 entities per community.
  ────────────────────────────────────────
  Risk: Reading history creating pressure
  What Goes Wrong: "You've read 15% of the codebase" feels like a progress bar
    that induces anxiety rather than motivation.
  How It Manifests: User feels like they'll never catch up.
  Mitigation: Frame as coverage, not completion. "You've explored the 3 most
    important subsystems" is better than "You've read 150 of 3000 entities."
    Community-level coverage is better than entity-level.

  ---
  12. Recommended Build Order

  v1 — "I Can Browse This Codebase"

  User feels: "I opened a large codebase and within 30 seconds I can see its
  structure and start reading."

  ┌───────────────────────────────────────────────┬─────────────────────────┐
  │                  What ships                   │   Experience enabled    │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ Tauri app shell with workspace drag-and-drop  │ Entry point             │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ Tree-sitter entity + edge extraction (2-pass  │ Foundation              │
  │ resolution)                                   │                         │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ SQLite schema: entities, edges, files,        │ Storage                 │
  │ snapshots                                     │                         │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ Architecture overview map (Leiden             │ First-open orientation  │
  │ communities, force layout)                    │                         │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ Community zoom → entity list (sorted by       │ Browse by concept, not  │
  │ PageRank)                                     │ folder                  │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ Source pane with callers/callees annotation   │ Clickable code reading  │
  │ chips                                         │                         │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ Breadcrumb trail (containment chain)          │ "You are here"          │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ Neighborhood mini-map (ego network, PPR)      │ Spatial context         │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ Search bar (RRF: FTS5 + trie + trigram)       │ Find things by name     │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ Precomputed PageRank + In-degree + Out-degree │ Ranking and metrics     │
  ├───────────────────────────────────────────────┼─────────────────────────┤
  │ Hotspot overlay toggle                        │ Where to focus reading  │
  └───────────────────────────────────────────────┴─────────────────────────┘

  v1 endpoint count: 10 (/search, /communities, /community/{id}/entities,
  /community/{id}/graph, /entity/{id}, /entity/{id}/annotations,
  /entity/{id}/containment-chain, /cluster, /anchor, /hotspots)

  v1.1 — "The App Guides Me"

  User feels: "I started a tour and now I understand the streaming module."

  ┌─────────────────────────────────────────────────┬───────────────────────┐
  │                   What ships                    │  Experience enabled   │
  ├─────────────────────────────────────────────────┼───────────────────────┤
  │ LLM companion panel (auto-explain on            │ Narrated reading      │
  │ navigation)                                     │                       │
  ├─────────────────────────────────────────────────┼───────────────────────┤
  │ Guided tour generation (LLM + graph)            │ Structured learning   │
  ├─────────────────────────────────────────────────┼───────────────────────┤
  │ "What to read next?" suggestions (PPR + history │ Reading momentum      │
  │  filter)                                        │                       │
  ├─────────────────────────────────────────────────┼───────────────────────┤
  │ Reading history tracking                        │ Multi-session         │
  │                                                 │ continuity            │
  ├─────────────────────────────────────────────────┼───────────────────────┤
  │ Reading coverage overlay on maps                │ Progress visibility   │
  ├─────────────────────────────────────────────────┼───────────────────────┤
  │ Resume from last session                        │ Retention             │
  ├─────────────────────────────────────────────────┼───────────────────────┤
  │ Bookmarks/pins                                  │ Personal organization │
  └─────────────────────────────────────────────────┴───────────────────────┘

  v1.1 adds: 7 endpoints (/suggest-next, /tour/generate, /history/*,
  /bookmark/*)

  v1.2 — "I Can Understand Rust Patterns"

  User feels: "I finally understand how traits and impls work in this codebase."

  ┌───────────────────────────────────────┬─────────────────────────────────┐
  │              What ships               │       Experience enabled        │
  ├───────────────────────────────────────┼─────────────────────────────────┤
  │ Trait/impl browser (split view,       │ Rust-specific navigation        │
  │ method mapping)                       │                                 │
  ├───────────────────────────────────────┼─────────────────────────────────┤
  │ Call chain explorer (vertical lane    │ Execution flow understanding    │
  │ visualization)                        │                                 │
  ├───────────────────────────────────────┼─────────────────────────────────┤
  │ Side-by-side comparison               │ Resolving "these seem similar"  │
  │                                       │ confusion                       │
  ├───────────────────────────────────────┼─────────────────────────────────┤
  │ Cycle detection overlay               │ Architecture health             │
  ├───────────────────────────────────────┼─────────────────────────────────┤
  │ Dead code dimming on maps             │ Focus reading on living code    │
  ├───────────────────────────────────────┼─────────────────────────────────┤
  │ k-core core/periphery overlay         │ Architecture layering           │
  ├───────────────────────────────────────┼─────────────────────────────────┤
  │ Dependency ladder view                │ Module boundary understanding   │
  ├───────────────────────────────────────┼─────────────────────────────────┤
  │ Confusion resolver LLM pattern        │ Targeted explanations           │
  └───────────────────────────────────────┴─────────────────────────────────┘

  v1.2 adds: 7 endpoints (/impls, /traits, /call-chain, /compare, /cycles,
  /dead-code, /core-periphery)

  Later

  ┌─────────────────────────┬───────────────────────────────────────────────┐
  │       What ships        │                   Why later                   │
  ├─────────────────────────┼───────────────────────────────────────────────┤
  │ Architecture simulation │ High value but requires shadow graph          │
  │  (mutate → diff →       │ infrastructure and the user needs to trust    │
  │ explain)                │ the base graph first                          │
  ├─────────────────────────┼───────────────────────────────────────────────┤
  │ Ownership/borrow        │ Limited by tree-sitter's inability to verify  │
  │ pattern visualization   │ borrow semantics — syntactic only             │
  ├─────────────────────────┼───────────────────────────────────────────────┤
  │ Temporal snapshot       │ Needs multi-snapshot storage, low priority    │
  │ comparison              │ until user base exists                        │
  ├─────────────────────────┼───────────────────────────────────────────────┤
  │ Blast radius, upstream  │ Strong for power users and LLM workflows, but │
  │ trace, coupling         │  not critical for the reading companion       │
  │ analysis                │ mission — add when users graduate from        │
  │                         │ reading to analyzing                          │
  ├─────────────────────────┼───────────────────────────────────────────────┤
  │ Betweenness centrality, │ Low priority until architecture review        │
  │  bridge detection       │ workflows mature                              │
  └─────────────────────────┴───────────────────────────────────────────────┘

  ---
  13. Final Synthesis

  The single best newcomer workflow: Architecture Overview → Community Zoom →
  Read the Most Important Entity. In 30 seconds, the user goes from "I have no
  idea what this codebase is" to reading the most critical function in the most
  relevant module. No other tool provides this path.

  The best visual workflow: The architecture map with community zoom. It
  replaces folder-tree browsing with concept-level navigation. The community map
   IS the product's visual identity. If this one surface is great, the product
  feels great.

  The best LLM-guided workflow: The guided tour. A numbered reading plan with
  per-stop narration, generated from graph structure, tracking progress across
  sessions. This is the LLM acting as a senior engineer walking you through the
  codebase — not answering questions, but planning your reading.

  The most dangerous gimmick to avoid: Making the LLM explain every entity
  automatically without the user asking. Auto-generated explanations that appear
   on every click will become noise within 5 minutes. The LLM should be
  available and concise, not aggressive and verbose. Default: short annotation.
  Expand: on user request.

  The one-sentence product thesis:

  Parseltongue is a reading environment that uses graph structure to turn a
  large codebase into something that feels like an explorable, guided,
  structured book — where every page has context, every concept has neighbors,
  and a companion is ready to explain exactly what you need when you need it.

```