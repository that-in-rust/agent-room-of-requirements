# Rust Conventions Quality Gates

**Decision supported.** This section helps decide what an agent or reviewer enforces at the end of Rust planning, implementation, or review. The seed no seed line states the mapped file's declared position in the workflow, use this file near the end of planning, implementation, or review, it is a closing gate layer, not a design guide, applying local conventions selectively and enforcing final quality gates after the substantive decisions are made.

**Recommended default and causal basis.** Apply the conventions selectively during implementation and run the full gate battery before any handoff or release claim. The file's opening sentence fixes its tempo, everything inside is either a convention to apply when feasible or a gate to require before handoff, so its authority is strongest at the finish line and weakest as upstream design doctrine.

**Operating conditions and assumptions.** The work is Rust under this bundle's process, other-language work and non-spec-driven Rust take only the general-Rust subset. This reference covers end-stage conventions and gates for Rust work under the executable-specs bundle, upstream requirement and design doctrine lives with the bundle's other files and adjacent themes.

**Failure boundary and alternatives.** Reading this theme as a design reference inverts its role, teams that consult gates first design toward passing checks rather than toward the requirements the checks exist to protect. Bounded alternatives and recoveries: the rust-coder reliability theme for the deep pattern doctrine behind several of these gates, this file is the checklist edge of that larger body.

**Counterexample, gotchas, and operational comparison.** Selective is load-bearing in section 1's title, four-word naming and Mermaid documentation are feasibility-conditioned local conventions, not laws, and the file polices its own rules twice more in section 7. Good: a review that runs the command gate and walks the checklist before approval. Bad: redesigning module boundaries from this file alone. Borderline: consulting the anti-pattern list mid-implementation, useful early, the command gate still runs at the end.

**Verification, evidence, and uncertainty.** Check that finished work under this theme cites the gate battery's results and the checklist state. The 74-line mapped file read in full this session. How the 202604 command set has aged against current cargo tooling is unknowable without external retrieval.

**Second-order consequence.** The file is symmetric in a way few gate documents are, sections 1 through 5 say what to require while sections 6 and 7 say what to reject and, rarer still, which of its own house rules must not be universalized, a built-in overreach brake.

**Revision decision.** Open with the end-stage framing and the file's two-sided structure, positive conventions and gates on one side, explicit rejection and de-universalization lists on the other.

**Retained seed evidence.** The exact theme title and gate framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source justifies each claim class reused from this theme. The seed one local row carries the theme while the file's content chains outward twice, its checklist requires each REQ-RUST-* requirement to link a test, importing the bundle's requirement format, and its anti-pattern list forbids L3 dependencies leaking into L1 core, importing the bundle's layering model, neither defined in the mapped file itself.

**Recommended default and causal basis.** Cite the mapped file by section number for its own content and name the bundle for chained contracts. The file is a bundle member, its gates enforce contracts other bundle files define, so provenance for the requirement-format and layering claims runs through the rust-executable-specs-01 bundle beyond the single mapped row.

**Operating conditions and assumptions.** The 202604 archive path remains stable for citation resolution. Provenance for this document's statements only, the four external URLs stayed unretrieved throughout this evolution and confer no current-fact authority.

**Failure boundary and alternatives.** Attributing the REQ-RUST-* format or the L1-to-L3 model to this file alone breaks the provenance trail, this file consumes those definitions as gate inputs, it does not author them. Bounded alternatives and recoveries: a future mapping revision adding the bundle's requirement and layering files as mapped rows, closing the two chained gaps.

**Counterexample, gotchas, and operational comparison.** The four external rows are the rust-cluster template set again, tokio and axum anchors fit section 3's async gates loosely and the naming, checklist, and de-universalization content not at all. Good: citing section 4 for the required command list. Bad: citing this file as the definition of L1/L2/L3 layering. Borderline: citing the checklist for the requirement-test linkage rule, correct as a gate, the format itself is bundle-defined.

**Verification, evidence, and uncertainty.** Trace disputed claims to the exact numbered section or named bundle concept that contains them. Full read this session of the mapped file and its two outward references identified. The bundle's other files were not mapped or read this assignment, their content is known only by the concepts this file imports.

**Second-order consequence.** The seed's heading signals stop at section 5, omitting the anti-patterns and rules-not-to-universalize sections, so the mapping row underdescribes exactly the two sections that make this file distinctive, an audit should not trust the signal list as a completeness proxy.

**Revision decision.** Anchor on the mapped file for convention, gate, checklist, and rejection claims, and mark the requirement-format and layering references as bundle-chained claims cited by concept name.

**Retained seed evidence.** The single local row and all four external rows with their column values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-executable-specs-01/references/rust-conventions-and-gates.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://github.com/rust-lang/api-guidelines | external_research_source_material | external_research_sourced_fact | Rust library-team API design recommendations |
| https://github.com/tokio-rs/tokio | external_research_source_material | external_research_sourced_fact | async runtime implementation and operational model |
| https://github.com/tokio-rs/axum | external_research_source_material | external_research_sourced_fact | Rust web framework implementation and design claims |
| https://docs.rs/axum/latest/axum/ | external_research_source_material | external_research_sourced_fact | published crate documentation for routing and extractors |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide how much verification each Rust change must buy before handoff. The seed scored corpus rows stand where the file's own priority structure is a hard-soft split, the four required commands, fmt check, clippy with denied warnings, full-feature tests, full-feature build, are unconditional, the two advanced commands, release tests and branch coverage at a seventy-five percent line floor, escalate only for higher-risk changes.

**Recommended default and causal basis.** Wire the four-command floor into CI unconditionally and trigger the advanced pair on a named risk classification. The split prices verification by risk, every change pays the four-command floor because it is cheap and mechanical, while release-mode testing and coverage floors cost enough that the file reserves them for changes whose failure cost justifies them.

**Operating conditions and assumptions.** Risk classification exists, without it the advanced gates either run always or never, both wrong. This ranking orders verification effort under this theme, pattern-level reliability rankings live with the rust-coder theme's sixty-pattern scoreboard.

**Failure boundary and alternatives.** Flattening the split fails both ways, running coverage gates on every doc fix burns pipeline budget, and skipping the four-command floor on small changes is exactly the drift the unconditional wording forbids. Bounded alternatives and recoveries: risk-proportional coverage floors varying by module criticality, finer than the file's single seventy-five percent line, at the cost of a threshold table to maintain.

**Counterexample, gotchas, and operational comparison.** All four required commands carry all-targets and all-features flags, dropping the flags quietly shrinks the gate, feature-gated code that never builds in CI is the standard escape this wording exists to close. Good: a feature PR passing all four floor commands with full flags. Bad: a clippy run without denied warnings counted as the gate. Borderline: skipping release-mode tests on a low-risk refactor, correct by the split, the risk call should be recorded.

**Verification, evidence, and uncertainty.** Compare CI configuration against the four required commands verbatim, flags included. Section 4's two command blocks read in full. The seventy-five percent line floor's fit for any particular codebase is a local calibration.

**Second-order consequence.** The four required commands are ordered by failure speed in practice, fmt fails in seconds, clippy in tens of seconds, tests and build last, so running them in the file's listed order is also the cheapest-first diagnostic sequence, the list doubles as an execution plan.

**Revision decision.** Present the hard-soft split as the operative ranking and keep the scored seed rows as corpus-process emphasis.

**Retained seed evidence.** The three scored seed rows with tier labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `rust_conventions_quality_gates` | 95 | default_adoption_pattern_tier | Source Map First: Load local rust conventions material before synthesizing quality gates recommendations. |
| `rust_conventions_quality_gates` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `rust_conventions_quality_gates` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide which of this theme's rules bind always and which bind only when feasible. The seed generic corpus formulas stand where the file's implicit thesis is conditional enforcement, apply local conventions when feasible, require universal gates always, and never let the local half masquerade as the universal half, the whole file is an exercise in keeping those two authorities separate.

