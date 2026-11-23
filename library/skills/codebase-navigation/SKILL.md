---
name: codebase-navigation
description: Find your way around a large unfamiliar codebase with five tools - a rough command-line dependency map, Parseltongue 1.7.2 graph queries, GitHub repository context capture with the gh CLI, Clarity file-level impact graphs, and Strata visual specs - and choose the right one for the question. Use when you must orient in an unknown repository, find entry points or the files around a feature, trace callers and callees or blast radius before a change, reconstruct why code looks the way it does from commits, pull requests, issues and discussions, check the structural shape of a change before commit, or keep a map of what you learned as a versioned diagram. Not for proving runtime behaviour, security properties or that code is unused (use tests, traces, compiler or language-server evidence), not for writing or reviewing the change itself, not for mutating GitHub state, and not for products that only share a name with these tools (Apache Strata and similar).
---

# Codebase Navigation

## Purpose

This skill gets you from "I have never seen this repository" to "I know which files to read, who depends on them, and why they look this way". It covers five tools. Each answers a different question. None of them proves runtime behaviour.

| Tool | Question it answers | Evidence it gives | Cost to start |
| --- | --- | --- | --- |
| Rough CLI dependency map | Where are the likely entry points and neighbouring files? | Lexical import edges and `file:start:end` pointers | One script run; needs `rg` and `python3` |
| Parseltongue 1.7.2 | Who calls this entity, what does it call, how far does a change spread? | Entity-level graph over an HTTP API | Download, index, and run a local server |
| GitHub context capture | What changed, who discussed it, where was the decision made? | Raw JSON from commits, pull requests, issues, reviews, timelines, discussions | `gh` with working auth |
| Clarity | Which files does this change or this file couple to? | File-level impact graph in Mermaid or DOT | An installed `clarity` binary |
| Strata | How do I keep and share the map I just built? | A versioned D2 diagram in a macOS app | Strata running on the same Mac |

All five produce candidates and structure. You still read the source before you claim anything about behaviour.

## When to use

- You joined a repository with thousands of files and need the entry points and the main modules.
- You know a feature name or a symbol and need the files around it with exact line spans.
- You plan to change, rename, split or delete something and need callers, callees and spread first.
- A bug shows up in one place and you suspect the cause is elsewhere.
- You need the history behind a piece of code: the pull request, the review thread, the linked issue.
- You want to check the structural shape of uncommitted work, the latest commit, or a branch range.
- You want the resulting map as a diagram that people and agents can update and diff.

Example requests:

- "Map this repo and return `file:start:end` candidate spans with rough dependency edges."
- "Who calls `serialize_result`, and what breaks if I change it?"
- "Why was this commit merged the way it was? Find the review discussion."
- "Show the design impact of my uncommitted changes before I commit."
- "Turn this module map into a Strata diagram we can keep."

## When not to use

- One known symbol in a small repository. Run `rg` and read the file. Do not build a map or start a server.
- Exact runtime behaviour, branch conditions, or value propagation. Use tests, a debugger, or traces.
- Operational incidents. Start from logs and failing tests, then come back for structure.
- Proof that code is unused or that a change is safe. These tools can only raise or lower suspicion.
- Writing to GitHub (comments, labels, merges). The GitHub workflow here is read-only.
- Organisation-wide or cross-repository history. The GitHub workflow is scoped to one repository.

## Core workflow

1. Write the question as one sentence. Name the decision it feeds and what happens if you miss a dependency.
2. Classify the question with the table in "Choosing a tool". Pick one tool. Add a second only when it covers a different blind spot.
3. Check the repository state: root, revision, dirty or clean, and any repository instructions about indexes or generated code.
4. Check that the tool is present and at the expected version. Do not install or rebuild anything unless the user asked.
5. Run the smallest collection that can answer the question. Write tool output to a disposable directory outside the repository tree, or to a directory the user named.
6. Read the coverage report before the results. Know which files, languages and surfaces the tool did not see.
7. Rank candidates. Use query match, neighbours, ownership and configuration, tests and entry-point evidence. Never rank by edge count alone.
8. Read the source for the top candidates at exact spans. Widen to the whole file when macros, annotations, configuration or distant invariants matter.
9. Check each edge that matters against aliases, manifests, registries, generated code, framework conventions and runtime configuration.
10. Escalate only the open facts that could change the decision. Use a language server, the compiler or build graph, tests, traces, or the code owner.
11. Report with the output contract below. Label every claim as candidate, observed in source, or verified for a stated scope.
12. Stop when the remaining uncertainty cannot change the decision, or name the owner who must resolve it.

## Choosing a tool

| Your question | Start with | Then |
| --- | --- | --- |
| Where is this one symbol or string? | `rg` and a file read | Nothing else, unless you need its consumers |
| What is in this repository and where do I start? | Rough CLI map | Parseltongue orientation if you will ask many more questions |
| Which files import or include this file? | Rough CLI map, or Clarity if installed | Source read of both ends |
| Who calls this function? What does it call? | Parseltongue | Source read; language server for exact references |
| What is the blast radius of changing this entity? | Parseltongue | Tests and build for the affected set |
| What is the blast radius of changing this file? | Clarity | Parseltongue for entity detail |
| Is X really causing Y? | Parseltongue meet-in-the-middle | Source read at the overlap |
| What does my uncommitted change or branch touch structurally? | Clarity | Tests and type checks |
| Why does this code look like this? Who decided? | GitHub context capture (Artifact Trace) | Read the linked thread |
| How did this repository evolve recently? | GitHub context capture (Repo Survey) | Trace the two or three artifacts that matter |
| How do I keep this map and share it? | Strata | Update it as the map changes |

