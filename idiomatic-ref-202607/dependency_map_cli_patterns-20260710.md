# Dependency Map Cli Patterns

Use this reference to build and interpret a **rough, disposable, CLI-only codebase map** when the immediate problem is orientation: which files and symbols are plausible entry points, which import/include neighborhoods deserve reading, and which exact `file:start:end` spans should enter context. The map is a hypothesis generator, not a semantic index or proof of complete blast radius.

The installed workflow combines `rg`, optional JSON-capable Universal Ctags, optional manual `ast-grep`, optional Graphviz `dot`, shell, and small Python transforms. It writes inventory, symbol, lexical edge, graph, tooling, and summary artifacts without a persistent database. That makes setup cheap and outputs inspectable, but precision is bounded by the files inventoried, supported extensions, parser branch, resolver heuristics, graph cap, and repository wiring style.

Choose the workflow by consequence:

| task_shape | rough_cli_map_fit | reason_and_required_followup |
| --- | --- | --- |
| unfamiliar repository orientation | strong fit | rank likely hubs, then read and verify a small set of exact spans |
| locate import/include neighborhood around a known feature | strong fit | combine query match with internal edges and inspect source plus tests/configuration |
| plan a bounded code review or likely change surface | useful first pass | verify every edge used to include or exclude a consequential file |
| tiny repository or one known symbol | often excessive | direct `rg -n`, file inventory, and exact reads may answer faster |
| exact callers/callees, runtime dispatch, DI/reflection, generated wiring | insufficient alone | escalate decisive questions to LSP, SCIP, compiler/build metadata, runtime traces, or focused tests |
| unsupported-language or untracked implementation dominates | misleading unless supplemented | audit coverage first and use language/repository-specific discovery |
| security, migration, destructive refactor, or production-impact guarantee | candidate generation only | require semantic and owner-reviewed evidence before changing scope |

**Default workflow**

1. **Frame the question.** Name the repository root, feature/error/symbol, desired decision, consequence of a missed edge, and whether the output is orientation, review scope, edit planning, or architecture explanation.
2. **Inspect state before writing artifacts.** Record current Git root/status, tracked versus untracked work relevant to the question, current repository instructions, intended output directory, and paths that must remain untouched. The builder creates its output directory and files.
3. **Confirm coverage and tools.** The current builder requires `rg` and also invokes `python3`. It recognizes only `.rs`, `.py`, `.js`, `.jsx`, `.ts`, `.tsx`, `.go`, `.java`, `.c`, `.cc`, `.cpp`, `.h`, and `.hpp`. In a Git worktree it inventories `git ls-files`, so untracked implementation is absent. Inspect `tooling.tsv` for capability flags, then inspect `symbols.tsv` kind values and `ctags.jsonl` state to determine whether Ctags output or fallback rows actually contributed; command presence alone is insufficient.
4. **Build into an explicit disposable location.** From the target repository root, invoke the selected installed script with an explicit root and output path. Avoid an output location whose files could be mistaken for product source or another agent's artifacts.
5. **Read metadata before graphs.** Open `tooling.tsv` and `summary.md`, then inspect `files.tsv`, `symbols.tsv`, `internal_file_edges.tsv`, and `external_ref_edges.tsv`. Treat counts and fan-in/fan-out as ranking signals, not importance proofs.
6. **Relate the query to candidates.** Rank files or symbols using query matches, ownership/configuration clues, internal neighbors, fan counts, tests, and entrypoint evidence. Do not select hubs from graph degree alone.
7. **Read exact spans.** Use pointer metadata to retrieve only the necessary source. Verify that the file exists, lines are in range, and a fallback one-line symbol pointer is expanded manually to the real definition body.
8. **Adjudicate material edges.** Open the import/include statement and target. Check aliases, manifests/build files, registries, generated code, framework conventions, runtime configuration, and tests that can confirm or contradict the lexical edge.
9. **Escalate selectively.** Use structural search for noisy syntax, language-server/compiler-aware navigation for exact relations, and runtime/build evidence for dynamic or generated wiring. Escalate only the unresolved facts that can change action.
10. **Return a bounded map result.** Provide top candidates with pointers, why each is relevant, verified local edges, known omissions/false positives, confidence by claim, and the next required read or tool.

The installed quick-start shape is:

```bash
bash /path/to/dependency-map-cli-tools-01/scripts/build_rough_codebase_map.sh \
  <repository-root> <explicit-output-directory>
```

Then inspect the artifacts rather than starting from the rendered graph:

```bash
cat <output-directory>/tooling.tsv
cat <output-directory>/summary.md
head -n 30 <output-directory>/symbols.tsv
head -n 30 <output-directory>/internal_file_edges.tsv
head -n 30 <output-directory>/external_ref_edges.tsv
```

For a reviewed pointer whose path contains no ambiguous colon:

```bash
bash /path/to/dependency-map-cli-tools-01/scripts/read_code_span_pointer.sh \
  path/to/file.ext:120:168
```

The reader also accepts separate file/start/end arguments, which is safer for a path containing a colon. It swaps reversed start/end values and adds context lines, but it does not prove that zero or beyond-end coordinates describe a real symbol. Never use an untrusted pointer to read arbitrary files outside the authorized repository scope.

**Artifact contract**

| artifact | current_local_meaning | key_limit |
| --- | --- | --- |
| `summary.md` | counts, detected tooling, top fan-out/fan-in, graph cap, and pointer-first reminder | rankings reflect extracted rows, not runtime centrality |
| `files.tsv` | inventoried supported source files and line counts | Git mode omits untracked/ignored files; unsupported extensions are absent |
| `symbols.tsv` | symbol, path, start/end, kind, and scope from Ctags or regex fallback | fallback sets `end_line` equal to the declaration line; regex language coverage is narrow |
| `import_edges.tsv` | raw lexical import/include references with source lines | a row can contain aliases, grouped syntax, package names, or false matches not resolved semantically |
| `internal_file_edges.tsv` | references matched to a known supported file by local heuristics | misses many module roots, aliases, generated paths, dynamic imports, Go modules, and framework wiring |
| `external_ref_edges.tsv` | extracted references not resolved to the current code inventory | "external" means unresolved, not necessarily third-party; local misses can appear here |
| `dependency_graph.mmd` | edge-capped Mermaid representation of ranked edge pairs | labels and cap can omit or misrender unusual paths; graph completeness is not implied |
| `dependency_graph.dot` | DOT representation of the same capped pairs | remains source text when Graphviz is absent |
| `dependency_graph.svg` | optional Graphviz rendering | exists only when compatible `dot` execution succeeds |
| `tooling.tsv` | capability flags observed by the builder | availability does not prove actual contribution; Ctags may pass the probe yet yield no usable output, causing fallback, and ast-grep is only recorded |

At this evolution capture, `rg` and `ast-grep` were discoverable, the available system `ctags` did not pass the builder's JSON-capability probe, and `dot` was absent. Therefore an actual run in the same unchanged environment would use regex symbol extraction, produce one-line fallback ranges, record structural-search availability without applying it, and omit SVG. This is environment evidence, not a permanent default; inspect every run's `tooling.tsv`.

**Coverage audit before interpretation**

- In a Git repository, compare `git ls-files` and relevant `git status --short` output with the task. Untracked new code will not enter `files.tsv`.
- Confirm that the implementation language appears in the extension filter. Kotlin (`.kt`, `.kts`), Ruby, C#, Swift, PHP, shell, build files, manifests, and many configuration formats are not mapped by this script.
- Record generated/vendor/submodule/symlink policy. Being tracked does not make generated or vendored edges architecturally owned.
- Inspect `tooling.tsv` before trusting symbol ranges. Command presence alone is weaker than the script's capability probe.
- Record `MAX_GRAPH_EDGES` when graph shape influences discussion. Capped rendering does not remove rows from TSV artifacts, but it can hide edges visually.
- Inspect unresolved references around the query; a large unresolved set can signal aliases or resolver mismatch rather than external dependency volume.

**Confidence by claim**

- **Inventory confidence:** high only for tracked files in the supported extension set under the captured root; lower when untracked, generated, submodule, or unsupported-language code matters.
- **Symbol confidence:** higher for reviewed JSON Ctags spans; lower for regex one-line declarations, nested definitions, overloads, and unusual syntax.
- **Edge confidence:** moderate for a directly inspected conventional relative import/include resolved to the correct file; low for unresolved, aliased, dynamic, generated, or framework-mediated wiring.
- **Ranking confidence:** a useful retrieval heuristic after query and ownership evidence; never a standalone architecture or risk score.
- **Action confidence:** earned only after the decisive source, configuration, tests, and precise-tool evidence agree sufficiently for the consequence.

Good use asks where request validation enters an unfamiliar TypeScript service, builds a tracked-file map, notes that JSON Ctags is unavailable, combines `rg` matches with internal neighbors, expands one-line pointers, checks path aliases and tests, and returns three bounded candidates with explicit gaps. Bad use sees no edge from a controller to a generated registry and declares the registry unaffected. A borderline use maps the tracked TypeScript core while relevant untracked files exist; it can still guide baseline reading, but the final result must keep untracked-code impact pending and probe it separately.

Return results in this shape:

```text
Candidate 1
- Pointer: path/to/file.ext:10:42
- Why: query match plus a reviewed graph/ownership relation
- Verified local edges: exact source pointers or none yet
- Coverage: tracked/supported/tool branch relevant to this candidate
- Confidence: high | medium | low, with reason
- Uncertainty: missing or potentially false relations
- Next probe: smallest read, structural query, test, or precise tool that can change action
```

Stop once the smallest sufficient candidate set and its material relations are verified. If map output cannot distinguish likely ownership, omits a consequence-bearing language/state surface, or conflicts with source/tests, do not compensate by reading every artifact. Switch to the language, build, runtime, or repository authority that can answer the exact unresolved question.

The deeper rule is **pointer first, precision on demand**. A rough map earns trust by exposing its coverage and making false conclusions easy to challenge. Its success is reduced reading and better next probes, not graph size, edge count, visual polish, or the appearance of complete architecture knowledge.

## Source Evidence Mapping Table

This map routes one claim to the evidence capable of supporting it. It is not a source-count vote. Repository instructions and user intent govern scope and authorization. The selected scripts govern extraction mechanics. A particular run's artifacts establish what was actually inventoried and emitted. Source, tests, configuration, and precise tooling establish whether a relation is real enough for action. Public links can provide future precedent after refresh, but they cannot repair missing local coverage.

| source_location_path_key | source_category_artifact_type | evidence_status_and_capture | source_usage_synthesis_role | important_boundary_or_invalidation |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202602/dependency-map-cli-tools-01/SKILL.md` | archived_workflow_snapshot | `local_corpus_sourced_fact`; SHA-256 `b20aa296d11385ccfd9e0b5e35e2653768363a9c144e2d04f2e583c3c1b19806` | Historical pointer-first workflow, artifact list, tool strategy, response contract, and practical limits. | Byte-identical to the 202603 and installed current skill at capture; it is lineage, not independent corroboration or current run evidence. |
| `agents-used-monthly-archive/codex-skills-202602/dependency-map-cli-tools-01/references/internet-precedents.md` | archived_precedent_snapshot | `local_corpus_sourced_fact_about_archived_text`; SHA-256 `6225de10e11642bd9df819b33bfc01835f6af5659c0680ded4dad784929f6637` | Historical rationale for pointer-first navigation, precise-search fallback, structural search, Ctags, ripgrep, and simple graph rendering. | Its linked public pages were not opened in this evolution; inherited descriptions are not refreshed external facts. |
| `agents-used-monthly-archive/codex-skills-202603/dependency-map-cli-tools-01/SKILL.md` | archived_duplicate_workflow_snapshot | `local_corpus_sourced_fact`; same SHA-256 as 202602/current | Confirms no byte change across these captured workflow snapshots. | Duplicate bytes contribute continuity, not another independent authority. |
| `agents-used-monthly-archive/codex-skills-202603/dependency-map-cli-tools-01/references/internet-precedents.md` | archived_duplicate_precedent_snapshot | `local_corpus_sourced_fact_about_archived_text`; same SHA-256 as 202602/current | Confirms the historical precedent note was unchanged across archive captures. | Does not refresh LSP, Sourcegraph, Tree-sitter, ast-grep, Ctags, ripgrep, Graphviz, or dependency-cruiser behavior. |
| `/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/SKILL.md` | installed_current_workflow | `current_local_explanatory_fact`; SHA-256 `b20aa296d11385ccfd9e0b5e35e2653768363a9c144e2d04f2e583c3c1b19806` | Current local entrypoint for rough-map purpose, workflow, artifacts, tool roles, validation, output contract, and escalation. | Identical prose does not prove the current scripts or environment are identical to an archive. |
| `/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/references/internet-precedents.md` | installed_current_historical_research_note | `current_local_fact_about_unrefreshed_note`; SHA-256 `6225de10e11642bd9df819b33bfc01835f6af5659c0680ded4dad784929f6637` | Explains why the skill was designed around pointers, hybrid precision, structural search, symbol spans, lexical search, and simple rendering. | The note's outbound sources remain unopened here; use it as design lineage and a future query index. |
| `/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/scripts/build_rough_codebase_map.sh` | installed_executable_builder | `current_local_executable_source`; SHA-256 `ea180f643cfa45edccdac825f5c4f263d0060f9edc9741a67adb8b93f7bd5ef3`; `bash -n` passed | Defines required commands, Git/rg inventory branch, extension filter, Ctags capability probe, regex fallback, lexical patterns, resolver candidates, graph cap/rendering, TSV schemas, and summary calculations. | Source review predicts behavior; only an authorized run proves artifacts for a target root. Any script hash change invalidates derived-mechanics claims. |
| `/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/scripts/read_code_span_pointer.sh` | installed_executable_pointer_reader | `current_local_executable_source`; SHA-256 `5c1f54948a789d67ed8cf803c3e5291156e3ccac74ac01f43b70888198b8066d`; `bash -n` passed | Defines pointer/separate-argument parsing, integer checks, reversed-range swap, context expansion, and numbered source output. | It accepts any existing authorized file, has colon-path ambiguity in pointer form, and does not validate symbol identity or line bounds semantically. |
| `/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/agents/openai.yaml` | installed_agent_metadata | `current_local_explanatory_fact`; SHA-256 `3cca38f60acf2bfa2e5f310301807d35e476ab4bcead18695bf101733ca2ab71` | Current display name, short description, and default invocation prompt. | Trigger metadata does not prove extraction quality or authorize writing map artifacts. |
| target repository instructions and user request | repository_policy_and_intent | `operation_specific_authority`; not captured by generic skill | Defines allowed root/output paths, ownership, query, ignored/generated/vendor policy, no-write constraints, and consequence of missed edges. | Must be reread for each repository/task and cannot be inferred from script access. |
| `git rev-parse`, `git ls-files`, and `git status --short` for target root | repository_state_observation | `operation_specific_local_state` | Establishes whether the builder will use tracked-only inventory and which relevant untracked changes need a supplement. | State expires with worktree changes; Git tracked status does not establish architectural ownership. |
| `tooling.tsv` from one map run | derived_run_metadata | `operation_specific_executable_observation` | Records the builder's `rg`, JSON-Ctags capability-probe result, ast-grep availability, and `dot` availability for that invocation. | Capability does not prove contribution: inspect `symbols.tsv` kinds and `ctags.jsonl`; ast-grep availability never means automatic structural extraction occurred. |
| `files.tsv`, `symbols.tsv`, `import_edges.tsv`, `internal_file_edges.tsv`, `external_ref_edges.tsv` | derived_run_artifacts | `operation_specific_best_effort_evidence` | Provide inventory, candidate pointers, raw references, heuristic local resolutions, and unresolved references for a captured root/tool branch. | Every artifact inherits inventory, parser, resolver, filesystem, and timing limits; unresolved does not mean third-party. |
| `summary.md`, `dependency_graph.mmd`, `dependency_graph.dot`, optional `dependency_graph.svg` | derived_summary_and_views | `operation_specific_ranked_view` | Prioritize candidate files and communicate a capped subset of edge pairs. | Summary counts and graph degree are retrieval signals, not semantic centrality, ownership, complete blast radius, or runtime behavior. |
| exact source spans, tests, manifests/build files, configuration, generated registries, and ownership records | target_repository_primary_evidence | `operation_specific_verification` | Confirm or refute map hypotheses used for a next read, review boundary, or edit plan. | One source read may still miss runtime wiring; choose further evidence by consequence. |
| LSP/SCIP/compiler/build-system queries or runtime traces | precise_or_dynamic_evidence | `adjacent_tool_evidence_when_executed` | Resolve exact symbols/call hierarchy, aliases, generated wiring, and runtime relations beyond the rough map. | Tool coverage and freshness must be recorded; precision infrastructure is not automatically available. |
| `https://developers.openai.com/codex/guides/agents-md` | external_research_source_material | `unrefreshed_external_pointer` | Future current source for Codex instruction-file scope when repository agent instructions affect map execution. | Not opened; it does not define dependency extraction or prove this repository's instructions. |
| `https://docs.github.com/actions` | external_research_source_material | `unrefreshed_external_pointer` | Future source when a map/verification workflow is intentionally automated in GitHub Actions. | Not opened; CI documentation cannot prove local graph correctness or authorize workflow changes. |
| `https://agents.md/` | external_research_source_material | `unrefreshed_external_pointer` | Future general instruction-format context when cross-tool repository guidance is consequential. | Not opened; it does not define this mapper, local policy, or dependency semantics. |

The archive precedent note also contains links for LSP 3.17, Sourcegraph precise navigation, Tree-sitter, ast-grep, Universal Ctags, ripgrep, Graphviz, and dependency-cruiser. None was refreshed. Preserve them as historical rationale and future primary/implementation leads, not as present-tense claims about current versions or guarantees.

**Claim-driven retrieval order**

1. Read the user's question and target repository instructions. Decide whether a map is needed and what a false negative would cost.
2. Inspect repository root, Git state, language/extensions, generated/vendor/submodule policy, and relevant untracked files before choosing inventory scope.
3. Select and hash the builder and pointer reader that will execute. Run syntax and exact capability probes when behavior matters.
4. Build only into an authorized explicit output directory. Record command, root, output, edge cap, time/state anchor, and result.
5. Read `tooling.tsv`, `summary.md`, and `files.tsv` before trusting symbols or edges.
6. Read TSV artifacts as hypotheses. Trace every candidate or exclusion used in a consequential decision back to source, tests, configuration, or a precise tool.
7. Use historical notes to explain the design and locate future research; do not let their linked descriptions override observed local behavior.
8. Stop loading evidence once candidate choice, material relation, confidence, and next action are sufficiently supported.

**Evidence pipeline and invalidation**

```text
request + repository policy/state
  -> selected builder + environment capability
  -> file inventory
  -> symbols + raw references
  -> heuristic resolved/unresolved edges
  -> capped summary/graphs
  -> ranked candidate pointers
  -> direct source/test/config/precise verification
  -> bounded next action
```

A root or Git-state change reopens inventory. An extension-filter or file-list change reopens every downstream artifact. A Ctags/tool branch change reopens span confidence. A resolver change reopens internal/external classification, fan counts, and graph views. A graph-cap change reopens only rendered-view completeness, not TSV rows. A source edit reopens pointers and relations for affected files. A test/config/runtime change can invalidate the code-level conclusion even when map artifacts are unchanged.

**Observed capture facts**

- The 202602, 202603, and current installed skill files are byte-identical; their precedent notes are also byte-identical.
- Both installed shell scripts pass shell syntax parsing at capture.
- `rg` and `ast-grep` were discoverable. The system `ctags` did not satisfy the builder's JSON output probe, and `dot` was absent.
- The builder records ast-grep availability but does not invoke ast-grep automatically.
- No map was generated during this reference evolution because writes were restricted to the reference, packet, and Delta journal.
- No public URL was opened; current external content and applicability remain unknown.

Good source use notices relevant untracked TypeScript code, records that the builder's Git branch excludes it, runs the tracked baseline only when authorized, supplements the missing files, and verifies candidate edges in source/tests. Bad use reads `summary.md` alone and declares the top fan-in file the architecture owner. Borderline use runs a repository-pinned archived toolchain: it is acceptable when the pin is explicit, outputs are tied to that version, and material conclusions are verified against current repository code.

For every consequential result retain: request, root/state, selected script hashes, capability branch, output identity, inventory coverage, artifact rows used, direct verification, rejected alternative, uncertainty, and invalidation trigger. A map is current only for that evidence chain; the existence of a familiar output directory is not proof that its contents match today's repository.

## Pattern Scoreboard Ranking Table

This scoreboard is an ordered decision aid, not a benchmark. The inherited values `95`, `91`, and `88` are preserved for archive continuity, but the available sources provide no scoring rubric, trial population, error bars, or outcome series from which to interpret them as percentages. A value of `95` therefore means "ranked first by the seed reference," not "95 percent accurate" or "95 percent likely to work." Small gaps between values have no statistical meaning.

| pattern_identifier_stable_key | inherited_score | adoption_tier | operational_control | default_action | primary_failure_prevented | lower_priority_or_escalation_condition |
| --- | ---: | --- | --- | --- | --- | --- |
| `dependency_map_cli_patterns` | 95 | default | Source Map First | Identify the frozen guidance, current scripts, repository state, generated artifacts, and direct source reads before interpreting a map. Include an inventory coverage check in this first control. | Conclusions whose provenance cannot be reproduced or whose input set silently omitted relevant files. | Keep this lightweight for reversible navigation; escalate the inventory audit when absence, deletion, ownership, or security claims depend on coverage. |
| `dependency_map_cli_patterns` | 91 | default | Evidence Boundary Split | Label each statement as observed local fact, artifact observation, external precedent, inference, or unresolved uncertainty. | A lexical edge, historical recommendation, or current environment probe being restated as authoritative code behavior. | A private scratch note can use shorter labels, but any handed-off conclusion still needs a visible evidence class. |
| `dependency_map_cli_patterns` | 88 | default | Verification Gate Coupling | Attach every consequential recommendation to a source read, artifact check, repository-native command, or more precise analyzer. | Plausible graph interpretations surviving because no falsification step was named. | A file-discovery hint may use pointer resolution alone; behavior, absence, and reachability claims require stronger corroboration. |
| `dependency_map_cli_patterns` | unscored | default | Pointer Before Dump | Query compact indexes and read only selected `file:start:end` spans before loading whole files. | Context dilution, repeated scanning, and accidental treatment of unrelated code as supporting evidence. | Read the whole file when definitions depend on module-level configuration, generated regions, macro context, or distant invariants. |
| `dependency_map_cli_patterns` | unscored | default | Sample Relations Before Ranking | Verify at least one consequential positive edge and one suspicious missing or unresolved relation before naming hubs or boundaries. | Centrality and blast-radius claims built on resolver mistakes, aliases, unsupported syntax, or presentation truncation. | More than sampling is required when the decision needs complete recall; route that case to semantic or runtime evidence. |
| `dependency_map_cli_patterns` | unscored | conditional | Precision Escalation | Move from rough lexical mapping to repository-native, language-aware, compiler-derived, or runtime tools as the consequence of error rises. | Reusing a discovery tool for authorization, deletion, migration completeness, or production reachability decisions it cannot support. | Stay with the rough map when the output is explicitly provisional, cheap to reverse, and followed by direct reading before action. |

The first three rows preserve the seed ranking. The added rows make its implicit control flow explicit. Operationally, `Source Map First` includes coverage before graph interpretation: the map cannot be more representative than its inventory. The controls then form a loop rather than a one-way checklist:

1. Establish sources and inventory coverage.
2. Separate what was observed from what was inferred.
3. Query compact artifacts and resolve selected pointers.
4. Verify representative relations and consequential claims.
5. Return to inventory or extraction settings when checks fail.
6. Escalate precision when the remaining uncertainty can change the decision.

**Task-sensitive priority overrides**

| task | highest-priority control | acceptable first evidence | required escalation trigger |
| --- | --- | --- | --- |
| Locate a likely implementation file | Pointer Before Dump | A matching index row plus a readable source span. | The pointer is stale, ambiguous, outside the intended language set, or insufficient to identify the implementation. |
| Explain a module boundary | Source Map First | Inventory metadata, relation rows, and direct reads on both sides of the proposed boundary. | Framework wiring, generated code, aliases, or unresolved edges materially affect the explanation. |
| Rank likely dependency hubs | Sample Relations Before Ranking | Full TSV counts, extraction-mode metadata, and sampled source confirmation. | The rendered graph is capped, coverage is partial, or sampled edges reveal systematic resolver errors. |
| Scope a refactor | Verification Gate Coupling | Candidate inbound and outbound relations followed by repository-native tests and source reads. | Missing a consumer could break a public contract, migration, persistence format, or runtime registration. |
| Assert that nothing depends on an entity | Precision Escalation | The rough map may identify candidates but cannot establish absence by itself. | Always escalate to a semantic, compiler-derived, repository-native, or otherwise authoritative check appropriate to the language. |
| Approve deletion or security-boundary change | Precision Escalation | Direct code evidence plus the strongest available static and runtime checks. | The rough map remains useful only as an auxiliary discovery artifact, never as sole authorization. |

**How to apply the scores without false precision**

- Preserve the inherited numbers when comparing this file with its archive seed, but do not average them, convert them to confidence percentages, or use the small gaps to settle a disputed decision.
- Rank controls by the failure they prevent in the current task. A coverage defect can invalidate every graph observation, while a missing visual render may not matter if the TSV artifacts are complete.
- Distinguish artifact completeness from presentation completeness. The builder can cap rendered graph edges through `MAX_GRAPH_EDGES` while retaining more rows in its tabular artifacts, so hub judgments should begin with the full rows rather than the picture.
- Treat tool branches as evidence. JSON-capable Universal Ctags can provide richer spans; the regex fallback may set `end_line` equal to `start_line`. The same repository can therefore yield different pointer quality on two machines without any source change.
- Treat unresolved references as questions, not classifications. A lexical resolver miss may reflect aliases, language conventions, generated wiring, dynamic loading, or an actual external dependency.

**Good, bad, and borderline uses**

| classification | example | why |
| --- | --- | --- |
| good | The operator compares tracked source counts with `all_files.txt`, `code_files.txt`, and `files.tsv`, records the extraction branch, inspects full relation rows, verifies a high-impact edge in source, and calls the resulting hub ranking provisional. | The conclusion retains provenance and has an explicit falsification path. |
| bad | A review states that the map is 95 percent reliable because the first row scores 95, then approves deletion because no incoming edge is visible. | The claim invents calibration and turns heuristic absence into authorization. |
| borderline | A developer uses one index pointer to open a likely file without auditing every supported extension. | This is reasonable for reversible navigation if no behavior or completeness claim is handed off. |
| improved borderline | The same developer labels the pointer as a candidate and names direct source reading as the next step. | The remaining uncertainty is visible and cannot silently become a durable architectural fact. |

**Verification gates for the ranked controls**

| control | quick gate | stronger gate | evidence to retain |
| --- | --- | --- | --- |
| Source Map First | Compare repository source inventory assumptions with generated `all_files.txt`, `code_files.txt`, and `files.tsv`, then inspect metadata for ignored, untracked, unsupported, or generated paths. | Build an independent inventory with repository-native tooling and reconcile every material difference. | Command, working tree state, extension policy, counts, timestamp, and artifact hash when durability matters. |
| Evidence Boundary Split | Audit a sample of prose claims and identify the local source, artifact row, external source, or inference behind each one. | Require claim-level provenance for all recommendations that authorize code changes. | Claim ledger with source class and unresolved caveats. |
| Verification Gate Coupling | Resolve each cited pointer and inspect selected relation endpoints in source. | Run language-aware analysis, repository tests, compiler checks, or runtime observation suited to the claim. | Commands, versions, selected samples, failures, and decision impact. |
| Pointer Before Dump | Check that `file:start:end` resolves inside the current file and that the span contains the expected construct. | Read surrounding module context or the complete file when local lines do not establish semantics. | Pointer, context width, source revision, and any range correction. |
| Sample Relations Before Ranking | Confirm one important positive edge and investigate one suspicious absence or unresolved row. | Use stratified samples across languages, relation types, directories, and extraction branches. | Sampling rationale, match class, mismatch taxonomy, and observed rate without overgeneralizing it. |
| Precision Escalation | State why the rough map is insufficient for the pending decision. | Use the authoritative semantic or runtime mechanism and reconcile disagreements with the lexical artifacts. | Tool identity, configuration, coverage limits, conflicting results, and final rationale. |

The scoreboard succeeds when it changes operator behavior: sources are identified before conclusions, compact evidence is inspected before context expands, important claims acquire checks, and the method explicitly yields when its extraction model is too weak. It fails when the visual map or inherited number becomes a substitute for those controls. A future evidence-based score could be derived from repeated, documented mismatch samples and downstream outcomes, but that local metric must remain separate from the inherited editorial values until its denominator, sampling policy, and decision scope are stable.

## Idiomatic Thesis Synthesis Statement

**Governing thesis:** A rough CLI dependency map is a reproducible hypothesis generator, not a complete program model. Use current local implementation and repository state to build a coverage-audited map, query compact artifacts before loading broad context, resolve selected pointers into source, and verify each consequential conclusion with evidence strong enough for the action. Escalate to repository-native, language-aware, compiler-derived, build-system, or runtime analysis whenever lexical evidence cannot falsify the claim or the cost of a false negative is material.

This thesis preserves and sharpens the seed's three evidence statements:

- `local_corpus_sourced_fact`: The archive row for `dependency_map_cli_patterns` names four local source paths. Those paths are the first retrieval surface for historical intent, but the currently installed scripts are the stronger source for present executable behavior.
- `external_research_sourced_fact`: The external source map retains public documentation, repository, and ecosystem analogues. In this no-browse evolution, those links are unrefreshed research pointers rather than newly verified facts about current upstream behavior.
- `combined_evidence_inference_note`: Reliable use comes from reconciling historical guidance, current scripts, current environment capabilities, generated run artifacts, direct source reads, and claim-specific verification. The sequence is adaptive: a failed check sends the operator back to the stage that produced the weak evidence.

**The bounded evidence loop**

| stage | decision answered | minimum evidence | output state | return or escalation condition |
| --- | --- | --- | --- | --- |
| 1. Preflight | Can the local builder and pointer reader run in this environment? | Script syntax, required `rg`, Python availability, optional Ctags and Graphviz capability, repository root, and writable authorized output path. | `environment_observed` | Fix missing required capabilities; record optional fallback branches before comparing runs. |
| 2. Inventory | Which files can this run actually observe? | Repository mode, `all_files.txt`, `code_files.txt`, `files.tsv`, tracked/untracked and ignored-file policy, supported extension list, generated/vendor policy, and independent source counts where consequence warrants. | `coverage_bounded` | Revise inventory or switch tools when relevant source classes are omitted. |
| 3. Extraction | What symbol and relation representation was produced? | Run metadata, extraction branch, symbol rows, import/include rows, unresolved rows, and edge-cap settings. | `artifact_observed` | Rebuild after configuration changes; question one-line fallback spans or systematic unresolved classes. |
| 4. Query | Which files, symbols, or neighborhoods are candidates? | Compact index and TSV filters, rank rationale, and full-row counts before rendered-graph interpretation. | `candidate_identified` | Broaden or narrow the query when results are empty, noisy, duplicated, or presentation-capped. |
| 5. Pointer read | Does the selected span contain the expected construct? | Resolved `file:start:end` range with enough context and the source revision to which it applies. | `source_observed` | Correct stale or ambiguous ranges; read the complete module when local lines do not establish semantics. |
| 6. Claim verification | Does the code or authoritative project mechanism support the intended conclusion? | Direct source evidence plus tests, compiler/build output, language-aware analysis, or runtime observation appropriate to the claim. | `claim_verified` or `claim_refuted` | Return to inventory, extraction, or resolver assumptions when evidence disagrees. |
| 7. Decision | Is remaining uncertainty acceptable for the proposed action? | Consequence, reversibility, corroboration, known omissions, and an explicit owner for unresolved risk. | `actionable` or `escalation_required` | Do not act on heuristic absence, reachability, or security claims without stronger evidence. |

The loop stops when the evidence is sufficient for the action, not when the builder exits successfully. A file-navigation hint can stop after a valid pointer and direct reading. A behavior explanation normally requires source confirmation. A claim that nothing depends on a symbol, that a component is safe to delete, or that a security boundary has no alternate path requires a stronger semantic or runtime mechanism.

**Claim-strength ladder**

| label | permitted statement | evidence floor | prohibited promotion |
| --- | --- | --- | --- |
| `candidate` | "This file or symbol is worth inspecting." | A compact artifact match with known inventory scope. | Do not restate it as the implementation or owner without reading source. |
| `observed` | "This generated row or source span contains this text or lexical relation." | A current artifact row or resolved source range. | Do not infer complete behavior, causality, or absence from observation alone. |
| `corroborated` | "Multiple independent evidence sources agree on this relation." | Direct source plus another suitable static, build, test, or runtime check. | Do not imply universal coverage when both sources share the same blind spot. |
| `verified` | "This claim is strong enough for the stated decision under recorded boundaries." | Claim-specific authoritative evidence and explicit remaining uncertainty. | Do not reuse verification outside its repository revision, configuration, workload, or action scope. |
| `unresolved` | "Available evidence conflicts or cannot observe the relation." | Recorded mismatch, missing capability, or unsupported construct. | Do not convert uncertainty into either presence or absence for convenience. |

**Where the default fits**

The local-first rough-map default works especially well for first-contact orientation, locating likely implementations, identifying conventional static import neighborhoods, preparing focused code review, and finding candidate refactor surfaces. It assumes readable local source, an authorized artifact location, and enough conventional static structure for lexical evidence to reduce the search space. Its success criterion is a smaller, better-ranked set of source reads, not proof that the map captured every relationship.

The default becomes a secondary aid when any of the following dominates the decision:

- dynamic imports, reflection, runtime registration, dependency injection, macros, code generation, build-script composition, feature-conditional wiring, or framework conventions invisible to lexical scanning;
- unsupported or omitted source extensions, relevant untracked or ignored files, vendored or generated sources, or a non-Git inventory whose policy differs from the target question;
- complete caller or dependency absence, security reachability, deletion authorization, migration completeness, licensing provenance, or another conclusion where a false negative has material cost;
- a repository-native analyzer, compiler query, language server, build graph, or runtime trace that can answer the exact claim more directly and precisely.

In those cases, the rough map may still supply vocabulary and candidate paths, but it must not be the primary authority.

**Evidence selection by decision**

