# Parseltongue Graph Workflow Patterns

**Decision supported.** This section helps decide whether and how to use Parseltongue 1.7.2 to orient, trace dependencies, test graph hypotheses, and narrow code reading for a specific codebase question. The seed title does not define the version-pinned run lifecycle, graph questions, evidence limits, or handoff to direct code reading.

**Recommended default and causal basis.** Pin and verify version 1.7.2, create or refresh an isolated run, load actual paths and server URL from `run.config`, verify health and coverage, orient before tracing, choose the smallest endpoint workflow matching the question, preserve query artifacts, and confirm dynamic or low-coverage conclusions in source. Correct run identity and coverage are prerequisites for trustworthy topology, while question-specific forward and reverse traces reduce context without pretending the graph is runtime execution.

**Operating conditions and assumptions.** The target codebase is indexable, the version and run folder are known, coverage is sufficient around the entities, and the question concerns topology, dependency pressure, architecture, or change risk. Use this reference for Parseltongue 1.7.2 graph workflows, not generic GitHub automation or exact dynamic analysis.

**Failure boundary and alternatives.** Exact branch behavior, value propagation, reflection, generated code, queues, or dynamic dispatch governs the answer; the graph is stale; or version and bound URL cannot be verified. Bounded alternatives and recoveries: refresh or rebuild the run, use direct file reads at parse frontiers, add runtime tests or traces, use a simpler dependency map, or stop when graph and code evidence conflict.

**Counterexample, gotchas, and operational comparison.** Assuming port 7777, trusting requested DB paths, watcher counters as sole proof, searching before orientation, treating blast radius as call execution, hard-coding entity names, and using heuristic caller thresholds as universal risk. Good: verify run health, search an entity, inspect reverse callers and forward callees, quantify blast radius, then read the narrowed code. Bad: declare a branch unreachable from graph absence. Borderline: use source-to-sink convergence as a strong hypothesis while confirming dynamic dispatch directly.

**Verification, evidence, and uncertainty.** Record Parseltongue version, run folder, `SERVER_URL`, `DB_URI`, workspace, health, watcher and logs, coverage, exact queries, entity keys, response summaries, direct-code confirmations, uncertainty, and stop or refresh decision. The fully read local sources directly define the 1.7.2 version policy, run ground truth, endpoint catalog, thirteen bidirectional workflows, twelve flow patterns, and modeling limits. No live run or target codebase was supplied, and public links were not refreshed, so endpoint behavior and graph quality remain conditional on actual setup.

**Second-order consequence.** Parseltongue is a hypothesis accelerator: its strongest contribution is reducing the search space and exposing topology, not replacing semantic code or runtime evidence.

**Revision decision.** Add a versioned run contract, question classifier, orientation and coverage gates, graph-evidence limits, direct-read handoff, and auditable query packet.

**Retained seed evidence.** The exact title and four local plus three external source rows remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source may support a Parseltongue 1.7.2 runtime claim, endpoint claim, workflow heuristic, or merely an adjacent process analogy. The seed lists four directly relevant local Parseltongue artifacts beside three public workflow links, but its uniform row shape can imply that every source has equal authority over graph behavior.

**Recommended default and causal basis.** Treat the pinned skill as the operational authority, the endpoint and workflow files as detailed local evidence, and the GitHub or Codex links as adjacent process context that cannot prove Parseltongue semantics. Provenance determines what a claim can legitimately say; a local endpoint catalog can establish a route contract while a generic CI page can only suggest review or automation practices.

**Operating conditions and assumptions.** The recommendation names a claim, traces it to one or more exact rows, labels synthesis separately, and preserves the distinction between tool behavior and surrounding agent workflow. Apply this hierarchy to the seven frozen source rows and to claims derived from them; do not infer source quality from local-versus-public location alone.

**Failure boundary and alternatives.** A public automation page is cited as proof of graph traversal, a local heuristic is promoted to runtime fact, a URL is assumed fresh without review, or an inference has no visible evidence chain. Bounded alternatives and recoveries: downgrade the statement to a labeled inference, remove the unsupported claim, consult the live API documentation from the verified run, or obtain direct runtime and source evidence before deciding.

**Counterexample, gotchas, and operational comparison.** Counting source rows as corroboration, mistaking adjacency for authority, hiding conflicts behind a combined label, and allowing a source title to substitute for reading the relevant passage. Good: cite the endpoint reference for `smart-context` availability and call its selection quality conditional. Bad: cite GitHub Actions to assert a Parseltongue database location. Borderline: borrow reusable-workflow review discipline while labeling it as an analogy.

**Verification, evidence, and uncertainty.** Build a claim-to-row ledger, open every cited local artifact, record whether support is direct or inferential, flag unused and conflicting rows, and ensure each operational claim has a tool-specific source or live observation. The four local files were fully read and their roles are concrete; the three external rows are preserved facts from the seed but were not refreshed and do not document Parseltongue itself. The exact freshness of public pages and any unpublished runtime changes remain unknown, so this map supports provenance discipline rather than current external feature claims.

**Second-order consequence.** Source authority is claim-relative: the same row may be canonical for installation policy, supporting for a workflow, and irrelevant to a dynamic-control-flow conclusion.

**Revision decision.** Add claim classes, authority rules, misuse examples, conflict handling, and a verification ledger while retaining every original path, URL, category, and synthesis role.

**Retained seed evidence.** All seven source rows and their exact evidence labels remain intact beneath the expanded provenance guidance. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_bidirectional_workflows.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_endpoints.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_flow_patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | primary automation and CI/CD workflow documentation |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | external_research_source_material | external_research_sourced_fact | primary guidance for reusable workflow composition |
| https://github.com/openai/codex/blob/-/AGENTS.md | external_research_source_material | external_research_sourced_fact | agent project instructions and testing guidance in a real repository |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide how to prioritize these three practices without treating editorial scores as calibrated probabilities, benchmark results, or universal ordering. The seed assigns scores of 95, 91, and 88 to source-map-first, evidence-boundary, and verification-gate patterns without defining a measurement scale or observed sample.

**Recommended default and causal basis.** Use the ranking as a sequencing heuristic: establish run and source truth first, separate facts from inference second, and attach executable verification third, while judging all three as required gates. Later verification cannot repair a query against the wrong run, and precise provenance cannot make an unverified conclusion operational; the order describes dependency, not dispensability.

**Operating conditions and assumptions.** A reviewer uses the tiers to order work, records actual pass or fail evidence for each gate, and revises priority when the task is a live incident, stale index, or narrow code-reading question. Retain the frozen values as seed metadata, but prohibit their use as probabilities, service objectives, or cross-reference quality comparisons.

**Failure boundary and alternatives.** The numbers are quoted as empirical confidence, a lower-ranked gate is skipped, score differences are used to resolve contradictory evidence, or the same ordering is imposed on every workload. Bounded alternatives and recoveries: replace numeric emphasis with prerequisite labels, use a task-specific risk matrix, elevate live-run validation during incidents, or treat all three patterns as a single completion checklist.

**Counterexample, gotchas, and operational comparison.** False precision from two-digit scores, confusing adoption tier with evidence strength, optimizing the ranking instead of the investigation, and hiding a failed gate behind a high aggregate impression. Good: run identity receives first attention before any trace, then evidence labels and direct confirmation close the claim. Bad: call a result 95-percent reliable because the first row scores 95. Borderline: reorder verification first during outage triage but still backfill provenance.

**Verification, evidence, and uncertainty.** For sampled uses, record which gate ran first, whether wrong-run or unsupported-claim errors were caught, whether every gate eventually passed, and whether a different ordering would have changed the decision. The seed directly preserves three ranked practices and their intended failure-prevention targets; no local source supplies a calibrated scoring method for the numeric values. Relative impact will vary by repository, graph coverage, and incident urgency, so the stated ordering is reasoned workflow guidance rather than measured causal effect.

**Second-order consequence.** The scoreboard is most useful as a dependency graph among safeguards: source truth enables meaningful evidence labels, and both make verification results interpretable.

**Revision decision.** Define the scale limitation, convert each row into an observable gate, explain task-specific reorderings, and require all three safeguards before a graph conclusion is accepted.

