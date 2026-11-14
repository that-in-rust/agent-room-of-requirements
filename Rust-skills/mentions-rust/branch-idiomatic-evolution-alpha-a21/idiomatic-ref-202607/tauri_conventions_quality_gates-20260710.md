# Tauri Conventions Quality Gates

**Decision supported.** This section helps decide how to frame a terminal gate file that bounds its own authority. The seed no seed line states what this theme's source actually is, an 83-line end-of-work gate file inside the tauri-executable-specs-01 skill, self-described for use near the end of planning, implementation, or review, carrying seven numbered sections that move from selective conventions through implementation rules, runtime safety verifications, a four-command cargo gate, a release checklist, rejected anti-patterns, and a closing list of rules explicitly forbidden from universalization.

**Recommended default and causal basis.** Apply the file at the end of Tauri work as a gate, never as a starting design guide. The skill factors its Tauri knowledge into a routing map, a playbook, a doctrine, and this gate file, and every read order in the map ends here, making the file the final checkpoint that all Tauri work passes regardless of entry mode.

**Operating conditions and assumptions.** The file remains at its single archive path inside the skill's references directory. This reference covers the gate file, the sibling doctrine and playbook files belong to their own corpus themes.

**Failure boundary and alternatives.** Reading it as general Tauri guidance misses its position, it assumes the doctrine and playbook already shaped the work and only checks that delivery-blocking properties hold at the end. Bounded alternatives and recoveries: the sibling doctrine theme for pattern-level Tauri design, this theme owns the delivery gate.

**Counterexample, gotchas, and operational comparison.** The file's checklist bans unfinished-work placeholder markers in finalized code, a rule this corpus's own contract happens to share, do not confuse the two mandates. Good: citing the gate with its end-of-work timing intact. Bad: quoting four-word naming as a universal Tauri rule the file itself refuses. Borderline: applying the cargo gate to a non-Tauri Rust repo, sound commands, wrong provenance, cite the Rust quality theme instead.

**Verification, evidence, and uncertainty.** Confirm the seven numbered headings before structural claims. The full 83-line read plus skill spine and routing map this session. The skill's upstream authorship and testing history are unrecorded.

**Second-order consequence.** The file is unusual for policing itself, section 7 lists its own conventions among rules not to universalize, four-word naming yields to API compatibility and Mermaid stays project-conditional, a gate file that ships with the boundaries of its own authority is rare in this corpus.

**Revision decision.** Open with the file's terminal-gate position, its seven-section anatomy, and the self-limiting design of its final section.

**Retained seed evidence.** The exact theme title and framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide what the effective evidence set and its internal contract are. The seed one local row names the gate file without recording its evidence context, the file exists only at this single path, md5 616924c0864e092e9fdd60df050df832 with no duplicate anywhere in the repository, and it lives inside a four-file reference set whose routing map assigns it the final position in all eight task-type read orders.

**Recommended default and causal basis.** Cite gate rules from this file and their justifications from the doctrine theme's coverage. The mapping row's role label, reference detail file for deeper pattern evidence, understates the file, it is not detail but the terminal gate the skill's own map routes everything through.

**Operating conditions and assumptions.** The skill directory structure survives future sweeps intact. Provenance for this theme's claims, the sibling files are context evidence here and primary evidence in their own themes.

**Failure boundary and alternatives.** Synthesizing without the directory context would miss that the file deliberately omits pattern rationale, the doctrine's twenty-nine patterns carry the why while this file carries only the final what-must-hold. Bounded alternatives and recoveries: retrieving upstream Tauri 2 documentation to first-source the rules, outside this evolution's local scope.

**Counterexample, gotchas, and operational comparison.** The routing map's read-orders reference doctrine patterns by number, Pattern 1 through Pattern 29, those numbers are stable citation anchors only while the doctrine file stays unedited. Good: citing the no-lock-across-await gate here and its reasoning to the doctrine theme. Bad: treating this file as the skill's complete Tauri knowledge. Borderline: quoting the SKILL.md mode list in this theme, legitimate boundary context, not gate content.

**Verification, evidence, and uncertainty.** Re-run the single-copy checksum check at each audit. Checksum sweep and full directory reads from this session. Whether future sweeps will archive newer revisions of the skill.

**Second-order consequence.** The four-file factoring gives each document a verifiable contract, the map routes, the playbook specifies, the doctrine justifies, and this file gates, so citing gate rules for their rationale is a category error the skill's own architecture warns against, the rationale citation belongs to the doctrine theme.

**Revision decision.** Annotate the row with the single-copy checksum, the terminal-gate role from the routing map, and the deliberate rationale-elsewhere design.

**Retained seed evidence.** The one local row and three external rows with their column values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/tauri-executable-specs-01/references/tauri-conventions-and-gates.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://v2.tauri.app/ | external_research_source_material | external_research_sourced_fact | primary Tauri 2 application and security documentation |
| https://github.com/tauri-apps/tauri | external_research_source_material | external_research_sourced_fact | desktop runtime implementation and release surface |
| https://github.com/rust-lang/api-guidelines | external_research_source_material | external_research_sourced_fact | Rust-facing API and error design reference |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which gate rules deserve default-tier ranking on this evidence. The seed three corpus-process rows stand where the gate file's own priorities rank, the least-privilege family leads, capabilities scoped by real window label, filesystem, plugin, and sidecar permissions scoped exactly, appearing in conventions, safety gates, checklist, and anti-patterns alike, then the async safety pair, no blocking work in async command contexts and no lock guard across await, then the serializable error surface, Result with AppError and no unwrap or expect in user-reachable paths.

**Recommended default and causal basis.** Treat verify-no rules as unconditional gates and feasibility-phrased rules as selective conventions. Rules that recur across the file's sections are the ones its authors gated redundantly on purpose, least privilege appears four times because permission breadth is the desktop platform's highest-consequence failure.

**Operating conditions and assumptions.** Recurrence reflects this one file's structure, not a survey of Tauri practice. Ranking the gate file's rules by internal recurrence and conditionality, corpus-process patterns rank in the seed rows.

**Failure boundary and alternatives.** Ranking by section order would put naming conventions above security gates, inverting the file's own emphasis, section 1 is explicitly selective while section 3's verifications are unconditional. Bounded alternatives and recoveries: the seed's process-tier scoreboard for corpus workflow ranking.

**Counterexample, gotchas, and operational comparison.** The async-mutex exception is easy to flatten, lock guards may cross await only where the chosen async mutex model explicitly requires it, a conditional inside an otherwise absolute gate. Good: ranking exact permission scoping first with its four appearances cited. Bad: ranking four-word naming as a top gate. Borderline: ranking the plugin-store size rule mid-tier, single appearance, but phrased as an unconditional keep.

**Verification, evidence, and uncertainty.** Spot-check recurrence counts against the seven sections at audit. The full gate file read this session. Real-world violation frequency of each rule is not in the file.

**Second-order consequence.** The file encodes priority through grammar, its highest rules are phrased as verify-no statements about absent hazards while its lowest are phrased as use-when-feasible preferences, so conditionality of phrasing is a machine-checkable proxy for how binding each rule is.

**Revision decision.** Present the recurrence-ranked core, least privilege, async safety, error serializability, with each rule's section appearances counted.

