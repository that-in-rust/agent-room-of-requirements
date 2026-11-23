# Codebase Navigation Reference

Depth for [SKILL.md](SKILL.md): pattern catalogs, full command lists, long tables, worked examples, failure modes and evidence limits for the five tools. Script paths such as `scripts/setup_parseltongue_1_7_2.sh` are relative to this skill's directory.

## Idiomatic Thesis Synthesis Statement

Navigation tools buy option preservation. Cheap, broad evidence narrows what you read next. It does not close claims that need semantic, build, configuration, runtime, security or owner evidence.

- Rough CLI map: a disposable hypothesis generator. Its precision is bounded by the file inventory, the supported extensions, which extractor ran, the resolver heuristics, the graph cap and how the repository is wired.
- Parseltongue 1.7.2: a topology and context-narrowing instrument. The ladder is: pin and verify the version and run identity, orient globally, choose a direction-specific trace, inspect callers, callees, clusters, cycles and spread, then confirm semantics in source or at runtime.
- GitHub context capture: an evidence-preserving join across content (what was written), chronology (when) and relationships (commit to pull request, pull request to issue, discussion links, shared participants). It is not search and not summarisation. Its value is normalisation plus synthesis, because people otherwise miss commit comments, review comments outside the pull request body, timeline events and Discussions.
- Clarity: file-level structural evidence about coupling, impact, boundaries, cycles and change shape.
- Strata: a versioned store for a visual spec. It records understanding; it does not create it.

Four statements hold for all five:

1. A graph edge does not prove execution. A missing edge does not prove impossibility.
2. Non-observation is a prompt for a stronger check, never proof of absence.
3. Agreement between methods that share a blind spot is not independent confirmation.
4. A mismatch is routing information. Missing files point at inventory policy. Weak spans point at the extractor. False relations point at the resolver. Semantic disagreement points at a stronger analyser.

The four questions GitHub context answers: What changed? Who discussed it? Where was the decision made? Which thread explains why the code looks like this?

## Pattern Scoreboard Ranking Table

The order below is a dependency order: each pattern only works when the ones above it hold. It is not a measured ranking, and no numeric score is attached.

| Rank | Pattern | Failure it prevents | Applies to |
| --- | --- | --- | --- |
| 1 | Question first: one falsifiable question, one decision, the cost of a missed edge | Collecting a graph nobody needed | All |
| 2 | Lightest tool that can observe the answer | Server setup or repo-wide crawl for a one-symbol question | All |
| 3 | Identity before queries: tool version, run or binary, repository revision, dirty state | Results from the wrong version, port, host or revision | All |
| 4 | Coverage before results: inventory, parse coverage, enabled surfaces, page caps | Trusting silence from files or surfaces that were never read | All |
| 5 | Scope bounded first, widened on a named gap | Unbounded crawls and context floods | GitHub, Parseltongue, rough map |
| 6 | Full rows over projections | Decisions from a capped graph or a count-only digest | Rough map, GitHub |
| 7 | Separate surfaces and evidence classes | Flattened comment types; lexical edges read as semantic | GitHub, rough map |
| 8 | Raw output preserved at stable paths | Re-crawling; unverifiable summaries | GitHub, Parseltongue, rough map |
| 9 | Source confirmation of every claim that matters | Topology reported as behaviour | All |
| 10 | Escalate by missing capability, not by topic | Retrying the same lexical method on a semantic question | All |
| 11 | Validate before mutate, with optimistic concurrency | Lost or unrendered diagram edits | Strata |

A later step cannot repair an earlier one. Verification cannot recover a surface that was never queried or reveal a page cap that was never recorded.

## Agent Usage Decision Guide

Classify the request before running anything:

| Class | Example | Route |
| --- | --- | --- |
| Exact location | "Where is `resolve_import_target`?" | `rg` or structural search, then read. No map. Answers location only. |
| Unfamiliar-repository orientation | "What is in here?" | Rough map with coverage audit; Parseltongue orientation queries if a run is justified |
| Backward trace from a symptom | "What reaches this failing function?" | Parseltongue reverse callers, then source |
| Forward trace from a candidate change | "What does this touch?" | Parseltongue forward callees and blast radius; Clarity for file level |
| Architecture risk | "Where are the cycles and hotspots?" | Parseltongue architecture endpoints; Clarity cycles if available |
| Change-shape check | "What did my branch couple together?" | Clarity on working tree, commit or range |
| History and rationale | "Why was it built this way?" | GitHub Artifact Trace |
| Recent evolution | "What has been happening here?" | GitHub Repo Survey, bounded |
| Persisting a map | "Draw this so we can keep it" | Strata |
| Exact behaviour | "Which branch runs for this input?" | Not these tools: tests, debugger, traces |

Activation conditions for a graph tool: a stable or discoverable entity exists, the answer is structural, the run or binary is verified, and you know when you will stop and read source. A request that merely contains the word "graph" does not qualify.

Route matrix for the rough map:

| Situation | Action |
| --- | --- |
| Exact symbol or string | Direct search |
| Existing map with matching producer, root, revision, working state, options and inventory | Reuse, with checks |
| Existing map with unknown provenance | Treat as a hint, or rebuild |
| Broad orientation in supported languages | Fresh map plus coverage audit |
| Review ranking | Complete rows, state the cap, sample |
| Refactor | Authoritative consumers, build, types, tests, contracts, variants |
| Deletion or security | Stronger evidence always |
| Unsupported language or file class | Native or language-aware tool |
| Writes restricted or output ownership unclear | Do not build |

GitHub mode choice: always preflight and fix scope before querying. Survey first and then trace when you do not yet know which artifact matters. Trace directly when you do. Good: trace why commit `abc` exists. Bad: crawl the repository to answer a question about one pull request. Borderline: widen a bounded survey, but only when a named gap matters. Stop on failed auth, unknown host or repository, missing permission, or a request to mutate without authorisation. Ask one scope question, then start bounded.

Stop conditions for every route: the narrowing is decisive, the remaining uncertainty cannot change the bounded action, or an owner has been named for it. The output is a smaller decision surface, not an ever-richer graph.

## Decision Tradeoff Guide

### Rough map

| Decision | Choose when | Reject or escalate when |
| --- | --- | --- |
| Build fresh | Broad unfamiliar orientation and an authorised output location | A native index answers the question; the claim is dynamic, generated, unsupported or about security |
| Reuse | Producer, target, revision, options, capability and inventory all match | Any identity is missing or a relevant file class was excluded |
| Direct search | Narrow known string, file or symbol | The question is about consumers or blast radius |
| Native graph or build data | The project maintains its own graph | It excludes variants or conflicts with source or runtime |
| No artifact | Writes are restricted or ownership is unclear | Obtain authorisation only if the map is necessary |

Freshness has several dimensions. A rebuild fixes time. It does not fix a wrong root, an unsupported extension or a tool that cannot observe the claim. A fully identified frozen artifact can be more reproducible than a fresh run. Make a gate hard when uncertainty could authorise harm (missing language coverage before a deletion). A warning is enough when the uncertainty is visible and harmless (no SVG for a navigation task).

Extraction ladder, weakest to strongest observation:

| Method | Gives | Limit |
| --- | --- | --- |
| Regex fallback | Cheap declaration candidates | One-line spans |
| JSON Ctags | Start and end lines, kinds, scopes | No type or call resolution |
| Lexical imports | Broad candidate relations | Aliases, re-exports, dynamic wiring |
| Structural search (`ast-grep`, Tree-sitter) | Syntax-aware matches | Grammar, rule and name-resolution limits |
| Language server or semantic index | Resolved references | Depends on server, index and configuration |
| Compiler or build graph | Configured targets, features, generated state | Only the configurations built |
| Runtime trace | What actually executed | Only the paths exercised |

Evidence depth by purpose: navigation needs a pointer and source. Explanation adds coverage, both endpoints, configuration and a native check. Review prioritisation needs full rows, de-duplication, the cap and stratified samples. Refactoring needs semantic consumers, contracts, build, tests and variants. Deletion and security need high-assurance semantic, build, configuration, runtime, threat and owner evidence.

### Parseltongue

| Option | Choose when | Caution |
| --- | --- | --- |
| Adopt | Healthy run and a structural question | Confirm version, run, coverage and source support |
| Adapt | Partial coverage or partial workflow fit on a valid run | State the inference and its limits. Never adapt around a wrong version or run. |
| Avoid | Exact dynamic behaviour dominates, evidence conflicts, or setup costs more than the narrowing saves | Use direct code, language-server references, tests, tracing, logs, ownership metadata or the rough map |
| Cost of being wrong | Wrong files, tests or abstraction; false exclusion during deletion or migration | Record what to undo, what to inspect next and the safer alternative |

Weigh repository size, readiness, expected reuse, entity stability and claim type per question. The rough map is the fallback when a persistent server is not justified.

### GitHub

| Mode | Choose when | Never |
| --- | --- | --- |
| Bounded Repo Survey | Orientation | Call it exhaustive |
| Widened Survey | A named gap affects the answer, or the user asked | Ignore rate limits |
| Focused Artifact Trace | A known focal commit, pull request, issue or discussion | Infer repo-wide patterns from it |
| Quick view (`gh pr view`) | A narrow question with stated coverage limits | Persist it as an archive |
| Canonical harvest (`gh api --paginate --slurp`) | A durable list is explicitly required | Drop the page and cursor record |
| Discussion query (GraphQL) | Discussions enabled and in scope | Assume nested replies are complete |
| Raw replay | Saved JSON already answers the question | Re-crawl for it |
| Defer | Auth, permission or scope is unresolved | Guess |

Design priorities for capture, in order: read-only safety; completeness per surface through canonical list and detail endpoints; provenance; separation of conversation types; chronology; recoverability through saved raw JSON. The capture needs no third-party `gh` extension, no browser automation, no GitHub app and no local clone. There is no page cap or repository size that suits every case.

### Clarity

| Choice | Choose when |
| --- | --- |
| Mermaid output (`-f mermaid`) | The client renders Mermaid or the result goes into Markdown |
| DOT output (`-f dot`) | Graphviz tooling or programmatic parsing |
| URL output (`-u`) | A shareable browser view is wanted |
| Installed binary as is | It has the commands the task needs |
| Rebuild from newer source | The user wants newer behaviour, or a needed command is missing, and a clean worktree is available |

### Strata

| Kit | Choose when |
| --- | --- |
| `user_flow` | The map is a journey with screens, actions, decisions and outcomes |
| `discovery_tree` | The map is outcomes and nested tasks with dependencies |
| `freeform` | The map is architecture, a module graph, a data flow, a state machine or an ownership map |

