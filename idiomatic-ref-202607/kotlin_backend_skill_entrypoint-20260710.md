# Kotlin Backend Skill Entrypoint

**Decision supported.** This section helps decide whether an incoming Kotlin backend task should enter this skill and which of its nine modes should govern the work. The seed title names the theme without stating what the entrypoint actually is, a mode-selection contract that turns vague Kotlin backend requests into decision-complete work packets before any code is written.

**Recommended default and causal basis.** Classify the backend surface, select modes from the nine-mode menu, and write executable requirements before touching implementation. The skill's first instruction is to choose one or more of nine modes before planning or coding, so an entrypoint description that skips mode selection drops the step everything downstream assumes.

**Operating conditions and assumptions.** The task is genuinely JVM backend work, the repository's existing stack is inspectable, and acceptance criteria can be extracted or drafted. This reference describes how to enter and drive the kotlin-backend-delivery skill and does not restate the framework doctrine its bundled references carry.

**Failure boundary and alternatives.** The entrypoint framing does not fit Android UI work, multiplatform client work, or generic Kotlin syntax questions, which the skill's guardrails explicitly exclude. Bounded alternatives and recoveries: generic Kotlin language references for syntax questions, dedicated Android or multiplatform guidance for client work, or a plain review checklist when no delivery is requested.

**Counterexample, gotchas, and operational comparison.** Agents jump straight to controllers or routes and let the first framework they recall overwrite the repository's actual stack, which the skill's stance rule forbids. Good: a vague endpoint request routed through Spec Mode plus Spring Boot Mode. Bad: rewriting a Ktor service in Spring because the agent knows Spring better. Borderline: a syntax question answered inline because it affects a backend boundary, noted as out-of-skill.

**Verification, evidence, and uncertainty.** Check that the transcript names the chosen modes and the preserved stack before the first code edit. The local SKILL.md defines nine modes, five default combinations, and an explicit framework-preservation rule. How often real tasks need more than two combined modes is unmeasured in this corpus.

**Second-order consequence.** The skill treats framework choice as a conservation problem, Spring Boot versus Ktor is preserved rather than decided, unless the user explicitly requests a migration.

**Revision decision.** Open by defining the entrypoint as spec-first mode selection, name the nine modes, and state the preservation rule for framework, build tool, and versions.

**Retained seed evidence.** The exact theme title and its framing as a skill entrypoint remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about the Kotlin backend entrypoint. The seed map lists one local row for SKILL.md although the skill's context strategy names seven bundled reference files that carry most of its doctrine.

**Recommended default and causal basis.** Cite SKILL.md for every mode, workflow, and guardrail claim and mark reference-file or URL-derived statements as unread or unretrieved. The SKILL.md instructs readers to load its references progressively, so a map that stops at the entrypoint under-declares the retrieval surface this theme actually depends on.

**Operating conditions and assumptions.** The archive path stays valid and the entrypoint's context-strategy list still names the same seven files. The table records provenance for this document's claims and does not certify the unread bundled references.

**Failure boundary and alternatives.** Adding all seven reference files as mapped rows would promise coverage this evolution did not perform, since only the entrypoint was read in full. Bounded alternatives and recoveries: read and map the seven bundled references in a follow-up pass, date external rows at first retrieval, or split the table into read and unread tiers.

**Counterexample, gotchas, and operational comparison.** The four external URLs look like a vetted bibliography, but nothing in this corpus records any of them being fetched. Good: citing SKILL.md for the nine-mode menu. Bad: quoting coroutine dispatcher rules as if the playbook reference had been read. Borderline: naming the reference-map file as a discovery pointer with an unread label.

**Verification, evidence, and uncertainty.** Confirm every claim in this document traces to the SKILL.md text or carries an unread or unretrieved marker. The SKILL.md context strategy enumerates seven reference files and the seed maps exactly one local path. Whether the bundled references contradict or merely elaborate the entrypoint is unknown until they are read.

**Second-order consequence.** The entrypoint is deliberately thin, it holds the mode menu and workflow while pushing doctrine into references, so mapping only SKILL.md is honest but incomplete by design.

**Revision decision.** Keep the single local row, note that seven bundled references exist as an unread discovery surface, and leave all four external URLs as unretrieved candidates.

**Retained seed evidence.** All five source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://kotlinlang.org/docs/home.html | external_research_source_material | external_research_sourced_fact | primary language documentation for Kotlin idioms and type system |
| https://github.com/Kotlin/kotlinx.coroutines | external_research_source_material | external_research_sourced_fact | official coroutine library and implementation evidence |
| https://github.com/spring-guides/tut-spring-boot-kotlin | external_research_source_material | external_research_sourced_fact | Spring-maintained Kotlin web application example |
| https://ktor.io/docs/welcome.html | external_research_source_material | external_research_sourced_fact | primary Ktor server and client framework documentation |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which entrypoint habits deserve default adoption when an agent picks up a Kotlin backend task. The seed scoreboard scores 95, 91, and 88 for corpus hygiene and never ranks the skill's own load-bearing patterns, mode selection first, executable requirements, and framework-stance preservation.

**Recommended default and causal basis.** Rank mode selection first, executable requirements second, and framework-stance preservation third. A scoreboard silent on the mode menu licenses code-first sessions, which is precisely the failure the skill's spec-first design exists to prevent.

**Operating conditions and assumptions.** Each promoted row names the concrete delivery failure it prevents, such as untestable acceptance criteria or accidental migrations. The scoreboard ranks entrypoint practices for this theme and does not rank Spring against Ktor.

**Failure boundary and alternatives.** The numeric scores were never measured in this corpus, so quoting them as findings rather than emphasis fabricates rigor. Bounded alternatives and recoveries: order rows by the skill's eight workflow steps, replace scores with a must-do flag, or keep an unnumbered tier list.

**Counterexample, gotchas, and operational comparison.** Vague-quality words like production-ready or idiomatic pass review while carrying no observable criteria, which the skill explicitly rejects. Good: a session opening with named modes and REQ identifiers. Bad: a feature built against the phrase make it production-ready. Borderline: keeping the seed's numeric scores with an editorial-only caveat.

**Verification, evidence, and uncertainty.** Trace each promoted row to the SKILL.md workflow step or guardrail that mandates it. The SKILL.md workflow steps one through three define classification, executable requirements, and stance selection in that order. Which omitted practice causes the most real delivery failures is unmeasured, so ordering encodes expected cost.

**Second-order consequence.** The three promoted practices are ordered gates, modes scope the work, requirements make it testable, and stance preservation stops the work from silently becoming a migration.

**Revision decision.** Promote mode-selection-first, WHEN-THEN-SHALL requirements, and stack preservation above the hygiene rows, marked editorial.

**Retained seed evidence.** All three scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `kotlin_backend_skill_entrypoint` | 95 | default_adoption_pattern_tier | Source Map First: Load local kotlin backend material before synthesizing skill entrypoint recommendations. |
| `kotlin_backend_skill_entrypoint` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `kotlin_backend_skill_entrypoint` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single orienting claim should govern how agents enter Kotlin backend work. The seed thesis counts one local path and repeats the load-local-first formula instead of the theme's central claim, that Kotlin backend work starts as a spec-first work packet whose modes, requirements, and stack stance are fixed before code.