**Recommended default and causal basis.** Enforce universal gates without exception and apply local conventions through a feasibility judgment that can be overridden with reasons. Every section carries the split, section 1 conditions its conventions on feasibility and risk, sections 3 and 4 speak in unconditional verify-and-require language, and section 7 exists solely to stop the local rules from leaking into universal doctrine.

**Operating conditions and assumptions.** Reviewers can tell the classes apart, which requires the tagging the revision prescribes. The thesis governs convention-versus-gate authority under this theme, what the conventions and gates contain is the business of their own sections.

**Failure boundary and alternatives.** Collapsing the two authorities produces the failure section 7 names, repeated duplicated doctrine copied verbatim into every skill or plan, house style hardening into false law as it travels. Bounded alternatives and recoveries: a single flat rule list with uniform authority, simpler to publish and the exact design section 7 was written to prevent.

**Counterexample, gotchas, and operational comparison.** Some rules sit in both worlds, avoiding unwrap in production paths is stated as a convention in section 2 but mirrors the reliability doctrine's universal rejection, the class boundary runs through individual rules, not just sections. Good: waiving four-word naming on a stable public API with the risk stated. Bad: waiving the clippy gate the same way. Borderline: Mermaid diagrams on a project without the standard, section 1 itself says do not apply it universally.

**Verification, evidence, and uncertainty.** Sample reused rules for authority tags and check waivers only ever attach to the local class. The conditional and unconditional wording patterns across all seven sections read in full. Whether the two-class model covers future rule additions is a maintainer judgment.

**Second-order consequence.** The file's most exportable idea is that a quality document should ship its own de-universalization list, section 7 is metadata about the other sections' scope, and any team importing this file's rules inherits the obligation to import their boundaries too.

**Revision decision.** State the two-authority thesis explicitly and tag every rule reused from this theme with its authority class, feasibility-conditioned local or unconditional universal.

**Retained seed evidence.** The three labeled thesis statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `rust_conventions_quality_gates` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Rust Conventions Quality Gates comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide how to consult a seven-section gate file efficiently at each closing stage. The seed map row lists five heading signals for a seven-section file, and no seed line explains the file's internal reading order, conventions first as implementation guidance, gates second as verification, then the two negative sections as the closing sweep the end-stage framing implies.

**Recommended default and causal basis.** Enter the file at the section matching the closing question and always finish review consultations with sections 6 and 7. The file's use statement, near the end of planning, implementation, or review, means most consultations arrive late and short on time, so knowing which sections answer which closing question is the map this row should carry.

**Operating conditions and assumptions.** The reader knows their stage, mid-implementation questions take sections 2 and 3, handoff takes 4 and 5. Navigation of the mapped file, bundle-level navigation belongs to the bundle's own entry documents.

**Failure boundary and alternatives.** A late-stage reader who stops at the checklist misses the anti-pattern sweep, and one who reads only the positive sections can enforce a local convention section 7 explicitly bounds. Bounded alternatives and recoveries: folding the file's content into CI configuration and PR templates directly, faster per use, disconnected from the section 7 boundaries that keep the rules honest.

**Counterexample, gotchas, and operational comparison.** Section 3's runtime gates are review questions phrased as verifications, no blocking on executors, no locks across await, no secrets in logs, they need a human or tool actually checking, listing them in a template does not run them. Good: a handoff that walks sections 4 and 5 then sweeps 6 and 7. Bad: a review that reads only the heading-signal five and misses both negative sections. Borderline: quoting section 2's API conventions during design, early but harmless, the authority tag travels with the quote.

**Verification, evidence, and uncertainty.** Check that recent consultations entered at the stage-matched section and included the negative sweep. The file's seven-section structure and use statement read in full. Actual consultation patterns by past users are unrecorded.

**Second-order consequence.** The checklist is the file's only self-referential gate, its final item forbids placeholder markers in finalized code, the same class of marker this corpus's own verifier polices, the file and the corpus enforce the same hygiene at different layers.

**Revision decision.** Annotate the row with the full seven-section structure and the consultation pattern, sections 2 and 3 during implementation, sections 4 and 5 at handoff, sections 6 and 7 as the review sweep.

**Retained seed evidence.** The single local source row with title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-executable-specs-01/references/rust-conventions-and-gates.md | Rust Conventions and Gates | Rust Conventions and Gates; 1) Selective Local Conventions; 2) Implementation Conventions; 3) Runtime and Safety Gates; 4) Verification Command Gate; 5) Release Readiness Checklist | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide which external targets deserve retrieval effort when this theme's claims need freshness. The seed four inherited framework anchors stand where this theme's real external surface is the cargo toolchain its command gate names, fmt, clippy, test, build, and llvm-cov, whose flags and behaviors evolve with cargo releases while the framework rows have no bearing on any command in the file.

**Recommended default and causal basis.** Prioritize a dated cargo-llvm-cov check when refreshing this theme and treat the first-party command floor as slow-moving. The gate battery is tool-version-sensitive in its details, flag names, lint sets, and coverage tooling change across releases, so this theme's freshness risk concentrates in the exact command lines section 4 fixes.

**Operating conditions and assumptions.** Any check pins the version it observed against the 202604 anchor. External rows serve future freshness verification only, all four remained unretrieved throughout this evolution.

**Failure boundary and alternatives.** Treating the template rows as this theme's verification queue would freshen axum extractor docs while the llvm-cov invocation, the most tooling-fragile line in the file, has no queued check. Bounded alternatives and recoveries: reading a real workspace's CI logs across toolchain updates, which reveals actual drift faster than release-note surveys.

**Counterexample, gotchas, and operational comparison.** Clippy's lint set grows across releases, so a pinned command line can start failing on new lints without any code change, the denied-warnings gate imports the toolchain's evolution as intentional pressure, teams should know that is the design. Good: a dated release-note check before asserting the coverage invocation is current. Bad: citing the tokio row to freshen the fmt gate. Borderline: an api-guidelines fetch for section 2's API conventions, genuinely adjacent, still not a command-gate source.

**Verification, evidence, and uncertainty.** Confirm externally-flavored claims name a dated retrieval or carry the unretrieved-candidate label. Zero fetches this assignment, the command inventory read in full from section 4. How far the 202604 command lines have drifted from current tooling is unknowable without the checks.

**Second-order consequence.** The four required commands are all first-party cargo subcommands, only the optional coverage gate depends on a third-party tool, so the unconditional half of the gate battery is far more drift-resistant than the advanced half, the risk split and the freshness split coincide.

**Revision decision.** Keep the rows as inherited candidates, flag the toolchain gap, and route real freshness needs through dated checks of cargo and cargo-llvm-cov release notes.

**Retained seed evidence.** All four external rows with their boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://github.com/rust-lang/api-guidelines | Rust API Guidelines | Rust library-team API design recommendations | external_research_sourced_fact |
| https://github.com/tokio-rs/tokio | Tokio repository | async runtime implementation and operational model | external_research_sourced_fact |
| https://github.com/tokio-rs/axum | Axum repository | Rust web framework implementation and design claims | external_research_sourced_fact |
| https://docs.rs/axum/latest/axum/ | Axum docs.rs | published crate documentation for routing and extractors | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which work products reviewers must reject at this theme's closing sweep. The seed three corpus-process rows stand where the mapped file ships its own seven-item rejection list, ambiguous requirements without measurable assertions, monolithic mixed-responsibility modules, hard concrete dependencies blocking tests, L3 leakage into L1 core, blocking or locks across await, library APIs returning application-grade errors, and concurrency code with no stress, model, or cancellation validation.

