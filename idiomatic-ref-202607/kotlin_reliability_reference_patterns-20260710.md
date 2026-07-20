# Kotlin Reliability Reference Patterns

**Decision supported.** This section helps decide whether a Kotlin change should be judged against this fifteen-pattern reliability checklist and what the checklist can and cannot certify. The seed title announces reliability patterns without the source's own premise, that reliable Kotlin comes from making ambiguity visible at the boundary and keeping the core small, non-null, typed, and cancellation-aware.

**Recommended default and causal basis.** Treat the fifteen scored KC1 patterns as the review baseline for any LLM-authored Kotlin change, applied at the boundary and the core in that order. The source declares itself a reliability checklist for LLM-authored Kotlin work rather than a tutorial, so an opening that reads like a survey misses that every one of its fifteen patterns is a checkable rule.

**Operating conditions and assumptions.** The code under review is Kotlin with JVM interop in scope and the reviewer can see boundary adapters, not just domain files. This reference operationalizes the fifteen KC1 patterns for agent use and does not extend them with new doctrine.

**Failure boundary and alternatives.** The checklist framing does not teach Kotlin from scratch, a reader without language basics needs the tutorial-shaped documentation this source explicitly declines to be. Bounded alternatives and recoveries: language tutorials for learning Kotlin, the kotlin backend entrypoint sibling for delivery workflow, or framework docs for Spring and Ktor specifics.

**Counterexample, gotchas, and operational comparison.** Casually-used ergonomics pass review while hiding Java platform types and coroutine leaks, which is the exact casual use the premise warns against. Good: a review pass walking a diff through the KC1 scoreboard. Bad: using this file to teach coroutine syntax. Borderline: applying the checklist to a pure-JVM Java adapter, useful for the interop rows only.

**Verification, evidence, and uncertainty.** Confirm a review against this reference cites specific KC1 identifiers rather than generic quality language. The local reference states its premise, its non-tutorial scope, and all fifteen identified patterns with scores. How well the checklist covers non-JVM Kotlin targets is unaddressed by the source.

**Second-order consequence.** The premise is a threat model, Kotlin's ergonomics themselves are the risk source, so the checklist exists because the language's convenience features hide exactly the failures it polices.

**Revision decision.** Open with the boundary-versus-core premise, name the four hidden hazards the source warns about, platform types, receiver confusion, coroutine leaks, and mutable domain models.

**Retained seed evidence.** The exact theme title and its reliability-patterns framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about Kotlin reliability patterns. The seed map's single local row does not say the mapped file was read in full here, 167 lines carrying fifteen scored patterns, five doctrine areas, and six review questions.

**Recommended default and causal basis.** Cite KC1 identifiers for every pattern claim and mark anything not traceable to the 167-line file as inference or candidate. Downstream claims in this document quote pattern identifiers and code shapes, so the map must record that these came from a complete read of the one mapped path, not from the skill entrypoint that references it.

**Operating conditions and assumptions.** The archive path stays valid and the KC1 numbering in the file remains unchanged. The table records provenance for this document's claims and does not inventory the surrounding skill directory.

**Failure boundary and alternatives.** The map cannot vouch for the rest of the kotlin-coder-01 skill, whose other reference files were not read in this pass. Bounded alternatives and recoveries: retrieve and date the four URLs in a refresh pass, read the sibling reference files of kotlin-coder-01, or split the table into read and unread tiers.

**Counterexample, gotchas, and operational comparison.** The external rows for kotlinlang.org and kotlinx.coroutines look authoritative for coroutine claims, but no retrieval happened and the local file is the only read evidence. Good: citing KC1-10 for the cancellation-rethrow rule. Bad: citing the kotlinx.coroutines repository for dispatcher advice nobody fetched. Borderline: attributing a paraphrased review question to the source's closing list.

**Verification, evidence, and uncertainty.** Confirm each claim in this document carries a KC1 identifier, a quoted source line, or an unretrieved marker. The mapped reference file was read in full during this evolution and its structure matches the description here. Whether the archived copy matches any live version of the kotlin-coder-01 skill was not established.

**Second-order consequence.** This theme's local evidence is unusually strong, one compact file carries the entire doctrine with stable KC1 identifiers, so nearly every claim here can cite a pattern ID instead of a page.

**Revision decision.** Keep the single local row as a read-in-full source, and downgrade all four external URLs to unretrieved candidates.

**Retained seed evidence.** All five source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/references/kotlin-reliability-reference.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://kotlinlang.org/docs/home.html | external_research_source_material | external_research_sourced_fact | primary language documentation for Kotlin idioms and type system |
| https://github.com/Kotlin/kotlinx.coroutines | external_research_source_material | external_research_sourced_fact | official coroutine library and implementation evidence |
| https://github.com/spring-guides/tut-spring-boot-kotlin | external_research_source_material | external_research_sourced_fact | Spring-maintained Kotlin web application example |
| https://ktor.io/docs/welcome.html | external_research_source_material | external_research_sourced_fact | primary Ktor server and client framework documentation |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which reliability patterns deserve review attention first when time is bounded. The seed scoreboard carries three corpus-hygiene rows while the source ships its own fifteen-row scoreboard with measured emphasis, KC1-01 at 98 down to KC1-14 at 86.

**Recommended default and causal basis.** Review changes against the KC1 scoreboard in descending score order, stopping when remaining rows cannot apply to the diff. The source's scores already rank what matters, platform-type containment, non-null domains, and structured concurrency top the list, so this section's job is transmitting that ranking rather than inventing one.

**Operating conditions and assumptions.** Reviewers use the stable KC1 identifiers so findings stay traceable across sessions. The scoreboard ranks reliability patterns for review priority and does not order implementation steps.

**Failure boundary and alternatives.** The KC1 scores express the source author's emphasis, not measured defect rates, and quoting them as empirical findings would overstate them. Bounded alternatives and recoveries: filter the fifteen rows to the diff's domain area first, adopt only the twelve rows above 87 as blocking, or rank by the five doctrine areas instead.

**Counterexample, gotchas, and operational comparison.** The two lowest-scored rows, extension-function ownership and API compatibility, are the ones agents most often skip although they bind exactly when code is a published library. Good: a review that clears KC1-01 and KC1-02 before styling notes. Bad: a review opening with scope-function nits while platform types leak. Borderline: skipping interop rows for a service with no Java callers, recorded as scoped out.

**Verification, evidence, and uncertainty.** Trace each promoted row to its scoreboard line in the source and confirm identifiers and scores match. The source's Pattern Scoreboard table lists all fifteen KC1 rows with the scores quoted here. Whether the author's score order matches this team's actual defect distribution is unmeasured.

**Second-order consequence.** The top of the scoreboard is boundary work and the bottom is polish, scores fall roughly as patterns move from the Java boundary inward to API compatibility, encoding the premise's boundary-first priority.

**Revision decision.** Point the ranking at the source scoreboard, lead with the three highest-scored patterns, KC1-01 containment at 98, KC1-02 non-null domains at 96, and KC1-09 structured concurrency at 95.

