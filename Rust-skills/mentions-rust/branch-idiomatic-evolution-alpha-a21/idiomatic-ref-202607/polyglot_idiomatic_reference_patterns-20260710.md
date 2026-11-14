# Polyglot Idiomatic Reference Patterns

**Decision supported.** This section helps decide which pattern corpus and stack section should drive an idiomatic recommendation for a given polyglot task. The seed title names a polyglot theme without stating its organizing move, that idioms must stay classified by stack and layer, TypeScript branded types, Java records, Go error wrapping, Kafka idempotent producers, Terraform typed variables, instead of being flattened into language-neutral advice.

**Recommended default and causal basis.** Route any polyglot idiom question first to the matching stack section of Idiom96 or Idiom98, then check whether the idiom is a language-core, standard-library, or ecosystem-layer concern before adopting it. All four mapped corpora organize by stack and layer, Idiom96 splits its library into TypeScript, Java, Go, DevOps, and Kafka parts, Idiom98 keeps per-stack sections with per-stack quality checklists, and broad-idiomatic-patterns mandates an L1 core, L2 std, L3 ecosystem split for Rust.

**Operating conditions and assumptions.** The task names a concrete stack covered by the corpus, TypeScript, JavaScript, Java/Spring, Go, Kafka, or Terraform/Kubernetes/Docker/GitHub Actions infrastructure. This reference governs how to select and cite idiomatic patterns across the four mapped polyglot corpora, not how to teach any single language from scratch.

**Failure boundary and alternatives.** Layer-tagged guidance collapses when a task spans stacks at their integration seam, a Go service publishing Avro events to a Java consumer needs cross-stack contract idioms that no single language section carries. Bounded alternatives and recoveries: for Rust tasks use broad-idiomatic-patterns' L1/L2/L3 extraction frame, for product-codebase idioms use opencode-genius-idiomatic-patterns' twelve provenance-tagged patterns, for uncovered stacks escalate to external research with explicit labels.

**Counterexample, gotchas, and operational comparison.** Idiom98 embeds tool recommendations dated 2024-2025, Vitest, Zod, Gradle Kotlin DSL, golangci-lint, ArgoCD, that will silently age, quoting them as current without a freshness check misleads. Good: pulling Go table-driven test shape from Idiom98 section G.1.2 for a Go test task. Bad: pasting the TypeScript Result type into a Java answer where Idiom98 already defines a sealed Result interface. Borderline: reusing the retry-with-jitter idiom across stacks, the shape ports but each runtime's sleep and error taxonomy differs.

**Verification, evidence, and uncertainty.** Confirm the recommendation cites a stack-matched section identifier such as TS.2.1, J.1.1, G.1.1, K.1.1, or D.1.1 from the mapped corpus. All four mapped local files were read in full during this evolution, 1,772 plus 8,681 plus 504 plus 1,960 lines. Whether the 2025-dated pattern libraries still match current compiler, framework, and broker releases cannot be judged from the archive alone.

**Second-order consequence.** Layer classification is what makes idioms portable, the same accept-interfaces-return-structs shape appears as Go small interfaces, Java repository interfaces with constructor injection, and TypeScript IDatabase constructor parameters, so the layer label reveals the shared principle beneath the syntax.

**Revision decision.** Open with the stack-and-layer classification rule and name the five stacks the local corpus actually covers so readers route to the right pattern family immediately.

**Retained seed evidence.** The exact theme title and its reference-patterns framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which kind of polyglot idiom claim. The seed map labels all four local rows with one generic role, historical idiomatic pattern corpus, hiding that they are four different instrument types, a pattern library, a TDD-workflow handbook, an extraction prompt, and a mined-codebase pattern report.

**Recommended default and causal basis.** Cite Idiom96 or Idiom98 for concrete stack idioms, broad-idiomatic-patterns for the extraction schema, and opencode-genius for production-provenance examples, never the external URLs for facts. Idiom96 is a flat catalog of stack idioms, Idiom98 wraps idioms in a stub-red-green-refactor delivery workflow with quality gates, broad-idiomatic-patterns is a prompt template for extracting new patterns, and opencode-genius documents patterns mined from one shipped TypeScript product.

**Operating conditions and assumptions.** Claims stay within what the four fully read files literally contain. The table records provenance for this document's claims and does not certify the external URLs as current or relevant.

**Failure boundary and alternatives.** The three external URL rows, the Codex AGENTS.md guide, GitHub Actions docs, and agents.md, were never retrieved in this evolution and cannot corroborate any polyglot idiom claim. Bounded alternatives and recoveries: retrieve the three URLs in a future refresh and upgrade their rows, or drop them from the map if they stay untouched across cycles.

**Counterexample, gotchas, and operational comparison.** The seed pairs polyglot pattern sources with agent-instruction URLs from a different theme, treating that pairing as evidence of relevance would be a category error. Good: citing Idiom98 K.1.2 for manual Kafka offset commit guidance. Bad: citing agents.md for anything about Go error wrapping. Borderline: citing opencode-genius for a general TypeScript idiom, it proves one codebase's usage, not ecosystem consensus.

**Verification, evidence, and uncertainty.** Trace every idiom claim in this file to a named section of one of the four read files. The source map rows and the full reads performed during this evolution. Why the seed generator attached agent-instruction URLs to a polyglot language theme is unrecorded.

**Second-order consequence.** The four instrument types compose into a pipeline, extract patterns with the broad prompt schema, catalog them Idiom96-style, operationalize them through Idiom98's TDD workflow, and validate them against a real codebase the way opencode-genius does.

**Revision decision.** Annotate each local row with its instrument type, catalog, workflow handbook, extraction prompt, or mined-pattern report, and mark all three external rows unretrieved.

**Retained seed evidence.** All source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom96-polyglot-basic-patterns-20251205.md | local_corpus_source_material | local_corpus_sourced_fact | historical idiomatic pattern corpus |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom98-Multi-Lang-Notes-20251205.md | local_corpus_source_material | local_corpus_sourced_fact | historical idiomatic pattern corpus |
| agents-used-monthly-archive/idiomatic-references-202602/broad-idiomatic-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | historical idiomatic pattern corpus |
| agents-used-monthly-archive/idiomatic-references-202602/opencode-genius-idiomatic-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | historical idiomatic pattern corpus |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary agent instruction context model |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | verification and automation model |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | general agent instruction format |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which idiom families deserve default adoption pressure across a polyglot codebase. The seed scoreboard scores three corpus-hygiene rules at 95, 91, and 88 while the corpus's own load-bearing polyglot rules, explicit types at boundaries, errors as values with context, dependencies injected through constructors, and effects made idempotent, go unranked.

**Recommended default and causal basis.** When prioritizing idiom adoption in a polyglot codebase, install the four cross-stack rules before any single-stack nicety. Those four recur across every stack section, TypeScript branded types and Zod, Go fmt.Errorf with the %w verb, Java constructor injection over field injection, and Kafka enable.idempotence with acks all.

**Operating conditions and assumptions.** The codebase spans at least two of the corpus stacks and has working compile plus test gates to enforce the rules. The scoreboard ranks cross-stack idiom families for adoption priority, not individual snippets inside one language.

**Failure boundary and alternatives.** The numeric scores were never measured, the corpus supplies checklists and NON-NEGOTIABLE headings, not benchmark data, so the numbers order emphasis rather than quantify anything. Bounded alternatives and recoveries: rank by observed incident frequency once the team has postmortem data, or rank by enforcement cost with lint-enforceable rules first.

**Counterexample, gotchas, and operational comparison.** Ranking by tier tempts teams to skip the per-stack instantiation step, a rule like idempotent effects means producer configuration in Kafka but temp-file-plus-rename in storage code. Good: adopting error wrapping repo-wide before debating Go functional options. Bad: enforcing the seed's abstract scores as if benchmarked. Borderline: promoting exhaustive pattern matching, TypeScript and Java 21 switch support it natively while Go approximates it with linters.