**Recommended default and causal basis.** Phrase the thesis as work packet before code, with the three evidence labels kept on its clauses. The thesis is the sentence that survives quotation, and a retrieval slogan cannot stop an agent from coding before the requirements exist.

**Operating conditions and assumptions.** The labels stay attached so entrypoint rules remain distinguishable from ecosystem inference when the thesis is reused. The thesis orients how this reference is used and does not restate the mode menu the entrypoint carries.

**Failure boundary and alternatives.** A spec-first thesis over-serves trivial one-line fixes where a full work packet is ceremony. Bounded alternatives and recoveries: quote the skill's opening sentence verbatim, split the thesis per evidence label, or phrase it as a pre-code gate condition.

**Counterexample, gotchas, and operational comparison.** Paraphrases keep spec-first and drop stack preservation, licensing exactly the silent migrations the skill forbids. Good: citing the thesis to demand requirements before a new endpoint. Bad: quoting it as universal JVM consensus. Borderline: compressing it for a prompt while keeping the preserve-the-stack clause.

**Verification, evidence, and uncertainty.** Check the local clause against the SKILL.md opening and workflow text and confirm the combined clause carries the inference label. The SKILL.md opening line defines decision-complete work packets that are spec-first, Kotlin-idiomatic, framework-aware, and production-biased. Whether external Kotlin guides endorse the same spec-first ordering is unknown without retrieval.

**Second-order consequence.** The skill converts idiomatic from an adjective into a rejection rule, any unmeasurable quality word must be replaced by observable criteria before work proceeds.

**Revision decision.** Restate the combined inference as select modes, write WHEN-THEN-SHALL requirements, preserve the existing stack, then implement against quality gates.

**Retained seed evidence.** The three labeled thesis lines with their local, external, and combined-inference structure remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `kotlin_backend_skill_entrypoint` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Kotlin Backend Skill Entrypoint comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which part of the local source a specific entrypoint question should open first. The seed map records the entrypoint's heading signals but not what each part of the skill answers, modes for scoping, workflow for sequencing, output contract for deliverable shape, guardrails for exclusions, and context strategy for further reading.

**Recommended default and causal basis.** Route what-mode questions to the mode menu, how-to-proceed questions to the workflow steps, and what-to-return questions to the output contract. A reader with a concrete question needs the right section of a 129-line file, and an undifferentiated row makes them reread the whole entrypoint per question.

**Operating conditions and assumptions.** The file remains readable at the mapped archive path and its six recorded heading signals still appear. The map indexes the single mapped local source and does not summarize the unread bundled references.

**Failure boundary and alternatives.** Heading signals go stale if the archived skill is revised, and the map records no snapshot date. Bounded alternatives and recoveries: add unread rows for the seven references, record the file's line count as a staleness tripwire, or snapshot-date the mapping.

**Counterexample, gotchas, and operational comparison.** The seven referenced doctrine files sit one directory away and are easy to mistake for already-mapped sources. Good: answering a test-strategy question from workflow step seven. Bad: hunting the entrypoint for JPA entity rules it delegates to references. Borderline: quoting the rg heading-search commands as the discovery method for unread references.

**Verification, evidence, and uncertainty.** Open the file at the mapped path and confirm the six recorded heading signals appear in order. The mapped SKILL.md was read in full during this evolution, 129 lines with frontmatter, six major sections, and a references list. Whether a newer copy of this skill exists elsewhere in the repository was not established.

**Second-order consequence.** The entrypoint is itself a router, its context strategy is a seven-step reading order with rg heading-search commands, so the source map's real job is pointing at a pointer.

**Revision decision.** Annotate the row with question routing, scoping questions to Mode Selection, sequencing to Workflow, deliverable shape to Output Contract, exclusions to Guardrails, and deeper doctrine to Context Strategy.

**Retained seed evidence.** The single local source row with its title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/SKILL.md | kotlin-backend-delivery-01 | Kotlin Backend Delivery 01; Mode Selection; Workflow; Output Contract; Guardrails; Context Strategy | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide how much weight external rows may carry in Kotlin backend entrypoint guidance. The seed map presents four external rows, Kotlin docs, kotlinx.coroutines, the Spring Boot Kotlin guide, and Ktor docs, as external facts although none was retrieved during this evolution.

**Recommended default and causal basis.** Rest all current claims on the mapped local SKILL.md and treat the URLs as leads for a dated refresh pass. An external-fact label promises documentary support, and an unretrieved URL can only supply a pointer, not evidence about current framework behavior.

**Operating conditions and assumptions.** Each row keeps a role note explaining what question a future retrieval should answer. The map catalogs candidate external references for this theme and does not certify their content or freshness.

**Failure boundary and alternatives.** Dropping the rows entirely would hide the natural refresh surface for a fast-moving framework ecosystem. Bounded alternatives and recoveries: retrieve and date the four URLs in a dedicated pass, add Spring Boot release notes as a fifth candidate, or drop the table until retrieval happens.

**Counterexample, gotchas, and operational comparison.** Candidate rows quietly harden into citations when text is reused, unless the unretrieved marker sits inside the row itself. Good: citing the Ktor docs URL as where to verify plugin APIs. Bad: claiming kotlinx.coroutines endorses the skill's dispatcher rules. Borderline: using the Spring guide URL as a worked-example pointer labeled inference.

**Verification, evidence, and uncertainty.** Confirm no claim in this document cites an external row as fact and that each row carries its unretrieved marker. No external retrieval was performed during this evolution, so the candidate labels reflect the actual evidence state. Whether any URL still matches the skill's framework-version assumptions is entirely unknown.

**Second-order consequence.** The four URLs mirror the skill's two-framework stance, one language anchor, one concurrency anchor, and one anchor per preserved framework, so the bibliography encodes the preservation rule.

**Revision decision.** Downgrade all four rows to unretrieved candidates and name what each would confirm, language idioms, coroutine semantics, Spring integration shape, and Ktor server doctrine.

**Retained seed evidence.** All four external rows with their names, roles, and boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://kotlinlang.org/docs/home.html | Kotlin documentation | primary language documentation for Kotlin idioms and type system | external_research_sourced_fact |
| https://github.com/Kotlin/kotlinx.coroutines | Kotlin coroutines repository | official coroutine library and implementation evidence | external_research_sourced_fact |
| https://github.com/spring-guides/tut-spring-boot-kotlin | Spring Boot Kotlin guide | Spring-maintained Kotlin web application example | external_research_sourced_fact |
| https://ktor.io/docs/welcome.html | Ktor documentation | primary Ktor server and client framework documentation | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which recurring Kotlin backend failures deserve standing detection rules. The seed registry lists three corpus-hygiene failures and omits the anti-patterns the skill legislates against by name, GlobalScope request work, business invariants living only in Bean Validation annotations, JPA entities modeled as ideal data classes, and retries without idempotency.