**Retained seed evidence.** All three seed scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `kotlin_reliability_reference_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local kotlin reliability material before synthesizing reference patterns recommendations. |
| `kotlin_reliability_reference_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `kotlin_reliability_reference_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single orienting claim should govern Kotlin reliability judgments. The seed thesis repeats the corpus retrieval formula instead of the source's actual thesis, ambiguity made visible at the boundary and a core kept small, non-null, typed, and cancellation-aware.

**Recommended default and causal basis.** Quote the boundary-core premise as the orienting claim with the three evidence labels kept on its clauses. The source states its premise in one quotable sentence, so the synthesis should carry that sentence's content rather than a generic load-local-first slogan.

**Operating conditions and assumptions.** The labels stay attached so the source-derived clause remains distinguishable from ecosystem inference. The thesis orients readers of this reference and does not replace the per-pattern rules.

**Failure boundary and alternatives.** A boundary-and-core thesis compresses fifteen patterns into two clauses and loses the testing and tooling doctrine that closes the source. Bounded alternatives and recoveries: quote the premise verbatim, phrase it as a two-gate review question, or split it per doctrine area.

**Counterexample, gotchas, and operational comparison.** Paraphrases tend to keep non-null and drop cancellation-aware, losing the coroutine half of the premise. Good: using the thesis to demand a parse-once boundary before domain work. Bad: quoting it as universal Kotlin community consensus. Borderline: compressing to boundary-visible, core-typed for a prompt with the cancellation clause noted.

**Verification, evidence, and uncertainty.** Check the thesis clauses against the source's premise paragraph and confirm the combined clause carries the inference label. The source premise names ambiguity at the boundary, a small non-null typed core, and cancellation awareness explicitly. Whether external Kotlin authorities phrase reliability the same way is unknown without retrieval.

**Second-order consequence.** The thesis assigns blame unusually, it treats the language's own ergonomics as the hazard, which means reliability review is about restraint in using features rather than adding machinery.

**Revision decision.** Restate the combined inference as contain ambiguity at boundaries, keep the domain core non-null and typed, preserve cancellation, and prove the risks with targeted tests and repository gates.

**Retained seed evidence.** The three labeled thesis lines with their local, external, and combined-inference structure remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `kotlin_reliability_reference_patterns` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Kotlin Reliability Reference Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which part of the local source a specific reliability question should open first. The seed map records heading signals without the file's real topology, a scoreboard, five numbered doctrine areas, API and type design, nullability and interop, coroutines and flow, testing, and tooling, plus a closing review-question list.

**Recommended default and causal basis.** Enter through the review questions for audits and through the numbered areas for design work, citing KC1 identifiers either way. A reviewer with a specific risk needs the right doctrine area fast, and the KC1 identifiers cross-cut the areas so navigation needs both the number and the section.

**Operating conditions and assumptions.** The file remains readable at the mapped path with its scoreboard and five areas intact. The map indexes the single mapped local source and does not describe the sibling files of kotlin-coder-01.

**Failure boundary and alternatives.** The topology note goes stale if the archived file is revised, and no snapshot date is recorded. Bounded alternatives and recoveries: record line anchors per doctrine area, snapshot-date the mapping, or add unread rows for the sibling reference files.

**Counterexample, gotchas, and operational comparison.** Three scoreboard rows, KC1-06, KC1-08, and KC1-13 through KC1-15, have thinner body sections than their scores suggest, so the scoreboard promises slightly more depth than the file delivers. Good: routing a lateinit question to area two. Bad: rereading the whole file for a dispatcher question area three answers. Borderline: answering a test-selection question from the review-question list alone.

**Verification, evidence, and uncertainty.** Open the mapped file and confirm the scoreboard, the five numbered areas, and the review questions appear in the described order. The mapped file was read in full, 167 lines with the topology recorded here. Whether the sibling references of kotlin-coder-01 duplicate or extend this doctrine is unknown until read.

**Second-order consequence.** The review-question list at the file's foot is a compressed re-index of the whole checklist, six questions that each point back into a doctrine area, making it the fastest entry point for review use.

**Revision decision.** Annotate the row with area routing, type-design questions to area one, interop to area two, coroutine risk to area three, test selection to area four, and gates to area five.

**Retained seed evidence.** The single local source row with its title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/references/kotlin-reliability-reference.md | Kotlin Reliability Reference | Kotlin Reliability Reference; Premise; Pattern Scoreboard; 1. Kotlin API And Type Design; 'KC1-03' Use value classes for meaningful primitive identifiers; 'KC1-04' Use sealed outcomes for closed result and state spaces | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide how much weight external rows may carry in Kotlin reliability guidance. The seed map labels the Kotlin docs, kotlinx.coroutines, the Spring Boot Kotlin guide, and Ktor docs as external facts although none was retrieved during this evolution.

**Recommended default and causal basis.** Rest all claims on the read local checklist and treat the URLs as retrieval targets for a dated refresh pass. The external-fact label promises documentary support, and this document's coroutine and interop claims rest entirely on the local checklist, not on the linked upstream projects.

**Operating conditions and assumptions.** Each row keeps a note naming which KC1 patterns its retrieval would confirm. The map catalogs candidate external references and does not certify their content or freshness.

**Failure boundary and alternatives.** Deleting the rows would discard the natural refresh channel for a doctrine coupled to evolving coroutine APIs. Bounded alternatives and recoveries: retrieve the two library URLs first, add the Kotlin coding conventions page as a candidate, or drop the framework rows to the sibling entrypoint theme.

**Counterexample, gotchas, and operational comparison.** The framework rows, Spring and Ktor, are peripheral to this checklist, which is framework-agnostic, and citing them for reliability rules would borrow authority the source never claims. Good: naming kotlinx.coroutines as where KC1-10 semantics would be verified. Bad: asserting current dispatcher defaults from the unfetched repository. Borderline: using the Kotlin docs URL as a reading pointer labeled candidate.

**Verification, evidence, and uncertainty.** Confirm no claim cites an external row as fact and each row carries its unretrieved marker. No external retrieval was performed during this evolution, so candidate labels reflect the actual evidence state. Whether current library releases still match the checklist's coroutine claims is unknown.

**Second-order consequence.** This theme's URL list is riskier than most, cancellation and dispatcher semantics are implementation-defined by kotlinx.coroutines, so unverified claims here can silently diverge from the library's current behavior.

**Revision decision.** Downgrade all four rows to unretrieved candidates, noting the two most load-bearing for this theme, kotlinlang.org for nullability semantics and kotlinx.coroutines for cancellation behavior.

**Retained seed evidence.** All four external rows with their names, roles, and boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://kotlinlang.org/docs/home.html | Kotlin documentation | primary language documentation for Kotlin idioms and type system | external_research_sourced_fact |
| https://github.com/Kotlin/kotlinx.coroutines | Kotlin coroutines repository | official coroutine library and implementation evidence | external_research_sourced_fact |
| https://github.com/spring-guides/tut-spring-boot-kotlin | Spring Boot Kotlin guide | Spring-maintained Kotlin web application example | external_research_sourced_fact |
| https://ktor.io/docs/welcome.html | Ktor documentation | primary Ktor server and client framework documentation | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which recurring Kotlin reliability failures deserve standing detection rules. The seed registry lists corpus-hygiene failures while the source names concrete Kotlin anti-patterns with identifiers, nullable-everything fields, double-bang migration shortcuts, lateinit dependencies, GlobalScope work, and swallowed CancellationException.

**Recommended default and causal basis.** Grep diffs for double-bang, lateinit, GlobalScope, and broad catch blocks around suspend calls before any style review. The source's avoid-lists are written as greppable code smells, so the registry should carry them with their KC1 homes and detection cues.

**Operating conditions and assumptions.** Each row pairs its smell with the KC1 identifier that owns the correction. The registry names code-level anti-patterns with detection signals and does not restate full pattern doctrine.

**Failure boundary and alternatives.** Importing every avoid-bullet would duplicate the checklist, so the registry keeps the highest-silence failures. Bounded alternatives and recoveries: encode the greppable rows as detekt or lint rules where the repository supports them, fold detection into review templates, or keep a top-five registry linking into the source.

**Counterexample, gotchas, and operational comparison.** A broad catch that logs and continues looks like defensive coding while it silently breaks cooperative cancellation, the source requires the rethrow-first shape. Good: a review catching a catch-all that fails to rethrow cancellation. Bad: double-bang accepted as a migration shortcut into production. Borderline: lateinit inside a lifecycle-managed framework bean, which the source explicitly tolerates.

**Verification, evidence, and uncertainty.** Replay each registry row against its KC1 rule and confirm the detection signal is checkable pre-merge. The source's avoid-lists name every added row, including the lateinit lifecycle exception quoted here. Relative production frequency of each anti-pattern in this team's code is unmeasured.

**Second-order consequence.** The deadliest rows are the polite ones, swallowed CancellationException and suspend-wrapped blocking both compile, pass unit tests, and fail only under cancellation or load, which is why the source demands they be caught by reading.

**Revision decision.** Add rows for nullable-everything under KC1-02, double-bang and lateinit shortcuts under KC1-02, GlobalScope request work under KC1-09, swallowed cancellation under KC1-10, and suspend-labeled blocking under KC1-11.

**Retained seed evidence.** All three original registry rows with their causes, replacements, and detection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which gates must pass before Kotlin reliability work or this reference's guidance is trusted. The seed gate names the corpus verifier while the source prescribes repository-native gates, gradlew test, build, ktlintCheck, and detekt, with mvnw test and verify as the Maven equivalents.

**Recommended default and causal basis.** Run the repository's native wrapper gates and require a matching risk test for every boundary the diff touches. The source's tooling area says prefer repository-native gates and lists six commands, so this theme's operative verification is those wrappers plus risk-targeted tests.

**Operating conditions and assumptions.** The repository exposes Gradle or Maven wrappers and its static-analysis baseline is preserved per the source's tooling rule. The gate set defines what must pass before Kotlin reliability work is trusted and does not design the tests themselves.

**Failure boundary and alternatives.** The wrapper gates prove compilation and style, not the boundary risks, which need the area-four test list, cancellation, nullability, and serialization boundary tests. Bounded alternatives and recoveries: property tests for parsers where a property stack exists, serialization round-trip suites for external contracts, or adapter tests with Java fakes for interop boundaries.

**Counterexample, gotchas, and operational comparison.** The source binds gates to preservation, existing Kotlin version, JVM target, and analysis baseline stay unless the task explicitly changes them, so a gate fixed by loosening the baseline is a violation. Good: a diff shipping with detekt clean and a cancellation test for its new suspend path. Bad: completion claimed on gradlew build alone for a boundary change. Borderline: skipping ktlintCheck in a repository that never configured it, noted explicitly.

**Verification, evidence, and uncertainty.** Execute the wrapper gates in a sample repository and confirm boundary diffs are rejected without matching risk tests. The source's tooling area lists all six commands and the preservation rule quoted here. How to enforce the risk-test pairing mechanically across repositories is unresolved by the source.

**Second-order consequence.** The source splits proof into two layers, gates catch regressions mechanically while the high-value test list targets the risks gates cannot see, so a green build alone never certifies reliability here.

**Revision decision.** Keep the corpus verifier and add the six repository-native commands, paired with a risk-test check that boundary changes carry boundary tests.

**Retained seed evidence.** The original verification gate line and its repository verifier command block remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when a working agent should open this reference and which doctrine area it should enter through. The seed guide keys usage to theme mentions instead of the acts that trigger this checklist, authoring Kotlin, wrapping Java, adding suspend paths, or reviewing LLM-written Kotlin.

**Recommended default and causal basis.** Open this reference whenever agent-authored Kotlin is about to be committed and walk the diff against the applicable KC1 rows. The source names its audience directly, a reliability checklist for LLM-authored Kotlin work, so the natural trigger is any moment agent-written Kotlin heads toward review or merge.

**Operating conditions and assumptions.** The diff's risk areas can be named, boundary, domain typing, coroutines, tests, or tooling, before rows are selected. The guide routes readers into this reference and does not schedule the review itself.

**Failure boundary and alternatives.** Keying to every Kotlin mention would drag the checklist into tutorials and syntax questions the source declines to serve. Bounded alternatives and recoveries: the sibling backend entrypoint for delivery workflow questions, language docs for syntax, or a compressed top-five row check for trivial diffs.

**Counterexample, gotchas, and operational comparison.** Agents apply the checklist only to new files and skip modified adapters, where platform-type leaks most often enter. Good: a self-review walking a new Java adapter through KC1-01 and KC1-12. Bad: opening the checklist to answer what a data class is. Borderline: applying only the coroutine rows to a pure-refactor diff, recorded as scoped.

**Verification, evidence, and uncertainty.** Walk one authorship and one review scenario through the guide and confirm each lands on the intended doctrine area. The source's premise names LLM-authored Kotlin work as the audience and its areas partition the entry points. How often trivial diffs justify the full fifteen-row walk is a judgment the source does not quantify.

**Second-order consequence.** The checklist is most valuable applied to the author's own output before handoff, self-review against KC1 rows catches the ergonomics traps at the moment they are cheapest to fix.

**Revision decision.** Trigger on Kotlin authorship and review events, route boundary work to areas one and two, coroutine work to area three, and audits to the review-question list.

**Retained seed evidence.** The original usage line and all four guidance bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide what end-to-end shape a reliable Kotlin change should take. The seed scenario shows a builder picking a pattern and stops before the journey this checklist scripts, parse at the boundary, type the core, preserve cancellation, test the risk, and pass the native gates.

**Recommended default and causal basis.** Narrate a payment-decision endpoint taken from raw Java client values to a sealed PaymentDecision domain with cancellation-tested suspend calls. The checklist's value shows in sequence, each doctrine area gates the next, so the journey should walk one change through all five areas rather than end at selection.

**Operating conditions and assumptions.** The repository's boundary adapters are identifiable and its test stack can express cancellation tests. The scenario dramatizes one representative journey and does not enumerate every pattern.

**Failure boundary and alternatives.** One linear journey cannot cover both authorship and audit uses, whose entry points differ. Bounded alternatives and recoveries: a second journey for auditing an existing service, a failure journey where a swallowed cancellation surfaces under load, or the source's PaymentDecision example expanded.

**Counterexample, gotchas, and operational comparison.** Journeys skipping the interop beat read clean while the real leak, a platform type assigned to a non-null field, sits in the adapter the story never visited. Good: a journey ending with risk tests named per boundary. Bad: one ending when the code compiles. Borderline: a hotfix journey that defers the property tests and says so.

**Verification, evidence, and uncertainty.** Check each journey beat against the five doctrine areas and confirm none is skipped silently. The source's five areas and its PaymentDecision sealed-interface example script exactly this sequence. Typical time cost of the full five-area walk per change is unmeasured.

**Second-order consequence.** The journey's pivotal beat is the parse-once moment, once raw input becomes typed non-null values at the boundary, every later KC1 rule gets simpler because ambiguity stops traveling.

**Revision decision.** Extend the journey through a Java-integration feature, platform types contained at the adapter, a sealed outcome replacing boolean flow, a cancellation-safe retry wrapper, risk tests, and green native gates.

**Retained seed evidence.** The role-based opening, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Kotlin backend builder is starting from a service, route, or worker that must become production-safe and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `kotlin_reliability_reference_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the smallest reliable backend pattern that preserves coroutine, framework, and operational discipline.
Reference opening trigger: Open this file when the task mentions kotlin reliability reference patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how an agent chooses which reliability rules bind for a given Kotlin change and what being wrong costs. The seed guide keys adopt, adapt, and avoid to generic evidence agreement instead of this theme's variables, boundary exposure, consumer language, coroutine involvement, and whether invariants can live in constructors.