Rules for choosing:

- Choose per question, not per repository. A repository can deserve a Parseltongue run for one question and a plain `rg` for the next.
- The rough map needs no server and no download. Pick it when you only have a shell, when the platform has no Parseltongue 1.7.2 binary, or when a persistent server is not justified.
- Parseltongue works at entity level (functions, classes). Clarity works at file level. The rough map works at file level with symbol pointers.
- GitHub context capture answers "why" and "who". The other four answer "where" and "what depends on what". Use the dependency tools to narrow to a few commits or files first, then trace those artifacts on GitHub.
- Strata never discovers structure. It stores a diagram you write. Use one of the other tools first, then draw.
- Two tools that share a blind spot do not confirm each other. A rough map and its own rendered graph are one pipeline. Add a tool only when it observes something the first cannot.

### Reading source directly versus querying an index

The tools disagree on this point, and both positions are kept:

- The rough map is pointer-first. It exists to tell you which spans to open, and you then read source directly.
- Parseltongue guidance says to prefer graph queries for understanding code and to fall back to direct reads (`rg`, `cat`, an editor) only when the entity or relationship cannot be found in the graph, or when coverage diagnostics show the area was not indexed.

How to choose: if a verified, fresh Parseltongue run covers the area, ask the graph first and read only the narrowed files. If there is no run, the run is stale, coverage is low, or the claim depends on branch logic, dynamic dispatch, reflection or generated code, read the source. In both cases a conclusion that matters is confirmed in source before you act on it.

## Rules for every tool

### Evidence

- Treat every edge as a hypothesis. A graph edge does not prove execution. A missing edge does not prove absence.
- Full rows and raw payloads are evidence. Summaries and rendered graphs are projections. When they disagree, read the full rows.
- Tool availability is not tool contribution. Record which extractor actually produced the rows you rely on.
- "Unresolved" is not "third-party". "No inbound edge" is not "unused". "Readable range" is not "correct symbol".
- Deletion, security and "nothing depends on this" claims always need stronger evidence than these tools give.
- Do not attach confidence percentages. State what was checked, in what scope, and what was not.

### Safety

- Read-only by default. Do not mutate GitHub state, repository instruction files, or Strata diagrams unless the user asked for that change.
- Do not install, upgrade or rebuild a tool without being asked. If the repository is dirty, never pull or rebuild in place; use a clean worktree or a temporary clone.
- Keep tool output out of directories that may later be zipped, uploaded or committed.
- Never print or log tokens. File paths and symbol names can be sensitive too.
- Never pass a pointer or path you did not produce or check to a script that reads files.

### Freshness

- Bind every result to a repository revision and working-tree state. Edits invalidate saved line pointers and entity keys.
- Rebuilding fixes age. It does not fix a wrong root, an unsupported language, or a tool that cannot observe the thing you are asking about.
- Retry only after changing something: the environment, the input, an option, the source state, or the method. An unchanged retry is repetition.

## Tool 1: Rough CLI dependency map

A disposable, lexical map built with command-line tools. It produces candidate files, import and include edges, and `file:start:end` pointers. It is not a semantic index and it does not prove a complete blast radius.

Pick it when: the repository is unfamiliar, the languages are in the supported list, and you need broad orientation or the neighbourhood of a known feature. Skip it for one symbol or a tiny repository.

Requirements: `rg` and `python3` are required. Universal Ctags with JSON output improves spans. `ast-grep` is detected but never run by the script; use it by hand in noisy areas. Graphviz `dot` adds an SVG.

Supported file extensions: `.rs .py .js .jsx .ts .tsx .go .java .c .cc .cpp .h .hpp`. Anything else is invisible to the map.

### Commands

```bash
SKILL_DIR=/path/to/codebase-navigation
REPO_ROOT=/path/to/repo
OUT_DIR=/path/outside/the/repo/code-map      # must not already exist

# Preflight
command -v rg python3
ctags --output-format=json -f - /dev/null >/dev/null 2>&1 && echo ctags_json=yes || echo ctags_json=no
command -v ast-grep || command -v sg || true
command -v dot || true

# Build
test -d "$REPO_ROOT" && test ! -e "$OUT_DIR"
MAX_GRAPH_EDGES="${MAX_GRAPH_EDGES:-160}" bash "$SKILL_DIR/scripts/build_rough_codebase_map.sh" "$REPO_ROOT" "$OUT_DIR"

# Read in this order
cat "$OUT_DIR/tooling.tsv"
cat "$OUT_DIR/summary.md"
head -n 30 "$OUT_DIR/symbols.tsv"
head -n 30 "$OUT_DIR/internal_file_edges.tsv"
head -n 30 "$OUT_DIR/external_ref_edges.tsv"

# Find candidates and read exact spans (run from the repository root)
rg -n -i 'checkout' "$OUT_DIR/symbols.tsv" | head -n 20
bash "$SKILL_DIR/scripts/read_code_span_pointer.sh" src/main.rs 120 168 3
```

