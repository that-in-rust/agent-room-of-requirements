## Section 001: Dependency Map Cli Patterns

### Question 01: What decision does this reference help make?
- **current_section_observation:** The title names a technique but does not help an operator decide whether a fast lexical file graph is sufficient, which code slice to inspect, or when semantic tooling is required.
- **supporting_reason:** A useful dependency map should reduce an orientation or impact question to ranked `file:start:end` candidates while preserving that extracted edges are hypotheses rather than compiler facts.
- **counterargument_or_limit:** A repository with dynamic registration, reflection, generated code, path aliases, or cross-language calls can make a lexical graph systematically incomplete.
- **assumptions_and_boundaries:** Use this reference for rapid repository orientation and bounded source selection; route exact call behavior, runtime wiring, and production dependency guarantees to language-aware tools and tests.
- **revision_decision:** Expand the opening into a fit decision plus a preflight-build-inspect-query-read-verify-escalate loop.
- **additional_insight_to_add:** The product of the workflow is a smaller evidence-backed reading set, not a claim that the repository has been fully indexed.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** No default states how to run the builder safely, interpret its artifacts, or move from file edges to code evidence.
- **supporting_reason:** Default to recording repository/query scope and Git state, selecting an explicit disposable output directory, running the current builder, reading tooling and summary first, ranking candidate files/symbols, reading exact spans, and validating decisive edges in source/tests/configuration.
- **counterargument_or_limit:** For a tiny repository or one known symbol, direct `rg` plus a few exact reads may be cheaper than generating ten artifacts.
- **assumptions_and_boundaries:** Build only when the map is likely to change candidate selection or blast-radius review; otherwise use the smallest direct probe.
- **revision_decision:** State a strong pointer-first workflow with an early no-build exit and explicit post-map verification.
- **additional_insight_to_add:** Summary-first reading constrains context before detailed inspection, while exact span reads prevent graph output from becoming another raw repository dump.

### Question 03: When does the default work well?
- **current_section_observation:** The title gives no fit conditions for languages, repository state, import style, or task type.
- **supporting_reason:** The installed builder works best on tracked files in its supported extension set, with conventional explicit imports/includes and questions about architecture hubs, nearby dependencies, or likely change surfaces.
- **counterargument_or_limit:** Even well-structured repositories can express important edges through manifests, build files, generated registries, tests, or runtime configuration the script does not scan.
- **assumptions_and_boundaries:** Supplement the graph with task-specific lexical/configuration probes and verify selected paths before implementation.
- **revision_decision:** Add positive fit criteria for orientation, ownership discovery, review planning, and rough blast-radius narrowing.
- **additional_insight_to_add:** Map usefulness depends on whether omitted edge mechanisms are peripheral to the question, not on an abstract accuracy percentage.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** No warning says that Git-mode inventory omits untracked files, unsupported extensions vanish, fallback symbols have one-line ranges, and resolver rules miss many aliases or dynamic edges.
- **supporting_reason:** Those omissions can rank the wrong hub or falsely reassure an agent that an affected file has no inbound dependency.
- **counterargument_or_limit:** An incomplete map can still be valuable when its blind spots are named and the task only needs candidate generation.
- **assumptions_and_boundaries:** Avoid definitive completeness language; escalate when a missing edge could reverse ownership, safety, migration, or test decisions.
- **revision_decision:** Add hard stop and escalation signals for unsupported languages, untracked work, dynamic wiring, exact call graphs, and security-critical impact analysis.
- **additional_insight_to_add:** False absence is more dangerous than a visible unresolved external edge because an empty result can look like proof unless coverage is audited first.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The title does not compare direct `rg`, ctags spans, structural search, language servers, SCIP indexes, compiler metadata, or persistent graph systems.
- **supporting_reason:** These alternatives trade startup cost, language coverage, semantic precision, persistence, query power, and operational complexity.
- **counterargument_or_limit:** Choosing the most precise available tool can waste setup time when a rough candidate list is enough.
- **assumptions_and_boundaries:** Start with the cheapest method that can answer the consequence-bearing question and escalate only when uncertainty remains material.
- **revision_decision:** Preview a precision ladder and defer detailed routing to the tradeoff and adjacent-reference sections.
- **additional_insight_to_add:** Hybrid use is often strongest: rough CLI artifacts locate a neighborhood, then language-aware queries adjudicate only the edges that affect action.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Likely traps include writing artifacts into an unintended tree, trusting tracked-only inventory, treating `external_ref_edges.tsv` as third-party truth, using fan counts as semantic importance, and reading imprecise fallback pointers as full definitions.
- **supporting_reason:** Each converts a best-effort implementation detail into an unsupported architecture conclusion.
- **counterargument_or_limit:** Explicit artifact metadata and sampled source checks make these outputs useful and reproducible despite their roughness.
- **assumptions_and_boundaries:** Record root, output path, tool availability, file coverage, edge cap, query, sampled checks, and unresolved mechanisms with every consequential result.
- **revision_decision:** Add opening cautions around mutation scope, inventory coverage, resolver semantics, ranking interpretation, and pointer bounds.
- **additional_insight_to_add:** Tool availability is part of data provenance because the same command can produce ctags spans on one machine and regex one-line pointers on another.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The title offers no example distinguishing useful orientation from graph theater.
- **supporting_reason:** Good use ranks three candidates and confirms their imports/tests; bad use declares an unlisted file unaffected; borderline use maps a TypeScript core but separately flags alias and untracked-code coverage gaps.
- **counterargument_or_limit:** A high-confidence candidate can still be wrong when runtime registration bypasses imports.
- **assumptions_and_boundaries:** Examples must show both positive evidence and the observation that would require another tool.
- **revision_decision:** Add concise good, bad, and bounded-partial examples in the opening and full fixtures later.
- **additional_insight_to_add:** A borderline map is successful when it narrows the next probe without pretending that unresolved wiring disappeared.

### Question 08: How can the important claims be verified?
- **current_section_observation:** No evidence chain connects generated TSV rows and pointers to real repository dependencies or a safe next edit.
- **supporting_reason:** Verify artifact existence and schema, reconcile tracked/supported file coverage, sample resolved and unresolved edges against source, bounds-check pointers, inspect candidate tests/configuration, and compare one material edge with a precise tool when available.
- **counterargument_or_limit:** Exhaustively verifying every edge defeats the purpose of a rough map.
- **assumptions_and_boundaries:** Sample by consequence and anomaly, then verify all edges directly relied upon for mutation or review scope.
- **revision_decision:** Establish artifact, coverage, edge, pointer, decision, and escalation gates.
- **additional_insight_to_add:** Verification should test whether the map changed the reading or action set correctly, not whether every row is globally complete.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local prose and scripts establish exact artifact names, extension filters, resolver branches, fallback behavior, and optional tooling, while public precedents were not refreshed.
- **supporting_reason:** Complete local reads support current-machine mechanics without establishing current external tool guarantees or repository-specific map quality.
- **counterargument_or_limit:** Script inspection alone does not exercise every filename, language construct, or tool-version branch.
- **assumptions_and_boundaries:** Present executable branches as current-local facts, actual run output as required operational evidence, and external links as unrefreshed historical pointers.
- **revision_decision:** Make source/version, environment, and inference boundaries explicit from the opening.
- **additional_insight_to_add:** Confidence should be attached separately to inventory coverage, symbol span, edge resolution, graph ranking, and the final code-level conclusion.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The title frames map generation as an endpoint and omits learning from recurrent false positives, missed edges, and candidate-selection failures.
- **supporting_reason:** Comparing map hypotheses with later source/test findings can reveal resolver rules, language coverage, or artifact diagnostics worth improving.
- **counterargument_or_limit:** Tuning a generic mapper around one unusual repository can reduce portability and increase maintenance.
- **assumptions_and_boundaries:** Promote repeated or high-consequence misses with fixtures and retain repository-specific supplements outside the generic script.
- **revision_decision:** Add a feedback path from verified map errors to resolver tests, coverage notes, and escalation policy.
- **additional_insight_to_add:** A mature rough mapper improves primarily by making uncertainty and omissions more observable, not by claiming to become a universal semantic index.
## Section 002: Source Evidence Mapping Table

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists duplicate archive generations and three unrelated public instruction/automation links without mapping inventory, symbol, edge, pointer, repository-state, or escalation claims to evidence that can establish them.
- **supporting_reason:** A source map must distinguish workflow intent, executable extraction logic, actual run artifacts, target-repository state, precise-tool evidence, and historical external precedents.
- **counterargument_or_limit:** A conceptual orientation question may not require reading every script branch or producing map artifacts.
- **assumptions_and_boundaries:** Retrieve only the evidence capable of changing coverage, candidate rank, edge confidence, mutation scope, or escalation.
- **revision_decision:** Expand the table with current installed skill, scripts, metadata, run artifacts, repository state, and explicit no-browse roles while preserving every seed row.
- **additional_insight_to_add:** The graph itself is downstream evidence; its authority cannot exceed the inventory and resolver code that produced it.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** All seed local rows appear equally current and all public rows are mislabeled as refreshed facts.
- **supporting_reason:** Default to current repository instructions and state, then the installed executable scripts, then actual run metadata/TSVs, with archive snapshots for lineage and public links retained only as unrefreshed leads.
- **counterargument_or_limit:** A repository may deliberately vendor and pin an archived mapper version.
- **assumptions_and_boundaries:** Use the complete pinned toolchain when explicit, record its hashes, and do not combine its prose with another builder silently.
- **revision_decision:** Add a claim-driven retrieval order and relabel external rows according to observed access status.
- **additional_insight_to_add:** Current behavior is defined by the script that runs plus its environment, not by the newest-looking copy of identical prose.

### Question 03: When does the default work well?
- **current_section_observation:** Local scripts and generated artifacts can directly answer how files, symbols, lexical references, resolved edges, graph caps, and pointers were produced.
- **supporting_reason:** This evidence stack works when the target root and tool versions are observable and the task accepts best-effort orientation.
- **counterargument_or_limit:** It cannot establish runtime calls, framework ownership, or language semantics absent from extraction.
- **assumptions_and_boundaries:** Pair material map claims with source/test/configuration reads and precise tooling when omission could alter action.
- **revision_decision:** Add scope and nonproof columns for every source family.
- **additional_insight_to_add:** Actual artifacts outrank generic workflow prose for what one run contained, while source code outranks artifacts for explaining systematic omissions.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A flat source list fails when archived precedent claims are treated as current external evidence, duplicate snapshots are counted as corroboration, or a summary rank is used without inspecting tooling and inventory.
- **supporting_reason:** These errors inflate confidence without adding independent support for repository-specific relations.
- **counterargument_or_limit:** Historical precedent remains useful for explaining the pointer-first and precision-ladder design.
- **assumptions_and_boundaries:** Keep historical rationale separate from current tool behavior and target-repository proof.
- **revision_decision:** Add duplicate-origin, stale-public, and derived-artifact conflict handling.
- **additional_insight_to_add:** Identical hashes across snapshots are one lineage fact, not three independent votes for correctness.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed omits `git status`, tracked-file inventory, map TSVs, command capability probes, code spans, tests/build files, LSP output, and runtime traces as evidence types.
- **supporting_reason:** Those sources trade generality, current-state specificity, semantic precision, reproducibility, and collection cost.
- **counterargument_or_limit:** Loading all of them defeats context minimization and can expose unrelated repository details.
- **assumptions_and_boundaries:** Add an evidence source only when it discriminates a live hypothesis or verifies a consequence-bearing claim.
- **revision_decision:** Add task-to-evidence routing and a stopping rule after the next action is supported.
- **additional_insight_to_add:** The strongest workflow alternates broad cheap evidence with narrow precise checks instead of collecting every source at one precision level.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Risks include path existence mistaken for complete read, shell syntax mistaken for successful extraction, tool presence mistaken for capability, untracked files omitted silently, and public URLs mistaken for current facts.
- **supporting_reason:** Each substitutes a nearby signal for the exact evidence needed to trust coverage or an edge.
- **counterargument_or_limit:** Hashes, syntax checks, and capability probes remain valuable reproducibility anchors when scoped correctly.
- **assumptions_and_boundaries:** Record source identity, hash, execution status, target root, output metadata, and claim limitation separately.
- **revision_decision:** Add provenance and invalidation requirements for prose, scripts, artifacts, repository state, and external leads.
- **additional_insight_to_add:** A valid shell script can still generate misleading output for a repository whose important files never enter `code_files.txt`.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No seed scenario shows source selection changing a map conclusion.
- **supporting_reason:** Good use checks Git/untracked coverage and script branch before reading edges; bad use cites the summary as architecture truth; borderline use follows a pinned archive tool and validates its output against current source.
- **counterargument_or_limit:** A summary can be enough to choose the first file for a low-consequence exploratory read.
- **assumptions_and_boundaries:** The final claim must stay at the level the evidence supports and name the next precision step.
- **revision_decision:** Add good, bad, and version-pinned examples tied to evidence precedence.
- **additional_insight_to_add:** The same artifact can be sufficient for navigation and insufficient for exclusion, so examples should name the decision being supported.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed map includes no existence, full-read, hash, syntax, capability, artifact-schema, edge-sample, or external-access gate.
- **supporting_reason:** Verify local hashes and complete reads, run shell syntax and exact capability probes, inspect run metadata, reconcile file coverage, and sample every map relation used in a decision.
- **counterargument_or_limit:** A no-write reference evolution cannot safely execute the builder into unauthorized locations.
- **assumptions_and_boundaries:** Inspect script behavior now and require an authorized isolated run for operational claims later.
- **revision_decision:** Add deterministic source checks plus runtime/artifact verification that remains pending until a map is actually built.
- **additional_insight_to_add:** Separating source verification from run verification prevents a reviewed script from being reported as if it successfully mapped the target repository.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Archive/current prose hashes, script bytes, syntax, extension filters, resolver branches, and current tool probes are known; public link content and target-repository map quality were not observed.
- **supporting_reason:** Local inspection supports mechanics while the no-browse/no-map boundary limits ecosystem and operational claims.
- **counterargument_or_limit:** Future script or environment changes can invalidate current observations even if prose remains identical.
- **assumptions_and_boundaries:** Bind every current-local claim to hashes/capability capture and every operational conclusion to a future run artifact.
- **revision_decision:** Add a source-status ledger and explicit pending states.
- **additional_insight_to_add:** Confidence decays independently for script bytes, tool branch, repository inventory, extracted relation, and code-level interpretation.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats sources as a bibliography rather than dependencies in an evidence-producing pipeline.
- **supporting_reason:** Inventory logic affects every downstream artifact, symbol extraction affects pointer confidence, resolver changes affect graphs, and pointer parsing affects final reads.
- **counterargument_or_limit:** A full provenance graph may be excessive for casual orientation.
- **assumptions_and_boundaries:** Track dependency links for claims that exclude files, rank hubs, or justify edits; keep simple navigation lightweight.
- **revision_decision:** Add targeted invalidation from source/tool changes to derived artifacts and conclusions.
- **additional_insight_to_add:** Evidence maintenance becomes cheaper when a changed resolver invalidates edge conclusions without unnecessarily reopening stable inventory or pointer-format guidance.