| pending decision | economical first method | evidence needed before action | why the boundary matters |
| --- | --- | --- | --- |
| Open the likely implementation | Query an index and resolve one pointer. | Read the span and enough surrounding context to identify the construct. | A wrong candidate is cheap to reverse. |
| Explain why two modules appear coupled | Inspect relation rows and both endpoint files. | Confirm the import or include semantics and any intervening abstraction. | Lexical adjacency does not establish runtime dependency direction. |
| Prioritize a review hotspot | Rank full tabular relations and sample important edges. | Reconcile presentation caps, coverage gaps, and false-edge classes. | A visually dense node may reflect extraction bias or duplicated rows. |
| Change a shared interface | Use the map to identify possible consumers. | Run authoritative search, compile/build checks, tests, and language-aware analysis as available. | Missing one consumer can break a contract outside the visible neighborhood. |
| Delete an apparently unused component | Treat empty inbound results as a prompt to investigate. | Establish absence through appropriate semantic/build/runtime evidence and project policy. | Heuristic non-observation is not evidence of non-existence. |
| Modify a security boundary | Use the map only for initial candidate enumeration. | Apply security-specific static, configuration, test, and runtime verification. | Dynamic paths and configuration can dominate the actual attack surface. |

**Known, conditional, and unknown**

| confidence class | current statement | boundary |
| --- | --- | --- |
| known from frozen local implementation | Inside a Git worktree, the builder uses tracked-file inventory; it recognizes a finite set of extensions; it can use JSON-capable Ctags or a regex fallback; its resolver is lexical; Graphviz rendering is optional; and rendered edges can be capped. | These statements apply to the hashed scripts read for this evolution and can change when those files change. |
| known from current capability probes | `rg` and `ast-grep` were detected; the available system Ctags did not pass the JSON capability probe; `dot` was absent. | A future shell, `PATH`, machine, or installed tool set can select different branches. |
| reasoned default | Coverage-first, pointer-first, verification-coupled use is a low-cost way to orient before deeper analysis. | Its value depends on task consequence, source conventions, and operator discipline. |
| unmeasured until a run | Repository-specific inventory recall, symbol-span quality, relation precision and recall, hub ranking stability, and unresolved-edge causes. | These require generated artifacts, independent comparison, and direct sampling on the target revision. |
| intentionally unverified here | Current claims behind retained public URLs and ecosystem tools. | No browsing is authorized; use the links as future research queues rather than current attestations. |

**Falsification checklist**

Before promoting a map observation into an actionable conclusion, ask:

1. Could the relevant file be untracked, ignored, generated, vendored, unsupported by extension, or outside the chosen root?
2. Which extraction branch produced the span, and does the pointer resolve to the expected construct?
3. Could aliases, re-exports, conditional compilation, dynamic loading, framework registration, or runtime data create a relation the lexical resolver cannot see?
4. Is the conclusion based on complete tabular rows or only an edge-capped rendering?
5. Has at least one consequential positive relation and one suspicious absence or unresolved relation been checked directly?
6. What evidence source would disagree if the current interpretation were false?
7. Is the remaining uncertainty acceptable for this action's consequence and reversibility?

**Scenario contrast**

Good: "The map identifies `src/registry.rs` as a candidate hub. The tracked inventory covers the relevant Rust files, the full relation table contains 18 inbound rows, two representative imports are confirmed in source, and the repository's build and tests pass after the scoped change. The hub label remains bounded to static relations on this revision."

Bad: "The rendered graph has no incoming arrow to `legacy.rs`, so the file is unused and can be removed." This conclusion ignores edge caps, inventory omissions, extraction limits, dynamic wiring, and the difference between non-observation and absence.

Borderline but acceptable for navigation: "The symbol index points to `src/registry.rs:42:42`; open that candidate and inspect surrounding context." The one-line range may reflect fallback extraction, but no semantic claim is made before the read.

The deeper consequence is that mismatches are routing information. A missing file redirects the operator to inventory policy; a weak span redirects to extraction capability; a false relation redirects to resolver assumptions; a semantic disagreement redirects to a stronger analyzer. This makes limitations operational instead of ceremonial. The method remains fast because it escalates only where a failed premise or consequential decision demands more evidence.

## Local Corpus Source Map

The local corpus has four evidence layers: historical guidance, current executable implementation, run-specific artifacts, and target source. They are connected but not interchangeable. Historical prose explains intended use; scripts define possible mechanics; run artifacts show which mechanics and inputs were selected; target source and authoritative project checks establish semantics.

**Preserved archive sources**

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role | observed_content_identity | authority_boundary |
| --- | --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202602/dependency-map-cli-tools-01/SKILL.md | dependency-map-cli-tools-01 | Dependency Map CLI Tools 01; Overview; Workflow; Quick Start; Artifacts; Tool Strategy | Historical skill entrypoint and reusable agent workflow. | SHA-256 `b20aa296d11385ccfd9e0b5e35e2653768363a9c144e2d04f2e583c3c1b19806`; byte-identical to the observed 202603 and current skill copies. | Supports archived intent and documented artifact usage, not proof of a current run or target-code behavior. |
| agents-used-monthly-archive/codex-skills-202602/dependency-map-cli-tools-01/references/internet-precedents.md | Internet Precedents: No-DB Codebase Mapping | Internet Precedents: No-DB Codebase Mapping; 1) Pointer-first navigation is standard; 2) "Precise first, search fallback" works in practice; 3) Concrete syntax trees and structural search are reliable primitives; 4) ctags gives cross-language symbol spans cheaply; 5) ripgrep is a strong lexical baseline | Historical rationale and queue of public precedents. | SHA-256 `6225de10e11642bd9df819b33bfc01835f6af5659c0680ded4dad784929f6637`; byte-identical to the observed 202603 and current precedent copies. | Supports provenance for design influences; retained public links are unrefreshed in this no-browse evolution. |
| agents-used-monthly-archive/codex-skills-202603/dependency-map-cli-tools-01/SKILL.md | dependency-map-cli-tools-01 | Dependency Map CLI Tools 01; Overview; Workflow; Quick Start; Artifacts; Tool Strategy | Later archive snapshot of the same workflow. | Same observed skill hash `b20aa296d11385ccfd9e0b5e35e2653768363a9c144e2d04f2e583c3c1b19806`. | Confirms persistence across archive paths but is not independent substantive corroboration. |
| agents-used-monthly-archive/codex-skills-202603/dependency-map-cli-tools-01/references/internet-precedents.md | Internet Precedents: No-DB Codebase Mapping | Internet Precedents: No-DB Codebase Mapping; 1) Pointer-first navigation is standard; 2) "Precise first, search fallback" works in practice; 3) Concrete syntax trees and structural search are reliable primitives; 4) ctags gives cross-language symbol spans cheaply; 5) ripgrep is a strong lexical baseline | Later archive snapshot of the same rationale. | Same observed precedent hash `6225de10e11642bd9df819b33bfc01835f6af5659c0680ded4dad784929f6637`. | Preserves temporal path provenance without multiplying the evidentiary weight of identical bytes. |

Hash equality collapses repeated interpretation, not provenance. The four paths remain listed because their dates and locations are part of the archive record, but the two skill files count as one semantic source family and the two precedent files count as another. Surrounding package state could still differ even when these file bytes do not.

**Current installed sources read for this evolution**

| source | observed_sha256 | strongest supported claim | insufficient by itself for | freshness trigger |
| --- | --- | --- | --- | --- |
| `/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/SKILL.md` | `b20aa296d11385ccfd9e0b5e35e2653768363a9c144e2d04f2e583c3c1b19806` | Current documented workflow, artifact contract, tool strategy, and verification suggestions on this machine. | Exact implementation branches, selected run behavior, repository coverage, or semantic correctness. | Reread and rehash after skill installation, update, or local edit. |
| `/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/references/internet-precedents.md` | `6225de10e11642bd9df819b33bfc01835f6af5659c0680ded4dad784929f6637` | Current locally retained rationale and public research pointers. | Present upstream versions, current external documentation, or target-repository facts. | Reread on local file change; browse only when separately authorized and current external facts matter. |
| `/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/scripts/build_rough_codebase_map.sh` | `ea180f643cfa45edccdac825f5c4f263d0060f9edc9741a67adb8b93f7bd5ef3` | Inventory, extension filtering, Ctags/fallback extraction, lexical relation resolution, edge capping, rendering, and artifact-writing mechanics implemented in the frozen builder. | Which branch a future environment takes, whether a target inventory is representative, or whether inferred edges match program semantics. | Reread and rerun syntax/capability checks whenever the hash, shell, Python runtime, `PATH`, options, or repository changes. |
| `/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/scripts/read_code_span_pointer.sh` | `5c1f54948a789d67ed8cf803c3e5291156e3ccac74ac01f43b70888198b8066d` | Accepted pointer forms, range normalization, context expansion, and line-reading behavior in the frozen reader. | Symbol identity, semantic range completeness, or unambiguous handling of every path containing colons. | Reread and probe after script change or when unusual paths, stale ranges, or invalid line inputs matter. |
| `/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/agents/openai.yaml` | `3cca38f60acf2bfa2e5f310301807d35e476ab4bcead18695bf101733ca2ab71` | Current agent-facing display and invocation metadata associated with the skill. | Builder correctness, map accuracy, or evidence about a target codebase. | Reinspect when agent discovery or presentation behavior changes. |

The installed skill and precedent files currently match both archive copies byte for byte. That observation is useful for deduplicating this read, but it should not be generalized into a promise that installed and archived versions always match.

**Generated run-artifact sources**

No target map was generated while evolving this reference because writes are restricted to the assigned reference, packet, and Delta journal. The following are therefore an artifact contract, not claims that files currently exist:

| generated_artifact | evidence role after an authorized run | verification question | invalidated by |
| --- | --- | --- | --- |
| `all_files.txt` | Raw inventory selected before code-extension filtering. Inside a Git worktree this is derived from tracked files. | Does this list reflect the repository population relevant to the question, including the intended policy for untracked, ignored, generated, vendored, and nested content? | Repository state, root, Git mode, inventory logic, or file policy change. |
| `code_files.txt` | Inventory remaining after the builder's supported-extension filter. | Are all task-relevant languages and file types represented, and which files disappeared between raw and code inventory? | Extension list or source population change. |
| `files.tsv` | Code-file rows with line counts for compact querying and reconciliation. | Do row counts and paths match `code_files.txt`, and are line counts from the same revision? | Inventory or source-content change. |
| `symbols.tsv` | Extracted symbol names and `file:start:end` pointers. | Which extraction branch produced the rows, do selected ranges resolve, and are duplicate or one-line spans understood? | Ctags capability, fallback logic, language syntax, file content, or options change. |
| `import_edges.tsv` | Lexically extracted import or include references before internal resolution. | Are representative references parsed correctly, and which language forms are not represented? | Parser patterns, source syntax, or inventory change. |
| `internal_file_edges.tsv` | Best-effort resolved file-to-file relations. | Do sampled endpoints agree with source and project semantics, including aliases and re-exports? | Resolver logic, naming conventions, source layout, or import rows change. |
| `external_ref_edges.tsv` | References the resolver did not map to an internal file. | Is each row truly external, or is it an alias, framework convention, generated target, unsupported form, or resolver miss? | Resolver, configuration, source layout, or dependency metadata change. |
| `tooling.tsv` | Capabilities detected by that run. | Did the run use JSON-capable Ctags or fallback extraction, was `ast-grep` merely available, and was Graphviz available? | Environment, `PATH`, installed versions, or capability probe change. |
| `dependency_graph.mmd` | Edge-capped Mermaid representation for text-native graph viewing. | What cap was applied, and do path labels or rendering rules alter how the selected edges appear? | Edge-cap option, relation rows, path labels, or graph-writing logic change. |
| `dependency_graph.dot` | Edge-capped graph presentation source. | What cap was applied, and how many tabular relations are omitted from the rendering? | Edge-cap option, relation rows, or graph-writing logic change. |
| `dependency_graph.svg` | Optional visual rendering created only when Graphviz `dot` is available. | Does the SVG correspond to the current DOT file, and is its absence an environment result rather than a map failure? | Graphviz availability, DOT content, or render option change. |
| `summary.md` | Run counts, likely fan-in and fan-out candidates, tool availability, and usage reminders. | Do summary counts reconcile with complete artifacts, and are rankings bounded by map coverage and relation quality? | Any upstream artifact, ranking logic, or run option change. |

The full TSV and text artifacts are evidence; the summary and graph are projections. When a visual or summary conflicts with complete rows, inspect the projection logic and configuration before changing an architectural conclusion.

**Target source and authoritative project evidence**

Generated pointers route into the target repository. Direct source spans establish what text and local structure exist at a revision, but broader semantics may require complete-file reads, configuration, generated output, build-system metadata, compiler or language-server queries, tests, and runtime traces. The source map therefore ends at the project's own evidence rather than at `summary.md`.

| claim class | first local source | confirming source | reason |
| --- | --- | --- | --- |
| Historical workflow intent | Dated archive skill. | Same-date precedent note and surrounding archive context. | Current installation cannot rewrite a past snapshot. |
| Current builder mechanics | Hashed builder script. | Syntax check and focused read of the relevant branch. | Prose can lag executable behavior. |
| Actual symbol extraction outcome | Run-specific `symbols.tsv` kind values and `ctags.jsonl` presence, interpreted with `tooling.tsv` capability flags. | Captured capability probe plus sampled pointer rows. | `ctags=yes` means the probe passed, not that the actual Ctags invocation produced usable symbols; empty output triggers fallback. |
| Repository inventory coverage | `all_files.txt`, `code_files.txt`, and `files.tsv`. | Independent repository-native inventory and explicit exclusion policy. | A successful build does not prove relevant files entered the map. |
| Candidate symbol location | `symbols.tsv`. | Pointer reader plus direct source. | A row is an index entry, not semantic confirmation. |
| Dependency relation | Import and internal-edge rows. | Both endpoint sources and a language-aware or repository-native check when consequential. | Lexical resolution is approximate. |
| No dependency exists | Empty or unresolved artifact result only as a prompt. | Appropriate semantic, build, configuration, and runtime evidence. | Non-observation cannot establish absence. |
| Safe code change | Candidate neighborhood from artifacts. | Tests, build or compile checks, contract review, and direct source reasoning. | A rough graph does not encode every behavioral consumer. |

**Default retrieval order**

1. Read one representative historical skill and precedent file; use hashes to detect semantic duplicates while retaining every archive path in provenance.
2. Read and hash the current builder and pointer reader; inspect the agent metadata only when discovery or invocation behavior matters.
3. Probe the current environment and record actual capabilities before predicting extraction or rendering behavior.
4. Generate artifacts only in an authorized disposable path and retain command, repository revision, working tree state, options, and timestamps.
5. Reconcile `all_files.txt`, `code_files.txt`, and `files.tsv` before interpreting symbols or edges.
6. Query compact TSV rows, then resolve selected source pointers rather than loading every file.
7. Verify consequential claims through direct source and authoritative project mechanisms.
8. Escalate when unsupported syntax, dynamic wiring, completeness requirements, or mismatch samples exceed the decision's tolerance.

**Source-to-claim invalidation**

| changed input | claims that must be reopened | claims that may remain stable |
| --- | --- | --- |
| Skill prose only | Workflow recommendations, artifact descriptions, and agent instructions. | Frozen script mechanics and prior run observations if their inputs are unchanged. |
| Builder script or options | Inventory, extraction, relation, summary, graph, and all conclusions derived from them. | Historical intent and independently verified target semantics. |
| Pointer reader | Span-resolution and context-read claims; selected source observations may need replay. | Artifact row contents that do not depend on pointer reading. |
| Environment capability | Selected extraction and rendering branches plus cross-run comparisons. | Repository bytes and historical source identities. |
| Repository revision or working tree | Inventory, pointers, relations, rankings, and behavior conclusions tied to the previous state. | General method guidance and script behavior under the same version. |
| One sampled edge mismatch | The specific conclusion and any ranking materially sensitive to that mismatch class. | Unrelated inventory facts, pending investigation of whether the defect is systematic. |

Good evidence pairing says: "The frozen builder uses tracked inventory in a Git worktree; this run's `all_files.txt` contains the expected module; `symbols.tsv` points to the candidate definition; direct source and the project build confirm the intended relationship." Bad pairing says: "The archived skill recommends mapping, therefore this target file was included and has no callers." A proposal-only architecture note can rely on guidance prose, but it must say that no repository observation has occurred.

The map should retain three timestamps or identities separately: the guidance or script version, the environment capability capture, and the target repository state. They decay at different rates. This separation allows targeted rereads: a resolver change reopens edge conclusions without forcing reinterpretation of stable archive intent, while a repository change invalidates pointers and relations without changing what the frozen script is capable of doing.

## External Research Source Map

No remote page was opened for this evolution. Every URL below is preserved from the seed or the hashed local precedent note and carries the status `locally_retained_pointer_unrefreshed`. The externally sourced fact established here is only that the local corpus contains the pointer and accompanying description. Present page content, availability, versions, compatibility, and performance claims remain unknown until an authorized refresh.

**Preserved seed pointers**

| external_source_url_value | locally_retained_name_text | intended_research_question | evidence_boundary_label_value | local_closure_check |
| --- | --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | How should repository-local agent instructions scope tool use, evidence boundaries, and verification behavior? | `locally_retained_pointer_unrefreshed` | Compare any refreshed guidance with the repository's actual instruction files and the active agent harness. |
| https://docs.github.com/actions | GitHub Actions documentation | How can repeatable map verification or artifact checks be automated in a repository workflow? | `locally_retained_pointer_unrefreshed` | Inspect the repository's own workflow syntax, permissions, runner environment, and executed logs before claiming automation coverage. |
| https://agents.md/ | AGENTS.md open format | What general conventions exist for hierarchical agent instruction context? | `locally_retained_pointer_unrefreshed` | Verify which convention the current agent implementation actually recognizes and how nested instructions are resolved. |

These three pointers concern agent context and automation around the mapping workflow. They do not validate symbol extraction, relation resolution, map accuracy, or the behavior of the installed builder.

**Tool and protocol pointers retained in the local precedent note**

| external_source_url_value | locally_retained_name_text | locally_recorded_design_role | question_that_should_trigger_refresh | required_local_follow_through |
| --- | --- | --- | --- | --- |
| https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/ | LSP 3.17 Specification | The local note records workspace symbol and call hierarchy APIs as a precedent for pointer-first navigation. | Can a language-aware server provide semantic symbols or incoming and outgoing calls for this repository? | Identify the actual server and version, probe the capability, measure index coverage, and compare selected results with source. |
| https://sourcegraph.com/docs/code_search/explanations/precise_code_navigation | Sourcegraph precise code navigation | The local note records precise indexes with text-search fallback as a hybrid-navigation precedent. | Should the rough map yield to a prebuilt precise index or use lexical search when indexed data is missing? | Confirm the deployed product, index format, repository revision, language support, and fallback behavior. |
| https://tree-sitter.github.io/tree-sitter/ | Tree-sitter documentation | The local note records concrete syntax trees and incremental parsing as structural primitives. | Would parser-aware extraction reduce regex noise for a supported language or construct? | Pin grammar and library versions, parse representative files, inspect error nodes, and compare extracted relations with the rough builder. |
| https://ast-grep.github.io/ | ast-grep documentation | The local note records AST-based pattern search on Tree-sitter as a structural-search option. | Can a focused structural rule answer the pending query more precisely than lexical scanning? | Match installed command and rule syntax, run on positive and negative fixtures, and inspect every consequential match. |
| https://docs.ctags.io/en/latest/man/ctags.1.html | Universal Ctags options | The local note records JSON output plus line and end-line fields as a cheap cross-language span source. | Which flags and fields are supported by the installed Ctags, and why did a capability probe select or reject it? | Capture binary identity, run the exact JSON probe, inspect output fields, and resolve sampled `file:start:end` ranges. |
| https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md | ripgrep guide | The local note records recursive line-oriented search as the lexical baseline. | Which search, glob, encoding, ignore, or line-number behavior matters for a repository inventory or fallback query? | Match installed version, run a repository-sized sample, and reconcile ignore and hidden-file behavior with the intended coverage policy. |
| https://graphviz.org/doc/info/lang.html | Graphviz DOT language | The local note records DOT as a simple dependency-graph interchange and rendering format. | Is a DOT syntax or rendering issue blocking an otherwise valid tabular map? | Validate the generated DOT locally, capture `dot` availability and version, and keep graph edge caps separate from full TSV evidence. |
| https://github.com/sverweij/dependency-cruiser | dependency-cruiser | The local note records another practical dependency-graph workflow. | Would a JavaScript or TypeScript-oriented dependency analyzer provide stronger project-specific resolution? | Verify language fit, configuration, aliases, package boundaries, version, and selected edges against direct source. |

The locally retained descriptions above are historical summaries, not fresh quotations from the linked pages. A protocol specification can describe an API without proving that a particular language server implements it. A tool manual can describe an option without proving that the installed binary supports it. A graph product can demonstrate a useful pattern without calibrating this builder's precision or recall.

**Research routing by local mismatch**

| observed local problem | first external family to consider | why | return condition |
| --- | --- | --- | --- |
| Symbol ranges collapse to one line or miss language constructs. | Version-matched Universal Ctags documentation, then Tree-sitter or ast-grep for structural extraction. | The mismatch concerns span capability or parser awareness. | Re-run a representative extraction and verify pointers directly in source. |
| Text search finds too much syntactic noise. | ast-grep and Tree-sitter primary documentation. | A structural pattern may express the construct more precisely than regex. | Test positive, negative, nested, malformed, and language-version cases. |
| Callers or callees cannot be established lexically. | LSP or another language-aware index relevant to the target language. | Semantic name resolution is outside the rough resolver's observation model. | Confirm server capability, indexing completeness, and selected call edges. |
| A precise index is partial or unavailable. | Precise-navigation and lexical-fallback design material. | The decision concerns graceful fallback and explicit confidence states. | Demonstrate which queries use precise data and which fall back, then label outputs accordingly. |
| Inventory or fallback search differs across machines. | Version-matched ripgrep documentation and local `--help`. | Ignore, hidden-file, glob, encoding, or version behavior may explain the difference. | Reproduce with frozen flags and reconcile counts. |
| The DOT file exists but rendering fails or appears incomplete. | Graphviz DOT documentation. | Syntax and rendering are separate from relation extraction, and presentation can be capped. | Validate DOT, record renderer capability, and compare against complete TSV rows. |
| JavaScript or TypeScript resolution needs package and alias semantics. | A project-appropriate dependency analyzer such as the retained dependency-cruiser pointer. | Specialized configuration may resolve relations the generic lexical mapper misses. | Pin configuration and compare sampled edges plus omissions with source and build tooling. |
| Agent instructions or automated checks need refinement. | Seed agent-instruction and GitHub Actions pointers. | This concerns workflow control rather than map semantics. | Confirm actual harness precedence, workflow permissions, runner tools, and test output. |

Routing begins with a local mismatch, not a broad survey. If a sampled edge is wrong, first classify whether the cause is inventory, extraction, resolution, configuration, or dynamic behavior. Only then choose the external source family. This prevents an authoritative but irrelevant document from adding confidence to the wrong explanation.

**Promotion protocol for an external claim**

An unrefreshed pointer can be promoted to a current external fact only after the following evidence is retained:

1. Open the primary source under explicit browsing authorization and record retrieval date, exact URL, page or release version, and relevant section.
2. Paraphrase the narrow claim and retain its preconditions, optionality, and stated limitations; do not turn a capability into a default or guarantee.
3. Match the document to the installed binary, server, protocol, grammar, action runner, or product version.
4. Reproduce the capability with a minimal local positive example and, where false positives matter, a negative or boundary example.
5. Apply it to a representative target-repository sample and compare with direct source or another independent mechanism.
6. Record disagreements and keep the external statement separate from empirical local results.

This protocol can be shortened for a conceptual, low-consequence design note, but version and applicability checks are mandatory before compatibility, security, performance, or completeness claims.

**Alternative evidence surfaces**

| evidence surface | advantage | limitation | best use |
| --- | --- | --- | --- |
| Installed `--help` or capability probe | Matches the binary available now. | Often omits conceptual limits and can vary by build flags. | Establish whether a specific option or output mode is locally available. |
| Vendored or versioned documentation | Reproducible with the repository revision. | Can age and may omit upstream corrections. | Audit and offline workflows that value stable context. |
| Primary live documentation | Potentially current and authoritative for stated behavior. | Mutable, sometimes unversioned, and not proof of local installation or project fit. | Refresh a material tool or protocol claim under browsing authorization. |
| Tool source or release notes | Precise about implementation changes. | Expensive to interpret and easy to mismatch with packaged builds. | Diagnose a version-specific capability or regression. |
| Repository-native guides and configuration | Directly applicable to project conventions. | May be incomplete or stale. | Understand aliases, generated code, build graph, and expected analysis commands. |
| Empirical fixture and target sample | Tests actual behavior in the environment. | Covers only exercised cases and requires careful sample design. | Close the loop after documentation research. |

**Good and bad external-evidence language**

Good: "The hashed local precedent note points to the LSP 3.17 specification as a future source for workspace-symbol and call-hierarchy research. This evolution did not open the page or establish that the target language server implements those capabilities."

Bad: "LSP guarantees complete incoming and outgoing calls for this repository." The specification cannot guarantee server implementation, index coverage, generated-code handling, configuration, or target correctness.

Conditionally acceptable: "Tree-sitter is a candidate structural primitive for replacing a noisy regex in this design." This is a proposal grounded in the locally retained note, not a claim about current API details or measured improvement. Before implementation, the grammar, version, parse behavior, and target fixtures still need checking.

**Known and unknown ledger**

- Known: the local precedent file with hash `6225de10e11642bd9df819b33bfc01835f6af5659c0680ded4dad784929f6637` contains the eight tool and protocol URLs above and the summarized roles reproduced here.
- Known: the seed reference contains the three agent and automation URLs preserved above.
- Unknown: whether each remote URL currently resolves, redirects, retains the summarized content, or documents the same version implied by its local description.
- Unknown: which external tool would improve a particular target repository until the mismatch class, language, configuration, cost, and authoritative project options are known.
- Unknown: comparative accuracy or performance; no refreshed documentation, benchmark, or target run was collected here.

External research becomes decision evidence only when it changes and then survives a local verification step. Until then, this section is a deliberately honest queue: it preserves where to look, why to look there, and what must be tested afterward without converting unvisited pages into current authority.

## Anti Pattern Registry Table

An anti-pattern entry is a diagnostic hypothesis, not an automatic verdict. Classify the pipeline stage, verify the mechanism, invalidate downstream conclusions that depend on it, and choose a response proportional to the pending action. Silent completeness errors receive higher severity than loud execution failures because plausible output invites continued interpretation.

| anti_pattern_failure_name | stage | failure_cause_risk_reason | detection_signal_review_method | safer_default_replacement_pattern | response |
| --- | --- | --- | --- | --- | --- |
| context_free_summary_output | evidence setup | The agent skips the local corpus and produces generic dependency-map advice detached from the installed implementation and repository state. | Trace every operational statement to a local source, current script, run artifact, target source, or explicit inference. | `source_map_first_synthesis`: establish temporal authority and evidence roles before recommendations. | Stop durable handoff until provenance exists; warn for private brainstorming. |
| unsourced_recommendation_claims | evidence setup | Guidance sounds authoritative without separating local observation, retained external pointer, inference, and uncertainty. | Sample recommendations and require an evidence class plus the narrow source that supports each one. | `evidence_boundary_split_pattern`: type claims as candidate, observed, corroborated, verified, or unresolved. | Stop consequential decisions that depend on an untyped claim. |
| unverified_agent_instruction | workflow control | A recommendation cannot be checked by a command, artifact invariant, source review, or escalation gate. | Ask what result would falsify the instruction and whether another operator can reproduce that check. | `verification_gate_coupling`: attach a concrete gate and retained evidence to every material instruction. | Warn for low-impact hints; stop changes whose acceptance condition is undefined. |
| successful_exit_equals_complete_map | preflight and inventory | A zero exit status is interpreted as representative repository coverage even though it only shows that implemented branches completed. | Reconcile `all_files.txt`, `code_files.txt`, and `files.tsv` with an independent inventory and the task's file policy. | `coverage_before_interpretation`: prove the relevant input population before reading symbols or edges. | Stop absence, deletion, and completeness claims. |
| tracked_inventory_blind_spot | inventory | Inside a Git worktree, untracked and ignored files do not enter the builder's `git ls-files` inventory even if they affect a local task or generated behavior. | Compare Git tracked output with working-tree status, ignore policy, build inputs, and any authorized independent filesystem inventory. | `inventory_policy_explicit`: choose and record whether transient, ignored, generated, vendored, or nested files matter. | Rebuild or use another inventory when omitted classes affect the decision. |
| supported_extension_equals_all_code | inventory | The finite extension filter is assumed to cover every source or configuration language; Kotlin and other unlisted types cannot contribute rows. | Enumerate relevant extensions independently and compare them with `.rs`, `.py`, `.js`, `.jsx`, `.ts`, `.tsx`, `.go`, `.java`, `.c`, `.cc`, `.cpp`, `.h`, and `.hpp`. | `language_coverage_reconciled`: add a suitable extractor or route unsupported languages to repository-native tooling. | Stop cross-language completeness claims when a relevant class is absent. |
| generated_and_configuration_erasure | inventory | Generated registries, schemas, build manifests, route configuration, or non-code files are excluded even though they define dependencies. | Trace build and startup inputs; inspect project manifests and generated-output policy outside the code-extension list. | `dependency_surface_declared`: include or separately analyze non-source relationship authorities. | Escalate whenever configuration or generation drives wiring. |
| tool_available_equals_tool_used | extraction | A capability listed in `tooling.tsv`, such as `ast-grep`, is assumed to participate automatically in extraction when the builder only records its availability. | Read the executed branch and compare artifact metadata with script calls rather than inferring use from presence. | `selected_branch_recorded`: distinguish detected, invoked, succeeded, and contributed-to-result states. | Correct the provenance claim and rerun only if the desired branch is implemented. |
| ctags_name_equals_json_capability | extraction | Any command named Ctags is assumed to support the JSON fields required for rich ranges. | Run the exact JSON capability probe and inspect output fields; record binary identity and version where available. | `capability_probe_before_branch`: select Ctags only when the required format and fields work. | Fall back explicitly or install a suitable analyzer; never conceal the branch. |
| fallback_span_equals_definition_range | extraction | Regex fallback rows with `end_line` equal to `start_line` are treated as complete symbol bodies. | Inspect `tooling.tsv`, calculate one-line-span prevalence, and round-trip representative pointers into source. | `pointer_is_entry_point`: read surrounding context or the full module before semantic interpretation. | Warn for navigation; stop range-sensitive transformations or metrics. |
| symbol_name_equals_unique_identity | extraction and query | Repeated names across files, scopes, overloads, or generated forms are collapsed into one conceptual entity. | Group `symbols.tsv` by name and inspect file, language, scope cues, and direct definitions for duplicates. | `qualified_candidate_selection`: retain path and range, then disambiguate with language-aware identity when needed. | Sample for navigation; escalate for caller or ownership claims. |
| lexical_reference_equals_semantic_dependency | resolution | A textual import or include is treated as a resolved runtime or build dependency without alias, re-export, condition, or type-only semantics. | Check both endpoints, project configuration, conditional forms, and an authoritative language or build mechanism. | `lexical_edge_as_candidate`: label rough rows as hypotheses until corroborated. | Stop behavioral and reachability claims based solely on the edge. |
| unresolved_equals_third_party | resolution | Every `external_ref_edges.tsv` row is classified as external even though aliases, framework conventions, generated targets, unsupported forms, or resolver defects can produce the same state. | Cluster unresolved rows by syntax and prefix; test known internal aliases and inspect relevant project configuration. | `unresolved_is_unknown`: classify only after targeted resolution or authoritative dependency metadata. | Warn in summaries; stop external-dependency inventories that use this shortcut. |
| missing_edge_equals_no_dependency | interpretation | Non-observation is promoted to absence despite inventory, parser, resolver, dynamic, or configuration blind spots. | Search independently, inspect language-aware or build graphs, test runtime registration where relevant, and review known exclusions. | `absence_requires_authority`: use an empty rough result only to choose stronger checks. | Critical stop for deletion, security, migration, and complete-consumer claims. |
| rendered_graph_equals_full_artifact | presentation | An edge-capped DOT or SVG view is read as the complete relationship set. | Compare `MAX_GRAPH_EDGES`, DOT edge count, full TSV row counts, and summary statements. | `tabular_truth_before_projection`: rank and audit complete rows before using the visual as navigation. | Recalculate or relabel every visual-derived hub conclusion. |
| visual_density_equals_architectural_centrality | interpretation | A visually dense node is called a critical hub without controlling for duplicate rows, extraction bias, omitted languages, edge direction, or graph caps. | Deduplicate, inspect fan-in and fan-out separately, sample edges, and compare with project ownership or runtime evidence. | `candidate_rank_with_confidence`: state metric, population, omissions, and corroboration. | Warn for review prioritization; stop redesign decisions based only on appearance. |
| stale_pointer_equals_current_source | retrieval | A saved `file:start:end` range is reused after source changes or across a different revision. | Confirm repository identity and revision, validate bounds, and inspect whether the expected construct still occupies the range. | `pointer_revision_binding`: regenerate or search by qualified identity, then retain the new range. | Correct before quoting, patching, or handing off evidence. |
| colon_path_parsed_as_range | retrieval | A path containing colons is ambiguously split when passed in combined pointer form. | Test the exact path through the pointer reader and compare with separate file/start/end arguments. | `separate_arguments_for_ambiguous_paths`: avoid the compact form when path syntax conflicts with range syntax. | Use explicit arguments or another reader; do not silently normalize the wrong file. |
| whole_repository_context_dump | context management | All files or large graph output are loaded before a focused question is formed, consuming attention and blending relevant with irrelevant code. | Measure selected bytes or tokens, count files not cited by the final conclusion, and inspect repeated broad reads. | `query_rank_pointer_read`: filter compact artifacts, rank candidates, and expand context only after evidence demands it. | Warn and narrow; retain whole-file reads when semantics genuinely span the module. |
| output_directory_without_provenance | run management | Artifacts are overwritten or handed off without command, revision, options, tool hashes, capability branch, and working-tree state. | Attempt to reproduce a row from the artifact directory alone and identify missing inputs. | `artifact_run_manifest`: bind results to producer and repository state in an authorized disposable location. | Stop cross-run comparison and durable architectural citation until provenance is restored. |
| heuristic_patch_instead_of_precision_escalation | method selection | More regex exceptions and warnings are added even though the pending claim fundamentally requires semantic or runtime evidence. | Ask whether the observation model can represent the relation class even with perfect implementation. | `consequence_driven_escalation`: switch to language-aware, compiler, build, configuration, or runtime analysis. | Critical stop when false negatives authorize material action. |

**Triage order**

1. Confirm the command and output directory belong to the intended repository and run.
2. Validate inventory population before diagnosing empty symbol or relation results.
3. Record capability flags, determine the actual symbol producer from `symbols.tsv` kinds and `ctags.jsonl`, and test pointer quality.
4. Reconcile raw imports, internally resolved edges, and unresolved references.
5. Compare complete tabular rows with summary and visual projections.
6. Verify selected source relations and classify mismatch mechanisms.
7. Decide whether the rough observation model can answer the pending claim at all.