**Retained seed evidence.** The three scored seed rows with tier labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `tauri_conventions_quality_gates` | 95 | default_adoption_pattern_tier | Source Map First: Load local tauri conventions material before synthesizing quality gates recommendations. |
| `tauri_conventions_quality_gates` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `tauri_conventions_quality_gates` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what standard separates deliverable Tauri work from merely compiling work. The seed generic corpus formulas stand where the file's thesis is legible in its structure, Tauri delivery quality is gated on desktop-specific hazards, capability breadth, async-runtime misuse, unserializable panics, sidecar supervision, rather than on generic Rust virtue, and section 7 makes the point explicit by rejecting generic Rust guidance that weakens Tauri-specific security choices.

**Recommended default and causal basis.** Gate Tauri work on the desktop-specific verifications first and treat generic quality tooling as necessary but insufficient. A Tauri app is a web frontend holding OS-level power through IPC, so its characteristic failures are boundary failures, over-granted permissions, blocked runtimes, and panicking command surfaces, which generic Rust linting does not see.

**Operating conditions and assumptions.** The project is a Tauri 2 application per the skill's stated scope. The thesis governs Tauri delivery gating, generic Rust quality doctrine lives in its own corpus themes.

**Failure boundary and alternatives.** Gating Tauri work on cargo checks alone passes builds that ship broad filesystem grants and unwraps in command paths, the exact anti-patterns the file's section 6 rejects. Bounded alternatives and recoveries: one-size Rust quality gating, exactly what section 6's second anti-pattern rejects.

**Counterexample, gotchas, and operational comparison.** The thesis does not license skipping the cargo gate, section 4 requires it fully, the claim is insufficiency, not irrelevance. Good: failing a review for a broad shell permission despite green cargo gates. Bad: waiving capability review because clippy passed. Borderline: applying the four-word naming convention in a fresh codebase, allowed as selective, never as a gate.

**Verification, evidence, and uncertainty.** Audit gate decisions for desktop-hazard checks beyond tool output. Sections 3, 6, and 7 read this session. How the thesis extends to Tauri versions beyond the archive's Tauri 2 frame.

**Second-order consequence.** The file's deepest move is bidirectional boundary defense, section 6 rejects generic rules overriding Tauri security while section 7 forbids exporting Tauri-local conventions outward, guarding against both import and export of misfit doctrine, a symmetry most convention documents lack.

**Revision decision.** State the desktop-boundary thesis with section 7's anti-universalization clause as its sharpest expression.

**Retained seed evidence.** The three labeled thesis statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `tauri_conventions_quality_gates` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Tauri Conventions Quality Gates comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide where in the skill's read order this theme's file sits and why. The seed heading signals list the file's sections while the working map is its position in the skill, the reference-map routes every one of eight task types through this file last, the SKILL.md spine names five modes that all terminate here, and the sibling doctrine and playbook carry the pattern rationale and spec machinery this file deliberately omits.

**Recommended default and causal basis.** Enter Tauri questions through the routing logic and reach this file at the end, quoting it as the closing check. The skill's default read order is map, playbook, relevant doctrine sections, then this file, so navigation within the theme means knowing what upstream files already handled before the gate applies.

**Operating conditions and assumptions.** The four-file set stays co-located so the routing references resolve. Navigation of this theme's file within its four-file reference set, sibling content belongs to adjacent themes.

**Failure boundary and alternatives.** Treating the gate file as an entry point produces rule application without rationale, the file compresses each rule to one line precisely because the doctrine holds the explanation. Bounded alternatives and recoveries: reading the gate file standalone, workable for pure review passes per the map's Review Mode ordering.

**Counterexample, gotchas, and operational comparison.** The routing map's heading-search commands use rg on relative paths, they assume execution from the skill root, not from the repository root. Good: a review pass reading doctrine non-negotiables then closing with this gate. Bad: starting greenfield planning from the gate file's conventions. Borderline: using section 4's commands as a quick health check mid-implementation, early use of a terminal gate, harmless and sometimes wise.

**Verification, evidence, and uncertainty.** Trace navigation claims to the routing map's tables at review. The map, spine, and gate file read in full this session. None about structure, the reference set was enumerated and read.

**Second-order consequence.** The routing map turns the gate file into the skill's only unconditional dependency, modes and doctrine sections vary per task but the gate is invariant, so any Tauri output from this skill family that lacks gate evidence is procedurally incomplete regardless of which mode produced it.

**Revision decision.** Annotate the map with the terminal position, the default read order, and the per-task-type routing that always closes on this file.

**Retained seed evidence.** The one local source row with title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/tauri-executable-specs-01/references/tauri-conventions-and-gates.md | Tauri Conventions and Gates | Tauri Conventions and Gates; 1) Selective Local Conventions; 2) Tauri Implementation Conventions; 3) Runtime and Safety Gates; 4) Verification Command Gate; 5) Release Readiness Checklist | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide which external claims this theme owns and how they decay. The seed three inherited agent-format anchors stand while the file's real external surface is the Tauri 2 platform itself, capabilities and window labels, plugin-store, channels and binary responses, sidecar packaging declarations, updater trust boundaries, plus the cargo and pnpm toolchains its command gate invokes, all archive-dated to the 202604 snapshot.

**Recommended default and causal basis.** Reuse gate intents as stable and their named mechanisms with archive-dated labels, following the file's own hedge. Gate rules name platform mechanisms, so each rule silently depends on that mechanism's continued shape, capability scoping syntax, channel APIs, and store plugins all evolve with Tauri releases.

**Operating conditions and assumptions.** The target project's Tauri version is known when the gate is applied. External dependencies for freshness tracking, all URLs stayed unretrieved this evolution.

**Failure boundary and alternatives.** The volatile-claim risk is concrete, a future Tauri major could rename capability semantics or supersede plugin-store, leaving gate lines correct in spirit but stale in mechanism. Bounded alternatives and recoveries: the seed's inherited AGENTS.md and Actions anchors, retained for ecosystem context.

**Counterexample, gotchas, and operational comparison.** The cargo commands look timeless but the flags matter, all-targets and all-features widen the gate beyond default invocations, dropping them silently narrows the gate. Good: reusing least-privilege intent while checking current capability syntax. Bad: quoting plugin-store guidance as current for an unknown Tauri version. Borderline: substituting npm for pnpm in the gate, explicitly licensed by the file's own hedge.

**Verification, evidence, and uncertainty.** Record mechanism-currency checks alongside externally-grounded reuse. Zero fetches this assignment and the mechanism inventory from the file. Current Tauri platform state is unverified from local evidence.

**Second-order consequence.** The file hedges its own toolchain volatility deliberately, section 4 says use the repo's actual package manager and scripts rather than forcing these exact command names, encoding mechanism-over-incantation, and that hedge is the template for how all its platform references should be read.

**Revision decision.** Keep the inherited rows and add the platform-mechanism inventory, capabilities, store, channels, sidecar packaging, updater, and the two toolchains, each marked archive-quoted.

**Retained seed evidence.** All three external rows with their boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://v2.tauri.app/ | Tauri documentation | primary Tauri 2 application and security documentation | external_research_sourced_fact |
| https://github.com/tauri-apps/tauri | Tauri repository | desktop runtime implementation and release surface | external_research_sourced_fact |
| https://github.com/rust-lang/api-guidelines | Rust API Guidelines | Rust-facing API and error design reference | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which list gates which kind of review. The seed three corpus-process rows stand where the file carries two native registries, section 6 rejects seven anti-patterns, vague desktop requirements, generic rules overriding Tauri security, convenience-default broad permissions, event spam for large payloads, unsupervised sidecar spawning, panicking or opaque command surfaces, and doctrine duplication across outputs, while section 7 lists five rules whose universalization is itself the anti-pattern.

