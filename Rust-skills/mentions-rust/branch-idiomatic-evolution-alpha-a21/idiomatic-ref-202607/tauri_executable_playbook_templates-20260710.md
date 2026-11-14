# Tauri Executable Playbook Templates

**Decision supported.** This section helps decide when a Tauri task must be converted into executable requirement contracts, a layered design plan, and a verification matrix before any implementation begins. The seed title names the theme but never states that its subject is a spec-first work-packet discipline that turns vague desktop requests into REQ-TAURI contracts, layered designs, and test plans.

**Recommended default and causal basis.** Open the local specs playbook first and produce a work packet with requirement contracts, a frontend-to-Rust design scaffold, and a verification matrix before writing application code. A Tauri change crosses at least three trust boundaries, the webview frontend, the IPC command layer, and the Rust core, and untyped requests sail through compilation while failing at exactly those boundaries.

**Operating conditions and assumptions.** The task is a desktop feature with a describable trigger and observable behavior, the team can name windows and permissions involved, and at least one test type can exercise the crossing from frontend to Rust. This reference governs spec and planning discipline for Tauri desktop work and does not by itself teach Tauri APIs, prescribe UI frameworks, or authorize changes to capability files without review.

**Failure boundary and alternatives.** The request is a one-line prototype spike where packet ceremony costs more than the code, the work is pure frontend styling that never crosses IPC, or requirements churn so fast the contracts are stale before red. Bounded alternatives and recoveries: code-first exploration for throwaway spikes, a lightweight checklist for frontend-only changes, or full architecture review with security sign-off when capabilities and sidecars change.

**Counterexample, gotchas, and operational comparison.** Packet templates can be filled ritually with untestable prose, requirement IDs can drift from the tests that claim them, and a beautiful design scaffold can hide that nobody validated the permission set. Good: a sync feature packet with three REQ-TAURI contracts each traced to a named test. Bad: a packet whose only requirement says the app should work reliably. Borderline: skipping the packet for a spike but writing contracts before the spike is promoted.

**Verification, evidence, and uncertainty.** Check that every requirement uses WHEN-THEN-SHALL form with one behavior per SHALL line, that the matrix maps each REQ-TAURI ID to at least one test, and that the design scaffold answers all six layer questions. The local playbook supplies the complete work packet shape, contract template, design table, matrix example, and TDD loop that this file operationalizes. How much packet ceremony is worth paying for small tasks is a judgment call the playbook does not quantify, so teams must tune the threshold from their own defect history.

**Second-order consequence.** A template's value is realized at the boundary crossings it forces the author to name; a packet that never mentions windows, permissions, or IPC shapes has not yet engaged with Tauri at all.

**Revision decision.** State up front that the theme is spec-first work-packet discipline for desktop features crossing webview, IPC, and Rust boundaries.

**Retained seed evidence.** The exact theme title and its framing as playbook templates for Tauri executables remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which evidence source should back each kind of claim this reference makes about Tauri spec, design, and verification practice. The seed map lists one local playbook and three public URLs with equal factual labels, without recording that only the local file was read or which claims each external link could actually support.

**Recommended default and causal basis.** Treat the local specs playbook as the sole verified source for templates and process, and hold the Tauri docs, Tauri repository, and Rust API guidelines as unrefreshed candidates until a claim is checked against them. Every template, contract form, and loop this reference teaches is traceable to the single local playbook, while nothing in this corpus records a retrieval of the three public pages at any date.

**Operating conditions and assumptions.** Rows carry a path or URL, an artifact role, a confidence label, and the synthesis role that tells a reader which claims that source may support. The map assigns provenance for this document's claims and cannot certify that Tauri 2 APIs, capability schemas, or release practices still match what the local playbook assumed when written.

**Failure boundary and alternatives.** The external rows are cited as current facts, the single local source is treated as an ecosystem consensus, or a claim about permissions or IPC is attributed to a page nobody opened. Bounded alternatives and recoveries: add a retrieval-date column and refresh ritual, demote external rows to candidate status explicitly, or expand the local corpus with a second Tauri artifact before promoting any claim to canonical.

**Counterexample, gotchas, and operational comparison.** One local source means no corroboration exists for any template choice, URL rows rot silently as Tauri versions ship, and a confident-sounding synthesis role can launder an unverified link into authority. Good: citing the playbook for the WHEN-THEN-SHALL contract form it literally contains. Bad: citing v2.tauri.app for a capability default no one checked. Borderline: using the Rust API guidelines link for error-type naming while labeling the advice unrefreshed.

**Verification, evidence, and uncertainty.** Open the local playbook and match each claimed template to its section, then record for each external row whether any statement in this file actually depends on it. The local playbook was read in full and contains every template, table, and loop this reference describes. Whether the three public sources still agree with the playbook's assumptions is unknown here, so external agreement remains an unchecked hypothesis rather than a mapped fact.

**Second-order consequence.** A source map with one read source is a provenance ledger, not a triangulation; its honest job is to say so before an agent treats convergence as evidence.

**Revision decision.** Mark the three external rows as unrefreshed candidates and record that the local playbook is the only read source.

**Retained seed evidence.** All four source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/tauri-executable-specs-01/references/tauri-executable-specs-playbook.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://v2.tauri.app/ | external_research_source_material | external_research_sourced_fact | primary Tauri 2 application and security documentation |
| https://github.com/tauri-apps/tauri | external_research_source_material | external_research_sourced_fact | desktop runtime implementation and release surface |
| https://github.com/rust-lang/api-guidelines | external_research_source_material | external_research_sourced_fact | Rust-facing API and error design reference |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which practices deserve default adoption when planning Tauri work, ranked by the cost of the failures they prevent. The seed scoreboard awards 95, 91, and 88 to three generic corpus-hygiene patterns and never ranks the playbook's own load-bearing practices, executable requirement contracts, layered design scaffolds, verification matrices, or least-privilege capabilities.

**Recommended default and causal basis.** Rank requirement-contract writing, boundary-typed IPC design, verification-matrix traceability, and least-privilege capability scoping ahead of generic source hygiene, because those four intercept the desktop failures this theme exists to prevent. A wrong permission or an untyped invoke payload ships a runtime defect into a packaged binary on user machines, while a missed source citation costs only a documentation fix.

**Operating conditions and assumptions.** Each row names an observable failure the pattern prevents, the tier states when adoption is default versus situational, and scores are read as relative priority rather than measurements. The scoreboard ranks planning patterns for this theme and does not grade Tauri plugin quality, frontend framework choices, or the team's general Rust practices.

**Failure boundary and alternatives.** Numeric scores are quoted as evidence in design debates, low-ranked patterns are skipped entirely rather than deprioritized, or the ranking freezes while Tauri's security model evolves under it. Bounded alternatives and recoveries: replace scores with a prevented-failure severity column, order rows by observed defect classes from past Tauri work, or collapse the tier system to default-versus-situational flags.

**Counterexample, gotchas, and operational comparison.** Unsourced numbers acquire false authority through repetition, three near-tied scores give no real ordering signal, and pattern names can drift from the sections that define them. Good: adopting contract-first specs because untyped IPC defects dominated the last release. Bad: citing the 95 score as proof in a review. Borderline: keeping the numeric column while documenting that values are editorial priority, not measurement.

**Verification, evidence, and uncertainty.** Trace each scoreboard row to the section that operationalizes it, and check that the highest-ranked rows correspond to failure classes the failure-mode table actually lists. The playbook's own emphasis, one testable behavior per SHALL line, thin command layers, and least-privilege capabilities, identifies which patterns carry the real weight. No defect data exists in this corpus to calibrate scores, so any ordering is editorial judgment awaiting real incident history.

**Second-order consequence.** A scoreboard that omits the theme's own core practices trains agents to optimize hygiene while shipping the expensive failures unranked.

**Revision decision.** Add the playbook's contract, design, matrix, and capability patterns as ranked rows and label all scores editorial.