**Recommended default and causal basis.** Screen every Kotlin backend change against the registry before handoff, treating any hit as a rework trigger. The SKILL.md writes seven explicit do-not guardrails because these are the failures that ship in real Kotlin services, so the registry should carry them with detection cues.

**Operating conditions and assumptions.** Each row pairs a failure with an observable signal a reviewer can grep or test for, like GlobalScope in request paths. The registry names entrypoint and delivery failures with detection signals and does not restate the full guardrail list.

**Failure boundary and alternatives.** Importing every guardrail verbatim would duplicate the skill instead of registering the highest-cost patterns with signals. Bounded alternatives and recoveries: fold detection into the completeness checklist, keep a short top-four registry linking into the guardrails, or add detekt rules where the repository supports them.

**Counterexample, gotchas, and operational comparison.** Blocking JDBC calls hidden inside suspend functions pass type checks and fail only under load, making dispatcher review a code-reading task. Good: catching a GlobalScope.launch in a request handler at review. Bad: a retry loop added to a non-idempotent payment call. Borderline: a blocking service kept intentionally blocking with the tradeoff named, which the skill permits.

**Verification, evidence, and uncertainty.** Replay each registry row against the guardrail that forbids it and confirm the detection signal is checkable pre-merge. The SKILL.md guardrails section names each added failure explicitly, including the retry, JPA, validation, and GlobalScope rules. Relative frequency of each anti-pattern in this team's services is unmeasured, so row order encodes expected cost.

**Second-order consequence.** Most guardrails police the seam between Kotlin idiom and framework machinery, code that is beautiful Kotlin can still be wrong Spring, which is why the skill forbids modeling entities as ideal data classes.

**Revision decision.** Add globalscope-request-work, annotation-only-invariants, naive-jpa-data-class, and retry-without-idempotency rows with review-time detection cues.

**Retained seed evidence.** All three original registry rows with their causes, replacements, and detection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which gates must pass before Kotlin backend work or this reference's guidance is trusted. The seed gate names one repository verifier command while the skill's real gates are the repository's own quality wrappers, gradlew test, build, detekt, and ktlintCheck, plus evidence for requirement coverage and migration safety.

**Recommended default and causal basis.** Run the corpus verifier for structure, the repository wrapper for code health, and a req-to-test traceability scan before claiming completion. The skill's workflow step eight mandates running the repository wrapper commands before handoff, so a gate set without them misses the theme's operative checks.

**Operating conditions and assumptions.** The repository exposes wrapper commands and the requirements were written with REQ-KOTLIN-BACKEND identifiers. The gate set defines what must pass before Kotlin backend work is handed off and does not implement the test strategy itself.

**Failure boundary and alternatives.** The gradle commands assume a Gradle repository, and Maven equivalents must substitute where the build tool differs. Bounded alternatives and recoveries: Testcontainers-backed suites where infrastructure behavior is in scope, migration dry-runs for schema changes, or contract tests for external clients.

**Counterexample, gotchas, and operational comparison.** Green unit tests create false confidence when persistence or messaging behavior was the requirement, which the skill says demands real infrastructure. Good: a handoff showing wrapper output and a filled traceability table. Bad: completion claimed on compile success alone. Borderline: skipping detekt in a repository that never configured it, noted explicitly.

**Verification, evidence, and uncertainty.** Execute the listed commands in a sample repository and confirm the traceability scan flags requirement rows without tests. SKILL.md workflow step eight names the four gradlew gates and requires evidence for coverage, migration safety, and security behavior. How to standardize traceability evidence across differently-shaped repositories is unresolved in the source.

**Second-order consequence.** The skill's traceability table makes coverage mechanical, a req_id without a matching test_id is a visible hole rather than a judgment call.

**Revision decision.** Keep the corpus verifier and add the wrapper gates, gradlew test, build, detekt, and ktlintCheck or Maven equivalents, plus a traceability check that each requirement row has a test.

**Retained seed evidence.** The original verification gate line and its repository verifier command block remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when a working agent should open this reference and which mode combination it should enter with. The seed guide says use this reference when the theme is mentioned, but the real trigger is an act, an agent is about to plan, build, harden, or review a Kotlin JVM backend and must first choose modes.

**Recommended default and causal basis.** Open this reference at Kotlin backend task intake, classify the surface, and adopt the matching default mode combination unless the task shape is novel. Mode selection attaches at task intake, and a guide keyed to topic mentions fires too late to shape the work packet.

**Operating conditions and assumptions.** The task's surface can be named, API, worker, job, consumer, migration, client, or review, before modes are chosen. The guide routes readers into this reference and does not decide the framework stance, which the workflow owns.

**Failure boundary and alternatives.** Keying to every Kotlin mention would open this reference for Android, multiplatform, and syntax questions the guardrails exclude. Bounded alternatives and recoveries: a lighter checklist for one-line fixes, direct guardrail review for pure hardening passes, or declining the skill for excluded surfaces.

**Counterexample, gotchas, and operational comparison.** Agents treat mode selection as optional flavor and pick modes after coding, inverting the skill's before-planning requirement. Good: an auth flow entering with Spec, framework, and Security modes. Bad: opening the skill for an Android layout question. Borderline: a worker refactor entered through Review Mode plus Coroutine Mode as the nearest risk mode.

**Verification, evidence, and uncertainty.** Walk a new-endpoint, an auth, and a migration request through the guide and confirm each lands on the skill's documented default combination. The SKILL.md default-combinations list maps five request shapes to mode sets and the guardrails name the excluded surfaces. How often novel task shapes fall outside the five defaults is unmeasured in this corpus.

**Second-order consequence.** The skill pre-computes routing, its five default combinations map common request shapes to mode sets, so intake classification is a lookup before it is a judgment.

**Revision decision.** Trigger on backend delivery events, new endpoint, auth flow, external client, migration, or review pass, and route each to its default mode combination.

**Retained seed evidence.** The original usage line and all four guidance bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide what end-to-end shape a competent Kotlin backend delivery session should take. The seed scenario shows a backend builder choosing a pattern and stops before the journey the skill scripts, classify the surface, write requirements, fix the stance, design boundaries, implement, and pass quality gates.

**Recommended default and causal basis.** Narrate a new-endpoint request taken from vague ask to named modes, three executable requirements, a slice-tested implementation, and a traceability-backed handoff. A journey that ends at pattern choice cannot rehearse the decisions that matter, which modes, which requirements, and which tests prove the behavior.

**Operating conditions and assumptions.** The repository's stack is inspectable and the user can confirm acceptance criteria when the spec surfaces ambiguity. The scenario dramatizes one representative delivery journey and does not enumerate every mode combination.

**Failure boundary and alternatives.** One linear journey cannot cover both greenfield endpoints and review passes, whose entry modes differ. Bounded alternatives and recoveries: a second journey for a production-readiness review, a failure journey where thin evidence forces a confidence warning, or the Spring guide URL as a candidate worked example.