**Retained seed evidence.** The identifiers, values 95, 91, and 88, tiers, and failure-prevention text remain exactly available in the original table. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `parseltongue_graph_workflow_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local parseltongue graph material before synthesizing workflow patterns recommendations. |
| `parseltongue_graph_workflow_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `parseltongue_graph_workflow_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what governing rule should control a Parseltongue-assisted investigation from initial setup through a defensible code or architecture conclusion. The seed thesis says to load local material, check public guidance, and add verification, but it does not state the causal limits of graph evidence or the order of run validation, orientation, tracing, and direct reading.

**Recommended default and causal basis.** Treat Parseltongue 1.7.2 as a version-pinned topology and context-narrowing instrument: verify the run, orient globally, select a question-shaped trace, and confirm semantic claims at the code or runtime boundary. Graph structure efficiently reveals callers, callees, clusters, cycles, and change spread, while branches, values, reflection, generated behavior, and operational execution require evidence the index does not encode.

**Operating conditions and assumptions.** The investigation asks a structural question, coverage is visible, entity identity is stable, trace results are preserved, and the analyst follows the narrowed path into source where interpretation begins. Use the thesis for structural discovery and hypothesis formation in Parseltongue 1.7.2; escalate exact behavior, temporal order, and data semantics to stronger evidence.

**Failure boundary and alternatives.** A graph edge is treated as proof of execution, a missing edge is treated as proof of impossibility, setup identity is assumed, or a broad context bundle replaces a concrete hypothesis. Bounded alternatives and recoveries: use direct code navigation for a small known surface, runtime tracing for execution claims, tests for behavioral contracts, logs for incidents, or a refreshed index when coverage and freshness are suspect.

**Counterexample, gotchas, and operational comparison.** Equating topology with semantics, allowing a polished diagram to hide stale data, querying before discovering repository shape, and making `smart-context` output the conclusion rather than the reading list. Good: use reverse callers to identify an entry corridor, forward callees to narrow downstream effects, then inspect guards in source. Bad: declare every callee executed. Borderline: use a cluster as an ownership clue pending repository metadata.

**Verification, evidence, and uncertainty.** Capture run identity and health, orientation outputs, query parameters, returned entity keys, coverage gaps, directly read spans, runtime corroboration where needed, and the final statement's evidence label. The local skill and references consistently describe version enforcement, orientation, traversal, graph workflows, modeling limits, and a direct-code handoff. The graph's actual completeness and language-specific parser behavior depend on a live indexed workspace, so this thesis cannot promise a fixed accuracy rate.

**Second-order consequence.** The workflow's value is multiplicative rather than substitutive: better topology makes code reading cheaper, and code reading makes topology safer to interpret.

**Revision decision.** Replace the generic synthesis with an explicit evidence ladder, model-limit statement, alternative-tool routing, operational example, and claim-level verification packet.

**Retained seed evidence.** The three evidence-boundary labels and the statement that local sources are the first retrieval surface remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `parseltongue_graph_workflow_patterns` contains 4 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Parseltongue Graph Workflow Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which local Parseltongue artifact to read first for a particular stage of setup, orientation, dependency tracing, architecture analysis, or flow interpretation. The seed accurately inventories the skill, bidirectional workflows, endpoints, and flow patterns, yet a reader still has to infer which file to open for setup, query syntax, investigation design, or graph-model caution.

**Recommended default and causal basis.** Open the skill for version and run ground truth, the endpoint catalog for concrete HTTP questions, the bidirectional reference for investigation choreography, and the flow-pattern reference for reusable structural hypotheses and limits. Routing by task avoids loading 924 lines indiscriminately and preserves each artifact's authority: operational policy, endpoint mechanics, multi-query workflow, and interpretive model play different roles.

**Operating conditions and assumptions.** The user can name the current decision stage, opens only the canonical file plus needed detail, records the relevant heading, and returns to source code once the selected workflow reaches its parse frontier. Route only among the four frozen local sources; live run output and repository code remain separate evidence that must be captured when the task requires them.

**Failure boundary and alternatives.** All four files are dumped into context without a question, a workflow narrative overrides endpoint truth, setup is copied from a detail file while ignoring `run.config`, or a pattern label is mistaken for observed runtime flow. Bounded alternatives and recoveries: start with the endpoint question matrix for an already healthy run, read only the skill for installation or reindexing, bypass the corpus for direct code reading when the target is already known, or consult live API help after endpoint drift.

**Counterexample, gotchas, and operational comparison.** Confusing heading coverage with claim support, reading workflow names without their stop conditions, missing the version policy in the skill, and treating supporting references as independent implementations. Good: for deletion safety, read the skill's ground truth, then the deletion classifier workflow and relevant traversal endpoints. Bad: load flow patterns to guess the bound port. Borderline: start at endpoints during an active run but verify version before acting.

**Verification, evidence, and uncertainty.** For each task, log the question class, chosen file and heading, omitted files with reasons, endpoint or command used, resulting code spans, and whether a second source changed the conclusion. The complete local corpus exposes clear headings for Ground Truth, Run Workflow, Endpoint Fit, thirteen bidirectional workflows, twelve flow patterns, and explicit modeling limits. The map describes archived 1.7.2 guidance and cannot prove that a particular indexed repository has full parser coverage or an unchanged live endpoint surface.

**Second-order consequence.** Progressive disclosure here is an accuracy control as well as a context optimization, because loading the right authority reduces accidental cross-layer claims.

**Revision decision.** Turn the inventory into a stage-by-stage router with read-first triggers, skip conditions, direct-code exits, and an audit record for source selection.

**Retained seed evidence.** All four local paths, titles, heading signals, and usage roles remain exactly present in the retained table. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/SKILL.md | run-parseltongue-1-7-2 | Run Parseltongue 1.7.2; Ground Truth; Enforce Version Policy; Code Reading Preference; Flow Modeling Guardrail; Run Workflow | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_bidirectional_workflows.md | Parseltongue 1.7.2 Bidirectional Workflows | Parseltongue 1.7.2 Bidirectional Workflows; Workflow Index; 1) Meet-in-the-Middle Hypothesis Test; Symptom side: who reaches the broken point?; Root-cause side: what does the suspected culprit reach?; Quantify each side | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_endpoints.md | Parseltongue 1.7.2 Endpoints | Parseltongue 1.7.2 Endpoints; Resolve the Base URL First; shellcheck source=/dev/null; Orientation Sequence; Search and Read; Dependency Traversal | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_flow_patterns.md | Parseltongue 1.7.2 Flow Patterns | Parseltongue 1.7.2 Flow Patterns; Modeling Limits; Pattern Index; 1) Ingress-to-Sink Corridor; 2) Gatekeeper Choke Point; 3) Orchestrator Versus Leaf Worker | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide whether and how these three public rows may influence a Parseltongue workflow recommendation without becoming false tool-specific authority. The seed preserves GitHub Actions, reusable workflow, and OpenAI Codex instruction links, none of which directly documents Parseltongue graph installation, endpoints, or modeling semantics.

**Recommended default and causal basis.** Use the public links only for adjacent practices such as automation composition, repository instruction discipline, and test or review handoffs, and label every borrowed practice as external analogy. Process analogues can improve reproducibility around a graph workflow, but they cannot establish the behavior of a separate pinned binary or the completeness of its index.

**Operating conditions and assumptions.** The external source contributes a clearly named operational convention, the local corpus independently supports the Parseltongue action, and the synthesis identifies where analogy ends. Retain these links as frozen external evidence rows and adjacent process context, not as documentation of Parseltongue 1.7.2 features or runtime guarantees.

**Failure boundary and alternatives.** GitHub CI documentation is used to infer an endpoint, Codex repository instructions are treated as universal policy, a link's current content is assumed without refreshing, or external prestige overrules contradictory local evidence. Bounded alternatives and recoveries: omit the external analogy, preserve the row only as historical seed evidence, consult the verified run's API help, or perform a future primary-source refresh when browsing is authorized.

**Counterexample, gotchas, and operational comparison.** Semantic drift behind stable URLs, conflating workflow in CI with graph workflow, importing repository-specific AGENTS rules, and giving an uncited public link equal weight to a fully read local contract. Good: borrow reusable-workflow ideas for making query scripts repeatable while deriving actual curl routes from the endpoint file. Bad: assert GitHub Actions validates Parseltongue coverage. Borderline: use Codex testing guidance as a review prompt, not a graph fact.

**Verification, evidence, and uncertainty.** Attach each external-derived sentence to its exact URL and role, state whether content was refreshed, require independent local support for every Parseltongue claim, and remove any sentence that survives only by analogy. The seed directly records the three URLs and intended adjacent roles; their mismatch with tool-specific semantics is evident from the local corpus topics. No browsing is permitted in this evolution pass, so page freshness, redirects, and current wording remain unverified and must not support time-sensitive claims.

**Second-order consequence.** An explicitly weak external map is more useful than an inflated one, because it prevents decorative citations from laundering unsupported tool behavior.

**Revision decision.** Add an adjacency warning, permissible-use matrix, freshness status, rejection examples, and a requirement for local or live corroboration of all tool claims.

**Retained seed evidence.** The three exact URLs, names, usage roles, and external evidence labels remain unchanged below the new boundary guidance. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://docs.github.com/actions | GitHub Actions documentation | primary automation and CI/CD workflow documentation | external_research_sourced_fact |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | Reusable workflow docs | primary guidance for reusable workflow composition | external_research_sourced_fact |
| https://github.com/openai/codex/blob/-/AGENTS.md | OpenAI Codex repository AGENTS | agent project instructions and testing guidance in a real repository | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which failure signatures should block a Parseltongue-assisted conclusion and what bounded recovery each signature requires. The seed names generic context-free, unsourced, and unverified output failures but omits the Parseltongue-specific ways a graph investigation can look rigorous while using the wrong run or exceeding the model.

**Recommended default and causal basis.** Reject conclusions produced from unverified version or run identity, stale or low-coverage graphs, topology-as-execution reasoning, unresolved entity ambiguity, or context bundles with no governing question. These failures corrupt either the evidence substrate or its interpretation, so additional prose and more queries amplify error rather than increasing confidence.

**Operating conditions and assumptions.** Each warning has an observable signal, a stop condition, a corrective action, and a stronger evidence route; generic seed anti-patterns remain umbrella categories rather than the full registry. Apply the registry to Parseltongue setup, query selection, graph interpretation, and handoff; diagnose tool implementation defects separately with logs and source evidence.

**Failure boundary and alternatives.** Warnings are treated as stylistic advice, the agent keeps querying after health or coverage fails, absence is overinterpreted, or mitigation merely repeats the same stale operation. Bounded alternatives and recoveries: source `run.config` and recheck health, refresh or rebuild the index, disambiguate with search and qualified keys, reduce the question scope, inspect code directly, or add runtime tests and tracing.

**Counterexample, gotchas, and operational comparison.** Assuming localhost port 7777, trusting requested instead of actual database paths, using watcher count alone, treating cycles as runtime loops, reading caller counts as severity, and accepting truncated context silently. Good: stop a blast-radius claim when the entity key resolves ambiguously and rerun after disambiguation. Bad: label an unindexed dynamic caller unreachable. Borderline: use high fan-in as review priority while withholding defect severity.

**Verification, evidence, and uncertainty.** Seed a review with wrong-port, stale-index, ambiguous-name, dynamic-dispatch, and oversized-context cases; require detection, stop behavior, corrective evidence, and an uncertainty label for every case. The local skill explicitly warns about actual bound URLs, run configuration, code-reading preference, and flow modeling; the workflow references expose heuristic selection and parse-frontier limits. Repository-specific parser gaps can create additional anti-patterns not visible in the archived corpus, so the registry must remain open to observed false positives and negatives.

**Second-order consequence.** The most dangerous graph failure is silent category error, because a structurally valid response can still be semantically incapable of answering the question asked.

**Revision decision.** Retain the three generic rows, add concrete graph failure signatures, observable detection tests, stop conditions, and recovery routes keyed to evidence strength.

**Retained seed evidence.** Context-free summary, unsourced claims, and unverified instruction rows remain unchanged as broad prevention categories. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which independent gates must pass before accepting the evolved reference itself and before accepting a conclusion produced with Parseltongue. The seed supplies one repository-generation verifier command, which checks an artifact stage but cannot establish live Parseltongue version, run identity, index health, endpoint responses, or semantic correctness.

**Recommended default and causal basis.** Run the focused reference validator for structure, uniqueness, frozen evidence, and expansion; then, for real graph work, verify version and `run.config`, health and diagnostics, query responses, source confirmation, and runtime evidence when behavior is claimed. Artifact correctness and investigation correctness are orthogonal: a perfectly validated guide can be misapplied to a stale run, while a healthy run cannot excuse a malformed evidence packet.

**Operating conditions and assumptions.** The reviewer names the claim class, selects the corresponding gate, records exact commands and summarized observations, and blocks only the failed layer rather than conflating every failure. Distinguish repository-reference QA from target-codebase graph QA and never let evidence from one layer certify the other.

**Failure boundary and alternatives.** The archive verifier is treated as proof of graph accuracy, health alone is treated as proof of coverage, a query returning HTTP success is treated as proof of interpretation, or validation output is not preserved. Bounded alternatives and recoveries: repair packet or heading structure for artifact failures, refresh or rebuild for index failures, inspect server logs and live API help for endpoint failures, and use code, tests, or traces for semantic failures.

**Counterexample, gotchas, and operational comparison.** Running against the seed path, sourcing the wrong run configuration, checking an assumed port, ignoring nonzero exits in piped commands, and reporting a pass without the command, path, and evidence counts. Good: focused-verify this file, then verify a live run and confirm a claimed gatekeeper in source. Bad: cite `verify_reference_generation.py` as proof of call reachability. Borderline: accept topology after health and coverage while marking branch behavior unresolved.

**Verification, evidence, and uncertainty.** Record command strings, working directory, exit status, version output, actual server URL and database URI, health and diagnostic summaries, entity keys, relevant response counts, direct-read spans, and unresolved model limits. The seed command is preserved, and the local corpus directly describes version, configuration, health, diagnostics, queries, incremental reindexing, and code-reading guardrails. No live Parseltongue process is part of this documentation task, so only artifact gates can run here; live-run commands remain procedures rather than observed passes.

**Second-order consequence.** Verification must follow the claim graph: each inference is valid only when every prerequisite gate from artifact integrity through semantic evidence has passed.

**Revision decision.** Add a layered gate matrix, exact evidence packet, pass and fail interpretation, recovery per layer, and the focused validator while retaining the original archive-stage command.

**Retained seed evidence.** The existing `verify_reference_generation.py --stage final` command remains intact as historical generation-stage evidence. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide whether Parseltongue should be used for the current task and which smallest workflow should be executed first. The seed routes tasks by theme mention and recommends local-first evidence, but it does not help an agent choose among orientation, backward tracing, forward tracing, architecture analysis, context budgeting, or direct reading.

**Recommended default and causal basis.** Classify the question before querying: orient an unfamiliar repository, trace backward from a symptom, trace forward from a candidate change, quantify architecture risk, select bounded context, or exit to direct semantic evidence. Question classification aligns endpoint direction with the decision and prevents broad graph exploration from consuming time without reducing uncertainty.

**Operating conditions and assumptions.** The task has a concrete entity or discoverable concept, the desired answer is structural, the run is verified, and the selected workflow includes a stop condition and source-reading handoff. Activate for structural codebase questions where Parseltongue 1.7.2 is available or can be safely prepared; do not activate solely because the task says graph or workflow.

**Failure boundary and alternatives.** The user needs exact values or temporal behavior, no stable entity can be found, parser coverage excludes the surface, the repository is already small and known, or graph setup costs exceed likely narrowing benefit. Bounded alternatives and recoveries: use targeted `rg` and file reads for known code, tests and debugger traces for behavior, logs and telemetry for incidents, ownership metadata for review routing, or a refreshed graph when staleness is the only blocker.

**Counterexample, gotchas, and operational comparison.** Using theme keywords as sufficient activation, running blast radius before orientation, selecting a forward trace for a symptom, overloading context before entity disambiguation, and continuing after the answer is already source-local. Good: a regression at `serialize_result` triggers reverse callers, convergence with a suspected normalizer, then direct code inspection. Bad: use fan-out to explain a bad runtime value. Borderline: use clusters to propose owners while checking CODEOWNERS separately.

**Verification, evidence, and uncertainty.** Record the initial question class, why graph use beats the nearest alternative, run and coverage checks, first endpoint selected, stop condition, narrowed files, direct confirmations, and whether the final answer changed. The endpoint reference directly maps questions to orientation, search, traversal, architecture, risk, context, and diagnostics; the workflow corpus supplies deeper combinations. Task value depends on repository size, indexing cost, entity quality, and user urgency, so activation should remain a documented judgment rather than an automatic keyword rule.

**Second-order consequence.** The fastest graph workflow is often the one that knows when to terminate; stopping after a decisive narrowing result protects both context and epistemic clarity.

**Revision decision.** Replace keyword routing with a decision tree covering prerequisites, endpoint direction, stopping rules, direct-evidence exits, and a compact activation audit.

**Retained seed evidence.** The local-first, explicit-gate, external-as-check, and evidence-label bullets remain preserved beneath the operational classifier. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide how a contributor should move from an unfamiliar codebase symptom or change request to a bounded, reviewable graph-assisted conclusion. The seed describes an unfamiliar-theme contributor choosing what to load and trust, but it stops before a concrete Parseltongue run, query sequence, decision point, and evidence handoff.

**Recommended default and causal basis.** Translate the request into one structural question, verify or prepare an isolated 1.7.2 run, orient before searching, resolve an entity, trace in the direction implied by the question, and read the narrowed source before recommending action. Each step removes a different uncertainty in order: environment identity, repository shape, entity identity, dependency topology, and finally program semantics.

**Operating conditions and assumptions.** The contributor has repository access, can preserve a run folder, can articulate a symptom or candidate change, and can stop once the graph has reduced the relevant code surface. Use this scenario for onboarding, code archaeology, refactor scoping, and structural bug hypotheses, while routing live production diagnosis to telemetry-first workflows.

**Failure boundary and alternatives.** The user expects a one-command diagnosis, the symptom is operational rather than structural, setup cannot be isolated, the entity surface is unparsed, or the trace grows without converging on a reviewable corridor. Bounded alternatives and recoveries: begin with logs or failing tests for operational symptoms, use direct search for a known small feature, ask for a stable symbol or file boundary, or defer graph setup until expected reuse justifies it.

**Counterexample, gotchas, and operational comparison.** Solving the wrong user question, presenting setup output as progress toward diagnosis, failing to capture the actual URL, following the first fuzzy search match, and handing the user a graph dump instead of a decision. Good: a contributor traces callers into a broken serializer, tests a suspected normalizer from the opposite direction, reads the overlap, and reports one guarded fix path. Bad: return all hotspots. Borderline: use a partial corridor but state missing dynamic edges.

**Verification, evidence, and uncertainty.** Preserve the initial request, structural reformulation, run facts, orientation snapshot, search candidates, chosen entity key, forward and reverse query summaries, source spans, rejected hypotheses, and final next action. The local corpus supplies every mechanical stage of this journey and multiple paired-direction workflows that convert broad repository questions into narrower source reads. Time-to-value varies with installation state, repository size, parser coverage, and symbol naming, so the journey has no defensible universal duration.

**Second-order consequence.** A successful user journey ends with less graph interaction than it began with; the output is a smaller decision surface, not an ever-richer graph.

**Revision decision.** Replace the generic role statement with a start-to-finish scenario, decision checkpoints, failure exits, evidence packet, and a concrete good, bad, and borderline outcome.

**Retained seed evidence.** The contributor role, starting uncertainty, trust decision, and theme-based opening trigger remain retained as the initial journey frame. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The new contributor or agent is starting from an unfamiliar theme and deciding whether this reference is the right tool and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `parseltongue_graph_workflow_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what to load, what to trust, what to avoid, and what evidence proves success.
Reference opening trigger: Open this file when the task mentions parseltongue graph workflow patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide whether to adopt a Parseltongue workflow unchanged, adapt it, avoid it, or stop after partial use for the task at hand. The seed offers adopt, adapt, avoid, and cost-of-being-wrong rows around source agreement, but it does not compare Parseltongue setup cost, graph reach, semantic limits, index freshness, or repeat-use value.