**Retained seed evidence.** All three scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `tauri_executable_playbook_templates` | 95 | default_adoption_pattern_tier | Source Map First: Load local tauri executable material before synthesizing playbook templates recommendations. |
| `tauri_executable_playbook_templates` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `tauri_executable_playbook_templates` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single governing claim should orient an agent before it reads any other section of this reference. The seed thesis counts source paths and repeats the generic load-local-then-external formula without stating the theme's actual thesis, that Tauri work becomes reliable when specs are executable and every layer boundary is typed, permissioned, and tested.

**Recommended default and causal basis.** State the thesis as: convert vague desktop requests into WHEN-THEN-SHALL contracts, design the frontend, command, core, state, capability, and lifecycle layers explicitly, and prove each requirement through the smallest sufficient test mix. An orienting thesis determines what an agent looks for in every later section, and a retrieval-order slogan orients it toward file loading instead of toward the boundary discipline that prevents desktop defects.

**Operating conditions and assumptions.** The statement keeps its three evidence-boundary labels so local facts, external facts, and inference stay distinguishable at the moment of synthesis. The thesis governs how this reference is used and does not summarize Tauri's full security model or replace reading the playbook when templates must be reproduced exactly.

**Failure boundary and alternatives.** The thesis is quoted as a substitute for the playbook's templates, the inference label is dropped in reuse, or the statement hardens into policy while the underlying playbook is revised. Bounded alternatives and recoveries: phrase the thesis as a falsifiable claim about defect classes, split it into one sentence per evidence label, or replace it with the playbook's own opening usage sentence.

**Counterexample, gotchas, and operational comparison.** Synthesis statements get copied into prompts verbatim and outlive their sources, and a sentence mixing fact and inference without labels reads as pure fact downstream. Good: an agent using the thesis to demand contracts before code. Bad: quoting the thesis as proof that external docs agree with the playbook. Borderline: paraphrasing the thesis in a prompt while keeping its labels intact.

**Verification, evidence, and uncertainty.** Check that each thesis clause carries an evidence label, that the local clause matches what the playbook literally supports, and that no clause asserts external agreement without a retrieval record. The playbook's opening line, use this when a task needs executable requirements, design planning, TDD sequencing, or a verification plan, directly supports the executable-spec thesis. Whether the ecosystem currently endorses this exact discipline is unverified, so the combined-inference clause remains inference rather than observed consensus.

**Second-order consequence.** The thesis is the highest-leverage sentence in the file because agents that read nothing else will still act on it; it must therefore carry the theme's real center of gravity.

**Revision decision.** Restate the combined inference around executable contracts and typed, permissioned, tested layer boundaries.

**Retained seed evidence.** All three labeled thesis lines, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `tauri_executable_playbook_templates` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Tauri Executable Playbook Templates comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which local artifact an agent must open, and which parts of it to trust, when this reference's summaries are not detailed enough to act on. The seed map lists the single playbook path with truncated heading signals and a generic usage role, without telling the reader which of its eight numbered sections answers which planning need.

**Recommended default and causal basis.** Route contract questions to the requirement template section, layering questions to the design scaffold, test-selection questions to the verification matrix and skeletons, and process questions to the TDD loop and review questions. A one-row map earns its place only by resolving to the right subsection, since the playbook's eight sections serve distinct planning moments and reading it linearly under time pressure invites skimming.

**Operating conditions and assumptions.** The row records the exact path, the section-level table of contents as heading signals, and the usage role that tells an agent when summary reading must give way to full reading. The map covers this theme's local evidence only and does not claim the archive holds no other Tauri material, nor that the playbook covers plugins, mobile targets, or store distribution.

**Failure boundary and alternatives.** The truncated signal column hides sections the agent needed, the single row is read as proof of corpus completeness, or the archive path is assumed stable across future reorganizations. Bounded alternatives and recoveries: expand the row into a per-section routing table, add a hash to detect content drift, or record sibling files in the same skill directory as secondary context.

**Counterexample, gotchas, and operational comparison.** Heading signals cut mid-word invite wrong guesses about content, one mapped source gives no fallback when it is silent, and path-based trust breaks silently if the file moves. Good: opening section three of the playbook for a managed-state question the summary cannot answer. Bad: answering a capability question from the truncated signal list alone. Borderline: citing the playbook's TDD loop from memory while flagging that exact wording needs the file.

**Verification, evidence, and uncertainty.** Open the mapped path, confirm its table of contents matches the recorded signals, and walk one real question from this reference to the specific playbook section that answers it. The mapped playbook exists at the recorded path and its eight sections, packet, contracts, scaffold, matrix, loop, skeletons, rewrites, and review questions, were read in full. Whether adjacent archive directories hold additional Tauri sources is unexplored here, so single-source status describes the map, not necessarily the corpus.

**Second-order consequence.** A source map is an index, and an index that stops at the file level pushes the real lookup cost onto every future reader at their moment of least patience.

**Revision decision.** Add per-section routing guidance and repair the truncated heading-signal list.

**Retained seed evidence.** The single source row with its path, title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/tauri-executable-specs-01/references/tauri-executable-specs-playbook.md | Tauri Executable Specs Playbook | Tauri Executable Specs Playbook; Table of Contents; 1) Tauri Work Packet Template; Tauri Work Mode; Executable Requirements; REQ-TAURI-001.0: <title> | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide which public sources should be consulted, and for what, when this reference's local evidence is stale or silent on a Tauri question. The seed map lists three URLs with usage roles but no retrieval record, no version anchor, and no statement of which local claims each source could confirm or contradict.

**Recommended default and causal basis.** Consult v2.tauri.app for capability, permission, and IPC semantics, the tauri-apps repository for release and breaking-change signals, and the Rust API guidelines for error and interface design, always recording the date and version consulted. Tauri 2 reorganized its security model around capability files, so permission guidance goes stale at framework major versions faster than spec-writing discipline does, and dated retrieval records are what distinguish refreshed facts from folklore.

**Operating conditions and assumptions.** Each row keeps its evidence-boundary label so an external fact remains distinguishable from local fact and inference when statements are reused downstream. The map directs freshness checks and cannot substitute for the local playbook's templates, which encode workflow choices no public documentation will make for a specific team.

**Failure boundary and alternatives.** A URL is cited for a claim it never contained, documentation for a different major version answers a version-specific question, or external guidance silently overrides a deliberate local convention. Bounded alternatives and recoveries: pin sources to versioned documentation paths, add the Tauri release notes as an explicit fourth row, or route ecosystem questions through the future-refresh queries section instead of ad hoc searching.

**Counterexample, gotchas, and operational comparison.** Documentation sites restructure and break deep links, repository README claims lag released behavior, and general Rust guidelines can conflict with Tauri-specific serialization constraints at the IPC boundary. Good: checking current capability schema on v2.tauri.app before editing permission files and recording the date. Bad: quoting this map as proof the ecosystem endorses the playbook. Borderline: applying a Rust API guideline to command error types while noting Tauri's serialization bounds.

**Verification, evidence, and uncertainty.** Resolve each URL, record what was actually read and when, and note for each row one local claim it confirmed, contradicted, or did not address. The three mapped sources are the authoritative public surfaces for Tauri semantics, release history, and Rust interface conventions respectively. None of the three sources was retrieved during this evolution, so their current content and agreement with the playbook remain unverified.

**Second-order consequence.** External sources are clocks as much as references; their value lies in dating the local corpus, and an undated citation cannot even do that.

**Revision decision.** Add retrieval-status and version-anchor expectations and state what each source can and cannot confirm.

**Retained seed evidence.** All three external rows with their names, usage roles, and evidence-boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://v2.tauri.app/ | Tauri documentation | primary Tauri 2 application and security documentation | external_research_sourced_fact |
| https://github.com/tauri-apps/tauri | Tauri repository | desktop runtime implementation and release surface | external_research_sourced_fact |
| https://github.com/rust-lang/api-guidelines | Rust API Guidelines | Rust-facing API and error design reference | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which recurring failures in Tauri planning work deserve standing names, detection signals, and prescribed replacements. The seed registry lists three corpus-hygiene failures but omits the desktop-specific anti-patterns the playbook itself campaigns against, vague untestable requirements, fat command layers, over-broad capabilities, and lifecycle behavior left as an afterthought.

