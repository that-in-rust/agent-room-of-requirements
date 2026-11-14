# Rust Backend Reference Routing

**Decision supported.** This section helps decide which routing discipline governs how an agent or engineer enters the Rust backend bundle. The seed theme name says routing but the seed never explains what is routed, the 83-line mapped map is a dispatcher that turns an incoming backend task into a work mode and an ordered list of which bundle files to read next.

**Recommended default and causal basis.** Consult the map before opening any other bundle file and follow the read order it emits for the classified mode or task type. The map exists because the bundle is too large to read whole per task, its opening line says to use it first to route the request before loading heavier backend references, making cheap routing the guard on expensive reading.

**Operating conditions and assumptions.** The incoming task is a Rust backend service task the bundle covers, non-service Rust work exits to the skills the parent guardrails name before routing begins. This reference covers dispatch into the rust-web-backend-delivery bundle, the content of the destination files is each destination's own subject.

**Failure boundary and alternatives.** Skipping the router and opening bundle files by filename intuition reproduces the misreads the map prevents, migration sequencing hunted in the playbook, session flows hunted in testing files. Bounded alternatives and recoveries: the parent SKILL.md's mode selection step, which performs the same classification one level up and hands its result to this map as step one of the context strategy.

**Counterexample, gotchas, and operational comparison.** The map routes reading, not implementation, a correct read order still leaves the design work to the destination files, treating the route as the answer skips the actual guidance. Good: a task classified to Operations Mode reading runtime-and-ops first per the mode table. Bad: reading all five files for a one-line cookie question. Borderline: a veteran skipping the map from memory, workable until the bundle revision moves a section.

**Verification, evidence, and uncertainty.** For a sample of recent tasks, compare the files actually opened against the map's prescribed order for their mode. Full read this session of the 83-line reference map and its five-file bundle. How much reading time the router saves in practice has never been measured for this bundle.

**Second-order consequence.** The map is deliberately the only file with no backend content at all, every one of its 83 lines is either a routing condition or a destination, which is what lets it stay cheap enough to consult on every task.

**Revision decision.** Frame this document as the corpus mirror of the bundle's dispatcher, its unit of value is a correct file-and-section read order, not backend advice of its own.

**Retained seed evidence.** The exact theme title and routing framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source may justify a routing claim versus a destination-content claim in this theme. The seed table's local row maps only reference-map.md, the router, while every destination the router points at, the playbook and three risk files, sits outside the mapped set even though routing claims are meaningless without their targets.

**Recommended default and causal basis.** Cite reference-map.md for routing conditions and read orders, named siblings for destination content, and external rows only as candidate pointers. A router's correctness is defined by its destinations, so this theme's evidence base necessarily spans the whole bundle, and destination facts used here must be cited to their own files by name rather than to the mapped router row.

**Operating conditions and assumptions.** The 202604 archive path stays stable so both the anchor row and the by-name destination citations resolve. The table certifies where this document's claims come from, it does not certify the four external URLs, which stayed unretrieved throughout this evolution.

**Failure boundary and alternatives.** Attributing a destination's content to the router row, for example quoting harness rules as if the map contained them, blurs the exact boundary this table exists to keep. Bounded alternatives and recoveries: a future mapping that lists router and destinations together, which would let routing claims and destination claims share one auditable table.

**Counterexample, gotchas, and operational comparison.** The external rows repeat the playbook theme's four URLs verbatim, none is routing-specific, so external corroboration for routing claims is even thinner than for content claims. Good: citing the map's mode table for who reads runtime-and-ops first. Bad: citing the map for what runtime-and-ops says about migrations. Borderline: citing SKILL.md's context strategy for read order, legitimate by name, absent from the mapped row.

**Verification, evidence, and uncertainty.** Audit citations by asking whether the claim is about where to read or what is read, and match the source accordingly. Full reads this session of the router and all four destination files. Whether the corpus template can express router-versus-destination roles in its fixed columns is untested.

**Second-order consequence.** Of the corpus's two rust-web-backend themes, the playbook theme anchors the content chapter and this theme anchors the dispatcher, together the two mapped rows cover the bundle's control plane and its largest data plane.

**Revision decision.** Hold the router as the anchor row and cite each destination file explicitly whenever its content, not its address, is used.

**Retained seed evidence.** The single local row and all four external rows with their column values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/reference-map.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://github.com/rust-lang/api-guidelines | external_research_source_material | external_research_sourced_fact | Rust library-team API design recommendations |
| https://github.com/tokio-rs/tokio | external_research_source_material | external_research_sourced_fact | async runtime implementation and operational model |
| https://github.com/tokio-rs/axum | external_research_source_material | external_research_sourced_fact | Rust web framework implementation and design claims |
| https://docs.rs/axum/latest/axum/ | external_research_source_material | external_research_sourced_fact | published crate documentation for routing and extractors |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which routing mechanism to reach for first when a backend task arrives. The seed scored rows rank document hygiene while the map's own implicit ranking is structural, mode classification outranks task-type lookup, which outranks the default read-everything order, because each tier costs more reading than the one before.

**Recommended default and causal basis.** Attempt mode classification first, drop to task-type lookup when the task names a concrete slice, and reserve the full sequence for genuinely unclassifiable work. The map presents its three mechanisms in exactly that order, section one the mode table, section two the task-type orders, section three the full-sequence default, an escalation ladder from cheapest dispatch to costliest fallback.

**Operating conditions and assumptions.** The reader can honestly distinguish unfamiliar-large from unclassified-small, self-serving escalation erodes the ladder from below. This ranking orders routing mechanisms, ranking the destination files' content doctrines belongs to the playbook theme's scoreboard.

**Failure boundary and alternatives.** Inverting the ladder, defaulting to read-everything, burns the context budget the router exists to protect and buries the risk file the task actually needed. Bounded alternatives and recoveries: the parent skill's default mode combinations, which pre-bundle two modes per common task shape and skip per-task classification entirely.

**Counterexample, gotchas, and operational comparison.** Modes and task types overlap deliberately, an auth task matches Security Mode and the auth task-type row, when both match the task-type row wins because it carries section-level precision the mode row lacks. Good: a password-reset task routed by the auth task-type row straight to three named security sections. Bad: reading the full sequence for a typo-level handler fix. Borderline: mode-only routing for a task that had a task-type row, correct destination, missed section precision.

**Verification, evidence, and uncertainty.** Review recent routing choices against the ladder and count how often the fallback tier was invoked and why. The map's three-section structure and its own use-this-first framing read in full. The real cost gap between tiers depends on reader speed and context limits, unmeasured here.

**Second-order consequence.** The ladder's fallback tier is self-limiting, the map grants the full-sequence order only to large unfamiliar tasks, implying that habitual fallback use signals a classification skill gap rather than task size.

**Revision decision.** Present the three-tier escalation ladder as the operative ranking and retain the scored rows as corpus-process emphasis.

**Retained seed evidence.** The three scored seed rows with tier labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `rust_backend_reference_routing` | 95 | default_adoption_pattern_tier | Source Map First: Load local rust backend material before synthesizing reference routing recommendations. |
| `rust_backend_reference_routing` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `rust_backend_reference_routing` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what principle orders which bundle files a given task reads and in what sequence. The seed generic load-local-first statements miss the routing thesis, correct backend work starts by classifying the task's dominant risk, then reading only the files that own that risk, in the order the map prescribes.