**Recommended default and causal basis.** Screen Tauri outputs against section 6 and screen any derived guidance against section 7 before publication. The two lists guard different failure directions, section 6 rejects bad work products while section 7 rejects bad rule propagation, misapplying the file's own local conventions as global law.

**Operating conditions and assumptions.** Reviewers know which list they are enforcing, the two have different objects. Tauri delivery failures from the source, corpus-process failures stay in the seed rows.

**Failure boundary and alternatives.** Merging the lists loses section 7's point, cargo clean constantly is not a bad practice to reject in code review, it is a rule to refuse admitting into doctrine at all. Bounded alternatives and recoveries: post-incident review taxonomies, downstream of what these registries prevent.

**Counterexample, gotchas, and operational comparison.** The doctrine-duplication anti-pattern applies to this corpus too, section 6's last item rejects copying doctrine into multiple outputs instead of routing through references, an instruction this reference honors by citing rather than restating the doctrine. Good: rejecting a PR granting broad filesystem access as a convenience default. Bad: adding always run cargo clean to a team's Tauri checklist. Borderline: event-based progress for a small payload stream, the anti-pattern targets spam for large payloads, judge by volume.

**Verification, evidence, and uncertainty.** Confirm registry rows cite their section and enforcement point. Sections 6 and 7 read in full this session. Relative real-world frequency of the twelve entries is not recorded.

**Second-order consequence.** Section 7 makes the file self-referentially safe, a reuser who universalizes four-word naming or Mermaid documentation violates the file while citing it, so the registry's second half functions as a tamper seal on the first half's authority.

**Revision decision.** Add both registries with their distinct enforcement points, section 6 at work review, section 7 at doctrine review.

**Retained seed evidence.** The three seed process rows with their detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which commands must pass before Tauri work is deliverable. The seed document verifier text stands where the source is itself a command gate, section 4 requires four cargo commands to succeed, fmt with check, clippy across all targets and features with warnings denied, test and build across all targets and features, plus the repo-normal frontend and Tauri checks for the changed boundary, illustratively pnpm test, build, and tauri build.

**Recommended default and causal basis.** Run both families for any changed Tauri boundary, preserving the flags exactly and mapping the frontend commands to the repo's real scripts. The two command families split the stack the way Tauri splits it, cargo gates the Rust core while the pnpm trio gates the web frontend and the bundling boundary between them.

**Operating conditions and assumptions.** The workspace builds under all features, projects with mutually exclusive features need a documented feature-matrix substitute. The source's delivery command gate, this document's own structural verification keeps the seed's retained block.

**Failure boundary and alternatives.** Running only the cargo family passes changes that break the frontend contract or the bundle, the file requires the boundary-appropriate frontend checks too, not as optional extras. Bounded alternatives and recoveries: the corpus verifier command in the seed's retained block for this document's own checks.

**Counterexample, gotchas, and operational comparison.** Requiring success is the gate's verb, a red clippy warning is a delivery blocker by definition here, not a note for later. Good: CI running the four cargo commands plus yarn equivalents mapped per the hedge. Bad: local cargo test alone standing in for the gate. Borderline: skipping pnpm tauri build for a docs-only change, defensible under the changed-boundary clause, record the reasoning.

**Verification, evidence, and uncertainty.** Check delivery records for both command families with flags intact. Section 4 read verbatim this session. Gate runtime cost on large workspaces is not addressed by the file.

**Second-order consequence.** The gate's strictness lives in its flags, all-targets pulls tests, benches, and examples into clippy and build, all-features closes the untested-feature-combination gap, and deny-warnings converts every lint into a failure, so reproducing the commands without the flags reproduces the ritual but not the gate.

**Revision decision.** State the full command set verbatim with its two-family structure and the package-manager hedge that governs the second family.

**Retained seed evidence.** The seed's document verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when and in what capacity an agent opens this file. The seed four generic bullets stand where the skill defines exact consumption, agents reach this file near the end of planning, implementation, or review per its opening line, arriving from one of five modes the spine defines, and use it in two distinct ways, as a checklist against finished work and as a selective-convention source whose section 1 rules apply only when feasible and compatibility-safe.

**Recommended default and causal basis.** Apply the file as the artifact-only closing contract for any Tauri work, whoever or whatever produced it. The file's one-line-per-rule compression is designed for end-state checking, an agent mid-design needs the doctrine's rationale while an agent closing work needs exactly this terse enforceable form.

**Operating conditions and assumptions.** The artifact is inspectable, capability files and configs included, intentions are not gate inputs. How agents consume this theme, mode selection mechanics belong to the skill-entrypoint themes.

**Failure boundary and alternatives.** The characteristic misuse is premature application, importing section 1's naming and structure conventions into early design as requirements, when the file itself marks them selective and compatibility-bounded. Bounded alternatives and recoveries: the sibling doctrine theme when the agent needs to know why a gate rule exists before arguing an exception.

**Counterexample, gotchas, and operational comparison.** Release readiness item one, requirements are executable and measurable, does reach back into spec territory, the gate checks that the playbook's contracts exist even though writing them was another phase's job. Good: a review agent walking sections 3 through 6 against a finished PR. Bad: a planning agent adopting section 1 wholesale as design requirements. Borderline: consulting section 2's async rules mid-implementation, early but harmless, the rules bind the artifact either way.

**Verification, evidence, and uncertainty.** Sample agent sessions for end-phase gate application. The opening line, spine modes, and section structure read this session. How often real sessions arrive at the gate without prior doctrine context.

**Second-order consequence.** The file works as a contract between phases, whatever mode produced the work, the gate reads only the artifact, code, capabilities, configs, and docs, never the intentions, so it functions across agent handoffs where the closing agent lacks the opening agent's context, precisely the multi-session situation this corpus serves.

**Revision decision.** Recast the section around the two consumption forms, terminal checklist and selective convention source, with the mode-arrival context from the spine.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide what a complete gate walk looks like on a real change. The seed one generic engineer stands where the natural journey is the closing reviewer, an agent or human holding a finished Tauri change, a new command with filesystem access and a sidecar, walking the gate top down, conventions honored or waived with reasons, implementation rules checked in code, safety verifications run against async paths and logs, both command families executed, the checklist ticked, and the anti-pattern lists scanned.

**Recommended default and causal basis.** Walk the sections in order and leave per-section evidence, the trail is the review. The file's section order mirrors a review's natural sweep from style through substance to mechanical verification, so the journey is simply the document applied in order to one artifact.

**Operating conditions and assumptions.** The reviewer can run the command gate, inspection-only review covers six sections and must say so. Journeys through this theme's gate, spec-writing journeys belong to the playbook's theme.

**Failure boundary and alternatives.** The journey's failure branch is checkbox theater, ticking release readiness items without artifact inspection, the file's phrasing resists this by demanding verifiable states, each REQ-TAURI has at least one linked test is checkable, felt confidence is not. Bounded alternatives and recoveries: the doctrine theme's review-mode journey for design-level rather than delivery-level review.

**Counterexample, gotchas, and operational comparison.** Sidecar changes trigger the journey's longest branch, supervision, bounded startup, permission scoping, and packaging declarations all appear in three different sections and must each be checked. Good: a review trail with a waiver note for four-word naming on a stable API plus green command logs. Bad: a ticked checklist with no linked tests behind item two. Borderline: gating a frontend-only change with sections 3 through 5 lightly applied, the changed-boundary clause supports proportionality.