**Recommended default and causal basis.** Extend the registry with vague-requirement drift, business logic embedded in command handlers, wildcard or window-mismatched permissions, unsupervised sidecars, and untested lifecycle paths, each with a detection signal a reviewer can apply. Anti-patterns pay off during review triage, and a reviewer armed only with hygiene failures will approve a packet whose requirements are untestable and whose capability set grants the whole filesystem.

**Operating conditions and assumptions.** Each row names the failure, the risk that makes it expensive, the safer replacement pattern, and a detection method executable from the packet or diff alone. The registry covers planning and spec failures for this theme and does not enumerate Rust language anti-patterns or frontend framework misuse, which belong to their own references.

**Failure boundary and alternatives.** Rows describe failures too abstractly to match a live diff, the replacement pattern is just the failure negated, or the registry grows unpruned until reviewers skim past it. Bounded alternatives and recoveries: order rows by observed frequency once review history accumulates, link each row to the checklist item that operationalizes it, or fold rare rows into failure families with shared detection.

**Counterexample, gotchas, and operational comparison.** Two anti-patterns often co-occur and mask each other, and a named registry can create false comfort that unlisted failures are rare. Good: rejecting a packet whose requirement says handle errors gracefully, citing the vague-requirement row. Bad: approving broad filesystem capability because only hygiene rows were checked. Borderline: allowing a temporarily fat command handler with a named extraction task and deadline.

**Verification, evidence, and uncertainty.** Apply each detection signal to one real packet or diff and confirm it fires on a seeded violation, then check every registry row has a corresponding rewrite pattern or design rule elsewhere in the file. The playbook's authoring rules, rewrite table, and design rules explicitly name vague statements, thin command surfaces, and least-privilege scoping as the behaviors at stake. Actual frequency ranking of these failures in this team's Tauri work is unknown, so row order encodes expected rather than observed cost.

**Second-order consequence.** A registry is the file's immune memory; failures it does not encode will be re-discovered at integration time, at the most expensive possible moment.

**Revision decision.** Add desktop-specific anti-pattern rows for vague requirements, fat commands, over-broad capabilities, sidecar neglect, and untested lifecycle.

**Retained seed evidence.** All three seed rows, context-free summaries, unsourced claims, and unverified instructions, with their detection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which commands and checks must pass before Tauri planning work, and the reference itself, may be called verified. The seed gate names a single repository verifier for editing this file and is silent about the quality gates the playbook demands for actual Tauri work, fmt, clippy, Rust tests, Rust build, frontend checks, and tauri checks.

**Recommended default and causal basis.** Keep the reference verifier for document edits and add the playbook's six-gate set for Tauri work itself, requiring each gate's result to be recorded in the work packet before completion is claimed. A gate section that verifies only the documentation trains agents to treat green markdown as green software, while the playbook's packet template reserves explicit lines for each quality gate result precisely to prevent that substitution.

**Operating conditions and assumptions.** Each gate names its command or check, the layer it protects, and where its result is recorded, so a reviewer can audit completion claims from the packet alone. Gates verify process and code health for this theme's work and do not replace the verification matrix, which maps individual requirements to individual tests.

**Failure boundary and alternatives.** Gates are run selectively and only passing results recorded, a green build is read as requirement satisfaction, or the gate list drifts from the commands the repository actually supports. Bounded alternatives and recoveries: wire gates into CI so recording is automatic, stage gates by layer so frontend changes skip Rust-only checks, or accept a documented manual review when a platform gate cannot run locally.

**Counterexample, gotchas, and operational comparison.** Clippy and fmt configuration differ across workspaces, tauri checks vary by platform target, and a gate command copied from documentation can silently no-op in a differently structured repo. Good: a packet whose quality-gate block shows all six results with the failing one owned and scheduled. Bad: claiming done with an empty gate block. Borderline: shipping with a documented platform-specific gate skipped on the local machine.

**Verification, evidence, and uncertainty.** Run each gate on a real slice of Tauri work, confirm results land in the packet's quality-gate block, and check the recorded commands exist in the target repository. The playbook's work packet template enumerates fmt, clippy, rust tests, rust build, frontend checks, and tauri checks as required result lines. Exact gate invocations depend on each repository's tooling, so the six-gate set names obligations while concrete commands remain per-project judgment.

**Second-order consequence.** Gates define what completion means; any gate left implicit will be satisfied implicitly, which is to say not at all.

**Revision decision.** Add the playbook's six quality gates with recording obligations alongside the document verifier.

**Retained seed evidence.** The repository verifier command and its run-after-editing instruction remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide whether an agent facing a task should open this reference, and once open, in what order to consume its sections. The seed guide gives four generic bullets, load local first, prefer gated patterns, treat external as freshness, keep labels, without saying which task shapes this theme serves or which sections answer which planning moment.

**Recommended default and causal basis.** Open this reference when a task must cross from frontend intent to Rust behavior in a packaged desktop app, then consume it as contracts first, design scaffold second, verification matrix third, gates last. Usage guides succeed by matching task shape to reading order, and a Tauri task's natural planning order, what must be true, how layers divide it, how it is proven, mirrors the playbook's own template sequence.

**Operating conditions and assumptions.** The agent has a concrete task, can identify whether IPC, permissions, or lifecycle are implicated, and is permitted to spend planning effort before implementation. The guide routes agents into this reference and does not rank it against other corpus references, which is the adjacent-routing section's job.

**Failure boundary and alternatives.** An agent opens this file for a pure frontend styling task, reads it linearly during an incident when only the failure table was needed, or follows the reading order while skipping the contracts it exists to produce. Bounded alternatives and recoveries: encode the guide as if-then routing rules keyed to task properties, add a thirty-second triage path for urgent tasks, or fold usage guidance into the journey scenario.

**Counterexample, gotchas, and operational comparison.** Generic bullets satisfy checklists without changing behavior, and reading-order advice is ignored precisely by the overloaded agents who need it most. Good: an agent with a sync feature reading contracts, scaffold, then matrix, and producing a packet. Bad: an agent citing this file's thesis while writing code with no contracts. Borderline: an agent skipping to the failure table mid-incident, then backfilling the packet afterward.

**Verification, evidence, and uncertainty.** Walk two contrasting tasks, one IPC-crossing and one frontend-only, through the guide and confirm it admits the first, routes the second away, and produces the right section order. The playbook's opening usage sentence and numbered section order directly support the task-shape trigger and the contracts-design-verification reading sequence. How often agents follow reading-order advice under time pressure is unmeasured, so the guide's practical compliance rate is unknown.

**Second-order consequence.** A decision guide is the file's front door; if it cannot turn away the wrong visitor it also cannot be trusted to seat the right one.

**Revision decision.** Add task-shape admission criteria and a section-order reading path.

**Retained seed evidence.** The usage trigger sentence and all four seed bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide which concrete situation should anchor a reader's mental model of when and how this reference gets used end to end. The seed scenario names a team, a frontend action crossing into Rust, and a boundary decision, but stops before showing the journey's outcome, what packet was produced, what the verification matrix caught, and how the team knew it was done.

**Recommended default and causal basis.** Extend the scenario through its full arc, the team drafts REQ-TAURI contracts, fills the six-layer design scaffold, builds a verification matrix, runs the stub-to-verify loop, and closes with recorded quality gates. Journeys teach by completeness, and a scenario that ends at the decision point leaves the reader without the payoff image, a traceable packet, that makes the discipline feel worth its cost.

**Operating conditions and assumptions.** The scenario keeps its four seed elements, role, starting state, decision, and opening trigger, so the extended arc stays anchored to the same persona and task. The scenario illustrates one representative journey and does not enumerate all task shapes this reference serves, nor claim every journey needs the full template set.

**Failure boundary and alternatives.** The persona drifts from the tasks real users bring, the arc becomes an advertisement in which nothing goes wrong, or the scenario hardens into the only sanctioned workflow. Bounded alternatives and recoveries: add a second mini-journey for a lifecycle-only task, include a mid-journey failure where a vague requirement is rewritten, or anchor the journey to a real journaled task once one exists.