**Verification, evidence, and uncertainty.** Check each promoted rule appears in at least three distinct stack sections of the mapped corpus. The eight non-negotiable principles of Idiom96 and the per-stack quality checklists closing Idiom98. Relative payoff between the four promoted rules is a judgment call the corpus does not quantify.

**Second-order consequence.** Each promoted rule is really a compile-time-or-review-time gate moved earlier, branded types fail at compile, wrapped errors fail loudly at review, injected dependencies fail visibly in test doubles, idempotence makes retries safe by construction.

**Revision decision.** Promote a top tier of four cross-stack rules, boundary-explicit types, contextual error values, constructor-injected dependencies, and idempotent effects, each with its per-stack instantiation named.

**Retained seed evidence.** All scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `polyglot_idiomatic_reference_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local polyglot idiomatic material before synthesizing reference patterns recommendations. |
| `polyglot_idiomatic_reference_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `polyglot_idiomatic_reference_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single claim should orient a builder applying polyglot idioms. The seed thesis repeats the generic load-local-first formula instead of the corpus's actual claim, that idiomatic polyglot code is produced by writing executable specifications first and letting each stack's type system and test harness enforce the idioms.

**Recommended default and causal basis.** Phrase the thesis as evidence-labeled, verification-coupled, stack-classified idiom guidance and keep the three evidence labels on its clauses. Idiom98 opens with the stub-red-green-refactor lifecycle, demonstrates it with parallel TypeScript, Java, and Go order-service implementations, and closes every stack with a checklist the tests and compilers can enforce.

**Operating conditions and assumptions.** The labels stay attached so corpus-derived clauses remain distinguishable from inference. The thesis orients use of this reference for application and pipeline code across the mapped stacks, it does not compress the individual pattern catalogs.

**Failure boundary and alternatives.** A tests-first thesis under-serves infrastructure code, Terraform validation blocks and Kubernetes probes in the corpus are declarative gates, not red-green cycles. Bounded alternatives and recoveries: a catalog-first thesis that treats Idiom96 as the index and Idiom98 as commentary, weaker because it drops the delivery workflow that makes idioms verifiable.

**Counterexample, gotchas, and operational comparison.** Idiom98's order example shows the GREEN phase deliberately omitting validation and logging, quoting GREEN-phase code as final idiom would bless incomplete implementations. Good: writing the failing insufficient-stock test before the order service in all three languages as S01 does. Bad: copying the refactored TypeScript service without its test suite. Borderline: applying red-green to a Terraform module, plan-and-validate approximates but does not equal a failing test.

**Verification, evidence, and uncertainty.** Confirm the thesis clauses each carry an evidence label and trace to a named corpus section. The S01 workflow narrative and the parallel three-language order-service example in Idiom98. How far the tests-first claim generalizes to exploratory or throwaway code is not addressed by the corpus.

**Second-order consequence.** The thesis unifies the catalogs, a branded type, a sealed interface, and a sentinel error are all the same move, making illegal states unrepresentable so the toolchain rejects unidiomatic code before review.

**Revision decision.** Restate the thesis as specification-first polyglot development, Gherkin or test tables define behavior, stack-native types encode invariants, and refactoring happens only behind green gates.

**Retained seed evidence.** The three labeled thesis statements remain preserved beneath the evolved synthesis. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `polyglot_idiomatic_reference_patterns` contains 4 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Polyglot Idiomatic Reference Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which of the four local files to open first for a given polyglot question. The seed map records titles and heading signals but not the reading order that the four files reward, Idiom98 for workflow and depth, Idiom96 for breadth, opencode-genius for production proof, broad-idiomatic-patterns for extraction method.

**Recommended default and causal basis.** Start polyglot tasks in the matching stack section of Idiom98, widen to Idiom96 when the stack section is thin, and reserve the other two files for provenance and extraction questions. Idiom98 is 8,681 lines and carries the only end-to-end worked example, Idiom96 covers the most stacks per line, opencode-genius uniquely ties every pattern to shipped code, and broad-idiomatic-patterns is a 504-line prompt rather than a reference.

**Operating conditions and assumptions.** The task is implementation-oriented, method-of-extraction tasks invert the order and start from broad-idiomatic-patterns. The map orders retrieval inside this theme's four files, it does not rank other idiomatic references in the archive.

**Failure boundary and alternatives.** Heading signals alone mislead here, broad-idiomatic-patterns' headings advertise Rust patterns but the file contains instructions for extracting them, not the patterns themselves. Bounded alternatives and recoveries: collapse the map into one merged index of section identifiers, or keep per-file maps and accept some duplication across the two catalogs.

**Counterexample, gotchas, and operational comparison.** Both Idiom96 and Idiom98 contain a Result type, a retry helper, and a worker pool, citing them interchangeably blurs which file's variant, with or without jitter and abort support, is meant. Good: answering a Kafka consumer question from Idiom98 K.1.2 with its manual-commit listing. Bad: citing broad-idiomatic-patterns as if it contained finished Rust idioms. Borderline: using opencode-genius' deep-merge pattern as general TypeScript guidance, it is one codebase's solution.

**Verification, evidence, and uncertainty.** Spot-check that cited heading signals still exist in the archive files at the recorded paths. Line counts and structural roles observed while reading all four files in full. Whether newer sibling archives supersede these 202602 snapshots is not determinable from this theme's map.

**Second-order consequence.** The four files differ in evidence strength, opencode-genius claims are anchored to a real codebase, Idiom96 and Idiom98 are curated best practice, and broad-idiomatic-patterns asserts nothing, so provenance weight should follow that order even though reading order does not.

**Revision decision.** Add a reading-order column, workflow depth first, catalog breadth second, production provenance third, extraction method last, and flag the prompt-not-catalog nature of the fourth file.

**Retained seed evidence.** All local source rows with their title and heading-signal columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom96-polyglot-basic-patterns-20251205.md | Comprehensive Production-Grade Idiomatic Pattern Libraries | Comprehensive Production-Grade Idiomatic Pattern Libraries; Part 1: TypeScript Pattern Library (400+ Patterns); 1.1 Meta-Principles; Naming Conventions for LLM Tokenization; 8 Non-Negotiable Principles; 1.2 Architecture Principles | historical idiomatic pattern corpus |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom98-Multi-Lang-Notes-20251205.md | S01: Polyglot Development - Core Principles & TDD Workflow | S01: Polyglot Development - Core Principles & TDD Workflow; Philosophy: Idiomatic Code Across Technology Stacks; CRITICAL: NAMING CONVENTIONS (LLM-Optimized); TypeScript/JavaScript; Java/Spring Boot; Golang | historical idiomatic pattern corpus |
| agents-used-monthly-archive/idiomatic-references-202602/broad-idiomatic-patterns.md | CONTEXT | CONTEXT; MISSION; ANALYSIS FRAMEWORK; EXTRACTION INSTRUCTIONS; 1. IDIOMATIC PATTERNS; 2. ANTI-PATTERNS | historical idiomatic pattern corpus |
| agents-used-monthly-archive/idiomatic-references-202602/opencode-genius-idiomatic-patterns.md | OpenCode: Genius-Level Idiomatic Code Patterns | OpenCode: Genius-Level Idiomatic Code Patterns; Executive Summary; Table of Contents; Pattern Details; 1. Hierarchical Multi-Instance State Sync with Event Streaming; 2. Lazy-Initialized Child Store with Owner Capture | historical idiomatic pattern corpus |

## External Research Source Map

**Decision supported.** This section helps decide how much trust an external row may carry in polyglot idiom guidance. The seed map lists the Codex AGENTS.md guide, GitHub Actions docs, and agents.md with the external_research_sourced_fact label even though none of the three URLs was retrieved during this evolution.

**Recommended default and causal basis.** Treat every external claim in this theme as unverified until the specific page is retrieved and its retrieval is recorded with a date. The evolution worked entirely from the local corpus, so the URL rows are candidate leads inherited from the seed generator, not consulted evidence.

**Operating conditions and assumptions.** No retrieval infrastructure or recorded fetch exists for these URLs within this corpus pass. The map inventories candidate external references for future refresh, it confers no authority on them today.

**Failure boundary and alternatives.** Labeling unretrieved links as sourced fact would launder candidates into corroboration and violate the evidence discipline this file teaches. Bounded alternatives and recoveries: perform a scoped retrieval pass in a future cycle, or replace the trio with per-stack authoritative documentation candidates.

**Counterexample, gotchas, and operational comparison.** Docs.github.com/actions is a documentation root, citing a root domain lets any claim hide behind it, future refreshes should cite specific pages. Good: writing needs-retrieval next to a claim that GitHub Actions supports concurrency cancellation. Bad: asserting current AGENTS.md format details from the unretrieved agents.md row. Borderline: using the URL trio to guess theme adjacency, suggestive but unverified.

**Verification, evidence, and uncertainty.** Check that no statement in this file rests solely on one of the three URL rows. The absence of any retrieval record for these URLs in this evolution's working notes. Whether the three URLs resolve today and what they currently say is unknown from the archive.

**Second-order consequence.** Useful external anchors for this theme would be per-stack authorities, the TypeScript handbook, Effective Go, Spring reference docs, Kafka documentation, and Terraform registry docs, none of which the seed lists, revealing the seed's URL trio was copied from an agent-instruction theme.

**Revision decision.** Downgrade each row to unretrieved candidate status and note that only the GitHub Actions URL even overlaps this theme's stacks, matching Idiom96's CI/CD section.

**Retained seed evidence.** All external source rows with their usage-role and boundary-label columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | external_research_sourced_fact |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which failure shapes reviewers should actively hunt in polyglot changes. The seed registry lists three meta-level failures about summarization while the corpus catalogs concrete polyglot anti-patterns, ignored Go errors, Java field injection and mutable POJOs, TypeScript any and boolean state flags, god services, anemic domain models, and fire-and-forget Kafka sends.

**Recommended default and causal basis.** When reviewing polyglot code, scan for the corpus's avoid blocks first, they mark the failure shapes the pattern authors considered most tempting. Idiom98 dedicates an anti-patterns section to god objects, anemic models, temporal coupling, leaky abstractions, primitive obsession, service locators, boolean parameters, and shotgun surgery, and every stack section pairs idioms with avoid blocks.

**Operating conditions and assumptions.** The code under review sits in a stack the corpus covers and review time allows checking replacements, not just flagging. The registry covers coding and messaging anti-patterns evidenced in the mapped corpus, not organizational or process failures.

**Failure boundary and alternatives.** Anti-pattern lists decay into taboo without the paired replacement, the corpus always shows the safer shape beside the bad one and this registry must too. Bounded alternatives and recoveries: encode the mechanical rows into linters, no-explicit-any, golangci-lint errcheck, ArchUnit-style injection rules, and reserve the registry for judgment cases.

**Counterexample, gotchas, and operational comparison.** Panic in Go is listed as anti-pattern only for recoverable errors, initialization-time panics remain idiomatic, blanket bans overcorrect. Good: rejecting a PR where user, _ := GetUser discards the error. Bad: flagging every boolean argument when a two-value option genuinely is binary. Borderline: an anemic DTO at a serialization boundary, records without behavior are correct there.

**Verification, evidence, and uncertainty.** For each registry row, locate the corresponding avoid block or anti-patterns entry in the mapped files. The anti-patterns section of Idiom98 and the avoid blocks distributed through both catalogs. Which anti-patterns actually dominate this repository's history is unmeasured, the registry inherits the corpus's emphasis.

**Second-order consequence.** Most rows reduce to two roots, hidden state and hidden dependencies, boolean flags hide state machines, service locators hide dependencies, anemic models hide invariants, which is why injection and union types keep reappearing as cures.

**Revision decision.** Add per-stack rows pairing each named anti-pattern with its corpus replacement, errors.Is wrapping for ignored errors, constructor injection for field injection, discriminated unions for boolean flags, callback-checked sends for fire-and-forget.

**Retained seed evidence.** All three seed registry rows with their causes, replacements, and detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which command or check proves a given polyglot recommendation was followed. The seed section names one repository verifier while the corpus prescribes per-stack gates, tsc and Vitest with coverage thresholds, JUnit with Testcontainers, go test with golangci-lint and go vet, terraform validate, and Kafka consumer-lag checks.

**Recommended default and causal basis.** Attach the stack's compile, test, and lint trio to every idiom recommendation drawn from this reference. Idiom98 closes each stack with a checklist whose items are tool-enforceable and its TS.0.5 Vitest config sets explicit 80 percent line, function, branch, and statement thresholds.

**Operating conditions and assumptions.** The consuming project already runs CI where these commands can execute, gates that never run are decoration. Gates here verify either this document's invariants or the idioms it recommends, each command must say which.

**Failure boundary and alternatives.** The listed repository verifier checks this reference file's structure, it cannot validate any code claim, conflating document gates with code gates would fake coverage. Bounded alternatives and recoveries: review-question gates for judgment claims that no command can check, such as whether an interface is minimal.

**Counterexample, gotchas, and operational comparison.** Coverage thresholds transplant badly, the corpus's 80 percent Vitest floor is a starting point, enforcing it retroactively on a legacy codebase blocks all merges. Good: gating a Go error-handling change on golangci-lint plus a table-driven test of both error paths. Bad: citing the document verifier as proof a Kafka consumer is idempotent. Borderline: terraform plan as a gate, it proves syntax and diff, not behavior.

**Verification, evidence, and uncertainty.** Run the document verifier for this file and confirm each recommended code gate names a runnable command. The per-stack quality checklists and tool tables in Idiom98 and the CI workflow patterns in Idiom96. Exact tool versions that current projects should pin are outside the archive's knowledge.

**Second-order consequence.** The corpus's idioms are chosen to be gate-visible, branded types make tsc the gate, wrapped errors make errcheck the gate, idempotent producers make broker metrics the gate, so a recommendation lacking any gate is probably not from this corpus.

**Revision decision.** Add a per-stack gate table, compile gate, test gate, lint gate, and operational gate per stack, and keep the document verifier as the file-level gate.

**Retained seed evidence.** The original verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide which corpus slice an agent should load and cite for a polyglot task. The seed guide says start with the local map but not how an agent should choose between the two overlapping catalogs or when to consult the workflow file versus the pattern files.

**Recommended default and causal basis.** Match the task's stack and question type, load only the matching section family, and emit the section identifier alongside every borrowed idiom. The corpus divides cleanly by question type, how-to-implement questions match Idiom96/Idiom98 stack sections, how-to-deliver questions match Idiom98's S01 workflow, how-to-extract questions match broad-idiomatic-patterns, and does-this-work-in-production questions match opencode-genius.

**Operating conditions and assumptions.** The task names its stack or the file extension makes it inferable. The guide steers agents choosing patterns within the mapped stacks, it does not authorize inventing idioms for unmapped languages.

**Failure boundary and alternatives.** An agent following the guide literally could load 12,917 lines of corpus for a one-line idiom question, retrieval must be section-targeted, not file-targeted. Bounded alternatives and recoveries: full-file loading when the task is a broad audit, or external research with explicit labels when the stack is unmapped.

**Counterexample, gotchas, and operational comparison.** The two catalogs disagree in small ways, Idiom96's withRetry lacks the jitter and shouldRetry predicate that Idiom98's version adds, agents must not blend them into an uncited hybrid. Good: an agent citing J.1.2 while adding a sealed OrderEvent hierarchy. Bad: an agent answering a Rust question from the TypeScript sections. Borderline: a MERN question, Idiom96 covers MERN briefly, thin evidence deserves a confidence warning.

**Verification, evidence, and uncertainty.** Inspect agent output for section identifiers and reject uncited idiom claims. The section-numbered structure observed across both catalogs during full reads. How well the routing holds for mixed-stack tasks touching three or more sections at once is untested.

**Second-order consequence.** Section identifiers like TS.1.1 or G.1.3 function as stable citation keys, an agent that quotes them produces auditable recommendations that reviewers can check in seconds.

**Revision decision.** Add a question-type routing list, implement, deliver, extract, validate, each pointing to its file and section family, plus an instruction to quote section identifiers in outputs.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide whether this reference fits the user's journey before they invest reading time. The seed scenario describes a generic uncertain user instead of the concrete journey the corpus serves, a developer landing in an unfamiliar stack of a polyglot codebase who must produce idiomatic code without months of immersion.

**Recommended default and causal basis.** Have the newcomer read their home-stack version of a pattern first, then the target-stack version, then implement behind the target stack's gates. Idiom98's naming conventions section is explicitly LLM-optimized and its parallel three-language order example exists precisely so one behavior can be compared across stacks by someone fluent in only one.

**Operating conditions and assumptions.** Both home and target stacks appear in the corpus and the behavior in question has a catalogued pattern. The journey covers cross-stack onboarding and review within the mapped stacks, not deep single-stack mastery.

**Failure boundary and alternatives.** The journey breaks for a user whose target stack is absent, a Python or Rust-implementation task gets no catalog support here beyond the extraction prompt. Bounded alternatives and recoveries: pairing with a stack-native reviewer when the corpus lacks the pattern, or extracting a new pattern via the broad-idiomatic-patterns schema.

**Counterexample, gotchas, and operational comparison.** Surface translation without idiom translation produces accents, a Go developer writing TypeScript with returned error tuples instead of Result unions has translated words, not idioms. Good: a Java developer porting Optional discipline to TypeScript via strict null checks and unions. Bad: a user expecting Python idioms from this corpus. Borderline: a DevOps engineer using only section D, valid but narrow.

**Verification, evidence, and uncertainty.** Ask whether the user can name their home stack, target stack, and the behavior to translate, three yes answers confirm fit. The S01 cross-language example set and the LLM-optimized naming rationale in Idiom98. How long the translation approach takes a real newcomer versus immersion is unmeasured.

**Second-order consequence.** The parallel order-service example is a Rosetta stone, mapping Result types to sealed interfaces to error returns teaches the translation function once, after which any pattern can be ported by analogy.

**Revision decision.** Recast the scenario as cross-stack translation, the user knows behavior X in their home stack and uses the parallel examples to express it idiomatically in the target stack.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The new contributor or agent is starting from an unfamiliar theme and deciding whether this reference is the right tool and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `polyglot_idiomatic_reference_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what to load, what to trust, what to avoid, and what evidence proves success.
Reference opening trigger: Open this file when the task mentions polyglot idiomatic reference patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide whether to adopt, adapt, or avoid a catalogued idiom given the surrounding code's conventions. The seed guide frames adopt, adapt, avoid abstractly without the corpus's concrete tension, catalog fidelity versus target-codebase consistency when the surrounding repository already deviates from the catalogued idiom.