## Section 003: Pattern Scoreboard Ranking Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed scoreboard helps an operator decide which dependency-mapping habits deserve default status, but its three repeated identifiers and unexplained numeric scores do not distinguish workflow priority from empirical performance.
- **supporting_reason:** A useful ranking must tell the reader what to do first when time is constrained: establish inventory coverage, keep evidence classes separate, and couple conclusions to checks before investing in richer visualization.
- **counterargument_or_limit:** A compact table can still function as a memory aid for readers who already know how the scores were assigned.
- **assumptions_and_boundaries:** Treat the inherited 95, 91, and 88 values as editorial priority metadata within this reference, not as measured probabilities, benchmark results, or universal utility coefficients.
- **revision_decision:** Recast the scoreboard as an ordered decision aid that names each control, its default action, the failure it prevents, and the condition that can lower its priority.
- **additional_insight_to_add:** Ranking workflow controls explicitly prevents visually impressive graph output from outranking the less visible coverage and validation work on which that output depends.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The highest-value default is to rank coverage-first mapping above graph interpretation because omitted tracked files silently corrupt every later centrality, hotspot, and blast-radius conclusion.
- **supporting_reason:** The builder's Git inventory branch excludes untracked and ignored paths, supports only a fixed extension list, and can fall back to start-line-only regex symbols, so a successful command is not proof of representative coverage.
- **counterargument_or_limit:** For a tiny, single-language repository whose tracked files and static imports are already known, exhaustive coverage auditing may add little beyond a quick count comparison.
- **assumptions_and_boundaries:** Apply the default whenever the map will support code edits, review findings, ownership decisions, or claims that an entity has no callers or dependencies.
- **revision_decision:** Put Coverage Before Graph Interpretation at the top of the evolved ranking, followed by evidence separation, pointer-first retrieval, sampled relation verification, and precision escalation.
- **additional_insight_to_add:** The ranking should encode dependency order as well as importance, because a lower-ranked verification step can invalidate conclusions derived from every higher-level graph view.

### Question 03: When does the default work well?
- **current_section_observation:** A coverage-led qualitative scoreboard works well during first-pass orientation, constrained reviews, migration scoping, and incident triage where the team needs a fast map without pretending it is a compiler-grade model.
- **supporting_reason:** These tasks benefit from cheap inventory and lexical relations, while explicit confidence labels let operators reserve source reads and specialized analyzers for the few paths that affect a decision.
- **counterargument_or_limit:** The ordering is less useful after a language-aware index already supplies complete symbols, resolved imports, generated-code policy, and reproducible provenance.
- **assumptions_and_boundaries:** The repository should be readable locally, the operator should be able to inspect generated TSV or Markdown artifacts, and sampling should include at least one important positive edge and one suspicious absence.
- **revision_decision:** Add a Works Well column that ties each ranked control to concrete tasks instead of implying identical value in every environment.
- **additional_insight_to_add:** A qualitative ranking accelerates work most when it narrows expensive verification to consequential claims rather than turning every heuristic edge into an equal-cost investigation.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The default ranking becomes wrong when the task requires semantic call resolution, runtime dependency behavior, macro expansion, reflection, framework injection, or security-grade completeness that lexical imports cannot establish.
- **supporting_reason:** No ordering of heuristic controls can recover information the extraction model never observes, and repeated sampling cannot prove the absence of dynamic or generated relationships.
- **counterargument_or_limit:** The rough map may still identify candidate files or vocabulary before the authoritative analyzer runs, provided its claims remain explicitly provisional.
- **assumptions_and_boundaries:** Escalate rather than reorder the scoreboard when false negatives could authorize deletion, weaken an access boundary, miss a migration consumer, or misstate production reachability.
- **revision_decision:** Give every ranked item a demotion or escalation condition, including a terminal condition that routes the task to language-aware or runtime evidence.
- **additional_insight_to_add:** A scoreboard is trustworthy only if it can recommend abandoning its own method; otherwise ranking becomes a mechanism for defending the available tool rather than serving the decision.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Relevant alternatives include manual directory reading, repository-native build or query tools, language-server indexes, compiler metadata, specialized graph analyzers, runtime tracing, and ownership databases.
- **supporting_reason:** Manual reading maximizes semantic nuance but scales poorly; lexical mapping is cheap and broad but approximate; semantic analyzers improve precision at setup cost; runtime traces expose actual executions but only for exercised paths.
- **counterargument_or_limit:** Combining every alternative creates operational overhead and can obscure the question under excessive evidence collection.
- **assumptions_and_boundaries:** Select the least expensive method that can falsify the consequential claim, and combine methods only when their blind spots are materially different.
- **revision_decision:** Add an alternatives row outside the numeric inheritance that compares quick map, semantic index, runtime observation, and direct source verification by cost and claim strength.
- **additional_insight_to_add:** The best score is task-relative: lexical breadth can outrank semantic depth for discovery, while semantic or runtime evidence must outrank lexical convenience for authorization and absence claims.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The most dangerous scoreboard failure is treating an editorial number as calibrated evidence, followed by ranking graph shape before inventory coverage and accepting unresolved or absent edges as architectural facts.
- **supporting_reason:** Numeric presentation invites false precision, while truncated graph rendering, unsupported extensions, Ctags fallback, aliases, dynamic loading, and resolver misses can each change apparent importance without changing the code's real behavior.
- **counterargument_or_limit:** Removing all numbers would lose continuity with the seed and make it harder to compare this month's reference with the archived version.
- **assumptions_and_boundaries:** Preserve inherited numbers only with an explicit legend and never calculate percentages, thresholds, or trend claims from them without a documented scoring procedure.
- **revision_decision:** Add failure signals beside each rank and state that ties or small score gaps have no statistical meaning.
- **additional_insight_to_add:** The graph edge cap can make presentation completeness diverge from artifact completeness, so ranking must direct users to TSV counts before they judge hubs from the rendered view.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good use ranks a coverage audit first, verifies a sampled high-impact edge in source, and labels the resulting hub claim provisional; a bad use cites score 95 as a 95-percent confidence guarantee.
- **supporting_reason:** The good example preserves the chain from tracked inventory through extraction to interpretation, whereas the bad example converts undocumented editorial metadata into unsupported precision.
- **counterargument_or_limit:** A borderline quick navigation task may reasonably skip formal sampling when the map only supplies a file pointer and no behavior or absence claim is communicated.
- **assumptions_and_boundaries:** Classify an example by the consequence of error: reversible file discovery permits lighter checks, while edits, deletions, security assertions, and ownership changes require stronger corroboration.
- **revision_decision:** Include a compact example matrix with acceptable, unacceptable, and conditional uses of the ranked controls.
- **additional_insight_to_add:** Borderline cases become safe when the output states the next verification action, making provisional convenience visible instead of letting it harden into undocumented certainty.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Scoreboard utility can be checked through process conformance and sampled accuracy rather than by assuming the inherited numeric order is self-validating.
- **supporting_reason:** Operators can compare repository inventory with `all_files.txt`, `code_files.txt`, and `files.tsv`, inspect extraction metadata, count full relation rows versus rendered edges, resolve selected pointers, and confirm claims in code or an authoritative tool.
- **counterargument_or_limit:** A few samples estimate obvious defects but cannot establish complete recall across an unfamiliar repository.
- **assumptions_and_boundaries:** Record commands, artifact hashes or timestamps, sample selection rationale, observed mismatches, and the decision each check supports so another operator can reproduce the evidence.
- **revision_decision:** Attach a verification gate to every scoreboard row and require stronger checks when a ranking informs irreversible or high-impact action.
- **additional_insight_to_add:** Tracking mismatch classes over repeated runs can eventually support a real local score, but such a metric must remain separate from the inherited editorial values until its denominator and sampling policy are stable.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is known from the frozen scripts that inventory, extension support, Ctags fallback, lexical resolution, optional rendering, and edge caps have specific behavior; the relative value scores remain editorial judgment.
- **supporting_reason:** Script bytes and successful capability probes are directly inspectable, while no supplied benchmark, rubric, sample population, or longitudinal outcome data explains why one pattern received 95 instead of 91.
- **counterargument_or_limit:** Experienced maintainers may have tacit production evidence that the archive did not preserve.
- **assumptions_and_boundaries:** State confidence at the claim level: high for observed implementation mechanics, medium for generally useful workflow ordering, and low for portability of exact numeric rankings.
- **revision_decision:** Add an Evidence Basis field and a confidence legend that separates source-backed facts, operational inference, and editorial prioritization.
- **additional_insight_to_add:** Preserving uncertainty increases the table's practical authority because readers can challenge the ranking without disputing verified tool behavior or discarding useful defaults.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed's three controls are not independent preferences; they form a causal chain in which source mapping enables evidence separation and evidence separation enables meaningful verification gates.
- **supporting_reason:** A check cannot validate an undefined evidence boundary, and a boundary cannot be applied reliably when the operator has not identified which local scripts, artifacts, repository state, and source reads produced the claim.
- **counterargument_or_limit:** A strictly linear chain can understate feedback loops, because verification failures should send the operator back to revise inventory assumptions or extraction settings.
- **assumptions_and_boundaries:** Model the ranking as an ordered loop with explicit backtracking rather than as a one-way maturity ladder or a universal scorecard.
- **revision_decision:** Evolve the table into a control stack and add a stop condition, a feedback rule, and a task-sensitive priority override.
- **additional_insight_to_add:** Once ranking is understood as dependency-aware control flow, the most valuable item is often the one that detects when an earlier premise failed, not the item with the most impressive standalone output.

## Section 004: Idiomatic Thesis Synthesis Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed thesis chooses an evidence-loading order but does not state the more consequential decision: whether a rough CLI map is adequate for orientation, needs direct source confirmation, or must yield to a higher-precision method.
- **supporting_reason:** Local skill prose, executable scripts, current repository state, generated artifacts, and source reads answer different questions; combining them without a sufficiency rule can make convenient evidence appear authoritative.
- **counterargument_or_limit:** A one-sentence thesis is easier to remember and may be enough for an experienced operator who already applies claim-specific verification.
- **assumptions_and_boundaries:** The evolved thesis must remain a compact governing rule while making its scope explicit for static discovery, behavior claims, absence claims, and high-consequence changes.
- **revision_decision:** State that rough maps are hypothesis generators whose conclusions become actionable only through coverage checks, pointer-resolved source evidence, and consequence-proportional escalation.
- **additional_insight_to_add:** The central decision boundary is evidence sufficiency, not tool preference; the same map can be adequate for navigation and inadequate for deletion approval in the same session.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is local-first, artifact-aware, pointer-first orientation followed by direct verification of every claim that can change code or architecture.
- **supporting_reason:** Current local scripts reveal actual inventory and extraction behavior, compact artifacts reduce context cost, and source reads expose semantics that lexical filenames, symbols, and edges cannot encode.
- **counterargument_or_limit:** Public documentation or a repository-native semantic tool may deserve first position when the local helper is stale, incompatible, or clearly outside the target language.
- **assumptions_and_boundaries:** Local-first means inspect current executable reality before relying on historical prose; it does not mean local heuristics outrank authoritative compiler or runtime evidence.
- **revision_decision:** Replace the seed's three-source sequence with a staged default: preflight, build, coverage audit, compact query, pointer read, claim verification, and escalation.
- **additional_insight_to_add:** A staged default minimizes both context use and false confidence because evidence becomes more expensive only as the decision becomes more consequential.