**Recommended default and causal basis.** Adopt when the run is healthy and the question is structural, adapt when coverage or workflow shape is partial, avoid when exact dynamic behavior dominates, and explicitly account for wrong-run and overreach costs. The relevant tradeoff is not graph versus no graph in the abstract; it is narrowing benefit and repeatability versus setup, staleness, parser gaps, and semantic confirmation cost.

**Operating conditions and assumptions.** The choice considers repository size, run readiness, expected reuse, entity stability, claim type, acceptable uncertainty, and a concrete next-best method. Apply tradeoffs per question and per claim rather than approving or rejecting the tool for an entire repository once.

**Failure boundary and alternatives.** Adopt is triggered merely by local/external agreement, adapt hides an invalid substrate, avoid means abandoning all evidence gathering, or cost of being wrong is expressed only as wasted time. Bounded alternatives and recoveries: use a lightweight dependency map, direct code search, language-server references, tests, runtime tracing, logs, ownership metadata, or a later refreshed Parseltongue run.

**Counterexample, gotchas, and operational comparison.** Sunk-cost bias after installation, overvaluing a visually broad blast radius, underpricing stale graph risk, adapting around a failed health gate, and ignoring the cost of false exclusion during deletion or migration. Good: adopt reverse and forward traces for a large refactor, then confirm guards in code. Bad: adapt a wrong-version run by caveating results. Borderline: use partial coverage to identify likely owners but not to certify deletion safety.