**Recommended default and causal basis.** Walk the seven rejections as a named review sweep after the command gate passes. The seven rejections span the bundle's whole pipeline, two police requirements and architecture, two police testability and layering, three police runtime Rust, so the list is the bundle's process contract restated as review vocabulary.

**Operating conditions and assumptions.** Reviewers can see architecture, the middle rejections need repository context a diff view hides. Work-product rejections under this theme, the seed's corpus-generation rows keep their own scope.

**Failure boundary and alternatives.** Each rejection ships green without its check, ambiguous requirements pass every command gate, layer leakage compiles cleanly, and unvalidated concurrency passes single runs, the list exists because the command battery cannot see any of them. Bounded alternatives and recoveries: encoding the mechanical subset as lints and grep rules, worthwhile, four of the seven remain judgment reviews regardless.

**Counterexample, gotchas, and operational comparison.** The runtime three duplicate reliability-theme doctrine deliberately, the bundle restates them so its own closing gate is self-sufficient, but fixes should cite the deeper theme's clauses, this list names the offense, the reliability doctrine names the repair. Good: blocking a merge whose new requirement has no measurable assertion. Bad: approving a service layer importing the database driver into L1 core. Borderline: a concurrency change validated by one stress run, the row asks for stress, model, or cancellation validation, one leg may satisfy it if chosen deliberately.

**Verification, evidence, and uncertainty.** Check each registry row names its detection route and appears in the review sweep record. Section 6's seven rejections read in full. Relative incidence of the seven rejections in real spec-driven Rust work is unmeasured.

**Second-order consequence.** The list's deepest row is the testability one, hard concrete dependencies blocking unit or integration testing, it rejects an architecture for what it prevents rather than what it does, a review question invisible to every tool in the command gate and answerable only by asking what cannot be tested here.

**Revision decision.** Import the seven rejections with detection routes, requirement review for the first, module and dependency review for the middle pair, layering audit for the leakage row, and the reliability theme's mechanical checks for the runtime three.

**Retained seed evidence.** The three seed process rows with their detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide what evidence a Rust change must show before it may claim release readiness. The seed document verifier stands where the mapped file provides this corpus's most literal gate content, four required cargo commands with full-target full-feature flags and two optional escalation commands, the only theme in the rust cluster whose source ships runnable gate lines verbatim.

**Recommended default and causal basis.** Require the four commands green plus the six checklist items affirmed before any release claim. Section 4's wording is contractual, run and require success, so the commands are not suggestions to adapt but a floor to reproduce, and any local variation is a departure to justify rather than a style choice.

**Operating conditions and assumptions.** The workspace builds with all features combined, feature matrices with mutually exclusive features need a documented gate variant. Code verification gates for work under this theme, the document verifier keeps its corpus jurisdiction.

**Failure boundary and alternatives.** Paraphrased gates drift, a CI file that runs clippy without all-features or tests without all-targets passes most days while quietly ungating exactly the configurations the flags exist to force. Bounded alternatives and recoveries: richer gate stacks from the reliability theme, Miri, loom, fuzzing, layered on top for boundary-heavy changes, this file's battery is the floor, not the ceiling.

**Counterexample, gotchas, and operational comparison.** The checklist's requirement-linkage item binds only under the bundle's requirement format, teams using this file outside the bundle should map that item to their own traceability convention rather than dropping it. Good: a release PR attaching four green commands and a checked checklist. Bad: a handoff claiming readiness on tests alone. Borderline: waiving the coverage gate on a low-risk change, allowed by the optional framing, the risk call should be written down.

**Verification, evidence, and uncertainty.** Diff the CI configuration against section 4's command lines verbatim and sample releases for checklist records. Sections 4 and 5 read in full. The marginal defect yield of the optional pair on typical changes is unmeasured here.

**Second-order consequence.** The command gate and the checklist verify different failure classes by design, the commands catch what machines can see, format, lints, test failures, build breaks, while the checklist catches what only humans can, requirement linkage, threshold-bearing performance claims, documentation truth, neither substitutes for the other.

**Revision decision.** Adopt the four-command floor verbatim, wire the two advanced commands to a recorded risk classification, and pair the battery with section 5's checklist as the human half of the gate.

**Retained seed evidence.** The seed's document verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide what completion contract an agent working under this theme must satisfy. The seed four generic bullets stand where this file implies a sharp agent contract, agents produce work that arrives at the gate, so the file's content is best injected as completion criteria, an agent's definition of done is the four commands green, the checklist affirmable, and the seven rejections absent.

**Recommended default and causal basis.** Require agents to emit the command outputs and a checklist affirmation alongside any completion claim. Agents optimize whatever completion signal they are given, a prompt that ends at code compiles ships at the weakest gate, while a prompt carrying this file's battery makes the agent run the floor itself before claiming completion.

**Operating conditions and assumptions.** The agent can execute commands, advisory-only agents attach the battery as explicit human follow-up instead of claiming it. Agent behavior over this theme's material, upstream requirement-writing agent rules live with the bundle's spec doctrine.

**Failure boundary and alternatives.** Agents given the conventions without the authority split universalize the local half, four-word naming applied to a stable public API is section 7's named failure executed by an obedient agent. Bounded alternatives and recoveries: post-hoc human gating of agent output with no agent-side contract, workable at low volume, it converts every agent completion into a review queue item.

**Counterexample, gotchas, and operational comparison.** An agent seeing the checklist's requirement-linkage item without the bundle context may invent requirement IDs to satisfy the letter of the gate, traceability theater, the linkage must point at real requirement artifacts. Good: an agent completion message attaching four green command outputs. Bad: an agent claiming done on successful compilation. Borderline: an agent affirming the documentation item on a docs-untouched change, fine when it states why the item is vacuous.

**Verification, evidence, and uncertainty.** Reject agent completion claims lacking command evidence or carrying unverifiable checklist affirmations. The gate battery, checklist, and section 7 boundaries read in full. How reliably agents self-enforce gate contracts across long sessions lacks measurement.

**Second-order consequence.** The checklist's placeholder-marker item is the most agent-relevant line in the file, generated code is where deferred-work markers accumulate silently, so an agent that greps its own output for placeholders before handoff closes the gap the checklist was written to catch.

**Revision decision.** Inject the gate battery as the agent's completion contract, the checklist as its self-review, and section 7 verbatim as the boundary on which conventions it may generalize.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide which entry into this theme matches the reader's current closing stage. The seed one generic engineer stands where the file's own use statement names three arrival stages, a planner closing a design who needs the conventions and rejection list as constraints, an implementer at handoff who needs the command battery and checklist, and a reviewer who needs the negative sections as a sweep.

**Recommended default and causal basis.** Identify the stage before opening the file and enter at that stage's sections. The file says near the end of planning, implementation, or review, three different ends, and each stage consumes different sections at different depths, so the journey determines both entry point and reading budget.

**Operating conditions and assumptions.** The stage is honest, work labeled review that is actually still implementation takes the implementer path. Journeys through this gate file, journeys through the bundle's spec-writing stages belong to the bundle's own themes.

**Failure boundary and alternatives.** Stage-blind consultation misallocates the file, a planner running the command gate has nothing to run it on, and a reviewer reading only the conventions approves work the rejection list would have caught. Bounded alternatives and recoveries: a single all-stages reading order, simpler to teach, it spends planner time on commands they cannot run yet.

**Counterexample, gotchas, and operational comparison.** The planner journey is the least obvious and most leveraged, reading section 6's rejections at planning time prevents the architectures that fail review later, the negative sections work upstream even though the file frames itself as end-stage. Good: a reviewer sweeping sections 6 and 7 against attached battery results. Bad: an implementer discovering the layering rejection after the architecture is set. Borderline: a planner walking the checklist as a preview, harmless, affirmations only count at handoff.