**Recommended default and causal basis.** Name the task's dominant risk aloud before opening any file and let that name pick the mode row. The mode table is built on risk ownership, each mode row names a main-risk condition, ambiguity, delivery sequencing, operational safety, security, resilience, or review readiness, and maps it to the files that own that risk class.

**Operating conditions and assumptions.** Tasks have one dominant risk, genuinely dual-risk work uses the parent skill's default mode combinations rather than forcing one row. The thesis governs how reading is ordered, what the destination files then demand of the code is their own doctrine.

**Failure boundary and alternatives.** Risk-blind routing reads by topic keyword instead, a retries question matches resilience risk and belongs in security-and-resilience, but keyword routing sends it to the playbook because retry appears in the client-boundary section. Bounded alternatives and recoveries: spec-first entry through the parent skill when the task is too vague to carry any risk classification yet.

**Counterexample, gotchas, and operational comparison.** The dominant risk is often not the stated topic, a migration task's stated topic is schema but its dominant risk is rollout ordering, which is why the map routes it to runtime-and-ops rather than the persistence playbook section. Good: an email-integration task naming resilience as dominant risk and reading the idempotency sections before the client-boundary section. Bad: routing by whichever file title shares a word with the ticket. Borderline: treating a review as delivery because the reviewer will also fix issues, defensible, the map's review row still reads risk-first.

**Verification, evidence, and uncertainty.** Check that each routing decision recorded the risk name it classified and that the files read match that risk's row. The mode table's main-risk column and the review-order inversion read in full. Whether risk classification stays reliable for engineers new to the bundle is untested.

**Second-order consequence.** The review-mode row inverts every other row's logic, builders read shape first and risk second, reviewers read risk files first and the playbook last, the map encodes that attention should start where production failures start.

**Revision decision.** State the thesis as classify risk, route by ownership, read in prescribed order, each clause anchored to one map section.

**Retained seed evidence.** The three labeled thesis statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `rust_backend_reference_routing` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Rust Backend Reference Routing comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide how to physically use the mapped router file when a task arrives. The seed map row lists heading signals but not the router's internal anatomy, section one dispatches by work mode, section two by task type with section-level precision, section three gives the fallback sequence, and section four supplies ripgrep commands for heading search.

**Recommended default and causal basis.** Enter the router at section one for approach questions, section two for named slices, and use section four's search commands inside any destination over a screen long. The four sections serve different callers, mode dispatch serves planners choosing an approach, task-type dispatch serves implementers with a named slice, the fallback serves newcomers, and heading search serves anyone landing in a large destination file.

**Operating conditions and assumptions.** Destination heading names stay synchronized with the router's inline section references. This map describes the router file itself, the five-file bundle it routes into is described by the playbook theme's corresponding section.

**Failure boundary and alternatives.** Reading the router linearly as prose wastes its structure, it is a lookup artifact, the correct use is to jump to the section matching what you already know about the task. Bounded alternatives and recoveries: grepping destination files directly with your own patterns, workable for experts, it forfeits the router's curated section shortlists.

**Counterexample, gotchas, and operational comparison.** The ripgrep commands are written references-relative, they resolve only from the skill root directory, run from elsewhere they return nothing and mimic missing content. Good: jumping to the database-change row and reading exactly the two named ops sections. Bad: reading the router top to bottom then the whole bundle anyway. Borderline: memorized routing that skips the file, fine until a bundle revision, the inline section names are the part memory gets wrong first.

**Verification, evidence, and uncertainty.** Spot-check the router's inline section names against the destination files' actual headings. The router's four-section structure and inline destination references read in full. Whether the corpus should track router-destination heading coupling automatically is an open tooling question.

**Second-order consequence.** The router embeds destination section titles inline, the auth row names three exact security-file sections, so its precision degrades silently if a destination renames a heading, a coupling no checksum on the router alone can catch.

**Revision decision.** Annotate the row with the four-section anatomy so readers enter the router at the right lookup table.

**Retained seed evidence.** The single local source row with title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/reference-map.md | Reference Map | Reference Map; 1) Choose the Work Mode; 2) Choose by Task Type; New Endpoint or Feature; Auth, Sessions, or Password Flows; Database Change, Migration, or Rollout | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide what role, if any, external links play in validating this theme's claims. The seed four rows are ecosystem anchors inherited from the theme template, yet routing is the one concern they least support, no external URL documents how this private bundle dispatches its own files.

**Recommended default and causal basis.** Use the rows only when a destination's crate example needs a freshness check, and route that check through the destination's own theme where one exists. Routing doctrine is intrinsically local, the map's conditions and read orders reference files that exist only in this archive, so external evidence can corroborate destination content but never the routing itself.

**Operating conditions and assumptions.** The docs.rs latest URL floats by design, any eventual fetch must pin the version it saw. External rows here serve the destinations' freshness, the router's correctness is checked against the bundle, not the ecosystem.

**Failure boundary and alternatives.** Seeking external validation for read orders misunderstands the artifact, an axum documentation page can confirm extractor facts, it cannot confirm that auth tasks should read security-and-resilience first. Bounded alternatives and recoveries: watching the upstream skill archive for revised bundles, the only genuinely external signal that could change routing guidance.

**Counterexample, gotchas, and operational comparison.** The rows' presence can mislead audits into expecting external corroboration for this theme, an auditor should expect none and treat its absence as correct, not as a gap. Good: flagging a tokio row fetch as serving the playbook theme's runtime examples. Bad: citing the axum repository to justify a read order. Borderline: using api-guidelines to sanity-check a destination's naming advice, on-topic for Rust, outside this theme's routing charter.

**Verification, evidence, and uncertainty.** Confirm no routing claim in this document cites an external row as support. Zero external retrievals this assignment, and the router's purely local reference targets. Whether future bundle revisions will publish routing rationale externally is unknowable.

**Second-order consequence.** This makes the theme's external boundary unusually clean, every externally-flavored statement in this document is really a destination-content statement, so the unretrieved-candidate label applies wholesale with no per-claim ambiguity.

**Revision decision.** Keep the rows as destination-freshness candidates and state plainly that routing claims have no external corroboration surface.

**Retained seed evidence.** All four external rows with their boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://github.com/rust-lang/api-guidelines | Rust API Guidelines | Rust library-team API design recommendations | external_research_sourced_fact |
| https://github.com/tokio-rs/tokio | Tokio repository | async runtime implementation and operational model | external_research_sourced_fact |
| https://github.com/tokio-rs/axum | Axum repository | Rust web framework implementation and design claims | external_research_sourced_fact |
| https://docs.rs/axum/latest/axum/ | Axum docs.rs | published crate documentation for routing and extractors | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which dispatch behaviors this theme must treat as defects when reviewing how work was routed. The seed process rows omit routing's own failure catalog, keyword routing that matches titles instead of risks, fallback abuse that reads everything every time, stale-memory routing that skips the map, and route-as-answer where dispatch substitutes for design.

**Recommended default and causal basis.** Review routing decisions for a named risk, a proportionate tier, a current map consult, and evidence that destination sections were actually read. Each failure defeats a specific router mechanism, keyword routing bypasses the main-risk column, fallback abuse collapses the escalation ladder, stale memory decouples from bundle revisions, and route-as-answer stops at section two without reading the destinations.

**Operating conditions and assumptions.** Routing decisions leave a trace, teams that route silently in their heads give the registry nothing to inspect. This registry names failures of dispatch, failures inside the destination content belong to the playbook theme's registry.