**Recommended default and causal basis.** Adopt catalog idioms verbatim in greenfield code, adapt to the established local dialect in brownfield code, and avoid the catalog where the stack is unmapped. The corpus itself encodes adaptations, Idiom98 presents both a hand-rolled Result namespace and the neverthrow library for the same need, and opencode-genius shows production code choosing bespoke solutions over textbook shapes.

**Operating conditions and assumptions.** The repository's existing conventions are discoverable and reasonably uniform. The guide arbitrates pattern-level choices, repository-wide convention changes need a migration decision outside this reference.

**Failure boundary and alternatives.** Adopting catalog idioms file-by-file inside a codebase with a different established convention produces two dialects, which the corpus's shotgun-surgery anti-pattern warns costs every future change. Bounded alternatives and recoveries: declare a bounded migration, one module converted per cycle behind gates, when the local dialect is worth replacing.

**Counterexample, gotchas, and operational comparison.** Consistency-first can entrench a harmful local convention, ignored errors are never worth preserving for uniformity, safety rules outrank dialect. Good: keeping a repo's existing neverthrow usage instead of introducing the hand-rolled Result. Bad: mixing both Result styles in one service. Borderline: introducing branded types into a repo of plain string IDs, high value but a visible dialect break.

**Verification, evidence, and uncertainty.** Sample three neighboring files before adopting and record which branch, adopt, adapt, or avoid, was taken and why. The duplicate-solution pairs present within the corpus and the anemic and shotgun-surgery costs it documents. Where exactly local-consistency deference should stop for borderline-harmful conventions is judgment.