### Question 03: When does the default work well?
- **current_section_observation:** The thesis works well for repositories with conventional tracked source files, mostly static imports or includes, inspectable text, and tasks centered on orientation or candidate discovery.
- **supporting_reason:** Under those conditions the builder's finite extension inventory and lexical resolver can cheaply reveal directories, likely entry points, import neighborhoods, and spans worth reading.
- **counterargument_or_limit:** Even a conventional repository can contain generated registries, build-script wiring, feature flags, or tests outside the mapped extension set.
- **assumptions_and_boundaries:** Success means reducing the search space and producing reproducible pointers, not proving complete semantics or runtime reachability.
- **revision_decision:** Add explicit fit criteria and name reversible navigation, review preparation, and first-pass refactor scoping as appropriate uses.
- **additional_insight_to_add:** The method's strongest benefit is decision compression: it spends broad cheap evidence to identify the narrow expensive evidence that deserves human or semantic inspection.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The thesis fails if rough-map output is treated as a complete program model in codebases dominated by dynamic imports, reflection, macros, generated code, framework injection, runtime registration, or unsupported languages.
- **supporting_reason:** Those relationships are absent from lexical import rows even when the builder exits successfully, so missing edges can reflect the observation model rather than the architecture.
- **counterargument_or_limit:** A partial map may still surface useful filenames and vocabulary before a specialized tool is available.
- **assumptions_and_boundaries:** It becomes the wrong primary method when false negatives can authorize deletion, understate a security boundary, omit a migration consumer, or misdiagnose production behavior.
- **revision_decision:** Put an explicit stop rule in the thesis: do not promote heuristic absence or centrality into a consequential conclusion without stronger evidence.
- **additional_insight_to_add:** The most hazardous failure is graceful incompleteness, because plausible artifacts and a zero exit status can conceal the fact that the important relation class was never observable.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The decision space includes direct manual reading, repository-native commands, language servers, compiler or build-system graphs, specialized static analyzers, and runtime traces in addition to the rough CLI map.
- **supporting_reason:** Each alternative exchanges setup cost, breadth, semantic precision, reproducibility, runtime representativeness, and context consumption differently.
- **counterargument_or_limit:** Selecting the theoretically strongest tool can delay a simple navigation task and create more setup work than the decision warrants.
- **assumptions_and_boundaries:** Prefer the cheapest evidence source that can materially falsify the pending claim, then layer complementary sources when their blind spots differ.
- **revision_decision:** Add a claim-to-evidence ladder rather than presenting external research as the single second step after local retrieval.
- **additional_insight_to_add:** Public precedents should shape method design, while current local artifacts and authoritative project tools should decide facts about the repository under inspection.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Major thesis-level traps are conflating source categories, overlooking tracked-only inventory, assuming every extension is supported, ignoring extraction fallback, reading a capped graph as complete, and treating unresolved edges as external dependencies.
- **supporting_reason:** Each trap breaks a different link between repository state and the final recommendation, so a single generic disclaimer cannot contain their combined effect.
- **counterargument_or_limit:** Listing every implementation caveat inside the governing thesis would make it unreadable and defeat its role as a memory anchor.
- **assumptions_and_boundaries:** Keep the thesis concise, then route readers to a small set of non-negotiable preconditions and escalation signals nearby.
- **revision_decision:** Pair the governing statement with a compact claim-strength ladder and a falsification checklist.
- **additional_insight_to_add:** A rough map should carry its observation contract alongside its output, much like a benchmark carries workload and environment metadata.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good application uses map rows to choose source spans and verifies a proposed boundary; a bad application equates no incoming row with no caller; a borderline application uses an unverified pointer only to navigate.
- **supporting_reason:** These examples separate reversible discovery from claims that can alter implementation, architecture, or risk posture.
- **counterargument_or_limit:** Consequence varies by project, so a navigation hint in one repository may become operationally important in another if it drives an urgent incident response.
- **assumptions_and_boundaries:** Judge examples by both claim type and action reversibility, not solely by whether the tool produced an artifact.
- **revision_decision:** Add scenario pairs showing how the same observation supports a candidate statement but not a completeness statement.
- **additional_insight_to_add:** Prefixing conclusions with candidate, observed, verified, or unresolved creates a lightweight evidence type system that reduces accidental promotion of weak claims.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The thesis can be verified operationally by reconstructing the chain from repository inventory through extraction metadata, relation rows, resolved pointers, and authoritative checks for consequential claims.
- **supporting_reason:** Each stage offers a concrete falsification point: missing files, weak spans, resolver mismatches, stale line ranges, or contradictory semantic and runtime evidence.
- **counterargument_or_limit:** Reproducing the complete chain for every low-impact lookup would consume more time than it saves.
- **assumptions_and_boundaries:** Scale evidence retention with decision cost while always recording enough state to explain why the selected method was considered sufficient.
- **revision_decision:** Define minimum verification by claim class: pointer resolution for navigation, source confirmation for behavior, and semantic or runtime corroboration for absence and reachability.
- **additional_insight_to_add:** Verification failures should update the map's local reliability profile and future tool choice, not merely correct the single conclusion that happened to expose the defect.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The frozen local files establish current script mechanics and historical guidance, while repository-specific completeness, relation accuracy, and optimal escalation points remain contingent until an actual authorized run is inspected.
- **supporting_reason:** Static reading can prove which branches and extensions the scripts implement but cannot prove which branch a future machine takes or how well lexical relations match an unseen target codebase.
- **counterargument_or_limit:** Existing production experience may justify a strong default even when this reference does not preserve its measurements.
- **assumptions_and_boundaries:** Label implementation facts as known, general workflow advice as reasoned default, public URLs as unrefreshed pointers, and project-level accuracy as unmeasured until sampled.
- **revision_decision:** Add a known-versus-conditional ledger immediately beneath the synthesis statement.
- **additional_insight_to_add:** Confidence must attach to individual claims rather than the tool as a whole, because inventory accuracy, symbol-span quality, edge precision, and semantic interpretation can differ sharply in one run.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed frames retrieval as a sequence, but the deeper pattern is an adaptive evidence pipeline whose next step depends on what the previous stage failed to establish.
- **supporting_reason:** Coverage mismatch should return the operator to inventory policy, an invalid pointer should reopen extraction mode, a false edge should challenge the resolver, and semantic disagreement should trigger precision escalation.
- **counterargument_or_limit:** Adaptive loops are harder to teach than a fixed recipe and can create indecision if stop conditions are vague.
- **assumptions_and_boundaries:** Define explicit sufficiency and escalation criteria so feedback changes the method without producing endless analysis.
- **revision_decision:** Express the final thesis as a bounded loop with provisional output states and a clear terminal requirement for consequential action.
- **additional_insight_to_add:** This loop turns tool limitations into routing information: each mismatch identifies the next evidence source instead of merely lowering an undifferentiated confidence score.

## Section 005: Local Corpus Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists four archive paths but does not help the reader decide which local file governs historical intent, current executable behavior, public-pointer context, agent discovery metadata, or repository-specific results.
- **supporting_reason:** The archived skill prose, precedent notes, installed scripts, metadata, generated artifacts, and direct target source have different authority and invalidation rules even when they discuss the same workflow.
- **counterargument_or_limit:** A flat list is easier to scan when all the reader needs is a path to begin browsing.
- **assumptions_and_boundaries:** The evolved map should preserve every seed row while distinguishing duplicate content, current sources outside the repository, and artifacts that do not exist until an authorized run.
- **revision_decision:** Convert the corpus list into a retrieval matrix with evidence class, claim authority, hash or freshness rule, dependency, and read trigger.
- **additional_insight_to_add:** Source routing prevents a common category error: using stable historical prose to answer a current implementation question that only the installed script or run metadata can settle.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default is to read historical skill and precedent material once for intent, then prefer the current hashed scripts and current environment probes for mechanics, followed by generated artifacts and direct source for repository claims.
- **supporting_reason:** All three observed skill copies are byte-identical and all three precedent copies are byte-identical, while the scripts uniquely define inventory, extraction, resolver, rendering, and pointer behavior.
- **counterargument_or_limit:** If the task is specifically to reconstruct a past agent's instructions, the dated archive copy rather than the current installation is the authoritative object.
- **assumptions_and_boundaries:** Choose authority according to the temporal question and never let a current file silently rewrite what a historical snapshot contained.
- **revision_decision:** Add a default retrieval order and a temporal-authority column to each local source family.
- **additional_insight_to_add:** Hash equality allows identical archive months to collapse into one semantic read while retaining every path for provenance and audit continuity.

### Question 03: When does the default work well?
- **current_section_observation:** Role-based local retrieval works well when the operator needs reproducible orientation, can access the installed skill directory, and will generate map artifacts in an authorized disposable location.
- **supporting_reason:** Stable hashes make duplicate detection cheap, executable scripts expose actual branches, and artifacts bind general mechanics to the selected repository revision and environment.
- **counterargument_or_limit:** A remote reviewer or packaged environment may have the repository archive but not the same user-level installed skill path.
- **assumptions_and_boundaries:** Missing current-local files must be reported and replaced by an explicitly named snapshot rather than inferred from archive prose.
- **revision_decision:** Document both repository-contained archive sources and machine-local current sources, with fallback behavior when one family is unavailable.
- **additional_insight_to_add:** The source map doubles as a portability diagnostic because it reveals which conclusions depend on workspace content and which depend on one operator's machine state.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The local corpus hierarchy fails when it is treated as sufficient evidence for target-code semantics, current upstream tool behavior, or a map run that has not actually occurred.
- **supporting_reason:** Guidance files describe a method, scripts define possible behavior, and environment probes reveal capabilities, but none substitutes for generated rows and direct source in the repository being analyzed.
- **counterargument_or_limit:** Static script inspection can still establish hard implementation bounds before a run, such as the finite extension list and the existence of a regex fallback.
- **assumptions_and_boundaries:** Separate potential behavior known from code from selected behavior known from run metadata and from semantic truth known through target evidence.
- **revision_decision:** Add explicit not-sufficient-for annotations to every source role.
- **additional_insight_to_add:** A corpus map becomes dangerous when completeness of documentation is mistaken for completeness of observation; the latter is a property of a particular run and repository state.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include rereading every duplicate snapshot, trusting only the newest file by date, relying solely on Git history, or building a formal provenance manifest for every claim.
- **supporting_reason:** Full rereads maximize independence checking but waste context on byte-identical copies; newest-only retrieval is efficient but can erase historical scope; formal manifests improve auditability at maintenance cost.
- **counterargument_or_limit:** Hash deduplication can hide meaningful metadata differences outside file bytes, such as path semantics, surrounding package state, or assignment timing.
- **assumptions_and_boundaries:** Collapse only content interpretation, not path provenance, and retain dates plus repository or machine location in the ledger.
- **revision_decision:** Recommend hash-assisted semantic deduplication with path-level provenance rather than either naive repetition or newest-file replacement.
- **additional_insight_to_add:** Separate content identity from contextual identity: two files can say the same thing while still proving that the same guidance persisted across two archive snapshots.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Key failures are counting duplicates as independent evidence, preferring prose over code for mechanics, overlooking user-home sources, citing absent run artifacts, and failing to invalidate conclusions after script or repository changes.
- **supporting_reason:** Each mistake creates false corroboration, stale behavior claims, nonportable references, fabricated observation, or conclusions detached from their inputs.
- **counterargument_or_limit:** A lightweight orientation note may not need cryptographic hashes for every input.
- **assumptions_and_boundaries:** Use hashes when freezing evidence for handoff or final verification; use clear timestamps and paths for ephemeral exploration where hashes would add little.
- **revision_decision:** Add duplicate-family, availability, and invalidation warnings directly in the source table.
- **additional_insight_to_add:** Generated artifacts should carry both code-version and repository-state provenance because changing either side can alter the same output without an obvious textual warning.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good source map cites the builder hash for an inventory claim and a run's `all_files.txt`, `code_files.txt`, or `files.tsv` for observed coverage; a bad map cites archive prose as proof that a target file was included.
- **supporting_reason:** The good example matches claim type to evidence authority, while the bad example confuses method documentation with repository observation.
- **counterargument_or_limit:** A borderline architecture sketch can cite historical guidance alone if it clearly describes a proposed workflow rather than claiming current results.
- **assumptions_and_boundaries:** Examples must name whether they concern intent, implementation possibility, selected runtime branch, artifact contents, or source semantics.
- **revision_decision:** Add claim-and-source pair examples plus the correction required when the pairing is weak.
- **additional_insight_to_add:** A one-line evidence-role prefix can prevent more errors than a long bibliography because it tells readers how a citation may and may not be used.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Local-corpus claims can be verified through existence checks, complete reads, SHA-256 comparisons, shell syntax checks, capability probes, artifact inspection, and direct source reconciliation.
- **supporting_reason:** These checks independently establish identity, parseability, branch availability, run selection, and semantic agreement rather than collapsing all verification into file presence.
- **counterargument_or_limit:** Hash stability proves byte identity but says nothing about correctness, relevance, or whether an external program invoked that file.
- **assumptions_and_boundaries:** Record what each check establishes and avoid using a stronger-sounding mechanism to answer a different question.
- **revision_decision:** Attach a verification method and retained evidence field to every source family.
- **additional_insight_to_add:** Verification should follow the provenance chain forward and backward: derive conclusions from inputs, then trace each conclusion back to the narrowest source that can support it.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The read corpus establishes exact identities for the duplicated skill and precedent families plus the current builder, pointer reader, and agent metadata; future artifact contents and current upstream statements remain unknown here.
- **supporting_reason:** Local bytes were read and hashed without browsing or executing a target map, so implementation facts are stronger than repository-specific outcome claims.
- **counterargument_or_limit:** Machine-local paths and capability probes can change after this checkpoint even if the reference remains unchanged.
- **assumptions_and_boundaries:** Bind known identities to hashes, observed capabilities to the recorded environment, and missing run evidence to an explicit pending state rather than extrapolation.
- **revision_decision:** Include a frozen evidence ledger and a freshness trigger for every mutable source.
- **additional_insight_to_add:** Confidence decays on different clocks: archive bytes are stable, installed scripts change on update, environment capabilities change with `PATH`, and artifacts change with every repository revision or build option.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The local corpus is better modeled as a dependency graph than a reading list: guidance influences scripts, scripts plus environment and repository state produce artifacts, and artifacts select source spans that support decisions.
- **supporting_reason:** A change at one node invalidates only downstream claims, while stable upstream intent or pointer-format guidance may remain reusable.
- **counterargument_or_limit:** Maintaining fine-grained invalidation edges can become burdensome for one-off orientation.
- **assumptions_and_boundaries:** Track dependencies at the granularity needed for durable handoff, high-consequence decisions, or repeated automation; keep casual exploration concise.
- **revision_decision:** Add a source-to-claim invalidation matrix and a minimal reread trigger for each change class.
- **additional_insight_to_add:** Targeted invalidation lowers maintenance cost and discourages ceremonial rereads, because operators revisit the exact evidence stage affected by a changed script, capability, artifact, or source revision.

## Section 006: External Research Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names three external sites but does not decide which public pointers can shape dependency-map method design, which support agent workflow context, and which need fresh verification before a current factual claim.
- **supporting_reason:** Agent instruction formats, automation documentation, language protocols, search tools, parsers, symbol extractors, and graph renderers answer different parts of the workflow and age at different rates.
- **counterargument_or_limit:** A short source list can still prompt an experienced reader to research the right ecosystem without a formal role taxonomy.
- **assumptions_and_boundaries:** No browsing is authorized, so the evolved section may preserve URLs and locally recorded descriptions but cannot attest to present page contents, versions, availability, or compatibility.
- **revision_decision:** Turn the map into a research queue with source family, intended question, locally retained claim, current-verification status, and refresh trigger.
- **additional_insight_to_add:** External links are most useful when they route a concrete uncertainty rather than decorating a recommendation with borrowed authority.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default is to use current local scripts and run evidence for immediate mechanics, then consult primary external documentation only when an unresolved tool or protocol claim materially affects the decision and browsing is authorized.
- **supporting_reason:** Local executable bytes are directly inspectable now, whereas an unvisited URL supplies neither current text nor proof that its documented behavior matches the installed version.
- **counterargument_or_limit:** External primary documentation may be the fastest route when local code delegates behavior to a complex third-party tool and the version is already known.
- **assumptions_and_boundaries:** Preserve public pointers without presenting their locally summarized descriptions as refreshed external facts.
- **revision_decision:** Label every row `locally_retained_pointer_unrefreshed` in this evolution and specify the evidence required to promote it later.
- **additional_insight_to_add:** Local-first is a freshness discipline, not isolationism; authoritative public sources become stronger than recollection once they are deliberately reopened and version-matched.