**Failure boundary and alternatives.** Routing failures are quieter than content failures, the reader still reads something plausible, the cost appears later as unread risk sections whose rules were violated in code. Bounded alternatives and recoveries: automating a route log line per task, cheap to emit, it converts three of the four failures from invisible to greppable.

**Counterexample, gotchas, and operational comparison.** Stale-memory routing worsens with expertise, the engineers most fluent in the bundle are the least likely to reopen the map after a revision moves a section. Good: rejecting a review that read only the playbook for an auth diff. Bad: accepting we read the relevant files as a routing record. Borderline: an expert's from-memory route that matches the current map exactly, correct outcome, unauditable process.

**Verification, evidence, and uncertainty.** Sample recent tasks and reconstruct their routes, checking each against the four rejection signatures. The router's mechanisms read in full and their inversion into failure modes. Base rates for each routing failure are unmeasured in this repository.

**Second-order consequence.** Route-as-answer is the inverted twin of the seed's context-free-summary row, one skips the sources entirely, the other touches the router and mistakes touching for reading, both produce confident guidance with no destination evidence underneath.

**Revision decision.** Add the four routing rejections with their detection signals, each tied to the mechanism it defeats.

**Retained seed evidence.** The three seed process rows with their detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide what checks must pass before routing guidance and routing practice are trusted. The seed document verifier checks this file's shape but nothing gates routing quality, whether tasks were classified, whether the files read matched the prescribed order, and whether the router's inline section names still exist in the destinations.

**Recommended default and causal basis.** Require the route declaration on backend PRs and run the heading-consistency script whenever the archive bundle changes. Routing is a process property, so its gates are audits over traces, a route log entry per task, a periodic heading-consistency check between router and destinations, and a review question asking which mode row governed this work.

**Operating conditions and assumptions.** The bundle remains at its archived path so the consistency script has stable targets. These gates verify routing practice and router-destination consistency, destination content gates live with the playbook theme's command set.

**Failure boundary and alternatives.** Gating only the document lets the practice decay invisibly, this file can pass every verifier run while every actual task routes by keyword and memory. Bounded alternatives and recoveries: manual quarterly spot-checks instead of scripting, cheaper to start, they decay exactly the way unscripted audits always decay.

**Counterexample, gotchas, and operational comparison.** The seed's verifier path points at the 202606 generation tooling, the corpus's live verifier for this file is the tests directory script used at every assignment, both exist and check different things. Good: a PR template field naming the mode row and files read. Bad: certifying routing health because this document's verifier passed. Borderline: trusting the declaration without sampling actual reading, better than nothing, still gameable.

**Verification, evidence, and uncertainty.** Run the document verifier for this file and confirm the two practice gates exist and produce records. The router's plain-text section references and the corpus verifier behavior observed this session. Whether teams will sustain route declarations without automation is unproven.

**Second-order consequence.** The heading-consistency check is mechanical, the router names destination sections in plain text, a short script can extract each reference and grep the destination, turning the router's silent coupling into a failing check.

**Revision decision.** Add the practice gates, per-task route declaration in review, and a scripted check that each router-referenced heading resolves in its destination file.

**Retained seed evidence.** The seed's document verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide what dispatch procedure an agent must follow before consuming any Rust backend bundle content. The seed four bullets tell an agent to start with the source map but not how to route, the operative procedure is the map's own, classify mode or task type, emit the file list in prescribed order, read only that list, then act.

**Recommended default and causal basis.** Require agents to cite the matched map row before any bundle file is opened and reject outputs whose cited row does not cover the files read. Agents suffer routing failures worse than humans, an agent that loads the full bundle spends context on files its task never needed, and one that keyword-routes confidently misreads never notices, so mechanical adherence to the map is the cheapest reliability lever available.

**Operating conditions and assumptions.** The agent can see the router file, embedding a stale copy in the prompt recreates stale-memory routing in automated form. This guide scripts agent dispatch into the bundle, what the agent does inside each destination follows that destination's own guidance.

**Failure boundary and alternatives.** An agent prompt that says use the rust backend bundle without the routing step produces exactly the fallback-abuse and keyword-routing defects the registry names, at machine speed. Bounded alternatives and recoveries: pre-routing by a human who hands the agent a fixed file list, safer for high-stakes work, it moves the classification burden without removing it.

**Counterexample, gotchas, and operational comparison.** Task-type rows sometimes name destination sections, an agent must read those named sections, not just the named file, or the row's precision is silently discarded. Good: an agent log citing the external-API task-type row and reading its three entries in order. Bad: an agent ingesting all five files for a cookie-flag question. Borderline: an agent citing a mode row when a sharper task-type row existed, right files, lost section precision.

**Verification, evidence, and uncertainty.** Audit agent logs for the cited row, the ordered list, and the match between list and files actually read. The map's condition-to-file-list tables and the parent skill's classify-first workflow read in full. How often agents misclassify mode on ambiguous tasks lacks measurement.

**Second-order consequence.** The map's structure is machine-friendly by accident, its tables map conditions to file lists, so an agent can be required to quote the exact row it matched, making every routing decision verifiable from the log alone.

**Revision decision.** Give agents the literal three-step routine, classify, emit ordered file list with the governing map row cited, read and act, logging all three steps.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide whether to spend the first minute of a backend task on explicit routing. The seed generic engineer scenario misses the journey this theme actually owns, a person or agent holding a fresh backend task and deciding, in under a minute, which of five files to read and in what order.

**Recommended default and causal basis.** Run the routing journey at every task start, including tasks that feel familiar, and let the emitted plan discipline the reading. The journey is short by design, read the map's matching row, note the file list, go, its entire value is compressing the expensive what-should-I-read deliberation into a table lookup.

**Operating conditions and assumptions.** The reader accepts the minute of routing overhead, under deadline pressure the journey is the first discipline dropped and the failure data shows up weeks later. The journey runs from task receipt to reading plan, the destination journeys, designing, testing, hardening, are the destination themes' scenarios.

**Failure boundary and alternatives.** The journey fails at its first step when the task resists classification, and the map's own answer is the fallback sequence, so the failure path is also a routed path rather than an improvisation. Bounded alternatives and recoveries: standing reading plans per team specialty, amortizing classification across similar tasks, at the cost of drifting from the map as the bundle revises.

**Counterexample, gotchas, and operational comparison.** Mid-task re-routing is part of the journey, a delivery task that uncovers an auth wrinkle re-enters the map at the auth row, treating the initial route as fixed for the task's life misses this. Good: a worker-queue task re-routed mid-flight to the background-processing row when durability questions surfaced. Bad: skipping routing because the task looked like last week's. Borderline: routing once for a batch of similar endpoints, acceptable when the batch truly shares one risk profile.

**Verification, evidence, and uncertainty.** Ask task owners to show the row they matched and the plan it emitted for their most recent piece of work. The map's use-this-first charter and its three lookup mechanisms read in full. The true median routing time for practiced users is estimated, not timed.

**Second-order consequence.** The journey repeats per task, not per project, which is why the router optimizes for lookup speed over completeness, a dispatcher consulted twenty times a week must cost seconds, and the map's terseness is that requirement made visible.