**Verification, evidence, and uncertainty.** Audit review trails for per-section evidence at sampled changes. The section order and checklist phrasing read this session. Typical walk duration on real changes is unrecorded.

**Second-order consequence.** The journey produces a natural artifact trail, each section's pass leaves distinct evidence, waiver reasons, verified-absence notes, command logs, and linked tests, so a completed walk is self-documenting and a later auditor can distinguish a real gate pass from a rubber stamp by the trail alone.

**Revision decision.** Recast the scenario as the closing-review walk with its per-section evidence, waiver notes, code findings, command outputs, and checklist links.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Tauri desktop app team is starting from a frontend action that must cross into Rust commands and platform permissions and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `tauri_conventions_quality_gates` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the safest command, permission, IPC, packaging, and verification boundary.
Reference opening trigger: Open this file when the task mentions tauri conventions quality gates, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide which side wins each recurring Tauri delivery trade-off and under what condition. The seed template rows skip the trade-offs the file actually adjudicates, naming consistency versus API compatibility, resolved for compatibility when renaming is risky, permission convenience versus least privilege, resolved for exact scoping always, event simplicity versus channel plumbing, resolved by payload volume, plugin-store ease versus proper storage, resolved by data size, and strict universal rules versus project-local conventions, resolved by section 7's explicit locality markers.

**Recommended default and causal basis.** Rule for convenience only on reversible, hazard-free axes, and for strictness wherever exposure outlives the change. Each trade-off pits developer convenience against a boundary hazard, and the file rules for convenience only where no hazard exists, naming and documentation style, never where permissions, panics, or runtime health are at stake.

**Operating conditions and assumptions.** Hazard assessment reflects the desktop boundary, a web-only intuition underrates filesystem and sidecar exposure. Trade-off structure the source teaches, corpus-process trade-offs stay in the seed rows.

**Failure boundary and alternatives.** Flattening the rulings into always-strict misreads section 1, the file deliberately keeps some rules selective to preserve compatibility and avoid convention-driven breakage. Bounded alternatives and recoveries: uniform strictness doctrine, simpler to teach and explicitly not what the file encodes.

**Counterexample, gotchas, and operational comparison.** The mutex rule is a genuine trade-off, not an absolute, the narrowest mutex that fits the access pattern licenses async mutexes where the access pattern demands guards across await. Good: keeping an old command identifier while renaming internals per the compatibility ruling. Bad: a broad shell permission justified by development speed. Borderline: plugin-store holding a medium-sized document, the size boundary is unquantified, judge against the small-structured-state intent.

**Verification, evidence, and uncertainty.** Review waiver notes for reversibility-based reasoning. Sections 1, 2, and 7 read against each other this session. The file quantifies neither payload nor storage thresholds, judgment fills the gap.

**Second-order consequence.** The file's rulings sort cleanly by reversibility, freely reversible choices like naming get selective treatment while hard-to-reverse exposures like granted permissions and shipped panics get absolute gates, giving reusers a test for novel cases the file never listed, ask how costly the choice is to undo.

**Revision decision.** Add the five trade-off rows with each ruling's condition, feasibility for conventions, hazard presence for gates.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the tauri conventions quality gates pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong tauri conventions quality gates guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which file's wording governs which question class. The seed role labels rank one file against nothing while the operative hierarchy is the skill's internal one, the SKILL.md spine states the workflow, the reference map routes, the playbook owns requirement contracts, the doctrine owns pattern rationale with its non-negotiables, and this gate file owns final delivery checks, with the map's read orders as the written precedence.

**Recommended default and causal basis.** Resolve apparent gate-doctrine tension by consulting the doctrine's full pattern text through its owning theme. The skill factored authority deliberately, section 6 rejects duplicated doctrine across outputs, so each question type has exactly one owning file and overlap is a routing error rather than a precedence contest.

**Operating conditions and assumptions.** The four files remain the versions archived together at 202604. Precedence within the tauri-executable-specs-01 reference set as it bears on this theme, sibling file contents belong to their own themes.

**Failure boundary and alternatives.** Citing this gate file for pattern rationale or the doctrine for delivery commands crosses the factoring, producing answers from the wrong authority even when the content sounds plausible. Bounded alternatives and recoveries: flat authority across the four files, which section 6's anti-duplication rule was written to prevent.

**Counterexample, gotchas, and operational comparison.** The seed labels the gate file canonical primary, true within this theme, misleading across the skill where the doctrine holds the deeper authority on any why question. Good: citing the gate for the command set and the doctrine for why channels beat events. Bad: quoting the gate's one-liner as the complete lock-across-await doctrine. Borderline: citing the map's read order as authority for review sequencing, legitimate, sequencing is the map's owned question.

**Verification, evidence, and uncertainty.** Test citation targets against the ownership map at audit. The four files' self-descriptions and routing read this session. None material, the reference set is small and was fully enumerated.

**Second-order consequence.** Conflicts between the gate and the doctrine should be nearly impossible by construction, the gate compresses doctrine conclusions, so any apparent disagreement signals either a stale compression or a misread, and the resolution is checking the doctrine's fuller statement rather than picking a winner.

**Revision decision.** State the ownership map, spine for workflow, map for routing, playbook for contracts, doctrine for rationale and non-negotiables, gate for delivery checks.

**Retained seed evidence.** The hierarchy rows and the classification vocabulary remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/tauri-executable-specs-01/references/tauri-conventions-and-gates.md | canonical primary source | Tauri Conventions and Gates; 1) Selective Local Conventions; 2) Tauri Implementation Conventions | What guidance, warning, or example should this source contribute to Tauri Conventions Quality Gates? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what standing evidence makes gate passage auditable per change. The seed generic worked-example artifact misses this theme's natural object, a gate walk record, a one-page per-change form with a row per gate section holding pass, fail, or waived-with-reason, links to the command outputs of both families, the REQ-to-test mapping demanded by the checklist, and the sidecar and capability declarations inspected.

**Recommended default and causal basis.** Complete the record for every gated change and file it with the change, waivers reasoned, verifications never waived. The gate's authority comes from being checked, and a standing record form converts the file's imperative sentences into inspectable state per change, the same move the checklist itself makes for requirements.

**Operating conditions and assumptions.** The record stays lightweight enough to survive real deadlines, one page is the design bound. One record per gated Tauri change, extensible with project-specific gate rows as conventions accrete.

**Failure boundary and alternatives.** Without the record, gate passage is a memory claim, and section 5's checkbox format invites exactly the unevidenced ticking the artifact exists to prevent. Bounded alternatives and recoveries: CI-enforced command gates alone, which cover section 4 but leave the inspection sections unevidenced.

**Counterexample, gotchas, and operational comparison.** A waiver column invites scope creep, only section 1 rows may carry waivers, a waived section 3 row is a gate failure wearing a form. Good: a record with a reasoned naming waiver, green command links, and three REQ-test rows. Bad: a record with a waived no-unwrap verification. Borderline: batching records for a stack of tiny changes, acceptable if each change's boundary is named.

**Verification, evidence, and uncertainty.** Check merged Tauri changes for completed records at sampled audits. The checklist structure and conditionality split read this session. Record discipline under deadline pressure is behavioral and unproven.

**Second-order consequence.** The waiver column is where the artifact earns its keep, section 1's conventions are waivable with reasons while section 3's verifications are not, so the form's structure itself teaches the file's conditionality split to every reviewer who fills it.

**Revision decision.** Define the artifact as the seven-row gate walk record with evidence links and a waiver column governed by section 7's locality rules.