**Recommended default and causal basis.** Bind every KC1 row whose risk surface appears in the diff and record scoped-out rows with the reason. The checklist's rules bind conditionally, interop rows only matter with Java consumers and coroutine rows only with suspend paths, so adoption is a per-diff scoping decision.

**Operating conditions and assumptions.** The diff's boundary, consumer, and concurrency surfaces are identifiable before rows are waived. The guide calibrates which KC1 rows bind for a given change and cannot waive rows that do bind.

**Failure boundary and alternatives.** Scoping can become an excuse, a diff judged boundary-free often still touches an adapter transitively. Bounded alternatives and recoveries: default to the full fifteen rows when scoping is doubtful, escalate ambiguous ownership boundaries to the user, or pilot with the six review questions.

**Counterexample, gotchas, and operational comparison.** Being wrong here ships silent hazards, an unscoped interop row means a platform type reaches production data paths where old malformed data makes double-bang fail. Good: binding interop rows for a diff that touches a Java SDK wrapper. Bad: waiving coroutine rows because the diff only adds one suspend call. Borderline: an intentionally blocking service kept blocking with the tradeoff named, which KC1-11 permits.

**Verification, evidence, and uncertainty.** Audit recent reviews for scoped-out rows and check each waiver names its absent risk surface. The source's own exception clauses for lateinit, supervisorScope, and intentional blocking anchor the adapt tier. How often transitive boundary exposure defeats scoping judgments is unmeasured.