**Counterexample, gotchas, and operational comparison.** Scenarios written after templates tend to justify the templates rather than test them, and a frictionless story teaches less than one where the matrix catches a real gap. Good: a journey where spec review rejects an untestable SHALL line and the rewrite table repairs it. Bad: a journey that ends with the team feeling confident. Borderline: a synthetic journey labeled illustrative pending a real logged case.

**Verification, evidence, and uncertainty.** Walk the extended scenario against the playbook's templates step by step and confirm each journey stage names the artifact it produces and the section that governs it. The seed's frontend-action-into-Rust-commands framing matches exactly the boundary crossing the playbook's design scaffold is organized around. No journaled real-world run of this journey exists in the corpus yet, so the scenario remains illustrative rather than evidentiary.

**Second-order consequence.** An unfinished journey teaches readers to start; only a finished one teaches them what done looks like, and done is the harder lesson.

**Revision decision.** Extend the journey through packet, matrix, loop, and gate stages to a verifiable completion.

**Retained seed evidence.** The role-based opening, starting state, decision line, and reference opening trigger remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Tauri desktop app team is starting from a frontend action that must cross into Rust commands and platform permissions and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `tauri_executable_playbook_templates` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the safest command, permission, IPC, packaging, and verification boundary.
Reference opening trigger: Open this file when the task mentions tauri executable playbook templates, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide whether to adopt, adapt, or avoid the playbook-template discipline for a specific Tauri task, and what each route costs when chosen wrongly. The seed table keys adopt, adapt, and avoid to generic local-versus-external evidence agreement rather than to the task properties that actually govern the choice, boundary crossings, permission changes, and requirement stability.

**Recommended default and causal basis.** Adopt full packets when the task crosses IPC or touches capabilities, adapt by trimming template sections for small bounded changes, and avoid the ceremony for throwaway spikes that will not be promoted. The cost of skipping contracts scales with the number of trust boundaries a change crosses, so boundary count and permission impact predict the value of the discipline far better than whether two document sets agree.

**Operating conditions and assumptions.** Each row names its triggering task property, the cost accepted, the recovery if wrong, and a verification question answerable from the packet or diff. The guide ranks planning-discipline choices for this theme and cannot authorize permission changes, releases, or scope the user has not granted.

**Failure boundary and alternatives.** Adopt is chosen because sources agree while the task is a spike, adapt quietly drops the verification matrix that was the point, or avoid becomes the habitual route for work that ships to users. Bounded alternatives and recoveries: run a one-contract pilot before committing to the full packet, defer the matrix but not the contracts for exploratory work, or ask the user when task stability is unknowable.

**Counterexample, gotchas, and operational comparison.** Template trimming removes exactly the sections that felt tedious, which are often the boundary ones, and spike code has a well-known habit of getting promoted without its missing contracts. Good: full packet for a feature adding filesystem access to a window. Bad: skipping contracts on a promoted spike because it already worked. Borderline: adapting to contracts-plus-gates only for a one-file fix, documenting the dropped sections.

**Verification, evidence, and uncertainty.** Answer each row's verification question from real artifacts, and trace one adopt and one avoid decision to its outcome to test whether the trigger predicted the cost. The seed's four-row adopt-adapt-avoid-cost skeleton and verification-question column provide reusable scaffolding for the rekeyed conditions. True costs of wrong routes depend on unmeasured task coupling and promotion rates, so cost wording remains judgment rather than measurement.

**Second-order consequence.** A tradeoff guide earns trust only when its avoid route is genuinely usable; a guide whose every path leads to adoption is a mandate wearing a decision's clothes.

**Revision decision.** Rekey each row from evidence agreement to boundary crossings, permission impact, and requirement stability.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the tauri executable playbook templates pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong tauri executable playbook templates guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide how much authority the single mapped local source should carry and what must happen before its guidance hardens into policy. The seed hierarchy crowns one playbook canonical while its own confidence warning admits single-source thinness, and its reviewer question is a generic contribution prompt no single-row table needs.

**Recommended default and causal basis.** Treat the playbook as provisional canon, authoritative for templates and process until a second local Tauri source or a refreshed external check corroborates or contradicts it. Hierarchy semantics assume competition, and with one row the real question is not ranking but calibration, how far one author's workflow choices should bind future agents without independent confirmation.

**Operating conditions and assumptions.** The row records path, role, heading signals, and a reviewer question, and the confidence warning stays adjacent so canonical status is always read together with its caveat. The hierarchy classifies retrieval priority within this corpus and does not measure the playbook's quality against external Tauri practice, which the research map governs.

**Failure boundary and alternatives.** Provisional canon quietly becomes permanent policy, the confidence warning is dropped in reuse, or a future second source is auto-ranked below the incumbent out of habit. Bounded alternatives and recoveries: actively search the archive for sibling Tauri material before the next revision, add a hash to detect silent edits to the canon, or convert the hierarchy to a calibration statement until a second source exists.

**Counterexample, gotchas, and operational comparison.** Single-source canon is self-reinforcing because every downstream document cites it and manufactures apparent consensus, and truncated heading signals misrepresent what the canon covers. Good: following the playbook's contract form while logging that it is single-source policy. Bad: rejecting a better external pattern because the local canon differs. Borderline: adopting an external capability practice with an inference note pending corpus expansion.

**Verification, evidence, and uncertainty.** Confirm the mapped file still matches its recorded signals, search adjacent archive directories for unmapped Tauri artifacts, and check that downstream citations preserve the confidence warning. The seed's own confidence warning, inviting adjacent-source discovery before canonical policy, already concedes the calibration problem this revision makes explicit. Whether undiscovered local Tauri sources exist is unknown, so single-source status is a statement about the map, not a proven property of the corpus.

**Second-order consequence.** In a one-source corpus the hierarchy's honest output is a confidence interval, not a ranking; pretending otherwise converts an author's habits into unexamined law.

**Revision decision.** Reframe canonical status as provisional pending corroboration and make the reviewer question calibration-specific.

**Retained seed evidence.** The classification vocabulary line, the confidence warning, and the single canonical source row remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/tauri-executable-specs-01/references/tauri-executable-specs-playbook.md | canonical primary source | Tauri Executable Specs Playbook; Table of Contents; 1) Tauri Work Packet Template | What guidance, warning, or example should this source contribute to Tauri Executable Playbook Templates? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete worked artifact must exist before this reference counts as operational for real Tauri planning work. The seed artifact table names goal, boundary, and gate fields but never instantiates them, so nothing demonstrates that the templates can carry one actual desktop feature from request to verified completion.

**Recommended default and causal basis.** Complete one real work packet, requirement contracts, filled design scaffold, verification matrix, and recorded quality gates, for an actual task, and keep it beside this reference as the living proof. An instantiated packet forces every template field to survive contact with a real feature, which exposes missing fields and untestable prose before other agents inherit the templates as gospel.

**Operating conditions and assumptions.** The artifact records the task identity, each REQ-TAURI contract, the six layer decisions, the matrix rows, and the gate results with dates, so a reviewer can audit it without reconstructing the task. The artifact certifies that the templates are usable, not that every future task needs every template section, which the tradeoff guide governs.

**Failure boundary and alternatives.** Fields are filled with restated definitions instead of task facts, the packet is written after implementation to decorate a decision already made, or one stale example certifies templates that have since changed. Bounded alternatives and recoveries: link to a real journaled task instead of a synthetic example, require one artifact per template revision rather than per task, or accept a reviewed dry-run walkthrough labeled as unexecuted when no live task exists.

**Counterexample, gotchas, and operational comparison.** A polished artifact can hide that its task never shipped, and goal statements drift from what the user actually asked once template vocabulary takes over. Good: a packet for a real sync feature with three contracts, six layer decisions, and dated gate results. Bad: a table whose user goal reads apply Tauri playbook templates. Borderline: a simulated packet marked unexecuted but structurally complete.