**Revision decision.** Recast the scenario as the sixty-second routing journey with its three exits, mode row, task-type row, or fallback sequence.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Rust reliability engineer is starting from a requirement that needs a safe API, explicit error model, and testable boundary and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `rust_backend_reference_routing` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the idiomatic ownership, async, error, and crate-boundary shape before coding.
Reference opening trigger: Open this file when the task mentions rust backend reference routing, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how strictly to follow the router's prescriptions when experience suggests shortcuts. The seed adopt-adapt-avoid rows never touch routing's live tradeoffs, lookup precision versus lookup cost, prescribed order versus reader judgment, and per-task routing versus standing habits.

**Recommended default and causal basis.** Follow the prescribed orders literally, route per task, and treat any standing habit as a cache that expires on every bundle revision. The router itself takes positions on all three, it buys precision with a three-tier ladder so most lookups stay cheap, it prescribes order because risk files read after code is written arrive too late, and it assumes per-task routing because bundle revisions invalidate habits silently.

**Operating conditions and assumptions.** Deviations are recorded with reasons, an undocumented deviation is indistinguishable from a routing failure in later audits. This guide weighs routing postures, weighing destination content choices like inline-versus-worker belongs to the playbook theme.

**Failure boundary and alternatives.** Resolving the tradeoffs against the router's positions has a common signature, experienced readers substitute judgment for prescription, and their outcomes stay fine until the first task whose risk profile their judgment mis-files. Bounded alternatives and recoveries: team-level routing conventions layered over the map, tolerable when they only add reading, corrosive when they subtract prescribed files.

**Counterexample, gotchas, and operational comparison.** The cost of routing wrong is asymmetric by direction, over-reading wastes minutes, under-reading ships unexamined risk, so when uncertain the ladder should be climbed toward more reading, not less. Good: a reviewer following the risk-first order despite knowing the codebase well. Bad: a standing habit of skipping testing-and-fixtures because the team has a harness already. Borderline: reordering two files within one route for personal flow, harmless when both still get read.

**Verification, evidence, and uncertainty.** Compare recorded deviations against later defect attributions to test whether the shortcuts were actually safe. The map's ordered rows and the review-order rationale read in full. How quickly standing habits drift from a revised map has no local measurement.

**Second-order consequence.** Prescribed order matters most for review tasks, the map's review row front-loads risk files precisely because a reviewer who reads the playbook first anchors on shape and under-weights the security findings that should have framed everything.

**Revision decision.** Add the three tradeoff axes with the router's stances and the conditions under which deviation is defensible.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the rust backend reference routing pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong rust backend reference routing guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which file's word wins for each class of question this theme fields. The seed hierarchy crowns the router canonical with a thin-evidence warning, but a router is canonical only about routing, every content question outranks it toward the destination that owns the risk.

**Recommended default and causal basis.** Resolve dispatch disputes in the map, content disputes in the owning destination, and applicability disputes in SKILL.md's description and guardrails. Authority here is functional, the router holds final word on which file to read and in what order, each destination holds final word on its own subject, and SKILL.md holds final word on when the bundle applies at all.

**Operating conditions and assumptions.** The bundle's files stay mutually consistent, when the router and a destination disagree about a section name, the destination is right and the router is stale. This hierarchy orders authority within the bundle for this theme's questions, corpus-wide precedence across rust themes is the adjacent routing section's concern.

**Failure boundary and alternatives.** Over-extending the router's canon lets a routing table settle content disputes it never addressed, the map naming a security section says nothing about what that section requires. Bounded alternatives and recoveries: flattening the hierarchy by reading everything and trusting no precedence, the fallback sequence institutionalizes this for the unclassifiable case only.

**Counterexample, gotchas, and operational comparison.** The seed's confidence warning reads as weakness but is accurate strength, one mapped source is exactly right for a theme whose subject is that one file's dispatch tables. Good: settling a which-file-first dispute by quoting the mode table. Bad: quoting the mode table to settle what counts as a valid session flow. Borderline: using the router's section names as a destination's table of contents, convenient, stale the moment the destination revises.

**Verification, evidence, and uncertainty.** Test disputed claims by class, dispatch, content, or applicability, and check the matching authority answered. Each bundle file's self-declared use statement and the context strategy's ordering read in full. No recorded case yet tests router-destination staleness in this archive.

**Second-order consequence.** The router is also the bundle's most fragile authority, it hard-codes destination section names, so a destination revision can make the canonical dispatcher wrong about its own subject, a failure direction the destinations themselves cannot suffer.

**Revision decision.** State the functional split, router canonical for dispatch, destinations canonical for content, parent skill canonical for applicability.

**Retained seed evidence.** The single hierarchy row and the confidence warning remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-web-backend-delivery-01/references/reference-map.md | canonical primary source | Reference Map; 1) Choose the Work Mode; 2) Choose by Task Type | What guidance, warning, or example should this source contribute to Rust Backend Reference Routing? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what standing object translates a team's task language into this bundle's routing rows. The seed named artifact, canonical routing rules for stale, duplicate, and conflicting sources, has no concrete form in the seed, its natural shape is a per-team routing card, one page mapping local task vocabulary onto the map's rows.

**Recommended default and causal basis.** Build the card from the last quarter's actual tickets, mapping each to its governing map row, and keep it to one page. Teams phrase tasks in product words, fix checkout emails, while the map speaks in risk words, external integration with resilience concerns, the routing card is the translation layer that makes the map's rows reachable from the words tickets actually use.

**Operating conditions and assumptions.** The team's ticket vocabulary is stable enough to enumerate, rapidly shifting products need the card rebuilt more often than it pays. The card translates into the map, it must never bypass it, a card row points at a map row, not directly at files.

**Failure boundary and alternatives.** Without the translation layer each engineer improvises the product-to-risk mapping, and improvised mappings are where keyword routing re-enters through the back door. Bounded alternatives and recoveries: training everyone to classify risks fluently instead, more durable per person, it leaves nothing behind when people rotate.

**Counterexample, gotchas, and operational comparison.** The card tempts direct file pointers because they save one hop, that hop is the entire safety property, a card with file pointers is a fork of the map that will silently diverge. Good: a card entry mapping payment webhook changes to the external-API task-type row. Bad: a card entry listing three files with no map row cited. Borderline: a card entry for a task class the map lacks, acceptable when marked as needing the fallback sequence.

**Verification, evidence, and uncertainty.** Sample card entries and confirm each cites a live map row whose conditions genuinely cover the ticket phrase. The map's row structure and the vocabulary gap between its risk terms and ordinary ticket language. The ticket-class coverage a one-page card can reach is team-specific.

**Second-order consequence.** Pointing card rows at map rows rather than files makes the card revision-proof, when a bundle update changes a row's file list, every card entry inherits the fix without editing, the indirection is the maintenance strategy.

**Revision decision.** Define the artifact as the routing card, ticket-vocabulary phrases on the left, matched map rows on the right, reviewed whenever the map or the product vocabulary shifts.

**Retained seed evidence.** The artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: canonical source routing rules for stale, duplicate, and conflicting sources.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Rust Backend Reference Routing | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which exercise teaches correct bundle dispatch fastest. The seed abstract usage lines never walk a real dispatch, the teaching example this theme needs is one task routed all three ways, by mode, by task type, and by fallback, with the differing read lists compared.

**Recommended default and causal basis.** Run new team members through the three-way walkthrough on a real recent ticket before they route unsupervised. Seeing the same task produce a two-file mode route and a three-section task-type route teaches the ladder's precision gradient faster than any rule statement, the comparison is the lesson.