The builder takes `ROOT_DIR` (default `.`) and `OUT_DIR` (default `.code-map`). The default output sits inside the repository, so pass an explicit directory. The builder does not clear an existing output directory, so start from a path that does not exist.

### What the files mean

| File | Content | Limit you must remember |
| --- | --- | --- |
| `tooling.tsv` | `tool`, `available` for rg, ctags, ast-grep, dot | A probe result. It does not say the tool contributed rows. |
| `all_files.txt` | File inventory | Inside a Git worktree this is `git ls-files`: tracked files only. Untracked, ignored and generated files are missing. |
| `code_files.txt`, `files.tsv` | Supported source files; `path`, `line_count` | Thirteen extensions only. A zero line count can mean a read error. |
| `symbols.tsv` | `symbol`, `path`, `start_line`, `end_line`, `kind`, `scope` | With the regex fallback, `kind` is `regex` and start equals end. Names repeat; identity is path plus range. |
| `import_edges.tsv` | `source_file`, `source_line`, `target_ref`, `edge_kind` | Fixed lexical patterns. Multi-line and unusual import forms are missed. |
| `internal_file_edges.tsv` | Edges resolved to a file in the repository | Misses aliases, re-exports, conditional and generated wiring. |
| `external_ref_edges.tsv` | Everything that did not resolve | Unresolved, not third-party. Path aliases and bare module names land here. |
| `summary.md` | Counts, tooling, top ten fan-out and fan-in files | A ranking for a first look, not a complete view. |
| `dependency_graph.mmd`, `.dot`, `.svg` | Most frequent edges, capped by `MAX_GRAPH_EDGES` (default 160) | For communication only. If no internal edges exist, the graph is drawn from unresolved references. |

The builder fails when `rg` is missing or when it finds no supported source files. In a Git worktree a directory of new, untracked files yields "no supported source files" even though the files exist.

### Reading spans

`read_code_span_pointer.sh` accepts `file:start:end` or `file start end`, plus optional context lines (default 2). It swaps reversed bounds and prints numbered lines. Use the three-argument form for paths that contain a colon. Exit status zero means the range was readable, not that it holds the symbol you wanted. Confirm the numbered lines show the expected construct.

### Using the map

- Read `tooling.tsv` and `summary.md` first, then full TSV rows, then source.
- Check the `kind` column in `symbols.tsv` to learn whether Ctags or the regex fallback produced the spans.
- Expand from a candidate through `internal_file_edges.tsv` in both directions.
- Classify the unresolved references that matter. For a TypeScript alias such as `@core/registry`, read `tsconfig` or the bundler configuration before calling it internal or external.
- Regenerate the map and re-resolve pointers after edits. An old range can still be readable and now name a neighbouring helper.
- When the map is not precise enough, move to a language server, a SCIP-class index, the compiler or build graph, or Parseltongue. Do not patch the regexes to answer a semantic question.

## Tool 2: Parseltongue 1.7.2 graph queries

Parseltongue indexes a codebase into an entity graph and serves it over HTTP on localhost. Use it for topology: callers, callees, blast radius, clusters, cycles, hotspots, and context selection. Its control-flow and data-flow answers are graph-derived approximations.

Pick it when: the question is structural, a stable entity can be found, you expect to ask several questions against the same snapshot, and the platform is supported (macOS arm64 or x86_64, Linux x86_64, Windows x86_64).

### Binding rules

1. Pin to `v1.7.2`. Check that `parseltongue --version` contains `1.7.2` before indexing or querying. Stop if it does not.
2. Every setup creates a new timestamped run folder named `parseltongue-1.7.2-<codebase-slug>-<timestamp>`. Binary, database, logs and query output stay inside it.
3. Default run home is `${CODEX_HOME:-$HOME/.codex}/tool-runs/parseltongue-1-7-2`. Keep it unless the user asks for another `--base-dir`. Never place a run folder inside a directory that will be zipped or uploaded.
4. Setup deletes run folders older than one day in the base directory (`--cleanup-days`, default 1).
5. Do not assume the indexer honours a requested database path. Read `DB_URI` and `WORKSPACE_PATH` from `run.config`. Do not assume `db/codegraph.db`.
6. Do not assume `http://localhost:7777`. The server can bind the next free port. Read `SERVER_URL` from `run.config`. If it is missing or stale, take the last `http://localhost:PORT` line in `<run-folder>/logs/server.log`.
7. Check both server health and watcher status before you rely on live re-indexing. Server logs plus a query for the changed symbol are stronger proof than watcher counters, which can lag or stay at zero.
8. `/api-reference-documentation-help` on the live server is the source of truth for endpoint names and parameters. It overrides any written list, including this one.
9. Entity keys contain colons and can contain spaces. URL-encode them in every query.

### Setup, refresh, stop