**Verification, evidence, and uncertainty.** Check each artifact field against the actual task record, rerun or inspect the named gates, and confirm the contracts trace to matrix rows that exist. The seed's three completion rules map directly onto the goal, boundary, and gate stages of the playbook's packet template. How often the artifact must be refreshed as Tauri versions and templates evolve is unmeasured, so its shelf life is maintenance judgment.

**Second-order consequence.** Templates rot invisibly; only an artifact that was actually pushed through a real task can certify that the forms still fit the work.

**Revision decision.** Extend the three-field skeleton into a full packet-instance record with contracts, layer decisions, matrix rows, and dated gate results.

**Retained seed evidence.** The worked-example definition line and the three artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: worked tauri executable playbook templates example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Tauri Executable Playbook Templates | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which uses of this reference should be taught as exemplary, negligent, or conditionally acceptable when coaching an agent through Tauri planning. The seed examples restate the generic load-canon, ignore-paths, and thin-evidence verdicts without showing a single requirement contract, design decision, permission choice, or test outcome.

**Recommended default and causal basis.** Anchor each verdict in a concrete planning event, what contract was written or skipped, what layer decision was made, what the matrix or gates then caught or missed. Examples transfer judgment only when they show action, signal, and consequence together, and a verdict about corpus-loading ritual teaches nothing about the desktop decisions this theme exists to improve.

**Operating conditions and assumptions.** Each example names the task shape, the planning action taken, the observable outcome, and the section of this reference whose rule the verdict applies. The examples teach planning judgment for this theme and do not certify frontend framework choices or Rust idioms beyond the boundary decisions shown.

**Failure boundary and alternatives.** The good case celebrates template compliance rather than outcome, the bad case is a strawman no agent would produce, or the borderline case gives no rule for when its exception expires. Bounded alternatives and recoveries: draw examples from the playbook's own vague-to-executable rewrite table, replace synthetic verdicts with journaled real cases as they accumulate, or add a second borderline covering permission ambiguity.

**Counterexample, gotchas, and operational comparison.** Examples copied into prompts shed the context that made them borderline, and verdicts can encode the author's taste rather than observed consequence. Good: rewriting add a sync feature into a typed invoke contract with a validating command, then tracing it to tests. Bad: coding against window.__TAURI__ globals with no contract and calling the packet done. Borderline: shipping a one-file fix with contracts but a deferred matrix, with the deferral logged.

**Verification, evidence, and uncertainty.** Trace each example to a reproducible scenario, confirm the good case's gates would actually fire on the bad case, and test that the borderline rule states when its exception ends. The playbook's rewrite table already pairs vague statements with executable rewrites, providing ready-made before-and-after material for grounded examples. Which borderline situations occur most often in this team's Tauri work is unknown, so the chosen third case reflects judgment about likely ambiguity.

**Second-order consequence.** An example set is the reference's practice field; if nothing in it could actually happen on a real task, agents will meet their first real decision untrained.

**Revision decision.** Rewrite each verdict around a concrete contract, layer, or gate event with its observable outcome.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Tauri Executable Playbook Templates after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Tauri Executable Playbook Templates as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Tauri Executable Playbook Templates only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising this reference or the planning discipline it encodes. The seed metrics name one leading indicator and one failure signal but define no measurement owner, no run population, and no corrective action bound to any threshold.

**Recommended default and causal basis.** Measure requirement-to-test traceability, spec-review rejection reasons, gate-failure classes, and post-release defect boundaries per task, and bind each degraded signal to a named revision of a specific section. Signals form a feedback loop only when a measurement on a defined population is wired to a corrective action; unattached indicators decay into slogans quoted in retrospectives.

**Operating conditions and assumptions.** Each metric states its unit, collection point in the journey, healthy range, breach action, and the owner who applies the correction. These metrics evaluate the reference and its planning discipline, not application performance or team velocity, which need their own instruments.

**Failure boundary and alternatives.** Indicators are averaged across unlike tasks, the failure signal fires only after a release, cadence becomes calendar ritual detached from change events, or breaches accumulate with no revision ever applied. Bounded alternatives and recoveries: sample post-task retrospectives instead of continuous counters, review metrics at template-revision boundaries rather than on a clock, or tie refresh to Tauri release events.

**Counterexample, gotchas, and operational comparison.** Traceability percentages are trivially gamed by writing vaguer requirements, and a green verifier says the document is well-formed, not that its advice is good. Good: reopening the capability guidance after two tasks hit permission-denied defects in packaged builds. Bad: declaring the discipline healthy because the verifier stayed green. Borderline: skipping a scheduled review after a quarter with no Tauri work, recording the skip.

**Verification, evidence, and uncertainty.** Inspect task records for measured values, confirm each breach maps to a committed revision, and check the leading indicator moved after the correction shipped. The seed's cross-layer testability indicator and its permissions-and-IPC failure signal already name the two highest-value measurement surfaces for this theme. Healthy thresholds for rejection and defect rates are unmeasured for this team, so initial ranges are provisional and must be calibrated from real runs.

**Second-order consequence.** A reference without a feedback loop can only degrade, because every Tauri release silently invalidates advice that nothing is measuring.

**Revision decision.** Bind each signal to a unit, population, threshold, owner, and section-level corrective action.

**Retained seed evidence.** The leading indicator, failure signal, and verifier-driven review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the feature can be tested across frontend, Rust command, and packaged desktop behavior.
Failure signal: the reference ignores permissions, IPC risk, or platform-specific verification.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared ready to hand to an agent, and what evidence backs each readiness claim. The seed checklist verifies that sections exist and name things but never asks whether the guidance is internally consistent, executable by an agent, or faithful to the playbook it summarizes.

**Recommended default and causal basis.** Keep the structural items and add content checks, contracts-to-matrix consistency, gate executability, capability guidance matching current Tauri semantics, and fidelity spot-checks against the source playbook, each tick citing its satisfying line. Existence checks catch missing prose cheaply, but the expensive failures are contradictions between sections and gates that cannot run, which only content-level checks with citations intercept.

**Operating conditions and assumptions.** Each item names the section it inspects, the evidence that satisfies it, and whether a script or a human evaluates it. The checklist gates this document's readiness and does not certify outcomes of tasks that later use it, which the metrics section observes.

**Failure boundary and alternatives.** Items are ticked from memory without citations, a structural pass is read as content endorsement, or the checklist freezes while sections evolve and silently stops covering new obligations. Bounded alternatives and recoveries: generate structural items from the repository verifier instead of maintaining them by hand, replace some ticks with paired-reviewer sign-off, or deep-read two random sections per review instead of shallow full passes.

**Counterexample, gotchas, and operational comparison.** Checklists reward completion theater, and reviewers stop reading carefully once early items pass, precisely when later items matter most. Good: ticking the artifact item only after quoting the instantiated packet it requires. Bad: ticking all seven items in one glance because headings exist. Borderline: carrying last revision's consistency tick forward with a staleness note.

**Verification, evidence, and uncertainty.** Demand a line citation per tick, rerun the structural verifier, and spot-check one section pair for actual agreement on defaults and boundaries. The seed's seven items map one-to-one onto sections this file genuinely contains, so the structural layer is sound scaffolding to build on. How much deep review each item deserves per revision depends on edit volume, so review depth remains judgment rather than fixed rule.

**Second-order consequence.** A checklist that can be completed without reading the document measures the checklist, not the document.

**Revision decision.** Append consistency, executability, fidelity, and capability-currency items and require cited evidence for every tick.

**Retained seed evidence.** All seven structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Tauri Executable Playbook Templates.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a task should leave this reference and which neighboring reference should own it instead. The seed routing splits the theme name into tauri, executable, and playbook keywords and points at three unnamed adjacent references, giving an agent no verified destination and no handoff condition.

**Recommended default and causal basis.** Route by task surface, spec-versus-policy questions to the Tauri doctrine and legacy references the guidance line already names, general Rust design depth to Rust-focused references, and agent-workflow questions to the orchestration references, each with carried context. Routing matters exactly when this file stops answering, and only a condition-plus-named-destination pair converts that moment into a next action instead of a keyword-shaped dead end.