This order matters. A missing Kotlin file cannot be repaired by tuning a graph rank, and a false internal edge cannot be repaired by reading a prettier SVG. Diagnose the earliest invalid premise and invalidate all dependent conclusions before continuing.

**Compound failure chains**

| chain | plausible but wrong outcome | selective rollback |
| --- | --- | --- |
| Tracked-only omission -> unresolved reference -> low apparent fan-in -> deletion candidate | A generated or ignored registry is absent, so a live component appears isolated. | Reopen inventory, all relations touching the omitted class, rankings derived from them, and the deletion conclusion. Keep unrelated pointer-reader tests. |
| Unsupported extension -> no symbols -> no inbound edges -> false language boundary | An unlisted source language disappears and the remaining graph appears cleanly layered. | Rebuild with language coverage or a specialized analyzer; discard cross-language boundary claims. |
| Ctags capability rejection -> one-line fallback -> context-free pointer read -> wrong symbol interpretation | A range points at a declaration line while critical annotations or body logic lie outside it. | Retain the candidate location, expand source context, and reopen any range-derived metric or transformation. |
| Alias resolver miss -> unresolved classified external -> dependency inventory inflation | Internal package aliases are reported as third-party dependencies. | Reclassify the alias family, rerun or post-process resolution, and revise external-dependency counts. |
| Edge cap -> sparse SVG -> visual centrality claim -> misplaced refactor priority | Complete TSV rows contain relations not rendered in the capped graph. | Recalculate from full rows, disclose cap, sample edges, and revise the priority list. |
| Dynamic registration -> missing edge -> no-dependency assertion -> security regression | Runtime configuration creates a path that static lexical scans never represent. | Abandon absence inference, inspect configuration and runtime behavior, then use security-specific verification. |

**Good, bad, and borderline recovery**

Good: `internal_file_edges.tsv` is unexpectedly empty. The operator first finds that the relevant language extension never entered `code_files.txt`, documents the coverage defect, selects an appropriate analyzer, and invalidates every prior relation and hub conclusion. The recovery changes the premise.

Bad: The SVG has no arrow into a file, so the operator removes it. This bypasses inventory, extraction, resolution, cap, dynamic-wiring, and authoritative absence checks.

Borderline: A fallback symbol pointer is one line long, but the operator uses it only to navigate to a candidate and immediately reads surrounding source. The range is weak, yet the action is reversible and no definition-body claim is made.

**Verification fixtures and reviews**

| failure class | controlled check | target-repository check | generalization limit |
| --- | --- | --- | --- |
| Inventory omission | Create representative tracked, untracked, ignored, unsupported, generated, and nested paths in a disposable fixture; compare raw and filtered lists. | Reconcile actual build inputs and repository-native inventory with all three inventory artifacts. | A fixture cannot enumerate every project policy. |
| Span quality | Include multiline declarations, annotations, overloads, nested constructs, and duplicate names; exercise both Ctags and fallback branches. | Resolve a stratified symbol sample and classify exact, partial, stale, duplicate, and invalid ranges. | Sampled precision does not prove complete recall. |
| Resolver behavior | Include relative paths, aliases, re-exports, index files, extensions, includes, conditionals, and an intentionally external reference. | Sample high-impact internal, unresolved, and missing relations against source and project configuration. | Dynamic behavior remains outside lexical fixtures. |
| Presentation cap | Generate more relations than the configured cap and compare TSV, DOT, SVG, and summary counts. | Record actual cap and verify that rankings use complete rows. | Full rows can still be incomplete relative to program behavior. |
| Pointer parsing | Exercise combined and separate forms, reversed bounds, out-of-range lines, whitespace, and colon-bearing paths. | Round-trip every pointer cited in a consequential handoff. | A valid read does not establish semantic range. |
| Precision escalation | Include a runtime registry or reflection path invisible to static imports. | Compare rough artifacts with language-aware, build, configuration, or runtime evidence. | One counterexample identifies a blind spot but does not quantify prevalence. |

Current script reading establishes the mechanisms behind tracked Git inventory, the finite extension set, capability-dependent span extraction, lexical resolution, optional Graphviz rendering, and edge-capped presentation. It does not establish how often each failure occurs across repositories. Severity here is therefore reasoned from invisibility, downstream blast radius, and reversibility rather than from an empirical incident rate.

When a new anti-pattern is discovered, add it only after recording the smallest reproducing input, the faulty artifact, the actual mechanism, the safer replacement, and the claims invalidated by the defect. That discipline turns the registry into reusable diagnostic memory instead of a growing list of vague cautions.

## Verification Gate Command Set

Commands are evidence-producing steps with narrow claim contracts. A zero exit status proves only the stated gate. Script syntax does not prove map coverage, nonempty artifacts do not prove relation accuracy, and sampled relations do not prove complete recall.

| gate | supported claim | does not prove | response on failure |
| --- | --- | --- | --- |
| Script integrity | The frozen shell files are readable and parse under the selected Bash. | That required tools exist or any target repository can be mapped. | Stop and inspect the exact script or shell mismatch. |
| Environment capability | Required commands exist and optional branches are observable on this machine. | That an optional tool is invoked, correctly configured, or accurate for the target. | Install, configure, or accept and record the intended fallback. |
| Authorized build | The builder completed and produced fresh output in the selected location. | That inventory is representative or relations are semantic. | Preserve diagnostics; do not interpret partial or stale artifacts as current output. |
| Artifact invariant | Required files, headers, row shapes, and cross-artifact counts satisfy the documented contract. | That extracted rows match code behavior or include every relationship. | Attribute the defect to production or schema before querying conclusions. |
| Pointer round trip | A selected path and line range resolve in the current source tree. | That the range covers the complete semantic construct. | Regenerate, disambiguate, or expand the read. |
| Relation sample | Selected rows agree or disagree with direct source and project configuration. | Complete precision or recall beyond the sample. | Classify mismatch mechanism and invalidate affected conclusions. |
| Project-native verification | The repository's own compiler, build, tests, analyzer, or runtime check supports the claim under its configuration. | Unexercised configurations or behaviors outside that mechanism. | Repair or narrow the claim; do not override authoritative failure with the rough map. |
| Reference-file verifier | The evolved reference satisfies focused structural and content rules. | The technical truth of every dependency-mapping recommendation. | Correct the assigned reference or packet without changing shared inputs. |

**Safety preconditions**

- Set `REPO_ROOT` to the intended target repository and `OUT_DIR` to a new, explicitly authorized disposable directory. The builder creates and writes the output directory.
- Record the target revision and working-tree state before the run. A dirty tree may be intentional, but it changes the evidence population.
- Use a fresh output directory. Do not mix artifacts from different scripts, options, environments, or revisions.
- Quote every path. Prefer separate file, start, and end arguments to the pointer reader when a path can contain colons.
- Capture `MAX_GRAPH_EDGES`; it changes Mermaid, DOT, and SVG presentation without making the complete TSV relation set smaller.
- Include a consequential positive relation and a suspicious absence or unresolved reference in sampling. Easy positive rows alone cannot expose false-negative classes.

**Gate 1: frozen-script integrity and capability preflight**

```bash
BUILDER=/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/scripts/build_rough_codebase_map.sh
READER=/Users/amuldotexe/.codex/skills/dependency-map-cli-tools-01/scripts/read_code_span_pointer.sh

test -r "$BUILDER"
test -r "$READER"
bash -n "$BUILDER"
bash -n "$READER"
command -v bash
command -v python3
command -v rg

if command -v ctags >/dev/null 2>&1; then
  ctags --output-format=json -f - /dev/null >/dev/null 2>&1 \
    && printf '%s\n' 'ctags_json=yes' \
    || printf '%s\n' 'ctags_json=no'
else
  printf '%s\n' 'ctags_json=absent'
fi

command -v ast-grep || command -v sg || true
command -v dot || true
```

Expected interpretation: `rg` and Python are required by the implementation even though the shell's explicit early check names `rg`; Ctags, ast-grep, and Graphviz are optional capabilities. Ast-grep detection does not mean this builder invokes it. A Ctags executable that fails the exact JSON probe selects fallback behavior. Absence of `dot` prevents SVG generation but does not prevent Mermaid or DOT text output.

At the recorded evolution checkpoint, both scripts passed `bash -n`; `rg` and `ast-grep` were detected; the available Ctags failed the JSON capability probe; and `dot` was absent. Those observations are environment-specific and must be refreshed before a future run.

**Gate 2: target identity and authorized production**

```bash
: "${REPO_ROOT:?set REPO_ROOT to the target repository}"
: "${OUT_DIR:?set OUT_DIR to a new authorized output directory}"
test -d "$REPO_ROOT"
test ! -e "$OUT_DIR"

git -C "$REPO_ROOT" rev-parse --show-toplevel 2>/dev/null || true
git -C "$REPO_ROOT" rev-parse HEAD 2>/dev/null || true
git -C "$REPO_ROOT" status --short 2>/dev/null || true

MAX_GRAPH_EDGES="${MAX_GRAPH_EDGES:-160}" \
  bash "$BUILDER" "$REPO_ROOT" "$OUT_DIR"
```

This gate writes artifacts and was not executed while evolving this file because the assignment permits writes only to the assigned reference, packet, and Delta journal. Run it only when the target and output path are authorized. Retain the command, target identity, revision, working-tree state, edge cap, script hash, timestamps, and exit status.

**Gate 3: required artifact and schema checks**

```bash
for artifact in \
  all_files.txt \
  code_files.txt \
  files.tsv \
  symbols.tsv \
  import_edges.tsv \
  internal_file_edges.tsv \
  external_ref_edges.tsv \
  tooling.tsv \
  dependency_graph.mmd \
  dependency_graph.dot \
  summary.md
do
  test -s "$OUT_DIR/$artifact"
done

python3 - "$OUT_DIR" <<'PY'
import csv
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
expected = {
    "files.tsv": ["path", "line_count"],
    "symbols.tsv": ["symbol", "path", "start_line", "end_line", "kind", "scope"],
    "import_edges.tsv": ["source_file", "source_line", "target_ref", "edge_kind"],
    "internal_file_edges.tsv": ["source_file", "source_line", "target_file", "edge_kind"],
    "external_ref_edges.tsv": ["source_file", "source_line", "target_ref", "edge_kind"],
    "tooling.tsv": ["tool", "available"],
}

for name, header in expected.items():
    with (root / name).open(newline="", encoding="utf-8") as handle:
        rows = csv.reader(handle, delimiter="\t")
        actual = next(rows, None)
        if actual != header:
            raise SystemExit(f"{name}: expected header {header!r}, got {actual!r}")
        for line_number, row in enumerate(rows, 2):
            if len(row) != len(header):
                raise SystemExit(
                    f"{name}:{line_number}: expected {len(header)} fields, got {len(row)}"
                )
print("artifact_schema=pass")
PY

if awk -F '\t' '$1 == "dot" && $2 == "yes" { found=1 } END { exit !found }' \
  "$OUT_DIR/tooling.tsv"
then
  test -s "$OUT_DIR/dependency_graph.svg"
fi
```

These checks establish expected names, nonempty required files, table headers, row widths, and conditional SVG presence. They do not establish that rows are correct. A relation table containing only its header is nonempty, so row counts and task expectations still need inspection.

**Gate 4: inventory reconciliation**

```bash
printf 'all_files=%s\n' "$(wc -l < "$OUT_DIR/all_files.txt")"
printf 'code_files=%s\n' "$(wc -l < "$OUT_DIR/code_files.txt")"
printf 'files_tsv_rows=%s\n' "$(( $(wc -l < "$OUT_DIR/files.tsv") - 1 ))"

diff -u \
  <(LC_ALL=C sort "$OUT_DIR/code_files.txt") \
  <(tail -n +2 "$OUT_DIR/files.tsv" | cut -f 1 | LC_ALL=C sort)

git -C "$REPO_ROOT" ls-files > "$OUT_DIR/independent_git_files.txt"
diff -u \
  <(LC_ALL=C sort "$OUT_DIR/independent_git_files.txt") \
  <(LC_ALL=C sort "$OUT_DIR/all_files.txt")
```

The last comparison confirms the implemented Git inventory branch, not the suitability of tracked-only coverage. Review `git status --short`, ignore rules, relevant generated files, configuration inputs, vendored policy, nested repositories, and unsupported extensions separately. For a non-Git root, derive an independent inventory with a method appropriate to the same file policy instead of using the Git command.

**Gate 5: pointer round trip**

```bash
python3 - "$OUT_DIR/symbols.tsv" > "$OUT_DIR/selected_symbol.txt" <<'PY'
import csv
import sys

with open(sys.argv[1], newline="", encoding="utf-8") as handle:
    rows = csv.DictReader(handle, delimiter="\t")
    row = next(rows, None)
    if row is None:
        raise SystemExit("symbols.tsv has no data rows")
    print(row["path"])
    print(row["start_line"])
    print(row["end_line"])
PY

mapfile -t selected < "$OUT_DIR/selected_symbol.txt"
bash "$READER" \
  "$REPO_ROOT/${selected[0]}" \
  "${selected[1]}" \
  "${selected[2]}" \
  3
```

The example writes one small selection file inside the already authorized output directory. On shells without `mapfile`, read the three lines using an equivalent structured wrapper. Do not select only the first row for a real accuracy sample: stratify by language, extraction branch, multiline shape, duplicate name, and decision importance. A valid range is an entry point; source review determines whether it covers the construct.

**Gate 6: relation and presentation reconciliation**

```bash
printf 'imports=%s\n' "$(( $(wc -l < "$OUT_DIR/import_edges.tsv") - 1 ))"
printf 'internal_edges=%s\n' "$(( $(wc -l < "$OUT_DIR/internal_file_edges.tsv") - 1 ))"
printf 'unresolved_refs=%s\n' "$(( $(wc -l < "$OUT_DIR/external_ref_edges.tsv") - 1 ))"
printf 'mermaid_edges=%s\n' "$(rg -c -- ' --> ' "$OUT_DIR/dependency_graph.mmd" || true)"
printf 'dot_edges=%s\n' "$(rg -c -- ' -> ' "$OUT_DIR/dependency_graph.dot" || true)"

head -n 21 "$OUT_DIR/internal_file_edges.tsv"
head -n 21 "$OUT_DIR/external_ref_edges.tsv"
```

Then choose samples deliberately. For an internal row, inspect the source line, target file, aliases, re-exports, and project configuration. For an unresolved row, test whether it is truly external or a resolver miss. For a suspicious absence, search independently and use a language-aware, build, configuration, or runtime tool. Compare graph counts with full rows and the recorded cap before interpreting visual density.

**Gate 7: project-native verification**

No universal command can replace repository-specific evidence. After mapping, discover and run the project's documented formatter, type checker, compiler, build, unit and integration tests, architecture checks, or runtime probe relevant to the proposed action. Record exact commands and configuration. If the rough map and an authoritative project mechanism disagree, investigate the mismatch; do not average the results or prefer the prettier output.

| claim | minimum follow-through |
| --- | --- |
| Candidate location | Resolve the pointer and read source. |
| Static import relation | Read both endpoints and relevant configuration. |
| Caller or consumer set | Use a language-aware or repository-native mechanism and inspect exceptions. |
| No dependency exists | Use appropriate semantic, build, configuration, and runtime evidence; rough emptiness is insufficient. |
| Refactor is safe | Run the affected build and tests, review contracts, and inspect consumers not representable by lexical edges. |
| Security path is absent | Use security-specific static, configuration, test, and runtime verification. |

**Gate 8: focused evolved-reference verification**

For this assigned reference, the focused verifier interface is:

```bash
python3 tests/verify_idiomatic_reference_file.py \
  --path idiomatic-ref-202607/dependency_map_cli_patterns-20260710.md
```

The packet additionally requires exact question text, `26` packet sections, `260` question headings, `1,560` mandatory fields, and both raw and prefix-stripped normalized uniqueness. Those packet gates require the repository's evolution tests or an equivalent focused parser; the reference-only command cannot establish them alone.

**Preserved seed final-corpus command**

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

This historical/global command is retained exactly from the seed. Its result can depend on shared corpus state outside one lane's authorized files, so distinguish an assignment-focused pass from a whole-queue failure caused by incomplete work owned elsewhere. Never modify shared rows merely to force a global green result.

**Pass-language discipline**

| observed result | defensible statement | overclaim to avoid |
| --- | --- | --- |
| `bash -n` succeeds | "The script parses under this Bash." | "The mapper works correctly." |
| Required artifacts are nonempty | "The producer emitted the required artifact set." | "The map covers the repository." |
| TSV schemas match | "Rows are structurally readable under the expected contract." | "The rows are accurate." |
| Selected pointer resolves | "This source range can be read on this revision." | "The range is the complete definition." |
| Sampled edge agrees with source | "This sampled relation is corroborated." | "All relations are precise and complete." |
| Project tests pass | "Exercised project behavior remains green under this configuration." | "No untested consumer or runtime path exists." |
| Focused reference verifier passes | "The assigned evolved artifact meets its structural gates." | "Every technical recommendation is universally true." |

A gate should also demonstrate rejection. Use disposable fixtures to confirm that unsupported inventory, malformed TSV rows, invalid pointers, alias misses, cap differences, and dynamic relationships produce the expected failure or uncertainty state. Without a negative case, a command may be ceremonial: it is known to pass healthy input but not known to detect the defect named in its contract.

## Agent Usage Decision Guide

Use this reference when the task involves codebase orientation, symbol or dependency discovery, pointer-first context selection, rough graph generation, analyzer choice, or interpretation of existing map artifacts. Relevance does not imply that a new map should be built. The first agent decision is which evidence route can answer the real question with the least cost and sufficient confidence.

**Routing sequence**

1. Read repository and directory-level instructions, then identify any native code search, ownership, build graph, language server, compiler query, architecture check, or generated index already expected by the project.
2. Restate the pending decision, not merely the surface query. "Find `Registry`" is a location question; "can I change `Registry` safely?" is a consumer and contract question.
3. If a known exact string, path, or symbol can answer a reversible location question, use direct `rg`, structural search, or an existing native index and read the source. Stop when the bounded question is answered.
4. If compatible map artifacts already exist, verify producer identity, target root, repository revision, working-tree state, options, capability branch, inventory policy, and artifact schemas before reuse.
5. If the repository is unfamiliar and the task requires broad candidate discovery across supported static source, build a fresh rough map in an explicitly authorized output directory, audit coverage, and query compact rows before reading files.
6. Resolve selected pointers and verify important relations in source. Do not stop at `summary.md`, Mermaid, DOT, SVG, or a fan-in ranking.
7. Escalate immediately when the decisive relationship is semantic, generated, configured, dynamic, runtime-dependent, security-sensitive, or requires proof of absence or complete recall.
8. Stop collecting evidence when the remaining uncertainty cannot change the bounded action, or hand the unresolved risk to a named owner with the needed next mechanism.

**Route selection matrix**

| task signal | default route | stop condition | escalation trigger |
| --- | --- | --- | --- |
| Exact error text, known filename, or one named symbol | Direct `rg`, structural search, or native symbol lookup, followed by source reading. | The expected construct and relevant local context are confirmed. | The task actually asks about callers, blast radius, ownership, or behavior beyond the located text. |
| Existing map with complete provenance and matching revision | Reuse compact artifacts; rerun invariant and sample checks appropriate to the decision. | Selected candidates and source evidence answer the bounded question. | Root, producer, revision, options, inventory policy, or capability branch differs or is unknown. |
| Existing map without provenance | Treat rows as untrusted hints only or rebuild in a fresh authorized location. | New evidence binds every used pointer and relation to current source. | Rebuild is prohibited or the missing provenance can change the conclusion; use direct or native tools instead. |
| Broad orientation in an unfamiliar repository | Build a rough map, audit inventory, inspect `tooling.tsv`, query TSV rows, and read ranked spans. | Entry points, likely boundaries, and next source reads are identified with explicit uncertainty. | Relevant source types are unsupported or framework wiring dominates. |
| Review prioritization or candidate hotspot discovery | Rank full relation rows, disclose caps and coverage, then sample important edges. | A defensible review order exists; centrality remains provisional. | Ranking changes ownership, architecture, or resource allocation without corroboration. |
| Refactor impact analysis | Use rough edges to enumerate candidates, then apply authoritative search, build, type, test, and contract checks. | Consumer evidence and project verification support the scoped change. | Public contracts, generated consumers, feature variants, or runtime registration may be missed. |
| "Nothing depends on this" or safe deletion | Use the empty rough result only to form stronger queries. | Appropriate semantic, build, configuration, and runtime evidence establish the bounded absence claim. | Always; rough non-observation is insufficient by itself. |
| Security reachability or authorization path | Skip rough mapping as primary evidence; use security-specific static, configuration, test, and runtime analysis. | The security claim is verified under defined threat and configuration boundaries. | Any unobserved dynamic or generated path remains material. |
| Unsupported language or relationship class | Use repository-native or language-aware tooling; the rough map may still locate adjacent supported files. | The decisive construct is observed by a suitable mechanism. | No available mechanism has adequate coverage; report and assign the unresolved risk. |
| Writes are restricted | Do not run the builder; use read-only source discovery or already authorized artifacts. | The question is answered without an out-of-scope write. | A fresh map is necessary; obtain authorization rather than writing implicitly. |

**Existing-artifact reuse contract**

An artifact is reusable only if all material dimensions match:

| dimension | reuse question | reject or narrow reuse when |
| --- | --- | --- |
| Producer | Which builder bytes and options created the directory? | Script identity or configuration is missing or differs in a way that affects the claim. |
| Target | Which repository root and nested-workspace boundary were scanned? | The current question includes files outside that root. |
| Source state | Which revision and working-tree state did the map observe? | Pointers, imports, generated files, or configuration have changed materially. |
| Environment | Which Ctags branch, Python, shell, `rg`, Graphviz, and optional capabilities were present? | Cross-run comparison assumes equivalent extraction or presentation but branches differ. |
| Inventory policy | Were tracked, untracked, ignored, generated, vendored, and unsupported files treated appropriately? | The pending claim depends on an excluded class. |
| Artifact integrity | Do required names, schemas, row counts, and presentation caps reconcile? | Rows are malformed, missing, stale, mixed, or inconsistent with summary views. |
| Decision scope | Was the artifact built for a question with compatible completeness and consequence requirements? | A navigation artifact is being promoted into deletion, security, or exhaustive consumer evidence. |

Age alone is not a sufficient freshness test. A one-minute-old map built from the wrong root is immediately stale for the decision, while an older map of an unchanged frozen revision can remain useful if producer and observation contract are preserved.

**Tool choice by observation strength**

| route | strength | cost and blind spot | use together with |
| --- | --- | --- | --- |
| Exact text search | Very fast evidence that matching text exists at reported lines. | Misses aliases and semantic identity; finds comments and unrelated strings. | Direct source reading and structural or semantic checks when meaning matters. |
| Structural search | Syntax-aware matches for expressible patterns. | Grammar and rule dependent; still may not resolve names or runtime wiring. | Positive and negative fixtures plus source review. |
| Rough CLI map | Broad, cheap inventory, symbol candidates, lexical relations, and compact graph projections. | Finite extensions, tracked-only Git inventory, fallback spans, heuristic resolution, and dynamic blind spots. | Coverage audit, pointer reads, sampling, and project-native verification. |
| Language server or semantic index | Resolved symbols, references, and sometimes call hierarchies. | Server capability, indexing coverage, generated code, and configuration vary. | Version/capability checks, source reads, compiler or build evidence. |
| Compiler or build graph | Strong evidence for configured compile and build relationships. | May cover only selected targets, features, and environments. | Variant matrix, tests, manifests, and runtime evidence. |
| Runtime trace | Observes actual exercised paths and dynamic registration. | Cannot reveal paths absent from the workload and may perturb timing or state. | Static evidence, workload design, and configuration audit. |
| Ownership or architecture metadata | Encodes intended boundaries and responsibility. | Can be stale or aspirational rather than descriptive. | Source and build behavior plus owner confirmation. |

The routes are complementary, not a maturity ladder. Rough breadth can identify candidates, semantic analysis can resolve identities, compiler or build data can establish configured composition, and runtime evidence can test dynamic paths. Use only the combination whose blind spots matter to the pending action.

**Scenario cards**

Good direct route: A user asks where `resolve_import_target` is defined. The agent uses exact or structural search, opens the matching source, disambiguates duplicates, and answers with a revision-bound pointer. Building a repository map would add side effects and delay without strengthening the location claim.

Good reuse route: A review needs likely fan-in candidates, and a map exists with matching script hash, revision, clean schemas, recorded edge cap, and reconciled inventory. The agent queries full TSV rows, verifies representative edges, and reports a provisional review order. Rebuilding is unnecessary.

Good build route: An unfamiliar supported-language repository has no native index, and the user asks for likely entry points and module neighborhoods. The agent builds into a fresh authorized directory, audits `all_files.txt`, `code_files.txt`, and `files.tsv`, records fallback extraction, queries candidates, and reads source before explaining boundaries.

Good escalation route: An empty inbound-edge query is being used to justify deleting a runtime-registered handler. The agent labels the rough result non-authoritative, inspects registration configuration and runtime behavior, uses language-aware references and project tests, and proceeds only if those independent mechanisms support the bounded absence claim.

Bad route: A named file is already known, but the agent builds a complete map, reads only `summary.md`, sees no visible inbound arrow in the capped SVG, and calls the file unused. This maximizes work while minimizing evidence quality.

Borderline route: A stale map supplies a likely file path during exploration. Reuse is acceptable only as an untrusted hint if the file is reopened on the current revision and no relation, ranking, or absence claim survives from the old artifact.

**Route-entry checks**

Before choosing a route, answer:

- What action could follow this evidence, and how reversible is it?
- Is the question about location, static text, symbol identity, configured dependency, runtime path, ownership, or complete absence?
- Which repository instructions and native tools govern the work?
- Does a compatible artifact already exist, and can its provenance be reconstructed?
- Can the rough builder observe every source and relationship class that might change the action?
- Is writing a map authorized in the chosen location?

**Route-exit and handoff checks**

Before stopping or handing off, record:

| field | content |
| --- | --- |
| Decision | The bounded action or explanation the evidence supports. |
| Route | Direct search, reused artifact, fresh rough map, semantic/build analysis, runtime evidence, or a deliberate combination. |
| Evidence | Producer and target identity, selected rows and pointers, direct source, project commands, and relevant outcomes. |
| Observation boundary | Included and excluded files, relation classes, configuration, runtime workload, and presentation caps. |
| Contradictions | Mismatches found, their pipeline stage, and which conclusions were invalidated. |
| Remaining uncertainty | What is unknown, whether it can change the action, and who owns escalation. |
| Stop reason | The question is answered, remaining uncertainty is immaterial, or a stronger mechanism or authorization is required. |

**Three-question continuation test**

After each evidence step, ask:

1. What material uncertainty remains?
2. Can resolving it change the bounded decision or prevent a consequential error?
3. Which available evidence source can falsify it with the least additional cost and side effect?

Continue only when all three answers justify another step. This qualitative value-of-information test avoids invented precision while preventing endless context accumulation. It also makes abstention legitimate: if the rough map cannot observe the decisive relation, the correct agent action is to route elsewhere, not to produce more rough artifacts.

## User Journey Scenario

This worked journey is illustrative. It demonstrates evidence transitions and failure recovery without claiming that the described files, counts, or runtime behavior were observed in the repository containing this reference.

**Opening state**

Role: A maintainer is preparing a change in an unfamiliar TypeScript service that also uses configuration-driven registration.

User request: "The central registry looks overloaded. Split it into smaller modules and remove the legacy loader if nothing uses it."

Primary uncertainty: The request combines two decisions with different evidence requirements:

- Branch A asks whether a statically visible registry is a useful refactor candidate and where its consumers lie.
- Branch B asks whether a loader has no live consumer and is safe to delete across source, configuration, generated state, and runtime variants.

Reference trigger: The task needs broad candidate discovery and dependency interpretation, but it also contains an absence claim that a rough lexical map cannot authorize alone.

**Step 1: Turn the request into claim cards**

| claim | action if true | consequence of false positive | evidence floor |
| --- | --- | --- | --- |
| The registry is a high-value refactor candidate. | Inspect responsibilities and propose a bounded split. | Review time may be misallocated or a cohesive module may be fragmented. | Coverage-audited static candidate ranking, direct source, representative consumer checks, and project tests for any implemented split. |
| The legacy loader is unused in every relevant configuration. | Remove source, registration, tests, and documentation. | A runtime path or customer configuration can fail after deletion. | Authoritative static references, configuration and generated-state audit, build variants, tests, and runtime evidence sufficient for bounded absence. |

The agent does not let evidence for Branch A answer Branch B. A map can be useful globally while supporting only a candidate-level claim locally.

**Step 2: Discover native instructions and choose the route**

The agent first reads repository instructions and discovers the documented build, type-check, test, and configuration-validation commands. No complete native dependency index exists. The service is unfamiliar and mostly uses supported `.ts` files, so a fresh rough map is appropriate for Branch A and for candidate enumeration in Branch B. The agent chooses a new authorized output directory and records repository revision, working-tree state, builder hash, and `MAX_GRAPH_EDGES`.

If a current native semantic index had existed, the journey would have used it first. If writes were restricted, the agent would have skipped the builder and used read-only search plus native tools.

**Step 3: Preflight without overclaiming**

The script syntax checks pass. `rg` and Python are available. The Ctags JSON capability probe fails, so symbol extraction will use the regex fallback and may produce one-line ranges. Graphviz is absent, so no SVG is expected; Mermaid and DOT text remain available. Ast-grep is detected but the builder does not automatically invoke it.

The agent records:

| observation | permitted conclusion | withheld conclusion |
| --- | --- | --- |
| Both shell files parse. | The selected Bash accepts the scripts. | The builder is accurate. |
| Ctags JSON probe fails. | Fallback span extraction should be expected for this run. | Every fallback symbol is incomplete or wrong. |
| Graphviz is absent. | SVG absence is an environment outcome. | The relation artifacts failed. |
| Ast-grep is available. | Structural search can be considered separately. | Structural extraction contributed to the map. |

**Step 4: Build, then audit coverage before reading the graph**

The authorized build completes. The agent reconciles `all_files.txt`, `code_files.txt`, and `files.tsv`. The audit reveals that tracked TypeScript source is represented, but `.yaml` registration files and generated JSON manifests do not enter `code_files.txt` because they are outside the supported extension set.

This is not a minor footnote. It changes Branch B's observation boundary. The loader may have no lexical TypeScript importer and still be selected through configuration. The agent marks configuration and generated registration as unresolved evidence classes before looking at the empty-edge result.

The coverage ledger becomes:

| surface | state | implication |
| --- | --- | --- |
| Tracked `.ts` and `.tsx` files | Included by the illustrative run. | Static lexical candidates can be queried, subject to extraction and resolver limits. |
| Untracked and ignored files | Excluded by the Git inventory branch. | Local development or generated behavior needs separate review if relevant. |
| YAML configuration | Not represented as code inventory. | Configuration-driven loader references cannot be ruled out by map edges. |
| Generated JSON manifest | Not represented by the supported code filter. | Generated registration must be inspected through build or artifact-specific tooling. |
| Runtime registration behavior | Outside static lexical observation. | A runtime probe or integration path is needed for Branch B. |

**Step 5: Query compact evidence before reading broad context**

The full `internal_file_edges.tsv` ranks the registry among likely fan-in candidates. The agent checks complete rows rather than relying on the edge-capped Mermaid or DOT view. It samples consumers from different directories, opens their import lines, and reads the registry implementation with expanded context because fallback symbol ranges are only entry points.

For the loader, the internal-edge query has no incoming row. The agent reports only: "No inbound relation to the loader was observed in this run's supported static lexical map." It does not say that the loader is unused.

**Step 6: Seek a counterexample deliberately**

The agent searches project configuration, build scripts, generated-manifest inputs, tests, and runtime registration code outside the rough relation table. In this illustrative scenario, a YAML registration key names the legacy loader, and startup code resolves that key through a dynamic registry. A representative integration configuration exercises the path.

That single positive counterexample refutes the universal unusedness claim. It does not matter that the rough map's empty result was internally consistent; the decisive relationship was outside its observation model.

| evidence event | branch affected | reasoning update |
| --- | --- | --- |
| Registry has corroborated static consumers. | Branch A | Retain as a review candidate, then inspect cohesion and contracts before splitting. |
| Loader has no rough inbound edge. | Branch B | Keep only as a static-map observation; initiate stronger absence checks. |
| YAML key and dynamic resolver connect to loader. | Branch B | Refute "unused in every relevant configuration" and block deletion. |
| Integration configuration exercises loader. | Branch B | Confirm current live use under that bounded configuration. |

**Step 7: Make a split decision instead of forcing one verdict**

Branch A can proceed to a scoped design review. The agent groups registry responsibilities, confirms selected consumer contracts, identifies a reversible extraction boundary, and proposes tests before implementation. Fan-in is a prioritization signal, not proof that splitting improves cohesion, so the design still needs source-level reasoning.

Branch B cannot proceed as requested. The agent explains that deletion is contradicted by configuration and runtime evidence. A separate migration could replace the loader registration, update generated state, cover every supported configuration, and only then revisit removal. That migration is a new authorized decision, not an implicit extension of the original cleanup.

**Step 8: Verify each branch with different gates**

| branch | verification before action | remaining boundary |
| --- | --- | --- |
| Registry review only | Direct implementation read, sampled consumers, responsibility analysis, and a proposed test plan. | No code behavior changes until implementation is authorized. |
| Registry split after authorization | Type checker, compiler or build, unit tests, integration tests, contract review, and authoritative consumer search. | Unexercised feature or deployment variants remain explicit. |
| Loader current-use conclusion | Configuration source, dynamic resolver, generated-state path, and representative integration run. | The positive use is bounded to observed configurations but already refutes universal unusedness. |
| Future loader removal | Migration inventory, all supported configurations, generated artifacts, semantic references, build variants, tests, and runtime checks. | Removal remains blocked until the migration's own acceptance criteria pass. |

**Step 9: Handoff the evidence, not just the answer**

The agent's concise handoff says:

> The rough map is useful for prioritizing the registry review: tracked TypeScript coverage was reconciled, full relation rows identify multiple static consumers, and representative imports were confirmed in source. That does not by itself prove a split is beneficial, so the next action is a bounded responsibility and contract review followed by tests if implementation is approved.
>
> The loader is not safe to remove. The rough map observed no supported static inbound edge, but YAML registration and the dynamic startup resolver connect it to an exercised integration configuration. The absence claim is refuted. Removal requires a separately scoped migration and configuration-wide verification.