**Second-order consequence.** The source pre-negotiates its own exceptions, lateinit in lifecycle frameworks, supervisorScope for intentional independent failure, intentionally-blocking APIs, so adapting is quoting the source, not overriding it.

**Revision decision.** Rekey adopt to rows whose risk surface the diff touches, adapt to lifecycle-managed exceptions the source itself names, and avoid to applying the checklist as tutorial material.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the kotlin reliability reference patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong kotlin reliability reference patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which local file outranks which when Kotlin guidance conflicts or runs out. The seed hierarchy names one canonical source with a thin-corpus warning without noting this theme's adjacency, the kotlin backend entrypoint reference in this corpus routes its reliability depth here.

**Recommended default and causal basis.** Consult this checklist for code-shape questions, the entrypoint reference for workflow and stance questions, and mark anything beyond both as unread. Two Kotlin themes now exist in this corpus with a deliberate division, workflow and stance in the entrypoint, code-level reliability doctrine here, so the hierarchy should record the division.

**Operating conditions and assumptions.** Both files remain present in the corpus and the division of labor stays as recorded. The hierarchy ranks local retrieval priority for this theme and does not merge the two Kotlin themes.

**Failure boundary and alternatives.** Cross-referencing the sibling cannot substitute for this theme's own thin external corroboration. Bounded alternatives and recoveries: a follow-up pass reading kotlin-coder-01's sibling files, folding the division note into routing only, or leaving the single-row hierarchy untouched.

**Counterexample, gotchas, and operational comparison.** The testing doctrine overlaps, the entrypoint mandates gates while this checklist selects risk tests, and conflating the two layers double-counts or drops test obligations. Good: sending a when-to-spec question to the entrypoint and a null-handling question here. Bad: quoting this checklist for mode-selection rules it never carries. Borderline: answering a gate question from either file, since both list the wrapper commands.

**Verification, evidence, and uncertainty.** Confirm both Kotlin references exist in the corpus and their recorded division of labor matches their content. The source checklist carries code doctrine while the previously evolved entrypoint reference carries the mode workflow, as recorded in this corpus. Whether future Kotlin themes will redraw this division is unknown.

**Second-order consequence.** The corpus now mirrors the source skill's own split, entrypoint-plus-references, so hierarchy questions can be answered by asking whether the question is about when to act or how code should look.

**Revision decision.** Keep the mapped checklist canonical, record the sibling entrypoint as the adjacent workflow authority, and note the unread sibling files of kotlin-coder-01 as a discovery surface.

**Retained seed evidence.** The classification vocabulary line, the confidence warning, and the single hierarchy row with its reviewer question remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/kotlin-coder-01/references/kotlin-reliability-reference.md | canonical primary source | Kotlin Reliability Reference; Premise; Pattern Scoreboard | What guidance, warning, or example should this source contribute to Kotlin Reliability Reference Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete evidence object must exist before this reference counts as operational. The seed artifact names a request lifecycle diagram while this theme's operational artifact is a completed KC1 review record, the diff walked row by row with findings tied to identifiers.

**Recommended default and causal basis.** Carry one filled review record for a representative boundary-touching diff as the reviewable instance. The source is a checklist, so its evidence of use is a filled checklist, findings keyed to KC1 identifiers with the six review questions answered.

**Operating conditions and assumptions.** The record names its diff, distinguishes bound from scoped-out rows, and attaches gate outcomes. The artifact certifies this reference is operational and does not grade the reviewed code's business logic.

**Failure boundary and alternatives.** A full fifteen-row record for every trivial diff is ceremony, so the record needs the scoped-out convention from the tradeoff guide. Bounded alternatives and recoveries: a compressed six-question record for small diffs, the record embedded in the PR description, or a lifecycle diagram kept as a design attachment.