**Second-order consequence.** Adapt is the dominant real-world branch, the corpus's own pairs, hand-rolled versus neverthrow, EmbeddedKafka versus Testcontainers, Jest versus Vitest, show the authors expected calibration to context rather than copying.

**Revision decision.** Add a fourth column asking what the surrounding code already does, and rule that local consistency beats catalog fidelity until a deliberate migration is declared.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the polyglot idiomatic reference patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong polyglot idiomatic reference patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which file's variant wins when the mapped sources overlap on a pattern. The seed hierarchy crowns Idiom96 canonical and demotes the other three to legacy, but Idiom98 is the deeper and more operational text, the only one with a delivery workflow, executable specifications, and per-stack quality gates.

**Recommended default and causal basis.** Resolve any conflict between the two catalogs toward Idiom98's variant unless the task specifically needs Idiom96's wider stack coverage. Full reads show Idiom96 is a wide catalog while Idiom98 subsumes most of its stacks and adds the S01 TDD workflow, contract documentation, and 8,681 lines of worked patterns.

**Operating conditions and assumptions.** The disagreement is a variant difference, true contradictions, none observed in full reads, would need explicit adjudication. The hierarchy governs precedence when the four mapped files disagree, it does not rank them for other themes.

**Failure boundary and alternatives.** Canonical-versus-legacy is the wrong axis here, the four files rarely conflict, they occupy different roles, so demotion language suggests staleness that reading does not confirm. Bounded alternatives and recoveries: maintain a merged pattern index with one winning variant per pattern name, higher upkeep but eliminates repeat adjudication.

**Counterexample, gotchas, and operational comparison.** Opencode-genius patterns look canonical because they shipped, but they encode one product's constraints, quota-aware localStorage eviction is not a general storage idiom. Good: choosing Idiom98's withRetry with jitter over Idiom96's plain exponential version. Bad: dismissing Idiom98 as legacy because the seed row says so. Borderline: preferring opencode-genius' deep merge for a settings migrator, its provenance matches that exact use.

**Verification, evidence, and uncertainty.** For each precedence claim, cite the two overlapping sections and the observed difference between them. Side-by-side comparison of overlapping patterns performed during the full reads. File dates alone cannot settle which catalog reflects later thinking, both carry the same 20251205 stamp.

**Second-order consequence.** Where the catalogs do overlap, Idiom98's variant is consistently the more defensive one, retry gains jitter and predicates, tests gain mock scaffolding, producers gain delivery timeouts, so overlap resolution can default to Idiom98.

**Revision decision.** Re-role the rows, Idiom98 canonical for workflow and depth, Idiom96 canonical for breadth and stacks Idiom98 lacks, opencode-genius supporting with production provenance, broad-idiomatic-patterns supporting as method.