**Retained seed evidence.** The artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: quality bar rubric with review blockers, lint gates, and release criteria.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Tauri Conventions Quality Gates | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which exercises teach the gate's compressed style fastest on this evidence. The seed abstract usage lines stand where the gate file supplies concrete gate objects, the four cargo commands with their exact flags as a runnable example, the REQ-TAURI linked-test requirement as a traceability example, and the sidecar rule as a compound example, startup checks, bounded waits, explicit restart rules, and packaging declarations, four verifiable properties in one line.

**Recommended default and causal basis.** Certify understanding by unpacking the sidecar line into its four checks and stating each check's failure form. An 83-line gate file teaches by enforceable specifics rather than narratives, so its worked examples are its most concrete rules unpacked into the checks they imply.

**Operating conditions and assumptions.** Unpacking stays faithful to the line's wording, invented sub-rules must be labeled as extensions. Teaching this theme's material, fuller Tauri pattern examples belong to the doctrine theme.

**Failure boundary and alternatives.** Teaching the gate through invented scenarios risks drifting from what the file actually requires, the safest examples are its own lines expanded to their verification procedures. Bounded alternatives and recoveries: worked examples from live Tauri repositories, richer and outside this corpus's local evidence.

**Counterexample, gotchas, and operational comparison.** The drill's trap is the missing fourth element, packaging declarations live in build configuration rather than code, and unpackings that stay code-only miss it. Good: an unpacking listing supervision, bounded wait, restart policy, and bundler declaration with a failure mode each. Bad: a sidecar review checking only that the process starts. Borderline: adding a health-endpoint sub-rule to the tetrad, sensible extension, label it beyond the file.

**Verification, evidence, and uncertainty.** Grade unpackings for completeness against the source line at review. The three unpacked rules read verbatim this session. Transfer from unpacking drills to live review quality is unmeasured.

**Second-order consequence.** The sidecar line is the file's densest teaching object, one sentence encoding process supervision, timeout discipline, failure policy, and build packaging, and an agent who can enumerate its four checks from the sentence has learned the file's compression style and can unpack every other rule the same way.

**Revision decision.** Anchor the section on three unpacked rules, the command gate with flag semantics, the traceability check, and the sidecar supervision tetrad, each with its pass and fail forms.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Tauri Conventions Quality Gates after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Tauri Conventions Quality Gates as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Tauri Conventions Quality Gates only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which numbers show the gate guarding versus eroding. The seed compile-centric indicator misses the gate's own measurable surface, command gate pass rate on first attempt, waiver frequency per section 1 convention, section 3 verification findings per review, REQ-to-test coverage from the checklist, and anti-pattern detections per section 6 category, all derivable from the gate walk records.

**Recommended default and causal basis.** Track the five measures from gate records and read waiver trends by row class before reacting. A gate that is never failed is either guarding excellence or being rubber-stamped, and only trend data on findings and first-pass rates distinguishes the two.

**Operating conditions and assumptions.** Gate walk records exist consistently enough for trends, the artifact section's discipline is this loop's input. Measuring this gate's operation plus this node's own evidence series, corpus-process metrics stay in the seed lines.

**Failure boundary and alternatives.** Without the loop, gate erosion is invisible, waivers quietly spread from section 1 into section 2 territory and command flags get trimmed for speed, each step locally reasonable. Bounded alternatives and recoveries: the evaluation theme's rubric metrics for skill artifacts rather than delivery gates.

**Counterexample, gotchas, and operational comparison.** First-pass rate can be gamed by running the commands before declaring the attempt, define the measure on the first gate-recorded run. Good: a quarter of records showing naming waivers concentrated on one legacy API, prompting a local amendment. Bad: three flag-trimmed clippy runs passing unremarked. Borderline: a spike in section 3 findings after a new contributor joins, signal about onboarding, not about the gate.

**Verification, evidence, and uncertainty.** Confirm record fields feed the five series at each review cycle. The gate structure and record design established this session. No operational baseline exists, the loop starts unprimed.

**Second-order consequence.** Waiver frequency is the loop's leading indicator in both directions, rising waivers on one convention argue the convention misfits the project and should be locally amended, while waivers appearing on verification rows signal gate erosion, the same number read by row class tells opposite stories.

**Revision decision.** Adopt the five record-derived measures with waiver drift and flag integrity as the erosion alarms.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the feature can be tested across frontend, Rust command, and packaged desktop behavior.
Failure signal: the reference ignores permissions, IPC risk, or platform-specific verification.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what must be confirmed before this synthesis is declared faithful. The seed shape items never audit this theme's distinctive claims, the single-copy checksum, the seven-section inventory, the terminal-gate position per the routing map, the ownership split keeping rationale citations pointed at the doctrine theme, and the conditionality split between selective conventions and absolute verifications.

**Recommended default and causal basis.** Run all distinctive checks wholesale each cycle and date the results. The synthesis rests on structural facts about one small file and its placement in a four-file skill, and those facts are cheap to verify wholesale but fatal to citations if silently changed.

**Operating conditions and assumptions.** The source and its directory remain in the archive at their current paths. Auditing this reference against its 83-line source and its directory context, all read wholesale this session.

**Failure boundary and alternatives.** A shape-only audit passes while a sweep moves the skill directory or a reuse cites the gate for doctrine rationale, the two drifts this theme's structure invites. Bounded alternatives and recoveries: sampled auditing, strictly worse at this scale.

**Counterexample, gotchas, and operational comparison.** The routing-position check needs the sibling reference-map file, an audit that reads only the mapped source cannot verify the terminal-gate claim this synthesis leans on. Good: an audit logging checksum, seven sections, map position, and clean citation splits. Bad: declaring fidelity from seed-shape checks alone. Borderline: skipping the ownership spot check in a cycle with no new reuse, defensible, note the skip.

**Verification, evidence, and uncertainty.** Execute the distinctive items and date each result in the audit record. The claim structure of every distinctive statement in this document. Future sweep handling of the skill directory is the main structural unknown.

**Second-order consequence.** At 83 lines the source permits the corpus's cheapest full-fidelity audit, every claim in this synthesis can be re-verified against the complete source in minutes, so audit findings here should always be exhaustive and any sampling would cost more to design than wholesale checking costs to run.

**Revision decision.** Add the distinctive items, checksum run, section inventory, routing-position check, ownership-split spot check on recent citations, and conditionality labels on reused rules.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Tauri Conventions Quality Gates.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send a question arriving at the gate theme. The seed token-split rows point nowhere while this theme's neighbors are unusually close, the tauri doctrine theme owns the twenty-nine-pattern rationale this gate compresses, the playbook's spec machinery belongs with the executable-specs themes, the Rust quality-gate themes own generic cargo discipline, and the systematic debugging theme owns what happens when a gate failure needs root-cause work.

**Recommended default and causal basis.** Answer the gate question asked and hand the rationale hunger to the doctrine theme explicitly. The gate file sits atop a documented dependency stack, so most questions arriving here are really questions for a neighbor, why a rule exists goes down to doctrine, how to write the requirement goes to spec themes, and generic Rust lint policy goes sideways to Rust themes.

**Operating conditions and assumptions.** The doctrine theme completes its own evolution, until then rationale routing lands on the raw doctrine file. Sending away what this theme holds only incidentally, destination doctrine is deliberately not restated.

**Failure boundary and alternatives.** Answering why-questions from this theme's compressed lines produces rationale-free rule recitation, while routing away delivery-gate questions loses the one theme that owns the closing check. Bounded alternatives and recoveries: for upstream Tauri platform questions, nothing local, only archive-quoted mechanism names.