**Counterexample, gotchas, and operational comparison.** Records filled after merge look identical to pre-merge reviews, so the record should carry its timestamp relative to the merge. Good: a record with two KC1-01 findings and their fixes. Bad: a review saying looks idiomatic with no identifiers. Borderline: a record with all rows scoped out for a docs-only diff, kept as a null instance.

**Verification, evidence, and uncertainty.** Check the artifact keys every finding to a KC1 identifier and answers all six review questions. The source's stable identifiers and closing question list define exactly the record shape described. Whether identifier-keyed review records measurably improve later audits is untested here.

**Second-order consequence.** Identifier-keyed findings make review quality auditable later, a finding that cites KC1-01 can be re-checked against the rule, while prose findings decay into opinion.

**Revision decision.** Define the artifact as one completed review record, the diff identifier, bound and scoped-out KC1 rows, per-row findings, the six review questions answered, and the gate results.

**Retained seed evidence.** The artifact definition line and the three artifact field rows with completion rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: reference freshness workflow with canonical source policy and update checklist.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Kotlin Reliability Reference Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which code behaviors should be taught as exemplary, negligent, or conditionally acceptable. The seed examples restate corpus verdicts and never grade code against the checklist, a contained boundary, a leaking platform type, or a tolerated lifecycle exception.

**Recommended default and causal basis.** Grade examples by two questions, does ambiguity stop at the boundary and does cancellation survive every wrapper. The source teaches through code shapes, value classes, sealed interfaces, rethrow-first catches, so graded examples should be code-shaped too.

**Operating conditions and assumptions.** Each example names its KC1 identifiers and the production consequence of the graded behavior. The examples grade conformance to the checklist, not overall service quality.

**Failure boundary and alternatives.** Examples graded on one pattern each cannot show interactions, like a sealed outcome undermined by a nullable-everything payload. Bounded alternatives and recoveries: draw examples from this repository's actual adapters, add a fourth case for a value-class parse factory, or grade the source's own PaymentDecision snippet.

**Counterexample, gotchas, and operational comparison.** Verdicts drift when examples cite patterns loosely, the borderline lateinit case is only acceptable inside lifecycle-managed frameworks, a nuance easily dropped. Good: an adapter converting Java returns to typed Kotlin immediately per KC1-01. Bad: a catch-all retry helper that never rethrows cancellation. Borderline: lateinit for a framework-injected dependency, cited with the source's lifecycle clause.

**Verification, evidence, and uncertainty.** Scan each verdict against its cited KC1 rule and confirm the graded behavior is visible in a code diff. The source's avoid-lists and its rethrow-first code sample anchor all three recast verdicts. Which negligent shape dominates this team's real diffs is unmeasured.

**Second-order consequence.** The strongest bad example is the helpful-looking one, a retry wrapper that logs all exceptions is defensive coding on its face and a cancellation leak in fact, matching KC1-10's exact warning.

**Revision decision.** Recast good as a parse-once adapter feeding a sealed domain, bad as a broad catch swallowing CancellationException inside a retry helper, and borderline as lateinit in a lifecycle-managed bean, tolerated by the source.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Kotlin Reliability Reference Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Kotlin Reliability Reference Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Kotlin Reliability Reference Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising review practice or this reference. The seed metrics name lead time and generic signals without this theme's observables, KC1 findings per review, anti-pattern grep hits per diff, and cancellation-test coverage on suspend paths.

**Recommended default and causal basis.** Track per review the bound rows, findings by identifier, and whether boundary diffs shipped with risk tests. The checklist improves outcomes by catching named smells pre-merge, so its instruments must count identifier-keyed findings and the risk tests that pin them down.

**Operating conditions and assumptions.** Reviews record their findings with KC1 identifiers as the artifact section requires. The metrics gauge checklist effectiveness, not service uptime, which belongs to operations doctrine.

**Failure boundary and alternatives.** Finding counts reward nitpicking if not paired with severity, fifteen KC1-08 style notes can outnumber one production-relevant KC1-01 leak. Bounded alternatives and recoveries: sampled deep audits instead of full counting, defect postmortems tagged to KC1 rows, or lint-rule hit rates where rules exist.

**Counterexample, gotchas, and operational comparison.** A falling finding count is ambiguous, it can mean cleaner code or lazier review, so grep trends serve as the independent check. Good: tightening adapter review after two KC1-01 leaks in a month. Bad: celebrating zero findings while grep shows rising double-bang counts. Borderline: skipping metrics in a period with no Kotlin diffs, noted.

**Verification, evidence, and uncertainty.** Compute the grep trends on recent history and reconcile them against recorded review findings. The seed's lead-time indicator and guessed-behavior failure signal anchor the loop these counters extend. Healthy baselines for findings-per-review are unmeasured, so first thresholds are provisional.

**Second-order consequence.** Grep trends are this theme's cheapest telemetry, double-bang, lateinit, and GlobalScope counts are computable from history without any review process at all.

**Revision decision.** Adopt findings-per-review keyed by identifier, double-bang and GlobalScope grep trends, and the fraction of suspend-path diffs carrying cancellation tests as primary signals.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: lead time from requirement to verified endpoint stays under one focused implementation session.
Failure signal: framework choice or coroutine behavior is guessed instead of verified with tests and docs.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared ready to hand to an agent. The seed checklist confirms generic sections exist and never checks this document's specific obligations, all fifteen KC1 identifiers represented, the five doctrine areas covered, and the source's exception clauses preserved.

**Recommended default and causal basis.** Tick structural items with citations, then grep this document for each KC1 identifier and each exception clause. This document transmits a checklist, so its readiness check must confirm the inner checklist survived transmission intact, identifiers, scores, and exceptions included.

**Operating conditions and assumptions.** Each added item names its target and whether a script or human verifies it. The checklist gates this document's readiness, not the quality of code later reviewed under it.

**Failure boundary and alternatives.** A reference that dropped the lateinit lifecycle exception would still pass a section-presence check while teaching a stricter rule than the source holds. Bounded alternatives and recoveries: generate coverage items mechanically from the source scoreboard, deep-check three random rows per review, or pair-review the artifact record.

**Counterexample, gotchas, and operational comparison.** Identifier presence can pass while a row's meaning inverted, so fidelity ticks need a spot-read, not just a grep. Good: a fidelity tick quoting the lateinit clause verbatim. Bad: all ticks green from a headings glance. Borderline: carrying forward last cycle's identifier tick with a staleness note.

**Verification, evidence, and uncertainty.** Grep this document for the fifteen identifiers and the exception clauses, then spot-read two rows against the source. The seed's seven structural items map onto real sections here and anchor the added fidelity layer. How much spot-reading each cycle needs depends on edit volume, so depth stays judgment.

**Second-order consequence.** Fidelity beats coverage here, the costly transcription error is not a missing row but a rule quoted stricter or looser than the source wrote it.

**Revision decision.** Append items requiring all fifteen KC1 identifiers present, the five areas named, the six review questions reachable, and the three exception clauses preserved.

**Retained seed evidence.** All seven structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Kotlin Reliability Reference Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a question should leave this reference and which neighbor owns it. The seed routing splits the theme name into keywords aimed at unnamed destinations instead of routing to this corpus's real Kotlin neighbor and its skill-authoring references.