**Counterexample, gotchas, and operational comparison.** Journeys written without an open-questions beat read as fiction, real intake surfaces unknowns the output contract explicitly reserves a section for. Good: a journey ending with the eight-section output contract filled. Bad: one ending at framework choice. Borderline: a hotfix journey that compresses the spec step and says so.

**Verification, evidence, and uncertainty.** Check each journey beat against the skill's eight workflow steps and confirm none is skipped silently. The SKILL.md workflow and output contract script exactly this sequence from classification to quality gates. Typical session length for a full work packet is unrecorded in this corpus.

**Second-order consequence.** The journey's pivotal moment is requirement writing, once behavior is WHEN-THEN-SHALL, framework choice, test mix, and done-ness all become checkable consequences.

**Revision decision.** Extend the journey through a named surface, REQ-KOTLIN-BACKEND requirements, a preserved framework stance, boundary design, and a wrapper-verified handoff in the output-contract order.

**Retained seed evidence.** The role-based opening, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Kotlin backend builder is starting from a service, route, or worker that must become production-safe and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `kotlin_backend_skill_entrypoint` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the smallest reliable backend pattern that preserves coroutine, framework, and operational discipline.
Reference opening trigger: Open this file when the task mentions kotlin backend skill entrypoint, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how an agent should choose between adopting, adapting, or avoiding this entrypoint for a given request and what being wrong costs. The seed guide keys adopt, adapt, and avoid to generic evidence agreement instead of the variables the skill uses, surface risk type, existing stack, and whether the request includes an explicit migration.

**Recommended default and causal basis.** Match mode combinations to surface shape, preserve the stack absent an explicit migration request, and route excluded surfaces away. The binding decision in Kotlin backend work is stance preservation versus migration, and evidence agreement says nothing about it.

**Operating conditions and assumptions.** The request's surface, risk, and stack can be judged before modes are locked. The guide calibrates entrypoint decisions per request and cannot waive the guardrails once a mode is chosen.

**Failure boundary and alternatives.** Stack-keyed advice under-determines greenfield services where there is no stack to preserve and Spec Mode must drive. Bounded alternatives and recoveries: default to Spec Mode alone when classification is doubtful, pilot with a review pass before delivery modes, or escalate stance conflicts to the user.

**Counterexample, gotchas, and operational comparison.** Agents read prefer Spring as prefer Spring everywhere, while the skill scopes it to repositories already in the Spring ecosystem. Good: adopting Spec plus Ktor Mode in a Ktor-first repo. Bad: avoiding the skill for a worker because workers feel non-standard. Borderline: adapting modes for a message consumer, composed from Coroutine and Resilience modes.

**Verification, evidence, and uncertainty.** Audit recent intakes for mode-to-surface match and check avoided tasks against the guardrail exclusion list. The SKILL.md framework-preference paragraph and guardrails define the adopt and avoid conditions explicitly. Borderline surface classifications remain judgment, and the source offers no tiebreak rule.

**Second-order consequence.** The skill prices being wrong in live traffic, its workload model warns that one bad recommendation can affect request handling, so avoid-decisions are cheap relative to a wrong stance.

**Revision decision.** Rekey adopt to matching a default mode combination on an inspectable stack, adapt to novel surfaces composed from the mode menu, and avoid to excluded surfaces or requests demanding unrequested migrations.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the kotlin backend skill entrypoint pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong kotlin backend skill entrypoint guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which local file outranks which when Kotlin backend entrypoint guidance conflicts or runs out. The seed hierarchy names one canonical source with a thin-corpus warning but does not say what the warning should trigger, reading the seven bundled reference files the entrypoint itself ranks in a numbered order.

**Recommended default and causal basis.** Consult SKILL.md first, follow its numbered reading order when deeper doctrine is needed, and use its rg heading-search commands for large files. The skill's context strategy is already a hierarchy, reference map first, then playbook, idioms, testing, ops, and security, so adjacent-source discovery has a prescribed path rather than an open search.

**Operating conditions and assumptions.** The references directory remains present beside the entrypoint at the archived path. The hierarchy ranks local retrieval priority for this theme and does not certify unread files.

**Failure boundary and alternatives.** Treating the bundled references as canonical without reading them would convert a discovery pointer into fabricated authority. Bounded alternatives and recoveries: a follow-up assignment reading the seven references, folding their headings into this map as unread signals, or leaving the single-row hierarchy with its warning intact.

**Counterexample, gotchas, and operational comparison.** The references list at the file's foot duplicates the context strategy, and skimming one while missing the other's ordering loses the priority information. Good: escalating a testing question to the testing-and-fixtures reference by the skill's order. Bad: quoting the unread playbook as canonical doctrine. Borderline: citing a reference's title and role from the entrypoint's own description, labeled unread.

**Verification, evidence, and uncertainty.** Confirm the seven reference paths exist beside the entrypoint and their listed order matches the context strategy. The SKILL.md context strategy numbers seven reference files and supplies heading-search commands for the five largest. Whether the archived references match any live copy of this skill was not established.

**Second-order consequence.** The confidence warning is self-resolving, the canonical source names exactly where its missing corpus lives, which most thin-corpus themes cannot do.

**Revision decision.** Keep SKILL.md canonical, list the seven bundled references as ranked unread discovery targets in the skill's own reading order, and retain the confidence warning until they are read.

**Retained seed evidence.** The classification vocabulary line, the confidence warning, and the single hierarchy row with its reviewer question remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/kotlin-backend-delivery-01/SKILL.md | canonical primary source | Kotlin Backend Delivery 01; Mode Selection; Workflow | What guidance, warning, or example should this source contribute to Kotlin Backend Skill Entrypoint? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete evidence object must exist before this reference counts as operational. The seed artifact names a request lifecycle diagram while the skill's operational artifact is its output contract, an eight-section work packet with a req-to-test traceability table.

**Recommended default and causal basis.** Carry one filled packet for a representative endpoint as the reviewable instance, with the lifecycle diagram kept as its service-design attachment. The skill instructs results be returned in a fixed order from work mode through open questions, so the reviewable artifact this theme produces is that packet, not a diagram alone.

**Operating conditions and assumptions.** The packet names its surface and modes and distinguishes user-confirmed requirements from agent-drafted ones. The artifact certifies this reference is operational and does not require retro-fitting packets onto past work.

**Failure boundary and alternatives.** A full eight-section packet is ceremony for trivial fixes where a two-line requirement and a test suffice. Bounded alternatives and recoveries: accept a compressed packet for hotfixes, pair the packet with the wrapper-gate output, or use the Spring guide URL as a future worked-example template.

**Counterexample, gotchas, and operational comparison.** Packets written after implementation look identical to spec-first ones, so provenance notes matter. Good: a packet whose every requirement row has a test row. Bad: a lifecycle diagram with no requirements behind it. Borderline: a review-mode packet with findings in place of an implementation plan, noted as review-shaped.