### Question 03: When does the default work well?
- **current_section_observation:** A queued external map works well for planning tool escalation, comparing lexical and semantic approaches, and identifying primary documentation to consult after local evidence exposes a specific gap.
- **supporting_reason:** The retained pointers cover LSP navigation, Sourcegraph indexing, Tree-sitter, ast-grep, Universal Ctags, ripgrep, Graphviz, dependency-cruiser, agent instructions, and automation.
- **counterargument_or_limit:** Breadth can become distraction when a repository-native tool already answers the pending claim directly.
- **assumptions_and_boundaries:** Open only the smallest source set needed to resolve the named uncertainty, and prefer primary maintainers' documentation over derivative summaries.
- **revision_decision:** Add task-to-pointer routing so readers do not browse the entire list by default.
- **additional_insight_to_add:** Research cost falls when local mismatch categories choose the external source: bad spans route to Ctags or parser docs, while missing semantic calls route to LSP or index documentation.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The external map fails when link presence is treated as evidence, documentation for one version is applied to another, or a general ecosystem precedent is used to validate this builder's repository-specific accuracy.
- **supporting_reason:** A protocol capability does not prove a server implements it, a tool manual does not prove the installed binary exposes that mode, and another mapper's strategy does not calibrate local resolver recall.
- **counterargument_or_limit:** Stable standards documents can remain directionally useful even when not freshly opened.
- **assumptions_and_boundaries:** Use unrefreshed links only to identify follow-up research, never to settle compatibility, security, performance, or current behavior claims.
- **revision_decision:** Add explicit invalid-use examples and version-match requirements.
- **additional_insight_to_add:** The wrong external source can increase confidence while reducing relevance, making authority mismatch more dangerous than having no citation at all.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include vendored documentation snapshots, installed `--help` output, package lockfiles, source code, release notes, repository-native guides, and authorized live browsing of primary pages.
- **supporting_reason:** Snapshots maximize reproducibility but age; live pages improve freshness but can drift; CLI help matches the installed binary but may omit conceptual limits; source code is precise but expensive to interpret.
- **counterargument_or_limit:** Collecting all evidence forms for a low-impact tool-selection question would be disproportionate.
- **assumptions_and_boundaries:** Choose the source whose temporal and version scope matches the claim, then retain enough identity to reproduce the decision.
- **revision_decision:** Add an external-evidence ladder from local installed behavior through versioned primary documentation to independent empirical comparison.
- **additional_insight_to_add:** Version identity is the join key between local capability and external documentation; without it, two individually accurate sources may still describe different systems.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** External-source hazards include link rot, redirects, mutable pages, unpinned latest docs, archived summaries that paraphrase too strongly, product marketing claims, and sources that document optional rather than default behavior.
- **supporting_reason:** These defects can silently alter meaning while the visible URL remains unchanged or while a locally retained sentence outlives its original caveats.
- **counterargument_or_limit:** Requiring immutable snapshots for every benign concept would make the reference cumbersome and may conflict with licensing or access constraints.
- **assumptions_and_boundaries:** Pin versions and capture dates for consequential facts; use a lighter unrefreshed-pointer label for conceptual research queues.
- **revision_decision:** Add freshness, version, and authority checks to the map's verification column.
- **additional_insight_to_add:** A source ledger should track both content freshness and applicability freshness, because a current page can still be irrelevant to the installed tool or repository language.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good use says the local precedent note points to LSP 3.17 for future semantic-navigation research; a bad use says the current project has complete call hierarchy because the LSP specification defines that API.
- **supporting_reason:** The good statement reports provenance and intent, while the bad one skips server capability, indexing coverage, language support, and target-project verification.
- **counterargument_or_limit:** A borderline design proposal may cite Tree-sitter conceptually without reopening its docs if no claim about current API or benchmark behavior is made.
- **assumptions_and_boundaries:** Classify examples by whether the external source supports a general design idea, an installed capability, or a measured target outcome.
- **revision_decision:** Include acceptable pointer language and prohibited current-fact language beside the table.
- **additional_insight_to_add:** Verbs expose evidence strength: `points to` and `documents as locally summarized` are safer than `proves`, `guarantees`, or `supports here` without fresh checks.

### Question 08: How can the important claims be verified?
- **current_section_observation:** When browsing becomes authorized, verify a public claim by opening the primary page, recording retrieval date and version scope, matching it to the installed tool, and reproducing the relevant capability locally.
- **supporting_reason:** Documentation inspection establishes stated behavior, while a version-matched probe establishes availability in the actual environment and a target sample tests applicability.
- **counterargument_or_limit:** Some hosted documentation changes without stable version anchors, and local probes may not exercise every documented edge case.
- **assumptions_and_boundaries:** Retain short paraphrases rather than extensive quotations and distinguish documentation evidence from empirical validation.
- **revision_decision:** Add a promotion protocol from unrefreshed pointer to verified external fact.
- **additional_insight_to_add:** The strongest external claim card combines source identity, version applicability, local capability, and one falsifiable example instead of relying on citation count.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is known that the hashed local precedent file contains the listed URLs and descriptions; the present content, status, versioning, and claims of those remote pages are intentionally unverified.
- **supporting_reason:** The local file was read completely and hashed, while network retrieval was prohibited by the assignment.
- **counterargument_or_limit:** Some URLs point to long-lived primary projects and may still resolve exactly as summarized.
- **assumptions_and_boundaries:** Report retained local provenance with high confidence and all current remote characteristics as unknown pending authorized refresh.
- **revision_decision:** Add a known-unknown ledger and avoid time-sensitive wording for unvisited sources.
- **additional_insight_to_add:** Honest uncertainty preserves future research value because a later worker can refresh precisely the rows whose unresolved status affects a live decision.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The external map is a routing layer between local failure modes and candidate precision upgrades rather than a bibliography ordered by prestige.
- **supporting_reason:** Inventory omissions, poor spans, lexical false positives, missing call semantics, and rendering needs each point to a different class of external standard or tool.
- **counterargument_or_limit:** One failure may have multiple causes, so routing by symptom alone can select the wrong research branch.
- **assumptions_and_boundaries:** Confirm the local mismatch class before opening external sources and return to an empirical target check afterward.
- **revision_decision:** Organize pointers by question and add the expected local verification that closes each research loop.
- **additional_insight_to_add:** External research earns operational value only when it changes a local test, tool choice, or evidence boundary; otherwise it remains background context rather than decision evidence.

## Section 007: Anti Pattern Registry Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed registry identifies generic sourcing failures but does not help an operator recognize when a rough dependency map has crossed from useful orientation into misleading architectural evidence.
- **supporting_reason:** Inventory omissions, extraction fallback, lexical resolution, edge-capped rendering, stale pointers, and dynamic wiring each produce distinct symptoms and require different recovery actions.
- **counterargument_or_limit:** A large failure catalog can slow first-pass navigation and encourage defensive ceremony around low-impact lookups.
- **assumptions_and_boundaries:** The registry should prioritize failures that materially change claims or actions and keep lighter navigation guidance concise.
- **revision_decision:** Preserve the three seed anti-patterns and add map-specific entries with trigger, mechanism, consequence, detection, recovery, and escalation boundary.
- **additional_insight_to_add:** Naming the causal mechanism makes the registry operational because the same empty result needs a different remedy when caused by inventory exclusion, unsupported syntax, or genuine absence.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default is to run cheap invariant checks before graph interpretation and to classify every surprising result by pipeline stage before changing code or architecture.
- **supporting_reason:** Inventory counts, tooling metadata, TSV reconciliation, pointer resolution, and sampled source checks expose many high-impact defects earlier than broad manual review.
- **counterargument_or_limit:** Invariants cannot detect relationships that the observation model never attempts to represent, especially runtime and generated wiring.
- **assumptions_and_boundaries:** Use invariant checks to validate the rough map's contract, then escalate whenever the pending claim lies outside that contract.
- **revision_decision:** Order the registry by pipeline stage and attach a minimal safe replacement to each failure.
- **additional_insight_to_add:** Early-stage checks have multiplicative value because correcting inventory or extraction before ranking prevents many downstream conclusions from needing individual repair.

### Question 03: When does the default work well?
- **current_section_observation:** A stage-based anti-pattern registry works well during onboarding, review preparation, refactor scoping, and repeated map automation where operators can compare current artifacts with known expectations.
- **supporting_reason:** These workflows produce recurring observable signals such as count shifts, empty tables, one-line spans, unresolved clusters, and stale ranges.
- **counterargument_or_limit:** A novel language or framework may fail in ways absent from a registry built around the current extension and resolver set.
- **assumptions_and_boundaries:** Treat registry entries as diagnostic hypotheses and add new failure classes only after verifying their mechanism.
- **revision_decision:** Include applicability and false-positive notes so detection signals do not become automatic verdicts.
- **additional_insight_to_add:** Repeated mismatch classification can reveal which pipeline stage deserves engineering investment rather than merely adding more warnings to user guidance.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The registry becomes the wrong primary control when correctness depends on semantic resolution, runtime traces, security analysis, or exhaustive build configuration that a rough artifact cannot observe.
- **supporting_reason:** Cataloging known lexical defects does not establish recall for unknown dynamic relationships or every configuration variant.
- **counterargument_or_limit:** The registry can still prevent overclaiming and route the operator toward the appropriate specialized evidence.
- **assumptions_and_boundaries:** Stop diagnosing within the rough-map pipeline once the claim's required evidence exceeds its observation model.
- **revision_decision:** Add an explicit tool-abandonment anti-pattern for repeatedly patching heuristics instead of escalating precision.
- **additional_insight_to_add:** A mature registry must detect method fixation itself, because compensating controls can otherwise create false confidence around a fundamentally unsuitable analyzer.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include hard validation that aborts a build, warning-only diagnostics, independent inventory comparison, language-aware analyzers, runtime tracing, and manual source audits.
- **supporting_reason:** Hard gates prevent unsafe continuation but can block partial navigation; warnings preserve flow but are easily ignored; stronger analyzers improve semantics at setup and compute cost.
- **counterargument_or_limit:** Combining strict gates with every possible analyzer can make the workflow brittle and expensive.
- **assumptions_and_boundaries:** Fail closed only for contract violations that invalidate the requested claim; otherwise emit bounded uncertainty and a clear next verification step.
- **revision_decision:** Give each anti-pattern a severity and a response mode of stop, warn, sample, rebuild, or escalate.
- **additional_insight_to_add:** Response severity should follow decision consequence rather than artifact aesthetics, so a missing SVG can be informational while an omitted language can block a deletion claim.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Highest-risk failures are equating command success with coverage, treating no edge as no dependency, classifying all unresolved references as third-party, interpreting capped visuals as complete, and trusting lexical resolution for dynamic behavior.
- **supporting_reason:** These failures convert non-observation or presentation limits into confident absence and reachability claims that can authorize harmful changes.
- **counterargument_or_limit:** Other operational defects such as output permissions or malformed paths can stop work even if they are less likely to create silent architectural error.
- **assumptions_and_boundaries:** Rank silent false confidence above loud execution failure, while still documenting recovery for both.
- **revision_decision:** Add a criticality column based on invisibility, blast radius, and reversibility.
- **additional_insight_to_add:** Silent completeness errors deserve stronger gates than explicit failures because the latter naturally stop interpretation while the former reward it with plausible output.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good recovery traces an empty relation to unsupported inventory and rebuilds or escalates; bad behavior deletes a file because the graph has no inbound arrow; borderline use accepts a stale one-line pointer only to locate a nearby candidate.
- **supporting_reason:** The examples show whether an observation is used for reversible navigation or promoted into a consequential semantic claim.
- **counterargument_or_limit:** A stale pointer can still waste time or open the wrong sensitive file during an incident even without a code change.
- **assumptions_and_boundaries:** State consequence, evidence state, and corrective step in every example.
- **revision_decision:** Add paired failure and recovery examples for the critical registry entries.
- **additional_insight_to_add:** Recovery quality is measurable by whether it revises the faulty premise, not merely whether it finds another path to the desired conclusion.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Registry entries can be verified with controlled fixtures, independent inventories, capability-branch probes, TSV count reconciliation, pointer round trips, sampled edge checks, and deliberate dynamic or alias counterexamples.
- **supporting_reason:** Positive and negative fixtures make the alleged mechanism observable and distinguish a systematic limitation from a one-off data issue.
- **counterargument_or_limit:** Fixture success does not quantify accuracy on a large heterogeneous repository or every language grammar.
- **assumptions_and_boundaries:** Retain fixture scope, tool versions, expected artifact differences, and target samples before generalizing a failure pattern.
- **revision_decision:** Attach at least one reproducible detection or falsification method to each critical entry.
- **additional_insight_to_add:** Counterexample fixtures should survive as regression probes when the builder evolves, turning anti-pattern knowledge into executable institutional memory.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Script reading establishes that tracked-only Git inventory, finite extensions, fallback spans, lexical resolution, optional rendering, and edge caps are real mechanics; their frequency and impact across repositories are unmeasured.
- **supporting_reason:** Implementation branches are directly inspectable, but no target run or representative corpus study was conducted within this assignment.
- **counterargument_or_limit:** Some consequences follow logically even without frequency data, such as unsupported files being unable to contribute relations.
- **assumptions_and_boundaries:** Separate deterministic capability limits from estimated operational severity and project-specific likelihood.
- **revision_decision:** Mark each anti-pattern's basis as implementation fact, reasoned consequence, observed run signal, or unmeasured risk.
- **additional_insight_to_add:** Severity can be high despite unknown prevalence when a failure is silent, hard to detect downstream, and capable of authorizing irreversible action.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Anti-patterns compose across stages: tracked-only omission can create an unresolved import, which can distort a hub rank, which can misdirect a refactor even though each artifact is internally consistent.
- **supporting_reason:** Downstream projections preserve upstream omissions unless an independent check reintroduces the missing evidence.
- **counterargument_or_limit:** Modeling every composition path would make the registry too complex for routine use.
- **assumptions_and_boundaries:** Document the highest-consequence chains and use stage attribution to infer which downstream claims share an invalid premise.
- **revision_decision:** Add compound-failure scenarios and a rule to invalidate dependent conclusions after an upstream defect is found.
- **additional_insight_to_add:** The registry should drive selective rollback of reasoning: one inventory defect can invalidate many rankings at once while leaving unrelated pointer-reader behavior intact.