**Verification, evidence, and uncertainty.** Ask recent users which stage they entered from and whether the section set matched their need. The use statement and per-section stage fit read in full. The actual stage mix of consultations per team is unmeasured.

**Second-order consequence.** The reviewer journey is the only one that can be fully evidence-driven, arriving after the battery has run means review time goes entirely to the judgment content, the rejections and boundaries, which is the highest-value use of scarce reviewer attention the file's structure enables.

**Revision decision.** Recast the scenario as three staged entries, planner into sections 1, 6, and 7, implementer into 2 through 5, reviewer into 6 and 7 with the battery results in hand.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Rust reliability engineer is starting from a requirement that needs a safe API, explicit error model, and testable boundary and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `rust_conventions_quality_gates` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the idiomatic ownership, async, error, and crate-boundary shape before coding.
Reference opening trigger: Open this file when the task mentions rust conventions quality gates, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how recurring convention-versus-cost arguments get settled under this theme. The seed template rows skip the file's live tensions, naming clarity versus API stability, where section 1 resolves toward wrappers and adapters over risky renames, convention uniformity versus project fit, where Mermaid binds only on projects already standardized, and gate strictness versus iteration speed, where the advanced commands price in risk.

**Recommended default and causal basis.** Resolve each axis by its written mechanism and record any waiver with the interest it preserves. Each tension carries a written resolution with a stated mechanism, compatibility preserved through adapters, documentation conventions conditioned on existing standards, verification escalated by risk class, the file trades in mechanisms rather than exhortations.

**Operating conditions and assumptions.** Waivers name interests, a waiver that names convenience is a defect, not a resolution. Tuning within this theme's rules, deep reliability tradeoffs live with the rust-coder theme's clause system.

**Failure boundary and alternatives.** Each tension has a seductive wrong pole, renaming stable APIs for naming purity breaks downstreams, universal Mermaid mandates decorate projects that render none of it, and always-maximal gates teach teams to route around CI. Bounded alternatives and recoveries: hard style-guide mandates fixing one pole per axis, cheaper to enforce, they discard the mechanism information the file's resolutions encode.

**Counterexample, gotchas, and operational comparison.** The compatibility resolution can decay into permanent adapter accretion, wrappers added to avoid breakage should carry removal intent, otherwise the codebase accumulates naming eras like sediment. Good: an adapter preserving a stable API while new surfaces take clear names. Bad: a rename cascade through a published crate for naming compliance. Borderline: adopting Mermaid on a half-standardized project, the condition is about existing practice, half counts as a judgment call to record.

**Verification, evidence, and uncertainty.** Audit recent waivers for named interests and revisit adapters older than their stated intent. Section 1's resolution mechanisms and section 4's risk split read in full. How often the mechanisms suffice without escalation is unmeasured here.

**Second-order consequence.** All three resolutions share one shape, preserve the interest the rule protects while varying the rule's surface, clarity survives through an adapter, documentation quality survives without Mermaid, verification survives at floor strength, the file consistently bends surfaces to protect interests.

**Revision decision.** Add the three axes with the file's resolutions and the recorded-waiver discipline the local class requires.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the rust conventions quality gates pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong rust conventions quality gates guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which document settles a question when this gate file and a deeper source both plausibly apply. The seed lone canonical row understates a two-axis hierarchy, within the bundle this file is the closing authority on gates while the spec and layering files own the upstream definitions it enforces, and across the corpus its runtime rules are compressed restatements of the rust-coder reliability doctrine that holds the full clauses.

**Recommended default and causal basis.** Resolve gate-content disputes here, requirement-format disputes in the bundle, and runtime-rule depth in the reliability theme. Gate files inherit their content, this one enforces REQ-RUST-* linkage defined elsewhere in the bundle and re-asserts async and error rules the reliability theme derives in depth, so authority questions here always ask which axis the question travels.

**Operating conditions and assumptions.** The bundle and the reliability theme stay consistent with this file's compressions, drift between a compression and its source is resolved toward the source. Precedence for this theme's content, bundle-internal precedence among unmapped sibling files is noted only as far as this file's imports reveal it.

**Failure boundary and alternatives.** The cross-corpus axis invites the misjudgment, settling a nuanced lock-across-await dispute from this file's one-line verification when the reliability theme carries the pattern's full use-when and avoid-when boundaries. Bounded alternatives and recoveries: treating CI configuration as the effective authority, operationally true and intellectually backwards, the config should trace to this file, not replace it.

**Counterexample, gotchas, and operational comparison.** The checklist's placeholder rule and this corpus's verifier enforce the same hygiene independently, a rare case where the mapped file and the corpus tooling are parallel authorities on one rule, agreement is expected but not structural. Good: settling the required flag set from section 4 alone. Bad: deriving cancellation design from section 3's one-line verification. Borderline: quoting this file's unwrap convention in a library review, adequate for the offense, the reliability clauses carry the invariant-story nuance.

**Verification, evidence, and uncertainty.** Test hierarchy claims against each document's self-declared role and the compression-source relationships. The file's imports, compressions, and section 7 self-limits read in full. Unread bundle siblings may claim authority this analysis cannot see.

**Second-order consequence.** Section 7 makes this file self-limiting in the hierarchy too, a document that lists which of its own rules must not be universalized has pre-answered the precedence question for those rules, local always yields to fit, an authority disclaimer few canonical sources carry.

**Revision decision.** Record both axes, this file canonical for the gate battery, checklist, and de-universalization list, the bundle canonical for requirement and layering definitions, the reliability theme canonical for runtime rule depth.

**Retained seed evidence.** The single hierarchy row and the confidence warning remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/rust-executable-specs-01/references/rust-conventions-and-gates.md | canonical primary source | Rust Conventions and Gates; 1) Selective Local Conventions; 2) Implementation Conventions | What guidance, warning, or example should this source contribute to Rust Conventions Quality Gates? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what standing evidence makes a release-readiness claim auditable after the fact. The seed generic worked-example artifact misses this theme's natural object, a gate record for each handoff, one page capturing the four command results with toolchain version, the risk classification and whether the advanced pair ran, the six checklist affirmations with evidence links, and the review sweep's verdict on the seven rejections.

**Recommended default and causal basis.** Generate the record from CI output where possible and require the human blocks, risk call and sweep verdict, as named entries. The file demands run and require success but nothing in it persists the running, so release claims decay into assertions, the gate record is the difference between we gate and we can show the gate.

**Operating conditions and assumptions.** Releases are discrete events, continuous-deployment flows attach the record to deployment units instead. One record per handoff or release claim under this theme, boundary ledgers belong to the reliability theme and suite manifests to the testing themes.

**Failure boundary and alternatives.** Without the record, a post-release defect cannot distinguish gate failure from gate skipping, the two demand opposite fixes, stronger commands versus enforced process. Bounded alternatives and recoveries: trusting CI history as the implicit record, fragile, histories expire, get rewritten, and never contain the human blocks.

**Counterexample, gotchas, and operational comparison.** Checklist affirmations without evidence links regress to the assertion problem the record exists to fix, each affirmed item should point at the test, doc, or threshold that makes it true. Good: a defect retrospective pulling the release's gate record and finding the sweep skipped. Bad: a release claim whose only evidence is a green badge. Borderline: auto-affirming the placeholder item from a clean grep, legitimate, the grep output is the evidence link.

**Verification, evidence, and uncertainty.** Sample recent release claims for complete four-block records. The run-and-require wording and checklist structure read in full. Record upkeep discipline under deadline pressure is the untested variable.

**Second-order consequence.** The record's toolchain-version field quietly solves the clippy drift gotcha, when a new toolchain fails old code the records show exactly which lint generation each release passed under, turning mysterious CI breakage into a documented tooling delta.