**Verification, evidence, and uncertainty.** Check the artifact shows all eight contract sections and a traceability table with no empty test cells. The SKILL.md output contract enumerates the eight sections and prescribes the traceability table shape. Whether packet completeness correlates with fewer delivery defects is untested in this corpus.

**Second-order consequence.** The traceability table is the packet's load-bearing row, it converts production-biased from a mood into a checkable mapping between promises and proofs.

**Revision decision.** Define the artifact as one completed work packet, named modes, executable requirements, service design, constraints, verification matrix with req_id-to-test_id rows, plan, gates, and open questions.

**Retained seed evidence.** The artifact definition line and the three artifact field rows with completion rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: request lifecycle diagram with persistence boundary, observability hook, and failure table.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Kotlin Backend Skill Entrypoint | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which entrypoint behaviors should be taught as exemplary, negligent, or conditionally acceptable. The seed examples restate generic load-canon verdicts and never show entrypoint conduct judged, a mode-scoped delivery, a code-first session, or a preserved-stack judgment call.

**Recommended default and causal basis.** Grade every example by two questions, were modes and requirements fixed before code and was the existing stack preserved. Authors calibrate on instances, and the skill's own default combinations supply concrete request shapes worth grading.

**Operating conditions and assumptions.** Each example names its surface, modes, and the delivery consequence. The examples grade entrypoint conduct, not the quality of the resulting Kotlin code.

**Failure boundary and alternatives.** Examples drawn only from greenfield endpoints transfer poorly to review passes, whose failure mode is missed risk rather than missing spec. Bounded alternatives and recoveries: draw examples from this repository's actual service history, add a fourth case for a guardrail catch at review, or pair each verdict with its registry row.

**Counterexample, gotchas, and operational comparison.** Stance violations hide inside dependency diffs, a new starter or plugin is often the first visible sign of an uninvited migration. Good: an auth flow delivered through Spec, Spring Boot, and Security modes with a filled packet. Bad: a Ktor service quietly rebuilt on Spring. Borderline: a blocking JDBC service kept blocking with the dispatcher tradeoff documented.

**Verification, evidence, and uncertainty.** Scan each verdict against the mode-selection and stance-preservation rules and confirm the graded behavior is observable in a transcript or diff. The SKILL.md stance paragraph and guardrails anchor all three recast verdicts. Which negligent pattern dominates real practice here is unmeasured, so the chosen cases reflect expected shapes.

**Second-order consequence.** The most instructive bad example is competence-shaped, an agent producing excellent Spring code in a Ktor repository, wrong not in quality but in stance.

**Revision decision.** Recast good as a mode-scoped spec-first delivery, bad as a code-first session that migrated frameworks uninvited, and borderline as an intentionally-blocking service with the tradeoff named.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Kotlin Backend Skill Entrypoint after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Kotlin Backend Skill Entrypoint as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Kotlin Backend Skill Entrypoint only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising entrypoint practice or this reference. The seed metrics name lead time and guessed-framework signals but no way to observe them, packets, traceability tables, and wrapper-gate outputs are the places these signals actually show up.

**Recommended default and causal basis.** Track per delivery the packet's section completeness, the traceability fill rate, and whether the stack survived unchanged. This theme improves outcomes through spec-first packets, so its instruments must watch packet completeness and requirement-to-test coverage, not impressions.

**Operating conditions and assumptions.** Deliveries record their packets somewhere reviewable. The metrics gauge the entrypoint discipline this reference teaches, not service runtime health, which Operations Mode owns.

**Failure boundary and alternatives.** Packet-based metrics need sessions to actually produce packets, making them blind to informal work. Bounded alternatives and recoveries: sampled packet audits instead of full coverage, reviewer-graded requirement quality, or wrapper-gate pass rates as a proxy.

**Counterexample, gotchas, and operational comparison.** Counting packets rewards ceremony, a filled template with untestable requirements passes the count while failing the point. Good: tightening intake after two packets ship with empty test cells. Bad: celebrating packet counts while requirements stay vague. Borderline: skipping packet audits in a period with no backend work, noted.

**Verification, evidence, and uncertainty.** Audit recent deliveries for packet records and confirm each traceability row's test actually exists in the repository. The seed's lead-time indicator and guessed-behavior failure signal anchor the loop the packet metrics extend. Healthy baselines for packet completeness rates are unmeasured, so first thresholds are provisional.

**Second-order consequence.** The vague-claim rejection rule doubles as a metric source, every rejected production-ready is a recorded moment where the spec discipline did its job.

**Revision decision.** Adopt packets-with-complete-traceability rate, requirements rejected for vagueness count, and uninvited-migration near-misses as primary signals alongside the seed's lead-time indicator.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: lead time from requirement to verified endpoint stays under one focused implementation session.
Failure signal: framework choice or coroutine behavior is guessed instead of verified with tests and docs.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared ready to hand to an agent. The seed checklist confirms generic sections exist and never checks the theme's own obligations, that the nine modes, the workflow order, the output contract, and the guardrail exclusions are all represented.

**Recommended default and causal basis.** Tick structural items with citations, then verify mode, workflow, contract, and guardrail coverage by grepping this document against the skill's lists. This document teaches a mode-gated entrypoint, so its readiness check must confirm the mode menu and contract survive intact, not just that prose sections exist.

**Operating conditions and assumptions.** Each added item names its target section and whether a script or human verifies it. The checklist gates this document's readiness, not the quality of services later delivered under it.

**Failure boundary and alternatives.** A reference that dropped the guardrail exclusions would still pass the current checklist and invite Android questions into a backend skill. Bounded alternatives and recoveries: generate coverage items mechanically from the skill's section headings, deep-check two random items per review, or pair-review the artifact packet.

**Counterexample, gotchas, and operational comparison.** Coverage can pass while descriptions contradict the source, so coverage ticks and fidelity ticks stay separate. Good: a coverage tick citing the line naming all nine modes. Bad: all ticks green from a headings glance. Borderline: carrying forward last review's contract tick with a staleness note.

**Verification, evidence, and uncertainty.** List the skill's modes, steps, contract sections, and guardrails, then grep this document for each and record the misses. The seed's seven structural items map onto real sections here and anchor the added coverage layer. How much fidelity checking each item needs per revision depends on edit volume, so depth stays judgment.

**Second-order consequence.** A checklist for an entrypoint document is a contract about a contract, its highest-value items are the ones confirming the inner contract was transcribed faithfully.

**Revision decision.** Append items requiring the nine modes named, the eight workflow steps ordered, the output contract's sections listed, and the exclusion guardrails present.

**Retained seed evidence.** All seven structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Kotlin Backend Skill Entrypoint.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a question should leave this reference and which neighbor owns it. The seed routing splits the theme name into kotlin, backend, and skill keywords aimed at unnamed destinations instead of routing by question type to real corpus neighbors.

**Recommended default and causal basis.** Keep intake, mode, and contract questions here, send reliability-depth questions to the kotlin reliability neighbor and cross-skill authoring questions to skill-structure references. Readers leave this reference with distinct needs, deeper Kotlin reliability doctrine and skill-authoring mechanics, and each need has a real neighbor in this corpus.