Route bundles for the rough map:

| Need | Sequence |
| --- | --- |
| Quick navigation | Query, pointer, source |
| Orientation | Map, coverage, ranking, reads |
| Review | Full rows, de-duplication, cap, samples, source |
| Refactor | Candidates, authoritative consumers, contracts, checks and variants |
| Absence | Empty rough result, independent search, semantic or build or configuration or runtime evidence, owner |

Pre-action audit, for any tool: the exact claim and action; the cost of a false positive and of a false negative, and whether the action can be reversed; which source and relation classes the claim needs; which blind spots your methods share; the strongest independent counter-signal; the escalation option; and any assurance floor set by policy.

During an incident the order may change so that verification comes first. Provenance and every gate still apply.

## Theme Specific Artifact

### Rough map: Dependency Map Decision Record

A compact provenance record for one target state and one bounded decision. It points at artifacts and source; it does not copy them.

Profiles: `navigation` (identity, query, pointer, source, boundary, stop); `standard_decision` (full run identity, coverage, ranking, positive and negative samples, claim cards, project checks, invalidation); `high_assurance` (standard plus semantic, build, configuration, generated, test, runtime, owner and variant evidence). Deletion, security and absence claims cannot use the navigation profile.

```text
Record: <id>   Profile: navigation | standard_decision | high_assurance
Goal: <user goal>
Question: <one falsifiable question>   Consequence if wrong: <...>
Target: root=<path> revision=<sha> branch=<name> dirty=<yes|no>
Producer: builder hash=<sha256> options=MAX_GRAPH_EDGES=<n> out=<dir>   reader hash=<sha256>
Environment: rg=<v> ctags_json=<yes|no> ast-grep=<yes|no> dot=<yes|no>   Time: <UTC>
Coverage: inventory mode=<git ls-files | rg --files>; files=<n>; supported=<n>
  Excluded: untracked, ignored, generated, vendored, nested repos, unsupported languages, config, data
  Extractor actually used: <ctags | regex>; range quality: <multi-line | one-line>
  Graph: cap=<n>; full edges=<n>; projected edges=<n>; SVG=<present|absent>
Evidence:
  EVIDENCE-001 class=<row|source|config|test> locator=<file:start:end or row key>
    observation=<what is there, not what it implies> scope=<...> reproduce=<command>
Claims:
  CLAIM-001 "<text>" state=candidate|observed|corroborated|verified_for_scope|refuted|unresolved
    support=<evidence ids> counterevidence=<ids> owner=<who> invalidated-by=<event>
Mismatches: stage, expected, actual, hypotheses, falsification step, mechanism or "unresolved"
Verification: gate, outcome, limitation
Decision: proceed | proceed within scope | redesign | reject | escalate
Rollback: <...>   Next action: <...>   Stop condition: <...>
```

A good record names the candidate scope and the missing coverage. A bad record rests on the SVG alone, carries an unexplained percentage, omits the cap or the dirty state, or approves a deletion because no inbound arrow was drawn.

Ranking signals:

| Signal | Use | Do not conclude |
| --- | --- | --- |
| Query match | Candidate relevance | That it is the right symbol |
| Fan-in and fan-out | Order of inspection | Importance or runtime criticality |
| Neighbour overlap | Shared neighbourhood with known files | A dependency |
| Ownership and configuration (owners files, manifests, build targets, registries) | Who and what wires it | Nothing from centrality; centrality never assigns ownership |
| Tests and entry points | Separate production wiring from test helpers | Coverage |
| Graph centrality, visual density | Where to look on the picture | Architecture priority |

Import resolution in the builder: relative imports with extension, index, `__init__` and `mod.rs` candidates; Python dotted modules that contain a dot; Rust `crate::` paths, also under `src/`; Java package paths; C and C++ includes relative to the source directory or the repository root; Go import blocks. Everything else (third-party packages, path aliases, bare Python modules, Rust `mod x;`, Go module paths) lands in `external_ref_edges.tsv`. Edge kinds are `import`, `module`, `require` and `include`. With Ctags the builder asks for `--fields=+neK --extras=+q` and keeps the raw output in `ctags.jsonl`. The Mermaid file is `graph TD`; the DOT file uses left-to-right rank direction.

### Parseltongue: endpoint list

Resolve the base URL first (`source run.config`). All paths are relative to `${SERVER_URL}`. URL-encode every entity key.

| Group | Endpoint | Purpose |
| --- | --- | --- |
| Health | `/server-health-check-status` | Server up; look for `"file_watcher_active": true` |
| Health | `/file-watcher-status-check` | Watcher state and event counters |
| Orientation | `/codebase-statistics-overview-summary` | How big is this? |
| Orientation | `/folder-structure-discovery-tree` | What folders exist? |
| Orientation | `/api-reference-documentation-help` | Live endpoint and parameter list |
| Search and read | `/code-entities-list-all` (optional `?entity_type=function`) | All entities |
| Search and read | `/code-entities-search-fuzzy?q=` | Where is X? |
| Search and read | `/code-entity-detail-view?key=` | What is X? |
| Traversal | `/dependency-edges-list-all` | All edges |
| Traversal | `/reverse-callers-query-graph?entity=` | Who uses X? |
| Traversal | `/forward-callees-query-graph?entity=` | What does X use? |
| Traversal | `/blast-radius-impact-analysis?entity=&hops=` | What breaks if I change X? |
| Context | `/smart-context-token-budget?focus=&tokens=` | Packaged context for LLM work (4000 default; 8000 for refactors) |
| Architecture | `/circular-dependency-detection-scan` | Is the architecture healthy? |
| Architecture | `/strongly-connected-components-analysis` | Cycles as SCCs |
| Architecture | `/complexity-hotspots-ranking-view?top=` | Where is the complexity? |
| Architecture | `/semantic-cluster-grouping-list` | What are the modules? |
| Architecture | `/leiden-community-detection-clusters` | Community clusters |
| Architecture | `/kcore-decomposition-layering-analysis` | Core versus peripheral code |
| Architecture | `/centrality-measures-entity-ranking?method=pagerank&top=` | Central entities |
| Architecture | `/technical-debt-sqale-scoring` | Technical debt score |
| Architecture | `/entropy-complexity-measurement-scores` | Entropy scores |
| Architecture | `/coupling-cohesion-metrics-suite` | Coupling and cohesion |
| Diagnostics | `/ingestion-coverage-folder-report?depth=2` | How much was parsed? |
| Diagnostics | `/ingestion-diagnostics-coverage-report?section=summary` (also `word_coverage`, `test_entities`, `ignored_files`) | Parse quality |
| Reindex | `POST /incremental-reindex-file-update?path=src/main.rs` | Reindex one file |

Scoped variants take a `scope` parameter on list, search and blast-radius calls, for example `?scope=crates||parseltongue-core`.

`run.config` keys: `PARSELTONGUE_VERSION`, `CODEBASE_PATH`, `REQUESTED_PORT`, `PORT`, `SERVER_URL`, `DB_URI`, `WORKSPACE_PATH`, `INDEX_LOG`. Run folder layout: `bin/`, `db/`, `logs/` (`index.log`, `server.log`), `queries/`, `run.config`, `server.pid`. Entity keys look like `language:kind:name:___path_slug:T<digits>`, for example `typescript:fn:alphaProbeFunction:___..._sample:T1597380345`.

What the bundled scripts do:

- Setup downloads the release asset for the platform from the `that-in-rust/parseltongue-rust-LLM-companion` repository, tag `v1.7.2`. It needs `curl`, `python3` and common shell utilities; `jq` is optional and used only by the smoke queries.
- The codebase slug in the folder name is lower-cased, non-alphanumeric characters become `-`, and it is cut at 40 characters.
- Indexing runs `pt01-folder-to-cozodb-streamer <codebase>` from inside the run folder, without a database flag. The database URI is taken from the `rocksdb:` line in `logs/index.log`, and the workspace is checked for a manifest file.
- The server runs `pt08-http-code-query-server --db <uri> --port <port>` detached, with the codebase as its working directory. The script reads the bound URL from `logs/server.log` (waiting up to 30 seconds), then waits up to 20 seconds for health.
- Smoke queries: health and statistics must succeed. Watcher status, folder tree, blast radius and smart context on the first listed entity key are optional and may fail without failing setup. A warning is printed when `"file_watcher_active":true` is absent.
- Cleanup removes `parseltongue-1.7.2-*` folders older than the cleanup age from the base directory.
- Reindex reads `run.config`, checks the version, stops the server through `server.pid`, deletes the workspace only when it lies inside the run folder, indexes again, restarts, runs health, statistics and watcher queries, and rewrites `run.config`.
- Stop reads `server.pid`, kills the process and removes the file. It reports when the process was already gone and fails when the file is missing.
- Each event is appended to the central log as `<UTC timestamp> | EVENT key='value' ...` with events `SETUP_START`, `SETUP_COMPLETE`, `REINDEX_START`, `REINDEX_COMPLETE`, `SERVER_HEALTH_OK` and `QUERY`.

`smart-context-token-budget` is available in 1.7.2. How well it selects context for a given question is not established; check what it returns.

When live edits do not appear:

1. Check `/server-health-check-status` for `"file_watcher_active": true`.
2. Check `/file-watcher-status-check` for state and counters.
3. Read `logs/index.log` and `logs/server.log` in the run folder.
4. If the watcher is inactive, the URL is stale or the workspace is suspect, run `scripts/reindex_parseltongue_1_7_2.sh <run-folder>` and reload `run.config`.
5. If it is still unclear, make a small code edit and search for the new symbol with `/code-entities-search-fuzzy`.

### Parseltongue: thirteen combined workflows

Legend: S = fuzzy search, D = detail view, R = reverse callers, F = forward callees, B2 or B3 = blast radius at 2 or 3 hops, C4 or C8 = smart context at 4000 or 8000 tokens, CYC = cycle scan, SCC = strongly connected components, HOT = hotspots (top 20), PR = PageRank centrality, CL = semantic clusters, TREE = folder tree, KC = k-core, CC = coupling and cohesion, COV = coverage report, DIAG = diagnostics summary and ignored files.