## Section 008: Verification Gate Command Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed supplies one final corpus verifier command but does not help the operator choose gates for script integrity, environment selection, artifact consistency, pointer validity, relation accuracy, or semantic sufficiency.
- **supporting_reason:** Each gate answers a different question, and a successful reference-generation check cannot establish that a dependency map represents a target program correctly.
- **counterargument_or_limit:** One canonical command is memorable and useful when the only task is validating generated reference structure.
- **assumptions_and_boundaries:** Preserve the seed command for its historical purpose while adding stage-specific gates and stating what every pass leaves unproven.
- **revision_decision:** Organize commands by preflight, build, invariant, sampling, project verification, and reference-file verification.
- **additional_insight_to_add:** A command set becomes trustworthy when each invocation has a claim contract, not merely when all commands return zero.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default is a least-mutating progression: inspect and syntax-check scripts, probe capabilities, choose an authorized output directory, build once, validate artifacts, resolve samples, then run project-native semantic checks.
- **supporting_reason:** Early read-only gates catch setup errors cheaply, while delayed artifact generation limits side effects and later semantic checks address what lexical maps cannot prove.
- **counterargument_or_limit:** A disposable fixture may benefit from building immediately because setup risk is low and output itself is the fastest diagnostic.
- **assumptions_and_boundaries:** Never run the builder into an unapproved or valuable directory, and never infer target semantics from shell or artifact-shape success.
- **revision_decision:** Provide copy-ready command blocks with required variables, expected outputs, failure interpretation, and cleanup ownership.
- **additional_insight_to_add:** Gate ordering reduces diagnostic ambiguity because a relation mismatch after verified inventory and extraction can be attributed more narrowly to resolution or semantics.

### Question 03: When does the default work well?
- **current_section_observation:** Layered command gates work well in local repositories with shell access, reproducible revisions, readable artifacts, and project-native tests or analyzers available after rough orientation.
- **supporting_reason:** The operator can bind commands to concrete files, capture capability branches, compare counts, and inspect source without relying on opaque service state.
- **counterargument_or_limit:** Sandboxed, remote, monorepo, or generated workspaces may require different roots, permissions, and project-specific entry commands.
- **assumptions_and_boundaries:** Parameterize paths and avoid presenting one repository's commands as universal.
- **revision_decision:** Add adaptation notes for Git versus non-Git inventory, optional tools, and repository-native verification.
- **additional_insight_to_add:** The reusable part is the invariant sequence; exact commands are implementations that should be replaced when the repository offers a stronger native mechanism.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The command set fails when zero exit codes are treated as proof of coverage, when destructive or unauthorized writes occur, or when generic shell checks substitute for language, build, security, or runtime verification.
- **supporting_reason:** Shell syntax says nothing about semantic recall, and artifact existence says nothing about whether omitted relationships matter to the pending action.
- **counterargument_or_limit:** Even a weak gate can catch regressions in file naming, table shape, and command invocation before deeper analysis.
- **assumptions_and_boundaries:** Explicitly label structural gates as necessary but insufficient and stop when the claim requires evidence unavailable in the current environment.
- **revision_decision:** Put a `does_not_prove` statement beside every command family.
- **additional_insight_to_add:** Overloaded gates create audit debt because later readers cannot tell whether a green result represented syntax, shape, sampled precision, or behavior.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include manual review, shell assertions, Python artifact parsers, repository tests, CI workflows, compiler queries, language servers, dedicated analyzers, and runtime instrumentation.
- **supporting_reason:** Shell gates are portable and transparent; structured parsers handle TSV and JSON robustly; CI improves repeatability; semantic tools improve precision but require setup and version control.
- **counterargument_or_limit:** Layering too many mechanisms can duplicate work and increase maintenance burden.
- **assumptions_and_boundaries:** Select the smallest independent gate set that covers the decision's failure modes and preserves actionable diagnostics.
- **revision_decision:** Add a gate-selection matrix by claim and consequence rather than mandating every command for every use.
- **additional_insight_to_add:** Independence matters more than quantity: two checks derived from the same lexical rows add less confidence than one source read or semantic check with a different observation model.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Command hazards include accidental output overwrite, stale artifact reuse, paths with whitespace or colons, pipeline exit masking, optional-tool branch drift, locale-dependent sorting, Git working-state changes, and checks that sample only easy positives.
- **supporting_reason:** These details can make identical-looking commands inspect different inputs or silently skip the edge cases most likely to falsify a conclusion.
- **counterargument_or_limit:** The frozen builder already uses strict shell mode, reducing some command-composition errors inside the script.
- **assumptions_and_boundaries:** Wrapper commands still need quoting, explicit roots, fresh output identity, and captured environment state.
- **revision_decision:** Add safety preconditions and negative-sample requirements before the command blocks.
- **additional_insight_to_add:** A fresh output directory is an evidence control, not housekeeping, because it prevents rows from an earlier producer or revision from contaminating the current decision.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good gate records the builder hash, revision, capability table, inventory reconciliation, and sampled edge result; a bad gate runs `test -s summary.md` and declares the architecture verified.
- **supporting_reason:** The good example preserves separate evidence for production, shape, and interpretation, while the bad example promotes nonempty output into semantic proof.
- **counterargument_or_limit:** A borderline quick lookup can reasonably stop after a valid symbol pointer and source read if it drives no broader claim.
- **assumptions_and_boundaries:** Examples should identify what action follows the pass and whether a false result is reversible.
- **revision_decision:** Add pass, fail, and conditional examples with exact claim language.
- **additional_insight_to_add:** The phrase after a command matters as much as the command: `artifact exists` is defensible, while `dependency is complete` requires an entirely different evidence chain.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The gate set itself can be verified by checking command availability, shell syntax, expected-failure fixtures, artifact schemas, pointer round trips, positive and negative relation samples, and project-native behavior tests.
- **supporting_reason:** Testing both passing and failing cases demonstrates that a gate detects the defect it claims to prevent rather than merely succeeding on healthy input.
- **counterargument_or_limit:** A small fixture cannot reproduce every repository layout, language construct, or operating-system path rule.
- **assumptions_and_boundaries:** Keep fixture conclusions narrow and complement them with representative target samples plus recorded limitations.
- **revision_decision:** Include expected result and failure meaning for each command family, not only invocation syntax.
- **additional_insight_to_add:** A verification gate without a demonstrated negative case may be ornamental because its ability to reject bad evidence has never been observed.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Current evidence confirms both shell scripts parse under Bash, `rg` and `ast-grep` are detectable, the available Ctags fails the builder's JSON probe, Graphviz `dot` is absent, and the historical final verifier path exists.
- **supporting_reason:** These facts came from local read-only probes on the recorded machine state rather than from assumptions about installed tool names.
- **counterargument_or_limit:** Capability state can change with `PATH`, installation, shell, or working directory before the next run.
- **assumptions_and_boundaries:** Bind observed gate results to this checkpoint and require fresh probes for future artifact production.
- **revision_decision:** Add a captured-evidence example and mark all target-map gates as not executed under the exclusive-write restriction.
- **additional_insight_to_add:** Separating verified command availability from unexecuted target behavior prevents documentation from implying that a map was built merely because its scripts passed syntax checks.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Gates form a proof graph: producer identity and inventory support artifact shape, shape supports queryability, pointer checks support local observations, and semantic checks support decisions.
- **supporting_reason:** Skipping an upstream node weakens every dependent conclusion, while a downstream failure identifies which preceding assumptions need reopening.
- **counterargument_or_limit:** Treating routine navigation as formal proof construction can add unnecessary ceremony.
- **assumptions_and_boundaries:** Use the full graph for durable or high-consequence conclusions and a clearly bounded subset for reversible exploration.
- **revision_decision:** Map each command to its supported claim and downstream dependents.
- **additional_insight_to_add:** Gate evidence should be composable but non-substitutable: multiple structural passes cannot be summed into semantic certainty, yet each can narrow where a semantic mismatch originates.

## Section 009: Agent Usage Decision Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed tells agents when the theme is relevant but does not choose among direct search, existing-artifact reuse, a new rough map, broader source reading, or immediate semantic and runtime escalation.
- **supporting_reason:** These routes have different setup cost, context cost, freshness risk, and evidentiary strength, so theme relevance alone cannot determine the right workflow.
- **counterargument_or_limit:** Experienced agents may infer the route from task wording and repository size without an explicit tree.
- **assumptions_and_boundaries:** The guide should optimize for the pending question and consequence rather than maximizing tool use.
- **revision_decision:** Add a decision tree keyed by target specificity, artifact freshness, repository unfamiliarity, relation type, and cost of error.
- **additional_insight_to_add:** Choosing not to build a map can be the most idiomatic use of this reference when direct evidence answers the question more cheaply and strongly.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default is query-first and consequence-aware: inspect fresh compatible artifacts if available, use direct source search for a narrow target, build only for broad unfamiliar orientation, and escalate before consequential absence or reachability claims.
- **supporting_reason:** Reuse avoids needless writes, direct search minimizes setup, rough mapping compresses broad discovery, and stronger analyzers prevent lexical blind spots from driving material action.
- **counterargument_or_limit:** Reusing artifacts can be riskier than rebuilding when producer identity, revision, options, or inventory policy are missing.
- **assumptions_and_boundaries:** Treat an artifact as reusable only when its provenance and observation contract match the current repository state and question.
- **revision_decision:** Define freshness and compatibility checks before the reuse branch.
- **additional_insight_to_add:** Artifact age is not the only freshness dimension; a recent map built with the wrong root or extension policy is stale for the decision immediately.

### Question 03: When does the default work well?
- **current_section_observation:** The routing default works well for agents handling orientation, review planning, candidate discovery, refactor preparation, and architecture explanation across repositories of uncertain structure.
- **supporting_reason:** These tasks benefit from progressively widening evidence while preserving an early exit when a direct pointer or authoritative project tool answers the question.
- **counterargument_or_limit:** Highly standardized monorepos may already have mandatory ownership, build-graph, or code-search systems that should always lead.
- **assumptions_and_boundaries:** Repository-native instructions and tooling outrank the generic route when they provide stronger applicable evidence.
- **revision_decision:** Add an initial instruction and native-tool discovery branch before invoking the rough builder.
- **additional_insight_to_add:** The guide should minimize tool switching by deciding the evidence class first and then selecting the cheapest mechanism that can supply it.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The guide fails when an agent follows the map workflow mechanically despite a known file, unsupported language, dynamic architecture, restricted write boundary, stale artifacts, or a high-consequence security or deletion decision.
- **supporting_reason:** In those cases the map adds cost, cannot observe the decisive relation, violates operational constraints, or creates false confidence.
- **counterargument_or_limit:** Even an unsuitable rough map may provide vocabulary and candidate paths before the primary method runs.
- **assumptions_and_boundaries:** Auxiliary use is acceptable only if its provisional status cannot be mistaken for authorization.
- **revision_decision:** Add explicit skip, reuse-denied, and escalation exits rather than routing every task through build and summary.
- **additional_insight_to_add:** A decision guide needs negative capability: it must make abstention and escalation first-class outcomes instead of treating them as failures to use the tool.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The major alternatives are exact-text search, structural search, manual directory reading, language-server queries, compiler or build graphs, dedicated dependency analyzers, ownership metadata, and runtime traces.
- **supporting_reason:** Exact search is fast but lexical; structural search improves syntax awareness; semantic indexes resolve identities; build graphs capture configured composition; runtime traces observe exercised behavior.
- **counterargument_or_limit:** Stronger mechanisms may be unavailable, slow to initialize, or incomplete for generated and conditional states.
- **assumptions_and_boundaries:** Compare setup, coverage, precision, reproducibility, side effects, and decision consequence rather than using a fixed tool hierarchy.
- **revision_decision:** Add a route comparison matrix and combination rules for complementary blind spots.
- **additional_insight_to_add:** The optimal route can be sequential: rough breadth finds candidates, semantic analysis resolves identities, and runtime evidence tests the paths that remain consequential.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Routing hazards include rebuilding over valuable artifacts, reusing a map from another revision, mapping the wrong root, ignoring repository instructions, expanding context before forming a query, and stopping after a visually plausible summary.
- **supporting_reason:** These mistakes waste work or detach evidence from the actual task even when each individual command succeeds.
- **counterargument_or_limit:** Some exploratory sessions intentionally tolerate stale hints if every selected source is reread before conclusions.
- **assumptions_and_boundaries:** State whether the route serves navigation, explanation, code change, or authorization, then scale freshness and verification accordingly.
- **revision_decision:** Add route-entry and route-exit checks with explicit evidence states.
- **additional_insight_to_add:** Workflow drift is detectable when the artifacts being inspected no longer reduce uncertainty about the question that initiated the map.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good routing uses `rg` for one known symbol, reuses a hash-bound current map for a broad review, and escalates an absence claim; bad routing builds a full map merely to open a named file or deletes code from an empty edge query.
- **supporting_reason:** These examples align cost and evidence strength with the question instead of rewarding maximal workflow complexity.
- **counterargument_or_limit:** A borderline map build may be justified for a named file if the real task is understanding its broader blast radius rather than locating it.
- **assumptions_and_boundaries:** Examples should include the actual decision behind the surface request.
- **revision_decision:** Add scenario cards with route, stop condition, and required handoff language.
- **additional_insight_to_add:** Clarifying the decision beneath the query prevents local optimization, such as finding a file quickly while missing that the user asked whether changing it is safe.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Route quality can be verified by checking whether the chosen method produced evidence sufficient for the action, minimized irrelevant reads, preserved provenance, and exposed contradictions before the decision.
- **supporting_reason:** These outcomes can be reviewed through artifact reuse checks, selected-context counts, mismatch logs, project verification, and reversals caused by late-discovered evidence.
- **counterargument_or_limit:** Efficiency metrics can favor superficial routes if evidence quality and avoided errors are not included.
- **assumptions_and_boundaries:** Evaluate both cost and decision correctness, with higher weight on false-negative prevention for consequential actions.
- **revision_decision:** Add route-review questions and evidence-retention requirements.
- **additional_insight_to_add:** A good route leaves an audit trail of discarded alternatives and why they were unnecessary, making efficiency defensible rather than merely fast.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local implementation defines its artifact and capability boundaries, but the best route for a target task remains judgment dependent on repository conventions, available native tools, map provenance, and consequence.
- **supporting_reason:** No universal threshold determines when map setup pays off or when a sample is sufficient across repository sizes and architectures.
- **counterargument_or_limit:** Strong defaults still reduce variance for common orientation tasks despite project-specific uncertainty.
- **assumptions_and_boundaries:** Present routing as default plus explicit override signals rather than a deterministic universal policy.
- **revision_decision:** Label high-confidence mechanical branches separately from judgment calls that require agent explanation.
- **additional_insight_to_add:** Uncertainty should be spent where it can change the route; once a direct authoritative answer exists, further mapping often has diminishing decision value.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Agent usage is a value-of-information problem: each step should be chosen for expected uncertainty reduction relative to cost, side effects, and the consequence of being wrong.
- **supporting_reason:** Direct search, rough maps, semantic indexes, and runtime checks offer different marginal information depending on what is already known.
- **counterargument_or_limit:** Formal value estimates are impractical during routine coding and can create false numeric precision.
- **assumptions_and_boundaries:** Use qualitative stop questions rather than invented scores: what uncertainty remains, can it change the action, and which evidence can falsify it cheapest?
- **revision_decision:** End the guide with a three-question continuation test and an explicit stop state.
- **additional_insight_to_add:** This framing prevents endless context accumulation because evidence collection stops when remaining uncertainty cannot change the bounded decision or has been consciously escalated to an owner.