**Operating conditions and assumptions.** Each route names its trigger, a destination resolving to a real file, and what stays here. Routing redirects within this corpus and cannot authorize work in a destination's domain.

**Failure boundary and alternatives.** Keyword routes point at references that exist only as words, stranding the reader who follows them. Bounded alternatives and recoveries: consult the corpus index before adding routes, keep unresolved needs here with a gap note, or escalate genuine overlap to the user.

**Counterexample, gotchas, and operational comparison.** Framework questions masquerade as routing needs, most are answered by the entrypoint's own stance rule without leaving the file. Good: sending a retry-budget deep-dive to the kotlin reliability reference. Bad: routing to the backend adjacent reference, a keyword with no file. Borderline: answering a small resilience question inline with a route noted for depth.

**Verification, evidence, and uncertainty.** Resolve each named destination to an existing corpus file and walk one sample question through each trigger. The kotlin reliability reference patterns file sits pending in this same queue directory alongside this file. The best split between answering inline and routing away depends on question depth, so borderline calls stay recorded judgment.

**Second-order consequence.** This file's nearest neighbor is its own sibling, the kotlin reliability reference sits adjacent in the queue and owns the day-two depth this entrypoint only gestures at.

**Revision decision.** Route reliability and hardening depth to the kotlin reliability reference patterns file and skill-structure questions to the corpus's skill-authoring references, keeping mode selection and workflow here.

**Retained seed evidence.** The adjacency guidance line and the three keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use runtime, security, or testing Kotlin references when the question is about day-two operation, abuse cases, or fixtures.
Adjacent reference 1: consider the kotlin adjacent reference when the current task pivots away from kotlin backend skill entrypoint.
Adjacent reference 2: consider the backend adjacent reference when the current task pivots away from kotlin backend skill entrypoint.
Adjacent reference 3: consider the skill adjacent reference when the current task pivots away from kotlin backend skill entrypoint.

## Workload Model

**Decision supported.** This section helps decide how much Kotlin backend work one request may consume before splitting or escalation. The seed model bounds one service boundary and twenty-five endpoints per batch but not the entrypoint's own working unit, one work packet per surface with modes fixed once and requirements enumerated before code.

**Recommended default and causal basis.** Plan one packet per surface, fix modes at intake, and split when requirements exceed what one session can verify. The costly unit in this theme is an unscoped session, work that spans surfaces without a packet loses the traceability that bounds review effort.

**Operating conditions and assumptions.** Surfaces are classified before sizing and requirement counts are visible at intake. The model bounds entrypoint effort per request and does not bound service runtime capacity, which belongs to operations doctrine.

**Failure boundary and alternatives.** Packet-per-surface budgeting varies with surface size, a message consumer and a full auth flow are both one surface with very different weights. Bounded alternatives and recoveries: time-boxed sessions with explicit open-questions handoffs, per-mode sub-packets for large surfaces, or reviewer-set requirement budgets.

**Counterexample, gotchas, and operational comparison.** Review passes tempt unbounded scope, twenty-five endpoints is the skill's explicit per-batch ceiling for exactly that reason. Good: an auth flow split into token issuance and reset-flow packets. Bad: one session refactoring three services without a packet. Borderline: a two-endpoint feature kept as one packet with both surfaces named.

**Verification, evidence, and uncertainty.** Count packets, surfaces, and requirements in recorded sessions and test whether packet-per-surface sessions close in one focused session. The seed's bounded capacity row sets the twenty-five endpoint and one-boundary ceilings this revision keys the packet unit to. Typical requirement counts per surface are unmeasured, so the split threshold stays a monitored judgment.

**Second-order consequence.** Requirements are the natural splitting currency, when a surface's REQ list outgrows one focused session the skill's own lead-time indicator says the task is two packets.

**Revision decision.** Rebound the model around one packet per classified surface, one mode set fixed at intake, and requirement counts as the size signal that triggers splitting.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Kotlin Backend Skill Entrypoint as a backend service operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | service implementation, route review, worker execution, and operational hardening work where a single wrong recommendation can affect live request handling | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one service boundary, up to 25 endpoints or workers, 1000 representative requests, and one deploy rollback path per review batch | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Kotlin Backend Delivery 01; Mode Selection; Workflow; Output Contract; Guardrails; Context Strategy | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is request lifecycle diagram with persistence boundary, observability hook, and failure table | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must demonstrate before its guidance is trusted. The seed table demands perfect boundary preservation and an 18-of-20 decision sample with no sampling procedure, and omits the theme's own reliability notions, requirement testability and stance preservation across deliveries.

**Recommended default and causal basis.** Keep the four dimensions with methods attached and lead with requirement-form audits and dependency-diff stance checks. The skill defines success operationally, every requirement expressed as WHEN-THEN-SHALL with a mapped test, and that definition is checkable where the seed's percentages are not.

**Operating conditions and assumptions.** Each target names its metric, sampling method, population, owner, and the corrective action a miss triggers. The targets judge this reference and the entrypoint discipline, not the runtime reliability of delivered services.

**Failure boundary and alternatives.** Quoting the unmeasured percentages as achieved performance manufactures rigor this corpus never earned. Bounded alternatives and recoveries: binary pass-fail packet audits, pooled sampling across the corpus's Kotlin themes, or postmortems on every stance violation instead of rates.

**Counterexample, gotchas, and operational comparison.** Stance checks against code alone miss build-file migrations, so audits must read dependency and plugin diffs too. Good: an audit of ten packets finding every REQ in WHEN-THEN-SHALL form. Bad: reporting the 18-of-20 nobody sampled. Borderline: a stance audit reading only source diffs, recorded with that caveat.

**Verification, evidence, and uncertainty.** Run one requirement-form audit and one dependency-diff stance check per review cycle. The SKILL.md requirement-form rule and stance-preservation paragraph give the operational definitions the added targets measure. No baseline exists for any threshold here, so the first measured cycle defines what is achievable.

**Second-order consequence.** Requirement testability is this theme's cheapest objective check, a requirement either names observable behavior or it does not, no sampling needed.

**Revision decision.** Add a requirement-testability target, every REQ row carries a WHEN-THEN-SHALL body and a test mapping, and a stance-preservation target, zero uninvited framework or version migrations, with every threshold marked unbaselined and owned.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failures in the Kotlin backend entrypoint fabric deserve standing mitigations. The seed table carries hygiene and traffic rows and omits how entrypoint work itself fails, modes never chosen, requirements left vague, stances silently migrated, and coroutine safety assumed rather than designed.

**Recommended default and causal basis.** Detect mode-skip by absent mode lists in packets, vagueness by unmeasurable words in requirements, migrations by dependency diffs, and coroutine risk by unreviewed blocking calls in suspend paths. Triage during a bad delivery needs rows describing how the work packet decayed, ranked by how silently each failure ships.

**Operating conditions and assumptions.** Each row names its trigger, earliest observable signal, blast radius, containment, and correction. The table covers entrypoint-process failures, while runtime failures belong to resilience and operations doctrine.