**Verification, evidence, and uncertainty.** Write a decision record with claim type, repository and run state, expected reuse, coverage evidence, chosen option, rejected alternatives, wrong-choice consequence, source-reading requirement, and stop or revisit trigger. The corpus provides strong examples for graph-supported debugging, migrations, seam discovery, deletion safety, and architecture analysis, alongside explicit modeling cautions. Setup and query costs are environment-dependent, and the sources provide no comparative benchmark against language servers or manual navigation.

**Second-order consequence.** Partial use is a first-class outcome: Parseltongue can validly narrow ownership or topology even when it cannot support the final behavioral claim.

**Revision decision.** Reframe adopt, adapt, avoid, and wrong-cost rows around run validity, structural fit, semantic depth, repeat value, and reversible partial use.

**Retained seed evidence.** The four original decision options and their verification prompts remain available in the retained table. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the parseltongue graph workflow patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong parseltongue graph workflow patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which evidence wins when Parseltongue policy, endpoint detail, workflow guidance, live run facts, or target-code behavior disagree. The seed labels the skill canonical and all three reference files supporting, but it does not specify conflict resolution among archived prose, live API help, run configuration, server output, and repository source.

**Recommended default and causal basis.** Use the skill for pinned-version policy, `run.config` and logs for this run's facts, live API documentation for exposed routes, detail references for workflow design, and target source or runtime evidence for program semantics. Authority changes with the question: static policy cannot reveal an auto-incremented port, a workflow cannot override a live route contract, and a graph service cannot determine unmodeled target behavior.

**Operating conditions and assumptions.** Each disputed claim is classified, compared only across relevant authorities, and either resolved by the highest direct evidence or retained as an explicit conflict requiring refresh. Use canonical and supporting labels for archived corpus organization, then incorporate live and target-code evidence by claim class without rewriting frozen source roles.

**Failure boundary and alternatives.** Canonical is interpreted as universally superior, live output silently rewrites archived policy, a supporting heuristic overrides endpoint behavior, or target code is ignored because the graph response appears complete. Bounded alternatives and recoveries: refresh the archived reference after confirmed drift, query API help, inspect server logs, reindex, read implementation source, or suspend the claim when two direct authorities remain inconsistent.

**Counterexample, gotchas, and operational comparison.** One global hierarchy for every claim, confusing recency with relevance, treating a generated config as aspirational input, allowing silent fallback behavior to pass as policy, and losing the version boundary during conflict resolution. Good: `run.config` determines the actual bound URL while the skill still governs the required version. Bad: a workflow sample fixes the port at 7777. Borderline: live API help differs from archived endpoints, so use the live route and record documentation drift.

**Verification, evidence, and uncertainty.** Maintain a conflict ledger containing claim class, competing evidence, timestamps or hashes, selected authority, rationale, effect on prior conclusions, refresh action, and unresolved uncertainty. The local sources explicitly distinguish ground truth, version policy, endpoint guidance, workflow catalogs, and code-reading limits, which supports a claim-relative hierarchy. The corpus cannot anticipate every live divergence or parser defect, so human judgment remains necessary when direct evidence conflicts at the same authority level.

**Second-order consequence.** A hierarchy is a routing function, not a prestige ladder; its purpose is to send each question to the evidence capable of answering it.

**Revision decision.** Add a claim-relative precedence matrix, conflict ledger, examples of legitimate overrides, same-level tie handling, and refresh obligations.

**Retained seed evidence.** The canonical skill row and three supporting detail rows, including paths and heading signals, remain exactly preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/SKILL.md | canonical primary source | Run Parseltongue 1.7.2; Ground Truth; Enforce Version Policy | What guidance, warning, or example should this source contribute to Parseltongue Graph Workflow Patterns? |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_bidirectional_workflows.md | supporting detail source | Parseltongue 1.7.2 Bidirectional Workflows; Workflow Index; 1) Meet-in-the-Middle Hypothesis Test | What guidance, warning, or example should this source contribute to Parseltongue Graph Workflow Patterns? |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_endpoints.md | supporting detail source | Parseltongue 1.7.2 Endpoints; Resolve the Base URL First; shellcheck source=/dev/null | What guidance, warning, or example should this source contribute to Parseltongue Graph Workflow Patterns? |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_flow_patterns.md | supporting detail source | Parseltongue 1.7.2 Flow Patterns; Modeling Limits; Pattern Index | What guidance, warning, or example should this source contribute to Parseltongue Graph Workflow Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what compact artifact should accompany every consequential Parseltongue investigation so another reviewer can reproduce the narrowing path and challenge its interpretation. The seed asks for a worked example with goal, decision boundary, and verification gate, but its three-field table is too small to reproduce a Parseltongue run or audit a graph-derived conclusion.

**Recommended default and causal basis.** Produce a graph investigation packet containing question and claim class, versioned run identity, orientation and coverage evidence, entity resolution, exact queries, summarized results, source confirmations, uncertainty, alternatives, and stop decision. Reproducibility requires both substrate facts and reasoning transitions; query output without its selected entity and model boundary cannot explain why a conclusion was reached.

**Operating conditions and assumptions.** The packet is small enough to review, includes only decision-relevant responses, links every conclusion to a query and source span, and records negative evidence without overclaiming absence. Require the full packet for changes, deletion, risk, and debugging claims; allow a lighter record for disposable exploratory orientation with no downstream decision.

**Failure boundary and alternatives.** The artifact is a raw transcript, omits actual URL or entity keys, stores only screenshots, discards rejected hypotheses, or reports a graph pattern without direct semantic confirmation where required. Bounded alternatives and recoveries: use a reduced orientation packet for simple onboarding, a migration choreography record for staged changes, an incident evidence packet for runtime symptoms, or direct source notes when graph use is not justified.

**Counterexample, gotchas, and operational comparison.** Copying huge JSON responses, leaking machine-specific paths unnecessarily, losing query order, recording labels but not parameters, and treating a context bundle as self-explanatory evidence. Good: a deletion-safety packet records reverse callers, forward callees, blast radius, dynamic-boundary caveats, and source confirmations. Bad: attach only hotspot output. Borderline: omit runtime proof for an architecture-only claim while stating that limit.