**Operating conditions and assumptions.** Each route names its trigger condition, a destination that resolves to a real corpus file, the context to carry across, and what this file retains ownership of after handoff. Routing redirects within this corpus and cannot substitute for the user's prioritization or authorize work in the destination's domain.

**Failure boundary and alternatives.** Keyword overlap routes to a file that merely shares a word, two references both claim a task and neither owns integration, or handoffs drop the packet context and force rediscovery. Bounded alternatives and recoveries: consult the corpus index for exact titles before routing, keep the task here with an explicit gap note when no destination fits, or escalate to the user when two references genuinely conflict over ownership.

**Counterexample, gotchas, and operational comparison.** Adjacent files evolve independently so routes dangle silently, and a plausible-sounding route can hide that the corpus simply lacks the needed reference. Good: routing a migration-policy question to the legacy Tauri reference named in the guidance line while keeping this task's contracts here. Bad: routing to the executable adjacent reference, which exists only as a keyword. Borderline: duplicating one shared gate rule locally with a sync note while routing the rest.

**Verification, evidence, and uncertainty.** Resolve every named destination to an actual corpus file, walk one sample task through each trigger, and confirm no route pair forms an ownerless cycle. The seed's own guidance line already names executable, doctrine, and legacy Tauri references as the real adjacent surfaces, which the keyword stubs then fail to use. The best destination for mixed spec-and-policy tasks depends on task emphasis, so some routings remain judgment calls the agent must record.

**Second-order consequence.** Routing quality is a property of the corpus, not the file; every unresolved route is evidence of a missing or misnamed reference the corpus owner should fix.

**Revision decision.** Replace keyword stubs with trigger-condition routes to named corpus files plus carried-context notes.

**Retained seed evidence.** The adjacency guidance line and the three keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use executable, doctrine, or legacy Tauri references when the task is about specs, policy, or migration.
Adjacent reference 1: consider the tauri adjacent reference when the current task pivots away from tauri executable playbook templates.
Adjacent reference 2: consider the executable adjacent reference when the current task pivots away from tauri executable playbook templates.
Adjacent reference 3: consider the playbook adjacent reference when the current task pivots away from tauri executable playbook templates.

## Workload Model

**Decision supported.** This section helps decide how large a Tauri work slice one packet and one session can safely carry before the discipline itself degrades. The seed model states a one-crate, hundred-symbol, single-integration-path boundary inherited from generic Rust guidance and truncates its own heading-signal cell, without deriving any limit from what actually binds Tauri planning, contract count and cross-layer review.

**Recommended default and causal basis.** Size slices by contract count and boundary spread, a handful of REQ-TAURI contracts whose design decisions and matrix rows one reviewer can hold at once, splitting when contracts multiply or a change spans several windows and capability files. The binding constraint is review comprehension across the six design layers, because each added contract multiplies matrix rows and gate surface faster than code volume grows.

**Operating conditions and assumptions.** The model tracks open contracts, layers touched, capability files affected, matrix rows pending, and gate results outstanding for the active slice. The model bounds one planning slice in one workspace and says nothing about team-level scheduling or multi-app release coordination.

**Failure boundary and alternatives.** Symbol counts are honored while a single capability change fans out across every window, the truncated source-pressure row is copied forward as noise, or slice limits are read as quality guarantees. Bounded alternatives and recoveries: measure per-slice review time and set caps empirically, use a work-in-progress limit on unverified contracts instead of size limits, or split by design layer with an interface freeze between slices.

**Counterexample, gotchas, and operational comparison.** Three trivially independent contracts cost less than one hidden-coupled pair, and numeric caps invite gaming precisely when judgment is most needed. Good: splitting a feature into two packets when its contracts touch both filesystem capabilities and tray lifecycle. Bad: accepting a hundred-symbol slice that rewrites every window's permissions. Borderline: temporarily exceeding the contract cap for read-only design exploration, with implementation still gated.

**Verification, evidence, and uncertainty.** Count contracts, layers, and pending matrix rows per journaled slice, and compare integration failures against slice size to test whether the stated caps predict degradation. The playbook's bounded-packet shape, one work mode, enumerated requirements, one verification matrix, embodies the slice discipline this model quantifies. The numeric caps are unmeasured heuristics and true limits vary with task coupling and reviewer familiarity, so all stated numbers are provisional planning aids.

**Second-order consequence.** Tauri work scales by boundaries crossed, not lines written; a workload model that counts symbols will approve exactly the permission-wide changes it should have split.

**Revision decision.** Rederive boundaries from contract count and layer spread, and repair the truncated heading-signal cell.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Tauri Executable Playbook Templates as a rust system operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | systems implementation, CLI or service hardening, async/runtime review, and safety-sensitive refactoring where compile success is necessary but not sufficient | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one crate or bounded workspace slice, up to 100 changed symbols, and one integration path that exercises error handling | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Tauri Executable Specs Playbook; Table of Contents; 1) Tauri Work Packet Template; Tauri Work Mode; Executable Requirements; REQ-TAURI-001.0: <title> | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked tauri executable playbook templates example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must demonstrate before its guidance is trusted to steer real Tauri planning. The seed table promises a 100 percent boundary-preservation rate and an 18-of-20 routing accuracy without any sampling procedure, sample source, or measurement owner in existence.

**Recommended default and causal basis.** Keep the four target dimensions but ground each in a feasible check, label structure via the verifier, routing accuracy sampled from journaled uses, unsupported claims caught at review, and recovery paths walked during audits, with all thresholds marked unbaselined. Targets create reliability only when someone can actually run the measurement; unmeasurable precision teaches readers to treat every number in the file as decoration.

**Operating conditions and assumptions.** Each target names its metric, method, sample population, evaluating owner, and the corrective action a miss triggers. The targets judge this document's guidance quality, not the reliability of Tauri itself or of applications built with it.

**Failure boundary and alternatives.** Percentages are quoted as achievements rather than aspirations, samples are drawn only from successful tasks, misses trigger no correction, or the zero-unsupported-claim rule quietly exempts this very table. Bounded alternatives and recoveries: start with binary pass-fail audits instead of ratio targets, pool samples across the reference family to reach measurable volume, or replace numeric accuracy with defect review of every miss.

**Counterexample, gotchas, and operational comparison.** A 20-use sample may take months to accumulate for a niche theme, reviewers disagree on what counts as a routing miss, and perfect label hygiene can coexist with substantively wrong advice. Good: auditing five journaled uses and reopening the tradeoff guide after two routing misses. Bad: reporting 18-of-20 accuracy no one measured. Borderline: claiming label preservation from verifier output while flagging that semantic drift is unchecked.

**Verification, evidence, and uncertainty.** Run the verifier for label structure, pull journaled uses for routing outcomes, demand a source row or inference note for every claim, and walk each failure row's recovery path once. The four seed dimensions align with failure classes this corpus has already met, label loss, misrouting, unsupported claims, and dead-end failure guidance. No baseline measurement exists for any target, so current compliance is unknown and the first audit will define achievable thresholds.

**Second-order consequence.** An unmeasured target is worse than none, because it manufactures confidence exactly where the document claims to be most rigorous.

**Revision decision.** Attach a sampling procedure, population, owner, and miss-triggered action to each target and mark all thresholds unbaselined.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failures in Tauri planning and execution deserve standing mitigations and how each is detected before it reaches a packaged build. The seed table pairs two corpus-hygiene rows with two systems rows on runtime contention and panic paths, but omits the desktop failure classes this theme's own sections rank highest, permission misscoping, IPC contract drift, and unowned lifecycle behavior.

**Recommended default and causal basis.** Keep the four seed rows and add capability misscoping, frontend-to-command payload drift, unsupervised sidecar failure, and lifecycle regressions such as broken single-instance handoff, each with an earliest observable signal and detection stage. Failure tables pay off at triage, and triage needs the failures that actually occur at webview, IPC, and packaging boundaries, ranked by blast radius in shipped binaries rather than by genericity.

