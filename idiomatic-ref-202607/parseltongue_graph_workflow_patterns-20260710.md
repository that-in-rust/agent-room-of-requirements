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

Role based opening scenario: The new contributor or agent is starting from an unfamiliar theme and deciding whether this reference is the right tool and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `parseltongue_graph_workflow_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what to load, what to trust, what to avoid, and what evidence proves success.
Reference opening trigger: Open this file when the task mentions parseltongue graph workflow patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the parseltongue graph workflow patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong parseltongue graph workflow patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/SKILL.md | canonical primary source | Run Parseltongue 1.7.2; Ground Truth; Enforce Version Policy | What guidance, warning, or example should this source contribute to Parseltongue Graph Workflow Patterns? |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_bidirectional_workflows.md | supporting detail source | Parseltongue 1.7.2 Bidirectional Workflows; Workflow Index; 1) Meet-in-the-Middle Hypothesis Test | What guidance, warning, or example should this source contribute to Parseltongue Graph Workflow Patterns? |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_endpoints.md | supporting detail source | Parseltongue 1.7.2 Endpoints; Resolve the Base URL First; shellcheck source=/dev/null | What guidance, warning, or example should this source contribute to Parseltongue Graph Workflow Patterns? |
| agents-used-monthly-archive/codex-skills-202603/run-parseltongue-1-7-2/references/parseltongue_1_7_2_flow_patterns.md | supporting detail source | Parseltongue 1.7.2 Flow Patterns; Modeling Limits; Pattern Index | What guidance, warning, or example should this source contribute to Parseltongue Graph Workflow Patterns? |

## Theme Specific Artifact

Theme specific artifact: worked parseltongue graph workflow patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Parseltongue Graph Workflow Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

Good example: Use Parseltongue Graph Workflow Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Parseltongue Graph Workflow Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Parseltongue Graph Workflow Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

Leading indicator: the next task uses the reference to make a better decision with less ambiguity.
Failure signal: the reference remains a source map and never becomes an operating guide.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

- The role scenario names the user, starting state, decision, and trigger for Parseltongue Graph Workflow Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

Adjacent reference guidance: Use the nearest language, workflow, agent, or documentation reference when the theme becomes concrete.
Adjacent reference 1: consider the parseltongue adjacent reference when the current task pivots away from parseltongue graph workflow patterns.
Adjacent reference 2: consider the graph adjacent reference when the current task pivots away from parseltongue graph workflow patterns.
Adjacent reference 3: consider the workflow adjacent reference when the current task pivots away from parseltongue graph workflow patterns.

## Workload Model

`combined_evidence_inference_note`: Treat Parseltongue Graph Workflow Patterns as a general reference operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | idiomatic reference selection and synthesis work where the reference must prevent generic advice and preserve evidence boundaries | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one theme, all mapped local sources, current external evidence when available, and one downstream task review | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Run Parseltongue 1.7.2; Ground Truth; Enforce Version Policy; Code Reading Preference; Flow Modeling Guardrail; Run Workflow; Parseltongue 1.7.2 Bidir | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked parseltongue graph workflow patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| decision path remains implicit | reader cannot tell when to adopt, adapt, or avoid the pattern | add decision table, cost of being wrong, and adjacent-reference route |
| large corpus becomes list | many sources are indexed but not synthesized into ranked guidance | classify canonical, supporting, legacy, duplicate, and conflicting sources |

## Retry Backpressure Guidance

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

Performance method: require source-boundary preservation and p95 under 10 minutes for a reviewer to identify the next verification action.
Leading indicator to measure: the next task uses the reference to make a better decision with less ambiguity.
Failure signal to watch: the reference remains a source map and never becomes an operating guide.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

Parseltongue Graph Workflow Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | parseltongue graph workflow patterns official documentation best practices |
| `github_repository_query_phrase` | parseltongue graph workflow patterns GitHub repository examples |
| `release_notes_query_phrase` | parseltongue graph workflow patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