| # | Workflow | Use when | Query sequence | How to read the result |
| --- | --- | --- | --- | --- |
| 1 | Meet-in-the-middle hypothesis test | You have a suspected cause and a visible symptom and do not know whether they connect | S symptom, R symptom; S suspect, F suspect; B2 on both | Shared mid-layer entities strengthen the hypothesis. Disjoint sets weaken it: look for another trigger or cause. |
| 2 | Symptom-to-system corridor | A local bug may span entry points, orchestration and helpers | S, D, R, F, B3, C8 | Callers expose upstream triggers. Callees expose sinks and collaborators. Blast radius says local, layered or systemic. |
| 3 | Change choreography | Replace, deprecate, rename or re-contract an entity without breaking dependents | D, R, F, B3, C8 | Callers are migration sites. Callees are hidden implementation coupling. Phase order: stabilise downstream, update a small caller slice, reindex and re-query, expand. |
| 4 | Narrow-waist seam discovery | Extract an interface or find the waist between many callers and a bounded dependency set | HOT, PR, R, F, C8 | Good seams have substantial inbound pressure, bounded outbound spread and clear local context. A chaotic forward graph is an unstable seam. |
| 5 | Boundary-leak detector | A module boundary seems to leak across layers or clusters | CL, TREE, R, F, CYC, SCC | Callers from unexpected modules are inbound leaks. Callees into unexpected modules are outbound leaks. Cycle evidence raises urgency. |
| 6 | Cycle-breaker scout | Cycles exist and you need the least painful cut | CYC, SCC, KC, R, F | Prefer nodes with fewer callers, tighter dependency sets and lower core-ness. High-pressure central nodes are usually hubs, not accidents. |
| 7 | Deletion-safety classifier | Is an entity removable, obscure or critical? | R, F, B2, PR (top 50) | Low usage, low spread, low centrality: deletion might be safe. Low usage with high forward spread: hidden glue, not dead code. High usage or blast radius: do not delete casually. |
| 8 | Hotspot pressure-versus-sink split | A hotspot hurts and you do not know whether demand or entanglement is the cause | HOT, CC, R, F | Heavy reverse pressure: consolidate callers. Heavy forward spread: reduce dependencies. |
| 9 | Parse-frontier probe | Reasoning near low-coverage or partly parsed areas | COV, DIAG, R, F | Strong evidence inside well-covered zones, partial near the frontier. Read files directly where the corridor enters ignored or low-coverage code. |
| 10 | Ownership and review router | Decide who should review or own a change | R, F, CL, C4 | Callers often reveal product-facing or API owners. Callees often reveal infrastructure, storage or platform reviewers. Confirm against ownership files. |
| 11 | Source-to-sink convergence | Test whether a likely source and a likely sink share a corridor | S source, F source; S sink, R sink; CL; C8 on source | Overlap in the same middle entities or clusters supports the corridor. No meeting means a wrong guess or a segment in dynamic or low-coverage code. |
| 12 | Sink-to-source accountability | Start from a write, publish or log and find who can trigger it | D sink, R sink, B3 sink, CL, C8 on sink | Callers are the initiators. Blast radius separates one local write path from a shared sink. Cluster spread routes the review. |
| 13 | Orchestrator split planner | One node coordinates too many scenarios | R, F, HOT, CL, C8 | Callers in a few clusters: split by upstream scenario. Callees in a few domains: split by downstream responsibility. Both chaotic: stabilise the boundary first. |

### Parseltongue: twelve flow patterns

Graph-derived approximations of control flow and data flow, for questions such as "where does the data actually go?". ENT = entropy scores, EDGES = all dependency edges; other codes as above.

| # | Pattern | Use when | Query sequence | How to read the result |
| --- | --- | --- | --- | --- |
| 1 | Ingress-to-sink corridor | You know an entry point, handler, command, job runner or adapter and want the path to storage, publishing or network sinks | S entry, F, B3, CL, C8 | A forward path that crosses clusters and ends near sinks approximates the corridor. Local spread means a thin adapter; orchestration sits one layer deeper. |
| 2 | Gatekeeper choke point | Find the narrow node many flows pass: auth, validation, policy, routing glue | PR, R, F, B2 | High inbound pressure, bounded outbound spread, high centrality. Wide multi-cluster outbound spread means an orchestrator instead. |
| 3 | Orchestrator versus leaf worker | Is this entity coordinating or doing one step? | R, F, HOT, CC, CL | Orchestrators show inbound usage, multi-cluster outbound spread, raised coupling. Leaf workers show bounded reach, one cluster, low blast radius. |
| 4 | Branch-hub suspicion | A function looks like a dispatcher, strategy switch or mode router | F, ENT, HOT, C4 | Wide fan-out plus entropy or hotspot evidence suggests branch-heavy logic. Read the code for the conditions; the graph cannot say which branch runs. |
| 5 | Feedback loop and re-entry | Flow seems to re-enter a prior layer | CYC, SCC, KC, R, F | SCC membership with pressure on both sides suggests re-entry. Lower-core nodes are easier break points. A graph cycle is not a runtime loop. |
| 6 | Source-to-sink convergence | Do a source and a sink share a data corridor? | S source, F source; S sink, R sink; B3 on both | Convergence on the same middle entities strengthens the lineage. Disjoint results suggest another route or an unparsed dynamic path. |
| 7 | Sink-to-source accountability | Start from a side effect and find plausible initiators | S sink, D sink, R sink, CL, C8 | Callers can cause the effect. Callers from different clusters are often distinct business flows sharing one sink. |
| 8 | Transformer ladder | Suspected chain of parse, validate, normalise, map, enrich, persist | S `map`, S `transform`, S `normalize`; R, F, CL | A bounded chain crossing a few layers in sequence approximates a ladder. Extreme inbound use from unrelated areas means shared utility code. |
| 9 | Payload gravity well | Find the models or payload types many flows orbit | PR (top 50), EDGES, R, F, B2 | High centrality with strong attachment both ways. Changes there are schema or contract changes in disguise. |
| 10 | Boundary-crossing lineage | Describe movement across API, domain and persistence | CL, TREE, F source, R sink, C8 | Each cluster or folder transition approximates a boundary crossing. Jumps across unrelated clusters suggest leakage or misplaced responsibility. |
| 11 | Normaliser funnel | Find the parse or validation step many inputs converge through | R, F, CC, C4 | Many callers with a small stable downstream set. Often the safest place to enforce invariants once the code confirms it. |
| 12 | Parse-frontier caution | The corridor may cross files the graph did not parse | COV, DIAG, F, R | Stop making strong flow claims where coverage is low and verify in code. |

### Parseltongue: graph investigation packet

Required for change, deletion, risk and debugging claims. A lighter orientation packet is fine for disposable exploration.

```text
Question and claim class: orientation | backward trace | forward trace | architecture risk | context selection
Run: version=1.7.2 folder=<run> SERVER_URL=<url> DB_URI=<uri> workspace=<path> code revision=<sha>
Health: server=<ok> watcher=<state> log evidence=<line>
Orientation: entity and edge counts, cycles present, top hotspots
Coverage: folders below expectation, ignored files that matter
Entity resolution: search term -> candidates -> chosen key (why)
Queries, in order: <endpoint and parameters> -> <summary of the response, including empty results>
Source confirmations: <file:start:end> confirms or refutes <graph claim>
Negative evidence and its coverage limit
Uncertainty, alternatives considered, stop or refresh decision
```

Do not submit raw transcripts or screenshots alone, drop the URL or keys, lose query order, or paste large JSON. The packet must replay from a clean shell against the named run.

### GitHub: surface matrix

| Surface | Preferred path | Why |
| --- | --- | --- |
| Repository metadata | `gh repo view --json ...` | Capability and visibility check |
| Default-branch commit history | `gh api repos/{owner}/{repo}/commits?...` | Canonical list |
| Commit detail | `gh api repos/{owner}/{repo}/commits/<sha>` | Metadata and stats |
| Commit comments | `repos/{owner}/{repo}/commits/<sha>/comments`, or repo-wide `repos/{owner}/{repo}/comments` | Separate from issue and review comments |
| Commit to pull request | `repos/{owner}/{repo}/commits/<sha>/pulls` | Best bridge from code to review thread |
| Pull request quick read | `gh pr view <n> --json ...` | Focused structured summary |
| Pull request list | `repos/{owner}/{repo}/pulls?state=all...` | Full pagination |
| Review comments | `repos/{owner}/{repo}/pulls/<n>/comments`, or repo-wide `repos/{owner}/{repo}/pulls/comments` | The code-review layer |
| Reviews | `repos/{owner}/{repo}/pulls/<n>/reviews` | Review state and summary comments |
| Issue quick read | `gh issue view <n> --json ...` | Focused structured summary |
| Issue or pull request timeline | `repos/{owner}/{repo}/issues/<n>/timeline` | State changes and chronology |
| Issue comments | `repos/{owner}/{repo}/issues/comments`, or `gh issue view --json comments` | Thread comments, not review comments |
| Discussions | `gh api graphql` | No first-class `gh` command |

### GitHub: Discussions queries

Repo-wide index, for discovery:

```graphql
query($owner: String!, $name: String!, $endCursor: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 100, after: $endCursor, orderBy: {field: UPDATED_AT, direction: DESC}) {
      nodes {
        number title url createdAt updatedAt answerChosenAt
        category { name }
        author { login }
        comments { totalCount }
      }
      pageInfo { hasNextPage endCursor }
    }
  }
}
```

One thread, for explanation:

```graphql
query($owner: String!, $name: String!, $number: Int!, $endCursor: String) {
  repository(owner: $owner, name: $name) {
    discussion(number: $number) {
      number title body url createdAt updatedAt answerChosenAt
      category { name }
      author { login }
      comments(first: 100, after: $endCursor) {
        nodes {
          id body createdAt updatedAt url isAnswer
          author { login }
          replyTo { id }
          replies(first: 100) {
            totalCount
            nodes { id body createdAt updatedAt url isAnswer author { login } replyTo { id } }
          }
        }
        pageInfo { hasNextPage endCursor }
      }
    }
  }
}
```

Run either with pagination and saved output:

```bash
gh api graphql --paginate --slurp -F owner=OWNER -F name=REPO -F number=42 -f query="$(cat thread.graphql)" > discussion_thread.json
```

`--paginate` follows only the connection tied to `$endCursor`. Compare each `replies.totalCount` with the number of reply nodes returned; a larger total means truncation.

### GitHub: capture package

What the bundled collectors write:

| Collector | Files |
| --- | --- |
| `scripts/collect_repo_context.sh` | `raw/repo.json`, `raw/commits.json` (default branch, optional `--since`), `raw/pulls.json` (all states, by update time), `raw/issues_and_pull_requests.json`, `raw/issue_comments.json`, `raw/review_comments.json`, `raw/commit_comments.json`, `raw/discussions_index.json` (only when enabled and not `--no-discussions`), `manifest.json` |
| `scripts/collect_artifact_context.sh --kind pr` | `pr.json`, `timeline.json`, `review_comments.json`, `reviews.json`, manifest |
| `--kind issue` | `issue.json`, `timeline.json`, manifest |
| `--kind commit` | `commit.json`, `commit_comments.json`, `associated_pulls.json`, manifest |
| `--kind discussion` | `discussion_thread.json`, manifest |