**Operating conditions and assumptions.** The chosen ticket genuinely matches a task-type row, tickets that only mode-match teach a two-way comparison instead. Worked examples here teach dispatch, examples of what to build once routed belong to the destination themes.

**Failure boundary and alternatives.** Training on routing rules without a walked dispatch leaves learners able to recite the ladder yet still keyword-route under pressure, the reflex is built by doing the lookup, not by knowing it exists. Bounded alternatives and recoveries: shadowing an experienced router on live tasks, richer signal, unrepeatable and unstandardized.

**Counterexample, gotchas, and operational comparison.** Learners anchor on the first route they compute, run the fallback last in training or its exhaustive list becomes the anchor and the ladder's economy lesson is lost. Good: a trainee producing three read lists for one ticket and explaining the precision gradient. Bad: memorizing the six mode names without ever opening the map's tables. Borderline: practicing only on clean single-risk tickets, real tickets are messier, the drill still builds the lookup habit.

**Verification, evidence, and uncertainty.** Have the trainee route a fresh ticket unsupervised and compare their list against the map's prescription. The map's three mechanisms and the auth row's section-level precision read in full. Retention of the routing habit past training has no local measurement.

**Second-order consequence.** The walkthrough exposes the task-type tier's hidden advantage, its auth row names three exact sections inside the security file, so the task-type route is not just shorter than the fallback, it is deeper than the mode route, precision and economy travel together.

**Revision decision.** Anchor the section on one concrete walkthrough, a session-cookie hardening task, routed via Security Mode, via the auth task-type row, and via the fallback, with read lists side by side.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Rust Backend Reference Routing after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Rust Backend Reference Routing as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Rust Backend Reference Routing only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which measurements reveal whether routing discipline is real and whether the map itself needs revision. The seed compile-centric indicator misses routing's own signals, share of tasks with a declared route, match rate between declared routes and the map's prescription, and downstream defects attributable to unread prescribed files.

**Recommended default and causal basis.** Collect route declarations at review time and attribute each backend defect to read, unread, or unroutable guidance during retrospectives. Routing quality is upstream of content quality, a task that skipped its prescribed security sections produces defects that look like content failures, only route records let the attribution reach back to the dispatch step where the failure actually began.

**Operating conditions and assumptions.** Reviews capture the declaration cheaply, a one-line template field, heavyweight capture kills the declaration rate the metric depends on. This loop measures dispatch practice, destination-content adoption metrics belong to the playbook theme's loop.

**Failure boundary and alternatives.** Measuring only downstream outcomes hides the router entirely, teams conclude the bundle's guidance failed when the guidance was simply never read for that task. Bounded alternatives and recoveries: instrumenting file-open telemetry on the archive, objective but invasive, declaration plus sampling reaches most of the signal at none of the surveillance cost.

**Counterexample, gotchas, and operational comparison.** A high match rate with a low declaration rate is the classic false comfort, the routers who declare are the ones already routing well, the silent majority is where the failures live. Good: a retro attributing a session bug to an unread prescribed section and fixing the routing habit, not just the bug. Bad: celebrating low defect counts while nobody declares routes. Borderline: counting declarations without sampling their honesty, workable early, gameable at scale.

**Verification, evidence, and uncertainty.** Check the quarterly review consumed all three metrics and produced at least one map or practice adjustment decision. The routing-upstream-of-content structure read from the map's charter and the bundle's division of labor. Expected healthy values for match rate have no baseline yet.

**Second-order consequence.** Prescription-match rate doubles as a map quality signal, a row that healthy tasks routinely deviate from is evidence the row's conditions are mis-drawn, so the metric feeds map revision, not just reader discipline.

**Revision decision.** Add the three routing metrics, declaration rate, prescription-match rate, and unread-file defect attribution, reviewed on the same quarterly cadence.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: compile attempts and review comments decrease because the API shape is explicit before implementation.
Failure signal: the reference hides ownership or error tradeoffs behind generic guidance.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what must be verified before this routing reference is declared faithful to its source. The seed shape items never audit this document against the router it mirrors, no item counts the six modes, six task-type orders, the four-section anatomy, or checks that quoted read orders match the live map.

**Recommended default and causal basis.** Run the count-and-diff audit at every reread cycle and after any archive change touching the bundle. This theme's fidelity is table-transcription fidelity, the map is 83 lines of enumerable rows, so completeness is checkable by counting rows and diffing quoted orders against the file, minutes of work with total coverage.

**Operating conditions and assumptions.** The archive path stays stable so the diff has a live target. This checklist audits this reference document, auditing live routing practice belongs to the metrics loop, and auditing the router's own health belongs to the verification gates.

**Failure boundary and alternatives.** The subtle staleness path is indirect, this document quotes destination section names via the router, so a destination revision can invalidate quotes here even while the router file itself is unchanged. Bounded alternatives and recoveries: hashing the router and re-auditing only on hash change, efficient, blind to destination revisions that stale the router's inline references.

**Counterexample, gotchas, and operational comparison.** Auditing counts without diffing quoted orders passes a document whose numbers are right and whose sequences are stale, the order is the payload, the counts are just its skeleton. Good: an audit catching that a quoted read order dropped the testing file. Bad: declaring completeness because 26 headings exist. Borderline: accepting paraphrased row conditions, tolerable when the file list and order are quoted exactly.

**Verification, evidence, and uncertainty.** Count the enumerables and diff every quoted read order against the current reference-map.md. The fully enumerable structure of the 83-line router read in full. Whether destination-revision staleness deserves its own automated check is an open question.

**Second-order consequence.** Because this theme quotes structure rather than prose, its audit is the cheapest in the rust cluster, every claim is either a count or a quoted list, there is almost no judgment surface for drift to hide in.

**Revision decision.** Add count items, six modes, six task types, three-tier ladder, four router sections, plus a quoted-order diff against the live map each audit.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Rust Backend Reference Routing.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send questions that arrive at this theme but are not dispatch questions. The seed token-split rows are self-referential, while this theme's real adjacency is precise, the playbook theme holds the bundle's content anchor, other rust themes hold specs and quality gates, and non-service Rust work exits the bundle entirely per the parent guardrails.

**Recommended default and causal basis.** Classify incoming questions as dispatch-shaped or content-shaped and forward content immediately rather than paraphrasing destination guidance here. This theme and the playbook theme partition one bundle, dispatch here, content there, so the commonest adjacency question, where is the actual backend guidance, has a single answer, the playbook theme and its siblings.

**Operating conditions and assumptions.** The named adjacent themes exist in the corpus and the archive skills remain at their referenced paths. This section sends away what this theme cannot answer, the destinations' contents are summarized nowhere here by design.

**Failure boundary and alternatives.** The recursive trap is real for a routing theme, questions about routing keep landing here even when they are content questions wearing routing vocabulary, which file covers retries is a routing question, what the retry policy should be is not. Bounded alternatives and recoveries: for questions no local theme covers, external documentation explicitly labeled unretrieved, never presented as verified.

**Counterexample, gotchas, and operational comparison.** Paraphrasing destination content here for convenience creates a shadow copy that staleness will eventually split from the destination, forwarding beats summarizing every time. Good: forwarding what should the idempotency key be to the playbook theme's cluster. Bad: answering it here from memory of the security file. Borderline: answering which section covers idempotency keys, legitimately this theme's job, the boundary runs exactly there.