**Failure boundary and alternatives.** Rows are worthless if their earliest signal fires only after the service is in production. Bounded alternatives and recoveries: wire packet checks into review templates, audit dependency diffs on a sampled cadence, or require the mode list in every PR description.

**Counterexample, gotchas, and operational comparison.** Assumed coroutine safety fails politely, code that compiles and passes unit tests can still starve dispatchers under production load. Good: a review template catching a packet with no mode list. Bad: a PR that swapped Ktor for Spring with no migration request on record. Borderline: mild requirement vagueness accepted for a spike, flagged as spike-only.

**Verification, evidence, and uncertainty.** Seed one failure per row in a drill and confirm the named signal fires before a simulated merge would ship the defect. The SKILL.md workflow, stance paragraph, and coroutine step document the disciplines whose absence these rows detect. Observed frequency of each failure in this team's history is unmeasured, so ordering encodes expected silence.

**Second-order consequence.** Every added failure is a missing artifact rather than a wrong one, no mode list, no observable criteria, no stance note, no dispatcher decision, which makes absence itself the detection signal.

**Revision decision.** Add mode-skip, vague-requirement, silent-migration, and assumed-coroutine-safety rows with pre-merge detection signals.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| request surge overloads path | traffic spikes exceed handler, pool, or coroutine limits | apply rate limits, queue bounds, cancellation, and rollback playbook before rollout |
| security boundary silently fails | auth, permission, or input validation assumptions are untested | run abuse-case tests and require explicit deny-by-default behavior |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failing operation, in delivered services or in reference work, should be retried, redesigned, or escalated. The seed bullets classify verification failures generically and never carry the skill's own retry doctrine, no retries without idempotency, timeout budgets, and failure classification.

**Recommended default and causal basis.** For services, classify failures and verify idempotency before any retry policy, and for reference work, keep the seed's one-bounded-retry-then-escalate rule. Retry advice that skips idempotency converts transient faults into duplicate side effects, which is why the skill's guardrail binds the three conditions together.

**Operating conditions and assumptions.** Service retry advice names its idempotency mechanism and timeout budget explicitly. This governs both retrying entrypoint verification work and the retry guidance the entrypoint gives services, kept as two labeled layers.

**Failure boundary and alternatives.** The idempotency precondition is about service-level retries, and applying it to documentation-verification retries would be a category error this section must keep separate. Bounded alternatives and recoveries: queue-and-drain designs for non-idempotent work, circuit breakers where downstream health is observable, or escalation to Resilience Mode for full failure design.

**Counterexample, gotchas, and operational comparison.** The tempting failure is adding retries to calm a flaky integration, which multiplies load exactly when the downstream is least able to absorb it. Good: a retry policy shipped with an idempotency key and a timeout budget. Bad: blanket retries on a payment call with no idempotency. Borderline: one bounded verification retry after a stale-evidence refresh, per the seed rule.

**Verification, evidence, and uncertainty.** Audit retry-bearing changes for named idempotency mechanisms and check verification reruns stayed within the bounded-retry rule. The SKILL.md guardrail forbids recommending retries without idempotency, timeout budgets, and failure classification. How often service retries in this team's history lacked idempotency is unmeasured.

**Second-order consequence.** The skill's retry guardrail is really a design-order rule, idempotency is a property you build before retrying, not a flag you enable after.

**Revision decision.** Add the service-layer rule, retries require idempotency, timeout budgets, and failure classification, alongside the existing documentation-layer retry bullets.

**Retained seed evidence.** All five retry and backpressure bullets, including the one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence must exist that an entrypoint session happened as claimed. The seed bullets recycle generic evidence records and never name this theme's evidence stream, the work packet itself, the mode list, the traceability table, wrapper-gate outputs, and the open-questions log.

**Recommended default and causal basis.** Record per delivery the packet, the wrapper-gate results, and the open questions, keeping raw transcripts out per the seed's small-evidence preference. The skill's output contract already defines the session record, so observability here means persisting the packet rather than inventing new telemetry.

**Operating conditions and assumptions.** Sessions can persist small text records alongside the delivered change. This covers observing entrypoint sessions, while service runtime observability belongs to Operations Mode and its Actuator, logging, and tracing doctrine.

**Failure boundary and alternatives.** Full packet retention for every small fix can outgrow its value, so retention needs a size-based selection rule. Bounded alternatives and recoveries: retain only packets plus gate summaries instead of full session logs, sample-audit recorded packets, or accept PR descriptions as the packet carrier.

**Counterexample, gotchas, and operational comparison.** Paraphrased requirements drift from what was actually agreed, so the recorded packet must be the literal delivered text. Good: a PR carrying its packet, gate output, and two open questions. Bad: a merged service with no recorded requirements. Borderline: a hotfix recorded as a two-line packet with the compression noted.

**Verification, evidence, and uncertainty.** Spot-check delivered changes for accompanying packets and confirm each records modes, traceability, and gate results. The SKILL.md output contract defines the packet sections this checklist persists, and the seed prefers small audit evidence over transcript dumps. The retention horizon for packet-level records is untuned, so the keep-packet rule is provisional.

**Second-order consequence.** The open-questions section is the packet's most diagnostic record, it captures what the spec could not resolve, which is where the next defect is most likely to live.

**Revision decision.** Recenter the checklist on session evidence, the packet, its mode list, the filled traceability table, wrapper-gate output summaries, and unresolved open questions.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture error count, timeout count, retry count, saturation signal, and rollback trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove the entrypoint discipline is buying more than it costs. The seed method fixes p95 and p99 latency numbers for handlers but not the theme's own performance question, whether spec-first entry actually shortens the requirement-to-verified-endpoint lead time it promises.

**Recommended default and causal basis.** Log per delivery the session time, packet completeness, rework rounds, and wrapper-gate outcomes, publishing ratios with their sample sizes. The skill's leading indicator is lead time within one focused session, so verification must time sessions against packet completeness, not just handlers against milliseconds.

**Operating conditions and assumptions.** Deliveries record start and handoff times and rework is attributable to its delivery. This evaluates the entrypoint discipline's cost and benefit, while handler latency targets belong to each service's own SLO.

**Failure boundary and alternatives.** Session-time comparisons need enough recorded deliveries to average over, making early ratios unstable. Bounded alternatives and recoveries: compare packet-backed against informal deliveries on rework rounds, use reviewer decision time as the documentation-side metric, or track only gate failures at first.

**Counterexample, gotchas, and operational comparison.** Lead time is inflatable by scope shrinking, a fast session that deferred half the requirements measured nothing. Good: a report showing packet-backed deliveries rework-free across a quarter. Bad: quoting handler latency as proof the entrypoint works. Borderline: an early lead-time ratio published with a sample-of-two caveat.

**Verification, evidence, and uncertainty.** Collect session times and rework counts across several deliveries and publish the comparison with its sample size. The seed's performance method line makes the latency numbers conditional on an absent service-specific SLO. Actual lead-time distributions for packet-backed work are absent from this corpus, so benefit claims stay unquantified.