The repo manifest records capture type, repository, default branch, collection time, since filter, page cap and Discussions state. Pages are stored as an array of pages. Collection stops at the first empty page or at the page cap; with 100 items per page the default cap of 5 pages means at most 500 items per surface. The artifact collector paginates without a cap. The renderer reads the manifest, counts each surface, separates issues from pull requests by the `pull_request` key and lists the first ten commits, eight pull requests and six discussions.

Typical uses of a capture: onboarding to a repository, reconstructing design history, tracing a regression back to its discussion, explaining why a pull request merged the way it did, finding the discussion threads linked to a commit, and producing a source-backed digest for an incident or architecture review.

A complete package holds: repository and host, mode, scope, collection time, filters and page caps, capabilities, surfaces and endpoints, page and cursor results, raw JSON manifest, relationship links, the digest, source URLs, gaps, permissions and rerun instructions. Keep collection immutable and synthesis revisable. Failures to avoid: Markdown without raw files, several surfaces in one raw file, missing caps or timestamps, overwritten paths, mixed hosts, leaked credentials. A focused trace may keep a single raw pull request file if its limits are stated.

### Clarity: newer-only features

Use only after `--help` confirms them:

- `clarity modules`: lists modules declared in `.clarity/modules.json` with file counts.
- `clarity cycles [path...]`: lists circular file dependencies; `-u` can emit URLs.
- `clarity show --reach up|down|both`: walks dependencies from an anchor; `--depth <n>` bounds the walk.
- `clarity show --all --collapse`: renders the whole tree collapsed into declared modules.
- `clarity show --module <name>`: renders a declared module in context.
- `clarity show --prune <path>`: shows a node and skips its subtree.
- `clarity show --also <glob>`: adds matching files that connect to the reach graph.

Recorded version evidence: installed binary `clarity version 0.19.2`, commit `eb4eba6`, built 2026-05-07; newer source at `origin/main` commit `99bc1f2`, pushed 2026-07-08. A build of the newer source was not completed because Go was not installed, so the newer flags above come from documentation.

Questions a Clarity summary answers: Which files or modules are central? Which edges cross expected boundaries? Are tests or docs connected to the changed production files? Are cycles present? Is the graph too broad because the command lacked a tight anchor? Which Clarity limits matter for the conclusion?

### Strata: MCP tools

Recorded for Strata 0.9.0 build 29 (bundle `com.legacycode.strata`, MCP protocol `2024-11-05`), nineteen tools:

| Tool | Use |
| --- | --- |
| `get_diagram` | Name, current D2 source, version, render status |
| `update_diagram` | Replace the full source after compile; pass `base_version` |
| `validate_diagram` | Dry-run compile for `freeform`, `user_flow` or `discovery_tree` |
| `describe_kit` | Grammar, vocabulary, statuses, directives, examples |
| `list_versions` | Snapshots, newest first |
| `get_version` | Source of one version |
| `restore_version` | Make an old snapshot current by creating a new snapshot |
| `diff_versions` | Unified diff between versions, or a version and current |
| `list_projects`, `create_project` | Projects |
| `list_diagrams`, `create_diagram` | Diagrams in a project; create optionally in a group |
| `rename_diagram` | Rename without touching source or history |
| `list_groups`, `create_group`, `rename_group` | Flat groups |
| `move_diagram` | Move to a group or to ungrouped |
| `delete_diagram` | Delete diagram and history; irreversible |
| `delete_group` | Delete a group, diagrams become ungrouped; irreversible over MCP |

Recorded smoke test on that version: `initialize` returned server `strata` 0.9.0 with `tools.listChanged` false; a create call returned `project_id`, `diagram_id`, `diagram_name`, `kit` and `version` 1; `get_diagram` then showed `render_ok` true. The server binds 127.0.0.1 only and stores specs in a local SQLite database.

The bundled scripts speak raw JSON-RPC over HTTP POST and accept both plain JSON and event-stream framed responses. `scripts/strata_mcp_probe.py` calls `initialize`, `tools/list`, `list_projects` and optionally `describe_kit`, with a 10 second timeout. `scripts/strata_mcp_tool.py` makes one `tools/call` with a 20 second timeout and prints the tool's JSON result, or the whole response with `--raw`.

Agent configuration for a Streamable HTTP server:

```toml
[mcp_servers.strata]
url = "http://127.0.0.1:7337/mcp"
```

If the agent platform lets a skill declare MCP dependencies, declare `strata` with transport `streamable_http` and the same URL. The recorded setup allowed the skill to be invoked implicitly.

### Strata: kit grammars

`describe_kit` is the live grammar. The following was recorded for 0.9.0.

`user_flow`:

```d2
@direction down

start open: Open app

screen home: Home
  action create: Click create
  decision has_data: Has required data?

system save: Save draft
end done success: Draft created
end blocked error: Missing data

open -> home
home -> create
create -> has_data
has_data -> save: yes
has_data -> blocked: no
save -> done
```

| Token | Meaning |
| --- | --- |
| `start` | Entry point: an email, deep link, browser or command |
| `screen` | Full page or screen; can contain indented actions and decisions |
| `surface` | Region within a screen: modal, panel, dialog |
| `action` | User action, usually indented under a screen or surface |
| `decision` | Branch point; label outgoing edges with the answers |
| `system` | Backend step with no UI |
| `connector` | Junction that merges or splits flow |
| `end` | Outcome: `success`, `drop-off` or `error`; default `success` |

Directives: `@direction down | left | right | up` on the first line (default down). `@status { <path>: building | verified }` highlights progress; unlisted paths are backlog. Rules: one node per line as `<type> <id>: <label>`; short unique IDs; edges on their own lines as `from -> to: optional label`; `#` for comments.

`discovery_tree`:

```d2
# Top-level bullets are outcomes. Nested bullets are tasks.
- Replace transactional email provider
  - done: Prove org invite email via new provider ^org-invite
  - doing: Improve email copy
  - Build durable outbox blocked-by ^org-invite
```

Rules: one item per line as `<indent>- [status:] label [^handle] [blocked-by ^id]`. Top-level bullets are outcomes and carry no status. Indent two spaces. Statuses: todo by default, `doing:`, `done:`. Parents derive status from children. `^handle` names an anchor; `blocked-by ^id` points at one.

`freeform` is raw D2. A module map drawn from another tool's findings:

```d2
direction: right

gateway: API gateway
email_port: TransactionalEmailSender
adapter: ProviderEmailAdapter
provider: Email provider API

gateway -> email_port: EmailIntent
email_port -> adapter: send()
adapter -> provider: HTTPS
```

If the syntax fails, `validate_diagram` returns line and column.

## Worked Example Set

Rough map:

1. Direct location. The request is "where is `resolve_import_target`?". Search, read the source, answer. No map. This establishes location, not callers or dynamic use.
2. Fallback orientation. Ctags JSON is unavailable, so `symbols.tsv` rows have `kind=regex` and equal start and end lines. Use the rows as candidates, open more of the file, and inspect the manifest, build file, startup code and test helpers. The fallback lowers range confidence; it does not remove the need to read.
3. Alias. `@core/registry` appears in `external_ref_edges.tsv`. The project configuration maps it to an internal directory. Classify it as internal only after reading that configuration.
4. Cap. The TSV has more edge rows than the Mermaid file shows. Rank from the TSV, state `MAX_GRAPH_EDGES`, and check for duplicates.
5. Stale pointer. A saved range is still readable after edits and now covers a neighbouring helper. Search by qualified name, regenerate, and read current source.
6. Dynamic registration. A handler is in the inventory. The YAML registry that wires it is not. No inbound static row plus runtime or configuration use blocks deletion. One positive counterexample defeats a claim of absence.

Parseltongue:

- Good: a regression appears at `serialize_result`. Take its reverse callers, take the forward callees of a suspected normaliser, inspect the overlap, read the source there, and reject or keep the branch hypothesis.
- Bad: delete a symbol because reverse callers came back empty. Also bad: use fan-out to explain a runtime value.
- Borderline: route reviewers from cluster and fan-in evidence, then verify against `CODEOWNERS`. Runtime proof may be skipped only for a claim declared as topology-only.

GitHub, one regression question answered three ways:

- Good: link the regression commit to its pull request, the reviews, the linked issue and the timeline, cite raw paths and URLs, and state that Discussions were disabled.
- Bad: search commits and summarise the first hit. Or dump commit messages.
- Borderline: a page-capped survey that states its limits and names the extra page or surface that could overturn the explanation.

A reviewer of any of these should be able to name the mode, scope, surfaces, omissions, relationship evidence, chronology and raw paths.

Clarity: before committing a refactor, run `clarity show -f mermaid` on the working tree. The graph shows a changed service file with a new edge into a storage adapter and no connected test file. Report the command and version, the new cross-boundary edge and the missing test neighbour as findings to check, then run the tests.

Strata: after a meet-in-the-middle trace, draw the confirmed corridor as a `freeform` diagram. Validate, create, read back `render_ok: true`, and report the diagram name and version. When the corridor changes, read the version, update with `base_version`, and add a message.

Turn an example into a regression fixture only when the failure recurs, is deterministic, is safe to represent, and protects a consequential branch.

## User Journey Scenario

A workshop-sized journey through a large unfamiliar repository:

1. Frame. "I must change how orders are serialised. I need the entry points, the consumers, and the reason the current format exists."
2. Orient with the rough map. Build it outside the repository. Read `tooling.tsv`: Ctags JSON is absent, so spans are one-line. Read `summary.md` for fan-in and fan-out. Note that the Kotlin module is invisible because its extension is unsupported.
3. Find candidates. Search `symbols.tsv` for `serialize`. Read three spans with the pointer reader. Expand through `internal_file_edges.tsv`.
4. Decide a graph run is worth it, because several caller questions will follow. Set up Parseltongue. Load `run.config`; the server bound port 7778, not 7777. Run orientation. Coverage is low for one generated folder.
5. Trace. Resolve the entity by search. Reverse callers: 9 direct callers, which suggests a medium amount of reading and testing. Blast radius at two hops. Read the narrowed files. One caller sits in the low-coverage folder, so read it directly.
6. Ask why. Find the commit that introduced the format with `git log` or the rough pointers, then run an Artifact Trace for that commit: associated pull request, review comments, linked issue. The review thread records a compatibility constraint.
7. Check the change shape. After editing, run Clarity on the working tree. Confirm with live help which flag style the binary accepts.
8. Keep the map. Draw the corridor and the constraint in Strata as a `freeform` diagram. Validate, create, confirm `render_ok`.
9. Report with the output contract: candidates, verified edges, the Kotlin and generated-code gaps, the compatibility constraint with its URL, and the next check (tests for the nine callers).