**Revision decision.** Define the artifact as the gate record with four blocks, commands, risk call, checklist, sweep, generated at handoff and attached to the release claim.

**Retained seed evidence.** The artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: quality bar rubric with review blockers, lint gates, and release criteria.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Rust Conventions Quality Gates | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which exercise most efficiently builds complete closing-gate habits. The seed abstract usage lines stand where this theme wants a closing-gate walkthrough, take one finished feature and run the full close, execute the four commands in listed order watching cheapest-fail-first, classify the risk and decide the advanced pair, walk the six checklist items attaching evidence, then sweep the seven rejections against the diff.

**Recommended default and causal basis.** Run new contributors through the walkthrough and the drill before they own release closes. The walkthrough exercises every section of the file in its intended sequence, so one rehearsal teaches the whole closing choreography that piecemeal reading never assembles.

**Operating conditions and assumptions.** A practice change with seeded rejections exists, drills on defect-free code teach only the happy path. Teaching this theme's closing procedure, requirement-writing walkthroughs belong to the bundle's spec themes.

**Failure boundary and alternatives.** Engineers who know the sections separately improvise the close under deadline, running commands but skipping the sweep, or affirming the checklist from memory, the partial closes that let section 6's rejections ship. Bounded alternatives and recoveries: shadowing a real release close, authentic and unrepeatable, the seeded drill is the controllable complement.

**Counterexample, gotchas, and operational comparison.** The drill's seeded violations must be tool-invisible by construction, a seeded clippy failure teaches nothing, the point is precisely the judgment content the commands miss. Good: a trainee's close record showing both seeded rejections caught in the sweep. Bad: certifying gate competence from command execution alone. Borderline: running the walkthrough on a trivial docs change, gentle, the risk-classification step degenerates to a formality.

**Verification, evidence, and uncertainty.** Have the trainee close a fresh change unsupervised and audit the resulting gate record. The file's section sequence and the command-versus-judgment split read in full. Habit persistence without periodic real closes is unmeasured.

**Second-order consequence.** The failure drill teaches the file's central lesson mechanically, the command gate is necessary and insufficient, feeling a green battery coexist with two real rejections converts the sweep from ceremony into the half of the gate that catches what machines cannot.

**Revision decision.** Anchor the section on the full-close walkthrough plus one failure drill, hand the learner a change that passes all four commands while violating two rejections, layering leakage and missing cancellation validation, and require the sweep to catch both.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Rust Conventions Quality Gates after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Rust Conventions Quality Gates as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Rust Conventions Quality Gates only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which measurements prove this theme's closing gate pays for itself. The seed compile-centric indicator misses what this gate layer predicts should move, gate-record completeness across releases, sweep catch rate, rejections found at review rather than in production, and waiver health, the ratio of recorded to unrecorded local-convention departures.

**Recommended default and causal basis.** Tag the three event streams as they occur and review the metrics quarterly beside escaped-defect counts. Each metric tests one file mechanism in operation, record completeness tests whether the close is real, catch rate tests whether the judgment half works, and waiver health tests whether the two-authority split survives practice.

**Operating conditions and assumptions.** Retrospectives classify escapes against the seven rejections honestly, the list is the classification rubric. Measuring this theme's closing discipline, code-reliability outcomes live with the reliability theme's metrics.

**Failure boundary and alternatives.** Ungated metrics let the close hollow out silently, batteries keep running while sweeps and records quietly stop, and the first evidence of the decay is a shipped rejection nobody can explain. Bounded alternatives and recoveries: counting green CI runs, already collected and nearly information-free, every run is green by construction at merge.

**Counterexample, gotchas, and operational comparison.** Record completeness can be gamed by templated auto-affirmation, pair the completeness number with spot-checks that evidence links actually resolve. Good: a quarter showing two layering rejections caught at sweep and zero escaped. Bad: defending the sweep with no catch data when its cost is challenged. Borderline: counting a command-gate failure as a sweep catch, wrong stream, the machine half already gets credit.

**Verification, evidence, and uncertainty.** Confirm the three metrics exist, cite real event streams, and were consumed at the last quarterly review. The alignment between the file's mechanisms and their measurable release signatures. Healthy baselines for the three metrics await the first measured quarters.

**Second-order consequence.** Sweep catch rate is the metric that justifies the whole human half, if sweeps catch nothing for quarters the either-way finding matters, either the upstream process has improved enough to retire ceremony or the sweeps have decayed into rubber stamps, the metric cannot say which but forces the question.

**Revision decision.** Add the three metrics with collection points, release audits for completeness, retrospective classification for catch rate, and review sampling for waiver records.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: compile attempts and review comments decrease because the API shape is explicit before implementation.
Failure signal: the reference hides ownership or error tradeoffs behind generic guidance.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what must be confirmed before this gate reference is declared faithful. The seed shape items never audit fidelity to the mapped file's countable content, seven sections, five selective conventions, five implementation conventions, five runtime gates, four required and two optional commands, six checklist items, seven rejections, and five rules not to universalize.

**Recommended default and causal basis.** Run the count-and-token audit at every reread cycle and after any archive change touching the bundle. This theme's claims transcribe an enumerable source, so completeness reduces to counting the enumerables and diffing the command block, whose exact flags are the payload most damaged by paraphrase.

**Operating conditions and assumptions.** The 202604 file remains at its path for line-level comparison. Auditing this reference document against its source, auditing live gate practice belongs to the metrics loop.

**Failure boundary and alternatives.** Count-passing paraphrase is the residual risk, a command row reworded without all-features keeps the count at four while ungating the feature matrix, drift invisible to any counter. Bounded alternatives and recoveries: checksumming the mapped file and re-auditing on change only, efficient, blind to drift introduced by this document's own future edits.

**Counterexample, gotchas, and operational comparison.** Auditing from memory rather than the open file is the standing corpus failure mode, at 74 source lines this file is the cheapest full-reread in the rust cluster, leaving no excuse. Good: an audit catching a dropped all-targets flag in a transcribed command. Bad: declaring fidelity because all 26 headings exist. Borderline: accepting reworded checklist prose, tolerable, the six-item count and each item's testable subject must survive.

**Verification, evidence, and uncertainty.** Count the enumerables and diff both command blocks token by token against the live mapped file. The fully enumerable structure of the 74-line mapped file read in full. Whether token-level auditing needs corpus tooling remains open.

**Second-order consequence.** The command blocks deserve token-level treatment because they are executable, every other section survives paraphrase with meaning intact, but a gate command is its own specification, one dropped token changes what the gate verifies.

**Revision decision.** Add the count items and a verbatim check on the two command blocks, flags compared token by token, each audit cycle.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Rust Conventions Quality Gates.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send a gate-flavored question this theme does not own. The seed token-split rows point nowhere while this theme's real neighbors are exact, the rust-coder reliability theme for the full clauses behind the runtime gates, the backend themes for HTTP-specific delivery gates, the bundle's spec territory for requirement-format questions the checklist merely enforces, and the testing themes for how the tests the command gate runs should be built.

**Recommended default and causal basis.** Answer verdict questions here and forward repair questions with the owning theme named. A closing gate touches every upstream concern by construction, so this theme accumulates questions that sound like gating but are really requirement design, test construction, or pattern depth wearing gate vocabulary.

**Operating conditions and assumptions.** Destination themes exist under their expected corpus names. Sending away what this theme cannot own, destination summaries are deliberately absent.

**Failure boundary and alternatives.** Answering upstream questions from the gate file gives one-line verifications where the neighbor holds full boundaries, shallow authority substituting for deep, confident and thin. Bounded alternatives and recoveries: for cargo tooling questions no local theme covers, cargo documentation externally labeled unretrieved.