**Operating conditions and assumptions.** Each row names its trigger, earliest signal, blast radius, containment step, corrective action, and the journey stage where detection belongs. The table covers planning and boundary failures for this theme and cannot enumerate application-domain defects, which belong to each repository's own test regime.

**Failure boundary and alternatives.** Rows describe failures too abstractly to match live symptoms, mitigations restate the failure as an imperative, or detection lands after packaging where evidence is expensive to gather. Bounded alternatives and recoveries: order rows by observed frequency once task history accumulates, link each row to the matrix test type that detects it, or merge overlapping rows into failure families with shared containment.

**Counterexample, gotchas, and operational comparison.** Permission failures often present as generic runtime errors in the webview, and two boundary failures can co-occur and mask each other during triage. Good: catching a capability gap in a mocked-IPC test before packaging. Bad: discovering a permission denial from user crash reports. Borderline: shipping with a known lifecycle edge documented, monitored, and scheduled.

**Verification, evidence, and uncertainty.** Seed one representative failure per row in a drill, confirm the named signal fires at the named stage, and check containment leaves the workspace recoverable. The playbook's verification matrix already assigns mocked-Tauri, lifecycle, and desktop-boundary test types to exactly these failure surfaces. Real frequency and cost rankings await accumulated task data, so today's ordering encodes expected rather than observed risk.

**Second-order consequence.** A failure table that omits the failures its own theme exists to prevent leaves agents triaging desktop incidents with a generic map.

**Revision decision.** Add capability, IPC-drift, sidecar, and lifecycle rows with earliest-signal and detection-stage columns.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| runtime contention masks failure | async tasks, locks, or shared state degrade under concurrent load | add contention benchmark, timeout budget, and structured cancellation path |
| panic path reaches production | unwrap or unchecked invariant survives compile and unit tests | require panic audit, Result propagation, and integration failure fixture |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed planning or verification step should be retried, escalated, or halted, and how work sheds load when gates go red. The seed bullets classify failure causes and cap retries sensibly but never define who classifies, where classifications are recorded, or how a halt releases once the blocking gate recovers.

**Recommended default and causal basis.** Classify each failure once in the task record, allow one bounded retry only for transient or stale-evidence causes, halt new implementation while any quality gate is red, and resume only after the blocking evidence is recorded green. Retries without recorded classification become loops with amnesia, and implementing against red gates multiplies unverifiable work faster than review can absorb it.

**Operating conditions and assumptions.** The guidance assumes recorded task journals, gates that report red or green unambiguously, and an agent empowered to pause its own implementation. This governs retry of planning and verification steps, not application-level retry logic inside the Tauri code being written, which belongs in requirement contracts.

**Failure boundary and alternatives.** A true contract contradiction is retried as if transient, a halt lifts because time passed rather than because evidence changed, or escalation has no named recipient. Bounded alternatives and recoveries: escalate immediately for authority or requirement-contradiction failures instead of consuming the retry, amend the input before any rerun, or hand persistent blockers to a fresh session through the journal.

**Counterexample, gotchas, and operational comparison.** Transient and systematic failures look identical on first occurrence, and rerunning a failed gate unchanged mostly reproduces the failure while consuming the retry budget. Good: one rerun after refreshing a stale external doc, then escalation with the diff attached. Bad: three silent reruns of a failing clippy gate. Borderline: retrying a flaky-looking desktop-boundary test once while logging that flakiness itself is an unverified hypothesis.

**Verification, evidence, and uncertainty.** Audit task records for classification-before-retry ordering, count retries per failure to confirm the bound held, and replay one halt to confirm release required green evidence rather than elapsed time. The seed's four-way failure classification and its checkpoint-before-destructive-step rule match the persistence discipline the playbook's TDD loop already implies. The right retry budget for semantic failures like weak contracts is judgment; one bounded retry is a defensible default, not a derived optimum.

**Second-order consequence.** Backpressure is a memory discipline as much as flow control; a halt that does not record its cause converts recoverable congestion into permanent context loss.

**Revision decision.** Add classification ownership, journal recording, and an evidence-based halt-release condition to the existing rules.

**Retained seed evidence.** All five retry and backpressure bullets, including the one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence each Tauri planning run must emit so a later reader can reconstruct its decisions without replaying the session. The seed bullets say record sources, commands, latencies, and error counters but never state where records live, which journey stage writes them, or who consumes each signal.

**Recommended default and causal basis.** Write observations into the work packet at fixed stages, sources and skips at load, contracts and layer decisions at design, matrix and gate results at verification, and a compact completion audit naming unresolved risks at the end. Evidence captured at the stage that produced it stays accurate and cheap, while end-of-session reconstruction forgets skipped sources and flattens the decision path into a tidy story.

**Operating conditions and assumptions.** The checklist assumes a persistent packet or journal, stage names shared with the journey scenario, and reviewers who read completion audits before accepting work. Observability here serves planning reconstruction and review, not runtime telemetry of the shipped desktop app, which the contracts themselves must specify.

**Failure boundary and alternatives.** Records are written only after success, latency percentiles are quoted for planning work nobody timed, or signals accumulate that no reviewer ever consumes. Bounded alternatives and recoveries: derive counters mechanically from packet structure instead of hand-logging, sample deep audits on a fraction of tasks, or attach evidence to the queue completion notes when no packet exists.

**Counterexample, gotchas, and operational comparison.** Recording effort competes with task effort so pressured sessions log least exactly when it matters most, and summaries can launder a bad decision into a clean narrative. Good: a completion audit naming one skipped gate and one unresolved permission risk. Bad: p95 latency claims for a planning session with no timer. Borderline: retroactively reconstructing one missing design record and labeling it reconstructed.

**Verification, evidence, and uncertainty.** Pick one completed task and rebuild its decision sequence solely from records, then list what could not be recovered and fix the stage that failed to write it. The playbook's packet template already reserves blocks for design decisions, matrix rows, and gate results, making stage-bound recording a matter of filling existing slots. The minimum record set that keeps runs reconstructable without drowning reviewers is workload-dependent and must be tuned from actual audit attempts.

**Second-order consequence.** Observability that depends on discipline fails under pressure; whatever the workflow does not capture structurally will be missing on exactly the runs worth investigating.

**Revision decision.** Bind each recorded signal to a journey stage, storage location, and named consumer, and drop untimed latency claims.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture error count, timeout count, retry count, saturation signal, and rollback trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove this reference improves Tauri planning outcomes enough to justify its reading and maintenance cost. The seed method demands memory, panic, and concurrency evidence with a 10 ms hot-path bound, importing runtime benchmarks into a planning document whose own pass condition is reviewer comprehension.

**Recommended default and causal basis.** Verify this document as decision quality, whether a reader reaches the correct contract form, layer split, and test mix faster and with fewer errors than without it, and reserve the runtime packet for the application requirements the contracts themselves state. A reference performs by changing decisions, so its verification must compare decisions made with and without it rather than timing operations the document never performs.

**Operating conditions and assumptions.** The method assumes representative tasks, at least two comparable runs or reviewers, journaled outcomes to score against, and prior agreement on what the correct next action was. This method evaluates the document's usefulness and does not benchmark Tauri runtime performance, which belongs inside REQ-TAURI contracts with explicit units.

**Failure boundary and alternatives.** Percentile theater replaces judgment, pass is declared because a reviewer liked the prose, or comparison runs differ in task difficulty so the delta is noise. Bounded alternatives and recoveries: run structured walkthroughs where a reviewer must locate five answers with citations, A-B test two versions of one section across tasks, or accept expert review as interim evidence while usage data accumulates.

**Counterexample, gotchas, and operational comparison.** Comprehension tests measure the reader as much as the document, and familiarity makes second runs faster regardless of the reference's quality. Good: timing how quickly a reviewer finds the correct capability-scoping rule and stop condition. Bad: reporting p99 latency for reading markdown. Borderline: counting planning round-trips saved in one paired task while flagging the sample of one.