```bash
SKILL_DIR=/path/to/codebase-navigation

# Install, index, start the server, run smoke queries
"$SKILL_DIR/scripts/setup_parseltongue_1_7_2.sh" /path/to/codebase
#   options: --base-dir DIR  --port 7777  --hops 2  --cleanup-days 1

# Load the facts of this run
RUN=/path/to/run-folder          # printed by setup
# shellcheck source=/dev/null
source "$RUN/run.config"
SERVER_URL="${SERVER_URL:-http://localhost:${PORT}}"
echo "$SERVER_URL $DB_URI $WORKSPACE_PATH"

# Refresh the index in place (same version, same run folder), then reload run.config
"$SKILL_DIR/scripts/reindex_parseltongue_1_7_2.sh" "$RUN"     # options: --codebase-path DIR  --port N
source "$RUN/run.config"

# Stop the server when done
"$SKILL_DIR/scripts/stop_parseltongue_server.sh" "$RUN"
```

Refresh when the user says "refresh", "refresh index" or "reindex", when watcher health is false, when live edits do not appear in queries, when the database looks stale, or when the server may have moved ports after a restart. Some machines have shell wrappers named `pt172-setup`, `pt172-refresh` and `pt172-stop` for these three scripts; use them if present.

The setup and reindex scripts append one line per event to `central-logs/parseltongue-query-log.txt` next to the `scripts/` directory. That file holds local paths. Do not commit or share it.

### Orientation

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

After these you know scale, parse coverage, hotspots, module groupings and whether cycles exist. Health alone is not coverage: read the coverage report before trusting a "no callers" answer. If `folder-structure-discovery-tree` returns HTTP 500, continue; use the coverage report for the folder view.

### Focused queries

```bash
enc() { python3 -c 'import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1], safe=""))' "$1"; }

curl -fsS "${SERVER_URL}/code-entities-search-fuzzy?q=main"
KEY="$(enc 'ENTITY_KEY_FROM_SEARCH')"
curl -fsS "${SERVER_URL}/code-entity-detail-view?key=${KEY}"
curl -fsS "${SERVER_URL}/reverse-callers-query-graph?entity=${KEY}"       # who uses this?
curl -fsS "${SERVER_URL}/forward-callees-query-graph?entity=${KEY}"       # what does this use?
curl -fsS "${SERVER_URL}/blast-radius-impact-analysis?entity=${KEY}&hops=2"   # how far does a change spread?
curl -fsS "${SERVER_URL}/smart-context-token-budget?focus=${KEY}&tokens=4000" # packaged context for an LLM
```

Use `tokens=8000` for refactors and complex debugging. Add a `scope` parameter, for example `&scope=crates||parseltongue-core`, to limit list, search and blast-radius queries; confirm the scope syntax in the live API help. Always search for the entity first; do not hard-code keys, and re-resolve them after every reindex. Pick a real source entity, not the first row of the full list, which can come from build output.

### The three basic traces

- Backward from a symptom (bug hunting): search, detail view, reverse callers, blast radius.
- Forward from a candidate change (planning): detail view, forward callees, blast radius, smart context.
- Refactor risk: reverse callers, blast radius at `hops=3`, cycle scan, smart context at 8000 tokens.

Triage numbers for refactor risk: 0 to 5 direct callers usually means low risk, 6 to 15 medium, more than 15 high. A blast radius above 100 at two hops usually means critical infrastructure or cross-cutting behaviour. These are rules of thumb that tell you how much to read and test. They are not measured thresholds, and no caller count approves a change by itself.

### Question to workflow

Thirteen combined workflows exist. The query sequences for all of them, and twelve flow patterns, are in [reference.md](reference.md). The selection rule:

| Question | Workflow |
| --- | --- |
| Is X really causing Y? | Meet-in-the-middle: reverse callers of the symptom, forward callees of the suspect, look for overlap |
| Why does a local break feel systemic? | Symptom-to-system corridor: callers, callees, blast radius at 3 hops |
| How do I change this safely in phases? | Change choreography: stabilise downstream, move a small caller slice, reindex, re-query, expand |
| Where should I extract an interface? | Narrow-waist seam: high inbound pressure, bounded outbound spread |
| Why are these modules entangled? | Boundary-leak detector: clusters, folder tree, callers and callees from unexpected modules |
| Where do I cut the cycle? | Cycle-breaker scout: fewest reverse callers, lowest core-ness |
| Can I delete this? | Deletion-safety classifier, then stronger evidence outside the graph |
| Why is this hotspot painful? | Pressure-versus-sink split: too many callers or too many dependencies |
| How much should I trust the graph here? | Parse-frontier probe: coverage and ignored-files reports |
| Who should review this? | Ownership router: callers, callees, clusters; then check ownership files |
| Does this source feed that sink? | Source-to-sink convergence |
| Who can cause this side effect? | Sink-to-source accountability |
| How do I split this orchestrator? | Orchestrator split planner |

### Limits

Strong for dependency topology, caller pressure, downstream spread, cluster boundaries and change risk. Weak for branch predicates, exact value propagation, reflection, generated code, queues, configuration-driven routing and dynamic dispatch. When the corridor you care about enters ignored or low-coverage files, stop making flow claims and read the code there. Blast radius is topology, not a call tree. Empty reverse callers never justify deletion.

## Tool 3: GitHub repository context capture