The handoff includes producer hash, target revision, working-tree state, coverage exclusions, extraction fallback, selected pointers, project commands, observed contradiction, and next owner. It does not hand off the graph image as self-explanatory proof.

**Wrong turn and recovery**

Wrong turn: The agent sees no inbound arrow to the loader in the rendered graph and drafts a deletion patch.

Detection: The coverage checklist shows YAML and generated JSON outside `code_files.txt`, and the deletion claim has no independent absence gate.

Recovery: Stop the patch, invalidate the unusedness conclusion, search configuration and generated-state authorities, inspect runtime resolution, and update the claim card. The recovery revises the premise rather than finding a different weak artifact that supports deletion.

**Outcome variants**

| quality | outcome | why |
| --- | --- | --- |
| Good | Advance the corroborated registry review and block loader deletion with a concrete counterexample and migration route. | Verified branches make progress while uncertainty and contradiction remain contained. |
| Bad | Delete the loader because the capped visual has no inbound arrow. | Presentation, inventory, resolution, configuration, and runtime boundaries are ignored. |
| Borderline | Report no static edge and postpone deletion without checking configuration. | No unsafe change occurs, but the handoff is incomplete unless it names the missing check and owner. |

**Reusable journey pattern**

1. Decompose compound requests into claims with separate consequences.
2. Select the cheapest route that can observe each claim.
3. Audit coverage and extraction before interpreting relations.
4. Use compact rows to rank source reads, not to replace them.
5. Seek at least one counterexample to consequential absence or centrality claims.
6. Let contradictions change the route and invalidate dependent conclusions.
7. Advance verified branches independently from blocked branches.
8. Handoff evidence identities, observation boundaries, remaining uncertainty, and exact next action.

The second-order lesson is branch-local confidence. A tool does not have one global trust score for a task. The same rough map can be sufficiently useful to prioritize a static review and categorically insufficient to authorize deletion. Keeping confidence attached to claims allows safe parallel progress without either premature certainty or an unnecessary halt of the entire request.

## Decision Tradeoff Guide

Use the cheapest evidence route capable of falsifying the pending claim, then escalate when a remaining blind spot can change the action. "Cheapest" includes setup, context, side effects, late rework, and option loss. "Sufficient" is claim-specific: evidence adequate for navigation can be inadequate for refactoring, deletion, migration completeness, or security review.

**Preserved posture guide**

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | Current local implementation, repository instructions, and task fit support a rough-map workflow for candidate discovery. | Fast broad orientation, but the map still needs coverage checks, source reads, and claim-level verification. | Can the implemented inventory and relation model observe every class needed for this bounded claim? |
| Adapt when | Rough artifacts are useful but provenance, unsupported languages, configuration, generated code, aliases, or dynamic behavior require another evidence source. | Preserves discovery value while adding setup and reconciliation work. | Does each added method close a distinct blind spot, and are disagreements resolved rather than averaged? |
| Avoid when | The decisive relation is outside the observation model, artifacts are untrusted, writes are unauthorized, or a native semantic mechanism answers the question directly. | Prevents false confidence but may require specialized tooling or a narrower answer. | Is abstaining from a new rough map cheaper and stronger for the actual decision? |
| Cost of being wrong | Wrong guidance can send an agent to the wrong files, consumers, tests, ownership boundary, or deletion decision. | Rework ranges from a wasted search loop to a production or security regression; detectability and reversibility vary. | Would a reviewer know which premise failed, which conclusions to invalidate, and what evidence must come next? |

The seed's original local/external agreement test is refined here because public pointers were not refreshed and agreement between prose sources cannot validate target-repository behavior. Current local scripts establish mechanics; generated artifacts establish run observations; project evidence establishes semantics.

**Production and artifact-lifecycle choices**

| choice | choose when | benefit | cost or blind spot | escalation or rejection trigger |
| --- | --- | --- | --- | --- |
| Reuse an existing map | Producer, root, revision, working state, options, capabilities, and inventory policy match the current question. | No new writes or build cost; stable comparison surface. | Hidden staleness or mixed provenance can make plausible rows belong to another state. | Any material identity is missing or the decision needs a file class excluded by the original run. |
| Build a fresh rough map | Broad unfamiliar orientation is needed and an authorized output path exists. | Current compact inventory, symbols, lexical relations, and graph views. | Setup and write side effects; finite extensions and heuristic semantics remain. | A native index already answers the query, or the decisive relation is dynamic, generated, unsupported, or security-sensitive. |
| Use direct search without a map | The target string, file, error, or construct is already narrow. | Lowest setup and easy source confirmation. | Weak identity resolution and no broad neighborhood by default. | The real question concerns consumers, boundaries, or blast radius beyond the direct match. |
| Use repository-native generated data | The build system, ownership service, compiler, or project index provides a maintained graph. | Better project fit and often stronger semantics. | Configuration-specific, potentially opaque, and still subject to freshness and coverage. | The native output excludes relevant variants or conflicts with source and runtime evidence. |
| Decline artifact production | Writes are restricted or output ownership is unclear. | Preserves workspace boundaries and avoids contamination. | Broad reusable orientation may be slower through read-only methods. | Obtain explicit authorization only if a fresh map is necessary for the bounded decision. |

Freshness is multidimensional. Rebuilding improves temporal freshness but does not repair a wrong root, unsupported extension, or unsuitable observation model. Reuse can be more reproducible than a fresh run when the target is a frozen revision and all identities are preserved.

**Extraction and relation choices**

| method | strongest economical use | precision and recall boundary | setup and interpretation cost | pair with |
| --- | --- | --- | --- | --- |
| Regex fallback symbols | Quick candidate names and declaration-line entry points when JSON-capable Ctags is unavailable. | One-line spans, syntax noise, duplicate names, and limited language constructs. | Very low setup; higher source-expansion burden. | Pointer round trips, surrounding reads, and semantic identity when consequential. |
| JSON-capable Ctags | Cross-language symbol spans under supported parser kinds and fields. | Not a full type or call resolver; packaged binaries vary. | Capability probe and field validation required. | Direct source, duplicate-name review, and language-aware analysis for callers. |
| Lexical imports and includes | Broad candidate file relations and unresolved-reference inventory. | Aliases, re-exports, conditionals, dynamic loading, generated wiring, and framework semantics. | Cheap extraction; mismatch classification required. | Configuration, project-native resolution, and sampled endpoint reads. |
| Structural search | Syntax-aware patterns for a known construct. | Rule and grammar dependent; name resolution and runtime paths may remain absent. | Rule design and fixture cost. | Positive and negative fixtures plus source review. |
| Semantic index or language server | Resolved symbols, references, and supported call hierarchies. | Server capability, workspace indexing, generated code, and configuration variants. | Initialization, version matching, and service state. | Compiler/build evidence, source reads, and coverage probes. |
| Compiler or build graph | Configured compile and build relationships. | Selected targets, features, platforms, and generated states only. | Potentially expensive setup and execution. | Variant matrix, tests, configuration audit, and runtime evidence. |
| Runtime trace | Dynamic dispatch, registration, and actually exercised paths. | No evidence about unexercised workloads or configurations. | Instrumentation, data, safety, and interpretation cost. | Static evidence and deliberate workload coverage. |

Do not count method agreement without checking shared blind spots. Two lexical searches can both miss runtime registration. A rough map and its own summary are one evidence pipeline, not two independent confirmations.

**Retrieval choices**

| retrieval option | choose when | benefit | cost | boundary check |
| --- | --- | --- | --- | --- |
| Compact TSV query | The question can be expressed as path, symbol, edge, unresolved prefix, or rank filter. | Minimal context and reproducible selection. | Schema and quoting discipline; row meaning remains approximate. | Confirm the queried artifact belongs to the current run and use complete rows rather than capped projections. |
| `file:start:end` pointer read | A candidate is selected and local source context should be opened. | Precise, cheap, and easy to cite. | Stale, one-line, duplicate, or colon-path ambiguity. | Bind to revision, validate range, and expand context when semantics extend beyond it. |
| Complete file read | Module-level configuration, distant invariants, macros, annotations, or lifecycle context matter. | Preserves intra-file semantics and avoids tunnel vision. | More context and potential distraction. | State why the local pointer was insufficient and which full-file facts affect the claim. |
| Neighborhood read | Several endpoints or adjacent configuration files jointly define the relationship. | Captures cross-file causality without loading the repository. | Selection bias can omit a hidden authority. | Include at least one independent search for missing consumers or configuration. |
| Broad repository dump | Almost never the first choice; reserve for tiny repositories or explicit archival review. | Complete text under the chosen root. | Severe context dilution, poor ranking, repeated material, and hidden unsupported files outside the dump policy. | Demonstrate that repository size and task genuinely make broad loading cheaper than query-first retrieval. |

Pointer-first is a default, not a ban on whole files. The tradeoff is between context economy and semantic sufficiency. Expand as soon as annotations, configuration, module initialization, generated regions, or distant invariants can change interpretation.

**Presentation choices**

| view | benefit | distortion risk | safe use |
| --- | --- | --- | --- |
| Full TSV rows | Complete artifact-level relation population and structured filtering. | The artifact itself can still omit program relationships. | Counts, sampling frames, and reproducible queries. |
| `summary.md` | Fast counts, likely fan-in and fan-out candidates, and capability reminders. | Ranking can hide duplicates, omissions, caps, and relation quality. | First-pass prioritization followed by row and source checks. |
| Mermaid | Text-native, reviewable graph subset without requiring Graphviz. | Path labels and edge cap can simplify or distort the visible structure. | Communication and candidate navigation, never completeness proof. |
| DOT | Standard graph source that can be inspected even without a renderer. | Same edge-cap and relation-quality limits as other projections. | Reproducible visualization input with cap disclosed. |
| SVG | Convenient visual output when `dot` is available. | Visual density invites centrality overclaims and can conceal excluded edges. | Presentation after complete-row analysis and source sampling. |

Visual simplicity is not architectural simplicity. Use graph views to ask where to look, then use full rows and source to decide what the relationships mean.

**Verification-depth choices**

| depth | suitable action | evidence bundle | option loss if wrong |
| --- | --- | --- | --- |
| Navigation | Open a likely file or declaration. | Current candidate row plus pointer resolution and source read. | Low; another search can correct the path. |
| Explanation | Describe a static relationship or likely boundary. | Coverage audit, direct endpoint reads, selected configuration, and corroborating project mechanism where semantics matter. | Medium; readers may form a durable mental model from the explanation. |
| Review prioritization | Order files or modules for human inspection. | Full-row ranking, cap disclosure, deduplication, and representative edge samples. | Medium; review effort can be misallocated but remains reversible. |
| Refactor proposal | Change a boundary or shared interface. | Candidate map, authoritative consumer search, contract analysis, compiler/build, tests, and variant review. | High; implementation can break hidden consumers or create incohesion. |
| Deletion or migration completeness | Remove a component or assert every consumer is handled. | Semantic/build/configuration/runtime absence evidence under explicit scope plus project tests. | Very high; lost behavior and rollback cost can be substantial. |
| Security authorization | Assert a path cannot occur or a boundary is closed. | Security-specific static, configuration, test, runtime, and threat-model evidence. | Critical; rough mapping is auxiliary only. |

Hard gates are appropriate when a contract violation invalidates the action, such as missing relevant language coverage before deletion. Warnings are appropriate when uncertainty can remain visible without authorizing harm, such as missing SVG during navigation.

**Recommended evidence bundles**

| bundle | composition | why the methods complement each other | stop rule |
| --- | --- | --- | --- |
| Quick navigation | Direct or compact query -> pointer -> source. | Search finds candidate text; source confirms local meaning. | Stop when the bounded construct is identified and no broader action depends on it. |
| Broad orientation | Fresh or trusted map -> coverage audit -> compact ranking -> selected source reads. | Broad cheap evidence chooses narrow rich context. | Stop at a provisional architecture sketch with omissions disclosed. |
| Review ranking | Full TSV counts -> deduplication -> cap reconciliation -> stratified edge samples -> source. | Projection bias and resolver defects are checked before allocating review effort. | Stop when the order is robust enough for reversible review. |
| Refactor safety | Rough candidate neighborhood -> semantic or native consumers -> contracts -> build/tests -> configuration variants. | Discovery breadth and authoritative behavior checks cover different risks. | Stop only when acceptance criteria pass under defined variants. |
| Absence claim | Rough empty result as prompt -> independent search -> semantic/build/configuration/runtime evidence -> owner approval. | Each stronger source can expose a distinct false-negative class. | Stop when the scoped absence threshold is met or report unresolved risk. |

**Good, bad, and conditional choices**

Good: use `rg` and a source read to answer where a known symbol is defined; use rough map rows and samples to prioritize review; use semantic and runtime evidence to decide whether a dynamically registered component is absent.

Bad: build a fresh graph for every narrow lookup, treat two projections from the same lexical rows as independent confirmation, or use an empty rough edge query to authorize deletion.

Conditional: skip mapping for a low-risk refactor when repository-native consumer search, tests, and conventions already supply stronger applicable evidence. The required observation model matters more than the name of the tool.

**Pre-action tradeoff audit**

1. What exact claim and action are being considered?
2. What is the cost, detectability, and reversibility of a false positive or false negative?
3. Which source classes and relation types must be observable?
4. Which chosen methods share blind spots?
5. What independent signal would reveal the most consequential miss before action?
6. Does the route preserve the option to escalate, or does it commit to an irreversible change prematurely?
7. Which policy or domain assurance floor overrides cost optimization?

After the action, record where evidence disagreed, which route caused rework, how much context was unused, and whether a cheaper or stronger sequence would have changed the outcome. Repeated local observations can eventually calibrate setup cost, mismatch classes, and route choice. Until such data exists, comparisons in this guide remain qualitative reasoned defaults, not benchmarked accuracy or productivity claims.

The deeper tradeoff is option preservation. Early evidence should narrow the next choices without committing the team to conclusions it cannot support. A compact pointer-first map is valuable because it creates several informative next steps. It stops being valuable when its convenience is used to close a decision that only semantic, build, configuration, or runtime evidence can safely close.

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, conflicting, executable, observed-run, semantic, and unrefreshed-pointer roles. These roles form a partial order by claim type, not one universal ranking. A concise skill can be the canonical orientation source while its script outranks it for mechanics and target source outranks both for program behavior.

**Preserved seed hierarchy metadata**

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer | observed_identity_note |
| --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202602/dependency-map-cli-tools-01/SKILL.md | canonical primary source | Dependency Map CLI Tools 01; Overview; Workflow | What historical guidance, warning, or example should this snapshot contribute? | Hash-equal to the observed 202603 and current installed skill copies. |
| agents-used-monthly-archive/codex-skills-202602/dependency-map-cli-tools-01/references/internet-precedents.md | supporting detail source | Internet Precedents: No-DB Codebase Mapping; 1) Pointer-first navigation is standard; 2) "Precise first, search fallback" works in practice | Which locally retained rationale or public research pointer supports the workflow design? | Hash-equal to the observed 202603 and current installed precedent copies. |
| agents-used-monthly-archive/codex-skills-202603/dependency-map-cli-tools-01/SKILL.md | legacy historical source | Dependency Map CLI Tools 01; Overview; Workflow | What did this dated snapshot preserve, and did it diverge from the designated canonical snapshot? | Same observed bytes as the 202602 source; the reason for the `legacy` role is not recorded here. |
| agents-used-monthly-archive/codex-skills-202603/dependency-map-cli-tools-01/references/internet-precedents.md | supporting detail source | Internet Precedents: No-DB Codebase Mapping; 1) Pointer-first navigation is standard; 2) "Precise first, search fallback" works in practice | Which rationale persisted across archive snapshots? | Same observed bytes as the 202602 precedent source; repeated path is persistence evidence, not an independent factual vote. |

The seed labels are retained exactly as corpus metadata. No local assignment note explains why the 202602 skill is `canonical` and the byte-identical 202603 skill is `legacy`. The evolved hierarchy therefore does not invent a rationale or let those labels decide current executable behavior.

**Role definitions**

| role | authority | limitation | conflict response |
| --- | --- | --- | --- |
| canonical orientation | Default concise explanation of intended workflow for its temporal scope. | Can lag executable code and cannot prove a run or target behavior. | Preserve the guidance, then reconcile mechanics with current script bytes. |
| supporting detail | Rationale, examples, design precedents, and deeper caveats. | May paraphrase external sources or describe optional tools not used by the builder. | Use to formulate checks and alternatives, not to override direct implementation. |
| legacy historical | What a dated path contained and how guidance evolved. | Recency or label does not determine current correctness. | Cite for historical reconstruction; compare bytes and surrounding context. |
| duplicate content | Same observed bytes at another path. | Adds no independent substantive confirmation. | Read once for meaning, retain every path and date for provenance. |
| conflicting content | Sources make incompatible statements under apparently matching scope. | A fixed rank can hide a real version or behavior difference. | Narrow temporal and claim scope, identify producer, and seek stronger evidence. |
| executable implementation | Branches, supported extensions, output names, parsing, resolution, and pointer mechanics in a frozen script. | Defines possible behavior, not the branch selected by a future environment or semantic accuracy. | Prefer over prose for current mechanics; bind to a hash. |
| environment observation | Capabilities and versions visible to a particular process. | Mutable with machine, shell, `PATH`, installation, and time. | Capture with the run and refresh before cross-environment comparison. |
| observed-run artifact | Inventory, symbols, relations, tooling, summary, and projections produced from a specific target state. | Can be stale, malformed, incomplete, or misinterpreted. | Verify provenance and invariants, then use only for claims within its observation contract. |
| target semantic evidence | Source, project configuration, compiler/build output, tests, and runtime behavior under defined variants. | Each mechanism still has scope and workload limits. | Prefer for program behavior and reconcile any disagreement with rough artifacts. |
| unrefreshed external pointer | A locally retained URL and historical description that routes future research. | Does not attest to current remote content, version, or applicability. | Refresh primary documentation only when authorized and materially needed. |

**Claim-specific precedence matrix**

| claim | first authority | corroborating authority | source that must not overrule it |
| --- | --- | --- | --- |
| What the 202602 skill said | The exact 202602 archive bytes and surrounding archive context. | Hash comparison with other snapshots. | Current installation or later prose cannot rewrite the historical record. |
| What workflow is currently documented locally | Current installed `SKILL.md` at its recorded hash. | Current script and metadata for consistency. | An older archive snapshot cannot establish current text if bytes diverge. |
| Which extensions enter `code_files.txt` | Current hashed builder script. | Controlled fixture or a generated inventory from that producer. | Skill summary and public tool documentation cannot override implementation literals. |
| Which extractor actually contributed symbol rows | `symbols.tsv` kind values and `ctags.jsonl` state interpreted with `tooling.tsv`. | Script branch inspection, binary identity, and sampled pointers. | `tooling.tsv` exposes capability-probe results, but a failed or empty actual Ctags run can still lead to regex fallback. |
| Which files were observed | `all_files.txt`, `code_files.txt`, and `files.tsv` from the identified run. | Independent repository-native inventory and exclusion policy. | Guidance prose cannot prove target inclusion. |
| Which lexical relation row exists | Identified TSV artifact. | Producer version, endpoint source, and configuration. | Summary or graph projection cannot add rows absent from complete artifacts. |
| What a relation means in the program | Direct source plus suitable semantic, build, configuration, test, or runtime evidence. | Independent mechanism with a different observation model. | A lexical edge or inherited pattern score cannot settle semantics. |
| Whether a component is absent or safe to remove | Claim-specific authoritative absence evidence under explicit scope. | Owner review, variants, tests, and runtime checks as appropriate. | Empty rough-map output is only a prompt, never sole authority. |
| What a public tool currently documents | Fresh versioned primary source under browsing authorization. | Installed capability and local reproduction. | The unrefreshed local precedent note cannot establish current remote behavior. |

**Observed content families**

| family | paths observed | SHA-256 | hierarchy consequence |
| --- | ---: | --- | --- |
| Skill guidance | 202602 archive, 202603 archive, current installed skill | `b20aa296d11385ccfd9e0b5e35e2653768363a9c144e2d04f2e583c3c1b19806` | One semantic read supports three path identities; archive roles and dates remain separately recorded. |
| Precedent note | 202602 archive, 202603 archive, current installed note | `6225de10e11642bd9df819b33bfc01835f6af5659c0680ded4dad784929f6637` | One local rationale family with three provenance locations; remote pages remain unrefreshed. |
| Builder | Current installed script | `ea180f643cfa45edccdac825f5c4f263d0060f9edc9741a67adb8b93f7bd5ef3` | Executable authority for the implemented rough-map pipeline at this checkpoint. |
| Pointer reader | Current installed script | `5c1f54948a789d67ed8cf803c3e5291156e3ccac74ac01f43b70888198b8066d` | Executable authority for accepted pointer forms and range-window behavior. |
| Agent metadata | Current installed `agents/openai.yaml` | `3cca38f60acf2bfa2e5f310301807d35e476ab4bcead18695bf101733ca2ab71` | Presentation and invocation metadata only; no authority over map semantics. |

Content identity and contextual identity are separate. Hash equality proves the observed bytes match; it does not prove the paths were loaded by the same agent, packaged with identical surrounding files, or assigned the same corpus role.

**Default retrieval route**

1. Start with one representative skill copy to understand intended workflow and artifact vocabulary.
2. Consult the precedent note only for deeper rationale or a specific future external research route.
3. Read the current builder and pointer reader before stating present mechanics.
4. Capture environment capabilities before predicting which optional branch a run selects.
5. Inspect identified artifacts before making repository-specific inventory, symbol, or relation claims.
6. Read target source and use authoritative project evidence before making behavior, completeness, or safety claims.
7. Return to historical copies only when reconstructing evolution, validating archive persistence, or resolving a dated conflict.

This is a starting route, not a final authority ranking. The source that orients the reader may be weaker than the source that settles the claim.

**Conflict-resolution rules**

| conflict | resolution |
| --- | --- |
| Prose and script disagree on an output name or branch. | Treat prose as intent, script as current mechanics, record the discrepancy, and update derived guidance without altering the archive. |
| Static script and `tooling.tsv` appear inconsistent. | Verify producer hash, capability probe, environment, options, and whether artifacts are mixed or stale. |
| Artifact row and source disagree. | Reopen revision identity, pointer freshness, parser and resolver behavior; prefer current source for local text and use semantic evidence for meaning. |
| Rough map and compiler/build graph disagree. | Investigate configuration and observation scope; do not average the results. The stronger mechanism governs claims within its configured scope. |
| Two historical snapshots disagree. | Preserve both, identify dates and intended scope, and avoid allowing a later copy to rewrite the earlier record. |
| Public pointer summary and refreshed primary documentation disagree. | Retain the local summary as historical provenance, record retrieval version and date, and use the refreshed primary source for current external claims. |
| Role label and content identity appear inconsistent. | Preserve the label as corpus metadata, report the unexplained discrepancy, and exclude it from technical authority until semantics are known. |

**Good and bad hierarchy use**

Good historical claim: "The 202602 archive skill contains this workflow, and its bytes match the observed 202603 and current copies." This separates snapshot authority from persistence evidence.

Good mechanical claim: "The current builder hash defines the finite extension filter and writes `dependency_graph.mmd`; an authorized run must still show which repository files entered that branch." This matches source role to claim.

Bad corroboration claim: "Three skill files independently prove the mapper is accurate." The files are byte-identical guidance, not three accuracy studies.

Conditionally concise: cite one representative archive path in prose while retaining the complete duplicate ledger in durable evidence. This avoids repeated context without erasing provenance.

**Targeted invalidation**

| changed node | reopen | retain unless separately affected |
| --- | --- | --- |
| Guidance file | Recommendations, examples, and documented artifact contract. | Frozen run artifacts and independently established target semantics. |
| Builder | Every artifact and conclusion derived from its inventory, extraction, resolver, summary, or graph logic. | Historical snapshot claims and target facts established independently. |
| Pointer reader | Range-resolution evidence and source observations obtained through affected pointer forms. | Raw artifact rows that did not depend on reader output. |
| Environment | Selected extraction and render branches plus cross-run comparisons. | Producer bytes and repository revision. |
| Repository state | Inventory, spans, relations, rankings, tests, and runtime conclusions tied to the old state. | General method guidance and historical evidence. |
| External page | Current external fact statements and compatibility conclusions. | Locally retained historical pointer and prior captured snapshot identity. |

The hierarchy is causal: guidance informs implementation; implementation plus environment, options, and repository state produces artifacts; artifacts route direct source checks; source and authoritative project evidence support decisions. Feedback creates a new versioned trajectory. A discovered resolver defect may improve future scripts and guidance, but it must not rewrite what the prior artifact observed under its original producer.

## Theme Specific Artifact

The theme-specific artifact is a **Dependency Map Decision Record**: a compact provenance graph for one target state and one bounded decision. It references generated map files and source evidence rather than copying them. Its purpose is to preserve why selected rows mattered, which claims they support or refute, what may change the decision, and when the record becomes stale.

No separate decision record was created during this reference evolution because the write scope permits only the assigned reference, packet, and Delta journal. The schema below is a completion contract for a future authorized analysis artifact.

**Completion profiles**

| profile | use | required depth | explicitly unnecessary unless consequence changes |
| --- | --- | --- | --- |
| `navigation` | Open a likely file, declaration, or local neighborhood. | Target identity, candidate query, current pointer, direct source read, observation boundary, and stop reason. | Broad relation sampling, owner approval, exhaustive absence checks, and runtime evidence. |
| `standard_decision` | Explain architecture, prioritize review, or scope a reversible refactor. | Full run identity, coverage ledger, candidate ranking, representative positive and negative samples, claim cards, project checks, and invalidation rules. | High-assurance variant enumeration unless the claim depends on it. |
| `high_assurance` | Authorize deletion, migration completeness, security conclusions, or another material absence claim. | Standard profile plus authoritative semantic, build, configuration, generated-state, test, runtime, owner, and variant evidence appropriate to the domain. | Nothing relevant may be omitted silently; unresolved risk must block or be explicitly accepted by an authorized owner. |

Profiles prevent both bureaucracy and under-specification. A navigation record stays small. A deletion record cannot inherit that lightness merely because both began with the same `symbols.tsv` query.

**Block A: record and decision identity**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `record_identifier` | Use a stable local identifier unique to the target state and decision; do not encode an unverified conclusion in the name. | Issue, review, incident, or analysis identifier. |
| `record_profile` | Select `navigation`, `standard_decision`, or `high_assurance` and state why the consequence warrants it. | Decision tradeoff guide and project policy. |
| `user_goal_statement` | State the user's concrete goal, intended action, and relevant non-goals before applying Dependency Map Cli Patterns. | User request, repository instructions, and critique findings. |
| `decision_question` | Phrase one falsifiable decision per claim card, separating compound requests such as refactor priority and safe deletion. | User journey scenario and claim decomposition. |
| `decision_consequence` | Describe false-positive and false-negative effects, reversibility, and who bears the risk. | Domain context, owner input, and change plan. |
| `decision_boundary_rule` | Define when rough mapping is sufficient, when it is auxiliary, and when this reference should be avoided in favor of stronger evidence. | Decision tradeoff and agent usage guides. |
| `record_state` | Use `collecting`, `candidate`, `contradicted`, `verified_for_scope`, `escalation_required`, or `invalidated`; include a timestamp and owner for transitions. | Claim outcomes and verification ledger. |

Prohibited values include "looks complete," an unexplained confidence percentage, or "safe" without scope. Record state describes evidence status, not approval unless the project's authorization process explicitly says so.

**Block B: producer, target, and environment identity**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `producer_identity` | Record builder path, SHA-256, invocation, options, and output directory. | Current script bytes and shell history or captured command. |
| `pointer_reader_identity` | Record reader path and SHA-256 for every pointer used in durable evidence. | Current pointer script. |
| `target_identity` | Record canonical repository root, revision, branch if relevant, and remote or workspace identity needed to disambiguate clones. | Git or repository-native metadata. |
| `working_state` | Record clean or dirty state and list material uncommitted, generated, or local-only inputs without exposing secrets. | Repository status and build context. |
| `environment_identity` | Record shell, Python, `rg`, Ctags capability, ast-grep availability, Graphviz availability, and other branch-affecting versions. | Preflight output and `tooling.tsv`. |
| `run_time_window` | Record start and finish timestamps plus time zone when artifacts or external state can change during collection. | Run capture. |
| `artifact_manifest` | List every generated artifact, size or row count, hash when durable comparison matters, and missing conditional output with reason. | Authorized output directory. |

This block prevents a current-looking row from being detached from the producer and source state that created it. A map without reconstructable identity remains a navigation hint, not a decision record.

**Block C: coverage and observation ledger**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `inventory_mode` | State Git tracked-file or non-Git `rg --files` branch and explain why that population fits the question. | Builder implementation and `all_files.txt`. |
| `raw_inventory_result` | Record `all_files.txt` count and independent reconciliation outcome. | Raw inventory plus repository-native check. |
| `code_inventory_result` | Record `code_files.txt` and `files.tsv` counts, equality check, and relevant extension differences. | Filtered artifacts and independent extension inventory. |
| `excluded_surface_classes` | Enumerate untracked, ignored, generated, vendored, nested, unsupported-language, configuration, data, and runtime surfaces that matter or explain why each is not applicable. | Working state, manifests, build inputs, project conventions. |
| `extraction_mode` | Record JSON-capable Ctags or fallback branch and its range-quality implications. | `tooling.tsv`, capability probe, and sampled symbols. |
| `relation_model` | State that imports and includes are lexical, name the supported forms actually relevant, and list known semantic blind spots. | Builder script and target samples. |
| `presentation_boundary` | Record `MAX_GRAPH_EDGES`, complete relation counts, projected counts, and optional SVG status. | Environment, TSV rows, Mermaid, DOT, SVG, and summary. |
| `coverage_sufficiency` | State whether coverage is sufficient for each claim card, not for the record globally. | Claim consequence and excluded surfaces. |

Silence is not an acceptable exclusion policy. A field may say that a class is not applicable only with a reason tied to the bounded decision.

**Block D: evidence item registry**

Every retained observation receives an identifier such as `EVIDENCE-001`; identifiers are local references, not scores.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `evidence_identifier` | Assign a unique stable identifier inside the record. | Record-local sequence. |
| `evidence_class` | Use `local_guidance`, `implementation`, `environment`, `artifact_row`, `source_span`, `project_check`, `runtime_observation`, or `unrefreshed_pointer`. | Local corpus hierarchy. |
| `evidence_locator` | Provide exact path, artifact row key, `file:start:end`, command, test name, or runtime trace identity. | Generated artifacts and direct checks. |
| `evidence_observation` | State only what was observed, without embedding the decision inference. | Raw output or source. |
| `evidence_scope` | Record revision, configuration, workload, language, sample-selection rule, and relevant exclusions. | Run and project context. |
| `evidence_reproduction` | Give the minimal read-only or authorized command and expected observable result. | Verification gate command set. |
| `evidence_supports_or_refutes` | Link every item to claim identifiers and label support, refutation, or context. | Claim registry. |
| `evidence_freshness_trigger` | Name the producer, repository, configuration, or environment change that invalidates reuse. | Source dependency graph. |

Do not paste whole source files, full TSVs, or opaque screenshots into this block. Retain stable locators and enough observation detail for another operator to reproduce the relevant evidence.

**Block E: candidate and dependency probe**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `query_statement` | Record the exact compact query, filter, rank, or unresolved cluster used to choose candidates. | TSV query or repository-native command. |
| `candidate_selection_rule` | Explain why these rows were selected and which relevant rows were excluded. | Full artifact population and task question. |
| `ownership_map` | Record declared owner, inferred owner, evidence source, and disagreement; do not infer ownership solely from graph centrality. | Ownership files, history, team input, and source boundaries. |
| `false_positive_rules` | List expected lexical false-positive classes and how sampled candidates were checked. | Anti-pattern registry and mismatch log. |
| `false_negative_rules` | List unsupported file, alias, dynamic, generated, configuration, and runtime classes relevant to the claim. | Coverage and relation boundaries. |
| `blast_radius_candidates` | List possible consumers or affected files as candidates with evidence links, not as a complete set unless stronger checks establish completeness. | Internal edges, semantic references, build graph, and tests. |
| `graph_projection_note` | State whether any conclusion came from summary, Mermaid, DOT, or SVG and link the complete rows used to validate it. | Presentation artifacts. |

The original theme artifact called for an ownership map, false-positive rules, and blast-radius examples. This block preserves those requirements while preventing a rough graph from claiming actual ownership or exhaustive impact.

**Block F: claim cards**

Each actionable claim receives an identifier such as `CLAIM-001`.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `claim_identifier` | Assign a stable record-local identifier. | Record-local sequence. |
| `claim_text` | Use bounded language that can be falsified and avoid converting non-observation into absence. | Decision question. |
| `claim_class` | Mark `candidate`, `observed`, `corroborated`, `verified_for_scope`, `refuted`, or `unresolved`. | Claim-strength ladder. |
| `claim_consequence` | Link to the exact action and error cost affected by this claim. | Decision identity block. |
| `supporting_evidence` | Link only evidence items that directly support the statement. | Evidence registry. |
| `counterevidence` | Link contradictions, missing coverage, and plausible alternative explanations. | Mismatch and evidence registries. |
| `sufficiency_rule` | State the evidence threshold for promotion to the next class. | Project policy, domain risk, and tradeoff guide. |
| `claim_owner` | Name who can accept, reject, or escalate the decision if authorization is needed. | Project ownership process. |
| `claim_invalidation` | List precise changes that return the claim to collecting or invalidated state. | Producer, source, environment, configuration, and workload dependencies. |

Confidence attaches to each claim, not to the map directory. One claim can be verified for a static review while another from the same run remains unresolved for deletion.

**Block G: mismatch and uncertainty log**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `mismatch_identifier` | Assign a unique identifier and pipeline stage. | Comparison or failed check. |
| `expected_observation` | State what the artifact or method was expected to show and why. | Contract or prior evidence. |
| `actual_observation` | Record the exact difference without immediately assigning cause. | Artifact, source, or project check. |
| `mechanism_hypothesis` | List plausible inventory, extraction, resolution, presentation, configuration, or runtime causes. | Anti-pattern registry. |
| `falsification_step` | Name the smallest check that distinguishes the leading causes. | Verification gates. |
| `resolved_mechanism` | Record confirmed cause or `unresolved` with remaining alternatives; never force closure. | Check outcome. |
| `invalidated_claims` | Link every downstream claim or ranking that must be reopened. | Claim dependency links. |
| `builder_learning` | Record whether a fixture, script change, guidance change, or no action is warranted. | Repeated mismatch pattern. |

Unresolved is a valid state. A complete-looking form must not force an unsupported mechanism or conclusion.