Shorter journeys:

- Locate one function: search, disambiguate duplicates, read. No map.
- Saved pointer after edits: reject blind reuse; bind to the revision, search by qualified name, regenerate.
- Dynamic handler deletion: no inbound lexical edge cannot authorise removal; check configuration, generated registries and runtime integration.
- Review ranking: rank complete TSV rows, state the cap, de-duplicate and sample.
- Operational symptom: logs and failing tests first, structure second.
- Parsing fails for the area of interest: ask for a stable symbol or file boundary, or read directly.
- GitHub credentials unavailable or a surface inaccessible: narrow to an accessible artifact, reuse a prior capture, give a conditional digest, or list the evidence still needed.

## Anti Pattern Registry Table

| Tool | Anti-pattern | What goes wrong | Do instead |
| --- | --- | --- | --- |
| Rough map | Tracked-only inventory assumed complete | Untracked, ignored and generated code is missing | Compare with the working tree; state the inventory mode |
| Rough map | Finite extension list treated as all code | Kotlin, Ruby, Swift and others vanish | Name unsupported languages; use a native tool |
| Rough map | Tool availability treated as use | `ast-grep` is detected and never invoked | Track detected, invoked, succeeded, contributed |
| Rough map | Any `ctags` treated as JSON-capable | Probe fails, regex fallback runs unnoticed | Run the JSON probe; read the `kind` column |
| Rough map | Fallback start equals end read as a full definition | One line taken for a body | Open more of the file |
| Rough map | Symbol name treated as identity | Overloads, scopes and tests collapse | Keep path and range |
| Rough map | Lexical edge treated as semantic dependency | False relation | Read both endpoints and configuration |
| Rough map | `external_ref_edges.tsv` read as third-party inventory | Aliases misclassified | Classify unresolved references |
| Rough map | Missing edge read as no dependency | False exclusion | Independent search, then semantic or runtime evidence |
| Rough map | Rendered graph read as the full artifact | Capped edges dropped | Use TSV rows; state the cap |
| Rough map | Visual density read as centrality | Wrong priorities | Rank with ownership, tests and entry points |
| Rough map | Stale pointer reused | Wrong lines edited | Regenerate after edits |
| Rough map | Colon path passed as a combined pointer | Wrong split | Three-argument form |
| Rough map | Whole repository dumped first | Context flooded | Pointer, then source |
| Rough map | Output without provenance | Not reproducible | Record command, root, revision, options |
| Rough map | Regex patched to answer a semantic or runtime claim | False precision | Escalate to a stronger tool |
| Parseltongue | Wrong version or run; stale or low-coverage graph | Answers about another snapshot | Source `run.config`; check URL, health, diagnostics, coverage; refresh or rebuild |
| Parseltongue | Ambiguous or obsolete entity key | Wrong entity or 404 | Search, disambiguate with the full key, re-resolve after reindex |
| Parseltongue | Topology treated as execution; cycles as runtime loops; fan-in as severity | Category error | Narrow the claim; read source; add tests or tracing |
| Parseltongue | Oversized context, or context with no governing question | Noise | Lower depth and token budget; keep empty results and uncertainty |
| Parseltongue | Caller-count heuristics used as approval | Unsafe change | Use them to size reading and testing only |
| GitHub | One-command mythology | Surfaces missed | Model capture as multi-surface |
| GitHub | Search used as archive | Incomplete history | Canonical list endpoints |
| GitHub | Flattened comments | Review layer lost; consensus overstated | One file and one label per surface |
| GitHub | Issue and pull request endpoints confused | Pull requests counted as issues | Filter on `pull_request` |
| GitHub | Discussions assumed | Errors or silent gap | Check `hasDiscussionsEnabled` |
| GitHub | Hidden page cap; unlimited pagination by default | False completeness, or rate-limit exhaustion | State the cap; widen deliberately |
| GitHub | Repo-wide timeline harvesting | Cost without benefit | Timelines per artifact |
| GitHub | Rendering before capture finishes; raw data lost | Unreplayable digest | Capture, save, then render |
| GitHub | Website scraping; mutation by default | Fragile and unsafe | CLI and APIs; read-only |
| GitHub | Stale snippets or generic examples as proof | Wrong on previews, Enterprise hosts, CLI drift, deprecated fields | Current official docs, then a live check |
| Clarity | Flag copied without checking help | Command fails or means something else | Probe first |
| Clarity | "Clarity proves behaviour" | Overclaim | "Shows structural coupling or impact" |
| Clarity | Pull or rebuild in a dirty checkout | User work at risk | Clean worktree or temporary clone |
| Clarity | `clarity setup` run unasked | `AGENTS.md` rewritten | Only on request; review the diff |
| Strata | Used for dependency analysis | No analysis happens | Discover with another tool, then draw |
| Strata | Update without `base_version` | Stale overwrite | Read, pass version, retry on conflict |
| Strata | Edit claimed without confirmation | Unsaved change reported as saved | Require `render_ok: true` or a success response |
| Strata | Delete without confirmation; SQLite edited by hand | History lost; state corrupted | Ask first; MCP only |
| Strata | Wrong product | Unrelated tool | Only the Legacy Code Labs macOS app |

The most dangerous failure in every tool is the silent category error: structure reported as behaviour.

## Verification Gate Command Set

Each gate has a narrow contract. Syntax checks prove parsing. Non-empty files prove emission. Headers prove structure. A pointer read proves a readable range. Sampled edges prove the samples. Project checks prove the configurations exercised.

Rough map:

```bash
bash -n "$SKILL_DIR/scripts/build_rough_codebase_map.sh" && bash -n "$SKILL_DIR/scripts/read_code_span_pointer.sh"
command -v bash python3 rg
ctags --output-format=json -f - /dev/null >/dev/null 2>&1 && echo ctags_json=yes || echo ctags_json=no

: "${REPO_ROOT:?}"; : "${OUT_DIR:?}"; test -d "$REPO_ROOT"; test ! -e "$OUT_DIR"
MAX_GRAPH_EDGES="${MAX_GRAPH_EDGES:-160}" bash "$SKILL_DIR/scripts/build_rough_codebase_map.sh" "$REPO_ROOT" "$OUT_DIR"

for f in summary.md tooling.tsv all_files.txt code_files.txt files.tsv symbols.tsv import_edges.tsv internal_file_edges.tsv external_ref_edges.tsv dependency_graph.mmd dependency_graph.dot; do test -s "$OUT_DIR/$f" || echo "MISSING $f"; done
head -n 1 "$OUT_DIR/files.tsv" "$OUT_DIR/symbols.tsv" "$OUT_DIR/tooling.tsv"
awk -F'\t' 'NF!=6 {print "bad width line " NR}' "$OUT_DIR/symbols.tsv" | head
awk -F'\t' 'NR>1 {k[$5]++} END {for (x in k) print x, k[x]}' "$OUT_DIR/symbols.tsv"
test -e "$OUT_DIR/ctags.jsonl" && wc -c "$OUT_DIR/ctags.jsonl"
grep -q '^dot.yes' "$OUT_DIR/tooling.tsv" && test -s "$OUT_DIR/dependency_graph.svg"
wc -l "$OUT_DIR/code_files.txt" "$OUT_DIR/files.tsv"
( cd "$REPO_ROOT" && git ls-files | wc -l ); wc -l "$OUT_DIR/all_files.txt"
wc -l "$OUT_DIR/import_edges.tsv" "$OUT_DIR/internal_file_edges.tsv" "$OUT_DIR/external_ref_edges.tsv"
grep -c -- '-->' "$OUT_DIR/dependency_graph.mmd"
```

Then: reconcile `code_files.txt` with `files.tsv`; investigate zero line counts; sample pointers across language, extractor, multi-line shape, duplicate names and decision importance, using separate arguments and context, and confirm the construct; sample internal and unresolved edges and read the source line, the target, aliases, re-exports and configuration; search independently for any suspicious absence; compare the graph edge count with the cap. Add negative fixtures (an untracked file, an unsupported extension, an alias, a graph above the cap, a reversed and an out-of-range pointer, a runtime registry), or the gates may pass without testing anything. A fixture cannot prove recall on a real repository. Keep the command, root, revision, status, cap, script hash, timestamps and exit status.

Triage order when something looks wrong: run identity and output directory; inventory; actual symbol producer and pointer quality; raw, internal and unresolved relations; full rows against projections; sampled source; whether this kind of observation can answer the claim at all.

Parseltongue:

```bash
source "$RUN/run.config"; echo "$PARSELTONGUE_VERSION $SERVER_URL $DB_URI $WORKSPACE_PATH"
"$RUN"/bin/parseltongue --version 2>/dev/null || ls "$RUN/bin"
curl -fsS "${SERVER_URL}/server-health-check-status"
curl -fsS "${SERVER_URL}/file-watcher-status-check"
curl -fsS "${SERVER_URL}/ingestion-coverage-folder-report?depth=2"
curl -fsS "${SERVER_URL}/ingestion-diagnostics-coverage-report?section=summary"
grep -Eo 'http://localhost:[0-9]+' "$RUN/logs/server.log" | tail -n 1
curl -sS -o /dev/null -w '%{http_code}\n' "${SERVER_URL}/code-entity-detail-view?key=${KEY}"
```

Health is not coverage. HTTP 200 is not interpretation. Index failures call for refresh or rebuild, endpoint failures for the server log and live API help, semantic doubts for code, tests and traces. Record command, working directory, exit status, version output, URL, DB URI, coverage, entity keys, response counts and the source spans read.

GitHub:

```bash
gh auth status --active
gh repo view owner/repo --json nameWithOwner,hasDiscussionsEnabled,isPrivate,visibility,url
python3 -c 'import json,sys; m=json.load(open(sys.argv[1])); print(m)' "$CAP/survey/manifest.json"
for f in "$CAP"/survey/raw/*.json; do python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(sys.argv[1], len(d) if isinstance(d, list) else "object")' "$f"; done
python3 "$SKILL_DIR/scripts/render_repo_context_digest.py" --input-dir "$CAP/survey" --output "$CAP/survey/digest.md"
grep -c '^## ' "$CAP/survey/digest.md"
gh api rate_limit --jq '.resources.core'
```