Use the `gh` CLI as a read-only layer over GitHub's REST and GraphQL APIs to capture how a repository changed and what people said while it changed. The deliverable is a source-linked Markdown digest, not a terminal dump. No local clone is needed.

Three modes:

- Repo Survey: a bounded, broad picture of recent evolution.
- Artifact Trace: the story behind one commit, pull request, issue or discussion.
- Digest Mode: a reusable Markdown summary rendered from captured JSON.

### Workflow

1. Preflight. Confirm `gh` exists and `gh auth status --active` is healthy. If auth is broken, stop and ask the user to run `gh auth login` or to provide `GH_TOKEN` or `GITHUB_TOKEN`. Confirm repository and host.
2. Check capabilities. Never assume Discussions exist.
3. Fix the scope before collecting: repo-wide snapshot, since-date snapshot, or a single pull request, issue, commit or discussion.
4. Pick the surface: high-level `gh` views for orientation and small reads, `gh api --paginate --slurp` for list capture, `gh api graphql` for Discussions.
5. Save raw JSON to stable paths, one file per surface, so the digest can be re-rendered without another network crawl.
6. Write the digest with provenance: scope, surfaces queried, chronology, key conversations, links, gaps.

```bash
SKILL_DIR=/path/to/codebase-navigation
CAP=/path/outside/the/repo/gh-capture

gh auth status --active
gh repo view owner/repo --json nameWithOwner,hasDiscussionsEnabled,isPrivate,visibility,url

# Repo Survey (bounded: 5 pages of 100 per surface by default)
"$SKILL_DIR/scripts/collect_repo_context.sh" --repo owner/repo --output-dir "$CAP/survey" --since 2026-01-01T00:00:00Z
#   --max-pages N (0 = unlimited)   --no-discussions

# Artifact Trace
"$SKILL_DIR/scripts/collect_artifact_context.sh" --repo owner/repo --kind pr --id 123 --output-dir "$CAP/pr-123"
#   --kind commit|pr|issue|discussion

# Digest
python3 "$SKILL_DIR/scripts/render_repo_context_digest.py" --input-dir "$CAP/pr-123" --output "$CAP/pr-123/digest.md"
```

Direct commands for single reads:

```bash
gh pr view 123 -R owner/repo --json number,title,body,comments,commits,files,reviews,url,createdAt,updatedAt
gh api --paginate --slurp "repos/owner/repo/commits?sha=main&per_page=100"
gh api --paginate --slurp "repos/owner/repo/commits/<sha>/pulls?per_page=100"      # commit to pull request
gh api --paginate --slurp "repos/owner/repo/issues/123/timeline?per_page=100"      # state-change events
gh api --paginate --slurp "repos/owner/repo/pulls/123/comments?per_page=100"       # review comments
gh api --paginate --slurp "repos/owner/repo/pulls/123/reviews?per_page=100"        # review state and summaries
```

### Surface rules

- Keep five conversation surfaces apart: issue-thread comments, pull request review comments, commit comments, timeline events, and discussion comments with their replies. A pull request inherits issue-thread comments, and its review comments are a separate surface. You usually need both.
- Timeline events are state-change metadata, not discussion. Collect them per artifact. Do not harvest timelines repo-wide by default.
- The repo-wide issues endpoint also returns pull requests. Filter on the `pull_request` key during synthesis.
- `gh search commits` finds hashes, phrases and authors. It is a discovery helper, not a complete history. Use the commits list endpoint for history.
- Discussions have no first-class `gh` command. Use GraphQL. `--paginate` follows only the top-level connection tied to `$endCursor`; nested replies are fetched 100 at a time and can truncate. Say so in the digest and run a focused follow-up when a long thread matters.
- In the repo collector, `--since` filters commits only. Pull requests, issues and comments are sorted by update time and cut at the page cap.
- No single command returns everything. Do not scrape the website when the CLI and APIs cover the task.

### Bounded first, exhaustive on request

Two goals pull against each other: complete capture per surface, and practical collection on large repositories. Start bounded. Widen (`--max-pages 0`, more surfaces, an earlier date) only when the user asks for deeper capture or a named gap affects the answer. A bounded survey is valid only when the digest states the page cap and the surfaces left out. Never describe a capture as the complete history of a repository.

### Digest sections

Return these sections in this order:

```markdown
## Scope
Repository, host, capture type, collection time, since filter, page cap.
## Surfaces Queried
Commits, pull requests, issues, issue comments, review comments, commit comments, timelines (if captured), discussions (if captured).
## Chronology
Dated events in order, each with its URL.
## Key Conversations
Review threads that mattered, accepted answers, dense comment activity. Name the surface for each.
## Linked Artifacts
Commit to pull request, pull request to issue, discussion URLs referenced from issues or pull requests.
## Gaps And Limits
Permissions, disabled Discussions, page caps reached, timelines not captured, truncated replies, search-versus-list caveats.
## Raw Output Paths
Manifest, raw JSON directory, digest path.
```

The renderer produces counts and lists. `Key Conversations` still needs you to read the raw threads and write the synthesis. A teammate reading the digest must be able to answer: what was collected, what happened when, where the main decisions happened, and what gaps remain.

## Tool 4: Clarity