**Counterexample, gotchas, and operational comparison.** Generic-looking cargo questions can be Tauri-specific in disguise, deny-warnings policy is generic but the all-features flag interacts with Tauri feature-gated plugins, split such answers rather than routing whole. Good: forwarding why channels over events to the doctrine theme's pattern coverage. Bad: answering a REQ-TAURI authoring question from the gate's one checklist line. Borderline: a clippy-flag policy question, answer the gate's usage here and route project-wide lint doctrine to the Rust themes.

**Verification, evidence, and uncertainty.** Sample recent answers for verb-consistent routing. The skill's ownership factoring and corpus theme map read this session. The doctrine theme's final section grain is unknown until it evolves.

**Second-order consequence.** This theme and the imminent doctrine theme form the corpus's tightest sibling pair, compressions of the same skill's knowledge at two altitudes, so their routing discipline is the in-corpus enactment of section 6's anti-duplication rule, each altitude answered once, in its own theme.

**Revision decision.** Route by question verb, what must pass stays here, why it must pass goes to the doctrine theme, how to specify goes to spec themes, how to fix a failure goes to debugging.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use executable, doctrine, or legacy Tauri references when the task is about specs, policy, or migration.
Adjacent reference 1: consider the tauri adjacent reference when the current task pivots away from tauri conventions quality gates.
Adjacent reference 2: consider the conventions adjacent reference when the current task pivots away from tauri conventions quality gates.
Adjacent reference 3: consider the quality adjacent reference when the current task pivots away from tauri conventions quality gates.

## Workload Model

**Decision supported.** This section helps decide how to budget a theme whose cost is per-change compute plus brief judgment. The seed symbol-count boundary misprices this node's work, whose units are the sunk read, 83 source lines plus 194 directory-context lines in minutes, per-change gate walks, minutes of inspection plus the command gate's build time which dominates, per-audit wholesale checks, minutes, and the one-time record-form setup.

**Recommended default and causal basis.** Absorb section 4 into CI, budget human minutes for sections 1 through 3 and 5 through 7, and keep audits wholesale. The theme's recurring cost is the command gate's compute, all-targets all-features builds and tests on every gated change, while every human-judgment step in the walk is fast against it.

**Operating conditions and assumptions.** CI capacity exists for the full-flag commands, trimming flags to fit CI budgets is a gate change, not a savings. Budgeting this node's upkeep and the gate's per-change operation, application development time belongs to the projects.

**Failure boundary and alternatives.** Budgeting the walk without the build time makes gate estimates optimistic by an order of magnitude on large workspaces, inviting the flag-trimming erosion the metrics loop watches for. Bounded alternatives and recoveries: the seed's crate-slice and symbol boundaries, retained as outer limits on any single consultation's scope.

**Counterexample, gotchas, and operational comparison.** Pnpm tauri build is the slowest command and the most skipped, its absence is the first place erosion shows in practice. Good: CI running both command families while a reviewer spends ten minutes on the inspection sections. Bad: a reviewer hand-running four cargo commands per change on a laptop and skipping the bundle. Borderline: nightly rather than per-change tauri build runs, a documented compromise on the slowest command.

**Verification, evidence, and uncertainty.** Check gate records for command provenance and human-time proportionality. The command set's cost structure and directory line counts from this session. Actual build times vary by workspace size and are unrecorded here.

**Second-order consequence.** The gate's cost profile argues for CI absorption, the expensive unit is machine time that parallelizes and caches, while the cheap units are judgment that does not, so the economical division runs commands in CI continuously and spends the human minutes on the inspection sections, exactly the split the record form's evidence-link design assumes.

**Revision decision.** Restate the model in its four units, sunk read, per-change walk with compute-dominated cost, wholesale audit, and record setup.

**Retained seed evidence.** The workload dimension rows with boundary values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Tauri Conventions Quality Gates as a rust system operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | systems implementation, CLI or service hardening, async/runtime review, and safety-sensitive refactoring where compile success is necessary but not sufficient | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one crate or bounded workspace slice, up to 100 changed symbols, and one integration path that exercises error handling | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Tauri Conventions and Gates; 1) Selective Local Conventions; 2) Tauri Implementation Conventions; 3) Runtime and Safety Gates; 4) Verification Command | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is quality bar rubric with review blockers, lint gates, and release criteria | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which invariants must demonstrably hold for this node's claims to stay citable. The seed document-property thresholds stand where this node's invariants should, single-copy checksum stability, seven-section inventory integrity, verbatim flag preservation in every reused command, conditionality fidelity keeping selective conventions and absolute verifications in their classes, and ownership fidelity keeping rationale citations pointed at the doctrine theme.

**Recommended default and causal basis.** Hold all five invariants at wholesale-audit cadence with the flag diff weighted heaviest. Each invariant guards a distinct corruption, structure drift breaks citations, flag trimming silently narrows the gate, class confusion turns waivable style into false law or hard gates into waivable style, and ownership drift recreates the duplication the skill forbids.

**Operating conditions and assumptions.** The archive path stays stable and reuse remains observable enough to review. Invariants for this node's claims, reliability of gated applications belongs to their teams.

**Failure boundary and alternatives.** The costliest breach is class confusion in the strict-to-loose direction, a verification row treated as waivable ships panics and broad permissions under this theme's apparent blessing. Bounded alternatives and recoveries: fact-only invariants, blind to the invocation drift that matters most here.

**Counterexample, gotchas, and operational comparison.** The class-label audit must cover this reference's own sections, the conditionality split runs through every synthesis paragraph above and would erode first in paraphrased reuse. Good: an audit diffing every reused command against section 4 token by token. Bad: a derived checklist listing clippy without deny-warnings. Borderline: a reuse reordering the four cargo commands, harmless to semantics, note it and pass.

**Verification, evidence, and uncertainty.** Review the five invariant series at each corpus checkpoint with dated evidence. The claim structure established across this document. None about current truth, all five invariants were verified during this evolution.

**Second-order consequence.** Flag preservation is the invariant unique to command-gate themes, prose themes decay by paraphrase but command themes decay by invocation drift, a copied command minus all-features looks identical in a skim and gates a strictly smaller surface, so the probe must diff tokens, not impressions.

**Revision decision.** Publish the five invariants with evidence methods, checksum runs, inventory checks, flag diffs, class-label audits, and citation-target reviews.

**Retained seed evidence.** All four seed reliability rows with thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which decay modes need standing probes for a compressed command-gate theme. The seed generic rows miss how this node specifically dies, flag erosion, reused commands shedding all-targets, all-features, or deny-warnings, class inversion, selective conventions hardening into universal law in defiance of section 7 or verifications softening into waivable style, altitude collapse, gate one-liners circulating as complete doctrine, and placement drift, the gate applied early as a design guide rather than late as a check.

**Recommended default and causal basis.** Run the four probes at each audit, weighting class checks toward reuses that quote section 1 or section 3 lines. All four attack the file's design decisions, its exact invocations, its two-class rule structure, its compression contract with the doctrine, and its end-of-work timing.

**Operating conditions and assumptions.** Reuse is observable enough to probe, unobserved reuse defaults to fixed-cadence checks. Decay of this node's claims and reuse, Tauri application failures belong to the file's own registries.

**Failure boundary and alternatives.** They compound, an early-applied, flag-trimmed, universalized copy of this gate becomes a design straitjacket that still misses panics and broad permissions, worse than no gate because it spends the review budget on the wrong things. Bounded alternatives and recoveries: quotation-only reuse with section numbers, resistant to all four modes and adequate for a file this quotable.