**Second-order consequence.** The seed's 200-millisecond default is explicitly a placeholder for a missing SLO, its real instruction is that someone must own a number before deployment.

**Revision decision.** Measure lead time per packet-backed delivery, rework rounds after handoff, and gate-failure counts, keeping the seed's latency defaults as the absent-SLO fallback they are.

**Retained seed evidence.** The performance method line, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require a service-specific SLO before deployment; absent that, keep local verification to p95 under 200 ms and p99 under 500 ms for representative handlers or document why latency does not apply.
Leading indicator to measure: lead time from requirement to verified endpoint stays under one focused implementation session.
Failure signal to watch: framework choice or coroutine behavior is guessed instead of verified with tests and docs.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what scale this entrypoint stops sufficing and what structure replaces it. The seed statement recites multi-system and SLO limits and misses this theme's scale walls, mode combinations that stop fitting novel surfaces, doctrine that outgrows the entrypoint into its references, and framework releases that retire stance assumptions.

**Recommended default and causal basis.** Answer intake questions from the entrypoint while they fit, escalate depth to the numbered references, and re-check stance assumptions after major framework releases. The entrypoint scales by delegation, its context strategy pushes depth into seven references, so the growth signal is questions the 129-line file can no longer answer alone.

**Operating conditions and assumptions.** The bundled references remain present and framework release events are noticed. The boundaries bound the entrypoint reference, not the size of services Kotlin can support.

**Failure boundary and alternatives.** Delegation advice fails when the referenced files are unread or stale, which this corpus has not yet verified. Bounded alternatives and recoveries: a follow-up pass reading the references before depth is needed, release-triggered stance audits, or splitting persistent novel surfaces into their own skills.

**Counterexample, gotchas, and operational comparison.** Framework releases silently retire version-coupled advice, the skill's compiler-plugin guidance is exactly the kind of claim a major release invalidates. Good: a testing deep-dive escalated to the testing reference by the skill's order. Bad: stretching the entrypoint to answer JPA proxying details it delegates. Borderline: composing a novel mode set for a streaming consumer, recorded as a menu gap.

**Verification, evidence, and uncertainty.** Track questions the entrypoint could not answer alone and confirm stance claims are re-checked after each major framework release. The SKILL.md context strategy exists precisely because the entrypoint delegates depth to seven referenced files. The question rate at which delegation beats inlining is unmeasured, so the boundary stays a monitored judgment.

**Second-order consequence.** The mode menu is the scale fuse, when intake repeatedly composes novel mode sets the menu itself is signaling that the skill needs a new mode or a split.

**Revision decision.** Add entrypoint-scale signals, recurring questions that need the bundled references, surfaces that fit no default mode combination, and framework releases that demand stance re-verification.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Kotlin Backend Skill Entrypoint stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would genuinely refresh this reference's external evidence. The seed query table drops the internal theme name into three templates whose literal phrasing targets a coinage no external author uses.

**Recommended default and causal basis.** Search framework and coroutine release notes on a periodic trigger, feeding the external map and the stance-bearing sections. Useful refresh queries speak the ecosystem's vocabulary, Kotlin backend best practices, Spring Boot Kotlin support, Ktor releases, coroutine guidance, not this corpus's file-naming scheme.

**Operating conditions and assumptions.** Each query names its target section, source type, and firing trigger. The queries refresh external analogues for this theme, while the local skill changes only through repository edits.

**Failure boundary and alternatives.** Empty results from a coinage query logged as freshness confirmed convert search blindness into false confidence. Bounded alternatives and recoveries: follow the four candidate URLs directly once retrieval is authorized, track Spring and Ktor blogs, or drive refresh from dated retrieval records.

**Counterexample, gotchas, and operational comparison.** Kotlin search results skew toward Android content, so backend-scoped phrasing matters more here than in most themes. Good: a query on Spring Boot Kotlin release notes feeding the stance sections. Bad: searching the literal theme title and logging zero hits as freshness. Borderline: adopting a well-argued practitioner post with an inference label pending corroboration.

**Verification, evidence, and uncertainty.** Run each query once, grade the top results for backend relevance, and rewrite phrasings that return mostly Android noise. The seed's three-row structure targeting docs, repositories, and release notes is sound scaffolding for the revised vocabulary. Which phrasings will track this vocabulary is unknowable in advance, so the queries need their own review cadence.

**Second-order consequence.** This theme's most perishable facts are stance-coupled, compiler plugins, framework versions, and coroutine APIs, which makes release-notes queries the highest-yield refresh channel.

**Revision decision.** Rephrase toward ecosystem vocabulary, Kotlin server-side documentation updates, Spring Boot Kotlin release notes, Ktor changelog, and kotlinx.coroutines releases, each tied to the section it refreshes.

**Retained seed evidence.** All three labeled query rows with their official-docs, repository, and release-notes targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | kotlin backend skill entrypoint official documentation best practices |
| `github_repository_query_phrase` | kotlin backend skill entrypoint GitHub repository examples |
| `release_notes_query_phrase` | kotlin backend skill entrypoint changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how statements in this reference must be labeled so readers know what each claim rests on and how fresh it is. The seed notes define the three labels but ignore this file's specific hazards, doctrine attributed to bundled references nobody read and stance facts coupled to framework versions that expire.

**Recommended default and causal basis.** Label per claim, mark the seven bundled references unread-local, and keep all four external URLs as unretrieved candidates. Downstream confidence calibrates on these labels, and a claim credited to an unread reference misleads exactly the reader who trusts citations most.

**Operating conditions and assumptions.** Labels stay stable corpus-wide and every combined-inference clause names the local and external inputs it merges. The notes govern labeling in this reference and its reuses, not the ranking of sources, which the hierarchy owns.

**Failure boundary and alternatives.** Labels applied per section rather than per claim let one labeled sentence launder its unlabeled neighbors. Bounded alternatives and recoveries: introduce an explicit unread-local tag, inline labels parenthetically on key claims, or index claims to labels during verification.

**Counterexample, gotchas, and operational comparison.** Packet and prompt reuse strips labels mechanically, so load-bearing claims need labels embedded in their own sentences. Good: the nine-mode menu cited as read local fact. Bad: playbook doctrine quoted as if consulted. Borderline: a reference file's role described from the entrypoint's own summary, labeled as entrypoint-derived.

**Verification, evidence, and uncertainty.** Sample load-bearing claims, confirm correct labels, and verify no bundled-reference claim lacks its unread marker. The three seed definitions match the corpus-wide label vocabulary and the boundary-preservation target elsewhere in this file. Label durability through packet reuse and prompt quotation is unaudited, so leakage risk remains an assumption.

**Second-order consequence.** This theme needs a distinction inside the local label itself, read-local versus unread-local, because the skill's own pointers make unread files look like consulted sources.

**Revision decision.** Add rules marking bundled-reference material as unread-local until actually read and dating version-coupled stance facts, with URL-derived material marked inference pending retrieval.

**Retained seed evidence.** All three label definitions, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