Clarity is the LegacyCodeHQ structural design CLI. It works at file granularity and shows coupling, impact, boundaries, cycles and the shape of a change. It does not prove runtime behaviour, API contracts or semantic correctness.

Pick it when: you want the structural impact of uncommitted work, a commit or a branch range; a file-level blast radius before a refactor; or a cycle or module view; and a `clarity` binary is already installed.

### First move: probe the binary

```bash
SKILL_DIR=/path/to/codebase-navigation
"$SKILL_DIR/scripts/probe_clarity.sh"          # set CLARITY_BIN=/path/to/clarity to point at a specific binary

# Equivalent by hand
CLARITY_BIN="${CLARITY_BIN:-$(command -v clarity)}"
"$CLARITY_BIN" --version
"$CLARITY_BIN" --help
"$CLARITY_BIN" show --help
```

If no binary is found, say so and stop. Do not install or build one unless the user asks. The probe script also checks a few fixed paths from its author's machine; they simply fail elsewhere.

### Workflow

1. Run from the target repository root, or pass `--repo <path>`. Run `git status --short --branch` before recommending commit or range commands.
2. Pick the mode:

| Goal | Command |
| --- | --- |
| Uncommitted work | `clarity show -f mermaid` or `clarity show -f dot` |
| Latest commit | `clarity show -c HEAD -f mermaid` |
| Branch range | `clarity show -c main...HEAD -f mermaid` |
| Supported languages and extensions | `clarity languages`, `clarity extensions --format text` |
| Live graph while editing | `clarity watch` (add `--port` if 4900 is busy) |
| Shareable graph URL | `clarity show -u` (it does not open a browser for you) |
| Workspace graph | `clarity workspace --language auto` |

3. Choose output: Mermaid for Markdown and clients that render it, DOT for Graphviz or parsing.
4. Interpret with care. Look for edges that cross expected boundaries, changed production files with no connected tests, high-degree files, cycles and module leakage.
5. Report the exact command and binary version, a plain summary, and caveats: unsupported extensions, dirty repository, command-surface mismatch, or a graph too broad to read.

### Two command surfaces

Flags changed between releases. Both forms are valid for their version. Live `--help` output decides which one you use.

| Goal | Newer style | Older style |
| --- | --- | --- |
| Scope to paths | `clarity show src tests` | `clarity show -i src,tests` |
| File blast radius | `clarity show path/to/file --reach both --depth 2` | `clarity show -p path/to/file --level 2` |
| Upstream dependents only | `clarity show path/to/file --reach up` | may not exist |
| Coupling between two paths | `clarity show --between a,b` | `clarity show -w a,b` |
| Live graph for a path | `clarity watch src --reach both` | `clarity watch -i src` |
| Module summary | `clarity modules` | may not exist |
| Module graph | `clarity show --module name --reach both` | may not exist |
| Cycle audit | `clarity cycles src` | may not exist |

Recorded observation: an installed 0.19.2 binary exposed `extensions`, `languages`, `setup`, `show`, `watch` and `workspace`. The newer `main` branch also documented `modules`, `cycles`, positional paths, `--reach`, `--all`, `--collapse`, `--module`, `--prune` and `--also`. Those newer flags were read from documentation, not executed, so confirm each with `--help` before use.

### Rebuild and setup

Rebuild only when the user wants newer behaviour or the installed binary lacks a needed command. Work in a clean worktree of the Clarity source checkout, never in a dirty one:

```bash
git fetch origin main --prune
git worktree add --detach /tmp/clarity-main-build origin/main
cd /tmp/clarity-main-build
make build-dev
./clarity --version && ./clarity --help
```

The build needs Go 1.21 or later with CGO, and Node with npm for the watch assets. Ask before installing system tooling.

`clarity setup` writes guidance into the repository's `AGENTS.md`. Run it only when the user wants repository instructions changed, and review the diff afterwards.

Say "Clarity shows structural coupling" or "shows impact". Do not say it proves behaviour. Pair it with tests and type checks for implementation claims.

## Tool 5: Strata

Strata is the Legacy Code Labs native macOS visual-spec app. It keeps versioned D2 diagrams and exposes them through a loopback-only MCP server at `http://127.0.0.1:7337/mcp`. In codebase navigation its job is to hold the map you built with another tool so it does not live only in chat. It does not analyse code.

Pick it when: you are on the Mac that runs Strata, and the user wants a durable, diffable diagram of a flow, an architecture, or a plan, or wants to check a feature against a diagram the team already shares.

### Start and connect

```bash
test -x /Applications/Strata.app/Contents/MacOS/Strata
open -a Strata
lsof -nP -iTCP:7337 -sTCP:LISTEN

codex mcp add strata --url http://127.0.0.1:7337/mcp     # or add the URL to your agent's MCP configuration
codex mcp list

SKILL_DIR=/path/to/codebase-navigation
"$SKILL_DIR/scripts/strata_mcp_probe.py" --kits            # read-only: initialize, list tools, list projects, describe kits
```

If the agent's tool list does not show Strata after it is configured, restart the agent or use the raw fallback script. The server is still usable over raw JSON-RPC. A browser GET to `/mcp` returns 405; that is expected, because the endpoint accepts POST only.