**Verification, evidence, and uncertainty.** Replay the packet from a clean shell against the named run, confirm query parameters and keys, compare summarized counts to responses, locate every cited source span, and ask whether the stop decision still follows. The local references provide all constituent operations, and the bidirectional workflows repeatedly combine orientation, paired traces, quantification, and direct follow-up. A universal packet size is not established; sensitive repositories may also require redaction or storage controls outside this reference.

**Second-order consequence.** The artifact should preserve the investigation's decision topology rather than every token, making review faster without erasing the path from question to evidence.

**Revision decision.** Expand the three seed fields into a reproducible packet schema, completion rules, redaction guidance, replay test, and claim-specific minimal variants.

**Retained seed evidence.** The original user goal, decision boundary, and verification gate rows remain retained as the packet's core. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: worked parseltongue graph workflow patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Parseltongue Graph Workflow Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide what observable behavior distinguishes a sound graph-assisted investigation from misuse and from a valid but incomplete structural result. The seed gives one generic good, bad, and borderline sentence about source loading, but none demonstrates actual Parseltongue direction choice, graph interpretation, or direct-code confirmation.

**Recommended default and causal basis.** Judge examples by substrate verification, question-to-endpoint fit, bounded interpretation, evidence preservation, source handoff, and an explicit stop or escalation condition. Contrasting examples teach decision boundaries more effectively than idealized commands because the same valid query can support, overstate, or fail a conclusion depending on its use.

**Operating conditions and assumptions.** The good case converges evidence from both directions, the bad case exposes a category error with consequences, and the borderline case states exactly which claim remains supportable. Use examples to teach graph-evidence reasoning across languages while preserving that parser coverage and dynamic features vary by target codebase.

**Failure boundary and alternatives.** Examples differ only in tone, the bad case is implausibly careless, the borderline case is secretly accepted as complete, or the recovery does not name stronger evidence. Bounded alternatives and recoveries: use a staged migration example for change planning, a boundary-leak example for architecture, a parse-frontier example for dynamic behavior, or an ownership-routing example for review assignment.

**Counterexample, gotchas, and operational comparison.** Making graph breadth look inherently good, omitting run verification from concise examples, treating a counterexample as proof the tool is useless, and failing to show the cost of a false negative. Good: intersect callers of a failing sink with callees of a suspected source, read the overlap, and falsify one branch hypothesis. Bad: delete a symbol because reverse callers are empty. Borderline: route reviewers from cluster and fan-in evidence while verifying ownership metadata.

**Verification, evidence, and uncertainty.** For each example, identify the question, run prerequisite, endpoint direction, graph observation, permissible inference, prohibited inference, direct evidence, consequence, recovery, and reviewer verdict. Meet-in-the-middle, deletion safety, boundary leak, ownership routing, and parse-frontier workflows are directly documented in the local corpus. The examples are schematic rather than executions against a supplied repository, so names and outcomes illustrate reasoning form rather than measured tool output.

**Second-order consequence.** Borderline examples are the strongest calibration device because they demonstrate that evidence can be useful without being sufficient for the final claim.

**Revision decision.** Replace generic contrasts with realistic meet-in-the-middle, deletion, and ownership cases that expose decisions, consequences, uncertainty, and stronger-evidence recovery.

**Retained seed evidence.** The original good, bad, and borderline source-boundary statements remain preserved before the richer operational contrasts. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Parseltongue Graph Workflow Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Parseltongue Graph Workflow Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Parseltongue Graph Workflow Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which signals show that Parseltongue reduces investigation uncertainty without increasing unsupported conclusions, and how failures should update the workflow. The seed names a better next decision, a source-map failure signal, and a refresh cadence, but none is defined sufficiently to measure graph-workflow usefulness or detect systematic overreach.

**Recommended default and causal basis.** Track time to first relevant entity, graph-to-source narrowing ratio, proportion of claims directly confirmed, ambiguous-entity corrections, stale-run detections, false-exclusion findings, and reviewer decision acceptance. Speed alone rewards broad but unsafe answers, while confirmation and correction metrics reveal whether topology actually improved the quality and efficiency of source reasoning.

**Operating conditions and assumptions.** Metrics are collected on comparable task classes, include denominator and evidence packet, distinguish orientation from diagnosis, and trigger a concrete workflow or corpus change. Measure assistance quality for repeated comparable investigations, not raw model quality, repository correctness, or universal Parseltongue accuracy.

**Failure boundary and alternatives.** Anecdotal wins become percentages, fewer tool calls is assumed better, large blast radius is treated as useful output, reviewer agreement replaces truth, or metrics never feed back into prompts and gates. Bounded alternatives and recoveries: use qualitative postmortems for low-volume work, measure query-to-source handoff completion, sample deletion and migration decisions, or track only gate failures until enough observations accumulate.

**Counterexample, gotchas, and operational comparison.** Survivorship bias from successful tasks, mixing repository sizes, measuring wall time without setup state, hiding unresolved dynamic edges, and optimizing the metric instead of the decision. Good: record that reverse tracing narrowed 80 candidate files to 6 and source reading rejected 2 graph hypotheses. Bad: claim 90-percent accuracy from reviewer approval. Borderline: report faster orientation while keeping semantic accuracy unmeasured.

**Verification, evidence, and uncertainty.** Define each metric, task cohort, numerator, denominator, collection point, reviewer role, acceptable uncertainty, adverse threshold, and the specific reference or workflow change triggered by a miss. The corpus supports measuring query direction, context selection, coverage, and direct-code handoff; the seed's leading and failure signals establish the intended decision-quality focus. No production dataset accompanies the sources, so thresholds and causal improvement claims must be learned locally rather than invented in this reference.

**Second-order consequence.** Corrections are valuable telemetry: a graph hypothesis disproved quickly by source can indicate successful narrowing, whereas an unrecorded contradiction teaches the system nothing.

**Revision decision.** Operationalize leading, adverse, and learning signals with denominators, cohort boundaries, feedback owners, and prohibition on unsupported benchmark claims.

**Retained seed evidence.** The better-decision leading indicator, source-map failure signal, and verifier-plus-refresh cadence remain intact as high-level anchors. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next task uses the reference to make a better decision with less ambiguity.
Failure signal: the reference remains a source map and never becomes an operating guide.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what minimum evidence must be present before a Parseltongue workflow reference or investigation packet can be called operationally complete. The seed checks role, decision options, hierarchy, artifact, examples, metrics, and adjacent routing, but it does not require verified run facts, model limits, query reproducibility, or source confirmation.

**Recommended default and causal basis.** Require all structural invariants plus version and run identity, orientation and coverage, question classification, entity resolution, exact query record, bounded inference, direct-code handoff, alternatives, stop condition, and unresolved uncertainty. Omitting any prerequisite can make a structurally polished packet irreproducible, misdirected, or semantically overconfident even when every original checklist item appears.

**Operating conditions and assumptions.** Each checkbox names an observable artifact or pass condition, nonapplicable items include a reason, failures block only dependent claims, and completion is rechecked after reconciliation edits. Apply the full list to consequential graph-assisted decisions, and document reduced variants explicitly rather than silently relaxing gates.

**Failure boundary and alternatives.** The list becomes a prose reminder, checkmarks lack evidence locations, semantic confirmation is waived without scope reduction, or a single verifier pass substitutes for claim-specific gates. Bounded alternatives and recoveries: use a lighter orientation checklist for disposable discovery, a stricter migration or deletion variant for high-blast-radius changes, or route runtime incidents to an observability evidence checklist.

**Counterexample, gotchas, and operational comparison.** Checking version without run identity, recording search text without selected key, counting query success without response relevance, omitting empty-result interpretation, and marking uncertainty complete merely because it is mentioned. Good: a refactor packet links every checked gate to config, response summary, or source span. Bad: all boxes are checked after only artifact validation. Borderline: skip runtime evidence for a topology-only conclusion and record the narrower scope.

**Verification, evidence, and uncertainty.** Audit every item against a location in the packet, rerun structural and uniqueness validators, replay sampled queries, inspect cited code, test exclusion cases, and require a reviewer to identify the final decision and stop condition. The source corpus directly supplies run, endpoint, workflow, diagnostic, context, and modeling-limit requirements; the seed checklist supplies the durable reference-level categories. Some repositories require additional language, confidentiality, or operational checks not represented in this tool-specific corpus.

**Second-order consequence.** Completeness is claim-dependent: a packet may be complete for ownership routing and simultaneously incomplete for deletion safety or runtime causality.

**Revision decision.** Extend every seed checklist category with evidence pointers, claim-dependent applicability, substrate and semantic gates, and a final reviewer replay check.

**Retained seed evidence.** All seven original checklist bullets remain preserved as top-level completion categories. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Parseltongue Graph Workflow Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to route when Parseltongue setup, structural graph analysis, exact code semantics, runtime behavior, repository history, or language-specific implementation becomes the dominant need. The seed points abstractly to parseltongue, graph, and workflow references without naming the capability gap that triggers a route or the evidence expected on return.