**Counterexample, gotchas, and operational comparison.** Waiver questions never leave this theme even when the waived rule is deep, the waiver mechanics, authority class, named interest, record, are gate content regardless of which rule is waived. Good: forwarding a cancel-safety design question to the reliability theme while keeping its gate verdict here. Bad: answering a requirement-format question from the checklist's one line. Borderline: a coverage-threshold tuning question, the number lives here, the philosophy of coverage gates lives with the reliability theme's clauses.

**Verification, evidence, and uncertainty.** Sample recent forwarded and kept questions against the verdict-versus-repair test. The file's compressions and imports read in full against the corpus's theme map. Misroute frequency into this theme lacks measurement.

**Second-order consequence.** The routing test for this theme is one question, is this about whether the gate passed or about how to make the work pass it, the first stays, the second always travels, the gate file owns verdicts, never repairs.

**Revision decision.** Route by depth, keep battery, checklist, waiver, and sweep mechanics here, forward pattern depth, requirement formats, suite construction, and HTTP delivery to their owners.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use backend, executable, or quality-gate Rust references when the question shifts to HTTP delivery, specs, or review gates.
Adjacent reference 1: consider the rust adjacent reference when the current task pivots away from rust conventions quality gates.
Adjacent reference 2: consider the conventions adjacent reference when the current task pivots away from rust conventions quality gates.
Adjacent reference 3: consider the quality adjacent reference when the current task pivots away from rust conventions quality gates.

## Workload Model

**Decision supported.** This section helps decide how to budget closing effort so gate cost shapes healthy batch sizes. The seed symbol-count boundary misprices gate work, whose real units are per-close cost, the fixed command-battery-plus-sweep price every handoff pays, per-waiver cost when a local convention needs a recorded departure, and per-escalation cost when risk classification triggers the advanced pair.

**Recommended default and causal basis.** Automate the battery and record, budget sweep time per close, and watch waiver and escalation counts as trend signals. Closing cost is dominated by the fixed unit, the battery runs in machine time and the sweep in bounded reviewer time, so gate workload scales with handoff frequency, not change size, small frequent changes pay the close more often than large rare ones.

**Operating conditions and assumptions.** Handoffs are discrete, continuous flows convert the fixed unit into a per-deployment-unit cost. Budgeting closing work under this theme, implementation workload lives with the reliability theme's surface units.

**Failure boundary and alternatives.** Pricing gates per symbol invites batching, teams accumulate giant changes to amortize closes, exactly backwards, large closes make sweeps shallower and defect attribution harder, the fixed cost should push toward smaller closes, not fewer. Bounded alternatives and recoveries: the seed's crate-slice and symbol boundaries, retained as outer limits on any single close's scope.

**Counterexample, gotchas, and operational comparison.** Escalations are the unit that resists automation, release tests and coverage runs cost real pipeline time, so a rising escalation rate is either honest risk growth or classification inflation, the trend needs the risk calls audited before either conclusion. Good: a team whose close automation let median change size fall by half. Bad: a quarterly mega-release closed in one heroic sweep. Borderline: batching trivial doc fixes into one close, harmless, the sweep on pure docs is near-free anyway.

**Verification, evidence, and uncertainty.** Compare close frequency and change size trends before and after battery automation. The fixed-versus-variable structure of the file's gate content read in full. Typical sweep minutes per close for a calibrated team are unestimated here.

**Second-order consequence.** Automating the fixed unit changes team behavior more than its own cost suggests, when the battery and record generation run unattended, the marginal close cost drops to sweep time alone, removing the amortization pressure that produces oversized changes, gate automation is really batch-size policy.

**Revision decision.** Restate the model in three units, fixed close cost per handoff, waiver cost per recorded departure, escalation cost per high-risk classification.

**Retained seed evidence.** The workload dimension rows with boundary values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Rust Conventions Quality Gates as a rust system operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | systems implementation, CLI or service hardening, async/runtime review, and safety-sensitive refactoring where compile success is necessary but not sufficient | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one crate or bounded workspace slice, up to 100 changed symbols, and one integration path that exercises error handling | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Rust Conventions and Gates; 1) Selective Local Conventions; 2) Implementation Conventions; 3) Runtime and Safety Gates; 4) Verification Command Gate;  | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is quality bar rubric with review blockers, lint gates, and release criteria | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which closing invariants must demonstrably hold for this theme's guidance to count as adopted. The seed document-property thresholds stand where closing invariants should, every release claim backed by a complete gate record, zero releases with a failed-or-skipped required command, every local-convention departure carrying a recorded waiver, and every high-risk close showing its advanced-gate results.

**Recommended default and causal basis.** Wire the command target into branch protection and hold the three record-based targets through release audit. Each target restates a file mechanism as an invariant, the record target operationalizes run and require success, the waiver target holds the two-authority split, and the escalation target keeps the optional pair from decaying into never.

**Operating conditions and assumptions.** Releases are identifiable events with owners, unowned releases fail the record target by construction. Closing invariants for work under this theme, code-level invariants live with the reliability theme's targets.

**Failure boundary and alternatives.** Targets held informally decay at deadlines, the first skipped sweep under pressure normalizes the second, and gate discipline is precisely the discipline that deadline pressure tests. Bounded alternatives and recoveries: trust-based closing with retrospective-only enforcement, cheaper day to day, it discovers gate decay only through the escapes the targets exist to prevent.

**Counterexample, gotchas, and operational comparison.** The waiver target measures recording, not frequency, a rising waiver count with full records is healthy visibility while a flat zero more likely means unrecorded departures than perfect compliance. Good: branch protection blocking a merge with a failed clippy check. Bad: declaring gate adoption from a quarter of green badges alone. Borderline: a hotfix bypassing the sweep under incident pressure, survivable exactly when the record says so and the sweep runs retroactively.

**Verification, evidence, and uncertainty.** Review the four target audits at each release checkpoint with evidence artifacts attached. The file's contractual wording and mechanism structure read in full. Audit sampling rates that catch decay early are team-calibrated.

**Second-order consequence.** The command target is the only one enforceable purely by machine, branch protection requiring the four checks makes skipping structurally impossible, so wiring it first converts the most deadline-vulnerable target into the most deadline-proof one, exactly where the protection is needed.

**Revision decision.** Publish the four targets with evidence methods, release audit for records, CI enforcement for commands, review sampling for waivers, and record inspection for escalations.

**Retained seed evidence.** All four seed reliability rows with thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which closing-decay modes need standing probes and what each probe cross-checks. The seed generic rows miss how closing gates specifically decay, battery erosion where flags get trimmed for speed until the commands no longer verify what section 4 wrote, sweep skipping where the judgment half quietly stops running while the machine half keeps the badges green, waiver inflation where the local class expands to swallow rules that were universal, and checklist rot where affirmations become templated clicks with dead evidence links.

**Recommended default and causal basis.** Run the four cross-check probes on a quarterly audit cadence with findings attributed to their mode. All four decay toward the same attractor, a close that looks complete and verifies less each quarter, because every one of them preserves the visible artifacts, green badges, checked boxes, closed releases, while hollowing the verification behind them.

**Operating conditions and assumptions.** Probes are owned, an unowned probe list is this table's own failure applied to itself. Decay of this theme's closing discipline, code-level failure modes live with the reliability theme.

**Failure boundary and alternatives.** The modes are mutually masking, a green battery hides a skipped sweep, a checked checklist hides trimmed flags, so no single artifact inspection reveals the decay, only cross-checks between artifact and underlying evidence do. Bounded alternatives and recoveries: periodic full gate re-derivation from the mapped file, the reset option that all four modes eventually justify.