## Section 010: User Journey Scenario
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed describes a generic designer or debugger opening the reference but does not demonstrate a real decision in which rough-map evidence, direct source, and project verification disagree.
- **supporting_reason:** A journey becomes instructive when the user must choose whether to split a registry hub and remove a loader whose runtime registration is invisible to lexical edges.
- **counterargument_or_limit:** One detailed scenario cannot represent every repository language, framework, or operational constraint.
- **assumptions_and_boundaries:** Use the scenario to teach decision transitions and evidence states, not to prescribe its exact commands or architecture everywhere.
- **revision_decision:** Build an end-to-end narrative from request clarification through map build, coverage surprise, source verification, route escalation, implementation boundary, and final handoff.
- **additional_insight_to_add:** A scenario that changes course teaches more than a perfect run because it shows that contradicting evidence is a normal routing signal rather than a workflow failure.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended journey starts by splitting the user's compound request into a hub-refactor hypothesis and a safe-deletion claim, because each requires different evidence strength.
- **supporting_reason:** Rough fan-in can prioritize registry review, while deletion requires authoritative absence evidence across static, configured, generated, and runtime paths.
- **counterargument_or_limit:** If the user only asked for navigation, decomposing downstream change decisions may exceed scope.
- **assumptions_and_boundaries:** Clarify intended action before collecting evidence and keep the journey bounded to decisions the user actually authorizes.
- **revision_decision:** Show separate claim cards, gates, and stop conditions for the two branches.
- **additional_insight_to_add:** Decomposition prevents a strong result for one subproblem from laundering confidence into another, such as using a verified hub rank to justify an unverified deletion.

### Question 03: When does the default work well?
- **current_section_observation:** The scenario works well for unfamiliar mixed-configuration repositories where static code is mostly supported but runtime wiring may live in manifests, generated registries, or framework conventions.
- **supporting_reason:** A rough map can efficiently narrow static candidates while an inventory audit exposes the evidence classes it cannot represent.
- **counterargument_or_limit:** In a repository with a complete native build graph and semantic index, the rough build step may be unnecessary.
- **assumptions_and_boundaries:** Substitute stronger native tools while preserving the scenario's claim decomposition, contradiction handling, and evidence handoff.
- **revision_decision:** Name fit assumptions and include a route override when project tooling already answers the question.
- **additional_insight_to_add:** The journey's reusable asset is its reasoning choreography, not the specific artifact producer.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The journey fails if the agent stops at the fan-in summary, treats an empty loader edge set as absence, or proceeds with code changes despite missing configuration and runtime evidence.
- **supporting_reason:** Those shortcuts preserve the user's initial hypothesis instead of testing it against the rough map's known blind spots.
- **counterargument_or_limit:** An empty edge result can still lower the priority of some static-consumer searches when inventory and resolver coverage are strong.
- **assumptions_and_boundaries:** Never let a probabilistic navigation hint become sole authorization for irreversible action.
- **revision_decision:** Include an explicit wrong turn, detection signal, and recovery step in the narrative.
- **additional_insight_to_add:** The user journey should reward premise revision, making evidence quality visible through changed decisions rather than through the number of artifacts produced.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternative routes include direct search, semantic references, compiler or build graphs, configuration inspection, generated-output analysis, tests, and runtime tracing.
- **supporting_reason:** Direct search and rough maps are inexpensive; semantic and build tools improve identity resolution; configuration and runtime checks reveal relationships static imports miss.
- **counterargument_or_limit:** Running every alternative would slow the task and can create contradictory data without a reconciliation plan.
- **assumptions_and_boundaries:** Choose alternatives based on the mismatch discovered and the consequence of each pending branch.
- **revision_decision:** Show why the hub branch can proceed with sampled static corroboration while the deletion branch escalates to configuration and runtime evidence.
- **additional_insight_to_add:** Branch-specific escalation keeps the overall task moving even when one claim is blocked by stronger evidence requirements.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Scenario-specific hazards include mapping the wrong root, excluding YAML or generated registries, fallback symbol ranges, graph edge caps, stale artifact reuse, and confirmation bias toward the requested deletion.
- **supporting_reason:** Each hazard can make the loader appear unused or the registry appear more central than it is.
- **counterargument_or_limit:** Some hazards may not occur in the chosen repository, and listing them all can distract from observed failures.
- **assumptions_and_boundaries:** Check cheap universal hazards first, then pursue only signals present in artifacts or project structure.
- **revision_decision:** Add a risk ledger that distinguishes checked, observed, not applicable, and unresolved states.
- **additional_insight_to_add:** Confirmation bias is an evidence-system defect when workflow stages only seek support for the requested change and lack a required counterexample search.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good behavior preserves the registry refactor candidate but blocks loader deletion after discovering runtime configuration; bad behavior deletes from a sparse graph; borderline behavior postpones deletion while still reporting the static no-edge observation.
- **supporting_reason:** These outcomes separate useful partial evidence from unjustified action and demonstrate that not every branch must end identically.
- **counterargument_or_limit:** Postponement can become indefinite if the handoff lacks a named next check and owner.
- **assumptions_and_boundaries:** Every unresolved branch needs explicit evidence still required, decision impact, and next responsibility.
- **revision_decision:** Add three outcome variants and a precise handoff record.
- **additional_insight_to_add:** A high-quality partial outcome advances safe work on verified branches while containing uncertainty on the branch that needs escalation.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify the scenario through inventory reconciliation, extraction metadata, full-row hub counts, sampled imports, direct registry and loader reads, configuration search, generated-output inspection, project tests, and a runtime registration probe.
- **supporting_reason:** These checks use independent observation models and target the exact failure path that lexical mapping misses.
- **counterargument_or_limit:** A runtime probe only covers the exercised configuration and workload, so variants remain a boundary.
- **assumptions_and_boundaries:** Record enabled features, configuration files, generated state, test selection, and runtime inputs with the final conclusion.
- **revision_decision:** Add a claim-to-check matrix with pass, contradiction, and unresolved interpretations.
- **additional_insight_to_add:** Verification should seek disagreement deliberately; one configuration variant that loads the component is enough to refute universal unusedness.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** In the scenario, static fan-in and sampled imports can be known for the mapped revision, while architectural importance, safe split boundaries, and universal loader absence require judgment or broader evidence.
- **supporting_reason:** Relation counts measure the selected lexical graph, not change cost, runtime criticality, ownership, or every configuration.
- **counterargument_or_limit:** Strong repository conventions and passing integration tests can substantially raise confidence in a proposed boundary.
- **assumptions_and_boundaries:** State which facts belong to the illustrative scenario and avoid presenting invented counts as measurements from this actual repository evolution.
- **revision_decision:** Use qualitative or explicitly illustrative values and mark all scenario outcomes as worked examples.
- **additional_insight_to_add:** Scenario realism comes from causal fidelity and evidence boundaries, not fabricated numeric precision.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The compound journey reveals that one artifact can support different confidence levels for different branches: enough to prioritize a hub review but insufficient to authorize deletion.
- **supporting_reason:** Evidence strength depends on the claim and consequence, not on a global quality label attached to the map.
- **counterargument_or_limit:** Maintaining claim-specific evidence cards adds documentation overhead for simple tasks.
- **assumptions_and_boundaries:** Use explicit cards when branches have different reversibility, owners, or verification mechanisms; keep trivial navigation informal.
- **revision_decision:** End the scenario with a split decision and separate next steps rather than a single success verdict.
- **additional_insight_to_add:** Branch-local confidence enables parallel progress without forcing either premature certainty or an all-or-nothing halt across the entire user request.

## Section 011: Decision Tradeoff Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed offers generic adopt, adapt, avoid, and error-cost rows but does not choose among the concrete dependency-mapping methods and evidence depths available to an agent.
- **supporting_reason:** Reuse versus rebuild, lexical breadth versus semantic precision, pointers versus whole files, samples versus exhaustive checks, and static versus runtime evidence each change cost and claim strength differently.
- **counterargument_or_limit:** A compact adopt/adapt/avoid frame is easier to remember than a multidimensional matrix.
- **assumptions_and_boundaries:** Preserve the seed frame as a top-level posture while adding task-specific choices underneath it.
- **revision_decision:** Build a tradeoff guide indexed by decision consequence, observation need, setup cost, and escalation trigger.
- **additional_insight_to_add:** Tradeoffs should be evaluated per claim because one task can rationally adopt rough mapping for discovery, adapt it for review ranking, and avoid it for deletion authorization.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is the cheapest evidence route capable of falsifying the pending claim, with explicit escalation when the remaining blind spot could change the action.
- **supporting_reason:** This principle avoids both under-verification from convenient lexical output and over-engineering from deploying semantic or runtime systems for simple navigation.
- **counterargument_or_limit:** Estimating sufficiency requires judgment and can vary between operators.
- **assumptions_and_boundaries:** Use consequence, reversibility, native-tool availability, and known observation gaps as stable decision prompts rather than invented numeric thresholds.
- **revision_decision:** Put a qualitative sufficiency rule and stop question above the option tables.
- **additional_insight_to_add:** The default optimizes expected decision quality, not tool sophistication or minimum elapsed time in isolation.

### Question 03: When does the default work well?
- **current_section_observation:** Cheapest-sufficient routing works well when claims are decomposed, evidence boundaries are visible, and agents can escalate incrementally without discarding useful earlier discovery.
- **supporting_reason:** Rough artifacts can narrow candidates before source, semantic, build, or runtime checks answer the consequential subset.
- **counterargument_or_limit:** Some regulated or safety-critical workflows prescribe a fixed evidence floor regardless of perceived local consequence.
- **assumptions_and_boundaries:** Organizational policy and domain assurance requirements override the generic cost-sensitive default.
- **revision_decision:** Add a mandatory-policy override and distinguish exploratory from approval workflows.
- **additional_insight_to_add:** Incremental escalation preserves value from weak evidence while preventing it from becoming the final authority.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The tradeoff default fails when operators underestimate false-negative cost, cannot reconstruct artifact provenance, or choose methods whose blind spots correlate rather than complement one another.
- **supporting_reason:** Two lexical checks may agree because both miss dynamic registration, and a cheap route may appear sufficient only because the decisive evidence is absent.
- **counterargument_or_limit:** Perfectly independent evidence sources rarely exist in practical engineering.
- **assumptions_and_boundaries:** Seek materially different observation models rather than formal independence and fail closed for high-consequence absence claims.
- **revision_decision:** Add correlated-blind-spot and unknown-provenance penalties to option selection.
- **additional_insight_to_add:** Agreement increases confidence only to the extent that the agreeing methods could have failed differently.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Material alternatives span direct search, structural search, rough maps, semantic indexes, build graphs, runtime traces, manual review, fresh builds, artifact reuse, full context, pointer slices, sampling, and exhaustive enumeration.
- **supporting_reason:** Each choice exchanges setup, context, precision, recall, reproducibility, freshness, side effects, and interpretability.
- **counterargument_or_limit:** A single table can obscure interactions, such as a fresh rough map still lacking semantic precision.
- **assumptions_and_boundaries:** Separate production choices, retrieval choices, and verification choices, then show common combinations.
- **revision_decision:** Add three matrices plus recommended bundles for navigation, review, refactor, and absence claims.
- **additional_insight_to_add:** Bundles should close complementary gaps rather than merely stack more artifacts from the same pipeline.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Tradeoff errors include treating speed as total cost, confusing fresh output with valid scope, preferring visual simplicity over complete rows, and equating more context with more understanding.
- **supporting_reason:** Late correction, false confidence, context dilution, and irreversible changes can dominate the small upfront savings that motivated the shortcut.
- **counterargument_or_limit:** Excessive caution also has cost through delayed feedback and blocked exploration.
- **assumptions_and_boundaries:** Allow lightweight provisional states for reversible work while requiring explicit promotion gates before material action.
- **revision_decision:** Include downstream rework and decision-reversal cost in every option's tradeoff description.
- **additional_insight_to_add:** The true cost of a method includes how clearly its errors can be detected and how selectively its conclusions can be rolled back.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good choice uses direct search for location, rough mapping plus samples for review priority, and semantic or runtime evidence for absence; a bad choice uses one method universally.
- **supporting_reason:** The good examples align observation strength with claim consequence, while the bad approach mistakes consistency for fit.
- **counterargument_or_limit:** A borderline low-risk refactor may proceed from broad search and tests without a formal map if repository conventions make consumers obvious.
- **assumptions_and_boundaries:** Evaluate the complete evidence bundle and action boundary rather than requiring a named tool.
- **revision_decision:** Add claim-specific good, bad, and conditional bundles.
- **additional_insight_to_add:** Tool substitution is acceptable when the replacement preserves the required observation model and verification strength.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Tradeoff choices can be reviewed through counterfactual checks: what failure could the selected route miss, which independent signal would reveal it, and would discovery occur before or after action.
- **supporting_reason:** This tests the decision architecture rather than merely replaying successful commands.
- **counterargument_or_limit:** Counterfactuals depend on imagination and may omit unfamiliar failure classes.
- **assumptions_and_boundaries:** Combine known anti-patterns, repository-specific risks, negative fixtures, and post-decision feedback.
- **revision_decision:** Add a pre-action tradeoff audit and a post-action route-quality review.
- **additional_insight_to_add:** Route quality improves when teams record not only which method worked but which plausible error it was selected to expose.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Tool mechanics and deterministic observation limits are known from local implementation, while relative cost, accuracy, and acceptable uncertainty remain repository- and decision-specific.
- **supporting_reason:** No benchmark or representative corpus in this assignment calibrates setup time, precision, recall, or rework across the alternatives.
- **counterargument_or_limit:** General engineering experience still supports strong qualitative ordering for common navigation and absence cases.
- **assumptions_and_boundaries:** Present comparisons as reasoned tradeoffs and avoid unsupported performance or accuracy numbers.
- **revision_decision:** Add an evidence-basis column and a local-calibration protocol.
- **additional_insight_to_add:** Unmeasured does not mean unknowable; repeated mismatch and outcome logs can gradually replace editorial preference with project-specific evidence.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Tradeoff selection is an option-preservation problem: early cheap evidence should narrow choices without committing the team to conclusions it cannot support.
- **supporting_reason:** Pointer-first maps preserve the ability to escalate, while premature deletion or architecture redesign destroys options before stronger evidence arrives.
- **counterargument_or_limit:** Keeping every option open can become indecision and prevent timely delivery.
- **assumptions_and_boundaries:** Define explicit evidence thresholds and deadlines for irreversible branches while allowing reversible experiments.
- **revision_decision:** Add reversibility and option-loss columns to the tradeoff guide.
- **additional_insight_to_add:** The best early method is often the one that maximizes informative next choices, not the one that appears to produce the most complete immediate answer.