**Recommended default and causal basis.** Stay in this reference for graph investigation design; route to the pinned run skill for environment operations, endpoint references for route syntax, direct code tools for semantics, runtime diagnostics for execution, and domain references for implementation. Adjacent routing should cross an evidence boundary intentionally, adding a capability that the current reference lacks instead of merely changing vocabulary.

**Operating conditions and assumptions.** The unresolved question is named, the destination can answer it, a minimal handoff packet travels with the task, and the result returns with its evidence class and effect on the graph hypothesis. Use this router at clear capability limits and preserve ownership of the original graph packet; do not let adjacent guidance silently rewrite verified run facts.

**Failure boundary and alternatives.** Routing is triggered by keyword similarity, the next reference repeats the same source map, history evidence is asked to prove runtime state, or a handoff loses run and entity identity. Bounded alternatives and recoveries: use lightweight CLI dependency mapping when a persistent server is unjustified, language-server navigation for local references, repository-history capture for change rationale, or language-specific testing guidance for implementation proof.

**Counterexample, gotchas, and operational comparison.** Routing too early before orientation, routing too late after a model boundary is crossed, opening several adjacent references at once, and allowing different tools' entity identifiers to be conflated. Good: graph evidence finds a parse frontier, then a language-specific reference guides direct analysis and tests. Bad: route to generic graph prose for a stale-index failure. Borderline: use Git history to explain ownership while keeping reachability claims separate.

**Verification, evidence, and uncertainty.** Record trigger question, destination capability, handoff inputs, evidence returned, contradictions, resolved and unresolved claims, and whether the task should return, continue there, or stop. The local skill explicitly prefers graph tools for topology and direct reading for exact code, and its supporting references expose distinct endpoint and workflow roles. The exact adjacent file inventory can evolve independently, so routing is defined by capability and evidence type rather than a frozen list of filenames.

**Second-order consequence.** A good route changes the evidence modality; if the destination cannot answer a question the current workflow cannot, the handoff only adds context cost.

**Revision decision.** Replace generic neighboring-theme pointers with capability-gap triggers, minimal handoff fields, return criteria, and examples spanning direct code, runtime, history, and lightweight mapping.

**Retained seed evidence.** The original parseltongue, graph, and workflow adjacency prompts remain retained as broad route labels. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use the nearest language, workflow, agent, or documentation reference when the theme becomes concrete.
Adjacent reference 1: consider the parseltongue adjacent reference when the current task pivots away from parseltongue graph workflow patterns.
Adjacent reference 2: consider the graph adjacent reference when the current task pivots away from parseltongue graph workflow patterns.
Adjacent reference 3: consider the workflow adjacent reference when the current task pivots away from parseltongue graph workflow patterns.

## Workload Model

**Decision supported.** This section helps decide how much repository and investigation work one Parseltongue run and one agent context should handle before the task must be narrowed, refreshed, or split. The seed defines one theme, all mapped sources, and one downstream review as capacity, but it does not model isolated-run setup, indexing freshness, query fan-out, response size, context selection, or semantic follow-up.

**Recommended default and causal basis.** Reuse one verified isolated run per stable workspace state, process one governing question at a time, bound traversal depth and context output, and split independent systems or ownership questions into separate evidence packets. The service can answer many topology queries, but agent attention and graph freshness degrade when unrelated hypotheses, repositories, or change states share one investigation record.

**Operating conditions and assumptions.** Workspace identity is stable, freshness is checked after code changes, query depth follows the decision, outputs are summarized before context inclusion, and each packet has one accountable conclusion. Use workload controls to protect investigation coherence; administer process-level server capacity with measured operational data outside this reference.

**Failure boundary and alternatives.** Multiple repositories share assumed configuration, long-running changes outpace indexing, broad blast and smart-context calls become default, or several independent decisions are merged into a single final claim. Bounded alternatives and recoveries: refresh incrementally between change batches, build separate timestamped runs, use scoped queries and lower depth, delegate independent packets to sole owners, or abandon server setup for a small direct-read task.

**Counterexample, gotchas, and operational comparison.** Equating server capacity with review capacity, ignoring response truncation, parallel writers mutating the same run evidence, carrying stale entity keys after reindexing, and measuring workload only by source count. Good: one migration packet evaluates a bounded corridor against a refreshed run. Bad: a single context combines architecture, incident, deletion, and ownership questions across services. Borderline: reuse one run for sequential questions while rechecking health and freshness.

**Verification, evidence, and uncertainty.** Record workspace and code revision, run folder, last index event, question count, traversal depths, response sizes, selected context size, packet owner, source-reading effort, refresh points, and split decisions. The skill requires isolated run folders and supports reindexing, while endpoint guidance offers scoped queries, depth controls, context budgets, and diagnostics. The sources do not provide universal repository-size, token, latency, or concurrency limits, so capacity must be observed and bounded locally.

**Second-order consequence.** The scarce resource is not graph storage alone but synchronized evidence: every additional question increases the chance that run state, context, and conclusion drift apart.

**Revision decision.** Replace the source-count capacity model with run lifecycle, freshness, query-depth, context, ownership, and split boundaries plus observable pressure signals.

**Retained seed evidence.** The four original workload rows remain preserved as high-level usage, capacity, source-pressure, and artifact-pressure anchors. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Parseltongue Graph Workflow Patterns as a general reference operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | idiomatic reference selection and synthesis work where the reference must prevent generic advice and preserve evidence boundaries | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one theme, all mapped local sources, current external evidence when available, and one downstream task review | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Run Parseltongue 1.7.2; Ground Truth; Enforce Version Policy; Code Reading Preference; Flow Modeling Guardrail; Run Workflow; Parseltongue 1.7.2 Bidir | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked parseltongue graph workflow patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what reliability means for a graph-assisted reference and how strict documentation gates should be separated from sampled investigation outcomes. The seed sets 100-percent evidence labels, 18-of-20 routing accuracy, zero unsupported claims, and universal recovery paths, but it does not identify these as proposed acceptance targets or cover graph freshness and false exclusion.

**Recommended default and causal basis.** Enforce deterministic gates for provenance, unsupported high-impact claims, and recovery instructions; sample task routing and semantic confirmation separately; monitor stale-run and false-exclusion incidents without inventing a universal accuracy promise. Document structure can reasonably require complete compliance, while investigation correctness depends on repository coverage and must be measured from observed tasks with explicit denominators.

**Operating conditions and assumptions.** Each target names its unit, evidence collector, sample boundary, consequence of a miss, and whether it is a hard release gate, review sample, or learning signal. Use seed thresholds as review contracts or proposed sampling gates, never as published measurements of Parseltongue or agent accuracy.

**Failure boundary and alternatives.** 18 of 20 is reported as demonstrated accuracy, 100 percent labels imply semantic truth, zero unsupported claims hides unlabeled uncertainty, or recovery-path presence substitutes for testing recovery. Bounded alternatives and recoveries: retain strict per-artifact review rules, bootstrap outcome baselines with qualitative audits, increase sampling for high-risk deletion or migration uses, or suspend aggregate reporting until task labels stabilize.

**Counterexample, gotchas, and operational comparison.** Small-sample confidence theater, double-counting one investigation across metrics, excluding failed setup attempts, treating dynamic-edge misses as user error, and optimizing labels without improving evidence. Good: reject an unlabeled production claim while separately sampling whether route choices led to correct evidence. Bad: advertise 90-percent accuracy from the 18-of-20 target. Borderline: accept a topology claim with full provenance while semantic reliability remains out of scope.

**Verification, evidence, and uncertainty.** For every target, record definition, hard-or-sampled class, denominator, observed result, confidence caveat, failure examples, owner, corrective action, and retest window. The four seed targets directly express provenance, routing, unsupported-claim, and recovery concerns; local modeling limits justify adding freshness and exclusion monitoring. No evaluated task sample or incident history accompanies the corpus, so outcome rates and useful thresholds remain local hypotheses until collected.

**Second-order consequence.** Reliability improves when hard invariants and empirical outcomes are not collapsed; one protects artifact discipline while the other reveals model and workflow limits.

**Revision decision.** Classify each target, add graph freshness and false-exclusion signals, require denominators and miss handling, and prohibit claims of achieved rates without observations.

**Retained seed evidence.** The original four threshold rows remain exactly preserved and visibly labeled as seed acceptance targets. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failure class occurred, how far its effects propagate through an investigation, and what evidence is required before dependent work resumes. The seed covers source drift, generic advice, implicit decisions, and unsynthesized corpora, but it omits wrong-run identity, stale indexing, ambiguous entities, graph-model overreach, and incomplete direct evidence.

**Recommended default and causal basis.** Classify failures by substrate, query selection, entity identity, graph coverage, interpretation, semantic confirmation, or artifact integrity, then invalidate only conclusions downstream of the failed prerequisite. Precise failure localization prevents both unsafe continuation and wasteful full restarts; a malformed packet does not necessarily corrupt live queries, while a stale run invalidates every dependent trace.

**Operating conditions and assumptions.** The trigger is observable, affected claims are enumerated, mitigation changes evidence state, recovery is reverified, and recurrence produces a durable update to the checklist or source map. Use this table for investigation and reference failures; report reproducible Parseltongue implementation defects through the tool's own issue and diagnostic process.