Test four cases before relying on the workflow: a survey of a public repository, a focused trace of at least one pull request or issue, digest rendering from real output, and clean degradation when Discussions are disabled. If the page count for a surface equals the cap, treat that surface as truncated. Failure cases worth exercising: broken auth or private access, page-cap exhaustion, issue and pull request filtering, comment separation, disabled Discussions, nested-reply overflow, missing raw files, and an attempted mutation. Re-render from saved JSON to separate renderer defects from collection defects. Confirm that no mutating command was run. A single pass cannot prove API coverage, and fixture tests prove formatting, not live permissions.

Clarity:

```bash
"$SKILL_DIR/scripts/probe_clarity.sh"
git status --short --branch
clarity show --help | grep -E -- '--reach|--between|-p,|-w,|-i,' || true
clarity languages
```

Strata:

```bash
lsof -nP -iTCP:7337 -sTCP:LISTEN
"$SKILL_DIR/scripts/strata_mcp_probe.py" --kits
"$SKILL_DIR/scripts/strata_mcp_tool.py" validate_diagram --args-json '{"kit":"user_flow","source":"@direction down\n\nstart s: Start\nscreen page: Page\nend e success: Done\ns -> page\npage -> e"}'
"$SKILL_DIR/scripts/strata_mcp_tool.py" get_diagram --args-json '{"diagram_id":"DIAGRAM_ID"}'
```

Finally run the project's formatter, type checker, build and tests. Do not average a disagreement between them and a map, and do not prefer the prettier output.

## Failure Mode Table

Rough map:

| Failure | Signal | Response |
| --- | --- | --- |
| `rg` missing, or only unsupported or untracked files | Builder exits 1 | Install nothing unasked; use a native tool or direct reads |
| Tracked-only, unsupported or configuration files omitted | `all_files.txt` smaller than the tree | State the gap; add direct search |
| Unreadable file | Zero line count in `files.tsv` | Investigate; do not treat as empty |
| Ctags JSON probe fails | `ctags no` in `tooling.tsv`; `kind=regex` rows | Accept one-line spans; read wider |
| Probe passes, Ctags output empty | Fallback rows despite `ctags yes` | Check `ctags.jsonl` size |
| Malformed non-empty Ctags output | Header-only `symbols.tsv` | Rerun without Ctags on the path, or fix Ctags |
| Legitimately header-only symbols | No declarations matched | Confirm with direct search |
| Multi-line or unusual import missed | Edge absent | Independent search |
| False lexical relation | Edge to a file that is not imported | Read both ends |
| Alias left unresolved | Row in `external_ref_edges.tsv` | Read project configuration |
| No internal rows | Graph drawn from unresolved references | Do not read it as internal structure |
| Cap hides edges | Fewer graph edges than TSV rows | Use TSV; raise `MAX_GRAPH_EDGES` if a picture is needed |
| Graphviz failure or stale SVG | SVG older than DOT, or missing | Delete and rerender; an SVG can survive a rerun without `dot` |
| Stale or out-of-range pointer | Header printed with no numbered lines, or the wrong construct | Regenerate; search by name |
| Colon in path, reversed range | Wrong file or swapped bounds | Three-argument form |
| Schema or green test promoted to semantic approval | Report says "map correct" | Reword to what the gate proved |
| Dynamic, generated or security gap retried lexically | Same empty result | Change method |

Repeated empty lexical scans add false certainty, not evidence.

Parseltongue:

| Failure | Signal | Response |
| --- | --- | --- |
| Unsupported platform | Setup exits before download (no Linux arm64 asset) | Use the rough map or Clarity |
| Version check fails | `--version` lacks `1.7.2` | Stop |
| Port drift | Connection refused on 7777 | Read `SERVER_URL`; ports 7777 to 7787 have been recorded, and a reindex moved one run from 7777 to 7778 |
| Stale `run.config` after restart | Health fails on recorded URL | Last URL in `logs/server.log`; rerun reindex |
| Unencoded key | curl status 000 for a key containing a space | Encode with the `enc` helper |
| 404 on blast radius | Key taken from the first row of the full list, often build output | Search for a real source entity |
| 500 on `/folder-structure-discovery-tree` | Recorded on 5 of 14 calls | Optional endpoint; use the coverage report |
| Watcher inactive or counters at zero | Health lacks `"file_watcher_active": true` | Check logs; query the changed symbol; reindex |
| HTTP 200 with empty content | Empty arrays | Check coverage and key; an empty result is not absence |
| Fuzzy-search collision | Several candidates | Choose by path and kind |
| Old keys after reindex | 404 or wrong entity | Re-resolve |
| Source read at another revision | Lines do not match the graph | Align revision; reindex |
| Workspace path outside the run folder | Reindex refuses to delete it | Start a fresh setup |
| Missing `server.pid` | Stop script errors | The server is not tracked; find the process by port |

The counts above come from a log of 74 queries across earlier runs (60 returned 200, 7 returned 404, 5 returned 500, 2 returned 000). They describe those runs. They are not a failure rate for the tool.

Classify a Parseltongue failure as substrate, query selection, entity identity, coverage, interpretation, semantic confirmation or record integrity, and invalidate only the claims downstream of the failed step.

GitHub:

| Failure stage | Signal | Recovery |
| --- | --- | --- |
| Auth or host | `gh auth status` fails; wrong host passes with empty results | Restore auth; confirm host |
| Repository identity | 404, or a fork captured | Correct `owner/repo` |
| Scope or mode | Crawl for a one-artifact question | Narrow; trace |
| Capability | Discussions query errors | Check `hasDiscussionsEnabled`; mark not applicable |
| Surface | Review comments absent from a pull request digest | Query the review-comment surface |
| Pagination | Pages equal the cap; nested replies below `totalCount` | Continue pagination; focused follow-up; state truncation |
| Relationship | Commit not linked to its pull request | `commits/<sha>/pulls` |
| Raw persistence | Digest without raw files | Re-capture to stable paths |
| Digest | Renderer raises on an unknown capture type or missing `raw/repo.json` | Fix the capture directory; rerender |
| Permission | Private or restricted surface | Report as inaccessible, not absent |
| Rate limit | 403 or 429 with rate headers | Wait for reset; narrow |
| Mutation | A write command was run | Stop; report; do not repeat |

Recover at the earliest failing stage. Missing review comments can make a polished digest overstate consensus.

Clarity:

| Failure | Signal | Response |
| --- | --- | --- |
| No binary | Probe prints an empty `CLARITY_BIN=` and exits 1 | Report; do not install unasked |
| Flag not recognised | Usage error | Read `show --help`; switch command style |
| Subcommand missing | `modules` or `cycles` not in help | Older binary; skip or rebuild on request |
| Port busy | `watch` fails on 4900 | Pass `--port` |
| Unsupported language | Files missing from the graph | `clarity languages`; state the gap |
| Graph too broad | Unreadable output | Anchor on a file or path; limit depth |
| Build tooling missing | `make build-dev` fails without Go or Node | Ask before installing |

Strata:

| Failure | Signal | Response |
| --- | --- | --- |
| App or MCP unreachable | Connection refused on 7337; `lsof` prints nothing | `open -a Strata`; install the app if `/Applications/Strata.app` is absent |
| GET returns 405 | Browser or plain curl | Expected; use POST JSON-RPC through the scripts or MCP tools |
| Tools not shown in the agent | Configured but not listed | Restart the agent, or use `scripts/strata_mcp_tool.py` |
| Compile or validation error | `compile_error` | Nothing saved; fix at the returned line and column; validate again |
| Stale `base_version` | Conflict response | Reread, merge, validate, retry with the new version |
| Active-diagram ambiguity | `diagram_id` omitted | Pass explicit IDs |
| Irreversible deletion | `delete_diagram`, `delete_group` | Confirm with the user first |
| Storage edited directly | SQLite file under `~/Library/Application Support/Strata/` touched | Never; use MCP |
| Wrong product | Request about another "Strata" | Out of scope |

## Workload Model

- Rough map: a batch scan with filesystem writes. Cost follows the number of inventory paths, supported files, bytes and lines, symbol rows, import rows and unique edges. The graph cap limits only the picture, not the scan. Large generated files and dense imports dominate. The scan covers the whole inventory, not just changed files. One build pays off when several questions reuse it. Stages: inventory, extension filter, line counting (a read error becomes a zero count), Ctags or regex extraction, lexical import scan and resolution, frequency-ranked capped graph, summary. The builder does not record its own identity and does not require an empty output directory, so the operator must capture the command and guarantee a fresh directory. Variants (features, platforms, configurations) still need authoritative checks however many questions reuse the map.
- Parseltongue: one verified run per stable workspace state. One governing question at a time. Bound hops and token budgets. Split independent systems into separate runs and packets. Record revision, run folder, last index event, question count, depths and response sizes.
- GitHub: bound one repository, one host, one mode, one time window, one surface set and one page cap. Cost follows thread density, endpoint caps, nested replies and rate limits, not item counts. Parallelise only independent read-only surfaces, each with its own raw path, with one manifest owner and one digest owner.
- Clarity: one command per question; anchor on files or paths to keep graphs readable.
- Strata: one diagram per map; each update replaces the full source.

No capacity figure (files, edges, pages, tokens, concurrency) has been measured for any of the five.

## Reliability Target

Not measured. No accuracy, recall or success rate exists for these tools. What can be held constant:

- Hard controls: read-only behaviour, declared scope, separate surfaces, stated caps, saved raw output, a source or payload behind every claim, reported gaps, no leaked credentials, no unsupported claims about production, security, latency or reliability.
- Evidence states for a claim: `candidate`, `observed`, `corroborated`, `verified_for_scope`, `refuted`, `unresolved`, `invalidated`.
- Promotion rules: guidance becomes fact only against the current implementation; a capability becomes a contribution only with actual output; a row becomes a finding only with revision-bound source; a lexical edge becomes a dependency only with semantic, configuration or build evidence; a static edge becomes behaviour only with a runtime observation; a missing row becomes absence only through an independent method; a fixture result does not generalise to a real repository; one repository does not make a universal rule.
- Navigation tolerates reversible, candidate-level uncertainty. Deletion and security do not.
- Things to watch: stale-run incidents, false exclusions, digests that later prove to have missed a decisive thread. A compliant digest can still miss an inaccessible review.

## Retry Backpressure Guidance