**Retained seed evidence.** All hierarchy rows with their heading signals and reviewer questions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom96-polyglot-basic-patterns-20251205.md | canonical primary source | Comprehensive Production-Grade Idiomatic Pattern Libraries; Part 1: TypeScript Pattern Library (400+ Patterns); 1.1 Meta-Principles | What guidance, warning, or example should this source contribute to Polyglot Idiomatic Reference Patterns? |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom98-Multi-Lang-Notes-20251205.md | legacy historical source | S01: Polyglot Development - Core Principles & TDD Workflow; Philosophy: Idiomatic Code Across Technology Stacks; CRITICAL: NAMING CONVENTIONS (LLM-Optimized) | What guidance, warning, or example should this source contribute to Polyglot Idiomatic Reference Patterns? |
| agents-used-monthly-archive/idiomatic-references-202602/broad-idiomatic-patterns.md | legacy historical source | CONTEXT; MISSION; ANALYSIS FRAMEWORK | What guidance, warning, or example should this source contribute to Polyglot Idiomatic Reference Patterns? |
| agents-used-monthly-archive/idiomatic-references-202602/opencode-genius-idiomatic-patterns.md | legacy historical source | OpenCode: Genius-Level Idiomatic Code Patterns; Executive Summary; Table of Contents | What guidance, warning, or example should this source contribute to Polyglot Idiomatic Reference Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what shape a new polyglot pattern must take before this reference may recommend it. The seed artifact table asks for a freshness workflow in the abstract while this theme's natural artifact is a per-stack idiom card, pattern name, layer, context, snippet, rationale, anti-pattern, and provenance, exactly the JSON schema broad-idiomatic-patterns defines.

**Recommended default and causal basis.** When this theme gains a new pattern, capture it as an eight-field card with layer classification and a named source before citing it in guidance. Broad-idiomatic-patterns specifies that extraction schema field by field, and opencode-genius demonstrates the filled-in form, twelve patterns each carrying problem, solution, and provenance.

**Operating conditions and assumptions.** The pattern was observed in real code or an authoritative document that the provenance field can name. The artifact standardizes how new polyglot patterns enter this theme, it does not replace the existing catalogs.

**Failure boundary and alternatives.** An artifact without the anti-pattern and provenance fields degrades into a snippet dump, the two fields are what make a card reviewable and refreshable. Bounded alternatives and recoveries: free-form pattern notes for exploratory captures, accepted only as drafts until carded.

**Counterexample, gotchas, and operational comparison.** The schema's solution_snippet demands a minimal verified example, pasting a 100-line listing defeats the card's review-in-seconds purpose. Good: a card for Go functional options citing G.1.3 with a ten-line snippet. Bad: a pattern claim with no provenance field. Borderline: a card whose provenance is an unretrieved URL, admissible as candidate only.

**Verification, evidence, and uncertainty.** Check candidate cards for all eight fields and a provenance that resolves to a readable source. The extraction schema in broad-idiomatic-patterns and its instantiation across opencode-genius. Whether card upkeep survives contact with real refresh cycles is untested in this repository.

**Second-order consequence.** The card schema doubles as a freshness mechanism, because provenance names a file or URL, a refresh cycle can re-check each card's source instead of re-reading whole corpora.

**Revision decision.** Replace the abstract artifact rows with the eight-field idiom card contract and require a filled example before the artifact counts as complete.

**Retained seed evidence.** The artifact field rows with their completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: reference freshness workflow with canonical source policy and update checklist.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Polyglot Idiomatic Reference Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which worked example a reader should replay to learn this reference's method. The seed examples speak generically about loading sources while the corpus contains a ready-made worked spine, the order-creation service specified in Gherkin and implemented in TypeScript, Java, and Go through the stub, red, green, and refactor phases.

**Recommended default and causal basis.** Study the GREEN-to-REFACTOR diff of the order example in your target stack before writing new service code against this reference. Idiom98 walks that single behavior end to end, failing tests for success and insufficient-stock paths, a minimal GREEN implementation, then a REFACTOR adding validation, correlation IDs, compensation, and structured logs.

**Operating conditions and assumptions.** The reader's task resembles a service behavior with success and failure paths. Worked examples here illustrate how to consume this reference, they are not tutorials replacing the corpus listings.

**Failure boundary and alternatives.** The order example is application-shaped, it exercises none of the Terraform, Kubernetes, or GitHub Actions idioms, so it cannot serve as the sole worked example for the infrastructure half of the corpus. Bounded alternatives and recoveries: for messaging tasks substitute the Kafka producer-consumer pair of K.1.1 and K.1.2 as the worked spine.

**Counterexample, gotchas, and operational comparison.** The Gherkin scenarios use SHALL and SHALL NOT clauses that double as assertions, dropping the SHALL NOT lines when borrowing the format silently deletes the negative tests. Good: reimplementing the insufficient-stock rejection in a fourth stack behind the same Gherkin spec. Bad: skipping RED and copying the refactored listing directly. Borderline: using the example's compensation logic verbatim, saga-style compensation may be overkill for a single-store transaction.

**Verification, evidence, and uncertainty.** Rerun the borrowed tests and confirm both the success and the SHALL NOT failure scenarios execute. The complete order-service lifecycle and its Gherkin background in Idiom98's S01 sections. How faithfully the three parallel implementations were kept in sync by the original authors is unverifiable.

**Second-order consequence.** The REFACTOR delta is the real lesson, comparing GREEN and refactored versions shows exactly which concerns, validation, compensation, observability, idiomatic code adds beyond passing tests.

**Revision decision.** Anchor the good example on the order-service spine with its section citations, and add an infrastructure counterpart, the EKS module with typed, validated variables from section D.1.1.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Polyglot Idiomatic Reference Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Polyglot Idiomatic Reference Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Polyglot Idiomatic Reference Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which signals show this reference is earning its maintenance cost. The seed metrics name a generic leading indicator while the corpus defines measurable per-stack outcomes, coverage thresholds, lint cleanliness, consumer lag, and p50/p99 latency budgets that could feed this section directly.

**Recommended default and causal basis.** Record after each reference-driven task whether the recommended idiom shipped, was adapted, or was rejected, and why. Idiom98's performance checklist demands P50 and P99 requirements with critical-path tests, its Vitest config encodes 80 percent thresholds, and its Kafka checklist names consumer lag and partition distribution as standing monitors.

**Operating conditions and assumptions.** Tasks actually declare when this reference guided them, otherwise the loop starves. This section tracks whether the reference improves decisions, the code metrics it borrows are evidence sources, not this document's own KPIs.

**Failure boundary and alternatives.** Gate metrics measure code health, not reference health, a repo can be lint-clean while this document goes stale, so document-level and code-level loops must stay separate. Bounded alternatives and recoveries: periodic audit sampling of merged polyglot changes against the anti-pattern registry when task-level recording proves too heavy.

**Counterexample, gotchas, and operational comparison.** Coverage percentages saturate, once a repo sits at threshold the metric stops moving and reviewers must sample test quality instead. Good: logging that G.1.1 wrapping was adopted in three services this cycle. Bad: claiming reference success from a green CI badge alone. Borderline: counting section citations in commit messages, easy to game but cheap to collect.

**Verification, evidence, and uncertainty.** Review the journal for shipped-adapted-rejected records tied to section identifiers each cycle. The threshold and monitoring values stated across the Idiom98 quality checklists. The causal share of the reference versus reviewer skill in any improvement is unmeasurable here.

**Second-order consequence.** Citation frequency of section identifiers in review comments is a cheap proxy for reference usefulness, zero citations over a cycle signals either full internalization or abandonment, and the follow-up question distinguishes them.

**Revision decision.** Define two loops, a document loop sampling whether citations of this file led to accepted idiomatic changes, and a code loop reusing the corpus's gate metrics as adoption evidence.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next task uses the reference to make a better decision with less ambiguity.
Failure signal: the reference remains a source map and never becomes an operating guide.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide whether this reference is complete enough to accept, reuse, or refresh. The seed checklist verifies the reference's own sections exist but never checks the property this theme lives on, that each recommended idiom carries stack, layer, section citation, and gate.

**Recommended default and causal basis.** Run the claim-level checklist during every reread pass and refuse acceptance while any idiom claim lacks its four attributes. The corpus binds every pattern to those four attributes, section identifiers classify stack and layer while use-when lines and avoid blocks supply conditions and gates.

**Operating conditions and assumptions.** The file remains small enough for a manual claim sweep, roughly its current size. The checklist audits this reference file before reuse or refresh, not the codebases that consume it.