**Verification, evidence, and uncertainty.** Define the answer key first, run the with-and-without comparison, score next-action correctness and time-to-answer, and record the delta with its sample-size caveat. The seed's own pass condition, a reviewer identifies the correct next action without reading unrelated files, is already the right criterion and anchors the revised method. Effect sizes from single-reviewer comparisons are unstable, so early performance claims must carry explicit low-confidence labels until several runs accumulate.

**Second-order consequence.** Measuring a planning document with runtime metrics is a category error that crowds out the harder measurement of whether it changes decisions.

**Revision decision.** Recenter measurement on decision-quality comparison and move runtime bounds into the requirement contracts where they belong.

**Retained seed evidence.** The performance method line, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require memory, panic, and concurrency evidence; hot-path operations need p95 under 10 ms locally or an explicit benchmark exception.
Leading indicator to measure: the feature can be tested across frontend, Rust command, and packaged desktop behavior.
Failure signal to watch: the reference ignores permissions, IPC risk, or platform-specific verification.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what task, team, or product scale this reference stops being sufficient and what must supplement it beyond that line. The seed statement names multi-system spans, ownership boundaries, and SLO-bearing traffic as limits but gives no early indicators that a Tauri effort is approaching them before quality fails.

**Recommended default and causal basis.** Treat multiplying window labels and capability files, growing sidecar fleets, divergent platform-specific behavior, and store-distribution requirements as approach signals, and add dedicated security review and release engineering before crossing them. Scale failures in desktop work announce themselves through permission sprawl and platform drift well before the hard boundary, so leading indicators buy the response time that hard limits cannot.

**Operating conditions and assumptions.** The boundaries assume one application workspace, a mappable window-and-capability inventory, and planning slices small enough for single-reviewer comprehension. The statement bounds this planning reference and does not define scaling architecture for the application itself, which needs its own capacity and distribution design.

**Failure boundary and alternatives.** Limits are read as targets to approach, platform-specific divergence is discovered at release, or an auto-updater rollout proceeds because no one owned the escalation. Bounded alternatives and recoveries: shard planning by window or capability domain with one verification owner per shard, hand off through journals at checkpoint boundaries, or downgrade ambition to research-only work when limits are near but unquantified.

**Counterexample, gotchas, and operational comparison.** Boundaries interact, since a small app with many windows and plugins can exceed permission-review capacity sooner than a large single-window one, and drift accumulates across long release cycles that each look fine locally. Good: splitting a tray-plus-updater effort into sequenced slices with an interface freeze between them. Bad: letting one packet govern permissions for a dozen windows across three platforms. Borderline: continuing past a permission-sprawl warning with doubled review frequency.

**Verification, evidence, and uncertainty.** Track approach indicators per task record, review incidents for which boundary was actually crossed, and test one planned split to confirm the handoff preserved constraints. The four seed boundary classes match the failure surfaces this file's workload and failure sections independently identify, giving the statement internal corroboration. Exact thresholds where sufficiency ends are unmeasured and product-dependent, so the boundaries mark judgment lines rather than calibrated limits.

**Second-order consequence.** Scale limits protect a workflow only when paired with early-warning signals; a boundary detected at the boundary has already been crossed.

**Revision decision.** Add leading approach indicators and pre-crossing actions for each stated boundary.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Tauri Executable Playbook Templates stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would actually refresh this reference's external evidence when a scheduled or event-driven update runs. The seed query table pastes the corpus-internal theme name into three generic templates whose literal phrasing would return noise, since tauri executable playbook templates is this corpus's coinage rather than ecosystem vocabulary.

**Recommended default and causal basis.** Search in the ecosystem's own terms, Tauri 2 capabilities and permissions changes, Tauri IPC and command patterns, Tauri sidecar and updater guidance, and Rust desktop testing practice, anchored to versions and release notes. Refresh queries succeed by matching the vocabulary the ecosystem publishes under, and no external author writes about this corpus's internal theme label.

**Operating conditions and assumptions.** Each query names the section it refreshes, the source type it targets, and the trigger, scheduled or release-driven, that should fire it. The queries refresh external evidence for this theme and do not govern refreshing the local playbook, which changes through repository edits rather than searches.

**Failure boundary and alternatives.** Literal theme-name queries return nothing and the refresh is declared complete, results from a different Tauri major version overwrite still-valid guidance, or query hits are pasted in without evidence-boundary labels. Bounded alternatives and recoveries: subscribe to Tauri release notes instead of polling searches, pin queries to the official docs domain, or drive refresh from the dated retrieval records the research map should carry.

**Counterexample, gotchas, and operational comparison.** Search engines increasingly paraphrase queries so noise looks relevant, and a query that once worked can silently degrade as ecosystem terminology shifts. Good: a release-triggered query for Tauri capability schema changes feeding the permission guidance. Bad: searching the literal theme title and logging zero results as freshness. Borderline: using a community blog result with an inference label pending official confirmation.

**Verification, evidence, and uncertainty.** Run each query once, record whether its top results are on-topic for the section it refreshes, and rewrite any query whose results are dominated by noise. The seed's three-query structure, official docs, repository, and release notes, targets the right source classes and needs only ecosystem-vocabulary phrasing. Which phrasings will stay effective as Tauri's documentation evolves is unknowable in advance, so queries need their own review cadence.

**Second-order consequence.** Refresh queries are the file's future sensory organs; queries phrased in a private dialect leave the reference blind precisely where it promised to keep watch.

**Revision decision.** Rephrase queries in ecosystem vocabulary and bind each to the section and trigger it serves.

**Retained seed evidence.** All three labeled query rows with their official-docs, repository, and release-notes targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | tauri executable playbook templates official documentation best practices |
| `github_repository_query_phrase` | tauri executable playbook templates GitHub repository examples |
| `release_notes_query_phrase` | tauri executable playbook templates changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how statements in this reference must be labeled so a reader always knows whether a claim rests on local files, public sources, or synthesis. The seed notes define the three labels correctly but give no application rules, what to do when a statement mixes origins, how labels survive quoting, or which label governs the many unrefreshed external claims above.

**Recommended default and causal basis.** Label at the claim level rather than the section level, split mixed statements into separately labeled clauses, and downgrade any external claim without a dated retrieval record to inference until refreshed. Evidence boundaries exist to keep confidence calibrated downstream, and labels that live only in one closing section are shed the moment a sentence is quoted into a prompt or packet.

**Operating conditions and assumptions.** The three labels stay stable across the corpus so tooling and reviewers can parse them, and every synthesis clause names at least one of the sources it combines. The notes govern labeling within this reference and its reuses, and do not rank source quality, which the hierarchy and research map handle.

**Failure boundary and alternatives.** A section-level label is stretched over claims of mixed origin, unrefreshed external rows are cited as external fact, or the inference label becomes a dumping ground that stops distinguishing reasoned synthesis from guesswork. Bounded alternatives and recoveries: inline the labels as parenthetical tags on load-bearing claims, add a dated-retrieval requirement to the external label's definition, or generate a claim-to-label index during verification.

**Counterexample, gotchas, and operational comparison.** Labels rot fastest at reuse boundaries where text is copied without its scaffolding, and a correct label on a stale claim still misleads. Good: a capability recommendation labeled inference with its local basis and unrefreshed external status both named. Bad: quoting the thesis as external fact because the research map lists URLs. Borderline: carrying a label through a paraphrase with a note that wording changed.

**Verification, evidence, and uncertainty.** Sample ten load-bearing claims, check each carries or inherits the correct label, and confirm every external-fact label traces to a recorded retrieval. The three seed definitions match the label vocabulary used throughout this corpus and align with the boundary-preservation target in the reliability section. How well labels survive downstream reuse in prompts and packets is unobserved, so label durability remains an assumption until an audit follows real reuses.

**Second-order consequence.** Evidence labels are a chain of custody; the chain's strength is set at the weakest reuse, not at the section where the labels were first defined.

**Revision decision.** Add claim-level application rules, mixed-origin splitting, and retrieval-dated requirements for the external label.

**Retained seed evidence.** All three label definitions, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