- Retry only when the next attempt changes a premise: environment, input, tool or version, option, source state, authorisation, scope or method. Predict the signal that would show the retry worked.
- Rough map: the builder has no retry, backoff, queue, lock, resume or transaction protocol; the operator owns these. Rerun into a fresh output directory and never into a mixed one. Eligible retries: install or fix a missing command; correct the root or output path; fix capacity or permissions; freeze the revision when the source is changing; diagnose malformed Ctags output; rerender the optional SVG only if it is needed. Never rerun unchanged for an unsupported extension, an alias, a dynamic or generated gap, or an absence already refuted.
- Retry states: `failure_observed`, then classify the earliest failing stage (`cause_classified`), name the changed premise and the expected signal (`retry_ready`, with fresh output, an owner and a stop rule), run (`retry_running`), and end in `retry_succeeded`, `new_failure_discovered` or `same_failure_repeated`. Terminal states also include `method_boundary_reached`, `authorization_blocked` and `contradicted`. A later failure in a different stage is a new failure, not proof that the first diagnosis was wrong.
- Attempt record: identifier, earliest failure signature, hypotheses, changed premise, expected signal, target identity, tool and options and actual extractor, fresh output path, owner, start and stop, result, and the effect on claims. One bounded retry is a reasoning safeguard, not a timing constant. For external systems follow their own rate-limit and idempotency rules; do not invent timing values.
- Parseltongue: after a verified code change, do one incremental refresh, re-resolve the entity and replay the bounded query. Retry one transient timeout once, then read source directly if health stays uncertain. Do not repeat queries against a wrong URL, loop reindexing, or carry keys across rebuilds.
- GitHub: classify the failed stage, keep the raw files that succeeded, change one condition and retry the smallest idempotent read. Retry one failed page into a new raw file and reconcile cursors. Retries can address transient auth state, rate limits, one failed page, a schema mismatch, a nested-reply follow-up or a renderer failure. They cannot bypass permissions, mutate state or widen scope. No parallel retries, duplicate pages, overwritten raw files or silent query changes.
- Strata: on a version conflict, reread, merge, validate and retry once with the new `base_version`. On a compile error, fix the source; do not resend it.
- Backpressure: stop synthesis while a coverage or verification gate is red. In long investigations, checkpoint after each batch and reread the question before any broad or destructive step. With several workers, give each file or surface one owner.
- Stop when the same failure mechanism recurs, when no new evidence arrives, or when authorisation is missing.

## Observability Checklist

Record enough that someone else can replay the investigation:

- All tools: question, tool and version, exact commands with exit status, working directory, repository root, revision, dirty state, timestamps, output paths, decisions, discarded hypotheses, errors and empty results.
- Rough map: builder and reader hashes, `MAX_GRAPH_EDGES`, inventory mode and counts, extractor actually used, full and projected edge counts.
- Parseltongue: run folder, `SERVER_URL`, `DB_URI`, health and watcher output with log evidence, coverage, entity resolution steps, query parameters, bounded response summaries, source confirmations.
- GitHub: capture time, host, repository, auth status without tokens, mode, scope and filters, capabilities, endpoints, pages and cursors, rate-limit state, raw paths and hashes, relationships found, digest path, gaps, retries, count of mutating calls (expected: zero).
- Clarity: binary path and version, command style, repository state, output format.
- Strata: project and diagram names, kit, versions before and after, validation result, `render_ok`.

Where to keep the record: a Markdown decision record, structured JSON or TSV, a secured shell log, a CI artifact, a metrics system, a runtime trace, or the issue and review system. Pick one authoritative identity and link the others to it; do not keep two mutable copies.

Depth by profile: navigation keeps revision, query, pointer, source, duplicate resolution and stop. Standard adds the full run envelope, coverage, extractor, samples, mismatches, checks and invalidation. High assurance adds variants, negative tests, build, runtime, security and domain review, and owner acceptance.

Prefer hashes, row keys, changed-file lists and pointers over raw dumps. Record truncation and any field you reconstructed afterwards. Never log credentials or URL query secrets. Paths, symbols and private thread content may be sensitive; redact as needed. Watcher counters without logs, health from a wrong URL and counts without their filters are not sufficient records. Test the record by having someone uninvolved reconstruct scope, surfaces and gaps from it.

## Performance Verification Method

Not measured. No latency, throughput or time-to-answer figure exists for any of the five tools. To measure:

- Separate the stages: tool setup or build, query, source reading, decision. For Parseltongue separate cold setup, warm investigation and source confirmation.
- Fix the repository snapshot, question, tool state, reviewer, start and stop events, context budget, correctness rubric and sample. Keep raw durations and include failures.
- GitHub quantities worth recording: requests, pages, objects, bytes, rate-limit use, collection and render time, reuse of saved captures, link validity, follow-up calls avoided, corrections.
- Compare like with like: same mode, same repository class. One run is not a percentile. Report percentiles only with enough comparable observations, the raw counts and the cohort.
- Speed is subordinate to uncertainty reduced. A focused trace can beat a large survey by reaching the decisive thread with less ambiguity. Reject raw object counts and calls per second as goals.
- Experiment card: hypothesis and decision; baseline and candidate identities; frozen workload (paths, supported files, bytes and lines, symbol rows, import rows, unique edges, graph cap, language mix, filesystem); environment and cache state; clock and boundaries; repetitions, order and failure handling; output equivalence or the intended semantic difference; counter-metrics; pass rule; and the boundary beyond which the result does not generalise.
- Tiers: a mechanism fixture (one causal branch), a representative snapshot (one repository and environment), a repository cohort (strata declared in advance), an operational workflow sample (bound to task and reviewer). Keep fixture results apart from capacity claims.
- Abort or relabel a comparison when revision, dirty state, generated files, root or inventory differ; when tool, capability, actual extractor or wrapper differ; when output is stale; when cap, language, filesystem or cache differ; on partial failure or background load; or when the evidence product itself changed.
- For a performance-only change to the builder, compare the path set and line counts, symbol rows with ranges and kinds, raw imports, internal and unresolved rows, projections and cap, summary and pointer behaviour. Use hashes only when output is deterministic. A semantic improvement needs expected corrected and regression cases, not forced equivalence.
- Cache discipline: state cold, warm or mixed and how it was established. A new process is not a cold operating-system cache. Alternate or randomise order, use fresh directories, disclose warm-ups, and keep failed, timed-out and cancelled runs.
- Counter-metrics: coverage, pointer hits on the intended construct, false internal edges, unresolved classification, relations hidden under the cap, missed consumers, correctness of the next action, escaped defects, logging overhead. Tool speed can worsen reviewer time, and a capped query can be fast because it hides evidence.
- Adopt a change only when the predeclared objective improves under a comparable workload, equivalence passes, variability is understood and no quality counter-metric regresses.
- Pass criterion for a navigation result: a reviewer can name the correct next action, the gate and the stop condition without opening unrelated files.

## Scale Boundary Statement

- Rough map: one repository root, supported languages, static wiring. No file, edge or sample threshold has been established. Beyond a single root, or where generated and dynamic wiring dominate, use native build graphs.
- Parseltongue: one run covers one coherent workspace snapshot with a revision and an owner. Split by repository or ownership boundary. Join findings across runs only through explicit APIs, contracts and runtime telemetry. Stop for several independent systems, unbounded discovery, or questions about production traffic. For those, use per-repository packets, service catalogs and traces, API and queue schemas, lightweight inventories, or one migration corridor at a time.
- GitHub: one repository. Organisation-wide joins, mixed hosts, shared cursors and unequal permissions need per-repository packages and a separate synthesis step with one digest owner. Scale is exceeded when reconciling relationships and permissions grows faster than the evidence gained from another request. On a large codebase, narrow with a dependency tool first, then capture history for the few artifacts that matter.
- Clarity: file granularity. Whole-tree graphs on large repositories need module collapse or a path anchor.
- Strata: one Mac, loopback only. It is not a shared server.

## Outcome Metrics and Feedback Loops

No values are implied. Define each metric before using it: purpose, numerator, denominator, unit, inclusion and exclusion, cohort (repository, revision, languages, task, tool and options), sampling, raw evidence kept, a counter-metric, and the action a change triggers.

- Leading indicator: decision-relevant uncertainty reduced without more missed consequential evidence. Not command speed.
- Rough map: inventory coverage, pointer hit rate (range holds the intended construct), relation agreement and mismatch classes, share of unresolved references classified, edges omitted by the cap, dependency defects that escaped.
- Parseltongue: time to first relevant entity, graph-to-source narrowing ratio, share of claims confirmed in source, ambiguous-entity corrections, stale-run detections, false exclusions found, reviewer acceptance of the decision. Reviewer approval is not accuracy.
- GitHub: selected-surface coverage, hidden gaps found later, page-cap disclosure, link validity, chronology corrections, commit-to-pull-request accuracy, digest replay from raw, duplicate network work avoided, mutating calls, follow-up traces needed.
- One-run deterministic checks for the rough map: `producer_identity_complete`, `artifact_set_consistent`, `coverage_reconciled`, `actual_symbol_producer_known`, `pointer_sample_valid`, `relation_sample_classified`, `projection_reconciled`, `claim_sufficiency_met`, `decision_reversibility_preserved`.

Keep observed, derived, illustrative, proposed and unknown values apart. Corrections are useful telemetry: record each disagreement between a map and the source, each rework, and each route that added nothing.

## Completeness Checklist

Before acting:

- [ ] Claim, action, consequence, stop condition, owner and rollback are written down.
- [ ] Tool, version, target and environment identity are recorded.
- [ ] Coverage exclusions are known.

Before interpreting:

- [ ] Inventories reconciled; extractor identified (rough map).
- [ ] Health, watcher and coverage read; entity resolved by search (Parseltongue).
- [ ] Auth, host, repository, capabilities, mode, scope, date and page bounds fixed; surfaces selected and kept separate; raw manifest present (GitHub).
- [ ] Live help read for every flag (Clarity).
- [ ] Kit described; source validated (Strata).
- [ ] Pointers and content validated; internal and unresolved edges sampled; full rows compared with capped projections.
- [ ] Configuration, generated and runtime surfaces inspected for the edges that matter.

Before a consequential action:

- [ ] Authoritative semantic, build, configuration, test, runtime or security checks run.
- [ ] Counterevidence and limits recorded.
- [ ] Owner acceptance obtained where policy requires it.

Invalidation:

- [ ] Tool or options changed: rebuild and reopen derived claims.
- [ ] Repository or dirty state changed: regenerate, re-resolve pointers and keys, rerun checks.
- [ ] Configuration, generated code or runtime workload changed: reopen the affected variants.
- [ ] A mismatch was found: invalidate dependent claims and add a fixture.