**Block H: verification and decision ledger**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `verification_gate_rule` | Define the command, checklist, review question, expected result, and claim it can prove. | Verification gate command set. |
| `verification_outcome` | Record pass, fail, contradiction, not applicable with reason, or not run with authorization or capability reason. | Captured result. |
| `verification_limitation` | State what a pass leaves unproven, including configuration and sample boundaries. | Gate contract. |
| `decision_result` | Record proceed, proceed within scope, redesign, reject, or escalation required for each claim. | Claim ledger and owner. |
| `implementation_boundary` | Name files, contracts, tests, configurations, and non-goals authorized by the decision. | Change plan. |
| `rollback_or_recovery` | Explain how to undo the action and which evidence to inspect if the claim fails. | Project operations and source dependency graph. |
| `next_action` | Provide an executable next step, owner, and stop condition; never leave the field empty. | Unresolved claim or approved work. |

**Block I: record invalidation and review**

| invalidation_event | minimum response |
| --- | --- |
| Builder or option change | Rebuild artifacts and reopen every claim derived from inventory, extraction, relation, summary, or graph behavior. |
| Pointer-reader change | Replay durable source-span evidence affected by pointer parsing or context behavior. |
| Repository or dirty-state change | Regenerate inventory and pointers; rerun project checks for every changed dependency surface. |
| Environment capability change | Reevaluate extraction and rendering comparability; do not compare branch-dependent metrics blindly. |
| Configuration, generated state, or runtime workload change | Reopen every claim whose behavior boundary includes the changed variant. |
| New mismatch class | Invalidate dependent claims, add a reproducing fixture when appropriate, and review whether earlier records share the premise. |
| External documentation refresh | Update current external claims while preserving the locally retained historical pointer and prior retrieval identity. |

**Acceptance checklist**

A standard or high-assurance record is accepted only when:

- the producer, target, environment, and artifact identities are reconstructable;
- inventory and extraction boundaries are explicit and reconciled with the question;
- every claim has bounded language, consequence, evidence links, counterevidence, owner, and invalidation rule;
- every retained evidence item supports, refutes, or contextualizes at least one claim;
- graph projections are linked back to complete rows and source samples;
- absence, deletion, migration, and security claims use stronger evidence than rough non-observation;
- mismatches identify affected downstream claims and remain unresolved when cause is not established;
- verification outcomes state what they do not prove;
- the next action and stop condition are nonempty;
- sensitive paths, data, and outputs follow project handling policy.

**Quality contrast**

Good record: identifies a current producer and revision, says a module is a *candidate* hub under tracked supported static relations, links full rows and sampled source, records missing configuration coverage, and routes a deletion subclaim to stronger evidence.

Bad record: pastes an SVG, assigns an unexplained `95%` confidence, calls visible edges the complete blast radius, omits dirty state and edge cap, and approves deletion from no inbound arrow.

Recoverable record: preserves a candidate pointer and source observation but lacks producer identity. It may remain a navigation hint after the current source is reread; all relation, ranking, and completeness claims are downgraded until provenance is restored or the map is rebuilt.

The record is a provenance graph in compact human-readable form: inputs and transformations produce observations; observations support or refute claim cards; claim cards authorize bounded actions; changes invalidate only dependent claims. For durable work, this permits selective review of the smallest changed evidence cut instead of ceremonial repetition of the entire workflow. For quick navigation, use the reduced profile and stop before the form costs more than the decision it protects.

## Worked Example Set

All repositories, paths, rows, and outcomes in this section are illustrative. The mechanisms are grounded in the frozen local scripts, but no fixture or target map was generated under this assignment's exclusive-write boundary. Each example states what a future authorized replay should observe.

Every example uses the same evidence frame:

| field | question |
| --- | --- |
| Decision | What bounded action or explanation is being considered? |
| Cheapest valid route | Which method can answer it without unnecessary context or writes? |
| Observation | What did the selected evidence actually show? |
| Missing evidence | Which plausible fact remains outside that observation model? |
| Verification | What independent check can support or refute the claim? |
| Defensible conclusion | What can be said now, under what scope? |
| Rejected overclaim | Which tempting statement exceeds the evidence? |
| Invalidation | What change makes the conclusion stale? |

**Example 1: Direct navigation should skip map production**

Decision: Locate the implementation of a named function `resolve_import_target` so a maintainer can read it. No caller, blast-radius, or absence claim is requested.

Cheapest valid route: Use exact or structural search, disambiguate duplicate definitions by path and signature, then read the current source. Building a rough repository map would add write and setup cost without strengthening this location claim.

| evidence step | illustrative observation | interpretation |
| --- | --- | --- |
| Exact search | A definition-like match appears in `tools/resolver.py`. | Candidate location only; comments, tests, or duplicate names can also match. |
| Direct read | The source span contains the expected parameters and implementation. | The bounded location question is answered on this revision. |
| Repository status | The file belongs to the current target state. | The pointer can be handed off with revision identity. |

Missing evidence: The search does not establish every caller or whether the function is used dynamically. Those facts are not needed for the stated navigation action.

Defensible conclusion: "The current implementation is at the cited source pointer." Rejected overclaim: "This is the only implementation and its complete blast radius is known."

Invalidation: Rename, move, source edit affecting line ranges, revision change, or discovery of another same-scope definition.

Future replay: Create a small fixture with a definition, a comment mention, and a same-name test helper. Confirm that direct search plus source inspection selects the implementation while the route stops without map production.

Transferable rule: Do not pay broad-orientation cost for a bounded location question.

**Example 2: Rough orientation with fallback spans**

Decision: Identify likely entry points and static module neighborhoods in an unfamiliar supported-language repository that lacks a native semantic index.

Cheapest valid route: Build a fresh map in an authorized directory, reconcile inventory, inspect `tooling.tsv`, rank full TSV rows, and resolve selected pointers.

Illustrative observations:

- `all_files.txt`, `code_files.txt`, and `files.tsv` reconcile for the intended tracked `.rs` and `.ts` files.
- The Ctags JSON probe is unavailable, so `symbols.tsv` contains fallback entries whose `start_line` and `end_line` are often equal.
- `summary.md` identifies candidate fan-in and fan-out files; full `internal_file_edges.tsv` rows supply the sampling frame.
- Expanded source reads show that one candidate is startup wiring and another is a test-only helper.

Missing evidence: Lexical edges do not resolve every alias, macro, generated module, or runtime registration. One-line pointers do not define complete symbol bodies.

Verification: Inspect representative entry-point source, compare manifest or build targets, confirm selected edges at both endpoints, and run repository-native entry or build checks.

Defensible conclusion: "These files are prioritized candidates for orientation under tracked supported static source; direct reads distinguish production startup from test helpers." Rejected overclaim: "The map contains every entry point and each symbol range is complete."

Invalidation: Producer, capability branch, root, inventory policy, repository revision, or build-target change.

Future replay: Exercise the same source fixture under JSON-capable Ctags and forced fallback, then verify that pointer quality changes while candidate navigation remains possible.

Transferable rule: Extraction fallback changes range confidence, not the need to inspect source.

**Example 3: Unresolved does not mean third-party**

Decision: Classify dependencies before changing package boundaries in a TypeScript project that uses a configured alias such as `@core/registry`.

Cheapest valid route: Query `external_ref_edges.tsv` to find unresolved families, then inspect `tsconfig` or build alias configuration and resolve representative references through a project-aware mechanism.

| evidence | illustrative result | evidence state |
| --- | --- | --- |
| Lexical import extraction | `services/start.ts` refers to `@core/registry`. | Observed raw reference. |
| Rough internal resolver | No matching internal target row is emitted. | Unresolved, not classified. |
| Project configuration | The `@core/*` alias maps to an internal `src/core/*` path. | Counterevidence to third-party classification. |
| Semantic or build check | The configured tool resolves the import to the internal registry file. | Corroborated internal dependency under that configuration. |

Missing evidence: Other alias variants, conditional mappings, and generated paths may still need examination for a complete boundary migration.

Defensible conclusion: "This unresolved rough-map row is an internal configured alias under the inspected project configuration." Rejected overclaim: "Every row in `external_ref_edges.tsv` is an external package."

Invalidation: Alias configuration, selected target, resolver, package layout, or source import change.

Future replay: Include one internal alias, one actual third-party package, one relative import, and one malformed alias. Verify that rough output groups them as unresolved candidates while configuration-aware checks separate classes.

Transferable rule: Unresolved is a workflow state, not a dependency taxonomy.

**Example 4: Edge-capped graphs are projections**

Decision: Prioritize modules for code review from a repository whose complete internal relation table contains more rows than the configured graph cap.

Cheapest valid route: Compute candidate fan-in and fan-out from complete TSV rows, disclose the cap, deduplicate, sample high-impact edges, then use Mermaid, DOT, or SVG only for communication.

Illustrative observations:

- The run records a finite `MAX_GRAPH_EDGES`.
- `internal_file_edges.tsv` has more relation rows than `dependency_graph.mmd` and `dependency_graph.dot` can display under that cap.
- A module that appears visually sparse has several valid rows beyond the projected subset.
- A visually dense module includes duplicate or low-value test relations that change its apparent priority.

Missing evidence: Static degree does not encode runtime criticality, change frequency, ownership, complexity, or business impact.

Verification: Reconcile row and projected counts, calculate the exact ranking metric from full rows, inspect duplicates, sample endpoints, and compare with repository ownership and change context.

Defensible conclusion: "The full static relation table suggests this review order under the stated metric and coverage." Rejected overclaim: "The SVG visually proves the architecture's most critical hub."

Invalidation: Edge-cap, relation extraction, deduplication, ranking metric, inventory, or source revision change.

Future replay: Generate a fixture with relation count above a deliberately small cap and verify that complete-row rankings remain stable while the graph omits selected edges.

Transferable rule: Analyze complete artifacts before interpreting a presentation subset.

**Example 5: A pointer is bound to source state**

Decision: Reuse a saved `file:start:end` pointer from a previous review to patch the same definition after nearby lines were inserted.

Cheapest valid route: Reject blind reuse, confirm producer and revision, validate bounds, search for the qualified construct, and generate a current pointer before editing.

| evidence step | illustrative result | update |
| --- | --- | --- |
| Old pointer read | The range resolves but now covers a neighboring helper. | Syntactically readable, semantically stale. |
| Qualified search | The intended definition moved farther down the same file. | New candidate found. |
| Expanded source read | Signature, annotations, and body match the review target. | Current local observation established. |
| Project diff and checks | The patch affects the intended construct and passes relevant verification. | Change evidence bound to current state. |

Missing evidence: A valid current pointer still does not establish every consumer or safe refactor boundary.

Defensible conclusion: "The earlier pointer is invalid for this revision; the regenerated pointer identifies the intended definition." Rejected overclaim: "Because the old line range still exists, it still names the same symbol."

Invalidation: Any later source edit that changes path, line layout, generation, or identity.

Future replay: Create a fixture, capture a pointer, insert lines and another declaration above it, then verify that range validity alone cannot detect semantic staleness.

Transferable rule: Pointer readability and pointer identity are different properties.

**Example 6: Empty static edges cannot authorize deletion**

Decision: Remove an apparently unused handler that is selected through runtime configuration rather than a static import.

Cheapest valid route: Use rough empty results only to formulate stronger searches, then inspect configuration, generated registries, semantic references, tests, and a representative runtime path.

Illustrative observations:

- The handler file enters `code_files.txt`, but a YAML registry does not because its extension is unsupported by the code filter.
- `internal_file_edges.tsv` has no inbound row to the handler.
- Configuration contains the handler's registration key, and startup code resolves keys dynamically.
- An integration configuration exercises the handler.

Missing evidence: Other supported configurations and future generated states still define the full migration scope, but one positive use already refutes universal unusedness.

Verification: Trace the key through configuration and dynamic resolution, run a representative integration check, enumerate supported variants, and define migration acceptance before revisiting deletion.

Defensible conclusion: "No supported static lexical inbound edge was observed, but the handler is used in the inspected runtime configuration, so deletion is blocked." Rejected overclaim: "No graph edge means no dependency."

Invalidation: Configuration, generated registry, runtime workload, startup resolution, or source change; a future removal decision requires new evidence across all relevant variants.

Future replay: Build a disposable fixture with a dynamically registered handler and assert that the rough map omits the runtime edge while the configuration and integration probe detect use.

Transferable rule: One positive counterexample refutes universal absence; rough non-observation cannot establish it.

**Good, bad, and borderline synthesis**

| classification | behavior | promotion or downgrade trigger |
| --- | --- | --- |
| Good | Loads claim-relevant local sources, chooses the cheapest valid route, records coverage and provenance, verifies selected evidence, seeks counterexamples, and changes course on contradiction. | May promote a claim only when its explicit sufficiency rule passes. |
| Bad | Uses the reference as a generic tutorial, ignores mapped local paths and current scripts, treats summary or graph as authority, and leaves no falsification or recovery route. | Must discard or reconstruct conclusions before any action. |
| Borderline | Retains thin or stale evidence only as an untrusted navigation hint with a current direct source read and visible warning. | Promote after producer and claim-specific verification; downgrade immediately if the hint enters durable review or automation without that evidence. |

**Fixture promotion criteria**

Promote an explanatory example into an executable regression fixture when the failure has recurred, can be represented without sensitive project data, has a deterministic expected artifact difference, and protects a consequential interpretation or branch. A useful fixture records producer identity, positive and negative cases, exact expected evidence state, and the unsafe conclusion it prevents. Do not expand the fixture suite merely to mirror every paragraph; preserve examples whose replay catches a real class of future drift.

## Outcome Metrics and Feedback Loops

No outcome values were measured while evolving this reference. The metrics below are future capture definitions, not current results, universal targets, or claimed productivity gains. Establish local baselines under stable definitions, retain raw evidence and cohort identity, and refuse comparisons when producer, repository population, task mix, or sampling policy materially changes.

**Metric card contract**

Every reported metric must include:

| field | completion rule |
| --- | --- |
| Decision purpose | Name the workflow or tool choice the metric can change. |
| Definition | Specify numerator, denominator, unit, inclusion, exclusion, and deduplication rules. |
| Cohort | Record repository, revision range, language mix, task class, producer, options, capability branch, and profile. |
| Sampling | State random, stratified, risk-based, exhaustive, or fixture selection and why it represents the claim. |
| Raw evidence | Retain row identifiers, source pointers, command results, mismatch records, or incident links needed to recalculate. |
| Counter-metric | Name the quality or safety signal that prevents optimization of the metric in isolation. |
| Uncertainty | Report sample size and known bias; use a no-comparison state when conditions differ. |
| Trigger | Define what change prompts investigation, not an unsupported universal pass threshold. |
| Action | Choose fix, document, reroute, expand with evidence, retire, or collect more data. |
| Invalidation | State which producer, definition, repository, or policy change makes the series incomparable. |

The original leading indicator remains valid only when made concrete: the chosen boundary should reduce decision-relevant uncertainty or unnecessary blast-radius exploration, as shown by explicit probes and without increasing missed consequential evidence.

**Deterministic contract gates**

These are pass/fail properties of one identified run, not estimates of semantic quality.

| gate metric | definition | pass interpretation | failure action |
| --- | --- | --- | --- |
| `producer_identity_complete` | Required producer path, hash, invocation, options, target root, revision, working state, and output location are present. | Another operator can identify the intended run inputs. | Downgrade artifacts to hints or rebuild with a complete manifest. |
| `artifact_set_consistent` | Required artifact names exist, schemas match, conditional SVG behavior agrees with `tooling.tsv`, and no mixed producer identity is detected. | The output contract is structurally usable. | Diagnose production, stale mixing, or schema drift before interpretation. |
| `inventory_rows_reconcile` | `code_files.txt` paths equal `files.tsv` paths under documented sorting and `all_files.txt` matches the implemented inventory branch. | Internal artifact inventory transformation is consistent. | Repair the producer or reject the run; separately assess whether inventory policy fits the task. |
| `pointer_bounds_valid` | Every durable cited pointer names an existing current file and valid integer range after revision binding. | Cited spans can be read. | Regenerate or disambiguate; validity still does not prove semantic identity. |
| `graph_projection_bounded` | Edge cap, full TSV count, Mermaid count, DOT count, and optional SVG state are recorded and noncontradictory. | Presentation limits are explicit. | Rebuild or correct projection claims before using the visual. |
| `claim_next_action_present` | Every unresolved or contradicted consequential claim has a nonempty owner, next mechanism, and stop condition. | Uncertainty has an operational route. | Block handoff until responsibility and evidence need are explicit. |

A deterministic green gate cannot be summed into an accuracy score. All six can pass while lexical relations still miss dynamic behavior.

**Sampled artifact-quality indicators**

| indicator | numerator | denominator | required stratification | misuse warning |
| --- | --- | --- | --- | --- |
| `pointer_resolution_rate` | Sampled symbol rows whose paths and bounds resolve on the bound revision. | All sampled symbol rows. | Language, extraction branch, multiline shape, duplicate name, file size, and decision importance. | Resolution does not mean the span covers the full construct. |
| `pointer_semantic_hit_rate` | Resolved sampled rows whose span or expanded context identifies the intended symbol. | Resolved sampled symbol rows inspected in source. | Same strata plus overloaded or nested constructs. | A high hit rate cannot establish recall for symbols never extracted. |
| `internal_edge_agreement_rate` | Sampled internal rows corroborated by source and the selected project-aware mechanism. | All sampled internal rows with completed checks. | Language, edge kind, alias use, directory boundary, test/production class, and fan rank. | Convenience positives can hide false edges in difficult classes. |
| `unresolved_classification_completion` | Sampled unresolved rows classified as internal miss, actual external, unsupported form, generated/configured, or still unresolved with reason. | All sampled unresolved rows. | Prefix cluster, language, source directory, and consequence. | Lower unresolved count is not inherently better; aggressive false resolution can game it. |
| `rough_absence_counterexample_rate` | Investigated rough empty or missing-edge claims for which stronger evidence finds at least one relevant relation. | Consequential rough absence claims sent to stronger checks. | Claim type, language, dynamic/configuration risk, and action consequence. | The metric reflects selected investigations and must not estimate global false-negative probability without representative design. |
| `ranked_candidate_usefulness` | Inspected ranked candidates that contribute to final source evidence or a documented eliminated hypothesis. | All ranked candidates inspected for the decision. | Query type, ranking method, repository area, and profile. | Eliminated hypotheses can be useful; counting only confirmed candidates rewards confirmation bias. |
| `mismatch_localization_rate` | Recorded mismatches assigned to a verified inventory, extraction, resolution, presentation, retrieval, or semantic mechanism. | All mismatches investigated to the agreed effort limit. | Pipeline stage and severity. | Do not force a mechanism to improve the ratio; unresolved is valid. |

Report counts alongside every rate. A ratio based on two easy samples should not look comparable to a stratified review of many high-impact rows. Controlled fixtures and target-repository samples must remain separate cohorts.

**Workflow and context indicators**

| indicator | definition | desirable interpretation | counter-metric |
| --- | --- | --- | --- |
| `time_to_first_relevant_source` | Elapsed time from clarified decision to the first source span later retained in evidence. | Routing and compact querying find a useful starting point quickly. | Final evidence sufficiency and late contradiction count; speed alone can reward premature commitment. |
| `selected_context_usefulness` | Inspected source units that support, refute, or materially contextualize a final claim divided by all inspected source units under a stable unit definition. | Query-first retrieval limits irrelevant reads while valuing eliminated hypotheses. | Missed-consumer and post-action defect signals; low context can mean under-search. |
| `whole_file_expansion_yield` | Complete-file expansions that reveal a material fact absent from the initial pointer divided by all complete-file expansions. | The pointer-to-file escalation rule selects cases where wider context matters. | False-negative reviews; low yield may reflect overexpansion, while high yield may indicate pointers are routinely too narrow. |
| `artifact_reuse_acceptance` | Existing artifact sets accepted after provenance and compatibility review divided by all reuse candidates. | Reuse saves rebuilds when identities genuinely match. | Stale-artifact discoveries and decision reversals; maximizing acceptance is unsafe. |
| `reproduction_success_rate` | Decision records another operator can replay to the same artifact observation under the recorded state divided by records audited. | Provenance and commands are usable. | Semantic agreement and environment portability; replaying the same weak producer does not validate truth. |
| `route_escalation_yield` | Escalations that discover material confirming, refuting, or boundary-changing evidence divided by completed escalations. | Agents route consequential uncertainty to stronger evidence productively. | Missed escalation incidents; maximizing yield can discourage necessary precautionary checks. |

Time and context measures are optional. Collect them only when routing efficiency is a real optimization question and when instrumentation does not distort the work. Never compare elapsed time across unlike repository sizes, task classes, machine states, or approval constraints without adjustment and explanation.

**Decision and downstream outcome indicators**

| indicator | definition | feedback meaning | latency |
| --- | --- | --- | --- |
| `pre_action_claim_reversal_count` | Claims downgraded or refuted by verification before implementation or authorization. | Often a healthy sign that counterexample checks prevent weak evidence from escaping. | Immediate. |
| `post_action_evidence_reversal_count` | Decisions reopened after action because material evidence was missed, stale, or misclassified. | Investigate route, coverage, escalation, and handoff failures. | Delayed. |
| `map_attributable_rework` | Rework episodes whose verified cause includes a wrong map-derived candidate, relation, absence, rank, or stale pointer. | Quantifies downstream cost only after causal review. | Delayed and confounded. |
| `escaped_dependency_defect_count` | Production, integration, or review defects where a relevant dependency was omitted or misinterpreted after the workflow claimed sufficient evidence. | High-severity lagging signal that can set a safety boundary even without statistical volume. | Potentially long. |
| `safe_abstention_count` | Consequential claims explicitly routed away from rough mapping before unsupported action. | Shows negative capability and appropriate method fit. | Immediate; do not optimize upward without context. |
| `record_invalidation_timeliness` | Time between a known invalidating change and downgrade or refresh of dependent decision records. | Measures whether durable claims stop being reused promptly. | Event-driven. |
| `reviewer_recovery_success` | Audited failures for which the record identifies the failed premise, dependent claims, and next evidence without reconstructing the entire session. | Tests selective rollback and handoff quality. | Review or incident time. |

A pre-action reversal is not necessarily failure: finding a configured runtime use before deletion is evidence that the feedback loop worked. A post-action reversal from the same missed class is more concerning. Metrics should distinguish prevention from escape.

**Feedback routing table**

| observed signal | likely stage | first investigation | possible durable action |
| --- | --- | --- | --- |
| Independent inventory finds relevant omitted files. | Inventory | Root, Git branch, ignore policy, extension filter, generated and nested inputs. | Fix inventory, add a coverage gate, or route that language or file class elsewhere. |
| Pointer bounds fail after a producer-stable run. | Retrieval or source freshness | Revision binding, generated files, path syntax, and pointer parser. | Improve manifest, regenerate pointers, or add a stale-range fixture. |
| Bounds resolve but semantic hit rate falls. | Extraction | Ctags/fallback branch, multiline constructs, duplicate names, and grammar support. | Improve extraction, expand context defaults, or use semantic indexing for affected constructs. |
| Internal-edge disagreements cluster around aliases. | Resolution | Project path configuration, re-exports, extension and index conventions. | Add tested resolver support or classify and route alias claims to native tools. |
| Unresolved count drops while false internal edges rise. | Resolution incentive | Aggressive resolver changes and classification policy. | Restore unresolved as a valid state and gate on sampled precision. |
| Graph-derived rankings reverse after full-row analysis. | Presentation | Edge cap, duplicates, rank metric, and summary projection. | Compute ranks from TSVs, disclose cap, and add a regression fixture. |
| Stronger checks repeatedly refute rough absence. | Observation-model boundary | Dynamic, generated, configuration, macro, or unsupported-language classes. | Make escalation mandatory or bypass rough mapping for that claim class. |
| Context grows but retained evidence does not. | Retrieval | Query specificity, rank rule, pointer expansion, and whole-file triggers. | Tighten query-first guidance and measure missed evidence as a counter-signal. |
| Another operator cannot reproduce a row. | Provenance | Producer hash, root, revision, working state, options, environment, and mixed artifacts. | Require decision-record identity fields and fresh output directories. |
| Downstream defects occur despite structurally green artifacts. | Gate overreach | Which structural pass was promoted into semantic certainty. | Rewrite pass language and add independent project verification. |

**Review cadence**

| event | review |
| --- | --- |
| Every generated-reference edit | Run the focused structural verifier, exact heading and expansion checks, packet uniqueness checks, and hygiene gates. |
| Builder or pointer-reader change | Replay contract fixtures, compare artifact schemas and branches, and invalidate producer-dependent metrics. |
| Optional-tool or environment change | Capture capability differences and avoid combining branch-dependent samples without stratification. |
| New language, framework, or repository class | Audit inventory and relation observation boundaries before extending prior baselines. |
| Consequential mismatch or escaped defect | Perform a causal review, update anti-patterns and routing, and add a fixture when the mechanism is reproducible. |
| Public API, documentation, or tool release relevant to a live decision | Refresh the primary external source only with authorization, version-match locally, and keep prior cohorts separate. |
| Periodic repeated-use review | Examine whether metrics changed decisions, whether fields are used, and whether the rough mapper should fix, reroute, or retire any claim class. |

**Good, bad, and sentinel interpretations**

Good: "Under the same producer and stratification, fallback pointer semantic hits improved after an extraction change, while internal-edge sample agreement and missed-consumer reviews did not worsen. Raw sample identifiers and counts are retained." This supports a local improvement claim within the cohort.

Bad: "The new mapper emits more edges and fewer unresolved rows, so accuracy increased." More edges can be false positives, and fewer unresolved rows can result from incorrect forced resolution.

Sentinel: One configuration-driven deletion regression can justify a mandatory escalation boundary even when there are too few events for a stable rate. Record it as a high-consequence counterexample, not as a percentage estimate.

**Feedback loop**

1. Capture an invariant failure, sampled mismatch, route outcome, or downstream event with complete identity.
2. Classify the earliest verified pipeline mechanism and the claims that depend on it.
3. Decide whether to fix implementation, improve documentation, add a gate, reroute a claim class, retire a workflow, or gather a better sample.
4. Replay controlled fixtures and a representative target sample under the new producer.
5. Start a new comparable series only when definitions and conditions permit; preserve the old cohort for historical interpretation.
6. Confirm that the change improved decision quality without degrading its counter-metric.

The most important feedback outcome may be an earlier stop. If recurring evidence shows that runtime-only or security absence claims cannot be served safely by rough mapping, success is not a higher edge count. Success is routing those claims to the right evidence system before weak output reaches a decision.

## Completeness Checklist

Use this checklist as a set of revisitable phase gates, not a one-pass form. Every completed item must point to evidence. A conditional item needs a recorded reason for not applying. A critical failure blocks all dependent claims even if later boxes were previously marked complete.

Status has three distinct meanings:

| status type | meaning | valid evidence |
| --- | --- | --- |
| Machine pass | Deterministic structure, identity, schema, count, hash, syntax, or format contract passed. | Captured command or parser result. |
| Reviewer pass | A person verified claim-to-evidence fit, counterarguments, scope, and interpretation. | Review record with source pointers and rationale. |
| Authorized acceptance | The project owner accepted the bounded decision and remaining risk under applicable policy. | Approval mechanism defined by the project. |

A machine pass never implies reviewer or owner acceptance.

**Gate A: reference-construction completeness**

The following seven rows preserve and strengthen the seed checklist.

| requirement | completion evidence | severity if missing |
| --- | --- | --- |
| The role scenario names the user, starting state, decision, and trigger for Dependency Map Cli Patterns. | Section 010 contains an explicit role, compound request, branch-specific decisions, observation boundary, route change, and handoff. | Stop reference completion because the guidance lacks an operational user journey. |
| The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong. | Section 011 preserves all four postures and connects each to concrete production, retrieval, and verification tradeoffs. | Stop reference completion because method fit and error consequence are underspecified. |
| The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning. | Section 012 preserves seed roles, hashes duplicate content, defines typed authority, and records the unexplained canonical-versus-legacy metadata. | Stop source-backed claims until authority and uncertainty are visible. |
| The theme specific artifact is concrete enough to review without reading every mapped source. | Section 013 defines a decision-record schema with producer, coverage, evidence, claim, mismatch, verification, decision, and invalidation blocks. | Stop durable handoff; navigation may continue with a current pointer. |
| The examples cover good, bad, and borderline usage. | Section 014 provides six orthogonal examples plus good, bad, and recoverable synthesis. | Warn for concise expert notes; stop training/reference completion if boundaries remain abstract. |
| The metrics section names one leading indicator and one failure signal. | Section 015 defines deterministic gates, sampled leading indicators, delayed failures, denominators, counter-metrics, and feedback actions without claiming measured values. | Stop metric claims; the workflow can continue without a measurement program. |
| The adjacent routing section points to a better reference when this one is not the right fit. | Section 017 must route by unresolved question and stronger observation model, including terminal escalation. | Stop claims outside rough-map fit until a suitable route is named. |

Additional reference requirements:

| requirement | verification | severity |
| --- | --- | --- |
| All 26 original level-two headings remain exact and ordered. | Parse reference and compare heading texts with the archive seed. | Critical structural stop. |
| Every evolved section is strictly longer than its matching seed section. | Compare parsed section character lengths. | Critical evolution stop. |
| The packet contains 26 exact section headings and 260 exact question headings. | Parse packet and compare each ten-question cycle with the specification. | Critical rationale stop. |
| The packet contains 1,560 mandatory values with raw and prefix-stripped normalized uniqueness. | Parse the six required fields under every question and normalize with the focused test helper. | Critical quality stop. |
| All factual source and implementation claims preserve evidence boundaries. | Review hashes, script literals, no-browse labels, and illustrative examples. | Stop unsupported claims; narrow or correct them. |
| No unrelated shared file or lane was changed. | Review scoped status and diff paths. | Critical ownership stop. |
| Output is ASCII, table-consistent, fence-balanced, tab-free, trailing-whitespace-free, marker-free, and final-newline-terminated. | Run focused hygiene parser. | Correct before final handoff. |

**Gate B: method fit before artifact production**

| check | completion evidence | profile | response if failed |
| --- | --- | --- | --- |
| The user's actual decision is stated separately from the surface query. | Claim card with action, false-positive cost, false-negative cost, and reversibility. | All profiles. | Clarify before choosing tools. |
| Repository and directory instructions were read. | Paths and relevant requirements recorded. | All profiles. | Stop; native tools and write boundaries may override this guide. |
| Native search, semantic, build, ownership, and runtime tools were considered. | Route-selection rationale. | Standard and high assurance; abbreviated for navigation. | Use the stronger native route if it answers the claim directly. |
| Rough mapping can observe the relevant source and relation classes. | Fit statement covering extensions, tracked policy, configuration, generation, dynamic behavior, and semantic need. | All profiles. | Skip or use as auxiliary discovery only. |
| Writing artifacts is authorized at the chosen output location. | Explicit scope or user/project authorization. | Every fresh build. | Do not run the builder. |
| Existing artifacts were considered before rebuilding. | Reuse eligibility or rejection record. | Standard and high assurance. | Reuse only with complete compatible provenance. |
| Stop and escalation conditions are known before production. | Named evidence threshold and route-away triggers. | All profiles. | Define them so a successful command cannot become automatic approval. |

Method-fit failure can be a complete and correct outcome: the claim is routed to a semantic, build, configuration, security, or runtime evidence system.

**Gate C: producer and target identity**

| check | completion evidence | prerequisite | severity |
| --- | --- | --- | --- |
| Builder and pointer reader are readable, syntax-valid, and hash-bound. | Paths, SHA-256 values, `bash -n` results. | Authorized build or durable pointer evidence. | Critical for reproducible use. |
| Target root and repository identity are unambiguous. | Canonical path, top-level result, revision, workspace identity. | Every map or reused artifact. | Critical; wrong-root output is irrelevant. |
| Working-tree and generated state are captured. | Status and material local-input note. | Standard and high assurance. | Critical when local state can alter evidence; warning for navigation. |
| Invocation, options, output directory, and timestamps are retained. | Exact command and run manifest. | Fresh build. | Critical for cross-run reuse. |
| Required and optional capabilities are distinguished. | Shell, Python, `rg`, Ctags JSON probe, ast-grep availability, Graphviz availability. | Fresh build and cross-run comparison. | Record fallback or stop when a required capability is absent. |
| Output directory is fresh and authorized. | Pre-run nonexistence and post-run manifest. | Fresh build. | Critical against artifact mixing or overwrite. |

**Gate D: inventory and artifact contract**

| check | completion evidence | what a pass does not prove | severity |
| --- | --- | --- | --- |
| `all_files.txt` matches the implemented inventory branch. | Independent sorted comparison. | That tracked-only or `rg --files` policy fits the question. | Critical for interpreting all downstream rows. |
| `code_files.txt` and `files.tsv` paths reconcile. | Structured TSV comparison and counts. | That supported extensions include every relevant source or configuration file. | Critical structural gate. |
| Excluded file and language classes are explicit. | Coverage ledger for untracked, ignored, generated, vendored, nested, unsupported, configuration, and data files. | That exclusions are harmless. | Critical when any class can affect the claim. |
| `tooling.tsv` records capability state and symbol artifacts reveal the actual producer. | Header, rows, captured preflight, `symbols.tsv` kind distribution, and `ctags.jsonl` presence. | That detected ast-grep was invoked or that Ctags/fallback rows are semantically correct. | Critical for span interpretation and comparisons. |
| Required artifacts exist and schemas match. | Structured parser over files, symbols, edges, tooling, summary, Mermaid, and DOT; conditional SVG check. | Accuracy, completeness, or semantic meaning. | Critical production contract. |
| Summary and graph projections reconcile with full rows and cap. | Full counts, projected counts, `MAX_GRAPH_EDGES`, optional render state. | That full TSV rows represent all program dependencies. | Stop graph-derived claims if inconsistent. |

An inventory defect reopens extraction, relation, ranking, and absence conclusions derived from that population. Do not patch only the visible summary.

**Gate E: query, pointer, and interpretation**

| check | completion evidence | profile | response if failed |
| --- | --- | --- | --- |
| The compact query and candidate-selection rule are retained. | Exact filter or rank, population, included and excluded rows. | Standard and high assurance; query note for navigation. | Reproduce or narrow selection before handoff. |
| Durable pointers resolve on the bound revision. | File existence, integer bounds, reader result. | All profiles. | Regenerate or disambiguate. |
| Pointer context is sufficient for the claim. | Expanded span or complete-file rationale. | All profiles. | Read wider context; one-line fallback is only an entry point. |
| Duplicate symbols and ambiguous identities are handled. | Qualified path, scope cues, semantic resolution when needed. | Standard and high assurance. | Keep candidate state or escalate. |
| Consequential positive edges are sampled in source. | Endpoint reads and project-aware corroboration. | Standard and high assurance. | Downgrade ranks and relation claims. |
| Suspicious absence or unresolved rows receive an independent check. | Search, configuration, semantic, build, or runtime result. | High assurance and any consequential absence. | Block absence, deletion, migration, or security claims. |
| Graph appearance is not used as sole architectural evidence. | Full-row analysis, cap disclosure, source samples. | Every graph-derived claim. | Recalculate from complete rows and narrow language. |