**Counterexample, gotchas, and operational comparison.** Battery erosion often arrives as performance engineering, dropping all-features to halve CI time is a defensible-sounding change whose review should treat the gate diff as the substantive content, not the minutes saved. Good: a quarterly diff catching all-targets dropped from the test command. Bad: trusting release records whose evidence links have been dead for two quarters. Borderline: a recorded waiver on the unwrap convention for a prototype crate, defensible individually, the quarterly class review is where the pattern gets judged.

**Verification, evidence, and uncertainty.** Confirm each failure row names its probe, owner, and cadence, and sample one probe's recent findings. The artifact-versus-evidence structure of the file's mechanisms read in full. Decay onset speed under sustained deadline pressure is unmeasured.

**Second-order consequence.** Waiver inflation is the subtlest row because it attacks the file's two-authority split itself, each individually reasonable reclassification of a universal rule as local moves the boundary, and section 7's list is the fixed reference point that makes the drift measurable, the de-universalization list doubles as the inflation gauge.

**Revision decision.** Add the four rows with cross-check probes, CI-config-versus-section-4 diffs for erosion, record audits for sweep presence, waiver-class review for inflation, and evidence-link resolution sampling for rot.

**Retained seed evidence.** All four seed failure rows with mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| runtime contention masks failure | async tasks, locks, or shared state degrade under concurrent load | add contention benchmark, timeout budget, and structured cancellation path |
| panic path reaches production | unwrap or unchecked invariant survives compile and unit tests | require panic audit, Result propagation, and integration failure fixture |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide which gate failures may rerun and what any rerun's result is allowed to mean. The seed corpus-process bullets stand where closing-gate retry doctrine should, a failed required command is a fix-forward signal, never a rerun-until-green candidate, because all four commands are deterministic on identical inputs, and any command that flakes is reporting environment debt, not test luck.

**Recommended default and causal basis.** Fail the close on any required-command failure, record the failure class in the gate record, and gate new-work starts on close health. Fmt, clippy, and build are pure functions of source and toolchain, and the test command inherits whatever determinism the suite provides, so gate retries can only launder nondeterminism that some upstream discipline, usually test isolation, has already failed to provide.

**Operating conditions and assumptions.** The pipeline distinguishes gate failures by command, aggregated pass-fail hides which discipline owes the debt. Retry semantics for this theme's gate battery, suite-level flake doctrine lives with the testing themes and code-level retry design with the reliability theme.

**Failure boundary and alternatives.** Retry-until-green on the gate teaches the team the badge lies, each laundered flake ships with a green record that certifies less than it claims, the gate equivalent of the checklist rot the failure table names. Bounded alternatives and recoveries: scheduled toolchain-update closes that absorb lint-generation changes deliberately, converting surprise drift into planned maintenance.

**Counterexample, gotchas, and operational comparison.** Clippy failures after toolchain updates look like flakes but are drift, the record's toolchain-version field is what distinguishes a new lint generation from a nondeterministic test, misclassifying drift as flake quarantines the wrong thing. Good: a red clippy close fixed forward with the new lints addressed. Bad: a merge on the third rerun of a flaky integration test. Borderline: one rerun to classify a suspected infrastructure failure, legitimate exactly when the result routes to diagnosis rather than to merge.

**Verification, evidence, and uncertainty.** Audit gate records for rerun patterns and confirm each rerun carries a classification. The deterministic character of the four required commands read from section 4. The close-failure rate that should trigger new-work backpressure is team-calibrated.

**Second-order consequence.** Backpressure at the gate is release-shaped, when closes start failing repeatedly the correct response is to stop opening new work and repay whatever debt the failures report, toolchain drift, suite flakes, feature-matrix breakage, a red gate is the system's only structural veto over more work-in-progress.

**Revision decision.** Add the gate regime, zero automatic retries on the four required commands, deterministic failures fix forward, nondeterministic failures route to the owning suite's quarantine process before the close proceeds.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what emission evidence each close must verify and what evidence the close itself must leave. The seed generic records stand beside the file's own observability gate, section 3 requires verifying no secrets or sensitive payloads are logged, the one line in the file that polices what running code emits, plus the record set the close itself needs, command outputs, risk calls, sweep verdicts, and waiver entries.

**Recommended default and causal basis.** Verify the secret-logging gate per close with grep and typed-secret checks, and generate the close record from CI plus named human entries. The close produces evidence in two directions, about the code, including the secret-logging verification, and about the close, the gate record's four blocks, and both decay independently, code telemetry through logging drift, close telemetry through record rot.

**Operating conditions and assumptions.** Secret patterns are enumerable for tooling, novel credential shapes still need the human review pass. What this theme's close must record and verify about emissions, full telemetry design lives with the reliability theme's tracing doctrine and ops themes.

**Failure boundary and alternatives.** The secret-logging gate is the highest-stakes single line in section 3, a leaked credential in logs outlives every rotation it forces, and unlike the async gates no compiler surface hints at the violation, only review and tooling see it. Bounded alternatives and recoveries: typed-secret wrappers per the reliability theme's secrecy doctrine, upstream prevention that shrinks what this gate must catch, complement, not substitute.

**Counterexample, gotchas, and operational comparison.** Debug and error paths are where payload dumps hide, the crash handler that prints the whole request is invisible in happy-path review and exactly where sensitive data surfaces under incident pressure. Good: a close record showing the secret-scan output beside the four command results. Bad: a payload-dumping error handler shipped through a sweep that checked only async gates. Borderline: logging request IDs that indirectly identify users, jurisdiction-dependent, the gate record should note the call either way.

**Verification, evidence, and uncertainty.** Pick a recent close and locate both directions of evidence from its record alone. Section 3's verification list and the close's evidence structure read in full. Tool coverage for secret-pattern detection across logging styles is implementation-dependent.

**Second-order consequence.** The secret-logging gate is the only section 3 verification that gets harder as observability improves, richer logging and tracing widen the leak surface, so teams adopting the reliability theme's tracing doctrine simultaneously raise the stakes on this gate, the two themes' guidance must be adopted together or the gap grows.

**Revision decision.** Pair the two directions explicitly, run the secret-logging verification with tooling support where available, and keep the close's own four-block record as the meta-telemetry.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture error count, timeout count, retry count, saturation signal, and rollback trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide which performance statements may survive a close and in what form. The seed latency packet stands beside the checklist's sharper rule, performance claims include explicit thresholds and test method, a gate on claims rather than on speed, no number with a named measurement, no pass.

**Recommended default and causal basis.** Sweep release-bound text for performance adjectives at the checklist walk and require each to resolve to a threshold-method pair. The rule targets the failure mode where fast enough ships as an adjective, unverifiable at review and undisputable at regression time, a threshold plus method converts the claim into a test that can fail.

**Operating conditions and assumptions.** Thresholds are testable in the project's environment, aspirational numbers with no runnable method fail the gate as surely as no number. Gating performance claims at the close, benchmark construction and correctness-preserving optimization live with the reliability theme's section 6 doctrine.

**Failure boundary and alternatives.** Unthresholded performance claims are unfalsifiable at close time and unenforceable afterward, the regression that halves throughput violates no stated contract because none was stated. Bounded alternatives and recoveries: central SLO catalogs owning all performance numbers, heavier, they subsume the claim gate for services while library and CLI claims still need the checklist rule.

**Counterexample, gotchas, and operational comparison.** Thresholds imported from requirements can go stale as hardware and load change, the claim gate verifies presence and method, the threshold's continued fitness needs an owner and a revisit date. Good: a release note stating p95 under ten milliseconds on the named benchmark. Bad: significantly faster parsing shipped in the changelog. Borderline: a comparative claim, faster than the previous release, passes only when the comparison method and margin are stated.

**Verification, evidence, and uncertainty.** Sample release-bound text for performance statements and check each carries threshold and method. The checklist's performance item and the file's own inline thresholds read in full. How often stale thresholds survive fitness review is unmeasured here.