**Counterexample, gotchas, and operational comparison.** Altitude collapse can look like helpfulness, a reuse padding gate lines with invented rationale reads better than the terse original while fabricating doctrine the real doctrine file may contradict. Good: a probe catching a CI config that dropped deny-warnings during a migration. Bad: a team wiki stating Tauri functions must have four-word names. Borderline: a reuse explaining the channel rule with plausible invented rationale, check it against the doctrine before correcting.

**Verification, evidence, and uncertainty.** Confirm each failure row names its probe and trigger point. The decay structure consolidated from this document's preceding sections. Reuse observability determines probe weighting.

**Second-order consequence.** Class inversion is the dominant risk because section 7 is the file's least quotable part, reusers excerpt rules and drop the meta-rules that bound them, so the probe should specifically check whether any reuse of section 1 content carries its feasibility conditions.

**Revision decision.** Add the four rows with probes, token diffs for flags, class-label checks for inversion, rationale-presence checks for altitude collapse, and timing checks for placement drift.

**Retained seed evidence.** All four seed failure rows with mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| runtime contention masks failure | async tasks, locks, or shared state degrade under concurrent load | add contention benchmark, timeout budget, and structured cancellation path |
| panic path reaches production | unwrap or unchecked invariant survives compile and unit tests | require panic audit, Result propagation, and integration failure fixture |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide what a gate failure is allowed to trigger. The seed corpus-process bullets stand beside what the gate implies for failure handling, a failed gate row is not retried into submission, command failures route to diagnosis and code change before rerun, verification findings route to fixes rather than waivers, and repeated failures of the same row across changes signal an upstream doctrine or training gap, not a reason to loosen the row.

**Recommended default and causal basis.** Treat every gate failure as information routed to fix, waiver-with-reason, or upstream escalation, never to silent weakening. Gates create retry pressure by design, every failure blocks a delivery someone wants shipped, so the gate's integrity depends on rules for what failure may and may not trigger, fix and rerun yes, trim and pass no.

**Operating conditions and assumptions.** Failure records exist per row, the gate walk record is this doctrine's substrate. Failure-response doctrine for this gate's operation, application-level retry engineering belongs to the system design theme.

**Failure boundary and alternatives.** The erosion path is retry-by-weakening, a red clippy run answered by allowing the lint, a failed bundle answered by skipping the command, each converting a finding into a permanent gate reduction. Bounded alternatives and recoveries: the system design theme's exponential backoff for network retries, same integrity principle, different substrate.

**Counterexample, gotchas, and operational comparison.** Flaky frontend tests create false gate failures that legitimize rerun-without-change habits, fix the flake with the debugging theme's condition-based waiting before it teaches the team to distrust the gate. Good: a repeated no-unwrap failure across three changes triggering a team error-handling session. Bad: adding an allow attribute to silence the recurring lint. Borderline: rerunning a failed bundle after only a dependency cache clear, a change of sorts, record what changed.

**Verification, evidence, and uncertainty.** Audit gate records for change-before-rerun and reasoned waivers. The gate's require-success phrasing and waiver structure read this session. Escalation thresholds for repeated failures are judgment, the file sets none.

**Second-order consequence.** The gate needs backpressure in the queueing sense, when many changes fail the same row, the correct pressure release is upstream, better patterns taught earlier in the skill's read order, not downstream loosening, mirroring how load shedding protects a service by refusing work rather than degrading correctness.

**Revision decision.** State the response rules, rerun only after a change, waive only section 1 rows with reasons, and escalate repeated same-row failures to doctrine review rather than gate adjustment.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which observability properties must hold before Tauri work passes the gate. The seed generic records stand beside the gate's own observability demands, section 3 requires verifying that no secrets or sensitive payloads are logged, section 2 pushes long-running work onto channels or binary responses whose progress is inherently observable, and sidecar supervision requires startup checks and bounded waits, which are liveness observations by definition.

**Recommended default and causal basis.** Verify log hygiene subtractively, route progress through channels, and give every sidecar a liveness check before gating a change as done. A desktop app's observability risk inverts the server case, logs live on user machines where leaked secrets persist beyond operator reach, so the gate's first logging rule is subtractive, verify absence of sensitive payloads, before any additive telemetry.

**Operating conditions and assumptions.** Reviewers can inspect actual log output paths, configuration-only review misses formatted-in secrets. Observability rules the gate enforces plus this node's own audit records, application telemetry design belongs to the doctrine and system design themes.

**Failure boundary and alternatives.** Importing server logging habits, log everything and filter later, ships user-resident files containing tokens and payloads that no log-retention policy can recall. Bounded alternatives and recoveries: the system design theme's server-side telemetry doctrine, correct for services and misfit for user-resident desktop logs.

**Counterexample, gotchas, and operational comparison.** Debug builds often log what release builds must not, the gate applies to what ships, verify the release configuration's output, not the development console. Good: a review grepping release log output for token and path patterns before passing section 3. Bad: a progress stream emitting per-row events for a million-row import. Borderline: logging a filename without its path, project-dependent sensitivity, judge against the user's exposure.

**Verification, evidence, and uncertainty.** Check gate records for evidence on all three observable surfaces. Sections 2 and 3's observability lines read this session. Platform-specific log locations and retention are outside the file's coverage.

**Second-order consequence.** The gate treats observability as a bounded resource on the desktop, event spam is rejected not just for performance but because unbounded emission is unobservable emission, a flooded event channel hides the signal it was meant to carry, aligning the payload rule with the logging rule under one economy-of-signal principle.

**Revision decision.** State the three observable surfaces the gate checks, log content hygiene, channel-based progress visibility, and sidecar liveness, each with its verification form.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture error count, timeout count, retry count, saturation signal, and rollback trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide what performance evidence the gate demands before delivery. The seed latency packet stands beside the gate's performance stance, performance is gated structurally rather than by benchmark, no blocking work in async command contexts protects runtime responsiveness, channels or binary responses for high-volume payloads protect IPC throughput, plugin-store limited to small structured state protects storage latency, and bounded sidecar waits protect startup time.

**Recommended default and causal basis.** Verify the four structural bounds at every gate walk and defer quantitative tuning to measurement after structure passes. Desktop responsiveness dies by architecture rather than by hot loops, a blocked async runtime freezes every command at once, so the gate checks the structural properties whose violation no later optimization can repair.

**Operating conditions and assumptions.** The change's data volumes are honestly estimated, structural checks need scale intent even without benchmarks. The gate's structural performance checks, quantitative budgeting method belongs to the system design theme's latency doctrine.

**Failure boundary and alternatives.** Benchmark-first performance review passes structurally doomed designs, an event-spam progress stream benchmarks fine at test volumes and collapses at user volumes. Bounded alternatives and recoveries: profiling-first review, correct for optimizing passed structures and wrong as a substitute for the structural gate.

**Counterexample, gotchas, and operational comparison.** Spawn-blocking moves work off the async runtime but does not make it fast, passing the structural check is the floor for responsiveness, not proof of it. Good: a file-import command moved to async with owned inputs and channel progress before gating. Bad: a synchronous hash computation inside an async command justified by a fast benchmark machine. Borderline: modest event-based progress for a bounded small stream, permitted by volume judgment, record the bound assumed.

**Verification, evidence, and uncertainty.** Sample gate records for all four structural checks with scale notes. Sections 2 and 3's structural performance lines read this session. Quantitative thresholds for high-volume are unquantified by the file.