**Gate F: claim sufficiency and action**

| check | completion evidence | severity |
| --- | --- | --- |
| Each claim is typed as candidate, observed, corroborated, verified for scope, refuted, or unresolved. | Claim card with bounded text. | Critical for durable handoff. |
| Supporting evidence and counterevidence are linked separately. | Bidirectional evidence registry. | Critical; confirmation-only records are incomplete. |
| Evidence strength matches consequence and reversibility. | Sufficiency rule and tradeoff review. | Critical for code changes and authorization. |
| Absence claims use authoritative evidence beyond rough non-observation. | Semantic, build, configuration, generated-state, test, runtime, and owner evidence appropriate to scope. | Critical hard stop. |
| Conflicting sources are reconciled or remain explicitly unresolved. | Mismatch record and affected claims. | Stop dependent decisions. |
| Project-native build and test gates cover the implemented boundary. | Exact commands, configuration, outcomes, and limitations. | Critical for implementation completion. |
| Remaining uncertainty has an owner and cannot silently broaden the claim. | Owner, next mechanism, stop condition, and accepted scope. | Critical for handoff. |

**Gate G: decision-record and handoff quality**

| check | completion evidence |
| --- | --- |
| Record profile matches the action. | Navigation, standard, or high-assurance rationale. |
| Producer, target, environment, and artifact identities are reconstructable. | Decision-record Blocks A through C. |
| Every evidence item supports, refutes, or contextualizes a claim. | Bidirectional links. |
| Every claim names consequence, owner, sufficiency, and invalidation. | Complete claim cards. |
| Every mismatch identifies the earliest verified stage and dependent claims. | Mismatch ledger. |
| Verification passes state what they leave unproven. | Gate limitation field. |
| Decision result and implementation boundary are explicit. | Proceed, proceed within scope, redesign, reject, or escalation required. |
| Rollback or recovery identifies what to inspect if the premise fails. | Recovery field and source dependency links. |
| Next action and stop condition are nonempty. | Executable next step with owner. |
| Sensitive repository or runtime data follows handling policy. | Redaction and storage review. |

**Gate H: final evolution and whole-file quality**

Before declaring this evolved reference complete:

1. Confirm packet section count `26`, question count `260`, field count `1,560`, raw unique count `1,560`, and prefix-stripped normalized unique count `1,560`.
2. Confirm the reference retains exactly the 26 original headings in order and each parsed section is longer than its seed counterpart.
3. Run the focused reference verifier and all shared structural tests that do not require modifying another lane.
4. Confirm local source hashes and frozen span anchors remain unchanged where the assignment expects immutability.
5. Scan both outputs for forbidden markers, non-ASCII characters, malformed tables, unbalanced fences, tabs, trailing whitespace, and missing final newline.
6. Reread the complete packet and reference in slices of at most five sections, persisting a review checkpoint after every slice.
7. Record Green after complete file and packet production, then Refactor after whole-file reread and final focused verification.
8. Report exact changed paths, counts, current test evidence, blockers, and the next assigned file without opening it early.

**Quality contrasts**

Good: The standard profile links a map run to reconciled coverage, source samples, counterevidence, project checks, and a bounded refactor decision. A dynamic deletion subclaim fails its hard gate and routes elsewhere while the review branch proceeds.

Bad: Every section exists, the summary is nonempty, and all boxes are marked, but producer identity, unsupported configuration files, counterevidence, and semantic checks are absent. This is document completeness without decision completeness.

Recoverable navigation: A current direct pointer and source read answer a location question under the lightweight profile. If that evidence later enters a refactor or deletion review, the stronger profile gates must be run; the old completion status cannot be promoted automatically.

The checklist is a prerequisite graph. Completion propagates forward only when supporting premises pass. Contradiction propagates backward to reopen the earliest false premise and every dependent conclusion. This selective invalidation is more useful than clearing every status, but it requires explicit dependency links and an honest unresolved state.

## Adjacent Reference Routing

Use dependency, debugging, timeline, system-design, map, and CLI references when the inquiry narrows, but route by missing observation capability rather than topic resemblance. The destination must be able to falsify the unresolved claim with a materially different evidence source. A second lexical graph does not independently verify a runtime-only absence claim.

This section identifies route classes and candidate local capabilities. Verify current availability, instructions, version, repository fit, and permissions when selecting a route. Later Delta assignments are not used as evidence here and remain unopened until their authorized sequence begins.

**Capability-gap router**

| unresolved question | rough-map boundary | primary route class | candidate local or project capability | evidence expected on return |
| --- | --- | --- | --- | --- |
| Where is an exact string, error, file, or named declaration? | A new broad map is unnecessary for a narrow location query. | Direct lexical search and source reading. | `rg`, repository-native search, or existing code index. | Current revision-bound path and source span with duplicate matches resolved. |
| Which syntax-shaped constructs match a pattern? | Regex or import extraction may be noisy or unable to express nesting. | Structural search or parser-aware query. | Installed ast-grep when selected deliberately, Tree-sitter-based tooling, or a project parser. | Rule identity, positive and negative examples, matches, parse limitations, and direct source review. |
| Which references or calls resolve to this symbol? | Lexical names and file heuristics do not establish semantic identity. | Language server, compiler, or precise semantic index. | Project IDE/index commands, LSP capability, language-specific analyzer. | Server/tool version, indexing scope, resolved identities, representative source confirmation, and missing variants. |
| What is the file/module dependency neighborhood or blast radius? | Rough rows are candidate edges with finite inventory and resolver limits. | More precise code graph plus source verification. | `clarity202606`, `run-parseltongue-1-7-2`, `codebase-memory-evidence-reader`, `codegraphcontext-evidence-reader`, or a repository-native graph when available and appropriate. | Producer and repository identity, traversal semantics, depth or budget, selected paths, contradictions with rough artifacts, and source evidence. |
| Which configured targets, packages, or generated units compose the build? | Lexical imports omit build-system and generation semantics. | Compiler or build graph. | Cargo, Gradle, Bazel, TypeScript project references, package tooling, or project-specific build query. | Target and feature configuration, generated inputs, dependency output, and variant boundary. |
| Is a component executed or registered at runtime? | Static map cannot observe reflection, data-driven dispatch, dynamic loading, or unexercised configuration. | Runtime tracing, integration probes, and configuration audit. | Project observability, startup diagnostics, test harness, logs, traces, or safely instrumented execution. | Workload and configuration identity, observed path, negative coverage limits, and link back to source. |
| Why is a failure occurring? | A dependency sketch identifies candidates but does not perform disciplined causal diagnosis. | Systematic debugging. | `systematic-debugging` or `matt-engineering-diagnose` when available and applicable. | Reproduction, minimized case, hypotheses, instrumentation, verified cause, fix, and regression evidence. |
| When and why did this architecture or relation change? | Current map has no historical intent or conversation context. | Repository history and decision archaeology. | Git history, issue/PR context, `capture-github-repo-context` when repository and access permit. | Commit/PR/issue identities, dated rationale, source changes, and separation of recorded fact from inference. |
| What should the change guarantee? | A graph does not define acceptance criteria, contracts, or authorization. | Executable specification and test planning. | `executable-specs-01`, repository requirement templates, or domain policy. | Bounded requirements, preconditions, postconditions, failure behavior, verification, and traceability. |
| How should a language-specific implementation be changed safely? | Generic map guidance does not encode language ownership, concurrency, type, framework, or runtime idioms. | Language- and framework-specific implementation guidance. | Applicable Rust, TypeScript, React, Java/Spring, Kotlin, Tauri, or other project-native references and tests. | Language-aware design, compiler/type checks, behavioral tests, and compatibility boundaries. |
| Does a security path, permission, or authorization boundary hold? | Rough static edges are not a security proof and omit configuration and runtime paths. | Security-specific threat, static, configuration, test, and runtime analysis with owner review. | Project security tooling and qualified domain guidance. | Threat scope, variants, attack paths, negative tests, residual risk, and authorized acceptance. |
| Does a performance or scale claim hold? | Edge count and rough workload estimates do not establish latency, memory, throughput, or scaling. | Benchmarking, profiling, load testing, and production telemetry. | Repository benchmark harness and observability stack. | Workload, environment, sample size, variance, baseline, raw results, and applicability limits. |
| What does a public tool or protocol currently support? | Local retained links are unrefreshed and installed behavior can differ by version. | Authorized primary-source refresh plus local capability reproduction. | Versioned official documentation and installed `--help` or probe. | Retrieval date/version, narrow paraphrase, installed version match, local example, and target applicability. |
| Who owns the decision or accepts residual risk? | Graph centrality cannot assign organizational authority. | Ownership metadata and human escalation. | CODEOWNERS-like files, service catalog, issue owner, technical lead, security or domain owner. | Named accountable owner, decision scope, accepted risk, and review state. |

Candidate capability names above are route examples, not claims that a particular binary, server, index, connector, or credential is ready in the current repository. Read the selected capability's instructions and probe it only when the route is needed.

**Preserved broad adjacent categories**

| seed category | route when | do not route when |
| --- | --- | --- |
| Dependency adjacent reference | The question needs more precise callers, callees, module relationships, cycles, or blast radius than the rough mapper provides. | The user only needs one exact source location. |
| Map adjacent reference | A different graph representation or persistent index has a materially stronger observation model. | The alternative merely redraws the same lexical rows. |
| CLI adjacent reference | The question concerns shell safety, command composition, portability, output contracts, or operational packaging of the mapper. | The unresolved issue is target-code semantics rather than command behavior. |
| Debugging adjacent reference | There is a reproducible failure, mismatch, or regression requiring causal diagnosis. | The task is only first-contact orientation with no observed defect. |
| Timeline or history reference | Current structure cannot explain why a boundary exists or when a relation changed. | The decision can be settled entirely from present source and tests. |
| System-design or specification reference | The task pivots from observing current dependencies to choosing desired boundaries and acceptance criteria. | The user has not yet established the current problem shape or decision consequence. |

**Route-entry contract**

Before handing off, record:

| field | required content |
| --- | --- |
| Original decision | The user's bounded action or explanation, not only the latest tool error. |
| Unresolved claim | One falsifiable statement or question and its evidence class. |
| Consequence | False-positive and false-negative cost, reversibility, and deadline if material. |
| Evidence already collected | Producer identities, artifact rows, source spans, project results, and current confidence state. |
| Earliest verified gap | Inventory, extraction, resolution, presentation, retrieval, semantics, build, configuration, runtime, history, policy, or authorization. |
| Current method boundary | Why the rough map cannot settle the claim or why another method is cheaper and stronger. |
| Destination requirement | The observation capability needed, not merely a preferred product name. |
| Expected return | Evidence form that can support, refute, or safely assign the claim. |
| Stop condition | When to return, proceed, reject, or escalate rather than continuing to collect context. |
| Sensitive-data boundary | What source, runtime, credential, or customer data may not be transferred. |

This packet prevents the destination from repeating broad orientation or losing the original decision consequence.

**Route-return contract**

The destination should return:

1. Tool or reference identity, version, configuration, repository state, and observation scope.
2. Exact claim addressed and whether the method has a materially different blind spot.
3. Reproducible observations with source, artifact, query, trace, test, or history locators.
4. Agreement and contradiction with prior rough-map evidence.
5. A bounded result of supported, refuted, unresolved, or escalation required.
6. Remaining variants, workload limits, and invalidation triggers.
7. The next state of the original decision record and every dependent claim that must reopen.

**Primary and secondary routes**

Some gaps need complementary routes:

| gap | primary route | secondary route | reason for combination |
| --- | --- | --- | --- |
| Alias or re-export miss | Project-aware semantic or build resolution. | Direct configuration and endpoint source. | Semantic result establishes identity; configuration explains why rough resolution failed. |
| Generated dependency | Build or generation graph. | Generated output inspection and tests. | Producer relationship and emitted behavior need separate evidence. |
| Dynamic registration | Configuration and runtime probe. | Static source and semantic references. | Runtime proves exercised use; static evidence bounds implementation and migration candidates. |
| Suspected unused component | Authoritative semantic/build/configuration search. | Runtime workload and owner review. | Static absence and runtime non-observation have different blind spots. |
| Architecture redesign | Current graph and source analysis. | Executable specification and ownership review. | Descriptive structure does not define the desired contract or approval. |
| Dependency-caused incident | Systematic diagnosis. | History and graph traversal. | Reproduction and instrumentation establish cause; history and topology explain introduction and scope. |

Do not add secondary routes merely to increase citation count. Add them when their observation models can fail differently in a way that matters to the action.

**Good, bad, and conditional routes**

Good: An unresolved `@core/*` family is handed to the project-aware resolver with the exact rows, target revision, and alias hypothesis. The return shows an internal configured path, direct source corroborates it, and external-dependency counts are revised.

Bad: An empty rough caller query is handed to a second regex search. Both find nothing, and the component is declared unused. Agreement between correlated lexical methods cannot establish absence.

Conditional: A second lexical search can still be valuable if it finds a direct counterexample. Weak tools often refute universal claims cheaply even when they cannot verify them positively.

**Loop detection and terminal routes**

Stop routing and escalate to an owner when:

- the same claim returns twice without new evidence or a narrower boundary;
- destinations share the same material blind spot and no independent mechanism is available;
- required access, authorization, credentials, runtime data, or project state is unavailable;
- evidence conflicts in a way that changes a consequential decision and no qualified resolver is available;
- policy, risk acceptance, or ownership rather than technical observation is the unresolved question;
- the cost or deadline requires a deliberate bounded decision under uncertainty.

Terminal escalation is not an empty handoff. Preserve the claim, evidence, contradictions, unavailable capability, consequence, and exact decision the owner must make.

**Route verification**

A route succeeds when the destination:

- consumed the stated capability gap rather than restarting generic discovery;
- used a method capable of observing something the prior route could not;
- returned reproducible evidence with identity and scope;
- reduced, reclassified, refuted, or safely assigned the uncertainty;
- updated the original decision rather than creating an isolated conclusion;
- avoided transferring sensitive data outside its policy boundary.

If none of these changed, the route added activity rather than information. Record that outcome and reconsider the problem formulation or terminal owner instead of opening another adjacent reference reflexively.

Adjacent routing is therefore an evidence graph. Its edges mean "this claim lacks this observation capability," and its returns mean "this new evidence changes this decision state." That precision allows specialized references and tools to remain modular without fragmenting the user's reasoning across disconnected workflows.

## Workload Model

`combined_evidence_inference_note`: Treat Dependency Map Cli Patterns as a repository operation with batch scans, filesystem writes, bounded projections, and evidence side effects, not as a prose summary.

The seed's `up to 500 changed files` boundary is not retained as an operational limit. No local benchmark, workload definition, environment, or failure threshold supports that number, and changed-file count is not the builder's primary input. The script scans the selected repository inventory, which can include many unchanged files. Capacity must be calibrated from actual source population, relation volume, filesystem, environment, query reuse, and evidence requirements.

**Workload variables**

| symbol | workload dimension | why it matters |
| --- | --- | --- |
| `F` | Paths in `all_files.txt`. | Inventory writing, path filtering, and raw coverage review scale with this population and total path text. |
| `C` | Supported code paths in `code_files.txt`. | File line counting, symbol extraction, relation scanning, and code-set memory scale with supported files. |
| `B` | Total bytes or lines across supported readable source. | Multiple stages read source content, so large files and filesystem throughput can dominate even when `C` is modest. |
| `S` | Rows in `symbols.tsv`. | Pointer storage, query cost, duplicate-name review, and sample size grow with extracted symbols. |
| `R` | Rows in `import_edges.tsv`. | Resolution work, internal and unresolved row memory, artifact size, and sampling population grow with lexical references. |
| `E` | Unique source-target pairs selected from resolved or fallback unresolved rows. | Frequency counting and graph candidate population grow with unique pairs. |
| `G` | `MAX_GRAPH_EDGES`. | Bounds Mermaid and DOT presentation work and optional SVG complexity, but does not bound full TSV extraction. |
| `Q` | Number and diversity of questions reusing one artifact set. | Determines whether batch production cost is amortized or repeated output becomes waste. |
| `V` | Number of repository, feature, platform, or configuration variants relevant to the decision. | Rough static output may need separate authoritative checks even if the batch map is produced once. |

Source count alone is insufficient. A repository with few very large generated files can be more expensive than one with many small files. A repository with modest source but dense lexical imports can produce large relation artifacts. A quick SVG cap can hide presentation cost without reducing the source and relation scans that precede it.

**Implemented stage model**

| stage | implementation behavior | primary growth driver | memory and I/O behavior | evidence output |
| --- | --- | --- | --- | --- |
| Root and output setup | Resolves absolute root, creates output directory, and reads `MAX_GRAPH_EDGES`. | Path and filesystem state. | Writes into the named directory and does not require it to be empty. | Producer and location context must be captured externally. |
| Raw inventory | Uses `git ls-files` inside a Git worktree; otherwise uses `rg --files`. | `F`, repository metadata, ignore policy, filesystem. | Streams path list to `all_files.txt`. | Raw selected population, not proof that policy fits the decision. |
| Code filter | Filters path text to `.rs`, `.py`, `.js`, `.jsx`, `.ts`, `.tsx`, `.go`, `.java`, `.c`, `.cc`, `.cpp`, `.h`, and `.hpp`. | `F` and total path characters. | Reads raw list and writes `code_files.txt`; exits if no supported source remains. | Finite supported code population. |
| Line counting | Python opens every selected code path and counts lines, replacing read errors with line count zero. | `C` and `B`. | Sequential source reads; stores little beyond one file at a time and writes `files.tsv`. | Path and line-count rows, with zero requiring investigation. |
| Symbol extraction with Ctags | When the exact JSON probe succeeds, invokes Ctags over the code-file list and converts JSON rows into symbol TSV. | `C`, `B`, language parser behavior, `S`. | External process plus JSONL artifact and conversion; output size grows with symbols. | Richer candidate spans when line and end fields exist, not semantic references. |
| Symbol extraction fallback | Otherwise reads supported source line by line and applies fixed regex families, writing one-line ranges. | `B` times a small fixed pattern set by extension. | Sequential reads and streaming writes; repeated source scan after line counting. | Candidate declarations with `start_line == end_line` and `kind=regex`. |
| Lexical relation extraction | Python loads the code path set, rereads every selected source, applies fixed import/include patterns, and accumulates rows. | `C`, `B`, `R`. | Holds `code_set` and the complete relation row list in memory; performs another full source scan. | `import_edges.tsv`. |
| Local resolution | For each lexical row, tests a small fixed list of path candidates or language-specific transformations against the in-memory code set. | `R` and constant candidate branches. | Holds internal and unresolved row lists; set membership is cheap, but semantics remain heuristic. | `internal_file_edges.tsv` and `external_ref_edges.tsv`. |
| Graph projection | Counts source-target pair frequency, chooses up to `G` common pairs, and writes Mermaid and DOT. If no internal pairs exist, unresolved pairs supply the projection. | `R`, `E`, and `G`. | Holds pair counts and graph labels; output is capped even when TSVs are not. | `dependency_graph.mmd` and `dependency_graph.dot`. |
| Optional rendering | Calls Graphviz `dot` when detected and tolerates render failure. | `G`, graph shape, renderer version. | External process and optional SVG write. | `dependency_graph.svg` only when rendering succeeds. |
| Summary | Reads generated TSVs, counts rows and fan-in/fan-out, records tooling, and writes a Markdown overview. | `C`, `S`, `R`, artifact read throughput. | Re-reads artifacts and holds counters rather than full source. | `summary.md`, a projection of existing artifacts. |

The batch is sequential from the shell's perspective. It has no persistent database, incremental index, stage cache, transaction marker, lock, resume protocol, or built-in per-stage telemetry. Strict shell mode makes many failures loud, but an earlier failure can leave a partially populated output directory, and optional Graphviz failure is intentionally nonfatal. Consumers must verify a fresh complete artifact contract before reuse.

**Repeated-read implications**

Under fallback extraction, source can be opened for at least line counting, symbol scanning, and lexical relation scanning. Under Ctags, line counting and relation scanning still read source, while Ctags performs its own parse. Filesystem cache may make later reads cheaper, but remote mounts, cold caches, very large files, antivirus or indexing overhead, and concurrent repository activity can change the profile.

Do not derive an exact I/O multiplier without measuring the selected branch and environment. The important operational fact is that a fresh map is a multi-pass batch scan, not one streaming traversal.

**Workload modes**

| mode | operation | best fit | stop or switch signal |
| --- | --- | --- | --- |
| Reuse query | Validate an existing artifact set, filter TSVs, resolve pointers, and verify selected source. | Matching producer and target state with several focused questions. | Missing provenance, changed revision, incompatible coverage, or a claim outside the old observation contract. |
| Fresh orientation | Run one full batch map, audit coverage, then serve many compact queries. | Unfamiliar local repository with supported static structure and authorized writes. | Scan or memory cost is unacceptable, relevant sources are excluded, or reuse horizon is too short. |
| Comparison run | Build with controlled producer, option, or environment change and compare artifacts. | Evaluating extraction branches, resolver changes, or regression fixtures. | Inputs or cohort differ beyond the intended variable, making comparison uninterpretable. |
| Narrow component run | Select a smaller root or independently prepared scope, then record external boundaries. | A component-local navigation question with well-defined cross-boundary policy. | The decision needs consumers or relationships outside the scoped root. |
| High-assurance augmentation | Use rough output for candidates, then add semantic, build, configuration, test, and runtime evidence. | Refactor, migration, deletion, or security work where rough breadth is useful but insufficient. | No authoritative mechanism can cover the remaining risk; escalate to an owner. |
| Persistent-index route | Skip or supplement batch mapping with an incremental semantic or graph system. | High query volume, frequent changes, large source populations, or semantic traversal needs. | Index freshness, lifecycle cost, or unsupported languages outweigh amortization value. |

**Favorable workload signature**

- Source is local, readable text on a stable filesystem.
- Relevant files mostly use supported extensions and conventional static imports or includes.
- A full batch completes within the user's acceptable interactive or background window under measured conditions.
- `S`, `R`, and artifact sizes remain easy to query with structured CLI or Python tools.
- Several decisions reuse the same producer and repository state.
- Direct source and native verification are available for consequential claims.

**Unfavorable workload signature**

- Remote or high-latency filesystem makes repeated reads dominant.
- Very large monorepo or generated source population makes artifacts and memory expensive.
- Revision churn invalidates pointers before `Q` can amortize production.
- Unsupported languages, configuration files, macros, generation, reflection, or runtime registration dominate the decisive relationships.
- Complete semantic or variant analysis is required, making rough mapping only an extra batch before the real tool.
- Output cannot be written safely, isolated, or bound to a target state.

**Pressure signals and responses**

| observed pressure | do first | avoid | possible route |
| --- | --- | --- | --- |
| Inventory time dominates. | Measure Git or `rg --files` branch, nested scope, ignored policy, and filesystem. | Silently excluding directories to hit a desired duration. | Use a justified component scope or repository-native inventory/index. |
| Source scan time dominates. | Measure `B`, large-file distribution, branch, cache state, and filesystem. | Inferring capacity only from `C`. | Persistent index, structural tool, or focused search for narrow questions. |
| Symbol rows are noisy or huge. | Inspect extraction branch, duplicate classes, and actual query needs. | Loading all rows into model context. | Query by path or name, improve extractor, or use semantic identity. |
| Relation rows consume memory or disk. | Measure `R`, language clusters, duplicate rows, and query utility. | Lowering unresolved count through unsafe forced resolution. | Stream or incrementally process in a future implementation, or use a suitable index. |
| Graph rendering is slow. | Lower `G` only for presentation and analyze full TSVs separately. | Claiming the reduced graph is complete. | Skip SVG, retain Mermaid/DOT, or use a viewer on selected subgraphs. |
| Artifacts stale before reuse. | Measure revision churn and `Q`. | Rebuilding reflexively for narrow exact queries. | Direct search or incremental semantic index. |
| Narrow scope misses cross-boundary edges. | Record external interfaces and independently query parent or adjacent scopes. | Calling component output whole-repository blast radius. | Build graph or semantic traversal at the required boundary. |
| Semantic verification dominates total work. | Ask whether rough candidate ranking materially reduces that work. | Keeping the rough stage only because it is familiar. | Route directly to native semantic, build, or runtime evidence. |

**Measurement card**

Before making capacity or performance claims, record:

| category | measurements |
| --- | --- |
| Producer | Builder and reader hashes, command, `MAX_GRAPH_EDGES`, capability flags, `symbols.tsv` kind distribution, and `ctags.jsonl` state. |
| Target | Root, revision, working state, filesystem type or locality, language and extension distribution. |
| Population | `F`, `C`, `B`, `S`, `R`, internal rows, unresolved rows, `E`, and artifact bytes. |
| Environment | Machine resources, shell, Python, `rg`, Ctags, Graphviz, cache state, competing load. |
| Stages | Wall and CPU time where available, peak resident memory, read/write volume, exit state, and partial-output state. |
| Utility | `Q`, time to first relevant source, retained evidence, mismatch classes, and whether the map changed a decision. |
| Quality | Coverage reconciliation, pointer samples, relation samples, counterexamples, and authoritative project outcomes. |

Repeat under equivalent conditions before attributing a change to implementation. Separate cold and warm filesystem runs. Report distributions or repeated observations rather than one lucky duration when variance matters. Do not extrapolate from a small fixture to a heterogeneous monorepo without validation.

**Optimization impact ledger**

| optimization | likely benefit | evidence-contract impact |
| --- | --- | --- |
| Reuse valid artifacts | Avoids repeated batch scans. | Safe only while producer, target, environment-relevant branch, and claim scope remain compatible. |
| Narrow root | Reduces `F`, `C`, `B`, `S`, and `R`. | Changes inventory population and can erase cross-boundary relationships; all global claims must be narrowed. |
| Lower graph cap | Reduces projection and rendering size. | Does not change TSV evidence, but visible density and graph-derived conclusions must disclose the new cap. |
| Skip SVG | Removes external render cost and dependency. | No semantic loss; Mermaid and DOT text remain presentation sources. |
| Stream relation rows in a future producer | Could lower peak `R` memory. | Must preserve ordering, duplicate policy, counters, and exact artifact contract or start a new comparable cohort. |
| Cache parsed source or incremental index | Amortizes repeated scans and queries. | Introduces invalidation correctness, persistent state, versioning, and stale-index risks. |
| Parallelize independent scans | May reduce elapsed time on suitable hardware and filesystem. | Can increase I/O contention and nondeterminism; outputs and error aggregation need verification. |
| Replace lexical resolver with semantic analysis | Improves identity for supported languages. | Produces a different evidence product with version, index, configuration, and coverage requirements. |

**Good, bad, and conditional workload decisions**

Good: Validate one current artifact set and reuse it for several pointer-first questions, while measuring stage cost and preserving claim-specific escalation. The broad scan is amortized and semantic limits remain visible.

Bad: Rebuild before every named-symbol lookup, quote the seed's 500-file number as a capacity guarantee, and reduce the root silently when runtime grows. This spends more while weakening evidence.

Conditional: Run a narrow component map for a local ownership review when external interfaces are explicitly recorded and no whole-repository blast-radius claim is made. The same artifact is invalid for a global deletion decision.

Workload optimization and reliability are coupled. Scoping, caching, capping, parallelism, and extractor changes can alter input population, freshness, relation meaning, or only presentation. Classify the impact before claiming improvement. Faster output is valuable only when it preserves the evidence contract needed by the bounded decision.

## Reliability Target

**Reliability objective:** The workflow must produce reproducible rough evidence, make its observation limits visible, prevent unsupported promotion into consequential action, detect material mismatches before handoff where practical, contain invalidation to dependent claims, and preserve a clear recovery or escalation path.

This is not a promise that every symbol or relation is correct. The mapper is intentionally heuristic and cannot observe every semantic, configured, generated, or runtime relationship. Reliability comes from separating what the producer can guarantee from what must be sampled, verified, or accepted by an owner.

**Target types**

| target type | appropriate use | expression | evidence |
| --- | --- | --- | --- |
| Hard invariant | Deterministic structure, provenance, policy, and promotion rules. | All required instances satisfy the rule, or the dependent state fails. | Parser, command, complete enumeration, or decision-record audit. |
| Sampled indicator | Pointer quality, relation agreement, route usefulness, and other repository-dependent behavior. | Counts and locally calibrated trends under a documented sampling frame; no universal threshold. | Stratified samples, raw evidence, uncertainty, and independent comparison. |
| Sentinel event | Rare but severe counterexample such as unsafe deletion from a missed runtime path. | One verified event can trigger a boundary or gate review without becoming a percentage estimate. | Causal incident or fixture record. |
| Owner-accepted risk | Residual uncertainty that technology cannot or need not eliminate under the bounded action. | Explicit scope, owner, rationale, review date, and invalidation trigger. | Project authorization mechanism. |

Do not combine these types into one synthetic reliability score. A structural pass is certain within its parser contract; semantic relation quality is sampled; a severe counterexample may set policy; risk acceptance belongs to an accountable owner.

**Reconciled seed targets**

| reliability_target_name | evolved target | evidence_collection_method | boundary |
| --- | --- | --- | --- |
| `source_boundary_preservation` | Every material final recommendation identifies its evidence class and distinguishes current local fact, run observation, target-source fact, unrefreshed external pointer, inference, and unresolved uncertainty. Missing classification fails durable handoff. | Claim-to-source audit plus focused parser where fields are structured. | This is a hard documentation invariant, not a claim that all underlying evidence is correct. |
| `decision_accuracy_sample` | Review route decisions through a documented local task sample with raw counts, task classes, reviewer criteria, disagreements, and uncertainty. No universal `18 of 20` threshold is asserted. | Stratified downstream-task review, route-return records, and consequence-weighted mismatch analysis. | Results apply only to the sampled producer, repositories, tasks, reviewers, and period. |
| `unsupported_claim_rate` | No final production, security, latency, reliability, completeness, or deletion claim may survive without claim-appropriate evidence, explicit inference where relevant, and a verification or escalation route. | Complete review of high-consequence final claims and rejection tests for promotion gates. | A zero-tolerance policy can be enforced; it does not imply that reviewers detect every hidden unsupported premise. |
| `recovery_path_clarity` | Every avoid, contradiction, invalidation, and failure case names the failed premise, affected claims, rollback or containment, owner, next evidence system, and stop condition. | Decision-record and failure-mode audit. | Recovery clarity does not guarantee recovery succeeds under unavailable access or tooling. |

The seed's `100 percent`, `18 of 20`, `zero`, and `every` expressions mixed unlike properties. Exact completion remains appropriate for enumerated hard policies, such as required fields. The unexplained routing sample is removed as a target because its task population, reviewer criteria, and statistical interpretation were absent.

**Reliability objective tree**

| dimension | hard objective | sampled or contextual objective | failure response |
| --- | --- | --- | --- |
| Prevention | Do not run writes outside authorization; do not reuse artifacts without identity; do not authorize consequential absence from rough non-observation. | Track which fit checks prevent unsuitable map use. | Stop production or promotion; route to suitable evidence. |
| Producer integrity | Scripts parse; required capabilities exist; invocation, producer, target, options, and output state are captured. | Compare stage behavior and artifact stability after producer changes. | Reject partial or mixed output and preserve diagnostics. |
| Artifact integrity | Required names and schemas reconcile; inventory transformations match; graph caps and conditional SVG state are explicit. | Sample row-level correctness and detect stale or duplicated artifacts. | Rebuild or repair before interpretation. |
| Evidence boundary | Every material claim has a source class, scope, and uncertainty state. | Audit whether reviewers interpret labels consistently. | Narrow, relabel, or reject the claim. |
| Retrieval reliability | Every durable cited pointer resolves on the bound revision and ambiguous paths use a safe form. | Sample whether expanded spans identify intended constructs. | Regenerate pointer, expand context, or use semantic identity. |
| Relation interpretation | Lexical rows remain candidate evidence until corroborated; unresolved remains a valid state. | Stratify internal, unresolved, and suspicious missing-edge checks by risk class. | Reclassify mismatch and invalidate dependent ranks or claims. |
| Decision containment | Evidence profile must match action consequence; high-assurance claims cannot inherit navigation status. | Review route choice and pre-action reversals. | Block, downgrade, or seek owner acceptance. |
| Recovery | Every durable claim has invalidation and next-step semantics. | Audit whether another operator can identify the failed premise and recover without replaying all context. | Update record, route, fixture, or guidance. |
| Learning | Producer and guidance changes start a new versioned evidence trajectory. | Trend recurring mismatch classes and downstream outcomes without pooling incompatible cohorts. | Fix, document, reroute, retire, or expand with verified evidence. |

**Reliability profiles**

| profile | reliable outcome | required controls | prohibited promotion |
| --- | --- | --- | --- |
| Navigation | A current candidate pointer and source read answer a reversible location question. | Target identity, direct read, duplicate disambiguation, and stop reason. | Cannot become a consumer, blast-radius, absence, or safety claim without stronger gates. |
| Standard decision | Coverage-audited rough evidence and project checks support an explanation, review order, or reversible scoped change. | Full provenance, artifacts, samples, counterevidence, source, project checks, and invalidation. | Cannot authorize material absence, security, or exhaustive migration by default. |
| High assurance | Claim-specific semantic, build, configuration, generated-state, test, runtime, and owner evidence support the bounded consequential action. | Standard controls plus domain policy, variants, negative tests, residual-risk review, and recovery. | Rough graph or one green test cannot substitute for the required evidence set. |

Profile status is not transitive upward. Reusing a navigation artifact in a high-assurance review requires running the missing gates; adding a warning is not enough.

**Hard reliability invariants**

For durable standard and high-assurance use:

1. Every artifact set has reconstructable producer, target, environment-relevant branch, options, working state, and timestamp identity.
2. Every source population has explicit inclusion and exclusion policy, and consequential omitted classes block dependent completeness claims.
3. Every graph projection discloses its cap and links back to complete relation rows.
4. Every durable pointer is checked against the current bound revision before citation or edit.
5. Every material claim links supporting evidence, counterevidence, sufficiency rule, owner, and invalidation trigger.
6. Every rough absence result remains candidate evidence until a stronger observation model addresses the relevant false-negative classes.
7. Every verification pass states what it leaves unproven.
8. Every contradiction reopens the earliest false premise and dependent conclusions.
9. Every unavailable evidence path leads to explicit escalation rather than invented certainty.
10. Every action remains inside write, data, security, and ownership authorization.

Failure of an invariant is not compensated by a high sampled relation agreement rate.

**Locally calibrated indicators**