**Recommended default and causal basis.** Answer code-shape questions here, send when-to-act and what-to-return questions to the entrypoint, and record genuinely unowned questions as gaps. Readers leave this checklist with two distinct needs, delivery workflow and stance questions, owned by the kotlin backend entrypoint reference, and deeper skill-structure questions owned by authoring references.

**Operating conditions and assumptions.** Each route names its trigger, a destination resolving to a real file, and what stays here. Routing redirects within this corpus and cannot authorize work in a destination's domain.

**Failure boundary and alternatives.** Keyword routes point at references that exist only as words, stranding the reader who follows them. Bounded alternatives and recoveries: consult the corpus index before adding routes, keep unresolved needs here with a gap note, or escalate genuine overlap to the user.

**Counterexample, gotchas, and operational comparison.** Testing questions sit on the seam, gate selection belongs to both files while risk-test selection belongs here, and the split should be stated when routing. Good: sending a which-mode question to the entrypoint reference. Bad: routing to the reliability adjacent reference, a keyword with no file. Borderline: answering a gate question inline while noting the entrypoint carries the same commands.

**Verification, evidence, and uncertainty.** Resolve each named destination to an existing corpus file and walk one sample question through each trigger. The kotlin backend entrypoint reference was evolved in this corpus immediately before this file and records the reciprocal route. The best inline-versus-route split for seam questions stays recorded judgment.

**Second-order consequence.** The two Kotlin references form a closed loop, the entrypoint routes reliability depth here and this file routes workflow back, so most Kotlin questions resolve without leaving the pair.

**Revision decision.** Route workflow, mode, and stance questions to the kotlin backend entrypoint reference and keep code-shape, interop, and coroutine doctrine here.

**Retained seed evidence.** The adjacency guidance line and the three keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use runtime, security, or testing Kotlin references when the question is about day-two operation, abuse cases, or fixtures.
Adjacent reference 1: consider the kotlin adjacent reference when the current task pivots away from kotlin reliability reference patterns.
Adjacent reference 2: consider the reliability adjacent reference when the current task pivots away from kotlin reliability reference patterns.
Adjacent reference 3: consider the reference adjacent reference when the current task pivots away from kotlin reliability reference patterns.

## Workload Model

**Decision supported.** This section helps decide how much Kotlin review work one change may consume before splitting or escalation. The seed model bounds endpoints per batch but not this theme's working unit, one diff walked against the bound KC1 rows in one focused review.

**Recommended default and causal basis.** Scope rows per diff, split reviews when a diff touches more than a handful of distinct boundaries, and keep one verification owner per record. The costly unit here is an oversized diff, a review spanning many boundaries cannot hold all fifteen rows in attention and starts skimming exactly the rows that matter.

**Operating conditions and assumptions.** Diffs are scoped before review and boundary touches are countable from the change set. The model bounds review effort per change and does not bound service capacity.

**Failure boundary and alternatives.** Diff-sized budgeting varies with density, a fifty-line adapter can carry more boundary risk than a five-hundred-line rename. Bounded alternatives and recoveries: time-boxed reviews with explicit unfinished-row handoffs, per-area sub-reviews for large changes, or reviewer-set boundary budgets.

**Counterexample, gotchas, and operational comparison.** Refactors tempt unbounded scope, a rename sweeping thirty files hides the one adapter edit that needed the full interop walk. Good: a large feature split into an adapter review and a domain review. Bad: one record covering three services' worth of diffs. Borderline: a two-boundary diff kept whole with both boundaries named.

**Verification, evidence, and uncertainty.** Count boundary touches and bound rows in recorded reviews and test whether single-boundary reviews close in one focused session. The seed's bounded capacity row sets the per-batch ceilings this revision keys the review unit to. Typical boundary-touch counts per diff are unmeasured, so the split threshold stays monitored judgment.

**Second-order consequence.** Boundary touches are the natural splitting currency, each touched adapter or new suspend path multiplies the rows that bind, so counting them prices the review before it starts.

**Revision decision.** Rebound the model around one diff per review record, bound rows fixed at scoping, and boundary-touch count as the size signal that triggers splitting.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Kotlin Reliability Reference Patterns as a documentation reference operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | reference selection, writing, roadmap, or explanation work where the output should improve the next human or agent decision | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one audience, one decision, up to 12 source documents, and one verification checklist per reference use | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Kotlin Reliability Reference; Premise; Pattern Scoreboard; 1. Kotlin API And Type Design; 'KC1-03' Use value classes for meaningful primitive identifi | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is reference freshness workflow with canonical source policy and update checklist | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must demonstrate before its guidance is trusted. The seed table demands perfect boundary preservation and an 18-of-20 decision sample with no procedure, and omits this theme's own checkable targets, zero unreviewed boundary diffs and zero swallowed cancellations reaching merge.

**Recommended default and causal basis.** Keep the four seed dimensions with methods attached and lead with the two binary scans per merge window. The source's rules are binary at the diff level, a platform type either escapes or not, cancellation either rethrows or not, so targets here can be pass-fail rather than sampled percentages.

**Operating conditions and assumptions.** Each target names its metric, scan method, population, owner, and the corrective action a miss triggers. The targets judge this reference and the review discipline, not the runtime reliability of reviewed services.

**Failure boundary and alternatives.** Quoting the unmeasured seed percentages as achieved performance manufactures rigor this corpus never earned. Bounded alternatives and recoveries: lint-rule enforcement where the repository supports it, sampled deep audits for the non-greppable rows, or postmortems on every escape instead of rates.

**Counterexample, gotchas, and operational comparison.** The cancellation scan needs syntax awareness, a broad catch is fine when a rethrow-first clause precedes it, so naive greps overcount. Good: a merge-window scan showing zero unrecorded boundary diffs. Bad: reporting the 18-of-20 nobody sampled. Borderline: a scan with two false-positive catch hits, resolved by reading.

**Verification, evidence, and uncertainty.** Run both binary scans over one merge window and record hits with their resolutions. The source's rethrow-first sample and boundary rules give the operational definitions the added targets scan for. No baseline exists for any threshold here, so the first measured window defines what is achievable.

**Second-order consequence.** Binary targets dodge the sampling problem the seed's percentages create, a greppable invariant needs no sample size, only a scan.

**Revision decision.** Add binary targets, every boundary-touching diff carries a review record and no merged diff contains an unrethrown broad catch around suspend work, each marked unbaselined and owned.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failures in the reliability-review fabric deserve standing mitigations. The seed table carries hygiene and traffic rows and omits how reliability review itself fails, rows skimmed on big diffs, exceptions misremembered stricter than written, greps trusted without reading, and scores mistaken for measurements.

**Recommended default and causal basis.** Detect skimming by records with no findings on boundary diffs, drift by findings contradicting source clauses, grep-trust by unresolved scan hits, and literalism by scores quoted as data. Triage during a bad review needs rows describing how the checklist's application decayed, ranked by how silently each failure ships defects.