**Verification, evidence, and uncertainty.** Sample recent uses of this document and check no destination content was answered inline. The guardrails' exit list and the two-theme partition of the bundle read in full. How often content questions arrive dressed as routing questions is unmeasured.

**Second-order consequence.** A routing theme's adjacency section is its own subject applied to itself, the test of this document is whether this very section routes better than the token-split rows it evolves, recursion made useful instead of circular.

**Revision decision.** Route content questions to the playbook theme, non-service Rust to the guardrail-named skills, and keep only dispatch mechanics, routing failure modes, and routing practice here.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use backend, executable, or quality-gate Rust references when the question shifts to HTTP delivery, specs, or review gates.
Adjacent reference 1: consider the rust adjacent reference when the current task pivots away from rust backend reference routing.
Adjacent reference 2: consider the backend adjacent reference when the current task pivots away from rust backend reference routing.
Adjacent reference 3: consider the reference adjacent reference when the current task pivots away from rust backend reference routing.

## Workload Model

**Decision supported.** This section helps decide how much time and maintenance dispatch discipline may consume before it stops paying. The seed endpoint-count budget models destination work, not dispatch, routing's own workload unit is the classification event, seconds per task, plus the rarer card and map maintenance events measured in minutes per quarter.

**Recommended default and causal basis.** Budget routing at under a minute per task, and treat any task exceeding that as a decomposition candidate before forcing a route. Dispatch cost is deliberately front-loaded and tiny, the router's design pushes all heavy cost into the destinations it selects, so this theme's capacity question is not how much routing a team can afford but whether the near-zero cost stays near zero as task volume grows.

**Operating conditions and assumptions.** Tasks arrive at slice granularity, portfolio-level initiatives route per constituent slice, not once at the top. This model budgets dispatch effort, the selected destinations' implementation effort is budgeted by the playbook theme's slice model.

**Failure boundary and alternatives.** The model breaks when classification stops being cheap, ambiguous multi-risk tasks that take real deliberation to route signal either a task that should be split or a map row whose conditions have drifted from the work the team actually gets. Bounded alternatives and recoveries: the routing card amortizing classification for recurring ticket shapes, legitimate as long as card rows still resolve through live map rows.

**Counterexample, gotchas, and operational comparison.** Batching routing across many tickets to save seconds recreates standing-habit drift, the per-task cost being trivial is exactly why it should be paid per task. Good: a compound migration-plus-worker ticket split into two cleanly routed slices. Bad: an hour spent debating one ticket's mode instead of splitting it. Borderline: routing a twenty-ticket cleanup batch once, acceptable when every ticket is genuinely the same shape.

**Verification, evidence, and uncertainty.** Watch for routing decisions that exceeded the minute budget and check each triggered a split or a map-row review. The router's lookup-speed design and the map's slice-shaped task-type rows read in full. The task volume at which even seconds-scale routing needs tooling is beyond current data.

**Second-order consequence.** Expensive routing is diagnostic, when a task resists the minute-scale lookup the resistance itself is information, the task is compound and should be split into slices that each route cleanly, dispatch difficulty predicting decomposition need.

**Revision decision.** Restate the workload as classification events at seconds each, card maintenance at one page per quarter, and map-consistency checks per bundle revision.

**Retained seed evidence.** The workload dimension rows with boundary values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Rust Backend Reference Routing as a backend service operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | service implementation, route review, worker execution, and operational hardening work where a single wrong recommendation can affect live request handling | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one service boundary, up to 25 endpoints or workers, 1000 representative requests, and one deploy rollback path per review batch | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Reference Map; 1) Choose the Work Mode; 2) Choose by Task Type; New Endpoint or Feature; Auth, Sessions, or Password Flows; Database Change, Migration | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is canonical source routing rules for stale, duplicate, and conflicting sources | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what dispatch reliability the team commits to before trusting that prescribed guidance reaches the work. The seed document-property targets omit dispatch reliability, the rates at which tasks get routed at all, routed to the prescribed files, and re-routed when their risk profile shifts mid-flight.

**Recommended default and causal basis.** Audit the three chain links quarterly from review records and attribute each miss to its tier, classification, prescription, or re-routing. Each target guards one link in the dispatch chain, declaration guards existence, prescription-match guards correctness, and mid-flight re-routing guards currency, a chain whose weakest link determines whether prescribed risk sections are actually read before code ships.

**Operating conditions and assumptions.** Route declarations exist to audit, the metrics loop's declaration rate is this target's precondition. These targets cover dispatch practice, the destination files' own correctness targets live with their themes.

**Failure boundary and alternatives.** Targets set only on destination outcomes let dispatch decay invisibly, by the time defect rates move, the routing discipline has usually been gone for months. Bounded alternatives and recoveries: outcome-only targets accepting slower detection in exchange for zero process overhead, defensible for tiny teams, expensive at scale.

**Counterexample, gotchas, and operational comparison.** Perfect match rates can indicate rubber-stamping rather than health, an auditor should expect occasional documented deviations, their total absence means deviations are happening without documentation. Good: a quarterly audit tracing two misses to the classification tier and sharpening the card. Bad: inferring dispatch health from a quiet defect quarter. Borderline: waiving the re-route target for one-day tasks, defensible, risk shifts rarely fit inside a day.

**Verification, evidence, and uncertainty.** Review the three link audits together and confirm each miss carries a tier attribution. The seed's own sampling row and the map's tiered mechanisms read in full. Sustainable match-rate baselines await the first audit cycles.

**Second-order consequence.** The seed's decision-accuracy row, eighteen of twenty sampled uses routing correctly, is already a dispatch target in disguise, the evolution here is attaching it to the map's specific mechanisms so a miss identifies which tier failed rather than just counting misses.

**Revision decision.** Set the chain targets, every backend task carries a route declaration, sampled declarations match the map's prescription at high rate, and mid-task risk shifts trigger documented re-routes.

**Retained seed evidence.** All four seed reliability rows with thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which dispatch decay modes need standing detection and what triggers each check. The seed seed's drift and surge rows miss the router's specific decay modes, coupling rot where destination revisions stale the map's inline section names, vocabulary drift where new ticket language stops matching row conditions, and revision lag where the bundle updates and routed habits do not.

**Recommended default and causal basis.** Wire each detection to its triggering event, bundle change runs the script, quarterly ticket sample refreshes the card, and archive updates invalidate memorized routes explicitly. All three are synchronization failures between artifacts on different change cadences, destinations change faster than the router, product vocabulary changes faster than the card, and the bundle changes faster than memorized habits.

**Operating conditions and assumptions.** Change events are observable, an archive updated silently defeats event-triggered detection and falls back to scheduled checks. This table catalogs dispatch decay, decay of the destination content itself belongs to the playbook theme's failure table.

**Failure boundary and alternatives.** Each mode fails softly, routes keep resolving to plausible files while their precision quietly degrades, the reader gets a working-looking dispatch whose section-level accuracy is gone. Bounded alternatives and recoveries: freezing the bundle version this corpus references, eliminating synchronization failures at the price of aging content, a defensible trade for an archival corpus.

**Counterexample, gotchas, and operational comparison.** Coupling rot is invisible from the router's side, the map file's hash is unchanged while its references rot, so monitoring the router file alone gives false assurance precisely when the failure is active. Good: a bundle update automatically running the consistency script and flagging one renamed section. Bad: trusting the map because its file has not changed. Borderline: skipping card refresh in a quarter with no new ticket shapes, acceptable when the sample confirms the vocabulary held.