### Workflow

1. `list_projects`. Create or choose a project.
2. Pick a kit:

| Kit | Use for |
| --- | --- |
| `user_flow` | UI navigation, journeys, branching logic, end-to-end paths |
| `discovery_tree` | Outcomes, nested tasks, dependency and planning trees |
| `freeform` | Raw D2: architecture, module maps, data flows, state machines, ownership maps |

3. Call `describe_kit` before writing a constrained kit. It is the live grammar.
4. Draft the source and call `validate_diagram` until it compiles.
5. `create_diagram`, or `get_diagram` then `update_diagram`.
6. For updates, pass the `version` you last read as `base_version`. On conflict: read again, merge on purpose, validate, retry.
7. Use `list_versions`, `diff_versions`, `get_version` and `restore_version` for review, rollback and audit.

```bash
T="$SKILL_DIR/scripts/strata_mcp_tool.py"
"$T" list_projects
"$T" list_diagrams --args-json '{"project_id":"PROJECT_ID"}'
"$T" validate_diagram --args-json '{"kit":"freeform","source":"direction: right\n\napi: HTTP handlers\ndomain: Order service\nstore: Postgres adapter\n\napi -> domain: place_order()\ndomain -> store: save()"}'
"$T" create_diagram --args-json '{"project_id":"PROJECT_ID","name":"Order flow module map","kit":"freeform","source":"..."}'
"$T" get_diagram --args-json '{"diagram_id":"DIAGRAM_ID"}'
"$T" update_diagram --args-json '{"diagram_id":"DIAGRAM_ID","base_version":1,"source":"...","message":"Add outbox edge"}'
```

A minimal `user_flow` source:

```d2
@direction down

start s: Start
screen page: Page
end e success: Done

s -> page
page -> e
```

### Safety rules

- Treat project, diagram and group IDs as opaque. Pass IDs explicitly. In summaries for people, use `diagram_name`.
- Omit `diagram_id` (to target the diagram selected in the app) only when the user is looking at it and says "this diagram".
- Validate before you mutate. `update_diagram` replaces the whole D2 source and creates a snapshot. Fill in `message`.
- Say an edit landed only when the response shows `render_ok: true` or a successful create or update. A `compile_error` means nothing was saved; fix it using the returned line and column.
- `delete_diagram` removes the diagram and its version history. `delete_group` removes the group and keeps its diagrams ungrouped. Neither can be undone over MCP. Ask for explicit confirmation first.
- Never edit Strata's SQLite database. Go through MCP so validation, snapshots and app state stay consistent.

## Output contract

Every navigation answer contains:

1. Question and decision: one sentence each.
2. Tool, version and exact commands. Repository root, revision and dirty state.
3. Coverage: what the tool did not see (languages, untracked files, low-coverage folders, page caps, disabled surfaces).
4. Candidates, at most three unless asked for more:

```text
Candidate 1
- Pointer: path/to/file.ext:10:42
- Why: query match + graph relation (for example high fan-in from related files)
- Local edges: importers or callers X, Y; imports or callees Z
- Evidence read: the lines that support this, quoted briefly
- Confidence: high|medium|low, with the reason
```

5. Verified edges and refuted edges, kept separate from candidates.
6. Open questions and the one extra read or check that would close each.
7. Where the raw output lives.

Tool-specific additions:

- Parseltongue: run folder, `SERVER_URL`, `DB_URI`, health and coverage summary, entity keys, queries in order, which graph claims were confirmed in source.
- GitHub: the seven digest sections above.
- Clarity: the binary version and which command style was used.
- Strata: `diagram_name`, kit, resulting version, and `render_ok`.

## Quality gates

Run the gates for the tools you used. Each gate proves only what it says.

```bash
SKILL_DIR=/path/to/codebase-navigation
# OUT_DIR, RUN, KEY and CAP are the variables set in the tool sections above.

# Scripts parse (proves syntax only)
for s in "$SKILL_DIR"/scripts/*.sh; do bash -n "$s" || echo "FAIL $s"; done

# Rough map: artifacts emitted (proves emission only)
for f in summary.md tooling.tsv files.tsv symbols.tsv import_edges.tsv internal_file_edges.tsv external_ref_edges.tsv dependency_graph.mmd dependency_graph.dot; do
  test -s "$OUT_DIR/$f" || echo "MISSING $f"
done
head -n 1 "$OUT_DIR/symbols.tsv"                                   # expect: symbol path start_line end_line kind scope
awk -F'\t' 'NR>1 {k[$5]++} END {for (x in k) print x, k[x]}' "$OUT_DIR/symbols.tsv"   # which extractor produced the rows
wc -l "$OUT_DIR/code_files.txt" "$OUT_DIR/files.tsv" "$OUT_DIR/internal_file_edges.tsv" "$OUT_DIR/external_ref_edges.tsv"

# Rough map: pointer round trip (proves a readable range; you confirm the construct)
bash "$SKILL_DIR/scripts/read_code_span_pointer.sh" path/to/file.ext 10 42 2

# Parseltongue: identity, health, coverage
source "$RUN/run.config" && echo "$SERVER_URL $DB_URI"
curl -fsS "${SERVER_URL}/server-health-check-status"
curl -fsS "${SERVER_URL}/file-watcher-status-check"
curl -fsS "${SERVER_URL}/ingestion-coverage-folder-report?depth=2"

# GitHub: auth, capability, raw files present
gh auth status --active
gh repo view owner/repo --json nameWithOwner,hasDiscussionsEnabled
test -s "$CAP/survey/manifest.json" && ls "$CAP/survey/raw"

# Clarity: binary and command surface
"$SKILL_DIR/scripts/probe_clarity.sh" | head -n 40

# Strata: server reachable, source compiles
lsof -nP -iTCP:7337 -sTCP:LISTEN
"$SKILL_DIR/scripts/strata_mcp_probe.py" --json | head -n 20
```