**Failure boundary and alternatives.** A checklist of section presence can pass on a hollow document, completeness here must mean claim-level auditability, not heading-level coverage. Bounded alternatives and recoveries: automate the citation check with a script grepping for section-identifier patterns near idiom keywords.

**Counterexample, gotchas, and operational comparison.** Checklists rot fastest at their newest items, the claim-level additions need the same verifier discipline as the structural ones or they become aspirational. Good: rejecting acceptance because one retry recommendation lacked a gate. Bad: passing the file because all 26 headings exist. Borderline: an idiom cited to a whole file rather than a section, weak but traceable.

**Verification, evidence, and uncertainty.** Sweep the evolved sections and count idiom claims missing any of the four attributes, zero is the pass bar. The attribute structure observed uniformly across both catalogs during full reads. Whether claim-level auditing stays affordable as the reference grows is untested.

**Second-order consequence.** The four claim-level attributes mirror the eight-field idiom card, so the checklist and the artifact contract converge, one audits stock, the other admits new inventory.

**Revision decision.** Add claim-level items, every idiom names its stack, cites a section identifier, states a use-when condition, and attaches a runnable or reviewable gate.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Polyglot Idiomatic Reference Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send a task this polyglot reference cannot finish. The seed routing derives three adjacents by splitting the theme name into polyglot, idiomatic, and reference tokens instead of routing by the real neighboring surfaces, single-stack depth, agent instruction files, and extraction methodology.

**Recommended default and causal basis.** When a task needs more than the catalogued variants of a pattern, hand off to the single-stack reference for that language rather than stretching this file. Tasks leave this theme in three observed directions, deeper into one stack than the catalogs go, outward to AGENTS.md-style agent instruction concerns the seed URLs hint at, or methodward into pattern extraction which broad-idiomatic-patterns serves.

**Operating conditions and assumptions.** A destination reference actually exists in the corpus for the stack or concern in question. Routing hands off tasks this reference cannot serve, it does not summarize the destinations.

**Failure boundary and alternatives.** Token-derived adjacents are circular, they route the reader back to this same theme under a synonym and waste the escape hatch this section exists to provide. Bounded alternatives and recoveries: external documentation with explicit unverified labels when no internal destination exists.

**Counterexample, gotchas, and operational comparison.** Routing away too early forfeits the cross-stack translation value that is this theme's unique contribution, check the parallel examples before leaving. Good: sending a Kafka Streams windowing deep-dive to a dedicated messaging reference. Bad: routing polyglot to idiomatic, the same shelf twice. Borderline: sending Rust questions to broad-idiomatic-patterns, it holds method, not answers.

**Verification, evidence, and uncertainty.** Test each route by confirming the named destination file exists and covers the handed-off concern. The coverage boundaries observed across the four mapped files during full reads. The actual distribution of outbound task directions is estimated from corpus shape, not measured traffic.

**Second-order consequence.** The most frequent handoff is depth, the catalogs give one to three variants per pattern while real tasks eventually need the stack's full option space, so the depth route deserves first position.

**Revision decision.** Route single-stack depth to the per-language references in the idiomatic-ref corpus, agent-instruction tasks to the documentation-theme references, and extraction tasks to the broad-idiomatic-patterns prompt itself.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use the nearest language, workflow, agent, or documentation reference when the theme becomes concrete.
Adjacent reference 1: consider the polyglot adjacent reference when the current task pivots away from polyglot idiomatic reference patterns.
Adjacent reference 2: consider the idiomatic adjacent reference when the current task pivots away from polyglot idiomatic reference patterns.
Adjacent reference 3: consider the reference adjacent reference when the current task pivots away from polyglot idiomatic reference patterns.

## Workload Model

**Decision supported.** This section helps decide how much corpus a single task may load before it must be split. The seed model bounds work at twelve source documents per use without reflecting this theme's real load shape, one enormous workflow file, one large catalog, and two small satellites totaling 12,917 lines that must never be loaded whole for a point question.

**Recommended default and causal basis.** Budget one stack family and one question type per reference use, and split tasks that need more into sequenced passes. Full reads measured the imbalance, Idiom98 alone is 67 percent of the theme's lines, so retrieval cost is dominated by whether section targeting works, not by document count.

**Operating conditions and assumptions.** Section identifiers remain stable in the archive so targeted retrieval keeps working. The model budgets reading and synthesis effort for tasks using this theme, not general repository work.

**Failure boundary and alternatives.** A document-count budget misprices the work, twelve small files are cheaper than one untargeted read of Idiom98. Bounded alternatives and recoveries: precomputed per-stack digests if repeated tasks show the same families being reloaded.

**Counterexample, gotchas, and operational comparison.** Cross-stack translation tasks legitimately need two families, home and target stack, the budget must allow that pair without treating it as scope creep. Good: loading only G.1 for a Go error-handling review. Bad: reading all of Idiom98 to answer one Vitest threshold question. Borderline: loading TS plus Java families for a port, allowed as a translation pair.

**Verification, evidence, and uncertainty.** Record loaded section families per task in the journal and flag tasks exceeding the pair budget. The measured line counts and section structure of the four mapped files. Optimal budget for audit-class tasks that genuinely need breadth remains a judgment call.

**Second-order consequence.** The corpus's section-identifier scheme is effectively an index built for this budget, honoring it converts a 12,917-line theme into a few-hundred-line working set per task.

**Revision decision.** Restate the capacity bound in section families, one stack section family plus at most one workflow section per task, escalating to multi-family loads only for audits.

**Retained seed evidence.** The workload dimension rows with their boundary values and pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Polyglot Idiomatic Reference Patterns as a documentation reference operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | reference selection, writing, roadmap, or explanation work where the output should improve the next human or agent decision | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one audience, one decision, up to 12 source documents, and one verification checklist per reference use | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Comprehensive Production-Grade Idiomatic Pattern Libraries; Part 1: TypeScript Pattern Library (400+ Patterns); 1.1 Meta-Principles; Naming Convention | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is reference freshness workflow with canonical source policy and update checklist | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable bar this reference's guidance must clear before reuse. The seed targets track label preservation and routing accuracy but omit the reliability property the corpus itself engineers for, that recommended idioms fail safe under partial failure, retries bounded, offsets committed after processing, reservations compensated.

**Recommended default and causal basis.** Reject any recommendation from this reference that touches a failure path but omits its bound, retry cap, timeout, compensation, or dead-letter route. Idiom98's refactored order service compensates inventory reservations when persistence fails, its Kafka consumer acknowledges only after idempotency-checked processing, and both retry helpers cap attempts and delay.

**Operating conditions and assumptions.** Reviewers actually read the failure-path clauses rather than pattern names alone. Targets here measure the reference's guidance quality, runtime SLOs belong to the consuming systems.

**Failure boundary and alternatives.** Document-level reliability targets cannot certify runtime behavior, this section can only require that recommendations carry their fail-safe conditions, not that deployments honor them. Bounded alternatives and recoveries: spot audits of merged changes against the fail-safe clause when systematic sampling is unstaffed.

**Counterexample, gotchas, and operational comparison.** Sampled-accuracy targets like 18 of 20 need someone to collect the sample, absent a sampling owner the target is fiction. Good: a retry recommendation naming five attempts, jitter, and a shouldRetry predicate. Bad: recommending retries with no cap. Borderline: citing a dead-letter topic without its FixedBackOff parameters, directionally safe but unbounded on paper.

**Verification, evidence, and uncertainty.** Sweep evolved sections for failure-path claims and check each names its bound. The compensation, acknowledgment, and backoff listings in Idiom98's order and Kafka sections. Whether guidance-level bounds translate into deployed bounds depends on consumers this file cannot observe.

**Second-order consequence.** The corpus treats reliability as a property of idiom choice, an idempotent producer plus manual commit makes at-least-once delivery safe by construction, so guidance completeness is a genuine upstream reliability control.

**Revision decision.** Add a target that 100 percent of failure-path recommendations name their bounded behavior, max attempts, compensation step, or acknowledgment condition, verifiable by reading the guidance.