## Section 012: Local Corpus Hierarchy
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed assigns canonical, supporting, and legacy roles to four archive paths but does not explain which source wins for historical intent, current mechanics, selected run behavior, target semantics, or public research status.
- **supporting_reason:** Authority is claim-dependent: a dated snapshot governs its own history, executable code governs implemented branches, artifacts govern run observations, and target evidence governs program behavior.
- **counterargument_or_limit:** A single total order is easier for agents to follow and can reduce debate over source selection.
- **assumptions_and_boundaries:** Simplicity must not permit a higher-ranked prose file to override direct implementation or semantic evidence outside its role.
- **revision_decision:** Replace the implicit total order with a precedence matrix by claim class while preserving seed role labels and paths.
- **additional_insight_to_add:** Hierarchy is safer when modeled as typed authority rather than prestige, because no source is globally canonical for every question in the pipeline.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default precedence is temporal snapshot for historical claims, current script for mechanics, captured environment and `tooling.tsv` for selected branches, generated rows for observations, and direct project evidence for semantics.
- **supporting_reason:** This order follows the causal production chain and assigns each statement to the narrowest source capable of supporting it.
- **counterargument_or_limit:** Generated artifacts can be corrupt or stale, and direct source can still be misinterpreted without build or runtime context.
- **assumptions_and_boundaries:** Every precedence step remains subject to identity, freshness, coverage, and corroboration checks.
- **revision_decision:** Add a claim-to-authority table plus conflict-resolution rules.
- **additional_insight_to_add:** Narrow-source authority reduces overreach: an artifact can establish that a row exists without outranking source on what the relation means.

### Question 03: When does the default work well?
- **current_section_observation:** Typed hierarchy works well for durable references, incident handoffs, repeated map runs, and archive comparisons where statements must remain traceable as files and environments change.
- **supporting_reason:** It lets reviewers reopen only the evidence family affected by a change and prevents duplicate archive copies from multiplying confidence.
- **counterargument_or_limit:** One-off private exploration may not justify a formal precedence ledger.
- **assumptions_and_boundaries:** Apply the full model when conclusions are handed off, repeated, or consequential; use abbreviated labels for reversible navigation.
- **revision_decision:** Add lightweight and durable-use variants.
- **additional_insight_to_add:** Typed provenance improves maintenance as well as correctness because invalidation can target the precise downstream claim family.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The hierarchy fails when role labels are treated as proof of correctness, newer paths automatically replace dated snapshots, or identical files are counted as independent corroboration.
- **supporting_reason:** Metadata can be stale, temporal questions can require older bytes, and hash-equal copies contribute persistence evidence rather than separate substantive support.
- **counterargument_or_limit:** Recency is often a useful heuristic when no stronger identity or intent signal exists.
- **assumptions_and_boundaries:** Use recency only after matching claim scope and detecting content identity or conflict.
- **revision_decision:** Add duplicate, conflicting, missing, and superseded states with explicit handling.
- **additional_insight_to_add:** A role system needs a conflict path because forcing disagreement into a fixed rank can erase the very evidence that should trigger investigation.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include newest-wins ordering, archive-designated canon, executable-code supremacy, majority agreement across sources, or a provenance graph without a single canonical source.
- **supporting_reason:** Newest-wins is simple but can rewrite history; code supremacy fits mechanics but not intent; majority agreement overcounts duplicates; provenance graphs preserve nuance at documentation cost.
- **counterargument_or_limit:** A full graph can overwhelm agents who need one path to start reading.
- **assumptions_and_boundaries:** Provide a default retrieval route while retaining typed conflict information for claims that matter.
- **revision_decision:** Use a compact precedence matrix backed by a source dependency graph rather than an unqualified total order.
- **additional_insight_to_add:** The start path and final authority can differ: begin with concise guidance for orientation, then settle mechanics or semantics with stronger evidence.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hierarchy hazards include path availability outside the repository, hash drift, mislabeled legacy status, archive context loss, current installation mutation, stale artifacts, and external pointers presented as refreshed facts.
- **supporting_reason:** Each can make a source appear more authoritative or portable than it is.
- **counterargument_or_limit:** Recording every machine and archive detail can add noise to user-facing guidance.
- **assumptions_and_boundaries:** Keep the full ledger in durable evidence and expose only the claim-relevant hierarchy in concise answers.
- **revision_decision:** Add availability, content identity, temporal scope, and freshness columns.
- **additional_insight_to_add:** Portability is itself an authority dimension: a machine-local path may best describe current behavior yet be inaccessible to a remote reviewer unless its identity is preserved.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good claim cites the 202602 file for what that snapshot said and the current builder for present mechanics; a bad claim calls three identical skill copies three independent confirmations.
- **supporting_reason:** The good example respects temporal and content identity, while the bad one converts duplication into false evidence weight.
- **counterargument_or_limit:** A borderline summary can cite one representative hash-equal path if it also records that equivalent snapshots exist.
- **assumptions_and_boundaries:** Preserve every required archive row even when only one copy needs semantic rereading.
- **revision_decision:** Add source-selection examples for historical, mechanical, run, semantic, and external claims.
- **additional_insight_to_add:** Representative citation and complete provenance are compatible when the ledger separates what was read for meaning from where identical bytes were found.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify hierarchy through complete reads, SHA-256 comparison, path and date capture, script-to-prose reconciliation, run metadata checks, and target-source or project-tool validation.
- **supporting_reason:** These checks establish content identity, temporal scope, executable divergence, selected behavior, and semantic agreement independently.
- **counterargument_or_limit:** Hashes cannot reveal why a role label was assigned or whether the content is substantively correct.
- **assumptions_and_boundaries:** Treat metadata and hashes as routing evidence, then verify the underlying claim using the appropriate authority.
- **revision_decision:** Add a hierarchy audit checklist and conflict record.
- **additional_insight_to_add:** A conflict is resolved only when the claim is narrowed or stronger evidence explains the divergence, not when one path is silently discarded.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is known that the three observed skill copies share one hash and the three precedent copies share another; the rationale behind the seed's canonical-versus-legacy assignments is not preserved.
- **supporting_reason:** Byte identity was measured directly, while no assignment note explains why 202602 is labeled canonical and 202603 legacy despite identical contents.
- **counterargument_or_limit:** The labels may reflect a corpus-generation policy outside this file rather than substantive ranking.
- **assumptions_and_boundaries:** Preserve labels without inventing their rationale and avoid using them to overrule claim-specific authority.
- **revision_decision:** Add an uncertainty note beside the historical role metadata.
- **additional_insight_to_add:** Unexplained metadata should be retained as evidence about the corpus process but quarantined from technical conclusions until its semantics are known.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The hierarchy is a partial order aligned with causality: guidance informs implementation, implementation plus environment and repository state produces artifacts, and artifacts route source checks that support decisions.
- **supporting_reason:** Upstream sources constrain possibilities while downstream evidence establishes selected and semantic reality.
- **counterargument_or_limit:** Causality can loop when runtime findings motivate script and guidance changes.
- **assumptions_and_boundaries:** Model feedback as a new versioned trajectory rather than allowing later edits to rewrite prior evidence.
- **revision_decision:** Add causal edges, feedback rules, and targeted invalidation guidance.
- **additional_insight_to_add:** Versioned partial orders preserve learning: a discovered resolver defect can improve future guidance while the prior artifact remains honestly interpretable under its original producer.

## Section 013: Theme Specific Artifact
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names a dependency graph probe with ownership, false-positive rules, and blast-radius examples but provides only three generic completion fields and no durable evidence contract.
- **supporting_reason:** Operators need one artifact that binds producer and repository identity to coverage, candidate claims, mismatches, verification, decisions, and invalidation triggers.
- **counterargument_or_limit:** A comprehensive decision record can duplicate information already present in generated map files and project issue trackers.
- **assumptions_and_boundaries:** The artifact should reference existing evidence by identity and pointer rather than copying entire TSVs or source files.
- **revision_decision:** Define a `Dependency Map Decision Record` schema with required, conditional, and prohibited content.
- **additional_insight_to_add:** A decision record is valuable because it preserves why selected rows mattered, not because it becomes another graph representation.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default is one record per target revision and bounded decision, containing a run manifest, coverage ledger, claim cards, sampled evidence, mismatch log, verification outcomes, and next action.
- **supporting_reason:** This scope keeps provenance coherent while preventing unrelated questions from inheriting one another's confidence or stop conditions.
- **counterargument_or_limit:** Several closely related decisions may share most evidence and create repetitive records.
- **assumptions_and_boundaries:** Allow shared run identity and evidence references, but keep each actionable claim and consequence separately typed.
- **revision_decision:** Add a reusable Markdown schema plus rules for linking shared evidence without duplicating field values.
- **additional_insight_to_add:** Claim-local records support split outcomes, letting one refactor branch proceed while an absence branch remains unresolved.

### Question 03: When does the default work well?
- **current_section_observation:** The decision record works well for refactor planning, code review handoff, repeated analysis, incident investigation, and any map-derived conclusion likely to outlive the current context window.
- **supporting_reason:** These workflows benefit from reproducible identities, explicit omissions, and a clear route from artifact row to source and project verification.
- **counterargument_or_limit:** A one-off navigation query may need only a current pointer and no durable record.
- **assumptions_and_boundaries:** Scale completion depth with consequence and lifespan while retaining the core evidence boundary for handed-off claims.
- **revision_decision:** Define lightweight, standard, and high-assurance completion profiles.
- **additional_insight_to_add:** The artifact is most useful at context boundaries, where implicit knowledge about why a candidate was selected would otherwise disappear.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The artifact fails when filled after the fact as ceremony, used to launder uncertain rows into approved claims, or maintained separately from changing producer and repository identities.
- **supporting_reason:** Structured fields cannot compensate for weak evidence, and stale records can appear more authoritative than the ephemeral reasoning they summarize.
- **counterargument_or_limit:** Even retrospective documentation can expose missing assumptions and prevent an unsafe handoff.
- **assumptions_and_boundaries:** Mark retrospective reconstruction and unresolved provenance explicitly; do not grant approval state without replayable gates.
- **revision_decision:** Add freshness, reconstruction, and evidence-sufficiency rules plus a prohibited-field list for unsupported precision.
- **additional_insight_to_add:** Formal structure increases both value and risk because readers tend to trust complete-looking forms; therefore incompleteness must be representable honestly.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include free-form notes, issue comments, machine-readable JSON or YAML, CI artifact manifests, architecture decision records, and graph annotations.
- **supporting_reason:** Markdown is readable and diffable; machine formats validate well but are less conversational; issue trackers add ownership; CI manifests capture automation but may omit reasoning.
- **counterargument_or_limit:** Maintaining several synchronized representations creates drift.
- **assumptions_and_boundaries:** Choose one authoritative record and link auxiliary machine outputs by stable identity.
- **revision_decision:** Recommend Markdown for human decision context with structured tables and optional machine validation when automation justifies it.
- **additional_insight_to_add:** The optimal representation follows the record's primary consumer: humans need causal explanation, while automation needs stable fields and schemas.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Artifact hazards include copying huge evidence dumps, omitting dirty-state identity, hiding unsupported files, using numeric confidence without calibration, failing to distinguish no row from no dependency, and leaving invalidation rules blank.
- **supporting_reason:** These defects make the record expensive, misleading, or impossible to refresh selectively.
- **counterargument_or_limit:** Some fields may genuinely be not applicable for a narrow navigation record.
- **assumptions_and_boundaries:** Require an explicit not-applicable reason rather than silent omission for conditional fields.
- **revision_decision:** Add field-level completion tests and anti-values.
- **additional_insight_to_add:** An invalidation trigger is as important as the original evidence because it defines when a durable claim must stop being reused.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good record cites exact artifact rows and source checks with bounded claim language; a bad record pastes an SVG and declares complete blast radius; a borderline record preserves a candidate pointer but lacks producer identity.
- **supporting_reason:** The examples separate decision evidence from presentation and show why provenance defects limit reuse.
- **counterargument_or_limit:** A screenshot or graph can still aid communication when linked to complete rows and observation limits.
- **assumptions_and_boundaries:** Evaluate whether another operator can reproduce, falsify, and invalidate the claim from the record.
- **revision_decision:** Include compact good, bad, and recoverable records.
- **additional_insight_to_add:** Recoverability should be explicit: a record with missing provenance may remain a search hint while losing authority for every stronger claim.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify the record by schema checks, hash and revision confirmation, artifact existence and row lookup, pointer round trips, source comparison, project commands, mismatch reconciliation, and freshness-trigger review.
- **supporting_reason:** This validates both document structure and the evidence references it contains.
- **counterargument_or_limit:** A structurally valid record can still contain a poor interpretation or an insufficient verification method.
- **assumptions_and_boundaries:** Require reviewer judgment on claim-to-evidence fit in addition to automated field validation.
- **revision_decision:** Add a record acceptance checklist with independent rejection cases.
- **additional_insight_to_add:** Verification should be bidirectional: every claim traces to evidence, and every retained evidence item states which claim it supports or refutes.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local corpus supports the need for pointer-first artifacts and verification gates, while the proposed decision-record schema is a reasoned synthesis not an empirically benchmarked standard.
- **supporting_reason:** No local source specifies this exact integrated artifact or measures its documentation cost and error-reduction benefit.
- **counterargument_or_limit:** Its fields derive directly from observed pipeline dependencies and known failure modes.
- **assumptions_and_boundaries:** Present the schema as a recommended default to calibrate through use rather than an established external standard.
- **revision_decision:** Label design rationale, evidence basis, and future metrics explicitly.
- **additional_insight_to_add:** Schema evolution should follow observed retrieval and decision failures, avoiding fields added only because they sound comprehensive.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The decision record can function as a compact provenance graph linking inputs, transformations, observations, claims, actions, and invalidation events.
- **supporting_reason:** Those links allow selective rollback when one producer, repository state, sample, or semantic premise changes.
- **counterargument_or_limit:** Fine-grained graph maintenance can outweigh value for low-impact tasks.
- **assumptions_and_boundaries:** Use claim-level edges for durable or consequential decisions and a reduced profile for navigation.
- **revision_decision:** Add dependency identifiers between record blocks and define selective invalidation behavior.
- **additional_insight_to_add:** Once claims are linked to their premises, review can focus on the smallest changed evidence cut instead of repeating the entire mapping workflow.