**Verification, evidence, and uncertainty.** Confirm each failure row names its trigger event, its detector, and its owner, and that triggers have fired historically. The router's hard-coded destination references and the differing change cadences observed across the bundle. Actual revision frequency of the upstream archive is outside this corpus's visibility.

**Second-order consequence.** The three modes share one mitigation shape, re-synchronization triggered by the faster artifact's change events, which means none needs a calendar, each needs a hook on the event that causes it, revision hooks beating scheduled reviews for all three.

**Revision decision.** Add the three synchronization rows, coupling rot caught by the heading-consistency script, vocabulary drift caught by card review against fresh tickets, revision lag caught by re-announcing routes after bundle changes.

**Retained seed evidence.** All four seed failure rows with mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| request surge overloads path | traffic spikes exceed handler, pool, or coroutine limits | apply rate limits, queue bounds, cancellation, and rollback playbook before rollout |
| security boundary silently fails | auth, permission, or input validation assumptions are untested | run abuse-case tests and require explicit deny-by-default behavior |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide how many dispatch retries a failed route deserves and what each retry must change. The seed seed's retry bullets govern corpus generation, while dispatch has its own retry question, what to do when a route fails, the files read did not answer the task, and naive re-routing just re-runs the same lookup into the same miss.

**Recommended default and causal basis.** Allow two structured retries per failed route, re-classify then escalate, and convert any third miss into a recorded gap rather than another attempt. A failed route means the classification was wrong or the map lacks a row, so the retry ladder is diagnostic, first re-classify with the task's surprise information, then escalate a tier toward the fallback sequence, then treat the miss as a map gap and route by nearest row while recording the gap.

**Operating conditions and assumptions.** Misses are recognized honestly, a reader who stretches destination content to cover the miss never triggers the ladder and the gap goes unrecorded. This section governs retrying dispatch decisions, retrying backend operations at runtime is destination content owned by the security sibling and routed accordingly.

**Failure boundary and alternatives.** The anti-pattern is silent looping, re-reading the same prescribed files hoping for a different answer, or abandoning routing entirely after one miss and reverting to keyword habits. Bounded alternatives and recoveries: immediate human escalation on first miss for high-stakes work, trading the learning signal for latency safety.

**Counterexample, gotchas, and operational comparison.** Tier escalation must go up the ladder toward more reading, never sideways to a different guess at the same tier, sideways retries are keyword routing with extra steps. Good: a miss re-classified from delivery to resilience after the task revealed durable-retry needs. Bad: re-reading the playbook three times for a session-cookie question. Borderline: jumping straight to the fallback sequence on first miss, wasteful but safe, the recorded reason keeps it honest.

**Verification, evidence, and uncertainty.** Review recorded route misses for the ladder's structure, changed classification, escalated tier, then recorded gap. The map's tier structure and its lack of any self-revision mechanism read in full. Real-world miss rates for this bundle's rows are unknown until records accumulate.

**Second-order consequence.** Route misses are the map's only organic improvement signal, a recorded gap with the workaround chosen is a draft row for the next map revision, so the retry ladder's final step is simultaneously failure handling and the map's evolution mechanism.

**Revision decision.** Add the dispatch retry ladder, one re-classification with new information, one tier escalation, then a recorded map-gap workaround, with backpressure halting new routing shortcuts while known gaps sit unrecorded.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence each routed task must leave behind for dispatch practice to be auditable. The seed seed logs latency and error counters, but dispatch observability needs different records, the route declaration per task, the map row cited, deviations with reasons, mid-task re-routes, and recorded route misses with their workarounds.

**Recommended default and causal basis.** Emit the route record at review time in the PR description or review template, keeping it terse enough that emission survives deadline pressure. Every routing metric, target, and failure detector defined above consumes these records, without them the declaration rate, match rate, tier attributions, and map-gap signals are all unmeasurable, the checklist is the data layer under the whole practice.

**Operating conditions and assumptions.** The record lands where audits already look, a routing log in a separate system nobody samples is observability theater. This checklist specifies dispatch records, service runtime observability is destination content that routes to the ops sibling.

**Failure boundary and alternatives.** Routing that leaves no trace makes every later audit reconstruct from memory, and memory reconstructs the route that should have happened, not the one that did. Bounded alternatives and recoveries: lightweight tooling that pre-fills the record from the cited row, worth building only after manual records prove the practice sticks.

**Counterexample, gotchas, and operational comparison.** Recording only deviations feels efficient but destroys the denominator, match-rate arithmetic needs the compliant routes recorded too, not just the interesting ones. Good: a PR line citing the migration task-type row with one documented file addition. Bad: a quarter of backend PRs with no route trace at all. Borderline: verbal route declarations in standups, better than silence, invisible to any later audit.

**Verification, evidence, and uncertainty.** Sample recent backend PRs and confirm route records exist, cite live rows, and note deviations. The dependence of every earlier metric and target on these records, read against the seed's runtime-flavored checklist. The record-keeping burden teams will tolerate long-term is untested.

**Second-order consequence.** The route record is self-describing in a way code telemetry is not, citing the map row embeds the expected file list by reference, so a single line captures both what was prescribed and what was done, the comparison any audit needs.

**Revision decision.** Define the minimal route record, task identifier, cited map row, file list emitted, deviations with reasons, re-routes, and misses, one or two lines per task in the existing review flow.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture error count, timeout count, retry count, saturation signal, and rollback trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove the routing practice is fast enough to sustain and precise enough to trust. The seed latency ceilings measure services, but this theme's performance question is dispatch speed and precision, how quickly a task resolves to its file list and how little excess reading the list contains.

**Recommended default and causal basis.** Verify routes stay under the minute budget and read lists stay lean, attributing chronic excess to the tier that emitted it. Routing performance has two axes that trade against each other, faster routes come from coarser tiers which prescribe more reading, so the verification method must measure both lookup time and read-list precision, not either alone.

**Operating conditions and assumptions.** Route records capture the emitted list, precision cannot be reconstructed from memory of what was read. This method verifies dispatch performance, the routed destinations' runtime performance methods are their own subject.

**Failure boundary and alternatives.** Optimizing lookup speed alone drives everyone to the fallback sequence, instant to choose and maximally wasteful to execute, the seed's own pass condition, identifying the next action without reading unrelated files, is precisely the precision axis. Bounded alternatives and recoveries: ignoring dispatch performance entirely on the grounds that seconds do not matter, defensible for tiny teams, it forfeits the drift signal that slow routes carry.

**Counterexample, gotchas, and operational comparison.** Excess reading is not always waste, risk files read and found inapplicable still discharge the review duty the map assigned, precision scoring must distinguish unread-irrelevant from read-and-cleared. Good: quarterly data showing task-type routes reading half the files of mode routes at equal outcomes. Bad: praising instant routes that all resolve to the full sequence. Borderline: a slow route on a genuinely novel task shape, expected, it should end in a recorded gap, not a budget breach.

**Verification, evidence, and uncertainty.** Compute lookup-time and precision distributions from route records each quarter and compare tiers. The seed's read-nothing-unrelated pass condition and the map's tier economics read in full. Acceptable precision baselines per tier await the first measured quarter.

**Second-order consequence.** Precision is measurable retroactively from route records plus outcomes, a prescribed file whose content shaped no decision was excess, so the same records powering match-rate audits also price each tier's real reading cost, no new instrumentation needed.