**Operating conditions and assumptions.** Each row names its trigger, earliest observable signal, blast radius, containment, and correction. The table covers review-process failures, while code-level failures belong to the anti-pattern registry.

**Failure boundary and alternatives.** Rows are worthless if their earliest signal fires only after a production incident. Bounded alternatives and recoveries: wire record checks into review templates, sample-audit zero-finding records, or require clause citations on blocking findings.

**Counterexample, gotchas, and operational comparison.** Zero-finding records look like clean code and often mean unread diffs, the ambiguity the metrics section's grep trends exist to break. Good: an audit catching a blocking finding that contradicts the source's supervisorScope clause. Bad: a boundary diff merged with a zero-finding record nobody audited. Borderline: mild skimming on a rename-only diff, accepted with the scope noted.

**Verification, evidence, and uncertainty.** Seed one failure per row in a drill and confirm the named signal fires before a simulated merge. The source's exception clauses and scoreboard are the referents these failure rows protect. Observed frequency of each review failure in this team's history is unmeasured.

**Second-order consequence.** Exception-drift is the subtle one, a reviewer who forgets the lateinit lifecycle clause starts blocking legitimate framework code, and overstrict review erodes trust in the whole checklist.

**Revision decision.** Add row-skimming, exception-drift, grep-trust, and score-literalism rows with pre-merge detection signals.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| decision path remains implicit | reader cannot tell when to adopt, adapt, or avoid the pattern | add decision table, cost of being wrong, and adjacent-reference route |
| large corpus becomes list | many sources are indexed but not synthesized into ranked guidance | classify canonical, supporting, legacy, duplicate, and conflicting sources |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failing operation, in reviewed code or in reference work, should be retried, redesigned, or escalated. The seed bullets classify verification failures generically and never carry this theme's retry-specific rule, any retry layer around suspend work must preserve cancellation.

**Recommended default and causal basis.** For code, require the rethrow-first shape in every retry helper, and for reference work, keep the seed's one-bounded-retry-then-escalate rule. The source singles out retry, logging, and error-normalization layers as the places cancellation gets swallowed, so retry guidance here is first about exception transparency.

**Operating conditions and assumptions.** Retry helpers around suspend work are identifiable in diffs and their catch clauses readable. This governs both retrying reference-verification work and the retry code shapes this checklist reviews, kept as two labeled layers.

**Failure boundary and alternatives.** The cancellation rule governs coroutine retries, and applying it to documentation-verification retries would be a category error kept separate here. Bounded alternatives and recoveries: backoff utilities from the coroutine library once verified, sealed-result mapping with an explicit cancellation branch, or escalation to redesign when retries mask non-idempotent work.

**Counterexample, gotchas, and operational comparison.** Error-normalization layers that map exceptions to sealed results swallow cancellation just as easily as retry loops, the source names both. Good: a retry helper whose first catch clause rethrows cancellation. Bad: a normalization layer mapping all throwables to a failure result. Borderline: one bounded verification rerun after a stale-evidence refresh, per the seed rule.

**Verification, evidence, and uncertainty.** Audit retry-bearing diffs for the rethrow-first shape and check verification reruns stayed within the bounded-retry rule. The source's KC1-10 section names retry, logging, and error-normalization layers as the cancellation hazards. How often existing helpers in this team's code violate the rethrow-first shape is unmeasured.

**Second-order consequence.** Retries are where two KC1 rules intersect, a retry helper is simultaneously a broad-catch risk under KC1-10 and a blocking risk under KC1-11, making it the highest-density review target in coroutine code.

**Revision decision.** Add the code-layer rule, every retry wrapper rethrows CancellationException before any broad catch, alongside the seed's documentation-layer retry bullets.

**Retained seed evidence.** All five retry and backpressure bullets, including the one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence must exist that a reliability review happened as claimed. The seed bullets recycle generic evidence records and never name this theme's evidence stream, the KC1 review record, the grep-trend counters, and the risk-test inventory per boundary.

**Recommended default and causal basis.** Record per review the bound rows, findings, scope-out reasons, and gate results, keeping raw transcripts out per the seed's small-evidence preference. The artifact section defines the review record and the metrics section defines the counters, so observability here means persisting those two streams next to the diffs they describe.

**Operating conditions and assumptions.** Reviews can persist small text records alongside the reviewed change. This covers observing review sessions, while runtime observability of reviewed services belongs to their own operations doctrine.

**Failure boundary and alternatives.** Full record retention for every diff can outgrow its value, so retention needs the null-instance convention for trivial diffs. Bounded alternatives and recoveries: embed records in PR descriptions, retain only records plus counter snapshots, or sample-audit records instead of keeping all.

**Counterexample, gotchas, and operational comparison.** Records that paraphrase findings lose the identifier keys, and unkeyed findings cannot be re-audited against the source rules later. Good: a PR carrying its record with two findings and one scope-out reason. Bad: a merged adapter change with no record at all. Borderline: a null-instance record for a docs-only diff, kept for the trend line.

**Verification, evidence, and uncertainty.** Spot-check merged boundary diffs for accompanying records and confirm each keys findings to identifiers. The seed's small-audit-evidence preference and this file's artifact definition anchor the record-centric stream. The retention horizon for review records is untuned, so the keep-record rule is provisional.

**Second-order consequence.** Scoped-out rows are the record's most diagnostic field, they capture what the reviewer decided not to look at, which is where the next escaped defect most likely lives.

**Revision decision.** Recenter the checklist on session evidence, the identifier-keyed record, scoped-out rows with reasons, grep-counter snapshots, and the risk tests added per boundary.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove the review discipline is buying more than it costs. The seed method fixes handler latency numbers but not this theme's performance question, whether checklist-backed review catches defects faster than the incidents it prevents would cost.

**Recommended default and causal basis.** Log per review its duration, findings, and bound-row count, and publish the escape ledger with attribution evidence. The checklist's promised benefit is pre-merge capture of silent hazards, so verification must compare review cost against escaped-defect cost, not measure handler milliseconds.

**Operating conditions and assumptions.** Reviews record durations and incidents get root-caused to code shapes. This evaluates the review discipline's cost and benefit, while handler latency belongs to each service's own SLO.

**Failure boundary and alternatives.** Escaped-defect comparisons need incidents attributable to specific unreviewed rows, which sparse histories cannot provide. Bounded alternatives and recoveries: compare reviewed against unreviewed merge windows on defect counts, use grep trends alone at first, or track only the escape ledger.

**Counterexample, gotchas, and operational comparison.** Review minutes inflate when records are written retroactively, so duration belongs in the record at review time. Good: an escape ledger tracing an incident to a skipped KC1-11 row. Bad: quoting handler latency as proof the checklist works. Borderline: an early cost ratio published with a sample-of-three caveat.

**Verification, evidence, and uncertainty.** Collect review durations and escape attributions across a merge window and publish the comparison with its sample size. The seed's performance method line makes the latency numbers conditional on an absent service-specific SLO. Actual defect-capture rates for checklist-backed review are absent from this corpus.