Then run the project's own checks for anything you intend to change: formatter, type checker, build, tests. If they disagree with a map, the project's checks win.

Phrase results by what the gate proved: "script parses", "artifacts emitted", "range readable", "sampled relation corroborated", "exercised behaviour green". Do not write "the map is correct", "covers the repository", or "no hidden consumer".

## Anti-patterns

- Building a map or starting a server to find one symbol.
- Dumping the whole repository into context before a targeted read.
- Treating a tracked-only, thirteen-extension inventory as all the code.
- Reading `external_ref_edges.tsv` as a list of third-party packages.
- Ranking importance by fan-in, PageRank or how dense the picture looks.
- Deleting or declaring dead code because a graph shows no inbound edge.
- Reusing a line pointer or an entity key after edits or a reindex.
- Querying `localhost:7777` without reading `run.config`.
- Sending an entity key without URL encoding.
- Explaining a runtime value or a branch outcome from fan-out.
- Calling a cycle in the graph a runtime loop.
- Summarising a pull request from `gh pr view` alone and calling it the full history.
- Mixing issue comments, review comments and commit comments into one list.
- Using `gh search commits` as the commit archive.
- Running an unbounded repo-wide crawl to answer a question about one pull request.
- Copying a Clarity flag from a document without checking `--help` on the installed binary.
- Rebuilding a tool inside a dirty checkout.
- Using Strata to discover dependencies, or editing its database file.
- Reporting a Strata edit without `render_ok: true`.
- Counting two lexical tools that agree as independent confirmation.

## Bundled scripts

All paths are relative to this skill's directory.

| Script | Tool | What it does |
| --- | --- | --- |
| `scripts/build_rough_codebase_map.sh` | Rough map | `ROOT_DIR OUT_DIR`; env `MAX_GRAPH_EDGES`. Writes the TSV, Markdown and graph files. |
| `scripts/read_code_span_pointer.sh` | Rough map | `file:start:end` or `file start end`, optional context lines. Prints numbered lines. |
| `scripts/setup_parseltongue_1_7_2.sh` | Parseltongue | Downloads v1.7.2, creates a run folder, indexes, starts the server, writes `run.config`, runs smoke queries. |
| `scripts/reindex_parseltongue_1_7_2.sh` | Parseltongue | Stops the server, rebuilds the index inside the run folder, restarts, rewrites `run.config`. |
| `scripts/stop_parseltongue_server.sh` | Parseltongue | Stops the server recorded in `<run-folder>/server.pid`. |
| `scripts/collect_repo_context.sh` | GitHub | Bounded repo-wide capture to `raw/*.json` plus `manifest.json`. Needs `gh` and `python3`. |
| `scripts/collect_artifact_context.sh` | GitHub | Focused capture for one commit, pull request, issue or discussion. |
| `scripts/render_repo_context_digest.py` | GitHub | Renders a Markdown digest skeleton from a capture directory. |
| `scripts/probe_clarity.sh` | Clarity | Finds a binary and prints version plus help for each subcommand it has. Exits 1 when none is found. |
| `scripts/strata_mcp_probe.py` | Strata | Read-only probe: `--url`, `--kits`, `--json`. Exits 2 on error. |
| `scripts/strata_mcp_tool.py` | Strata | One MCP tool call: `<tool> [--args-json JSON or --args-file PATH] [--raw]`. Exits 2 on error. |

Deeper material is in [reference.md](reference.md): all Parseltongue workflows and flow patterns with query sequences, the full endpoint list, GitHub GraphQL queries and the surface matrix, Strata kit grammars and the tool list, failure tables for each tool, and worked examples.

## Self-check before you answer

- Did I state the question, the decision and the cost of a missed dependency?
- Did I pick the lightest tool that can answer it, and say why not the others?
- Did I record tool version, exact commands, repository revision and dirty state?
- Did I read the coverage report and name what the tool could not see?
- Did I read the source behind every candidate I present?
- Is every claim labelled candidate, observed, or verified for a stated scope?
- Did I avoid any claim of absence, safety or runtime behaviour that rests only on a graph?
- For Parseltongue: did the URL come from `run.config`, and are keys encoded and current?
- For GitHub: are the surfaces separate, the caps stated, and the raw JSON saved?
- For Clarity: did live help confirm every flag I used?
- For Strata: did validation pass, and did the response confirm the write?
- Did I leave the repository, GitHub and the user's tools unchanged unless asked?
- Did I say what to check next and when to stop?