| indicator | purpose | required report | no-claim boundary |
| --- | --- | --- | --- |
| Pointer semantic hits | Detect extraction or stale-range problems. | Counts, stratification, producer, revision, exact mismatches. | Cannot estimate symbols never extracted. |
| Internal-edge agreement | Detect lexical false positives and configuration misses. | Sample rule, source and semantic checks, agreement classes. | Cannot establish complete recall. |
| Rough-absence counterexamples | Detect false-negative classes before action. | Consequential claims investigated, stronger evidence, mechanism. | Selection bias prevents universal probability claims. |
| Route-review agreement | Improve adopt, adapt, avoid, and adjacent-route decisions. | Task classes, reviewer rubric, disagreements, consequence. | Reviewer consensus is not program truth. |
| Reproduction success | Test provenance and command usability. | Record cohort, replay environment, exact divergence. | Reproducing the same producer does not validate semantic correctness. |
| Pre-action versus post-action reversals | Distinguish healthy detection from escaped evidence failure. | Claim, timing, consequence, root cause, affected gates. | Sparse events should remain events, not unstable percentages. |

Local target setting should begin only after the team has enough comparable observations to understand variance and sampling bias. The target must state which decision it protects and what happens when missed. This reference supplies no current baseline.

**Consumer reliability obligations**

The producer can write accurate metadata and still be used unreliably. Consumers must:

- inspect complete rows before graph projections;
- preserve candidate and unresolved states instead of forcing conclusions;
- read target source before explaining behavior;
- seek independent evidence for consequential relations and absences;
- reject stale or mixed artifacts;
- carry exclusions, branch differences, and counterevidence into summaries;
- avoid treating multiple outputs from the same lexical pipeline as independent corroboration;
- rerun invalidated gates after source, producer, environment, configuration, or workload change.

**Failure budget interpretation**

No numeric semantic-error budget is asserted. Reliability response follows error class and consequence:

| event | acceptable containment | required response |
| --- | --- | --- |
| Wrong candidate found during navigation | Source read detects mismatch before action. | Search another candidate; record systematic extraction issue if recurring. |
| False internal edge in review ranking | Sample or source check detects it before priority is finalized. | Recalculate affected ranks and inspect mismatch class. |
| Missing dynamic edge before deletion | Stronger configuration or runtime check detects it and blocks action. | Preserve as sentinel, strengthen mandatory escalation, add fixture when safe. |
| Unsupported claim reaches durable handoff | No acceptable containment. | Withdraw or narrow claim, audit promotion path, and repair gate. |
| Invalidated record remains in use | No acceptable durable state once invalidation is known. | Mark invalid, notify dependent owners, refresh or retire. |
| Optional SVG missing while TSVs are valid | Acceptable under recorded Graphviz absence. | Continue with text artifacts; do not classify as semantic failure. |

This consequence-aware approach avoids treating all mismatches equally while refusing to normalize severe escapes into an average rate.

**Verification ladder**

1. Run deterministic syntax, identity, schema, heading, field, uniqueness, and hygiene checks.
2. Exercise negative fixtures for inventory exclusions, fallback spans, aliases, graph caps, stale pointers, and dynamic registration.
3. Audit stratified target samples against direct source and an independent project-aware mechanism.
4. Review route decisions and claim promotions with explicit rubrics and dissent records.
5. Analyze pre-action catches, post-action reversals, and escaped defects causally.
6. Confirm that fixes improve the protected outcome without degrading a counter-metric or changing the product silently.

**Good, bad, and conditional target language**

Good hard target: "Every high-consequence final claim has claim-appropriate evidence and an escalation path; a missing field blocks handoff." The population is enumerable and the enforcement response is clear.

Bad empirical target: "At least 18 of 20 uses are correct, so routing is 90 percent reliable." Without task sampling, reviewer definition, uncertainty, and consequence, the fraction is unsupported and nonportable.

Conditionally valid report: "In this documented local sample, reviewers agreed on 18 routes and disagreed on 2." This may be useful raw evidence if the tasks, rubric, reviewers, disagreements, and no-generalization boundary are retained. It still does not become a universal guarantee.

Reliability decomposes into prevention, detection, containment, recovery, and learning. An approximate candidate can be operationally safe when source checks catch errors before action; a rare undetected absence error can be severe. For decision-support mapping, bounded error propagation and clear recovery can matter more than an uncalibrated average match rate.

## Failure Mode Table

Treat failure as a state transition. Identify the earliest verified stage, preserve diagnostics, reject artifacts whose integrity cannot be established, and invalidate every dependent claim. Continue only when the remaining artifacts are both structurally valid and sufficient for the narrowed claim.

| handling class | meaning | default action |
| --- | --- | --- |
| `fatal_production` | Required input, command, parse, or write contract failed; the run did not complete reliably. | Stop, retain diagnostics, and rebuild in a fresh authorized directory after correcting the cause. |
| `silent_degradation` | The run may finish but coverage or artifact content is weaker than appearance suggests. | Detect through invariants and samples, label the degradation, and block dependent claims. |
| `claim_blocking` | Artifacts can support some navigation but cannot support the pending semantic or consequential conclusion. | Preserve useful candidates, downgrade the claim, and route to stronger evidence. |
| `optional_output_loss` | A nonessential projection or convenience output failed while core tabular artifacts remain valid. | Record the loss and continue within the unaffected evidence contract. |
| `informational_difference` | Environment or branch differs but no contract has failed yet. | Capture the difference and avoid invalid cross-run comparisons. |

**Producer and artifact failures**

| failure_mode_name | class | likely_trigger_condition | observable_signal | required_mitigation_action | invalidated_or_preserved_evidence |
| --- | --- | --- | --- | --- | --- |
| source drift hides truth | claim_blocking | Local guidance, script, target source, configuration, or external documentation changes after a record was written. | Hash, revision, capability, artifact, or refreshed-source identity no longer matches. | Mark dependent claims stale, rerun only affected stages, and preserve the prior version as historical evidence. | Invalidates claims downstream of the changed source; unrelated historical facts remain. |
| generic advice escapes review | claim_blocking | Agent copies plausible best practices without theme-specific source and verification. | Recommendation has no evidence class, target boundary, falsification, or next gate. | Block durable completion until claim, source, inference, and verification are explicit. | Navigation ideas may remain hypotheses; no action authorization survives. |
| dirty tree loses intent | claim_blocking | Mutation begins before separating user changes, generated state, and map output. | Status lacks baseline or touched files mix unrelated owners and producers. | Capture state before production, isolate output, and attribute each changed path before edits. | Existing source observations may be ambiguous until state is reconstructed. |
| blast radius exceeds review | claim_blocking | Broad query or rewrite touches files outside the user's intended decision. | Changed-file or evidence set expands without a revised boundary. | Stop mutation, compare planned versus actual scope, and obtain authorization or split the task. | Preserve verified in-scope evidence; reopen cross-boundary claims. |
| target root does not resolve | fatal_production | Root path is missing, inaccessible, or not a directory. | Initial `cd` fails and the strict shell exits. | Correct and re-identify the root; do not reuse any directory from the failed attempt. | No target-map conclusion is valid. |
| wrong root maps successfully | silent_degradation | A valid but unintended directory is supplied. | Artifacts are internally valid yet repository identity, expected paths, or counts disagree. | Verify canonical root before build and compare manifest with user scope. | Entire artifact set is irrelevant to the intended target, even if technically correct. |
| required ripgrep missing | fatal_production | `rg` is absent from `PATH`. | Explicit error says ripgrep is required. | Install or expose an authorized `rg`, or choose another method; rerun preflight. | No run artifacts should be interpreted. |
| implicit Python requirement missing | fatal_production | `python3` is absent or incompatible. | A Python stage fails after early shell setup; the script's initial explicit check did not name Python. | Include Python in preflight, capture version, and rebuild fresh after correction. | Earlier inventory files may exist but the directory is partial and untrusted as a complete map. |
| output directory creation or write fails | fatal_production | Permission, invalid path, storage exhaustion, read-only mount, or quota prevents creation or writes. | `mkdir`, `cd`, redirection, or Python open fails. | Select an authorized writable fresh location and verify capacity. | Reject partial output; source repository remains unchanged unless another command wrote elsewhere. |
| existing output directory mixes runs | silent_degradation | The builder writes into a directory containing artifacts from an older producer or environment. | Required files are overwritten selectively while stale conditional files such as prior SVG or Ctags JSON can remain. | Require a new directory or a verified transactional cleanup owned by the operator; manifest every file. | Reject optional and mixed artifacts; rebuild before cross-file interpretation. |
| interrupted run leaves partial artifacts | fatal_production | Shell, Python, disk, signal, or user interruption stops between stages. | Some named files exist, but required set, schemas, timestamps, or summary are incomplete. | Treat completion marker as absent, preserve diagnostics, and rebuild fresh rather than resuming implicitly. | No complete-run claim survives; individually inspected raw files remain diagnostic only. |
| invalid graph cap fails late | fatal_production | `MAX_GRAPH_EDGES` is not parseable as an integer or is otherwise unsuitable for the Python logic. | Relation/projection Python exits after earlier inventory and symbol artifacts may already exist. | Validate option before production and rerun in a fresh directory. | Earlier artifacts are partial-run diagnostics; summary and graph conclusions are invalid. |
| no supported source remains | fatal_production | Filtered inventory contains none of the finite supported extensions. | Explicit `no supported source files` error. | Select a suitable language-aware tool or correct the root and coverage policy. | The rough builder is not the primary method for this target. |

**Inventory and source-read failures**

| failure_mode_name | class | likely_trigger_condition | observable_signal | required_mitigation_action | invalidated_or_preserved_evidence |
| --- | --- | --- | --- | --- | --- |
| tracked-only inventory omits live input | silent_degradation | Relevant untracked, ignored, generated, or nested content exists inside a Git worktree. | Independent build/input audit finds paths absent from `all_files.txt`. | State policy, include through an authorized alternative, or route to project-native analysis. | Invalidates completeness, rank, and absence claims affected by omitted content. |
| supported-extension filter erases a dependency authority | silent_degradation | Configuration, schemas, Kotlin, templates, generated manifests, or other relevant types are not in the fixed list. | Raw inventory includes the path but `code_files.txt` does not. | Add a separate analysis route or a tested producer change; retain exclusion in every claim. | Supported-source navigation can continue; cross-surface completeness cannot. |
| selected source disappears or cannot be read | silent_degradation | File is deleted, races with the run, has permission issues, or cannot be opened. | `files.tsv` can record line count zero; symbol and relation scans catch `OSError` and skip the file. | Investigate every zero count, freeze source state where possible, and rebuild. | All symbol, relation, and absence conclusions involving the skipped file or its consumers are invalid. |
| decoding replacement hides malformed text | silent_degradation | Source contains bytes invalid under UTF-8. | Readers use `errors="replace"`; extraction may see replacement characters without a fatal error. | Identify encoding, inspect affected files with project-appropriate tooling, and avoid claiming parser completeness. | Unaffected files remain candidates; affected-file syntax conclusions are weak. |
| repository changes during multi-pass scan | silent_degradation | Source mutates between line count, symbol extraction, relation scan, and summary. | Counts, pointers, or rows disagree with current source despite one run directory. | Run against a stable revision or detect state change before and after production. | Artifact consistency and all cross-stage comparisons are suspect. |

**Symbol extraction failures**

| failure_mode_name | class | likely_trigger_condition | observable_signal | required_mitigation_action | invalidated_or_preserved_evidence |
| --- | --- | --- | --- | --- | --- |
| Ctags unavailable or JSON probe fails | informational_difference | No Ctags command or exact JSON mode is unsupported. | `tooling.tsv` records `ctags=no`; regex `kind` rows appear. | Record fallback, sample pointer quality, and escalate for semantic identity when needed. | Navigation may continue; complete spans and semantic symbols are not implied. |
| Ctags probe passes but actual run yields nothing | silent_degradation | Actual Ctags invocation fails or emits an empty `ctags.jsonl` after the capability probe succeeded. | `tooling.tsv` says `ctags=yes`, while fallback `kind=regex` rows appear because an empty symbol file triggers fallback. | Determine actual producer from `symbols.tsv` kinds and `ctags.jsonl`, preserve diagnostics, and avoid calling capability the selected extractor. | Fallback candidates remain usable under their limits; Ctags-span claims are invalid. |
| malformed nonempty Ctags output blocks fallback | silent_degradation | `ctags.jsonl` is nonempty but records are invalid JSON or lack path/name fields. | Parser creates a header-only `symbols.tsv`; nonempty header prevents fallback. | Validate data-row count and JSON parse yield, then correct Ctags or force an explicit tested fallback in a future producer. | Relation artifacts may remain available; symbol and pointer discovery is incomplete. |
| legitimate header-only symbol table misclassified | informational_difference | Supported files contain no constructs matched by the active extractor. | `symbols.tsv` has only its header, source inventory is valid, and no parser error is found. | Compare expected constructs and use direct or structural search; do not label failure without an expectation. | File and relation artifacts can still be valid; symbol-based claims remain absent. |
| fallback range overstates definition coverage | claim_blocking | Regex extractor records declaration line as both start and end. | `kind=regex` and equal range values. | Treat pointer as entry point, expand context, and inspect full module when annotations or body matter. | Candidate identity may survive; body, size, and range-sensitive claims do not. |
| duplicate names collapse conceptual identity | claim_blocking | Same name occurs across scopes, overloads, tests, or files. | Grouped symbol query returns multiple path/range rows. | Keep path-qualified candidates and use language-aware identity when callers or ownership matter. | Name-only summaries and merged consumer claims are invalid. |

**Relation and projection failures**

| failure_mode_name | class | likely_trigger_condition | observable_signal | required_mitigation_action | invalidated_or_preserved_evidence |
| --- | --- | --- | --- | --- | --- |
| multiline or unsupported import form is missed | claim_blocking | Syntax does not match fixed line-oriented patterns. | Direct source or native analyzer finds a relation absent from `import_edges.tsv`. | Record mismatch class and use structural, semantic, build, or configuration evidence. | All affected recall and absence claims are invalid; observed rows remain observations. |
| lexical match is not a semantic dependency | claim_blocking | Type-only, conditional, commented-like, platform-specific, or otherwise nonbehavioral syntax matches. | Endpoint or project-aware review contradicts inferred meaning. | Preserve raw row, reclassify claim, and sample the mismatch family. | Raw extraction fact survives; behavior and rank interpretation may not. |
| internal alias remains unresolved | claim_blocking | Project alias, re-export, package, or framework convention is outside resolver rules. | Row appears in `external_ref_edges.tsv` but project configuration resolves internally. | Keep unresolved state until project-aware resolution; revise external classification and counts. | Raw reference survives; external-dependency claim is invalid. |
| unresolved row is forced external | silent_degradation | Consumer treats filename `external_ref_edges.tsv` as taxonomy. | External inventory lacks configuration check and clusters internal-looking aliases. | Rename concept in downstream prose to unresolved and verify each consequential family. | Artifact row remains; third-party and ownership conclusions are blocked. |
| no internal edges makes graph use unresolved pairs | silent_degradation | `internal_rows` is empty, so graph pair counts fall back to unresolved source-target references. | Mermaid and DOT contain targets not present as internal files; summary internal count is zero. | Label graph as unresolved-reference projection, inspect complete external rows, and avoid architectural interpretation. | Raw unresolved navigation survives; internal topology and hub claims are invalid. |
| graph cap hides relations | claim_blocking | Unique pair population exceeds `MAX_GRAPH_EDGES`. | TSV counts exceed Mermaid/DOT edge counts. | Analyze complete rows, disclose cap, and treat graph as presentation only. | Full TSV evidence survives; visual completeness and visual centrality claims do not. |
| graph label syntax breaks projection | optional_output_loss | Paths or targets contain characters that are not safely escaped for Mermaid or DOT output. | Renderer or parser errors, malformed labels, or missing nodes despite valid TSV rows. | Use TSVs as authority, sanitize in a tested future producer, and validate projection. | Tabular artifacts remain; graph communication is invalid. |
| Graphviz rendering fails nonfatally | optional_output_loss | `dot` is detected but render command fails, or SVG cannot be written. | `tooling.tsv` can say `dot=yes` while current SVG is missing; the shell intentionally tolerates render failure. | Record render failure, verify DOT text, and reject any stale SVG from a reused directory. | TSV, Mermaid, DOT, and summary may remain valid after independent checks. |

**Pointer and consumer failures**

| failure_mode_name | class | likely_trigger_condition | observable_signal | required_mitigation_action | invalidated_or_preserved_evidence |
| --- | --- | --- | --- | --- | --- |
| stale pointer still resolves | silent_degradation | Lines move while old numeric bounds remain inside the file. | Reader exits successfully but displayed text no longer identifies the expected construct. | Bind revision, verify content identity, search qualified symbol, and regenerate. | Old pointer identity is invalid; current direct source can restore the observation. |
| out-of-range pointer yields no source lines | silent_degradation | Start and end exceed file length. | Reader prints pointer and window headers, `sed` returns success, but no numbered source lines follow. | Assert that output contains expected lines and validate bounds against current file length. | Exit status alone is invalid evidence; no source observation occurred. |
| colon-bearing path is parsed incorrectly | fatal_production for retrieval | Combined `file:start:end` form conflicts with colons in the path. | File lookup targets a truncated path or numeric fields are wrong. | Use separate file, start, and end arguments and test the exact path. | Combined pointer is invalid; artifact row may remain usable. |
| reversed range hides upstream defect | informational_difference | Producer or user supplies start greater than end. | Reader silently swaps bounds and displays content. | Record normalization and investigate whether producer range logic is wrong when repeated. | Local read can be usable; original range-order quality claim is not. |
| successful artifact shape becomes semantic approval | claim_blocking | Consumer treats schema, nonempty files, or green reference tests as proof of code behavior. | Final claim lacks source, project, or runtime evidence appropriate to consequence. | Downgrade, add independent verification, and audit promotion path. | Structural pass remains true; semantic conclusion is withdrawn. |
| observation-model gap triggers endless retries | claim_blocking | Dynamic, generated, security, or runtime claim is repeatedly sent through lexical mapping. | New runs produce no material evidence change. | Stop retrying, preserve the gap, and route to the capable system or owner. | Candidate discovery may remain; the pending consequential claim is unresolved. |

**Causal failure chains**

| chain | unsafe outcome | earliest break and recovery |
| --- | --- | --- |
| Existing directory -> stale SVG survives -> new run lacks `dot` -> reviewer opens old SVG | Architecture is interpreted from another producer or revision. | Require fresh directory and manifest; delete or archive only under owned policy, then rebuild. |
| Ctags probe succeeds -> actual output malformed -> header-only symbols -> no candidates | Repository appears to have no symbols. | Validate data-row and parse yield; inspect `ctags.jsonl`; use explicit fallback or another extractor. |
| File becomes unreadable -> line count zero and scans skip -> no inbound edge -> deletion | Live code disappears silently from the evidence population. | Investigate zero line counts and stabilize source before relation interpretation. |
| No internal resolutions -> graph falls back to unresolved pairs -> visual looks connected | Unresolved names are mistaken for internal topology. | Compare internal count and graph targets; label or reject projection for architecture claims. |
| Old pointer remains in bounds -> reader exits zero -> wrong helper is edited | Successful range read masks semantic staleness. | Verify expected construct identity and revision before editing. |
| Rough absence -> repeated lexical retries -> no new evidence -> owner pressure | Unsupported certainty accumulates through repetition. | Detect same-blind-spot loop and escalate to semantic, configuration, runtime, or owner evidence. |

**Failure-injection plan for a future authorized fixture**

| injected condition | expected observable state | required workflow transition |
| --- | --- | --- |
| Missing `rg` | Explicit early failure and no accepted map. | `fatal_production` -> correct environment or switch method. |
| Unsupported-only source tree | Explicit no-supported-source failure. | Route to another analyzer. |
| Nonempty malformed Ctags JSON | Header-only symbol data unless producer is improved. | Reject symbol completeness and record regression case. |
| Unreadable selected source | Zero line count or missing rows. | Coverage gate fails before relation use. |
| Alias plus actual external import | Both rough unresolved, project-aware check separates them. | Preserve unresolved state until classification. |
| More pairs than graph cap | Full TSV count exceeds projections. | Keep full-row authority and disclose cap. |
| Existing directory with old SVG, later run without `dot` | Stale SVG remains unless consumer rejects directory. | Manifest/freshness gate fails. |
| Pointer beyond file length | Reader returns headers without numbered source. | Content-presence gate fails despite exit zero. |
| Dynamic configuration registration | No rough internal edge, positive runtime/configuration evidence. | Absence claim refuted and routed. |

Current script reading establishes these mechanics; occurrence rates across operating systems, filesystems, Ctags builds, path conventions, and repositories are unmeasured. Classify severity by invisibility, affected claim, and consequence, then collect local incidence only under stable definitions.

The table's core invariant is that recovery changes a premise. A retry is justified only when environment, input, producer, option, or method changes in a way that addresses the verified cause. Unchanged repetition should trigger backpressure and escalation, which the next section defines.

## Retry Backpressure Guidance

Retry only after the failed signal has a verified or testable class and the next attempt changes a premise. A retry is a controlled experiment, not repetition. Name the changed environment, input, producer, option, state, authorization, or method; predict the intermediate signal that should differ; isolate the output; and stop when the same mechanism recurs without new information.

The builder itself has no retry, backoff, queue, lock, resume, or transaction protocol. These controls belong to the operator or surrounding orchestrator unless a future producer implements and verifies them.

**Retry state machine**

| state | entry evidence | permitted transition | prohibited action |
| --- | --- | --- | --- |
| `failure_observed` | Command error, invariant mismatch, empty or malformed content, contradiction, or unavailable evidence. | Preserve diagnostics and classify earliest stage. | Immediate blind rerun into the same directory. |
| `cause_classified` | Transient, environment, authorization, input, source stability, producer, option, artifact mixing, semantic gap, contradiction, or unknown class recorded. | Identify a changed premise and expected new signal, or route to terminal state. | Labeling every failure transient for convenience. |
| `retry_ready` | Corrective condition exists, output location is fresh and authorized, target state is captured, owner and stop condition are named. | Execute one bounded attempt and capture a new manifest. | Reusing partial output or discarding first diagnostics. |
| `retry_running` | Attempt identity, start state, resource owner, and cancellation boundary are recorded. | Complete, fail with a new signature, or fail with the same mechanism. | Concurrent writer entering the same artifact path. |
| `retry_succeeded` | Predicted intermediate gate changes and full artifact plus claim gates pass. | Compare attempts, retain causal conclusion, and resume bounded work. | Treating eventual exit zero as proof that the diagnosed cause was correct. |
| `new_failure_discovered` | Attempt progresses beyond the old stage but exposes a distinct mechanism. | Return to classification with the new evidence. | Charging a new mechanism against an unrelated retry rule without diagnosis. |
| `same_failure_repeated` | Same earliest mechanism recurs without material information gain. | Apply backpressure and route, redesign, wait, or escalate. | Another unchanged rerun. |
| `method_boundary_reached` | The claim requires evidence the rough mapper cannot observe. | Transfer the claim to semantic, build, configuration, runtime, security, history, or owner route. | Adding lexical retries or warnings as substitutes. |
| `authorization_blocked` | Required write, data, credential, or owner approval is unavailable. | Wait for explicit state change or answer within a narrower read-only boundary. | Circumventing ownership or permission controls. |
| `contradicted` | Positive evidence refutes the pending universal or absence claim. | Update decision, invalidate dependents, or define a separately authorized migration. | Retrying until the contradicting evidence disappears. |

Success requires both the predicted changed signal and all downstream gates relevant to the claim. If installing `rg` allows inventory to begin but Python then fails, the first diagnosis was valid and a new failure was discovered; the map is still incomplete.

**Failure-class guidance**

| failure class | retry eligibility | changed premise required | backpressure or terminal route |
| --- | --- | --- | --- |
| Missing required command | Eligible after authorized installation or `PATH` correction. | The exact capability probe now passes. | Switch method if installation is unavailable or prohibited. |
| Invalid root or output path | Eligible after path identity and authorization are corrected. | Canonical root and fresh writable output are verified. | Escalate scope or permission when ownership is unclear. |
| Storage or permission pressure | Eligible after capacity or permission state changes. | Fresh output can be created and written safely. | Wait, choose an authorized volume, or stop; do not overwrite valuable files. |
| Source changed during multi-pass run | Eligible after source state stabilizes or a frozen revision is selected. | Pre- and post-run identities match. | Use immutable checkout, project snapshot, or accept a narrower observation. |
| Existing directory contains mixed artifacts | Do not rerun in place. Rebuild as a new attempt. | New empty authorized directory and complete manifest. | Quarantine old directory as diagnostic evidence. |
| Ctags capability passes but actual output is empty or malformed | Not eligible unchanged. | Diagnose binary and invocation, correct producer, or deliberately select a tested fallback. | Use direct/structural/semantic route if symbol quality remains inadequate. |
| Optional Graphviz rendering fails | Core map need not retry when TSV, Mermaid, DOT, and summary gates pass. | If visual output is required, correct renderer or label issue and rerender from verified DOT. | Continue without SVG under an explicit optional-output state. |
| Unsupported source extension | Not retryable by the unchanged builder. | Producer gains tested support or a different analyzer is selected. | Route that source class elsewhere and narrow claims. |
| Alias or semantic resolution miss | Not solved by unchanged lexical rerun. | Project-aware configuration or semantic method is introduced. | Preserve unresolved state and route. |
| Dynamic or generated relationship gap | Not retryable within the same observation model. | Build, configuration, generation, or runtime evidence becomes available. | Terminal for rough-map verification. |
| Positive counterexample refutes absence | No retry of the original claim. | A new migration changes the system and has its own acceptance criteria. | Mark refuted and block deletion under current state. |
| Public documentation is stale | Refresh only when browsing is authorized and the current claim needs it. | Primary source is retrieved, version-matched, and locally reproduced. | After one scoped refresh that does not settle applicability, route to owner or narrower source. |
| Shared workspace owner is editing the path | Wait rather than retrying writes. | Owner releases boundary or coordinates an explicit handoff. | Do not overwrite, revert, or race another lane. |
| Unknown cause | One diagnostic attempt may be appropriate if it adds instrumentation rather than repeating output. | New observability is added and expected hypotheses are named. | Stop after no information gain and escalate diagnosis. |

The "one bounded retry" default is a reasoning safeguard for deterministic local work, not a universal distributed-systems parameter. When an external API, remote service, network filesystem, or job runner has an established retry policy, follow its idempotency, delay, jitter, deadline, and rate-limit semantics. Do not invent timing constants in this reference.

**Retry attempt record**

| field | required content |
| --- | --- |
| `attempt_identifier` | Unique identity linked to the original decision and prior attempt. |
| `failure_signature` | Earliest failed stage, exact observable signal, and affected artifact or claim. |
| `cause_class` | Verified cause or bounded hypotheses with distinguishing check. |
| `changed_premise` | Environment, input, producer, option, source state, authorization, scope, or method difference. |
| `expected_new_signal` | The first intermediate result that should change if the diagnosis is correct. |
| `target_identity` | Root, revision, working state, and relevant configuration. |
| `producer_identity` | Script hash, command, options, capabilities, and actual symbol-producer evidence. |
| `output_identity` | New authorized directory; never the prior partial or complete attempt path. |
| `resource_owner` | Agent or operator with exclusive write responsibility during the attempt. |
| `start_and_stop_condition` | When to launch, cancel, wait, route, or accept completion. |
| `result` | Predicted signal outcome, complete gates, new failure, repeated failure, or contradiction. |
| `claim_effect` | Claims resumed, narrowed, invalidated, refuted, or transferred. |

Retain enough diagnostics to explain divergence without preserving sensitive source or runtime data outside policy.

**Backpressure controls**

| pressure | control | release condition |
| --- | --- | --- |
| Red source-coverage gate | Stop graph interpretation and implementation derived from omitted classes. | Inventory is corrected or claims are narrowed and routed. |
| Red artifact-integrity gate | Stop query and handoff; reject partial or mixed directory. | Fresh complete run passes manifest and schema checks. |
| Red pointer-content gate | Stop citation and patching from the range. | Current source identity and expected construct are restored. |
| Red consequential-claim gate | Stop deletion, migration, security, or broad refactor authorization. | Claim-appropriate independent evidence and owner acceptance pass. |
| Repeated same failure | Open a circuit for that method and claim combination. | A materially new capability, producer, input, or authorization state is available. |
| CPU, memory, I/O, or storage pressure | Serialize, schedule, narrow with explicit boundary, or switch to an amortized index. | Resource budget and evidence contract are restored. |
| Shared output-path contention | Enforce one writer and unique attempt directories. | Current owner completes or hands off explicitly. |
| Context-window pressure | Persist packet, reference, decision record, and progress checkpoint before loading more context. | Durable state can reconstruct the exact next step. |
| Reviewer or owner capacity | Queue consequential decisions rather than auto-approving weak evidence. | Qualified reviewer accepts the bounded claim or requests more evidence. |
| External rate or service pressure | Use service-specific retry and deadline policy with idempotency. | Service recovers or terminal policy activates. |

Backpressure is not merely sleeping. It includes refusing new generation, limiting concurrency, isolating output, narrowing scope visibly, preserving context on disk, pausing promotion, and escalating authority.

**Long-running agent cadence**

- Persist each complete ten-question packet section before rewriting its reference section.
- Persist the matching evolved reference section immediately, then run an atomic sanity check.
- Record a lane checkpoint no later than every three completed sections and at Red, Green, and Refactor transitions.
- During full reread, persist review progress after at most five sections so an interruption does not erase review state.
- Re-read the current specification, exclusive paths, user updates, and progress journal before any broad rewrite or phase transition.
- Never commit, push, clean, revert, or modify a shared assignment surface unless explicitly authorized.
- Treat new user instructions as state changes that may invalidate the plan before the next write.

**Distributed execution rules**

1. Assign exactly one owner per generated file, packet, or theme batch.
2. Use unique output and attempt paths; never let two producers write the same artifact directory.
3. Preserve unrelated workspace changes and coordinate when another owner's edit affects the same decision.
4. Do not use retries to race an active owner or overwrite a newer artifact.
5. Require integration-time verification of exact paths, headings, evidence boundaries, producer identities, and normalized uniqueness where applicable.
6. Transfer blockers with the last verified state, repeated failure signature, attempted premise changes, and release condition.

**Examples**

Good local retry: Preflight fails because `rg` is missing. After an authorized installation, the exact probe succeeds. A new output directory is selected, inventory appears as predicted, and all downstream gates run. The changed capability explains progress.

Bad semantic retry: An empty rough inbound-edge query is rerun several times against unchanged source and producer, then treated as stronger absence evidence. No premise changed and the observation model still cannot see runtime registration.

Conditional source-stability retry: The first run spans a source update and produces pointer mismatches. The agent records both states, selects a stable revision, and rebuilds in a new directory. This is valid even though the script bytes are unchanged because the input-consistency premise changed.

Good no-retry decision: `dot` rendering fails, but complete TSV, Mermaid, DOT text, summary, and cap checks pass. SVG is optional for the user's source-navigation question, so the failure is recorded and work continues without consuming another full map attempt.

**Verification of retry and backpressure**

A future authorized fixture suite should establish that:

- correcting a missing command advances the predicted stage;
- unchanged deterministic reruns are blocked after repeated mechanism detection;
- every retry uses a fresh directory and preserves prior diagnostics;
- concurrent owners cannot claim the same output path;
- optional render failure does not invalidate complete tabular artifacts;
- unsupported and runtime-only claims transition to route states rather than retry loops;
- an out-of-range pointer's successful exit does not pass the content gate;
- source mutation between stages is detected or invalidates the run;
- a positive counterexample moves an absence claim to refuted, not retry-ready;
- progress checkpoints reconstruct the exact durable boundary after interruption.

Attempt history is an evidence trajectory. Recurring mechanisms should update failure fixtures, observability, routing, or producer design so future workers do not repeat no-information work. The history need not be verbose for trivial corrections, but durable or repeated failures should leave a concise sanitized record of what changed and why another attempt is or is not justified.

## Observability Checklist

Observability must make a map-derived decision reconstructable without turning the record into a source dump. Capture identities, boundaries, transitions, and bounded observations. Retain raw diagnostics only when reproduction, policy, and secure storage require them.

**What the current builder emits**

| emitted surface | observable fact | missing context that must come from wrapper or operator |
| --- | --- | --- |
| `all_files.txt` | Raw selected path population for the inventory branch. | Target revision, dirty state, command, producer hash, and whether the population fits the decision. |
| `code_files.txt` | Paths surviving the finite extension filter. | Relevant unsupported, configuration, generated, untracked, ignored, and runtime surfaces. |
| `files.tsv` | Selected paths and line counts, including possible zero on read failure. | Why a zero occurred and whether source changed during the run. |
| `symbols.tsv` | Symbol candidates, ranges, kind, and scope fields. | Whether rows came from usable Ctags output or fallback must be inferred from kind distribution and `ctags.jsonl`; semantic identity is absent. |
| `ctags.jsonl` when the capability branch runs | Raw Ctags command output, possibly empty or malformed. | Binary identity, actual invocation status, parse yield, and whether fallback later contributed. |
| Relation TSVs | Lexical import rows, resolved internal candidates, and unresolved references. | Semantic accuracy, alias configuration, complete recall, and runtime relationship meaning. |
| `tooling.tsv` | `rg` assumption plus Ctags JSON-probe, ast-grep availability, and `dot` availability flags. | Actual ast-grep contribution is always absent in this producer; Ctags capability does not prove actual symbol contribution; tool versions are not captured. |
| Mermaid and DOT | Up to the configured common source-target pairs. | Full relation population, cap value unless retained elsewhere, label validity, and semantic meaning. |
| Optional SVG | Graphviz rendering exists when detected execution succeeds. | A missing current SVG can reflect absent or failed rendering, and an old SVG can survive directory reuse. |
| `summary.md` | Counts, tooling flags, fan candidates, and pointer-first reminder. | Producer and target identity, stage duration, sample accuracy, decision rationale, and complete graph evidence. |

The builder does not emit a transactional completion marker, run identifier, artifact hash manifest, stage start/finish events, per-stage timing, peak memory, read/write volume, retry history, query history, claim state, or owner approval. A shell wrapper or decision record can add those without changing extraction semantics, but the wrapper then becomes part of the producer chain and needs its own identity.

**Minimum run envelope**