**Second-order consequence.** The claim gate also disciplines the optional coverage command's cousin problem, gates that measure must say what passing means, the file's own seventy-five percent line floor models the rule it demands, every measuring gate in the file carries its threshold inline.

**Revision decision.** Enforce the claim gate at the checklist walk, any performance statement in requirements, docs, or release notes must carry its threshold and method or be demoted to explicitly unverified.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require memory, panic, and concurrency evidence; hot-path operations need p95 under 10 ms locally or an explicit benchmark exception.
Leading indicator to measure: compile attempts and review comments decrease because the API shape is explicit before implementation.
Failure signal to watch: the reference hides ownership or error tradeoffs behind generic guidance.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what workspace count, team count, or format count this theme's close must be re-architected rather than stretched. The seed task-splitting bounds stand beside the file's real scale seams, the command gate assumes one workspace where all features build together, the checklist assumes requirements traceable in one bundle format, and the close assumes one team owning the release, each assumption breaks at a nameable size.

**Recommended default and causal basis.** Operate single-context closes as written and treat each trigger as a record-architecture event, not a workaround opportunity. Multi-workspace monorepos break the single battery invocation, cross-team releases break single-owner records, and polyglot or multi-bundle codebases break the requirement-linkage item's format assumption, the file's mechanisms are single-context by construction.

**Operating conditions and assumptions.** Contexts are visible, the second workspace added quietly inside a repo crosses the seam the day its code ships unbatteried. Bounding this theme's closing doctrine, code-level scale seams live with the reliability and backend themes.

**Failure boundary and alternatives.** Stretching a single close across contexts produces the worst artifact, one gate record signing for workspaces its commands never ran against, completeness theater at exactly the scale where verification matters most. Bounded alternatives and recoveries: org-level release trains with dedicated gate infrastructure, the heavyweight resolution the third seam eventually demands.

**Counterexample, gotchas, and operational comparison.** Feature-matrix growth is the stealth seam inside a single workspace, when features become mutually exclusive the all-features command silently stops being runnable, and the gate needs a documented matrix variant before the flag quietly disappears. Good: a monorepo release record composing three per-workspace batteries. Bad: one battery run at the repo root signing for untested workspaces. Borderline: two teams sharing one workspace and one close, workable while the sweep genuinely covers both teams' diffs.

**Verification, evidence, and uncertainty.** At each growth event, re-test the three assumptions and record which seams the event crossed. The single-context assumptions read from the file's command and checklist structure. The workspace count at which aggregate records become unmanageable is team-specific.

**Second-order consequence.** The gate record is the scaling artifact, batteries and sweeps replicate per context naturally, but the release claim needs one aggregate view, so scale design for this theme is really record design, how per-context evidence composes into one auditable release story.

**Revision decision.** Name the three seams with triggers, a second workspace triggers per-workspace batteries with an aggregate record, a second owning team triggers split closes with named interfaces, and a second requirement format triggers per-format checklist mappings.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Rust Conventions Quality Gates stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which probes reveal that this theme's gate commands or doctrine have gone stale. The seed theme-name queries would surface generic quality content while this theme's staleness lives in named places, the cargo subcommand flags section 4 fixes, the cargo-llvm-cov tool the optional gate names, clippy's evolving lint generations, and the upstream bundle's own revision state.

**Recommended default and causal basis.** Run the dry-run probe at each corpus refresh, date the result against the 202604 anchor, and check the archive for bundle revisions. Gate content ages at the toolchain's release tempo, flags deprecate, lint sets grow, coverage tooling evolves, while the file's judgment content, the rejections and boundaries, ages only with practice, so probes should track the tool layer and mostly leave the judgment layer alone.

**Operating conditions and assumptions.** Probe findings are triaged into flag-level fixes versus doctrine-level rewrites, toolchain churn is almost always the former. Refreshing this document's tooling and lineage claims, judgment-content refresh rides on upstream bundle revisions.

**Failure boundary and alternatives.** Name-based searching returns tutorials that neither confirm nor deny whether the 202604 command lines still run clean on current stable, the one operational question a refresh of this theme must answer. Bounded alternatives and recoveries: pinning the document explicitly to the 202604 toolchain and marking every command archive-dated, zero probe cost, honest, and decreasingly useful as toolchains advance.

**Counterexample, gotchas, and operational comparison.** A clean dry run does not certify the optional pair, cargo-llvm-cov is the third-party dependency whose invocation syntax has the most drift room, it needs its own dated check even when the floor passes. Good: a dated dry run confirming all four commands pass on current stable. Bad: logging that rust quality gate tutorials say nothing new. Borderline: probing new cargo subcommands for gate candidacy, adjacent and promising, findings extend the battery rather than refresh it.

**Verification, evidence, and uncertainty.** Record each probe with its date and the specific command or claim it confirmed or flagged. The tool-versus-judgment aging split read across the file's sections. Actual toolchain drift since 202604 is unknowable without the dry run.

**Second-order consequence.** This theme has the cheapest possible freshness probe in the corpus, executing its own four commands on a current toolchain against any healthy workspace, the gate content is self-testing in a way prose doctrine never is, a ten-minute dry run settles what documentation surveys only estimate.

**Revision decision.** Replace the name queries with targeted probes, a current-stable dry run of the four required commands, cargo-llvm-cov release notes since 202604, and the archive watch for a revised executable-specs bundle.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | rust conventions quality gates official documentation best practices |
| `github_repository_query_phrase` | rust conventions quality gates GitHub repository examples |
| `release_notes_query_phrase` | rust conventions quality gates changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide under what label and with what attached caveats each claim here may be reused. The seed label definitions stand without this assignment's ledger, one 74-line mapped file read fully, zero external URLs fetched, bundle siblings unread and known only through the concepts this file imports, and every closing-practice construct above marked as inference.

**Recommended default and causal basis.** Before reusing a claim, identify its stratum, cite section numbers for facts, date the command lines, and attach reasoning to inference. The fact stratum is the file's transcribable content, the section counts, the convention lists, the command lines with their flags, the checklist items, the rejections, and the de-universalization list, while the gate records, probes, targets, and close economics are this evolution's constructed machinery.

**Operating conditions and assumptions.** The archive path stays stable so fact-class claims remain mechanically checkable. Reuse rules for this document's claims, transcribed content travels with section citations, constructed machinery travels only with its reasoning.

**Failure boundary and alternatives.** The costliest mislabel would present the command lines as currently verified against modern toolchains, they are 202604 archive content, runnable then, of unknown fitness now, and the dry-run probe is the only path from archive fact to current fact. Bounded alternatives and recoveries: per-paragraph inline labels if the stratum-level split ever proves too coarse for a dispute.

**Counterexample, gotchas, and operational comparison.** The REQ-RUST-* and L1/L2/L3 mentions above are references to unread bundle definitions, reusing them as if their full semantics were established here would overclaim, this document knows they exist, not what they fully say. Good: reusing the four-command floor with its section 4 citation and archive date. Bad: citing the gate record as bundle doctrine. Borderline: reusing the two-authority thesis elsewhere, the mechanism is visible in the file, the generalization is this evolution's inference.

**Verification, evidence, and uncertainty.** Sample claims from earlier sections and confirm each declares its stratum cleanly. This assignment's read ledger, one file read in full, zero retrievals. Readers can check the citations but not the reading behind them.

**Second-order consequence.** This file's most quotable line needs its scope carried along, the de-universalization list is local corpus fact about this bundle's rules specifically, quoting it as a general principle about quality documents is inference, attractive inference, but the label must downgrade with the generalization.

**Revision decision.** Publish the strata, countable file content as local corpus fact by section number, bundle-chained concepts as by-name local references, command currency as archive-dated pending the dry run, and all practice machinery as combined-evidence inference.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