**Retained seed evidence.** All four seed reliability rows with thresholds and collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failure shapes deserve standing mitigations when this reference drives work. The seed table lists document-drift failures but not the dominant failure of polyglot references, cross-stack blending, where an idiom valid in one stack is transplanted into another that has a different native shape.

**Recommended default and causal basis.** When any output from this reference looks plausible but uncited, treat it as a suspected blend and re-derive it from a named section. The corpus exists to prevent exactly that, it shows Optional is a return-type idiom in Java but an anti-pattern for parameters, and that panic is unacceptable for recoverable Go errors while exceptions are normal in Java.

**Operating conditions and assumptions.** Reviewers know the section-identifier scheme well enough to demand and check citations. The table catalogs failures of using this reference, not general production incident taxonomy.

**Failure boundary and alternatives.** Blending is hard to detect in review because transplanted code often compiles and passes shallow tests, only stack-native reviewers or lint rules catch the accent. Bounded alternatives and recoveries: per-stack linters encode some mitigations mechanically, errcheck catches ignored errors regardless of reviewer attention.

**Counterexample, gotchas, and operational comparison.** Mitigations that require rereading whole files will be skipped under deadline, mitigations must be citation-sized to survive. Good: catching a returned-error-tuple pattern in a TypeScript PR as Go blending. Bad: shipping the GREEN order service with its known-missing validation. Borderline: mixing the two catalogs' retry variants, mostly harmless but uncitable.

**Verification, evidence, and uncertainty.** Audit a sample of reference-driven changes for the four added failure signatures. The per-stack idiom boundaries and phase-labeled listings observed across the corpus. The base rate of blending in this repository's actual polyglot changes is unmeasured.

**Second-order consequence.** All four added failures share one mechanism, provenance loss, the guidance detached from its stack, phase, retrieval status, or file of origin, so the single mitigation family is mandatory citation.

**Revision decision.** Add rows for cross-stack blending, GREEN-phase code quoted as final, unretrieved-URL laundering, and catalog-variant mixing, each with its trigger and mitigation.

**Retained seed evidence.** All four seed failure rows with triggers and mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| decision path remains implicit | reader cannot tell when to adopt, adapt, or avoid the pattern | add decision table, cost of being wrong, and adjacent-reference route |
| large corpus becomes list | many sources are indexed but not synthesized into ranked guidance | classify canonical, supporting, legacy, duplicate, and conflicting sources |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed operation may be retried and when it must escalate instead. The seed guidance covers retrying failed verification of this document but not the retry discipline the corpus prescribes for code, exponential backoff with jitter, retry predicates on error class, bounded attempts, and dead-letter escalation.

**Recommended default and causal basis.** Recommend retries only alongside their idempotence story, an idempotency key, an idempotent producer, or a naturally idempotent operation. Idiom98's withRetry adds jitter and a shouldRetry predicate keyed to network errors and 5xx codes, its Kafka error handler pairs FixedBackOff of three attempts with a dead-letter recoverer, and its AsyncQueue bounds concurrency with timeouts.

**Operating conditions and assumptions.** The failing operation's error taxonomy distinguishes transient from permanent classes. This section governs both loops explicitly, document-verification retries and the code retry idioms this reference recommends, kept in separate paragraphs.

**Failure boundary and alternatives.** Retry guidance for documents and for code must not merge, one bounded retry for stale evidence is a research policy, three broker redeliveries is a runtime policy, conflating them confuses both. Bounded alternatives and recoveries: circuit breakers for persistent downstream failure, queue-depth shedding for overload, both present in the corpus's operational sections.

**Counterexample, gotchas, and operational comparison.** Retrying validation errors is pure waste and can mask bugs, the corpus's RetryableException split exists to stop exactly that. Good: retrying a 503 with jittered backoff and five-attempt cap. Bad: retrying a Zod validation failure. Borderline: redelivering a poison message three times before dead-lettering, bounded but still triples the damage of a non-idempotent consumer.

**Verification, evidence, and uncertainty.** Check every recommended retry names its predicate, cap, backoff shape, and idempotence guarantee. The withRetry, DefaultErrorHandler, and AsyncQueue listings read in full in Idiom98. Correct retry budgets for this repository's actual downstreams require measurements the corpus cannot supply.

**Second-order consequence.** Backpressure and idempotence are dual requirements, the corpus caps in-flight requests at five only because idempotence is enabled, retries without idempotent effects convert transient failures into duplicates.

**Revision decision.** Keep the seed's document-loop rules and add the code-loop contract, classify the error, retry only transient classes, back off exponentially with jitter, cap attempts, then escalate to dead-letter or human.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which observability evidence must exist for reference-driven code and for the reference itself. The seed checklist records document-usage evidence but omits the observability contract the corpus attaches to every service idiom, structured JSON logs with correlation IDs, RED metrics, health and readiness probes, and distributed tracing.

**Recommended default and causal basis.** Require every service recommendation from this reference to name its log structure, its metrics trio, and its probe or lag signal before it ships. Idiom98's observability checklist names each of those, its refactored order service threads a correlationId through every log line, and its Kubernetes manifests wire liveness and readiness probes with resource limits.

**Operating conditions and assumptions.** The consuming system has somewhere to send structured logs and metrics, otherwise install that first. This section keeps two ledgers, evidence about uses of this reference, and the code-observability items this reference tells builders to install.

**Failure boundary and alternatives.** Observability advice divorced from the stack becomes boilerplate, probe endpoints matter in Kubernetes deployments, consumer lag matters for Kafka, reviewer-time metrics matter for documents, the checklist must say which applies where. Bounded alternatives and recoveries: OpenTelemetry auto-instrumentation as a floor when hand-threading correlation IDs is not yet feasible.

**Counterexample, gotchas, and operational comparison.** Logging the whole event payload alongside the correlation ID leaks PII into logs, the corpus logs identifiers and counts, not bodies. Good: an order flow traceable by one correlationId across three stacks. Bad: console.log debugging left in a merged service. Borderline: metrics without traces, enough for alerting, thin for diagnosis.

**Verification, evidence, and uncertainty.** Grep recommended-service code for correlation-ID threading and confirm probe endpoints respond in deployment manifests. The observability checklist, the correlationId-threaded service listing, and the probe-bearing manifests in the corpus. Appropriate retention and cardinality budgets for logs and metrics are deployment-specific and outside the corpus.

**Second-order consequence.** Correlation IDs are the polyglot glue, the same request ID crossing a TypeScript gateway, a Java service, and a Kafka topic is what makes multi-stack failures diagnosable at all, which is why the corpus threads it through the REFACTOR phase rather than leaving it to operations.

**Revision decision.** Retain the document ledger and add the code ledger, correlation-ID logging, RED metrics, probes, tracing, and consumer-lag monitors, each tagged with its applicable stack.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how a performance claim tied to this reference gets proven or rejected. The seed method measures reviewer navigation time but not the performance discipline the corpus builds into its idioms, P50/P99 latency requirements with critical-path tests, N+1 query avoidance, connection pooling, caching, and pagination.

**Recommended default and causal basis.** Verify structural performance idioms by inspection first, and demand percentile measurements only where a stated latency target exists. Idiom98's performance checklist demands defined P50 and P99 targets with tests on critical paths, its JPA section exists largely to kill N+1 queries with fetch joins, and its Kafka producer config tunes batching, linger, and compression for throughput.

**Operating conditions and assumptions.** The recommendation actually sits on a latency- or throughput-critical path, cold paths need no percentile ceremony. This section verifies performance claims made by guidance from this reference, actual load testing belongs to the consuming project.

**Failure boundary and alternatives.** Document navigation speed and code latency are different quantities, a ten-minute review target says nothing about a 300ms P99, the method must keep the two measurements apart. Bounded alternatives and recoveries: profiling sessions when a target is missed and no structural idiom is obviously absent.