**Failure boundary and alternatives.** All errors become stale context, a retry is prescribed before classification, partial query results are silently accepted, or a fixed document is assumed to repair conclusions produced from bad graph state. Bounded alternatives and recoveries: repair structural artifacts, resolve entity keys, narrow or switch endpoints, incrementally reindex, rebuild an isolated run, read code directly, or use runtime diagnostics for unmodeled behavior.

**Counterexample, gotchas, and operational comparison.** HTTP success with semantically empty results, stale config after process restart, fuzzy-search collisions, old entity keys after reindex, graph cycles mislabeled feedback execution, and source confirmation performed on a different revision. Good: an ambiguous entity invalidates only symbol-specific traces and is resolved before replay. Bad: retry the same blast query after discovering stale indexing. Borderline: keep cluster evidence for orientation while withdrawing a dynamic reachability claim.

**Verification, evidence, and uncertainty.** Capture failure class, first observable signal, run and code revision, affected packet fields and claims, mitigation, replay output, source or runtime confirmation, recurrence counter, and permanent prevention change. The skill and endpoint references provide diagnostics, configuration, reindex, search, and code-reading controls; flow guidance explicitly warns about approximation. New language parsers, server defects, and repository generation pipelines may create failure signatures absent from the archived guidance.

**Second-order consequence.** Failure blast radius should itself be traced: knowing which conclusions depend on a bad prerequisite is the documentation analogue of dependency analysis.

**Revision decision.** Retain the four generic rows and add failure layers, downstream invalidation rules, evidence-changing mitigations, replay requirements, and recurrence feedback.

**Retained seed evidence.** Source drift, generic advice, implicit decisions, and corpus-list failures remain preserved as cross-cutting categories. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| decision path remains implicit | reader cannot tell when to adopt, adapt, or avoid the pattern | add decision table, cost of being wrong, and adjacent-reference route |
| large corpus becomes list | many sources are indexed but not synthesized into ranked guidance | classify canonical, supporting, legacy, duplicate, and conflicting sources |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed Parseltongue operation deserves a retry, when investigation work must pause, and when the workflow should switch evidence modalities. The seed sensibly limits stale-evidence retries and stops work on red gates, but it does not define retry identity, evidence change, safe query replay, or how reindexing affects entity keys and conclusions.

**Recommended default and causal basis.** Retry only transient transport or freshness failures after changing an observable prerequisite, cap repeated attempts per failure class, replay from verified run identity, and stop graph work when substrate or model-fit gates remain red. A retry that does not change state is repetition, while uncontrolled continuation on stale or ambiguous evidence compounds invalid conclusions across later queries.

**Operating conditions and assumptions.** The failure is classified, retry precondition and budget are explicit, operations are read-only or safely refreshable, prior entity assumptions are revalidated, and success is measured beyond HTTP status. Apply these controls to agent-operated local Parseltongue 1.7.2 runs and documentation workflows, not as a generic distributed-system retry policy.

**Failure boundary and alternatives.** Semantic disagreement triggers the same query, reindex loops indefinitely, concurrent agents refresh one run, entity keys survive unchecked across rebuilds, or a retry budget is reset by rewording the error. Bounded alternatives and recoveries: switch to direct code reading, inspect server logs, use live API help, create a fresh isolated run, reduce traversal scope, defer to runtime tests, or escalate with the preserved evidence packet.

**Counterexample, gotchas, and operational comparison.** Automatic port changes after restart, stale shell variables, partial index updates, cached responses, non-idempotent helper scripts, and background processes that make a failed attempt appear recovered. Good: after a verified code change, perform one incremental refresh, re-resolve the entity, and replay the bounded query. Bad: rerun search ten times on a wrong server URL. Borderline: retry one transient timeout, then switch to direct reading if health stays uncertain.

**Verification, evidence, and uncertainty.** Record failure fingerprint, attempt number, changed prerequisite, command, run identity before and after, logs, health and coverage result, entity re-resolution, query semantic result, stop reason, and escalation destination. The local skill documents reindexing, configuration, diagnostics, and process lifecycle, while the seed establishes bounded retry, backpressure, checkpointing, and sole ownership. Safe retry counts and timeout policies depend on local process behavior and workload; the corpus does not define production-grade service SLOs.

**Second-order consequence.** Backpressure protects epistemic state as much as compute: pausing prevents later reasoning from normalizing an unresolved substrate failure.

**Revision decision.** Add retry fingerprints, evidence-change prerequisites, entity revalidation, concurrency ownership, semantic success criteria, and modality-switch escalation.

**Retained seed evidence.** The original classification, one-refresh retry, red-gate stop, checkpoint, and single-owner bullets remain intact. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which minimal observations must be captured so setup failures, query choices, graph interpretations, and later contradictions can be reconstructed. The seed records sources, verification, latency, reviewer decisions, signals, and compact audit evidence, but it lacks the run, index, entity, query, and code-revision context needed to explain a Parseltongue result.

**Recommended default and causal basis.** Log version, run folder, actual configuration, code revision, health and diagnostics, index freshness, coverage, entity resolution, query parameters, bounded response summaries, source confirmations, decisions, and unresolved risks. Without correlation across run state and claim state, a later reviewer cannot distinguish tool drift, repository drift, query error, or interpretive overreach.

**Operating conditions and assumptions.** Records use stable identifiers and timestamps, redact sensitive paths where necessary, summarize rather than dump responses, link claims to observations, and preserve errors and discarded hypotheses. Capture enough local evidence for reproducibility and review while avoiding secrets, full raw transcripts, and claims about production monitoring architecture.

**Failure boundary and alternatives.** Telemetry contains only success output, raw logs overwhelm the decision record, machine paths are exposed unnecessarily, timestamps have no code revision, or p95 numbers mix setup and review stages. Bounded alternatives and recoveries: use a lightweight packet for one-off orientation, a structured incident trace for server instability, version-controlled fixtures for repeatable endpoint tests, or direct source annotations when no run exists.

**Counterexample, gotchas, and operational comparison.** Watcher counters without logs, health from the wrong URL, response counts without query filters, missing empty-result semantics, inconsistent clocks, and observability that changes behavior through expensive unbounded calls. Good: correlate a stale reverse trace with code revision and last reindex event, then replay after refresh. Bad: attach server.log and call the case observable. Borderline: omit detailed timings for a qualitative architecture review while retaining causal evidence.

**Verification, evidence, and uncertainty.** Sample records and reconstruct the run, selected entity, query direction, response interpretation, source handoff, and final decision; reject packets with orphan claims or observations that cannot identify their producer. The skill explicitly calls for configuration, health, watcher, logs, and changed-symbol checks, and the endpoint reference provides diagnostics plus query surfaces. Retention, privacy, and centralized telemetry requirements depend on the host environment and are outside the local corpus.

**Second-order consequence.** Observability should make disagreement diagnosable: the goal is to locate the first divergence in substrate, query, or interpretation rather than merely prove activity.

**Revision decision.** Extend the checklist with run and code correlation, index and entity state, compact response schemas, error preservation, redaction, and reconstruction tests.

**Retained seed evidence.** The six original bullets on source loading, proof, timing, reviewer decisions, signals, and concise audit evidence remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to evaluate whether Parseltongue helps reviewers reach a correct next verification action efficiently without sacrificing evidence quality. The seed proposes source preservation and p95 under ten minutes for identifying a next action, but it does not define the timing boundary, task cohort, setup state, reviewer population, or baseline.

**Recommended default and causal basis.** Treat the ten-minute p95 as a candidate acceptance hypothesis, separate cold setup from warm investigation and source confirmation, compare like task classes, and require decision correctness and evidence completeness alongside elapsed time. A fast wrong route is not useful performance, while including installation in every sample can obscure the repeat-use value of a prepared graph workflow.

**Operating conditions and assumptions.** The benchmark fixes repository snapshot, task prompt, run state, reviewer role, start and stop events, context budget, correctness rubric, sample size, and treatment of timeouts and retries. Evaluate documentation and investigation workflow efficiency, not Parseltongue server throughput or production service latency without a separate load-testing design.

**Failure boundary and alternatives.** One successful run is labeled p95, unmatched manual and graph cohorts are compared, setup costs disappear, reviewer time ends before source confirmation, or slow failures are excluded. Bounded alternatives and recoveries: measure time to first relevant entity, time to bounded source set, reviewer effort, query count, or qualitative action clarity until enough samples exist for percentiles.

**Counterexample, gotchas, and operational comparison.** Cache and warm-run effects, learning between repeated tasks, repository-size confounding, parallel work hidden from wall time, cherry-picked tasks, and a target becoming an asserted result. Good: benchmark warm reverse-trace tasks separately and score the chosen next action against source evidence. Bad: announce p95 below ten minutes from the seed sentence. Borderline: report median narrowing time with no tail claim while the sample grows.