**Second-order consequence.** All four checks share one shape, they bound the coupling between work volume and a shared resource, the runtime, the IPC channel, the store, the startup path, so novel performance questions at this gate reduce to asking which shared resource the change couples to unbounded work.

**Revision decision.** State the four structural checks as the performance gate, each phrased as a verifiable absence or boundedness.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require memory, panic, and concurrency evidence; hot-path operations need p95 under 10 ms locally or an explicit benchmark exception.
Leading indicator to measure: the feature can be tested across frontend, Rust command, and packaged desktop behavior.
Failure signal to watch: the reference ignores permissions, IPC risk, or platform-specific verification.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what scale this gate applies and where its authority hands off. The seed task-splitting bounds stand beside the gate's own scale limits, the file governs one Tauri 2 application boundary at a time, its checks are per-change rather than per-portfolio, its conventions are explicitly project-local per section 7, and its authority ends where the doctrine begins, at any question requiring pattern rationale or design alternatives.

**Recommended default and causal basis.** Apply the gate per change, keep additions in project-local records rather than the gate itself, and route scope growth to the doctrine. A terminal gate scales by repetition rather than by expansion, applying the same bounded checklist to every change, and the design keeps each application cheap precisely by refusing to grow the file's scope.

**Operating conditions and assumptions.** Teams resist the natural urge to append lessons learned to the gate file directly. Scale limits of this gate's application, this evolution's own task splitting keeps the seed paragraphs.

**Failure boundary and alternatives.** Scope creep is the scale failure, gate files that accrete project lore grow until walks take hours and teams route around them, the file's compression and its section 7 self-limits are the documented defense. Bounded alternatives and recoveries: portfolio-level Tauri governance, a different instrument that this per-change gate feeds but cannot replace.

**Counterexample, gotchas, and operational comparison.** Multi-window and multi-app workspaces stress the per-boundary frame, each window label and each app boundary needs its own capability review even within one gated change. Good: a team keeping its extra lint rows in the walk record template, gate file untouched. Bad: a forked gate file grown to three hundred lines of project history. Borderline: adding one org-wide security row to a local gate copy, defensible if marked local per section 7's spirit.

**Verification, evidence, and uncertainty.** At each audit, diff any local gate copies against the archive original. Section 7 and the file's compression design read this session. How the boundaries hold across very large multi-app monorepos is untested here.

**Second-order consequence.** Section 7 is a scale mechanism disguised as a caveat list, by naming which rules must not propagate it lets the gate travel across projects without dragging project-local sediment, the file stays 83 lines because its authors built the boundary that keeps additions out.

**Revision decision.** State the three boundaries, per-change application, per-project convention locality, and the rationale line where doctrine takes over.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Tauri Conventions Quality Gates stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which probes reveal decay in this node's claims and on what clocks. The seed theme-name queries would surface generic Tauri chatter while this node's staleness has exact homes, the archive file's checksum, the skill directory's integrity including the routing map this synthesis leans on, the sweep inventory that could gain newer skill revisions, and the Tauri platform mechanisms, capabilities, plugin-store, channels, sidecar packaging, whose currency only external windows can confirm.

**Recommended default and causal basis.** Run structural probes each cycle and the mechanism pass at external windows, doctrine first, gate second. The gate's judgment layer is stable while its mechanism layer tracks Tauri releases, so refresh effort belongs on the platform-mechanism inventory and the archive structure, not on re-debating gate philosophy.

**Operating conditions and assumptions.** External verification windows occur, without them mechanism claims stay strictly archive-dated. Refreshing this node's evidence and labels, live project gating needs no refresh from here.

**Failure boundary and alternatives.** Undirected refreshing would miss the quiet break that matters, a Tauri major release changing capability semantics while the gate's lines keep gating yesterday's mechanism. Bounded alternatives and recoveries: declaring the theme historical wholesale, wasteful for judgment content that decays at textbook speed.

**Counterexample, gotchas, and operational comparison.** A refreshed mechanism finding updates this synthesis's labels, never the archive file, which stays frozen as historical evidence. Good: a refresh logging checksum stability and a dated capability-syntax check against current Tauri docs. Bad: logging that Tauri quality gates searches returned nothing new. Borderline: skipping the mechanism pass when no project uses Tauri, defensible deprioritization, record it.

**Verification, evidence, and uncertainty.** Record each probe with its date and the claim it confirmed or updated. The mechanism inventory and directory structure established this session. Future sweep contents and Tauri release timing are what the probes exist to learn.

**Second-order consequence.** The sibling doctrine file doubles as a refresh bellwether, at 470 lines it names mechanisms in more detail than the gate, so when an external window opens, checking the doctrine's mechanism claims first localizes which gate lines need re-dating, the compression relationship that structures citation also structures refresh.

**Revision decision.** Replace name queries with targeted probes, checksum and directory-integrity checks, sweep scans for newer tauri-executable-specs revisions, and a dated mechanism-currency pass over the platform inventory at external windows.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | tauri conventions quality gates official documentation best practices |
| `github_repository_query_phrase` | tauri conventions quality gates GitHub repository examples |
| `release_notes_query_phrase` | tauri conventions quality gates changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide under what label, chain, and state each claim class here may be reused. The seed label definitions stand without this assignment's distinctive ledger, one 83-line source read in full, its directory context read in full including the spine and routing map, single-copy status checksum-verified, zero external URLs fetched, no Tauri application built or gated, and no gate command executed against a real workspace this session.

**Recommended default and causal basis.** Before reusing a claim, declare it structural fact, quoted doctrine, archive-dated mechanism, or designed inference, and treat unlabeled claims as inference. Gate themes split their evidence the same way conduct themes do, the rules are fully verifiable as text while their enforcement value is only demonstrable through gated deliveries this corpus has not run.

**Operating conditions and assumptions.** The source stays unedited at its path and labels persist through reuse, both watched by the established probes. Reuse rules for this document's claims, each claim travels with class, source section, and verification state.

**Failure boundary and alternatives.** The costliest mislabel would present the gate's rules as validated practice, they are one skill author's archived doctrine, coherent and self-limiting, but untested by any delivery this corpus can point to. Bounded alternatives and recoveries: executing the command gate against a sample Tauri workspace to earn the demonstrated stratum, declined for scope, queued as the natural verification upgrade.

**Counterexample, gotchas, and operational comparison.** The gate's confident imperative voice invites authority inflation, run and require success reads like tested policy, the local evidence supports only that the archive says so. Good: reusing the seven-section inventory as local fact and the sidecar tetrad as quoted doctrine. Bad: citing the gate as an industry-validated Tauri standard. Borderline: reusing the cargo commands as generically sound Rust practice, plausible on general knowledge, still archive-quoted in this corpus's terms.

**Verification, evidence, and uncertainty.** Sample claims from earlier sections and confirm each declares its class cleanly. This assignment's ledger, full reads, checksum run, zero fetches, zero executions. Enforcement value awaits real gated deliveries under these rules.

**Second-order consequence.** The file's command gate creates a rare executable stratum, unlike prose rules, section 4's commands could be run against any Rust workspace today to verify they still parse and function, an upgrade path from quoted doctrine to demonstrated mechanism that costs one CI run.

**Revision decision.** Publish the strata explicitly, file contents and directory structure as same-session local facts, gate rules as accurately-quoted archived doctrine, platform mechanisms as archive-dated references, and all extensions here, the walk record, the reversibility test, the erosion probes, as labeled inference.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