Completeness is relative to the declared scope and claim. A GitHub capture is never "the complete repository history". Ownership routing can be complete while deletion safety is not. A contradiction reopens the earliest false premise and what depends on it, not unrelated facts.

## Adjacent Reference Routing

Route by the capability that is missing, not by topic resemblance. The destination must be able to falsify the claim by a different method.

| Missing capability | Route to |
| --- | --- |
| Exact text location | `rg`, direct read |
| Syntax-aware matching | `ast-grep`, Tree-sitter |
| Resolved references, exact callers | Language server, SCIP-class index, compiler |
| Entity graph, blast radius | Parseltongue (this skill); other precise graph readers such as codebase-memory or codegraphcontext where they are installed |
| File-level change impact | Clarity (this skill) |
| Lightweight map without a server | Rough CLI map (this skill) |
| Configured targets, features, generated code | Build graph: Cargo, Gradle, Bazel, TypeScript project references |
| What actually runs | Tests, debugger, traces, logs, telemetry |
| Rationale and decisions | GitHub context capture (this skill), Git history |
| Review ownership | `CODEOWNERS` and ownership metadata |
| Expected behaviour as a contract | Executable specifications: [A03-Executable-Specs01.md](../../A03-Executable-Specs01.md) |
| Working method for AI-assisted changes | [A01-LLM-Workflow01.md](../../A01-LLM-Workflow01.md) |
| Threat and security properties | Security review |
| Cost and latency | Benchmarking |
| A durable picture | Strata (this skill) |

Hand over a packet: the original decision, the falsifiable claim and its consequence, the evidence collected, the earliest gap, the capability needed, the expected evidence, a stop condition and the sensitive-data boundary. Expect back: tool, version and scope, reproducible observations, contradictions, a bounded result (`supported`, `refuted`, `unresolved`, `escalation required`) and remaining limits. A handoff does not widen mutation rights, scope or confidence. A route succeeded if it closed the capability gap and updated the original decision; otherwise it added activity, not information.

For GitHub context, route onward (to code archaeology, a technical debate, review remediation, CI diagnosis or another repository) only after a digest exists with repository, scope, raw paths, key URLs, chronology and gaps, and only on a concrete pivot question. Conclusions about another repository need evidence from that repository. If one missing relationship matters, go back to a focused capture before analysing.

Combine routes only for different blind spots: an alias needs semantic or build evidence plus configuration; generated code needs the generation step plus emitted output or tests; dynamic wiring needs configuration or runtime evidence plus static structure; suspected dead code needs authoritative search plus runtime evidence and the owner; a redesign needs graph and source plus specification and ownership; an incident needs diagnosis plus history and graph.

Stop routing when the same claim comes back twice with no new evidence, when every destination shares the blind spot, when access is unavailable, or when the conflict needs an owner's decision. Route after orientation and before crossing a model boundary: a parse frontier calls for language-specific analysis or tests, and Git history can explain ownership but not reachability.

## Source Evidence Mapping Table

Authority depends on the claim:

| Claim about | Authority |
| --- | --- |
| Rough-map file formats, extensions, resolution rules | The bundled builder script as shipped |
| What a rough-map run actually did | Its `tooling.tsv`, `symbols.tsv` kinds, `ctags.jsonl` and row counts |
| Parseltongue version and run-folder policy | The binding rules in SKILL.md and the setup script |
| Parseltongue URL, database, workspace | `run.config`, `logs/server.log`, live health |
| Parseltongue endpoints and parameters | Live `/api-reference-documentation-help`; the tables here are a 1.7.2 record |
| Parseltongue workflows and flow patterns | The catalogs here; they are designs, not measured executions |
| GitHub endpoints, fields, pagination | Current GitHub CLI and API documentation plus a live call; this text reflects documentation checked 2026-04-08 |
| GitHub capture contents | The manifest and raw JSON of that capture |
| Clarity commands and flags | Live `--help` of the binary in use; the tables record 0.19.2 and a newer source revision |
| Strata tools and kit grammar | Live `tools/list` and `describe_kit`; the tables record 0.9.0 build 29 |
| What the target program does | Its source, build, configuration, tests and runtime |

Provenance of the rough-map approach: language servers answer symbol and call-hierarchy queries by location first, then content; precise code navigation systems fall back to text search; Tree-sitter and `ast-grep` provide syntax-aware matching; Universal Ctags emits JSON with start and end lines without a database; ripgrep is a fast recursive line-oriented search; Graphviz DOT and Mermaid are enough to draw extracted edges, as dependency-cruiser does. Links are under Sources.

## Evidence Boundary Notes

- Use verbs that match the evidence: a file records, a tool emits, a row contains, a pattern suggests, a second method corroborates, a counterexample refutes, a check verifies for a scope.
- Safe wordings: not "Ctags is installed" but "the JSON probe passed and rows have Ctags kinds". Not "the graph has no callers" but "no caller rows in complete output; stronger caller search still needed". Not "third-party" but "unresolved until classified". Not "pointer succeeded" but "numbered lines show the expected construct". Not "tests pass" but "the exercised configuration is green".
- Parseltongue: keep recorded tool facts, live-run observations, target-code facts, runtime evidence and provisional graph hypotheses apart. Source-backed is not semantically sufficient. Live is not necessarily version-correct. Code presence is not execution. A runtime occurrence is not universal reachability.
- GitHub: label claims as raw API fact, URL fact, timeline event, human-authored conversation, inferred relationship, search lead, synthesis inference, inaccessible surface, truncated surface, or absence at capture time. An absence claim must state permission and pagination status. An uncaptured Discussion is not an absent one.
- Rough map: one recorded environment check found `rg` and `ast-grep` present, the Ctags JSON probe failing and `dot` absent. That describes one machine. Rerun the preflight on yours.
- Clarity: newer-style flags in this document were not executed against a built binary.
- Strata: the tool list and grammars describe one observed version on one machine.
- The Parseltongue caller and blast-radius numbers are rules of thumb. The query status counts describe one log.
- Nothing here has been measured for accuracy, speed, capacity or productivity.
- Claim card: a bounded falsifiable claim and the action it supports; state; evidence type; source identity (hash, version, revision, command, row, pointer, trace or approval); scope; inference; counterevidence; the check that would falsify it and its limitation; owner; invalidation trigger; next action.
- Changed evidence invalidates selectively. Builder or options: inventory, extraction, relations, projections. Pointer reader: span evidence. Environment: extractor, rendering and performance comparability. Repository or dirty state: inventory, pointers, relations, source reads and checks. Configuration, generated code or runtime workload: the affected behaviour. An external document: current external claims. Policy or owner: authorisation and risk.
- Duplicated bytes add provenance, not independent weight. Conflicting sources need a narrower time or claim scope, not an average.
- Promote a claim only through an explicit gate. When a premise changes, retract the claims that depend on it and keep unrelated facts.
- Confidence is compositional: say which link in the evidence chain would change the recommendation if it broke.

## Future Refresh Search Queries

Refresh when a command fails, a flag is missing or a tool version changes. Start from the live tool (`--help`, API help, `describe_kit`, response headers), then official versioned documentation. Search results are leads, not facts. Reject snippets, forks, mirrors, similarly named tools and documentation for other versions.

Rough map:

- `LSP 3.17 workspace/symbol call hierarchy capability`
- `Ctags --output-format=json end line fields`
- `ast-grep Tree-sitter structural search`
- `ripgrep ignore hidden files line numbers`
- `Graphviz DOT escaping`
- `dependency-cruiser aliases TypeScript`
- `AGENTS.md hierarchical instructions`
- `GitHub Actions artifact verification`

Parseltongue:

- `parseltongue-rust-LLM-companion releases v1.7.2 changelog`
- `parseltongue HTTP API endpoints api-reference-documentation-help`
- `parseltongue pt01-folder-to-cozodb-streamer pt08-http-code-query-server`

GitHub:

- `gh api --paginate --slurp behavior`
- `GitHub GraphQL discussions nested replies pagination`
- `GitHub REST issues timeline events pagination`
- `GitHub REST list commits pull requests associated with a commit`

Clarity:

- `LegacyCodeHQ clarity CLI release notes show --reach --between`
- `clarity CLI modules cycles .clarity/modules.json`

Strata:

- `Strata Legacy Code Labs MCP server tools describe_kit`
- `Strata visual spec user_flow discovery_tree grammar`

None of these queries has been run. For each refresh record the claim, query, date, tool version, source, live check and what changed. Bring back the exact source and version, a narrow paraphrase, an installed-capability probe, a positive and a negative fixture, and any compatibility limit left open.

## Sources

Read when the rough-map approach was designed, and GitHub documentation checked 2026-04-08. Not refreshed since.

- Language Server Protocol 3.17: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/
- Sourcegraph precise code navigation: https://sourcegraph.com/docs/code_search/explanations/precise_code_navigation
- Tree-sitter: https://tree-sitter.github.io/tree-sitter/
- ast-grep: https://ast-grep.github.io/
- Universal Ctags manual: https://docs.ctags.io/en/latest/man/ctags.1.html
- ripgrep guide: https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md
- Graphviz DOT language: https://graphviz.org/doc/info/lang.html
- dependency-cruiser: https://github.com/sverweij/dependency-cruiser
- `gh api`: https://cli.github.com/manual/gh_api
- `gh pr view`: https://cli.github.com/manual/gh_pr_view
- `gh issue view`: https://cli.github.com/manual/gh_issue_view
- `gh repo view`: https://cli.github.com/manual/gh_repo_view
- `gh search commits`: https://cli.github.com/manual/gh_search_commits
- GraphQL API for Discussions: https://docs.github.com/en/graphql/guides/using-the-graphql-api-for-discussions
- REST commits: https://docs.github.com/en/rest/commits/commits
- REST commit comments: https://docs.github.com/en/rest/commits/comments
- REST issue comments: https://docs.github.com/en/rest/issues/comments
- REST issue timeline: https://docs.github.com/en/rest/issues/timeline
- REST pull request review comments: https://docs.github.com/en/rest/pulls/comments
- GitHub MCP server: https://github.com/github/github-mcp-server
- GitHub Actions documentation: https://docs.github.com/actions
- Reusing workflow configurations: https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations
- AGENTS.md format: https://agents.md/
- Codex AGENTS.md guide: https://developers.openai.com/codex/guides/agents-md
- Codex repository AGENTS.md: https://github.com/openai/codex/blob/-/AGENTS.md

The last six cover repository instructions, automation and MCP governance. They do not establish any endpoint, pagination or graph behaviour described here.