**Counterexample, gotchas, and operational comparison.** Batching raises throughput while raising per-message latency, the corpus's linger.ms of ten milliseconds is a traded cost, quoting the throughput without the latency cost misrepresents it. Good: adding a fetch join and showing the query count drop from N+1 to one. Bad: claiming a service is fast because it uses the recommended patterns. Borderline: enforcing an 80 percent coverage threshold on a performance test suite, coverage mismeasures benchmark value.

**Verification, evidence, and uncertainty.** For each performance recommendation, record the structural idiom present and, where a target exists, the measured percentile against it. The performance checklist, JPA fetch-join listings, and tuned producer configuration in the corpus. Concrete latency budgets for this repository's services are unknown to the corpus and must come from owners.

**Second-order consequence.** Most corpus performance idioms are structural rather than tuning, pooling, pagination, fetch joins, and async processing move complexity classes, so verifying their presence is cheaper and more durable than benchmarking constants.

**Revision decision.** Keep the reviewer-time gate for the document and add the code gate, any performance-relevant recommendation must name its target percentile, its measurement point, and the corpus idiom that serves it.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail condition lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require the reader to find the correct next action in 10 minutes or less during review sampling.
Leading indicator to measure: the next task uses the reference to make a better decision with less ambiguity.
Failure signal to watch: the reference remains a source map and never becomes an operating guide.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when a scaling question has outgrown this reference and must move to system-design ground. The seed statement bounds document scale but not the scale seams the corpus marks in code, worker pools sized by explicit counts, queues with declared concurrency and timeouts, partition-keyed Kafka topics, and autoscaling bounded by HPA min and max.

**Recommended default and causal basis.** Adopt the corpus's bounded shapes with locally derived numbers and escalate to system-design references when coordination must cross service or cluster boundaries. Every concurrency idiom in the corpus carries an explicit bound, the Go worker pool takes numWorkers, the AsyncQueue takes a concurrency option, the EKS node groups declare min, max, and desired sizes with at least two subnets for availability.

**Operating conditions and assumptions.** Load characteristics are known well enough to size pools and partitions deliberately. This section states where this reference's guidance stops scaling, both as a document and in the systems it advises.

**Failure boundary and alternatives.** Bounded-by-default breaks when the bound is guessed, a worker count copied from an example encodes the example's machine, not the deployment's, bounds must be derived or measured. Bounded alternatives and recoveries: vertical scaling within one bounded worker before adding horizontal complexity, often sufficient at this repository's scale.

**Counterexample, gotchas, and operational comparison.** Kafka ordering holds only within a partition, scaling consumers past partition count idles them and scaling partitions breaks key ordering assumptions, both edges are invisible until hit. Good: sizing a worker pool from measured throughput per worker. Bad: promising exactly-once semantics across two independent brokers from this corpus. Borderline: HPA on CPU for a latency-sensitive service, bounded but often the wrong signal.

**Verification, evidence, and uncertainty.** Check every recommended concurrency construct declares its bound and the bound's derivation. The explicitly parameterized pool, queue, node-group, and autoscaler listings across the corpus. The traffic level at which this repository's services would hit these seams is unknown here.

**Second-order consequence.** The corpus's scaling story is compositional, idempotence plus partitioning plus bounded pools lets each component scale independently, which is why none of its patterns require global coordination, and tasks that do require it have left this reference's territory.

**Revision decision.** Add the code-scale clause, this reference covers single-service and single-cluster idioms, multi-region delivery, cross-cluster ordering, and exactly-once across systems exceed its evidence.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Polyglot Idiomatic Reference Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which searches will efficiently reveal that this reference has gone stale. The seed queries recycle the theme name verbatim, which will retrieve directory listings rather than the stack-specific developments that would actually age this reference, new TypeScript and Java language features, Go releases, and Kafka semantics changes.

**Recommended default and causal basis.** Run the per-stack version probes each refresh cycle and update or caveat any claim whose pinned version is no longer current practice. The corpus's claims are pinned to versioned features, satisfies from TypeScript 4.9, records and sealed types from Java 17 and 21, errors.Join from Go 1.20, and 2024-2025 tool choices like Vitest and ArgoCD, each a natural staleness probe.

**Operating conditions and assumptions.** Refresh time is bounded, probes are ordered by aging speed, tools first, language features second, protocol semantics last. Queries here schedule staleness checks for this file's claims, they do not commission new pattern research.

**Failure boundary and alternatives.** A refresh driven by theme-name queries would confirm the reference exists without testing whether any pinned claim has been superseded. Bounded alternatives and recoveries: subscribing to per-stack release notes instead of query-based refresh, steadier but higher standing cost.

**Counterexample, gotchas, and operational comparison.** Newer language features do not automatically deprecate catalogued idioms, branded types survived multiple TypeScript releases, the probe question is superseded, not merely older. Good: a probe finding Go added structured error joining and updating G.1.1 guidance. Bad: re-running the theme-name query and logging no change. Borderline: probing MERN currency, the corpus's coverage there is already thin.

**Verification, evidence, and uncertainty.** Record each probe, its date, and the claim it confirmed or invalidated in the refresh journal. The version-pinned features and dated tool table observed across the corpus. Release cadences shift, the probe ordering by aging speed is an estimate.

**Second-order consequence.** The tool-recommendation table is the fastest-aging asset in the corpus, checking whether Vitest, Zod, Gradle Kotlin DSL, golangci-lint, and ArgoCD remain primary choices is a one-table probe that indicates overall freshness.

**Revision decision.** Replace the generic trio with versioned probes, one per stack, current TypeScript release features, current Java LTS pattern-matching status, current Go error-handling additions, current Kafka exactly-once and queue semantics, and current recommended testing stacks.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | polyglot idiomatic reference patterns official documentation best practices |
| `github_repository_query_phrase` | polyglot idiomatic reference patterns GitHub repository examples |
| `release_notes_query_phrase` | polyglot idiomatic reference patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide which statements in this file may be reused, with what caveats, and which must stay quarantined. The seed notes define the three labels but not this evolution's actual boundary facts, four local files read in full, three external URLs left unretrieved, and all cross-stack synthesis marked as inference.

**Recommended default and causal basis.** Before reusing any claim from this file, check its label, local facts may be cited with their section, inferences must travel with their reasoning, external candidates must not travel at all. Every evolved claim above traces to the full reads of Idiom96, Idiom98, broad-idiomatic-patterns, and opencode-genius, while no external retrieval occurred, so the local and inference labels carry the entire file.

**Operating conditions and assumptions.** The archive files remain at their recorded paths so local facts stay re-checkable. These notes bound what this document may assert, they are the last gate before any claim is reused elsewhere.

**Failure boundary and alternatives.** The strongest-looking claims here, that idioms converge across stacks on explicitness and bounded failure, are combined inference, presenting them as sourced fact would overstate the corpus. Bounded alternatives and recoveries: tightening to per-claim footnotes if label-level discipline proves too coarse for future disputes.

**Counterexample, gotchas, and operational comparison.** Opencode-genius facts are local-corpus facts about one external codebase, a subtle double boundary, they prove what that codebase did, not what its upstream project does today. Good: reusing the manual-commit idiom with its K.1.2 citation. Bad: quoting the agents.md row as evidence about instruction formats. Borderline: reusing the cross-stack convergence thesis, sound inference but inference nonetheless.

**Verification, evidence, and uncertainty.** Sample ten claims from the evolved sections and confirm each carries the correct label class. The read ledger of this evolution, 1,772 plus 8,681 plus 504 plus 1,960 lines read, zero external retrievals. Future readers cannot re-verify the reading effort itself, only the traceability it left behind.

**Second-order consequence.** Boundary notes make refresh cheap, because unretrieved candidates are already marked, a future cycle knows precisely which claims a retrieval pass could upgrade and which are settled local facts.

**Revision decision.** State the read ledger explicitly, per-file line counts and full-read status, the unretrieved status of all three URLs, and the rule that section identifiers accompany every local fact.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