**Revision decision.** Measure per-route lookup time against the minute budget and read-list precision as the share of prescribed files that proved relevant, reviewing both distributions quarterly.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require a service-specific SLO before deployment; absent that, keep local verification to p95 under 200 ms and p99 under 500 ms for representative handlers or document why latency does not apply.
Leading indicator to measure: compile attempts and review comments decrease because the API shape is explicit before implementation.
Failure signal to watch: the reference hides ownership or error tradeoffs behind generic guidance.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what bundle count, team count, or task volume this routing practice must be redesigned rather than stretched. The seed seed bounds task scale, but routing has its own scale seams, the map serves one bundle, so more bundles need a router of routers, more teams multiply vocabulary cards, and heavier task volume eventually demands routing automation.

**Recommended default and causal basis.** Run the practice as designed within one bundle, one team, and human-speed volume, and treat any seam crossing as a design event for the routing layer itself. Each seam follows from a linear assumption in the current design, one map assumes one destination set, one card assumes one team vocabulary, and manual lookup assumes task volume where seconds-scale routing stays negligible in aggregate.

**Operating conditions and assumptions.** Someone owns noticing the seams, growth in bundles, teams, or volume arrives gradually and the linear assumptions fail without announcing themselves. This statement bounds the dispatch practice, the destination content's scale limits are stated by the playbook theme's boundary section.

**Failure boundary and alternatives.** Stretching past the seams without redesign produces predictable shapes, cross-bundle questions bouncing between corpus themes with no dispatcher above them, and card forks drifting apart across teams until the same ticket routes differently by floor. Bounded alternatives and recoveries: centralizing all routing into one corpus-wide dispatcher now, premature for current scale, the per-bundle map plus adjacent-routing mesh carries the present load.

**Counterexample, gotchas, and operational comparison.** The multi-team seam is the sneakiest because card forks are locally rational, each team tunes its own vocabulary, and the divergence only surfaces when engineers move between teams and route the same work differently. Good: a second backend bundle triggering an explicit cross-bundle routing note instead of ad hoc guessing. Bad: five teams maintaining five silently diverged cards. Borderline: partial automation that pre-fills route records while humans still classify, a reasonable seam-straddling step.

**Verification, evidence, and uncertainty.** At each growth event, re-test the three linear assumptions and record which still hold. The map's single-bundle charter and this corpus's own adjacent-routing mesh read in full. The volume threshold where manual routing aggregates into real cost is unestimated.

**Second-order consequence.** This corpus is already pressing the first seam, its adjacent-routing sections are a distributed router of routers, each theme pointing sideways at its neighbors, the seam is crossed not by one new artifact but by keeping those distributed pointers mutually consistent.

**Revision decision.** Name the three seams, corpus-level routing needs its own layer above per-bundle maps, multi-team use needs card governance, and volume growth needs the route record automated before the manual practice collapses.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Rust Backend Reference Routing stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which checks reveal that this routing document's pointers have gone stale. The seed theme-name queries would return this corpus to itself, while this theme's staleness sources are concrete, upstream revisions of the rust-web-backend-delivery bundle, destination heading changes that rot the map's inline references, and corpus-side changes to the adjacent rust themes this document routes toward.

**Recommended default and causal basis.** Run the three pointer probes together at every corpus refresh cycle and after any archive-touching commit. A routing document ages exactly as fast as the things it points at, so its refresh probes are pointer checks, does the archive hold a newer bundle, do the router's referenced headings still resolve, and do the adjacent corpus themes still exist under their expected names.

**Operating conditions and assumptions.** Probe findings get acted on, a detected heading rot that nobody fixes converts a known-stale pointer into a trusted-stale one, worse than undetected. These probes refresh this document's pointers, refreshing the destinations' ecosystem content belongs to the playbook theme's crate-release probes.

**Failure boundary and alternatives.** Generic web queries cannot detect any of the three, the bundle is private archive content, the coupling is internal, and the adjacent themes are corpus-local, every real staleness source is invisible to a search engine. Bounded alternatives and recoveries: subscribing to archive-change notifications instead of scanning, cleaner when available, the scan works today with no infrastructure.

**Counterexample, gotchas, and operational comparison.** The external URL rows still deserve one probe each eventually, not for routing truth but because the seed presents them as candidates, retiring or confirming them closes a loop this theme inherited rather than chose. Good: a probe catching that a destination renamed a section the map still cites. Bad: a web search for rust backend reference routing best practices. Borderline: probing adjacent themes' content quality rather than existence, beyond pointer freshness, occasionally worth the extra look.

**Verification, evidence, and uncertainty.** Log each probe run with its date and the pointers it confirmed or flagged. The wholly local pointer structure of the router and this document's adjacency claims. How often the upstream archive actually revises is outside corpus visibility.

**Second-order consequence.** All three probes are local filesystem operations, this theme is unique in the rust cluster in needing zero external searching to stay fresh, its entire staleness surface is greppable from the repository root.

**Revision decision.** Replace the name queries with pointer probes, an archive scan for bundle revisions, the heading-consistency script run, and a corpus check that adjacent theme files still match their routed names.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | rust backend reference routing official documentation best practices |
| `github_repository_query_phrase` | rust backend reference routing GitHub repository examples |
| `release_notes_query_phrase` | rust backend reference routing changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide under what label each of this document's statements may be reused elsewhere. The seed label definitions stand alone without this assignment's ledger, one mapped router read fully, four destination files and SKILL.md read fully and cited by name, zero external fetches, and all routing-practice machinery marked as inference.

**Recommended default and causal basis.** Before reusing any claim, test whether it can be pointed at a specific map row or section, cite the row if yes, carry the reasoning if no. The fact side of this document is the router's enumerable structure, six modes, six task-type orders, the tier ladder, the four sections, and the inline destination references, while the practice side, cards, records, metrics, ladders, and seams, is constructed inference built on those facts.

**Operating conditions and assumptions.** The archive bundle stays at its path so fact-class claims remain mechanically checkable. These notes govern reuse of this document's claims elsewhere, quoted routing tables travel with citations, practice machinery travels only with its reasoning attached.

**Failure boundary and alternatives.** The likeliest mislabel is presenting the routing-practice machinery as bundle doctrine, the map prescribes read orders, it never prescribes declarations, match audits, or retry ladders, those are this evolution's additions and must travel labeled as such. Bounded alternatives and recoveries: inline labels per paragraph if the document-level split ever proves too coarse for a dispute.

**Counterexample, gotchas, and operational comparison.** By-name destination citations look like mapped-source facts but rest on files outside the mapped row, reusers must preserve the by-name attribution or the evidence trail breaks at its first hop. Good: reusing the six-mode table with its map citation. Bad: citing the route-declaration requirement as a rust-web-backend-delivery rule. Borderline: reusing the review-order inversion insight, the order is quoted fact, the attention rationale is inference riding on it.

**Verification, evidence, and uncertainty.** Sample claims from earlier sections and confirm each lands cleanly on one side of the published split. This assignment's read ledger, six bundle files read in full, zero retrievals. Readers can verify the citations but not the reading behind them.

**Second-order consequence.** This theme has the cleanest boundary in the rust cluster because its source is pure structure, there is no prose doctrine to paraphrase and blur, a claim here either quotes a table or it is inference, with almost nothing in between.

**Revision decision.** Publish the split, everything countable in reference-map.md is local corpus fact, everything about how teams should operate the map is combined-evidence inference.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