**Second-order consequence.** The cheapest benefit signal is asymmetric, one production cancellation leak traced to an unreviewed retry helper outweighs months of review minutes, so even a single attributed escape justifies the discipline.

**Revision decision.** Measure review minutes per record, findings caught pre-merge versus defects escaped, and grep-counter direction, keeping the seed's latency defaults as the absent-SLO fallback they are.

**Retained seed evidence.** The performance method line, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require the reader to find the correct next action in 10 minutes or less during review sampling.
Leading indicator to measure: lead time from requirement to verified endpoint stays under one focused implementation session.
Failure signal to watch: framework choice or coroutine behavior is guessed instead of verified with tests and docs.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what scale this checklist stops sufficing and what structure replaces it. The seed statement recites multi-system limits and misses this theme's scale walls, codebases too large for manual row walks, coroutine semantics that shift under library releases, and Kotlin targets beyond the JVM the checklist never addresses.

**Recommended default and causal basis.** Walk rows manually while volume permits, mechanize the greppable rows as volume grows, and re-verify coroutine rows after major library releases. The checklist scales by mechanization, its greppable rows can become lint rules while its judgment rows cannot, so the growth path is splitting the fifteen rows by automatability.

**Operating conditions and assumptions.** Lint infrastructure exists for mechanization and library release events are noticed. The boundaries bound this reference and its review discipline, not the size of systems Kotlin can serve.

**Failure boundary and alternatives.** Mechanized rules drift from source intent when encoded loosely, a naive double-bang lint flags test fixtures the doctrine never targeted. Bounded alternatives and recoveries: adopt existing detekt rulesets before writing custom rules, scope the checklist to JVM modules explicitly, or split a multiplatform variant when needed.

**Counterexample, gotchas, and operational comparison.** Multiplatform code invalidates the interop rows silently, KC1-01 and KC1-12 assume a Java boundary that non-JVM targets do not have. Good: double-bang and GlobalScope rows encoded as lint at high diff volume. Bad: stretching interop rows over a Kotlin/JS module. Borderline: a custom lint rule with known false positives, kept with a triage note.

**Verification, evidence, and uncertainty.** Track review backlog against diff volume and confirm coroutine rows are re-checked after each major library release. The source's greppable avoid-lists and judgment-based rows exhibit exactly the split the mechanization path follows. The diff volume at which manual walks break down is unmeasured for this team.

**Second-order consequence.** The fifteen rows split naturally at scale, roughly the greppable half mechanizes into lint while boundary judgment, receiver clarity, and API compatibility stay human, defining the automation frontier.

**Revision decision.** Add scale signals, diff volume exceeding manual review capacity, kotlinx.coroutines releases changing cancellation semantics, and non-JVM targets where interop rows lose meaning.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Kotlin Reliability Reference Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would genuinely refresh this reference's external evidence. The seed query table drops the internal theme name into three templates whose literal phrasing targets a coinage no external author uses.

**Recommended default and causal basis.** Search the coroutine changelog and the language conventions on a periodic trigger, feeding the coroutine rows and the external map. Useful refresh queries speak the ecosystem's vocabulary, Kotlin coding conventions, coroutine cancellation best practices, kotlinx.coroutines release notes, not this corpus's file-naming scheme.

**Operating conditions and assumptions.** Each query names its target rows, source type, and firing trigger. The queries refresh external analogues for this theme, while the local checklist changes only through repository edits.

**Failure boundary and alternatives.** Empty results from a coinage query logged as freshness confirmed convert search blindness into false confidence. Bounded alternatives and recoveries: follow the four candidate URLs directly once retrieval is authorized, track the Kotlin blog, or drive refresh from dated retrieval records.

**Counterexample, gotchas, and operational comparison.** Kotlin search results skew toward Android lifecycle content, whose cancellation advice differs from server-side doctrine in exactly the rows this file cares about. Good: a kotlinx.coroutines changelog query feeding the KC1-10 row. Bad: searching the literal theme title and logging zero hits as freshness. Borderline: adopting a well-argued practitioner post on scope functions with an inference label.

**Verification, evidence, and uncertainty.** Run each query once, grade the top results for server-side relevance, and rewrite phrasings that return mostly Android noise. The seed's three-row structure targeting docs, repositories, and release notes is sound scaffolding for the revised vocabulary. Which phrasings will track this vocabulary is unknowable in advance, so the queries need their own review cadence.

**Second-order consequence.** This theme's most perishable rows are the coroutine trio, KC1-09 through KC1-11 track a library that still evolves its cancellation and dispatcher semantics, so the changelog query outranks the others.

**Revision decision.** Rephrase toward ecosystem vocabulary, Kotlin coding conventions updates, kotlinx.coroutines changelog, cancellation and structured concurrency guidance, and Kotlin binary-compatibility tooling, each tied to the rows it refreshes.

**Retained seed evidence.** All three labeled query rows with their official-docs, repository, and release-notes targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | kotlin reliability reference patterns official documentation best practices |
| `github_repository_query_phrase` | kotlin reliability reference patterns GitHub repository examples |
| `release_notes_query_phrase` | kotlin reliability reference patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how statements in this reference must be labeled so readers know what each claim rests on and how fresh it is. The seed notes define the three labels but ignore this file's specific hazards, checklist scores that read like measurements and coroutine claims coupled to an evolving library nobody re-verified.

**Recommended default and causal basis.** Label per claim, cite KC1 identifiers for rules, flag scores as emphasis, and keep all four external URLs as unretrieved candidates. Downstream confidence calibrates on these labels, and a score of 98 quoted without its author-emphasis caveat reads as empirical data it never was.

**Operating conditions and assumptions.** Labels stay stable corpus-wide and every combined-inference clause names the inputs it merges. The notes govern labeling in this reference and its reuses, not source ranking, which the hierarchy owns.

**Failure boundary and alternatives.** Labels applied per section rather than per claim let one labeled sentence launder its unlabeled neighbors. Bounded alternatives and recoveries: an explicit emphasis-value tag for scores, inline labels parenthetically on key claims, or claim-to-label indexing during verification.

**Counterexample, gotchas, and operational comparison.** Packet and prompt reuse strips labels mechanically, so load-bearing claims need labels embedded in their own sentences. Good: the rethrow-first rule cited as read local fact under KC1-10. Bad: the 98 score quoted as measured defect impact. Borderline: a coroutine claim labeled local fact with a library-version caveat attached.

**Verification, evidence, and uncertainty.** Sample load-bearing claims, confirm correct labels, and verify no score is quoted without its emphasis caveat. The three seed definitions match the corpus-wide label vocabulary and the score table's undocumented methodology motivates the emphasis rule. Label durability through packet reuse and prompt quotation is unaudited, so leakage risk remains an assumption.

**Second-order consequence.** This theme's local label needs a sub-grade, rule versus emphasis, because the source mixes normative rules with numeric emphasis and the two decay differently, rules by revision and scores by opinion.

**Revision decision.** Add rules marking KC1 scores as author-assigned emphasis, dating coroutine-semantics claims against library versions, and keeping URL-derived material as inference pending retrieval.

**Retained seed evidence.** All three label definitions, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