## Section 014: Worked Example Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed supplies one sentence each for good, bad, and borderline use but does not show how an agent selects a route, interprets an artifact, detects a limitation, and changes a conclusion.
- **supporting_reason:** Worked examples should help readers distinguish candidate navigation, corroborated static relations, presentation artifacts, stale pointers, resolver misses, and unsupported absence claims.
- **counterargument_or_limit:** Too many detailed examples can obscure the compact defaults and invite copy-paste without adapting to the repository.
- **assumptions_and_boundaries:** Use a small orthogonal set, mark values illustrative, and extract the transferable decision rule from each one.
- **revision_decision:** Add six examples spanning direct navigation, rough orientation, alias resolution, graph caps, stale pointers, and dynamic registration.
- **additional_insight_to_add:** Orthogonal examples teach the observation model more effectively than repeated success cases because each exposes a different reason that plausible output can mislead.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default example format is question, route, observed evidence, missing evidence, verification, conclusion, rejected overclaim, and invalidation trigger.
- **supporting_reason:** This structure keeps method choice and claim strength visible while making the conclusion reproducible and falsifiable.
- **counterargument_or_limit:** A compact code snippet may communicate some mechanics faster than a full evidence narrative.
- **assumptions_and_boundaries:** Include snippets only when they illuminate a specific mechanism and retain the surrounding decision contract.
- **revision_decision:** Standardize every example on the same eight fields.
- **additional_insight_to_add:** A consistent example schema lets readers compare where routes diverge without mistaking different claim types for inconsistent guidance.

### Question 03: When does the default work well?
- **current_section_observation:** Structured examples work well for onboarding, review checklists, agent prompt design, incident retrospectives, and training on evidence boundaries.
- **supporting_reason:** They expose both action and rationale in a form that can be replayed against a target repository.
- **counterargument_or_limit:** Experts may prefer terse counterexamples once the evidence model is familiar.
- **assumptions_and_boundaries:** Keep a concise takeaway under each scenario so experienced readers can scan while newer readers inspect the full chain.
- **revision_decision:** Add a one-line transferable rule to every example.
- **additional_insight_to_add:** Examples become reusable test cases when their inputs and expected evidence states are concrete enough to replay after tool changes.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Worked examples fail when illustrative details are presented as measured facts, when only happy paths appear, or when readers infer that one fixture calibrates repository-wide accuracy.
- **supporting_reason:** Fabricated precision and unrepresentative samples can make training material more authoritative-looking than actual evidence.
- **counterargument_or_limit:** Some numeric values help explain caps, counts, and decision thresholds when clearly labeled illustrative.
- **assumptions_and_boundaries:** Use qualitative outcomes or explicitly illustrative values and never convert them into performance or reliability claims.
- **revision_decision:** Add an illustration boundary and counterexample to every scenario.
- **additional_insight_to_add:** The credibility of an example comes from causal accuracy, not realism theater or exact-looking numbers.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Example formats can be prose journeys, command transcripts, before-and-after tables, controlled fixtures, decision records, or incident narratives.
- **supporting_reason:** Commands improve reproducibility, tables improve comparison, fixtures isolate mechanisms, and narratives show route changes under uncertainty.
- **counterargument_or_limit:** Combining all formats in every example would be verbose and repetitive.
- **assumptions_and_boundaries:** Select the format that best exposes the failure mechanism while keeping a common evidence schema.
- **revision_decision:** Mix concise tables and short narratives rather than duplicating full command blocks already documented elsewhere.
- **additional_insight_to_add:** Format diversity is useful only when semantic fields remain comparable across examples.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Example hazards include paths that imply real repository files, commands that write without authorization, unsupported shell features, omitted negative cases, and conclusions that quietly exceed the shown evidence.
- **supporting_reason:** Readers may execute or generalize examples literally, turning pedagogical simplification into operational risk.
- **counterargument_or_limit:** Excessive warnings can make examples unreadable.
- **assumptions_and_boundaries:** Put boundaries next to the exact step they constrain and avoid unnecessary executable side effects.
- **revision_decision:** Label all repositories and values illustrative and keep commands conceptual unless their safety preconditions are complete.
- **additional_insight_to_add:** A safe example demonstrates refusal and escalation as normal outputs, not merely successful production.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good examples match route to claim and revise on contradiction; bad examples promote graph or empty-query output into semantics; borderline examples retain weak evidence only as a current source-navigation hint.
- **supporting_reason:** These categories map directly to reversibility, evidence sufficiency, and handoff risk.
- **counterargument_or_limit:** Borderline status can shift when an exploratory hint enters a durable review or automated decision.
- **assumptions_and_boundaries:** Reclassify examples by downstream use, not solely by how the evidence was first collected.
- **revision_decision:** Include promotion and downgrade triggers beside each classification.
- **additional_insight_to_add:** Evidence can be safe in one context and unsafe in another, so examples need lifecycle as well as initial quality.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify examples by replaying controlled fixtures, checking expected artifact differences, resolving pointers, inspecting source and configuration, and confirming that negative cases cause downgrade or escalation.
- **supporting_reason:** A worked example is credible when its described gate can distinguish the good path from the tempting bad conclusion.
- **counterargument_or_limit:** This reference does not create fixture files due exclusive write scope, so the examples remain designs for future authorized execution.
- **assumptions_and_boundaries:** State unexecuted status and the exact observable outcome a fixture should produce.
- **revision_decision:** Add a future replay check to each example without claiming it ran here.
- **additional_insight_to_add:** The negative assertion is the stronger pedagogical test: the example should show what evidence would make the agent stop or change routes.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The examples can rely confidently on frozen script mechanics, but their repository files, artifact rows, and outcomes are illustrative rather than observed in this assignment.
- **supporting_reason:** No target output directory or fixture was authorized, while source inspection establishes the relevant branch behavior and limitations.
- **counterargument_or_limit:** An illustrative scenario can still be technically wrong if it assumes unsupported syntax or artifact fields.
- **assumptions_and_boundaries:** Match every example to literal builder contracts and avoid claims about untested parser behavior beyond those contracts.
- **revision_decision:** Add an evidence-basis note and avoid empirical frequency language.
- **additional_insight_to_add:** Separating implementation-grounded mechanism from invented target data lets examples remain useful without pretending to be observations.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The example set can become a regression-oriented curriculum: each scenario names a tool blind spot, an unsafe inference, and the evidence route that repairs it.
- **supporting_reason:** When the builder evolves, replaying these mechanisms reveals whether guidance, gates, and interpretation rules still match behavior.
- **counterargument_or_limit:** Maintaining examples as tests requires separate fixture ownership and versioning beyond this reference.
- **assumptions_and_boundaries:** Promote only high-value recurring examples into executable fixtures and keep explanatory cases lightweight.
- **revision_decision:** Add candidate fixture identifiers and promotion criteria.
- **additional_insight_to_add:** The best examples are seeds for future quality gates because they preserve the reason a check exists, not just its syntax.

## Section 015: Outcome Metrics and Feedback Loops
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names uncertainty reduction, premature pattern choice, and refresh cadence but does not define measurable signals for whether rough mapping improved a real decision.
- **supporting_reason:** Outcome review needs separate measures for input coverage, artifact integrity, sampled evidence quality, context efficiency, reproducibility, escalation, decision correction, and downstream defects.
- **counterargument_or_limit:** Measurement can cost more than the orientation workflow and encourage optimizing the record rather than the engineering outcome.
- **assumptions_and_boundaries:** Use a small metric set tied to recurring or consequential decisions, not mandatory telemetry for every navigation lookup.
- **revision_decision:** Define metric cards with purpose, numerator, denominator, sampling rule, interpretation, and feedback action.
- **additional_insight_to_add:** Metrics should reveal where evidence failed in the pipeline, not compress every outcome into one map-quality score.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default is to establish a local baseline, trend stable definitions over time, and pair each quantitative signal with mismatch narratives and decision consequence.
- **supporting_reason:** Repository languages, tooling, architecture, and task mix differ too much for universal accuracy or speed thresholds, while local trends can reveal regressions and useful upgrades.
- **counterargument_or_limit:** Local baselines can normalize poor performance if no external or authoritative comparison is ever introduced.
- **assumptions_and_boundaries:** Periodically compare against stronger project evidence and deliberate counterexamples rather than relying only on historical self-comparison.
- **revision_decision:** Add local calibration and independent-audit rules.
- **additional_insight_to_add:** A baseline is a navigation instrument, not an acceptance standard; it shows change but does not define adequacy for every decision.

### Question 03: When does the default work well?
- **current_section_observation:** Metric-driven feedback works well for repeated map automation, stable repositories, recurring reviews, tool upgrades, and teams that retain mismatch and decision records.
- **supporting_reason:** Repeated comparable runs provide denominators and reveal whether changes improve one stage while harming another.
- **counterargument_or_limit:** One-off repositories and rapidly changing architectures may not produce comparable cohorts.
- **assumptions_and_boundaries:** In sparse settings use qualitative postmortems and focused fixtures instead of unstable aggregate ratios.
- **revision_decision:** Define minimum sample and comparability questions before trend interpretation.
- **additional_insight_to_add:** Controlled fixture metrics and production-decision metrics answer different questions and should never be pooled silently.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Metrics fail when agents optimize visible edge count, low unresolved count, short context, or fast completion without preserving correctness and appropriate escalation.
- **supporting_reason:** Resolver overreach can reduce unresolved rows by creating false internal edges, while premature stopping can improve time metrics and increase missed consumers.
- **counterargument_or_limit:** Guardrails and balanced measures can reduce but not eliminate gaming or Goodhart effects.
- **assumptions_and_boundaries:** Pair efficiency measures with contradiction, defect, and evidence-sufficiency checks; review incentives explicitly.
- **revision_decision:** Add misuse warnings and counter-metrics to every easily gamed signal.
- **additional_insight_to_add:** A metric becomes dangerous when its easiest improvement bypasses the uncertainty it was meant to measure.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include qualitative review notes, controlled fixtures, random sampling, stratified sampling, full semantic comparison, user feedback, defect tracking, and time-on-task measurement.
- **supporting_reason:** Fixtures isolate mechanisms; samples estimate target behavior; semantic comparison is stronger but expensive; user and defect outcomes capture downstream value but have confounders and delay.
- **counterargument_or_limit:** Combining all methods can create a measurement program larger than the tool itself.
- **assumptions_and_boundaries:** Select measures based on the change being evaluated and the error class that could affect decisions.
- **revision_decision:** Add a metric-selection guide by feedback latency and evidence strength.
- **additional_insight_to_add:** Leading indicators should trigger early investigation, while lagging outcomes validate whether those indicators actually predict safer decisions.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Measurement hazards include denominator drift, convenience samples, duplicate rows, changing tool branches, mixed repository revisions, survivorship bias, unrecorded escalations, and treating unresolved as automatically bad.
- **supporting_reason:** These defects can reverse apparent trends or reward aggressive but incorrect resolution.
- **counterargument_or_limit:** Perfectly controlled operational data is rarely available during routine coding.
- **assumptions_and_boundaries:** Retain cohort identity and uncertainty, and refuse comparisons when definitions or observation conditions materially differ.
- **revision_decision:** Add comparability metadata and a no-comparison state.
- **additional_insight_to_add:** Missing or incomparable data is itself useful when it exposes that the workflow lacks reproducible provenance.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good report says sampled pointer validity improved under the same stratification while relation mismatches stayed stable; a bad report celebrates more edges without checking false positives.
- **supporting_reason:** The good example holds definitions and counter-metrics steady, whereas the bad example rewards volume detached from decision quality.
- **counterargument_or_limit:** A borderline single incident can justify a gate change even without aggregate significance when consequence is severe.
- **assumptions_and_boundaries:** Separate anecdotal sentinel events from trend estimates and document why each drives action.
- **revision_decision:** Include metric interpretation examples and forbidden conclusions.
- **additional_insight_to_add:** One high-consequence counterexample can set a safety boundary, while aggregate trends guide optimization inside that boundary.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify metric claims by freezing definitions, reproducing queries, auditing sample selection, recalculating numerators and denominators, checking raw evidence, and comparing with an independent mechanism.
- **supporting_reason:** This prevents dashboard summaries from becoming untraceable claims and detects arithmetic or cohort mistakes.
- **counterargument_or_limit:** Independent audits consume reviewer time and may still share hidden assumptions.
- **assumptions_and_boundaries:** Audit material trend changes and tool-release decisions more deeply than routine snapshots.
- **revision_decision:** Add a metric claim card and review cadence linked to consequence.
- **additional_insight_to_add:** Metrics need provenance and invalidation just like dependency claims because their meaning changes when producer, sample, or repository state changes.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The pipeline offers countable artifacts and reproducible checks, but no local dataset currently establishes baseline values, target thresholds, productivity improvement, or defect reduction.
- **supporting_reason:** This evolution did not generate target maps or collect longitudinal outcomes.
- **counterargument_or_limit:** Some invariant metrics, such as schema consistency or pointer bounds, can have deterministic pass criteria without historical data.
- **assumptions_and_boundaries:** Distinguish contract gates from empirical performance indicators and avoid reporting unmeasured outcomes.
- **revision_decision:** Mark all proposed metrics as definitions for future capture rather than current results.
- **additional_insight_to_add:** Deterministic integrity gates and statistical quality measures should remain separate so a guaranteed schema property is not confused with estimated semantic accuracy.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Feedback should update routing and observation contracts, not merely tune extraction: recurring misses may show that a claim class should bypass the rough mapper entirely.
- **supporting_reason:** Improving a lexical resolver cannot make runtime-only relationships observable, while mismatch data can identify where semantic escalation pays off.
- **counterargument_or_limit:** Tool capability may evolve enough to absorb some previously external relation classes.
- **assumptions_and_boundaries:** Reevaluate boundaries after verified implementation changes and keep prior metrics tied to their producer version.
- **revision_decision:** Add feedback actions of fix, document, reroute, retire, or expand only with evidence.
- **additional_insight_to_add:** The highest-value metric outcome may be discovering that a workflow should stop earlier and hand a claim to a different evidence system.