**Verification, evidence, and uncertainty.** Publish protocol, task cohort, raw durations, setup classification, failures, retries, action correctness rubric, evidence-completeness score, percentile calculation, baseline, and uncertainty before accepting the target. The seed directly states the proposed p95 and reviewer-action intent; local endpoints support concrete stages whose durations can be measured independently. No benchmark observations, sample size, hardware, repository cohort, or reviewer calibration is provided, so this reference cannot claim achieved performance.

**Second-order consequence.** The best performance unit is a verified decision transition, not a tool response, because endpoint latency may be negligible while interpretation dominates total effort.

**Revision decision.** Define the candidate target as unproven, split timing stages, add matched cohorts and correctness gates, expose percentile requirements, and offer low-sample alternatives.

**Retained seed evidence.** The p95-under-ten-minutes statement, leading indicator, failure signal, measurement packet, pass condition, and fail condition remain preserved as seed criteria. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require source-boundary preservation and p95 under 10 minutes for a reviewer to identify the next verification action.
Leading indicator to measure: the next task uses the reference to make a better decision with less ambiguity.
Failure signal to watch: the reference remains a source map and never becomes an operating guide.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when a single Parseltongue 1.7.2 run and evidence packet cease to be a sufficient model for the system or organizational question. The seed stops at multiple systems, ownership boundaries, unbounded discovery, production traffic, and large codebases, but it does not specify run partitioning, cross-repository edges, change velocity, or dynamic integration limits.

**Recommended default and causal basis.** Keep one run scoped to one coherent workspace snapshot, split independent repositories and owners, bound traversal and context, and use explicit cross-system contracts plus runtime telemetry for relationships the static graph cannot represent. Scaling a query over an incomplete model increases apparent coverage without adding missing deployment, message, reflection, generated, or organizational edges.

**Operating conditions and assumptions.** The system boundary is declared, each run has a revision and owner, cross-boundary claims cite independent evidence, packet summaries preserve provenance, and a coordinator reconciles only explicit interfaces. Apply this statement to analysis scope and evidence coordination, not to claims about maximum supported repository size or server throughput.

**Failure boundary and alternatives.** Separate services are merged by name, one graph is assumed to cover deployed topology, frequent changes outrun indexing, distributed agents write the same packet, or context compression drops uncertainty. Bounded alternatives and recoveries: federate per-repository packets manually, use service catalogs and distributed traces, analyze API schemas and queues, create a lightweight dependency inventory, or narrow to one migration corridor.

**Counterexample, gotchas, and operational comparison.** Entity-key collisions across runs, incompatible language coverage, hidden generated clients, asynchronous message edges, cross-repo version skew, and aggregate hotspots that erase ownership. Good: analyze each service in its own verified run and join findings at a documented API contract. Bad: use one blast radius to certify a distributed rollout. Borderline: infer likely cross-repo coupling from names while requiring contract and runtime confirmation.

**Verification, evidence, and uncertainty.** Record workspace partitions, revisions, language coverage, owners, cross-system evidence, indexing lag, query bounds, packet handoffs, unresolved dynamic links, coordinator decision, and explicit stop threshold. The local sources frame Parseltongue as a code graph with modeling limits, while the seed already recognizes ownership, context drift, large-codebase narrowing, and production-SLO boundaries. Actual service capacity, multi-repository support, and concurrency behavior are not benchmarked in the archived material and must not be inferred.

**Second-order consequence.** Scale failure often begins as evidence-identity failure: once a response cannot be tied to one workspace snapshot and owner, more graph depth reduces trust.

**Revision decision.** Add workspace partitioning, revision and owner identity, cross-system evidence requirements, dynamic-edge routing, coordination rules, and measurable stop triggers.

**Retained seed evidence.** The original multiple-system, ownership, distributed-agent, context-drift, and graph-narrowing boundaries remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Parseltongue Graph Workflow Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide when and how a future maintainer should search for changed Parseltongue guidance without letting search results silently rewrite pinned 1.7.2 evidence. The seed provides three generic web queries for official documentation, GitHub examples, and releases, but it does not specify refresh triggers, source acceptance criteria, version scoping, or reconciliation with live API truth.

**Recommended default and causal basis.** Refresh only on a documented trigger, begin with verified live API help and authoritative project sources, include the exact version and feature, archive accepted evidence, and reconcile every change claim against the frozen corpus. Search queries discover candidates rather than establish facts; version-aware acceptance and diff review prevent current or unofficial material from contaminating a pinned workflow.

**Operating conditions and assumptions.** The trigger names suspected drift, queries target a concrete route or behavior, primary sources outrank summaries, dates and versions are recorded, and the maintainer labels additions, supersessions, and unresolved conflicts. Use future searches to discover candidate updates for Parseltongue guidance, never as substitutes for live validation, versioned sources, or target-code evidence.

**Failure boundary and alternatives.** Routine browsing is presented as freshness proof, result snippets become citations, latest-version docs overwrite 1.7.2 behavior, absence of results proves feature absence, or query phrasing is mistaken for a test. Bounded alternatives and recoveries: use the running service's API documentation, inspect installed binary help, compare release artifacts, read source at a version tag, or retain the current uncertainty when authoritative evidence is unavailable.

**Counterexample, gotchas, and operational comparison.** SEO summaries, forks and mirrors, unstable `latest` pages, similarly named tools, undocumented redirects, generated API docs from another version, and search personalization. Good: search an exact endpoint plus version after live help diverges, then archive and reconcile the authoritative result. Bad: adopt a blog's newest command. Borderline: retain a community workaround as provisional external evidence pending reproduction.

**Verification, evidence, and uncertainty.** Record refresh trigger, exact queries, retrieval date, source ownership, version, archived location or hash, relevant excerpt summary, conflict analysis, live reproduction, changed claims, reviewer, and next trigger. The seed directly preserves three query categories, and the local skill makes version policy and live configuration central to trustworthy operation. This pass performs no browsing, so the queries are unexecuted maintenance aids and no external freshness conclusion follows from their presence.

**Second-order consequence.** A refresh process should maximize change detection while minimizing authority drift; the right output is a reconciled evidence diff, not a larger link collection.

**Revision decision.** Retain the three exact query rows and add trigger policy, version qualifiers, source ranking, archive and diff requirements, reproduction gates, and rejection examples.

**Retained seed evidence.** The official-docs, GitHub-repository, and release-notes query labels and texts remain unchanged in the original table. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | parseltongue graph workflow patterns official documentation best practices |
| `github_repository_query_phrase` | parseltongue graph workflow patterns GitHub repository examples |
| `release_notes_query_phrase` | parseltongue graph workflow patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how every consequential sentence should be labeled and combined so a reviewer can tell what was read, observed, inferred, tested, or left unresolved. The seed defines local, external, and combined labels, but it does not distinguish archived tool facts from live run observations, target-repository code facts, runtime evidence, or hypotheses generated from graph topology.

**Recommended default and causal basis.** Preserve the three seed labels, add live-run, target-code, runtime, and provisional-hypothesis classes in usage, and require combined conclusions to enumerate their prerequisites and model limits. Parseltongue investigations cross several evidence modalities whose authority differs by claim; explicit boundaries prevent a graph response from inheriting the certainty of source code or a public link.

**Operating conditions and assumptions.** Facts cite exact artifacts or observations, inferences identify inputs and reasoning scope, negative evidence states coverage limits, contradictions remain visible, and the final recommendation names stronger evidence still needed. Apply these labels to this reference and downstream Parseltongue packets while preserving exact frozen seed labels for compatibility.

**Failure boundary and alternatives.** Labels decorate paragraphs without traceability, combined inference hides disagreement, local archive facts are treated as current runtime observations, graph absence proves code absence, or uncertainty is detached from the decision it affects. Bounded alternatives and recoveries: split an overcombined statement into atomic claims, downgrade it to a hypothesis, gather live or source evidence, preserve conflicting interpretations, or decline the conclusion when no adequate modality exists.

**Counterexample, gotchas, and operational comparison.** Source-backed does not mean semantically sufficient, live does not mean version-correct, code presence does not mean execution, runtime occurrence does not prove all paths, and multiple weak sources do not become one strong fact. Good: local docs establish endpoint intent, live output establishes this run's response, code confirms a guard, and synthesis proposes a bounded refactor. Bad: call a blast radius a runtime call tree. Borderline: infer ownership from clusters while marking metadata confirmation pending.

**Verification, evidence, and uncertainty.** Sample every recommendation, trace each clause to evidence class and location, test that combined claims list prerequisites, inspect conflicts and negative evidence, confirm uncertainty changes action, and reject orphan assertions. The local corpus directly supports distinctions among policy, configuration, graph topology, modeling limits, and code-reading confirmation; the seed provides the foundational three labels. Evidence taxonomy cannot eliminate judgment about source quality or semantic sufficiency, and a real repository may require additional operational or organizational classes.

**Second-order consequence.** The most useful confidence statement is compositional: it explains which link in the evidence chain would change the recommendation if falsified.

**Revision decision.** Extend the three-label note with a claim ledger, live and target evidence classes, combination rules, conflict handling, negative-evidence cautions, and compositional confidence.

**Retained seed evidence.** The exact local-corpus, external-research, and combined-evidence definitions remain preserved verbatim at the end of the evolved section. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