| field | required observation | reason |
| --- | --- | --- |
| `decision_identifier` | Stable link to the bounded user decision and claim cards. | Correlates static, source, project, runtime, and handoff evidence. |
| `attempt_identifier` | Unique value for every production or diagnostic attempt. | Prevents output and retry history from merging. |
| `producer_chain` | Wrapper, builder, pointer reader paths and hashes plus exact command and options. | Reconstructs implemented and orchestration behavior. |
| `target_identity` | Canonical root, repository/workspace identity, revision, branch when relevant, and working-state summary. | Binds every pointer and relation to source state. |
| `authorization_boundary` | Allowed read/write paths, sensitive-data constraints, commit/push boundary, and owner. | Prevents observability and artifacts from escaping scope. |
| `environment_identity` | Shell, Python, `rg`, Ctags probe and version where available, ast-grep availability, Graphviz state, filesystem locality, and relevant machine context. | Explains branch and performance differences. |
| `time_identity` | Start, finish, time zone, and clock source when comparisons matter. | Orders attempts and detects long source-change windows. |
| `output_identity` | Fresh authorized directory and ownership. | Rejects partial, mixed, or raced artifact sets. |
| `completion_state` | Complete, failed stage, cancelled, partial, contradicted, or route-away. | Exit code alone is not enough for optional and content-level failures. |

Capture branch and dirty-state information because they affect evidence identity, not because branch names inherently prove source content. Changed-file count is contextual; the builder scans selected repository inventory, not only the changed set.

**Stage-event checklist**

| stage | start observation | completion observation | critical anomaly |
| --- | --- | --- | --- |
| Preflight | Required paths, commands, capabilities, root, output authorization. | Exact probes and selected intended mode recorded. | Missing required tool, ambiguous root, or unauthorized output. |
| Inventory | Repository state and inventory branch. | `all_files.txt` count, hash or identity, independent reconciliation. | Omitted relevant class or source state changes. |
| Code filter | Supported extension policy. | `code_files.txt` and `files.tsv` path equality plus exclusion ledger. | Relevant language or dependency authority disappears. |
| Symbols | Ctags capability and expected constructs. | `ctags.jsonl` state, `symbols.tsv` row count and kind distribution, sampled pointers. | Capability/output divergence, header-only unexpected table, or stale ranges. |
| Relations | Source population and fixed parser families. | Import, internal, unresolved counts; sample and mismatch classes. | Empty internal set with unresolved graph fallback, alias cluster, or missing known relation. |
| Projection | Full pair count and `MAX_GRAPH_EDGES`. | Mermaid/DOT counts, label validation, optional SVG state. | Projection exceeds or contradicts cap, malformed labels, or stale optional output. |
| Summary | All input artifact identities. | Summary counts reconcile and fan lists are bounded as candidates. | Summary derived from mixed, partial, or mismatched artifacts. |
| Query and read | Exact question, filter, selected rows, pointer reader identity. | Current source observations and eliminated hypotheses. | No numbered source lines, wrong construct, duplicate identity, or irrelevant context growth. |
| Decision | Claim evidence, counterevidence, sufficiency rule, owner. | Supported, refuted, unresolved, or escalation state with next action. | Rough output promoted beyond profile or contradiction omitted. |

Stage events can be a compact table or structured event stream. They need not contain source bodies.

**Artifact manifest checklist**

For every attempt, retain:

- artifact filename and role;
- size and row count where meaningful;
- SHA-256 when durable comparison or handoff justifies it;
- created or observed timestamp;
- required, conditional, diagnostic, or derived status;
- schema version or expected header;
- producer and target identity link;
- missing or stale status with reason;
- privacy and retention class;
- downstream claims that reference the artifact.

Manifest checks should detect an old SVG or `ctags.jsonl` left by directory reuse, not merely confirm that expected required files exist.

**Coverage observability**

| question | retained evidence |
| --- | --- |
| Which local sources and instructions were loaded? | Exact paths, hashes when durable, and sections or roles used. |
| Which sources were intentionally skipped? | Path class, reason, consequence, and route if later needed. |
| Which repository files could enter the map? | Inventory branch, raw and filtered counts, independent comparison. |
| Which files could not contribute relations? | Unsupported extensions, read errors, untracked/ignored policy, generated and configuration surfaces. |
| Which observation classes are absent by design? | Semantic identity, dynamic dispatch, runtime registration, unexercised configurations, ownership authority. |
| Did coverage change during collection? | Pre/post revision and working-state check or frozen source identity. |

Absence of a file or edge from telemetry is not evidence that it does not exist in the program. Observability must name the observation population.

**Query and context observability**

Record:

| field | purpose |
| --- | --- |
| Original question | Prevents query activity from drifting away from the decision. |
| Artifact query | Makes candidate selection reproducible. |
| Population and rank | Shows whether selection came from complete rows or a capped view. |
| Selected and rejected candidates | Preserves useful negative evidence and detects confirmation bias. |
| Pointer and context width | Binds source observation and explains expansion. |
| Complete-file reason | Shows why pointer context was insufficient. |
| Context unit and retained-use classification | Supports future efficiency review without equating less context with better evidence. |
| Stop reason | Records when remaining uncertainty no longer changes the action or must route elsewhere. |

**Evidence and claim observability**

Every material claim should expose:

- claim identifier, bounded text, class, consequence, and profile;
- supporting and refuting evidence identifiers;
- source class and observation scope for each item;
- exact verification command, reviewer question, source span, rendered artifact, project check, or runtime trace used;
- contradictions and the earliest verified pipeline stage;
- promotion and downgrade events with actor and reason;
- owner, residual risk, invalidation trigger, next action, and stop condition.

A graph screenshot can be linked as a presentation artifact, but it cannot be recorded as the sole proof of semantic blast radius.

**Retry and backpressure observability**

| event | record |
| --- | --- |
| Failure | Stage, signature, diagnostics locator, affected artifacts and claims. |
| Classification | Transient, environment, input, producer, semantic gap, contradiction, authorization, or unknown. |
| Changed premise | Exact condition altered before retry. |
| Attempt | New output identity, resource owner, expected signal, start and stop conditions. |
| Repeated mechanism | Circuit-open or route decision and release condition. |
| Recovery | Causal comparison, resumed claims, and new invalidation rules. |
| No retry | Why another run cannot add information and which evidence system owns the claim. |

Record failures and contradictions, not only successful attempts. Otherwise feedback data systematically hides the cases that should change guidance.

**Timing and reviewer-effort measurements**

The seed requests p50, p95, and p99 latency or reviewer-time measurements. Percentiles are appropriate only when there are enough comparable observations and the tail statistic is stable for the decision. Do not publish percentile labels from a tiny or mixed sample merely because the names sound operational.

For timing claims, retain:

| field | requirement |
| --- | --- |
| Workload | `F`, `C`, `B`, `S`, `R`, `E`, `G`, query class, and verification profile as relevant. |
| Environment | Machine, filesystem, cache state, tool versions, load, and producer. |
| Sample | Count, inclusion, exclusions, failed/cancelled treatment, and raw observations or durable aggregate source. |
| Clock | Wall versus CPU time, start/stop boundary, precision, and time zone when needed. |
| Distribution | Median and tail measures only when justified; include range or variability and counts. |
| Interpretation | What changed, uncertainty, and no-generalization boundary. |
| Counter-metric | Coverage, mismatch, defect, or evidence-sufficiency signal that prevents speed gaming. |

When only one run exists, report it as one observed duration under stated conditions, not as a percentile or performance guarantee. Reviewer time is similarly task- and expertise-dependent.

**Storage and retention choices**

| sink | strength | risk | suitable content |
| --- | --- | --- | --- |
| Markdown journal or decision record | Human-readable rationale and handoff. | Free-form drift and large diffs. | Claims, evidence locators, decisions, uncertainty, next actions. |
| Structured JSON or TSV events | Machine validation and aggregation. | Schema lifecycle and accidental sensitive fields. | Run identity, stage state, counts, timing, manifest, mismatch classes. |
| Shell output log | High-fidelity execution diagnostics. | Noise, truncation, secrets, path exposure, and poor queryability. | Securely retained failed-command context when needed. |
| CI artifact | Centralized repeatability and owner visibility. | Retention limits, runner differences, and access controls. | Manifests, structured summaries, fixture outcomes, approved map output. |
| Metrics system | Trends and alerts over comparable cohorts. | Lost raw context and incentive gaming. | Aggregates with links to definitions and evidence. |
| Trace or runtime observability system | Correlation across dynamic behavior. | Sensitive data, sampling, cost, and unexercised paths. | Routed runtime claims under service policy. |
| Issue or review system | Ownership, discussion, and approval. | Manual summaries can become stale. | Decision state, reviewer dissent, accepted risk, and follow-up. |

Choose one authoritative identity and link secondary sinks. Do not copy mutable decision state into several places without an owner and synchronization rule.

**Data minimization and integrity**

- Prefer command summaries, artifact hashes and row keys, changed-file lists, pointers, mismatch classes, and unresolved-risk notes over raw transcript or repository dumps.
- Do not log credentials, tokens, private customer data, environment secrets, or unrestricted runtime payloads.
- Treat paths and symbol names as potentially sensitive under project policy.
- Record truncation explicitly; missing tail output can hide the actual failure.
- Protect manifests and logs from concurrent writers and partial upload.
- Mark reconstructed state as reconstructed, including which fields came from filesystem timestamps or later inference.
- Measure wrapper overhead when timing claims matter; observability can affect the workload it observes.

**Profile examples**

Navigation: retain target revision, exact query, selected pointer, direct source observation, duplicate resolution, and stop reason. No broad run telemetry is needed if no map was produced.

Standard decision: retain the full run envelope, manifest, coverage, actual symbol-producer evidence, queries, samples, mismatches, project checks, claim transitions, and invalidation.

High assurance: add configuration and variant identities, negative tests, build and runtime evidence, security or domain review, residual risk, and owner acceptance under applicable retention policy.

Bad observability: save only an SVG and one elapsed-time value, with no cap, producer, root, revision, coverage, or source verification. The record cannot explain architecture or performance.

**Reconstruction acceptance test**

Give a reviewer who lacks the original conversation the retained record and ask them to identify:

1. The exact user decision and consequence.
2. Producer, target, working state, capabilities, actual symbol producer, options, and attempt.
3. Whether the artifact directory is complete, fresh, and internally consistent.
4. Included and excluded evidence surfaces.
5. The query, selected rows, pointers, and direct source observations.
6. Which evidence supports and refutes each material claim.
7. Every failure, retry, contradiction, and route transition.
8. The current decision state, owner, remaining uncertainty, invalidation, and next action.
9. Which details are observed, derived, reconstructed, illustrative, or unknown.
10. What can be discarded without losing reproducibility or violating retention policy.

If the reviewer fills gaps from personal repository familiarity, repeat with a less context-rich reviewer. The strongest observability test is successful handoff under context loss.

Observability closes the learning loop only when it retains correlation. A pointer mismatch without producer and revision cannot improve extraction; a post-action defect without its claim route cannot improve promotion gates. The run envelope and decision identifier provide those edges while keeping evidence compact enough to review.

## Performance Verification Method

No performance benchmark was executed for this evolution. The method below defines how a future authorized study can make a bounded claim. Current latency, memory, throughput, capacity, percentile, reviewer-time, and productivity values remain unknown.

**Separate the performance subject**

| subject | start boundary | stop boundary | primary measures | quality counter-metrics |
| --- | --- | --- | --- | --- |
| Artifact production | Validated root and fresh output are ready. | Complete manifest and artifact gates finish. | Wall time, CPU time, peak memory, bytes read/written if available, artifact bytes, and stage times. | Inventory coverage, schema, symbol and relation samples, projection consistency, partial/failure count. |
| Artifact query | Compatible artifacts are ready and a question is stated. | Ranked candidate rows are produced. | Query wall time, rows scanned, candidates returned, and memory where relevant. | Candidate usefulness, missed known candidates, complete-row versus projection use. |
| Pointer retrieval | Candidate row and bound revision are ready. | Expected source context is displayed and classified. | Time to source, bytes or lines read, and expansion count. | Pointer semantic hit, stale range, duplicate identity, missing context. |
| Decision workflow | User decision and evidence profile are stated. | Reviewer identifies next action, verification gate, stop condition, and residual uncertainty. | End-to-end elapsed time, reviewer active time when measurable, source units inspected, route count, and rework. | Claim sufficiency, contradiction discovery, post-action reversal, and escaped dependency defects. |

Do not combine these subjects into one unlabeled duration. A producer optimization can improve map time and worsen reviewer time by emitting noisier candidates. A query can be fast because it reads a capped projection instead of complete evidence.

**Experiment card**

Before collecting a timing, define:

| field | completion rule |
| --- | --- |
| Hypothesis | Name one causal change and the expected metric direction, stage, and reason. |
| Decision | State what implementation or route choice the result can change. |
| Baseline | Producer hash, wrapper, command, options, capabilities, and artifact contract. |
| Candidate | Exact changed producer or method, with unrelated changes excluded. |
| Workload | Frozen repository or fixture identity, `F`, `C`, `B`, `S`, `R`, `E`, `G`, language mix, filesystem, and evidence profile. |
| Environment | Hardware, operating system, shell, Python, `rg`, Ctags, Graphviz, filesystem locality, cache state, power state, and competing load as relevant. |
| Measurement boundary | Exact start and stop events, clock, profiler, sampling, warmup, and timeout/cancellation policy. |
| Repetition design | Run count chosen from observed variance and desired claim, order randomization or alternation, and failed-run handling. |
| Output equivalence | Structural and semantic properties that must match, plus intended differences. |
| Counter-metrics | Coverage, pointer, relation, decision, and defect signals that must not regress silently. |
| Pass rule | Predeclared evidence needed to adopt, reject, investigate, or reroute. |
| No-claim boundary | Repositories, machines, variants, or user populations to which results do not generalize. |

**Workload tiers**

| tier | purpose | design | claim allowed |
| --- | --- | --- | --- |
| Mechanism fixture | Isolate one branch such as fallback spans, dense imports, graph cap, malformed labels, or streaming memory. | Small controlled source with deterministic expected artifacts and negative cases. | Causal statement about that mechanism under the fixture. |
| Representative repository snapshot | Estimate behavior on a real stable source population. | Frozen revision, working-state policy, language and size profile, secure authorized output. | Bounded result for that repository and environment. |
| Repository cohort | Assess portability across selected source populations. | Predeclared inclusion, language and architecture strata, identical benchmark protocol. | Cohort-bounded trend with heterogeneity reported. |
| Operational workflow sample | Measure end-to-end decision and reviewer effects. | Comparable tasks, users or agents, evidence profiles, decision outcomes, and follow-up window. | Workflow result under the sampled task and reviewer population. |

Keep fixture and target results separate. A fixture explains why a stage changes; it does not establish monorepo capacity. A repository snapshot establishes one environment; it does not become a universal threshold.

**Baseline comparability gates**

Abort or relabel the comparison when:

- repository revision, dirty state, generated inputs, root, or inventory policy differs unintentionally;
- Ctags capability, actual symbol producer, Python, `rg`, Graphviz inclusion, shell, or wrapper differs outside the hypothesis;
- one attempt uses an existing output directory or contains stale conditional artifacts;
- `MAX_GRAPH_EDGES`, language mix, fixture content, filesystem location, or cache treatment differs unintentionally;
- one producer fails or emits a partial artifact set and the other completes;
- background load, power state, thermal behavior, or storage pressure makes observations noncomparable for the intended claim;
- measurement tooling or logging overhead differs materially;
- quality gates reveal that the candidate produces a different evidence product not covered by the hypothesis.

Real-world variation can be studied later as a field distribution. First establish controlled causality; then establish representativeness.

**Output-equivalence contract**

When the candidate intends only a performance change, verify:

| artifact or claim | equivalence check |
| --- | --- |
| Inventory | Same ordered or normalized path population and line counts, unless ordering is explicitly irrelevant and compared as a multiset. |
| Symbols | Same schema and semantically equivalent row multiset under the same actual extractor; inspect ranges and kinds, not only count. |
| Raw imports | Same source, line, target reference, and kind rows under a defined duplicate and ordering policy. |
| Internal and unresolved relations | Same row multisets and classifications under the same resolver contract. |
| Projections | Same selected pair frequencies and cap behavior, allowing only documented deterministic serialization differences. |
| Summary | Counts and fan rankings reconcile with equivalent underlying rows. |
| Pointer behavior | Same accepted forms, normalization, context windows, and expected source output. |
| Decision evidence | Same candidate, contradiction, and escalation outcomes on predeclared tasks. |

Byte hashes are useful when deterministic serialization is expected. If timestamps, ordering, environment paths, or intentionally changed semantics make bytes differ, compare structured fields and row multisets with a parser. An unexplained artifact difference blocks a pure-performance claim.

If the candidate intentionally improves semantics, do not force equivalence. Define expected corrected cases, unaffected cases, regression samples, and a new evidence-product version. Compare both quality and cost.

**Instrumentation plan**

| measurement | method class | caution |
| --- | --- | --- |
| Whole-command wall time | Monotonic external clock around preflight-complete invocation through manifest validation. | Include or exclude verification explicitly; do not mix boundaries. |
| CPU and peak memory | Platform-appropriate process accounting or profiler, including child processes. | Tool syntax and accounting differ by operating system; record tool identity and overhead. |
| Stage duration | Wrapper events around inventory, line count, symbols, relations/projection, rendering, and summary, or an instrumented candidate producer. | Current builder lacks stage telemetry; instrumentation changes the producer chain. |
| Filesystem I/O | Operating-system counters, profiler, or wrapper estimates. | Cache, compression, network mounts, and other processes complicate attribution. |
| Artifact size and rows | Structured file inspection and manifest. | More or fewer rows can be a semantic change, not performance. |
| Query and pointer time | Clock bounded around reproducible query and source read. | Human typing and cold process startup should be included or excluded consistently. |
| Reviewer active time | Instrumented task study or carefully logged activity intervals. | Expertise, interruptions, task difficulty, and observation effects are major confounders. |
| Evidence utility | Decision record: retained candidates, contradictions, route changes, and correct next action. | Do not reduce heterogeneous value to an uncalibrated composite score. |

Record tool-call count only if it answers a cost or orchestration question. Fewer calls are not inherently better when one call hides broad output or skips verification.

**Cache and order design**

- State whether runs are cold, warm, or operationally mixed and how that state was established.
- Do not claim a cold cache merely because the process is new; operating-system cache can persist.
- Alternate or randomize baseline and candidate order when drift and warmup could bias one side.
- Use fresh output directories for every attempt.
- Disclose warmup runs and exclude them only under a predeclared rule.
- Keep failed, timed-out, and cancelled attempts in the ledger; classify rather than silently dropping them.
- Monitor source identity before and after each multi-pass run.

Avoid privileged cache manipulation unless explicitly authorized and safe. If true cold-cache control is impractical, measure the operational cache state and narrow the claim.

**Distribution reporting**

The seed requests p50, p95, and p99 measurements where runtime applies. Use a percentile only when the sample contains enough comparable observations for that tail to be meaningful, the quantile definition is stated, and raw counts are retained. This reference supplies no fixed minimum sample because required stability depends on variance and decision consequence.

Report:

- number of valid, failed, timed-out, cancelled, and excluded attempts;
- raw observations or a durable recalculation source;
- median, range, variability, and tail summaries justified by the data;
- baseline and candidate paired or unpaired design;
- confidence interval or uncertainty method when making an inferential claim;
- outlier policy and sensitivity to alternative treatment;
- exact cohort and no-generalization boundary.

One run is one observation. Report its duration and conditions honestly; do not label it p50, p95, p99, typical, or guaranteed.

**Quality counter-metric gate**

A candidate cannot pass on speed alone. Verify at least the quality dimensions affected by the hypothesis:

| risk | counter-metric or gate |
| --- | --- |
| Faster inventory omits files. | Independent coverage reconciliation and excluded-surface review. |
| Faster symbol extraction loses constructs or ranges. | Stratified pointer resolution and semantic-hit samples plus fixture expectations. |
| Faster resolver forces more false internal edges. | Internal-edge agreement and unresolved classification samples. |
| Lower graph cap improves render time but hides relations. | Full-row equality and explicit projection-only claim. |
| Fewer source reads miss context. | Claim sufficiency, whole-file expansion yield, contradiction and missed-consumer review. |
| Faster workflow stops too early. | Correct next action, verification gate, stop condition, post-action reversals, and escaped defects. |
| More logging slows production. | Wrapper overhead measured with equal observability requirements and no loss of reconstruction quality. |

**Route-specific pass conditions**

| performance decision | pass condition |
| --- | --- |
| Adopt a producer optimization | Predeclared performance objective improves under comparable workload, output equivalence or intended semantic improvement passes, variability is understood, and counter-metrics do not reveal material regression. |
| Adopt a query optimization | Candidate set and complete-row semantics are preserved while relevant query cost improves under representative filters. |
| Reduce context | Reviewer still identifies the correct bounded next action, evidence gate, stop condition, and unresolved risk without reading unrelated files or missing consequential evidence. |
| Reuse instead of rebuild | Provenance-validation plus query cost is lower than measured rebuild cost for the decision, and artifact compatibility gates pass. |
| Skip mapping | Direct or native evidence answers the claim with lower measured workflow cost and equal or stronger sufficiency. |
| Reject result | Comparability, output, quality, sample, or uncertainty gates fail, even if one timing is faster. |

**Worked experiment design, without results**

Hypothesis: Streaming relation serialization in a future producer reduces peak memory for high-`R` workloads without changing relation rows, pair frequencies, graph projection, summary counts, or decision samples.

Plan:

1. Freeze a mechanism fixture with dense imports and a representative repository snapshot.
2. Bind baseline and candidate hashes, wrapper, options, actual symbol producer, and environment.
3. Use fresh attempt directories and alternate run order under disclosed cache state.
4. Measure whole-command and relation-stage time, child-inclusive peak memory, artifact bytes, and attempt outcomes.
5. Parse TSVs and compare row multisets; compare pair-frequency projections and summary counts.
6. Replay alias, unresolved, cap, and selected decision samples.
7. Report raw counts, distribution summaries justified by sample stability, instrumentation overhead, and no-claim boundary.
8. Adopt only if memory improvement is reproducible and no semantic or operational regression appears.

This design is actionable but contains no fabricated duration, memory saving, sample result, or pass verdict.

**Performance result language**

Good: "Under the frozen snapshot, matched capability branch, fresh output, and stated cache design, the candidate reduced the predeclared production measure across repeated runs; structured artifacts were equivalent and quality samples showed no observed regression within their scope."

Bad: "One warm run was faster, so p99 performance improved and the tool scales." The evidence supports neither a tail statistic nor a capacity claim.

Diagnostic only: "One run took the observed duration and spent most sampled CPU in the relation stage." This can motivate a controlled experiment but is not a general performance conclusion.

The leading indicator remains decision-relevant uncertainty reduction, not raw command speed. The failure signal remains pattern or implementation commitment before workload, reliability, and failure boundaries are explicit. Performance verification is therefore evidence-throughput verification: time and resources matter only alongside the quality and decision value they produce.

## Scale Boundary Statement

Dependency Map Cli Patterns stops being sufficient when its batch workload, observation model, artifact lifecycle, review capacity, or ownership model cannot preserve the evidence contract required by the decision. Crossing a scale boundary does not mean every artifact is useless. It means claims must narrow, production must change, or the question must route to another evidence system.

There is no universal file, line, edge, duration, memory, or agent-count threshold in this reference. Measure the intended workload and define local budgets. The current producer has no persistent index, incrementality, lock, queue, resume, transaction marker, or measured capacity.

**Scale dimensions and route triggers**

| dimension | observable pressure | boundary crossed when | response |
| --- | --- | --- | --- |
| Raw inventory `F` | Inventory time, path artifact size, nested scope, ignored policy. | A complete intended population cannot be produced or reviewed within authorized resource and time budgets. | Use native inventory, justified scope, or a persistent index; preserve exclusion ledger. |
| Supported source `C` and `B` | Repeated line-count, symbol, and relation scans; large-file distribution; filesystem throughput. | Multi-pass batch cost exceeds reuse value or cannot complete reliably. | Direct search for narrow tasks, component scope with boundary rules, incremental parser/index, or scheduled background production. |
| Symbols `S` | Artifact size, duplicate identities, query noise, pointer sample burden. | Compact queries no longer narrow source meaningfully or extractor quality cannot be reviewed. | Add qualification and semantic index, improve extractor with fixtures, or route symbol claims. |
| Relation rows `R` and pairs `E` | Memory, TSV size, rank computation, sample and mismatch load. | In-memory accumulation or review burden is unacceptable, or heuristic error dominates useful candidates. | Stream in a future producer, persist a queryable graph, partition with join semantics, or use a stronger resolver. |
| Projection cap `G` | Mermaid/DOT/SVG size and visual comprehensibility. | Graph cannot communicate a useful selected neighborhood even after cap and query. | Render focused subgraphs; keep TSVs authoritative. Lowering `G` never solves full extraction cost. |
| Query volume `Q` | Repeated artifact filters, rebuild frequency, number of users or decisions. | Batch production and freshness checks are repeatedly paid or artifact access becomes contended. | Use shared immutable artifacts, indexed query service, or repository-native semantic platform with lifecycle ownership. |
| Churn and reuse horizon | Revision changes, pointer invalidation, regenerated files, map age at first query. | Artifacts become stale before enough questions reuse them. | Direct or incremental search, event-driven rebuild, or a native index with verified invalidation. |
| Language and syntax diversity | Unsupported extensions, mixed parser branches, alias and macro clusters. | Relevant source or relation classes fall outside observation or samples cannot bound error. | Federate language-specific analyzers under one decision identity. |
| Configuration variants `V` | Features, targets, platforms, tenants, deployment modes, generated states. | One static map cannot support claims across relevant variants. | Build/configuration matrices, generated-state checks, tests, runtime observations, and owner scope. |
| Dynamic behavior | Reflection, registration, plugin loading, data-driven dispatch, runtime topology. | The decisive relation exists only outside static lexical evidence. | Route to configuration and runtime evidence; rough map remains auxiliary discovery. |
| Multiple systems | Repositories, services, deployed components, APIs, queues, databases, or third-party boundaries. | A local file graph cannot represent the end-to-end dependency or failure path. | Federated service/build/runtime topology and system-design or incident evidence. |
| Ownership boundaries | Several teams, approval processes, sensitive domains, or conflicting architecture intent. | No single mapper or agent can authorize the global decision. | Preserve per-owner evidence, interface contracts, merge review, and accountable acceptance. |
| Agent concurrency | Parallel readers and writers, shared output, overlapping files, merge conflicts. | Ownership or artifact identity can no longer be guaranteed. | One writer per surface, unique outputs, explicit handoffs, merge-time verification, and backpressure. |
| Context and reviewer capacity | Large artifacts, repeated reads, unresolved-risk volume, handoff complexity. | Reviewers cannot reconstruct why selected evidence supports the action. | Query-first context, decision records, component reviews, and staged approval. |
| Assurance level | Deletion, migration, security, compliance, availability, or production-impact claim. | Rough evidence cannot satisfy the required prevention and verification floor even at small input size. | Skip to high-assurance semantic, build, test, configuration, runtime, and owner evidence. |

Scale is claim-relative. A huge repository can still support an exact `rg` navigation answer. A tiny service with runtime plugin registration can exceed the rough mapper's semantic boundary immediately.

**Boundary outcomes**

| outcome | permitted use | required language |
| --- | --- | --- |
| `within_full_batch_boundary` | Fresh full map, compact queries, source checks, and profile-appropriate verification. | State measured workload and no-generalization boundary. |
| `within_scoped_boundary` | Component-local map and decisions whose consumers and interfaces are explicitly bounded. | Say component or root scope; never imply whole-repository completeness. |
| `projection_only_boundary` | Full TSV artifacts remain usable, but graph rendering is capped or visually overloaded. | Analyze rows and describe graph as selected presentation. |
| `discovery_only_boundary` | Rough evidence can identify candidates but cannot settle the claim. | Use candidate, observed, or unresolved states and name the stronger route. |
| `batch_economics_boundary` | Fresh maps cost more than their reuse and decision utility. | Explain direct, incremental, or persistent replacement. |
| `observation_model_boundary` | Unsupported, semantic, configured, generated, runtime, or security relation is decisive. | Stop verification within rough mapping and route. |
| `governance_boundary` | Multiple owners or systems require coordinated authority. | Split evidence by ownership while preserving interfaces and global decision record. |
| `authorization_boundary` | Required source, output, runtime, or data access is unavailable. | Report blocked evidence and owner; do not circumvent. |

**Safe narrowing contract**

Narrowing root, files, relation classes, queries, or samples is safe only when:

1. The user decision can be restated within the narrowed scope.
2. External interfaces and possible consumers outside scope are listed.
3. The inventory rule and excluded paths are explicit.
4. Cross-boundary imports, builds, configuration, runtime calls, data, and owners have a separate evidence route.
5. No global absence, complete blast-radius, or whole-system claim is made from the narrowed artifact.
6. The decision record carries the scope into source checks, tests, handoff, and invalidation.
7. Scope expansion has a named trigger when new evidence crosses the boundary.

Arbitrary directory scoping to make runtime acceptable is not a performance fix; it creates a different evidence product.

**Sharding contract**

When one full batch is impractical and the decision genuinely spans shards, define:

| shard concern | required rule |
| --- | --- |
| Partition | Stable ownership, build, package, language, or component boundary with a reason; avoid accidental path-size chunks. |
| Identity | Global repository revision and producer plus shard identifier and root. |
| Coverage | Union and overlap policy; every intended file maps to zero, one, or documented multiple shards. |
| Node identity | Qualified path or semantic identifier that prevents duplicate-name collapse across shards. |
| Cross-shard edges | Separate extraction or authoritative system capable of finding interfaces beyond local roots. |
| Duplicate policy | Deterministic handling of shared files, generated outputs, vendored code, and repeated relations. |
| Merge | Structured row and claim reconciliation, not graph-image concatenation. |
| Conflict | Owner and method for incompatible evidence, version, or configuration. |
| Verification | Per-shard gates plus global interface, variant, and absence checks appropriate to the decision. |
| Invalidation | Source or producer changes identify affected shards and global claims. |

Parallel shards improve elapsed time only if filesystem and resource contention allow it. They increase coordination, merge, and identity cost. Measure both.

**Persistent and federated routes**

| need | likely route | new reliability burden |
| --- | --- | --- |
| Many repeated symbol and relation queries | Persistent semantic or code graph index. | Index version, freshness, invalidation, schema, access, and service availability. |
| Frequent source churn | Incremental parser/index or repository-native service. | Correct incremental updates and stale-read detection. |
| Multi-language semantics | Federated language analyzers with normalized identifiers. | Cross-language joins, differing capabilities, and partial failure. |
| Build and generated composition | Build-system and generation graph. | Variant and target configuration, cache, generated artifact identity. |
| Distributed runtime behavior | Traces, service topology, logs, and configuration inventory. | Sampling, workload coverage, privacy, clock correlation, and production safety. |
| Organization ownership | Service catalog, ownership metadata, and review workflow. | Staleness, authority, and conflict with descriptive source evidence. |

The scalable design is often federated evidence under a common decision identifier, not one graph pretending to encode source, build, runtime, and ownership equally.

**Distributed execution boundary**

- Assign one verification owner and one writer for each reference, packet, shard, or artifact directory.
- Parallelize only independent reads or outputs with explicit roots and merge contracts.
- Do not let agents rewrite the same reference or output without an ordered handoff and merge checkpoint.
- Persist atomic section or shard completion before starting another unit.
- Use backpressure when shared resource, review, or ownership capacity is saturated.
- Verify exact paths, heading/order contracts, producer identities, coverage union, cross-shard edges, and evidence boundaries at merge.
- Preserve user changes and other lanes; scale does not authorize destructive cleanup.

**Long-running context boundary**

Treat context drift as a reliability failure. Durable state must include current decision, completed units, source identities, open mismatches, failed attempts, exclusive paths, verification evidence, next step, and stop condition. Checkpoint before broad rewrites and at most every configured review slice. Re-read the current specification and newest user instructions after interruption.

Context compaction is not evidence compaction. Preserve claim-relevant locators and invalidation even when conversation prose is summarized.

**Production-traffic boundary**

A repository map cannot establish a production service-level objective, latency distribution, throughput, availability, or live reachability. When a change affects production traffic:

- define the service objective and workload separately;
- identify deployed versions and configuration;
- use benchmark, load, canary, trace, log, metric, and rollback evidence appropriate to the system;
- protect sensitive production data and respect change controls;
- treat static map candidates as source-navigation input only;
- obtain operational owner acceptance for residual risk.

The task crosses this reference's primary boundary even if the source repository is small.

**Scale assessment procedure**

1. State the decision and reliability profile.
2. Estimate or probe `F`, `C`, `B`, expected `S`, `R`, `E`, `G`, `Q`, `V`, churn, systems, owners, and reviewer capacity.
3. Identify relevant unsupported and dynamic relation classes before full production.
4. Run a controlled fixture or representative snapshot only when authorized and safe.
5. Capture resource, artifact, quality, freshness, and reconstruction measures.
6. Compare full, scoped, persistent, or routed alternatives under the same claim.
7. Select the least costly route that preserves evidence sufficiency and governance.
8. Record boundary outcome, exclusions, release trigger, and invalidation.

**Scale test tiers**

| test | verifies | does not verify |
| --- | --- | --- |
| Growth fixture over source bytes and relation density | Stage growth and resource saturation mechanism. | Real repository semantics or filesystem mix. |
| Scoped-versus-full snapshot comparison | Which candidate rows and cross-boundary relations narrowing loses. | Other repositories or future churn. |
| Churn replay | Artifact invalidation and rebuild or index freshness behavior. | Runtime configuration not represented in source. |
| Concurrent shard test | Output isolation, contention, merge, and failure handling. | Human owner agreement or semantic joins beyond test cases. |
| Reviewer reconstruction | Whether evidence remains understandable at artifact scale. | Automated correctness of all claims. |
| High-assurance scenario | Whether routing and owner gates block weak evidence. | Universal security or production safety. |

**Examples**

Good volume scaling: A measured full run exceeds the accepted batch window, so the team uses ownership-aligned shards, preserves a global revision, audits coverage union, extracts cross-shard interfaces with a native build graph, and limits local claims to each component.

Bad volume scaling: The agent maps only `src/core`, omits cross-boundary consumers, and reports whole-repository blast radius because the command completed quickly.

Good churn scaling: Maps become stale before reuse, so exact queries use direct search and repeated semantic queries move to an incremental index with freshness observability. Batch output is retained only for frozen review snapshots.

Good assurance scaling: A small repository's security absence claim bypasses rough verification and routes to configuration, tests, runtime evidence, and an authorized security owner. Input size does not lower the assurance boundary.

Conditional component use: A narrow map supports local navigation inside one service if interfaces and external consumers are out of scope and stated. It cannot authorize deletion of a shared contract.

Scaling changes governance as well as computation. More shards, agents, indexes, variants, and systems require shared identity, ownership, merge semantics, invalidation, and conflict resolution. The first saturated resource may be reviewer coherence rather than CPU or memory. Preserve the evidence contract first; then optimize the mechanism that actually crossed its boundary.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | dependency map cli patterns official documentation best practices |
| `github_repository_query_phrase` | dependency map cli patterns GitHub repository examples |
| `release_notes_query_phrase` | dependency map cli patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
